#!/usr/bin/env python3
"""Generate Tailwind redesign category pages and homepage product rows."""

from __future__ import annotations

import html
import sys
from pathlib import Path

sys.path.insert(0, str(Path("/Users/maneeshreddy/nutripharm")))
from importlib.machinery import SourceFileLoader

inj = SourceFileLoader("inj", "/Users/maneeshreddy/nutripharm/inject-category-products.py").load_module()
PAGES = inj.PAGES

ROOT = Path("/Users/maneeshreddy/nutripharm")

META = {
    "oral-sprays-2": {
        "slug": "oral-sprays",
        "nav": "Oral Sprays",
        "icon": "fa-spray-can",
        "title_tag": "Oral Sprays — Vivid Nutripharm",
        "desc": "Liposomal sublingual and buccal oral sprays for private-label nutraceutical brands.",
    },
    "phytosomes": {
        "slug": "phytosomes",
        "nav": "Phytosomes",
        "icon": "fa-dna",
        "title_tag": "Phytosomes — Vivid Nutripharm",
        "desc": "Phytosomal curcumin, berberine and silymarin for improved botanical delivery.",
    },
    "chronic-disease-management": {
        "slug": "chronic-disease-management",
        "nav": "Chronic Disease",
        "icon": "fa-heart-pulse",
        "title_tag": "Chronic Disease Formulations — Vivid Nutripharm",
        "desc": "Condition-led nutraceutical tablets for kidney, metabolic, joint and respiratory wellness.",
    },
    "mens-sexual-wellness": {
        "slug": "mens-sexual-wellness",
        "nav": "Men’s Wellness",
        "icon": "fa-person",
        "title_tag": "Men’s Sexual Wellness — Vivid Nutripharm",
        "desc": "Men’s vitality, fertility and sexual wellness tablet formulations for private label.",
    },
    "women-wellness": {
        "slug": "women-wellness",
        "nav": "Women Wellness",
        "icon": "fa-venus",
        "title_tag": "Women Wellness — Vivid Nutripharm",
        "desc": "Fertility, PCOS, intimate wellness and ingestible skincare formulations.",
    },
    "effervescent": {
        "slug": "effervescent",
        "nav": "Effervescent",
        "icon": "fa-glass-water",
        "title_tag": "Effervescent Formulations — Vivid Nutripharm",
        "desc": "Effervescent tablets for vitality, gut health, weight management and molecular hydrogen.",
    },
    "single-extracts": {
        "slug": "single-extracts",
        "nav": "General Wellness",
        "icon": "fa-leaf",
        "title_tag": "General Wellness SKUs — Vivid Nutripharm",
        "desc": "Magnesium, omega-3, digestive mints, energy and antioxidant tablets for private label.",
    },
}

CAT_LINKS = [
    ("../durt-cordyceps-range/", "Cordyceps Range"),
    ("../oral-sprays/", "Oral Sprays"),
    ("../phytosomes/", "Phytosomes"),
    ("../chronic-disease-management/", "Chronic Disease"),
    ("../mens-sexual-wellness/", "Men’s Wellness"),
    ("../women-wellness/", "Women Wellness"),
    ("../effervescent/", "Effervescent"),
    ("../single-extracts/", "General Wellness"),
]


def e(s: str) -> str:
    return html.escape(s, quote=True)


def product_cards(products: list[dict], icon: str) -> str:
    bits = []
    for i, p in enumerate(products):
        specs = "".join(
            f'<span class="rounded-full bg-white px-2.5 py-1 text-[10px] font-bold uppercase tracking-wide text-forest-700">{e(s)}</span>'
            for s in p.get("specs", [])
        )
        featured = i == 0
        extra = (
            " bg-forest-900 p-5 text-left text-white"
            if featured
            else " bg-mist p-5 text-left"
        )
        spec_cls = "bg-white/10 text-forest-300" if featured else "bg-white text-forest-700"
        specs = "".join(
            f'<span class="rounded-full {spec_cls} px-2.5 py-1 text-[10px] font-bold uppercase tracking-wide">{e(s)}</span>'
            for s in p.get("specs", [])
        )
        title_cls = "text-white" if featured else "text-ink"
        desc_cls = "text-white/60" if featured else "text-ink/55"
        cta_cls = "text-forest-300" if featured else "text-forest-700"
        icon_wrap = "bg-white/10 text-forest-300" if featured else "bg-forest-100 text-forest-700"
        bits.append(
            f'''
          <button type="button" id="{e(p["id"])}" data-product="{e(p["id"])}" data-unit="units" class="product-card group rounded-3xl border border-forest-800/10{extra}">
            <div class="flex h-12 w-12 items-center justify-center rounded-2xl {icon_wrap}"><i class="fa-solid {icon}"></i></div>
            <h3 class="mt-5 text-lg font-bold {title_cls}">{e(p["name"])}</h3>
            <div class="mt-3 flex flex-wrap gap-2">{specs}</div>
            <p class="mt-3 text-sm {desc_cls}">{e(p.get("cardDesc", ""))}</p>
            <p class="mt-2 text-xs {desc_cls}">Key ingredients: {e(p.get("ingredients", "—"))}</p>
            <span class="mt-4 inline-flex items-center gap-2 text-sm font-bold {cta_cls}">Quote this SKU <i class="fa-solid fa-arrow-right text-xs transition group-hover:translate-x-1"></i></span>
          </button>'''
        )
    return "\n".join(bits)


def faq_html(faqs: list[tuple[str, str]]) -> str:
    out = []
    for q, a in faqs:
        out.append(
            f'''
            <details class="faq group rounded-2xl border border-forest-800/10 bg-white px-5 py-4">
              <summary class="flex cursor-pointer list-none items-center justify-between gap-4 text-sm font-bold text-ink">
                {e(q)}
                <span class="faq-icon flex h-7 w-7 shrink-0 items-center justify-center rounded-full bg-forest-100 text-forest-700 transition">+</span>
              </summary>
              <p class="mt-3 text-sm leading-relaxed text-ink/60">{e(a)}</p>
            </details>'''
        )
    return "\n".join(out)


def options_html(products: list[dict]) -> str:
    return "\n".join(f'                  <option value="{e(p["id"])}">{e(p["name"])}</option>' for p in products)


def why_html(whys: list[tuple[str, str]], icon: str) -> str:
    out = []
    for t, d in whys:
        out.append(
            f'''
          <article class="rounded-3xl border border-forest-800/10 bg-white p-6 shadow-glass">
            <div class="flex h-11 w-11 items-center justify-center rounded-2xl bg-forest-100 text-forest-700"><i class="fa-solid {icon}"></i></div>
            <h3 class="mt-5 text-lg font-bold text-ink">{e(t)}</h3>
            <p class="mt-2 text-sm leading-relaxed text-ink/55">{e(d)}</p>
          </article>'''
        )
    return "\n".join(out)


def cred_html(creds: list[tuple[str, str]]) -> str:
    return "\n".join(
        f'''        <div>
          <p class="font-display text-lg font-semibold">{e(t)}</p>
          <p class="mt-1 text-xs text-white/55">{e(d)}</p>
        </div>'''
        for t, d in creds
    )


def cat_nav_links(current: str) -> str:
    items = []
    for href, label in CAT_LINKS:
        slug = href.strip("/.").split("/")[-1] if False else href.replace("../", "").rstrip("/")
        active = slug == current
        cls = "text-sm font-bold text-forest-800" if active else "text-sm font-semibold text-ink/80 hover:text-forest-800"
        items.append(f'        <a href="{href}" class="{cls}">{e(label)}</a>')
    return "\n".join(items[:5])  # keep header uncluttered; rest in footer


def page_html(key: str) -> str:
    cfg = PAGES[key]
    meta = META[key]
    products = cfg["products"]
    stats = "".join(
        f'<div><p class="font-display text-2xl font-semibold">{e(v)}</p><p class="mt-1 text-[11px] uppercase tracking-wider text-white/50">{e(l)}</p></div>'
        for v, l in cfg["stats"]
    )
    footer_products = "\n".join(
        f'          <li><a href="{href}" class="hover:text-white">{e(label)}</a></li>' for href, label in CAT_LINKS
    )
    return f'''<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{e(meta["title_tag"])}</title>
  <meta name="description" content="{e(meta["desc"])}" />
  <link rel="icon" href="../assets/cropped-ChatGPT-Image-Aug-6-2026-12_16_26-PM-75x75.png" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet" />
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      theme: {{
        extend: {{
          colors: {{
            forest: {{
              950: '#031810', 900: '#062a20', 800: '#0a3d2e', 700: '#0f5240',
              600: '#147a5c', 500: '#1a9a74', 400: '#2db890', 300: '#6fd4b0',
              100: '#e6f7f0', 50: '#f3fbf7',
            }},
            mist: '#f6f8f6',
            ink: '#0c1612',
          }},
          fontFamily: {{
            sans: ['"Plus Jakarta Sans"', 'system-ui', 'sans-serif'],
            display: ['Fraunces', 'Georgia', 'serif'],
          }},
          boxShadow: {{
            glass: '0 8px 32px rgba(6, 42, 32, 0.12)',
            lift: '0 20px 50px rgba(6, 42, 32, 0.18)',
          }},
        }},
      }},
    }};
  </script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" />
  <style>
    body {{ background: #f6f8f6; color: #0c1612; font-family: 'Plus Jakarta Sans', system-ui, sans-serif; }}
    .font-display {{ font-family: Fraunces, Georgia, serif; }}
    .glass-nav {{
      background: rgba(255,255,255,0.72);
      backdrop-filter: blur(18px) saturate(1.4);
      -webkit-backdrop-filter: blur(18px) saturate(1.4);
      border: 1px solid rgba(255,255,255,0.55);
      box-shadow: 0 10px 40px rgba(6,42,32,0.08);
    }}
    .glass-nav.is-scrolled {{ background: rgba(255,255,255,0.9); }}
    .hero-mesh {{
      background:
        radial-gradient(ellipse 70% 50% at 80% 30%, rgba(26,154,116,0.32), transparent 55%),
        linear-gradient(155deg, #031810 0%, #062a20 50%, #0a3d2e 100%);
    }}
    .reveal {{ opacity: 0; transform: translateY(24px); transition: opacity .7s ease, transform .7s ease; }}
    .reveal.visible {{ opacity: 1; transform: translateY(0); }}
    .product-card {{ transition: transform .35s ease, box-shadow .35s ease, border-color .35s ease; }}
    .product-card:hover {{ transform: translateY(-4px); box-shadow: 0 24px 48px rgba(6,42,32,0.14); border-color: rgba(26,154,116,.35); }}
    .product-card.is-selected {{ border-color: #1a9a74; box-shadow: 0 0 0 3px rgba(26,154,116,.18); }}
    details.faq summary::-webkit-details-marker {{ display: none; }}
    details.faq[open] .faq-icon {{ transform: rotate(45deg); }}
    input:focus, select:focus, textarea:focus {{
      outline: none; border-color: #1a9a74; box-shadow: 0 0 0 3px rgba(26,154,116,.18);
    }}
    .qty-hint.invalid {{ color: #b45309; }}
  </style>
</head>
<body class="antialiased overflow-x-hidden">
  <header class="fixed top-0 inset-x-0 z-50 px-4 pt-4 md:px-6 md:pt-5">
    <nav id="navbar" class="glass-nav mx-auto flex max-w-6xl items-center justify-between rounded-2xl px-4 py-3 md:px-6 transition-all" aria-label="Primary">
      <a href="../" class="flex items-center gap-2.5 group">
        <img src="../assets/ChatGPT-Image-Aug-6-2026-12_16_26-PM.png" alt="Vivid Nutripharm" class="h-10 w-10 rounded-full object-cover ring-2 ring-forest-100 transition-transform group-hover:scale-105" />
        <span class="text-sm font-extrabold tracking-[0.14em] text-forest-900 uppercase">Vivid Nutripharm</span>
      </a>
      <div class="hidden items-center gap-6 lg:flex">
        <a href="../#solutions" class="text-sm font-semibold text-ink/80 hover:text-forest-800">Solutions</a>
        <a href="./" class="text-sm font-bold text-forest-800">{e(meta["nav"])}</a>
        <a href="#products" class="text-sm font-semibold text-ink/80 hover:text-forest-800">Products</a>
        <a href="#quote" class="inline-flex items-center gap-2 rounded-full bg-forest-800 px-5 py-2.5 text-sm font-semibold text-white transition-all hover:-translate-y-0.5 hover:bg-forest-700 hover:shadow-lift">
          Request Quote <i class="fa-solid fa-arrow-right text-xs"></i>
        </a>
      </div>
      <button id="menuBtn" type="button" class="lg:hidden inline-flex h-11 w-11 items-center justify-center rounded-xl border border-forest-800/10 bg-white/60 text-forest-800" aria-label="Open menu" aria-expanded="false">
        <i class="fa-solid fa-bars"></i>
      </button>
    </nav>
    <div id="mobileMenu" class="mx-auto mt-2 hidden max-w-6xl rounded-2xl border border-white/50 bg-white/95 p-4 shadow-lift backdrop-blur-xl lg:hidden">
      <a href="../#solutions" class="mobile-link block rounded-xl px-4 py-3 text-sm font-semibold hover:bg-forest-50">Solutions</a>
      <a href="#products" class="mobile-link block rounded-xl px-4 py-3 text-sm font-semibold hover:bg-forest-50">Products</a>
      <a href="#quote" class="mobile-link mt-2 block rounded-xl bg-forest-800 px-4 py-3 text-center text-sm font-semibold text-white">Request Quote</a>
    </div>
  </header>

  <main>
    <section class="hero-mesh relative overflow-hidden text-white">
      <div class="relative mx-auto max-w-6xl px-6 pb-20 pt-36 md:pb-28 md:pt-44 lg:px-8">
        <p class="text-[11px] font-bold uppercase tracking-[0.28em] text-forest-300">{e(cfg["eyebrow"])}</p>
        <h1 class="font-display mt-4 max-w-3xl text-[clamp(2.1rem,5vw,3.8rem)] font-semibold leading-[1.08] tracking-tight">{e(cfg["title"])}</h1>
        <p class="mt-5 max-w-2xl text-base leading-relaxed text-white/70 md:text-lg">{e(cfg["intro"])}</p>
        <div class="mt-9 flex flex-wrap gap-3">
          <a href="#products" class="inline-flex items-center gap-2 rounded-full bg-white px-7 py-3.5 text-sm font-bold text-forest-900 transition-all hover:-translate-y-0.5 hover:shadow-lift">
            View products <i class="fa-solid fa-arrow-down text-xs"></i>
          </a>
          <a href="#quote" class="inline-flex items-center gap-2 rounded-full border border-white/25 bg-white/5 px-7 py-3.5 text-sm font-semibold text-white backdrop-blur-md transition-all hover:-translate-y-0.5 hover:bg-white/10">
            Request a quote
          </a>
        </div>
        <div class="mt-12 grid max-w-3xl grid-cols-2 gap-6 sm:grid-cols-4">{stats}</div>
      </div>
    </section>

    <section class="bg-forest-800 py-8 text-white">
      <div class="mx-auto grid max-w-6xl gap-6 px-6 sm:grid-cols-2 lg:grid-cols-4 lg:px-8">
{cred_html(cfg["creds"])}
      </div>
    </section>

    <section class="bg-mist py-20 md:py-24">
      <div class="mx-auto max-w-6xl px-6 lg:px-8">
        <div class="reveal max-w-2xl">
          <p class="text-xs font-bold uppercase tracking-[0.22em] text-forest-600">Why this range</p>
          <h2 class="font-display mt-4 text-3xl font-semibold text-ink md:text-4xl">Differentiated formats, partner-ready supply.</h2>
          <p class="mt-4 text-base text-ink/60">{e(cfg["note"])}</p>
        </div>
        <div class="reveal mt-12 grid gap-5 sm:grid-cols-2 lg:grid-cols-4">
{why_html(cfg["whys"], meta["icon"])}
        </div>
      </div>
    </section>

    <section id="products" class="bg-white py-24 md:py-32">
      <div class="mx-auto max-w-6xl px-6 lg:px-8">
        <div class="reveal max-w-2xl">
          <p class="text-xs font-bold uppercase tracking-[0.22em] text-forest-600">Product list</p>
          <h2 class="font-display mt-4 text-3xl font-semibold text-ink md:text-5xl">{e(cfg["products_h2"])}</h2>
          <p class="mt-4 text-base text-ink/60">{e(cfg["products_p"])} Select a SKU to prefill your quote.</p>
        </div>
        <div class="reveal mt-14 grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
{product_cards(products, meta["icon"])}
        </div>
      </div>
    </section>

    <section class="bg-mist py-24 md:py-32">
      <div class="mx-auto grid max-w-6xl gap-12 px-6 lg:grid-cols-12 lg:gap-14 lg:px-8">
        <div id="faq" class="reveal lg:col-span-5">
          <p class="text-xs font-bold uppercase tracking-[0.22em] text-forest-600">Partner FAQs</p>
          <h2 class="font-display mt-4 text-3xl font-semibold text-ink md:text-4xl">Before you request a quote</h2>
          <div class="mt-8 space-y-3">
{faq_html(cfg["faqs"])}
          </div>
        </div>
        <div id="quote" class="reveal lg:col-span-7">
          <div class="rounded-[2rem] border border-forest-800/10 bg-white p-6 shadow-glass md:p-8">
            <p class="text-xs font-bold uppercase tracking-[0.22em] text-forest-600">Partner enquiry</p>
            <h2 class="font-display mt-3 text-2xl font-semibold text-ink md:text-3xl">Request a quote</h2>
            <p class="mt-2 text-sm text-ink/55">Tell us the product and quantity — our team will come back with pricing and lead time.</p>
            <form id="quoteForm" class="mt-8 space-y-4">
              <label class="block text-sm font-medium text-ink/80">
                Full name *
                <input required name="name" type="text" placeholder="Your name" class="mt-1.5 w-full rounded-xl border border-forest-800/15 bg-mist px-4 py-3 text-sm" />
              </label>
              <label class="block text-sm font-medium text-ink/80">
                Product *
                <select required id="cf-product" name="product" class="mt-1.5 w-full rounded-xl border border-forest-800/15 bg-mist px-4 py-3 text-sm">
{options_html(products)}
                </select>
              </label>
              <div class="grid gap-4 sm:grid-cols-2">
                <label class="block text-sm font-medium text-ink/80">
                  Unit *
                  <select required id="cf-unit" name="unit" class="mt-1.5 w-full rounded-xl border border-forest-800/15 bg-mist px-4 py-3 text-sm">
                    <option value="units">Units (packs)</option>
                    <option value="kg">Kilograms (kg)</option>
                  </select>
                </label>
                <label class="block text-sm font-medium text-ink/80">
                  Quantity *
                  <input required id="cf-qty" name="quantity" type="number" min="500" step="1" placeholder="e.g. 500" class="mt-1.5 w-full rounded-xl border border-forest-800/15 bg-mist px-4 py-3 text-sm" />
                </label>
              </div>
              <span id="qtyHint" class="qty-hint block text-xs text-ink/45">Minimum order: 500 units.</span>
              <div class="grid gap-4 sm:grid-cols-2">
                <label class="block text-sm font-medium text-ink/80">
                  Mobile number *
                  <input required name="mobile" type="tel" placeholder="+91 98765 43210" class="mt-1.5 w-full rounded-xl border border-forest-800/15 bg-mist px-4 py-3 text-sm" />
                </label>
                <label class="block text-sm font-medium text-ink/80">
                  Email *
                  <input required name="email" type="email" placeholder="you@company.com" class="mt-1.5 w-full rounded-xl border border-forest-800/15 bg-mist px-4 py-3 text-sm" />
                </label>
              </div>
              <label class="block text-sm font-medium text-ink/80">
                Delivery location *
                <input required name="location" type="text" placeholder="City, country" class="mt-1.5 w-full rounded-xl border border-forest-800/15 bg-mist px-4 py-3 text-sm" />
              </label>
              <label class="block text-sm font-medium text-ink/80">
                Notes (optional)
                <textarea name="notes" rows="3" placeholder="Flavour, dose, private-label needs…" class="mt-1.5 w-full resize-y rounded-xl border border-forest-800/15 bg-mist px-4 py-3 text-sm"></textarea>
              </label>
              <button type="submit" class="inline-flex w-full items-center justify-center gap-2 rounded-full bg-forest-800 px-6 py-3.5 text-sm font-bold text-white transition-all hover:-translate-y-0.5 hover:bg-forest-700 hover:shadow-lift sm:w-auto">
                Submit enquiry <i class="fa-solid fa-paper-plane text-xs"></i>
              </button>
              <p id="quoteStatus" class="hidden text-sm font-medium text-forest-600" role="status"></p>
            </form>
          </div>
        </div>
      </div>
    </section>

    <section class="bg-forest-900 py-16 text-center text-white">
      <div class="mx-auto max-w-2xl px-6">
        <p class="text-base text-white/70">Looking for another category?</p>
        <a href="../#solutions" class="mt-4 inline-flex items-center gap-2 text-sm font-bold text-white transition hover:gap-3">
          See all solutions <i class="fa-solid fa-arrow-right text-xs"></i>
        </a>
      </div>
    </section>
  </main>

  <footer class="bg-forest-950 text-white">
    <div class="mx-auto grid max-w-6xl gap-10 px-6 py-14 md:grid-cols-3 lg:px-8">
      <div>
        <div class="flex items-center gap-3">
          <img src="../assets/ChatGPT-Image-Aug-6-2026-12_16_26-PM.png" alt="" class="h-10 w-10 rounded-full object-cover" />
          <span class="text-sm font-extrabold uppercase tracking-[0.14em]">Vivid Nutripharm</span>
        </div>
        <p class="mt-4 text-sm leading-relaxed text-white/55">Differentiated wellness manufacturing for brands that move the industry forward.</p>
      </div>
      <div>
        <h4 class="text-xs font-bold uppercase tracking-[0.18em] text-white/40">Products</h4>
        <ul class="mt-4 space-y-2 text-sm text-white/70">
{footer_products}
        </ul>
      </div>
      <div>
        <h4 class="text-xs font-bold uppercase tracking-[0.18em] text-white/40">Contact</h4>
        <ul class="mt-4 space-y-2 text-sm text-white/70">
          <li><a href="tel:7036300776" class="hover:text-white">7036300776</a> · <a href="tel:8179678794" class="hover:text-white">8179678794</a></li>
          <li><a href="mailto:info@vividnutripharm.com" class="hover:text-white">info@vividnutripharm.com</a></li>
          <li>Miyapur, Hyderabad-500049, India</li>
        </ul>
      </div>
    </div>
    <div class="border-t border-white/10 px-6 py-5 text-center text-xs text-white/40">© 2026 Vivid Nutripharm. All rights reserved.</div>
  </footer>

  <script>
    const navbar = document.getElementById('navbar');
    const menuBtn = document.getElementById('menuBtn');
    const mobileMenu = document.getElementById('mobileMenu');
    const productSelect = document.getElementById('cf-product');
    const unitSelect = document.getElementById('cf-unit');
    const qtyInput = document.getElementById('cf-qty');
    const qtyHint = document.getElementById('qtyHint');

    function moqFor(unit) {{ return unit === 'units' ? 500 : 10; }}
    function updateMoqHint() {{
      const unit = unitSelect.value;
      const min = moqFor(unit);
      const label = unit === 'units' ? '500 units' : '10 kg';
      qtyHint.textContent = 'Minimum order: ' + label + '.';
      qtyInput.min = String(min);
      const qty = Number(qtyInput.value);
      if (qtyInput.value && qty < min) {{
        qtyHint.classList.add('invalid');
        qtyHint.textContent = 'Please enter at least ' + label + ' for this unit.';
      }} else {{
        qtyHint.classList.remove('invalid');
      }}
    }}
    function selectProduct(product, unit) {{
      productSelect.value = product;
      if (unit) unitSelect.value = unit;
      document.querySelectorAll('.product-card').forEach((card) => {{
        card.classList.toggle('is-selected', card.dataset.product === product);
      }});
      updateMoqHint();
    }}
    window.addEventListener('scroll', () => {{
      navbar.classList.toggle('is-scrolled', window.scrollY > 40);
    }}, {{ passive: true }});
    menuBtn.addEventListener('click', () => {{
      const open = !mobileMenu.classList.contains('hidden');
      mobileMenu.classList.toggle('hidden', open);
      menuBtn.setAttribute('aria-expanded', String(!open));
      menuBtn.innerHTML = open ? '<i class="fa-solid fa-bars"></i>' : '<i class="fa-solid fa-xmark"></i>';
    }});
    document.querySelectorAll('.mobile-link').forEach((link) => {{
      link.addEventListener('click', () => {{
        mobileMenu.classList.add('hidden');
        menuBtn.setAttribute('aria-expanded', 'false');
        menuBtn.innerHTML = '<i class="fa-solid fa-bars"></i>';
      }});
    }});
    document.querySelectorAll('.product-card').forEach((card) => {{
      card.addEventListener('click', () => {{
        selectProduct(card.dataset.product, card.dataset.unit);
        document.getElementById('quote').scrollIntoView({{ behavior: 'smooth', block: 'start' }});
      }});
    }});
    productSelect.addEventListener('change', () => selectProduct(productSelect.value, unitSelect.value));
    unitSelect.addEventListener('change', updateMoqHint);
    qtyInput.addEventListener('input', updateMoqHint);
    updateMoqHint();
    const params = new URLSearchParams(location.search);
    const pre = params.get('product') || (location.hash || '').replace('#', '');
    if (pre && document.querySelector('[data-product="' + pre + '"]')) {{
      selectProduct(pre, 'units');
    }}
    document.getElementById('quoteForm').addEventListener('submit', async (e) => {{
      e.preventDefault();
      const form = e.currentTarget;
      if (!form.checkValidity()) {{ form.reportValidity(); return; }}
      const min = moqFor(unitSelect.value);
      if (Number(qtyInput.value) < min) {{ updateMoqHint(); qtyInput.focus(); return; }}
      const status = document.getElementById('quoteStatus');
      const submitBtn = form.querySelector('button[type="submit"]');
      const originalBtnHtml = submitBtn.innerHTML;
      const data = Object.fromEntries(new FormData(form).entries());
      status.classList.remove('hidden', 'text-red-600');
      status.classList.add('text-forest-600');
      status.textContent = 'Sending your enquiry…';
      submitBtn.disabled = true;
      submitBtn.innerHTML = 'Sending…';
      try {{
        const res = await fetch('https://formsubmit.co/ajax/info@vividnutripharm.com', {{
          method: 'POST',
          headers: {{ 'Content-Type': 'application/json', Accept: 'application/json' }},
          body: JSON.stringify({{
            _subject: `Quote request: ${{data.product}}`,
            _template: 'table',
            _captcha: 'false',
            ...data,
          }}),
        }});
        if (!res.ok) throw new Error('fail');
        status.textContent = 'Thanks — your enquiry was sent. Our team will follow up shortly.';
        form.reset();
        updateMoqHint();
      }} catch (err) {{
        status.classList.remove('text-forest-600');
        status.classList.add('text-red-600');
        status.textContent = 'Could not send right now. Please email info@vividnutripharm.com directly.';
      }} finally {{
        submitBtn.disabled = false;
        submitBtn.innerHTML = originalBtnHtml;
      }}
    }});
    const observer = new IntersectionObserver((entries) => {{
      entries.forEach((entry) => {{
        if (entry.isIntersecting) {{
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }}
      }});
    }}, {{ threshold: 0.12, rootMargin: '0px 0px -40px 0px' }});
    document.querySelectorAll('.reveal').forEach((el) => observer.observe(el));
  </script>
</body>
</html>
'''


def home_strip_item(href: str, name: str, spec: str, icon: str) -> str:
    return f'''            <a href="{href}" class="w-44 shrink-0 snap-start rounded-2xl border border-forest-800/8 bg-white p-4 text-center transition hover:-translate-y-1 hover:shadow-glass">
              <div class="mx-auto flex h-12 w-12 items-center justify-center rounded-2xl bg-forest-100 text-forest-700"><i class="fa-solid {icon}"></i></div>
              <span class="mt-3 block text-xs font-semibold text-ink">{e(name)}</span>
              <span class="mt-1 block text-[11px] text-ink/45">{e(spec)}</span>
            </a>'''


def patch_homepage() -> None:
    path = ROOT / "index.html"
    html_src = path.read_text()

    html_src = html_src.replace(
        '<a href="#contact" class="bento-card rounded-3xl border border-forest-800/10 bg-mist p-6 transition-colors hover:bg-forest-50">\n            <i class="fa-solid fa-spray-can text-forest-600"></i>\n            <h3 class="mt-6 text-lg font-bold text-ink">Oral Sprays</h3>',
        '<a href="./oral-sprays/" class="bento-card rounded-3xl border border-forest-800/10 bg-mist p-6 transition-colors hover:bg-forest-50">\n            <i class="fa-solid fa-spray-can text-forest-600"></i>\n            <h3 class="mt-6 text-lg font-bold text-ink">Oral Sprays</h3>',
    )
    html_src = html_src.replace(
        '<a href="#contact" class="bento-card rounded-3xl border border-forest-800/10 bg-mist p-6 hover:bg-forest-50">\n            <i class="fa-solid fa-dna text-forest-600"></i>\n            <h3 class="mt-6 text-lg font-bold text-ink">Phytosomes</h3>',
        '<a href="./phytosomes/" class="bento-card rounded-3xl border border-forest-800/10 bg-mist p-6 hover:bg-forest-50">\n            <i class="fa-solid fa-dna text-forest-600"></i>\n            <h3 class="mt-6 text-lg font-bold text-ink">Phytosomes</h3>',
    )
    html_src = html_src.replace(
        '<a href="#contact" class="bento-card rounded-3xl border border-forest-800/10 bg-mist p-6 hover:bg-forest-50">\n            <i class="fa-solid fa-heart-pulse text-forest-600"></i>\n            <h3 class="mt-6 text-lg font-bold text-ink">Chronic Disease</h3>',
        '<a href="./chronic-disease-management/" class="bento-card rounded-3xl border border-forest-800/10 bg-mist p-6 hover:bg-forest-50">\n            <i class="fa-solid fa-heart-pulse text-forest-600"></i>\n            <h3 class="mt-6 text-lg font-bold text-ink">Chronic Disease</h3>',
    )
    html_src = html_src.replace(
        '<a href="#contact" class="bento-card rounded-3xl border border-forest-800/10 bg-mist p-6 hover:bg-forest-50">\n            <i class="fa-solid fa-person text-forest-600"></i>\n            <h3 class="mt-6 text-lg font-bold text-ink">Men’s Wellness</h3>',
        '<a href="./mens-sexual-wellness/" class="bento-card rounded-3xl border border-forest-800/10 bg-mist p-6 hover:bg-forest-50">\n            <i class="fa-solid fa-person text-forest-600"></i>\n            <h3 class="mt-6 text-lg font-bold text-ink">Men’s Wellness</h3>',
    )
    html_src = html_src.replace(
        '<a href="#contact" class="bento-card rounded-3xl border border-forest-800/10 bg-mist p-6 hover:bg-forest-50">\n            <i class="fa-solid fa-venus text-forest-600"></i>\n            <h3 class="mt-6 text-lg font-bold text-ink">Women Wellness</h3>',
        '<a href="./women-wellness/" class="bento-card rounded-3xl border border-forest-800/10 bg-mist p-6 hover:bg-forest-50">\n            <i class="fa-solid fa-venus text-forest-600"></i>\n            <h3 class="mt-6 text-lg font-bold text-ink">Women Wellness</h3>',
    )
    html_src = html_src.replace(
        '<a href="#contact" class="bento-card rounded-3xl border border-forest-800/10 bg-mist p-6 hover:bg-forest-50">\n            <i class="fa-solid fa-glass-water text-forest-600"></i>\n            <h3 class="mt-6 text-lg font-bold text-ink">Effervescent</h3>',
        '<a href="./effervescent/" class="bento-card rounded-3xl border border-forest-800/10 bg-mist p-6 hover:bg-forest-50">\n            <i class="fa-solid fa-glass-water text-forest-600"></i>\n            <h3 class="mt-6 text-lg font-bold text-ink">Effervescent</h3>',
    )
    html_src = html_src.replace(
        '<a href="#contact" class="bento-card rounded-3xl border border-forest-800/10 bg-forest-800 p-6 text-white lg:col-span-2">\n            <i class="fa-solid fa-leaf text-forest-300"></i>\n            <h3 class="mt-6 text-lg font-bold">Single Extracts</h3>',
        '<a href="./single-extracts/" class="bento-card rounded-3xl border border-forest-800/10 bg-forest-800 p-6 text-white lg:col-span-2">\n            <i class="fa-solid fa-leaf text-forest-300"></i>\n            <h3 class="mt-6 text-lg font-bold">Single Extracts</h3>',
    )

    html_src = html_src.replace(
        """          <li><a href="./durt-cordyceps-range/" class="hover:text-white">Cordyceps Range</a></li>
          <li><a href="#solutions" class="hover:text-white">Oral Sprays</a></li>
          <li><a href="#solutions" class="hover:text-white">Phytosomes</a></li>
          <li><a href="#solutions" class="hover:text-white">Effervescent</a></li>
          <li><a href="#solutions" class="hover:text-white">Single Extracts</a></li>""",
        """          <li><a href="./durt-cordyceps-range/" class="hover:text-white">Cordyceps Range</a></li>
          <li><a href="./oral-sprays/" class="hover:text-white">Oral Sprays</a></li>
          <li><a href="./phytosomes/" class="hover:text-white">Phytosomes</a></li>
          <li><a href="./chronic-disease-management/" class="hover:text-white">Chronic Disease</a></li>
          <li><a href="./mens-sexual-wellness/" class="hover:text-white">Men’s Wellness</a></li>
          <li><a href="./women-wellness/" class="hover:text-white">Women Wellness</a></li>
          <li><a href="./effervescent/" class="hover:text-white">Effervescent</a></li>
          <li><a href="./single-extracts/" class="hover:text-white">General Wellness</a></li>""",
    )

    start = html_src.find("        <!-- Cordyceps product strip -->")
    end = html_src.find("      </div>\n    </section>\n\n    <!-- Leaders -->")
    if start < 0 or end < 0:
        raise SystemExit("Could not find product strip in homepage")

    tabs = [
        ("cordyceps", "Our Cordyceps"),
        ("oral-sprays", "Oral Sprays"),
        ("phytosomes", "Phytosomes"),
        ("chronic-disease", "Chronic Disease"),
        ("mens-wellness", "Men’s Wellness"),
        ("women-wellness", "Women Wellness"),
        ("effervescent", "Effervescent"),
        ("single-extracts", "General Wellness"),
    ]
    tab_btns = []
    for i, (tid, label) in enumerate(tabs):
        active = "sol-tab-active bg-forest-800 text-white" if i == 0 else "bg-white text-ink/70 hover:bg-forest-50"
        tab_btns.append(
            f'<button type="button" class="sol-tab shrink-0 rounded-full border border-forest-800/10 px-4 py-2 text-xs font-bold {active}" data-sol="{tid}">{e(label)}</button>'
        )

    cordy_panel = html_src[html_src.find('          <div class="mb-6 flex items-center justify-between gap-4">'):html_src.find("          </div>\n        </div>\n      </div>\n    </section>\n\n    <!-- Leaders -->")]
    # The original inner of the strip starting at mb-6... keep as cordyceps panel content
    orig_inner_start = html_src.find('          <div class="mb-6 flex items-center justify-between gap-4">', start)
    orig_inner_end = html_src.find("          </div>\n        </div>\n      </div>\n    </section>", orig_inner_start)
    cordy_inner = html_src[orig_inner_start:orig_inner_end + len("          </div>")]

    def panel(pid: str, title: str, href: str, icon: str, products: list, extra: str = "") -> str:
        items = "\n".join(
            home_strip_item(f"{href}?product={p['id']}#quote", p["name"], p["specs"][0] if p.get("specs") else "", icon)
            for p in products
        )
        hidden = "" if pid == "cordyceps" else ' hidden'
        if extra:
            row = extra
        else:
            row = f'<div class="facility-track flex gap-4 overflow-x-auto pb-2">\n{items}\n          </div>'
        return f'''
          <div class="sol-panel{hidden}" data-sol-panel="{pid}">
            <div class="mb-6 flex items-center justify-between gap-4">
              <h3 class="text-sm font-bold uppercase tracking-[0.18em] text-forest-700">{e(title)}</h3>
              <a href="{href}" class="text-xs font-bold text-forest-700 transition hover:gap-2 inline-flex items-center gap-1.5">View all <i class="fa-solid fa-arrow-right text-[10px]"></i></a>
            </div>
            {row}
          </div>'''

    # reuse original cordyceps image strip as the first panel body
    cordy_row = html_src[html_src.find('          <div class="facility-track flex gap-4 overflow-x-auto pb-2">', start): html_src.find("          </div>\n        </div>\n      </div>\n    </section>\n\n    <!-- Leaders -->")]
    # facility-track block through its closing div
    ft_start = html_src.find('          <div class="facility-track flex gap-4 overflow-x-auto pb-2">', start)
    ft_end = html_src.find("\n        </div>\n      </div>\n    </section>\n\n    <!-- Leaders -->", ft_start)
    cordy_track = html_src[ft_start:ft_end].rstrip()
    if cordy_track.endswith("</div>"):
        pass

    panels = [
        panel("cordyceps", "Cordyceps highlight", "./durt-cordyceps-range/", "fa-seedling", [], extra=cordy_track),
        panel("oral-sprays", "Oral sprays", "./oral-sprays/", "fa-spray-can", PAGES["oral-sprays-2"]["products"]),
        panel("phytosomes", "Phytosomes", "./phytosomes/", "fa-dna", PAGES["phytosomes"]["products"]),
        panel("chronic-disease", "Chronic disease", "./chronic-disease-management/", "fa-heart-pulse", PAGES["chronic-disease-management"]["products"]),
        panel("mens-wellness", "Men’s wellness", "./mens-sexual-wellness/", "fa-person", PAGES["mens-sexual-wellness"]["products"]),
        panel("women-wellness", "Women wellness", "./women-wellness/", "fa-venus", PAGES["women-wellness"]["products"]),
        panel("effervescent", "Effervescent", "./effervescent/", "fa-glass-water", PAGES["effervescent"]["products"]),
        panel("single-extracts", "General wellness", "./single-extracts/", "fa-leaf", PAGES["single-extracts"]["products"]),
    ]

    new_block = f'''        <!-- Category product rows -->
        <div class="reveal mt-10 overflow-hidden rounded-3xl border border-forest-800/8 bg-mist p-6 md:p-8">
          <div id="solTabs" class="mb-6 flex gap-2 overflow-x-auto pb-1">
            {"".join(tab_btns)}
          </div>
          <div id="solPanels">
            {"".join(panels)}
          </div>
        </div>
'''

    html_src = html_src[:start] + new_block + html_src[end:]

    script_marker = "    // Active nav highlight"
    tab_script = '''
    const solTabs = document.querySelectorAll('#solTabs .sol-tab');
    const solPanels = document.querySelectorAll('#solPanels .sol-panel');
    solTabs.forEach((tab) => {
      tab.addEventListener('click', () => {
        const id = tab.getAttribute('data-sol');
        solTabs.forEach((t) => {
          t.classList.remove('sol-tab-active', 'bg-forest-800', 'text-white');
          t.classList.add('bg-white', 'text-ink/70');
        });
        tab.classList.add('sol-tab-active', 'bg-forest-800', 'text-white');
        tab.classList.remove('bg-white', 'text-ink/70');
        solPanels.forEach((p) => p.classList.toggle('hidden', p.getAttribute('data-sol-panel') !== id));
      });
    });

'''
    if "solTabs" not in html_src:
        html_src = html_src.replace(script_marker, tab_script + script_marker)

    path.write_text(html_src)
    print("patched homepage")


def main() -> None:
    for key, meta in META.items():
        dest = ROOT / meta["slug"] / "index.html"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(page_html(key))
        print("wrote", dest, len(PAGES[key]["products"]), "products")
    patch_homepage()


if __name__ == "__main__":
    main()
