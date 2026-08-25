# Verified 候选（V1 原文真实性核对 + V2/V3 抽查）

## cases

- **C1 MPLS 五收益论证案例**：BGP-free core、简单查找、自愈、流量工程、统一基础设施逐条展开。<<<PAGE 5-6>>>
- **C2 双标签封装-解封端到端流程**："The iLER binds the customer's traffic from the SAP... by 'pushing' the Service Label... Then another Transport label is added... Once the packet reaches the eLER, the top label (transport label) is 'popped' and the Service Label is processed and also 'popped'." <<<PAGE 20-21>>>
- **C3 LDP 邻居发现与会话建立流程**："LSRs start sending UDP-based LDP Hello messages on all links... After Hello messages are exchanged... they attempt to establish an LDP session between them using TCP-based messages... negotiate LDP session parameters by exchanging LDP Initialization messages." <<<PAGE 12>>>
- **C4 T-LDP 与直连 LDP 的场景对比**：远端 LER 间服务标签交换、链路故障时会话保持。"T-LDP, as can be observed from the name 'targeted', uses unicast UDP communication for discovery and unicast TCP to establish the session." <<<PAGE 15>>>
- **C5 push/swap/pop 三操作数据面走包**："the iLER inserts or 'push' a label... it 'swaps' or changes the top label... all labels are 'popped' or removed before the packet is switched out." <<<PAGE 16>>>
- **C6 PHP 与 explicit NULL 的 QoS 保留对比案例**："When the last LSR removes the top label, the EXP bits are also removed... The explicit NULL... will preserve the EXP bits in the explicit NULL label." <<<PAGE 16-17>>>
- **C7 QoS uniform/pipe 双模式行为**："In uniform mode, the IP precedence value... is copied to the EXP bits... In pipe mode, the EXP value is set according to the Service Provider's policy." <<<PAGE 18>>>
- **C8 TTL uniform/pipe 双模式（L3VPN 减 2、L2VPN 不变）**："In case of a Layer 3 VPN, the TTL is decremented by 1 at the iLER and again at the eLER, while for Layer 2 VPN, the TTL is not changed." <<<PAGE 19>>>
- **C9 LSP ping 实测案例**："mpls ping ldp 1.1.1.4/32" 5 发 5 中，min/avg/max = 0.67/1.30/1.94 ms。<<<PAGE 44>>>
- **C10 LSP traceroute 实测案例**："mpls trace ldp 1.1.1.4/32" 逐跳 TTL 递增发现 "0 20.2.1.2 [Labels: implicit-null]"。<<<PAGE 44>>>
- **C11 MPLS backbone 五步配置案例（R1 视角）**：接口 → 单区域 OSPF（p2p+BFD+SPF delay 0）→ 安装 uosn-mpls-v1.deb 包 → mpls interface → mpls ldp interface。<<<PAGE 29-31>>>
- **C12 LDP-VPLS 五步配置案例**：access port → SDP（far-end）→ service vpls vplsid + signaling ldp → SAP port 1/1/4:0 → bind-sdp 102 103（mesh，R1/R6/R7）。<<<PAGE 33-34>>>
- **C13 BGP-VPLS 四步配置案例**："ip bgp address-family l2vpn-vpls" + neighbor activate l2vpn-vpls + "service 2 vpls vplsid 11 signaling bgp ve-id 1" + SAP。<<<PAGE 34-35>>>
- **C14 VPWS 四步配置案例**：service vpws vcid 100 → SDP far-end → bind-sdp 20 spoke → 两端 SAP port 1/1/1:0、1/1/2:0，"The above configuration will setup a virtual bridge between port 1/1/1 on PE1 and port 1/1/2 on PE2." <<<PAGE 41-42>>>
- **C15 验证命令族全景案例**：show mpls / ftn-table / ilm-table / forwarding-table / ldp [neighbor|session]；show service [vpls|vpws|bind-sdp|mesh-sdp]；show ip bgp l2vpn-vpls [path]；show mac-learning domain vpls。<<<PAGE 31-44>>>
- **C16 FTN/ILM 表项解读案例**："FTN Code: B - BGP, L - LDP; OpCode: 1 = PUSH, 2 = POP, 3 = SWAP" 配真实表项输出。<<<PAGE 32>>>
- **C17 LDP 会话协商结果案例**："Advertisement mode = Downstream Unsolicited, Label retention mode = Liberal, Graceful restart = Enabled, Restarting mode = Helper." <<<PAGE 33>>>
- **C18 BGP VPLS 自动发现结果案例**："show ip bgp l2vpn-vpls path 50" 展示 VPLS-ID 50、VE Block Offset 1、Label Base 53122、Ext Community RT+MTU:9194。<<<PAGE 38-39>>>

## counter-examples

- **X1 核心 BGP 规模爆炸（不用 MPLS 时）**："the core routers do not need to support a large number of routes"（反面即核心被迫承载大量路由、成本上升）。<<<PAGE 5>>>
- **X2 LSR ID 不唯一导致不可预测行为**："It is important that the LSR ID, or the loopback address is unique in the MPLS domain to avoid any unpredictable behavior." <<<PAGE 13>>>
- **X3 Hello hold-timer 超时判死邻居**："if the timer expires without receiving a matching hello packet from the peer, LSR concludes that the peer is no longer alive and then deletes the Hello adjacency." <<<PAGE 12>>>
- **X4 Keepalive 超时终结会话**："If this timer expires, the LSR concludes that the transport connection is bad or that the peer has failed, and it terminates the LDP session by closing the transport connection." <<<PAGE 12>>>
- **X5 会话参数谈不拢则反复重谈**："If they agree, they maintain the LDP session, otherwise they will try to re-negotiate." <<<PAGE 12>>>
- **X6 MD5 密钥不匹配则建不起会话**："Authentication must be configured on both LDP peers using the same MD5 key (password), otherwise the peer session will not be established." <<<PAGE 14>>>
- **X7 MD5 签名不符静默丢弃 TCP 段**："silently rejects the TCP segment if the computed MD5 signature doesn't match with received MD5 signature." <<<PAGE 14-15>>>
- **X8 MD5 本身强度不足（RFC 建议更强算法）**："Currently MD5 key based authentication is proposed in the RFC but it also mentions that keychains with a stronger encryption algorithm like SHA can be implemented." <<<PAGE 14>>>
- **X9 implicit NULL 弹标签丢掉 EXP/QoS**："When the last LSR removes the top label, the EXP bits are also removed, thus removing any QoS values in the header." <<<PAGE 16-17>>>
- **X10 非 PHP 让 eLER 做两次查表**："This is to avoid performing two lookups in the MPLS FIB."（反面：不省性能）。<<<PAGE 16>>>
- **X11 OAM Alert Label 未广泛实现**："The Operation and Maintenance (OAM) Alert Label differentiates OAM packets from normal user data packets, but it is not widely implemented." <<<PAGE 10>>>
- **X12 非 GR 场景（非计划接管/链路断）流量中断**："supported only for planned takeovers... not unplanned takeovers (for example, the primary Chassis Management Modules (CMMs) unexpectedly fails) or when a link goes down between the two routers." <<<PAGE 19>>>
- **X13 无 T-LDP 时链路故障直接丢 LDP 会话**："when a link between two LSRs in an LSP fails without T-LDP, then the LDP session is lost." <<<PAGE 15>>>
- **X14 PW 回环风险（若无 split horizon）**："a PE must never send a packet on a PW if that packet has been received from a PW. This ensures that traffic cannot form a loop over the backbone network using PWs." <<<PAGE 21>>>
- **X15 MPLS 复杂度与性能成正比**："It's complexity is proportional to it's performance."（结论章自认的代价）。<<<PAGE 44>>>
- **X16 AOS 当前不支持项清单**："Only Downstream Unsolicited Mode is supported in the current release." / "Only Independent Label Distribution control is supported" / "Only Liberal Label Retention Mode is supported" / "Only MD5 key-based authentication is supported" / "Explicit NULL is currently not supported in AOS implementation." / "QOS over EXP bit is not supported" / "TTL manipulation is not supported for MPLS tag." <<<PAGE 13-17-19>>>
- **X17 配置示例偏离自身最佳实践（/24 代替 /31）**："It is recommended to consider using (/31) contiguous addresses for point-to-point links, but we have used in this configuration (/24)." <<<PAGE 29>>>
- **X18 未装 license 则 MPLS 接口起不来**："It is also required to install Site-based or Node-based license for MPLS interface to be up and running." <<<PAGE 30>>>

## frameworks

## F1 标签分发/控制/保留模式选型框架
三组正交决策：分发方式（DoD 按需 vs DU 主动）、控制模式（ILD 独立即刻通告 vs OLD 有序等下游标签）、保留模式（CLR 只留有效下一跳 vs LLR 全保留）。用途：解释/规划 LDP 行为与收敛特性；AOS 支持态为 DU+ILD+LLR。
- 引用："An LSR can use different modes to distribute label bindings to LDP neighbors... There are also two modes of control for label creation... There is also retention modes..." <<<PAGE 13-14>>>
## F2 L2VPN 服务选型框架（VPLS vs VPWS × EPL vs EVPL × 信令 LDP vs BGP）
决策链：连通需求（E-LAN 多点 vs E-LINE 点对点）→ VPLS 需全互联 PW + MAC 学习，VPWS 透明转发不学 MAC → VPWS 再分 EPL（整端口）/EVPL（按 C-VLAN 复用多条 PW）→ 信令选 T-LDP（手工 SDP/far-end）或 MP-BGP l2vpn-vpls（自动发现+信令一体，单 AS 需 full-mesh 或 RR）。
- 引用："The method of establishing VPLS with BGP accomplishes both auto-discovery and signaling." <<<PAGE 21>>>；"MEF 6.3 defines two types of P2P Ethernet VPWS services - EPL and EVPL." <<<PAGE 22>>>
## F3 MPLS 部署定位框架（园区 vs 城域）
决策变量：网络层级覆盖范围。园区中小型网：IP/MPLS 从接入到核心端到端；城域/Smart City：核心+汇聚跑 MPLS，接入层保持标准以太交换。共同前提：先 IGP 底层 + /32 loopback 唯一 Router-ID。
- 引用："For metro ethernet networks such as smart city networks, IP/MPLS network can be configured at the core and distribution layers of a three-tier network architecture." <<<PAGE 24-25>>>
## F4 双层标签服务模型框架（transport × service 二层解耦）
封装模型：服务只在 LER 存在（SAP/AC 面向 CE，SDP/VC 面向远端）；transport LSP（FEC=loopback）+ service tunnel（FEC=service id）标签栈叠加；传输隧道可换承载（LDP/RSVP-TE/静态）而不动服务层。用途：故障域隔离与排错分层（transport 层用 show mpls *，service 层用 show service *，OAM 用 mpls ping/trace）。
- 引用："There are two FECs associated with providing VPN services. One FEC for the service tunnel, which is the service identifier, and another is for the transport tunnel, which is the loopback interface for each LSR." <<<PAGE 20>>>
## F5 QoS/TTL 透明性选型框架（uniform vs pipe）
决策变量：是否让客户标记穿透运营商域。QoS：uniform 客户 DSCP 复制到 EXP 再回写；pipe 运营商自定 EXP、客户 DSCP 不动。TTL：uniform 复制 IP TTL 逐跳递减（traceroute 可见骨干）；pipe IP TTL 不变（L3VPN 仅两端各减 1、L2VPN 完全不变）。
- 引用："In uniform mode, the IP precedence value... is copied to the EXP bits... In pipe mode, the EXP value is set according to the Service Provider's policy and is independent of the customer's QoS markings." <<<PAGE 18>>>

## glossary

- **MPLS (Multiprotocol Label Switching)**：基于预分配标签的标签交换技术，转发不看内层 IP 头。<<<PAGE 5>>>
- **LER (Label Edge Router)**：MPLS 域边缘路由器（即 PE），负责 push/pop 标签；分 iLER/eLER。<<<PAGE 7>>>
- **LSR (Label Switch Router)**：MPLS 域内路由器，执行 swap；LER 也算 LSR。<<<PAGE 7>>>
- **LSP (Label Switched Path)**：从 iLER 到 eLER 的预确定传输隧道；单向。<<<PAGE 8>>>
- **FEC (Forward Equivalence Class)**：被赋同一标签的相似包集合（目标 IP 前缀/QoS 标记等），多与 LSP 对应。<<<PAGE 8>>>
- **LDP (Label Distribution Protocol)**：RFC 5036 定义的标签交换信令，依 IGP 路由建传输 LSP。<<<PAGE 8>>>
- **T-LDP (Targeted-LDP)**：远端 LER 间单播 UDP/TCP 会话，用于服务标签与服务隧道，兼提收敛与 TE。<<<PAGE 15>>>
- **MP-BGP**：RFC 2283，为服务交换路由+服务标签，并自动发现同服务 PE/隧道端点。<<<PAGE 15>>>
- **MPLS 标签结构**：32 位 shim 头 = 20-bit Label + 3-bit EXP + 1-bit S(BoS) + 8-bit TTL；又称 Layer 2.5 协议。<<<PAGE 9>>>
- **EXP bits**：MPLS 头中 3 个实验位，用于 QoS；仅顶层标签被处理。<<<PAGE 9>>>
- **S Bit / BoS (Bottom of Stack)**：标签栈底标志位。<<<PAGE 9>>>
- **保留标签 0-15**：0=IPv4 Explicit NULL、1=Router Alert、2=IPv6 Explicit NULL、3=Implicit NULL、14=OAM Alert。<<<PAGE 9-10>>>
- **标签栈 (Label Stacking)**：LIFO 多标签；VPN 中顶为 transport 标签、底为 service 标签；多数厂商支持 4-6 层。<<<PAGE 10>>>
- **FTN (FEC-To-NHLFE)**：FIB 中面向 Push 操作的条目。<<<PAGE 10>>>
- **ILM (Ingress Label Mapping)**：FIB 中面向 Swap/Pop 操作的条目；本地与远端标签绑定均存于此。<<<PAGE 10>>>
- **NHLFE (Next Hop Label Forwarding Entry)**：下一跳标签转发表项。<<<PAGE 10>>>
- **push / swap / pop**：LSR 三种标签操作（imposition/disposition 为 push/pop 别称）。<<<PAGE 16>>>
- **PHP (Penultimate Hop Popping)**：eLER 以 implicit NULL(3) 请求倒数第二跳弹掉传输标签以省一次查表。<<<PAGE 16>>>
- **Implicit NULL (label 3)**：PHP 信号标签。<<<PAGE 10-16>>>
- **Explicit NULL (0/2)**：保留 EXP 的 PHP 替代；AOS 当前不支持。<<<PAGE 16-17>>>
- **MPLS QoS uniform mode**：客户 IP precedence 复制进 EXP，出域再回写。<<<PAGE 18>>>
- **MPLS QoS pipe mode**：EXP 由运营商策略设定，客户 DSCP 不变。<<<PAGE 18>>>
- **MPLS TTL uniform/pipe mode**：uniform 复制 IP TTL 逐跳递减；pipe 中 L3VPN 两端各减 1、L2VPN 不变。<<<PAGE 19>>>
- **LDP 消息四类**：Discovery / Session / Advertisement / Notification；UDP 646 发现、TCP 646 会话、224.0.0.2 组播 hello。<<<PAGE 11-12>>>
- **Label Mapping / Withdraw / Release**：标签映射通告 / 撤销 / 释放三类核心通告消息。<<<PAGE 11-13>>>
- **DoD (Downstream-on-Demand)**：仅应答对端请求才发标签。<<<PAGE 13>>>
- **DU (Downstream Unsolicited)**：不待请求主动发标签；AOS 唯一支持；常配 LLR。<<<PAGE 13>>>
- **ILD (Independent Label Distribution)**：随时可通告标签映射；AOS 唯一支持。<<<PAGE 13-14>>>
- **OLD (Ordered Label Distribution)**：收到下游标签或自身为 egress 才通告。<<<PAGE 14>>>
- **CLR (Conservative Label Retention)**：只保留有效下一跳的标签绑定。<<<PAGE 14>>>
- **LLR (Liberal Label Retention)**：保留所有收到的标签绑定；AOS 唯一支持。<<<PAGE 14>>>
- **LDP ID**：6 字节 = 4 字节 LSR 唯一标识（loopback）+ 2 字节标签空间（0=per-platform）。<<<PAGE 13>>>
- **LDP MD5 认证**：为每个 TCP 段附加 MD5 签名防伪造；双方同钥。<<<PAGE 14-15>>>
- **LDP Graceful Restart**：RFC 3478，控制面重启期间保留转发状态（NSF）；仅计划内接管。<<<PAGE 19>>>
- **SAP (Service Access Point) / AC (Attachment Circuit)**：UNI 侧逻辑端口，绑定物理端口与客户流量类型到服务；同端口可多 SAP 复用。<<<PAGE 20>>>
- **SDP (Service Distribution Point) / VC**：NNI 侧单向逻辑连接，绑定服务到远端路由器；本地唯一 ID。<<<PAGE 20>>>
- **Service Tunnel**：在传输 LSP 内透明承载服务流量的虚拟链路（FEC=服务标识）。<<<PAGE 20>>>
- **Transport Tunnel**：基于 FEC 的单向传输路径（FEC=各 LSR loopback）。<<<PAGE 20>>>
- **VPLS (Virtual Private LAN Service)**：E-LAN 多点 L2VPN；需 PE 间全互联 PW 与 per-VPLS MAC 学习/桥接/复制。<<<PAGE 21>>>
- **PW (Pseudowire)**：LER 间的虚拟线路；VPLS 全互联成网。<<<PAGE 21>>>
- **VPWS (Virtual Private Wire Service)**：E-LINE 点对点 L2VPN；不学客户 MAC、透明转发；RFC 8077。<<<PAGE 21-22>>>
- **EPL (Ethernet Private Line)**：MEF 6.3 定义的整端口 VPWS 服务。<<<PAGE 22>>>
- **EVPL (Ethernet Virtual Private Line)**：基于 C-VLAN 复用的 VPWS 服务，单端口可多条 PW。<<<PAGE 22>>>
- **E-pipe**：PW 服务的别称，定义两 SAP 间的 E-LINE 虚拟专线。<<<PAGE 22>>>
- **VE-ID / VBO / VBS**：BGP VPLS 的站点标识与标签块偏移/尺寸参数（show ip bgp l2vpn-vpls path 可见）。<<<PAGE 38-39>>>
- **LSP Ping / Traceroute**：RFC 4379 的 MPLS OAM，echo request/reply 走标签验证数据面；目的 127/8、UDP 3503；traceroute 靠 TTL 递增逐跳发现。<<<PAGE 23-24>>>
- **Site-based license**：浮动共享 license，最多 4 网络节点（节点可为 8 单元虚拟机箱），由站点 license 服务器管理。<<<PAGE 26>>>
- **Node-based license**：绑定单个 MPLS 节点、不绑硬件序列号/MAC 的 license。<<<PAGE 26>>>
- **SILOS / SWLIC**：站点本地 license 服务器（Debian 包）/ 每台 MPLS 交换机上的 license 客户端。<<<PAGE 26>>>

## principles

- **P1 标签隧道换来 BGP-free core**："Since MPLS uses labelling as a tunnel mechanism, this allows for a BGP-free core network. This saves cost to the service provider since the core routers do not need to support a large number of routes." <<<PAGE 5>>>
- **P2 精确匹配优于最长匹配**："a simpler lookup process based on exact match rather than longest match lookup as in the case of routing." <<<PAGE 5>>>
- **P3 MPLS 底层必须先有 IGP 全可达**："MPLS is tunneling protocol which relies on the underlay network to be pre-configured with an IGP routing protocol to allow full reachability between LERs." <<<PAGE 10>>>
- **P4 服务只在有站点的 LER 上创建**："The service needs to be only created on LER nodes which are servicing the locations associated to the service." <<<PAGE 20>>>
- **P5 VPN 靠双层标签：transport 在顶、service 在底**："In a VPN implementation, the top label is the transport label and the bottom label is the service label." <<<PAGE 10>>>
- **P6 中间 LSR 不感知服务**："Intermediate LSR are unaware of the service tunnels and labels and only process the transport labels." <<<PAGE 21>>>
- **P7 LSP 单向，双向流量需两条**："LSPs are unidirectional... This means that two LSPs are required for bidirectional traffic flow." <<<PAGE 8>>>
- **P8 标签按 LIFO 出栈，栈深受硬件与包长限制**："sorted in a Last-In, First-Out (LIFO) fashion... The number of labels which can be stacked is unlimited, it depends however on the hardware support and the packet size. Most vendors support between 4 and 6 labels." <<<PAGE 10>>>
- **P9 PHP 用 implicit NULL 让倒数第二跳弹标签省一次查表**："the eLER assigns the implicit NULL label (label value 3) to a FEC to request the upstream LSR to perform a pop operation... This enhances the performance on the eLER." <<<PAGE 16>>>
- **P10 只有顶层（传输）标签的 EXP/TTL 被处理**："Only the EXP bits of the top label (transport label) is processed." / "only the Transport label TTL is decremented." <<<PAGE 18-19>>>
- **P11 VPLS split horizon：PW 进 PW 出禁止**："a PE must never send a packet on a PW if that packet has been received from a PW. This ensures that traffic cannot form a loop over the backbone network using PWs." <<<PAGE 21>>>
- **P12 VPLS 需 PE 具备每实例 MAC 学习/桥接/复制**："the PE must be capable of MAC learning, bridging and replication on a per-VPLS basis." <<<PAGE 21>>>
- **P13 VPWS 点对点不学 MAC、透明转发**："With a PW point-to-point connection, there is no forwarding decision to be made... customer MAC addresses are not learned on the SAP attachment points." <<<PAGE 22>>>
- **P14 T-LDP 保会话抗链路故障**："with T-LDP, the LDP session stays up since an alternative path may exist and negotiated labels are preserved." <<<PAGE 15>>>
- **P15 LSR ID（loopback）必须全网唯一**："It is important that the LSR ID, or the loopback address is unique in the MPLS domain to avoid any unpredictable behavior." <<<PAGE 13>>>
- **P16 hold-timer 取双方较低值，接口级覆盖全局**："Each proposes a hold time value, and the LSR uses the lower of the two hold-time values. The hold-time value set on the interface overrides the hold-time value set globally." <<<PAGE 12>>>
- **P17 LDP 不在面向 CE 的接口使能**："LDP should be enabled on all interfaces in the MPLS domain except towards the CE router (in the LER router)." <<<PAGE 12>>>
- **P18 LDP 认证双方必须同钥**："Authentication must be configured on both LDP peers using the same MD5 key (password), otherwise the peer session will not be established." <<<PAGE 14>>>
- **P19 标签分发从 eLER 向 iLER 上游泛洪**："LDP label distribution is propagated and flooded from the eLER upstream towards the iLER." <<<PAGE 14>>>
- **P20 一对 LSR 多链路仍只建一个（直连）会话**："In most cases, one LDP session is established even if multiple links exist between the LSRs." <<<PAGE 13>>>
- **P21 OAM 探测用 127/8 目的地址防 IP 转发泄漏**："The destination IP address will be an address from 127.x.x.x/8 subnet, which prevents the MPLS echo packets from being IP forwarded and exiting the egress provider edge router as an IP packet." <<<PAGE 23>>>
- **P22 Best Practice 清单：/32 loopback + Router-ID 唯一 + p2p + routed 接口 + BFD + /31 互联**："Configure a (/32) loopback interface on each switch... Assign the loopback interface as the Router-ID (make sure it is unique for each switch)... Consider using /31 contiguous (/31) addresses for point-to-point links." <<<PAGE 28>>>
- **P23 LDP 可靠性靠 hello/keepalive 双定时器双保险**："An LSR maintains a hold-timer with each Hello adjacency... a keepalive timer is used to monitor the integrity of the established session." <<<PAGE 12>>>
- **P24 传输隧道可由 LDP/RSVP-TE/静态任一种承载，T-LDP 依赖传输隧道建服务隧道**："T-LDP still depends on transport tunnels to establish the service tunnels. Transport tunnels can be created using LDP, RSVP-TE, or through static configuration." <<<PAGE 15>>>
- **P25 LSP 由下游 LER 发起建立**："LSPs will then be established between LERs to allow for full reachability. LSPs are established upstream from downstream LERs." <<<PAGE 10>>>
- **P26 单一 AS 内 BGP VPLS 用 RR 免全互联**："using MP-BGP will require either a full-mesh of peerings between LERs, or using Route Reflectors (RR)." <<<PAGE 21>>>
- **P27 Graceful Restart 只保计划内接管**："This mechanism is supported only for planned takeovers... not unplanned takeovers... or when a link goes down between the two routers." <<<PAGE 19>>>
- **P28 标签值范围 16 起步、0-15 保留**："Label: (20 bits)... with the first 16 values reserved for special use." <<<PAGE 9>>>
- **P29 MPLS 定位：园区端到端或城域核心+汇聚**：campus "implemented from the access to the core layer"；metro "configured at the core and distribution layers... At the access layer, ethernet standard switching will be configured." <<<PAGE 24-25>>>
- **P30 VPLS 是 VPWS 超集**："VPLS is a superset of VPWS. VPWS only provides point-to-point customer connectivity without providing any L2/L3 functionality." <<<PAGE 21>>>
- **P31 EVPL 靠外层 C-VLAN 复用多条 PW 于同一接入端口**："Multiple PWs can be associated with a single Access Port to allow service multiplexing. Multiplexing is based on the outer VLAN (C-VLAN) tag value." <<<PAGE 22>>>
- **P32 LSP ping/trace 验证数据面（控制面看似正常时）**："used to detect and isolate data plane failures in MPLS LSPs when IP reachability and MPLS control plane seem to be working fine." <<<PAGE 23>>>
- **P33 MPLS 是 Layer 2.5 协议（shim 头位置）**："The MPLS label sits between the IP Packet and the Ethernet header as a 'shim' header. This is the reason why it is sometimes referred to as a Layer 2.5 protocol." <<<PAGE 9>>>
