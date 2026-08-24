# ACFE WLAN - Basic Deployment With OmniVista (Ed04) · 关键概念词典
# 来源: fulltext.md（585 页全书），55 条，按字母排序，source_chapter 为首次/最佳定义页码

```yaml
- id: g01
  term: 802.1X
  full: IEEE 802.1X Port-Based Network Access Control
  source_chapter: "p310"
  definition: |
    基于 IEEE 802.1X 的企业级认证（WPA/WPA2/WPA3 Enterprise），客户端经 RADIUS 服务器校验用户名密码或证书后才获得密钥，安全级别高于 PSK 和 MAC 认证。员工 SSID 的标准做法：认证源指向内置 UPAMRadiusServer 或外部 RADIUS，本地库建 Employee 账号。交付时客户端配置 PEAP/MSCHAPv2 即可接入，排障用 AP 上 cat AAA_server.conf 确认 RADIUS 参数已下发。

- id: g02
  term: 802.11k
  full: Radio Resource Measurement (Neighbor Report)
  source_chapter: "p480"
  definition: |
    无线资源测量修正案，客户端可向 AP 索取一份优化的邻居 AP 信道清单，避免全频段盲扫，更快找到漫游目标。与 Roaming RSSI 阈值、802.11v 组合使用，共同解决"粘客户端"问题。交付时在语音、移动办公场景与 802.11r/v 一起规划开启。

- id: g03
  term: 802.11r
  full: Fast BSS Transition (FT)
  source_chapter: "p478"
  definition: |
    快速漫游标准，利用 FT PMK R0/R1 密钥缓存优化认证握手、去掉重复 RADIUS 认证，显著缩短跨 AP 切换时间。仅支持 WPA2/WPA3 加密（Personal 或 Enterprise），按 SSID 开启。交付时对 IP 语音、移动查房等时延敏感业务必开，验收要测跨 AP 通话不断线。

- id: g04
  term: 802.11v
  full: BSS Transition Management
  source_chapter: "p480"
  definition: |
    BSS 过渡管理，AP 主动向客户端建议更优的目标 AP，配合 802.11k 的邻居清单引导客户端离开弱信号 AP，是 Sticky Client Avoidance（粘客户端规避）的核心协议。交付时在高层办公/高密度场景与 Roaming RSSI 阈值（RF Profile 内配置）联动开启。

- id: g05
  term: Access Role Profile
  full: Access Role Profile (ARP)
  source_chapter: "p315"
  definition: |
    访问角色档案，把 VLAN 映射、QoS、带宽、Policy List 打包成一个"角色"，用户通过 MAC/802.1X/Portal 任一方式认证后被指派角色并继承全部网络权限。BYOD 的 Post Portal Enforcement 本质就是认证后换一个 ARP。交付时按"员工/访客/BYOD/承包商"规划角色矩阵，后续调权限只需改 ARP 一处。

- id: g06
  term: Active Survey
  full: Active Site Survey
  source_chapter: "p529"
  definition: |
    主动勘测，勘测终端真实关联到 AP，除信号强度与噪声外还能测丢包、重传、实际物理速率。用于部署后的客户端性能分析与故障定位。交付验收时在关键点位做主动勘测，拿丢包/重传统计作为验收证据。

- id: g07
  term: AP Group
  full: Access Point Group
  source_chapter: "p270"
  definition: |
    接入点组，组内 AP 共享同一套配置（SSID 指派、RF Profile、模板），与物理网络位置无关，可混插任意型号，Cloud 模式下单组上限 2000 台（Express 集群 255 台）。SSID 创建后按组绑定才生效。交付时按楼宇/楼层/用途分组，一次配置全组生效，扩容只需把新 AP 序列号加入组。

- id: g08
  term: Background Scanning
  full: Radio Background Scanning
  source_chapter: "p448"
  definition: |
    背景扫描，每个射频周期性逐信道监听空口（默认间隔 20 秒、时长 50 毫秒），扫描期间该射频暂停收发 802.11 数据，对客户端有轻微影响。WIPS 的 Rogue 与攻击检测依赖扫描数据。交付时开 WIPS 就必须保留扫描；语音敏感场景可开 Voice/Video Awareness 让有活跃会话的 AP 跳过扫描。

- id: g09
  term: Band Steering
  full: Band Steering
  source_chapter: "p445"
  definition: |
    频段引导，把双频客户端推向 5GHz/6GHz 以避开 2.4GHz 拥堵，可加 Force 5/6G 强制模式，默认关闭。前提是两个频段覆盖大致相同，否则会把客户端推进 5G 覆盖洞。交付时先核实双频覆盖一致再开启；覆盖差异大的站点可用 Exclude MAC OUI 排除扫描枪、MIPT 话机等老终端。

- id: g10
  term: Bandwidth Control
  full: Bandwidth Contract
  source_chapter: "p408"
  definition: |
    带宽合同，可在 SSID、Access Role Profile、Policy List（ACL/QoS 动作）三层限速：Policy List 命中的流量按规则限，其余按 ARP 用户级限，再退到 SSID 级（该 SSID 全体用户在单 AP 上共享）。访客限速、BYOD 分流都靠它落地。交付典型做法：访客 ARP 限 10Mbps、员工不限，防止访客视频挤占出口带宽。

- id: g11
  term: BYOD
  full: Bring Your Own Device
  source_chapter: "p352"
  definition: |
    员工自带设备接入：SSID 开放接入，认证前先落在受限 VLAN（如访客网），经 BYOD Captive Portal 用企业账号注册后，由 Post Portal Enforcement 换到员工角色与 VLAN。账号源可用 UPAM 本地库或外部 LDAP/AD/RADIUS。交付时验收两条路径：未注册只有受限权限，注册成功后 IP 落到员工网段。

- id: g12
  term: Call Home
  full: Device Call Home Interval
  source_chapter: "p250"
  definition: |
    设备周期性主动联系云管完成激活与状态上报：OmniSwitch 默认约 30 分钟、Stellar AP 最长约 30 分钟一次。Device Catalog 状态停在"Waiting for first contact"时，重启设备或在交换机上执行 cloud-agent admin-state restart 可立即触发。交付开局用它加速激活，卡住时先看 Activation Log 定位原因。

- id: g13
  term: Captive Portal
  full: Captive Portal
  source_chapter: "p138"
  definition: |
    强制门户，客户端连上开放 SSID 后访问任意非 HTTPS 页面即被重定向到认证页，支持账号密码、访问码、条款确认、自助注册、社交登录等方式。AP 内置简易版（Express），Cirrus 的 UPAM 提供可定制模板（Logo、背景、登录按钮）。交付时给前台开 Guest Operator 账号代发访客凭证，模板替换成客户品牌元素。

- id: g14
  term: Client Context Sharing
  full: Client Context Sharing
  source_chapter: "p472"
  definition: |
    客户端上下文共享：AP 通过空中发现协议学习邻居 AP 及其 IP，客户端关联/去关联时用 Add/Del 消息经 LAN 同步上下文（VLAN、角色、Policy List、Portal 状态、PMKSA/FT 密钥缓存），是 L2/L3 漫游的基础。作用域限于同一 OmniVista 管理且具备相同 WLAN 服务的 AP。交付时注意被墙体隔断的"地理相邻、射频不通"AP 需手工互加 Neighbor AP，否则无法漫游。

- id: g15
  term: Cloud Mode
  full: Wi-Fi Cloud Mode (OmniVista Cirrus Managed)
  source_chapter: "p27"
  definition: |
    三种部署模式之一：AP 由 OmniVista Cirrus 云平台（SaaS）纳管，功能与 OV2500 相近，平台可管约 1 万 AP + 2 千交换机，零本地部署。设备经激活服务器加 VPN 注册到组织。交付前置检查：防火墙放行 9093/30123-30125 端口与出向 443/80/123/53，DNS/NTP 可用，License 订阅已导入组织。

- id: g16
  term: DHCP Option 138
  full: DHCP Option 138 (CAPWAP/WLAN Management Address)
  source_chapter: "p17"
  definition: |
    DHCP 选项 138，内容为 OmniVista 2500 的 IP 地址。AP 开机获取地址时，若 DHCP offer 携带 138 则转入 Enterprise 模式注册，否则保持默认 Express（再尝试用 MAC/序列号匹配 Cirrus）。交付时在 AP 管理 VLAN 的 DHCP 作用域加 option 138（isc-dhcp-server 需自定义 option 138 = ip-address），实现模式自动选择。

- id: g17
  term: D-PGPSK
  full: Dynamic Private Group PSK
  source_chapter: "p329"
  definition: |
    动态私有组 PSK：在 PSK 条目基础上同时绑定 VLAN ID 与 Access Role Profile，多条口令可复用同一 ARP 但落到不同 VLAN，省去"一 VLAN 一角色"的重复配置，需把 Device Specific PSK 设为 Prefer 并启用 Dynamic VLAN Selection。交付时按部门/外包商发不同口令自动分流到各自 VLAN，某个口令泄露只需重置对应条目。

- id: g18
  term: DRM
  full: Distributed Radio Management
  source_chapter: "p439"
  definition: |
    分布式射频管理：每个 AP 与空中邻居互通射频上下文（信道利用率、干扰、每频段客户端数、功率），自行以 try-wait-retry 机制决策信道与功率调整，不依赖 AP Group 或管理 VLAN，范围限于邻居 AP。Stellar 无控制器架构下射频自优化的核心机制。交付时把 Country Code 写进 RF Profile、给 Auto Channel Selection 留足候选信道列表即可，无须逐台手调。

- id: g19
  term: DSPSK
  full: Device Specific PSK
  source_chapter: "p326"
  definition: |
    设备专属 PSK：设备先做 MAC 认证，UPAM 在 Company Property（公司资产）库里按 MAC 返回该设备专属口令。分 Force（SSID 级不设全局口令，只认专属口令）与 Prefer（未入库设备可回落全局口令）两档，加密不能选 AUTO_WPA_WPA2。交付时给打印机、扫描仪等哑终端入库发独立口令，单台泄露不影响全网。

- id: g20
  term: Ekahau
  full: Ekahau Site Survey
  source_chapter: "p532"
  definition: |
    行业主流 Wi-Fi 勘测与设计工具（培训用 Ekahau Site Survey on Windows 演示），支持热图、覆盖分析、AP 摆位模拟与问题定位（穿墙衰减、同频/邻频干扰）。本书勘测 Lab 基于它操作。交付时用它做预测设计出物料清单，竣工后做被动勘测对比验证覆盖。

- id: g21
  term: Employee SSID
  full: Employee SSID (Enterprise Network for Employees)
  source_chapter: "p320"
  definition: |
    员工 SSID，典型配置：WPA2/WPA3 Enterprise（802.1X）+ UPAMRadiusServer 认证 + VLAN 映射到员工网，加密选 WPA2_AES、频段 2.4/5/6GHz。Cirrus 建 SSID 时 Usage 选"Enterprise Network for Employees"会自动带出认证策略与角色模板。交付顺序：先建 VLAN 与 IP 接口，再建 SSID 并绑定 AP Group，最后用测试账号验证 IP 落在员工网段（DHCP 范围）。

- id: g22
  term: Enterprise Mode
  full: Wi-Fi Enterprise Mode (OmniVista 2500 Managed)
  source_chapter: "p89"
  definition: |
    三种部署模式之一：本地部署 OmniVista 2500 统一管理，最多 4000 AP，含 UPAM、Guest/BYOD、wIDS/wIPS、热图与报表，控制器无关（Controller-less）架构。适合数据不出企业、低时延或监管场景。交付时用 DHCP Option 138 引导 AP 注册；Express 转 Enterprise 可在 Web 界面点 Convert 或恢复出厂。

- id: g23
  term: Express Mode
  full: Wi-Fi Express Mode (Standalone Cluster)
  source_chapter: "p87"
  definition: |
    出厂默认模式：AP 自组独立集群（最多 255 台），无需 License 与网管服务器，向导式配置、内置访客门户、集成 DHCP/DNS/NAT 与 WIPS。适合 SOHO/SMB。交付时连接默认 SSID mywifi-XXXX（MAC 后四位）或访问 http://AP地址:8080 进入统一 Web 管理界面；迁移到 OV 模式后集群配置不保留。

- id: g24
  term: Friendly AP
  full: Friendly Access Point
  source_chapter: "p514"
  definition: |
    友好 AP：手工标记或命中 Friendly OUI 列表（默认含 ALE OUI，可追加）的相邻 AP，永远不被判定为 Rogue。常用于邻居单位、自家其他管理域的 AP。交付时把确定无害的邻居 AP 加入 Friendly 名单，避免误围堵殃及周边网络。

- id: g25
  term: Guest SSID
  full: Guest SSID (Guest Network with Captive Portal)
  source_chapter: "p360"
  definition: |
    访客 SSID：开放接入（或 MAC/PSK）+ Captive Portal 认证，凭证放 UPAM 本地库，可由 Guest Operator 代建或自助注册，VLAN 落访客网。Cirrus 创建时 Usage 选"Guest Network"自动生成模板与 Guest Access Strategy。交付时配好登录方式、过期时间与 Post Portal Enforcement 限权，绑定访客 VLAN 并测试限速生效。

- id: g26
  term: Guest Tunneling
  full: Guest Tunneling (L2 GRE per Access Role Profile)
  source_chapter: "p366"
  definition: |
    访客隧道：按 Access Role Profile 把访客流量用 L2 GRE 隧道从 AP 送到指定交换机/路由器，跨 L2/L3 网络也能集中隔离出公网，OmniSwitch 支持自动建隧道并可加 GRE 备份隧道。SSID 的 VLAN/Tunnel Mapping 里选 Tunnel 即启用。交付时多分支/多楼层场景用它统一访客出口，免掉每站点单独做访客策略。

- id: g27
  term: Interfering AP
  full: Interfering Access Point
  source_chapter: "p514"
  definition: |
    干扰 AP：空中发现的其他 AP 的默认分类（未被本 OVC 管理也未命中 Rogue 策略），同一 OVC 管理的 AP 排除在外。它是空口环境评估的输入。交付时结合勘测判断是否需要调信道或加 Friendly 标记，必要时升级 Rogue 策略。

- id: g28
  term: L2 Roaming
  full: Layer 2 Roaming
  source_chapter: "p482"
  definition: |
    二层漫游：客户端在新 AP 上存在上下文、WLAN 服务与角色一致、且 VLAN 映射一致时直接切换，始终处于初始 VLAN，默认开启无需配置。适用于同一管理域、同 VLAN 的园区移动。交付时保证漫游区域 SSID/角色/VLAN 映射一致，并用热图核实 AP 覆盖有重叠。

- id: g29
  term: L3 Roaming
  full: Layer 3 Roaming (L2 GRE between Home and Foreign AP)
  source_chapter: "p485"
  definition: |
    三层漫游：新 AP（foreign）的 VLAN 与家 AP（home）不同时，通过两 AP 间的 L2 GRE 隧道把客户端流量送回家 VLAN，保持 IP 不变业务不断。默认关闭，需在 SSID 配置中开启。跨 AP Group/跨 VLAN 的移动办公场景交付时开启并实测连通性与时延。

- id: g30
  term: MSP
  full: Managed Services Provider
  source_chapter: "p196"
  definition: |
    托管服务商：Cirrus 中 MSP 层用户可创建/编辑/删除多个客户 Organization，并邀请组织级用户，权限分 Admin/Viewer/Limited。Partner 账号默认是 MSP 级用户，一个邮箱账号在 OVC 10.4.3 后只能归属一个 MSP 门户（可用邮箱子地址扩展）。交付多客户项目时用 MSP 门户统一运维，客户各自只看到自己的组织。

- id: g31
  term: OKC
  full: Opportunistic Key Caching
  source_chapter: "p478"
  definition: |
    机会式密钥缓存：客户端漫游到新 AP 时复用缓存的 PMKSA 快速完成四次握手，免去完整 RADIUS 认证，属于 Fast Roaming 手段之一。仅 WPA2/WPA3 Enterprise 可用，按 SSID 开启。交付时与 802.11r 二选一或组合，语音终端场景先验证终端兼容性。

- id: g32
  term: OmniVista 2500
  full: OmniVista 2500 NMS
  source_chapter: "p15"
  definition: |
    ALE 本地有线无线统一网管：Enterprise 模式的管理平面，管理 Stellar AP 与 OmniSwitch，内置 UPAM、Guest/BYOD、wIDS/wIPS、热图与高可用。RAP 场景与 Cirrus 分工配合：Cirrus 负责注册与 VPN 指引，OV2500 负责向远程 AP 下发 SSID/射频配置。交付时以虚拟机形态部署，配好 IP/网关/路由即可纳管。

- id: g33
  term: OmniVista Cirrus
  full: OmniVista Cirrus (Cloud NMS)
  source_chapter: "p163"
  definition: |
    ALE 云管平台（SaaS）：统一管理 Stellar AP 与 OmniSwitch，提供 Onboarding、SSID/策略、WIPS、分析与报表，分区域门户（如 eu.manage.ovcirrus.com）。设备经激活服务器取证书、建 VPN 后注册到组织，License 订阅挂在组织上。本书 Day1 后半至 Day2 的全部实操都基于它展开。

- id: g34
  term: Onboarding
  full: Device Onboarding
  source_chapter: "p281"
  definition: |
    设备上线纳管流程：Device Catalog 声明序列号 → 设备 Call Home → 取证书 → 建 VPN → Provisioning 下发配置，状态从 Waiting for first contact 走到 OV Managed。AP 纳管的三种方式：手工分类（端口手配管理 VLAN）、UNP（LLDP 自动分类进 defaultWLANProfile）、XLSX/CSV 批量导入。交付时大项目用模板批量导入，卡住按 Activation Status/Log 逐步定位。

- id: g35
  term: Organization
  full: Cirrus Organization
  source_chapter: "p199"
  definition: |
    Cirrus 的租户单位：一个组织对应一个企业/实体，内含多个站点与网络设备，License 订阅挂在组织级，可建可删、可在 MSP 间迁移。Partner（MSP）账号跨组织管理，Customer 账号可邀请 Partner 协作。交付时给客户建独立组织，先申请 Trial 试用期再转正式订阅（eBuy 下单 → Subscription Manager 建订阅 → 组织导入）。

- id: g36
  term: Passive Survey
  full: Passive Site Survey
  source_chapter: "p529"
  definition: |
    被动勘测：勘测网卡只监听不关联，扫全频段，测信号强度、噪声并发现周边 AP，用于部署后的 RF 环境分析与覆盖验证。培训 Lab 用 Ekahau 做被动勘测出热图。交付验收时逐层走测，将实测覆盖与设计图对比闭环。

- id: g37
  term: Planes of Operation
  full: Management / Control / Data Planes
  source_chapter: "p19"
  definition: |
    Stellar 三平面架构：管理平面负责配置与监控（Express 集中在 PVM、Enterprise/Cloud 集中在 OmniVista，管理流量上联口恒为 untagged）；控制平面是 AP 间空中/LAN 协议，管 RF 与漫游上下文；数据平面把无线流量在 AP 本地转以太网打 Tag 上送，纯二层、不经网管。交付排障按平面切：配置问题查管理面、漫游问题查控制面、通断问题查数据面 VLAN。

- id: g38
  term: PoE
  full: Power over Ethernet
  source_chapter: "p109"
  definition: |
    以太网供电：AP 由交换机经网线直接供电（802.3af/at/bt），OmniSwitch 默认开启，show lanpower 查端口功率与等级。交付时核对 AP 需求与交换机功率预算（AP1301 用 802.3af 即满功能，高端三射频型号需 802.3bt），非 PoE 环境加装 PoE 注入器或电源适配器。

- id: g39
  term: PPSK
  full: Private Group PSK
  source_chapter: "p328"
  definition: |
    私有组 PSK：一个 SSID 配多组口令条目，每组绑定独立的 Access Role Profile，用户输哪组口令就落到哪个角色，同时可保留全局 PSK 作兜底。"一个 SSID 服务多个外包商/部门"的交付场景用它，节省 SSID 数量又能按组隔离权限。

- id: g40
  term: Predictive Survey
  full: Predictive Site Survey
  source_chapter: "p529"
  definition: |
    预测勘测（模拟勘测）：无需到场，导入楼层平面图与材料衰减特性，工具自动建模 RF 环境并推荐 AP 位置与数量。用于部署前的规划设计。交付前用它出 AP 摆位图与物料清单支撑报价，竣工后再以被动/主动勘测闭环验证。

- id: g41
  term: Provisioning Configuration
  full: AP Group Provisioning Configuration
  source_chapter: "p273"
  definition: |
    供应配置档：挂在 AP Group 上的基础配置模板，必填名称/站点/RF Profile/时区，另含 SSH/AP Web 开关、证书、SNMP、Syslog、IoT 射频、Data VPN 等十几项，组内所有 AP 继承。RF Profile 的实际载体就在这里。交付时每个 AP Group 配一份，调射频策略直接改此处的 RF Profile 字段，删除前须先解绑自定义 RF Profile。

- id: g42
  term: PSK
  full: Pre-Shared Key
  source_chapter: "p324"
  definition: |
    预共享密钥（WPA/WPA2/WPA3 Personal）：全部用户共用一个口令，配置最简单，但一处泄露全网皆知，安全级别低于 802.1X。SSID Usage 选"Protected Network"即 PSK 模式。交付时中小客户可先用 PSK 快速上线，规模扩大后升级 DSPSK/PPSK/D-PGPSK 或 802.1X。

- id: g43
  term: PVM
  full: Primary Virtual Manager
  source_chapter: "p10"
  definition: |
    主虚拟管理器：Express 模式下 AP Group 中当选的中央管理 AP，选举规则为先比 AP 型号高低、再比 MAC 大小，整组的配置、监控、升级都从 PVM 的统一 Web 界面完成。SVM 为第二顺位接管者，其余 AP 为 Member。交付 Express 集群时只连 PVM 的 IP 即可管理全网；PVM 宕机由 SVM 自动顶替，无需人工干预。

- id: g44
  term: RAP
  full: Remote Access Point
  source_chapter: "p496"
  definition: |
    远程接入点：把 Stellar AP 放到门店/展台/家庭等远程点，经 ALE VPN Server 建两条隧道（管理隧道由 Cirrus 的 Mgmt VPN Settings 下发、用户数据隧道由 OV2500 的 Data VPN 配置），在远端广播企业 SSID，用户数据穿隧道回公司。交付五步：Cirrus 建 RAP 组织声明序列号 → 配管理 VPN 并导出 conf → 部署/导入 VPN Server 虚机 → OV2500 建 Data VPN 并绑 AP Group → 远端 AP 接电即注册。

- id: g45
  term: RF Profile
  full: Radio Frequency Profile
  source_chapter: "p441"
  definition: |
    射频档案：集中定义国家码、Smart Load Balance、背景扫描、各频段（2.4G/5G 高低/6G）信道与功率模式（Auto/Explicit）、信道宽度、Beacon 间隔、Short Guard Interval、MU-MIMO 等参数，挂到 Provisioning Configuration（组级）或单台 AP。交付调优主战场：改信道列表、调功率、开关 Band Steering 都在此一处生效全组，AP 侧可用 cat /tmp/config/rfprofile.conf 核对下发结果。

- id: g46
  term: Rogue AP
  full: Rogue Access Point
  source_chapter: "p515"
  definition: |
    流氓 AP：干扰 AP 命中 Rogue 策略后升级而成，策略含信号强度阈值（默认 -70dBm）、广播本网合法 SSID（Detect Valid SSID，默认开）、SSID 关键字黑名单、Rogue OUI 四类。默认启用围堵（Containment）：扫描 AP 向其客户端发去认证帧。交付时同名 SSID 检测保持开启可抓钓鱼热点，调整阈值前先评估对邻居网络的影响。

- id: g47
  term: RSSI
  full: Received Signal Strength Indicator
  source_chapter: "p453"
  definition: |
    接收信号强度指示，衡量设备间收听质量，取值 0-100 对应约 -96 至 -53 dBm，数值越大信号越好；Cirrus 显示平均值，AP CLI（wlanconfig）显示瞬时值。交付用它做门限：关联 RSSI 门限推荐 2.4G=5、5G=10，漫游门限推荐 2.4G=10、5G=15；低于约 -76dBm（RSSI 20）不宜承载音视频业务。

- id: g48
  term: Site
  full: Cirrus Site (Building / Floor)
  source_chapter: "p224"
  definition: |
    组织内的站点：含国家/时区/地理位置，下建楼栋与楼层，可导入并标定楼层平面图（缩放/旋转/对齐地图）；每台网络设备声明时必须归属一个站点。热图、勘测与设备过滤都以站点为范围。交付时按园区/楼宇建站，导入平面图并把 AP 摆到楼层上，位置类分析才有意义。

- id: g49
  term: Smart Air Share
  full: Smart Air Share
  source_chapter: "p444"
  definition: |
    SSID 级空口优化：控制各频段客户端最低接入数据速率（推荐 2.4G=12、5G=24、6G=24）与 Beacon 管理帧速率，把远距离弱速率终端挡在门外，提升整体空口吞吐。高密度场景交付调优的第一项，配合勘测结果逐频段设置。

- id: g50
  term: Smart Load Balance
  full: Smart Load Balance (SLB)
  source_chapter: "p445"
  definition: |
    智能负载均衡，含三件事：Band Steering 把双频客户端推向 5/6GHz（可 Force）、Association RSSI 门限拒绝弱信号接入并断开变弱客户端、Dynamic Load Balance 让多 AP 按各自负载竞争应答把新客户端引到最轻的 AP。配置在 RF Profile 的 Smart Load Balance 区。交付时结合 RSSI 实测调门限（低值多接入弱终端、高值吞吐更好），5G 覆盖差的区域慎用强推。

- id: g51
  term: Stellar Remote-Lab
  full: Stellar Remote Lab (R-Lab)
  source_chapter: "p69"
  definition: |
    ALE 培训远程实验室：浏览器连 https://rdp.al-mydemo.com 进入远程桌面，每个 POD 含 OS6870/6360/2360 三台交换机、AP1301/AP1321 两台 AP、DHCP 与 NAT 服务器及对应 Cirrus 组织，桌面提供各设备控制台快捷方式与 Reset_PodX 重置脚本。本书全部 Lab 在此环境完成。新人交付工程师可在其中演练从开局到验收的完整流程，POD 编号对应 SSID 命名后缀（如 Employees25）。

- id: g52
  term: SVM
  full: Secondary Virtual Manager
  source_chapter: "p10"
  definition: |
    备虚拟管理器：Express 集群里 MAC 次高（同型号时）的 AP，平时作为 Member 工作，PVM 故障时自动接管集群管理。交付时无须任何配置；理解它的存在即可解释"拔掉主管理 AP 后集群仍可管理"的现象，排障时可先用 getmode/控制台确认当前 PVM 角色。

- id: g53
  term: UPAM
  full: Unified Policy Authentication Manager
  source_chapter: "p351"
  definition: |
    统一策略认证管理器：Cirrus/OV2500 内置的准入平台，含内置 RADIUS 服务器、MAC 认证服务器、Guest/BYOD 门户与账号库（Employee/Guest/Company Property/Guest Operator），也可对接外部 RADIUS/LDAP/Azure AD。员工/访客/BYOD SSID 的认证策略统一指向 UPAMRadiusServer。交付时账号、认证策略、Portal 模板都在 Network Access > UPAM-NAC 菜单下配置，认证记录在 Access Records 里查证。

- id: g54
  term: Unified Policy
  full: Unified Policies (with Policy List)
  source_chapter: "p404"
  definition: |
    统一策略：按条件（L3 IP/子网、L4 协议端口等）匹配流量并施加动作（Accept/Drop、限速、802.1p/DSCP 标记、TCM 三色），多条策略组成 Policy List 挂到 Access Role Profile（或由 RADIUS 账号下发），双向执行。交付典型如 Block_SSH：禁访客网对核心交换机 22 端口的访问；策略建完必须回到 SSID 的 ACL/QoS 处挂上才生效。

- id: g55
  term: WIPS
  full: Wireless Intrusion Prevention System
  source_chapter: "p513"
  definition: |
    无线入侵防护：依赖具备扫描的 AP 持续监测空口，做 AP 分类（Interfering/Rogue/Friendly）、Rogue 围堵、AP/客户端攻击检测（检测级别 High/Medium/Low/Custom）与客户端黑名单（如 60 秒内认证失败 10 次自动拉黑）。全局配置作用于 OVC 管理的全部 AP。交付时开 WIPS 必须保留背景扫描，验收检查 Rogue 报表与 Top N 攻击列表，误报 AP 及时转 Friendly。
```
