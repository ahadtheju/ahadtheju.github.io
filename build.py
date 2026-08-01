#!/usr/bin/env python3
"""
Optional. Regenerates the seven HTML pages so the shared header/footer stay
identical. You do not need to run this to use the site - the .html files are
already built. Run `python3 build.py` from this folder if you edit the
boilerplate below.
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))

NAV = [
    ("index.html", "Home"),
    ("rsvp.html", "RSVP"),
    ("events.html", "Events"),
    ("stay.html", "Stay"),
    ("faqs.html", "FAQs"),
    ("places.html", "Places"),
    ("colocated.html", "Colocated"),
]

SHELL = """<!DOCTYPE html>
<html lang="en" class="locked">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="noindex, nofollow">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Montserrat:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css">
<script src="assets/site.js" defer></script>
</head>
<body>

<noscript>
  <div style="max-width:520px;margin:60px auto;padding:30px;text-align:center;
              font-family:Montserrat,Arial,sans-serif;background:#FBF9F4;
              border:1px solid #E2D4B4;color:#5F5A50">
    This site needs JavaScript to unlock. Please turn it on and reload.
  </div>
</noscript>

<div class="site">

  <header class="topbar">
    <div class="topbar__in">
      <a class="wordmark" href="index.html">Theju <span>&amp;</span> Ahad</a>
      <button class="nav__toggle" type="button" aria-expanded="false" aria-controls="nav">Menu</button>
      <nav class="nav" id="nav" aria-label="Main">
{nav}
      </nav>
    </div>
  </header>

  <main>
{body}
  </main>

  <footer class="footer">
    <div class="waves"></div>
    <div class="footer__in">
      <div class="kolam kolam--sm"></div>
      <p class="names" style="margin-top:10px">Theju &amp; Ahad</p>
      <p>13 &amp; 14 December 2026 &middot; Chennai, India</p>
    </div>
  </footer>

</div>
</body>
</html>
"""

HERO_SCENE = (
    '<img class="hero__scene" src="assets/art/hero-chennai.png" width="1390" '
    'height="760" alt="Line drawing of a Chennai beach: coconut palms, the sea '
    'and a temple gopuram">')


def page(page_file, title, desc, body):
    nav_html = "\n".join(
        '        <a href="{href}"{cur}>{label}</a>'.format(
            href=href,
            label=label,
            cur=' aria-current="page"' if href == page_file else "",
        )
        for href, label in NAV
    )
    out = SHELL.format(title=title, desc=desc, nav=nav_html, body=body)
    with open(os.path.join(HERE, page_file), "w", encoding="utf-8") as fh:
        fh.write(out)
    print("wrote", page_file)


# ---------------------------------------------------------------- home ----
INDEX = """    <section class="hero">
      <div class="hero__card">
        <span class="sprig sprig--tr" aria-hidden="true"></span>
        <span class="sprig sprig--bl" aria-hidden="true"></span>
        <div class="hero__inner">
          """ + HERO_SCENE + """
          <p class="eyebrow">Join us for our wedding celebrations</p>
          <h1 class="names">Thejaswini <em>&amp;</em> Ahad</h1>
          <p class="dates">December 13 &amp; 14, 2026</p>
          <p class="place">Chennai, India</p>
        </div>
      </div>
    </section>

    <section class="section wrap">
      <div class="rule"><span class="kolam"></span></div>
      <div class="panel" style="text-align:center">
        <p class="lead" style="max-width:52ch;margin:0 auto">
          Come celebrate with us in Chennai this December. Two days, a lot of
          food, and no dress code you have to worry about. Everything you need
          to know is below.
        </p>
        <p style="margin-top:22px"><a class="btn" href="rsvp.html">RSVP</a></p>
      </div>

      <div class="grid grid--3" style="margin-top:22px">
        <a class="card" href="events.html" style="text-decoration:none">
          <div class="card__body">
            <p class="eyebrow eyebrow--navy" style="margin-bottom:.5rem">01</p>
            <h3>Events and schedule</h3>
            <p>What happens on the 13th and the 14th, and where.</p>
          </div>
        </a>
        <a class="card" href="stay.html" style="text-decoration:none">
          <div class="card__body">
            <p class="eyebrow eyebrow--navy" style="margin-bottom:.5rem">02</p>
            <h3>Stay</h3>
            <p>Where to sleep, and which part of the city to aim for.</p>
          </div>
        </a>
        <a class="card" href="faqs.html" style="text-decoration:none">
          <div class="card__body">
            <p class="eyebrow eyebrow--navy" style="margin-bottom:.5rem">03</p>
            <h3>FAQs and information</h3>
            <p>What to expect, what to wear, food, gifts.</p>
          </div>
        </a>
        <a class="card" href="places.html" style="text-decoration:none">
          <div class="card__body">
            <p class="eyebrow eyebrow--navy" style="margin-bottom:.5rem">04</p>
            <h3>Places to visit nearby</h3>
            <p>Day trips out of Chennai, and where to eat.</p>
          </div>
        </a>
        <a class="card" href="colocated.html" style="text-decoration:none">
          <div class="card__body">
            <p class="eyebrow eyebrow--navy" style="margin-bottom:.5rem">05</p>
            <h3>Colocated events</h3>
            <p>For the theoretical computer scientists among you.</p>
          </div>
        </a>
        <a class="card" href="rsvp.html" style="text-decoration:none">
          <div class="card__body">
            <p class="eyebrow eyebrow--navy" style="margin-bottom:.5rem">06</p>
            <h3>RSVP</h3>
            <p>Tell us you are coming so we can count you in.</p>
          </div>
        </a>
      </div>
    </section>
"""

# ---------------------------------------------------------------- rsvp ----
RSVP = """    <section class="pagehead">
      <div class="pagehead__in">
        <div class="kolam"></div>
        <p class="eyebrow">Thejaswini &amp; Ahad</p>
        <h1>RSVP</h1>
        <p class="lead">Fill in the form below so we know you are coming.</p>
      </div>
    </section>

    <section class="section wrap">
      <p style="text-align:center;margin-bottom:20px">
        <a class="btn btn--ghost" target="_blank" rel="noopener"
           href="https://docs.google.com/forms/d/e/1FAIpQLSdDzNXvLAQRDB1RFnpD4bATDlHAFRmEfuaA7yKAKqmdtDCkfw/viewform">
          Open the form in a new window
        </a>
      </p>
      <div class="formwrap">
        <iframe title="RSVP form"
          src="https://docs.google.com/forms/d/e/1FAIpQLSdDzNXvLAQRDB1RFnpD4bATDlHAFRmEfuaA7yKAKqmdtDCkfw/viewform?embedded=true"
          loading="lazy">Loading form...</iframe>
      </div>
    </section>
"""

# -------------------------------------------------------------- events ----
EVENTS = """    <section class="pagehead">
      <div class="pagehead__in">
        <div class="kolam"></div>
        <p class="eyebrow">Thejaswini &amp; Ahad</p>
        <h1>Events and schedule</h1>
        <p class="lead">Two days. Come to as much or as little as you like.</p>
      </div>
    </section>

    <section class="section wrap">

      <article class="day panel">
        <div class="day__head">
          <span class="day__date">13th December</span>
          <span class="day__venue">Keys Prima by Lemon Tree Hotels &mdash; Katti-Ma, Chennai</span>
        </div>

        <div class="ph ph--wide" data-file="images/events-day1.jpg" style="margin-bottom:22px">
          <img src="images/events-day1.jpg" alt="Wedding day one" loading="lazy">
        </div>

        <div class="slot">
          <div class="slot__time">7:00 AM</div>
          <div class="slot__body">
            <h3>Breakfast &amp; morning ceremony</h3>
            <p>The day begins with the traditional religious elements of the wedding.
               Breakfast will be served starting at 7:00 AM. After the meal, Theju and
               Ahad will take part in several sacred rituals.</p>
          </div>
        </div>

        <div class="slot">
          <div class="slot__time">Afternoon</div>
          <div class="slot__body">
            <h3>Valayadal / Nalangu</h3>
            <p>A lighthearted, joyous tradition with friendly competition and music.
               Guests are encouraged to pick a side and cheer them on!</p>
          </div>
        </div>
      </article>

      <article class="day panel">
        <div class="day__head">
          <span class="day__date">14th December</span>
          <span class="day__venue">Matsya</span>
        </div>

        <div class="ph ph--wide" data-file="images/events-day2.jpg" style="margin-bottom:22px">
          <img src="images/events-day2.jpg" alt="Reception" loading="lazy">
        </div>

        <div class="slot">
          <div class="slot__time">11:00 AM onwards</div>
          <div class="slot__body">
            <h3>Reception</h3>
            <p>A post-wedding brunch and lunch that lasts till 4 pm. This one is just
               for us to dance and have fun.</p>
          </div>
        </div>
      </article>

      <article class="day panel panel--warm">
        <div class="day__head">
          <span class="day__date">14th December</span>
          <span class="day__venue">After party</span>
        </div>

        <div class="grid grid--2" style="align-items:center">
          <div class="ph" data-file="images/events-afterparty.jpg">
            <img src="images/events-afterparty.jpg" alt="After party" loading="lazy">
          </div>
          <div>
            <p class="slot__time" style="margin-bottom:.4rem">Evening / night</p>
            <h3>Afterparty</h3>
            <p class="muted" style="margin-top:.35rem">We might head somewhere for dinner
               and drinks. One drink per person is on us. Details to follow.</p>
          </div>
        </div>
      </article>

    </section>
"""

# ---------------------------------------------------------------- stay ----
STAY = """    <section class="pagehead">
      <div class="pagehead__in">
        <div class="kolam"></div>
        <p class="eyebrow">Thejaswini &amp; Ahad</p>
        <h1>Stay</h1>
        <p class="lead">Three options, depending on what you are after.</p>
      </div>
    </section>

    <section class="section wrap">
      <div class="grid grid--3">

        <article class="card">
          <div class="ph" data-file="images/stay-keys-prima.jpg">
            <img src="images/stay-keys-prima.jpg" alt="Keys Prima by Lemon Tree Hotels" loading="lazy">
          </div>
          <div class="card__body">
            <p class="eyebrow eyebrow--navy" style="margin-bottom:.5rem">Closest to everything</p>
            <h3>Keys Prima by Lemon Tree Hotels</h3>
            <p>Next to Theju's parents' house. Thejaswini will be staying at her parents'
               place, less than 3 minutes away, and this hotel is the venue for Day 1.</p>
            <p style="margin-top:1rem">
              <a target="_blank" rel="noopener"
                 href="https://www.lemontreehotels.com/keys-prima-hotel/chennai/hotel-katti-ma-chennai">Book here</a>
            </p>
          </div>
        </article>

        <article class="card">
          <div class="ph" data-file="images/stay-cmi.jpg">
            <img src="images/stay-cmi.jpg" alt="Chennai Mathematical Institute" loading="lazy">
          </div>
          <div class="card__body">
            <p class="eyebrow eyebrow--navy" style="margin-bottom:.5rem">Limited!!!</p>
            <h3>Chennai Mathematical Institute guest house</h3>
            <p>If you give an academic talk before or after the wedding, you might be able
               to get a room at CMI.</p>
          </div>
        </article>

        <article class="card">
          <div class="ph" data-file="images/stay-airbnb.jpg">
            <img src="images/stay-airbnb.jpg" alt="Airbnb in Chennai" loading="lazy">
          </div>
          <div class="card__body">
            <p class="eyebrow eyebrow--navy" style="margin-bottom:.5rem">With other friends</p>
            <h3>Airbnb</h3>
            <p>There are many Airbnbs. We recommend staying closer to Thiruvanmiyur, to
               avoid some traffic and to be reasonably central without breathing polluted air.</p>
          </div>
        </article>

      </div>
    </section>
"""

# ---------------------------------------------------------------- faqs ----
ATTIRE = [
    ("Saree", "images/attire-saree.jpg",
     "A continuous piece of fabric, typically 5-9 yards long, gracefully draped over a "
     "fitted blouse and an underskirt. Traditionally worn by women, with several draping "
     "styles and fabric choices, from lightweight cottons to ornate silks. It normally "
     "needs a specific draping technique, but pre-stitched sarees are now available for "
     "easier wear."),
    ("Kurtha / Kurthi", "images/attire-kurtha.jpg",
     "A loose, collarless tunic that falls just above or below the knees, traditionally "
     "paired with drawstring trousers, fitted churidars, or even western trousers. A "
     "popular and comfortable garment worn by men and women."),
    ("Lehenga", "images/attire-lehenga.jpg",
     "A three-piece ensemble: a flared, ankle-length skirt, a fitted blouse (choli), and "
     "a matching drape (dupatta). Mostly worn by women, and a favourite for festive "
     "occasions and weddings because of the embroidery and colours."),
    ("Salwar", "images/attire-salwar.jpg",
     "A comfortable outfit of loose, pleated trousers (the salwar) that taper at the "
     "ankles, paired with a long tunic (kameez) and a scarf (dupatta). Worn "
     "predominantly by women."),
    ("Dhoti", "images/attire-dhoti.jpg",
     "A traditional unstitched garment for men: a rectangular piece of cloth wrapped "
     "around the waist and legs, usually paired with a kurtha or a shirt. A classic "
     "style for religious ceremonies. It normally needs a specific draping technique, "
     "but pre-stitched dhothis are now available for easier wear."),
    ("Anything else!", "images/attire-anything-else.jpg",
     "Whatever you feel good in."),
]

attire_cards = "\n".join(
    """        <article class="card">
          <div class="ph ph--tall" data-file="{img}">
            <img src="{img}" alt="{name}" loading="lazy">
          </div>
          <div class="card__body">
            <h3>{name}</h3>{para}
          </div>
        </article>""".format(
        img=img, name=name,
        para=("\n            <p>" + text + "</p>") if text else "")
    for name, img, text in ATTIRE
)

FAQS = """    <section class="pagehead">
      <div class="pagehead__in">
        <div class="kolam"></div>
        <p class="eyebrow">Thejaswini &amp; Ahad</p>
        <h1>FAQs and information</h1>
        <p class="lead">Ask us if you have any specific questions!</p>
      </div>
    </section>

    <section class="section wrap">
      <div class="panel">
        <div class="faq">

          <details open>
            <summary>I have never been to an Indian wedding before. What should I expect?</summary>
            <div class="answer">
              <p>India is large and diverse, with many cultures and many kinds of weddings.
                 This wedding is similar in spirit to Tamil weddings, and is a much shorter
                 version of the weddings in Theju's family, which traditionally last 5 days.</p>
              <p>Unlike Western weddings, it is quite chaotic and loud. There is no real
                 solemn moment and no seating chart. You are not expected to attend all of
                 the rituals. You can move around freely during the events, talk to people,
                 eat, and just mingle while the religious ceremony happens. There will be a
                 priest conducting the ceremony in Sanskrit (sadly we do not have subtitles),
                 while the bride and groom, and sometimes other relatives, sit next to him in
                 front of a fire performing some rituals. Ours is NOT going to be a big fat
                 Indian wedding, but we hope the food will still be great! Food will be
                 served as a buffet at all events.</p>
              <p>For the second day, 14th December, there are really no rules. It is just a
                 lunch and perhaps an after-party, both with music and hopefully some dancing.
                 If you want, feel free to sing, dance and talk to us.</p>
              <p>Ask us if you have any specific questions!</p>
            </div>
          </details>

          <details>
            <summary>What should I wear?</summary>
            <div class="answer">
              <p>We are just excited that you will be there, so we are happy no matter what
                 you wear. Below we describe what we think others might wear traditionally,
                 and you are welcome to join in if you feel like it.</p>

              <h4>December 13th</h4>
              <p>Traditional Indian attire is welcome and encouraged, but not required! Some
                 options are a saree, kurtha, dhothi, salwar kameez, or lehenga (see below).
                 You can also wear colourful western clothes, or anything else really, and
                 that is completely fine. If you choose to wear traditional clothes, we can
                 help you put them on at the venue. We have a couple of rooms where you can
                 change if you come in advance.</p>

              <h4>December 14th</h4>
              <p>This is a casual meet, and traditional attire is again encouraged, but you
                 can also choose to wear, say, cocktail clothes. There might be some dancing,
                 so please prioritise being comfortable.</p>
            </div>
          </details>

          <details>
            <summary>Can we go shopping in Chennai?</summary>
            <div class="answer">
              <p>YES! We definitely recommend it, for both regular clothes and Indian
                 clothes, since it is quite cheap here.</p>
              <p>We will try to pair you with an Indian person, if you need one and do not
                 already know someone in this crowd who can help, so you can go shopping a
                 day or two before the wedding. Stitching is also fast in many places in
                 India, and Theju will tell you where to shop for clothes and other things
                 close to her house in Thiruvanmiyur, Chennai.</p>
            </div>
          </details>

          <details>
            <summary>Should I eat beforehand?</summary>
            <div class="answer">
              <p>No. All food served is vegetarian. Some of it is vegan. Let us know
                 beforehand if you have any other allergies.</p>
            </div>
          </details>

          <details>
            <summary>Is it safe to travel in Chennai and South India?</summary>
            <div class="answer">
              <p>This is complicated. India definitely is not as safe as most parts of
                 Western Europe.</p>
            </div>
          </details>

          <details>
            <summary>What can I give as a gift?</summary>
            <div class="answer">
              <p>Clich&eacute;: your presence is a present.</p>
              <p>We are grateful that you are flying from so far away to celebrate with us,
                 and we need nothing more than for you to be there.</p>
              <p>If that does not stop you, then you can:</p>
              <ol>
                <li>Volunteer to help with some part of organising the wedding, either some
                    performances for 14th December, or local organisation.</li>
                <li>Give us a book you think we have not read. Neither of us reads as much
                    as we would like, but we want to live in a house of books. If you would
                    rather, we are also building a small vinyl collection. Buy either and
                    give it to us in person, or, preferably and if it is feasible for you,
                    send it to our Belgian address: Thejaswini K S Raghavan, Rue Scarron 20,
                    Bt 15, Ixelles, Brussels, Belgium.</li>
                <li>If you truly have way too much money and want to spend a bunch of it,
                    you can satisfy that urge by giving to
                    <a href="https://aidindia.in/" target="_blank" rel="noopener">AID India</a>
                    instead.</li>
              </ol>
            </div>
          </details>

        </div>
      </div>

      <div class="rule"><span class="kolam"></span></div>

      <div class="section--tight" style="text-align:center">
        <p class="eyebrow">A quick guide</p>
        <h2>What people might wear</h2>
      </div>

      <div class="grid grid--3">
""" + attire_cards + """
      </div>
    </section>
"""

# -------------------------------------------------------------- places ----
PLACES = """    <section class="pagehead">
      <div class="pagehead__in">
        <div class="kolam"></div>
        <p class="eyebrow">Food and tourism</p>
        <h1>Places to visit nearby</h1>
        <p class="lead">In and around Chennai, and a bit further south.</p>
      </div>
    </section>

    <section class="section wrap">
      <div class="grid grid--3">

        <article class="card">
          <div class="ph" data-file="images/place-dakshinachitra.jpg">
            <img src="images/place-dakshinachitra.jpg" alt="DakshinaChitra" loading="lazy">
          </div>
          <div class="card__body">
            <h3>DakshinaChitra</h3>
            <p>A day trip from Chennai, on the way to Mahabalipuram. It is a cultural
               museum, and we completely recommend visiting if you have not been before.</p>
          </div>
        </article>

        <article class="card">
          <div class="ph" data-file="images/place-mahabalipuram.jpg">
            <img src="images/place-mahabalipuram.jpg" alt="Mahabalipuram" loading="lazy">
          </div>
          <div class="card__body">
            <h3>Mahabalipuram</h3>
            <p>Also a day trip. Mamallapuram, or Mahabalipuram, is a town on a strip of land
               between the Bay of Bengal and the Great Salt Lake, in the south Indian state
               of Tamil Nadu. It is known for its temples and monuments built by the Pallava
               dynasty in the 7th and 8th centuries.</p>
          </div>
        </article>

        <article class="card">
          <div class="ph" data-file="images/place-kapaleeshwarar.jpg">
            <img src="images/place-kapaleeshwarar.jpg" alt="Kapaleeshwarar Temple" loading="lazy">
          </div>
          <div class="card__body">
            <h3>Kapaleeshwarar Temple</h3>
            <p>In Chennai. A Hindu temple dedicated to the god Shiva, in Mylapore. It was
               built around the 7th century A.D. and is an example of South Indian
               architecture.</p>
          </div>
        </article>

      </div>

      <div class="rule"><span class="kolam"></span></div>

      <div class="section--tight" style="text-align:center">
        <h2>Some food recs</h2>
      </div>

      <div class="grid grid--3">

        <article class="card">
          <div class="ph" data-file="images/food-annalakshmi.jpg">
            <img src="images/food-annalakshmi.jpg" alt="Annalakshmi" loading="lazy">
          </div>
          <div class="card__body">
            <h3><a href="https://www.annalakshmichennai.com/" target="_blank" rel="noopener">Annalakshmi</a></h3>
          </div>
        </article>

        <article class="card">
          <div class="ph" data-file="images/food-the-farm.jpg">
            <img src="images/food-the-farm.jpg" alt="The Farm" loading="lazy">
          </div>
          <div class="card__body">
            <h3><a href="https://www.thefarmchennai.com" target="_blank" rel="noopener">The Farm</a></h3>
          </div>
        </article>

        <article class="card">
          <div class="ph" data-file="images/food-kappa-chakka-kandhari.jpg">
            <img src="images/food-kappa-chakka-kandhari.jpg" alt="Kappa Chakka Kandhari" loading="lazy">
          </div>
          <div class="card__body">
            <h3><a href="https://kappachakkakandhari.com/menu-restaurant/" target="_blank" rel="noopener">Kappa Chakka Kandhari</a></h3>
          </div>
        </article>

        <article class="card">
          <div class="ph" data-file="images/food-sandys.jpg">
            <img src="images/food-sandys.jpg" alt="Sandy's chocolate laboratory" loading="lazy">
          </div>
          <div class="card__body">
            <h3><a href="https://www.instagram.com/sandyschocolatelab/reels/" target="_blank" rel="noopener">Sandy's chocolate laboratory</a></h3>
          </div>
        </article>

        <article class="card">
          <div class="ph" data-file="images/food-kipling-cafe.jpg">
            <img src="images/food-kipling-cafe.jpg" alt="Kipling Cafe" loading="lazy">
          </div>
          <div class="card__body">
            <h3><a href="https://kiplingcafe.blogspot.com" target="_blank" rel="noopener">Kipling Cafe</a></h3>
          </div>
        </article>

        <article class="card">
          <div class="ph" data-file="images/food-murugan-idly-kadai.jpg">
            <img src="images/food-murugan-idly-kadai.jpg" alt="Murugan Idly Kadai" loading="lazy">
          </div>
          <div class="card__body">
            <h3>Murugan Idly Kadai</h3>
            <p>A chain, so there is one near you.</p>
          </div>
        </article>

      </div>

      <div class="rule"><span class="kolam"></span></div>

      <div class="section--tight" style="text-align:center">
        <h2>Other places in the south of India</h2>
      </div>

      <div class="grid grid--2">

        <article class="card">
          <div class="ph ph--wide" data-file="images/south-kerala.jpg">
            <img src="images/south-kerala.jpg" alt="Kerala" loading="lazy">
          </div>
          <div class="card__body">
            <h3>Kochi, Alleppey and Thiruvananthapuram, in Kerala</h3>
            <p>Just google it. It is a great place to visit.</p>
          </div>
        </article>

        <article class="card">
          <div class="ph ph--wide" data-file="images/south-goa.jpg">
            <img src="images/south-goa.jpg" alt="Goa" loading="lazy">
          </div>
          <div class="card__body">
            <h3>Goa</h3>
            <p>Cool beaches! Great places to party too!</p>
          </div>
        </article>

        <article class="card">
          <div class="ph ph--wide" data-file="images/south-hyderabad.jpg">
            <img src="images/south-hyderabad.jpg" alt="Hyderabad" loading="lazy">
          </div>
          <div class="card__body">
            <h3>Hyderabad</h3>
            <p>Home to Hyderabadi biriyani.</p>
          </div>
        </article>

        <article class="card">
          <div class="ph ph--wide" data-file="images/south-ooty-kodaikanal.jpg">
            <img src="images/south-ooty-kodaikanal.jpg" alt="Ooty or Kodaikanal" loading="lazy">
          </div>
          <div class="card__body">
            <h3>Ooty or Kodaikanal</h3>
            <p>Attempt only if you are brave and can get there by bus or train overnight.</p>
          </div>
        </article>

      </div>
    </section>
"""

# ----------------------------------------------------------- colocated ----
COLOCATED = """    <section class="pagehead">
      <div class="pagehead__in">
        <div class="kolam"></div>
        <p class="eyebrow">Thejaswini &amp; Ahad</p>
        <h1>Colocated events</h1>
      </div>
    </section>

    <section class="section wrap">
      <div class="grid grid--2" style="align-items:center">
        <div class="ph ph--wide" data-file="images/colocated-cmi.jpg">
          <img src="images/colocated-cmi.jpg" alt="Chennai Mathematical Institute" loading="lazy">
        </div>
        <div class="panel">
          <p class="eyebrow eyebrow--navy">Around 10-11 December</p>
          <h2 style="margin-bottom:.6rem">A workshop at CMI</h2>
          <p class="muted">If you are a theoretical computer scientist, consider attending a
             workshop at Chennai Mathematical Institute, probably around the 10th and 11th
             of December.</p>
          <p class="note" style="margin-top:18px">More details to follow.</p>
        </div>
      </div>
    </section>
"""

PAGES = [
    ("index.html", "Theju &amp; Ahad", "Join us to celebrate in Chennai in December!", INDEX),
    ("rsvp.html", "RSVP - Theju &amp; Ahad", "RSVP", RSVP),
    ("events.html", "Events and schedule - Theju &amp; Ahad", "Events and schedule", EVENTS),
    ("stay.html", "Stay - Theju &amp; Ahad", "Where to stay in Chennai", STAY),
    ("faqs.html", "FAQs and information - Theju &amp; Ahad", "FAQs and information", FAQS),
    ("places.html", "Places to visit nearby - Theju &amp; Ahad", "Food and tourism around Chennai", PLACES),
    ("colocated.html", "Colocated events - Theju &amp; Ahad", "Colocated events", COLOCATED),
]

if __name__ == "__main__":
    for f, t, d, b in PAGES:
        page(f, t, d, b)
    print("done")
