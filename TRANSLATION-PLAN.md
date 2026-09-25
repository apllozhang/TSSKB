# TSSKB 翻译提升工作安排（v2 · 详细执行版）

> 制定：2026-09-25（v2，决策已回填）。执行者：任一能克隆本仓库的 AI/工程师（机器无关）。
> 方法论：COMKB 通信线 25 本验证过的翻译流水线——**分块锚定 + 术语硬约束 + 低并发幂等并行 +
> 三道门 QA（V1 回译忠实度 / V2 术语 lint / V3 双译比对）+ 事实零改动**。
> 提示词模板与故障处理：见姊妹仓库 apllozhang/COMKB 的 `HANDOFF.md` §4–§5（本文件只写差异）。
> 门户：8899（VPN 10.20.30.103:8899 ≡ 局域网 10.10.10.169:8899）。

## 0. 决策记录（2026-09-25 已拍板）

| # | 决策 | 内容 |
|---|---|---|
| D1 | **A（已定）** | 中文全文译文不入本公开仓库，存执行机本地；**备份到 10.10.10.169**（规程见 §6） |
| D2 | **A（已定）** | 阅读层形态 = 每本书详情页加"中文全文"入口/标签页，不做独立 /zh/ 板块 |
| D3 | **认可（已定）** | 首批六本：os-lan-vxlan-evpn、os-lan-core-switching-v2、os-lan-troubleshooting、ov2500-nms-admin、stellar-wlan-enterprise-basic、aos810-net-config |
| D4 | **并发 2 起步（已定）** | 固定 2 并发开跑；连续 3 轮（≥6 个子代理）零失败才可升 3；出现任何验证码超时/限流立即降回 2。**禁止 4 并发** |

## 1. 起点事实（已核实，命令须与此对齐）

- 源文两种路径变体并存，切分器必须都支持：
  - 根部：`books/<code>/fulltext.md`（core-switching-v2 668K、ov2500-nms-admin 601K、aos810-net-config **3770K**）
  - source/ 下：`books/<code>/source/fulltext.md`（vxlan-evpn 250K、troubleshooting 368K、stellar-enterprise-basic 284K）
- 六本书均有 GLOSSARY.md（116 份全库词汇表可聚合）。
- **体量警告**：首批合计约 5.9MB ≈ **990 块（6000 字符/块）≈ 通信线 25 本全项目的 4 倍**。
  其中 aos810-net-config 一本占 63%。因此：
  - aos810-net-config 先做**体量异常核查**（P2-0 任务）：抽样判断是否为 CLI 转储堆料；
    若命令表占比过高，只译叙述段/章节导语，块量可砍到 1/5 以下。
  - 工时口径：Phase 2 主体（除 net-config 外约 320 块）在 2 并发下约 **3–5 个工作日**墙钟。
- 构建系统：`tsskb build/validate/metrics`，CI quality-gate 必须全程绿灯。
- 部署凭据走 `TSSKB_DEPLOY_KEY` / `TSSKB_DEPLOY_PASSWORD` 环境变量（线下提供，不入仓库）。

## 2. 环境准备（一次性）

1. Python 3.10+，`pip install pyyaml`；克隆本仓库 + 姊妹仓库 apllozhang/COMKB（取提示词模板）。
2. 翻译工作目录约定：译文统一写 `books/<code>/zh-fulltext/`（已被 §4 的 .gitignore 拦截，不会进 git）。
3. 备份通道：到 10.10.10.169 的 SSH 凭据由交付方线下提供（不放仓库）。
4. 翻译子代理用执行方自己的模型账号；翻译过程不需要访问 8899，部署阶段才需要。

## 3. 阶段安排

### Phase 0 · 准备（约 1 天，纯确定性工作）

| # | 任务 | 做法 | 验收 |
|---|---|---|---|
| P0-1 | .gitignore 版权防线（本仓库） | 拦截 `**/zh-fulltext/`、`**/中文全译本*.md`、`*.handoff.zip`（已完成并提交） | `git status` 对译文目录不敏感 |
| P0-2 | 移植流水线到 `translation_tools/` | 从 COMKB pipeline/ 复制 translate_pipeline.py、build_term_table.py、translation_status.py（术语表 v3 产物 term_table.yaml 直接复制）；输入适配：fulltext 发现顺序 = `books/<code>/fulltext.md` → `books/<code>/source/fulltext.md` | `translation_status.py` 可运行（初始全 0） |
| P0-3 | 切分器 **md 模式** | 按 H1/H2 标题切块：小节合并至约 6000 字符、超大节二次按段落切；**标题行即锚**——译文必须逐字保留源文标题行（含编号），manifest 记"标题路径序列 + SHA256"；check 子命令校验锚序列 | 试点书 check PASS |
| P0-4 | 术语表 v3（网络域） | 聚合 116 份 GLOSSARY.md（根 GLOSSARY + candidates/glossary.md），共识(≥3 书)升全局、其余按书作用域；新增网络域 curated 与**保留英文缩写清单**（OSPF、VLAN、LACP、STP/RSTP、SPB、VXLAN、EVPN、MPLS、ISIS、BGP、VRRP、MC-LAG、QoS、ACL、MACsec、TCAM、ISSU、DDM、PoE、LLDP、RADIUS、DHCP、NAT、GRE、PIM、IGMP、MLD、UDLD、AMAP、EDP 等）；与通信域表合并为公司级表（域作用域隔离） | term_table v3 生成；试点书注入零冲突 |
| P0-5 | 语料分档清单 | `translation_tools/CORPUS-PLAN.md`：翻译书单（含顺序）、跳过书及理由 | 评审通过 |

### Phase 1 · 试点（约 1 天）——os-lan-vxlan-evpn（250K ≈ 42 块）

执行序列（每步验收不过不进下一步）：

```
1) chunk(md 模式)                    → work/en/chunkNNNN.txt + manifest.json
2) terms                             → work/terms/ 注入清单
3) A 译（2 并发 × ~4 块/代理）        → work/zh/
4) check                             → PASS（锚序列 100%）
5) B 译（意译对照，同并发纪律）       → work/zhb/
6) compare                           → work/qa/divergence.md（人工终审标记）
7) 回译抽查（抽 3 块）               → work/qa/back_*.json
8) lint（A 译）                      → 禁用形 0 命中（未译残留仅限合法 CLI/菜单路径）
9) qa                                → TRANSLATION-QA.md 三道门
10) 合并全译本                        → books/<code>/zh-fulltext/中文全译本-<CODE>.md
11) 备份到 10.10.10.169（§6）
```

**md 模式提示词差异**（在 COMKB HANDOFF §4 模板基础上替换锚规则）：
"正文中所有 Markdown 标题行（# 开头）是结构锚，必须逐字保留、位置对应，不得翻译标题行本身、
不得增删合并标题；块首行 `<!-- chunk ... -->` 注释原样保留。其余规则不变。"

验收门：V1 平均 ≥90（3 块回译）；锚 100%；lint 零禁用形；术语冲突清单回填
build_term_table OVERRIDES。**全部通过才进 Phase 2；任何一门不过，先修因再重跑该门。**

### Phase 2 · 批量（试点通过后）

排程（2 并发）：

| 波 | 书 | 块量(约) | 备注 |
|---|---|---|---|
| P2-1 | os-lan-troubleshooting（368K） | 62 | |
| P2-2 | stellar-wlan-enterprise-basic（284K） | 48 | |
| P2-3 | ov2500-nms-admin（601K） | 100 | |
| P2-4 | os-lan-core-switching-v2（668K） | 112 | |
| P2-0 | aos810-net-config **体量异常核查** | — | 抽样 5 处判断命令表占比；定"全文 or 只译叙述段"，重估块量后排波 |
| P2-5+ | aos810-net-config（按核查结论） | 100–620 | 单列，可拆章多波 |

- 每波流程 = Phase 1 的 3)–11) 步；波内 2 并发，跨波串行。
- 每本完成定义：A/B 译块数 = en 块数；回译抽查 ≥90；TRANSLATION-QA.md 落盘；全译本合并；已备份 169。
- 工时口径：P2-1…P2-4 约 320 块，2 并发下 3–5 个工作日墙钟；net-config 视核查结论另计。

### Phase 3 · 站点集成与部署（1–2 天）

1. `tsskb build` 增加中文阅读层渲染（D2A：书详情页"中文全文"入口/标签页）；译文从本地
   `books/<code>/zh-fulltext/` 注入，构建产物含译文但**仓库不含**。
2. 过 CI 同款质量门：`tsskb build --output dist/site --full --strict && tsskb validate --site dist/site --strict`
   （ruff/mypy/pytest 不受影响，不新增依赖更佳）。
3. 部署 8899：走 src/tsskb/deploy 既有机制（TSSKB_DEPLOY_* 环境变量），10.10.10.169 局域网直连，
   VPN 侧 10.20.30.103:8899 同站。
4. 可选并行包：现有中文蒸馏页（368 张卡）保真审计——V1 回译抽查 + V2 术语 lint，出体检报告按需修复。

## 4. 版权防线（D1A 落地）

- `.gitignore`（已提交）：`**/zh-fulltext/`、`**/中文全译本*.md`、`*.handoff.zip`。
- 译文唯一权威副本 = 执行机本地；**每日收工备份到 10.10.10.169**（§6）。
- 若未来要译文入库：先把仓库转 Private，再改防线——这是新的决策，默认不发生。

## 5. 红线（违反=返工）

1. 标题锚/PAGE 锚序列与源文 100% 一致；标题行不翻译。
2. 事实零改动：数字、IP、口令、型号、版本、命令、菜单路径原样保留；源文笔误照抄并备案。
3. 术语主译名必须采用；旧译禁用；保留英文清单内缩写不译；语境冲突按 COMKB HANDOFF 规则 8
   取舍并汇报，重复冲突回填 OVERRIDES。
4. 只译不评、不为空、不漏段。
5. 译文/源文不进公开仓库；不动 books/ 既有蒸馏产物与 src/tsskb 构建逻辑（阅读层渲染除外）。

## 6. 备份规程（到 10.10.10.169）

- 频率：每个工作波次收工时 + 每本完成时。
- 内容：`books/<code>/zh-fulltext/` 整目录 + `TRANSLATION-QA.md` + `translation_tools/term_table.yaml`。
- 方式（凭据线下提供，替换 <user>；不写密码进任何脚本仓库）：

```bash
rsync -avz books/<code>/zh-fulltext/ <user>@10.10.10.169:/home/<user>/tsskb-zh-backup/<code>/zh-fulltext/
# Windows 无 rsync 时用 scp -r 或 tar over ssh，等效即可
```

- 恢复演练：每完成 3 本书做一次"从备份恢复到干净目录"的演练，确保备份可用。

## 7. 验收总表

| 里程碑 | 验收标准 |
|---|---|
| Phase 0 完成 | status 脚本运行；md 切分 check PASS；term_table v3 生成且试点注入零冲突 |
| 试点完成 | §3 Phase 1 验收门全过；全译本合并；已备份 |
| 每本书完成 | 块数对账 + 三道门 + 备份（§3 Phase 2 完成定义） |
| Phase 3 完成 | 质量门绿灯；8899 书详情页可见"中文全文"入口；线上抽 3 页渲染正常 |
| 项目完成 | 六本书全过验收；备份恢复演练通过；CORPUS-PLAN 更新下一批建议 |
