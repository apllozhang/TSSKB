# Verified 候选（V1 原文真实性核对 + V2/V3 抽查）

## cases

## C1. Cirrus 账号创建（区域 URL 选择）
- 页码：<<<PAGE 33>>><<<PAGE 34>>><<<PAGE 35>>>
- 原文摘录："https://eu.manage.ovcirrus.com/ … https://us.manage.ovcirrus.com/"，选择 Americas / Asia Pacific / EMEA，填 First/Last Name、E-mail、Country 创建 Customer 或 Partner 账号。
## C2. Partner 账号密码与激活
- 页码：<<<PAGE 38>>><<<PAGE 40>>>
- 原文摘录："Define the password with the appropriate security requirements • Password can be generated automatically with strong security"；创建后经激活邮件激活。
## C3. 创建组织（Organization）
- 页码：<<<PAGE 51>>><<<PAGE 52>>>
- 原文摘录："Click here to create your organization"；填 Organization Name、Security Policy（推荐强密码）、Country and timezone。
## C4. Trial 申请表单填写
- 页码：<<<PAGE 54>>>
- 原文摘录："Contact (mandatory): Name and email of the Sales ALE that supports this trial … If you don't know your ALE Contact name and email, use the Generic name 'My-ALE-Contact' and email MyALEContact@al-enterprise.com … Partner Name and CRD ID (copy information from eBuy) … Pre-filled duration and number of Trial equipment. Do not change, unless there is a special reason."
## C5. eBuy 下单 License
- 页码：<<<PAGE 25>>><<<PAGE 97>>>
- 原文摘录："URL: https://ebuy.businesspartner.al-enterprise.com/ Or, from MyPortal: Other Quick Links > eBuy … Create a new shopping cart and select: 'Other Services & Items Section' … Enter the license(s) reference and the required quantity … Fill the Order Entry (PO, requested date,…) and validate."
## C6. Subscription Manager 创建订阅
- 页码：<<<PAGE 26>>><<<PAGE 27>>><<<PAGE 28>>>
- 原文摘录：MyPortal: Installed Base > eLicensing Management > OVC Subscription Manager；选 offer → "Your purchased license" → Action "Create a subscription" → 选数量、填客户信息、同意条款 → 记录 Subscription reference；状态 "Created / Pending activation from OVC UI" 后展开记录 Subscription 和 Order ID。
## C7. Cirrus 导入订阅（Trial 转正）
- 页码：<<<PAGE 62>>><<<PAGE 63>>><<<PAGE 64>>><<<PAGE 65>>><<<PAGE 66>>><<<PAGE 67>>>
- 原文摘录：License Management > import licenses > CAPEX Subscription > 输入 Subscription ID + Activation Code > 同意条款 > Import Subscription > 步骤2选自动/手动设备分配 > 步骤3 review + upgrade > Proceed 确认 paid mode > 验证 License mode/Duration/Type/型号数量。
## C8. Terra 部署 VM（OVA 部署与控制台初始化）
- 页码：<<<PAGE 76>>><<<PAGE 77>>><<<PAGE 78>>><<<PAGE 79>>><<<PAGE 80>>>
- 原文摘录："Download the OmniVista Terra virtual appliance (OVA) and build (.7z) files … Enter the Name • Select a NIC card … Power on"；控制台：键盘布局 → hostname（e.g. ovtx-100）→ IP/掩码/网关/主备 DNS（须解析 myovterra.myovcloud.com）→ ovtx 密码 → 应用配置重启 → `ip addr` 验证 → 第2/3节点换 hostname/IP 重复。
## C9. WebAdmin 首次设置（Admin 账号/集群/IP/SMTP）
- 页码：<<<PAGE 82>>><<<PAGE 83>>><<<PAGE 84>>><<<PAGE 85>>><<<PAGE 86>>>
- 原文摘录："Connect to any of the VM node's IP using port 3000 … URL: <Node_IP_address>:3000"；创建 admin 账号；General Info（Email/Company/Country/Timezone/预期 AP 与交换机数量）+ 输入第2/3节点 IP 并确认可达；定义 4 个 IP（Main/VPN/UPAM Captive Portal/UPAM Radius）；SMTP（示例 smtp.gmail.com:465，TLS/StartTLS，SMTP 认证）。
## C10. Terra Build 部署与状态检查
- 页码：<<<PAGE 87>>><<<PAGE 88>>><<<PAGE 89>>>
- 原文摘录："Select the build release file (.7z), upload it and then click on Done … Confirm the deployment"；完成后刷新 admin center 查看 Dashboard 的 Nodes 与 Pods 状态；Install 菜单查看 "Success / Failure / In Progress"，失败点 "Download the logs"。
## C11. Terra DNS 配置
- 页码：<<<PAGE 90>>><<<PAGE 91>>>
- 原文摘录：在 DNS 服务器（示例 Windows DNS）配置 activation/as.myovterra.com、vpn.myovterra.com、images.myovterra.com、myovterra.myovcloud.com；之后以 myovterra.myovcloud.com 初始登录。
## C12. Terra License 下载与导入
- 页码：<<<PAGE 101>>><<<PAGE 113>>><<<PAGE 114>>><<<PAGE 115>>><<<PAGE 116>>><<<PAGE 117>>>
- 原文摘录：Admin Center 右上角取 OmniVista ID → Subscription Manager 中 "Download Licenses / Activate subscription"；导入时输入 Subscription ID + Activation Code + License file (.json) > 同意条款 > Import > 选设备分配 > upgrade > Proceed；验证 License mode/Duration/Type/数量。
## C13. 创建站点与楼层
- 页码：<<<PAGE 124>>><<<PAGE 125>>><<<PAGE 126>>><<<PAGE 127>>><<<PAGE 128>>>
- 原文摘录：创建 Site；Configure buildings and floors；楼层平面图校准："Scale up/down the plan / Rotate the plan / Move the plan / Move and calibrate the plan"。
## C14. 邀请组织级用户（单个/批量）
- 页码：<<<PAGE 131>>><<<PAGE 132>>><<<PAGE 133>>><<<PAGE 134>>><<<PAGE 135>>>
- 原文摘录："Organization user rights to be set: Globally / Per organization"（Admin/Viewer/Limited）；支持邀请用户列表（批量）。
## C15. Stellar AP 单台/批量宣告
- 页码：<<<PAGE 142>>><<<PAGE 143>>><<<PAGE 144>>>
- 原文摘录："Import and declare multiple Stellar Access Points in a single file. ▪XLSX template ▪CSV template"。
## C16. AP 查看激活状态与日志（含 AP CLI）
- 页码：<<<PAGE 146>>><<<PAGE 148>>><<<PAGE 150>>>
- 原文摘录：Device Catalog 看 Activation Status（正常链最长 5 分钟）；Activation Log 排障；AP CLI：`> ocloud_show`。
## C17. 创建 AP Group 与 Provisioning Configuration
- 页码：<<<PAGE 153>>><<<PAGE 155>>><<<PAGE 156>>>
- 原文摘录：创建 AP Group；创建 Provisioning Configuration（必填 Name/Site/RF Profile/Timezone，另含 SSH Login、SNMP、IoT Radio 等配置分节）。
## C18. 交换机 cloud-agent CLI 操作集
- 页码：<<<PAGE 171>>><<<PAGE 172>>>
- 原文摘录：`cloud-agent admin-state enable/disable`（默认 enable）、`cloud-agent admin-state disable force`（重建 VPN）、`cloud-agent discovery-interval`（默认 30 分钟）、`show cloud-agent status`、`show cloud-agent vpn status`；示例输出 Activation Server: activation.ovng.myovcloud.com:443、VPN Server: vpnb.ovng.myovcloud.com:443。
## C19. 交换机重激活操作
- 页码：<<<PAGE 170>>>
- 原文摘录："Restart the cloud agent process / Manual restart of the equipment or"。
## C20. CLI 模板化配置（Initial / Incremental）
- 页码：<<<PAGE 174>>><<<PAGE 175>>><<<PAGE 176>>><<<PAGE 177>>><<<PAGE 178>>><<<PAGE 179>>><<<PAGE 180>>>
- 原文摘录：Initial 模板在设备变 managed 前应用（onboarding 时 "Initial Configuration"）；Value Mappings 将模板变量映射到值；Incremental 模板对已分配交换机应用（Save and Assign 或 Actions > Assign，Step1 选站点/单机，Step2 选 Value mapping）。
## C21. VLAN Manager 创建 VLAN（L2 配置）
- 页码：<<<PAGE 182>>><<<PAGE 183>>><<<PAGE 184>>>
- 原文摘录："VLAN IDs … Default VLAN ID … Default Ports Template: VLAN is untagged on the default port • Q Tagged Ports Template … Switch selection"；可顺带配置 Spanning Tree（Summary/Bridge/Port）与 IP Router。
## C22. 创建 IP Interface（L3 配置）
- 页码：<<<PAGE 187>>><<<PAGE 188>>>
- 原文摘录："IP interface name • IP Address / Mask • Device type (Unbound, EMP, VLAN, Tunnel,…) • VRF IP • Enable/Disable: Admin State, IP Forward, Local Proxy ARP, Primary Interface • Switch selection"。
## C23. 802.1X SSID 配置示例
- 页码：<<<PAGE 225>>><<<PAGE 226>>><<<PAGE 227>>><<<PAGE 228>>>
- 原文摘录：Usage 选 "Enterprise Network for Employee" → Encryption → Authentication Strategy 用 UPAMRadiusServer + 内部库建 Employee → Configure Access Role Attributes（VLAN ID: Employee(20)，可加 ACL/QoS 如 Full-Access、10Mbit/s）→ Network Assignment 选 Site + AP Group(s) → Schedule/VLAN Mapping 加 VLAN 完成。
## C24. Guest SSID + UPAM Guest 策略配置
- 页码：<<<PAGE 249>>>
- 原文摘录："Create a Guest SSID with the usage 'Guest Network' • Activate the Captive portal option • Select the RADIUS server in the Authentication Strategy • Create a Guest account if the UPAM internal RADIUS server is used • In the Guest Access Strategy, define the login method and Post Portal enforcement … Assign a VLAN to the Guest SSID."
## C25. Captive Portal 定制
- 页码：<<<PAGE 258>>><<<PAGE 259>>>
- 原文摘录："This Template can be customized to reflect your own company logos, images or colors"；可定制 Background Image、Login Background Color、Image Logo、Login Button；完成后点 apply the changes to the Devices。
## C26. Guest Operator 门户操作
- 页码：<<<PAGE 287>>><<<PAGE 288>>>
- 原文摘录："Manage Guest Operators accounts, used to create Guest accounts and approve Guest self-registration requests … Guest Operator Login URL"；门户内 Manage Guests / Create Guest Account/Access Code / Import from XLXS or CSV / 审批自注册。
## C27. 软件升级计划（Scheduled Upgrade）
- 页码：<<<PAGE 356>>><<<PAGE 357>>>
- 原文摘录："Set the occurrence, starting and end date • Select a Site, AP Group(s) or Access Point • Software version: for all AP Groups or per AP Group • Review and Create Upgrade Schedule"；管理操作 Execute/Activate/Deactivate/Edit/Delete。
## C28. 备份管理（即时/计划）
- 页码：<<<PAGE 355>>>
- 原文摘录："Create an Instant Backup … Security files optional … Scheduled Backups • Scope selection: switch, site, floor"；文件管理 View/Download/Delete。
## C29. 设备排障与支持信息收集
- 页码：<<<PAGE 348>>><<<PAGE 358>>><<<PAGE 359>>>
- 原文摘录：Ping Device（及 From device）、Reboot Device、Reset Device（仅 AP）、Collect support info、Troubleshoot device、View activation log；AP 下载 tar.gz 快照（配置+日志），交换机选 Swlog/Cfg/Tech-support 文件下载 tar.gz。
## C30. Mesh/Bridge 配置操作路径
- 页码：<<<PAGE 442>>><<<PAGE 443>>><<<PAGE 444>>>
- 原文摘录："In the Device Catalog section, select the AP … Actions > Edit Device > Mesh/Bridge Configuration"；Mesh 监控显示拓扑，Root 角色与 Repeater 的 Parent Address（Root AP 的 MAC）。

## counter-examples

## CE1. eBuy 购买后订阅最长延迟 24 小时
- 页码：<<<PAGE 26>>><<<PAGE 98>>>
- 原文摘录："Note: The licenses purchased in eBuy can take up to 24h before coming up in Subscription Manager."
- 陷阱：下单后立刻在 Subscription Manager 找不到 License 并非故障。
## CE2. 一个邮箱只能绑定一个 MSP 门户
- 页码：<<<PAGE 49>>>
- 原文摘录："In OVC 10.4.3, a unique account (linked to a mail address) can only be assigned to one MSP portal. If a user want access to multiple MSP portals, he must use different mail addresses."
- 陷阱：需多 MSP 访问时用子地址（MyMail+sub@MyCompany.com）；激活链接仍发原始邮箱。
## CE3. 组织脱离 MSP 后 MSP 用户立即失去访问
- 页码：<<<PAGE 59>>>
- 原文摘录："Be aware that all users within the MSP will no longer have access to that organization once removed from the MSP."
## CE4. 设备序列号不能同时存在于 OVC4 与 OVC（迁移）
- 页码：<<<PAGE 70>>>
- 原文摘录："The serial number of a network device cannot be declared in both OmniVista CIRRUS 4 and OmniVista Cirrus. Make sure to remove all your equipment first."
- 陷阱：旧平台未删设备直接在新平台 onboard 会冲突。
## CE5. OVC4→OVC 无自动迁移工具
- 页码：<<<PAGE 69>>>
- 原文摘录："In the current version, there are no tools for migrating from OVC4 to OVC."
- 陷阱：需手工重建 AP Group/Provisioning/SSID/Access Policy 并核对配置。
## CE6. Terra CPU 指令集陷阱（AVX/AVX2 与 EVC 基线）
- 页码：<<<PAGE 75>>>
- 原文摘录："CPU must support AVX/AVX2 Instructions – in a vCenter cluster configuration, it is required to enable EVC mode with the CPU baseline set to 'Ice Lake' … As a minimum requirement, the 'Broadwell' baseline may be used."
- 陷阱：vCenter 集群 EVC 基线低于 Broadwell 会导致部署失败。
## CE7. Terra 部署失败时的取证路径
- 页码：<<<PAGE 89>>>
- 原文摘录："In the Install menu on the left, check the status of the deployment: Success / Failure / In Progress. If the deployment fails, click on the 'Download the logs' button to get the installation logs."
## CE8. Terra License "Activate subscription" 即开始倒计时
- 页码：<<<PAGE 101>>>
- 原文摘录："Enabling the option 'Activate subscription' will start the countdown of your license."
- 陷阱：过早激活会白白消耗订阅期。
## CE9. 曾被 Cirrus 管理的 AP 接入 Terra 前必须清除证书
- 页码：<<<PAGE 141>>>
- 原文摘录："Optional - If the Stellar AP is/was managed by an OmniVista Cirrus, remove the certificates: > rm -rf /.ocloud/callhome_hash.json /.ocloud/certificateFile.cert /.ocloud/cloudCaChain.pem /.ocloud/privateKey.key /.ocloud/csr.csr /.ocloud/publicKey.key ./privateKey.key.dec"
- 陷阱：残留云证书会导致激活异常；还需 DHCP option 43 指向 activation.myovterra.com 并 `firstboot`+`reboot`。
## CE10. 交换机切 Terra 需改 cloudagent.cfg 激活 URL 并删证书
- 页码：<<<PAGE 161>>>
- 原文摘录："cd switch/cloud > rm -f client.crt cloudCAchain.pem csr.crt private.key public.key … In the directory /working, edit the file cloudagent.cfg … Modify the first line 'Activation Server URL: activation.myovterra.com'"
## CE11. 激活失败状态族与排查入口
- 页码：<<<PAGE 146>>><<<PAGE 147>>>
- 原文摘录："Failed To Get Certificate / Upgrade Failed / Configuring VPN Failed / Provisioning Failed / Device Validation Failed / Factory Reset Required"；"Provisioning Failed: Device was unable to process the provisioning configuration … or OmniVista Cirrus 10 was unable to discover the device"；"Unsupported Device Model: OmniVista Cirrus does not support the device."
## CE12. VPN profile 变更后设备需恢复出厂
- 页码：<<<PAGE 147>>>
- 原文摘录："Factory Reset required: The VPN profile was changed/updated. A Factory Reset is required on the device."
## CE13. 不支持的 AP 型号（AP1101 / AP1201L/H/HL）
- 页码：<<<PAGE 9>>><<<PAGE 18>>><<<PAGE 140>>>
- 原文摘录："All Stellar models supported, except: AP1101, AP1201L/H/HL"；AP1101 也不兼容 RAP 特性（p421）。
## CE14. DSPSK 不支持 AUTO_WPA_WPA2 加密
- 页码：<<<PAGE 232>>>
- 原文摘录："Encryption AUTO_WPA_WPA2 is NOT supported • PSK/PassPhrase: only active with 'Prefer Device Specific PSK' • Device Specific PSK: Enabled."
## CE15. Fast Roaming / OKC 的加密限制
- 页码：<<<PAGE 395>>><<<PAGE 402>>>
- 原文摘录："OKC can be enabled with WPA2/WPA3 Enterprise only • 802.11r (Fast Roaming) can be enabled with WPA2/WPA3 encryption only (Personal or Enterprise) • If Fast Roaming is not enabled, then standard Roaming is used."
## CE16. 地理相邻但互相看不见的 AP 无法共享上下文
- 页码：<<<PAGE 415>>>
- 原文摘录："In some cases, Stellar APs are geographical neighbors but can't see each other (i.e: radio waves blocked by corridor with right angles,…). Client context can't be shared. No roaming. Solution: On both AP, add statically the neighbor Stellar AP."
- 陷阱：需在 AP Registration > Access Point 视图手工加 Neighbor AP，且两端都要加。
## CE17. Roaming RSSI 阈值设错的两类后果
- 页码：<<<PAGE 416>>>
- 原文摘录："If the RSSI threshold is too low, the client remains on a low signal strength site, even with a stronger site nearby. If the RSSI threshold is too high, the client roams too much that could result to packet loss."
## CE18. WIPS Client Blocklist 的局限
- 页码：<<<PAGE 387>>>
- 原文摘录："The attacker source MAC can be anything (an AP mac, a BSSID mac, a wireless NIC card mac..) • Blocklisting the attacker source MAC is only relevant when the source MAC is an actual wireless client."
- 陷阱：默认禁用；拉黑 AP/BSSID MAC 无意义。
## CE19. 扫描参数的安全/性能权衡
- 页码：<<<PAGE 373>>><<<PAGE 376>>>
- 原文摘录："During scanning wireless clients are impacted – no 802.11 data • Scanning is required for WIPS"；"Higher scanning interval or lower scanning duration means intrusions are less likely being detected but client performance will be better"。
## CE20. RSSI 差（Bad 区间）不建议音视频应用
- 页码：<<<PAGE 379>>>
- 原文摘录："Bad — Not recommended for Video or Audio applications；OK – not bad；Desired and recommended"（RSSI 对照表分档）。
## CE21. Bridge 模式 VLAN tagging 兼容性
- 页码：<<<PAGE 437>>>
- 原文摘录："* AP1101, AP1201 & AP1201H are not compatible with VLAN tagging over a bridge."
## CE22. Heat Map 至少需要 3 个 AP
- 页码：<<<PAGE 337>>>
- 原文摘录："* Minimum of 3 Stellar APs required to generate a Heat Map."

## frameworks

## F1. 三级账号体系（Partner/MSP/Customer）
- 页码：<<<PAGE 50>>>
- 原文摘录："A Managed Services Provider (MSP) Level User • Creates and configures Organization • Invites Users in the organizations. An MSP user has the access rights • Admin • Viewer • Limited. An organization can • Be an enterprise or entity • Contain multiple sites. The newly Partner account is an MSP-level user. (Customer account is not associated to an MSP)"
- 要点：Partner 账号即 MSP 级用户，创建/配置组织、邀请用户；Customer 账号不挂接 MSP；组织 = 企业或实体，可含多站点。
## F2. Partner 账号创建与 MSP 挂接三选项
- 页码：<<<PAGE 39>>>
- 原文摘录："Account can be created without an association to any MSP / Account can join an existing MSP / Account can create its own MSP"
- 要点：Partner 账号三种 MSP 关联方式：不挂 MSP / 加入既有 MSP / 自建 MSP。
## F3. Customer 账号两种交付方式
- 页码：<<<PAGE 43>>><<<PAGE 45>>>
- 原文摘录："With this option, an invitation email is sent to the partner to access the organization" / "With this option, a new account is ready-to-use for the customer to access."
- 要点：客户账号可"邀请 Partner 邮箱"（伙伴自助注册访问）或"直接创建客户凭据"（开箱即用账号）。
## F4. 组织创建与 Trial 试用期申请流程
- 页码：<<<PAGE 51>>><<<PAGE 52>>><<<PAGE 53>>><<<PAGE 54>>><<<PAGE 55>>>
- 原文摘录："Click here to create your organization. Organization Name / Security Policy / Strong password recommended / Country and timezone"（p52）；"The organization has just been created, but it does not have licenses at the moment. Click on Request a trial period for this organization."（p53）；Trial 表单必填 ALE 销售/CSM/KAM 联系人，不知道则用 "My-ALE-Contact / MyALEContact@al-enterprise.com"（p54）；"The initiator is notified by email when the request is validated. The status of the organization is updated."（p55）
- 要点：建组织（名称/安全策略/国家时区）→ 申请 Trial → ALE 审批邮件通知 → 组织状态更新。
## F5. Trial 转正（转订阅）流程
- 页码：<<<PAGE 62>>><<<PAGE 63>>><<<PAGE 64>>><<<PAGE 65>>><<<PAGE 66>>><<<PAGE 67>>>
- 原文摘录："1. Go to License Management. 2. Click on import licenses."（p62）；"Select: CAPEX Subscription; Enter: Subscription ID / Activation Code; Agree to terms; Click 'Import Subscription'"（p63）；步骤2选择自动或手动把 License 分配到设备（p64）；步骤3 review 后点 upgrade（p65）；确认弹窗 "moved to paid mode"（p66）；验证 License mode/Duration/Subscription Type/型号与数量（p67）。
## F6. License 订购→订阅生成→导入三段流程（eBuy/Subscription Manager/OV）
- 页码：<<<PAGE 24>>><<<PAGE 25>>><<<PAGE 26>>><<<PAGE 27>>><<<PAGE 28>>>
- 原文摘录："eBuy • License ordering → Subscription manager • Create the subscription … → OmniVista CIRRUS • Import of licenses: Order ID / Activation code"（p24）；订购入口 https://ebuy.businesspartner.al-enterprise.com/，购物车选 "Other Services & Items Section"（p25）；Subscription Manager 中 "Create a subscription"，注意 "The licenses purchased in eBuy can take up to 24h before coming up in Subscription Manager"（p26）；订阅状态 "Created / Pending activation from OVC UI" 时可导入（p28）。
- 要点：eBuy 下单（最多24h延迟）→ Subscription Manager 建订阅 → 在 OV 实例导入。
## F7. Terra 3-VM 部署全流程
- 页码：<<<PAGE 76>>><<<PAGE 77>>><<<PAGE 78>>><<<PAGE 79>>><<<PAGE 80>>><<<PAGE 82>>><<<PAGE 83>>><<<PAGE 84>>><<<PAGE 87>>><<<PAGE 90>>><<<PAGE 91>>>
- 原文摘录：部署 OVA（命名/选 NIC）→ 上电 → 控制台配置键盘/hostname（如 ovtx-100）（p76-77）→ IP/掩码/网关/DNS（须能解析 myovterra.myovcloud.com）+ ovtx 用户密码（p78）→ 应用配置重启、`ip addr` 验证（p79）→ 第 2/3 节点重复（p80）→ WebAdmin `<Node_IP>:3000`（p82）→ 创建 Admin 账号（p83）→ General Info + 集群节点 IP（p84）→ 上传 build (.7z) 开始部署（p87）→ 配 DNS 四域名（p90）→ 首登 myovterra.myovcloud.com（p91）。
## F8. Terra 侧 License 激活流程（与 Cirrus 差异：需下载 license 文件）
- 页码：<<<PAGE 100>>><<<PAGE 101>>><<<PAGE 114>>>
- 原文摘录："You also need to download the license file."（p100）；"In the OmniVista Admin Center, get your OmniVista ID in the top right corner; select the action 'Download Licenses / Activate subscription'. Enabling the option 'Activate subscription' will start the countdown of your license."（p101）；Terra 导入需 Subscription ID + Activation Code + License file (.json)（p114）。
## F9. Stellar AP Onboarding 流程（Cirrus/Terra 通用 + Terra 前置）
- 页码：<<<PAGE 141>>><<<PAGE 142>>><<<PAGE 143>>><<<PAGE 144>>>
- 原文摘录：Terra 前置三步：①曾由 Cirrus 管理的 AP 需删证书 `rm -rf /.ocloud/callhome_hash.json /.ocloud/certificateFile.cert ...`；②DHCP option 43 = activation.myovterra.com 并重启 DHCP；③AP 上 `firstboot` + `reboot`（p141）；批量宣告用 XLSX/CSV 模板（p144）。
## F10. OmniSwitch Onboarding 流程
- 页码：<<<PAGE 161>>><<<PAGE 162>>><<<PAGE 163>>><<<PAGE 164>>>
- 原文摘录：Terra 前置：①删证书 `cd switch/cloud; rm -f client.crt cloudCAchain.pem csr.crt private.key public.key`；②编辑 /working/cloudagent.cfg 首行 "Activation Server URL: activation.myovterra.com"（p161）；"The same procedure … is used to onboard your OmniSwitches in both OmniVista Cirrus and Terra"；批量 XLSX/CSV（p164）。
## F11. 组织在 MSP 间迁移与脱离 MSP
- 页码：<<<PAGE 59>>><<<PAGE 60>>>
- 原文摘录："Actions > Disassociate … Be aware that all users within the MSP will no longer have access to that organization once removed from the MSP"（p59）；"Actions > Change MSP • Enter the email address of an administrator of the destination MSP."（p60）
## F12. AP Group + Provisioning Configuration 配置下发模型
- 页码：<<<PAGE 152>>><<<PAGE 153>>><<<PAGE 154>>>
- 原文摘录："Management of Stellar solution on AP Group only: SSID assignment / RF Profiles / Profiles and Templates assignment"（p152）；"All Access Points get the configuration from the Provisioning Configuration assigned to the AP Group. Mandatory: Name / Site / RF Profile / Timezone"（p154）。
## F13. 有线客户端 MAC 认证四步配置流程
- 页码：<<<PAGE 451>>><<<PAGE 452>>><<<PAGE 453>>><<<PAGE 454>>><<<PAGE 455>>><<<PAGE 456>>>
- 原文摘录：[PRE] 预配 ARP_DEFAULT/ARP_PASS → ①AAA Server Profile（UPAMRadiusServer, MAC）→ ②Access Auth Profile（MAC 方法 + AAA Profile + 默认 ARP + AP Group + 端口 Eth1）→ ③Access Policy（Auth Type=MAC, Local-Database, ARP_PASS, 无重定向）→ ④本地数据库建 MAC（Company Property）。路径：Configure > Network Access > Unified Access / UPAM-NAC / Accounts。
## F14. RAP（远程 AP）五步开通序列
- 页码：<<<PAGE 423>>><<<PAGE 425>>><<<PAGE 426>>><<<PAGE 427>>><<<PAGE 428>>><<<PAGE 429>>><<<PAGE 432>>>
- 原文摘录：[PRE] 管理员预录入（OV Cirrus：序列号/RAP 模式/VPN Server 公网 IP/OV2500 IP/VPN Client IP；VPN Server：公网/私网 IP/密钥；OV2500：AP 设置）→ 1 AP 启动按序列号注册 → 2 OV Cirrus 下发 VPN 与 OV2500 参数 → 3 建管理流量 VPN 隧道 → 4 从 OV2500 取配置（SSID/射频）→ 5 第二条 VPN（客户端流量）+ 客户端接入（p423-429）；配置步骤三块：①配 OV Cirrus ②部署 ALE VPN Server VM（eth0 公网/eth1 私网，导入 VPN 设置）③配 OV2500（p432）。
## F15. OVC4 → OV Cirrus 迁移流程
- 页码：<<<PAGE 69>>><<<PAGE 70>>>
- 原文摘录："Manually setup the initial configuration for the Access Point … to match the configuration in OmniVista CIRRUS 4. Check then the configuration between OVC4 and OVC." → "Remove all the network devices from the device catalog in OmniVista CIRRUS 4" → 在新平台添加设备并等 Call Home（AP 最长 30 分钟或重启；交换机默认 30 分钟或重启 cloud-agent）（p69）；"The serial number of a network device cannot be declared in both OmniVista CIRRUS 4 and OmniVista CIRRUS."（p70）

## glossary

| # | 术语 | 中文解释 | 页码 |
|---|------|---------|------|
| 1 | OmniVista Cirrus (OVC) | ALE 云管网络平台（SaaS 模式），统一管理 Stellar AP 与 OmniSwitch | <<<PAGE 5>>> |
| 2 | OmniVista Terra (OVTX) | OmniVista 的本地部署（On-Premises）版本，客户自托管 3-VM 集群，单租户 | <<<PAGE 13>>><<<PAGE 14>>> |
| 3 | Stellar / OmniAccess Stellar | ALE 无线品牌，Stellar AP 即 Wi-Fi 接入点产品线 | <<<PAGE 9>>> |
| 4 | OmniSwitch | ALE 有线交换机产品线，运行 AOS 系统 | <<<PAGE 9>>> |
| 5 | AWOS | Stellar AP 的操作系统软件（如 AWOS 4.0.6 GA） | <<<PAGE 9>>> |
| 6 | AOS | Alcatel-Lucent Operating System，OmniSwitch 操作系统（如 8.9R1） | <<<PAGE 9>>> |
| 7 | MSP (Managed Services Provider) | 托管服务提供商，MSP 级用户可创建/配置组织并邀请用户 | <<<PAGE 47>>><<<PAGE 50>>> |
| 8 | Organization | Cirrus/Terra 的管理租户单元，可为一家企业或实体，含多个站点 | <<<PAGE 50>>> |
| 9 | Partner Account | 伙伴账号，创建后即为 MSP 级用户 | <<<PAGE 37>>> |
| 10 | Customer Account | 客户账号，挂接组织、不关联 MSP | <<<PAGE 42>>> |
| 11 | Trial Period | 组织试用期（Terra 组织自动激活 90 天 Trial），可申请后转订阅 | <<<PAGE 53>>><<<PAGE 110>>> |
| 12 | eBuy | ALE 渠道订购平台（ebuy.businesspartner.al-enterprise.com），License 下单入口 | <<<PAGE 25>>> |
| 13 | Subscription Manager | 订阅管理器，创建/管理订阅（续订、增购、延期、转移） | <<<PAGE 24>>><<<PAGE 26>>> |
| 14 | CAPEX Subscription | 买断式订阅，导入 License 时选择的订阅类型 | <<<PAGE 63>>> |
| 15 | Activation Code | 激活码，与 Subscription ID 一起用于在 OV 实例导入 License | <<<PAGE 63>>> |
| 16 | Device Catalog | 设备目录，设备宣告/清单/激活状态/激活日志所在应用 | <<<PAGE 145>>> |
| 17 | Activation Status | 激活状态，设备从宣告到 OV Managed 的状态机（Registered→Obtaining Certificate→…→Connected to OV） | <<<PAGE 146>>><<<PAGE 147>>> |
| 18 | OV Managed | 激活终态：设备已就绪可被完全管理 | <<<PAGE 147>>> |
| 19 | Call Home | 设备定期主动联系云/平台服务器的机制（交换机默认 30 分钟一次） | <<<PAGE 69>>><<<PAGE 171>>> |
| 20 | cloud-agent | OmniSwitch 上与 OV 云/平台对接的代理进程（CLI：cloud-agent …） | <<<PAGE 171>>> |
| 21 | ocloud | Stellar AP 上的云代理组件（证书存于 /.ocloud/ 目录，CLI：ocloud_show） | <<<PAGE 141>>><<<PAGE 150>>> |
| 22 | DHCP Option 43 | 厂商自定义 DHCP 选项，用于向设备下发激活服务器 URL（如 activation.myovterra.com） | <<<PAGE 141>>> |
| 23 | AP Group | AP 分组：同组共享配置（SSID/RF Profile/模板），与物理网络无关，每组最多 20000 AP | <<<PAGE 152>>> |
| 24 | Provisioning Configuration | 供给配置，绑定到 AP Group 的 AP 配置模板（必填 Name/Site/RF Profile/Timezone） | <<<PAGE 154>>> |
| 25 | RF Profile | 射频模板：国家码、Smart Load Balance、扫描、信道/功率设置 | <<<PAGE 366>>><<<PAGE 367>>> |
| 26 | DRM (Distributed Radio Management) | 分布式射频管理：AP 间空口发现邻居 + LAN 上共享 RF 上下文，各 AP 自主射频决策 | <<<PAGE 364>>> |
| 27 | ACS (Auto Channel Selection) | 自动信道选择，管理员可在 DRM 中限定 5G/6G 候选信道列表 | <<<PAGE 368>>> |
| 28 | Smart Load Balance | 智能负载均衡（含 Band Steering 与 Dynamic Load Balance） | <<<PAGE 370>>> |
| 29 | Band Steering | 频段引导：把客户端引导到 5G/6GHz 频段 | <<<PAGE 370>>> |
| 30 | Dynamic Load Balance | 动态负载均衡：相邻 AP 按负载计时，引导新客户端接入最轻负载 AP | <<<PAGE 372>>> |
| 31 | Smart Air Share | SSID 级速率控制（2.4G 最低速率建议 12、5G/6G 建议 24）提升 802.11a/n 客户端体验 | <<<PAGE 369>>> |
| 32 | Scanning (Background) | 背景扫描：射频周期扫空口，WIPS 必需；默认间隔 20s、时长 50ms | <<<PAGE 373>>> |
| 33 | RSSI | Received Signal Strength Indicator 接收信号强度指示（OV 上为平均值，AP 上为瞬时值） | <<<PAGE 378>>> |
| 34 | WIPS / WIDS | 无线入侵防护/检测系统：识别 Interfering/Rogue/Friendly AP 并自动反制 | <<<PAGE 384>>> |
| 35 | Rogue AP Containment | 流氓 AP 反制：扫描 AP 向 Rogue AP 的客户端发 de-auth（默认启用） | <<<PAGE 384>>> |
| 36 | SSID Usage | SSID 用途预设模板（Guest/Employee/BYOD/Enterprise 等），决定向导参数 | <<<PAGE 214>>><<<PAGE 218>>> |
| 37 | UPAM (Unified Policy Authentication Manager) | 统一策略认证管理器：Guest/BYOD 接入 + 内置 RADIUS + 内置 MAC 认证服务器 | <<<PAGE 240>>> |
| 38 | Captive Portal | 强制门户：Web 认证页面，可定制 Logo/背景/按钮 | <<<PAGE 258>>><<<PAGE 259>>> |
| 39 | BYOD (Bring Your Own Device) | 员工自带设备接入，经 BYOD 门户注册认证 | <<<PAGE 241>>> |
| 40 | Guest Self-Registration | 访客自注册：访客自建账号，可由员工审批 | <<<PAGE 247>>> |
| 41 | Guest Operator | 访客操作员账号：前台/运营人员创建访客账号并审批自注册请求 | <<<PAGE 287>>> |
| 42 | Service Level | 访客服务等级：绑定 ARP+Policy List+注册 Profile+有效期+删除策略，最多 5 个 | <<<PAGE 282>>> |
| 43 | Registration Profile | 注册 Profile：按用户定义有效期、时间/数据配额及配额耗尽处理 | <<<PAGE 283>>> |
| 44 | Guest Tunneling | 访客隧道：按 ARP 从 AP 到交换机/路由器的 L2 GRE 隧道，可加备份隧道 | <<<PAGE 256>>> |
| 45 | GRE | Generic Routing Encapsulation，通用路由封装（L2 GRE 用于 L3 漫游与访客隧道） | <<<PAGE 256>>><<<PAGE 394>>> |
| 46 | Access Role Profile (ARP) | 接入角色模板：定义用户 VLAN、带宽、默认 Policy List 等 | <<<PAGE 220>>> |
| 47 | Access Auth Profile | 接入认证 Profile：有线端口认证方法（802.1X/MAC/CP）与 AAA 服务器绑定 | <<<PAGE 454>>> |
| 48 | Policy List | 策略列表：ACL/QoS 规则集合（Accept/Drop、限速、802.1p/DSCP 标记），双向执行 | <<<PAGE 264>>> |
| 49 | DSPSK (Device Specific PSK) | 设备专属预共享密钥：按 MAC 分配独立 passphrase（Force/Prefer 两档） | <<<PAGE 231>>> |
| 50 | PPSK (Private Group PSK) | 私有组 PSK：多个 passphrase 各绑一个 ARP | <<<PAGE 233>>> |
| 51 | Dynamic Private Group PSK | 动态私有组 PSK：条目同时绑定 VLAN ID 与 ARP，免去为每个 VLAN 建 ARP | <<<PAGE 234>>> |
| 52 | VLAN Pooling | VLAN 池：一个 SSID 分配最多 256 个 VLAN，避免大广播域 | <<<PAGE 224>>> |
| 53 | QoE Analytics | 体验质量分析：连接时间/漫游时间/RSSI/信道利用率/uptime 及失败原因 | <<<PAGE 292>>> |
| 54 | Heat Map | 热图：按站点/AP 展示覆盖与客户端密度（红高/黄中/绿低），最少 3 个 AP | <<<PAGE 337>>> |
| 55 | Golden Configuration | 黄金配置：交换机基准备份配置，偏离则 Non-Compliant | <<<PAGE 195>>> |
| 56 | RAP (Remote Access Point) | 远程接入点：经 VPN 隧道把企业网络延伸到远程站点/家庭办公 | <<<PAGE 420>>> |
| 57 | WiFi Bridge | Wi-Fi 桥接：替代物理布线连接两地网络，不给无线客户端提供服务 | <<<PAGE 437>>> |
| 58 | WiFi Mesh | Wi-Fi 网状网：AP 间无线回程（最多 16 AP/4 跳），同时可服务客户端 | <<<PAGE 437>>><<<PAGE 439>>> |
| 59 | Auto Mesh | 自动 Mesh：LAN 上的 root AP 广播隐藏 SSID "Stellar-MESH"，未联网 AP 自动入网 | <<<PAGE 440>>> |
| 60 | Sticky Client Avoidance | 粘滞客户端规避：用 802.11k/v + Roaming RSSI 阈值引导客户端切换 AP | <<<PAGE 404>>><<<PAGE 416>>> |
| 61 | OKC (802.11k) | Opportunistic Key Caching，密钥缓存快速漫游，仅 WPA2/WPA3 Enterprise | <<<PAGE 402>>> |
| 62 | 802.11r (FT) | Fast BSS Transition 快速漫游，仅 WPA2/WPA3 加密（Personal 或 Enterprise） | <<<PAGE 402>>> |
| 63 | WebAdmin UI | Terra 管理 UI，端口 3000（<Node_IP>:3000），用于首装与 Admin Center | <<<PAGE 82>>> |
| 64 | Build (.7z) | Terra 的软件构建包，WebAdmin 上传后触发 K8s 部署 | <<<PAGE 76>>><<<PAGE 87>>> |
| 65 | IoT Device Profiling | IoT 设备识别：基于 MAC OUI 与 DHCP 指纹（option 55/60）分类并映射 ARP | <<<PAGE 464>>> |
| 66 | UNP | Unified Network Policy，OmniSwitch 上的统一网络策略（有线客户端/port 视图） | <<<PAGE 193>>><<<PAGE 313>>> |
| 67 | EVC mode | VMware vCenter 集群的 CPU 兼容基线（需 Broadwell 及以上以支持 AVX/AVX2） | <<<PAGE 75>>> |
| 68 | Walled Garden | 围墙花园：社交登录等认证前放行的预授权域名范围 | <<<PAGE 219>>> |
| 69 | RadSec | 基于 TCP/TLS 的 RADIUS 安全传输 | <<<PAGE 8>>> |
| 70 | WIPS Attack Containment / Client Blocklist | 攻击反制的客户端黑名单（默认禁用，仅对真实无线客户端 MAC 有意义） | <<<PAGE 387>>> |

## principles

## P1. Cirrus vs Terra 产品定位差异（云 SaaS vs 本地部署）
- 页码：<<<PAGE 5>>><<<PAGE 13>>><<<PAGE 14>>>
- 原文摘录：Cirrus："Software as a Service (SaaS) model … Zero Deployment"（p5）；Terra："On-Premises customer hosted … Virtualized infrastructure – cluster of VMs • Single tenant"（p13-14）。
## P2. 容量差异：Cirrus 12000 台 vs Terra 2000 台
- 页码：<<<PAGE 6>>><<<PAGE 14>>>
- 原文摘录：Cirrus "Up to 12.000 Network devices supported • 10.000 Access Points + 2.000 OmniSwitches"（p6）；Terra "Up to 2.000 Network devices supported • Up to 1.600 Stellar APs and 400 OmniSwitches"（p14）。
## P3. Terra 功能与 Cirrus 对等（parity）+ 相同商业结构
- 页码：<<<PAGE 14>>><<<PAGE 17>>>
- 原文摘录："Features parity with OmniVista Cirrus … Same commercial structure than OVCX … Consistent User Interface & Experience"（p17）。
## P4. Terra 高层架构：3 VM 组成 Kubernetes 集群
- 页码：<<<PAGE 17>>><<<PAGE 75>>>
- 原文摘录："A virtualized environment supporting: VMware environment … Multi-servers for high availability & scalability • High availability: Active-Active L3 … Kubernetes cluster … OmniVista Terra VM/Server ×3 … VPN Server / Load balancer … Kafka / MQTT … HTTPS"（p17）。
## P5. Terra VM 硬件要求
- 页码：<<<PAGE 75>>>
- 原文摘录："Number of Virtual Machines required: 3 • Minimum EXSi version: 8 • Processors: 8 vCPU @3GHz minimum • CPU must support AVX/AVX2 … EVC mode … 'Ice Lake' … As a minimum requirement, the 'Broadwell' baseline may be used • RAM: 32 GB • Disk type: SSD (Minimum 50MB/s) • System Disk: 200 GB • Data Disk: 3 TB"
## P6. 网络前置条件：Cirrus 与 Terra 的防火墙端口差异
- 页码：<<<PAGE 9>>><<<PAGE 18>>><<<PAGE 140>>>
- 原文摘录：Cirrus 需开放 9093/30123/30124/30125（AP→云）+ 出向 443/80/123/53；Terra 只需出向 443/80/123/53；DHCP 标准 options 1,3,6,28,42,43，代理时加 129-133,138；至少 1 个 NTP 服务器。
## P7. 设备软件版本前置：Cirrus 与 Terra 不同
- 页码：<<<PAGE 9>>><<<PAGE 18>>>
- 原文摘录：Stellar AP：Cirrus 要求 "AWOS 4.0.6 GA or higher"，Terra 要求 "AWOS 4.0.7.14 or higher"；OmniSwitch：Cirrus "AOS 8.9R1 or higher"，Terra "AOS 8.9.82R01 or higher"；不支持 AP1101、AP1201L/H/HL。
## P8. License SKU 编码模型（OVCX-68-BAS-3Y）
- 页码：<<<PAGE 23>>><<<PAGE 95>>>
- 原文摘录："OVCX-68-BAS-3Y … License level: BASE(BAS)/BUSINESS(BIZ)/PREMIUM(PRM) … duration: 1Y/3Y/5Y（Terra 另有 7Y）… category: APL（低端 AP1x0x/1x1x/1x2x）/APH/63/64/65/68/69/99"。
## P9. Terra 组织自动 90 天 Trial
- 页码：<<<PAGE 110>>>
- 原文摘录："The organization is automatically activated: In trial mode, for 90 days."
## P10. Terra 激活 License 时开启倒计时
- 页码：<<<PAGE 101>>>
- 原文摘录："Enabling the option 'Activate subscription' will start the countdown of your license."
## P11. eBuy→Subscription Manager 24 小时延迟
- 页码：<<<PAGE 26>>><<<PAGE 98>>>
- 原文摘录："The licenses purchased in eBuy can take up to 24h before coming up in Subscription Manager."
## P12. 单邮箱单 MSP 门户限制与子地址法（Sub-addressing）
- 页码：<<<PAGE 49>>>
- 原文摘录："In OVC 10.4.3, a unique account (linked to a mail address) can only be assigned to one MSP portal … Sub-addressing (MyMail+[subaddress]@MyCompany.com) … Activation links, upon account creation, are sent to the original mail address."
## P13. MSP 级用户三种权限：Admin/Viewer/Limited
- 页码：<<<PAGE 50>>><<<PAGE 130>>>
- 原文摘录："An MSP user has the access rights • Admin • Viewer • Limited"；组织级用户权限可"globally"或"per organization"设置（p132）。
## P14. Device Catalog 激活状态机（正常链）
- 页码：<<<PAGE 146>>><<<PAGE 147>>><<<PAGE 166>>><<<PAGE 167>>>
- 原文摘录：中间态 Registered → Obtaining Certificate → Upgrade/Upgrading → Assigned → VPN Configuring → Connected to OV；"Expected Activation Status … Up to 5 minutes"；期望终态 "OV Managed: Device is ready for full management"；状态含 "Waiting for first contact / Certificate Previously Issued / Provisioning / Unsupported Device Model" 等（p147 详细定义）。
## P15. 激活失败状态集合
- 页码：<<<PAGE 146>>><<<PAGE 147>>>
- 原文摘录："Activation Status failures: Failed To Get Certificate / Upgrade Failed / Configuring VPN Failed / Provisioning Failed / Device Validation Failed / Factory Reset Required"；"Factory Reset required: The VPN profile was changed/updated. A Factory Reset is required on the device."
## P16. 证书与 VPN 通道的激活原理
- 页码：<<<PAGE 147>>>
- 原文摘录："Obtaining Certificate: Device has contacted the OmniVista Cirrus server, and the server is creating a digital certificate that is used in creating the secure VPN channel between your device and the OmniVista Cirrus server."
## P17. AP Group 概念与规模
- 页码：<<<PAGE 152>>>
- 原文摘录："Multiple APs in the same AP Group, sharing the same configuration • Mix of any AP type & total number of AP up to 20000 • Not dependent of physical network"。
## P18. Provisioning Configuration 必填四要素
- 页码：<<<PAGE 154>>>
- 原文摘录："Mandatory Provisioning Configuration: Name / Site / RF Profile / Timezone"；配置范围含 SSH Login、AP Web、证书、SNMP、IoT Radio、Syslog(最多4) 等。
## P19. 交换机激活 cloud-agent 机制
- 页码：<<<PAGE 171>>><<<PAGE 172>>><<<PAGE 170>>>
- 原文摘录："cloud-agent admin-state enable/disable … cloud-agent discovery-interval … default= 30mns"；`show cloud-agent status` 显示 Activation Server State: completeOK、Device State: DeviceManaged 等；重激活=重启 cloud-agent 进程或手动重启设备。
## P20. SSID Usage 预定义模板模型
- 页码：<<<PAGE 214>>><<<PAGE 218>>>
- 原文摘录："Wizard driven tool. Selection of Pre-defined Usage (Guest, Employee, BYOD,…) … Each usage leads to a predefined template"；Guest=Open/MAC+Captive Portal、Protected Network=PSK、Enterprise=802.1X 等映射表（p218）。
## P21. 认证安全等级模型
- 页码：<<<PAGE 215>>>
- 原文摘录：Open+CP（无安全）→ MAC 认证（可伪造、无加密）→ WPA2/WPA3 Personal PSK（共享密钥）→ WPA2/WPA3 Enterprise 802.1X（最强）。
## P22. DSPSK / PPSK / Dynamic Private Group PSK 原理
- 页码：<<<PAGE 231>>><<<PAGE 233>>><<<PAGE 234>>><<<PAGE 235>>>
- 原文摘录：DSPSK="In the Company property database, a specific PSK pass phrase is assigned to the MAC address"（Force/Prefer 两种）；PPSK=多个 passphrase 各绑 ARP；Dynamic PGPSK="Each entry is linked to a VLAN ID and ARP … No need to create as many ARP as VLANs"，可选 Priority ARP over VLAN-ID 或反之。
## P23. UPAM 组成：内置 RADIUS + MAC 认证服务器
- 页码：<<<PAGE 240>>><<<PAGE 242>>><<<PAGE 243>>>
- 原文摘录："UPAM consists of Guest Access • BYOD Access • A built-in RADIUS Server • A built-in MAC Authentication Server"；认证源：Internal RADIUS/外部 RADIUS/IMSI-IMEI(Celona)/Azure AD。
## P24. Guest Tunneling：L2 GRE 隧道
- 页码：<<<PAGE 256>>>
- 原文摘录："Tunnel per Access Role Profile from Access Point to a switch/router/controller. • L2 GRE tunnel over L2/L3 networks • OmniSwitch simplifies deployment with automatic tunnel creation to AP IP • GRE Backup tunnel can be added for resiliency."
## P25. 带宽控制三层模型与判定顺序
- 页码：<<<PAGE 268>>><<<PAGE 269>>>
- 原文摘录：SSID 级（per SSID per AP 共享）→ ARP 级（per user）→ Policy List ACL/QoS 规则级；p269 给出判定流程图（匹配 ACL→按规则限速，否则按 ARP，再否则按 SSID）。
## P26. Policy List 双向执行
- 页码：<<<PAGE 264>>>
- 原文摘录："Policy List • List of Policy Rules (QoS, ACLs) … Enforcement is bidirectional"；分配来源 RADIUS（账号）或 ARP（Default Policy List）。
## P27. Registration Profile 配额与耗尽处理
- 页码：<<<PAGE 283>>><<<PAGE 284>>>
- 原文摘录："Data Quota: Max data traffic allowed per guest (in MB) • Time Quota per day (in hours)… Exhaustion Handling: Block for remaining Duration (Redirection URL) / Reduced up/down bandwidth (in kB/s)"。
## P28. QoE 分析指标与失败原因分类
- 页码：<<<PAGE 296>>><<<PAGE 297>>>
- 原文摘录：连接时间/漫游时间（失败原因 Association/Authorization/DHCP/Portal）、平均 RSSI（Weak Signal/Asymmetry）、信道利用率（干扰/客户端数）、设备平均 uptime。
## P29. DRM 分布式射频管理架构
- 页码：<<<PAGE 364>>><<<PAGE 365>>>
- 原文摘录："Fully distributed control Plane • Each AP communicates with its neighbor APs … Over the air protocol: neighbor AP discovery … Over the LAN protocol: RF management … Each AP can take RF action … Limited to neighbor APs • Does not rely on AP Group or AP management vlan"；RF Profile 应用于 AP Group 或 AP 级。
## P30. Smart Load Balance：Band Steering 与 Dynamic Load Balance
- 页码：<<<PAGE 370>>><<<PAGE 371>>><<<PAGE 372>>>
- 原文摘录："Band Steering: Steer client to 2.4/5/6GHz … Recommended value: 2.4G = 5, 5G = 10（RSSI）"；"Overloaded: A channel is considered overloaded when its average medium utilization over the span of a minute exceeds 70%"（p371）；DLB：各 AP 基于自身负载设 timer，新客户端被引导至最轻负载 AP（p372）。
## P31. 背景扫描机制与参数
- 页码：<<<PAGE 373>>>
- 原文摘录："Each radio periodically scans the air – One channel at the time • During scanning wireless clients are impacted – no 802.11 data • Scanning is required for WIPS • Default interval = 20 sec – Range = 5-10800 sec • Default Duration = 50 ms – Range = 50-110 ms"；支持 Dedicated AP scanning mode 与 Voice/Video Awareness（检测 SIP/H.323 绕过扫描）。
## P32. RSSI 定义与数值对照
- 页码：<<<PAGE 378>>><<<PAGE 379>>>
- 原文摘录："How well a device can hear a signal from an access point … Average on OmniVista Cirrus 10 • Instant on the Stellar Access Point"；RSSI 10≈-86dBm（Bad）… 25≈-71dBm（Desired and recommended）；AP CLI：`wlanconfig ath002 list`，-24dBm = 72 RSSI。
## P33. WIPS 分类：Interfering/Rogue/Friendly
- 页码：<<<PAGE 384>>><<<PAGE 385>>>
- 原文摘录："Interfering AP: Any other APs discovered over the air … Rogue AP: Based on the Rogue AP Policy … Rogue AP Containment – enabled by default … sends de-auth request"；Rogue 判定策略：Signal Strength Threshold（默认 -70dBm，范围 -50~-90）、Detect Valid SSID、Rogue SSID Keyword（黑名单）、Rogue OUI。
## P34. 漫游判定条件（L2/L3 选择）
- 页码：<<<PAGE 400>>><<<PAGE 394>>>
- 原文摘录："L2 or L3 Roaming selection based on the client VLAN between 'home' and 'foreign' AP … L3 Roaming based on L2 GRE tunnel"；三条件判定表：无上下文→新客户端；上下文+ WLAN/ARP 匹配 + VLAN 匹配→L2；VLAN 不匹配→L3。
## P35. 客户端上下文共享机制（Add/Del）
- 页码：<<<PAGE 397>>><<<PAGE 399>>>
- 原文摘录："Each AP learns about its 'over-the-air' adjacent APs … No dependency on AP Groups and Management VLAN … On Client Association, AP sends a Add message to all adjacent APs … Upon Roaming, Del Message triggered on the 'old' AP upon Add Message from the 'new' AP"；上下文含 VLAN ID/ARP/Policy List/PMKSA cache 等。
## P36. Fast Roaming 条件限制
- 页码：<<<PAGE 395>>><<<PAGE 402>>>
- 原文摘录："L2 Roaming always enabled • L3 Roaming disabled by default … OKC can be enabled with WPA2/WPA3 Enterprise only • 802.11r (Fast Roaming) can be enabled with WPA2/WPA3 encryption only (Personal or Enterprise)"；OKC=802.11k 优化漫游目标列表，802.11r 用 FT 快速认证。
## P37. Sticky Client Avoidance 与 Roaming RSSI 阈值
- 页码：<<<PAGE 404>>><<<PAGE 416>>>
- 原文摘录："802.11v (BSS Transition Management) … 802.11k … Roaming RSSI … Recommended value for 2.4GHz: RSSI = 10 … 5GHz: RSSI = 15"；阈值过低→客户端滞留弱信号，过高→频繁漫游丢包。
## P38. Mesh 拓扑限制
- 页码：<<<PAGE 439>>>
- 原文摘录："UP TO 8 SLAVE APS • UP TO 4 HOPS • UP TO 5 APS IN A SINGLE HOP … UP TO 16 APS IN THE MESH NETWORK • ALL APS CAN BROADCAST UP TO 5 SSIDS FOR CLIENTS"；最佳实践 BAND 5GHz、CHANNEL > 100。
## P39. Auto Mesh 机制
- 页码：<<<PAGE 440>>>
- 原文摘录：连 LAN 且配置为 Mesh root 的 AP 广播隐藏 SSID "Stellar-MESH"（5GHz）；未连 LAN 的 AP 自动以 non-root 加入 Mesh。
## P40. IoT 设备识别原理
- 页码：<<<PAGE 464>>><<<PAGE 465>>>
- 原文摘录："MAC OUI: allows devices to be recognized by identifying their MAC addresses. • DHCP FingerPrinting"；基于 DHCP option 55（参数请求列表）与 option 60（厂商标识）；流程=Collect from End Points → Profile & Inventory → Enforcement（按设备类别映射 ARP）。
## P41. VLAN Pooling 原理
- 页码：<<<PAGE 224>>>
- 原文摘录："VLAN Pooling: Pool of VLAN assigned to the SSID (up to 256) • Avoid large broadcast domain with a single VLAN."
## P42. Golden Configuration 合规检查
- 页码：<<<PAGE 195>>><<<PAGE 196>>><<<PAGE 351>>>
- 原文摘录："A Golden Configuration is a backup that can be used to restore the configuration of a switch if it changes unexpectedly"（p195）；"Status is Compliant if there are no deviations"（p196）；支持周期审计与即时审计（p351）。
## P43. Terra DNS 四域名映射
- 页码：<<<PAGE 90>>>
- 原文摘录："activation.myovterra.com / as.myovterra.com – activation server URL (Main IP) • vpn.myovterra.com – VPN (VPN IP) • images.myovterra.com – Image Server URL (Main IP) • myovterra.myovcloud.com – main URL (Main IP)"。

## glossary

| # | 术语 | 中文解释 | 页码 |
|---|------|---------|------|
| 1 | OmniVista Cirrus (OVC) | ALE 云管网络平台（SaaS 模式），统一管理 Stellar AP 与 OmniSwitch | <<<PAGE 5>>> |
| 2 | OmniVista Terra (OVTX) | OmniVista 的本地部署（On-Premises）版本，客户自托管 3-VM 集群，单租户 | <<<PAGE 13>>><<<PAGE 14>>> |
| 3 | Stellar / OmniAccess Stellar | ALE 无线品牌，Stellar AP 即 Wi-Fi 接入点产品线 | <<<PAGE 9>>> |
| 4 | OmniSwitch | ALE 有线交换机产品线，运行 AOS 系统 | <<<PAGE 9>>> |
| 5 | AWOS | Stellar AP 的操作系统软件（如 AWOS 4.0.6 GA） | <<<PAGE 9>>> |
| 6 | AOS | Alcatel-Lucent Operating System，OmniSwitch 操作系统（如 8.9R1） | <<<PAGE 9>>> |
| 7 | MSP (Managed Services Provider) | 托管服务提供商，MSP 级用户可创建/配置组织并邀请用户 | <<<PAGE 47>>><<<PAGE 50>>> |
| 8 | Organization | Cirrus/Terra 的管理租户单元，可为一家企业或实体，含多个站点 | <<<PAGE 50>>> |
| 9 | Partner Account | 伙伴账号，创建后即为 MSP 级用户 | <<<PAGE 37>>> |
| 10 | Customer Account | 客户账号，挂接组织、不关联 MSP | <<<PAGE 42>>> |
| 11 | Trial Period | 组织试用期（Terra 组织自动激活 90 天 Trial），可申请后转订阅 | <<<PAGE 53>>><<<PAGE 110>>> |
| 12 | eBuy | ALE 渠道订购平台（ebuy.businesspartner.al-enterprise.com），License 下单入口 | <<<PAGE 25>>> |
| 13 | Subscription Manager | 订阅管理器，创建/管理订阅（续订、增购、延期、转移） | <<<PAGE 24>>><<<PAGE 26>>> |
| 14 | CAPEX Subscription | 买断式订阅，导入 License 时选择的订阅类型 | <<<PAGE 63>>> |
| 15 | Activation Code | 激活码，与 Subscription ID 一起用于在 OV 实例导入 License | <<<PAGE 63>>> |
| 16 | Device Catalog | 设备目录，设备宣告/清单/激活状态/激活日志所在应用 | <<<PAGE 145>>> |
| 17 | Activation Status | 激活状态，设备从宣告到 OV Managed 的状态机（Registered→Obtaining Certificate→…→Connected to OV） | <<<PAGE 146>>><<<PAGE 147>>> |
| 18 | OV Managed | 激活终态：设备已就绪可被完全管理 | <<<PAGE 147>>> |
| 19 | Call Home | 设备定期主动联系云/平台服务器的机制（交换机默认 30 分钟一次） | <<<PAGE 69>>><<<PAGE 171>>> |
| 20 | cloud-agent | OmniSwitch 上与 OV 云/平台对接的代理进程（CLI：cloud-agent …） | <<<PAGE 171>>> |
| 21 | ocloud | Stellar AP 上的云代理组件（证书存于 /.ocloud/ 目录，CLI：ocloud_show） | <<<PAGE 141>>><<<PAGE 150>>> |
| 22 | DHCP Option 43 | 厂商自定义 DHCP 选项，用于向设备下发激活服务器 URL（如 activation.myovterra.com） | <<<PAGE 141>>> |
| 23 | AP Group | AP 分组：同组共享配置（SSID/RF Profile/模板），与物理网络无关，每组最多 20000 AP | <<<PAGE 152>>> |
| 24 | Provisioning Configuration | 供给配置，绑定到 AP Group 的 AP 配置模板（必填 Name/Site/RF Profile/Timezone） | <<<PAGE 154>>> |
| 25 | RF Profile | 射频模板：国家码、Smart Load Balance、扫描、信道/功率设置 | <<<PAGE 366>>><<<PAGE 367>>> |
| 26 | DRM (Distributed Radio Management) | 分布式射频管理：AP 间空口发现邻居 + LAN 上共享 RF 上下文，各 AP 自主射频决策 | <<<PAGE 364>>> |
| 27 | ACS (Auto Channel Selection) | 自动信道选择，管理员可在 DRM 中限定 5G/6G 候选信道列表 | <<<PAGE 368>>> |
| 28 | Smart Load Balance | 智能负载均衡（含 Band Steering 与 Dynamic Load Balance） | <<<PAGE 370>>> |
| 29 | Band Steering | 频段引导：把客户端引导到 5G/6GHz 频段 | <<<PAGE 370>>> |
| 30 | Dynamic Load Balance | 动态负载均衡：相邻 AP 按负载计时，引导新客户端接入最轻负载 AP | <<<PAGE 372>>> |
| 31 | Smart Air Share | SSID 级速率控制（2.4G 最低速率建议 12、5G/6G 建议 24）提升 802.11a/n 客户端体验 | <<<PAGE 369>>> |
| 32 | Scanning (Background) | 背景扫描：射频周期扫空口，WIPS 必需；默认间隔 20s、时长 50ms | <<<PAGE 373>>> |
| 33 | RSSI | Received Signal Strength Indicator 接收信号强度指示（OV 上为平均值，AP 上为瞬时值） | <<<PAGE 378>>> |
| 35 | Rogue AP Containment | 流氓 AP 反制：扫描 AP 向 Rogue AP 的客户端发 de-auth（默认启用） | <<<PAGE 384>>> |
| 36 | SSID Usage | SSID 用途预设模板（Guest/Employee/BYOD/Enterprise 等），决定向导参数 | <<<PAGE 214>>><<<PAGE 218>>> |
| 37 | UPAM (Unified Policy Authentication Manager) | 统一策略认证管理器：Guest/BYOD 接入 + 内置 RADIUS + 内置 MAC 认证服务器 | <<<PAGE 240>>> |
| 38 | Captive Portal | 强制门户：Web 认证页面，可定制 Logo/背景/按钮 | <<<PAGE 258>>><<<PAGE 259>>> |
| 39 | BYOD (Bring Your Own Device) | 员工自带设备接入，经 BYOD 门户注册认证 | <<<PAGE 241>>> |
| 40 | Guest Self-Registration | 访客自注册：访客自建账号，可由员工审批 | <<<PAGE 247>>> |
| 41 | Guest Operator | 访客操作员账号：前台/运营人员创建访客账号并审批自注册请求 | <<<PAGE 287>>> |
| 42 | Service Level | 访客服务等级：绑定 ARP+Policy List+注册 Profile+有效期+删除策略，最多 5 个 | <<<PAGE 282>>> |
| 43 | Registration Profile | 注册 Profile：按用户定义有效期、时间/数据配额及配额耗尽处理 | <<<PAGE 283>>> |
| 44 | Guest Tunneling | 访客隧道：按 ARP 从 AP 到交换机/路由器的 L2 GRE 隧道，可加备份隧道 | <<<PAGE 256>>> |
| 46 | Access Role Profile (ARP) | 接入角色模板：定义用户 VLAN、带宽、默认 Policy List 等 | <<<PAGE 220>>> |
| 47 | Access Auth Profile | 接入认证 Profile：有线端口认证方法（802.1X/MAC/CP）与 AAA 服务器绑定 | <<<PAGE 454>>> |
| 48 | Policy List | 策略列表：ACL/QoS 规则集合（Accept/Drop、限速、802.1p/DSCP 标记），双向执行 | <<<PAGE 264>>> |
| 49 | DSPSK (Device Specific PSK) | 设备专属预共享密钥：按 MAC 分配独立 passphrase（Force/Prefer 两档） | <<<PAGE 231>>> |
| 50 | PPSK (Private Group PSK) | 私有组 PSK：多个 passphrase 各绑一个 ARP | <<<PAGE 233>>> |
| 51 | Dynamic Private Group PSK | 动态私有组 PSK：条目同时绑定 VLAN ID 与 ARP，免去为每个 VLAN 建 ARP | <<<PAGE 234>>> |
| 52 | VLAN Pooling | VLAN 池：一个 SSID 分配最多 256 个 VLAN，避免大广播域 | <<<PAGE 224>>> |
| 54 | Heat Map | 热图：按站点/AP 展示覆盖与客户端密度（红高/黄中/绿低），最少 3 个 AP | <<<PAGE 337>>> |
| 55 | Golden Configuration | 黄金配置：交换机基准备份配置，偏离则 Non-Compliant | <<<PAGE 195>>> |
| 56 | RAP (Remote Access Point) | 远程接入点：经 VPN 隧道把企业网络延伸到远程站点/家庭办公 | <<<PAGE 420>>> |
| 57 | WiFi Bridge | Wi-Fi 桥接：替代物理布线连接两地网络，不给无线客户端提供服务 | <<<PAGE 437>>> |
| 58 | WiFi Mesh | Wi-Fi 网状网：AP 间无线回程（最多 16 AP/4 跳），同时可服务客户端 | <<<PAGE 437>>><<<PAGE 439>>> |
| 59 | Auto Mesh | 自动 Mesh：LAN 上的 root AP 广播隐藏 SSID "Stellar-MESH"，未联网 AP 自动入网 | <<<PAGE 440>>> |
| 60 | Sticky Client Avoidance | 粘滞客户端规避：用 802.11k/v + Roaming RSSI 阈值引导客户端切换 AP | <<<PAGE 404>>><<<PAGE 416>>> |
| 61 | OKC (802.11k) | Opportunistic Key Caching，密钥缓存快速漫游，仅 WPA2/WPA3 Enterprise | <<<PAGE 402>>> |
| 62 | 802.11r (FT) | Fast BSS Transition 快速漫游，仅 WPA2/WPA3 加密（Personal 或 Enterprise） | <<<PAGE 402>>> |
| 63 | WebAdmin UI | Terra 管理 UI，端口 3000（<Node_IP>:3000），用于首装与 Admin Center | <<<PAGE 82>>> |
| 64 | Build (.7z) | Terra 的软件构建包，WebAdmin 上传后触发 K8s 部署 | <<<PAGE 76>>><<<PAGE 87>>> |
| 65 | IoT Device Profiling | IoT 设备识别：基于 MAC OUI 与 DHCP 指纹（option 55/60）分类并映射 ARP | <<<PAGE 464>>> |
| 66 | UNP | Unified Network Policy，OmniSwitch 上的统一网络策略（有线客户端/port 视图） | <<<PAGE 193>>><<<PAGE 313>>> |
| 67 | EVC mode | VMware vCenter 集群的 CPU 兼容基线（需 Broadwell 及以上以支持 AVX/AVX2） | <<<PAGE 75>>> |
| 68 | Walled Garden | 围墙花园：社交登录等认证前放行的预授权域名范围 | <<<PAGE 219>>> |
| 70 | WIPS Attack Containment / Client Blocklist | 攻击反制的客户端黑名单（默认禁用，仅对真实无线客户端 MAC 有意义） | <<<PAGE 387>>> |
