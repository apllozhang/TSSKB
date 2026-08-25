# GLOSSARY — OmniSwitch AOS 8.10R4 Advanced Routing Guide 核心术语

从 verified 术语库（175 条）精选约 110 条，按主题分组。协议/命令保留英文，页码为原书页码。

## 通用与框架

- **Advanced Routing Add-on Package**：本书协议需另购的附加软件包（<<<PAGE 12>>>）
- **IGP（Interior Gateway Protocol）**：自治系统内部路由协议（OSPF/IS-IS）（<<<PAGE 24>>>）
- **EGP（External Gateway Protocol）**：自治系统间路由协议（BGP）（<<<PAGE 123>>>）
- **Route Map（路由映射）**：Action/Match/Set 三类语句控制重分发的策略对象（<<<PAGE 40>>>）
- **Redistribution（重分发）**：把源协议路由注入目的协议（<<<PAGE 43>>>）
- **IP Access List**：把多条 IPv4/IPv6 地址聚合进 route map 的机制（<<<PAGE 43>>>）
- **Graceful Restart（GR，优雅重启）**：接管期间由 helper 维持邻接与 LSA 的不间断机制（<<<PAGE 30>>>）
- **Takeover / CMM / Helper Router**：主备 CMM 接管 / 机箱管理模块 / GR 辅助路由器（<<<PAGE 30>>>）
- **BFD（Bidirectional Forwarding Detection）**：转发故障快速检测（<<<PAGE 22>>>）
- **VLAN / IP Interface**：AOS 上一切路由协议接口的载体（<<<PAGE 21>>>）
- **Router ID**：路由器标识，未配置时自动取主接口地址（<<<PAGE 32>>>）
- **boot.cfg / write memory**：启动配置文件与保存命令（<<<PAGE 33, 231>>>）
- **Working / Certified Directory**：交换机运行目录体系（<<<PAGE 240, 269>>>）

## OSPF / OSPFv3

- **OSPF**：链路状态 IGP，最低开销选路（<<<PAGE 24>>>）
- **LSA / LSDB**：链路状态通告 / 全 LSA 汇成的区域拓扑库（<<<PAGE 24, 20>>>）
- **SPF**：以自身为根的最短路径优先算法（<<<PAGE 24>>>）
- **Area / Backbone（Area 0.0.0.0）**：区域与负责区间分发的骨干区（<<<PAGE 25>>>）
- **ABR / ASBR / Internal Router**：区域边界 / AS 边界 / 内部路由器三角色（<<<PAGE 26>>>）
- **Virtual Link / Transit Area**：恢复骨干连续性的虚链路及其穿越区（<<<PAGE 26>>>）
- **Stub Area / Totally Stubby Area / NSSA / Type-7 LSA**：末节三档与 NSSA 专属 LSA（<<<PAGE 27-28>>>）
- **NSSA Translator Role / Stability Interval**：Type-7 翻译角色与交接稳定间隔（默认 40s）（<<<PAGE 72>>>）
- **area-summary（noareasummary/sendareasummary）**：控制汇总 LSA 进入 Stub/NSSA（<<<PAGE 71>>>）
- **ECMP**：等价多路径，按流分发、不看线速（<<<PAGE 29>>>）
- **DR / BDR**：多路访问网络的指定/备份指定路由器（<<<PAGE 24>>>）
- **NBMA / Point-to-Multipoint**：非广播多路访问及其替代模式（<<<PAGE 29>>>）
- **Passive Interface（被动接口）**：只通告网段不建邻接（<<<PAGE 46>>>）
- **Area Range**：ABR 上汇总区域路由兼作过滤（<<<PAGE 35>>>）
- **Hello / Dead / Poll Interval**：邻居保活三定时器（10s/40s/120s 等）（<<<PAGE 20>>>）
- **SPF Timer（delay/hold）**：SPF 计算延迟/抑制（默认 5/10）（<<<PAGE 20>>>）
- **Keychain Authentication**：密钥轮转认证，可 SHA256（<<<PAGE 38>>>）
- **ip load ospf**：动态加载 OSPF 软件进内存（<<<PAGE 32>>>）
- **OSPFv3 / Grace-LSA / Opaque-LSA**：IPv6 版 OSPF 及其 GR 通告 LSA（<<<PAGE 55, 67>>>）
- **Link-Local Address**：fe80::/10 链路本地地址，OSPFv3 邻居与对等用（<<<PAGE 82>>>）
- **Loopback0 Interface**：不绑 VLAN 永久 up 的管理环回（<<<PAGE 151, 73>>>）
- **nssa-summarize**：NSSA 内 IPv6 前缀汇总为外部 LSA（<<<PAGE 72>>>）

## IS-IS

- **IS-IS**：ISO 链路状态 IGP，同时支持 IP 与 OSI（<<<PAGE 89>>>）
- **CLNP / CLNS / NSAP / NET**：IS-IS 承载协议族与 OSI 地址体系（NSEL=00 的 NSAP 即 NET）（<<<PAGE 89, 95>>>）
- **System ID / Area ID**：NSAP 的 6 字节设备标识与区域标识（最多 3 个/路由器）（<<<PAGE 95, 102>>>）
- **Level-1 / Level-2 / Level-1/2**：区内/区间/双能力路由层级（<<<PAGE 98>>>）
- **IIH / LSP / CSNP / PSNP**：IS-IS 四类报文（<<<PAGE 97>>>）
- **DIS / SNPA**：指定中间系统（优先级默认 64）/ 子网连接点（通常 MAC）（<<<PAGE 95>>>）
- **Wide Metrics**：支持 metric>64 的扩展度量（<<<PAGE 115>>>）
- **L1→L2 Leaking**：Level-1 路由注入 Level-2（route map 实现）（<<<PAGE 115>>>）
- **M-ISIS / MT ID / MT TLV**：多拓扑 IS-IS 及其拓扑标识（IPv4=0、IPv6=2）与能力通告（<<<PAGE 120>>>）
- **Overload State**：路由器过载比特（<<<PAGE 116>>>）
- **Strict Adjacency Check**：GR 期间邻接一致性检查开关（<<<PAGE 90>>>）
- **ip isis area-id**：创建 IS-IS 区域标识命令（<<<PAGE 102>>>）

## BGP

- **BGP / BGP-4**：自治系统间路由协议，本实现支持 BGP-4（<<<PAGE 123>>>）
- **AS / ASN / 4-Octet ASN / AS_TRANS（23456）**：自治系统与编号体系（<<<PAGE 127-128>>>）
- **asplain / asdot+ / asdot**：4 字节 ASN 三种表示格式（<<<PAGE 128>>>）
- **IBGP / EBGP / Transit AS**：AS 内/间会话与穿越自治系统（<<<PAGE 129>>>）
- **TCP 179**：BGP 承载协议与端口（<<<PAGE 126>>>）
- **AS_PATH / AS4_PATH / AS4_AGGREGATE**：AS 序列属性及 4 字节过渡属性（<<<PAGE 126, 128>>>）
- **NEXT_HOP / Local Preference / MED**：下一跳/本地优先级（默认 100）/多出口鉴别器三属性（<<<PAGE 126, 141, 143>>>）
- **Community（no-export 等）**：AS:编号 逻辑分组属性（<<<PAGE 130, 164>>>）
- **Route Reflector / RR Client / Cluster / cluster-id**：路由反射器体系（<<<PAGE 131, 161-163>>>）
- **Confederation（联邦）**：子 AS 组成超 AS 的扩展方案（<<<PAGE 132, 165>>>）
- **Synchronization（BGP-IGP 同步）**：IGP 未知不向 EBGP 通告的规则（默认关）（<<<PAGE 144>>>）
- **Route Dampening / Half-life / Reuse / Suppress / Max Suppress**：抖动抑制四参数（默认 300/200/300/1800）（<<<PAGE 156-157>>>）
- **CIDR / Aggregate Route（summary-only/as-set）**：无类别路由与聚合（<<<PAGE 126, 152>>>）
- **BGP Peer / Neighbor**：显式配置的 BGP 对等实体（<<<PAGE 146>>>）
- **ebgp-multihop / update-source / next-hop-self / remove-private-as**：peer 常用四参数（<<<PAGE 147-150>>>）
- **soft-reconfiguration / clear soft**：不复位会话的软重配置（<<<PAGE 147, 149>>>）
- **maximum-prefix（warning-only）**：限制对等前缀数（默认 5000，80% 告警）（<<<PAGE 146>>>）
- **check-first-as / default-originate**：UPDATE 首 AS 校验 / 向对等通告默认路由（<<<PAGE 149, 146>>>）
- **Regular Expression（AS 正则）**：元字符匹配 AS path 的策略表达式（<<<PAGE 134>>>）
- **AS Path List / Community List / Prefix List / Prefix6 List**：四类 BGP 原子策略（<<<PAGE 133, 201>>>）
- **Routing Policy（in-/out-）**：绑定 peer 学习/通告方向的策略（<<<PAGE 201>>>）
- **asprepend（as-path prepend）**：route map 中追加 AS 的动作（<<<PAGE 204>>>）
- **BGP Graceful Restart / restart-interval**：接管期间保路由连续转发（默认 90s）（<<<PAGE 140, 172>>>）
- **MP-BGP / MP_REACH_NLRI / MP_UNREACH_NLRI**：多协议扩展及其属性（<<<PAGE 177>>>）
- **ipv6 bgp unicast / activate-ipv6**：启用 IPv6 单播能力并激活对等（<<<PAGE 178>>>）
- **ipv6-nexthop / ipv4-nexthop**：跨族对等手工指定下一跳（<<<PAGE 178, 183>>>）
- **GTSM（ttl-security）**：基于 TTL 的 eBGP 防攻击机制（<<<PAGE 212>>>）
- **VPLS / l2vpn-vpls 地址族**：MPLS L2 VPN 服务及其 BGP 信令地址族（<<<PAGE 214>>>）
- **EVPN / evpn-nbr-type-fabric / evpn-fabric-autonomous-system**：BGP EVPN 能力与 fabric 邻居体系（<<<PAGE 216>>>）
- **BGP Neighbor Template（nbr-template）**：批量 peer 模板（当前仅 EVPN 族）（<<<PAGE 218>>>）
- **ip bgp max-neighbors**：VRF 内最大 peer 数（默认 32）（<<<PAGE 144>>>）

## 组播通用与地址边界

- **Administratively Scoped Multicast Addresses**：IANA 保留私组播段 239.0.0.0-239.255.255.255（<<<PAGE 221>>>）
- **Multicast Address Boundary（ip mroute-boundary）**：接口上限定作用域地址不外发（<<<PAGE 222>>>）
- **Concurrent Multicast Addresses**：借边界多域复用同段地址（<<<PAGE 223>>>）
- **SSM 地址段（232.0.0.0/8 与 FF3x::/32）**：源特定组播保留段，须手动启用（<<<PAGE 221, 282>>>）
- **IANA**：互联网编号分配机构（<<<PAGE 221>>>）
- **IGMP / MLD**：IPv4/IPv6 组播成员发现协议（<<<PAGE 232, 282>>>）
- **IPMS**：IP Multicast Switching，组播转发基础（<<<PAGE 231>>>）

## DVMRP

- **DVMRP**：距离矢量组播路由协议 v3，广播-剪枝（<<<PAGE 229>>>）
- **RPF（Reverse Path Multicasting）**：按通往源的最好路由校验到达接口（<<<PAGE 232>>>）
- **Probe Message / All-DVMRP-Routers（224.0.0.4）**：邻居发现消息及其组播地址（<<<PAGE 233>>>）
- **Route Report Message / Flash Update**：周期路由报告与其间变化通告（flash 默认 5s）（<<<PAGE 233, 241>>>）
- **Poison Reverse / Infinity（metric 32）/ Dependent Downstream Router**：毒性反转依赖体系（<<<PAGE 234>>>）
- **Prune / Prune Lifetime / Graft / Graft-Ack**：剪枝（默认 7200s）与嫁接机制（<<<PAGE 235, 242>>>）
- **DVMRP Tunnel**：IP-IP 封装穿越非组播网络（<<<PAGE 236>>>）
- **Route Hold-down**：失效路由以无穷度量继续通告（默认 120s）（<<<PAGE 242>>>）
- **Subordinate Neighbor（subord-default）**：影响初始大流量冲击处理的邻居标志（<<<PAGE 237>>>）

## PIM

- **PIM**：协议无关组播，复用单播 RPF 信息（<<<PAGE 247>>>）
- **PIM-SM / PIM-DM / PIM-SSM**：稀疏/密集/源特定三模式（<<<PAGE 254, 258, 264>>>）
- **RP（Rendezvous Point）**：共享树根，解封装 Register（<<<PAGE 254>>>）
- **C-RP / C-BSR / BSR / RP-set / Bootstrap Message**：候选 RP 与自举路由器选举体系（<<<PAGE 254-255>>>）
- **DR（Designated Router）**：每 LAN 一个；源侧封装 Register、接收侧发 Join（<<<PAGE 255>>>）
- **RPT / SPT**：RP 共享树（(*,G)）/ 源最短路径树（<<<PAGE 254, 258>>>）
- **Register Message / Register-Stop**：源侧 DR 到 RP 的注册与应答（<<<PAGE 258, 260>>>）
- **(*,G) Join / (S,G) Join / (S,G,RPT) Prune**：三类加入/剪枝消息（<<<PAGE 256-263>>>）
- **RP Threshold / SPT Switchover**：RP 触发源 Join 的速率门限 / 末跳 SPT 切换（<<<PAGE 259, 262>>>）
- **Static RP / Anycast RP**：静态组到 RP 映射 / 多 RP 同地址冗余（<<<PAGE 273-274>>>）
- **Group-to-RP Mapping**：最长匹配→最高优先级→hash→最高 IP 四步算法（<<<PAGE 276>>>）
- **Keepalive Period / State Refresh**：(S,G) 状态维持（默认 210s）/ DM 剪枝状态刷新（<<<PAGE 276, 249>>>）
- **Join/Prune Packing / Register Packing / Register MTU**：控制面消息打包调优三参数（<<<PAGE 278-280>>>）
- **ip pim max-rps**：域内最大 RP 数（默认 32，改前须禁 SM）（<<<PAGE 271>>>）
- **RP-Switchover（IPv6）**：IPv6 RP 收首个 Register 即切原生转发（<<<PAGE 292>>>）
- **SPB 服务上的 PIM**：PIM 接口可绑 SPB 服务（<<<PAGE 266>>>）

## MBR

- **MBR（Multicast Border Router）**：同机 DVMRP+PIM 实例互通两域（RFC 2715）（<<<PAGE 297, 299>>>）
- **MBR Default Route Advertisement（mbr-default-information）**：DVMRP 接口通告默认路由（<<<PAGE 302>>>）
- **MBR Protocol Registration**：首个接口 enabled 后自动向 MBR 注册（<<<PAGE 300>>>）
- **ip pim mbr all-sources**：让 PIM 向 DVMRP 通告全部学到的源路由（<<<PAGE 301>>>）
