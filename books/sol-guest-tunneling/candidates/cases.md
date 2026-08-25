# cases.md · Guest Traffic Tunnelling Services Application Note · 配置流程与场景案例提取
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
