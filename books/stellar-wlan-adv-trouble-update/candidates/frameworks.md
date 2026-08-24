# 框架/配置与更新工作流 · OmniAccess Stellar WLAN Advanced Troubleshooting and Update (DT00XTE378EN)

> 来源：source/fulltext.md（页码即教材 PDF 页码）
> 范围：仅 p134 以后的 Features Update 增量内容（p1-133 排障篇以姊妹书 T478 为准）

- id: f01
  title: SSID 向导三步创建流程（命名/选 Usage → 定制 → AP 组分配与调度）
  type: framework
  source_chapter: "p242-250"
  source_quote: |
    "SSID: Wizard driven tool. Pre-defined Usage (Guest, Employee, BYOD,...). All the configuration is performed from the wizard. Recommended mode. WLAN service (expert): Manual configuration. Profiles, policies, users configured independently and assigned then to the WLAN service. Limited usage for specific SSIDs."
  summary: |
    OmniVista 2500 建新 SSID 有两条路：推荐用 SSID 向导（Wizard），另一条是 WLAN Service (expert) 手工模式。向导分三步：第一步起 "SSID Service" 服务名与空口 SSID 名（多个服务可共用同一 SSID 名），并选 Usage 模板（Guest/Employee/BYOD 等，模板决定默认安全级别与是否启用 Captive Portal/BYOD 注册）；第二步定制（允许频段 2.4/5/6GHz、加密与 PSK、默认 VLAN 或 VLAN Pool、Access Role Profile 的 QoS/带宽/VLAN 映射、认证策略选本地库/外部 RADIUS/LDAP-AD、Guest/BYOD 访问策略）；第三步把 SSID 绑到一个或多个 AP Group 并可调度广播时段（默认 Always Available）。Expert 模式只留给模板覆盖不到的特殊 SSID：Profile、策略、账号各自独立创建再挂到 WLAN Service 上。

  tags: [ssid, wizard, omnivista-2500, workflow]

- id: f02
  title: Enterprise 模式设备上线工作流（VLAN/三层就绪 → SNMPv3 → 设备发现 → AP Group 纳管）
  type: framework
  source_chapter: "p213-232"
  source_quote: |
    "The Stellar Access Points that we are going to use during this training need to: Receive an IP Address from the DHCP Server > IP DHCP Relay; Forward the Wi-Fi clients traffic to a default route > Static route; Have the switch interface where they are connected enabled; Receive power from the OmniSwitches > The Power over Ethernet (PoE) feature must be enabled."
  summary: |
    把 OmniSwitch 和 Stellar AP 纳入 OmniVista 2500 管理的完整工作流：(1) Backbone VLAN（教材为 VLAN 1305）互联交换机、OmniVista 与 DHCP 服务器，每台交换机配三层 IP 接口并互 ping 验证；(2) 全网交换机配 SNMPv3（user … sha+des + snmp station … v3 enable），OmniVista 侧建相同参数的 SNMPv3 Discovery Profile，按 IP 段发现交换机；(3) 建 AP 管理 VLAN（VLAN 40），核心交换机配 DHCP relay（DHCP Offer 携带 option 138 = OmniVista IP）与静态路由，接入交换机启用端口并重启 PoE 逼 AP 上电注册；(4) AP 出现在 Managed/Unmanaged 列表，改 Trust 状态后加入 AP Group（OmniVista 只按 AP Group 管理 AP，配置对组内全部 AP 生效）。

  tags: [discovery, snmpv3, option-138, ap-group, onboarding]

- id: f03
  title: Stellar 远程实验室重初始化流程（Reset 脚本 → OV2500 快照回滚 → 首登 → 评估许可 → 客户端清理）
  type: framework
  source_chapter: "p202-212"
  source_quote: |
    "A snapshot preserves the state and data of a virtual machine at a specific point in time. We use it to easily revert the OV 2500 back to its initial configuration, to wipe all the previous training configuration."
  summary: |
    远程实验室（R-Lab）复位到初始状态的五段流程：(1) 桌面 Reset PODX 脚本重置全部交换机与 AP（交换机约 5 分钟、AP 约 1 分半到 2 分钟）；(2) OmniVista 2500 是虚机，用 vSphere 的快照回滚（Revert To "Initial State" 快照）再开机，抹掉上一期培训的全部配置；(3) 首次登录 Web 管理界面（admin/switch），强制改默认密码；(4) 到 ALE 许可门户生成 90 天评估许可（一个文件含全部设备与服务许可），以文件或密钥方式导入；(5) 无线客户端跑 "Clean Wireless Networks" 清空已保存网络。交换机侧复位不是清空配置而是下发一套预置配置（接口全 down、6870 预配 VLAN/IP），做实验时再手工启用要用的接口。

  tags: [remote-lab, snapshot, evaluation-license, reinit]

- id: f04
  title: 用户带宽控制四层判定流程（DPI 规则 → ACL 规则 → Access Role Profile → SSID 共享）
  type: framework
  source_chapter: "p284"
  source_quote: |
    "Matches a DPI application in the Policy List? Y: Application Specific BW Enforcement as per DPI Rule... Matches an ACL in the Policy List? Y: ACL Specific BW Enforcement as per Policy List... Access Role set with BW Control? Y: User BW Enforcement as per Access Role Profile... SSID set with BW Control? Y: Shared BW Enforced as per WLAN Service/SSID. N: No BW Limitation."
  summary: |
    限速到底按哪层执行，教材给了统一判定顺序，从细到粗四层依次匹配：(1) 流量命中 Policy List 里的 DPI 应用规则 → 按该应用规则限速；(2) 未命中 DPI 但命中 ACL 规则 → 按 ACL 动作限速；(3) 都未命中但用户所属 Access Role Profile 配了带宽 → 按用户级（不共享）限速；(4) Role 没配但 SSID/WLAN Service 配了 Bandwidth Contract → 全体用户按 radio 共享该带宽；四层全无 → 不限速。配置入口对应三处：SSID 级在 Advanced WLAN Service、用户级在 Advanced Access Role、规则级在 Unified Policy 的 Policy List。

  tags: [bandwidth-control, policy-list, dpi, qos, decision-flow]

- id: f05
  title: RAP 上线流程——Premium 账号四步（Cirrus 声明 → 配置下发 → VPN 隧道 → 客户端接入）
  type: framework
  source_chapter: "p377-382"
  source_quote: |
    "1 – Stellar Access Point Startup & Registration; [PRE] – Settings to be Entered by the Administrator; 2 – Configuration Settings Retrieval; 3 - VPN Tunnel (Client Traffic) Establishment; 4 – Client Connection."
  summary: |
    远程 AP（RAP，把公司网络延伸到分支/家庭办公）在 OmniVista Cirrus 4 Premium 账号下的上线四步：管理员先预录入三类信息（Cirrus 侧的 AP MAC/VPN 服务器公网 IP/VPN 客户端 IP 池/AP 配置，VPN 服务器侧的公网私网 IP 与密钥）；(1) AP 上电自动连 Cirrus，凭 MAC 地址被识别；(2) Cirrus 下发 VPN 服务器公网 IP、VPN 客户端 IP 和 AP 配置（SSID、射频参数）；(3) AP 据此与公司侧 ALE VPN Server 建立 VPN 隧道；(4) 远端用户连员工 SSID，数据走隧道回公司网。Premium 模式全部配置在 Cirrus 完成，不需要本地 OmniVista 2500。

  tags: [rap, vpn, omnivista-cirrus, commissioning]

- id: f06
  title: RAP 上线流程——Freemium 账号五步（双隧道：管理流量 + 客户数据流量）
  type: framework
  source_chapter: "p384-390"
  source_quote: |
    "1 – Stellar Access Point Startup & Registration; 2 - VPN & OmniVista 2500 Settings Retrieval; 3 - VPN Tunnel (Management Traffic) Establishment; 4 – Configuration Settings Retrieval; 5 – VPN Tunnel (Clients Traffic) & Client Connection."
  summary: |
    Freemium（免费）Cirrus 账号 + 本地 OmniVista 2500 的 RAP 上线比 Premium 多一步，因为要建两条 VPN 隧道：Cirrus 只当"引路人"，AP 从 Cirrus 拿到 RAP 模式、VPN 客户端 IP、VPN 服务器公网 IP 和 OmniVista 2500 地址（步骤 2），先建管理隧道连 OV2500（步骤 3），OV2500 再把 SSID/射频配置推给 RAP（步骤 4），最后建立第二条承载数据流量的隧道（L2GRE），客户端才能接入（步骤 5）。管理员预录入项也更多：Cirrus 侧多了 MODE=RAP 与 OV2500 服务器 IP，OV2500 侧要配 AP 设置，VPN 服务器要三块网卡（公网/管理/数据）。

  tags: [rap, freemium, l2gre, dual-tunnel, omnivista-2500]

- id: f07
  title: OmniVista Cirrus 4 设备注册流程（版本自查 → 建账号 → 入目录 → 赋许可 → 预配置 → 激活）
  type: framework
  source_chapter: "p413-421"
  source_quote: |
    "Customer network minimum configuration; OV CIRRUS Account Creation; Network device required OS upgrade; Restarting Activation Process; Adding devices to OV Catalog; Device Registration Completion; Assigning OV CIRRUS Licenses to devices; Setting Pre-Provisioning parameters."
  summary: |
    把现网设备搬上 Cirrus 4 云管的顺序：先确认设备软件版本满足最低要求（不满足先升级，见对应原则条目）；自助注册 Freemium 或购买 Premium 账号；设备出厂默认走 DHCP 或手工/Auto-config/预配置均可上线；设备进入 OV Catalog 后，Freemium 走一次性激活，Premium 还要把许可逐台分配给设备并设置预配置参数（如 AP 的 MAC/组名/射频模板）；卡在 Waiting For First Contact 状态时重启激活流程——AOS 交换机停云代理（cloud-agent admin-state disable force）或整机重启，Stellar AP 进 failsafe 模式（开机约 20 秒按 [f]）做 firstboot。完成后设备从 Device Catalog 进入 Managed devices。

  tags: [omnivista-cirrus, device-registration, cloud, licensing]

- id: f08
  title: 备份-恢复-升级三段工作流（Save Running → Resource Manager 备份/恢复 → 固件升级两条路）
  type: framework
  source_chapter: "p426-432"
  source_quote: |
    "A dedicated application is available in the OmniVista 2500 to perform the backup and restore operations of AOS: The Resource Manager... Backup By Devices... Backup By AP Group: backup Stellar AP Series Devices... Backup Type: Configuration Only."
  summary: |
    变更前的标准三段操作：(1) 先保存现场——通知区铃铛图标 Save All，把全部在网设备的管理配置存为 Running（交换机另需 Copy Working/Running to Certified）；(2) 用 Resource Manager 备份：按设备选（AOS 交换机，需 FTP 认证）或按 AP Group 选（Stellar AP 只能按组备份），类型选 Configuration Only / Full / Images Only，可设单次或周期调度；恢复仅对 AOS 有效，恢复文件落到 WORKING 和 CERTIFIED 后必须 reload from working 才真正生效；(3) 固件升级两条路——Resource Manager 的 Upgrade Image（导入→选型号→选设备或 AP 组→Install）或单台 AP 的 Web 页（AP Group 开 AP Web 后 https://<AP IP> 上传镜像）。

  tags: [backup, restore, upgrade, resource-manager, firmware]
