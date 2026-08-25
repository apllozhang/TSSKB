# frameworks.md · Guest Traffic Tunnelling Services Application Note · 体系框架提取
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
