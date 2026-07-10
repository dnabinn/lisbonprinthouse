# -*- coding: utf-8 -*-
from build import *

def page_hero(eyebrow, title, desc, crumbs):
  bc = " &rsaquo; ".join(f'<a href="{("../"*0)+href}">{label}</a>' if href else label for label, href in crumbs)
  return f"""
<section class="page-hero">
  <div class="container">
    <div class="breadcrumbs">{bc}</div>
    <div class="eyebrow" style="justify-content:center;display:flex;">{eyebrow}</div>
    <h1>{title}</h1>
    <p>{desc}</p>
  </div>
</section>"""

# ---------------- ABOUT ----------------
body = page_hero("About Us","Printing Lisbon's Businesses Since Day One","We're a Lisbon-based print shop on a mission to make premium printing simple, reliable, and accessible for every local business.", [("Home","index.html"),("About",None)]) + f"""
<section>
  <div class="container hero-grid">
    <div class="fade-up">
      <h2>A Print Partner, Not Just a Print Shop</h2>
      <p style="margin-bottom:20px;">Lisbon Print House was founded with one goal: give Lisbon's restaurants, retailers, and local businesses access to the kind of premium printing usually reserved for big national brands — without the slow quotes, confusing forms, or inflated prices.</p>
      <p style="margin-bottom:20px;">Today we work with hundreds of businesses across Portugal, from neighborhood cafés ordering their first menus to growing retail chains needing consistent signage across multiple locations.</p>
      <p>Every order goes through the same quality checks, runs on professional commercial equipment, and is backed by a team that actually picks up the phone — or replies on WhatsApp.</p>
    </div>
    <div class="hero-media fade-up"><img src="https://images.unsplash.com/photo-1773525912476-213bff96b8a4?w=800&q=80" alt="Lisbon Print House production team" loading="lazy"></div>
  </div>
</section>
<section class="bg-soft">
  <div class="container">
    <div class="section-head center"><div class="eyebrow">Our Values</div><h2>What Drives Every Order We Print</h2></div>
    <div class="grid grid-3">
      <div class="card icon-card fade-up"><div class="icon-wrap">{ICONS['shield']}</div><h3>Quality First</h3><p>We never cut corners on materials — every print reflects on your business, so it reflects our standards too.</p></div>
      <div class="card icon-card fade-up"><div class="icon-wrap">{ICONS['clock']}</div><h3>Clear Lead Times</h3><p>We give you an honest timeline upfront so you can plan around your order — no surprises, no chasing.</p></div>
      <div class="card icon-card fade-up"><div class="icon-wrap">{ICONS['wa']}</div><h3>Radically Simple</h3><p>One WhatsApp message instead of five-page forms. Print should be the easy part of running your business.</p></div>
    </div>
  </div>
</section>
<section>
  <div class="container grid grid-4 text-center">
    <div class="fade-up"><strong data-counter="300" style="font-size:2.4rem;font-weight:800;display:block;color:var(--color-primary);">0</strong><span>Businesses Served</span></div>
    <div class="fade-up"><strong data-counter="12000" style="font-size:2.4rem;font-weight:800;display:block;color:var(--color-primary);">0</strong><span>Orders Delivered</span></div>
    <div class="fade-up"><strong data-counter="5" style="font-size:2.4rem;font-weight:800;display:block;color:var(--color-primary);">0</strong><span>Years in Business</span></div>
    <div class="fade-up"><strong data-counter="18" style="font-size:2.4rem;font-weight:800;display:block;color:var(--color-primary);">0</strong><span>Districts Covered in Portugal</span></div>
  </div>
</section>
"""
write("about.html", page("About Us | Lisbon Print House","Learn about Lisbon Print House — a Lisbon-based commercial printer helping local businesses print faster, better, and at fair prices.",0,"about",body,"about.html",schema=org_schema()+breadcrumb_schema([("Home","index.html"),("About","about.html")])))

# ---------------- PRICING ----------------
plans = [
  ("Starter","Perfect for small batches and first orders.",False,["100 Business Cards (350gsm)","25 A5 Flyers","Digital proof before printing","Pickup in Lisbon"]),
  ("Business","Our most popular package for growing businesses.",True,["500 Business Cards (350gsm, soft-touch)","250 A5 Flyers","100 A2 Posters or 1 Roll-up Banner","Free design review","Portugal-wide delivery"]),
  ("Enterprise","For multi-location brands and bulk ordering.",False,["Custom quantities across all products","Dedicated account contact on WhatsApp","Volume-based pricing","Multi-location delivery scheduling"]),
]
plan_cards = ""
for name, desc, featured, feats in plans:
  ribbon = '<div class="ribbon">Most Popular</div>' if featured else ""
  plan_cards += f"""<div class="price-card fade-up {'featured' if featured else ''}">{ribbon}
    <h3>{name}</h3><p>{desc}</p>
    <div class="price">Custom <span>quote</span></div>
    <ul>{''.join(f'<li>{ICONS["check"]}{f}</li>' for f in feats)}</ul>
    <a href="#" class="btn {'btn-primary' if featured else 'btn-outline'} btn-block" data-wa data-wa-message="Hi! I'd like a quote for the {name} package.">{ICONS['wa']} Get Quote</a>
  </div>"""

body = page_hero("Pricing","Transparent, Fair Pricing for Every Business Size","Every order is unique, so every quote is too. Browse typical packages below, then get an exact price on WhatsApp in minutes.", [("Home","index.html"),("Pricing",None)]) + f"""
<section>
  <div class="container">
    <div class="grid grid-3">{plan_cards}</div>
    <p class="text-center" style="margin-top:32px;">Prices vary by quantity, paper stock, and finish. Message us on WhatsApp for an exact quote.</p>
  </div>
</section>
<section class="bg-soft">
  <div class="container">
    <div class="section-head center"><div class="eyebrow">Sample Pricing</div><h2>Typical Starting Prices</h2><p>Indicative pricing — final quote depends on quantity, finish, and materials.</p></div>
    <table class="table-clean">
      <tr><th>Product</th><th>Starting From</th></tr>
      <tr><td>Business Cards (100 units)</td><td>€25</td></tr>
      <tr><td>A5 Flyers (250 units)</td><td>€35</td></tr>
      <tr><td>Restaurant Menus (A4, laminated)</td><td>€2.50/unit</td></tr>
      <tr><td>PVC Banner (2m x 1m)</td><td>€45</td></tr>
      <tr><td>Roll-up Banner (85x200cm)</td><td>€65</td></tr>
      <tr><td>Vinyl Stickers (100 units)</td><td>€30</td></tr>
    </table>
  </div>
</section>
"""
write("pricing.html", page("Printing Prices in Lisbon | Lisbon Print House","See typical pricing for business cards, flyers, banners, menus and more. Get an exact quote fast on WhatsApp.",0,"pricing",body,"pricing.html",schema=org_schema()+breadcrumb_schema([("Home","index.html"),("Pricing","pricing.html")])))

# ---------------- INDUSTRIES ----------------
industries_data = [
  ("Restaurants & Cafés","Menus, table cards, packaging, and promotional flyers that match your brand and survive daily use.","https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=700&q=80"),
  ("Hotels","Guest directories, room signage, branded amenities materials, and lobby displays.","https://images.unsplash.com/photo-1551882547-ff40c63fe5fa?w=700&q=80"),
  ("Retail Stores","Window graphics, price cards, packaging, and promotional signage that drive foot traffic.","https://images.unsplash.com/photo-1441986300917-64674bd600d8?w=700&q=80"),
  ("Beauty Salons & Barbers","Loyalty cards, price lists, posters, and branded packaging for retail products.","https://images.unsplash.com/photo-1521590832167-7bcbfaa6381f?w=700&q=80"),
  ("Real Estate Agencies","Property flyers, yard signs, business cards, and branded brochures that close deals.","https://images.unsplash.com/photo-1560518883-ce09059eeffa?w=700&q=80"),
  ("Gyms & Fitness Studios","Class schedules, membership cards, motivational posters, and window vinyl.","https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=700&q=80"),
  ("Offices & Startups","Business cards, letterheads, branded stationery, and event signage.","https://images.unsplash.com/photo-1497366216548-37526070297c?w=700&q=80"),
  ("Bars & Nightlife","Event posters, drink menus, coasters, and promotional flyers.","https://images.unsplash.com/photo-1572116469696-31de0f17cc34?w=700&q=80"),
]
ind_cards = "".join(f"""<div class="service-card fade-up"><div class="thumb"><img src="{img}" alt="Printing for {name}" loading="lazy"></div>
  <div class="body"><h3>{name}</h3><p>{desc}</p><a href="#" class="link" data-wa data-wa-message="Hi! I run a {name.lower()} business and want to ask about printing options.">Talk to Us {ICONS['arrow']}</a></div></div>""" for name, desc, img in industries_data)

body = page_hero("Industries","Printing Solutions Tailored to Your Industry","We understand the specific printing needs of different businesses — because we've already solved them.", [("Home","index.html"),("Industries",None)]) + f"""
<section><div class="container grid grid-4">{ind_cards}</div></section>
"""
write("industries.html", page("Industries We Serve | Lisbon Print House","Printing solutions for restaurants, hotels, retail, salons, real estate, gyms and more across Lisbon and Portugal.",0,"industries",body,"industries.html",schema=org_schema()+breadcrumb_schema([("Home","index.html"),("Industries","industries.html")])))

# ---------------- FAQ ----------------
faqs = [
  ("How long does printing take?","Lead times vary by product and quantity. Contact us on WhatsApp with your order details and we'll confirm the exact timeline."),
  ("Do you deliver outside Lisbon?","Yes, we deliver to businesses across all of Portugal via trusted courier partners."),
  ("Can you design my artwork for me?","Absolutely — our in-house design team can create artwork from scratch or refine files you already have."),
  ("What file formats do you accept?","We accept PDF, AI, EPS, PSD, and high-resolution JPG/PNG files. Not sure if your file works? Send it on WhatsApp and we'll check."),
  ("What's the minimum order quantity?","It depends on the product. Many items like business cards and stickers have low minimums suited to small businesses."),
  ("How do I pay?","We accept bank transfer, MB Way, and card payment. Payment details are shared once your quote is confirmed."),
  ("Do you offer installation for banners or window graphics?","Yes, installation is available for banners, window graphics, and vinyl signage within the Lisbon area."),
  ("Can I order a sample before committing to a large order?","Yes, samples are available for most products — just ask when requesting your quote."),
  ("How do I get a price?","Send us a WhatsApp message describing what you need — product, quantity, and finish. We'll come back with a full quote."),
  ("Do you work with businesses outside Lisbon?","Yes, we proudly serve businesses across all of Portugal with nationwide delivery."),
]
faq_html = "".join(f'<details class="faq-item fade-up"><summary>{q}</summary><p>{a}</p></details>' for q, a in faqs)
body = page_hero("FAQ","Frequently Asked Questions","Everything you need to know about ordering printing from Lisbon Print House.", [("Home","index.html"),("FAQ",None)]) + f"""
<section><div class="container"><div class="faq-list">{faq_html}</div></div></section>
"""
write("faq.html", page("FAQ | Lisbon Print House","Answers to common questions about printing turnaround, delivery, pricing, file formats, and more.",0,"faq",body,"faq.html",schema=org_schema()+faq_schema(faqs)+breadcrumb_schema([("Home","index.html"),("FAQ","faq.html")])))

# ---------------- CONTACT ----------------
body = page_hero("Contact","Let's Start Your Next Print Project","Reach us on WhatsApp for the fastest response, or use the form below.", [("Home","index.html"),("Contact",None)]) + f"""
<section>
  <div class="container contact-grid">
    <div class="fade-up">
      <h2>Get In Touch</h2>
      <p style="margin-bottom:32px;">Message us on WhatsApp for the most direct response, or use the form below and we'll get back to you.</p>
      <div class="contact-info-item"><div class="icon-wrap">{ICONS['wa']}</div><div><strong>WhatsApp</strong><span>{PHONE_DISPLAY}</span></div></div>
      <div class="contact-info-item"><div class="icon-wrap">{ICONS['mail']}</div><div><strong>Email</strong><span>{EMAIL}</span></div></div>
      <div class="contact-info-item"><div class="icon-wrap">{ICONS['clock']}</div><div><strong>Business Hours</strong><span>{HOURS}</span></div></div>
      <div class="contact-info-item"><div class="icon-wrap">{ICONS['pin']}</div><div><strong>Service Area</strong><span>Lisbon, Portugal &mdash; nationwide delivery</span></div></div>
      <a href="#" class="btn btn-primary" data-wa>{ICONS['wa']} Message Us on WhatsApp</a>
      <div class="map-embed"><iframe src="https://www.google.com/maps?q=Lisbon,Portugal&output=embed" loading="lazy" title="Lisbon Print House location map"></iframe></div>
    </div>
    <div class="card fade-up">
      <h3 style="margin-bottom:20px;">Request a Quote</h3>
      <form id="quote-form">
        <div class="form-group"><label>Full Name</label><input type="text" name="name" required></div>
        <div class="form-group"><label>Service Needed</label>
          <select name="service">
            <option>Business Cards</option><option>Flyers</option><option>Restaurant Menus</option>
            <option>Banners</option><option>Stickers & Labels</option><option>Packaging</option><option>Other</option>
          </select>
        </div>
        <div class="form-group"><label>Project Details</label><textarea name="details" rows="4" placeholder="Quantity, sizes, deadline..."></textarea></div>
        <button type="submit" class="btn btn-primary btn-block">{ICONS['wa']} Send via WhatsApp</button>
      </form>
    </div>
  </div>
</section>
"""
write("contact.html", page("Contact Us | Lisbon Print House","Contact Lisbon Print House via WhatsApp, email, or our quote form. Based in Lisbon, delivering across Portugal.",0,"contact",body,"contact.html",schema=org_schema()+breadcrumb_schema([("Home","index.html"),("Contact","contact.html")])))

# ---------------- REQUEST QUOTE ----------------
body = page_hero("Request a Quote","Tell Us What You Need","Fill in a few details and we'll open WhatsApp with everything pre-filled. Or skip the form and message us directly.", [("Home","index.html"),("Request a Quote",None)]) + f"""
<section>
  <div class="container" style="max-width:640px;">
    <div class="card fade-up">
      <form id="quote-form">
        <div class="form-group"><label>Full Name</label><input type="text" name="name" required></div>
        <div class="form-group"><label>Service Needed</label>
          <select name="service">
            <option>Business Cards</option><option>Flyers</option><option>Folded Flyers</option><option>Posters</option>
            <option>Restaurant Menus</option><option>PVC Banners</option><option>Roll-up Banners</option>
            <option>Vinyl Stickers</option><option>Window Graphics</option><option>Labels</option><option>Packaging</option>
            <option>Brochures</option><option>Booklets</option><option>Catalogues</option><option>Graphic Design</option><option>Other</option>
          </select>
        </div>
        <div class="form-group"><label>Quantity</label><input type="text" name="details" placeholder="e.g. 500 units, A5 size, due in 1 week"></div>
        <button type="submit" class="btn btn-primary btn-block">{ICONS['wa']} Send via WhatsApp</button>
      </form>
      <p class="text-center" style="margin-top:20px;font-size:0.85rem;">Prefer to just chat? <a href="#" data-wa style="color:var(--color-accent);font-weight:700;">Open WhatsApp directly</a></p>
    </div>
  </div>
</section>
"""
write("request-quote.html", page("Request a Quote | Lisbon Print House","Request a printing quote from Lisbon Print House via WhatsApp. Tell us what you need and we'll come back with accurate pricing.",0,"contact",body,"request-quote.html",schema=org_schema()))

print("Core pages built.")
