---
name: AOS 8 CLI 命令地图——Fabric 骨干域（SPB/MPLS/Service Manager，第 9-11 章）
description: 需要在 OmniSwitch AOS 8 上配置 SPB 骨干（ISIS-SPB/BVLAN/ECT）、SPBM 服务（ISID/SAP/PBB）、MPLS LSP/VPN，或查 spb/mpls 命令语法与平台支持时使用。含 MPLS/LDP、SPB 骨干、SPBM 服务三层核心命令速查表（A3，60+ 条语法/默认值/示例/页码）。
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

## A3（核心命令速查）

以下语法/默认值/示例均摘自原书第 9-11 章对应条目，页码为 fulltext `<<<PAGE N>>>` 标记值。`{enable | disable}` 等花括号取值表示"多选一"。

### MPLS / LDP（第 9 章）

| 命令 | 语法要点 | 关键参数与默认值 | 典型用法（一行示例） | 页码 |
|---|---|---|---|---|
| mpls interface | `mpls interface if_name [admin-state {enable \| disable}]`，`no` 删除 | 创建时默认 admin disable；if_name 为已存在的 VLAN/IP 接口 | `-> mpls interface vlan10` | 691 |
| mpls load ldp | `mpls load ldp` | 无参数；所有 `mpls ldp` 命令的前置条件 | `-> mpls load ldp` | 707 |
| mpls ldp admin-state | `mpls ldp admin-state [{enable \| disable}]` | 全局启停 LDP | `-> mpls ldp admin-state enable` | 709 |
| mpls ldp | `mpls ldp [hello-interval seconds] [hold-time seconds] [keepalive-interval seconds] [keepalive-timeout seconds]` | hello=5、hold=15、keepalive-interval=10（秒）；hold-time ≥ 3×hello，keepalive-timeout ≥ 3×keepalive-interval；区间 hello 1-21845、hold 3-65535 | `-> mpls ldp hello-interval 10 hold-time 30` | 711 |
| mpls ldp interface | `mpls ldp interface if_name [admin-state {enable \| disable}]`，计时器子参数同上 | 接口级 hello/hold/keepalive，默认值同全局 | `-> mpls ldp interface vlan10 admin-state enable` | 713/715 |
| mpls ldp session-protection | `mpls ldp session-protection [admin-state {enable \| disable}]` | 默认按平台/版本 | `-> mpls ldp session-protection admin-state enable` | 717 |
| mpls ldp graceful-restart | `mpls ldp graceful-restart [maximum-recovery-time seconds] [neighbor-liveness-time seconds]`，`no` 关闭 | 默认 graceful restart 连同 helper 模式启用 | `-> mpls ldp graceful-restart maximum-recovery-time 200 neighbor-liveness-time 150` | 719 |
| mpls ldp neighbor | `mpls ldp neighbor peer_address md5 key {key \| none}` | key 为 MD5 认证密钥字符串，none 表示清除 | `-> mpls ldp neighbor 5.5.5.5 md5 key testkey1` | 721 |
| mpls ping ldp | `mpls ping ldp fec_prefix [destination ip_address] [source ip_address] [timeout seconds] [repeat count]` | fec_prefix 为目标前缀（如 1.1.1.4/32） | `-> mpls ping ldp 1.1.1.4/32` | 740 |
| mpls trace ldp | `mpls trace ldp fec_prefix [destination ip_address] [source ip_address] [timeout seconds]` | 逐跳追踪 LSP | `-> mpls trace ldp 1.1.1.4/32` | 741 |
| show mpls | `show mpls` | 无参数，MPLS 全局概览 | `-> show mpls` | 693 |
| show mpls interface | `show mpls interface` | 全部 MPLS 接口 | `-> show mpls interface` | 695 |
| show mpls ftn-table | `show mpls ftn-table` | FEC-to-NHLFT 标签映射表 | `-> show mpls ftn-table` | 697 |
| show mpls ilm-table | `show mpls ilm-table` | 入标签映射表 | `-> show mpls ilm-table` | 699 |
| show mpls forwarding-table | `show mpls forwarding-table` | 标签转发综合表 | `-> show mpls forwarding-table` | 701 |
| show mpls vpls mesh | `show mpls vpls mesh` | VPLS mesh 绑定 | `-> show mpls vpls mesh` | 703 |
| show mpls vpws vc-table | `show mpls vpws vc-table` | VPWS 虚电路表 | `-> show mpls vpws vc-table` | 704 |
| show mpls ldp | `show mpls ldp` | LDP 全局状态 | `-> show mpls ldp` | 725 |
| show mpls ldp interface | `show mpls ldp interface [if_name]` | 可按接口过滤 | `-> show mpls ldp interface vlan10` | 726 |
| show mpls ldp neighbor | `show mpls ldp neighbor` | 邻居与会话概览 | `-> show mpls ldp neighbor` | 729 |
| show mpls ldp session | `show mpls ldp session [peer_address]`；另有 `rx-addresses/rx-labels/tx-labels peer_address` | 可查每个方向的地址与标签 | `-> show mpls ldp session 5.5.5.5` | 730/732-737 |

### SPB 骨干（ISIS-SPB / BVLAN，第 10 章）

| 命令 | 语法要点 | 关键参数与默认值 | 典型用法（一行示例） | 页码 |
|---|---|---|---|---|
| spb bvlan | `spb bvlan {bvlan_id[-bvlan_id2]} [admin-state {enable \| disable}] [name description]`，`no spb bvlan bvlan_id` | bvlan_id 1-4094，支持区间（10-20）；默认 enable；平台：6360/6465/6560 为 No | `-> spb bvlan 200 name BVLAN-200` | 745 |
| spb isis bvlan ect-id | `spb isis bvlan bvlan_id ect-id ect_id` | ect_id 1-16；默认自动分配下一个可用 ECT；bvlan 须已存在 | `-> spb isis bvlan 200 ect-id 5` | 747 |
| spb isis control-bvlan | `spb isis control-bvlan bvlan_id` | 指定控制面 BVLAN；无默认 | `-> spb isis control-bvlan 200` | 749 |
| spb isis bvlan tandem-multicast-mode | `spb isis bvlan bvlan_id tandem-multicast-mode {sgmode \| gmode}` | 默认 sgmode（(S,G) 模式） | `-> spb isis bvlan 200 tandem-multicast-mode gmode` | 751 |
| spb isis bridge-priority | `spb isis bridge-priority priority` | 默认 32768，越小越优；占 8 字节 Bridge ID 高 2 字节 | `-> spb isis bridge-priority 15` | 753 |
| spb isis interface | `spb isis interface {port chassis/slot/port[-port2] \| linkagg agg_id} [admin-state {enable \| disable}] [hello-interval seconds] [hello-multiplier count] [metric metric] [type {p2p \| multi-access}] [priority priority]` | 默认 enable、hello=9(p2p)/3(multi-access)、multiplier=3、metric=10、type=p2p；metric 取链路两端较大值 | `-> spb isis interface port 1/4/7 hello-interval 60` | 755 |
| spb isis admin-state | `spb isis admin-state {enable \| disable}` | 全局启停 ISIS-SPB；启用后所有 SPB 接口开始发 hello | `-> spb isis admin-state enable` | 779 |
| spb isis area-address | `spb isis area-address area_address` | 默认 0.0.0（ISIS-SPB 常用值）；全网须一致 | `-> spb isis area-address 1.1.1` | 781 |
| spb isis source-id | `spb isis source-id {source_id \| auto}` | 默认取 system ID 低 3 字节；格式如 00-2a-1d | `-> spb isis source-id auto` | 783 |
| spb isis control-address | `spb isis control-address {alll1 \| alll2 \| allis}` | 默认 AllL1 | `-> spb isis control-address alll1` | 785 |
| spb isis spf-wait | `spb isis spf-wait [initial-wait ms \| second-wait ms \| max-wait ms]` | 默认 initial=100、second=300、max=1000（毫秒）；平台：6360/6465 为 No | `-> spb isis spf-wait max-wait 2500 initial-wait 1000` | 787 |
| spb isis lsp-wait | `spb isis lsp-wait {max-wait ms \| initial-wait ms \| second-wait ms}` | 默认 initial=0、second/max 见原书表（P789） | `-> spb isis lsp-wait max-wait 2000 initial-wait 1000` | 789 |
| spb isis rapid-lsp-converge | `spb isis rapid-lsp-converge {isid instance_id \| admin-state {enable \| disable}}` | 默认启用，I-SID 默认 16776961（255.255.1） | `-> spb isis rapid-lsp-converge isid 4001` | 791 |
| spb isis overload | `spb isis overload [timeout seconds]`，`no` 撤销 | 默认禁用；timeout 后自动退出 overload | `-> spb isis overload timeout 70` | 793 |
| spb isis overload-on-boot | `spb isis overload-on-boot [timeout seconds]` | 默认重启后不进入 overload | `-> spb isis overload-on-boot timeout 80` | 795 |
| spb isis graceful-restart | `spb isis graceful-restart`，`no` 关闭 | 默认启用 | `-> spb isis graceful-restart` | 797 |
| spb isis graceful-restart helper | `spb isis graceful-restart helper {enable \| disable}` | helper 邻居侧辅助 | `-> spb isis graceful-restart helper disable` | 799 |
| spb ipvpn bind | `spb ipvpn bind vrf {vrf_name \| default} isid instance_id gateway ip_address [import-route-map rm] [export-route-map rm]` | VRF/ISID/网关须已存在 | `-> spb ipvpn bind vrf1 isid 1000 gateway 10.1.1.1 all-routes` | 759 |
| spb ipvpn redist | `spb ipvpn redist {source-isid ... destination-isid ... {all-routes \| route-map rm} \| source-vrf vrf_name destination-isid ...}` | all-routes 为默认 | `-> spb ipvpn redist source-isid 1000 destination-isid 2000 all-routes` | 761 |
| spb ipvpn6 bind / redist | 同 v4 版本，gateway 为 IPv6 | 同上 | `-> spb ipvpn6 bind vrf1 isid 1000 gateway 1000::1 all-routes` | 769/771 |
| show spb isis info | `show spb isis info` | ISIS-SPB 全局状态首查命令 | `-> show spb isis info` | 801 |
| show spb isis bvlans | `show spb isis bvlans` | BVLAN 配置一览 | `-> show spb isis bvlans` | 804 |
| show spb isis interface | `show spb isis interface [port chassis/slot/port \| linkagg id]` | 默认显示摘要 | `-> show spb isis interface` | 806 |
| show spb isis adjacency | `show spb isis adjacency [detail]` | 邻接排障第一入口；默认摘要 | `-> show spb isis adjacency` | 809 |
| show spb isis database | `show spb isis database [lsp-id lsp_id] [detail]` | 默认显示整个 LSDB | `-> show spb isis database` | 812 |
| show spb isis nodes | `show spb isis nodes` | 全网 SPB 节点（BMAC/SYSID） | `-> show spb isis nodes` | 819 |
| show spb isis unicast-table | `show spb isis unicast-table [bvlan bvlan_id]` | 单播转发表 | `-> show spb isis unicast-table` | 821 |
| show spb isis services | `show spb isis services [isid instance_id]` | I-SID 映射 | `-> show spb isis services` | 823 |
| show spb isis spf | `show spb isis spf bvlan bvlan_id [bmac mac_address]` | 指定 BVLAN 的 SPT | `-> show spb isis spf bvlan 4001` | 825 |
| show spb isis multicast-table | `show spb isis multicast-table [isid instance_id]` | 组播转发表 | `-> show spb isis multicast-table` | 827 |
| show spb ipvpn bind/redist/route-table | `show spb ipvpn bind [vrf ...]` / `redist` / `route-table [isid id]` | 默认显示全部；IPv6 版 `ipvpn6` 同构 | `-> show spb ipvpn route-table` | 763-768/773-778 |

### SPBM 服务层（Service Manager，第 11 章）

| 命令 | 语法要点 | 关键参数与默认值 | 典型用法（一行示例） | 页码 |
|---|---|---|---|---|
| service spb | `service service_id[-id2] spb isid instance_id[-id2] bvlan bvlan_id[:x] [admin-state ...] [multicast-mode {head-end \| tandem \| hybrid}] [description ...]` | service_id 唯一编号；支持区间批量 | `-> service 100 spb isid 1000 bvlan 4001` | 843 |
| service vxlan | `service service_id[-id2] vxlan vnid {vxlan_id[-id2] \| vlan-id vlan_id[:x]} [multicast-mode ...] [description ...]` | 默认 hybrid 组播模式 | `-> service 10 vxlan vnid 1000 description "VxLAN service for VNID 1000"` | 847 |
| service l2gre | `service service_id l2gre vpnid vpn_id [description ...] [admin-state ...] [vlan-xlation ...] [remove-ingress-tag ...]` | — | `-> service 10 l2gre vpnid 1000` | 851 |
| service vpls | `service service_id vpls vplsid vpls_id signaling {ldp \| bgp} [ve-id id] [admin-state ...]` | signaling 必选 | `-> service 1 vpls vplsid 100 signaling ldp` | 854 |
| service vpws | `service service_id vpws vcid vc_id [description ...] [admin-state ...]` | — | `-> service 2 vpws vcid 200 admin-state enable` | 857 |
| service pseudo-wire | `service service_id pseudo-wire {enable \| disable}` | SPB 服务默认 mp2p（E-LAN），pw 用于 p2p | `-> service 100 spb isid 1000 bvlan 4000 pseudo-wire enable` | 862 |
| service admin-state | `service service_id admin-state {enable \| disable}` | 创建时默认 disable | `-> service 100 admin-state enable` | 874 |
| service multicast-mode | `service service_id multicast-mode {head-end \| tandem \| hybrid}` | SPB/VPLS/VPWS 默认 head-end，VXLAN 默认 hybrid | `-> service 100 multicast-mode hybrid` | 867 |
| service stats | `service service_id stats {enable \| disable}` | 默认 disabled | `-> service 100 stats enable` | 870 |
| service sap | `service service_id sap {port chassis/slot/port[-p2][:vlan[.vlan2] \| :all] \| linkagg id:...} [admin-state ...] [description ...]` | SAP 创建时默认 admin enable、trusted、stats disable；`:0` 无标签、`:50` 单 VLAN、`:100.200` QinQ | `-> service 100 sap port 1/1/1:50` | 930 |
| service sap trusted | `service service_id sap {port ...} {trusted \| un-trusted} [priority 0-7]` | 默认 trusted、priority=0（best effort） | `-> service 10 sap port 1/1/2:10 trusted` | 936 |
| service sdp vxlan | `service sdp sdp_id vxlan {far-end ip_address \| multicast-group ip_address} [ttl {ttl_num \| default}] [admin-state ...] [description ...]` | VXLAN 隧道端点（VTEP）定义 | `-> service sdp 10 vxlan multicast-group 224.2.1.1 ttl 20` | 943 |
| service sdp l2gre | `service sdp sdp_id l2gre far-end ip_address [ttl ...] [admin-state ...]` | — | `-> service sdp 20 l2gre far-end 192.168.0.10 admin-state enable` | 946 |
| service sdp mpls | `service sdp sdp_id mpls far-end ip_address [description ...] [admin-state ...]` | — | `-> service sdp 20 mpls far-end 10.10.10.2` | 948 |
| service bind-sdp | `service service_id bind-sdp sdp_id1 [sdp_id2 ...] [spoke] [description ...]`，`no` 解绑 | 将服务绑定到 SDP 隧道 | `-> service 1 bind-sdp 10` | 950 |
| service vxlan udp-port | `service vxlan udp-port {udp_port_num \| default}` | 默认 4789（default VRF） | `-> service vxlan udp-port 8472` | 898 |
| service l2gre reserved-vlan | `service l2gre reserved-vlan vlan_id[-id2]` | 默认无保留 VLAN | `-> service l2gre reserved-vlan 4000` | 912 |
| service bgp-evpn | `vrf vrf_name service service_id ... bgp-evpn enable`（随服务创建，见 EX） | 默认 disabled；当前支持 VXLAN 服务 | `-> vrf vrf1 service 101 vxlan vnid 101 bgp-evpn enable` | 859 |
| service bgp-evpn route-target | `service service_id bgp-evpn route-target {import \| export \| both} rt` | 默认 auto-RT（2 字节全局:4 字节本地） | `-> vrf vrf1 service 1 bgp-evpn route-target both 68000:9999` | 896 |
| show service | `show service [spb \| vxlan \| l2gre \| vpls \| vpws \| evpn \| service_id]` | 默认列出全部服务 | `-> show service` | 966 |
| show service ports | `show service {service_id \| vnid id \| vpnid id \| isid id} ports` | 按业务键查端口 | `-> show service 100 ports` | 977 |
| show service access | `show service access [port ... \| linkagg ...] [sap]` | 默认全部接入端口 | `-> show service access` | 963 |
| show service spb sap | `show service spb service_id sap {port chassis/slot/port}` | SPB 服务 SAP 明细 | `-> show service spb 525 sap port 1/11:2524` | 982 |
| show service sdp | `show service sdp [sdp_id]`；分类型子命令 `sdp spb/vxlan/l2gre/mpls` | 默认全部 SDP | `-> show service sdp vxlan` | 991-1005 |
| show service bind-sdp | `show service bind-sdp [sdp_id[:service_id]]`；分类型 spb/vxlan/l2gre/vpls/vpws | 默认全部绑定 | `-> show service bind-sdp` | 1006-1021 |
| show service counters | `show service {service_id \| vnid id \| vpnid id \| isid id} counters` | 需先 `service stats enable` | `-> show service 20 counters` | 1059 |
| clear service counters | `clear service [service_id] [sap {port ...}] counters` | 默认清除指定服务全部计数 | `-> clear service 100 counters` | 1062 |
| show service info | `show service info` | 服务管理全局信息（UDP 端口等） | `-> show service info` | 1033 |
| show service evpn evi | `vrf vrf_name show service evpn [evi evi_id [ethernet-segment-info]]` | EVPN 实例状态 | `-> vrf vrf1 show service evpn evi 780` | 1041 |
| show service evpn ethernet-segment | `show service evpn ethernet-segment [{esi_id [aliasing-info \| remote]}]` | ES/多归属状态 | `-> vrf vrf1 show service evpn ethernet-segment` | 1046 |

## E（实证案例）
- 命令地图型 skill，不搬运案例；原书每条命令自带 Example，按章首页码回查（cases 原件未创建）

## B（反例/坑）
- BVLAN 平台支持：仅 6570M/6860/6860N/6865/6870/6900/6575/6920/9900；6360/6465/6560 为 No（X1，<<<PAGE 745>>>）
- 每台 SPB 桥的 BVLAN 配置必须完全一致，否则 ISIS-SPB 邻居发现与最短路径计算失败（X17，<<<PAGE 745>>>）
- 同一 ISID 不能既绑定又重分发到同一 VRF 实例（X11）

## 来源
OmniSwitch AOS Release 810R04 CLI Reference User Guide 第 9 章（<<<PAGE 689>>>）、第 10 章（<<<PAGE 743>>>）、第 11 章（<<<PAGE 839>>>）。条目来源：principles P11-P15；counter-examples X1/X11/X17；frameworks F4。
