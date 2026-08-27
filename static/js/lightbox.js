(() => {
  const images = document.querySelectorAll(".markdown-body img, .product-gallery img");
  if (!images.length) return;
  const box = document.createElement("div");
  box.className = "lightbox";
  box.setAttribute("role", "dialog");
  box.setAttribute("aria-modal", "true");
  box.setAttribute("aria-label", "图片预览");
  box.innerHTML = '<img alt=""><div class="lightbox-controls"><button data-action="out" aria-label="缩小">−</button><button data-action="reset" aria-label="恢复原始大小">100%</button><button data-action="in" aria-label="放大">＋</button><button data-action="close" aria-label="关闭">✕</button></div>';
  document.body.appendChild(box);
  const preview = box.querySelector("img");
  const resetLabel = box.querySelector('[data-action="reset"]');
  let scale = 1;
  const apply = () => {
    preview.style.transform = `scale(${scale})`;
    resetLabel.textContent = `${Math.round(scale * 100)}%`;
  };
  const close = () => { box.classList.remove("open"); document.body.style.overflow = ""; };
  const open = (source) => {
    preview.src = source.src;
    preview.alt = source.alt || "图片预览";
    scale = 1;
    apply();
    box.classList.add("open");
    document.body.style.overflow = "hidden";
    box.querySelector('[data-action="close"]').focus();
  };
  images.forEach((image) => {
    image.setAttribute("tabindex", "0");
    image.addEventListener("click", () => open(image));
    image.addEventListener("keydown", (event) => { if (event.key === "Enter") open(image); });
  });
  box.addEventListener("click", (event) => {
    const action = event.target.dataset.action;
    if (action === "close" || event.target === box) close();
    if (action === "in") { scale = Math.min(5, scale * 1.25); apply(); }
    if (action === "out") { scale = Math.max(.25, scale / 1.25); apply(); }
    if (action === "reset") { scale = 1; apply(); }
  });
  document.addEventListener("keydown", (event) => { if (event.key === "Escape") close(); });
})();
