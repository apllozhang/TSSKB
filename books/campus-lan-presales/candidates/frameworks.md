# Campus LAN Presales Ed29 · 决策框架/思维模型候选（frameworks.md）
> 提取器：框架提取器（cangjie-skill 流水线）
> 来源：fulltext.md（480 页全书）+ figures_captions.md + BOOK_OVERVIEW.md
> 原则：宁多勿漏，每条含原文引用与页码；后续有独立验证阶段筛选

```yaml
- id: f01
  title: 网络设计目标十维检查清单
  type: framework
  source_chapter: "p287"
  source_quote: |
    "NETWORK DESIGN PROCESS GOALS AND CONSIDERATIONS
    • Scalability • Adaptability • Reliability • Cost / ROI • Predictability
    • Ease of Implementation • Manageability • Business / Application Growth
    • Troubleshooting"
  summary: |
    在动手画拓扑之前，先用十个维度校验设计是否合格：可扩展性、适应性、可靠性、成本/投资回报、可预测性、实施难度、可管理性、业务/应用增长、故障排查。
    这是全书方案设计章节（p283 起）的入口检查清单，任何客户需求进来都先过这十项再选架构。
    售前可用于方案评审自查，也可反向用作客户需求澄清提纲——逐项问客户"你在乎哪几条"。
  tags: [design, checklist, requirements]

- id: f02
  title: 分层×拓扑二维设计法（2-tier/3-tier × 拓扑类型选择）
  type: framework
  source_chapter: "p288"
  source_quote: |
    "LAN OMNISWITCH HIERARCHICAL LAYERING DESIGN APPROACH
    Network Topology: Shared / Ring / Star / Tree / Spine & Leaf / POD / Mesh
    Network Architecture: Access–Aggregation–Core, 2-tier, 3-tier"
  summary: |
    ALE 园区网设计的第一刀切法：先在网络架构轴上选 2-tier（接入+核心）还是 3-tier（接入+汇聚+核心），再在网络拓扑轴上选 Star/Tree/Ring/Mesh/Spine-Leaf/POD 等形态，两轴组合出具体架构。
    3-tier 适合可扩展分段、灵活低成本、中等密度场景（p289）；2-tier 适合高吞吐高密度、最低时延（1.5-6µs）、接入汇聚合并、管理点更少的场景（p291）。
    售前拿到客户平面图后按此二维矩阵定位，15 分钟内可出架构草图雏形。
  tags: [design, topology, selection]

- id: f03
  title: 机型层级定位表用法（基础设施层级→机型决策表）
  type: framework
  source_chapter: "p300"
  source_quote: |
    "OMNISWITCH SELECTION NETWORK LAYER BASED
    Model × Layer: User Access / Distribution / Core / Data Center
    Switch model utilization per infrastructure layer"
  summary: |
    一张"机型 × 层级"的是/否矩阵表：OS6360/OS6465 只能做用户接入，OS6560/E/OS6570M 可上汇聚，OS6860N/OS6870/OS6900/OS9900 可做核心与数据中心（OS6900 明确不做用户接入）。
    用法是先确定设备要落在哪一层（用户接入/汇聚/核心/数据中心），再用表横向筛出候选机型集合，是选型流程的第二步（第一步是定架构层级）。
    该表可直接抄进方案建议书作为选型依据页。
  tags: [selection, matrix, layering]

- id: f04
  title: 机型功能矩阵筛选法（功能需求→机型过滤）
  type: framework
  source_chapter: "p301"
  source_quote: |
    "OMNISWITCH SELECTION FOR CAMPUS DESIGN
    Availability: Virtual Chassis / ISSU / Hot swap power supply
    Layer 2: Shortest Path Bridging (SPB) / DHL Active-Active / ERPv2
    Layer 3: Basic / Advanced / VRF / Multicast routing
    User network Profile / Fanless / Metro Ethernet / MPLS / Remote VC
    ** License based feature"
  summary: |
    与层级定位表（f03）互补的第二张决策表：把 11 个机型当列、把关键功能当行（VC、ISSU、热插拔电源、SPB、DHL、ERPv2、基础/高级 L3、VRF、组播路由、UNP、无风扇、Metro Ethernet、MPLS、远程 VC），逐格打勾筛机型。
    客户招标文件里的硬性技术条款可直接映射到行，再取"全满足列"即得合规机型；带 ** 的项需加 License，报价时要同步补许可行。
    这是"需求清单→机型"的可复用过滤器，也是应标符合性表的底稿。
  tags: [selection, matrix, features, compliance]

- id: f05
  title: 虚拟机箱 vs 物理机箱对比决策法
  type: framework
  source_chapter: "p303"
  source_quote: |
    "VIRTUAL CHASSIS VS PHYSICAL CHASSIS
    Virtual Chassis (6x6900) / Chassis (9907/9912):
    Initial Investment: Lower – Pay as you grow / Higher
    Rack space: Lower (6U) / Higher (11U/17U)
    Cost: Lower / Significantly Higher
    Redundancy: Mgmt, PS / Mgmt Module, Fabric, PS, Fans"
  summary: |
    回答"客户问为什么不做整机箱"的标准决策表：从初期投资（按需扩容 vs 一次到位）、时延（多跳略高 vs 单跳略低）、重启时间、机架空间（6U vs 11/17U）、管理方式（分布式 vs 集中式）、PoE、成本、端口密度、冗余维度逐项对比 VC 堆叠与 9907/9912 机箱。
    结论倾向：预算受限、渐进扩容选 VC；追求极致时延与单机冗余（管理模块/交换矩阵/电源/风扇全冗余）选物理机箱。
    竞标防守时可直接引用此表挡"堆叠不如机箱"的攻击。
  tags: [selection, comparison, cost, vc]

- id: f06
  title: 高可用方案六选一对比决策矩阵
  type: framework
  source_chapter: "p129"
  source_quote: |
    "HIGH AVAILABILITY DESIGN SUMMARY
    Redundancy solution ACTIVE-ACTIVE L2: VIRTUAL CHASSIS (VC) preferred — Link redundancy / 100% Bandwidth / Switch redundancy / Unified Management / Unified L2/L3
    STP: 50% Bandwidth … LACP … DHL Active-Active: 100% Bandwidth … ERP: Scalability … SPB: 100% Links UP / Traffic isolation"
  summary: |
    把六种高可用手段（STP、LACP、DHL Active-Active、ERP 环网、VC 虚拟机箱、SPB）放到统一坐标下对比：链路冗余、带宽利用率（50% 还是 100%）、收敛时间、交换机冗余、可扩展性、统一管理。
    书中明确标注 VC 为 ACTIVE-ACTIVE L2 场景的"preferred"方案；SPB 以全链路可用+流量隔离胜出；STP 只剩 50% 带宽作为兜底。
    客户提出可靠性指标（收敛时间、双活要求）时，用此矩阵横向定位应选哪种技术组合。
  tags: [design, resiliency, comparison, ha]

- id: f07
  title: SMB 一体化参考架构模板
  type: framework
  source_chapter: "p305"
  source_quote: |
    "OMNISWITCH 6360/6560 SMALL BUSINESS SOLUTION
    • SMB solution
    • Short installation and set-up time with zero-touch configuration saves time/cost
    • Fully integrated and lab tested, single vendor, plug and play solution (IP Network + Wi-Fi + Voice + Mobility)"
  summary: |
    面向 20-100 用户 SMB 的套用模板：OS6360/6560 做接入，叠加 Stellar AP、OmniPCX 话机、PTZ 摄像头，组成单厂商即插即用的语音+数据+Wi-Fi 一体网。
    核心卖点是零接触配置（与 OXO 配合"20 分钟配好语音、数据、Wi-Fi"，见 p306），适合追求极简安装的小微场景。
    售前遇到小企业/分支/门店需求，直接套此模板改端口数即可出图出 BOM。
  tags: [reference-architecture, smb, unified-access]

- id: f08
  title: 紧凑核心（Compact Core）参考架构模板
  type: framework
  source_chapter: "p314"
  source_quote: |
    "OMNISWITCH COMPACT CORE NETWORK • Key Elements
    • Network virtualized using Virtual Chassis (VC) for simplified two-layer architecture
    • Fully redundant and resilient network
    • Fast re-convergence time on failure
    • UNP for NAC security and QoS
    • Server farm or data center dual home connected directly to network core with LAG"
  summary: |
    中型园区的主流模板：核心层用 OS6870（或 6860N）组 VC 虚拟机箱把三层网压成两层，接入层用 OS6560/E（1/2.5/5G PoE+ 10G 上联），服务器区用 LAG 双归直连核心。
    高配版（p315）核心可换 OS6900、接 OS6860N/6870 做多千兆接入。
    适用"单楼宇或紧凑园区、要冗余但要控制管理点数量"的客户，是中型项目投标的默认起点架构。
  tags: [reference-architecture, core, vc]

- id: f09
  title: 分布式环网参考架构模板（ERPv2 多楼宇环）
  type: framework
  source_chapter: "p316"
  source_quote: |
    "OMNISWITCH 10/40 GIGE DISTRIBUTED RING NETWORK • Key Elements
    • Network virtualized using ERPv2
    • Simplified two-layer architecture
    • Fully redundant and resilient network
    • Fast re-convergence time on failure
    • Dual Home Link (DHL) at the access
    • 10 GigE links from the network core to Server farm or data center"
  summary: |
    多楼宇分布式园区的环网模板：楼宇间用 ERPv2（G.8032，<50ms 收敛）组成光纤环，核心 OS6900，接入 OS6870/6860N/6560E/6360，接入侧再叠 DHL 双归属。
    适用场景是光纤资源呈环形布放（如校园、厂区、轨道交通沿线），铺双路星型光纤成本高的客户。
    与紧凑核心模板的差别就在楼宇互联形态：星型 LAG 换成 ERP 环，其余分层逻辑复用。
  tags: [reference-architecture, ring, erp, campus]

- id: f10
  title: 密集核心（Dense Core）参考架构模板
  type: framework
  source_chapter: "p317"
  source_quote: |
    "OMNISWITCH 10/40/100 GIGE DENSE CORE NETWORK • Keys Elements
    • Very large networks with high concentration of users on certain locations
    • Network virtualized using Virtual Chassis (VC)
    • Widely scalable architecture
    • Dual Home Link (DHL) at the access
    • Reduced management point with VC technology from access to core"
  summary: |
    大型/超大型园区模板：核心 OS9900（10/40/100G）+ 汇聚 OS6900（10/40G）+ 接入 OS6860N 多千兆，VC 技术从接入贯穿到核心以压缩管理点，接入侧 DHL 双归属。
    低配版（p318）核心可降到 OS6900、汇聚用 OS6870。
    判定信号是"用户高度集中于个别楼宇/站点、规模很大"，如总部大楼、大型医院、高校集中区。
  tags: [reference-architecture, core, large-network]

- id: f11
  title: SPB 园区核心参考架构模板
  type: framework
  source_chapter: "p319"
  source_quote: |
    "ENTERPRISE SPB LAN CORE
    MPLS styled service architecture
    VLAN extensibility across campus / No STP / Faster, easier to deploy
    Service Virtualization (ISID) for departmental isolation
    Enabling multi-tenancy on campus sites
    L3 inter-departmental routed control with VPN-lite or L3-VPN
    VXLAN support for DCI"
  summary: |
    以 SPB 为核心的园区模板：核心/汇聚用 6860N/6870/6900/9900 组 SPB 网络，各部门（Admin/Staff/Agent）用 I-SID 做服务虚拟化隔离，跨园区 VLAN 透传，L3 互通走 VPN-lite 或 L3-VPN，数据中心互联再加 VXLAN。
    卖点框架是"MPLS 风格的服务架构但没有 MPLS 的复杂度"，用多租户、部门隔离、无 STP 三个词对抗竞品的 EVPN/VXLAN 方案。
    适用多部门强隔离、多校区、需要租户化的政企/园区客户。
  tags: [reference-architecture, spb, multi-tenancy]

- id: f12
  title: SPB 部署三层角色分工法（Access/BEB/BCB）
  type: framework
  source_chapter: "p100"
  source_quote: |
    "SPB DEPLOYMENT IN LAN NETWORK
    Backbone Core Bridge (BCB) role: Learns BEB addresses, IS-IS SPB for paths, PBB for data plane, L3 routing
    Aggregation – Backbone edge bridge (BEB) role: VLAN to I-SID, IS-IS for MAC learning, IS-IS for SPB paths, PBB for data plane, Loopback Detection Feature
    Access: IEEE 802.1Q VLAN on uplinks (port or LAG), STP towards BEB"
  summary: |
    把 SPB 网络按三种角色分工部署：接入层仍是普通 802.1Q VLAN（上联口或 LAG，向 BEB 跑 STP），汇聚层 BEB 负责 VLAN 到 I-SID 的映射与 MAC 学习，核心层 BCB 只看 BMAC 转发并做 L3 路由。
    这个分工意味着接入层设备无需 SPB 能力（老机型可保留），只在汇聚以上引入 SPB，改造成本可控。
    售前做 SPB 方案时按此角色表逐层指定机型（BEB/BCB 需 SPB 机型，接入任意），即可生成设备分工图。
  tags: [spb, design, roles, deployment]

- id: f13
  title: ERPv2 多环/梯形网络设计规则（主环/子环/RPL 放置）
  type: framework
  source_chapter: "p127"
  source_quote: |
    "ERP & RPL — Different placement of RPL on Master and Sub-ring
    Each ring must have its own RPL
    • The RPL can be placed anywhere on the Master Ring, including the shared links
    • The RPL can be placed anywhere on the Sub Rings, including the "sub-ring" port
    • Since the Sub Ring is not closed using the shared link, the RPL cannot be placed on the shared link"
  summary: |
    ERP 环网的结构化设计规则：网络拆成主环（Major Ring）+ 子环（Sub-Ring），交点设备叫互连节点（Interconnection Node），共享链路（Shared Link）归主环；每个环必须有且只有一个 RPL 阻塞点，且 RPL 不能放在子环共享段上。
    扩展形态有多环并联、链式环、梯形网（同一互连节点挂多个子环，p124/p128），单机最多 64 环、每环建议 16 节点。
    售前拿到光纤路由图后按此规则切环、定 RPL 位置，可直接产出环网设计稿。
  tags: [erp, design, ring, rules]

- id: f14
  title: 网管平台部署模式选型法（本地 OV2500 vs 云 Cirrus）
  type: framework
  source_chapter: "p217"
  source_quote: |
    "OV CIRRUS OVERVIEW — SaaS model
    • Subscription based service
    • Zero Deployment/Zero footprint from Cloud
    • Designed for both Green and Brown field environments
    Full Network Control • Integrated/Unified LAN & WLAN management
    • Currently each OV tenant can support up to 5000 devices / up to 4000 APs"
  summary: |
    ALE 网管按部署模式二分：OmniVista 2500 本地部署（虚拟机、HA 冗余、内嵌 UPAM Radius，见 p188）与 OmniVista Cirrus 云 SaaS（订阅制、零部署零运维、绿色棕色场地皆宜、单租户 5000 设备/4000 AP）。
    选型判据是客户 IT 运维成熟度与数据驻留要求：无机房/无运维团队选 Cirrus，要本地管控/已有虚拟化平台/合规要求数据不出境选 OV2500；大企业另有 Terra。
    Network Advisor（p230）作为独立 AI 运维件不强依赖任一平台，可单独叠加销售。
  tags: [nms, selection, cloud, positioning]

- id: f15
  title: OV Cirrus 订阅三维配置法（License 类型 × 年限 × 服务包）
  type: framework
  source_chapter: "p220"
  source_quote: |
    "OV CIRRUS ORDERING
    License types: Essential, Advanced, Core, Access Points
    Subscription duration: 1, 3 or 5 years
    Service bundles: Base, Premium and Business
    Subscription done through ALE Business Store/CPQ or eBUY/OVCirrus"
  summary: |
    Cirrus 报价按三个维度组合：功能档（Essential/Advanced/Core/Access Points）× 订阅年限（1/3/5 年）× 服务包（Base/Premium/Business），可扩容、缩容、续订。
    另有 Freemium 免费层（自注册、无配置能力、仅库存与一次性升级，p219）作为获客入口。
    售前配置 Cirrus 报价时按"设备类型定 License 档→预算定年限→服务级别定 bundle"三步走，即可生成订阅单。
  tags: [nms, subscription, quotation, cirrus]

- id: f16
  title: OV2500 许可模型三层结构法（设备许可×服务许可×扩展许可）
  type: framework
  source_chapter: "p194"
  source_quote: |
    "OMNIVISTA 2500 NMS - LICENSE TYPES
    • Device Licenses - Manage a specific number of devices.
    Alcatel-Lucent Enterprise Devices / Third Party Devices / OmniAccess Stellar APs
    Starter Pack License is free (OV4-START-NEW)"
  summary: |
    OV2500 报价按三层许可组织：设备许可（按管理设备数，ALE 设备/第三方设备/Stellar AP 各算一类，VC 堆叠按成员数计，p199）；服务许可（VM 数、Guest 设备、BYOD 入网设备、HA、Web 内容过滤，p195）；扩展许可（节点管理/AP 管理/访客/入网分级扩容 SKU，p197）。
    Starter Pack 免费（10 设备）可作 PoC 起步。
    报 OV2500 时先数设备清单定基础许可，再按用到的功能（BYOD/访客/HA）加服务许可行，避免漏报。
  tags: [nms, licensing, quotation, ov2500]

- id: f17
  title: Network Advisor AI 运维三步循环（Identify→Mitigate→Optimize）
  type: framework
  source_chapter: "p240"
  source_quote: |
    "OMNIVISTA NETWORK ADVISOR
    Identify: Detect issues/anomalies & trigger immediate alert. Understand the normal network behavior with Artificial Intelligence & Machine Learning
    Mitigate: Propose a solution & the ability to fix the issue in one tap. Automatic corrective actions for abnormal behavior and cybersecurity threats
    Optimize: Network fine tuning for better quality of experience. Leverage Rainbow CPaaS"
  summary: |
    ALE AI 运维叙事的标准三段式：Identify（AI/ML 学基线、异常即告警）→ Mitigate（一键修复/自动纠正，手机端可操作）→ Optimize（持续调优提升体验，借 Rainbow 协作）。
    配套内容有预置异常清单（网络环、端口抖动、DDoS、VC takeover、CPU/内存高 等 30+ 类，p233）与用户角色（Admin/Support，p235）。
    售前讲 AI 运维故事、做续费加购 pitch 时直接套这三步结构，比罗列功能更有说服力。
  tags: [ai-ops, nms, loop, narrative]

- id: f18
  title: 网络问题生命周期介入框架（四阶段卖点定位）
  type: framework
  source_chapter: "p241"
  source_quote: |
    "WHERE CAN THE ALE OMNIVISTA NETWORK ADVISOR HELP YOU? Network Issues Lifecycle
    1. Facilitate the capture of information / Audit the configuration / Continuous Data Collection
    2. Early Detection / Preventive remediation with Admin Notification
    3. Instantaneous intervention / Minimize impact & side effects
    4. Proactive data collection & Admin Notification / Continuous Data Collection"
  summary: |
    把客户网络问题生命周期（用户报障→伙伴开工单→问题闭环）切成四段，逐段标注 Network Advisor 的介入点：事前审计与持续采集、早期检测与预防性修复、瞬时介入降影响、事后主动取证。
    这是把技术产品翻译成客户运维流程价值的框架，用于应对"我已有网管为什么还要买 Advisor"的异议。
    同样的四段式可以迁移到任何运维类增值服务的售前话术。
  tags: [ai-ops, lifecycle, pitch, objection-handling]

- id: f19
  title: Access Guardian 四环节安全框架
  type: framework
  source_chapter: "p147"
  source_quote: |
    "ACCESS GUARDIAN SECURITY FRAMEWORK
    Authentication: 802.1x, MAC, Captive Portal, RADIUS server
    Classification: UNP profile rules (mobility rules), UNP port default profiles, RADIUS server (UNP)
    Role-Based Access: UNP profiles, QoS policy lists, Captive Portal, BYOD
    Restrict or Block: Restricted roles, Re-authentication, Quarantine, Remediation, filter MAC"
  summary: |
    ALE 准入安全的结构化四环节：认证（802.1x/MAC/Captive Portal/RADIUS）→ 分类（UNP 规则给设备贴档案）→ 基于角色授权（VLAN+ACL+QoS 跟人走）→ 限制或阻断（受限角色、重认证、隔离、补救）。
    每个环节都有对应配置对象，售前做安全方案分册时按四环节展开即可成章。
    也用作竞标应答框架：客户提任何准入需求，先归类到四环节之一再答对应特性。
  tags: [security, access-guardian, framework]

- id: f20
  title: 上下文策略管理公式（用户+设备+情境=策略）
  type: framework
  source_chapter: "p157"
  source_quote: |
    "CONTEXT-BASED POLICY MANAGEMENT FOR WIRED AND WIRELESS DEVICES
    User + Device + Situation = Policy to be enforced
    (Time / Location / Posture / Medium; Limit access / Quarantine / Prioritize / Control BW)
    e.g. Lower priority of all app group social media between 8:30 AM and 4:30 PM"
  summary: |
    一个可迁移的策略思维公式：策略 = 用户身份 + 设备类型 + 情境（时间/位置/姿态/接入介质），输出动作是限制访问/隔离/优先级/带宽控制。
    书中给了五个具体策略例句（工作时间降社交应用优先级、营销部外全员禁发 Facebook、P2P 限 1Mbps 等），证明公式可逐条落地。
    售前收集策略需求时按此公式三问（谁、用什么设备、什么时间地点），即可把客户口语需求转成策略条目。
  tags: [security, policy, formula, requirements]

- id: f21
  title: UNP 两级认证与动态角色模型
  type: framework
  source_chapter: "p152"
  source_quote: |
    "ACCESS GUARDIAN R8 AUTHENTICATION PROCESS
    L2 authentication: 802.1x or MAC authentication or classification. Result of this process is a UNP edge profile
    L3 classification: Based on UNP properties… If validations fail the user is put into a Restricted Role (policy list)
    Initial UNP (which provides the initial policy list and role) and Vlan does not change during the lifetime of the user. Only the roles change dynamically"
  summary: |
    UNP 的分层认证模型：第一级 L2 认证（802.1x/MAC/分类）产出初始 UNP 边缘档案（定 VLAN 和初始策略）；第二级 L3 分类叠加时间/位置/Portal 校验，校验失败落入受限角色。
    关键设计原则是"初始 VLAN 终身不变、只有角色动态变化"，避免用户换角色时掉线重配。
    用于向客户解释 ALE 准入"身份跟着人走、策略随情境变"的机制差异，也是排障时判断用户落在哪个角色的思维地图。
  tags: [security, unp, access, model]

- id: f22
  title: IoT 设备画像与自动处置闭环（采集→分类→强制执行）
  type: framework
  source_chapter: "p164"
  source_quote: |
    "IOT DEVICE PROFILING
    New Endpoint first classified in "a" UNP before profiling/enforcement
    MAC OUI / DHCP fingerprint (i.e. DHCP option 55) / DHCP Vendor-ID (i.e. DHCP option 60) / Up to 5 HTTP User-Agents
    Enforcement Policy Assigns UNP based on the Category
    Network Enforcement: Assign UNP to Endpoint"
  summary: |
    IoT 处置闭环：终端先被临时分类进一个 UNP，画像服务用 MAC OUI、DHCP 指纹（option 55）、厂商 ID（option 60）、HTTP User-Agent 等多维特征识别设备类别，再按"类别→UNP"的强制策略自动下发网络档案（VLAN/ACL/QoS），交换机/AP 更新本地缓存。
    新端点先入临时档案再被处置，保证未知设备既不断网也不放任。
    适用于摄像头、传感器、医疗仪器等哑终端入网治理场景，售前可作为"无 Agent 安全"方案骨架。
  tags: [iot, profiling, automation, security]

- id: f23
  title: iFab 智能织构自动化部署法（Auto-VC→Auto-LACP→Auto-SPB 全链）
  type: framework
  source_chapter: "p135"
  source_quote: |
    "INTELLIGENT FABRIC — Addressing operational challenges: Automated deployment, Plug-n-play deployment, Self-healing network fabric, Preventing configuration errors
    Auto-VC: Automated VC creation / Auto-LACP: LACP Link aggregates creation between neighbors / Auto-SPB Fabric: Automated SPB-M (L2) domains creation / Auto-Routing: L3 routing configuration / Auto-Network Profile / Auto-MVRP: Automated VLAN propagation"
  summary: |
    智能织构是一组自动化能力的叠加链：Auto-VC 自动建堆叠、Auto-LACP 邻居间自动做链路聚合、Auto-SPB 自动建 SPB 域、Auto-Routing 自动配 L3、Auto-Network Profile 自动建档案、Auto-MVRP 自动传播 VLAN。
    演进路线（p134）是 Stacking→Auto VC→Access Fabric→Intelligent Fabric，逐级减少人工配置；8.10R2 起 auto-fabric 默认改为 opt-in（p137），部署时需在启动提示中选择开启或独立模式。
    售前用"开机即成网、自愈织构"叙事打运维人力不足的客户，交付侧则要提醒 opt-in 变更。
  tags: [automation, ifab, deployment, zero-touch]

- id: f24
  title: 应用可视化与管控四步闭环（Enable→Monitor→Enforce→Analyze）
  type: framework
  source_chapter: "p265"
  source_quote: |
    "APPLICATION VISIBILITY
    Application Signature Management: Feature enabled by OV License, Signature update automation, "OneTouch" deployment
    Application Control: Role based enforcement, Dynamically tunable role-based policies, Cohesive workflow for Unified Role-based policies
    Enable / Monitor / Enforce / Analyze & Reports — Business critical apps / Non-compliant apps"
  summary: |
    应用层运营的四步闭环：Enable（签名库订阅、OneTouch 下发）→ Monitor（DPI 实时识别 Top N 应用/用户）→ Enforce（按角色做优先级/限速/阻断）→ Analyze & Report（仪表盘与报表复盘）。
    技术底座是 OS6860N/6870 的硬件 DPI（8K 流/台、VC 64K 流，p268），OV 侧做签名管理与策略编排。
    客户谈"看不见应用流量/关键应用卡顿"时，按这四步给方案路径，从可视化切入再追加管控，是典型的分阶段销售结构。
  tags: [app-visibility, dpi, loop, qos]

- id: f25
  title: WWPL 价格表结构与供货分级框架
  type: framework
  source_chapter: "p326"
  source_quote: |
    "Product Availability: Standard / Extended / Contact
    • Standard: … Average delivery lead-time is two (2) weeks ARO.
    • Extended: … Average delivery lead-time is Four (4) weeks ARO.
    • Contact: Product is announced but not released…
    Sales category designations are A, B, C, D, E, F, G, H, I, J, K, L, M, O, P, Q, S, U, W, Z and NA. Consult your contract or channel partner for actual discount level.
    Service category designations are a combination of two digits."
  summary: |
    ALE 全球价目表（WWPL）的读表框架：价格条目由 Family/Item/Sales Category（折扣级字母）/Service Category（两位数字）/Availability（Standard 2 周、Extended 4 周、Contact 未上市）/List Price 组成（p325-326）。
    售前查价流程：MyPortal 下载当月 WWPL（含 Addendum 促销/新品/EOS 清单，p324）→ 按型号查列表价与折扣级 → 用自己合同折扣算净价 → 标注供货分级避免交期承诺失误。
    投标前必须对最新 WWPL 复核价格与 EOS 状态，是本书反复强调的商务底线。
  tags: [pricing, wwpl, quotation, business]

- id: f26
  title: 下单 BOM 五件套构成法（机型→电源→堆叠/光模块→License）
  type: framework
  source_chapter: "p328"
  source_quote: |
    "OMNISWITCH ORDERING GUIDELINES
    OmniSwitch model / Backup & POE Power-Supply / Stacking Interface, Cables, Transceivers and Accessories / Licenses
    Switch model with "-ZZ" extension have no power cord included… For OS6860N models with "-00" extension PS must be ordered separately"
  summary: |
    每个机型的订单都按四段式构成：整机型号 + 备份/PoE 电源 + 堆叠线缆与光模块等附件 + 软件 License，p329-342 逐机型给出各自的四段清单。
    特别规则：型号后缀 -ZZ 不含电源线、-00 不含电源需单独订购；MACsec License 免费但必须显式下单（OS-SW-MACSEC）。
    售前做 BOM 时按此五件套逐机型过一遍，可系统性避免漏配电源/漏配光模块/漏下免费许可导致交付失败。
  tags: [quotation, bom, ordering, checklist]

- id: f27
  title: 订阅服务报价法（按设备数计许可 + 占网总价约 1.8% 锚点）
  type: framework
  source_chapter: "p246"
  source_quote: |
    "OmniVista Network Advisor Quotation: The quantity of devices reflects the quantity of licenses to order
    For example: your customer has 50 OmniAccess Stellar access points, 42 OmniSwitches and wants to subscribe the service for 1 Year
    (* 1,8% of the total network cost, All are in List Prices)"
  summary: |
    订阅制网管的报价方法：许可数量直接等于受管设备数量（AP/交换机/第三方设备分别计价，1/3/5 年三档，价目见 p244），在硬件 BOM 末尾追加订阅行即可。
    书中给出锚点经验值：Network Advisor 订阅约占网络总成本的 1.8%（按列表价），可用来快速验证报价合理性或向客户定位"不到两个点的保险费"。
    该方法可迁移到一切按设备数订阅的安全/运维服务报价。
  tags: [quotation, subscription, pricing, anchor]

- id: f28
  title: 堆叠产品组合定位矩阵（规模×场景×能力三维定位图）
  type: framework
  source_chapter: "p357"
  source_quote: |
    "POSITIONING IN THE STACKABLE PORTFOLIO
    Gig / Small / Gig w/ 10G / Hardened / Large
    OmniSwitch 2260/2360: Value AOS L2 WebSmart
    OmniSwitch 6360: Value AOS L2+ GE
    OmniSwitch 6560/E: AOS Advanced L3 licensed
    OmniSwitch 6570M: AOS L3+ Metro Ethernet
    OmniSwitch 6860N: Advanced AOS L3 GE
    OmniSwitch 6870: AOS Advanced L3"
  summary: |
    全书反复出现的定位图（p357/p367/p374/p384 同款）：横轴按规模与场景（Gig 小型/Gig+10G/Hardened 工业加固/Large 大型）把堆叠家族逐格安放，纵轴标注各家族的软件档位（L2 WebSmart→L2+→L3 许可制→Advanced L3）。
    用途是快速回答"这个需求该报哪个家族"：小型便宜选 2260/2360/6360，多千兆 Wi-Fi 选 6560E/6860N，Metro 场景 6570M，高规格 6870，加固环境 6465/6865/6575。
    也是向渠道/新人讲产品线的标准教具。
  tags: [portfolio, positioning, matrix, sales-enablement]

- id: f29
  title: 视频监控网络概念设计模板（VMS+交换机+SPB 分层）
  type: framework
  source_chapter: "p465"
  source_quote: |
    "SURVEILLANCE NETWORK CONCEPTUAL DESIGN
    IP CAMERAS / PAN TILT ZOOM CAMERAS / DETECTORS / EDGE STORAGE / 360 CAMERAS / AUDIO
    SMART WALL / SMART CLIENT OPERATIONS / DMZ / FIREWALL / WEB CLIENT / USERS / MANAGEMENT CLIENT / ADMINISTRATION
    MILESTONE VMS & PLUGINS — STORAGE / EVENT / NETWORK MANAGEMENT / SQL SERVERS — SPB"
  summary: |
    视频监控垂直方案的概念模板：前端各类摄像机与探测器经交换机接入，承载网用 SPB 分段隔离，后端接 Milestone VMS（管理/事件/录像/SQL 服务器）与 Smart Wall 大屏，远程访问过 DMZ 防火墙。
    配套 OmniSwitch Milestone 插件可在 VMS 界面内管交换机端口、一键复位摄像头、按摄像头设 PoE 优先级（p463-464），支持的接入机型清单见 p466。
    售前接安防/弱电集成项目时按此模板画图，把网络设备从"哑管道"提升为 VMS 内可运维的组件。
  tags: [vms, surveillance, reference-architecture, vertical]
```
