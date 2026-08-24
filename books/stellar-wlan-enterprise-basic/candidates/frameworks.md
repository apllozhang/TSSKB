# 框架/流程 · OmniAccess Stellar WLAN Enterprise Basic (DT00XTE368EN)

> 来源：source/fulltext.md（页码即教材 PDF 页码）

- id: f01
  title: 勘测四阶段任务地图（PLAN→VALIDATE→MONITOR→TROUBLESHOOT）
  type: framework
  source_chapter: "p85"
  source_quote: |
    "SITE SURVEY TASKS: PLAN > VALIDATE > MONITOR > TROUBLESHOOT. PLAN: PREPARATION & REQUIREMENTS, PREDICTIVE SITE SURVEY. VALIDATE: PRE-DEPLOYMENT SITE SURVEY, INSTALLATION AND CONFIGURATION, POST-DEPLOYMENT SITE SURVEY. MONITOR/TROUBLESHOOT: SPECTRUM ANALYSIS, PACKET ANALYSIS, PERIODIC CHECK-UPS, CONTINUOUS MONITORING."
  summary: |
    教材无线勘测方法论的总骨架：规划（PLAN）阶段先做需求准备与预测性勘测；验证（VALIDATE）阶段依次完成预部署勘测、安装配置、后部署勘测；监控与排障（MONITOR/TROUBLESHOOT）阶段用频谱分析、抓包分析、定期巡检和持续监控闭环。任何 WLAN 交付项目都可以把工作项映射到这四个阶段，避免"装完就走"式的漏项。教材在 p107、p124 两次复用这张地图，说明它是贯穿勘测章节的主线框架。

  tags: [site-survey, methodology, lifecycle, wlan]

- id: f02
  title: Ekahau 预测勘测七步法（加图→画墙→导入→圈区→自动规划→复核→出报告）
  type: framework
  source_chapter: "p110-121"
  source_quote: |
    "Predictive Survey / Virtual Survey: Uses variables: Building materials, Square footage, Number of wireless users, Applications, Access point models... Launch the planner: Access point selection and Tx power, Antenna height, Channel and bandwidth settings, Dual 5Ghz toggle, Minimum data rate, Band steering, Number of SSIDs, Max associated clients, RTS / CTS toggle."
  summary: |
    无线网络未部署前的仿真设计流程：（1）把楼层图导入 Ekahau（支持 BMP/JPG/PNG/PDF/DWG 等格式）；（2）用 Wall Outlining Wizard（WOW）标定比例尺并逐类画出内墙/窗/门，每类材质赋固定衰减值（见 p14 参数条目）；（3）导入地图与设置；（4）用 Area 工具圈出覆盖区域，设定终端类型与数量；（5）运行 Auto-Planner 自动摆 AP，可调 AP 型号与发射功率、天线高度、信道带宽、双 5GHz、最低速率、频段引导、SSID 数、最大关联终端数、RTS/CTS；（6）复核覆盖与 AP 位置，调参重跑；（7）输出报告（AP 配置表、位置图、覆盖性能可视化）。产出直接用于后续 WLAN 部署配置。

  tags: [ekahau, predictive-survey, rf-design, workflow]

- id: f03
  title: 预部署 Stop-and-Go 勘测法（AP-on-a-Stick 逐点冻结）
  type: framework
  source_chapter: "p126"
  source_quote: |
    "1.From the Survey tab in Ekahau select Stop-and-Go Survey. 2.Turn on the access point. 3.Perform survey by walking the area and clicking to collect data. 4.Stop surveying, Freeze the AP and move it to the next area. 5.Repeat steps 3-4 until all the necessary AP locations have been surveyed."
  summary: |
    网络尚未安装时的现场实测法（俗称"杆上 AP"）：把一台 AP 装在三脚架/小车上通电，在 Ekahau 里选 Stop-and-Go 模式，围绕该 AP 位置走动并点击采样；一个点位测完就 Freeze（冻结）该 AP 数据，把设备搬到下一个候选位置重复，直到把设计要求的全部 AP 位置测完。可主动或被动模式，目标是拿到 SNR、RSSI、干扰与理想 AP 布放位置。要点是"冻结后搬站"，多点位数据最终拼成整层热图。

  tags: [pre-deployment, stop-and-go, ekahau, ap-on-a-stick]

- id: f04
  title: 后部署主动勘测法（ePerf 吞吐服务器 + 连续走测）
  type: framework
  source_chapter: "p127-128"
  source_quote: |
    "1.Install an ePerf server in your network. 2.Set your connected device interface. 3.Set the IP address of the ePerf server for throughput testing... 1.From the survey tab in Ekahau select Continuous Survey. 2.Perform survey by walking the area at a consistent pace to collect data. 3.Analyze the data and add notes. Obstructions areas not covered, antenna orientation. 4.Generate reports."
  summary: |
    网络已上线后的验证与基线化流程：先在网内装 ePerf 吞吐测试服务器，把勘测终端的接口与服务器 IP 配好；然后在 Ekahau 选 Continuous Survey，以稳定步速走遍目标区域采集数据（认证、关联、丢包、RTT、吞吐）；走完后分析数据并加注障碍物、覆盖空洞、天线朝向等问题点；最后用 Ekahau 出报告。与预部署的"停走采样"相反，这里强调匀速连续走测，用于验证部署效果并留下性能基线。

  tags: [post-deployment, active-survey, throughput, baseline]

- id: f05
  title: 现场排障三步法（平面图定位→勘测观察→纠正措施）
  type: framework
  source_chapter: "p462-465"
  source_quote: |
    "Step 1 – Get the floor plans: Identify potential issues: obstacles, walls, ceiling height... Identify areas where WiFi is required... Locate Access Point. Step 2 – Site Survey observation: Identify AP model: same as original design? RF overlap: Co/Adjacent channel interference? Areas with no radio coverage... transmission power: Default or customized? Step 3 – Corrective actions: Change AP model; Rework RF wireless design; Rework channel width; Remove lower data rates; Improve AP placement."
  summary: |
    "WiFi 网络表现差"类投诉的现场处置框架。第一步拿平面图，圈出高/中优先级区域、障碍物与既有 AP 位置，先定义问题范围（Where/When/Who/How）；第二步实测观察五项——AP 型号是否与设计一致、AP 间是否存在同频/邻频干扰、是否有覆盖空洞（AP 宕机或缺失）、发射功率是默认还是定制、布放位置是否别扭；第三步从五类纠正措施中选：换 AP 型号（更好天线/室外型）、重做 RF 设计（调功率/换信道）、收窄信道带宽压干扰、删掉低速率逼迫终端粘优质 AP、改善布放。教材同时给出改功率/加 AP/挪 AP 三个典型用例。

  tags: [troubleshooting, on-site, corrective-action, rf]

- id: f06
  title: Stellar 三种管理模式选型（Express / Enterprise / Cloud）
  type: framework
  source_chapter: "p145"
  source_quote: |
    "Wi-Fi Express: Standalone mode. Wi-Fi Enterprise: In Premise, Managed mode with OmniVista 2500 NMS. Wi-Fi Cloud: Cloud based, Managed mode with OmniVista Cirrus NMS. Move from Express to Enterprise/Cloud when/if needed."
  summary: |
    Stellar AP 有三种管理模式，是所有部署决策的第一步：Express 模式即 AP 自组集群（无网管服务器，PVM 虚拟主管理器，最多 255 台）；Enterprise 模式由本地 OmniVista 2500 统一管理（最多 4000 台，含 UPAM 认证/策略）；Cloud 模式由 OmniVista Cirrus 云管。教材强调可以从 Express 平滑迁到 Enterprise/Cloud（需要 DHCP option 138 指向网管 + 模式切换或恢复出厂，见反例条目）。本课程主线即 Enterprise 模式。

  tags: [mode-selection, express, enterprise, cloud, ov2500]

- id: f07
  title: Enterprise 模式 AP 上线四步流程（上电→DHCP 138→注册→下发配置）
  type: framework
  source_chapter: "p242"
  source_quote: |
    "1. AP is connected to the network and powered on. AP sends a DHCP request. AP selects the Management VLAN through LLDP. 2. AP determines IP of OV2500 if option 138 is returned by DHCP server. AP is set in Enterprise mode. 3. AP contacts OV2500 for registration. 4. OV2500 assigns an AP Group to the AP. OV2500 applies the configuration to the AP."
  summary: |
    Enterprise 模式下 AP 从上电到受管的完整链路：（1）AP 接入 PoE 端口上电，发 DHCP 请求，通过 LLDP 选定管理 VLAN；（2）DHCP 服务器在管理 VLAN 作用域里返回 option 138（OV2500 的 IP），AP 据此切入 Enterprise 模式；（3）AP 主动联系 OV2500 的 AP Registration 组件发起注册；（4）注册成功后 OV2500 把 AP 分配进 AP Group 并向其下发配置（SSID、射频等）。排障时按这四步倒查：PoE/线缆→option 138→注册状态→AP Group。

  tags: [ap-onboarding, dhcp-option-138, registration, enterprise]

- id: f08
  title: AP 受管三条件判定（Trusted + Licensed + 国家码匹配）
  type: framework
  source_chapter: "p243"
  source_quote: |
    "AP is managed when Registration succeeds: AP is Trusted (Manually or automatically); AP is Licensed: Enough AP Licenses on OV; Country Code matches RF profile CC. AP is unmanaged when Registration fails: AP is not Trusted; AP is not Licensed; Country Code does not match the Country Code from the RF Profile. Configuration not applied & All Radios are off."
  summary: |
    AP 能否进入"受管"状态的判定逻辑，三个条件全过才算注册成功：被信任（手动点 Trust 按钮或预先导入 MAC 白名单）、有足够 AP 许可（License 数量要覆盖总 AP 数）、AP 国家码与 OV2500 RF Profile 的国家码一致。任一不满足即注册失败、落入 Unmanaged，且配置不下发、所有射频关闭。这是排障"AP 在列表里但射频不工作"的第一张检查表。

  tags: [registration, trust, license, country-code]

- id: f09
  title: SSID 创建向导三步法（命名/选 Usage→定制→AP Group 分配与排程）
  type: framework
  source_chapter: "p283-289"
  source_quote: |
    "Step 1 Create SSID: Name the SSID Service (unique name to identify a wireless service); Name the SSID (unique SSID name broadcasted in the air); Select the SSID Usage. Step 2 Customize SSID: Minimal configuration contains: Basic Parameters, Allowed Band: 2.4GHz, 5GHz, 6GHz; Security Settings; Default VLAN/Network; ACL/QoS rules; Authentication Strategy. Step 3 AP Group Assignment & Schedule: Schedule the SSID broadcast... Apply the SSID to one or multiple AP Group(s)."
  summary: |
    OV2500 推荐的 SSID 创建路径（区别于专家模式的手工拼装）：第一步起服务名（可多个服务共用同一 SSID 名）并选 Usage 模板（Guest/Employee/BYOD/PSK 等，模板决定认证与门户组合）；第二步按 Usage 展开定制——允许频段、加密/PSK、默认 VLAN 或 VLAN 池、Access Role Profile（VLAN+QoS+带宽）、认证策略（本地库/外部 RADIUS/LDAP-AD），Guest/BYOD 还可配门户策略；第三步把 SSID 绑到若干 AP Group 并设置广播时间表（默认 Always Available）。向导模式覆盖绝大多数场景，专家模式留给特殊 SSID。

  tags: [ssid-wizard, ov2500, workflow, usage-template]

- id: f10
  title: WLAN Service（专家模式）七步部署法
  type: framework
  source_chapter: "p321"
  source_quote: |
    "The deployment of an SSID consists in several steps: Creation of a WLAN Service profile (SSID); Creation of an AAA Server Profile (if do not exist); Creation of an Access Role Profile (if do not exist); Creation of an Access Policy (if do not exist); Definition of an Authentication Strategy (if do not exist); Create a Radius local employee account (if do not exist); Deployment of the profiles (templates) to AP-Group(s)."
  summary: |
    专家模式下手工部署一个 SSID 的标准次序：先建 WLAN Service（SSID 本体：ESSID、隐藏、频段、安全级别、加密、AAA Profile、默认 Access Role Profile），再建 AAA Server Profile（802.1X/门户/MAC 认证与计账服务器，可用内置 UPAMRadiusServer），建 Access Role Profile（用户拿到 VLAN/QoS/带宽属性）并 Apply to Devices 映射到 VLAN，建 Authentication Strategy（认证源+登录方式），建 Access Policy（把策略按 SSID 属性映射到用户组），创建本地员工账号，最后把整套模板下发到 AP Group。理解这条链就理解了 OV2500 SSID 的对象模型。

  tags: [wlan-service, expert-mode, aaa, access-role, ov2500]

- id: f11
  title: UPAM Guest SSID 工作流（Guest Usage→门户重定向→Guest 策略→VLAN）
  type: framework
  source_chapter: "p343"
  source_quote: |
    "How it works: Create a Guest SSID with the usage Guest Network; Activate the Captive portal option; Select the RADIUS server in the Authentication Strategy; Create a Guest account if the UPAM internal RADIUS server is used; In the Guest Access Strategy, define the login method (username and password) and Post Portal enforcement to restrict Guest traffic; Assign a VLAN to the Guest SSID."
  summary: |
    访客网络的完整工作流：用 Guest Network 模板建 SSID 并勾选强制门户；认证策略选 RADIUS 服务器（内置即 UPAMRadiusServer）；用内置服务器时在本地库建 Guest 账号（可配数据配额）；在 Guest Access Strategy 里定登录方式（账密/接入码/条款）、自助注册与员工赞助审批，并用 Post Portal Enforcement 给通过门户的访客换更严格的角色；最后给 SSID 绑 Guest VLAN。配套能力：Kickoff 踢下线、黑名单、门户页定制（UPAM > SETTINGS > Captive Portal）。

  tags: [upam, guest-access, captive-portal, workflow]

- id: f12
  title: 带宽控制四级优先级判定链（DPI→ACL→Access Role→SSID）
  type: framework
  source_chapter: "p364"
  source_quote: |
    "Matches a DPI application in the Policy List? Y: Application Specific BW Enforcement as per DPI Rule. N: Matches an ACL in the Policy List? Y: ACL Specific BW Enforcement as per Policy List. N: Access Role set with BW Control? Y: User BW Enforcement as per Access Role Profile. N: SSID set with BW Control? Y: Shared BW Enforced as per WLAN Service/SSID. N: No BW Limitation."
  summary: |
    用户流量被哪一层限速的判定顺序，从细到粗四级：先看是否命中 Policy List 里的 DPI 应用规则（按应用限速）→ 再看是否命中 ACL 规则（按 ACL 动作限速）→ 再看用户所属 Access Role Profile 是否设了带宽（按用户限速，不共享）→ 最后看 SSID/WLAN Service 是否设了带宽合同（该射频上所有用户共享）→ 都没有则不限速。设计限速策略时按这条链反推放哪一层：精确到应用放 DPI，精确到用户放 Access Role，兜底放 SSID。

  tags: [bandwidth-control, precedence, qos, policy-list]

- id: f13
  title: L2/L3 漫游三条件判定（上下文存在→服务存在→VLAN 匹配）
  type: framework
  source_chapter: "p412"
  source_quote: |
    "Client Context exists on the new AP? No: No Roaming, new client. Yes: WLAN service and Access Role Profile exist in the Client Context on the new AP? No: No Roaming, new client. Yes: Client Context VLAN ID = VLAN ID mapped to the Access Role Profile on the new AP? Yes: L2 Roaming; No: L3 Roaming."
  summary: |
    终端从 home AP 漫游到 foreign AP 时的处理判定：新 AP 上没有该终端的 Client Context（或上下文里缺少对应 WLAN Service/Access Role Profile），就不算漫游，按全新客户端重新接入；上下文齐全且其中的 VLAN ID 与新 AP 上映射给该 Access Role Profile 的 VLAN 一致，走 L2 漫游（默认，总是开启）；VLAN 不一致则走 L3 漫游（基于 home/foreign AP 之间的 L2 GRE 隧道，默认关闭需在 Advanced WLAN Service 里开）。判定依据全部来自 Client Context 内容，因此上下文共享（Add/Del 消息）是漫游的前提。

  tags: [roaming, l2-l3, client-context, gre]

- id: f14
  title: 漫游设计四查法（模式→覆盖→邻居→粘性终端）
  type: framework
  source_chapter: "p421-425"
  source_quote: |
    "Identify the roaming mode: Based on the VLAN ID between the home and foreign AP, select Layer 2 Roaming (default) or Layer 3 Roaming. Check the security level of the SSID... Check the radio coverage: Use the Heat Map application... In some cases, Stellar APs are geographical neighbors but can't see each other... On both AP, add statically the neighbor Stellar AP. The roaming decision is made by the client device. Use the Roaming RSSI Threshold in the RF profile."
  summary: |
    规划/排障漫游时的四步检查：一查漫游模式——按 home/foreign AP 的 VLAN 选 L2 或 L3，并按 SSID 安全级别确认快速漫游可用性（OKC 仅 WPA2/WPA3 Enterprise；802.11r 需 WPA2/WPA3 加密）；二查射频覆盖——用 Heat Map 按 2.4/5/6 GHz 分别确认 AP 间有信号重叠，无重叠则无漫游；三查 AP 邻居——空间相邻但电波被直角走廊等遮挡互不可见时，在两台 AP 上互配静态 Neighbor AP；四查粘性终端——漫游决定权在终端，用 RF Profile 里的 Roaming RSSI Threshold 配合 802.11k/802.11v 引导切换。

  tags: [roaming-design, coverage, neighbor-ap, sticky-client]

- id: f15
  title: RAP 五步部署流程（OV2500+Cirrus Freemium 方案）
  type: framework
  source_chapter: "p439"
  source_quote: |
    "1 – Stellar Access Point Startup & Registration. [PRE] – Settings to be Entered by the Administrator. 2 - VPN & OmniVista 2500 Settings Retrieval. 3 - VPN Tunnel (Management Traffic) Establishment. 4 – Configuration Settings Retrieval. 5 – VPN Tunnel (Clients Traffic) & Client Connection."
  summary: |
    远程 AP（RAP）把公司 SSID 延伸到分支/家庭的上线流程（Freemium 方案，Premium 少一步 OV2500 环节）：管理员先在 Cirrus 4 预录 AP 的序列号/MAC、VPN 服务器公网 IP、VPN 客户端地址池、OV2500 地址（[PRE] 步）；（1）AP 上电自动连 Cirrus 4，按 MAC 被识别；（2）Cirrus 下发模式=RAP、客户端 VPN IP、VPN 服务器公网 IP、OV2500 IP；（3）AP 与总部 ALE VPN Server 建管理 VPN 隧道；（4）AP 经隧道从 OV2500 拉取配置（SSID、射频等）；（5）再建第二条客户端数据 VPN（L2GRE），远程用户连企业 SSID，流量过隧道回公司。配套配置次序见 f 案例条目 c10。

  tags: [rap, vpn, cirrus, commissioning, remote-office]

- id: f16
  title: OmniSwitch UNP 自动配置流程（LLDP 分类→分 VLAN→上报位置）
  type: framework
  source_chapter: "p236-237"
  source_quote: |
    "Configure Access ports as UNP port-type bridge. Disable the trust-tag (security reasons). Create an UNP classification rule to classify the AP in a role based on the AP LLDP traffic. Map a VLAN ID to the role received by the AP... 1. AP sends LLDP. 2. AP classified in defaultWLANProfile -> VLAN 125 assigned. 3. AP sends untagged DHCP, get IP on vlan 125. 4. Switch sends LLDP with Port LAN ID and AP Location."
  summary: |
    边缘交换机免预配置接入 AP 的自动化方案：把接入口配成 UNP port-type bridge（同口可插 AP/话机/摄像头/PC），关闭 trust-tag（安全上不接受任意 tagged 流量），建基于 LLDP 的分类规则把 AP 归入角色，角色映射管理 VLAN。运行时序：AP 发 LLDP→交换机按 defaultWLANProfile 分配管理 VLAN→AP 发无标签 DHCP 拿到该 VLAN 地址→交换机回发带 Port VLAN ID 和 AP Location（机架:端口）的 LLDP→AP 更新管理 VLAN 与位置信息，OV2500 拓扑即得精确落点。好处是无需提前知道 AP 接哪个口、无需手工配 trunk。

  tags: [unp, lldp, zero-touch, omniswitch, ap-location]
