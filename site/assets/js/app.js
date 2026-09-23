(() => {
  const toggle = document.querySelector("[data-nav-toggle]");
  const nav = document.getElementById("primary-nav");
  if (toggle && nav) {
    toggle.addEventListener("click", () => {
      const open = nav.classList.toggle("open");
      toggle.setAttribute("aria-expanded", String(open));
    });
  }

  const filter = document.querySelector("[data-category-filter]");
  if (filter) {
    filter.addEventListener("input", () => {
      const query = filter.value.trim().toLocaleLowerCase();
      document.querySelectorAll("[data-course-card]").forEach((card) => {
        card.hidden = Boolean(query) && !card.textContent.toLocaleLowerCase().includes(query);
      });
    });
  }

  // 桌面端目录栏折叠/展开（状态记忆，折叠后正文占满整行）
  const layout = document.querySelector(".course-layout");
  const sidebar = document.querySelector("[data-sidebar]");
  const isMobile = () => window.matchMedia("(max-width: 860px)").matches;
  if (layout && sidebar) {
    const CHEVRON_LEFT =
      '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="15 18 9 12 15 6"/></svg>';
    const CHEVRON_RIGHT =
      '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="9 18 15 12 9 6"/></svg>';
    const STORAGE_KEY = "tsskb_sidebar_collapsed";

    const rail = document.createElement("button");
    rail.type = "button";
    rail.className = "sidebar-rail";
    rail.title = "展开课程目录";
    rail.setAttribute("aria-label", "展开课程目录");
    rail.innerHTML = CHEVRON_RIGHT;
    document.body.appendChild(rail);

    const toggle = document.createElement("button");
    toggle.type = "button";
    toggle.className = "sidebar-toggle";
    toggle.title = "收起课程目录";
    toggle.setAttribute("aria-label", "收起课程目录");
    toggle.setAttribute("aria-expanded", "true");
    toggle.innerHTML = CHEVRON_LEFT;
    sidebar.appendChild(toggle);

    const apply = (collapsed) => {
      layout.classList.toggle("sidebar-collapsed", collapsed);
      toggle.setAttribute("aria-expanded", String(!collapsed));
      rail.hidden = !collapsed;
      localStorage.setItem(STORAGE_KEY, collapsed ? "1" : "0");
    };

    toggle.addEventListener("click", () => apply(true));
    rail.addEventListener("click", () => apply(false));

    if (!isMobile() && localStorage.getItem(STORAGE_KEY) === "1") {
      apply(true);
    }
  }

  if (sidebar && isMobile()) {
    const heading = sidebar.querySelector(".sidebar-heading");
    if (heading) {
      heading.setAttribute("role", "button");
      heading.setAttribute("tabindex", "0");
      heading.setAttribute("aria-label", "展开或收起课程目录");
      const activate = () => sidebar.classList.toggle("collapsed");
      heading.addEventListener("click", activate);
      heading.addEventListener("keydown", (event) => {
        if (event.key === "Enter" || event.key === " ") activate();
      });
    }
  }
})();
