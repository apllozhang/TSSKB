/**
 * TSSKB 登录页交互 —— 移植自 ale-dan 登录页的 GSAP 动效：
 * 全屏轮播（Ken Burns + 交叉淡入）、逐字轮换文案、卡片入场动画。
 */
(function () {
  "use strict";

  var SLIDE_TEXTS = [
    "培训教材一站汇集，知识触手可及",
    "全文检索快速精准，直达目标内容",
    "内容契约严格校验，质量持续可信",
    "发布版本原子切换，随时可回滚",
  ];
  var SLIDE_INTERVAL_MS = 6000;

  /* ==================== 全屏轮播 ==================== */

  function initCarousel() {
    var carousel = document.getElementById("login-carousel");
    if (!carousel) return null;

    var layers = carousel.querySelectorAll(".carousel-layer");
    var dots = carousel.querySelectorAll(".dot");
    var current = 0;
    var timer = null;

    function startKenBurns(index) {
      var el = layers[index];
      if (!el) return;
      el.classList.remove("ken-left", "ken-right");
      void el.offsetWidth; /* 重启动画 */
      el.classList.add(index % 2 === 0 ? "ken-left" : "ken-right");
    }

    function show(index) {
      layers[current].classList.remove("is-active");
      layers[current].classList.remove("ken-left", "ken-right");
      dots[current].classList.remove("is-active");

      current = index;
      layers[current].classList.add("is-active");
      dots[current].classList.add("is-active");
      startKenBurns(current);
    }

    function next() {
      show((current + 1) % layers.length);
    }

    /* 预加载图片，首图就绪后启动 */
    var first = new Image();
    var started = false;
    function begin() {
      if (started) return;
      started = true;
      layers[0].classList.add("is-active");
      startKenBurns(0);
      for (var i = 1; i < layers.length; i++) {
        var img = new Image();
        img.src = getBgUrl(layers[i]);
      }
      timer = setInterval(next, SLIDE_INTERVAL_MS);
    }
    function getBgUrl(el) {
      var style = window.getComputedStyle(el).backgroundImage;
      var match = style && style.match(/url\(["']?([^"')]+)["']?\)/);
      return match ? match[1] : "";
    }
    first.onload = begin;
    first.src = getBgUrl(layers[0]);
    if (first.complete) begin();
    /* 兜底：图片加载失败也要呈现渐变背景与登录表单 */
    setTimeout(begin, 2500);

    return { stop: function () { if (timer) clearInterval(timer); } };
  }

  /* ==================== 逐字轮换文案 ==================== */

  function initRotatingText() {
    var charsEl = document.getElementById("rotating-chars");
    var lineEl = document.getElementById("rotating-line");
    var barEl = document.getElementById("progress-bar");
    if (!charsEl || !lineEl || !barEl) return;

    var index = 0;

    function renderChars(text) {
      charsEl.textContent = "";
      var chars = text.split("");
      for (var i = 0; i < chars.length; i++) {
        var span = document.createElement("span");
        span.className = "char";
        span.textContent = chars[i];
        span.style.transitionDelay = i * 25 + "ms";
        charsEl.appendChild(span);
      }
    }

    function animateIn() {
      lineEl.classList.remove("is-in");
      barEl.classList.remove("is-filling");
      void lineEl.offsetWidth;
      lineEl.classList.add("is-in");
      barEl.classList.add("is-filling");

      var spans = charsEl.querySelectorAll(".char");
      for (var i = 0; i < spans.length; i++) {
        (function (el, delay) {
          setTimeout(function () {
            el.classList.add("is-in");
          }, delay);
        })(spans[i], 200 + i * 25);
      }
    }

    function animateOutThen(text) {
      charsEl.classList.add("is-out");
      var spans = charsEl.querySelectorAll(".char");
      var outDelay = 0;
      for (var i = spans.length - 1; i >= 0; i--) {
        (function (el, delay) {
          setTimeout(function () {
            el.classList.remove("is-in");
          }, delay);
        })(spans[i], outDelay);
        outDelay += 15;
      }

      setTimeout(function () {
        charsEl.classList.remove("is-out");
        renderChars(text);
        animateIn();
      }, outDelay + 320);
    }

    function showSlide(i) {
      animateOutThen(SLIDE_TEXTS[i]);
    }

    renderChars(SLIDE_TEXTS[0]);
    animateIn();

    setInterval(function () {
      index = (index + 1) % SLIDE_TEXTS.length;
      showSlide(index);
    }, SLIDE_INTERVAL_MS);
  }

  /* ==================== 登录表单 ==================== */

  function safeNextPath() {
    var params = new URLSearchParams(location.search);
    var next = params.get("next") || "";
    try {
      next = next || sessionStorage.getItem("tsskb_auth_next") || "";
    } catch (err) {
      /* ignore */
    }
    if (next && next.charAt(0) === "/" && next.charAt(1) !== "/") {
      return next;
    }
    return "/index.html";
  }

  function initLoginForm() {
    var form = document.getElementById("login-form");
    var errorEl = document.getElementById("form-error");
    var btn = document.getElementById("login-btn");
    var label = document.getElementById("login-btn-label");
    if (!form || !window.TSSKB || !window.TSSKB.auth) return;

    /* 已登录直接进入 */
    if (window.TSSKB.auth.isAuthed()) {
      location.replace(safeNextPath());
      return;
    }

    function setError(message) {
      if (message) {
        errorEl.textContent = message;
        errorEl.classList.add("is-visible");
      } else {
        errorEl.textContent = "";
        errorEl.classList.remove("is-visible");
      }
    }

    function setPending(pending) {
      btn.disabled = pending;
      label.textContent = pending ? "登录中..." : "登 录";
      if (pending) {
        var spinner = document.createElement("span");
        spinner.className = "spinner";
        label.parentNode.insertBefore(spinner, label);
      } else {
        var old = btn.querySelector(".spinner");
        if (old) old.remove();
      }
    }

    form.addEventListener("submit", function (event) {
      event.preventDefault();
      setError("");

      var username = document.getElementById("username").value.trim();
      var password = document.getElementById("password").value;
      if (!username || !password) {
        setError("请输入用户名和密码");
        return;
      }

      setPending(true);
      window.TSSKB.auth
        .login(username, password)
        .then(function () {
          var next = safeNextPath();
          try {
            sessionStorage.removeItem("tsskb_auth_next");
          } catch (err) {
            /* ignore */
          }
          location.replace(next);
        })
        .catch(function () {
          setPending(false);
          setError("用户名或密码错误");
        });
    });
  }

  /* ==================== 启动 ==================== */

  function boot() {
    var yearEl = document.getElementById("copyright-year");
    if (yearEl) yearEl.textContent = String(new Date().getFullYear());
    initCarousel();
    initRotatingText();
    initLoginForm();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();
