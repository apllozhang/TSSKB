# principles — bp-nms-brochures（NMS/网管工具选型速查）

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
