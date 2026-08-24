# frameworks 候选 — DT00XTE317 OmniVista Cirrus/Terra Deployment and Configuration

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
