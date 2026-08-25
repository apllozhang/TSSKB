# counter-examples.md · Guest Traffic Tunnelling Services Application Note · 限制/兼容/坑提取
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
