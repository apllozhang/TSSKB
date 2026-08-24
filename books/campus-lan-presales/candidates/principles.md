# Campus LAN Presales Ed29 — 原则/清单/规则/常数候选（principles）
# 来源：source/fulltext.md（480 页全书）+ figures_captions.md
# 每条 source_chapter 填主要页码；跨页引用在 quote 内以 (pXXX) 标注。

```yaml
- id: p01
  title: 网络设计流程的九项目标与考量清单
  type: principle
  source_chapter: "p287"
  source_quote: |
    "NETWORK DESIGN PROCESS GOALS AND CONSIDERATIONS
    • Scalability • Adaptability • Reliability • Cost / ROI • Predictability
    • Ease of Implementation • Manageability • Business / Application Growth
    • Troubleshooting"
  summary: |
    售前做校园网方案设计时的目标自检清单，共 9 项：可扩展性、适应性、可靠性、
    成本/投资回报、可预测性、实施容易度、可管理性、业务/应用增长、故障排查。
    应标书"设计目标"章节与方案评审时逐项对照。
  tags: [design, checklist, presales]

- id: p02
  title: 按网络层级选机型的规则（接入/汇聚/核心/数据中心）
  type: principle
  source_chapter: "p300"
  source_quote: |
    "OMNISWITCH SELECTION NETWORK LAYER BASED
    Model Layer: OS6360 OS6465 OS6560/E OS6570M OS6575 OS6860N OS6870 OS6900 OS9900
    User Access:  Yes  Yes  Yes  Yes  Yes  Yes  Yes  No   Yes
    Distribution: No   No   Yes  Yes  Yes  Yes  Yes  Yes  Yes
    Core:         No   No   No   No   No   Yes  Yes  Yes  Yes
    Data Center:  No   No   No   No   No   Yes  Yes  Yes  Yes
    Switch model utilization per infrastructure layer"
  summary: |
    机型定位铁律：接入层除 OS6900 外全系可用；汇聚层从 OS6560/E、OS6570M、
    OS6575 起步（6360/6465 只能做接入）；核心层与数据中心只有 OS6860N、
    OS6870、OS6900、OS9900 四个系列可放。OS9900 虽可做用户接入（配 GNI 板），
    但 OS6900 定位纯汇聚/核心，不做用户接入。
  tags: [model, positioning, design]

- id: p03
  title: 机型功能支持矩阵（VC/ISSU/热插拔电源/SPB/DHL/ERP/MPLS/远程VC）
  type: principle
  source_chapter: "p301"
  source_quote: |
    "列序: OS2260 / OS2360-24/48 / OS6360-10 / OS6360-24/48 / OS6465 / OS6560E / OS6570M / OS6860N / OS6870 / OS6900 / OS9900
    Virtual Chassis: No Yes Yes Yes Yes Yes Yes Yes Yes Yes Yes
    ISSU: No No Yes Yes No No Yes Yes Yes Yes Yes
    Hot swap power supply: No No No Yes Yes No Yes Yes Yes Yes Yes
    SPB: No No No No No Yes** Yes** Yes Yes Yes Yes
    MPLS: No No No No No No No Yes** Yes** Yes** No
    * Roadmap  ** License based feature"
  summary: |
    全系功能对照（**=需许可）：VC 除 OS2260 外全系支持；ISSU 仅 6360-10、
    6360-24/48、6570M、6860N、6870、6900、9900；热插拔电源仅 6360-24/48、6465、
    6570M 及以上高端（6560/E 标 No）；SPB 从 6560/E（许可）与 6570M（许可）起步；
    MPLS 仅 6860N/6870/6900 需许可支持——注意本表 9900 的 MPLS 标 No，与 p443
    "9907 支持 MPLS"的描述矛盾，报价前需按最新 datasheet 核实。DHL 行：
    6570M/6900/9900 标 No，其余 Yes（与 p54 "除 9900 全支持"亦有出入）。
    ERPv2 除 OS2260 外全系支持；高级 L3/VRF 从 6560/E(许可)、6570M(许可)起步；
    Metro 仅 6465/6560E/6570M 及以上。
  tags: [model, feature-matrix, vc, issu, spb, mpls]

- id: p04
  title: 六大中高端机型容量常数对比（Mpps/交换容量/MAC表/路由表）
  type: principle
  source_chapter: "p302"
  source_quote: |
    "列序: OS6360 / OS6465 / OS6560E / OS6570M / OS6860N / OS6870
    Switching: 208 Mpps | 131 Mpps | 241 Mpps | 210 Mpps | 758.9 Mpps | 1,488 Mpps
    Fabric Capacity: 140 Gb/s | 176 Gb/s | 324 Gb/s | 60/168 Gb/s | 1,020 Gb/s | 2,000 Gb/s
    Mac Table: 16K | 16K | 16K | 32K | 64K | 128K
    Routing Table: 64 routes | 32 routes | 2K | 16K | 144K | 312K"
  summary: |
    校园设计选型核心背参数（列序 OS6360/6465/6560E/6570M/6860N/6870）：
    包转发 208/131/241/210/758.9/1488 Mpps；交换容量 140/176/324/60或168/
    1020/2000 Gb/s；MAC 表 16K/16K/16K/32K/64K/128K；路由表 64/32/2K/16K/
    144K/312K。注意 p27 旧版对比表数值略低（6465 为 95.3Mpps/128Gb/s、
    6560E 208Mpps/240Gb/s、6570M 125Mpps），以 p302 较新数据为准。
  tags: [model, capacity, comparison]

- id: p05
  title: 入门级 OS2260/OS2360 对比常数
  type: principle
  source_chapter: "p26"
  source_quote: |
    "OS2260 vs OS2360
    Stacking: No | Yes
    Uplinks: 1 Gbps | 1/10 Gbps
    Switching: 80.4 Mpps | 133.9 Mpps
    Fabric Capacity: 216 Gb/s | 216 Gb/s
    Mac Table: 16K | 16K
    Routing Table: 2 Static entries | 32 Static entries"
  summary: |
    WebSmart 双子对比：两者同为 L2+静态路由、216Gb/s 容量、16K MAC、802.3at；
    差异在 2360 可堆叠（10G 堆叠口）、上联可到 10G、转发 133.9 vs 80.4 Mpps、
    静态路由 32 vs 2 条；2260 无堆叠、无 10G 上联、无备份电源。两者均不在
    美国销售（NOTE: Not sold in the USA）。
  tags: [model, capacity, comparison, entry]

- id: p06
  title: 高端四机型容量常数对比（6860N/6870/6900/9900）
  type: principle
  source_chapter: "p28"
  source_quote: |
    "列序: OS6860N / OS6870 / OS6900 / OS9900
    Switching: 758.9 Mpps | 1488 Mpps | 2000 Mpps | 15118/30950 Mpps
    Fabric Capacity: 1,120 Gb/s | 2,000 Gb/s | 6.4 Tb/s | 25.6/51.2 Tb/s
    Mac Table: 64K | 128K | 228K | 128K
    Routing Table: 144K | 116K | 128K | 128K
    Stacking: 100 Gbps | 100/200 Gbps | 10/40/100 Gbps | 2x40 or 4x100 Gbps links"
  summary: |
    高端容量背参数：6860N 758.9Mpps/1.12Tb/s/64K MAC/144K 路由；6870
    1488Mpps/2Tb/s/128K/116K；6900 2000Mpps/6.4Tb/s/228K/128K；9900
    15118(9907)/30950(9912) Mpps、25.6/51.2 Tb/s、128K/128K。四者均支持
    VC/SPB-M/VXLAN/MACsec 与全 IP 组播路由；6870 额外有 MACsec 与 100/200G
    堆叠。
  tags: [model, capacity, comparison, high-end]

- id: p07
  title: 各机型虚拟机箱（VC）最大台数规则
  type: principle
  source_chapter: "p59"
  source_quote: |
    "STACKING / VIRTUAL CHASSIS TOPOLOGIES
    8 x OmniSwitch [6465] T/P6/P12/P28 models
    4 x OS6465
    6 x OS6900-X/T/V/C
    2 x OS9907
    10/P10 models [excluded]
    4 x OS6360
    OS6360 (except 10 ports model) OS6560/E OS6860E* OS6865* OS6570M OS6860N OS6870
    * can be mixed in same VC
    P12/U28 models
    4 x OS6575
    2 x OS6920"
  summary: |
    VC 台数规则：OS6900 家族最多 6 台（mesh）；OS9907 双机 VC；OS6360 的
    24/48 口型最多 4 台（10/P10 型不做 VC）；OS6570M 最多 8 台（8.9R4 起，
    见 p38）；OS6575 的 P12/U28 型 4 台；OS6920 初始版本 2 台（p439 路标
    到 4 台）；6560/E、6860E、6865、6570M、6860N、6870 等常规家族最多
    8 台环形（p76）；6860/6860E/6865 可在同一 VC 内混插。注意 p59 对 6465
    家族同时出现 8 台与 4 台两种标注，与 p22 "最多 4 台"不一致，需按
    datasheet 核实。VC 本身不需要 license（p58 No license needed）。
  tags: [vc, model, stacking]

- id: p08
  title: VFL 链路规则（成员口数、速率不混、家族混插限制）
  type: principle
  source_chapter: "p60"
  source_quote: |
    "• VFL trunk are comprised of up to 16 member ports according to the model
    • VFL link speeds MAY not be mixed
    (p61) No mix between 6860N and 6870
    (p62) OS9900: Up to 16 VFL member ports for 10Gbps ... QSFP ports on CMM with 40G-to-10G splitter cable ... for 100Gbps QSFP28 ports on CMM2
    (p63) OS6920-D32: up to 8 VFL member ports, 50/100/200/400 Gbps QSFP-DD"
  summary: |
    VFL（机箱互联）规则：单个 VFL trunk 按机型最多 16 个成员口；同一 VFL
    内不同链路速率不可混用；6860N 与 6870 不能组成同一 VC；6860E/6860/
    6865 可混。9900 的 VFL：10G 用 CMM 的 QSFP 40G→10G 分支线（最多 16 口）
    或 XNI-U24/48；40G 用 XNI-UP24Q2/CNI-U8/U20 或 CMM QSFP；100G 用 CMM2
    QSFP28。6900 家族 VFL 可跑 10/25/40/100G（原生口或 splitter），最多
    16 成员口；OS6920-D32 最多 8 个 VFL 成员口，速率 50/100/200/400G。
  tags: [vc, vfl, stacking]

- id: p09
  title: VC 两大阵营差异与默认 VFL 端口号规则
  type: principle
  source_chapter: "p76"
  source_quote: |
    "Static chassis-id assignment (mandatory for 9900) Chassis-id has to be configured through the vcsetup.cfg in every unit trying to form a VC.
    Automatic chassis-id assignment (Auto-VC / VFL mode Auto)
    • VC of 2 (9900), 3 up to 6 in mesh configuration (6900)
    VC of 2, 3 up to 8 in ring topology (on dedicated VFL ports only)
    (p77) On models without EMP port, you must add a dedicated USB to Ethernet converter, supported models are ASIX 8817 interface and RealTek RTL8153.
    OS6560/E: dedicated VFL ports, or ports 29-30 for 24 ports model, ports 53-54 for 48 ports model
    OS6465: ports 27-28 for OS6465-P28
    OS6360: ports 11/12 (10 port models), 27/28 (24 ports models) or 51/52 (48 ports models)"
  summary: |
    9900/6900 阵营：chassis-id 必须静态配置（每台 vcsetup.cfg）；6900 支持
    Auto 模式（默认取每台最后 5 口，p77）；拓扑 9900 双机、6900 2-6 台 mesh。
    其他阵营（6360/6465/6560E/6570M/6860N/6865/6870）：自动分配 chassis-id，
    2-8 台环形、仅限专用 VFL 口。VC 属基础软件（8.3.1.R02 前需 license）。
    无 EMP 口机型（6360/6560 等）做带外管理/RCD 须加 USB-Ethernet 转换器
    （支持 ASIX 8817 与 RealTek RTL8153 芯片）。默认 VFL 端口号：6560/E
    24 口型 29-30、48 口型 53-54；6465-P28 为 27/28；6360 为 11/12（10 口型）、
    27/28（24 口型）、51/52（48 口型）；6870 默认 2 个 QSFP28/56 VFL 可改；
    6570M 为 2 个专用 10G SFP+。
  tags: [vc, vfl, emp, configuration]

- id: p10
  title: 虚拟机箱主/从选举优先级顺序
  type: principle
  source_chapter: "p66"
  source_quote: |
    "Master/Slave election based on virtual chassis protocol (ISIS-VC)
    Highest chassis priority value
    Longest chassis uptime (if difference in uptime >10 mn)
    Smallest Chassis ID value
    Smallest chassis MAC address"
  summary: |
    VC 主从选举四级判据依次比较：①chassis 优先级最高者当选；②开机时长最长者
    （仅当差值超过 10 分钟才比这项）；③chassis ID 数值最小者；④chassis MAC
    地址最小者。master 重启或故障时 slave 本地基于已知伙伴信息重选，新 master
    确认后接管（p68）。
  tags: [vc, election, ha]

- id: p11
  title: VC 脑裂（Split Chassis）检测与保护机制
  type: principle
  source_chapter: "p71"
  source_quote: |
    "• Failures on VFL links cause potential MAC/IP duplication
    • 2 mechanisms
    • Out of Band: EMP Remote Chassis Detection (RCD)
    • In Band: VC Split Protocol
    (p72) RCD use the following IP addresses in order of preference 1. CMM IP address stored in NVRAM (if configured) 2. Chassis EMP IP address
    (p73) Every VC member switch recommended to have one port as part of the VCSP LAG to the helper device
    (p74) One sub-VC assumes 'MASTER' status & other 'Protection' status ... Shuts off all user ports (LAG and VFL ports are up)"
  summary: |
    VFL 断链会导致 MAC/IP 重复，两套防脑裂机制：①带外——EMP 口上常驻的 RCD
    协议（每台收发公告；RCD 选址顺序：先 NVRAM 中配置的 CMM IP，其次 chassis
    EMP IP；无 EMP 口机型需 USB-Ethernet 转换器）；②带内——专有 VC Split
    Protocol（VCSP），需一台上游/下游 helper 交换机，建议每台 VC 成员出一个
    口加入去 helper 的 VCSP LAG（静态或动态 LAG 均可）。检测到分裂后：含原
    master 的子 VC 保持 MASTER，另一子 VC 自动进 Protection 模式并关闭全部
    用户口（仅保留 LAG 与 VFL 口），避免重复 MAC/IP。
  tags: [vc, split-protection, ha, rcd]

- id: p12
  title: auto-fabric 自 8.10R2 起改为选择启用（opt-in）
  type: principle
  source_chapter: "p137"
  source_quote: |
    "Prompt to disable auto-fabric during the boot sequence giving user 10s to decide
    Auto-VC, RCL and auto-fabric are enabled
    input is [Y] (default)
    input is [N] RCL and auto-fabric are disabled
    Starting with 8.10R2 auto-fabric is opt-in !!"
  summary: |
    首次开机/重启时提示 10 秒决定是否关闭自动配置；输入 Y（默认）启用
    Auto-VC、RCL 与 auto-fabric，输入 N 则关闭 RCL 与 auto-fabric。重要变更：
    从 8.10R2 起 auto-fabric 由默认开启改为 opt-in（需显式启用），升级部署
    与开局脚本要注意该行为变化。
  tags: [ifab, auto-configuration, aos-release]

- id: p13
  title: DHL（双归属链路主主）配置规则
  type: principle
  source_chapter: "p54"
  source_quote: |
    "• Dual Home Link Active-Active • AOS based feature • High availability feature
    • Fast failover between core and access switches without using Spanning tree
    • DHL managed only an access switch
    • Configurable on regular switch ports and on link aggregation ports
    • Two DHL links are both active
    • Available on all OmniSwitch models, except OmniSwitch 9900
    (p55) • One session per switch is allowed
    • Two DHL links associated with the session (link A and link B)
    • DHL Active-Active splits a number of VLANs between two active links"
  summary: |
    DHL 规则：AOS 软件特性；只作用于接入交换机（双上行到两台核心/汇聚）；
    可配在普通端口或链路聚合口上；两条 DHL 链路同时活跃，按 VLAN 拆分到
    Link A / Link B 负载分担，故障时修改各 VLAN 转发状态实现快速切换，
    全程不用生成树。限制：每台交换机只允许 1 个 DHL 会话、每个会话恰好
    2 条链路。可用机型：除 OS9900 外全部 OmniSwitch（p301 矩阵中 6570M、
    6900 亦标 No，选型时以机型表为准）。
  tags: [dhl, ha, access]

- id: p14
  title: DHL 环路风险与接入侧防环三件套
  type: principle
  source_chapter: "p56"
  source_quote: |
    "• Link between uplink device other than core network is not advisable as it will create loop
    • Solution on Access switches
    • LPS, Loop Guard, BPDU Shutdown"
  summary: |
    DHL 部署中，两台上行设备之间除核心网内部互联外不得再挂其他链路/设备，
    否则成环。接入交换机上配套的防环手段：LPS（Learned Port Security）、
    Loop Guard、BPDU Shutdown。DHL 通过修改各 VLAN 的转发状态防环并在
    链路故障时保持到核心的连通。
  tags: [dhl, loop-prevention, security]

- id: p15
  title: ERPv2 关键常数（50ms/16节点/4094 VLAN/64环/1200km）
  type: principle
  source_chapter: "p122"
  source_quote: |
    "• Network protection mechanism (ring topology) that enables 50 ms convergence time upon a link or node failure
    • Ethernet Ring Protection - ITU-T G.8032/Y.1344
    • Packet format compliant to OAM PDU Format - IEEE 802.1ag
    • 16 nodes per ring (recommended) • 4094 protected Vlans
    (p125) with less than 1200 km of ring fiber circumference, and fewer than 16 Ethernet Ring Nodes, the switch completion time ... shall be less than 50 ms.
    (p128) Maximum of 64 ERP rings per switch"
  summary: |
    ERPv2 环网保护常数：链路/节点故障后 50ms 内切换（G.8032 承诺条件：无
    拥塞、节点空闲态、环光纤周长 <1200km、节点数 <16）；每环建议最多 16 节点；
    每环最多 4094 个保护 VLAN；每台交换机最多 64 个 ERP 环。标准基于
    ITU-T G.8032/Y.1344，报文格式符合 IEEE 802.1ag。支持机型：6360/6560E/
    6570M/6860N/6870/6865/6900/9900（OS2260 除外）。
  tags: [erp, g8032, ha, ring]

- id: p16
  title: ERP 回切模式与 RPL 放置规则
  type: principle
  source_chapter: "p123"
  source_quote: |
    "• Revertive and Non-Revertive Mode
    • Non-Revertive Mode : After ring or links failure recovery, the ring does not automatically revert
    (p127) • Each ring must have its own RPL
    • The RPL can be placed anywhere on the Master Ring, including the shared links
    • The RPL can be placed anywhere on the Sub Rings, including the 'sub-ring' port
    • Since the Sub Ring is not closed using the shared link, the RPL cannot be placed on the shared link"
  summary: |
    ERPv2 支持回切（Revertive）与非回切（Non-Revertive）两种模式，非回切
    模式下环/链路故障恢复后不自动回切。RPL（环保护链路）规则：每个环（主环、
    子环各自独立）必须有且只有一个 RPL；主环的 RPL 可放任意位置包括共享链路；
    子环 RPL 可放任意位置包括子环口，但子环 RPL 不能放在共享链路上（因
    子环经共享链路不闭合）。子环可用 R-APS 虚拟通道承载控制报文。
  tags: [erp, rpl, ring, configuration]

- id: p17
  title: SPB 核心优势与规模常数（~300ms 收敛/1000 节点）
  type: principle
  source_chapter: "p103"
  source_quote: |
    "Resiliency / Scalability
    • Fast reconvergence (~300ms)
    • Path diversity / Increase bandwidth utilization
    • Low latency • High availability
    • Scalability (up to 1000 nodes)
    (p85) • All network links are use with no loops
    • Spanning Tree Protocol replacement
    • Uses the shortest path end to end
    • 100's ms convergence times
    • Symmetrical and congruent paths
    • Address isolation through mac-in-mac"
  summary: |
    SPB-M（IEEE 802.1aq）卖点常数：故障重收敛约 300ms；单域规模最多 1000
    节点；全部链路可用且无环（替代 STP）；端到端走最短路径；流量对称同径
    （适合防火墙/监控）；MAC-in-MAC 地址隔离；多租户/VPN；相比 MPLS 更简单。
    支持机型：6860N、6870、6865、6900、9900（p85；6570M/6575 自 8.10R4 起
    支持，6560/E 需许可）。
  tags: [spb, ha, capacity, convergence]

- id: p18
  title: SPB 园网部署的三层角色规则（BCB/BEB/接入）
  type: principle
  source_chapter: "p100"
  source_quote: |
    "Core — Backbone Core Bridge (BCB) role: Learns BEB addresses, IS-IS SPB for paths, PBB for data plane, L3 routing
    Aggregation — Backbone edge bridge (BEB) role: VLAN to I-SID, IS-IS for MAC learning, IS-IS for SPB paths, PBB for data plane, Loopback Detection Feature
    Access — IEEE 802.1Q VLAN on uplinks (port or LAG), STP towards BEB"
  summary: |
    SPB 园网分层角色分配：核心层 OS9900/OS6900 做 BCB（只学 BEB 的 BMAC，
    不感知业务，做 L3 路由）；汇聚层 OS6870/OS6860N（或 6900/9900）做 BEB
    （VLAN→I-SID 映射、业务终结、边缘 MAC 学习、环回检测）；接入层保持普通
    802.1Q VLAN 上联（端口或 LAG），向 BEB 跑 STP。报价时核心/汇聚按此角色
    选型。
  tags: [spb, beb, bcb, design]

- id: p19
  title: SPB 上跑三层路由的两种机制（IP-VPN Lite vs L3/IP-VPN）
  type: principle
  source_chapter: "p95"
  source_quote: |
    "AOS supported two mechanisms: IP-VPN Lite / L3/IP-VPN
    (p97 VPN-Lite) Run routing protocols on L3VPN IP interfaces ... No need IGP in the Core/Aggregation for routing
    (p99 L3/IP-VPN) Routes can be selectively imported into ISIS-SPB and advertised across the SPB-M domain
    ISIS-SPB protocol acts as an IP-IGP protocol
    No need to run routing protocols on L3 VPN IP interfaces
    (p95) VRFs on different BEBs are tied together by ISIDs across SPB-M backbone"
  summary: |
    SPB 骨干上的 L3 VPN 两种做法：①IP-VPN Lite——BEB 上建 VRF IP 接口，
    不同 BEB 的 VRF 靠 I-SID 打通，需要在 L3 VPN 接口上运行路由协议；
    ②L3/IP-VPN——VRF 路由经 ISIS/SPB 专用 TLV 选择性发布，ISIS-SPB 本身
    充当 IP IGP，无需在 VPN 接口上跑路由协议。两者共同点：核心/汇聚无需
    额外 IGP，SPB-M 网络等效为一台物理设备。
  tags: [spb, vpn, routing]

- id: p20
  title: VXLAN 关键常数（UDP 4789/50字节开销/24bit VNI/16M网络）
  type: principle
  source_chapter: "p107"
  source_quote: |
    "• UDP port 4789 by default
    VXLAN header • 50 bytes of overhead
    • Include 24 bit VXLAN Identifier
    • 16 M logical networks
    (p105) • Acts as a L2 VPN over L3 • RFC 7348
    (p118) • In the case of the AOS gateway is PIM-BIDIR. • In VXLAN, one multicast group is used per VNI.
    (p119) • Compliant with IETF RFC 5015 (BIDIR-PIM)"
  summary: |
    VXLAN 常数与规则：RFC 7348；默认 UDP 目的端口 4789；封装开销 50 字节；
    24bit VNI 最多 1600 万逻辑网络；外层源/目的 IP 即本地与远端 VTEP 地址
    （VTEP 用 Loopback0 标识）。BUM 流量两种转发：Head-End 复制（单播复制
    到所有已知远端 VTEP）与 Tandem 模式（标准 IP 组播，AOS 网关侧用
    PIM-BIDIR，符合 RFC 5015，每个 VNI 一个组播组）。VTEP 机型：6860N/
    6870/6900/9900；所有 OmniSwitch 都可透传 VXLAN 隧道（p105）。
  tags: [vxlan, constant, vtep, multicast]

- id: p21
  title: VXLAN 三层路由的两种交付方法（VPN-Lite vs L3VPN/EVPN）
  type: principle
  source_chapter: "p120"
  source_quote: |
    "We have delivered improvements in two steps for VXLAN-L3, which allow route exchanges over VXLAN service, using one of the two following methods :
    - VPN-Lite (Inline IP routing over VXLAN service - routing protocols running end-to-end, no BGP EVPN/VXLAN control plane)
    - L3VPN (Inline IP routing over VXLAN service - BGP EVPN/VXLAN control plane)"
  summary: |
    VXLAN-L3（VXLAN 业务上交换路由）两种方式：①VPN-Lite——内联 IP 路由，
    路由协议端到端运行，无 BGP EVPN/VXLAN 控制面；②L3VPN——内联 IP 路由
    配 BGP EVPN/VXLAN 控制面（MP-BGP，支持 RR/Route Server、Route Target 等）。
    8.10R1/R2 分两步交付于 OS6900，随后 OS6870。
  tags: [vxlan, evpn, routing]

- id: p22
  title: 二层高可用方案选型总结（VC 首选）
  type: principle
  source_chapter: "p129"
  source_quote: |
    "Redundancy solution ACTIVE-ACTIVE L2 : VIRTUAL CHASSIS (VC) preferred
    Link redundancy 100% Bandwidth Switch redundancy Unified Management [VC]
    Link redundancy 50% Bandwidth ... [STP]
    Link redundancy 100% Bandwidth ... [802.3Ad LACP] No Unified Mngt
    Link redundancy DHL Active-Active 100% Bandwidth Switch redundancy [DHL] No Unified Mngt
    Link redundancy ERP 100% Bandwidth Switch redundancy Scalability [ERP] No Unified Management
    100% Links UP Scalability Traffic isolation [SPB] No Unified Management"
  summary: |
    接入双上联冗余方案对比（售前话术要点）：VC——链路+整机冗余、100% 带宽、
    统一管理，L2 主主首选；STP——仅 50% 带宽、无统一管理；LACP——100%
    带宽但无交换机冗余与统一管理；DHL——100% 带宽+交换机冗余，无统一管理；
    ERP——100% 带宽+可扩展（环网），无统一管理；SPB——100% 全链路 UP、
    可扩展、流量隔离，无统一管理（核心层方案）。
  tags: [ha, vc, stp, lacp, dhl, erp, spb, positioning]

- id: p23
  title: MACsec 站点许可规则（OS-SW-MACsec 每客户一份免费）
  type: principle
  source_chapter: "p177"
  source_quote: |
    "OS-SW-MACsec
    One license per customer at no cost.
    Site license to enable MACsec on applicable models:
    OS6465 OS6560/E OS6570M OS6860N OS6870 OS6865 OS6900 OS9900
    Beginning in 8.6R1 the MACsec feature requires a site license. After upgrading, the feature will be disabled until a license is installed.
    There is no reboot required after applying the license."
  summary: |
    MACsec 许可规则：OS-SW-MACsec 为站点级许可，每个客户一份、免费；适用
    机型 6465/6560E/6570M/6860N/6870/6865/6900/9900。自 8.6R1 起 MACsec 必须
    装许可，升级后未装许可则功能禁用；装许可后无需重启。报价时 MACsec
    license 零成本但必须列入订单行。
  tags: [macsec, licensing]

- id: p24
  title: MACsec 机型/端口支持矩阵与 OS6560 端口分段规则
  type: principle
  source_chapter: "p178"
  source_quote: |
    "OS6870: Static Yes / Dynamic-PSK Yes / Dynamic-EAP Yes — All ports, all models, except VFL ports on 6870-24/48
    OS6860N-U28: Static No ... All ports except VFL
    OS6570M-12: Static No ...
    (p180) OS6560-P24X4 Ports 1-24: User ports (Static and Dynamic modes) Ports 25-30: SFP(+) uplink ports (Not Supported)
    OS6560-P48X4 Ports 1-48: 1G user ports (Static and Dynamic modes) Ports 49-52: SFP(+) uplink ports (Dynamic mode only) Ports 53-54: SFP+ uplink ports (Not Supported)"
  summary: |
    MACsec 支持规则：OS6870 全机型全端口支持 Static/Dynamic PSK/Dynamic EAP
    三模式（仅 6870-24/48 的 VFL 口除外）；OS6860N 各型不支持 Static、以
    动态为主（U28 全口除 VFL；P48Z/P24Z 仅 SFP28 上联口；P48M 仅 MG 口与
    扩展模块）；OS6570M-12 无 Static、U28 全模式全口；OS6465-P12/P6 全模式
    1G 口；6900 各 NI 与 CMM 全模式。OS6560 端口分段规则：P24X4 1-24 口
    静+动、25-30 不支持；P48X4 1-48 静+动、49-52 仅动态、53-54 不支持；
    6560E-P48Z16 1-32(1G) 与 33-48(MG) 静+动、49-52 仅动态、53-54 QSFP+
    不支持；6560-X10 1-8 仅动态、9-10 QSFP 不支持。
  tags: [macsec, model, port-matrix]

- id: p25
  title: OmniVista 2500 容量常数与节点许可规则
  type: principle
  source_chapter: "p191"
  source_quote: |
    "• Up to 10,000 devices (includes AOS and Third-Party)
    • Up to 4000 Stellar APs
    • Up to 5,000 VMs from all Hypervisors
    (p194) Starter Pack License is free OV4-START-NEW
    (p199) 1 License Unit per Physical Unit ... OS9900 in VC– All units need to be licensed A VC of 2 = 2 license units ... 1 license count per IP mgmt address [3rd party]"
  summary: |
    OV2500 容量：单套最多管理 10000 台设备（含 AOS 与三方）、4000 台
    Stellar AP、5000 个 VM（VM Manager，不限 Hypervisor 数量）。节点许可
    规则：ALE 交换机/WLAN 控制器每物理台 1 个许可单元，VC 内每台都要计
    （2 台 VC=2 个许可）；Stellar AP 每 AP 1 个；三方设备按管理 IP 地址
    每地址 1 个。Starter Pack（OV4-START-NEW）免费；HA 许可自 4.3R1 提供，
    加到主机后备机无需重复购买许可（p198）。虚拟机平台：VMware ESXi
    6.5-8.0、Hyper-V 2012R2-2022、Linux KVM/Ubuntu 22.04（p191）。
  tags: [ov2500, licensing, capacity]

- id: p26
  title: OmniVista Cirrus 订阅与 Freemium 规则
  type: principle
  source_chapter: "p217"
  source_quote: |
    "• Currently each OV tenant can support • up to 5000 devices • up to 4000 APs
    (p219) Freemium Self Registration Free of charge No device capacity limitation No duration limitation No network Configuration ... Max amount of licenses: 5000 included Stellar APs and OmniSwitch
    (p220) License types Essential, Advanced, Core, Access Points
    Subscription duration 1, 3 or 5 years
    Service bundles Base, Premium and Business"
  summary: |
    OV Cirrus（云管）规则：每租户最多 5000 台设备、4000 台 AP；Freemium
    免费自注册，无设备数与时长限制，但不能做网络配置（仅一次性设备升级、
    清单），可升级为付费账户；付费订阅结构：许可类型 Essential/Advanced/
    Core/Access Points，订阅期 1/3/5 年，服务包 Base/Premium/Business，经
    ALE Business Store/CPQ 或 eBUY 订购，可扩容/缩容/续订；许可上限 5000
    （含 Stellar AP 与 OmniSwitch）。
  tags: [cirrus, saas, licensing, subscription]

- id: p27
  title: OmniVista Network Advisor 定价与许可生命周期规则
  type: principle
  source_chapter: "p244"
  source_quote: |
    "NETAD-AP-1Y ... 50 USD 48 EURO / NETAD-SWITCH-1Y ... 100 USD 96 EURO / NETAD-TP-1Y ... 100 USD 96 EURO
    NETAD-AP-3Y 100 USD 96 EURO / NETAD-SWITCH-3Y 200 USD 191 EURO / NETAD-TP-3Y 200 USD 191 EURO
    NETAD-AP-5Y 150 USD 143 EURO / NETAD-SWITCH-5Y 300 USD 286 EURO / NETAD-TP-5Y 300 USD 286 EURO
    (p245) A 30 days grace period is attached to the duration of the license.
    (p246) Limits: 2000 Network devices ... * 1,8% of the total network cost"
  summary: |
    Network Advisor（AI 运维伴随）许可规则：每台设备 1 个 license（已含
    管理应用+Rainbow 伴随服务+支持服务，经 eBuy 订购）。牌价：AP 1年
    $50/48€、3年 $100/96€、5年 $150/143€；OmniSwitch 与三方设备 1年
    $100/96€、3年 $200/191€、5年 $300/286€——约为网络总成本的 1.8%。
    许可激活即开始计时，含 30 天宽限期；平台限 2000 台设备。版本门槛
    （p243）：OS6xxx/9xxx 需 AOS 8.7R2+，OS2xxx 需 5.2.R1+，Stellar AP 需
    AWOS 4.0.3 MR-3+；虚拟机 ALE 不售需自备（4 核/8GB RAM/50GB HDD）。
  tags: [network-advisor, pricing, licensing]

- id: p28
  title: 供货分级规则（Standard 2周/Extended 4周/Contact）
  type: principle
  source_chapter: "p326"
  source_quote: |
    "• Standard: Indicates that availability of product ARO (After Receipt of Order) is within standard delivery times quoted by Alcatel-Lucent . Average delivery lead-time is two (2) weeks ARO.
    • Extended: Indicates that availability of product ARO is greater than standard delivery time. Average delivery lead-time is Four (4) weeks ARO.
    • Contact: Product is announced but not released; availability information can only be given by contacting your Alcatel-Lucent representative.
    • 'Contact' within the Service and Support section identifies items that must be scheduled before placing an order.
    Sales category designations are A, B, C, D, E, F, G, H, I, J, K, L, M, O, P, Q, S, U, W, Z and NA .
    • Service category designations are a combination of two digits."
  summary: |
    价目表供货三档：Standard——ARO（收单后）平均 2 周到货；Extended——平均
    4 周 ARO；Contact——已发布未上市，交期需联系 ALE 代表（服务与支持栏的
    Contact 表示下单前须先排期）。价目表编码规则：Sales Category 为单个
    字母（A/B/C/D/E/F/G/H/I/J/K/L/M/O/P/Q/S/U/W/Z/NA），决定折扣级别；
    Service Category 为两位数字组合，决定服务级别；两者都需按合同或渠道
    查询。注：任务提示中的 PW/SP 维护合约前缀规则未在本册出现。
  tags: [pricing, availability, ordering]

- id: p29
  title: 订购型号后缀规则（-ZZ 无电源线 / -00 无电源）
  type: principle
  source_chapter: "p328"
  source_quote: |
    "Switch model with “–ZZ” extension have no power cord included
    e.g. OS6860N-P48M-ZZ OS6560-P24X4-ZZ
    For OS6860N models with “-00” extension PS must be ordered separately
    e.g. OS6860N-P24M-00"
  summary: |
    OmniSwitch 订购规则：型号后缀 -ZZ 表示不含电源线（需按国家单独订
    电源线）；-00 表示不含电源（PS 需单独下订）。完整订单四要素：交换机
    主机（含/不含 PS）+ 备份与 PoE 电源 + 堆叠线/光模块/配件 + 软件许可。
    其他后缀：P=PoE 机型，D= bundle 带 DC 电源（p335）。
  tags: [ordering, suffix, quotation]

- id: p30
  title: 各机型软件许可订购规则汇总（MACsec/Metro/AR/PRM/PERF/MPLS）
  type: principle
  source_chapter: "p334"
  source_quote: |
    "OS6570M: • No license needed for Metro Ethernet, it is included
    • Advanced Routing (AR) license from 8.9R4
    • PRM12 license to enable both AR and SPB on 12/12D
    • PERF license to enable additional 10G ports on U28
    • PRM28 to enable 25G speed on uplinks, Advanced Routing and SPB on U28
    (p337) OS6870: • PERF license per unit
    • PRM1 to enable VxLAN EVPN and 50G on Premium models (M and V)
    • PRM2 to enable VxLAN EVPN on advanced models (24/48 and Z)
    (p335) OS6860N: • MACsec license per unit (no cost) • MPLS license per unit"
  summary: |
    机型许可规则：OS6570M——Metro 以太网功能内置免许可；AR 许可自 8.9R4；
    PRM12 开 12/12D 的 AR+SPB；PERF 开 U28 额外 10G 口；PRM28 开 U28 的
    25G 上联+AR+SPB。OS6870——PERF 每台；PRM1 开 Premium（M/V）型的
    VXLAN EVPN+50G；PRM2 开高级型（24/48 与 Z）的 VXLAN EVPN。OS6860N——
    MACsec 每台免费、MPLS 每台收费。OS6560——Metro 许可 8.9R1 起、AR 许可
    8.9R4 起、上联口可用许可升 10G（p333/369）。OS6465/6360——MACsec 免费、
    6360 有 10G 升级许可（p331/332）。OS6900/6920——内置冗余电源，MACsec
    （OS-SW-MACSEC 免费必须列入）+ MPLS 许可（p340）。
  tags: [licensing, model, ordering]

- id: p31
  title: 演示许可与永久许可的差异规则
  type: principle
  source_chapter: "p346"
  source_quote: |
    "• Demo License
    • Available once for MPLS (can be used one time and not more)
    • Valid for 30 days total
    • Activated as soon as MPLS is run on a node
    • Permanent License (for MPLS, Metro Ethernet, Advanced routing, 10G)
    • Each one is unique (serialized)
    • Valid for a specific set of feature and platform"
  summary: |
    软件许可两类：演示（Demo）许可仅 MPLS 提供、每客户只能用一次、总有效期
    30 天、在节点上第一次运行 MPLS 即激活计时；永久许可（MPLS/Metro
    Ethernet/Advanced Routing/10G）与设备序列号绑定、针对特定特性集与平台，
    以纸质文档或电子副本交付。
  tags: [licensing, demo, mpls]

- id: p32
  title: OS9900 机箱平台常数（9907/9912 槽位/容量/PoE/VC）
  type: principle
  source_chapter: "p12"
  source_quote: |
    "OMNISWITCH 9907: 7 Slot Chassis ... 1 CMM Slot 1 CMM/NI Slot 5 Network Interface Module Slots 4 CFM Slots, rear accessible 4 power supply bays 3 fan tray Slots
    25.6 Tbps Full Duplex max switching capacity
    Up to two OS9907 can be connected using virtual chassis technology.
    10800W of inline PoE power 11-RU form factor
    OMNISWITCH 9912: 12-slot ... 2 CMM Slots 10 Network Interface Module Slots
    51.2 Tbps Full Duplex switching fabric
    OS9912 will support virtual chassis technology in future release.
    7920W of inline PoE power 17.25-RU form factor"
  summary: |
    OS9907：7 槽机箱（1 CMM + 1 CMM/NI + 5 NI + 后部 4 CFM + 4 电源 + 3
    风扇），交换容量 25.6Tbps（CFM2 单芯片 12.8Tbps），PoE 10800W，11RU，
    支持双机 VC。OS9912：12 槽（2 CMM + 10 NI），51.2Tbps，PoE 7920W，
    17.25RU，VC 为未来版本支持。CMM/CMM2 带 4×100G QSFP28 上联/VFL 口，
    冗余系统最多 8×100G；每 40/100G 口可拆 4×10/25G（p445）。典型部署：
    融合校园核心/汇聚、数据中心 EoR、Spine-Leaf。
  tags: [os9900, chassis, capacity, poe]

- id: p33
  title: OS9900 供电与 PoE 分配规则（75W 前8口/30W 其余40口）
  type: principle
  source_chapter: "p454"
  source_quote: |
    "Power Supply Available Power per PS
    AC at 240V (highline) 3000 W
    AC at 120V (lowline) 1200 W
    DC 2500 W
    (p455) • OS9907 provides up to 10800W • OS9912 provides up to 7920W • 75 W per port
    • GNI-P48 & XNI-P48Z16 support 75 watts for ports 1-8 and up to 30 watts for the remaining 40 ports
    Standard Max. PoE power per port
    IEEE 802.3af 15.4/12.95 watts
    IEEE 802.3at 30/25.5 watts
    HPoE (first 8 Ports) 75 watts"
  summary: |
    OS9900 供电规则：系统与 PoE 共用电源，无需外置电源架；每块电源可用
    功率 AC 240V 时 3000W、AC 120V 时 1200W、DC 2500W；4 槽 3+1 冗余；
    系统上电优先，剩余功率全部给 PoE，可配 N+1 冗余模式。PoE 分配：
    802.3af 15.4/12.95W、802.3at 30/25.5W、HPoE 75W；GNI-P48 与
    XNI-P48Z16 板前 8 口 75W、其余 40 口最高 30W。9907 最大 PoE 10800W
    （单 CMM 双 CFM + 4×3KW 电源带 6×GNI-P48），9912 为 7920W。
  tags: [os9900, power, poe]

- id: p34
  title: 虚拟机箱 vs 物理机箱选型对比常数（6×6900 vs 9907/9912）
  type: principle
  source_chapter: "p303"
  source_quote: |
    "Virtual Chassis (6x6900) vs Chassis (9907/9912)
    Initial Investment: Lower – Pay as you grow | Higher for Chassis itself, high capacity power supply, and blade space
    Reboot time (switch or blade): Higher (control & data plane) | Lower (only data plane)
    Rack space: Lower (6U) | Higher (11U/17U)
    POE: None with OS6900 | 75 & 30 W per port on P module
    Cost: Lower | Significantly Higher
    1G: 432 | 288/480  10G: 432 | 256/480  40G/100G: 162 | 108/208
    ACLS: 4K | 1K"
  summary: |
    核心层"6 台 6900 组 VC"对比"9907/9912 机箱"：初始投资更低（按需扩容）
    vs 更高；时延略高（多跳）vs 略低（单跳）；整机/刀片重启时间 VC 更长
    （控制+数据面）vs 机箱更短（仅数据面）；机架 6U vs 11/17U；管理分布
    式 vs 集中式；6900 无 PoE vs P 模块 75/30W；总成本 VC 更低。端口数：
    1G 432 vs 288/480；10G 432 vs 256/480；40/100G 162（C32E 27 口×6）vs
    108/208；ACL 4K vs 1K；IP 路由 12K-384K（按型号）vs 128K；L2 MAC
    16K-228K vs 128K。
  tags: [vc, chassis, comparison, core]

- id: p35
  title: OS6900/OS6920 关键常数（容量/时延/VC台数）
  type: principle
  source_chapter: "p428"
  source_quote: |
    "OMNISWITCH 6900-C32E
    • 128 x 10G ports • 128 x 25G ports
    • Scalable with 32x100G-BaseX ports with QSFP28 connectors
    • Very Low Latency <600ns
    • 6.4Tbps switching and 4.8 Gbs throughput
    • Virtual chassis of up to 6 switches
    (p439) OS6920-D32: 64 x 200G ports • 256 x 50G • 128 x 100/25/10G ports
    • Very Low Latency <500ns • 12.8 Tbps switching and 9.6 Gbs throughput
    • Virtual chassis of up to 4 switches"
  summary: |
    OS6900-C32E：32×QSFP28 100G 口（splitter 可拆 128×10G 或 128×25G），
    6.4Tbps 容量，时延 <600ns，VC 最多 6 台，450W 冗余电源、5+1 风扇。
    其他 6900 型号：X/T48C6 与 X48C6 为 2.16Tbps，X/T24C2 为 1.08Tbps
    （400W 新电源）；V48C8 48×SFP28+8×QSFP28；X48C4E 自 8.9R4 起支持 VC
    且全口 MACsec。OS6920-D32：32×QSFP-DD 400G（可拆 64×200G/256×50G/
    128×100/25/10G），12.8Tbps，<500ns，VC 最多 4 台（初期 2 台，p63），
    1500W 电源。
  tags: [os6900, os6920, capacity, latency]

- id: p36
  title: OS6870 家族常数（单芯片容量/PoE预算/VC×8）
  type: principle
  source_chapter: "p424"
  source_quote: |
    "OS6870 24/48/P24Z/P48Z/P24M/P48M/V12
    Uplinks: Fixed 4x or 6x 1/10/25G SFP28; Modular 6 x 10/25/50G SFP56 or 2 x 40/100G QSFP28
    VFL ports: 2 x 40/100G QSFP28 (24/48/Z) | 2 x 40G/100G/200G QSFP56 (P24M/P48M/V12)
    PS Supported: 600W, 1200W (Z) | 600W, 1200W, 2000W AC PoE (M) | 550W AC, 250W DC (V12)
    Memory: 8GB SDRAM; 32 GB Flash  AOS Release 8.10R2
    (p415) Single ASIC with 1.88 Tbps ... 802.3bt compliant 95W per port, maximum 3630W budget ... Max VC 8 mix and match with any OS6870 models"
  summary: |
    OS6870 家族背参数（AOS 8.10R2、8GB/32GB、最多 8 台 VC 且任意型号混搭）：
    单芯片容量 P24M/P48M 1.88Tbps（95W/口，PoE 预算最大 3630W/3600W）、
    V12 2Tbps（12×SFP28+2×QSFP56，无 PoE，550W AC/250W DC）、P24Z
    820Gbps/2300W、P48Z 940Gbps/2000W（60W/口）、24 型 748G、48 型
    796G（无 PoE，250W）。高级型（24/48/Z）VFL 为 2×QSFP28 40/100G 且
    MACsec 除 VFL 口外全口支持；Premium（M/V）VFL 为 2×QSFP56 最高 200G、
    全口 MACsec。电源 600/1200/2000W，支持不平衡负载分担（两块不同功率
    电源可负载分担）。
  tags: [os6870, capacity, poe, vc]

- id: p37
  title: OS6360 各型号 PoE 预算常数（满配 vs 优化）
  type: principle
  source_chapter: "p360"
  source_quote: |
    "OS6360-P10: Internal 160W fixed power supply • 120W Full PoE power budget (~15W/port)
    OS6360-P24: Internal 260W fixed supply • 200W optimized PoE power budget (8.33W/port)
    OS6360-P48: Internal 550W fixed supply • 390W optimized PoE power budget (8.125W/port)
    (p363) OS6360-PH24: Internal 550W fixed power supply • 390W Full PoE power budget: (16.25W/port)
    OS6360-P24X/P48X: Internal 550W/950 fixed power supply • 390W/780W Full PoE power budget: (16.25W/port)"
  summary: |
    OS6360 PoE 预算速查：P10 120W 满配（约 15W/口，内置 160W 电源）；P24
    200W 优化预算（8.33W/口，260W 电源）；P48 390W 优化（8.125W/口，
    550W 电源）；PH24/P24X/P48X 390W/780W 满配（16.25W/口）。全系支持
    Fast & Perpetual PoE；系统功耗约 20-65W；OS6360-P48X 有 2 口
    1G/2.5/5G HPoE。选型时按 AP/话机实际每口功率决定选优化型还是满配型。
  tags: [os6360, poe, budget]

- id: p38
  title: OS6865 PoE 预算随电源配置变化规则
  type: principle
  source_chapter: "p404"
  source_quote: |
    "(1) OS6865-BP or (1) OS6865-BP-D @48V: P16X 140W | U12X 140W | U28X 100W
    (2) OS6865-BP / (2) OS6865-BP-D @48V or mixed: 300W | 300W | 280W
    (1) OS6865-BP-D @24V: 100W | 100W | 80W
    Power Supply OS6865-BP: 180W (System and PoE power) OS6865-BP-D: 180W (System and PoE power)"
  summary: |
    OS6865 PoE 预算按电源数量与电压：1 块 BP/BP-D@48V 时 P16X 140W、U12X
    140W、U28X 100W；2 块 @48V（或 AC+DC 混配）时 300/300/280W；@24V 时
    降为 100/100/80W（2 块或混配 240/240/200W）。每块电源总功率 180W
    （系统+PoE 合计）；P16X 前 4 口支持 75W HPoE。
  tags: [os6865, poe, power, ruggedized]

- id: p39
  title: 应用监控（AppMon/DPI）流表与签名常数
  type: principle
  source_chapter: "p268"
  source_quote: |
    "• Available on all models of OS6860N and OS6870 family
    • Does not require switch license
    8K flows per unit
    64k flows per VC (8 units)
    (p269) • Up to 2000 user configured signatures"
  summary: |
    应用可见性与监控（AppMon/DPI）规则：OS6860N 与 OS6870 全系内置、无需
    交换机许可；每台跟踪 8K 条流、每个 VC（8 台）64K 条流；签名库由
    OmniVista 自动下载更新，用户自定义监控应用（profiling）签名最多
    2000 条（OS6860E 侧，p269）。
  tags: [appmon, dpi, capacity, os6860n, os6870]

- id: p40
  title: UNP 认证两步流程与"初始 UNP/VLAN 终身不变"规则
  type: principle
  source_chapter: "p152"
  source_quote: |
    "L2 authentication
    802.1x or MAC authentication or classificiation
    Result of this process is a UNP edge profile
    L3 classification
    Based on UNP properties into which the user was learnt into after the 1st Step
    QMR/Location/Time based validations may be enabled in the UNP
    If validations fail the user is put into a Restricted Role (policy list)
    Initial UNP (which provides the initial policy list and role) and Vlan does not change during the lifetime of the user
    Only the roles change dynamically"
  summary: |
    Access Guardian/UNP 认证流程规则：第一步 L2 认证（802.1x/MAC/分类）产生
    边缘 UNP；第二步 L3 分类，可启用 QMR/位置/时间校验，失败则进受限角色。
    关键约束：用户的初始 UNP（含初始策略与 VLAN）在会话生命周期内不变，
    动态变化的只是角色（policy list）。
  tags: [unp, access-guardian, authentication]

- id: p41
  title: IoT 设备画像的四种指纹依据
  type: principle
  source_chapter: "p164"
  source_quote: |
    "MAC OUI
    DHCP fingerprint (i.e. DHCP option 55)
    DHCP Vendor-ID (i.e. DHCP option 60)
    Up to 5 HTTP User-Agents"
  summary: |
    IoT 设备画像（Device Profiling）收集端点上报的四种指纹：MAC OUI、
    DHCP 指纹（option 55）、DHCP Vendor-ID（option 60）、最多 5 条 HTTP
    User-Agent。画像服务据此分类并向交换机/AP 下发 Enforcement 消息
    （MAC+类别+可选 UNP），按类别自动分配 UNP（内置 PoE 摄像头、温度
    传感器、心率监护等类别模板）。
  tags: [iot, profiling, unp]

- id: p42
  title: OmniVista 预测分析的数据区间规则
  type: principle
  source_chapter: "p272"
  source_quote: |
    "Configured Time Interval | Amount of Predicted Data
    Last 24 Hours | 12 Hours
    Last 7 Days | 3 Days
    Last 4 Weeks | 2 Weeks"
  summary: |
    OmniVista Top N Ports 趋势预测的换算规则：报表取最近 24 小时数据则
    预测未来 12 小时；取最近 7 天预测 3 天；取最近 4 周预测 2 周。预测基于
    机器学习算法、带可配置误差率，用于容量规划。
  tags: [ov2500, analytics, predictive]

- id: p43
  title: 两层 vs 三层架构的特征与速率/时延常数
  type: principle
  source_chapter: "p289"
  source_quote: |
    "THREE-TIER MODEL: • Scalable Segmentation ... • Low-latency (>12µs)
    Access 100M->1G->2.5G->5G->10G / Aggregation 1G->10G->25G / Core 10G->25G->40G->100G
    (p291) TWO-TIER MODEL: • High-throughput • High Density • Lowest-Latency
    • Faultless with low and predictable latency • 1.5 to 6µs
    • Access and distribution layers merging
    100M->1G->2.5G->5G->10G / 10G->25G->40G->50G->100G"
  summary: |
    架构常数：三层模型（接入-汇聚-核心）时延量级 >12µs，接入与汇聚分离、
    设备分设 L2/L3，适合分段扩展；两层模型（接入分布层合并）时延 1.5-6µs、
    无阻塞低收敛比，适合高密度/数据中心。速率路径：接入 100M→10G，三层
    汇聚 1G→25G、核心 10G→100G；两层上联/核心 10G→50G→100G。
  tags: [design, architecture, latency]

- id: p44
  title: 企业 SPB LAN 核心设计原则
  type: principle
  source_chapter: "p319"
  source_quote: |
    "MPLS styled service architecture
    VLAN extensibility across campus
    No STP
    Faster, easier to deploy
    Service Virtualization (ISID) for departmental isolation
    Enabling multi-tenancy on campus sites
    L3 inter-departmental routed control with VPN-lite or L3-VPN
    VXLAN support for DCI
    Transparent VLAN extension and transport between campus segments across SPB-M network"
  summary: |
    企业 SPB 核心设计要点：类 MPLS 的业务架构；VLAN 跨校园透明延伸；无
    STP、部署更快更简单；I-SID 业务虚化实现部门隔离与园区多租户；部门间
    三层互通用 VPN-Lite 或 L3/IP-VPN；数据中心互联用 VXLAN。核心/汇聚用
    6860N/6870/6900/9900（BEB/BCB），接入仍用 6360/6465/6560E 普通 VLAN。
  tags: [spb, design, enterprise]

- id: p45
  title: OS6465 PROFINET 认证规则（Class B，仅单体 VC）
  type: principle
  source_chapter: "p381"
  source_quote: |
    "• OS6465 and OS6465T products are certified as Managed switches in PROFINET network
    • Certified for PROFINET Conformance Class-B compliance
    • PROFINET supported in VC of 1"
  summary: |
    OS6465/6465T 通过 PROFINET Conformance Class-B 管理型交换机认证（可用
    于 PROFINET 工业网网管交换机）；重要限制：PROFINET 只在 VC of 1（单机、
    不堆叠）状态下支持。OS6575 的 PROFINET 支持与认证自 8.10R4 引入（p33）。
  tags: [os6465, profinet, industrial]

- id: p46
  title: WWPL 价目表规则（升级不打折/币种/价格可变）
  type: principle
  source_chapter: "p324"
  source_quote: |
    "* The date noted on the front page of this price list.
    The products and prices are subject to change without notice.
    No discount is offered on upgrades.
    All prices in the Worldwide Price List version are in US Dollars and in the Worldwide Price List Euro are in Euros.
    (p200) • Paid Upgrades – based on UPG & U SKU from WWPL"
  summary: |
    价目表（WWPL）通用规则：产品与价格可随时变更且不另行通知；升级
    （Upgrade）订单不提供折扣；WWPL 版本以美元计价、Euro 版本以欧元计价。
    OV2500 等软件的付费升级基于 WWPL 的 UPG/U SKU，跨大版本许可钥不同，
    升级前需备份以保留拓扑/Locator/资源管理等数据（p200）。
  tags: [pricing, wwpl, upgrade]
```
