# ACFE WLAN - Basic Deployment With OmniVista Ed04 · 案例(Lab 实操)提取
# 来源:fulltext.md(585 页)+ figures_captions.md(351 条插图标注)
# 说明:条目为书中亲自演练、可复现的 Lab 与配置样例;X 统一代表学员 POD 编号(25-32)

- id: c01
  title: 连接并使用 Stellar 远程实验室(R-Lab)
  type: case
  source_chapter: "p69"
  source_quote: |
    "A web browser is required to connect to the Rlab ... Rlab access URL: https://rdp.al-mydemo.com/ ... Username: Refer to the table below to get the corresponding 'User Account' to the Rlab type you are using ... Password: unique per session - sent from our LMS to the Instructor"
  summary: |
    Lab 目标:学会连接 Stellar 远程实验室(R-Lab),认识实验拓扑与各类设备入口。
    关键步骤:1) 用浏览器(推荐 Chrome/Edge)访问 https://rdp.al-mydemo.com/,账号形如 stellanpod25a(POD 25-32),密码由培训系统发讲师;2) 拓扑为三层结构:接入层 OS-2360/OS-6360(学员配置)、汇聚层 OS-6870(保留脚本预配置)、核心 OS-6900(不管理),服务器侧 DHCP(AAA Training Server)与 pfSense NAT/Firewall 不允许改动;3) 桌面快捷方式 SW7-OS-6870A/SW5-OS-6360A/SW4-OS-2360 打开 TeraTerm 交换机控制台(遇 "Hunting Group Busy" 说明控制台被其他会话占用);4) RealVNC 连 WifiClientX 树莓派(user/superuser),用 "Clean Wireless Networks" 清除已存网络;5) vSphere 打开 client5 有线客户端 VM。
    涉及参数:POD 账号对照表;DHCP 服务器预配 scope(VLAN10 192.168.10.70-79 / VLAN20 192.168.20.70-79 / VLAN30 192.168.30.70-79)。
    验证方法:交换机控制台有输出、VNC 能登树莓派、client5 控制台可打开。
  tags: [lab, rlab, remote-lab, topology, console]

- id: c02
  title: R-Lab 设备重初始化(Reset_PodX 脚本)
  type: case
  source_chapter: "p77"
  source_quote: |
    "Reset all the R-Lab's equipment by using the Reset_PodX script (X = R-Lab Number) ... Open the DT00CTE210 directory ... Double click on the Reset PodX - DT00XTE210 shortcut ... @OmniSwitch switch > The reinitialization process takes around 5 minutes ... @OmniAccess Stellar Access Point > The reinitialization takes around 1min30 - 2min"
  summary: |
    Lab 目标:把 R-Lab 全部交换机与 AP 重置为课程默认配置。
    关键步骤:1) 桌面 DT00CTE210 目录下双击 "Reset PodX - DT00XTE210" 快捷方式,弹出多个命令窗口等待自动消失;2) 注意交换机重置后"默认配置"并非空配置——所有端口被禁用,后续 Lab 需逐个启用;3) 重置 WifiClient 树莓派:user/superuser 登录,"Clean Wireless Networks" → Execute 删除全部已存无线网络。
    涉及参数:交换机重置约 5 分钟,AP 约 1 分 30 秒-2 分钟;初始状态 OS-2360/6360 无配置且端口禁用,AP1301/AP1321 为出厂设置。
    验证方法:命令窗口消失后设备可登录;树莓派无线列表为空。
  tags: [lab, rlab, reset, how-to]

- id: c03
  title: 设备启动与连接(OmniSwitch 6360 控制台 + AP1321 配置向导)
  type: case
  source_chapter: "p108"
  source_quote: |
    "OS6360-XTE210 -> interfaces 1/1/6 admin-state enable ... OS6360-XTE210 -> ip interface int_1 address 192.168.1.2/24 vlan 1 ... -> show ip interface ... -> write memory flash-synchro ... Modify the administration password: superuser ... Create the SSID 'AdminX'"
  summary: |
    Lab 目标:首次通过控制台配置 OS-6360,并用配置向导初始化 Stellar AP1321。
    关键步骤:1) SW5-OS-6360A 控制台登录 admin/switch;2) 启用端口 `interfaces 1/1/6 admin-state enable`(AP 口,AP 由 6360 PoE 供电)和 `interfaces 1/1/1 admin-state enable`(client5 口);3) 建管理 IP `ip interface int_1 address 192.168.1.2/24 vlan 1`,`show ip interface` 验证,`write memory flash-synchro` 保存;4) client5 VM 手工改 IP 192.168.1.200/24,浏览器访问 192.168.1.254:8080,Administrator/admin 登录 AP;5) 向导:管理员密码改 superuser → 选国家/时区 → 建 SSID AdminX(X=POD 号)密码 superuser(替代默认 mywifi-XXXX);6) 改 AP IP:AP 页 → Detailed Information → IP Mode > Edit → Static 192.168.1.3/24 网关 192.168.1.2 → 用 192.168.1.3:8080 重连。
    附录(重初始化):AP 按住 Reset 10 秒,或控制台(support/aos2016)`ssudo firstboot -y` + `ssudo reboot`;交换机(勿在 R-Lab 实操)`rm /flash/working/vcboot.cfg` + `reload from working no rollback-timeout`。
    验证方法:show ip interface 显示 int_1 UP;AP 新 IP/新密码可登录。
  tags: [lab, omniswitch, console, stellar-ap, wizard, poe]

- id: c04
  title: PoE、VLAN 与 DHCP 配置(Express 阶段网络基础)
  type: case
  source_chapter: "p121"
  source_quote: |
    "OS6360-XTE210-> show lanpower slot 1/1 ... OS6360-XTE210-> vlan 10 name Management-AP ... vlan 20 name Employees ... vlan 30 name Guests ... vlan 10 members port 1/1/6 untagged ... Select IP Mode: DHCP ... mywifi.al-enterprise.com:8080"
  summary: |
    Lab 目标:验证 PoE、创建三个业务 VLAN 并做端口划分,把 AP 改为 DHCP 取址。
    关键步骤:1) `show lanpower slot 1/1` 查看 PoE(1/1/6 端口 7000mW、Class 4、Powered On,默认开启无需配置);2) `vlan 10 name Management-AP`、`vlan 20 name Employees`、`vlan 30 name Guests`,`show vlan` 验证;3) 端口分配:上联口 1/1/3 三个 VLAN 全 tagged;AP 口 1/1/6 VLAN10 untagged(默认 VLAN)+ VLAN20/30 tagged;`show vlan members port 1/1/6` 验证;`interfaces 1/1/3 admin-state enable` 打通上联;4) 树莓派连 AdminX(手工 IP 192.168.1.201/24)→ 192.168.1.3:8080 → AP → IP Mode 改 DHCP → Save;5) 客户端改回 Automatic(DHCP)重连,此后用域名 mywifi.al-enterprise.com:8080 访问 AP 管理页。
    验证方法:AP 详细信息面板显示 DHCP 分配的 IP;附录用 `show mac-learning` 核对 AP 的 MAC(dc:08:56:xx)与端口。
  tags: [lab, poe, vlan, dhcp, cli, omniswitch]

- id: c05
  title: Express 模式下创建 Employee 与 Guest SSID(AP 本地 Web)
  type: case
  source_chapter: "p144"
  source_quote: |
    "WLAN name: EmployeesX ... Security: Personal ... Password: superuser ... Enter VLAN ID: 20 ... WLAN name: GuestsX ... Security: Open ... Captive Portal: Yes ... Fill the VLAN ID: 30 ... UserName: Guest ... Password: superuser"
  summary: |
    Lab 目标:在 Stellar AP1321 内置 Web 管理界面创建带密码的员工 SSID 和带 Captive Portal 的访客 SSID,分别落到专属 VLAN。
    关键步骤:1) mywifi.al-enterprise.com:8080 登录(Administrator/superuser);2) WLAN → New:EmployeesX(X=POD 号),Security Personal,密码 superuser,Advanced → VLAN ID 20;3) 测试:树莓派连 EmployeesX 密码 superuser,`ifconfig` 应得 192.168.20.70-79,网关 192.168.20.7(OS-6870 的 VLAN20 接口),AP Web 的 Clients 页可见该终端;4) GuestsX:Security Open、Captive Portal Yes,VLAN 30;5) Access → Authentication 选 Account 模式,Add 账户 Guest/superuser 并设起止有效期(大小写敏感);6) 访客连接后浏览器开任意非 https URL(如 http://2.2.2.2)被重定向到内置 Portal,输入 Guest/superuser 并接受条款。
    验证方法:员工/访客分别拿到 192.168.20.x / 192.168.30.x 池内地址。
  tags: [lab, ssid, express-mode, captive-portal, guest, employee]

- id: c06
  title: 附录:把 Stellar AP 配置为内嵌 DHCP 服务器
  type: case
  source_chapter: "p154"
  source_quote: |
    "Fill the following IP settings for the vlan10: IP Address: 192.168.10.3, Subnetwork: 255.255.255.0, DNS: 192.168.10.3 ... Pool name: Employees ... Gateway: 192.168.10.3 ... Range Start: 192.168.10.10 ... Range Stop: 192.168.10.50 ... Select Bind Network: vlan10"
  summary: |
    Lab 目标:不依赖外部 DHCP 时,用 AP 内置 DHCP 服务给 SSID 用户分配地址。
    关键步骤:1) AP 页点击 AP IP 打开新标签 → Network → AP Networks → vlan10 行 Manage:IP 192.168.10.3/24,DNS 192.168.10.3;2) Service → DHCP → Create:Pool name Employees,Subnet /24,Gateway 192.168.10.3,Range 192.168.10.10-50(40 个地址),DNS1 192.168.10.3;3) Action 下拉 → Bind Network → vlan10 保存;4) vlan20/Guests 同理:AP IP 192.168.20.3/24,Pool Guests,Range 192.168.20.10-50,绑定 vlan20。
    验证方法:DHCP 页显示池大小 41 且开始分配;接入对应 SSID 的终端获得池内地址。
  tags: [lab, annex, dhcp, ap-embedded, ssid]

- id: c07
  title: 附录:用户行为日志、Operator 账号与外部 RADIUS 认证
  type: case
  source_chapter: "p158"
  source_quote: |
    "At the bottom of the page, enable Client Behavior Tracking ... Then, select the desired Log To Server (ex. TFTP server) ... - Operator: Enable, Password: superuser ... Security: Enterprise ... AuthServer: IP@ of the RADIUS server (ex. 192.168.1.250)"
  summary: |
    三段附录实操:1) 用户上下线日志:Access → Authentication → 底部启用 Client Behavior Tracking,Log To Server 选 TFTP/SFTP/Syslog,填服务器 IP、端口、远程路径、发送周期;日志行含事件时间、客户端 MAC/IP、AP MAC、SSID、ONLINE/OFFLINE 状态;2) Operator 受限账号:System → General → Account Management → Operator Enable(密码 superuser),注销后以 GuestOperator 登录即得仅供管理访客账户的简化界面;3) 外部 RADIUS:WLAN → New,WLAN name EmployeesX,Security Enterprise,AuthServer 填 RADIUS IP(如 192.168.1.250),AuthSecret 填共享密钥,VLAN ID 10。
    验证方法:TFTP 服务器收到 ONLINE/OFFLINE 日志文件;GuestOperator 登录只见访客账户管理页。
  tags: [lab, annex, logging, operator, radius, captive-portal]

- id: c08
  title: 配置样例:isc-dhcp-server 用 DHCP Option 138 指向 OmniVista
  type: case
  source_chapter: "p33"
  source_quote: |
    "class \"STELLAR\" { match if substring (option vendor-class-identifier, 0, 4) = \"HAP.\"; } ... option ovwma code 138 = ip-address; ... pool { allow members of \"STELLAR\"; range 192.168.10.10 192.168.10.20; option ovwma 192.168.0.61; }"
  summary: |
    书中给出的 Linux isc-dhcp-server 配置样例(p17 与 p33 两处),用于把 Stellar AP 引导到 OmniVista 2500(Enterprise 模式)。
    关键内容:1) 用 vendor-class-identifier 前 4 字节 "HAP." 把 Stellar AP 归入 "STELLAR" 类;2) 因 138 非标准选项,先声明 `option ovwma code 138 = ip-address;`;3) 在 AP 专用 pool 内 `allow members of "STELLAR"` 并下发 `option ovwma 192.168.0.61`(OV2500 地址);OmniSwitch 做 DHCP 服务器时的 dhcpd.conf 对应写法为 `option 138 192.168.0.61;`。
    验证方法:AP 获取地址并向 option 138 指定的 OmniVista 注册(模式选择流程:有 138 → Enterprise;无 138 且未在 Cirrus 登记 → Express)。
  tags: [config-example, dhcp, option-138, linux, omnivista-2500]

- id: c09
  title: OmniVista Cirrus 账号创建、组织与许可证订阅流程
  type: case
  source_chapter: "p169"
  source_quote: |
    "1) URL: https://ebuy.businesspartner.al-enterprise.com/ ... 2) Create a new shopping cart and select: 'Other Services & Items Section' ... 3) In the tab 'Your purchased license', locate your order and select the Action 'Create a subscription' ... 4) Select: CAPEX Subscription ... Enter: Subscription ID, Activation Code"
  summary: |
    配置样例(全书用整章截图演示):1) 许可订购:eBuy 下单,许可参考号如 OVCX-68-BAS-3Y(级别 BAS/BIZ/PRM,年限 1Y/3Y/5Y,按设备类别);2) 订阅创建:MyPortal > OVC Subscription Manager 选 OmniVista CIRRUS → Your purchased license → Create a subscription,填客户唯一名/国家,记录 Subscription 与 Order ID;3) 账号:https://eu.manage.ovcirrus.com(EU)或 us(Americas),分 Partner/Customer 账号,一个邮箱只能绑一个 MSP 门户,可用子地址 MyMail+sub@company.com 复用;4) 组织:MSP Dashboard → Create Organization(名称/强密码策略/国家时区)→ Request a trial period(填 ALE 联系人、是否 RAP 模式、Partner CRD ID)→ 邮件批准;5) 导入:License Management → import licenses → CAPEX Subscription → 输 Subscription ID + Activation Code → 选设备分配 → Upgrade → 验证许可模式/时长/型号数量;附录含 OVC4 → OVC10 迁移步骤(先删 OVC4 设备目录再等 Call Home)。
    验证方法:组织状态变为已授权,License Management 显示已导入许可证。
  tags: [config-example, licensing, subscription, organization, account, cirrus]

- id: c10
  title: Lab:远程实验室重初始化(Cirrus 课程预配置加载)
  type: case
  source_chapter: "p238"
  source_quote: |
    "On the Remote Desktop Connection, go to the folder 'OmniVista CIRRUS 10' located on the desktop and double-click on the script called 'reset_PODX' ... -> ping 192.168.100.102 (Connection to the DHCP server) -> ping www.google.com (Connection to Internet) ... -> ssudo ping 192.168.100.102"
  summary: |
    Lab 目标:在进入 Cirrus 系列实验前,为三台交换机(OS-6870/6360/2360)与两台 AP(AP1301/1321)加载课程网络预配置(VLAN、IP、路由已由脚本预配,学员在其上叠加)。
    关键步骤:1) 桌面 "OmniVista CIRRUS 10" 目录运行 reset_PODX;脚本先关掉全部控制台会话,再依次重置 AP 与交换机;2) 交换机重启期间严禁按键(否则落入 Miniboot 中断启动);3) 等待数分钟后验证:三台交换机控制台(admin/switch)`ping 192.168.100.102`(DHCP 服务器)与 `ping www.google.com`;AP1301 控制台(support/aos2016)`ssudo ping 192.168.100.102`、`ssudo ping www.google.com`。
    验证方法:上述 ping 全通;AP1321 此时无法 ping 通属预期(所连 OS-6360 尚未配完,留待后续 Lab)。
  tags: [lab, rlab, reset, preconfiguration, cirrus]

- id: c11
  title: Lab:环境创建(站点/楼宇/楼层)与 OmniSwitch 上云 Onboarding
  type: case
  source_chapter: "p241"
  source_quote: |
    "Go to INVENTORY > DEVICE CATALOG ... Click on '+ Create Device' ... In the Device Family, select 'OmniSwitch' ... -> show chassis ... Serial Number: V3281742 ... OS6870 & OS6360 -> cloud-agent admin-state restart ... 'Connected to OV', followed by 'Provisioning' and 'OV Managed'"
  summary: |
    Lab 目标:在 OmniVista Cirrus 组织中创建站点并把 OS-6870A、OS-6360A 以现有配置上云管理。
    关键步骤:1) 登录 https://eu.manage.ovcirrus.com(pod##@ale-training.com / Superuser01!),进入 Training POD## 组织(另一 Common Training Organization 仅 Viewer);2) 建站点:ORGANIZATION → Sites Management → Sites → +Create Site,名 My Site、FR-France、Europe/Paris、默认站点 YES,地址栏搜 "115 rue Antoine de St Exupéry 29490 Guipavas",缩放到绿色提示后 Create;3) 建 Building A 与 Ground Floor(楼层号 0、海拔 0),导入平面图 C:\Resources\Site-Brest-plan,全屏缩放旋转对齐地图,Draw the Floor Perimeter 勾勒周界(约 1200-1300 m²);4) 上云 6870A:Device Catalog → +Create Device → OmniSwitch,控制台 `show chassis` 取序列号(示例 V3281742),软件选 Do Not Upgrade,分配 My Site/Building A/Ground Floor,Initial Configuration 不选模板,Management User Template 用 Default → Create;6360A(SN WHS233501662)同理;5) 激活:状态从 Waiting for validation → Waiting for first Contact,可 `cloud-agent admin-state restart`(推荐)或 `reload from working no rollback-timeout` 强制 Call Home,约 2 分钟到 OV Managed;`show cloud-agent status` 确认 DeviceManaged/completeOK。
    排障:L2 `show interfaces 1/1/5`、`show vlan members port 1/1/5`;L3 `show ip interface`(如 int_217 172.16.17.7)、`ping eu.activation.ovng.myovcloud.com`;OVC 端 Action > Diagnostic Tools > View Activation Log。
  tags: [lab, cirrus, site, floor-plan, omniswitch, onboarding, cloud-agent, troubleshooting]

- id: c12
  title: Lab:Stellar AP 上云 Onboarding 与 AP Group/Provisioning 配置
  type: case
  source_chapter: "p293"
  source_quote: |
    "-> vlan 10 name AP-MGMT -> vlan 10 members port 1/1/6 untagged -> vlan 10 members port 1/1/3 tagged ... showsysinfo ... SN:SSZ231200742 ... name your AP Group: 'My-AP-Group' ... name your AP Group: 'My-Provisioning-Config' ... The Device Activation Status should display 'OV Managed'"
  summary: |
    Lab 目标:把 AP1321、AP1301 声明到 OmniVista Cirrus 并纳入同一 AP Group(两 AP 共用同一 Provisioning 配置)。
    关键步骤:1) OS-6360 预配置:`vlan 10 name AP-MGMT`、`vlan 10 members port 1/1/6 untagged`(AP 口)、`vlan 10 members port 1/1/3 tagged`(上联),否则 AP 拿不到管理 VLAN 地址;2) 添加 AP1321:Device Catalog → Device List → +Create Device → Stellar AP,控制台(support/aos2016)`showsysinfo` 取 SN(示例 SSZ231200742);3) 创建 AP Group:新标签页命名 My-AP-Group、选 My Site;4) 创建 Provisioning Configuration:新标签页命名 My-Provisioning-Config,Site=My Site,RF Profile=Default RF Profile,Timezone=Europe/Paris,其余默认;5) 返回完成 Group 与设备创建(Building A/Ground Floor),勾 Create another 连续添加 AP1301(SN SSZ231201971)入同组;6) 激活:重启 AP(`ssudo firstboot -y`、`ssudo reboot`)或等 Call Home,状态 OV Managed;CLI `ocloud_show` 验证(VPN Status: connected,AP IP 192.168.10.71,Activation Server eu.activation.ovng.myovcloud.com)。
    排障:`show lanpower slot 1/1`(PoE)、`show vlan members port 1/1/6`(VLAN10 default forwarding)、Reset 键 6 秒或串口 115200 8N1 进 console `ssudo firstboot`;`getmode` 应为 OVNG;`cat /etc/config/network` 确认 proto dhcp;`ssudo ifconfig br-wan` 看 IP;`getovinfo` 返回激活服务器 IP;L3 `show ip interface`(int_management 192.168.10.7/27)与 `ssudo ping eu.activation.ovng.myovcloud.com`。
  tags: [lab, cirrus, stellar-ap, ap-group, provisioning, onboarding, troubleshooting]

- id: c13
  title: Lab:Employee SSID 创建(802.1X + UPAM)及排障
  type: case
  source_chapter: "p332"
  source_quote: |
    "> Profile Name: EmployeesX ... > Usage: Enterprise Network for Employees (802.1X) ... > Encryption Type: WPA2_AES ... > RADIUS Server: UPAMRadiusServer ... > Set the Authentication Source option to Local Database ... In the VLAN/Tunnel Mapping window, set the Choose Network Mapping to VLAN ... Set the VLAN ID to 20"
  summary: |
    Lab 目标:在 Cirrus 上完成 VLAN 20 → IP 接口 → 802.1X 员工 SSID → 账号 → 测试 → 监控全流程。
    关键步骤:1) VLAN:LAN → Layer 2 → VLAN → +Create VLAN(ID 20,描述 Employee,选 OS-6870A tagged 1/1/3+1/1/8、OS-6360A tagged 1/1/3+1/1/6);OS-2360 不受管,控制台手工 `vlan 20 name EMPLOYEE`、`vlan 20 members port 1/1/6 tagged`、`vlan 20 members port 1/1/8 tagged`;2) IP 接口:LAN → Layer 3 → IP Interface → +Create:int_employees,192.168.20.7/24,VLAN 20,IP Forward Enabled,部署到 OS-6870A;3) SSID:Wireless → SSIDs → +Create SSID,Profile EmployeesX,Usage=Enterprise Network for Employees(802.1X),WPA2_AES,2.4+5GHz;Authentication Strategy 选 UPAMRadiusServer → Manage Employee Accounts(新页)→ +Create Employee Account(Username Employee / Password password);Access Policy:Authentication Source=Local Database,Web Authentication=None;4) Network Assignments:Add Site=My Site、组=My-AP-Group(移除 default);Schedule and VLAN mappings:Edit My-AP-Group → VLAN 20 → Create;5) 测试:树莓派连 EmployeesX,参数 Authentication=ProtectedEAP、No CA certificate、PEAP version=Automatic、Inner Auth=MSCHAPv2,账号 Employee/password;应得 192.168.20.70-79,可 ping 192.168.100.102 与 192.168.20.7;6) 监控:Network → Access Records → Authentication Records;Network → Analytics → Clients。
    排障(AP CLI,support/aos2016):`iwconfig`(ESSID/信道/功率)、`iwlist ath101 channel|txpower|bitrate`、`ssudo sta_list`(终端 VLAN/角色)、`ssudo wlanconfig ath101 list`(RSSI/SNR)、`ssudo wam_debug sta_list`(JSON:assignedVLAN/assignedAR/各阶段认证结果)、`cat /proc/kes_syslog | grep <MAC>`;RADIUS 链路:`cat /var/config/wlanservice.conf`、`cat /var/config/AAA_profile.conf`(primaryServer=UPAMRadiusServer)、`cat /var/config/AAA_server.conf`(1812/1813、10.130.5.50),抓包 `tcpdump -i br-wan -s 0 host <radiusIP>`。
  tags: [lab, cirrus, ssid, 802.1x, upam, vlan, radius, monitoring, troubleshooting]

- id: c14
  title: 配置样例:PSK 家族四种密钥方案(PSK/DSPSK/PPSK/动态组 PSK)
  type: case
  source_chapter: "p324"
  source_quote: |
    "Device Specific PSK: Enabled ... Prefer Device Specific PSK ... Force Device Specific PSK ... Activate Private Group PSK and enter one/multiple entries: A name ... A unique passphrase ... A pre-configured Access Role Profile ... Each entry is linked to a VLAN ID and ARP ... Priority VLAN-ID over ARP: the VLAN ID from the Dynamic GPPSK entry is used for this user."
  summary: |
    SSID 创建向导中的四种预共享密钥配置样例(书中逐屏截图):1) 通用 PSK:Usage 选 Protected Network(或 Protected Network for Employees),启用 MAC 认证之外只设统一 PassPhrase,DSPSK/PPSK 均 Disable;2) Device Specific PSK(DSPSK):启用 MAC 认证 + Device Specific PSK,Force 模式=SSID 级无全局口令、每台设备在 Company Property 库按 MAC 配专用口令;Prefer 模式=设备优先用 MAC 认证返回的口令,否则回落全局 PSK;注意 AUTO_WPA_WPA2 加密不受支持;3) Private Group PSK(PPSK):DSPSK 关闭或 Prefer 时可配置多条"名称+唯一口令+预定义 Access Role Profile"条目,用户按所用口令落到对应角色;4) Dynamic Private Group PSK:DSPSK 设 Prefer + 启用 Dynamic Private Group PSK,每条 PSK 绑定 VLAN ID 与 ARP,配合 Dynamic VLAN Selection 的 Priority ARP over VLAN-ID / Priority VLAN-ID over ARP 决定归属,免去"每个 VLAN 建一个 ARP"。
    验证方法:不同口令登录的终端在 Clients/认证记录中呈现不同 VLAN 或 Access Role Profile。
  tags: [config-example, ssid, psk, dspsk, ppsk, access-role]

- id: c15
  title: Lab:Guest SSID 创建(开放 + OV-UPAM Captive Portal)与踢下线
  type: case
  source_chapter: "p372"
  source_quote: |
    "> Usage: Guest Network (Open or Captive Portal) ... > Do you want users to go through a Captive Portal? YES ... > Captive Portal Type: OV-UPAM Captive Portal ... Strategy Name: Guests_OVX ... > Login By: Username & Password ... Set the VLAN ID to 30"
  summary: |
    Lab 目标:创建 VLAN30 承载的开放访客 SSID,经 OV-UPAM Captive Portal 认证,并练习监控与强制下线。
    关键步骤:1) VLAN30 与 IP 接口同 Employee 流程:Create VLAN 30(描述 Guest,6870 tagged 1/1/3+1/1/8,6360 tagged 1/1/3+1/1/6),OS-2360 手工 `vlan 30 name GUEST` + 两口 tagged;IP 接口 int_guests 192.168.30.7/24 VLAN30 部署到 OS-6870;2) SSID:Profile GuestsX,Usage=Guest Network,Captive Portal=YES、类型 OV-UPAM Captive Portal,Enhanced Open Disabled;RADIUS=UPAMRadiusServer → Manage Guest Accounts → +Create Guest Account(Guest/password);3) Access Policy:Allow All EAPs=Yes、Authentication Source=None、Web Authentication=Guest;Create Guest Access Strategy(新页):Guests_OVX → Create Template(新页):My_CPTemplate_X 任选布局 → Login By=Username & Password;4) 分配 My-AP-Group 并映射 VLAN 30;5) 测试:连 GuestsX → 浏览器开 http://2.2.2.2 重定向 Portal → Guest/password + 接受条款,得 192.168.30.70-79,可 ping 192.168.100.102/192.168.30.7;6) 监控:Authentication Records 与 Network → Access Records → Captive Portal Records;Clients → Live Wireless Clients 点 MAC 看会话历史(roaming timeline、RSSI、吞吐、PHY 速率);7) 踢下线:Clients → 选用户 → Actions > Kick Off → Confirm,可重连验证。
    排障(AP CLI):`date`(访客账户有效期依赖正确时间)、`cat /etc/resolv.conf`(Portal 重定向依赖 DNS)、iwconfig/iwlist、`ssudo sta_list`;Portal 侧 `ps | grep eag`、`eag_cli show user all`(PORTAL 认证用户表)、`eag_cli kick user index 1`、`tail -f /tmp/log/eag.log`、`cat /proc/kes_syslog | grep eag`。
  tags: [lab, cirrus, ssid, guest, captive-portal, upam, monitoring, kickoff, troubleshooting]

- id: c16
  title: Lab:BYOD SSID 创建(预认证 Guest VLAN → 认证后切 Employee VLAN)
  type: case
  source_chapter: "p389"
  source_quote: |
    "> Usage: Employee BYOD Network ... we will reuse the VLAN 20 (Employee) and 30 (Guest). The BYOD employee device will be placed first in the Guest VLAN (pre-authentication). Once authenticated via a Captive Portal, it will be moved to the Employee VLAN (post-authentication)."
  summary: |
    Lab 目标:为员工自带设备(BYOD)建开放 SSID,Portal 认证前落 Guest VLAN30、认证后经 Post Portal Enforcement 移入 Employee VLAN20。
    关键步骤:1) SSID:Profile BYODX,Usage=Employee BYOD Network,2.4+5GHz,Enhanced Open Disabled;RADIUS 保持 UPAMRadiusServer;Access Policy:Authentication Source=None、Web Authentication=Employee(带出 BYOD Portal);2) Create BYOD Access Strategy(新页):My_BYOD_Strategy,Captive Portal 模板复用 My_CPTemplate_X,Authentication Source=Local Database(Employee/password 已存在);3) Post Portal Authentication Enforcement → Create Access Role Profile(新页):Employee_BYODX → Network Assignments 选 Group Assignment=My-AP-Group → VLAN mappings=VLAN 20 → Create;回 Strategy 页将 Access Role Profile 设为 Employee_BYODX;4) SSID 页选 BYOD Access Strategy=My_BYOD_Strategy,SSID 级 VLAN 映射设为 30(预认证);5) 测试:连 BYODX → Portal 输 Employee/password → MONITOR → Network → Analytics → Clients → Additional Information,Authentication 段 VLAN 应为 20。
    监控:Authentication Records 可见 VLAN 与 Access Role Profile=Employee_BYODX(证明 Portal 后角色生效);Captive Portal Records 可对照 Guest(前一 Lab)与 Employee(BYOD)两条记录。
    排障:`cat /etc/resolv.conf`、`iwconfig`(ath003/ath103)、`iwlist ath003 channel|txpower|bitrate`、`ssudo sta_list`(应显示 192.168.20.x、VLAN 20)、`ssudo wam_debug sta_list`(CPAuthResult 与 ARFromMACAuth/ARFromCPAuth)。
  tags: [lab, cirrus, ssid, byod, upam, post-portal, vlan, monitoring]

- id: c17
  title: Lab:Unified Policy 创建与绑定(Block_SSH 拦截测试)
  type: case
  source_chapter: "p411"
  source_quote: |
    "> Policy Name: Block_SSH ... > In the Choose a Condition box, select L3 IPs ... > IP Address: 192.168.20.0, > Subnet Mask: 255.255.255.0 ... > In the Choose a Condition box, select L4 Services ... Service Protocol: TCP ... Name the service Port: SSH ... Port Number: 22 ... > Accessibility: Drop ... > In the ACL/QoS box, select the Block_SSH policy"
  summary: |
    Lab 目标:创建一条"禁止员工 SSID 用户 SSH 到网关交换机"的统一策略,并验证策略生效。
    关键步骤:1) 基线测试:客户端连 EmployeesX,`ping 192.168.20.7` 通、`ssh admin@192.168.20.7`(密码 switch)通;2) 创建策略:Network Access → Unified Access → Unified Policies → +Create Unified Policy;Policy Name=Block_SSH;Condition 1 选 L3 IPs,Destination Subnet 192.168.20.0/255.255.255.0;Condition 2 选 L4 Services,Port(s)、TCP,Destination Port 无 SSH 选项时点 Add New → Create Service Port(新页):名称 SSH、Protocol TCP、Port 22;3) QoS Action:Accessibility=Drop;4) Group Assignment=My-AP-Group(确保不含 default 组)→ Create;5) 绑定:Wireless → SSIDs → EmployeesX → Edit → Default VLAN/Network 的 ACL/QoS 选 Block_SSH → Next → Save;6) 复测:ping 仍通、SSH 被拒绝。
    可扩展:同界面还有 L2/L3 优先级、Max Output Rate、三色标记(TCM)等带宽动作,以及 Location/Period 策略入口(More Settings for Default VLAN/Network)。
  tags: [lab, cirrus, unified-policy, acl, qos, ssh, security]

- id: c18
  title: Lab:RF 管理(自定义 RF Profile 与关联 RSSI 阈值实验)
  type: case
  source_chapter: "p456"
  source_quote: |
    "Enter the name 'My_RF_Profile'. Keep the country/Region 'FR-France' ... Modify the Association RSSI Threshold for all the bands to a value much higher than the Client value (ex. 90, which is higher than -41 dBm = 51) and click Save ... Set RF Profile to My_RF_Profile"
  summary: |
    Lab 目标:掌握 RF Profile 的创建、下发,并用"关联 RSSI 阈值"做一次可观测的接入失败实验。
    关键步骤:1) 创建:CONFIGURE → Wireless → Profile → RF Profiles → +Create RF Template,名 My_RF_Profile,国家 FR-France,描述自定义;Smart Load Balance 区含 Band Steering(默认关,5G 覆盖差时勿开或用 Exclude MAC OUI 豁免老终端)、Force 5G/6G、Roaming RSSI Threshold;Per Band Info 区含 Band/Channel Setting(Auto=ACS)/Client-aware/Channel DRM/Channel List/Channel Width/Power Setting/Min-Max TX Power(3-23dBm)/外部天线增益/Beacon 间隔/SGI/MU-MIMO/High Efficiency(802.11ax);2) 读客户端 RSSI:MONITOR → Network → Analytics → Clients → Live Wireless Clients 点客户端 MAC,记录 RSSI(如 -41 dBm=51);3) 把 My_RF_Profile 的 Association RSSI Threshold 全频段调到高于客户端值(如 90)保存;4) 下发:Wireless → Profile → Provisioning Configuration → My-Provisioning-Config → Edit → RF Profile=My_RF_Profile(也可 Device Catalog 对单 AP 覆盖);5) 验证:客户端断开重连 EmployeesX 无法关联;Network → Analytics → QoE → Successful Connects → More details,关联失败列表 Failure message 显示 RSSI 阈值未达;6) 回退:Provisioning Config 改回 Default RF Profile。
    排障:Device Catalog SSH(support/aos2016)`cat /tmp/config/rfprofile.conf` 查看下发的 signalStrengthThreshold 等;`cat /proc/kes_syslog | grep ACS` 查自动选信道日志。
  tags: [lab, cirrus, rf-profile, rssi, acs, qoe, troubleshooting]

- id: c19
  title: Lab:WIPS 配置与 AP 分类(Interfering/Rogue/Friendly)
  type: case
  source_chapter: "p521"
  source_quote: |
    "Signal Strength Threshold - Default: Disabled ... Detect Valid SSID - Default: Enabled ... In the tab Interfering AP, enter the value 'EmployeesX' in the research field ... Select all the entries from the table that start with the Stellar MAC OUI 'dc:08:56' ... Click on the button Action > Add to Friendly ... check the box 'Detect Rogue SSID Keyword' ... Enter the value 'EmployeesX'"
  summary: |
    Lab 目标:理解 WIPS 三分类(Interfering/Rogue/Friendly),练习把相邻 POD 的 AP 加为 Friendly 并验证 Rogue 策略对 Friendly 无效。
    关键步骤:1) 策略总览:CONFIGURE → Wireless → WIPS → Policy;Rogue AP Policy 四条件——Signal Strength Threshold(默认禁用,默认 -70dBm,范围 -50~-90)、Detect Valid SSID(默认启用,广播我方 SSID 即判 Rogue)、Detect Rogue SSID Keyword(关键字黑名单)、Rogue OUI;Containment Policy 默认启用(向 Rogue AP 的关联终端发 de-auth);AP/Client Attack Detection 可选 High/Medium/Low/Custom;Client Blocklist 默认 60 秒内认证失败 10 次拉黑、老化 1 天;2) Friendly 分类:Intrusive Access Points → Interfering AP 标签,搜索其他学员的 SSID "EmployeesX",勾选全部 dc:08:56 OUI 条目(每 AP 2.4/5G 各 1 BSSID、两台 AP 共 4 条且多 AP 扫描会重复)→ Action > Add to Friendly → 确认;Policy 页 Friendly MAC 列表可核对;3) 验证:勾选 Detect Rogue SSID Keyword 填 EmployeesX 保存,这些 AP 仍不进 Rogue 标签;客户端连该 SSID 正常;Network → Analytics → WIPS Analytics 的 Access Points 标签无 Rogue Detected,Clients 标签无 DeAuth Client 记录。
    验证方法:WIPS Analytics 与 Intrusive Access Points 三标签页状态;另一学员可在 Clients 中看到你的终端。
  tags: [lab, cirrus, wips, rogue-ap, friendly-ap, security]

- id: c20
  title: Lab:组织配置清理(Organization clean up 25 步)
  type: case
  source_chapter: "p542"
  source_quote: |
    "As OmniVista Cirrus is cloud-based, it is not possible to revert the configuration back to the default parameters with one click. You can use this lab as a guideline if you need to replace your network devices, move to a new office or building, or reconfigure your network."
  summary: |
    Lab 目标:把整个培训期间创建的对象按依赖顺序删除,还原组织(也可作为设备替换/搬场/重配的操作手册)。
    关键步骤(顺序即依赖):1) Inventory → Backup/Upgrade 删 Scheduled Upgrades 与 Configuration Backups;2) Inventory → Device Troubleshooting 删已分配命令;3) Wireless → WIPS → Policy → Apply to default;4) Device Catalog 两 AP → Edit Devices > Group/RF Profile 改回 default device group;5) Access Point Groups 把 My-AP-Group 的 Provisioning 改回 Default Provisioning Config 后删除组(组内不能挂自定义配置才可删);6) 删 My-Provisioning-Config(报错则先把其中 RF Profile 改回 Default)→ 删 My_RF_Profile;7) Wireless → SSIDs 全删;8) Network Access 下依次删 Unified Policies(Block_SSH)、Service Ports(SSH 22)、BYOD Access Strategy(My_BYOD_Strategy)、Access Role Profile(Employee_BYOD#)、Guest Access Strategy(Guest_OV#)、Captive Portal Templates(MyCPTemplate#)、Employee/Guest 账户;9) Network > Reports 删报表;Diagnostic Tools → Collect Support Info 清空;10) Sites Management 删 My Site(连带楼宇楼层与设备归属);确认 Device Catalog 为空;11) LAN → CLI Based Provisioning 删 Templates 与 Value Mappings。
    验证方法:Device Catalog 页显示"尚未创建设备"的空状态。
  tags: [lab, cirrus, cleanup, housekeeping, best-practice]

- id: c21
  title: Lab:RAP 远程接入点部署(OVC10 + ALE VPN Server + OmniVista 2500)
  type: case
  source_chapter: "p549"
  source_quote: |
    "Enter: Name: RAP-Organization, Country/Region: France, Timezone: Europe/Paris ... Click on + Create Mgmt VPN Settings ... Server's Public IP ... Port ... Server's VPN IP ... OmniVista Enterprise Server IP ... Client VPN IP Address Pool ... Transfer the <VPN Server name>.conf file in the folder /opt/OmniVista_2500_NMS/data/vpn_conf/vpn_profile"
  summary: |
    Lab 目标:把一台 Stellar AP 部署为远程接入点(RAP),经双重 VPN(管理流量 + 客户端数据 L2GRE)延伸公司网络到远端。
    参考地址规划:VPN Server 公网 IP(隐藏)/私网 10.130.5.251;vpn_mgmt 服务端 192.168.0.1、客户端池 192.168.0.2-20;vpn_data 服务端 10.7.0.61、客户端池 10.7.0.55-60;OV2500 10.130.5.50;管理网 VLAN1305(10.130.5.x)、员工网 VLAN30(10.7.0.x)。
    关键步骤:1) OVC10:建 RAP-Organization(法国/Europe-Paris/Strong 密码)→ Request Teaser Period(选 RAP 部署=Yes);CONFIGURE → Wireless → Mgmt VPN Settings → +Create(Name、Server Public IP、Port 如 6550、Server VPN IP 192.168.0.1、OV Enterprise Server IP、客户端池 192.168.0.2-20);Device Catalog 声明 AP(SN 取机身标签或 `showsysinfo`),RAP 段选该 VPN 配置;AP 接互联网后注册;Action > Export 导出 .conf;2) VPN Server VA(附录:ESXi Deploy OVF Template 部署):控制台首启设 admin 密码(如 Alcatel.0);NIC1 公网/NIC2 私网地址、默认网关、DNS;启用 SSH(端口 6550);FileZilla(SFTP 22)把 .conf 传到 /opt/OmniVista_2500_NMS/data/vpn_conf/vpn_profile;Network Services 建 vpn_(vpn_mgmt,公网 IP+端口);Network Endpoints → Configure a VPN endpoint 选 vpn_mgmt+conf+None(Layer 3 VPN)→ Apply;3) 重启 AP 建管理隧道,VA 控制台 Maintenance → VPN Status 应出现 peer(公网 IP、最新握手、收发字节);4) OV2500:VA 控制台 [2]Configure → [8]Configure Route → [3]Add Route v4(192.168.0.0/24 网关 10.130.5.251);Web(10.130.5.50)→ NETWORK → AP Registration → Access Points 出现 Managed AP(选国家/时区);Data VPN Servers 新建(公网 IP、端口、Server VPN IP 10.7.0.61、池 10.7.0.55-60)→ Export VPN Settings;AP Group(default)Data VPN Setting 选该 VPN → Commit;建员工 SSID(WLAN → SSIDs,Usage=Enterprise Network for Employees,加密 WPA3_AES,RADIUS=UPAMRadiusServer,Employee/password,Default VLAN/Network 选 Use Tunnel、Tunnel ID 0、选 VPN Server)→ Save and Apply;5) VPN Server 二次导入:上传第二个 .conf,建 vpn_data(端口如 6551),endpoint 绑 eth2,Apply;6) 远端验证:Windows 连 EmployeesX 输 Employee/password,获得员工网段地址。
  tags: [lab, rap, vpn, ovc10, omnivista-2500, remote-deployment, gre-tunnel]

- id: c22
  title: Wi-Fi 现场勘测方法论(被动/主动/预测 + Ekahau 三步排障)
  type: case
  source_chapter: "p526"
  source_quote: |
    "Passive: Listen WLAN traffic, No authentication and 802.11 association, All frequencies are scanned ... Active: Associate survey tool to (multiple) access point ... Measure packets loss, Measure retransmission, Measure physical rates ... Predictive: Simulation tool, Import site plan & RF characteristics of objects ... Learn how to perform and analyze a passive site survey with Ekahau mapper"
  summary: |
    课程演示案例:如何选勘测类型并按三步法排障(工具:Ekahau Site Survey on Windows、WiFi Analyzer on Android)。
    关键内容:1) 类型选择:新部署/换网用 Predictive(导入平面图与材质损耗建模、自动布 AP)+ 部署后 Passive(RF 环境、干扰、覆盖);性能排障用 Active(关联 AP 测丢包/重传/物理速率);2) 信号劣化四大原因:AP 摆位(正对混凝土立柱/墙造成盲区)、材质衰减(混凝土、木门、金属柜、钢结构、玻璃镜面、砖、水体)、天线类型错配(定向 vs 全向覆盖形状)、同频/邻频干扰(对策改信道);3) 现场排障三步:Step1 取平面图,标注障碍、高低优先级区域与 AP 位置;Step2 勘测观察五项——AP 型号是否与设计一致、AP 间 RF 重叠与同/邻频干扰、无覆盖区(AP 宕机或漏布)、发射功率是否默认值(默认 17dBm,覆盖不足可加大)、位置是否不当;Step3 纠正动作:换 AP 型号、改功率/信道/信道宽度、砍低速率逼终端走更近 AP、优化摆位或新增 AP(用例:修改单 AP 发射功率、新增 Stellar AP、挪 AP)。
    验证方法:勘测热图中同频干扰消除、盲区消除、RSSI 恢复到推荐区间(参考书内 RSSI-dBm 对照表:-65 以上为理想,低于 -80 不适合音视频)。
  tags: [survey, ekahau, rf-troubleshooting, site-survey, methodology]

- id: c23
  title: 客户端账号与配额管理样例(Employee/Guest/Company Property/Guest Operator)
  type: case
  source_chapter: "p417"
  source_quote: |
    "Creation of client accounts in the UPAM local database. Used to define network access control: Employee Accounts, for employee Network; Company Property, for BYOD Network; Guest Accounts, for Guest Network ... Data Quota: Max data traffic allowed per guest (in MB) ... Time Quota per day (in hours) ... Exhaustion Handling: Block for remaining Duration ... Reduced up/down bandwidth"
  summary: |
    界面操作样例(Network Access → Accounts 各页):1) Employee Accounts:登录/口令(必填)、Enforcement Policy 及 Session timeout、Accounting Interim Interval、最大上/下行带宽;账户设置页可定义口令与用户名强度策略(最小长度/复杂度);2) Company Property:按 MAC 登记公司设备,绑定 Employee 账户/ARP/Policy List,可下发 Device Specific PSK(含随机口令生成与有效期);3) Guest Accounts:登录/口令/有效期/Service Level(必填),支持批量创建(前缀+访问码长度)、到期自动删除策略(永不/到期/若干天)、票据(Ticket)页脚 Logo 定制与打印;4) Service Level 最多 5 个,组合 ARP + Unified Policy List + Registration Profile + 有效期 + 删除策略;5) Registration Profile 配额示例(书中给出的具体数值):Data Quota 100MB、Time Quota 每天 4 小时,Exhaustion Handling 选"降速"UP=100kB/s / DOWN=1000kB/s——示例中 Day1 用 90MB/3H 未触发,Day2 累计 115MB 触发限速;6) Guest Operator:建运营账号(登录/口令/邮箱/电话),其 Portal 可建访客账户/访问码、批量导入 XLSX/CSV、审批或拒绝自助注册请求。
    验证方法:访客超配额后带宽被压到设定值,票据可打印,Operator Portal 只见访客管理功能。
  tags: [config-example, upam, accounts, quota, guest-operator, byod]
