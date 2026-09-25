# TSSKB 翻译提升工作安排（方法论移植）

> 制定：2026-09-25。执行者：任一能克隆本仓库的 AI/工程师（机器无关，已在 COMKB 线验证可移植性）。
> 方法论出处：COMKB 通信线 25 本翻译实践（对齐 deusyu/translate-book 架构），要点：
> **分块锚定 + 术语硬约束 + 低并发幂等并行 + 三道门 QA（V1 回译忠实度 / V2 术语 lint / V3 双译比对）+ 事实零改动**。
> 门户：8899（VPN 10.20.30.103:8899 ≡ 局域网 10.10.10.169:8899）。

## 0. 起点盘点（评估结论，2026-09-25 已核实）

| 项 | 状态 |
|---|---|
| 英文源文 | 60 份 fulltext.md 已在本仓库（books/*/fulltext.md 或 source/fulltext.md，91K–1045K） |
| 术语原料 | 116 份 GLOSSARY.md（每书一份 + candidates/glossary.md）——术语表工作从"聚合"降级为"规范化" |
| 蒸馏产物 | 368 张 SKILL.md 能力卡（页面已是中文） |
| 构建系统 | `tsskb build/validate/metrics`，CI quality-gate（ruff/mypy/pytest/strict 构建） |
| 部署 | src/tsskb/deploy，凭据走 TSSKB_DEPLOY_KEY / TSSKB_DEPLOY_PASSWORD 环境变量（无明文，保持） |
| 流水线脚本 | 在姊妹仓库 apllozhang/COMKB 的 pipeline/（translate_pipeline.py 等，已可移植化）——**任务 T0 复制进本仓库** |

**语料三档取舍**（决定翻什么，不做全文一刀切）：

| 档 | 典型书 | 处置 |
|---|---|---|
| 操作手册型 | os-lan-*、aos810-*、ov2500-*、stellar-wlan-*、smb-*、ov-terra-deploy | **全文中文阅读层**（本计划主体，约 20–25 本） |
| 数据表/彩页型 | bp-*（datasheets）、hw-*（硬件书，图为主） | 不翻译；hw-* 可只译 Overview/Digest 叙述段 |
| 售前叙事型 | dan、dan-cases、golden-rfp、*presales | 不做全文翻译；现有中文页做保真审计（可选并行包） |

例外：aos810-cli-reference 全是命令，只译章节导语与说明段。

## 1. 决策点（开工前需确认，D1 必须先拍板）

- **D1 版权口径**：本仓库为 PUBLIC 且已含 60 份英文全文（既有状态）。**中文全文译文默认不入本仓库**——
  译文写本地/私有层（与 COMKB 交接包同口径），站点构建时从本地注入。若要译文入库，先把仓库转 Private。
- D2 阅读层形态：书详情页加"中文全文"入口，还是独立 `/zh/` 板块？（Phase 3 前定，建议前者，改动小）
- D3 首批书目：建议第一批 = os-lan-vxlan-evpn、os-lan-core-switching-v2、os-lan-troubleshooting、
  ov2500-nms-admin、stellar-wlan-enterprise-basic、aos810-net-config（覆盖交换/无线/网管三域验证术语表）。

## 2. 阶段安排

### Phase 0 · 准备（约 1 天，纯确定性工作）

| # | 任务 | 验收 |
|---|---|---|
| T0 | 从 COMKB pipeline/ 复制 translate_pipeline.py、build_term_table.py、term_table.yaml、translation_status.py 到本仓库 `translation_tools/`；适配目录差异（输入 fulltext.md 而非 source_fulltext.txt，位置两种：`books/<code>/fulltext.md` 与 `books/<code>/source/fulltext.md`） | 对任一书能产出 work/en 块与 manifest |
| T1 | 切分器增加 **md 模式**：按 H1/H2 标题切块（约 6000 字符），标题行即锚（保真锚 = 标题文本+顺序），manifest 记锚序列+SHA256；PAGE 锚模式保留 | 试点书锚序列 100% 对齐 |
| T2 | 术语表 v3（网络域）：聚合 116 份 GLOSSARY.md → 共识升全局 / 按书作用域；新增网络域 curated 与**保留英文缩写清单**（OSPF、VLAN、LACP、STP/RSTP、SPB、VXLAN、EVPN、MPLS、ISIS、BGP、VRRP、MC-LAG、QoS、ACL、MACsec、TCAM、ISSU、DDM、PoE、LLDP 等——约 80–100 条）；与通信域 term_table 合并为公司级表（域作用域隔离，gateway/trunk 等跨域词统一） | term_table v3 生成；试点书 terms 注入零冲突 |
| T3 | 语料分档清单落成 `translation_tools/CORPUS-PLAN.md`（翻译书单+顺序+跳过理由） | 清单评审通过 |

### Phase 1 · 试点（约 1 天）

os-lan-vxlan-evpn（250K，技术密度最高，最能验证术语表）走全流程：

```
chunk(md 模式) → terms → A 译(直译打底) → check → B 译(意译对照) → lint → compare → 回译抽查 → qa → 合并全译本
```

验收门：V1 ≥90（抽 3 块回译）；锚序列 100%；lint 零禁用形命中（未译残留仅限合法保留的
CLI/菜单路径）；A/B 分歧清单产出并人工终审标记。**试点通过才进 Phase 2。**

### Phase 2 · 批量（约 2–3 天 agent 时间）

- 操作手册型书按 fulltext 大小排序分波，**每波 4 本**；每本 25–40 块，A 译/B 译/回译抽查三波子代理。
- 并发纪律：**3–4 并发起步，禁止高并发**（实测撞限流/验证码超时整批报废）；块文件幂等，
  失败组单独重试，`translation_status.py` 对账续跑。
- 每本完成定义：A/B 译块数 = en 块数；back_*.json 平均分 ≥90；TRANSLATION-QA.md 三道门落盘；
  合并全译本产出。
- 提示词模板、红线、故障处理：见 COMKB 仓库 HANDOFF.md §4–§5（本计划不重复，以那边为准）。

### Phase 3 · 站点集成与部署（1–2 天）

1. `tsskb build` 增加中文阅读层渲染（按 D2 决策）；译文从本地/私有层注入，不进 git。
2. 过 CI 同款质量门：`tsskb build --output dist/site --full --strict && tsskb validate --site dist/site --strict`。
3. 部署到 8899：走 src/tsskb/deploy 既有机制（TSSKB_DEPLOY_* 环境变量）；10.10.10.169 局域网直连，
   VPN 侧为 10.20.30.103:8899。
4. 可选并行包（不翻译也能提质）：**现有中文蒸馏页保真审计**——V1 回译抽查（中文页回译对照英文源文）
   + V2 术语 lint，产出体检报告，按需修复。

### Phase 4 · 沉淀

- 网络域术语表随试点/批量反馈迭代（OVERRIDES 机制，禁改 yaml 手改）。
- 通信+网络两域术语表合并为公司级表，跨域词（gateway、trunk、license 等）口径统一。
- dt00xte215en（8900 侧"待归类"的 OmniSwitch 教材）归属网络线，翻译直接复用本线产物。

## 3. 红线（违反=返工）

1. 锚保真：md 切块的标题锚序列必须与源文一致（PAGE 锚模式同）。
2. 事实零改动：数字、IP、口令、型号、版本、命令、菜单路径原样保留；源文笔误照抄并备案。
3. 术语主译名必须采用；旧译禁用；保留英文清单内缩写不译。
4. 只译不评、不为空、不漏段。
5. **译文与源文不入公开仓库**（.gitignore 拦截 + 译文走本地/私有层，见 D1）。
6. 不动 books/ 下既有蒸馏产物与 src/tsskb 构建逻辑（阅读层渲染除外）。
