# Lab/配置案例 · OmniAccess Stellar WLAN Advanced Troubleshooting and Update (DT00XTE378EN)

> 来源：source/fulltext.md（页码即教材 PDF 页码）
> 范围：仅 p134 以后 Features Update 篇的新 Lab 与配置演示（p1-133 排障篇以姊妹书 T478 为准）

- id: c01
  title: Lab：AOS OmniSwitch 在 OmniVista 2500 中的发现（Backbone VLAN + SNMPv3）
  type: case
  source_chapter: "p213-223"
  source_quote: |
    "OS6870, OS6360, OS2360: -> user snmpuserv3 read-write all password \"Superuser=1\" sha+des -> snmp station 10.130.5.5X 162 snmpuserv3 v3 enable... Select NETWORK > DISCOVERY > Managed Devices > Click Discover New Devices... SNMPv3 Profile Parameters: Timeout 5000; Retry Count 3; User Name: snmpuserv3; Auth & Priv Protocol: SHA+DES."
  summary: |
    三台 OmniSwitch（6870/6360/2360）纳管进 OV2500 的完整实验：预置 Backbone VLAN 1305 互联所有管理设备，交换机侧两条 CLI 建 SNMPv3（用户 snmpuserv3、密码 Superuser=1、SHA+DES 认证加密、trap 目标 10.130.5.5X:162）；OV2500 侧在 Discovery Profile 里配同名参数（超时 5000ms、重试 3 次），Managed Devices 下按 IP 段（10.130.5.20X/22X/24X 三个范围）发起 Discover Now。失败时按层排：二层 show interfaces / show vlan members port 查线缆与 VLAN；三层 show ip interface 查 IP 接口状态、OV2500 虚机菜单（cliadmin 登录）查 IP 配置、双向 ping；SNMP 层 show snmp station、show aaa authentication 并重输密码对齐两端参数后重新发现。

  tags: [lab, snmpv3, discovery, omnivista-2500, omniswitch]

- id: c02
  title: Lab：Stellar AP 云上线（VLAN Manager + Option 138 + PoE 重启 + AP Group 纳管）
  type: case
  source_chapter: "p224-239"
  source_quote: |
    "Once powered on, the Stellar Access Points will send a DHCP request on the VLAN 40. This request will be relayed by the core switch 6870 to the DHCP Server on the VLAN 1305. The DHCP Server will then send a DHCP Offer with the option 138 (IP address of the OmniVista 2500). Once this option received, the Stellar Access Point will work in Enterprise mode."
  summary: |
    AP 上线链路实验：用 VLAN Manager 的 Create VLAN by Devices 向导一次给三台交换机建管理 VLAN 40（接入交换机 1/1/6 做 default 口、级联口打 Q-tag）；核心 6870 预配 int_management IP 接口、DHCP relay（ip dhcp relay destination + admin-state enable）与静态路由；接入交换机启用 AP 端口并用 lanpower slot 1/1 service stop/start 重启 PoE 逼 AP 重启注册；AP 的 DHCP 请求经 relay 到服务器，Offer 带 option 138（OV2500 地址），AP 进入 Enterprise 模式。发现环节先选国家码（FR）与时区，AP 在 Unmanaged 列表里 Change to Trust Status 后建 APGX 组并 Change Group 纳管。排障路径：查 PoE（show lanpower）、VLAN、AP 串口（support 账号）getmode 看是否 OV 模式、getovinfo 看 OV 地址、tcpdump 抓 DHCP Offer 验证 option 138/43；Windows Server 侧在 DHCP 预定义选项里加 Code 138/IP Address 类型并填 OV2500 地址。

  tags: [lab, ap-onboarding, option-138, vlan-manager, poe, ap-group]

- id: c03
  title: Lab：安全 Employee SSID 创建与 802.1X 验证（UPAM 内置 RADIUS）
  type: case
  source_chapter: "p290-310"
  source_quote: |
    "SSID Service Name: EmployeesX; Usage: Enterprise Network for Employees (802.1X)... Allowed Band: 2.4GHz and 5GHz; Encryption Type: WPA3_AES... RADIUS Server: UPAMRadiusServer... Default VLAN/Network: VLAN ID: 20... Authentication: ProtectedEAP; No CA certificate; PEAP version: Automatic; Inner Auth: MSCHAPv2."
  summary: |
    员工 SSID 全流程：先建 VLAN 20 并确认 6870 预配的 int_employee 接口（10.7.X.62/27）；向导建 EmployeesX（Usage 选 Enterprise Network for Employees，WPA3_AES，认证策略选 UPAMRadiusServer，顺手建 Employee 账号），默认 VLAN 20，Save and Apply 到 APGX 组；树莓派客户端用 PEAP/MSCHAPv2（不校验 CA）连入，验证拿到 10.7.X.32/27 段地址并能 ping 通 DHCP 与 OV2500；监控用 UPAM Authentication Record 与 WLAN Client List/Session 查认证记录与所在 AP。附带的 Expert 模式等价操作串起七个对象：WLAN Service → AAA Server Profile → Access Role Profile（Apply to Devices 映射 VLAN 20 到 AP Group）→ Authentication Strategy（本地库）→ Access Policy（映射条件 SSID=EmployeeX）→ 部署。AP 侧排障链：iwconfig/iwlist 查配置与信道、sta_list/wam_debug sta_list 查客户端、cat wlanservice.conf 与 AAA_server.conf 核对 RADIUS 参数、tcpdump -i br-wan -s 0 host radiusIP 抓认证报文。

  tags: [lab, employee-ssid, 802.1x, upam, peap, wlan-service-expert]

- id: c04
  title: Lab：Employee SSID 对接 Microsoft Active Directory 认证
  type: case
  source_chapter: "p311-316"
  source_quote: |
    "Select UPAM > SETTINGS > LDAP/AD Configuration: LDAP/AD Server: Enable; Server Type: AD; TLS/LDAPS: NS; NETBIOS Domain Name: COMPANY; DNS Domain Name: company.com; FQDN/IP address of Domain Controller: 10.130.5.130; Username: ov2500; Password: Alcatel.0; AD Port: 389; Click on Test Connection to test the connection to the AD."
  summary: |
    在 c03 基础上把认证源从 UPAM 本地库切到企业 AD 两步完成：(1) UPAM > SETTINGS > LDAP/AD Configuration 声明 AD 服务器——服务器类型 AD、不启用 TLS/LDAPS、填 NETBIOS 域名（COMPANY）、DNS 域名（company.com）、域控 IP（10.130.5.130）、绑定账号（ov2500）、AD 端口 389，先点 Test Connection 验证连通再 Apply；(2) 回到 EmployeesX SSID 的 Authentication Strategy 点 Edit，认证源从本地库改成 External LDAP/AD 并 Apply。测试时先用 Clean Wireless Networks 清空客户端保存的网络再重连，账号改用 AD 里的 Employee/Alcatel.0（域口令），认证记录在 UPAM Authentication Record 里核对。这是"本地账号过渡到企业目录"最短路径的样板。

  tags: [lab, active-directory, ldap, upam, authentication]

- id: c05
  title: Lab：Guest SSID + Captive Portal（含踢除与黑名单、访客服务限制）
  type: case
  source_chapter: "p317-338"
  source_quote: |
    "Usage: Guest Network (Open or Captive Portal); Do you want users to go through a Captive Portal? YES; Captive Portal Type: OV-UPAM Captive Portal... Guest Access Strategy: Portal Page: DefaultPortal; Login by: Username & Password... Select the Client; Click on KickOff... Click on Add to Blocklist."
  summary: |
    访客 SSID 全流程：建 VLAN 30 与预配 int_guest（10.7.X.94/27）；向导建 GuestsX，Usage 选 Guest Network 并启用 OV-UPAM 门户，建 Guest 账号（Data Quota 禁用），Guest Access Strategy 设门户模板与用户名密码登录，默认 VLAN 30，应用到 APGX；客户端连入后开浏览器访问任意非 HTTPS URL（如 http://2.2.2.2）被重定向到门户，勾选条款登录；验证拿到 10.7.X.64/27 段地址。管理动作两个：UPAM > Guest Access > Guest Device 里 KickOff 踢下线（可重连），WLAN Client List 里 Add to Blocklist 拉黑（不可重连，Client BlockList 可解除）。附录用 Unified Policy 限制访客服务：建 DeniedServ 策略（Service Group 含 telnet 23/SSH 22，动作 DROP，下发到 6870+APGX，注意 OS2360/6360 不支持）与 GuestsPolicy 列表（DeniedServ + 默认 AcceptAll），Notify All 推送后挂到 __GuestsX Access Role Profile（映射 VLAN 30），客户端重连触发重认证后 ssh 10.7.X.62 被拒。排障含时间/日期核对（访客账号有有效期）、AP DNS 配置、eag_cli show user all 与 eag.log。

  tags: [lab, guest-ssid, captive-portal, blocklist, unified-policy]

- id: c06
  title: Lab：Web Content Filtering 按类别过滤访客网页（Social/Gambling 拒绝）
  type: case
  source_chapter: "p339-349"
  source_quote: |
    "In the category Web Content Filtering, activate WCF: Click on Commit... Name: WCF-guests; Category: Social Networking; Action: Reject; Category: Gambling; Action: Reject... Under the category Web Content Filtering (WCF), select WCF-Guests from the drop-down menu; Click on Apply... Apply it to the AP Group. Otherwise, the modification is just changed locally."
  summary: |
    WCF 落地四步：(1) AP Group（或单 AP 的私有配置）里激活 WCF 并 Commit；(2) UPAM > Web Content Filtering 建 WCF-guests 档案，加两条规则 Social Networking=Reject、Gambling=Reject（默认其余全放行）；(3) 把档案绑到访客的 Access Role Profile __GuestsX；(4) 关键一步——改完 ARP 必须 Apply to Devices（Map to VLAN 30 + APGX 组），否则改动只留在服务器不推 AP。验证：google 可达；facebook/twitter（社交类）与 unibet（博彩类）不可达——AP 不再转发该网站域名的 DNS 解析，浏览器直接报错。原理链路：AP 对 DNS 做窥探取 FQDN → Brightcloud SDK 分类 → 按 ARP/类别定策略 → 把 Allow/Block 状态发回 AP → AP 生成针对该 FQDN 解析 IP 的阻断 ACL。排障：OV2500 虚机菜单查 DNS 配置（选项 2→6，DNS1 10.130.5.130 / DNS2 10.0.0.51），缺 DNS 时 WCF 状态为 Not in service。

  tags: [lab, wcf, dns-snooping, brightcloud, guest-filtering]

- id: c07
  title: Lab：BYOD 员工自带设备 SSID（预认证进 Guest VLAN，过门户后迁移 Employee VLAN）
  type: case
  source_chapter: "p350-361"
  source_quote: |
    "For this SSID, no additional VLANs need to be created: we will reuse the VLAN 20 (Employee) and 30 (Guest). The BYOD employee device will be placed first in the Guest VLAN (pre-authentication). Once authenticated via a Captive Portal, it will be moved to the Employee VLAN(post-authentication)."
  summary: |
    BYOD SSID 的巧妙之处是不建新 VLAN：向导建 BYODX（Usage 选 Employee BYOD Network，启用 BYOD Registration），BYOD Access Strategy 的 Post Portal Authentication Enforcement 里设 Fixed Access Role Profile = _EmployeesX（认证通过后授予员工角色），默认 VLAN 填 30——设备先落在访客 VLAN 受限上网，员工在门户用企业账号（Employee/password）注册个人设备，认证成功后被动态迁到 VLAN 20 获得员工权限。验证看 WLAN Client List 里该客户端的 VLAN 变成 20。门户成功页还提供"添加更多个人设备"入口：登录后分 Online Devices（当前在线设备）与 Remembered Devices（已记住设备，支持手动添加无界面设备）两个页签。AP 侧排障沿用 iwconfig ath003、resolv.conf 查 DNS、sta_list 看客户端 VLAN 归属。

  tags: [lab, byod, dynamic-vlan, post-authentication, captive-portal]

- id: c08
  title: Lab：RF Profile 与 Association RSSI 阈值（把弱信号客户端挡在门外）
  type: case
  source_chapter: "p362-371"
  source_quote: |
    "Modify the Association RSSI Threshold for all the bands to a value much higher than the Client value (ex. 90, which is higher than -18 dBm = 78) and click Apply... The client tries to associate to the SSID but is not able to. The Stellar AP will ignore all association requests from the Wi-Fi client as the power of its signal is lower than the threshold."
  summary: |
    RF Profile 实验：建 My_RF_Profile（选国家码），Smart Load Balance 区含 Band Steering/Exclude MAC OUI/Force 5GHz/Association 与 Roaming RSSI 阈值，Per Band Info 区控制每频段的信道（ACS 自动/手选/信道列表/DRM 范围）、信道宽度、功率上下限、外接天线增益、信标间隔、短保护间隔、MU-MIMO、High Efficiency（关掉则 11ax 降级 VHT）。核心演示：先在 Client List 记下客户端信号（-18dBm），按换算规则（dBm=RSSI-96，即 78）把 Association RSSI Threshold 设为 90，Apply 后把 Profile 挂到 APGX 组——客户端 RSSI 70-78 < 90，AP 直接忽略其关联请求，任何 SSID 都连不上；把组切回默认 RF Profile 恢复。AP 侧核验配置用 cat /tmp/config/rfprofile.conf（看 signalStrengthThreshold/roamingSignalStrengthThreshold 等实际下发值），客户端 RSSI 用 wlanconfig ath102 list，信道调度的 ACS 日志在 kes_syslog 里 grep DRM。

  tags: [lab, rf-profile, rssi-threshold, smart-load-balance, acs]

- id: c09
  title: Lab：RAP 远程 AP 部署（Freemium Cirrus + OV2500 + 双隧道 VPN Server 全流程）
  type: case
  source_chapter: "p451-481"
  source_quote: |
    "Enter the AP Serial Number... Select Is this a Remote AP? YES... VPN Settings: Server's Public IP; Port; Server's VPN IP; OmniVista Enterprise Server IP; Client VPN IP Address Pool... Transfer the <VPN Server name>.conf file in the folder /opt/OmniVista_2500_NMS/data/vpn_conf/vpn_profile... Use Tunnel; Tunnel ID (must be 0); select the VPN Server."
  summary: |
    最重的压轴 Lab，串起云、服务器、AP、客户端四端：Cirrus 4 建 Freemium 账号（registration.ovcirrus.com），Device Catalog 里凭 AP 序列号+MAC 声明并勾选 Is this a Remote AP，配管理 VPN（公网 IP:6550、服务器 192.168.0.1、客户端池 192.168.0.2-.20、OV2500 IP），Save 后导出 .conf；VPN Server VA 控制台配双网卡（eth0 公网、eth1 私网 10.130.5.251）、网关、DNS、SSH(22)，FileZilla 把 .conf 传到 /opt/OmniVista_2500_NMS/data/vpn_conf/vpn_profile，建 vpn_mgmt 服务并绑定端点（Layer 3 VPN），Apply 后重启 AP，Maintenance > VPN Status 里看到 peer 握手即隧道通；OV2500 侧加默认路由（192.168.0.0/24 网关 10.130.5.251），AP 出现在 Managed AP；再建数据 VPN（vpn_data，端口 6551，服务器 10.7.0.61、客户端池 10.7.0.55-.60，L2GRE），导出第二个 .conf 导入 VPN Server 的 eth2 端点，AP Group 里指定 Data VPN；最后建 Employee SSID 时 Default VLAN/Network 选 Use Tunnel（Tunnel ID 0 + 选 VPN Server），远端 Windows 客户端连 SSID 即拿到员工网段地址。附录含 Cirrus 账号创建与 VPN Server OVF 在 ESXi 的部署。

  tags: [lab, rap, vpn-server, l2gre, freemium, end-to-end]

- id: c10
  title: Lab：备份/恢复/升级（含"恢复不生效"的现场复现与固件升级双路径）
  type: case
  source_chapter: "p423-432"
  source_quote: |
    "Select the OS6870 in the list; Click on the RESTORE button... Select only the 2 vcboot.cfg files... the configuration files are transferred in the WORKING and CERTIFIED folders but are NOT applied on the RUNNING configuration... launch the following command: reload from working no rollback-timeout."
  summary: |
    变更管理实操：铃铛图标 Save All 保存全网 Running；Resource Manager 按设备备份三台交换机（FTP 认证 admin/switch，Configuration Only）+ 按 AP Group 备份 Stellar；随后故意在 6870 上建临时 VLAN 70-80，再恢复备份——恢复结果显示成功但 VLAN 70-80 仍在，因为文件只落 WORKING/CERTIFIED 不碰 RUNNING，必须 reload from working no rollback-timeout 重启（约 3 分钟）才真正回滚，之后 VLAN Manager 里点 Poll 刷新确认删除。固件升级两条路：Resource Manager > Upgrade Image 导入 ALE 的 WinZip 可执行包（切勿手动解压）后按型号选设备或 AP 组 Install；或单台 AP 走 Web——AP Group 开 AP Web（密码 Alcatel.0），https://<AP IP> 用 Administrator 登录，System 页上传镜像文件或填镜像 URL。可顺带配置周期备份调度（Start At/Recurrence/Range）。

  tags: [lab, backup, restore, upgrade, resource-manager, reload-working]

- id: c11
  title: Lab：拓扑监控与 Trap Responder 邮件告警（重启 AP 触发 Critical 通知）
  type: case
  source_chapter: "p433-443"
  source_quote: |
    "Agent Type: AP Group; Traps which match these severities: Critical; Response: Action: Send an e-mail... E-mail Subject: Warning! Critical Trap Received on $TrapAgent$ ($TrapAgentName$)!... SMTP Server: 10.130.5.6; 'From' Address: ov2500@company.com; SMTP Authentication: OFF."
  summary: |
    监控闭环演示：Topology 应用建 Site 聚合 5 台设备，学两组状态语义——设备圈颜色（绿=Up、橙=Warning 收到 trap、红=Down）与通知圈颜色（无圈=正常、橙=Warning、紫=Minor、黄=Major、红=Critical），链路颜色（绿全通/橙部分断/红全断/蓝未知）；ACK/CLEAR 处理通知（单次上限 1000 条，可 Ack All/Clear All），AP 与交换机之间链路不显示时用 Poll Link 手动拉。告警链路：Trap Responder 建规则（Agent 选 AP Group APGX、严重级别 Critical、动作发邮件，主题/正文可用 $TrapAgent$/$TrapAgentName$ 变量）；ADMINISTRATION > PREFERENCES > System Settings 声明 SMTP 服务器并发测试邮件；最后在拓扑里重启一台 AP 人为制造 Critical trap，等几分钟查邮箱验证告警送达。Notifications Home 支持按 AP Group + 严重级别过滤（实验里能看到本课程历次重启记录）。

  tags: [lab, monitoring, topology, trap-responder, email-alert]

- id: c12
  title: Lab：Heat Map 与 Floor Plan（手工布点看覆盖 vs 算法自动布点）
  type: case
  source_chapter: "p444-450"
  source_quote: |
    "Heat Map: Campus > Building > Floor Map... Click on Scale the Map; Trace a line on the map; Enter a distance for this segment (5 meters)... Draw:WallsHeavy... (Floor Plan) Click on Operation > Auto Deployment; Quality: Excellent; AP Model: OAW-AP1231; TX Power: 14."
  summary: |
    两个 RF 规划工具对比实验。Heat Map（现状呈现）：按 Campus>Building>Floor 三级层级建档并导入平面图 jpg，三步出图——画一条 5 米线段标定比例尺、用 WallsHeavy 等障碍物工具描墙（预置障碍各有吸收系数 dB，也可自定义）、把在线 AP 拖放到实际位置，即可按 AP 真实频段与功率渲染覆盖；拖动 AP 位置可模拟新覆盖，Survey Toggle 切 2.4/5GHz 能直观看到 2.4G 穿墙强、5G 速度快但穿墙弱的差异。Floor Plan（规划仿真）：同样标尺与障碍后走 Auto Deployment，输入期望质量（Excellent）、AP 型号（OAW-AP1231）、发射功率（14），算法自动给出最优布点；结果随比例尺、障碍数量类型、AP 型号、质量档位变化，冷区可手工补点再 Save The Layout 看整体覆盖。

  tags: [lab, heat-map, floor-plan, auto-deployment, rf-planning]
