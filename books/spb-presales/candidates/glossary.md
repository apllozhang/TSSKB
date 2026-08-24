# GLOSSARY · OmniSwitch LAN SPB Presales (DT00XPS279EN Issue 05)
# 提取自全书（重点 p24 官方缩写表），40 条，按字母序排列。
# 注：任务清单中的 ERP（Ethernet Ring Protection）全书未出现，未收录。

- id: g01
  term: AOS
  full: Alcatel-Lucent OmniSwitch Operating System
  source_chapter: "p6, p22, p133"
  definition: |
    ALE OmniSwitch 全系列交换机统一的网络操作系统，SPB、EVPN、MPLS 三种织物技术都跑在同一个 AOS 上。
    书中反复强调 SPB 在 AOS 上免许可（no license）、全产品线支持（OS6860E 到 OS9900）。
    售前用法：客户担心厂商锁定时，用"同一 OS 三种技术、按区域任选"化解，这是 OmniFabric 章技术中立防御的根基。

- id: g02
  term: B-MAC
  full: Backbone MAC Address
  source_chapter: "p24, p26, p35"
  definition: |
    骨干网里每台 SPB 交换机的唯一 MAC 地址，与提供者实例端口（PIP）关联，用于构造穿越骨干的封装帧外层 MAC 头；IS-IS 把它当 SYS-ID 广告出去。
    核心交换机（BCB）只认 B-MAC 转发，客户 MAC 永远不进骨干。
    售前用法：这是"地址隔离、核心 FDB 极小"卖点的机制根基，也是 4096 VLAN 上限被打破的原因。

- id: g03
  term: B-TAG / I-TAG
  full: Backbone TAG / Service Instance TAG (IEEE 802.1ah)
  source_chapter: "p47, p48"
  definition: |
    802.1ah 封装的两个标签：外层 B-TAG（EtherType 0x88a8）承载 12 位 B-VID 和骨干优先级，决定帧走哪条路；内层 I-TAG（EtherType 0x88e7）承载 24 位 I-SID 和服务优先级，决定帧属于哪个服务。
    客户原始帧（含 C-TAG）被完整封装在里层，对骨干透明。
    售前用法：讲清"外层选路、内层选服务"的二级结构，就解释了一张骨干同时承载上千个隔离服务的原理。

- id: g04
  term: B-VID
  full: Backbone VLAN ID
  source_chapter: "p24, p42-43"
  definition: |
    PBB 封装头里的 12 位骨干 VLAN 标识字段，格式与 802.1ad 的 S-TAG 相同。
    每个 B-VID 对应一棵独立计算的最短路径树，同一路径上多个 B-VID 可走不同 ECT 树实现流量分担。
    售前用法：Metz 案例（p123）正是用多个 BVLAN 让多条路径同时活跃，把"全链路利用"从口号落到设计。

- id: g05
  term: BCB
  full: Backbone Core Bridge
  source_chapter: "p24, p27"
  definition: |
    SPB 骨干的核心桥，只按外层 B-MAC/B-VID 做转发，对 I-SID 和服务完全无感知。
    不学客户 MAC、不做服务配置，扩容加节点时核心近乎零改动（no-touch core）。
    售前用法："核心零触碰"是运维降本论证的核心证据——网络长大，配置工作量只随边缘线性增长。

- id: g06
  term: BEB
  full: Backbone Edge Bridge
  source_chapter: "p24, p26, p80-81"
  definition: |
    SPB 网络的边缘桥：负责 802.1ah 封装/解封装、客户 MAC 学习、SAP 与服务（I-SID）配置，是服务终结点。
    L3 服务（VPN-Lite、L3 VPN）的路由也跑在 BEB 上，一台设备同时当桥和路由器。
    售前用法：整网只有 BEB 需要配置服务，"edge-only provisioning" 卖点的载体；机型选型时 BEB 的 SAP/I-SID 规格是关键参数。

- id: g07
  term: BVLAN
  full: Backbone VLAN (B-VLAN)
  source_chapter: "p24, p28, p39-40"
  definition: |
    服务商分配用于在 SPB 骨干上传输客户流量的特殊 VLAN：无生成树控制、不学客户源 MAC、不泛洪未知目的地，每个 BVLAN 独立算最短路径树。
    其中控制 BVLAN 专门承载 IS-IS 控制报文，还可挂带内管理 IP 接口（静态或动态路由）。
    AOS 支持最多 16 个 BVLAN，书中建议 4 个（p75）。售前用法：BVLAN 规划是网络设计第一步；"控制 BVLAN 白送带内管理通道"是免费的加分项。

- id: g08
  term: CVLAN
  full: Customer VLAN
  source_chapter: "p31, p55"
  definition: |
    客户侧传统 802.1Q VLAN，在接入交换机上照常带 MAC 学习和泛洪，用户设备接在这里。
    进入 SPB 时由 SAP 按 VLAN 标签映射到 I-SID，多个 CVLAN 可并入同一服务，同一 CVLAN 在不同端口也可翻译成不同编号。
    售前用法：向客户保证"接入层什么都不用改，只动骨干"，这是低风险渐进迁移叙事的基础。

- id: g09
  term: DHL
  full: Dual Home Loopback（书中未展开定义，此为 AOS 通用叫法，待确认）
  source_chapter: "p32-33"
  definition: |
    书中仅在 2-tier/3-tier 拓扑设计页出现，作为接入交换机上行到 BEB 的冗余选项之一，与 STP、LAG 并列（"STP or DHL towards BEB"、"LAG or DHL"）。
    指 AOS 里接入交换机双归两台 BEB 时的双归属环回检测方案，替代生成树实现主备冗余，具体配置超出本书范围（属售后课程 DT00WTE323）。
    售前用法：客户接入层不愿跑 STP 时，给出 LACP/DHL 的替代选项组合。

- id: g10
  term: DIS
  full: Designated Intermediate System
  source_chapter: "p37-38"
  definition: |
    IS-IS 在多路访问共享链路上选出的指定中间系统，充当伪节点负责链路状态数据库同步和 LSP 泛洪。
    选举规则是接口优先级最高、平局比最大 B-MAC；没有 DIS 备份，但重选约 3 秒完成，无显著中断。
    售前用法：SPB 能经微波点对多点、第三方二层网/运营商网跨多路访问域扩展（p37 use case），靠的就是这套机制。

- id: g11
  term: E-LAN / E-LINE
  full: Ethernet LAN / Ethernet Line service (MEF 服务模型)
  source_chapter: "p50, p53"
  definition: |
    SPB 服务的两种形态：E-LAN 是多点透明局域网服务，一个 I-SID 把多个站点的 SAP 连成一个洪泛域；E-LINE 是两点伪线（pseudo-wire），书里称 SPB Point-to-Point Transparent Circuit，透明转发、不做源 MAC 学习、用头端组播模式。
    一个 E-LAN 服务相当于给每个部门/租户/设备类型一张专有 VPN。
    售前用法：一张骨干同时交付多点 L2 VPN 和点对点专线，直接对应运营商伪线和企业专线的替换场景。

- id: g12
  term: ECT
  full: Equal Cost Tree (ECT-Algorithm / ECT-Mask)
  source_chapter: "p24, p41-43"
  definition: |
    等价树算法：当多条等代价最短路径并存时，用一组平局判决规则从中选路，标准预定义 16 个算法（编号 1-16）。
    计算方法是把路径上各节点的 BridgeID 与 64 位 ECT-Mask 逐字节 XOR，取结果最小的路径；每个 BVLAN 创建时自动分配下一个 ECT 算法号（可修改）。
    单播和组播用同一算法，保证同构对称。售前用法：16 棵等价树是"链路利用率翻倍、带宽分担"卖点的机制；浅层流量工程（把不同 BVLAN 的流量导到不同路径）也靠调 ECT。

- id: g13
  term: EVPN
  full: Ethernet VPN (EVPN-VXLAN)
  source_chapter: "p134, p137, p138"
  definition: |
    以太网 VPN，数据中心主流织物技术，控制面用 BGP、封装用 VXLAN；书 p137 附小词典（EVI=以太网虚拟实例如 VNI、ESI=以太网段标识、DF=指定转发者、IRB=集成路由桥接）。
    对比表（p134）定位：EVPN 部署 Moderate to complex、培训 Moderate to High、排障 Intermediate，主用例是数据中心。
    售前用法：客户点名 EVPN 时不硬顶——用"同一 AOS 全支持"化解锁定质疑，数据中心场景主动让位 EVPN（p138），把 SPB 推回园区/物联网场景。

- id: g14
  term: GRT
  full: Global Routing Table（书 p90 另写 Global Routing Manager，两页写法不一致）
  source_chapter: "p90-91"
  definition: |
    全局路由表：L3 VPN 模式下 VRF 路由先导入/导出 GRT，再选择性进入 ISIS-SPB 的 IPVPN 路由表跨域广告。
    配套动作包括 VRF 到 I-SID 的路由导入、I-SID 之间的路由重分发。
    售前用法：解释"核心设备不需要跑 OSPF/BGP"的原理——路由搭 IS-IS 顺风车穿过骨干，这直接支撑"消灭独立路由层"的论证。

- id: g15
  term: Head-End Replication
  full: Head-End (Multicast) Replication
  source_chapter: "p65-68"
  definition: |
    BUM 流量（广播/未知单播/组播）的本地默认复制模式：入口 BEB 给每个存在该 I-SID 的远端 BEB 各复制一份，封装目的 BEB 的单播 B-MAC，组播跟着单播树走、共用同一张 FDB。
    适合兴趣社区稀疏、组播带宽低的场景；配合服务级 IGMP 窥探（IP Multicast Optimization）可只复制给有 IGMP 客户端的端口。
    售前用法：小规模组播场景状态少、内存省；视频会议类客户给出"优化前后"对比（p67-68）。

- id: g16
  term: I-SID
  full: Backbone Service Instance Identifier
  source_chapter: "p24, p30, p75, p109"
  definition: |
    24 位骨干服务实例标识（取值范围 256-16777214），写在 I-TAG 里，定义帧该映射到哪个服务；一个 I-SID 就是一个 E-LAN 洪泛域，全网唯一。
    所有 SPB 节点经 IS-IS 自动知晓全部服务和端点；机型规格从 2K 到 8K 个 I-SID 不等（p75）。
    售前用法：多租户/微分段卖点的直接载体——"每个部门、每类设备一个 I-SID"；POC 第一步就是和客户一起定 I-SID 编号规划。

- id: g17
  term: Inline Routing
  full: Inline Routing (Front-panel port / Service-based)
  source_chapter: "p92-97"
  definition: |
    不占物理环回线的两种内联路由方式：前面板口内联是把物理口或静态聚合配成 loopback 模式，带宽走前面板口（OS6900-V72/C32）；服务型单遍内联（service-based single-pass）直接在软件里把 IP 接口绑到 SPB 服务，不需专用口（OS6860N/6870/6900-X 系列/9900）。
    IPv4 和 IPv6 接口可绑同一服务，前提是在同一 VRF 实例里。
    售前用法：按客户机型给最省端口、最简配置的路由集成方案，service-based 是新一代机型的默认推荐。

- id: g18
  term: IS-IS SPB
  full: Intermediate System-to-Intermediate System, SPB extensions (RFC 6329)
  source_chapter: "p34-38"
  definition: |
    SPB 的控制面：在 IS-IS 上加 SPB 扩展（Hello、节点信息、邻接信息、服务信息 TLV），完成拓扑与服务自动发现、链路状态数据库同步、最短路径树计算。
    每个节点都以自己为根算树，路径对称（双向一致）、同构（单播组播同路）、靠 RPFC 保证无环；邻接支持点对点和点对多点。
    售前用法："单协议"卖点的核心——一个 IS-IS 同时管 L2 和 L3、IPv4 和 IPv6，替换掉 STP 加一堆 IGP 的协议栈。

- id: g19
  term: L3 VPN
  full: Layer 3 VPN over SPB (SPB IPVPN)
  source_chapter: "p89-91, p94, p97"
  definition: |
    SPB 上承载三层路由的全自动模式：VRF 之间的路由经 IS-IS TLV 交换，骨干上不需要独立路由协议；采用 I-SID-per-VRF 映射，路由经 GRT 导入导出、支持 I-SID 间重分发。
    配置核心是 spb ipvpn bind vrf 1 isid 1000 gateway ... all-routes 加 VRF 的 export/import。
    售前用法：投标 L3 方案时的"全配版"——给客户看连 OSPF/BGP 都不用上核心，路由全靠 IS-IS 顺风车。

- id: g20
  term: LBD
  full: Loopback Detection
  source_chapter: "p71, p73"
  definition: |
    自动环回检测：不需要 STP/RSTP/MSTP，周期性从所有使能端口发检测帧，发现环路后按策略关端口/发 Trap/记事件日志，并支持定时或手工恢复。
    可配在桥口或服务接入口（port/linkagg），SPB 骨干内则按最高 PortID/最高 BridgeID 关端口。
    售前用法：接入层"无 STP 也防环"的配套件，补齐替换生成树故事的最后一块板。

- id: g21
  term: Mac-in-Mac
  full: MAC-in-MAC (Ethernet in Ethernet framing, IEEE 802.1ah)
  source_chapter: "p22-24, p48"
  definition: |
    把客户完整的以太网帧再包一层骨干以太网头（B-DA/B-SA/B-TAG/I-TAG）的封装方式，骨干里只有 B-MAC 可见。
    由此实现地址隔离：客户 MAC 学习被限制在边缘，核心不学客户地址，4096 VLAN 上限被打破。
    售前用法：安全叙事的技术根基——核心见不到客户 MAC 也非 IP 转发，天然免疫 IP 扫描、DOS、中间人（p9）。

- id: g22
  term: MPLS
  full: Multiprotocol Label Switching
  source_chapter: "p134, p136, p138"
  definition: |
    多协议标签交换，运营商和关键业务网的主力技术。书中对比表给它的定位：弹性 Very High、但部署 Moderate to complex、培训 High、协议开销大（LDP/RSVP/BGP）、排障 Complex & Slow、收敛 50ms、成本 $$$。
    适用场景是 MAN/智能城市和铁路电力等对收敛极端敏感的网，或标书强制要求 IP-MPLS 时。
    售前用法：用对比表把天平拉回 SPB（成本 $$、培训低、排障快）；标书强制 MPLS 时退一步卖 MPLS+SPB 混合（p136 架构图）。

- id: g23
  term: OmniFabric
  full: ALE OmniFabric
  source_chapter: "p6, p128-133"
  definition: |
    ALE 的多技术网络织物品牌：同一个 AOS 之下整合 SPB、EVPN、MPLS，主打零信任架构下的端到端安全、宏/微分段、内建自动化和 IoT 设备自动检测分级。
    关键卖点是 IT/OT 融合、防厂商锁定（多厂商环境兼容）、TCO 优化（无隐藏费用、统一管理）。
    售前用法：技术中立防御伞——先承认客户可能要三种技术中的任何一种，再用"SPB 培训成本低、协议开销低、排障快"的对比表把默认选项拉回 SPB。

- id: g24
  term: OmniVista 2500
  full: OmniVista 2500 Network Management System (OV2500)
  source_chapter: "p99-113, p40"
  definition: |
    ALE 的网管系统，内置 SPB Provisioning 应用：服务创建（OneTouch 模式）、L2 Profile 配置、SPB Profile（Tag/I-SID/BVLAN/组播模式/VLAN 翻译）、服务和 SAP/SDP 监控、拓扑视图。
    还能通过控制 BVLAN 的带内管理子网纳管全网（p40）。
    售前用法：图形化交付是"降低运维门槛"的证明材料，POC 演示利器；深度故障排查则指向售后课程。

- id: g25
  term: Outline Routing
  full: Outline Routing (physical loopback cable)
  source_chapter: "p82-84, p87"
  definition: |
    用两根物理环回线做外部路由：一侧端口当 SPB 接入口（SAP 侧），另一侧是只做路由的桥接口（VRF 侧），中间靠一个专用 VLAN 接通。
    书 p83 明确说这是 L3 VPN 设计的首选方法（Preferred method for L3 VPN designs），VLAN UNI 设计里路由实际发生在 SPB 之前的 VLAN 域。
    支持机型 OS6900-X20/X72/T20/Q32、OS6860/E。售前用法：保守方案或老机型的兜底选项，代价是占两个端口和一对线。

- id: g26
  term: PBB
  full: Provider Backbone Bridge (IEEE 802.1ah)
  source_chapter: "p24-25"
  definition: |
    提供者骨干桥标准（802.1ah），即 Mac-in-Mac，是 SPB 的数据面基础；SPB 802.1aq 站在 802.1ad（Q-in-Q 数据面）、802.1ah（PBB 数据面）、IS-IS（控制面）、802.1ag（ETH-OAM）四个成熟标准之上。
    书中用这一点论证 SPB 不是激进新发明。
    售前用法：客户嫌"新技术风险大"时，把 SPB 拆成三个老标准的组合来讲，降低决策心理门槛。

- id: g27
  term: RPFC
  full: Reverse Path Forwarding Check
  source_chapter: "p35"
  definition: |
    反向路径转发检查：交换机收到封装帧后，校验其源 B-MAC 按最短路径树是否应从该端口到达，不是就丢弃。
    这是 SPB 对称同构路径之外的第三道无环保险，专防异常路径帧造成环路。
    售前用法：客户技术负责人追问"凭什么说无环"时的机制级答案（对称 + 同构 + RPFC 三件套）。

- id: g28
  term: SAP
  full: Service Access Point
  source_chapter: "p24, p51, p54-56, p64"
  definition: |
    UNI 侧逻辑端口：把物理端口（或 LAG）和特定客户流量类型（untagged、单标签、双标签、全部）绑定到一个 SPB 服务，只能在接入口上创建；近端客户 MAC 绑定在 BEB 的 MAC 表里。
    分静态 SAP（同口多种封装、多 CVLAN 映射）和动态 SAP（由 UNP 服务档案自动生成），QoS 上分 trusted（信任标签优先级）/untrusted（用户定义优先级）。
    售前用法：客户流量进 SPB 的唯一入口概念；SAP 数量（2K-8K，p75）是机型选型的硬指标。

- id: g29
  term: SDP
  full: Service Distribution Point
  source_chapter: "p24, p52, p108"
  definition: |
    NNI 侧逻辑端口：表示一条到远端 BEB 的 802.1ah 逻辑隧道（B-MAC + BVLAN 组合），把服务绑定到远端实例化该服务的 BEB；远端客户 MAC 绑定在远端 SDP 上。
    全部自动动态配置，人工不碰。
    售前用法："核心/隧道零配置"的直接证据——人工只配置 SAP，NNI 侧全自动，运维只看得到、不用管。

- id: g30
  term: SPB
  full: Shortest Path Bridging (IEEE 802.1aq)
  source_chapter: "p22-23, p76"
  definition: |
    最短路径桥接：用 IS-IS 算路、用 Mac-in-Mac 封装的以太网骨干，每台交换机都是自己最短路径树的根。
    书中卖点清单：千节点规模、亚秒收敛（约 100ms）、全链路利用无阻塞、无环、地址隔离、边缘供给、免许可。
    售前用法：一句话定位后接 STP 四宗罪（次优路径/阻塞浪费带宽/逐跳配置/慢收敛，p23），这是全书攻防的起点。

- id: g31
  term: SPB-M
  full: Shortest Path Bridging - Mac-in-Mac (802.1aq PBB data plane)
  source_chapter: "p24-25"
  definition: |
    采用 802.1ah PBB 数据面的 SPB 模式，是 AOS 实现并主推的模式；与之并列的还有 SPB-V（802.1ad Q-in-Q/PB 数据面）。
    两种模式数据面不同，互通时要确认对端跑的是哪种。
    售前用法：标书和互联方案里写清楚 "SPB-M (PBB)"，避免与 SPB-V 阵营设备对不上。

- id: g32
  term: STP
  full: Spanning Tree Protocol
  source_chapter: "p23, p32-33, p118"
  definition: |
    生成树协议，全书反派：单棵树所有流量绕根桥走、相邻节点也可能五跳、大量端口被阻塞浪费带宽、逐跳配置、收敛慢。
    三个成功案例（Linköping/NDOT/Metz）都把"消灭 STP"作为核心成果。
    售前用法：四大罪弹药库（p23 对比页）是开场破冰的标准打法；客户现网 STP 痛点越多，SPB 越好卖。

- id: g33
  term: Tandem Replication
  full: Tandem Replication (S,G / *,G multicast trees)
  source_chapter: "p65, p69-70"
  definition: |
    BUM 流量的优化复制模式，分两档：(S,G) 模式给每个 I-SID 的每个源建源特定组播树，用特殊组播组 B-MAC（由源节点 SPSourceID 派生）封装，中间节点只装组 B-MAC 表项，带宽效率最高；(*,G) 模式给每个 BVLAN 建一棵共享树，由 BridgeID 最低的节点当根，资源占用更少。
    与 Head-End 相比更适合组播密集、兴趣社区集中的场景。
    售前用法：视频监控、IPTV 类客户的关键卖点——NDOT 路边网络和赌场视频监控用例（p138）直接对应。

- id: g34
  term: UNI / NNI
  full: User-to-Network Interface / Network-to-Network Interface
  source_chapter: "p24, p58"
  definition: |
    网络的两个界面：UNI 面向客户接入，SAP 挂在 UNI 侧；NNI 面向 SPB 骨干互联，SDP 属于 NNI 侧逻辑端口。
    书 p58 起的图把 SPB UNI（接入口/UNP 档案/静态动态 SAP）和 SPB NNI（骨干 BVLAN）分开画，理清配置边界。
    售前用法：借用运营商采购语言讲清"客户侧只配 SAP、骨干侧全自动"的分工，客户网络团队容易对号入座。

- id: g35
  term: UNP
  full: User Network Profile（书中未给全称，此为 AOS 通用叫法）
  source_chapter: "p56, p58-62, p76"
  definition: |
    用户网络档案机制：终端经 MAC 认证（非 supplicant）或 802.1x（supplicant）认证后，被分派到 SPB 服务档案，档案里带 VLAN Tag、I-SID、BVLAN、组播模式、VLAN 翻译、Policy/ACL/QoS，SAP 随之自动创建。
    还支持 persistent SAP（认证后固化的持久 SAP）。
    售前用法："认证-分级-自动供给"（p11）和微分段卖点的落地点——设备插上网线，策略和 VPN 自动到位。

- id: g36
  term: VC
  full: Virtual Chassis
  source_chapter: "p32-33, p133, p138"
  definition: |
    虚拟机箱：多台物理交换机堆叠成一台逻辑设备。SPB 2-tier 设计里，BEB 冗余可用"两台以上物理机箱组成 VC 拓扑的 BEB"实现（配 LACP 无环接入）。
    p133 把 Virtual Chassis 列为 AOS 通用能力，p138 的用例规模也以 Virtual-chassis 为单位统计。
    售前用法：客户要"核心双机、接入双归属但不想跑 STP"时，VC 化 BEB 加 LACP 是标准答案。

- id: g37
  term: VLAN Translation
  full: VLAN Translation (per access port / per service)
  source_chapter: "p57, p58-59, p93"
  definition: |
    VLAN 翻译：按接入口或按服务把客户 VLAN 编号在 SAP 处翻译，让不同站点 VLAN 编号不一致的流量（如 20/30/10/21/40）进同一个 I-SID。
    可在 UNP 服务档案里启停，配置示例见 p93 的 vlan-xlation enable。
    售前用法：客户现网 VLAN 编号混乱、两栋楼同一个业务不同 VLAN 号——这是迁移方案里最常被问到的痛点，直接给这页。

- id: g38
  term: VPN-Lite
  full: VPN-Lite (VRF routing over SPB)
  source_chapter: "p85-88, p93, p96"
  definition: |
    轻量版 L3 over SPB：SPB 骨干当物理媒介用，各 BEB 的 VRF 之间跑标准路由协议（静态路由、OSPF、VRRP），路由器自己算路，不用 IS-IS TLV 传路由。
    可用物理环回线、前面板口内联或服务型内联三种承载方式，配置守则见 p88。
    售前用法：客户运维团队只会 OSPF 时的低门槛选项；和 L3 VPN 组成"简版/全版"两档报价，先上 Lite 再平滑升级。

- id: g39
  term: VRF
  full: Virtual Routing and Forwarding
  source_chapter: "p81, p88, p90"
  definition: |
    虚拟路由转发实例：BEB 在 VRF 里做三层转发、同时做 SPB 桥接，不同 BEB 上的 VRF 靠同一 I-SID 连成一张网。
    VPN-Lite 里一个 VRF 可绑多个 I-SID，但两个 VRF 不能共享同一个 I-SID（p88）；规格上支持 VRF 到 I-SID 的一对一/一对多映射（p75）。
    售前用法：多租户三层隔离的基本单位；VRF-I-SID 映射方案是 L3 售前方案的设计参数。

- id: g40
  term: VXLAN
  full: Virtual eXtensible LAN
  source_chapter: "p32, p76, p134, p139"
  definition: |
    数据中心 overlay 封装技术，EVPN 的数据面搭档。书中两个用途：EVPN-VXLAN 数据中心织物（p134/137）；以及远程站点扩展——SPB 域的 NNI 可以借 VXLAN（或 MPLS）隧道连到远端节点（p32/76）。
    p139 给出各机型 VxLAN/VxLAN EVPN 支持矩阵。
    售前用法：SPB 和 EVPN 不是二选一——跨数据中心互联场景可用 VXLAN 当 SPB 节点间的传输垫层，打消"选了 SPB 就进不了 DC"的顾虑。
