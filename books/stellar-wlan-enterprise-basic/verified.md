# 验证通过条目 · stellar-wlan-enterprise-basic

> 三重验证（V1 原文真实性 / V2 可操作价值 / V3 独特性）已完成；glossary 按规则免验保留。

> 汇总：候选 126 条（frameworks 16 / principles 39 / cases 10 / counter-examples 16 / glossary 45），通过 119 条，淘汰 7 条（全部为 principles 的公开标准参数表，V3 淘汰）。

# frameworks（16 条）

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


# principles（32 条）

- id: p05
  title: MU-MIMO 与 OFDMA 的适用场景分工
  type: principle
  source_chapter: "p33"
  source_quote: |
    "MU-MIMO: Improve the capacity; Increase the rate of each user; Most suitable for high bandwidth applications; Most suitable for large-packet transmission. OFDMA: Improved the efficiency; Reduced latency; Most suitable for low bandwidth applications; Most suitable for small packet transmissions."
  summary: |
    WiFi 6 两大并行技术的选型原则：MU-MIMO 靠波束赋形在空间上分流，提升总容量和单用户速率，适合高带宽、大包业务（如视频下载）；OFDMA 把信道切成多个资源单元（RU）给多终端同时收发，提升效率和时延，适合低带宽、小包业务（如 IoT、语音、信令）。实际网络两者叠加使用，理解分工才能解释"为什么换了 WiFi 6 语音时延和 IoT 密集场景改善明显"。

  tags: [mu-mimo, ofdma, use-case, wifi6]

- id: p07
  title: 6 GHz 室外功率规则（AFC 与 LPI/VLP 等级）
  type: principle
  source_chapter: "p44"
  source_quote: |
    "Standard-Power AP (AFC Controlled): 36 dBm... Low-Power AP (indoor only): 30 dBm... Client Connected to Low-Power AP: 24 dBm. LPI: 23 dBm, 10 dBm/MHz. VLP: 14 dBm, 1 dBm/MHz... EU and RW prohibit using 6GHz band Outdoors for Standard Power APs. FCC approved 7 AFC providers."
  summary: |
    6 GHz 室外/室内功率分级（监管红线）：FCC 域标准功率 AP 及其固定客户端需经 AFC（自动频率协调）控制，EIRP 上限 36 dBm，标准功率 AP 下客户端 30 dBm；低功率室内 AP（LPI，必须有有线供电、内置天线、非电池）30 dBm、其客户端 24 dBm；EU 域 LPI 为 23 dBm/10 dBm/MHz，VLP（便携设备，室内外均可但禁道路车辆与无人机）14 dBm/1 dBm/MHz。EU 及多数地区禁止标准功率 AP 在 6 GHz 室外使用；FCC 批准了 7 家 AFC 服务商（Qualcomm、Federated Wireless 等）。部署 6E 室外链路前必须先核对本地区适用等级。

  tags: [6ghz, afc, eirp, lpi, vlp, regulation]

- id: p09
  title: 天线三大类型与选型原则
  type: principle
  source_chapter: "p49-53"
  source_quote: |
    "OMNIDIRECTIONAL: RF Signal > Equal in all directions; Point to Multipoint; Short Distance. Example: Dipole. SEMI-DIRECTIONAL: RF Signal > Specific Direction; Point-to-Point Communication; Short to Medium Distance. Examples: Patch/Panel, Yagi. HIGHLY-DIRECTIONAL: RF Signal > Very Specific Direction; Long Distance. Example: Grid."
  summary: |
    按辐射图选天线的速查规则：全向天线（偶极子，AP 内置默认）各方向能量均等，适合点对多点、短距离覆盖；半定向天线（Patch/Panel 板状、Yagi 八木）能量集中一个方向，适合点对点中短距无线桥接；高定向天线（Grid 栅格）方向性极强，适合长距离点对点链路。Stellar AP 默认内置全向天线，型号尾号为"2"（如 AP1322/AP1362）才支持外接天线；换外接天线可控制能量分布/覆盖形状，但必须复核不超过所在国法定功率限值（p138）。

  tags: [antenna, radiation-pattern, selection, omnidirectional, directional]

- id: p11
  title: WPA3 的 SAE 与 CNSA 规则
  type: principle
  source_chapter: "p295"
  source_quote: |
    "WPA/WPA2-Personal PSK replaced by WPA3-Personal SAE (Simultaneous Authentication of Equals): Stronger Encryption Key (128 bits), Offline dictionary attack resistance, No additional complexity to connect. Optional 192-bit security mode (CNSA option): CNSA enabled: Only wpa3 client authorized on the SSID; CNSA disabled: wpa2 or wpa3 clients authorized. CNSA option not enabled on AP1101 only."
  summary: |
    WPA3 落地细节：Personal 场景 PSK 被 SAE 取代——密钥加强到 128 位、可抗离线字典攻击、用户连接操作复杂度不增加；Enterprise 场景可选 192 位 CNSA 模式，开启后 SSID 只允许 WPA3 客户端（混合终端网络要慎开），关闭则 WPA2/WPA3 客户端都能接入；AP1101 是唯一不支持 CNSA 选项的型号。所有 Stellar AP 软件升级后均支持 WPA3。

  tags: [wpa3, sae, cnsa, 192-bit, compatibility]

- id: p12
  title: 认证方式信任等级与取舍
  type: principle
  source_chapter: "p294"
  source_quote: |
    "Open + Captive Portal: Cons: No Security; Pros: any type of device can be authenticated. MAC authentication: Cons: MAC can be spoofed, no traffic encryption; Pros: Available for basic wireless devices (printers, scanners). PSK: Pros: Easy set up; Cons: all keys can be hacked or stolen (key shared by all users). 802.1X: Pros: Strongest security, ease of Management, scalability; Cons: More configuration during initial setup."
  summary: |
    SSID 认证方式的选型权衡表（信任等级从低到高）：Open+门户——无加密但任何设备都能过门户认证；MAC 认证——可被仿冒且不加密流量，只适合打印机/扫描仪等哑终端；PSK——部署简单但全网共享密钥易泄露；802.1X——安全性最强、管理扩展性好，代价是初期要搭 RADIUS/UPAM 与用户库。企业员工网用 802.1X，访客网用门户+后置策略，哑终端用 MAC，是教材隐含的推荐组合。

  tags: [authentication, 802.1x, psk, mac-auth, captive-portal]

- id: p13
  title: Ekahau 材质衰减常数表（墙/窗/门 dB 值）
  type: principle
  source_chapter: "p113-115"
  source_quote: |
    "Wall, Brick (10dB); Wall, Cinder Block (5dB); Wall, Concrete (12dB); Wall, Dry (3dB); Wall, Dry Hollow (2dB). Window, Interior (1dB); Window, Thick (3dB). Solid Wood Door 6 dB; Hollow Wood Door 4 dB; Office Door w/Window 4 dB; Steel Fire/Exit Door 13 dB / 19 dB; Steel Rollup Door 11 dB. The survey tool makes its measurements with the doors closed."
  summary: |
    预测勘测画图时给障碍物赋的衰减值：内墙——砖 10 dB、砌块 5 dB、混凝土 12 dB、石膏板 3 dB、空心石膏 2 dB；窗——室内窗 1 dB、厚窗 3 dB；门——实木 6 dB、空心木 4 dB、带窗办公室门 4 dB、钢质防火/疏散门 13/19 dB、卷帘门 11 dB。注意勘测工具按"门全关"的保守口径计算。配合 p136 的现场经验（金属吸波、电梯井屏蔽、镀膜玻璃含金属）一起用于覆盖估算。

  tags: [attenuation, materials, ekahau, predictive-survey]

- id: p14
  title: 已知 WiFi 干扰源清单
  type: principle
  source_chapter: "p137"
  source_quote: |
    "Microwave ovens; 2.4GHz cordless phones, DSSS and FHSS; Fluorescent bulbs; 2.4GHz video cameras; Elevator motors; Cauterizing devices; Plasma cutters; Bluetooth radios; Nearby 802.11, 802.11b or 802.11g WLANs; WISPs; Bookcases; File Cabinets; Pallet Racks; 5GHz cordless phones; Radar; Perimeter sensors; Digital satellite; Outdoor wireless 5GHz bridges."
  summary: |
    现场排查干扰时的对照清单：2.4 GHz 段——微波炉、无绳电话（DSSS/FHSS）、荧光灯、2.4G 摄像头、蓝牙、邻近 b/g 网；5 GHz 段——5G 无绳电话、雷达、周界传感器、数字卫星、户外 5G 桥接；通用——电梯电机、电灼/等离子切割设备；还有书架、文件柜、货架这类物理遮挡"干扰源"。频谱分析（Spectrum Survey）中识别出的占空比异常设备大多能在这张表里对号入座。

  tags: [interference, spectrum, 2.4ghz, 5ghz, checklist]

- id: p15
  title: AP 布放与环境施工原则
  type: principle
  source_chapter: "p138-139"
  source_quote: |
    "Start with antennas pointing straight up or down. Use semi-directional antenna for coverage as opposed to an omni-directional antenna for long corridors... Rain, snow, and wind can interfere... Place access points equal distant from the walls... Place Access points above all sources of obstruction... Try not to place the AP near sources of heat or under the sun."
  summary: |
    安装施工守则：射频侧——天线初始朝向垂直（正上/正下）；长走廊用半定向天线做覆盖而非全向；每次更换天线后复核不超国别法定功率；雨雪风、人群（人体吸波）、树木都会衰减信号。布放侧——AP 与四周墙面等距、尽量放房间/覆盖区中央；必须高于所有障碍物（比如办公位隔断上方、贴近天花板），即使这一点压过"居中"原则；远离热源与暴晒。配合 p136：金属吸 WiFi 信号，电梯井几乎全屏蔽（覆盖井道要在井顶/井底或轿厢内放 AP），镀膜玻璃和窗膜含金属要预期掉信号。

  tags: [ap-placement, installation, environment, best-practice]

- id: p16
  title: Enterprise 模式最低部署要求清单
  type: principle
  source_chapter: "p226-227"
  source_quote: |
    "Hardware requirement: Access Point, PoE Switch, DHCP Server, OmniVista 2500. Minimal configuration required: Stellar Access Point: Purged AP with default factory configuration. OmniSwitch: PoE, Management VLAN, 'ip dhcp-relay' for external DHCP server. DHCP server: Option 138 on Management VLAN, Address Plan for Service VLAN. OmniVista 2500 server: IP configuration, Licenses."
  summary: |
    Enterprise 模式开局的四件套与最小配置：硬件——AP、PoE 交换机、DHCP 服务器、OV2500；AP 侧要求出厂默认的净化状态；交换机侧要开 PoE、划管理 VLAN、DHCP 在外部时配 ip dhcp-relay；DHCP 侧管理 VLAN 作用域必须带 option 138（指向 OV2500），并为业务 VLAN 规划地址池；OV2500 侧完成 IP 配置与许可导入。这份清单同时是 p164 拓扑图（trunk 口 native VLAN=管理 VLAN、tagged VLAN=SSID VLAN）的文字版。

  tags: [enterprise, requirements, minimal-config, poe, dhcp]

- id: p17
  title: OV2500 许可证体系与扩容规则
  type: principle
  source_chapter: "p229-230"
  source_quote: |
    "OmniVista Core License - required (Network devices). OmniVista VMM License - optional. OmniVista AP License count: Stellar Access Point: Per AP License model. OmniVista Guest Management License count: Per device license model. OmniVista BYOD License count: Per device license model. OmniVista High Availability (HA) License: One License per set of OmniVista servers. OmniVista Web Content Filtering License: One license for 10 Access Point."
  summary: |
    许可模型速记：Core 许可必需（管网络设备）；VMM 可选；AP 许可按 AP 台数（Stellar 每 AP 一枚）；Guest 与 BYOD 许可都按"设备数"而非账号数计；HA 许可每对 OV 服务器一枚；WCF 许可按 1:10 AP 比例。扩容规则：AP 许可数要大于待部署 AP 总数；不足时先导入增量许可再上 AP（如 100+50=150）。评估许可（EVAL）全功能但只有 90 天有效期，一个文件含全部设备与服务许可。

  tags: [license, ov2500, capacity, guest, byod, wcf]

- id: p18
  title: Express 集群规模与 PVM 选举规则
  type: principle
  source_chapter: "p149-152"
  source_quote: |
    "In an AP group, one AP supports the role of centralized management. It is called PVM (Primary Virtual Manager)... Another AP is responsible for rescuing the PVM. It is called SVM... Highest Model Type, Highest MAC address -> PVM; AP with the second highest MAC is designated as the SVM... Cluster Max. Size: 255. Recommendations: Max Up to 32 APs per OmniSwitch, Max Up to 64 APs per stack."
  summary: |
    Express 模式的集群规则：同 Group ID 的 AP 里选一台当 PVM（主虚拟管理器）集中管理，选举依据是最高型号、再最高 MAC；第二高 MAC 的当 SVM（备机）负责接管；其余都是 Member，集群上限 255 台。可靠性设计上，集群超过 64 台时建议每台 OmniSwitch 最多挂 32 台 AP、每堆叠最多 64 台，避免单点故障域过大。Enterprise 模式对应的上限是 4000 AP（p154-155）。

  tags: [express, pvm, svm, cluster-sizing, election]

- id: p19
  title: Stellar 三平面流量规则（管理不打标/数据打标/无隧道）
  type: principle
  source_chapter: "p159-163"
  source_quote: |
    "Management Plane: AP management traffic is always untagged. Control Plane: AP to AP protocol over the air and over the LAN; Used for RF Management, Neighbor AP discovery, Roaming client context sharing. Data Plane: Wireless data converted to Ethernet in the AP and sent to the AP uplink. Wireless traffic always tagged on the AP uplink. No tunnel mode to OV or Virtual Controller. Data Plane is only L2... Routing provided by LAN infrastructure."
  summary: |
    无控制器架构的三平面行为约定，排障抓包必背：管理平面——配置/监控流量永远不打标签（走 native/管理 VLAN），Express 集中在 PVM、Enterprise 集中在 OV2500；控制平面——AP 间协议走空口和 LAN 两路，承担射频管理、邻居发现、漫游上下文共享，属 AP 内部流量；数据平面——无线帧在 AP 本地转成以太网上行，业务流量在 AP 上联口永远打标签，到 OV/虚拟控制器没有隧道，数据面只做二层，路由由 LAN 基础设施承担。解释"为什么 AP 口要配 trunk 且 native VLAN=管理 VLAN"就靠这条。

  tags: [planes, untagged, tagged, no-tunnel, controller-less]

- id: p20
  title: DHCP Option 138 配置规则（指向 OV2500）
  type: principle
  source_chapter: "p156/172"
  source_quote: |
    "WiFi Express is the default mode. DHCP option 138 equals the IP address of the OmniVista 2500 Server. # Classify OmniAccess Stellar AP as STELLAR: class STELLAR { match if substring (option vendor-class-identifier, 0, 4) = 'HAP.'; } option ovwma code 138 = ip-address; option ovwma 192.168.0.61;"
  summary: |
    Enterprise 模式触发开关：AP 默认 Express 模式，只有当 DHCP 服务器在管理 VLAN 作用域里返回 option 138 且值为 OV2500 的 IP 时，AP 才切换为 Enterprise。isc-dhcp-server 写法：Stellar AP 的 vendor-class 以"HAP."开头可据此分类，138 非标准选项需先定义 `option ovwma code 138 = ip-address;` 再在池内下发；OmniSwitch 做 DHCP 服务器时直接 `option 138 x.x.x.x`。Windows Server 配置路径见 c04 案例附录（p278）。

  tags: [dhcp, option-138, enterprise-mode, isc-dhcp]

- id: p21
  title: AP Group 容量与配置模型
  type: principle
  source_chapter: "p161/271"
  source_quote: |
    "AP Group: Multiple APs in the same AP Group, sharing the same configuration. Mix of any AP type & total number of AP limited to 4000 (Enterprise) or 255 (Express). When an AP initially registers with OmniVista, the AP is placed into a pre-configured 'Default' AP Group. Any configuration applied to an AP Group is applied to all APs in the group."
  summary: |
    OV2500 不直接管理单台 AP，一切配置以 AP Group 为单位：同组成员共享配置（管理 VLAN、RF Profile、Data VPN 等），组内可混插任意 AP 型号，Enterprise 全局上限 4000 台（可分散在多个组），Express 255 台，组数无限制。新注册 AP 自动落入 Default 组，需要手工改到目标组。给 AP Group 下发的任何配置都会同步到组内所有 AP——这也是配置回滚/批量变更的最小单位。

  tags: [ap-group, ov2500, scale, configuration-model]

- id: p22
  title: OV2500 高可用（HA）机制要求
  type: principle
  source_chapter: "p232-233"
  source_quote: |
    "High Availability (HA) creates a redundant (Stand-by) OmniVista which will take over if the primary (Main) OmniVista becomes unavailable. With HA, 2 instances of OV are constantly running. Connection across a Layer 2 network; Extension to Layer 3 network, if VxLAN or SPB are used. Network devices must communicate to Virtual IP. Dedicated OmniVista HA license."
  summary: |
    HA 部署要点：主备两台 OV 常驻运行、实时同步服务与数据库；正常要求二层网络互联，若底层有 VxLAN 或 SPB 可扩展到三层；AP/交换机等网络设备一律对"虚拟 IP"通信，主备切换对设备透明；切换时 UPAM（含 BYOD/Guest）与全部监控服务由备机接管；需要专门的 HA 许可（每对服务器一枚）。规划时先确认二层可达或 SPB/VxLAN 基础，再申请许可。

  tags: [ha, virtual-ip, ov2500, spb, vxlan]

- id: p23
  title: SNMP 发现参数基线（v3 + SHA+DES）
  type: principle
  source_chapter: "p256-257"
  source_quote: |
    "OS6870, OS6360, OS2360: user snmpuserv3 read-write all password 'Superuser=1' sha+des; snmp station 10.130.5.5X 162 snmpuserv3 v3 enable. SNMPv3 Profile Parameters: Timeout (msec): 5000; Retry Count: 3; User Name: snmpuserv3; Auth & Priv Protocol: SHA+DES; Auth Password / Priv Password: Superuser=1."
  summary: |
    OV2500 发现 OmniSwitch 用 SNMP（v1/2/3 均支持，推荐 v3）。交换机侧两条命令建读写用户与工作站；OV 侧发现参数基线：超时 5000 ms、重试 3 次、认证与加密协议 SHA+DES、用户名/密码两侧严格一致。发现失败的复核顺序（p262）：交换机 `show snmp station` 核对 IP/用户名、重输密码确认协议组合、OV 侧在 Discovery Profiles 里核对或重建档案后重跑 Discover Now。

  tags: [snmpv3, discovery, parameters, omniswitch]

- id: p24
  title: AP Location 自动生成优先级
  type: principle
  source_chapter: "p238"
  source_quote: |
    "If port alias is configured on the port => AP Location = Port Alias. If system location is configured => AP Location = System Location:PortID. If the system name is configured => AP Location = System Name:PortID. By default => AP Location = Chassis ID:PortID (Chassis MAC address / chassis/slot/port format)."
  summary: |
    OV2500 拓扑里 AP 位置字符串的取值优先级（高到低）：端口别名（interfaces chassis/slot/port alias）> 交换机 system location > 交换机 system name > 默认的机箱 MAC:端口号。想让拓扑图上直接显示"楼层-机房-机架"这类语义位置，就在接入交换机上配 system location 或逐口配 port alias，AP 会通过 LLDP 学到并上报。这也是 f16 UNP 自动配置流程第 4 步的落地细节。

  tags: [ap-location, lldp, topology, port-alias]

- id: p25
  title: SSID Usage 模板矩阵（Usage→安全级别+门户组合）
  type: principle
  source_chapter: "p284"
  source_quote: |
    "Guest Network: Captive Portal, SSID Security Level Open or MAC... Employee BYOD Network: 802.1X or MAC followed by Captive Portal BYOD. Enterprise Network for Employees: 802.1X. Protected Network: PSK. Protected Network for Employees (BYOD): PSK followed by Captive Portal BYOD."
  summary: |
    向导里选 Usage 即选定模板组合：Guest Network=Open/MAC+访客门户；Employee BYOD Network=802.1X 或 MAC 认证后接 BYOD 门户；Enterprise Network for Employees=纯 802.1X（员工企业网标准形态）；Protected Network=纯 PSK；Protected Network for Employees（BYOD）=PSK 后接 BYOD 门户。模板只给默认值，创建后仍可在向导里改。选错 Usage 意味着后面要手工纠正认证与门户组合，选型时对照本表。

  tags: [ssid, usage-template, security-level, captive-portal]

- id: p26
  title: VLAN Pooling 原则（避免单一大广播域）
  type: principle
  source_chapter: "p286"
  source_quote: |
    "VLAN options: Default VLAN: Single VLAN assigned to the SSID. VLAN Pooling: Pool of VLAN assigned to the SSID. Avoid large broadcast domain with a single VLAN."
  summary: |
    SSID 的 VLAN 两种模式：默认单 VLAN；VLAN Pooling 把一组 VLAN（如 20/30/40）绑到同一 SSID，终端哈希分配。设计动机是避免单个 VLAN 形成巨大广播域——高密场景（大会议室、场馆）下一个 /16 员工段的广播/组播开销会拖垮空口，用 VLAN 池切小广播域。Access Role Profile 与 VLAN 的映射关系在池化后依然按角色走。

  tags: [vlan-pooling, broadcast-domain, ssid, design]

- id: p27
  title: WLAN Service 加密类型清单（Enterprise/Personal 各自合法值）
  type: principle
  source_chapter: "p300"
  source_quote: |
    "Enterprise: DYNAMIC_WEP, WPA_TKIP, WPA_EAS, WPA2__TKIP, WPA2_AES, WPA3_AES; 802.1x Bypass is option; AAA Profile is mandatory. Personal: WPA_PSK_TKIP, WPA_PSK_AES, WPA_PSK_AES_TKIP, WPA2_PSK_TKIP, WPA2_PSK_AES, WPA3_SAE_AES, WPA3_PSK_SAE_AES; Passphrase is mandatory; Key Format; AAA Profile is Mandatory."
  summary: |
    专家模式安全设置里可选的加密枚举值：Enterprise 级可选 DYNAMIC_WEP/WPA_TKIP/WPA_EAS/WPA2_TKIP/WPA2_AES/WPA3_AES（含 TKIP 老算法仅作兼容）；Personal 级可选 WPA/WPA2 PSK 系列与 WPA3_SAE_AES、WPA3_PSK_SAE_AES，口令与密钥格式必填。无论哪种级别 AAA Profile 都是必填字段（Personal 也需要，用于门户/MAC 认证路径）。排错时先核对这些枚举值是否与终端能力匹配。

  tags: [encryption, enterprise, personal, aaa-profile, wlan-service]

- id: p28
  title: UPAM 能力边界与许可口径
  type: principle
  source_chapter: "p335-337"
  source_quote: |
    "UPAM consists of Guest Access (Guest License required), BYOD Access (BYOD License required), A built-in RADIUS Server, A built-in MAC Authentication Server. Internal RADIUS server used to authenticate both Guest and BYOD users; UPAM logs can be redirected to an external syslog server; Guest Access License: per device license model (not per account); BYOD Access License: per device license model (not per account)."
  summary: |
    UPAM（统一策略认证管理器）内嵌在 OV2500 里，由四部分组成：Guest Access、BYOD Access、内置 RADIUS 服务器、内置 MAC 认证服务器。认证源可选内部 RADIUS+本地库，或外接 LDAP/AD/RADIUS（还可按 AD 属性做角色映射）；日志可转发外部 syslog。许可口径要点：Guest 与 BYOD 许可都按接入设备数计、与账号数无关——开 1 万个访客账号不额外耗许可，按并发接入设备算。

  tags: [upam, radius, guest, byod, licensing]

- id: p29
  title: 带宽合同三层级（SSID 共享/ARP 按用户/ACL 按规则）
  type: principle
  source_chapter: "p363"
  source_quote: |
    "Bandwidth contract at SSID level: Configured in Advanced WLAN Service Configuration; Bandwidth shared for all user, per radio. Bandwidth contract at Access Role Profile level: Configured in Advanced Access Role Configuration; Bandwidth assigned per user of the profile - Not shared. Bandwidth contract at Role level: A Policy List (ACL/QoS) can restrict the Bandwidth as an action."
  summary: |
    限速的三种落点：SSID/WLAN Service 级——该射频上全体用户共享一个总带宽合同；Access Role Profile 级——每个用户独享设定带宽、互不共享；Role/Policy List 级——把限速作为 ACL/QoS 规则的动作（还可叠 DPI 应用规则）。三层可共存，实际生效优先级见框架 f12（DPI 最细、SSID 最粗）。常见设计：SSID 级兜底总限 + 访客角色按人限速。

  tags: [bandwidth, contract, qos, access-role, ssid]

- id: p30
  title: WCF 工作机制与前提（DNS Snooping + Brightcloud）
  type: principle
  source_chapter: "p366-367"
  source_quote: |
    "Stellar AP DNS Snooping: 1. DNS request FQDN www.facebook.com. 2. FQDN filtered? 3. FQDN category? Social Network. 4. Send action to AP. 5. Create Block ACL rule to IP of the FQDN... Activate WCF: Per AP Group... or per Access Point. Configure DNS: No DNS -> WCF not in Service. Not supported: AP1101, AP1201H."
  summary: |
    Web 内容过滤的实现链路：AP 对客户端 DNS 请求做嗅探→把 FQDN 送 OV2500（内嵌 Brightcloud SDK）查分类与允许/阻断状态→结果回发 AP→AP 生成针对该 FQDN 解析 IP 的阻断 ACL，后续流量在 AP 本地拦截（默认放行、命中拒绝类目才拦）。启用粒度可按 AP Group 或单 AP；前提是 OV2500 必须配 DNS，否则状态为 Not in service；AP1101/AP1201H 不支持。WCF Profile 一个 Access Role Profile 只能绑一个。

  tags: [wcf, dns-snooping, brightcloud, acl, web-filtering]

- id: p31
  title: 漫游默认状态与快速漫游约束
  type: principle
  source_chapter: "p407/414"
  source_quote: |
    "L2 Roaming always enabled. L3 Roaming disabled by default, configured in the Advanced WLAN Service Configuration. Fast Roaming disabled by default, configured per SSID. OKC can be enabled with WPA2/WPA3 Enterprise only. 802.11r (Fast Roaming) can be enabled with WPA2/WPA3 encryption only (Personal or Enterprise)."
  summary: |
    漫游功能的默认值与依赖：L2 漫游总是开启；L3 漫游默认关闭、在 Advanced WLAN Service 里开；快速漫游（Fast Roaming）默认关闭、按 SSID 开启，且受安全级别约束——OKC（机会式密钥缓存/802.11k）只能配在 WPA2/WPA3 Enterprise，802.11r（FT 快速 BSS 切换）只能配在 WPA2/WPA3 加密（Personal 或 Enterprise 均可）。开错组合（如对 Open SSID 开 11r）会直接配不上；不开快速漫游则回落标准漫游（重新走 RADIUS）。

  tags: [roaming, fast-roaming, okc, 802.11r, defaults]

- id: p32
  title: Roaming RSSI 阈值推荐值与两个极端
  type: principle
  source_chapter: "p424"
  source_quote: |
    "Value range is 0-100. Recommended value for 2.4GHz: RSSI = 10. Recommended value for 5GHz: RSSI = 15. The Roaming RSSI Threshold controls the signal strength a client needs to see before searching for another site. If the RSSI threshold is too low, the client remains on a low signal strength site. If the RSSI threshold is too high, the client roams too much that could result to packet loss."
  summary: |
    RF Profile 里 Roaming RSSI Threshold 的调参基准：取值 0-100，推荐 2.4 GHz 用 10、5 GHz 用 15，并配合 802.11k/802.11v 使用。阈值含义是终端感知信号低于该值才发起找新 AP。两个失败模式要背：设太低——终端粘在弱信号 AP 上不切换（粘性终端）；设太高——频繁切换反而丢包。调优时从推荐值起小幅试。

  tags: [rssi-threshold, sticky-client, roaming, rf-profile, tuning]

- id: p33
  title: 广播/组播优化参数（密钥轮换/广播过滤/组播转单播上限）
  type: principle
  source_chapter: "p502-503"
  source_quote: |
    "Broadcast Key rotation: Only applicable for Enterprise. Rotate the keys periodically to avoid key cracking. Default period: 15 min - Range 1 min - 24 hours. Broadcast Filter All: Drop all broadcast packets except DHCP & ARP. Broadcast Filter ARP: Convert broadcast ARP to unicast ARP. Multicast Optimization: Convert multicast to unicast, uses the highest data rate... Channel Utilization: default value 90%; Number of Clients: default value 6."
  summary: |
    Advanced WLAN Service 里的空口优化参数：广播密钥轮换仅限 Enterprise 安全级，默认 15 分钟（可调 1 分钟-24 小时）周期轮换 PTK/GTK 防破解；Broadcast Filter All 丢弃除 DHCP/ARP 外全部广播，Broadcast Filter ARP 把广播 ARP 转单播（无组播业务时推荐开启）；组播优化把组播转单播、用单播密钥和最高速率发送，但在信道利用率超 90%（默认）或高吞吐客户端数超 6（默认）时自动停止，防 CPU 过载。

  tags: [broadcast-filter, multicast-optimization, key-rotation, airtime]

- id: p34
  title: WMM QoS 四类推荐映射（802.1p/DSCP）
  type: principle
  source_chapter: "p505"
  source_quote: |
    "Recommended Settings: WMM 802.1p DSCP. Best Effort: 0 / 0. Background: 2 / 18 - AF21. Voice: 5 / 46 - EF. Video: 4 / 34 - AF41. Default OV Settings: Best Effort 0,3 / 0x00, 0x18; Background 1,2 / 0x08, 0x10; Voice 6,7 / 0x30, 0x38; Video 4,5 / 0x20, 0x28."
  summary: |
    WMM 四队列与 802.1p/DSCP 的映射基准：推荐配置——Best Effort=1p 0/DSCP 0、Background=1p 2/DSCP 18(AF21)、Voice=1p 5/DSCP 46(EF)、Video=1p 4/DSCP 34(AF41)；OV 默认配置把四类各扩成两个 1p/DSCP 档（如 Voice 6,7→48/56）。语音走 EF、视频走 AF41 是跨设备对接的行业惯例，与运营商/骨干 QoS 策略对齐时以推荐表为准。

  tags: [wmm, qos, 802.1p, dscp, mapping]

- id: p35
  title: 四种勘测类型对比（预测/被动/主动/吞吐+频谱）
  type: principle
  source_chapter: "p93"
  source_quote: |
    "Predictive Survey: Simulate RF by defining wall, placing Simulated heatmaps of capacity and coverage. Passive Survey: Walk around, collect beacons, probes, measure signal strength, interference, SNR for all APs -> SNR, RSSI, interference heatmaps for all APs. Active Survey: Walk, connect to the network, test for packet loss, RTT, association -> Heatmaps and analysis for roaming. Throughput Survey: Measure throughput and jitter. Spectrum Survey: Detect all RF sources -> Interferers, duty cycle."
  summary: |
    勘测类型选型表：预测勘测在软件里建墙仿真、出容量覆盖模拟热图（无需到场）；被动勘测现场走测只听不关联，采集全部 AP 的信标/信号强度/干扰/SNR；主动勘测关联到网络实测丢包、RTT、关联与漫游行为；吞吐勘测专测吞吐与抖动（瞬时容量/语音分析）；频谱勘测检测所有 RF 源（含非 WiFi 干扰源与占空比）。项目映射（p455）：新部署/换网用预测，部署后 RF 分析用被动，客户端性能分析用主动。

  tags: [survey-types, passive, active, predictive, spectrum]

- id: p36
  title: BLE Beaconing 默认参数
  type: principle
  source_chapter: "p170"
  source_quote: |
    "BLE Beacon is configured per AP Group. Turned OFF by default. Configurable parameters are: Beaconing Mode: iBeacon per default; Transmission Power; Frequency/Emission Period; UUID (Universal Unique Identifier) - ALE specific UUID for all ALE products; Major and Minor values - used for greater accuracy than UUID alone."
  summary: |
    AP 内置 BLE 信标做资产/人员定位时的参数口径：按 AP Group 配置、默认关闭；可调项——信标模式（默认 iBeacon）、发射功率、发射周期、UUID（ALE 全产品统一 UUID）、Major/Minor（比 UUID 单独定位更精细的分层字段）。AP1230/13xx 系列自带 BLE。配套生态：AeroScout RTLS 用 Stellar AP 上报的标签 RSSI 做定位引擎（p171）。

  tags: [ble, ibeacon, asset-tracking, default-off]

- id: p37
  title: IPv6 支持范围（客户端/管理面全支持，RADIUS 仍走 IPv4）
  type: principle
  source_chapter: "p173-174"
  source_quote: |
    "IPv6 Client Support - Enterprise Mode: AP Management through IPv6; Client MAC/1X Authentication: Client authentication request to AP through IPv6; Radius communication between AP and UPAM through IPv4; Client Portal Authentication: Client to portal server through IPv6; Portal server to Radius Server through IPv4."
  summary: |
    Enterprise 模式 IPv6 能力边界：AP 管理接口可拿 IPv6（DHCPv6 取地址/网关/DNS）；客户端 802.1X/MAC 认证请求可走 IPv6 到 AP，但 AP 到 UPAM 的 RADIUS 通信仍是 IPv4；门户认证客户端到门户服务器可走 IPv6，门户服务器到 RADIUS 仍是 IPv4。客户端流量在 IPv6 客户端与 IPv6 网关间正常转发并支持 IPv6 QoS/ACL。规划纯 IPv6 管理网时要留意 RADIUS 链路仍需 IPv4 通路。

  tags: [ipv6, radius, enterprise, limitation]

- id: p38
  title: Stellar AP 硬件共性规格（专用扫描射频/SSID 数/客户端数/温度）
  type: principle
  source_chapter: "p184-195"
  source_quote: |
    "AP1301: 1 full band (radio) dedicated to radio scanning; Improving network security and Wi-Fi quality. Up to 16 SSID (8 per radio); 512 clients per AP... AP1451: Up to 48 SSID (16 BSSID per radio); 1536 clients per AP... Operating Temp: 0°C to 45°C (indoor); AP1361: Temperature range -40 to +65 degree C (outdoor)."
  summary: |
    选型时常用的系列共性参数：WiFi 6 起中高端机型（AP1301/1301H/1311/1320/1331/1351/1360、6E 的 AP1451 等）配 1 个全频段专用扫描射频，专职安全与射频质量监测；每射频 SSID/BSSID 数——入门 8 个、多数 16 个（AP1451 三射频可达 48 SSID）；单 AP 客户端数——入门 512、中端 1024、高端 1536；室内机工作温度 0-45 °C，户外 AP1361 为 -40 到 +65 °C。PoE 档位从 802.3af（AP1301 全功能）到 802.3bt（AP1331/1431/1451/1521）。

  tags: [hardware, ap-specs, scanning-radio, ssid-count, temperature]

- id: p39
  title: WiFi4EU 与 Hotspot 2.0 要求
  type: principle
  source_chapter: "p506-507"
  source_quote: |
    "WiFi4EU: European Union Initiative, to provide free WiFi access to citizen in public venues; Networks with WiFi4EU SSID use an HTTPS Captive Portal; Session timeout should be configurable up to 12 hours. Hotspot 2.0 is a WLAN Service option. Stellar Access Point support 802.11u (GAS/ANPQ), EAP-SIM / EAP-AKA."
  summary: |
    两个公共热点特性：WiFi4EU 是欧盟公共场所免费 WiFi 计划，SSID 必须用 HTTPS 强制门户，会话超时需可配置到最长 12 小时（配置入口在 Guest SSID 的 Guest Access Strategy）；Hotspot 2.0（Passpoint）做无缝安全接入，Stellar AP 支持 802.11u（GAS/ANQP）与 EAP-SIM/EAP-AKA（SIM 卡认证、运营商分流），配置入口在 WPA2-Enterprise SSID 的 Advanced WLAN configuration。

  tags: [wifi4eu, hotspot-2.0, 802.11u, eap-sim, public-wifi]


# cases（10 条）

- id: c01
  title: Lab：远程实验室连接与整机重置（Reset PODX 脚本）
  type: case
  source_chapter: "p207-216"
  source_quote: |
    "A shortcut Reset PODX is available on the desktop to reinitialize all the equipment... THE SWITCHES DEFAULT CONFIGURATION IS NOT AN EMPTY CONFIGURATION! A SPECIFIC CONFIGURATION IS APPLIED TO THE SWITCHES; ALL THE INTERFACES ARE PUT DOWN... THE OMNISWITCH 6870 IS PRE-CONFIGURED (VLAN, IP interface...)... @Switch > The reinitialization process takes around 5 minutes; @Access Point > around 1min30 - 2min."
  summary: |
    目标：接入 R-Lab 并把整套环境复位到初始态。步骤：浏览器连 https://rdp.al-mydemo.com/ 远程桌面（推荐 Chrome/Edge），按分配的 POD 号（25-32）用 stellanpodXa 账号登录；重置交换机与 AP 用桌面 Reset PodX 脚本——注意脚本给交换机灌的是特定预配置而非空配置、全部接口被置 down（实验中要手工 enable 所用接口）、6870 预配了 VLAN 和 IP 接口，耗时约 5 分钟，AP 约 1 分半-2 分钟；重置 OV2500 用 vSphere 恢复快照 "DT00XTE26X - Initial State" 后重启 VM（快照即保存虚机某时刻状态，用于抹掉上一期培训配置）。验证：TeraTerm 控制台能打开交换机并看到消息；Raspberry Pi 客户端（VNC，user/superuser）可达。

  tags: [rlab, reset, snapshot, vsphere, lab-setup]

- id: c02
  title: Lab：OV2500 首次登录与评估许可生成安装
  type: case
  source_chapter: "p217-222"
  source_quote: |
    "An Evaluation License provides full OmniVista 2500 NMS feature functionality, but is valid only for 90 Days... Enter: Customer ID: 99999, Order Number: evaluation; License Type: EVAL-OV2500-ALL-TYPE_1; Passcode: omnivista. 2 possibilities: Inserting directly the license file... Inserting the license keys. Don't do both!"
  summary: |
    目标：完成 OV2500 首登并装上全功能评估许可。步骤：（1）浏览器访问 10.130.5.5X，默认 admin/switch，首登强制改密为 Training123#；（2）在 https://lds.al-enterprise.com/ 生成评估许可——Customer ID 填 99999、Order Number 填 evaluation、类型选 EVAL-OV2500-ALL-TYPE_1、口令 omnivista，生成下载许可文件（先删除桌面上往期 "-EVAL-OV2500…" 文件防混淆）；（3）安装二选一：直接 Add License 上传文件（勾 OK、不勾 Enable ProActive Lifecycle Management），或用文本编辑器打开文件把许可 key 明文逐条粘进 License Key 字段——文件与 key 两种方式只能选一种，粘 key 时只复制 key 本身不带许可名行。验证：登录后不再弹许可提示；装完删除本地许可文件。

  tags: [ov2500, license, eval, first-login, lds]

- id: c03
  title: Lab：OmniSwitch 在 OV2500 中的 SNMPv3 发现
  type: case
  source_chapter: "p252-262"
  source_quote: |
    "The backbone VLAN (VLAN 1305) is pre-configured and connects the 3 OmniSwitches, the OmniVista 2500 (10.130.5.5X) and the DHCP Server (10.130.5.7)... -> user snmpuserv3 read-write all password 'Superuser=1' sha+des; -> snmp station 10.130.5.5X 162 snmpuserv3 v3 enable... Click on Discover Now to launch the discovery process."
  summary: |
    目标：把 3 台 OmniSwitch 纳入 OV2500 管理。步骤：（1）复用预配的 Backbone VLAN 1305（互联交换机/OV2500/DHCP，承载 SNMP 流量），从 6360/2360 ping 通 6870、DHCP、OV2500 验证连通；（2）三台交换机各配 SNMPv3：`user snmpuserv3 read-write all password "Superuser=1" sha+des` + `snmp station 10.130.5.5X 162 snmpuserv3 v3 enable`；（3）OV2500 侧 NETWORK > DISCOVERY > Managed Devices 逐段新建 IP 范围（10.130.5.20X/22X/24X），建 SNMPv3 发现档案（超时 5000ms、重试 3、SHA+DES、Superuser=1），Discover Now。验证：6870/6360/2360 出现在可管理列表。排障路径（同章节）：L2 查线缆 `show interfaces`/查 VLAN `show vlan members port`→L3 查 IP 接口 `show ip interface`、OV2500 虚机菜单核 IP、双向 ping→SNMP 复核 `show snmp station` 与两侧档案后重跑发现。

  tags: [omniswitch, discovery, snmpv3, backbone-vlan, troubleshooting]

- id: c04
  title: Lab：Stellar AP 发现、信任与入组
  type: case
  source_chapter: "p263-278"
  source_quote: |
    "Create the VLAN 40 (MANAGEMENT)... Once this option [138] received, the Stellar Access Point will work in Enterprise mode... Select Country/Region = FR-France... DO NOT CHOOSE THE COUNTRY CODE USA, JAPAN OR ISRAEL... Click on Unmanaged AP > Select both > Change to Trust Status... Group name: APGX. WARNING: DO NOT ENABLE THE 'SSH LOGIN' SETTING."
  summary: |
    目标：AP1301/AP1321 两台 AP 上线并纳入 AP Group。步骤：（1）用 VLAN Manager 在三台交换机建管理 VLAN 40（6870 预配 IP 接口 10.7.X.126/27，6360/2360 纯二层）；（2）AP 所接端口 1/1/6 enable + `lanpower slot 1/1 service stop/start` 重启 PoE 强制 AP 重启；（3）DHCP 经 6870 的 dhcp relay（`ip dhcp relay destination 10.130.5.7`）转给服务器并回 option 138，AP 进 Enterprise 模式；（4）AP REGISTRATION 页选国家码（实验室必须选 FR，选 USA/日本/以色列会因硬件不兼容出问题）与时区，AP 出现在 Unmanaged 则选中点 Change to Trust Status；（5）建 AP Group APGX 并把两台 AP Change Group 进去（不要开 SSH Login 选项）。验证：Managed AP 页看到两台 AP 带 10.7.X 地址。排障工具链（p274-276）：串口 115200 8N1 登 support/aos2016，`getmode` 应为 OV、`cat /etc/config/network` 核 DHCP 模式、`getovinfo` 核 OV 地址、`ssudo ifconfig br-wan` 核 IP，必要时 `tcpdump -i br-wan -s0 -w trace.pcap` 抓 DHCP Offer 核 option 138/43。附录给出 Windows Server 上配置 option 138 的路径（Set Predefined Options > Code 138 > IP Address）。

  tags: [ap-discovery, trust, ap-group, option-138, poe, serial-console]

- id: c05
  title: Lab：安全 Employee SSID 创建（802.1X + UPAM）
  type: case
  source_chapter: "p305-325"
  source_quote: |
    "Usage: Enterprise Network for Employees (802.1X); Allowed Band: 2.4GHz and 5GHz; Encryption Type: WPA3_AES; RADIUS Server: UPAMRadiusServer; VLAN ID: 20... Authentication: ProtectedEAP; No CA certificate; PEAP version: Automatic; Inner Auth: MSCHAPv2; Username: Employee; Password: password."
  summary: |
    目标：建员工 802.1X SSID 并验证。步骤：（1）VLAN Manager 建 VLAN 20（EMPLOYEES），6870 预配 int_employee 10.7.X.62/27；（2）WLAN > SSIDs 新建 EmployeesX，Usage 选 Enterprise Network for Employees，频段 2.4+5 GHz，加密 WPA3_AES，认证策略 RADIUS 选 UPAMRadiusServer，用 Manage Employee Accounts 快捷建账号 Employee/password（账号实际落在 UPAM > Authentication > Employee Account，支持 xls/csv 批量导入）；（3）默认 VLAN 20，Save and Apply to AP Group，把 SSID 从 default 组改绑到 APGX（可设广播时间表，默认 Always）。验证：树莓派选 EmployeesX，PEAP/MSCHAPv2/不校验 CA 连接，IP 落在 10.7.X.32/27，ping 通 DHCP 与 OV2500；UPAM Authentication Record 与 WLAN > Client List 能查到客户端挂在哪台 AP。专家模式附录（p321-325）按 f10 七步用手工对象重建同一 SSID（WLAN Service + AAA-Server-PODX + Access-role-employeeX + User-PODX 策略/Access Policy 按 SSID 属性映射），系统内置 NAS 条目 All Managed Devices 的共享密钥为 123456。AP 侧排障：`iwconfig`/`iwlist channel|txpower|bitrate`、`ssudo sta_list`、`wam_debug sta_list` 看 JSON（含 assignedVLAN/assignedAR/各认证来源角色）、`cat /var/config/wlanservice.conf`、`AAA_profile.conf`、`AAA_server.conf` 核对 RADIUS 地址端口 1812/1813，RADIUS 仍失败用 `tcpdump -i br-wan -s 0 host radiusIP` 抓包。

  tags: [employee-ssid, 802.1x, peap, upam, expert-mode, troubleshooting]

- id: c06
  title: Lab：Active Directory 外部认证接入 Employee SSID
  type: case
  source_chapter: "p326-331"
  source_quote: |
    "Select UPAM > SETTINGS > LDAP/AD Configuration: LDAP/AD Server: Enable; Server Type: AD; NETBIOS Domain Name: COMPANY; DNS Domain Name: company.com; FQDN/IP address of Domain Controller: 10.130.5.130; AD Port: 389... Click on Test Connection... Select External LDAP/AD > Apply."
  summary: |
    目标：把员工认证从 UPAM 本地库切到企业 AD。步骤：（1）UPAM > SETTINGS > LDAP/AD Configuration 声明 AD——启用、类型 AD、TLS/LDAPS 关（NS）、NETBIOS 域 COMPANY、DNS 域 company.com、域控 10.130.5.130、账号 ov2500/Alcatel.0、端口 389，先 Test Connection 通过再 Apply；（2）回到 EmployeesX SSID 的认证策略点 Edit，认证源从本地库改为 External LDAP/AD；（3）客户端先跑 Clean Wireless Networks 清掉已存网络，再以 PEAP/MSCHAPv2 用 AD 里的 Employee/Alcatel.0 重连。验证：IP 仍在 10.7.X.32/27 段，ping 通 DHCP/OV2500，UPAM Authentication Record 显示本次认证记录。要点：改的是认证源这一处，SSID 与 VLAN 配置不动——体现 UPAM 认证策略与 SSID 解耦的设计。

  tags: [active-directory, ldap, authentication-strategy, upam]

- id: c07
  title: Lab：Guest SSID 创建与访客运营（门户/踢线/黑名单）
  type: case
  source_chapter: "p370-387"
  source_quote: |
    "Usage: Guest Network (Open or Captive Portal); Do you want users to go through a Captive Portal? YES; Captive Portal Type: OV-UPAM Captive Portal... Portal Page: DefaultPortal; Login by: Username & Password; VLAN ID: 30... Enter any non-https URL (ex: http://2.2.2.2) and you are redirected to the Captive Portal."
  summary: |
    目标：建访客门户 SSID 并演练访客管控。步骤：（1）VLAN Manager 建 VLAN 30（GUESTS），6870 预配 int_guest 10.7.X.94/27；（2）新建 GuestsX，Usage 选 Guest Network、勾强制门户、类型 OV-UPAM Captive Portal，频段 2.4+5 GHz；（3）Manage Guest Accounts 建访客 Guest/password（可设 Data Quota，本例 Disable）；（4）Guest Access Strategy 设门户页 DefaultPortal、登录方式账密，默认 VLAN 30，绑定 APGX；（5）树莓派连 GuestsX 后手动开浏览器访问任意非 HTTPS URL（http://2.2.2.2）触发重定向到门户，输入账密勾条款登录；（6）管控演练：UPAM > Guest Device 里 KickOff 踢线（可重连）；WLAN > Client List 里 Add to Blocklist 拉黑（移出黑名单前无法重连，名单在 Client BlockList 页管理）。验证：客户端 IP 在 10.7.X.64/27 段，Authentication Record 与 Captive Portal Access Record 均有记录。排障（p382-387）：访客账号有有效期，先核 OV2500（虚机菜单 [10] Advanced Mode 后 `date`）与 AP（`date`）时间；`cat /etc/resolv.conf` 核 AP 的 DNS（门户重定向必需）；门户进程 `ps | grep eag`、在线用户 `eag_cli show user all`、踢线 `ssudo eag_cli kick user index N`、门户日志 `tail -f /tmp/log/eag.log` 等。

  tags: [guest-ssid, captive-portal, kickoff, blocklist, eag]

- id: c08
  title: Lab 附录：访客服务限制（Unified Policy 拒绝 telnet/SSH）
  type: case
  source_chapter: "p388-391"
  source_quote: |
    "Create a Policy: Set Condition: L4 Services > Service Group DeniedSrv (telnet 23, SSH 22); Set Action: QOS > Disposition: DROP; Validity Periods: AllTheTime... Policy List: Add Unified Policy DeniedServ + OV-L3-AcceptAllPolicy... Select Policy List = GuestsPolicy > Apply to Devices (VLAN 30, OS6870 + AP Group APGX)."
  summary: |
    目标：给通过认证的访客下发"禁 telnet/SSH、其余放行"的策略。步骤：（1）UNIFIED ACCESS > UNIFIED POLICY 建 Policy DeniedServ——条件选 L4 Services，先建 Service Group DeniedSrv（服务 telnet=TCP23、SSH=TCP22），动作 QoS Disposition=DROP，有效期 AllTheTime，设备选 OS6870 与 AP Group APGX（OS2360/6360 不支持）；（2）建 Policy List GuestsPolicy：顺序放 DeniedServ，兜底接默认存在的 OV-L3-AcceptAllPolicy；（3）Unify Policies/Policy List 两处各点 Notify All 下发；（4）把 Policy List 塞进访客认证后自动套用的 Access Role Profile __GuestsX，再 Apply to Devices 映射 VLAN 30 推给 OS6870+APGX。验证：重连 GuestsX 后 `ssh 10.7.X.62` 被拒。关键前提：策略只在认证成功时套用，测试前必须断开重连强制重新认证。

  tags: [unified-policy, acl, service-group, guest-restriction, drop]

- id: c09
  title: Lab：Web 内容过滤（拒社交网络与博彩类目）
  type: case
  source_chapter: "p392-402"
  source_quote: |
    "Activate WCF per AP Group... WCF Profile: Name: WCF-guests; Category: Social Networking > Reject; Category: Gambling > Reject... Select WCF-Guests in the Access Role Profile __GuestsX... Map to VLAN 30... google.com OK; facebook.com KO... The WCF feature requires the DNS configuration on the OmniVista server."
  summary: |
    目标：访客网屏蔽 Social Networking 与 Gambling 两类网站。步骤：（1）NETWORK > AP REGISTRATION > AP Group 编辑 APGX，勾选启用 Web Content Filtering 并 Commit（也可按单 AP 在 Access Point > Edit > Web Content Filtering 开 Private Config）；（2）UPAM > Web Content Filtering > WCF Profile 建 WCF-guests：类目 Social Networking 动作 Reject、类目 Gambling 动作 Reject，其余流量默认 Accept；（3）把 WCF-guests 绑到访客角色 __GuestsX，随后必须 Apply to Devices（Map to VLAN 30、选 OS6870+APGX）——只改 ARP 不下发则配置停留在 OV 服务器上不会推给 AP。验证：访客连 GuestsX 过门户后，google.com 可达，facebook/twitter/unibet 全部被拒（阻断 ACL 已推到 AP，AP 不再转发该站点的客户端 DNS）。排障：WCF 显示 Not in service 时查 OV2500 DNS——虚机控制台 [2] 配置/[6] DNS，补上 10.130.5.130 与 10.0.0.51 后重启服务生效。

  tags: [wcf, category-filter, brightcloud, access-role, dns]

- id: c10
  title: Lab：RAP 部署（Cirrus 4 Freemium + OV2500 + ALE VPN Server）
  type: case
  source_chapter: "p467-497"
  source_quote: |
    "Enter the AP Serial Number; Select Device Filters = AP; Enter the AP MAC Address; Select Is this a Remote AP? YES... Click on Export VPN Settings -> download <VPN Server name>.conf... Transfer the .conf file in /opt/OmniVista_2500_NMS/data/vpn_conf/vpn_profile... Go to NETWORK > AP REGISTRATION > Data VPN Servers... In the Data VPN Setting, select the Data VPN Server(s) previously created... Select Use Tunnel; Enter the Tunnel ID (must be 0)."
  summary: |
    目标：把一台 Stellar AP 部署成远程 AP，广播企业员工 SSID，数据走 VPN 回总部。步骤：（1）读 AP 尾部标签取序列号/MAC，在 Cirrus 4（registration.ovcirrus.com，Freemium 账号）Inventory > Device Catalog 录入并勾 Is this a Remote AP=YES；（2）配 VPN（管理隧道）参数——服务器公网 IP/端口 6550、Server's VPN IP 192.168.0.1、客户端池 192.168.0.2-20、OV2500 IP，Export VPN Settings 导出 .conf（文件务必保存好）；（3）AP 接互联网上电，Cirrus 显示已注册；（4）配置 ALE VPN Server 虚机（ESXi 部署 OVF）：控制台设 admin 密码、eth0 公网 IP、eth1 私网 10.130.5.251、网关/DNS，开 SSH（端口 22），FileZilla 把 .conf 传到 /opt/OmniVista_2500_NMS/data/vpn_conf/vpn_profile，建 vpn_mgmt 服务（绑公网 IP:6550）并导入 VPN endpoint（None/Layer 3 VPN），Apply 后重启 AP，Maintenance > VPN Status 应出现 peer 与握手记录；（5）OV2500 侧：虚机菜单加默认路由（192.168.0.0/24 网关 10.130.5.251），AP REGISTRATION 里选国家码后 RAP 出现在 Managed AP；NETWORK > AP REGISTRATION > Data VPN Servers 建第二条客户端数据 VPN（server 10.7.0.61、客户端池 10.7.0.55-60）并同样导出 .conf 导入 VPN 服务器（vpn_data、端口 6551、绑 eth2）；（6）AP Group 的 Data VPN Setting 选中新 Data VPN Server；（7）建 EmployeesX SSID 时 Default VLAN/Network 选 Use Tunnel、Tunnel ID 填 0 并选择 VPN Server，下发。验证：远程 Windows 客户端连 EmployeesX，凭 Employee/password 过 802.1X，拿到员工网段地址、可访问公司网。本例地址规划：管理走 VLAN 1305（10.130.5.x），员工客户端走 VLAN 30（10.7.0.x）。

  tags: [rap, vpn-server, cirrus4, l2gre, tunnel, remote-deployment]


# counter-examples（16 条）

- id: ce01
  title: 陷阱：现场禁用 WEP（40/104 位密钥均可破）
  type: counter-example
  source_chapter: "p63"
  source_quote: |
    "WEP: Encryption Algorithm: Rivest Cipher 4 (RC4); 2 Modes: 40-BIT KEY + 24-BIT IV; 104-BIT KEY + 24-BIT IV... TOO WEAK. TOO WEAK. NEVER USE WEP ON SITE. 128 Bits Mode -> TOO WEAK."
  summary: |
    教材用全大写强调的红线：WEP 无论 64 位（40 位密钥+24 位 IV）还是 128 位（104 位密钥+24 位 IV）模式都太弱，现场永远不要用。这是全书唯一用"NEVER"字样的安全禁令。遇到遗留 WEP 网络（老打印机/老扫描仪环境）应迁移到 MAC 认证过渡或直接换 WPA2/WPA3，同时注意 6E/WiFi7 时代 PMF 强制、老协议根本进不了 6 GHz 频段。

  tags: [wep, security, forbidden, rc4]

- id: ce02
  title: 陷阱：勘测只是时间快照，预测不了未来
  type: counter-example
  source_chapter: "p133"
  source_quote: |
    "No matter how accurately the wireless site survey is done, its not possible to accurately determine future: Usage patterns; Expansions; External interferences. The Site survey is a snapshot in time. The more snapshots you have the better you can understand the environment."
  summary: |
    对勘测报告的期望管理：再精确的勘测也无法准确预知后续的使用模式变化、扩容和外部干扰出现——勘测是某一时刻的快照。应对办法是做周期性复测，多份快照对比才能理解环境的演化趋势（教材配了 1st/2nd/3rd/4th 四次快照示意）。给客户交付勘测报告时应写明这一局限性，避免"测一次管五年"的错误预期。

  tags: [site-survey, snapshot, expectation, periodic]

- id: ce03
  title: 陷阱：无线网络不要过度配置（Over provisioning）
  type: counter-example
  source_chapter: "p134"
  source_quote: |
    "Over provisioning is not a good option with wireless networks. Wireless controllers can take care of the channel interference but there are a limited number of channels in the 2.4 Ghz, 5 Ghz and 6GHz bands."
  summary: |
    有线网"多买设备总没错"的思路在无线不成立：2.4/5/6 GHz 每个频段的信道数是硬上限，AP 摆得再多，同频复用密度过高后自干扰抵消增益，控制器能自动调信道功率也救不回信道不够用的根本约束。容量不足的正确解法是重做 RF 设计（更宽频段/更窄蜂窝/卸载到 6 GHz），而非盲目堆 AP。

  tags: [over-provisioning, co-channel, capacity, design-error]

- id: ce04
  title: 陷阱：勘测复现不了大规模并发，也算不出天线朝向
  type: counter-example
  source_chapter: "p135"
  source_quote: |
    "It is difficult to replicate the whole set-up for wireless network, during the site survey. The results of a large number of concurrent users simultaneously accessing the wireless network is different from the site survey results. Site survey software cannot accommodate/suggest antenna orientation or directional coverage. Antennas must be adjusted manually."
  summary: |
    勘测数据的两个盲区：（1）勘测环境很难 1:1 复刻真实负载，大量用户并发接入时的实测表现会偏离勘测结果——勘测热图好不代表高峰期体验好；（2）勘测软件无法建议天线朝向或定向覆盖形状，外接天线的方向图必须人工调整验证。交付后遇到"勘测全绿、用户吐槽"的场景，先查这两条。

  tags: [survey-limitation, concurrency, antenna-orientation, gap]

- id: ce05
  title: 陷阱：金属吸波、电梯屏蔽、镀膜玻璃掉信号
  type: counter-example
  source_chapter: "p136"
  source_quote: |
    "Materials such as brick, plaster, cement, metal, stone, and double-glazed glass may cause problems. Metal absorb Wi-Fi signals. Elevators block Wi-Fi signals to a great extent. To cover inside an elevator place APs at the top or bottom of the shaft or in the car itself. Tinted glass and window film have metal in them so expect a drop in signal strength."
  summary: |
    建筑材质的三个高频翻车点：金属直接吸收 WiFi 信号（货架、文件柜、机柜旁都是弱覆盖区）；电梯井对信号近乎全屏蔽，要覆盖轿厢内必须把 AP 放井道顶部/底部或轿厢内；着色玻璃和窗贴膜含金属成分，穿过后信号强度会明显下降。非多孔材质墙体也会让覆盖半径变小或速率变慢。勘测画墙时这些要与 p113-115 的 dB 常数一起计入。

  tags: [materials, metal, elevator, tinted-glass, attenuation]

- id: ce06
  title: 陷阱：Express 切 Enterprise 不迁移配置，集群配置全丢
  type: counter-example
  source_chapter: "p157"
  source_quote: |
    "Mode can be changed: Manually in Express mode with a 'Convert to Enterprise' button; Or requires a factory reset (push button) and reboot... Add option 138 in the DHCP server for the AP management scope... No configuration migration, AP cluster configuration is lost."
  summary: |
    模式迁移的代价必须提前告知客户：从 WiFi Express（集群）切到 WiFi Enterprise（OV 管理）时，原集群的配置不迁移、直接丢失。正确姿势是先在 DHCP 管理 VLAN 作用域加 option 138，再用 Express 界面的 Convert to Enterprise 按钮或恢复出厂重启用 AP 进 Enterprise 模式，然后在 OV2500 里重建 SSID/策略等配置。变更窗口里要预留配置重建时间。

  tags: [mode-change, migration, config-loss, express-to-enterprise]

- id: ce07
  title: 陷阱：AP 不出现在 Unregistered 列表的五查清单
  type: counter-example
  source_chapter: "p250"
  source_quote: |
    "Check the Managed tab (the AP has been manually added)... The AP did not contact OmniVista: Check option 138 on the DHCP Server: Option 138 is missing; Wrong IP address in the option 138. Check the network infrastructure: Management VLAN is missing; Missing route in a L3 network; 'ip dhcp-relay' not configured on the OmniSwitch. OmniVista 2500 is not ready: Check that all the OmniVista services are started from the Watchdog."
  summary: |
    AP 无影的排查顺序：先看 Managed 页（可能已被手工添加自动入列）；再查 option 138（缺失或 IP 填错都直接断联系）；再查网络侧（管理 VLAN 没放通、三层缺路由、交换机没配 ip dhcp-relay）；最后查 OV2500 本身——从 Watchdog 确认所有服务状态为 Running。这五条覆盖了 Enterprise 上线故障的绝大多数根因，按序排查避免乱抓。

  tags: [troubleshooting, ap-registration, option-138, dhcp-relay, watchdog]

- id: ce08
  title: 陷阱：国家码不匹配=射频全关；实验室禁选 USA/日本/以色列
  type: counter-example
  source_chapter: "p243/270"
  source_quote: |
    "AP is unmanaged when Registration fails... Country Code does not match the Country Code from the RF Profile. Configuration not applied & All Radios are off." / "DO NOT CHOOSE THE COUNTRY CODE USA, JAPAN OR ISRAEL AS THE STELLAR ACCESS POINTS USED IN THE REMOTE LAB ARE NOT COMPATIBLE WITH THESE COUNTRY CODES."
  summary: |
    两层教训：（1）通用规则——AP 国家码与 OV2500 RF Profile 国家码不一致即注册失败进 Unmanaged，配置不下发且全部射频关闭；跨国项目里灰 parallel 进口设备常踩这条；（2）实验室特例——R-Lab 的 Stellar AP 硬件与 USA/日本/以色列国家码不兼容，选国家码必须选 FR-France，否则直接兼容性问题。设定国家码时硬件来源与 RF Profile 两边都要核。

  tags: [country-code, rf-profile, radios-off, registration-failure]

- id: ce09
  title: 陷阱：AP Group 属性里不要开 SSH Login
  type: counter-example
  source_chapter: "p271"
  source_quote: |
    "WARNING: DO NOT ENABLE THE 'SSH LOGIN' SETTING (in the AP Group properties)."
  summary: |
    实验与生产中都适用的告警：AP Group 属性面板里的 SSH Login 选项不要启用。Enterprise 模式下 AP 的 SSH 控制台默认是关闭的（OV2500 的 CLI Terminal 进不去），官方路径是 Network > AP Registration > AP Group 里编辑并修改 support/root 密码来激活 SSH；但课程明确要求不要开该选项——AP 侧排障应使用实验室预置的 AP 控制台连接，并保持 AP Group 密码不动，避免破坏环境一致性。

  tags: [ssh-login, ap-group, security, warning]

- id: ce10
  title: 陷阱：许可 key 只贴 key 不贴整行，文件与 key 二选一
  type: counter-example
  source_chapter: "p220"
  source_quote: |
    "2 possibilities: Inserting directly the license file... Inserting the license keys. Don't do both!... COPY AND PASTE ONLY THE LICENSE KEYS AND NOT THE ENTIRE LINES! EVAL-NM-EX-20-N, KEQWEXRH-VXDJBEUM-4EX$299Z-..."
  summary: |
    安装评估许可的两个易错点：（1）文件导入与 key 手工粘贴两种方式只能选其一，同时做会冲突；（2）粘 key 时只复制许可 key 本身，不要把整行（含许可名如 "EVAL-NM-EX-20-N,"）一起复制，否则提交失败。许可文件本身是明文，用记事本打开即可逐条取 key。装完记得删除本地许可文件，防止下期培训混淆。

  tags: [license, installation, key-format, warning]

- id: ce11
  title: 陷阱：Roaming RSSI 阈值过低粘终端、过高频切换
  type: counter-example
  source_chapter: "p424"
  source_quote: |
    "If the RSSI threshold is too low, the client remains on a low signal strength site, even with a stronger site nearby. If the RSSI threshold is too high, the client roams too much that could result to packet loss."
  summary: |
    漫游调参的双向失败模式：阈值太低——终端守着弱信号 AP 不肯走，明明旁边有更强信号也不切换（粘性终端症状）；阈值太高——终端过于敏感频繁换 AP，每次切换都可能丢包。推荐起点 2.4 GHz=10、5 GHz=15（范围 0-100），配合 802.11k/802.11v。调优时症状对号：用户"信号差还不断线"查偏低，"频繁掉线切换"查偏高。

  tags: [rssi-threshold, sticky-client, roaming, tuning, failure-mode]

- id: ce12
  title: 陷阱：背景扫描打断实时业务（语音除外）
  type: counter-example
  source_chapter: "p425"
  source_quote: |
    "When a user roams, his real time traffic can be interrupted if the new AP on which he is connected is using the background scanning. No impact on the voice traffic. The AP is voice aware and will deactivate the background scanning when a voice call is detected. Other real-time traffic can be impacted. Solution: Deactivate the Background scanning on the Stellar APs, or Install new Stellar APs acting as dedicated scanning APs."
  summary: |
    背景扫描与实时业务的冲突：用户漫游到一台正在做背景扫描的 AP 时，实时流量可能被打断。语音有幸免机制——AP 具备语音感知，检测到通话会暂停背景扫描；但其他实时业务（视频会议、流媒体）没有这层保护。两种解法：直接关 AP 的背景扫描，或加装专用扫描 AP（代价是要额外采购 AP）。高实时业务占比的场馆/医院网络要在设计期就决策。

  tags: [background-scanning, real-time, voice-aware, design-tradeoff]

- id: ce13
  title: 陷阱：AP 地理相邻却电波互不可见，漫游失效
  type: counter-example
  source_chapter: "p423"
  source_quote: |
    "In some cases, Stellar APs are geographical neighbors but can't see each other (i.e: radio waves blocked by corridor with right angles...). The client context can't be shared. No roaming. Solution: On both AP, add statically the neighbor Stellar AP from the list of known AP. The client context can be shared through the LAN and the client can roam."
  summary: |
    漫游失效的一类隐蔽根因：两台 AP 空间上相邻，但电波被直角走廊等结构遮挡，互相发现不了——空口邻居发现失败导致客户端上下文无法共享，漫游直接不发生。解法是在两台 AP 上互配静态 Neighbor AP（AP Registration > Access Point 视图里点 Neighbor AP 链接编辑，两边都要配），让上下文改走 LAN 共享，漫游恢复。排查"走到固定区域必掉线"类工单时优先怀疑这个。

  tags: [neighbor-ap, roaming-failure, rf-blocked, static-config]

- id: ce14
  title: 陷阱：OV2500 没配 DNS，WCF 直接 Not in service
  type: counter-example
  source_chapter: "p401"
  source_quote: |
    "The Web Content Filtering feature requires the DNS configuration on the OmniVista server. If the DNS configuration is missing in the OmniVista 2500, the status of the WCF feature will be 'Not in service' and the OmniVista won't be able to join the Brightcloud API."
  summary: |
    WCF 部署的前置条件常被漏掉：OV2500 服务器本身必须配好 DNS，否则 WCF 状态停在 Not in service，根本连不上 Brightcloud 云分类 API——此时 AP Group 开了 WCF、Profile 配了类目也全部无效。修复路径：vSphere 进 OV2500 控制台，菜单 [2]/[6] 配置 DNS 服务器（本实验为 10.130.5.130 与 10.0.0.51），服务需重启生效。验收 WCF 部署时第一步先看 WCF Profile 页的运行状态。

  tags: [wcf, dns, brightcloud, not-in-service, prerequisite]

- id: ce15
  title: 陷阱：策略在认证时套用，改完不重连不生效
  type: counter-example
  source_chapter: "p391"
  source_quote: |
    "BEFORE PERFORMING THE TEST, BE SURE TO DISCONNECT AND RECONNECT THE VIRTUAL MACHINE FROM THE NETWORK TO FORCE THE RE AUTHENTICATION AS THE POLICY IS APPLIED ONCE THE CLIENT AUTHENTICATION IS SUCCESSFUL."
  summary: |
    Unified Policy/Policy List 的生效时机：策略在客户端认证成功那一刻套用到用户角色上。修改或新下发策略后，已在线的用户不会自动吃到新策略——必须断开重连（强制重新认证）才应用。测试策略与生产变更都适用：改完 Access Role Profile/Policy List 后先让目标用户重连再验结论，否则会误判"策略没生效"。

  tags: [policy, re-authentication, timing, testing]

- id: ce16
  title: 陷阱：访客账号过期与服务器/AP 时间不同步
  type: counter-example
  source_chapter: "p382-383"
  source_quote: |
    "A guest account has an expiration date. It is important to check that the date and time are correctly set up... OmniVista 2500 Console: Choose option [10] Advanced Mode, From the CLI, use the command date... support@AP-0E:E0:~$ date (on the Stellar AP)."
  summary: |
    访客认证失败的隐藏变量：Guest 账号带有效期，而有效期判断依赖系统时钟——OV2500 与 AP 两端的日期时间任一不准，都会出现"账号明明没到期却登录失败"。排障动作固定两步：OV2500 虚机菜单 [10] Advanced Mode 后执行 `date`；AP 串口下执行 `date`。同类问题也影响门户 HTTPS 证书校验。部署时给 OV2500 与 AP 配 NTP 是根治方案。

  tags: [guest-account, expiration, ntp, time-sync, troubleshooting]

# glossary（45 条，免验保留）


- id: g01
  title: IEEE 802.11 与 Wi-Fi 联盟（标准 vs 认证）
  type: glossary
  source_chapter: "p6"
  source_quote: |
    "IEEE 802.11: Institute of Electrical and Electronics Engineers. Wi-Fi: Wireless Fidelity, Wi-Fi Alliance. CERTIFICATION: STANDARD: WI-FI ALLIANCE, IEEE. 802.11 ≈ WI-FI."
  summary: |
    IEEE 802.11 是电气电子工程师学会制定的技术标准家族；Wi-Fi 则是 Wi-Fi 联盟（行业组织）提供的互操作性认证与商标。联盟提供兼容性指南、设备命名（WiFi 4/5/6/6E/7）与产品描述规范。两者约等但视角不同：一个管标准文本，一个管认证贴标。售前沟通时"802.11ax"与"WiFi 6"是同一事物的两种叫法。

  tags: [802.11, wifi-alliance, standard, certification]

- id: g02
  title: BSS / BSSID / DS（基本服务集及其标识）
  type: glossary
  source_chapter: "p10"
  source_quote: |
    "BSS (Basic Service Set): Set formed by the access point (AP) and the equipment located in its coverage area. BSSID (Basic Service Set Identifier): Each BSS is identified by a BSSID, an identifier of 6 bytes (Access Point MAC@). DS (Distribution System): Infrastructure that connect Access Points (APs)."
  summary: |
    基础设施模式的三个积木：BSS 是一台 AP 加其覆盖区内终端构成的服务集；BSSID 是 BSS 的 6 字节标识，直接取 AP 的 MAC 地址（AP 每个射频每个 SSID 各有一个 BSSID）；DS 分布系统是互联各 AP 的有线基础设施，让跨 BSS 通信成为可能。抓包时看到的"AP MAC"就是 BSSID；教材后文 AP1451 "48 SSID (16 BSSID per radio)"即按每射频 16 个 BSSID 计算。

  tags: [bss, bssid, ds, infrastructure-mode]

- id: g03
  title: ESS / ESSID / SSID（扩展服务集与网络名）
  type: glossary
  source_chapter: "p10-11"
  source_quote: |
    "ESS (Extended Service Set): One or more interconnected basic service sets (BSS) and their associated LANs. ESSID (Extended Service Set IDentifier): Also called SSID, represents the name of the ESS network (32 characters)."
  summary: |
    ESS 是经 DS 互联的一个或多个 BSS 及其关联 LAN 的总和——即同一 SSID 名下多台 AP 组成的大覆盖网。ESSID 又称 SSID，是 ESS 的网络名，最长 32 字符，即终端扫描列表里看到的 WiFi 名。注意与 BSSID 区分：SSID 是人读的名字，BSSID 是机器读的 MAC。多个 WLAN Service 也可以广播同一个 SSID 名。

  tags: [ess, essid, ssid, network-name]

- id: g04
  title: IBSS / Ad-hoc 模式（无 AP 自组网）
  type: glossary
  source_chapter: "p11"
  source_quote: |
    "IBSS (Independent Basic Service Set): Wireless network made up of at least two stations and not using an Access Point (AP). SSID (Service Set IDentifier): Represents the name of the IBSS network (32 characters)."
  summary: |
    802.11 的第二种工作模式：独立基本服务集，至少两台终端直连组网、不经过 AP，网络名同样是最长 32 字符的 SSID。与基础设施模式（BSS/ESS，经 AP 转发）相对。企业网里基本不用，但排障时终端"连了个奇怪的同名网"常是误连了 ad-hoc。

  tags: [ibss, adhoc, operating-mode]

- id: g05
  title: 802.11 修正案演进（a/b/g/n/ac/ax/be）
  type: glossary
  source_chapter: "p16-17"
  source_quote: |
    "802.11BE, 802.11B, 802.11A, 802.11G, 802.11N, 802.11AC, 802.11AX: INTRODUCTION STANDARD 802.11 AMENDMENTS. IEEE 802.11 – AMENDMENTS SPECIFICATIONS: 1997, 1999, 2003, 2009, 2019, 2013."
  summary: |
    802.11 是 1997 年的基线标准，后续以字母修正案扩展：b（1999，11 Mbps/2.4G）、a（1999，54 Mbps/5G）、g（2003，54 Mbps/2.4G）、n/HT（2009，600 Mbps，MIMO 引入）、ac/VHT（2013-14，6.9 Gbps，仅 5G Wave2 MU-MIMO）、ax/HE（2019-21，9.6 Gbps，OFDMA/TWT，6E 进 6 GHz）、be（2024，46 Gbps，WiFi 7）。与 ALE 产品对应：AP1301/1320/1331/1351/1360 属 WiFi 6，AP1411/1431/1451 属 6E，AP1511/1521 属 WiFi 7，AP1230 属 WiFi 5（p19）。

  tags: [amendments, 802.11n, 802.11ac, 802.11ax, 802.11be, evolution]

- id: g06
  title: OFDM → OFDMA 与资源单元（RU）
  type: glossary
  source_chapter: "p32"
  source_quote: |
    "OFDMA DL/UL: Enables an 802.11ax access point to simultaneously communicate with multiple devices by dividing each WiFi channel into smaller sub-channels known as Resource Units (RU). Each individual RU (or sub-channel) can be utilized for different clients that are serviced simultaneously."
  summary: |
    OFDM 是 802.11a/g/n/ac 的正交频分复用，一个时刻整条信道只服务一个用户；OFDMA（正交频分多址）是 802.11ax 引入的升级：把信道在频域切成多个资源单元 RU，不同终端的 RU 可在同一时刻并行收发（上下行都支持）。这是 WiFi 6 高密场景时延与效率提升的核心机制。WiFi 7 进一步允许多个不连续 RU 聚合（MRU）。

  tags: [ofdm, ofdma, ru, wifi6, multiplexing]

- id: g07
  title: MU-MIMO（多用户多入多出）
  type: glossary
  source_chapter: "p31"
  source_quote: |
    "802.11ax devices will use beamforming techniques to direct packets simultaneously to spatially diverse users. WiFi 5: 4x4, Downlink only. WiFi 6: 8x8, Uplink/Downlink."
  summary: |
    多用户 MIMO：AP 用波束赋形技术把数据包同时发给空间上可区分的多个用户，靠空间流并行提升容量。代际规格：WiFi 5 为 4x4 且仅下行；WiFi 6 为 8x8 且上行/下行双向；WiFi 7 提到最高 16x16。与 OFDMA 的分工见原则 p05——MU-MIMO 管大包高带宽，OFDMA 管小包低时延。

  tags: [mu-mimo, beamforming, spatial-streams, wifi6]

- id: g08
  title: QAM（正交振幅调制：256/1024/4096）
  type: glossary
  source_chapter: "p34"
  source_quote: |
    "Quadrature amplitude modulation (QAM) is a modulation scheme that results in a denser constellations to increase data rates. This is done by varying the amplitude and the phase of the signal. More bits per hertz... each symbol transmits 8-bit data (WiFi 5), 10-bit data (WiFi 6)."
  summary: |
    QAM 通过同时改变信号的幅度与相位形成更密的星座图，让每符号携带更多比特：256-QAM（WiFi 5）每符号 8 bit，1024-QAM（WiFi 6/6E）10 bit（单流 +25%），4096-QAM（WiFi 7）12 bit（原始速率再 +20%）。"每赫兹更多比特"意味着对信噪比更敏感，距离远/干扰强时自动回落低阶调制。

  tags: [qam, modulation, constellation, data-rate]

- id: g09
  title: BSS Coloring 与 CCA（同频复用染色）
  type: glossary
  source_chapter: "p39"
  source_quote: |
    "BSS Coloring allows 2 devices to transmit data on the same channel and at the same frequency as long as the colors are different. Coloring also allows WiFi 6 access points to precisely adjust Clear Channel Assessment (CCA) parameters, including energy (adaptive power) and signal detection (sensitivity thresholds) levels."
  summary: |
    WiFi 6 的空间复用机制：给每个 BSS 标一个"颜色"，同信道同频上只要颜色不同就允许并行发送，只有同色才触发同频拥避让。配套可精细调节 CCA（空闲信道评估）的能量门限与信号检测灵敏度阈值。效果是把"同信道=必须退避"放松为"同信道同色=才退避"，高密部署的信道复用率因此提升。

  tags: [bss-coloring, cca, spatial-reuse, wifi6]

- id: g10
  title: TWT（目标唤醒时间）
  type: glossary
  source_chapter: "p40"
  source_quote: |
    "Target Wake Time: STAs to negotiate with APs for the waking schedule and then send or receive data."
  summary: |
    WiFi 6 省电机制：终端（STA）与 AP 协商好各自的唤醒时间表，到点才醒来收发，其余时间深睡——对比 WiFi 5 时代终端需反复 Waiting+Sleep 空耗。对电池供电的 IoT 与手机续航收益直接。WiFi 7 进一步引入 RTWT（Restricted TWT，受限目标唤醒时间）为低时延业务保留唤醒窗口（p205）。

  tags: [twt, power-saving, wifi6, iot]

- id: g11
  title: MLO（多链路操作，WiFi 7）
  type: glossary
  source_chapter: "p42"
  source_quote: |
    "MLO: allows for multi-link aggregation between a single STA and a single AP that has multiple radio chips, including 2.4 GHz, 5 GHz, and 6 GHz chips. MLO is a MAC layer technology that can aggregate multiple links across different frequency bands into a virtual link."
  summary: |
    WiFi 7 标志性技术：单终端与带多射频芯片（2.4/5/6 GHz）的 AP 之间做链路聚合，把跨频段的多条物理链路聚成一条虚拟链路。收益是可靠性与时延（链路间冗余切换）、吞吐（带宽叠加），密集区域体验更好。教材定位其为 MAC 层技术，与物理层的 320 MHz/4096-QAM 互补。

  tags: [mlo, wifi7, multi-link, mac-layer]

- id: g12
  title: MRU（多资源单元，WiFi 7）
  type: glossary
  source_chapter: "p43"
  source_quote: |
    "In WiFi 7, each device can receive several non-continuous Resource Units. Maximum Spectrum Efficiency, Reduced Latency, Increased Bandwidth. MRUs client 1 / MRUs client 2: 20 Mhz (106+26), 80 Mhz (242+242+242+242)."
  summary: |
    WiFi 7 对 OFDMA 的增强：允许一台设备分到多个不连续的 RU 并聚合使用（如 20 MHz 里的 106+26-tone 组合、80 MHz 里的多段 242 组合），而 WiFi 6 每设备只能占一段连续 RU。收益是频谱效率最大化、时延下降、可用带宽增加——碎片化的频谱资源也能被利用。

  tags: [mru, wifi7, ofdma, spectrum-efficiency]

- id: g13
  title: AFC（自动频率协调）
  type: glossary
  source_chapter: "p44"
  source_quote: |
    "Automatic Frequency Coordination (AFC)... Either a 'coordination' mechanism to assign frequency (channel) and EIRP. AFC in FCC domain... FCC approved 7 AFC providers (Qualcomm, Federated Wireless, Sony, Comsearch, WiFi Alliance, Wireless Broadband Alliance, and Broadcom)."
  summary: |
    6 GHz 室外标准功率设备的监管协调机制：因为 6 GHz 频段已有移动网络、微波链路、卫星、射电天文等在用业务，标准功率 AP（FCC 域最高 36 dBm EIRP）必须经 AFC 系统协调分配信道与功率才能发射。FCC 批准了 7 家 AFC 服务商。EU 域则干脆禁止标准功率 AP 室外使用，只留 LPI/VLP 低功率等级。

  tags: [afc, 6ghz, regulation, outdoor, coordination]

- id: g14
  title: Greenfield（绿地频段）
  type: glossary
  source_chapter: "p27/38"
  source_quote: |
    "Reliability: Greenfield (n/ac, 6(ax), 6e, a/b/g). 6GHz: Greenfield band for WiFi. Backwards compatibility not required. 60 Channels Available."
  summary: |
    "绿地"指没有遗留设备、无需向下兼容的干净频段。6 GHz 对 WiFi 就是 Greenfield：老 a/b/g/n/ac 终端根本不支持 6 GHz，因此无需为兼容旧协议保留开销（如 2.4/5 GHz 上的保护时隙与低速率），可靠性、信道宽度利用与安全策略（强制 PMF、禁旧协议）都能一步到位。这是 6E 除容量外的第二大卖点。

  tags: [greenfield, 6ghz, backward-compatibility]

- id: g15
  title: EIRP（等效全向辐射功率）
  type: glossary
  source_chapter: "p44"
  source_quote: |
    "Device Class / Operating Bands / Maximum EIRP: Standard-Power AP (AFC Controlled): 36 dBm; Fixed Client (AFC Controlled): 36 dBm; Client Connected to Standard-Power AP: 30 dBm; Low-Power AP (indoor only): 30 dBm... LPI: 23 dBm, Maximum EIRP density 10 dBm/MHz; VLP: 14 dBm, 1 dBm/MHz."
  summary: |
    等效全向辐射功率：发射功率加天线增益后的总辐射水平，是各国无线电法规管控的对象（还分总功率与功率谱密度 dBm/MHz 两个口径）。6 GHz 规则速记：FCC 域标准功率 AP/固定客户端 36 dBm、低功率室内 AP 30 dBm、LPI 客户端 24 dBm；EU 域 LPI 23 dBm、VLP 14 dBm。教材 p138 提醒：每次更换天线都要复核 EIRP 不超所在国法定限值。

  tags: [eirp, power, regulation, antenna-gain]

- id: g16
  title: 天线三大类型与辐射图（Radiation Pattern）
  type: glossary
  source_chapter: "p49-53"
  source_quote: |
    "3 Main Types: OmniDirectional, Semi-Directional, Highly Directional. OMNIDIRECTIONAL: RF Signal > Equal in all directions; Point to Multipoint; Short Distance (Dipole). SEMI-DIRECTIONAL: Patch/Panel, Yagi. HIGHLY-DIRECTIONAL: Grid; Long Distance."
  summary: |
    辐射图是天线能量在空间分布的图形描述，三大类：全向（偶极子，各向均匀，点对多点短距，AP 内置默认）、半定向（板状 Patch/Panel、八木 Yagi，集中单方向，点对点中短距桥接）、高定向（栅格 Grid，极窄波束长距链路）。选型口径见原则 p09。Stellar 外接天线型号尾号为"2"（AP1322/AP1362），其余为内置全向。

  tags: [antenna, radiation-pattern, omni, yagi, grid]

- id: g17
  title: RSSI 与 SNR（信号强度/信噪比）
  type: glossary
  source_chapter: "p91"
  source_quote: |
    "Signal to Noise: Excellent, Good, Fair, Weak. DATA RATE / SIGNAL STRENGTH / SIGNAL TO NOISE RATIO (SNR): coverage evaluation matrix used during site surveys."
  summary: |
    RSSI 是接收信号强度指示（数值越接近 0 越强，如 -43 dBm 优于 -77 dBm）；SNR 是信号与噪声的比值，直接决定可用数据速率——勘测热图按 Excellent/Good/Fair/Weak 分档。两者与速率联动评估覆盖质量（教材配三层对照矩阵）。AP 侧排障 `iwconfig` 输出里同时给出 Signal level 与 Noise level，相减即得 SNR。

  tags: [rssi, snr, signal-strength, data-rate]

- id: g18
  title: 同频/邻频干扰与覆盖盲区
  type: glossary
  source_chapter: "p89-90"
  source_quote: |
    "Optimal access point placement... Co-Channel, Adjacent-Channel... Identify sources of interference within the area; Dead spots in the coverage area."
  summary: |
    Co-Channel Interference 是同一信道上多个 AP 互相竞争空口（同频退避）；Adjacent-Channel Interference 是相邻信道能量溢出重叠造成的干扰——高密设计里两者都靠信道复用规划与收窄信道宽度治理。Dead spot（盲区）是覆盖区域内收不到足够信号的死角，勘测热图上表现为空洞，成因多为遮挡或 AP 宕机（p463-464）。现场用 WiFi Analyzer/Ekahau 可视化定位，处置是换信道、加 AP 或挪 AP。

  tags: [co-channel, adjacent-channel, interference, dead-spot]

- id: g19
  title: 勘测类型五分法（预测/被动/主动/吞吐/频谱）
  type: glossary
  source_chapter: "p93"
  source_quote: |
    "Predictive Survey: Simulate RF by defining wall, placing. Passive Survey: Walk around, collect beacons, probes... Active Survey: Walk, connect to the network, test for packet loss, RTT, association. Throughput Survey: Measure throughput and jitter. Spectrum Survey: Detect all RF sources."
  summary: |
    站点勘测按手段分五型：预测（软件仿真）、被动（现场只听不关联，测信号/噪声/干扰/SNR）、主动（关联入网实测丢包/RTT/关联与漫游）、吞吐（专测吞吐与抖动）、频谱（检测一切 RF 源与占空比，含非 WiFi 干扰）。选型映射见原则 p35 与勘测框架 f01-f04。被动与主动的核心区别是"是否认证关联"。

  tags: [site-survey, survey-types, passive, active, spectrum]

- id: g20
  title: Ekahau 与 Heatmap（勘测工具与热图）
  type: glossary
  source_chapter: "p92"
  source_quote: |
    "A laptop with a survey application and hardware (ex. Ekahau software)... The site map is imported into Ekahau and calibrates the settings based on the requirements."
  summary: |
    Ekahau Site Survey 是教材全程使用的勘测软件（预测、主动、被动、频谱分析一体），把楼层图导入后按需求标定环境；配套装备见 p101 清单（笔记本、频谱仪、三脚架、电池包、100ft 网线、至少 3 台 AP、外置无线网卡、测距轮、相机等）。Heatmap（热图）是把 RSSI/SNR/速率/干扰等指标按位置着色的可视化结果，是勘测交付物的标准形态。OV2500 里也有 Heat Map 应用用于检查射频覆盖与漫游重叠（p422）。

  tags: [ekahau, heatmap, survey-tool, visualization]

- id: g21
  title: PoE（以太网供电）
  type: glossary
  source_chapter: "p72"
  source_quote: |
    "Enhanced CPU Performance. Power over Ethernet (PoE): Power provided by Switch. DATA + POWER over ETHERNET CABLE."
  summary: |
    企业级 AP 与家用 AP 的硬件分水岭之一：数据与电力走同一根网线、由交换机供电。标准档位：802.3af（约 15W，AP1301 全功能）、802.3at（约 30-60W，AP1230/1320 等，部分机型 2 对供电时功能受限）、802.3bt（高功率，AP1331/1431/1451/1511/1521）。无 PoE 交换机时可外加 PoE 注入器（midspan）或电源适配器（p198）。排障 AP 不上线第一步就是 `show lanpower` 查供电状态（p273）。

  tags: [poe, 802.3af, 802.3at, 802.3bt, power]

- id: g22
  title: WEP（有线等效保密）
  type: glossary
  source_chapter: "p63"
  source_quote: |
    "Wired Equivalent Privacy (WEP): Encryption Algorithm: Rivest Cipher 4 (RC4); 2 Modes: 64 Bits Mode (40-bit key + 24-bit IV), 128 Bits Mode (104-bit key + 24-bit IV); Authentication: Open System (Null Authentication) or Shared Key."
  summary: |
    最早的 802.11 安全协议（1999 前后），意图达到"与有线等效"的保密性：RC4 流加密，密钥 40 或 104 位加 24 位 IV，认证分开放系统（两帧、空认证）与共享密钥（四帧）两种。因 IV 太短可被破解，两种位宽都被判 TOO WEAK，现场禁用（见反例 ce01）。它的历史意义是定义了"认证+加密"的两段式安全框架，WPA 系沿此演进。

  tags: [wep, rc4, legacy-security, deprecated]

- id: g23
  title: TKIP（临时密钥完整性协议）
  type: glossary
  source_chapter: "p64"
  source_quote: |
    "WPA: Encryption Algorithm: RC4 + TKIP (Temporal Key Integrity Protocol); Authentication Method: PSK (Pre Shared Keys) | 802.1X/EAP."
  summary: |
    WPA 时代的过渡加密增强：仍用 RC4 算法，但每包动态换密钥（临时密钥）修补 WEP 静态密钥的致命伤。只出现在 WPA 与 WPA2 的兼容选项里（WPA_TKIP、WPA2__TKIP、WPA_PSK_TKIP 等，见 p300 枚举），现代网络只在迁就极老终端时才开。WPA2 起正确选择是 AES-CCMP。

  tags: [tkip, wpa, rc4, transitional]

- id: g24
  title: PSK 与 802.1X/EAP（Personal 与 Enterprise 两型认证）
  type: glossary
  source_chapter: "p64"
  source_quote: |
    "WPA Personal: Authentication Method: PSK (Pre Shared Keys). WPA Enterprise: Authentication Method: 802.1X/EAP."
  summary: |
    WPA 系协议的两条认证分支：Personal 型用预共享密钥 PSK——全网共享一个口令，部署最简单但密钥可被提取/共享；Enterprise 型用 802.1X 框架加 EAP 封装（实验室用 PEAP+MSCHAPv2 内层），终端与 RADIUS/UPAM 逐个认证，每用户独立凭据、支持动态下发 VLAN/角色，是企业网标准形态。WiFi6E/7 时代 6 GHz 频段只认 WPA2/WPA3 级别安全。

  tags: [psk, 802.1x, eap, peap, personal-enterprise]

- id: g25
  title: AES-CCMP（计数器模式 CBC-MAC 协议）
  type: glossary
  source_chapter: "p65"
  source_quote: |
    "WPA2: AUTHENTICATION: PSK (PERSONAL) | 802.1X-EAP (ENTERPRISE); ENCRYPTION: AES-128 / CCMP."
  summary: |
    WPA2 起的标配加密：AES-128 算法配 CCMP 协议（计数器模式加密+CBC-MAC 完整性校验），取代 RC4+TKIP。WPA3 沿用 CCMP 但 Personal 认证换 SAE、Enterprise 可升级 AES-192。OV2500 里的枚举名即 WPA2_AES、WPA3_AES。选中它基本等于选中"当代合规"的最低安全线。

  tags: [aes, ccmp, wpa2, encryption]

- id: g26
  title: SAE（对等同步认证，WPA3-Personal）
  type: glossary
  source_chapter: "p295"
  source_quote: |
    "WPA/WPA2-Personal PSK replaced by WPA3-Personal SAE (Simultaneous Authentication of Equals): Stronger Encryption Key (128 bits), Offline dictionary attack resistance, No additional complexity to connect (user side)."
  summary: |
    WPA3-Personal 用 SAE（又称 Dragonfly 握手）替代 PSK 认证：密钥协商机制使攻击者无法离线跑字典爆破，加密密钥加强到 128 位；对用户而言连接操作与 PSK 一样简单（输密码即可）。OE2500 枚举里的 WPA3_SAE_AES 即此组合。混合 WPA2/WPA3 终端的环境要注意过渡模式兼容性。

  tags: [sae, wpa3, personal, dictionary-attack]

- id: g27
  title: PMF（受保护管理帧）
  type: glossary
  source_chapter: "p28/66"
  source_quote: |
    "Security: Use the latest security methods; Disallow outdated legacy protocols; Require use of Protected Management Frames (PMF). PMF (MANDATORY) in WPA3."
  summary: |
    对信标、去关联、去认证等管理帧做加密保护，防"伪造去认证帧踢人"这类廉价攻击。6E/WiFi6 的 6 GHz 频段把 PMF 列为强制要求，WPA3 也将其作为标配（WPA2 时代为可选）。OV2500 SSID 配置里对应 PMF 相关开关，混合老终端时是兼容性考量点。

  tags: [pmf, management-frames, wpa3, 6ghz]

- id: g28
  title: CNSA（WPA3-Enterprise 192 位模式）
  type: glossary
  source_chapter: "p295"
  source_quote: |
    "WPA/WPA2-Enterprise replaced by WPA3-Enterprise. Optional 192-bit security mode (CNSA option): CNSA enabled: Only wpa3 client authorized on the SSID; CNSA disabled: wpa2 or wpa3 clients authorized on the SSID; CNSA option not enabled on AP1101 only."
  summary: |
    WPA3-Enterprise 的可选 192 位国家安全套件：开启后 SSID 只放 WPA3 客户端（高安全场景如政府/军事），关闭则 WPA2/WPA3 混合接入。是"安全最大化 vs 终端兼容性"的开关。硬件限制：仅 AP1101 不支持该选项。

  tags: [cnsa, 192-bit, wpa3-enterprise, high-security]

- id: g29
  title: Captive Portal（强制门户）与 Walled Garden
  type: glossary
  source_chapter: "p78/343/500"
  source_quote: |
    "Guest Management: GUESTS -> Captive Portal -> Internet Access / Restricted access to the network. Guest SSID + Captive Portal option... Walled Garden: Allow a wireless client to access the URLs of the whitelist without authentication."
  summary: |
    强制门户是把未认证用户重定向到登录页的接入控制（HTTP 重定向，故需访问非 HTTPS URL 触发）；Stellar 方案里门户由 UPAM 提供（OV-UPAM Captive Portal，可定制模板，也支持外部门户+MAC 认证组合）。Walled Garden（围墙花园）是门户的白名单机制：放行清单内 URL 免认证访问（如登录页资源、赞助商页面）。配套运营功能：自助注册、员工赞助审批、社交登录、接入码、条款确认。

  tags: [captive-portal, walled-garden, guest, redirection]

- id: g30
  title: UPAM（统一策略认证管理器）与 BYOD
  type: glossary
  source_chapter: "p335-336"
  source_quote: |
    "UPAM consists of Guest Access (Guest License required), BYOD Access (BYOD License required), A built-in RADIUS Server, A built-in MAC Authentication Server... BYOD: Employee user access the corporate network with its personal device, Authentication via a BYOD Captive Portal."
  summary: |
    UPAM 内嵌于 OV2500 的统一接入控制平台，服务 AOS 交换机与 Stellar AP 两类设备：含 Guest Access、BYOD Access、内置 RADIUS、内置 MAC 认证服务器四大件。BYOD（自带设备办公）指员工用个人终端经 BYOD 门户认证后访问公司网，门户与用户库由 UPAM BYOD 模块管理（许可按设备数计）。认证源支持本地库或外接 LDAP/AD/RADIUS。

  tags: [upam, byod, radius, guest-access, ov2500]

- id: g31
  title: Band Steering 与 Load Balancing（频段引导/负载均衡）
  type: glossary
  source_chapter: "p76"
  source_quote: |
    "FEATURES: Load Balancing; Band Steering. CLIENTS CONNECTED: 10 / 8 (2.4 GHZ), 5 / 8 (5 GHZ)."
  summary: |
    企业级 AP 的两项智能调度特性：Band Steering（频段引导）把双频终端推向 5/6 GHz，避免挤在拥挤的 2.4 GHz；Load Balancing（负载均衡）按各 AP 关联终端数把新终端引导到较空的 AP，平衡空口负载。Ekahau Auto-Planner 里也有对应开关（p118）。两者都是"企业无线 vs 家用无线"的差异化功能（p76-77 同类还有无缝漫游、QoS/ACL）。

  tags: [band-steering, load-balancing, features, enterprise-ap]

- id: g32
  title: AP Group（AP 组）
  type: glossary
  source_chapter: "p161/271"
  source_quote: |
    "AP Group: Multiple APs in the same AP Group, sharing the same configuration. Mix of any AP type & total number of AP limited to 4000 (Enterprise) or 255 (Express). When an AP initially registers, the AP is placed into a pre-configured 'Default' AP Group."
  summary: |
    OV2500 的配置管理单位：同组 AP 共享管理 VLAN、RF Profile、WCF、Data VPN 等属性，任何对组下发的配置同步全组。Enterprise 上限 4000 台（可多组）、Express 255 台，组数无限制，新注册 AP 自动入 Default 组。SSID 通过"绑定 AP Group+时间表"决定在哪些 AP 上广播。Express 模式里 AP-Group 则是靠 Group ID 相同而自组集群的概念（p149），同名不同机制。

  tags: [ap-group, configuration, ov2500, scale]

- id: g33
  title: RF Profile（射频档案）
  type: glossary
  source_chapter: "p243/297/424"
  source_quote: |
    "Country Code matches RF profile CC... AP Group -> RF Profile -> Specific RF Profile... Use the Roaming RSSI Threshold in the RF profile. Value range is 0-100."
  summary: |
    射频参数模板，挂在 AP Group 下：含国家码（与 AP 国家码不一致即注册失败、射频全关）、信道/功率策略、Roaming RSSI 阈值（0-100，推荐 2.4G=10/5G=15）等。专家模式对象模型里 AP Group→RF Profile 与 WLAN Service→AAA/Access Role 是两条并行的配置链（p297）。改漫游行为、换国家码都从它入手。

  tags: [rf-profile, country-code, rssi-threshold, radio]

- id: g34
  title: DHCP Option 138（CAPWAP/网管发现选项）
  type: glossary
  source_chapter: "p156"
  source_quote: |
    "DHCP option 138 equals the IP address of the OmniVista 2500 Server... option 138 192.168.0.61."
  summary: |
    DHCP 选项 138，Stellar 用它携带网管地址：AP 收到带 138 的 DHCP Offer 即从默认 Express 模式切换到 Enterprise（值=OV2500 IP）；Cirrus 云管则用 option 43。isc-dhcp 需自定义 `option ovwma code 138 = ip-address;`，OmniSwitch 原生支持 `option 138`，Windows Server 在预定义选项里加 Code 138/IP Address（p278）。排障 AP 找不到网管第一查项（ce07）。

  tags: [dhcp, option-138, enterprise-mode, onboarding]

- id: g35
  title: Access Role Profile（接入角色档案）
  type: glossary
  source_chapter: "p301"
  source_quote: |
    "An Access Role Profile contains the various UNP properties for the users assigned to this profile: QOS Policy List, Captive Portal Authentication, Bandwidth Controls. The Default Access Role Profile is assigned to the VLAN ID of the SSID."
  summary: |
    用户角色的属性包：拿到该角色的用户即获得其中的 UNP 属性——QoS Policy List、门户认证、带宽控制，并映射到 SSID 的 VLAN。来源有三：RADIUS 返回（含 LDAP 角色映射）、802.1X/MAC 认证结果、SSID 的 Default Access Role Profile 兜底。命名惯例：SSID 向导自动生成 "__SSID 名" 形态的角色（如 __Guests0）。WCF Profile 也绑在它上面（一对一）。

  tags: [access-role-profile, unp, vlan-mapping, user-role]

- id: g36
  title: AAA Server Profile（认证授权计账服务器档案）
  type: glossary
  source_chapter: "p302"
  source_quote: |
    "An AAA Server Profile is mandatory when the security level is set to Enterprise or Personal. The AAA Server Profile defines: 802.1x Authentication Servers, MAC Authentication Servers, Captive Portal Authentication Servers, Accounting Servers. The Default UPAM Server can be chosen by default."
  summary: |
    把四类服务器（802.1X 认证、MAC 认证、门户认证、计账）打包的档案，Enterprise/Personal 安全级下必选；默认可指到内置 UPAMRadiusServer（RADIUS 端口 1812/1813）。AP 侧落地为 AAA_profile.conf/AAA_server.conf。系统内置 NAS 条目 "All Managed Devices" 把所有受管设备自动纳入 UPAM 的 NAS 库，共享密钥 123456（p322）。

  tags: [aaa, radius, profile, authentication]

- id: g37
  title: Policy List / User Role（策略清单与用户角色）
  type: glossary
  source_chapter: "p360"
  source_quote: |
    "User Role = Policy List: List of Policy Rules (QoS, ACLs). Action can be: Accept/drop, Bandwidth control, Priority, 802.1p, DSCP marking, Application Policy Rules (DPI). Enforcement is bidirectional. Policy List Assignment: From RADIUS, From Access Role Profile (Default Policy List)."
  summary: |
    在 OV2500 对象模型里 User Role 就是 Policy List：一串有序策略规则，动作可为放行/丢弃、限速、优先级标记（802.1p/DSCP）乃至 DPI 应用规则（基于约 2000 个应用的签名库），执行是双向的。分配来源：RADIUS 动态下发或 Access Role Profile 的默认清单。内置角色有 Redirection（UPAM 重定向）与 Unauthorized（时间/位置策略）。构建入口在 Unified Access > Unified Policy。

  tags: [policy-list, user-role, acl, qos, dpi]

- id: g38
  title: WCF（Web 内容过滤）
  type: glossary
  source_chapter: "p366"
  source_quote: |
    "Web Content Filtering: Stellar AP DNS Snooping -> FQDN category lookup (Brightcloud SDK) -> Send Allow/Block status to Stellar AP -> ACL allow/block IP destination."
  summary: |
    基于 DNS 嗅探的网页过滤：AP 截获客户端 DNS 查询，向 OV2500（内嵌 Brightcloud 分类 SDK）查询 FQDN 类目与策略，AP 据此生成允许/阻断 ACL 到解析 IP，后续流量本地拦截。WCF Profile 定义各类目 Accept/Reject（默认全放行），绑定到 Access Role Profile（一对一）；激活粒度按 AP Group 或单 AP；前提是 OV2500 配好 DNS，AP1101/AP1201H 不支持。许可按 1:10 AP。

  tags: [wcf, dns-snooping, brightcloud, category]

- id: g39
  title: Client Context（客户端上下文）
  type: glossary
  source_chapter: "p411"
  source_quote: |
    "Client Context Content: SSID & WLAN service, MAC Address, IP Address, Currently assigned Unified Access (VLAN ID, Access Role Profile, Policy List, Redirect-URL, Captive Portal status), AP Context, Fast Roaming: PMKSA cache, FT PMK R0/R1 cache."
  summary: |
    AP 间共享的终端档案，漫游的原材料：网络侧含 SSID/WLAN Service、MAC/IP、当前 VLAN/角色/策略/重定向 URL/门户状态；AP 侧含 MAC、IP、OV 地址；快速漫游密钥缓存（PMKSA、FT PMK R0/R1）也随上下文携带。共享机制：终端关联时 AP 向空口邻居广播 Add、去关联时发 Del，新 AP 的 Add 触发旧 AP 删档；接收端若不是同一 OV 管理或没有对应 WLAN Service 则丢弃。L2/L3 漫游判定完全基于它（f13）。

  tags: [client-context, roaming, add-del, key-cache]

- id: g40
  title: L2 漫游与 L3 漫游
  type: glossary
  source_chapter: "p406"
  source_quote: |
    "Roaming relies on client context sharing between over the air adjacent APs. L2 or L3 Roaming selection based on the client VLAN between home and foreign AP. L3 Roaming based on L2 GRE tunnel between home and foreign AP. L2 Roaming always enabled; L3 Roaming disabled by default."
  summary: |
    两种漫游形态：L2 漫游——home/foreign AP 映射到同一 VLAN，终端直接切换（默认开启，无感）；L3 漫游——两侧 VLAN 不同，靠 home/foreign AP 间的 L2 GRE 隧道把终端流量送回原网段保持 IP 不变（默认关闭，Advanced WLAN Service 里开）。判定规则见框架 f13。Express 模式漫游仅限同集群内 L2。

  tags: [l2-roaming, l3-roaming, gre, vlan]

- id: g41
  title: 快速漫游术语组（OKC / 802.11r / 802.11k / 802.11v 与粘性终端）
  type: glossary
  source_chapter: "p414-417/424"
  source_quote: |
    "Support OKC (802.11k) and 802.11r. OKC / 802.11k: PMK (Pairwise Master Key) caching... Re-auth reduced to 4-way handshake. 802.11r / Fast BSS Transition (FT): Initial handshake for PTK/GTK with the new AP is done before the client roams. 802.11v (BSS Transition Management): Obtain Roaming target APs. 802.11k: Guide client to roam to best connection AP."
  summary: |
    降低漫游切换时间的组合拳：OKC（机会式密钥缓存，教材标注 802.11k）缓存 PMK，终端可在关联请求里带 PMKID，重认证压缩为 4 次握手建 PTK/GTK，仅限 WPA2/WPA3 Enterprise；802.11r（FT 快速 BSS 切换）在漫游发生前就完成与新 AP 的密钥握手，支持 Over-the-Air 与 Over-the-DS 两种模式，适用 WPA2/WPA3 加密；802.11v（BSS 过渡管理）向终端提供漫游目标 AP 列表；802.11k 引导终端漫游到最优 AP。粘性终端（Sticky Client）指该走不走的终端，靠 RF Profile 的 Roaming RSSI 阈值（2.4G=10/5G=15）加 11k/11v 治理。PMK 缓存始终存于客户端上下文，FT R0/R1 缓存仅在开 11r 时才有。

  tags: [fast-roaming, okc, 802.11r, 802.11k, 802.11v, ft, pmk]

- id: g42
  title: RAP（远程接入点）
  type: glossary
  source_chapter: "p429-430"
  source_quote: |
    "RAP = Remote Access Point. Goal: Extend the corporate network to remote site(s). Shops > Access to the corporate network to check the inventory; Booth > Events. Equipment: OmniVista Cirrus 4 (Freemium with OV2500 / Premium) + ALE VPN Server + Stellar AP (AP1101 not compatible)."
  summary: |
    把一台 Stellar AP 放到分支/家庭，经互联网与总部 ALE VPN Server 建隧道，本地广播企业 SSID、终端流量经 VPN 回公司网的管理形态。适用门店查库存、展会展位、居家办公（可本地突围 Local Breakout+VLAN 标签区分业务）。配套：Cirrus 4 云管做零接触注册（Freemium 配 OV2500 或 Premium 全云）、ALE 提供的 VPN Server 虚机；AP1101 不兼容 RAP。上线流程见 f15/c10。

  tags: [rap, remote-ap, vpn, branch, cirrus]

- id: g43
  title: GRE 隧道（L2GRE 与 Guest Tunneling）
  type: glossary
  source_chapter: "p345/485"
  source_quote: |
    "Guest Tunneling: Overlay Guest network while preserving Enterprise security. Tunnel per Access Role Profile from Access Point to a switch/router/controller. L2 GRE tunnel over L2/L3 networks... Supported switches: OS6860, OS6900. Supported routers: Nokia 7750."
  summary: |
    GRE（通用路由封装）在 Stellar 方案里的两种用法：Guest Tunneling 把访客流量按 Access Role Profile 从 AP 用 L2 GRE 隧道送到集中出口（OmniSwitch 自动建隧道、OS6860/6900 支持，也支持 7750 路由器与第三方控制器），实现访客网与企业网的物理隔离叠加；RAP 场景则用 L2GRE 做"客户端数据流量"的第二条 VPN（OV2500 > Data VPN Servers 配置，Server IP+客户端池，SSID 的 Default VLAN 选 Use Tunnel + Tunnel ID 0）。

  tags: [gre, l2gre, guest-tunneling, tunnel, rap]

- id: g44
  title: WMM 与 UAPSD（无线 QoS 与省电）
  type: glossary
  source_chapter: "p501/504"
  source_quote: |
    "UAPSD: Unscheduled Automatic Power Save Delivery is a QoS facility defined in IEEE 802.11e that extends the battery life of mobile clients. WMM QoS: Four categories; QOS treatment per category: Uplink 802.1p/DSCP, Downlink 802.1p/DSCP."
  summary: |
    WMM（WiFi 多媒体）是 802.11e 的 QoS 框架，分四类队列：Voice、Video、Best Effort、Background，每类可独立设置上/下行 802.1p 与 DSCP 标记（推荐映射见 p34：Voice=5/46-EF、Video=4/34-AF41、Background=2/18、Best Effort=0/0）。UAPSD（非调度自动省电交付）是同在 802.11e 里定义的 QoS 省电设施，延长移动终端电池寿命，作为 SSID 高级选项开关。

  tags: [wmm, uapsd, qos, 802.11e, dscp]

- id: g45
  title: Hotspot 2.0 / Passpoint 与 WiFi4EU
  type: glossary
  source_chapter: "p506"
  source_quote: |
    "Hotspot 2.0: Deliver seamless and secure network (WPA2 or WPA3 Enterprise) for clients in public spaces. Stellar Access Point support 802.11u (GAS/ANPQ), EAP-SIM / EAP-AKA... WiFi4EU: European Union Initiative to provide free WiFi access to citizen in public venues; HTTPS Captive Portal; Session timeout configurable up to 12 hours."
  summary: |
    Hotspot 2.0（Passpoint）让手机在公共场所自动发现并接入可信任网络：AP 广播 802.11u（GAS/ANQP）能力信息，终端可用 EAP-SIM/EAP-AKA 以运营商凭据认证（对接 Home AAA/HLR），实现 3G/4G 流量卸载到 WiFi。WiFi4EU 是欧盟公共场馆免费 WiFi 计划，要求 SSID 用 HTTPS 强制门户、会话超时可配到 12 小时。前者配在 WPA2-Enterprise SSID 的高级选项，后者配在 Guest SSID 的 Guest Access Strategy（p507）。

  tags: [hotspot-2.0, passpoint, 802.11u, eap-sim, wifi4eu]

