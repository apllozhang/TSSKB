# frameworks.md · ACFE WLAN Basic Deployment With OmniVista Ed04 — 框架/流程候选
# 提取器：cangjie-skill 框架提取阶段（宁多勿漏，待独立验证）
# 来源：source/fulltext.md（页码与原文一致）、figures_captions.md、BOOK_OVERVIEW.md

```yaml
- id: f01
  title: AP 网络部署模式自动选择决策树（Express / Enterprise / Cloud）
  type: framework
  source_chapter: "p100"
  source_quote: |
    "NETWORK DEPLOYMENT MODE SELECTION
    DHCP REQUEST
    IF DHCP SERVER SENDS OFFER WITH OPTION 138 = YES (IP@ OF OV2500) ... AP REGISTERS AND RETRIEVES ITS CONFIGURATION FROM OV2500
    IF DHCP SERVER SENDS OFFER WITH OPTION 138 = NO ... AP CONTACTS OV CIRRUS
    IF AP REGISTERED IN OV CIRRUS (MAC/SN) = YES ... AP RETRIEVES ITS CONFIGURATION FROM OV CIRRUS
    IF AP REGISTERED IN OV CIRRUS (MAC/SN) = NO ... AP BOOTS IN EXPRESS MODE"
  summary: |
    Stellar AP 上电后按三级判定自动落入三种管理模式：先看 DHCP offer 是否携带 option 138（指向 OmniVista 2500），有则进企业模式；没有则尝试联系 Cirrus 云，若序列号/MAC 已在云上登记则进云管理模式；两者都不满足则落到默认的 Express 独立模式。交付工程师可反向利用该决策树做模式规划：想上云就提前在 Cirrus 声明序列号，想进企业模式就在 DHCP 作用域配 option 138。模式迁移（p18）同样遵循此机制：给 AP 管理作用域加 option 138，再恢复出厂或手动 Convert，且集群配置不会迁移会丢失。
  tags: [deployment, mode-selection, dhcp, option138, onboarding]

- id: f02
  title: Stellar AP 三平面流量分析模型（管理/控制/数据平面）
  type: framework
  source_chapter: "p266"
  source_quote: |
    "PLANES OF OPERATION
    • Management Plane • Centralized management on OmniVista Cirrus • APs managed with the same parameters are gathered in an AP Group • A Management VLAN is assigned to the AP group to carry the Management traffic
    • Control Plane per AP
    • Data Plane per AP • One VLAN per SSID
    (p269) Wireless data converted to Ethernet in the AP and sent to the AP uplink • Wireless traffic always tagged on the AP uplink • Traffic not forwarded to OmniVista Cirrus • Data Plane is only L2"
  summary: |
    把 AP 的流量拆成三个平面来分析和排障：管理平面集中在网管（Express 是 PVM，云管是 Cirrus），走 AP 管理且始终不打标签（untagged）的管理 VLAN；控制平面分布在每个 AP 上，空中邻居发现 + 经 LAN 的射频管理与漫游上下文共享；数据平面也在 AP 本地终结，无线转以太网后按 SSID 打标签上行，纯二层、无隧道回传网管、路由交给 LAN。做端口规划（管理 VLAN untagged、SSID VLAN tagged）和判断"哪些流量走哪条路"时直接套用该模型。
  tags: [architecture, planes, troubleshooting, vlan]

- id: f03
  title: AP 接入网络前置条件清单（PoE 干道 / VLAN / DHCP / DNS / 路由）
  type: framework
  source_chapter: "p25"
  source_quote: |
    "Trunk Port with POE
    •Untagged/Native vlan = AP Mgt VLAN
    •Tagged VLANs = SSID VLANs
    DHCP Scope for
    •All AP Mgt VLANs Require option 138 for OV IP address
    •All SSID VLANs
    DNS Server for
    •All AP Mgt subnets
    •All SSID subnets
    L3 protocols / Routing ... IP interfaces / Routers for • All AP Mgt VLANs • All SSID VLANs"
  summary: |
    推荐拓扑给出的上线检查清单：接入交换机到 AP 的端口必须是带 PoE 的 trunk，本征/不打标签 VLAN 固定给 AP 管理，SSID 对应 VLAN 全部打标签；DHCP 要为所有管理 VLAN 和 SSID VLAN 各建作用域（管理作用域需 option 138 指向网管）；DNS 覆盖全部子网；核心/汇聚为所有 VLAN 提供三层接口与路由。开局失败时按此清单逐项核对物理层、VLAN、DHCP、DNS、路由五类前提。教材实验沿用的编号惯例是 VLAN10 管理、VLAN20 员工、VLAN30 访客（p79/p123）。
  tags: [deployment, checklist, vlan, dhcp, poe, topology]

- id: f04
  title: Express 集群 AP Group 与 PVM/SVM 选举机制
  type: framework
  source_chapter: "p105"
  source_quote: |
    "In the AP Group, a Stellar AP is elected PVM (Primary Virtual Controller) • The PVM manages all the Group • The Group management is done from the PVM web interface
    SVM & Members • in the AP Group, another Stellar AP is elected SVM (Secondary Virtual Manager) to replace the PVM in case of failure
    PVM/SVM Election • Criteria 1 : highest Stellar AP model • Criteria 2 : highest MAC address"
  summary: |
    Express 模式的集群组织框架：相同 Group ID 且同 VLAN 的 AP 自动成组（出厂统一 Group ID 100、VLAN 1），组内按"最高型号优先、其次最大 MAC"选出 PVM 当虚拟控制器、第二位当 SVM 备份，其余为成员，全部管理都从 PVM 的统一 Web 界面完成，单组上限 255 台。排障或更换设备时先判断哪台是 PVM（换掉 PVM 会触发重选举，管理界面随之漂移），扩容超 64 台还要满足每台 OmniSwitch ≤32 AP、每堆叠 ≤64 AP 的弹性设计建议（p13）。
  tags: [express, cluster, pvm, election, resilience]

- id: f05
  title: Express 开箱默认行为与首次 Web 管理接入方法
  type: framework
  source_chapter: "p101"
  source_quote: |
    "BY DEFAULT, THE OMNIACCESS STELLAR AP:
    - BROADCASTS A SSID "MYWIFI-ABCD" WITH ABCD = LAST BYTES OF THE AP MAC@
    - HAS THE IP@ = 192.168.1.254 (OR AN IP@ RECEIVED FROM THE DHCP SERVER)
    TO ACCESS THE WEB ADMIN INTERFACE:
    - CONNECT TO THE SSID « MYWIFI-ABCD »
    - OPEN A WEB BROWSER AND INSERT THE FOLLOWING URL HTTP://<IP@ OF THE AP>:8080"
  summary: |
    Express 模式"开箱即接触"的标准路径：新 AP 默认广播 SSID mywifi-XXXX（XXXX 为 MAC 末四位）、默认管理 IP 192.168.1.254（有 DHCP 则改用分配地址），客户端连上默认 SSID 或与之同网段后，浏览器访问 http://AP-IP:8080 进 Web 管理。首次登录会强制走配置向导：改管理员密码 → 选国家/时区 → 建第一个 SSID（p114-115），之后按需把 IP 改为静态或 DHCP。现场没有 DHCP/网管时可按此最小路径先把单台 AP 配起来。
  tags: [express, first-contact, wizard, default-config]

- id: f06
  title: AP 云管 Onboarding 方法选择（手动 VLAN 分类 vs UNP 自动分类）
  type: framework
  source_chapter: "p284"
  source_quote: |
    "METHOD 1 > MANUAL CLASSIFICATION
    Create a VLAN that will serve as the management VLAN for the Stellar AP devices. This VLAN must then be manually configured as default/untagged VLAN on all ports where an AP is connected.
    METHOD 2 > ON BOARDING WITH UNP
    "defaultWLANProfile" UNP • Designated for classifying AP devices. • Automatically assigned to a built-in UNP LLDP classification rule that recognize and classify AP devices into the "defaultWLANProfile" UNP."
  summary: |
    AP 接入云管前的交换机侧准备有两种方法可选：方法一手动分类，自建管理 VLAN 并在每台 AP 端口手工配成默认/不打标签 VLAN，后续 AP 和 SSID VLAN 都要逐端口手工加（p286 明确列出该限制）；方法二用 OmniSwitch 内置的 defaultWLANProfile UNP 策略，端口设为 UNP 口后靠 LLDP-MED 自动识别 AP 并下发 Port VLAN ID，新增 AP 免配置。选型权衡：UNP 免运维但不做 802.1X 认证，未过认证的 AP 的 VLAN 标记流量仍会被转发（p291 安全限制）；对安全性要求高的端口用手动分类。教材目标页写 3 种方法，正文详述这 2 种。
  tags: [onboarding, unp, lldp, vlan, security]

- id: f07
  title: 设备云上线激活状态机与失败状态对照表
  type: framework
  source_chapter: "p261"
  source_quote: |
    "Intermediate Status
    Registered / Obtaining Certificate / Upgrade / Upgrading / Assigned / VPN Configuring / Connected to OV
    Expected Activation Status Up to 5 minutes
    Activation Status failures
    Failed To Get Certificate / Upgrade Failed / Configuring VPN Failed / Provisioning Failed / Device Validation Failed / Factory Reset Required"
  summary: |
    设备在 Cirrus 的 Device Catalog 里沿一条状态链推进：等待验证 → 等待首次联系 → 获取证书 → Registered → 升级 → Assigned → VPN 配置 → Connected to OV → Provisioning → OV Managed（全管托）。每个中间状态正常不超过约 5 分钟，卡住即对照失败状态定位（取证书失败、升级失败、VPN 配置失败、Provisioning 失败、需恢复出厂等）。设备靠周期性 Call Home 联系云，赶时间可在交换机执行 cloud-agent admin-state restart、在 AP 重启或 firstboot 强制立即呼叫（p250-251）；还可以用 ocloud_show / show cloud-agent status 在设备侧核对，用 Action > View Activation Log 看日志（p253）。
  tags: [activation, onboarding, cloud, call-home, troubleshooting]

- id: f08
  title: 设备不被云管发现的分层排障流程（L2 → L3 → 云激活日志）
  type: framework
  source_chapter: "p252"
  source_quote: |
    "4.1. Troubleshooting the Level 2
    4.1.1. Checking the cables: First, make sure that the cables are correctly plugged and recognized
    4.1.2. Checking the VLAN(s): Then, check that the VLAN(s) is/are correctly configured on each involved port
    4.2. L3 Troubleshooting
    4.2.1. Checking the IP Interfaces: Check that the IP interface is correctly configured on the OmniSwitch, and that its status is UP
    4.2.2. Pinging the server OVC: make sure that the OS6870 can ping the OmniVista Cirrus activation URL. This will also confirm that the Domain Name Resolution is working as intended"
  summary: |
    "设备在 OmniVista Cirrus 里不出现"的标准排查路径，自底向上三层推进：先查二层（show interfaces 确认线缆/链路 up，show vlan members port 确认端口 VLAN 正确），再查三层（show ip interface 确认 IP 接口 UP 且可转发），最后 ping 云激活域名（同时验证 DNS 解析），仍不行则打开设备的 Activation Log 看失败原因。AP 版本（p304-306）在同一骨架上加了 AP 专属检查：PoE 供电（show lanpower）、恢复出厂（Reset 键 6 秒或 ssudo firstboot）、getmode 确认 OVNG 模式、确认 DHCP 模式与拿到 IP、getovinfo 确认可达激活服务器。这是全书反复复用的排障决策树。
  tags: [troubleshooting, l2, l3, onboarding, decision-tree]

- id: f09
  title: SSID 认证安全级别选型矩阵（信任等级递进）
  type: framework
  source_chapter: "p310"
  source_quote: |
    "Open + Captive Portal • Cons: No Security • Pros: Followed by Captive Portal, any type of device can be authenticated
    MAC authentication • Cons: MAC can be spoofed, no traffic encryption • Pros: Available for basic wireless devices (printers, scanners,…)
    WPA/WPA2/WPA3 Personal = Pre-Shared Key (PSK) • Pros: Easy set up, strong keys can be difficult to hack • Cons: But all keys can be hacked or stolen (key shared by all users)
    WPA/WPA2/WPA3 Enterprise = 802.1X • Pros: Strongest security, ease of Management, scalability • Cons: More configuration during initial setup (server, users)"
  summary: |
    按"信任等级"从低到高排出的认证方式选型矩阵：开放+强制门户（无加密但任何终端可认证，适合访客）、MAC 认证（可伪造、无加密，只用于打印机/扫描仪等哑终端）、PSK 个人版（部署简单但全员共享密钥易泄露）、802.1X 企业版（安全性最强、可管理可扩展，代价是要先建 RADIUS 和用户库）。给客户设计 SSID 时先问终端类型与安全要求，再沿此矩阵落位；教材在 p313 进一步把选型固化成 SSID Usage 模板（访客网络/员工 BYOD/企业员工/受保护网络及其组合）。
  tags: [security, authentication, ssid, selection-matrix]

- id: f10
  title: Cirrus SSID 创建三段式向导流程（设置 → 网络指派 → 计划与 VLAN 映射）
  type: framework
  source_chapter: "p312"
  source_quote: |
    "SECTION 1 « SSID SETTINGS » ... Select the SSID Usage • Each usage leads to a predefined template ... Authentication Strategy ... Default VLAN/Network ... Optional - ACL/QoS rules applied to the SSID
    SECTION 2 « NETWORK ASSIGNMENTS » • Apply the SSID to one site • Apply the SSID to one or multiple AP Groups
    SECTION 3 « SCHEDULE AND VLAN MAPPINGS» • Apply Schedule • Always available • Customized schedule ... • Apply VLAN/Tunnel Mapping • One or multiple VLAN • One Guest Tunnel"
  summary: |
    Cirrus 建 SSID 固定走三段式：第一段定 SSID 本体（Profile 名、广播名、Usage 模板、认证策略、默认 VLAN/网络、可选 ACL/QoS 与 Walled Garden），第二段做网络指派（选定站点，再勾一个或多个 AP Group，同一 SSID 可跨组下发），第三段做计划与映射（按组设置上线时间表，逐组编辑 VLAN/Tunnel 映射，可选单 VLAN、VLAN 池最多 256 个或 Guest 隧道）。所有 SSID（员工 802.1X、访客、BYOD、PSK）都复用这一个骨架，只是第一段的参数不同；先建好 VLAN 与三层接口再回来映射是实验中固定的前置顺序（p334-337）。
  tags: [ssid, wizard, workflow, vlan-mapping, ovc]

- id: f11
  title: PSK 密钥体系四级选型（全局 PSK / 设备专属 PSK / 私有组 PSK / 动态组 PSK）
  type: framework
  source_chapter: "p326"
  source_quote: |
    "Device Specific PSK: Option Device Specific PSK is enabled; Device performs MAC authentication; In the Company property database, a specific PSK pass phrase is assigned to the MAC address of the device
    Private Group PSK: A user connects to the SSID with one of the passphrase in PPSK entries. He is assigned to the ARP attached.
    Dynamic Private Group PSK: A user uses one passphrase from the list, and is assigned to the corresponding VLAN ID and ARP."
  summary: |
    同一个 PSK SSID 下按"一钥 → 一设备一键 → 一组一键 → 一键绑定 VLAN+角色"逐级演进：全局 PSK 全员共享一个口令；DSPSK 开 MAC 认证后在 Company Property 库按设备 MAC 发专属口令（Force 模式彻底取消全局口令，Prefer 模式保留兜底）；PPSK 建多条口令条目，每条绑定一个 Access Role Profile，用哪条口令就落哪个角色；动态 PPSK 再把口令条目与 VLAN ID、ARP 双绑定，同一 ARP 可复用于多个 VLAN，免建大量角色。选型看运维粒度：哑终端分设备管、部门分组管、租户/工种按 VLAN 隔离时选动态。
  tags: [psk, security, ssid, selection, role]

- id: f12
  title: UPAM Guest 访问策略工作流（Guest SSID 六步开通）
  type: framework
  source_chapter: "p360"
  source_quote: |
    "How it works
    • Create a Guest SSID with the usage « Guest Network »
    • Activate the Captive portal option
    • Select the RADIUS server in the Authentication Strategy
    • Create a Guest account if the UPAM internal RADIUS server is used
    • In the Guest Access Strategy, define the login method (username and password) and Post portal enforcement to restrict Guest traffic
    • Assign a VLAN to the Guest SSID"
  summary: |
    访客网络的开通六步：建 Usage 为 Guest Network 的 SSID → 打开强制门户选项 → 认证策略里选 RADIUS 服务器（通常用内嵌 UPAM）→ 在本地库建访客账号（可批量导入 CSV/XLSX）→ 在 Guest Access Strategy 里定登录方式（账号密码/接入码/使用条款/自注册，p357-358）并配 Post Portal Enforcement 限制访客流量 → 最后给 SSID 绑定 VLAN。验证用 UPAM 的 Authentication Records 与 Captive Portal Records 两张记录表（p383）。Express 单机场景对应简化版：内嵌门户三选一认证 + 带有效期的访客账号（p151）。
  tags: [upam, guest, captive-portal, workflow, ssid]

- id: f13
  title: UPAM BYOD 访问策略工作流（预认证/后认证双 VLAN 切换）
  type: framework
  source_chapter: "p365"
  source_quote: |
    "How it works
    • Employee connects to the BYOD SSID and is redirected to the Captive Portal
    • BYOD SSID is open with network access restrictions
    • Employee provides its corporate credentials to register his personal device
    • Employee is now allowed to access the corporate network"
  summary: |
    员工自带设备（BYOD）走"先Guest 后员工"的双阶段准入：SSID 本身开放但有网络限制，员工连上被重定向到员工门户，输入企业凭据完成注册后获得正式网络访问。落地配置的关键是两个 VLAN：SSID 级 VLAN 映射指向访客 VLAN（预认证沙箱），BYOD Access Strategy 的 Post Portal Enforcement 里新建 Access Role Profile 并映射到员工 VLAN（p391-393），认证成功即将终端从 VLAN30 搬到 VLAN20，可在 Clients 视图按 VLAN 核验。认证源可选本地库、外部 LDAP/AD 或 RADIUS（p362）。
  tags: [upam, byod, workflow, vlan, post-auth]

- id: f14
  title: Unified Policy 条件—动作—绑定配置流程
  type: framework
  source_chapter: "p414"
  source_quote: |
    "(p405) Configure the policies first ... Assign the policies in the policy list ... Assign the Policy List to an Access Role Profile
    (p413-414) The first step is to create a Policy Condition. A policy Condition defines the type of traffic that will be inspected in the network devices. ... The next step is to define the Action. A policy action defines the treatment that will be given to the traffic that matches the condition."
  summary: |
    统一策略的配置顺序固定为"先策略后绑定"：第一步建 Policy Condition（如 L3 目的子网 + L4 服务端口，端口对象不存在就先建 Service Port），第二步定 Action（放行/丢弃、优先级、带宽等 QoS 动作），第三步做 Group Assignment 指定生效的 AP Group，最后把策略（列表）挂到 SSID 对应的 Access Role Profile 的 ACL/QoS 框里生效。策略动作是双向执行的，可来自 RADIUS 账号属性或 ARP 默认策略（p404）。验证手法：先测策略前基线（ping/SSH 通），再挂策略复测对比（p416 的 Block_SSH 实验）。
  tags: [policy, acl, qos, workflow, enforcement]

- id: f15
  title: 三层带宽控制模型与执行优先级（SSID / 角色 / 策略）
  type: framework
  source_chapter: "p408"
  source_quote: |
    "Bandwidth contract at SSID level • Configured in "Detailed SSID Settings" • Bandwidth assigned per SSID and per AP, shared between all users connected to the SSID
    Bandwidth contract at Access Role Profile level • Configured in "Bandwidth Control" section • Bandwidth assigned to the users using this profile
    Bandwidth contract at Role level • A Policy List (ACL/QoS) can restrict the Bandwidth as an action • Bandwidth limited by the ACL/QoS Rule"
  summary: |
    带宽治理分三层落点：SSID 级合同按"每 AP 每 SSID"限总带宽、组内用户共享；Access Role Profile 级合同限制使用该角色的每个用户；策略级在 Policy List 里用 ACL/QoS 规则对命中流量限速。执行时的优先级判定（p409 流程图）：用户流量先过 Policy List，命中 ACL 就按策略限速，否则看角色是否设带宽，再否则看 SSID 是否有合同，都没有则不限速——即"策略最细最优先，SSID 合同是兜底"。设计套餐时按此分层：全员总量用 SSID 合同、身份差异化用 ARP、应用级精细控制用策略。
  tags: [bandwidth, qos, policy, role, design]

- id: f16
  title: RF Profile 创建—绑定—验证—回退流程（含 Band Steering 风险规避）
  type: framework
  source_chapter: "p463"
  source_quote: |
    "The RF profile is contained in the Provisioning configuration of your AP Group. This is where we are changing it. ... Note that it is also possible to assign an RF Profile to a specific AP (instead of an AP Group). ... Assign the default RF Profile back to the Provisioning Configuration associated to your AP Group"
  summary: |
    射频参数管理的标准闭环：先建 RF Profile（通用设置含国家码 → Smart Load Balance 段 → Per Band Info 按频段细配），再经由 AP Group 的 Provisioning Configuration 换绑生效（也可在 Device Catalog 对单 AP 覆盖），然后用客户端连接行为与 QoE 分析验证（p464 的关联失败列表），出问题把 Provisioning Config 换回 Default RF Profile 即回退。Band Steering 默认关闭有明确原因（p459）：它假设 2.4G/5G 覆盖对等，若 5G 覆盖差会把终端逼进弱信号区，补救是按双频同覆盖设计网络，或用 Exclude MAC OUI 放行扫描枪等时延敏感终端。
  tags: [rf, workflow, rf-profile, band-steering, rollback]

- id: f17
  title: RF 优化参数推荐基线表（负载均衡/扫描/信道功率/信道宽度）
  type: framework
  source_chapter: "p451"
  source_quote: |
    "Smart Load Balance / Band Steering: Enable ... Signal Strength/Client SNR Threshold: Keep default threshold • Low value recommendation is 10, many weak client can associated, overall throughput is low. • High value recommendation 25, weak client cannot associate, overall throughput is better.
    Scanning / Background scanning: Enabled, Only required for WIPS
    Channel & Power: Auto Mode, It is recommended to use auto channel & power instead of static setting.
    Channel Width: Keep Default settings, Narrow width for dense AP deployment, Large width for sparse AP deployment"
  summary: |
    一份可直接抄的射频调优基线：Band Steering 与动态负载均衡默认开启；RSSI 阈值取低值（10）容忍弱终端但拉低整体吞吐、取高值（25）拒绝弱终端保吞吐，按业务取舍；背景扫描仅为 WIPS 所需，间隔/时长保持默认——扫描更勤则入侵检出率高但客户端性能降，反之亦然；信道与功率优先 Auto（ACS/APC 基于邻居共享的射频上下文决策，p449）；信道宽度按部署密度选，密集布点用窄宽抗干扰、稀疏用宽宽提吞吐。Smart Load Balance 的机制支撑见 p445-447（频段差值阈值、信道利用率超 70% 判过载、新客户端引导至负载最轻 AP）。
  tags: [rf, optimization, baseline, best-practice, tuning]

- id: f18
  title: 漫游模式判定决策表与快速漫游配置指南
  type: framework
  source_chapter: "p489"
  source_quote: |
    "Check the roaming conditions ... Based on the VLAN ID between the "home" and "foreign" AP, select either: • Layer 2 Roaming (default) • Layer 3 Roaming
    Check the security level of the SSID (WPA/WPA2/WPA3, Enterprise/Personal)
    • OKC can be enabled with WPA2/WPA3 Enterprise only
    • 802.11r (Fast Roaming) can be enabled with WPA/WPA2 encryption only (Personal or Enterprise)"
  summary: |
    漫游配置的判定顺序：先按归属 AP 与目标 AP 间的 VLAN 关系选模式——客户端上下文存在、WLAN 服务与角色匹配且 VLAN 一致则 L2 漫游（默认），上下文在但 VLAN 不一致则走 L3 漫游（L2 GRE 隧道回 home AP，p476 决策表）；再按 SSID 安全级别选快速漫游——OKC 只配 WPA2/WPA3 企业版，802.11r 要求 WPA2/WPA3 加密。配套检查：用 Heat Map 分频段确认覆盖有重叠（p490）；地理相邻但射频互不可见（直角走廊）时在两台 AP 上手工互加 Neighbor AP（p491）；粘性客户端用 Roaming RSSI 阈值（2.4G 建议 10、5G 建议 15）配合 802.11k/v 引导切换，阈值过低赖着不走、过高频繁漫游丢包（p492）。
  tags: [roaming, 802.11r, decision-tree, guidelines, l2-l3]

- id: f19
  title: WIPS 三分类框架与 Rogue 判定策略矩阵
  type: framework
  source_chapter: "p514"
  source_quote: |
    "Interfering AP • Any other APs discovered over the air • These APs are marked as Interfering • APs managed by the same OVC 10 are excluded
    Rogue AP • Based on the Rogue AP Policy ... Rogue AP Containment – enabled by default • The scanning Stellar AP sends de-auth request to all clients associated to the rogue AP
    Friendly AP ... An Interfering or Rogue AP can be set as Friendly AP manually"
  summary: |
    WIPS 的分类决策框架：空口发现的外部 AP 默认全部标 Interfering（本云管的 AP 除外）；命中 Rogue AP Policy 四条规则之一才升级为 Rogue——信号强度超阈值（默认 -70dBm）、广播了我方合法 SSID（Detect Valid SSID，默认启用）、SSID 名含黑名单关键词、MAC OUI 匹配（p515）；人工标记的 Friendly AP 永不被判 Rogue（含 ALE OUI 默认白名单）。Rogue Containment 默认开启，扫描 AP 会向 Rogue 的关联客户端发去认证帧，因此分类参数要谨慎调，误伤后果大。配套还有 AP/客户端攻击检测分级（高/中/低/自定义）与客户端黑名单（默认 60 秒内认证失败 10 次拉黑 1 天，p516-517）。
  tags: [wips, security, classification, rogue-ap, policy]

- id: f20
  title: Wi-Fi 勘测类型选型矩阵（预测 / 被动 / 主动）
  type: framework
  source_chapter: "p529"
  source_quote: |
    "Passive • Listen WLAN traffic • No authentication and 802.11 association • All frequencies are scanned • Detects Access Points • Measure signal strength • Measure noise
    Active • Associate survey tool to (multiple) access point • Same measures as passive survey • Measure packets loss • Measure retransmission • Measure physical rates
    Predictive • Simulation tool • Import site plan & RF characteristics of objects • Model RF environment • Deploy (automatically) AP on the map"
  summary: |
    按项目阶段选勘测方法（p530 映射）：新建网络前的规划用预测式勘测，导入平面图与材质衰减特性建模自动摆 AP，无需现场测量；部署后做射频体检用被动勘测，只听不发（不关联不认证），全频段扫描 AP、信号强度与噪声；评估真实客户端性能用主动勘测，勘测终端实际关联 AP，在被动指标之上加测丢包、重传和物理速率；排障项目则被动+主动组合。信号质量的判读用书中的 RSSI 对照标尺（p454）：低 RSSI 区（约 -85 至 -71dBm）判 Bad 不适合音视频，高档位为 Desired 推荐区。
  tags: [survey, methodology, selection-matrix, rf, planning]

- id: f21
  title: 现场无线排障三步法（平面图 → 勘测观察 → 纠正措施）
  type: framework
  source_chapter: "p537"
  source_quote: |
    "Step 1 – Get the floor plans • Identify potential issues: obstacles, walls, ceiling height,… • Identify areas where Wifi is required: offices, labs, welcome desk,… • Locate Access Point
    Step 2 – Site Survey observation • Identify Access Point model : same as original design? • Identify RF overlap between Access Points : Co/Adjacent channel interference? • Identify areas with no radio coverage ... • Access Point location: Troublesome placement?
    Step 3 – Corrective actions • Change Access Point model ... • Rework RF wireless design ... • Improve AP placement"
  summary: |
    "Wi-Fi 网络性能不达标"的现场处理流程：第 0 步先定义问题（Where/When/Who/How 圈定范围与测试点）；第 1 步拿平面图，标出障碍物、需要覆盖的区域（按优先级分级）和现有 AP 位置；第 2 步实地勘测观察，逐项核对 AP 型号与设计是否一致、AP 间射频重叠有无同频/邻频干扰、有无覆盖空洞（AP 掉线或缺位）、发射功率是默认还是改过、安装位置是否别扭；第 3 步给纠正措施，从换 AP 型号、重做射频设计（功率/信道）、收窄信道宽度、砍掉低速率逼终端贴近 AP，到挪 AP 或新增 AP（p540）。
  tags: [troubleshooting, survey, workflow, on-site]

- id: f22
  title: Wi-Fi 信号劣化四大原因清单（位置/材质/天线/干扰）
  type: framework
  source_chapter: "p533"
  source_quote: |
    "Signal degrades when going through:
    • Concrete (walls) • Wood (doors) • Metal (cabinet, shelves,…) • Steel (building structure) • Glass & Mirrors • Brick (fireplace) • Water (liquid: fish tank; vapor: bathroom)
    (p532) Access Point placement: bad location (wall, pillar) ... (p534) directional or omnidirectional ... Wrong type of antennas ... (p535) Co-channel Interference / Adjacent channel Interference ... Loss of throughput → Change AP channel"
  summary: |
    信号差的归因清单按四类排查：一是 AP 安装位置，正对混凝土墙/柱会自己挡自己，应在障碍物两侧各放一台；二是穿透材质衰减，混凝土、木材、金属柜架、钢结构、玻璃镜面、砖、水（鱼缸/浴室水汽）都会显著掉信号，书中的实例是 4 米穿 1-4 面墙后 RSSI 只剩 -70dBm 不够无线语音；三是天线类型选错，定向天线覆盖小扇区、全向覆盖整圆，要按环境选型（外置天线 AP 型号尾数带 2，如 AP1322）；四是同频/邻频干扰，表现为吞吐下降、丢包、数据损坏，对策是换信道。与三步排障法（f21）配合使用，作为第 2 步的观察维度。
  tags: [troubleshooting, rf, attenuation, antenna, interference]

- id: f23
  title: 客户端接入故障排障命令链（802.1X 与强制门户两套）
  type: framework
  source_chapter: "p347"
  source_quote: |
    "Check that the Radius configuration and AAA server profile have been correctly retrieved by the Stellar AP: cat /var/config/wlanservice.conf / AAA_profile.conf / AAA_server.conf
    If the radius authentication still fails:
    - Capture and analyze the data by using the following command: tcpdump -i br-wan –s 0 host radiusIP
    - Check the Radius server configuration"
  summary: |
    无线客户端连不上时的 AP 侧排查链（support/aos2016 登录）：先用 iwconfig 看无线配置与信号、iwlist channel/txpower/bitrate 确认信道功率速率（p343-344）；再用 ssudo sta_list / wlanconfig / wam_debug sta_list 列出关联客户端及其 VLAN、角色、各类认证结果字段（p345-346）；再 cat /proc/kes_syslog | grep MAC 查该客户端日志；802.1X 失败则核对 AP 是否正确收到 RADIUS/AAA 配置（三个 .conf 文件），仍失败用 tcpdump 抓 RADIUS 报文并查服务器侧。访客/CP 类问题另有一套（p385-388）：先查 AP 日期时间（账号有有效期）和 DNS（重定向必需），再看 eag 进程、eag_cli show user 列已认证用户、tail eag 日志。
  tags: [troubleshooting, client, cli, 802.1x, captive-portal]

- id: f24
  title: RAP 远程接入点五步上线流程（预配置 + 三段管理面配置）
  type: framework
  source_chapter: "p499"
  source_quote: |
    "[PRE] – Settings to be Entered by the Administrator
    1 – Stellar Access Point Startup & Registration
    2 - VPN & OmniVista 2500 Settings Retrieval
    3 - VPN Tunnel (Management Traffic) Establishment
    4 – Configuration Settings Retrieval
    5 – VPN Tunnel (Clients Traffic) & Client Connection"
  summary: |
    远程 AP（分支/家庭办公延伸企业网）的上线时序：管理员预置三处参数后，AP 上电即自动走五步——凭序列号向 Cirrus 注册 → 从 Cirrus 取回 RAP 模式、VPN 服务器公网地址、客户端 VPN 地址池、OV2500 地址 → 建管理流量 VPN 隧道 → 从 OV2500 拉取 SSID/射频等配置 → 再建第二条客户端数据 GRE 隧道，远程用户连企业 SSID 即入网。管理面配置对应三段（p508）：配 Cirrus（建专用 RAP 组织、声明序列号、配 Mgmt VPN、导出 .conf）、部署/配置 VPN 服务器虚拟机（双网卡+导入 .conf）、配 OV2500（加回程路由、发现 RAP、配 Data VPN 并指派、建走隧道的 SSID）。
  tags: [rap, vpn, remote-deployment, workflow, branch]

- id: f25
  title: Cirrus 组织清理与配置回退流程（按依赖逆序拆除）
  type: framework
  source_chapter: "p544"
  source_quote: |
    "As OmniVista Cirrus is cloud-based, it is not possible to revert the configuration back to the default parameters with one click. You can use this lab as a guideline if you need to replace your network devices, move to a new office or building, or reconfigure your network."
  summary: |
    云管没有一键恢复出厂，清理必须按依赖关系逆序手工拆：先删计划升级、备份、排障任务并复位 WIPS 策略 → 把 AP 从自定义 AP Group 摘回 default device group → 给 AP Group 换回默认 Provisioning Config 再删组、删自定义 Provisioning Config（其中引用的自定义 RF Profile 也要先换回默认才能删）→ 删 SSID、统一策略、服务端口、BYOD/Guest 策略、门户模板、ARP、账号、报表、站点，最后确认 Device Catalog 已空。该顺序同样适用于换设备、搬办公室、重配网络的交付场景——先解除引用再删除对象，否则会报错。
  tags: [cleanup, teardown, dependency-order, workflow, ovc]

- id: f26
  title: OmniVista Cirrus 许可订阅生命周期流程（eBuy → 订阅 → 导入 → 验证）
  type: framework
  source_chapter: "p173"
  source_quote: |
    "Subscription manager • Create the subscription • Lifecycle operations: • Renewal, • Add-on, • Extension, • Transfer, • …
    OmniVista CIRRUS • Import of licenses • Order ID • Activation code
    Alcatel-Lucent Enterprise eBuy • License ordering"
  summary: |
    云管许可的端到端流程横跨三个系统：在 eBuy 下单（Other Services & Items 里填许可型号与数量，型号编码含等级 BAS/BIZ/PRM、年限、设备类别，p172、p174）；到 Subscription Manager 用订单创建订阅、填客户信息，拿到 Subscription ID 与 Activation Code（购买到出现在订阅管理器最多 24 小时，p175-177）；再回到 Cirrus 组织内 License Management 导入订阅（选 CAPEX、填 ID 和激活码）、选择自动或手工把许可指派到设备、确认升级到付费模式（p211-215）；最后核验许可模式、时长、订阅类型与数量（p216）。试用转正式也走同一条导入路径。
  tags: [license, subscription, workflow, ebuy, administration]

- id: f27
  title: 访客账号配额治理框架（Service Level / Registration Profile / 配额与耗尽处理）
  type: framework
  source_chapter: "p429"
  source_quote: |
    "Defines, per user, a validity period, a time and data quota and an exhaustion handling, when the quotas are reached.
    ▪ Name ▪ Data/Time Quota ▪ Validity Period • Remember Device • Max Device Number ▪ Exhaustion Handling"
  summary: |
    访客上网的治理由三层对象组合：Registration Profile 定义每用户的流量配额（MB）、时长配额（每日小时数/总小时数）、有效期、是否记住设备与最大设备数，以及配额耗尽后的处理——阻断剩余时长（可配重定向 URL）或降速（分别设上行/下行 kB/s）；Service Level（最多 5 档）把 Access Role Profile、统一策略列表、注册档案、账号有效期与删除策略打包成服务等级，供批量开户引用（p428）；全局设置再管批量账号生成、过期后删除策略与登录密码策略（p427），访客工单可自定义页眉页脚并打印（p431）。日常运营交由 Guest Operator 前台账号开号、审自注册（p432-434）。
  tags: [guest, quota, service-level, lifecycle, upam]

- id: f28
  title: Express 模式员工与访客 SSID 创建流程（内嵌门户三种认证 + AP 内置 DHCP 三步）
  type: framework
  source_chapter: "p151"
  source_quote: |
    "The internal captive portal is activated by default. Now the authentication type must be selected (account, access code, or terms of use):
    - If the authentication mode account is selected, an account must be created
    - If the authentication mode access code is selected, an access code must be created
    - If the authentication mode Terms of use is selected, the guest access attempt will be authorized if he accepts a terms of use (customizable)"
  summary: |
    无网管 SMB 场景下的双 SSID 标准做法：员工 SSID 用 Personal 密码 + 高级设置里指 VLAN（p147）；访客 SSID 用 Open + 内嵌 Captive Portal + 指访客 VLAN，门户认证三选一——账号（建带起止日期的访客账号）、接入码、仅勾选使用条款，Operator 受限账号可交给前台只管访客开户（p159）。无基础设施 DHCP 时启用 AP 内置服务三步走（p154-157）：在 AP Networks 给目标 vlan 配 IP/DNS → 建 DHCP 池（网关、起止范围、DNS）→ 用 Bind Network 把池绑定到该 vlan。验证模式统一为"连接后检查 IP 落在对应 DHCP 段、ping 网关"。
  tags: [express, ssid, captive-portal, guest, dhcp, workflow]
```
