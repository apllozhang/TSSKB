# cases 候选 — DT00XTE310 OmniSwitch LAN Access & OmniAccess Stellar WLAN Express

> 实战案例/操作序列/命令组合（含 `>>>`/`->` 命令）。每条含页码引用。共 30 条。

## C1. Lab：R-Lab 连接与拓扑认知（三台交换机+两 AP+Cirrus）
- <<<PAGE 97>>>-<<<PAGE 103>>>
- 要点：rdp.al-mydemo.com 登录 Pod；接入层 OS6360/OS2360（L2 交换）、汇聚 OS6870（预配置勿动）、核心 OS6900 透明；DHCP 服务器 VLAN10/20/30 三个 scope（192.168.10.70-79 等，<<<PAGE 106>>>）。

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
