---
name: AOS 8 CLI 命令地图——Fabric 骨干域（SPB/MPLS/Service Manager，第 9-11 章）
description: 需要在 OmniSwitch AOS 8 上配置 SPB 骨干（ISIS-SPB/BVLAN/ECT）、SPBM 服务（ISID/SAP/PBB）、MPLS LSP/VPN，或查 spb/mpls 命令语法与平台支持时使用。
source_book: OmniSwitch AOS Release 810R04 CLI Reference User Guide
---

## R（触发场景）
- 部署/排障 SPB 骨干：BVLAN、桥优先级、ECT、IS-IS SPB 邻接
- 配 SPBM 业务：ISID/SAP 绑定、PBB 封装、SPB IP VPN（VRF 绑定）
- MPLS LSP/标签转发/VPN 隧道命令查询
- SPB 邻居发现失败、最短路径计算异常的配置一致性核对

## I（核心理念）
SPBM 架构（P11，<<<PAGE 743>>>）：SPB-M 按 IEEE 802.1aq 用 PBB（802.1ah MAC-in-MAC）封装穿越骨干，最短路径树由 ISIS-SPB（IS-IS + SPB TLV 扩展）计算；命令分两层——第 10 章 Shortest Path Bridging 管 backbone（控制面），第 11 章 Service Manager 管 services（数据面），互为配套。MPLS（第 9 章）是并列的标签转发域。查命令时先分清"骨干层还是服务层"，再到对应章。

## A1（决策框架）
1. **骨干控制面**（BVLAN/桥优先级/ISIS-SPB 参数）→ 第 10 章
2. **业务数据面**（ISID/SAP/PBB 服务）→ 第 11 章
3. **L3 over SPB**（ISID 绑定/重分发进 VRF）→ 第 10 章 `spb ipvpn`
4. **MPLS** → 第 9 章
5. 平台核对：BVLAN 等命令在 6360/6465/6560 为 No（X1）

## A2（操作步骤）·章节清单与代表命令
- **Ch9 MPLS（<<<PAGE 689>>>，约 26 条）**：`mpls` LSP 与 VPN 隧道命令族
- **Ch10 Shortest Path Bridging（<<<PAGE 743>>>，约 43 条）**：`spb bvlan <id>`（1-4094，支持区间如 10-20；默认 admin-state=enable）（P12）；`spb isis bridge-priority`（默认 32768，越小越优；占 8 字节 Bridge ID 高 2 字节，低 6 字节为桥 MAC）（P14）；`spb ipvpn bind/redist`（P15）；BVLAN 上 STP 自动禁用、全部端口保持转发态（P13）
- **Ch11 Service Manager（<<<PAGE 839>>>，约 83 条）**：`spbm` 服务层——ISID/SAP 绑定、PBB 封装业务

## E（实证案例）
- 命令地图型 skill，不搬运案例；原书每条命令自带 Example，按章首页码回查（cases 原件未创建）

## B（反例/坑）
- BVLAN 平台支持：仅 6570M/6860/6860N/6865/6870/6900/6575/6920/9900；6360/6465/6560 为 No（X1，<<<PAGE 745>>>）
- 每台 SPB 桥的 BVLAN 配置必须完全一致，否则 ISIS-SPB 邻居发现与最短路径计算失败（X17，<<<PAGE 745>>>）
- 同一 ISID 不能既绑定又重分发到同一 VRF 实例（X11）

## 来源
OmniSwitch AOS Release 810R04 CLI Reference User Guide 第 9 章（<<<PAGE 689>>>）、第 10 章（<<<PAGE 743>>>）、第 11 章（<<<PAGE 839>>>）。条目来源：principles P11-P15；counter-examples X1/X11/X17；frameworks F4。
