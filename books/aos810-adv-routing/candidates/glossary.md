# glossary.md — 术语候选（按章分组）
来源：《OmniSwitch AOS Release 8.10R4 Advanced Routing Configuration Guide》。页码为 `<<<PAGE N>>>` 真实标记。

## 第 1 章 OSPF

- **OSPF（Open Shortest Path First）**：链路状态 IGP，在单一 AS 内分发路由信息，选最低开销路径。 <<<PAGE 24>>>
- **IGP（Interior Gateway Protocol，内部网关协议）**：自治系统内部使用的路由协议（如 OSPF、IS-IS）。 <<<PAGE 24>>>
- **LSA（Link State Advertisement，链路状态通告）**：路由器本地状态的通告单元，泛洪构建拓扑库。 <<<PAGE 24>>>
- **LSDB（Link State Database，链路状态数据库）**：由全部 LSA 汇成的区域拓扑库。 <<<PAGE 20>>>
- **SPF（Shortest Path First，最短路径优先算法）**：以自身为根计算最短路径树。 <<<PAGE 24>>>
- **Area（区域）**：连续网络与主机的分组，各区域独立运行 SPF、维护独立拓扑库。 <<<PAGE 25>>>
- **Backbone（骨干区，Area 0.0.0.0）**：负责区间路由信息分发的特殊区域，必须连续。 <<<PAGE 25>>>
- **ABR（Area Border Router，区域边界路由器）**：连接多区域的路由器，为每区域运行一份 SPF 并浓缩拓扑。 <<<PAGE 26>>>
- **ASBR（AS Boundary Router，自治系统边界路由器）**：与其他 AS 交换路由信息的路由器。 <<<PAGE 26>>>
- **Internal Router（内部路由器）**：所有直连网络同属一个区域的路由器。 <<<PAGE 26>>>
- **Virtual Link（虚链路）**：穿越 transit 区恢复骨干连续性的逻辑点到点链路。 <<<PAGE 26>>>
- **Transit Area（转接区域）**：虚链路所穿越的非骨干区域。 <<<PAGE 26>>>
- **Stub Area（末节区域）**：不含 AS 外部 LSA、依赖默认路由的区域。 <<<PAGE 27>>>
- **NSSA（Not-So-Stubby Area，非纯末节区域）**：可用 Type-7 LSA 选择性导入外部路由的末节扩展（RFC 1587）。 <<<PAGE 28>>>
- **Type-7 LSA**：NSSA 内泛洪、在 NSSA 边界翻译为 AS-external LSA 的 LSA 类型。 <<<PAGE 28>>>
- **Totally Stubby Area（完全末节区域）**：在 Stub 基础上再过滤 Type-3 汇总 LSA、仅留默认路由的区域。 <<<PAGE 28>>>
- **ECMP（Equal Cost Multi-Path，等价多路径）**：等开销路径同时保留并按流分发。 <<<PAGE 29>>>
- **NBMA（Non Broadcast Multi Access，非广播多路访问）**：需静态配置邻居、要求全互联的网络类型。 <<<PAGE 29>>>
- **Point-to-Multipoint（点到多点）**：非广播网络的另一种 OSPF 运行模式。 <<<PAGE 29>>>
- **DR / BDR（Designated Router / Backup DR，指定路由器/备份）**：多路访问网络上代表全网泛洪 LSA 的选举角色。 <<<PAGE 24>>>
- **Graceful Restart（优雅重启，GR）**：主备 CMM 接管期间由 helper 维持邻接与 LSA 的不间断机制。 <<<PAGE 30>>>
- **Takeover（接管）**：主 CMM 失效时备 CMM 立即接管主角色。 <<<PAGE 30>>>
- **CMM（Chassis Management Module，机箱管理模块）**：机箱式交换机的管理模块，可双模块冗余。 <<<PAGE 30>>>
- **Helper Router（辅助路由器）**：GR 期间替重启路由器维持 LSA 与邻接的邻居。 <<<PAGE 30>>>
- **Passive Interface（被动接口）**：不收发路由更新、仅向邻居通告该接口网络的接口。 <<<PAGE 46>>>
- **Route Map（路由映射）**：由 Action/Match/Set 语句控制重分发的策略对象。 <<<PAGE 40>>>
- **Redistribution（重分发）**：把源协议学到的路由注入目的协议。 <<<PAGE 43>>>
- **IP Access List（IP 访问列表）**：把多条 IPv4/IPv6 地址聚合进 route map 的机制。 <<<PAGE 43>>>
- **Area Range（区域范围）**：ABR 上把多条区域路由汇总成单条通告，兼作过滤。 <<<PAGE 35>>>
- **Router ID（路由器标识）**：点分十进制标识，未配置时自动取主接口地址。 <<<PAGE 32>>>
- **Dead Interval（死亡间隔）**：未收到 Hello 判邻居失效的时间（广播/P2P 默认 40s，NBMA 120s）。 <<<PAGE 20>>>
- **Hello Interval / Poll Interval**：Hello 周期（默认 10s/30s）与 NBMA 轮询间隔（默认 120s）。 <<<PAGE 20>>>
- **SPF Timer（delay/hold）**：SPF 计算的延迟与抑制定时器（默认 5/10）。 <<<PAGE 20>>>
- **Keychain Authentication（密钥链认证）**：定期轮换密钥的认证方式，可配 SHA256。 <<<PAGE 38>>>
- **ip load ospf**：把 OSPF 软件动态加载进运行内存的命令。 <<<PAGE 32>>>

## 第 2 章 OSPFv3

- **OSPFv3**：OSPFv2 的 IPv6 版本，机制与 v2 对应。 <<<PAGE 55>>>
- **Grace-LSA**：OSPFv3 GR 用链路本地 Opaque-LSA 通告重启意图与宽限期。 <<<PAGE 67>>>
- **Opaque-LSA**：可扩展携带附加信息的 LSA 类别。 <<<PAGE 67>>>
- **NSSA Translator Role（always/candidate）**：NSSA 边界路由器是否无条件承担 Type-7→Type-5 翻译。 <<<PAGE 72>>>
- **NSSA Translator Stability Interval**：翻译者角色交接后的稳定间隔（默认 40s）。 <<<PAGE 72>>>
- **area-summary（noareasummary/sendareasummary）**：控制汇总 LSA 是否进入 Stub/NSSA。 <<<PAGE 71>>>
- **nssa-summarize**：NSSA 内 IPv6 前缀汇总为外部 LSA 通告，filter 可抑制。 <<<PAGE 72>>>
- **Loopback0 Interface**：不绑定 VLAN、永久 up 的管理用环回接口。 <<<PAGE 151>>>（OSPFv3 通告需 point-to-point：<<<PAGE 73>>>）
- **Link-Local Address（链路本地地址）**：OSPFv3/IPv6 邻居与对等使用的 fe80::/10 地址。 <<<PAGE 82>>>

## 第 3 章 IS-IS

- **IS-IS（Intermediate System-to-Intermediate System）**：ISO 定义的链路状态 IGP，同时支持 IP 与 OSI 环境。 <<<PAGE 89>>>
- **CLNP / CLNS**：IS-IS 承载所用的无连接网络协议/服务（即便纯 IP 环境也需 ISO 地址）。 <<<PAGE 89>>>
- **NSAP（Network Service Access Point）**：OSI 网络层地址，由 Area ID + System ID + NSEL 组成。 <<<PAGE 95>>>
- **NET（Network Entity Title）**：NSEL=00 的 NSAP，即 IS-IS 网络层地址。 <<<PAGE 95>>>
- **System ID**：NSAP 中 6 字节设备标识（常用 MAC 或 Loopback IP）。 <<<PAGE 95>>>
- **Level-1 / Level-2 / Level-1/2**：IS-IS 区内/区间/双能力路由层级。 <<<PAGE 98>>>
- **IIH（IS-IS Hello）**：邻居发现与邻接建立的 Hello 报文。 <<<PAGE 97>>>
- **LSP（Link State Packet）**：IS-IS 的链路状态通告，含邻接、前缀、区域等信息。 <<<PAGE 97>>>
- **CSNP（Complete Sequence Number PDU）**：全量 LSP 清单，用于数据库同步。 <<<PAGE 97>>>
- **PSNP（Partial Sequence Number PDU）**：请求与确认 LSP 的部分序号报文。 <<<PAGE 97>>>
- **DIS（Designated Intermediate System）**：广播网上的指定中间系统，按优先级/SNPA 选举。 <<<PAGE 95>>>
- **SNPA（Subnetwork Point of Attachment）**：子网连接点，通常即 MAC 地址。 <<<PAGE 95>>>
- **Wide Metrics（宽度量）**：支持大于 64 度量值的扩展 metric。 <<<PAGE 115>>>
- **Level-1 to Level-2 Leaking（L1→L2 泄漏）**：把 L1 路由注入 L2（反向前缀分发亦支持）。 <<<PAGE 115>>>
- **M-ISIS（Multi-Topology IS-IS）**：单域内为 IPv4/IPv6 分别跑独立 SPF/RIB 的多拓扑模式。 <<<PAGE 120>>>
- **MT ID / MT TLV**：多拓扑标识（IPv4=0，IPv6=2）与 Hello/LSP 中的能力通告 TLV。 <<<PAGE 120>>>
- **Overload State（过载状态）**：指示路由器参与转发的过载比特，可带超时配置。 <<<PAGE 116>>>
- **ip isis area-id**：创建 IS-IS 区域标识（1–13 字节，每路由器最多 3 个）。 <<<PAGE 102>>>
- **Strict Adjacency Check（严格邻接检查）**：GR 期间邻接一致性检查开关。 <<<PAGE 90>>>

## 第 4 章 BGP

- **BGP（Border Gateway Protocol）**：自治系统间交换路由的外部网关协议，本实现支持 BGP-4。 <<<PAGE 123>>>
- **AS（Autonomous System，自治系统）**：单一策略、单一管理下的路由器集合。 <<<PAGE 127>>>
- **ASN / 4-Octet ASN**：AS 编号；4 字节 ASN 按 RFC 6793 支持，兼容 2 字节设备。 <<<PAGE 127>>>
- **AS_TRANS（23456）**：4 字节与 2 字节 ASN 互通用的保留 2 字节 AS 号。 <<<PAGE 128>>>
- **asplain / asdot+ / asdot**：4 字节 ASN 的三种表示格式。 <<<PAGE 128>>>
- **IBGP / EBGP（Internal/External BGP）**：AS 内部 / AS 之间的 BGP 会话。 <<<PAGE 129>>>
- **Transit AS（穿越自治系统）**：为其他 AS 转发流量的多宿主 AS。 <<<PAGE 129>>>
- **TCP 179**：BGP 承载协议与端口。 <<<PAGE 126>>>
- **AS_PATH**：路由穿越的 AS 序列属性，兼作环路检测。 <<<PAGE 126>>>
- **AS4_PATH / AS4_AGGREGATE**：与旧 BGP 互通时携带 4 字节 AS 信息的可选过渡属性。 <<<PAGE 128>>>
- **NEXT_HOP**：BGP 最重要的路径属性之一，指下一跳。 <<<PAGE 126>>>
- **Local Preference（本地优先级）**：AS 内选路偏好，数值越高越优先（默认 100）。 <<<PAGE 141>>>
- **MED（Multi Exit Discriminator，多出口鉴别器）**：向邻居 AS 建议的出口权重，越低越优先，不向下一 AS 传播。 <<<PAGE 143>>>
- **Community（团体）**：以 AS:编号 标识的路由逻辑分组（如 no-export、no-advertise、no-export-subconfed）。 <<<PAGE 130>>><<<PAGE 164>>>
- **Route Reflector（RR，路由反射器）**：集中反射 IBGP 路由以避免全互联的服务角色。 <<<PAGE 131>>>
- **RR Client / Non-Client**：与 RR 同 AS 的两类内部对等；client 免全互联，non-client 需全互联。 <<<PAGE 161>>>
- **Cluster（集群）**：RR 及其 client 组成的集合；冗余 RR 以 cluster-id 标识。 <<<PAGE 161>>><<<PAGE 163>>>
- **Confederation（联邦）**：把子 AS 组成超 AS 的大型网扩展方案，子 AS 间走 EBGP。 <<<PAGE 132>>><<<PAGE 165>>>
- **Synchronization（BGP-IGP 同步）**：仅当 IGP 也已知该目的地时才向 EBGP 通告的规则（默认关闭）。 <<<PAGE 144>>>
- **Route Dampening（路由抖动抑制）**：按 flap 次数抑制不稳定路由的机制。 <<<PAGE 137>>>
- **Instability Metric / Half-life / Reuse / Suppress / Max Suppress Time**：抖动抑制四参数（默认 300/200/300/1800）。 <<<PAGE 156>>><<<PAGE 157>>>
- **CIDR（Classless Inter-Domain Routing，无类别域间路由）**：前缀/掩码式路由表示。 <<<PAGE 126>>><<<PAGE 137>>>
- **Aggregate Route（聚合路由）**：合并多条更精确路由的通告（summary-only/as-set）。 <<<PAGE 152>>>
- **BGP Network（本地网络）**：指示 BGP 从本路由器起源某网络。 <<<PAGE 153>>>
- **BGP Peer / Neighbor**：显式配置的 BGP 对等实体（peer 与 neighbor 混用）。 <<<PAGE 146>>>
- **ebgp-multihop**：允许非直连外部对等建立会话。 <<<PAGE 147>>>
- **update-source**：强制 BGP 会话 TCP 采用指定本地接口/地址。 <<<PAGE 150>>>
- **next-hop-self**：让对等在 UPDATE 中以自身为下一跳。 <<<PAGE 147>>>
- **remove-private-as**：向对等通告时剥离私有 AS 号。 <<<PAGE 147>>>
- **soft-reconfiguration / clear soft**：不复位会话的入/出策略软重配置。 <<<PAGE 147>>><<<PAGE 149>>>
- **maximum-prefix（warning-only）**：限制对等通告前缀数（默认 5000，80% 告警）。 <<<PAGE 146>>>
- **Regular Expression（AS 正则）**：用元字符（^ $ . ? + * | []）匹配 AS path 的策略表达式。 <<<PAGE 134>>>
- **AS Path List / Community List / Prefix List / Prefix6 List**：四类 BGP 原子过滤策略。 <<<PAGE 133>>><<<PAGE 201>>>
- **Routing Policy（in-/out-）**：绑定到 peer 学习/通告方向的策略。 <<<PAGE 201>>>
- **asprepend（as-path prepend）**：route map 中向 AS path 追加 AS 的动作。 <<<PAGE 204>>>
- **BGP Graceful Restart**：CMM 接管期间保留路由信息的连续转发机制（restart-interval 默认 90s）。 <<<PAGE 140>>><<<PAGE 172>>>
- **MP-BGP（Multiprotocol Extensions）**：以 MP_REACH/MP_UNREACH_NLRI 支持多网络层协议（IPv6 等）。 <<<PAGE 177>>>
- **MP_REACH_NLRI / MP_UNREACH_NLRI**：多协议可达/不可达 NLRI 属性。 <<<PAGE 177>>>
- **ipv6 bgp unicast / activate-ipv6**：启用 IPv6 单播能力并激活对等交换 IPv6 前缀。 <<<PAGE 178>>>
- **ipv6-nexthop / ipv4-nexthop**：跨族对等时手工指定对应族下一跳。 <<<PAGE 178>>><<<PAGE 183>>>
- **GTSM（Generalized TTL Security Mechanism）**：基于 TTL 的 eBGP 会话防攻击机制（ttl-security）。 <<<PAGE 212>>>
- **VPLS（Virtual Private LAN Service）**：MPLS L2 VPN LAN 服务；BGP 信令实现 PE 自动发现与标签分发。 <<<PAGE 214>>>
- **L2VPN VPLS Address Family（l2vpn-vpls）**：承载 VPLS NLRI 的 BGP 地址族。 <<<PAGE 214>>>
- **EVPN（Ethernet VPN）**：BGP EVPN 能力，按 peer 在默认 VRF 激活。 <<<PAGE 216>>>
- **evpn-nbr-type-fabric**：把邻居标记为 fabric 侧（super-spine/对等/远端 border spine）连接。 <<<PAGE 216>>>
- **evpn-fabric-autonomous-system**：border spine/leaf 面向 fabric eBGP 会话的附加本地 AS 号。 <<<PAGE 216>>>
- **BGP Neighbor Template（nbr-template）**：批量 peer 配置模板，当前仅支持 EVPN 族。 <<<PAGE 218>>>
- **ip bgp max-neighbors**：VRF 内最大 peer 数（默认 32）。 <<<PAGE 144>>>
- **check-first-as**：处理 UPDATE 时校验 AS path 首个 AS 的开关。 <<<PAGE 149>>>
- **default-originate（peer 级）**：向对等通告默认路由。 <<<PAGE 146>>>

## 第 5 章 组播地址边界

- **Administratively Scoped Multicast Addresses**：IANA 保留给私有组播域的 239.0.0.0–239.255.255.255。 <<<PAGE 221>>>
- **Multicast Address Boundary（组播地址边界）**：在 IP 接口上限定作用域组播地址不外发（ip mroute-boundary）。 <<<PAGE 222>>>
- **Concurrent Multicast Addresses（并发组播地址）**：借助边界在多域复用同一地址段。 <<<PAGE 223>>>
- **IANA（Internet Assigned Numbers Authority）**：互联网编号分配机构，规制组播地址段。 <<<PAGE 221>>>
- **SSM 地址段（232.0.0.0/8）**：IANA 保留给源特定组播的目的地址段。 <<<PAGE 221>>>

## 第 6 章 DVMRP

- **DVMRP（Distance Vector Multicast Routing Protocol）**：密集模式组播路由协议（v3），广播-剪枝建源树。 <<<PAGE 229>>>
- **Reverse Path Multicasting / RPF（逆向路径组播/转发检查）**：按通往源的最好路由校验到达接口再转发。 <<<PAGE 232>>>
- **Probe Message（探测消息）**：周期发往 224.0.0.4 的邻居发现/保活消息，含 Neighbor List。 <<<PAGE 233>>>
- **All-DVMRP-Routers（224.0.0.4）**：DVMRP Probe 的组播目的地址。 <<<PAGE 233>>>
- **Route Report Message（路由报告消息）**：周期交换含掩码源网络与跳数度量的路由表。 <<<PAGE 233>>>
- **Poison Reverse（毒性反转）**：下游以原 metric+32（无穷）回送路由声明依赖。 <<<PAGE 234>>>
- **Infinity（DVMRP metric 32）**：DVMRP 的无穷度量值；32–64 区间视为依赖声明。 <<<PAGE 234>>>
- **Dependent Downstream Router（依赖下游路由器）**：上游据毒性反转建立的按源依赖列表。 <<<PAGE 234>>>
- **Prune / Prune Lifetime（剪枝/剪枝生存期）**：上游停止转发的消息及其有效期（默认 7200s）。 <<<PAGE 235>>><<<PAGE 242>>>
- **Graft / Graft-Ack（嫁接/嫁接确认）**：快速把剪掉分支接回分发树及其确认机制。 <<<PAGE 235>>>
- **DVMRP Tunnel（DVMRP 隧道）**：IP-IP 封装使组播穿越非组播网络的隧道接口。 <<<PAGE 236>>>
- **Flash Update（Routing Table Change 消息）**：两次全量报告间的变化通告（flash-interval 默认 5s）。 <<<PAGE 241>>>
- **Route Hold-down（路由保持）**：失效路由以无穷度量继续通告一段时间（默认 120s）。 <<<PAGE 242>>>
- **Subordinate Neighbor（从属邻居状态，subord-default）**：影响初始大流量冲击处理的邻居状态标志。 <<<PAGE 237>>>
- **IGMP（Internet Group Management Protocol）**：主机向路由器表达组播成员关系的协议。 <<<PAGE 232>>>

## 第 7 章 PIM

- **PIM（Protocol-Independent Multicast）**：协议无关组播路由，复用单播 RPF 信息。 <<<PAGE 247>>>
- **PIM-SM（Sparse Mode，稀疏模式）**：接收者显式 Join 才转发的模式。 <<<PAGE 254>>>
- **PIM-DM（Dense Mode，密集模式）**：泛洪-剪枝、无 RP 的密集模式。 <<<PAGE 258>>>
- **PIM-SSM（Source-Specific Multicast）**：显式频道订阅、免 RP 直连源的模式。 <<<PAGE 264>>>
- **RP（Rendezvous Point，汇聚点）**：共享树根，解封装 Register 并向下分发。 <<<PAGE 254>>>
- **C-RP（Candidate RP，候选汇聚点）**：向 BSR 周期通告自身的候选 RP（默认优先级 192，通告 60s）。 <<<PAGE 254>>><<<PAGE 249>>>
- **BSR（Bootstrap Router）**：域内唯一，汇集并向全网分发 RP-set。 <<<PAGE 255>>>
- **C-BSR（Candidate BSR）**：可参选 BSR 的候选（优先级高者当选，平局比 IP）。 <<<PAGE 255>>>
- **RP-set**：BSR 维护并分发的可达 C-RP 列表。 <<<PAGE 255>>>
- **Bootstrap Message**：BSR 周期扩散 RP-set 的消息。 <<<PAGE 255>>>
- **DR（Designated Router，指定路由器）**：每 LAN 一个；源侧 DR 封装 Register，接收侧 DR 发 Join/Prune。 <<<PAGE 255>>>
- **RPT（RP Tree，共享树）**：以 RP 为根的共享分发树（(*,G) 树）。 <<<PAGE 254>>>
- **SPT（Shortest Path Tree，最短路径树）**：源到接收者的最短路径树。 <<<PAGE 258>>>
- **Register Message / Register-Stop**：源侧 DR 单播封装给 RP 的注册消息与 RP 的停止应答。 <<<PAGE 258>>><<<PAGE 260>>>
- **(*,G) Join / (S,G) Join**：对全源组加入与源特定加入消息。 <<<PAGE 256>>><<<PAGE 259>>>
- **(S,G,RPT) Prune**：SPT 切换后剪掉共享树上该源流量的消息。 <<<PAGE 263>>>
- **RP Threshold（RP 阈值）**：触发 RP 发起 (S,G) Join 的速率门限（ip pim rp-threshold）。 <<<PAGE 259>>>
- **SPT Switchover（SPT 切换）**：末跳 DR 收到首个数据包即切换到 SPT（ip pim spt admin-state）。 <<<PAGE 262>>>
- **Static RP（静态 RP）**：手工配置的组到 RP 映射（ip pim static-rp）。 <<<PAGE 273>>>
- **Anycast RP**：多 RP 共用同一 RP 地址 + IGP 通告的负载分担/冗余机制。 <<<PAGE 274>>>
- **Group-to-RP Mapping（组到 RP 映射算法）**：最长匹配→最高优先级→hash→最高 IP 四步。 <<<PAGE 276>>>
- **Keepalive Period（保活周期）**：(S,G) 状态无显式 Join 时的维持时间（默认 210s）。 <<<PAGE 276>>>
- **State Refresh（状态刷新）**：DM 模式周期刷新剪枝状态（interval 60s、TTL 16）。 <<<PAGE 249>>>
- **Join/Prune Packing（加入/剪枝打包）**：合并 J/P 消息降低控制面丢包（默认 enable）。 <<<PAGE 280>>>
- **Register Packing / Register MTU / Register Delay**：Null Register 打包、打包 MTU 与触发延迟（仅 SM）。 <<<PAGE 278>>><<<PAGE 279>>>
- **ip pim max-rps**：域内最大 RP 数（默认 32，改前须禁 PIM-SM）。 <<<PAGE 271>>>
- **IPMS（IP Multicast Switching）**：组播转发基础，随协议使能自动开启。 <<<PAGE 231>>>
- **MLD（Multicast Listener Discovery）**：IPv6 的组播成员发现协议（源自 IGMPv2，用 ICMPv6）。 <<<PAGE 282>>>
- **IPv6 SSM 地址段（FF3x::/32）**：IPv6 源特定组播保留段，须手动启用。 <<<PAGE 282>>>
- **RP-Switchover（IPv6）**：IPv6 RP 收到首个 Register 即切原生转发（无阈值）。 <<<PAGE 292>>>
- **ip pim mbr all-sources**：让 PIM 向 DVMRP 通告全部学到的源路由（MBR 场景）。 <<<PAGE 301>>>
- **SPB（Shortest Path Bridging）服务上的 PIM**：PIM 接口可绑 SPB 服务（9900 上支持 SPB L3 VPN in-line routing）。 <<<PAGE 266>>>

## 第 8 章 MBR

- **MBR（Multicast Border Router，组播边界路由器）**：同机运行 DVMRP 与 PIM 实例实现两域互通（RFC 2715 / RFC 4601）。 <<<PAGE 297>>><<<PAGE 299>>>
- **MBR Default Route Advertisement（mbr-default-information）**：在 DVMRP 接口通告默认路由以覆盖 DVMRP 域内路由器。 <<<PAGE 302>>>
- **MBR Protocol Registration**：PIM/DVMRP 首个接口 enabled 后自动向 MBR 注册。 <<<PAGE 300>>>

## 通用/跨章

- **Advanced Routing Add-on Package（高级路由附加包）**：本书所述协议需另行购买加载的软件包。 <<<PAGE 12>>>
- **boot.cfg**：控制交换机参数的 ASCII 配置文件；保存协议命令可实现重启自动加载。 <<<PAGE 33>>><<<PAGE 240>>>
- **Working / Certified Directory（工作/认证目录）**：交换机运行目录体系，决定重启后加载的配置。 <<<PAGE 240>>><<<PAGE 269>>>
- **write memory**：把当前配置保存到 Working 目录 boot.cfg。 <<<PAGE 231>>>
- **BFD（Bidirectional Forwarding Detection）**：转发故障快速检测（各协议 show 输出中的 BFD Status）。 <<<PAGE 22>>>
- **VLAN / IP Interface（路由端口）**：AOS 上一切路由协议接口的载体。 <<<PAGE 21>>>
- **Redistribution Administrative Status（重分发管理状态）**：ip redist 配置的启停开关（默认 enable）。 <<<PAGE 44>>>
