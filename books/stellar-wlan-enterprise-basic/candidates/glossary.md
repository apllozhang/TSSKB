# 术语 · OmniAccess Stellar WLAN Enterprise Basic (DT00XTE368EN)

> 来源：source/fulltext.md（页码即教材 PDF 页码）

- id: g01
  title: IEEE 802.11 与 Wi-Fi 联盟（标准 vs 认证）
  type: glossary
  source_chapter: "p6"
  source_quote: |
    "IEEE 802.11: Institute of Electrical and Electronics Engineers. Wi-Fi: Wireless Fidelity, Wi-Fi Alliance. CERTIFICATION: STANDARD: WI-FI ALLIANCE, IEEE. 802.11 ≈ WI-FI."
  summary: |
    IEEE 802.11 是电气电子工程师学会制定的技术标准家族；Wi-Fi 则是 Wi-Fi 联盟（行业组织）提供的互操作性认证与商标。联盟提供兼容性指南、设备命名（WiFi 4/5/6/6E/7）与产品描述规范。两者约等但视角不同：一个管标准文本，一个管认证贴标。售前沟通时"802.11ax"与"WiFi 6"是同一事物的两种叫法。

  tags: [802.11, wifi-alliance, standard, certification]

- id: g02
  title: BSS / BSSID / DS（基本服务集及其标识）
  type: glossary
  source_chapter: "p10"
  source_quote: |
    "BSS (Basic Service Set): Set formed by the access point (AP) and the equipment located in its coverage area. BSSID (Basic Service Set Identifier): Each BSS is identified by a BSSID, an identifier of 6 bytes (Access Point MAC@). DS (Distribution System): Infrastructure that connect Access Points (APs)."
  summary: |
    基础设施模式的三个积木：BSS 是一台 AP 加其覆盖区内终端构成的服务集；BSSID 是 BSS 的 6 字节标识，直接取 AP 的 MAC 地址（AP 每个射频每个 SSID 各有一个 BSSID）；DS 分布系统是互联各 AP 的有线基础设施，让跨 BSS 通信成为可能。抓包时看到的"AP MAC"就是 BSSID；教材后文 AP1451 "48 SSID (16 BSSID per radio)"即按每射频 16 个 BSSID 计算。

  tags: [bss, bssid, ds, infrastructure-mode]

- id: g03
  title: ESS / ESSID / SSID（扩展服务集与网络名）
  type: glossary
  source_chapter: "p10-11"
  source_quote: |
    "ESS (Extended Service Set): One or more interconnected basic service sets (BSS) and their associated LANs. ESSID (Extended Service Set IDentifier): Also called SSID, represents the name of the ESS network (32 characters)."
  summary: |
    ESS 是经 DS 互联的一个或多个 BSS 及其关联 LAN 的总和——即同一 SSID 名下多台 AP 组成的大覆盖网。ESSID 又称 SSID，是 ESS 的网络名，最长 32 字符，即终端扫描列表里看到的 WiFi 名。注意与 BSSID 区分：SSID 是人读的名字，BSSID 是机器读的 MAC。多个 WLAN Service 也可以广播同一个 SSID 名。

  tags: [ess, essid, ssid, network-name]

- id: g04
  title: IBSS / Ad-hoc 模式（无 AP 自组网）
  type: glossary
  source_chapter: "p11"
  source_quote: |
    "IBSS (Independent Basic Service Set): Wireless network made up of at least two stations and not using an Access Point (AP). SSID (Service Set IDentifier): Represents the name of the IBSS network (32 characters)."
  summary: |
    802.11 的第二种工作模式：独立基本服务集，至少两台终端直连组网、不经过 AP，网络名同样是最长 32 字符的 SSID。与基础设施模式（BSS/ESS，经 AP 转发）相对。企业网里基本不用，但排障时终端"连了个奇怪的同名网"常是误连了 ad-hoc。

  tags: [ibss, adhoc, operating-mode]

- id: g05
  title: 802.11 修正案演进（a/b/g/n/ac/ax/be）
  type: glossary
  source_chapter: "p16-17"
  source_quote: |
    "802.11BE, 802.11B, 802.11A, 802.11G, 802.11N, 802.11AC, 802.11AX: INTRODUCTION STANDARD 802.11 AMENDMENTS. IEEE 802.11 – AMENDMENTS SPECIFICATIONS: 1997, 1999, 2003, 2009, 2019, 2013."
  summary: |
    802.11 是 1997 年的基线标准，后续以字母修正案扩展：b（1999，11 Mbps/2.4G）、a（1999，54 Mbps/5G）、g（2003，54 Mbps/2.4G）、n/HT（2009，600 Mbps，MIMO 引入）、ac/VHT（2013-14，6.9 Gbps，仅 5G Wave2 MU-MIMO）、ax/HE（2019-21，9.6 Gbps，OFDMA/TWT，6E 进 6 GHz）、be（2024，46 Gbps，WiFi 7）。与 ALE 产品对应：AP1301/1320/1331/1351/1360 属 WiFi 6，AP1411/1431/1451 属 6E，AP1511/1521 属 WiFi 7，AP1230 属 WiFi 5（p19）。

  tags: [amendments, 802.11n, 802.11ac, 802.11ax, 802.11be, evolution]

- id: g06
  title: OFDM → OFDMA 与资源单元（RU）
  type: glossary
  source_chapter: "p32"
  source_quote: |
    "OFDMA DL/UL: Enables an 802.11ax access point to simultaneously communicate with multiple devices by dividing each WiFi channel into smaller sub-channels known as Resource Units (RU). Each individual RU (or sub-channel) can be utilized for different clients that are serviced simultaneously."
  summary: |
    OFDM 是 802.11a/g/n/ac 的正交频分复用，一个时刻整条信道只服务一个用户；OFDMA（正交频分多址）是 802.11ax 引入的升级：把信道在频域切成多个资源单元 RU，不同终端的 RU 可在同一时刻并行收发（上下行都支持）。这是 WiFi 6 高密场景时延与效率提升的核心机制。WiFi 7 进一步允许多个不连续 RU 聚合（MRU）。

  tags: [ofdm, ofdma, ru, wifi6, multiplexing]

- id: g07
  title: MU-MIMO（多用户多入多出）
  type: glossary
  source_chapter: "p31"
  source_quote: |
    "802.11ax devices will use beamforming techniques to direct packets simultaneously to spatially diverse users. WiFi 5: 4x4, Downlink only. WiFi 6: 8x8, Uplink/Downlink."
  summary: |
    多用户 MIMO：AP 用波束赋形技术把数据包同时发给空间上可区分的多个用户，靠空间流并行提升容量。代际规格：WiFi 5 为 4x4 且仅下行；WiFi 6 为 8x8 且上行/下行双向；WiFi 7 提到最高 16x16。与 OFDMA 的分工见原则 p05——MU-MIMO 管大包高带宽，OFDMA 管小包低时延。

  tags: [mu-mimo, beamforming, spatial-streams, wifi6]

- id: g08
  title: QAM（正交振幅调制：256/1024/4096）
  type: glossary
  source_chapter: "p34"
  source_quote: |
    "Quadrature amplitude modulation (QAM) is a modulation scheme that results in a denser constellations to increase data rates. This is done by varying the amplitude and the phase of the signal. More bits per hertz... each symbol transmits 8-bit data (WiFi 5), 10-bit data (WiFi 6)."
  summary: |
    QAM 通过同时改变信号的幅度与相位形成更密的星座图，让每符号携带更多比特：256-QAM（WiFi 5）每符号 8 bit，1024-QAM（WiFi 6/6E）10 bit（单流 +25%），4096-QAM（WiFi 7）12 bit（原始速率再 +20%）。"每赫兹更多比特"意味着对信噪比更敏感，距离远/干扰强时自动回落低阶调制。

  tags: [qam, modulation, constellation, data-rate]

- id: g09
  title: BSS Coloring 与 CCA（同频复用染色）
  type: glossary
  source_chapter: "p39"
  source_quote: |
    "BSS Coloring allows 2 devices to transmit data on the same channel and at the same frequency as long as the colors are different. Coloring also allows WiFi 6 access points to precisely adjust Clear Channel Assessment (CCA) parameters, including energy (adaptive power) and signal detection (sensitivity thresholds) levels."
  summary: |
    WiFi 6 的空间复用机制：给每个 BSS 标一个"颜色"，同信道同频上只要颜色不同就允许并行发送，只有同色才触发同频拥避让。配套可精细调节 CCA（空闲信道评估）的能量门限与信号检测灵敏度阈值。效果是把"同信道=必须退避"放松为"同信道同色=才退避"，高密部署的信道复用率因此提升。

  tags: [bss-coloring, cca, spatial-reuse, wifi6]

- id: g10
  title: TWT（目标唤醒时间）
  type: glossary
  source_chapter: "p40"
  source_quote: |
    "Target Wake Time: STAs to negotiate with APs for the waking schedule and then send or receive data."
  summary: |
    WiFi 6 省电机制：终端（STA）与 AP 协商好各自的唤醒时间表，到点才醒来收发，其余时间深睡——对比 WiFi 5 时代终端需反复 Waiting+Sleep 空耗。对电池供电的 IoT 与手机续航收益直接。WiFi 7 进一步引入 RTWT（Restricted TWT，受限目标唤醒时间）为低时延业务保留唤醒窗口（p205）。

  tags: [twt, power-saving, wifi6, iot]

- id: g11
  title: MLO（多链路操作，WiFi 7）
  type: glossary
  source_chapter: "p42"
  source_quote: |
    "MLO: allows for multi-link aggregation between a single STA and a single AP that has multiple radio chips, including 2.4 GHz, 5 GHz, and 6 GHz chips. MLO is a MAC layer technology that can aggregate multiple links across different frequency bands into a virtual link."
  summary: |
    WiFi 7 标志性技术：单终端与带多射频芯片（2.4/5/6 GHz）的 AP 之间做链路聚合，把跨频段的多条物理链路聚成一条虚拟链路。收益是可靠性与时延（链路间冗余切换）、吞吐（带宽叠加），密集区域体验更好。教材定位其为 MAC 层技术，与物理层的 320 MHz/4096-QAM 互补。

  tags: [mlo, wifi7, multi-link, mac-layer]

- id: g12
  title: MRU（多资源单元，WiFi 7）
  type: glossary
  source_chapter: "p43"
  source_quote: |
    "In WiFi 7, each device can receive several non-continuous Resource Units. Maximum Spectrum Efficiency, Reduced Latency, Increased Bandwidth. MRUs client 1 / MRUs client 2: 20 Mhz (106+26), 80 Mhz (242+242+242+242)."
  summary: |
    WiFi 7 对 OFDMA 的增强：允许一台设备分到多个不连续的 RU 并聚合使用（如 20 MHz 里的 106+26-tone 组合、80 MHz 里的多段 242 组合），而 WiFi 6 每设备只能占一段连续 RU。收益是频谱效率最大化、时延下降、可用带宽增加——碎片化的频谱资源也能被利用。

  tags: [mru, wifi7, ofdma, spectrum-efficiency]

- id: g13
  title: AFC（自动频率协调）
  type: glossary
  source_chapter: "p44"
  source_quote: |
    "Automatic Frequency Coordination (AFC)... Either a 'coordination' mechanism to assign frequency (channel) and EIRP. AFC in FCC domain... FCC approved 7 AFC providers (Qualcomm, Federated Wireless, Sony, Comsearch, WiFi Alliance, Wireless Broadband Alliance, and Broadcom)."
  summary: |
    6 GHz 室外标准功率设备的监管协调机制：因为 6 GHz 频段已有移动网络、微波链路、卫星、射电天文等在用业务，标准功率 AP（FCC 域最高 36 dBm EIRP）必须经 AFC 系统协调分配信道与功率才能发射。FCC 批准了 7 家 AFC 服务商。EU 域则干脆禁止标准功率 AP 室外使用，只留 LPI/VLP 低功率等级。

  tags: [afc, 6ghz, regulation, outdoor, coordination]

- id: g14
  title: Greenfield（绿地频段）
  type: glossary
  source_chapter: "p27/38"
  source_quote: |
    "Reliability: Greenfield (n/ac, 6(ax), 6e, a/b/g). 6GHz: Greenfield band for WiFi. Backwards compatibility not required. 60 Channels Available."
  summary: |
    "绿地"指没有遗留设备、无需向下兼容的干净频段。6 GHz 对 WiFi 就是 Greenfield：老 a/b/g/n/ac 终端根本不支持 6 GHz，因此无需为兼容旧协议保留开销（如 2.4/5 GHz 上的保护时隙与低速率），可靠性、信道宽度利用与安全策略（强制 PMF、禁旧协议）都能一步到位。这是 6E 除容量外的第二大卖点。

  tags: [greenfield, 6ghz, backward-compatibility]

- id: g15
  title: EIRP（等效全向辐射功率）
  type: glossary
  source_chapter: "p44"
  source_quote: |
    "Device Class / Operating Bands / Maximum EIRP: Standard-Power AP (AFC Controlled): 36 dBm; Fixed Client (AFC Controlled): 36 dBm; Client Connected to Standard-Power AP: 30 dBm; Low-Power AP (indoor only): 30 dBm... LPI: 23 dBm, Maximum EIRP density 10 dBm/MHz; VLP: 14 dBm, 1 dBm/MHz."
  summary: |
    等效全向辐射功率：发射功率加天线增益后的总辐射水平，是各国无线电法规管控的对象（还分总功率与功率谱密度 dBm/MHz 两个口径）。6 GHz 规则速记：FCC 域标准功率 AP/固定客户端 36 dBm、低功率室内 AP 30 dBm、LPI 客户端 24 dBm；EU 域 LPI 23 dBm、VLP 14 dBm。教材 p138 提醒：每次更换天线都要复核 EIRP 不超所在国法定限值。

  tags: [eirp, power, regulation, antenna-gain]

- id: g16
  title: 天线三大类型与辐射图（Radiation Pattern）
  type: glossary
  source_chapter: "p49-53"
  source_quote: |
    "3 Main Types: OmniDirectional, Semi-Directional, Highly Directional. OMNIDIRECTIONAL: RF Signal > Equal in all directions; Point to Multipoint; Short Distance (Dipole). SEMI-DIRECTIONAL: Patch/Panel, Yagi. HIGHLY-DIRECTIONAL: Grid; Long Distance."
  summary: |
    辐射图是天线能量在空间分布的图形描述，三大类：全向（偶极子，各向均匀，点对多点短距，AP 内置默认）、半定向（板状 Patch/Panel、八木 Yagi，集中单方向，点对点中短距桥接）、高定向（栅格 Grid，极窄波束长距链路）。选型口径见原则 p09。Stellar 外接天线型号尾号为"2"（AP1322/AP1362），其余为内置全向。

  tags: [antenna, radiation-pattern, omni, yagi, grid]

- id: g17
  title: RSSI 与 SNR（信号强度/信噪比）
  type: glossary
  source_chapter: "p91"
  source_quote: |
    "Signal to Noise: Excellent, Good, Fair, Weak. DATA RATE / SIGNAL STRENGTH / SIGNAL TO NOISE RATIO (SNR): coverage evaluation matrix used during site surveys."
  summary: |
    RSSI 是接收信号强度指示（数值越接近 0 越强，如 -43 dBm 优于 -77 dBm）；SNR 是信号与噪声的比值，直接决定可用数据速率——勘测热图按 Excellent/Good/Fair/Weak 分档。两者与速率联动评估覆盖质量（教材配三层对照矩阵）。AP 侧排障 `iwconfig` 输出里同时给出 Signal level 与 Noise level，相减即得 SNR。

  tags: [rssi, snr, signal-strength, data-rate]

- id: g18
  title: 同频/邻频干扰与覆盖盲区
  type: glossary
  source_chapter: "p89-90"
  source_quote: |
    "Optimal access point placement... Co-Channel, Adjacent-Channel... Identify sources of interference within the area; Dead spots in the coverage area."
  summary: |
    Co-Channel Interference 是同一信道上多个 AP 互相竞争空口（同频退避）；Adjacent-Channel Interference 是相邻信道能量溢出重叠造成的干扰——高密设计里两者都靠信道复用规划与收窄信道宽度治理。Dead spot（盲区）是覆盖区域内收不到足够信号的死角，勘测热图上表现为空洞，成因多为遮挡或 AP 宕机（p463-464）。现场用 WiFi Analyzer/Ekahau 可视化定位，处置是换信道、加 AP 或挪 AP。

  tags: [co-channel, adjacent-channel, interference, dead-spot]

- id: g19
  title: 勘测类型五分法（预测/被动/主动/吞吐/频谱）
  type: glossary
  source_chapter: "p93"
  source_quote: |
    "Predictive Survey: Simulate RF by defining wall, placing. Passive Survey: Walk around, collect beacons, probes... Active Survey: Walk, connect to the network, test for packet loss, RTT, association. Throughput Survey: Measure throughput and jitter. Spectrum Survey: Detect all RF sources."
  summary: |
    站点勘测按手段分五型：预测（软件仿真）、被动（现场只听不关联，测信号/噪声/干扰/SNR）、主动（关联入网实测丢包/RTT/关联与漫游）、吞吐（专测吞吐与抖动）、频谱（检测一切 RF 源与占空比，含非 WiFi 干扰）。选型映射见原则 p35 与勘测框架 f01-f04。被动与主动的核心区别是"是否认证关联"。

  tags: [site-survey, survey-types, passive, active, spectrum]

- id: g20
  title: Ekahau 与 Heatmap（勘测工具与热图）
  type: glossary
  source_chapter: "p92"
  source_quote: |
    "A laptop with a survey application and hardware (ex. Ekahau software)... The site map is imported into Ekahau and calibrates the settings based on the requirements."
  summary: |
    Ekahau Site Survey 是教材全程使用的勘测软件（预测、主动、被动、频谱分析一体），把楼层图导入后按需求标定环境；配套装备见 p101 清单（笔记本、频谱仪、三脚架、电池包、100ft 网线、至少 3 台 AP、外置无线网卡、测距轮、相机等）。Heatmap（热图）是把 RSSI/SNR/速率/干扰等指标按位置着色的可视化结果，是勘测交付物的标准形态。OV2500 里也有 Heat Map 应用用于检查射频覆盖与漫游重叠（p422）。

  tags: [ekahau, heatmap, survey-tool, visualization]

- id: g21
  title: PoE（以太网供电）
  type: glossary
  source_chapter: "p72"
  source_quote: |
    "Enhanced CPU Performance. Power over Ethernet (PoE): Power provided by Switch. DATA + POWER over ETHERNET CABLE."
  summary: |
    企业级 AP 与家用 AP 的硬件分水岭之一：数据与电力走同一根网线、由交换机供电。标准档位：802.3af（约 15W，AP1301 全功能）、802.3at（约 30-60W，AP1230/1320 等，部分机型 2 对供电时功能受限）、802.3bt（高功率，AP1331/1431/1451/1511/1521）。无 PoE 交换机时可外加 PoE 注入器（midspan）或电源适配器（p198）。排障 AP 不上线第一步就是 `show lanpower` 查供电状态（p273）。

  tags: [poe, 802.3af, 802.3at, 802.3bt, power]

- id: g22
  title: WEP（有线等效保密）
  type: glossary
  source_chapter: "p63"
  source_quote: |
    "Wired Equivalent Privacy (WEP): Encryption Algorithm: Rivest Cipher 4 (RC4); 2 Modes: 64 Bits Mode (40-bit key + 24-bit IV), 128 Bits Mode (104-bit key + 24-bit IV); Authentication: Open System (Null Authentication) or Shared Key."
  summary: |
    最早的 802.11 安全协议（1999 前后），意图达到"与有线等效"的保密性：RC4 流加密，密钥 40 或 104 位加 24 位 IV，认证分开放系统（两帧、空认证）与共享密钥（四帧）两种。因 IV 太短可被破解，两种位宽都被判 TOO WEAK，现场禁用（见反例 ce01）。它的历史意义是定义了"认证+加密"的两段式安全框架，WPA 系沿此演进。

  tags: [wep, rc4, legacy-security, deprecated]

- id: g23
  title: TKIP（临时密钥完整性协议）
  type: glossary
  source_chapter: "p64"
  source_quote: |
    "WPA: Encryption Algorithm: RC4 + TKIP (Temporal Key Integrity Protocol); Authentication Method: PSK (Pre Shared Keys) | 802.1X/EAP."
  summary: |
    WPA 时代的过渡加密增强：仍用 RC4 算法，但每包动态换密钥（临时密钥）修补 WEP 静态密钥的致命伤。只出现在 WPA 与 WPA2 的兼容选项里（WPA_TKIP、WPA2__TKIP、WPA_PSK_TKIP 等，见 p300 枚举），现代网络只在迁就极老终端时才开。WPA2 起正确选择是 AES-CCMP。

  tags: [tkip, wpa, rc4, transitional]

- id: g24
  title: PSK 与 802.1X/EAP（Personal 与 Enterprise 两型认证）
  type: glossary
  source_chapter: "p64"
  source_quote: |
    "WPA Personal: Authentication Method: PSK (Pre Shared Keys). WPA Enterprise: Authentication Method: 802.1X/EAP."
  summary: |
    WPA 系协议的两条认证分支：Personal 型用预共享密钥 PSK——全网共享一个口令，部署最简单但密钥可被提取/共享；Enterprise 型用 802.1X 框架加 EAP 封装（实验室用 PEAP+MSCHAPv2 内层），终端与 RADIUS/UPAM 逐个认证，每用户独立凭据、支持动态下发 VLAN/角色，是企业网标准形态。WiFi6E/7 时代 6 GHz 频段只认 WPA2/WPA3 级别安全。

  tags: [psk, 802.1x, eap, peap, personal-enterprise]

- id: g25
  title: AES-CCMP（计数器模式 CBC-MAC 协议）
  type: glossary
  source_chapter: "p65"
  source_quote: |
    "WPA2: AUTHENTICATION: PSK (PERSONAL) | 802.1X-EAP (ENTERPRISE); ENCRYPTION: AES-128 / CCMP."
  summary: |
    WPA2 起的标配加密：AES-128 算法配 CCMP 协议（计数器模式加密+CBC-MAC 完整性校验），取代 RC4+TKIP。WPA3 沿用 CCMP 但 Personal 认证换 SAE、Enterprise 可升级 AES-192。OV2500 里的枚举名即 WPA2_AES、WPA3_AES。选中它基本等于选中"当代合规"的最低安全线。

  tags: [aes, ccmp, wpa2, encryption]

- id: g26
  title: SAE（对等同步认证，WPA3-Personal）
  type: glossary
  source_chapter: "p295"
  source_quote: |
    "WPA/WPA2-Personal PSK replaced by WPA3-Personal SAE (Simultaneous Authentication of Equals): Stronger Encryption Key (128 bits), Offline dictionary attack resistance, No additional complexity to connect (user side)."
  summary: |
    WPA3-Personal 用 SAE（又称 Dragonfly 握手）替代 PSK 认证：密钥协商机制使攻击者无法离线跑字典爆破，加密密钥加强到 128 位；对用户而言连接操作与 PSK 一样简单（输密码即可）。OE2500 枚举里的 WPA3_SAE_AES 即此组合。混合 WPA2/WPA3 终端的环境要注意过渡模式兼容性。

  tags: [sae, wpa3, personal, dictionary-attack]

- id: g27
  title: PMF（受保护管理帧）
  type: glossary
  source_chapter: "p28/66"
  source_quote: |
    "Security: Use the latest security methods; Disallow outdated legacy protocols; Require use of Protected Management Frames (PMF). PMF (MANDATORY) in WPA3."
  summary: |
    对信标、去关联、去认证等管理帧做加密保护，防"伪造去认证帧踢人"这类廉价攻击。6E/WiFi6 的 6 GHz 频段把 PMF 列为强制要求，WPA3 也将其作为标配（WPA2 时代为可选）。OV2500 SSID 配置里对应 PMF 相关开关，混合老终端时是兼容性考量点。

  tags: [pmf, management-frames, wpa3, 6ghz]

- id: g28
  title: CNSA（WPA3-Enterprise 192 位模式）
  type: glossary
  source_chapter: "p295"
  source_quote: |
    "WPA/WPA2-Enterprise replaced by WPA3-Enterprise. Optional 192-bit security mode (CNSA option): CNSA enabled: Only wpa3 client authorized on the SSID; CNSA disabled: wpa2 or wpa3 clients authorized on the SSID; CNSA option not enabled on AP1101 only."
  summary: |
    WPA3-Enterprise 的可选 192 位国家安全套件：开启后 SSID 只放 WPA3 客户端（高安全场景如政府/军事），关闭则 WPA2/WPA3 混合接入。是"安全最大化 vs 终端兼容性"的开关。硬件限制：仅 AP1101 不支持该选项。

  tags: [cnsa, 192-bit, wpa3-enterprise, high-security]

- id: g29
  title: Captive Portal（强制门户）与 Walled Garden
  type: glossary
  source_chapter: "p78/343/500"
  source_quote: |
    "Guest Management: GUESTS -> Captive Portal -> Internet Access / Restricted access to the network. Guest SSID + Captive Portal option... Walled Garden: Allow a wireless client to access the URLs of the whitelist without authentication."
  summary: |
    强制门户是把未认证用户重定向到登录页的接入控制（HTTP 重定向，故需访问非 HTTPS URL 触发）；Stellar 方案里门户由 UPAM 提供（OV-UPAM Captive Portal，可定制模板，也支持外部门户+MAC 认证组合）。Walled Garden（围墙花园）是门户的白名单机制：放行清单内 URL 免认证访问（如登录页资源、赞助商页面）。配套运营功能：自助注册、员工赞助审批、社交登录、接入码、条款确认。

  tags: [captive-portal, walled-garden, guest, redirection]

- id: g30
  title: UPAM（统一策略认证管理器）与 BYOD
  type: glossary
  source_chapter: "p335-336"
  source_quote: |
    "UPAM consists of Guest Access (Guest License required), BYOD Access (BYOD License required), A built-in RADIUS Server, A built-in MAC Authentication Server... BYOD: Employee user access the corporate network with its personal device, Authentication via a BYOD Captive Portal."
  summary: |
    UPAM 内嵌于 OV2500 的统一接入控制平台，服务 AOS 交换机与 Stellar AP 两类设备：含 Guest Access、BYOD Access、内置 RADIUS、内置 MAC 认证服务器四大件。BYOD（自带设备办公）指员工用个人终端经 BYOD 门户认证后访问公司网，门户与用户库由 UPAM BYOD 模块管理（许可按设备数计）。认证源支持本地库或外接 LDAP/AD/RADIUS。

  tags: [upam, byod, radius, guest-access, ov2500]

- id: g31
  title: Band Steering 与 Load Balancing（频段引导/负载均衡）
  type: glossary
  source_chapter: "p76"
  source_quote: |
    "FEATURES: Load Balancing; Band Steering. CLIENTS CONNECTED: 10 / 8 (2.4 GHZ), 5 / 8 (5 GHZ)."
  summary: |
    企业级 AP 的两项智能调度特性：Band Steering（频段引导）把双频终端推向 5/6 GHz，避免挤在拥挤的 2.4 GHz；Load Balancing（负载均衡）按各 AP 关联终端数把新终端引导到较空的 AP，平衡空口负载。Ekahau Auto-Planner 里也有对应开关（p118）。两者都是"企业无线 vs 家用无线"的差异化功能（p76-77 同类还有无缝漫游、QoS/ACL）。

  tags: [band-steering, load-balancing, features, enterprise-ap]

- id: g32
  title: AP Group（AP 组）
  type: glossary
  source_chapter: "p161/271"
  source_quote: |
    "AP Group: Multiple APs in the same AP Group, sharing the same configuration. Mix of any AP type & total number of AP limited to 4000 (Enterprise) or 255 (Express). When an AP initially registers, the AP is placed into a pre-configured 'Default' AP Group."
  summary: |
    OV2500 的配置管理单位：同组 AP 共享管理 VLAN、RF Profile、WCF、Data VPN 等属性，任何对组下发的配置同步全组。Enterprise 上限 4000 台（可多组）、Express 255 台，组数无限制，新注册 AP 自动入 Default 组。SSID 通过"绑定 AP Group+时间表"决定在哪些 AP 上广播。Express 模式里 AP-Group 则是靠 Group ID 相同而自组集群的概念（p149），同名不同机制。

  tags: [ap-group, configuration, ov2500, scale]

- id: g33
  title: RF Profile（射频档案）
  type: glossary
  source_chapter: "p243/297/424"
  source_quote: |
    "Country Code matches RF profile CC... AP Group -> RF Profile -> Specific RF Profile... Use the Roaming RSSI Threshold in the RF profile. Value range is 0-100."
  summary: |
    射频参数模板，挂在 AP Group 下：含国家码（与 AP 国家码不一致即注册失败、射频全关）、信道/功率策略、Roaming RSSI 阈值（0-100，推荐 2.4G=10/5G=15）等。专家模式对象模型里 AP Group→RF Profile 与 WLAN Service→AAA/Access Role 是两条并行的配置链（p297）。改漫游行为、换国家码都从它入手。

  tags: [rf-profile, country-code, rssi-threshold, radio]

- id: g34
  title: DHCP Option 138（CAPWAP/网管发现选项）
  type: glossary
  source_chapter: "p156"
  source_quote: |
    "DHCP option 138 equals the IP address of the OmniVista 2500 Server... option 138 192.168.0.61."
  summary: |
    DHCP 选项 138，Stellar 用它携带网管地址：AP 收到带 138 的 DHCP Offer 即从默认 Express 模式切换到 Enterprise（值=OV2500 IP）；Cirrus 云管则用 option 43。isc-dhcp 需自定义 `option ovwma code 138 = ip-address;`，OmniSwitch 原生支持 `option 138`，Windows Server 在预定义选项里加 Code 138/IP Address（p278）。排障 AP 找不到网管第一查项（ce07）。

  tags: [dhcp, option-138, enterprise-mode, onboarding]

- id: g35
  title: Access Role Profile（接入角色档案）
  type: glossary
  source_chapter: "p301"
  source_quote: |
    "An Access Role Profile contains the various UNP properties for the users assigned to this profile: QOS Policy List, Captive Portal Authentication, Bandwidth Controls. The Default Access Role Profile is assigned to the VLAN ID of the SSID."
  summary: |
    用户角色的属性包：拿到该角色的用户即获得其中的 UNP 属性——QoS Policy List、门户认证、带宽控制，并映射到 SSID 的 VLAN。来源有三：RADIUS 返回（含 LDAP 角色映射）、802.1X/MAC 认证结果、SSID 的 Default Access Role Profile 兜底。命名惯例：SSID 向导自动生成 "__SSID 名" 形态的角色（如 __Guests0）。WCF Profile 也绑在它上面（一对一）。

  tags: [access-role-profile, unp, vlan-mapping, user-role]

- id: g36
  title: AAA Server Profile（认证授权计账服务器档案）
  type: glossary
  source_chapter: "p302"
  source_quote: |
    "An AAA Server Profile is mandatory when the security level is set to Enterprise or Personal. The AAA Server Profile defines: 802.1x Authentication Servers, MAC Authentication Servers, Captive Portal Authentication Servers, Accounting Servers. The Default UPAM Server can be chosen by default."
  summary: |
    把四类服务器（802.1X 认证、MAC 认证、门户认证、计账）打包的档案，Enterprise/Personal 安全级下必选；默认可指到内置 UPAMRadiusServer（RADIUS 端口 1812/1813）。AP 侧落地为 AAA_profile.conf/AAA_server.conf。系统内置 NAS 条目 "All Managed Devices" 把所有受管设备自动纳入 UPAM 的 NAS 库，共享密钥 123456（p322）。

  tags: [aaa, radius, profile, authentication]

- id: g37
  title: Policy List / User Role（策略清单与用户角色）
  type: glossary
  source_chapter: "p360"
  source_quote: |
    "User Role = Policy List: List of Policy Rules (QoS, ACLs). Action can be: Accept/drop, Bandwidth control, Priority, 802.1p, DSCP marking, Application Policy Rules (DPI). Enforcement is bidirectional. Policy List Assignment: From RADIUS, From Access Role Profile (Default Policy List)."
  summary: |
    在 OV2500 对象模型里 User Role 就是 Policy List：一串有序策略规则，动作可为放行/丢弃、限速、优先级标记（802.1p/DSCP）乃至 DPI 应用规则（基于约 2000 个应用的签名库），执行是双向的。分配来源：RADIUS 动态下发或 Access Role Profile 的默认清单。内置角色有 Redirection（UPAM 重定向）与 Unauthorized（时间/位置策略）。构建入口在 Unified Access > Unified Policy。

  tags: [policy-list, user-role, acl, qos, dpi]

- id: g38
  title: WCF（Web 内容过滤）
  type: glossary
  source_chapter: "p366"
  source_quote: |
    "Web Content Filtering: Stellar AP DNS Snooping -> FQDN category lookup (Brightcloud SDK) -> Send Allow/Block status to Stellar AP -> ACL allow/block IP destination."
  summary: |
    基于 DNS 嗅探的网页过滤：AP 截获客户端 DNS 查询，向 OV2500（内嵌 Brightcloud 分类 SDK）查询 FQDN 类目与策略，AP 据此生成允许/阻断 ACL 到解析 IP，后续流量本地拦截。WCF Profile 定义各类目 Accept/Reject（默认全放行），绑定到 Access Role Profile（一对一）；激活粒度按 AP Group 或单 AP；前提是 OV2500 配好 DNS，AP1101/AP1201H 不支持。许可按 1:10 AP。

  tags: [wcf, dns-snooping, brightcloud, category]

- id: g39
  title: Client Context（客户端上下文）
  type: glossary
  source_chapter: "p411"
  source_quote: |
    "Client Context Content: SSID & WLAN service, MAC Address, IP Address, Currently assigned Unified Access (VLAN ID, Access Role Profile, Policy List, Redirect-URL, Captive Portal status), AP Context, Fast Roaming: PMKSA cache, FT PMK R0/R1 cache."
  summary: |
    AP 间共享的终端档案，漫游的原材料：网络侧含 SSID/WLAN Service、MAC/IP、当前 VLAN/角色/策略/重定向 URL/门户状态；AP 侧含 MAC、IP、OV 地址；快速漫游密钥缓存（PMKSA、FT PMK R0/R1）也随上下文携带。共享机制：终端关联时 AP 向空口邻居广播 Add、去关联时发 Del，新 AP 的 Add 触发旧 AP 删档；接收端若不是同一 OV 管理或没有对应 WLAN Service 则丢弃。L2/L3 漫游判定完全基于它（f13）。

  tags: [client-context, roaming, add-del, key-cache]

- id: g40
  title: L2 漫游与 L3 漫游
  type: glossary
  source_chapter: "p406"
  source_quote: |
    "Roaming relies on client context sharing between over the air adjacent APs. L2 or L3 Roaming selection based on the client VLAN between home and foreign AP. L3 Roaming based on L2 GRE tunnel between home and foreign AP. L2 Roaming always enabled; L3 Roaming disabled by default."
  summary: |
    两种漫游形态：L2 漫游——home/foreign AP 映射到同一 VLAN，终端直接切换（默认开启，无感）；L3 漫游——两侧 VLAN 不同，靠 home/foreign AP 间的 L2 GRE 隧道把终端流量送回原网段保持 IP 不变（默认关闭，Advanced WLAN Service 里开）。判定规则见框架 f13。Express 模式漫游仅限同集群内 L2。

  tags: [l2-roaming, l3-roaming, gre, vlan]

- id: g41
  title: 快速漫游术语组（OKC / 802.11r / 802.11k / 802.11v 与粘性终端）
  type: glossary
  source_chapter: "p414-417/424"
  source_quote: |
    "Support OKC (802.11k) and 802.11r. OKC / 802.11k: PMK (Pairwise Master Key) caching... Re-auth reduced to 4-way handshake. 802.11r / Fast BSS Transition (FT): Initial handshake for PTK/GTK with the new AP is done before the client roams. 802.11v (BSS Transition Management): Obtain Roaming target APs. 802.11k: Guide client to roam to best connection AP."
  summary: |
    降低漫游切换时间的组合拳：OKC（机会式密钥缓存，教材标注 802.11k）缓存 PMK，终端可在关联请求里带 PMKID，重认证压缩为 4 次握手建 PTK/GTK，仅限 WPA2/WPA3 Enterprise；802.11r（FT 快速 BSS 切换）在漫游发生前就完成与新 AP 的密钥握手，支持 Over-the-Air 与 Over-the-DS 两种模式，适用 WPA2/WPA3 加密；802.11v（BSS 过渡管理）向终端提供漫游目标 AP 列表；802.11k 引导终端漫游到最优 AP。粘性终端（Sticky Client）指该走不走的终端，靠 RF Profile 的 Roaming RSSI 阈值（2.4G=10/5G=15）加 11k/11v 治理。PMK 缓存始终存于客户端上下文，FT R0/R1 缓存仅在开 11r 时才有。

  tags: [fast-roaming, okc, 802.11r, 802.11k, 802.11v, ft, pmk]

- id: g42
  title: RAP（远程接入点）
  type: glossary
  source_chapter: "p429-430"
  source_quote: |
    "RAP = Remote Access Point. Goal: Extend the corporate network to remote site(s). Shops > Access to the corporate network to check the inventory; Booth > Events. Equipment: OmniVista Cirrus 4 (Freemium with OV2500 / Premium) + ALE VPN Server + Stellar AP (AP1101 not compatible)."
  summary: |
    把一台 Stellar AP 放到分支/家庭，经互联网与总部 ALE VPN Server 建隧道，本地广播企业 SSID、终端流量经 VPN 回公司网的管理形态。适用门店查库存、展会展位、居家办公（可本地突围 Local Breakout+VLAN 标签区分业务）。配套：Cirrus 4 云管做零接触注册（Freemium 配 OV2500 或 Premium 全云）、ALE 提供的 VPN Server 虚机；AP1101 不兼容 RAP。上线流程见 f15/c10。

  tags: [rap, remote-ap, vpn, branch, cirrus]

- id: g43
  title: GRE 隧道（L2GRE 与 Guest Tunneling）
  type: glossary
  source_chapter: "p345/485"
  source_quote: |
    "Guest Tunneling: Overlay Guest network while preserving Enterprise security. Tunnel per Access Role Profile from Access Point to a switch/router/controller. L2 GRE tunnel over L2/L3 networks... Supported switches: OS6860, OS6900. Supported routers: Nokia 7750."
  summary: |
    GRE（通用路由封装）在 Stellar 方案里的两种用法：Guest Tunneling 把访客流量按 Access Role Profile 从 AP 用 L2 GRE 隧道送到集中出口（OmniSwitch 自动建隧道、OS6860/6900 支持，也支持 7750 路由器与第三方控制器），实现访客网与企业网的物理隔离叠加；RAP 场景则用 L2GRE 做"客户端数据流量"的第二条 VPN（OV2500 > Data VPN Servers 配置，Server IP+客户端池，SSID 的 Default VLAN 选 Use Tunnel + Tunnel ID 0）。

  tags: [gre, l2gre, guest-tunneling, tunnel, rap]

- id: g44
  title: WMM 与 UAPSD（无线 QoS 与省电）
  type: glossary
  source_chapter: "p501/504"
  source_quote: |
    "UAPSD: Unscheduled Automatic Power Save Delivery is a QoS facility defined in IEEE 802.11e that extends the battery life of mobile clients. WMM QoS: Four categories; QOS treatment per category: Uplink 802.1p/DSCP, Downlink 802.1p/DSCP."
  summary: |
    WMM（WiFi 多媒体）是 802.11e 的 QoS 框架，分四类队列：Voice、Video、Best Effort、Background，每类可独立设置上/下行 802.1p 与 DSCP 标记（推荐映射见 p34：Voice=5/46-EF、Video=4/34-AF41、Background=2/18、Best Effort=0/0）。UAPSD（非调度自动省电交付）是同在 802.11e 里定义的 QoS 省电设施，延长移动终端电池寿命，作为 SSID 高级选项开关。

  tags: [wmm, uapsd, qos, 802.11e, dscp]

- id: g45
  title: Hotspot 2.0 / Passpoint 与 WiFi4EU
  type: glossary
  source_chapter: "p506"
  source_quote: |
    "Hotspot 2.0: Deliver seamless and secure network (WPA2 or WPA3 Enterprise) for clients in public spaces. Stellar Access Point support 802.11u (GAS/ANPQ), EAP-SIM / EAP-AKA... WiFi4EU: European Union Initiative to provide free WiFi access to citizen in public venues; HTTPS Captive Portal; Session timeout configurable up to 12 hours."
  summary: |
    Hotspot 2.0（Passpoint）让手机在公共场所自动发现并接入可信任网络：AP 广播 802.11u（GAS/ANQP）能力信息，终端可用 EAP-SIM/EAP-AKA 以运营商凭据认证（对接 Home AAA/HLR），实现 3G/4G 流量卸载到 WiFi。WiFi4EU 是欧盟公共场馆免费 WiFi 计划，要求 SSID 用 HTTPS 强制门户、会话超时可配到 12 小时。前者配在 WPA2-Enterprise SSID 的高级选项，后者配在 Guest SSID 的 Guest Access Strategy（p507）。

  tags: [hotspot-2.0, passpoint, 802.11u, eap-sim, wifi4eu]
