/**
 * TSSKB 图片灯箱：缩略图点击放大 + 加/减/恢复按钮 + 滚轮以光标为中心缩放
 * + 拖拽平移 + 双击缩放 + 键盘（+/-/0/Esc）。
 */
(() => {
  const SCALE_MIN = 0.25;
  const SCALE_MAX = 8;
  const images = document.querySelectorAll(".markdown-body img, .product-gallery img");
  if (!images.length) return;

  const box = document.createElement("div");
  box.className = "lightbox";
  box.setAttribute("role", "dialog");
  box.setAttribute("aria-modal", "true");
  box.setAttribute("aria-label", "图片预览");
  box.innerHTML =
    '<img alt="">' +
    '<div class="lightbox-zoom-pill" id="lightbox-zoom-pill">100%</div>' +
    '<div class="lightbox-controls">' +
    '<button data-action="out" aria-label="缩小" title="缩小（-）">−</button>' +
    '<button data-action="reset" aria-label="恢复正常大小" title="恢复正常（0）">100%</button>' +
    '<button data-action="in" aria-label="放大" title="放大（+）">＋</button>' +
    '<button data-action="close" aria-label="关闭" title="关闭（Esc）">✕</button>' +
    "</div>";
  document.body.appendChild(box);

  const preview = box.querySelector("img");
  const zoomPill = box.querySelector("#lightbox-zoom-pill");
  const resetButton = box.querySelector('[data-action="reset"]');
  let scale = 1;
  let tx = 0;
  let ty = 0;

  const clamp = (value) => Math.min(SCALE_MAX, Math.max(SCALE_MIN, value));

  const apply = () => {
    preview.style.transform = "translate(" + tx + "px, " + ty + "px) scale(" + scale + ")";
    const label = Math.round(scale * 100) + "%";
    resetButton.textContent = label;
    zoomPill.textContent = label;
    zoomPill.style.opacity = scale === 1 ? "0" : "1";
  };

  const close = () => {
    box.classList.remove("open");
    document.body.style.overflow = "";
  };

  const open = (source) => {
    preview.src = source.src;
    preview.alt = source.alt || "图片预览";
    scale = 1;
    tx = 0;
    ty = 0;
    preview.style.transformOrigin = "center";
    apply();
    box.classList.add("open");
    document.body.style.overflow = "hidden";
    box.querySelector('[data-action="close"]').focus();
  };

  /* 以视口点 (clientX, clientY) 为中心缩放：用 transform-origin 定位光标下的图像比例点 */
  const zoomAt = (clientX, clientY, factor) => {
    const rect = preview.getBoundingClientRect();
    const px = ((clientX - rect.left) / rect.width) * 100;
    const py = ((clientY - rect.top) / rect.height) * 100;
    preview.style.transformOrigin = px.toFixed(2) + "% " + py.toFixed(2) + "%";
    scale = clamp(scale * factor);
    apply();
  };

  const zoomCentered = (factor) => {
    preview.style.transformOrigin = "center";
    scale = clamp(scale * factor);
    apply();
  };

  images.forEach((image) => {
    image.setAttribute("tabindex", "0");
    image.addEventListener("click", () => open(image));
    image.addEventListener("keydown", (event) => {
      if (event.key === "Enter") open(image);
    });
  });

  /* 工具条按钮 */
  box.addEventListener("click", (event) => {
    const action = event.target.dataset.action;
    if (action === "close" || event.target === box) close();
    if (action === "in") zoomCentered(1.25);
    if (action === "out") zoomCentered(1 / 1.25);
    if (action === "reset") {
      preview.style.transformOrigin = "center";
      scale = 1;
      tx = 0;
      ty = 0;
      apply();
    }
  });

  /* 滚轮缩放（以光标为中心） */
  box.addEventListener(
    "wheel",
    (event) => {
      if (!box.classList.contains("open")) return;
      event.preventDefault();
      zoomAt(event.clientX, event.clientY, event.deltaY < 0 ? 1.2 : 1 / 1.2);
    },
    { passive: false },
  );

  /* 双击：1x ↔ 2.5x 切换 */
  preview.addEventListener("dblclick", (event) => {
    event.preventDefault();
    if (scale > 1.05) {
      preview.style.transformOrigin = "center";
      scale = 1;
      tx = 0;
      ty = 0;
      apply();
    } else {
      zoomAt(event.clientX, event.clientY, 2.5 / Math.max(scale, 0.01));
    }
  });

  /* 拖拽平移（放大后可用） */
  let dragging = false;
  let startX = 0;
  let startY = 0;
  preview.addEventListener("mousedown", (event) => {
    if (scale <= 1) return;
    event.preventDefault();
    dragging = true;
    startX = event.clientX - tx;
    startY = event.clientY - ty;
    preview.style.cursor = "grabbing";
  });
  window.addEventListener("mousemove", (event) => {
    if (!dragging) return;
    tx = event.clientX - startX;
    ty = event.clientY - startY;
    apply();
  });
  window.addEventListener("mouseup", () => {
    dragging = false;
    preview.style.cursor = scale > 1 ? "grab" : "zoom-in";
  });

  /* 键盘：+ / - / 0 / Esc，方向键平移 */
  document.addEventListener("keydown", (event) => {
    if (!box.classList.contains("open")) return;
    if (event.key === "Escape") close();
    if (event.key === "+" || event.key === "=") zoomCentered(1.25);
    if (event.key === "-" || event.key === "_") zoomCentered(1 / 1.25);
    if (event.key === "0") {
      preview.style.transformOrigin = "center";
      scale = 1;
      tx = 0;
      ty = 0;
      apply();
    }
    const step = 60;
    if (event.key === "ArrowLeft") { tx += step; apply(); }
    if (event.key === "ArrowRight") { tx -= step; apply(); }
    if (event.key === "ArrowUp") { ty += step; apply(); }
    if (event.key === "ArrowDown") { ty -= step; apply(); }
  });
})();
