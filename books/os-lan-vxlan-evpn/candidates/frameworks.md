# frameworks.md · 框架 / 流程提取
# 来源: OmniSwitch LAN VxLAN/EVPN Concepts & Implementation (DT00XTE325EN, Edition 01)
# 规则: 每条含原文引用与页码；宁多勿漏，待后续独立验证阶段筛选

```yaml
- id: f01
  title: EVPN 五步配置法总框架（Underlay→Overlay→Service Access→Service→SAP）
  type: framework
  source_chapter: "p59"
  source_quote: |
    EVPN CONFIGURATION STEPS – PART 1/5
    Steps for Configuring EVPN on Overlay Service
    [步骤图依次为] Underlay Configuration / Overlay Configuration / Service Access / Service / SAP
  summary: |
    AOS EVPN 实施总路线图，同一张步骤图在 p59/p62/p66/p68 逐段展开：①Underlay 配置（L3 路由底座）；②Overlay 配置（MP-BGP EVPN）；③Service Access（接入口启用以太网段）；④Service（EVPN-VXLAN 业务实例化）；⑤SAP（业务接入点绑定 VLAN）。Part 1/5（p56-75）讲完五步主线；Part 2/5 加 IRB/DAG（p90）；Part 3/5 加 MAC 学习/Proxy ARP/MAC mobility（p119）；Part 4/5 加路由反射器（p130）；Part 5/5 加多归属与 RD/RT、路由类型附录（p139-149）。三个 Lab（p76-158）与架构指南配置示例（p187-204）均按此主线展开。
  tags: [evpn, vxlan, configuration, five-steps, framework, aos]

- id: f02
  title: 五步法之 Step1——Underlay 配置流程与路由协议选型
  type: framework
  source_chapter: "p60"
  source_quote: |
    EVPN CONFIGURATION STEPS
    • Layer 3 protocols: ISIS, OSPF, BGP
    • Spine and Leaf/PE) are identified by the Loopback0 interface
    • Support for ECMP to balance traffic between Spine nodes
    • For BGP underlay use eBGP
    • Spine nodes share a single AS
    • Each Leaf node has unique AS
  summary: |
    Underlay 三选一（ISIS/OSPF/BGP）；每台 Spine/Leaf 用 Loopback0 作为身份标识；靠 ECMP 在多条 Spine 链路间分担流量；若用 BGP 做 underlay 则必须 eBGP 且 AS 规划为"所有 Spine 共享一个 AS、每台 Leaf 独有 AS"（p60 图示 AS65000 vs AS65001-65004）。课程 Lab 与架构指南均选 OSPF underlay + iBGP overlay 推荐组合（p186 原文 "The recommended topology to be used is an OSPF underlay with iBGP overlay"）。具体执行顺序：Loopback0→router-id→互联 VLAN 路由口→BFD→OSPF 接口（p2p+bfd-state）→全局启用（p61、p188-193）。
  tags: [underlay, ospf, isis, bgp, loopback, ecmp, as-planning]

- id: f03
  title: 五步法之 Step2——Overlay（MP-BGP EVPN）四步配置流程
  type: framework
  source_chapter: "p84"
  source_quote: |
    The following steps will be taken to configure it:
    - Load and enable BGP. Set the ASN to be the same for all the switches.
    - Enable the EVPN advertisements for the BGP routing process.
    - Configure the iBGP peering sessions with the loopback interfaces. Set the "update-source" as the loopback interface.
    - Activate EVPN capability for each peer in BGP.
  summary: |
    Overlay 配置四步：①ip load bgp 并设全网统一 AS（Lab/设计指南均为 65000）；②ip bgp address-family evpn 打开 EVPN 地址族通告；③对每个邻居按 Loopback 建 iBGP 会话（neighbor <对端Loopback> remote-as <本AS> + update-source Loopback0）；④逐邻居 activate-evpn + admin-state enable，最后全局 ip bgp admin-state enable（完整 CLI 见 p63/p85-86/p193-197）。验证标准：show ip bgp neighbors 显示 Oper state=established 且 Activate evpn=enabled、Neighbor evpn=advertised（p86/p197）。
  tags: [overlay, bgp, evpn, ibgp, address-family, update-source]

- id: f04
  title: 五步法之 Step3-5——业务开通三部曲（Access Port→VXLAN Service→SAP）
  type: framework
  source_chapter: "p67, p69"
  source_quote: |
    -> service access port 1/1/7 evpn-ethernet-segment enable
    -> service 100 vxlan vnid 1000 bgp-evpn enable
    -> service 100 sap port 1/1/7:10
  summary: |
    Overlay 就绪后三条命令开通一条 L2 EVPN 业务：①把物理口声明为 service access port 并启用 evpn-ethernet-segment（自动生成 ESI，单归属 SH 模式，p64-65）；②service <id> vxlan vnid <vni> bgp-evpn enable 创建虚拟桥（示例 service 100↔VNI/EVI 1000，p67）；③service <id> sap port <端口>:<VLAN> 挂 SAP，冒号后为客户 VLAN（即 ETag，p69）。对端 Leaf 重复同样三条（p71 "Configure the same on remote PE (VTEP)"）。Spine 默认不建业务（p104 Total Services: 0）；只有在非对称 IRB 场景才用 dummy 口补建（p105）。
  tags: [service, sap, vxlan, vnid, evi, access-port, provisioning]

- id: f05
  title: Part2/5——IRB 选型框架（非对称 vs 对称路由）
  type: framework
  source_chapter: "p91"
  source_quote: |
    Asymmetric Routing vs Symmetric Routing:
    Ingress PE performs MAC and IP lookup / Egress PE performs only MAC lookup
    No need for routed VXLAN / Routed VXLAN needed
    Every PE must have full ARP table for all hosts (Proxy) / All MAC vrfs have to be created on all PEs although no host present
    Based on RT2 updates, no need for RT5 / RT5 support mandatory
    Simpler to implement / More complex, 4 flavors; Less scalable / More scalable
  summary: |
    跨子网路由两种模型决策表：非对称=入端 PE 一次完成 L2 查找→IRB 路由→再 L2 查找到目的 VNI，出端只做 MAC 查找；无需 routed VXLAN；所有 PE 必须全量 ARP 表和全量业务；只依赖 RT2；实现简单但扩展性差。对称=两端都做 MAC+IP 查找；需要 routed VXLAN，RT5 强制、host route 必开；业务只配有主机的 PE；更可扩展但有 4 种实现变体。AOS 当前支持 host-based 非对称 IRB（p109/p201），对称 IRB 的配置入口是 fabric-vpn 服务（p97：service 50 vpn-type fabric-vpn + vrf 1 ip interface ... service 50），但 8.10R1 首版不支持（p179 注）。
  tags: [irb, asymmetric, symmetric, routing, model-selection, rt2, rt5]

- id: f06
  title: Part3/5——EVPN MAC 学习与 Proxy ARP 三段流程
  type: framework
  source_chapter: "p121-124"
  source_quote: |
    [EVPN MAC LEARNING 1/3-3/3 流程图]
    ARP request → (Leaf1 本地学习并泛洪 VXLAN)
    RT2 - Used to advertise end-host MAC reachability information between VTEPs and optionally host IPs.
    Route Reflectors re-advertised this info to all Leaf nodes.
    [PROXY ARP full process] (1) RT2 (MAC) (2) RT2 (Mac, IP) / ARP request for 10.2 → ARP flooded → RT2 MAC by Leaf1 / Snoop IP by leaf 1 / RT2 IP-MAC by Leaf 1 → ARP Response from client 6
  summary: |
    控制面学习三步（p121-123）：①源主机 ARP 广播→入 PE 按 ingress replication list 泛洪并在本地 MAC-VRF 学源 MAC；②PE 发 RT2（仅 MAC，或经 GARP/DHCP snooping 学到 IP 后发 MAC+IP）经 RR 转发给所有 Leaf，对端写入 MAC-VRF——全程无数据面泛洪学习；③目的主机 ARP 应答单播返回，两端都有表项。Proxy ARP（p124/p110）：PE 收 ARP 先查本地 proxy-ARP 缓存，命中直接代答（ARP suppression），未命中才在 EVPN 业务内泛洪；默认启用。验证：sh mac-learning evpn-vxlan / show service X proxy-arp config / sh ip evpn proxy-arp evi X。
  tags: [mac-learning, rt2, proxy-arp, arp-suppression, control-plane, mac-vrf]

- id: f07
  title: Part4/5——路由反射器（RR）架构框架
  type: framework
  source_chapter: "p132, p136"
  source_quote: |
    ROUTE REFLECTORS - OBJECTIVE
    Without Router Reflectors, N Leafs require N*(N-1)/2 session
    For example, having 10 routers will result in 10(10-1)/2 = 45 peerings.
    [RESUME] RR is useful for scalability and redundancy in networks. ... Usually, spine switches can be used route reflectors.
  summary: |
    BGP EVPN overlay 的规模化解法：全互联 iBGP 会话数=N(N-1)/2（10 台 45 会话），引入 RR 后 Leaf 只与 RR 建会话、RR 间再互联。三类节点：Route reflector / Client / Non-client（p133）；冗余形态：单集群单 RR 与单集群双 RR（p134）。RR 侧专属命令：ip bgp client-to-client reflection、ip bgp cluster-id <id>、neighbor <ip> route-reflector-client（p135）。实践惯例：Spine 直接兼任 RR（p136；Lab 拓扑中 Spine 承担 RR 转发 RT2/RT3，p122 "Route Reflectors re-advertised this info to all Leaf nodes"）。
  tags: [route-reflector, bgp, scalability, cluster-id, spine, full-mesh]

- id: f08
  title: Part5/5——EVPN 多归属框架（两种模式+DF 选举+四特性）
  type: framework
  source_chapter: "p141, p182"
  source_quote: |
    MULTIHOMING • All-active or Single-active
    [架构指南] 1. Single-active: This redundancy mode allows active/standby connectivity with one path active at any time.
    2. All-active: This redundancy mode allows active/active connectivity of multi-homed devices. ... LAG is required to be configured between the PE switches and the multi-homed CE device. This is to avoid receiving duplicate packets and for loop prevention.
  summary: |
    CE 双归/多归多台 PE 的完整框架：两种冗余模式——all-active（主主，需 PE-CE 间 LAG 防重复包和防环）与 single-active（主备）。机制链条（p182-183）：RT4 发现同一 ES 的对端 PE→DF 选举（service carving，EVI mod N，默认抢占式）→DF 负责向 CE 转发 BUM（all-active 下单播按 LACP 哈希、single-active 下 DF 独占一切流量、非 DF 直接把口拉 down，p146）→RT1A/RT1B 支撑 aliasing、backup path、mass withdraw、split horizon 四特性。AOS 默认行为：物理口单归属、LACP 口 MH single-active（p102/p198）；8.10R1 首版仅支持 single-active（p182 注）。
  tags: [multihoming, all-active, single-active, df-election, esi, lag, rfc7432]

- id: f09
  title: EVPN Architecture Guide——EVPN 总体架构模型（痛点→VXLAN→控制面分层）
  type: framework
  source_chapter: "p164-167"
  source_quote: |
    MP-BGP EVPN is a control plane protocol for VXLAN based on RFC 7342 and RFC 8365.
    [传统模式四痛点] Inefficient use of resources (STP blocked redundant links) / Scalability issues (12-bit VLAN ID, upper limit 4096) / Operational complexity (VLANs configured at every switch) / Traffic tromboning (static first-hop router)
    MP-BGP EVPN changes this model and uses a proactive approach for end-host reachability information learning. It provides a separate control plane for VXLAN tunnels.
  summary: |
    架构指南（p159-206）的概念主线：传统 DC 的 STP+VLAN 模型四痛点（p164）→ VXLAN 数据面解耦（MAC-in-UDP、24bit VNI、16M 逻辑网络，p165）→ 学习模型对比：反应式 flood-and-learn（数据面）vs 主动式控制面学习（p166）→ MP-BGP EVPN 作为 VXLAN 的独立控制面（VTEP 发现+主机可达性通告，p167-168）。用例分层：DC leaf-spine/Clos（可上 Super-Spine 三层架构做 DCI）、Enterprise Campus Fabric（微分段/多租户/L2 WiFi 漫游，p166）。选型四收益：统一控制面（L2+L3 一套协议）、可扩展高效（多归属/aliasing/ARP 抑制/DAG/MAC mobility）、灵活性（VXLAN/MPLS/PBB 多封装、多厂商互通）、安全控制（VRF+VNI+RD+RT，p54/p167）。
  tags: [evpn, architecture, vxlan, control-plane, data-plane, use-cases, dc-fabric, campus-fabric]

- id: f10
  title: AOS EVPN 实现模型（全端口 ESI+ETag 路由+自动 RD/RT+按需导入）
  type: framework
  source_chapter: "p184-185"
  source_quote: |
    The AOS EVPN service model provides enhanced stability, better scalability, and improved convergence of BGP based EVPN network by:
    • Instantiating an ESI for any access port that is enabled for EVPN.
    • Providing high granularity, by generating the ESI+ETag aware routes.
    • Supports the auto-generation of the RD and RT for various EVPN R-T messages.
    • Only in-use addresses are imported into the data-plane ... AOS EVPN uses an on-demand model which helps to vastly improve the FDB scalability
  summary: |
    AOS 私有增强四件套（p184-185）：①任何 EVPN 使能的接入口（物理/单归属/LAG 多归属）都实例化 ESI，全部走 EVPN 控制面 FDB 管理，使企业网与 DC 网都能部署；②ETag 模型：每个 SAP 生成 ETag（=VLAN ID）级别路由，路由撤收可按 ETag 汇总而非逐 MAC；③RD/RT 自动生成（Type-1 RD 基于 Loopback0/Router ID，p185）；④on-demand 按需导入：路由在 BGP RIB 全网分发，但只有被查找的目的主机才导入硬件 FDB，避免存无用表项。服务模型实现为 VLAN bundle + VLAN-aware 的 hybrid（p176/p185）。ESI 生成范围表：物理口自动、LACP LAG 自动、静态 LAG 必须手工（p185）。
  tags: [aos, evpn-model, esi, etag, rd-rt, on-demand, fdb, scalability]
```
