---
name: spb-presales-battlecard
description: 客户问"为什么换 SPB / 为什么换掉 STP"时，用瑞士军刀定位、非 IP 安全、投资保护、自动化降本四组弹药组织售前开场与答辩。
source_book: DT00XPS279EN SPB Presales
---

# SPB 售前攻防弹药库（Why SPB）

## R · 原文引用

> "IT'S AN ALL-IN-ONE SWISS-KNIFE SOLUTION — Spanning Tree replacement / Multi-tenancy / Micro-segmentation / IoT. Campus; Data Centre: intra and inter-DC fabric, any to any, fast convergence; WAN: MPLS-like L2/L3 VPN Services. One Solution — Reduce the complexity of managing multiple technologies."（p7）

> "IT'S NOT IP-BASED => IT'S MORE SECURE. x Scanning x DOS x Man-in-the-middle. Not vulnerable to IP-based attacks."（p9）

> "IT'S INTEROPERABLE AND BACKWARDS COMPATIBLE. L2: 802.1Q, Q-in-Q, LACP; L3: OSPF, IS-IS, BGP; Multicast: PIM SM/DM/BIDIR/SSM. ✓ Investment protection ✓ Phased migration ✓ No forklift upgrade."（p10）

> "Spanning Tree: a single tree, traffic always passes through the Root bridge; F to G requires five hops and it is right next to G; lots of blocked path, wasted bandwidth; hop by hop configuration; high convergence times. SPB: each switch is its own Root Bridge with symmetrical trees, controlled by IS-IS, traffic flows the shortest path, address isolation through Mac-in-Mac, no loops, fast recovery."（p23）

## I · 方法论骨架

四组弹药构成完整的售前攻防线，按客户质疑对号入座：

| 客户质疑 | 弹药组 | 核心论点 |
|---|---|---|
| "多场景要多种技术，太复杂" | 瑞士军刀定位（f01） | 一套 SPB 横跨园区/DC/WAN，四种用途（STP 替换/多租户/微分段/IoT） |
| "新协议安不安全" | 非 IP 转发论证（f02） | 核心只认 BMAC 非 IP，逐项排除 IP 扫描/DOS/中间人 |
| "现网投资会不会作废" | 互操作三承诺（f03/p04） | L2/L3/组播协议清单 → 投资保护/分阶段迁移/无需整机更换 |
| "运维成本降在哪" | 简化四支柱（f05/p03） | 自动化三件套 + edge-only 零触碰核心 + 单协议 IS-IS 管 L2+L3/IPv4+IPv6 |
| "凭什么换掉 STP" | STP 十维对比（f07） | 九条罪状 ↔ SPB 优势一一映射，F-to-G 五跳反例做实 |

可背常数（p01/p25）：**1000 节点规模、突破 4096 VLAN 限制、亚秒收敛（约 100ms）、1000 节点内全链路无阻塞**；SPB 还可跑在 VPLS/微波/VXLAN/IPVPN 之上（跨域组网卖点）。

术语支撑：AOS（三技术同一 OS 的中立根基）、SPB/SPB-M（标书互联必写区分）、Mac-in-Mac/PBB（"三个老标准组合"降心理门槛）、B-MAC（地址隔离机制）、STP（反派索引）、VC（双机核心+LACP 免 STP 接入答案）。

## A1 · 书中案例

p23 对比页是全书攻防核心：左栏列 STP 九条罪（单树绕根桥、F 到 G 相邻也要五跳、阻塞浪费带宽、逐跳配置、链路利用率低、无最短路径、广播低效、扩展性差、收敛慢），右栏 SPB 逐条对应（每台交换机自为根、IS-IS 控制、最短路径、Mac-in-Mac 地址隔离、网状拓扑、无环、快速恢复）。p76 Key Takeaway 再用弹性/安全/可管理三类归纳收尾。

## A2 · 触发场景

- 客户开场问"SPB 是什么、为什么要换"；
- 投标答辩"平滑演进 / 投资保护"章节组织话术；
- CIO/运维主管质疑安全性、迁移风险、运维成本时。
与相邻 skill 区分：与 EVPN/MPLS 的正面对比选型走 `spb-vs-evpn-mpls-selection`；具体微分段落地走 `spb-micro-segmentation`；迁移施工细节走 `spb-stp-migration-cases`。

## E · 可执行步骤

1. 开场用瑞士军刀矩阵定总命题："一个方案覆盖园区/DC/WAN，不必为每个场景引入不同织物技术"。
2. 按客户角色选弹药组：安全质疑→非 IP 论证；预算质疑→四支柱降本；投资质疑→互操作三承诺；现状是 STP→十维对比+F-to-G 五跳反例。
3. 每组弹药落到一条可背常数收尾（1000 节点 / 突破 4096 / 亚秒收敛 / ~100ms 重收敛）。

## B · 边界与陷阱

- 话术精确化：说"替换 STP"指核心骨干消除阻塞链路，接入层与 legacy 域仍可能保留 STP/DHL/LBD（详见迁移 skill 的 ce14），不可承诺"全网灭 STP"。
- ~100ms 收敛对轨交/电力等毫秒级刚需场景不占优，勿拿 SPB 硬碰（ce13 归选型 skill）。
- 规模超 1000 节点或超大型 DC 主动让位 EVPN，勿超界应标。
- 免许可、全系支持等规格数字引用前按最新 AOS 规格书复核（时效纪律见 spec skill 的 ce16）。

---
来源条目: f01, f02, f03, f05, f07, p01, p03, p04, p25, g01, g02, g21, g26, g30, g31, g32, g36
