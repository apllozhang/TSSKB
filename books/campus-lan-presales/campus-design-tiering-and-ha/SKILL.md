---
name: campus-design-tiering-and-ha
description: 拿到客户平面图/需求清单后，先定两层/三层架构与拓扑形态，再横比六种高可用方案定位技术选型。
source_book: DT00XPS281EN Campus LAN Presales
---

# 园区网分层设计法与高可用方案横比

## R · 原文引用

> "LAN OMNISWITCH HIERARCHICAL LAYERING DESIGN APPROACH — Network Topology: Shared / Ring / Star / Tree / Spine & Leaf / POD / Mesh; Network Architecture: Access–Aggregation–Core, 2-tier, 3-tier" (p288)

> "TWO-TIER MODEL: High-throughput • High Density • Lowest-Latency • Faultless with low and predictable latency • 1.5 to 6µs • Access and distribution layers merging. THREE-TIER MODEL: Scalable Segmentation • Low-latency (>12µs)" (p289-291)

> "HIGH AVAILABILITY DESIGN SUMMARY — Redundancy solution ACTIVE-ACTIVE L2: VIRTUAL CHASSIS (VC) preferred — Link redundancy / 100% Bandwidth / Switch redundancy / Unified Management / Unified L2/L3. STP: 50% Bandwidth … DHL Active-Active: 100% Bandwidth … ERP: Scalability … SPB: 100% Links UP / Traffic isolation" (p129)

## I · 方法论骨架

设计流程第一刀是二维定位法：**架构轴**（2-tier vs 3-tier）× **拓扑轴**（Star/Tree/Ring/Mesh/Spine-Leaf/POD），两轴交点即架构草图。

| 维度 | 两层（接入+核心） | 三层（接入+汇聚+核心） |
|---|---|---|
| 时延 | 1.5-6µs，无阻塞 | >12µs |
| 速率路径 | 接入 100M-10G；上联/核心 10G→50G→100G | 接入 100M-10G；汇聚 1G→25G；核心 10G→100G |
| 适合 | 高吞吐高密度、管理点少、接入汇聚合并 | 可扩展分段、中等密度、多楼宇 |

高可用六方案横比（同一坐标系）：

| 方案 | 带宽利用率 | 交换机冗余 | 统一管理 | 定位 |
|---|---|---|---|---|
| **VC（官方 preferred）** | 100% | 有 | 有 | L2 主主首选 |
| STP | 50% | 无 | 无 | 兜底 |
| LACP | 100% | 无 | 无 | 纯链路聚合 |
| DHL Active-Active | 100% | 有 | 无 | 接入双归（不堆叠也能双活） |
| ERP 环网 | 100% | 有 | 无 | 环拓扑可扩展 |
| SPB | 100% 全链路 UP | — | 无 | 核心层方案，流量隔离 |

## A1 · 书中案例

c07（p307）：校园网两层/三层选型总图——两层网边缘 OS6360/6465/6560-E 千兆 PoE 接入 + OS6860N/6870 VC 或 DHL 直连核心；三层网 OS6560/E 做汇聚、OS6900/6870/9900 做核心，骨干 10/40G，并按端口速率与供电等级逐层标注机型。

## A2 · 触发场景（含与相邻 skill 的区分）

- 触发：客户给平面图/需求清单，要求 15 分钟出架构草图；或客户提出可靠性指标（收敛时间、双活）问选哪种冗余技术。
- 区分：本 skill 只回答"架构形态 + 冗余技术路线"两问；**具体选哪台机型**走 `omniswitch-model-selection`；**落成可投标的架构模板**（紧凑核心/环网/密集核心等）走 `campus-reference-architectures`；环网技术细节走 `dhl-erp-ring-protection`。

## E · 可执行步骤

1. 过需求十维自检（可扩展/可靠/成本/可管理/易实施/排障等，p287），问客户"最在乎哪三条"。
2. 判层数：单楼宇或要求最低时延→两层；多楼宇、分段扩展→三层。
3. 选拓扑：光纤星型→Star/Mesh；光纤环形→Ring（ERP）；数据中心→Spine-Leaf/POD。
4. 按上表定冗余技术：L2 双活默认推 VC；客户拒绝堆叠则 DHL；环资源则 ERP；多租户核心则 SPB。
5. 产出：一张架构草图 + 一句话技术路线（"两层 + VC + DHL 接入"这类），交机型选型 skill 续作。

## B · 边界与陷阱

- "最低时延 1.5-6µs"是两层模型的理论量级，实际还受链路与机型影响，投标写 SLA 前实测。
- SPB 收敛约 300ms，达不到电信级 50ms（时敏场景用 ERPv2，见 dhl-erp-ring-protection skill 的 ce07）。
- 各方案对比表是 Ed29 口径，版本迭代后以最新 release notes 复核。

---
来源条目: f02, f06, p22, p43, c07
