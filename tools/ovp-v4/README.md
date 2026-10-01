# OVP demo 4 — build tools

Internal tooling for `ovp-demo-v4/` (not part of the site).

- `python3 build.py` — regenerates all 14 HTML pages (shared header, footer, service template). Add `STYLEGUIDE=1` for a temporary `styleguide.html`.
- `python3 verify.py` — checks links/anchors, one h1 per page, heading order, noindex, alt/width on images, external `rel`, banned words, JS size, home weight, and lists every `[OVP: …]` placeholder.
- `node shot.mjs index.html,contact.html 375,768,1280,1440` — full-page screenshots into `shots/` (needs `playwright`).
- `node behave.mjs` — keyboard/menu/form behaviour checks.

CSS and JS are edited directly in `ovp-demo-v4/assets/`.
