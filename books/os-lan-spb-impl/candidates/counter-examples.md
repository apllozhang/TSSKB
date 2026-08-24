# counter-examples.md · 陷阱 / 警告 / 反例提取
# 来源: OmniSwitch LAN SPB Concepts & Implementation (DT00XTE323EN, Edition 12)
# 规则: 每条含原文引用与页码；宁多勿漏，待后续独立验证阶段筛选

```yaml
- id: ce01
  title: 陷阱——控制 BVLAN 在 IS-IS 启用状态下无法更改
  type: counter-example
  source_chapter: "p83"
  source_quote: |
    "Notes
    Control BVLAN carries the ISIS PDUs which are single tagged with the chosen BVLAN ID.
    Control BVLAN can only be changed when protocol is disabled.
    There is no Spanning Tree on BVLANs"
  summary: |
    常见报错场景：试图直接执行 spb isis control-bvlan 改控制 BVLAN 失败。正确顺序是先 spb isis admin-state disable 再改，改完再 enable（Lab 1 与 p326 混合端口 Lab 均按此顺序）。另注意 BVLAN 上不存在生成树，不要指望 STP 在骨干里做环路保护。
  tags: [control-bvlan, isis, ordering, pitfall]

- id: ce02
  title: 陷阱——链路两侧 metric 配不一致时整条链路按最大值计算
  type: counter-example
  source_chapter: "p129"
  source_quote: |
    "Notes
    If the SPB interface metric value is set to a different value for each side of a link, the highest metric value is applied to the entire link."
  summary: |
    只想"单侧降级"某链路是行不通的：一侧 10 一侧 40 时系统按 40 算整条链路。做路径调整实验/维护时必须两端同步改（Lab 步骤在 Switch 7 和 Switch 8 上都执行 metric 40），做完恢复也要两端同回 10，否则残留不等价状态影响 ECT 分流判断。
  tags: [metric, link-cost, asymmetric, pitfall]

- id: ce03
  title: 陷阱——LBD 在 linkagg 上检测到环路会关闭整个聚合组所有端口
  type: counter-example
  source_chapter: "p131"
  source_quote: |
    "Notes
    When loopback is detected on any one of the Linkagg port, all the ports of the Linkagg will be shut down due to loopback detection."
  summary: |
    LBD 的作用域是聚合组而非物理成员口：任一成员口检测到环路，整个 linkagg 全部 shutdown。生产环境若把 LBD 开在承载多条业务的聚合接入口上，一次误判会放大故障面；规划时应评估该口是否聚合、自动恢复定时器（默认 300 秒）是否可接受。
  tags: [lbd, linkagg, shutdown, blast-radius, pitfall]

- id: ce04
  title: 反例——LBD 端口关闭的裁决规则（最高 BridgeID / 最高 PortID 被关）
  type: counter-example
  source_chapter: "p122"
  source_quote: |
    "Port in switch with highest BridgeID is shut down
    Port with highest PortID is shut down
    In case the 2 SAP ports are on the same switch, port 1/1/8 is shutdown as this interface has higher port identifier
    Port LBD State : ShutDown"
  summary: |
    两台 BEB 的 SAP 口形成环路时，LBD 不是随机封口：两机之间关 BridgeID 较高那台的口；同一台交换机上两个 SAP 口成环时关 PortID 较大的口。p123 实测：System ID e8e7.32d4.850d（较高）的 BEB-B 1/1/7 被 shutdown，日志可见 "source LBD, reason lbd shutdown"。排障时要按此规则预判哪个口会被封，避免误以为设备故障。
  tags: [lbd, bridge-id, port-id, tiebreak, behavior]

- id: ce05
  title: 陷阱——服务绑定 IP 接口后 VLAN 转换状态被锁定不可改
  type: counter-example
  source_chapter: "p163"
  source_quote: |
    "VLAN translation is implicitly enabled when a service is assigned to an IP interface regardless of whether or not VLAN translation is enabled for the service
    The VLAN translation status is no longer configurable as long as the service is bound to an IP interface"
  summary: |
    在 L3 场景（VPN-Lite/L3VPN）下试图手工 service X vlan-xlation disable 会失败：一旦 ip interface ... service X 绑定，转换被隐式置为 enable（show 显示 "Vlan Translation : Y (Auto)"）且绑定期间禁止修改。想让两端 CVLAN 不同又需要 L3 时，规划阶段就要确认翻译需求，不要指望事后在服务上改。
  tags: [vlan-xlation, ip-interface, locked-config, pitfall]

- id: ce06
  title: 反例——同一 I-SID 不能既绑定（bind）某 VRF 又被重分发（redist）到该 VRF
  type: counter-example
  source_chapter: "p198"
  source_quote: |
    "One ISID cannot be attached (binding) and be redistributed to a same VRF instance"
  summary: |
    L3-VPN 路由泄漏的冲突约束：对同一个 VRF，某 I-SID 已经通过 spb ipvpn bind 绑定，就不能再用 spb ipvpn redist source-isid X destination-isid Y（或反向）把同一 I-SID 的路由泄漏进该 VRF，否则路由来源重复/冲突。设计多部门互通（Dept1↔Dept2，见 p207 例）时，泄漏路径必须绕开已绑定的组合。
  tags: [l3vpn, redist, bind, conflict, constraint]

- id: ce07
  title: 反例——VPN-Lite 中两个 VRF 不能共享同一 I-SID
  type: counter-example
  source_chapter: "p175"
  source_quote: |
    "In the VPN Lite version there can actually be multiple IP interfaces tied to different I-SID per VRF (but two VRF cannot share the same ISID).
    There is a corresponding SAP on the other side of the loopback tied to the correct I-SID using the same VLAN as its identifier."
  summary: |
    VPN-Lite 的扩展边界：一个 VRF 可以挂多个接口对应多个 I-SID（跨多服务），但两个不同 VRF 不能落在同一个 I-SID 上——I-SID 就是 L3 隔离边界。想要租户间共享某网段需另建服务或改用 L3-VPN 的 redist 泄漏。回环对的 VLAN 标识也必须与对侧 SAP 一致。
  tags: [vpn-lite, vrf, isid, sharing, constraint]

- id: ce08
  title: 陷阱——ERP/SPB 互操作的硬性禁区（BEB 不能做 RPL、环不能建在 tag 口/STP NNI）
  type: counter-example
  source_chapter: "p242"
  source_quote: |
    "• Only two ERP type NNI associations are allowed per SVLAN
    • Configuring an ERP ring on 802.1q tagged port associations with SVLANs is not allowed
    • Configuring an ERP ring on an STP type NNI association with an SVLAN is not allowed
    • BEB cannot be a RPL node • RPL port shall not be configured on SPB network • RPL port cannot be configured as a SAP neighbour
    • SPB Service associated with the ERP Service VLAN has to be configured in the Control BVLAN
    each ERP ring must have an exclusive range of VLANs including the service VLAN relative to the other ERP rings"
  summary: |
    ERP 过 SPB 的六条禁令合并为一张检查表：①每 SVLAN 最多两个 ERP 型 NNI 关联；②环不能配在 802.1q tag 端口关联的 SVLAN 上；③不能配在 STP 型 NNI 关联上；④BEB 不能当 RPL 节点、RPL 口不能放进 SPB 网、RPL 口不能当 SAP neighbor；⑤ERP 服务 VLAN 对应的 SPB 服务必须建在控制 BVLAN 上；⑥多 ERP 环共存时各环 VLAN 范围（含服务 VLAN）必须互斥、服务 ID 不得跨环。任一条违反都会导致环协议行为异常或配置被拒。
  tags: [erp, rpl, constraints, forbidden-config, pitfall]

- id: ce09
  title: 陷阱——E-Tree 服务自 8.9.R03 起新建 SAP 全为 Leaf，Leaf 之间不通
  type: counter-example
  source_chapter: "p318"
  source_quote: |
    "A leaf SAP cannot communicate with another Leaf SAP in the service spanning multiple BEBs whereas Leaf SAP to Root SAP traffic is allowed.
    Note: Conventional SAPs are called Root SAPs. Note: As of 8.9.R03, all SAPs created for E-Tree service are only of type Leaf"
  summary: |
    两个易踩点：①业务语义——E-Tree 里 Leaf↔Leaf 天然隔离，用户报障"同服务两站不通"先查是否都是 Leaf；②版本行为——8.9.R03 起 E-Tree 服务新建的 SAP 一律 Leaf 型，Root 必须落在对端 BEB 的普通（非 e-tree）服务上（p319/331 Lab 的 Root 侧配置无 e-tree 选项）。把两端都配成 e-tree 会得到全隔离的死网。
  tags: [e-tree, leaf, root, 89r3, isolation, pitfall]

- id: ce10
  title: 陷阱——mac-ping 目标不能是广播/组播/空地址，超时固定 1 秒
  type: counter-example
  source_chapter: "p147"
  source_quote: |
    "Mac-ping: Proprietary ping
    • The timeout for each ping request packet is 1 sec. (not configurable)
    • Destination MAC cannot be a broadcast, multicast, or NULL address"
  summary: |
    用 mac-ping 验证转发时的限制：不能拿组播 B-MAC（如 tandem 组播树地址）或广播地址当目标，必须先 show spb isis info 取对端单播 B-MAC；每包超时固定 1 秒不可调，做时延基线时注意这个粒度。组播路径要用 show spb isis multicast-table 查表而非 ping。
  tags: [mac-ping, oam, restrictions, pitfall]

- id: ce11
  title: 陷阱——回环模式端口被独占且专用 VLAN 只能关联回环口
  type: counter-example
  source_chapter: "p359"
  source_quote: |
    "Once a port or link aggregate is configured to run in the loopback mode, no other functionality is supported on the port or link aggregate.
    The dedicated VLAN is reserved for the L3 VPN and can only be associated with the loopback port or link aggregate
    Once the loopback mode is enabled for a link aggregate, the link aggregate is dedicated to providing loopback functionality ... The loopback mode is disabled only when the link aggregate is deleted."
  summary: |
    老平台面板口回环模式的独占性：端口/聚合口进入 loopback 模式后不能再承担任何其他功能；配套的专用 VLAN 只能关联该回环口（用 rtr-port+vlan 形式的 IP 接口保证）；对 linkagg 而言回环模式一旦开启只能靠删除聚合组来解除。规划端口预算时要把这些口从业务端口池里扣除。
  tags: [loopback-mode, rtr-port, port-budget, exclusivity, pitfall]

- id: ce12
  title: 陷阱——SNMP 用户名禁用 admin/diag/user 三个保留字
  type: counter-example
  source_chapter: "p309"
  source_quote: |
    "Notes: The username string cannot be "admin", "diag", or "user". A unique username must be used.
    In this case we are creating a user named snmpuser to access SNMP."
  summary: |
    给 OV2500 纳管建 SNMP 用户时的静默约束：user 命令的账号名不能取 admin/diag/user，必须换独特名（教材用 snmpuser）。若沿用习惯的 admin 会建号失败或映射不生效，导致发现流程卡住。
  tags: [snmp, username, reserved-names, ov2500, pitfall]

- id: ce13
  title: 反例——UNP 接入口的隔离用户不能被重定向做补救
  type: counter-example
  source_chapter: "p262"
  source_quote: |
    "Dynamic SAPs supported from UNP service profiles
    Device assignment to an SPB service profile / Automatic SAP creation / Quarantine Manager support *
    * Redirecting quarantined users learned on UNP access ports for remediation is not supported"
  summary: |
    UNP 动态 SAP 的功能缺口：Quarantine Manager 虽然标称支持，但"把 UNP 接入口上被隔离的用户重定向到补救门户"不被支持。做 NAC 合规整改（用户先去修复页面再放行）的设计时要改用其他放行/隔离机制，不能依赖该重定向。
  tags: [unp, quarantine, remediation, unsupported, pitfall]

- id: ce14
  title: 反例——人为制造环路：禁用 VLAN 生成树 + 增加并行 SAP 路径导致 MAC 漂移与 ping 中断
  type: counter-example
  source_chapter: "p131"
  source_quote: |
    "3. Disable Spanning Tree on Switch 5 Vlan 2
    Switch 5 -> spantree vlan 2 admin-state disable
    5. Check that a loop has been created
    Client 5 is learned on both switches 7 and 8 on access port
    Ping between Client 5 & 6 is not operational anymore"
  summary: |
    教材故意构造的故障模型：在 Sw8 新建 SAP 1/1/4:2、Sw5 把 VLAN 2 tag 到并行端口并 spantree vlan 2 admin-state disable 后，接入侧形成物理环路——show mac-learning port 显示 Client 5 的 MAC 同时出现在 Sw7 1/1/3 与 Sw8 1/1/4（MAC 漂移/抖动），Client 5↔6 ping 彻底中断。该实验证明：SPB 骨干本身无环，但接入层并行双路径若无 STP/LBD 兜底仍会成环；随后的 LBD 步骤（ce03/ce04）演示自动解环。生产中对应教训是双上联接入必须配 DHL/ERP/LBD 之一。
  tags: [loop, mac-flapping, stp-disabled, lab-failure, root-cause]
```
