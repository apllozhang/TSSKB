---
name: dhl-erp-ring-protection
description: 接入双归用 DHL、光纤成环用 ERPv2：设计规则、50ms 承诺条件与 RPL 放置、防环三件套。
source_book: DT00XPS281EN Campus LAN Presales
---

# DHL 双归属与 ERPv2 环网保护

## R · 原文引用

> "Dual Home Link Active-Active • Fast failover between core and access switches without using Spanning tree • DHL managed only an access switch • Two DHL links are both active … One session per switch is allowed … DHL Active-Active splits a number of VLANs between two active links" (p54-55)

> "Network protection mechanism (ring topology) that enables 50 ms convergence time … ITU-T G.8032/Y.1344 … 16 nodes per ring (recommended) • 4094 protected Vlans … with less than 1200 km of ring fiber circumference, and fewer than 16 Ethernet Ring Nodes, the … time … shall be less than 50 ms. Maximum of 64 ERP rings per switch" (p122-128)

> "Each ring must have its own RPL. The RPL can be placed anywhere on the Master Ring, including the shared links … Since the Sub Ring is not closed using the shared link, the RPL cannot be placed on the shared link" (p127)

## I · 方法论骨架

**DHL（接入双活，替代堆叠双归）**
- 作用域只管接入交换机；每台 1 会话、恰 2 条链路（可配普通口或 LAG 口）。
- 双链路同时活跃，VLAN 分组拆到 Link A/B 负载分担，故障时改各 VLAN 转发状态切换，全程无 STP。
- 防环红线：两台上行设备之间不得再挂核心以外的链路；接入侧配三件套 **LPS / Loop Guard / BPDU Shutdown**。
- 机型口径矛盾（需注版）：p54 称"除 9900 全支持"，p301 矩阵 6570M/6900/9900 均 No——DHL 只在接入/汇聚层兑现。

**ERPv2（G.8032 环网）关键常数**

| 常数 | 值 | 前提 |
|---|---|---|
| 收敛 | <50ms | 环周长 <1200km、节点 <16、无拥塞、节点 idle 态 |
| 每环节点 | 建议 16 | — |
| 保护 VLAN | 每环 4094 | — |
| 每机环数 | 64 | — |

**多环设计规则**：主环（Major Ring）+ 子环（Sub-Ring）+ 互连节点 + 共享链路（归主环）；每环（主、子各自）有且只有一个 RPL；子环 RPL 不能放共享链路上；形态可多环并联、链式、梯形（一个互连节点挂多子环）。回切/非回切模式可选，非回切在故障恢复后不自动回切。

## A1 · 书中案例

c12（p316，详见参考架构库 skill）：五楼宇 10/40G ERPv2 环 + 核心侧 DHL 接入双归的分布式环网方案。

## A2 · 触发场景（含与相邻 skill 的区分）

- 触发：客户光纤资源呈环形（校园/厂区/轨道交通沿线），或招标书写"故障倒换 ≤50ms"的电信级 SLA；接入交换机不想堆叠但要双活上联。
- 区分：本 skill 管 **DHL 与 ERP 的机制与规则**；整体架构模板（环网+接入机型组合）走 `campus-reference-architectures`；"六种高可用方案选哪条路线"的横比走 `campus-design-tiering-and-ha`；SPB 场景（非时敏大网）走 `spb-vxlan-core-fabric`。

## E · 可执行步骤

1. 判 SLA：要求 50ms → ERPv2；只要接入双活不要堆叠 → DHL；两者可叠加（环骨干 + DHL 接入）。
2. DHL 设计：确认接入机型在支持列（6360/6465/6560/6860N/6870 等），划 VLAN 到 Link A/B，接入侧开三件套。
3. ERP 设计：拿光纤路由图切主环/子环，核 <16 节点、<1200km 周长、<4094 VLAN、单机 <64 环。
4. 逐环放 RPL（唯一性检查，子环避开共享链路），定回切模式。
5. 输出环网设计稿 + 施工规范（禁止 DHL 上联互接非核心设备）。

## B · 边界与陷阱

- ce07：SPB 约 300ms ≠ 50ms；50ms 只能用 ERPv2 兑现，且 50ms 本身有 1200km/16 节点/无拥塞前提，应标时要写条件。
- ce03：DHL 上联误接非核心设备即成环、广播风暴——三件套必须配进基线配置。
- ce04：DHL 机型支持按 p54 全承诺会翻车，以 p301 矩阵 + 最新 release notes 为准。
- ERPv2 除 OS2260 外全系支持（6360 起）。

---
来源条目: f13, p13, p14, p15, p16, ce03, ce04, ce07, g13, g15, g36
