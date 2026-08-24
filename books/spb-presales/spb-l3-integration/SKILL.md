---
name: spb-l3-integration
description: 做 L3 over SPB 方案选型（Outline/前面板 inline/单遍 inline 三形态 × VPN-Lite/L3 VPN 两机制）或写 AOS 路由集成配置时使用。
source_book: DT00XPS279EN SPB Presales
---

# SPB 三层集成选型与配置（三种形态 × 两档路由机制）

## R · 原文引用

> "Outline routing: use of two physical loopback ports. One side as an access port for SPB, other side is a bridged port configured for routing only. AOS support: OS6900-X20/X72/T20/Q32, OS6860/E."（p82）

> "VLAN ports support all standard features — Preferred method for L3 VPN designs. SAP Ports are locally limited in support of edge features such as port-QoS, LPS, DHCP Snooping, STP etc."（p83）

> "VPN Lite: Routing L3 traffic over a L2 SPBM backbone network. Run routing protocols on L3VPN IP interfaces. SPB acts more like a physical media."（p85）

> "Service based inline routing: No physical loopback cable required, No dedicated front-panel ports. IP service-based interface configured through software for single-pass in-line routing... Both an IPv4 and IPv6 interface can be assigned to the same SPB service as long as both are in the same VRF instance."（p95）

## I · 方法论骨架

两步选型：**先选物理形态（f14），再选路由机制（f15）**。

**① 物理形态三选一（f14/p26/p29/p30）**

| 形态 | 端口代价 | 支持机型 | 备注 |
|---|---|---|---|
| Outline 物理环回线 | 消耗两个物理口+线缆 | OS6900-X20/X72/T20/Q32、OS6860/E（最广） | 通用兜底；端点终结在 VLAN UNI 是 L3 VPN 首选（p27） |
| 前面板口 inline | 占前面板口（软件 loopback 模式，带宽取自该口） | **仅 OS6900-V72 / C32** | 免外部线缆 |
| Service-based 单遍 inline | 零端口，纯软件 | OS6860N/6870/6900-X,T 系列/OS9900（最广的新方案） | IP 接口直接绑 SPB service |

**② 路由机制两档（f15）**

| | VPN-Lite（简版） | L3 VPN（全版） |
|---|---|---|
| 原理 | SPB 当物理媒介，VRF 间跑静态/OSPF（VRRP 可冗余） | 路由经 IS-IS SPB TLV 直接跨骨干分发，ISID-per-VRF |
| 适用 | 客户会 OSPF、规模小、要简单 | MPLS 式自动路由分发、多 VRF 大规模 |

**③ VPN-Lite 六条守则（p28/ce11）**：每 VRF 环回路由侧单 IP 接口绑专用 VLAN（他口不用）；一 VRF 可多 IP 接口对应多 I-SID，但**两 VRF 不得共享同一 I-SID**；对侧 SAP 用同 VLAN 号绑同 I-SID；VRRP 可按接口配（hello 穿 PBB）；可全静态路由。硬件约束：IPv4/IPv6 同绑一 SPB 业务须同一 VRF 实例（p30）。

**④ 配置模板（c04-c07）**
- Outline：`vlan 500` + `spb bvlan 4001` + `service spb 10 isid 1000` + `service spb 10 sap port 1/1/24:500` + `vrf 1 ip interface L3vpn1 vlan 500 address 10.5.1.1/24`。
- VPN-Lite 路由：`vrf 1 ip static-route 192.168.3.0/24 gateway 10.5.1.2` 或 `vrf 1 ip load ospf` + area 0.0.0.0。
- 前面板 inline：`interfaces port 1/1/18 loopback` + `ip interface L3vpn1 ... rtr-port port 1/1/18 tagged vlan 200`。
- Service-based inline（最简）：`vrf 1 ip interface L3vpn1 address 10.5.1.1/24 service 10`。
- L3 VPN 增量：`spb ipvpn bind vrf 1 isid 1000 gateway 10.5.1.1 all-routes` + `vrf 1 ip export/import ... all-routes`。

## A1 · 书中案例

p84/87/93-94/96-97 四套 CLI 样例构成完整配置手册：ISID-1000 承载、两 BEB（10.5.1.1/10.5.1.2）、VRF 1 内 192.168.x.0/24 网段互通；同一形态上 VPN-Lite 与 L3 VPN 只差 bind/export/import 三行。

## A2 · 触发场景

- 标书需要"L3 over SPB"技术方案章节：选形态（按机型与端口预算）+ 选机制（按客户技能与规模）；
- 写或审 AOS 三层集成配置（直接套四套模板）；
- 客户问"BEB 能不能同时当桥和路由器"（能——消灭独立路由层的论证）。
与相邻 skill 区分：选 EVPN 还是 SPB 做整体织物走 `spb-vs-evpn-mpls-selection`；机型规格总表走 `spb-license-spec-sizing`。

## E · 可执行步骤

1. 按机型矩阵定形态：核对客户 BoM 机型在 p82/92/95 三张清单的归属（投资前逐型号核对，含 IPv6 支持待确认项）。
2. 按团队画像定机制：客户熟悉 OSPF/静态路由且 VRF 少 → VPN-Lite；要多 VRF 大规模自动分发 → L3 VPN。
3. 建三列对照表（VRF–VLAN–I-SID）做配置前校验，套用对应 CLI 模板，L3 VPN 追加 bind/export/import 三行。

## B · 边界与陷阱

- **SAP 口边缘特性受限**（ce01）：终结在 SPB SAP UNI 时 port-QoS/LPS/DHCP Snooping/STP 支持有限，部署后期才发现会返工；首选 VLAN UNI 设计（"VLAN ports support all standard features"）。
- **机型矩阵不齐**（ce07）：前面板 inline 仅 OS6900-V72/C32；service-based inline 仅 p95 清单型号；老/低端机只能 Outline 还要搭物理端口。p75 规格表只标 IPv4，IPv6 支持范围引用前必须核对最新 AOS 规格书。
- **VPN-Lite 铁律**（ce11）：两 VRF 共享 I-SID、loopback VLAN 复用 → 路由串线、故障极难定位；一律用三列对照表预防。

---
来源条目: f14, f15, p26, p27, p28, p29, p30, c04, c05, c06, c07, ce01, ce07, ce11, g14, g17, g19, g25, g38, g39
