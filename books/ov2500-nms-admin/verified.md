# Verified 候选（V1 原文真实性核对 + V2/V3 抽查）

## cases

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

## counter-examples

1. 许可安装二选一陷阱：License 文件与 License Keys 不可同时使用
   - <<<PAGE 104>>>："There are 2 different ways to install the evaluation license: By inserting directly the license file … OR by typing the license keys. **Don't do both!**"
2. License Key 粘贴整行的反例（会把许可名一起粘进去）
   - <<<PAGE 104>>> Warning："COPY AND PASTE ONLY THE LICENSE KEYS AND NOT THE ENTIRE LINES!（示例行 'EVAL-NM-EX-20-N, KEQWEXRH-…'，只取逗号后的 key 部分）"；且 "remove the license name before inserting them"。
3. 默认状态下交换机不能被 OV 管理（必须先配 SNMP）
   - <<<PAGE 97>>>："By default, an OmniSwitch cannot be managed by Omnivista. The switch must be modified to allow SNMP access."
   - <<<PAGE 164>>>："SNMP users and community strings need to be configured on devices before they can be managed by OmniVista."
4. 路由表缺 Loopback0 → 实验环境直接失败（需联系培训师）
   - <<<PAGE 90>>> Attention："IF THE ROUTING TABLE DOES NOT CONTAIN LOOPBACK0 ADDRESSES, PLEASE CONTACT THE TRAINER!"
5. 无可用快照 → 无法恢复 OV 初始配置
   - <<<PAGE 100>>>："IF NO SNAPSHOT IS AVAILABLE, PLEASE CONTACT YOUR TRAINER."（快照含 OV 的 IP、网关、network size 初始参数）。
6. 默认密码未改即无法继续 / 装完许可文件未删的隐患
   - <<<PAGE 101-102>>>：首登强制改默认密码（admin/switch → Training123#）才能进系统。
   - <<<PAGE 105>>>："Once the license file correctly inserted, please delete the file ('EVAL…') from the computer."
7. 误勾 Enable Fleet Supervision
   - <<<PAGE 104>>>：接受 EULA 时明确指示 "Check OK (don't check Enable Fleet Supervision)"，后面再次强调 "do not select the Enable Fleet Supervision option"。
8. HA 缺失时的业务中断反例（UPAM 认证停摆）
   - <<<PAGE 18>>>："If using UPAM, no new additional clients would be able to authenticate"（Main OV 失效且无 HA 时）。
9. 容量规划反例：High 档带 4000 AP 时交换机上限骤降
   - <<<PAGE 45>>>："**If there are 4,000 Stellar AP in a 'High' network size, up to 500 AOS switches can be supported. If there are 4,000 Stellar APs in a 'Very High' network size, up to 1,000 AOS switches can be supported."（选错 Network Size 会限制可管理规模）。
10. Trap 邮件Responder 不含 Normal 级别的配置注意点
    - <<<PAGE 192>>>："In the Trap Type section, disable the Normal trap so only the other severity levels are included in the mail."（不禁用会涌入正常事件）。
    - 前置条件：收 link trap 需交换机启用 `interfaces <slot>[/port] link-trap enable`（<<<PAGE 192>>> Note）。
11. VLAN 802.1X 客户端认证页签不可见的排查反例
    - <<<PAGE 266>>>："If Authentication tab is not available, click on the Start button, Run…, type services.msc … Look for Wired AutoConfig service and start it."
    - <<<PAGE 267-268>>>：必须取消 "Cache user information"、取消 "Automatically use my windows logon name and password"、取消 "Validate server certificate"，否则测试不成立。
12. 重新认证前未清 UNP 用户状态 → 残留会话干扰结果
    - <<<PAGE 268>>>："To ensure a clean status of the user ports on the 6860 … type: `-> unp user flush port 1/1/1`"，再禁用/启用网卡触发弹窗。
    - 同页 Note："You may see a second entry with a different MAC address. This is the link to the physical NIC associated with the client VM."（勿误判为异常）。
13. Client 拿不到 DHCP 地址的排障边界
    - <<<PAGE 290>>>："If Client07 does not get an IP address, then make sure that the AAA Training Server PodX VM is powered on. If this does not solve the issue, then assign a static IP address in the 192.168.80.X subnet with the default gateway set to 192.168.80.8"（IP helper 依赖 DHCP 服务器 VM）。
14. UNP 命名不一致 → RADIUS 返回值匹配失败
    - <<<PAGE 263>>> Notes："Type the UNP name as shown as it is the value returned from the RADIUS server"（Access Role Profile 名必须与 Filter-ID 完全一致，否则用户落不到 profile）。
15. 签名 Profile / 统计 Profile 的"一机一档"限制
    - <<<PAGE 342>>>："Note: A switch can only be in one profile of a particular Profile Type."（Analytics Profile）。
    - <<<PAGE 372>>>："A switch can be assigned only to one Signature Profile."（AppVis）。
    - <<<PAGE 391>>>："If you create a new profile, you will first have to unassign the 'Default Profile' from the desired switches."（统计采集）。
16. "NO DATA AVAILABLE" 并非故障——数据生成时延
    - <<<PAGE 380>>>："you should see a 'NO DATA AVAILABLE' warning. The main reason is that no traffic has been already generated from the client 8 … 'App Discovery' will only display the traffic captured after the generation of the internet traffic."
    - <<<PAGE 382>>>："Wait for 15-20 minutes before the applications are displayed in the OV widgets."
17. 自定义数据 3 个月上限与滚动覆盖
    - <<<PAGE 324>>>："You can display up to 3 months of data. When data reaches the 3-month maximum, it is overwritten with new data."
18. 应用端口映射导入会覆盖现有映射
    - <<<PAGE 351>>>："An existing application ports mapping file (.json file) can be imported … Note that this new mapping will override the existing mapping."
    - 未映射端口显示为 "Unknown"（<<<PAGE 350>>>）。
19. QM 内置规则默认全部禁用（以为开了其实没开）
    - <<<PAGE 304>>>："By Default all of the rules are disabled."
20. Candidates List 设备流量不被阻断的语义陷阱
    - <<<PAGE 308>>>："If a device is placed on the Candidates List, traffic to and from that device will continue until the Network Administrator decides what action should take place."（误以为进候选名单即隔离）。
21. Control Panel 误停服务的课堂警告
    - <<<PAGE 221>>>："(DO NOT modify or stop any process unless directed by your instructor!)"。
22. 镜像升级实验的环境约束与升级后手动动作
    - <<<PAGE 203>>>："DO NOT perform this section unless directed by your instructor."（镜像升级节）。
    - <<<PAGE 206>>>：升级完成信息须仔细读并照做：需 SSH 到交换机从 working 目录 reload，重启后执行 Copy Working Certified——漏做则升级不生效。
23. Thin Client 模式下直接改交换机配置的反例
    - <<<PAGE 75>>>："All configuration changes should be done in OV 2500."（thin-client 模式交换机本地不留 running 配置，本地改动无意义/会被覆盖）。
    - 版本边界："Thin Client is supported only on switches running AOS Release 8.8R1 (or higher)."
24. IoT 仅 IPv4 限制
    - <<<PAGE 404>>>："Note: IoT is supported on IPv4 devices only."
25. Mobile App 场景的连通性前提（未来版本功能边界）
    - <<<PAGE 415/451>>>："Mobile App: … Available in future release"——四个部署场景中的场景 1/2 依赖该未发布功能，当前不可实施。
26. 备份交换机 FTP 凭据缺失会中断备份向导
    - <<<PAGE 198>>>："Your switch may not have the FTP authentication credentials. Click on Add FTP Authentication if prompted."（须补 admin/switch 后数据库才同步）。
27. Check Service Stats 警告弹窗的处理
    - <<<PAGE 376>>>："A Check Service Stats warning message may appear. Click Ok if prompted."（AppVis Profile 应用时的已知提示）。
28. 远程实验室音频/剪贴板限制
    - <<<PAGE 195>>>："Due to the Remote lab Setup an audio device is not available to listen the notification sounds."
    - <<<PAGE 81>>>：Firefox 复制粘贴问题与 workaround 链接。
29. OVNA 设备不出现的排障边界
    - <<<PAGE 433-434>>>：需等待下次同步（每小时）；"Switches / APs need to be configured including managment IP, syslog configuration and make sure that OVNA is reachable from these devices"。
30. Sizing 环境变量影响实际容量
    - <<<PAGE 45>>>："Specific configurations may vary depending on the network, number of wired/wireless clients, number of VLANs, open applications, etc."（标称容量非保证值）。

## frameworks

1. Unified Access 三层策略模型（AAA Server Profile → Access Role Profile → Access Auth Profile → Unified Policy）
   - <<<PAGE 235>>>：Unified Profile Templates 定义各对象："Access Role Profiles. Contains the various UNP properties (e.g., QoS Policy List attached to the UNP, Access Policies, Captive Portal Authentication)"、"AAA Server Profile. Defines specific AAA parameters that can be used in an Access Auth Profile or a Captive Portal Profile"、"Access Auth Profile. Enables the assignment of a pre-defined UNP port configuration to an edge port"。
   - <<<PAGE 246>>>："Unified policies are part of the Access Role Profile configuration."（QoS 策略最终挂在 Access Role Profile 下）。
   - 实操链路证据：<<<PAGE 259-265>>>（先建 RADIUS Server → AAA Server Profile（AAA_RADIUS）→ Access Role Profile（UNP-employee）→ Access Auth Profile（UNP_template）→ Apply to Devices/Port）。
2. 用户角色导向访问策略（User Role Oriented Access Policy：Employee/Guest Profile 分别映射 VLAN/带宽/优先级）
   - <<<PAGE 231>>>：图示 "Employee Profile → VLAN 20, Employee Resources, Higher Bandwidth, Higher Priority"；"Guest Profile → VLAN 30, Internet Only, Lower Bandwidth, Lower Priority"，由 "OV 2500 / UPAM" 下发 "Employee/Guest Access Profile (ARP/UNP)"。
3. PolicyView QoS 规则配置四步法（Condition → Action → Rule → Apply）
   - <<<PAGE 275>>>："QOS RULE CONFIGURATION STEPS：Create a Policy Condition / Create a Policy Action / Create a Policy Rule / Apply the Policy"。
   - Expert Mode 向导五步：<<<PAGE 279-284>>>：Create Policy（名称/Precedence/高级选项）→ Device Selection → Set Condition（L2 MAC/L3 IP/DSCP/L4/L7）→ Set Action（QoS/Disposition/TCM）→ Validity Period and Review。
4. PolicyView 双模式框架（OneTouch vs Expert Mode）
   - <<<PAGE 273>>>："Operation modes: OneTouch for Voice, Data & ACL … Expert Mode. Advanced QoS controls for complex policies (including validation scheme)"；OneTouch "Sets parameters once, Distributed to devices at the same time"。
   - OneTouch 三子模式：Voice（<<<PAGE 276>>>）、Data（Platinum/Gold/Silver/Bronze 优先级，<<<PAGE 277>>>）、ACL（Accept/Drop，<<<PAGE 278>>>）。
5. Policy Flow（LDAP 策略仓库驱动的策略下发流程）
   - <<<PAGE 272>>>："Policies stored in LDAP server configured as part of OmniVista installation. Switches notified to retrieve new policies from this server."
   - <<<PAGE 286>>>：流程图：用户在 PolicyView 创建策略(1) → 存入 Policy Directory Server(2) → Policy Enabled(3) → Switches 从 LDAP 拉取(4)。
6. Discovery 配置流程（Profile 三段式 + IP 范围 + Discover Now）
   - <<<PAGE 110-112>>>：Discovery Profile 三段：General（Name/CLI-FTP 用户密码）、SNMP（版本/Timeout 默认 5000ms/v3 用户与 Auth-Priv）、Advanced（Trap Station User/Discover Link/Shell Preference Telnet 或 SSH/Use Get Bulk/Max Repetitions）。
   - <<<PAGE 113-114>>>：先定义 IP 地址范围并关联 SNMP 设置，再 "click on the Discover Now button"。
   - 实操：<<<PAGE 170-172>>>（Network → Discovery → Discovery Profiles → + → 填三段参数 → Managed Devices → Discover New Devices → Start/End IP → Discover Now → Finish）。
7. OV2500 容量规划（Sizing）决策框架：Network Size 四档
   - <<<PAGE 45>>>："PLATFORM AND SIZING REQUIREMENTS … OmniVista allocates memory based on the network size selected during installation"；"If there are 4,000 Stellar AP in a 'High' network size, up to 500 AOS switches can be supported. If there are 4,000 Stellar APs in a 'Very High' network size, up to 1,000 AOS switches can be supported."
   - <<<PAGE 58>>>：Network Size 分档表：Low <500 / Medium 500-2000 / High 2000-5000 / Very High 5000-10000 台设备。
   - <<<PAGE 44>>>：容量上限：10000 devices、4000 Stellar APs、5000 VMs。
8. Virtual Appliance 安装部署序列框架
   - <<<PAGE 55-60>>>：Deploy VA（从 BPWS 下载）→ Power on → Hypervisor Console 依次填 Initial Settings（键盘/cliadmin 密码）→ IP Settings（OV IP/HTTP-HTTPS 端口/Captive Portal/Additional OV Web）→ Network Size → Additional Options（Hostname/DNS/NTP/Timezone/Routes）→ Exit & Reboot。
   - <<<PAGE 54>>>：vSphere OVF 部署向导步骤（"Disk formatting (Thin or Thick Provision). (Thick provision is recommended.)"）。
9. License 类型决策框架（Device License vs Service License；Starter/Evaluation/Production）
   - <<<PAGE 46-49>>>：两类许可（Device/Service）；Device 三型：Starter Pack（免费 30 台：10 AOS+10 三方+10 Stellar）、Evaluation（90 天 60 台）、Production（最多 10000 台）；Service：VM/Guest/On-Boarding/HA/Web Content Filtering。
   - <<<PAGE 50-51>>>：HA 许可自 4.3R1 起，"you don't have to double the licenses on the redundant system"；节点计数规则：VC 内每台物理设备 1 license（"VC of 2 = 2 license units"）。
10. Quarantine Manager 攻击检测与遏制框架（Detection → Rules → Enforcement → Responder）
    - <<<PAGE 303-307>>>：检测（AOS AlaDosTrap/Syslog 事件）→ 规则（内置+自定义：名称/描述/触发表达式/提取表达式/动作）→ 执行（Quarantine VLAN (vlan 999 <mac>) / ACL / Port shutdown / 黑名单）。
    - <<<PAGE 304>>>："By Default all of the rules are disabled"。
    - <<<PAGE 308-310>>>：三列表决策模型：Candidates（等待管理员决策）/ Banned（隔离直至手动释放）/ Never Banned（OV 自身与已发现交换机隐式加入）。
11. Template Based Provisioning 部署场景决策框架（4 场景矩阵）
    - <<<PAGE 418/451>>>：场景表：①Mobile App 离线+可选 Basic DHCP（无 3G/4G 远程站点）②Mobile App 在线（有电话网络）③Advanced DHCP+RCL（企业/园区）④仅 Advanced DHCP（企业/园区）。
    - <<<PAGE 414>>>：三阶段状态模型：Factory-default（隔离不可用）→ Bootstrapped（有限连通，待 Provisioning）→ Provisioned（完全受管）。
12. 动态模板 + 值映射（Value Mapping）实例化框架
    - <<<PAGE 463-464>>>：模板可为 Static（无变量）或 Dynamic（带 $VLAN/$PORTS 变量）；动态模板必须创建 Value Mappings，模板+变量值表推导出实际下发给交换机的配置。
13. Application Visibility 四步配置框架（Signature File → Signature Profile → Apply to Devices → 报表/强制）
    - <<<PAGE 373-375>>>：向导步骤：创建 Profile 名 → 选择 Signature File → Monitor Flow Count 组（建 App Group）→ Bandwidth Usage and Enforcement 组（配 ACL/QoS：Disposition DROP）→ Create Profile → Apply to Devices 选端口。
    - <<<PAGE 365-366>>>：策略归一化："The Policy has to be included in a Policy List. Then, the Policy List is included as part of the Access Role Profile configuration."
14. Analytics 报表体系框架（Visibility vs Availability；Profile 先行）
    - <<<PAGE 317-318>>>：两类报表（Visibility：Top N Apps/Clients/Ports/POE；Availability：设备状态/Alarms）；"To generate an Analytics Report for any of the 'Visibility' Reports, you must first create an Analytics Profile"。
    - <<<PAGE 321>>>：KPI-机制-结果对应表：Top N Apps ← sFlow sampling + TCP/UDP 端口识别；Top N Switches ← CPU/内存/温度派生指数；Top N Port ← SNMP MIB Polling。
15. Access Classification 回退分类规则框架（认证不可用时按规则定 Profile）
    - <<<PAGE 243>>>："If authentication is not available or does not return a profile name for whatever reason, Access Classification rules are applied to determine the profile assignment."
    - <<<PAGE 244>>>：有线规则类型（Port/MAC/MAC OUI/MAC+Port/MAC+IP+Port/LLDP/认证类型/IP+Port）；无线规则类型（MAC/BSSID/ESSID/DHCP Option/DHCP Option 77/加密类型/位置）。

## principles

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
