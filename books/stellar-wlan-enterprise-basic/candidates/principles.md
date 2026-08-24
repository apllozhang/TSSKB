# 原则/参数 · OmniAccess Stellar WLAN Enterprise Basic (DT00XTE368EN)

> 来源：source/fulltext.md（页码即教材 PDF 页码）

- id: p01
  title: 802.11 标准演进参数总表（速率/频段/年份）
  type: principle
  source_chapter: "p24"
  source_quote: |
    "802.11: 1997, 2 Mbps, 2.4 GHz. 802.11b: 1999, 11 Mbps, 2.4/5 GHz. 802.11a: 1999, 54 Mbps, 5 GHz. 802.11g: 2003, 54 Mbps, 2.4 GHz. 802.11n (HT): 2009, 600 Mbps, 2.4/5 GHz. 802.11ac (VHT): 2014, 6.9 Gbps, 5 GHz. 802.11ax (HE): 2021, 9.6 Gbps, 2.4/5/6 GHz. 802.11be: 2024, 46 Gbps, 2.4/5/6 GHz."
  summary: |
    802.11 修正案的基准参数：原始 802.11（1997，2 Mbps，2.4 GHz）→ b（1999，11 Mbps）→ a（1999，54 Mbps，5 GHz）→ g（2003，54 Mbps）→ n/HT（2009，600 Mbps）→ ac/VHT（2014，6.9 Gbps，仅 5 GHz）→ ax/HE（2021，9.6 Gbps，新增 6 GHz）→ be（2024，46 Gbps）。同页给出 WiFi 联盟商品名对照：802.11be=WiFi 7（2024）、ax=WiFi 6（2019/2021）、ac=WiFi 5（2013）、n=WiFi 4（2007）。802.11 是 IEEE 标准，Wi-Fi 是联盟的互操作认证品牌。

  tags: [802.11, standards, data-rate, spectrum, wifi-generations]

- id: p02
  title: WiFi6E 的三大卖点（容量/可靠性/安全）
  type: principle
  source_chapter: "p26-28"
  source_quote: |
    "Capacity: Up to 60 contiguous Channels Available in the 6 Ghz Bands, 60 X 20 MHz, 29 X 40 MHz, 14 X 80 MHz, 7 X 160 MHz. Reliability: Greenfield... Security: Use the latest security methods, Disallow outdated legacy protocols, Require use of Protected Management Frames (PMF)."
  summary: |
    6E 的价值主张三条：容量——6 GHz 连续 1200 MHz 频谱可容纳 60 个 20 MHz / 29 个 40 MHz / 14 个 80 MHz / 7 个 160 MHz 信道；可靠性——6 GHz 是 WiFi 的 Greenfield（全新绿地）频段，不要求向下兼容 a/b/g/n/ac 老协议，没有同频退避包袱；安全——强制使用最新安全方法、禁用过时遗留协议、强制 PMF（受保护管理帧）。向客户解释"为什么要上 6E"就用这三条。

  tags: [wifi6e, 6ghz, capacity, greenfield, pmf]

- id: p03
  title: 2.4/5/6 GHz 信道资源清单
  type: principle
  source_chapter: "p36-38"
  source_quote: |
    "2.4 GHz: 3 Channels Allocated, 20 MHz, 60 MHz spectrum... 5 GHz: 25 Channels Allocated, 20 MHz, 500 MHz spectrum: 12 x 40 MHz, 6 x 80 MHz, 2 x 160 MHz... 6 GHz: Greenfield band for WiFi. Backwards compatibility not required. 60 Channels Available: 60 x 20 MHz, 29 x 40 MHz, 14 x 80 MHz, 7 x 160 MHz, 1200 MHz."
  summary: |
    三个频段的信道账本：2.4 GHz 总共 60 MHz，只能放 3 个不重叠 20 MHz 信道（2.412-2.484 GHz），但留作兼容老终端、恶劣环境和低成本场景；5 GHz 共 500 MHz，25 个 20 MHz、12 个 40 MHz、6 个 80 MHz、2 个 160 MHz（5170-5835 MHz，受 DFS 约束）；6 GHz 共 1200 MHz，60 个 20 MHz（或 29/14/7 个更宽信道），无需向后兼容。做高密设计时信道数直接决定复用模式，6 GHz 的容量优势即来源于此。

  tags: [channels, 2.4ghz, 5ghz, 6ghz, spectrum]

- id: p04
  title: WiFi5 与 WiFi6E 关键差异对照
  type: principle
  source_chapter: "p29"
  source_quote: |
    "WiFi 6e (802.11ax): Multi-user support (OFDMA); 8 AP Spatial streams; 2.4GHZ, 5 GHz & 6 Ghz band; 9.6 Gbps Max data rate; Uplink & Downlink MU-MIMO. WiFi 5 (802.11ac): Single-user support (OFDM); 4 AP spatial streams; 5 GHz frequency band; 6.9 Gbps Max data rate; Downlink MU-MIMO."
  summary: |
    新老两代的核心差异：WiFi 6E 用 OFDMA 支持多用户并行（WiFi 5 的 OFDM 单用户）、空间流从 4 条扩到 8 条（MU-MIMO 从仅下行升级为上/下行双向）、频段从仅 5 GHz 扩到 2.4/5/6 GHz、峰值速率 9.6 Gbps 对 6.9 Gbps。p31 补充 MU-MIMO 规格从 WiFi 5 的 4x4 仅下行变为 WiFi 6 的 8x8 上/下行。给客户做代际升级论证时直接引用这张对照表。

  tags: [wifi5, wifi6e, ofdma, mu-mimo, comparison]

- id: p05
  title: MU-MIMO 与 OFDMA 的适用场景分工
  type: principle
  source_chapter: "p33"
  source_quote: |
    "MU-MIMO: Improve the capacity; Increase the rate of each user; Most suitable for high bandwidth applications; Most suitable for large-packet transmission. OFDMA: Improved the efficiency; Reduced latency; Most suitable for low bandwidth applications; Most suitable for small packet transmissions."
  summary: |
    WiFi 6 两大并行技术的选型原则：MU-MIMO 靠波束赋形在空间上分流，提升总容量和单用户速率，适合高带宽、大包业务（如视频下载）；OFDMA 把信道切成多个资源单元（RU）给多终端同时收发，提升效率和时延，适合低带宽、小包业务（如 IoT、语音、信令）。实际网络两者叠加使用，理解分工才能解释"为什么换了 WiFi 6 语音时延和 IoT 密集场景改善明显"。

  tags: [mu-mimo, ofdma, use-case, wifi6]

- id: p06
  title: 1024-QAM 单流速率提升 25%
  type: principle
  source_chapter: "p34"
  source_quote: |
    "Quadrature amplitude modulation (QAM) is a modulation scheme that results in a denser constellations to increase data rates. This is done by varying the amplitude and the phase of the signal. More bits per hertz, 25% data rate increase of a single spatial stream... each symbol transmits 10-bit data (WiFi 6) vs 8-bit (WiFi 5)."
  summary: |
    WiFi 6 的调制升级：1024-QAM 通过更密的星座图让每个符号携带 10 bit（WiFi 5 的 256-QAM 为 8 bit），单条空间流速率提升 25%。代价是对信噪比要求更高，只有在信号足够好时才能跑到最高阶调制。后续 WiFi 7 用 4096-QAM 再加 20% 原始速率（见 p204），思路一脉相承。

  tags: [qam, modulation, data-rate, wifi6]

- id: p07
  title: 6 GHz 室外功率规则（AFC 与 LPI/VLP 等级）
  type: principle
  source_chapter: "p44"
  source_quote: |
    "Standard-Power AP (AFC Controlled): 36 dBm... Low-Power AP (indoor only): 30 dBm... Client Connected to Low-Power AP: 24 dBm. LPI: 23 dBm, 10 dBm/MHz. VLP: 14 dBm, 1 dBm/MHz... EU and RW prohibit using 6GHz band Outdoors for Standard Power APs. FCC approved 7 AFC providers."
  summary: |
    6 GHz 室外/室内功率分级（监管红线）：FCC 域标准功率 AP 及其固定客户端需经 AFC（自动频率协调）控制，EIRP 上限 36 dBm，标准功率 AP 下客户端 30 dBm；低功率室内 AP（LPI，必须有有线供电、内置天线、非电池）30 dBm、其客户端 24 dBm；EU 域 LPI 为 23 dBm/10 dBm/MHz，VLP（便携设备，室内外均可但禁道路车辆与无人机）14 dBm/1 dBm/MHz。EU 及多数地区禁止标准功率 AP 在 6 GHz 室外使用；FCC 批准了 7 家 AFC 服务商（Qualcomm、Federated Wireless 等）。部署 6E 室外链路前必须先核对本地区适用等级。

  tags: [6ghz, afc, eirp, lpi, vlp, regulation]

- id: p08
  title: WiFi7 关键技术参数（320 MHz/4096-QAM/16x16/MLO）
  type: principle
  source_chapter: "p204-205"
  source_quote: |
    "4096-QAM: +20% raw speed increase. Wider Channel Bandwidth: 320 MHz, 46 Gbps vs. 9.6 in Wi-Fi 6E. MU-MIMO up to (16x16:16). Multi-Link Operation (MLO): Reliability, Efficiency & Performance. Channel width: up to 320 MHz. Security: WPA 3. Power Saving: TWT, RTWT."
  summary: |
    WiFi 7（802.11be）的性能清单：信道带宽最高 320 MHz、4096-QAM（比 WiFi 6E 原始速率 +20%）、MU-MIMO 最高 16x16、多链路操作 MLO、多资源单元 MRU、前导码穿孔（Preamble Puncturing）、AFC 协调机制、峰值 46 Gbps。世代对比表（p205）：WiFi 4/5/6/6E/7 的信道宽度 20-40/20-160/20-160/最高 320 MHz，调制 64-QAM→4096-QAM，安全从 WPA2 升到 WPA3，省电从 TWT 到 RTWT。WiFi 7 认证就绪于 2023 Q4，标准终稿 2024 H1。

  tags: [wifi7, 802.11be, mlo, 320mhz, 4096-qam]

- id: p09
  title: 天线三大类型与选型原则
  type: principle
  source_chapter: "p49-53"
  source_quote: |
    "OMNIDIRECTIONAL: RF Signal > Equal in all directions; Point to Multipoint; Short Distance. Example: Dipole. SEMI-DIRECTIONAL: RF Signal > Specific Direction; Point-to-Point Communication; Short to Medium Distance. Examples: Patch/Panel, Yagi. HIGHLY-DIRECTIONAL: RF Signal > Very Specific Direction; Long Distance. Example: Grid."
  summary: |
    按辐射图选天线的速查规则：全向天线（偶极子，AP 内置默认）各方向能量均等，适合点对多点、短距离覆盖；半定向天线（Patch/Panel 板状、Yagi 八木）能量集中一个方向，适合点对点中短距无线桥接；高定向天线（Grid 栅格）方向性极强，适合长距离点对点链路。Stellar AP 默认内置全向天线，型号尾号为"2"（如 AP1322/AP1362）才支持外接天线；换外接天线可控制能量分布/覆盖形状，但必须复核不超过所在国法定功率限值（p138）。

  tags: [antenna, radiation-pattern, selection, omnidirectional, directional]

- id: p10
  title: 无线安全协议演进参数（WEP→WPA→WPA2→WPA3）
  type: principle
  source_chapter: "p63-66"
  source_quote: |
    "WEP: Rivest Cipher 4 (RC4), 40-BIT KEY + 24-BIT IV or 104-bit key... TOO WEAK, NEVER USE WEP ON SITE. WPA: RC4 + TKIP; PSK (Personal) or 802.1X/EAP (Enterprise). WPA2: AES-CCMP; PSK or 802.1X/EAP. WPA3: SAE (Personal) | 802.1X-EAP (Enterprise); AES-128 (Personal) | AES-192 (Enterprise); PMF (MANDATORY)."
  summary: |
    安全协议四代参数：WEP 用 RC4+40/104 位密钥加 24 位 IV，已彻底失守（现场禁用）；WPA 过渡方案 RC4+TKIP，认证分 Personal（PSK）与 Enterprise（802.1X/EAP）两型；WPA2 换 AES-CCMP 加密，认证仍分 PSK/802.1X；WPA3 Personal 用 SAE 替代 PSK、Enterprise 可选 AES-192，PMF 成为强制项。给 SSID 选安全级别就是在这条演进线上按终端兼容性取"最新可用"的那档。

  tags: [security, wep, wpa, wpa2, wpa3, tkip, ccmp]

- id: p11
  title: WPA3 的 SAE 与 CNSA 规则
  type: principle
  source_chapter: "p295"
  source_quote: |
    "WPA/WPA2-Personal PSK replaced by WPA3-Personal SAE (Simultaneous Authentication of Equals): Stronger Encryption Key (128 bits), Offline dictionary attack resistance, No additional complexity to connect. Optional 192-bit security mode (CNSA option): CNSA enabled: Only wpa3 client authorized on the SSID; CNSA disabled: wpa2 or wpa3 clients authorized. CNSA option not enabled on AP1101 only."
  summary: |
    WPA3 落地细节：Personal 场景 PSK 被 SAE 取代——密钥加强到 128 位、可抗离线字典攻击、用户连接操作复杂度不增加；Enterprise 场景可选 192 位 CNSA 模式，开启后 SSID 只允许 WPA3 客户端（混合终端网络要慎开），关闭则 WPA2/WPA3 客户端都能接入；AP1101 是唯一不支持 CNSA 选项的型号。所有 Stellar AP 软件升级后均支持 WPA3。

  tags: [wpa3, sae, cnsa, 192-bit, compatibility]

- id: p12
  title: 认证方式信任等级与取舍
  type: principle
  source_chapter: "p294"
  source_quote: |
    "Open + Captive Portal: Cons: No Security; Pros: any type of device can be authenticated. MAC authentication: Cons: MAC can be spoofed, no traffic encryption; Pros: Available for basic wireless devices (printers, scanners). PSK: Pros: Easy set up; Cons: all keys can be hacked or stolen (key shared by all users). 802.1X: Pros: Strongest security, ease of Management, scalability; Cons: More configuration during initial setup."
  summary: |
    SSID 认证方式的选型权衡表（信任等级从低到高）：Open+门户——无加密但任何设备都能过门户认证；MAC 认证——可被仿冒且不加密流量，只适合打印机/扫描仪等哑终端；PSK——部署简单但全网共享密钥易泄露；802.1X——安全性最强、管理扩展性好，代价是初期要搭 RADIUS/UPAM 与用户库。企业员工网用 802.1X，访客网用门户+后置策略，哑终端用 MAC，是教材隐含的推荐组合。

  tags: [authentication, 802.1x, psk, mac-auth, captive-portal]

- id: p13
  title: Ekahau 材质衰减常数表（墙/窗/门 dB 值）
  type: principle
  source_chapter: "p113-115"
  source_quote: |
    "Wall, Brick (10dB); Wall, Cinder Block (5dB); Wall, Concrete (12dB); Wall, Dry (3dB); Wall, Dry Hollow (2dB). Window, Interior (1dB); Window, Thick (3dB). Solid Wood Door 6 dB; Hollow Wood Door 4 dB; Office Door w/Window 4 dB; Steel Fire/Exit Door 13 dB / 19 dB; Steel Rollup Door 11 dB. The survey tool makes its measurements with the doors closed."
  summary: |
    预测勘测画图时给障碍物赋的衰减值：内墙——砖 10 dB、砌块 5 dB、混凝土 12 dB、石膏板 3 dB、空心石膏 2 dB；窗——室内窗 1 dB、厚窗 3 dB；门——实木 6 dB、空心木 4 dB、带窗办公室门 4 dB、钢质防火/疏散门 13/19 dB、卷帘门 11 dB。注意勘测工具按"门全关"的保守口径计算。配合 p136 的现场经验（金属吸波、电梯井屏蔽、镀膜玻璃含金属）一起用于覆盖估算。

  tags: [attenuation, materials, ekahau, predictive-survey]

- id: p14
  title: 已知 WiFi 干扰源清单
  type: principle
  source_chapter: "p137"
  source_quote: |
    "Microwave ovens; 2.4GHz cordless phones, DSSS and FHSS; Fluorescent bulbs; 2.4GHz video cameras; Elevator motors; Cauterizing devices; Plasma cutters; Bluetooth radios; Nearby 802.11, 802.11b or 802.11g WLANs; WISPs; Bookcases; File Cabinets; Pallet Racks; 5GHz cordless phones; Radar; Perimeter sensors; Digital satellite; Outdoor wireless 5GHz bridges."
  summary: |
    现场排查干扰时的对照清单：2.4 GHz 段——微波炉、无绳电话（DSSS/FHSS）、荧光灯、2.4G 摄像头、蓝牙、邻近 b/g 网；5 GHz 段——5G 无绳电话、雷达、周界传感器、数字卫星、户外 5G 桥接；通用——电梯电机、电灼/等离子切割设备；还有书架、文件柜、货架这类物理遮挡"干扰源"。频谱分析（Spectrum Survey）中识别出的占空比异常设备大多能在这张表里对号入座。

  tags: [interference, spectrum, 2.4ghz, 5ghz, checklist]

- id: p15
  title: AP 布放与环境施工原则
  type: principle
  source_chapter: "p138-139"
  source_quote: |
    "Start with antennas pointing straight up or down. Use semi-directional antenna for coverage as opposed to an omni-directional antenna for long corridors... Rain, snow, and wind can interfere... Place access points equal distant from the walls... Place Access points above all sources of obstruction... Try not to place the AP near sources of heat or under the sun."
  summary: |
    安装施工守则：射频侧——天线初始朝向垂直（正上/正下）；长走廊用半定向天线做覆盖而非全向；每次更换天线后复核不超国别法定功率；雨雪风、人群（人体吸波）、树木都会衰减信号。布放侧——AP 与四周墙面等距、尽量放房间/覆盖区中央；必须高于所有障碍物（比如办公位隔断上方、贴近天花板），即使这一点压过"居中"原则；远离热源与暴晒。配合 p136：金属吸 WiFi 信号，电梯井几乎全屏蔽（覆盖井道要在井顶/井底或轿厢内放 AP），镀膜玻璃和窗膜含金属要预期掉信号。

  tags: [ap-placement, installation, environment, best-practice]

- id: p16
  title: Enterprise 模式最低部署要求清单
  type: principle
  source_chapter: "p226-227"
  source_quote: |
    "Hardware requirement: Access Point, PoE Switch, DHCP Server, OmniVista 2500. Minimal configuration required: Stellar Access Point: Purged AP with default factory configuration. OmniSwitch: PoE, Management VLAN, 'ip dhcp-relay' for external DHCP server. DHCP server: Option 138 on Management VLAN, Address Plan for Service VLAN. OmniVista 2500 server: IP configuration, Licenses."
  summary: |
    Enterprise 模式开局的四件套与最小配置：硬件——AP、PoE 交换机、DHCP 服务器、OV2500；AP 侧要求出厂默认的净化状态；交换机侧要开 PoE、划管理 VLAN、DHCP 在外部时配 ip dhcp-relay；DHCP 侧管理 VLAN 作用域必须带 option 138（指向 OV2500），并为业务 VLAN 规划地址池；OV2500 侧完成 IP 配置与许可导入。这份清单同时是 p164 拓扑图（trunk 口 native VLAN=管理 VLAN、tagged VLAN=SSID VLAN）的文字版。

  tags: [enterprise, requirements, minimal-config, poe, dhcp]

- id: p17
  title: OV2500 许可证体系与扩容规则
  type: principle
  source_chapter: "p229-230"
  source_quote: |
    "OmniVista Core License - required (Network devices). OmniVista VMM License - optional. OmniVista AP License count: Stellar Access Point: Per AP License model. OmniVista Guest Management License count: Per device license model. OmniVista BYOD License count: Per device license model. OmniVista High Availability (HA) License: One License per set of OmniVista servers. OmniVista Web Content Filtering License: One license for 10 Access Point."
  summary: |
    许可模型速记：Core 许可必需（管网络设备）；VMM 可选；AP 许可按 AP 台数（Stellar 每 AP 一枚）；Guest 与 BYOD 许可都按"设备数"而非账号数计；HA 许可每对 OV 服务器一枚；WCF 许可按 1:10 AP 比例。扩容规则：AP 许可数要大于待部署 AP 总数；不足时先导入增量许可再上 AP（如 100+50=150）。评估许可（EVAL）全功能但只有 90 天有效期，一个文件含全部设备与服务许可。

  tags: [license, ov2500, capacity, guest, byod, wcf]

- id: p18
  title: Express 集群规模与 PVM 选举规则
  type: principle
  source_chapter: "p149-152"
  source_quote: |
    "In an AP group, one AP supports the role of centralized management. It is called PVM (Primary Virtual Manager)... Another AP is responsible for rescuing the PVM. It is called SVM... Highest Model Type, Highest MAC address -> PVM; AP with the second highest MAC is designated as the SVM... Cluster Max. Size: 255. Recommendations: Max Up to 32 APs per OmniSwitch, Max Up to 64 APs per stack."
  summary: |
    Express 模式的集群规则：同 Group ID 的 AP 里选一台当 PVM（主虚拟管理器）集中管理，选举依据是最高型号、再最高 MAC；第二高 MAC 的当 SVM（备机）负责接管；其余都是 Member，集群上限 255 台。可靠性设计上，集群超过 64 台时建议每台 OmniSwitch 最多挂 32 台 AP、每堆叠最多 64 台，避免单点故障域过大。Enterprise 模式对应的上限是 4000 AP（p154-155）。

  tags: [express, pvm, svm, cluster-sizing, election]

- id: p19
  title: Stellar 三平面流量规则（管理不打标/数据打标/无隧道）
  type: principle
  source_chapter: "p159-163"
  source_quote: |
    "Management Plane: AP management traffic is always untagged. Control Plane: AP to AP protocol over the air and over the LAN; Used for RF Management, Neighbor AP discovery, Roaming client context sharing. Data Plane: Wireless data converted to Ethernet in the AP and sent to the AP uplink. Wireless traffic always tagged on the AP uplink. No tunnel mode to OV or Virtual Controller. Data Plane is only L2... Routing provided by LAN infrastructure."
  summary: |
    无控制器架构的三平面行为约定，排障抓包必背：管理平面——配置/监控流量永远不打标签（走 native/管理 VLAN），Express 集中在 PVM、Enterprise 集中在 OV2500；控制平面——AP 间协议走空口和 LAN 两路，承担射频管理、邻居发现、漫游上下文共享，属 AP 内部流量；数据平面——无线帧在 AP 本地转成以太网上行，业务流量在 AP 上联口永远打标签，到 OV/虚拟控制器没有隧道，数据面只做二层，路由由 LAN 基础设施承担。解释"为什么 AP 口要配 trunk 且 native VLAN=管理 VLAN"就靠这条。

  tags: [planes, untagged, tagged, no-tunnel, controller-less]

- id: p20
  title: DHCP Option 138 配置规则（指向 OV2500）
  type: principle
  source_chapter: "p156/172"
  source_quote: |
    "WiFi Express is the default mode. DHCP option 138 equals the IP address of the OmniVista 2500 Server. # Classify OmniAccess Stellar AP as STELLAR: class STELLAR { match if substring (option vendor-class-identifier, 0, 4) = 'HAP.'; } option ovwma code 138 = ip-address; option ovwma 192.168.0.61;"
  summary: |
    Enterprise 模式触发开关：AP 默认 Express 模式，只有当 DHCP 服务器在管理 VLAN 作用域里返回 option 138 且值为 OV2500 的 IP 时，AP 才切换为 Enterprise。isc-dhcp-server 写法：Stellar AP 的 vendor-class 以"HAP."开头可据此分类，138 非标准选项需先定义 `option ovwma code 138 = ip-address;` 再在池内下发；OmniSwitch 做 DHCP 服务器时直接 `option 138 x.x.x.x`。Windows Server 配置路径见 c04 案例附录（p278）。

  tags: [dhcp, option-138, enterprise-mode, isc-dhcp]

- id: p21
  title: AP Group 容量与配置模型
  type: principle
  source_chapter: "p161/271"
  source_quote: |
    "AP Group: Multiple APs in the same AP Group, sharing the same configuration. Mix of any AP type & total number of AP limited to 4000 (Enterprise) or 255 (Express). When an AP initially registers with OmniVista, the AP is placed into a pre-configured 'Default' AP Group. Any configuration applied to an AP Group is applied to all APs in the group."
  summary: |
    OV2500 不直接管理单台 AP，一切配置以 AP Group 为单位：同组成员共享配置（管理 VLAN、RF Profile、Data VPN 等），组内可混插任意 AP 型号，Enterprise 全局上限 4000 台（可分散在多个组），Express 255 台，组数无限制。新注册 AP 自动落入 Default 组，需要手工改到目标组。给 AP Group 下发的任何配置都会同步到组内所有 AP——这也是配置回滚/批量变更的最小单位。

  tags: [ap-group, ov2500, scale, configuration-model]

- id: p22
  title: OV2500 高可用（HA）机制要求
  type: principle
  source_chapter: "p232-233"
  source_quote: |
    "High Availability (HA) creates a redundant (Stand-by) OmniVista which will take over if the primary (Main) OmniVista becomes unavailable. With HA, 2 instances of OV are constantly running. Connection across a Layer 2 network; Extension to Layer 3 network, if VxLAN or SPB are used. Network devices must communicate to Virtual IP. Dedicated OmniVista HA license."
  summary: |
    HA 部署要点：主备两台 OV 常驻运行、实时同步服务与数据库；正常要求二层网络互联，若底层有 VxLAN 或 SPB 可扩展到三层；AP/交换机等网络设备一律对"虚拟 IP"通信，主备切换对设备透明；切换时 UPAM（含 BYOD/Guest）与全部监控服务由备机接管；需要专门的 HA 许可（每对服务器一枚）。规划时先确认二层可达或 SPB/VxLAN 基础，再申请许可。

  tags: [ha, virtual-ip, ov2500, spb, vxlan]

- id: p23
  title: SNMP 发现参数基线（v3 + SHA+DES）
  type: principle
  source_chapter: "p256-257"
  source_quote: |
    "OS6870, OS6360, OS2360: user snmpuserv3 read-write all password 'Superuser=1' sha+des; snmp station 10.130.5.5X 162 snmpuserv3 v3 enable. SNMPv3 Profile Parameters: Timeout (msec): 5000; Retry Count: 3; User Name: snmpuserv3; Auth & Priv Protocol: SHA+DES; Auth Password / Priv Password: Superuser=1."
  summary: |
    OV2500 发现 OmniSwitch 用 SNMP（v1/2/3 均支持，推荐 v3）。交换机侧两条命令建读写用户与工作站；OV 侧发现参数基线：超时 5000 ms、重试 3 次、认证与加密协议 SHA+DES、用户名/密码两侧严格一致。发现失败的复核顺序（p262）：交换机 `show snmp station` 核对 IP/用户名、重输密码确认协议组合、OV 侧在 Discovery Profiles 里核对或重建档案后重跑 Discover Now。

  tags: [snmpv3, discovery, parameters, omniswitch]

- id: p24
  title: AP Location 自动生成优先级
  type: principle
  source_chapter: "p238"
  source_quote: |
    "If port alias is configured on the port => AP Location = Port Alias. If system location is configured => AP Location = System Location:PortID. If the system name is configured => AP Location = System Name:PortID. By default => AP Location = Chassis ID:PortID (Chassis MAC address / chassis/slot/port format)."
  summary: |
    OV2500 拓扑里 AP 位置字符串的取值优先级（高到低）：端口别名（interfaces chassis/slot/port alias）> 交换机 system location > 交换机 system name > 默认的机箱 MAC:端口号。想让拓扑图上直接显示"楼层-机房-机架"这类语义位置，就在接入交换机上配 system location 或逐口配 port alias，AP 会通过 LLDP 学到并上报。这也是 f16 UNP 自动配置流程第 4 步的落地细节。

  tags: [ap-location, lldp, topology, port-alias]

- id: p25
  title: SSID Usage 模板矩阵（Usage→安全级别+门户组合）
  type: principle
  source_chapter: "p284"
  source_quote: |
    "Guest Network: Captive Portal, SSID Security Level Open or MAC... Employee BYOD Network: 802.1X or MAC followed by Captive Portal BYOD. Enterprise Network for Employees: 802.1X. Protected Network: PSK. Protected Network for Employees (BYOD): PSK followed by Captive Portal BYOD."
  summary: |
    向导里选 Usage 即选定模板组合：Guest Network=Open/MAC+访客门户；Employee BYOD Network=802.1X 或 MAC 认证后接 BYOD 门户；Enterprise Network for Employees=纯 802.1X（员工企业网标准形态）；Protected Network=纯 PSK；Protected Network for Employees（BYOD）=PSK 后接 BYOD 门户。模板只给默认值，创建后仍可在向导里改。选错 Usage 意味着后面要手工纠正认证与门户组合，选型时对照本表。

  tags: [ssid, usage-template, security-level, captive-portal]

- id: p26
  title: VLAN Pooling 原则（避免单一大广播域）
  type: principle
  source_chapter: "p286"
  source_quote: |
    "VLAN options: Default VLAN: Single VLAN assigned to the SSID. VLAN Pooling: Pool of VLAN assigned to the SSID. Avoid large broadcast domain with a single VLAN."
  summary: |
    SSID 的 VLAN 两种模式：默认单 VLAN；VLAN Pooling 把一组 VLAN（如 20/30/40）绑到同一 SSID，终端哈希分配。设计动机是避免单个 VLAN 形成巨大广播域——高密场景（大会议室、场馆）下一个 /16 员工段的广播/组播开销会拖垮空口，用 VLAN 池切小广播域。Access Role Profile 与 VLAN 的映射关系在池化后依然按角色走。

  tags: [vlan-pooling, broadcast-domain, ssid, design]

- id: p27
  title: WLAN Service 加密类型清单（Enterprise/Personal 各自合法值）
  type: principle
  source_chapter: "p300"
  source_quote: |
    "Enterprise: DYNAMIC_WEP, WPA_TKIP, WPA_EAS, WPA2__TKIP, WPA2_AES, WPA3_AES; 802.1x Bypass is option; AAA Profile is mandatory. Personal: WPA_PSK_TKIP, WPA_PSK_AES, WPA_PSK_AES_TKIP, WPA2_PSK_TKIP, WPA2_PSK_AES, WPA3_SAE_AES, WPA3_PSK_SAE_AES; Passphrase is mandatory; Key Format; AAA Profile is Mandatory."
  summary: |
    专家模式安全设置里可选的加密枚举值：Enterprise 级可选 DYNAMIC_WEP/WPA_TKIP/WPA_EAS/WPA2_TKIP/WPA2_AES/WPA3_AES（含 TKIP 老算法仅作兼容）；Personal 级可选 WPA/WPA2 PSK 系列与 WPA3_SAE_AES、WPA3_PSK_SAE_AES，口令与密钥格式必填。无论哪种级别 AAA Profile 都是必填字段（Personal 也需要，用于门户/MAC 认证路径）。排错时先核对这些枚举值是否与终端能力匹配。

  tags: [encryption, enterprise, personal, aaa-profile, wlan-service]

- id: p28
  title: UPAM 能力边界与许可口径
  type: principle
  source_chapter: "p335-337"
  source_quote: |
    "UPAM consists of Guest Access (Guest License required), BYOD Access (BYOD License required), A built-in RADIUS Server, A built-in MAC Authentication Server. Internal RADIUS server used to authenticate both Guest and BYOD users; UPAM logs can be redirected to an external syslog server; Guest Access License: per device license model (not per account); BYOD Access License: per device license model (not per account)."
  summary: |
    UPAM（统一策略认证管理器）内嵌在 OV2500 里，由四部分组成：Guest Access、BYOD Access、内置 RADIUS 服务器、内置 MAC 认证服务器。认证源可选内部 RADIUS+本地库，或外接 LDAP/AD/RADIUS（还可按 AD 属性做角色映射）；日志可转发外部 syslog。许可口径要点：Guest 与 BYOD 许可都按接入设备数计、与账号数无关——开 1 万个访客账号不额外耗许可，按并发接入设备算。

  tags: [upam, radius, guest, byod, licensing]

- id: p29
  title: 带宽合同三层级（SSID 共享/ARP 按用户/ACL 按规则）
  type: principle
  source_chapter: "p363"
  source_quote: |
    "Bandwidth contract at SSID level: Configured in Advanced WLAN Service Configuration; Bandwidth shared for all user, per radio. Bandwidth contract at Access Role Profile level: Configured in Advanced Access Role Configuration; Bandwidth assigned per user of the profile - Not shared. Bandwidth contract at Role level: A Policy List (ACL/QoS) can restrict the Bandwidth as an action."
  summary: |
    限速的三种落点：SSID/WLAN Service 级——该射频上全体用户共享一个总带宽合同；Access Role Profile 级——每个用户独享设定带宽、互不共享；Role/Policy List 级——把限速作为 ACL/QoS 规则的动作（还可叠 DPI 应用规则）。三层可共存，实际生效优先级见框架 f12（DPI 最细、SSID 最粗）。常见设计：SSID 级兜底总限 + 访客角色按人限速。

  tags: [bandwidth, contract, qos, access-role, ssid]

- id: p30
  title: WCF 工作机制与前提（DNS Snooping + Brightcloud）
  type: principle
  source_chapter: "p366-367"
  source_quote: |
    "Stellar AP DNS Snooping: 1. DNS request FQDN www.facebook.com. 2. FQDN filtered? 3. FQDN category? Social Network. 4. Send action to AP. 5. Create Block ACL rule to IP of the FQDN... Activate WCF: Per AP Group... or per Access Point. Configure DNS: No DNS -> WCF not in Service. Not supported: AP1101, AP1201H."
  summary: |
    Web 内容过滤的实现链路：AP 对客户端 DNS 请求做嗅探→把 FQDN 送 OV2500（内嵌 Brightcloud SDK）查分类与允许/阻断状态→结果回发 AP→AP 生成针对该 FQDN 解析 IP 的阻断 ACL，后续流量在 AP 本地拦截（默认放行、命中拒绝类目才拦）。启用粒度可按 AP Group 或单 AP；前提是 OV2500 必须配 DNS，否则状态为 Not in service；AP1101/AP1201H 不支持。WCF Profile 一个 Access Role Profile 只能绑一个。

  tags: [wcf, dns-snooping, brightcloud, acl, web-filtering]

- id: p31
  title: 漫游默认状态与快速漫游约束
  type: principle
  source_chapter: "p407/414"
  source_quote: |
    "L2 Roaming always enabled. L3 Roaming disabled by default, configured in the Advanced WLAN Service Configuration. Fast Roaming disabled by default, configured per SSID. OKC can be enabled with WPA2/WPA3 Enterprise only. 802.11r (Fast Roaming) can be enabled with WPA2/WPA3 encryption only (Personal or Enterprise)."
  summary: |
    漫游功能的默认值与依赖：L2 漫游总是开启；L3 漫游默认关闭、在 Advanced WLAN Service 里开；快速漫游（Fast Roaming）默认关闭、按 SSID 开启，且受安全级别约束——OKC（机会式密钥缓存/802.11k）只能配在 WPA2/WPA3 Enterprise，802.11r（FT 快速 BSS 切换）只能配在 WPA2/WPA3 加密（Personal 或 Enterprise 均可）。开错组合（如对 Open SSID 开 11r）会直接配不上；不开快速漫游则回落标准漫游（重新走 RADIUS）。

  tags: [roaming, fast-roaming, okc, 802.11r, defaults]

- id: p32
  title: Roaming RSSI 阈值推荐值与两个极端
  type: principle
  source_chapter: "p424"
  source_quote: |
    "Value range is 0-100. Recommended value for 2.4GHz: RSSI = 10. Recommended value for 5GHz: RSSI = 15. The Roaming RSSI Threshold controls the signal strength a client needs to see before searching for another site. If the RSSI threshold is too low, the client remains on a low signal strength site. If the RSSI threshold is too high, the client roams too much that could result to packet loss."
  summary: |
    RF Profile 里 Roaming RSSI Threshold 的调参基准：取值 0-100，推荐 2.4 GHz 用 10、5 GHz 用 15，并配合 802.11k/802.11v 使用。阈值含义是终端感知信号低于该值才发起找新 AP。两个失败模式要背：设太低——终端粘在弱信号 AP 上不切换（粘性终端）；设太高——频繁切换反而丢包。调优时从推荐值起小幅试。

  tags: [rssi-threshold, sticky-client, roaming, rf-profile, tuning]

- id: p33
  title: 广播/组播优化参数（密钥轮换/广播过滤/组播转单播上限）
  type: principle
  source_chapter: "p502-503"
  source_quote: |
    "Broadcast Key rotation: Only applicable for Enterprise. Rotate the keys periodically to avoid key cracking. Default period: 15 min - Range 1 min - 24 hours. Broadcast Filter All: Drop all broadcast packets except DHCP & ARP. Broadcast Filter ARP: Convert broadcast ARP to unicast ARP. Multicast Optimization: Convert multicast to unicast, uses the highest data rate... Channel Utilization: default value 90%; Number of Clients: default value 6."
  summary: |
    Advanced WLAN Service 里的空口优化参数：广播密钥轮换仅限 Enterprise 安全级，默认 15 分钟（可调 1 分钟-24 小时）周期轮换 PTK/GTK 防破解；Broadcast Filter All 丢弃除 DHCP/ARP 外全部广播，Broadcast Filter ARP 把广播 ARP 转单播（无组播业务时推荐开启）；组播优化把组播转单播、用单播密钥和最高速率发送，但在信道利用率超 90%（默认）或高吞吐客户端数超 6（默认）时自动停止，防 CPU 过载。

  tags: [broadcast-filter, multicast-optimization, key-rotation, airtime]

- id: p34
  title: WMM QoS 四类推荐映射（802.1p/DSCP）
  type: principle
  source_chapter: "p505"
  source_quote: |
    "Recommended Settings: WMM 802.1p DSCP. Best Effort: 0 / 0. Background: 2 / 18 - AF21. Voice: 5 / 46 - EF. Video: 4 / 34 - AF41. Default OV Settings: Best Effort 0,3 / 0x00, 0x18; Background 1,2 / 0x08, 0x10; Voice 6,7 / 0x30, 0x38; Video 4,5 / 0x20, 0x28."
  summary: |
    WMM 四队列与 802.1p/DSCP 的映射基准：推荐配置——Best Effort=1p 0/DSCP 0、Background=1p 2/DSCP 18(AF21)、Voice=1p 5/DSCP 46(EF)、Video=1p 4/DSCP 34(AF41)；OV 默认配置把四类各扩成两个 1p/DSCP 档（如 Voice 6,7→48/56）。语音走 EF、视频走 AF41 是跨设备对接的行业惯例，与运营商/骨干 QoS 策略对齐时以推荐表为准。

  tags: [wmm, qos, 802.1p, dscp, mapping]

- id: p35
  title: 四种勘测类型对比（预测/被动/主动/吞吐+频谱）
  type: principle
  source_chapter: "p93"
  source_quote: |
    "Predictive Survey: Simulate RF by defining wall, placing Simulated heatmaps of capacity and coverage. Passive Survey: Walk around, collect beacons, probes, measure signal strength, interference, SNR for all APs -> SNR, RSSI, interference heatmaps for all APs. Active Survey: Walk, connect to the network, test for packet loss, RTT, association -> Heatmaps and analysis for roaming. Throughput Survey: Measure throughput and jitter. Spectrum Survey: Detect all RF sources -> Interferers, duty cycle."
  summary: |
    勘测类型选型表：预测勘测在软件里建墙仿真、出容量覆盖模拟热图（无需到场）；被动勘测现场走测只听不关联，采集全部 AP 的信标/信号强度/干扰/SNR；主动勘测关联到网络实测丢包、RTT、关联与漫游行为；吞吐勘测专测吞吐与抖动（瞬时容量/语音分析）；频谱勘测检测所有 RF 源（含非 WiFi 干扰源与占空比）。项目映射（p455）：新部署/换网用预测，部署后 RF 分析用被动，客户端性能分析用主动。

  tags: [survey-types, passive, active, predictive, spectrum]

- id: p36
  title: BLE Beaconing 默认参数
  type: principle
  source_chapter: "p170"
  source_quote: |
    "BLE Beacon is configured per AP Group. Turned OFF by default. Configurable parameters are: Beaconing Mode: iBeacon per default; Transmission Power; Frequency/Emission Period; UUID (Universal Unique Identifier) - ALE specific UUID for all ALE products; Major and Minor values - used for greater accuracy than UUID alone."
  summary: |
    AP 内置 BLE 信标做资产/人员定位时的参数口径：按 AP Group 配置、默认关闭；可调项——信标模式（默认 iBeacon）、发射功率、发射周期、UUID（ALE 全产品统一 UUID）、Major/Minor（比 UUID 单独定位更精细的分层字段）。AP1230/13xx 系列自带 BLE。配套生态：AeroScout RTLS 用 Stellar AP 上报的标签 RSSI 做定位引擎（p171）。

  tags: [ble, ibeacon, asset-tracking, default-off]

- id: p37
  title: IPv6 支持范围（客户端/管理面全支持，RADIUS 仍走 IPv4）
  type: principle
  source_chapter: "p173-174"
  source_quote: |
    "IPv6 Client Support - Enterprise Mode: AP Management through IPv6; Client MAC/1X Authentication: Client authentication request to AP through IPv6; Radius communication between AP and UPAM through IPv4; Client Portal Authentication: Client to portal server through IPv6; Portal server to Radius Server through IPv4."
  summary: |
    Enterprise 模式 IPv6 能力边界：AP 管理接口可拿 IPv6（DHCPv6 取地址/网关/DNS）；客户端 802.1X/MAC 认证请求可走 IPv6 到 AP，但 AP 到 UPAM 的 RADIUS 通信仍是 IPv4；门户认证客户端到门户服务器可走 IPv6，门户服务器到 RADIUS 仍是 IPv4。客户端流量在 IPv6 客户端与 IPv6 网关间正常转发并支持 IPv6 QoS/ACL。规划纯 IPv6 管理网时要留意 RADIUS 链路仍需 IPv4 通路。

  tags: [ipv6, radius, enterprise, limitation]

- id: p38
  title: Stellar AP 硬件共性规格（专用扫描射频/SSID 数/客户端数/温度）
  type: principle
  source_chapter: "p184-195"
  source_quote: |
    "AP1301: 1 full band (radio) dedicated to radio scanning; Improving network security and Wi-Fi quality. Up to 16 SSID (8 per radio); 512 clients per AP... AP1451: Up to 48 SSID (16 BSSID per radio); 1536 clients per AP... Operating Temp: 0°C to 45°C (indoor); AP1361: Temperature range -40 to +65 degree C (outdoor)."
  summary: |
    选型时常用的系列共性参数：WiFi 6 起中高端机型（AP1301/1301H/1311/1320/1331/1351/1360、6E 的 AP1451 等）配 1 个全频段专用扫描射频，专职安全与射频质量监测；每射频 SSID/BSSID 数——入门 8 个、多数 16 个（AP1451 三射频可达 48 SSID）；单 AP 客户端数——入门 512、中端 1024、高端 1536；室内机工作温度 0-45 °C，户外 AP1361 为 -40 到 +65 °C。PoE 档位从 802.3af（AP1301 全功能）到 802.3bt（AP1331/1431/1451/1521）。

  tags: [hardware, ap-specs, scanning-radio, ssid-count, temperature]

- id: p39
  title: WiFi4EU 与 Hotspot 2.0 要求
  type: principle
  source_chapter: "p506-507"
  source_quote: |
    "WiFi4EU: European Union Initiative, to provide free WiFi access to citizen in public venues; Networks with WiFi4EU SSID use an HTTPS Captive Portal; Session timeout should be configurable up to 12 hours. Hotspot 2.0 is a WLAN Service option. Stellar Access Point support 802.11u (GAS/ANPQ), EAP-SIM / EAP-AKA."
  summary: |
    两个公共热点特性：WiFi4EU 是欧盟公共场所免费 WiFi 计划，SSID 必须用 HTTPS 强制门户，会话超时需可配置到最长 12 小时（配置入口在 Guest SSID 的 Guest Access Strategy）；Hotspot 2.0（Passpoint）做无缝安全接入，Stellar AP 支持 802.11u（GAS/ANQP）与 EAP-SIM/EAP-AKA（SIM 卡认证、运营商分流），配置入口在 WPA2-Enterprise SSID 的 Advanced WLAN configuration。

  tags: [wifi4eu, hotspot-2.0, 802.11u, eap-sim, public-wifi]
