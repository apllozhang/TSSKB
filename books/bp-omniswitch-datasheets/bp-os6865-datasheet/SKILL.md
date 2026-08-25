---
name: OmniSwitch 6865 数据表速查（工业 L3 旗舰：75W/SPB-M/-40~74°C）
description: 售前为交通/电力/视频监控等严苛工业环境选型 OS6865（加固 L3 + SPB-M VPN），核对每型 4 口 75W bt、U28X 专用 20G VC 口、双热插拔电源与 6465/6575 差异时使用。
source_book: bp-omniswitch-datasheets（DOC 11 omniswitch_6865，p99-109）
---

## R（触发场景）
- 需要 SPB-M VPN + 工业加固的 L3 组网（交通控制、电力、视频监控、室外安装）
- 每型 4 口 75W bt 供电的大功率工业设备（PTZ/室外 AP）规划
- 10 km 远程堆叠（Remote VC）与 U28X 专用 20G QSFP+ VC 口设计
- -40~74°C 宽温 + 6KV 防雷 + MIL-STD 军规/变电站认证应答

## I（核心理念）
OS6865 是"加固的进阶 L3 可扩展交换机"（<<<PAGE 99>>>："ruggedized, advanced Layer 3... offering SPB-M based VPNs"）：75W bt、1588v2、Fast/Perpetual PoE、Intelligent-Fabric 零配置开局。层级：工业加固阵营的最高档（汇聚级），下接 6465/6575。

## A1（与相邻系列选型差异）
- vs OS6465：6465 是 60W bt + 静态/RIP + VC 4 台；6865 是 75W bt + 完整动态路由/SPB-M + VC 8 台 + 双热插拔电源——要 L3/SPB VPN 组网的工业场景必选 6865（C6）。
- vs OS6575-MP16：6575 壁挂 IP67 小点位（120W 预算、无光口上联）；6865 面向机柜汇聚（U28X 20x SFP + 4x10G、280~300W）。
- vs OS6860：6860 是室内旗舰（0~45°C、95W、fabric 全家）；6865 用 75W + SPB-M 换宽温与加固。

## A2（规格细节速查表）
机型矩阵（<<<PAGE 100>>> 表 / <<<PAGE 107>>> 订购信息）：
| 型号 | RJ45 | SFP(1G) | SFP+(1G/10G) | 75W/30W 口 | 最大 PoE | 安装 |
|---|---|---|---|---|---|---|
| OS6865-P16X（/D） | 12 PoE+ | 2 | 2 | 4/8 | 300W | 半机架 2RU，DIN/壁挂/机架 |
| OS6865-U12X（/D） | 4x75W | 4+2 | 2 | 4/— | 300W | 半机架 2RU，DIN/壁挂/机架 |
| OS6865-U28X（/D） | 4x75W | 20 | 4 | 4/— | 280W | 全机架 1RU + 2x20G QSFP+ VFL |

上联与堆叠：全系 10G SFP+ 建 VC 最多 8 台（<<<PAGE 100>>>）；U28X 另有 2 个专用 20G QSFP+ VFL 口（后置）；VFL 原始容量 42/84 Gb/s（<<<PAGE 102>>>）；远程 VC 最远 10 km（<<<PAGE 103>>>）。
交换容量与包转发（<<<PAGE 101>>>）：P16X 68 Gb/s / 50.6 Mpps；U12X 60 Gb/s / 44.6 Mpps；U28X 208 Gb/s / 154.8 Mpps（raw fabric 224 Gb/s）。
电源体系：1+1 热插拔、负载分摊、可分体电源托架安装；AC+AC、AC+DC、DC+DC 任意组合（<<<PAGE 101>>>）；BP 180W AC / BP-D 180W@-36~-72V（140W@-20~-28V，<<<PAGE 102>>>）。
Layer 特性：完整 IPv4/IPv6 动态路由内置（OSPF/IS-IS/BGP/VRF + 泄漏、GRE、PIM 全家，<<<PAGE 104>>>）；SPB-M + in-band management（<<<PAGE 104>>>）；1588v2（P16X 16 口/U12X 12 口/U28X 28 口能力，<<<PAGE 101>>>）；G.8032 环保护；64K IPv4 路由、48K MAC（<<<PAGE 102>>>）；OpenFlow 1.3.1/1.0；预装完整 AOS + 高级路由软件，无许可门槛（<<<PAGE 107>>>）。
功耗/环境（<<<PAGE 101>>>）：-40~74°C（密闭无风冷时 -40~65°C）；待机 29~49.6W；6KV 铜口防雷；MTBF 单/双电源 709k~1142k 小时。
工业/联邦认证（<<<PAGE 102>>>/<<<PAGE 103>>>）：EN 50155/61373（铁路）、IEEE 1613/IEC 61850-3（变电站）、NEMA TS-2、UL 508/Class I Div 2、MIL-STD-810F/461 军规、FIPS 140-2/CC EAL2/NDcPP/JITC/TAA；DNV 船用需套件；TAA 版 TA6865-*。
规格红线：75W 口每型仅 4 个；IP30（非 6575 的 IP67）；无 MACsec/多千兆。

## E（适用场景）
- 需要 75W PoE + 10G + SPB VPN 的工业组网（对照 C6：比 6465/6575 高一档的选型终点）
- 交通控制/电力/视频监控骨干：U28X 20x SFP 全光 + 20G VC
- 变电站/铁路/军用（MIL-STD）项目认证应答
- 零配置开局大规模部署：Intelligent-Fabric 自动发现（跨厂商 SPBM/LACP 设备亦可，<<<PAGE 103>>>）

## B（限制与坑）
- 75W 口每型只有 4 个——更多高功率口要组合机型或上 6860/6870（对照 C11）
- 密闭无风冷机柜上限 65°C（非 74°C，<<<PAGE 101>>> 注 *）——密封柜设计要按 65°C 算
- IP30 防护——直接淋水/粉尘环境选 6575（IP67）
- PoE 预算 300W 上限（双电源、-40~60°C 条件下，<<<PAGE 101>>> 注 **）——大预算场景上 6860N
- U28X 无 DIN 安装（仅 19" 机架 + 专用后置安装件，<<<PAGE 108>>>）
- DNV 船用必须配电源盖套件（OS6865-DNV-HRCK/FRCK，<<<PAGE 108>>>）

来源：bp-omniswitch-datasheets DOC 11（p99-109，MPR00302457EN October 2025）；verified.md C6/C11/P19/F1/F3/F4/F5
