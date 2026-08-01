/* ==========================================================================
   Theju & Ahad — password gate, nav, image fallbacks
   --------------------------------------------------------------------------
   TO CHANGE THE PASSWORD: edit the one line below. That is the only place
   it appears.

   HONEST LIMITATION: this is a client-side check on a static site. It keeps
   the pages out of casual view and out of search results, but the page text
   is still in the HTML source, so anyone who opens "view source" can read it
   without the password. Do not put anything on here you would mind a
   determined stranger seeing.
   ========================================================================== */

var PASSWORD = "chennai1314";

/* ---------------------------------------------------------------- gate --- */
(function () {
  var KEY = "theju-ahad-unlocked";

  function remembered() {
    try { return sessionStorage.getItem(KEY) === "1"; } catch (e) { return false; }
  }
  function remember() {
    try { sessionStorage.setItem(KEY, "1"); } catch (e) { /* private mode: fine */ }
  }
  function norm(v) { return String(v || "").trim().toLowerCase(); }

  function unlock() {
    document.documentElement.classList.remove("locked");
    var g = document.getElementById("gate");
    if (g) { g.remove(); }
  }

  function buildGate() {
    var g = document.createElement("div");
    g.id = "gate";
    g.innerHTML =
      '<div class="gate__card">' +
        '<div class="gate__in">' +
          '<div class="kolam"></div>' +
          '<h1>Theju &amp; Ahad</h1>' +
          '<p class="dates">13 &amp; 14 December 2026</p>' +
          '<p class="place">Chennai, India</p>' +
          '<form class="gate__form" novalidate>' +
            '<label for="gate-pw">Enter the password from your invite</label>' +
            '<input id="gate-pw" type="password" autocomplete="off" autocapitalize="off" ' +
                   'autocorrect="off" spellcheck="false" placeholder="password">' +
            '<button type="submit">Come in</button>' +
            '<p class="gate__err" role="alert"></p>' +
          '</form>' +
          '<p class="gate__hint">Lost it? Ask Theju or Ahad.</p>' +
        '</div>' +
      '</div>';
    document.body.appendChild(g);

    var form = g.querySelector("form");
    var input = g.querySelector("input");
    var err = g.querySelector(".gate__err");
    input.focus();

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (norm(input.value) === norm(PASSWORD)) {
        remember();
        unlock();
      } else {
        err.textContent = "That is not it. Try again.";
        input.value = "";
        input.focus();
      }
    });
  }

  function start() {
    if (remembered()) { unlock(); } else { buildGate(); }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", start);
  } else {
    start();
  }
})();

/* ----------------------------------------------------------------- nav --- */
(function () {
  function start() {
    var btn = document.querySelector(".nav__toggle");
    var nav = document.getElementById("nav");
    if (!btn || !nav) { return; }
    btn.addEventListener("click", function () {
      var open = nav.classList.toggle("is-open");
      btn.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", start);
  } else { start(); }
})();

/* --------------------------------------------------- image placeholders --- */
/* Until the photos are dropped into /images, show a labelled gold placeholder
   instead of a broken-image icon. Delete this block once images are in. */
(function () {
  function mark(img) {
    var box = img.closest(".ph");
    if (box) { box.classList.add("is-missing"); }
  }
  function start() {
    var imgs = document.querySelectorAll(".ph img");
    for (var i = 0; i < imgs.length; i++) {
      (function (img) {
        if (img.complete && img.naturalWidth === 0) { mark(img); }
        img.addEventListener("error", function () { mark(img); });
      })(imgs[i]);
    }
  }
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", start);
  } else { start(); }
})();
