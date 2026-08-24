# principles 候选 — DT00XTE317 OmniVista Cirrus/Terra Deployment and Configuration

## P1. Cirrus vs Terra 产品定位差异（云 SaaS vs 本地部署）
- 页码：<<<PAGE 5>>><<<PAGE 13>>><<<PAGE 14>>>
- 原文摘录：Cirrus："Software as a Service (SaaS) model … Zero Deployment"（p5）；Terra："On-Premises customer hosted … Virtualized infrastructure – cluster of VMs • Single tenant"（p13-14）。

## P2. 容量差异：Cirrus 12000 台 vs Terra 2000 台
- 页码：<<<PAGE 6>>><<<PAGE 14>>>
- 原文摘录：Cirrus "Up to 12.000 Network devices supported • 10.000 Access Points + 2.000 OmniSwitches"（p6）；Terra "Up to 2.000 Network devices supported • Up to 1.600 Stellar APs and 400 OmniSwitches"（p14）。

## P3. Terra 功能与 Cirrus 对等（parity）+ 相同商业结构
- 页码：<<<PAGE 14>>><<<PAGE 17>>>
- 原文摘录："Features parity with OmniVista Cirrus … Same commercial structure than OVCX … Consistent User Interface & Experience"（p17）。

## P4. Terra 高层架构：3 VM 组成 Kubernetes 集群
- 页码：<<<PAGE 17>>><<<PAGE 75>>>
- 原文摘录："A virtualized environment supporting: VMware environment … Multi-servers for high availability & scalability • High availability: Active-Active L3 … Kubernetes cluster … OmniVista Terra VM/Server ×3 … VPN Server / Load balancer … Kafka / MQTT … HTTPS"（p17）。

## P5. Terra VM 硬件要求
- 页码：<<<PAGE 75>>>
- 原文摘录："Number of Virtual Machines required: 3 • Minimum EXSi version: 8 • Processors: 8 vCPU @3GHz minimum • CPU must support AVX/AVX2 … EVC mode … 'Ice Lake' … As a minimum requirement, the 'Broadwell' baseline may be used • RAM: 32 GB • Disk type: SSD (Minimum 50MB/s) • System Disk: 200 GB • Data Disk: 3 TB"

## P6. 网络前置条件：Cirrus 与 Terra 的防火墙端口差异
- 页码：<<<PAGE 9>>><<<PAGE 18>>><<<PAGE 140>>>
- 原文摘录：Cirrus 需开放 9093/30123/30124/30125（AP→云）+ 出向 443/80/123/53；Terra 只需出向 443/80/123/53；DHCP 标准 options 1,3,6,28,42,43，代理时加 129-133,138；至少 1 个 NTP 服务器。

## P7. 设备软件版本前置：Cirrus 与 Terra 不同
- 页码：<<<PAGE 9>>><<<PAGE 18>>>
- 原文摘录：Stellar AP：Cirrus 要求 "AWOS 4.0.6 GA or higher"，Terra 要求 "AWOS 4.0.7.14 or higher"；OmniSwitch：Cirrus "AOS 8.9R1 or higher"，Terra "AOS 8.9.82R01 or higher"；不支持 AP1101、AP1201L/H/HL。

## P8. License SKU 编码模型（OVCX-68-BAS-3Y）
- 页码：<<<PAGE 23>>><<<PAGE 95>>>
- 原文摘录："OVCX-68-BAS-3Y … License level: BASE(BAS)/BUSINESS(BIZ)/PREMIUM(PRM) … duration: 1Y/3Y/5Y（Terra 另有 7Y）… category: APL（低端 AP1x0x/1x1x/1x2x）/APH/63/64/65/68/69/99"。

## P9. Terra 组织自动 90 天 Trial
- 页码：<<<PAGE 110>>>
- 原文摘录："The organization is automatically activated: In trial mode, for 90 days."

## P10. Terra 激活 License 时开启倒计时
- 页码：<<<PAGE 101>>>
- 原文摘录："Enabling the option 'Activate subscription' will start the countdown of your license."

## P11. eBuy→Subscription Manager 24 小时延迟
- 页码：<<<PAGE 26>>><<<PAGE 98>>>
- 原文摘录："The licenses purchased in eBuy can take up to 24h before coming up in Subscription Manager."

## P12. 单邮箱单 MSP 门户限制与子地址法（Sub-addressing）
- 页码：<<<PAGE 49>>>
- 原文摘录："In OVC 10.4.3, a unique account (linked to a mail address) can only be assigned to one MSP portal … Sub-addressing (MyMail+[subaddress]@MyCompany.com) … Activation links, upon account creation, are sent to the original mail address."

## P13. MSP 级用户三种权限：Admin/Viewer/Limited
- 页码：<<<PAGE 50>>><<<PAGE 130>>>
- 原文摘录："An MSP user has the access rights • Admin • Viewer • Limited"；组织级用户权限可"globally"或"per organization"设置（p132）。

## P14. Device Catalog 激活状态机（正常链）
- 页码：<<<PAGE 146>>><<<PAGE 147>>><<<PAGE 166>>><<<PAGE 167>>>
- 原文摘录：中间态 Registered → Obtaining Certificate → Upgrade/Upgrading → Assigned → VPN Configuring → Connected to OV；"Expected Activation Status … Up to 5 minutes"；期望终态 "OV Managed: Device is ready for full management"；状态含 "Waiting for first contact / Certificate Previously Issued / Provisioning / Unsupported Device Model" 等（p147 详细定义）。

## P15. 激活失败状态集合
- 页码：<<<PAGE 146>>><<<PAGE 147>>>
- 原文摘录："Activation Status failures: Failed To Get Certificate / Upgrade Failed / Configuring VPN Failed / Provisioning Failed / Device Validation Failed / Factory Reset Required"；"Factory Reset required: The VPN profile was changed/updated. A Factory Reset is required on the device."

## P16. 证书与 VPN 通道的激活原理
- 页码：<<<PAGE 147>>>
- 原文摘录："Obtaining Certificate: Device has contacted the OmniVista Cirrus server, and the server is creating a digital certificate that is used in creating the secure VPN channel between your device and the OmniVista Cirrus server."

## P17. AP Group 概念与规模
- 页码：<<<PAGE 152>>>
- 原文摘录："Multiple APs in the same AP Group, sharing the same configuration • Mix of any AP type & total number of AP up to 20000 • Not dependent of physical network"。

## P18. Provisioning Configuration 必填四要素
- 页码：<<<PAGE 154>>>
- 原文摘录："Mandatory Provisioning Configuration: Name / Site / RF Profile / Timezone"；配置范围含 SSH Login、AP Web、证书、SNMP、IoT Radio、Syslog(最多4) 等。

## P19. 交换机激活 cloud-agent 机制
- 页码：<<<PAGE 171>>><<<PAGE 172>>><<<PAGE 170>>>
- 原文摘录："cloud-agent admin-state enable/disable … cloud-agent discovery-interval … default= 30mns"；`show cloud-agent status` 显示 Activation Server State: completeOK、Device State: DeviceManaged 等；重激活=重启 cloud-agent 进程或手动重启设备。

## P20. SSID Usage 预定义模板模型
- 页码：<<<PAGE 214>>><<<PAGE 218>>>
- 原文摘录："Wizard driven tool. Selection of Pre-defined Usage (Guest, Employee, BYOD,…) … Each usage leads to a predefined template"；Guest=Open/MAC+Captive Portal、Protected Network=PSK、Enterprise=802.1X 等映射表（p218）。

## P21. 认证安全等级模型
- 页码：<<<PAGE 215>>>
- 原文摘录：Open+CP（无安全）→ MAC 认证（可伪造、无加密）→ WPA2/WPA3 Personal PSK（共享密钥）→ WPA2/WPA3 Enterprise 802.1X（最强）。

## P22. DSPSK / PPSK / Dynamic Private Group PSK 原理
- 页码：<<<PAGE 231>>><<<PAGE 233>>><<<PAGE 234>>><<<PAGE 235>>>
- 原文摘录：DSPSK="In the Company property database, a specific PSK pass phrase is assigned to the MAC address"（Force/Prefer 两种）；PPSK=多个 passphrase 各绑 ARP；Dynamic PGPSK="Each entry is linked to a VLAN ID and ARP … No need to create as many ARP as VLANs"，可选 Priority ARP over VLAN-ID 或反之。

## P23. UPAM 组成：内置 RADIUS + MAC 认证服务器
- 页码：<<<PAGE 240>>><<<PAGE 242>>><<<PAGE 243>>>
- 原文摘录："UPAM consists of Guest Access • BYOD Access • A built-in RADIUS Server • A built-in MAC Authentication Server"；认证源：Internal RADIUS/外部 RADIUS/IMSI-IMEI(Celona)/Azure AD。

## P24. Guest Tunneling：L2 GRE 隧道
- 页码：<<<PAGE 256>>>
- 原文摘录："Tunnel per Access Role Profile from Access Point to a switch/router/controller. • L2 GRE tunnel over L2/L3 networks • OmniSwitch simplifies deployment with automatic tunnel creation to AP IP • GRE Backup tunnel can be added for resiliency."

## P25. 带宽控制三层模型与判定顺序
- 页码：<<<PAGE 268>>><<<PAGE 269>>>
- 原文摘录：SSID 级（per SSID per AP 共享）→ ARP 级（per user）→ Policy List ACL/QoS 规则级；p269 给出判定流程图（匹配 ACL→按规则限速，否则按 ARP，再否则按 SSID）。

## P26. Policy List 双向执行
- 页码：<<<PAGE 264>>>
- 原文摘录："Policy List • List of Policy Rules (QoS, ACLs) … Enforcement is bidirectional"；分配来源 RADIUS（账号）或 ARP（Default Policy List）。

## P27. Registration Profile 配额与耗尽处理
- 页码：<<<PAGE 283>>><<<PAGE 284>>>
- 原文摘录："Data Quota: Max data traffic allowed per guest (in MB) • Time Quota per day (in hours)… Exhaustion Handling: Block for remaining Duration (Redirection URL) / Reduced up/down bandwidth (in kB/s)"。

## P28. QoE 分析指标与失败原因分类
- 页码：<<<PAGE 296>>><<<PAGE 297>>>
- 原文摘录：连接时间/漫游时间（失败原因 Association/Authorization/DHCP/Portal）、平均 RSSI（Weak Signal/Asymmetry）、信道利用率（干扰/客户端数）、设备平均 uptime。

## P29. DRM 分布式射频管理架构
- 页码：<<<PAGE 364>>><<<PAGE 365>>>
- 原文摘录："Fully distributed control Plane • Each AP communicates with its neighbor APs … Over the air protocol: neighbor AP discovery … Over the LAN protocol: RF management … Each AP can take RF action … Limited to neighbor APs • Does not rely on AP Group or AP management vlan"；RF Profile 应用于 AP Group 或 AP 级。

## P30. Smart Load Balance：Band Steering 与 Dynamic Load Balance
- 页码：<<<PAGE 370>>><<<PAGE 371>>><<<PAGE 372>>>
- 原文摘录："Band Steering: Steer client to 2.4/5/6GHz … Recommended value: 2.4G = 5, 5G = 10（RSSI）"；"Overloaded: A channel is considered overloaded when its average medium utilization over the span of a minute exceeds 70%"（p371）；DLB：各 AP 基于自身负载设 timer，新客户端被引导至最轻负载 AP（p372）。

## P31. 背景扫描机制与参数
- 页码：<<<PAGE 373>>>
- 原文摘录："Each radio periodically scans the air – One channel at the time • During scanning wireless clients are impacted – no 802.11 data • Scanning is required for WIPS • Default interval = 20 sec – Range = 5-10800 sec • Default Duration = 50 ms – Range = 50-110 ms"；支持 Dedicated AP scanning mode 与 Voice/Video Awareness（检测 SIP/H.323 绕过扫描）。

## P32. RSSI 定义与数值对照
- 页码：<<<PAGE 378>>><<<PAGE 379>>>
- 原文摘录："How well a device can hear a signal from an access point … Average on OmniVista Cirrus 10 • Instant on the Stellar Access Point"；RSSI 10≈-86dBm（Bad）… 25≈-71dBm（Desired and recommended）；AP CLI：`wlanconfig ath002 list`，-24dBm = 72 RSSI。

## P33. WIPS 分类：Interfering/Rogue/Friendly
- 页码：<<<PAGE 384>>><<<PAGE 385>>>
- 原文摘录："Interfering AP: Any other APs discovered over the air … Rogue AP: Based on the Rogue AP Policy … Rogue AP Containment – enabled by default … sends de-auth request"；Rogue 判定策略：Signal Strength Threshold（默认 -70dBm，范围 -50~-90）、Detect Valid SSID、Rogue SSID Keyword（黑名单）、Rogue OUI。

## P34. 漫游判定条件（L2/L3 选择）
- 页码：<<<PAGE 400>>><<<PAGE 394>>>
- 原文摘录："L2 or L3 Roaming selection based on the client VLAN between 'home' and 'foreign' AP … L3 Roaming based on L2 GRE tunnel"；三条件判定表：无上下文→新客户端；上下文+ WLAN/ARP 匹配 + VLAN 匹配→L2；VLAN 不匹配→L3。

## P35. 客户端上下文共享机制（Add/Del）
- 页码：<<<PAGE 397>>><<<PAGE 399>>>
- 原文摘录："Each AP learns about its 'over-the-air' adjacent APs … No dependency on AP Groups and Management VLAN … On Client Association, AP sends a Add message to all adjacent APs … Upon Roaming, Del Message triggered on the 'old' AP upon Add Message from the 'new' AP"；上下文含 VLAN ID/ARP/Policy List/PMKSA cache 等。

## P36. Fast Roaming 条件限制
- 页码：<<<PAGE 395>>><<<PAGE 402>>>
- 原文摘录："L2 Roaming always enabled • L3 Roaming disabled by default … OKC can be enabled with WPA2/WPA3 Enterprise only • 802.11r (Fast Roaming) can be enabled with WPA2/WPA3 encryption only (Personal or Enterprise)"；OKC=802.11k 优化漫游目标列表，802.11r 用 FT 快速认证。

## P37. Sticky Client Avoidance 与 Roaming RSSI 阈值
- 页码：<<<PAGE 404>>><<<PAGE 416>>>
- 原文摘录："802.11v (BSS Transition Management) … 802.11k … Roaming RSSI … Recommended value for 2.4GHz: RSSI = 10 … 5GHz: RSSI = 15"；阈值过低→客户端滞留弱信号，过高→频繁漫游丢包。

## P38. Mesh 拓扑限制
- 页码：<<<PAGE 439>>>
- 原文摘录："UP TO 8 SLAVE APS • UP TO 4 HOPS • UP TO 5 APS IN A SINGLE HOP … UP TO 16 APS IN THE MESH NETWORK • ALL APS CAN BROADCAST UP TO 5 SSIDS FOR CLIENTS"；最佳实践 BAND 5GHz、CHANNEL > 100。

## P39. Auto Mesh 机制
- 页码：<<<PAGE 440>>>
- 原文摘录：连 LAN 且配置为 Mesh root 的 AP 广播隐藏 SSID "Stellar-MESH"（5GHz）；未连 LAN 的 AP 自动以 non-root 加入 Mesh。

## P40. IoT 设备识别原理
- 页码：<<<PAGE 464>>><<<PAGE 465>>>
- 原文摘录："MAC OUI: allows devices to be recognized by identifying their MAC addresses. • DHCP FingerPrinting"；基于 DHCP option 55（参数请求列表）与 option 60（厂商标识）；流程=Collect from End Points → Profile & Inventory → Enforcement（按设备类别映射 ARP）。

## P41. VLAN Pooling 原理
- 页码：<<<PAGE 224>>>
- 原文摘录："VLAN Pooling: Pool of VLAN assigned to the SSID (up to 256) • Avoid large broadcast domain with a single VLAN."

## P42. Golden Configuration 合规检查
- 页码：<<<PAGE 195>>><<<PAGE 196>>><<<PAGE 351>>>
- 原文摘录："A Golden Configuration is a backup that can be used to restore the configuration of a switch if it changes unexpectedly"（p195）；"Status is Compliant if there are no deviations"（p196）；支持周期审计与即时审计（p351）。

## P43. Terra DNS 四域名映射
- 页码：<<<PAGE 90>>>
- 原文摘录："activation.myovterra.com / as.myovterra.com – activation server URL (Main IP) • vpn.myovterra.com – VPN (VPN IP) • images.myovterra.com – Image Server URL (Main IP) • myovterra.myovcloud.com – main URL (Main IP)"。
