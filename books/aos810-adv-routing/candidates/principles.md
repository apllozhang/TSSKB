# principles.md — 原理机制候选（P1…）
来源：《OmniSwitch AOS Release 8.10R4 Advanced Routing Configuration Guide》。页码为 `<<<PAGE N>>>` 真实标记；摘录保留英文原文。

## OSPF（第 1 章）

- **P1 OSPF 是链路状态 IGP，以最低开销选路**：OSPF chooses the least-cost path as the best path. …OSPF is an interior gateway protocol (IGP) that distributes routing information between routers in a Single Autonomous System (AS). <<<PAGE 24>>>
- **P2 LSA 泛洪保证全区域一致的拓扑库**：The flooding algorithm ensures that all routers have exactly the same topological database. …From this database each router calculates a shortest-path tree, with itself as root. <<<PAGE 24>>>
- **P3 Hello 协议承担邻居发现与 DR 选举**：On all networks (broadcast or non-broadcast), the Hello Protocol also elects a designated router for the network. <<<PAGE 24>>>
- **P4 邻接关系控制协议报文分发**：Adjacencies control the distribution of routing protocol packets. Routing protocol packets are sent and received only on adjacencies. <<<PAGE 24>>>
- **P5 多路访问网络由 DR 泛洪网络 LSA**：Each multi-access network that has at least two attached routers has a designated router and a backup designated router. The designated router floods a link state advertisement for the multi-access network. <<<PAGE 24>>>
- **P6 区域隔离拓扑知识以减少路由流量**：An area's topology is visible only to the members of the area. …This isolation of knowledge enables the protocol to reduce routing traffic by concentrating on small areas of an AS. <<<PAGE 25>>>
- **P7 骨干区（Area 0.0.0.0）负责区间路由信息分发**：Different areas communicate with each other through a backbone. …The backbone is responsible for distributing routing information between areas. <<<PAGE 25>>>
- **P8 区域参数不一致将阻止邻接形成**：All routers belonging to an area must agree on that area's configuration. Misconfiguration will keep neighbors from forming adjacencies between themselves, and OSPF will not function. <<<PAGE 25>>>
- **P9 四类路由器角色（内部/ABR/骨干/ASBR）可重叠**：Internal routers. …Area border routers. …Backbone routers. …AS boundary routers. …This classification is completely independent of the previous classifications. <<<PAGE 26>>>
- **P10 ABR 为每个所连区域运行一份 SPF 并浓缩拓扑**：Area border routers run multiple copies of the SPF algorithm, one copy for each attached area. Area border routers condense the topological information of their attached areas for flooding to other areas. <<<PAGE 26>>>
- **P11 虚链路将两台骨干路由器视作无编号点到点连接**：The protocol treats two routers joined by a virtual link as if they were connected by an unnumbered point-to-point network. <<<PAGE 26>>>
- **P12 Stub 区域不通告 AS 外部 LSA，靠默认路由出域**：A stub area is an area with routers that have no AS external Link State Advertisements (LSAs). …default routing must be used in the stub area. <<<PAGE 27>>>
- **P13 NSSA 用 Type-7 LSA 有选择地导入外部路由**：These routes are imported into the NSSA using a new LSA type: Type-7 LSA. Type-7 LSAs are flooded within the NSSA and are translated at the NSSA boundary into AS-external LSAs. <<<PAGE 28>>>
- **P14 Totally Stubby 区域在 Stub 基础上再过滤 Type-3 LSA**：This concept has been extended with Totally Stubby Areas by filtering Type 3 LSAs (Network Summary LSA) in addition to Type 4 and 5 with the exception of one single Type 3 LSA used to advertise a default route. <<<PAGE 28>>>
- **P15 ECMP 按流分发而非轮询，且不考虑线速**：Delivery of packets along equal paths is based on flows rather than a round-robin scheme. …other variables, such as line speed, are not considered. <<<PAGE 29>>>
- **P16 NBMA 网络必须全互联且需静态配置邻居**：For non-broadcast networks neighbors should be statically configured. …a fully meshed network is mandatory. <<<PAGE 29>>>
- **P17 冗余 CMM 接管触发改邻接重建的优雅重启（GR）**：This time period between the restart and the reestablishment of adjacencies is termed graceful restart. <<<PAGE 30>>>
- **P18 Helper 路由器在 GR 期间维持重启路由器的 LSA（含 DR 身份）**：Router Y's LSAs continue to list an adjacency to Router X over network segment S, regardless of the adjacency's current synchronization state. <<<PAGE 30>>>
- **P19 Totally Stubby 的实现方式 = Stub 类型 + 关闭汇总**：In order to configure a totally stubby area you need to configure the area as stub on the ABR and disable summarization. <<<PAGE 35>>>
- **P20 被动接口不收发路由更新且立即拆除已有邻接**：No OSPF adjacency is formed on a passive interface, and if a OSPF-enabled interface is configured as passive where an adjacency already exists, the adjacency drops almost immediately. <<<PAGE 46>>>
- **P21 用 Route Map 重分发 local 路由成内部路由，批量生成被动接口**：A route map with set action of route-type 'internal' needs to be created for the local interface (routes) on which passive OSPF interface needs to be created. <<<PAGE 46>>>
- **P22 配置重分发即自动成为 ASBR**：An OSPF router automatically becomes an Autonomous System Border Router (ASBR) when redistribution is configured on the router. <<<PAGE 43>>>
- **P23 iBGP→OSPF 重分发默认禁止，需显式开启**：By default, redistribution of iBGP routes is not allowed into OSPF protocol. To allow redistribution of iBGP routes (from the same AS) into OSPF protocol, use the ip ospf redist-bgp-internal command. <<<PAGE 48>>>
- **P24 OSPF 接口认证三种：simple / MD5 / keychain（可 SHA256）**：There are three types of authentication: simple, MD5, and Keychain authentication. …The authentication type can be set to SHA256 when using the key-chain parameter. <<<PAGE 37>>><<<PAGE 38>>>
- **P25 MD5 key ID 与 key string 必须分两条命令配置**：Note that setting the key ID and key string must be done in two separate commands. <<<PAGE 37>>>

## Route Map 与重分发（跨章机制）

- **P26 Route Map 三类语句：Action / Match / Set**：Action. An action statement configures the route map name, sequence number, and whether or not redistribution is permitted or denied…Match…Set. <<<PAGE 40>>>
- **P27 序列间隐含逻辑 OR；同类型 match 之间 OR、不同类型之间 AND**：Note that there is an implied logical OR between sequences. …If these statements are of the same kind …then a logical OR is implied…If the match statements specify different types of matches…then a logical AND is implied. <<<PAGE 42>>>
- **P28 无 match 语句的 route map 重分发所有路由**：If a route map does not contain any match statements and the route map is applied using the ip redist command, the router redistributes all routes into the network of the receiving protocol. <<<PAGE 77>>><<<PAGE 111>>>
- **P29 route map 未配序列号时默认取 50**：If a value is not configured, then the number 50 is used by default. <<<PAGE 76>>>
- **P30 deny 某路由不等于默认放行其余路由**：With route maps denying a route does not mean that all the other routes are automatically permitted. It is necessary to configure proper permit/deny rule for each route. <<<PAGE 42>>><<<PAGE 168>>>
- **P31 set metric 支持 add/subtract/replace/none 四种效果**：Add - Adds the given value to the routes metric…Subtract…Replace…None - Ignores the given value and passes the routes metric through. <<<PAGE 42>>><<<PAGE 168>>>
- **P32 访问列表把多条地址聚合进单条 route map 语句**：An IP access list provides a convenient way to add multiple IPv4 or IPv6 addresses to a route map. <<<PAGE 43>>>
- **P33 重分发要求源/目的协议均已加载并使能**：Make sure that both protocols are loaded and enabled before configuring redistribution. <<<PAGE 43>>>

## OSPFv3（第 2 章）

- **P34 OSPFv3 是 OSPFv2 的 IPv6 扩展，GR 默认使能**：OSPFv3 is an extension of OSPF version 2 that provides support for networks using the IPv6 protocol. …By default, OSPFv3 is enabled on the router. <<<PAGE 55>>><<<PAGE 56>>>
- **P35 OSPFv3 GR 用链路本地 Grace-LSA 通告重启意图**：The OSPFv3 router attempting a graceful restart originates link-local Opaque-LSAs, called Grace-LSAs, announcing the intention to perform a graceful restart and requests for a grace period. <<<PAGE 67>>>
- **P36 helper 三条件：宽限期未到、helper 使能、拓扑稳定**：these neighbors continue to announce the 'restarting' router in their LSAs as if it were fully adjacent provided the grace period has not expired, graceful restart helper functionality is enabled, and network topology remains stable. <<<PAGE 67>>>
- **P37 重启完成后 flush Grace-LSA 结束 GR**：Once all adjacencies are established, the restarting router flushes its grace LSAs signaling the successful termination of graceful restart. <<<PAGE 67>>>
- **P38 NSSA translator 角色与稳定性间隔（默认 40s）**：Stability interval is the duration for which a Type-7 translator will continue in the translator role after another NSSA border router translator has assumed the role. <<<PAGE 72>>>
- **P39 area-summary 两档：noareasummary 只进默认路由 / sendareasummary 汇总后放行**：When set to noareasummary option, inter-area LSAs will neither originate or propagate into the stub or NSSA. Only a default route will be advertised. <<<PAGE 71>>>
- **P40 OSPFv3 Loopback0 不会自动通告，需配成 point-to-point**：Unlike with OSPFv2, the OSPFv3 Loopback0 interface is not automatically advertised to its neighbor. To advertise the Loopback0 interface, configure it as a point-to-point interface. <<<PAGE 73>>>
- **P41 OSPFv3 静态邻居使用链路本地地址**：to create an OSPFv3 neighbor with a link-local address to be a static neighbor…ipv6 ospf neighbor fe80::2e0:b1ff:fe7e:5f1e interface vlan-213 eligible. <<<PAGE 82>>>

## IS-IS（第 3 章）

- **P42 IS-IS 两层层级：Level-1 区内、Level-2 区间**：Routing within an area is referred to as Level-1 routing. …Routing between areas is referred to as Level-2 routing. <<<PAGE 95>>>
- **P43 NSAP 三字段：Area ID + System ID + NSEL（=00 时称 NET）**：NSEL field…System ID…Area ID…The NSAP address with its NSEL set to 00 is called Network Entity Title (NET). <<<PAGE 95>>>
- **P44 DIS 选举按接口优先级（默认 64），平局比 SNPA/MAC**：Election of the DIS is based on the highest interface priority, the default value of which is 64. …In case of a tie, the router with the highest Subnetwork Point Of Attachment (SNPA) address (usually the MAC address). <<<PAGE 95>>>
- **P45 形成邻接的三要素：认证匹配、IS 类型、MTU**：The primary criteria for forming adjacencies are authentication match, IS-type, and MTU size. <<<PAGE 95>>>
- **P46 IS-IS 四种报文：IIH / LSP / CSNP / PSNP**：Intermediate System-to-Intermediate System Hello (IIH)—Used by routers to detect neighbors…CSNP—Contains a list of all the LSPs…PSNP—Used to request an LSP(s) and acknowledge receipt of an LSP(s). <<<PAGE 97>>>
- **P47 IS-IS 路由器完全属于单一区域（对比 OSPF 接口分域）**：In IS-IS, the router belongs entirely to a single area. <<<PAGE 98>>>
- **P48 全局与接口 level 能力组合决定潜在邻接**：When the level capabilities are configured both globally and on per-interface basis, the combination of the two settings will decide the potential adjacency. <<<PAGE 103>>>
- **P49 汇总路由取最小 metric 通告；内部路由不能在 L1 汇总**：The metric that is used to advertise the summary address is the smallest metric than any of the more specific IP routes. …It is not possible to summarize IS-IS internal routes at Level-1. <<<PAGE 104>>>
- **P50 认证可在全局/level/电路/电路级四层配置，低层覆盖全局**：Keychain authentication can be applied at a global level, capability level, circuit level, and capability level per circuit. …Enabling authentication on specific IS-IS levels over-rides the global authentication. <<<PAGE 107>>><<<PAGE 108>>>
- **P51 auth-check 关闭时仍认证但只报错不丢包**：If disabled, the authentication PDUs are generated and the IS-IS PDUs are authenticated on receipt. An error message will be generated in case of a mismatch; but PDUs will not be rejected. <<<PAGE 107>>>
- **P52 IS-IS GR：IIH 携带重启请求与 Remaining Time，helper 同步 CSNP**：The IS-IS Hello (IIH) messages are modified to signal a graceful restart request. …They send their Complete Sequence Number PDUs (CSNPs) to the restarting router. <<<PAGE 98>>>
- **P53 Level-1→Level-2 泄漏及 L2→L1 前缀分发经 route map 实现**：IS-IS allows redistributing Level-1 IS-IS routes into Level-2 IS-IS routes. This is termed as Level-1 to Level-2 Leaking. This release also supports the prefix distribution from the level-2 IS-IS routes to level-1. <<<PAGE 115>>>
- **P54 M-ISIS 背景：单拓扑 IPv4/IPv6 混布会黑洞**：This behavior may result in black-holed routing when there are some IPv4-only or IPv6-only routers in an IS-IS routing domain. <<<PAGE 120>>>
- **P55 M-ISIS 为每个拓扑独立 SPF 与 RIB（IPv4=MT ID 0，IPv6=MT ID 2）**：M-ISIS mechanism runs multiple, independent IP topologies within a single IS-IS network domain, using separate topology-specific SPF computation and multiple Routing Information Bases (RIBs). <<<PAGE 120>>>
- **P56 MT 能力经 Hello 的 MT TLV 通告；无 MT TLV 视为默认拓扑**：M-ISIS routers advertise their MT capability by including a set of MT TLVs in their Hello PDUs. Any IS-IS router that does not advertise MT capability…is considered as belonging to the default topology. <<<PAGE 120>>>
- **P57 点到点无共同拓扑不成邻接；广播网即使无共同拓扑也成邻接**：On point-to-point interfaces, if two neighboring MT capable IS-IS routers have no common topologies in common, no adjacency is formed. On broadcast interfaces, an adjacency is formed…even if there is no topology in common. <<<PAGE 120>>>
- **P58 切换 multi-topology 会内部重启 IS-IS 并复位邻接**：Changing the multi-topology mode with this command will result in internal disabling and re-enabling of IS-IS protocol…This causes IS-IS adjacencies to be reset. <<<PAGE 120>>>
- **P59 非 MT 模式下 MT TLV 不参与 SPF 计算（向后兼容默认 IPv4 TLV）**：even if M-ISIS capability is enabled, AOS IS-IS will continue to exchange IPv4 prefixes in the default IPv4 reachability TLVs. <<<PAGE 121>>>

## BGP（第 4 章）

- **P60 BGP 用 TCP 179，增量更新使长会话更高效**：Hosts using BGP communicate using the Transmission Control Protocol (TCP) on port 179. …only changes are exchanged after startup, which makes long running BGP sessions more efficient than shorter ones. <<<PAGE 126>>>
- **P61 AS_PATH 承担 AS 级环路检测**：Loops are detected and avoided by checking for your own AS number in AS_PATHs received from neighboring Autonomous Systems. <<<PAGE 126>>>
- **P62 BGP 定位是 EGP，作 IGP 时适合多出口 transit AS**：It is not intended to be used as an Interior Gateway protocol (IGP)…is best used in transit autonomous systems with multiple exit points. <<<PAGE 126>>><<<PAGE 127>>>
- **P63 IGP 策略偏技术，EGP 策略偏商业关系**：IGP policies tend to be set due to traffic concerns and technical demands, while EGP policies are set more on business relationships between corporate entities. <<<PAGE 127>>>
- **P64 4 字节 ASN：AS4_PATH/AS4_AGGREGATOR 属性 + AS_TRANS 23456 兼容旧设备**：Support for two new optional transitive attributes AS4_PATH and AS4_AGGREGATE…To establish a neighbor relationship between non-mappable BGP 4-octet ASNs with BGP 2-octet ASNs the reserved 2-octet ASN AS_TRANS 23456 is used. <<<PAGE 128>>>
- **P65 IBGP 全互联规则及 RR 对规则的放松**：routes learned through one IBGP speaker cannot be advertised to another IBGP speaker, route reflection allows the router reflector servers to "reflect" routes, thereby relaxing the IBGP standards. <<<PAGE 131>>>
- **P66 RR 通告规则表（按路由来源决定反射范围）**：External BGP Router→All Clients and Non-Clients；Non-Client Peer→All Clients；Client Peer→All Clients and Non-Clients. <<<PAGE 162>>>
- **P67 Cluster 内 client 不需全互联，non-client 必须全互联**：The client peers do not need to be fully meshed…but the non-client peers must be fully meshed. <<<PAGE 161>>>
- **P68 冗余 RR 用 cluster-id 标识且 RR 之间全互联**：Redundant route reflectors must be identified by a 4-byte cluster ID…All route reflectors in the same cluster must be fully meshed and should have the exact same client and non-client peers. <<<PAGE 163>>>
- **P69 联邦：子 AS 间走 EBGP 但整体表现为 IBGP，属性跨子 AS 保留**：Even though EBGP is used to communicate between AS 1001 and 1002, the entire confederation behaves as though it were using IBGP. …the sub AS attributes are preserved when crossing the sub AS boundaries. <<<PAGE 132>>>
- **P70 Community 逻辑分组跨 AS 传播策略语义（如 no-export）**：Communities are used to simplify routing policies by identifying routes based on a logical property rather than an IP prefix or an AS number. <<<PAGE 130>>>
- **P71 MED 只在同一邻居 AS 间比较，绝不向下一 AS 传播**：If received on external links, the MED may be propagated over internal links to other BGP speakers in the same AS. However, the MED is never propagated to speakers in a neighboring AS. <<<PAGE 143>>>
- **P72 同步规则：IGP 未知的 IBGP 路由不向 EBGP 通告**：a BGP router should not advertise to external neighbors destinations learned from IBGP neighbors unless those destinations are also known via an IGP. <<<PAGE 144>>>
- **P73 路由抖动抑制：不稳定性度量、半衰期折半、低于复用值重新通告**：Each time a route flaps…its "instability metric" is increased by 1. Once a route's instability metric reaches the suppress value, it is suppressed…its instability metric will be cut in half…Once below the reuse value, a route will be re-advertised. <<<PAGE 156>>>
- **P74 dampening 参数必须一次性按序全部输入**：The variables for these parameters must be entered together, in one command, in order. <<<PAGE 157>>>
- **P75 聚合路由需至少存在一条更精确路由；聚合本身无需本地已知**：You cannot aggregate an address…if you do not have at least one more-specific route of the address…in the BGP routing table. Aggregate routes do not need to be known to the local BGP speaker. <<<PAGE 152>>>
- **P76 AS 正则按 token 匹配而非字符匹配，便于书写与加速加载**：the BGP implementation treats AS numbers as single tokens, providing two benefits: It makes writing (and reading) policies much easier. It enables the router to begin using the policies more quickly after startup. <<<PAGE 134>>>
- **P77 本地优先级数值越高越优先，是选路首要属性之一**：In many cases, it will be the most important criteria in determining the selection of one route over another. …The higher the number, the higher the preference. <<<PAGE 141>>><<<PAGE 153>>>
- **P78 4 类策略（AS path/community/prefix(prefix6)/route map）先建后绑到 peer 的 in/out 方向**：each BGP peer needs to be tied to inbound and/or outbound policies (direction based on whether routes are being learned or advertised). <<<PAGE 201>>>
- **P79 AS 正则元字符语义（^ $ . ? + * () [] 等）**：^ Matches the beginning of the AS path list…$ Matches the end of the AS path list…( ) Begins/Ends an alternation sequence…[ ] Begin/End a range pair. <<<PAGE 134>>>
- **P80 多协议 BGP 用 MP_REACH/MP_UNREACH_NLRI 承载 IPv6 前缀与下一跳**：two new non-transitive attributes are introduced, Multiprotocol Reachable NLRI (MP_REACH_NLRI) and Multiprotocol Unreachable NLRI (MP_UNREACH_NLRI). <<<PAGE 177>>>
- **P81 IPv6 对等可跑在 IPv4 会话上（需 activate-ipv6 + ipv6-nexthop）**：Multiprotocol BGP extensions support the advertisement of IPv6 prefixes over the BGP sessions established between two BGP speakers using either of their IPv4 or IPv6 addresses. <<<PAGE 177>>><<<PAGE 178>>>
- **P82 本地 IPv6 地址（FC00::/7）在 iBGP 间交换、eBGP 间忽略**：The local IPv6 address prefixes are exchanged between internal BGP (IBGP) speakers within the same Autonomous System (AS)…As Exterior BGP (EBGP) peers between different AS ignore receipt of and do not advertise prefixes with the well-known FC00::/7 prefix. <<<PAGE 182>>>
- **P83 GTSM：控制包 TTL 置 255，接收方按剩余 TTL 判跳数、超限丢弃**：the TTL (IPv4) and hop limit (IPv6) field of BGP control packets sent to the peer is set to 255. …If the number of hops exceeds the maximum configured value, the packet is dropped. <<<PAGE 212>>>
- **P84 VPLS BGP 信令：NLRI 自动发现 PE + 单条 Update 携带全部远端 PE 标签**：each PE discovers which other PEs are part of a given VPLS by using the BGP protocol to send BGP NLRI updates for the l2vpn-vpls address family. …a PE to send a single (common) Update message that contains MPLS labels for all the remote PEs. <<<PAGE 214>>>
- **P85 BGP EVPN：每 peer 会话需在默认 VRF 上显式激活 EVPN 能力**：The BGP EVPN capability must be activated for each peer BGP session on the default VRF. <<<PAGE 216>>>
- **P86 邻居模板的优先级：个体 peer 配置覆盖模板配置**：The individual BGP peer configuration will take precedence over the BGP neighbor template configuration. <<<PAGE 218>>>
- **P87 BGP GR 保持转发不断以支撑域间流量**：On an OmniSwitch router in a redundant CMM configuration, inter-domain routing is not disrupted during a CMM takeover/failover. BGP retains routing information using Graceful Restart mechanisms. <<<PAGE 172>>>
- **P88 Loopback0 永久 up，适合作 BGP 对等源（配合 update-source / ebgp-multihop）**：The Loopback0 interface is not bound to any VLAN, so it will always remain operationally active. <<<PAGE 151>>>
- **P89 BGP soft reset（clear soft）只重应用策略不复位会话**：Use the ip bgp neighbor clear soft command to reset peer policy parameters. <<<PAGE 149>>>
- **P90 多条全局命令要求先禁用 BGP 才能修改（AS 号、本地优先级、MED 比较等）**：Many BGP global commands require the user to disable the protocol before changing parameters. <<<PAGE 139>>>

## 组播地址边界（第 5 章）

- **P91 239.0.0.0/8 为管理作用域组播地址**：Multicast addresses 239.0.0.0 through 239.255.255.255 have been reserved by the IANA as administratively scoped addresses for use in private multicast domains. <<<PAGE 221>>>
- **P92 边界阻止作用域地址的组播流量 leaking 到域外**：A boundary is used to eliminate these conflicts by confining multicast traffic on an IP interface. When a boundary is set, multicast packets with a destination address within the specified boundary will not be forwarded on the interface. <<<PAGE 222>>>
- **P93 边界使同一作用域地址块可在多个域并发复用**：scoped multicast addresses can be reused throughout the network. This allows network administrators to conserve limited multicast address space. <<<PAGE 223>>>

## DVMRP（第 6 章）

- **P94 DVMRP = 广播-剪枝型密集模式协议，按源生成分发树**：DVMRP, essentially a "broadcast and prune" routing protocol…dynamically generates per-source delivery trees based upon routing exchanges, using a technique called Reverse Path Multicasting. <<<PAGE 229>>><<<PAGE 232>>>
- **P95 RPF 检查：仅当分组到达上游接口才转发**：If the packet arrived on an upstream interface that would be used to transmit packets back to the source, it is forwarded…Otherwise, it is not on the optimal delivery tree and is discarded. <<<PAGE 232>>>
- **P96 邻居发现靠周期 Probe（224.0.0.4），Neighbor List 出现自己即双向邻接**：When a DVMRP router receives a Probe with its own IP address included in the Neighbor List, the router knows that a two-way adjacency has been successfully formed. <<<PAGE 233>>>
- **P97 DVMRPv3 未建立邻接不接受 Route Report**：In DVMRPv3, a router will not accept a Route Report from another DVMRP router until it has established adjacency with that neighboring router. <<<PAGE 233>>>
- **P98 毒性反转：回送 metric=原值+32 的路由，上游据此建依赖列表**：it indicates this by echoing back the route on the upstream interface with a metric equal to the original metric plus infinity. (DVMRP uses a metric of 32 as infinity.) <<<PAGE 234>>>
- **P99 DVMRP 毒性反转语义区别于单播 DV 协议**：Poison reverse is used differently in DVMRP than in most unicast distance vector routing protocols (such as RIP), which use poison reverse to advertise that a particular route is unreachable. <<<PAGE 234>>>
- **P100 剪枝自下而上逐级回传，直到无用的分支全部移除**：If the upstream router is able to remove all of its downstream interfaces in this manner, it can then send a DVMRP Prune message to its upstream router. <<<PAGE 235>>>
- **P101 Graft/Graft-Ack 机制把重加入时延降到毫秒级**：By using a graft mechanism, DVMRP reduces the join latency to a few milliseconds. <<<PAGE 235>>>
- **P102 DVMRP 隧道用 IP-IP 封装穿越非组播网络，协议消息也走单播**：IP multicast packets are encapsulated in unicast IP packets…DVMRP protocol messages…are sent between tunnel endpoints using unicast, rather than multicast, packets. <<<PAGE 236>>>
- **P103 路由保持 holddown 以无穷度量继续通告，防旧路由回环传播**：it is common in distance vector protocols to continue to advertise a route that has been deleted with a metric of infinity…The hold down period is usually two report intervals. <<<PAGE 242>>>
- **P104 路由表带掩码，DVMRP 实际是 classless 协议**：The key difference…is that DVMRP routes are advertised with a subnet mask, which makes DVMRP effectively a classless protocol. <<<PAGE 241>>>
- **P105 分支路由器发送剪枝的 lifetime 取本机配置与队列中最小剩余值**：the prune-lifetime value inserted into the prune packet is the smallest of the following values: the value of ip dvmrp prune-lifetime on the sending device…the amount of lifetime that remains for each individual prune… <<<PAGE 242>>>

## PIM（第 7 章）

- **P106 PIM 协议无关：复用任一单播协议的 RIB**：Protocol-Independent Multicast (PIM) is an IP multicast routing protocol that uses routing information provided by unicast routing protocols such as RIP and OSPF. PIM is "protocol-independent" because it does not rely on any particular unicast routing protocol. <<<PAGE 247>>>
- **P107 PIM-SM 接收者驱动（显式 Join），适合稀疏/WAN 场景**：multicast forwarding in PIM-SM is initiated only via specific requests, referred to as Join messages. …ideal for network environments where receiver groups are thinly populated and bandwidth conservation is a concern. <<<PAGE 254>>>
- **P108 RP 是共享树（RPT）根，负责解封装 Register 并向下分发**：shared distribution trees are rooted at a common forwarding router, referred to as a Rendezvous Point (RP). The RP unencapsulates Register messages and forwards multicast packets natively down established distribution trees. <<<PAGE 254>>>
- **P109 BSR 域内唯一，经 Bootstrap 消息分发 RP-set**：There is only one BSR per PIM domain. This allows all PIM routers in the PIM domain to view the same RP set. <<<PAGE 255>>>
- **P110 C-BSR 选举：优先级最高者胜，平局比 IP**：The C-BSR with the highest priority level is elected as the BSR…If two or more C-BSRs have the same priority value, the C-BSR with the highest IP address is elected. <<<PAGE 255>>>
- **P111 DR 选举看 DR 优先级（Hello 携带），平局比 IP；源侧 DR 封装 Register**：When a DR receives multicast data from the source, the DR encapsulates the data packets into the Register messages, which are in turn sent to the RP. <<<PAGE 255>>>
- **P112 Register 封装低效：耗 CPU 且路径可能绕远**：The encapsulation and unencapsulation of Register messages tax router resources. Hardware routing does not support encapsulation and unencapsulation. …data may have to travel "out of their way" to the RP. <<<PAGE 258>>>
- **P113 RP 阈值触发的 (S,G) 源特定 Join + Register-Stop**：When the data rate at the Rendezvous Point (RP) exceeds the configured RP threshold value, the RP will initiate a (S, G) source-specific Join message toward the source. …A register-stop packet is sent back to the sender's DR. <<<PAGE 259>>><<<PAGE 260>>>
- **P114 SPT 切换由最后一跳 DR 收到首个组播数据包即自动发起**：The last hop Designated Router (DR) initiates the switchover to a true Shortest Path Tree (SPT) once the DR receives the first multicast data packet. <<<PAGE 262>>>
- **P115 SPT/RPT 双流期间丢 RPT 份并发 (S,G,RPT) 剪枝**：This router drops the packets arriving via the RP tree and forwards only those packets arriving via the SPT. An (S, G, RPT) Prune message is sent toward the RP. <<<PAGE 263>>>
- **P116 PIM-DM 与 SM 本质差异：无周期 Join、无 RP**：There are no periodic joins transmitted, only explicitly triggered prunes and grafts. There is no Rendezvous Point (RP). <<<PAGE 258>>>
- **P117 PIM-SSM：显式频道订阅，无需 RP，直接建 SPT**：SSM, using an explicit channel subscription model, allows receivers to receive multicast traffic directly from the source; an RP tree model is not used. <<<PAGE 264>>>
- **P118 232.0.0.0/8 为 SSM 保留段，须手动配置才启用**：The multicast address range from 232.0.0.0 through 232.255.255.255 have been reserved by the Internet Assigned Numbers Authority (IANA) as Source-Specific Multicast (SSM) destination addresses. …needs to be configured manually to support SSM. <<<PAGE 264>>>
- **P119 组到 RP 映射算法：最长匹配→最高优先级→hash→最高 IP**：1 Perform longest match on group-range…2 find the one with the highest priority…4 use the PIM-SM hash function defined in the RFC to choose one. <<<PAGE 276>>><<<PAGE 292>>>
- **P120 Anycast RP：多机同一 RP 地址 + IGP 通告，收敛与 IGP 同级**：Anycast RP introduces the concept where the same IP address (RP Address) is configured on two or more routers serving as the RP. …In case of a failure, the convergence is the same as the IGP. <<<PAGE 274>>>
- **P121 Register/Join-Prune 打包降低控制面丢包风险**：In large networks with a lot of sources, this can amount to a lot of PIM Control packets which ultimately may be dropped due to control plane processing overhead or CPU queue rate-limiting. The packing of these Null Registers and Register stops has been added to reduce the possibility of losing these packets. <<<PAGE 278>>>
- **P122 IPv6 SSM 保留段为 FF3x::/32，同样需手动启用**：The multicast addresses range FF3x::/32 that has been reserved by the Internet Assigned Numbers Authority (IANA) as Source-Specific Multicast (SSM) destination addresses is not enabled automatically. <<<PAGE 282>>>
- **P123 IPv6 RP-switchover 无阈值概念，收到首个 Register 即切换**：You can configure an RP to attempt switching to native forwarding upon receiving the first register-encapsulated packet from the source DR in the IPv6 PIM domain. <<<PAGE 292>>>
- **P124 MLD 是 IPv6 的组播成员发现（源自 IGMPv2，走 ICMPv6）**：Multicast Listener Discovery (MLD) is the protocol used by an IPv6 router to discover the nodes that request multicast packets…MLD is derived from version 2 of IPv4's Internet Group Management Protocol, IGMPv2. <<<PAGE 282>>>

## MBR（第 8 章）

- **P125 MBR = 同机 DVMRP 实例 + PIM 实例，按 RFC 2715 互通**：an OmniSwitch MBR consists of a DVMRP instance and a PIM instance with one or more active interfaces in each instance. <<<PAGE 299>>>
- **P126 MBR 三职能：拉取 PIM 域注入 DVMRP、导入 DVMRP 域流量、 transit 穿越**：The MBR first pulls down packets generated within the PIM domain and injects them into the DVMRP domain. …imports packets generated within the DVMRP domain…passes the multicast traffic through. <<<PAGE 299>>>
- **P127 PIM/DVMRP 首个接口 enabled 后自动向 MBR 注册**：PIM and DVMRP are dynamically registered with MBR as soon as the first interface is enabled and operational for the particular protocol. <<<PAGE 300>>>
- **P128 IPv6 无广播地址，组播前缀 ff00::/8**：There are no broadcast addresses in IPv6. …multicast addresses begin with the prefix ff00::/8. <<<PAGE 177>>><<<PAGE 282>>>
