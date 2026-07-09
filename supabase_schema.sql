-- Lisbon Print House — Supabase Schema
-- Paste this entire file into your Supabase SQL Editor and click Run.

-- ────────────────────────────────────────────────────────────────────────────
-- PRODUCTS
-- ────────────────────────────────────────────────────────────────────────────
create table if not exists products (
  id            uuid primary key default gen_random_uuid(),
  created_at    timestamptz default now(),
  updated_at    timestamptz default now(),
  name          text not null,
  slug          text not null unique,
  category      text not null,
  tagline       text,
  description   text,
  price_from    numeric(10,2),      -- starting price e.g. 12.50
  price_unit    text default '/ 100 units',
  image_url     text,
  stripe_link   text,               -- Stripe Payment Link URL
  features      jsonb default '[]', -- ["Fast turnaround","Matte or gloss"]
  sizes         jsonb default '[]', -- ["A4","A5","Custom"]
  active        boolean default true,
  sort_order    integer default 0
);

-- ────────────────────────────────────────────────────────────────────────────
-- ORDERS  (created when Stripe webhook fires, or manually)
-- ────────────────────────────────────────────────────────────────────────────
create table if not exists orders (
  id                uuid primary key default gen_random_uuid(),
  created_at        timestamptz default now(),
  customer_name     text,
  customer_email    text,
  customer_phone    text,
  product_id        uuid references products(id),
  quantity          integer,
  notes             text,
  total_amount      numeric(10,2),
  status            text default 'pending',  -- pending | confirmed | printing | delivered | cancelled
  stripe_session_id text,
  stripe_payment_id text
);

-- ────────────────────────────────────────────────────────────────────────────
-- CONTACTS  (from the WhatsApp quote form, optional)
-- ────────────────────────────────────────────────────────────────────────────
create table if not exists contacts (
  id           uuid primary key default gen_random_uuid(),
  created_at   timestamptz default now(),
  name         text,
  email        text,
  phone        text,
  service      text,
  message      text
);

-- ────────────────────────────────────────────────────────────────────────────
-- ROW LEVEL SECURITY
-- Public can SELECT active products. Admin (authenticated) has full access.
-- ────────────────────────────────────────────────────────────────────────────
alter table products enable row level security;
alter table orders   enable row level security;
alter table contacts enable row level security;

-- Products: anyone can read active products
create policy "Public read active products"
  on products for select
  using (active = true);

-- Authenticated users (admin) can do everything
create policy "Admin full access products"
  on products for all
  using (auth.role() = 'authenticated');

create policy "Admin full access orders"
  on orders for all
  using (auth.role() = 'authenticated');

create policy "Admin full access contacts"
  on contacts for all
  using (auth.role() = 'authenticated');

-- Anyone can insert a contact (quote form)
create policy "Public insert contacts"
  on contacts for insert
  with check (true);

-- ────────────────────────────────────────────────────────────────────────────
-- SEED — pre-load the 8 core services
-- ────────────────────────────────────────────────────────────────────────────
insert into products (name, slug, category, tagline, description, price_from, price_unit, image_url, features, sizes, sort_order) values
(
  'Business Cards', 'business-cards', 'Cards',
  'Premium matte, gloss, and soft-touch finishes',
  'Make a lasting first impression with professional business cards printed on 350gsm stock. Choose from matte, gloss, soft-touch lamination, or uncoated finishes.',
  12.50, '/ 100 cards',
  'https://images.unsplash.com/photo-1561015314-6bd8c1e875ee?w=600&q=80',
  '["350gsm card stock","Double-sided printing","Matte, gloss or soft-touch lamination","Rounded corners available","48h standard turnaround"]',
  '["85×55mm (Standard)","90×50mm","Custom sizes"]',
  1
),
(
  'Flyers & Folded Flyers', 'flyers', 'Flyers',
  'Eye-catching flyers for promotions and local marketing',
  'High-impact flyers printed on 135gsm or 170gsm coated stock. Available in A4, A5, A6, and DL sizes, single or double-sided.',
  8.00, '/ 100 units',
  'https://images.unsplash.com/photo-1695634621375-0b66a9d5d1bc?w=600&q=80',
  '["135gsm or 170gsm coated stock","Single or double-sided","A4, A5, A6, DL sizes","Folded options available","Fast 24h turnaround"]',
  '["A4","A5","A6","DL","1/3 A4"]',
  2
),
(
  'Restaurant Menus', 'restaurant-menus', 'Menus',
  'Durable menus that match your restaurant''s identity',
  'Professionally printed menus on 300gsm laminated stock. Resistant to spills and daily handling. Available as single-page, folded, or multi-page booklets.',
  45.00, '/ 50 menus',
  'https://images.unsplash.com/photo-1556742205-e10c9486e506?w=600&q=80',
  '["300gsm laminated stock","Wipe-clean surface","Single-page, folded, or booklet","Full colour printing","Custom sizes available"]',
  '["A4","A5","DL","Custom"]',
  3
),
(
  'PVC & Roll-up Banners', 'banners', 'Banners',
  'Bold signage for storefronts, events, and trade shows',
  'Outdoor-grade PVC banners with reinforced hems and eyelets, or portable roll-up banners for indoor events. Custom sizes available.',
  35.00, '/ banner',
  'https://images.unsplash.com/photo-1762888244575-779a9515174b?w=600&q=80',
  '["Weatherproof PVC material","Reinforced hems & eyelets","Roll-up stands available","Full bleed printing","Custom sizes"]',
  '["1m×1m","2m×1m","85×200cm (Roll-up)","Custom"]',
  4
),
(
  'Stickers & Labels', 'stickers', 'Stickers',
  'Custom-shaped vinyl stickers for packaging and branding',
  'Die-cut vinyl stickers and custom labels in any shape or size. Waterproof, scratch-resistant, and perfect for product packaging or brand promotion.',
  18.00, '/ 100 units',
  'https://images.unsplash.com/photo-1625768376503-68d2495d78c5?w=600&q=80',
  '["Waterproof vinyl","Die-cut to any shape","Matte or gloss finish","Indoor & outdoor grade","Low minimum quantity"]',
  '["Round","Square","Custom shape","Label rolls"]',
  5
),
(
  'Window Graphics', 'window-graphics', 'Signage',
  'Vinyl window displays that turn storefronts into silent salespeople',
  'Frosted, opaque, or perforated vinyl window graphics professionally installed on your storefront. Ideal for promotions, branding, and privacy screening.',
  120.00, '/ m²',
  'https://images.unsplash.com/photo-1781617320919-1ac35d5f2443?w=600&q=80',
  '["Frosted, opaque or perforated vinyl","Professional installation available","Repositionable options","UV-resistant inks","Full-colour printing"]',
  '["Custom — priced per m²"]',
  6
),
(
  'Packaging & Boxes', 'packaging', 'Packaging',
  'Branded packaging that protects your product and elevates your brand',
  'Custom-printed boxes, bags, and packaging in any size. Perfect for retail, e-commerce, food packaging, and gift boxes.',
  95.00, '/ 50 units',
  'https://images.unsplash.com/photo-1656543802898-41c8c46683a7?w=600&q=80',
  '["Custom sizes & shapes","Full-colour printing","Matte or gloss lamination","Eco-friendly options available","Low minimum runs"]',
  '["Custom — specify dimensions"]',
  7
),
(
  'Booklets & Catalogues', 'booklets', 'Booklets',
  'Multi-page booklets and catalogues, professionally bound and finished',
  'Saddle-stitched or perfect-bound booklets from 8 to 100+ pages. Ideal for product catalogues, lookbooks, training manuals, and annual reports.',
  85.00, '/ 25 booklets',
  'https://images.unsplash.com/photo-1614036634955-ae5e90f9b9eb?w=600&q=80',
  '["Saddle-stitch or perfect binding","A4 or A5 sizes","150gsm inner pages","300gsm laminated cover","Custom page counts"]',
  '["A4","A5","Custom"]',
  8
);
