---
name: campus-reference-architectures
description: 按场景套用参考架构模板库：SMB 一体化/紧凑核心/分布式环网/密集核心，及城域、DC、多千兆边缘等垂直案例。
source_book: DT00XPS281EN Campus LAN Presales
---

# 园区参考架构模板库（含垂直行业案例）

## R · 原文引用

> "OMNISWITCH COMPACT CORE NETWORK — Network virtualized using Virtual Chassis (VC) for simplified two-layer architecture; Fully redundant and resilient; UNP for NAC security and QoS; Server farm dual home connected directly to network core with LAG" (p314)

> "OMNISWITCH 10/40 GIGE DISTRIBUTED RING NETWORK — Network virtualized using ERPv2; Simplified two-layer architecture; Dual Home Link (DHL) at the access; 10 GigE links from the network core to Server farm" (p316)

> "SMB solution — Short installation and set-up time with zero-touch configuration … Fully integrated and lab tested, single vendor, plug and play solution (IP Network + Wi-Fi + Voice + Mobility)" (p305)

## I · 方法论骨架

四大园区模板 + 垂直案例，按判定信号选模板再改端口出 BOM：

| 模板 | 判定信号 | 核心 | 接入 | 变体 |
|---|---|---|---|---|
| SMB 一体化（f07/c05/c06） | 20-100 用户、无 IT | 6360/6560 + Stellar AP + OmniPCX | 6360-P10/P24/P48 | OXO Purple 20 分钟零接触装机 |
| 紧凑核心（f08/c11） | 单楼宇/紧凑园区、要冗余少管理点 | 6870 或 6860N 组 VC（10/25G） | 6560/E PoE+ | 高配：核心 6900 + 6860N/6870 接入 |
| 分布式环网（f09/c12） | 多楼宇、光纤成环、双路星型贵 | 6900（ERPv2 环 10/40G） | 6870/6860N/6560E/6360 + DHL | 服务器 10G 直挂核心 |
| 密集核心（f10/c13） | 用户高度集中于个别楼宇、超大网 | 9900（10/40/100G） | 6860N 多千兆 PoE+ | 低配：6900 核心 + 6870 汇聚 |
| 多千兆无线边缘（c08/c09） | Wi-Fi 6/6E/7 AP 空口 >1G | 6900，4×25G LACP | 6560E-P24Z8/P24Z24/E-P48Z16 或 8×6860N VC（384 千兆/192 多千兆口、95W） | CAT5e/6 布线即可 |
| 双核心两层/三层（c10） | 中大型政企、最大冗余 | 9900 双核心（或 6900 SPB-M 核心+BEB） | 6360/6465/6560E/6860N/6870 | 10G LAG / DHL |

垂直行业案例：城域商业管理服务（c01：10G 环 6860N 汇聚 + 6465-P28 双归 IP/MPLS，opt82/ARP 检查/802.1ad/SPB/EVPN over I-SID 特性清单）；住宅 Triple-Play（c02：6560/E 接入 + 组播 TV VLAN）；数据中心 POD（c03：6×6900 Mesh，服务器 1/10G L2、POD 间 10/40/100G L2/L3）。

## A1 · 书中案例

见上表括注（c01-c03、c05、c06、c08、c10-c13），全部为书中 p296-319 的官方架构页，可直接改写为方案分册章节。

## A2 · 触发场景（含与相邻 skill 的区分）

- 触发：需求清单到手要 30 分钟出架构图与机型 BOM 框架；投标技术分册要参考架构章节。
- 区分：本 skill 是**成品模板库**（拿来改端口就用）；先做架构分层决策与高可用选型走 `campus-design-tiering-and-ha`；模板里用到的 VC/ERP/SPB 机制细节分别走 `virtual-chassis-design`、`dhl-erp-ring-protection`、`spb-vxlan-core-fabric`；视频监控垂直方案独立在 `video-surveillance-design`。

## E · 可执行步骤

1. 按判定信号选模板（楼宇分布/光纤形态/用户密度/无线需求）。
2. 数端口：按信息点数选接入机型与口数，套模板高/低配变体。
3. 核对模板附带卖点（VC 统一管理、DHL 双活、UNP 安全、零接触），写进方案亮点段。
4. 改图：替换机型型号与端口数，输出架构图 + 分层 BOM 骨架。
5. 服务器区/数据中心按模板接 LAG 双归或 POD 形态。

## B · 边界与陷阱

- 模板机型组合基于 Ed29 产品线，换代后按最新产品组合等价替换。
- c12 环网模板的 50ms 承诺须满足 ERP 前提条件（见 dhl-erp skill）。
- c01/c02 城域案例涉 Metro 特性多为许可制，BOM 补许可行（见 license skill）。
- 模板不回答"为什么选这个架构"——答辩前先过分层设计法的决策依据。

---
来源条目: f07, f08, f09, f10, c01, c02, c03, c05, c06, c08, c10, c11, c12, c13, g03
