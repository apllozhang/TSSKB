# glossary.md · OmniSwitch LAN MPLS Concepts & Implementation (DT00XTE324EN)
# 来源: D:\Claude code\TSSKB\books\os-lan-mpls-impl (153 页教材，p115-146 为 Reference Design Guide)

- id: g01
  title: MPLS（多协议标签交换，Multiprotocol Label Switching）
  type: term
  source_chapter: "p27, p119"
  source_quote: |
    "MPLS is a forwarding mechanism in which packets are forwarded based on labels. ... MPLS is a label-switching technology where forwarding of traffic is based on pre-determined labels which are advertised between routers to build a label-to-label mapping."
  summary: |
    基于标签的转发机制：路由器间预先通告标签建立标签映射，MPLS 路由器只看附在 IP 包头的标签值转发，不查内层 IP 目的地址。标签通常对应 IP 目的网络，也可对应 QoS、源地址等参数（流量工程、不等价链路负载分担的基础）。标签头以 shim 垫片形式插在以太网头与 IP 包之间，故称"2.5 层"协议。核心好处：只有边缘路由器做路由查表、核心路由器只做简单标签查表交换。
  tags: [MPLS, 标签转发, 基础概念]

- id: g02
  title: FEC（转发等价类，Forwarding Equivalence Class）
  type: term
  source_chapter: "p32, p121"
  source_quote: |
    "A FEC is a group of IP packets forwarding in the same manner, over the same path, and with the same forwarding treatment ... In IP networks, the most used Forwarding Equivalence Class is the packet's destination Ip address (Prefixes)"
  summary: |
    按相同方式、走相同路径、享受相同转发处理的一组 IP 报文。传统 IP 路由中 FEC 查找每跳都做，且最常用 FEC 就是目的 IP 前缀；MPLS 中 FEC 查找只在 iLER 做一次，之后映射为标签沿 LSP 转发。MPLS 语境下 FEC 通常对应一条 LSP，也可按 QoS 标记等分类。
  tags: [FEC, 转发等价类, 基础概念]

- id: g03
  title: LSR（标签交换路由器，Label Switch Router）
  type: term
  source_chapter: "p35, p120"
  source_quote: |
    "The Label Switch Router (LSR) is a router that operates within the MPLS network and is connecting to other LSR Routers. ... An intermediate LSR is responsible to "swap" MPLS label from incoming packets as they transit through the MPLS network based on the LSP."
  summary: |
    MPLS 域内部的路由器，与其他 LSR 互联，对过境报文做标签交换（swap）。LER 也是一种 LSR，只是通常承担 push/pop 操作。标签由各 LSR 本地分配（仅本地唯一），每个 LSR 用 loopback 标识（LSR ID，必须全网唯一）。
  tags: [LSR, 标签交换, 角色术语]

- id: g04
  title: LER / iLER / eLER（标签边缘路由器，入/出方向）
  type: term
  source_chapter: "p35, p120"
  source_quote: |
    "The Label Edge Router (LER) is a router that operates at the edge of the MPLS network connecting to the Customer Edge (CE) router. ... It is the router responsible to "push" or insert an MPLS label into an incoming packet to the MPLS network and "pop" or remove an MPLS label from an incoming packet exiting the MPLS network. There are two types of LER routers, the ingress LER (iLER), and the egress LER (eLER)."
  summary: |
    MPLS 域边缘、连接 CE 的路由器（服务提供商术语里即 PE）。入方向 iLER 做 FEC 查找并 push 标签，出方向 eLER pop 标签后恢复 IP 转发；iLER/eLER 随数据流方向而定，同一台 LER 对不同流可同时是两者。AOS 中 VPLS 业务（service/sap/sdp）都配在 LER 上。
  tags: [LER, iLER, eLER, PE, 角色术语]

- id: g05
  title: PE / CE / P（服务架构三角色）
  type: term
  source_chapter: "p35"
  source_quote: |
    "MPLS Terminology
    iLER:  Ingress Label Edge Router
    eLER:  Egress Label Edge Router
    LSR: Label Switch Router
    Service Architecture Terminology
    PE:  Provider Edge Router
    CE:  Customer Edge Router
    P : Provider Core Router"
  summary: |
    服务架构视角的三角色：PE=运营商边缘路由器（对应 MPLS 域的 LER，业务终结点）、CE=客户边缘路由器（不跑 MPLS，通过 SAP 接入）、P=运营商核心路由器（域内 LSR，只做标签交换、不感知 VPN）。Lab 中 sw7/sw8 是 PE、sw9/sw10 是 P、6360/6560 是 CE 侧。讲解时注意 LER/LSR 是 MPLS 域术语，PE/CE/P 是业务架构术语，两组常混用。
  tags: [PE, CE, P, 角色术语, 服务架构]

- id: g06
  title: LSP（标签交换路径，Label Switched Path）
  type: term
  source_chapter: "p37, p121"
  source_quote: |
    "The Label Switched Path (LSP) is the transport tunnel or the pre-determined path which is defined to switch packets from the iLER to the eLER. LSPs are unidirectional."
  summary: |
    从 iLER 到 eLER 的传输隧道/预定路径，单向（unidirectional）——双向业务需要一对方向相反的 LSP。建法分逐跳（hop-by-hop，LDP 跟随 IGP 最优路径）与显式路径（RSVP-TE 按约束计算）。LDP 会话建立、标签分发完成后，域内自动形成全网状传输隧道 LSP。
  tags: [LSP, 隧道, 单向, 基础概念]

- id: g07
  title: Push / Swap / Pop（标签三操作）
  type: term
  source_chapter: "p36, p128"
  source_quote: |
    "There are three operations for an LSR to switch packets through a LSP: push, pop, and swap. The "push" operation is also sometimes refered to as "imposition" and the pop operation is referred to as "disposition"."
  summary: |
    Push（压入/imposition）：iLER 做 FEC 查找后给未打标报文插入标签；Swap（交换）：中间 LSR 替换栈顶标签沿 LSP 转发；Pop（弹出/disposition）：eLER 侧移除标签后送出 MPLS 域。show mpls ftn-table 的 Opcode 列（1-PUSH/2-POP/3-SWAP）即对应这三操作。
  tags: [Push, Swap, Pop, 数据面操作]

- id: g08
  title: 标签堆栈（Label Stacking）
  type: term
  source_chapter: "p38, p123"
  source_quote: |
    "This is implemented through label stacking, which is sorted in a Last-In, First-Out (LIFO) fashion. The first label which is "pushed" to the packet is called the top label, and the last label is called the bottom label. In a VPN implementation, the top label is the transport label and the bottom label is the service label."
  summary: |
    多个标签按后进先出（LIFO）堆叠：先压的是栈顶，最后压的是栈底（S=1）。VPN 实现中栈顶=传输标签（对应 LSP/loopback），栈底=服务标签（对应 vplsid/VC）。栈深理论上不限，实际受硬件与报文尺寸限制，多数厂商支持 4-6 层。VPLS 报文封装（p49 图示）即 Ethernet+MPLS(LSP 标签)+MPLS(VPN 标签)+Ethernet+IP。
  tags: [标签堆栈, 传输标签, 服务标签, LIFO]

- id: g09
  title: PHP（倒数第二跳弹出，Penultimate Hop Popping）
  type: term
  source_chapter: "p128"
  source_quote: |
    "An efficiency mechanism called Penultimate Hop Popping (PHP) is performed when an eLER assigns the implicit NULL label (label value 3) to a FEC to request the upstream LSR to perform a pop operation and remove the transport label."
  summary: |
    eLER 给 FEC 分配隐式 NULL(3)，由倒数第二跳 LSR 弹出传输标签，eLER 少做一次查表、性能提升。副作用：弹标签时 EXP 位（QoS）一并丢失，补救的显式 NULL 不被 AOS 支持（详见 ce03）。Lab 输出中直连网段 Out-Label=3/impl-null 就是 PHP。
  tags: [PHP, 隐式NULL, 性能机制]

- id: g10
  title: 隐式 NULL / 显式 NULL（保留标签 3 / 0）
  type: term
  source_chapter: "p122, p128-129"
  source_quote: |
    "0 IPv4 Explicit NULL Label
    1 Router Alert Label
    2 IPv6 Explicit NULL Label
    3 Implicit NULL Label
    14 OAM Alert Label"
  summary: |
    保留标签表（RFC 3032）：0=IPv4 显式 NULL、1=路由器告警、2=IPv6 显式 NULL、3=隐式 NULL、14=OAM 告警。隐式 NULL 用于 PHP——倒数第二跳直接弹标签；显式 NULL 用于想保留 EXP 位时把标签换为 0/2 传到 eLER。AOS 支持隐式 NULL/PHP，不支持显式 NULL（p129）。
  tags: [保留标签, 显式NULL, 隐式NULL, RFC3032]

- id: g11
  title: LIB 与 LFIB（标签信息库 / 标签转发表）
  type: term
  source_chapter: "p44, p46"
  source_quote: |
    "MPLS Protocols Exchange label Bindings for their FECs and build the LIB (Label Information Base)
    Label Bindings information is transferred to the DATA Plane and is stored in the LFIB (Label Forwarding Information Base)"
  summary: |
    控制面各协议（LDP/BGP 等）交换 FEC 的标签绑定形成 LIB（标签信息库，类比 RIB）；绑定信息下发到数据面存入 LFIB（标签转发信息库，类比 FIB），据此做线速标签转发。排障链路：RIB→FIB（IP 侧）、LIB→LFIB（标签侧），show mpls ftn-table/ilm-table/forwarding-table 看的就是 LFIB 视角。
  tags: [LIB, LFIB, 控制面, 数据面]

- id: g12
  title: FTN 与 ILM（转发表两类表项）
  type: term
  source_chapter: "p123, p140"
  source_quote: |
    "MPLS FIB comprises FTN (FEC To Next Hop label Forwarding Entry-NHLFE) and tunnel entries for requests for a Push operation and Ingress Label Mapping (ILM) entries for requests for a Swap/Pop operation."
  summary: |
    MPLS FIB 由两类表项组成：FTN（FEC 到下一跳标签转发项，服务于入方向 PUSH，"未打标→打标"的场景）和 ILM（入标签映射，服务于 SWAP/POP，"已打标→换标/弹标"的场景）。对应命令 show mpls ftn-table 与 show mpls ilm-table，两表配合还原一台 LSR 的完整标签转发行为。
  tags: [FTN, ILM, NHLFE, 表项, 排障]

- id: g13
  title: LDP（标签分发协议，Label Distribution Protocol）
  type: term
  source_chapter: "p121, p124"
  source_quote: |
    "Label Distribution Protocol (LDP) is a signaling protocol used in MPLS for label exchange and signaling to create LSP paths using the pre-determined routing information provided by the underlying IGP."
  summary: |
    RFC 5036 定义的标签分发协议：基于 IGP 提供的路由信息建立 LSP。发现用 UDP 646 发组播 224.0.0.2，会话用 TCP 646；消息四类（Discovery/Session/Advertisement/Notification）。AOS 默认 DU+ILD+LLR（见 p08 原则）。AOS 命令两级使能：mpls load ldp + mpls ldp admin-state enable（全局）、mpls ldp interface <if> admin-state enable（接口）。
  tags: [LDP, RFC5036, 信令协议]

- id: g14
  title: T-LDP（定向 LDP，Targeted-LDP）
  type: term
  source_chapter: "p126-127"
  source_quote: |
    "Targeted-LDP (T-LDP) is used when labels are required to be exchanged between remote LERs. In our case, it is used to establish the service labels and the service tunnel. ... T-LDP still depends on transport tunnels to establish the service tunnels. ... T-LDP ... uses unicast UDP communication to establish the adjacency and session."
  summary: |
    远端 LER 之间的 LDP 会话（非直连邻居），用于建立服务标签与服务隧道（VPLS 的 VC 标签）。用单播 UDP 建邻接与会话，但仍依赖底层传输隧道；附加价值：两 LSR 间链路故障时普通 LDP 会话丢失，T-LDP 会话可经替代路径保持、已协商标签保留，改善收敛。AOS 中由 service sdp <id> vpls far-end <对端 loopback> 触发建立。
  tags: [T-LDP, 定向会话, 服务隧道, VPLS]

- id: g15
  title: RSVP-TE（资源预留协议-流量工程，AOS 不支持）
  type: term
  source_chapter: "p121, p127"
  source_quote: |
    "Resource Reservation Protocol with Traffic Engineering extension (RSVP-TE), described in RFC 3209, which is sometimes refered to as MPLS-TE, is a signaling protocol that is used to establish LSPs and enables the allocation of resources along the path. ... Current implementation of IP/MPLS in AOS does not support RSVP."
  summary: |
    RFC 3209 定义的 LSP 建立协议，可按约束做流量工程与带宽预留：iLER 发 RSVP Path 消息下游到 eLER，eLER 分配标签后经 RSVP Resv 消息上游回传；用 DoD 模式分发标签，同样依赖 IGP。代价是管理开销大。注意：AOS 当前实现不支持 RSVP，需要带宽预留/TE 的方案在 AOS 上落不了地（见 ce05）。
  tags: [RSVP-TE, 流量工程, RFC3209, 不支持特性]

- id: g16
  title: MP-BGP 与 l2vpn-vpls 地址族（多协议 BGP）
  type: term
  source_chapter: "p127"
  source_quote: |
    "MP-BGP, which is defined in RFC 2283, may be used by the Service Provider to exchange routes of a particular Service among the LERs that are attached to that Service. Each route within a VPN is assigned an MPLS Service Label and BGP is used to distribute the route and the label. ... The multiprotocol capabilities of BGP also enables the auto discovery of PE's or tunnel end point in the same service instance."
  summary: |
    多协议 BGP 扩展（RFC 2283，NLRI+AFI）：为 VPN 内每条路由/实例分配 MPLS 服务标签并用 BGP 分发路由+标签；在 VPLS 场景中完成同一实例内 PE/隧道端点的自动发现与信令（一步到位，对应 RFC 4761）。AOS 配置关键句：ip bgp address-family l2vpn-vpls、每邻居 activate l2vpn-vpls。验证 show ip bgp l2vpn-vpls [path]，输出含 VE-ID、RD、VBO/VBS、LabelBase。
  tags: [MP-BGP, l2vpn-vpls, RFC2283, 自动发现]

- id: g17
  title: SAP（业务接入点，Service Access Point）
  type: term
  source_chapter: "p50, p131"
  source_quote: |
    "Service Access Point (SAP): A UNI-side logical port which binds a physical port and spcific customer traffic types to a service. It is the point where the customer traffic ingress/egress the MPLS network. Multiple SAPs can be associated to the same physical port"
  summary: |
    UNI 侧逻辑端口，把物理口与特定客户流量封装绑定到服务，是客户流量进出 MPLS 网络的出入口；同一物理口可挂多个 SAP 复用不同客户封装。AOS 配置两步：service access port <slot/port> 声明业务接入口，service <id> sap port <slot/port>:<vlan-id> 挂到服务（:0 表示 untagged）。show 输出中 MAC 从 sap:x:y 接口学到。
  tags: [SAP, UNI, 接入点, AOS配置]

- id: g18
  title: SDP（业务分发点，Service Distribution Point）
  type: term
  source_chapter: "p50, p131"
  source_quote: |
    "Service Distribution Point (SDP): An NNI-side logical port which binds a service to a far-end router over which MPLS encapsulated packets are distributed."
  summary: |
    NNI 侧逻辑端口，把服务绑定到远端路由器，MPLS 封装报文经它分发。LDP-VPLS 中手工配置：service sdp <id> vpls far-end <对端 loopback>，再 service <id> bind-sdp <sdp-id> 绑到服务触发 T-LDP 协商 VC 标签；一条 SDP 可被多个服务复用、一个服务可绑多条 SDP（p78 样例）。BGP-VPLS 则由自动发现生成（表项显示 sdp:32768:x）。show service sdp / show service bind-sdp 查看。
  tags: [SDP, NNI, 远端绑定, AOS配置]

- id: g19
  title: PW / 伪线（Pseudowire）
  type: term
  source_chapter: "p119, p133"
  source_quote: |
    "Layer 2 VPN (L2VPN) services such as Virtual Private Wire Service (VPWS) or Pseudowire (PW) Service, Virtual Private LAN Service (VPLS) ... A full-mesh of PWs needs to be established between LERs to form a VPLS."
  summary: |
    在 MPLS 骨干上模拟二层链路的隧道，是 L2VPN 的承载基础。VPLS 中 LER 之间必须建全网状 PW（配合 Split Horizon 防环）；点对点形态即 VPWS/E-Pipe（AOS 不支持）。PW 的服务标签即 VC 标签（LDP-VPLS 中 bind-sdp 时由 CMM 建立）。
  tags: [PW, 伪线, 伪线, L2VPN]

- id: g20
  title: VPWS / E-Pipe（虚拟专线业务，AOS 不支持）
  type: term
  source_chapter: "p132"
  source_quote: |
    "Defined in RFC 8077, a Pseudo-wire service, also called E-pipe, is used to define a virtual wire (E-LINE) connection between two local SAPs or between two SAPs across the SPB network. ... With a PW point-to-point connection, there is no forwarding decision to be made; packets simply enter one end of the connection and leave the other end of the connection unchanged. As a result, customer MAC addresses are not learned on the SAP attachment points. ... VPWS is not supported in the current implementation of AOS."
  summary: |
    RFC 8077 定义的点对点二层虚拟专线（E-LINE）：两个 SAP 间透明传送，无转发决策、不学客户 MAC、报文原样进出，流量模型简单、硬件开销低。注意 AOS 当前不支持 VPWS，客户要"以太专线"时需用两点 VPLS 等效实现（见 ce05）。
  tags: [VPWS, E-Pipe, E-LINE, RFC8077, 不支持特性]

- id: g21
  title: VPLS（虚拟专用局域网业务，Virtual Private LAN Service）
  type: term
  source_chapter: "p132-133"
  source_quote: |
    "VPLS is an L2VPN service that allows any-to-any (multipoint) connectivity (E-LAN). The provider network emulates a LAN by connecting all the customer's remote sites at the edge of the provider network to a single bridged LAN. ... As VPLS is an Ethernet layer 2 service, the PE must be capable of MAC learning, bridging and replication on a per-VPLS basis."
  summary: |
    任意到任意（多点）的二层 VPN（E-LAN）：把客户各远端站点桥接成一张局域网。CE-PE 之间跑以太网，PE 需按 VPLS 实例做 MAC 学习、桥接与复制。AOS 支持两种信令：LDP（RFC 4762，手工 SDP/T-LDP）与 BGP（RFC 4761，自动发现+信令）。本课程三个 Lab 的主角，配置入口 service <id> vpls vplsid <x> signaling {ldp|bgp}。
  tags: [VPLS, E-LAN, L2VPN, RFC4761, RFC4762]

- id: g22
  title: Split Horizon（水平分割，VPLS 防环规则）
  type: term
  source_chapter: "p133"
  source_quote: |
    "the so-called "Split Horizon" rule is used. In the VPLS context, this rule basically implies that a PE must never send a packet on a PW if that packet has been received from a PW."
  summary: |
    VPLS 骨干防环的核心规则：从伪线收到的报文不得再从任何伪线发出。因为 PE 间伪线总是全网状，广播可达所有站点，规则保证流量不会在骨干里成环。VPLS 因此不需要在骨干跑 STP。
  tags: [Split-Horizon, 防环, VPLS]

- id: g23
  title: VE-ID（VPLS 边缘标识，BGP 信令用）
  type: term
  source_chapter: "p75, p144"
  source_quote: |
    "service 2 vpls vplsid 200 signaling bgp ve-id 1 description "VPLS instance 200 with bgp signaling" admin-state enable" (p75)
    "VPLS-ID    VE-ID        Route-Target   Route-Distinguisher   Discovered-Peers" (p144)
  summary: |
    BGP-VPLS 中标识每个 VPLS 边缘（VE）站点的编号，在 service ... signaling bgp ve-id <n> 中配置，同一 VPLS 实例内各 PE 必须取不同值（Lab 中 sw7=1、sw8=2）。show ip bgp l2vpn-vpls [path] 输出中与 VPLS-ID、RD、VE Block Offset/Size、LabelBase 一起呈现，用于核对自动发现结果。
  tags: [VE-ID, BGP-VPLS, 自动发现]

- id: g24
  title: vlan-xlation（VLAN 转换，ITAG/OTAG）
  type: term
  source_chapter: "p79-80"
  source_quote: |
    ""ITAG" and "OTAG" refer to inner tag and outer tag, respectively
    To enable translation at the service level, use the service vlan-xlation command.
    To enable VLAN translation at the port level, use the service access vlan-xlation command."
  summary: |
    AOS 的 VLAN 转换特性，分服务级（service <id> vlan-xlation enable）与端口级（service access port <port> vlan-xlation enable）两层使能，教材次序先端口后服务。ITAG=内层标签、OTAG=外层标签。用于两端站点 VLAN 规划不一致时在 VPLS 边缘改写标签；注意 :0 untagged SAP 的出口行为约束（ce08）。sh service 中 Vlan Translation 字段显示是否启用。
  tags: [vlan-xlation, VLAN转换, ITAG, OTAG, AOS特性]

- id: g25
  title: SILOS 与 SWLIC（站点许可服务器 / 交换机许可客户端）
  type: term
  source_chapter: "p62-63, p135-136"
  source_quote: |
    "The SILOS (Site Local Licensing Server) is available as a ALE Debian software package that runs on a switch or a virtual chassis acts as a server issuing the site or node licenses to the sites and nodes. SWLIC (Switch Local Licensing client) runs on every MPLS-enabled switch in the network and acts as a client getting the site or node licenses from the SILOS."
  summary: |
    AOS 许可体系两角色：SILOS（站点本地许可服务器）以 Debian 包跑在某台交换机/VC 上，向站点和节点发放许可，配置 license server ip-address <ip> listen-port 8883 admin-state enable；SWLIC（交换机本地许可客户端）默认内置于 AOS 镜像，跑在每台 MPLS 交换机上，经安全 MQTT（Secure MQTT）与 SILOS 通信取许可，配置 license client site-id Master server-ip <ip> server-port 8883。许可文件在 ALE Portal 生成后装到 SILOS。查看：show license-server usage/info、sh license-info。
  tags: [SILOS, SWLIC, 许可架构, MQTT, AOS特性]
