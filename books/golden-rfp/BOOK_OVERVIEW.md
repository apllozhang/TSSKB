# Golden RFP — ALE 售前投标弹药库

把 ALE（Alcatel-Lucent Enterprise）的 8 份 "Golden RFP" 标准化需求清单文档蒸馏成中文课程：写标书时直接抄需求条目与响应口径。

## 源文档一览

| 来源文件 | 文档 | 定位 | 版本锚点 |
|---|---|---|---|
| sources/grfp-sw-features.md | OMNISWITCH GOLDEN RFP - 8.10R4 | 全系交换机软件特性需求总矩阵，97 页，12 个机型族 × 21 个功能域（Section），每机型一张 C/PC/NC 表 | AOS 8.10R4 |
| sources/grfp-aidc.md | AI-DC Solution Golden RFP | GPU 集群 AI 数据中心全套需求：OC8100 服务器 + 后端无损 RoCEv2 fabric + 前端 EVPN-VXLAN + 管理网 + 双 NOS + Orchestra 编排 | v1, 2026-05, Offer Phase 2 |
| sources/grfp-wlan.md | OmniAccess Stellar WLAN Golden RFP | 无线全家族：管理架构/RF/方案级共性需求 + Type A-Q2 共 22 类 AP（WiFi 5→7）逐台规格 | 6.0.2, 2026-08 (AWOS 5.0.5 / OVCX·OVTX 10.6.1) |
| sources/grfp-ovng.md | OmniVista NMS 10.5 Golden RFP | SaaS 网管平台（OVCX 云 + OVTX 本地）11 章 72 条编号需求：架构/多租户/LAN 管理/API/NAC/QoE 分析 | 10.5.2, 2026-01 |
| sources/grfp-6360.md | OmniSwitch 6360 Golden RFP | 园区接入堆叠千兆机型，10 个型号硬指标（含 Multi-Gig/10G PoE） | 基于 AOS 8.10R4 |
| sources/grfp-6465.md | OmniSwitch 6465 Golden RFP | 工业加固无风扇机型：-40~75°C、DIN 导轨、全口 MACsec、1588v2 | Version 8.10R4 |
| sources/grfp-2260.md | OmniSwitch 2260 Golden RFP | WebSmart 轻管理接入：6 型号、半宽无风扇、PoE 75–370W | V5.1 |
| sources/grfp-2360.md | OmniSwitch 2360 Golden RFP（法文版） | SME 可堆叠接入：8 型号（含 U 系列 SFP 全光口）、虚拟 chassis ≤4 台 | V5.1 |

## 单元导航

| 单元 | 一句话 | 主要来源 |
|---|---|---|
| [grfp-guide](../grfp-guide/SKILL.md) | Golden RFP 怎么用：C/PC/NC 分级机制、空白即 NC、"C 必须举证"、选文档选版本地图 | 全部 8 份的 Introduction/Scope |
| [grfp-sw-features](../grfp-sw-features/SKILL.md) | AOS 8.10R4 软件特性矩阵精粹：按域抽样 80+ 条标书条目（VC/ERPv2/UNP/SPB/VXLAN/MACsec/PoE…），附机型可用性 | grfp-sw-features |
| [grfp-aidc](../grfp-aidc/SKILL.md) | AI 数据中心需求要点：JCT 由尾延迟决定 → 五条设计铁律；GPU 服务器与 51.2T/25.6T 交换机硬指标 | grfp-aidc |
| [grfp-lan-access](../grfp-lan-access/SKILL.md) | 接入交换机硬指标对比表：2260/2360/6360/6465 的端口/PoE/功耗/温度/MTBF 抽样 | grfp-2260/2360/6360/6465 |
| [grfp-wlan](../grfp-wlan/SKILL.md) | Stellar WLAN 精粹：免控制器自组网叙事 + RF 客户端引导五连 + wIDS/wIPS 内置 + AP 分档选型 | grfp-wlan |
| [grfp-nms](../grfp-nms/SKILL.md) | OmniVista 10.5 精粹：11 章 72 条从订阅到 NAC 的应答素材，内置 RADIUS 不拆卖等话术点 | grfp-ovng |
