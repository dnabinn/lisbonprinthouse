# -*- coding: utf-8 -*-
from build import *

def page_hero(depth, eyebrow, title, desc, crumbs):
  bc = " &rsaquo; ".join(f'<a href="{rel(depth,href)}">{label}</a>' if href else label for label, href in crumbs)
  return f"""
<section class="page-hero">
  <div class="container">
    <div class="breadcrumbs">{bc}</div>
    <div class="eyebrow" style="justify-content:center;display:flex;">{eyebrow}</div>
    <h1>{title}</h1>
    <p>{desc}</p>
  </div>
</section>"""

SERVICES = [
  dict(slug="business-card-printing", name="Business Card Printing", title="Business Card Printing in Lisbon",
    desc="Premium business cards with matte, gloss, soft-touch, or textured finishes â€” the first impression your business deserves.",
    img="https://images.unsplash.com/photo-1561015314-6bd8c1e875ee?w=900&q=80",
    benefits=["Premium 350â€“600gsm card stock options","Matte, gloss, soft-touch & spot-UV finishes","Rounded corners and custom shapes available","Low minimum order quantities","Digital proof before every order"],
    sizes=["Standard 85 x 55mm","Square 55 x 55mm","US Standard 89 x 51mm","Custom sizes on request"],
    paper=["350gsm Matte","400gsm Soft-Touch","450gsm Premium Gloss","600gsm Luxury (double-thick)"],
    finishes=["Matte Lamination","Gloss Lamination","Spot UV","Foil Stamping","Rounded Corners"],
    turnaround="Contact us on WhatsApp for current lead times.",
    faqs=[("What's the minimum order quantity?","We can print as few as 100 business cards, with better per-unit pricing at higher quantities."),
          ("Can I get double-sided printing?","Yes, double-sided printing is included as standard at no extra cost."),
          ("Do you offer design services?","Yes â€” our designers can build your business card from scratch or refine your existing files.")]),
  dict(slug="flyer-printing", name="Flyer Printing", title="Flyer & Folded Flyer Printing in Lisbon",
    desc="Bold, attention-grabbing flyers for promotions, events, and local marketing â€” printed fast on quality paper stock.",
    img="https://images.unsplash.com/photo-1695634621375-0b66a9d5d1bc?w=900&q=80",
    benefits=["Vivid full-color printing","Single and folded flyer formats","Bulk pricing for large campaigns","Easy reprints for recurring promotions","Free layout check before printing"],
    sizes=["A6 (105 x 148mm)","A5 (148 x 210mm)","A4 (210 x 297mm)","DL Folded (99 x 210mm)"],
    paper=["135gsm Gloss","170gsm Silk","250gsm Matte","300gsm Premium"],
    finishes=["Gloss or Matte Lamination","Single or Double-Sided","Bi-fold & Tri-fold options"],
    turnaround="Contact us on WhatsApp for current lead times.",
    faqs=[("Can you design my flyer?","Yes, our design team can create your flyer from a brief or rough idea."),
          ("What's the best paper for outdoor flyer distribution?","We recommend 170gsm silk or higher with gloss lamination for durability."),
          ("Do you offer folded flyers?","Yes, bi-fold and tri-fold formats are available in several standard sizes.")]),
  dict(slug="folded-flyer-printing", name="Folded Flyer Printing", title="Folded Flyer Printing (Bi-Fold & Tri-Fold) in Lisbon",
    desc="Professional bi-fold and tri-fold flyers ideal for menus, brochures-lite, and detailed promotions.",
    img="https://images.unsplash.com/photo-1630734242335-1555e4a438a0?w=900&q=80",
    benefits=["More space to tell your story than a flat flyer","Bi-fold and tri-fold formats","Crisp, accurate folding on every unit","Durable stock options for handouts","Digital proof before printing"],
    sizes=["DL Folded (99 x 210mm)","A5 Folded to A6","A4 Folded to A5 or DL"],
    paper=["170gsm Silk","250gsm Matte","300gsm Premium"],
    finishes=["Gloss or Matte Lamination","Score & Fold","Double-Sided Print"],
    turnaround="Contact us on WhatsApp for current lead times.",
    faqs=[("What's the difference between a flyer and a folded flyer?","A folded flyer gives you more panels and space for content while staying compact and easy to hand out."),
          ("Can I get tri-fold brochure-style flyers?","Yes, tri-fold is one of our most popular folded formats.")]),
  dict(slug="poster-printing", name="Poster Printing", title="Poster Printing in Lisbon",
    desc="Large-format posters for promotions, events, and in-store displays â€” sharp print quality at any size.",
    img="https://images.unsplash.com/photo-1563050860-87d45eaaeabb?w=900&q=80",
    benefits=["Vibrant large-format color printing","Indoor and outdoor-rated stock options","Custom sizes for any wall or window","Bulk pricing for multi-location campaigns","Colour-accurate digital proof included"],
    sizes=["A3 (297 x 420mm)","A2 (420 x 594mm)","A1 (594 x 841mm)","A0 (841 x 1189mm)","Custom sizes"],
    paper=["150gsm Poster Paper","200gsm Photo Gloss","Synthetic weatherproof stock"],
    finishes=["Matte or Gloss","Lamination for durability","Mounting on foam board (optional)"],
    turnaround="Contact us on WhatsApp for current lead times.",
    faqs=[("Can posters be used outdoors?","Yes, we offer weatherproof synthetic stock for outdoor placement."),
          ("Do you offer mounting?","Yes, foam board mounting is available as an add-on.")]),
  dict(slug="restaurant-menu-printing", name="Restaurant Menu Printing", title="Restaurant Menu Printing in Lisbon",
    desc="Durable, beautifully finished menus that survive daily handling and reflect your restaurant's brand.",
    img="https://images.unsplash.com/photo-1556742205-e10c9486e506?w=900&q=80",
    benefits=["Spill and wear-resistant laminate options","Multi-page and single-sheet formats","Custom sizes to match your table settings","Matches table cards, drink menus & signage","Quick reprints when prices change"],
    sizes=["A4","A5","Custom panel & booklet formats","Tabletop tent cards"],
    paper=["300gsm Matte with lamination","350gsm Soft-Touch","Synthetic waterproof stock"],
    finishes=["Gloss or Matte Lamination","Rounded Corners","Spiral or Saddle-Stitch Binding for multi-page menus"],
    turnaround="Contact us on WhatsApp for current lead times.",
    faqs=[("Can menus be laminated for durability?","Yes, lamination is recommended and included as an option on all menu orders."),
          ("Do you print multi-page menus?","Yes, we offer booklet-style menus with spiral or saddle-stitch binding."),
          ("Can you match my restaurant's branding?","Yes, our design team can align menus with your existing brand or build a new design.")]),
  dict(slug="banner-printing", name="PVC Banner Printing", title="PVC Banner Printing in Lisbon",
    desc="Big, bold, weatherproof banners for storefronts, events, and promotions â€” built to last outdoors.",
    img="https://images.unsplash.com/photo-1762888244575-779a9515174b?w=900&q=80",
    benefits=["Weatherproof PVC material","Vivid, fade-resistant printing","Reinforced hems and eyelets included","Custom sizes for any space","Optional installation in Lisbon"],
    sizes=["1m x 1m","2m x 1m","3m x 2m","Custom sizes available"],
    paper=["440gsm PVC Banner Material","510gsm Heavy-Duty PVC"],
    finishes=["Hemmed Edges","Eyelets for Hanging","Wind Slits for Outdoor Use"],
    turnaround="Contact us on WhatsApp for current lead times.",
    faqs=[("Are PVC banners weatherproof?","Yes, our PVC banners are designed for outdoor use in all weather conditions."),
          ("Do you offer installation?","Yes, installation is available within the Lisbon area.")]),
  dict(slug="roll-up-banner-printing", name="Roll-up Banner Printing", title="Roll-up Banner Printing in Lisbon",
    desc="Portable, professional roll-up banners perfect for events, trade shows, and in-store promotions.",
    img="https://images.unsplash.com/photo-1617355405361-29f0f0a3d737?w=900&q=80",
    benefits=["Lightweight, portable aluminum stand included","Quick assembly in under a minute","Scratch-resistant printed banner material","Carry case included","Vivid full-color printing"],
    sizes=["85 x 200cm (standard)","100 x 200cm","Custom sizes available"],
    paper=["220gsm Roll-up Banner Material (matte or satin)"],
    finishes=["Anti-curl coating","Scratch-resistant laminate"],
    turnaround="Contact us on WhatsApp for current lead times.",
    faqs=[("Does it come with a stand?","Yes, every roll-up banner includes a retractable aluminum stand and carry case."),
          ("Can I reuse the stand with a new banner later?","Yes, replacement banner prints can be ordered separately.")]),
  dict(slug="sticker-printing", name="Vinyl Sticker & Label Printing", title="Vinyl Sticker & Label Printing in Lisbon",
    desc="Custom-shaped vinyl stickers and labels for packaging, branding, and promotions.",
    img="https://images.unsplash.com/photo-1625768376503-68d2495d78c5?w=900&q=80",
    benefits=["Custom die-cut shapes","Waterproof, durable vinyl","Glossy or matte finish options","Great for packaging, branding & promos","Low minimums for small businesses"],
    sizes=["Custom shapes & sizes","Standard circles, squares & rectangles"],
    paper=["Vinyl (glossy)","Vinyl (matte)","Clear/Transparent Vinyl"],
    finishes=["Die-Cut to Shape","Laminate Overcoat for Durability"],
    turnaround="Contact us on WhatsApp for current lead times.",
    faqs=[("Are the stickers waterproof?","Yes, our vinyl stickers are waterproof and suitable for outdoor and packaging use."),
          ("Can I order custom shapes?","Yes, we die-cut to any custom shape you need.")]),
  dict(slug="window-graphics-printing", name="Window Graphics Printing", title="Window Graphics & Vinyl Printing in Lisbon",
    desc="Eye-catching window vinyl that turns your storefront into a silent salesperson.",
    img="https://images.unsplash.com/photo-1781617320919-1ac35d5f2443?w=900&q=80",
    benefits=["Full-color or cut vinyl lettering","One-way vision film options","Professional installation available","Removable without residue","Custom shapes and sizes"],
    sizes=["Custom â€” measured to your window"],
    paper=["Self-adhesive vinyl","Perforated one-way vision film","Frosted vinyl"],
    finishes=["Cut-to-shape lettering/logos","Full-color printed graphics","UV laminate for fade resistance"],
    turnaround="Contact us on WhatsApp for current lead times.",
    faqs=[("Will the vinyl damage my windows?","No, our vinyl is designed for clean removal without residue."),
          ("Do you install the graphics?","Yes, professional installation is available in the Lisbon area.")]),
  dict(slug="packaging-printing", name="Packaging Printing", title="Custom Packaging Printing in Lisbon",
    desc="Branded packaging and boxes that protect your product and elevate your brand on every shelf.",
    img="https://images.unsplash.com/photo-1656543802898-41c8c46683a7?w=900&q=80",
    benefits=["Custom box sizes and structures","Full-color branded printing","Food-safe options for restaurants","Eco-friendly material options","Scalable for growing order volumes"],
    sizes=["Custom â€” based on your product"],
    paper=["Kraft Cardboard","White Lined Chipboard","Corrugated Board"],
    finishes=["Matte or Gloss Lamination","Spot UV Logo","Food-Safe Coating"],
    turnaround="Contact us on WhatsApp for current lead times.",
    faqs=[("Can packaging be food-safe?","Yes, we offer food-safe coatings and materials suitable for restaurants and cafÃ©s."),
          ("What's the minimum order for custom packaging?","Minimums vary by structure â€” message us with your product details for an exact quote.")]),
  dict(slug="booklet-printing", name="Booklet & Catalogue Printing", title="Booklet, Brochure & Catalogue Printing in Lisbon",
    desc="Multi-page booklets and catalogues, professionally bound and finished for a premium feel.",
    img="https://images.unsplash.com/photo-1614036634955-ae5e90f9b9eb?w=900&q=80",
    benefits=["Saddle-stitch or spiral binding","Professional-grade color accuracy","Custom page counts","Premium cover stock options","Ideal for catalogues, brochures & reports"],
    sizes=["A4","A5","Square format","Custom sizes"],
    paper=["150gsm Silk (inner pages)","300gsm Matte (cover)","Recycled stock options"],
    finishes=["Saddle-Stitch Binding","Spiral Binding","Matte or Gloss Lamination on Cover"],
    turnaround="Contact us on WhatsApp for current lead times.",
    faqs=[("What binding options are available?","We offer saddle-stitch and spiral binding depending on page count and use case."),
          ("Can I order a small batch to test the design?","Yes, small test batches are available before committing to a full print run.")]),
]

cards_html = ""
for s in SERVICES:
  cards_html += f"""<div class="service-card fade-up"><div class="thumb"><img src="{s['img']}" alt="{s['name']} Lisbon" loading="lazy"></div>
    <div class="body"><h3>{s['name']}</h3><p>{s['desc']}</p><a href="{s['slug']}.html" class="link">View Details {ICONS['arrow']}</a></div></div>"""

hub_body = page_hero(1,"Our Services","Printing Services for Every Business Need","From everyday essentials to large-format signage â€” explore our full range of printing services.", [("Home","index.html"),("Services",None)]) + f"""
<section><div class="container grid grid-3">{cards_html}</div></section>
"""
write("services/index.html", page(
  "Printing Services in Lisbon | Lisbon Print House",
  "Explore all printing services offered by Lisbon Print House: business cards, flyers, menus, banners, stickers, packaging, booklets and more.",
  1, "services", hub_body, "services/index.html",
  schema=org_schema()+breadcrumb_schema([("Home","index.html"),("Services","services/index.html")])
))

for s in SERVICES:
  benefits_html = "".join(f'<li>{ICONS["check"]}{b}</li>' for b in s["benefits"])
  sizes_html = "".join(f'<span class="badge">{x}</span>' for x in s["sizes"])
  paper_html = "".join(f'<span class="badge">{x}</span>' for x in s["paper"])
  finishes_html = "".join(f'<span class="badge">{x}</span>' for x in s["finishes"])
  faq_html = "".join(f'<details class="faq-item fade-up"><summary>{q}</summary><p>{a}</p></details>' for q, a in s["faqs"])

  body = page_hero(1, "Services", s["title"], s["desc"], [("Home","index.html"),("Services","services/index.html"),(s["name"],None)]) + f"""
<section>
  <div class="container hero-grid">
    <div class="fade-up">
      <h2>About This Service</h2>
      <p style="margin-bottom:24px;">{s['desc']} Every order is checked for color accuracy and finish quality before it leaves our production floor, so what you approve is exactly what you receive.</p>
      <h3 style="margin-bottom:14px;">Key Benefits</h3>
      <ul style="display:flex;flex-direction:column;gap:10px;">{benefits_html}</ul>
    </div>
    <div class="hero-media fade-up"><img src="{s['img']}" alt="{s['name']} sample" loading="lazy"></div>
  </div>
</section>
<section class="bg-soft">
  <div class="container grid grid-3">
    <div class="card fade-up"><h3>Available Sizes</h3><div style="margin-top:16px;">{sizes_html}</div></div>
    <div class="card fade-up"><h3>Paper & Material Options</h3><div style="margin-top:16px;">{paper_html}</div></div>
    <div class="card fade-up"><h3>Finishes</h3><div style="margin-top:16px;">{finishes_html}</div></div>
  </div>
  <div class="container">
    <div class="card fade-up" style="margin-top:28px;display:flex;align-items:center;gap:20px;">
      <div class="icon-wrap" style="width:56px;height:56px;border-radius:8px;background:#fff;display:flex;align-items:center;justify-content:center;color:var(--color-accent);flex-shrink:0;">{ICONS['clock']}</div>
      <div><strong>Turnaround Time</strong><p style="margin:0;">{s['turnaround']}</p></div>
    </div>
  </div>
</section>
<section>
  <div class="container">
    <div class="section-head center"><div class="eyebrow">Gallery</div><h2>Recent {s['name']} Work</h2></div>
    <div class="grid grid-3">
      <div class="masonry-item fade-up"><img src="{s['img']}" alt="{s['name']} example 1" loading="lazy"></div>
      <div class="masonry-item fade-up"><img src="https://images.unsplash.com/photo-1758183961426-88d64eb5f787?w=600&q=80" alt="{s['name']} production at Lisbon Print House" loading="lazy"></div>
      <div class="masonry-item fade-up"><img src="https://images.unsplash.com/photo-1773525912476-213bff96b8a4?w=600&q=80" alt="{s['name']} finishing process" loading="lazy"></div>
    </div>
  </div>
</section>
<section class="bg-soft">
  <div class="container">
    <div class="section-head center"><div class="eyebrow">FAQ</div><h2>Common Questions</h2></div>
    <div class="faq-list">{faq_html}</div>
  </div>
</section>
"""
  schema = org_schema() + breadcrumb_schema([("Home","index.html"),("Services","services/index.html"),(s["name"], f"services/{s['slug']}.html")]) + faq_schema(s["faqs"]) + f"""<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"Service","name":"{s['name']}","description":"{s['desc']}","provider":{{"@type":"LocalBusiness","name":"{BIZ}"}},"areaServed":"Portugal"}}
</script>"""

  write(f"services/{s['slug']}.html", page(
    f"{s['title']} | {BIZ}",
    f"{s['desc']} Premium materials, reliable quality, and pricing on WhatsApp.",
    1, "services", body, f"services/{s['slug']}.html", schema=schema
  ))

print(f"Built services hub + {len(SERVICES)} service pages.")
