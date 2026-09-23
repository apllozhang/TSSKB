/**
 * TSSKB 全站登录门卫：在 base.html <head> 中同步加载，
 * 未登录时在页面渲染前重定向到 /login.html。
 */
(function () {
  "use strict";

  var auth = window.TSSKB && window.TSSKB.auth;
  if (!auth) return;

  if (!auth.isAuthed()) {
    try {
      var next =
        location.pathname + location.search + location.hash;
      sessionStorage.setItem("tsskb_auth_next", next);
    } catch (err) {
      /* 隐私模式下 sessionStorage 不可用时忽略 */
    }
    location.replace("/login.html");
    return;
  }

  function wireLogout() {
    var btn = document.getElementById("logout-btn");
    if (!btn || btn.dataset.wired) return;
    btn.hidden = false;
    btn.dataset.wired = "1";
    btn.addEventListener("click", function () {
      auth.logout();
      location.replace("/login.html");
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", wireLogout);
  } else {
    wireLogout();
  }
})();
