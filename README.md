# Vivid Nutripharm — static site

A static mirror of [vividnutripharm](https://skyblue-echidna-752271.hostingersite.com),
published via GitHub Pages.

## What's here

| Page | File |
|---|---|
| Home | `index.html` |
| About Us | `about-us.html` |
| Solutions | `solutions.html` |
| Contact | `contact.html` |
| Cordyceps Range | `durt-cordyceps-range.html` |
| Mushroom Tinctures | `mushroom-tinctures.html` |
| Oral Sprays | `oral-sprays-2.html` |
| Phytosomes | `phytosomes.html` |
| Chronic Disease Management | `chronic-disease-management.html` |
| Men's Sexual Wellness | `mens-sexual-wellness.html` |
| Women Wellness | `women-wellness.html` |
| Effervescent | `effervescent.html` |
| Single Extracts | `single-extracts.html` |

54 products across the nine product pages. Clicking a product opens a large
flip-out detail panel; homepage tiles deep-link straight to it via
`<page>.html#<product-id>`.

## Two rebuilt graphics

The homepage process circle and the Cordyceps benefits diagram are inline SVG
rather than flat images — real text, exact geometry, sharp at any zoom. Together
they are ~25 KB where the originals were ~2.8 MB. The two cut-out photographs
they place live in `assets/`.

## Dependency worth knowing

Stylesheets, scripts and most images load from the live WordPress install at
`skyblue-echidna-752271.hostingersite.com`. If that host goes away or its theme
changes, these pages change with it. Only `assets/product-disc.png` and
`assets/cordyceps-subject.png` are served from this repo.

## Not wired up

None of the contact or enquiry forms transmit. They validate, show a success
message and reset — the submit handler is still a placeholder on the live site
too. Working contact routes are the phone numbers and `info@vividnutripharm.com`.
