# -*- coding: utf-8 -*-
"""
Static site generator for Lisbon Print House.
Run: python build.py
Generates all HTML pages from templates below. Edit data dicts to update content.
"""
import os, re

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = "https://lisbonprinthouse.com"
BIZ = "Lisbon Print House"
PHONE_DISPLAY = "+351 900 000 000"
EMAIL = "info@lisbonprinthouse.com"
HOURS = "Mon–Fri 9:00–18:00, Sat 10:00–14:00"

ICONS = {
  "check": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M5 13l4 4L19 7"/></svg>',
  "shield": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2l8 4v6c0 5-3.5 8.5-8 10-4.5-1.5-8-5-8-10V6l8-4z"/></svg>',
  "truck": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 7h11v8H3zM14 11h4l3 3v1h-7zM6 19a2 2 0 100-4 2 2 0 000 4zM17 19a2 2 0 100-4 2 2 0 000 4z"/></svg>',
  "star": '<svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3.1 6.3 6.9 1-5 4.9 1.2 6.8L12 17.8 5.8 21l1.2-6.8-5-4.9 6.9-1z"/></svg>',
  "clock": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>',
  "phone": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.9v3a2 2 0 01-2.2 2 19.8 19.8 0 01-8.6-3 19.5 19.5 0 01-6-6 19.8 19.8 0 01-3-8.7A2 2 0 014.1 2h3a2 2 0 012 1.7c.1.9.3 1.8.6 2.7a2 2 0 01-.5 2.1L8 9.7a16 16 0 006 6l1.2-1.2a2 2 0 012.1-.5c.9.3 1.8.5 2.7.6a2 2 0 011.7 2z"/></svg>',
  "mail": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="M22 6l-10 7L2 6"/></svg>',
  "pin": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 6-9 12-9 12s-9-6-9-12a9 9 0 1118 0z"/><circle cx="12" cy="10" r="3"/></svg>',
  "wa": '<svg width="28" height="28" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2a10 10 0 00-8.6 15.1L2 22l5.1-1.3A10 10 0 1012 2zm5.7 14.2c-.3.7-1.4 1.3-2 1.4-.5.1-1.2.2-3.4-.7-2.9-1.2-4.7-4.1-4.9-4.3-.1-.2-1.2-1.6-1.2-3 0-1.4.7-2.1 1-2.4.3-.3.6-.4.8-.4h.6c.2 0 .5 0 .7.5.3.7.9 2.2 1 2.4.1.2.1.4 0 .6-.4.8-.8 1-1 1.2-.2.2-.4.4-.2.8.3.6 1.1 1.6 2.3 2.6 1.5 1.3 2.3 1.5 2.7 1.6.3.1.6.1.8-.1.3-.3.7-.9 1.1-1.3.3-.3.5-.3.8-.2l2 1c.3.1.5.2.6.4.1.2.1 1-.2 1.7z"/></svg>',
  "arrow": '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M13 5l7 7-7 7"/></svg>',
  "clip": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 11l3 3L22 4M21 12v7a2 2 0 01-2 2H5a2 2 0 01-2-2V5a2 2 0 012-2h11"/></svg>',
}

NAV = [
  ("Home","index.html"), ("About","about.html"), ("Services","services/index.html"),
  ("Portfolio","portfolio.html"), ("Pricing","pricing.html"), ("Industries","industries.html"),
  ("FAQ","faq.html"), ("Blog","blog/index.html"), ("Contact","contact.html"),
]

def rel(depth, path):
  return ("../"*depth) + path

def header(depth=0, active=""):
  items = ""
  for label, href in NAV:
    cls = " active" if href.split("/")[-1].replace(".html","")==active else ""
    items += f'<li><a href="{rel(depth,href)}" class="{cls.strip()}">{label}</a></li>'
  return f"""
<header class="site-header">
  <nav class="nav">
    <a href="{rel(depth,'index.html')}" class="nav-logo">{BIZ.split(' ')[0]} <span>{ ' '.join(BIZ.split(' ')[1:]) }</span></a>
    <ul class="nav-links">{items}</ul>
    <div class="nav-cta">
      <a href="{rel(depth,'request-quote.html')}" class="btn btn-primary btn-sm" data-wa>{ICONS['wa']}<span class="btn-sm-label">Get a Quote on WhatsApp</span></a>
      <button class="nav-toggle" aria-label="Menu"><span></span><span></span><span></span></button>
    </div>
  </nav>
</header>
"""

def footer(depth=0):
  return f"""
<a href="#" class="wa-float" data-wa aria-label="Chat on WhatsApp">{ICONS['wa']}</a>
<section class="container" style="padding:0 24px 80px;">
  <div class="cta-band fade-up">
    <h2>Ready to Print? Let's Talk on WhatsApp.</h2>
    <p>Send us your idea, files, or just a few details — we'll reply fast with pricing and next steps. No forms, no hassle.</p>
    <div class="ctas">
      <a href="#" class="btn btn-primary" data-wa>{ICONS['wa']} Request a Quote on WhatsApp</a>
      <a href="{rel(depth,'portfolio.html')}" class="btn btn-outline-light">View Portfolio</a>
    </div>
  </div>
</section>
<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <a href="{rel(depth,'index.html')}" class="nav-logo">{BIZ.split(' ')[0]} <span>{ ' '.join(BIZ.split(' ')[1:]) }</span></a>
        <p>Premium printing for businesses in Lisbon and across Portugal. Fast turnaround, reliable quality, and a quote that's one WhatsApp message away.</p>
        <div class="footer-social">
          <a href="#" aria-label="Instagram">IG</a>
          <a href="#" aria-label="Facebook">FB</a>
          <a href="#" aria-label="LinkedIn">IN</a>
        </div>
      </div>
      <div class="footer-col">
        <h4>Company</h4>
        <ul>
          <li><a href="{rel(depth,'about.html')}">About Us</a></li>
          <li><a href="{rel(depth,'portfolio.html')}">Portfolio</a></li>
          <li><a href="{rel(depth,'industries.html')}">Industries</a></li>
          <li><a href="{rel(depth,'blog/index.html')}">Blog</a></li>
          <li><a href="{rel(depth,'contact.html')}">Contact</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Services</h4>
        <ul>
          <li><a href="{rel(depth,'services/business-card-printing.html')}">Business Cards</a></li>
          <li><a href="{rel(depth,'services/flyer-printing.html')}">Flyers</a></li>
          <li><a href="{rel(depth,'services/restaurant-menu-printing.html')}">Restaurant Menus</a></li>
          <li><a href="{rel(depth,'services/banner-printing.html')}">PVC Banners</a></li>
          <li><a href="{rel(depth,'services/index.html')}">All Services</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Get In Touch</h4>
        <ul>
          <li><a href="#" data-wa>WhatsApp: {PHONE_DISPLAY}</a></li>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li><a href="#">Lisbon, Portugal</a></li>
          <li>{HOURS}</li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; 2026 {BIZ}. All rights reserved.</span>
      <span><a href="{rel(depth,'contact.html')}">Privacy Policy</a> &middot; <a href="{rel(depth,'contact.html')}">Terms of Service</a></span>
    </div>
  </div>
</footer>
<script src="{rel(depth,'js/main.js')}"></script>
"""

def page(title, description, depth, active, body, canonical_path, og_image="images/og-default.jpg", schema="", extra_head=""):
  canonical = f"{SITE}/{canonical_path}"
  css = rel(depth, "css/style.css")
  fonts = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">'
  return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
{fonts}
<link rel="stylesheet" href="{css}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="website">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE}/{og_image}">
<meta property="og:site_name" content="{BIZ}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{description}">
<meta name="twitter:image" content="{SITE}/{og_image}">
{extra_head}
{schema}
</head>
<body>
{header(depth, active)}
{body}
{footer(depth)}
</body>
</html>"""

def org_schema():
  return f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "{BIZ}",
  "image": "{SITE}/images/og-default.jpg",
  "url": "{SITE}",
  "telephone": "{PHONE_DISPLAY}",
  "email": "{EMAIL}",
  "address": {{ "@type": "PostalAddress", "addressLocality": "Lisbon", "addressCountry": "PT" }},
  "openingHours": "Mo-Fr 09:00-18:00, Sa 10:00-14:00",
  "priceRange": "€€",
  "areaServed": "Portugal"
}}
</script>"""

def breadcrumb_schema(items):
  els = []
  for i, (name, url) in enumerate(items, 1):
    els.append(f'{{"@type":"ListItem","position":{i},"name":"{name}","item":"{SITE}/{url}"}}')
  return f"""<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{",".join(els)}]}}
</script>"""

def faq_schema(items):
  qs = []
  for q, a in items:
    qs.append(f'{{"@type":"Question","name":"{q}","acceptedAnswer":{{"@type":"Answer","text":"{a}"}}}}')
  return f"""<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{",".join(qs)}]}}
</script>"""

def write(path, content):
  full = os.path.join(ROOT, path)
  os.makedirs(os.path.dirname(full), exist_ok=True)
  with open(full, "w", encoding="utf-8") as f:
    f.write(content)
  print("wrote", path)

if __name__ == "__main__":
  print("Template engine loaded. Import this in other build_*.py scripts.")
