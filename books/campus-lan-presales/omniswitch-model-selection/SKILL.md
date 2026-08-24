---
name: omniswitch-model-selection
description: 从层级定位表、功能矩阵、产品组合定位图三张表筛机型，并查容量/PoE 常数与 VC vs 机箱对比定案。
source_book: DT00XPS281EN Campus LAN Presales
---

# OmniSwitch 机型选型决策表与容量常数库

## R · 原文引用

> "OMNISWITCH SELECTION NETWORK LAYER BASED — Model Layer: OS6360 OS6465 OS6560/E OS6570M OS6575 OS6860N OS6870 OS6900 OS9900. User Access: Yes Yes Yes Yes Yes Yes Yes No Yes; Distribution: No No Yes Yes Yes Yes Yes Yes Yes; Core: No No No No No Yes Yes Yes Yes" (p300)

> "OMNISWITCH SELECTION FOR CAMPUS DESIGN — Availability: Virtual Chassis / ISSU / Hot swap power supply; Layer 2: SPB / DHL Active-Active / ERPv2; Layer 3: Basic / Advanced / VRF / Multicast; User network Profile / Fanless / Metro Ethernet / MPLS / Remote VC. ** License based feature" (p301)

> "POSITIONING IN THE STACKABLE PORTFOLIO — Gig / Small / Gig w/ 10G / Hardened / Large: OmniSwitch 2260/2360 Value AOS L2 WebSmart; 6360 Value AOS L2+ GE; 6560/E AOS Advanced L3 licensed; 6570M AOS L3+ Metro Ethernet; 6860N Advanced AOS L3 GE; 6870 AOS Advanced L3" (p357)

## I · 方法论骨架

选型三张表 + 常数库，按序使用：

**表 1 · 层级定位（Yes/No 铁律，p300）**

| 机型 | 用户接入 | 汇聚 | 核心/DC |
|---|---|---|---|
| OS6360 / OS6465 | Yes | No | No |
| OS6560/E / OS6570M / OS6575 | Yes | Yes | No |
| OS6860N / OS6870 | Yes | Yes | Yes |
| OS6900 | **No** | Yes | Yes |
| OS9900 | Yes（配 GNI 板） | Yes | Yes |

**表 2 · 功能矩阵要点（p301，** = 需 license）**：VC 除 OS2260 外全系；ISSU 仅 6360-24/48 及以上（2260/2360/6465/6560E 无）；SPB 从 6560/E（**）起步；MPLS 仅 6860N/6870/6900（**）；热插拔电源从 6360-24/48 起。DHL 行 6570M/6900/9900 标 No（与 p54 矛盾，需注版）。

**表 3 · 组合定位（p357）**：小型便宜→2260/2360/6360；多千兆 Wi-Fi→6560E/6860N；Metro→6570M；高规格→6870；加固→6465/6865/6575。

**容量常数（选型背参数）**

| 机型 | 转发 Mpps | 容量 | MAC 表 | 路由表 |
|---|---|---|---|---|
| OS6360 | 208 | 140G | 16K | 64 |
| OS6465 | 131 | 176G | 16K | 32 |
| OS6560E | 241 | 324G | 16K | 2K |
| OS6570M | 210 | 60/168G | 32K | 16K |
| OS6860N | 758.9 | 1.02T | 64K | 144K |
| OS6870 | 1488 | 2T | 128K | 312K |
| OS6900 | 2000 | 6.4T | 228K | 128K |
| OS9900 | 15118/30950 | 25.6/51.2T | 128K | 128K |

入门对比：OS2260 无堆叠/80.4Mpps/2 条静态路由；OS2360 可堆叠/133.9Mpps/32 条/10G 上联。**两者均不在美国销售。**

**VC vs 物理机箱（6×6900 vs 9907/9912，p303）**：VC 胜初期投资（按需扩容）、6U 机架、1G/10G 各 432 口、ACL 4K；机箱胜时延（单跳）、重启仅数据面、PoE 75/30W、40/100G 密度与全冗余。

**9900 平台常数**：9907 = 7 槽/25.6Tbps/10800W PoE/11RU/双机 VC；9912 = 12 槽/51.2Tbps/7920W/17.25RU（VC 属 roadmap）。供电：AC240V 3000W、AC120V 1200W、DC 2500W；GNI-P48/XNI-P48Z16 前 8 口 75W、其余 40 口 30W。

**PoE 预算速查**：OS6360-P10 120W/P24 200W 优化/P48 390W 优化/PH24·P24X·P48X 390-780W 满配；OS6865 随电源块数与电压（48V 单块 100-140W、双块 280-300W）；6900-C32E 128×10G/128×25G/32×100G、<600ns；6920-D32 400G 级、<500ns；6870 单芯片 1.88-2Tbps、95W/口、8 台 VC 任意混搭。OS6465 PROFINET Class B 认证，但仅 VC of 1（单机）支持。

## A1 · 书中案例

c04（p303）：6×6900 VC 对比 9907/9912 的量化竞标弹药（端口数 432 vs 288/480、重启面、PoE）。c19-c25（p12-25）：各产品家族明星机型页——9900 机箱、6900/6920 固定核心、6870/6860N 多千兆双雄、6865/6575 坚固型、6570M/6465 城域与紧凑加固、6560/E 价值多千兆、6360/2260/2360 入门。

## A2 · 触发场景（含与相邻 skill 的区分）

- 触发：招标硬条款逐条映射到功能矩阵行取"全满足列"；或"这个需求报哪个家族"的快速问答。
- 区分：本 skill 管**选哪台机器**；架构怎么搭走 `campus-design-tiering-and-ha`；套模板出图走 `campus-reference-architectures`；堆叠设计细节走 `virtual-chassis-design`；带 ** 项的许可报价走 `license-wwpl-pricing`。

## E · 可执行步骤

1. 先过层级定位表：确定设备落在接入/汇聚/核心/DC 哪层，划出候选集。
2. 把招标硬条款逐条映射到功能矩阵行，取"全满足列"；带 ** 的项记下待补 license 行。
3. 按组合定位图缩小家族，用容量常数表核对 Mpps/表项/PoE 预算是否够。
4. 核心层做 VC vs 机箱对比，按预算与扩容节奏定形态。
5. 查供货分级与美国市场限制（2260/2360 不在美售），产出候选机型清单 + 风险标注。

## B · 边界与陷阱

- **教材原文矛盾（引用需注版 Ed29）**：p301 矩阵 9900 MPLS 标 No，p443/444 写 9907/9912 "MACsec, 1588v2 & MPLS support"（ce09）；p54 "DHL 除 9900 全支持" vs p301 矩阵 6900/9900 均 No（ce08 相关）。冲突时以最新 datasheet/release notes 为准。
- Roadmap 陷阱（ce14）：6870 的 MPLS/SPB-MS/50G、9912 的 VC 均为"硬件就绪软件未交付"，带星号特性不可承诺。
- ce08 典型错配：6360/6465 承诺 SPB、6900 放接入层、给 2260 上堆叠、给 6465/6560 承诺 ISSU。
- ce16：美国项目 BOM 屏蔽 OS2260/2360。
- 容量数据基于 Ed29 时点，投标前对最新 WWPL/datasheet。

---
来源条目: f03, f04, f05, f28, p02, p03, p04, p05, p06, p32, p33, p34, p35, p36, p37, p38, p45, c04, c19, c20, c21, c22, c23, c24, c25, ce08, ce09, ce14, ce16, g10, g19, g22, g23, g31, g32, g33
