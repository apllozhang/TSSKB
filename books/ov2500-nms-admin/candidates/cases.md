# cases 候选 — DT00XTE311 OmniVista 2500 NMS Administration R4

1. 部署 Virtual Appliance（vSphere OVF 全流程）
   - <<<PAGE 54>>>："1. Log into vCenter and open the vSphere client. 2. Select File > Deploy OVF Template … Disk formatting (Thin or Thick Provision). (Thick provision is recommended.) … 4. If the new Virtual Appliance was not powered on via the deployment wizard, power on the VM now."

2. 安装序列：控制台初始化（IP/Network Size/附加选项 → 重启 → 首登改密 → License）
   - <<<PAGE 56-60>>>：Hypervisor Console 填 cliadmin 密码 → IP Settings（OV IP、HTTP/HTTPS 端口、Captive Portal IP/端口、Additional OV Web）→ Network Size → Hostname/DNS/NTP/Timezone/Routes → Exit & Reboot。
   - <<<PAGE 61/101-102>>>：浏览器访问 `https://<IP>`，首登强制改默认密码，随后弹 License 窗口。

3. 生成并安装 Evaluation License（lds.al-enterprise.com）
   - <<<PAGE 103-104>>>：访问 https://lds.al-enterprise.com/ → OmniVista 2500 NMS → Customer ID 99999 / Order Number "evaluation" → License Type EVAL-OV2500-ALL-TYPE_1 / Passcode omnivista → Generate License 保存文件；安装两法：Add License → Browse 上传文件，或手输 License Keys；EULA 勾 OK、不勾 Enable Fleet Supervision。
   - <<<PAGE 105>>>：装好后删除本地 EVAL 许可文件。

4. AOS 交换机 SNMP 准备（六台交换机逐台执行）
   - <<<PAGE 97>>>：命令序列：`aaa authentication default local` → `user snmpuserv3 read-write all password "Superuser=1" sha+des` → `snmp security privacy all` → `snmp authentication-trap enable` → `snmp station 192.168.100.107 snmpuserv3 v3 enable` → `snmp-trap absorption enable` / `snmp-trap to-webview enable`。
   - SNMPv1/v2 变体：<<<PAGE 68>>>：`snmp community map public user test1234 enable`、`snmp security no security`。

5. 基础网络初始化（Loopback0 + OSPF + LACP）——按交换机逐台脚本
   - <<<PAGE 92-95>>>：sw1(6900A) 完整命令块（linkagg lacp agg 12、vlan 100/112/117、ip interface、ip ospf area 0.0.0.0、redist、static-route 0.0.0.0/0、`ip interface Loopback0 address 192.168.200.1`、dhcp relay）至 sw8(6860B)。
   - <<<PAGE 90-91>>>：验证：`show ip routes` 需含全部 Loopback0/32 路由；从 OS6900-A ping 各 192.168.200.x。

6. 创建 Discovery Profile 并发现设备
   - <<<PAGE 170-172>>>：路径：Network → Discovery → Discovery Profiles → "+"；General：Name=Training、CLI/FTP admin/switch；SNMP：SNMPv3、Timeout 5000、Retry 3、User snmpuserv3、SHA+DES、密码 Superuser=1；Advanced：Trap Station User=admin、Discover Link=Normally、Shell=SSH、GetBulk on、Max Repetitions 10 → Create → Managed Devices → Discover New Devices → Start IP 192.168.200.0 / End 192.168.200.8 / Mask 255.255.255.0 → 关联 Profile → Create → Discover Now → Finish。

7. 创建拓扑站点与地图
   - <<<PAGE 175-176>>>：Network → Topology → Create Site（Site Name、Street Address、选全部交换机）→ 选中站点 → Go to Topology → 拖拽排布；"If a link is not being shown in the map, select the switch and look for the Operations window on the right. Select Poll Device or Poll Link"。

8. VLAN Manager 批量建 VLAN 与 IP 接口
   - <<<PAGE 180-184>>>：Configuration → VLANs → Create VLAN by Devices（VLAN Wizard）：填 VLAN ID → Add/Remove Devices（Add All>>）→ Q Tagged Ports Assignment（逐交换机 Add Port）→ Review → Create；再点 IP interface → "+" 建 IP 接口（Name/IP 192.168.VLAN#.Switch#/Mask/Device）→ Create → 控制台验证。

9. Locator 按 IP/MAC/授权用户定位
   - <<<PAGE 187-188>>>：Network → Locator → 输入 192.168.X.Y → Locate（可切 Live/Historical）→ Locate on Map 跳转拓扑；Browse → ADD → Use Picker 选交换机查看 MAC 表；视图含 Location/Classification/Data Center/Layer 3。

10. 配置 SMTP 邮件服务器与 Trap Responder（断链邮件告警演练）
    - <<<PAGE 191-194>>>：Administration > Preferences > System Settings > Email（SMTP 10.130.5.6、From 地址、Send Test E-mail 验证）；Network → Notifications → Trap Responders → "+"：Agent Type=Device、IP 范围 192.168.200.1-8 → Trap Type 关掉 Normal → Response=Send an e-mail → Create；拔链路生成 trap，登录邮箱验证；"Try different events, i.e. logging in to the switch with an incorrect username or password and notice the trap being generated."

11. 告警声音配置
    - <<<PAGE 195>>>：Administration – Preferences – User Settings – Sounds → Alarm Sounds 启用 Notifications → For All Severities → Apply（可按严重级别分设不同声音）。

12. Resource Manager：配置备份与恢复
    - <<<PAGE 197-201>>>：Configuration → Resource Manager → Backup/Restore → Backup → Backup by Devices → Use Switch Picker 选交换机 → （如提示 FTP 认证，Add FTP Authentication：admin/switch）→ Backup Type=Configuration Only → Backup；恢复：Restore → Add/Remove Backup Files → 选文件 → Restore → 确认 Yes。

13. Resource Manager：镜像导入与交换机升级（含升级后手工 reload）
    - <<<PAGE 203-206>>>：Upgrade Image → Import（*.zip 镜像）→ Install → 选固件文件 → Add/Remove Device（"OmniVista will only present the switches that can run this firmware version"）→ Install Software；完成后："Go to the Topology Application, select your switch and click on CLI Scripting – SSH. Reload your switch from the working directory. When the switch reboots, perform a Copy Working Certified."

14. Inventory 报表生成
    - <<<PAGE 202>>>：Resource Manager → Inventory → Create Report → Select Devices → 选报告类型 → Create → 点链接在浏览器打开报表。

15. CLI Scripting：创建/发送脚本与查看日志
    - <<<PAGE 209-214>>>：Configuration → CLI Scripting → Scripts（可查看预置脚本命令）→ Send Script（向导）→ Add/Remove Devices 选交换机 → 立即 Send 或 Next 调度（Periodically + Simple/Cron）→ 填用户变量 → Send Script；Terminal 菜单开 Telnet/SSH 会话；Logs 菜单查看脚本执行结果（Success/Error/语法错误）。

16. 计划性批量升级（Scheduled Upgrades）
    - <<<PAGE 124-126>>>：Discovery → Scheduled Upgrades："Allows to upgrade multiple switches at the same time. Upgrade can be done immediately or scheduled"；可为每台设备设不同版本与安装目录；完成后到 Managed Devices 检查 "the directory where the installation was made is correct and that the status of the update is successful"。

17. 用户与用户组（只读权限演练）
    - <<<PAGE 216-218>>>：Security → Users & User Groups → Group → 创建 Training 组、Group Rights 选 Read → User → 创建 training_user（密码强度指示 Risky–Weak–Fair–OK）→ 登出用新账号登录验证只读（"you are limited to view information, but you are not allowed to modify the configuration"）。

18. Control Panel / Watchdog 与 Scheduler History
    - <<<PAGE 221>>>：Administrator → Control Panel → Watchdog Screen 查看服务状态、点服务看描述/状态/依赖、滑块启停；Scheduler → Scheduler History 查看 Asset Management 事件历史。

19. Unified Access 全流程实验（RADIUS + AAA Profile + UNP + 802.1X 客户端）
    - <<<PAGE 258-268>>>：vSphere 开 AAA Training Server VM → Security > Authentication Servers > RADIUS 建 RADIUS_VM（192.168.100.102 / secret alcatel-lucent）→ Unified Access > Unified Profile > Templates：AAA Server Profile（802.1X Primary/MAC Primary=RADIUS_VM）→ Access Role Profile UNP-employee（"Type the UNP name as shown as it is the value returned from the RADIUS server"）→ Apply to Devices（Map to VLAN 80、选 6860B）→ Access Auth Profile UNP_template（AAA=AAA_RADIUS、Port Bounce/MAC Auth/802.1X Auth Enabled）→ Apply to Devices 选 6860B 端口 1/1/1。
    - 验证：`aaa test-radius-server RADIUS_VM type authentication user employee password password`（返回 Filter-ID = UNP-employee）；客户端启用 IEEE 802.1X（EAP-MSCHAP v2、不缓存凭据、不自动用 Windows 登录名）；`unp user flush port 1/1/1` 清状态后重连；`show unp user` 应显示 employee/VLAN 80/UNP-employee；Network → Locator 按 Auth. User=employee Live 查询。
    - <<<PAGE 266>>>：客户端排查：认证页签缺失时 "click on the Start button, Run…, type services.msc … Look for Wired AutoConfig service and start it."

20. PolicyView Expert Mode 实验：阻断客户端访问 Loopback0 网段
    - <<<PAGE 290-293>>>：Configuration > PolicyView → Expert Mode → Create：Name=Block_Loopback0_access、Precedence=30001 → Device Selection 选 switch8 → Condition：L3 IPs，Source IP Range 192.168.80.0/24、Destination 192.168.200.0/24 → Action：QOS、Disposition=DROP → Validity=AllTheTime → Create → Existing Policies 选策略 → Select Device(6860B) → "Click on Notify Selected and wait for the Notify Success! Message"；验证：ping 192.168.200.# 不通、ping 192.168.100.102 正常。

21. Quarantine Manager 内置规则族（AlaDosTrap/Fortinet/OA WLAN）
    - <<<PAGE 304>>>：Alcatel DOS Trap Rule（Teardrop/Ping of Death/Port Scan）；Fortinet Anomaly/Signature/Virus（忽略 Fortigate 上配 Pass 的项）；OA WLAN Rogue AP Active/Detected/Station w/ Rogue AP。
    - <<<PAGE 305>>>：自定义规则四要素：名称、描述、触发表达式、提取表达式（取源地址）、动作（入 Candidates 或 Banned）。

22. QM Responder（邮件/外部程序）
    - <<<PAGE 311>>>："AQM can send an e-mail to any address you specify. Based on variables to specify the information to be included in the e-mail … AQM can execute an external program or script on the OmniVista server."

23. 2FA 初始设置操作
    - <<<PAGE 158-159>>>：按 User Role 启用 2FA → 手机装 Google Authenticator → 登录页出现二维码 → App 扫码 → 在 TOTP Code 字段输入 6 位码 → Verify 登录。

24. Switch User Account（UPAM 代管交换机账号）
    - <<<PAGE 166>>>："Creates switch user accounts through UPAM. After creating a switch user, you create a AAA Profile for the user, setting UPAM as the server used for switch access, and assign the AAA Profile to network switches."
    - <<<PAGE 167>>>：Switch Access Record 显示经 UPAM 的交换机认证访问记录。

25. SSH/Telnet 到未纳管新设备（4.3R2+）
    - <<<PAGE 164>>>："You can now SSH/Telnet to a newly added device that is not yet reachable by SNMP to configure the device for OmniVista management."

26. Application Visibility 配置实验（OS6860-B 监控+封禁社交/游戏应用）
    - <<<PAGE 371-376>>>：Network → Application Visibility → Devices Management 确认无 Profile → Signature Files（AppSig.upgrade_kit_3 用于 OS6860）→ Signature Profiles → "+"：Name=OS6860_Profile → 选 Signature File → Monitor Flow Count 组新建 App Group "MyApps"（Facebook/Twitter/youtube/bet365）→ Bandwidth Usage and Enforcement 组选 MyApps → ACL/QoS 字段点 N/A：Disposition=DROP → Create Profile → Apply to Devices（6860-B，端口 1/1/1 与 1/1/5）。
    - 验证：交换机日志出现 "Kit update complete"；PolicyView Users and Groups > Unified Policies 出现自动生成策略（含 MyApps）；CLI：`show app-mon config`、`show app-mon ipv4-flow-table monitor|enforcement verbose`、`show app-mon app-record hourly`；客户端访问 facebook.com 被阻断（<<<PAGE 382>>>）。

27. Analytics Profile 创建与报表/Widget 展示
    - <<<PAGE 384-389>>>：Network → Analytics → Profiles → "+"：Profile Name、Profile Type（Top N Apps & Clients / Top N Ports Utilization）→ 选交换机并 Add Ports（按拓扑逐台加 1/1/1、1/1/5 等）→ Create；Reports 页查看 Top N Clients/Ports/Applications；Dashboard → Add Widget 添加分析组件（Config 调显示量/时间区间，More 跳转报表页）。

28. Statistics 采集与自定义 View Profile（上仪表盘）
    - <<<PAGE 390-394>>>：NETWORK > ANALYTICS > Statistics → Collection → 编辑 Default Profile 属性集；Statistics → Selectors：Attributes（Switch Health CPU/内存/温度、Port Rx/Tx Bytes）+ Devices（6860-B）+ Counters（含具体端口）→ View 图形/View Table → Save Selection As…（My_View_Profile，刷新 2 分钟）→ 首页 Performance Monitoring → Add Widget（My_View_Widget 绑定 Profile）。

29. 定期 PDF 报表（Report Configuration）
    - <<<PAGE 354-357>>>：Report Configuration → Create：Report Title、Purging Policy、Schedule（Now/Periodically，Simple 或 Cron）；再到 Analytics 各报表右上 Export → Add to Report 将视图挂入；Report → List 下载/删除 PDF。

30. OVNA 集成配置序列
    - <<<PAGE 424-434>>>：五步："Obtain OVE API Key（Security > External Apps）→ Obtain OVNA UUID（OVNA Dashboard）→ Declare OVE instance in OVNA（Configuration > OmniVista Synchronization，填 Server Type/OmniVista URL/API Key）→ Declare OVNA instance in OVE（Managed Devices → Features → Enable OmniVista Network Advisor → + Add New 填名称/IP/UUID）→ Monitor devices in OVNA Rainbow bubble"；同步周期每小时；设备侧需配好管理 IP、syslog 并确保可达 OVNA。

31. IoT 启用与清单
    - <<<PAGE 404-405>>>：Managed Devices List 勾选设备 → Enable IoT；IoT Inventory 展示 End Point MAC/IP、Status（Active/Offline/Error）、Category、Manufacturer、Port/ESSID、起止时间；"updated every 5 minutes for devices connected to Stellar APs and every 15 minutes for devices connected to AOS Switches"；可导出 .xls。

32. Provisioning Rule 创建与 Golden Config / Force Provision
    - <<<PAGE 462>>>：Rule 字段：Serial Number/MAC、Switch Model、Switch Config Template（追加到现有配置）、Value Mapping（动态模板必填）、Mgmt Users Template（默认推送）、Save and Certify。
    - <<<PAGE 466-467>>>：Results 表查看尝试过的交换机；Golden Config 列点 Edit 从最近三次备份中选一并 Apply；"The Force Provisioning Config button is used to push a Provisioning Rule configuration to a matching switch the next time the switch contacts the OmniVista server."

33. Thin Client 配置规则属性
    - <<<PAGE 76>>>：Provisioning Rule 附加属性：Thin Switch Yes/No；Desired Switch Config 可选 Switch Config Template + Incremental Template、Config Snapshot from latest backup、Config Snapshot from Golden Configuration。

34. 交换机侧初始配置恢复命令（Lab 环境重建）
    - <<<PAGE 92>>>："If the initial setup was not applied correctly you can type the following commands to configure VLANs and IP addresses: Do this ONLY if the initial setup was not applied and with the approval of your instructor."（随后给出 sw1-sw8 完整命令块）。

35. 远程实验室连接（R-Lab）
    - <<<PAGE 81/86>>>：浏览器访问 https://rdp.al-mydemo.com/，账号 LanpodXa/LanpodXb；OV2500 地址 https://10.4.pod#.208:8443；"Other web browser may have some issue with copy/paste … Known workaround for FireFox: https://sudoedit.com/firefox-async-clipboard/"。
