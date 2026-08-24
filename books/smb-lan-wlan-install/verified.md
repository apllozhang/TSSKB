# Verified 候选（V1 原文真实性核对 + V2/V3 抽查）

## cases

## C01. 首次登录并开通 OS6360 端口 + 管理 IP（Devices Startup Lab）
- 页码：<<<PAGE 95>>>–<<<PAGE 96>>>
- 命令序列：
  - `OS6360-XTE210 -> interfaces 1/1/6 admin-state enable`（AP 口）
  - `OS6360-XTE210 -> interfaces 1/1/1 admin-state enable`（客户端口）
  - `OS6360-XTE210 -> ip interface int_1 address 192.168.1.2/24 vlan 1`
  - 验证：`-> show ip interface`
  - 保存：`-> write memory flash-synchro`
- 原文摘录："Create an IP interface on the OmniSwitch 6360 to reach the AP Stellar 1321"
## C02. Stellar AP1321 首次配置向导（Configuration Wizard）
- 页码：<<<PAGE 99>>>–<<<PAGE 103>>>
- 步骤：浏览器访问 `192.168.1.254:8080`（默认口令 admin）→ 向导改管理员密码 → 选国家/时区 → 创建首个 SSID（AdminX/superuser，替换默认 mywifi-XXXX）→ AP 面板改 IP Mode 为 Static（IP 192.168.1.3，网关指向 6360）→ 用新 IP 重连。
- 原文摘录："A new SSID « AdminX » has been created and replace the default SSID broadcasted by the Stellar AP"
## C03. Stellar AP1321 恢复出厂的两条路径
- 页码：<<<PAGE 104>>>
- 路径A（Reset 键）："Press the Reset for 10 seconds in the back of the AP, then release it"
- 路径B（Console，凭据 support/aos2016）：
  - `ssudo firstboot -y`
  - `ssudo reboot`
## C04. OS6360 恢复出厂（删除配置 + 重启）
- 页码：<<<PAGE 105>>>
- 命令：`-> rm /flash/working/vcboot.cfg` → `-> reload from working no rollback-timeout`（约 5 分钟）
- 原文摘录："It takes approximately 5 minutes for the OmniSwitch 6360 to reboot."
## C05. 开启 SSH/HTTP 远程管理（Remote Access Lab）
- 页码：<<<PAGE 107>>>–<<<PAGE 109>>>
- 命令序列：
  - `OS6360-XTE210-> aaa authentication ssh local`（默认 SSH 被 deny）
  - `OS6360-XTE210-> aaa authentication http local`
  - 检查：`-> show aaa authentication`、`-> show webview`
- 后续（<<<PAGE 111>>>）：`-> show session config` 验证 Inactivity Timer（CLI 45 / HTTP 15 分钟）。
## C06. WebView 图形化建/删 VLAN
- 页码：<<<PAGE 113>>>–<<<PAGE 114>>>
- 步骤：Layer 2 > VLAN > "+" > 填 VLAN 59 / 描述 Student > SUBMIT > Save > CLI 用 `show vlan` 交叉验证；删除同理（勾选后点 Delete 图标）。
- 原文摘录："Click on + to add a VLAN and insert the following VLAN information: Vlan: 59, Description: Student"
## C07. 目录管理全流程实验（working/certified/user-defined）
- 页码：<<<PAGE 131>>>–<<<PAGE 137>>>
- 关键命令：
  - `-> ls -l /flash/working |or| ls -l /flash/certified`
  - `-> show microcode working |or| certified |or| loaded`
  - `-> show running-directory`（判读 RUNNING / CERTIFY NEEDED / SYNCHRONIZED）
  - `-> vlan 2 / vlan 3 / vlan 99`（改 RAM 后状态变 NOT SYNCHRONIZED）
  - `-> write memory` → `-> reload all` → `-> reload from working no rollback-timeout`
  - `-> mkdir lab` → `-> cp working/*.* lab` → `-> reload from lab no rollback-timeout`
  - `-> copy running certified`、`-> modify running-directory working`
- 原文摘录："Running configuration: lab > the OmniSwitch is running from the user-defined lab."
## C08. USB 备份与查看 uflash 内容
- 页码：<<<PAGE 138>>>–<<<PAGE 139>>>
- 命令：`-> usb enable` → `-> usb backup admin-state enable` → `-> write memory`（自动同步到 USB）→ `cd /uflash; ls` 验证 certified/working 目录。
- 提示："CAUTION: Do usb disable before removing usb"
## C09. PoE 监控 + 三 VLAN 规划与端口分配（PoE/VLAN/DHCP Lab）
- 页码：<<<PAGE 173>>>–<<<PAGE 175>>>
- 命令序列：
  - `-> show lanpower slot 1/1`（确认 1/1/6 口 Powered On，Class 4）
  - `-> vlan 10 name Management-AP / vlan 20 name Employees / vlan 30 name Guests`
  - 上联口 1/1/3：`vlan 10|20|30 members port 1/1/3 tagged`
  - AP 口 1/1/6：`vlan 10 members port 1/1/6 untagged` + VLAN20/30 tagged
  - `-> show vlan members port 1/1/6` 验证
- 原文摘录："The VLAN 10 (Administration AP) as default/untagged VLAN. The VLAN 20 and 30 as tagged VLANs."
## C10. AP 切换 DHCP 模式与 mywifi 域名重连
- 页码：<<<PAGE 176>>>–<<<PAGE 180>>>
- 步骤：连 AdminX SSID → Web 界面 AP > IP Mode > Edit > DHCP > Save → 此后用 `mywifi.al-enterprise.com:8080` 域名访问管理页（IP 已动态化）。
- 交叉验证（<<<PAGE 181>>>）：交换机侧 `-> show mac-learning` 找到 AP 的 MAC（dc:08:56:00:0c:e0 on 1/1/6）。
## C11. Express 模式 Employees SSID 创建（密码认证 + VLAN 20）
- 页码：<<<PAGE 221>>>–<<<PAGE 224>>>
- 步骤：Web 界面 WLAN > New > 名称 EmployeesX、Security Personal、密码 superuser > Advanced > VLAN ID 20 > Save；客户端连接后 `ifconfig` 确认落在 192.168.20.70–79。
- 原文摘录："The default gateway 192.168.20.7, which is the router's IP interface address of sw7 for the VLAN 20."
## C12. Express 模式 Guests SSID + 内置 Captive Portal + 访客账号
- 页码：<<<PAGE 225>>>–<<<PAGE 228>>>
- 步骤：WLAN > New > GuestsX、Security Open、Captive Portal Yes、VLAN 30 > Access > Authentication 选 Account > Add 建账号 Guest/superuser 并设起止日期 > 客户端连 SSID 后访问任意 non-https URL 被重定向到门户 > 登录后取 192.168.30.x 地址。
- 原文摘录："Enter any non-https URL (ex: http://2.2.2.2) and you are redirected to the Captive Portal"
## C13. AP 内置 DHCP 服务器配置（AP Networks + Pool 绑定）
- 页码：<<<PAGE 229>>>–<<<PAGE 233>>>
- 步骤：AP > 点击 AP IP > 新页签 Network > AP Networks > vlan10 行 Manage > 填 IP 192.168.10.3/24 > Service > DHCP > Create（Pool Employees，Range 192.168.10.10–50，网关/DNS=192.168.10.3）> Action > Bind Network > vlan10；vlan20/Guests 同法。
- 原文摘录："The DHCP range contains 40 IP addresses. So only 40 devices can be connected simultaneously."
## C14. 访客行为日志（Client Behavior Tracking）
- 页码：<<<PAGE 233>>>
- 步骤：Access > Authentication > 启用 Client Behavior Tracking > Log To 选 TFTP/SFTP/Syslog 并填服务器 IP、周期；日志行含事件时间、客户端 MAC/IP、AP MAC、SSID、ONLINE/OFFLINE 状态。
## C15. GuestOperator 受限管理账号
- 页码：<<<PAGE 234>>>
- 步骤：System > General > Account Management > Operator Enable + 设密码 > 重新登录选 GuestOperator，进入仅管理访客账号的简化界面。
## C16. 外部 RADIUS 认证的 SSID 配置（Enterprise）
- 页码：<<<PAGE 235>>>
- 步骤：WLAN > New > Security Enterprise > AuthServer 填 RADIUS IP（192.168.1.250）+ AuthSecret > Advanced > VLAN 10 > Save。
## C17. 多交换机多 AP 环境：OS2360 接入 + AP 自动成组
- 页码：<<<PAGE 264>>>–<<<PAGE 268>>>
- 命令（OS2360）：
  - `vlan 10` / `vlan 10 members port 1/1/8 tagged` / `vlan 10 members port 1/1/6 untagged`
  - `interfaces 1/1/8 admin-state enable`、`interfaces 1/1/6 admin-state enable`
- 验证：连 AdminX 后 `mywifi.al-enterprise.com:8080` 中两台 AP 出现在同一 AP Group；System > General 可改 Group 名/ID/管理 IP；PVM 为型号更高的 AP1321。
## C18. OV Cirrus 交换机上线全流程（含强制 call-home）
- 页码：<<<PAGE 338>>>–<<<PAGE 346>>>
- 命令（OS6360）：
  - `vlan 1305 name SW-MANAGEMENT`、`ip interface "int_sw-mgmt" address 10.130.5.5/24 vlan 1305`、`vlan 1305 members port 1/1/3 tagged`、`ip static-route 0.0.0.0/0 gateway 10.130.5.7`
  - `aaa authentication default local`、`snmp security authentication all`
  - `ntp client admin-state enable`、`ip domain-name remote-lab.com`、`ip name-server 9.9.9.9`、`ip domain-lookup`
  - `cloud-agent admin-state enable`
  - 强制上线：`cloud-agent admin-state disable force` → `cloud-agent admin-state enable`（或 `reload from working no rollback-timeout`）
  - 验证：`show cloud-agent status`（DeviceManaged / Certificate Consistent）
- Cirrus 侧：建 Site/Building/Floor > Device Catalog > Create Device（贴 `show chassis` 序列号）> 等 "OV Managed"。
## C19. OV Cirrus Stellar AP 上线与 AP Group/Provisioning 创建
- 页码：<<<PAGE 352>>>–<<<PAGE 357>>>
- 步骤：Console `showsysinfo`（support/aos2016）取 SN > Device Catalog > Create Device（Stellar AP）> Create Access Point Group"My-AP-Group" > Create Provisioning Configuration"My-Provisioning-Config"（Site + Default RF Profile + Timezone）> 绑组 > 重启 AP 加速 call-home（`ssudo firstboot -y; ssudo reboot`）> CLI `ocloud_show` 验证 VPN connected。
## C20. OV Cirrus Employees SSID 创建（802.1X + UPAM）
- 页码：<<<PAGE 390>>>–<<<PAGE 396>>>
- 步骤：
  1. Cirrus 建 VLAN 20（LAN > Layer 2 > VLAN，OS6360A 端口 1/1/3、1/1/6 tagged）；OS2360 手工 `vlan 20 name EMPLOYEE / vlan 20 members port 1/1/6 tagged / vlan 20 members port 1/1/8 tagged`
  2. Wireless > SSIDs > Create SSID：Usage=Enterprise Network for Employees (802.1X)、WPA2_AES、2.4+5GHz
  3. 认证策略 RADIUS Server=UPAMRadiusServer > Manage Employee Accounts 建账号 Employee/password
  4. Network Assignments 绑 My-AP-Group > VLAN/Tunnel Mapping=VLAN 20
  5. 客户端 PEAP/MSCHAPv2 连接验证；Network > Access Records > Authentication Records 查认证记录。
## C21. OV Cirrus Guests SSID 创建（Captive Portal + 踢出客户端）
- 页码：<<<PAGE 418>>>–<<<PAGE 425>>>
- 步骤：VLAN 30（Cirrus + OS2360 手工）> Create SSID：Usage=Guest Network、Captive Portal=YES（OV-UPAM）> 建 Guest 账号 > Create Guest Access Strategy + Captive Portal Template（Login By Username & Password）> 绑 My-AP-Group/VLAN 30 > 客户端 non-https URL 触发门户 > Network > Analytics > Clients > Actions > Kick Off 踢出用户。
## C22. Stellar AP 侧 Wi-Fi 故障诊断命令集
- 页码：<<<PAGE 397>>>–<<<PAGE 400>>>、<<<PAGE 426>>>–<<<PAGE 430>>>
- 命令（support 登录）：
  - `iwconfig`（ESSIN/频率/功率/信号）
  - `iwlist ath01 channel | txpower | bitrate`
  - `ssudo sta_list`（客户端 + VLAN + Final_role）
  - `wlanconfig ath01 list`
  - `ssudo wam_debug sta_list`（JSON：assignedVLAN / assignedAR / 各认证来源）
  - `cat /proc/kes_syslog | grep "<MAC>"`（客户端日志）
  - 802.1X 排查：`cat /var/config/wlanservice.conf`、`cat /var/config/AAA_profile.conf`、`cat /var/config/AAA_server.conf`；抓包 `tcpdump -i br-wan -s 0 host radiusIP`
  - Captive Portal：`ps |grep eag`、`eag_cli show user all`、`eag_cli kick user index 1`、`tail -f /tmp/log/eag.log`
## C23. 设备未在 Cirrus 出现的分层排障流程
- 页码：<<<PAGE 347>>>–<<<PAGE 348>>>（交换机）、<<<PAGE 358>>>–<<<PAGE 360>>>（AP）
- 步骤：L2 查线缆（`show interfaces 1/1/5`）→ 查 VLAN（`show vlan members port`）→ 查 PoE（`show lanpower slot 1/1`）→ L3 查 IP 接口（`show ip interface`）→ ping 激活域名 `ping eu.activation.ovng.myovcloud.com` → AP 侧 `getmode`（须 OVNG）、`cat /etc/config/network`（proto 须 dhcp）、`getovinfo` → Cirrus 侧 Action > Diagnostic Tools > View Activation Log。
## C24. OV Cirrus 运维：计划升级 / 支持信息收集 / 设备排障命令
- 页码：<<<PAGE 451>>>–<<<PAGE 456>>>
- 步骤：
  - Scheduled Upgrades 四步：Schedule Setting（occurrence/时长 6h）> AP Groups Selection > Set Software Version（统一或分组）> Review。
  - Collect Support Info：AP 一键 tar.gz；交换机可选 swlog/cfg/Tech Support L2/L3/Engineering。
  - Device Troubleshooting：Assign Command > 选设备 > 选命令（如 setDateTime）> 编辑参数 > 等待回显。
## C25. AOS 镜像升级实操命令链
- 页码：<<<PAGE 469>>>
- 命令：`-> update uboot cmm all file u-boot.8.4.1.R03.141.tar.gz` → `-> update fpga-cpld cmm all file fpga_kit_3312` → `-> reload from working no rollback-timeout` → 验证后 `-> copy running certified`、`-> show running-directory`。
## C26. Lightning Config 完整实操（含模板导入）
- 页码：<<<PAGE 481>>>–<<<PAGE 490>>>
- 步骤：笔记本设 DHCP > 网线接交换机 port 1 > 上电等 3 分钟 > Chrome 访问 `https://192.168.0.1/`（本机获 192.168.0.200）> admin/switch + 接受自签证书 > RECOMMENDED DEFAULTS > LIGHTNING CONFIG 填 IP/网关 > 改 admin 密码（8 位+大小写+数字+特殊字符，勿用 ! 或 $）> 保存为 working > 主页 PoE Port Configuration 查受电状态；模板法：IMPORT .json 模板 > Lightning Config > SAVE CONFIGURATION。
## C27. PoE 端口级配置命令组
- 页码：<<<PAGE 150>>>–<<<PAGE 154>>>
- 命令：
  - `-> show powersupply`
  - `-> lanpower slot 1/1 service start`
  - `-> lanpower port 1/1/1 admin-state enable`（默认 disabled）
  - `-> lanpower port 1/1/24 power 18000`（mW 上限）
  - `-> lanpower slot 1/1 maxpower 400`（W）
  - `-> lanpower port 1/1/6 priority critical`
  - `-> lanpower slot 1/1 capacitor-detection enable`、`-> lanpower slot 1/1 priority-disconnect enable`
  - `-> lanpower slot 1/1 delayed-start enable seconds 120`
  - `-> lanpower fpoe enable / lanpower ppoe enable`（<<<PAGE 144>>>–<<<PAGE 145>>>）
## C28. STP/LACP 配置命令组
- 页码：<<<PAGE 243>>>–<<<PAGE 247>>>、<<<PAGE 253>>>–<<<PAGE 255>>>
- 命令：
  - `-> spantree mode {flat | per-vlan}`；`-> spantree [cist|vlan id] protocol {stp|rstp|mstp}`
  - `-> spantree vlan 20 priority 20000`；`-> spantree vlan 200 port 2/1/1 priority 15`
  - `-> spantree path-cost-mode auto|32bit`
  - 监控：`show spantree`、`show spantree vlan 20 ports active`、`show spantree ports`
  - 静态聚合：`-> linkagg static agg <n> size <s> admin-state enable` + `-> linkagg static port <c/s/p> agg <n>`
  - LACP：`-> linkagg lacp agg <n> size <s> admin-state enable` + `-> linkagg lacp agg <n> actor admin-key <k>` + `-> linkagg lacp port <c/s/p> actor admin-key <k>`
  - VLAN 挂聚合口：`-> vlan <vid> members linkagg <n> tagged|untagged`（<<<PAGE 255>>>）
## C29. OV Cirrus 许可订阅创建步骤
- 页码：<<<PAGE 297>>>–<<<PAGE 300>>>
- 步骤：eBuy 下单（Other Services & Items 填许可号+数量）> Subscription Manager 选 OmniVista CIRRUS > Your purchased licenses > Create a subscription（选数量、填客户唯一名/国家）> 记录 Subscription ID + Order ID > OVC UI 导入。
- 注意："The licenses purchased in eBuy can take up to 24h before coming up in Subscription Manager."
## C30. R-Lab 环境重置脚本与实验基线
- 页码：<<<PAGE 89>>>–<<<PAGE 92>>>
- 步骤：桌面 Reset_PodX 快捷键一键重置全部设备（交换机约 5 分钟、AP 约 1.5–2 分钟）> WifiClientX（user/superuser）> Clean Wireless Networks 清除已保存无线配置；DHCP 规划：VLAN10 管理 192.168.10.70-79 / VLAN20 员工 192.168.20.70-79 / VLAN30 访客 192.168.30.70-79（<<<PAGE 88>>>）。

## counter-examples

## CE01. R-Lab 默认配置不是空配置，重置后所有端口被禁用
- 页码：<<<PAGE 89>>>
- 原文摘录（WARNING）："THE OMNISWITCH SWITCHES DEFAULT CONFIGURATION IS NOT AN EMPTY CONFIGURATION! WHEN CLICKING ON THE SHORTCUT: A SPECIFIC CONFIGURATION IS APPLIED TO THE SWITCHES, ALL THE INTERFACES ARE DISABLED. DURING THE NEXT LABS, IT WILL BE ASKED TO ENABLE THE INTERFACES THAT YOU WILL USE."
- 陷阱：以为重置=干净出厂；实际端口全 disabled，不通时先 `interfaces x admin-state enable`。
## CE02. 不要把实验室交换机恢复真出厂配置
- 页码：<<<PAGE 105>>>
- 原文摘录（Warning）："DON'T TEST THE FOLLOWING PART ON YOUR LAB! THE SWITCHES … ARE LOADED WITH A SPECIFIC DEFAULT CONFIGURATION. REINITIALIZING THEM TO THEIR FACTORY DEFAULT CONFIGURATION MAY LEAD TO ISSUES!"
- 陷阱：教学/托管环境里 `rm vcboot.cfg` + reload 会破坏预置基线。
## CE03. `reload all` 无条件从 certified 启动
- 页码：<<<PAGE 132>>>
- 原文摘录（Warning）："IF THE OMNISWITCH IS REBOOTED WITH THE 'RELOAD ALL' COMMAND, IT WILL REBOOT FROM THE CERTIFIED DIRECTORY, NO MATTER WHAT THE CONTENT OF THE RUNNING DIRECTORY IS"
- 陷阱：用 `reload all` 验证新配置会回退到 certified 旧配置；应用 `reload from working no rollback-timeout`。
## CE04. 未保存配置时断电/重启即丢失
- 页码：<<<PAGE 133>>>
- 原文摘录（Warning）："IF THE OMNISWITCH IS REBOOTED NOW …, ALL THE CHANGES IN THE RUNNING CONFIGURATION WILL BE OVERWRITTEN … IN OUR CASE, THE VLAN 2, 3 AND 99 WILL BE LOST"
- 陷阱：RAM 中的 VLAN 修改未 `write memory`，重启即丢。
## CE05. Certified 运行模式下无法保存任何修改
- 页码：<<<PAGE 135>>>
- 原文摘录：`write memory` 返回 "ERROR: Write memory is not permitted when switch is running in certified mode"
- 陷阱：从 certified 启动后做配置全部白做；须先 `modify running-directory working` 或换启动目录。
## CE06. AP 加入 AP Group 后本地配置被清除
- 页码：<<<PAGE 266>>>
- 原文摘录（Warning）："WHEN AN OMNIACCESS STELLAR ACCESS POINT GETS IN AN AP GROUP, ITS CONFIGURATION IS DELETED AND REPLACED BY THE CONFIGURATION SENT FROM THE PRIMARY VIRTUAL MANAGER (PVM) ACCESS POINT."
- 陷阱：单点调好的 AP 一旦成组，配置被 PVM 下发的组配置覆盖。
## CE07. Raspberry Pi 有线网卡不可触碰
- 页码：<<<PAGE 85>>>（原文页 2000–2003 行对应 Lab 文档页 6）
- 原文摘录（Warning）："Never touch the Ethernet card (configuration or disconnection), because it is from the wired network that you can join the raspberry pi desktop."
- 陷阱：误改/误拔树莓派有线口会直接失联。
## CE08. "Hunting Group Busy" = 控制台会话被占用
- 页码：<<<PAGE 82>>>
- 原文摘录（Tips）："If you get a message 'Hunting Group Busy' when you open a TeraTerm console, it means that another TeraTerm session has already been opened (from your account or another account)."
- 陷阱：不是设备故障，是并发 console 占用。
## CE09. Firefox 剪贴板问题导致实验指南无法粘贴
- 页码：<<<PAGE 79>>>
- 原文摘录："Other web browser may have some issue with copy/paste from a lab guide to the remote terminal session. Known workaround for FireFox: https://sudoedit.com/firefox-async-clipboard/"
- 陷阱：推荐 Chrome/Edge 访问 R-Lab。
## CE10. 不要删除 OV Cirrus 组织
- 页码：<<<PAGE 340>>>
- 原文摘录（Warning）："DO NOT use the action Delete on your Organization."
- 陷阱：MSP 视图下误删组织不可恢复。
## CE11. Captive Portal 重定向需要 non-https URL
- 页码：<<<PAGE 422>>>
- 原文摘录（Notes）："you have to open your web browser manually and open any non-https URL to be redirected to the Captive Portal"（Debian 树莓派不会自动弹门户）
- 陷阱：访问 https 站点不会触发重定向，易误判门户故障。
## CE12. 访客账号字段区分大小写
- 页码：<<<PAGE 226>>>
- 原文摘录："The username and password fields are case sensitive (ex. The username 'Guest' is different than 'guest')"
- 陷阱：大小写不一致导致门户登录失败。
## CE13. Lightning Config 前禁止把新交换机接入网络/互联
- 页码：<<<PAGE 477>>>、<<<PAGE 486>>>
- 原文摘录："Do not pre-cable the ALE switch to the network. / Do not connect the ALE switch to any other switch. / Do not connect the ALE switch to a DHCP server."；"Never connect an out-of-box ALE switch to another without running Lightning Config first."
- 陷阱：多台未配置交换机同网段会 IP 冲突（默认都是 192.168.0.1）；另外"Do NOT skip the Recommended Defaults!"（<<<PAGE 484>>>）。
## CE14. 物理环路未做防环会拖垮全网
- 页码：<<<PAGE 494>>>
- 原文摘录："Physical loops in networks can be very bad … cause communication … to continually circle the network and slow down or even halt effective communication. … please STOP and consult with the solution architect to ensure they have implemented loop avoidance"
- 陷阱：按模板接线出现环路前必须确认 STP 等防环已启用。
## CE15. AP1101 / AP1201L/H/HL 不支持 OV Cirrus 云管
- 页码：<<<PAGE 290>>>
- 原文摘录："All Stellar models supported, except: AP1101, AP1201L/H/HL. Software version: AWOS 4.0.6 GA or higher"
- 陷阱：老/入门 AP 型号或低版本 AWOS 无法上云。
## CE16. OS2360（AOS 5.2）无法 onboard 到 Cirrus
- 页码：<<<PAGE 337>>>
- 原文摘录："We can onboard in OVC only switches with AOS 8.9R1 or higher so we can't onboard OmniSwitch 2360 AOS 5.2."
- 陷阱：AOS 版本低于 8.9R1 的交换机只能 CLI 管理，VLAN 需手工配置。
## CE17. cloudagent.cfg 缺失则交换机无法注册 Cirrus
- 页码：<<<PAGE 338>>>
- 原文摘录（Warning）："IF THE FILE IS NOT PRESENT, TYPE THE FOLLOWING COMMAND TO COPY IT FROM A BACKUP DIRECTORY: -> cp /flash/cirrus/cloudagent.cfg /flash/working/cloudagent.cfg"
- 陷阱：working 目录丢文件时激活服务器 URL 丢失。
## CE18. FPoE/PPoE 与 delayed-start 互斥；P10A 不支持 FPoE/PPoE
- 页码：<<<PAGE 154>>>、<<<PAGE 144>>>–<<<PAGE 145>>>
- 原文摘录："Fpoe and Ppoe is not supported on enabling this feature (delayed-start)."；"Note: OS6360 – P10A does not support FPoE / PPoE"
- 陷阱：特性组合与具体子型号限制，规划供电时须核对。
## CE19. 升级窗口内设备不可用、客户端断线
- 页码：<<<PAGE 452>>>
- 原文摘录："when a device is upgraded, it will reboot with the new image. It will then become unavailable during this upgrade duration and all the end clients connected to this device will be disconnected."
- 陷阱：计划升级需安排在业务空闲时段。
## CE20. 多 AP 同时默认 IP 192.168.1.254 会冲突
- 页码：<<<PAGE 101>>>
- 原文摘录："By default, all the OmniAccess Stellar AP have the same administration IP address (192.168.1.254)."
- 陷阱：静态管理多台新 AP 前必须逐台改 IP 或直接依赖 DHCP；AP 改 IP 后旧地址访问失效（<<<PAGE 103>>>）。
## CE21. boot.md5 拷贝报 Permission denied 属正常
- 页码：<<<PAGE 136>>>
- 原文摘录（Tips）："it tries to copy the boot.md5 file but a 'permission denied' message is displayed. This file is auto generated so ignore this error and proceed."
- 陷阱：复制 working 目录到 user 目录时的预期报错，不代表复制失败。

## frameworks

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

## glossary

1. **OmniSwitch** — ALE 的 LAN 交换机产品线，覆盖接入/汇聚/核心（<<<PAGE 11>>>）。
2. **OmniSwitch 6360** — Value 级 AOS L2+ 千兆接入交换机，本课程主力实验机型（<<<PAGE 12>>>）。
3. **OmniSwitch 2360** — WebSmart L2 入门交换机，运行 AOS 5.2，不能上 Cirrus（<<<PAGE 13>>>、<<<PAGE 337>>>）。
4. **OmniSwitch 6870** — 新一代 Advanced L3 交换机，支持 10/25/40/50/100G 上联（<<<PAGE 12>>>）。
5. **OmniSwitch 6900 / 9900** — 汇聚/核心与模块化机箱旗舰（<<<PAGE 12>>>）。
6. **OmniAccess Stellar** — ALE 无控制器架构 Wi-Fi AP 产品族，覆盖 Wi-Fi 6/6E/7（<<<PAGE 16>>>–<<<PAGE 18>>>）。
7. **AP1301 / AP1311** — Wi-Fi 6 入门级 AP，2x2:2 双频 + 扫描射频（<<<PAGE 26>>>、<<<PAGE 28>>>）。
8. **AP1321/1322** — Wi-Fi 6 中端 AP；尾号 2 支持外置天线（<<<PAGE 29>>>、<<<PAGE 41>>>）。
9. **AP1301H** — 酒店/宿舍场景 Wi-Fi 6 AP，带 4 个下行 GE 口与 PoE 下行（<<<PAGE 27>>>）。
10. **AP1351 / AP1451** — Wi-Fi 6 / 6E 高端三射频 AP，8x8:8 5GHz（<<<PAGE 31>>>、<<<PAGE 35>>>）。
11. **AP136x** — Wi-Fi 6 户外加固 AP，-40~+65°C（<<<PAGE 32>>>）。
12. **AP1411 / AP1431** — Wi-Fi 6E 入门/中端 AP，6GHz 射频（<<<PAGE 33>>>、<<<PAGE 34>>>）。
13. **AP1511 / AP1521 / AP157x** — Wi-Fi 7（802.11be）AP 家族（<<<PAGE 36>>>、<<<PAGE 37>>>、<<<PAGE 18>>>）。
14. **OmniVista Cirrus (OVC)** — 云端 SaaS 网管平台，支持最多 12000 台设备（10000 AP + 2000 交换机）（<<<PAGE 286>>>、<<<PAGE 287>>>）。
15. **OmniVista 2500 / Terra** — 本地部署 NMS，对应 Enterprise 模式（<<<PAGE 11>>>、<<<PAGE 187>>>）。
16. **OV Cirrus 10 Device Catalog** — Cirrus 设备目录，管理设备申报与激活状态（<<<PAGE 308>>>）。
17. **R-Lab (Remote Labs)** — ALE 远程实验室，浏览器 RDP 接入 POD（<<<PAGE 5>>>、<<<PAGE 79>>>）。
18. **ALE Knowledge Hub / eBuy / MyPortal / Spacewalkers** — 培训平台 / 许可下单 / 合作伙伴门户 / 技术社区（<<<PAGE 8>>>、<<<PAGE 297>>>）。
19. **OmniVista Smart Tool (OST)** — 免费安装排障工具，含 PoE 向导、自动开票、流量分析（<<<PAGE 498>>>–<<<PAGE 504>>>）。
20. **OXO Connect** — ALE 中小语音平台，与 Stellar ZTP 集成（<<<PAGE 186>>>）。
21. **Rainbow** — ALE 协作云，可作为 Social Login 凭据源（<<<PAGE 369>>>、<<<PAGE 409>>>）。

## 部署模式与管理架构
22. **Express 模式（Wi-Fi Express）** — AP 自管理独立集群，最多 255 台，免许可，Web 向导配置（<<<PAGE 185>>>）。
23. **Enterprise 模式（Wi-Fi Enterprise）** — 由本地 OV2500 集中管理，最多 4000 AP（<<<PAGE 187>>>）。
24. **Cloud 模式（Wi-Fi Cloud）** — 由 OmniVista Cirrus 云管，最多 10000 AP（<<<PAGE 189>>>）。
25. **AP Group** — 同 Group ID + 同 VLAN 的 AP 自动组成的管理组，统一 Web 界面（<<<PAGE 202>>>；Cirrus 版见 <<<PAGE 277>>>）。
26. **PVM (Primary Virtual Controller)** — AP Group 中当选的主控 AP，承载统一管理界面（<<<PAGE 203>>>）。
27. **SVM (Secondary Virtual Manager)** — 备份主控，PVM 故障时接管（<<<PAGE 203>>>）。
28. **Provisioning Configuration** — Cirrus 中挂在 AP Group 下的配置档（Name/Site/RF Profile/Timezone 等）（<<<PAGE 331>>>）。
29. **Distributed Control** — 无控制器架构下 AP 间空口/LAN 直接交换漫游上下文与 RF 参数（<<<PAGE 280>>>）。
30. **Thin Client 模式** — 交换机不在本地存配置，全部从 OV2500 拉取（<<<PAGE 127>>>）。

## 认证与安全
31. **UPAM (Unified Policy Authentication Manager)** — Cirrus/OV 内嵌统一策略认证模块，含 RADIUS 服务器与 Captive Portal（<<<PAGE 188>>>、<<<PAGE 367>>>）。
32. **ASA (Authenticated Switch Access)** — 交换机管理通道认证框架，按 Console/Telnet/SSH/HTTP 等服务分别锁定（<<<PAGE 58>>>）。
33. **ARP (Access Role Profile)** — 六元组用户策略档案：VLAN/QoS/防火墙/L7 规则/位置/时段（<<<PAGE 376>>>；注意与地址解析协议 ARP 区分）。
34. **Captive Portal** — Web 认证门户，支持账号/接入码/条款/社交登录/自助注册（<<<PAGE 213>>>、<<<PAGE 409>>>）。
35. **Walled Garden** — 访客认证前即可访问的白名单站点集合（<<<PAGE 235>>>）。
36. **GuestOperator 账号** — 仅能管理访客账号的受限管理界面（<<<PAGE 234>>>）。
37. **802.1X** — 基于端口的接入认证，员工 SSID 常用（PEAP/MSCHAPv2）（<<<PAGE 211>>>、<<<PAGE 395>>>）。
38. **MAC 认证** — 按 MAC 地址到 RADIUS/UPAM 验证，可回传 Filter-ID 指定 ARP（<<<PAGE 384>>>）。
39. **Filter-ID** — RADIUS 属性，用于向 AP 下发应套用的 ARP 名（<<<PAGE 385>>>）。
40. **WPA2 / WPA3** — Wi-Fi 安全协议代际，Wi-Fi 6 起支持 WPA3（<<<PAGE 45>>>）。
41. **IEC 62443-3-3 Level 2** — 工控安全标准，8.10R3 起支持强制密码刷新（<<<PAGE 62>>>）。

## 交换机技术
42. **AOS R8** — OmniSwitch Release 8 操作系统（<<<PAGE 117>>>）。
43. **Working / Certified 目录** — Flash 中"待验证配置"与"已认证配置"双目录，支撑回滚（<<<PAGE 118>>>、<<<PAGE 131>>>）。
44. **Running Directory / Running Configuration** — 当前运行目录及 RAM 中的运行配置（<<<PAGE 131>>>）。
45. **vcboot.cfg / vcsetup.cfg** — 交换机启动与设置配置文件（<<<PAGE 131>>>）。
46. **write memory flash-synchro** — 保存并同步 certified 的组合命令（<<<PAGE 122>>>）。
47. **reload all** — 无条件从 certified 目录重启的命令（<<<PAGE 132>>>）。
48. **EMP (Ethernet Management Port)** — 交换机带外管理口，直连 CMM（<<<PAGE 66>>>）。
49. **CMM** — 交换机控制/管理模块（chassis 管理大脑）（<<<PAGE 66>>>）。
50. **Virtual Chassis (VC)** — 多台物理交换机虚拟化为一台逻辑设备（<<<PAGE 12>>>）。
51. **WebView** — 交换机内嵌 Web 管理界面，默认强制 HTTPS/TLS1.2（<<<PAGE 68>>>、<<<PAGE 69>>>）。
52. **Lightning Config (OLC)** — 开箱 5 分钟级快速配置向导，默认 IP 192.168.0.1（<<<PAGE 73>>>、<<<PAGE 475>>>）。
53. **Fast PoE (FPoE)** — 上电数秒内即向 PD 供电，不等系统完全启动（<<<PAGE 144>>>）。
54. **Perpetual PoE (PPoE)** — 交换机软重启期间对 PD 不断电（<<<PAGE 145>>>）。
55. **Delayed-start** — lanpower 延迟启动（120–600s）以等系统稳定（<<<PAGE 154>>>）。
56. **EEE (802.3az)** — 能效以太网，空闲低功耗，仅铜缆 100/1000M（<<<PAGE 146>>>）。
57. **PoE Class** — PD 功率等级，Class 1–8（bt Type 4），决定预算分配（<<<PAGE 147>>>）。
58. **802.1Q** — VLAN 打标标准，12bit VID 共 4096 个（<<<PAGE 165>>>、<<<PAGE 166>>>）。
59. **802.1p** — 802.1Q 头内 3bit 优先级字段，8 级 CoS（<<<PAGE 166>>>）。
60. **VLAN Mobile Tag** — 允许移动端口接收带标签帧并按 VID 动态入组，优先级高于其他 VLAN 规则（<<<PAGE 169>>>）。

## 无线与网络协议
61. **SSID** — 无线网络服务标识（网络名），与 VLAN 映射实现用户分流（<<<PAGE 215>>>）。
62. **mywifi-XXXX** — Stellar AP 出厂默认 SSID（MAC 后四位），默认管理 IP 192.168.1.254:8080（<<<PAGE 199>>>）。
63. **DHCP Option 138** — DHCP 下发 OV2500 地址、引导 AP 进 Enterprise 模式的选项（<<<PAGE 198>>>；Cirrus 代理场景见 <<<PAGE 290>>>）。
64. **MU-MIMO** — 多用户多入多出，Wi-Fi 5 起的下行、Wi-Fi 6 起上下行（<<<PAGE 45>>>）。
65. **MLO (Multi-Link Operation)** — Wi-Fi 7 多链路操作，提升可靠性与时延（<<<PAGE 44>>>）。
66. **AFC (Automated Frequency Coordination)** — Wi-Fi 7 标准 6GHz 自动频率协调（<<<PAGE 44>>>）。
67. **BLE / Zigbee** — AP 内置 IoT 射频技术，用于物联网与定位（<<<PAGE 28>>>）。
69. **WIDS / WIPS** — 无线入侵检测/防护，含 Rogue 遏制（<<<PAGE 188>>>）。
71. **Path Cost** — STP 端口路径开销，16bit/32bit 两套标准值（<<<PAGE 239>>>）。
72. **LACP (802.3ad)** — 链路聚合控制协议，LACPDU 协商动态聚合（<<<PAGE 252>>>）。
73. **Linkagg / admin-key** — AOS 聚合组及其端口归属键（<<<PAGE 254>>>）。
74. **Hash-control (brief/extended)** — 聚合/ECMP 负载分担哈希算法选择（<<<PAGE 259>>>）。
75. **cloud-agent** — 交换机上负责呼叫 Cirrus 激活服务器的代理进程（<<<PAGE 314>>>）。
76. **Call Home / Discovery Interval** — 设备周期性联系云管的机制，默认 30 分钟（<<<PAGE 314>>>）。
77. **OV Managed** — Cirrus 激活状态机的最终态，表示完全受管（<<<PAGE 310>>>）。
78. **ocloud_show** — Stellar AP 侧查看云连接状态的 CLI 命令（<<<PAGE 327>>>、<<<PAGE 357>>>）。
79. **QoE Analytics** — Cirrus 中来自设备的体验质量分析事件流（<<<PAGE 453>>>）。
80. **Golden Config** — Cirrus 中标记为基准的运行配置，用于审计漂移（<<<PAGE 439>>>）。
81. **GRE Tunnel（Use Tunnel）** — SSID 用户经 GRE 隧道集中到远端解除的映射方式（<<<PAGE 369>>>）。
82. **PoE Injector / Midspan** — 为非 PoE 交换机环境补供电的注入器（<<<PAGE 39>>>）。
83. **Mounting Kit** — AP 天花板/墙面安装套件（<<<PAGE 40>>>）。
84. **VMS (Video Management System)** — 视频监控管理系统，Lightning Config 提供组播参数选项（<<<PAGE 74>>>、<<<PAGE 492>>>）。
85. **RCL (Remote Configuration Load)** — 交换机远程配置加载服务器，存在时 Lightning Config 不触发（<<<PAGE 75>>>）。

## principles

## P01. PoE 四标准功率等级对照
- 页码：<<<PAGE 147>>>
- 原文摘录："802.3af (Type 1) 'PoE': Power available at the PD 12.95 W, Max delivered 15.40 W, 350 mA, Three power class levels (1-3) / 802.3at Type 2 'PoE+': 25.50 W / 30.0 W / 600 mA, Four class (1-4) / 802.3bt Type 3: 51 W / 60 W, Six class (1-6) / Type 4: 71 W / 100 W, Eight class (1-8)"
- 提取内容：PD 可用功率 / PSE 最大供给 / 电流 / 等级数四栏对照，PoE 预算计算的基础。
## P02. PoE 端口优先级与断电顺序
- 页码：<<<PAGE 151>>>
- 原文摘录："Low: inline power to low-priority ports is interrupted first / Critical: inline power to critical ports is maintained as long as possible"
- 提取内容：功耗超预算时按 Low → High → Critical 顺序断电；关键设备（如 AP 上联口）应设 critical。
## P03. PoE 动态分配与型号标识
- 页码：<<<PAGE 147>>>、<<<PAGE 148>>>
- 原文摘录："Dynamic PoE Allocation: Provide only the amount of power needed by powered devices (PD) up to the total energy budget"；"OmniSwitches models compatibles with the PoE protocol have the « P » letter in their reference."
- 提取内容：型号带 P 才支持 PoE；按 PD 实际需求动态供电提高总预算利用率。
## P04. EEE（802.3az）适用边界
- 页码：<<<PAGE 146>>>
- 原文摘录："EEE is only applicable to OmniSwitch copper ports operating at 100/1000 Mbps speed"，且不兼容光口"U"机型。
- 提取内容：空闲低功耗仅限铜缆 100/1000M 端口。
## P05. 电容检测法仅限 legacy 话机
- 页码：<<<PAGE 152>>>
- 原文摘录："Not compatible with IEEE specification 802.3af. It should only be enabled to support legacy IP phones"
- 提取内容：capacitor-detection 是非标检测，只用于老式 IP 话机，默认不开启。
## P06. OmniSwitch 交换机默认凭据与强制改密策略
- 页码：<<<PAGE 60>>>、<<<PAGE 61>>>
- 原文摘录："Default login name and password: Login: admin, Password: switch"；"Beginning in 8.10R3 a warning message will be displayed … Beginning in 8.10R4 changing the default password will be mandatory."
- 提取内容：admin/switch 默认凭据；8.10R3 起告警、8.10R4 起强制修改。本地用户库 userTable9 存于 flash/system，最多 64 用户。
## P07. ASA 认证服务禁用语义
- 页码：<<<PAGE 58>>>、<<<PAGE 59>>>
- 原文摘录："Authenticated Switch Access (ASA) feature: Lock or Unlock session types (aaa authentication command)"；示例 `-> no aaa authentication http` 后 "Service type = Http, Authentication = denied"
- 提取内容：Console/Telnet/FTP/HTTP/SSH/SNMP 各管理通道独立开关；默认 Console+Default 走 local 库。
## P08. exit-on-fail 与多服务器 fail-through
- 页码：<<<PAGE 63>>>
- 原文摘录："aaa authentication {console | telnet | …} server1 [server2...] [local] [exit-on-fail {enable | disable}]"；"When enabled, the switch uses only the first available server in the list … When disabled, the switch uses all the available servers"
- 提取内容：exit-on-fail 启用时只查首台可用服务器，禁用时逐台回退（fail-through）。
## P09. WebView 嵌入式管理与安全默认
- 页码：<<<PAGE 68>>>、<<<PAGE 69>>>
- 原文摘录："The WebView application is embedded in the switch and is accessible via a web browser"；"webview force-ssl enable: Forces SSL connection between browser and switch (default=enabled)"，TLS 1.2（<<<PAGE 109>>>）
- 提取内容：WebView 内嵌于交换机、仅限单机视图，默认强制 HTTPS。
## P10. 并发会话数上限
- 页码：<<<PAGE 67>>>
- 原文摘录："Telnet 6 / FTP 4 / SSH + SFTP 8 / HTTP 4 / Total sessions 20 / SNMP 50"
- 提取内容：各类管理会话的规格上限。
## P11. EMP 带外管理口原理
- 页码：<<<PAGE 66>>>
- 原文摘录："Bypass the network interface modules (NI) … Remotely manage the switch directly via the CMM"；`ip interface master emp address 172.25.167.203 mask 255.255.255.224`
- 提取内容：EMP 绕过业务端口直连 CMM 的带外管理通道；无 EMP 机型可用 USB Ethernet Dongle 等效。
## P12. Console 默认串口参数
- 页码：<<<PAGE 65>>>
- 原文摘录："Speed (baud): 115200 / Parity: None / Stop bits: 1 / Flow control: none"（新一代 6900/6860N 速率不同）
- 提取内容：Tera Term/Putty 连接交换机 console 的标准参数。
## P13. AOS 启动序列（Bootrom → 镜像选择 → RAM 加载）
- 页码：<<<PAGE 119>>>
- 原文摘录："Bootstrap Basic Operation (U-Boot) / Hardware Initialization / Memory Diagnostics / Image selection / AOS is copied and loaded into RAM"
- 提取内容：U-Boot 引导 → 硬件初始化 → 内存诊断 → 镜像选择 → 拷入 RAM 运行。
## P14. 冷启动目录选择规则与 reload all 特例
- 页码：<<<PAGE 132>>>
- 原文摘录："The switch will reboot from certified directory if contents are different from the running directory … IF THE OMNISWITCH IS REBOOTED WITH THE 'RELOAD ALL' COMMAND, IT WILL REBOOT FROM THE CERTIFIED DIRECTORY, NO MATTER WHAT"
- 提取内容：内容一致从 running 启动，不一致回退 certified；`reload all` 无条件从 certified 启动。
## P15. 从 Certified 目录运行时无法保存配置
- 页码：<<<PAGE 124>>>、<<<PAGE 135>>>
- 原文摘录："When the switch boots from the CERTIFIED directory, changes made to the switch cannot be saved"；`write memory` 报 "ERROR: Write memory is not permitted when switch is running in certified mode"
- 提取内容：certified 运行模式为只读保护，需 `modify running-directory` 切回可写目录。
## P16. write memory flash-synchro 组合语义
- 页码：<<<PAGE 122>>>
- 原文摘录："write memory flash-synchro = write memory + copy running certified"
- 提取内容：一步完成保存 + 认证同步。
## P17. USB 自动备份机制
- 页码：<<<PAGE 126>>>、<<<PAGE 138>>>
- 原文摘录："switch will store image files, power supply and system configuration files to USB storage drive automatically upon user commands 'write memory' or 'copy running-certified' … if USB backup is enabled"；可设密码加密备份内容
- 提取内容：启用后写配置即自动镜像到 /uflash。
## P18. Thin Client 模式（零配置交换机）
- 页码：<<<PAGE 127>>>
- 原文摘录："No configuration is stored on the switch. It will contact OmniVista 2500 to retrieve the config. … 'write memory' can be executed but configurations will not be saved"
- 提取内容：配置全量由 OV2500 下发，本地仅保留最小网络可达配置。
## P19. CLI 内建辅助（补全/过滤/历史/帮助）
- 页码：<<<PAGE 128>>>
- 原文摘录："Completion: Recognize partial keywords … Eg: sh vl for show vlan"；"-> show mac-learning | grep 00:20:da:55:56:76"；`?` 在线帮助
- 提取内容：AOS CLI 的效率特性集合。
## P20. VLAN 广播域划分与端口入组四途径
- 页码：<<<PAGE 158>>>
- 原文摘录："Ports become members of VLANs by: Static Configuration / Mobility with or without Authentication / 802.1q / VLAN Mobile Tag"
- 提取内容：VLAN 逻辑分段 LAN，端口成员有静态、移动、802.1Q、Mobile Tag 四种来源。
## P21. 默认 VLAN 与静态端口分配
- 页码：<<<PAGE 159>>>、<<<PAGE 160>>>
- 原文摘录："By default, all ports belong to VLAN 1"；`vlan 2 members port <slot>/<port> untagged`
- 提取内容：untagged 即端口的 default VLAN；多词 VLAN 名需引号。
## P22. VLAN 间路由触发条件
- 页码：<<<PAGE 162>>>
- 原文摘录："IP routing is active as soon as at least one IP interface is associated with a VLAN"；`ip interface <name> address <ip/mask> vlan <vlan_id>`
- 提取内容：任一 VLAN 绑定 IP 接口即激活三层路由（虚拟路由器网关模式）。
## P23. 802.1Q 标签结构与地址空间
- 页码：<<<PAGE 166>>>
- 原文摘录："4096 unique VLAN Tags (addresses) / VLAN ID == GID == VLAN Tag / 802.1P: Three bits field within 802.1Q header, Allows up to 8 different priorities"
- 提取内容：4 字节标签 = 12bit VLAN ID + 3bit 802.1p 优先级。
## P24. Mobile Tag 与 802.1Q 的分工
- 页码：<<<PAGE 170>>>
- 原文摘录："VLAN Mobile Tag: Allows mobile ports to receive 802.1Q tagged packets … Takes precedence over all VLAN Rules / 802.1Q Tag: Not supported on mobile ports"
- 提取内容：固定端口用 802.1Q 静态打标；移动端口靠 Mobile Tag 按 VID 动态归类且优先级最高。
## P25. STP 双模式三协议与收敛时间
- 页码：<<<PAGE 238>>>
- 原文摘录："flat (single STP instance per switch) / per-VLAN (single STP instance per VLAN) (By default on OmniSwitch) … STP (802.1d): Convergence time: 50 secs / RSTP (802.1w): < 1 sec / MSTP (802.1s): < 1 sec"
- 提取内容：OmniSwitch 默认 per-VLAN 模式；协议收敛 50s vs <1s。
## P26. STP 默认路径开销（16bit/32bit）
- 页码：<<<PAGE 239>>>
- 原文摘录："10 Mbps 100/2,000,000 … 1 Gbps 4/20,000 … 10 Gbps 2/2,000"（16bit 用于 STP/RSTP，32bit 用于 MSTP）
- 提取内容：两种开销体系随协议自动切换（`spantree path-cost-mode auto`，<<<PAGE 247>>>）。
## P27. per-VLAN STP 负载分担手法
- 页码：<<<PAGE 240>>>
- 原文摘录："per vlan (1x1) - load balancing … spantree vlan 20 priority 20000" 后 VLAN 20 根桥迁移到 SW-C
- 提取内容：按 VLAN 调 bridge priority 可让不同 VLAN 的阻塞端口错开，实现环路链路负载分担。
## P28. LACP 动态聚合协商原理
- 页码：<<<PAGE 252>>>
- 原文摘录："Dynamic: IEEE 802.3ad LACP. LACP will negotiate the optimal parameters for both ends using LACPDU … It also works between two different devices"；"Static: Only works between Alcatel-Lucent OmniSwitches"
- 提取内容：静态聚合仅限 ALE 互通；LACP 跨厂商、经 LACPDU 协商最优参数。
## P29. 哈希负载均衡算法 brief/extended
- 页码：<<<PAGE 259>>>
- 原文摘录："Brief Mode: UDP/TCP ports not included … Extended: UDP/TCP ports to be included in the hashing algorithm. Result in more efficient load balancing"；各机型默认值表（6360/6465/6900=brief，其余=extended）
- 提取内容：`hash-control extended` 引入四层端口提高分担均匀度。
## P30. 聚合口组播分担默认行为
- 页码：<<<PAGE 260>>>
- 原文摘录："Multicast traffic is by default forwarded through the primary port of the Link Aggregation Group … enable hashing for non-unicast traffic"
- 提取内容：组播默认走主端口，需显式开启 non-ucast 哈希才全组分担。
## P31. Wi-Fi 6 核心改进
- 页码：<<<PAGE 43>>>
- 原文摘录："Increased network throughput / Increased efficiency in dense environments / Increased robustness outdoors / Reduced power consumption / Enhanced Wi-Fi coexistence / Reduced overhead"
- 提取内容：Wi-Fi 6 面向高密与 IoT 场景的六项改进。
## P32. Wi-Fi 7 关键新技术
- 页码：<<<PAGE 44>>>
- 原文摘录："Multi Link Operation (MLO) … 4096-QAM … 320 MHz … Multi Resource Unit (MRU) … Preamble Puncturing … Automated Frequency Coordination (AFC)"
- 提取内容：MLO、4096-QAM、320MHz 信道等 Wi-Fi 7 特性清单（46 Gbps vs Wi-Fi 6E 9.6 Gbps）。
## P33. Stellar AP 出厂默认行为
- 页码：<<<PAGE 199>>>
- 原文摘录："BROADCASTS A SSID 'MYWIFI-ABCD' WITH ABCD = LAST BYTES OF THE AP MAC@ / HAS THE IP@ = 192.168.1.254 (OR AN IP@ RECEIVED FROM THE DHCP SERVER)"；Web 管理口 `HTTP://<IP@ OF THE AP>:8080`
- 提取内容：开箱即广播 mywifi-XXXX（MAC 后四位），默认管理 IP 192.168.1.254，端口 8080。
## P34. AP Group 自动成组条件与默认 Group ID
- 页码：<<<PAGE 202>>>
- 原文摘录："OmniAccess Stellar Access Points with the same group identifier (Group ID) and the same VLAN are automatically placed in the same group … Initial Settings: Identical Group ID (Group ID 100), Identical default VLAN (VLAN 1)"
- 提取内容：同 Group ID + 同 VLAN = 自动成组；出厂 Group ID 100。
## P35. PVM/SVM 角色与选举
- 页码：<<<PAGE 203>>>
- 原文摘录："a Stellar AP is elected PVM (Primary Virtual Controller). The PVM manages all the Group … SVM (Secondary Virtual Manager) to replace the PVM in case of failure … Criteria 1: highest Stellar AP model / Criteria 2: highest MAC address"
- 提取内容：主备虚拟控制器双准则选举，统一 Web 界面挂在 PVM 上。
## P36. SSID→VLAN 自动映射
- 页码：<<<PAGE 215>>>
- 原文摘录："A predefined VLAN is automatically assigned to a client when it connects to an SSID"
- 提取内容：客户端按接入 SSID 自动落入预定义 VLAN（Employees→VLAN10、Guests→VLAN20 的示例）。
## P37. AP 内置 DHCP/DNS/NAT 服务
- 页码：<<<PAGE 216>>>
- 原文摘录："DHCP, DNS & NAT services integrated in all the OmniAccess Stellar Access Points"
- 提取内容：无控制器架构下 AP 自带三件套基础网络服务。
## P38. AP 内置 QoS/ACL 与三角色用例
- 页码：<<<PAGE 217>>>
- 原文摘录："Employees VLAN 10, Access: All, Bandwidth: High, Priority: Normal / Guests VLAN 20, Access: internet only, Bandwidth: Normal, Priority: Low / Phones VLAN 30, Access: Voice, Bandwidth: Low, Priority: High"
- 提取内容：按用户类型（员工/访客/话机）做 VLAN+带宽+优先级三维差异化策略。
## P39. 访客 Captive Portal 三种认证方式
- 页码：<<<PAGE 226>>>
- 原文摘录："the authentication type must be selected (account, access code, or terms of use)"；"The username and password fields are case sensitive"
- 提取内容：账号 / 接入码 / 使用条款三选一；账号字段区分大小写，可设有效期。
## P40. UPAM 统一策略认证模块定位
- 页码：<<<PAGE 367>>>（另见 <<<PAGE 188>>>、<<<PAGE 392>>>）
- 原文摘录："THE UPAM MODULE (UNIFIED POLICY AUTHENTICATION MANAGER) PROVIDES A CENTRALIZED MANAGEMENT OF THE ACCESS RULES. THE UPAM ALSO EMBEDS A RADIUS SERVER AND A CAPTIVE PORTAL."
- 提取内容：OV Cirrus 内嵌的统一接入管理平台，同时充当 RADIUS 服务器与 Captive Portal，覆盖 MAC/802.1X/Portal 三类认证。
## P41. ARP（Access Role Profile）属性构成
- 页码：<<<PAGE 376>>>
- 原文摘录："ARP = Access Role Profile: VLAN TAG / QOS POLICY / FIREWALL RULES (ACLS) / L7 APPLICATION RULES / LOCATION / PERIOD"
- 提取内容：六元组用户策略档案（VLAN、QoS、防火墙、L7 应用、位置、时段）。
## P42. Stellar AP LED 状态语义
- 页码：<<<PAGE 52>>>
- 原文摘录："Green blinking: System started up, Default SSID broadcasted / Blue: Dual band 2.4 GHz AND 5 GHz / Blue & Red blinking: Software Update / Blue/Red/Green blinking: AP Localization / Red: System startup"
- 提取内容：LED 颜色/闪烁模式与 AP 运行状态对照（AP136x 独立 LED 表见 <<<PAGE 54>>>）。
## P43. 交换机面板 OK/PWR LED 语义
- 页码：<<<PAGE 50>>>
- 原文摘录："OK1 Green: System Diagnostic & Startup OK / Blinking Green: pending / Amber: NOK / PWR Green: Power supply OK / Blinking Green: power supply present, but malfunction"
- 提取内容：启动自检与电源状态的双 LED 判读法。
## P44. PoE 端口 LED 判读
- 页码：<<<PAGE 143>>>
- 原文摘录："Amber: Device connected, Device powered with PoE / Green: Device connected, Device not powered with PoE"
- 提取内容：琥珀=受电、绿色=连接但未受电。
## P45. OV Cirrus 网络前提（端口/DHCP 选项/版本）
- 页码：<<<PAGE 290>>>
- 原文摘录："Open Firewall ports 9093, 30123, 30124, 30125 … outbound 443, 80, 123, 53 … Enable DHCP standard options: 1, 2, 6, 28, 42, 43 … when using proxy: 129, 130, 131, 132, 133, 138 … All Stellar models supported, except: AP1101, AP1201L/H/HL … AWOS 4.0.6 GA or higher … AOS 8.9R1 or higher"
- 提取内容：上云的防火墙、DHCP option、软件版本三类前置条件。
## P46. cloud-agent 呼叫机制与激活状态机
- 页码：<<<PAGE 314>>>、<<<PAGE 309>>>–<<<PAGE 310>>>
- 原文摘录："cloud-agent discovery-interval: the time interval after which the switch will call-home the activation server, in case of any error (default= 30mns)"；激活状态流 "Registered > Obtaining Certificate > Assigned > VPN Configuring > Connected to OV > Provisioning > OV Managed"
- 提取内容：设备周期性 call-home；状态机含中间态与失败态（Failed To Get Certificate / Factory Reset Required 等）。
## P47. 分布式控制架构（空口 + 局域网交换）
- 页码：<<<PAGE 280>>>
- 原文摘录："Over the Air Exchange: Roaming client's context, MAC addresses, Keys, Access Role Profiles / Over the LAN Exchange: Radio Frequency settings, Power, Channel, RSSI"
- 提取内容：无控制器下 AP 间通过空口同步漫游上下文、通过 LAN 同步 RF 参数。
## P48. AP Group（Cirrus 版）配置继承模型
- 页码：<<<PAGE 277>>>、<<<PAGE 329>>>、<<<PAGE 331>>>
- 原文摘录："AP(s) inherits the AP Group configuration … SSIDS, FIREWALL POLICY, AUTHENTICATION POLICY, RADIOFREQUENCY POLICY"；"Mandatory Provisioning Configuration: Name, Site, RF Profile, Timezone"
- 提取内容：AP→AP Group→Provisioning Configuration 三层继承；组内可混插任意 AP 型号、上限 10000。
## P49. Walled Garden 特性
- 页码：<<<PAGE 235>>>、<<<PAGE 410>>>
- 原文摘录："provides the visitor / guest with the ability to access certain predefined websites even before authenticating (eg. Access to the hotel website possible even if the guest has not authenticated)"
- 提取内容：认证前白名单放行指定站点的访客预访问机制。
## P50. AP 外置天线命名规则
- 页码：<<<PAGE 41>>>
- 原文摘录："Access points compatible with external antennas have their reference ends with '2' (ex. AP1322, AP1362) … All OmniAccess Stellar Access Points are equipped with an internal antenna (omni-directional coverage pattern)"
- 提取内容：型号尾数 2 = 支持外置天线；其余均为内置全向天线。
