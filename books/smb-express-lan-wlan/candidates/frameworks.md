# frameworks 候选 — DT00XTE310 OmniSwitch LAN Access & OmniAccess Stellar WLAN Express

> 每条含页码引用 <<<PAGE N>>> 与原文摘录。宁缺毋滥，共 12 条。

## F1. Stellar AP 部署模式自动选择决策流程（Express / Enterprise / Cloud）
- 页码：<<<PAGE 201>>>（同 <<<PAGE 264>>>）
- 原文摘录："DHCP REQUEST → IF DHCP SERVER SENDS OFFER WITH OPTION 138 = YES (IP@ OF OV2500) → AP REGISTERS AND RETRIEVES ITS CONFIGURATION FROM OV2500 … IF AP REGISTERED IN OV CIRRUS (MAC/SN) = YES → AP RETRIEVES ITS CONFIGURATION FROM OV CIRRUS … IF AP REGISTERED IN OV CIRRUS (MAC/SN) = NO → AP BOOTS IN EXPRESS MODE"
- 要点：AP 上电后按"DHCP option 138（OV2500）→ Cirrus 注册（MAC/序列号）→ 都没有则 Express"三级判定自动进入对应管理模式。这是三模式选型的核心技术逻辑。

## F2. 三模式定位与规模决策（Express ≤255 / Enterprise ≤4000 / Cloud ≤10000）
- 页码：<<<PAGE 188>>>、<<<PAGE 190>>>、<<<PAGE 192>>>、<<<PAGE 198>>>
- 原文摘录：Express "Self-managed standalone cluster • Up to 255 APs … No license required"（<<<PAGE 188>>>/<<<PAGE 199>>>）；Enterprise "Centralized management via the OmniVista 2500 NMS • Up to 4000 APs"（<<<PAGE 190>>>）；Cloud "Centralized management via the cloud platform OmniVista Cirrus NMS • Up to 10000 APs"（<<<PAGE 192>>>）；"Wi-Fi Express Standalone mode / Wi-Fi Enterprise In Premise Managed mode with OmniVista 2500 NMS / Wi-Fi Cloud Cloud based"（<<<PAGE 198>>>）
- 要点：SMB 用 Express（免许可证），本地集中管理用 Enterprise，混合/云管最大规模用 Cloud。

## F3. Voice over WLAN 五阶段部署方法论（Prepare→Plan→Design→Implement→Operate）
- 页码：<<<PAGE 252>>>
- 原文摘录："Identify the Voice usages: understand the challenges and requirements → Prepare / Plan / Design / Implement / Operate … These are the major steps for the deployment of VoWLAN in a WLAN Stellar environment."
- 要点：与附录部署指南（<<<PAGE 964>>> "Prepare – identify Voice and Audio/Video usages … Operate – provide the Voice service to users, monitor… maintain and extend the service"）一致，是全书语音 WLAN 主线框架。

## F4. VoWLAN Preparation 阶段工作框架（现场勘测 + RF 环境 + AP 密度）
- 页码：<<<PAGE 253>>>
- 原文摘录："Requirements: What are the voice coverage requirements? … Actions: Site survey • Analyze the RF environment • Discover the source of interferences … 1 access point / 255 m² … Number of users per AP – Average of 20-25 users"
- 要点：语音覆盖以 -60/-70dBm 小区交叠设计，办公区 1 AP/225-255 m²、每 AP 20-25 用户为基准容量规划法。

## F5. AOS R8 双分区配置管理流程（working/certified/user-defined + running-directory 状态机）
- 页码：<<<PAGE 85>>>、<<<PAGE 88>>>-<<<PAGE 91>>>、<<<PAGE 126>>>-<<<PAGE 131>>>
- 原文摘录："Rollback Based on the working, certified and User-defined directories"（<<<PAGE 85>>>）；"sw7 (OS6860-A) -> write memory flash-synchro = write memory + copy running certified"（<<<PAGE 89>>>）；"When the switch boots from the CERTIFIED directory, changes made to the switch cannot be saved"（<<<PAGE 91>>>）；"reload all" 强制从 certified 启动（<<<PAGE 126>>> WARNING）
- 要点：write memory（running→working）、copy running certified（认证）、write memory flash-synchro（三合一）、modify running-directory（切换运行目录）构成完整配置保存/回滚流程。

## F6. AOS 配置备份与恢复流程（configuration_backup.tar + USB 备份）
- 页码：<<<PAGE 92>>>、<<<PAGE 93>>>、<<<PAGE 132>>>-<<<PAGE 133>>>
- 原文摘录："The configuration backup command creates a .tar file where are stored the collected files … placed in /flash/config-backup-recovery folder … Up to 10 .tar files"（<<<PAGE 92>>>）；"usb backup admin-state {enable | disable} … If USB backup is enabled, switch will store image files, power supply and system configuration files to USB storage automatically upon user commands 'write memory' or 'copy running-certified'"（<<<PAGE 93>>>）
- 要点：内置备份（banner+userTable+vcboot.cfg 打 tar）与 USB 自动备份/恢复两条路径。

## F7. OmniVista Cirrus Cloud 模式上线流程（许可证→订阅→组织→站点→设备宣告→激活）
- 页码：<<<PAGE 285>>>-<<<PAGE 315>>>、<<<PAGE 272>>>
- 原文摘录：License 参考示例 "OVCX-68-BAS-3Y … BASE level: BAS … 3 years: 3Y"（<<<PAGE 285>>>）；"eBuy → OVC Subscription Manager → OmniVista CIRRUS 导入 Subscription ID + Activation Code"（<<<PAGE 286>>>-<<<PAGE 312>>>）；配置步骤 "DECLARE THE AP IN THE OMNIVISTA CIRRUS (SERIAL NUMBER| QR CODE | XLS) → [OPTIONAL] ASSIGN AN AP GROUP → PERFORM CONFIGURATION → CHECK THAT THE AP APPEARS ('OV MANAGED')"（<<<PAGE 272>>>）
- 要点：云管部署的完整序列：买许可→建订阅→建组织/站点→宣告 SN→AP call home→状态变 OV Managed。

## F8. Cirrus 设备激活状态机（Waiting for first contact → … → OV Managed）
- 页码：<<<PAGE 327>>>-<<<PAGE 328>>>
- 原文摘录："Intermediate Status: Registered / Obtaining Certificate / Upgrade / Upgrading / Assigned / VPN Configuring / Connected to OV → Expected Activation Status … Activation Status failures: Failed To Get Certificate, Upgrade Failed, Configuring VPN Failed, Provisioning Failed, Device Validation Failed, Factory Reset Required"
- 要点：交换机/AP 上云的排障依据：每一步中间态与失败态都有明确定义（含 Factory Reset Required 表示 VPN profile 变更需恢复出厂）。

## F9. SSID 创建五步向导框架（General → Auth Strategy → Access Policy → Default VLAN/Network → Assignment & Schedule）
- 页码：<<<PAGE 383>>>、<<<PAGE 390>>>（员工）、<<<PAGE 423>>>、<<<PAGE 431>>>（访客）
- 原文摘录："WI-FI NETWORK (SSID) CREATION STEPS • GENERAL SETTINGS • AUTHENTICATION • ACCESS POLICY • DEFAULT VLAN | NETWORK • ASSIGNMENT & SCHEDULE"（<<<PAGE 383>>>）；访客增加 "GUESTS ACCESS STRATEGY（Portal Page / Login By / Social Login / Self-Registration）"（<<<PAGE 427>>>）
- 要点：员工 SSID 与访客 SSID 共用五步向导框架，访客多出 Captive Portal 定制步骤。

## F10. ARP（Access Role Profile）优先级裁决框架
- 页码：<<<PAGE 394>>>、<<<PAGE 400>>>-<<<PAGE 403>>>
- 原文摘录："ARP = Access Role Profile → VLAN TAG / QOS POLICY / FIREWALL RULES (ACLS) / L7 APPLICATION RULES / LOCATION / PERIOD"（<<<PAGE 394>>>）；"ARP COMING FROM EXTERNAL SOURCE OR INTERNAL DATABASE > IF NO ARP … THEN ARP CONFIGURED IN THE AUTHENTICATION STRATEGY IS APPLIED > IF NO … THEN THE DEFAULT ARP IS APPLIED"（<<<PAGE 400>>>）
- 要点：外部 RADIUS/LDAP Filter-ID > 认证策略内 ARP > SSID 默认 ARP（__SSIDname）的三级优先级。

## F11. OmniSwitch 软件镜像升级流程（下载→FTP→reload from working→验证→certify→uboot/FPGA）
- 页码：<<<PAGE 1013>>>-<<<PAGE 1017>>>
- 原文摘录："Analyse Requirements on the release note → FTP the Upgrade Files to the Switch → Upgrade the image file → Verify the Software Upgrade → Certify the Software Upgrade → Upgrade uboot and/or FPGA if mandatory"；"-> update uboot cmm all file u-boot.8.4.1.R03.141.tar.gz … -> copy running certified"（<<<PAGE 1017>>>）
- 要点：升级先看 release note 的内存/UBoot/FPGA 要求，验证无误后 certify；出问题可回滚到先前 certified 版本。

## F12. Stellar 分布式控制架构下的 AP Group/PVM-SVM 选举与主备倒换框架
- 页码：<<<PAGE 204>>>-<<<PAGE 207>>>、<<<PAGE 270>>>
- 原文摘录："OmniAccess Stellar Access Points with the same group identifier (Group ID) and the same VLAN are automatically placed in the same group (AP Group) … a Stellar AP is elected PVM (Primary Virtual Controller) … another Stellar AP is elected SVM … Criteria 1 : highest Stellar AP model / Criteria 2 : highest MAC address"（<<<PAGE 205>>>-<<<PAGE 206>>>）
- 要点：出厂 Group ID=100/VLAN 1 自动成组；PVM/SVM 按型号、MAC 选举，从 PVM Web 统一管理全组（建 SSID、备份、升级）。
