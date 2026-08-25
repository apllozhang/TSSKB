# frameworks — 命令域地图（F1…F11）

来源：《OmniSwitch AOS Release 8.10R4 CLI Reference Guide》，页码为全文 `<<<PAGE N>>>` 标记。70 章归入 11 个命令域，形成"域 → 章 → 命令"三级导航。

## F1 端口与 PoE（基础连接层）
- 覆盖：第 1 章 Ethernet Port（<<<PAGE 67>>>，85 条）、第 2 章 PoE（<<<PAGE 254>>>，38 条）、第 3 章 UDLD（<<<PAGE 327>>>，12 条）
- 核心命令族：`interfaces`（speed/duplex/fec/break-out/ddm 等 30+ 子命令）、`lanpower`（PoE 供电/预算/分级）、`udld` 单向链路检测
- 页码区间：67–351

## F2 二层与 VLAN
- 覆盖：第 4 章 Source Learning（<<<PAGE 351>>>）、第 5 章 VLAN Management（<<<PAGE 427>>>）、第 6 章 High Availability VLAN（<<<PAGE 455>>>）、第 7 章 VLAN Stacking（<<<PAGE 476>>>）、第 17 章 MVRP（<<<PAGE 1340>>>）
- 核心命令族：`vlan`/`vlan members`/`pvlan`、`mac-address-table`、`vlan stacking`（QinQ）、`mvrp` 动态 VLAN 注册
- 页码区间：351–567 与 1340–1390

## F3 冗余与环网保护
- 覆盖：第 8 章 Distributed Spanning Tree（<<<PAGE 567>>>）、第 12 章 Loopback Detection（<<<PAGE 1070>>>）、第 13 章 Link Aggregation（<<<PAGE 1092>>>）、第 15 章 Ethernet Ring Protection（<<<PAGE 1268>>>）、第 16 章 MRP（<<<PAGE 1306>>>）
- 核心命令族：`spanty`/`bridge`、`linkagg`、`loopback-detection`、`erp`/`mrp` 环网倒换
- 页码区间：567–689 与 1070–1268 与 1306–1340

## F4 SPB/MPLS 骨干与服务（PBB 骨干）
- 覆盖：第 9 章 MPLS（<<<PAGE 689>>>）、第 10 章 Shortest Path Bridging（<<<PAGE 743>>>）、第 11 章 Service Manager（<<<PAGE 839>>>）
- 核心命令族：`spb isis`（区域/桥优先级/BVLAN/ECT）、`spbm` 服务（ISID/SAP 绑定）、`mpls` LSP 与 VPN
- 页码区间：689–1070；第 10 章（ISIS-SPB 骨干）与第 11 章（SPBM 服务层）互为控制面/数据面配套
- 关键结构：SPBM = PBB（802.1ah MAC-in-MAC）封装 + ISIS-SPB 最短路径树，分 backbone（控制面）与 services（数据面）两层

## F5 VC/自动织构与数据中心
- 覆盖：第 14 章 Virtual Chassis（<<<PAGE 1198>>>）、第 19 章 SIP（<<<PAGE 1486>>>，域归属待确认）、第 20 章 Automatic Fabric（<<<PAGE 1523>>>）、第 45 章 FIP Snooping（<<<PAGE 5039>>>）、第 46 章 FCoE/FC Gateway（<<<PAGE 5090>>>）、第 47 章 VXLAN Snooping（<<<PAGE 5152>>>）、第 48 章 Port Mapping（<<<PAGE 5195>>>）
- 核心命令族：`virtual-chassis`（VFL/chassis group）、`fabric`/`auto-fabric`、FCoE/VXLAN 侦听与映射
- 页码区间：1198–1268 与 1486–1549 与 5039–5212

## F6 IP 与路由（单播路由与服务）
- 覆盖：第 21 章 IP（<<<PAGE 1549>>>）、第 22 章 IPv6（<<<PAGE 1793>>>）、第 24 章 RIP（<<<PAGE 1974>>>）、第 25 章 BFD（<<<PAGE 2058>>>）、第 26 章 DHCP Relay（<<<PAGE 2092>>>）、第 27 章 VRRP（<<<PAGE 2334>>>）、第 28 章 OSPF（<<<PAGE 2392>>>）、第 29 章 OSPFv3（<<<PAGE 2513>>>）、第 30 章 IS-IS（<<<PAGE 2610>>>）、第 31 章 BGP（<<<PAGE 2744>>>）、第 32 章 SLB（<<<PAGE 3160>>>）
- 核心命令族：`ip interface`/`ip route`、`ip ospf`、`ip bgp`（194 条，全书第二大章）、`ip vrrp`、`ip rip`、`ipv6`、`bootp relay`、`ip bfd`、`slb`
- 页码区间：1549–3227（本书体量最大的域）
- 关键结构：路由命令普遍要求 `ip load <protocol>` 先加载协议模块；全局参数类命令多处要求先停协议（见 X 条目）

## F7 组播
- 覆盖：第 33 章 IP Multicast Switching（<<<PAGE 3227>>>）、第 34 章 IP Multicast VLAN（<<<PAGE 3471>>>）、第 35 章 DVMRP（<<<PAGE 3495>>>）、第 36 章 PIM（<<<PAGE 3542>>>）、第 37 章 Multicast Routing（<<<PAGE 3769>>>）
- 核心命令族：`ip msdp`? 否——AOS 为 `mcs`/`ip igmp`/`ip pim`/`ip dvmrp`/`mvr`（组播 VLAN 注册）
- 页码区间：3227–3797
- 关键结构：三层组播（PIM/DVMRP/IGMP）与二层组播交换（MCS/MVR）分层

## F8 安全与准入
- 覆盖：第 23 章 IPsec（<<<PAGE 1948>>>）、第 41 章 AAA（<<<PAGE 4205>>>）、第 42 章 Access Guardian（<<<PAGE 4470>>>，199 条，全书第一大章）、第 49 章 Learned Port Security（<<<PAGE 5212>>>）、第 58 章 PPPoE Intermediate Agent（<<<PAGE 5571>>>）
- 核心命令族：`unp`（UNP profile/port/domain/redirect）、`aaa`/`radius`/`tacacs`、`lps`、`ipsec`、`pppoe ia`
- 页码区间：1948–1974 与 4205–4470 与 5212–5256 与 5571–5597
- 关键结构：Access Guardian 以 UNP（Universal Network Profile）为框架，联动 AAA（第 41 章）与 LPS（第 49 章）

## F9 监测与 OAM
- 覆盖：第 18 章 802.1AB/LLDP（<<<PAGE 1390>>>）、第 50 章 Port Mirroring（<<<PAGE 5256>>>）、第 51 章 sFlow（<<<PAGE 5277>>>）、第 52 章 RMON（<<<PAGE 5305>>>）、第 54 章 Health Monitoring（<<<PAGE 5347>>>）、第 55 章 Ethernet OAM/CFM（<<<PAGE 5358>>>）、第 56 章 LINK OAM（<<<PAGE 5432>>>）、第 57 章 CPE Test Head（<<<PAGE 5503>>>）、第 59 章 Service Assurance Agent（<<<PAGE 5597>>>）
- 核心命令族：`lldp`、`ports mirror`、`sflow`、`rmon`、`ethernet-oam`（802.3ah）、`cfm`（802.1ag）、`saa`
- 页码区间：1390–1486 与 5256–5358 与 5432–5645

## F10 QoS 与策略
- 覆盖：第 38 章 QoS（<<<PAGE 3797>>>）、第 39 章 QoS Policy（<<<PAGE 3953>>>）、第 40 章 Policy Server（<<<PAGE 4190>>>）、第 43 章 Application Monitoring and Enforcement（<<<PAGE 4934>>>）、第 44 章 Application Fingerprinting（<<<PAGE 5016>>>）
- 核心命令族：`policy condition`/`policy action`/`policy rule`/`policy list`（条件-动作-规则-列表四级模型）、group 类命令（network/mac/port/vlan/service group）、QoS 硬件队列参数、AppMon 应用识别
- 页码区间：3797–4205 与 4934–5039
- 关键结构：策略=条件+动作；规则经 `policy rule` 绑定 condition 与 action，再经 `policy list` 编排；条件子命令 40+（ip/port/vlan/mac/dscp/app-mon 等）

## F11 系统与管理
- 覆盖：第 53 章 Switch Logging（<<<PAGE 5313>>>）、第 60 章 CMM（<<<PAGE 5645>>>）、第 61 章 Chassis Management（<<<PAGE 5697>>>）、第 62 章 NTP（<<<PAGE 5884>>>）、第 63 章 Session Management（<<<PAGE 5936>>>）、第 64 章 File Management（<<<PAGE 5999>>>）、第 65 章 Web Management（<<<PAGE 6040>>>）、第 66 章 Configuration File Manager（<<<PAGE 6060>>>）、第 67 章 SNMP（<<<PAGE 6079>>>）、第 68 章 OmniVista Cirrus（<<<PAGE 6132>>>）、第 69 章 OpenFlow（<<<PAGE 6151>>>）、第 70 章 DNS（<<<PAGE 6169>>>）
- 核心命令族：`syslog`、`ntp`、`copy`/`directory`、`configuration`/`working-set`、`snmp`、`chassis`/`temperature`/`fan`/`psu`
- 页码区间：5313–5347 与 5645–5884 与 5936–6240（全书尾部）
