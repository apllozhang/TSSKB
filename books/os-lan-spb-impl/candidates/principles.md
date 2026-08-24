# principles.md · 原则 / 参数 / 规则提取
# 来源: OmniSwitch LAN SPB Concepts & Implementation (DT00XTE323EN, Edition 12)
# 规则: 每条含原文引用与页码；宁多勿漏，待后续独立验证阶段筛选

```yaml
- id: p01
  title: BVLAN 五特性规则（无 STP/无源 MAC 学习/无泛洪/控制面承载体/AOS 上限 16 个）
  type: principle
  source_chapter: "p66"
  source_quote: |
    "BVLANS (BACKBONE VLAN)
    • Shortest path bridge VLAN • No spanning tree control • No source @mac learning of Customer data traffic • No flooding of unknown destination or multicast frames
    • IP interface supported on Control BVLANs to provide In-Band Management • Each B-VLAN calculates its own Shortest Path Tree
    • Control BVLAN carries IS-IS control packets • AOS support: 16 BVLANs
    -> spb bvlan 4001 admin-state enable / -> spb isis control-bvlan 4001"
  summary: |
    BVLAN 的行为边界：不跑生成树、不学客户源 MAC、不泛洪未知/组播目的帧；每个 BVLAN 独立算自己的最短路径树；控制 BVLAN 承载 IS-IS 报文并可挂 IP 接口做带内管理；AOS 最多支持 16 个 BVLAN。创建 BVLAN 用 spb bvlan N，指定控制 BVLAN 用 spb isis control-bvlan N。
  tags: [bvlan, isis, control-bvlan, limits]

- id: p02
  title: BVLAN 与 ECT 配置全网一致性原则
  type: principle
  source_chapter: "p83"
  source_quote: |
    "BVLAN configuration and ECT algorithm assignment must match on each SPB bridge to ensure proper ISIS-SPB neighbour discovery and shortest path calculations throughout the backbone SPB network.
    When creating multiple BVLANs for each node, it is best practice to use different ECT algorithm for each BVLAN to maximize the traffic distribution."
  summary: |
    每台 SPB 桥上的 BVLAN 编号与 ECT 算法指派必须完全一致，否则 IS-IS 邻居发现和 SPF 计算会出问题；最佳实践是每个 BVLAN 用不同的 ECT 算法，把流量分散到不同等价路径上（Lab 用 2000/ect 1、2001/ect 2、2002/ect 3）。p326 混合端口 Lab 重申同一条规则。
  tags: [bvlan, ect, consistency, load-balancing]

- id: p03
  title: 控制 BVLAN 只能在协议禁用时更改；BVLAN 自动禁用 STP
  type: principle
  source_chapter: "p83"
  source_quote: |
    "Control BVLAN carries the ISIS PDUs which are single tagged with the chosen BVLAN ID.
    Control BVLAN can only be changed when protocol is disabled. There is no Spanning Tree on BVLANs"
  summary: |
    更换 control BVLAN 前必须先 spb isis admin-state disable（Lab 步骤因此是先 disable 再 spb isis control-bvlan 2000）；任何 BVLAN 创建时系统自动关闭其生成树（p326 写作 "Spanning Tree is automatically disabled for any BVLAN created"）。排障时若发现控制 BVLAN 改不动，先查协议是否处于启用状态。
  tags: [control-bvlan, spanning-tree, isis, ordering]

- id: p04
  title: ECT 算法规则——16 个预定义算法按 BVLAN 顺序自动分配
  type: principle
  source_chapter: "p70"
  source_quote: |
    "All bridges use predefined ECT algorithms to calculate layer 2 congruency and symmetry for switching
    • Standard provides 16 predefined algorithms • 16 ECT -> index 1-16 • Same algorithm is used both for unicast and multicast
    • Each mask is assigned to a BVLAN ... The next available ECT ID is automatically assigned to a BVLAN when the BVLAN is created
    1 0x00 4001 ECT-MASK(1) = 0x00 → default, will pick the lowest BridgeID
    2 0xFF 4002 ECT-MASK(2) = 0xFF → will invert, pick the largest BridgeID"
  summary: |
    等价路径的最终裁定规则：metric 相同比跳数，跳数也相同则用 ECT 算法（对 BridgeID 逐字节 XOR 16 种掩码之一）打破平局，单播组播用同一算法保证同构对称。ECT-ID 无需显式配置——建 BVLAN 时自动按 1-16 顺序分配，每个掩码对应一个 BVLAN。ECT1（掩码 0x00）选最小 BridgeID，ECT2（0xFF）反选取最大，ECT3/4 混合取小再取大/取大再取小。
  tags: [ect, path-selection, tiebreak, bvlan]

- id: p05
  title: 最短路径选优顺序——先 metric、后跳数、再 ECT
  type: principle
  source_chapter: "p70"
  source_quote: |
    "SPB Link Metric Cost: Metric (Link cost) lower metric = higher priority
    Lowest Hop Count = higher priority — When multiple links have an equal cost (metric and hop count) [use ECT]
    SPB path calculations use the maximum value of the two nodes when the metric is different"
  summary: |
    SPB 路径比较的三级优先序：链路 metric 低者优先；metric 相同比总跳数；两者都相同进入 ECT 平局裁决。关键参数：链路两侧 metric 不一致时，整条链路按两侧最大值参与计算。Bridge ID = System ID（6 字节，即基 MAC）+ Priority（2 字节，默认 32768）。
  tags: [metric, hop-count, path-selection, spf]

- id: p06
  title: 链路 metric 两侧不一致时取最大值
  type: principle
  source_chapter: "p129"
  source_quote: |
    "Switch 7 -> spb isis interface port 1/1/6 metric 40
    Switch 8 -> spb isis interface port 1/1/6 metric 40
    Notes: If the SPB interface metric value is set to a different value for each side of a link, the highest metric value is applied to the entire link."
  summary: |
    调整路径代价（metric）的实验规则：想把流量从某条链路赶走，必须链路两端同时改大 metric（默认 10），只改一侧无效——两侧不同值时系统取最大值作用于整条链路。改完后 show spb isis spf bvlan X 可见 metric 与跳数变化，实验做完要把 metric 恢复 10 回到等价状态。
  tags: [metric, link-cost, isis-interface, asymmetric]

- id: p07
  title: service/ISID/BVLAN 三者的本地性与全局性规则及容量
  type: principle
  source_chapter: "p109"
  source_quote: |
    "The service number is only locally significant and can differ across different BEBs.
    The ISID number is globally significant and must match across all BEBs connecting a given service.
    The BVLAN that the service is mapped must also match across all BEBs connecting a given service.
    Different services can be mapped to different BVLANs to achieve traffic load balancing
    Each ISID can be attached to one BVLAN only."
  summary: |
    三个编号的匹配纪律：service 号只在本机有意义可不同；I-SID 全网必须一致；映射的 BVLAN 也必须一致；一个 I-SID 只能绑一个 BVLAN，把不同服务映射到不同 BVLAN 可实现流量负载分担。容量参数（p92）：AOS 每BVLAN 1024 个 I-SID、每 I-SID 4094 个 VLAN。另支持范围语法（p93）：service spb 11-13 isid 1001-1003 bvlan 4001:3 一次建三个服务（4001:3 表示从 4001 起连取 3 个 BVLAN）。
  tags: [service, isid, bvlan, consistency, capacity, ranges]

- id: p08
  title: SAP 创建规则——只能建在 access 口上，封装标识决定准入流量
  type: principle
  source_chapter: "p97"
  source_quote: |
    "A SAP is uniquely identified by the following: • Physical Ethernet port • Configured as an access port • Encapsulation identifier (ID), such as VLAN ID, Q-tag.
    SAPs can only be created on access interfaces.
    A switch can support either multiple services for one CVLAN, or one service for multiple CVLANs."
  summary: |
    SAP 语法与约束：SAP = access 端口 + 封装标识，只能在 service access port 上建。封装写法（p99）：port 1/1/3:20 单 VLAN、:0 未打标、:all 全部、:30.32 QinQ 外层.内层；同一端口可配多个不同封装的 SAP，不同 SAP 可分属不同服务。access 口可以是物理口或 linkagg（p96：service access port/linkagg）。
  tags: [sap, access-port, encapsulation, qinq]

- id: p09
  title: VLAN 转换（vlan-xlation）默认关闭、绑 IP 接口后隐式启用且锁定
  type: principle
  source_chapter: "p100"
  source_quote: |
    "-> service service_id vlan-xlation {enable | disable}
    Configuring the status of egress VLAN translation for all SAPs associated with the specified service. default: disable
    -> service access {port chassis/slot/port | linkagg agg_id} vlan-xlation {enable | disable} — default: disable"
  summary: |
    vlan-xlation 在服务级和 access 口级都可配，默认全 disable；用途是两端 CVLAN 不同（如 10↔20）时在 UNI 出口改写 VLAN tag。与 L3 联动时的强规则（p163）：一旦服务绑定 IP 接口，VLAN 转换被隐式启用（show 里显示 "Vlan Translation : Y (Auto)"），且只要服务还绑着 IP 接口就不能再手动改转换状态。
  tags: [vlan-xlation, l3vpn, ip-interface, defaults]

- id: p10
  title: L2 Profile 控制帧默认处理动作表
  type: principle
  source_chapter: "p115"
  source_quote: |
    "L2 Protocol Default Treatment: STP Tunnel / 802.1X Drop / 802.1AB Drop / 802.3AD Peer / GVRP Tunnel / AMAP Drop / MVRP Tunnel
    Peer: Interact with the peer switch according to the protocol; Drop: discards unconditionally the specified PDU; Tunnel: Control packet encapsulated across the provider network"
  summary: |
    静态 access 口默认套 def-access-profile：STP/GVRP/MVRP 隧道穿越、802.1X/LLDP(802.1AB)/AMAP 丢弃、LACP(802.3AD) 对等交互；动态 UNP 口默认套 unp-def-access-profile（STP drop、802.1X peer，见 p134 表）。802.1AB 可按 tagged/untagged 分别设动作（p117）。自定义：service l2profile <name> <proto> {tunnel|peer|drop}，再 service access port X l2profile <name> 挂到口上。
  tags: [l2-profile, control-frames, stp, lldp, lacp, defaults]

- id: p11
  title: SAP 的 CoS 分类原则——分类只发生在边缘
  type: principle
  source_chapter: "p118"
  source_quote: |
    "SPB uses Class of Service (CoS) mechanism • Traffic is classified at the SAP level
    Highest priority assigned to untagged tunnelled L2 Control BPDUs
    • No further classification within the SPB backbone due to MAC-in-MAC encapsulation
    Tagged traffic: CoS marking from incoming VLAN tag onto BVLAN tag
    Untagged traffic: the port's default priority is used
    Trusted SAPs: Set the CoS marking to a user-defined value / Untrusted SAPs"
  summary: |
    QoS 设计要点：流量分类只在入 BEB 的 SAP 完成，进入骨干后因 MAC-in-MAC 封装不再重分类；打标流量把客户 VLAN tag 的 802.1p 搬到 BVLAN tag，未打标流量用端口默认优先级；隧道化未打标的 L2 控制 BPDU 给最高优先级；Trusted SAP 信任入标记，Untrusted SAP 可强制改写为用户定义值。
  tags: [qos, cos, sap, 8021p, classification]

- id: p12
  title: LBD 环路检测机制与关键定时器
  type: principle
  source_chapter: "p120"
  source_quote: |
    "Periodically sends out frames from all loopback detection enabled ports • Based on specific multicast frames
    D-MAC: ALU proprietary MAC 0x01-20-DA-02-01-71 • S-MAC: Individual Port MAC
    Actions: Port shutdown / Trap / Event log / Port recovery: Automatically after a configurable timer or manually
    Global LBD Transmission Timer : 10 sec, Global LBD Auto-recovery Timer : 300 sec"
  summary: |
    LBD（环回检测）用私有多播目的 MAC 0x01-20-DA-02-01-71 周期发包，检测到环路后关闭端口并发 trap/记日志；默认发送定时器 10 秒（Lab 环境显示 30 秒）、自动恢复定时器 300 秒。配置三件套（p121）：loopback-detection enable（全局）、loopback-detection service access port X enable（端口）、show loopback-detection statistics port X。不需要 STP/RSTP/MSTP。
  tags: [lbd, loopback-detection, timers, access-port]

- id: p13
  title: IS-IS 接口默认 P2P；multi-access 的 DIS 选举规则与优先级默认 64
  type: principle
  source_chapter: "p229"
  source_quote: |
    "-> spb isis interface port 2/1 type multi-access
    -> spb isis interface linkagg 5 priority 90 — Default: 64
    DIS: Highest interface priority; Tiebreaker: highest @BMAC ... No DIS backup; New DIS election without significant disruption (3s)
    Configuring a P2P and a multi-access network interfaces on the same switch is supported."
  summary: |
    SPB 网络口默认类型是 P2P（每口一个邻接）；跨共享网（运营商以太网/微波 PMP/另一 SPB 域）时改为 multi-access（每口多邻接），同一台交换机可混合两种类型。DIS 选举按接口优先级最高者（默认 64），同分取 B-MAC 最大者；无 DIS 备份，重选约 3 秒完成。Hello 报文除 P2P TLV 外加 priority 和 LAN ID（p227）。
  tags: [isis, multi-access, dis, priority, adjacency]

- id: p14
  title: Overload 状态机制——人为引导流量绕行
  type: principle
  source_chapter: "p130"
  source_quote: |
    "The Overload state mechanism allows ISIS-SPB to inform its neighbors that the ISIS instance is nearing or exceeding its capabilities. When peers see that a switch is advertising in this state, they will select an alternate path around the overloaded switch.
    -> spb isis overload timeout 120 ... -> spb isis overload-on-boot [timeout seconds]"
  summary: |
    Overload 用法两条：①维护中把某台核心"软隔离"——spb isis overload timeout N 让邻接节点在 N 秒内绕开它（重启/下电前引流，目标直连流量除外）；②spb isis overload-on-boot 让设备重启后先处于 overload 一段时间，等 LSDB 同步完再承载穿越流量。Lab 用永久 ping 验证切换无感。
  tags: [overload, isis, maintenance, traffic-engineering]

- id: p15
  title: 组播模式配置层级——服务级/全局 head-end|tandem，tandem 细分逐 BVLAN
  type: principle
  source_chapter: "p145"
  source_quote: |
    "Multicast mode can be specified on a per I-SID basis or globally
    Same multicast mode is used across all nodes for a given SPB BVLAN
    -> service spb [service_id|all] multicast-mode [head-end | tandem]
    -> spb isis bvlan bvlan_id tandem-multicast-mode {sgmode | gmode}
    Tandem Multicast mode is specified on a per BVLAN basis; All ISIDs on the bvlan will use the same tandem mode configured for the bvlan."
  summary: |
    组播模式的配置纪律：head-end/tandem 可逐服务（service spb X multicast-mode）或全局（all）配置；同一 BVLAN 上所有节点必须用同一模式。tandem 的子模式（S,G 或 *,G）逐 BVLAN 配（spb isis bvlan N tandem-multicast-mode sgmode|gmode），该 BVLAN 上所有 I-SID 共用。
  tags: [multicast-mode, head-end, tandem, sgmode, gmode]

- id: p16
  title: SPBM 组播组 B-MAC 的编码规则
  type: principle
  source_chapter: "p142"
  source_quote: |
    "SPBM Group MAC addresses are derived from of B-DA unicast address and I-SID information
    • I/G (multicast bit) = 1 • U/L (local bit) = 1 • SPB type = 00
    • SPSourceID == 20-bit 'short-form' node ID • I-SID == 24-bit I-component identifier.
    2c:fa:a2:05:cd:71 → 53:cd:71:00:07:09 (I-SID 1001, BVLAN 4001): I-SID encoded as last 3 octets; Last 3 Octets of B-DA encoded as 1st 3 octets"
  summary: |
    Tandem (S,G) 模式下组播 B-MAC 的推导公式：源 BEB 单播 B-DA 的末 3 字节翻转到目的地址前 3 字节，I-SID（1001→0x0007:09 形式）编码进末 3 字节，首字节两位（I/G=1、U/L=1）标记为本地管理组地址，SPB 类型 00。掌握该编码可在 show spb isis multicast-table 里直接反推源节点与 I-SID；SPSourceID 是 20 位短节点 ID。
  tags: [multicast, bmac, group-mac, spsourceid, isid-encoding]

- id: p17
  title: IPMS（IP 组播优化）必须逐服务显式启用
  type: principle
  source_chapter: "p145"
  source_quote: |
    "-> ip multicast service service_id admin-state enable
    Enable SPB IP Multicast at service level to all BEBs
    IPMS must be explicitly enabled or disabled for each SPB service."
  summary: |
    不开 IP 组播 snooping 时，所有组播控制/数据流量会无差别泛洪到服务的全部 SAP 和 SDP 隧道；开启 ip multicast service X admin-state enable 后按 IGMP/MLD 代理逐服务抑制泛洪、只复制给订阅客户端，节省骨干带宽。支持 IPv4/IPv6(MLD)、Querier 转发、零基查询、欺骗/换台/健壮性控制（p143）。
  tags: [ipms, igmp, mld, snooping, multicast, flooding]

- id: p18
  title: SPB 内联路由 IP 接口三条硬规则
  type: principle
  source_chapter: "p163"
  source_quote: |
    "When creating an IP interface for an SPB service:
    • An SPB service with the specified ID must exist in the switch configuration
    • VLAN translation is implicitly enabled when a service is assigned to an IP interface regardless of whether or not VLAN translation is enabled for the service
    • Both an IPv4 and IPv6 interface can be assigned to the same SPB service as long as both interface types are in the same VRF instance."
  summary: |
    ip interface <name> address A/M service <id> 建内联 L3 接口的前置与副作用：①对应 service ID 必须已存在；②绑定的瞬间 VLAN 转换被隐式启用（与手工设置无关），且绑定期间不可改（见反例条目）；③IPv4 与 IPv6 接口可绑同一服务，但必须同属一个 VRF。接口地址即绑定 VRF 到 SPB 服务的网关地址（p160）。
  tags: [inline-routing, ip-interface, vlan-xlation, vrf]

- id: p19
  title: UNP 分类规则七级优先序
  type: principle
  source_chapter: "p267"
  source_quote: |
    "UNP Port classification rule precedence
    1. – MAC address + VLAN tag 2. – MAC address 3. – MAC address range + VLAN tag 4. – MAC address range
    5. – IP address + VLAN tag 6. – IP address 7. – VLAN tag"
  summary: |
    UNP 口同时配多条分类规则时的命中顺序：MAC+VLAN 最精确者优先，其后纯 MAC、MAC 段+VLAN、MAC 段、IP+VLAN、纯 IP，最后才是 VLAN tag。规则语法 unp classification {mac-address|mac-range|ip-address|vlan-tag} ... profile1 <name> [profile2] [profile3]。设计策略时把长尾场景交给 vlan-tag 兜底、精细终端交给 MAC/IP 规则。
  tags: [unp, classification, precedence, rules]

- id: p20
  title: UNP System Default 动态服务编号计算公式与可调参数
  type: principle
  source_chapter: "p275"
  source_quote: |
    "Default SPB Service ID number Calculation: Service ID number: 32768 incremented by 1 for each additional dynamic service (SPB or VXLAN); Multicast Mode: head-end; VLAN translation: enabled
    Default I-SID number Calculation: 10,000,000 + (Domain ID * 10,000) + (Vlan Tag % 512)
    Default BVLAN number to use: BVLAN index (Calculated I-SID number %8)"
  summary: |
    动态服务的三个确定性公式：Service ID 从 32768 递增（多租户场景可用 unp system-default service-base 改基数、service-mod 改模数，默认 10,000,000/512，见 p279）；I-SID = 10,000,000 + 域 ID×10,000 + (VLAN tag mod 512)；BVLAN 用 I-SID mod 8 做索引在已建 BVLAN 列表取值（例：2 个 BVLAN 4015/4016 时取 4015）。自动创建的服务默认 head-end 组播、vlan-xlation 使能。不想自动建可用 unp port X dynamic-service none 关闭。
  tags: [unp, system-default, isid-calculation, service-base, service-mod]

- id: p21
  title: 多未打标 SAP（multi-untag-sap）的支持范围与用途
  type: principle
  source_chapter: "p271"
  source_quote: |
    "-> unp multi-untag-sap
    Enable multiple untagged users; Classification of different untagged users to the same UNP dynamic untagged SAP
    Supported only for UNP dynamic SAPs. Available on: 6860N, 6900-V72, 6900-X48C6/T48C6/X48C4E, 6900-V48C8, 6900-C32/32E, 6900-T24C2/X24C2"
  summary: |
    同一 UNP 口进来多台未打标设备（IP 话机+PC、或 Hub 下多终端）需要分流到不同服务时，全局开启 unp multi-untag-sap，允许多个未打标用户按分类规则落到同一动态未打标 SAP/不同服务。两个硬约束：只支持 UNP 动态 SAP（静态 SAP 不行），且只有列出的新硬件平台支持。
  tags: [unp, multi-untag, dynamic-sap, platform-support]

- id: p22
  title: 持久 SAP 与 MAC 移动性（mac-mobility）——静默设备与 VRRP 场景
  type: principle
  source_chapter: "p272"
  source_quote: |
    "Use Case: Silent Device
    -> unp profile silent map service-type spb tag-value 100 isid 1004 bvlan 4002
    -> unp port 5/1/1 profile silent -> unp profile silent mac-mobility
    A persistent SAP does not age out ... Up to eight SPB service profiles per UNP port"
  summary: |
    两级保障：①unp port X profile <name> 静态指派 profile，生成的持久 SAP 不老化，适合静默设备（设备 MAC 老化后业务仍在）；每口最多挂 8 个 SPB 服务 profile。②unp profile <name> mac-mobility（需先全局 unp mac-mobility，p273）使能 MAC 移动性，典型用途是 VRRP 主备间通告不中断——主备选举报文依赖持久不老化的 SAP 传递。p286-287 Lab 用静默设备（打印机类）验证 flush 后 SAP 仍存活。
  tags: [unp, persistent-sap, mac-mobility, silent-device, vrrp]

- id: p23
  title: ERP/SPB 互操作约束清单
  type: principle
  source_chapter: "p242"
  source_quote: |
    "• Only two ERP type NNI associations are allowed per SVLAN
    • Configuring an ERP ring on 802.1q tagged port associations with SVLANs is not allowed
    • Configuring an ERP ring on an STP type NNI association with an SVLAN is not allowed
    • BEB cannot be a RPL node • RPL port shall not be configured on SPB network • RPL port cannot be configured as a SAP neighbour
    • SPB Service associated with the ERP Service VLAN has to be configured in the Control BVLAN"
  summary: |
    ERP 环过 SPB 的六条铁律：每 SVLAN 最多两个 ERP 型 NNI 关联；环不能建在 802.1q tag 口或 STP 型 NNI 关联上；BEB 不能当 RPL 节点、RPL 口不能在 SPB 网内也不能做 SAP 邻居；承载 ERP 服务 VLAN 的 SPB 服务必须配在控制 BVLAN 上。多环共享底网时各环 VLAN 范围（含服务 VLAN）必须互斥、服务 ID 不能跨环延伸。
  tags: [erp, constraints, rpl, svlan, control-bvlan]

- id: p24
  title: 混合接入端口（Hybrid）——一口双角色
  type: principle
  source_chapter: "p315"
  source_quote: |
    "Hybrid SAP and Bridge Port Hybrid access port feature allows a single port to function both as an access port and a bridging port
    Hybrid configured port: a bridge port with a default VLAN and tagged VLAN for bridging; a SAPs for services with mapped tagged VLANs.
    -> service access port 1/1/3-10 hybrid enable"
  summary: |
    AOS 8.9.R03 起，一个口可同时做桥端口（默认 VLAN+tag VLAN 走普通 VLAN 域）与业务接入口（SAP VLAN tag 流量进服务域），聚合交换机下联口不用再分两个物理口。开/关命令 service access port X hybrid enable|disable。分类发生在入口：SAP VLAN 打标流量按服务处理，常规打标/未打标流量按 VLAN 域桥接（p324 图解）。
  tags: [hybrid-port, access-port, bridging, 89r3]

- id: p25
  title: E-Tree 服务的 Leaf/Root 语义与版本约束
  type: principle
  source_chapter: "p318"
  source_quote: |
    "SAPs are designated as either leaf SAP or Root SAP
    A leaf SAP cannot communicate with another Leaf SAP in the service spanning multiple BEBs whereas Leaf SAP to Root SAP traffic is allowed. Root SAPs can communicate to all Leaf SAPs and Root SAPs.
    Note: Conventional SAPs are called Root SAPs. Note: As of 8.9.R03, all SAPs created for E-Tree service are only of type Leaf"
  summary: |
    E-Tree 提供有根多点（P2MP）连接，实现 SAP 级客户间隔离（PVLAN on SAP）：Leaf↔Leaf 不通、Leaf↔Root 与 Root↔Root 全通，区别于 E-LAN 的任意互通。配置 service X spb isid N bvlan V e-tree enable 或 UNP profile 的 e-tree 选项（p321）。关键版本约束：8.9.R03 起新建 E-Tree 服务的 SAP 全部为 Leaf 型；Root 侧需在同 I-SID 的对端 BEB 上以普通（非 e-tree）服务形态出现（p319 Lab 即这样配）。
  tags: [e-tree, leaf, root, isolation, 89r3]

- id: p26
  title: mac-ping 的固定超时与目标限制
  type: principle
  source_chapter: "p147"
  source_quote: |
    "Mac-ping: Proprietary ping
    • The timeout for each ping request packet is 1 sec. (not configurable)
    • Destination MAC cannot be a broadcast, multicast, or NULL address
    -> mac-ping dst-mac e8:e7:32:a4:77:7d vlan 4015"
  summary: |
    mac-ping 按目的 B-MAC + BVLAN 验证转发面：每请求包超时固定 1 秒不可调；目的 MAC 不能是广播/组播/空地址（所以必须先从 show spb isis info 拿对端 B-MAC）。完整语法含 priority/drop-eligible/count/interval/size/isid-check 可选项。
  tags: [mac-ping, oam, timeout, restrictions]

- id: p27
  title: SAA SPB 自动探测默认参数集
  type: principle
  source_chapter: "p150"
  source_quote: |
    "SPB creation parameters:
    Auto-create: Enabled, Auto-start: Enabled, Interval(minutes): 1,
    Jitter Threshold (us): 100, RTT Threshold (us): 500,
    Payload-Size (bytes): 32, Num-pkts: 5, Inter-pkt-delay: 1000, Keep: Disabled"
  summary: |
    saa spb auto-start 的默认值：每 1 分钟一轮、每轮 5 包、包间隔 1000us、载荷 32 字节、RTT 阈值 500us、抖动阈值 100us。自动为每个 BVLAN-B-MAC 对建会话（LAG 目的会遍历所有成员链路）；历史统计写 /flash/network/saa.xml（文件名/周期可配）。验收时看 show saa statistics aggregate 的 RTT/Jitter min/avg/max 与丢包。
  tags: [saa, oam, defaults, thresholds, statistics]

- id: p28
  title: SPB IS-IS 运行参数默认值（计时器/优先级/GR）
  type: principle
  source_chapter: "p76"
  source_quote: |
    "BridgePriority = 32768 (0x8000) ... SPF Wait = Max: 1000 ms Initial: 100 ms Second: 300 ms,
    LSP Lifetime = 1200, LSP Wait = Max: 1000 ms, Initial: 0 ms, Second: 300 ms,
    Graceful Restart = Enabled, GR helper-mode = Enabled, Control Address = 01:80:c2:00:00:14 (AllL1)"
  summary: |
    show spb isis info 暴露的节点级默认参数：桥优先级 32768；SPF 抑制等待（100/300/1000ms）与 LSP 生成等待；LSP 生存期 1200 秒；GR 与 GR helper 默认开启；协议控制目的 MAC 01:80:c2:00:00:14（AllL1，p69）。接口级（p75）：默认 metric 10、Hello 9 秒、Hello 乘数 3（hold=27s）、P2P 优先级不适用、multi-access 优先级默认 64（可到 127）、CSNP 间隔 10 秒。
  tags: [isis, timers, defaults, graceful-restart, spf]

- id: p29
  title: DHL（双归属链路）组成与限制
  type: principle
  source_chapter: "p250"
  source_quote: |
    "The Dual-Home Link (DHL) is an AOS feature on access switches. DHL provides fast failover between core and edge switches without implementing Spanning Tree.
    A DHL Active-Active configuration consists of: A DHL session. Only one session per switch is allowed. Two DHL links associated with the session (link A and link B). A physical switch port or a logical link aggregate (linkagg) ID are configurable as a DHL link. A group of VLANs ... A VLAN-to-link mapping that specifies which of the VLANs each DHL link will service."
  summary: |
    接入交换机双上联两台 BEB 且不跑 STP 的方案：每交换机仅一个 DHL 会话，会话含 link A/link B 两条（物理口或 linkagg）；VLAN 池同时 tag 到两条链路，再用 vlan-map 指定每条链路服务哪些 VLAN（如 LinkB 只跑 VLAN 40）；mac-flushing raw 触发切换时清 MAC。Lab 配置（p251）：dhl 1 → dhl 1 linka port 1/1/7 linkb port 1/1/8 → dhl 1 vlan-map linkb 40 → dhl 1 mac-flushing raw → dhl 1 admin-state enable。
  tags: [dhl, dual-home, access, failover, no-stp]

- id: p30
  title: 伪线（Pseudo-wire）服务行为规则
  type: principle
  source_chapter: "p94"
  source_quote: |
    "E-LINE connection between two local SAPs or between two SAPs across the SPB network. Also known as SPB Point-to-Point Transparent Circuit
    • Transparent packets forwarding • No source @mac learning on the SAP • Head-end multicast mode • No Flooding and replication
    -> service 100 spb isid 1000 bvlan 4000 pseudo-wire enable description "Pseudo-wire for ISID 1000""
  summary: |
    伪线 = SPB 上的点对点透明电路（E-LINE）：两 SAP 间透明转发，自动关闭 MAC 学习，强制 head-end 组播，无泛洪复制。配置在 service spb 命令上加 pseudo-wire enable（可带 remote-node <对端 B-MAC>，p236）；反向改回 E-LAN 用 pseudo-wire disable（恢复 MAC 学习）。适合电路仿真/基站回传类业务。
  tags: [pseudo-wire, e-line, transparent-circuit, mac-learning]

- id: p31
  title: VPN-Lite 回环口配置准则（VRF↔I-SID 用 VLAN ID 协调）
  type: principle
  source_chapter: "p175"
  source_quote: |
    "• Each VRF must have a single IP interface on the routing side of the loop back tied to a specific VLAN not used on other ports.
    • In the VPN Lite version there can actually be multiple IP interfaces tied to different I-SID per VRF (but two VRF cannot share the same ISID).
    • There is a corresponding SAP on the other side of the loopback tied to the correct I-SID using the same VLAN as its identifier.
    • VRRP can also be configured per interface on the loopback to allow two or more BEB to act as redundant routers ... VRRP hellos are sent across the PBB network"
  summary: |
    老平台 VPN-Lite 的回环对规则：路由侧每个 VRF 的 IP 接口绑一个专属 VLAN（别处不可用），对侧 SAP 用同一 VLAN 标识挂到正确 I-SID；一个 VRF 可有多个接口对应不同 I-SID，但两个 VRF 不能共享同一 I-SID；路由侧可跑路由协议或直接做主机网关，VRRP 通告可穿越 PBB 网实现多 BEB 冗余网关。
  tags: [vpn-lite, loopback, vrf, isid, vrrp]

- id: p32
  title: 控制 BVLAN 带内管理与 spb-mgmt 路由重分发原则
  type: principle
  source_chapter: "p67"
  source_quote: |
    "• IP interface on the Control BVLAN
    • ISIS-SPB protocol for: Advertising IP routing in the IP BVLAN domain; Mapping MAC-to-IP addresses -> No ARP packet
    -> spb isis control-bvlan 4001
    -> ip interface "spb-mgmt" address 172.30.1.1/24 vlan 4001"
  summary: |
    带内管理三件套：在控制 BVLAN 上建 IP 接口（每台 BEB/BCB 一个管理地址），ISIS-SPB 直接在 BVLAN 域内通告该 IP 路由并做 MAC-IP 映射（免 ARP）；出域流量靠静态路由（ip static-route 0.0.0.0/0 gateway <BEB IP>）或动态路由，并可用 ip redist <ospf> into spb-mgmt / ip redist spb-mgmt into <ospf> [all-routes|route-map] 双向重分发（p68）。p304 Lab 用 172.30.1.x/24 vlan 2000 为 OV2500 纳管铺路。
  tags: [in-band-management, control-bvlan, spb-mgmt, redistribution]

- id: p33
  title: VRRP over SPB 的优先级分工配置模式
  type: principle
  source_chapter: "p169"
  source_quote: |
    "Switch 1 -> ip vrrp 2 interface L3vpnvlan2 priority 200 / -> ip vrrp 2 interface L3vpnvlan2 address 192.168.2.254 / -> ip vrrp 2 interface L3vpnvlan2 admin-state enable
    Switch 2 -> ip vrrp 2 interface L3vpnvlan2 priority 100 ...
    2 L3vpnvlan2 Master ... 3 L3vpnvlan3 Backup"
  summary: |
    双 BEB 网关冗余的标准打法：每 SVLAN 一个 VRID，两台各配 .1/.2 物理地址 + 同一个 .254 虚地址，优先级交叉（S1: vlan2=200/vlan3=100，S2 相反）实现网关负载分担。验证 show ip vrrp（State Master/Backup）+ show ip vrrp statistics；故障演练时持续 ping 同时断上联。p221 示例另含 preempt interval 100 version v3 参数。
  tags: [vrrp, redundancy, gateway, priority, load-sharing]

- id: p34
  title: UNP 动态 SAP 的平台能力与 quarantine 限制
  type: principle
  source_chapter: "p262"
  source_quote: |
    "Dynamic SAPs supported from UNP service profiles
    Device assignment to an SPB service profile / Automatic SAP creation / Quarantine Manager support * / LPS support
    * Redirecting quarantined users learned on UNP access ports for remediation is not supported"
  summary: |
    UNP 口（unp port X port-type access）相对静态 access 口的能力差异：支持从服务 profile 动态生成 SAP、终端经认证/分类自动归入 profile、支持 LPS；Quarantine Manager 有星号限制——UNP 接入口上学到的被隔离用户不能被重定向去做补救（remediation）。规划 NAC 时需绕开该限制。
  tags: [unp, dynamic-sap, quarantine, limitations]

- id: p35
  title: SNMP 被纳管参数准则（用户名/安全模式/团体映射）
  type: principle
  source_chapter: "p309"
  source_quote: |
    "Notes: The username string cannot be "admin", "diag", or "user". A unique username must be used.
    -> aaa authentication snmp local
    -> user snmpuser password "Superuser=1" read-write all no auth
    -> snmp security no-security
    -> snmp community-map public user snmpuser enable
    -> snmp community-map mode enable
    -> snmp station 192.168.100.107 snmpuser v2 enable
    -> snmp-trap absorption enable"
  summary: |
    交换机被 OV2500 发现/纳管的 SNMP 准备序列：SNMP 认证走本地库；建读写用户（用户名禁用 admin/diag/user 三个保留字）；snmp security no-security 同时接受 v1/v2/v3；community-map 把 public 团体映射到该用户并全局使能映射模式；station 指定 trap 接收地址（OV 的 IP）；可开 trap absorption 让 OV 集中呈现告警。
  tags: [snmp, ov2500, aaa, community-map, station]
```
