# -*- coding: utf-8 -*-
from build import *

SERVICES = [
  ("Business Cards","business-card-printing.html","Premium matte, gloss, and textured finishes that make a first impression last.","https://images.unsplash.com/photo-1561015314-6bd8c1e875ee?w=600&q=80"),
  ("Flyers & Folded Flyers","flyer-printing.html","Eye-catching flyers for promotions, menus, and local marketing campaigns.","https://images.unsplash.com/photo-1695634621375-0b66a9d5d1bc?w=600&q=80"),
  ("Restaurant Menus","restaurant-menu-printing.html","Durable, beautifully designed menus that match your restaurant's identity.","https://images.unsplash.com/photo-1556742205-e10c9486e506?w=600&q=80"),
  ("PVC & Roll-up Banners","banner-printing.html","Big, bold signage for storefronts, events, and trade shows.","https://images.unsplash.com/photo-1762888244575-779a9515174b?w=600&q=80"),
  ("Stickers & Labels","sticker-printing.html","Custom-shaped vinyl stickers and labels for packaging and branding.","https://images.unsplash.com/photo-1625768376503-68d2495d78c5?w=600&q=80"),
  ("Window Graphics","window-graphics-printing.html","Vinyl window displays that turn storefronts into silent salespeople.","https://images.unsplash.com/photo-1781617320919-1ac35d5f2443?w=600&q=80"),
  ("Packaging & Boxes","packaging-printing.html","Branded packaging that protects your product and elevates your brand.","https://images.unsplash.com/photo-1656543802898-41c8c46683a7?w=600&q=80"),
  ("Booklets & Catalogues","booklet-printing.html","Multi-page booklets and catalogues, professionally bound and finished.","https://images.unsplash.com/photo-1614036634955-ae5e90f9b9eb?w=600&q=80"),
]

INDUSTRIES = [
  ("Restaurants & Cafés","https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=500&q=80"),
  ("Hotels","https://images.unsplash.com/photo-1551882547-ff40c63fe5fa?w=500&q=80"),
  ("Retail Stores","https://images.unsplash.com/photo-1441986300917-64674bd600d8?w=500&q=80"),
  ("Beauty Salons & Barbers","https://images.unsplash.com/photo-1521590832167-7bcbfaa6381f?w=500&q=80"),
  ("Real Estate","https://images.unsplash.com/photo-1560518883-ce09059eeffa?w=500&q=80"),
  ("Gyms & Fitness","https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=500&q=80"),
]

body = f"""
<section class="hero">
  <div class="container hero-grid">
    <div class="fade-up">
      <div class="hero-eyebrow"><span class="dot"></span> Trusted by 300+ Lisbon businesses</div>
      <h1>Professional Printing Services for Businesses in Lisbon</h1>
      <p class="lead">Premium quality printing, competitive prices, and dedicated customer support — all one WhatsApp message away.</p>
      <div class="hero-ctas">
        <a href="#" class="btn btn-primary" data-wa>{ICONS['wa']} Get a Quote on WhatsApp</a>
        <a href="portfolio.html" class="btn btn-outline">View Portfolio</a>
      </div>
      <div class="hero-stats">
        <div class="hero-stat"><strong data-counter="300">0</strong><span>Businesses Served</span></div>
        <div class="hero-stat"><strong data-counter="12000">0</strong><span>Orders Delivered</span></div>
        <div class="hero-stat"><strong data-counter="5">0</strong><span>Years in Business</span></div>
      </div>
    </div>
    <div class="hero-media fade-up">
      <img src="https://images.unsplash.com/photo-1758183961426-88d64eb5f787?w=900&q=80" alt="Premium printed materials for Lisbon businesses" loading="lazy">
      <div class="hero-badge">
        <div class="icon">{ICONS['shield']}</div>
        <div><strong>Quality Guaranteed</strong><span>Or we reprint, free</span></div>
      </div>
    </div>
  </div>
</section>

<div class="trust-bar">
  <div class="container trust-grid">
    <div class="trust-item">{ICONS['truck']} Portugal-Wide Delivery</div>
    <div class="trust-item">{ICONS['clock']} Reliable Lead Times</div>
    <div class="trust-item">{ICONS['shield']} Premium Materials</div>
    <div class="trust-item">{ICONS['star']} 4.9/5 Customer Rating</div>
  </div>
</div>

<section>
  <div class="container">
    <div class="section-head center">
      <div class="eyebrow">Why Lisbon Print House</div>
      <h2>Built for Businesses That Demand Quality</h2>
      <p>We combine premium print quality with a personal service that makes every order simple.</p>
    </div>
    <div class="grid grid-4">
      <div class="card icon-card fade-up"><div class="icon-wrap">{ICONS['shield']}</div><h3>Premium Quality</h3><p>Commercial-grade printing on professional equipment, checked before every delivery.</p></div>
      <div class="card icon-card fade-up"><div class="icon-wrap">{ICONS['wa']}</div><h3>WhatsApp Support</h3><p>Talk directly to a real person, get quotes and track your order with zero hassle.</p></div>
      <div class="card icon-card fade-up"><div class="icon-wrap">{ICONS['truck']}</div><h3>Portugal-Wide Delivery</h3><p>Based in Lisbon, delivering to businesses across the entire country.</p></div>
      <div class="card icon-card fade-up"><div class="icon-wrap">{ICONS['star']}</div><h3>Colour Guaranteed</h3><p>Every order is proofed for colour accuracy before printing — what you approve is what you get.</p></div>
    </div>
  </div>
</section>

<section class="bg-soft">
  <div class="container">
    <div class="section-head center">
      <div class="eyebrow">What We Print</div>
      <h2>Everything Your Business Needs to Print</h2>
      <p>From business cards to full restaurant branding — explore our most requested services.</p>
    </div>
    <div class="grid grid-4">
      {''.join(f'''<div class="service-card fade-up">
        <div class="thumb"><img src="{img}" alt="{name} printing in Lisbon" loading="lazy"></div>
        <div class="body"><h3>{name}</h3><p>{desc}</p><a href="services/{href}" class="link">Learn More {ICONS['arrow']}</a></div>
      </div>''' for name, href, desc, img in SERVICES)}
    </div>
    <div class="text-center" style="margin-top:40px;">
      <a href="services/index.html" class="btn btn-dark">View All Services</a>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head center">
      <div class="eyebrow">Industries We Serve</div>
      <h2>Trusted by Lisbon's Local Businesses</h2>
      <p>We understand what each industry needs because we've printed for them all.</p>
    </div>
    <div class="grid grid-3">
      {''.join(f'''<a href="industries.html" class="industry-card fade-up"><img src="{img}" alt="{name} printing services" loading="lazy"><span>{name}</span></a>''' for name, img in INDUSTRIES)}
    </div>
  </div>
</section>

<section class="bg-soft">
  <div class="container">
    <div class="section-head center">
      <div class="eyebrow">Featured Work</div>
      <h2>Recent Projects We're Proud Of</h2>
    </div>
    <div class="grid grid-3">
      <div class="masonry-item fade-up"><img src="https://images.unsplash.com/photo-1556742205-e10c9486e506?w=600&q=80" alt="Restaurant menu printing project" loading="lazy"><div class="overlay"><span>Menu Redesign</span><small>Local Restaurant, Lisbon</small></div></div>
      <div class="masonry-item fade-up"><img src="https://images.unsplash.com/photo-1561015314-6bd8c1e875ee?w=600&q=80" alt="Business card printing project" loading="lazy"><div class="overlay"><span>Business Cards</span><small>Real Estate Agency</small></div></div>
      <div class="masonry-item fade-up"><img src="https://images.unsplash.com/photo-1762888244575-779a9515174b?w=600&q=80" alt="Storefront banner printing project" loading="lazy"><div class="overlay"><span>Storefront Banner</span><small>Retail Boutique</small></div></div>
    </div>
    <div class="text-center" style="margin-top:40px;"><a href="portfolio.html" class="btn btn-outline">View Full Portfolio</a></div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head center">
      <div class="eyebrow">Testimonials</div>
      <h2>What Our Clients Say</h2>
    </div>
    <div class="grid grid-3">
      <div class="testimonial-card fade-up"><div class="stars">★★★★★</div><p class="quote">"Ordered new menus on a Tuesday, had them in hand by Thursday. Quality is better than what we used to pay double for."</p><div class="testimonial-author"><img src="https://i.pravatar.cc/100?img=12" alt="Restaurant owner"><div><strong>Miguel Santos</strong><span>Owner, Taberna do Bairro</span></div></div></div>
      <div class="testimonial-card fade-up"><div class="stars">★★★★★</div><p class="quote">"WhatsApp ordering is genuinely the easiest way I've ever bought printing. No forms, no waiting on hold."</p><div class="testimonial-author"><img src="https://i.pravatar.cc/100?img=45" alt="Salon owner"><div><strong>Ana Ferreira</strong><span>Owner, Studio Beleza</span></div></div></div>
      <div class="testimonial-card fade-up"><div class="stars">★★★★★</div><p class="quote">"Our storefront vinyl looks incredible and installation was included. Highly recommend for any retail business."</p><div class="testimonial-author"><img src="https://i.pravatar.cc/100?img=33" alt="Retail owner"><div><strong>João Pereira</strong><span>Manager, Loja Central</span></div></div></div>
    </div>
  </div>
</section>

<section class="bg-soft">
  <div class="container">
    <div class="section-head center">
      <div class="eyebrow">How It Works</div>
      <h2>From Message to Delivery in 4 Simple Steps</h2>
    </div>
    <div class="process-steps">
      <div class="process-step fade-up"><div class="num">01</div><h3>Message Us on WhatsApp</h3><p>Tell us what you need — or just send a photo or rough idea.</p></div>
      <div class="process-step fade-up"><div class="num">02</div><h3>Get a Quote</h3><p>We reply with pricing, sizes, and lead time for your order.</p></div>
      <div class="process-step fade-up"><div class="num">03</div><h3>Approve & We Print</h3><p>Confirm your design and we get your order into production.</p></div>
      <div class="process-step fade-up"><div class="num">04</div><h3>Pickup or Delivery</h3><p>Collect in Lisbon or get it delivered anywhere in Portugal.</p></div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head center">
      <div class="eyebrow">FAQ</div>
      <h2>Frequently Asked Questions</h2>
    </div>
    <div class="faq-list">
      <details class="faq-item fade-up" open><summary>How long does printing take?</summary><p>Lead times vary by product and quantity. Message us on WhatsApp with your order details and we'll confirm the exact timeline before you commit.</p></details>
      <details class="faq-item fade-up"><summary>Do you deliver outside Lisbon?</summary><p>Yes — we deliver to businesses across all of Portugal via courier partners.</p></details>
      <details class="faq-item fade-up"><summary>Can you design my artwork for me?</summary><p>Absolutely. Our graphic design team can create your artwork from scratch or refine files you already have.</p></details>
      <details class="faq-item fade-up"><summary>What's the minimum order quantity?</summary><p>It depends on the product — many items like business cards and stickers have low minimums suited to small businesses.</p></details>
      <details class="faq-item fade-up"><summary>How do I get a price?</summary><p>Just send us a WhatsApp message with what you need — product, quantity, and any finish preferences. We'll come back with a full quote.</p></details>
    </div>
  </div>
</section>
"""

schema = org_schema() + faq_schema([
  ("How long does printing take?","Lead times vary by product and quantity. Contact us on WhatsApp for the exact timeline for your order."),
  ("Do you deliver outside Lisbon?","Yes, we deliver to businesses across all of Portugal."),
  ("Can you design my artwork for me?","Yes, our graphic design team can create or refine your artwork."),
])

html = page(
  title="Lisbon Print House | Professional Printing Services in Lisbon, Portugal",
  description="Premium printing for businesses in Lisbon and across Portugal. Business cards, flyers, banners, menus, packaging & more. Get a fast quote on WhatsApp.",
  depth=0, active="index", body=body, canonical_path="index.html", schema=schema
)
write("index.html", html)
