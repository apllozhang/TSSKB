/* 知识版图 — 数据运行时取自本页课程卡片（单一真源 = DOM），课程增删图表自动跟随。
   色值经 tokens.css 令牌读取；依赖 /assets/js/vendor/echarts.min.js。
   图表仅作形状概览，精确数值以目录卡片为准。 */
(function () {
  "use strict";

  function init() {
    if (typeof echarts === "undefined") return;
    var root = document.documentElement;
    var css = getComputedStyle(root);
    function tok(name, fallback) {
      var v = css.getPropertyValue(name).trim();
      return v || fallback;
    }
    var purple700 = tok("--ale-purple-700", "#4f3478");
    var purple600 = tok("--ale-purple-600", "#6b489d");
    var purple500 = tok("--ale-purple-500", "#7e5cb4");
    var ink900 = tok("--ink-900", "#1a1a1a");
    var ink500 = tok("--ink-500", "#75787b");
    var line = tok("--line", "#d9d9d6");
    var reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

    function planCards(scope) {
      var out = [];
      (scope || document).querySelectorAll(".course-card").forEach(function (card) {
        if (!card.classList.contains("planned")) out.push(card);
      });
      return out;
    }
    function chipNum(card, unit) {
      var re = new RegExp("(\\d+)\\s*" + unit);
      var chips = card.querySelectorAll(".chips span");
      for (var i = 0; i < chips.length; i++) {
        var m = chips[i].textContent.match(re);
        if (m) return parseInt(m[1], 10);
      }
      return null;
    }

    var tooltipStyle = {
      backgroundColor: "#fff",
      borderColor: line,
      borderWidth: 1,
      textStyle: { color: ink900, fontSize: 13 },
      extraCssText: "box-shadow:0 10px 30px rgb(50 36 76 / 14%);border-radius:8px;",
    };
    var charts = [];

    /* ── 图 1：各分类知识单元数（轴标注明课程数） ── */
    var elCat = document.getElementById("km-category-chart");
    if (elCat) {
      var groups = [];
      document.querySelectorAll(".catalog-group").forEach(function (g) {
        var h = g.querySelector(".catalog-heading h3");
        if (!h) return;
        var cards = planCards(g);
        var units = 0;
        cards.forEach(function (card) {
          var n = chipNum(card, "单元");
          if (n != null) units += n;
        });
        groups.push({ name: h.textContent.trim(), courses: cards.length, units: units });
      });
      groups.sort(function (a, b) { return b.units - a.units; });
      var byName = {};
      groups.forEach(function (g) { byName[g.name] = g; });

      var catChart = echarts.init(elCat);
      var catNarrow = elCat.clientWidth < 480; /* 窄容器隐藏 x 轴刻度（柱端已有精确值，刻度冗余且会重叠） */
      catChart.setOption({
        animation: !reducedMotion,
        backgroundColor: "transparent",
        tooltip: Object.assign({}, tooltipStyle, {
          trigger: "item",
          formatter: function (p) {
            var g = byName[p.name] || {};
            return (
              '<div style="font-weight:700;color:' + purple700 + '">' + p.name + "</div>" +
              '<div style="color:' + ink500 + ';margin-top:4px">' + g.courses + " 门课程 · " + g.units + " 个知识单元</div>"
            );
          },
        }),
        grid: { left: 8, right: 44, top: 8, bottom: 24, containLabel: true },
        xAxis: {
          type: "value",
          splitLine: { lineStyle: { color: line, opacity: 0.6 } },
          axisLabel: { show: !catNarrow, color: ink500, fontSize: 11 },
        },
        yAxis: {
          type: "category",
          inverse: true,
          data: groups.map(function (g) { return g.name; }),
          axisLine: { lineStyle: { color: line } },
          axisTick: { show: false },
          axisLabel: {
            color: ink900,
            fontSize: 12,
            formatter: function (name) {
              var g = byName[name];
              return name + "\n" + (g ? g.courses + " 门" : "");
            },
          },
        },
        series: [{
          type: "bar",
          barWidth: 14,
          itemStyle: { color: purple600, borderRadius: [0, 6, 6, 0] },
          label: { show: true, position: "right", color: ink500, fontSize: 11 },
          data: groups.map(function (g) { return g.units; }),
        }],
      });
      charts.push(catChart);
    }

    /* ── 图 2：课程体量 Top10（官方教材页数） ── */
    var elPages = document.getElementById("km-pages-chart");
    if (elPages) {
      var pages = [];
      planCards(document).forEach(function (card) {
        var h4 = card.querySelector("h4");
        var pg = chipNum(card, "页");
        if (h4 && pg != null) pages.push({ name: h4.textContent.trim(), pages: pg });
      });
      pages.sort(function (a, b) { return b.pages - a.pages; });
      pages = pages.slice(0, 10);
      var byTitle = {};
      pages.forEach(function (p) { byTitle[p.name] = p; });
      function short(t) {
        return t.length > 18 ? t.slice(0, 17) + "…" : t;
      }

      var pageChart = echarts.init(elPages);
      var pageNarrow = elPages.clientWidth < 480;
      pageChart.setOption({
        animation: !reducedMotion,
        backgroundColor: "transparent",
        tooltip: Object.assign({}, tooltipStyle, {
          trigger: "item",
          formatter: function (p) {
            var d = pages[p.dataIndex] || { name: p.name, pages: p.value };
            return (
              '<div style="font-weight:700;color:' + purple700 + '">' + d.name + "</div>" +
              '<div style="color:' + ink500 + ';margin-top:4px">官方教材 ' + d.pages + " 页</div>"
            );
          },
        }),
        grid: { left: 8, right: 56, top: 8, bottom: 24, containLabel: true },
        xAxis: {
          type: "value",
          splitLine: { lineStyle: { color: line, opacity: 0.6 } },
          axisLabel: { show: !pageNarrow, color: ink500, fontSize: 11 },
        },
        yAxis: {
          type: "category",
          inverse: true,
          data: pages.map(function (p) { return short(p.name); }),
          axisLine: { lineStyle: { color: line } },
          axisTick: { show: false },
          axisLabel: { color: ink900, fontSize: 12 },
        },
        series: [{
          type: "bar",
          barWidth: 14,
          itemStyle: {
            color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [
              { offset: 0, color: purple700 },
              { offset: 1, color: purple500 },
            ]),
            borderRadius: [0, 6, 6, 0],
          },
          label: { show: true, position: "right", color: ink500, fontSize: 11, formatter: "{c} 页" },
          data: pages.map(function (p) { return p.pages; }),
        }],
      });
      charts.push(pageChart);
    }

    window.addEventListener("resize", function () {
      charts.forEach(function (c) { c.resize(); });
      if (elCat) {
        var n1 = elCat.clientWidth < 480;
        if (n1 !== catNarrow) { catNarrow = n1; catChart.setOption({ xAxis: { axisLabel: { show: !n1 } } }); }
      }
      if (elPages) {
        var n2 = elPages.clientWidth < 480;
        if (n2 !== pageNarrow) { pageNarrow = n2; pageChart.setOption({ xAxis: { axisLabel: { show: !n2 } } }); }
      }
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
