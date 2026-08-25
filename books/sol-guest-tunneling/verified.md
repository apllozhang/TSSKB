# Verified 候选（V1 原文真实性核对 + V2/V3 抽查）

## cases

# 提取范围：fulltext.md（p1-p19）

- id: C1
  title: 交换机侧 GTTS 五步配置流程（l2profile→access port→service→sap→vlan）
  type: case
  source_chapter: "p9"
  source_quote: |
    "service l2profile "guest-l2profile" stp drop gvrp drop mvrp drop
    service access port 1/1/49A vlan-xlation enable l2profile "guest-l2profile" description "L2GRE Loopback Port"
    service 100 l2gre vpnid 50 description "guest" stats enable vlan-xlation enable remove-ingress-tag enable
    service 100 sap port 1/1/49A:50
    vlan 50 members port 1/1/50 untagged"
  summary: |
    五步：(1) 建 l2profile 并丢弃 stp/gvrp/mvrp；(2) 选 Hairpin 一侧端口应用 profile（vlan-xlation enable）；(3) 建 service，编号本机自定，VPN ID 必须与 SSID 侧一致；(4) `service "id" sap port X/X/XX:"vpn-id"` 把 service 挂到 SAP 口；(5) Hairpin 另一侧配普通 access 口挂 VLAN。例中 SAP=1/1/49A、ACCESS=1/1/50、VLAN 50（VLAN ID 与 VPN ID 一致仅为方便，不强制相同）。
  tags: [cli, switch, config]

- id: C2
  title: AP 侧 GTTS 配置：SSID 建 Use Tunnel + Tunnel ID + GRE Server IP + Preemption
  type: case
  source_chapter: "p10-11"
  source_quote: |
    "During the SSID creation, instead of choosing a VLAN to be mapped to the SSID, the option Use Tunnel must
    be checked. ... Tunnel ID: ... must be the same as configured in the switch. ... GRE Tunnel Server IP
    Address/Data VPN Server: the IP address of the tunnel aggregation switch ... Backup GRE Tunnel Server IP
    Address: the IP address of the secondary tunnel aggregation switch"
  summary: |
    建 SSID 时勾选 Use Tunnel 替代 VLAN 映射，配置面板四要素：Tunnel ID（须与交换机侧一致）、GRE Tunnel Server IP（主聚合交换机）、Backup GRE Tunnel Server IP（可选，备机）、Preemption+倒计时（可选）。单 SSID 多 ARP 场景需切 Expert 模式建多个 ARP 并各配 Tunnel Profile（p11）。Entropy 必须启用。
  tags: [cli, ap, ssid]

- id: C3
  title: 场景一：访客流量隧道到 DMZ——三区防火墙隔离基线架构
  type: case
  source_chapter: "p11"
  source_quote: |
    "The Guest SSID is mapped to a tunnel configured with the tunnel aggregation switch as the endpoint,
    located in the DMZ. A DHCP server is part of this DMZ to deliver IPs to Guests located physically in the
    Corporate block, but their first open door is in fact on the tunnel aggregation switch inside the DMZ,
    enclosed by firewalls. All viruses, malware, and security breaches thereby are ineffective."
  summary: |
    最简 GTTS 架构：网络分 Corporate/DMZ/External 三区，各由防火墙分隔；Guest SSID 隧道终点=DMZ 内聚合交换机，DHCP 也在 DMZ。访客人虽在 Corporate 区，"第一扇门"开在 DMZ，病毒/恶意软件被防火墙挡住，只能出 Internet。
  tags: [scenario, dmz, guest]

- id: C4
  title: 场景二：Campus 园区多站点统一隧道到数据中心（AP Group 规模化）
  type: case
  source_chapter: "p12"
  source_quote: |
    "By using OmniVista, this is absolutely possible to tunnel the traffic from all location toward the Data
    Center. All you need to do is to have all APs part of the same AP Group, and apply the GTTS SSID
    configuration to this AP Group. All APs will broadcast the same SSID toward the same tunnel endpoint"
  summary: |
    园区架构：1 个数据中心 + 多站点，同 SSID 全站广播支持漫游；OV2500 里把所有 AP 放进同一 AP Group、对该组应用 GTTS SSID 配置，即全站点流量统一隧道到数据中心。聚合交换机配置与 p9 完全相同。适用于公司、医院、教育等多人群 WLAN 场景。
  tags: [scenario, campus, ov2500]

- id: C5
  title: 场景三：单台聚合交换机多租户（运营商 MSP 模式）
  type: case
  source_chapter: "p13"
  source_quote: |
    "Each customer has their own AP Group, and potentially their own OmniVista. So each AP Group is thus
    configured with the tunnel aggregation switch IP address of the Service Provider. The tunneled traffic
    travels through the already established link between customers and the Service Provider."
  summary: |
    运营商模式：每客户一个 AP Group（可各有 OmniVista），各 AP Group 均配运营商聚合交换机 IP；隧道流量借客户-运营商既有链路（SD-WAN 或 SPB/MPLS）传输，在运营商侧落隧道并施安全策略，客户间逻辑隔离。
  tags: [scenario, multi-tenancy, sp]

- id: C6
  title: R1 Hairpin 冗余配置：SAP/ACCESS 各建一条 LACP 链路聚合
  type: case
  source_chapter: "p15-16"
  source_quote: |
    "linkagg lacp agg 1 size 2 admin-state enable / linkagg lacp port 1/1/25 actor admin-key 1 / linkagg lacp
    port 1/1/26 actor admin-key 1 ... service access linkagg 1 vlan-xlation enable l2profile "guest-l2profile"
    ... service 100 sap linkagg 1:50 ... vlan 50 members linkagg 2 untagged"
  summary: |
    Hairpin 冗余=两条链路聚合（SAP 侧 agg 1、ACCESS 侧 agg 2，各含 2 端口）。所有 SAP 相关配置把 "port" 换成 "linkagg" 即可，service/vpnid 不变。原文样例：agg1=1/1/25+26（admin-key 1）、agg2=1/1/27+28（admin-key 2）。Hairpin 数量不限于 2 条，可与 R2/R3/R4 叠加。
  tags: [cli, redundancy, r1, linkagg]

- id: C7
  title: R2 Primary & Secondary 配置：Backup GRE Tunnel Server IP + VPN ID 一致
  type: case
  source_chapter: "p16-17"
  source_quote: |
    "The Secondary tunnel aggregation switch configuration is the same as the Primary Switch. Be only sure
    that the VPN ID is the same as the Primary Switch, because this is the one used by the AP to open tunnels
    with the endpoints. ... the field "Backup GRE Tunnel Server IP Address" must be specified"
  summary: |
    备机配置与主机完全相同（尤其 VPN ID 必须一致，AP 用它开隧道）；SSID 里填 Backup GRE Tunnel Server IP 即启用。AP 失联主机时隧道改开到备机，收敛秒级；可开 Preemption 让主机恢复后按计时器回收并迁移会话。
  tags: [cli, redundancy, r2]

- id: C8
  title: R3 Virtual-Chassis 配置：跨成员 linkagg 的双 Hairpin
  type: case
  source_chapter: "p17-18"
  source_quote: |
    "linkagg lacp port 1/1/25 actor admin-key 1 / linkagg lacp port 2/1/25 actor admin-key 1 ... service 100
    sap linkagg 1:50 ... vlan 50 members linkagg 2 untagged"
  summary: |
    先把两台聚合交换机组 Virtual-Chassis；再配两条跨成员 linkagg（agg1 SAP 侧=slot1 的 1/1/25 + slot2 的 2/1/25；agg2 ACCESS 侧=1/1/27 + 2/1/27），service/sap/vlan 配置同 R1。VC 替代 Primary-Backup 后收敛亚秒级；Hairpin、网络连接、整机三层故障全覆盖。
  tags: [cli, redundancy, r3, virtual-chassis]

- id: C9
  title: R4 每 SSID 一对交换机配置：多套 VC + 各 SSID 指向各自交换机对
  type: case
  source_chapter: "p18-19"
  source_quote: |
    "The highest level of redundancy is reached by having a couple of switches for each SSID. Couples of
    switches should be in different locations to prevent geographical failure. ... There is the need of
    creating multiple Virtual-Chassis, the link aggregations for SAP and ACCESS ports, and each SSID need to
    be configured to tunneled traffic toward each switch."
  summary: |
    最高冗余：每个 GTTS SSID 独占一对交换机（建议异地部署防地理性故障），Primary-Backup 或 Virtual-Chassis 均可实现。配置=前几种案例的组合：建多套 VC、各自配 SAP/ACCESS linkagg、每个 SSID 分别指向自己的交换机对。连续故障或整站宕机时只影响对应 SSID。
  tags: [cli, redundancy, r4]

## counter-examples

# 提取范围：fulltext.md（p1-p19）

- id: X1
  title: 坑：一台 AP 广播 N 个不同 ARP 的 GTTS SSID 却只配少量聚合交换机 → 隧道起不来
  type: counter_example
  source_chapter: "p7"
  source_quote: |
    "Each AP can only have ONE active tunnel at a time toward ONE tunnel aggregation switch. ... if 3 SSIDs
    using the GTTS feature are broadcasted from an AP, each of them using a different Access Role Profile,
    this is mandatory to have at least 3 tunnel aggregation switches, one for each SSID."
  summary: |
    One ARP 是硬规则：每个 ARP 的隧道同一时刻只能活跃在一台聚合交换机上。规划 3 个各用不同 ARP 的隧道 SSID 就必须备 3 台交换机；只配 1 台则其余 SSID 隧道无法建立。交换机数量按"同时活跃的 ARP 数"规划。
  tags: [pitfall, one-arp, sizing]

- id: X2
  title: 反模式：多个 SSID 共用同一个 ARP（同一条隧道）没有收益
  type: counter_example
  source_chapter: "p7"
  source_quote: |
    "This is technically possible to have multiple SSIDs using the same Access Role Profile, thus the same
    tunnel at the end. But ... In a real scenario, creating multiple SSIDs using the same Access Role Profile
    have no benefits because all SSIDs will have at the end the same configuration, besides the SSID name and
    the association method."
  summary: |
    技术上可行但无意义：ARP 决定 ACL/QoS/用户 VLAN/Portal 等全部配置，多 SSID 共用一个 ARP 最终只是名字和关联方式不同的同一套网络。要做差异化就必须分 ARP（并按 X1 补交换机）。
  tags: [anti-pattern, arp]

- id: X3
  title: 坑：AP 管理 IP 与 GRE Tunnel Server IP 同网段 → 违反 Layer 3 hop 前置
  type: counter_example
  source_chapter: "p7"
  source_quote: |
    "A layer 3 hop must exist between the far-ends APs and the tunnel aggregation switch. In other words, the
    management IP address of the AP must not be in the same subnet as the IP address sets as the GRE Tunnel
    Server IP while creating the SSID."
  summary: |
    AP 与聚合交换机之间必须有三层路由跳变；AP 管理地址与 GRE Server IP 同子网属于违反强制架构前置，GTTS 无法工作。开局核对项。
  tags: [pitfall, l3-hop]

- id: X4
  title: 坑：跨公司网络跑 GTTS 未协调 MTU → 24 字节封装开销导致丢包
  type: counter_example
  source_chapter: "p8"
  source_quote: |
    "An issue can occurs when the GTTS feature is used across a network belonging to another company. In that
    case, communication between the two network administrators must be done to authorize both networks to
    allow packets that are slightly larger."
  summary: |
    L2 GRE 加 24 字节（GRE 4B+IP 20B）。借道运营商/其他公司网络（多租户、SD-WAN 场景常见）时必须双方网管协商放行略大报文，否则大包被静默丢弃。
  tags: [pitfall, mtu]

- id: X5
  title: 坑：auto-discover 被关 → 每台远端 AP 都要手工加 MAC
  type: counter_example
  source_chapter: "p8"
  source_quote: |
    "Without this feature enabled, each far-end AP has to be manually set in the switch by adding their MAC
    address. By default, the auto-discover is enabled."
  summary: |
    auto-discover 默认开，但一旦被关，交换机不再动态接受 AP 隧道，需逐台手工登记 MAC。开局用 `service l2gre auto-discover enable` 确认。
  tags: [pitfall, auto-discover]

- id: X6
  title: 误区：以为组 Virtual-Chassis 能抬高单机隧道数上限
  type: counter_example
  source_chapter: "p8"
  source_quote: |
    "The maximum number of active tunnels on a tunnel aggregation switch depends of the switch model. This
    number doesn't go up if Virtual-Chassis is used"
  summary: |
    隧道数上限按单机机型定档（1000/2000/6000），组 VC 后不增加。容量规划不能指望堆叠翻倍，必须直接选高档机型。
  tags: [misconception, scalability, vc]

- id: X7
  title: 反例：R0 无冗余——交换机/Hairpin/连接任一失败，GTTS SSID 全灭
  type: counter_example
  source_chapter: "p14"
  source_quote: |
    "There is only one tunnel aggregation switch configured as the Primary, and one mandatory Hairpin. If
    either the switch, the Hairpin, or the connectivity between the Corporate switch and the tunnel
    aggregation switch fails, the GTTS SSID is not usable anymore."
  summary: |
    R0 基线无任何冗余：单交换机+单 Hairpin，三个单点（整机、自环线、网络连接）任一故障即 SSID 不可用。生产环境至少上 R1/R2。
  tags: [counter-example, r0]

- id: X8
  title: 误区：R1 Hairpin 冗余被当成整机冗余
  type: counter_example
  source_chapter: "p15"
  source_quote: |
    "There is still no redundancy regarding the switch and the network connectivity, but up to 1 SAP port and
    1 ACCESS port can fail with no impact on the GTTS traffic."
  summary: |
    R1 只冗余 Hairpin 端口（SAP/ACCESS 各坏 1 个口无影响），交换机本身与网络连接仍是单点。要整机冗余需 R2（Primary/Backup）或 R3（Virtual-Chassis）。
  tags: [misconception, r1]

- id: X9
  title: 坑：AP 侧 Entropy 未启用 → GTTS 不可用（文档加粗的强制项）
  type: counter_example
  source_chapter: "p10"
  source_quote: |
    "Important: Support of Entropy MUST be Enabled for the used of the GTTS feature."
  summary: |
    AP 的 SSID 隧道配置中 Entropy 支持必须启用，是文档以 Important 标注的硬性前提，漏开 GTTS 不工作。
  tags: [pitfall, ap, entropy]

- id: X10
  title: 坑：把 DHCP/Portal 留在内网、指望隧道外服务——安全与可达性双输
  type: counter_example
  source_chapter: "p4-5"
  source_quote: |
    "a DHCP server must be deployed in the same area of the tunnel aggregation switch. This is still possible
    to use protocols to forward DHCP requests to a server that is not part of the same subnet, but a dedicated
    server is still better from a security point of view."
  summary: |
    DHCP 流量在隧道内，服务器必须在聚合交换机区域可达；可用 DHCP 中继转发到别处子网，但安全角度应给隧道 SSID 配专属 DHCP/Portal/DNS/NTP 服务集。复用内网服务既难可达又破坏隔离初衷。
  tags: [pitfall, services, security]

- id: X11
  title: 坑：Tunnel ID / VPN ID 两侧不一致 → 隧道对不上
  type: counter_example
  source_chapter: "p9-10, p16"
  source_quote: |
    "The VPN ID, on the other hand, must be the same as configured during the SSID creation" / "Be only sure
    that the VPN ID is the same as the Primary Switch, because this is the one used by the AP to open tunnels"
  summary: |
    AP 侧 Tunnel ID、交换机侧 vpnid、备机（R2）的 vpnid 三处必须一致，AP 靠它开隧道；service 编号则只是本机局部编号可任选。配错 ID 是隧道建不起来的第一嫌疑。另注意 VLAN ID 与 VPN ID 不必相同（p9）。
  tags: [pitfall, vpn-id]

- id: X12
  title: 局限：Hairpin 带宽是 SSID 吞吐天花板，默认单线易成瓶颈
  type: counter_example
  source_chapter: "p8"
  source_quote: |
    "the maximum bandwidth of the SSID is capped by the hairpin bandwidth"
  summary: |
    全部流量过一根自环线，SSID 峰值带宽=该线线速。高带宽隧道 SSID 必须用多条 Hairpin/linkagg 扩容（顺带获得 R1 冗余），否则交换机性能再好也被 Hairpin 卡死。
  tags: [limit, hairpin, capacity]

## frameworks

# 提取范围：fulltext.md（p1-p19）

- id: F1
  title: GTTS 三用例 × 三场景体系（为什么隧道 + 隧道落在哪）
  type: framework
  source_chapter: "p3, p11-13"
  source_quote: |
    "1. Guest Traffic: ... their traffic should be completely isolated from corporate traffic ... 2. Security
    Policy: Certain security services, such as IPS, require the security appliance to be deployed in-line ...
    3. Migration: When migrating from a controller-based architecture to a distributed one ..."
  summary: |
    纵轴三用例（p3）：访客隔离（隧道到 DMZ 只出 Internet）、安全策略（IPS 类串行设备 bump-in-the-wire、在中心 scrub 流量）、迁移（控制器架构转分布式时边缘不加 VLAN，VLAN 只配在中心）。横轴三场景（p11-13）：DMZ 访客隧道（单区隔离基线）→ Campus 园区（多站点同 AP Group 汇聚数据中心）→ 单机多租户（运营商为多客户终结隧道）。选型时先定用例，再按组织形态（企业/园区/运营商）选场景模板。
  tags: [framework, use-case, scenario]

- id: F2
  title: 冗余五级阶梯 R0-R4：单点 → 端口 → 整机(备胎) → 整机(亚秒) → 按SSID地理分散
  type: framework
  source_chapter: "p14-19"
  source_quote: |
    "We will see in this chapter a few solutions to avoid that this switch become a single point of failure
    of an architecture using the GTTS feature."
  summary: |
    R0（p14）无冗余：单交换机+单 Hairpin，三单点；R1（p15）Hairpin 冗余：SAP/ACCESS 各建 linkagg，端口级故障无感，带宽顺带翻倍，可与 R2/R3/R4 叠加；R2（p16）Primary & Secondary：SSID 填 Backup GRE Server IP，整机切换秒级，Preemption 可回收；R3（p17）Virtual-Chassis：VC+跨成员 linkagg，亚秒收敛，Hairpin/连接/整机全覆盖；R4（p18）每 SSID 一对交换机：最高等级，交换机对异地部署，连续故障/整站宕机只伤单个 SSID，可组合 Primary-Backup 或 VC。选型递进：预算从低到高、收敛从秒级到亚秒级、爆炸半径从全网到单 SSID。
  tags: [framework, redundancy, r0-r4]

- id: F3
  title: GTTS 数据路径统一模型：分类→封装→隧道→Hairpin→VLAN 域
  type: framework
  source_chapter: "p4-5"
  source_quote: |
    "Traffic received on the Access Point is classified into a Access Role Profile L2 GRE service profile that
    is mapped to an L2 GRE tunnel service. ... the GRE encapsulation is removed, and the traffic is then
    forwarded to a VLAN domain."
  summary: |
    全书配置皆由此模型推出：AP 收到流量→按 ARP 分类进 L2 GRE service profile→加 GRE 头过隧道→聚合交换机解封装→经 Hairpin（SAP 口→物理线→ACCESS 口）→落 VLAN 域出 Internet/边界网。双向对称（下行先过 ACCESS 进 SAP 再入隧道）。排障按此路径逐段定位：分类错（ARP）→隧道没建（ID/IP/L3hop/auto-discover）→落地错（service/sap/vlan）。
  tags: [framework, datapath]

## glossary

- **GTTS（Guest Traffic Tunneling Services，访客流量隧道服务）**：OmniAccess Stellar 与 OmniSwitch 联合特性，把无线用户流量从 AP 灵活隧道到一台或多台 OmniSwitch 隧道聚合端点；虽名为"访客"，也用于安全策略旁挂与架构迁移。<<<PAGE 3>>>
- **L2 GRE（Layer 2 Generic Routing Encapsulation，二层通用路由封装）**：GTTS 底层协议，在 IP 网上承载二层 overlay，识别并隔离设备流量；以 service 形式实现，可关联 UNP profile，实现思路同 OmniSwitch VXLAN。<<<PAGE 4>>>
- **tunnel aggregation switch（隧道聚合交换机）**：L2 GRE 隧道的交换机侧终点，通常部署在 DMZ 等防火墙围护的安全区；解封装后经 Hairpin 把流量送入 VLAN 域。<<<PAGE 4>>>
- **Hairpin**：同一台交换机上两个端口用一根线自环；一侧 SAP 口出隧道，另一侧 ACCESS 口落 VLAN；其线速封顶 SSID 带宽。<<<PAGE 4>>>
- **SAP port（Service Access Point port，业务接入点端口）**：Hairpin 的隧道侧端口，创建 service 并映射到此口，隧道流量从此出隧道；冗余设计中可换成 linkagg。<<<PAGE 4>>>
- **ACCESS port（Hairpin 的接入侧端口）**：Hairpin 另一侧的普通传统接入端口，映射 VLAN；隧道流量由此进入 VLAN 域，下行流量反向先经此口进隧道。<<<PAGE 4>>>
- **ARP（Access Role Profile，访问角色档案）**：Stellar 的角色配置对象（含 ACL/QoS/用户 VLAN/Portal 等）；GTTS 隧道粒度可细到 ARP 级，每个 ARP 同一时刻只对应一条活跃隧道。<<<PAGE 3>>><<<PAGE 7>>>
- **Tunnel Profile（隧道档案）**：包含建立 L2 GRE 隧道全部参数的配置对象；单 SSID 多 ARP 场景下每个 ARP 各映射一个 Tunnel Profile，在 OV2500 Expert 模式创建。<<<PAGE 5>>><<<PAGE 11>>>
- **VPN ID**：service l2gre 的隧道标识，AP 侧 Tunnel ID、主备交换机 vpnid 必须一致，AP 依此开隧道；与 ACCESS 口 VLAN ID 不必相同。<<<PAGE 9>>><<<PAGE 16>>>
- **Tunnel ID**：AP 侧 SSID 隧道配置中的隧道编号，必须与交换机侧配置一致。<<<PAGE 10>>>
- **GRE Tunnel Server IP / Data VPN Server**：SSID 隧道配置中主隧道聚合交换机的 IP 地址。<<<PAGE 10>>>
- **Backup GRE Tunnel Server IP**：备隧道聚合交换机 IP；与 Primary 无同/异网段要求，失联 Primary 时隧道切换到此机（R2 冗余）。<<<PAGE 10>>><<<PAGE 17>>>
- **Preemption（抢占）**：R2 冗余选项；Primary 恢复后按 Preemption Countdown Timer 到期回收 Master 角色，AP 把全部会话迁回 Primary。<<<PAGE 10>>><<<PAGE 17>>>
- **Entropy（熵）**：AP 侧 SSID 隧道配置项，文档以 Important 标注必须启用，否则 GTTS 不可用。<<<PAGE 10>>>
- **auto-discover（自动发现）**：交换机特性，动态接受远端 AP 发起的隧道；默认开启，关闭则需逐台手工登记 AP MAC。命令 `service l2gre auto-discover enable`。<<<PAGE 8>>>
- **l2profile（L2 服务档案）**：交换机侧服务端口模板，建 GTTS SAP 口时创建并丢弃 stp/gvrp/mvrp，配合 vlan-xlation 启用。<<<PAGE 9>>>
- **vlan-xlation（VLAN translation，VLAN 转换）**：service access port 与 service 上的开关，Hairpin 两侧 VLAN 映射所需。<<<PAGE 9>>>
- **One ARP 规则**：每台 AP 同一时刻对一个 ARP 只能有一条活跃隧道指向一台聚合交换机；N 个不同 ARP 的隧道 SSID 需要 N 台聚合交换机。<<<PAGE 7>>>
- **Layer 3 hop（三层跳变）**：强制架构前置——AP 管理 IP 与 GRE Tunnel Server IP 必须不同子网，中间存在三层路由。<<<PAGE 7>>>
- **Virtual-Chassis（虚拟机箱）**：OmniSwitch 堆叠技术；R3 冗余用它替代 Primary-Backup，两台聚合交换机组 VC 后配合跨成员 linkagg 实现亚秒收敛。<<<PAGE 17>>>
- **DMZ（Demilitarized Zone，非军事区）**：企业内网与外部网之间的缓冲区，由防火墙分隔；GTTS 聚合交换机与专属 DHCP 通常部署于此。<<<PAGE 4>>><<<PAGE 11>>>
- **Multi-tenancy（多租户）**：运营商场景下多个客户的流量集中终结于同一台（或多台）GTTS 聚合交换机且保持客户间逻辑隔离；每客户一个 AP Group，链路可为 SD-WAN/SPB/MPLS。<<<PAGE 3>>><<<PAGE 13>>>
- **AP Group（接入点组）**：GTTS 的配置粒度单位；组内 AP 广播同一 SSID 指向同一隧道终点，是园区多站规模化与多租户隔离的基础。<<<PAGE 3>>><<<PAGE 12>>>
- **Filter-id**：802.1X 认证返回字段，可用于把一个 SSID 的用户分类到不同 ARP，进而进不同隧道。<<<PAGE 5>>>
- **linkagg / LACP（链路聚合）**：R1/R3 冗余中把 Hairpin 的 SAP 侧与 ACCESS 侧各自做成聚合（跨 VC 成员则双机各出一口），端口级冗余并提升 Hairpin 带宽。<<<PAGE 15>>><<<PAGE 17>>>

## principles

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
