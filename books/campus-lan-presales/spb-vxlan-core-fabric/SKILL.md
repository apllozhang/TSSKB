---
name: spb-vxlan-core-fabric
description: 用 SPB（BCB/BEB/I-SID）做多租户园区核心、VXLAN 做 DCI/EVPN 应标：角色分工、路由机制与常数。
source_book: DT00XPS281EN Campus LAN Presales
---

# SPB/VXLAN 核心织构与多租户设计

## R · 原文引用

> "SPB DEPLOYMENT IN LAN NETWORK — Core, Backbone Core Bridge (BCB): Learns BEB addresses, IS-IS SPB for paths, PBB for data plane, L3 routing. Aggregation, Backbone edge bridge (BEB): VLAN to I-SID, IS-IS for MAC learning … Access: IEEE 802.1Q VLAN on uplinks, STP towards BEB" (p100)

> "ENTERPRISE SPB LAN CORE — MPLS styled service architecture; VLAN extensibility across campus / No STP / Faster, easier to deploy; Service Virtualization (ISID) for departmental isolation; Enabling multi-tenancy … L3 inter-departmental routed control with VPN-lite or L3-VPN; VXLAN support for DCI" (p319)

> "VXLAN: UDP port 4789 by default • 50 bytes of overhead • 24 bit VXLAN Identifier • 16 M logical networks … one multicast group is used per VNI (PIM-BIDIR)" (p107, p118)

## I · 方法论骨架

**SPB 三层角色分工（改造成本可控的关键：接入免 SPB）**

| 层 | 角色 | 职责 | 机型 |
|---|---|---|---|
| 接入 | 普通 802.1Q | VLAN 上联，向 BEB 跑 STP | 任意（6360/6465/6560E） |
| 汇聚 | BEB | VLAN→I-SID 映射、边缘 MAC 学习、环回检测 | 6860N/6870/6900/9900 |
| 核心 | BCB | 只学 BEB 的 B-MAC、IS-IS 算路、L3 路由 | 6900/9900 |

SPB 卖点常数：收敛约 **300ms**；单域最多 **1000 节点**；全链路 UP 无 STP；流量对称同径；MAC-in-MAC 地址隔离。BVLAN 管"走哪条路"，I-SID 管"属于哪个业务"（部门/租户隔离：一人一个 I-SID 即私有 VPN）。

**SPB 上 L3 路由两种机制**：①IP-VPN Lite——BEB 上 VRF 接口跑路由协议，VRF 靠 I-SID 打通；②L3/IP-VPN——VRF 路由经 ISIS-SPB TLV 发布，ISIS-SPB 充当 IGP，VPN 接口免跑路由协议。共同点：核心/汇聚无需额外 IGP。

**VXLAN 常数**：RFC 7348、UDP 4789、开销 50 字节、24bit VNI（1600 万逻辑网）；VTEP 用 Loopback0 标识，硬件 VTEP 机型 6860N/6870/6900/9900，全系可透传。BUM 两种转发：Head-End 复制（须知道 VNI 内全部远端 VTEP IP）与 Tandem 组播（PIM-BIDIR，每 VNI 一个组播组）。VXLAN-L3 两种交付：VPN-Lite（无 EVPN 控制面）vs L3VPN（BGP EVPN），8.10R1/R2 起交付于 6900/6870。

## A1 · 书中案例

c14（p319）：企业 SPB LAN 核心——核心 6860N/6865/6870/6900/9900 组 SPB，按部门 Admin/Staff/Agent 分 I-SID 隔离，VLAN 跨园区透明扩展、免 STP，部门间走 VPN-lite/L3-VPN，DCI 用 VXLAN；接入仍 6360/6465/6560-E 普通 VLAN。

## A2 · 触发场景（含与相邻 skill 的区分）

- 触发：多部门强隔离/多校区/租户化的政企园区；客户或设计院点名 EVPN/VXLAN 需要应标话术；数据中心互联。
- 区分：本 skill 管 **SPB/VXLAN 机制与角色设计**；"SPB 园区核心"整体模板在 `campus-reference-architectures`；EVPN over I-SID 与 VXLAN EVPN 的路线取舍在本 skill 内答。时敏 50ms 场景不在 SPB 职责内（走 `dhl-erp-ring-protection`）。

## E · 可执行步骤

1. 盘隔离需求：列部门/租户清单，一户一 I-SID；规划少量 BVLAN（如 1001/1002），业务扩张只加 I-SID。
2. 按角色分工表逐层指定机型：BEB/BCB 用 SPB 机型，接入层保留现网。
3. 定 L3 机制：VPN-Lite（简单，接口跑路由协议）vs L3/IP-VPN（ISIS-SPB 当 IGP，免配接口路由）。
4. 客户认 EVPN 时：接入网/园区推"SPB 达到同样效果更简单"；数据中心/DCI 走 VXLAN EVPN（6900/6870），选 Head-End 或 Tandem BUM 模式。
5. 输出：角色分工图 + I-SID 分配表 + 路由机制说明，写进方案分册。

## B · 边界与陷阱

- SPB 收敛 ~300ms，达不到电信级 50ms（ce07，见 dhl-erp skill）——别拿 SPB 应时敏 SLA。
- SPB 机型门槛：6560/E 需许可、6570M/6575 自 8.10R4 起；入门机型（6360/6465）无 SPB，只能做接入。
- VXLAN Head-End 复制漏登记任一远端 VTEP IP，该站点静默丢广播/未知单播（部分站点 ARP 学不到、时通时断），难排查。
- 对抗话术有边界：竞品 EVPN 已在客户侧扎根时，改推 VXLAN EVPN 路线比硬拗 SPB 更稳。

---
来源条目: f11, f12, p17, p18, p19, p20, p21, p44, c14, g06, g07, g08, g16, g17, g38, g39, g40, g47, g48, g49
