# counter-examples · OmniSwitch LAN SPB Presales (DT00XPS279EN Issue 05)
# 来源: source/fulltext.md（页码即 <<<PAGE n>>> 标记）+ BOOK_OVERVIEW.md 批判章节
# 规则: 每条含页码、原文引用(<=100 词)、中文"踩坑场景/后果/规避"

```yaml
- id: ce01
  title: SAP 端口边缘特性受限
  type: counter-example
  source_chapter: "p83"
  source_quote: |
    "Endpoints connected through SPB SAP UNIs; SPB end-to-end; Hairpin only used for Routing;
    SAP Ports are locally limited in support of edge features such as port-QoS, LPS, DHCP Snooping, STP etc."
    (对照设计: "VLAN ports support all standard features — Preferred method for L3 VPN designs")
  summary: |
    踩坑场景：L3 VPN 设计时选"SAP UNI 端到端 SPB"方案（hairpin 只做路由），把终端直接接在 SAP 端口上，
    还期望普通接入口一样的边缘能力。限制清单（书原话）：SAP 端口本地仅有限支持 port-QoS、LPS（链路保护）、
    DHCP Snooping、STP 等边缘特性。后果：DHCP 防护、端口级 QoS、环路保护等接入侧功能缺位，常在部署后期才发现，
    被迫返工。规避：教材推荐 VLAN UNI 设计——路由先发生在 VLAN 域、SPB 只从 hairpin 起进骨干，
    "VLAN ports support all standard features"，且这是 L3 VPN 首选方法。
  tags: [limitation, sap, l3vpn, edge-features, port-qos, dhcp-snooping, design]

- id: ce02
  title: STP 失败模式（全书反面教材）
  type: counter-example
  source_chapter: "p23"
  source_quote: |
    "A single tree, the traffic always has to pass through the 'Root' bridge; F to G requires five hops
    and it is right next to G; Lots of blocked path, wasted bandwidth; Hop by hop configuration;
    Inefficient links utilization; No Shortest Path; Inefficient Broadcast; Low scalability; High convergence times"
  summary: |
    踩坑场景：继续在网状/冗余园区里跑生成树。失败模式清单：流量绕行根桥（相邻的 F 到 G 也要五跳）、
    大量链路被阻塞浪费带宽、逐跳手工配置、广播低效、扩展性差、收敛慢。后果：可用带宽被砍半、路径次优、
    扩容受阻、故障恢复以秒计。规避：换 SPB 对称同构最短路径树——每台交换机都是自己流量树的根、IS-IS 控制、
    无环、快速恢复；这也是全书"为什么卖 SPB"的开场弹药，可直接用于回应"为什么要换掉 STP"。
  tags: [failure-mode, stp, suboptimal-path, blocked-links, convergence]

- id: ce03
  title: 多路访问网段 DIS 无备份（单点风险 + 约 3 秒中断）
  type: counter-example
  source_chapter: "p38"
  source_quote: |
    "All shortest paths calculated travel through the DIS... No DIS backup; New DIS election
    without significant disruption (3s)"
  summary: |
    踩坑场景：用 Point-to-MultiPoint 邻接把 SPB 域扩展到共享二层网/微波 PMP/第三方运营商网络时，
    DIS（指定中间系统）承担伪节点、LSP 数据库同步与洪泛，且所有最短路径都经过它——但 DIS 没有备份机制。
    后果：DIS 故障触发重新选举，约 3 秒显著中断；DIS 本身是共享网段的逻辑单点，规模越大影响面越大。
    规避：共享网段尽量收窄；利用选举规则（最高接口优先级、平局比最高 BMAC）提前规划谁当 DIS 并加固该节点；
    对高可用敏感场景评估 3s 中断是否可接受，必要时改用 P2P 邻接设计。
  tags: [risk, dis, isis, p2mp, single-point-of-failure, convergence]

- id: ce04
  title: Head-End 复制的带宽放大与 IP 组播洪泛
  type: counter-example
  source_chapter: "p65-69"
  source_quote: |
    "Head-End: Sparse community of interest, Low Multicast bandwidth... One copy of each packet is sent
    to each BEB where the ISID exists (p66). Without IP Multicast snooping, floods IP multicast over the
    service; Flooding of ALL SAPs and SDP (p67). Tandem: More bandwidth-efficient (p69)"
  summary: |
    踩坑场景一：接收者众多或组播流量大的 I-SID 用 Head-End（AOS 原生默认模式）——入口 BEB 给每个远端 BEB
    各复制一份，骨干流量随节点数线性放大。Head-End 只适合"兴趣共同体稀疏、组播带宽低"的服务。
    踩坑场景二：没开 IP 组播优化，IP 组播会在服务内洪泛到所有 SAP 和所有 SDP 隧道。
    后果：视频监控/IPTV 类业务直接把骨干带宽打爆。规避：密集组播改用 Tandem (S,G)/*,G 复制
    （书评："More bandwidth-efficient"、"Less resource usage"）；同时开启服务级 IP multicast snooping，
    让数据只复制给有 IGMP 报告的客户端。
  tags: [pitfall, multicast, head-end-replication, tandem, bandwidth, snooping]

- id: ce05
  title: BVLAN 上限 16 个，推荐仅 4 个
  type: counter-example
  source_chapter: "p39, p75"
  source_quote: |
    "AOS support: 16 BVLANs (p39)... Maximum number of BVLANs: 16 (4 is recommended) (p75)"
  summary: |
    踩坑场景：方案里给每类业务/每条等价路径都规划独立 BVLAN，或照搬 ECT 16 算法想做满 16 路分担。
    限制：AOS 每网只支持 16 个 BVLAN，且官方推荐值只有 4 个。后果：超 16 个直接落不了地；
    即使 10 个左右能配，调优复杂度也远超收益（概述文档同样点名"16 BVLAN、ECT 调优复杂度被一笔带过"）。
    规避：路径分担压缩到 4 个左右 BVLAN（配合 ECT 算法 ID 选择），业务数量扩展全部走 I-SID
    （24 位、千万级空间），不要用 BVLAN 承载业务维度。
  tags: [limitation, bvlan, ect, scale, design]

- id: ce06
  title: SPB 规模上限 1000 节点，超大规模 DC 该用 EVPN
  type: counter-example
  source_chapter: "p22, p131, p138"
  source_quote: |
    "Scales to 1000 nodes (PBB Data Plane and IS-IS Control Plane) (p22)... Large-data center ->
    Scalability -> EVPN (p138)... SPB in campus networks, EVPN in data centers, and MPLS in
    metropolitan area networks (p131)"
  summary: |
    踩坑场景：拿 SPB 去应标超大规模数据中心或数千节点 fabric。边界：PBB 数据面 + IS-IS 控制面的设计规模是
    1000 节点（p22、p76 均重复此数）；书自己在用例矩阵里把"Large-data center（诉求 Scalability）"判给 EVPN。
    后果：超界投标被 scalability 一票否决，还给竞品留下攻击点。规避：园区/校园/物联/城域主推 SPB；
    大 DC 场景主动切 EVPN 叙事——同一 AOS 双支持，无厂商锁定，再用 p134 对比表
    （SPB 部署简单/培训低/协议开销低/排障快）守住 SPB 的主场。
  tags: [boundary, scale, datacenter, evpn, positioning]

- id: ce07
  title: L3 内联路由机型矩阵不齐，低端机只能 Outline（还要搭物理端口）
  type: counter-example
  source_chapter: "p82, p92, p95"
  source_quote: |
    "Outline Routing using external loopback cable: OS6900-X20/X72/T20/Q32, OS6860/E (p82)...
    Front-panel port inline routing: OS6900-V72, OS6900-C32 (p92)... SPB Service based inline routing:
    OS6860N, OS6870, OS6900-X/T24C2, X/T48C6, X48C4E, C32E, V48C8, OS9900 (p95)"
  summary: |
    踩坑场景：不看机型就承诺"免环回线的单遍内联路由（service-based inline）"或前面板口内联。
    限制：外部环回线 Outline 支持面最广；前面板口 inline 仅 OS6900-V72/C32；免物理环回、免专用端口的
    service-based inline 只有 p95 列出的型号。后果：低端/老机型被迫走 Outline——每个环回要占用物理端口，
    前面板口方式还"Bandwidth processing is taken from the front panel port"（消耗端口带宽处理能力）；
    中低端机型（如 6860N）的支持矩阵需查最新 AOS 规格书（概述文档批判点）。
    另注：p75 规格表"IP Over SPBM"行只标 IPv4（VPN-Lite 和 L3 VPN），正文 p93-94 有 IPv6 接口样例，
    IPv6 支持范围属"待确认"，引用前必须核对最新规格。规避：投标前逐型号对照 p82/92/95 与最新
    AOS Specifications Guide。
  tags: [limitation, model-matrix, l3vpn, outline-routing, inline-routing, port-consumption]

- id: ce08
  title: 每节点 IS-IS 邻接数与 I-SID/SAP 数量的机型上限
  type: counter-example
  source_chapter: "p75"
  source_quote: |
    "Maximum number of IS-IS adjacencies: 70 / 128... Maximum number of IS-IS interfaces: 70 / 128...
    Maximum number of I-SIDs: 2K / 8K / 1K... Max number of VLANs or SVLANs per ISID: 2K / 4K...
    Maximum number of SAPs: 2K / 8K... Please refer to latest « AOS Specifications Guide » for up-to-date figures"
  summary: |
    踩坑场景：全 mesh 核心或海量服务接入时只算带宽、不算控制面规格。限制：IS-IS 邻接数与接口数随机型
    70~128 不等（OS6860/6865 为 70 档，高端 128）；I-SID 数低端 2K、6900 高端 8K、OS9900 列仅 1K；
    每 I-SID 的 VLAN/SVLAN 数 2K~4K；SAP 数 2K~8K。后果：mesh 度超邻接上限会邻接建不满；
    服务数超 I-SID 上限在扩容阶段卡壳。规避：设计期把节点 mesh 度、每 BEB 承载的 I-SID/SAP 数
    与机型规格表逐项对齐；书中数字是快照，落地前按其免责声明查最新《AOS Specifications Guide》。
  tags: [limitation, isis, adjacency, isid, sap, scale, model-matrix]

- id: ce09
  title: 骨干内不能二次 QoS 分类，CoS 只在 SAP 入口定型
  type: counter-example
  source_chapter: "p64"
  source_quote: |
    "Traffic is classified at the SAP level... No further classification within the SPB backbone
    due to MAC-in-MAC encapsulation... Tagged traffic: CoS marking from incoming VLAN tag onto BVLAN tag.
    Untagged traffic: the port's default priority is used"
  summary: |
    踩坑场景：客户要求"核心里按应用重新打标/差异化调度"，或接入侧 802.1p 标记混乱就上 SPB。
    限制：Mac-in-Mac 封装后骨干内不再有任何进一步分类；优先级完全在 SAP 入口定型——trusted SAP
    沿用入站标签（未打标流量用端口默认优先级 PRI 0），untrusted SAP 由管理员指定固定值。
    后果：入口标记不规范 = 全网 QoS 失真，且事后在核心无法补救。规避：在 UNI/接入层统一 802.1p 规范；
    每个 SAP 明确 trusted/untrusted 与固定优先级；利用"未打标隧道化的 L2 控制 BPDUs 赋最高优先级"
    的既定规则保护控制流量。
  tags: [limitation, qos, cos, sap, mac-in-mac]

- id: ce10
  title: L2 控制协议在 SAP 端口默认 Drop，需 L2 Profile 显式改处置
  type: counter-example
  source_chapter: "p63"
  source_quote: |
    "L2 Protocol Default Treatment: STP Tunnel; 802.1X Drop; 802.1AB Drop; 802.3AD Peer; GVRP Tunnel;
    AMAP Drop; MVRP Tunnel... Drop: discards unconditionally the specified PDU"
  summary: |
    踩坑场景：把两台远端交换机经 SPB 透传互联，默认 802.1X、LLDP（802.1AB）、AMAP 等协议还能照常工作。
    限制：SAP 入端口的二层控制帧有默认处置表——STP/GVRP/MVRP 默认 Tunnel（封装穿越 SPB）、802.3AD 默认
    Peer（与对端交换机按协议交互）、802.1X/802.1AB/AMAP 默认 Drop（无条件丢弃）。后果：默认 Drop 的协议被
    静默吞包，表现为"链路通但认证/邻接建不起来"的疑难杂症，排障方向容易被带偏。规避：为每个 SAP 关联
    L2 Profile 按需改处置（Tunnel/Peer/Drop）；需要跨 SPB 传 STP 控制时，Metz 案例（p123）的做法是
    用一条点对点 SPB 服务专门承载。
  tags: [pitfall, l2-profile, control-frames, 802.1x, lldp, drop]

- id: ce11
  title: VPN-Lite 设计铁律：两 VRF 不得共享同一 I-SID，loopback VLAN 必须专用
  type: counter-example
  source_chapter: "p88"
  source_quote: |
    "Each VRF must have a single IP interface on the routing side of the loop back tied to a specific
    VLAN not used on other ports... In the VPN Lite version there can actually be multiple IP interfaces
    tied to different I-SID per VRF (but two VRF cannot share the same ISID)"
  summary: |
    踩坑场景：VPN-Lite/环回设计里为省 VLAN 或 I-SID 做复用。规则：每个 VRF 在环回路由侧只能有一个 IP 接口，
    绑定专用 VLAN（不得在其他端口使用）；一个 VRF 可有多个 IP 接口对应不同 I-SID，但两个 VRF 绝不能共享
    同一 I-SID；对端 SAP 必须用同一 VLAN 作标识绑定到正确的 I-SID。后果：VLAN/I-SID 复用导致路由串线、
    服务误映射，故障定位极难。规避：建立 VRF-VLAN-I-SID 三列对照表做配置前校验；冗余网关需求用 VRRP
    （hello 可穿越 PBB 网络）或一 VRF 多 I-SID 设计满足。
  tags: [pitfall, vpn-lite, vrf, isid, vlan, design-rule]

- id: ce12
  title: E-LINE 伪线固定 Head-End 组播模式、SAP 不学源 MAC
  type: counter-example
  source_chapter: "p53"
  source_quote: |
    "E-LINE connection between two local SAPs or between two SAPs across the SPB network...
    No source @mac learning on the SAP. Head-end multicast mode. No Flooding and replication"
  summary: |
    踩坑场景：把 E-LINE（点对点透明电路/伪线）当普通交换端口用，期望 MAC 学习与洪泛行为一致。
    限制：伪线 SAP 不做源 MAC 学习；BUM 处理固定为 Head-End 组播模式；无洪泛与复制机制，
    没有 Tandem 选项。后果：依赖源 MAC 学习的统计/定位手段在伪线上失效；对组播密集的两点互联，
    Head-End 放大效应无法用 Tandem 消解。规避：两点透传、CE 对接场景用 E-LINE；
    需要完整 L2 服务行为（多点、多租户、可选复制模式）的场景用 E-LAN 服务。
  tags: [limitation, e-line, pseudo-wire, head-end-replication, mac-learning]

- id: ce13
  title: 收敛 100ms 低于 MPLS 50ms，超低时延场景书自己推荐 IP-MPLS
  type: counter-example
  source_chapter: "p136, p138"
  source_quote: |
    "MPLS... Convergence: 50 ms... SPB... Convergence: 100 ms (p136)... Rail, E&U:
    Very low convergence-times -> IP-MPLS (p138)"
  summary: |
    踩坑场景：向轨交、电力（E&U）等对倒换时间毫秒必争的客户主打"SPB 快收敛"。
    边界：书内对比页明示 SPB 收敛 100ms、MPLS 50ms；用例矩阵把"Very low convergence-times"判给 IP-MPLS，
    MAN/Smart City 行还注明 tender 强制 IP-MPLS 时的让位条款。后果：在毫秒级保护刚需的标书里被技术参数
    直接否决。规避：话术定位为"sub-second/~100ms 恢复，对比 STP 秒级是代差提升"，主打园区/城域/物联网；
    轨交电力场景主动报 IP-MPLS 方案，避免拿 SPB 硬碰。
  tags: [boundary, convergence, mpls, rail, utility, positioning]

- id: ce14
  title: "SPB 替代 STP"不等于全网灭 STP，接入层仍要 STP/DHL
  type: counter-example
  source_chapter: "p32-33, p123"
  source_quote: |
    "Access Switch: 802.1Q VLAN on LAG; STP or DHL towards BEB (p32-33)... Loops without SPBs are
    controlled by unique and independent STP instances... A point-to-point SPB service is dedicated
    to transporting STP control (p123, Metz)"
  summary: |
    踩坑场景：售前话术过度承诺"上 SPB 后现网 STP 全部退役"。边界：教材自己的 2-tier/3-tier 参考设计里，
    非 SPB 的接入交换机上行到 BEB 仍用 STP 或 DHL 做冗余；Metz 迁移案例里 SPB 域外的环路由独立 STP 实例
    控制，相邻双环的 BEB 配 Root/Next Best Root 双 STP 实例，甚至专门开一条点对点 SPB 服务传输 STP 控制帧。
    后果：客户验收时发现现网仍有 STP 实例，质疑"替换 STP"承诺的兑现度。规避：话术精确化为
    "核心/骨干层消除 STP 阻塞链路、全链路利用"；接入与 legacy 域的环路防护（STP/DHL/LBD）如实保留并写进方案。
  tags: [boundary, stp, access-layer, dhl, migration, metz-case]

- id: ce15
  title: BVLAN 无生成树控制，防环依赖 RPFC + 显式启用 LBD
  type: counter-example
  source_chapter: "p35, p39, p71"
  source_quote: |
    "No spanning tree control... No source @mac learning of Customer (only BMAC)... No flooding of
    unknown destination or multicast frames (p39)... Loop-free via RPFC on source BMAC (p35)...
    Loopback Detection (LBD): No need of STP/RSTP/MSTP; Available on bridge or service access ports;
    Actions: Port shutdown, Trap, Event log, Port recovery (p71)"
  summary: |
    踩坑场景：把 BVLAN 当普通 VLAN，以为有 STP 兜底；或 BEB 接入侧没开 LBD（Loopback Detection）。
    限制：BVLAN 上没有生成树控制、不学客户源 MAC、不洪泛未知/组播帧——SPB 骨干防环完全靠对称同构最短路径
    与 RPFC（基于源 BMAC 的反向路径校验）；当遗留设备在 SPB 域外绕接出物理环（如两台 BEB 经接入侧串回）时，
    必须靠 LBD 兜底，而 LBD 是可选功能（p73 标注 optional），动作是把最高 PortID / 最高 BridgeID 一侧端口关断。
    后果：不开 LBD 时外部物理环路会把 BUM 流量放大成广播风暴。规避：在桥端口与业务接入端口（port/linkagg）
    按需启用 LBD，配自动恢复定时器与告警；混合组网迁移期把 LBD 列入标准开局清单。
  tags: [risk, loop, bvlan, rpfc, lbd, broadcast-storm]

- id: ce16
  title: 教材时代与数据快照局限（2025 Issue 05 / AOS R8）
  type: counter-example
  source_chapter: "p1, p74, p75, p139"
  source_quote: |
    "OMNISWITCH LAN R8 — OMNISWITCH LAN SPB PRESALES - ISSUE 05 (p1)... Please refer to latest
    « AOS Specifications Guide » for up-to-date figures (p75)... * Supported starting with 8.10 R3/R4;
    ** HW ready (p139)"
  summary: |
    踩坑场景：把书中规格数字与支持矩阵直接抄进 2026 年以后的标书或方案。局限：本书基于 2025-02 的 Issue 05
    （AOS R8 时代）；p75 规格表自带"以最新 AOS Specifications Guide 为准"的免责声明；p139 OmniFabric 支持
    矩阵多处标注"8.10 R3/R4 起才支持"或"HW ready（硬件就绪、软件未放行）"，且 P/O 图例书中未定义
    （推测 P=部分支持、O=支持，引用需核实）；成功案例均为早期欧洲/北美公共部门项目（概述文档批判点），
    缺超大规模 DC 佐证（该书也自认 DC 归 EVPN）；深度排障不在本书范围（p74 指引去售后课 DT00WTE323 等）。
    后果：拿旧数字应标，轻则参数过期重写、重则支持项翻车砸标。规避：所有机型/数量/版本相关数字在下单与
    投标前用最新 AOS 规格书复核；把本书定位为"叙事与架构弹药库"，规格一律以最新官方文档为准。
  tags: [meta, book-limitation, data-freshness, aos-r8, version-matrix]
```
