# Theju & Ahad, wedding site

A plain static site. Seven HTML pages, one stylesheet, one script, no build
step and no framework. Open `index.html` in a browser and it works.

## The password

`chennai1314`

Change it in `assets/site.js`, line 14:

```js
var PASSWORD = "chennai1314";
```

That is the only place it appears. It is case-insensitive and ignores spaces
around it, so a guest typing `Chennai1314 ` still gets in.

Once a guest enters it, they stay unlocked for the rest of the browser session,
across all seven pages. Closing the browser locks it again.

**What this protects and what it does not.** This is a client-side check on a
static site, which is the only kind possible without a server. It keeps the
pages out of casual view, off search engines, and away from anyone who stumbles
on the link. It does *not* stop someone who opens "view source": the page text
is sitting there in the HTML. So treat it as a front door, not a safe. Do not
put anything on here you would mind a determined stranger reading.

If you later want real protection, the cheapest route is Netlify's
password-protected sites or a Cloudflare Access rule. Both check the password
on the server before sending any HTML.

## Photos

The 26 photos are not included. See `images/PHOTOS.md`, or just run:

```bash
bash download-images.sh
```

from this folder. Until they are in place, each photo slot shows a labelled
gold placeholder rather than a broken image.

## Hosting

Any static host works. Drag the whole folder onto
[app.netlify.com/drop](https://app.netlify.com/drop) and it is live in about ten
seconds, with a URL you can rename. GitHub Pages, Cloudflare Pages, Vercel and
Surge all work the same way. Nothing needs a server.

Every page carries `<meta name="robots" content="noindex, nofollow">`, so
Google will not list it.

## Files

```
index.html          Home
rsvp.html           RSVP, embeds the existing Google Form
events.html         Events and schedule
stay.html           Stay
faqs.html           FAQs and information, plus the attire guide
places.html         Places to visit nearby
colocated.html      Colocated events
assets/style.css    All the styling, colours at the top under :root
assets/site.js      Password gate, mobile menu, image placeholders
images/             Photos go here, see PHOTOS.md
assets/art/         The decorative artwork, lifted off the save-the-date card
build.py            Optional, regenerates the 7 pages from shared boilerplate
make-art.py         Optional, how assets/art was made (needs the card photo)
download-images.sh  Optional, pulls the photos off the old Google Site
```

You can edit the `.html` files directly and ignore `build.py` entirely. It only
exists so the header, nav and footer stay identical across all seven pages if
you change them. If you do run it, run it from this folder: `python3 build.py`.

## Theme

Taken from the save-the-date card. The colours are all at the top of
`style.css`:

| | |
|---|---|
| `--paper` `#EFE9DD` | the cream backdrop |
| `--card` `#FBF9F4` | the card itself |
| `--gold` `#C0A062` | the line art and hairlines |
| `--navy` `#1B4E6B` | the date blue |
| `--sage` `#9FB49E` | the green leaves |
| `--sea` `#A6C4D4` | the waves |

Fonts are Playfair Display and Montserrat, loaded from Google Fonts.

The decorative artwork is not drawn from scratch. It is lifted straight off
the photo of your save-the-date card, so it is the same illustration, not an
imitation of it:

```
assets/art/hero-chennai.png   the beach scene: palms, sea, the gopuram
assets/art/kolam.png          the kolam from the foot of the card
assets/art/kolam-pale.png     the same, pale, for empty photo slots
assets/art/sprig.png          the corner leaves
```

They are transparent PNGs, so they sit on any background. Each one was cut out
of the card photo, separated from the paper, cleaned of speckle, recoloured to
the palette above and upscaled. `make-art.py` is the script that did it; it
needs the original card photo to run, so treat it as a record of how the files
were produced rather than something to re-run.

To swap any piece, drop a replacement PNG into `assets/art/` with the same
filename. Nothing else needs changing.

## Language changes from the old site

Content is the same; I fixed typos and left the tone alone. The notable ones:

- "Fir the second day" → "For the second day"
- "you can move freely during the events, talks to people" → "talk to people"
- "chose to wear" → "choose to wear"
- "Kurtha\Kurthi" → "Kurtha / Kurthi"
- "Theju's parent's house" → "parents' house"
- "Theoretical computer Scientist" → "theoretical computer scientist"
- "If this does not convince you from not giving us gifts" → "If that does not stop you"
- "11:00AM Afternoon" → "11:00 AM onwards"
- Place names to their standard spellings: Thiruvanmyur → Thiruvanmiyur,
  Dakshinchitra → DakshinaChitra, Allepey → Alleppey,
  Thiruvanandapuram → Thiruvananthapuram, Cochin → Kochi

Two things I left as they were, because they are in the original: the
Mahabalipuram description says "the Great Salt Lake" (that is Google's own
wording, and the lake there is usually called Kaliveli or the Great Salt Lake
in older sources), and "biriyani" is the common South Indian spelling.

One line is new, on the Home page: "Come celebrate with us in Chennai this
December. Two days, a lot of food, and no dress code you have to worry about."
The old Home page repeated its own headline, so this replaces the duplicate.
Delete it in `index.html` if you would rather not have it.
