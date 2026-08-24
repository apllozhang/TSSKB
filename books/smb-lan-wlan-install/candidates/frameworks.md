# frameworks 候选 — DT00XTE301 LAN & WLAN Installation & Configuration for SMB

## F01. Stellar AP 三模式自动选择决策树（Express / Enterprise / Cloud）
- 页码：<<<PAGE 198>>>（另见 <<<PAGE 274>>>、<<<PAGE 195>>>）
- 原文摘录："IF DHCP SERVER SENDS OFFER WITH OPTION 138 = YES (IP@ OF OV2500) > AP REGISTERS AND RETRIEVES ITS CONFIGURATION FROM OV2500 / IF DHCP SERVER SENDS OFFER WITH OPTION 138 = NO > AP CONTACTS OV CIRRUS / IF AP REGISTERED IN OV CIRRUS (MAC/SN) = YES > AP RETRIEVES ITS CONFIGURATION FROM OV CIRRUS / IF AP REGISTERED IN OV CIRRUS (MAC/SN) = NO > AP BOOTS IN EXPRESS MODE"
- 提取内容：AP 上电后按 DHCP option 138 → OV2500（Enterprise 模式）→ OV Cirrus 注册检查（Cloud 模式）→ 均不命中则 Express 模式的三段式决策树。可直接复用为 Stellar 部署模式选型/故障定位流程。

## F02. Stellar 三部署模式定位与规模选型
- 页码：<<<PAGE 195>>>、<<<PAGE 185>>>、<<<PAGE 187>>>、<<<PAGE 189>>>
- 原文摘录："Wi-Fi Express / Standalone mode … Wi-Fi Enterprise - In Premise - Managed mode with OmniVista 2500 NMS … Wi-Fi Cloud - Cloud based - Managed mode with OmniVista Cirrus NMS"；"EXPRESS MODE: Self-managed standalone cluster, Up to 255 APs"；"ENTERPRISE MODE: Centralized management via the OmniVista 2500 NMS, Up to 4000 APs"；"CLOUD MODE: Centralized management via the cloud platform OmniVista Cirrus NMS, Up to 10000 APs"
- 提取内容：按"管理面位置（本机 Web / 本地 NMS / 云 NMS）+ AP 规模上限（255 / 4000 / 10000）+ 目标市场（SMB / MLE / 混合）"三维度选型框架。

## F03. OmniSwitch AOS 软件升级七步流程
- 页码：<<<PAGE 465>>>（展开于 <<<PAGE 466>>>–<<<PAGE 469>>>）
- 原文摘录："Analyse Requirements on the release note / Download the Upgrade Files / FTP the Upgrade Files to the Switch / Upgrade the image file / Verify the Software Upgrade / Certify the Software Upgrade / Upgrade uboot and/or FPGA if mandatory"
- 提取内容：读 release note → 下载 → FTP 传文件到 running 目录 → 升级镜像 → 验证 → 认证（copy running certified）→ 按需升级 uboot/FPGA。命令示例：`>>> update uboot cmm all file u-boot.8.4.1.R03.141.tar.gz`（<<<PAGE 469>>>）。

## F04. OV Cirrus 设备上线（Onboarding）四步流程
- 页码：<<<PAGE 282>>>
- 原文摘录："DECLARE THE AP IN THE OMNIVISTA CIRRUS (SERIAL NUMBER| QR CODE | XLS) / [OPTIONAL] ASSIGN AN AP GROUP TO THE AP / PERFORM CONFIGURATION (SSIDS, RADIOFREQUENCY SETTINGS, RULES …) / CHECK THAT THE AP APPEARS IN THE OMNIVISTA CIRRUS ('OV MANAGED')"
- 提取内容：申报（SN/QR/表格导入）→ 分配 AP Group → 下发配置 → 确认 "OV Managed" 状态。适用于交换机与 AP 两类设备（见 <<<PAGE 309>>>–<<<PAGE 310>>> 激活状态机）。

## F05. OV Cirrus SSID 创建向导五步流程
- 页码：<<<PAGE 365>>>、<<<PAGE 372>>>（Guest 版六步见 <<<PAGE 405>>>、<<<PAGE 413>>>）
- 原文摘录："WI-FI NETWORK (SSID) CREATION STEPS: GENERAL SETTINGS / AUTHENTICATION / ACCESS POLICY / DEFAULT VLAN | NETWORK / ASSIGNMENT & SCHEDULE"
- 提取内容：①通用设置（SSID 名、Usage、频段、加密）→ ②认证策略（UPAM/外部 RADIUS/LDAP）→ ③访问策略（SSID↔认证策略映射）→ ④默认 VLAN/隧道 + ACL/QoS → ⑤AP Group 指派与广播排程。Guest 场景增加第 4 步 "Guests Access Strategy"（门户定制 + 登录方式）。

## F06. ARP（Access Role Profile）优先级裁决规则
- 页码：<<<PAGE 382>>>（判定流程图见 <<<PAGE 385>>>）
- 原文摘录："ARP COMING FROM EXTERNAL SOURCE OR INTERNAL DATABASE [最高] / IF NO ARP … THEN ARP CONFIGURED IN THE AUTHENTICATION STRATEGY IS APPLIED. / IF NO ARP … AND NO ARP IN AUTHENTICATION STRATEGY, THEN THE DEFAULT ARP IS APPLIED."
- 提取内容：外部源（RADIUS Filter-ID / LDAP/AD）> 内部用户库 > 认证策略中的 ARP > SSID 默认 ARP（`__SSID名`）。可复用为用户分权策略排障顺序。

## F07. Lightning Config（闪电配置）触发条件与部署流程
- 页码：<<<PAGE 75>>>（条件）、<<<PAGE 474>>>–<<<PAGE 490>>>（流程）
- 原文摘录："Only first or second physical port connected with the client, no other ports connected / No prior switch configuration exist / No DHCP address assignment occurs after boot up / No remote configuration load (RCL) server and OmniVista NMS connection exists"；"Fast Setup: Go from unboxing to passing traffic in less than 5 minutes per switch."
- 提取内容：五项前置条件（仅 1/2 端口接入、无既有配置、无 DHCP 分配、无 RCL/NMS）→ 浏览器访问 https://192.168.0.1 → Recommended Defaults → Lightning Config 表单 → 改 admin 密码 → 保存并认证。开箱即用交付方法。

## F08. OmniSwitch Flash 目录与回滚模型（working / certified / user-defined）
- 页码：<<<PAGE 118>>>–<<<PAGE 124>>>（命令见 <<<PAGE 120>>>、<<<PAGE 122>>>）
- 原文摘录："The certified directory contains files that have been certified … The working directory is a holding place for new files … Command to force reboot from CERTIFIED directory: -> reload all"；"write memory flash-synchro = write memory + copy running certified"
- 提取内容：三层目录 + RAM 运行配置的保存/认证/回滚状态机，是 AOS 配置管理的方法论骨架（详见 principles P08、cases C05）。

## F09. 多交换机多 AP 环境扩展流程（AP Group 成组法）
- 页码：<<<PAGE 262>>>–<<<PAGE 268>>>
- 原文摘录："if several OmniAccess Stellar access point can reach each other (same VLAN, same IP subnetwork) and have the same Group ID, they will automatically form a group"；"The PVM is elected following the model criteria (highest model). In this exercise, the PVM is the OmniAccess Stellar AP1321"
- 提取内容：新交换机配 AP 管理 VLAN（untagged 到 AP 口、tagged 到上联）→ AP 通电取 DHCP → 与既有 AP 同 VLAN+同 Group ID 自动成组 → 统一 Web 界面管理。SMB 横向扩容标准路径。

## F10. PoE 供电特性选型（Fast PoE / Perpetual PoE / Delayed-start）
- 页码：<<<PAGE 144>>>–<<<PAGE 145>>>、<<<PAGE 154>>>
- 原文摘录："Fast PoE: Used to provide PoE power a few seconds after powering up the chassis"；"Perpetual PoE: Provides uninterrupted power to the connected device (PD) even when the switch is restarting"；"This feature is used to introduce a delay in lanpower on system bootup … leave some time for system stability"
- 提取内容：按业务需求选择：即时供电（FPoE）、重启不断电（PPoE）、等待系统稳定再供电（delayed-start，120–600 秒，5 的倍数）。

## F11. Wi-Fi 代际演进对照选型表
- 页码：<<<PAGE 45>>>
- 原文摘录："Wi-Fi 4 … 802.11n … 1.2 Gbps … WPA 2 / Wi-Fi 6 … 802.11ax … 9.6 Gbps … WPA 3 … 8x8 UL/DL MU-MIMO / Wi-Fi 7 … 802.11be … 46 Gbps … Up to 320 MHz … 16x16 MU-MIMO"
- 提取内容：按发布年、IEEE 标准、最大速率、频段、安全、信道宽度、调制、MIMO、省电机制九维度的代际对照，供 AP 选型与方案讲解复用。

## F12. OmniSwitch LAN 家族定位矩阵（Edge / Aggregation / Core）
- 页码：<<<PAGE 12>>>–<<<PAGE 13>>>
- 原文摘录："OmniSwitch 6360 … Value AOS L2+ GE / OmniSwitch 6560/E … AOS Advanced L3 licensed 10G Uplinks / OmniSwitch 6900 … AOS Advanced L2-L3 Aggregation/Core DC TOR / OmniSwitch 9900 Modular Chassis"
- 提取内容：按"Gig/10G/Hardened/Large + 接入-汇聚-核心"两轴定位全部在售机型，是 SMB 组网设备选型速查框架。

## F13. OV Cirrus 许可订购与订阅生成流程
- 页码：<<<PAGE 295>>>–<<<PAGE 300>>>
- 原文摘录："OVCX-68-BAS-3Y … License level: BASE/BUSINESS/PREMIUM … License duration 1Y/3Y/5Y"；流程："eBuy 下单 > Subscription Manager 创建订阅（最长等 24h）> 选择许可数量与客户信息 > 在 OVC UI 导入 Subscription ID + Order ID"
- 提取内容：许可 SKU 编码规则（设备类别+等级+年限）+ 订阅生命周期（Renewal/Add-on/Extension/Transfer）操作链。

## F14. SMB 标准拓扑模板（Layer 2 与 Mesh/SPB 两档）
- 页码：<<<PAGE 491>>>–<<<PAGE 493>>>
- 原文摘录："MEDIUM NETWORKS – LAYER 2 ONLY: Virtual Chassis 8 Max, Link Aggregation 20Gigs"；"MEDIUM NETWORKS, WITH MESH LAYER 2 OR SPB/LAYER 3: Full Layer 3: OSPF, BGP, SPB, PIM, Dual core 100G stacking"
- 提取内容：按冗余等级（可选/强制）、PoE 能力（.bt 90W、最大摄像头数）、上联速率分档的两套参考拓扑，配合环避免警示（<<<PAGE 494>>>）。

## F15. Stellar AP 群选举准则（PVM/SVM）
- 页码：<<<PAGE 203>>>
- 原文摘录："PVM/SVM Election: Criteria 1: highest Stellar AP model / Criteria 2: highest MAC address"
- 提取内容：先比型号高低、再比 MAC 大小的双准则选举，用于预测/验证集群主控归属。
