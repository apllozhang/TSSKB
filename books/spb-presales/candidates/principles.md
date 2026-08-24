# principles 候选条目 — OmniSwitch LAN SPB Presales (Issue 05)
# 来源: source/fulltext.md（页码即 <<<PAGE n>>> 标记）; 提取器: 原则提取器
# 规则: 原文引用 ≤100 英文词, 参数常数保留具体数字, 宁多勿漏

```yaml
- id: p01
  title: SPB 核心能力常数：1000 节点规模、突破 4096 VLAN 限制、亚秒收敛
  type: principle
  source_chapter: "p22"
  source_quote: |
    "Scales to 1000 nodes (PBB Data Plane and IS-IS Control Plane) ... Address isolation through mac-in-mac breaks the 4096 limit ... Service provisioning at the edge ... Customer MAC address learning restricted to the edge ... Fast recovery Sub-second Convergence ... No loops"
  summary: |
    SPB（IEEE 802.1aq）用 PBB 数据面 + IS-IS 控制面可扩展到 1000 台节点；
    通过 MAC-in-MAC 地址隔离打破传统 802.1Q 的 4096 个 VLAN 上限；
    客户 MAC 学习只发生在边缘，收敛为亚秒级且无环路。售前谈规模与收敛时可背诵的三个常数：1000 节点、突破 4096、亚秒级收敛。
  tags: [capacity, scalability, mac-in-mac, convergence, spb]

- id: p02
  title: SPB 功能免许可（No license），AOS 全系主流机型支持
  type: principle
  source_chapter: "p22"
  source_quote: |
    "• AOS support
    • OS6860E
    • OS6860N
    • OS6870
    • OS6865
    • OS6900
    • OS9900
    • No license"
  summary: |
    报价/选型规则：SPB 在 AOS 上不需要单独购买许可，支持机型覆盖
    OS6860E、OS6860N、OS6870、OS6865、OS6900、OS9900。
    售前可强调 SPB 特性零许可成本。
  tags: [licensing, pricing, positioning, aos]

- id: p03
  title: Edge-only 配置原则：只在边缘开通服务、核心零触碰、单协议 IS-IS
  type: principle
  source_chapter: "p12"
  source_quote: |
    "Automatic Edge Only ◼Edge-only provisioning ◼No-touch core ◼OmniVista NMS Single Protocol ◼No protocol "stack" ◼One protocol ◼L2 + L3 ◼IPv4 + IPv6 IS-IS"
  summary: |
    SPB 网络自动化三原则：业务只在边缘节点（BEB）开通，核心（BCB）零配置零触碰；
    只跑一个协议 IS-IS，同时承载 L2+L3、IPv4+IPv6，不需要协议栈堆叠。
    配合 OmniVista NMS 实现 auto backbone / auto services / auto attachment / self healing。
  tags: [design, automation, edge-only, isis, provisioning]

- id: p04
  title: 互操作与迁移原则：投资保护、分阶段迁移、无需推倒重来
  type: principle
  source_chapter: "p10"
  source_quote: |
    "L2 ◼802.1Q ◼Q-in-Q ◼LACP ... L3 ◼OSPF ◼IS-IS ◼BGP Multicast ◼PIM SM ◼PIM DM ◼PIM BIDIR ◼PIM SSM ✓Investment protection ✓Phased migration ✓No forklift upgrade"
  summary: |
    SPB 可与现网并存（L2 的 802.1Q/Q-in-Q/LACP，L3 的 OSPF/IS-IS/BGP，
    组播的 PIM 全系列），因此迁移策略是：投资保护、分阶段（phased）迁移、
    不需要 fork-lift（整机更换）式升级。SPB 域可与 Legacy 域并行运行（见 p13）。
  tags: [migration, interoperability, positioning, investment-protection]

- id: p05
  title: SPB 分层拓扑设计规则：三层（接入/BEB/BCB）与两层（BEB 全互联）
  type: principle
  source_chapter: "p32"
  source_quote: |
    "Access Switch • 802.1Q VLAN on LAG • STP or DHL towards BEB • Redundancy achieved through VC BEB and/or dual BEB nodes, LACP protocol / Aggregation Switch • Backbone edge bridge (BEB) role • VLAN to I-SID • IS-IS for MAC learning • IS-IS for SPB paths • PBB for data plane / Core Switch • Backbone Core Bridge (BCB) role • Learns BEB addresses"
  summary: |
    三层设计：接入交换机跑 802.1Q VLAN on LAG，用 STP 或 DHL 上联 BEB，靠 VC（虚拟机箱）
    BEB 或双 BEB + LACP 做冗余；汇聚交换机承担 BEB 角色（VLAN 到 I-SID 映射、IS-IS 学 MAC 和算路、PBB 数据面）；核心交换机承担 BCB 角色（只学 BEB 地址）。
    两层设计（p33）：无需 BCB 节点，核心即 BEB，BEB 之间部分或全互联，冗余靠 VC 拓扑中
    两台以上物理机箱实现。远程站点可通过 MPLS/VXLAN 域延伸 SPB。
  tags: [design, topology, beb, bcb, tier, redundancy]

- id: p06
  title: IS-IS SPB 默认控制 MAC 地址与邻接类型常数
  type: principle
  source_chapter: "p35"
  source_quote: |
    "IS-IS Hello packets Computation and auto-discovery AOS supported adjacencies ➢Point-to-Point ➢Point-to-MultiPoint Default Control MAC address: 01:80:c2:00:00:14 ... Nodes compute shortest path trees to all nodes based on Link metrics, without blocked links"
  summary: |
    可背诵常数：IS-IS SPB 的默认控制目的 MAC 地址为 01:80:c2:00:00:14。
    AOS 支持两种邻接类型：点对点（P2P）和点对多点（P2MP）。
    每台桥用唯一 BMAC 作为 SYS-ID 由 IS-IS 通告，各节点基于链路 metric 计算
    到所有节点的最短路径树，没有阻塞链路。
  tags: [isis, control-plane, mac-address, adjacency, constant]

- id: p07
  title: SPB 路径三特性：对称（Symmetric）、同路（Congruent）、RPFC 无环
  type: principle
  source_chapter: "p35"
  source_quote: |
    "Shortest paths exist now every node to every node:
    - Symmetric (same in both directions
    - Congruent (ucast/mcast) (unicast/multicast follow same route)
    - Loop-free via RPFC on source BMAC"
  summary: |
    SPB 最短路径的三条硬规则：1) 对称——去回两个方向走同一条路径；
    2) 同路（congruent）——单播和组播走同一条路由；
    3) 无环——通过 RPFC（基于源 BMAC 的反向路径检查）保证。
    这三条是 SPB 替代 STP 的理论根基，也是排障和讲解流量行为的基准。
  tags: [spf, symmetric, congruent, rpfc, loop-free]

- id: p08
  title: P2MP 共享网段 DIS 选举规则：最高接口优先级、平局取最高 BMAC、无备份、3 秒重选
  type: principle
  source_chapter: "p38"
  source_quote: |
    "No DIS backup ➢New DIS election without significant disruption (3s) ... DIS: Highest interface priority • Tiebreaker: highest @BMAC DIS Election"
  summary: |
    点对多点（多路访问共享网段）场景下 IS-IS SPB 选举 DIS（指定中间系统）：
    先比接口优先级最高者当选，平局时取 BMAC 最高者。
    DIS 负责伪节点 LSP 同步、洪泛和 SPT 计算，所有最短路径都经过 DIS。
    注意两点：没有备份 DIS；DIS 重选举仅需约 3 秒且无重大中断。
  tags: [isis, dis, p2mp, election, multicast-access]

- id: p09
  title: BVLAN 设计规则：无 STP、不学客户 MAC、不洪泛、每 BVLAN 独立 SPT、AOS 上限 16 个
  type: principle
  source_chapter: "p39"
  source_quote: |
    "Shortest path bridge VLAN No spanning tree control No source @mac learning of Customer (only BMAC) No flooding of unknown destination or multicast frames Each B-VLAN calculates its own Shortest Path Tree Control BVLAN carries IS-IS control packets AOS support: 16 BVLANs"
  summary: |
    骨干 VLAN（BVLAN）六条规则：1) 不跑生成树控制；2) 不学客户源 MAC，只处理 BMAC；
    3) 不洪泛未知目的地或组播帧；4) 每个 BVLAN 独立计算自己的最短路径树；
    5) Control BVLAN 专门承载 IS-IS 控制报文；6) AOS 最多支持 16 个 BVLAN
    （推荐规划 4 个，见 p75 规格表）。
  tags: [bvlan, capacity, control-plane, isis, design]

- id: p10
  title: Control BVLAN 可兼作带内管理网（BEB 与 BCB 均支持）
  type: principle
  source_chapter: "p40"
  source_quote: |
    "In-Band Management IP interface Supported on Control BVLAN BEBs as well as BCBs In-band management subnet routing Static or Dynamic routing Redistribute routes into ISIS-SPB"
  summary: |
    工程规则：带内管理 IP 接口只支持建在 Control BVLAN 上，BEB 和 BCB 都可以配置。
    管理子网可跑静态或动态路由，并可将路由重分发进 ISIS-SPB，
    使 OmniVista 等 NMS 可通过 IP 网络（如 OSPF 域）到达 SPB 网元。
  tags: [management, control-bvlan, in-band, routing]

- id: p11
  title: 最多 16 条等价最短路径，由头端（Head-end）分配流量
  type: principle
  source_chapter: "p41"
  source_quote: |
    "Multi-path loop-free shortest path routing ➢Up to 16 paths (Equal cost Tree Algorithms) ➢Head-end assignment of traffic to any of those 16 shortest paths ➢Excellent use of mesh connectivity Unicast/Multicast symmetry ➢Same in both directions Congruency ➢Unicast/Multicast follow the same route"
  summary: |
    容量常数与负载分担原则：SPB 支持最多 16 条等价无环最短路径（ECT 算法），
    流量由入侧头端（ingress/head-end）节点分配到这 16 条路径中的任意一条，
    充分利用网状连接；同时保持单组播对称与同路。
  tags: [ect, multipath, load-balancing, capacity]

- id: p12
  title: ECT 算法规则：16 个预定义算法（索引 1-16）、单组播同算法、新建 BVLAN 自动分配 ECT ID
  type: principle
  source_chapter: "p42"
  source_quote: |
    "All bridges use predefined ECT algorithms to calculate layer 2 congruency and symmetry for switching • Standard provides 16 predefined algorithms • 16 ECT -> index 1-16 • Same algorithm is used both for unicast and multicast • Byte-by-byte XOR ECT-MASK (16 masks to provide 16 ECT) for all nodes excluding source and destination • Next available ECT-algorithm ID is assigned to a BVLAN when the BVLAN is created (can be modified)"
  summary: |
    选路判定顺序：先比链路 metric（越小越优）、再比跳数（最少优先）；
    仍相等时全网交换机用预定义 ECT 算法打破平局。标准提供 16 个预定义算法，索引 1-16，
    对应 16 个 ECT-MASK（ECT-1=0x00 选最低 BridgeID、ECT-2=0xFF 选最高 BridgeID 等）。
    同一算法同时用于单播和组播。新建 BVLAN 时自动分配下一个可用 ECT 算法 ID（可手工修改）。
    BridgeID = 2 字节可配置优先级 || 6 字节系统 BMAC。
  tags: [ect, tie-break, bvlan, spf, metric]

- id: p13
  title: ECT 计算方法：ECT-MASK 与 BridgeID 逐字节异或，取最低路径 ID 获胜
  type: principle
  source_chapter: "p43"
  source_quote: |
    "1 Byte-by-byte XOR (ECT-MASK, BridgeID) For all nodes along the path (excluding source and destination) 2 Pick up the ECT with the lowest path identifier (i.e path with lowest Bridge ID) ... A failure in link 1to4 would remove ECT-1 and ECT-3 from the list and ECT-2 would win"
  summary: |
    ECT 打破平局的两步计算：1) 对路径上所有中间节点（不含源和目的）的 BridgeID
    与 ECT-MASK 逐字节异或；2) 选异或后路径标识（等效 BridgeID）最低的那条 ECT 路径，
    该路径同时用于单播和组播。链路故障时被依赖的 ECT 从列表剔除，剩余最低者接管
    （例：链路 1-4 故障会移除 ECT-1 和 ECT-3，ECT-2 胜出）。
  tags: [ect, xor, path-selection, failure, algorithm]

- id: p14
  title: 802.1ah PBB 封装头部字段常数（Ethertype、I-SID、B-VID、PCP）
  type: principle
  source_chapter: "p47"
  source_quote: |
    "B-TAG Ether-type 2 bytes 0x88a8 B-VID 12 bits Tunnel VID (802.1Q compliant). B-TAG PCP 3 bits Tunnel Priority Code Point (0-7) I-SID 24 bits Service identifier (1 – 16 million) I-TAG Ether-type 2 bytes 0x88e7 I-TAG PCP 3 bits Service Priority Code Point (0-7)"
  summary: |
    可背诵的封装常数：B-TAG Ethertype = 0x88a8，I-TAG Ethertype = 0x88e7；
    B-VID 12 比特；I-SID 24 比特（取值 1-1600 万）；B-TAG/I-TAG 的 PCP 均为 3 比特
    （0-7），DEI 1 比特。Backbone-DA 必须是单播地址（组播场景用特殊组 BMAC），
    Backbone-SA 标识本节点。
  tags: [pbb, encapsulation, ethertype, isid, constant]

- id: p15
  title: 伪线服务（E-LINE / 点对点透明电路）四条特性
  type: principle
  source_chapter: "p53"
  source_quote: |
    "• E-LINE connection between two local SAPs or between two SAPs across the SPB network. • Also known as SPB Point-to-Point Transparent Circuit • Transparent packets forwarding ... • No source @mac learning on the SAP • Head-end multicast mode • No Flooding and replication"
  summary: |
    SPB 伪线规则：提供两个 SAP 之间（本地或跨 SPB 网络）的 E-LINE 连接，
    也叫点对点透明电路；报文透明转发；SAP 上不学源 MAC；
    组播采用头端复制模式；不洪泛、不复制。适合点对点透明管道类业务。
  tags: [pseudo-wire, e-line, sap, transparency]

- id: p16
  title: SAP 只能在 access 接口上创建（物理口或 LAG）
  type: principle
  source_chapter: "p54"
  source_quote: |
    "• Physical Ethernet port or LAG
    - Configured as an access port
    - Encapsulation identifier (ID), such as VLAN ID, Q-tag.
    - SAPs can only be created on access interfaces
    • Static or Dynamic SAPs"
  summary: |
    硬性配置规则：SAP（业务接入点）只能创建在配置为 access 角色的接口上，
    载体可以是物理以太网口或 LAG；每个 SAP 用封装标识（如 VLAN ID、Q-tag）区分。
    SAP 分静态和动态两类。这是 SPB 业务配置的第一条约束。
  tags: [sap, access-port, config, uni]

- id: p17
  title: 静态 SAP 封装组合规则：同一 access 口可混用 Untagged/Tagged/QinQ
  type: principle
  source_chapter: "p55"
  source_quote: |
    "Different encapsulation types on the same access port • Untagged, Tagged, QinQ • Multiple services for one CVLAN or one service for multiple CVLANs"
  summary: |
    同一个 access 端口上可以配置不同封装类型的 SAP：Untagged、Tagged（单层 VLAN）、
    QinQ（双层标签）。映射关系灵活：一个 CVLAN 可对应多个业务，
    多个 CVLAN 也可合并进一个业务（示例中 VLAN 10/20/30/31/32 分别进 Service 1000/2000/3000）。
  tags: [sap, encapsulation, qinq, vlan-mapping]

- id: p18
  title: 动态 SAP 由 UNP 业务 profile 自动创建
  type: principle
  source_chapter: "p56"
  source_quote: |
    "Dynamic SAPs supported from UNP service profiles Device assignment to an SPB service profile Automatic SAP creation ... MAC auth? 802.1x auth? Classification Rules?"
  summary: |
    自动化规则：动态 SAP 从 UNP（User Network Profile）业务 profile 派生，
    设备通过 MAC 认证（非 supplicant）或 802.1x 认证（supplicant）及分类规则
    被指派到 SPB 业务 profile 后，SAP 自动创建。profile 内含 VLAN Tag→I-SID→BVLAN
    映射、组播模式、VLAN 转换、策略表（ACL/QoS）（见 p58-62 静态/动态/持久 SAP 叠加）。
  tags: [sap, unp, dynamic, automation, authentication]

- id: p19
  title: L2 控制协议在 SAP 口的默认处理表（STP 隧道、802.1X 丢弃、LACP 对等）
  type: principle
  source_chapter: "p63"
  source_quote: |
    "L2 Protocol Default Treatment STP Tunnel 802.1X Drop 802.1AB Drop 802.3AD Peer GVRP Tunnel AMAP Drop MVRP Tunnel"
  summary: |
    可背诵默认表：STP→Tunnel，802.1X→Drop，802.1AB（LLDP）→Drop，
    802.3AD（LACP）→Peer，GVRP→Tunnel，AMAP→Drop，MVRP→Tunnel。
    三种动作定义：Peer=与对端交换机按协议交互；Drop=无条件丢弃该 PDU；
    Tunnel=控制报文封装后穿越 SPB 网络透明传输。L2 profile 可逐 SAP 口调整。
  tags: [l2-profile, control-frames, stp, tunnel, drop, peer]

- id: p20
  title: SAP QoS 规则：分类只在 SAP 入口做一次，骨干内不再分类
  type: principle
  source_chapter: "p64"
  source_quote: |
    "Traffic is classified at the SAP level Highest priority assigned to untagged tunneled L2 Control BPDUs No further classification within the SPB backbone due to MAC-in-MAC encapsulation Default classification 802.1p Tagged traffic: CoS marking from incoming VLAN tag onto BVLAN tag Untagged traffic: the port's default priority is used"
  summary: |
    QoS 原则：1) 流量只在 SAP 入口分类，进入骨干后因 MAC-in-MAC 封装不再重新分类；
    2) 未打标签的隧道化 L2 控制 BPDU 自动获得最高优先级；
    3) 默认按 802.1p 分类：有标签流量把入 VLAN 标签的 CoS 拷贝到 BVLAN 标签，
    无标签流量用端口默认优先级（PRI 0）；4) SAP 分 Trusted（信任标签）/Untrusted
    （管理员强制指定优先级）两种；封装范围 Tagged/QinQ 均为 VLAN 1-4094。
  tags: [qos, cos, sap, classification, trust]

- id: p21
  title: BUM 流量两种复制模式：Head-End（原生）与 Tandem（优化）
  type: principle
  source_chapter: "p65"
  source_quote: |
    "BUM = Broadcast Unknown Multicast • ARPs packets, Boot-p/DHCP requests, etc. SPB supports two BUM traffic distribution methods for replicating and forwarding multicast frames • Head-End (native mode) • Tandem (optimized)"
  summary: |
    SPB 对 BUM（广播/未知单播/组播，如 ARP、DHCP）只有两种复制转发模式：
    Head-End（头端复制，原生模式）和 Tandem（串联复制，优化模式）。
    选型依据（p66）：兴趣社群稀疏、组播带宽低的场景用 Head-End——
    入口 BEB 对每个存在该 I-SID 的远端 BEB 各复制一份，用目的 BEB 的 BMAC 封装，
    组播走单播树、共用同一 FDB；配合 IP 组播优化（service 级 IGMP snooping）
    可只复制给有 IGMP 客户端的 SAP/SDP，避免洪泛。
  tags: [bum, multicast, head-end, replication, igmp-snooping]

- id: p22
  title: Tandem 复制的两种树：(S,G) 每 I-SID 源树省带宽，(*,G) 每 BVLAN 共享树省资源
  type: principle
  source_chapter: "p69"
  source_quote: |
    "For every ISID, each bridge builds a source specific multicast trees (S,G) ➢Using special destination Multicast Group B-MAC ➢Replicate and forward the BUM traffic ➢Every node is the root of the tree and computes Multicast Tree per service ➢More bandwidth-efficient"
  summary: |
    Tandem 模式分两种：1) (S,G) 源特定树——每个 I-SID、每个源建一棵树，
    使用特殊组播组 B-MAC（如 03:00:11:00:01:90），中间节点只装组 BMAC 表项，
    带宽效率更高；2) (*,G) 共享树（p70）——每个 BVLAN 建一棵共享组播树，
    以 BridgeID 最低的节点作根，资源占用更少。按带宽 vs 表项资源取舍。
  tags: [tandem, multicast, s-g, shared-tree, bvlan]

- id: p23
  title: 环路检测（LBD）规则：无需 STP，关最高 PortID / 最高 BridgeID 侧端口
  type: principle
  source_chapter: "p71"
  source_quote: |
    "Automatically Loop detection ➢No need of STP/RSTP/MSTP ➢Periodically sends out frames from all loopback detection enabled ports ... Actions ➢Port shutdown ➢Trap ➢Event log ➢Port recovery • Automatic after a configurable timer or manually ... Port with highest PortID is shut down / Port in switch with highest BridgeID is shut down"
  summary: |
    LBD 规则：自动环路检测，替代 STP/RSTP/MSTP；周期性从所有使能端口发探测帧，
    可配在桥或业务 access 口（物理口/linkagg）。检测到环后的判定：
    同一交换机上关 PortID 最高的端口；跨交换机时关 BridgeID 最高交换机上的端口。
    动作四选：关端口、发 Trap、记事件日志、端口恢复（定时器自动或手工）。
  tags: [lbd, loop-detection, stp-replacement, resiliency]

- id: p24
  title: AOS SPB 容量规格表：BVLAN 16（推荐 4）、IS-IS 邻接 70/128、I-SID 2K-8K、SAP 2K-8K
  type: principle
  source_chapter: "p75"
  source_quote: |
    "Maximum number of BVLANs 16 (4 is recommended) ... Number of ECT algorithm IDs supported 16 (Can select any ID between 1 and 16 to assign to a BVLAN) Maximum number of I-SIDs 2K 2K 2K 8K 8K X/T24C2 : 2K 1K ... Maximum number of SAPs 2K 2K 2K 8K 8K 8K Please refer to latest « AOS Specifications Guide » for up-to-date figures"
  summary: |
    按机型的容量常数（OS6860/6860N/6865、OS6900 V72/C32、OS6900 X/T 系列、OS9900）：
    BVLAN 最多 16 个，推荐规划 4 个；IS-IS 邻接数与接口数：小机型 70，其余 128；
    ECT 算法 ID 支持 16 个（可在 1-16 中任选分配给 BVLAN）；I-SID 上限：
    OS6860/6860N/6865 为 2K，OS6900 多数 8K，X/T24C2 为 2K，OS9900 为 1K；
    每 I-SID 的 VLAN/SVLAN 数 2K-4K；SAP 上限 2K（小机型）至 8K。
    报价前应以最新《AOS Specifications Guide》为准。
  tags: [capacity, specifications, bvlan, isid, sap, isis, sizing]

- id: p25
  title: SPB 快速重收敛约 100ms（Key Takeaway 常数）
  type: principle
  source_chapter: "p76"
  source_quote: |
    "• Natively protect failures and reroute ... • Fast reconvergence (~100ms) ... • Scalability (up to 1000 nodes) ... • Runs over other technologies • L2 Services (VPLS, Microwave links, etc,). • L3 Services (IPVPN, Internet) • Using VxLAN to transport SPB-ISIS Interfaces (NNI) between SPB nodes."
  summary: |
    全书要点页给出的可背诵常数：SPB 故障快速重收敛约 100ms，规模可达 1000 节点。
    同时 SPB 可跑在其他技术之上（L2 的 VPLS/微波链路，L3 的 IPVPN/Internet，
    以及用 VxLAN 承载 SPB 节点间 NNI 的 IS-IS 接口）——跨域组网时的关键卖点。
  tags: [convergence, capacity, constant, key-takeaway, transport]

- id: p26
  title: Outline 路由（物理环回线）构成规则与支持机型
  type: principle
  source_chapter: "p82"
  source_quote: |
    "Use of two physical loopback ports. • One side of as an access port for SPB. • Other side is a bridged port configured for routing only. Static linkagg port or a physical port. Multiple ports can be shared among different VRFs. AOS support ●L3 VPN routing over SPB ●VPN Lite over SPB ... OS6900-X20 OS6900-X72 OS6900-T20 OS6900-Q32 OS6860/E"
  summary: |
    Outline routing（外接环回线法）规则：使用两个物理环回口，
    一侧配成 SPB access 口（L3 VPN Access Port），另一侧配成纯路由桥接口
    （L3 VPN Router Port）；载体为静态链路聚合或物理口，多对环回口可在不同 VRF 间共享。
    支持 L3 VPN 与 VPN Lite 两种机制。支持机型：OS6900-X20/X72/T20/Q32、OS6860/E。
  tags: [l3vpn, vpn-lite, outline-routing, loopback, model-support]

- id: p27
  title: 环回口设计取舍：VLAN UNI 是 L3 VPN 首选方法，SAP 口边缘特性受限
  type: principle
  source_chapter: "p83"
  source_quote: |
    "Endpoints connected through VLAN UNIs Routing actually happens in the VLAN domain before SPB ... VLAN ports support all standard features Preferred method for L3 VPN designs ... Endpoints connected through connected through SPB SAP UNIs SPB end-to-end Hairpin only used for Routing SAP Ports are locally limited in support of edge features such as port-QoS, LPS, DHCP Snooping, STP etc."
  summary: |
    设计规则：环回口方案有两种终结方式。1) 终结在 VLAN UNI：路由发生在进 SPB 之前的
    VLAN 域，VLAN 端口支持全部标准边缘特性（port-QoS、LPS、DHCP Snooping、STP 等），
    是 L3 VPN 设计的首选方法；2) 终结在 SPB SAP UNI：SPB 端到端、发夹仅用于路由，
    但 SAP 口对边缘特性支持有限（port-QoS、LPS、DHCP Snooping、STP 等受限）。
  tags: [l3vpn, design, vlan-uni, sap, edge-features]

- id: p28
  title: VPN-Lite 配置六条守则（每 VRF 单 IP 接口、两 VRF 不得共享同一 I-SID）
  type: principle
  source_chapter: "p88"
  source_quote: |
    "• Each VRF must have a single IP interface on the routing side of the loop back tied to a specific VLAN not used on other ports. • In the VPN Lite version there can actually be multiple IP interfaces tied to different I-SID per VRF (but two VRF cannot share the same ISID). • There is a corresponding SAP on the other side of the loopback tied to the correct I-SID using the same VLAN as its identifier. • VRRP can also be configured per interface on the loopback to allow two or more BEB to act as redundant routers"
  summary: |
    VPN-Lite 配置清单：1) 每个 VRF 在环回口路由侧只能有一个 IP 接口，
    绑定一个其他端口不用的专用 VLAN；2) 一个 VRF 可以有多个 IP 接口对应不同 I-SID，
    但两个 VRF 不能共享同一个 I-SID；3) 环回另一侧的 SAP 用同一 VLAN 号做标识
    绑到正确 I-SID；4) 路由侧既可跑路由协议也可直接接主机网段；
    5) 可在环回口按接口配 VRRP，让两台以上 BEB 做冗余路由器（VRRP hello 穿越 PBB 网络传送）；
    6) 也可不用动态路由，静态路由把网关指向经 SPB 连接的对端 BEB 环回 IP 接口。
  tags: [vpn-lite, config, vrf, isid, vrrp, checklist]

- id: p29
  title: 前面板口 Inline 路由：免物理环回线，仅 OS6900-V72/C32 支持
  type: principle
  source_chapter: "p92"
  source_quote: |
    "No physical loopback cable required Front panel port or link aggregate configured to run in loopback mode VPN interface defined through specific front panel port(s) Bandwidth processing is taken from the front panel port AOS support ... OS6900-V72 OS6900-C32"
  summary: |
    Front-panel inline routing 规则：不需要物理环回线缆，把前面板口或静态链路聚合
    配成 loopback 模式即可；VPN 接口通过指定前面板口定义，
    带宽处理能力取自该前面板口。机型限制严格：仅 OS6900-V72 和 OS6900-C32 支持，
    选型时注意端口与带宽消耗。
  tags: [inline-routing, front-panel, loopback, model-support, l3vpn]

- id: p30
  title: 基于业务的 Inline 路由：免环回线免专用口，IPv4/IPv6 同业务须同 VRF
  type: principle
  source_chapter: "p95"
  source_quote: |
    "No physical loopback cable required No dedicated front-panel ports IP service-based interface configured through software for single-pass in-line routing L3 VPN interface defined through the configuration of an IP interface bound to an SPB service Both an IPv4 and IPv6 interface can be assigned to the same SPB service as long as both interface types are in the same VRF instance."
  summary: |
    Service-based inline routing（单遍内联路由）规则：既不要物理环回线也不要专用前面板口，
    IP 接口直接绑定到 SPB 业务上由软件实现。硬性约束：IPv4 和 IPv6 接口可绑同一个
    SPB 业务，前提是两类接口属于同一 VRF 实例。支持机型最广：
    OS6860N、OS6870、OS6900-X/T24C2、X/T48C6、X48C4E、C32E、V48C8、OS9900。
  tags: [inline-routing, service-based, ipv6, vrf, model-support]

- id: p31
  title: OV2500 服务参数默认值：VPN MTU 默认 1500 字节
  type: principle
  source_chapter: "p102"
  source_quote: |
    "VPN MTU - Set the VPN MTU. The largest frame size, in octets, that the Service can handle. (Default = 1,500)"
  summary: |
    OmniVista 2500 上创建/监控 SPB 业务时的可背常数：VPN MTU（业务能处理的最大帧长，
    单位字节）默认 1500。业务参数还包括 Mcast Mode（Headend/Tandem）、
    VLAN Translation（是/否）、Remove Ingress（是/否）等（p102/p106 监控页同名字段）。
  tags: [ov2500, mtu, default, provisioning]

- id: p32
  title: OV2500 SPB Profile 中 I-SID 有效范围 256-16777214，无标签流量 SAP 封装值为 0
  type: principle
  source_chapter: "p109"
  source_quote: |
    "Tag Value - The VLAN tag information from classified traffic used to create the Service Access Point (SAP) for the traffic. If the traffic is untagged, the SAP is created with 0 as the encapsulation value (for example, 1/12:0). ISID - A service instance identifier (ISID) that is used to identify an SPB service in a provider backbone bridge (PBB) network. The valid range is 256 - 16777214."
  summary: |
    OV2500 SPB Profile（Unified Access > Unified Profile > Template > SPB Profile）参数规则：
    I-SID 有效范围 256 - 16777214（避开 0-255 保留段）；Tag Value 取分类流量的 VLAN 标签
    用于创建 SAP，无标签流量则以 0 作为封装值创建 SAP（如 1/12:0）；
    BVLAN 必须填已存在的 SPB 骨干 VLAN；组播模式下拉选 Headend 或 Tandem。
  tags: [ov2500, isid, range, sap, provisioning, untagged]

- id: p33
  title: SPB / EVPN / MPLS 定位对比：SPB 部署最简、开销最低、排障最快
  type: principle
  source_chapter: "p134"
  source_quote: |
    "Main use case Datacenter, Campus, IoT Networks / Datacenter / Service Provider & Mission critical networks ... Ease of deployment Simple to Moderate / Moderate to complex / Moderate to complex Training needed Low to Moderate / Moderate to High / High Protocol Overhead Low IS-IS only / Moderate BGP & VXLAN/ MPLS / High LDP, RSVP, BGP Troubleshooting Simple & Fast / Intermediate time / Complex & Slow"
  summary: |
    三技术选型对比表（顺序 SPB / EVPN / MPLS）：主用场景——数据中心+园区+IoT /
    数据中心 / 运营商与任务关键网；扩展性 Large / Large-Very large / Large-Very large；
    弹性 High / High / Very High；部署难度 简单到中等 / 中等到复杂 / 中等到复杂；
    培训需求 低到中 / 中到高 / 高；协议开销 低（仅 IS-IS）/ 中（BGP+VXLAN/MPLS）/
    高（LDP、RSVP、BGP）；排障 简单快速 / 中等 / 复杂缓慢。
    售前话术：SPB 胜在简、轻、快。
  tags: [positioning, spb, evpn, mpls, comparison, presales]

- id: p34
  title: 收敛与成本常数：MPLS 50ms/$$$ vs SPB 100ms/$$（均覆盖核心骨干）
  type: principle
  source_chapter: "p136"
  source_quote: |
    "MPLS Highly scalable Core, backbone Convergence: 50 ms Complex Cost: $$$ SPB Scalable Access, core, backbone Convergence: 100 ms Cost: $$"
  summary: |
    售前可背常数：MPLS 收敛 50ms、复杂度高、成本 $$$；
    SPB 收敛 100ms、成本 $$，且覆盖位置从接入到核心骨干（MPLS 一般不下接入）。
    论极端收敛 MPLS 占优，论性价比与全位置覆盖 SPB 占优。
  tags: [positioning, convergence, cost, mpls, spb, constant]

- id: p35
  title: 行业用例选型规则：园区/视频/ITS 用 SPB，大 DC 用 EVPN，铁路等极端收敛用 IP-MPLS
  type: principle
  source_chapter: "p138"
  source_quote: |
    "Video Surveillance Scale < 1,000 Virtual-chassis ... SPB – simplicity ... Campus Network ... SPB - simplicity ITS Network ... SPB – simplicity, ruggedized equipment Large-data center Scalability EVPN Rail, E&U Very low convergence-times IP-MPLS MANs/Smart City Scalability Traffic Control SPB/IP-MPLS* * When IP-MPLS is mandatory in the tender"
  summary: |
    用例选型速查：视频监控、赌场（视频+运营）、园区网——规模小于 1000 节点、
    人手少、组播多——选 SPB（简单性）；ITS（智能交通）网——户外部署——选 SPB
    （简单+加固设备）；大型数据中心——扩展性诉求——选 EVPN；铁路、电力等
    要求极低收敛时间——选 IP-MPLS；城域网/智慧城市——SPB 或 IP-MPLS，
    仅当招标书强制要求 IP-MPLS 时才上 IP-MPLS。
  tags: [positioning, use-cases, vertical, selection, tender]

- id: p36
  title: Metz 案例：SPB 与多环共存的工程经验（双 STP 实例 + 专线传 STP 控制 + 多 BVLAN 活路）
  type: principle
  source_chapter: "p123"
  source_quote: |
    "SPB uses an SPF algorithm to find the best path between two nodes. Several BVLANs will be included to allow several active paths to be maintained. ... Loops without SPBs are controlled by unique and independent STP instances BEBs adjoining two loops are configured with two STP instances in Root Bridge and Next Best Root. A point-to-point SPB service is dedicated to transporting STP control."
  summary: |
    工程经验法则（Metz Eurometropolis，200 台交换机/100km 光纤/80 栋楼）：
    1) 部署多个 BVLAN 以同时保持多条活路径、全链路利用；
    2) 未迁移到 SPB 的接入环用各自独立 STP 实例控环；
    3) 毗邻两个环的 BEB 配两个 STP 实例，分别做 Root Bridge 和 Next Best Root；
    4) 用一条点对点 SPB 专线专门传送 STP 控制报文；
    5) 核心全网 SPB 化后该部分不再有二层环。整体迁移期间业务零中断。
  tags: [case-study, migration, stp, bvlan, engineering-practice]
```
