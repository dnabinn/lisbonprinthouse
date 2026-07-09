/* ============================================
   Lisbon Print House — Global Config & Scripts
   Swap WHATSAPP_NUMBER below when the real number is ready.
   ============================================ */
const LPH = {
  WHATSAPP_NUMBER: "351920418547",
  WHATSAPP_DEFAULT_MESSAGE: "Hi! I'd like to request a printing quote.",
};

function waLink(message){
  const msg = encodeURIComponent(message || LPH.WHATSAPP_DEFAULT_MESSAGE);
  return `https://wa.me/${LPH.WHATSAPP_NUMBER}?text=${msg}`;
}

document.addEventListener("DOMContentLoaded", () => {
  // Populate every WhatsApp CTA with the live link + message (data-wa-message optional override)
  document.querySelectorAll("[data-wa]").forEach(el => {
    el.href = waLink(el.getAttribute("data-wa-message"));
    el.target = "_blank";
    el.rel = "noopener noreferrer";
  });

  // Mobile nav toggle
  const toggle = document.querySelector(".nav-toggle");
  const links = document.querySelector(".nav-links");
  if (toggle && links) {
    toggle.addEventListener("click", () => links.classList.toggle("open"));
    links.querySelectorAll("a").forEach(a => a.addEventListener("click", () => links.classList.remove("open")));
  }

  // Active nav link
  const path = location.pathname.split("/").pop() || "index.html";
  document.querySelectorAll(".nav-links a").forEach(a => {
    const href = a.getAttribute("href");
    if (href === path || (path === "" && href === "index.html")) a.classList.add("active");
  });

  // Fade-up on scroll
  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => { if (entry.isIntersecting) entry.target.classList.add("in-view"); });
  }, { threshold: 0.15 });
  document.querySelectorAll(".fade-up").forEach(el => observer.observe(el));

  // Animated counters
  const counters = document.querySelectorAll("[data-counter]");
  const counterObserver = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (!entry.isIntersecting) return;
      const el = entry.target;
      const target = parseInt(el.getAttribute("data-counter"), 10);
      let current = 0;
      const step = Math.max(1, Math.ceil(target / 60));
      const tick = () => {
        current += step;
        if (current >= target) { el.textContent = target.toLocaleString(); return; }
        el.textContent = current.toLocaleString();
        requestAnimationFrame(tick);
      };
      tick();
      counterObserver.unobserve(el);
    });
  }, { threshold: 0.4 });
  counters.forEach(el => counterObserver.observe(el));

  // Portfolio filters
  const filterBtns = document.querySelectorAll(".filter-btn");
  if (filterBtns.length) {
    filterBtns.forEach(btn => {
      btn.addEventListener("click", () => {
        filterBtns.forEach(b => b.classList.remove("active"));
        btn.classList.add("active");
        const cat = btn.getAttribute("data-filter");
        document.querySelectorAll(".masonry-item").forEach(item => {
          item.hidden = cat !== "all" && item.getAttribute("data-category") !== cat;
        });
      });
    });
  }

  // Contact form -> redirect to WhatsApp with prefilled message
  const quoteForm = document.querySelector("#quote-form");
  if (quoteForm) {
    quoteForm.addEventListener("submit", (e) => {
      e.preventDefault();
      const data = new FormData(quoteForm);
      const name = data.get("name") || "";
      const service = data.get("service") || "";
      const details = data.get("details") || "";
      const msg = `Hi! My name is ${name}. I'd like a quote for: ${service}. Details: ${details}`;
      window.open(waLink(msg), "_blank");
    });
  }
});
