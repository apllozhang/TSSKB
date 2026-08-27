---
name: ALE Golden RFP 使用指南（C/PC/NC 分级/应标口径/文档覆盖地图）
description: 写标书、响应 RFx 招标、或评审供应商投标响应时使用：ALE Golden RFP 系列的 C/PC/NC（Compliant / Partially Compliant / Non-Compliant）应答机制、空白与"见数据表"视为不满足的评判规则、"C 必须附证据"的举证口径、各 Golden RFP 文档的覆盖范围与版本对应关系。
source_book: ALE Golden RFP 系列（8 份源文档）
---

## R（何时用）
- 客户发来招标书 / RFx，需要把 ALE 产品能力逐条映射成投标响应
- 写标书前要选对"母本"——该抄哪份 Golden RFP、版本是否匹配客户引用的产品版本
- 评标时核对厂商响应表：哪些答法会被判无效
- 售前要给客户解释"Golden RFP 是什么、怎么用"

## I（核心理念）
Golden RFP 的本质是一份"预写好的需求答案库"：ALE 把自家产品的可应答需求条目整理成标准矩阵，售前直接照条目和参数搬进标书，评委按同一口径核对。所有机型类文档的格式是"需求条目 + C/PC/NC 三级勾选列"（grfp-2260 全文每条都带 C/PC/NC 列）；软件特性类是"Section 分域 + 编号条目 + Pass C/PC/NC"（grfp-sw-features 每个机型一张表）。分级含义以 AI-DC 文档定义最完整（sources/grfp-aidc.md Introduction）：C = Compliant 完全满足；PC = Partially Compliant 部分满足且必须描述差距；NC = Non-Compliant 不满足。

三条硬规则决定了整个体系的严肃性：
1. **必答**："The bidder must answer every requirement"（aidc，Introduction 后）——一条都不许空。
2. **空白即出局**："A blank cell, a dash, or 'see datasheet' will be treated as Non-Compliant"（aidc，Introduction 后）。填表时"详见数据手册"等于自认不满足。
3. **C 要举证**："must provide the public datasheet, release-notes reference, or test report that substantiates each 'C' answer"（aidc，同段）——每个 C 都要有公开数据表、版本说明或测试报告背书。

## A1（决策要点）
1. **选文档**：客户问整机硬指标（端口/PoE/温度/MTBF）→ 机型类 Golden RFP；问软件功能清单 → grfp-sw-features 按机型找 Section；AI 数据中心项目 → aidc；无线 → wlan；网管平台 → ovng。
2. **选版本**：Golden RFP 有版本对应关系，引用时要与客户标的的 AOS/固件版本一致。对应关系：6360/6465 基于 AOS 8.10R4；sw-features 为 OMNISWITCH GOLDEN RFP - 8.10R4 总表；ovng 10.5.2 对应 OVCX/OVTX 10.5.2；wlan 6.0.2 对应 AWOS 5.0.5 + OVCX/OVTX 10.6.1 + OVE 4.9R3；2260/2360 用独立版本号 V5.1；aidc v1（2026-05）基于 AI-DC Offer Phase 2。
3. **评判口径**：自己写标书时标 C 必须能在公开资料里找到依据，宁可标 PC 并写清差距，也不要虚标 C 被评标澄清打回。
4. **逐条必答**：哪怕整节不适用也要逐行给结论，不留空格、不给横线。

## A2（细节速查表）

| 文档 | 定位 | 版本锚点 | 来源文件 |
|---|---|---|---|
| OS6360 Golden RFP | 接入堆叠千兆机型 | AOS 8.10R4 | sources/grfp-6360.md |
| OS6465 Golden RFP | 工业加固无风扇机型（DIN 导轨/-40~75°C/MACsec） | Version 8.10R4 | sources/grfp-6465.md |
| OS2260 Golden RFP | WebSmart 轻管理接入（V5.1，英文版） | V5.1 | sources/grfp-2260.md |
| OS2360 Golden RFP | SME 可堆叠接入（法文版！） | V5.1 | sources/grfp-2360.md |
| OmniSwitch SW features | 12 个机型族 × 功能域需求总矩阵（97 页） | AOS 8.10R4 | sources/grfp-sw-features.md |
| AI-DC Golden RFP | GPU 集群后端无损以太网 + 前端 EVPN-VXLAN 全套 | v1 (2026-05, Phase 2) | sources/grfp-aidc.md |
| Stellar WLAN Golden RFP | AP Type A-Q2 共 22 类 + 管理/RF 通用需求 | 6.0.2 (2026-08) | sources/grfp-wlan.md |
| OmniVista NMS 10.5 Golden RFP | SaaS 网管平台 72 条编号需求 | 10.5.2 (2026-01) | sources/grfp-ovng.md |

sw-features 总表覆盖机型族（按文中出现顺序）：OS6360 / OS6465 / OS6560 / OS6570M / OS6575 / OS6860N / OS6865 / OS6870 / OS6900-V72/C32 / OS6920 / OS9900。每个机型的 Section 编号体系一致（1 Management、2 Resiliency、3 Layer 2、4 IPv4、5 IPv6、6 QoS、7 Multicast、8 Multi-technology fabric、9 Service technologies、10 Security、11 Security framework、12 Timing、15 Network performance、16 PoE、17 Metro Ethernet、18 Monitoring/Troubleshooting、19 Data Center（仅 6920）、20 SDN、21 Certifications），低阶机型没有的域直接缺席（如 6360 无 Section 8/9/17）。

## E（场景案例/怎么用）
- 场景一：标书要求"提供全系列交换机的 PoE 能力矩阵"。做法：从 lan-access 单元拿 2260/2360/6360/6465 的 PoE budget 行，从 sw-features 各机型 Section 16 拿 Perpetual/Fast PoE 条目，合成一张带出处页码的对比表，全部标 C 并附 8.10R4 数据表链接。
- 场景二：评标发现某竞品响应表里写 "see datasheet"。按 aidc Introduction 规则可直接提质疑：视同 NC。
- 场景三：客户写的是 AOS 8.10R2。此时不能直接抄 8.10R4 版 Golden RFP 答 C，需先确认特性在 8.10R2 已交付，否则标 PC。

## B(限制与坑)
- **2360 是法文版**（文件名 omniswitch-2360-golden-rfp-fr），"Le commutateur doit prendre en charge les éléments suivants" 就是"The switch must support the following"；搬进中文/英文标书时需自行翻译并复核数字（如逗号小数点习惯："68,4 Mpps" 即 68.4 Mpps）。个别地方保留英文（PoE perpétuel et rapide = Perpetual and Fast PoE）。
- **wlan 版本时效最强**：AP 型号随 WiFi 代际快速更替（Type D AP1411 已标注 Planned phase-out in 2026；Type A 在美国不可售）。引用 AP 具体型号前先核可用性脚注。
- **ovng 明确不含 Stellar WLAN 特性**（Scope 一节原文声明），也别把它的 NAC 条目当独占能力——Guest Access 另有专门 Golden RFP。
- **C/PC/NC 不是评分等级**，是符合性声明；评级高低的应该是招标方自己的打分模型，别混淆。
- sw-features 提取文本有 OCR 断词（如 "Bloetooth"、"108bGbps"、"Pv6"），引用英文原句时先修正。

来源：ALE Golden RFP 系列 8 份文档的 Introduction / Scope / Gold Rules 相关章节（sources/*.md 开头部分）
