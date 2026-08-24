# principles.md · OmniSwitch LAN MPLS Concepts & Implementation (DT00XTE324EN)
# 来源: D:\Claude code\TSSKB\books\os-lan-mpls-impl (153 页教材，p115-146 为 Reference Design Guide)

- id: p01
  title: MPLS 许可类型：站点许可浮动共享 4 节点 / 节点许可独立绑定
  type: principle
  source_chapter: "p52, p135"
  source_quote: |
    "Two types of licenses are supported:
    Site-based licenses
    Floating/shared license
    Shared by 4 network nodes
    Network node can be a standalone switches or a VC of up to 8 units
    Node-based licenses
    Specific to any MPLS node
    Not bound to HW and are not tied to Node's serial number and mac-address"
  summary: |
    AOS 中 MPLS 是受许可控制的特性（支持平台 OS6860N）。站点许可（Site-based）可浮动/共享，最多覆盖 4 个网络节点，一个网络节点可以是独立交换机或最多 8 台的虚拟机箱（VC），到期/吊销/转移等管理都由站点许可服务器处理；节点许可（Node-based）绑定单个 MPLS 节点，与硬件序列号、MAC 无关。两类许可都在 ALE Licensing Portal 购买生成。客户交换机多于 4 台时可购买多个站点/节点许可。
  tags: [许可, Site-license, Node-license, VC, ALE-Portal]

- id: p02
  title: MPLS 以 Debian 包动态安装，首版 8.9R3 仅 OS6860N
  type: principle
  source_chapter: "p59, p118"
  source_quote: |
    "IP/MPLS first supported release is 8.9R3 and supported on the OmniSwitch 6860N platform. AOS supports installation or removal of AOS MPLS package. MPLS is packaged into a Debian package which can be installed on the switch. To configure MPLS in AOS, it is required to install the MPLS package using Package Manager commands"
  summary: |
    AOS 的 MPLS 是可独立装卸的 Debian 软件包：pkgmgr install uosn-mpls-v1.deb 安装（包文件需先拷到 /flash/working/pkg）、pkgmgr verify 校验、show pkgmgr 确认。装包后 MPLS 进程即加载，但 LDP/BGP 模块还要分别执行 mpls load ldp、ip load bgp 才加载。首个支持版本为 AOS 8.9R3，支持平台 OmniSwitch 6860N——售前确认软硬件版本时以此为准。
  tags: [pkgmgr, Debian包, 8.9R3, OS6860N, 版本要求]

- id: p03
  title: Loopback0 作为系统 IP 是 OmniSwitch 的特有前置要求
  type: principle
  source_chapter: "p58"
  source_quote: |
    "A Loopback0 interface that will serve as the system IP address to identify the router as an MPLS router. This requirement is specific to the OmniSwitch."
  summary: |
    配置 MPLS 接口的三个前提：已装站点或节点许可、稳定的 IP 网络拓扑（MPLS 隧道要穿越其上）、每台交换机一个 Loopback0 接口充当系统 IP 来标识 MPLS 路由器——最后一点是 OmniSwitch 特有的要求。Lab 中四台交换机分别配 192.168.254.7/8/9/10，参考设计样例用 1.1.1.1/32。BGP 邻居的 update-source 也指向它。
  tags: [Loopback0, 系统IP, 前置条件, OmniSwitch]

- id: p04
  title: MPLS 部署最佳实践七条
  type: principle
  source_chapter: "p136"
  source_quote: |
    "Configure IGP (OSPF/IS-IS) as an underlay in your network
    Configure a (/32) loopback interface on each switch to be used and advertise it into your IGP
    Assign the loopback interface as the Router-ID (make sure it is unique for each switch)
    Configure the OSPF/IS-IS network type as point-to-point between your switches
    Use routed interfaces
    Use Bidirectional Forwarding Detection (BFD) for fast detection and convergence
    Consider using /31 contiguous (/31) addresses for point-to-point links"
  summary: |
    Reference Design Guide 的最佳实践：用 OSPF/IS-IS 做 underlay；每台交换机配 /32 loopback 并宣告进 IGP；loopback 作 Router-ID 且全网唯一；交换机互联链路 OSPF/IS-IS 网络类型设 point-to-point；用路由接口（routed interface）；启用 BFD 加快检测与收敛；点对点链路建议用 /31 连续地址（教材示例中实际用了 /24，是可读性取舍）。
  tags: [最佳实践, OSPF, BFD, /31, point-to-point, underlay]

- id: p05
  title: 标签分配规则：直连路由=隐式 NULL(3)，其余从 16 起，0-15 保留
  type: principle
  source_chapter: "p100, p122"
  source_quote: |
    "Any directly connected route is allocated the special label Implicit NULL, i.e. 3.
    Any other route is allocated a label starting at 16 (the maximum limit depends on the equipment).
    Labels from 0 to 15 are in fact special labels reserved in RFC 3032."
  summary: |
    标签由各 LSR 本地分配，只有本地唯一性（不同 LSR 可用同一标签值）。规则：直连路由分配特殊标签隐式 NULL（值 3）；其他路由从 16 开始分配（上限因设备而异，show mpls 可见 AOS 配置为 16~1048575）；0-15 为 RFC 3032 保留标签（0=IPv4 显式 NULL、1=路由器告警、2=IPv6 显式 NULL、3=隐式 NULL、14=OAM 告警）。Lab 输出中 forwarding-table 的 impl-null 与 52480+ 的标签值即对应这两类。
  tags: [标签分配, 隐式NULL, RFC3032, 保留标签]

- id: p06
  title: MPLS 标签头 32 位结构与"2.5 层"位置
  type: principle
  source_chapter: "p34, p122"
  source_quote: |
    "MPLS label header is 32 bits (4 bytes) and includes the following fields:
    Label: (20 bits) This is the label value which are in a range of 0-1048575 with the first 16 values reserved for special use.
    EXP: (3 bits) These are the experimental bits used for QoS applications.
    S Bit or Bottom of Stack (BoS): (1 bit)
    Time To Live (TTL): (8 bits)"
  summary: |
    MPLS 标签头 32 位（4 字节）：Label 20 位（0-1048575，前 16 个保留）、EXP 3 位（QoS 用）、S 位/栈底标志 1 位（=1 表示栈底）、TTL 8 位（防环，逐跳减 1，到 0 丢包）。标签头以"垫片"（shim）形式插在以太网头与 IP 包之间，所以 MPLS 常被称为 2.5 层协议。讲解报文结构或排查 EXP/TTL 问题时以此为准。
  tags: [标签结构, shim, EXP, TTL, BoS]

- id: p07
  title: LDP 传输参数：224.0.0.2 发现、UDP 646/TCP 646
  type: principle
  source_chapter: "p124"
  source_quote: |
    "LDP uses the reserved multicast address for "all-routers" 224.0.0.2 and uses UDP port 646 for discovery messages to establish sessions between LDP neighbors and TCP 646 for the remaining messages."
  summary: |
    LDP（RFC 5036）发现报文（Hello）走 UDP 646 发往组播 224.0.0.2；邻居发现后建立会话，其余消息（Initialization、KeepAlive、Label Mapping/Withdraw/Release 等）走 TCP 646。LDP 消息四大类：Discovery、Session、Advertisement、Notification。做防火墙放行、抓包过滤时直接用这组参数。
  tags: [LDP, UDP646, TCP646, 224.0.0.2, RFC5036]

- id: p08
  title: AOS LDP 默认模式：下游主动分配 DU + 独立控制 ILD + 自由保留 LLR
  type: principle
  source_chapter: "p125-126, p96"
  source_quote: |
    "Downstream Unsolicited (DU) Mode: This parameter distributes labels to peers without waiting for a label request. This is the default mode in AOS.
    Independent Label Distribution (ILD) Control: ... This is the default mode in AOS.
    Liberal Label Retention (LLR) Mode: Retain all labels binding to FEC received from label distribution peers, even if the LSR is not the current next-hop. ... This is the default mode in AOS."
  summary: |
    标签分发三个维度及 AOS 默认值：分配方式=下游主动（DU，不等请求就发标签），替代方案是下游按需（DoD，RSVP-TE 用）；控制模式=独立分发（ILD，随时可通告映射），替代是有序分发（OLD，等下游标签到位才上游通告）；保留模式=自由保留（LLR，保留所有学到的绑定，包括非当前下一跳的，链路倒换快但占资源），替代是保守保留（CLR）。Lab 输出印证：show mpls ldp session 显示 Advertisement mode = Downstream Unsolicited、Label retention mode = Liberal。
  tags: [LDP, DU, ILD, LLR, 默认模式]

- id: p09
  title: LDP hold-time 协商规则与默认定时器
  type: principle
  source_chapter: "p125, p141"
  source_quote: |
    "Each proposes a hold time value, and the LSR uses the lower of the two hold-time values. The hold-time value set on the interface overrides the hold-time value set globally. The same also applies to Keepalive time and Keepalive timeout."
  summary: |
    两台 LSR 各自提议 hold-time，取两者中较小值生效；接口级配置覆盖全局配置（Keepalive 时间与超时同理）。AOS 默认值（show mpls ldp）：Hello 间隔 5s、Hold time 15s、Targeted Hello 15s、Targeted Hold 45s、Keepalive 间隔 10s、超时 30s，Graceful Restart 使能。Lab 的 show mpls ldp interface 输出也显示 Hello-Interval 5 / Hold-Time 15。调定时器时记住"取小者"规则，只改一端可能不生效。
  tags: [LDP, hold-time, keepalive, 定时器]

- id: p10
  title: LDP 会话与 LDP ID 结构（多链路单会话、per-platform 标签空间）
  type: principle
  source_chapter: "p125"
  source_quote: |
    "In most cases, one LDP session is established even if multiple links exist between the LSRs. LSRs that are running LDP have an LDP Identifier, or LDP ID. This LDP ID is a 6-byte field that consists of 4 bytes identifying the LSR uniquely (the loopback address) and 2 bytes identifying the label space that the LSR is using. If the last two bytes are 0, the label space is the platform-wide or per-platform label space"
  summary: |
    两台 LSR 之间即使有多条链路，通常也只建立一个 LDP 会话（走 TCP）。LDP ID 共 6 字节 = 4 字节 LSR 唯一标识（loopback 地址）+ 2 字节标签空间编号；末 2 字节为 0 表示整平台标签空间（per-platform，常用实现），非 0 表示按接口标签空间。Lab 中 show mpls ldp neighbor 显示的 192.168.254.10:0 即此格式。排查"物理口多但会话只有一个"时属正常行为。
  tags: [LDP, LDP-ID, 标签空间, 会话]

- id: p11
  title: MPLS 依赖 underlay IGP 先行全可达
  type: principle
  source_chapter: "p123"
  source_quote: |
    "MPLS is tunneling protocol which relies on the underlay network to be pre-configured with an IGP routing protocol to allow full rechability between LERs. Open Shortest Path First (OSPF) and Intermediate System to Intermediate System (IS-IS) are usually configured in the MPLS backbone network."
  summary: |
    MPLS 是隧道协议，前提是 underlay 已用 IGP（OSPF 或 IS-IS）配好且 LER 之间全可达；路由表（RIB）选出最优路由进 FIB 后，LDP 再基于 IGP 的最优路径建立全网状传输隧道 LSP。每个 LSR 的 loopback 用于相互可达。实施顺序永远是"先 IGP 后 MPLS"，Lab 1 也是先完成 OSPF 并确认 sh ip routes 全部学到的。
  tags: [underlay, IGP, OSPF, IS-IS, 依赖关系]

- id: p12
  title: PHP 倒数第二跳弹出机制与目的
  type: principle
  source_chapter: "p128"
  source_quote: |
    "An efficiency mechanism called Penultimate Hop Popping (PHP) is performed when an eLER assigns the implicit NULL label (label value 3) to a FEC to request the upstream LSR to perform a pop operation and remove the transport label. This is to avoid performing two lookups in the MPLS FIB. This enhances the performance on the eLER."
  summary: |
    PHP：eLER 给 FEC 分配隐式 NULL（3），让倒数第二跳 LSR 直接弹出传输标签，eLER 免做两次查表，性能更优。Lab 输出可见去向邻接网段的 Out-Label=3 即 PHP 生效。代价见 ce03：弹掉顶层标签时 EXP 位一并丢失。显式 NULL 可保 EXP，但 AOS 当前不支持（p129）。
  tags: [PHP, 隐式NULL, eLER, 性能优化]

- id: p13
  title: VPN 双层标签栈：传输标签在上、服务标签在下
  type: principle
  source_chapter: "p38, p123, p131"
  source_quote: |
    "In a VPN implementation, the top label is the transport label and the bottom label is the service label.
    This is implemented through label stacking, which is sorted in a Last-In, First-Out (LIFO) fashion. ... The number of labels which can be stacked is unlimited, it depends however on the hardware support and the packet size. Most vendors support between 4 and 6 labels."
  summary: |
    标签栈 LIFO 组织：先 push 的是栈顶（传输标签，对应 LSP/loopback FEC），后 push 的是栈底（服务标签，对应 vplsid FEC）。iLER 先压服务标签再压传输标签；中间 LSR 只 swap 传输标签、不感知服务隧道；eLER 弹传输标签后处理并弹出服务标签。栈深理论上无限，实际受硬件与包大小限制，多数厂商支持 4-6 层。两个 FEC 分别对应服务隧道与传输隧道（p131）。
  tags: [标签堆栈, 传输标签, 服务标签, LIFO]

- id: p14
  title: 服务模型三要点：只建在 LER、SAP/SDP 分工、按 VPLS 做 MAC 学习
  type: principle
  source_chapter: "p131, p133"
  source_quote: |
    "An MPLS service represents a VPN, or tenant and is uniquely identified by it's service identifier. The service needs to be only created on LER nodes which are servicing the locations associated to the service.
    As VPLS is an Ethernet layer 2 service, the PE must be capable of MAC learning, bridging and replication on a per-VPLS basis."
  summary: |
    服务（VPN/租户）用服务标识唯一标识，只在服务相关站点的 LER 上创建，中间 P/LSR 不感知。VPLS 作为以太网二层业务，PE 必须具备按 VPLS 实例的 MAC 学习、桥接和复制能力——这也是 show mac-learning domain vpls 能看到 sap: 与 sdp: 两类接口 MAC 的原因。配置服务时先想清楚哪些 PE 是 LER，P 节点不需要任何 service 配置（Lab 中 sw9/sw10 的 mac-learning domain vpls 为空即证）。
  tags: [服务模型, LER, MAC学习, VPLS, PE职责]

- id: p15
  title: VPLS Split Horizon（水平分割）规则
  type: principle
  source_chapter: "p133"
  source_quote: |
    "To prevent forwarding loops, the so-called "Split Horizon" rule is used. In the VPLS context, this rule basically implies that a PE must never send a packet on a PW if that packet has been received from a PW. This ensures that traffic cannot form a loop over the backbone network using PWs. The fact that there is always a full mesh of PWs between the PE devices ensures that every destination within the VPLS will be reached by a broadcast packet."
  summary: |
    VPLS 骨干防环不靠 STP，靠规则：PE 从伪线（PW）收到的报文绝不再从任何伪线转发出去；配合 PE 间伪线全网状，广播报文总能到达 VPLS 内所有目的地。这是 VPLS 有别于普通以太网桥接的核心约束，也是全网状 PW（每对 PE 一条）成为 VPLS 硬性要求的原因。
  tags: [Split-Horizon, 防环, PW, 全网状, VPLS]

- id: p16
  title: vlan-xlation 使能层级与命令（先端口级、再服务级）
  type: principle
  source_chapter: "p79-80"
  source_quote: |
    "First at the access port level and then at the service level.
    To enable translation at the service level, use the service vlan-xlation command.
    To enable VLAN translation at the port level, use the service access vlan-xlation command.
    -> service 2 vlan-xlation enable
    -> service access port 1/1/3 vlan-xlation enable"
  summary: |
    VLAN 转换（Vlan Translation）在两层使能：端口级 service access port <port> vlan-xlation enable 与服务级 service <id> vlan-xlation enable，教材次序是先端口后服务。ITAG/OTAG 分别指内层/外层标签。Lab 2 中跨站点 VLAN 对不齐时就是靠补 vlan-xlation 恢复连通（p104-105）。注意 ce08：SAP 配成 untagged（:0）时出口永远 untagged。
  tags: [vlan-xlation, VLAN转换, ITAG, OTAG, 配置要点]

- id: p17
  title: BGP VPLS 邻居配置要点：同 AS 全互联 + update-source Loopback0 + activate l2vpn-vpls
  type: principle
  source_chapter: "p74, p110"
  source_quote: |
    "ip bgp autonomous-system 65724
    ip bgp address-family l2vpn-vpls
    ip bgp admin-state enable
    ip bgp neighbor 192.168.254.8 remote-as 65724
    ip bgp neighbor 192.168.254.8 update-source Loopback0
    ip bgp neighbor 192.168.254.8 admin-state enable
    ip bgp neighbor 192.168.254.8 activate l2vpn-vpls"
  summary: |
    BGP VPLS 的邻居模板五要素：双方同 AS 号（IBGP，Lab 用 65724，参考设计样例同）、邻居地址用对端 loopback、update-source 指向本端 Loopback0、每邻居单独 activate l2vpn-vpls 地址族、再 admin-state enable。全局侧还需 address-family l2vpn-vpls 与 admin-state enable。由于 AOS 不支持 RR（p132-133），每个 PE 都要与所有其他 PE 建邻居（全互联）。验证用 show ip bgp neighbors 看 established 与 Activate L2VPN vpls = enabled。
  tags: [BGP, l2vpn-vpls, update-source, IBGP, 全互联]

- id: p18
  title: MPLS/VPLS 验证命令族谱（Reference Design Guide 汇总）
  type: principle
  source_chapter: "p139-145"
  source_quote: |
    "# Displays the installed packages in the switch.
    -> show pkgmgr [mpls]
    # Displays the MPLS global attributes of a local router.
    -> show mpls
    # Use this command to display FTN (FEC-To-NHLF) table information.
    -> show mpls ftn-table
    # Use this command to view Incoming label mapping (ILM) table entries.
    -> show mpls ilm-table"
  summary: |
    按层次组织的排障命令全集：包/许可（show pkgmgr、show license-server usage/info、sh license-info）；MPLS 全局与接口（show mpls、show mpls interface）；标签表（show mpls ftn-table=入方向 PUSH 视角、ilm-table=入标签 SWAP/POP 视角、forwarding-table=综合视图、vpls-mesh=VC 连接状态）；LDP（show mpls ldp、ldp interface、ldp neighbor、ldp session [含 tx-labels/rx-labels]）；业务（show service [vpls]、show service sdp、show service bind-sdp）；BGP（show ip bgp、show ip bgp neighbors、show ip bgp l2vpn-vpls [path]，path 输出含 VE-ID/VBO/VBS/LabelBase）；MAC（show mac-learning domain vpls）。
  tags: [验证命令, 排障, show, FTN, ILM, 参考手册]
