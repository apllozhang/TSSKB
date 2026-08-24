# 术语表 · OmniAccess Stellar AP User Guide (AWOS 5.0.3)

> 来源：source/fulltext.md（页码即手册 PDF 页码）

- id: g01
  term: AWOS
  full: Alcatel-Lucent Enterprise Wireless OS
  source_chapter: "p1"
  definition: |
    OmniAccess Stellar AP 的固件/操作系统，本手册对应 AWOS 5.0.3 版本（2025 年 9 月，060966-00 Rev. A）。版本号还影响兼容性判断，例如 AWOS4.0.0 及之前版本的 AP 默认不允许加入组（MQTT 兼容开关控制）。

- id: g02
  term: Express 模式
  full: Wi-Fi Express Mode
  source_chapter: "p8"
  definition: |
    Stellar AP 的本地集群管理模式，即本手册覆盖的模式：AP 自组成组、通过内置 Web GUI（Dashboard）完成配置与监控。与 Enterprise 模式（由 OmniVista On-Premise 统一管理）相对，切换到 Enterprise 模式需指定 OV 服务器地址且 AP 会重启。

- id: g03
  term: AP Group / Cluster
  full: AP 群组/集群
  source_chapter: "p13"
  definition: |
    具有相同 cluster ID 且位于同一 VLAN 的一组 Stellar AP，组内基于组播通信，最多 255 台。组内自动选举 PVM 和 SVM，整组共享一份配置文件。无 OV 管理时各组独立、组间不漫游。

- id: g04
  term: PVM
  full: Primary Virtual Manager
  source_chapter: "p13"
  definition: |
    AP 组的主管理虚拟角色，由组内按机型优先级和 MAC 地址选举产生，承担配置同步、用量统计、固件升级、Portal 服务等职责；组管理 IP（GMIP）配置在 PVM 上。PVM 故障时 SVM 自动接替，成员 AP 和无线用户业务不中断。

- id: g05
  term: SVM
  full: Secondary Virtual Manager
  source_chapter: "p13"
  definition: |
    AP 组的备份管理角色，选举规则与 PVM 相同（同优先级中 MAC 次高者当选）。PVM 无响应时自动升级为 PVM；替换 PVM 硬件前也应先把 SVM 升为 PVM。

- id: g06
  term: GMIP
  full: Group Management IP
  source_chapter: "p31-32"
  definition: |
    AP 组管理虚拟 IP，默认 10.0.0.1，配置在 PVM 上。用于规避 AP 从 DHCP 动态取址导致管理地址漂移的问题，可通过 http://GMIP:8080 有线或无线访问整组管理界面；建议取 AP 所在网段的空闲 IP，并保证从管理终端可路由。

- id: g07
  term: mywifi-xxxx
  full: Pre-defined SSID
  source_chapter: "p13"
  definition: |
    AP 组默认广播的预置 SSID，xxxx 为 PVM MAC 地址的最后两个字节。连接它可访问 http://mywifi.al-enterprise.com:8080 进入初始化向导；向导完成后该 SSID 自动删除。相关域名 mywifi.al-enterprise.com 同时是内置 HTTPS 证书的固定域名。

- id: g08
  term: 初始化向导
  full: Initializing Wizard
  source_chapter: "p14-17"
  definition: |
    首次开局向导，共五步：欢迎页、修改管理员密码（默认 admin）、选国家码与时区（仅 -RW 机型）、创建新 WLAN、完成确认。向导阶段不能配 VLAN；全程需保持终端连在 mywifi-xxxx 上。

- id: g09
  term: ZTP
  full: Zero Touch Provisioning
  source_chapter: "p11"
  definition: |
    零接触开通。手册场景 2：AP 从 ALE OXO 服务器获取 IP、下载固件与配置文件，自动重启成组并生效三个 WLAN，全程无需手工逐台配置。

- id: g10
  term: OXO
  full: ALE OXO Server
  source_chapter: "p11"
  definition: |
    ALE 的 OXO 服务器，在 ZTP 场景中为 AP 分配 IP 地址并下发固件与配置文件，是 AP 组开局的上游自动化节点。

- id: g11
  term: RDA
  full: Radio Dynamic Adjustment
  source_chapter: "p40-41"
  definition: |
    ALE 的射频动态调整技术（商标 ™），根据周围无线环境自动调整工作信道与发射功率，包含 ACS（自动选信道）与 APC（自动功率控制）两个功能，默认启用。依赖后台扫描开启；手动指定信道/功率前必须关闭 ACS/APC。

- id: g12
  term: ACS
  full: Auto Channel Selection
  source_chapter: "p41"
  definition: |
    自动信道选择，RDA 的组成部分，默认开启并周期性执行。开启 Client Aware 时不为有客户端的 AP 换信道（雷达检测等高优先级事件除外）；ACS 不会选用 160MHz 信道。

- id: g13
  term: APC
  full: Auto Power Control
  source_chapter: "p41"
  definition: |
    自动功率控制，与 ACS 同属 RDA，动态调整 AP 发射功率。关闭后进入手动模式，功率按 1 dB 步进设置，且 2.4G/5G 两个频段都要分别配置。

- id: g14
  term: wIDS/wIPS
  full: Wireless Intrusion Detection/Prevention System
  source_chapter: "p42-45"
  definition: |
    无线入侵检测/防御系统。通过后台扫描发现外部未知 AP（干扰 AP 与 rogue AP），支持 AP allowlist（信任名单）、AP blocklist（仅 rogue 可入）、Suppress（向 rogue 的客户端发 DEAUTH，默认关闭）与 Dynamic blocklist（自动拉黑 ad-hoc 设备，默认关闭）。

- id: g15
  term: 干扰 AP / Rogue AP
  full: Interfering AP / Rogue AP
  source_chapter: "p42"
  definition: |
    干扰 AP 指出现在无线环境但未接入有线网络的外部 AP，仅构成潜在射频干扰、不算直接安全威胁。Rogue AP 指未经授权插入网络有线侧的外部 AP，或广播与 AP 组相同 SSID 的外部 AP，被视为安全威胁，可加入 blocklist 阻止其伪装客户端接入。

- id: g16
  term: Captive Portal
  full: 强制门户认证
  source_chapter: "p59, p92-97"
  definition: |
    开放网络上的 Web 认证机制：用户浏览任意网站时弹出 Portal 页，输入账号密码、访问码或勾选使用条款后放行。Stellar 支持内置/外部 Portal 服务器、自定义 Splash 页、Walled Garden、Portal allowlist、用户行为日志（TFTP/SFTP/Syslog，1/2/4 小时周期）。

- id: g17
  term: Walled Garden
  full: 认证前白名单园区
  source_chapter: "p54"
  definition: |
    captive portal 场景下的网络资源控制机制：把允许的域名或 IP 加入 Walled Garden 后，客户端在通过 Portal 认证之前即可访问这些资源（如酒店官网）。要放行某资源必须预先知道其 IP 或域名。

- id: g18
  term: Dynamic VLAN
  full: RADIUS 动态 VLAN 分配
  source_chapter: "p62"
  definition: |
    Enterprise WLAN 下按 RADIUS 下发属性把客户端划入不同 VLAN 的功能。Express 模式支持 RFC-2868 三属性：Tunnel-Type (IETF #64)=VLAN、Tunnel-Medium-Type (IETF #65)=802(6)、Tunnel-Private-Group-ID (IETF #81)。

- id: g19
  term: RadSec
  full: RADIUS over TLS
  source_chapter: "p62"
  definition: |
    用 TLS 隧道安全传输 RADIUS 认证与计费数据的协议。启用后 AuthPort 须改为 2083（或映射 RadSec 服务器的值）；该特性仅适用于无线客户端，且只支持主 RADIUS 服务器，不支持 secondary。

- id: g20
  term: PMF
  full: Protected Management Frames (IEEE 802.11w)
  source_chapter: "p62"
  definition: |
    管理帧保护标准，为管理帧提供机密性保护。可选 Disabled/Optional/Required 三态；WPA3 Enterprise 选 CNSA 时 PMF 强制为 Required（仅支持 PMF 的客户端可接入）。

- id: g21
  term: CNSA
  full: Commercial National Security Algorithm Suite
  source_chapter: "p62, p92"
  definition: |
    美国商用国家安全算法套件。WPA3-Enterprise 192 位安全套件与 CNSA 对齐，常见于政务、国防、金融等高安全网络。注意机型限制：AP1101 全频段、AP1201H/AP1201L 的 2.4G 不支持，配置后静默回退 WPA2。

- id: g22
  term: Enhanced Open / OWE
  full: Opportunistic Wireless Encryption
  source_chapter: "p71"
  definition: |
    开放网络的增强加密：客户端与 WLAN 在接入过程中做 Diffie-Hellman 密钥交换并用 4 次握手生成成对密钥，防止明文被嗅探。Transition 模式下同一虚拟 AP 同时广播传统 Open SSID（2.4/5G）与 Enhanced Open SSID（2.4/5/6G）。6GHz 网络只允许 WPA3 与 Enhanced Open。

- id: g23
  term: MLO
  full: Multi-Link Operation
  source_chapter: "p63"
  definition: |
    Wi-Fi 7 的关键特性，允许设备同时使用多个频段（2.4G/5G/6G）聚合传输以提升速率与效率。MLO 生效依赖对应射频开启且 EHT（802.11be）已启用；MLO 客户端的 MAC 栏显示 MLD 地址，附着频段按 6GHz>5GHz>2.4GHz 优先显示。

- id: g24
  term: EHT / HE / VHT
  full: Extremely High / High / Very High Throughput
  source_chapter: "p42"
  definition: |
    分别对应 802.11be（Wi-Fi 7）、802.11ax（Wi-Fi 6）、802.11ac 的 PHY 模式。关闭 High Efficiency 时 HE 能力的 AP 降级到 VHT；关闭 Extremely High Throughput 时 EHT 能力的 AP 降级到 HE。

- id: g25
  term: Band Steering
  full: 频段引导
  source_chapter: "p46-47"
  definition: |
    把双频客户端引导到 5GHz 的特性，默认启用。Prefer 5G 模式基于信道利用率和客户端密度柔性引导（5G 忙时可回 2.4G）；Force 5G 模式强制双频终端只能上 5G（仅支持 2.4G 的终端不受限）。可按客户端排除（Exclude）。

- id: g26
  term: Airtime Fairness
  full: 空口时间公平
  source_chapter: "p47"
  definition: |
    让所有客户端（包括低速传统客户端）均等分享无线传输时间片的优化特性，默认禁用。配套特性还有 Load Balance（默认启用，客户端密度阈值 10、信道利用率阈值 70%）、RSSI Threshold、Roaming RSSI（配合 802.11k/v）。

- id: g27
  term: RSSI
  full: Received Signal Strength Indication
  source_chapter: "p26"
  definition: |
    接收信号强度指示，客户端窗口中取值 0~99。Client Health 分级依据：信号强度 >30 为 Best、15~30 为 Good、<15 为 Fair。wIDS/wIPS 还用 RSSI 估算未知 AP 距离：> -20dBm 最近、-45~-20dBm 近、-70~-45dBm 远、< -70dBm 最远。

- id: g28
  term: WMM
  full: Wi-Fi Multimedia (IEEE 802.11e)
  source_chapter: "p74"
  definition: |
    Wi-Fi 联盟基于 802.11e 的 QoS 认证，按四个接入类别排队：voice (AC_VO)、video (AC_VI)、best effort (AC_BE)、background (AC_BK)。Stellar AP 上可编辑 DSCP/802.1p 值与 WMM 优先级的映射关系（Modify WLAN QoS）。

- id: g29
  term: DTIM
  full: Delivery Traffic Indication Map
  source_chapter: "p65"
  definition: |
    Beacon 中的 DTIM 周期参数，决定 AP 向省电模式客户端投递缓存广播/组播帧的频率。默认 1（每个 Beacon 都检查缓存数据）；调大可增强终端省电效果。

- id: g30
  term: UAPSD
  full: Unscheduled Automatic Power Save Delivery
  source_chapter: "p64"
  definition: |
    802.11e 的非调度自动省电交付机制，可延长 Wi-Fi 终端电池续航，默认启用。相关漫游加速特性 OKC（Opportunistic Key Caching）复用缓存的 PMK 避免完整 802.1X 认证，实现快速漫游。

- id: g31
  term: Out-of-box MESH
  full: 开箱即连 Mesh
  source_chapter: "p103"
  definition: |
    出厂配置的 AP 在无有线 uplink 上电时，自动用内置 SSID "Stellar-MESH"（2.4G 频段）建立 Mesh 链路的特性，管理员只需指定根节点。AP 一旦接过有线 uplink 即被永久禁用，只有恢复出厂才能找回。Regular MESH 则需逐台登录 AP UI 手工配置。

- id: g32
  term: Wireless Bridge
  full: 点对点无线网桥
  source_chapter: "p105"
  definition: |
    通过无线接口连接不同楼宇/局域网的点对点网桥，替代昂贵专线与光纤。与 MESH 的关键区别：网桥 AP 只提供桥接链路、不能服务无线客户端；且 AP1201/AP1201L/AP1201H/AP1201HL 不支持带 VLAN 标签的桥接报文，不推荐做网桥。

- id: g33
  term: PMD
  full: Post Mortem Dump
  source_chapter: "p99"
  definition: |
    AP 致命崩溃后的故障诊断机制，用于定位 core dump 与异常指针的根因。启用并配置后，AP 关键进程崩溃时立即把 PMD 文件发送到指定 TFTP 服务器；默认向外发送是关闭的。

- id: g34
  term: DHCP Option 138 / Option 43
  full: DHCP 选项 138/43
  source_chapter: "p24"
  definition: |
    AP 切换到 Enterprise 模式（OmniVista On-Premise 管理）时，可通过这两个 DHCP 选项在 AP 启动阶段自动获取 OV 服务器地址，也可静态指定 OV 服务器地址。相关：组内还可通过 "Contact to Cloud" 周期性联系 OmniVista Cirrus 云管（默认启用）。

- id: g35
  term: LACP / 双上行
  full: Link Aggregation Control Protocol
  source_chapter: "p14"
  definition: |
    AP1230 系列、AP1311、AP1301、AP1351、AP1331、AP1411、AP1431、AP1451 支持双上行并在启动时与上游交换机自动建立 LACP 链路聚合。供电模式分 PoE Redundancy（单口供电）与 PoE Sharing（两口同时供电，AP1351/AP1451 为 Class 7、要求 IEEE 802.3bt 交换机）。

- id: g36
  term: Scanning Mode
  full: AP 扫描模式
  source_chapter: "p110"
  definition: |
    AP UI 里用于查看 RF Environment 数据的专用模式，分 One Time（持续 5 分钟后自动恢复）与 Always（持续扫描、拒绝客户端接入）两种。无扫描射频的机型进入该模式会中断常规 Wi-Fi 服务；AP1451 的 6GHz 服务会中断。
