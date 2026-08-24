# Verified 候选（V1 原文真实性核对 + V2/V3 抽查）

## cases

## C2. Lab：R-Lab 设备一键复位（Reset_PodX 脚本）
- <<<PAGE 104>>>-<<<PAGE 110>>>
- 原文摘录："Reset all the R-Lab's equipment by using the Reset_PodX script … The reinitialization process takes around 5 minutes（交换机）/ around 1min30 – 2min（AP）"（<<<PAGE 108>>>）
- WARNING：复位后交换机加载的是"特定默认配置、所有端口禁用"，并非空配置（<<<PAGE 107>>>）。
## C3. Lab：交换机首次 Console 登录与端口开启
- <<<PAGE 113>>>
- 命令序列：`-> interfaces 1/1/6 admin-state enable`（AP 口）→ `-> interfaces 1/1/1 admin-state enable`（客户端口）→ `-> ip interface int_1 address 192.168.1.2/24 vlan 1` → `-> show ip interface` 验证 → `-> write memory flash-synchro`（<<<PAGE 114>>>）
## C4. Lab：Stellar AP1321 首次向导配置（改密码+建 SSID+改 IP）
- <<<PAGE 117>>>-<<<PAGE 121>>>
- 步骤：浏览器 192.168.1.254:8080 → admin/admin → Wizard 改密 superuser → 国家/时区 → 建 SSID AdminX（替换默认 mywifi-XXXX）→ AP > IP Mode > Edit 改静态 IP 192.168.1.3/网关 192.168.1.2。
## C5. AP 出厂复位两法（Reset 键 / Console firstboot）
- <<<PAGE 122>>>、<<<PAGE 376>>>
- 命令：Console 登录 support/aos2016 → `ssudo firstboot -y` → `ssudo reboot`；或"Press 6 seconds on the Reset button（until the led blinks red）"（<<<PAGE 376>>>）。
## C6. Lab：双分区目录全流程实验（建 VLAN→write memory→reload all 回滚→user 目录→certify）
- <<<PAGE 127>>>-<<<PAGE 131>>>
- 命令序列：`vlan 2/3/99` → `show running-directory`（NOT SYNCHRONIZED）→ `write memory`（CERTIFY NEEDED）→ `reload all`（回到 CERTIFIED，VLAN 丢失）→ `reload from working no rollback-timeout`（找回）→ `mkdir lab` / `cp working/*.* lab` → `reload from lab no rollback-timeout` → `copy running certified` → `modify running-directory working`。
- 实测错误："ERROR: Write memory is not permitted when switch is running in certified mode"（<<<PAGE 129>>>）
## C7. Lab：USB 备份/恢复
- <<<PAGE 132>>>-<<<PAGE 133>>>
- 命令：`usb enable` → `usb backup admin-state enable` → `write memory`（自动同步到 /uflash）→ `cd /uflash`+`ls` 验证 certified/working 两目录。
## C8. Lab：SSH/WebView 远程接入（AAA 开放）
- <<<PAGE 135>>>-<<<PAGE 139>>>
- 命令：`aaa authentication ssh local`、`aaa authentication http local` → `show webview`（Force-SSL Enabled）→ HTTPS://EMP-IP 登录 admin/switch → WebView 改 inactivity timer、建/删 VLAN 59 并 `show vlan` 验证。
## C9. PoE 管理与监控命令集
- <<<PAGE 153>>>-<<<PAGE 157>>>
- 命令组合：`show powersupply`；`lanpower slot 1/1 service start`；`lanpower port 1/1/1 admin-state enable`；`lanpower port 1/1/24 power 18000`（mW）；`lanpower slot 1/1 maxpower 400`（W）；`lanpower port 1/1/6 priority critical`；`show lanpower slot 1/1`（看 Actual Used/Power Budget）。
- 实例：AP 口 Actual Used 7000mW、Class 4（<<<PAGE 176>>>）。
## C10. Lab：PoE/VLAN/DHCP 联调（AP 改 DHCP 模式）
- <<<PAGE 177>>>-<<<PAGE 183>>>
- 命令序列：`vlan 10 name Management-AP` / `vlan 20 name Employees` / `vlan 30 name Guests` → `vlan 10 members port 1/1/3 tagged`（上行）→ `vlan 10 members port 1/1/6 untagged` + 20/30 tagged（AP 口）→ `show vlan members port 1/1/6` 验证 → AP Web 改 IP Mode=DHCP → 用 `mywifi.al-enterprise.com:8080` 域名重连。
- 验证 MAC：`show mac-learning`（<<<PAGE 184>>>）。
## C11. Lab：员工/访客 SSID 创建（Express 模式 AP Web）
- <<<PAGE 224>>>-<<<PAGE 231>>>
- 步骤：WLAN > New → EmployeesX/Personal/密码 + Advanced 里 VLAN ID 20 → 客户端连接验证拿到 192.168.20.7x 网段；Guests：Open + Captive Portal:Yes + VLAN 30 → Access>Authentication 选 Account 模式建 Guest/superuser 账号（区分大小写）→ 浏览器任一 http URL 跳转 Portal。
## C12. AP 内置 DHCP 服务器配置（annex）
- <<<PAGE 232>>>-<<<PAGE 236>>>
- 步骤：Network > AP Networks > vlan10 Manage 配 IP 192.168.10.3 → Service > DHCP Create（Pool Employees，Range 192.168.10.10-50，DNS 自身）→ Action > Bind Network vlan10。40 个地址=40 并发设备上限提示。
## C13. 用户行为日志（Client Behavior Tracking → TFTP/Syslog）
- <<<PAGE 236>>>-<<<PAGE 237>>>
- Access > Authentication > Client Behavior Tracking，日志行含 Event date/client MAC/IP/AP MAC/SSID/ONLINE-OFFLINE 状态。
## C14. GuestOperator 简化前台账号
- <<<PAGE 237>>>
- System > General > Account Management > Operator: Enable + 密码 → 用 GuestOperator 登录仅可管理访客账号。
## C15. 外部 RADIUS 认证的员工 SSID（annex）
- <<<PAGE 238>>>
- Create WLAN → Security: Enterprise → AuthServer: 192.168.1.250 + AuthSecret → Advanced VLAN ID 10。
## C16. Lab：多交换机多 AP 环境（AP1301+AP1321 自动成组）
- <<<PAGE 240>>>-<<<PAGE 245>>>
- 命令（OS2360）：`vlan 10 members port 1/1/8 tagged` / `vlan 10 members port 1/1/6 untagged` → `interfaces 1/1/8 admin-state enable`。两 AP 同 VLAN+同 Group ID 自动组组，PVM=AP1321（型号更高）。
- 修改组：System>General 设 Group name/Management IP/Group ID。
## C17. Lab：交换机上云（OmniSwitch Onboarding 到 Cirrus）
- <<<PAGE 353>>>-<<<PAGE 364>>>
- 命令序列：确认 `ls /flash/working` 有 cloudagent.cfg（缺则 `cp /flash/cirrus/cloudagent.cfg /flash/working/`，<<<PAGE 356>>>）→ `vlan 1305 name SW-MANAGEMENT` + `ip interface "int_sw-mgmt" address 10.130.5.5/24 vlan 1305` + `ip static-route 0.0.0.0/0 gateway 10.130.5.7` → `snmp security authentication all` → `ntp client admin-state enable` / `ip name-server 9.9.9.9` / `ip domain-lookup` → `cloud-agent admin-state enable` → Cirrus 建 Site/Building/Floor → Device Catalog 用 `show chassis` 的 SN 建 Device → 强制 call home：`cloud-agent admin-state disable force` + `enable` → `show cloud-agent status`（DeviceManaged/completeOK）。
## C18. Lab：Stellar AP 上云 Provisioning（AP Group + Provisioning Config）
- <<<PAGE 369>>>-<<<PAGE 375>>>
- 步骤：AP Console `showsysinfo` 取 SN → Device Catalog 建 Stellar AP（Do Not Upgrade）→ Create AP Group "My-AP-Group" → Create Provisioning Configuration（Name/Site/Default RF Profile/Timezone）→ 激活验证 `ocloud_show`（VPN Status connected, cloudProcessStatus completeOK）。
## C19. 上云排障五步法（PoE→线缆→VLAN→AP 状态→L3）
- <<<PAGE 376>>>-<<<PAGE 378>>>、<<<PAGE 365>>>-<<<PAGE 366>>>
- 命令组合：`show lanpower slot 1/1`；`show vlan members port 1/1/6`（管理 VLAN 须 untagged）；AP 侧 `getmode`（须 OVNG）、`cat /etc/config/network`（proto dhcp）、`getovinfo`；交换机 `show ip interface` + `ping eu.activation.ovng.myovcloud.com`；OVC 侧 Action>Diagnostic Tools>View Activation Log。
## C20. Lab：Cirrus 员工 SSID（802.1X + UPAM）全流程
- <<<PAGE 407>>>-<<<PAGE 414>>>
- 步骤：Cirrus 建 VLAN20（GUI 点选 6360 端口 1/1/3、1/1/6 tagged）→ OS2360 手工 `vlan 20 … members port 1/1/6 tagged` 等 → Wireless>SSIDs>Create（Usage: Enterprise Network for Employees (802.1X)，WPA2_AES）→ RADIUS Server=UPAMRadiusServer → 建 Employee 账号 → Access Policy Local Database/Web Auth None → Network Assignments 选 My-AP-Group → VLAN/Tunnel Mapping=VLAN 20 → 客户端 PEAP/MSCHAPv2 连接验证（192.168.20.7x）→ Network>Access Records>Authentication Records 查认证记录。
## C21. Lab：Cirrus 访客 SSID（Captive Portal 模板）+ 踢下线
- <<<PAGE 437>>>-<<<PAGE 443>>>
- 步骤：Create Guest Access Strategy（含 Captive Portal Template：Layout）→ Login By: Username & Password → 建 Guest 账号 → 映射 VLAN 30 → 客户端 http 跳转认证 → Kick Off：Network>Analytics>Clients>Actions>Kick Off。
## C22. 员工 SSID 连接排障（iwconfig/iwlist/sta_list/AAA conf）
- <<<PAGE 415>>>-<<<PAGE 418>>>
- AP CLI 命令组：`iwconfig`（看 ESSID/Tx-Power/SNR）；`iwlist ath01 channel`；`iwlist ath01 txpower`；`ssudo sta_list`（VLANID/Final_role）；`ssudo wam_debug sta_list`（JSON：assignedVLAN/assignedAR）；`cat /proc/kes_syslog | grep "<MAC>"`；`cat /var/config/AAA_profile.conf` + `AAA_server.conf`（核对 UPAMRadiusServer IP/secret）；仍失败 `tcpdump -i br-wan –s 0 host radiusIP`。
## C23. Captive Portal 排障（eag 进程与日志）
- <<<PAGE 444>>>-<<<PAGE 448>>>
- 命令：`ps |grep eag`（/usr/sbin/eag_app 存活）；`eag_cli show user all`（PORTAL 认证用户列表）；`eag_cli kick user index 1`；`tail -f /tmp/log/eag.log`、`cat /var/log/eag.log`；前置检查 `date`（账号有效期）与 `cat /etc/resolv.conf`（DNS 必需）。
## C24. Lab：Virtual Chassis 6360 两台堆叠配置
- <<<PAGE 490>>>-<<<PAGE 497>>>
- 命令序列：`show chassis` 定型号 → A：`virtual-chassis chassis-group 1` + `virtual-chassis chassis-id 1 configured-chassis-priority 200` → `write memory` + `reload from working no rollback-timeout` → B：`virtual-chassis chassis-id 1 configured-chassis-id 2` + `chassis-group 1` → 重启 → 双方 `virtual-chassis vf-link-mode auto` + `auto-vf-link-port 1/1/27`（P24）或 1/1/11（P10）→ `interfaces 1/1/27-28 admin-state enable` → `show virtual-chassis topology` → `write memory flash-synchro` 同步 → `show virtual-chassis consistency` → `ssh-chassis admin@2` 访问从机。
## C25. Lab：动态链路聚合（LACP linkagg 7）+ 冗余测试
- <<<PAGE 588>>>-<<<PAGE 594>>>
- 命令序列：双端 `linkagg lacp agg 7 size 2 actor admin-key 7` → `linkagg lacp port 1/1/3 actor admin-key 7`（6360 VC 跨机箱 1/1/3+2/1/4）→ `show linkagg`/`show linkagg agg 7` → 改默认 VLAN：`vlan 57 members linkagg 7 untagged` → ping -t 期间 `interface 1/1/3 admin-state disable` 验证不丢包。
## C26. Lab：802.1Q 跨交换机多 VLAN 打 tag
- <<<PAGE 596>>>-<<<PAGE 601>>>
- 命令组合：`vlan 20 members linkagg 7 tagged` / `vlan 20 members port 2/1/3 tagged`（三台交换机对互联链路 tag 20/30）→ `show vlan members port 2/1/3`（20/30 tagged + 58 untagged）→ 客户端互 ping 验证 L2/L3 路径。
## C27. Lab：STP 根桥指定与冗余收敛测试
- <<<PAGE 616>>>-<<<PAGE 625>>>
- 命令：`spantree vlan 20 priority 20000`（6870-A 为根）→ `show spantree vlan 20`（Bridge ID=Designated Root 即根）→ `show spantree ports blocking`（6360 上 2/1/3 BLK/ALT）→ ping -t 期间 `linkagg lacp agg 7 admin-state disable` 观察 RSTP 秒级收敛 → 1x1 负载分担：6870 `spantree vlan 30 priority 32768`、6860 `spantree vlan 30 priority 20000`。
## C28. Lab：DHL Active-Active 配置与倒换
- <<<PAGE 640>>>-<<<PAGE 643>>>
- 命令序列：清端口 VLAN 配置后建 linkagg 8 → `vlan 57 members linkagg 8 untagged`、20/30 tagged → `dhl 1` → `dhl 1 linka linkagg 7 linkb linkagg 8` → `dhl 1 vlan-map linkb 30` → `dhl 1 admin-state enable` → `dhl 1 mac-flushing raw` → `show dhl 1`（LinkA Active Vlans 20 57 / LinkB 30）→ 断 agg7 验证 VLAN20 转移到 agg8（show vlan 20 members 见 dhl-blocking 消失）。
## C29. Lab：VRRP 主备 + 双活负载分担
- <<<PAGE 684>>>-<<<PAGE 689>>>
- 命令序列：双机各建 int_20/int_30 → `ip vrrp 1 interface int_20` + `address 192.168.20.254` + `admin-state enable`（VRID1/VRID2）→ `show ip vrrp statistics`（Master/Backup）→ 改优先级（先 disable）：`ip vrrp 1 interface int_20 admin-state disable` → `priority 150` → `enable`，实现 6870 主 VLAN20、6860 主 VLAN30 → 重启主设备验证 Backup 秒级接管，客户端 ARP 表里 192.168.20.254 的 MAC=00-00-5E-00-01-01。
## C30. Lab：DHCP Relay（ip dhcp relay）+ QoS/ACL/Access Guardian 组合
- <<<PAGE 669>>>-<<<PAGE 670>>>：`ip dhcp relay destination 192.168.100.102` + `admin-state enable` → `show ip dhcp relay statistics`（Reception/Tx 计数）。
- <<<PAGE 724>>>-<<<PAGE 726>>>（QoS）：`policy condition client_traffic source vlan 20` → `policy action priority_5 802.1p 5` → `policy rule rule1 …` → `qos apply` → 大包 ping 触发 Red Packets（限速生效）。
- <<<PAGE 749>>>-<<<PAGE 751>>>（ACL）：`policy condition ftpfromvlan20 source vlan 20 destination ip-port 20-21 ip-protocol 6` + `policy action deny disposition deny` + `precedence 65535` 实现员工禁 FTP；`policy service group http`+deny 禁外包 HTTP；`policy port group UserPorts 1/1/1-2` + `qos user-port shutdown bpdu` 防环。
- <<<PAGE 777>>>-<<<PAGE 783>>>（Access Guardian）：`aaa radius-server my_radius host 192.168.100.102 key alcatel-lucent` → `aaa device-authentication 802.1x my_radius` → 建 UNP-employee/UNP-contractor（map vlan 20/30 + qos-policy-list）→ `unp port 1/1/1 port-type bridge` + `802.1x-authentication` + `mac-authentication` → 客户端 802.1X 登录 → `show unp user details`（Profile Source: Auth-Pass-Server UNP）→ `unp user flush port 1/1/1` 重测；`aaa test-radius-server my_radius type authentication user employee password password` 验证 RADIUS。

## counter-examples

## X1. reload all 无条件从 certified 启动（丢未认证配置）
- <<<PAGE 126>>>
- 原文摘录："Warning > The 'reload all' command particularity: IF THE OMNISWITCH IS REBOOTED WITH THE 'RELOAD ALL' COMMAND, IT WILL REBOOT FROM THE CERTIFIED DIRECTORY, NO MATTER WHAT THE CONTENT OF THE RUNNING DIRECTORY IS"
## X2. RAM 未保存就重启 → 配置全部回滚
- <<<PAGE 127>>>
- 原文摘录："Warning > What if the OmniSwitch reboots now? … ALL THE CHANGES IN THE RUNNING CONFIGURATION WILL BE OVERWRITTEN … IN OUR CASE, THE VLAN 2, 3 AND 99 WILL BE LOST"
## X3. Certified 模式下禁止 write memory（典型报错）
- <<<PAGE 129>>>
- 原文摘录："-> vlan 4 / -> write memory / ERROR: Write memory is not permitted when switch is running in certified mode"
- 解法：`reload from working no rollback-timeout` 或 `modify running-directory working`。
## X4. AP 加入 AP Group 时其自身配置会被 PVM 覆盖删除
- <<<PAGE 243>>>
- 原文摘录："Warning：WHEN AN OMNIACCESS STELLAR ACCESS POINT GETS IN AN AP GROUP, ITS CONFIGURATION IS DELETED AND REPLACED BY THE CONFIGURATION SENT FROM THE PRIMARY VIRTUAL MANAGER (PVM) ACCESS POINT."
- 要点：多 AP 混部前务必先把目标配置做到 PVM，否则新入组 AP 的本地配置丢失。
## X5. R-Lab 交换机恢复出厂会破坏实验环境
- <<<PAGE 123>>>
- 原文摘录："Warning：DON'T TEST THE FOLLOWING PART ON YOUR LAB! THE SWITCHES THAT ARE USED IN OUR REMOTE-LAB ARE LOADED WITH A SPECIFIC DEFAULT CONFIGURATION. REINITIALIZING THEM TO THEIR FACTORY DEFAULT CONFIGURATION MAY LEAD TO ISSUES!"
- 通用原则：预配置设备（汇聚/核心/服务器）不要动出厂（另见 <<<PAGE 100>>> "DO NOT MANAGE AND CONFIGURE the core switch OS6900"、<<<PAGE 358>>> "DO NOT use the action Delete on your Organization"）。
## X6. AP 默认口令安全基线（8.10R3 警告 / R4 强制改密）
- <<<PAGE 64>>>-<<<PAGE 65>>>
- 原文摘录："Login : admin / Password : switch"；"Beginning in 8.10R3 a warning message will be displayed urging for the default password to be changed … Beginning in 8.10R4 changing the default password will be mandatory."
## X7. OVC4→OVC10 迁移：序列号不能同时在两个平台
- <<<PAGE 318>>>
- 原文摘录："The serial number of a network device cannot be declared in both OmniVista CIRRUS 4 and OmniVista CIRRUS 10. Make sure to remove all your equipment first"
- 迁移步骤：先在 OVC4 删除全部设备→OVC10 宣告→等 call home（AP 最长 30 分钟，交换机 30 分钟或重启 cloud-agent）。
## X8. call home 太慢 → 手动强制激活（推荐 disable force/enable 而非整机重启）
- <<<PAGE 331>>>、<<<PAGE 363>>>
- 原文摘录："cloud-agent admin-state disable force / cloud-agent admin-state enable … 或 reload from working no rollback-timeout"；cloud-agent.cfg 缺失时需 `cp /flash/cirrus/cloudagent.cfg /flash/working/cloudagent.cfg`（<<<PAGE 356>>> Warning）。
## X9. 改 VRRP priority 未先 disable → 配置不生效
- <<<PAGE 689>>>
- 原文摘录："Warning：THE VRRP INSTANCE MUST BE DISABLED BEFORE CHANGING THE PRIORITY"
## X10. 端口有 VLAN/默认 VLAN 配置时无法加入 linkagg
- <<<PAGE 640>>>
- 原文摘录："-> linkagg lacp port 2/1/3 actor admin-key 8 / ERROR: Port cannot be added to Linkagg, please remove other configuration on this port"
- 解法：先 `no vlan XX members port …` 清干净再加入聚合。
## X11. DHL 与 STP 互斥 + MAC 老化风险（默认 mac-flushing=none）
- <<<PAGE 630>>>、<<<PAGE 642>>>
- 原文摘录："Problem: No topology change after changeover of DHL links … None (default): The staled MAC address entries are kept in the MAC table"；实验："Spanning Tree is disabled on all the DHL enabled ports"（<<<PAGE 642>>> Note）。
- 要点：生产建议显式配置 `dhl 1 mac-flushing raw`（或 mvrp），否则倒换后可能保留过期 MAC。
## X12. 802.11r 与旧终端兼容性：不支持的设备可能无法关联
- <<<PAGE 938>>>、<<<PAGE 940>>>
- 原文摘录："devices which do not support 802.11r may not be able to associate to a 802.11r WLAN, then ALE recommends set specific WLAN for devices supporting 802.11r, 802.11k and 802.11v"；"8158s and 8168s handsets reject the APs 802.11v request in their current version"（<<<PAGE 940>>>）
- 要点：按终端能力分 SSID；81x8s 话机当前版本忽略/拒绝 802.11v。
## X13. RAP 部署三禁区（总部勿用、带宽减半、同地两 RAP 无切换）
- <<<PAGE 904>>>
- 原文摘录："It is not recommanded to use RAP in headquarter due to VPN tunnel constraints … the expected encrypted performance with AP1201H configured as RAP is about 100Mbps while … 433Mbps … In case 2 RAPs are geographically collocated, 8168s handover between 2 RAPs is not supported."
## X14. 模式选错的规模/功能边界（Express 无 DPI 分析、AP1101 组规模腰斩）
- <<<PAGE 875>>>、<<<PAGE 826>>>
- 原文摘录："The voice application bandwidth control in Wifi-Express mode is managed directly by Stellar DPI, through the PVM … There no Voice analytics and Voice application visibility in Wifi-Express mode."（<<<PAGE 875>>>）；"One AP1101 only AP-Group supports up to 64 OmniAccess® Access points, 256 concurrent clients"（<<<PAGE 868>>>，低于 AP13XX 的 255/512）
- 要点：要语音可视化/大规模就必须 Enterprise/Cloud，选 Express 前核对 AP-Group 规模表。
## X15. Lightning Config 使用前提（顺序错了向导不触发）
- <<<PAGE 79>>>、<<<PAGE 1025>>>
- 原文摘录："The easy configuration process (lightning configuration) starts only if: Only first or second physical port connected with the client, no other ports connected • No prior switch configuration exist • No DHCP address assignment occurs after bootup • No remote configuration load (RCL) server and OmniVista NMS connection exists"；"Do not pre-cable the ALE switch to the network … Never connect an out-of-box ALE switch to another without running Lightning Config first"（<<<PAGE 1034>>>）
- 要点：保存配置后默认 IP 192.168.0.1 会被内部移除（<<<PAGE 79>>>）。
## X16. 2.4GHz 语音 + 信道聚合是反模式
- <<<PAGE 908>>>-<<<PAGE 909>>>、<<<PAGE 913>>>
- 原文摘录："HT40 configuration in the 2.4GHz radio band remains possible for a hot spot (using few APs) but is not adapted to a large deployment due to the 3-channels limitation"；"This implementation (Voice on 2.4GHz) is possible but not recommended as 2.4GHz radio band is prone to interferences from Bluetooth, microwave oven and intrusion radar"
- 要点：语音走 5GHz（802.11a/n/ac/ax），2.4GHz 信道聚合在多 AP 部署中会自扰。
## X17. Port Mirroring 与 Port Monitoring 不能同端口、镜像会话数有限
- <<<PAGE 554>>>、<<<PAGE 718>>>
- 原文摘录："Cannot use port monitoring and mirroring on same port"（<<<PAGE 554>>>）；"Port mirroring and monitoring cannot be configured on the same port"（<<<PAGE 718>>>）；6870 上镜像会话上限 2（<<<PAGE 568>>> "The maximum number of mirroring sessions is limited to two"），而部分新型号 8.9R3 提升到 4（<<<PAGE 552>>>）。

## frameworks

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

## glossary

1. **OmniSwitch** — ALE 以太网交换机家族；AOS R8 覆盖 6360/6465/6560/6570M/6860E/N/6865/6870/6900/9900（<<<PAGE 84>>>）
2. **OmniAccess Stellar** — ALE WLAN 接入点家族（Wi-Fi 6/6E/7：AP1301~AP1571），无控制器分布式架构（<<<PAGE 20>>>-<<<PAGE 23>>>）
3. **OmniVista Cirrus (OVC10)** — 云管平台（SaaS），管理 10000 AP + 2000 交换机（<<<PAGE 276>>>-<<<PAGE 277>>>）
4. **OmniVista 2500** — 本地 NMS，Enterprise 模式管理服务器兼许可证服务器（<<<PAGE 190>>>、<<<PAGE 845>>>）
5. **AWOS** — Stellar AP 的操作系统（软件名，如 AWOS 4.0.7）（<<<PAGE 370>>>）
6. **AOS** — Alcatel-Lucent Operating System，OmniSwitch 操作系统 R6/R8 双目录结构（<<<PAGE 125>>>）
7. **OXO Connect / OXE** — ALE 中小/大企业 IP 话音通信服务器（OmniPCX），VoWLAN 的 PBX 侧（<<<PAGE 824>>>）
8. **Rainbow UCaaS** — ALE 云统一通信客户端（iOS/Android/桌面），WebRTC 音视频（<<<PAGE 858>>>）
9. **OTC (OpenTouch Conversation)** — ALE 移动协作客户端（<<<PAGE 824>>>）
10. **8158s / 8168s** — ALE WLAN 话机（Ascom OEM）；8168s 彩屏/免提/PTT/Ekahau RTLS，8158s 黑白屏（<<<PAGE 847>>>）
11. **IMS3** — Integrated Messaging and Wireless Services，81x8s 话机集中网管/告警服务器（ELISE3 硬件 Linux）（<<<PAGE 853>>>）
12. **WinPDM** — Windows Portable Device Manager，话机配置工具（配 Cradle）（<<<PAGE 853>>>）
13. **ALE OmniVista Smart Tool (OST)** — 免费安装/排障工具（PoE 向导、auto-ticket、配置备份）（<<<PAGE 1046>>>-<<<PAGE 1052>>>）
14. **Lightning Config (OLC)** — 交换机开箱即用向导（默认 192.168.0.1，仅 1/2 口触发）（<<<PAGE 77>>>-<<<PAGE 79>>>）
16. **Wi-Fi Express 模式** — 自管理 AP 集群（AP-Group+PVM），≤255 AP，免许可证（<<<PAGE 188>>>）
17. **Wi-Fi Enterprise 模式** — OV2500 集中管理模式，≤4000 AP（<<<PAGE 190>>>）
18. **Wi-Fi Cloud 模式** — Cirrus 云管，≤10000 AP（<<<PAGE 192>>>）
19. **AP Group** — 同 Group ID+同 VLAN 的 AP 自动成组，统一配置单元（Cloud 下按组下发 SSID/RF/策略）（<<<PAGE 205>>>、<<<PAGE 267>>>）
20. **PVM / SVM** — Primary/Secondary Virtual Manager（Controller），组内主/备管理 AP，按型号→MAC 选举（<<<PAGE 206>>>）
21. **UPAM** — Unified Policy Authentication Manager，内嵌 RADIUS + Captive Portal 的统一认证平台（<<<PAGE 385>>>）
22. **ARP (Access Role Profile)** — 接入角色档案：VLAN/QoS/ACL/L7 规则/位置/时段的集合（<<<PAGE 394>>>）
23. **UNP (User Network Profile)** — OmniSwitch 侧用户网络档案（VLAN+Policy List+ACL+QoS+Location+Period）（<<<PAGE 755>>>）
24. **Access Guardian** — 基于 UNP 的角色化接入控制（802.1X/MAC 认证后套用 UNP）（<<<PAGE 754>>>）
25. **Device Catalog** — Cirrus 设备目录，按 SN 宣告并跟踪激活状态至 OV Managed（<<<PAGE 326>>>）
26. **Call Home** — 设备周期性主动联系云激活服务器（默认间隔 30 分钟）（<<<PAGE 332>>>）
27. **cloud-agent** — AOS 交换机上负责 Cirrus 注册/VPN 的代理进程（cloud-agent.cfg 存激活 URL）（<<<PAGE 332>>>）
28. **RAP (Remote AP)** — 远程站点 AP，经 Wireguard VPN 隧道回连总部 VPN VA（Tunnel/Local breakout 两模式）（<<<PAGE 904>>>）

## 交换技术
29. **VFL (Virtual Fabric Link)** — Virtual Chassis 成员间堆叠互联链路（<<<PAGE 468>>>）
30. **Virtual Chassis** — 多台交换机虚拟成单逻辑设备（ISIS-VC 管理，ISSU 升级）（<<<PAGE 468>>>）
31. **ISSU** — In-Service Software Upgrade，逐台 slave 重启的在线升级（<<<PAGE 478>>>）
32. **RCD** — Remote Chassis Detection，VC 分裂的带外检测（走 EMP）（<<<PAGE 476>>>）
33. **LACP (802.3ad)** — 动态链路聚合控制协议，actor admin key 关联端口（<<<PAGE 576>>>）
34. **DHL (Dual-Home Link)** — Active-Active 双归属链路，按 VLAN 划分活跃链路防环（替代 STP）（<<<PAGE 628>>>）
35. **VRRP** — 虚拟路由冗余协议（虚拟 MAC 00-00-5E-00-01-VRID）（<<<PAGE 674>>>）
36. **STP/RSTP/MSTP；flat/per-VLAN(1x1)** — 生成树协议与两种模式（OmniSwitch 默认 per-VLAN）（<<<PAGE 604>>>）
37. **802.1Q / 802.1p** — VLAN 打 tag（12bit VID）/tag 内 3bit 优先级（<<<PAGE 169>>>）
38. **Mobile Tag** — 允许移动口收 802.1Q tag 并动态入 VLAN（话机场景）（<<<PAGE 172>>>）
39. **Loopback0** — 不绑 VLAN 的稳定管理/服务源地址接口（<<<PAGE 659>>>）
40. **EMP** — Ethernet Management Port，带外管理口（master emp 地址命令配置）（<<<PAGE 70>>>）

## PoE
42. **Fast PoE / Perpetual PoE** — 开机即供电 / 重启不断电（需 FPGA 升级）（<<<PAGE 147>>>-<<<PAGE 148>>>）
43. **EEE (802.3az)** — 空闲低功耗节能以太网（仅铜口 100/1000M）（<<<PAGE 149>>>）
45. **SSID** — 服务集标识（Wi-Fi 网络名）；Cirrus 建 SSID 走五步向导（<<<PAGE 383>>>）
46. **Captive Portal** — 访客 Web 认证门户（AP 内置或 UPAM/外部）（<<<PAGE 216>>>）
47. **Walled Garden** — 访客认证前即可访问的白名单网站列表（<<<PAGE 238>>>、<<<PAGE 428>>>）
48. **MU-MIMO** — 多用户多输入多输出（M 发 N 收，多用户复用空间流）（<<<PAGE 912>>>）
49. **OFDMA / BSS Coloring / TWT** — Wi-Fi 6 高效率三件套：子载波调度/同频染色/目标唤醒时间（<<<PAGE 911>>>）
50. **MLO** — Multi-Link Operation，Wi-Fi 7 多链路并发（<<<PAGE 48>>>）
51. **DFS (802.11h)** — 动态频率选择，检测雷达避让信道（<<<PAGE 927>>>）
53. **CNCS (Client Network Context Sharing)** — AP 间客户端上下文共享，漫游判定基础（<<<PAGE 842>>>）
54. **L3 Roaming (GRE tunnel)** — 跨子网漫游时新 AP↔Home AP 建 L2 GRE 隧道（<<<PAGE 894>>>）
55. **DRM (Dynamic Radio Manager)** — Stellar 射频自动管理（ACS/APC、自愈、负载均衡、频段引导）（<<<PAGE 841>>>）
56. **DPI (Deep Packet Inspection)** — AP 内置应用识别，配合 OV 做应用可视与带宽管控（<<<PAGE 875>>>）
57. **WIPS/WIDS** — 无线入侵防护/检测（Rogue AP 检测与压制）（<<<PAGE 993>>>）
58. **Stellar Asset Tracking / Ekahau RTLS** — 基于 BLE 信标 / RSSI 三角定位的资产与人员定位（<<<PAGE 880>>>）

## principles

## P1. Wi-Fi 代际性能对比（Wi-Fi 4/5/6/6E/7）
- <<<PAGE 49>>>
- 原文摘录："Wi-Fi 4 … 802.11n 1.2 Gbps / Wi-Fi 5 … 3.5 / Wi-Fi 6 … 9.6 / Wi-Fi 7 … 46 Gbps；Security WPA2→WPA3；Channel width Up to 320 MHz；Modulation 4096-QAM, OFDMA；MIMO 16x16 MU-MIMO"
- 要点：速率、频段、加密、信道宽度、调制、MIMO 随代际演进的全表。
## P2. Wi-Fi 7 关键技术（MLO / 320MHz / 4096-QAM / MRU / AFC）
- <<<PAGE 48>>>
- 原文摘录："Wider Channel Bandwidth 320 MHz … MU-MIMO up to (16x16:16) … Multi-Link Operation (MLO) Reliability, Efficiency & Performance … 4096-QAM +20% raw speed increase … Automated Frequency Coordination (AFC)"
- 要点：Wi-Fi 7 五大增强及各自收益。
## P3. Wi-Fi 6 高效率技术（OFDMA / BSS Coloring / TWT / 扫描射频 / BLE-Zigbee）
- <<<PAGE 47>>>、<<<PAGE 910>>>-<<<PAGE 911>>>
- 原文摘录："Stellar WLAN brings integrated Bluetooth/Zigbee, dedicated Wi-Fi scanning radio technology"（<<<PAGE 47>>>）；"802.11ax: OFDMA access, BSS coloring, Additional Multi-User-MIMO streams downlink and uplink (up to 8), TWT (Target Wake Time)"（<<<PAGE 911>>>）
## P4. MU-MIMO 原理（MxN 定义与空间流复用）
- <<<PAGE 912>>>
- 原文摘录："802.11n technology has introduced the MIMO … 802.11ac/ax technologies enhance the MIMO with the ability to multiplex several users on each spatial stream … Multi-User MIMO is defined as MxN: e.g. 2x2, 3x3 and up to 4x4. M = number of transmit antennas, N = number of antennas at the receiver."
- 要点：话机 1x1 走视距+分集，MU-MIMO 客户端复用多径空间流。
## P5. PoE 标准演进与功率预算（802.3af/at/bt Type1-4）
- <<<PAGE 150>>>
- 原文摘录："802.3af PoE 12.95W@PD / 15.40W@PSE / 350mA；802.3at Type 2 PoE+ 25.50W / 30.0W / 600mA；802.3bt Type 3 51W / 60W / 600mA per pair；802.3bt Type 4 71W / 100W / 960mA per pair；Energy Management 三/四/六/八级 class"
- 要点：四档 PoE 的 PD 可用功率、PSE 供给功率、电流与供电等级完整对照。
## P6. PoE 端口优先级与断电顺序（Low/High/Critical）
- <<<PAGE 154>>>
- 原文摘录："Low: In the event of a power management issue, inline power to low-priority ports is interrupted first … Critical: inline power to critical ports is maintained as long as possible"
- 要点：功率不足时按 low→high→critical 顺序断电，默认 low。
## P7. PoE 动态分配原理（Dynamic PoE Allocation）
- <<<PAGE 150>>>
- 原文摘录："Dynamic PoE Allocation: Provide only the amount of power needed by powered devices (PD) up to the total energy budget for the most efficient power consumption possible"
## P8. Fast PoE / Perpetual PoE 原理
- <<<PAGE 147>>>-<<<PAGE 148>>>
- 原文摘录："Fast PoE … Allows the chassis to immediately provide PoE power to any connected device after powering up without waiting for the chassis to finish booting"；"Perpetual PoE … Provides uninterrupted power to the connected device (PD) even when the switch is restarting"
- 要点：两者都需升级 FPGA/CPLD；OS6360-P10A 不支持。
## P9. EEE 节能以太网（802.3az）
- <<<PAGE 149>>>
- 原文摘录："Protocol to allow chipset to go to a low power mode state when idle … EEE is only applicable to OmniSwitch copper ports operating at 100/1000 Mbps speed"，光口 U 型号不支持。
## P10. AOS 双分区启动判定规则
- <<<PAGE 126>>>、<<<PAGE 88>>>
- 原文摘录："The switch will reboot from certified directory if contents (images and vcboot.cfg) are different from the running directory … If contents are the same, the switch will reboot from the running directory"；"reload all" 无论何时都从 certified 启动（<<<PAGE 126>>> WARNING）
- 要点：冷启动默认比较 working 与 certified 内容决定启动目录；这是防"半配置"开机的回滚保护机制。
## P11. Certified 模式只读原理
- <<<PAGE 91>>>、<<<PAGE 129>>>
- 原文摘录："When the switch boots from the CERTIFIED directory, changes made to the switch cannot be saved and files cannot be moved between directories"；实测 "ERROR: Write memory is not permitted when switch is running in certified mode"（<<<PAGE 129>>>）
## P12. VLAN 间路由原理（IP interface 绑定 VLAN 即开路由）
- <<<PAGE 165>>>、<<<PAGE 512>>>
- 原文摘录："IP interfaces are associated with VLANs • IP routing is active as soon as at least one IP interface is associated with a VLAN -> ip interface <int_name> address <ip address/mask> vlan <vlan_id>"；"The operational status of a VLAN remains inactive as long as no active port is associated with this VLAN"（<<<PAGE 512>>>）
- 要点：网关即虚拟路由器端口；VLAN 无活动成员时 IP 接口 DOWN、不参与路由通告。
## P13. 802.1Q VLAN Tag 帧结构（12bit VID + 3bit 802.1p）
- <<<PAGE 169>>>、<<<PAGE 516>>>
- 原文摘录："802.3 MAC header change • 4096 unique VLAN Tags (addresses) … 802.1P Three bits field within 802.1Q header allows up to 8 different priorities"
- 要点：4 字节 tag = Ethertype + Priority + VID。
## P14. 物理端口恒有一个默认（untagged）VLAN 桥接
- <<<PAGE 599>>>
- 原文摘录："A PHYSICAL PORT ALWAYS HAS 1 VLAN (THE DEFAULT VLAN FOR THE PORT) THAT BRIDGES TRAFFIC (LEVEL 2)"
## P15. VLAN Mobile Tag 与 802.1Q Tag 的区别
- <<<PAGE 173>>>、<<<PAGE 793>>>
- 原文摘录："Mobile Tag: Allows mobile ports to receive 802.1Q tagged packets … Triggers dynamic assignment … 802.1Q Tag: Not supported on mobile ports … Statically assigns (tags) fixed ports"
## P16. UNP 动态 VLAN 分类规则优先级（Port/Domain/MAC/LLDP/IP/Tag）
- <<<PAGE 506>>>
- 原文摘录："UNP Port classification rules 1. Port/Linkagg 2. Domain 3. MAC address 4. MAC-OUI 5. MAC address range 6. LLDP 7. Auth-type 8. IP address 9. VLAN tag"
## P17. Stellar 默认出厂行为（mywifi SSID + 192.168.1.254 + Group ID 100）
- <<<PAGE 202>>>、<<<PAGE 205>>>
- 原文摘录："BROADCASTS A SSID 'MYWIFI-ABCD' … HAS THE IP@ = 192.168.1.254 … HTTP://<IP@ OF THE AP>:8080"；"Identical Group ID (Group ID 100) • Identical default VLAN (VLAN 1)"
## P18. Stellar 分布式控制面：空口+LAN 交换 RF/客户端上下文
- <<<PAGE 270>>>
- 原文摘录："Over the Air Exchange: Radio Frequency settings, Power, Channel, RSSI … Over the LAN Exchange: Roaming client's context, MAC addresses, Keys, Access Role Profiles"
- 要点：无控制器架构下 AP 间通过空口/LAN 同步 RF 决策与漫游上下文（CNCS）。
## P19. Stellar L3 漫游原理（Home AP + L2 GRE 隧道）
- <<<PAGE 894>>>、<<<PAGE 843>>>
- 原文摘录："A mobile IP Tunnel (L2 GRE) is created between the two AP groups by the 'New associated AP3', to the Home AP2"；"Stellar allows automatically the tunneling of client traffic from the Home AP … keeping all policies including QoS and security ACLs maintained"
- 要点：跨子网漫游时新 AP 到 Home AP 建 GRE 隧道，用户 IP 不变。
## P20. 802.11r/k/v 快速漫游机制
- <<<PAGE 938>>>-<<<PAGE 940>>>、<<<PAGE 127>>>（附录页码同 <<<PAGE 938>>> 段）
- 原文摘录："802.11r -Fast Transition (FT) … allows the client-AP handshake and key exchange with new AP to be done before the client roams"；"802.11k standard allows clients to request reports containing information about known neighbor APs"；"802.11v – BSS Transition Management … AP will try to assist in the roaming decision making"
- 要点：over-the-air FT 为默认模式；11k 邻居报告省去全信道扫描；11v 由 AP 主动建议漫游目标；不支持 11r 的终端可能无法关联 11r WLAN，需分 SSID。
## P21. 语音小区规划 RSSI 门限（-70dBm 覆盖 / -62~-64dBm 漫游 / 8dB 重叠）
- <<<PAGE 928>>>-<<<PAGE 931>>>
- 原文摘录："a -70 dBm RSSI (or better) is required … generally a -62dBm RSSI (or better) is required to ensure a correct roaming"；"The APs should be placed to overlap their boundaries by approximately 8 dB"；"SNR 25 dB or better, Noise level < -92 dBm, RSSI > -67 dBm"
## P22. 智能手机 EIRP 不对称问题
- <<<PAGE 931>>>
- 原文摘录："Smartphones set generally lower EIRP than APs in 5 GHz band … with only 11dBm … the RF range provided by the iPhone is much shorter than the Access Point RF range (EIRP here is 8 times lower)"
- 要点：降低 AP 功率匹配手机不可取（AP 数量暴涨）；手机 VoWLAN 只能 Best Effort。
## P23. WMM/DSCP/802.1p QoS 映射（Voice=EF46/6, Video=4, BE=0）
- <<<PAGE 874>>>、<<<PAGE 932>>>
- 原文摘录："Voice: DSCP 46 (48,56) → 802.1p 6；Video: 40 → 4；Best effort: 0 → 0；Background: 8 → 1"；话机侧 "a DSCP value of 46 is recommended for the Voice traffic and a value of 26 is recommended for the Voice signaling"（<<<PAGE 933>>>）
## P24. VoWLAN 质量门限（MOS≈4 的网络指标）
- <<<PAGE 933>>>、<<<PAGE 1007>>>
- 原文摘录："Network round trip delay must be less than 250 ms • 802.11 retransmissions should be kept under 15% • Jitter must be less than 100 ms • Packet loss must be less than 2%"；MOS 表：4=Good R-value 80-90（<<<PAGE 1008>>>）
## P25. 语音 AP 容量基准（每 AP 并发语音流 / 带宽）
- <<<PAGE 892>>>
- 原文摘录："All Stellar AP13XX in 11ax: 14Mbps (400Kbps per user) … Up to 35 Voice streams (18)；All Stellar AP12XX in 11ac: 13Mbps … Up to 32 Voice streams (16)；Rainbow Audio/Video HD: Up to 105Mbps (3Mbps) / 35 streams"
- 要点：G.711/Opus NB 编码下各代 AP 的语音容量对照。
## P26. 网状/桥接带宽衰减规律（4 跳/4 方向、每 mesh 点 /4）
- <<<PAGE 899>>>
- 原文摘录："4 voice mesh hops max - the bandwidth will be divided by 3 when reaching a mesh point … 4 voice mesh directions max - … equivalent to the mesh root AP bandwidth divided by 4 … Max transit capacity of about 15 8158s/8168s per root AP"
- 要点：Mesh 拓扑中 VoIP 只能 Best Effort（11r/PMK key 处理限制）。
## P27. Virtual Chassis 原理（VFL 互联=单逻辑交换机，ISIS-VC 拓扑管理）
- <<<PAGE 468>>>、<<<PAGE 471>>>
- 原文摘录："Virtual Chassis = Group of switches which appears as a single router or bridge • No STP/VRRP between Access and Core switches • Upgrade via ISSU • No license needed"；"VC topology managed by ISIS-VC … Maintains a loop-free topology for BUM traffic"
- 要点：Master 选举顺序：最高 priority → 最长 uptime（>10min 差）→ 最小 chassis ID → 最小 MAC（<<<PAGE 472>>>）。
## P28. VC 分裂（Split Chassis）双检测机制（RCD out-of-band + VSCP in-band）
- <<<PAGE 476>>>-<<<PAGE 477>>>
- 原文摘录："Out of Band: EMP Remote Chassis Detection (RCD) … The former Slave chassis will shutdown all its front-panel user ports to prevent duplicate IP and chassis MAC addresses"；"In Band: VC Split Protocol … requires an upstream or downstream device to act as helper switch"
## P29. ISSU 原理（逐台 slave 升级、最小中断）
- <<<PAGE 478>>>
- 原文摘录："Used to upgrade the software on a VC with minimal network disruption • Each element is upgraded individually … The Slaves are then reloaded from the ISSU directory in order from lowest to highest chassis ID"
## P30. STP 模式与协议（flat/per-vlan × STP/RSTP/MSTP）
- <<<PAGE 604>>>
- 原文摘录："Supports two Spanning Tree operating modes: flat (single STP instance per switch), per-VLAN … (By default on OmniSwitch)；STP (802.1d): Convergence time : 50 secs；RSTP (802.1w): < 1 sec；MSTP (802.1s)"
## P31. STP 1x1 负载分担原理（按 VLAN 改 priority 分根桥）
- <<<PAGE 606>>>、<<<PAGE 622>>>
- 原文摘录："per vlan (1x1) - load balancing … To take advantage of the 1x1 mode and provide load-balancing, it may be necessary to modify bridge priority"；示例：6870 为 VLAN 20 根、6860 为 VLAN 30 根。
## P32. LACP 动态聚合原理（actor admin key 关联端口）
- <<<PAGE 576>>>、<<<PAGE 588>>>
- 原文摘录："Dynamic: IEEE 802.3ad LACP • LACP will negotiate the optimal parameters for both ends using LACPDU … Static: Only works between Alcatel-Lucent OmniSwitches"；"the actor admin key has local significance only"（<<<PAGE 588>>> Note）
## P33. 负载分担哈希算法（brief vs extended）
- <<<PAGE 583>>>
- 原文摘录："Brief Mode: UDP/TCP ports not included … Extended: UDP/TCP ports to be included in the hashing algorithm → more efficient load balancing"；默认值：6900/6465/6360 brief，其余 extended。
## P34. DHL Dual-Home Link Active-Active 原理（按 VLAN 划分活跃链路防环）
- <<<PAGE 628>>>-<<<PAGE 630>>>
- 原文摘录："DHL Active-Active splits VLANs between two active links • The forwarding status of each VLAN is modified by DHL to prevent network loops"；"Spanning Tree is automatically disabled on DHL ports"；MAC flushing 三选项 RAW Flooding / MVRP Enhanced / None（默认）
## P35. VRRP 原理（虚拟 MAC 00-00-5E-00-01-VRID、多 VRID 负载分担）
- <<<PAGE 674>>>-<<<PAGE 675>>>
- 原文摘录："Virtual MAC address: 00-00-5E-00-01-{VRID} … Multicast 224.0.0.18"；"Two virtual routers with their hosts splitting traffic between them"（<<<PAGE 675>>>）
- 要点：修改 priority 前必须先 disable 实例（<<<PAGE 689>>> Warning）。
## P36. DHCP Option 138/43 与 AP 云注册
- <<<PAGE 280>>>、<<<PAGE 877>>>（troubleshooting 138/43）
- 原文摘录："Enable DHCP standard options: 1, 2, 6, 28, 42, 43. And, when using proxy: 129, 130, 131, 132, 133, 138"；"The DHCP Server sends the OmniVista IP address to the Stellar AP via a specific option (138/43)"（<<<PAGE 377>>>）
## P37. Loopback0 接口用途（管理面稳定源地址）
- <<<PAGE 659>>>
- 原文摘录："Identify a consistent address for network management purposes • Not bound to any VLAN • Always remain operationally active … Use: RP in PIMSM, sFlow Agent IP address, Source IP of RADIUS authentication, NTP Client, BGP peering, OSPF router-id, Switch and Traps Identification"
## P38. QoS Policy 三件套（condition + action + rule）
- <<<PAGE 699>>>
- 原文摘录："A policy (or a policy rule) is made up of: 1. a condition 2. an action"；condition 可达 L1-L4（source port/MAC/VLAN/IP/DSCP/TCP-UDP port），action 含 disposition accept|drop|deny、priority、bandwidth、mirror、redirect。
- 要点：qos apply 才下发硬件；规则默认 accept 不匹配流量。
## P39. ACL 安全组（UserPorts/DropServices/Port Disable）
- <<<PAGE 739>>>-<<<PAGE 740>>>
- 原文摘录："UserPorts … Used by default to prevent spoofed IP addresses on ports … -> qos user-port {filter | shutdown} {spoof|bgp|bpdu|rip|ospf|vrrp|…}"；DropServices 保留服务组可按服务丢包；port-disable 命中即管理关闭端口。
## P40. LLDP-MED 网络策略 TLV（语音 VLAN + L2 priority + DSCP 自动下发）
- <<<PAGE 787>>>-<<<PAGE 794>>>
- 原文摘录："-> lldp network-policy 1 application voice vlan 151 l2-priority 5 dscp 46 … Switch send a LLDP Frame"；"MED: Power and Capability, Inventory Management, Network Policy"；实例 "unp profile 'voip-temp' mobile-tag … lldp med-endpoint ip-phone classification"（<<<PAGE 794>>>）
- 要点：IP 话机上电经 LLDP-MED 自动获得语音 VLAN/QoS，配合 UNP mobile-tag 动态入 VLAN。
## P41. 漫游判定逻辑（CNC 表判定 L2/L3 漫游）
- <<<PAGE 917>>>
- 原文摘录："Client Network Context exists? … Client Ntw Context VLAN Id = AP Access Role VLAN Id? Yes → Layer 2 roaming / No → Layer 3 roaming"
## P42. RAP（Remote AP）两种模式（Tunnel / Local breakout）
- <<<PAGE 904>>>
- 原文摘录："Tunnel mode: all traffic between Remote AP and VPN VA goes through a VPN tunnel … Local breakout: Traffic between 2 users at remote location remains local"；"expected encrypted performance with AP1201H configured as RAP is about 100Mbps while the same … in headquarter has about 433Mbps"
- 要点：RAP 不建议部署在总部；两台 RAP 同地不支持 8168s 互相切换（handover）。
