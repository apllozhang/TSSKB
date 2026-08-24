# principles 候选 — DT00XTE311 OmniVista 2500 NMS Administration R4

1. OV2500 纯虚机形态原理（Virtual Appliance = Linux OS + OV 应用，无独立安装器）
   - <<<PAGE 25>>>："OmniVista 2500 = Virtual Appliance. No standalone installers. Hypervisors: VMware ESXi, MS Hyper-V, KVM"。
   - <<<PAGE 44>>>："Includes both operating system (Linux) and OmniVista application"；支持的 hypervisor 版本：ESXi 6.5-8.0、Hyper-V 2012R2-2022、KVM Ubuntu 22.04。

2. 高可用（HA）双实例原理：Main/Standby 常驻、状态同步、故障接管
   - <<<PAGE 18>>>："Two instances of OV are constantly running: All functions are handled by the Main OV. The Main OV keeps the standby OV in sync … When control is moved from Main to Standby, all services and operations are transferred. UPAM with BYOD and Guest Access is taken over by Standby."
   - <<<PAGE 17>>>：HA over L2/L3，"Single server deployment to Primary/secondary operation controlled by optional software license"。
   - <<<PAGE 19>>>：HA 改进：安装设置只填一次、后台磁盘同步、"Traps automatically configured for both instances … Trap Replay automatic on failover. Alert banner displayed on failover."；容量认证 "up to 4K AP w/1.5K Switches"。

3. 无 HA 的后果原理（为什么需要 HA）
   - <<<PAGE 18>>>："if OmniVista became unavailable … The network administrator would no longer be able to monitor or make configuration changes. If using UPAM, no new additional clients would be able to authenticate."

4. Watchdog 服务管理原理
   - <<<PAGE 71>>>："Watchdog Application Manages Services (GUI / CLI). Watchdog can Start/Stop Services, View Service info."
   - <<<PAGE 221>>>：Control Panel → Watchdog Screen 显示所有 OV 服务状态，可逐个 Start/Stop（滑块控制），或 Start All/Restart All/Shutdown。

5. OV System Health / 会话管理原理
   - <<<PAGE 72>>>：系统健康提供 VA 的 CPU、内存、网络流量概览，"also provides information if there is a problem with the VA configuration"。
   - <<<PAGE 73>>>：Session Management 列出所有客户端登录会话，可用于强制登出某会话。

6. Thin Client OmniSwitch 原理（交换机零本地配置，配置存于 OV2500）
   - <<<PAGE 75>>>："No configuration is stored on the switch. It will contact OmniVista 2500 to retrieve the config."；仅 AOS 8.8R1+ 支持；"In thin-client mode, no configuration is saved in the 'running' directory. But there will be vcboot.cfg with the minimal network reachability configuration."；开关机经 activation 流程（Callhome / Sends Config）。
   - <<<PAGE 77>>>：Incremental Template 只在下一次周期 call-home（默认 30 分钟）应用一次。

7. SNMP 安全级别矩阵（snmp security 各档接受哪些请求）
   - <<<PAGE 69>>>：no security → 接受所有请求；authentication set → 接受 v1/v2 Get 及非认证 v3 Get；privacy all → 仅加密 v3 Set/Get；traps only → "All SNMP requests are rejected"。

8. SNMP source address / Loopback0 管理寻址原理
   - <<<PAGE 70>>>："-> snmp source ip preferred {default | no-loopback | ip_address}"；Default：有 loopback0 则用其作为源 IP，否则用 IP 栈第一个可用地址。发现用 Loopback0 地址（<<<PAGE 90>>>："These are the IP addresses that will be used to discover the switches in Omnivista"）。

9. NMS 组件模型（SNMP/sFlow/MIB/Traps/RMON 代理体系）
   - <<<PAGE 21>>>："NMS COMPONENTS: SNMP, sFlow (Analytics), MIB, Traps, RMON"，Agents ↔ Managed Devices ↔ Network Management Systems 三角。

10. CLI vs GUI 管理接口取舍原理
    - <<<PAGE 22-24>>>：CLI Pros（熟练度/脚本/熟悉度，"ASCII based configuration files can be copied and pasted from one switch to another"）；GUI Pros（颜色编码/易发现问题/减少 fat-finger 错误/批量操作）；WebView 为单设备原生网元管理器，"100% CLI equivalent features. Integrated with OmniVista"。

11. 双因素认证（2FA/TOTP）原理
    - <<<PAGE 157>>>："Used to enable/disable Two-Factor Authentication for user login based on User Role. It requires a user to enter an authentication code after entering their login/password."
    - <<<PAGE 158-159>>>："uses the Google Authenticator App to generate a time-based, 6-digit code"；首登扫 QR 码绑定，输入 TOTP Code 验证。

12. Quarantine Manager 遏制执行机制（VLAN/ACL/端口/黑名单）
    - <<<PAGE 307>>>：执行手段明细："VLAN MAC Rule (vlan 999 <mac_address>)、VLAN DHCP MAC Rule、ACL (condition IP source <>action <>)、IP <-> MAC、SNMP Set message"。
    - <<<PAGE 298>>>：检测来源开放："Syslog, Trap from Alcatel-Lucent or Third party IPS/IDP solutions … Brick Firewall … OmniAccess WLAN rogue Alert"；遏制动作含 "Port Shut down for Third party switches, Wireless end user block Listing"。

13. Quarantine 三列表语义（Candidates/Banned/Never Banned）
    - <<<PAGE 308>>>：Candidates：设备流量继续放行，等管理员 Release/Ban/Never-ban。
    - <<<PAGE 309>>>：Banned："it remains quarantined until the Network Administrator manually releases it."
    - <<<PAGE 310>>>：Never Banned："The OmniVista server and all switches discovered by OmniVista are implicitly placed in the Never Banned list."

14. Ethernet OAM / SAA 统计原理
    - <<<PAGE 140-141>>>："SAA ETHERNET OAM: Displays information about all configured SAAs and is used to create, edit, and delete SAAs between switch pairs"；统计维度 Jitter、RTT、Packet Loss，可从 Dashboard 以折线/柱状图展示。

15. Locator 定位原理（Live vs Historical；MAC/IP/授权用户三键）
    - <<<PAGE 30>>>："Troubleshooting tool to identify devices & end-user location (switch, slot/port, MAC and IP addresses). Live or historical searches for immediate reaction or forensic use."
    - <<<PAGE 136-137>>>：按 IPv4/v6、MAC、Authorized User 检索；命中交换机时自动在拓扑图定位居中。

16. Discovery 链路发现机制（AMAP/LLDP + 手工链路）
    - <<<PAGE 117>>>："Automatically discovered using AMAP or LLDP. Links can also be added manually."
    - <<<PAGE 118>>>："Manual links are persistent and displayed in RED when the link goes down. Recommended to configure critical links providing better monitoring capabilities."

17. 第三方设备支持机制（MIB-2 兜底 + 自定义 Mibset）
    - <<<PAGE 121-123>>>：支持 Web/Telnet/SSH、Custom MIBs、Custom Icons、Traps、Locator；添加方式：建 Mibset（OID/Display Name/MIB Directory）；"If you want to use MIB-2 level support for third-party devices, enter mib-2"；MIB 文件须 .mib 后缀，新目录须导入整套 MIB。

18. PolicyView LDAP 仓库架构原理
    - <<<PAGE 272/285>>>：策略存于 OV 安装时配置的 LDAP 目录服务器，交换机被通知后从该服务器拉取策略；Policy Administration ↔ LDAP Repository 多向同步。

19. sFlow 采样分析原理（Analytics 数据面）
    - <<<PAGE 316>>>："This application leverages sflow information. Essentially L1-L4 information."
    - <<<PAGE 322>>>：架构图：AOS Switch 发 Sflow Packets → OV Analytics Service → Mongo DB 存储 → WebServer 呈现；"OV profiles used to create sampling on switch ports"。
    - <<<PAGE 325>>>：应用识别："OmniVista identifies the applications using the TCP/UDP port obtained from sFlow packets"；知名端口自动标注。

20. 采样率定义
    - <<<PAGE 341>>>："Sampling Rate … Ratio of packets observed at the data source to the samples generated. For example, a sampling rate of 100 specifies that 1 sample will be generated for every 100 packets observed."

21. Top N Ports 趋势预测原理（机器学习）
    - <<<PAGE 334>>>："OmniVista samples past port utilization for a period of time (Prediction: Training Timeout), and predicts future utilization within a configurable error rate (Prediction: Training Error) using a machine learning algorithm."；预测数据量随区间：Last 24 Hours→12h、7 Days→3 Days、4 Weeks→2 Weeks。

22. Applications Management 双模式原理（Range-Based vs Enumerated）
    - <<<PAGE 350>>>：Range-Based：范围内端口被监控，未映射端口标 "Unknown"；Enumerated："Only those ports you define when you create a mapping will be monitored."

23. Application Visibility 签名机制原理
    - <<<PAGE 360/372>>>："A Signature File contains application signature information that is used to create Signature Profiles"；"A switch can be assigned only to one Signature Profile"；OS6860E/N 支持签名文件 Auto-Update："OmniVista automatically clone updates the profile, and assigns the updated profile to switches"；OV 自动检查 ALE 签名仓库并下载。

24. AppMon 交换机侧机制（flow table / enforcement 策略联动）
    - <<<PAGE 377-383>>>：CLI 验证命令族（show app-mon config / app-list / ipv4-flow-table monitor|enforcement / app-record hourly）；enforcement 流表命中策略规则 G_DL_MyAppsDR；"Wait for 15-20 minutes before the applications are displayed in the OV widgets."

25. IoT 设备画像原理（MAC OUI + DHCP 指纹）
    - <<<PAGE 400>>>："To Identify an IoT device, OmniVista uses the following: MAC OUI … DHCP FingerPrinting: allows to track the devices on the network"；数据源 "DHCP option 55 (the parameter request list) and option 60 (the vendor identifier)"。
    - <<<PAGE 405>>>：端点状态刷新周期：Stellar AP 设备每 5 分钟、AOS 交换机设备每 15 分钟。

26. IoT 执法（Enforcement）与豁免原理
    - <<<PAGE 408>>>："Configures category-based device authentication. By associating a Category with an Access Role Profile … exceptions for specific devices by SSID, MAC address, AP Group, or IP address."
    - <<<PAGE 404>>>：限制："IoT is supported on IPv4 devices only."

27. 统计采集与视图分离原理（Collection Profile vs View Profile）
    - <<<PAGE 343>>>："All managed switches are automatically included in a Default Statistics Collection Profile"；
    - <<<PAGE 391>>>："Only one profile can be assigned to an OmniSwitch … If you create a new profile, you will first have to unassign the 'Default Profile' from the desired switches."

28. SIP Snooping 原理（DSCP 标记 + 语音质量度量）
    - <<<PAGE 438>>>："Identifies and marks SIP and its corresponding media streams (RTP/RTCP) … Marking is done using the DSCP field"；计算 "Delay, Jitter, Round trip time, R factor and MOS values"。
    - <<<PAGE 442>>>：OneTouch 媒体模板固定优先级：Voice dscp 46/precedence 50000，Video dscp 34/44000，Other dscp 24/44001。

29. OVNA（OmniVista Network Advisor）云边协同原理
    - <<<PAGE 422-423>>>：Edge Computing（本地 Linux 服务器，收 syslog/SSH 采集）+ Cloud Processing & Orchestration；工作流：设备发 syslog(1) → 模式匹配执行脚本(2) → HTTPS 查询(3) → Rainbow 通知(4-6) → SSH 脚本化处置(7-9)。设备要求：OS 6xxx/9xxx AOS 8.7.R2+，Stellar AP AWOS 4.0.3 MR-3+。

30. Provisioning Rule 匹配机制（序列号/MAC/型号 + 5 分钟轮询）
    - <<<PAGE 461>>>："Rules can be created for specific switches (by serial number or MAC Address) or by switch model … the switches will contact the OV server every 5 minutes. If a switch matches a Rule, the Management and Configuration Templates in the Rule are pushed to the switch."

31. Golden Configuration 审计原理
    - <<<PAGE 467>>>："Configuration selected from a list of the three most recent switch backups that can be applied to a switch in the event there is an unwanted configuration change."
    - <<<PAGE 417>>>：Provisioning 后 OV 可周期审计配置、"Allow operators to mark a configuration as 'golden'"、偏离告警、必要时强制回归。

32. RCL/Bootstrap 引导原理（DHCP Option 43 Sub-option 128 / DNS 别名）
    - <<<PAGE 460>>>："Set up the DHCP Server to point to the local OmniVista Server as the Activation Server for provisioning - Option 43, Sub-Option 128 (recommended); OR set up the DNS to resolve activation.myovcloud.com to point to the OmniVista Server."；存量交换机需改 cloudagent.cfg 的 Activation Server URL（格式 as-lite.*.ove.local）并 `cloud-agent admin-state enable`。

33. NaaS 设备许可状态模型
    - <<<PAGE 127>>>："A device interacts with a designated License Activation Server to obtain a Device License: NaaS … CAPEX … CAPEX Undecided. The switch has not yet obtained a license."

34. VM Manager / UNP-VLAN 联动原理
    - <<<PAGE 30>>>："Single vCenter interface. Track VM and their associations to network equipment. Manage UNP VLANs for virtual machines. Notification of VMs not joining UNPs because of misconfiguration."

35. Captive Portal Profile/Domain Policy 分层原理
    - <<<PAGE 252>>>：Profile 仅对启用 CP 认证的 Access Role Profile 有效："Only valid when assigned to Access Role Profiles on which Captive Portal authentication is enabled"。
    - <<<PAGE 253-254>>>：Profile Domain Policy List（按登录域分配 CP Profile + QoS Policy List）与 Domain Policy List（按认证 realm 定义策略，"without the profile coming into play"）。
    - <<<PAGE 255>>>：定制文件（html/jpeg）构成 CP 登录页。

36. Access Auth Profile 端口行为细节（Port Bounce / Bypass / Failure Policy）
    - <<<PAGE 241>>>："Port Bounce. Required to handle scenarios where a client is switched from one VLAN to other after COA. If it is enabled, the port will be administratively put down. This is to trigger DHCP renewal and re-authentication"；"802.1X Auth and MAC Auth only applies to wired devices."
    - <<<PAGE 242>>>：802.1X Pass Alt / Bypass Status（跳过 802.1X 直入 MAC 认证或分类）/ Failure Policy；MAC Pass Alt / MAC Allow EAP。
