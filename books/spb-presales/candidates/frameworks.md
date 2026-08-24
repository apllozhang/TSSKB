# frameworks.md · 决策框架 / 思维模型 / 结构化方法提取
# 来源: OmniSwitch LAN SPB Presales (DT00XPS279EN Issue 05)
# 规则: 每条含原文引用与页码；宁多勿漏，待后续独立验证阶段筛选

```yaml
- id: f01
  title: SPB"瑞士军刀"全场景定位框架（一个方案 × 三类场景 × 四种用途）
  type: framework
  source_chapter: "p7"
  source_quote: |
    "IT'S AN ALL-IN-ONE SWISS-KNIFE SOLUTION
    ◼Spanning Tree replacement ◼Multi-tenancy ◼Micro-segmentation ◼IoT
    Campus
    Data Centre: ◼Intra and inter-DC fabric ◼Any to any ◼Fast convergence
    WAN: ◼MPLS-like L2/L3 VPN Services ◼Multi-site ◼Multi-tenancy
    One Solution ✓Reduce the complexity of managing multiple technologies."
  summary: |
    售前开场定位框架：把 SPB 包装成"一把瑞士军刀"，横向覆盖园区、数据中心、广域网三类场景，纵向在每个场景里对应四种用途（替换生成树、多租户、微分段、IoT），落点是"一个方案降低多技术管理复杂度"。结构是"单一技术 × 场景矩阵"，用途是让客户先接受"不必为每个场景引入不同织物技术"的总命题，再展开后续分卖点。p8 进一步补充全产品线覆盖（加固型/模块化/紧凑型/接入型四种形态对应不同部署位置），强化"全场景都有机型落地"的论证。
  tags: [positioning, spb, presales, swiss-knife]

- id: f02
  title: 非 IP 转发安全论证法（"不是 IP，所以免疫 IP 攻击"推理链）
  type: framework
  source_chapter: "p9"
  source_quote: |
    "IT'S NOT IP-BASED => IT'S MORE SECURE
    x Scanning
    x DOS
    x Man-in-the-middle
    x …
    ✓
    Not vulnerable to IP-based attacks"
  summary: |
    售前攻防论证结构：把"SPB 核心转发基于 BMAC 而非 IP"这一技术事实，转译为安全卖点——逐项列出 IP 扫描、DOS、中间人等 IP 类攻击手段并打叉，推出"天然免疫 IP 类攻击"的结论。推理路径是"技术特性 → 威胁模型逐项排除 → 安全结论"，可迁移到任何"用架构差异化解安全质疑"的售前场景。p15-17 再补充"动态弹性 ⇒ 更安全"的延伸论证（服务随策略伸缩、缩小攻击面），同一手法把弹性也归入安全收益。
  tags: [security, argumentation, presales, spb]

- id: f03
  title: 互操作投资保护论证法（协议清单 → 三项客户承诺）
  type: framework
  source_chapter: "p10"
  source_quote: |
    "IT'S INTEROPERABLE AND BACKWARDS COMPATIBLE
    L2: ◼802.1Q ◼Q-in-Q ◼LACP ◼Etc
    L3: ◼OSPF ◼IS-IS ◼BGP
    Multicast: ◼PIM SM ◼PIM DM ◼PIM BIDIR ◼PIM SSM
    ✓ Investment protection
    ✓ Phased migration
    ✓ No forklift upgrade"
  summary: |
    回应 CIO"换网会不会推翻现有投资"质疑的论证框架：分 L2/L3/组播三层罗列 SPB 可互通的既有协议清单，然后落三条承诺——投资保护、分阶段迁移、无需整体推倒重来（no forklift upgrade）。结构是"兼容性清单 + 客户语言的三项收益承诺"，把技术互操作翻译成财务与风险语言。适合投标答辩里"平滑演进"章节的标准论证骨架。
  tags: [interoperability, investment-protection, argumentation, presales]

- id: f04
  title: 宏/微分段三步法（对每类设备执行 认证 → 分类 → 供给）
  type: framework
  source_chapter: "p11"
  source_quote: |
    "MACRO AND MICRO-SEGMENTATION
    ✓ Authenticate ✓ Classify ✓ Provision — Users
    ✓ Authenticate ✓ Classify ✓ Provision — HVAC
    ✓ Zero-trust framework
    ✓ Software-defined segmentation"
  summary: |
    零信任分段的操作化方法：对每一类接入对象（用户、暖通 HVAC 等 IoT 设备）统一走"认证 → 分类 → 按角色供给策略"三步，用宏分段（粗粒度隔离）与微分段（细粒度策略）组合实现。论证价值在于把"零信任"从概念落到三步可执行动作上，且不同对象类型复用同一条流水线。售前可用它回答"微分段具体怎么落地"，也是把 SPB 多租户能力包装成安全方案的桥梁。
  tags: [zero-trust, segmentation, iot, method]

- id: f05
  title: 网络自动化"简化"四支柱论证法（Simpler / Automatic / Edge-only / Single-protocol）
  type: framework
  source_chapter: "p12"
  source_quote: |
    "SIMPLER NETWORK AUTOMATION
    Simpler: ◼Auto backbone ◼Auto services ◼Auto attachment ◼Self healing
    Edge Only: ◼Edge-only provisioning ◼No-touch core ◼OmniVista NMS
    Single Protocol: ◼No protocol "stack" ◼One protocol ◼L2 + L3 ◼IPv4 + IPv6 IS-IS
    ✓ Simpler to deploy ✓ Simpler to operate"
  summary: |
    降本论证框架：从四个支柱论证 SPB 比"协议栈式"方案更省——①自动化三件套（auto backbone / auto services / auto attachment）加自愈；②只在边缘配置、核心零触碰；③单一协议（IS-IS）同时管 L2+L3、IPv4+IPv6，没有协议栈；④落到"部署更简单、运维更简单"两条运营结论。可迁移为任何网络方案的"复杂度对比"话术骨架：把复杂度拆成配置面、管理面、协议面三个维度逐项对比。
  tags: [automation, tco, argumentation, is-is]

- id: f06
  title: 双域并行分阶段迁移法（SPB 域与遗留域共存，按服务逐块搬迁）
  type: framework
  source_chapter: "p13"
  source_quote: |
    "IT CAN RUN IN PARALLEL WITH YOUR CURRENT DESIGN
    ✓SPB Domain
    HVAC
    ✓SPB Domain
    Security
    ✓Legacy Domain
    Desktop
    Telephony
    ✓Phased migration"
  summary: |
    迁移策略框架：把网络划分为 SPB 域与遗留（Legacy）域并行运行，按业务/部门（如先 HVAC、安防等 IoT 流量，后桌面、语音）逐批把服务搬进 SPB 域，实现分阶段迁移而非一次割接。论证用途是消除客户"割接风险"顾虑：每一步都可回退、两域长期共存。p14 进一步给出跨第三方网络扩展的变体（WAN 抽象、端到端服务、无需服务拼接）。与 f03（互操作承诺）构成"能共存 → 可分批"的完整迁移论证链。
  tags: [migration, phased-rollout, risk-reduction, spb]

- id: f07
  title: STP vs SPB 十维攻防对比框架（售前对抗性论证模板）
  type: framework
  source_chapter: "p23"
  source_quote: |
    "STP VS. SPB
    Spanning Tree: A single tree, the traffic always has to pass through the 'Root' bridge • F to G requires five hops and it is right next to G • Lots of blocked path, wasted bandwidth • Hop by hop configuration • Inefficient links utilization • No Shortest Path • Inefficient Broadcast • Low scalability • High convergence times
    SPB: Each switch is its own Root Bridge with symmetrical trees • Controlled by IS-IS • Traffic flows the Shortest path • Address isolation through Mac-in-Mac • Mesh topologies • No loops • Fast recovery"
  summary: |
    全书核心攻防页：左右分栏把生成树的九条罪状（单棵树绕根桥、次优路径举 F-to-G 五跳实例、阻塞链路浪费带宽、逐跳配置、链路利用率低、无最短路径、广播低效、扩展性差、收敛慢）与 SPB 的对应优势逐条对齐。可迁移的论证结构是"痛点清单 ↔ 特性清单一一映射 + 一个具体反例数字"，用于任何新旧技术替换提案。p76"Key Takeaway"再用弹性/安全/可管理三类归纳同一批优势，形成 recap 版本。
  tags: [argumentation, stp, comparison, presales]

- id: f08
  title: SPB 拓扑层级选型法（3-tier BEB/BCB 分工 vs 2-tier 全 BEB 网格）
  type: framework
  source_chapter: "p32"
  source_quote: |
    "SPB DESIGN 3-TIER TOPOLOGY
    Access Switch: 802.1Q VLAN on LAG • STP or DHL towards BEB • Redundancy through VC BEB and/or dual BEB nodes, LACP protocol
    Aggregation Switch: Backbone edge bridge (BEB) role • VLAN to I-SID • IS-IS for MAC learning • IS-IS for SPB paths • PBB for data plane • Redundancy through dual BCB nodes
    Core Switch: Backbone Core Bridge (BCB) role • Learns BEB addresses"
  summary: |
    拓扑设计决策框架。3-tier 版（p32）：接入交换机保持 802.1Q+LAG 传统方式上联，汇聚层承担 BEB 角色（VLAN→I-SID 映射、IS-IS 学 MAC、PBB 数据面），核心层做纯 BCB（只学 BEB 地址、按 BMAC 转发），冗余靠双 BCB。2-tier 版（p33）：取消 BCB，核心交换机直接做 BEB，BEB 之间部分或全网状连接，冗余靠虚拟机箱（VC）多机箱 BEB。选型依据是层级规模与冗余手段：中小型扁平化用 2-tier 省掉一层；大型/需要独立核心转发层用 3-tier。两版都保留"经 MPLS/VXLAN 域扩展到远端站点"的选项。
  tags: [topology, design, 2-tier, 3-tier, beb, bcb]

- id: f09
  title: 最短路径树计算与 ECT 等价树选路法（metric → 跳数 → 16 个 ECT 平 mask 决胜）
  type: framework
  source_chapter: "p42"
  source_quote: |
    "SHORTEST PATH TREES CALCULATION
    ◼Metric (Link cost) lower metric = higher priority
    ◼Lowest Hop Count = higher priority
    ◼When multiple links have an equal cost (metric and hop count)
    ◼All bridges use predefined ECT algorithms to calculate layer 2 congruency and symmetry for switching
    • Standard provides 16 predefined algorithms • 16 ECT -> index 1-16
    • Byte-by-byte XOR ECT-MASK (16 masks to provide 16 ECT) for all nodes excluding source and destination"
  summary: |
    SPB 选路的三级决胜规则：先比链路 metric（低者优先），再比跳数（少者优先），等价路径存在时用 16 个预定义 ECT 算法（对 BridgeID 逐字节 XOR 不同 ECT-MASK）生成排序路径表、取最低路径 ID，且同一算法同时用于单播和组播以保证同构一致（symmetry/congruency）。每个 BVLAN 创建时自动分配下一个可用 ECT-ID（可改），从而使多条等价链路可同时活跃分摊流量。p43 给出故障重算示例：某链路失效会从 ECT 候选列表剔除相关树、由次优树接管。售前用它解释"为什么 SPB 能用满所有链路还无环"。
  tags: [ect, path-selection, load-balancing, is-is, spb]

- id: f10
  title: L2 控制帧三态处置法（Tunnel / Drop / Peer 及默认策略表）
  type: framework
  source_chapter: "p63"
  source_quote: |
    "L2 Protocol Default Treatment: STP Tunnel; 802.1X Drop; 802.1AB Drop; 802.3AD Peer; GVRP Tunnel; AMAP Drop; MVRP Tunnel
    Peer: Interact with the peer switch according to the protocol
    Drop: discards unconditionally the specified PDU
    Tunnel: Control packet encapsulated across the SPB network"
  summary: |
    SAP 口上对二层控制协议的处置决策框架：每个控制协议只能在三种处理里选一——Tunnel（封装透传过 SPB 网络，两端设备无感知）、Drop（无条件丢弃）、Peer（在边缘与对端设备正常交互协议）。书中给出默认表：STP/GVRP/MVRP 默认 Tunnel，802.1X/802.1AB/AMAP 默认 Drop，802.3AD（LACP）默认 Peer。设计方法是为每个 SAP 关联 L2 Profile、按"该协议应该被透传、拦截还是终结"逐项决策。可迁移为"中间网络对遗留控制协议的分类处置"通用思路。
  tags: [l2-profile, tunnel, drop, peer, design]

- id: f11
  title: SAP 信任模式 QoS 决策矩阵（流量封装类型 × Trusted/Untrusted）
  type: framework
  source_chapter: "p64"
  source_quote: |
    "Traffic is classified at the SAP level
    Highest priority assigned to untagged tunneled L2 Control BPDUs
    No further classification within the SPB backbone due to MAC-in-MAC encapsulation
    Trusted SAPs: Tagged traffic priority derived from tags
    Untrusted SAPs: Set the CoS marking to a user-defined value
    Tagged (VLAN 1–4094) / QinQ (outer VLAN 1–4094) / Wild Card / Untagged — each Trusted or Untrusted"
  summary: |
    边缘 QoS 分类的决策矩阵：分类只发生在 SAP 入口（核心因 Mac-in-Mac 封装不再分类），矩阵两轴分别是封装类型（Tagged/QinQ/通配/Untagged）与信任模式——Trusted 沿用报文自带标记（untagged 用端口默认优先级），Untrusted 则由管理员统一改写 CoS。经 Tunnel 透传的 L2 控制 BPDU 恒定最高优先级是矩阵的特例规则。可迁移的思路是"边缘一次分类、核心零再分类"，以及"是否信任用户侧标记"这一信任决策维度。
  tags: [qos, cos, sap, decision-matrix]

- id: f12
  title: BUM 组播复制模式选择法（Head-End 逐副本 vs Tandem S,G / *,G 共享树）
  type: framework
  source_chapter: "p65"
  source_quote: |
    "MULTICAST FORWARDING
    BUM = Broadcast Unknown Multicast • ARPs packets, Boot-p/DHCP requests, etc.
    SPB supports two BUM traffic distribution methods for replicating and forwarding multicast frames
    • Head-End (native mode)
    • Tandem (optimized)"
  summary: |
    组播设计选择框架，两个主选项加一个优化开关。Head-End（原生模式，p66）：入口 BEB 复制，对每个存在该 I-SID 的远端 BEB 发一份、用其 BMAC 封装、沿单播树走，适用判据是"兴趣社区稀疏、组播带宽低"。Tandem（优化模式，p69-70）再分两档：S,G 按每源每 ISID 建源特定组播树（带宽效率最高），*,G 按 BVLAN 建共享树、最低 BridgeID 节点当根（资源占用最少）。第三个维度是 IP 组播优化（p67-68）：开 IGMP snooping 前 BUM 洪泛所有 SAP/SDP，开后只复制给有 IGMP 客户端的端口。选型逻辑：接收端少且流量小选 Head-End，接收端多或带宽敏感选 Tandem，按资源预算决定 S,G 与 *,G。
  tags: [multicast, head-end, tandem, selection, bum]

- id: f13
  title: AOS SPB 配置分层法（Core level NNI 配置 vs Access level UNI 配置）
  type: framework
  source_chapter: "p73"
  source_quote: |
    "Control Plane (NNI ports) SPB Core level On BEB + BCB
    Data Plane (UNI ports) SPB Access level Only on BEB
    Services: UNP Access Port (Dynamic), UNP Profiles (Dynamic), Access Port SAP, Access Port (Static), SAP (Static/Dynamic), Pseudo-wire, Service
    L2 Profiles (optional), Loopback Detection (LBD) (optional)"
  summary: |
    把 SPB 配置工作按两个层级组织的方法：核心层（SPB Core level，作用在 NNI 口，BEB 与 BCB 都要配）只管 IS-IS 接口、BVLAN、控制 BVLAN 等骨干控制面；接入层（SPB Access level，只在 BEB 上）管服务面——静态/动态 SAP、UNP profile、伪线、可选的 L2 Profile 与环回检测。价值在于配置清单可拆成"骨干一次配好、之后基本不动；服务只在边缘增删"两张独立工单，与 f05 的 edge-only 论证互为印证。售前做实施方案时可直接按此两张表排配置工作量。
  tags: [configuration, edge-only, unp, sap, method]

- id: f14
  title: L3 集成形态三选一（Outline 物理环回线 / 前面板口 inline / Service-based 单遍 inline）
  type: framework
  source_chapter: "p79"
  source_quote: |
    "LESSON SUMMARY
    ✓Concepts
    ✓Outline routing
    ✓Front-panel ports Inline Routing
    ✓Single-pass Inline Routing
    ✓VPN Lite method
    ✓L3 VPN method"
  summary: |
    把 L3 流量叠加到 SPB 骨架上的三种物理形态选择法。①Outline（p82-84）：用外部环回线缆连两个物理口，一侧做 SPB SAP、一侧做路由 VLAN 口，通用性最好、多数机型支持，但消耗端口和线缆；其"端点经 VLAN UNI 接入"的变体是 L3 VPN 设计首选，因为 SAP 口对 port-QoS、DHCP Snooping、STP 等边缘特性支持受限（p83）。②Front-panel inline（p92-94）：端口软件配置 loopback 模式，免外部线缆但仍占前面板口，仅 OS6900-V72/C32 支持。③Service-based 单遍 inline（p95-97）：IP 接口直接绑定 SPB service（vrf 1 ip interface … service 10），零端口占用、软件单遍路由，支持机型最广（6860N/6870/6900/9900 等）。选型维度为端口预算、机型支持矩阵（p75）与边缘特性需求；每种形态之上再选 VPN-Lite 或 L3 VPN 路由机制（见 f15）。
  tags: [l3, selection, inline-routing, outline, vpn]

- id: f15
  title: VPN-Lite vs L3 VPN 路由机制两档选法（跑路由协议 over ISID vs IS-IS TLV 分发路由）
  type: framework
  source_chapter: "p85"
  source_quote: |
    "VPN Lite
    Routing L3 traffic over a L2 SPBM backbone network
    Run routing protocols on L3VPN IP interfaces
    VRFs interconnections across a SPB cloud
    SPB acts more like a physical media"
  summary: |
    在选定 L3 形态后选路由机制的两档框架。VPN-Lite（简版）：SPB 只当物理媒介，VRF 之间跑静态路由或 OSPF（点对点/多点路由、VRRP 冗余均可），配置准则见 p88——每 VRF 在环回路由侧单 IP 接口绑定专用 VLAN、多 IP 接口可绑不同 I-SID 但两个 VRF 不得共享同一 I-SID、对侧 SAP 用相同 VLAN 标识。L3 VPN（全版，p89-91）：不用任何 IP 路由协议，VRF 路由经 IS-IS SPB 的 TLV 直接跨骨干分发，采用 ISID-per-VRF 映射，配合 GRT（全局路由表）做导入导出、I-SID 间重分发。选档逻辑：客户已掌握 OSPF/静态路由、规模小、要简单 → VPN-Lite；要 MPLS 式自动路由分发、多 VRF 大规模 → L3 VPN。
  tags: [vpn-lite, l3vpn, vrf, isid, selection]

- id: f16
  title: OV2500 服务创建流程法（Basic → UNP Profiling 可选 → Advanced 按需 → 创建）
  type: framework
  source_chapter: "p104"
  source_quote: |
    "SPB - SERVICE CREATION
    • Basic
    Select/edit/add devices
    UNP Profiling
    (Optional Steps)
    Advanced
    (if required)
    Service - Creation"
  summary: |
    用 OmniVista 2500 创建 SPB 服务的结构化流程：第一步 Basic 选定目标设备，第二步 UNP Profiling 为可选项（配置动态接入画像），第三步 Advanced 仅在需要时设置高级参数，最后执行服务创建。方法论要点是"必选项最小化、可选项显式分层"，避免管理员一次面对全部参数；配合 p100 的四大功能分区（服务配置 / L2 Profiles / 全局设置 / OneTouch 模式）与 p109 的 SPB Profile 模板（Tag/ISID/BVLAN/组播模式/VLAN 翻译一次定义、多处套用），形成模板化交付路径。可迁移为网管侧"向导式服务开通"设计思路。
  tags: [ov2500, provisioning, workflow, template]

- id: f17
  title: STP→SPB 无中断迁移操作法（独立 STP 域隔离 + 点对点 SPB 服务承载 STP 控制）
  type: framework
  source_chapter: "p123"
  source_quote: |
    "Loops without SPBs are controlled by unique and independent STP instances
    BEBs adjoining two loops are configured with two STP instances in Root Bridge and Next Best Root.
    A point-to-point SPB service is dedicated to transporting STP control.
    SPB uses an SPF algorithm to find the best path between two nodes. Several BVLANs will be included to allow several active paths to be maintained."
  summary: |
    Metz 案例展示的迁移施工法：核心网交换机先全部 SPB 化（该区域不再有 L2 环）；尚未迁移的接入环各自运行独立 STP 实例防环，横跨两个环的 BEB 配置两个 STP 实例（Root Bridge 与 Next Best Root）实现桥接，专门建一条点对点 SPB 服务用来传输 STP 控制帧；同时取消 transit VLAN（SPB 按服务映射流量）、部署多个 BVLAN 维持多条活跃路径。总原则是"SPB 区域无环、遗留区域 STP 自治、交界点受控桥接、服务级搬迁"，实现全程无业务中断（p124 验证：No service disruption during the transition）。这是 f06 分阶段迁移框架在真实工程里的操作细则。
  tags: [migration, stp, non-disruptive, metro, case-method]

- id: f18
  title: 改造案例论证三段式（现状痛点 → 改造后架构 → 四组收益亮点）
  type: framework
  source_chapter: "p124"
  source_quote: |
    "KEY HIGHLIGHTS
    • No service disruption during the transition
    • Extended Level 2 transparent for existing L2 services
    • All links are used
    • Replacement of Spanning Tree protocols
    • Use of the shortest paths
    • IS-IS: automatic traffic protection and redirection
    • Configuration of SPB access services at the edge only
    • Integration of existing standards
    OPTIMISING BANDWIDTH AND STABILITY / LATENCY AND RESILIENCE / SIMPLIFIED CONFIGURATION AND MONITORING / SIMPLE, LOW-IMPACT TRANSITION"
  summary: |
    成功案例的标准包装结构，以 Metz（80 栋楼、200 台交换机）为例：p121 先铺背景（规模、自持光纤、设备种类），p122 用编号痛点刻画旧网（大广播域、万级设备扁平 L2、路由集中在双路由器 VRRP、全部 VLAN 上联 transit VLAN、STP 防环），p123 给改造后架构（对应 f17），p124 把收益归入四组标题——带宽与稳定、时延与弹性、配置与监控简化、平滑迁移。可迁移为售前 reference 的通用叙事模板：背景量化 → 痛点编号 → 方案要点 → 收益分组，且收益组与客户质疑一一对应。NDOT 案例（p118-119）是同模板的交通行业变体（"路边网络企业级化"演进论证）。
  tags: [case-study, storytelling, presales, reference]

- id: f19
  title: SPB vs EVPN vs MPLS 七维定位对比决策表
  type: framework
  source_chapter: "p134"
  source_quote: |
    "Main use case: SPB — Datacenter, Campus, IoT Networks; EVPN — Datacenter; MPLS — Service Provider & Mission critical networks
    Scalability: Large / Large-Very large / Large-Very large
    Resiliency: High / High / Very High
    Ease of deployment: Simple to Moderate / Moderate to complex / Moderate to complex
    Training needed: Low to Moderate / Moderate to High / High
    Protocol Overhead: Low, IS-IS only / Moderate, BGP & VXLAN/MPLS / High, LDP, RSVP, BGP
    Troubleshooting: Simple & Fast / Intermediate time / Complex & Slow"
  summary: |
    技术中立防御的核心决策表：当客户指定 EVPN 或 MPLS 时，用七个维度（主用场景、扩展性、弹性、部署难度、培训成本、协议开销、排障难度）横向对比三种织物技术，让 SPB 在部署/培训/开销/排障四维占优、仅在"极低收敛/超大规格"场景让位。p136 补充架构定位版：MPLS 收敛 50ms 但复杂且成本 $$$，SPB 收敛 100ms 成本 $$，同一张网可 MPLS 骨干 + SPB 接入混布。配合 p6/p129/p133 的"三技术同一 AOS"维恩定位，化解厂商锁定质疑的同时把默认选项拉回 SPB。投标"技术选型"章节可直接复用此表结构。
  tags: [selection, spb, evpn, mpls, comparison, positioning]

- id: f20
  title: 行业用例选技术矩阵（市场 × 关键问题 × 推荐技术）
  type: framework
  source_chapter: "p138"
  source_quote: |
    "USE CASE EXAMPLES
    Market / Key Issues / Advantage
    Video Surveillance: Scale < 1,000, Virtual-chassis, Staff with video expertise, Multicast → SPB – simplicity
    Campus Network: Staff with broad responsibility (LAN, WLAN, FW) → SPB - simplicity
    ITS Network: Staff with broad responsibility, Outdoor deployments → SPB – simplicity, ruggedized equipment
    Large-data center: Scalability → EVPN
    Rail, E&U: Very low convergence-times → IP-MPLS
    MANs/Smart City: Scalability, Traffic Control → SPB/IP-MPLS* (* When IP-MPLS is mandatory in the tender)"
  summary: |
    按行业选技术的快速决策矩阵：行是细分市场（视频监控、赌场、园区、智能交通、大型数据中心、铁路与电力、城域/智慧城市），列是"关键问题"（规模上限、团队技能面、组播需求、室外部署、收敛时间、标书强制要求），单元格给出推荐技术。决策线索以"运维团队画像"为主——技能面广而不深的团队一律推 SPB（卖点 simplicity），超大数据中心推 EVPN，极低收敛要求推 IP-MPLS，标书强制 MPLS 时推 SPB/MPLS 混合。与 p131 的分区布局法（园区 SPB / 数据中心 EVPN / 城域 MPLS）互补，构成"按区域 + 按行业"两张选型索引。
  tags: [selection, vertical-market, use-case, spb, evpn, mpls]
```
