---
name: vxlan-evpn-underlay-bgp-design
description: 何时用：搭建或调优 VxLAN/EVPN 的 OSPF/eBGP underlay、iBGP EVPN overlay 与路由反射器时。
source_book: DT00XTE325EN VxLAN/EVPN
---

# Underlay 与 BGP Overlay/RR 设计（Loopback0 / OSPF / eBGP / iBGP / RR）

## R · 原文引用

> Layer 3 protocols: ISIS, OSPF, BGP. Spine and Leaf are identified by the Loopback0 interface. Support for ECMP... For BGP underlay use eBGP. Spine nodes share a single AS. Each Leaf node has unique AS.（p60）

> Use a single-area OSPF configuration to limit the SPF flooding domain. Use point-to-point OSPF network type... This eliminates DR election wait times. Using BFD for fast-convergence... Set OSPF SPF delay and hold timers to 0.（p80；p186 补 ECMP 与 MTU 预留 50 字节）

> Overlay 配置四步：Load and enable BGP. Set the ASN to be the same for all the switches. / Enable the EVPN advertisements... / Configure the iBGP peering sessions with the loopback interfaces. Set the "update-source" as the loopback interface. / Activate EVPN capability for each peer.（p84；CLI：ip load bgp / ip bgp autonomous-system 65000 / ip bgp address-family evpn / neighbor 1.1.1.10 remote-as 65000 + update-source Loopback0 + activate-evpn）

> Without Route Reflectors, N Leafs require N*(N-1)/2 sessions... having 10 routers will result in 45 peerings. Usually, spine switches can be used route reflectors.（p132/p136）

## I · 方法论骨架

1. **身份原则**：一切从 Loopback0 开始——VTEP 身份、OSPF router-id、BGP router-id、update-source 四合一复用同一 Loopback0 地址。
2. **Underlay 选型**：ISIS/OSPF/BGP 三选一，课程与架构指南推荐组合为 **OSPF underlay + iBGP overlay**（p186 原文推荐句）。若用 BGP underlay 必须 eBGP，AS 规划=所有 Spine 共享一个 AS、每台 Leaf 唯一 AS（overlay 则全网同 AS 65000，两者别混）。
3. **OSPF 收敛参数包六条**：单区域；互联口 router VLAN 口 + 网络类型 point-to-point（免 DR 等待）；BFD 毫秒检测（transmit/receive/echo-interval 均 200 + `ip ospf bfd-state enable`）；`spf-timer delay 0 / hold 0`；ECMP 多路径；MTU 预留 VXLAN 头 50 字节。设计指南加强版：`debug ip ospf set subsecond 1 / bfdsubsecond 1`。
4. **Overlay 五要素**：全网同一 ASN；`ip bgp address-family evpn`（AFI=25/SAFI=70）；邻居=对端 Loopback0；update-source Loopback0；逐邻居 `activate-evpn`（漏一条就不交换 EVPN NLRI）。
5. **RR 扩展**：会话数 N(N-1)/2 不可持续 → Leaf 只与 RR 建会话；RR 专属命令 `ip bgp client-to-client reflection`、`ip bgp cluster-id <id>`、`neighbor <ip> route-reflector-client`；实践惯例 Spine 兼任 RR，冗余用单集群双 RR。

## A1 · 书中案例

- Lab1 四节点底座（p78-86）：Loopback 取值 Spine-1/2=1.1.1.10/11、Leaf-1/2=1.1.1.1/2；互联 VLAN 110(S-S)/101/102/111/112，子网 172.16.1xy.0/24，端口号对称；验证链 `sh ip ospf neighbor` 全 Full → `sh ip routes` 看 Leaf 双等价路径 → `show ip bgp neighbors` established + evpn advertised。
- 架构指南 6 节点参考设计（p187-197）：Spine=1.1.1.1/2、Leaf=1.1.1.10/20/30/40；互联口挂聚合口（如 port 1/1/50A tagged）；6 台全互联 iBGP EVPN（每台 5 邻居），全量 established。

## A2 · 触发场景（含与相邻 skill 的区分）

- 触发：新建 fabric 底座、BGP EVPN 会话起不来、underlay 收敛调优、Spine 规模化改造上 RR。
- 区分：底座通了以后开业务/开网关 → `vxlan-evpn-service-provisioning`；整体路线与版本边界 → `vxlan-evpn-five-step-architecture`。本 skill 只管"让 Loopback 之间路由可达、EVPN 会话建立"这一层。

## E · 可执行步骤

1. 每台配 `ip interface "Loopback0" address <x.x.x.x>`，同地址设 OSPF/BGP router-id。
2. 逐链路建 router VLAN 口（`ip interface "vl101" address 172.16.101.10/24 vlan 101 rtr-port port 1/1/27 tagged`）。
3. 全局 `ip bfd transmit 200 / receive 200 / echo-interval 200`；接口 `ip ospf interface "vl101" type point-to-point / bfd-state enable`；全局 `ip ospf spf-timer delay 0 / hold 0`。
4. Overlay：`ip load bgp` → `ip bgp autonomous-system 65000` → `ip bgp address-family evpn` → 对每个对端 Loopback `neighbor <ip> remote-as 65000 / update-source Loopback0 / activate-evpn / admin-state enable` → 全局 `ip bgp admin-state enable`。
5.（规模化）在 Spine 上配 cluster-id 与 route-reflector-client，Leaf 改为只与 RR 建会话。
6. 验证：`sh ip ospf neighbor` 全 Full；`sh ip routes` 等价路径；`show ip bgp neighbors` Oper=established 且 Activate evpn=enabled、Neighbor evpn=advertised。

## B · 边界与陷阱

- eBGP underlay 与 iBGP overlay 的 AS 规则相反（underlay：Spine 同 AS/Leaf 各异；overlay：全网同 AS），迁移或混合场景最容易配反。
- `activate-evpn` 是逐邻居开关，漏一条该邻居只建普通 BGP 会话、不交换 EVPN 路由。
- MTU 是隐性杀手：underlay 不预留 50 字节 VXLAN 头会出现大帧静默丢包、小包正常的现象。

---
来源条目: f02, f03, f07, p02, p03, p04, p05, c01, c06, g15, g16, g19
