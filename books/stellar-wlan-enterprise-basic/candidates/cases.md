# Lab 案例 · OmniAccess Stellar WLAN Enterprise Basic (DT00XTE368EN)

> 来源：source/fulltext.md（页码即教材 PDF 页码），R-Lab 实验环境：3 台 OmniSwitch（6870/6360/2360）+ 2 台 Stellar AP + OV2500 虚机 + Raspberry Pi 无线客户端

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
