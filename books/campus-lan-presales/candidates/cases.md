# Campus LAN Presales Ed29 — 案例候选（cases）
# 提取自书中亲自使用的实例：参考架构、垂直行业方案、对比实例、视频监控插件方案、产品家族明星机型。
# 页码对应 fulltext.md 中 <<<PAGE N>>> 标记。

```yaml
- id: c01
  title: 城域以太商业管理服务汇聚环（OS6860N + OS6465-P28）
  type: case
  source_chapter: "p296"
  source_quote: |
    "OmniSwitch 6860N / Ring of OmniSwitches / Ethernet Access / Business Managed Services
    Aggregation / IP/MPLS / Core / 10 Gig Ring / 1 Gig Fiber / OmniSwitch 6465-P28 / Dual Homed fiber
    DHCP Option 82 configurable / DHCP Snooping / IP Anti-Spoofing based on DHCP snooping
    Dynamic ARP Inspection / Multicast TV VLAN / IEEE 802.1ad Provider Bridges
    IEEE 802.1aq Shortest Path Bridging (SPB-M) / Multipoint Ethernet VPN (EVPN) over I-SID"
  summary: |
    垂直行业方案：城域以太/运营商管理业务场景。10G 环上的 OmniSwitch 6860N 做以太接入与业务
    汇聚，OS6465-P28 双归光纤上联进入 IP/MPLS 核心网；1G 光纤环接入小客户。配套城域特性清单：
    DHCP Option 82/DHCP Snooping、IP 防欺骗、动态 ARP 检查、组播 TV VLAN、802.1ad 运营商桥、
    SPB-M、基于 I-SID 的多点 EVPN、VLAN 翻译映射、ETH-OAM 802.1ag。适用客户：电信运营商、
    开展以太专线/管理业务的服务商。
  tags: [vertical-industry, metro-ethernet, spb, erp-ring, os6860n, os6465, service-provider]

- id: c02
  title: 住宅三重播放（Triple-Play）城域接入（OS6560/E + 服务路由器）
  type: case
  source_chapter: "p296"
  source_quote: |
    "OmniSwitch 6560/E / Ethernet Access / Residential Triple-Play Services
    Service Router / OS6560 / 10 Gig Fiber / Metro Ethernet Network Switching
    Customer A / Customer B / Customer C / Metro Access Ring / Service Provider Network"
  summary: |
    垂直行业方案：住宅三重播放（语音+数据+视频）。OS6560/E 以太接入经 10G 光纤上联服务路由器，
    城域接入环承载客户 A/B/C 多户流量进入运营商网络。关键特性是 Multicast TV VLAN 支持 IPTV
    组播分发，配合 DHCP Snooping/ARP 检查做住户隔离。适用客户：住宅宽带运营商、光纤到楼/到户
    场景。
  tags: [vertical-industry, residential, triple-play, multicast-tv-vlan, os6560, service-provider]

- id: c03
  title: 数据中心 POD 网状架构（6 台 OS6900 Mesh POD）
  type: case
  source_chapter: "p297"
  source_quote: |
    "Data Center Network / 1/10 GigE / Layer 2 Switching / 10/40/100 GigE uplinks
    Mesh POD / 10/40/100 GigE / Layer 2/3 Switching / OS6900 x6 / POD / 10/40 GigE
    Server Hosting VMs x4"
  summary: |
    垂直行业方案：数据中心 POD（模块化机房单元）。6 台 OS6900 组成全网状（Mesh）POB 二/三层
    交换矩阵，服务器托管 VM 通过 1/10G 接入，POD 间以 10/40/100G 上联互联。端口数据：服务器侧
    1/10 GigE L2 交换，POD 骨干 10/40/100 GigE L2/L3 交换。适用客户：云服务商、企业数据中心
    扩容模块化建设。
  tags: [vertical-industry, datacenter, pod, mesh, os6900, vm]

- id: c04
  title: 虚拟机箱 VC（6x OS6900）与物理机箱（9907/9912）对比实例
  type: case
  source_chapter: "p303"
  source_quote: |
    "Virtual Chassis (6x6900) vs Chassis (9907/9912)
    Initial Investment: Lower – Pay as you grow / Higher
    Rack space: Lower (6U) / Higher (11U/17U)
    1G: 432 / 288/480 ; 10G: 432 / 256/480
    40G/100G: 162 (with C32E, 27 ports x 6 switches) / 108/208
    POE: None with OS6900 / 75 & 30 W per port on P module
    Reboot time: Higher (control & data plane) / Lower (only data plane)"
  summary: |
    售前常用对比实例：6 台 OS6900 组虚拟机箱对比 9907/9912 物理机箱。VC 优势：初始投资低、
    按需扩容、6U 机架空间、1G/10G 端口更多（各 432 个）；机箱优势：单跳时延更低、重启只影响
    数据面、P 模块可 75W/30W 供电、40/100G 密度与冗余（管理模块/矩阵/电源/风扇）。IP 路由表
    12K-384K 对 128K，MAC 16K-228K 对 128K。适用场景：核心选型辩论时的量化弹药。
  tags: [comparison, vc, chassis, os6900, os9900, core-selection, presales-argument]

- id: c05
  title: SMB 一体化方案（OS6360/6560 + OmniAccess IAP + OmniPCX + PTZ 摄像头）
  type: case
  source_chapter: "p305"
  source_quote: |
    "SMB solution / Short installation and set-up time with zero-touch configuration saves time/cost
    Fully integrated and lab tested, single vendor, plug and play solution (IP Network + Wi-Fi + Voice + Mobility)
    Gigabit access for next generation Wi-Fi (WiFi 5/6/7)
    Up to 4 x 10 Gig uplinks / Secure BYOD services (6560) / PoE+ support for voice, data and video surveillance
    OmniSwitch 6360-P10 / 6360-P24 / 6360-P48, OmniAccess Instant Access Points (IAP),
    MyIC & 8-Series phones, OpenTouch & OmniPCX Office (RCE), PTZ Camera"
  summary: |
    参考架构：SMB 一体化方案。单一厂商全家桶：OS6360-P10/P24/P48 千兆 PoE+ 交换机 + OmniAccess
    IAP 无线 + OmniPCX Office/OpenTouch 语音 + MyIC/8 系列话机 + PTZ 监控摄像头，上网经 PSTN/
    Internet 出口。卖点：零触摸配置、实验室预集成即插即用、WiFi 5/6/7 千兆接入、最高 4x10G 上联、
    基础统一接入安全（MAC/802.1x/AAA/uNP 策略）。适用客户：20-100 人小企业/分支办公室。
  tags: [reference-arch, smb, all-in-one, zero-touch, os6360, unified-access, poe]

- id: c06
  title: OS6360 SMB 方案"20 分钟配置语音/数据/Wi-Fi"零接触部署
  type: case
  source_chapter: "p306"
  source_quote: |
    "Configure Voice, Data and Wi-Fi in under 20 minutes
    OXO Purple boot-up process and OMC access
    Once boot-up, starting automatically download the configuration files from the OmniPCX
    OS6360 positioning: Support for 20-100 SMB users / Up to 10Gbs uplink speeds
    Cost-effective, enterprise quality switch / Zero-touch provisioning
    OmniAccess Stellar Access Points, ALE 300/400/500 phones, OXO Purple Clients, PTZ Camera"
  summary: |
    SMB 部署流程实例：OXO Purple（OmniPCX）上电引导后，交换机自动从 OmniPCX 下载配置文件，
    网络自建、IP 话机上线、首个 AP 接入 OS6360 即自动初始化——"20 分钟内配好语音/数据/Wi-Fi"。
    终端组合：OmniAccess Stellar AP、ALE 300/400/500 话机、OXO Purple 客户端、PTZ 摄像头。
    OS6360 定位 20-100 SMB 用户、最高 10G 上联。适用客户：无 IT 人员的小型办公室。
  tags: [smb, zero-touch, oxo-purple, omnipc-x, os6360, stellar, deployment-flow]

- id: c07
  title: 校园网两层/三层总体架构（接入-核心 / 接入-汇聚-核心选型图）
  type: case
  source_chapter: "p307"
  source_quote: |
    "L3 Core/Aggregation / Small enterprise Access/Core 'virtual chassis'
    Edge: OS6560/E OS6360 OS6465 / OS6900 / OS6870 / OS9900
    Aggregation: OS6560/E / Core: OS6860N OS6870 / 10/40 GigE Backbone
    Virtual Chassis DHL / 10/100M 1G/2.5G 5G/10G PoE PoE+ HPoE
    2-tier networks / 3-tier networks"
  summary: |
    参考架构：全书选型总图。两层网：边缘 OS6360/6465/6560-E 千兆 PoE 接入，OS6860N/6870 VC 或
    DHL 直连核心；三层网：OS6560/E 做汇聚，核心用 OS6900/6870/9900，骨干 10/40G。按端口速率
    （10/100M 到 10G）与供电（PoE/PoE+/HPoE）标注各层位置。适用客户：从单楼宇两层到多楼宇三层
    的通用园区。
  tags: [reference-arch, campus, two-tier, three-tier, design-approach, portfolio-mapping]

- id: c08
  title: OS6560/E 多千兆融合 IP 网边缘（WiFi 6/6E/7 AP + 95W HPoE）
  type: case
  source_chapter: "p308"
  source_quote: |
    "OS6560/E AT THE EDGE OF MGIG CONVERGED IP NETWORK
    AP15xx 2 x 2:2 MU-MIMO / 4 x 4:4 MU-MIMO / CAT5e / CAT6 cable
    10G Optical Uplink / WiFi 6/6E/7 AP's / 95W HPoE
    AP132x AP12xx AP13xx AP14xx
    2 x 10G SFP+ OS6560E-P24Z8 / OS6560-P24Z24/E-P48Z16 / 4 x 10G SFP+"
  summary: |
    参考架构：多千兆无线边缘。OS6560E-P24Z8、OS6560-P24Z24/E-P48Z16 等机型用 2.5G/5G 端口喂
    WiFi 6/6E/7 AP（AP12xx/13xx/132x/14xx/15xx，2x2 与 4x4 MU-MIMO），单口 95W HPoE（802.3bt）
    供电，CAT5e/6 布线即可，10G 光上联。适用客户：AP 空口吞吐超 1G、需在现有布线上跑多千兆的
    办公园区。
  tags: [reference-arch, mgig, wifi6, wifi7, hpoe, os6560, wireless-edge]

- id: c09
  title: OS6860N 八台虚拟机箱多千兆边缘（最多 384 千兆/192 多千兆口）
  type: case
  source_chapter: "p309"
  source_quote: |
    "Virtual Chassis for simplified architecture / Fully redundant and resilient network
    VC ports operate at 20/40/100GigE / Remote Stacking up to 100m / Up to 8 switches in a VC
    95W of PoE / 8 x OS6860N units / Up to 384 Gig ports / Up to 192 Multi Gig ports
    Core OS6900 / 4 x 25G SFP+ LACP / IEEE 802.11ax WiFi 6 AP's / IEEE 802.11be WiFi 7 AP's"
  summary: |
    参考架构：8 台 OS6860N 组一个虚拟机箱（100m 内远程堆叠，VC 端口 20/40/100G），可提供最多
    384 个千兆口或 192 个多千兆口，95W PoE（802.3bt）直供 WiFi 6/7 AP；上联以 4x25G SFP+ LACP
    接 OS6900 核心。附加能力：SPB/VXLAN/MPLS、MACsec、UNP、AppMon、快速故障收敛。适用客户：
    高密度无线楼宇、三层网大边缘。
  tags: [reference-arch, vc, remote-stacking, os6860n, mgig, wifi7, lacp, access-layer]

- id: c10
  title: OS9900/OS6900 单楼宇两层与多楼宇三层双核心设计
  type: case
  source_chapter: "p311-312"
  source_quote: |
    "OMNISWITCH 9900 TWO TIER/ THREE TIER DESIGN
    In the Core of the Network / At the Access layer: OS6360 OS6560/E OS6860N OS6870
    Two Tier, single Building / 10 GigE Link Aggregation / Dual Home link Active-Active
    Three Tier, Multi-Building / 10/40 GigE Link Aggregation / Dual core network for maximum redundancy
    OMNISWITCH 6900 ... SPB-M Core / SPB-M BEB"
  summary: |
    参考架构两个变体：p311 用 OS9900 做核心——单楼宇两层（10G LAG/DHL 双归属）与多楼宇三层
    （双核心最大冗余，10/40G LAG）；p312 用 OS6900 组 SPB-M 核心与 BEB 边缘，同样支持两层/三层
    双核心，接入层由 OS6360/6465/6560-E/6860N/6870 覆盖。适用客户：中型到大型政企园区、需要
    双核心冗余或 SPB 服务的场景。
  tags: [reference-arch, os9900, os6900, spb, dual-core, two-tier, three-tier, dhl]

- id: c11
  title: 紧凑核心网络（Compact Core，VC 虚拟化两层架构，两个核心变体）
  type: case
  source_chapter: "p314-315"
  source_quote: |
    "Network virtualized using Virtual Chassis (VC) for simplified two-layer architecture
    Fully redundant and resilient network / Fast re-convergence time on failure
    Server farm or data center dual home connected directly to network core with LAG
    OmniSwitch 6870 or 6860N for 10/25 GigE L2/L3 Core switching
    OmniSwitch 6560/E for 1/2.5/5 GigE access with PoE+ and 10GigE uplinks"
  summary: |
    参考架构：紧凑核心。p314 变体：OS6870 或 6860N 组 VC 做 10/25G L2/L3 核心，OS6560/E 做
    1/2.5/5G PoE+ 接入，服务器群以 LAG 双归属直挂核心；p315 变体：核心升级为 OS6900（10/25/40/
    100G），接入改为 OS6860N/6870（PoE++ 与 10/25/40/100G 上联）。两层架构+VC 软件升级，含
    UNP/DPI/AppMon。适用客户：中型单站点园区、扁平化改造。
  tags: [reference-arch, compact-core, vc, os6870, os6860n, os6900, two-layer, lag]

- id: c12
  title: 10/40G 分布式环网（ERPv2 + DHL，多楼宇）
  type: case
  source_chapter: "p316"
  source_quote: |
    "OMNISWITCH 10/40 GIGE DISTRIBUTED RING NETWORK
    Network virtualized using ERPv2 / Simplified two-layer architecture
    Fully redundant and resilient network / Fast re-convergence time on failure
    Dual Home Link (DHL) at the access / 10 GigE links from the network core to Server farm or data center
    OmniSwitch 6900 for 10/40/100 GigE Core switching
    OmniSwitch 6870/6860N/6560/E/6360 for 1 GigE or MultiGigE access / Building 1-5"
  summary: |
    参考架构：分布式环网。五个楼宇经 ERPv2（G.8032 以太环保护）组 10/40G 环，核心 OS6900
    （10/40/100G），楼宇接入可选 6870/6860N/6560-E/6360（1G 或多千兆，PoE+），服务器群 10G 直挂
    核心。接入侧 DHL 双归属 + UNP 移动性，环上故障快速收敛。适用客户：多楼宇分散园区、工厂或
    校园，光纤资源有限适合环型拓扑。
  tags: [reference-arch, erp, ring, os6900, dhl, multi-building, resilience]

- id: c13
  title: 10/40/100G 密集核心网络（Dense Core，两个核心/汇聚组合变体）
  type: case
  source_chapter: "p317-318"
  source_quote: |
    "Very large networks with high concentration of users on certain locations
    Network virtualized using Virtual Chassis (VC) / Widely scalable architecture
    Dual Home Link (DHL) at the access
    Reduced management point with VC technology from access to core
    OmniSwitch 9900 10/40/100 GigE core switching / OmniSwitch 6900 10/40 GigE at aggregation layer
    OmniSwitch 6860N for Multi GigE access with PoE+ & 10GigE uplinks"
  summary: |
    参考架构：密集核心（超大规模、用户高度集中）。p317 变体：OS9900 核心 + OS6900 汇聚（10/40G）
    + 6860N 多千兆 PoE+ 接入；p318 变体：OS6900 核心（10/40/100G）+ OS6870 汇聚（1/10/25G）
    + 6360/6465/6560-E 接入（最高 5G、PoE+、10G 上联）。数据中心以 10G LAG 双归属挂核心，
    VC 从接入贯穿到核心减少管理点，三速端口适配多种终端。适用客户：大型园区、总部密集办公。
  tags: [reference-arch, dense-core, vc, os9900, os6900, os6870, large-network, dhl]

- id: c14
  title: 企业 SPB LAN 核心（6860N/6865/6870/6900/9900，MPLS 风格园区服务架构）
  type: case
  source_chapter: "p319"
  source_quote: |
    "OMNISWITCH 6860N / 6865 / 6870 / 6900 / 9900 ENTERPRISE SPB LAN CORE
    MPLS styled service architecture / VLAN extensibility across campus / No STP
    Service Virtualization (ISID) for departmental isolation
    Enabling multi-tenancy on campus sites
    L3 inter-departmental routed control with VPN-lite or L3-VPN
    VXLAN support for DCI / Admin / Staff / Agent"
  summary: |
    参考架构：SPB 园区核心。核心层用 OS6860/6865/6900/9900（含 10K）组建 SPB 网络，楼宇侧
    6360/6465/6560-E/6860N 接入。按部门（Admin/Staff/Agent）用 I-SID 做服务虚拟化隔离，VLAN
    跨园区透明扩展、免 STP、部署更快；部门间 L3 互访走 VPN-lite 或 L3-VPN，VXLAN 支持 DCI。
    适用客户：需要多租户/多部门隔离的大园区、医院、政务、机场值机分区类场景。
  tags: [reference-arch, spb, isid, multi-tenancy, vpn-lite, vxlan, dci, campus-core]

- id: c15
  title: 虚拟机箱校园部署（OS6870 中型核心 + 远程 VC 楼宇接入）
  type: case
  source_chapter: "p79"
  source_quote: |
    "VIRTUAL CHASSIS - DEPLOYMENT IN CAMPUS LAN
    Mid-Size Core / Mixed 1/10/25 GigE Wire-rate Core / OS6870 / LAG
    Access: OS6360 OS6465 OS6560/E OS6575 OS6570M OS6860N OS6870
    10, 25, 40 or 100G Ethernet links based (remote VC) / 1/10/25G Eth"
  summary: |
    VC 特性章节中的部署实例：中型园区核心用 OS6870（1/10/25G 线速），各楼宇接入交换机
    （6360/6465/6560-E/6575/6570M/6860N/6870 全家族可选）通过 10/25/40/100G 以太链路做远程 VC
    （remote VC）+ LAG 上联，跨楼宇堆叠成单一管理实体。适用客户：多楼宇但运维团队小、希望
    "多台当一台管"的中型园区。
  tags: [vc, remote-vc, campus, os6870, access-layer, ease-of-management]

- id: c16
  title: 视频监控网络概念设计（Milestone VMS + SPB 骨干 + Smart Wall）
  type: case
  source_chapter: "p465"
  source_quote: |
    "IP CAMERAS / PAN TILT ZOOM CAMERAS / DETECTORS / EDGE STORAGE CAMERAS
    360 CAMERAS / AUDIO / SMART WALL / SMART CLIENT OPERATIONS
    DMZ / FIREWALL / WEB CLIENT USERS / MANAGEMENT CLIENT ADMINISTRATION
    MILESTONE VMS & PLUGINS / SURVEILLANCE NETWORK CONCEPTUAL DESIGN / SPB"
  summary: |
    视频监控方案概念设计：前端含 IP 摄像头、PTZ 云台、360 全景、边缘存储摄像头、探测器与音频；
    承载网以 SPB 做骨干；后端 Milestone VMS（Management Client 管理端 + Smart Client 操作端 +
    Event/SQL/存储服务器）与 Smart Wall 电视墙，外部访问经 DMZ 防火墙与 Web 客户端。适用客户：
    城市/园区/交通等大中型安防监控项目。
  tags: [video-surveillance, milestone, vms, spb, conceptual-design, security]

- id: c17
  title: OmniSwitch Milestone 插件功能实例（Management/Smart Client 双端管控交换机）
  type: case
  source_chapter: "p463-464"
  source_quote: |
    "XProtect Management plugin / Boost operational efficiency and improve video surveillance infrastructure security
    Add an OmniSwitch to the Management client / Retrieve switch and port related information
    Port – reset, power reset, LPS lock-unlock, PoE priority
    Test camera status and reset if needed with one click. Set PoE priority on a per camera basis
    ensuring critical devices remain powered if the power budget is exceeded"
  summary: |
    插件方案功能实例：Management Client 插件可把 OmniSwitch 加入/移出管理端、读取交换机与端口
    信息、执行端口复位/电源复位/LPS 端口锁定与 PoE 优先级设置；Smart Client 插件面向操作员，
    在端口表中查看摄像头上下线、PoE 消耗与最大可用功率，一键测试/复位摄像头，按摄像头设 PoE
    优先级保障关键设备供电，并搜索摄像头、查看交换机型号/版本/IP/位置/温度。适用客户：安防
    运维团队与集成商。
  tags: [video-surveillance, milestone-plugin, xprotect, poe-priority, port-control, ops]

- id: c18
  title: Milestone 插件支持的交换机型号清单（11 个 PoE 机型）
  type: case
  source_chapter: "p466"
  source_quote: |
    "SWITCHES SUPPORTED
    OS6360-P10 /A / OS6360-P24 PH/X / OS6360-P48 PH/X
    OS6465-P6 P12 H-P12 / OS6465-P28 / OS6465T-P12
    OS6560-P24 X4/Z8/Z24 / OS6560-P48 X4/Z16
    OS6860E P24/P48/Z8 / OS6860N P24/P48 Z/M / OS6865-P16X
    From Alcatel-Lucent Enterprise: ALE OmniSwitch and Plug-in Software / From Milestone Systems"
  summary: |
    插件方案兼容清单：6360/6465/6560/6860E/6860N/6865 共 11 个 PoE 机型（含 PH/H 高功率与
    Z 多千兆变体、OS6865-P16X 坚固型），全部为可给摄像头供电的型号。方案由 ALE 交换机+插件
    软件与 Milestone 系统两侧组成。适用场景：视频监控项目里选接入交换机时的合规对照表。
  tags: [video-surveillance, milestone-plugin, supported-switches, poe, compatibility-matrix]

- id: c19
  title: OS9900 机箱家族明星机型（9907/9912 核心机箱）
  type: case
  source_chapter: "p12-13"
  source_quote: |
    "OMNISWITCH 9907: 7 Slot Chassis based LAN Switch with 6 line card slots
    25.6 Tbps Full Duplex max switching capacity
    Internal PoE supply/ HPoE up to 75W & 802.3at support / 10800W of inline PoE power
    11-RU form factor / Up to two OS9907 can be connected using virtual chassis technology
    Core/aggregation switch / End of Row Switch / Spine-Leaf Architecture (L3 design)"
  summary: |
    产品明星机型：OS9907 七槽机箱（1 CMM/NI + 5 NI + 4 CFM + 4 电源 + 3 风扇），25.6Tbps 全双工、
    10800W 机内 PoE（HPoE 75W）、11RU，两台可组 VC；OS9912 十二槽 51.2Tbps、7920W、17.25RU，
    未来版本支持 VC。电源 PS-AC 3000W@220V / PS-DC 2500W，3+1 冗余。典型部署：融合园区核心/
    汇聚、数据中心 EoR、Spine-Leaf。适用客户：大型核心与高密度 PoE 需求。
  tags: [product-family, chassis, os9900, core-switch, hpoe, vc, spine-leaf]

- id: c20
  title: OS6900/OS6920 固定配置核心家族（10-400G 全速率）
  type: case
  source_chapter: "p15"
  source_quote: |
    "Stackable 10/25/40/100/200/400 Gig LAN switch / Sub-microsecond latency
    Up to 25.6 Tb/s of wire-rate capacity / SPB, IPv4/IPv6 routing over SPB
    Virtual Extensible LAN (VxLAN L2, VxLAN EVPN) / MPLS (VPLS EVPN)
    OS6900-X48C6: 48 fixed SFP+ (1G/10G) ports, 6 fixed QSFP28 ports
    OS6920-D32: 32-port QSFP56 400/200/100/50/40/25/10 GE"
  summary: |
    产品明星机型：OS6900 固定配置 10-100G（X48C6 48 SFP+ + 6 QSFP28；C32E 32 口 QSFP28 可裂解；
    X48C4E 自 8.9R4 起 VC 支持），OS6920-D32 新增 QSFP56 400G。亚微秒时延、25.6Tbps 容量、
    VRF/组播/IPv4/IPv6 高级路由、SPB/VXLAN L2/EVPN/MPLS、ISSU、RESTful API。典型部署：大网
    核心、数据中心 ToR/Spine。适用客户：数据中心与园区核心的高端口密度场景。
  tags: [product-family, os6900, os6920, core-switch, datacenter, evpn, vxlan, 400g]

- id: c21
  title: OS6870/OS6860N 高端多千兆接入双雄（WiFi 7 就绪 95W PoE）
  type: case
  source_chapter: "p16-17"
  source_quote: |
    "OMNISWITCH 6870: PREMIUM STACKABLE MULTIGIGABIT ETHERNET LAN SWITCH
    SPB, SPB-MS, VxLAN, MPLS VPNs* / 256-bit MACsec / WiFi 7 Ready / Full Multi-gig Support
    95W PoE (802.3bt) / High fabric capacity (up to 2 Tbps) / 2 x 200G Stacking
    OmniSwitch 6870-P48M: 48 100/1G/2.5G/5G BaseT bt PoE, 2 QSFP56 VFL/uplink ports
    OS6860N-P(H)(X)48M: 36 100/1G/2.5G BaseT bt PoE + 12 100/1G/2.5G/5G/10G BaseT bt PoE"
  summary: |
    产品明星机型：OS6870 顶级堆叠多千兆交换机（2Tbps 容量、2x200G 堆叠、P48M 48 口全多千兆
    95W、扩展槽可加 2xQSFP28 或 6xSFP56）；OS6860N 为同代稍低配（2x100G 堆叠、1Tbps 级），
    P48M/P24M 提供 5G/10G BaseT 端口。共同卖点：WiFi 7 就绪、802.3bt 95W、MACsec 256 位、
    SPB/VXLAN/MPLS、内联路由与流遥测。适用客户：新一代 L3 接入网、高密无线楼宇、ToR。
  tags: [product-family, os6870, os6860n, mgig, wifi7, 95w-poe, macsec, access-switch]

- id: c22
  title: 坚固型交换机 OS6865/OS6575（工业与户外，75W HPoE）
  type: case
  source_chapter: "p18-19"
  source_quote: |
    "OMNISWITCH 6865: ADVANCED RUGGEDIZED ETHERNET LAN SWITCH
    Up to eight switches in a virtual chassis / IEEE 1588v2: Precision Time Protocol (PTP)
    Pre-defined role templates in AG for IEDs, Cameras / Multicast Over SPB Optimizations
    Model OS6865-P16X: 8 x 10/100/1000 ports (POE+), 4 x POE+ HPoE 75W, Up to 320W PoE Budget
    OMNISWITCH 6575: -40 to +75 C / MACsec 256-bit on all ports / PRP, PROFINET / IP66/67"
  summary: |
    产品明星机型：OS6865 高级加固型（8 台 VC、1588v2 PTP、AG 内置 IED/摄像头角色模板、组播
    SPB 优化；P16X 320W PoE 预算、4 口 75W HPoE，U28X 20 口全光 SFP）；OS6575 工业型（-40~
    +75°C、IP66/67 MP16 机型、PRR/PROFINET 工业协议、快速/永久 PoE、报警干接点、DIN 导轨）。
    典型部署：工业自动化、电力交通、户外机柜、安防监控。适用客户：工业与公用事业。
  tags: [product-family, ruggedized, os6865, os6575, industrial, ptp, hpoe, surveillance]

- id: c23
  title: 城域/紧凑加固交换机 OS6570M 与 OS6465
  type: case
  source_chapter: "p20, p22"
  source_quote: |
    "OMNISWITCH 6570M: METRO ETHERNET LAN SWITCH
    OSPF, Multicast routing, VRFs, ISIS, GRE Tunneling* / IEEE 1588v2 PTP
    Edge of small-to-mid-sized networks / Service provider managed services / CPE / Fiber aggregations
    OMNISWITCH 6465: Virtual Chassis: Up to 4 switches in a local or remote stack (up to 10km)
    Industrial PoE with HPoE (60W) on all models / Fanless / Temperature -40 to +75 C"
  summary: |
    产品明星机型：OS6570M 城域以太交换机（许可制 OSPF/ISIS/PIM/VRF/GRE，12 与 U28X 全光机型，
    AC/DC 两种供电），面向中小网边缘、运营商管理业务、CPE 与光纤汇聚；OS6465 紧凑加固价值型
    （4 台本地/10km 远程堆叠、全系 60W HPoE、无风扇、-40~+75°C、热插拔冗余电源），机型
    P6/H-P12/T-P12/P28。适用客户：运营商边缘、交通信号、电力、IP 监控与户外安装。
  tags: [product-family, metro-ethernet, os6570m, os6465, hardened, cpe, fiber-aggregation]

- id: c24
  title: OS6560/E 价值型多千兆接入家族（95W 单口 PoE）
  type: case
  source_chapter: "p21"
  source_quote: |
    "OMNISWITCH 6560/6560E: Value Multi-GIG LAN switch
    1 Gig or MultiGig (1G/2.5G) port models - 5 GigE on E models
    Up to eight switches in a virtual chassis / PoE (802.3.at) and HPOE (802.3.bt) standards
    For networks with 802.11ax multi-gig APs (over the air throughput >1G) (PoE+ over 2.5G/5G access)
    Model OS6560-P24Z24: 24 x 100/1G/2,5G Base-T, POE (Up to 95W on a port), 4 x SFP+ 10G
    2 x QSFP 20G dedicated stacking ports"
  summary: |
    产品明星机型：OS6560/E 面向 WiFi 6（802.11ax）多千兆 AP 的价值型接入。P24Z24 为 24 口
    2.5G（单口最高 95W）+ 4x10G SFP+ + 2xQSFP 20G 专用堆叠；E-P48Z16 为 32 千兆 + 12 口 2.5G +
    4 口 5G 混合。8 台 VC、10G/10G 远程/20G 堆叠、MACsec、可选备份电源（与 6860 同款）、许可制
    城域特性（OSPF/组播/6x10G 上联）。适用客户：无线为主的中型园区接入与汇聚。
  tags: [product-family, os6560, mgig, value, wifi6, 95w-poe, access-switch, vc]

- id: c25
  title: OS6360 及入门家族 OS2260/OS2360（小网与桌面连接）
  type: case
  source_chapter: "p23-25"
  source_quote: |
    "OMNISWITCH 6360: Gigabit Ethernet LAN switch
    10, 24, 48 port models (PoE/non-PoE) / Fast & Perpetual PoE support
    Gigabit Ethernet switch in small networks / Provides integrated Voice/Data/Wi-Fi solution
    OMNISWITCH 2260/2360: Small and medium-sized business network solutions
    NOTE: Not sold in the USA"
  summary: |
    产品明星机型：OS6360 全功能 AOS 8 千兆家族（10/24/48 口、快充/永久 PoE、10G BaseT 与增强
    上联、无风扇型号多），定位小网与语音/数据/Wi-Fi 一体化，是 SMB 方案主力；OS2260 为独立
    L2+ 静态路由（无堆叠/无备份电源/无 10G），OS2360 为可堆叠千兆（VFL 虚拟机箱链路，SFP/SFP+
    上联），两者均为 OEM 机型且不在美国销售。适用客户：小企业、分支与桌面连接。
  tags: [product-family, os6360, os2260, os2360, smb, gigabit, entry-level, oem]
```

## 备注
- 提示中提到的"ONVIF 发现"在本书全文中未出现（grep 无匹配），未编造；书中组播优化相关内容为 SPB 的 "IP Multicast Optimization"（p102）与 OS6865 的 "Multicast Over SPB Optimizations"（p18），已并入对应条目。
- 引文均直接摘自 fulltext.md 对应页，幻灯片文字以 " / " 连接断行。
