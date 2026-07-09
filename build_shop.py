# -*- coding: utf-8 -*-
from build import *

body = """
<section class="page-hero">
  <div class="container">
    <div class="breadcrumbs"><a href="index.html">Home</a> &rsaquo; Shop</div>
    <div class="eyebrow" style="justify-content:center;display:flex;">Order Online</div>
    <h1>Order Printing Online</h1>
    <p>Browse our services, choose your product, and pay securely with Stripe — or message us on WhatsApp for a custom quote.</p>
  </div>
</section>

<section>
  <div class="container">
    <div id="shop-filters" class="filters" style="margin-bottom:40px;"></div>
    <div id="shop-grid" class="grid grid-4">
      <!-- injected by shop.js -->
      <div class="loading-state" style="grid-column:1/-1;text-align:center;padding:80px 0;color:var(--color-text-muted);">
        <p>Loading products…</p>
      </div>
    </div>
  </div>
</section>

<!-- Product detail modal -->
<div id="product-modal" class="modal-overlay" role="dialog" aria-modal="true" hidden>
  <div class="modal-box">
    <button class="modal-close" id="modal-close" aria-label="Close">&times;</button>
    <div class="modal-inner">
      <div class="modal-img-wrap">
        <img id="modal-img" src="" alt="">
      </div>
      <div class="modal-content">
        <div class="eyebrow" id="modal-cat"></div>
        <h2 id="modal-name"></h2>
        <p id="modal-tagline" style="color:var(--color-text-muted);margin-top:4px;"></p>
        <p id="modal-desc" style="margin-top:16px;"></p>
        <div id="modal-features" class="modal-features"></div>
        <div id="modal-sizes" class="modal-sizes"></div>
        <div class="modal-price">
          <span class="price-from">From</span>
          <strong id="modal-price"></strong>
          <span id="modal-unit" style="color:var(--color-text-muted);font-size:0.9rem;"></span>
        </div>
        <div class="modal-ctas">
          <a id="modal-stripe-btn" href="#" class="btn btn-primary" target="_blank" rel="noopener" hidden>
            Pay &amp; Order Online
          </a>
          <a id="modal-wa-btn" href="#" class="btn btn-outline" data-wa>
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2a10 10 0 00-8.6 15.1L2 22l5.1-1.3A10 10 0 1012 2zm5.7 14.2c-.3.7-1.4 1.3-2 1.4-.5.1-1.2.2-3.4-.7-2.9-1.2-4.7-4.1-4.9-4.3-.1-.2-1.2-1.6-1.2-3 0-1.4.7-2.1 1-2.4.3-.3.6-.4.8-.4h.6c.2 0 .5 0 .7.5.3.7.9 2.2 1 2.4.1.2.1.4 0 .6-.4.8-.8 1-1 1.2-.2.2-.4.4-.2.8.3.6 1.1 1.6 2.3 2.6 1.5 1.3 2.3 1.5 2.7 1.6.3.1.6.1.8-.1.3-.3.7-.9 1.1-1.3.3-.3.5-.3.8-.2l2 1c.3.1.5.2.6.4.1.2.1 1-.2 1.7z"/></svg>
            Request Custom Quote
          </a>
        </div>
      </div>
    </div>
  </div>
</div>
"""

extra_head = """
<link rel="stylesheet" href="css/shop.css">
<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2/dist/umd/supabase.js"></script>
<script src="js/supabase-config.js"></script>
"""

write("shop.html", page(
  "Order Printing Online | Lisbon Print House",
  "Order business cards, flyers, menus, banners and more online. Secure payment via Stripe, fast delivery across Portugal.",
  0, "shop", body, "shop.html",
  schema=org_schema()+breadcrumb_schema([("Home","index.html"),("Shop","shop.html")]),
  extra_head=extra_head
))

# Inject shop.js reference at end — done separately so footer() still injects main.js first
print("Built shop.html")
