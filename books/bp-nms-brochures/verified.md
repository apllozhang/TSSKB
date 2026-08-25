# Verified 候选（V1 原文真实性核对 + V2/V3 抽查）

## cases

- **C1 MSP 管理多家客户网络：选 Cirrus 而非 Terra**
  场景：托管服务商要集中管理多个客户组织。决策依据 <<<PAGE 15>>>："Multi-tenancy services - Allow Managed Service Providers (MSP) and large organizations to effectively manage and monitor multiple associated customers"；而 <<<PAGE 10>>> 明确 "Multi-tenancy: OmniVista Cirrus" 仅云版支持。Terra 只有 Multi-sites（单组织多站点）。
- **C2 数据主权严格（政务/受监管行业）：选 Terra 而非 Cirrus**
  决策依据 <<<PAGE 9>>>："OmniVista Terra – On-Premises: addresses stringent requirements for local infrastructure management, data sovereignty, and advanced security compliance." 客户要求数据不出境时选本地部署 Terra。
- **C3 大型本地网络（≤5000 设备）：Terra 规格规划**
  场景： campus 全本地管理约 4000 台 AP+交换机。决策依据 <<<PAGE 15>>>："up to 5,000 devices... Scales from one to three virtual machines" — 按设备数规划 1-3 台虚机（每台 8vCPU/32GB/3TB 数据盘），超 5000 设备需评估拆分或多实例。
- **C4 老平台（OV2500/Cirrus 4）客户升级谈判**
  场景：客户担心换新平台要重配全部设备。话术依据 <<<PAGE 10>>>："Minimal device reconfiguration when migrating from OmniVista Cirrus 4 or OmniVista 2500... to the new platform" + 标准包自带迁移工具（"Migration Tool Availability - Included as part of the standard package"）。
- **C5 只想买网管软件、硬件已有维保：选 Base 档**
  场景：客户设备已购硬件维保，只要云网管。决策依据 <<<PAGE 17>>>：Base 档 "Base Support (Excluding device hardware maintenance and node support access) - Includes OVC Updates & Cloud Support access"。要硬件维保打包则升 Business（Partner Plus + AVR），最终客户要直享 ALE 支持则 Premium（<<<PAGE 16>>> "End Customer Access support"）。
- **C6 混合 ALE+第三方设备网络加 AI 运维：Network Advisor**
  场景：客户已有一批第三方交换机，想上异常检测。决策依据 <<<PAGE 1>>> "It can also interface with 3rd party devices able to send syslog" + <<<PAGE 3>>> 第三方设备走 "Syslog Server support, with manual customization for anomalies and remediation rules"，按 NETAD-TP-* 订阅（<<<PAGE 4>>>）。前提：自备虚拟机（ALE 不卖，见 X1）。
- **C7 视频监控行业客户：Milestone Plugin 优先于通用网管做摄像机运维**
  场景：安防集成商，摄像机频繁掉线需派人现场重启。决策依据 <<<PAGE 7>>>："eliminates the need for expensive on-site visits and vendor calls when camera problems arise" + "Faster resolution for more than 90% of camera issues"；且 <<<PAGE 8>>> 可按端口看 PoE 消耗并设摄像机 PoE 优先级。条件：客户用 Milestone VMS + OmniSwitch。
- **C8 OT 现场无云连接、装维外包：Smart Tool 而非 Cirrus**
  场景：工厂/交通现场，云不可达，装维人员非网络专业。决策依据 <<<PAGE 22>>>："Limited or restricted cloud connectivity in OT environments" → OST 是 "standalone, cloud-independent field utility"；差异化能力 <<<PAGE 23>>> PoE 向导 60 秒修复 + TDR 线缆测试。
- **C9 预算有限客户的零成本切入：Fleet Supervision 先行**
  场景：先给客户免费价值再谈付费网管。依据 <<<PAGE 5>>>："Free of charge online tool - Self signup approach"，先盘点资产/生命周期/支持合规（NIS2，<<<PAGE 6>>>），再据盘点结果推动软件升级与换新预算。
- **C10 OPEX 预算客户：Cirrus Flexible Pay**
  场景：客户拒绝一次性预付、要按月支出。依据 <<<PAGE 16>>>："Flexible Pay with variable durations and payment terms is available only for OmniVista Cirrus" + <<<PAGE 19>>> OVC-C-ESS-M / OVC-C-ADV-M 按月定价、12-60 月期限、月/季/年/预付四种付款节奏。注意 Essential/Advanced 设备分档对应关系。

## counter-examples

- **X1 Network Advisor 虚拟机需自购，ALE 不卖** <<<PAGE 3>>>
  "Virtual Appliance to be acquired separately (not sold by ALE)"
  要点：NetAdvisor 本地组件的虚拟机要客户自备，报价时勿遗漏。
- **X2 NetAdvisor 不依赖 OmniVista Cirrus** <<<PAGE 3>>>
  "OmniVista Cirrus is not required"
  要点：买 NetAdvisor 不强制先买 Cirrus。
- **X3 NetAdvisor 用户必须有 Rainbow 账号** <<<PAGE 3>>>
  "OmniVista Network Advisor users must have an active Rainbow account"
  要点：交互全靠 Rainbow Bot/Bubble，无 Rainbow 无法用（p2 "Uses a dedicated Rainbow Bot and Bubble"）。
- **X4 NetAdvisor 第三方设备能力受限：仅 syslog + 手工定制** <<<PAGE 3>>>
  "Third-Party devices able to send syslogs (over Syslog Server support, with manual customization for anomalies and remediation rules)"
  要点：第三方设备无深度遥测，异常/修复规则要手工配。
- **X5 新 OmniVista 平台不支持 AP1101 / AP1201H** <<<PAGE 15>>>
  "(Access Points from AP 12xx, 13xx,14xx and 15xxSeries) - AP1101, AP1201H models not supported"
  要点：老 AP1101 与 AP1201H 被明确排除，存量客户需先换 AP。
- **X6 新 OmniVista 平台交换机门槛 AOS 8.9R1** <<<PAGE 15>>>
  "Devices with minimum AOS release 8.9R1"
  要点：比 NetAdvisor 的 8.7R2 更高；老版本交换机需先升级。
- **X7 Stellar AP 需 AWOS 5.0.1MR 起** <<<PAGE 15>>>
  "OmniAccess Stellar WLAN Access Points (Access Points 15xx series) with minimum AWOS release 5.0.1MR"
  要点：网管平台对接 AP 的最低固件，低于此版本纳管受限。
- **X8 Terra 仅支持 VMware/Hyper-V，ESXi 最低 8** <<<PAGE 15>>>
  "Supported virtualization platform: VMware and Hyper-V / Minimum ESXi version: 8 / AVX/AVX2 instructions must be supported / Disk must be SSD/NVMe with at least 50MB/s rate"
  要点：KVM/Nutanix 等不在列；老 ESXi 6.x/7.x 不支持；磁盘必须是 SSD/NVMe。
- **X9 Terra 无 Flexible Pay，只能预付** <<<PAGE 16>>>
  "Flexible Pay with variable durations and payment terms is available only for OmniVista Cirrus."
  要点：Terra 只有 PrePaid/Upfront；期限 1/3/5/7 年（Cirrus 1/3/5 年）。
- **X10 Base 档不含设备硬件维保与设备支持** <<<PAGE 17>>>
  "Base Support (Excluding device hardware maintenance and node support access)"
  要点：Base 只保 OmniVista 软件本身；设备维保需另购或升 Business/Premium。
- **X11 Terra 客户软件升级需自访问 ALE 仓库** <<<PAGE 16>>>
  "OmniVista Terra is deployed and managed on the customer's premises. Customers can access the ALE repository to upgrade to the latest device software and firmware version."
  要点：Terra 无云自动推送，升级由客户自己从仓库拉取执行。
- **X12 Flexible Pay 不含设备硬件维保** <<<PAGE 19>>>
  "Not included: Device hardware maintenance and Support access plans (sold separately)"
  要点：OPEX 月付模式仅含 SaaS+升级+支持入口，硬件维保单卖。
- **X13 Flexible Pay 最短 12 个月** <<<PAGE 19>>>
  "Require Subscription Configuration for duration (min 12-to-60-month max)"
  要点：不支持短于一年的订阅。
- **X14 迁移工具能力因源系统而异** <<<PAGE 10>>>
  "functionality may vary depending on source system and version"
  要点：OV2500/Cirrus4 迁移并非全自动等价迁移，需评估差异。
- **X15 Fleet Supervision 故障换新需有效最终客户支持合同** <<<PAGE 6>>>
  "For customers with an active end-customer support contract"（脚注 1，对应 "Request faulty device replacements directly to streamline operations"）
  要点：无支持合同不能在线发起换新。

## frameworks

- **F1 OmniVista 管理产品代际与形态矩阵** <<<PAGE 9>>> / <<<PAGE 10>>>
  ```
                云端 SaaS                 本地 On-Prem
  上一代     OmniVista Cirrus 4        OmniVista 2500
  新一代     OmniVista Cirrus          OmniVista Terra
             （微服务/多租户/MSP）      （≤5000 设备/Active-Active L2/数据主权）
  伴随层     OmniVista Network Advisor（AI/ML 异常检测+修复，混合架构，p1）
  ```
  依据摘录 <<<PAGE 10>>>："migrating from OmniVista Cirrus 4 or OmniVista 2500... to the new platform"；<<<PAGE 9>>>："OmniVista Cirrus – Cloud-based... OmniVista Terra – On-Premises"。
- **F2 管理深度光谱：从免费盘点到 AI 自愈** <<<PAGE 5>>> / <<<PAGE 1>>> / <<<PAGE 9>>>
  ```
  免费资产可见 → 网管平台（配置/监控/NAC）→ AI 运维伴随 → 现场独立工具
  Fleet Supervision   OmniVista C/T        Network Advisor    Smart Tool
  （零成本,自助注册）  （订阅制全功能）      （异常检测/自动修复） （免云免CLI,OT专用）
  ```
  选型第一问：客户痛点在"看不见资产"、"管不住配置"、"修不过来告警"还是"现场没人会装"。
- **F3 订阅分档三轴模型（Cirrus/Terra 订购决策树）** <<<PAGE 16>>> / <<<PAGE 17>>> / <<<PAGE 19>>>
  ```
  轴1 形态：云 Cirrus（可 Flexible Pay）/ 本地 Terra（仅预付，多 7 年期选项）
  轴2 服务档：Base（软件支持）→ Business（+设备硬件维保 AVR）→ Premium（+最终客户直享支持）
  轴3 设备档：AP 分 APL（x0x/x1x/x2x）/ APH（x3x 及以上）；交换机按系列 63/64/65/68/69/99；
             Flexible Pay 分 Essential（AP+OS63/64/65） / Advanced（OS68 及以上）
  ```
- **F4 运维工具按"谁在用/在哪用"定位** <<<PAGE 2>>> / <<<PAGE 22>>> / <<<PAGE 7>>>
  ```
  IT 网络团队日常运维 → OmniVista 平台 + Network Advisor（Rainbow/Teams 伴随）
  安防/视频运维人员   → Milestone Plugin（在 VMS 界面内复位摄像机）
  OT 现场装维外包人员 → Smart Tool（手机/PC 直连交换机，免 CLI 免云）
  资产/合规经理       → Fleet Supervision（Web 仪表盘）
  ```
  同一网络可同时部署多工具，互不替代。
- **F5 ALE"订阅+设备合同"总拥有成本检查清单** <<<PAGE 16>>> / <<<PAGE 4>>> / <<<PAGE 3>>>
  ```
  1. 网管订阅本体（OVCX/OVTX 或 NETAD SKU）
  2. 设备级支持合同（Base 档与 Flexible Pay 均不含，需另购）
  3. 自备资源（NetAdvisor 虚拟机 8GB+/Terra 虚机 8vCPU/3TB）
  4. 版本升级预算（交换机 AOS 8.9R1+、AP AWOS 5.0.1MR+ 前置）
  5. 老设备淘汰（AP1101/AP1201H 不支持新平台）
  ```

## glossary

- **OmniVista Cirrus**：新一代云端网管平台，微服务架构，支持多租户/MSP <<<PAGE 9>>>
- **OmniVista Terra**：新一代本地部署网管，最多 5000 设备，VMware/Hyper-V 虚机 <<<PAGE 15>>>
- **OmniVista 2500**：上一代本地网管（本书仅目录级出现，迁移来源） <<<PAGE 10>>>
- **OmniVista Cirrus 4**：上一代云网管（迁移来源） <<<PAGE 10>>>
- **UPAM（Unified Policy Access Manager）**：内置 NAC 模块，认证/角色/访客/BYOD <<<PAGE 9>>>
- **QoE（Quality of Experience）**：用户体验质量指标：连接成功率、连接时长、漫游时间、覆盖 <<<PAGE 12>>>
- **AP-Group**：AP 管理实体，组内 AP 继承 SSID/ARP/RF 等全部配置 <<<PAGE 14>>>
- **Access Role Profile (ARP)**：设备接入角色模板（QoS/隧道/VLAN/带宽） <<<PAGE 14>>>
- **RF Profile**：射频配置模板（频段/信道/regulatory domain/关联速率） <<<PAGE 14>>>
- **Golden Configuration**：金标配置，用于配置比对与漂移审计 <<<PAGE 14>>>
- **DPI（Deep Packet Inspection）**：应用级深度包检测，交换机与 AP 均支持 <<<PAGE 14>>>
- **Heatmap**：Wi-Fi 覆盖/客户端密度热图，用于容量规划 <<<PAGE 13>>>
- **SPB（Shortest Path Bridging）**：最短路径桥接，Terra/Cirrus 提供图形化 fabric 视图 <<<PAGE 15>>>
- **Zero-Touch Provisioning**：AP 零触摸上线，免现场配置 <<<PAGE 10>>>
- **RADsec**：RADIUS over TLS，用户/设备认证加密 <<<PAGE 14>>>
- **MFA / 2FA**：多因子/双因子认证，网管登录保护 <<<PAGE 10>>>
- **SAML 2.0 SSO**：单点登录，支持 Okta 与 Microsoft Azure AD <<<PAGE 14>>>
- **GDPR / CCPA**：欧盟/加州数据隐私法规，Cirrus 数据中心合规 <<<PAGE 15>>>
- **SOC1 / SOC2**：数据中心安全审计认证 <<<PAGE 10>>>
- **NIS2**：欧盟网络安全指令，Fleet Supervision 支持合同合规检查场景 <<<PAGE 6>>>
- **Active-Active L2**：Terra 本地高可用模式 <<<PAGE 10>>>
- **MSP（Managed Service Provider）**：托管服务商，Cirrus 多租户顶层角色 <<<PAGE 15>>>

## 订阅 SKU 体系
- **OVCX-\*-BIZ/BAS/PRM-nY**：Cirrus 预付订阅（Base/Business/Premium，n=1/3/5 年） <<<PAGE 17>>>
- **OVTX-\*-BAS/BIZ/PRM-nY**：Terra 预付订阅（n=1/3/5/7 年） <<<PAGE 19>>>
- **OVCX-APL-***：低端 AP 订阅（AP1x0x/x1x/x2x） <<<PAGE 17>>>
- **OVCX-APH-***：高端 AP 订阅（AP1x3x/x4x/x5x/x6x/x7x） <<<PAGE 17>>>
- **OVC-C-ESS-M**：Cirrus Flexible Pay Essential 月度许可（AP+OS6360/6465/6560/6570M） <<<PAGE 19>>>
- **OVC-C-ADV-M**：Cirrus Flexible Pay Advanced 月度许可（OS6860/6865/6870/6900/9900 等） <<<PAGE 19>>>
- **NETAD-AP/SWITCH/TP-1Y/3Y/5Y**：Network Advisor 按设备类型订阅（AP/交换机/第三方） <<<PAGE 4>>>
- **AVR**：设备高级换新维护（Business/Premium 档包含） <<<PAGE 16>>>
- **Flexible Pay（OPEX mode）**：仅 Cirrus 可用的按月灵活付费模式 <<<PAGE 16>>>
- **NaaS（Network as a Service）**：网络即服务 Opex 运营模式 <<<PAGE 10>>>

## Network Advisor
- **OmniVista Network Advisor**：AI/ML 网络运维伴随工具，异常检测+一键/自动修复 <<<PAGE 1>>>
- **Rainbow CPaaS**：ALE 协作云平台，NetAdvisor 的 Bot/Bubble 交互载体 <<<PAGE 1>>>
- **Anomaly（异常）**：AI/ML 定义的偏离正常网络行为事件，可自定义 <<<PAGE 2>>>
- **Remediation**：修复动作，自动或用户发起 <<<PAGE 1>>>
- **Microsoft Teams support**：NetAdvisor 协作支持 Teams <<<PAGE 2>>>

## Fleet Supervision
- **Network Fleet Supervision**：免费在线资产与支持合规工具，自助注册 <<<PAGE 5>>>
- **End of Sales / End of Life**：停售/停维生命周期节点，用于换新预算规划 <<<PAGE 5>>>
- **Asset Collection**：资产采集，自动（多 OmniVista 系统）+手工导入序列号 <<<PAGE 6>>>

## Milestone Plugin
- **OmniSwitch Milestone Plugin**：与 Milestone VMS 集成的视频监控运维插件 <<<PAGE 7>>>
- **Milestone Systems VMS**：视频管理系统（第三方） <<<PAGE 7>>>
- **PoE priority per camera**：按摄像机设置 PoE 优先级，超预算保关键设备 <<<PAGE 8>>>

## Smart Tool
- **OST（OmniVista Smart Tool）**：OT/IoT 现场独立运维工具，免云免 CLI <<<PAGE 22>>>
- **PoE Wizard**：60 秒内诊断修复常见 PoE 问题的向导 <<<PAGE 23>>>
- **PoE Power Cycle**：一键 PoE 断电重启，保留人工确认 <<<PAGE 23>>>
- **TDR**：时域反射电缆健康测试 <<<PAGE 23>>>
- **Lightning Config**：OmniSwitch 首装配置向导 <<<PAGE 22>>>

## 版本/平台术语
- **AOS**：Alcatel-Lucent OmniSwitch 操作系统（NetAdvisor 要求 8.7R2+，新平台 8.9R1+） <<<PAGE 3>>> / <<<PAGE 15>>>
- **AWOS**：OmniAccess Stellar AP 无线操作系统（NetAdvisor 要求 4.0.3MR-3+，新平台 5.0.1MR+） <<<PAGE 3>>> / <<<PAGE 15>>>
- **ESXi**：VMware 虚拟化平台，Terra 要求版本 8+ <<<PAGE 15>>>
- **AVX/AVX2**：CPU 指令集，Terra 虚机硬性要求 <<<PAGE 15>>>

## principles

- **P1 Network Advisor 定位：AI/ML 运维伴随工具** <<<PAGE 1>>>
  "The Alcatel-Lucent OmniVista® Network Advisor is an intelligent and autonomous system, that provides real-time network monitoring and alerts for potential risks and network remediation." 摘录：`it provides the first brick in a new software service that includes Artificial Intelligence (AI)/Machine Learning (ML) developed and powered by ALE.`
  要点：NetAdvisor 是加在 OmniSwitch/OmniAccess Stellar 之上的运维伴随服务，非网管替代品。
- **P2 Network Advisor 三大能力：识别/缓解/优化** <<<PAGE 1>>>
  "Identify risks/issues that may otherwise decrease QoE... Mitigate network issues with fixes execution, with one tap or can be automatically carried out... Optimise the network, with fine tuning recommendations."
  要点：告警→一键或自动修复→调优建议，闭环。
- **P3 Network Advisor 混合架构** <<<PAGE 1>>>
  "The service combines hybrid processing, on premises and in the cloud, delivering a high performance and easily scalable solution."
  要点：本地+云混合处理，部署需自备虚拟机（见 X 条目）。
- **P4 Network Advisor 支持 3rd party 设备** <<<PAGE 1>>>
  "It can also interface with 3rd party devices able to send syslog."
  要点：非 ALE 设备也能纳入监控，走 syslog + 手工定制异常规则。
- **P5 NetAdvisor 设备版本门槛** <<<PAGE 3>>>
  "OS 6xxx and 9xxx models, AOS 8.7.R2 or Higher / Stellar APs, AWOS 4.0.3 MR-3 or Higher / OmniSwitch 2260 & 2360 models with minimum release AOS 5.1R1"
  要点：OS6xxx/9xxx 需 AOS 8.7R2+，Stellar AP 需 AWOS 4.0.3MR-3+，2260/2360 小交换机只需 AOS 5.1R1。
- **P6 NetAdvisor 容量：2000 设备** <<<PAGE 3>>>
  "2000 devices supported" 摘录：`For 1000 devices, 120 GB storage is recommended / For 2000 devices, 210 GB storage is recommended`
  要点：1000/2000 设备档位对应 120GB/210GB 存储。
- **P7 NetAdvisor 订阅 SKU 按 1/3/5 年** <<<PAGE 4>>>
  "NETAD-AP-1Y ... NETAD-SWITCH-1Y ... NETAD-TP-1Y"（AP/交换机/第三方设备三类，各 1/3/5 年）
  要点：按被管设备类型单台订阅；Support service 随许可包含。
- **P8 Fleet Supervision：免费自助注册** <<<PAGE 5>>>
  "Free of charge online tool - Self signup approach"
  要点：零成本资产管理入口，可作为销售切入点。
- **P9 Fleet Supervision 四大价值** <<<PAGE 5>>>
  "Take inventory of all OmniSwitch® and OmniAccess Stellar® devices... Track hardware lifecycle and plan budget for replacement (end of sales, end of life)... Check current software version and plan proactive updates... Streamline faulty device replacements"
  要点：资产盘点/生命周期/软件版本/故障换新四合一。
- **P10 Fleet Supervision 资产采集双模式** <<<PAGE 6>>>
  "Automatic asset inventory - Display devices managed by several OmniVista management systems / Manual option to import serial numbers for unmanaged devices or assets behind firewall"
  要点：自动采集多 OmniVista 系统 + 手工导入防火墙后设备序列号。
- **P11 Fleet Supervision 合规卖点：NIS2** <<<PAGE 6>>>
  "Verify your support contract status to ensure compliance with security regulations (e.g. NIS2)"
  要点：欧洲客户 NIS2 合规检查的抓手。
- **P12 Milestone Plugin 价值：远程处置摄像机故障** <<<PAGE 7>>>
  "This service assurance solution enables remote troubleshooting for common camera issues directly from the video surveillance management system. It allows the operations team to remotely reset out of service cameras and apply resolutions quickly."
  要点：省现场拜访，>90% 摄像机问题快速解决（见 p7 "Faster resolution for more than 90% of camera issues"）。
- **P13 Milestone Plugin 端口级 PoE 可视** <<<PAGE 8>>>
  "View camera status up/down on a per port basis, Power over Ethernet (PoE) consumed and Maximum PoE power available"
  要点：可按摄像机设置 PoE 优先级，超预算时保关键设备（p8 "Set PoE priority on a per camera basis"）。
- **P14 OmniVista 新平台双形态：Cirrus 云 / Terra 本地** <<<PAGE 9>>>
  "OmniVista Cirrus – Cloud-based deployment... native cloud-based microservices architecture. / OmniVista Terra – On-Premises: addresses stringent requirements for local infrastructure management, data sovereignty, and advanced security compliance."
  要点：云选 Cirrus，数据主权/本地合规选 Terra。
- **P15 内置 NAC：UPAM** <<<PAGE 9>>>
  "Unified Policies Access Manager (UPAM)—a Network Access Control (NAC) module offering enterprise-wide authentication, role-based management, guest access, and BYOD support."
  要点：网管自带 NAC，不必单独采购准入系统。
- **P16 迁移投资保护** <<<PAGE 10>>>
  "Minimal device reconfiguration when migrating from OmniVista Cirrus 4 or OmniVista 2500 with Alcatel-Lucent Enterprise devices to the new platform"
  要点：OV2500/Cirrus4 老用户迁新平台设备基本免重配。
- **P17 多站点 vs 多租户** <<<PAGE 10>>>
  "Multi-sites Management: OmniVista Cirrus & OmniVista Terra / Multi-tenancy: OmniVista Cirrus"
  要点：多组织/物理站点集中管理（MSP 场景）只有 Cirrus 支持；Terra 只有多站点。
- **P18 高可用架构差异** <<<PAGE 10>>>
  "Cloud: Hosted in multiple regional data centers with best-in-class availability... / On-Premises: High-availability for enhanced reliability with Active-Active L2"
  要点：云靠多区域数据中心+灾备；Terra 本地做 Active-Active L2。
- **P19 云安全：SOC1/SOC2 + MFA** <<<PAGE 10>>>
  "Software as a Service (SaaS) application hosted in SOC1 and SOC2 data centers... Multi-Factor Authentication (MFA) to secure network administration"
  要点：管理面与用户数据面分离，双向证书认证。
- **P20 Zero-Touch + 模板自动化** <<<PAGE 10>>>
  "Simplified devices onboarding process with Zero-Touch provisioning for OmniAccess Stellar access points and for OmniSwitch through template automation"
  要点：AP 零触摸、交换机模板化，分钟级上线免到现场。
- **P21 UPAM 认证源广泛** <<<PAGE 11>>>
  "Enterprise 802.1x authentication with internal or external sources including RADIUS, AD, LDAP, Microsoft Entra AD (Microsoft Azure AD)"
  要点：访客门户支持 email/SMS/社交登录（Facebook、Microsoft 365、Rainbow）。
- **P22 固件合规调度升级** <<<PAGE 11>>>
  "Device software version upgrade based on Scheduling, (best software version and AP group selection) reducing maintenance window"
  要点：按 AP 组选择最优版本、缩维护窗口。
- **P23 QoE 分析定位故障** <<<PAGE 12>>>
  "OmniVista QoE Analytics shows the quality experienced by the connected clients. Successful connects, time to connect, roaming time, coverage, and available capacity trends for problem identification (i.e., DHCP server down)"
  要点：连接成功率/时长/漫游时间等指标直指 DHCP/DNS/认证类故障。
- **P24 热图与容量规划** <<<PAGE 13>>>
  "OmniVista Cirrus Heatmaps help IT identify areas with poor WLAN coverage or high client density. This information is valuable for capacity planning"
  要点：覆盖热图+密度热图支撑无线容量规划，含客户端定位。
- **P25 Cirrus 配置模型：SSID/ARP/RF/AP-Group 四类 Profile** <<<PAGE 14>>>
  "SSID profile has all the information related to SSID... Access Role Profiles (ARP)... Radio-Frequency (RF) profiles... AP-Group profile is the management entity for a set of APs... All APs in the same group will inherit the AP-Group configuration"
  要点：AP-Group 是继承根，新 AP 入组即继承全部配置。
- **P26 Golden Config 合规比对** <<<PAGE 14>>>
  "Golden configuration allowing maximum compliance for comparison between different versions. Compare configuration, visualize configuration drift for Audit and 'out of the compliance' remediation"
  要点：金标配置+漂移可视化，用于审计与纠偏；含计划备份恢复。
- **P27 SPB 服务管理与拓扑** <<<PAGE 14>>> / <<<PAGE 15>>>
  "Provides SPB service configuration and management via the Service Manager" + "SPB topology feature provides a real-time, graphical view of the SPB fabric, allowing operators to visualize shortest paths, services, and fabric health"
  要点：新平台深度纳管 SPB（最短路径桥接） fabric。
- **P28 开放 API + 第三方集成** <<<PAGE 15>>>
  "OmniVista Cirrus is built as a native API platform... The authenticated and encrypted API is open and stable" + "Integrates and monitors Celona Private 5G access points."
  要点：全 API 化可自动化；可纳管 Celona 5G 小站。
- **P29 Cirrus 多租户层级模型（MSP）** <<<PAGE 15>>>
  "The multi-tenancy model operates under a hierarchical model, with Managed Service Provider on top, managing the different tenants and organization and sites structure"
  要点：MSP 顶层→租户→站点层级，RBAC 按站点。
- **P30 GDPR/CCPA 合规** <<<PAGE 15>>>
  "Compliant with General Data Protection Regulation (GDPR) and California Consumer Privacy Act (CCPA)"
  要点：区域数据中心托管，数据合规双认证。
- **P31 Terra 容量：5000 设备 / 1-3 虚机** <<<PAGE 15>>>
  "It enables unified LAN and WLAN management for up to 5,000 devices (Wi-Fi switches and access points)... Scales from one to three virtual machines according to the number of managed devices."
  要点：每虚机推荐 8 vCPU/32GB RAM/200GB 系统盘/3TB 数据盘，ESXi 8+，需 AVX/AVX2、SSD/NVMe ≥50MB/s。
- **P32 订阅模式差异** <<<PAGE 16>>>
  "Flexible Pay with variable durations and payment terms is available only for OmniVista Cirrus." 摘录：Cirrus 1/3/5 年；Terra 1/3/5/7 年。
  要点：只有 Cirrus 有 Flexible Pay（OPEX 按月等）；Terra 只能预付。
- **P33 Cirrus 三档服务分级覆盖范围递增** <<<PAGE 16>>>
  "Base → ALE Business Partner support for OmniVista software / Business → ALE Partner Support Plus for all managed devices (inc. Hardware maintenance, AVR and Advanced replacement) / Premium → End Customer Access support"
  要点：Base 只保软件、Business 加硬件维保（含 AVR）、Premium 最终客户直享支持。
- **P34 AP 高低端分档定价（APL/APH）** <<<PAGE 17>>>
  "Covers Low end OmniAccess Stellar AP models AP1x0x, AP1x1x, AP1x2x" vs "Covers High end OmniAccess Stellar AP models AP1x3x, AP1x4x, AP1x5x, AP1x6x and AP1x7x"
  要点：订阅 SKU 按末位数字分档：x0x/x1x/x2x 低端，x3x 及以上高端。
- **P35 Flexible Pay 设备分档：Essential vs Advanced** <<<PAGE 19>>>
  "Essential: OmniAccess Stellar Access Points, OS6360, OS6465, OS6560, OS6570M series / Advanced: OS6860, OS6860E, OS6860N, OS6860P, OS6865, OS6870, OS6900, OS9900 series"
  要点：接入级交换机归 Essential，核心级归 Advanced；12-60 月按月计价。
- **P36 Smart Tool 定位：免云免 CLI 的现场工具** <<<PAGE 22>>>
  "A standalone, cloud-independent field utility... install and troubleshoot device connectivity without relying on CLI tools, cloud dashboards, or advanced networking expertise."
  要点：面向 OT 环境受限云连接场景，装维人员零网络背景可用。
- **P37 Smart Tool PoE 向导 60 秒诊断** <<<PAGE 23>>>
  "Diagnoses and repairs common PoE issues in under 60 seconds" + "One-button PoE Power Cycle... keeping a human in the loop for accountability in high-assurance markets such as correctional facilities, casinos, and banks."
  要点：一键 PoE 断电重启保留人工确认，满足监狱/赌场/银行高保证场景。
- **P38 Smart Tool 核心功能四件套** <<<PAGE 23>>>
  "Ethernet cable health testing (TDR) / Per-port device discovery and power visibility (LLDP) / Secure configuration wizards for rapid setup / No CLI dependency during installation"
  要点：TDR 线缆健康测试是差异化能力，摄像头问题多为电力/布线类（"Most physical security problems are power or cabling related"）。
