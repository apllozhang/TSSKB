# Verified 候选（V1 原文真实性核对 + V2/V3 抽查）

## cases

- **C1 DC/Campus 双场景用例论证**：DC 用 spine-leaf 2/3-tier；campus 可沿用传统三层或 spine-leaf。"A common topology used is spine-and-leaf or Clos architecture. It can be 2-tier (3-stage) or 3-tier (5-stage) depending on the scale." <<<PAGE 8>>>
- **C2 3-tier Super-Spine DCI 场景**："A 3-tier (5-stage) spine-leaf topology can be used for requirements with hyper scalability for DCI... when the core network (Inter-site) is operating in a different overlay protocol (for example, MPLS)." <<<PAGE 8>>>
- **C3 Intra-subnet 五步走包分析（Client-1→Client-6）**：ARP request → LEAF-1 查 proxy ARP 缓存 → 代答 → 单播封装 VXLAN → LEAF-6 解封装桥接。"3. Since proxy ARP is enabled, LEAF-1 will send an ARP response to Client-1 with the MAC+IP address information for Client-6." <<<PAGE 31>>>
- **C4 Inter-subnet 对称 IRB 六步走包分析（Client-1→Client-4）**：ARP 网关 → IP-VRF 查 SBD overlay index → 递归解析 LEAF-4 IRB MAC → VXLAN 封装 → 对端 SBD IP-VRF → MAC-VRF 下发。"5. LEAF-1 consults the ARP table to identify the destination (LEAF-4) MAC address and consults the SBD MAC-VRF table to determine the VNI." <<<PAGE 31-32>>>
- **C5 多归属开局流程案例（R-T4 发现→DF 选举→R-T1A/1B 通告冗余模式）**：single-active flags=1、all-active flags=0。"R-T1A (A-D per ES) route is advertised with ESI Label extended community. This extended community has a flags field set to 1 to indicate single-active redundancy." <<<PAGE 32-33>>>
- **C6 DF change 丢包场景与 SMET-by-all-PEs 补救**："In the event of a DF change, there will be traffic drop to clients, as the remote PEs will continue to forward the traffic to older PE until they receive the SMET routes form the new PE." <<<PAGE 36>>>
- **C7 OISM 跨子网组播转发案例**：IGMP join → R-T6 带 Fabric-VPN RT → 源 PE IPMS 建 Fabric-VPN 组表项 → 隧道转发。"The PE where the multicast source is connected, assuming it is in a different EVI, will import the R-T6 and informs the IP Multicast Switching (IPMS) service." <<<PAGE 37-38>>>
- **C8 双 PEG 冗余 + 外部 PIM 互通案例**："it is possible to have two PEGs acting as redundant pairs for a given VRF and supports load balancing across different VRFs... a dedicated L3 link should be used between PEGs for RP reachability." <<<PAGE 38>>>
- **C9 R-T10 源发现信令流案例**：ingress PE 收到组播首包 → R-T10(S,G) → DR PEG 注册到外部 RP → PIM join 回来 → PEG 发 R-T6 拉流。"When the DR PEG recieves the PIM join, it will generate R-T6 for the given (S,G) to pull traffic from the source." <<<PAGE 39>>>
- **C10 MAC duplication 场景（同 MAC 两主机/环路）**："a continuous exchange of the MAC being advertised and withdrawn in the control plane among all the PEs... leads to degradation of the EVPN network performance." 靠 hold-down + retry-time 解除。<<<PAGE 39>>>
- **C11 Duplicate IP（DAD）双主机同 IP 场景**："Now, a new ARP with the same IP from host 2 (MAC B) entering to the EVPN network is considered as IP Mobility." Confirm message 探测旧主。<<<PAGE 39-40>>>
- **C12 Silent host（WAKE-ON-LAN）静态绑定案例**："it may be necessary to statically bind MAC address to a SAP port... for example for a WAKE-ON-LAN packet." <<<PAGE 40>>>
- **C13 外部连通场景：border leaf + GRM 路由注入**："LEAF-1 should export the routes from VRF-2 to the Global Route Manager (GRM) and the Fabric-VPN (EVI-50) should register with the GRM to receive these routes." <<<PAGE 47>>>
- **C14 全册端到端配置案例（2 spine + 6 leaf）**：VLAN/VNI/IP 规划表 → OSPF underlay（10 步）→ BGP RR overlay（5 步）→ LAG → Fabric-VPN → SAP/ES → service → 对称 IRB → DAG → 外部 OSPF → proxy ARP，逐段验证。"Since we are using symmetric IRB in this configuration example, it is not required to have all the services instantiated in all leaf switches, but only where the hosts are attached." <<<PAGE 48-72>>>
- **C15 静态 LAG ESI 手工配置实例**："service access linkagg 20 vlan-xlation enable evpn-ethernet-segment enable esi 01:01:01:02:04" <<<PAGE 64>>>
- **C16 BFD 参数实例（200ms 发包）**："ip bfd transmit 200 / receive 200 / echo-interval 200" <<<PAGE 50>>>
- **C17 Anycast MAC 自动派生实例**："Anycast MAC = 00:00:5e:00:01:01"（00:00:5e:00:01:<VRF-ID> 规则）<<<PAGE 69>>>
- **C18 验证命令家族案例**：show ip bgp neighbors / show service evpn / show service evpn ethernet-segment / show ip evpn proxy-arp / show ip routes 逐段展示。<<<PAGE 60-71>>>
- **C19 Proxy ARP 表老化后的恢复操作**："In case Proxy ARP Table is empty, it has probably timed out. Please try to send communication between the hosts and this should generate entries in the table." <<<PAGE 72>>>
- **C20 VLAN-based 回退时的行为差异案例**："In data plane, the passenger packet is stripped of all tags and sent in the tunnel as untagged. Egress VLAN translation on PE's take care of adding the right VLAN." <<<PAGE 42>>>

## counter-examples

- **X1 STP 阻塞链路浪费资源**："The use of Spanning Tree Protocol (STP) led to inefficient use of resources due to blocked redundant links... It was also complex, slow to converge, and had inter-operating issues between different versions." <<<PAGE 5>>>
- **X2 L2 环路与广播风暴（无 TTL）**："Broadcast storms and endless Layer 2 loops (due to lack of TTL in Layer 2 frames) can cause instability of the entire infrastructure." <<<PAGE 5>>>
- **X3 12-bit VLAN 上限**："VLAN segmentation allows for a 12-bit VLAN ID, which has an upper limit of 4096 VLANs. This is very restrictive specifically in data center environments." <<<PAGE 5>>>
- **X4 Traffic tromboning（静态首跳网关导致绕行）**："Inter-VLAN traffic flows could suffer a 'trombone' effect and follow a sub-optimal path for east-west traffic. This is due to having a static first-hop router." <<<PAGE 5>>>
- **X5 洪泛学习需组播底层、复杂度叠加**："In a VXLAN enabled network, this model requires a multicast-enabled underlay to discover remote VTEPs and to learn endpoint MAC addresses. This adds complexity to the architecture." <<<PAGE 7>>>
- **X6 持续洪泛伤扩展性**："Constant flooding over the fabric in such a deployment in order to maintain accurate end-host reachability information can present a challenge for scalability." <<<PAGE 9>>>
- **X7 广播帧走 EVI 隧道不被推荐**："Broadcast frames can also be forwarded using the EVI distribution tunnels but is generally not recommended since the FDB learning and ARP suppression mechanism is relied upon to reduce the flood traffic." <<<PAGE 14>>>
- **X8 应禁用 proxy ARP 的例外场景**："some use cases might require to disable it. Some example are hosts that are using Gratuitous ARPs or ARP probes for detection and when you're debugging L2/L3 connectivity issues and require full visibility of ARP packets in the EVPN fabric." <<<PAGE 21>>>
- **X9 VRRP 集中网关低效**："a redundancy protocol (such as VRRP) would be required on the VTEPs such that only the master VTEP router can act as the gateway. But this solution is not efficient since it can lead to traffic tromboning and the overhead of the control plane." <<<PAGE 28>>>
- **X10 自动派生 anycast MAC 的碰撞风险**："Auto-derivation of the anycast MAC can only be used if there is a certainty that the auto-derived MAC does not collide with any MAC address that is already being used in the network." <<<PAGE 29>>>
- **X11 Tandem replication 复杂 vs ingress replication 低效**："tandem replication adds complexity by using a multicast-enabled underlay... ingress replication... is less efficient than tandem replication. Ingress replication, however, is much simpler to configure." <<<PAGE 29-30>>>
- **X12 非对称 IRB 资源/配置密集**："all PEs need to maintain each host's (local and remote) IP and MAC address in its ARP table and maintain MAC-VRFs and IRB interfaces for all subnets... makes the model more resource and configuration intensive." <<<PAGE 24>>>
- **X13 无 R-T6/7/8 时多归属 IGMP 状态问题**："All-active: There is no guarantee that IGMP Join and Leave packets will be sent to the DF for that ES / Single-active: A failover in the DF will cause a loss of IGMP state information." <<<PAGE 36>>>
- **X14 DF change 期间组播丢包**："In the event of a DF change, there will be traffic drop to clients, as the remote PEs will continue to forward the traffic to older PE until they receive the SMET routes form the new PE." <<<PAGE 36>>>
- **X15 MAC duplication 拖垮控制平面**："Such a behavior leads to a continuous exchange of the MAC being advertised and withdrawn in the control plane among all the PEs... and leads to degradation of the EVPN network performance." <<<PAGE 39>>>
- **X16 重复 IP 可能是人为错误或欺骗攻击**："This could be either because of human error or a spoofing attack on an EVPN network." <<<PAGE 39>>>
- **X17 静默主机休眠失联**："These periods of inactivity can result in a loss of service binding, thus making the device effectively unreachable (for example for a WAKE-ON-LAN packet)." <<<PAGE 40>>>
- **X18 8-bit 本地段 ID 限制 ES 数量**："The 8-bit value will limit the number of locally configurable ES to a maximum of 256 Segments." <<<PAGE 43>>>
- **X19 SMET-by-all-PEs 的核心带宽浪费**："The disadvantage with this approach is that there will be traffic duplication in the core, wasting the bandwidth." <<<PAGE 43-44>>>
- **X20 Border leaf 泄漏主机路由压垮外部路由器**："The border leaf will advertise all the host routes to the external network leading to excessive load in both the control-plane and the data-plane of the external router." <<<PAGE 48>>>
- **X21 外部路由器路由回声（双 border leaf）**："it is possible for the external router to echo a route from one border leaf back to the other border leaf." <<<PAGE 48>>>
- **X22 多归属 SAP 配置不一致导致 CE 侧黑洞**："Please ensure that the SAP is configured consistently on all peer nodes of a MH-ES, otherwise... However, the CE side traffic towards the PE will be black-holed! (if the flow were to hash to the attached PE that has the missing config)." <<<PAGE 66>>>
- **X23 R-T10 源发现引入少量建流时延**："R-T10 based source discovery adds a little latency (additional delta time taken by PEG to generate RT-6 route plus traffic forwarding from source PE to PEG) when establishing data path." <<<PAGE 39>>>
- **X24 VLAN-aware 模型多归属两端 VLAN ID 必须一致**："Local and peer PE's in multi-homed segment should still have identical VLAN IDs." <<<PAGE 20>>>

## frameworks

## F1 EVPN 演进决策链：为什么选 EVPN（问题→方案映射框架）
传统模型的五类问题（资源低效 / 稳定性 / 可扩展性 / 运维复杂度 / tromboning）逐项映射到 VXLAN/EVPN 能力。用途：向客户论证技术选型。
- 数据：STP 阻塞链路 → routed underlay；4096 上限 → 24-bit VNI（约 1600 万）；洪泛学习 → 控制平面学习。<<<PAGE 5-9>>>
- 引用："Modern data centers required an evolution from the traditional flood-and-learn and VLAN segmentation networking due to the limitations placed on such model." <<<PAGE 5>>>
## F2 Underlay/Overlay 设计选型框架
决策变量：underlay 协议（OSPF/IS-IS/eBGP）× overlay（iBGP/eBGP）× RR 拓扑（全网状 vs 冗余 RR）。AOS 推荐态：OSPF 单区域 + p2p + BFD + 冗余 RR（同 cluster-id）+ iBGP overlay + TTL security 0。EVPN-VXLAN 限定单一 underlay VRF。
- 引用："Typically, the options which are configured in Data Center topologies, include OSPF/IS-IS underlay with an iBGP overlay, or eBGP for both underlay and overlay. The recommended topology to be used is an OSPF underlay with iBGP overlay." <<<PAGE 45>>>
## F3 IRB 模型选型框架（非对称 vs 对称 × host-based vs prefix-based）
决策变量：是否全 PE 配全 EVI、ARP/MAC-VRF 维护范围、SBD(L3EVI) 是否存在。判定：对称 IRB + interface-ful SBD 模型为主流推荐；prefix-based 只能走对称；host-based 两者皆可。RFC 9136 三模型（interface-less / interface-ful SBD / interface-ful unnumbered）按 overlay index 类型区分。
- 引用："The Symmetric IRB model is simpler for configuration and deployment and offers better scalability... and therefore is the prevalent and recommended configuration." <<<PAGE 24>>>
## F4 Multi-homing 模式与防环机制框架
决策链：单归属(SH) / 单活(SA) / 全活(AA) → LACP vs 静态 LAG（决定 ESI 自动/手工）→ DF 选举（service carving: DF = EVI mod N）→ 防环三件套（split horizon / local bias / ES pruning）→ 流量优化（aliasing 负载分担、backup path 主备、mass withdraw 快收敛）。
- 引用："The default algorithm used is a modulo-based algorithm, which is (DF = EVI mod N), where N is the number of PEs in the RT list." <<<PAGE 33>>>
## F5 BUM 复制与外部连通性设计框架
BUM：tandem replication（组播底层、核心高效、配置复杂）vs ingress replication（R-T3、简单、单播复制低效；AOS 仅支持后者）。外部连通：border leaf 位置 → Fabric-VPN + GRM 注入 → 路由汇总策略（route-map + ACL 只放聚合）→ 双 leaf 防回声（import 优先级）。
- 引用："Each of these methods have their pros and cons." <<<PAGE 29>>>；"A route-map policy needs to be defined with a specific ACL. This ACL will contain only the aggregate route for each IRB subnets." <<<PAGE 48>>>

## glossary

- **VXLAN**：基于 RFC 7348 的标准 L2 overlay 技术，将以太网帧封装进 UDP/IP 在 L3 网络中隧道传输。<<<PAGE 6>>>
- **VNI (VXLAN Network Identifier)**：24-bit 标识 VXLAN segment，上限约 1600 万逻辑网络。<<<PAGE 6>>>
- **VTEP (VXLAN Tunnel End Point)**：配置一个或多个 VTI 的设备，L2 帧封装/解封装端点。<<<PAGE 6>>>
- **VTI (VXLAN Tunnel Interface)**：在 VTEP 之间转发 VXLAN 封装包的 UDP 隧道。<<<PAGE 6>>>
- **VXLAN gateway**：作为 VTEP 在 VXLAN 与传统 VLAN 域之间透明桥接的设备。<<<PAGE 6>>>
- **EVI (Ethernet VPN Instance)**：跨所有 PE 的 EVPN 转发/路由实例，按客户配置，含 RD/RT。<<<PAGE 9>>>
- **BD (Broadcast Domain)**：广播域，可与 EVI 一一对应或一个 EVI 含多个 BD（视服务模型）。<<<PAGE 10>>>
- **ES (Ethernet Segment)**：连接一组 PE 的一组以太网链路。<<<PAGE 10>>>
- **ESI (Ethernet Segment Identifier)**：标识 ES 的唯一非零 10 字节标识符（如 11:22:...:99），多归属 CE 必需。<<<PAGE 10>>>
- **ETag (Ethernet Tag)**：标识特定广播域（如 VLAN），值为 SAP 关联的 VLAN ID。<<<PAGE 10>>>
- **MAC-VRF**：单个 EVI 的 MAC 地址 VRF 表。<<<PAGE 10>>>
- **IP-VRF**：PE 上 IP 路由的 VRF 表。<<<PAGE 10>>>
- **SAP (Service Access Point)**：PE 上绑定接入端口到服务的逻辑服务实体（虚拟端口），指定封装的客户流量类型。<<<PAGE 10>>>
- **PE (Provider Edge)**：服务 originates/terminates、与其他 PE 建隧道的设备；本文中与 VTEP 混用。<<<PAGE 10>>>
- **CE (Customer Edge)**：位于客户侧的主机/交换机/路由器。<<<PAGE 10>>>
- **MP-BGP EVPN**：基于 RFC 7432/8365 的 VXLAN 控制平面协议，AFI 25(L2VPN)/SAFI 70(EVPN)。<<<PAGE 9-10>>>
- **BUM traffic**：Broadcast/Unknown-unicast/Multicast 流量。<<<PAGE 9>>>
- **R-T1 (Ethernet A-D Route)**：多归属场景通告 ES 可达性；用于 aliasing、split horizon、mass withdraw；分 per-ESI(R-T1A, ETag=0xFFFFFFFF) 与 per-EVI(R-T1B) 两子类。<<<PAGE 11-13>>>
- **R-T2 (MAC/IP Advertisement Route)**：通告端主机 MAC（及可选 IP）可达性；支撑 ARP suppression/proxy ARP。<<<PAGE 11>>>
- **R-T3 (IMET, Inclusive Multicast Ethernet Tag Route)**：按 VNI 自动发现 VTEP 位置，构建 ingress replication 列表（BUM 隧道）。<<<PAGE 11>>>
- **R-T4 (Ethernet Segment Route)**：发现同 ES 的 PE 并执行 DF 选举；仅多归属 PE 生成。<<<PAGE 11>>>
- **R-T5 (IP Prefix Route)**：通告 IP 前缀（RFC 9136），用于外部连通与路由汇总、L3VPN；8.10R2 起支持。<<<PAGE 11>>>
- **R-T6 (SMET, Selective Multicast Ethernet Tag Route)**：IGMP/MLD proxy 功能，通告主机对 (*,G)/(S,G) 的组播兴趣。<<<PAGE 11>>>
- **R-T7 / R-T8 (IGMP Join/Leave Synch Route)**：多归属节点间同步 IGMP Join/Leave 状态。<<<PAGE 11>>>
- **RD (Route Distinguisher)**：8 字节，使不同租户/VRF 的重叠路由唯一；EVPN 用 RFC 4364 Type-1 RD（源于 Router ID/Loopback0）。<<<PAGE 19>>>
- **RT (Route Target)**：6 字节扩展社区，控制 MAC-VRF 的导入/导出；可多条；AOS 由 ASN+Etag(VNI) 自动派生。<<<PAGE 19>>>
- **VLAN-based service model**：VLAN:MAC-VRF:VNI:EVI 一一对应；ETag 必须为 0；允许 VLAN 转换。<<<PAGE 19>>>
- **VLAN bundle service model**：多 VLAN 共享一个 BD/EVI；ETag 必须为 0；不允许 VLAN 转换。<<<PAGE 20>>>
- **VLAN-aware service model**：一个 EVI 内多 VLAN 各自成广播域（ETag=VLAN）；MAC 可重叠。<<<PAGE 20>>>
- **Enhanced VLAN-bundle service interface**：ALE 定义模型；R-T1B/R-T2 带 ETag，每 EVI 仅一条 R-T3（ETag=0）；数据面同 VLAN-bundle（跨 ETag 的 MAC 不允许，视为 move）。<<<PAGE 41>>>
- **ARP suppression / Proxy ARP**：PE 代答本地 ARP 请求以抑制洪泛；AOS 默认开启。<<<PAGE 20-21>>>
- **GARP (Gratuitous ARP)**：主机主动发送的免费 ARP，可被 PE 用来学习 MAC+IP 并触发重复检测。<<<PAGE 21>>>
- **ES-Import RT Extended Community**：随 R-T4 携带，确保仅同 ES 的 PE 导入 ES 路由；6 字节由 ESI 自动编码。<<<PAGE 21>>>
- **ESI Label Extended Community**：R-T1A 携带；MPLS 下用于 split horizon 过滤并指示冗余模式（flags 1=single-active, 0=all-active）；VXLAN 不含 ESI label。<<<PAGE 21>>>
- **BGP Tunnel Encapsulation EC**：指示数据面封装类型；EVPN-VXLAN 为 8。<<<PAGE 22>>>
- **MAC Mobility Extended Community**：携带序列号跟踪主机最新位置，实现亚秒级 VM 迁移收敛。<<<PAGE 22>>>
- **Default Gateway Extended Community**：PE 以 R-T2 通告默认网关 MAC，ESI 置零，实现网关分布式。<<<PAGE 22>>>
- **DF Election Extended Community**：RFC 8584，标识 ES 使用的 DF 选举过程。<<<PAGE 22>>>
- **Router MAC Extended Community**：携带始发路由器 MAC；仅在 MAC 作 overlay index 的对称 IRB 场景使用。<<<PAGE 23>>>
- **IRB (Integrated Routing and Bridging)**：基于 EVPN 的动态高效跨子网连通方案，本地 PE 直接路由不同子网主机间流量。<<<PAGE 23>>>
- **Asymmetric IRB**：拉伸 EVI 设计；ingress PE 三次查表（桥-路由-桥）、egress 仅桥；资源与配置密集。<<<PAGE 24>>>
- **Symmetric IRB**：ingress/egress 均执行桥+路由；只需在主机接入 PE 配服务；推荐模型。<<<PAGE 24-25>>>
- **SBD (Supplementary Broadcast Domain) / Fabric-VPN**：每 VRF 一个的 L3EVI，提供 VRF 内所有 IRB 服务间可达与前缀路由网关；AOS 中记作 Fabric-VPN。<<<PAGE 25>>>
- **Host-based routing**：仅以 R-T2 通告主机 /32 路由；可用对称或非对称 IRB。<<<PAGE 26>>>
- **Prefix-based routing**：以 R-T5 通告任意长度前缀；仅对称 IRB；RFC 9136 定义 interface-less / interface-ful SBD / interface-ful unnumbered 三模型。<<<PAGE 26>>>
- **Overlay index**：R-T5 中的递归查找索引，可为网关 IP、MAC 或 ESI。<<<PAGE 15>>>
- **DAG (Distributed Anycast Gateway)**：所有共 EVI 的 PE 配同一 anycast IP + anycast MAC（每 VRF 一个 VMAC），无需 VRRP 类冗余协议即支持主机移动。<<<PAGE 28>>>
- **Anycast MAC auto-derivation**：自动派生规则 00:00:5e:00:01:<VRF-ID>；或 site-based（OUI+2 字节 site-id+1 字节 VRF-ID）。<<<PAGE 29>>>
- **Ingress replication**：头端复制，ingress 设备将 BUM 包逐个单播复制到远端 egress；AOS 唯一支持方式。<<<PAGE 29-30>>>
- **Tandem replication**：组播底层中继复制；核心高效但需组播底层。<<<PAGE 29>>>
- **PMSI (Provider Multicast Service Interface)**：R-T3 附带的隧道属性，标识 BUM 使用的 P-Tunnel（类型/标签/隧道标识）。<<<PAGE 15>>>
- **Multi-homing**：CE 经 LAG 连多 PE 的冗余接入；RFC 7432 定义 single-active 与 all-active 两模式。<<<PAGE 32>>>
- **DF (Designated Forwarder)**：ES 内选出的指定转发者，负责 BUM 从 fabric 到 CE 的转发，防止重复/环路。<<<PAGE 32-33>>>
- **Service carving**：按 EVI/VLAN 选举多 DF 分散 BUM 负载的默认 DF 选举过程；模算法 DF = EVI mod N。<<<PAGE 33>>>
- **Split Horizon Group (SPG)**：non-DF SAP 关联的 BUM 出方向过滤组，丢弃来自网络隧道的 BUM。<<<PAGE 34>>>
- **Local Bias / ES Pruning**：发往本 PE 上 all-active ES 的流量总走本地接入；远端 PE（含 DF）丢弃重复 BUM；BUM 位置 VXLAN 头置位。<<<PAGE 34>>>
- **Aliasing**：全活 ES 各 PE 通告 R-T1A/1B，远端据此构建 VTEP 列表按流负载分担。<<<PAGE 34>>>
- **Backup path**：单活场景 Primary/Backup PE 列表，主撤路时远端无缝切换。<<<PAGE 35-36>>>
- **Mass withdraw**：R-T1A 以 EVI=0xFFFFFFFF 编码 ES 不可达，远端批量刷新/清空关联 MAC 路径列表。<<<PAGE 36>>>
- **IPMS / IPMSv6**：OmniSwitch 的 IGMP/MLD snooping 实现，硬件线速组播交付。<<<PAGE 37>>>
- **OISM (Optimized Inter-Subnet Multicast)**：RFC 9625，基于 Fabric-VPN(SBD)+R-T6 的跨子网组播路由，无需 PIM；8.10R3 EA。<<<PAGE 37>>>
- **PEG (PIM EVPN Gateway)**：EVPN fabric 与外部 PIM 路由器互通的网关功能；双 PEG 时需专用 L3 互联链路；8.10R3 EA。<<<PAGE 38>>>
- **Default SBD-SMET route (*,*)**：RFC 9625 提议的内部源发现方式，PEG 借其收到全部组播流量；带宽低效，可改用 R-T10。<<<PAGE 38-39>>>
- **MAC duplication / hold-down**：MAC 反复迁移达到 N 次/M 秒阈值后进入 hold-down，停止处理该 MAC 的 BGP 通告直至 retry-time 结束。<<<PAGE 39>>>
- **DAD (Duplicate Address Detection)**：同 IP 出现在不同 MAC 的检测；N 次 IP-move/M 秒进入 filtering state，hold-down 3×M；用 unicast ARP Confirm 探测旧主。<<<PAGE 39>>>
- **Silent host**：长时间不发包（如省电模式）的设备，需静态绑 MAC 到 SAP 并以 sticky bit 通告。<<<PAGE 40>>>
- **Sticky bit**：静态 MAC 通告标志，远端节点不得触发该 MAC 迁移。<<<PAGE 40>>>
- **AOS auto-ESI (Type 0x3)**：物理口 0x3+Port_MAC+0xFFFFFF；LACP LAG 0x3+CE_MAC+0xFF+AggID；静态 LAG 手工 5 字节。<<<PAGE 41>>>
- **Auto-generated RD**：Loopback0 + 2 字节 Type + Object Type/ID（Service 0x0=VFI、ESI 0x1=8bit 段ID+5bit 片段ID（上限 256 段）、Prefix 0x2=VRF-ID）。<<<PAGE 42-43>>>
- **GRM (Global Route Manager)**：VRF 间/VRF 与 Fabric-VPN 间路由重分发中介。<<<PAGE 47>>>
- **Border leaf**：对外部网络做网关的 PE 节点；需路由汇总与防路由回声处理。<<<PAGE 46-48>>>
- **RR (Route Reflector)**：spine 兼任的 BGP 路由反射器；冗余 RR 建议 same cluster-id + TTL security。<<<PAGE 46>>>
- **TTL Security**：BGP 邻居直连性保障；max-hops 0 时直连断则邻居断。<<<PAGE 46>>>
- **UNP (Universal Network Profile)**：ALE 边到核自主多技术 fabric 的服务定义网络特性之一。<<<PAGE 72>>>
- **Virtual Chassis (VC)**：ALE 实现多归属的另一技术路线（与 EVPN multi-homing 相对）。<<<PAGE 32>>>

## principles

- **P1 用控制平面主动学习取代数据面洪泛学习**：endpoint reachability 通过 MP-BGP NLRI 智能通告，而非 flood-and-learn。"endpoint reachability information is advertised intelligently through the control plane within MP-BGP Network Layer Reachability Information (NLRI) updates." <<<PAGE 7>>>
- **P2 路由式底层（routed underlay）消灭 STP 问题**："The routed architecture eliminates STP issues." spine-leaf 全路由架构保证等价路径。<<<PAGE 8>>>
- **P3 单一控制平面同时承载 L2/L3 服务**："a single control plane protocol that supports Layer 2 and Layer 3 VPN services and allows for seamless integration." <<<PAGE 9>>>
- **P4 多租户隔离靠 VRF + VNI + RD/RT 四件套**："delivery of multi-tenant services across a shared infrastructure using Virtual routing and forwarding (VRF) instances, VNIs, Route Distinguishers (RDs), and Route Targets (RTs) for segmentation and control." <<<PAGE 9>>>
- **P5 控制平面学到的 MAC 不做老化**："MAC address table aging will be disabled for all MAC address learnt from the EVPN control plane." 以对端撤路为生命周期。<<<PAGE 13>>>
- **P6 ARP 抑制默认开启以减少 BUM**："Proxy ARP should always be kept enabled for performance." <<<PAGE 21>>>
- **P7 MAC mobility用序列号决胜**："the PEs retain the R-T2 with the highest sequence number." <<<PAGE 22>>>
- **P8 默认网关分布式化，流量不过 fabric**："it allows the default gateway to be fully distributed across all PEs in the EVPN fabric. Inter-subnet traffic for VMs connected in same PE does not need to cross the fabric." <<<PAGE 22>>>
- **P9 对称 IRB 优先于非对称 IRB**："The Symmetric IRB model is simpler for configuration and deployment and offers better scalability than the Asymmetric IRB model and therefore is the prevalent and recommended configuration." <<<PAGE 24>>>
- **P10 对称 IRB 下每 PE 只维护本地 ARP/MAC-VRF**："each PE participating in symmetric IRB only maintains ARP entries for locally connected hosts and MAC-VRFs for only locally configured subnets." <<<PAGE 25>>>
- **P11 每个 VRF 一个 L3EVI(SBD) 提供跨 EVI 可达**："only one L3EVI is required per VRF which will provide the inter-EVI reachability for all the IRB services in the VRF." <<<PAGE 25>>>
- **P12 主机路由用 R-T2、前缀路由用 R-T5**："Host routes (/32) are usually advertised using R-T2, while prefix routes are advertised using R-T5." <<<PAGE 15>>>
- **P13 LAG 是多归属防环/防重复包的前提**："LAG is required to be configured between the PE switches and the multi-homed CE device. This is to avoid receiving duplicate packets and for loop prevention." <<<PAGE 32>>>
- **P14 DF 选举防止 BUM 重复洪泛**："elect a Designated Forwarder (DF) for the ES. This is required for loop prevention and to prevent duplicate traffic." <<<PAGE 32>>>
- **P15 Service carving 按 EVI 分散 DF 负载**："It is also possible to elect multiple DFs per ES (one per VLAN) in order to perform load balancing of BUM traffic." DF = EVI mod N。<<<PAGE 33>>>
- **P16 Split horizon 原则：信息永不原路返回**："Information about the routing for a particular packet is never sent back in the direction from which it was received." <<<PAGE 34>>>
- **P17 VXLAN 下 split horizon 靠源 IP 列表而非 ESI label**："EVPN-VXLAN does not include the ESI label... The procedure used for split horizon is for each PE to track and maintain a list of peer PE IP address which are part of the same ES." <<<PAGE 34>>>
- **P18 Local bias：本 PE 的 BUM 只从本地 ES 出**："the forwarding to this ES from other access ports of the PE should always use the local access attachment." <<<PAGE 34>>>
- **P19 Aliasing 让远端按流负载分担到全活 ES**："The aliasing feature allows the remote PEs to perform per-flow load balancing of traffic to an all-active multi-homed ES." <<<PAGE 34>>>
- **P20 Mass withdraw：一条 ESI 撤路批量刷新 MAC**："a mass withdraw of the MAC addresses based on a single ESI update message." <<<PAGE 36>>>
- **P21 静默主机静态绑 MAC + sticky 位防误迁移**："statically binding the MAC address to the SAP port... advertised by BGP-EVPN with a sticky bit." <<<PAGE 40>>>
- **P22 自动生成 RD/RT 降低配置面**："Supports the auto-generation of the RD and RT for various EVPN R-T messages." <<<PAGE 40>>>
- **P23 优先用增强 VLAN-bundle 模型，互操作时回退 VLAN-based**："It is recommended to always use the enhanced VLAN-bundle service model for optimal performance, and to fall back to VLAN-based service model when required for inter-operability purposes." <<<PAGE 42>>>
- **P24 每 EVI 一条 R-T3 以减少路由数**："In case of ALE model, only one R-T3 is generated for an EVI, which is applicable to all ETags (hence ETAG = 0). This reduces the number of R-T3 routes in the network." <<<PAGE 41>>>
- **P25 速率与可用性权衡：SMET by all PEs 用带宽换丢包**："The disadvantage with this approach is that there will be traffic duplication in the core, wasting the bandwidth. So, this feature is recommended for customer scenarios in which the traffic loss is a concern." <<<PAGE 43-44>>>
- **P26 底层选 OSPF underlay + iBGP overlay**："The recommended topology to be used is an OSPF underlay with iBGP overlay." <<<PAGE 45>>>
- **P27 单区域 OSPF + p2p 网络类型 + BFD 提速收敛**："Use a single-area OSPF configuration to limit the SPF flooding domain." / "point-to-point OSPF network type... eliminates DR election wait times." / "BFD for millisecond fast-convergence." <<<PAGE 45-46>>>
- **P28 SPF delay/hold 调 0 立即算路**："Set OSPF SPF delay and hold timers to 0 to trigger SPF calculation immediately." <<<PAGE 50>>>
- **P29 冗余 RR 用相同 cluster-id 省内存**："Use the same cluster ID in the spines as it will save on memory usage and resources." <<<PAGE 46>>>
- **P30 RR 场景开 TTL Security max-hop 0**："it is recommended to enable TTL Security feature and set the max-hops to 0... will bring the BGP neighbor down when direct connection goes down." <<<PAGE 46>>>
- **P31 VXLAN MTU 由底层承担封装开销**："MTU should be considered in your underlay to allow for overhead of the VXLAN header. This is automatically adjusted in AOS." <<<PAGE 46>>>
- **P32 EVPN-VXLAN 只跑在一个 underlay VRF（默认 VRF）**："The EVPN-VXLAN is operational in only one underlay VRF which is usually the default VRF, with the overlay configured in a non-default VRF." <<<PAGE 46>>>
- **P33 外部连通必须走对称 IRB + Fabric-VPN**："it is mandatory to configure a Fabric-VPN for the PE(s) that needs reachability to the prefix-route." <<<PAGE 46>>>
- **P34 Border leaf 对外只重分发聚合路由，不泄漏主机路由**："there is a need to summarize the host routes under the subnet of their IRB interface... The border leaf will advertise all the host routes to the external network leading to excessive load." <<<PAGE 48>>>
- **P35 双 border leaf 防 OSPF 路由回声：调 import 路由优先级**："the import routes should have to be configured to have a higher route-preference than the OSPF routes (lower value than OSPF)." <<<PAGE 48>>>
- **P36 复制检测靠 N 次/M 秒阈值 + hold-down**："Duplicate IP detection monitors N 'IP-moves' within M-second timer. If there are N moves within M time interval, then the host is moved to 'filtering state' (F state)." <<<PAGE 39>>>
- **P37 确认旧主先于激活新主**："To detect the duplicate IP faster, the PE will send a Confirm message to the former owner of the IP." <<<PAGE 39>>>
- **P38 IP+MAC 同迁（VM motion）不算 DAD**："In case of VM mobility where the Host (IP+MAC) is moved from one ESI to another ESI, this is not considered as DAD." <<<PAGE 40>>>
- **P39 多归属场景 R-T7/R-T8 同步 IGMP 状态防丢**：无同步时 "All-active: There is no guarantee that IGMP Join and Leave packets will be sent to the DF for that ES"。<<<PAGE 36>>>
- **P40 源发现选 R-T10 而非 (*,*) 默认路由省带宽**："this approach makes the inefficient use of EVPN network bandwidth. The other approach is to inherit MVPN source discovery mechanism using R-T10." <<<PAGE 38-39>>>
- **P41 静态 LAG 必须手工给 ESI**："Static LAG — No [auto]... User will input manual 5-byte ESI." <<<PAGE 41>>>
- **P42 Anycast MAC 每 VRF 一个、同 VRF 全子网共用**："This anycast MAC must be setup per VRF and the same anycast MAC address is used for all subnet anycast IP interfaces of VRFs." <<<PAGE 28>>>
