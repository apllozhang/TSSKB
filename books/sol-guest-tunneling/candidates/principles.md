# principles.md · Guest Traffic Tunnelling Services Application Note · 原则/机制/前置条件提取
# 提取范围：fulltext.md（p1-p19）
# 页码为原书 PDF 页码（<<<PAGE N>>> 真实标记）

- id: P1
  title: GTTS 基于 L2 GRE 隧道协议，实现类似 VXLAN 的二层 overlay
  type: principle
  source_chapter: "p4"
  source_quote: |
    "The GTTS is based on the L2 GRE Tunneling protocol. Layer 2 Generic Routing Encapsulation (L2 GRE)
    tunneling is a mechanism that is used to identify and isolate device traffic from the rest of the
    internal network traffic. This implementation of L2 GRE tunneling is like the OmniSwitch implementation of VXLAN"
  summary: |
    GTTS 用 L2 GRE（二层通用路由封装）在 IP 网上建二层 overlay，把设备流量与内网其余流量识别并隔离；与 OmniSwitch 的 VXLAN 实现同源思想：L2 GRE 作为 service 实现，也可关联 UNP profile。隧道两端 = AP 上的 L2 GRE endpoint + 隧道聚合交换机上的 L2 GRE endpoint。
  tags: [mechanism, l2gre, overlay]

- id: P2
  title: 交换机侧靠 Hairpin（同机两口自环）终结隧道：SAP 口出隧道、ACCESS 口落 VLAN
  type: principle
  source_chapter: "p4"
  source_quote: |
    "On the switch side, a Hairpin is necessary. This is a loop, one cable from one port is connected to
    another port on the same switch. ... o SAP port: this is where the tunneled traffic will be entered to
    go out of the tunnel. ... o ACCESS port: The ACCESS port is the other side of the Hairpin. This is a
    legacy access port where a VLAN is mapped."
  summary: |
    Hairpin = 一根线把同一台交换机的两个口连起来。SAP 口绑 service（隧道出方向），ACCESS 口是普通 access 口挂 VLAN（隧道流量最终落的 VLAN 域）。上行：AP→隧道→SAP 口→物理线→ACCESS 口→VLAN；下行反之，所有去客户端的包也必须先过 ACCESS 口进 SAP 口入隧道。
  tags: [mechanism, hairpin, sap]

- id: P3
  title: 隧道聚合交换机应部署在逻辑安全区（DMZ），隧道终点=风险最高点
  type: principle
  source_chapter: "p4"
  source_quote: |
    "Usually, the tunnel aggregation switch is deployed in a place that is logically secured, as a DMZ
    secured by one or multiple firewalls. We want a high security level at this level because this is
    where the tunnel ends, and so where the risks are the highest."
  summary: |
    隧道终点是风险最高点，聚合交换机通常放 DMZ、由一道或多道防火墙围住；访客在此只通 Internet/边界网络，病毒与恶意软件在 DMZ 内即被拦住，进不了内网。
  tags: [security, dmz, design]

- id: P4
  title: 用户流量在 SSID 关联后立即入隧道，DHCP/Portal/DNS/NTP 等服务必须从聚合交换机可达
  type: principle
  source_chapter: "p4-5"
  source_quote: |
    "The user traffic is tunneled directly after the SSID association. That means that even DHCP flows
    travel inside the tunnel. Therefore, a DHCP server must be deployed in the same area of the tunnel
    aggregation switch. ... all services like DHCP, Captive Portal, DNS, NTP, …, must be reachable from
    the tunnel aggregation switch. The best would be to have dedicated services for tunneled SSID"
  summary: |
    连 DHCP 报文都在隧道里跑，所以 DHCP 服务器必须部署在聚合交换机同区域（可用中继转发到别处，但安全角度首选专属服务器）；内置 Captive Portal 同理。最佳实践：为隧道 SSID 配专属服务集，保持高安全等级。
  tags: [services, dhcp, portal]

- id: P5
  title: 隧道粒度三级可选：全部无线流量 / SSID 级 / ARP 级
  type: principle
  source_chapter: "p3"
  source_quote: |
    "This tunnelling is flexible because it allows fine-grained selection of the specific traffic that
    needs to be tunneled: all wireless traffic, at SSID level or even at the ARP (Access Role Profile) level."
  summary: |
    GTTS 粒度灵活：可隧道全部无线流量、按 SSID、甚至按 ARP（访问角色档案）。ARP 级意味着同一 SSID 下不同设备按分类进不同隧道终点。
  tags: [granularity, arp, ssid]

- id: P6
  title: GTTS 按 AP Group 级配置，多站点流量可去不同终点或同一中心点
  type: principle
  source_chapter: "p3"
  source_quote: |
    "GTTS is configurable at the AP Group level. Because of that, wireless traffic from different sites
    can be tunneled to different points or to a central point."
  summary: |
    配置落点是 AP Group 而非单台 AP，天然支持多站点规模化：各站 AP 入同一 AP Group 即可把流量统一引到中心隧道终点（园区场景的基础）。
  tags: [ap-group, scalability]

- id: P7
  title: GTTS 天然支持多租户：多客户流量汇到同一终点仍保持逻辑隔离
  type: principle
  source_chapter: "p3"
  source_quote: |
    "GTTS is also applicable in multi-tenanted scenarios in which traffic from multiple different customers
    is concentrated on the same GTTS termination end point(s) whilst still preserving logical isolation
    between different customers."
  summary: |
    运营商场景：多客户流量集中到同一台（或多台）GTTS 终点交换机，客户之间逻辑隔离不破坏——单机多租户场景（p13）的实现基础。
  tags: [multi-tenancy, sp]

- id: P8
  title: One ARP 规则：每个 ARP 同一时刻只有一条活跃隧道；N 个隧道 SSID 需 N 台聚合交换机
  type: principle
  source_chapter: "p7"
  source_quote: |
    "Each AP can only have ONE active tunnel at a time toward ONE tunnel aggregation switch. ... if 3 SSIDs
    using the GTTS feature are broadcasted from an AP, each of them using a different Access Role Profile,
    this is mandatory to have at least 3 tunnel aggregation switches, one for each SSID."
  summary: |
    每个 SSID 映射一个 ARP，ARP 映射一条隧道，同一时刻一条隧道只能活跃在一台聚合交换机上。推论：一台 AP 广播 3 个各用不同 ARP 的 GTTS SSID，就必须有至少 3 台聚合交换机。一台 AP 可以同时与多台不同聚合交换机各建活跃隧道（每 ARP 一条）。
  tags: [constraint, one-arp, sizing]

- id: P9
  title: Layer 3 hop 前置：AP 管理 IP 不得与 GRE Tunnel Server IP 同网段
  type: principle
  source_chapter: "p7"
  source_quote: |
    "A layer 3 hop must exist between the far-ends APs and the tunnel aggregation switch. In other words,
    the management IP address of the AP must not be in the same subnet as the IP address sets as the GRE
    Tunnel Server IP while creating the SSID."
  summary: |
    AP 与聚合交换机之间必须存在三层跳变；建 SSID 时填的 GRE Tunnel Server IP 不能与 AP 管理 IP 同子网，否则隧道起不来。这是文档标注"必须遵守"的架构前置之一。
  tags: [prerequisite, l3-hop]

- id: P10
  title: Hairpin 线速封顶 SSID 带宽；增加 Hairpin 即扩容
  type: principle
  source_chapter: "p8"
  source_quote: |
    "Given that all the traffic transits through the hairpin in the tunnel aggregation switch, the maximum
    bandwidth of the SSID is capped by the hairpin bandwidth. Additional hairpin can be configured as
    explained in the Redundancy chapter also increases the maximum bandwidth used for GTTS SSIDs."
  summary: |
    全部隧道流量都过 Hairpin 物理自环线，SSID 最大带宽=Hairpin 带宽。加配多条 Hairpin（如 R1 冗余的 linkagg 做法）既提高可靠又线性提高 GTTS SSID 可用带宽。
  tags: [capacity, hairpin]

- id: P11
  title: MTU 前置：L2 GRE 封装增加 24 字节（GRE 头 4B + IP 头 20B）
  type: principle
  source_chapter: "p8"
  source_quote: |
    "Given that GTTS use the L2GRE encapsulation, a total of 24 bytes are added to the packets (4 bytes for
    GRE header + 20 bytes for IP header). An issue can occurs when the GTTS feature is used across a network
    belonging to another company."
  summary: |
    规划 MTU 时必须计入 24 字节封装开销；跨运营商/其他公司网络（如 SD-WAN/运营商链路）时要提前与对方网络管理员沟通放行略大的报文，否则会静默丢包。
  tags: [prerequisite, mtu]

- id: P12
  title: auto-discover 默认开启，使交换机动态接受远端 AP 的隧道
  type: principle
  source_chapter: "p8"
  source_quote: |
    "The Auto-discover feature allows switches to dynamically accepts tunnels for far-ends APs. Without this
    feature enabled, each far-end AP has to be manually set in the switch by adding their MAC address. By
    default, the auto-discover is enabled. ... service l2gre auto-discover enable"
  summary: |
    开局必查项：auto-discover 默认开启，用 `service l2gre auto-discover enable` 确保；关闭则每台远端 AP 都要在交换机上手工加 MAC，规模化不可行。
  tags: [cli, auto-discover]

- id: P13
  title: 单交换机隧道数上限按机型三档：1000 / 2000 / 6000，Virtual-Chassis 不抬高
  type: principle
  source_chapter: "p8"
  source_quote: |
    "The maximum number of active tunnels on a tunnel aggregation switch depends of the switch model. This
    number doesn't go up if Virtual-Chassis is used: 6900-Q32/X72 → 1000; 6860; 6860N; 6865; 6900-X/T24C2 → 2000;
    6900-V72; 6900-C32; 6900-X/T48C6; 6900-X48C4E; 6900-V48C8; 6900-C32E → 6000"
  summary: |
    选型硬指标：6900-Q32/X72 为 1000 条；6860/6860N/6865/6900-X24C2/T24C2 为 2000 条；6900-V72/C32/X48C6/T48C6/X48C4E/V48C8/C32E 为 6000 条。组 Virtual-Chassis 不增加上限，按单机档位规划。
  tags: [scalability, platform]

- id: P14
  title: 版本前置：AOS ≥8.4.1.R02、AWOS ≥3.0.2.19
  type: principle
  source_chapter: "p6"
  source_quote: |
    "The GTTS feature needs the following prerequisites: AOS release 8.4.1.R02 or greater; AWOS release
    3.0.2.19 or greater"
  summary: |
    GTTS 最低版本组合：OmniSwitch AOS 8.4.1.R02+，AP 侧 AWOS 3.0.2.19+。文档验证环境为 OS6900 系列 + AOS 8.7.98/8.9.78 GA、AP1201/AP1331 + AOS R4.0.5.2038 MR、OV2500 4.7R1（p7）。
  tags: [prerequisite, version]

- id: P15
  title: 一个 SSID 映射多个 ARP：经 Filter-id / IoT Enforcement / 设备专属 ARP 分类，各进不同隧道
  type: principle
  source_chapter: "p5, p11"
  source_quote: |
    "Through multiple ways, one SSID can be mapped to multiple ARPs ...: 802.1x authentication using Filter-id
    field, IoT Enforcement, Device specific ARP. In that case, multiple ARPs must be created and mapped to as
    many of Tunnel Profiles, which contains all the parameters to setup the L2 GRE tunnel."
  summary: |
    单 SSID 多 ARP 的三条分类途径：802.1X 的 Filter-id 字段、IoT Enforcement、设备专属 ARP。每条 ARP 各映射一个 Tunnel Profile（含建 L2 GRE 隧道全部参数）；OV2500 里需用 Expert 模式创建（p11）。效果：同一 SSID 下不同设备流量按分类去不同隧道终点。
  tags: [arp, tunnel-profile, classification]

- id: P16
  title: Preemption 机制：Primary 恢复后按倒计时回收隧道并迁移会话
  type: principle
  source_chapter: "p10, p17"
  source_quote: |
    "Preemption: enabled to have the Primary switch become Primary again at the end of the timer while the
    Secondary switch is Master. Preemption Countdown Timer: the timer which at the end the Primary switch
    become the Master of the tunnel, while the Secondary is currently the Master."
  summary: |
    R2 冗余可开抢占：Primary 不可达时隧道切到 Secondary；Primary 恢复后，倒计时到期 AP 重连 Primary 并把全部现存会话迁移回来（p17）。
  tags: [redundancy, preemption]

- id: P17
  title: Backup GRE Server IP 与 Primary 无同网段/异网段要求
  type: principle
  source_chapter: "p10"
  source_quote: |
    "Note: Primary and Backup GRE Tunnel Server IP have no requirements to be or not to be in the same IP subnet."
  summary: |
    AP 隧道配置里 Primary 与 Backup 两台聚合交换机的 IP 可以同网段也可以不同网段，无约束——给异地容灾（R4 不同地理位置）留了自由度。
  tags: [redundancy, design]
