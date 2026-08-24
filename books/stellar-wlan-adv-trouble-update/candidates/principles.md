# 原则/参数 · OmniAccess Stellar WLAN Advanced Troubleshooting and Update (DT00XTE378EN)

> 来源：source/fulltext.md（页码即教材 PDF 页码）
> 范围：仅 p134 以后的 Features Update 增量内容（p1-133 排障篇以姊妹书 T478 为准）

- id: p01
  title: 新 AP 家族全景——Wi-Fi 6/6E/7 三代产品线定位
  type: principle
  source_chapter: "p136-139"
  source_quote: |
    "Wi-Fi 6 Indoor MLE AP132x; Wi-Fi 6 Outdoor Rugged AP136x; Wi-Fi 6 Indoor SMB AP1311; Wi-Fi 6 Indoor MLE AP1351; Wi-Fi 6 Indoor Hosp. AP1301H. Wi-Fi 6E Indoor MLE AP1431; Wi-Fi 6E Indoor SMB AP1411; Wi-Fi 6E Indoor MLE AP1451. Wi-Fi 7 Indoor MLE AP1521; Wi-Fi 7 Indoor SMB AP1511."
  summary: |
    教材按 Wi-Fi 代际重排了 Stellar 产品线：Wi-Fi 5 只剩 AP123x（MLE 高端）；Wi-Fi 6 覆盖最全——AP1301（SMB 入门）、AP1301H（酒店/医疗款，带下行口）、AP1311（SMB+IoT）、AP132x（中档，1231 内置天线/1322 外接）、AP1331（中档 4x4）、AP1351（高端三射频）、AP136x（室外加固）；Wi-Fi 6E 三款——AP1411（入门，5/6GHz 可切换）、AP1431（中档三射频）、AP1451（高端三射频 8x8）；Wi-Fi 7 两款——AP1511（Premium 入门）、AP1521（中档）。命名规律：末位 1 多为内置天线、2 为外接天线款（1322/1362），x1 SMB、x3x/x5x 中高端。

  tags: [product-line, wi-fi6, wi-fi6e, wi-fi7, portfolio]

- id: p02
  title: Wi-Fi 7 双雄规格——AP1511 与 AP1521
  type: principle
  source_chapter: "p152-153"
  source_quote: |
    "AP1511: Tri radio; 2.4GHz radio: 688Mbps (2x2:2SS/EHT40); 5GHz radio: 2.88Gbps (2x2:2SS/EHT160); 6GHz radio: 5.76Gbps (2x2:2SS/EHT320); Up to 32 SSID; 512 clients per AP; 802.3at/bt POE (up to 35W). AP1521: 6GHz 5.76Gbps (EHT320); 1 x 1/2.5/5/10GE multi-gigabit uplink; 802.3bt POE (up to 60W); 802.3at (up to 15W) in low power mode; Temperature range 0 to +50 degree C."
  summary: |
    Wi-Fi 7 两款的差异化规格：AP1511 定位 Premium 入门，三射频 2x2（2.4G 688M / 5G 2.88G EHT160 / 6G 5.76G EHT320），32 SSID、512 客户端、1/2.5/5GE 多速率上联、802.3at/bt 最大 35W；AP1521 定位中档，同样三射频与 32 SSID，但上联升到 1/2.5/5/10GE 并多一个 1GE 下联口，802.3bt 最大 60W，低功率模式 802.3at 只给 15W。两者均集成 BLE5.1/ZigBee、工作温度上探 +50°C。选型要点：要 10G 上联和 60W 供电能力选 1521，成本敏感选 1511。

  tags: [ap1511, ap1521, wi-fi7, eht320, poe-bt, specs]

- id: p03
  title: Wi-Fi 7 技术六大特性与各代性能对照表
  type: principle
  source_chapter: "p162-163"
  source_quote: |
    "4096-QAM: +20% raw speed increase; Wider Channel Bandwidth: 320 MHz, 5x faster, 46 Gbps vs. 9.6 in Wi-Fi 6E; Multi-Link Operation (MLO); Multi Resource Unit (MRU); Preamble Puncturing; Automated Frequency Coordination (AFC)... Wi-Fi 7: Launch 2024, IEEE 802.11be, WPA3, Up to 320 MHz, 16x16 MU-MIMO."
  summary: |
    Wi-Fi 7 (802.11be) 的六个卖点及量化收益：4096-QAM（比 1024-QAM 原始速率 +20%）、320MHz 信道带宽（峰值 46 Gbps，是 6E 9.6 Gbps 的近 5 倍）、MLO 多链路操作（2.4/5/6GHz 同时收发，可靠性与低时延）、MRU 多资源单元、前导码打孔（Preamble Puncturing，被干扰的频段挖洞继续用）、AFC 自动频率协调（合规使用 6GHz）。代际对照表要点：Wi-Fi 6/6E/7 分别对应 802.11ax/ax/be，安全级别 WPA3 从 6 起步，MIMO 从 8x8（6E）升到 16x16（7），Wi-Fi 7 商用起点 2024 年。

  tags: [wi-fi7, 802.11be, mlo, 4096-qam, afc]

- id: p04
  title: 三种管理模式与规模红线（Express 集群 255 AP / 每交换机 32 / 每堆叠 64；Enterprise 4000 AP）
  type: principle
  source_chapter: "p169-176"
  source_quote: |
    "WiFi Express: Standalone mode; WiFi Enterprise: Managed mode with OmniVista 2500 NMS; WiFi Cloud: Managed mode with OmniVista Cirrus NMS. Move from Express to Enterprise/Cloud when/if needed. Self configured AP cluster, up to 255 APs... Max Up to 32 APs per OmniSwitch; Max Up to 64 APs per stack; Minimum 2xAP123X, AP13xx, 14xx or 15X1 in each Stack. Up to 4000 APs."
  summary: |
    Stellar 有三种管理模式且可迁移：Express（AP 自组集群、内置 Web 管理、向导配置、自带访客门户，集群上限 255 台 AP）；Enterprise（OmniVista 2500 本地网管，统一有线无线、UPAM 认证、热图/wIPS，规模上限 4000 AP、单设备 10 万客户端）；Cloud（OmniVista Cirrus 云管）。Express 的弹性设计约束：单台 OmniSwitch 挂 AP 不超过 32 台、一个堆叠不超过 64 台，且每个堆叠里至少放 2 台能担当 PVM/SVM 角色的高端型号（AP123X/13xx/14xx/15X1），避免单点故障导致集群失智。业务扩张时可平滑迁到 Enterprise/Cloud。

  tags: [express-mode, enterprise-mode, cluster-sizing, pvm-svm]

- id: p05
  title: IPv6 客户端支持差异——Express 全栈 IPv6，Enterprise 管理面仍走 IPv4
  type: principle
  source_chapter: "p178-179"
  source_quote: |
    "Express: IPv6 supported on Client side; IPv6 Policies supported; IPv6 address on AP management interface; AP get IPv6 address & gateway... Enterprise: AP Management through IPv4; No IPv6 network interface on AP; DPI support for IPv6 clients; Client authentication request to AP through IPv6; Radius communication between AP and UPAM through IPv4."
  summary: |
    两种模式对 IPv6 的支持深度不同，做教育/医疗/政务等 IPv6 刚性项目时必须先看这一条：Express 模式端到端 IPv6——客户端流量、IPv6 QoS/ACL 策略、AP 管理接口都可以用 IPv6（地址与网关从 DHCPv6 获取）；Enterprise 模式下 AP 没有 IPv6 管理接口，AP 与 OmniVista 的管理通信只走 IPv4，但客户端侧 IPv6 可用：IPv6 客户端可做 MAC/802.1X 认证（客户端到 AP 走 IPv6，AP 到 UPAM RADIUS 仍走 IPv4）、支持 DPI、门户认证客户端到门户服务器走 IPv6、门户到 RADIUS 走 IPv4，客户端之间及到 IPv6 网关的二三层转发正常。

  tags: [ipv6, express-mode, enterprise-mode, dhcpv6, dpi]

- id: p06
  title: WPA3 要点——SAE 个人版与 CNSA 192 位企业版
  type: principle
  source_chapter: "p256"
  source_quote: |
    "All Stellar APs are WPA3 compatible with software upgrade. WPA/WPA2-Personal PSK replaced by WPA3-Personal SAE (Simultaneous Authentication of Equals): Stronger Encryption Key (128 bits), Offline dictionary attack resistance. WPA3-Enterprise: Optional 192-bit security mode (CNSA option). CNSA enabled: Only wpa3 client authorized on the SSID. CNSA disabled: wpa2 or wpa3 clients authorized. CNSA option not enabled on AP1101 only."
  summary: |
    WPA3 是 2018 年发布、2019 年终端普及的新安全标准，全部 Stellar AP 升级软件即可支持。个人网用 SAE 替代 PSK：密钥加强到 128 位、可抗离线字典攻击，用户连接操作不变；企业网可开可选的 192 位 CNSA 模式——开启后 SSID 只允许 WPA3 客户端接入（老 WPA2 终端会被拒），不开则 WPA2/WPA3 双兼容。唯一例外是 AP1101 不支持 CNSA 选项，高安全需求选型时要避开这台入门机。

  tags: [wpa3, sae, cnsa, security, ap1101]

- id: p07
  title: SSID Usage 模板与安全级别映射表
  type: principle
  source_chapter: "p245"
  source_quote: |
    "Guest Network: Open or MAC, Captive Portal Guest. Employee BYOD Network: BYOD? 802.1X followed by Captive Portal BYOD, or 802.1X or MAC followed by 802.1X. Enterprise Network for Employees: Captive Portal? N. Protected Network (PSK): PSK followed by Captive Portal Guest; Protected Network for Employees (BYOD): PSK followed by Captive Portal BYOD."
  summary: |
    SSID 向导里选 Usage 等于选了一张安全模板：Guest Network = Open 或 MAC 认证 + 访客门户；Employee BYOD Network = 802.1X（或先 802.1X/MAC 再过 BYOD 门户）+ BYOD 注册；Enterprise Network for Employees = 纯 802.1X 企业认证、无门户；Protected Network = PSK 先认证再可选 Guest/BYOD 门户。模板只给默认值，全部参数之后仍可改。选错 Usage 会导致后续向导步骤里出现的选项集不同，建议按目标场景直接选对模板再微调。

  tags: [ssid-usage, template, security-level, captive-portal]

- id: p08
  title: WLAN Service 加密类型全集与必填项（Enterprise/Personal 两套清单）
  type: principle
  source_chapter: "p261"
  source_quote: |
    "Enterprise: Encryption Type DYNAMIC_WEP, WPA_TKIP, WPA_EAS, WPA2__TKIP, WPA2_AES, WPA3_AES; 802.1x Bypass is option; MAC Allow EAP is option; AAA Profile is a mandatory field. Personal: WPA_PSK_TKIP, WPA_PSK_AES, WPA_PSK_AES_TKIP, WPA2_PSK_TKIP, WPA2_PSK_AES, WPA3_SAE_AES, WPA3_PSK_SAE_AES; Passphrase is mandatory; Key Format; AAA Profile is Mandatory."
  summary: |
    WLAN Service (expert) 的 Security Settings 按安全级别出不同输入项。Enterprise 级：加密类型六选一（DYNAMIC_WEP 到 WPA3_AES），802.1x Bypass 与 MAC Allow EAP 可选，AAA Profile 必填；Personal 级：加密七选一（含 WPA3_SAE_AES 与 WPA3_PSK_SAE_AES），Passphrase 与 Key Format 必填，AAA Profile 同样必填。另有两个硬规则：Default Access Role Profile 一律必填（承载 UNP 属性：QoS 策略、门户认证、带宽控制，并映射到 SSID 的 VLAN）；Enterprise/Personal 级都必须配 AAA Server Profile（定义 802.1X/MAC/门户认证服务器与计费服务器，默认可选内嵌 UPAM）。

  tags: [encryption, wlan-service, aaa-profile, mandatory-fields]

- id: p09
  title: 广播/组播优化参数——密钥轮换 15 分钟、组播优化双阈值 90%/6 客户端
  type: principle
  source_chapter: "p270-271"
  source_quote: |
    "Broadcast Key rotation: Only applicable for Enterprise; Rotate the keys periodically to avoid key cracking. Default period: 15 min – Range 1 min – 24 hours. Broadcast Filter All: Drop all broadcast packets except DHCP & ARP. Multicast Optimization: Convert multicast to unicast... Upper limit: Channel Utilization default 90%; Number of Clients default 6."
  summary: |
    高级 WLAN Service 里一组容易忽略的广播/组播参数：(1) Broadcast Key Rotation 仅企业级可用，周期轮换 PTK/GTK 防破解，默认 15 分钟、范围 1 分钟到 24 小时；(2) Broadcast Filter All 丢弃除 DHCP/ARP 外的全部广播包，Broadcast Filter ARP 把广播 ARP 转单播——没有特殊组播应用时建议开启；(3) Multicast Optimization 把组播转单播（用 PTK 单播密钥、最高速率发送，仅限 IP 组播与 IGMP Snooping 流量），但它有自动熔断：信道利用率超过默认 90%（射频环境太差）或高吞吐客户端数超过默认 6（CPU 吃紧）时自动停止优化。调优时别把阈值当摆设，高负载下组播优化会悄悄失效。

  tags: [broadcast-filter, multicast-optimization, key-rotation, thresholds]

- id: p10
  title: WMM QoS 推荐 DSCP/802.1p 映射表
  type: principle
  source_chapter: "p273"
  source_quote: |
    "Recommended Settings: Best Effort 802.1p 0, DSCP 0; Background 2, 18 – AF21; Voice 5, 46 – EF; Video 4, 34 – AF41. Default OV Settings: Best Effort 0,3 / 0x00, 0x18; Background 1,2 / 0x08, 0x10; Voice 6,7 / 0x30, 0x38; Video 4,5 / 0x20, 0x28."
  summary: |
    四个 WMM 队列与 802.1p/DSCP 的两组映射：推荐配置（语音 5/46-EF、视频 4/34-AF41、尽力而为 0/0、后台 2/18-AF21）与 OmniVista 默认配置（语音 6,7/48,56、视频 4,5/32,40、尽力而为 0,3/0,24、后台 1,2/8,16）并不一致。默认值把多档 DSCP 归到同一 WMM 类，推荐值则是一对一的规范映射。做语音/视频业务或与有线侧 QoS 策略联动时，应按推荐表改映射，上下行方向分别配置（Uplink/Downlink 802.1p/DSCP），避免无线侧标记与交换机队列错位。

  tags: [wmm, qos, dscp, 802.1p, mapping]

- id: p11
  title: 漫游特性参数——OKC 只配 WPA2-Enterprise，802.11r 推荐，Roaming RSSI 阈值 2.4G=10/5G=15
  type: principle
  source_chapter: "p188-191"
  source_quote: |
    "Based on the VLAN ID between the 'home' and 'foreign' AP, select either Layer 2 Roaming or Layer 3 Roaming. With WPA2 Enterprise only, OKC can be activated. With WPA2 only, 802.11r (Fast Roaming) can be activated (recommended)... Use the Roaming RSSI Threshold in the RF profile. Use in conjunction with 802.11k and 802.11v. Value range is 0-100. Recommended value for 2.4GHz: RSSI = 10; Recommended value for 5GHz: RSSI = 15."
  summary: |
    漫游设计的三组参数：(1) 先按"本地 AP 与外地 AP 是否同 VLAN"决定做二层还是三层漫游；(2) 快速漫游特性与安全级别绑定——OKC（机会性密钥缓存）只能在 WPA2-Enterprise 下启用，802.11r 快速漫游在 WPA2 下可启用且是教材推荐项；(3) 治粘滞客户端用 RF Profile 里的 Roaming RSSI Threshold（配合 802.11k/11v 引导），取值 0-100，推荐 2.4GHz 设 10、5GHz 设 15——该阈值控制客户端在什么信号强度下才开始找下一个 AP。地理相邻但射频互相看不见的 AP（直角走廊遮挡）要手动互加 Neighbor AP 才能共享客户端上下文。

  tags: [roaming, 802.11r, okc, rssi-threshold, sticky-client]

- id: p12
  title: RSSI 与 dBm 换算规则（dBm = RSSI − 96）及信号分档
  type: principle
  source_chapter: "p186, p365"
  source_quote: |
    "RSSI 10 = -86 dBm; RSSI 20 = -76; RSSI 30 = -66; RSSI 40 = -56; RSSI 43 = -53. Bad: Not recommended for Video or Audio applications. OK – not bad. Desired and recommended. (p365) To convert the RSSI value to dBm you just need to subtract 96 to the RSSI value. -18 dBm = 78."
  summary: |
    Stellar 体系里 RSSI 与 dBm 并存，换算口诀是 dBm = RSSI − 96（如 RSSI 10 = -86dBm、RSSI 30 = -66dBm、-18dBm 反算回 RSSI 78）。信号分档：RSSI 10-19（约 -86 至 -77dBm）为差，不建议跑视频/音频；20-28 为一般可用；29 以上（约 -67dBm 以上）为期望推荐值。注意 OmniVista 2500 的客户端列表显示 dBm，而 AP 的 RF 设置（关联/漫游阈值）用 RSSI，配置前必须先换算单位再比较，这正是 RF Profile 实验里"客户端 -18dBm 要挡住就得把阈值设到 90"的由来。

  tags: [rssi, dbm, conversion, signal-quality]

- id: p13
  title: BLE Beaconing 参数——默认关闭、iBeacon 模式、UUID/Major/Minor 按 AP Group 配置
  type: principle
  source_chapter: "p194"
  source_quote: |
    "BLE Beaconing ready for the AP1230 and AP13XX series with a built-in BLE. BLE Beacon is configured per AP Group. Turned OFF by default. Configurable parameters are: Beaconing Mode: iBeacon per default; Transmission Power; Frequency/Emission Period; UUID – ALE specific UUID for all ALE products; Major and Minor values – used for greater accuracy than UUID alone."
  summary: |
    内置 BLE 的 AP（AP1230、AP13xx 系列）可做资产定位信标，为资产追踪方案（找轮椅、医疗设备、笔记本电脑，缩短找人找物时间）打底。配置粒度是 AP Group 而非单台 AP，默认关闭，启用后可调四类参数：信标模式（默认 iBeacon）、发射功率、发射周期、UUID（ALE 产品统一 UUID）与 Major/Minor 值（比单用 UUID 定位更精细）。配套方案是与 AeroScout RTLS 集成：Stellar AP 把标签与客户端的 RSSI 测量值送给 AeroScout Engine，由引擎解算位置并在地图上呈现热图、地理围栏告警。

  tags: [ble, ibeacon, asset-tracking, aerioscout, rtls]

- id: p14
  title: Wi-Fi Mesh 规格红线——4 跳 / 单跳 5 台 / 全网 16 台 / 每台 5 个 SSID
  type: principle
  source_chapter: "p399-401"
  source_quote: |
    "WIFI MESH – LIMITATIONS: UP TO 4 HOPS; UP TO 5 APS IN A SINGLE HOP IN A PEER TO MULTI PEER CONNECTION; UP TO 16 APS IN THE MESH NETWORK; ALL APS CAN BROADCAST UP TO 5 SSIDS FOR CLIENTS. WIFI MESH – BEST PRACTICE: BAND: 5 GHZ (OR 6GHZ); CHANNEL > 100."
  summary: |
    Mesh 组网的四条硬限制：最大 4 跳、单跳点到多点连接最多 5 台 AP、整个 Mesh 网络最多 16 台 AP、每台 AP 最多广播 5 个面向客户端的 SSID。Mesh 属性四要素（SSID、频段、Is Root、Passphrase）两端必须一致，与 Bridge 不同的是 Mesh 允许多台 AP 同为 Root。最佳实践：回程用 5GHz（或 6GHz）、信道选 100 以上（DFS 之外更稳）。Auto Mesh 机制：连着有线且配成 Mesh Root 的 AP 会广播隐藏 SSID "Stellar-MESH"（5GHz）；没插网线的 AP 自动以非 Root 身份入网，实现免配置快速部署。

  tags: [mesh, auto-mesh, limitations, best-practice, backhaul]

- id: p15
  title: Wi-Fi Bridge 与 Mesh 的属性差异及 VLAN tagging 兼容性
  type: principle
  source_chapter: "p398-399"
  source_quote: |
    "WiFi Bridge: Replace physical cabling; VLANs can be used to separate & secure traffic over the bridge*; Cannot provide service (WiFi) to WiFi clients. WiFi Mesh: Can provide service (WiFi) to WiFi clients... * AP1101, AP1201 & AP1201H are not compatible with VLAN tagging over a bridge."
  summary: |
    Bridge 与 Mesh 的本质区别：Bridge 是"无线网线"，替代两栋楼之间的物理布线（场景：隔街建筑、拉不了线），可以用 VLAN 隔离和保护桥上流量，但不能给 Wi-Fi 客户端提供服务；Mesh 在回程之外还能给客户端发 SSID（场景：营地全覆盖），并按 SSID 用 VLAN 隔离不同客户端流量。两者共同属性：SSID、频段、Passphrase 两端必须相同，Bridge 必须且只能有 1 台 Root，Mesh 可多 Root。兼容性红旗：AP1101、AP1201、AP1201H 不支持桥上 VLAN tagging，需要 VLAN 隔离的桥接场景不能用这三款。

  tags: [wifi-bridge, mesh, vlan-tagging, ap1101, compatibility]

- id: p16
  title: OmniVista Cirrus 4 订阅与许可模型——Freemium/Premium 差异、5000 设备上限、每 AP 含 50+50 门户许可
  type: principle
  source_chapter: "p409-411"
  source_quote: |
    "Freemium: Self Registration, Free of charge, No device capacity limitation, No duration limitation, No network Configuration, On-time Network Device Upgrade, Restricted OV CIRRUS capabilities, Can be upgraded to Premium. Premium: All OV CIRRUS capabilities... Max amount of licenses: 5000... Duration of 1, 3 or 5 Years; 1 license per Access Point; 50xGuest and 50xBYOD licenses included per AP license."
  summary: |
    Cirrus 4 是 SaaS 订阅制云管，单实例上限 5000 设备 / 4000 AP。Freemium 免费自助注册：不限设备数量与时长，但不能做网络配置、只提供一次性设备升级、功能受限，可升级为 Premium。Premium 全功能，按设备类型/数量/时长（1/3/5 年）订阅，经 ALE Business Store/CPQ 或 eBUY 购买，可扩容缩容续订。许可分档：LAN Essential（OS2260/2360/6350/6450/6465/6560）、LAN Advanced（OS6860N/6865/6870）、LAN Core（OS6900）；Stellar AP 全型号一个档，1 AP 1 个许可，且每个 AP 许可附送 50 个 Guest + 50 个 BYOD 门户账号许可。

  tags: [omnivista-cirrus, subscription, licensing, freemium, premium]

- id: p17
  title: Cirrus 4 上云最低软件版本要求（AOS 8.4.1.R03+ / 6.7.2.R03+ / 5.1R1+，AWOS 3.0.2+）
  type: principle
  source_chapter: "p414"
  source_quote: |
    "OS version required on Network Device. AOS 8.4.1.R03 +: OS6560, OS6860N, OS6865, OS6870, OS6900. AOS 6.7.2.R03 +: OS6350, OS6450. AOS 5.1R1 +: OS2260, OS2360. AWOS 3.0.2 +: All Stellar Access Point models."
  summary: |
    存量设备注册到 OmniVista Cirrus 4 前必须核对四条版本底线：OS6560/6860N/6865/6870/6900 要 AOS 8.4.1.R03 及以上；OS6350/6450 要 AOS 6.7.2.R03 及以上；OS2260/2360 要 AOS 5.1R1 及以上；全部 Stellar AP 要 AWOS 3.0.2 及以上。低于底线的设备先在本地升级再上云，否则卡在注册/激活环节。这也是存量网络"上云评估"的第一张检查表——先盘点全网版本分布，再决定升级工作量。

  tags: [omnivista-cirrus, minimum-version, aos, awos, upgrade]

- id: p18
  title: RAP 部署的设备与账号要求——AP1101 不兼容，Premium 只需 Cirrus，Freemium 需 OV2500+VPN 服务器
  type: principle
  source_chapter: "p375"
  source_quote: |
    "* AP1101 not compatible with the RAP Feature. EQUIPMENTS: OmniVista Cirrus 4 > Freemium Account with OmniVista 2500; OmniVista Cirrus 4 > Premium Account."
  summary: |
    远程 AP（RAP）功能的两条硬性前提：硬件上 AP1101 不支持 RAP，选型时远程站点要避开这台入门机；平台上有两种组合——Premium 账号只要 OmniVista Cirrus 4（配置与 AP 状态全在云端），Freemium 账号则必须搭配本地 OmniVista 2500（Cirrus 只负责引导，实际管理在 OV2500）。两种模式都要在公司侧部署 ALE 提供的 VPN Server 虚拟机（VPN Server VA，OVF 包从 BPWS 下载，可装 VMware 或 Hyper-V），Freemium 模式该虚机要三块网卡（公网/管理隧道/数据隧道）。

  tags: [rap, ap1101, premium, freemium, vpn-server]

- id: p19
  title: Stellar AP 备份规则——只能按 AP Group 备份、按地图备份不含 AP、且不支持 Restore
  type: principle
  source_chapter: "p427, p430"
  source_quote: |
    "Backup by Maps: select a map(s) to backup all devices in the map(s). Note that if a map contains AOS Devices and Stellar APs, the Stellar APs will not be backed up. Stellar APs can only be backed up by AP Group. (p430) It is not possible to perform a restore on a Stellar AP, as most of the configuration is pushed when the Access Points is inserted in an AP Group."
  summary: |
    Resource Manager 备份的三种方式里藏着一个坑：Backup by Devices 选交换机、Backup by Maps 按地图打包、Backup by AP Group 只用于 Stellar AP。按地图备份时即使地图里有 AP，AP 也不会被备份——Stellar AP 只能按 AP Group 备份。恢复操作只对 AOS 交换机可用：Stellar AP 无法执行 Restore，因为它的配置绝大部分来自所在 AP Group 的下发；AP 的备份文件的价值是离线分析/排障与提供给技术支持，而不是回灌。

  tags: [backup, stellar-ap, ap-group, restore, resource-manager]

- id: p20
  title: 外接天线判定规则——型号尾数为 2 才支持外接，全部 AP 标配内置全向天线
  type: principle
  source_chapter: "p158"
  source_quote: |
    "Some OmniAccess Stellar Access Points can be equipped with external antennas to: Gain more control over the energy radiated; Tailor the shape based on the coverage needed. Access points compatible with external antennas have their reference ends with '2' (ex. AP1322, AP1362). Note: All OmniAccess Stellar Access Points are equipped with an internal antenna (omni-directional coverage pattern)."
  summary: |
    选外接天线前的两条判定规则：(1) 只有型号末位为 2 的 AP 支持外接天线（AP1322、AP1362 等），作用是精确控制辐射能量、按覆盖需求定制天线形状；(2) 所有 Stellar AP（包括外接款）都自带内置全向天线，不开箱即用场景不需要另购。具体兼容哪款天线要查各 AP 的数据手册或 Product Line Matrix 的天线矩阵（含频率范围、增益、波束宽度、极化方式）。配套配件同理：PoE 注入器用于非 PoE 交换机场景、电源适配器直插插座、安装套件（吊装/壁装）的兼容性都在数据手册里查。

  tags: [external-antenna, antenna-matrix, accessories, naming-rule]

- id: p21
  title: UPAM 内置 RADIUS 的 NAS 项 "All Managed Devices" 与共享密钥 123456
  type: principle
  source_chapter: "p307"
  source_quote: |
    "In UPAM, there is a system-defined NAS Client Item (All Managed Devices). It cannot be deleted and is used to indicate that all the devices managed by OmniVista are automatically added into the NAS Client Database of UPAM and perform the AAA process. The shared secret in the system-defined 'All Managed Devices' NAS profile is '123456'."
  summary: |
    UPAM（OmniVista 2500 内嵌的统一认证平台，兼做 Captive Portal 服务器与 RADIUS 服务器，支持 MAC/802.1X/门户多种认证）里有一个系统级 NAS Client 项 "All Managed Devices"：不可删除，作用是把 OmniVista 管理的所有设备自动登记为 UPAM 的 NAS 客户端参与 AAA 流程，省去逐台添加。该系统项的共享密钥固定为 "123456"。排障 802.1X 时若怀疑密钥不匹配，先想到这个默认值；AP 侧 AAA_server.conf 里也能看到 UPAMRadiusServer 的 secret 明文。

  tags: [upam, radius, nas, shared-secret, default-credentials]

- id: p22
  title: 应用识别（DPI）与 WCF 的硬件支持范围——AP1101 与 AP1201H 被排除
  type: principle
  source_chapter: "p281, p287"
  source_quote: |
    "Full Application Visibility signature kit (~2000 applications). Creation of Policy List, based on the L7 Application (Google, Facebook,…). The Application Visibility feature is supported on: OS6860N & OS6870 switches; All Stellar APs models (except AP1101 and AP1201H). (p287) Not supported: AP1101; AP1201H."
  summary: |
    两项 L4-L7 特性对硬件有要求：应用可视化（Application Visibility，约 2000 个应用签名的 DPI，可按 L7 应用如 Google/Facebook 建 Policy List，双向执行）只支持 OS6860N/OS6870 交换机和除 AP1101、AP1201H 之外的全部 Stellar AP；Web Content Filtering（网页内容过滤）同样不支持 AP1101 与 AP1201H。规划基于 DPI 的用户角色限速或访客网页过滤时，覆盖区域里混有这两款入门 AP 就会出现策略"部分生效"，选型或换机时要先清点这两款设备的位置。

  tags: [dpi, application-visibility, wcf, ap1101, ap1201h, support-matrix]
