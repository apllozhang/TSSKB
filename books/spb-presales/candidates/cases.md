# SPB Presales 教材 · 案例提取结果（书中亲自使用的实例）
# 来源：fulltext.md（含页码标记）+ figures_captions.md（插图标注）
# 提取原则：不做筛选、宁多勿漏；引用原文 ≤100 英文词；保留客户规模/设备型号/数字结果

```yaml
- id: c01
  title: Linköping 大学 spine-leaf 改造成功故事
  type: case
  source_chapter: "p115-116"
  source_quote: |
    "Spine & leaf topology after successful SPB implementation.
    Our new campus network is incredibly simple to configure and manage. We can now fully meet user expectations and provide them with additional services. With ALE, we have a partner who helps us succeed.
    David Byers, Head of IT office, Linköping University"
  summary: |
    瑞典 Linköping 大学校园网改造案例。部署 SPB 后全网采用 spine-leaf（脊叶）拓扑。
    客户证言（David Byers，IT 办公室负责人）：新校园网配置和管理极其简单，能完全满足
    用户期望并提供额外服务，ALE 是帮助其成功的伙伴。
    售前弹药点：教育行业标杆 + spine-leaf 成果 + 具名高管证言 + 官方完整故事链接
    （al-enterprise.com/en/company/customers/linkoping-university）。
    注意：书中本案例仅给出成果拓扑与证言，未提供设备型号和规模数字，引用时勿自行补数。
  tags: [education, success-story, spine-leaf, campus, testimonial]

- id: c02
  title: 美国内华达州交通厅 NDOT 路边网络企业级改造
  type: case
  source_chapter: "p117-119"
  source_quote: |
    "Roadside networks need to evolve and become 'enterprise-class':
    Better management tools to facilitate troubleshooting, decrease MTTR.
    Analytics to better understand usage trends.
    Open, standards-based protocols like shortest-path bridging… allows for the elimination of spanning tree, increasing reliability.
    Spanning tree eliminated in favor of SPB. SPB to the edge, Fully Managed from NOC. High flexibility: stacking switches, ample PoE budgets."
  summary: |
    美国内华达州交通厅（NDOT）案例：将公路路边网络升级为"企业级"。
    挑战：排障工具不足导致 MTTR（平均修复时间）高、缺乏使用趋势分析、生成树可靠性差。
    方案架构（三层）：
    1) 网络运营中心 NOC：OmniVista 2500 统一网管，全网从 NOC 集中管理，管理型交换机提供高可见度；
    2) 分配层/光纤交接箱（Distribution/Fiber Hut）：光纤环 + OS6900 做环网聚合、冗余环连接、支持 PoE；
    3) 边缘/加固交换机：温控 NEMA-TS2 交通机柜内部署 OS6860E、OS6865，SPB 延伸到边缘，堆叠灵活、PoE 预算充足；
    核心/数据中心：OS6900 网状拓扑（Core Mesh），承担服务器连接与光纤环聚合。
    量化/关键结果：全面消除生成树改用 SPB，可靠性提升，MTTR 下降。
    配图素材：p118 有交换机产品照与网管界面截图，p121 有高速公路互通立交鸟瞰图。
  tags: [transportation, success-story, usa, harsh-environment, roadside-network, poe, stp-replacement, omnivista-2500]

- id: c03
  title: 法国 Metz 欧洲都会区全网 SPB 改造（背景/挑战/方案/收益）
  type: case
  source_chapter: "p120-124"
  source_quote: |
    "Serves nearly 80 public administrative buildings. The network is made up of 100km of fibre optic cable belonging to the metropolitan authority. Thousands of items of equipment pass through the network: PCs and mobiles on the WLAN network, servers, boiler room automats, swimming pool turnstiles, intruder alarms, etc. 200 switches, 100 APs, ALE supervision and analytics."
  summary: |
    法国大型城市 Metz 欧洲都会区（Metz Eurometropolis）案例，都会区与市政厅共享 IT 服务。
    客户规模（p121）：近 80 栋公共行政建筑；100 km 自有光纤；数千台设备（WLAN 上的 PC/手机、
    服务器、锅炉房自动化装置、游泳池闸机、入侵报警等）；200 台交换机 + 100 台 AP + ALE 监管分析。
    改造前痛点（p122）：大二层数据域过大，10,000 台设备跨越 L2；一对集中式 VRRP 路由器承担全网
    路由；每站点一个 VLAN 策略，上行链路承载全部 VLAN（transit VLAN）；STP 控制冗余拓扑引入的环路。
    改造后（p123）：用 SPB 取代 STP，无环、全链路可用；低时延快速收敛；多站点多租户；不再需要
    transit VLAN（SPB 按服务映射）；核心网交换机全部 SPB 兼容；多个 BVLAN 维持多条活跃路径；
    SPB 用 SPF 算法选最优路径；相邻两环的 BEB 配两个 STP 实例（Root Bridge 与 Next Best Root），
    一条点对点 SPB 服务专门承载 STP 控制。
    量化收益（p124）：迁移全程无业务中断；对既有 L2 服务透明的二层扩展；全链路使用；最短路径；
    IS-IS 自动流量保护与重定向；接入服务只在边缘配置；兼容既有标准。四大主题：优化带宽与稳定性、
    时延与弹性、简化配置与监控、简单低影响迁移。
  tags: [government, smart-city, success-story, france, stp-replacement, multi-tenant, migration]

- id: c04
  title: L3 VPN/VPN-Lite 物理环回口（loopback）配置样例
  type: config
  source_chapter: "p84"
  source_quote: |
    "Loopback ports Configuration example. Configure the L3 VPN loopback ports for VPN-Lite or L3 VPN mechanisms.
    The loopback configuration consists of one port tagged with an IP interface VLAN that belongs to a single VRF instance connected to another port that is assigned to an SPB SAP, to which the VLAN ID associated with the other loopback port is assigned."
  summary: |
    AOS CLI 配置演示：用两根物理环回线缆口实现 L3 VPN / VPN-Lite 的 outline routing。
    机制：一个端口做 SPB access 口（SAP 侧），另一个端口做仅路由的 bridge 口（VRF 侧）。
    支持 AOS 平台（p82）：OS6900-X20、OS6900-X72、OS6900-T20、OS6900-Q32、OS6860/E。
    CLI 关键行（两台 BEB 各一侧）：
    vlan 500; vlan 500 members 1/1/23 tagged; spb bvlan 4001;
    service access port 1/1/24; service spb 10 isid 1000 bvlan 4001 admin-state enable;
    service spb 10 sap port 1/1/24:500; vrf create 1;
    vrf 1 ip interface L3vpn1 vlan 500 address 10.5.1.1/24（对端 10.5.1.2/24，端口对 1/1/11↔1/1/12）。
    演示拓扑：ISID-1000 承载，VRF 1 内网 192.168.1.0/24、192.168.2.0/24 与 192.168.3.0/24、192.168.4.0/24 互通。
  tags: [config-sample, cli, l3vpn, vpn-lite, loopback, vrf, isid, os6900]

- id: c05
  title: VPN-Lite outline routing 静态路由 + OSPF 配置样例
  type: config
  source_chapter: "p87"
  source_quote: |
    "vrf 1 ip interface L3vpn1 address 10.5.1.1/24 vlan 500
    vrf 1 ip static-route 192.168.3.0/24 gateway 10.5.1.2
    vrf 1 ip load ospf
    vrf 1 ip ospf interface L3vpn1 admin-state enable
    vrf 1 ip ospf area 0.0.0.0
    vrf 1 ip ospf admin-state enable"
  summary: |
    AOS CLI 配置演示：VPN-Lite（L2 SPB 骨干上跑 L3 流量）的静态路由与 OSPF 动态路由两种写法。
    静态路由示例：vrf 1 ip static-route 192.168.1.0/24（及 192.168.2.0/24）gateway 指向对端 10.5.1.1；
    动态路由示例：vrf 1 ip load ospf，接口 L3vpn1/L3vpn2 使能，area 0.0.0.0，进程 admin-state enable。
    场景：两个 VRF 通过 ISID-1000 跨 SPB 骨干互联，SPB 充当物理媒质；配合 p88 的配置准则
    （每 VRF 一个 IP 接口绑定专用 VLAN、两个 VRF 不能共享同一 ISID、VRRP hello 可跨 PBB 网络发送实现双 BEB 冗余网关）。
  tags: [config-sample, cli, vpn-lite, ospf, static-route, vrf, spb-backbone]

- id: c06
  title: 前面板端口内联路由配置样例（VPN-Lite 与 L3 VPN，免物理环回线）
  type: config
  source_chapter: "p93-94"
  source_quote: |
    "interfaces port 1/1/18 loopback
    service access port 1/1/18 vlan-xlation enable
    service 10 sap port 1/1/18:200
    ip interface L3vpn1 address 10.5.1.1/24 rtr-port port 1/1/18 tagged vlan 200
    spb ipvpn bind vrf 1 isid 1000 gateway 10.5.1.1 all-routes
    vrf 1 ip export all-routes
    vrf 1 ip import isid 1000 all-routes"
  summary: |
    AOS CLI 配置演示：前面板端口（或静态链路聚合）配置为 loopback 模式，无需外部环回线缆。
    VPN-Lite 版（p93）：interfaces port 1/1/18 loopback + vlan-xlation enable，
    service 10 sap port 1/1/18:200，ip/ipv6 interface 以 rtr-port 方式绑定同一端口 tagged vlan 200，
    静态路由与 OSPF 同 c05；支持 OS6900-V72、OS6900-C32。
    L3 VPN 版（p94）：在相同端口配置上增加 spb ipvpn bind vrf 1 isid 1000 gateway 10.5.1.1 all-routes，
    vrf 1 ip export all-routes + vrf 1 ip import isid 1000 all-routes（路由经 ISIS TLV 跨 SPB 域交互）；
    IPv6 示例地址 2001:db8:10::1/64。
  tags: [config-sample, cli, front-panel, inline-routing, vpn-lite, l3vpn, os6900-v72, os6900-c32]

- id: c07
  title: 基于服务的内联路由配置样例（单遍 inline，免专用端口）
  type: config
  source_chapter: "p96-97"
  source_quote: |
    "vrf 1 ip interface L3vpn1 address 10.5.1.1/24 service 10
    spb ipvpn bind vrf 1 isid 1000 gateway 10.5.1.1 all-routes
    vrf 1 ip export all-routes
    vrf 1 ip import isid 1000 all-routes"
  summary: |
    AOS CLI 配置演示：软件定义的 IP 服务接口直接绑定 SPB 服务（service 10），单遍内联路由，
    既不要物理环回线缆也不占用专用前面板口。
    VPN-Lite 版（p96）：vrf 1 ip interface L3vpn2 address 10.5.1.2/24 service 10，配合静态路由或 OSPF；
    L3 VPN 版（p97）：spb ipvpn bind vrf 1 isid 1000 gateway … all-routes + export/import。
    支持平台（p95）：OS6860N、OS6870、OS6900-X/T24C2、X/T48C6、X48C4E、C32E、V48C8、OS9900
    （配图设备 OS6900-X48C4E、OS9900）；IPv4 与 IPv6 接口可绑同一 SPB 服务（须同一 VRF 实例）。
  tags: [config-sample, cli, service-based-inline-routing, vpn-lite, l3vpn, ipv6, os9900]

- id: c08
  title: 行业用例矩阵：视频监控/赌场/园区/ITS/数据中心/铁路/城域各自适合的技术
  type: matrix
  source_chapter: "p138"
  source_quote: |
    "Video Surveillance: Scale < 1,000; Virtual-chassis; Staff with video expertise; Multicast → SPB – simplicity.
    Casino – video & operations: Scale < 1,000; Virtual-chassis; Staff with video expertise; Multicast → SPB – simplicity.
    Campus Network: Scale < 1,000; Virtual-chassis; Staff with broad responsibility (LAN, WLAN, FW) → SPB - simplicity.
    ITS Network: Staff with broad responsibility; Outdoor deployments → SPB – simplicity, ruggedized equipment.
    Large-data center: Scalability → EVPN. Rail, E&U: Very low convergence-times → IP-MPLS.
    MANs/Smart City: Scalability; Traffic Control → SPB/IP-MPLS* (* When IP-MPLS is mandatory in the tender)"
  summary: |
    售前选型矩阵（Use Case Examples），按市场给关键技术建议：
    1) 视频监控：规模 <1000、虚拟机箱、团队懂视频、有组播需求 → SPB（赢在简单）；
    2) 赌场（视频+运营）：同上条件 → SPB；
    3) 园区网：规模 <1000、虚拟机箱、团队职责覆盖 LAN/WLAN/防火墙 → SPB；
    4) ITS 智能交通网：职责广的团队、室外部署 → SPB（简单性 + 加固型设备）；
    5) 大型数据中心：诉求是可扩展性 → EVPN；
    6) 铁路与电力/公用事业（E&U）：要求极低收敛时间 → IP-MPLS；
    7) 城域网/智慧城市：可扩展 + 流量控制 → SPB 或 IP-MPLS（标书强制 MPLS 时选 IP-MPLS）。
    售前用法：客户行业 + 运维团队画像（专才 vs 全才）+ 规模阈值 1000 是选型三要素。
  tags: [industry-matrix, use-case, spb, evpn, mpls, video-surveillance, casino, campus, its, datacenter, rail, smart-city]

- id: c09
  title: SPB vs EVPN vs MPLS 定位对比矩阵
  type: matrix
  source_chapter: "p134"
  source_quote: |
    "Main use case: SPB – Datacenter, Campus, IoT Networks; EVPN – Datacenter; MPLS – Service Provider & Mission critical networks.
    Scalability: SPB Large; EVPN Large/Very large; MPLS Large/Very large.
    Ease of deployment: SPB Simple to Moderate; EVPN/MPLS Moderate to complex.
    Training needed: SPB Low to Moderate; EVPN Moderate to High; MPLS High.
    Protocol Overhead: SPB Low (IS-IS only); EVPN Moderate (BGP & VXLAN/MPLS); MPLS High (LDP, RSVP, BGP).
    Troubleshooting: SPB Simple & Fast; EVPN Intermediate time; MPLS Complex & Slow."
  summary: |
    三技术定位总结表（EVPN, SPB & MPLS – Positioning Summary），横向 7 个维度：
    主用例（SPB=数据中心/园区/IoT 网；EVPN=数据中心；MPLS=运营商与任务关键网）、
    可扩展性、弹性（SPB 高、EVPN 高、MPLS 极高）、部署难度、培训成本、协议开销、排障难度。
    核心话术：SPB 部署简单到中等、培训低到中、协议开销低（仅 IS-IS）、排障简单快速；
    MPLS 弹性最高但复杂度、培训、开销、排障成本都最高；EVPN 居中，主打数据中心。
  tags: [comparison-matrix, positioning, spb, evpn, mpls, is-is, tco]

- id: c10
  title: MPLS+SPB 混合 Fabric 样例架构（双数据中心 + 主园区 + 分支）
  type: architecture
  source_chapter: "p136"
  source_quote: |
    "MPLS: Highly scalable, Core, backbone, Convergence: 50 ms, Complex, Cost: $$$.
    SPB: Scalable, Access, core, backbone, Convergence: 100 ms, Cost: $$.
    Mission critical support for harsh environments. High availability in every type of environment."
  summary: |
    样例架构图（Sample Architectures 章节）：一张图同时给出技术参数与设备清单。
    量化对比：MPLS 收敛 50 ms、复杂、成本 $$$，用于核心/骨干；SPB 收敛 100 ms、成本 $$，
    覆盖接入/核心/骨干。
    拓扑组成：主园区（OS6900、OS6860、OS6560）；主数据中心与灾备数据中心
    （Primary/Secondary DC：OS9900、OS6900、OS6860、OS6865，配套 OmniVista 网管、OXE 语音交换
    PBX、NSP、VM/存储）；分支站点（Branch）；骨干 SPB+MPLS 混合承载，面向恶劣环境的任务关键支持。
  tags: [reference-architecture, mpls, spb, dual-datacenter, campus, branch, os9900, oxe]

- id: c11
  title: EVPN-VXLAN Fabric 样例架构（EVI/ESI/DF 多归属演示）
  type: architecture
  source_chapter: "p137"
  source_quote: |
    "EVI 1: VNI 100. EVI 2: VNI 200. EVI 3: VNI 300/400.
    ESI: Ethernet Segment Identifier. Globally significant / Auto vs Manual. Single-homed segments have ESI=0 (as per RFC).
    DF: Designated Forwarder. Election based on algorithm. AA: All-active: To all attached PE. SA: Single-active: to single PE (DF).
    IRB: Integrated Routing and Bridging interface. Connected between Layer 2 domain and IP-VRF."
  summary: |
    EVPN-VXLAN Fabric 样例架构图：4 台 PE（PE-1~PE-4）+ CE 与 VM（VLAN 100~400），
    三层 EVI 对应 VNI 100/200/300-400；LAG 与 ESI（xxxx/yyyy）做多归属，DF/nDF 选举按 EVI 分担；
    单归属段 ESI=0（遵循 RFC）；MH-AA（全活，单播与 BUM 到所有 PE）与 MH-SA（单活）两种转发模式；
    MAC-VRF 绑 L2VNI、IP-VRF 绑 L3VNI、IRB 连接二层域与 IP-VRF。
    售前用法：向数据中心客户展示 ALE 的 EVPN 能力与 SPB（c09/c10）形成完整组合。
  tags: [reference-architecture, evpn, vxlan, esi, df, multi-homing, irb, datacenter]

- id: c12
  title: OmniVista 2500 SPB 服务开通全流程演示（GUI）
  type: config
  source_chapter: "p100-112"
  source_quote: |
    "OneTouch Mode. Services Configuration: Used to view, configure, create services on network devices. Switches must first be selected on the Global Settings Screen before you can view and configure SPB services on those switches. L2 Profiles: Used to configure Layer 2 Profiles, which can be associated with an SPB Service Access Point (SAP)."
  summary: |
    OmniVista 2500 的 SPB Provisioning 应用操作演示（书内含成套界面截图，见 figures_captions p104-112）。
    演示路径：Global Settings 选交换机 → 服务配置主界面（字段：Tunnel ID、Service ID、BVLAN、
    Mcast Mode=Headend/Tandem、VLAN Translation、Remove Ingress、Stats、Router Interface、
    VPN MTU 默认 1500、Port Isolation）→ 服务创建向导（Basic 选/加设备 → UNP Profiling 可选 →
    Advanced 按需）→ L2 Profile 创建（控制帧处理：STP 默认 Tunnel、802.1X 默认 Drop、
    802.3AD/LACP 默认 Peer，另有 Tunnel/Drop/Peer 三模式选择界面）→ 服务监控（设备/SAP/SDP 三级
    信息表，SDP ID 由 OmniVista 动态生成）→ Unified Access > Unified Profile > Template > SPB Profile
    创建（SPB Profile Name、Tag Value、ISID 有效范围 256-16777214、BVLAN、VLAN Translation、
    Multicast Mode）→ 服务端口信息与 SPB 网络拓扑视图（含 LACP 链路明细表、SDP/SAP 状态）。
    售前话术：边缘只配一次、核心零触碰（No-touch core），GUI 全流程可视化。
  tags: [config-sample, gui, omnivista-2500, provisioning, spb-profile, sap, sdp, l2-profile]

- id: c13
  title: AOS SPB 平台规格矩阵（BVLAN/I-SID/SAP 上限，按交换机型号）
  type: spec
  source_chapter: "p75"
  source_quote: |
    "Maximum number of BVLANs: 16 (4 is recommended). Maximum number of IS-IS adjacencies: 70 (OS6860/6865) / 128 (OS6900, OS9900). Maximum number of I-SIDs: 2K (OS6860, OS6860N, OS6865, OS6900-X/T24C2) / 8K (OS6900 X/T48C6, X48C4E, V48C8, C32E) / 1K (OS9900). Maximum number of SAPs: 2K / 8K. Please refer to latest « AOS Specifications Guide » for up-to-date figures"
  summary: |
    AOS SPB 网络规格表（按型号）：OS6860、OS6860N、OS6865、OS6900（V72/C32 与 X/T24C2、
    X/T48C6、X48C4E、V48C8、C32E 等子型号）、OS9900。
    关键数字：BVLAN 上限 16（推荐只用 4）；IS-IS 邻接数与接口数：OS6860/6865 为 70，OS6900 与
    OS9900 为 128；ECT 算法 16 个（可任选 1-16 分配给 BVLAN）；I-SID 上限：OS6860/6860N/6865 及
    OS6900-X/T24C2 为 2K，OS6900 其他子型号 8K，OS9900 为 1K；每 ISID 的 VLAN/SVLAN 数 2K~4K；
    SAP 上限 2K（OS6860 系列）~8K（OS6900）。
    L3 能力（IP over SPBM）：IPv4 VPN-Lite 与 L3 VPN 均支持，VRF-to-ISID 映射（一对一/一对多），
    各型号路由方式见_outline/inline 列。
    注意书末提示：数字以最新《AOS Specifications Guide》为准。
  tags: [spec-matrix, scalability, bvlan, isid, sap, isis, os6860, os6900, os9900, l3vpn]

- id: c14
  title: OmniFabric 各 OmniSwitch 型号技术支持矩阵（SPB/VxLAN EVPN/MPLS）
  type: matrix
  source_chapter: "p139"
  source_quote: |
    "* Supported starting with 8.10 R3/R4. ** HW ready.
    OmniSwitch 6860E: SPB P, VxLAN/VxLAN EVPN O, MPLS O. OmniSwitch 6570M: SPB O**, VxLAN O, MPLS O.
    OmniSwitch 6860N: SPB P, VxLAN P/O, MPLS P. OmniSwitch 6870: SPB P, VxLAN P/P*, MPLS O**.
    OmniSwitch 6900: SPB P, VxLAN P/P, MPLS P. OmniSwitch 9900: SPB P, VxLAN P*/P*, MPLS O**"
  summary: |
    OmniFabric 支持矩阵：每种 OmniSwitch 型号对 SPB、VxLAN/VxLAN EVPN、MPLS 三种 fabric 技术的
    支持等级（P=平台级支持，O=可选/需授权，P*=8.10 R3/R4 起支持，O**=硬件就绪 HW ready）。
    型号覆盖：OmniSwitch 6860E、6570M、6860N、6870、6900、9900。
    要点：OS6900 三项全 P（最全）；OS6860N 与 OS6900 的 MPLS 为 P；6870 与 9900 的 VxLAN EVPN
    自 8.10 R3/R4 起平台支持；6860E 的 SPB 为 P 而 VxLAN/MPLS 为 O。
    售前用法：按客户 BoM 选型时快速核对三技术可用性，避免许诺不支持组合。
  tags: [support-matrix, omnifabric, spb, vxlan, evpn, mpls, os6860e, os6570m, os6860n, os6870, os6900, os9900]

- id: c15
  title: 校园动态弹性微分段演示场景（STEM 项目驱动服务伸缩）
  type: scenario
  source_chapter: "p15-17"
  source_quote: |
    "Stadium, Dormitory, Library, STEM Lab, Faculty, Student, STEM PROJECT.
    Services stretch and contract as needed. Policy and identity driven. Reduced attack surface."
  summary: |
    书中"Why SPB"章节连续三页（p15-17）用同一校园场景演示 SPB 的动态弹性：
    场景元素包括体育场（Stadium）、宿舍（Dormitory）、图书馆（Library）、STEM 实验室（STEM Lab）、
    教职工（Faculty）、学生（Student）；一个 STEM 项目（STEM PROJECT）临时把跨楼宇的成员拉进同一
    专用服务，项目结束服务自动收缩。
    卖点三连：服务按需伸展与收缩（Services stretch and contract as needed）、策略与身份驱动
    （Policy and identity driven）、攻击面收敛（Reduced attack surface）。
    售前用法：面向教育/园区客户讲"零信任微分段"时的入门故事脚本；p11 另配 YouTube 演示视频
    （youtu.be/IttOgoATWpY，主题 macro/micro-segmentation、认证-分类-供给三步）。
  tags: [scenario, campus, education, elasticity, micro-segmentation, zero-trust, stem-project]
```
