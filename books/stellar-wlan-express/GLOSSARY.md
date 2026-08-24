# 术语词典 GLOSSARY

| 术语 | 全称 | 出处 | 定义 |
|---|---|---|---|
| **Express Mode** | Express 模式（免云管自管模式） | p40-41 | \| Stellar AP 的三种部署模式之一，本书主题：无控制器、无网管云平台，AP 自组织为 standalone cluster（独立集群），通过内置安全 Web 界面做向导式配置。上限 255 台（混合型号集群），内置客户门户、内置用户数据库、内置 DHCP/DNS/NAT、无线 Mesh、WIPS、证书管理、多语言 GUI（含简体中文），支持 OXO Connect R2.1 ZTP 与远程集群管理。适用于 SMB/小微项目。 |
| **Enterprise Mode** | 企业模式 | p42-43 | \| 三种部署模式之二：接入 OmniVista 2500 网管（NMS）做集中管理，上限 4000 台 AP 分布于不限数量的 AP Group。获得 UPAM 统一策略认证、Unified Access NAC、DPI、UPnP/Bonjour 服务共享、MACsec、热图/报表等网管级能力。 |
| **Cloud Mode** | 云管理模式 | p44-45 | \| 三种部署模式之三：接入 OmniVista Cirrus 云平台集中管理，上限同为 4000 台。教材明确 Cirrus 的功能与 OmniVista 2500 基本等同（similar features as OmniVista 2500），差别只在云端与本地部署形态。 |
| **PVM** | Primary Virtual Manager（主虚拟管理器） | p79-80 | \| AP Group 中承担集中管理角色的那台 AP：组内所有其他 AP（Member）都归它管，配置、维护、集群动作都面向 PVM 执行。由自动选举产生，判据为先比 AP 型号等级（Highest Model Type）再比 MAC 地址（Highest MAC）。PVM 产生后广播用于组配置的 SSID（如 mywifi-0102）。 |
| **SVM** | Secondary Virtual Manager（备虚拟管理器） | p79-80 | \| 集群中负责"救援"集中管理角色的备用管理 AP：MAC 地址第二高的 AP 自动当选。PVM 失效时由 SVM 接管管理职能，避免单点故障导致整组失管。 |
| **Member** | 成员 AP | p79 | \| AP Group 中除 PVM 之外、接受 PVM 管理的全部 AP。成员并非纯被管：p84 指出成员各自承担数据面管理、认证管理、本地 ACL 管理等本地职责，并通过 WLAN 邻接参与射频协调。 |
| **AP Group / Group ID** | AP 组/组标识 | p79, p81 | \| 若干 AP 通过 LAN 以"overlay"（覆盖）方式连接、无需改造基础架构所形成的管理组，用 Group ID 标识；ID 相同的 AP 归同一个 PVM 管理。扩容设计采用"VLAN X → Group ID X"映射，一组上限 255 台；组间无 L2/L3 漫游。 |
| **mywifi** | 出厂默认 SSID | p46, p60 | \| Stellar AP 出厂广播的默认无线网络名（教材图示为 MYWIFI:ABCD 形式）。首次配置流程（f03）中终端先连 mywifi，再进入 AP 的 Web 界面完成向导配置。PVM 当选后也会发一个用于 AP-Group 配置的 SSID（如 mywifi-0102）。 |
| **Group Mgt IP** | 组管理 IP | p84, p86 | \| 集群对外的单一 IP 管理接口，承载配置同步、组管理界面与通知。远程集群管理即通过在防火墙上放行该 IP 实现（get/set 模式），除 AP Group 镜像升级外所有操作支持远程。 |
| **Captive Portal** | 强制网络门户（内置客户门户） | p93 | \| Express 模式内置的访客认证门户：客户端连上开放 SSID 后 HTTP 请求被重定向到门户页，凭账号密码或访问码认证后放行。注意两个行为边界：https 请求不做重定向（ce06）；命中 MAC 白名单或 walled garden 的客户端直接放行不弹页（ce07）。认证模块进程为 EAG（g29）。 |
| **Walled Garden** | 围墙花园 | p143 | \| 内置 Portal 的免认证访问清单：客户端 IP 在清单内的目标地址可以不经认证直接访问，因此这些客户端不会被重定向到门户页。排障"Portal 不弹页"时必须核对该清单；也可主动用它为打印机/哑设备开通道。 |
| **内置 DHCP/DNS/NAT 服务** | Built-in DHCP/DNS/NAT | p92 | \| Express 模式下 AP 本地自带的三件网络服务（Built-In Services 模块），可在 Web 界面启用管理，让无任何外部基础设施的小微环境也能直接放号、解析与出网。同模块还包括防火墙规则（Firewall Rules）配置。 |
| **DRM** | Dynamic Radio Management（动态射频管理） | p98 | \| Radio Settings 模块的首项功能：AP 自动管理自身射频（信道/功率）的机制，与 DFS 动态选频、TPC 发射功率控制（p41）同属射频自动化能力，也可按需改为信道与功率手工指定。 |
| **Client Behavior Tracking / Sticky Client Avoidance** | 客户端行为跟踪/黏性客户端规避 | p99-100 | \| 射频设置中的两项客户端体验功能：前者跟踪客户端行为，后者解决"黏性客户端"问题——终端死守信号已差的远端 AP 不漫游。规避手段让 AP 引导此类客户端切换到更近的 AP；勘测纠正措施里的"删除低速率"（p22）也是同一思路的强制版。 |
| **Smart Air Share** | 智能空口共享 | p101 | \| Radio Settings 模块列出的射频优化功能之一，用于空口时间/资源的智能分配调度，与 DRM、客户端跟踪、黏性规避、Rogue AP 检测、后台扫描、频段引导、负载均衡并列（p97 目标清单）。 |
| **Rogue AP** | 流讯 AP（非法接入点） | p102 | \| 未经授权私接入网、或仿冒合法网络的 AP。Radio Settings 模块含 Rogue AP 检测；配合 p41 的 WIPS 防护（无线入侵防护）可检测并遏制。Express 依赖 AP 内置能力实现，无需外置网管。 |
| **Background Scanning** | 后台扫描 | p103 | \| 射频设置功能之一：AP 周期性在后台扫描各频段，收集射频环境数据（用于 DRM、Rogue 检测等），与 Band Steering、Load Balancing 同页列出。硬件上多数 Stellar 型号还配有专用扫描射频（1 full band dedicated to radio scanning，见 p23 硬件规格）。 |
| **Band Steering** | 频段引导 | p103 | \| 射频优化功能：把支持 5GHz（双频）的客户端引导到 5GHz 频段，为只支持 2.4GHz 的老设备腾空口。与后台扫描、负载均衡同属 Radio Settings 的常规开关项。 |
| **Load Balancing** | 负载均衡 | p103 | \| 射频优化功能：按客户端数量/负载把终端分流到不同 AP 或频段，避免个别 AP 过载。与 MaxClients（ce14）配合构成容量管理两面：均衡管分布，MaxClients 管上限。 |
| **WiFi Bridge** | 无线网桥 | p112-113 | \| 两台 AP 间的点对点无线回程链路，用于替代跨街楼宇等无法布线的场景。四属性（SSID/Band/Is Root/Passphrase）中三项须双方一致、根只能一个；链路可用 VLAN 分离加固流量（AP1101/1201/1201H 除外，见 ce03）；纯回程、不为客户端提供 WiFi 服务（ce04）。 |
| **WiFi Mesh** | 无线网状网 | p112, p114 | \| 多台 AP 组成的自组织无线回程+覆盖网络：允许多根（Multiple roots），节点在回程之外同时广播 SSID 服务客户端，VLAN 按 SSID 分离客户端流量。硬上限：4 跳、单跳 5 台、全网 16 台、每节点 5 个客户端 SSID（ce05）。典型场景：营地整场覆盖。 |
| **Auto Mesh** | 自动 Mesh | p115 | \| Mesh 的零配置快速部署形态：接 LAN 的 AP 配成 Mesh root 后自动广播隐藏 SSID "Stellar-MESH"（5GHz）；任何未接 LAN 的 Stellar AP 上电即自动以非根身份入网。只需配置根节点即可完成整网部署。 |
| **Root AP** | 根 AP（回程根节点） | p113-114 | \| Bridge/Mesh 拓扑中回程的锚点节点（Is Root=Yes），通常是接 LAN、拥有出口的那台。Bridge 必须且只能有一个根；Mesh 可以有多个根形成多出口回程。根节点配置错误（双根或无根）是桥接/组网失败的常见原因。 |
| **UPAM** | Unified Policy Authentication Manager（统一策略认证管理器） | p43 | \| OmniVista 集成的认证与策略组件（Enterprise/Cloud 模式特性）：员工 Supplicant/非 Supplicant 安全认证、访客自助注册/员工担保/社交登录、BYOD、基于策略的强制执行、门户深度定制与外部门户支持。Express 模式不含 UPAM，对应能力由内置用户数据库+内置/外部门户替代。 |
| **OmniVista 2500 / OmniVista Cirrus** | OV2500 网管 / Cirrus 云管 | p42, p44 | \| Stellar 的两个集中管理平台：OV2500 为本地部署网管（NMS），Cirrus 为云平台，两者功能基本等同，各管 4000 台 AP。Express 模式不依赖它们——这正是本课"免云管交付"的前提。 |
| **BLE / ZigBee 集成射频** | 蓝牙低功耗/ZigBee 物联网射频 | p13-25 | \| Stellar 多数型号（AP1311/1320/1331/1351/1360/1411/1431/1451/1511/1521 等）内置的 IoT 无线电（BLE 5.1 与 ZigBee），为物联网接入、定位分析等提供框架（p33）；老款 AP1230 为 BLE。选型带 IoT 需求时核对该项。 |
| **PoE Injector / Midspan** | PoE 供电器（中间跨接器） | p28 | \| 当上联交换机不支持 PoE 时，串接在网线上为 AP 注入电力的设备（也叫 midspan 或 PoE adapter）。与之并列的还有电源适配器（Power Adapter，插座取电）。各 AP 兼容的型号清单在对应 datasheet 里查。 |
| **Site Survey** | 无线勘测（被动/主动/预测三型） | p164-165 | \| 分析射频环境、发现干扰、选定 AP 位置的手段，分三型：Passive（只听不关联，测信号/噪声/发现 AP）、Active（关联 AP，加测丢包/重传/物理速率）、Predictive（软件仿真建模，无现场实测）。按项目阶段选型：部署前预测、部署后被动看射频、主动看客户端性能。工具：Ekahau（Windows）、WiFi Analyzer（Android）。 |
| **EAG** | 门户重定向/认证进程 | p143, p152 | \| AP 内负责 Captive Portal 重定向与认证的进程/模块。Portal 不弹页排障的最后一查是 ps \| grep eag 确认其存活；认证失败排障用 cat /proc/kes_syslog \| grep eag 或 cat /var/log/eag.log 调试。 |
| **ACS** | 自动信道选择（Automatic Channel Selection） | p155 | \| 低吞吐排障五查之一："Is the ACS function enabled? If not, enable it."——AP 自动择优信道的开关功能，关闭后信道固定，环境变化时易陷入干扰信道。性能投诉时确认 ACS 开启是标准动作。 |
| **RSSI** | Received Signal Strength Indicator（接收信号强度指示） | p168 | \| 衡量接收信号强度的指标（教材以 dBm 表述）。本书给出的实践基准：4 米穿 1-4 堵墙后 RSSI=-70dBm，已不足以支撑 VoWLAN（无线语音）。勘测中用于判定覆盖是否达标、定位弱覆盖区。 |
| **Co-channel / Adjacent Channel Interference** | 同频干扰/邻频干扰 | p170 | \| 两类信道规划类干扰：同频干扰为多 AP 工作在同一信道竞争空口；邻频干扰为相邻信道部分重叠。症状：吞吐下降、丢包、数据损坏。统一对策是给受影响 AP 换信道（设计期错开信道、收窄带宽）。 |
| **ZTP** | Zero Touch Provisioning（零接触开通） | p41 | \| Express 特性清单中的自动开通能力：OXO Connect R2.1 通过安全 HTTPS 与 Stellar ZTP 集成，设备上电后自动获得配置，免手工初始化。与 OXO 电话系统配套场景使用。 |
| **lighttpd / wam / athstats / sfe** | AP 内部进程与诊断命令族 | p133-134, p150, p154, p158 | \| Console 排障命令族：lighttpd=Web 服务进程（Web 打不开时 ps \| grep lighttpd，用 /etc/init.d/lighttpd start 重建）；wam=无线接入管理进程（客户端连不上时按 athXX 端口查/重建）；athstats -i wifi0/1=查 PHY 错误；wlanconfig athXX list=查连接帧与信号；sfe=跟踪无线客户端会话（输出 Src ip:Sport -> dest ip:Dport、协议、方向 O/R、包数字节数）。 |
| **VoWLAN** | Voice over WLAN（无线语音） | p168 | \| 走无线网络的语音业务，对信号质量要求高于普通数据。教材基准：RSSI -70dBm 不够 VoWLAN 使用；语音级覆盖设计与验收以此为门槛之一。 |
| **GuestOperator** | 访客操作员受限角色 | p41 | \| Express Web 界面的受限管理角色：仅供运营访客门户的人员使用（如前台创建访客账号），看不到全局配置。与 HTTPS 访问、多语言支持并列于 Express 管理能力清单。 |