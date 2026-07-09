// ─── Shop Page — fetches products from Supabase ───────────────────────────
(async function () {
  const { createClient } = supabase;
  const db = createClient(SUPABASE_URL, SUPABASE_ANON_KEY);

  const grid    = document.getElementById("shop-grid");
  const filters = document.getElementById("shop-filters");
  const modal   = document.getElementById("product-modal");
  const closeBtn = document.getElementById("modal-close");

  let allProducts = [];
  let activeFilter = "All";

  // ── Fetch ──────────────────────────────────────────────────────────────────
  const { data, error } = await db
    .from("products")
    .select("*")
    .eq("active", true)
    .order("sort_order");

  if (error || !data?.length) {
    grid.innerHTML = `<div style="grid-column:1/-1;text-align:center;padding:80px 0;color:var(--color-text-muted);">
      <p>Unable to load products. Please try again or <a href="#" data-wa>contact us on WhatsApp</a>.</p></div>`;
    return;
  }

  allProducts = data;

  // ── Build filter buttons ──────────────────────────────────────────────────
  const cats = ["All", ...new Set(data.map(p => p.category))];
  filters.innerHTML = cats.map(c =>
    `<button class="filter-btn${c === "All" ? " active" : ""}" data-cat="${c}">${c}</button>`
  ).join("");

  filters.querySelectorAll(".filter-btn").forEach(btn => {
    btn.addEventListener("click", () => {
      activeFilter = btn.dataset.cat;
      filters.querySelectorAll(".filter-btn").forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      renderGrid();
    });
  });

  // ── Render product cards ──────────────────────────────────────────────────
  function formatPrice(p) {
    if (!p.price_from) return "";
    return `€${parseFloat(p.price_from).toFixed(2)}`;
  }

  function renderGrid() {
    const visible = activeFilter === "All"
      ? allProducts
      : allProducts.filter(p => p.category === activeFilter);

    grid.innerHTML = visible.map(p => `
      <div class="product-card fade-up" data-id="${p.id}">
        <div class="thumb">
          <img src="${p.image_url || ""}" alt="${p.name}" loading="lazy">
        </div>
        <div class="body">
          <div class="cat-tag">${p.category}</div>
          <h3>${p.name}</h3>
          <p class="tagline">${p.tagline || ""}</p>
          ${p.price_from ? `<div class="price-row"><span class="price">from ${formatPrice(p)}</span><span class="price-unit">${p.price_unit || ""}</span></div>` : ""}
          <div class="card-actions">
            <button class="btn btn-primary open-modal" data-id="${p.id}">View Details</button>
          </div>
        </div>
      </div>
    `).join("");

    // Re-trigger fade-up for newly injected elements
    grid.querySelectorAll(".fade-up").forEach(el => {
      const obs = new IntersectionObserver(entries => {
        entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add("in-view"); obs.unobserve(e.target); }});
      }, { threshold: 0.1 });
      obs.observe(el);
    });

    grid.querySelectorAll(".open-modal").forEach(btn => {
      btn.addEventListener("click", e => {
        e.stopPropagation();
        openModal(btn.dataset.id);
      });
    });
    grid.querySelectorAll(".product-card").forEach(card => {
      card.addEventListener("click", () => openModal(card.dataset.id));
    });

    // Re-wire WhatsApp links
    if (window.LPH) {
      document.querySelectorAll("[data-wa]").forEach(el => {
        const msg = el.getAttribute("data-wa-message") || LPH.WHATSAPP_DEFAULT_MESSAGE;
        el.href = `https://wa.me/${LPH.WHATSAPP_NUMBER}?text=${encodeURIComponent(msg)}`;
      });
    }
  }

  renderGrid();

  // ── Modal ─────────────────────────────────────────────────────────────────
  const CHECK_SVG = `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M5 13l4 4L19 7"/></svg>`;

  function openModal(id) {
    const p = allProducts.find(x => x.id === id);
    if (!p) return;

    document.getElementById("modal-img").src = p.image_url || "";
    document.getElementById("modal-img").alt = p.name;
    document.getElementById("modal-cat").textContent = p.category;
    document.getElementById("modal-name").textContent = p.name;
    document.getElementById("modal-tagline").textContent = p.tagline || "";
    document.getElementById("modal-desc").textContent = p.description || "";
    document.getElementById("modal-price").textContent = p.price_from ? formatPrice(p) : "Custom quote";
    document.getElementById("modal-unit").textContent = p.price_from ? (p.price_unit || "") : "";

    // Features
    const features = typeof p.features === "string" ? JSON.parse(p.features) : (p.features || []);
    document.getElementById("modal-features").innerHTML = features.map(f =>
      `<div class="modal-feature-item">${CHECK_SVG}<span>${f}</span></div>`
    ).join("");

    // Sizes
    const sizes = typeof p.sizes === "string" ? JSON.parse(p.sizes) : (p.sizes || []);
    document.getElementById("modal-sizes").innerHTML = sizes.map(s =>
      `<span class="size-tag">${s}</span>`
    ).join("");

    // Stripe button
    const stripeBtn = document.getElementById("modal-stripe-btn");
    if (p.stripe_link) {
      stripeBtn.href = p.stripe_link;
      stripeBtn.removeAttribute("hidden");
    } else {
      stripeBtn.setAttribute("hidden", "");
    }

    // WhatsApp button
    const waBtn = document.getElementById("modal-wa-btn");
    const msg = `Hi! I'd like a quote for ${p.name}.`;
    if (window.LPH) {
      waBtn.href = `https://wa.me/${LPH.WHATSAPP_NUMBER}?text=${encodeURIComponent(msg)}`;
    }

    modal.removeAttribute("hidden");
    document.body.style.overflow = "hidden";
  }

  function closeModal() {
    modal.setAttribute("hidden", "");
    document.body.style.overflow = "";
  }

  closeBtn.addEventListener("click", closeModal);
  modal.addEventListener("click", e => { if (e.target === modal) closeModal(); });
  document.addEventListener("keydown", e => { if (e.key === "Escape") closeModal(); });
})();
