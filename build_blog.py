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

POSTS = [
  dict(slug="how-to-design-business-cards", cat="Graphic Design", title="How to Design Business Cards That Actually Get Kept",
    desc="A practical guide to designing business cards that make a strong first impression and avoid the trash bin.",
    img="https://images.unsplash.com/photo-1561015314-6bd8c1e875ee?w=900&q=80",
    body=[
      ("Start With One Clear Message","A business card has about three seconds to communicate who you are and what you do. Resist the urge to cram in every detail — your name, role, business name, and one way to contact you should dominate the layout. Everything else is secondary."),
      ("Choose Paper Stock Like It's Part of the Design","The feel of a card in someone's hand is part of the impression. A 350gsm soft-touch finish communicates something different than a thin, glossy card. Match the stock to your brand: premium services often pair well with matte or soft-touch, while creative brands can experiment with textured or uncoated stock."),
      ("Leave Room to Breathe","Tight margins and overcrowded layouts read as cheap, regardless of how good your logo is. Generous white space signals confidence and makes your contact details easier to find at a glance."),
      ("Design for Both Sides","A double-sided card gives you space for a clean front (logo, name, role) and a detail-rich back (services, QR code, social handles) without cluttering either side."),
      ("Get a Physical Proof Before Printing in Bulk","Colors and fonts look different on screen than in hand. Always request a sample or digital proof before committing to a large print run — it's a five-minute step that prevents costly reprints."),
    ]),
  dict(slug="best-menu-materials-for-restaurants", cat="Restaurant Marketing", title="Best Menu Materials for Restaurants (And What to Avoid)",
    desc="Choosing the right paper and finish for restaurant menus that survive daily handling and still look premium.",
    img="https://images.unsplash.com/photo-1556742205-e10c9486e506?w=900&q=80",
    body=[
      ("Why Material Choice Matters More Than Design","A beautifully designed menu printed on thin, uncoated paper will look worn within a week. Restaurants handle menus dozens of times a day — spills, grease, and constant handling demand materials built for durability, not just looks."),
      ("Laminated Matte or Gloss Stock","Lamination is the single most important upgrade for restaurant menus. A laminated 300gsm matte or gloss finish resists spills, wipes clean, and holds up far longer than uncoated paper."),
      ("Synthetic Waterproof Stock for High-Traffic Venues","For bars, cafés, and busy restaurants, synthetic stock (a plastic-like paper) is nearly indestructible and ideal for menus that get heavy daily use."),
      ("Avoid Thin, Uncoated Paper","Standard office paper or thin uncoated stock might save money upfront, but it tears, stains, and needs replacing constantly — costing more over time than a one-time investment in durable materials."),
      ("Match Finish to Menu Type","Single-page menus benefit from lamination; multi-page menus are better served by booklet binding with a sturdy laminated cover and lighter inner pages to keep the booklet manageable."),
    ]),
  dict(slug="choosing-banner-sizes", cat="Printing Tips", title="Choosing the Right Banner Size for Your Storefront or Event",
    desc="A simple framework for picking banner dimensions that get noticed without overwhelming the space.",
    img="https://images.unsplash.com/photo-1762888244575-779a9515174b?w=900&q=80",
    body=[
      ("Measure the Space, Not Just the Message","Before choosing a size, measure where the banner will actually hang — a storefront facade, a fence line, an event backdrop. The available space should dictate the size, not the amount of text you want to include."),
      ("Readability Distance Matters","A banner read from a moving car needs much larger text and a simpler layout than one read by pedestrians standing a few meters away. As a rule of thumb, lettering height should be roughly 2.5cm for every 3 meters of intended reading distance."),
      ("Standard Sizes That Work for Most Businesses","1m x 1m banners work well for small entryways or temporary signage. 2m x 1m suits most storefront facades. For events or large exterior walls, 3m x 2m or custom sizes give maximum visibility."),
      ("Roll-Up Banners for Indoor Events","If you're exhibiting at a trade show or hosting an in-store promotion, a portable roll-up banner (85 x 200cm standard) offers professional presence without the installation needs of a PVC banner."),
      ("Don't Forget Material","Outdoor banners need weatherproof PVC with reinforced hems and eyelets; indoor banners can use lighter, more cost-effective materials since they won't face wind or rain."),
    ]),
  dict(slug="flyer-design-tips", cat="Printing Tips", title="Flyer Design Tips That Actually Drive Foot Traffic",
    desc="Practical design principles for flyers that get read, remembered, and acted on.",
    img="https://images.unsplash.com/photo-1695634621375-0b66a9d5d1bc?w=900&q=80",
    body=[
      ("Lead With the Offer, Not the Logo","Your business name matters, but the offer or message is what stops someone from tossing the flyer. Put the most compelling line — a discount, an event date, a clear benefit — in the largest text on the page."),
      ("One Call to Action, Stated Clearly","Flyers with multiple competing calls to action confuse readers. Pick one action — visit, call, scan a QR code, message on WhatsApp — and make it the most visible element after the headline."),
      ("Use Contrast to Guide the Eye","High contrast between background and text isn't just a stylistic choice — it's what makes a flyer scannable from a few feet away. Avoid light gray text on white backgrounds, no matter how elegant it looks on screen."),
      ("Print on Stock That Matches the Use Case","A flyer handed out at a festival needs to survive being folded into a pocket; a flyer left on a café counter can use lighter stock. Match paper weight and lamination to how the flyer will actually be used."),
      ("Track What Works","Add a unique QR code, discount code, or WhatsApp link to each flyer batch so you can see which design or distribution location actually drives responses."),
    ]),
  dict(slug="printed-marketing-still-works", cat="Marketing", title="Why Printed Marketing Still Works in a Digital World",
    desc="Digital ads are everywhere — which is exactly why physical print stands out more than ever for local businesses.",
    img="https://images.unsplash.com/photo-1758183961426-88d64eb5f787?w=900&q=80",
    body=[
      ("Attention Is the Scarcest Resource Online","The average person sees hundreds of digital ads a day and remembers almost none of them. A well-designed flyer, menu, or storefront banner doesn't compete in that noise — it exists in physical space, where attention is far less divided."),
      ("Print Builds Trust Digital Often Can't","A polished menu, business card, or storefront sign signals permanence and investment in a way a website alone doesn't always achieve. For local businesses especially, tangible materials reinforce credibility face-to-face."),
      ("Local Businesses Benefit Most","Restaurants, salons, retail stores, and other location-based businesses rely on foot traffic and in-person impressions — exactly where printed materials (signage, menus, window graphics) have the most influence."),
      ("It Pairs Well With Digital, Not Against It","QR codes on flyers, menus, and packaging connect physical materials directly to digital channels — reviews, social media, online ordering — making print and digital work together rather than competing."),
      ("The ROI Is Often Underestimated","Because print doesn't have real-time analytics dashboards like digital ads, businesses sometimes undervalue it. But consistent, well-placed printed marketing — done right — drives measurable walk-in traffic and repeat business for far less than what's spent chasing digital impressions."),
    ]),
]

cards = ""
for p in POSTS:
  cards += f"""<a href="blog/{p['slug']}.html" class="blog-card fade-up" style="display:block;">
    <div class="thumb"><img src="{p['img']}" alt="{p['title']}" loading="lazy"></div>
    <div class="body"><div class="meta">{p['cat']}</div><h3>{p['title']}</h3><p>{p['desc']}</p><span class="link" style="font-weight:700;color:var(--color-accent);">Read Article {ICONS['arrow']}</span></div>
  </a>"""

hub_body = f"""
<section class="page-hero">
  <div class="container">
    <div class="breadcrumbs"><a href="../index.html">Home</a> &rsaquo; Blog</div>
    <div class="eyebrow" style="justify-content:center;display:flex;">Blog</div>
    <h1>Printing & Marketing Insights for Lisbon Businesses</h1>
    <p>Practical tips on print design, restaurant branding, and marketing that drives real foot traffic.</p>
  </div>
</section>
<section><div class="container grid grid-3">{cards}</div></section>
"""
write("blog/index.html", page(
  "Blog | Lisbon Print House",
  "Printing tips, restaurant marketing advice, and graphic design guidance from Lisbon Print House.",
  1, "blog", hub_body, "blog/index.html",
  schema=org_schema()+breadcrumb_schema([("Home","index.html"),("Blog","blog/index.html")])
))

for p in POSTS:
  sections = "".join(f"<h2>{h}</h2><p>{t}</p>" for h, t in p["body"])
  body = f"""
<section class="page-hero">
  <div class="container">
    <div class="breadcrumbs"><a href="../index.html">Home</a> &rsaquo; <a href="index.html">Blog</a> &rsaquo; {p['title']}</div>
    <div class="eyebrow" style="justify-content:center;display:flex;">{p['cat']}</div>
    <h1>{p['title']}</h1>
  </div>
</section>
<section>
  <div class="container blog-post-body">
    <img src="{p['img']}" alt="{p['title']}" loading="lazy" style="border-radius:16px;margin-bottom:32px;width:100%;aspect-ratio:16/9;object-fit:cover;">
    {sections}
    <div class="cta-band" style="margin-top:48px;">
      <h2>Have a Print Project in Mind?</h2>
      <p>Get a fast, no-obligation quote — just send us a message on WhatsApp.</p>
      <div class="ctas"><a href="#" class="btn btn-primary" data-wa>{ICONS['wa']} Request a Quote on WhatsApp</a></div>
    </div>
  </div>
</section>
"""
  schema = org_schema() + breadcrumb_schema([("Home","index.html"),("Blog","blog/index.html"),(p["title"], f"blog/{p['slug']}.html")]) + f"""<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"BlogPosting","headline":"{p['title']}","description":"{p['desc']}","image":"{p['img']}","author":{{"@type":"Organization","name":"{BIZ}"}},"publisher":{{"@type":"Organization","name":"{BIZ}"}}}}
</script>"""
  write(f"blog/{p['slug']}.html", page(
    f"{p['title']} | {BIZ} Blog",
    p["desc"], 1, "blog", body, f"blog/{p['slug']}.html", schema=schema
  ))

print(f"Built blog hub + {len(POSTS)} posts.")
