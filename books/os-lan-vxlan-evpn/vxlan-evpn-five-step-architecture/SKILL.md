---
name: vxlan-evpn-five-step-architecture
description: 何时用：从零规划或讲解 AOS VxLAN/EVPN 部署路线、论证迁移动因、核对 8.10R1 版本能力边界时。
source_book: DT00XTE325EN VxLAN/EVPN
---

# VxLAN/EVPN 五步配置法总纲与 AOS 架构模型

## R · 原文引用

> EVPN CONFIGURATION STEPS – PART 1/5: Underlay Configuration / Overlay Configuration / Service Access / Service / SAP.（p59，同一张步骤图在 p59/p62/p66/p68 逐段展开，贯穿 p59-149 共 21 处）

> 传统 DC 四痛点：Inefficient use of resources (STP blocked redundant links) / Scalability issues (12-bit VLAN ID, upper limit 4096) / Operational complexity / Traffic tromboning (static first-hop router)。MP-BGP EVPN changes this model and uses a proactive approach for end-host reachability information learning.（p164/167）

> The AOS EVPN service model provides enhanced stability... by: Instantiating an ESI for any access port that is enabled for EVPN; generating the ESI+ETag aware routes; auto-generation of the RD and RT; Only in-use addresses are imported into the data-plane (on-demand model).（p184-185）

> R-T5 / Symmetric IRB / tandem 复制 / All-active "will not be supported in the initial release 8.10R1"（p173/p179/p180/p182 四句逐条命中）

## I · 方法论骨架

1. **五步法主线**（AOS 独有教学结构）：①Underlay（L3 路由底座）→ ②Overlay（MP-BGP EVPN）→ ③Service Access（接入口启用以太网段）→ ④Service（EVPN-VXLAN 业务实例化）→ ⑤SAP（业务接入点绑定 VLAN）。Part2-5 依次叠加 IRB/DAG、MAC 学习/Proxy ARP、RR、多归属与 RD/RT。
2. **迁移论证链**（给客户讲为什么）：STP+VLAN 四痛点 → VXLAN 数据面解耦（MAC-in-UDP、24bit VNI、16M 网络）→ 裸 VXLAN 仍靠 flood-and-learn → MP-BGP EVPN 补上主动式控制面。选型四收益：统一控制面、可扩展（多归属/ARP 抑制/DAG/MAC mobility）、多封装灵活、VRF+VNI+RD+RT 安全隔离。
3. **AOS 实现模型四件套**：全端口 ESI 实例化；ESI+ETag 粒度路由（按 ETag 汇总撤收）；RD/RT 自动生成；on-demand 按需导入（BGP RIB 全网分发，仅被查找的目的才进硬件 FDB）。
4. **VXLAN 封装参数**：UDP 4789、头部开销 50 字节（underlay MTU 必须预留）、24bit VNI/16M 网络、外层 IP 即两端 VTEP 的 Loopback0。
5. **版本能力边界**（售前/交付核对表）：EVPN 首版 8.10R1、仅 OS6900；首版不支持 RT5、对称 IRB、tandem 组播复制、all-active 多归属。

## A1 · 书中案例

- 数据面学习模型（p38）：每 VNI 一个虚拟桥（service 实例），SAP/SDP 均为虚端口；EVPN 下远端 MAC 经 RT2 学到、挂 sdp:32768 虚端口；学习可禁用（禁后未知 MAC 直接丢弃）。
- on-demand 现象判读（p184/p117）：`sh mac-learning evpn-vxlan` 表项少于 BGP RT2 路由数属正常，用 `debug evpn show bgp route-type rt2` 对比即可，不代表路由缺失。
- 转发流程（p181-182）：同子网 8 步（ARP 泛洪→RT2 通告→应答入表→单播直达）；跨子网（非对称 IRB）6 步（ARP 网关→入端 PE 查 MAC-VRF 后查 IP-VRF 跨 IRB 路由→目的 VNI 封装转发）。

## A2 · 触发场景（含与相邻 skill 的区分）

- 触发：方案论证/写迁移建议书、开局排总路线、8.10R1 能力核对、"BGP 有路由但 MAC 表没有"的正常性判读。
- 区分：具体命令怎么配 → `vxlan-evpn-underlay-bgp-design`（底座）与 `vxlan-evpn-service-provisioning`（业务）；多归属/DF → `vxlan-evpn-multihoming-df`；BUM 与排障 → `vxlan-evpn-bum-troubleshooting`。本 skill 只管"路线图 + 架构论证 + 版本边界"。

## E · 可执行步骤

1. 售前核对：客户需求若命中 RT5（L3VPN/外联汇总）、对称 IRB、组播 tandem、all-active 四项任一，标注"8.10R1 不支持"，改方案或核对目标版本 release notes。
2. MTU 规划：underlay 各链路 MTU ≥ 客户帧 + 50 字节 VXLAN 开销（业务默认 MTU 9194 / VPN IP-MTU 1500）。
3. 开局按五步顺序推进并逐层验证：Underlay（OSPF 邻居 Full）→ Overlay（BGP established）→ Access/Service/SAP（业务 Oper Up）→ RT3/MAC/SDP 隧道。
4. 判读 MAC 表项少于 BGP 路由：先 `debug evpn show bgp route-type rt2` 确认控制面有路由，再按 on-demand 模型判定为正常。

## B · 边界与陷阱

- EVPN 控制面仅 OS6900、8.10R1 起支持；培训环境为 8.10R2，能力表随 release 滚动放开，交付前必须复核目标版本。
- on-demand 模型下不能拿硬件 FDB 表项数当路由健康指标。
- VXLAN 学习可被禁用，禁用后任何未知 MAC（源或目的）直接丢弃——排障先查该开关。

---
来源条目: f01, f09, f10, p01, p18, p20, p21, ce02, g10, g24, g25, g26, g27, g28
