---
name: AOS 8 CLI 命令地图——路由域（IP/IPv6/IPsec/RIP/BFD/DHCP/VRRP/OSPF/IS-IS/BGP，第 21-32 章）
description: 需要在 OmniSwitch AOS 8 上配置 IP/IPv6 接口与路由、RIP/OSPF/OSPFv3/IS-IS/BGP、BFD、VRRP、DHCP Relay、IPsec、SLB 时，用本地图定位 CLI Reference 对应章节与代表命令。含 IP/IPv6/RIP/BFD/DHCP/VRRP/OSPF/IS-IS/BGP/SLB 分域核心命令速查表（A3，70+ 条语法/默认值/示例/页码）。
source_book: OmniSwitch AOS Release 810R04 CLI Reference User Guide
---

## R（触发场景）
- 查路由类命令语法/默认值/平台矩阵（ip ospf、ip bgp、ipv6 等）
- 路由协议命令敲了不生效——忘了 `ip load <protocol>` 先加载模块
- OSPF 定时器、BGP ECMP 等关键默认值核对
- DHCP Relay / IPsec / VRRP / BFD / SLB 章节定位

## I（核心理念）
本域是全书体量最大的命令域（<<<PAGE 1549-3227>>>），两条通用规律：其一，路由协议命令生效前需 `ip load <protocol>` 加载对应模块（X8，RIP/OSPF/IS-IS/BGP/VRRP）；其二，部分全局参数类命令要求先停协议再改。BGP 章 194 条为全书第二大章，命令分 Global/Aggregate/Network/Neighbor/Address-family/VRF 组（P20）；OSPF 章按 Global/Area/Interface/BFD/VRF 分组（P17）。

## A1（决策框架）
1. **单播底座**（接口/静态路由/ARP/DNS/UDP 中继）→ 第 21 章 IP（113 条）
2. **IPv6**→ 第 22 章；**IPsec**→ 第 23 章
3. **IGP/网关/检测**：RIP→24；BFD→25；VRRP→27；OSPF→28；OSPFv3→29；IS-IS→30
4. **EGP 与负载均衡**：BGP→31；SLB→32
5. **DHCP 中继/option82**→ 第 26 章（116 条）
6. 记住先 `ip load <protocol>`，再配协议命令

## A2（操作步骤）·章节清单与代表命令
- **Ch21 IP（<<<PAGE 1549>>>，约 113 条）**：`ip interface`、`ip route`、`ip domain`、ARP、`ip helper` 等单播底座（P16）
- **Ch22 IPv6（<<<PAGE 1793>>>，约 68 条）**：`ipv6` 地址/邻居发现/路由与过渡
- **Ch23 IPsec（<<<PAGE 1948>>>，约 11 条）**：`ipsec`/IKE 隧道加密
- **Ch24 RIP（<<<PAGE 1974>>>，约 41 条）**：`ip rip` 距离矢量
- **Ch25 BFD（<<<PAGE 2058>>>，约 16 条）**：`ip bfd`（为路由协议提供毫秒级故障检测）
- **Ch26 DHCP Relay（<<<PAGE 2092>>>，约 116 条）**：`bootp relay`/DHCP 中继、option82、监督
- **Ch27 VRRP（<<<PAGE 2334>>>，约 24 条）**：`ip vrrp`（首跳网关备份）
- **Ch28 OSPF（<<<PAGE 2392>>>，约 57 条）**：`ip ospf spf-timer [delay seconds] [hold seconds]`（0-65535，默认 delay=5/hold=10；任一为 0 则立即触发 SPF）（P18）；`ip ospf interface hello-interval`（0-65535 秒，默认 broadcast/P2P=10、NBMA/P2MP=30）（P19）；`ip load ospf` 前置（X8）
- **Ch29 OSPFv3（<<<PAGE 2513>>>，约 46 条）**
- **Ch30 IS-IS（<<<PAGE 2610>>>，约 62 条）**：SPB 控制面基础
- **Ch31 BGP（<<<PAGE 2744>>>，约 194 条）**：`ip bgp maximum-paths`（ECMP 开关，默认 disabled；启用后忽略 router-id 判等装全部等价路径；要求先停 BGP）（P22）；`ip bgp default local-preference`；BGP-4+MP-BGP（IPv6 前缀与邻居），peer 与 neighbor 术语互换（P20）
- **Ch32 SLB（<<<PAGE 3160>>>，约 31 条）**：`slb`（VIP/实服务组/健康检查）

## A3（核心命令速查）

语法/默认值/示例均摘自原书第 21-32 章对应条目；页码为 fulltext `<<<PAGE N>>>` 标记值。`{enable | disable}` 表示"多选一"。注意 X8：RIP/OSPF/IS-IS/BGP/VRRP 等协议命令前需 `ip load <protocol>`。

### IP 单播底座（第 21 章）

| 命令 | 语法要点 | 关键参数与默认值 | 典型用法（一行示例） | 页码 |
|---|---|---|---|---|
| ip interface | `ip interface if_name [{address \| vip-address} ip_address] [mask subnet_mask] [vlan vlan_id \| service service_id]`，`no` 删除 | 创建 IP 路由接口；emp/master emp 用于管理口 | `-> ip interface vlan-100 address 10.0.0.1 mask 255.255.255.0 vlan 100` | 1553 |
| ip static-route | `ip static-route ip_address [mask mask] {gateway {gateway_address \| null} \| interface if_name} [metric n] [tag n]`，`no` 删除 | 静态路由优先级高于动态路由 | `-> ip static-route 10.10.0.0 gateway 10.0.0.2` | 1569 |
| ip route-pref | `[vrf vrf_name] ip route-pref {static \| ospf \| rip \| isisl1 \| isisl2 \| ebgp \| ibgp \| spb-mgmt \| import} value` | 各协议路由优先级 | `-> ip route-pref ospf 20` | 1576 |
| ip redist | `[vrf name] ip redist {local \| static \| rip \| ospf \| isis \| bgp \| spb-mgmt \| import} into {rip \| ospf \| isis \| bgp \| spb-mgmt} {all-routes \| route-map rm}` | 协议间重分发 | `-> ip redist static into ospf all-routes` | 1605 |
| ip route-map action / match / set | `ip route-map name action {permit \| deny}`；`match ip address / tag / metric / route-type ...`；`set metric / tag / local-preference / ip-nexthop ...` | 策略路由与重分发过滤的四级模型 | `-> ip route-map rm1 action permit` | 1612-1650 |
| vrf | `vrf [create] [vrf_name \| default] [profile {max [no-autoload-vrrp] \| low}]`，`no vrf vrf_name` | 默认存在 default VRF | `-> vrf create vrf1` | 1652 |
| ip export / ip import | `[vrf name] ip export {all-routes \| route-map rm \| to-all-vrfs ...}`；`[vrf name] ip import {vrf {src \| default} \| isid id} {all-routes \| route-map rm}` | VRF↔GRT 路由导入导出 | `-> ip import vrf vrf1 all-routes` | 1655/1658 |
| arp | `arp ip_address mac_address [vlan vlan_id]` | 永久 ARP 表项（不老化） | `-> arp 10.0.0.99 00:d0:c0:86:12:07` | 1667 |
| clear arp-cache | `clear arp-cache` | 清全部动态 ARP | `-> clear arp-cache` | 1673 |
| show ip interface / routes | `show ip interface [if_name]` / `show ip routes [ip mask]` | 接口与路由表首查 | `-> show ip routes` | 1719/1729 |
| show ip router database | `show ip router database [protocol type]` | 各协议原始路由库 | `-> show ip router database` | 1742 |

### IPv6（第 22 章）

| 命令 | 语法要点 | 关键参数与默认值 | 典型用法（一行示例） | 页码 |
|---|---|---|---|---|
| ipv6 interface | `ipv6 interface if_name [vlan vlan_id \| loopback loopback_id \| tunnel tunnel_id]`，`no` 删除 | IPv6 路由接口 | `-> ipv6 interface Test vlan 1` | 1795 |
| ipv6 address | `ipv6 address ipv6_address/prefix_length if_name`；eui-64 后缀变体 | — | `-> ipv6 address 2001:db8:4132:86::19a/64 Test_Lab` | 1801 |
| ipv6 static-route | `ipv6 static-route ipv6_prefix/prefix_length gateway {ipv6_address [if_name] \| interface if_name} [metric n]` | — | `-> ipv6 static-route 212:95:5::/64 gateway 2001::205 emp` | 1840 |
| ipv6 neighbor | `ipv6 neighbor ipv6_address hardware_address if_name [port c/s/p]`；`ipv6 neighbor limit count` | limit 默认 6465=64、6560/6570M=128，其他平台不限 | `-> ipv6 neighbor 4132:86::203 00:d0:c0:86:12:07 Test port 1/1/1` | 1827/1831 |
| ipv6 ra-filter | `ipv6 ra-filter if-name [admin-state {enable \| disable}]`；`trusted port/linkagg` 子命令 | RA 防护默认 disabled；端口默认 untrusted | `-> ipv6 ra-filter vlan-23 admin-state enable` | 1849/1851 |
| ipv6 redist / import / export | 同 IPv4 版本结构 | — | `-> ipv6 redist rip into ospf route-map rip-to-ospf1` | 1875/1899/1903 |
| show ipv6 interface / routes / neighbors | `show ipv6 interface [if_name]` / `show ipv6 routes` / `show ipv6 neighbors` | 排障三件套 | `-> show ipv6 routes` | 1950-1977 |

### RIP（第 24 章）

| 命令 | 语法要点 | 关键参数与默认值 | 典型用法（一行示例） | 页码 |
|---|---|---|---|---|
| ip load rip / ipv6 load rip | `ip load rip` / `ipv6 load rip` | 先加载模块（X8） | `-> ip load rip` | 1975/2038 |
| ip rip admin-state | `ip rip admin-state {enable \| disable}` | 全局开关 | `-> ip rip admin-state enable` | 1977 |
| ip rip interface | `ip rip interface if_name`，`no` 删除；子命令 metric/send-version/recv-version/auth-type/auth-key/ingress-filter/egress-filter | 计时器族 update-interval/invalid-timer/garbage-timer/holddown-timer | `-> ip rip interface rip-1 send-version v1` | 1979-2005 |
| ipv6 rip interface | `ipv6 rip interface if_name` + metric/recv-status/send-status/horizon 子命令 | — | `-> ipv6 rip interface Test_Lab send-status enable` | 2047-2056 |
| show ip rip / interface / routes | `show ip rip` / `show ip rip interface [if_name]` / `show ip rip routes` | IPv6 版同构 | `-> show ip rip routes` | 2008-2020 |

### BFD（第 25 章）

| 命令 | 语法要点 | 关键参数与默认值 | 典型用法（一行示例） | 页码 |
|---|---|---|---|---|
| ip bfd admin-state | `ip bfd admin-state {enable \| disable}` | 全局默认 disabled | `-> ip bfd admin-state enable` | 2059 |
| ip bfd transmit / receive / multiplier | `ip bfd {transmit \| receive} interval_ms` / `ip bfd multiplier num` | multiplier 默认 3 | `-> ip bfd transmit 500` | 2061-2065 |
| ip bfd interface | `ip bfd interface if_name`；子命令 admin-state/transmit/receive/multiplier/echo-interval | 接口创建时默认 disabled | `-> ip bfd interface bfd-vlan-101 admin-state enable` | 2069-2077 |
| show ip bfd sessions | `show ip bfd sessions [session_id]`；另有 interfaces/statistics 子命令 | 默认全部会话 | `-> show ip bfd sessions` | 2085-2089 |

### DHCP Relay / Snooping（第 26 章）

| 命令 | 语法要点 | 关键参数与默认值 | 典型用法（一行示例） | 页码 |
|---|---|---|---|---|
| ip dhcp relay admin-state | `ip dhcp relay admin-state {enable \| disable}` | 默认 disabled | `-> ip dhcp relay admin-state enable` | 2095 |
| ip dhcp relay destination | `ip dhcp relay destination ip_address`，`no` 删除 | 全局模式目的服务器 | `-> ip dhcp relay destination 3.3.0.2` | 2097 |
| ip dhcp relay interface destination | `ip dhcp relay interface if_name destination ip_address` | 接口级目的 | `-> ip dhcp relay interface client_traffic destination 75.0.0.10` | 2101 |
| ip dhcp relay maximum-hops | `ip dhcp relay maximum-hops hops` | 默认 16 | `-> ip dhcp relay maximum-hops 10` | 2107 |
| ip dhcp relay insert-agent-information | `ip dhcp relay insert-agent-information`，`no` 关闭 | Option-82 注入，默认 disabled | `-> ip dhcp relay insert-agent-information` | 2109 |
| ip helper address | `ip helper address ip_address`，`no` 删除 | UDP 广播中继（本版本标注 Not supported） | `-> ip helper address 75.0.0.10` | 2131 |
| dhcp-snooping vlan / port | `dhcp-snooping vlan vlan_id admin-state {enable \| disable}`；`dhcp-snooping port c/s/p {block \| client-only \| trust}` | snooping 默认 disabled；端口默认 client-only | `-> dhcp-snooping port 1/1/24 trust` | 2247/2249 |
| show ip dhcp relay statistics | `show ip dhcp relay statistics`；`ip dhcp relay clear statistics` | — | `-> show ip dhcp relay statistics` | 2121/2123 |
| show dhcp-snooping binding | `show dhcp-snooping binding [port ... \| ip-address ... \| snapshot]` | 默认全部绑定表 | `-> show dhcp-snooping binding` | 2293 |

### VRRP（第 27 章）

| 命令 | 语法要点 | 关键参数与默认值 | 典型用法（一行示例） | 页码 |
|---|---|---|---|---|
| ip vrrp（实例） | `ip vrrp vrid interface if_name [address ip] [priority n] [admin-state {enable \| disable}]` | vrid 1-255；先 `ip load vrrp`（X8） | `-> ip vrrp 23 interface ipv4-100 priority 75` | 2335 |
| ip vrrp track | `ip vrrp track track_id [admin-state ...] priority decrement ipv4-interface if_name`；可挂 `address ip bfd-state` | track_id 1-255 | `-> ip vrrp track 2 admin-state enable priority 50 ipv4-interface Marketing` | 2341 |
| ip vrrp bfd-state / preempt / accept | `ip vrrp {bfd-state {enable \| disable} \| preempt \| accept}` | 主备检测与抢占 | `-> ip vrrp bfd-state enable` | 2345-2353 |
| ip vrrp group | `ip vrrp group vrgid [interval centiseconds] [priority n] [preempt] [no accept] [version {v2 \| v3}]`，`no` 删除 | 虚拟路由组模板 | `-> ip vrrp group 25 interval 200 priority 50 no preempt version v3` | 2369 |
| show ip vrrp | `show ip vrrp [vrid]`；另有 statistics/track/track-association/group | — | `-> show ip vrrp` | 2384-2402 |

### OSPF / OSPFv3（第 28-29 章）

| 命令 | 语法要点 | 关键参数与默认值 | 典型用法（一行示例） | 页码 |
|---|---|---|---|---|
| ip load ospf | `ip load ospf` | 先加载（X8） | `-> ip load ospf` | 2394 |
| ip ospf admin-state | `ip ospf admin-state {enable \| disable}` | — | `-> ip ospf admin-state enable` | 2396 |
| ip ospf spf-timer | `ip ospf spf-timer [delay seconds] [hold seconds]` | 0-65535，默认 delay=5/hold=10；任一为 0 立即触发 SPF（P18）；平台 6360/6465 No | `-> ip ospf spf-timer delay 20 hold 35` | 2409 |
| ip ospf interface | `ip ospf interface if_name`；子命令 admin-state/area/auth-type/auth-key/md5/type/cost/priority/poll-interval/retrans-interval/transit-delay | 接口入 OSPF | `-> ip ospf interface vlan-101 area 0.0.0.1` | 2430/2438 |
| ip ospf interface hello-interval / dead-interval | `ip ospf interface if_name {hello-interval \| dead-interval} seconds` | hello 默认 broadcast/P2P=10、NBMA/P2MP=30；hello=0 即被动接口（X23）；平台 6360/6465 No | `-> ip ospf interface vlan-101 hello-interval 50` | 2434 |
| ip ospf area | `ip ospf area area_id [type {normal \| stub \| nssa}] [summary {enable \| disable}]`；`range summary ip mask` 汇总 | — | `-> ip ospf area 0.0.0.1 type stub` | 2418/2424 |
| ip ospf default-originate | `ip ospf default-originate {always \| only} [metric n] [metric-type type1\|type2]` | 注入默认路由 | `-> ip ospf default-originate always` | 2410 |
| ip ospf bfd-state | `ip ospf bfd-state {enable \| disable}`；`all-interfaces`；接口级 `drs-only`/`all-neighbors` | 需先开 BFD | `-> ip ospf bfd-state enable` | 2470-2482 |
| ip ospf restart-support | `ip ospf restart-support {planned-unplanned ...}` | GR 默认 disabled；helper 默认启用 | `-> ip ospf restart-support planned-unplanned` | 2485 |
| show ip ospf neighbor / lsdb / routes / interface | `show ip ospf neighbor [ip]` / `lsdb [area ...]` / `routes` / `interface [if]` | 邻居/LSDB/路由/接口四件套 | `-> show ip ospf neighbor` | 2451-2484 |
| ipv6 load ospf + 接口族 | `ipv6 load ospf`；`ipv6 ospf interface if_name [area id] [hello-interval/dead-interval/cost/priority/type ...]` | OSPFv3 同构 | `-> ipv6 ospf interface vlan-101 area 0.0.0.1` | 2515+ |
| show ipv6 ospf | `show ipv6 ospf [neighbor \| lsdb \| routes \| interface ...]` | — | `-> show ipv6 ospf neighbor` | 2589+ |

### IS-IS（第 30 章）

| 命令 | 语法要点 | 关键参数与默认值 | 典型用法（一行示例） | 页码 |
|---|---|---|---|---|
| ip load isis / ip isis admin-state | `ip load isis` → `ip isis admin-state {enable \| disable}` | 默认未加载（X8） | `-> ip load isis` | 2613/2614 |
| ip isis area-id | `ip isis area-id area_address`，`no` 删除 | 区域地址如 49.0001 | `-> ip isis area-id 49.0001` | 2616 |
| ip isis level-capability | `ip isis level-capability {level-1 \| level-2 \| level-1/2}` | — | `-> ip isis level-capability level-2` | 2618 |
| ip isis vlan | `ip isis vlan vlan_id [address-family {v4 \| v6 \| v4v6}]` | 地址族默认 disabled | `-> ip isis vlan 10 address-family v4v6` | 2660 |
| ip isis vlan level hello-interval / metric | `ip isis vlan vlan_id level {1 \| 2} {hello-interval seconds \| metric number}` | — | `-> ip isis vlan 10 level 1 metric 25` | 2681/2685 |
| ip isis overload / graceful-restart | `ip isis overload [timeout seconds]` / `ip isis graceful-restart` | overload 默认 disabled；GR 默认 disabled | `-> ip isis overload timeout 70` | 2638/2642 |
| ip isis summary-address | `ip isis summary-address ip_prefix/mask {level-1 \| level-2 \| level-1/2}` | 区域路由汇总 | `-> ip isis summary-address 10.0.0.0/8 level-2` | 2636 |
| show ip isis adjacency / database / routes | `show ip isis adjacency [system-id ...] [detail]` / `database [system_id ...] [detail] [level {1\|2}]` / `routes` | 邻接/LSDB/路由 | `-> show ip isis adjacency` | 2699/2703/2710 |

### BGP（第 31 章，194 条）

| 命令 | 语法要点 | 关键参数与默认值 | 典型用法（一行示例） | 页码 |
|---|---|---|---|---|
| ip load bgp / ip bgp admin-state | `ip load bgp` → `ip bgp admin-state {enable \| disable}` | 先加载再启用（X8） | `-> ip load bgp` | 2749/2751 |
| ip bgp autonomous-system | `ip bgp autonomous-system as_num` | 本端 AS 号 | `-> ip bgp autonomous-system 64724` | 2753 |
| ip bgp default local-preference | `ip bgp default local-preference value` | 平台 6360/6465/6575 No（X3） | `-> ip bgp default local-preference 200` | 2759 |
| ip bgp maximum-paths | `ip bgp maximum-paths`，`no` 关闭 | ECMP，默认 disabled；启用要求先停 BGP（P22）；平台同上 No | `-> ip bgp maximum-paths` | 2775 |
| ip bgp dampening | `ip bgp dampening [half-life h reuse r suppress s max-suppress-time m]` | 路由抖动抑制，默认 disabled | `-> ip bgp dampening half-life 15 reuse 750 suppress 3000` | 2779 |
| ip bgp network | `ip bgp network ip_address [mask m] [metric n] [community ...] [local-preference ...]` | 宣告本地已知网络 | `-> ip bgp network 10.1.0.0` | 2799 |
| ip bgp aggregate-address | `ip bgp aggregate-address ip_address mask [as-set] [summary-only] [community ...]` | 聚合路由 | `-> ip bgp aggregate-address 172.22.0.0 255.255.0.0 summary-only` | 2785 |
| ip bgp neighbor | `ip bgp neighbor ip_address`，`no` 删除 | 创建对等体，默认无 peer | `-> ip bgp neighbor 172.22.2.115` | 2809 |
| ip bgp neighbor remote-as | `ip bgp neighbor ip_address remote-as value` | 对端 AS | `-> ip bgp neighbor 172.22.2.115 remote-as 65000` | 2843 |
| ip bgp neighbor timers | `ip bgp neighbor ip_address timers keepalive holdtime` | KEEPALIVE/保持时间（秒） | `-> ip bgp neighbor 172.22.2.115 timers 10 30` | 2825 |
| ip bgp neighbor route-map | `ip bgp neighbor ip_address route-map {name \| none} {in \| out}`，`no` 移除 | 邻居策略 | `-> ip bgp neighbor 172.22.2.115 route-map InboundRoute in` | 2871 |
| ip bgp neighbor next-hop-self | `ip bgp neighbor ip_address next-hop-self`，`no` 关闭 | 默认 disabled | `-> ip bgp neighbor 172.22.2.115 next-hop-self` | 2839 |
| ip bgp neighbor 其他常用 | `description / md5 key / ebgp-multihop / update-source / maximum-prefix / default-originate / passive / soft-reconfiguration / route-reflector-client` | 见各条目 | `-> ip bgp neighbor 1.1.1.1 ebgp-multihop` | 2809-2873 |
| ip bgp policy 族 | `ip bgp policy {aspath-list / community-list / prefix-list / prefix6-list / route-map} ...` | BGP 专用策略对象（match/set 动作族） | `-> ip bgp policy route-map rm1 action permit` | 2892-2959 |
| ipv6 bgp neighbor / network | `ipv6 bgp neighbor ipv6_address` / `ipv6 bgp network prefix` + remote-as/timers 等同构子命令 | MP-BGP for IPv6 | `-> ipv6 bgp neighbor 2001::1 remote-as 65000` | 3071/3059 |
| ip bgp address-family evpn | `ip bgp address-family evpn`，`no` 关闭 | EVPN 地址族默认 disabled；配 `neighbor activate-evpn` 联动 | `-> ip bgp address-family evpn` | 3019 |
| ip bgp graceful-restart | `ip bgp graceful-restart`，`no` 关闭 | GR 默认 enabled | `-> ip bgp graceful-restart` | 3013 |
| show ip bgp / routes / neighbors | `show ip bgp` / `show ip bgp routes [ip mask]` / `show ip bgp neighbors [ip] [policy \| timer \| statistics]` | 全局/路由/邻居三件套 | `-> show ip bgp neighbors` | 2961/2975/2981 |

### SLB（第 32 章）

| 命令 | 语法要点 | 关键参数与默认值 | 典型用法（一行示例） | 页码 |
|---|---|---|---|---|
| ip slb admin-state | `ip slb admin-state {enable \| disable}` | — | `-> ip slb admin-state enable` | 3161 |
| ip slb cluster | `ip slb cluster name vip ip_address`，`no` 删除；子命令 admin-state/hashing/ping period-timeout-retries/probe/wait-to-restore | 集群创建即 admin enable；wait-to-restore 默认 0 | `-> ip slb cluster corporate_servers vip 1.2.3.4` | 3165 |
| ip slb server ip cluster | `ip slb server ip ip_address cluster cluster_name [admin-state ...]` | 实服务器入组 | `-> ip slb server ip 10.255.11.127 cluster corporate_servers` | 3181 |
| ip slb probe | `ip slb probe probe_name {ftp \| http \| smtp \| tcp \| udp} ...`；timeout/period/port/retries/url/expect 子参数 | 健康检查 | `-> ip slb probe mail_server_probe smtp` | 3188 |
| show ip slb | `show ip slb [clusters \| cluster name \| servers \| probes]` | — | `-> show ip slb clusters statistics` | 3221-3232 |

## E（实证案例）
- 命令地图型 skill，不搬运案例；原书每条命令自带 Example，按章首页码回查（cases 原件未创建）

## B（反例/坑）
- 路由协议命令生效前需 `ip load <protocol>` 加载模块（X8，第 24/27/28/30/31 章）
- `ip ospf spf-timer`/`hello-interval` 平台：6360/6465 不支持，6560 起支持（X2，<<<PAGE 2409>>>/<<<PAGE 2434>>>）
- `ip ospf interface hello-interval` 设 0 的语义是创建被动接口（不发 hello），并非更快收敛（X23，<<<PAGE 2434>>>）
- `ip bgp default local-preference`/`maximum-paths` 平台：6360/6465/6575 不支持（X3，<<<PAGE 2759>>>/<<<PAGE 2776>>>）
- `ip bgp maximum-paths` 同样要求先停 BGP 再配（P22）

## 来源
OmniSwitch AOS Release 810R04 CLI Reference User Guide 第 21-32 章（<<<PAGE 1549-3227>>>）。条目来源：principles P16-P22；counter-examples X2/X3/X8/X23；frameworks F6。
