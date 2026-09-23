/* 学习路径阶段推进图 — 数据运行时取自本页 .learning-path 清单（单一真源 = DOM），
   课程增删图表自动跟随。每段为一步，颜色由浅入深即建议顺序；点击色块直达课程。
   色值经 tokens.css 令牌读取；依赖 /assets/js/vendor/echarts.min.js。 */
(function () {
  "use strict";

  function init() {
    if (typeof echarts === "undefined") return;
    var el = document.getElementById("path-progress-chart");
    if (!el) return;
    var css = getComputedStyle(document.documentElement);
    function tok(name, fallback) {
      var v = css.getPropertyValue(name).trim();
      return v || fallback;
    }
    var purple700 = tok("--ale-purple-700", "#4f3478");
    var purple500 = tok("--ale-purple-500", "#7e5cb4");
    var purple100 = tok("--ale-purple-100", "#f1ecf7");
    var ink900 = tok("--ink-900", "#1a1a1a");
    var ink500 = tok("--ink-500", "#75787b");
    var line = tok("--line", "#d9d9d6");
    var reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

    /* ── DOM 取数：三条路径 → 行，各步 → 段 ── */
    var rows = [];
    document.querySelectorAll(".learning-path").forEach(function (sec) {
      var h2 = sec.querySelector(".path-cover header h2");
      var steps = [];
      sec.querySelectorAll("ol > li").forEach(function (li) {
        var a = li.querySelector("a");
        var p = li.querySelector("p");
        if (!a) return;
        steps.push({ title: a.textContent.trim(), desc: p ? p.textContent.trim() : "", href: a.getAttribute("href") || "" });
      });
      if (h2 && steps.length) rows.push({ name: h2.textContent.trim(), steps: steps });
    });
    if (!rows.length) return;
    var maxSteps = Math.max.apply(null, rows.map(function (r) { return r.steps.length; }));
    var rowByName = {};
    rows.forEach(function (r) { rowByName[r.name] = r; });

    function hex2rgb(x) {
      return [parseInt(x.slice(1, 3), 16), parseInt(x.slice(3, 5), 16), parseInt(x.slice(5, 7), 16)];
    }
    function mixRGB(A, B, t) {
      return A.map(function (v, i) { return Math.round(v + (B[i] - v) * t); });
    }
    function cssRGB(A) { return "rgb(" + A.join(" ") + ")"; }

    var chart = echarts.init(el);
    var narrow = el.clientWidth < 480;

    /* 三段式全幅梯度：浅紫起步 → 紫500 → 深紫收尾，段间区分度优先。
       浅端不是纯紫100（白卡片上会隐形），混 25% 紫500 保底可见度。 */
    var rampStartA = mixRGB(hex2rgb(purple100), hex2rgb(purple500), 0.25);
    function segColor(t) {
      var A = t < 0.5
        ? mixRGB(rampStartA, hex2rgb(purple500), t * 2)
        : mixRGB(hex2rgb(purple500), hex2rgb(purple700), (t - 0.5) * 2);
      return cssRGB(A);
    }
    /* 底色亮度自适应文字色：浅底深字、深底白字 */
    function textOn(rgb) {
      var m = rgb.match(/(\d+)/g) || [0, 0, 0];
      var lum = (0.299 * m[0] + 0.587 * m[1] + 0.114 * m[2]) / 255;
      return lum > 0.6 ? ink900 : "#fff";
    }

    /* 堆叠条实现阶段段：第 i 步 = 第 i 个系列在该行落 1 格，颜色由浅入深 */
    var series = [];
    var loop = maxSteps;
    for (var i = 0; i < loop; i++) {
      (function (i) {
        series.push({
          type: "bar",
          stack: "path",
          barWidth: 30,
          cursor: "pointer",
          itemStyle: { borderColor: "#fff", borderWidth: 2 },
          label: {
            show: true, position: "inside", fontWeight: 700, fontSize: 12, color: "#fff",
            formatter: function (p) { return p.data.stepNo; },
          },
          data: rows.map(function (r) {
            var s = r.steps[i];
            if (!s) return null;
            var t = loop > 1 ? i / (loop - 1) : 0;
            var first = i === 0, last = i === r.steps.length - 1;
            var bg = segColor(t);
            return {
              value: 1, stepNo: i + 1, step: s, row: r.name,
              itemStyle: {
                color: bg,
                borderRadius: first ? [6, 0, 0, 6] : (last ? [0, 6, 6, 0] : 0),
              },
              label: { color: textOn(bg) },
            };
          }),
        });
      })(i);
    }

    chart.setOption({
      animation: !reducedMotion,
      backgroundColor: "transparent",
      tooltip: {
        trigger: "item",
        backgroundColor: "#fff",
        borderColor: line,
        borderWidth: 1,
        textStyle: { color: ink900, fontSize: 13 },
        extraCssText: "box-shadow:0 10px 30px rgb(50 36 76 / 14%);border-radius:8px;",
        formatter: function (p) {
          var d = p.data;
          if (!d || !d.step) return "";
          var desc = d.step.desc.length > 46 ? d.step.desc.slice(0, 45) + "…" : d.step.desc;
          return (
            '<div style="font-weight:700;color:' + purple700 + '">第 ' + d.stepNo + " 步 · " + d.step.title + "</div>" +
            '<div style="color:' + ink500 + ';margin-top:4px;max-width:260px">' + desc + "</div>" +
            '<div style="color:' + purple500 + ';margin-top:4px">点击进入课程 →</div>'
          );
        },
      },
      grid: { left: 8, right: 24, top: 8, bottom: 30, containLabel: true },
      xAxis: {
        type: "value", min: 0, max: maxSteps, interval: 1,
        splitLine: { show: false },
        axisLine: { show: false }, axisTick: { show: false },
        axisLabel: { show: !narrow, color: ink500, fontSize: 11 },
        name: "步骤", nameLocation: "middle", nameGap: 26, nameTextStyle: { color: ink500, fontSize: 11 },
      },
      yAxis: {
        type: "category", inverse: true,
        data: rows.map(function (r) { return r.name; }),
        axisLine: { lineStyle: { color: line } },
        axisTick: { show: false },
        axisLabel: {
          color: ink900, fontSize: 12,
          formatter: function (n) { var r = rowByName[n]; return n + "\n" + (r ? r.steps.length + " 步" : ""); },
        },
      },
      series: series,
    });

    chart.on("click", function (p) {
      var d = p.data;
      if (d && d.step && d.step.href) window.location.href = d.step.href;
    });

    window.addEventListener("resize", function () {
      chart.resize();
      var n2 = el.clientWidth < 480;
      if (n2 !== narrow) { narrow = n2; chart.setOption({ xAxis: { axisLabel: { show: !n2 } } }); }
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
