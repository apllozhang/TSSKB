# 2026-09-23 线上分叉合并与产物回流

## 背景

GitHub 主干与本轮线上部署出现三层分叉：

1. **内容漂移**：103（staging，先建）与 203（prod，后建）之间 61 页正文实质漂移，绝大多数 203 更新（Golden RFP 补充、硬件/彩页修订、认证课程等）。
2. **功能只在服务器上**：203 的登录认证体系（auth-config / auth-core / auth-guard + login 三件套）与 103 的知识版图（charts.css / knowledge-map.js / path-progress.js / echarts）都不在仓库里——漂移的根源。
3. **仓库滞后**：仓库 site/ 停留在 8 月底构建产物，static/ 缺上述全部新资产。

## 本次处置（2026-09-23）

以 **203 线上终版为基线**，把 103 的知识版图功能合并进去，产出统一版本：

- **203（prod）**：统一版本 + 登录认证（auth local 模式，用户 aletss，密码哈希未动）。已发布到 `/vol4/apps/tsskb/site`（rsync 就地同步），14 项健康检查通过。回滚点：`/vol4/apps/tsskb/site.bak-kg2`。
- **103（staging）**：同一版本、剥离每页 auth 引用（免登录，方便测试）。按原子发布模型上线 `releases/20260923-staging-kg`。回滚点：旧 release `65bd483f8bb9a21c`。
- **仓库回流**：`site/` ← 203 线上终版（837 文件）；`static/` ← 线上 assets/（32 文件，含认证、登录、知识版图、vendor/echarts、轮播图、面板图等全部资产）。

漂移清零：两站由同一份产物部署，唯一差异是 103 免认证。

## 已知债务（后续处理）

1. **books/ 源滞后于 site/ 产物**：61 页内容修订未反推回蒸馏源。在补齐源之前，**不要对 site/ 跑全量 `tsskb build` 覆盖**，否则会用旧源回退线上内容。
2. **认证与知识版图未进 build 管线**：两套功能的模板注入逻辑目前只存在于产物层（每页 HTML 已带），`src/tsskb/build` 与 `templates/` 尚无对应模板参数。后续应做成构建开关（如 `auth.enabled`、`knowledge_map.enabled`）。
3. **103 免认证版未参数化**：当前是部署时用脚本剥离 auth 引用（脚本在本地工作区 `.cangjie/`），应演进为构建 flavor。

## 两站角色（本轮起固定）

| 站点 | 角色 | 认证 | 发布方式 |
|---|---|---|---|
| 103:8899 | 测试验证床 | 无 | tsskb 原子发布（releases/ + current 软链） |
| 203:8090 | 生产 | local 模式（aletss / SHA-256） | tsskb-web 容器只读挂载，rsync 就地同步 |

发布流程：仓库 main → 构建产物 → 103 验证 → 203 发布。禁止直接改线上页面（本轮之前的漂移即由此产生）。
