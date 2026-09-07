# Gemini image prompts — Vivid Nutripharm product photography

Paste **Block 1** into Gemini once to set the house style, then paste the
individual prompts from **Block 2** one at a time. Block 3 is the
post-processing checklist that gets each file to the size the site expects.

Tested against Gemini's image models (Nano Banana / Nano Banana Pro). Set
**Resolution: 2K** in the model settings where the option is offered.

---

## Why these aspect ratios

Every product image renders in two places on the site:

| Slot | CSS | Effective box |
|---|---|---|
| Grid card `.p-thumb` | `aspect-ratio:4/3`, `object-fit:contain`, `padding:14px` | ~411 x 301 CSS px |
| Detail popup `.modal-img` | `max-width:100%; max-height:420px; object-fit:contain`, `padding:20px` | ~392 x 420 CSS px |

Both use `object-fit:contain`, so **cut-out packshots may be any aspect
ratio** — nothing is cropped. The binding constraint is the popup at 2x
retina: **~800 x 840 device px**. Generating at 2K and trimming leaves
comfortable headroom.

Four pages are the exception — `single-extracts.html`,
`chronic-disease-management.html`, `mens-sexual-wellness.html` and
`women-wellness.html` use `object-fit:cover`, which **does** crop to 4:3.
Those images must be generated at a true 4:3.

---

## Block 1 — paste this first (house style)

```
You are producing a consistent set of B2B nutraceutical product photographs for
Vivid Nutripharm, a contract manufacturer of supplements. I will send you one
product description at a time. For every image, apply all of the following
rules without me repeating them:

STYLE
- Commercial e-commerce packshot photography. Clean, modern, premium, clinical.
- Single product, centred, shot straight on at eye level with a very slight
  three-quarter turn so the front face and one side edge are both readable.
- Studio lighting: large soft key light from the upper left, subtle fill from
  the right, gentle specular highlight down one edge of the bottle or tube.
- Sharp focus edge to edge. No depth-of-field blur. No lens flare, no bokeh.
- Colour: neutral and accurate. No warm or teal grade, no film emulation.
- A soft contact shadow directly under the product only. No long cast shadows,
  no reflective mirror floor, no pedestal, no props, no hands, no people,
  no leaves, no scattered powder, no background scenery.

BACKGROUND
- Pure transparent background, exported as PNG with a real alpha channel.
- If transparency is not available, use a flat pure white #FFFFFF background
  with no gradient, no vignette and no visible horizon line, so it can be
  keyed out cleanly afterwards.

FRAMING
- The product fills the frame vertically with roughly 6-8% empty margin on all
  sides. Do not crop any part of the product. Do not add a border.

LABEL AND TEXT
- The pack label must be legible and correctly spelled. Only use the exact text
  I give you for that product. Do not invent extra marketing copy, do not add
  nutrition panels, barcodes, QR codes, award badges, certification seals,
  star ratings, prices, or any watermark.
- Brand wordmark on the label reads: VIVID NUTRIPHARM
- Label design language across the whole set: white or off-white label stock,
  a single accent colour band, one clean geometric sans-serif typeface,
  generous white space, no illustrations of plants or molecules unless I ask.
- The accent colour is given per product. Keep it as the only strong colour.

CONSISTENCY
- Treat every image in this set as the same photoshoot: identical camera angle,
  identical lighting direction, identical label layout grid, identical relative
  scale. Only the product form, label text and accent colour change.

Confirm you understand, then wait for my first product.
```

---

## Block 2 — one prompt per image

Each line gives the **target filename**, the **aspect ratio to set in Gemini**,
and the prompt text. Send the prompt text only; the filename is for you.

### Oral sprays — `assets/products/`

All ten are the same vessel: a **30 ml amber-free frosted white PET oral spray
bottle, tall and slim, with a matte white fine-mist pump and a clear over-cap**.
Set **aspect ratio 2:3** for every one of these.

| File | Prompt |
|---|---|
| `spray-vitamin-d3-k2.png` | A 30 ml sublingual oral spray bottle. Label text: "VIVID NUTRIPHARM / VITAMIN D3 + K2 / Liposomal Oral Spray / 3,600 IU D3 + 55 mcg K2-7 per ml / 30 ml". Accent colour: warm gold #E8A22B. |
| `spray-multivitamin.png` | A 30 ml sublingual oral spray bottle. Label text: "VIVID NUTRIPHARM / MULTIVITAMIN / Liposomal Oral Spray / B-Complex + Fat-Soluble Vitamins / 30 ml". Accent colour: deep green #1F8F3F. |
| `spray-vitamin-c.png` | A 30 ml sublingual oral spray bottle. Label text: "VIVID NUTRIPHARM / VITAMIN C / Oral Spray / 360 mg per ml / 30 ml". Accent colour: citrus orange #F26722. |
| `spray-iron.png` | A 30 ml sublingual oral spray bottle. Label text: "VIVID NUTRIPHARM / IRON / Oral Spray / Iron Bisglycinate / No Metallic Aftertaste / 30 ml". Accent colour: deep crimson #A6273C. |
| `spray-zma.png` | A 30 ml sublingual oral spray bottle. Label text: "VIVID NUTRIPHARM / ZMA / Oral Spray / Zinc + Magnesium + Vitamin B6 / 30 ml". Accent colour: slate blue #35618E. |
| `spray-erectile-dysfunction.png` | A 30 ml sublingual oral spray bottle. Label text: "VIVID NUTRIPHARM / MEN'S PERFORMANCE / Oral Spray / Nitrosigine + Cordyceps + Pine Bark / 30 ml". Accent colour: graphite #2B2B2B with a thin red #C0392B rule. |
| `spray-testoboost.png` | A 30 ml sublingual oral spray bottle. Label text: "VIVID NUTRIPHARM / TESTOBOOST / Oral Spray / Maca + Rhodiola + Shilajit / 30 ml". Accent colour: bronze #8C5A2B. |
| `spray-vo2-maxx.png` | A 30 ml sublingual oral spray bottle. Label text: "VIVID NUTRIPHARM / VO2 MAXX / Endurance Oral Spray / Cordyceps + Rhodiola + Beta-Alanine / 30 ml". Accent colour: electric blue #0F6FCB. |
| `spray-smokers-cough.png` | A 30 ml sublingual oral spray bottle. Label text: "VIVID NUTRIPHARM / RESPIRATORY SUPPORT / Oral Spray / Cordyceps + Astragalus + Vasaka / 30 ml". Accent colour: teal #1B7F79. |
| `spray-biotin.png` | A 30 ml sublingual oral spray bottle. Label text: "VIVID NUTRIPHARM / BIOTIN / Oral Spray / 30 ml / 30-Day Pack". Accent colour: rose #C2557A. |

### Mushroom tinctures — `assets/products/`

Same vessel for all three: a **30 ml amber glass dropper bottle with a black
ribbed cap and integrated glass pipette, pipette seated in the bottle**.
Set **aspect ratio 2:3**.

| File | Prompt |
|---|---|
| `tincture-cordyceps.png` | A 30 ml amber glass dropper bottle. Label text: "VIVID NUTRIPHARM / CORDY AMRIT / Cordyceps Double Extract Tincture / 30 ml". Accent colour: burnt orange #D9722B. |
| `tincture-lions-mane.png` | A 30 ml amber glass dropper bottle. Label text: "VIVID NUTRIPHARM / LION'S MANE / Double Extract Tincture / 30 ml". Accent colour: cream #E4D6A7 on charcoal. |
| `tincture-reishi.png` | A 30 ml amber glass dropper bottle. Label text: "VIVID NUTRIPHARM / REISHI / Double Extract Tincture / 30 ml". Accent colour: oxblood #7B2D3B. |

### Effervescent tubes — `assets/products/`

Same vessel for all four: a **standing cylindrical effervescent tablet tube,
matte white, with a coloured shrink-sleeve label and a matching flip-top
desiccant cap, 20 tablets**. Set **aspect ratio 2:3**.

| File | Prompt |
|---|---|
| `eff-instant-sex-drive.png` | An effervescent tablet tube. Label text: "VIVID NUTRIPHARM / INSTANT DRIVE / Effervescent Tablets / 20 Tablets". Accent colour: deep magenta #A31F5B. |
| `eff-gut-health-probiotics.png` | An effervescent tablet tube. Label text: "VIVID NUTRIPHARM / GUT HEALTH / Probiotic Effervescent Tablets / 20 Tablets". Accent colour: fresh green #4CAF50. |
| `eff-weight-loss-probiotics.png` | An effervescent tablet tube. Label text: "VIVID NUTRIPHARM / WEIGHT MANAGEMENT / Probiotic Effervescent Tablets / 20 Tablets". Accent colour: lime #8BC34A. |
| `eff-molecular-hydrogen.png` | An effervescent tablet tube. Label text: "VIVID NUTRIPHARM / MOLECULAR HYDROGEN / Effervescent Tablets / 20 Tablets". Accent colour: ice blue #4FA8D8. |

### Phytosomes — `assets/products/`

| File | Ratio | Prompt |
|---|---|---|
| `phyto-curcumin.png` | 4:3 | A shallow wide-mouth white HDPE supplement jar lying beside a small neat mound of deep yellow-orange curcumin phytosome powder. Label text: "VIVID NUTRIPHARM / PHYTO CURCUMIN / Phytosome Complex". Accent colour: turmeric gold #E3A008. Landscape composition, product left of centre, powder right. |
| `phyto-berberine.jpg` | 4:3 | A shallow wide-mouth white HDPE supplement jar lying beside a small neat mound of mustard-yellow berberine phytosome powder. Label text: "VIVID NUTRIPHARM / PHYTO BERBERINE / Phytosome Complex". Accent colour: amber #C98A16. Landscape composition matching the curcumin shot exactly. |
| `phyto-silymarin.png` | 2:3 | An upright white HDPE supplement jar with a white screw cap. Label text: "VIVID NUTRIPHARM / PHYTO SILYMARIN / Milk Thistle Phytosome Complex". Accent colour: thistle purple #6B4C8A. Portrait composition. |

### Cordyceps range — `assets/products/`

| File | Ratio | Prompt |
|---|---|---|
| `cordyceps-fruiting-bodies.jpg` | 3:4 | A small tidy pile of whole dried Cordyceps militaris fruiting bodies — slender bright orange club-shaped stalks, 4-6 cm long, natural texture, no soil. Macro product photography, no packaging, no label. Everything else per the house style. |
| `cordy-maxx-extract.png` | 2:3 | A tall cylindrical white HDPE bulk-ingredient jar with a white screw cap. Label text: "VIVID NUTRIPHARM / CORDY MAXX / Cordyceps Extract Powder / Standardised". Accent colour: burnt orange #D9722B. |
| `cordyceps-coffee.jpg` | 1:1 | A matte black stand-up coffee pouch with a degassing valve and a resealable top, standing upright. Label text: "VIVID NUTRIPHARM / CORDYCEPS + ARABICA / Coffee Extract Blend". Accent colour: burnt orange #D9722B on black. |

### Page heroes — `assets/`

Heroes sit in a `contain` box with `min-height:360px`. These are the one place
a lifestyle or scene image is appropriate.

| File | Ratio | Prompt |
|---|---|---|
| `hero-oral-sprays.jpg` | 3:4 | A group shot of five 30 ml white oral spray bottles from the Vivid Nutripharm range, arranged in a staggered row at slightly different depths on a seamless pure white background, straight-on studio lighting, labels legible but not readable in detail. Premium B2B contract-manufacturing catalogue look. |
| `hero-mushroom-tinctures.jpg` | 1:1 | A group shot of three 30 ml amber glass dropper bottles with black caps, arranged in a tight triangle on a seamless pure white background, one pipette lifted slightly. Premium apothecary look, clinical not rustic. |
| `hero-phytosome-technology.jpg` | 16:9 | A clean scientific still life on a seamless white background: three shallow white jars of fine botanical extract powder in gold, mustard and pale green, arranged in a wide horizontal line with even spacing. Laboratory-clean, no glassware, no molecules, no diagrams, no text. |
| `hero-effervescent.jpg` | 3:4 | A group shot of four matte white effervescent tablet tubes with coloured labels in green, lime, blue and magenta, standing in a staggered row on a seamless pure white background. |

### Category images used by the four cropping pages

`single-extracts.html`, `chronic-disease-management.html`,
`mens-sexual-wellness.html` and `women-wellness.html` still pull these from the
WordPress host and they are cropped to 4:3 by `object-fit:cover`. Generate at
**aspect ratio 4:3** and save into `assets/products/`, then repoint the `img`
fields in those pages.

| Suggested file | Prompt |
|---|---|
| `cat-tablets.jpg` | A neat arrangement of round white uncoated supplement tablets spilling from a tipped white HDPE bottle onto a seamless white surface. No label text. Landscape 4:3, subject centred with even margins so a centre crop stays balanced. |
| `cat-softgels.jpg` | A neat arrangement of translucent golden omega-3 softgel capsules on a seamless white surface, a few catching the light. No packaging. Landscape 4:3, subject centred. |
| `cat-sachets.jpg` | Three matte white single-dose stick packs lying flat in a fanned row on a seamless white surface, unbranded blank labels. Landscape 4:3, subject centred. |
| `cat-performance-energy.jpg` | A white scoop of pale beige performance powder resting beside a matte white bulk jar on a seamless white surface. No label text. Landscape 4:3, subject centred. |
| `cat-metabolic-wellness.jpg` | A white HDPE supplement bottle beside a small pile of white capsules and a simple stainless measuring spoon on a seamless white surface. Landscape 4:3, subject centred. |
| `cat-respiratory-health.jpg` | A white oral spray bottle beside a small pile of dried Astragalus root slices on a seamless white surface. Clinical, not rustic. Landscape 4:3, subject centred. |
| `cat-sleep-stress.jpg` | A dark navy supplement bottle beside three white oval tablets on a seamless white surface, cool low-contrast lighting suggesting evening. No moon, no stars, no bedroom scene. Landscape 4:3, subject centred. |
| `cat-womens-health.jpg` | A soft rose-labelled white supplement bottle beside a small pile of pale pink coated tablets on a seamless white surface. Landscape 4:3, subject centred. |
| `cat-full-spectrum-cordyceps.jpg` | A white bulk jar of orange Cordyceps extract powder beside a few whole dried orange Cordyceps militaris fruiting bodies on a seamless white surface. Landscape 4:3, subject centred. |
| `cat-oral-sprays.jpg` | Two white 30 ml oral spray bottles standing side by side on a seamless white surface, unbranded blank labels. Landscape 4:3, subject centred. |
| `cat-dried-cordyceps-powder.jpg` | A small neat mound of fine orange dried Cordyceps powder beside a white bulk jar on a seamless white surface. Landscape 4:3, subject centred. |
| `cat-cordyceps-capsules.jpg` | A white HDPE bottle beside a small pile of orange-tinted vegetarian capsules on a seamless white surface. Landscape 4:3, subject centred. |
| `cat-cordyceps-green-tea.jpg` | A matte white pouch beside a small pile of green tea leaf and a pinch of orange Cordyceps powder on a seamless white surface. Landscape 4:3, subject centred. |

---

## Do NOT regenerate these

- **`assets/certification-badges-transparent.png`** (5200 x 1120) — these are
  real certification marks (GMP, ISO, FSSAI and similar). An AI-generated
  version produces garbled, legally unusable logos. Get the official artwork
  from each certifying body.
- **`assets/product-disc.png`** and **`assets/cordyceps-subject.png`** — these
  are cut-outs positioned inside the hand-built inline SVG diagrams on the
  homepage. Replacing them shifts the geometry of those graphics.
- **`assets/product-lifecycle.png`** (1900 x 1990, 792 KB) — a labelled process
  diagram. Text-heavy diagrams are the weakest thing image models produce;
  rebuild it as inline SVG the way the other two homepage graphics were.

---

## Block 3 — after Gemini returns each image

1. **Check the alpha channel.** If Gemini returned a white background instead
   of transparency, key it out before saving. Every packshot page renders the
   popup on `#eef4ea` (`--green-tint`), so a baked-in white rectangle will show
   as a hard box against the green.
2. **Trim the transparent margin** tight to the product. The CSS supplies its
   own padding — 14px on the card, 20px in the popup — so baked-in whitespace
   just shrinks the product.
3. **Check the long edge is at least 1200 px** after trimming. That covers the
   420 px popup at 2x with room to spare.
4. **Compress.** Target under 150 KB per packshot; the current sprays are
   16-24 KB, so there is plenty of headroom. `pngquant --quality 65-85` for
   PNGs, quality 82 JPEG for the photographic ones.
5. **Keep the exact existing filename and extension** — the `img` fields in the
   `products` array in each page reference them literally. Changing `.png` to
   `.jpg` means editing the page too.
6. **Spot-check the label text.** Image models routinely misspell. Zoom to 100%
   and read every word before committing.

## Current file inventory for reference

| File | Current size | Notes |
|---|---|---|
| `spray-biotin.png` | 183 x 648 | under 2x for the popup |
| `spray-smokers-cough.png` | 192 x 652 | under 2x |
| `spray-vo2-maxx.png` | 192 x 652 | under 2x |
| `spray-testoboost.png` | 211 x 649 | under 2x |
| `spray-vitamin-c.png` | 214 x 614 | under 2x |
| `spray-iron.png` | 216 x 650 | under 2x |
| `spray-zma.png` | 216 x 654 | under 2x |
| `spray-erectile-dysfunction.png` | 217 x 652 | under 2x |
| `spray-vitamin-d3-k2.png` | 232 x 614 | under 2x |
| `spray-multivitamin.png` | 239 x 611 | under 2x |
| `tincture-reishi.png` | 209 x 453 | under 2x |
| `tincture-lions-mane.png` | 223 x 511 | under 2x |
| `tincture-cordyceps.png` | 333 x 800 | borderline |
| `cordy-maxx-extract.png` | 378 x 900 | ok |
| `eff-gut-health-probiotics.png` | 354 x 800 | borderline |
| `eff-instant-sex-drive.png` | 356 x 800 | borderline |
| `eff-molecular-hydrogen.png` | 371 x 800 | borderline |
| `eff-weight-loss-probiotics.png` | 370 x 800 | borderline |
| `phyto-silymarin.png` | 383 x 800 | borderline |
| `phyto-curcumin.png` | 800 x 534 | landscape |
| `phyto-berberine.jpg` | 900 x 602 | landscape |
| `cordyceps-coffee.jpg` | 538 x 561 | near square |
| `cordyceps-fruiting-bodies.jpg` | 610 x 720 | ok |
| `hero-effervescent.jpg` | 440 x 640 | small for a hero |
| `hero-mushroom-tinctures.jpg` | 725 x 677 | ok |
| `hero-oral-sprays.jpg` | 900 x 1200 | ok |
| `hero-phytosome-technology.jpg` | 1500 x 844 | ok |
