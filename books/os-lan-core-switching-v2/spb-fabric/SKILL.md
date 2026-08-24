---
name: SPB 最短路径桥接 Fabric
description: 需要评估/部署 SPB-M 骨干（BVLAN/ISIS/I-SID/SAP）替代 STP，或设计其 L2/L3 服务与 iFab 自动化时使用本技能。
source_book: DT00XTE216 OmniSwitch LAN Core Switching Ed15
---

## R（触发场景）
- 园区核心二层 Fabric 嫌 STP 链路利用率低、收敛慢，考虑 SPB-M
- 要在 SPB 骨干上开通跨 BEB 的 L2 VPN（I-SID/SAP）或 L3 服务
- iFab 零触摸部署的动态服务编号/隔离策略需要设计或排障

## I（核心理念）
SPB（802.1aq）用 IS-IS 做控制平面、MAC-in-MAC（PBB，802.1ah）做数据平面：BCB 只按 BMAC 转发不学客户 MAC，每节点对每个 BVLAN 建一棵以自己为根的 SPF 树，全链路可用、路径对称、帧有序。服务标识 I-SID 全局强一致，service 号仅本地有效。相比 STP 的"闲置链路+次优路径+慢收敛"，SPB 换来全链路利用与百毫秒级收敛。

## A1（行动框架）
1. 骨干四任务（<<<PAGE 547>>>-<<<PAGE 548>>>）：`spb bvlan 2000/2001/2002`（各 BVLAN 配不同 ECT-ID 最大化分流）→ 修改 control BVLAN 前先 `spb isis admin-state disable` → `spb isis control-bvlan 2000` → `spb isis interface port 1/1/x`（各骨干口）→ `spb isis admin-state enable`
2. L2 服务：`service spb 2001 isid 2001 bvlan 2001 description vlan2 admin-state enable`；接入 `service access port 1/1/3` + `service spb 2001 sap port 1/1/3:2 admin-state enable stats enable`（<<<PAGE 555>>>-<<<PAGE 556>>>）
3. 验证：`show mac-learning domain spb`（CMAC 绑定 sap:/sdp: 接口）（<<<PAGE 558>>>）；健康检查命令族 `show spb isis bvlans / interface / adjacency [detail] / info / unicast-table bvlan 2000 / spf bvlan 2000 / database / nodes`（<<<PAGE 549>>>-<<<PAGE 550>>>）

## A2（进阶应用）
- BUM 复制模式：Head-End（默认，带宽效率低/资源高/同径）与 Tandem（带宽高/资源低；(S,G) 同径、(*,G) 不同径）；head-end 与 tandem 按 per-service 选，(S,G)/(*,G) 按 per-BVLAN 选（<<<PAGE 539>>>、<<<PAGE 573>>>-<<<PAGE 577>>>）
- L3 服务选型：域内用 L3 VPN（VRF 路由经 IS-IS TLV 携带，无需在 VPN 接口跑路由协议），仅边界节点对接外部用 VPN Lite（叠跑 OSPF/BGP）（<<<PAGE 534>>>-<<<PAGE 537>>>、<<<PAGE 592>>>）
- 动态服务编号：ISID = Base Service Number + Domain ID + (VLAN % Service Modulo)，默认 Modulo 512 会让最多 8 个 VLAN 混入同一服务，需隔离时改 4096（<<<PAGE 600>>>-<<<PAGE 601>>>）
- iFab 七阶段零触摸（Auto-VC→RCD→LACP→Routing→SPB→Profiling→MVRP），任一阶段失败自动回退；管理命令 `auto-fabric protocols spb|mvrp... admin-state disable`、`show auto-fabric config`、`auto-fabric config-save admin-state enable`；默认 BVLAN 4000-4015/ECT 1-16、控制 BVLAN 4000（<<<PAGE 624>>>-<<<PAGE 638>>>）
- SPB+LAG 哈希：外层是 BMAC 熵不足，聚合口需开 tunnel-protocol 哈希内层 CMAC/IP（<<<PAGE 611>>>）
- Overload 硬隔离：开启后节点不转发任何穿越流量，即使无替代路径（<<<PAGE 605>>>）

## E（实证案例）
- C-35 SPB 骨干+L2 服务全流程：BVLAN/ISIS/SAP/I-SID 打通跨 BEB 的 L2 VPN，ISID 全局一致而 service 号本地有效（<<<PAGE 548>>>-<<<PAGE 558>>>）
- C-36 SPB 监控命令族实战输出（<<<PAGE 549>>>-<<<PAGE 550>>>）
- C-37 iFab Auto-Fabric 管理命令（<<<PAGE 639>>>）

## B（边界与陷阱）
- ISID 与 BVLAN 映射在所有相连 BEB 上必须全局一致，错配则服务不通；每个 ISID 只能映射一个 BVLAN（<<<PAGE 555>>>）
- Control BVLAN 只能在协议禁用时修改；BVLAN 上没有 STP，不要指望生成树防环（<<<PAGE 548>>>）
- BVLAN 数量不要超过物理等价路径数，盲目建满 16 个反而增加控制平面负载（<<<PAGE 610>>>）
- 不同 VLAN 映射同一服务会导致 MAC 反复学习/清空（mac-move）震荡，一个 VLAN 一个 ISID/SAP（<<<PAGE 610>>>）
- 默认 Service Modulo 512 会把不同 VLAN 混入同一 L2 域，多租户场景必改 4096（<<<PAGE 601>>>）

## 来源
- framework·F-10 STP vs SPB 选型（<<<PAGE 521>>>-<<<PAGE 523>>>、<<<PAGE 565>>>）
- framework·F-11 SPB 骨干四任务（<<<PAGE 547>>>、<<<PAGE 548>>>）
- framework·F-12 iFab 零触摸流水线（<<<PAGE 624>>>-<<<PAGE 638>>>）
- principle·P-62 控制平面/数据平面（<<<PAGE 525>>>、<<<PAGE 567>>>-<<<PAGE 570>>>）
- principle·P-63 BUM 复制模式（<<<PAGE 539>>>、<<<PAGE 573>>>、<<<PAGE 574>>>）
- principle·P-64 L3 服务两变体（<<<PAGE 534>>>-<<<PAGE 537>>>、<<<PAGE 592>>>）
- principle·P-65 动态服务编号（<<<PAGE 600>>>、<<<PAGE 601>>>）
- case·C-35/C-36/C-37；counter·X-24/X-25/X-26/X-27/X-28/X-29/X-30
