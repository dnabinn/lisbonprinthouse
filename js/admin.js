// ─── Admin Panel ─────────────────────────────────────────────────────────────
const { createClient } = supabase;
const db = createClient(SUPABASE_URL, SUPABASE_ANON_KEY);

const loginScreen = document.getElementById("login-screen");
const adminApp    = document.getElementById("admin-app");
const adminMain   = document.getElementById("admin-main");

// ── Auth ──────────────────────────────────────────────────────────────────────
async function checkAuth() {
  const { data: { session } } = await db.auth.getSession();
  if (session) showApp();
  else showLogin();
}

function showLogin() {
  loginScreen.style.display = "flex";
  adminApp.style.display = "none";
}

function showApp() {
  loginScreen.style.display = "none";
  adminApp.style.display = "grid";
  renderPage("dashboard");
}

document.getElementById("login-form").addEventListener("submit", async e => {
  e.preventDefault();
  const email    = document.getElementById("email").value;
  const password = document.getElementById("password").value;
  const errEl    = document.getElementById("login-error");
  errEl.style.display = "none";

  const { error } = await db.auth.signInWithPassword({ email, password });
  if (error) {
    errEl.textContent = error.message;
    errEl.style.display = "block";
  } else {
    showApp();
  }
});

document.getElementById("logout-btn").addEventListener("click", async e => {
  e.preventDefault();
  await db.auth.signOut();
  showLogin();
});

// ── Nav ───────────────────────────────────────────────────────────────────────
document.querySelectorAll(".nav-link[data-page]").forEach(link => {
  link.addEventListener("click", e => {
    e.preventDefault();
    document.querySelectorAll(".nav-link").forEach(l => l.classList.remove("active"));
    link.classList.add("active");
    renderPage(link.dataset.page);
  });
});

// ── Pages ─────────────────────────────────────────────────────────────────────
async function renderPage(page) {
  adminMain.innerHTML = `<div style="text-align:center;padding:80px 0;color:var(--color-text-muted);">Loading…</div>`;
  if (page === "dashboard") await renderDashboard();
  if (page === "products")  await renderProducts();
  if (page === "orders")    await renderOrders();
  if (page === "contacts")  await renderContacts();
}

// ── Dashboard ─────────────────────────────────────────────────────────────────
async function renderDashboard() {
  const [{ count: productCount }, { count: orderCount }, { count: contactCount }, { data: recentOrders }] = await Promise.all([
    db.from("products").select("*", { count: "exact", head: true }),
    db.from("orders").select("*", { count: "exact", head: true }),
    db.from("contacts").select("*", { count: "exact", head: true }),
    db.from("orders").select("*, products(name)").order("created_at", { ascending: false }).limit(5),
  ]);

  adminMain.innerHTML = `
    <div class="admin-topbar">
      <h1>Dashboard</h1>
      <a href="../shop.html" target="_blank" class="btn btn-outline btn-sm">View Shop →</a>
    </div>
    <div class="admin-stats">
      <div class="stat-card"><div class="stat-label">Active Products</div><div class="stat-value">${productCount ?? 0}</div></div>
      <div class="stat-card"><div class="stat-label">Total Orders</div><div class="stat-value">${orderCount ?? 0}</div></div>
      <div class="stat-card"><div class="stat-label">Enquiries</div><div class="stat-value">${contactCount ?? 0}</div></div>
      <div class="stat-card"><div class="stat-label">Revenue</div><div class="stat-value">—</div></div>
    </div>
    <div class="admin-table-wrap">
      <div class="table-header">
        <h2>Recent Orders</h2>
        <a href="#" class="btn btn-outline btn-sm nav-link" data-page="orders">View All</a>
      </div>
      <table class="data-table">
        <thead><tr><th>Date</th><th>Customer</th><th>Product</th><th>Amount</th><th>Status</th></tr></thead>
        <tbody>
          ${(recentOrders || []).length === 0
            ? `<tr><td colspan="5" style="text-align:center;color:var(--color-text-muted);padding:32px;">No orders yet.</td></tr>`
            : (recentOrders || []).map(o => `
              <tr>
                <td>${new Date(o.created_at).toLocaleDateString("en-GB")}</td>
                <td>${o.customer_name || "—"}</td>
                <td>${o.products?.name || "—"}</td>
                <td>${o.total_amount ? "€" + parseFloat(o.total_amount).toFixed(2) : "—"}</td>
                <td><span class="badge badge-${o.status}">${o.status}</span></td>
              </tr>`).join("")
          }
        </tbody>
      </table>
    </div>
  `;

  // Wire dashboard "View All" nav link
  adminMain.querySelectorAll(".nav-link[data-page]").forEach(link => {
    link.addEventListener("click", e => {
      e.preventDefault();
      document.querySelectorAll(".nav-link").forEach(l => l.classList.remove("active"));
      document.querySelector(`.admin-nav .nav-link[data-page="${link.dataset.page}"]`)?.classList.add("active");
      renderPage(link.dataset.page);
    });
  });
}

// ── Products ──────────────────────────────────────────────────────────────────
async function renderProducts() {
  const { data: products } = await db.from("products").select("*").order("sort_order");

  adminMain.innerHTML = `
    <div class="admin-topbar">
      <h1>Products</h1>
      <button class="btn btn-primary btn-sm" id="add-product-btn">+ Add Product</button>
    </div>
    <div class="admin-table-wrap">
      <table class="data-table">
        <thead><tr><th>Name</th><th>Category</th><th>Price From</th><th>Stripe Link</th><th>Status</th><th>Actions</th></tr></thead>
        <tbody>
          ${(products || []).map(p => `
            <tr>
              <td><strong>${p.name}</strong></td>
              <td>${p.category}</td>
              <td>${p.price_from ? "€" + parseFloat(p.price_from).toFixed(2) + " " + (p.price_unit || "") : "—"}</td>
              <td>${p.stripe_link ? `<a href="${p.stripe_link}" target="_blank" style="color:var(--color-accent);font-size:0.82rem;">Stripe Link ↗</a>` : '<span style="color:var(--color-text-muted);">Not set</span>'}</td>
              <td><span class="badge badge-${p.active ? "active" : "inactive"}">${p.active ? "Active" : "Inactive"}</span></td>
              <td style="display:flex;gap:8px;">
                <button class="btn btn-outline btn-sm edit-product" data-id="${p.id}">Edit</button>
                <button class="btn btn-sm" style="border:1px solid #F8D7DA;color:#721C24;background:none;" data-id="${p.id}" class="del-product">Delete</button>
              </td>
            </tr>`).join("")}
        </tbody>
      </table>
    </div>
  `;

  document.getElementById("add-product-btn").addEventListener("click", () => openProductForm());
  adminMain.querySelectorAll(".edit-product").forEach(btn => {
    btn.addEventListener("click", () => {
      const p = products.find(x => x.id === btn.dataset.id);
      if (p) openProductForm(p);
    });
  });
  adminMain.querySelectorAll("[class='btn btn-sm']").forEach(btn => {
    btn.addEventListener("click", () => deleteProduct(btn.dataset.id));
  });
}

// ── Product form modal ────────────────────────────────────────────────────────
const productModal  = document.getElementById("product-form-modal");
const productForm   = document.getElementById("product-form");
const cancelFormBtn = document.getElementById("product-form-cancel");

cancelFormBtn.addEventListener("click", () => { productModal.setAttribute("hidden",""); });

function openProductForm(p = null) {
  document.getElementById("product-form-title").textContent = p ? "Edit Product" : "Add Product";
  document.getElementById("pf-id").value          = p?.id || "";
  document.getElementById("pf-name").value        = p?.name || "";
  document.getElementById("pf-slug").value        = p?.slug || "";
  document.getElementById("pf-category").value    = p?.category || "";
  document.getElementById("pf-tagline").value     = p?.tagline || "";
  document.getElementById("pf-description").value = p?.description || "";
  document.getElementById("pf-price").value       = p?.price_from || "";
  document.getElementById("pf-price-unit").value  = p?.price_unit || "";
  document.getElementById("pf-image").value       = p?.image_url || "";
  document.getElementById("pf-stripe").value      = p?.stripe_link || "";
  document.getElementById("pf-sort").value        = p?.sort_order ?? 0;
  document.getElementById("pf-active").value      = p?.active === false ? "false" : "true";

  const features = typeof p?.features === "string" ? JSON.parse(p.features) : (p?.features || []);
  const sizes    = typeof p?.sizes    === "string" ? JSON.parse(p.sizes)    : (p?.sizes    || []);
  document.getElementById("pf-features").value = features.join("\n");
  document.getElementById("pf-sizes").value    = sizes.join("\n");

  // Auto-slug from name
  document.getElementById("pf-name").addEventListener("input", function () {
    if (!p) {
      document.getElementById("pf-slug").value = this.value.toLowerCase()
        .replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "");
    }
  }, { once: true });

  productModal.removeAttribute("hidden");
}

productForm.addEventListener("submit", async e => {
  e.preventDefault();
  const id = document.getElementById("pf-id").value;

  const featuresRaw = document.getElementById("pf-features").value;
  const sizesRaw    = document.getElementById("pf-sizes").value;

  const payload = {
    name:        document.getElementById("pf-name").value,
    slug:        document.getElementById("pf-slug").value,
    category:    document.getElementById("pf-category").value,
    tagline:     document.getElementById("pf-tagline").value || null,
    description: document.getElementById("pf-description").value || null,
    price_from:  document.getElementById("pf-price").value || null,
    price_unit:  document.getElementById("pf-price-unit").value || null,
    image_url:   document.getElementById("pf-image").value || null,
    stripe_link: document.getElementById("pf-stripe").value || null,
    sort_order:  parseInt(document.getElementById("pf-sort").value) || 0,
    active:      document.getElementById("pf-active").value === "true",
    features:    featuresRaw ? featuresRaw.split("\n").map(s => s.trim()).filter(Boolean) : [],
    sizes:       sizesRaw    ? sizesRaw.split("\n").map(s => s.trim()).filter(Boolean)    : [],
    updated_at:  new Date().toISOString(),
  };

  const submitBtn = document.getElementById("product-form-submit");
  submitBtn.textContent = "Saving…";
  submitBtn.disabled = true;

  const { error } = id
    ? await db.from("products").update(payload).eq("id", id)
    : await db.from("products").insert(payload);

  submitBtn.textContent = "Save Product";
  submitBtn.disabled = false;

  if (error) { alert("Error: " + error.message); return; }

  productModal.setAttribute("hidden","");
  renderProducts();
});

async function deleteProduct(id) {
  if (!confirm("Delete this product? This cannot be undone.")) return;
  const { error } = await db.from("products").delete().eq("id", id);
  if (error) { alert("Error: " + error.message); return; }
  renderProducts();
}

// ── Orders ────────────────────────────────────────────────────────────────────
async function renderOrders() {
  const { data: orders } = await db.from("orders")
    .select("*, products(name)")
    .order("created_at", { ascending: false });

  const statuses = ["pending","confirmed","printing","delivered","cancelled"];

  adminMain.innerHTML = `
    <div class="admin-topbar"><h1>Orders</h1></div>
    <div class="admin-table-wrap">
      <table class="data-table">
        <thead><tr><th>Date</th><th>Customer</th><th>Product</th><th>Qty</th><th>Amount</th><th>Status</th><th>Notes</th></tr></thead>
        <tbody>
          ${(orders || []).length === 0
            ? `<tr><td colspan="7" style="text-align:center;color:var(--color-text-muted);padding:32px;">No orders yet. Orders from Stripe will appear here after setup.</td></tr>`
            : (orders || []).map(o => `
              <tr>
                <td>${new Date(o.created_at).toLocaleDateString("en-GB")}</td>
                <td>
                  <strong>${o.customer_name || "—"}</strong><br>
                  <span style="font-size:0.8rem;color:var(--color-text-muted);">${o.customer_email || ""}</span>
                </td>
                <td>${o.products?.name || "—"}</td>
                <td>${o.quantity || "—"}</td>
                <td>${o.total_amount ? "€" + parseFloat(o.total_amount).toFixed(2) : "—"}</td>
                <td>
                  <select class="status-select" data-id="${o.id}" style="font-size:0.82rem;padding:4px 8px;border:1px solid var(--color-border);border-radius:6px;font-family:var(--font-base);">
                    ${statuses.map(s => `<option value="${s}" ${o.status===s?"selected":""}>${s}</option>`).join("")}
                  </select>
                </td>
                <td style="max-width:180px;font-size:0.82rem;color:var(--color-text-muted);">${o.notes || "—"}</td>
              </tr>`).join("")}
        </tbody>
      </table>
    </div>
  `;

  adminMain.querySelectorAll(".status-select").forEach(sel => {
    sel.addEventListener("change", async () => {
      await db.from("orders").update({ status: sel.value }).eq("id", sel.dataset.id);
    });
  });
}

// ── Contacts / Enquiries ──────────────────────────────────────────────────────
async function renderContacts() {
  const { data: contacts } = await db.from("contacts")
    .select("*").order("created_at", { ascending: false });

  adminMain.innerHTML = `
    <div class="admin-topbar"><h1>Enquiries</h1></div>
    <div class="admin-table-wrap">
      <table class="data-table">
        <thead><tr><th>Date</th><th>Name</th><th>Email</th><th>Phone</th><th>Service</th><th>Message</th></tr></thead>
        <tbody>
          ${(contacts || []).length === 0
            ? `<tr><td colspan="6" style="text-align:center;color:var(--color-text-muted);padding:32px;">No enquiries yet.</td></tr>`
            : (contacts || []).map(c => `
              <tr>
                <td>${new Date(c.created_at).toLocaleDateString("en-GB")}</td>
                <td>${c.name || "—"}</td>
                <td><a href="mailto:${c.email}">${c.email || "—"}</a></td>
                <td>${c.phone || "—"}</td>
                <td>${c.service || "—"}</td>
                <td style="max-width:220px;font-size:0.82rem;">${c.message || "—"}</td>
              </tr>`).join("")}
        </tbody>
      </table>
    </div>
  `;
}

// ── Init ──────────────────────────────────────────────────────────────────────
checkAuth();
