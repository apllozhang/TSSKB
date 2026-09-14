# TSSKB × ALE WebUI v6 试点（v6-pilot 分支）

> M5 三项目试点之一。范围：课程内容页（Static + content-site 链路）；不动 main、不改内容契约与构建管线语义。

## 变更

1. `static/css/tokens.css`：整体替换为 webui kit 生成物（vendored 副本，单一令牌真源）；
2. `static/css/tokens-bridge.css`（新增）：历史变量名 → v6 语义令牌映射（ink/surface/line/content-width/category-accent 兜底），不新增任何色值；
3. `templates/base.html`：加载 bridge；
4. `static/css/content.css`：长文阅读区限宽 `--reading-max`（760px）。

## 试点页与验证

- 页面：`/aos/advanced-routing/skills/aos-ar-bgp.html`（知识单元）、`/aos/advanced-routing/overview.html`（课程概览）
- 断言（webui kit/tools/_pilot/verify-tsskb.mjs）：资产 200、阅读宽度 760 实测一致、内容层级无跳级、ALE 令牌生效（#6b489d）、控制台零错、320 根级无溢出 —— **12/12 PASS**
- 截图：320+1440（webui 仓库 _pilot-evidence/tsskb/）
- 迁移耗时：约 40 分钟（含流水线构建）；缺失令牌：无（bridge 层映射即可满足）；视觉差异：暗色 slate 旧版 → ALE 亮色令牌（预期内换肤）

- **R4-02 字体接入(M6-R1)**:vendored `static/fonts/noto.css`(构建映射 /assets/fonts/) + `noto/*.woff2`(400/500/700,SIL OFL,与 kit shared 同源),页面真实请求 200、FontFaceSet loaded、`document.fonts.check` 命中——FONT-CHAIN PASS。
