"""How assets/art/ was made.

This is a record, not something you need to run. It lifts the line art off the
photo of the save-the-date card and writes the transparent PNGs the site uses.
It needs that original photo, so point CARD below at it if you ever want to
re-cut a piece (different crop, different colour, higher resolution).

Needs: pip install opencv-python numpy pillow

Lift the line art off the save-the-date card into clean transparent PNGs.

The card is a photo, so each piece is: separate ink from paper, un-blend the
colour, optionally keep only one hue family (to drop the blue waves that sit
beside the kolam), recolour to the site palette, upscale, save RGBA.
"""
import cv2
import numpy as np
from PIL import Image

CARD = "save-the-date.jpg"      # the original card photo

# The crops that produced assets/art, as (left, top, right, bottom) fractions
# of the card. Reproduce them with:
#
#   piece((0.150, 0.226, 0.786, 0.394), "assets/art/hero-chennai.png",
#         factor=3.6, bg_radius=17, floor_pct=5, mode="palette", crisp=.30,
#         speck=10, thin=1.12,
#         cut=[(0.80, 0, 1, 0.13), (0.94, 0, 1, 0.34), (0.86, 0, 1, 0.10)])
#
#   piece((0.375, 0.700, 0.640, 0.830), "assets/art/kolam.png", factor=3.8,
#         bg_radius=13, floor_pct=6, gain=0.92, keep="warm", solid=GOLD,
#         crisp=.26, speck=4, thin=1.45, min_alpha=0.10,
#         cut=[(0, 0.74, 0.16, 1), (0.72, 0.72, 1, 1)])
#
#   piece((0.545, 0.150, 0.890, 0.286), "assets/art/sprig.png", factor=4.0,
#         bg_radius=15, floor_pct=5, mode="palette", crisp=.30, speck=10,
#         thin=1.12, cut=[(0, 0.56, 0.46, 1), (0.33, 0.82, 0.62, 1),
#                         (0, 0.90, 1, 1), (0, 0.10, 0.11, 0.40)])
#
# Then quantize each result (PIL, FASTOCTREE, 32-96 colours) to keep it small.

GOLD = (0xC0, 0xA0, 0x62)
SAGE = (0x9F, 0xB4, 0x9E)
SEA = (0xA6, 0xC4, 0xD4)


def load():
    im = cv2.imread(CARD, cv2.IMREAD_COLOR)
    return cv2.cvtColor(im, cv2.COLOR_BGR2RGB).astype(np.float32)


def matte(rgb, bg_radius=17, floor_pct=3.0, gain=1.0):
    lum = rgb.mean(axis=2)
    k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (bg_radius, bg_radius))

    def paper_of(ch):
        return cv2.GaussianBlur(cv2.morphologyEx(ch, cv2.MORPH_CLOSE, k), (0, 0),
                                bg_radius / 3.0)

    paper = paper_of(lum)
    depth = np.clip(paper - lum, 0, None)
    live = depth[depth > 1.0]
    floor = np.percentile(live, 100 - floor_pct) if live.size else 1.0
    alpha = np.clip(depth / max(floor, 1e-3) * gain, 0, 1)

    paper_rgb = np.stack([paper_of(rgb[:, :, c]) for c in range(3)], axis=2)
    a = alpha[:, :, None]
    fg = np.where(a > 0.05, (rgb - (1 - a) * paper_rgb) / np.maximum(a, 1e-3), rgb)
    return np.clip(fg, 0, 255), alpha


def hue_weight(fg, alpha, family):
    """Soft membership of each pixel in a hue family: warm | cool | green."""
    hsv = cv2.cvtColor(np.clip(fg, 0, 255).astype(np.uint8)[None] if fg.ndim == 2
                       else np.clip(fg, 0, 255).astype(np.uint8), cv2.COLOR_RGB2HSV)
    h = hsv[:, :, 0].astype(np.float32) * 2.0        # 0..360
    s = hsv[:, :, 2].astype(np.float32)              # use value as a proxy weight
    r, g, b = fg[:, :, 0], fg[:, :, 1], fg[:, :, 2]
    warm = (r - b)                                    # gold/brown: red over blue
    cool = (b - r)
    green = (g - (r + b) / 2)
    if family == "warm":
        raw = warm
    elif family == "cool":
        raw = cool - np.clip(green, 0, None) * 0.5
    else:
        raw = green - np.clip(cool, 0, None) * 0.5
    del h, s
    return np.clip(raw / 14.0, 0, 1)


def recolour(fg, alpha, colour):
    out = np.zeros_like(fg)
    out[:, :] = colour
    return out


def palette_map(fg, alpha):
    """Snap the scene to the three site colours, weighted by hue membership."""
    w = np.stack([hue_weight(fg, alpha, f) for f in ("warm", "cool", "green")], axis=2)
    w[:, :, 0] += 0.10                                # gold is the default
    w = w / np.maximum(w.sum(axis=2, keepdims=True), 1e-6)
    cols = np.array([GOLD, SEA, SAGE], dtype=np.float32)
    return (w[:, :, :, None] * cols[None, None, :, :]).sum(axis=2)


def denoise(alpha, min_area=14, level=0.22):
    """Drop speckles: paper grain and stray fragments from neighbouring art."""
    mask = (alpha > level).astype(np.uint8)
    n, lab, stats, _ = cv2.connectedComponentsWithStats(mask, 8)
    keep = np.zeros(n, np.uint8)
    for i in range(1, n):
        keep[i] = stats[i, cv2.CC_STAT_AREA] >= min_area
    return alpha * keep[lab]


def box_out(alpha, x0, y0, x1, y1):
    """Zero a fractional rectangle (used to cut neighbouring artwork away)."""
    h, w = alpha.shape
    a = alpha.copy()
    a[int(y0*h):int(y1*h), int(x0*w):int(x1*w)] = 0.0
    return a


def trim(fg, alpha, thresh=0.12, pad=4):
    ys, xs = np.where(alpha > thresh)
    if not len(ys):
        return fg, alpha
    y0, y1 = max(0, ys.min()-pad), min(alpha.shape[0], ys.max()+pad+1)
    x0, x1 = max(0, xs.min()-pad), min(alpha.shape[1], xs.max()+pad+1)
    return fg[y0:y1, x0:x1], alpha[y0:y1, x0:x1]


def upscale(fg, alpha, factor, crisp=0.42):
    h, w = alpha.shape
    nh, nw = int(round(h*factor)), int(round(w*factor))
    a = np.clip(cv2.resize(alpha, (nw, nh), interpolation=cv2.INTER_CUBIC), 0, 1)
    f = cv2.resize(fg, (nw, nh), interpolation=cv2.INTER_CUBIC)
    if crisp:
        a = np.clip((a - 0.5) / max(1e-3, 1 - crisp) + 0.5, 0, 1)
    return np.clip(f, 0, 255), a


def save(path, fg, alpha):
    Image.fromarray(np.dstack([fg, alpha*255]).astype(np.uint8), "RGBA").save(path)
    im = Image.open(path)
    return path, im.size


def piece(box, out, factor=3.0, bg_radius=17, floor_pct=3.0, gain=1.0,
          keep=None, solid=None, mode=None, crisp=0.42, pad=4, min_alpha=0.06,
          speck=14, thin=1.0, cut=()):
    card = load()
    H, W = card.shape[:2]
    x0, y0, x1, y1 = (int(box[0]*W), int(box[1]*H), int(box[2]*W), int(box[3]*H))
    fg, a = matte(card[y0:y1, x0:x1], bg_radius, floor_pct, gain)

    if keep:                                   # drop everything not in this hue family
        a = a * np.clip(hue_weight(fg, a, keep) * 1.6, 0, 1)
        a[a < min_alpha] = 0.0
    a = denoise(a, min_area=speck)
    for r in cut:
        a = box_out(a, *r)
    if thin != 1.0:
        a = np.clip(a, 0, 1) ** thin
    if solid is not None:
        fg = recolour(fg, a, solid)
    elif mode == "palette":
        fg = palette_map(fg, a)

    fg, a = trim(fg, a, pad=pad)
    fg, a = upscale(fg, a, factor, crisp)
    return save(out, fg, a)
