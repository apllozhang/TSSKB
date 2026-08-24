# frameworks.md · 决策框架/思维模型/结构化方法候选（OmniAccess Stellar WLAN Presales Ed28）
> 提取阶段产物，未做筛选，宁多勿漏；后续有独立验证阶段。
> 引用均为书中英文原文，source_chapter 为原文页码标记。

```yaml
- id: f01
  title: AP 选型三维矩阵法（Wi-Fi 代际 × 室内/外形态 × 市场分层）
  type: framework
  source_chapter: "p11"
  source_quote: |
    "OMNIACCESS STELLAR LINEUP – WI-FI 6: Wi-Fi 6 Indoor MLE AP132x / Wi-Fi 6 Outdoor Rugged AP136x / Wi-Fi 6 Indoor SMB AP1311 / Wi-Fi 6 Indoor SMB AP1301 / Wi-Fi 6 Indoor MLE AP1351 / Wi-Fi 6 Indoor MLE AP1331 / Wi-Fi 6 Indoor Hosp. AP1301H"
  summary: |
    全书把 AP 产品线组织成一张三维选型矩阵：第一维是 Wi-Fi 代际（5/6/6E/7，p10-13 分页陈列），第二维是部署形态（Indoor 室内 / Outdoor Rugged 室外加固），第三维是市场分层（MLE 中大型企业 / SMB 中小企业 / Hosp. 医疗酒店特化）。
    售前接到需求后按三个维度逐层收窄：先按预算与终端能力定代际，再按安装环境定形态，最后按客户规模与行业定档位（如酒店病房选 AP1301H，室外选 AP1361，Wi-Fi 7 中端选 AP1521）。
    这个"代际×形态×分层"的收窄式选型结构可直接迁移到任何硬件产品线的选型话术。
  tags: [selection, ap, product-matrix, wlan]

- id: f02
  title: 网络管理模式三选一决策法（Express 免管 / Enterprise 本地 / Cloud 云管）
  type: framework
  source_chapter: "p41"
  source_quote: |
    "NETWORK MANAGEMENT MODES - OVERVIEW: Wi-Fi Express Standalone mode; Wi-Fi Enterprise - In Premise - Managed mode with OmniVista 2500 NMS; Wi-Fi Cloud - Cloud based - Managed mode with OmniVista Cirrus NMS. Move from Express to Enterprise/Cloud when/if needed. Small and Medium Networks (SMB). Medium to Large Networks. Small, Medium and Large Networks."
  summary: |
    这是全书第一根主轴：同一套 Stellar AP 硬件有三种玩法——Express 免许可证自管集群（面向 SMB）、Enterprise 本地 OV2500 管理（面向中大型/安全敏感客户）、Cloud 由 OmniVista Cirrus 云管（各规模通用）。
    决策变量有两个：客户网络规模（小→中→大）和管理方式偏好（免管 / 本地部署 / 云订阅），且明确"可先上 Express、需要时再迁到 Enterprise/Cloud"，给客户一条成长路径。
    售前用法：客户说"我只要简单 WiFi"就推 Express（5 个免费 License 起步），合规要求本地部署推 OV2500，多分支连锁推 Cirrus 云管。
  tags: [selection, management-mode, express, cloud, on-premise]

- id: f03
  title: Express 免管集群规模与弹性设计法（255 上限 + 多组分簇 + 冗余建议）
  type: framework
  source_chapter: "p46"
  source_quote: |
    "A Group can not contain more than 255 APs. The 256th AP is not taken into account. Will stay in 'joining' mode. To have more than 255 APs on a network it is necessary to configure several Group-ids or to configure two separate VLANs"
  summary: |
    Express 模式下的容量设计规则：一个 AP-Group（集群）硬上限 255 台，第 256 台会卡在 joining 状态不纳管；超过 255 台必须拆多个 Group-ID 或分 VLAN 部署，每个集群各自形成独立的管理域与射频域。
    配套弹性建议（p48）：集群超过 64 台就要做网络层冗余，每台 OmniSwitch 最多接 32 台 AP、每个堆叠最多 64 台，且每个堆叠里至少放 2 台能当 PVM/SVM 的 AP 型号。
    这套"上限→拆分→冗余"的三段式容量设计法可直接用于 SMB 场景的方案设计与答标时的规模质疑。
  tags: [sizing, express, cluster, design, wlan]

- id: f04
  title: Express→Enterprise 平滑迁移升级法（先小后大的成长路径）
  type: framework
  source_chapter: "p66"
  source_quote: |
    "Factory Default mode: WiFi Express. AP Mode is hard coded at first boot: Mode can not be changed. Requires a factory reset (push button) and reboot. Migration from existing Express to Enterprise mode: From the Web interface, load the new software. Add option 138 in the DHCP server for the AP management scope. Perform a factory reset/reboot. No configuration migration, AP 'cluster' configuration is lost"
  summary: |
    出厂默认即 Express 模式，模式在首次启动时固化；判定机制很简单——DHCP 没下发 option 138 就是 Express 集群，下发了 OV2500 地址就转 Enterprise（p67 同流程）。
    迁移四步：Web 界面加载新版软件 → 在 DHCP 管理作用域加 option 138 → 恢复出厂并重启 → 重新注册；关键风险提示是原集群配置不迁移、会全部丢失，必须提前向客户声明。
    售前价值：用"今天 Express 明天 Enterprise"降低 SMB 客户首购门槛，同时把配置丢失这个坑写进实施合同边界。
  tags: [migration, express, enterprise, dhcp-option-138, upgrade-path]

- id: f05
  title: AP 纳管注册三条件判定流（Trusted / Licensed / Country Code）
  type: framework
  source_chapter: "p68"
  source_quote: |
    "AP is managed when Registration succeeds: AP is Trusted, AP is Licensed, Country Code matches RF profile CC. AP is unmanaged when Registration fails: AP is not Trusted, AP is not Licensed, Country Code does not match the Country Code from the RF Profile... Configuration not applied, All Radios are off"
  summary: |
    AP 能否被 OmniVista 纳管由三个条件与门决定：可信（默认需管理员手动 Trust，手工导入/创建的 AP 视为可信）、有 License、AP 国家码与 RF Profile 国家码一致。
    三个条件全过才推配置进 AP Group，任一失败即"Unmanaged"，不下发配置且所有射频关闭——这条判定流是排查"AP 上线但不上班"类问题的标准检查清单。
    该"准入三条件 + 失败即静默"的模式可迁移到任何网管系统的新设备接入排障话术。
  tags: [troubleshooting, registration, onboarding, decision-flow]

- id: f06
  title: WiFi Bridge vs WiFi Mesh 选型法（按"是否要给终端提供服务"二分）
  type: framework
  source_chapter: "p110"
  source_quote: |
    "WIFI BRIDGE AIM: Replace physical cabling. PROPERTIES: VLANs can be used to separate & secure traffic over the bridge. Cannot provide service (WiFi) to WiFi clients. WIFI MESH PROPERTIES: VLANs can be used to separate & secure traffic coming from Wi-FI clients connected on different SSID. Can provide service (WiFi) to WiFi clients"
  summary: |
    两个无线回程方案按单一判据二分选择：只做"替代布线"（跨街楼宇、露营地理点对点/点对多点连接）选 WiFi Bridge，桥接链路上还能用 VLAN 隔离流量但不能给终端发 WiFi；既要回程又要给手机笔记本提供覆盖，选 WiFi Mesh。
    配套工程参数（p112）：Mesh 上限 8 台从 AP、4 跳、全网 16 台；最佳实践是回程用 5GHz（Wi-Fi 6E 可 6GHz）且信道选 100 以上。
    这是"目标→属性→限制"三段式选型结构，可迁移到任何两类相近技术的选择论证。
  tags: [selection, bridge, mesh, wireless-backhaul]

- id: f07
  title: License 三体系总览选型法（免 License / OV2500 永久 / Cirrus 订阅）
  type: framework
  source_chapter: "p128"
  source_quote: |
    "STELLAR WLAN LICENSES: Stellar Express - No License, 5 permanent licenses; Stellar Enterprise On Premise (OmniVista 2500); Stellar Enterprise Cloud (OmniVista Cirrus 4)"
  summary: |
    商务层与 p41 的管理模式三选一一一对应：Express 完全免 License（且送 5 个永久授权，第 6 台起才需要转企业模式）；Enterprise 本地版走 OV2500 永久式买断 License；Cloud 版走 Cirrus 订阅制。
    这是"硬件与软件订阅分离"商务模型的骨架：同一台 AP，价格与商业形态由管理模式决定，售前报方案时必须先锁模式再拼报价，否则 License 会报错体系。
    讲给客户听的版本：小规模近乎零软件成本，规模上去后按"买断 vs 订阅"的 CAPEX/OPEX 偏好二选一。
  tags: [licensing, selection, business-model, ov2500, cirrus]

- id: f08
  title: OV2500 License 强制+可选模块组合法（1 必选 + 4 选配）
  type: framework
  source_chapter: "p131"
  source_quote: |
    "OV 2500 / Stellar WLAN Mandatory License: AP License - OV2500-NG-AP (Wireless support Discovery, Registration, Provisioning troubleshooting, Lifecycle management, Access Guardian, Application visibility and WLAN Analytics, RF management, WIDS, WiPS, Floor Plan, Heat map). OV 2500 / Stellar WLAN Optional License Modules: Guest License - OV2500-NG-GUEST; On-Boarding License - OV2500-NG-ONBOARDING; High Availability License - OV-NMS-HA; Web Content Filtering License - OV-AP-WCF"
  summary: |
    OV2500 的报价按"1 个强制 + 4 个选配"的模块结构组合：AP License（OV2500-NG-AP）必买，覆盖发现/注册/RF 管理/WIPS/热图等全部无线管理功能；访客接入（GUEST）、BYOD 入网（ONBOARDING）、双机高可用（HA）、网页内容过滤（WCF，10 台 AP 一份）按需加购。
    每类 License 有 20/50/100/500/1000 档位（p135），报价时按客户在网 AP 数、访客并发数、BYOD 终端数分档取整。
    这是典型的"基础平台 + 功能模块 + 容量档位"三层报价结构，可迁移到任何软件定义网络产品的报价组织。
  tags: [licensing, ov2500, quotation, modules]

- id: f09
  title: 报价四要素清单法（AP 设备 + License + 配件 + 维保合约）
  type: framework
  source_chapter: "p134"
  source_quote: |
    "QUOTATION NOTES: OmniAccess Stellar Access Points; OmniAccess Stellar Licenses; OmniAccess Wireless AP Accessories; Maintenance Contract"
  summary: |
    书里给出的报价防漏项清单就四个格：AP 硬件（OAW-APxxxx-Region，区域码 RW/JP/ME/US）、License（对应 p131/p135 的 OV2500 或 Cirrus 体系）、配件（安装支架 OAW-AP-MNT-X、PoE 供电器、电源、天线，p136 有编码规则）、维保合约（1/2/3/5 年）。
    维保编码本身也是一套可拆解语法（p137）：如 PW2R-OVBYOD100N = P 合作伙伴 / W 软件支持 / 2 年 / R 续保 / 100 用户；SP5N-OAWAP1201 = S 终端客户 / P 支持Plus含AVR / 5 年 / 新购。
    售前自查报价单时按这四格过一遍即可避免"漏配件、漏维保"这类最常见事故。
  tags: [quotation, checklist, licensing, maintenance]

- id: f10
  title: Cirrus 4 Freemium→Premium 双轨升级路径法（免费起步 + 订阅解锁）
  type: framework
  source_chapter: "p139"
  source_quote: |
    "Freemium: Self Registration, Free of charge, No device capacity limitation, No duration limitation, No network Configuration, On-time Network Device Upgrade, Restricted OV Cirrus capabilities, Can be upgraded to Premium. Premium: All OV Cirrus capabilities, Based on OV Cirrus Subscription, Flexible (Device type, capacity and Duration)"
  summary: |
    Cirrus 4 云管采用"免费版获客 + 订阅版变现"的双轨设计：Freemium 自注册、免费、不限设备数不限时长，但无网络配置能力、仅一次性升级；Premium 解锁全部能力，按设备类型/数量/时长灵活订阅。
    Premium 内部再分两层维度（p140-141）：License 按交换机系列分 LAN Core/Essential/Advanced（Stellar AP 不分型号 1 License/台，每台 AP 附送 50 Guest + 50 BYOD），服务包分 Base/Business/Premium（差别在 TAC 对设备的服务、AVR 硬件Next-Business-Day 等）。
    这是云服务典型的"入门免费-按需订阅-分级服务包"三层商业化结构，可直接迁移为 SaaS 类方案的商务叙事。
  tags: [licensing, cirrus, freemium, subscription, saas]

- id: f11
  title: Cirrus 10 订阅 Part Number 三维语法法（类别×级别×时长 = 63 个编码）
  type: framework
  source_chapter: "p153"
  source_quote: |
    "License category: Low end Stellar models: APL, High end Stellar models: APH, OmniSwitch 63xx model: 63... License level: BASE level : BAS, BUSINESS level : BIZ, PREMIUM level : PRM. License duration: 1 year : 1Y, 3 years : 3Y, 5 years : 5Y. Total number of license part numbers: 7 x 3 x 3 = 63 part numbers"
  summary: |
    新一代 Cirrus 10 的报价被压成一条可拼装的编码语法：OVCX-[类别 7 选 1]-[级别 3 选 1]-[时长 3 选 1]，共 7×3×3=63 个 part number。类别按设备型号归并（低端 AP=APL、高端 AP=APH、交换机 63/64/65/68/69 按系列），APL/APH 的划分规则在 p154（如 AP1431 归 APH）。
    级别 BAS/BIZ/PRM 对应服务权益梯度（p155：Base 无 TAC、Business 面向合作伙伴、Premium 面向终端客户），时长 1/3/5 年预付。
    售前只要知道设备型号、客户要的服务级别和年限，就能直接拼出 OVCX-68-BIZ-3Y 这类编码，这是"防报错"的语法化报价设计，可迁移到任何复杂 SKU 体系。
  tags: [licensing, cirrus10, part-number, syntax, quotation]

- id: f12
  title: 云订阅三步激活流程法（eBuy 下单 → Subscription Manager 建订阅 → 云端导入）
  type: framework
  source_chapter: "p158"
  source_quote: |
    "Subscription manager: Create the subscription. Lifecycle operations: Renewal, add-on, extension, transfer,… OmniVista Cirrus 10: Import of licenses - Order ID, Activation code. Alcatel-Lucent Enterprise eBuy: License ordering"
  summary: |
    云订阅从下单到生效固定三步：第一步在 eBuy 下单 License；第二步在 OVC Subscription Manager 里从已购许可池创建订阅（选数量、填客户信息），拿到 Subscription ID 和激活码；第三步在 OmniVista Cirrus 10 的 License Management 页面导入（选 CAPEX Subscription 模式），并把 License 逐台分配给设备。
    订阅创建后状态为"Created/Pending activation from OVC UI"即表示可在云实例里激活（p162）；后续续保、扩容、转让都在 Subscription Manager 里做生命周期操作。
    这套"下单→建订阅→云导入"三段流程是所有订阅制软件交付的通用骨架，可当作实施交接清单使用。
  tags: [licensing, cirrus10, activation, process, subscription]

- id: f13
  title: 行业用例四段式论证法（Identity→Challenges→Why ALE?→Benefits，附 Technical Description）
  type: framework
  source_chapter: "p171"
  source_quote: |
    "HOSPITAL: With the overhaul of the hospitals, the goal is to have a new Wi-Fi infrastructure to improve the service to the medical team and to the patients. Replacement of the existing Aruba infrastructure... Identity / Challenges"
  summary: |
    p169-199 的全部行业案例（医院、五星酒店、理工大学、文理学院、轮渡船队、音乐学院、零售 ESL）共用一个四段式模板：Identity 交代客户身份与规模（床位/学生/船队数），Challenges 列业务与技术挑战（常含"替换某竞品"），Why ALE? 给出选 ALE 的决定性理由（几乎每案都出现"合作伙伴+ALE 联合 POC"和"无控制器架构"），Benefits 按"技术/财务/体验"收口，最后补一页 Technical Description 落到具体型号与配置。
    反复出现的获胜理由可沉淀为话术库：controllerless 降维护成本（渡轮机舱没地方放控制器）、DPI 控流量、统一 LAN/WLAN 管理、POC 联合验证。
    这个四段式可直接改写成投标里的"客户现状-需求-方案优势-收益"案例页。
  tags: [use-case, storytelling, argumentation, verticals, presales]

- id: f14
  title: VoWLAN 五步部署法（Prepare→Plan→Design→Implement→Operate）
  type: framework
  source_chapter: "p206"
  source_quote: |
    "VOICE OVER WLAN DEPLOYMENT STEPS: Identify the Voice usages: understand the challenges and requirements. Prepare / Plan / Design / Implement / Operate. These are the major steps for the deployment of VoWLAN in a WLAN Stellar environment. Requirements: wireless infrastructure, Voice devices, environments, performance, security and management. Choice of architecture. Deploy and manage Voice users as per design. Provide Voice service to users, maintain and extend the service."
  summary: |
    无线语音项目被拆成五步生命周期：Prepare（p207 做站点勘察、算 AP 数量与布点）、Plan（p208 定语音业务/安全级别/射频策略/漫游策略）、Design（p209 选天线信道、端到端 QoS 标签、DPI 语音识别、语音专用 VLAN）、Implement（p210 布线、装服务器、配 RADIUS/DNS/DHCP/IMS3、模板化下发话机）、Operate（p211 监控 SNR、VoIP 审计、Ekahau 复测、专业服务兜底）。
    每步都有明确的输入输出物（如 Prepare 输出 AP 布点图，Implement 输出配置模板），是可直接当项目 WBS 用的方案骨架。
    售前答技术质疑时可按五步逐段给出 ALE 的对应能力，展示方法论完整性。
  tags: [vowlan, deployment, process, voice, qos]

- id: f15
  title: 无线语音容量工程常数法（每 AP 覆盖面积 / 并发用户数 / 漫游 RSSI 阈值）
  type: framework
  source_chapter: "p207"
  source_quote: |
    "PREPARATION - Requirements: What are the voice coverage requirements? What is the bandwidth required for the handsets and/or applications? What is the placement of the APs? ... Requirements for Voice: 1 access point / 255 m². Number of users per AP – Average of 20-25 users"
  summary: |
    语音覆盖勘察用三条可背的工程经验值快速估规模：语音场景 1 台 AP 覆盖约 255 平方米；单 AP 平均带 20-25 个语音用户，并按每 AP 36 Mbps 用户吞吐做容量规划（p208）。
    漫游门槛：一般要求 RSSI 达到 -62dBm 或更好才能保证正确漫游；射频策略 5GHz 优先（更鲁棒性能更好），为能力相近的终端规划专用 SSID，并在前台等关键位置做 AP 冗余覆盖。
    这些常数是售前在没有勘察数据时快速报 AP 数量、答客户"你们怎么算出来的"质疑的底牌。
  tags: [vowlan, capacity-planning, rules-of-thumb, rf-design]

- id: f16
  title: Network Advisor AI 运维三循环法（Identify→Mitigate→Optimize）
  type: framework
  source_chapter: "p227"
  source_quote: |
    "Identify: Detect issues/anomalies & trigger immediate alert. Understand the normal network behavior with Artificial Intelligence & Machine Learning. Mitigate: Propose a solution & the ability to fix the issue in one tap. Automatic corrective actions for abnormal behavior and cybersecurity threats. Optimize: Network fine tuning for better quality of experience. Leverage Rainbow CPaaS: collaborate to react faster and connect to applications and other AIs"
  summary: |
    Network Advisor 把 AI 运维闭环压成三个动词：Identify（用 AI/ML 学习"正常网络行为"，异常即告警，内置 40+ 预置异常库，p220）、Mitigate（在 Rainbow/Teams 气泡里一键修复或自动执行纠正动作）、Optimize（网络微调提升体验，并借 Rainbow CPaaS 连接应用与其他 AI 协作）。
    交付形态是边云混合：客户侧边缘计算引擎 + 云端管理应用 + 手机伴侣服务，且独立于 OV2500/Cirrus 单独销售。
    这个"识别-缓解-优化"三循环可作为任何 AIOps 产品的价值叙事框架，也方便售前按客户痛点选择切入循环。
  tags: [aiops, network-advisor, monitoring, loop, presales]

- id: f17
  title: 网络问题生命周期四阶段支撑法（把工具价值映射到问题时间轴）
  type: framework
  source_chapter: "p228"
  source_quote: |
    "WHERE CAN THE ALE OMNIVISTA NETWORK ADVISOR HELP YOU? Network Issues Lifecycle / Production Environment: User problem observed → Partner creates Service Request → Problem closed. Facilitate the capture of information. Audit the configuration. Continuous Data Collection. Early Detection. Preventive remediation with Admin Notification. Instantaneous intervention. Minimize impact & side effects. Proactive data collection & Admin Notification"
  summary: |
    这页把一个网络问题的生命周期画成四段（问题潜伏→用户报障→创建服务请求→问题关闭），并在每一段上标注 Network Advisor 的介入点：事前持续采集数据与配置审计、事前早期检测与管理员通知、事中即时干预并最小化影响与副作用、事后主动采集数据支撑关单。
    这是"按客户工作流时间轴摆产品能力"的论证结构，比罗列功能更容易让运维负责人对号入座，可迁移到任何运维工具的售前话术。
  tags: [aiops, lifecycle, value-mapping, storytelling, network-advisor]

- id: f18
  title: 无线需求识别五要素法（终端 / 流量 / 环境 / 容量 / 覆盖场景对照）
  type: framework
  source_chapter: "p239"
  source_quote: |
    "WLAN COVERAGE SCENARIOS AND CHARACTERISTICS. In your project, identify: The client devices (type, number, authentication); The type of traffic (applications); The environment (indoor/outdoor, low/high density, open/complex environment); The capacity (number of clients, % of concurrent clients, uplink bandwidth required). Ex: Offices - Coverage / Applications / Authentication / Clients / Capacity / AP devices"
  summary: |
    部署指引章开篇给出需求澄清的五要素清单：终端（类型/数量/认证方式）、流量类型（应用）、环境（室内外/密度/开阔或复杂）、容量（客户端数/并发比例/上行带宽）、以及由此落到覆盖场景与 AP 选型的对照表（书中 Offices 示例：500+ 客户端、50%+ 并发、10G+ 上行 → 选 AP1231/AP13xx/14xx/15xx）。
    售前勘察前的需求访谈可以直接拿这五问当提纲，问完即可套入场景模板出初稿方案。
    这是"要素清单→场景模板→选型结论"的三级收敛结构，可迁移到任何方案前期的需求澄清环节。
  tags: [requirements, discovery, survey, checklist, wlan]

- id: f19
  title: 站点勘察二分法（Virtual 虚拟勘察 vs Physical 实地勘察）
  type: framework
  source_chapter: "p240"
  source_quote: |
    "Site Survey and capacity planning: Recommended for an optimal placement of the APs throughout the building/facility/outdoor space. Two type of surveys can be carried out: Virtual site survey - Software based. Simulates the environment and AP placement. Fine tune AP placement and output power. Physical site survey - On-site. Exact reading of how an AP performs. Discovery of hidden or unknown interferences. Goals: Analyze Radio Frequency (RF) environment. Identify Radio Frequency (RF) interferences. Find optimum location for Access Points"
  summary: |
    勘察方法二选一：虚拟勘察用软件建模，模拟环境与 AP 布点，反复微调位置和发射功率，成本低适合前期规划；实地勘察上现场实测 AP 真实表现，能发现隐藏/未知的干扰源，成本高但结论可靠。
    无论哪种，目标固定三个：分析射频环境、识别射频干扰、找到 AP 最优安装位置；配合容量规划一起做。
    用例章里 ALE 反复演示这一步（酒店 Ekahau 装后审计发现信道重叠、渡轮因金属结构增加室外 AP），说明"先勘察后部署"是投标方案的必备论证环节。
  tags: [site-survey, rf-planning, deployment, methodology]

- id: f20
  title: 客房场景 AP 密度计算法（墙体分级 + 数量公式 + 5% 冗余）
  type: framework
  source_chapter: "p243"
  source_quote: |
    "AP DEPLOYMENT IN HOSPITALITY ROOMS ... Solution: AP1301H: 2.4GHz and 5GHz dual radio frequency. 802.11ac. Up to 1024 clients. AP quantity = M/2+N+(M+N)*5%. Explanation: M: number of rooms with normal walls. N: number of rooms with load-bearing wall. 5%: represents the redundant backup. Example: 20 rooms M, 10 rooms N. AP quantity = 21,5. Rounded up to 22 AP1301H"
  summary: |
    医院/酒店客房这类高密度同构房间场景有专用估算公式：AP 数 = 普通墙房间数 M ÷ 2 + 承重墙房间数 N + 总房间数 × 5% 冗余，结果向上取整（例：20 普通 + 10 承重 = 21.5 → 22 台 AP1301H）。
    公式背后的物据是墙体衰减分级（p244-245）：普通墙衰减约 15dBm，可以隔房间装（-65dBm 最坏情况可用）；承重墙衰减约 30dBm，5GHz 穿墙后跌到 -80dBm 无法接入，所以承重墙房间必须一房一 AP。
    安装规范配套：壁挂高度 1.5 米以上、避开电视/金属柜等遮挡。这是"环境参数分级→数量公式→安装规范"三件套的密度规划方法，可迁移到宿舍、公寓等房间型场景。
  tags: [capacity-planning, hospitality, ap-dimensioning, formula, deployment]

- id: f21
  title: 场景化配置基线表法（按部署场景给出"特性→推荐值→理由"九项配置表）
  type: framework
  source_chapter: "p247"
  source_quote: |
    "RECOMMENDED CONFIGURATION - Features / Configurations / Descriptions: RSSI Threshold - 2.4G RSSI :20, 5G RSSI :15 ... ACS - Enable (The AP performs dynamic monitoring and selects the best channel) ... APC - Disable (recommended that the APs transmission power be manually adjusted) ... Band steering - Enable ... Traffic limitation - 2mbps for upload, 4mbps for download ... Load Balance - Enable"
  summary: |
    部署指引对每种场景（客房 p247、高密度场馆 p252、中小会议室 p261、室外 p263）都给一张同构的"特性→推荐配置→选择理由"表，覆盖 RSSI 门槛、漫游 RSSI、ACS 自动选信道、APC 自动功率、信道带宽（HT20/40/80）、频段引导、单机限速、BG-S、负载均衡、语音视频感知等约十项。
    表的精髓是同一特性在不同场景取值相反并有理由：客房全封闭环境关 APC 手动调功率、场馆手动锁信道且功率≤15dBm、会议室开 HT80 提容量——即"配置跟着场景走，不跟着默认值走"。
    这套基线表可以直接当实施交付的验收 checklist 和售前"我们不是拍脑袋配置"的证据，也示范了如何把产品特性库转译为场景化最佳实践。
  tags: [configuration, best-practice, scenario, deployment, checklist]
```
