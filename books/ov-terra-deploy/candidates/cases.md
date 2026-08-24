# cases 候选 — DT00XTE317 OmniVista Cirrus/Terra Deployment and Configuration

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
