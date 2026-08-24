---
name: spb-license-spec-sizing
description: 报价选型阶段核对 SPB 许可成本、机型容量上限（BVLAN/I-SID/SAP/IS-IS 邻接）与 OmniFabric 三技术支持矩阵时使用。
source_book: DT00XPS279EN SPB Presales
---

# SPB 许可与机型规格 Sizing 手册

## R · 原文引用

> "AOS support: OS6860E, OS6860N, OS6870, OS6865, OS6900, OS9900. No license."（p22）

> "Maximum number of BVLANs: 16 (4 is recommended). Maximum number of IS-IS adjacencies: 70 / 128. Maximum number of I-SIDs: 2K / 8K / 1K. Maximum number of SAPs: 2K / 8K. Please refer to latest « AOS Specifications Guide » for up-to-date figures."（p75）

> "OmniSwitch 6900: SPB P, VxLAN P/P, MPLS P. OmniSwitch 6870: SPB P, VxLAN P/P*, MPLS O**. * Supported starting with 8.10 R3/R4. ** HW ready."（p139）

## I · 方法论骨架

**① 许可规则（p02）**：SPB 在 AOS 上 **No license**（零许可成本），全系主流机型支持——报价时可直说无额外软件授权费。

**② 容量规格矩阵（p24/c13，按机型）**

| 指标 | OS6860/6860N/6865 | OS6900 多数子型 | OS6900 X/T24C2 | OS9900 |
|---|---|---|---|---|
| BVLAN | 16（推荐 4） | 16 | 16 | 16 |
| IS-IS 邻接/接口 | 70 | 128 | 128 | 128 |
| I-SID | 2K | 8K | 2K | **1K** |
| SAP | 2K | 8K | 8K | 8K |
| 每 I-SID VLAN/SVLAN | 2K | 4K | 4K | 4K |

ECT 算法 ID 16 个（1-16 任选分配给 BVLAN）。

**③ OmniFabric 技术支持矩阵（c14，P/O 标记）**：核对每机型 SPB / VxLAN-VxLAN EVPN / MPLS 三项支持等级——OS6900 三项全 P；OS6860N、OS6900 的 MPLS 为 P；6870 与 9900 的 VxLAN EVPN 自 8.10 R3/R4 起平台支持（P*）；6860E 的 VxLAN/MPLS 为 O；6570M SPB 为 O（HW ready，O**）。

**④ 时效纪律（ce16）**：所有数字是 2025-02 Issue 05（AOS R8 时代）快照，p75 自带"以最新 AOS Specifications Guide 为准"免责声明。

## A1 · 书中案例

p75 规格表覆盖六族机型，是报价前 sizing 的硬指标来源；p139 矩阵脚注（*/8.10 R3/R4、**/HW ready）演示了如何读版本依赖；L3 能力行（IP over SPBM：VPN-Lite/L3 VPN、VRF-to-ISID 映射）与三形态机型清单联动（见 L3 集成 skill）。

## A2 · 触发场景

- BoM/报价阶段：核对机型容量是否满足设计（mesh 度、服务数、接入数）；
- 答复"SPB 要不要买许可"；
- 混合织物方案核对机型三技术支持组合。
与相邻 skill 区分：三技术整体选型逻辑走 `spb-vs-evpn-mpls-selection`；本 skill 只管"这台机器到底支持多少、要不要钱"。

## E · 可执行步骤

1. 设计参数四项对表：节点 mesh 度 vs IS-IS 邻接上限（70/128）、业务总数 vs I-SID 上限（1K-8K）、接入点数 vs SAP 上限、路径分担数 vs BVLAN 16/推荐 4。
2. 混合方案逐型号查 OmniFabric 矩阵，标出版本依赖脚注（8.10 R3/R4、HW ready）。
3. 报价页写明 SPB 零许可，并在方案脚注声明"规格以最新 AOS Specifications Guide 为准"。

## B · 边界与陷阱

- **邻接数档位按机型分布**（ce08）：全 mesh 核心只算带宽不算控制面会邻接建不满；OS9900 的 I-SID 反而只有 1K，高端不等于每项都高。
- **细分列对应存疑**（verified.md 遗留项）：p75 表中 IS-IS 邻接 70/128 按机型（OS6860N 归哪档）在 PDF 文本流中无法精确判定，按型号引用细分数字前必须对原书表格核对。
- **数字时效**（ce16）：教材自带免责声明，下单与投标前一律用最新 AOS 规格书复核；p139 的 P/O 图例书中未定义（推测 P=平台级、O=可选/需授权），引用需核实。
- p75 的"IP over SPBM"行只标 IPv4，IPv6 支持范围待确认（见 L3 集成 skill 的 ce07）。

---
来源条目: p02, p24, c13, c14, ce08, ce16
