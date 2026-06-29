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

ITEMS = [
  ("Restaurants","Menu Redesign","Taberna do Bairro","https://images.unsplash.com/photo-1556742205-e10c9486e506?w=700&q=80"),
  ("Business Cards","Premium Soft-Touch Cards","Pereira Advogados","https://images.unsplash.com/photo-1561015314-6bd8c1e875ee?w=700&q=80"),
  ("Banners","Storefront Vinyl Banner","Loja Central","https://images.unsplash.com/photo-1762888244575-779a9515174b?w=700&q=80"),
  ("Retail","Window Graphics Install","Studio Beleza","https://images.unsplash.com/photo-1781617320919-1ac35d5f2443?w=700&q=80"),
  ("Packaging","Branded Takeaway Boxes","Café Lumiar","https://images.unsplash.com/photo-1656543802898-41c8c46683a7?w=700&q=80"),
  ("Events","Festival Poster Series","Lisboa Music Fest","https://images.unsplash.com/photo-1563050860-87d45eaaeabb?w=700&q=80"),
  ("Corporate","Stationery Suite","Nexus Consulting","https://images.unsplash.com/photo-1614036634955-ae5e90f9b9eb?w=700&q=80"),
  ("Menus","Drinks Menu & Coasters","Bar Alfama","https://images.unsplash.com/photo-1625173616412-7b403d49a41e?w=700&q=80"),
  ("Restaurants","Table Tent Cards","Marisqueira do Porto","https://images.unsplash.com/photo-1544025162-d76694265947?w=700&q=80"),
  ("Retail","Promotional Flyers","Moda Lisboa Store","https://images.unsplash.com/photo-1695634621375-0b66a9d5d1bc?w=700&q=80"),
  ("Business Cards","Real Estate Card Set","Casa Nova Imóveis","https://images.unsplash.com/photo-1535381273077-21e00c27b1b7?w=700&q=80"),
  ("Events","Roll-up Banners for Expo","TechLisbon Summit","https://images.unsplash.com/photo-1617355405361-29f0f0a3d737?w=700&q=80"),
  ("Corporate","Branded Brochure","Atlas Architecture","https://images.unsplash.com/photo-1631270314738-e6f6827f8d9f?w=700&q=80"),
  ("Packaging","Vinyl Sticker Labels","Mel Doce Bakery","https://images.unsplash.com/photo-1625768376503-68d2495d78c5?w=700&q=80"),
  ("Banners","Gym Window Vinyl","FitZone Lisboa","https://images.unsplash.com/photo-1605513524006-063ed6ed31e7?w=700&q=80"),
]
CATS = ["All","Restaurants","Retail","Events","Corporate","Packaging","Menus","Banners","Business Cards"]
filters = "".join(f'<button class="filter-btn{" active" if c=="All" else ""}" data-filter="{"all" if c=="All" else c}">{c}</button>' for c in CATS)
items_html = "".join(f"""<div class="masonry-item fade-up" data-category="{cat}"><img src="{img}" alt="{title} — {client}" loading="lazy"><div class="overlay"><span>{title}</span><small>{client}</small></div></div>""" for cat, title, client, img in ITEMS)

body = page_hero(0,"Portfolio","Real Work for Real Lisbon Businesses","A look at recent projects across restaurants, retail, events, and corporate clients.", [("Home","index.html"),("Portfolio",None)]) + f"""
<section>
  <div class="container">
    <div class="filters">{filters}</div>
    <div class="masonry">{items_html}</div>
  </div>
</section>
"""
write("portfolio.html", page(
  "Portfolio | Lisbon Print House",
  "Browse real printing projects by Lisbon Print House: restaurant menus, business cards, banners, packaging and more.",
  0, "portfolio", body, "portfolio.html",
  schema=org_schema()+breadcrumb_schema([("Home","index.html"),("Portfolio","portfolio.html")])
))
print("Built portfolio.")
