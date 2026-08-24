# frameworks.md · 框架 / 流程提取
# 来源: OmniSwitch LAN SPB Concepts & Implementation (DT00XTE323EN, Edition 12)
# 规则: 每条含原文引用与页码；宁多勿漏，待后续独立验证阶段筛选

```yaml
- id: f01
  title: SPB 配置分层总框架（控制面在 BEB+BCB，服务面只在 BEB）
  type: framework
  source_chapter: "p65"
  source_quote: |
    "SPB CONFIGURATION STEPS
    Interfaces IS-IS / Services / Control Plane (NNI ports) / SPB Core level — On BEB + BCB
    Access Port / SAP / Data Plane (UNI ports) / SPB Access level — Only on BEB
    Service: Multi Access / P2P / Pseudo-wire; L2 Profiles (optional); Loopback Detection (LBD) (optional)"
  summary: |
    全书配置主线框架：SPB 配置分两层。骨干部（SPB Core level）= BVLAN + IS-IS 接口 + 服务控制面，BEB 和 BCB 都要配；接入部（SPB Access level）= Access Port + SAP（静态或 UNP 动态）+ 可选 L2 Profile/LBD，只在 BEB 上配。p89 重复此图并加"UNP Access Port (Dynamic)/UNP Profiles (Dynamic)"分支。任何 SPB 交付都按"先骨干后服务"推进，BCB 永不感知服务。
  tags: [spb, configuration, framework, beb, bcb, control-plane, data-plane]

- id: f02
  title: SPB 骨干部署四步流程（建 BVLAN→定控制 BVLAN→配 IS-IS 接口→启用 IS-IS）
  type: framework
  source_chapter: "p83"
  source_quote: |
    "Backbone configuration entails the following tasks:
    - Creating one or more BVLANs with their associated ECT-IDs. ECT-IDs need not be explicitly defined, default ECT-IDs are applied
    - Defining the control BVLAN
    - Defining one or more SPB IS-IS interfaces
    - Enabling the SPB IS-IS protocol"
  summary: |
    Lab 1 给出的骨干预配置顺序：①每节点建 BVLAN 并（可选）指定 ECT-ID；②在协议禁用状态下指定 control BVLAN；③按物理连线把端口配成 SPB IS-IS 接口（配完自动成为 SPB network port，系统自动把所有 BVLAN 加到该口）；④全局 spb isis admin-state enable 启动发现/邻接/SPF 计算。教材明确"先配好 SPBM 再逐台启用"（p85），p326 混合端口 Lab 复用同一四步。
  tags: [spb, backbone, deployment, bvlan, isis, lab-flow]

- id: f03
  title: L2 服务开通五步流程（VLAN→Access Port→Profile→I-SID→SAP）
  type: framework
  source_chapter: "p108"
  source_quote: |
    "So, Configuration steps will be:
    1. Creating VLANs on access switches
    2. Create the Service Access Port
    3. Create the Service Access Profile (Optional)
    4. Create the Service I-SID
    5. Create the Service SAP"
  summary: |
    在已建好的骨干上开 L2 服务的标准顺序：先在接入交换机建客户 VLAN 并 tag 上联；再在 BEB 上把面向接入的端口声明为 service access port；可选建 L2 Profile；然后创建 service spb X isid Y bvlan Z 把 I-SID 映射到 BVLAN；最后用 service spb X sap port n:n:vlan 挂 SAP 定义准入流量。服务只需建在需要交付的 BEB 上，不建在 BCB 上（p108 原文："Services need only be created on BEBs, not on BCBs"）。
  tags: [spb, l2-service, provisioning, sap, isid, lab-flow]

- id: f04
  title: SPB IS-IS 验证命令序列（从 BVLAN 到 SPF 的逐层排障链）
  type: framework
  source_chapter: "p85"
  source_quote: |
    "- Check the BVLANs and the associated ECT algorithm ... -> show spb isis bvlans / -> show vlan id
    - Display the list of all the SPB interfaces ... -> show spb isis interface
    - Determine if ISIS SPB is in "UP" state ... -> show spb isis adjacency [detail]
    - Display the global ISIS-SPB status ... -> show spb isis info
    - Verify the unicast addresses learned ... -> show spb isis unicast-table bvlan 2000
    - Checks the shortest path first (SPF) information ... -> show spb isis spf bvlan 2000 [bmac <BMAC>]
    - Display information about the ISIS SPB topology database -> show spb isis database [lsp-id]
    - Display the discovered node ... -> show spb isis nodes"
  summary: |
    骨干部署后的验证/排障顺序，按"配置→接口→邻接→节点→转发表→路径→数据库"自底向上：show spb isis bvlans 查 ECT，interface 查端口类型/状态，adjacency 查邻接 UP，info 查本桥 System ID/B-MAC/控制 BVLAN，unicast-table 查每个 BVLAN 的出接口，spf 查 metric/跳数/下一跳，database/nodes 查 LSDB 与全网节点。p127-128 的故障切换实验即用 unicast-table 前后对比确认重新选路。
  tags: [spb, troubleshooting, verification, isis, show-commands]

- id: f05
  title: SPB/EVPN/MPLS 三技术定位对比选型框架
  type: framework
  source_chapter: "p31"
  source_quote: |
    "SPB: Main use case Datacenter, Campus, IoT Networks; Scalability Large; Resiliency High; Ease of deployment Simple to Moderate; Training needed Low to Moderate; Protocol Overhead Low — IS-IS only; Troubleshooting Simple & Fast.
    EVPN: Datacenter; Moderate to complex; BGP & VXLAN/MPLS; Intermediate time.
    MPLS: Service Provider & Mission critical networks; Very High; LDP, RSVP, BGP; Complex & Slow."
  summary: |
    OmniFabric 内三技术的选型矩阵：SPB 面向园区/DC/IoT，只跑 IS-IS 一个协议、开销低、部署与排障最简单；EVPN 面向大型 DC，BGP+VXLAN，复杂度中等；MPLS 面向运营商与关键业务网，弹性最高但需 LDP/RSVP/BGP 多协议栈、培训成本最高。p33 补充量化对比：MPLS 收敛 50ms/成本 $$$，SPB 收敛 100ms/成本 $$；p35 用案例矩阵（视频监控、赌场、园区、ITS→SPB；大型 DC→EVPN；铁路/轨交→IP-MPLS）落地选型。
  tags: [positioning, spb, evpn, mpls, omni-fabric, selection]

- id: f06
  title: SPB 两层 vs 三层设计拓扑框架
  type: framework
  source_chapter: "p61"
  source_quote: |
    "SPB DESIGN TWO-TIER TOPOLOGY — Core Switch: No need for BCB nodes; Backbone edge bridge (BEB) role; BEB nodes in partial or full mesh topology; VLAN to I-SID; IS-IS for MAC learning; IS-IS for SPB paths; PBB for data plane; Redundancy achieved through BEB nodes made of two or more physical chassis in VC topology. Access Switch: 802.1Q VLAN on LAG; STP or DHL towards BEB."
  summary: |
    两层设计（p61）：核心即 BEB 全互联，不需要 BCB，冗余靠虚拟机箱（VC）双机；接入交换机用普通 802.1Q VLAN 上联，向 BEB 方向跑 STP 或 DHL。三层设计（p62）：核心为 BCB 只学 B-MAC 做 PBB 转发，汇聚层 BEB 做 VLAN→I-SID 映射，冗余靠双 BCB。两图都注明远端可通过 MPLS/VXLAN 域扩展 SPB。选型依据是规模：小网两层够用，大网才引入 BCB 层。
  tags: [spb, design, topology, beb, bcb, two-tier, three-tier]

- id: f07
  title: IP over SPB 三方案递进框架（Inline 冗余→VPN-Lite→L3-VPN）
  type: framework
  source_chapter: "p156"
  source_quote: |
    "VPN Lite: A VPN Lite L3 Service is created by overlaying a L3 routing protocol on top of the L2 WAN SPB service. This routing protocol can be OSPF, BGP, or even static routing.
    L3 VPN: SPB L3 VPN leverages the existing SPB IS-IS instance to carry customer VPN routes without requiring an additional routing protocol such as OSPF. This is accomplished with additional IS-IS TLVs extensions"
  summary: |
    Day 2 的课程主线：同一 SPB 骨干上叠路由的三种做法按"是否另跑路由协议"递进——①纯 VRRP 冗余网关（ip interface ... service X + vrrp，无路由协议）；②VPN-Lite：在 L3VPN IP 接口上再跑 OSPF/BGP/静态，VRF 间靠 I-SID 打通；③L3-VPN：用 SPB IS-IS 的 IPVPN TLV 直接携带 VRF 路由，免路由协议。p199 给出选型判据（见 counter-examples/principles 条目）：L3-VPN 在简单性、扩展性、收敛三方面全面占优，VPN-Lite 适用于需与传统路由协议对接的场景。
  tags: [ip-over-spb, vpn-lite, l3vpn, vrrp, progression]

- id: f08
  title: SPB L3-VPN 路由交换四步流程（bind→export→import→redist）
  type: framework
  source_chapter: "p193"
  source_quote: |
    "Routes exchanged by importing and exporting between VRF and SPB-ISIS via GRT table
    -> spb ipvpn bind vrf default isid 4001 gateway 10.1.2.1 all-routes
    -> vrf default ip export route-map net1
    -> vrf default ip import isid 4001 route-map net3
    -> spb ipvpn redist source-isid 4001 destination-isid 4002 route-map net9"
  summary: |
    L3-VPN 配置心法四步：①spb ipvpn bind 把 <VRF, I-SID, gateway IP> 绑定，建立 VRF↔I-SID 双向通道（经 GRM/GRT 表）；②vrf X ip export [route-map] 把本 VRF 路由导出到 GRT；③vrf X ip import isid N 把远端 I-SID 路由从 GRT 导回本 VRF；④可选 spb ipvpn redist 做 I-SID↔I-SID 或 VRF→I-SID 的跨实例泄漏，全部步骤可用 route-map 过滤。p211-213 的 Lab 完整走了一遍：bind vrf default isid 2009 → route-map local-to-spb → ip export route-map → ip import isid 2009 all-routes。
  tags: [l3vpn, spb-ipvpn, bind, export, import, redistribution]

- id: f09
  title: BUM 流量分发模式选择框架（Head-End / Tandem S,G / Tandem *,G）
  type: framework
  source_chapter: "p138"
  source_quote: |
    "BUM = Broadcast Unknown Multicast — ARPs packets, Boot-p/DHCP requests, etc.
    SPBM supports two BUM traffic distribution methods for replicating and forwarding multicast frames
    • Head-End (native mode) • Tandem (optimized)"
  summary: |
    三种 BUM 复制模式的选型：①Head-End（默认，p139）：入口 BEB 复制，每目的 BEB 一份、按对端 B-MAC 单播封装，适合兴趣社区稀疏/组播带宽低的场景；②Tandem S,G（p140）：每 I-SID 每源建 (S,G) 组播树，用组 B-MAC，带宽效率高；③Tandem *,G（p141）：每 BVLAN 共享一棵树、最低 Bridge ID 节点做根，资源占用最少。p145 配置层级：service spb X multicast-mode 逐服务或全局配 head-end/tandem，tandem 细分 sgmode/gmode 逐 BVLAN 配（spb isis bvlan N tandem-multicast-mode）。
  tags: [bum, multicast, head-end, tandem, sgmode, gmode, isid, bvlan]

- id: f10
  title: UNP 动态服务创建决策流程与编号计算
  type: framework
  source_chapter: "p274"
  source_quote: |
    "Traffic received on UNP access ports that is not assigned to a configured service profile is assigned to the System Default service profile.
    Default I-SID number Calculation: 10,000,000 + (Domain ID * 10,000) + (Vlan Tag % 512)
    Default SPB Service ID number Calculation: Service ID number: 32768 incremented by 1 for each additional dynamic service (SPB or VXLAN)
    Default BVLAN number to use: BVLAN index (Calculated I-SID number %8)"
  summary: |
    UNP 动态 SAP 的自动化决策流（p274 流程图）：UNP 口收到流量→分类规则命中？→命中则按 profile 建 SAP；未命中且端口开启动态服务（unp port X dynamic-service spb）→查 SAP 是否已存在→不存在则按 System Default 规则自动建 I-SID/Service/BVLAN。三个公式：I-SID = 10,000,000 + 域 ID×10,000 + (VLAN tag mod 512)；Service ID 从 32768 起递增；BVLAN = I-SID mod 8 作为索引在已建 BVLAN 列表里取。p275 用 VLAN 412 演算出 10,000,412/4015。service-base 与 service-mod 可由管理员改（p279：unp system-default service-base/service-mod）。
  tags: [unp, dynamic-sap, system-default, isid-calculation, automation]

- id: f11
  title: OV2500 SPB 编排上线流程（VM 初始化→License→SNMP→发现→拓扑）
  type: framework
  source_chapter: "p305"
  source_quote: |
    "Turn on the Virtual Machine called "Pod#-OV2500.4xx" ... In the Snapshot Manager Window Select "OV-init" and click on Go to ...
    -> aaa authentication snmp local / -> user snmpuser password "Superuser=1" read-write all no auth / -> snmp security no-security / -> snmp community-map public user snmpuser enable / -> snmp station 192.168.100.107 snmpuser v2 enable
    -> Network -> Managed Devices -> Discover New Devices ... Start IP: 172.30.1.1 End IP: 172.30.1.8"
  summary: |
    OV2500 纳管 SPB 网的固定流程：①vSphere 里恢复 OV-init 快照并开机（预配了网络与默认 SNMPv2 但无 License）；②首次登录改密（admin/switch→Training123=!）并在 lds.al-enterprise.com 生成 EVAL-OV2500 评估 License（90 天）导入；③交换机侧配 SNMP（本地认证用户+community-map+trap station 指向 OV 地址）；④OV 里按控制 BVLAN 网段（172.30.1.1-8）建 Range List 发起发现；⑤Topology→SPB Network→Poll Latest Data 查看 SPB 拓扑，可选 BVLAN 逐个查看。前提是 SPB 带内管理已就绪（p304：控制 BVLAN 上配 ip interface spb-mgmt）。
  tags: [ov2500, orchestration, snmp, discovery, license, in-band-management]

- id: f12
  title: SPB OAM 排障流程（mac-ping 定位 + SAA 持续探测）
  type: framework
  source_chapter: "p147"
  source_quote: |
    "Mac-ping: Proprietary ping — The timeout for each ping request packet is 1 sec. (not configurable)
    sw2-> mac-ping dst-mac e8:e7:32:a4:77:7d vlan 4015
    Reply from E8:E7:32:A4:77:7D - 1/1/5 : bytes=64 seq=1 time=109us
    -> saa spb auto-start ... SAA sessions are created for each VLAN/MAC pairing. If the destination MAC is on a link aggregation group, SAA traverse all paths of the Linkaggs"
  summary: |
    两层排障工具：第一层 mac-ping——先 show spb isis info 拿对端 B-MAC，再 mac-ping dst-mac <BMAC> vlan <BVLAN> 按 BVLAN 验证转发连通与时延（每包超时固定 1 秒）；第二层 SAA——saa spb auto-start 自动为每个发现的 BVLAN/B-MAC 对建 mac-ping 会话（LAG 场景会遍历所有成员路径），按分钟级间隔持续统计 RTT/Jitter，结果写 /flash/network/saa.xml。适合部署验收（逐对测通）与长期监控（阈值告警：RTT 500us/Jitter 100us 默认阈值）。
  tags: [oam, mac-ping, saa, troubleshooting, monitoring]

- id: f13
  title: ERP/SPB 互操作部署流程（环内节点 + BEB 两侧分工）
  type: framework
  source_chapter: "p243"
  source_quote: |
    "-> erp-ring ring_id port1 {chassis/slot/port | linkagg agg_id} port2 {chassis/slot/port | linkagg agg_id} service-vlan vlan_id level level_num
    -> erp-ring ring_id rpl-node {port chassis/slot/port | linkagg agg_id}
    -> erp-ring ring_id sap-neighbor {port chassis/slot/port | linkagg agg_id}
    -> erp-ring ring_id port1 ... access-[tagged|untagged] spb-remote-system switch_mac_address service-vlan vlan_id level level_num
    -> erp-ring ring_id enable"
  summary: |
    ERP 环经 SPB 延伸的配置分工：环上普通节点配 erp-ring N port1/port2 + service-vlan + MEG level，RPL owner 节点额外配 rpl-node 与 wait-to-restore-timer，靠 BEB 的 SAP 口节点配 sap-neighbor；BEB 侧则建服务/SAP（ERP 控制 VLAN 与业务 VLAN 各挂 SAP）并用带 spb-remote-system <对端 B-MAC> 的 access-tagged 形式把环"接"过 SPB 云。Lab（p256-258）以 VLAN 30/40 业务 + VLAN 1000 ERP 服务 VLAN 演练，保护倒换用 show erp / show erp statistics 验证。
  tags: [erp, g8032, spb-interworking, rpl, sap-neighbor]

- id: f14
  title: 课程主线框架——SPB 交付生命周期（Day1 骨干→Day2 路由→Day3 自动化）
  type: framework
  source_chapter: "p6"
  source_quote: |
    "Day 1: OmniFabric Overview / Why SPB? / Shortest Path Bridging Mac-in-MAC — Lab: Deploying a Backbone network based on SPB-M technology / ... L2 services / SPB protocol Analysis and protection / BUM Traffic flows & Troubleshoot
    Day 2: IP Routing over SPB — Routing Redundancy / IP-VPN Lite / L3-VPN / SPB Advanced Configuration
    Day 3: Dynamic Services — Lab: Setting up UNP SPB Dynamic SAP / OmniVista 2500 & SPB / Hybrid SAP and Bridge Port and SPB E-Tree Services / Success Stories"
  summary: |
    三天课程的编排本身就是一条 SPB 交付方法论：Day1 从零搭骨干（BVLAN/IS-IS/SPT）、开 L2 服务、做协议分析与保护（metric/overload/LBD/L2 profile）、理解 BUM 与排障；Day2 在同一骨干上叠三层（VRRP 冗余→VPN-Lite→L3-VPN），再加高级拓扑（多接入共享网、伪线、ERP 互操作）；Day3 走自动化与运维（UNP 动态 SAP、OV2500 编排、混合接入与 E-Tree），最后用成功案例收尾。做现场交付规划时可按此顺序分期：骨干可达→L2 业务→L3 业务→自动化纳管。
  tags: [course-structure, delivery-lifecycle, spb, training]
```
