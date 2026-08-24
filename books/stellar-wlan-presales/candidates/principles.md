# 原则/清单/规则/参数常数候选条目 — OmniAccess Stellar WLAN Presales Ed28
# 提取自 source/fulltext.md（页码即 <<<PAGE n>>> 标记），宁多勿漏，未做筛选。

- id: p01
  title: 外接天线 AP 型号尾数规则（以"2"结尾）
  type: principle
  source_chapter: "p32"
  source_quote: |
    "Access points compatible with external antennas have their reference ends with “2” (ex. AP1322, AP1362)
    Note: All OmniAccess Stellar Access Points are equipped with an internal antenna (omni-directional coverage pattern)"
  summary: |
    支持 External Antennas（外接天线）的 Stellar AP，其型号以数字"2"结尾（如 AP1322、AP1362）；
    以"1"结尾的型号（如 AP1321、AP1361）为内置全向天线，不能接外置天线。所有 Stellar AP 出厂
    都带内置全向天线。外接天线用于需要控制辐射能量、定制覆盖形状的场景；具体兼容天线型号查
    各 AP 的 datasheet 或 Product Line Matrix。售前选型时可凭尾数快速判断是否支持外接天线。
  tags: [ap-hardware, antenna, naming-rule, selection]

- id: p02
  title: Wi-Fi 代际性能常数表（Wi-Fi 4/5/6/6E/7）
  type: principle
  source_chapter: "p37"
  source_quote: |
    "Wi-Fi Generations: Wi-Fi 4 / Wi-Fi 5 / Wi-Fi 6 / Wi-Fi 6E / Wi-Fi 7
    Launch date 2007 / 2013 / 2019 / 2021 / 2024
    IEEE std. 802.11n / 802.11ac / 802.11ax / [802.11ax] / 802.11be
    Max data rate 1.2 Gbps / 3.5 Gbps / 9.6 Gbps / 46 Gbps
    Bands 2.4/5 GHz / 2.4/5 GHz / 2.4/5 GHz / 2.4/5/6 GHz / 2.4/5/6 GHz
    Security WPA 2 / WPA 2 / WPA 3 / WPA 3
    Channel width 20,40 MHz / 20,40,80,80+80,160 MHz / 20,40,80,80+80,160 MHz / Up to 320 MHz
    Modulation 64-QAM, OFDM / 256-QAM, OFDM / 1024-QAM, OFDMA / 4096-QAM, OFDMA
    MIMO 4x4 MIMO / 4x4 MIMO, DL MU-MIMO / 8x8 UL/DL MU-MIMO / 16x16 MU-MIMO
    Power Saving TWT / RTWT"
  summary: |
    Wi-Fi 各代际可背诵对照：Wi-Fi 4（2007, 802.11n, 1.2Gbps, 64-QAM）→ Wi-Fi 5（2013, 802.11ac,
    3.5Gbps, 256-QAM）→ Wi-Fi 6（2019, 802.11ax, 9.6Gbps, 1024-QAM, OFDMA, TWT）→ Wi-Fi 6E（2021,
    新增 6GHz 频段）→ Wi-Fi 7（2024, 802.11be, 46Gbps, 320MHz 信道, 4096-QAM, 16x16 MU-MIMO, MLO,
    RTWT）。安全上 Wi-Fi 6 起默认 WPA3。Wi-Fi 7 相对 6E 原始速率提升约 +20%（46 vs 9.6 Gbps）。
    售前对比友商或解释升级价值时直接引用。
  tags: [wifi-standards, wifi6, wifi7, constants, benchmark]

- id: p03
  title: Express 集群规则：PVM/SVM 选举与 255 AP 上限
  type: principle
  source_chapter: "p45"
  source_quote: |
    "In the case of a VLAN with several APs started at the same time an election process is perform to select the PVM
    Highest Model Type / Highest MAC address
    AP with the second highest MAC is designated as the SVM
    Once the PVM is designated, it sends an SSID for the configuration of the AP-group mywifi-0102
    All other APs become members of the group with up to 255 APs in a group."
  summary: |
    WiFi Express（无控制器自立集群）核心规则：同一 VLAN 内多台 AP 同时启动时自动选举 PVM
    （Primary Virtual Manager，主虚拟管理器），选举依据为"最高型号等级 + 最高 MAC 地址"；
    MAC 第二高的 AP 成为 SVM（备援）。PVM 选定后广播默认管理 SSID "mywifi-0102"。
    一个 Group 最多 255 台 AP（p46：第 256 台不被纳管，停留在 joining 状态）；要超过 255 台
    必须划分多个 Group-ID 或多个 VLAN（p47：Cluster Max Size 255，全系列 AP 均可担任 PVM/SVM）。
    p48 弹性建议：集群超过 64 台时要做网络冗余设计；每台 OmniSwitch 最多接 32 台 AP、每个堆叠
    最多 64 台 AP、每个堆叠内至少放 2 台 AP12xx/13xx/14xx/15xx 以保证 PVM/SVM 双保险。
  tags: [express-mode, cluster, pvm, election, scaling, capacity]

- id: p04
  title: DHCP Option 138 决定 AP 模式（出厂默认 Express）
  type: principle
  source_chapter: "p66"
  source_quote: |
    "Factory Default mode: WiFi Express
    AP Mode is hard coded at first boot: Mode can not be changed
    ⚫Requires a factory reset (push button) and reboot
    Migration from existing Express to Enterprise mode
    ⚫From the Web interface, load the new software
    ⚫Add option 138 in the DHCP server for the AP management scope
    ⚫Perform a factory reset/reboot
    ⚫No configuration migration, AP “cluster” configuration is lost"
  summary: |
    Stellar AP 出厂默认为 WiFi Express 模式，且模式在首次启动时被硬编码，运行中不能直接切换。
    DHCP 是否下发 Option 138（内容为 OmniVista 2500/Cirrus 服务器 IP）是模式判定的开关：
    p67 注释——DHCP offer 中没有 Option 138 → AP 进 Cluster（Express）模式；有 Option 138 →
    AP 联系 OV 服务器注册，进入 Enterprise/Cloud 模式。从 Express 迁移到 Enterprise 需：
    Web 界面加载新软件、在 DHCP 管理 scope 加 Option 138、恢复出厂并重启；原有集群配置不迁移、
    全部丢失。售前做割接方案时必须提醒客户配置需重建。
  tags: [dhcp, option-138, express-mode, enterprise-mode, migration, deployment]

- id: p05
  title: AP 注册成功三条件（Trusted + Licensed + 国家码匹配）
  type: principle
  source_chapter: "p68"
  source_quote: |
    "AP is managed when Registration succeeds ⚫AP is Trusted ⚫AP is Licensed ⚫Country Code matches RF profile CC
    AP is unmanaged when Registration fails ⚫AP is not Trusted ⚫AP is not Licensed
    ⚫Country Code does not match the Country Code from the RF Profile ⚫Others
    ⚫Configuration not applied ⚫All Radios are off"
  summary: |
    Enterprise/Cloud 模式下，AP 在 OmniVista 注册成功转为"受管"必须同时满足三个条件：
    ① Trusted（被信任；p69：默认新 AP 不自动注册，需要管理员手动 Trust，但手动创建或
    Excel 导入的 AP 自动视为 Trusted）；② Licensed（有对应 AP License）；③ AP 的 Country Code
    （国家码/区域码）与 RF Profile 中的国家码一致。任一条件不满足则注册失败、AP 处于
    Unmanaged 状态：配置不下发、所有射频关闭。排障时按这三条逐一核查。
  tags: [registration, trust, license, country-code, troubleshooting]

- id: p06
  title: Enterprise/Cloud 模式容量常数：4000 AP / 100K 客户端
  type: principle
  source_chapter: "p75"
  source_quote: |
    "AP managed by OmniVista (2500/Cirrus) • Distributed intelligence • Distributed Control Plane …
    • Scalable • Up to 4000 APs • Up to 100K clients"
  summary: |
    Enterprise 模式（OmniVista 2500，p52）与 Cloud 模式（OmniVista Cirrus 4/10，p60）的单台
    网管容量上限均为 4000 台 AP、10 万并发客户端；AP Group 数量无限制（p76），4000 台 AP 可
    分布在一个或多个 AP Group。数据面仍为分布式（只有 L2 转发、无集中隧道），管理面集中。
    超过 4000 AP 需多套 OV 或分域管理。报价与方案规模校核时的硬上限。
  tags: [enterprise-mode, cloud-mode, capacity, scaling, omnivista]

- id: p07
  title: 智能负载均衡 SNR 门限默认值（2.4G=18dB / 5G=12dB）
  type: principle
  source_chapter: "p87"
  source_quote: |
    "Client SNR Strength Threshold
    ⚫Client Signal to Noise Ratio in db (noise floor ~95dbm)
    ⚫Deny connection to APs when signal of client is too weaker
    ⚫Disconnect client when signal of client becomes weak
    ⚫Default value : 2.4G =18db , 5G = 12db - Range 0-40 db"
  summary: |
    Smart Load Balancing（智能负载均衡）三件套：Band Steering（引导终端到 2.4/5/6GHz，可强制
    5G/6G）、Dynamic/Smart Load Balance（按每 AP 客户端数做 AP 间负载分担）、Smart Air Share
    （限制 11b/g 老终端、最低速率控制）。客户端 SNR 门限规则：底噪约 -95dBm；信号过弱的客户端
    会被拒绝接入（Deny）或被踢下线（Disconnect）；默认门限 2.4GHz=18dB、5GHz=12dB，可调范围
    0-40dB。三个功能的判决依据分别是：每射频客户端数、信道利用率、客户端 SNR。
  tags: [load-balancing, band-steering, snr, radio-management, constants]

- id: p08
  title: 快速漫游协议适用规则（OKC vs 802.11r）
  type: principle
  source_chapter: "p89"
  source_quote: |
    "Fast Roaming supported
    OKC for WPA2 Enterprise only
    802.11r for WPA2 Personal and Enterprise"
  summary: |
    Stellar 支持两种快速漫游（Fast Roaming）机制，按认证方式选择：OKC（Opportunistic Key
    Caching）仅适用于 WPA2-Enterprise；802.11r 对 WPA2-Personal 和 WPA2-Enterprise 都适用。
    跨 AP Group 的 L3 漫游通过客户端上下文（CTX）同步与清理实现，VLAN 映射随 Access Role
    Profile 变化。语音/漫游敏感项目选型时按终端认证方式套用此规则；802.11k/v 辅助粘性客户端
    优化（p114：802.11v/k + Roaming RSSI 门限，Express 与 Enterprise 均可配）。
  tags: [roaming, fast-roaming, 802.11r, okc, voice]

- id: p09
  title: BLE Beacon 与 Zigbee IoT 能力边界
  type: principle
  source_chapter: "p95"
  source_quote: |
    "BLE Beacon is configured per AP Group • Turned OFF by default • Configurable parameters are
    • Beaconing Mode : iBeacon per default • Transmission Power • Frequency/Emission Period
    • UUID (Universal Unique Identifier) – ALE specific UUID for all ALE products
    • Major and Minor values – used for greater accuracy than UUID alone"
  summary: |
    BLE Beaconing 规则：按 AP Group 配置、默认关闭；默认模式 iBeacon；可调参数为发射功率、
    发射频次/周期、UUID（全 ALE 产品共用 ALE 专属 UUID）、Major/Minor（比 UUID 更精细定位）。
    支持 BLE 的型号：AP1201、AP1230 系列、AP1301H/1311/1351、AP1320/1360 系列、AP1411/1431/1451、
    AP1511/1521（均内置）。Zigbee（p98，门锁/智能家居等楼宇自动化场景）：除 AP1301 和 AP1230
    系列外全系列支持（BLE 5.1/Zigbee 内置电台）。售前做资产追踪或数字门锁方案时按此清单选型。
  tags: [ble, iBeacon, zigbee, iot, asset-tracking, compatibility]

- id: p10
  title: RAP（远程接入 AP）前提条件清单
  type: principle
  source_chapter: "p99"
  source_quote: |
    "Prerequisites
    ⚫Stellar AP models : ALL except AP1101
    ⚫Stellar AP version : 4.0.0 and above
    ⚫OmniVista Cirrus : 4.5.1 and above
    ⚫OmniVista Enterprise : 4.5.1 and above"
  summary: |
    RAP（Remote Access Point，远程办公/分支接入）前提：支持除 AP1101 外所有 Stellar AP 型号；
    AP 固件 4.0.0 及以上；OmniVista Cirrus 4.5.1 及以上或 OmniVista Enterprise（OV2500）4.5.1
    及以上。方案要点（p99-100）：企业网内部署 VPN 服务器，AP 与 VPN 服务器之间加密传客户端
    数据（支持 VLAN 打标），多个 RAP 可连同一 VPN 服务器；OV Cirrus 账号规则——已用 OV2500
    纳管时配 OV Cirrus Freemium 账号，不用 OV2500 时需 OV Cirrus Premium 账号；RAP 模式与
    VPN 服务器 IP、OV2500 IP 由云端下发。
  tags: [rap, remote-ap, vpn, homeworking, prerequisites, version]

- id: p11
  title: WPA3 安全规则（SAE 128 位、CNSA 192 位）
  type: principle
  source_chapter: "p105"
  source_quote: |
    "WPA/WPA2-Personal PSK (Pre-Shared Key) replaced by WPA3-Personal SAE (Simultaneous Authentication of Equals)
    ⚫Stronger Encryption Key (128 bits) ⚫Offline dictionary attack resistance
    ⚫No additional complexity to connect (user side)
    WPA/WPA2-Enterprise replaced by WPA3-Enterprise
    ⚫Optional 192-bit security mode (CNSA option)
    CNSA enabled: Only wpa3 client authorized on the SSID
    CNSA disabled: wpa2 or wpa3 clients authorized on the SSID"
  summary: |
    WPA3（Wi-Fi Alliance 2018 发布、2019 终端普及）规则：Personal 模式用 SAE 取代 PSK，密钥
    强度 128 位、可抗离线字典攻击、用户侧连接复杂度不变；Enterprise 模式可选 192 位安全模式
    （CNSA，面向高安全客户）。CNSA 开启时该 SSID 仅允许 WPA3 客户端接入；CNSA 关闭时 WPA2
    与 WPA3 客户端都允许（兼容模式）。所有 Stellar AP 可通过软件升级支持 WPA3。
  tags: [security, wpa3, sae, cnsa, encryption]

- id: p12
  title: Hotspot 2.0 / WiFi4EU 会话常数（最长 12 小时）
  type: principle
  source_chapter: "p108"
  source_quote: |
    "WiFi4EU ⚫European Union Initiative, to provide free Wifi access to citizen in public venues
    ⚫Networks with WiFi4EU SSID use an HTTPS Captive Portal
    ⚫Session timeout should be configurable up to 12 hours"
  summary: |
    Hotspot 2.0（Passpoint）作为 WLAN Service 的一个选项，用于把 3G/4G 流量卸载到 WiFi 并提供
    无缝安全接入（WPA2-Enterprise + 802.11u GAS/ANQP + EAP-SIM/EAP-AKA）。WiFi4EU（欧盟公共
    场所免费 WiFi 计划）合规要点：SSID 使用 HTTPS Captive Portal，会话超时必须可配置到最长
    12 小时。做欧盟公共场馆项目时这是硬性合规参数。
  tags: [hotspot2.0, wifi4eu, captive-portal, compliance, session-timeout]

- id: p13
  title: WiFi Mesh 限制常数与最佳实践
  type: principle
  source_chapter: "p112"
  source_quote: |
    "WIFI MESH – LIMITATIONS
    • UP TO 8 SLAVE APS • UP TO 4 HOPS
    • UP TO 5 APS IN A SINGLE HOP IN A PEER TO MULTI PEER CONNECTION
    • UP TO 16 APS IN THE MESH NETWORK • ALL APS CAN BROADCAST UP TO 5 SSIDS FOR CLIENTS
    WIFI MESH – BEST PRACTICE • BAND: 5 GHZ; 6 GHZ ON STELLAR AP WI-FI 6E • CHANNEL > 100"
  summary: |
    WiFi Mesh 组网硬限制：最多 8 台从 AP（slave）、最多 4 跳、单跳对多点连接中每跳最多 5 台
    AP、整个 Mesh 网络最多 16 台 AP、所有 AP 总共最多广播 5 个客户端 SSID。最佳实践：回程用
    5GHz（Wi-Fi 6E AP 可用 6GHz）、信道选大于 100（避开常用客户端信道）。区分 Bridge 与 Mesh
    （p110）：Bridge 只替代线缆、不给 WiFi 客户端提供服务，SSID/频段/密码两端必须一致且必须
    指定 1 台 Root；AP1101/AP1201/AP1201H 的 Bridge 不支持 VLAN 打标。Auto Mesh（p113）：连
    有线且配为 Mesh Root 的 AP 广播隐藏 SSID "Stellar-MESH"（5GHz），未连有线的 AP 自动以
    non-root 入网。Mesh 属性中可定义多个 Root，Bridge 只能 1 个。
  tags: [mesh, bridge, wireless-backhaul, limitations, best-practice]

- id: p14
  title: Guest 隧道（GRE Tunneling）容量常数
  type: principle
  source_chapter: "p115"
  source_quote: |
    "Tunnel per Access Role Profile from Access Point to a OS6860/E or OS6900
    • L2 GRE tunnel over L2/L3 networks
    • OmniSwitch simplifies deployment with automatic tunnel creation to AP IP
    • Max 16 tunnel starts per AP
    • 6860/E →750 tunnel terminations
    • 6900 →1000 tunnel termination"
  summary: |
    Guest Tunneling（访客流量隔离）：按 Access Role Profile 建 L2 GRE 隧道，从 AP 直达汇聚/
    核心交换机（OS6860/E 或 OS6900），可跨 L2/L3 网络；OmniSwitch 支持向 AP IP 自动建立隧道。
    容量常数：每台 AP 最多发起 16 条隧道；OS6860/E 最多终结 750 条隧道；OS6900 最多终结
    1000 条。做大型访客隔离方案（如高校、场馆）时按此校核交换机数量。
  tags: [guest-access, gre-tunnel, capacity, omniswitch, security]

- id: p15
  title: 三种管理模式的 License 边界（Express 免费 5 个永久 License）
  type: principle
  source_chapter: "p128"
  source_quote: |
    "Stellar Enterprise On Premise (OmniVista 2500)
    Stellar Express No License 5 permanent licenses
    Stellar Enterprise Cloud (OmniVista Cirrus 4)"
  summary: |
    管理模式与 License 对应关系：① WiFi Express（独立模式）——无需 License，随机附 5 个永久
    License；② Stellar Enterprise On-Premise——用 OmniVista 2500 网管，需购买 OV2500 License；
    ③ Stellar Enterprise Cloud——用 OmniVista Cirrus 4，需订阅。模式定位（p41）：Express 面向
    中小网络（SMB），Enterprise 面向中大网络，Cloud 覆盖小中大；客户可按需从 Express 迁移到
    Enterprise/Cloud。报价起点判断：纯 Express 项目不产生网管软件费用。
  tags: [license, express-mode, enterprise-mode, cloud-mode, boundary, quotation]

- id: p16
  title: OV2500 License 模块清单与 Starter/Evaluation 规则
  type: principle
  source_chapter: "p131"
  source_quote: |
    "•AP License - OV2500-NG-AP ⚫Wireless support Discovery ⚫Registration ⚫Provisioning troubleshooting
    ⚫Lifecycle management ⚫Access Guardian ⚫Application visibility and WLAN Analytics
    ⚫RF management • WIDS • WiPS • Floor Plan • Heat map
    •High Availability License - OV-NMS-HA •One license per node required
    •Web Content Filtering License - OV-AP-WCF •One license for 10 Access Points"
  summary: |
    OV2500（Stellar Enterprise On-Premise）License 结构：必购——AP License（OV2500-NG-AP，含
    AP 发现/注册/开通/生命周期/Access Guardian/应用可视化/WLAN 分析/RF 管理/WIDS/WIPS/
    Floor Plan/Heat Map）；可选——Guest License（OV2500-NG-GUEST，访客认证管理与 Captive
    Portal）、On-Boarding License（OV2500-NG-ONBOARDING，BYOD）、High Availability
    （OV-NMS-HA，每个 HA 节点各需 1 个）、Web Content Filtering（OV-AP-WCF，1 个 License
    覆盖 10 台 AP）。Starter Pack（p130）：Evaluation 版 60 天免费，含 10 台 OmniSwitch、
    10 台 Stellar AP、10 个 Guest、10 个 BYOD、10 台第三方设备；Production 版按设备数生成、
    永不过期。p122：OV2500-Starter pack 免费附带 10 个 Guest + 10 个 BYOD License。
  tags: [license, ov2500, starter-pack, evaluation, module, part-number]

- id: p17
  title: OV2500 订购 License 的 Part Number 规则（OV-AP-NM-X-N 等）
  type: principle
  source_chapter: "p136"
  source_quote: |
    "• Licenses
    • AP License: OV-AP-NM-X-N • X = 10, 20, 50, 100, 500 APs
    • Guest license: OV-GA-X-N • X = 20, 50, 100, 500, 1000, 5000 or 25000 Guest users
    • On-Boarding license: OV-BYOD-X-N • X = 20, 50, 100, 500, 1000, 5000 or 25000 users
    • High Availability license: OV4-NMS-HA
    • Web Content Filtering license: OV-AP-WCF-10-N"
  summary: |
    下单用 License Part Number 编码规则（区别于 p131 的功能模块名）：AP License = OV-AP-NM-X-N，
    X 取 10/20/50/100/500 台；Guest = OV-GA-X-N，X 取 20/50/100/500/1000/5000/25000 用户；
    BYOD = OV-BYOD-X-N，档位同 Guest；High Availability = OV4-NMS-HA（单一 PN）；Web Content
    Filtering = OV-AP-WCF-10-N（每 10 台 AP 一档）。p135 对应的 OV2500-NG-* 系列数量档为
    20/50/100/500/1000。报价时按设备数/用户数向上取最近的档位。
  tags: [license, part-number, quotation, ov2500, ordering]

- id: p18
  title: AP 与配件订购命名规则（OAW-APxxxx-Region / ANT-O / ANT-S / MNT-X）
  type: principle
  source_chapter: "p136"
  source_quote: |
    "• Access Points Model • OAW-APxxxx-Region
    • xxxx = AP model (ex: 1231)
    • Region = RW (Rest of the World), JP (Japan), ME (Middle East), US (United States)"
  summary: |
    AP 型号命名规则：OAW-APxxxx-Region。xxxx=AP 数字型号（如 1231 → OAW-AP1231）；Region
    区域后缀：RW=除日/美/中东外的全球其他地区、JP=日本、ME=中东、US=美国。区域码与 p68 的
    Country Code 匹配规则联动，下单区域错会导致注册失败。配件命名（p136）：安装支架
    OAW-AP-MNT-X，X=B（T 型龙骨吊顶）/C（吊顶）/DSK（AP1201H 桌面）/W（墙面）；PoE 供电器
    PD-XXXX（查 Portfolio）；电源适配器 ADP-30HRBD 与 ADP-60GRBC；天线及馈线 ANT-O-XX
    （全向）/ANT-S-XX（定向扇区）。同一规则在 Cirrus 10 章节重复出现（p144/p167）。
  tags: [part-number, naming-rule, ap-hardware, accessories, region-code, quotation]

- id: p19
  title: 维护合约编码规则（PW/SP 前缀解码）
  type: principle
  source_chapter: "p137"
  source_quote: |
    "• Maintenance contract of 1, 2, 3 or 5 years for the following items: …
    • PW2R-OVBYOD100N: • P=Partner; W=Software support; 2=2 Years; R=(Maintenance) Renewal;
    OVBYOD=On-Boarding license; 100N=For 100 users
    • SP5N-OAWAP1201: • S=End Customer; P=(Support) Plus (with AVR); 5=5 Years; N=New (Maintenance);
    OAWAP1201= For an AP1201"
  summary: |
    维护合约（Maintenance Contract）时长可选 1/2/3/5 年，覆盖 OV2500 各 License（OV-NM/OV-AP/
    OV-GA/OV-BYOD/OV4-NMS-HA/OV-WCF 的软件支持）和 Stellar AP 硬件（OAWAPxxxx 硬件+软件
    维护）。编码解码规则：第 1 位 P=Partner（合作伙伴价）或 S=End Customer（最终客户）；
    第 2 位 W=Software support（软件支持）或 P=Support Plus 含 AVR（硬件高级更换服务）；
    数字=年数；末段 R=Renewal（续保）/N=New（新购）；中间为产品缩写+数量。示例：
    PW2R-OVBYOD100N = Partner 软件支持 2 年续保、BYOD License 100 用户；SP5N-OAWAP1201 =
    终端客户 Support Plus（含 AVR）5 年新购、AP1201。最新 WPL 以 MyPortal 为准。
  tags: [maintenance-contract, part-number, encoding, quotation, support]

- id: p20
  title: OV Cirrus 4 账号模式：Freemium vs Premium（5000 License 上限）
  type: principle
  source_chapter: "p139"
  source_quote: |
    "Freemium: Self Registration • Free of charge • No device capacity limitation • No duration limitation
    • No network Configuration • On-time Network Device Upgrade • Restricted OV Cirrus capabilities
    • Can be upgraded to Premium
    Premium: All OV Cirrus capabilities • Based on OV Cirrus Subscription
    • Flexible (Device type, capacity and Duration) • Subscription done through eBUY/OVCirrus
    • Max amount of licenses: 5000 included • Stellar APs and OmniSwitch
    • Subscription Expansion, reduction or renewal"
  summary: |
    OmniVista Cirrus 4 云管两种账号：Freemium——自助注册、免费、设备数量与时长无限制，但不能
    做网络配置、仅一次性设备升级、功能受限，可升级到 Premium；Premium——全功能，基于订阅
    （设备类型/容量/时长灵活），通过 eBUY/OVCirrus 订购，单订阅最多含 5000 个 License（覆盖
    Stellar AP 与 OmniSwitch），支持扩容、缩减、续订。免费试用或小型云管场景可先落 Freemium。
  tags: [ov-cirrus, freemium, premium, subscription, cloud-management, license]

- id: p21
  title: OV Cirrus 4 订阅规则（每 AP 1 License，附 50 Guest + 50 BYOD）
  type: principle
  source_chapter: "p140"
  source_quote: |
    "Duration of 1, 3 or 5 Years
    Service bundles: Base, Premium and Business
    - 1 license per Stellar AP (regardless the model)
    - 50 Guest licenses and 50 BYOD licenses included per AP license"
  summary: |
    OV Cirrus 4 订阅结构：按设备类型分 LAN Core（OS6900）、LAN Essential（OS6350/6450/6465/
    6560）、LAN Advanced（OS6860/6860E/6865）和 Stellar AP；Stellar AP 无论型号每台 1 个
    License；每个 AP License 免费附送 50 个 Guest + 50 个 BYOD License（与 OV2500 Starter
    的 10+10 形成对比，云管附送额度更大）。时长 1/3/5 年。服务包三档（p141）：Base——仅
    SaaS 网管+固件升级+应用本身 TAC，不含设备 TAC/支持门户/AVR 硬件服务（可另购设备单独
    支持合同）；Business（面向合作伙伴）与 Premium（面向终端客户）——含设备 TAC、Support
    Portal、Global Welcome Center 及全部授权设备的 AVR-NBD 硬件服务。
  tags: [ov-cirrus, subscription, license, service-bundle, guest, byod, quotation]

- id: p22
  title: OV Cirrus 4 订购 Part Number（OVC-AP-BAS/BIZ/XY）
  type: principle
  source_chapter: "p144"
  source_quote: |
    "• Ordering through eBuy/eSR
    • One Stellar AP license per AP:
    • OVC-AP-BAS-XY : Base Bundle for X = 1, 3 or 5 years
    • OVC-AP-BIZ-XY: Business Bundle for X = 1, 3 or 5 years
    • OVC-AP-XY: Premium Bundle for X = 1, 3 or 5 years"
  summary: |
    Cirrus 4 时代 Stellar AP 云管订阅下单规则：每台 AP 一个 License，Part Number 为
    OVC-AP-BAS-XY（Base 包）、OVC-AP-BIZ-XY（Business 包）、OVC-AP-XY（Premium 包，注意
    Premium 无服务档位中缀），Y 固定，X=1/3/5 年。订购渠道 eBuy/eSR；AP 硬件仍按
    OAW-APxxxx-Region（RW/JP/ME/US）下单。订购与激活三步（p142）：① Freemium 账号自注册
    （registration.ovcirrus.com）；② eBuy/eSR 下单；③ 在 OVC Subscription Manager
    （licensemanager.al-enterprise.com）创建订阅，回 Cirrus 输入订阅号+激活码激活。
    注意此为旧版规则，Cirrus 10 已改为 OVCX- 编码（见 p153）。
  tags: [ov-cirrus, part-number, subscription, ordering, ebuy]

- id: p23
  title: OmniVista Cirrus 10 License 编码：OVCX-[Category]-[Level]-[Duration] 共 63 个 PN
  type: principle
  source_chapter: "p153"
  source_quote: |
    "OVCX-68-BAS-3Y = OmniVista Cirrus X (=10) license
    • License category: • Low end Stellar models: APL • High end Stellar models: APH
    • OmniSwitch 63xx model: 63 • OmniSwitch 64xx model: 64 • OmniSwitch 65xx model: 65
    • OmniSwitch 68xx model: 68 • OmniSwitch 69xx model: 69
    • License level: • BASE level : BAS • BUSINESS level : BIZ • PREMIUM level : PRM
    • License duration • 1 year : 1Y • 3 years : 3Y • 5 years : 5Y
    Total number of license part numbers: 7 x 3 x 3 = 63 part numbers"
  summary: |
    Cirrus 10 订阅 License 编码规则：OVCX-[Category]-[Level]-[Duration]，X=10。三个维度：
    ① 类别 7 种——APL（低端 Stellar AP）、APH（高端 Stellar AP）、63/64/65/68/69（对应
    OmniSwitch 63xx/64xx/65xx/68xx/69xx）；② 等级 3 种——BAS/BIZ/PRM；③ 时长 3 种——
    1Y/3Y/5Y。合计 7×3×3=63 个 Part Number。类别判定细则（p154）：APL 覆盖 AP1x0x（1201、
    1301/1301H）、AP1x1x（1311、1411、1511）、AP1x2x（1221、1321、1322、1521）等；APH 为
    其余全部型号——例：AP1431 → OVCX-APH-xxx-nY，OS6860N-P24Z → OVCX-68-xxx-nY。每设备
    一个 License；续订/扩展在 ALE Subscription Manager 操作；示例 OVCX-64-BIZ-1Y（p167）。
    支持设备范围（p166）：全部 Stellar AP（AP1101、AP1201H/L/LH 除外）+ 运行 8.9Rx 的
    OmniSwitch。
  tags: [ov-cirrus, cirrus10, part-number, license, subscription, encoding, quotation]

- id: p24
  title: Cirrus 10 三档服务（BAS/BIZ/PRM）能力差异表
  type: principle
  source_chapter: "p155"
  source_quote: |
    "Services: OV CIRRUS 10 Base / OV CIRRUS 10 Business / OV CIRRUS 10 Premium
    OV CIRRUS 10 access and support: Yes / Yes / Yes
    Software and firmware update for managed device: Only software upgrade, limited to the available version in OVC10 / Yes / Yes
    OmniVista Cirrus 10 - TAC access: Not Available / For Partner / For End Customer
    Hardware service (advanced replacement) and support: Not Available, sold separately / For Partner / For End Customer"
  summary: |
    Cirrus 10 三档订阅差异：Base——可访问与使用 OVC10，但设备软件/固件更新仅限 OVC10 内可用
    版本的软件升级，无 TAC 支持，硬件高级更换服务需单独购买；Business——面向合作伙伴
    （Partner），含完整软件固件更新、Partner TAC、硬件服务；Premium——面向终端客户
    （End Customer），权益同 Business 但 TAC 与硬件服务直接给最终客户。向客户推荐档位时
    按"谁来找 TAC、要不要硬件更换服务"决策。
  tags: [ov-cirrus, cirrus10, service-level, tac, hardware-service, comparison]

- id: p25
  title: USB ESL 电子价签方案规则（零售连锁，Hanshow USB Dongle）
  type: principle
  source_chapter: "p197"
  source_quote: |
    "▪Stellar AP: USB type A or type C (female) port. Activation of the Stellar AP USB port.
    ▪ESL USB dongle: USB type C (male) port. USB cable to interface both devices.
    ▪Hanshow solution. Two types of transmitters available:
    ▪Proprietary ESL transmitter -> Not selected. Because new deployment (wiring, device installation) required.
    ▪Proprietary ESL USB dongle -> Selected. To be connected to the existing Stellar infrastructure. Minimal impact for deployment."
  summary: |
    零售 ESL（Electronic Shelf Label，电子 shelf 价签）方案规则：Stellar AP 提供 USB Type A
    或 Type C 母口，需在 AP 上激活 USB 口；选 Hanshow USB ESL Dongle（Type C 公头，经 USB 线
    连 AP）。两种发射器选型结论——独立专有 ESL 发射器需重新布线安装设备，未被选择；USB
    Dongle 直接复用现有 Stellar 基础设施、部署影响最小，被选择。技术细节（p198）：Dongle 由
    AP USB 口供电，用 2.4GHz 专有射频与 ESL 价签通信，同时连 Hanshow 云做管理配置；AP 可在
    Express 或 Cloud（OmniVista Cirrus）模式管理，需互联网访问 OV Cirrus 与 Hanshow 云；
    SSID 可广播 2.4/5/6GHz。ESL 市场技术路线（p196）：低频 38.4kHz、红外、高频 2.4MHz 多种
    波长方案并存。案例背景：40+ 门店、150 台 AP（AP1301/1311/1251）由 Cirrus 10 管理。
  tags: [esl, retail, usb, iot, hanshow, use-case, selection]

- id: p26
  title: VoWLAN 语音终端兼容性最低要求（iOS 8 / Galaxy S7 / S9 支持 11v）
  type: principle
  source_chapter: "p203"
  source_quote: |
    "• Voice applications: • Rainbow UCaaS client • Rainbow mobility with OXO/OXE integration
    • OTC mobile application • Non-ALE softphones applications (Facetime,…)
    • Roaming assistance with 802.11r/k/v protocols
    • iOS 8 and above • Samsung Galaxy S7 minimum • S9 minimum for 802.11v"
  summary: |
    手机/笔记本软终端语音规则：语音应用包括 Rainbow UCaaS 客户端、Rainbow 与 OXO/OXE 集成、
    OTC 移动应用及非 ALE 软电话（Facetime 等）；漫游辅助依赖 802.11r/k/v。终端最低要求：
    iOS 8 及以上；安卓 Samsung Galaxy S7 起步；要支持 802.11v 需 S9 起步。语音质量随终端
    硬件/操作系统差异而变化，售前评估 BYOD 语音时要先盘终端型号。专用话机（p202）走
    ALE NOE 与 SIP 标准协议（8118/8128/8158s/8168s，Ascom 系列）。
  tags: [vowlan, voice-devices, compatibility, 802.11r, rainbow, byod]

- id: p27
  title: VoWLAN 覆盖设计常数（1 AP / 255m²，20-25 用户/AP）
  type: principle
  source_chapter: "p207"
  source_quote: |
    "• Requirements for Voice
    • 1 access point / 255 m²
    • Number of users per AP – Average of 20-25 users"
  summary: |
    语音覆盖（Prepare 阶段）可背诵常数：语音业务按每 255 平方米 1 台 AP 规划覆盖；每台 AP
    平均承载 20-25 个并发用户。准备阶段动作：现场勘查（Site Survey）、分析 RF 环境、找出
    干扰源及其强度、计算 AP 数量与布放位置（结合 5GHz 发射功率与蜂窝半径/重叠设计，图示
    参考电平 -60dBm/-70dBm），并为高可用区域（如前台接待）规划多 AP 冗余覆盖。这是语音
    项目 AP 数量快速估算的基准公式。
  tags: [vowlan, rf-design, coverage, capacity, site-survey, constants]

- id: p28
  title: VoWLAN 规划参数（5GHz 优先、36Mbps 吞吐、-62dBm 漫游阈值）
  type: principle
  source_chapter: "p208"
  source_quote: |
    "• RF Management • 5GHz prefered (robust, best performance)
    • Capacity planning • 20 to 25 clients per Aps, providing 36 Mbps user throughput
    • Roaming: • Activate the roaming options supported by the devices.
    • Plan dedicated SSIDs for devices sharing the same capacities
    • Generally a -62dBm RSSI (or better) is required to ensure a correct roaming"
  summary: |
    VoWLAN Plan 阶段核心参数：RF 管理首选 5GHz（更稳健、性能最佳）；容量规划按每 AP 20-25
    个客户端、为用户提供 36Mbps 吞吐；漫游设计——激活终端支持的漫游选项（802.11r/k/v，
    见 p26 终端门槛）、为能力相近的终端规划专用 SSID、蜂窝边缘 RSSI 一般需达到 -62dBm 或更
    好才能保证正确漫游；同时要求 AP 侧网络可靠冗余。Design 阶段（p209）配套规则：相邻 AP
    用非重叠信道（信道选择依国家码）、为语音设计 WMM QoS 策略（语音实时流量高优先级、协作
    应用尽力而为）、DSCP/802.1p 打标贯穿无线-边缘-核心、语音单独 VLAN 并保证带宽、
    802.11ac 吞吐要求接入交换机千兆用户端口，可选 Stellar DPI 做语音应用强制管控。
  tags: [vowlan, roaming, rssi, capacity, qos, 5ghz, constants]

- id: p29
  title: 酒店客房 AP 数量公式：M/2 + N + (M+N)×5%
  type: principle
  source_chapter: "p243"
  source_quote: |
    "• AP quantity = M/2+N+(M+N)*5%
    Explanation: • M: number of rooms with normal walls • N: number of rooms with load-bearing wall
    • 5%: represents the redundant backup
    Example: 20 rooms M, 10 rooms N • AP quantity = 21,5. Rounded up to 22 AP1301H"
  summary: |
    高密度同构房间（酒店/病房/宿舍/办公室，每间 2-4 人、最多 10 个无线终端）AP 数量公式：
    AP 数 = M/2 + N + (M+N)×5%。M=普通隔墙房间数（两间共用 1 台 AP，隔间部署）；N=承重墙
    房间数（每间 1 台 AP）；5% 为冗余备份。示例：20 间普通墙 + 10 间承重墙 = 21.5，向上取
    整 22 台 AP1301H。墙体衰减常数（p244/245）：普通墙 15dB、承重墙 30dB；AP1301H 最大发射
    功率 21dBm（2.4/5GHz），天线增益 2.4G=4dB、5G=6dB；无承重墙时隔间部署最差处约
    -65dBm 可用；有承重墙若仍隔间部署，5GHz 掉到 -80dBm 无法接入、2.4GHz -70dBm 极差，
    故必须每间 1 台。安装要求（p246/p260）：壁挂高度 1.5 米（5 英尺）及以上，避开电视、
    显示器、金属架等衰减遮挡物，不可装在承重墙侧面。
  tags: [hospitality, ap-sizing, formula, wall-attenuation, deployment, constants]

- id: p30
  title: 酒店客房推荐配置清单（RSSI 20/15、HT20、限速 2/4Mbps）
  type: principle
  source_chapter: "p247"
  source_quote: |
    "RSSI Threshold: 2.4G RSSI :20 / 5G RSSI :15 — Roaming RSSI: 2.4G RSSI :20 / 5G RSSI :15
    ACS: Enable — APC: Disable
    Bandwidth setting: HT20 for 2.4G / HT20 for 5G
    Band steering: Enable — Traffic limitation: 2mbps for upload / 4mbps for download
    BG-S: Disable — Load Balance: Enable — Voice/Video awareness: Disable — ATF: Disable"
  summary: |
    客房场景推荐配置（可背清单）：RSSI 门限 2.4G=20、5G=15；漫游 RSSI 同值（引导终端连
    最近 AP）；ACS 自动选信道开（动态选最优信道、降低维护复杂度）；APC 自动功率控关
    （封闭独立环境建议手工调功率）；带宽 2.4G/5G 都用 HT20（无大流量需求时提升信道隔离、
    降低 AP 间干扰）；Band Steering 开（优先引导 5G）；单终端限速上行 2Mbps/下行 4Mbps
    （防单用户占满带宽）；BG-S（后台扫描）关——除非需要 WIPS/APC/快速漫游；Load Balance
    开（AP 间负载均衡）；Voice/Video awareness 关（因 BG-S 已关）；ATF 关（未装 AP 的房间
    体验会受损）。
  tags: [hospitality, recommended-config, rssi, acs, band-steering, traffic-limit]

- id: p31
  title: 高密度场馆容量估算与部署参数（750 并发 / 8-10 AP / 1-6-11 信道）
  type: principle
  source_chapter: "p249"
  source_quote: |
    "• Venue capacity: 1500. Estimated concurrent users: less the 50% →Around 750 active users
    • Wifi 6 AP1321: Three RF card (2.4G 4x4 + 5G 4x4 + full band scanning) & 2.5Gbps ethernet port.
    • Number of APs: 8-10
    [p251] • 2.4GHz: use channels 1 – 6 - 11 • Reduce internal interference at 2.4GHz
    • 2.4GHz turned off on some APs • Prevent co-channel interferences"
  summary: |
    高密度室内场馆（展厅、室内体育馆）容量估算：按场馆容量×并发率估算，例：1500 人场馆、
    并发约 50% → 约 750 活跃用户 → 部署 8-10 台三射频 AP（Wi-Fi 5 AP1231：2.4G 4x4 + 5G
    低频 4x4 + 5G 高频 4x4；或 Wi-Fi 6 AP1321：2.4G 4x4 + 5G 4x4 + 全频扫描），均配 2.5G
    以太口。部署要点：安装优先吊顶（天花板高、容量大场景），备选壁挂（p250）；网络侧推荐
    2.5Gbps 上联口、交换机支持 802.3bt PoE、接入端口 2.5G 防有线侧瓶颈（如 OmniSwitch
    6560）（p251）；2.4GHz 只用 1/6/11 三个非重叠信道，部分 AP 直接关闭 2.4GHz 防同频干扰。
    发射功率参考（p250）：AP1231 最大 24dBm，AP1321 为 20dBm(2.4G)/24dBm(5G)。Wi-Fi 6 高
    密度补充（p254/256）：利用 OFDMA/MU-MIMO/1024-QAM/TWT；屋顶不超过 5 米用吊顶安装、
    房间宽度不超过 30 米用壁挂安装。
  tags: [high-density, venue, ap-sizing, channels, capacity, wifi6, deployment]

- id: p32
  title: 高密度场馆推荐配置清单（RSSI 30/30、功率≤15dBm、HT40、GI 0.8/1.6us）
  type: principle
  source_chapter: "p252"
  source_quote: |
    "RSSI Threshold: 2.4G RSSI :30 / 5G RSSI :30
    Roaming RSSI: 2.4G RSSI :30 / 5G RSSI :35
    ACS: Disable — APC: Disable (It is recommended that the AP's transmission power not be higher than 15 dBm)
    Bandwidth setting: HT20 for 2.4G / HT40 for 5G
    Force to 5GHz: Enable — Traffic limitation: 2mbps for upload / 4mbps for download
    Short Guard Interval: Disable … configured to 0.8us for Wi-Fi 5 AP, and 1.6 us for Wi-Fi 6 AP"
  summary: |
    高密度场馆推荐配置（对照客房清单记忆）：RSSI 门限 2.4G=30、5G=30（踢出弱信号终端保
    体验）；漫游 RSSI 2.4G=30、5G=35；ACS 关——封闭独立环境 AP 不多，建议手工指定信道以保
    最佳性能（与客房相反）；APC 关但发射功率手工控制不超过 15dBm；带宽 2.4G 用 HT20、5G 用
    HT40（提升信道隔离）；Band Steering 与强制 5GHz 都开；限速上行 2Mbps/下行 4Mbps；BG-S 关、
    Load Balance 开、Voice/Video awareness 关；Short GI 关——多径明显时短 GI 会引发码间干扰
    与重传，GI 取值 Wi-Fi 5 AP 配 0.8us、Wi-Fi 6 AP 配 1.6us。
  tags: [high-density, recommended-config, rssi, acs, guard-interval, force-5ghz]

- id: p33
  title: 中小会议室 AP 数量对照表与配置（40-60 客户端 1 台起）
  type: principle
  source_chapter: "p258"
  source_quote: |
    "Room type / Number of clients / Recommended AP / Number of APs:
    Small room 40-60 AP1231/1321 1
    Medium room 80-120 AP1231/1321 2
    Lecture hall / Conference room 160-200 AP1231/1321 4
    • Estimated concurrent users: 100%. All clients require at least 2Mbps of bandwidth."
  summary: |
    中小规模房间（办公室、教室、阶梯教室、会议室，高密度+高流量应用）AP 数量速查表：小房间
    40-60 客户端 → 1 台 AP1231/1321；中房间 80-120 → 2 台；阶梯教室/大会议室 160-200 →
    4 台。假设并发率 100%，每客户端至少 2Mbps 带宽。安装（p259/260）：任何房间优先吊顶，
    备选壁挂；壁挂高度须大于 1.5 米、让所有终端可见 AP，禁止装得过低或装在承重墙侧面（信号
    急剧衰减）。推荐配置（p261）：RSSI 门限与漫游 RSSI 均 2.4G=30、5G=30；ACS 开、APC 关但
    发射功率手工调至不超过 10dBm（降低邻间干扰）；带宽 2.4G 用 HT20、5G 用 HT80（高并发+
    固定高流量场景提升 AP 容量）；Band Steering 与强制 5G 开；限速 2/4Mbps；BG-S 关、
    Load Balance 开。
  tags: [meeting-room, ap-sizing, recommended-config, rssi, ht80, classroom]

- id: p34
  title: 户外 AP 部署规则（并发 20%、6-8 台 AP1361、抱杆最高点）
  type: principle
  source_chapter: "p263"
  source_quote: |
    "• Outdoor deployment. Medium to large scale coverage. Low/medium density of clients.
    • Estimated concurrent users: 20% →Around 200 concurrent users estimated
    • Solution: • Wifi 6 - AP1361: • Number of APs: 6-8
    [p265] • In open areas, without buildings in proximity: AP mounted on a pole – the highest possible
    • A PoE switch – supporting 802.3at standard – used as power supply"
  summary: |
    户外场景（度假村、露营地、码头、公园、仓库装卸区、工厂等恶劣环境，覆盖中大规模、客户端
    低中密度）部署规则：并发率按 20% 估算（例：约 200 并发用户）；选用 Wi-Fi 6 户外三防
    AP1361（工作温度 -40~+65°C），约 6-8 台。安装（p264/265）：有建筑物（体育场、仓库装卸
    月台、主楼）时优先吊顶、否则壁挂；开阔无建筑区域用抱杆安装且尽量装在最高点；供电用
    支持 802.3at 标准的 PoE 交换机；规划时要把树木、墙体等自然障碍物计入覆盖计算。
  tags: [outdoor, ap1361, deployment, poe, capacity, site-survey]

- id: p35
  title: OmniVista Network Advisor 定价与许可规则（AP $50/年、SW $100/年）
  type: principle
  source_chapter: "p231"
  source_quote: |
    "OmniVista Network Advisor offer, consists of one license per network device (IP Address):
    NETAD-AP-1Y Network Advisor - 1 year subscription for one OmniAccess Stellar Access Point 50 USD 48 EURO
    NETAD-SWITCH-1Y Network Advisor - 1 year subscription for one OmniSwitch 100 USD 96 EURO
    NETAD-TP-1Y Network Advisor - 1 year subscription for one Third-Party Device 100 USD 96 EURO
    NETAD-AP-3Y … 100 USD / NETAD-SWITCH-3Y … 200 USD / NETAD-TP-3Y … 200 USD
    NETAD-AP-5Y … 150 USD / NETAD-SWITCH-5Y … 300 USD / NETAD-TP-5Y … 300 USD"
  summary: |
    Network Advisor（AI 网络运维伴侣，独立服务，不需要 OV Cirrus/2500）定价常数（牌价，
    1 欧元≈1.04 美元档）：AP 每台 $50/1Y、$100/3Y、$150/5Y（€48/€96/€143）；OmniSwitch 与
    第三方设备每台 $100/1Y、$200/3Y、$300/5Y（€96/€191/€286）。按每个网络设备（每个 IP
    地址）1 个 License 计费，License 原生包含软件、管理应用与 Companion Service（Rainbow）。
    支持范围（p230）：OS 6xxx/9xxx 需 AOS 8.7.R2+，OS 2xxx 需 AOS 5.2.R1+，Stellar AP 需
    AWOS 4.0.3 MR-3+；虚拟机自备（四核 CPU、8GB 内存、50GB 硬盘）。许可生命周期（p232）：
    时长自激活起递减，附 30 天宽限期，到期前后有通知。报价示例（p233）：50 台 AP + 21 台
    交换机 1 年 ≈ €4,416，约占整网成本 1.8%；单实例上限 2000 台网络设备。订购走 eBuy，
    类目：Products > Network Products > Network Management > OmniVista Network Advisor。
  tags: [network-advisor, pricing, license, ai-ops, quotation, part-number]
