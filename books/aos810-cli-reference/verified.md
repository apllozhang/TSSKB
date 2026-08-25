# Verified 候选（V1 原文真实性核对 + V2/V3 抽查）

## counter-examples

## 平台限定
- **X1 spb bvlan 平台支持（第 10 章，<<<PAGE 745>>>）**：BVLAN 仅 6570M/6860/6860N/6865/6870/6900/6575/6920/9900 支持；6360/6465/6560 为 No。
- **X2 ip ospf spf-timer / hello-interval 平台（第 28 章，<<<PAGE 2409>>>/<<<PAGE 2434>>>）**：6360/6465 不支持；6560 起全部支持。
- **X3 ip bgp default local-preference / maximum-paths 平台（第 31 章，<<<PAGE 2759>>>/<<<PAGE 2776>>>）**：6360/6465/6575 不支持（6575 对 maximum-paths 为 No）。
- **X4 QoS Policy 章通用限制（第 39 章，<<<PAGE 3953>>>）**：原书明示"部分命令当前在一个或多个平台不受支持，需查各命令平台矩阵与 release notes"。
## 前置条件（必须先做什么）
- **X7 PoE 802.3at 分级检测（第 2 章）**：要按 802.3at 供电必须先 `lanpower slot class-detection` 启用分级检测；802.3bt 下则自动启用、相关手工命令不受支持。
- **X8 路由协议加载（第 24/27/28/30/31 章）**：RIP/OSPF/IS-IS/BGP/VRRP 命令生效前需 `ip load <protocol>` 加载对应模块。
- **X9 OS 6465 PoE 电源（第 2 章）**：OmniSwitch 6465 不能自动检测电源类型，必须手工配置，否则系统与 PoE 功率信息显示错误。
- **X10 VC chassis id 生效时机（第 14 章，<<<PAGE 1198>>>）**：配置的 chassis identifier 要到目标机箱下次重启才生效。
## 互斥与冲突
- **X11 ISID 与 VRF 绑定互斥（第 10 章）**：同一 ISID 不能既绑定又重分发到同一 VRF 实例。
- **X12 linkagg 与 AppMon 互斥（第 13 章，<<<PAGE 1092>>>）**：链路聚合不能配置在 AppMon（应用监测）已启用的端口上。
- **X13 UNP multi-untag SAP 与 persistent profile 互斥（第 42 章，<<<PAGE 4470>>>）**：persistent profile 存在时两者互斥。
- **X14 Trust-Tagged VLAN 限制（第 42 章）**：私有 VLAN 不能配置为 Trust-Tagged VLAN；关联 Trust-Tagged VLAN 的 UNP profile 不能映射到 service domain；使用 Trust-Tagged VLAN 时端口的 Trust-Tag 必须禁用。
- **X15 动态 VLAN 删除限制（第 42 章）**：UNP 动态创建的 VLAN 不能用标准 `no vlan vlan_id` 删除。
- **X16 hash-control brief 模式退化（第 13 章）**：brief 模式下聚合哈希仅基于源 MAC（L2）或源 IP（L3），负载分担粒度下降。
## 使用限制与边界
- **X17 BVLAN 一致性要求（第 10 章，<<<PAGE 745>>>）**：每台 SPB 桥的 BVLAN 配置必须完全一致，否则 ISIS-SPB 邻居发现与最短路径计算失败。
- **X18 reserved VLAN 不可常规配置（第 7 章，<<<PAGE 476>>>）**：VLAN Stacking 的保留 VLAN 不能用标准 vlan 命令配置；NNI 口一旦成为 stacking 口，其 TPID（非 0x8100 时）不可再修改。
- **X19 legacy BPDU 双限制（第 7 章）**：legacy BPDU 仅当交换机处于 flat STP 模式时支持，且只应在连接 legacy 设备的 VLAN Stacking 网络端口上启用。
- **X20 VC 同型限制（第 14 章）**：Virtual Chassis 只支持同型号两台交换机之间（如 6860 与 6900 之间不支持）；`no virtual-chassis` 形式仅在交换机上无任何 VFL 配置时可用。
- **X21 PolicyView 规则只读（第 39 章，<<<PAGE 3953>>>）**：经 PolicyView 创建的规则不能经 CLI 修改（CLI 只能以更高优先级新建策略覆盖）。
- **X22 VLAN prompt-on-deletion（第 5 章，<<<PAGE 428>>>）**：默认删除带成员端口的 VLAN 不弹确认，误删风险由 prompt-on-deletion 参数兜底（默认 disable）。
- **X23 OSPF hello=0 语义（第 28 章，<<<PAGE 2434>>>）**：hello-interval 设 0 的含义是创建被动接口（不发送 hello），并非更快收敛。
- **X24 LLDP 控制帧默认丢弃（第 18 章，<<<PAGE 1390>>>）**：带标签与无标签 802.1AB 控制帧默认均丢弃，需 `ethernet-service uni` 显式配置处理方式。

## frameworks

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

## glossary

- **第1章 Ethernet Port Commands**：D1 端口物理层参数（speed/duplex/fec/ddm/violation 等）与端口统计，约 85 条 <<<PAGE 67>>>
- **第2章 Power over Ethernet (PoE) Commands**：D1 PoE 供电预算、分级、power rule 管理，约 38 条 <<<PAGE 254>>>
- **第3章 UDLD Commands**：D1 单向链路检测，防单向光纤故障成环，约 12 条 <<<PAGE 327>>>
- **第4章 Source Learning Commands**：D2 MAC 地址学习/过滤/老化与 FDB 管理，约 33 条 <<<PAGE 351>>>
- **第5章 VLAN Management Commands**：D2 VLAN/私有 VLAN 创建、成员划分与 STP 开关，约 13 条 <<<PAGE 427>>>
- **第6章 High Availability VLAN Commands**：D2 跨机箱 VLAN 高可用同步，约 10 条 <<<PAGE 455>>>
- **第7章 VLAN Stacking Commands**：D2 QinQ 双层标签/保留 VLAN/NNI-UNI 角色，约 40 条 <<<PAGE 476>>>
- **第8章 Distributed Spanning Tree Commands**：D3 802.1D 分布式 STP/RSTP/MSTP 树形防环，约 50 条 <<<PAGE 567>>>
- **第9章 MPLS Commands**：D4 MPLS LSP/标签转发与 VPN 隧道，约 26 条 <<<PAGE 689>>>
- **第10章 Shortest Path Bridging Commands**：D4 ISIS-SPB 骨干（BVLAN/桥优先级/ECT/GR），SPBM 控制面，约 43 条 <<<PAGE 743>>>
- **第11章 Service Manager Commands**：D4 SPBM 服务层（ISID/SAP/PBB 封装业务），SPBM 数据面，约 83 条 <<<PAGE 839>>>
- **第12章 Loopback Detection Commands**：D3 二层环路检测与端口自动阻断，约 11 条 <<<PAGE 1070>>>
- **第13章 Link Aggregation Commands**：D3 静态/LACP 链路聚合与哈希控制，约 46 条 <<<PAGE 1092>>>
- **第14章 Virtual Chassis Commands**：D5 虚拟机箱（VFL 互联/双机箱管理），约 32 条 <<<PAGE 1198>>>
- **第15章 Ethernet Ring Protection Commands**：D3 ITU-T G.8032 环网保护倒换，约 16 条 <<<PAGE 1268>>>
- **第16章 Media Redundancy Protocol Commands**：D3 IEC 62439-2 MRP 工业环网冗余，约 11 条 <<<PAGE 1306>>>
- **第17章 MVRP Commands**：D2 802.1ak MVRP 动态 VLAN 注册传播，约 23 条 <<<PAGE 1340>>>
- **第18章 802.1AB Commands**：D9 LLDP 邻居发现与 TLV 管理，约 40 条 <<<PAGE 1390>>>
- **第19章 SIP Commands**：D5 会话/互联类命令（章名缩写未展开，域归属待确认），约 18 条 <<<PAGE 1486>>>
- **第20章 Automatic Fabric Commands**：D5 自动织构（Auto-Fabric 节点角色与自动发现），约 12 条 <<<PAGE 1523>>>
- **第21章 IP Commands**：D6 IP 接口/路由/ARP/DNS/UDP 中继等单播底座，约 113 条 <<<PAGE 1549>>>
- **第22章 IPv6 Commands**：D6 IPv6 地址/邻居发现/路由与过渡，约 68 条 <<<PAGE 1793>>>
- **第23章 IPsec Commands**：D8 IPsec/IKE 隧道加密，约 11 条 <<<PAGE 1948>>>
- **第24章 RIP Commands**：D6 RIP/RIPv2 距离矢量路由，约 41 条 <<<PAGE 1974>>>
- **第25章 BFD Commands**：D6 双向转发检测（为路由协议提供毫秒级故障检测），约 16 条 <<<PAGE 2058>>>
- **第26章 DHCP Relay Commands**：D6 DHCP 中继/option82/监督，约 116 条 <<<PAGE 2092>>>
- **第27章 VRRP Commands**：D6 虚拟路由冗余（首跳网关备份），约 24 条 <<<PAGE 2334>>>
- **第28章 OSPF Commands**：D6 OSPFv2 链路态 IGP（区域/接口/虚链路/重分发），约 57 条 <<<PAGE 2392>>>
- **第29章 OSPFv3 Commands**：D6 OSPFv3（IPv6 版链路态 IGP），约 46 条 <<<PAGE 2513>>>
- **第30章 IS-IS Commands**：D6 IS-IS 链路态路由（SPB 控制面基础），约 62 条 <<<PAGE 2610>>>
- **第31章 BGP Commands**：D6 BGP-4/MP-BGP 域间路由（全书第二大章），约 194 条 <<<PAGE 2744>>>
- **第32章 Server Load Balancing Commands**：D6 服务器负载均衡（VIP/实服务组/健康检查），约 31 条 <<<PAGE 3160>>>
- **第33章 IP Multicast Switching Commands**：D7 二层组播交换（IGMP 侦听/MCS），约 106 条 <<<PAGE 3227>>>
- **第34章 IP Multicast VLAN Commands**：D7 组播 VLAN（MVR）业务通道，约 12 条 <<<PAGE 3471>>>
- **第35章 DVMRP Commands**：D7 距离矢量组播路由，约 23 条 <<<PAGE 3495>>>
- **第36章 PIM Commands**：D7 PIM-SM/SSM/DM 组播路由协议，约 99 条 <<<PAGE 3542>>>
- **第37章 Multicast Routing Commands**：D7 组播路由全局/边界/静态组播路由管理，约 14 条 <<<PAGE 3769>>>
- **第38章 QoS Commands**：D10 QoS 硬件队列/调度/端口 QoS 参数，约 70 条 <<<PAGE 3797>>>
- **第39章 QoS Policy Commands**：D10 策略条件-动作-规则-列表模型与各类 group，约 111 条 <<<PAGE 3953>>>
- **第40章 Policy Server Commands**：D10 策略服务器（LDAP 端 PolicyView 联动），约 9 条 <<<PAGE 4190>>>
- **第41章 AAA Commands**：D8 RADIUS/TACACS+/LDAP 与认证授权计费方法链，约 119 条 <<<PAGE 4205>>>
- **第42章 Access Guardian Commands**：D8 UNP/BYOD/Captive Portal/QMR/IoST 设备画像安全准入框架（全书第一大章），约 199 条 <<<PAGE 4470>>>
- **第43章 Application Monitoring and Enforcement Commands**：D10 应用识别与流量管控（AppMon），约 37 条 <<<PAGE 4934>>>
- **第44章 Application Fingerprinting Commands**：D10 应用指纹库管理，约 12 条 <<<PAGE 5016>>>
- **第45章 FIP Snooping Commands**：D5 FCoE 初始化协议侦听（FCoE 安全），约 22 条 <<<PAGE 5039>>>
- **第46章 FCoE/FC Gateway Commands**：D5 以太网光纤通道与 FC 网关，约 27 条 <<<PAGE 5090>>>
- **第47章 VXLAN Snooping Commands**：D5 VXLAN 侦听与虚拟网段管理，约 20 条 <<<PAGE 5152>>>
- **第48章 Port Mapping Commands**：D5 端口映射（数据流量重定向到应用/服务），约 9 条 <<<PAGE 5195>>>
- **第49章 Learned Port Security Commands**：D8 已学习端口安全（LPS，限定可接入设备），约 18 条 <<<PAGE 5212>>>
- **第50章 Port Mirroring and Monitoring Commands**：D9 端口镜像与流量监测，约 9 条 <<<PAGE 5256>>>
- **第51章 sFlow Commands**：D9 sFlow 采样流量监测，约 13 条 <<<PAGE 5277>>>
- **第52章 RMON Commands**：D9 RMON 远程网络监视告警/历史/统计，约 4 条 <<<PAGE 5305>>>
- **第53章 Switch Logging Commands**：D11 系统日志（syslog）级别/服务器/过滤，约 14 条 <<<PAGE 5313>>>
- **第54章 Health Monitoring Commands**：D9 健康监测（CPU/内存/进程阈值检查），约 6 条 <<<PAGE 5347>>>
- **第55章 Ethernet OAM Commands**：D9 802.1ag CFM 连通性故障管理（MEP/MAID），约 46 条 <<<PAGE 5358>>>
- **第56章 LINK OAM Commands**：D9 802.3ah 链路级 OAM 远端发现/环回/远端故障指示，约 23 条 <<<PAGE 5432>>>
- **第57章 CPE Test Head Commands**：D9 CPE 测试头（接入侧业务拨测），约 31 条 <<<PAGE 5503>>>
- **第58章 PPPoE Intermediate Agent**：D8 PPPoE 中间代理（接入侧认证辅助/截留），约 12 条 <<<PAGE 5571>>>
- **第59章 Service Assurance Agent Commands**：D9 SAA 主动探测（ping/ftp/http 等业务质量测量），约 19 条 <<<PAGE 5597>>>
- **第60章 CMM Commands**：D11 通信模块管理（CMM 控制模块冗余/同步），约 29 条 <<<PAGE 5645>>>
- **第61章 Chassis Management and Monitoring Commands**：D11 机箱/风扇/电源/温度等硬件管理，约 91 条 <<<PAGE 5697>>>
- **第62章 Network Time Protocol Commands**：D11 NTP/SNTP 时间同步，约 25 条 <<<PAGE 5884>>>
- **第63章 Session Management Commands**：D11 CLI 会话/telnet/SSH 连接与超时管理，约 35 条 <<<PAGE 5936>>>
- **第64章 File Management Commands**：D11 文件系统（copy/delete/directory/脚本）管理，约 21 条 <<<PAGE 5999>>>
- **第65章 Web Management Commands**：D11 内嵌 Web 管理开关与 HTTP/HTTPS 配置，约 11 条 <<<PAGE 6040>>>
- **第66章 Configuration File Manager Commands**：D11 配置文件（running/committed/备份/回滚）管理，约 11 条 <<<PAGE 6060>>>
- **第67章 SNMP Commands**：D11 SNMP v1/v2c/v3 团体/用户/陷阱/通知管理，约 26 条 <<<PAGE 6079>>>
- **第68章 OmniVista Cirrus Commands**：D11 云管理平台（OmniVista Cirrus）对接配置，约 10 条 <<<PAGE 6132>>>
- **第69章 OpenFlow Commands**：D11 SDN OpenFlow 控制器/流表混合模式管理，约 8 条 <<<PAGE 6151>>>
- **第70章 DNS Commands**：D11 DNS 客户端解析配置，约 6 条 <<<PAGE 6169>>>

## principles

## 端口与 PoE（第 1、2 章）
- **P1 `interfaces` 命令族（第 1 章，<<<PAGE 67>>>）**：以太网端口软件负责硬件诊断、链路状态通知、线路参数配置与统计采集。`interfaces speed|duplex|fec|break-out|eee|ddm` 等 30+ 子命令覆盖物理层全部可调参数；`violation`/`clear violation` 管理端口违例恢复。
- **P2 端口监视与统计（第 1 章）**：`show interfaces status/counters/counters errors/traffic/ddm` 按场景拆分展示；`interfaces link-monitoring link-flap-threshold/link-error-threshold` 提供链路抖动自动检测。
- **P3 PoE 供电管理（第 2 章，<<<PAGE 254>>>）**：`lanpower` 族管理 PSE 供电预算、端口优先级与 power rule；802.3bt（固件 3.xx）下 class-detection 自动启用，无需手工配置；power rule 需先创建再绑定到槽位/端口才生效。
- **P4 PoE 平台差异（第 2 章）**：OmniSwitch 6465 无法自动检测电源类型，必须手工配置电源型号才能正确显示系统与 PoE 功率信息。
## 二层与 VLAN（第 5、7 章）
- **P5 `vlan` 命令（第 5 章，<<<PAGE 428>>>）**：`vlan vlan_id [admin-state {enable|disable}] [name description | prompt-on-deletion]`。默认 admin-state=enable、prompt-on-deletion=disable；支持 `vlan 10-15` 连续区间写法；删除 VLAN 前自动剥离全部成员端口，端口回退默认 VLAN 1。
- **P6 VLAN 语义（第 5 章）**：所有物理端口初始属于 VLAN 1；VLAN 在至少一个成员端口 active 前不会操作生效；admin-state disable 保留静态端口归属但停止转发。
- **P7 私有 VLAN（第 5 章）**：`pvlan`/`pvlan secondary`/`pvlan mapping` 三级结构（primary/secondary/isolated-community），MIB 为 ALCATEL-IND1-VLAN-MGR-MIB。
- **P10 链路聚合（第 13 章，<<<PAGE 1092>>>）**：`linkagg` 支持静态与动态（LACP）聚合；动态聚合仅兼容 IEEE 802.3ad 标准实现；hash-control brief 模式下哈希退化为仅源 MAC（L2）或仅源 IP（L3）。
## SPB 骨干与服务（第 10、11 章）
- **P11 SPBM 架构（第 10 章，<<<PAGE 743>>>）**：SPB-M 按 IEEE 802.1aq 用 PBB（802.1ah MAC-in-MAC）封装穿越骨干，最短路径树由 ISIS-SPB（IS-IS + SPB TLV 扩展）计算；分 backbone（控制面）与 services（数据面）两层，服务层命令在第 11 章 Service Manager。
- **P12 `spb bvlan`（第 10 章，<<<PAGE 745>>>）**：BVLAN ID 取值 1–4094，支持区间（如 10-20）；默认 admin-state=enable；BVLAN 配置必须在每台 SPB 桥上完全一致，否则 ISIS-SPB 邻居发现与最短路径计算失败。平台：6360/6465/6560 不支持，6570M 起支持。
- **P13 BVLAN 与普通 VLAN 差异（第 10 章）**：BVLAN 上 STP 自动禁用、全部端口保持转发态。
- **P14 `spb isis bridge-priority`（第 10 章，<<<PAGE 750>>> 附近）**：默认 32768，数值越小优先级越高；桥优先级占 8 字节 SPB Bridge ID 的高 2 字节，低 6 字节为桥 MAC（system ID）。
- **P15 SPB IP VPN（第 10 章，<<<PAGE 744>>>）**：`spb ipvpn bind/redist` 把 ISID 绑定/重分发进 VRF；同一 ISID 不能绑定并重分发进同一 VRF 实例。
## IP 与路由（第 21、28、31 章）
- **P16 IP 命令章规模（第 21 章，<<<PAGE 1549>>>）**：113 条，`ip interface`/`ip route`/`ip domain`/ARP/`ip helper` 等构成单播路由底座；路由协议均需先 `ip load <protocol>` 加载。
- **P17 OSPF 定位（第 28 章，<<<PAGE 2392>>>）**：链路态 IGP，符合 RFC 1370/1850/2328/2370/3101/3623；命令按 Global/Area/Interface/BFD/VRF 分组；DR/BDR 机制。
- **P18 `ip ospf spf-timer`（第 28 章，<<<PAGE 2409>>>）**：`[delay seconds] [hold seconds]`，取值均 0–65535；默认 delay=5、hold=10；任一值设 0 则拓扑变化立即触发 SPF 且可背靠背计算。平台：6360/6465 不支持，6560 起支持。
- **P19 `ip ospf interface hello-interval`（第 28 章，<<<PAGE 2434>>>）**：取值 0–65535 秒；默认 broadcast/点对点=10、NBMA/点对多点=30；值 0 创建被动（passive）OSPF 接口。
- **P20 BGP 定位（第 31 章，<<<PAGE 2744>>>）**：BGP-4 + 多协议扩展（MP-BGP 支持 IPv6 单播前缀与 IPv6 邻居会话），符合 RFC 4271/4760/2545/7947 等；命令分 Global/Aggregate/Network/Neighbor/Address-family/VRF 组；peer 与 neighbor 术语互换使用。
- **P22 `ip bgp maximum-paths`（第 31 章，<<<PAGE 2776>>>）**：等价多路径（ECMP）开关，默认 disabled；启用后在忽略 router-id 判等时把全部等价路径装表；同样要求先停 BGP。
## QoS 与策略（第 38、39 章）
- **P23 策略模型（第 39 章，<<<PAGE 3953>>>）**：policy rule = policy condition + policy action；rule 编入 policy list 后生效；策略可经 CLI/SNMP/PolicyView（LDAP 端 GUI）三种途径创建。
- **P24 CLI 与 PolicyView 优先级（第 39 章）**：PolicyView 创建的规则不能经 CLI 修改，但 CLI 创建的策略可覆盖 PolicyView 策略的优先级。
- **P25 条件子命令族（第 39 章，<<<PAGE 3955>>>）**：`policy condition` 40+ 子命令，覆盖 ip/ipv6/ip-port/tcp-port/udp-port/ethertype/tcpflags/service/icmp/ip-protocol/flow-label/tos/dscp/mac/vlan/802.1p/port/vrf/fragments/app-mon 等，inner 前缀支持 QinQ 内层字段。
- **P26 动作子命令族（第 39 章，<<<PAGE 3956>>>）**：`policy action` 提供 disposition（accept/drop/deny）、cir（承诺信息速率，bps + cbs/pir/pbs）、maximum bandwidth/depth、802.1p/dscp/tos 改写与 map 映射、redirect port/linkagg、mirror、port-disable、permanent gateway 等。
- **P27 group 复用机制（第 39 章）**：`policy network/mac/port/vlan/map/service group` 把同类对象成组，供多个 condition 引用，减少重复定义。
- **P28 QoS 硬件章（第 38 章，<<<PAGE 3797>>>）**：与第 39 章策略软件互补，管理硬件队列、调度与端口 QoS 参数（70 条）。
## 安全与准入（第 41、42 章）
- **P29 Access Guardian 架构（第 42 章，<<<PAGE 4470>>>）**：UNP（Universal Network Profile）为统一框架——端口使能 UNP 后对用户认证/分类进 profile，profile 映射 VLAN 或 SAP；组件含 BYOD（UPAM/ClearPass 联动，含 mDNS/SSDP GRE 隧道）、Captive Portal（内置 Web 服务器内外部认证）、QMR（隔离与补救）、IoT Device Profiling（DHCP 指纹 + MAC OUI）。199 条为全书最大命令章。
- **P30 UNP 命令分组（第 42 章，<<<PAGE 4471>>>）**：全局配置（dynamic-vlan-configuration、auth-server-down、redirect 族、mac-mobility 等）与 profile 配置（trust-tagged-vlans、qos-policy-list、captive-portal 等）两大类，另加 port/domain/user/show 组。
- **P31 AAA 支撑（第 41 章，<<<PAGE 4205>>>）**：119 条，RADIUS/TACACS+/LDAP 服务器组与认证方法链，为 Access Guardian 提供 AAA 底座（原书明确指引联动）。
## 监测与 OAM（第 18、50-57 章）
- **P32 LLDP（第 18 章，<<<PAGE 1390>>>）**：802.1AB 以 LLDPDU 与邻居交换信息并维护邻居数据库；`ethernet-service uni` 控制带标签/无标签 LLDPDU 的处理（默认两者均丢弃）。
- **P33 双 OAM 体系（第 55、56 章）**：Ethernet OAM/CFM（802.1ag，MEP/MAID/远端 MEP 状态，<<<PAGE 5358>>>）面向连通性故障管理；LINK OAM（802.3ah，<<<PAGE 5432>>>）面向单链路监测，两章共 69 条。
## 系统与管理（第 61、66 章）
- **P34 配置管理模型（第 61、66 章，<<<PAGE 5697>>>/<<<PAGE 6060>>>）**：`working-set`/`configuration` 命令族支持 VC 多机箱批量配置与 running/committed 双区管理；Chassis Management 章 91 条覆盖风扇/电源/温度/防雷等硬件运维。
