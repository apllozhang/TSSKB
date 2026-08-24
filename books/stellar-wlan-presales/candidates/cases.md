# 案例/实例候选 · OmniAccess Stellar WLAN Presales Ed28
# 提取来源：source/fulltext.md（273 页全书）；页码均为书内 <<<PAGE n>>> 标记。
# 引用原文均 ≤100 英文词，摘自书中原句。

- id: c01
  title: 四院合并的千床医院整体更换 Aruba 无线网
  type: case
  source_chapter: "p171-174"
  source_quote: |
    "Recently, an hospital merged with 3 others for a total of 1000 beds. Maternity center, retirement home with an ALZHEIMER unit, emergency service, IRM etc.. The given activity is 15 000 admissions, 50 000 consultations, 30 000 medical imaging taken, 95% occupation rate in retirement home... Total staff 1500 including 1100 caregivers. Replacement of the existing Aruba infrastructure."
  summary: |
    客户背景：一家医院与另外 3 家合并，共 1000 张床位；含妇产中心、带阿尔茨海默病区的养老院、急诊、核磁共振（IRM）等；年活动量 15,000 住院、50,000 门诊、30,000 医学影像，养老院入住率 95%；员工 1500 人（护理人员 1100）。
    挑战：医院整体翻新，重建 Wi-Fi 基础设施以提升医疗团队与患者服务；替换存量 Aruba 网络。
    方案：保留 HPE 存量 LAN 与 OXE 话机做 VoWLAN；中心院区与远程站点 2 部署室内 AP1321；医疗员工双认证方式（远程站点 PSK、中心站点 WPA2）；远程站点 2 用 2 个 SSID（Internal_staff、Guests），访客由 UCOPIA 做 QoS/带宽画像；中心站点 3 个 SSID（Internal_staff、IoT、Nurse_Education & Guests），访客 URL 过滤同样用 UCOPIA；ALE 专业服务（PRO services）支持部署；p174 给出远程站点经 VPN MPLS 连中心站点（OV2500）的拓扑。
    Why ALE：BP/ALE 联合投入 POC，现场演示行业规范要求的医疗专项认证（Healthcare specific Certifications）特性对比竞品；无控制器分布式架构（不集中于单台控制器）是关键制胜技术点；部署快、管理简单。
    收益：员工 PC 从 2.4GHz 迁移到 5GHz 后带宽显著提升，生产力与员工满意度提高；功能/性能/经济比非常好。
  tags: [healthcare, replace-aruba, vowlan, ap1321, ucpia, psk-wpa2, distributed-architecture, ale-proserv]

- id: c02
  title: 五星酒店升级为宫殿式酒店的全楼 802.11ac wave2 改造
  type: case
  source_chapter: "p175-178"
  source_quote: |
    "The HOTEL 5* group currently houses around 90 coffee shop and a 5* hotel in the capital. Decision to extend the hotel sector with another hotel in the country and others around the world. The Hotel from the capital evolves to become a palace with three annex buildings... 8 SSID in the HOTEL 5*, 64 clients associated per AP and per radio."
  summary: |
    客户背景：某集团旗下拥有约 90 家咖啡店和首都一家五星级酒店，决定在国内再开一家、全球多店扩张，首都店升级为宫殿式（palace）酒店并带 3 栋附楼。
    挑战：每间客房必须独特并在电视上达到影院级体验（带宽性能硬指标），宾客 Wi-Fi 须用最新 802.11ac wave2 技术；一层餐厅也要最好带宽；酒店用 IoT 家居自动化设备，需严格安全的识别与流管理；Wi-Fi 至关重要，须有实时仪表盘描述每台 AP 状态；方案要能扩展到 3 栋附楼。
    方案：基于 ALE OmniSwitch + Stellar AP：室内 AP1321/AP1322、室外 AP1361；接入交换机 6360-P24、OS6560-P48，核心 6860E-48 虚拟机箱（Virtual Chassis）；全店 8 个 SSID，每 AP 每射频 64 个关联客户端；OmniVista 做 LAN/WLAN 统一管理；BP 用 Ekahau 做装后审计，总体良好但个别区域带宽低，发现信道重叠问题，通过缩窄这些 AP 的信道宽度解决；机房施工需防石膏粉尘；计划在 Wi-Fi 上承载 Rainbow VoIP（员工）。
    Why ALE：客户要 CAPEX 一次性拥有常新设备，不愿为老化设备持续付 OPEX；Stellar AP/6860E 上的 DPI 可监控宾客用量并限制员工流量；支持客人用 Apple TV 或 Chromecast 只在自己房间电视投屏；价格/性能/功能比最优；统一 LAN/WLAN 管理对最终客户极其有用。
  tags: [hospitality, hotel, ap1321, ap1322, ap1361, os6560, os6860e, omnivista, dpi, ekahau, chromecast, rainbow]

- id: c03
  title: 理工大学替换 Cisco 无线网并兼容 EDUROAM（600 AP 演进）
  type: case
  source_chapter: "p180-182"
  source_quote: |
    "This University of Technology hosts 4000 students and 600 staff spread over 3 sites. Renewal of existing Wi-Fi infrastructure (Cisco). Deployment of an evolutionary Wi-Fi solution supporting 600 Aps at the end of the project... EDUROAM SSID Authentication Compatibility. Authentication types: 802.1x, Peap MSvchap, WPA2... ALE solution deployed in phase 1 : Indoor AP (AP1321) & OV Cirrus."
  summary: |
    客户背景：某理工大学属全国理工大学网络成员，4000 名学生 + 600 名员工，分布 3 个校区。
    挑战：翻新存量 Cisco Wi-Fi；部署可演进的方案，项目终期支持 600 台 AP；访客（Guest）安全接入既有 Captive Portal。
    方案：保留 HPE 存量 LAN；替换思科旧无线；EDUROAM SSID 认证兼容；认证方式 802.1X / PEAP MS-CHAPv2 / WPA2；访客用开源 Captive Portal「Chillispot」；一期部署室内 AP1321 + OmniVista Cirrus 云管理。
    Why ALE：无控制器（controllerless）架构显著降低维护成本；BP/ALE 联合投入 POC（OmniVista 演示 + 覆盖测试）；部署快、管理简单；访客流量经 OS6860 上的 GRE 隧道保障安全；OmniVista 集中管理容易；分布式架构；可向三校区全覆盖演进。
    收益点：换掉 Cisco 后维护成本下降，访客隔离有 GRE 隧道兜底。
  tags: [education, university, replace-cisco, eduroam, 8021x-peap, ap1321, ov-cirrus, gre-tunnel, os6860]

- id: c04
  title: 文理学院换掉 Ubiquiti：混凝土墙+雷暴环境的移动校园
  type: case
  source_chapter: "p184-186"
  source_quote: |
    "College of liberal arts. This College hosts 350 students and 50 staff on one site. Renewal of existing Wi-Fi infrastructure (Ubiquiti). Environmental challenges: Thick concrete walls, lack of accessible cabling, thunderstorms. Robust hardware required. Flexible solution that can accommodate the 400 daily users or up to 2000 users during events."
  summary: |
    客户背景：某文理学院（College of liberal arts），单校区 350 名学生 + 50 名员工。
    挑战：替换存量 Ubiquiti 无线网；环境恶劣：厚混凝土墙、缺少可访问布线、雷暴天气；需坚固（robust）硬件；方案要能弹性支撑日常 400 用户、活动时最多 2000 用户。
    方案：基于第三方（third-party）LAN 交换机 + Stellar AP：室内 AP1321、室外 AP1361；3 个 SSID：Students、Staff、Guest；认证 802.1X / PEAP MS-CHAPv2 / WPA2；访客用 OmniVista 内置 Captive Portal；OmniVista Cirrus 由业务伙伴（BP）远程运维监管。
    Why ALE：无控制器架构显著降低维护成本；BP/ALE 深度参与勘测（site survey）与实施阶段；与第三方 LAN 交换机完全互通 + BP 远程管理；近两年硬件零故障；价格最具竞争力、维护成本低；用户体验：室内外全覆盖，礼堂/报告厅等高密地点无连接问题。
  tags: [education, college, replace-ubiquiti, ap1321, ap1361, third-party-lan, ov-cirrus, outdoor, high-density, remote-managed-by-partner]

- id: c05
  title: 20 艘轮渡船队全船 Wi-Fi：客舱视频点播与金属船体覆盖
  type: case
  source_chapter: "p188-190"
  source_quote: |
    "The fleet consists of twenty ferries that can carry up to 1500 passengers. Provide the best Wifi bandwidth for the passengers of each cabin. Video On Demand and Data are the main services to be delivered on the Guest SSID... External AP1251 required for the bridge. The metallic structure of the ferry impacts the radio coverage."
  summary: |
    客户背景：某轮渡公司经营多港口间车辆/乘客日常航线，船队 20 艘渡轮，单船最多 1500 名乘客。
    挑战：为每间客舱提供最佳 Wi-Fi 带宽；Guest SSID 主打视频点播（VoD）+ 数据；Staff SSID 提供数据；另有员工 BYOD SSID；替换既有 Wi-Fi 方案；船桥（bridge）需要室外 AP1251；金属船体结构影响无线覆盖。
    方案：ALE OmniSwitch + Stellar AP：室内 AP1301H/AP1321、室外 AP1361；接入交换机 6460，核心 6900-X72 虚拟机箱；4 个 SSID（Guest、Crew、BYOD Crew、VoD）；OmniVista 统一 LAN/WLAN 管理；ALE ProServ 用 Ekahau 做安装前审计，因金属船体结构优化 Stellar AP 布放；为覆盖全部桥区增加了室外 AP1251 数量。
    Why ALE：BP/ALE 深度参与方案设计（现场勘测、POC）；船上空间有限，必须无控制器架构；Stellar AP/6860E 上 DPI 监控乘客用量、必要时限带宽。
    收益：Wi-Fi 覆盖与带宽提升；所有客舱可享受视频点播新服务。
  tags: [transportation, maritime, ferry, ap1301h, ap1321, ap1361, ap1251, os6460, os6900, vod, dpi, ekahau, controllerless]

- id: c06
  title: 市立音乐学院：百台 AP1321 的智慧城市数字化改造
  type: case
  source_chapter: "p192-194"
  source_quote: |
    "Created in the late 19th century, the music conservatory is managed by the city. The music conservatory hosts 200 users (students and staff included) and occasionally hosts events for 300 guests. Existing architecture: 10 x 6900-x20 & 20 x 6460, interco with CISCO equipment, 2 FW Palo Alto for application filtering... Internal WLAN network with 100 AP Stellar 1321."
  summary: |
    客户背景：某音乐学院创建于 19 世纪末，由市政府管理（归入政府/智慧城市场景）；日常 200 用户（学生+员工），偶尔举办 300 名嘉宾的活动。
    挑战：为学院员工及各类演员、嘉宾提供专用 Wi-Fi 服务；通过更好的 Wi-Fi 改善公众接待。
    方案（技术描述）：存量架构 10 台 6900-X20 + 20 台 6460 交换机、与思科设备互联、2 台 Palo Alto 防火墙做应用过滤；已装最新 AOS R8、4 台 6900 启用 Intelligent Fabric；Stellar Enterprise 方案且 OV Cirrus 已部署；内部 WLAN 共 100 台 Stellar AP1321；OmniVista 经 Kiwi 服务器管理企业（员工）SSID 的 syslog；Guest SSID 集成 UCOPIA 门户；员工认证经 UPAM 对接外部 LDAP；访客门户为 OPEN 模式+条款确认（最多 500 个活跃会话）；LAN/WLAN 统一在 OmniVista 管理。
    Why ALE：BP/ALE 深度参与设计与部署；部署快、管理简单；带宽提升带来生产力与员工满意度；学院在数字化/智慧城市方向现代化；方案功能/性能/经济比非常好。
  tags: [government, smart-city, music-conservatory, ap1321, os6900, os6460, palo-alto, ov-cirrus, upam, ldap, ucpia, open-guest-portal]

- id: c07
  title: 零售连锁 40+ 门店：ESL 电子价签经 Stellar AP USB 口供电联网
  type: case
  source_chapter: "p196-198"
  source_quote: |
    "Over 40 retail stores across the country. OmniAccess Stellar WLAN solution already deployed in the stores. OmniVista Cirrus 10 used to manage and monitor the 150 Stellar Access Points (AP1301, AP1311, AP1251). All the paper shelf labels are replaced by Electronic Shelf Labels (ESL)... Proprietary ESL USB dongle -> Selected. To be connected to the existing Stellar infrastructure. Minimal impact for deployment."
  summary: |
    客户背景：全国 40+ 家零售门店；店内已部署 OmniAccess Stellar WLAN；OmniVista Cirrus 10 管理监控 150 台 Stellar AP（AP1301、AP1311、AP1251）。
    新需求：全部纸质货架价签换成电子价签（ESL）；收益是价格与库存可远程更新、标签可定位（闪烁提示）；市面多厂商方案用不同波长：低频 38.4kHz、红外、高频 2.4MHz。
    选型（Hanshow 方案二选一）：专用 ESL 发射器——需新布线+新装设备，未选；专用 ESL USB dongle——接到既有 Stellar 基础设施，部署影响最小，选中。
    技术描述：Stellar AP 侧激活 USB Type A/C（母）口；ESL USB dongle 为 USB-C（公）头，用 USB 线连接；AP 以 Express 或 Cloud 模式由 OmniVista Cirrus 管理，可广播 2.4/5/6 GHz SSID；dongle 由 USB 口取电联网，用 2.4GHz 专有射频连 ESL 标签，并连 Hanshow 云做管理与配置。
    竞品/替代点：对比"新装发射器"方案，复用既有 AP USB 口是核心卖点。
  tags: [retail, esl, electronic-shelf-label, usb-dongle, hanshow, ov-cirrus-10, ap1301, ap1311, ap1251, iot]

- id: c08
  title: 产品实例：AP1301H 客房型 Wi-Fi 6 AP（医院/酒店/轮渡客舱）
  type: case
  source_chapter: "p17"
  source_quote: |
    "OMNIACCESS STELLAR AP1301H • Dual radio • 2.4GHz radio: 573.5Mbps (2x2:2SS/HE40) • 5GHz radio: 1.2Gbps (2x2:2SS/HE80) • 1 full band (radio) dedicated to radio scanning... Up to 32 SSID (16 per radio). 1024 clients per AP. 1 x 1GE PoE (802.3at/af) uplink port. 1 x 1GE PoE-PSE (802.3af) downlink port. 3 x 1GE downlink port. 1 x USB2.0, 1 x RJ45 console passthrough."
  summary: |
    产品定位：书称 Indoor Hospitality Wi-Fi 6 Access Point（客房/病房壁挂型），在本医院换 Aruba 场景之外的轮渡客舱（c05）与部署指南客房公式（c18）中被实际使用。
    规格：双频 2x2（2.4G 573.5Mbps + 5G 1.2Gbps）+ 1 个全频段专用扫描射频（提升安全与 Wi-Fi 质量）；MU-MIMO；32 SSID（每射频 16）；1024 客户端/AP；上行 1GE PoE（802.3at/af）；下行 1GE PoE-PSE（802.3af，可给下挂设备供电）+ 3 x 1GE 数据口 + USB2.0 + RJ45 控制台直通；内置全向天线；0-45°C、plenum rated。
    售前要点：下联 PoE 出电 + 多网口 + 控制台直通，适合每间房一台、房内有线终端/话机接入的酒店与医疗病房场景。
  tags: [product, ap, ap1301h, wifi6, hospitality, healthcare, poe-out, pass-through]

- id: c09
  title: 产品实例：AP1231 三射频 Wi-Fi 5 高端 AP 与高密场馆选型
  type: case
  source_chapter: "p15, p249-252"
  source_quote: |
    "OMNIACCESS STELLAR AP1230 SERIES • Tri radio • First 5GHz radio: 1,733Mbps (with 4SS/VHT80 clients or 2SS/VHT160 clients) • Second Multiband radio: 1,733Mbps... • Third 2.4GHz radio: 800Mbps 2.4GHz (4SS/VHT40)... Up to 24 SSID (8 per radio). 768 client devices per AP... High-end AP • 802.11ac Wave 2 MU-MIMO"
  summary: |
    产品规格：Wi-Fi 5 旗舰三射频 AP（OAW-AP1231 内置天线 / OAW-AP1232 外置天线接口）；两路 5GHz 多频段射频各 1,733Mbps + 2.4GHz 800Mbps；MU-MIMO、内置 BLE；24 SSID（每射频 8）；768 客户端/AP；1xGbE + 1x2.5GbE 网口、RJ45 控制台、USB；802.3at PoE（4 对 60W）或 48V DC。
    书中用法（p249 高密场馆）：场馆容量 1500 人、估计并发 <50%（约 750 活跃用户）时，Wi-Fi 5 选 AP1231（三射频卡：2.4G 4x4 + 5G 低频 4x4 + 5G 高频 4x4 + 2.5Gbps 网口），或 Wi-Fi 6 选 AP1321；建议 8-10 台 AP；2.4G 只用 1/6/11 且部分 AP 关 2.4G；推荐 2.5G 上联 + OmniSwitch 6560（802.3bt）避免有线瓶颈。
    备注：p91 热图示例图注出现同系 OAW-AP1221；p154 Cirrus 10 许可分类 AP1x2x 列有 1221。（全书正文的三射频 Wi-Fi 5 型号为 AP1231/AP1232。）
  tags: [product, ap, ap1231, ap1232, wifi5, tri-radio, high-density, ble, os6560]

- id: c10
  title: 产品实例：AP15xx Wi-Fi 7 系列（AP1511 入门 / AP1521 中档）
  type: case
  source_chapter: "p26-27"
  source_quote: |
    "OMNIACCESS STELLAR AP1521 • Tri radio • 2.4GHz radio: 688Mbps (2x2:2SS/EHT40) • 5GHz radio: 2.88Gbps (4x4:4SS/EHT160) • 6GHz radio: 5.76Gbps (2x2:2SS/ EHT320)... 1 x 1/2.5/5/10GE multi-gigabit uplink... 802.3bt POE (up to 60W) compliant... Mid-range Wi-Fi 7 AP • 802.11be (Wi-Fi 7) – Indoor AP"
  summary: |
    Wi-Fi 7（802.11be）室内系列两款：
    AP1511（Premium entry，入门偏高档）：三射频 2.4G 688Mbps（EHT40）+ 5G 2.88Gbps（EHT160）+ 6G 5.76Gbps（EHT320）；32 SSID；512 客户端；1 x 1/2.5/5GE 多千兆上行；802.3at/bt 最高 35W；0-50°C；内置 BLE5.1/ZigBee。
    AP1521（中档）：5GHz 升为 4x4:4SS；1 x 1/2.5/5/10GE 上行 + 1 x 1GE 下行；802.3bt 最高 60W、低功率模式 802.3at 15W；0-50°C。
    售前背景（p36-37 Wi-Fi 7 技术）：320MHz 信道（吞吐 5 倍，46Gbps vs Wi-Fi 6E 9.6Gbps）、4096-QAM（+20% 原始速率）、MLO 多链路操作、MRU、前导码穿孔、AFC；Wi-Fi 7 定位更低时延与更高密容量。
  tags: [product, ap, wifi7, ap1511, ap1521, eht320, mlo, 4096-qam, multigig]

- id: c11
  title: 产品实例：VoWLAN 话机产品线 8118/8128/8158s/8168s 与移动语音
  type: case
  source_chapter: "p202-203"
  source_quote: |
    "ENTERPRISE HANDSET • Handsets • ALE NOE & SIP standard protocols handled • Key Features • Seamless Roaming • Power Save • Real-time handset location (Ekahau RTLS for OT8168s and OT8128) • For industrial use 8168s. • Handset Management & Alarm Tool... 8118 8128 8158s 8168s ASCOM"
  summary: |
    企业话机四款：8118、8128、8158s、8168s（8168s 为工业级；OT8168s 与 OT8128 支持 Ekahau RTLS 实时定位）。
    关键能力：支持 ALE NOE 与 SIP 标准协议；无缝漫游；省电；话机管理与告警工具。
    配套：IMS3 Mass Deployment Server（批量部署）、USB 配置底座；配件含机架充电器、电池机架充电器、皮带/旋转夹、携带套、桌面充电器、电池。
    移动/软终端语音（p203）：Rainbow UCaaS 客户端、Rainbow 与 OXO/OXE 集成、OTC 移动应用、非 ALE 软电话（Facetime 等）；802.11r/k/v 协议辅助漫游；iOS 8 及以上；三星 Galaxy S7 起步、802.11v 需 S9 起；语音质量随终端硬件/OS 而异。
    适配（p204）：所有 Stellar AP 均支持语音，需将 AP 升级到最新版本。
  tags: [product, vowlan, handset, 8118, 8128, 8158s, 8168s, ims3, rainbow, ascom, ekahau-rtls, 802-11rkv]

- id: c12
  title: 互操作案例：Aruba AP 向 Stellar 过渡的两种共存路径
  type: case
  source_chapter: "p117"
  source_quote: |
    "Aruba AP to Stellar Solution transition ◼Case A: Integration of a new Stellar infrastructure with an already installed Clearpass server... ◼Case B: New OmniVista server used to authenticate an already installed Aruba Controller/IAP base"
  summary: |
    书中"互操作特性"章给出的 Aruba 替换过渡双路径：
    Case A：客户已有 Aruba ClearPass 认证服务器，新建 Stellar 网络直接对接存量 ClearPass 完成认证（Stellar AP + ClearPass）。
    Case B：反向场景，用新 OmniVista/UPAM 服务器为存量 Aruba Controller/Instant AP（IAP）基站提供认证（OV/UPAM + Aruba Controller/IAP）。
    售前用途：竞品替换项目中，认证层面可先行共存/接管，避免一次性割接风险。
  tags: [interoperability, replace-aruba, clearpass, migration, coexistence, upam, omnivista]

- id: c13
  title: 用例：Zigbee 集成客房电子门锁（集中管理数字钥匙）
  type: case
  source_chapter: "p98"
  source_quote: |
    "IOT - ZIGBEE • Zigbee • IoT protocol commonly used for home and building automation • Aim • Manage the Zigbee endpoints from the OmniVista • Advantages • Improved guest experience (ex. digital key management)... USE CASE : INTEGRATION WITH DOOR LOCKS (CENTRALIZED MANAGEMENT OF GUESTROOM DIGITAL DOOR LOCKS)"
  summary: |
    用例内容：与门锁集成，实现客房电子门锁集中管理。
    技术路径（p98 配图）：门锁（Zigbee2006）无线连 Stellar AP，AP 经 HTTP 隧道连 Assa Abloy 服务器。
    能力范围：Zigbee 是家居与楼宇自动化常用 IoT 协议；除 AP1301 与 AP1230 系列外，所有 Stellar AP 均兼容（内置 BLE/ZigBee）；目标是从 OmniVista 统一管理 Zigbee 终端。
    收益：宾客体验提升（数字钥匙管理）、安全管控增强、IT 服务自动化。
  tags: [iot, zigbee, door-lock, digital-key, hospitality, omnivista, assa-abloy]

- id: c14
  title: 用例：AeroScout RTLS 实时定位与 Stellar AP 集成
  type: case
  source_chapter: "p119"
  source_quote: |
    "Integration with AeroScout Location Engine. AeroScout RTLS (Real Time Location Services) provides location services. i.g: Tracking of employees in the building at the plant. Customers use the Stellar AP to communicate with AeroScout tags and deliver information to the AeroScout Location Engine."
  summary: |
    用例内容：AeroScout 实时定位服务（RTLS）基于标准 Wi-Fi（802.11）基础设施运行，复用 Stellar AP 作为采集网元。
    架构四要素：AeroScout 标签按预设间隔发 802.11 报文；Stellar AP 把标签与 Wi-Fi 客户端的 RSSI 测量值送达引擎；AeroScout Engine Server（AES）基于 RSSI 计算位置；AeroScout Engine Manager（AEM）做配置、地图展示、热图、分析与地理围栏告警。
    书中示例场景：厂房内员工追踪。
    售前要点：无需新建定位专网，客户既有/新建 Stellar 网即可承载资产与人員定位。
  tags: [rtls, location-tracking, interoperability, iot, asset-tracking]

- id: c15
  title: 用例：Wi-Fi Bridge 覆盖露营地 vs Wi-Fi Mesh 连接隔街楼宇
  type: case
  source_chapter: "p110-113"
  source_quote: |
    "Wifi Bridge vs Wifi Mesh. USE CASE • Coverage of a camping ◼WiFi Bridge... USE CASE • Buildings separated by a street... AIM • Replace physical cabling. PROPERTIES • VLANs can be used to separate & secure traffic coming from Wi-FI clients connected on different SSID. • Can provide service (WiFi) to WiFi clients"
  summary: |
    书中成对给出两个无线回运用例：
    Wi-Fi Bridge（露营场地覆盖/替代物理布线）：可用 VLAN 分离并保护回传流量；但不能向 Wi-Fi 客户端提供服务；AP1101、AP1201、AP1201H 不支持桥上 VLAN 标签。属性：SSID/频段/Passphrase 两端一致，指定 1 台 Root。示例：STELLAR-BRIDGE、5GHz、ALCATEL123!。
    Wi-Fi Mesh（隔街楼宇互联）：既能回传又能给客户端提供 Wi-Fi，按 SSID 用 VLAN 隔离；可多台 Root。限制：最多 8 台从 AP、4 跳、单跳点对多点 5 台、全网 16 台、每台最多广播 5 个客户端 SSID。示例：STELLAR-MESH 隐藏 SSID、5GHz、ALCATATEL123!。
    最佳实践：5GHz（Wi-Fi 6E AP 可 6GHz），信道 >100；Auto Mesh 可自动成网（连 LAN 的做 Root，未连的做非 Root）。
  tags: [mesh, bridge, wireless-backhaul, camping, cross-street, config-example, vlan-isolation]

- id: c16
  title: 用例：RAP 远程接入 AP——居家办公与分支机构
  type: case
  source_chapter: "p99-100"
  source_quote: |
    "RAP – REMOTE ACCESS POINT • Aim • Access to the corporate network from everywhere • Use Cases • Homeworking • Corporate Branch Offices • Solution • VPN Server in the corporate network • Clients data encrypted between the Stellar AP and the VPN Server (tagged VLAN supported) • Benefits • OmniVista Management from everywhere"
  summary: |
    用例内容：居家办公（Homeworking）与企业分支机构（Corporate Branch Offices）远程接入公司网络。
    方案：公司网内部署 VPN 服务器；客户端数据在 Stellar AP 与 VPN 服务器之间加密传输（支持 VLAN 标签）；多台 Stellar AP 可接同一 VPN 服务器；OmniVista 可从任意位置管理。
    两种组合（p100）：OV2500 在网时配 OV Cirrus Freemium 账号；无 OV2500 时用 OV Cirrus Premium 账号；RAP 设置（VPN 服务器 IP、OV2500 IP、AP 模式）由云端下发。
    前提条件：除 AP1101 外全部 Stellar AP 型号；AP 软件 4.0.0+；OmniVista Cirrus/Enterprise 4.5.1+。
  tags: [rap, vpn, remote-work, branch-office, homeworking, ov-cirrus]

- id: c17
  title: 报价实例：Network Advisor 订阅（50 AP + 42 交换机客户清单与价格）
  type: case
  source_chapter: "p233"
  source_quote: |
    "OmniVista Network Advisor Quotation: The quantity of devices reflects the quantity of licenses to order. For example: your customer has 50 OmniAccess Stellar access points, 42 OmniSwitches and wants to subscribe the service for 1 Year... Limits: 2000 Network devices"
  summary: |
    书中完整报价演练：客户有 50 台 Stellar AP、42 台 OmniSwitch，订阅 1 年 OmniVista Network Advisor。
    网络清单（列表价）：核心 2 x OS6900X24-F（16,500 欧元/台）+ 2 x QSFP-100G-C1M；接入 40 x OS6360-P24X（2,965 欧元/台）+ 40 x OS6360-CBL-1M + 40 x SFP-10G-SR；Wi-Fi 50 x OAW-AP1311-RW（696 欧元/台）+ 50 x OAW-AP-MNT-B 安装件（23 欧元/个）；硬件小计 244,728 欧元。
    订阅清单：NETAD-AP-1Y x50（48 欧元/个 = 2,400 欧元）；NETAD-SWITCH-1Y x21（96 欧元/个 = 2,016 欧元）；小计 4,416 欧元，约占网络总成本 1.8%（书注：均为 List Price；42 台交换机仅订 21 份许可）。
    单价表（p231）：AP 1 年 48 欧元/3 年 96 欧元/5 年 143 欧元；OmniSwitch 与第三方设备 1 年 96 欧元/3 年 191 欧元/5 年 286 欧元（另有美元价）。
  tags: [quotation, network-advisor, price-list, example, ap1311, os6360, os6900, ebuy]

- id: c18
  title: 部署指南实例：酒店/病房 AP1301H 数量公式与推荐配置
  type: case
  source_chapter: "p243-247"
  source_quote: |
    "AP quantity = M/2+N+(M+N)*5%. Explanation: • M: number of rooms with normal walls • N: number of rooms with load-bearing wall • 5%: represents the redundant backup. Example: 20 rooms M, 10 rooms N • AP quantity = 21,5. Rounded up to 22 AP1301H"
  summary: |
    场景：室内高密度同构房间（医院病房、酒店客房、宿舍、办公室），每房 2-4 人、最多 10 个无线客户端；选 AP1301H（双频 802.11，最高 1024 客户端）。
    数量公式：AP 数 = M/2 + N + (M+N)*5%；M=普通墙房间数、N=承重墙房间数、5%=冗余备份；示例 20 间 M + 10 间 N = 21.5，向上取整 22 台。
    布放规则：无承重墙时隔房装 1 台（普通墙衰耗 15dBm，无 AP 房间最差 -65dBm 可用）；有承重墙每房 1 台（承重墙衰耗 30dBm，否则 5GHz 低至 -80dBm 无法接入、2.4GHz -70dBm 极差）；壁装高度 1.5 米以上，避开电视/显示器/金属架。
    推荐配置（p247 表）：RSSI 门限 2.4G=20、5G=15；漫游 RSSI 同值；ACS 开、APC 关（手动调功率）；2.4G/5G 均 HT20；Band steering 开；单客户端限速上行 2Mbps/下行 4Mbps；负载均衡开；BG-S 关（无 WIPS/APC/快速漫游需求时）；语音视频感知与 ATF 关。
  tags: [deployment-guide, ap1301h, hospitality, hospital-room, capacity-formula, recommended-config, rss-threshold]
