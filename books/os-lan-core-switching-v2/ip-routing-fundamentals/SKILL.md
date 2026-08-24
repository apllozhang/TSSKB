---
name: IP 路由基础与静态/RIP/IS-IS
description: 需要配置静态/递归路由、RIP 或理解 AOS 路由优先级、Loopback 约定时使用本技能。
source_book: DT00XTE216 OmniSwitch LAN Core Switching Ed15
---

## R（触发场景）
- 交换机要上默认路由/备份路由，或下一跳不固定需要递归静态路由
- 小型网络仍跑 RIP，直连/静态路由不通告需要重分发
- 需要判断多协议共存时 RIB 的选路次序

## I（核心理念）
AOS 的路由世界观是"路由数据库（router database）+ 协议优先级（route-pref）"：Local 1 / Static 2 / OSPF 110 / ISIS-L1 115 / ISIS-L2 118 / RIP 120 / EBGP 190 / IBGP 200 / Import 210。Loopback0 是全网稳定的身份地址（router-id、BGP peering、PIM RP 等），RIP/OSPF 自动通告它而 BGP 不会。静态路由的递归形式（follows）让下一跳跟随另一条路由动态解析。

## A1（行动框架）
1. 静态与默认路由：`ip static-route 134.1.21.0/24 gateway 10.1.1.1` / `ip static-route 0.0.0.0/0 gateway 10.1.1.1`；双默认路由用 metric 1 与 metric 2 互备；`show ip router database` 可见 inactive 备份（<<<PAGE 222>>>-<<<PAGE 223>>>）
2. 递归路由：`ip static-route 172.30.0.0/16 follows 2.2.2.2 metric 1`（<<<PAGE 225>>>）
3. RIP 最小配置：`ip load rip` → `ip rip interface <if> admin-state enable` → `ip rip admin-state enable`（<<<PAGE 228>>>）
4. RIP 重分发：`ip route-map rip_1 sequence-number 50 action permit / match ip-address 0.0.0.0/0` + `ip redist local into rip route-map rip_1 admin-state enable`（static 同理）（<<<PAGE 228>>>）
5. IS-IS 最小配置：`ip load isis` → `ip isis admin-state enable` → `ip isis area-id 49.0001` → `ip isis activate-ipv4` → `ip isis vlan 5` → `ip isis vlan 5 address-family v4` → `ip isis vlan 5 admin-state enable`；`show ip isis adjacency/route/spf`（<<<PAGE 697>>>-<<<PAGE 698>>>）

## A2（进阶应用）
- RIP 四定时器：Update 30（1..120）/ Invalid 180（3..360）/ Garbage 120（0..180）/ Hold-down 0（0..120）；约束 update ≤ invalid/3、invalid ≥ 3×update（<<<PAGE 231>>>）
- RIP 16 跳不可达、网络直径最大 15（<<<PAGE 227>>>）
- 优先级可改：`ip route-pref BGP 8`（<<<PAGE 503>>>）
- IS-IS NSAP 结构（Area-ID/System-ID/NSEL），本地管理 AFI=49；DIS 类似 OSPF DR 但可抢占，Hello 9s（DIS 3s），按优先级+MAC 选举（<<<PAGE 686>>>、<<<PAGE 689>>>-<<<PAGE 690>>>、<<<PAGE 694>>>）

## E（实证案例）
- C-19 双默认路由 metric 互备，database 中 inactive 展示（<<<PAGE 222>>>-<<<PAGE 223>>>）
- C-20 RIP 最小配置与 local/static 重分发（<<<PAGE 228>>>）
- C-39 IS-IS 单区域启用模板（<<<PAGE 697>>>）

## B（边界与陷阱）
- RIP 默认只通告学到的 RIP 路由和 Loopback0，local/static 路由必须重分发，漏配即路由缺失（<<<PAGE 228>>>）
- 递归静态路由的网关随 follow 目标路由变化而漂移，设计时要确保 follow 目标稳定防环路（<<<PAGE 225>>>）
- Loopback0 被 RIP/OSPF 自动通告但 BGP 不通告（<<<PAGE 216>>>）

## 来源
- principle·P-35 IP 接口与 Loopback0（<<<PAGE 214>>>、<<<PAGE 216>>>）
- principle·P-36 递归静态路由（<<<PAGE 224>>>、<<<PAGE 225>>>）
- principle·P-37 RIP 规格与定时器（<<<PAGE 227>>>、<<<PAGE 231>>>、<<<PAGE 232>>>）
- principle·P-38 路由协议优先级（<<<PAGE 299>>>、<<<PAGE 503>>>）
- principle·P-66 IS-IS NSAP 与 DIS（<<<PAGE 686>>>-<<<PAGE 694>>>）
- case·C-19/C-20/C-39；counter·X-17/X-18
