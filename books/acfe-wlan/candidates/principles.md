# principles.md · ACFE WLAN - Basic Deployment With OmniVista Ed04 · 原则/清单/规则/常数提取
# 提取范围：fulltext.md（p1-p585）+ figures_captions.md
# 每条 source_chapter 为原书 PDF 页码（p页码）

- id: p01
  title: 部署模式判定规则：DHCP option 138 决定 Express 还是 Enterprise/Cloud
  type: principle
  source_chapter: "p17"
  source_quote: |
    "WiFi Express is the default mode
    • AP requests and receives an IP address from the DHCP server.
    • DHCP option 138 equals the IP address of the OmniVista 2500 Server"
  summary: |
    Stellar AP 出厂默认 Express 模式。启动判据（p100 决策树）：AP 发 DHCP 请求；若 DHCP 下发 option 138（值为 OmniVista 2500 的 IP）则进 Enterprise 模式；否则尝试联系 OV Cirrus，若 AP 的 MAC/序列号已在 Cirrus 登记则进 Cloud 模式；两者都不满足才以 Express 模式启动。开局排障第一步就是查 option 138 与设备是否已登记。
  tags: [mode, dhcp, onboarding]

- id: p02
  title: Express 模式出厂默认值：mywifi-ABCD / 192.168.1.254 / 端口 8080
  type: principle
  source_chapter: "p101"
  source_quote: |
    "BY DEFAULT, THE OMNIACCESS STELLAR AP:
    - BROADCASTS A SSID "MYWIFI-ABCD" WITH ABCD = LAST BYTES OF THE AP MAC@
    - HAS THE IP@ = 192.168.1.254 (OR AN IP@ RECEIVED FROM THE DHCP SERVER)
    TO ACCESS THE WEB ADMIN INTERFACE:
    - OPEN A WEB BROWSER AND INSERT THE FOLLOWING URL HTTP://<IP@ OF THE AP>:8080"
  summary: |
    出厂 AP 广播 SSID mywifi-ABCD（ABCD=AP MAC 地址末 4 位十六进制），默认管理 IP 192.168.1.254（有 DHCP 时取分配地址）。Web 管理界面地址 http://<AP IP>:8080。AP 改为 DHCP 模式后可用域名 mywifi.al-enterprise.com:8080 访问（p127-129）。默认管理员密码 admin（p114）。
  tags: [express, default, access]

- id: p03
  title: AP Group 出厂成组规则：Group ID 100 + VLAN 1 自动同组
  type: principle
  source_chapter: "p104"
  source_quote: |
    "OmniAccess Stellar Access Points with the same group identifier (Group ID) and the same VLAN are automatically placed in the same group (AP Group)
    • Initial Settings (Factory Settings)
    • Identical Group ID (Group ID 100)
    • Identical default VLAN (VLAN 1)"
  summary: |
    Express 模式下，Group ID 相同且 VLAN 相同的 AP 自动组成一个 AP Group。出厂时所有 AP 的 Group ID 均为 100、默认 VLAN 均为 VLAN 1，因此开箱后同一二层内的 AP 会自动归入同一组，统一由 PVM 的 Web 界面管理。
  tags: [express, ap-group]

- id: p04
  title: PVM/SVM 选举规则：先比最高型号再比最高 MAC
  type: principle
  source_chapter: "p11"
  source_quote: |
    "In the case of a VLAN with several APs started at the same time an election process is perform to select the PVM
    Highest Model Type
    Highest MAC address
    AP with the second highest MAC is designated as the SVM
    All other APs become members of the group with up to 255 APs in a group."
  summary: |
    同一 VLAN 内多台 AP 同时启动时触发选举：PVM（主虚拟管理器）按"型号最高、MAC 最大"两级 criteria 选出；SVM（备）取第二高 MAC 的 AP；其余为 Member，单组上限 255 台。当选 PVM 后会生成组配置 SSID（形如 mywifi-0102）。
  tags: [express, pvm, election]

- id: p05
  title: Express 集群规模与弹性建议：255 上限、>64 需冗余、每交换机 32/每堆叠 64
  type: principle
  source_chapter: "p13"
  source_quote: |
    "• Cluster size > 64
    • Resiliency in the network design
    • Recommendations
    • Max Up to 32 APs per OmniSwitch
    • Max Up to 64 APs per stack"
  summary: |
    集群最大 255 台（p12）。集群规模超过 64 台时必须在网络设计中考虑弹性：建议每台 OmniSwitch 最多接 32 台 AP、每个堆叠最多 64 台 AP。
  tags: [express, sizing, capacity]

- id: p06
  title: 模式切换规则：改模式即丢配置
  type: principle
  source_chapter: "p18"
  source_quote: |
    "• Mode can be changed:
    • Manually in Express mode with a "Convert to Enterprise" button
    • Or requires a factory reset (push button) and reboot
    • Add option 138 in the DHCP server for the AP management scope
    No configuration migration, AP « cluster » configuration is lost"
  summary: |
    从 Express 迁到 Enterprise/Cloud：在 AP 管理 DHCP 作用域加 option 138，然后在 Express 界面点 "Convert to Enterprise" 或按Reset键恢复出厂重启。关键警告：不做配置迁移，原集群（cluster）配置全部丢失，需提前备份重建。
  tags: [mode, migration]

- id: p07
  title: 三平面标签规则：管理流量永远 untagged，无线数据流量上联口永远 tagged 且纯 L2
  type: principle
  source_chapter: "p24"
  source_quote: |
    "• Wireless traffic always tagged on the AP uplink
    • No tunnel mode to OV or Virtual Controller
    • Data Plane is only L2
    • No routing for data user traffic
    • Routing provided by LAN infrastructure"
  summary: |
    管理面（p21）：AP 管理流量在边缘交换机到 AP 之间永远 untagged（管理 VLAN=Native VLAN）。数据面（p24）：无线数据在 AP 内转成以太网上联、永远 tagged（每 SSID 一个 VLAN），无到 OV/虚拟控制器的隧道，数据面仅二层，用户数据路由由 LAN 基础设施承担。这是交换机端口规划（Native/Trunk）与排障的根基规则。
  tags: [vlan, planes, topology]

- id: p08
  title: 开局网络拓扑检查清单（PoE trunk / DHCP / option 138 / DNS / 路由）
  type: principle
  source_chapter: "p25"
  source_quote: |
    "Trunk Port with POE
    •Untagged/Native vlan = AP Mgt VLAN
    •Tagged VLANs = SSID VLANs
    DHCP Scope for
    •All AP Mgt VLANs
    Require option 138 for OV IP address
    •All SSID VLANs"
  summary: |
    标准开局清单：AP 接入交换机口为 PoE trunk——Native/untagged VLAN=AP 管理 VLAN，SSID 对应 VLAN 全部 tagged；核心/汇聚为所有管理 VLAN 和 SSID VLAN 提供 IP 接口与路由；DHCP 服务器为所有管理 VLAN（企业模式需 option 138 指向 OV）和所有 SSID VLAN 建作用域；DNS 可选但建议为所有子网配置。
  tags: [checklist, topology, dhcp, vlan]

- id: p09
  title: 管理平台规模上限：OV2500 4000 AP / Cirrus 实例 12000 设备
  type: principle
  source_chapter: "p164"
  source_quote: |
    "• Up to 12.000 Network devices supported
    • 10.000 Access Points + 2.000 OmniSwitches"
  summary: |
    OmniVista 2500（Enterprise，p15-16）：最多 4000 台 AP、单设备 10 万客户端。OV Cirrus（p164）：单实例最多 12000 台网络设备=10000 AP+2000 OmniSwitch；p27 另给出常用部署档"最多 2000 AP"或"1600 AP+400 交换机"。Cirrus 内 AP Group 上限 2000 台（p271）。
  tags: [capacity, cirrus, ov2500]

- id: p10
  title: Wi-Fi 代际性能常数表（Wi-Fi 4/5/6/6E/7）
  type: principle
  source_chapter: "p67"
  source_quote: |
    "Max data rate 1.2 Gbps / 3.5 Gbps / 9.6 Gbps / 9.6 Gbps / 46 Gbps
    Channel width 20,40 MHz ... 20,40,80,80+80,160 MHz ... Up to 320 MHz
    Security WPA 2 / WPA 2 / WPA 3 / WPA 3
    MIMO 4x4 MIMO ... 8x8 UL/DL MU-MIMO / 16x16 MU-MIMO"
  summary: |
    代际对照：Wi-Fi 4(2007, 802.11n) 最大 1.2Gbps、20/40MHz；Wi-Fi 5(2013, ac) 3.5Gbps、最宽 160MHz；Wi-Fi 6(2019, ax) 9.6Gbps、1024-QAM+OFDMA、8x8 UL/DL MU-MIMO、TWT；Wi-Fi 6E(2021) 加 6GHz；Wi-Fi 7(2024, be) 46Gbps、320MHz、4096-QAM、16x16 MU-MIMO、MLO、RTWT。安全从 WPA2（4/5 代）升级到 WPA3（6/6E/7）。
  tags: [wifi-standards, constants]

- id: p11
  title: AP 型号 PoE 供电等级与降级规则
  type: principle
  source_chapter: "p47"
  source_quote: |
    "• PoE 802.3af/at compliant
    • Full function at 802.3at PoE source
    • Disable private PSE and USB with 802.3af PoE source"
  summary: |
    PoE 要求随型号不同（p44-57）：AP1301 仅需 802.3af 即全功能；AP1311 需 802.3at 才全功能（af 下禁用 PSE 下联口和 USB）；AP1230 需 802.3at 4 对 60W（2 对供电功能受限）；AP1351 需 802.3bt 全功能；AP1320 为 802.3at（带 PoE backup）；AP1411/AP1431 为 bt Type 3；AP1521 bt，低功率模式可跑 802.3at（最高 15W）；AP1570 802.3bz。SSID/客户端容量参考：AP1301/1311 16 SSID、512 客户端；AP1320/1331/1301H 32 SSID、1024 客户端；AP1451/1511/1521 48 SSID；AP1351/1451 1536 客户端。室外机型（AP136x/157x）温度范围 -40~+65°C，室内多为 0~45°C（Wi-Fi 7 为 0~50°C）。
  tags: [poe, hardware, capacity]

- id: p12
  title: BLE 信标配置规则：按 AP Group 配置、默认关闭、默认 iBeacon
  type: principle
  source_chapter: "p278"
  source_quote: |
    "• BLE Beacon is configured per AP Group
    • Turned OFF by default
    • Configurable parameters are
    • Beaconing Mode : iBeacon per default
    • Transmission Power
    • Frequency/Emission Period
    • UUID (Universal Unique Identifier) – ALE specific UUID for all ALE products
    • Major and Minor values – used for greater accuracy than UUID alone"
  summary: |
    BLE Beaconing（适用于内置 BLE 的 AP1230/13xx/14xx/15xx）按 AP Group 统一配置，默认关闭；开启后默认模式 iBeacon，可调发射功率、发射周期、UUID（ALE 产品统一 UUID）、Major/Minor 值（比单 UUID 更精确定位）。用于资产追踪/定位场景。
  tags: [ble, iot, config]

- id: p13
  title: ISC-DHCP 识别 Stellar AP 与自定义 option 138 写法
  type: principle
  source_chapter: "p33"
  source_quote: |
    "class "STELLAR" {
    match if substring (option vendor-class-identifier, 0, 4) = "HAP.";
    }
    option ovwma code 138 = ip-address;"
  summary: |
    isc-dhcp-server 不认识 option 138，需先自定义：option ovwma code 138 = ip-address; 再用 vendor-class-identifier 前 4 字节等于 "HAP." 的 class 匹配 Stellar AP，在专属 pool 中下发 option ovwma <OV2500 IP>（示例 192.168.0.61）。OmniSwitch 作 DHCP 服务器时直接写 option 138 <IP>。
  tags: [dhcp, config, cli]

- id: p14
  title: AP 恢复出厂与默认控制台凭据（support/aos2016）
  type: principle
  source_chapter: "p119"
  source_quote: |
    "Press the Reset for 10 seconds in the back of the AP, then release it
    Enter in the default credentials:
    - Login: support
    - Password: aos2016
    ssudo firstboot -y
    ssudo reboot"
  summary: |
    AP 恢复出厂两条路：(1) 长按背面 Reset 键 10 秒（p304 另述：按 6 秒至 LED 闪红即可复位）；(2) 控制台/SSH 用 support/aos2016 登录后执行 ssudo firstboot -y && ssudo reboot。ssudo reboot 也用于强制 AP 立即 Call Home 完成云注册（p302）。
  tags: [reset, credentials, cli]

- id: p15
  title: OmniSwitch 出厂默认：仅控制台可管理、PoE 默认开启
  type: principle
  source_chapter: "p110"
  source_quote: |
    "By default, the OmniSwitch 6360 can only be configured from the console port. For security reasons, the other protocols (Telnet, SSH, Web Interface) are disabled."
  summary: |
    OmniSwitch 6360 出厂只有控制口可配（Telnet/SSH/Web 全部禁用），默认凭据 admin/switch。PoE 默认开启、无需配置（p122）。验证命令 show lanpower slot 1/1：AP1321 接入显示 Class 4、端口上限 30000mW、实耗约 7000mW（6360/2360 部分端口为 60000mW，p304）。保存配置用 write memory flash-synchro（p111）。
  tags: [switch, default, poe, credentials]

- id: p16
  title: AP 接入端口 VLAN 分配规则：管理 VLAN untagged、SSID VLAN tagged
  type: principle
  source_chapter: "p123"
  source_quote: |
    "OS6360-XTE210-> vlan 10 members port 1/1/6 untagged
    OS6360-XTE210-> vlan 20 members port 1/1/6 tagged
    OS6360-XTE210-> vlan 30 members port 1/1/6 tagged"
  summary: |
    AP 所在端口：管理 VLAN（如 VLAN 10）设为 default/untagged，员工/访客等 SSID VLAN（20、30）设为 tagged；上联/级联口（如 1/1/3）把全部 VLAN tagged。标准命令序列：vlan 10 name AP-MGMT → vlan 10 members port 1/1/6 untagged → vlan 20/30 members port 1/1/6 tagged；验证 show vlan members port 1/1/6。
  tags: [vlan, config, cli]

- id: p17
  title: 培训实验网 IP/DHCP 规划常数（VLAN 10/20/30）
  type: principle
  source_chapter: "p79"
  source_quote: |
    "VLAN / VLAN Description / IP Addresses Range
    10 AP Management 192.168.10.70 to 192.168.10.79
    20 Employees 192.168.20.70 to 192.168.20.79
    30 Guests 192.168.30.70 to 192.168.30.79"
  summary: |
    远程实验室（R-Lab）预置 DHCP 作用域：VLAN 10=AP 管理（192.168.10.70-79）、VLAN 20=Employees（192.168.20.70-79）、VLAN 30=Guests（192.168.30.70-79）。所有 Lab 验证步骤都以此判断客户端是否落对 VLAN；网关分别为 6870 上 192.168.20.7 / 192.168.30.7（p149、p153）。DHCP/NAT 服务器（192.168.100.102）与核心 OS6900 不允许改动（p72）。
  tags: [lab, dhcp, addressing]

- id: p18
  title: Express 模式员工/访客 SSID 认证模型
  type: principle
  source_chapter: "p134"
  source_quote: |
    "• 2 methods available:
    • Access the Wi-Fi network using a password
    • Authentication via 802.1X (external RADIUS)"
  summary: |
    员工 SSID 两种安全方式：密码（Personal/PSK）或 802.1X（外部 RADIUS，可按凭据或 MAC 校验，p136）。访客 SSID（p138）通常 Open + 内嵌 Captive Portal 认证（高级门户在 OmniVista Cirrus 上）。
  tags: [express, ssid, security]

- id: p19
  title: 每 SSID 自动 VLAN 分配与 AP 内置服务
  type: principle
  source_chapter: "p140"
  source_quote: |
    "• A predefined VLAN is automatically assigned to a client when it connects to an SSID
    SSID « Employees »
    • VLAN : 10
    SSID « Guests »
    • VLAN : 20"
  summary: |
    客户端按所连 SSID 自动进预定义 VLAN（SSID↔VLAN 映射）。所有 Stellar AP 内置 DHCP/DNS/NAT 服务（p141）与 QoS/ACL（p142）：典型模板——员工 VLAN 10 全访问/高带宽/普通优先级，访客 VLAN 20 仅 Internet/普通带宽/低优先级，话机 VLAN 30 语音访问/低带宽/高优先级。
  tags: [ssid, vlan, qos]

- id: p20
  title: 内置 Captive Portal 三种认证模式与账号规则
  type: principle
  source_chapter: "p151"
  source_quote: |
    "The internal captive portal is activated by default. Now the authentication type must be selected (account, access code, or terms of use)
    The username and password fields are case sensitive"
  summary: |
    AP 内嵌 Captive Portal 默认已激活，认证三选一：Account（建账号，填起止日期即有效期）、Access Code（访问码）、Terms of use（勾选条款即放行）。用户名/密码区分大小写。配套：Operator 账户默认禁用（p159，System>General>Account Management 启用后提供访客账号简化管理界面）；Walled Garden（p160）允许访客认证前访问预定义站点。
  tags: [captive-portal, guest, config]

- id: p21
  title: AP 内置 DHCP 服务器：先建 Pool 再 Bind Network
  type: principle
  source_chapter: "p155"
  source_quote: |
    "Fill the following settings in the new DHCP range:
    - Pool name: Employees
    - Subnet: 255.255.255.0
    - Gateway: 192.168.10.3
    - Range Start: 192.168.10.10
    - Range Stop: 192.168.10.50
    - DNS1: 192.168.10.3"
  summary: |
    AP 可充当 DHCP 服务器（Service>DHCP>Create）：填 Pool 名、掩码、网关、起止范围、DNS，保存后必须 Action>Bind Network 绑定到对应网络（vlan10/vlan20）才生效。示例池 .10-.50 共 40 个地址=同时在线 40 台设备，用户更多需扩大范围。
  tags: [dhcp, express, config]

- id: p22
  title: OV Cirrus 网络前置条件清单（防火墙端口/DHCP options/版本）
  type: principle
  source_chapter: "p167"
  source_quote: |
    "Open Firewall ports
    • 9093 • 30123 • 30124 • 30125
    And to allow outbound traffic from local network:
    • 443 • 80 • 123 • 53
    Enable DHCP standard options:
    1, 3, 6, 28, 42, 43
    And, when using proxy:
    129, 130, 131, 132, 133, 138"
  summary: |
    云管前置条件：Stellar AP 固件 AWOS 4.0.6 GA 或更高（AP1101、AP1201L/H/HL 不被 Cirrus 支持）；OmniSwitch 运行 AOS 8.9R1+（支持 8.9RX/8.10RX，release 5 不支持，p242）。防火墙开放入向 9093/30123/30124/30125，出向放行 443/80/123/53；DHCP 标准选项 1,3,6,28,42,43（用代理时另加 129-133、138）；至少配置 1 台 NTP 服务器。
  tags: [cirrus, prerequisites, firewall, ports]

- id: p23
  title: Cirrus License 编码规则（OVCX-68-BAS-3Y 解析）
  type: principle
  source_chapter: "p172"
  source_quote: |
    "OVCX-68-BAS-3Y
    • License level
    • BASE level: BAS
    • BUSINESS level: BIZ
    • PREMIUM level: PRM
    • License duration
    • 1 year: 1Y • 3 years: 3Y • 5 years: 5Y
    • License category
    • Low end Stellar models: APL (AP1x0x, AP1x1x, AP1x2x)
    • High end Stellar models: APH"
  summary: |
    订货号结构：OVCX-{系列}-{级别}-{年限}。级别 BAS/BIZ/PRM；期限 1Y/3Y/5Y；类别 APL=低端 Stellar（AP1x0x/1x1x/1x2x）、APH=其余 AP 型号、63/64/65/68/69/99=对应 OmniSwitch 63xx/64xx/65xx/68xx/69xx/99xx。示例 OVCX-68-BAS-3Y=OmniSwitch 68xx、BASE 级、3 年。
  tags: [license, ordering]

- id: p24
  title: License 订购与订阅流程（eBuy → Subscription Manager → Cirrus 导入）
  type: principle
  source_chapter: "p175"
  source_quote: |
    "Note: The licenses purchased in eBuy can take up to 24h before coming up in Subscription Manager."
  summary: |
    流程：eBuy（https://ebuy.businesspartner.al-enterprise.com/，MyPortal 也可进）下单品号和数量 → Subscription Manager 建 Subscription（选设备数量、客户信息，记下 Subscription ID 与 Activation Code）→ 在 Cirrus 组织 License Management>Import Licenses 选 CAPEX Subscription、填 ID+激活码导入并分配设备。注意：eBuy 采购到 Subscription Manager 可见最长延迟 24 小时。
  tags: [license, workflow, url]

- id: p25
  title: 账户-组织层级规则与一邮箱一 MSP 限制（子地址技巧）
  type: principle
  source_chapter: "p198"
  source_quote: |
    "In OVC 10.4.3, a unique account (linked to a mail address) can only be assigned to one MSP portal.
    If a user want access to multiple MSP portals, he must use different mail addresses:
    • Or using the sub-addressing method for his email
    Sub-addressing (MyMail+[subaddress]@MyCompany.com)"
  summary: |
    层级：MSP 门户 > Organization（可含多站点）> Site > Building > Floor。账号分 Customer/Partner 两类；MSP 级用户权限三种：Admin/Viewer/Limited（p199、p233）。OVC 10.4.3 起一个邮箱（=一个账号）只能属于一个 MSP 门户；要访问多个 MSP 用不同邮箱或子地址 MyMail+tag@MyCompany.com（激活邮件仍发原地址，主流邮箱服务商均支持）。组织可在 MSP 间迁移（Actions>Change MSP）或脱离（Disassociate，脱离后该 MSP 全部用户失去访问权，p208-209）。区域入口：https://eu.manage.ovcirrus.com / https://us.manage.ovcirrus.com（p182）。密码策略：14-100 字符，大小写+数字+特殊字符，不得含邮箱串（p187 配图）。
  tags: [account, msp, organization, url]

- id: p26
  title: OVC4→OVC 迁移规则：序列号不得双登记、Call Home 最长 30 分钟
  type: principle
  source_chapter: "p219"
  source_quote: |
    "The serial number of a network device cannot be declared in both OmniVista CIRRUS 4 and OmniVista CIRRUS. Make sure to remove all your equipment first"
  summary: |
    迁移步骤（p218）：先在 OVC 手工重建 AP Group/SSID/策略等对象并比对 OVC4 配置 → 在 OVC4 Device Catalog 删除全部设备（序列号不能同时存在于两套系统）→ 在 OVC 手工或 XLSX/CSV 模板重新登记设备 → 等下一次 Call Home：AP 最长 30 分钟（或直接重启 AP），OmniSwitch 默认 30 分钟（或重启 cloud-agent 进程）。
  tags: [migration, cirrus]

- id: p27
  title: 设备激活状态机与 Call Home 强制方法
  type: principle
  source_chapter: "p261"
  source_quote: |
    "Intermediate Status
    Registered / Obtaining Certificate / Upgrade-Upgrading / Assigned / VPN Configuring / Connected to OV
    Expected Activation Status: Up to 5 minutes
    Activation Status failures
    Failed To Get Certificate / Upgrade Failed / Configuring VPN Failed / Provisioning Failed / Device Validation Failed / Factory Reset Required"
  summary: |
    正常链路：Waiting for validation（OV 自动验证）→ Waiting for first contact → Obtaining Certificate → Registered → Assigned → VPN Configuring → Connected to OV → Provisioning → OV Managed，中间态最长约 5 分钟。设备按 Call Home 周期自动激活；嫌慢可强制：交换机推荐 cloud-agent admin-state restart（或 reload from working no rollback-timeout），约 2 分钟完成；AP 直接重启（p250-251、p302）。验证：交换机 show cloud-agent status 应显示 Activation Server State=completeOK、Device State=DeviceManaged；AP 用 ocloud_show 看 VPN Status=connected。排障入口：Device Catalog>Action>Diagnostic Tools>View Activation Log（p253）。失败态中 "Factory Reset Required" 表示 VPN profile 变更过，设备需恢复出厂。
  tags: [onboarding, activation, troubleshooting]

- id: p28
  title: AP Group/Provisioning Configuration 强制字段
  type: principle
  source_chapter: "p273"
  source_quote: |
    "Mandatory Provisioning Configuration:
    • Name
    • Site
    • RF Profile
    • Timezone"
  summary: |
    Cirrus 对 Stellar 的管理以 AP Group 为单位（SSID/RF Profile/模板都挂组），组内可混插任意 AP 型号、总数上限 2000、不依赖物理网络（p271）。Provisioning Configuration 四个必填：Name、Site、RF Profile、Timezone；可选项含 SSH Login、AP Web、Client Behavior Tracking、证书、SNMP、IoT Radio、Data VPN、Syslog（最多 4 台）等。AP 也可在 Device Catalog 单独改 RF Profile 覆盖组配置（p463）。
  tags: [cirrus, ap-group, provisioning]

- id: p29
  title: Onboarding 方法一：手工 VLAN 分类及其扩展代价
  type: principle
  source_chapter: "p286"
  source_quote: |
    "The AP Management VLAN must be manually configured on the port(s) where the AP devices are connected to.
    • If a new AP is connected on a port, the AP Management VLAN AND the VLAN mapped to SSIDs must be assigned to this port manually."
  summary: |
    手工法：先建 AP 管理 VLAN，再在每个 AP 口上把它设为 default/untagged。流程：AP 发 DHCP 请求 → DHCP 分配 IP → AP 连激活服务器（eu.activation.ovng.myovcloud.com）→ 序列号有效则 OVC 回送管理信息。限制：每加一台新 AP 都必须手工在其端口补管理 VLAN（untagged）+ 所有 SSID VLAN（tagged），扩展性差。
  tags: [onboarding, vlan, method]

- id: p30
  title: Onboarding 方法二：UNP 自动分类（defaultWLANProfile + LLDP）
  type: principle
  source_chapter: "p288"
  source_quote: |
    "• "defaultWLANProfile" UNP
    • Designated for classifying AP devices.
    • Automatically assigned to a built-in UNP LLDP classification rule that recognize and classify AP devices into the "defaultWLANProfile" UNP."
  summary: |
    UNP 法：交换机内置 defaultWLANProfile UNP 和 LLDP 分类规则（出厂即有）；只需建管理 VLAN、把 AP 口设为 UNP 口、把 VLAN 映射到该 UNP。AP 上电发 LLDP-MED TLV 自报身份 → 交换机自动归入 defaultWLANProfile → 回发 Port VLAN ID 与 AP 位置 TLV；另需配一个 >999 的"Dummy VLAN"（AP Mode 特性默认启用时用于此步）。限制（p291）：AP 不做 802.1X 认证——即使端口开了 802.1X 且 AP 认证失败，其 VLAN-tagged 客户端流量仍被信任转发（ rogue AP 风险点）。
  tags: [onboarding, unp, lldp]

- id: p31
  title: Stellar AP 排障 CLI 工具箱（串口参数/关键命令）
  type: principle
  source_chapter: "p305"
  source_quote: |
    "> Baud rate: 115200
    > Data bits: 8
    > Parity: None
    > Stop bits: 1
    > login: support
    > password: aos2016"
  summary: |
    串口参数 115200-8-N-1，凭据 support/aos2016。核心命令：showsysinfo（序列号/MAC/固件，云登记必用）；getmode（必须返回 OVNG 才是云管模式）；ocloud_show（VPN Status、激活服务器、下次 Call Home 倒计时）；getovinfo（激活服务器 IP）；ssudo ifconfig br-wan（管理 IP）；cat /etc/config/network（确认 DHCP 模式）。业务排障：iwconfig/iwlist channel|txpower|bitrate（射频状态）、ssudo sta_list 与 ssudo wlanconfig athX list（在线客户端及 VLAN/ARP）、ssudo wam_debug sta_list（JSON 明细）、cat /proc/kes_syslog | grep <MAC>（客户端日志）。访客排障先查 date（账号有有效期）与 cat /etc/resolv.conf（DNS 必须有效才能重定向门户，p385）。RADIUS 不通时：cat /var/config/AAA_server.conf（端口/密钥）、tcpdump -i br-wan -s 0 host <radiusIP>（p347）。
  tags: [troubleshooting, cli, commands]

- id: p32
  title: 认证方式安全等级排序（Open+门户 < MAC < PSK < 802.1X）
  type: principle
  source_chapter: "p310"
  source_quote: |
    "▪Open + Captive Portal
    • Cons: No Security
    ▪MAC authentication
    • Cons: MAC can be spoofed, no traffic encryption
    ▪WPA/WPA2/WPA3 Personal = Pre-Shared Key (PSK)
    • Cons: But all keys can be hacked or stolen (key shared by all users)
    ▪WPA/WPA2/WPA3 Enterprise = 802.1X
    • Pros: Strongest security, ease of Management, scalability"
  summary: |
    信任度从低到高：Open+Captive Portal（无加密，兼容一切设备）、MAC 认证（可伪造、无加密，适合打印机等哑终端）、PSK（部署简单但全员共用一把钥匙）、802.1X 企业级（最强、易管理、可扩展，但初始配置多）。选 SSID 安全方案时按此梯度权衡。
  tags: [security, ssid]

- id: p33
  title: SSID Usage 模板映射表（Usage 决定安全模型）
  type: principle
  source_chapter: "p313"
  source_quote: |
    "Usage: Guest Network / Employee BYOD Network / Enterprise Network for Employees / Protected Network / Protected Network for Employees (BYOD)
    Captive Portal Guest: Open or MAC
    Captive Portal BYOD: 802.1X or MAC followed by 802.1X
    PSK Guest / PSK BYOD: Pre-Shared Key (PSK)"
  summary: |
    Cirrus 建 SSID 时选 Usage 即套用预置模板（Access Policy/Authentication Strategy 自动生成，可再改）：Guest Network=Open 或 MAC+门户；Employee BYOD Network=802.1X 或 MAC+BYOD 门户；Protected Network=PSK+（可选）门户；Enterprise Network for Employees=802.1X。最小配置集（p314）：Allowed Band（2.4/5/6GHz）、认证源（None/Local Database/External Radius）、Default VLAN/Network；可选 ACL/QoS、Walled Garden、Access Role Profile（QoS 策略+带宽上限+VLAN）。
  tags: [ssid, usage, template]

- id: p34
  title: SSID 的 VLAN/Tunnel 映射与 VLAN 池（上限 256）
  type: principle
  source_chapter: "p319"
  source_quote: |
    "• Default VLAN
    • Single VLAN assigned to the SSID
    • VLAN Pooling
    • Pool of VLAN assigned to the SSID (up to 256)
    • Avoid large broadcast domain with a single VLAN"
  summary: |
    第 3 步 Schedule and VLAN Mappings 可按"全部站点/组"或"每 AP Group"设定：调度默认 Always Available（可按星期和时间段定制）；网络映射可选单 VLAN、多 VLAN 池（最多 256 个，避免单 VLAN 大广播域）、一条 Guest Tunnel、或 Tunnel+VLAN（隧道内允许 VLAN 标签）。
  tags: [ssid, vlan, mapping]

- id: p35
  title: 全局 PSK 与设备专用 PSK（DSPSK 的 Force/Prefer 语义）
  type: principle
  source_chapter: "p326"
  source_quote: |
    "• Force Device Specific PSK: No global PSK configured on the SSID level, only a specific passphrase per device is used.
    • Prefer Device Specific PSK: Device must use the passphrase returned from the MAC authentication. If not configured, user can use the global PSK passphrase"
  summary: |
    DSPSK 原理：开启后设备先做 MAC 认证，在 Company Property 数据库里按 MAC 查到专属 passphrase，用户必须用它连接。Force=SSID 级不设全局 PSK，仅每设备一把钥匙；Prefer=优先用设备专属钥匙，未登记设备仍可用全局 PSK。约束（p327）：必须启用 MAC 认证；加密不能选 AUTO_WPA_WPA2；全局 PSK/PassPhrase 字段仅在 Prefer 模式下可填。
  tags: [ssid, psk, dspsk]

- id: p36
  title: 私有组 PSK（PPSK）与动态私有组 PSK（D-PGPSK）
  type: principle
  source_chapter: "p328"
  source_quote: |
    "• Activate Private Group PSK and enter one/multiple entries:
    • A name to differenciate the entries
    • A unique passphrase
    • A pre-configured Access Role Profile"
  summary: |
    PPSK：DSPSK 关闭或 Prefer 时启用，可建多条"名称+独立 passphrase+绑定 ARP"的条目；用户用哪把钥匙就落入哪个 Access Role Profile，仍可用全局 PSK（落 SSID 默认 ARP）。动态 PPSK（p329-330）：DSPSK 设 Prefer + 启用 Dynamic Group PSK，每条 PSK 条目直接绑定 VLAN ID 和 ARP（同一 ARP 可在不同条目配不同 VLAN，无需为每个 VLAN 建 ARP）；用户用某 passphrase 即进对应 VLAN+ARP。Dynamic VLAN Selection 可选 Priority ARP over VLAN-ID（用 ARP 内 VLAN）或 Priority VLAN-ID over ARP（用条目里的 VLAN）。
  tags: [ssid, psk, ppsk, vlan]

- id: p37
  title: Employee SSID（802.1X）创建要点与客户端 PEAP 参数
  type: principle
  source_chapter: "p338"
  source_quote: |
    "> Usage: Enterprise Network for Employees (802.1X)
    > Encryption Type: WPA2_AES
    > Allowed Band: 2.4GHz and 5GHz
    > RADIUS Server: UPAMRadiusServer
    > Set the Authentication Source option to Local Database
    > Set the Web Authentication option to None"
  summary: |
    员工 SSID 标准配置：Usage=Enterprise Network for Employees、加密 WPA2_AES（RAP 实验用 WPA3_AES，p570）、双频；认证策略选 UPAMRadiusServer、Authentication Source=Local Database（也可外部 RADIUS）、Web Authentication=None（员工网络不需要门户）。Linux 客户端 802.1X 参数（p341）：ProtectedEAP、不校验 CA 证书、PEAP 版本 Automatic、内层 MSCHAPv2。建网前置：先建 VLAN 20 并在 6870/6360/2360 上 tagged，再在 6870 建 IP 接口（示例 int_employees 192.168.20.7/24，VLAN 20，IP Forward Enabled）；2360 不受 Cirrus 管需 CLI 手配（p334-337）。
  tags: [ssid, 8021x, employee, config]

- id: p38
  title: UPAM RADIUS 常数：端口 1812/1813、重试 2、超时 5 秒
  type: principle
  source_chapter: "p347"
  source_quote: |
    ""accountingPort":1813,
    "retries":2,
    "timeout":5,
    "authenticationPort":1812"
  summary: |
    AP 侧 AAA_server.conf 中 UPAMRadiusServer 默认参数：认证端口 1812、计费端口 1813、重试 2 次、超时 5 秒。排障顺序：先 cat /var/config/wlanservice.conf 与 AAA_profile.conf 确认 AP 已取到 RADIUS 配置和 AAA Profile，再查 AAA_server.conf 的服务器地址/密钥，仍失败用 tcpdump 抓包并核对 RADIUS 服务端配置。
  tags: [radius, constants, troubleshooting]

- id: p39
  title: UPAM 组成与可选认证源
  type: principle
  source_chapter: "p351"
  source_quote: |
    "UPAM consists of
    • Guest Access
    • BYOD Access
    • A built-in RADIUS Server
    • A built-in MAC Authentication Server"
  summary: |
    UPAM（Unified Policy Authentication Manager）内嵌于 OmniVista Cirrus，同时服务 AOS 交换机与 Stellar AP，含访客接入、BYOD 接入、内置 RADIUS、内置 MAC 认证四大件；另提供邮件服务（访客赞助审批）、外置日志（syslog）、专属门户+数据库。认证源（p354）可选：内置 RADIUS+本地库、外部 RADIUS、IMSI/IMEI 库（Celona Edge）、云身份（Azure AD）。监控入口：Network>Access Records>Authentication Records / Captive Portal Records（p342、p383）。
  tags: [upam, authentication]

- id: p40
  title: Guest Access Strategy 三大配置块
  type: principle
  source_chapter: "p357"
  source_quote: |
    "• Guest Access Strategy defines:
    • Login Strategy
    • How the Guest is authenticated: credentials, access code, Terms & conditions, Simple Persona (no T&C)"
  summary: |
    Guest Access Strategy 定义：(1) Login Strategy——凭据/访问码/条款/Simple Persona（无 T&C），还支持 Azure 与社交登录（Facebook、Rainbow、Office365）；(2) Post Portal Enforcement——门户认证通过后给访客换新 Role（ARP）限权；(3) 自注册策略——访客自建账号可由员工审批。建 Guest SSID 工作流（p360）：选 Guest Network 用途+激活 Captive Portal→认证策略选 RADIUS→本地库建访客账号→配 Guest Access Strategy→挂 VLAN。
  tags: [upam, guest, strategy]

- id: p41
  title: Guest SSID 配置规则（Allow All EAPs=Yes、Web Auth=Guest）
  type: principle
  source_chapter: "p379"
  source_quote: |
    "> Set the Allow All EAPs to Yes.
    > Set the Authentication Source option to None
    > Set the Web Authentication option to Guest"
  summary: |
    Guest SSID 建法：Usage=Guest Network、Captive Portal=YES、类型 OV-UPAM Captive Portal、Enhanced Open=Disabled；认证策略 RADIUS 选 UPAMRadiusServer，Access Policy 中 Allow All EAPs=Yes、Authentication Source=None、Web Authentication=Guest；再建 Guest Access Strategy（含 Captive Portal Template）并在 VLAN 映射挂 Guest VLAN（实验为 30）。客户端连上后需手动开浏览器访问任意非 https URL（如 http://2.2.2.2）触发门户重定向（p381）。
  tags: [ssid, guest, captive-portal]

- id: p42
  title: Guest Tunneling 规则：按 ARP 建 L2 GRE 隧道
  type: principle
  source_chapter: "p367"
  source_quote: |
    "• Tunnel per Access Role Profile from Access Point to a switch/router/controller.
    • L2 GRE tunnel over L2/L3 networks
    • OmniSwitch simplifies deployment with automatic tunnel creation to AP IP
    • GRE Backup tunnel can be added for resiliency"
  summary: |
    访客隧道用于在不破坏企业安全的前提下叠加访客网络：控制哪些流量进隧道；每个 Access Role Profile 一条从 AP 到交换机/路由器的 L2 GRE 隧道（可跨 L2/L3 网络）；OmniSwitch 支持自动向 AP IP 建隧道简化部署；可加 GRE Backup 隧道做冗余。SSID 创建第 3 步的网络映射中可选 Guest Tunnel 或 Tunnel+VLAN（VLAN 标签封在隧道内）。
  tags: [guest, tunnel, gre]

- id: p43
  title: BYOD SSID 的 VLAN 流转：预认证 Guest VLAN → 认证后 Employee VLAN
  type: principle
  source_chapter: "p391"
  source_quote: |
    "The BYOD employee device will be placed first in the Guest VLAN (pre-authentication). Once authenticated via a Captive Portal, it will be moved to the Employee VLAN(post-authentication)."
  summary: |
    Employee BYOD SSID 不需要新建 VLAN：SSID 的 VLAN 映射挂 Guest VLAN（实验 30）作为预认证落点；BYOD Access Strategy 中 Post Portal Authentication Enforcement 绑定一个 Access Role Profile（该 ARP 内配 VLAN 20），员工在门户用企业凭据认证成功后即被切到 Employee VLAN。验证：Analytics>Clients 里该客户端 VLAN 应变为 20（p395）。BYOD 认证源可为本地库、外部 LDAP/AD、RADIUS。
  tags: [byod, ssid, vlan]

- id: p44
  title: 统一策略与三级带宽控制及执行顺序
  type: principle
  source_chapter: "p408"
  source_quote: |
    "• Bandwidth contract at SSID level
    • Bandwidth assigned per SSID and per AP, shared between all users connected to the SSID
    • Bandwidth contract at Access Role Profile level
    • Bandwidth assigned to the users using this profile
    • Bandwidth contract at Role level
    • A Policy List (ACL/QoS) can restrict the Bandwidth as an action"
  summary: |
    Policy List=策略规则（QoS/ACL）的有序集合，动作可为 Accept/Drop、限速、802.1p/DSCP 标记，双向执行；来源可为 RADIUS 账号属性或 ARP 的 Default Policy List。带宽控制三层：SSID 级（每 SSID 每 AP 共享池，Detailed SSID Settings 里配）、ARP 级（该 Profile 每用户）、策略规则级（ACL/QoS 动作限速）。执行优先序（p409）：用户流量先匹配 Policy List 中 ACL→按 ACL 带宽执行；未匹配再看 ARP 是否设带宽；都没有则受 SSID 合同约束；SSID 也未设则不限速。另有 Location Policy（限定接入位置）与 Period Policy（限定接入日/时段），作用于该 ARP 的设备（p406）。
  tags: [qos, policy, bandwidth]

- id: p45
  title: 客户账号类型与必填字段（员工/公司资产/访客/Guest Operator）
  type: principle
  source_chapter: "p426"
  source_quote: |
    "▪ Login/password (mandatory)
    ▪ Expiration date (mandatory)
    ▪ Service Level/Registration profile (mandatory)"
  summary: |
    UPAM 本地库四类账号：Employee（登录名/密码必填；可配 Session timeout、计费间隔、上下行带宽上限）；Company Property（MAC 必填，用于 BYOD/DSPSK，可绑员工账号/ARP/Policy List）；Guest（登录名/密码/失效日期/Service Level 或 Registration Profile 均必填）；Guest Operator（登录名/密码必填+联系方式，用专属门户建访客账号、审批自注册）。全局设置（p427）：批量建号、有效期策略、过期删除策略（Never/到期即删/N 天后删）。Service Level（p428）最多建 5 个，每个绑定 ARP+Unified Policy List+Registration Profile+有效期+删除策略。密码策略默认"弱"可改强（最小长度+复杂度，p422）。
  tags: [accounts, upam, guest]

- id: p46
  title: Registration Profile：数据/时间配额与耗尽处理
  type: principle
  source_chapter: "p429"
  source_quote: |
    "▪Data Quota:
    • Max data traffic allowed per guest (in MB)
    ▪Time Quota:
    • Time Quota per day (in hours)
    • Time Quota by hours (total number of hours)
    ▪Exhaustion Handling:
    • Block for remaining Duration (Redirection URL)
    • Reduced up/down bandwidth (in kB/s)"
  summary: |
    Registration Profile 定义：数据配额（MB）、时间配额（每天小时数+总小时数）、有效期、Remember Device 与最大设备数、配额耗尽处理——阻断剩余时长（可配重定向 URL）或降速（分别设上行/下行 kB/s）。书中示例：100MB+每天 4 小时，耗尽后 UP=100kB/s、DOWN=1000kB/s；Day1 用 90MB/3H 无动作，Day2 超 100MB 触发限速。访客票据（Ticket）可自定义页眉/页脚/Logo 并从账号列表打印（p431）。
  tags: [quota, guest, upam]

- id: p47
  title: DRM 分布式射频管理原则
  type: principle
  source_chapter: "p439"
  source_quote: |
    "• Each AP communicates with its neighbor APs
    • Over the air protocol : neighbor AP discovery
    • Over the LAN protocol : RF management
    • RF context sharing
    • Each AP can take RF action (try, wait, retry mechanism)
    • Limited to neighbor APs
    • Does not rely on AP Group or AP management vlan"
  summary: |
    DRM 完全分布式：空口协议做邻居发现，LAN 侧协议做 RF 管理与上下文共享（信道利用率/干扰/每频段客户端数/功率等）；每台 AP 可自主采取 RF 动作（尝试-等待-重试），作用域限于邻居 AP，不依赖 AP Group 或管理 VLAN。RF Profile（含国家代码）可按 AP Group 或单 AP 下发；管理员可在 RF Profile 里为 5GHz（含 High/Low）和 6GHz 指定 ACS 可选信道列表，选够信道避免 AP 间干扰（p443）。
  tags: [rf, drm, automation]

- id: p48
  title: Smart Air Share 最小数据速率推荐值（2.4G=12、5G=24、6G=24）
  type: principle
  source_chapter: "p444"
  source_quote: |
    "• 2.4G client minimum data rate control →Advanced control (recommended value 12)
    • 5G client minimum data rate control →Advanced control (recommended value 24)
    • 6G client minimum data rate control →Advanced control (recommended value 24)"
  summary: |
    SSID 配置中的 Smart Air Share 面向 802.11a/n 客户端做精细化控制，提升整体 Wi-Fi 体验：最小数据速率推荐 2.4G=12Mbps、5G=24Mbps、6G=24Mbps（抬高最低速率可逼远端弱信号客户端切换到更近 AP）；另可分别设置 2.4G/5G/6G 的管理帧（beacon）速率。
  tags: [rf, ssid, optimization, constants]

- id: p49
  title: 智能负载均衡与关联 RSSI 阈值推荐（2.4G=5、5G=10）
  type: principle
  source_chapter: "p445"
  source_quote: |
    "• Association RSSI Threshold
    • Deny connection to APs when wireless signal of client is too weak (RSSI)
    • Disconnect a client when the signal of this client becomes weak
    • Recommended value: 2.4G = 5 , 5G = 10"
  summary: |
    Smart Load Balance 两功能：Band Steering 把双频客户端引向 5/6GHz（可选强制）；Dynamic Load Balance + Association RSSI Threshold 拒绝信号过弱的客户端接入、信号变弱时将其断开。关联 RSSI 阈值推荐 2.4G=5、5G=10。实验佐证（p460-463）：把阈值设 90 后 RSSI 51dB 的客户端全部关联失败，QoE>Analytics 里可见 "RSSI threshold not met" 失败记录；调回默认即恢复。
  tags: [rf, load-balance, rssi, constants]

- id: p50
  title: Band Steering 判定阈值、信道过载定义（70%/1 分钟）与默认禁用原因
  type: principle
  source_chapter: "p446"
  source_quote: |
    "• Pri-Diff. = 5G High Client # – 2.4G Client # (Threshold:10)
    • Sec-Diff. = 5G Low Client # – 2.4G Client # (Threshold:10)
    Diff. = 5G Client Number – 2.4G Client Number (Threshold:10)
    Overloaded: A channel is considered overloaded when its average medium utilization over the span of a minute exceeds 70%."
  summary: |
    频段引导按客户端数差值判定：双频 AP 取 5G-2.4G 客户端数差，三频 AP 分 5G High/5G Low 各与 2.4G 求差，阈值均为 10；信道"过载"定义为 1 分钟平均介质利用率超过 70%。注意 Band Steering 默认禁用（p459）：前提是 2.4G 与 5G 覆盖大致相同，若 5G 覆盖明显弱/有洞会出问题；对策——网络设计成双频同覆盖，做不到就别用 band steering 或用 Exclude MAC OUI 排除老旧/时延敏感终端（扫描枪、MIPT 话机）。Force 5G/6G 模式则完全不允许回落 2.4G，5/6G 信号弱的区域会出覆盖问题（p460）。
  tags: [rf, band-steering, thresholds]

- id: p51
  title: 背景扫描参数：默认 20 秒/50 毫秒，WIPS 依赖扫描
  type: principle
  source_chapter: "p448"
  source_quote: |
    "• Scanning Interval and duration
    • Default interval = 20 sec – Range = 5-10800 sec
    • Default Duration = 50 ms – Range = 50-110 ms"
  summary: |
    每个射频周期性逐信道扫空口；扫描期间无法收发 802.11 数据（影响客户端）。扫描是 WIPS 的必要条件（干扰/Rogue AP 检测、攻击检测）。参数：间隔默认 20 秒（范围 5-10800 秒），时长默认 50ms（范围 50-110ms）。可选 Dedicated AP scanning mode 让整台 AP 只做扫描；Voice and Video Awareness 在 AP 有活动语音/视频会话（检测 SIP、H.323）时跳过扫描。权衡（p451）：间隔加大/时长减小=入侵漏检风险升、客户端性能好；反之亦然。
  tags: [rf, scanning, wips, constants]

- id: p52
  title: 信道宽度选项与发射功率范围（显式模式）
  type: principle
  source_chapter: "p450"
  source_quote: |
    "• Channel width for 2.4G: 20Mhz (default) or 40 Mhz
    • Channel width for 5G, 5G Low, 5G High: 20Mhz , 40 Mhz (default), 80Mhz or 160 Mhz
    • Channel width for 6G: 20Mhz , 40 Mhz, 80Mhz or 160 Mhz
    • Power: Auto or value in 3-23Dbm"
  summary: |
    信道/功率有 Auto（ACS/APC 自动调优，基于邻居共享的 RF 上下文，与背景扫描开关无关，但信道宽度仍需手选）与 Explicit 两种模式。显式模式手设信道号（受国家代码限制）、宽度与功率：2.4G 宽度 20MHz（默认）或 40MHz；5G/5G Low/5G High 为 20/40（默认）/80/160MHz；6G 为 20/40/80/160MHz；功率 Auto 或 3-23dBm。另可设 Min/Max TX Power、External Antenna Gain（仅外置天线型号）、Beacon interval、Short Guard Interval、MU-MIMO、High Efficiency 开关（p462）。
  tags: [rf, channel, power, constants]

- id: p53
  title: RF 优化推荐参数总表
  type: principle
  source_chapter: "p451"
  source_quote: |
    "• Low value recommendation is 10, many weak client can associated, overall throughput is low.
    • High value recommendation 25, weak client cannot associate, overall throughput is better.
    It is recommended to use auto channel & power instead of static setting."
  summary: |
    官方推荐基线：Band Steering=Enable（若双频覆盖对等）；信号强度/客户端 SNR 阈值保持默认（低值 10 放弱客户端入网拉低整体吞吐，高值 25 拒弱客户端保吞吐）；Dynamic Load Balance=Enable；Background Scanning=Enable（仅为 WIPS 所需），间隔/时长保持默认；Voice and Video Awareness=Enable；Short Guard Interval=Enable（射频环境差、客户端拥挤时关闭）；信道与功率用 Auto 而非静态；信道宽度保持默认——密集部署用窄宽度、稀疏部署用宽宽度。
  tags: [rf, optimization, checklist]

- id: p54
  title: RSSI-dBm 换算表与信号质量分级
  type: principle
  source_chapter: "p454"
  source_quote: |
    "RSSI dBm
    10 -86
    20 -76
    30 -66
    43 -53
    Bad / Not recommended for Video or Audio applications
    OK – not bad
    Desired and recommended"
  summary: |
    换算规律：dBm = RSSI - 96（如 RSSI 10=-86dBm、20=-76dBm、43=-53dBm；反向例 -24dBm=72 RSSI）。质量分级：低端（约 RSSI<20）为 Bad，不建议跑视频/音频；中段 OK 偏弱；高端（约 RSSI>30）为期望推荐值。注意口径差异：Cirrus 上显示平均值，AP CLI（wlanconfig）为瞬时值（p453）。
  tags: [rf, rssi, constants]

- id: p55
  title: SGI 增益、MU-MIMO/HE 开关与 RF Profile 下发路径
  type: principle
  source_chapter: "p462"
  source_quote: |
    "Guard Interval is used to ensure that distinct transmissions occur between the successive data symbols transmitted by a device. This would provide approximately an 11% increase in data rates.
    If disabled, a High Efficiency mode capable AP will downgrade to VHT (Very High Throughput) mode."
  summary: |
    Short Guard Interval 约提升 11% 速率，但信道时延扩展超限或收发定时不准时误包率上升（恶劣环境关闭）。MU-MIMO 开启后 AP 可同时与多用户通信；High Efficiency 关闭时 802.11ax AP 会降级到 VHT 模式。RF Profile 生效路径（p463）：AP Group>Provisioning Configuration>Basic Information 里改 RF Profile（组级），或 Device Catalog>Edit Device>Group/RF Profile 对单 AP 覆盖；排障可 cat /tmp/config/rfprofile.conf 看下发结果、cat /proc/kes_syslog | grep ACS 查自动选信道日志（p465-466）。
  tags: [rf, sgi, mu-mimo, config]

- id: p56
  title: 漫游默认状态与快漫游协议约束（OKC/802.11r 的加密前提）
  type: principle
  source_chapter: "p471"
  source_quote: |
    "• L2 Roaming always enabled
    • L3 Roaming disabled by default
    • L3 Roaming configured in the SSID Configuration
    • Fast Roaming disabled by default
    • OKC can be enabled with WPA2/WPA3 Enterprise only
    • 802.11r (Fast Roaming) can be enabled with WPA2/WPA3 encryption only (Personal or Enterprise)"
  summary: |
    L2 漫游永远开启；L3 漫游默认关闭、在 SSID 配置里开启（基于 home/foreign AP 间 L2 GRE 隧道）；Fast Roaming 默认关闭、按 SSID 开启。协议硬约束：OKC（802.11k，优化信道列表辅助选目标 AP）仅 WPA2/WPA3 Enterprise 可用；802.11r（FT 快速切换，省 RADIUS 重认证）要求 WPA2/WPA3 加密（Personal 或 Enterprise 均可）。漫游依赖客户端上下文在空口相邻 AP 间共享（Add/Del 消息机制，p473），仅限同一 OmniVista 管理且新 AP 有相同 WLAN service 的场景（p475）。
  tags: [roaming, 80211r, 80211k]

- id: p57
  title: L2/L3 漫游判定表（三个条件决定结果）
  type: principle
  source_chapter: "p476"
  source_quote: |
    "Client Context exists on the new AP?
    WLAN service and Access Role Profile exist in the Client Context on the new AP?
    Client Context VLAN ID = VLAN ID mapped to the Access Role Profile on the new AP?
    Yes/Yes/Yes → L2 Roaming
    Yes/Yes/No → L3 Roaming
    No → No Roaming, new client"
  summary: |
    判定链（基于 home/foreign AP 间的管理 VLAN/VLAN 映射差异）：新 AP 无客户端上下文→不漫游按新客户端处理；有上下文但 WLAN service/ARP 不存在→同样按新客户端；上下文齐全且上下文 VLAN=新 AP 上映射给该 ARP 的 VLAN→L2 漫游；上下文齐全但 VLAN 不同→L3 漫游（home AP 保持客户端上下文并经 GRE 隧道回程，p485-487）。典型触发：同一 SSID 在不同 AP Group 映射了不同 VLAN（如 Group1=2001、Group2=2002）。
  tags: [roaming, l2, l3]

- id: p58
  title: 粘滞客户端规避与 Roaming RSSI 阈值（推荐 2.4G=10、5G=15）
  type: principle
  source_chapter: "p492"
  source_quote: |
    "• Use the Roaming RSSI Threshold in the RF profile.
    • Use in conjuction with 802.11k and 802.11v
    • Value range is 0-100
    • Recommended value for 2.4GHz : RSSI = 10
    • Recommended value for 5GHz : RSSI = 15"
  summary: |
    漫游决定权在客户端，部分设备粘住旧 AP。组合拳：RF Profile 的 Roaming RSSI 阈值（范围 0-100；推荐 2.4G=10、5G=15）+ 802.11v（BSS Transition Management 提供漫游目标）+ 802.11k（引导客户端漫游到最优 AP）。阈值过低→客户端守着弱信号不漫游；过高→漫游过于频繁导致丢包。关联阈值与漫游阈值语义不同：前者管"能不能连"，后者管"何时该走"（p461）。
  tags: [roaming, rssi, sticky-client]

- id: p59
  title: 相邻 AP 互相看不见时的静态邻居配置
  type: principle
  source_chapter: "p491"
  source_quote: |
    "• In some cases, Stellar APs are geographical neighbors but can't see each other (i.e: radio waves blocked by corridor with right angles,…).
    • Client context can't be shared. No roaming.
    • Solution:
    • On both AP, add statically the neighbor Stellar AP from the list of known AP."
  summary: |
    地理相邻但空口互相侦听不到（直角走廊等遮挡）时无法共享客户端上下文→无法漫游。解决：在两台 AP 上互相静态添加对方为 Neighbor AP（AP Registration>Access Point 视图>Neighbor AP>Edit 选择），上下文改走 LAN 共享即可漫游。规划期用 Heat Map 分别检查 2.4/5/6GHz 覆盖（三者覆盖范围不同），有重叠才有漫游（p490）。
  tags: [roaming, neighbor-ap, troubleshooting]

- id: p60
  title: RAP 部署设备要求与开局五步
  type: principle
  source_chapter: "p497"
  source_quote: |
    "▪OmniVista Cirrus
    • With OmniVista 2500
    * AP1101 not compatible with the RAP Feature"
  summary: |
    RAP（Remote Access Point）把企业网延伸到远程站点（门店/展会/家庭办公）。所需设备：OV Cirrus + OV2500 + ALE VPN Server 虚机 + Stellar AP（AP1101 不兼容 RAP）。开局五步（p499）：(1) AP 启动并以序列号在 Cirrus 注册；(2) Cirrus 下发 RAP 模式、VPN 客户端 IP、VPN Server 公网 IP、OV2500 IP；(3) AP 与 VPN Server 建管理流量 VPN 隧道；(4) 从 OV2500 取配置（SSID/RF 等）；(5) 建第二条客户端数据 VPN 隧道，远程用户上企业网。管理员预置（p500/p508）：Cirrus 建 RAP 专用组织+登记序列号+配 Mgmt VPN（Server 公网 IP/端口、VPN IP、客户端 IP 池、OV2500 IP）并导出 .conf；部署 VPN Server VM（eth0=公网、eth1=私网）；.conf 上传至 /opt/OmniVista_2500_NMS/data/vpn_conf/vpn_profile 后导入；OV2500 配默认路由、Data VPN Server（实验：vpn_mgmt 192.168.0.1/.2-20，vpn_data 10.7.0.61/.55-60）并挂到 AP Group；SSID 用 Use Tunnel（Tunnel ID=0）选 VPN Server。
  tags: [rap, vpn, deployment]

- id: p61
  title: WIPS 三类 AP 分类与 Rogue 遏制默认开启
  type: principle
  source_chapter: "p514"
  source_quote: |
    "• Rogue AP Containment – enabled by default
    • The scanning Stellar AP sends de-auth request to all clients associated to the rogue AP
    • Friendly AP is not reported as Interfering or Rogue
    • Friendly AP OUI can be set – ALE OUI set by default"
  summary: |
    空口发现的外部 AP 分三类：Interfering（默认所有陌生 AP；同 OVC 管理的 AP 排除）、Rogue（命中 Rogue AP 策略者）、Friendly（手工添加，永不判 Rogue；Friendly OUI 默认含 ALE OUI，可追加）。Rogue Containment 默认开启：扫描 AP 向 Rogue AP 的关联客户端发 de-auth。前提：WIPS 全局配置作用于 OV 管理的全部 AP，且 AP 必须开扫描。注意每个 AP 每 SSID 双频各一个 BSSID，干扰列表中同一 AP 会出现多条（p524）。
  tags: [wips, rogue, security]

- id: p62
  title: Rogue AP 策略四条件与信号阈值默认 -70dBm
  type: principle
  source_chapter: "p515"
  source_quote: |
    "Signal Strength Threshold
    The detected AP signal in dbm is too strong and above the threshold
    Default: – 70 dbm ; Range -50 to -90 dbm
    Detect Valid SSID
    The detected foreign AP is broadcasting a SSID that is configured in OmniVista Cirrus..."
  summary: |
    Interfering AP 命中任一策略即升 Rogue：(1) Signal Strength Threshold——信号强于阈值（默认 -70dBm，范围 -50~-90dBm；实验界面默认 Disabled，p523）；(2) Detect Valid SSID——广播了你 Cirrus 里配置的合法 SSID（默认 Enabled）；(3) Detect Rogue SSID Keyword——SSID 名含关键字（黑名单）；(4) Rogue OUI——MAC OUI 匹配。改参数需谨慎：Rogue 动作（de-auth）可能波及其他无线网络。
  tags: [wips, rogue, thresholds]

- id: p63
  title: 无线攻击检测与客户端黑名单触发常数（10 次/60 秒、老化 1 天）
  type: principle
  source_chapter: "p524"
  source_quote: |
    "- The maximum authentication failure times. By default, if a client fails to authenticate 10 times in 60 seconds, it will be placed in the blocklist.
    - And a client placed in a blocklist is removed from it after one day (Aging Time = 1 day by default)."
  summary: |
    无线攻击检测默认开启（p516），分 AP 攻击与客户端攻击两类策略，检测级别 Custom/High/Medium/Low。Client Blocklist Policy 默认禁用（p517）：开启后攻击源 MAC 进黑名单，全网 Stellar AP 拒绝其关联；默认触发条件 60 秒内认证失败 10 次，老化时间 1 天（可配）。局限：源 MAC 可能是 AP/BSSID/网卡任意 MAC，只有真实无线客户端 MAC 拉黑才有意义。
  tags: [wips, attack, blocklist, constants]

- id: p64
  title: 勘测三类型与适用阶段（Predictive/Passive/Active）
  type: principle
  source_chapter: "p529"
  source_quote: |
    "Passive
    • Listen WLAN traffic
    • No authentication and 802.11 association
    • All frequencies are scanned
    Active
    • Associate survey tool to (multiple) access point
    • Measure packets loss / retransmission / physical rates
    Predictive
    • Simulation tool
    • Import site plan & RF characteristics of objects"
  summary: |
    被动勘测：只听不发（不关联不认证），扫全频段，测 AP 发现/信号强度/噪声；主动勘测：工具关联 AP，额外测丢包/重传/物理速率；预测勘测：纯仿真，导平面图和材料 RF 特性建模并自动布 AP。阶段匹配（p530）：新建网/换网前用 Predictive；部署后 RF 分析用 Passive；部署后客户端性能分析用 Active。工具：Ekahau Site Survey（Windows）、WiFi Analyzer（Android）。
  tags: [survey, methodology]

- id: p65
  title: 信号衰减材质清单与现场排障三步法
  type: principle
  source_chapter: "p533"
  source_quote: |
    "• Signal degrades when going through:
    • Concrete (walls) • Wood (doors) • Metal (cabinet, shelves,…) • Steel (building structure)
    • Glass & Mirrors • Brick (fireplace) • Water (liquid: fish tank; vapor: bathroom)"
  summary: |
    信号劣化主因：AP 位置不当（正对墙体/立柱，应两侧各放一台或加 AP）、材质衰减（混凝土/木材/金属/钢构/玻璃镜面/砖/水）、天线类型选错（定向 vs 全向按覆盖形状选）、同频/邻频干扰（换信道）。现场三步（p537-540）：Step1 拿平面图，标障碍、需求区域（高/中优先级）和 AP 位置；Step2 勘测观察——AP 型号是否与设计一致、AP 间 RF 重叠/同频邻频干扰、盲区（AP 宕机或缺位）、发射功率是否默认值（示例默认 17dBm，可加大改善覆盖）、位置是否别扭；Step3 纠正——换 AP 型号、改功率/信道、收窄信道宽度、去掉低速率逼客户端用更近 AP、优化 AP 布放。参考量：4 米穿 1-4 面墙后 RSSI 约 -70dBm，不够 VoWLAN 使用（p533）。
  tags: [survey, attenuation, troubleshooting]
