# principles 候选 — DT00XTE301 LAN & WLAN Installation & Configuration for SMB

## P01. PoE 四标准功率等级对照
- 页码：<<<PAGE 147>>>
- 原文摘录："802.3af (Type 1) 'PoE': Power available at the PD 12.95 W, Max delivered 15.40 W, 350 mA, Three power class levels (1-3) / 802.3at Type 2 'PoE+': 25.50 W / 30.0 W / 600 mA, Four class (1-4) / 802.3bt Type 3: 51 W / 60 W, Six class (1-6) / Type 4: 71 W / 100 W, Eight class (1-8)"
- 提取内容：PD 可用功率 / PSE 最大供给 / 电流 / 等级数四栏对照，PoE 预算计算的基础。

## P02. PoE 端口优先级与断电顺序
- 页码：<<<PAGE 151>>>
- 原文摘录："Low: inline power to low-priority ports is interrupted first / Critical: inline power to critical ports is maintained as long as possible"
- 提取内容：功耗超预算时按 Low → High → Critical 顺序断电；关键设备（如 AP 上联口）应设 critical。

## P03. PoE 动态分配与型号标识
- 页码：<<<PAGE 147>>>、<<<PAGE 148>>>
- 原文摘录："Dynamic PoE Allocation: Provide only the amount of power needed by powered devices (PD) up to the total energy budget"；"OmniSwitches models compatibles with the PoE protocol have the « P » letter in their reference."
- 提取内容：型号带 P 才支持 PoE；按 PD 实际需求动态供电提高总预算利用率。

## P04. EEE（802.3az）适用边界
- 页码：<<<PAGE 146>>>
- 原文摘录："EEE is only applicable to OmniSwitch copper ports operating at 100/1000 Mbps speed"，且不兼容光口"U"机型。
- 提取内容：空闲低功耗仅限铜缆 100/1000M 端口。

## P05. 电容检测法仅限 legacy 话机
- 页码：<<<PAGE 152>>>
- 原文摘录："Not compatible with IEEE specification 802.3af. It should only be enabled to support legacy IP phones"
- 提取内容：capacitor-detection 是非标检测，只用于老式 IP 话机，默认不开启。

## P06. OmniSwitch 交换机默认凭据与强制改密策略
- 页码：<<<PAGE 60>>>、<<<PAGE 61>>>
- 原文摘录："Default login name and password: Login: admin, Password: switch"；"Beginning in 8.10R3 a warning message will be displayed … Beginning in 8.10R4 changing the default password will be mandatory."
- 提取内容：admin/switch 默认凭据；8.10R3 起告警、8.10R4 起强制修改。本地用户库 userTable9 存于 flash/system，最多 64 用户。

## P07. ASA 认证服务禁用语义
- 页码：<<<PAGE 58>>>、<<<PAGE 59>>>
- 原文摘录："Authenticated Switch Access (ASA) feature: Lock or Unlock session types (aaa authentication command)"；示例 `-> no aaa authentication http` 后 "Service type = Http, Authentication = denied"
- 提取内容：Console/Telnet/FTP/HTTP/SSH/SNMP 各管理通道独立开关；默认 Console+Default 走 local 库。

## P08. exit-on-fail 与多服务器 fail-through
- 页码：<<<PAGE 63>>>
- 原文摘录："aaa authentication {console | telnet | …} server1 [server2...] [local] [exit-on-fail {enable | disable}]"；"When enabled, the switch uses only the first available server in the list … When disabled, the switch uses all the available servers"
- 提取内容：exit-on-fail 启用时只查首台可用服务器，禁用时逐台回退（fail-through）。

## P09. WebView 嵌入式管理与安全默认
- 页码：<<<PAGE 68>>>、<<<PAGE 69>>>
- 原文摘录："The WebView application is embedded in the switch and is accessible via a web browser"；"webview force-ssl enable: Forces SSL connection between browser and switch (default=enabled)"，TLS 1.2（<<<PAGE 109>>>）
- 提取内容：WebView 内嵌于交换机、仅限单机视图，默认强制 HTTPS。

## P10. 并发会话数上限
- 页码：<<<PAGE 67>>>
- 原文摘录："Telnet 6 / FTP 4 / SSH + SFTP 8 / HTTP 4 / Total sessions 20 / SNMP 50"
- 提取内容：各类管理会话的规格上限。

## P11. EMP 带外管理口原理
- 页码：<<<PAGE 66>>>
- 原文摘录："Bypass the network interface modules (NI) … Remotely manage the switch directly via the CMM"；`ip interface master emp address 172.25.167.203 mask 255.255.255.224`
- 提取内容：EMP 绕过业务端口直连 CMM 的带外管理通道；无 EMP 机型可用 USB Ethernet Dongle 等效。

## P12. Console 默认串口参数
- 页码：<<<PAGE 65>>>
- 原文摘录："Speed (baud): 115200 / Parity: None / Stop bits: 1 / Flow control: none"（新一代 6900/6860N 速率不同）
- 提取内容：Tera Term/Putty 连接交换机 console 的标准参数。

## P13. AOS 启动序列（Bootrom → 镜像选择 → RAM 加载）
- 页码：<<<PAGE 119>>>
- 原文摘录："Bootstrap Basic Operation (U-Boot) / Hardware Initialization / Memory Diagnostics / Image selection / AOS is copied and loaded into RAM"
- 提取内容：U-Boot 引导 → 硬件初始化 → 内存诊断 → 镜像选择 → 拷入 RAM 运行。

## P14. 冷启动目录选择规则与 reload all 特例
- 页码：<<<PAGE 132>>>
- 原文摘录："The switch will reboot from certified directory if contents are different from the running directory … IF THE OMNISWITCH IS REBOOTED WITH THE 'RELOAD ALL' COMMAND, IT WILL REBOOT FROM THE CERTIFIED DIRECTORY, NO MATTER WHAT"
- 提取内容：内容一致从 running 启动，不一致回退 certified；`reload all` 无条件从 certified 启动。

## P15. 从 Certified 目录运行时无法保存配置
- 页码：<<<PAGE 124>>>、<<<PAGE 135>>>
- 原文摘录："When the switch boots from the CERTIFIED directory, changes made to the switch cannot be saved"；`write memory` 报 "ERROR: Write memory is not permitted when switch is running in certified mode"
- 提取内容：certified 运行模式为只读保护，需 `modify running-directory` 切回可写目录。

## P16. write memory flash-synchro 组合语义
- 页码：<<<PAGE 122>>>
- 原文摘录："write memory flash-synchro = write memory + copy running certified"
- 提取内容：一步完成保存 + 认证同步。

## P17. USB 自动备份机制
- 页码：<<<PAGE 126>>>、<<<PAGE 138>>>
- 原文摘录："switch will store image files, power supply and system configuration files to USB storage drive automatically upon user commands 'write memory' or 'copy running-certified' … if USB backup is enabled"；可设密码加密备份内容
- 提取内容：启用后写配置即自动镜像到 /uflash。

## P18. Thin Client 模式（零配置交换机）
- 页码：<<<PAGE 127>>>
- 原文摘录："No configuration is stored on the switch. It will contact OmniVista 2500 to retrieve the config. … 'write memory' can be executed but configurations will not be saved"
- 提取内容：配置全量由 OV2500 下发，本地仅保留最小网络可达配置。

## P19. CLI 内建辅助（补全/过滤/历史/帮助）
- 页码：<<<PAGE 128>>>
- 原文摘录："Completion: Recognize partial keywords … Eg: sh vl for show vlan"；"-> show mac-learning | grep 00:20:da:55:56:76"；`?` 在线帮助
- 提取内容：AOS CLI 的效率特性集合。

## P20. VLAN 广播域划分与端口入组四途径
- 页码：<<<PAGE 158>>>
- 原文摘录："Ports become members of VLANs by: Static Configuration / Mobility with or without Authentication / 802.1q / VLAN Mobile Tag"
- 提取内容：VLAN 逻辑分段 LAN，端口成员有静态、移动、802.1Q、Mobile Tag 四种来源。

## P21. 默认 VLAN 与静态端口分配
- 页码：<<<PAGE 159>>>、<<<PAGE 160>>>
- 原文摘录："By default, all ports belong to VLAN 1"；`vlan 2 members port <slot>/<port> untagged`
- 提取内容：untagged 即端口的 default VLAN；多词 VLAN 名需引号。

## P22. VLAN 间路由触发条件
- 页码：<<<PAGE 162>>>
- 原文摘录："IP routing is active as soon as at least one IP interface is associated with a VLAN"；`ip interface <name> address <ip/mask> vlan <vlan_id>`
- 提取内容：任一 VLAN 绑定 IP 接口即激活三层路由（虚拟路由器网关模式）。

## P23. 802.1Q 标签结构与地址空间
- 页码：<<<PAGE 166>>>
- 原文摘录："4096 unique VLAN Tags (addresses) / VLAN ID == GID == VLAN Tag / 802.1P: Three bits field within 802.1Q header, Allows up to 8 different priorities"
- 提取内容：4 字节标签 = 12bit VLAN ID + 3bit 802.1p 优先级。

## P24. Mobile Tag 与 802.1Q 的分工
- 页码：<<<PAGE 170>>>
- 原文摘录："VLAN Mobile Tag: Allows mobile ports to receive 802.1Q tagged packets … Takes precedence over all VLAN Rules / 802.1Q Tag: Not supported on mobile ports"
- 提取内容：固定端口用 802.1Q 静态打标；移动端口靠 Mobile Tag 按 VID 动态归类且优先级最高。

## P25. STP 双模式三协议与收敛时间
- 页码：<<<PAGE 238>>>
- 原文摘录："flat (single STP instance per switch) / per-VLAN (single STP instance per VLAN) (By default on OmniSwitch) … STP (802.1d): Convergence time: 50 secs / RSTP (802.1w): < 1 sec / MSTP (802.1s): < 1 sec"
- 提取内容：OmniSwitch 默认 per-VLAN 模式；协议收敛 50s vs <1s。

## P26. STP 默认路径开销（16bit/32bit）
- 页码：<<<PAGE 239>>>
- 原文摘录："10 Mbps 100/2,000,000 … 1 Gbps 4/20,000 … 10 Gbps 2/2,000"（16bit 用于 STP/RSTP，32bit 用于 MSTP）
- 提取内容：两种开销体系随协议自动切换（`spantree path-cost-mode auto`，<<<PAGE 247>>>）。

## P27. per-VLAN STP 负载分担手法
- 页码：<<<PAGE 240>>>
- 原文摘录："per vlan (1x1) - load balancing … spantree vlan 20 priority 20000" 后 VLAN 20 根桥迁移到 SW-C
- 提取内容：按 VLAN 调 bridge priority 可让不同 VLAN 的阻塞端口错开，实现环路链路负载分担。

## P28. LACP 动态聚合协商原理
- 页码：<<<PAGE 252>>>
- 原文摘录："Dynamic: IEEE 802.3ad LACP. LACP will negotiate the optimal parameters for both ends using LACPDU … It also works between two different devices"；"Static: Only works between Alcatel-Lucent OmniSwitches"
- 提取内容：静态聚合仅限 ALE 互通；LACP 跨厂商、经 LACPDU 协商最优参数。

## P29. 哈希负载均衡算法 brief/extended
- 页码：<<<PAGE 259>>>
- 原文摘录："Brief Mode: UDP/TCP ports not included … Extended: UDP/TCP ports to be included in the hashing algorithm. Result in more efficient load balancing"；各机型默认值表（6360/6465/6900=brief，其余=extended）
- 提取内容：`hash-control extended` 引入四层端口提高分担均匀度。

## P30. 聚合口组播分担默认行为
- 页码：<<<PAGE 260>>>
- 原文摘录："Multicast traffic is by default forwarded through the primary port of the Link Aggregation Group … enable hashing for non-unicast traffic"
- 提取内容：组播默认走主端口，需显式开启 non-ucast 哈希才全组分担。

## P31. Wi-Fi 6 核心改进
- 页码：<<<PAGE 43>>>
- 原文摘录："Increased network throughput / Increased efficiency in dense environments / Increased robustness outdoors / Reduced power consumption / Enhanced Wi-Fi coexistence / Reduced overhead"
- 提取内容：Wi-Fi 6 面向高密与 IoT 场景的六项改进。

## P32. Wi-Fi 7 关键新技术
- 页码：<<<PAGE 44>>>
- 原文摘录："Multi Link Operation (MLO) … 4096-QAM … 320 MHz … Multi Resource Unit (MRU) … Preamble Puncturing … Automated Frequency Coordination (AFC)"
- 提取内容：MLO、4096-QAM、320MHz 信道等 Wi-Fi 7 特性清单（46 Gbps vs Wi-Fi 6E 9.6 Gbps）。

## P33. Stellar AP 出厂默认行为
- 页码：<<<PAGE 199>>>
- 原文摘录："BROADCASTS A SSID 'MYWIFI-ABCD' WITH ABCD = LAST BYTES OF THE AP MAC@ / HAS THE IP@ = 192.168.1.254 (OR AN IP@ RECEIVED FROM THE DHCP SERVER)"；Web 管理口 `HTTP://<IP@ OF THE AP>:8080`
- 提取内容：开箱即广播 mywifi-XXXX（MAC 后四位），默认管理 IP 192.168.1.254，端口 8080。

## P34. AP Group 自动成组条件与默认 Group ID
- 页码：<<<PAGE 202>>>
- 原文摘录："OmniAccess Stellar Access Points with the same group identifier (Group ID) and the same VLAN are automatically placed in the same group … Initial Settings: Identical Group ID (Group ID 100), Identical default VLAN (VLAN 1)"
- 提取内容：同 Group ID + 同 VLAN = 自动成组；出厂 Group ID 100。

## P35. PVM/SVM 角色与选举
- 页码：<<<PAGE 203>>>
- 原文摘录："a Stellar AP is elected PVM (Primary Virtual Controller). The PVM manages all the Group … SVM (Secondary Virtual Manager) to replace the PVM in case of failure … Criteria 1: highest Stellar AP model / Criteria 2: highest MAC address"
- 提取内容：主备虚拟控制器双准则选举，统一 Web 界面挂在 PVM 上。

## P36. SSID→VLAN 自动映射
- 页码：<<<PAGE 215>>>
- 原文摘录："A predefined VLAN is automatically assigned to a client when it connects to an SSID"
- 提取内容：客户端按接入 SSID 自动落入预定义 VLAN（Employees→VLAN10、Guests→VLAN20 的示例）。

## P37. AP 内置 DHCP/DNS/NAT 服务
- 页码：<<<PAGE 216>>>
- 原文摘录："DHCP, DNS & NAT services integrated in all the OmniAccess Stellar Access Points"
- 提取内容：无控制器架构下 AP 自带三件套基础网络服务。

## P38. AP 内置 QoS/ACL 与三角色用例
- 页码：<<<PAGE 217>>>
- 原文摘录："Employees VLAN 10, Access: All, Bandwidth: High, Priority: Normal / Guests VLAN 20, Access: internet only, Bandwidth: Normal, Priority: Low / Phones VLAN 30, Access: Voice, Bandwidth: Low, Priority: High"
- 提取内容：按用户类型（员工/访客/话机）做 VLAN+带宽+优先级三维差异化策略。

## P39. 访客 Captive Portal 三种认证方式
- 页码：<<<PAGE 226>>>
- 原文摘录："the authentication type must be selected (account, access code, or terms of use)"；"The username and password fields are case sensitive"
- 提取内容：账号 / 接入码 / 使用条款三选一；账号字段区分大小写，可设有效期。

## P40. UPAM 统一策略认证模块定位
- 页码：<<<PAGE 367>>>（另见 <<<PAGE 188>>>、<<<PAGE 392>>>）
- 原文摘录："THE UPAM MODULE (UNIFIED POLICY AUTHENTICATION MANAGER) PROVIDES A CENTRALIZED MANAGEMENT OF THE ACCESS RULES. THE UPAM ALSO EMBEDS A RADIUS SERVER AND A CAPTIVE PORTAL."
- 提取内容：OV Cirrus 内嵌的统一接入管理平台，同时充当 RADIUS 服务器与 Captive Portal，覆盖 MAC/802.1X/Portal 三类认证。

## P41. ARP（Access Role Profile）属性构成
- 页码：<<<PAGE 376>>>
- 原文摘录："ARP = Access Role Profile: VLAN TAG / QOS POLICY / FIREWALL RULES (ACLS) / L7 APPLICATION RULES / LOCATION / PERIOD"
- 提取内容：六元组用户策略档案（VLAN、QoS、防火墙、L7 应用、位置、时段）。

## P42. Stellar AP LED 状态语义
- 页码：<<<PAGE 52>>>
- 原文摘录："Green blinking: System started up, Default SSID broadcasted / Blue: Dual band 2.4 GHz AND 5 GHz / Blue & Red blinking: Software Update / Blue/Red/Green blinking: AP Localization / Red: System startup"
- 提取内容：LED 颜色/闪烁模式与 AP 运行状态对照（AP136x 独立 LED 表见 <<<PAGE 54>>>）。

## P43. 交换机面板 OK/PWR LED 语义
- 页码：<<<PAGE 50>>>
- 原文摘录："OK1 Green: System Diagnostic & Startup OK / Blinking Green: pending / Amber: NOK / PWR Green: Power supply OK / Blinking Green: power supply present, but malfunction"
- 提取内容：启动自检与电源状态的双 LED 判读法。

## P44. PoE 端口 LED 判读
- 页码：<<<PAGE 143>>>
- 原文摘录："Amber: Device connected, Device powered with PoE / Green: Device connected, Device not powered with PoE"
- 提取内容：琥珀=受电、绿色=连接但未受电。

## P45. OV Cirrus 网络前提（端口/DHCP 选项/版本）
- 页码：<<<PAGE 290>>>
- 原文摘录："Open Firewall ports 9093, 30123, 30124, 30125 … outbound 443, 80, 123, 53 … Enable DHCP standard options: 1, 2, 6, 28, 42, 43 … when using proxy: 129, 130, 131, 132, 133, 138 … All Stellar models supported, except: AP1101, AP1201L/H/HL … AWOS 4.0.6 GA or higher … AOS 8.9R1 or higher"
- 提取内容：上云的防火墙、DHCP option、软件版本三类前置条件。

## P46. cloud-agent 呼叫机制与激活状态机
- 页码：<<<PAGE 314>>>、<<<PAGE 309>>>–<<<PAGE 310>>>
- 原文摘录："cloud-agent discovery-interval: the time interval after which the switch will call-home the activation server, in case of any error (default= 30mns)"；激活状态流 "Registered > Obtaining Certificate > Assigned > VPN Configuring > Connected to OV > Provisioning > OV Managed"
- 提取内容：设备周期性 call-home；状态机含中间态与失败态（Failed To Get Certificate / Factory Reset Required 等）。

## P47. 分布式控制架构（空口 + 局域网交换）
- 页码：<<<PAGE 280>>>
- 原文摘录："Over the Air Exchange: Roaming client's context, MAC addresses, Keys, Access Role Profiles / Over the LAN Exchange: Radio Frequency settings, Power, Channel, RSSI"
- 提取内容：无控制器下 AP 间通过空口同步漫游上下文、通过 LAN 同步 RF 参数。

## P48. AP Group（Cirrus 版）配置继承模型
- 页码：<<<PAGE 277>>>、<<<PAGE 329>>>、<<<PAGE 331>>>
- 原文摘录："AP(s) inherits the AP Group configuration … SSIDS, FIREWALL POLICY, AUTHENTICATION POLICY, RADIOFREQUENCY POLICY"；"Mandatory Provisioning Configuration: Name, Site, RF Profile, Timezone"
- 提取内容：AP→AP Group→Provisioning Configuration 三层继承；组内可混插任意 AP 型号、上限 10000。

## P49. Walled Garden 特性
- 页码：<<<PAGE 235>>>、<<<PAGE 410>>>
- 原文摘录："provides the visitor / guest with the ability to access certain predefined websites even before authenticating (eg. Access to the hotel website possible even if the guest has not authenticated)"
- 提取内容：认证前白名单放行指定站点的访客预访问机制。

## P50. AP 外置天线命名规则
- 页码：<<<PAGE 41>>>
- 原文摘录："Access points compatible with external antennas have their reference ends with '2' (ex. AP1322, AP1362) … All OmniAccess Stellar Access Points are equipped with an internal antenna (omni-directional coverage pattern)"
- 提取内容：型号尾数 2 = 支持外置天线；其余均为内置全向天线。
