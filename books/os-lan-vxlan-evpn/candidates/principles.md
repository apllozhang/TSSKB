# principles.md · 原则 / 参数 / 规则提取
# 来源: OmniSwitch LAN VxLAN/EVPN Concepts & Implementation (DT00XTE325EN, Edition 01)
# 规则: 每条含原文引用与页码；宁多勿漏，待后续独立验证阶段筛选

```yaml
- id: p01
  title: VXLAN 封装参数规则（UDP 4789 / 50 字节开销 / 24bit VNI / 1600 万网络）
  type: principle
  source_chapter: "p31"
  source_quote: |
    VXLAN FRAME FORMAT - Virtual L2 VPN over L3
    • Frame transport at L2 across an IP routed network
    • MAC over UDP packet encapsulation method
    • UDP port 4789 by default
    VXLAN header: • 50 bytes of overhead • Include 24 bit VXLAN Identifier • 16 M logical networks
    • Source IP address= local node's VTEP address • Destination IP address= remote node's VTEP address
  summary: |
    VXLAN 报文五要素：外层 UDP 目的端口默认 4789；VXLAN 头开销 50 字节（做 underlay MTU 规划时必须预留，p186 重申）；VNI 24bit 支持 16M 逻辑网络（对比 VLAN 12bit/4096，p164）；外层源 IP=本端 VTEP 地址、目的 IP=远端 VTEP 地址（即 Loopback0）。帧格式定义来自 RFC 7348（p29）。
  tags: [vxlan, encapsulation, udp-4789, mtu, vni, 24-bit]

- id: p02
  title: 设备身份原则——VTEP/Spine/Leaf 一律以 Loopback0 标识
  type: principle
  source_chapter: "p33, p79"
  source_quote: |
    VTEP OVERVIEW: • An entity that initiates and or terminates VXLAN tunnels • May support many VNI
    • Identified by the Loopback0 IP address
    [Lab] Configure the router ID for both OSPF and BGP overlay. • This will be the same as the Loopback0 address.
  summary: |
    VTEP 身份=Loopback0 IP（p33）；OSPF router-id 与 BGP router-id 都直接复用 Loopback0 地址（p79、p188 步骤 1/2）。Lab 取值惯例：Spine-1=1.1.1.10、Spine-2=1.1.1.11、Leaf-1=1.1.1.1、Leaf-2=1.1.1.2（p79）；架构指南取 1.1.1.1/1.1.1.2（Spine）+1.1.1.10/20/30/40（Leaf，p188-192）。BGP update-source 也统一指向 Loopback0（p85）。
  tags: [loopback0, vtep, router-id, identity, convention]

- id: p03
  title: Underlay 收敛最佳实践六条（单区域 OSPF / P2P / BFD / ECMP / 调优 / MTU）
  type: principle
  source_chapter: "p80, p186"
  source_quote: |
    - Use a single-area OSPF configuration to limit the SPF flooding domain.
    - Use point-to-point OSPF network type between the switches with routed VLAN-based IP interfaces. This eliminates DR election wait times.
    - Using BFD for fast-convergence and failure detection on the OSPF-enabled interfaces
    - Set OSPF SPF delay and hold timers to 0 to trigger SPF calculation immediately after failed interface events.
    [p186] - ECMP for efficient multi-pathing - MTU should be considered in your underlay to allow for overhead of the VXLAN header.
  summary: |
    OSPF underlay 标准参数包：单区域（缩小 SPF 泛洪域）；互联口用 router VLAN 口且 OSPF 网络类型 point-to-point（省掉 DR 选举等待）；BFD 毫秒级检测（Lab 参数 transmit/receive/echo-interval 均 200，且 ip ospf bfd-state enable）；SPF delay/hold 都设 0（接口故障立即重算）；ECMP 多路径分担；underlay MTU 预留 VXLAN 头 50 字节。架构指南版另加 debug ip ospf set subsecond 1 / bfdsubsecond 1（p189）。
  tags: [ospf, best-practice, bfd, point-to-point, spf-timer, ecmp, mtu]

- id: p04
  title: eBGP underlay 的 AS 规划规则（Spine 共享单 AS、每 Leaf 唯一 AS）
  type: principle
  source_chapter: "p60"
  source_quote: |
    • For BGP underlay use eBGP
    • Spine nodes share a single AS
    • Each Leaf node has unique AS
    AS65001 AS65002 AS65003 AS65004 [Leaf] / AS65000 AS65000 [Spine]
  summary: |
    若选 BGP 做 underlay（ISIS/OSPF/BGP 三选一，p60）：必须用 eBGP；AS 编号规则是所有 Spine 共用一个 AS（示例 AS65000），每台 Leaf 分配全局唯一 AS（示例 AS65001-65004），配合 ECMP 在 Spine 间分流。注意与 overlay 的区别：overlay iBGP 全网同一个 AS 65000（p84）。
  tags: [underlay, ebgp, as-number, spine, leaf, ecmp]

- id: p05
  title: iBGP EVPN overlay 配置五要素（同 AS / EVPN 地址族 / loopback 邻居 / update-source / activate-evpn）
  type: principle
  source_chapter: "p84-85"
  source_quote: |
    - Load and enable BGP. Set the ASN to be the same for all the switches.
    - Enable the EVPN advertisements for the BGP routing process.
    - Configure the iBGP peering sessions with the loopback interfaces. Set the "update-source" as the loopback interface.
    - Activate EVPN capability for each peer in BGP.
    ip load bgp / ip bgp autonomous-system 65000 / ip bgp address-family evpn
    ip bgp neighbor 1.1.1.10 remote-as 65000 / update-source Loopback0 / activate-evpn / admin-state enable
  summary: |
    overlay iBGP 固定套路：全网同一 ASN（65000）；ip bgp address-family evpn 全局开 EVPN 通告；邻居地址用对端 Loopback0；update-source Loopback0；每个邻居逐条 activate-evpn 才会交换 EVPN NLRI；邻居与全局都要 admin-state enable。EVPN 地址族编码：AFI=25（L2VPN）、SAFI=70（EVPN）（p51）。验证看 show ip bgp neighbors 的 "Neighbor evpn = advertised"（p86）。
  tags: [bgp, ibgp, evpn, address-family, activate-evpn, overlay]

- id: p06
  title: EVPN 业务实例默认参数（MTU 9194 / VPN IP-MTU 1500 / Hybrid / Proxy-Arp Ena / Unknown-Mac-Route Ena）
  type: principle
  source_chapter: "p67"
  source_quote: |
    EVPN Service Detailed Info
    Service Id : 100, EVI : 1000,
    Multicast-Mode : Hybrid, Service Type : VxLAN, Allocation Type : Static
    MTU : 9194, VPN IP-MTU : 1500
    BGP-EVPN : Ena, Mac-Advertisement: Ena, Proxy-Arp : Ena
    Unknown-Mac-Route: Ena, Mac-Vrf-Hw-Lrng : Dis
  summary: |
    service X vxlan vnid Y bgp-evpn enable 创建后的出厂默认：业务 MTU 9194（underlay 需满足）、VPN 内 IP-MTU 1500；组播模式 Hybrid；MAC 通告、Proxy ARP、Unknown-Mac-Route 默认启用；MAC-VRF 硬件学习默认关闭（对应 on-demand 按需导入模型，p184）；分配类型 Static。业务/EVI/VNI 三元映射示例：service 100 ↔ EVI 1000 ↔ vnid 1000 ↔ SAP 1/1/7:10（ETag=10）（p67/p69）。
  tags: [service, evi, default, mtu, proxy-arp, unknown-mac-route, hybrid]

- id: p07
  title: AOS 接入默认行为——物理口默认单归属、LAG 口默认 MH single-active
  type: principle
  source_chapter: "p102, p198"
  source_quote: |
    As part of the AOS EVPN model for simplicity:
    • single-homing is activated by default for physical access port
    • ESI Type multi-homing single-active is activated by default for link aggregation port
  summary: |
    AOS 简化模型的两条默认：物理 service access port 自动按单归属（SH）处理并自动生成 ESI；链路聚合口（LACP）自动按 ESI 多归属 single-active（MH-SA）处理。show service evpn ethernet-segment 中的类型标志对应为 SH[L-A]/SH[R] 与 MH-SA[L-A]/MH-SA[R]（p145/p154），L=本地 R=远端 A=自动 M=手工。静态 LAG 例外：必须手工提供 ESI（p156/p199，见 ce08）。
  tags: [single-homing, multi-homing, default, esi, lag, access-port]

- id: p08
  title: 非对称 IRB 全实例化原则（所有交换机所有业务 + operational 端口）
  type: principle
  source_chapter: "p105, p109"
  source_quote: |
    Since we will be using asymmetric IRB in this configuration example, it is required to have all the services instantiated in all the switches and to have an operational physical or logical port provisioned for all services.
    [p109] Currently, host based Asymmetric IRB model is supported in AOS, in which the IRB interface performs routing only on the ingress PE. In case of asymmetric IRB, the services are stretched to all the access PEs
  summary: |
    非对称 IRB 的硬性前提：每个 EVI 必须在所有交换机（含 Spine）实例化，且每业务都要有一个 operational 的物理/逻辑端口——Spine 没有真实业务口，须用 dummy 口占位（Lab 用 1/1/24，设计指南用 1/1/48）。AOS 实现的是 host-based 非对称 IRB：路由只发生在入端 PE 的 IRB 接口。对称 IRB 无此要求（业务只配有主机的 PE）但 8.10R1 不支持（p179）。
  tags: [asymmetric-irb, instantiation, dummy-port, spine, prerequisite]

- id: p09
  title: DAG 网关编址规则（统一 .254 网关 + anycast 虚拟 MAC 00:00:5E:00:01:XX）
  type: principle
  source_chapter: "p99, p109"
  source_quote: |
    • Default gateway IP address is the same for all hosts connected to different leafs
    • All hosts will have .254 as a default gateway (not dedicated as a duplicate IP address)
    • Anycast gateway has a virtual MAC address in addition to a hardware one
    ip anycast-gateway-mac auto
    ip interface leaf1svc100 anycast-gateway-address 192.168.10.254
    By default, a virtual MAC is (autogenerated) 00:00:5E:00:01:XX, XX = virtual router ID
    EVPN RT2 advertises both, hardware and virtual MAC address.
  summary: |
    分布式任播网关三规则：①所有 Leaf 上同一 EVI 的网关 IP 相同（Lab 惯例统一用 .254），是"任播地址"而非重复地址冲突；②ip anycast-gateway-mac auto 自动生成虚拟 MAC，格式 00:00:5E:00:01:XX（XX=虚拟路由器 ID）；③RT2 同时通告硬件 MAC 和虚拟 MAC。Anycast MAC 需按 VRF 设置，同一 VRF 所有子网 anycast 接口共用一个虚拟 MAC（p179/p202）。VM 的默认网关就填这个 anycast IP（p187 规划表）。
  tags: [dag, anycast-gateway, virtual-mac, default-gateway, 254, rt2]

- id: p10
  title: Proxy ARP 默认启用与四个参数项
  type: principle
  source_chapter: "p110"
  source_quote: |
    Enabling the proxy ARP will check for the local proxy-ARP cache and generates an ARP reply if target IP is found, otherwise those ARP requests will be flooded in the targeted EVPN service. By default, Proxy ARP is enabled for an EVPN enabled service.
    show service 100 proxy-arp config:
    arp-suppression: complete, flood-unknown-unicast-suppression: discard,
    unicast-forward: disable, arp-probe: enable
  summary: |
    EVPN 业务默认开启 Proxy ARP：先查本地 proxy-ARP 缓存，命中直接代答（ARP 抑制），未命中才在业务内泛洪。验证命令 show service <id> proxy-arp config 的四个默认值：arp-suppression=complete、flood-unknown-unicast-suppression=discard、unicast-forward=disable、arp-probe=enable（p110/p203 同款输出）。表项来源：ARP/GARP、DHCP snooping、IPv6 ND 或静态配置（p177 ARP Extended Community 节）。查表用 sh ip evpn proxy-arp evi <id>，统计用 show ip evpn proxy-arp summary（p203-204）。
  tags: [proxy-arp, arp-suppression, default, verification, bum]

- id: p11
  title: EVPN 路由类型 RT1-RT8 总表（含 RFC 出处与用途）
  type: principle
  source_chapter: "p52"
  source_quote: |
    Type 1 Ethernet Auto-Discovery (AD) Route, RFC 7432: multihoming, aliasing (load-balancing), backup path, split-horizon, mass withdraw.
    Type 2 MAC/IP Advertisement Route, RFC 7432: end-host MAC reachability and optionally host IPs; ARP suppression/proxy ARP; L2VPN.
    Type 3 Inclusive Multicast Ethernet Tag (IMET), RFC 7432: VTEP location per-VNI, automatic discovery, BUM replication.
    Type 4 Ethernet Segment (ES) Route, RFC 7432: discover VTEPs on same shared ES, DF Election.
    Type 5 IP Prefix Route, RFC 9136: IP prefix + next-hop, L3VPN, external connectivity.
    Type 6 SMET, RFC 9251: IGMP/MLD proxy, (*,G)/(S,G). Type 7/8 IGMP/MLD Join/Leave Synch, RFC 9251.
  summary: |
    EVPN NLRI 八种路由类型速查表：RT1（以太网自动发现，多归属场景：aliasing/备份路径/水平分割防环/批量撤销快收敛）；RT2（MAC/IP 通告，主机可达性+ARP 抑制）；RT3（IMET，按 VNI 的 VTEP 自动发现+BUM 复制）；RT4（ES 路由，发现同 ES 对端+DF 选举）；RT5（IP 前缀，L3VPN/外联，RFC 9136）；RT6/7/8（SMET 与 IGMP/MLD 同步，RFC 9251）。基础路由通告主要用 RT1-RT4（p169 阴影标注）。架构指南 p169-174 逐条给出 NLRI 字段编码。RT1 细分：per-ES（ETag=0xFFFFFFFF，快收敛/水平分割）与 per-EVI（ETag 非零，aliasing）（p170）。
  tags: [route-types, rt1, rt2, rt3, rt4, rt5, smet, rfc7432, rfc9136, rfc9251]

- id: p12
  title: RD/RT 构造规则与 AOS 自动生成（RD=SystemIP:EVI，RT=target:AS:EVI）
  type: principle
  source_chapter: "p148, p185"
  source_quote: |
    • Route Distinguisher (RD): RD= <System IP>:<EVI>
    • Route Target (RT): RT= target:<AS number>:<EVI>
    [p185] all EVPN Route Types will use the Type-1 RD ... mostly based on the Loopback0 (Router ID) of the originating router.
    The RD value ... 8-octet: Type Field (2 Octets) + Value Field (6 Octets); for EVPN the Type Field is set to 0x1
  summary: |
    AOS 的 RD/RT 自动生成公式（p148 例：RD=1.1.1.10:100，RT=target:65000:100）：RD=系统 IP（Loopback0/Router ID）:EVI；RT=target:AS 号:EVI。RD 为 8 字节 Type-1 格式（RFC 4364/RFC 7432），值字段含 Loopback0(4B)+对象类型(3bit)+对象 ID(13bit)，对象类型分 service/ESI/prefix 三种（p185）。作用：RD 让不同租户/EVI 的重叠路由唯一；RT 做 MAC-VRF 的导入导出过滤，export RT 与接收方 EVI 的 import RT 匹配才导入（p175）。ES-Import RT 特殊：6 字节、自动从 ESI 编码、加在 RT4 上确保只有同 ES 的 PE 导入（p176-177）。
  tags: [rd, rt, auto-generation, type-1-rd, mac-vrf, import-export, multi-tenant]

- id: p13
  title: ETag 三种服务模型与 AOS 的 hybrid 实现
  type: principle
  source_chapter: "p175-176, p185"
  source_quote: |
    • VLAN-based Service Model: one-to-one mapping, each VLAN to a dedicated MAC-VRF, VNI, EVI ... Ethernet Tag ID in all EVPN routes MUST be set to 0.
    • VLAN Bundle Service Model: many-to-one ... single broadcast domain, MAC addresses must be unique ... VLAN translation is not allowed and the Ethernet Tag ID MUST be set to 0.
    • VLAN-aware Service Model: many-to-one, multiple switching tables, separate VNIs ... Ethernet Tag ID will be set according to the VLAN ID(s) configured in the SAP.
    [p185] AOS EVPN implements a hybrid of VLAN bundle and VLAN aware bundle service model.
  summary: |
    RFC 7432 三种 ETag 服务接口模型：VLAN-based（VLAN:MAC-VRF:VNI:EVI 一对一，可 VLAN 翻译，ETag 恒 0）；VLAN bundle（多 VLAN 共享一个广播域/MAC 必须唯一，ETag 恒 0，不允许 VLAN 翻译）；VLAN-aware（一个 MAC-VRF 多张交换表、每 VLAN 独立 VNI/广播域，ETag=SAP 的 VLAN ID）。AOS 实现的是 VLAN bundle 与 VLAN-aware 的混合体（p176/p185），ETag 取 SAP 关联的 VLAN ID（如 SAP 1/1/7:10 → ETag 10，p107 sap-info），按 ETag 级别做路由汇总撤收。
  tags: [etag, service-model, vlan-based, vlan-bundle, vlan-aware, hybrid, aos]

- id: p14
  title: MAC mobility 序列号规则与环回保护三参数
  type: principle
  source_chapter: "p127, p177"
  source_quote: |
    When the MAC address is first advertised, it includes the MAC mobility extended community with a sequence number of 0. When the host moves ... it sends a new R-T2 with the MAC mobility extended community with an incremented sequence number of 1. Eventually, the old PE ages out the R-T2 with the lower sequence number, and the PEs retain the R-T2 with the highest sequence number.
    [p127] service bgp-evpn mac-mobility loop-protection {enable | disable} (retry-time [seconds] | threshold [count] | timeout [seconds])
  summary: |
    主机移动机制：RT2 携带 MAC mobility 扩展团体属性，首次通告序列号=0；MAC 换位置后新 PE 用序列号+1 重新通告，各 PE 保留最高序列号的 RT2、老化低序列号旧表项（亚秒收敛）。防 MAC 抖动：全局命令 service bgp-evpn mac-mobility loop-protection（retry-time 秒/threshold 次数/timeout 秒三参数，在所有 Leaf 上配，p127/p204）；检测到 timeout 内移动次数达 threshold 即判定 MAC duplication，将该 MAC hold-down 并停止收发其 BGP MAC 路由，retry-time 到期后解禁重启检测（p177）。
  tags: [mac-mobility, sequence-number, loop-protection, retry-time, threshold, timeout]

- id: p15
  title: BUM 复制两机制——头端复制（HER）与 Tandem 组播（PIM-BIDIR）
  type: principle
  source_chapter: "p40-42, p180"
  source_quote: |
    2 mechanisms: • Head end replication • Tandem multicast
    [HER, p41] One copy of each frame is sent to each known remote VTEP with a unicast IP header
    [Tandem, p42] Refers to standard IP multicast. In the case of the AOS gateway is PIM-BIDIR. In VXLAN, one multicast group is used per VNI.
    [p180] Head-end or ingress replication using EVPN R-T3 ... Only ingress (head-end) replication is supported in the initial release 8.10R1
  summary: |
    BUM 流量两种复制方式：①头端复制=入端 VTEP 给每个已知远端 VTEP 逐份单播（EVPN 下用 RT3 IMET 自动发现建 ingress replication list，同 PE 多 VNI 共享隧道，p180）；②Tandem=标准 IP 组播，AOS 网关用 PIM-BIDIR（RFC 5015，双向共享树、免源状态、IPv4/IPv6 双栈，p42-43），每个 VNI 一个组播组。8.10R1 首版 EVPN 只支持 ingress replication（p180 注）。VXLAN 网关下每 VNI 创建时分配组播地址，ARP/BOOTP/DHCP 都按 BUM 处理（p40）。
  tags: [bum, head-end-replication, tandem, pim-bidir, imet, rt3, multicast]

- id: p16
  title: DF 选举规则（service carving / EVI mod N / 默认抢占）
  type: principle
  source_chapter: "p182-183"
  source_quote: |
    A DF is elected after ESI member discovery using R-T4 is performed to avoid duplicate BUM flooding in multi-homing scenarios. In single-active multi-homing, one DF is elected per ESI ... In all-active multi-homing, the DF is only responsible to forward BUM traffic to the CE while unicast traffic can be forwarded based on LACP hashing.
    The default procedure for DF election is referred to as "service carving". ... The default algorithm used is a modulo-based algorithm, which is DF = EVI mod N, where N is the number of PEs in the candidate list. By default, the DF election is pre-emptive.
  summary: |
    DF（指定转发者）选举：RT4 发现同 ES 成员后进行，避免 BUM 重复泛洪。single-active 下每 ESI 选一个 DF 负责 BUM+单播；all-active 下 DF 只管 BUM、单播按 LACP 哈希。算法细节：默认过程叫 service carving；候选列表（R-T1 收齐后排序）上按 DF = EVI mod N 取模；可以每 VLAN 一个 DF 分摊 BUM（多 DF）；默认抢占式——候选 PE 列表变化即重算。验证：show service evpn ethernet-segment <esi> sap-info 输出中带 * 的是 DF；carving-info 显示 EVI→DF/nDFs 映射（p200-201）。
  tags: [df-election, service-carving, modulo, pre-emptive, multihoming, rt4]

- id: p17
  title: AOS ESI 编码规则（Type 0x3 MAC-based 两种格式）
  type: principle
  source_chapter: "p142, p184-185"
  source_quote: |
    ESI ... A network-wide 10-byte unique identifier of an ES
    AOS (auto-generated) ESI model:
    03:Access port MAC(6):ff:ff:ff for physical access port
    03:CE-MAC(6):ff:<Key-Id>(2) for LACP ports
    [p184] All the ESI generated by AOS nodes will be based on Type 0x3 (MAC address-based) ESI as specified in the RFC 7432.
    Type Field (1 Octet) / MAC Address (6 Octets) / Local Discriminator (3 Octets)
  summary: |
    AOS 自动 ESI 一律用 RFC 7432 Type 0x3（基于 MAC），10 字节=Type(1)+MAC(6)+本地标识(3)：物理接入口格式 03:<端口MAC(6)>:ff:ff:ff（如 03:78:24:59:2b:32:b8:ff:ff:ff）；LACP 口格式 03:<CE-MAC(6)>:ff:<Key-Id(2)>（如 03:2c:fa:a2:a2:f2:ad:00:03:00，admin-key 3 体现在 Key-Id 00:03:00，p143/p154）。生成范围表（p185）：物理口=自动、LACP LAG=自动、静态 LAG=仅手工。ESI 的 2-7 字节还可用作 ES route-target（p142）。ESI 全网唯一，多归属 CE 各端必须一致（手工 ESI 场景，Lab 用 esi 01:01:01:02:04，p156）。
  tags: [esi, type-0x3, auto-generation, lacp, static-lag, key-id, rfc7432]

- id: p18
  title: VXLAN 地址学习规则（每 VNI 一个虚拟桥 / SAP-SDP 虚端口 / 可禁学习）
  type: principle
  source_chapter: "p38"
  source_quote: |
    Each VNI has a virtual bridge instance (service) created for it in AOS
    • All SAPs and SDPs associated with a VNI have a virtual port created for them
    • MACs that are received from local SAPs or on SDPs associated with remote VTEPs are learned on their corresponding virtual ports
    Learning can be disabled, in which any unknown MAC address (SA or DA) is dropped
    The VTEPs participating in a VNI can be learned through the SDP creation and bind commands, or can be learned dynamically
  summary: |
    AOS VXLAN 数据面学习模型：每个 VNI 对应一个虚拟桥（service 实例）；本端 SAP 和指向远端 VTEP 的 SDP 都表现为虚拟端口；MAC 按普通学习流程记在对应虚端口上并按 MAC DA 查表桥接。远端 VTEP 可静态（SDP creation/bind）或动态学习。风险提示：学习可被禁用，此时任何未知 MAC（源或目的）直接丢弃。EVPN 下远端 MAC 经 RT2 学到、挂 sdp:32768 虚端口（sh mac-learning evpn-vxlan 输出，p73/p116）。
  tags: [mac-learning, virtual-bridge, sap, sdp, virtual-port, learning-disable]

- id: p19
  title: 冗余接入选型——Virtual Chassis vs EVPN Multi-homing
  type: principle
  source_chapter: "p187"
  source_quote: |
    Virtual Chassis: Simple to configure and maintain / Faster convergence (data plane-based) / LACP-based configuration on hypervisor
    EVPN Multi-homing: Complex for configuration and troubleshooting / Slower convergence (control plane-based) / Static bonding configuration on hypervisor
  summary: |
    主机/虚拟化接入双归属的两种方案对比：VC（虚拟机箱）配置维护简单、数据面收敛快、hypervisor 侧用标准 LACP；EVPN 多归属配置排障复杂、控制面收敛较慢、hypervisor 侧要用静态 bonding。选型逻辑：小规模/单机房优先 VC，跨 leaf 扩展/多租户场景用 EVPN MH。p206 结论另提 ALE 服务定义网络全家桶（VC、动态服务、零信任、UNP）可与 EVPN 组合。
  tags: [virtual-chassis, multihoming, redundancy, selection, convergence, lacp]

- id: p20
  title: AOS on-demand 原则——只有"在用"地址才进硬件 FDB
  type: principle
  source_chapter: "p184"
  source_quote: |
    Only in-use addresses are imported into the data-plane, which allows for high scalability. This means that while a discovered source may be distributed to all the participating nodes of the EVPN network and maintained in the BGP RIB, it is only imported to the data-plane when there is a lookup for the end-host (destination)
    AOS EVPN uses an on-demand model which helps to vastly improve the FDB scalability and convergence of the data-plane by avoiding having to store in the hardware FDB any unused host entries.
  summary: |
    AOS EVPN 的 FDB 策略：控制面路由（BGP RIB）全网分发，但数据面只在真正发生对该目的主机的查找时才导入硬件表项——避免硬件 FDB 存储从未被使用的表项，大幅提升 FDB 容量利用与收敛。配套默认值：业务视图 Mac-Vrf-Hw-Lrng=Dis（p67），即硬件 MAC-VRF 学习默认关闭，与该模型一致。实施含义：sh mac-learning evpn-vxlan 看到的表项少于 BGP RT2 路由数属正常现象，不代表路由缺失（用 debug evpn show bgp route-type rt2 对比，p117/p205）。
  tags: [on-demand, fdb, scalability, mac-vrf, bgp-rib, convergence]

- id: p21
  title: EVPN 通信两流程——同子网 8 步 / 跨子网 6 步（假设非对称 IRB）
  type: principle
  source_chapter: "p181-182"
  source_quote: |
    [Intra-subnet] 1. The source host sends an ARP request ... 2. the ingress PE ... consults its ingress replication list ... floods the frame ... 3. learns the source host MAC ... advertised using R-T2 ... 6. the destination ... responds with an ARP reply ... 8. This destination host MAC address is also stored by the local PE and sent to remote PEs as a R-T2 update.
    [Inter-subnet] the host sends an ARP request for the DGW ... the local PE ... will route the packet from the source IRB interface to the destination IRB interface ... encpasulates the packet with the VXLAN header
  summary: |
    架构指南给的标准转发流程。同子网（proxy ARP 表为空时）8 步：ARP 广播→入 PE 查 ingress replication list 封装泛洪→入 PE 学源 MAC 发 RT2→远端 PE 写 MAC-VRF→远端解封向同广播域 SAP 泛洪→目的主机单播 ARP 应答→本地 PE 查表封装转发→目的 MAC 同样入表并 RT2 通告；此后单播直达。跨子网（非对称 IRB）6 步：主机 ARP 网关 IRB→PE 回 IRB MAC→主机发帧（目的 MAC=IRB）→入 PE 查 MAC-VRF 后查 IP-VRF 从源 IRB 路由到目的 IRB→查目的 MAC-VRF 封 VXLAN 转发→远端 VTEP 解封查 MAC-VRF 交付。
  tags: [intra-subnet, inter-subnet, forwarding, flow, irb, rt2, arp]
```
