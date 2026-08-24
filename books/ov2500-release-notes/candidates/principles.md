# principles · OV 2500 NMS 4.9R2 Release Notes（93 页，Part No. 033792-10 Rev. C，2025-09）

> 提取范围：4.9R2 新特性（p6-9）、软硬件兼容性矩阵（p6、p10-14）、系统要求与升级路径规则（p13-23）。
> 页码为 fulltext.md 中 <<<PAGE N>>> 标记的 PDF 页号。

- id: p01
  title: 部署形态与虚拟化平台支持
  type: principle
  source_chapter: "p5"
  source_quote: |
    OmniVista 2500 NMS 4.9R2 is installed as a Virtual Appliance, and can be deployed on the following hypervisors: Vmware ESXi 6.5, 6.7. 7.0.2, 8.0; MS Hyper-V: 2012 R2, 2016, 2019, and 2022; MS Hyper-V on Windows 10 Professional; Linux KVM/Ubuntu 22.04
  summary: |
    OV 2500 NMS 4.9R2 以虚拟设备（VA）形式交付，不是物理机安装。支持四类 hypervisor：VMware ESXi 6.5/6.7/7.0.2/8.0、Microsoft Hyper-V 2012R2/2016/2019/2022、Windows 10 专业版上的 Hyper-V、Linux KVM（Ubuntu 22.04）。做升级评估时先确认现有虚拟化平台在列表内。
  tags: [部署, hypervisor, 兼容性, ESXi, Hyper-V, KVM]

- id: p02
  title: 4.9R2 新增软硬件版本支持与认证固件矩阵
  type: principle
  source_chapter: "p6, p13-14"
  source_quote: |
    The following new switch models are now supported: OS6870 ... AOS 5.2R7 – OmniVista 2500 NMS now supports AOS 5.2R7 for the OS2260 and OS2360 Series Switches. AOS 8.9R4 MR ... AOS 8.10R2 ... AOS 8.10R3 ... AWOS 5.0.2 – OmniVista 2500 NMS now supports AWOS 5.0.2 on all previously supported Stellar APs.
  summary: |
    新增支持：交换机 OS6870；AOS 5.2R7（OS2260/OS2360）、AOS 8.9R4 MR、8.10R2、8.10R3（所有已支持 AOS 交换机）；AWOS 5.0.2（所有已支持 Stellar AP）。认证固件矩阵（p13-14）：OS2260/2360=5.2R5-R7；OS6350/6450=6.7.2.R06-R08；OS6360/6465/6560/6570M/6860E/6860N/6865=8.9R4/8.10R2/8.10R3；OS6870=仅 8.10R2/R3（无 8.9R4）；OS6900-X20/X40/T20/T40/Q32/X72=仅 8.9R4；OS6900-V72 等其余型号与 OS9907/9912=8.9R4/8.10R2/8.10R3。OAW-4030/4604/4704/4x50=OAW 6.5.1/6.5.4；IAP-105/205/225/325/335=6.5.4/8.3.0。Stellar AP 推荐 AWOS 5.0.2。
  tags: [兼容性, 固件版本, AOS, AWOS, OS6870, 升级评估]

- id: p03
  title: OS6870 支持边界：CPLD 不经 OV 升级、应用强制未支持
  type: principle
  source_chapter: "p6"
  source_quote: |
    OmniVista does not support performing CPLD upgrades. To upgrade the CPLD version, refer to the AOS Release Notes for the CPLD procedure on ONIE-based switches. Application Monitoring is now supported on an OS6870 running AOS 8.10R3 or higher. Application Enforcement is not yet supported.
  summary: |
    新接入的 OS6870 有三条边界：OV 不能做 CPLD 升级（须按 AOS Release Notes 在 ONIE 交换机上操作）；Application Monitoring 需 AOS 8.10R3 及以上；Application Enforcement 本版本尚不支持。规划 OS6870 管理能力时不要把这三项算进去。
  tags: [OS6870, CPLD, 应用监控, 功能限制]

- id: p04
  title: PALM 下线，由 Fleet Supervision 接替
  type: principle
  source_chapter: "p6"
  source_quote: |
    The ProActive LifeCycle Management (PALM) application is no longer available as a service and support option. OmniVista now provides Fleet Supervision as a PALM replacement for monitoring Service and Support entitlement, hardware status, and software versions, etc. Go to https://myfleet.ovcirrus.com/
  summary: |
    ProActive LifeCycle Management（PALM）不再作为服务与支持选项提供，替代品是 Fleet Supervision（https://myfleet.ovcirrus.com/），用于监控服务/支持权益、硬件状态与软件版本。从旧版本升级后，凡是依赖 PALM 的运维流程要切换到 Fleet Supervision。
  tags: [PALM, Fleet Supervision, 生命周期管理, 变更]

- id: p05
  title: 用户登录密码策略增强：有效期与 CLI 管理员找回
  type: principle
  source_chapter: "p7"
  source_quote: |
    Enforce Strong Password Setting – New Password Expiry policy now configurable. You can specify the number of days during which a password remains valid. By default, Password Expiry is set to "Never". Changes to this setting apply immediately to new users, but do not affect existing users until they change their password ... Password Recovery for CLI Admin – ... go to the "Change Password" option in the VA Menu
  summary: |
    两条新能力：(1) 密码有效期策略可配置（天数），默认 Never；改动对新用户立即生效，老用户要等下次改密才受影响。(2) CLI 管理员密码找回：登录页提示 "Forget your password? Use the VA menu to reset it."，在 VA 菜单的 Change Password 选项重置。注意 4.9R1 升 4.9R2 后强口令设置会被自动打开（见 ce67）。
  tags: [密码策略, 安全, VA 菜单, 新特性]

- id: p06
  title: SNMPv3 供给加密算法全量扩展
  type: principle
  source_chapter: "p7"
  source_quote: |
    Provisioning Encryption Strengthening – Support added for all Auth & Priv protocols when configuring SNMPv3 access in the default or custom Management Users Template. MD5 SHA MD5+DES SHA+DES SHA+AES SHA+AES192 SHA+AES256 SHA+3DES SHA224 ... SHA256+AES256+... SHA384+AES
  summary: |
    管理用户模板里配置 SNMPv3 访问时，认证/加密（Auth & Priv）协议组合全面扩展：MD5、SHA、MD5+DES、SHA+DES/AES/AES192/AES256/3DES、SHA224/SHA256/SHA384 系列组合。此前用非标准组合（如 SHA256+AES256）的设备现在可以直接纳管，不必降级到 MD5+DES。
  tags: [SNMPv3, 加密, 供给, 新特性]

- id: p07
  title: Wi-Fi Enhanced Open 过渡模式：一套开放 SSID 兼容新旧客户端
  type: principle
  source_chapter: "p7"
  source_quote: |
    When this mode is enabled, the AP broadcasts two different types of BSSID: one legacy Open SSID on 2.4GHz/5.0GHz band and one Enhanced Open SSID on 2.4GHz/5.0GHz/6.0GHz band ... the Enhanced Open Transition Mode is supported only on APs running AWOS 4.0.8 or above. Enabling this mode for APs running older AWOS versions may cause the SSID to revert to an open SSID after a reboot.
  summary: |
    SSID 新增 Enhanced Open Transition Mode：AP 同时广播传统开放 BSSID（2.4/5GHz）与 Enhanced Open BSSID（2.4/5/6GHz），让支持与不支持 OWE 加密的客户端共用同一开放 SSID。入口在 SSID 用途为 Guest Network（Open/Captive Portal）或 Employee BYOD 时可用。硬性前提：AP 必须 AWOS 4.0.8+，旧版本 AP 开启后重启可能导致 SSID 退回纯开放，官方强烈建议先升级网络。
  tags: [SSID, Enhanced Open, OWE, 无线, AWOS 版本依赖]

- id: p08
  title: 6GHz SSID 的 Backward Compatibility：让旧终端连得上
  type: principle
  source_chapter: "p7-8"
  source_quote: |
    When the 6.0GHz band is selected for the SSID, the other bands inherit using WPA3_SAE_AES encryption, which some legacy devices cannot use to connect ... When Backward Compatibility is enabled, the WPA3_PSK_SAE_AES Encryption Type is automatically used for the 2.4GHz and 5.0GHz bands ... if the MLO Band setting includes 6.0GHz, then the Backward Compatibility option is automatically disabled.
  summary: |
    选 6GHz 频段时其他频段会继承 WPA3_SAE_AES，旧设备连不上；开启 Backward Compatibility 后 2.4/5GHz 自动改用 WPA3_PSK_SAE_AES，6GHz 保持 WPA3_SAE_AES。可用条件：SSID 用途为 Protected Network（预共享密钥）或员工 Protected Network，且 Allowed Band 为 6GHz。互斥项：MLO Band 含 6GHz 时该选项自动禁用。
  tags: [SSID, WPA3, 6GHz, 向后兼容, MLO]

- id: p09
  title: Blast-RADIUS 防护：Require Message-Authenticator 开关
  type: principle
  source_chapter: "p8-9"
  source_quote: |
    A new Require Message Authenticator flag is now available to specify whether to check RADIUS packets for the Message-Authenticator attribute ... resolves CVE-2024-3596 (#Blast-RADIUS) ... The OmniSwitch does not include the Message-Authenticator attribute in RADIUS requests ... use the aaa radius message-authenticator CLI command on the switch. This CLI command is a global command supported on AOS 8.10R2 or higher.
  summary: |
    修复 CVE-2024-3596（Blast-RADIUS）：新增 Require Message Authenticator 开关，三种场景行为不同——(1) UPAM 做 RADIUS 服务器：AP 请求总带该属性；OmniSwitch 默认不带，须在交换机上执行 aaa radius message-authenticator（全局命令，AOS 8.10R2+）。(2) 外部 RADIUS 直连：AWOS>=5.0.2 的 AP 会校验响应包，旧 AWOS 不校验；OmniSwitch 同样要 CLI 命令。(3) UPAM 做代理：开关开启时 UPAM 校验外部服务器响应，缺失则丢弃并按 Retries 重试。升级后建议全网核对交换机 AOS 版本。
  tags: [安全, Blast-RADIUS, CVE-2024-3596, RADIUS, UPAM, 交换机 CLI]

- id: p10
  title: 框架更新：Oracle Linux 8.7 升 8.10 与 10 项 CVE 修复
  type: principle
  source_chapter: "p9"
  source_quote: |
    OmniVista VA and RAP VPN VA – Oracle Linux upgrade from version 8.7 to version 8.10 ... The following CVEs were fixed in this release: CVE-2024-52046 CVE-2017-18342 CVE-2025-24813 CVE-2020-14343 CVE-2024-52316 CVE-2022-30123 CVE-2018-1270 CVE-2024-41110 CVE-2018-1275 CVE-2025-30215
  summary: |
    OV VA 与 RAP VPN VA 的底层 Oracle Linux 从 8.7 升到 8.10；本版本修复 10 项 CVE（含 CVE-2025-24813、CVE-2025-30215 等）。安全合规驱动的升级可直接引用这份清单。另：阿里云短信网关新增 Messages Language 选项，可将 UPAM 短信翻译为中文并按语言生成模板（p9）。
  tags: [CVE, 安全补丁, Oracle Linux, 底层升级, 阿里云短信]

- id: p11
  title: 升级路径总则：只有 4.9R1 能直升，新工作流强制含 4.9R1 Patch 1
  type: principle
  source_chapter: "p9, p15-16"
  source_quote: |
    you can only directly upgrade to OV 2500 NMS 4.9R2 from OV 2500 NMS 4.9R1 ... To upgrade from older releases to 4.9R2, you must first upgrade to 4.9R1. Upgrading an OV 2500 NMS from 4.9R1 to 4.9R2 automatically includes a required upgrade to a 4.9R1 Patch 1 ... ensure that the 4.9R1 upgrade to 4.9R1 Patch 1 occurs first, before the upgrade to 4.9R2.
  summary: |
    直升 4.9R2 只能来自 4.9R1；更老版本必须先升到 4.9R1。4.9R1→4.9R2 采用全新升级工作流：流程会自动先升 4.9R1 Patch 1 再升 4.9R2，必须严格按 Installation and Upgrade Guide 的 "Upgrading from 4.9R1 to 4.9R2" 章节操作，不要手工跳步。从 4.7R1 出发的完整路径：4.7R1 Patch 2 → 4.8R1 → 4.8R2 → 4.9R1 → 4.9R2（共五步）。
  tags: [升级路径, 4.9R1 Patch 1, 升级工作流, 变更管理]

- id: p12
  title: HA 升级顺序与集群转换规则
  type: principle
  source_chapter: "p15, p19-20"
  source_quote: |
    The HA upgrade procedure requires first updating the Standby node then updating the Active node ... An L3 HA cluster is supported only with a fresh HA installation; you cannot convert an L2 HA cluster to an L3 HA cluster ... You can convert a 4.9R2 Standalone Installation to a 4.9R2 HA Installation if the 4.9R2 Standalone installation was upgraded from a 4.3R2 or newer Standalone Installation.
  summary: |
    HA 升级铁律：先升 Standby 节点，再升 Active 节点（L2/L3 各有专门章节）。L3 HA 集群只能全新安装，L2 不能转 L3；但可以给全新 4.9R2 单机加第二个节点组成 L3 HA，也可以把 4.9R1 单机升到 4.9R2 后再转 L3 HA。单机转 HA 的前提：该 4.9R2 单机是由 4.3R2 或更新版本的 Standalone 升级而来（从 4.3R1 升级来的不能转，见 ce69）。
  tags: [HA, 升级顺序, L3 HA, 单机转 HA, 集群]

- id: p13
  title: 网络规模分档与最低资源配置表
  type: principle
  source_chapter: "p17-19"
  source_quote: |
    Total Number of Managed Devices 500 / 2,000 / 5,000 / 10,000 ... Minimum Reserved OmniVista VA RAM for Standalone 20GB / 36GB / 64GB / 64GB ... HDD1:50GB HDD2:512GB/1024GB/2048GB ... The High-Availability Feature supports up to 4,000 devices. An HA installation should be done on a "Medium" or higher size VA.
  summary: |
    四档规模（Low/Medium/High/Very High）：管理设备 500/2000/5000/10000，Stellar AP 上限 500/2000/4000/4000，UPAM 认证客户端 2 万-10 万。CPU 需 2.4GHz 8/8/12/12 逻辑核；单机 RAM 20/36/64/64GB，HA 40/64/64GB；磁盘 HDD1:50GB + HDD2:512/1024/2048/2048GB，读写 100/150/200/200 MB/s。硬性规则：HA 最多 4000 台设备，且必须部署在 Medium 或更高规格 VA 上。High 档 4000 AP 时可另带 500 台 AOS 交换机，Very High 可带 1000 台（HA Very High 1500 台）。
  tags: [容量规划, 资源配置, RAM, 磁盘, HA 上限]

- id: p14
  title: VA 首次部署六条硬规则（磁盘/RAM/CPU/AES-NI）
  type: principle
  source_chapter: "p18-19"
  source_quote: |
    When deploying the OmniVista VA for the first time, do not add the new disks in the hypervisor until after OmniVista is configured and rebooted ... never allocate more memory than is available on the Host Server ... it is recommended that you reserve that RAM for the OmniVista VM ... Set CPU Shares to "High" ... A recommended algorithm is AES ... we recommend that you use Intel processors with the AES-NI instruction set enabled.
  summary: |
    部署 VA 六条规则：(1) 首次部署时，OV 完成配置并重启之前不要在 hypervisor 里加新磁盘。(2) RAM 分配不得超过宿主机可用量。(3) 按规模表分配并预留（reserve）RAM，避免性能问题。(4) CPU Shares 设为 High，逻辑核数不超过规模表推荐值。(5) 默认分区 HDD1:50GB + HDD2:512GB，管理超过 500 台设备要用 VA 菜单扩 HDD2。(6) 用 SNMPv3+AES 时建议 Intel AES-NI（2010 后 CPU、BIOS 开启、hypervisor 不屏蔽；VirtualBox 需确认 Nested paging）。
  tags: [部署, 容量, hypervisor, AES-NI, 性能]

- id: p15
  title: Stellar AP 升级顺序：先 OV 后 AP，Mesh 逐跳从末端开始
  type: principle
  source_chapter: "p14, p19"
  source_quote: |
    Stellar APs in your network should be running AWOS version of 5.0.2. First upgrade to OV 2500 NMS 4.9R2; then upgrade your Stellar APs to 5.0.2 ... when upgrading Stellar APs in a Mesh Network, you must upgrade them starting from the last node and proceeding hop-by-hop. You cannot use OmniVista Resource Manager for the upgrade since Resource Manager upgrades Stellar APs by AP Group simultaneously. You must use Stellar AP Web GUI for the upgrades.
  summary: |
    推荐全网 Stellar AP 运行 AWOS 5.0.2，顺序必须是先升 OV 2500 4.9R2、再升 AP 到 5.0.2。Mesh 组网下更要小心：从最末节点开始逐跳升级；不能用 Resource Manager（它按 AP Group 同时升级，会打断 Mesh），必须用 Stellar AP 的 Web GUI 逐台操作。
  tags: [Stellar AP, AWOS 5.0.2, Mesh 升级, 升级顺序, Resource Manager 限制]

- id: p16
  title: 外联防火墙白名单与关键端口表
  type: principle
  source_chapter: "p16-17"
  source_quote: |
    The following URLs must be allowed ... ALE Central Repository - ovrepo.fluentnetworking.com; AV Repository - ep1.fluentnetworking.com; Call Home Backend - us.fluentnetworking.com; Device Fingerprinting Service - api.fingerbank.org; Web Content Filtering – api.bcti.brightcloud.com
  summary: |
    出墙白名单五个域名：ovrepo.fluentnetworking.com（软件仓库/升级）、ep1.fluentnetworking.com（应用可见性签名）、us.fluentnetworking.com（Call Home/Fleet Supervision）、api.fingerbank.org（设备指纹）、api.bcti.brightcloud.com（WCF）。无直连外网时必须配代理（p16 2.1），否则签名更新、Fleet Supervision、软件升级都不可用。关键端口（p16-17）：HTTP 80/HTTPS 443、SNMP 161/162、MQTT 1883、RADIUS 1812/1813（转发 1814/1815）、CoA 3799、Syslog 514、VMM 的 135+49152-65535（RPC 动态口）、HA 节点间 TCP 8000/7801/2224 + UDP 5405、cliadmin SSH 2222。
  tags: [防火墙, 白名单, 端口, 代理, 网络准备]

- id: p17
  title: 许可证体系：三种类型与容量上限
  type: principle
  source_chapter: "p20-21"
  source_quote: |
    Starter Pack - Is free and enables you to use OmniVista on a limited basis without expiration. You can manage up to 30 devices (10 AOS, 10 Third Party, 10 Stellar APs). Evaluation - Is free ... 90 days ... 60 devices ... Production - Gives you full use of OmniVista without expiration ... certified to manage up to 10,000 devices ... up to 4,000 Stellar APs ... VM Manager application supports a maximum of 5,000 VMs
  summary: |
    许可分设备许可（ALE 设备认证上限 10000 台、第三方设备、Stellar AP 上限 4000 台；OAW 非 Stellar 设备按 AOS 计数）与服务许可（VM：VMM 上限 5000 台，超出告警并写日志；Guest 设备与 BYOD 设备：20/50/100/500/1000 档；HA：仅 Production；WCF）。三档类型：Starter Pack 免费 30 台（10+10+10）不过期；Evaluation 免费 60 台（20+20+20）90 天；Production 全功能不过期。导入/升级许可在 Administrator – License 页面完成；超限后再发现设备会产生审计日志与状态提示。
  tags: [许可证, 容量上限, Starter Pack, 评估版, VMM]

- id: p18
  title: 客户端访问：浏览器支持、入口地址与 Watchdog
  type: principle
  source_chapter: "p22"
  source_quote: |
    OV 2500 NMS 4.9R2 is supported on Chrome, Firefox, and Microsoft Edge browsers ... Internet Explorer is not recommended and has been deprecated ... The Watchdog Application, which enables all of the necessary OV 2500 NMS 4.9R2 Services must be started to launch OV 2500 NMS 4.9R2.
  summary: |
    浏览器仅支持 Chrome、Firefox、Edge，IE 已弃用。访问地址按安装类型区分：单机填服务器 IP；L2 HA 填虚拟 IP；L3 HA 填当前 Active 节点 IP。改过默认 HTTPS 443 端口要在地址后带端口号。启动排障第一步：确认 Watchdog 服务已启用（默认自启），它会拉起其余全部 OV 服务；可在 VA 控制台选 Run Watchdog Command 查看状态。
  tags: [浏览器, 访问入口, Watchdog, 启动排障, HA 地址]

- id: p19
  title: 默认登录凭据与首次强制改密
  type: principle
  source_chapter: "p23"
  source_quote: |
    log in using the Default Username and Password: Username: admin Password: switch ... When you first log in to OmniVista using the "admin" username and "switch" password, OmniVista will prompt you to change the default password.
  summary: |
    首次登录默认凭据 admin/switch，系统会强制要求修改默认密码。安全基线检查与交接环境时先核对这个账号；CLI 管理员密码丢失则走 VA 菜单 Change Password 找回（见 p05）。
  tags: [默认凭据, admin, 安全基线, 首次登录]

- id: p20
  title: 设备功能支持矩阵的关键限制（VMM/动态 VLAN/分析等）
  type: principle
  source_chapter: "p10-13"
  source_quote: |
    The VM Manager (VMM) application is supported on Hyper-V 2012, 2012 R2, and 2016. VMM is not supported on Hyper-V 2019 or higher ... Dynamic VLAN configuration is not supported on OS2260 and OS2360 switches; only static VLAN configuration and MVRP is supported ... only the English version of third-party software ... is tested and certified
  summary: |
    功能矩阵脚注里的硬限制：VM Manager 仅支持 Hyper-V 2012/2012R2/2016（不支持 2019+ 与 Windows Server 2022；第三方虚拟化软件仅英文版经过认证；VMM VLAN 配置不支持）；OS2260/2360 不支持动态 VLAN，只有静态 VLAN + MVRP；OS6900-X48C6 等也只有部分功能。第三方设备（Cisco/Extreme）纳管需在 Discovery 的 Third-Party Devices Support 手工提供 OID 并映射到 mib-2；LLDP 链路需两端都是受管设备且对端支持 IEEE 802.1AB lldpMIB。CLI Scripting 不能下发到 Stellar AP/第三方设备（但可以 SSH 连过去）。详见 counter-examples ce70-73。
  tags: [功能矩阵, VMM, 动态 VLAN, 第三方设备, LLDP, 兼容性]
