# 框架/流程 · OmniAccess Stellar WLAN Express (DT00XTE455EN)

> 来源：source/fulltext.md（页码即教材 PDF 页码）。本书为 Express 免云管模式专题，流程类知识集中在集群、Bridge/Mesh 与勘测三章。

- id: f01
  title: 集群角色模型与 PVM/SVM 选举流程
  type: framework
  source_chapter: "p79-80"
  source_quote: |
    "In an AP group, one AP supports the role of centralized management. It is called PVM. (Primary Virtual Manager). All other APs are under management of the PVM of the group. They are called Members. Another AP is responsible for rescuing the centralized management role. It is called Secondary Virtual Manager (SVM). In the case of a VLAN with several APs started at the same time an election process is perform to select the PVM. Highest Model Type, Highest MAC address. AP with the second highest MAC is designated as the SVM."
  summary: |
    Express 集群的三角色模型：一个 AP-Group 内，一台 AP 担任集中管理角色即 PVM（主虚拟管理器），其余 AP 全部是 Member（成员）；另有一台 AP 负责接管备份，即 SVM（备虚拟管理器）。同一 VLAN 内多台 AP 同时启动时触发自动选举：先比型号等级（Highest Model Type），再比 MAC 地址（Highest MAC），最高者当 PVM，MAC 第二高者当 SVM。PVM 产生后广播一个用于配置 AP-Group 的 SSID（如 mywifi-0102），其余 AP 以成员身份加入，单组上限 255 台。排障时先确认谁是 PVM/SVM，再看目标 AP 是不是 Member。

  tags: [cluster, pvm-svm-election, express-mode]

- id: f02
  title: 集群扩展与分域设计流程（Group ID/VLAN 隔离 + 单 IP 管理）
  type: framework
  source_chapter: "p81-84"
  source_quote: |
    "A Group can not contain more than 255 APs. To have more than 255 APs on a network it is necessary to configure several Group-ids or to configure two separate VLANs. VLAN X > GROUP ID X, VLAN Y > GROUP ID Y. Clusters are on a separate VLAN or different Group Id. Distinct administration domain (PVM) and RF domain. Via a single IP interface (Group Mgt IP): Configuration synchronization, Group Management Interface, Notifications."
  summary: |
    网络规模超过 255 台 AP 时的标准拆分法：按"一个 VLAN 对应一个 Group ID"的映射建多个集群（VLAN X → Group ID X，VLAN Y → Group ID Y），每个集群拥有独立的管理域（PVM）和射频域，互不干扰。集群内部运行机制：成员 AP 之间通过单一 IP 接口（Group Mgt IP，组管理 IP）完成配置同步、组管理与通知；成员各自负责数据面管理、认证管理与本地 ACL；AP 间还建立 WLAN 邻接关系以感知彼此射频环境。设计时的口诀是"一 VLAN 一 Group ID，一集群一 PVM"。

  tags: [cluster-scaling, group-id, vlan-design, group-mgt-ip]

- id: f03
  title: AP 开箱到首次配置上线的六步流程
  type: framework
  source_chapter: "p57-62"
  source_quote: |
    "PREREQUISITES. POWER. IP ADDRESS ASSIGNMENT. MYWIFI CONNECTION. WEB INTERFACE ACCESS. AP CONFIGURATION."
  summary: |
    First Steps 模块给出的单台 AP 从零到可管理的标准路径：（1）确认前置条件；（2）上电（PoE 或 DC/适配器，硬件口为 RJ45 以太网、Console、复位按钮）；（3）IP 地址获取（DHCP 或手工指定，DHCP 失败时用默认 IP 192.168.1.254 兜底）；（4）连接出厂 SSID mywifi；（5）访问 Web 管理界面；（6）执行向导式初始配置。教材该章以界面截图演示为主，文字即这六步标题；后续所有配置（常规设置、SSID、集群）都建立在这六步完成之上。

  tags: [first-steps, onboarding, wizard, web-gui]

- id: f04
  title: WiFi Bridge 点对点部署流程（四属性一致 + 单根原则）
  type: framework
  source_chapter: "p112-113"
  source_quote: |
    "SSID: WLAN used to setup wireless bridge connection. Must be the same on both APs. Band: Wireless bridge working frequency. Must be the same on both APs. Is Root: Specify the root AP of the wireless bridge. 1 AP must be set as Root. Passphrase: Password of the WLAN. Must be the same on both APs."
  summary: |
    用无线桥替代跨街楼宇间的物理布线时，两端 AP 必须配齐四个属性且三点必须双方一致：SSID（桥接用 WLAN 名称）、Band（工作频段）、Is Root（是否为根，两端必须且只能有一台设为 Root）、Passphrase（密码）。教材示例：根端 SSID=STELLAR-BRIDGE、Band=5GHz、Is Root=Yes、Passphrase=ALCATEL123!；对端同 SSID/同频段/同密码、Is Root=No。桥接链路上可用 VLAN 分离与保护流量（注意 AP1101/1201/1201H 不支持）。配完四属性桥即建立。

  tags: [wifi-bridge, point-to-point, root-ap, vlan]

- id: f05
  title: WiFi Mesh 部署与 Auto Mesh 快速建网流程
  type: framework
  source_chapter: "p114-115"
  source_quote: |
    "AUTO MESH. Aim: quick & easy deployment of a Mesh topology. If a Stellar AP is: Connected to the LAN, Configured as MESH root, It will Broadcast an hidden SSID « Stellar-MESH », Band: 5 GHz. If a Stellar AP is: Not connected to the LAN, It will Have MESH enabled as non-root, Broadcast an hidden SSID « Stellar-MESH »."
  summary: |
    手工 Mesh 与 Bridge 属性相同（SSID/Band/Passphrase 双方一致），区别在于 Mesh 允许多台 AP 同为 Root，且 Mesh 节点同时可对客户端提供 WiFi 服务（教材示例：节点同时广播开放加密的 WIFI GUESTS 与回程 STELLAR-MESH）。Auto Mesh 是免配置建网法：把接 LAN 的 AP 配成 Mesh Root，它会自动广播隐藏 SSID "Stellar-MESH"（5GHz）；任何没接 LAN 的 Stellar AP 上电后自动以非根 Mesh 节点身份接入该隐藏 SSID，回程自动打通，实现"通电即入网"。最佳实践：回程用 5GHz（或 6GHz）、信道选 >100。

  tags: [wifi-mesh, auto-mesh, hidden-ssid, backhaul]

- id: f06
  title: 三种部署模式选型框架（Express/Enterprise/Cloud）
  type: framework
  source_chapter: "p40, p42, p44"
  source_quote: |
    "EXPRESS MODE: Self-managed standalone cluster, Up to 255 APs, Integrated secure Web managed, Wizard driven configuration, Integrated guest captive portal, Distributed intelligence control. ENTERPRISE MODE: Centralized management via the OmniVista 2500 NMS, Up to 4000 APs, [OV2500] Unified Access, Deep Packet Inspection, Floor Plan / Heat Map & Reporting. CLOUD MODE: Centralized management via the cloud platform OmniVista Cirrus NMS, Up to 4000 APs."
  summary: |
    Stellar AP 的管理模式三分法，选型看规模与管理平台：Express=无控制器、无云，AP 自组织集群，Web 向导管理，上限 255 台，内置客户门户与分布式智能，适合 SMB/小微；Enterprise=接入 OmniVista 2500 网管（OV2500），上限 4000 台，获得 UPAM 统一策略认证、DPI、热图与报表；Cloud=接入 OmniVista Cirrus 云管，功能与 OV2500 基本等同，上限同样 4000 台。同一批硬件三种模式皆可入，差别在管理面；本书后续章节全部围绕 Express 展开。

  tags: [deployment-modes, express, enterprise, cloud, sizing]

- id: f07
  title: 勘测类型选择框架（预测/被动/主动 × 部署前后）
  type: framework
  source_chapter: "p164-165"
  source_quote: |
    "Passive: Listen WLAN traffic, No authentication and 802.11 association, All frequencies are scanned, Detects Access Points, Measure signal strength, Measure noise. Active: Associate survey tool to (multiple) access point, Same measures as passive survey, Measure packets loss, Measure retransmission, Measure physical rates. Predictive: Simulation tool, Import site plan & RF characteristics of objects, No field measurements. Predictive: Pre-deployment, place new APs. Passive: Post-deployment, RF analysis. Active: Post-deployment, clients performance analysis."
  summary: |
    三类勘测按"是否到场、是否关联 AP"划分：被动勘测只听不发（不认证不关联），扫全频段，能发现 AP、测信号强度与噪声；主动勘测把勘测工具关联到一个或多个 AP，在被动指标之上加测丢包、重传和物理速率；预测勘测纯软件仿真，导入平面图与物体射频特性建模并自动布放 AP，无现场实测。项目阶段决定选型：部署前规划用预测；部署后做射频分析用被动；部署后分析客户端实际性能用主动。新建网、换网、排障三类项目分别对应这套组合。

  tags: [site-survey, passive, active, predictive, ekahau]

- id: f08
  title: 现场勘测排障三步流程（平面图→现场观测→纠正措施）
  type: framework
  source_chapter: "p172-175"
  source_quote: |
    "Step 1 – Get the floor plans: Identify potential issues: obstacles, walls, ceiling height… Identify areas where WiFi is required: offices, labs, welcome desk… Locate Access Point. Step 2 – Site Survey observation: Identify Access Point model: same as original design? Identify RF overlap… No radio coverage… transmission power: Default or customized value? Step 3 – Corrective actions: Change Access Point model… Rework RF wireless design… Rework channel width… Remove lower data rates… Improve AP placement."
  summary: |
    "WiFi 网络表现不佳"类工单的现场作业 SOP。第一步拿平面图：标出障碍物/墙/层高等潜在问题点，圈出需要 WiFi 的区域并分优先级，定位现有 AP。第二步现场观测五问：AP 型号是否与设计一致、AP 间是否存在同频/邻频重叠、无覆盖区是 AP 掉电还是压根没布、发射功率是默认还是改过、AP 位置是否别扭。第三步针对性行动：换 AP 型号（更好天线/户外型）、改发射功率与信道、收窄信道带宽压制干扰、删除低速率逼终端漫游到近处 AP、优化布放。教材 p174 给出五点标注的实例图（干扰正常/无覆盖/遮挡/默认功率 17dBm/挪 AP）。

  tags: [on-site-survey, troubleshooting-flow, corrective-actions, floor-plan]

- id: f09
  title: 排障案例三级分类体系（AP 侧/客户端侧/性能侧 × 15 案例）
  type: framework
  source_chapter: "p126-160"
  source_quote: |
    "AP TROUBLESHOOTING - CASE 1: AP can't be powered up. CASE 2: AP fails to get an IP address from the DHCP server. CASE 3: Cannot ping or access the AP using web GUI, SSH or console. CASE 4: AP can't join a cluster. CLIENT TROUBLESHOOTING - CASE 5: 802.1X authentication not working. CASE 6: Captive Portal redirection not working. CASE 7: Client can't get an IP. CASE 8: Client is unable to connect to AP/Cluster. PERFORMANCE TROUBLESHOOTING - CASE 10: signal strength, PHY errors. CASE 11: Low throughput/latency. CASE 13: AP not supplied with PoE."
  summary: |
    教材排障章把 15 个案例按故障对象分三域：AP 侧（无法上电、拿不到 IP、ping 不通/Web 打不开、入不了集群）、客户端侧（802.1X 认证失败、Portal 不弹页、拿不到 IP、连不上 AP/集群、Portal 认证失败）、性能侧（连接帧/信号强度/PHY 错误查看、低吞吐高时延、端口错误、PoE 不供电、会话跟踪、管理帧抓取）。每案固定"现象→分步检查→命令验证"结构，命令集中在 console（tcpdump、ifconfig、ps、top、athstats）。接单时先归域再套对应案例。

  tags: [troubleshooting, case-taxonomy, ap-client-performance]

- id: f10
  title: 集群维护与远程管理操作框架
  type: framework
  source_chapter: "p85-88"
  source_quote: |
    "MAINTENANCE: Individual Maintenance Actions, Cluster Maintenance Actions, Primary Details, Primary IP Details. REMOTE CLUSTER MANAGEMENT: New management architecture, AP Group can be managed remotely (opening the Firewall settings for AP Group Management IP), All operations supported (except AP Group image upgrade), PVM, SVM, get/set."
  summary: |
    集群维护操作分两层：单机维护动作（Individual Maintenance Actions，针对某一台 AP）与集群维护动作（Cluster Maintenance Actions，作用于整组），界面上区分主节点详情（Primary Details）与主节点 IP 详情（Primary IP Details），即日常操作都应面向 PVM 做。远程集群管理架构允许运维不进现场、通过 Group Management IP 远程管理整个 AP Group（get/set 模式），前提是在防火墙上为组管理 IP 放行；除 AP Group 镜像升级外的所有操作都支持远程执行。新 AP 加入集群（Join a cluster）也在此模块完成。

  tags: [cluster-maintenance, remote-management, pvm, firewall]
