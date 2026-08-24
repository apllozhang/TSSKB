# cases 候选 — DT00XTE301 LAN & WLAN Installation & Configuration for SMB

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
