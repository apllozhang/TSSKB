# GLOSSARY · OmniAccess Stellar WLAN Presales Ed28 关键概念词典
# 来源：fulltext.md（273 页）+ BOOK_OVERVIEW.md · 共 45 条 · 按字母排序
# 注：任务提示中的 MSR（疑为多业务无线电）全书未出现，未收录。

- id: g01
  term: 802.11r/k/v
  full: IEEE 802.11r / 802.11k / 802.11v Fast Roaming amendments
  source_chapter: "p89, p114"
  definition: |
    三个加速漫游的 IEEE 修正案：11r 负责快速切换（书中明确 802.11r 支持 WPA2 Personal 和 Enterprise，OKC 只支持 WPA2 Enterprise）、11k 负责无线资源测量、11v 负责终端辅助切换。Stellar 的"粘性终端规避"（Sticky Client Avoidance）就是靠启用这三项加 Roaming RSSI 阈值，把终端从信号差的 AP 上踢到最优 AP。售前答"语音漫游会不会断"时，这是必背的技术底牌。

- id: g02
  term: Access Guardian (AG)
  full: Access Guardian（ALE 统一网络准入控制方案，Unified Access AG 2.0）
  source_chapter: "p64, p76"
  definition: |
    ALE 的 NAC（网络准入控制）组件，在 OmniSwitch 上与 UNP 框架配合，实现有线无线统一的终端识别与策略下发。书 p76 把"Secure NAC with Unified Access AG 2.0 Integration"列为 Wi-Fi Enterprise 特性，p64 把它算进"Stellar AP 部署在 OmniSwitch 上"的关键收益之一。打有线无线一体化标书时，AG + UPAM 是 ALE 区别于纯无线厂商的组合拳。

- id: g03
  term: AeroScout RTLS
  full: AeroScout Real-Time Location Services
  source_chapter: "p119"
  definition: |
    第三方实时定位引擎，利用标准 802.11 作为通信基础：AeroScout 标签周期性发 802.11 报文，Stellar AP 把测到的 RSSI 上报给 AeroScout Engine Server 计算位置，Engine Manager 负责地图、热图与地理围栏告警。医院里追踪人员、轮椅、医疗设备就靠它。客户已有 AeroScout 而想换 AP 时，这是"Stellar AP 直接兼容、标签不用换"的迁移话术。

- id: g04
  term: AWOS
  full: ALE WLAN OS（Stellar AP 固件操作系统；书中仅出现版本号 AWOS 4.0.3 MR-3，全称按 ALE 通行叫法）
  source_chapter: "p230"
  definition: |
    Stellar AP 的运行软件版本体系，书中在 Network Advisor 的设备要求里出现："Stellar APs, AWOS 4.0.3 MR-3 or Higher"。售前做兼容性核对时要拿它对照 AP 固件，判断客户现网 AP 能否直接纳管或必须先升级。报价含升级服务时，这也是工作量估算的依据。

- id: g05
  term: BLE Beaconing
  full: Bluetooth Low Energy Beaconing
  source_chapter: "p95"
  definition: |
    Stellar AP 内置 BLE 蓝牙信标能力（默认 iBeacon 模式，默认关闭），可配置发射功率、周期、UUID 及 Major/Minor 值，按 AP Group 统一下发。配合定位方案可做资产追踪（轮椅、医疗设备、笔记本），缩短找资产的时间。医院、物流客户投标时，"AP 即信标、不用另购蓝牙网关"是一个零成本加分的卖点。

- id: g06
  term: BYOD
  full: Bring Your Own Device
  source_chapter: "p122"
  definition: |
    员工自带设备安全接入方案，属于 OV2500/Cirrus 的 UPAM 能力：Web 重定向注册、supplicant/非 supplicant 设备安全上线、可定制门户页。License 按设备数计费（OV2500-NG-ONBOARDING / OV-BYOD-X-N），OV2500-Starter Pack 内免费含 10 个。售前注意：客户说"要管员工手机"时，BYOD 与 Guest 是两个独立计费项，报价别漏。

- id: g07
  term: Captive Portal
  full: Captive Portal（强制门户认证页）
  source_chapter: "p43, p109"
  definition: |
    访客接入 Web 认证页。Express 模式出厂自带集成 Captive Portal，Enterprise 模式支持内部与外部两种门户。书 p109 专门讲 External Captive Portal Integration：连锁酒店、大卖场用已有品牌门户页对接 Stellar（外部门户 + MAC 认证）。问客户"门户页要不要用你们自己的品牌"，是把技术话题引向客户体验的常用开场。

- id: g08
  term: Controller-less Architecture
  full: Controller-less Architecture（无控制器架构）
  source_chapter: "p75, p128"
  definition: |
    Stellar 的核心架构叙事：控制面分布在 AP 之间（DRM 分布式射频管理、分布式控制/数据面），不需要无线控制器，管理与用户数据分离、L2 直通。全书用例反复用它换算 TCO 优势——轮渡机舱没地方放控制器、理工大学换 Cisco 后维护费大降。遇到"你们控制器坏了怎么办"的质疑，答案是"本来就没有控制器"。

- id: g09
  term: DHCP Option 138
  full: DHCP Option 138（CAPWAP/AP AC 地址通告选项）
  source_chapter: "p55, p66-67"
  definition: |
    在 AP 管理 VLAN 的 DHCP 作用域里下发 OmniVista 2500 的 IP 地址，AP 开机据此注册到网管并"硬编码"进 Enterprise 模式；没有 option 138 则默认进 Express 集群模式。Express 升级 Enterprise 的官方路径就是：加载新软件 + 加 option 138 + 恢复出厂重启（原集群配置不保留）。这是开局方案里必须写进交换机/DHCP 配置清单的一项，漏了 AP 就"失联"。

- id: g10
  term: DPI
  full: Deep Packet Inspection
  source_chapter: "p76, p123, p177"
  definition: |
    深度包检测，Stellar AP 上内嵌（Network Analytics 应用可见性与管控），可对 LAN+WLAN 统一做 L7 应用识别、限速与阻断，并支持 IPv6 客户端。酒店案例（p177）用它监控客人流量、限制员工带宽；渡轮案例用它做带宽管控。对标"上网行为管理盒子"时，"AP 和交换机上原生自带 DPI"可以省掉一台旁挂设备。

- id: g11
  term: DRM
  full: Distributed RF Management（分布式射频管理）
  source_chapter: "p75, p86"
  definition: |
    Enterprise 模式下 AP 之间通过空口发现 + 局域网同步完成射频协调，同一 AP Group 内可按 RF Profile 分组管理信道与功率，相邻 AP 为作用域。它是 controller-less 架构的技术底座，管理面在 OmniVista、执行面在 AP 本地。客户担心"没有控制器谁来做 RF 优化"时，DRM 就是答案。

- id: g12
  term: eBuy
  full: ALE eBuy（合作伙伴在线订货平台）
  source_chapter: "p142, p159"
  definition: |
    ALE 渠道下单平台（可从 MyPortal 快捷入口进入），Cirrus 4 与 Cirrus 10 的 License 都在这里订购，之后在 OVC Subscription Manager 里创建订阅、拿到 Subscription ID 和 Activation Code 再导入云管。售前报价闭环的关键一环：客户问"云管理怎么开通"，流程就是 eBuy 下单 → 建订阅 → 云端导入激活。

- id: g13
  term: EDUROAM
  full: Education Roaming（教育网国际漫游服务）
  source_chapter: "p182"
  definition: |
    全球教育机构的无线漫游联盟，师生用本校账号在任何成员学校自动接入。理工大学案例（换 Cisco）把它列为硬性要求："EDUROAM SSID Authentication Compatibility"，配合 802.1x/PEAP-MSCHAPv2/WPA2。打教育行业标书时，能否兼容既有 EDUROAM SSID 是一票否决项，要在方案里第一时间应答。

- id: g14
  term: Ekahau
  full: Ekahau Site Survey / Ekahau RTLS（第三方无线勘察与定位工具）
  source_chapter: "p178, p190, p211"
  definition: |
    行业标准的 Wi-Fi 勘察工具。书中多次出现：五星酒店装后审计发现信道重叠、降信道宽度解决；渡轮装前勘察因金属船体结构优化 AP 布点；Operate 阶段用 Ekahau Survey PRO 或 AirMagnet 做周期性复测；话机 8168s/8128 还可用 Ekahau RTLS 做实时定位。方案里把"Ekahau 勘察"写进工作量，显得专业且可交付。

- id: g15
  term: ESL
  full: Electronic Shelf Label（电子货架标签）
  source_chapter: "p196-198"
  definition: |
    零售电子价签，替代纸质价签，价格库存可远程更新、标签可闪灯定位。书中的亮点玩法：把 ESL 厂商（Hanshow）的 USB dongle 插在已部署的 Stellar AP USB 口上，dongle 用 2.4GHz 专有射频连价签并回连 Hanshow 云，复用现有 WLAN 免布线。对已有 Stellar 网的零售连锁，这是"加装功能不动网络"的增量销售话术。

- id: g16
  term: Freemium / Premium
  full: OmniVista Cirrus Freemium / Premium（免费版与订阅版云管账户）
  source_chapter: "p139-143"
  definition: |
    Cirrus 云管的两种账户形态。Freemium 免费自助注册，不限设备数、不限时长，但能力受限（无网络配置、仅一次性设备升级），可升级到 Premium；Premium 按订阅付费，能力全开，含最多 5000 个 AP/交换机 License，可扩容、缩容、续订。售前节奏：先用 Freemium 让客户零门槛上云体验，再按需转 Premium 订阅。

- id: g17
  term: GRE Guest Tunneling
  full: Guest Tunneling over L2 GRE（访客流量 GRE 隧道）
  source_chapter: "p115"
  definition: |
    按 Access Role Profile 把访客流量用 L2 GRE 隧道从 AP 送到 OS6860E/OS6900 交换机终结，实现访客与内网隔离；OmniSwitch 可自动建隧道简化部署。规格：每 AP 最多 16 条隧道、6860E 终结 750 条、6900 终结 1000 条。客户要"访客流量物理隔离出 Internet"时，这是不用加盒子的答案，报价时记得核对交换机型号与隧道数。

- id: g18
  term: HA
  full: High Availability（OmniVista 2500 高可用）
  source_chapter: "p93-94"
  definition: |
    OV2500 双机主备：Stand-by 实例与 Main 持续同步，主挂了全部服务（含 UPAM 的 Guest/BYOD）切换到备机，设备统一对 Virtual IP 通信，部署在二层网络（有 VxLAN/SPB 可扩到三层）。License 用 OV-NMS-HA，每个节点一份。客户是医院、生产网这类"网管不能停"的场景，HA 是必报项。

- id: g19
  term: Hotspot 2.0 (Passpoint)
  full: Hotspot 2.0 / Passpoint（无缝公共 Wi-Fi 接入标准）
  source_chapter: "p108"
  definition: |
    让手机像连蜂窝一样自动发现并安全接入公共 Wi-Fi 的标准：Stellar AP 支持 802.11u（GAS/ANQP）与 EAP-SIM/EAP-AKA（用运营商 SIM 卡凭据认证），可把流量从 3G/4G 卸载到 Wi-Fi。书里同时提到欧盟 WiFi4EU 项目（公共场所免费 Wi-Fi，HTTPS 门户、会话最长 12 小时配置）。做智慧城市、公共交通、运营商合作项目时是关键应答项。

- id: g20
  term: "Maintenance Contract (PW/SP)"
  full: Maintenance Contract（维护合约，PW/SP 编码体系）
  source_chapter: "p137"
  definition: |
    ALE 维护合约订货编码规则：首字母 P=Partner / S=End Customer，第二个字母 W=软件支持 / P=Support Plus（含 AVR 硬件服务），数字为 1/2/3/5 年，再接 R=续约 / N=新购 + 产品编码。例：PW2R-OVBYOD100N 是"伙伴、软件支持、2 年、续约、100 用户 On-Boarding"；SP5N-OAWAP1201 是"最终客户、Support Plus、5 年、新购、AP1201"。License 与 AP 都要配维护合约，漏报维护是报价单最常见的错。

- id: g21
  term: Network Advisor
  full: OmniVista Network Advisor（AI 网络运维伴侣）
  source_chapter: "p213-233"
  definition: |
    ALE 的 AI 运维产品：边缘计算 + 云的混合架构，独立服务（不要求先买 OV2500/Cirrus），内置 30+ 种预置异常（环路、端口闪断、DDoS、CPU 高、AP 客户数超限等，持续更新）并支持自定义，通过 Rainbow 或 Teams 消息一键修复或自动处置。License 按设备按年：AP 50 美元/年、交换机/第三方设备 100 美元/年（目录价，1 年约占总网成本 1.8%），上限 2000 台设备。给运维人手不足的客户算"省一个网管工程师"的账最有效。

- id: g22
  term: OAW-APxxxx-Region
  full: OmniAccess Stellar AP 订货型号规则
  source_chapter: "p136, p167"
  definition: |
    AP 下单编码：OAW-APxxxx-Region，xxxx 为 AP 型号（如 1231），Region 为区域码 RW（全球除下列外）/JP（日本）/ME（中东）/US（美国）。无线射频法规随区域不同，下错区域码的 AP 无法合规发射。报价复核清单第一条就是核对区域后缀与项目所在国一致。

- id: g23
  term: OmniVista 2500 (OV2500)
  full: OmniVista 2500 Network Management System（本地网管）
  source_chapter: "p52, p72"
  definition: |
    ALE 本地部署的 LAN+WLAN 统一网管（虚拟机/虚拟板卡形态），管理 OmniSwitch、Stellar AP 与第三方设备：集中升级、配置同步、AP Group 管理、UPAM 认证、WIPS、热图报表，单套最多 4000 AP / 10 万客户端。对应 Stellar Enterprise On-Premise 模式，是数据不出客户机房的选项，打政府、医疗、军工等安全敏感客户必用。

- id: g24
  term: OmniVista Cirrus 4
  full: OmniVista Cirrus 4（云管平台，SaaS）
  source_chapter: "p138-149"
  definition: |
    ALE 云管平台（当前一代），对应 Stellar Enterprise Cloud 模式。License 分 LAN Core（OS6900、Stellar AP）/LAN Essential（OS6350-6560）/LAN Advanced（OS6860 系），时长 1/3/5 年，服务包 Base/Business/Premium；每 AP 一颗 License 附送 50 Guest + 50 BYOD。开通三步：注册 Freemium 账户 → eBuy/eSR 下单 → Subscription Manager 建订阅激活。给多分支连锁客户做云管报价的主战场。

- id: g25
  term: OmniVista Cirrus 10
  full: OmniVista Cirrus 10（新一代云管订阅平台）
  source_chapter: "p151-167"
  definition: |
    新一代云管 SaaS，License 语法 OVCX-[类别]-[级别]-[时长]，共 63 个 part number。支持设备为除 AP1101/AP1201H/L/LH 外的 Stellar AP 和 AOS 8.9Rx 的 OmniSwitch。售前拼单时按"设备档位 + 服务级别 + 年限"三步就能出编码，是新一代云管报价的主战场。

- id: g26
  term: OV2500-NG-AP
  full: OmniVista 2500 AP License（Stellar AP 管理授权）
  source_chapter: "p131, p136"
  definition: |
    OV2500 管理 Stellar AP 的强制 License（功能覆盖发现、注册、开通、生命周期、Access Guardian、应用可见性、RF 管理、WIDS/WIPS、热图等），容量档 20/50/100/500/1000 台；下单编码写作 OV-AP-NM-X-N（X=10/20/50/100/500）。与 Guest、On-Boarding、HA、WCF 并称 OV2500 五类 License，做本地管理模式报价时的核心计费行。

- id: g27
  term: "OVCX-[Category]-[Level]-[Duration]"
  full: OmniVista Cirrus 10 License 命名语法
  source_chapter: "p153-156"
  definition: |
    Cirrus 10 订阅编码三段式：类别（7 种：低档 AP=APL、高档 AP=APH、交换机按系列 63/64/65/68/69）× 级别（BAS/BIZ/PRM）× 时长（1Y/3Y/5Y）= 63 个 part number。例：OVCX-68-BIZ-3Y 表示 68xx 交换机、Business 级、3 年。级别的差别在 TAC 与硬件先行更换服务的对象（BAS 无、BIZ 给伙伴、PRM 给最终客户）。这是"报价不出错"的核心防错设计，售前必须背熟。

- id: g28
  term: PVM / SVM
  full: Primary Virtual Manager / Secondary Virtual Manager（主/备虚拟管理 AP）
  source_chapter: "p44-45"
  definition: |
    Express 模式集群里的两个管理角色：同 VLAN 多台 AP 同时启动时按"最高型号、最高 MAC"选出 PVM 承担集中管理，次高的做 SVM 备份，其余为 Member，单集群上限 255 台。PVM 选定后会广播类似 mywifi-0102 的管理 SSID。向 SMB 客户解释"没有控制器谁管事"时，答案就是"组里自动选出一台 AP 当管家，坏了自动换"。

- id: g29
  term: Rainbow
  full: ALE Rainbow（UCaaS/CPaaS 云通信平台）
  source_chapter: "p203, p227"
  definition: |
    ALE 的云统一通信平台。在 VoWLAN 章它是 iOS/Android/PC 软终端（Rainbow UCaaS client，可与 OXO/OXE 话务系统集成）；在 UPAM 里它是访客社交登录方式之一（Google/Facebook/WeChat/Rainbow）；在 Network Advisor 里它是 Companion Service 的消息通道（配合 Teams 一键修复），p227 还提到 Rainbow CPaaS 可连应用和其他 AI。ALE 方案里"通信 + 网络"两条线在 Rainbow 上汇合，做联合销售的话术抓手。

- id: g30
  term: RAP
  full: Remote Access Point（远程接入点模式）
  source_chapter: "p99-100"
  definition: |
    把 Stellar AP 部署在分公司或员工家里，通过 VPN 隧道（客户网络里的 VPN Server）加密回传数据（支持 VLAN 打标）并接受 OmniVista 远程管理的模式。用于居家办公和小型分支。条件：除 AP1101 外全型号、AP 软件 4.0.0+、OV Cirrus/Enterprise 4.5.1+；若主用 OV2500 还需搭配一个 Cirrus Freemium 或 Premium 账户来传 RAP 设置。卖"总部一套网管、分支即插即用"就用它。

- id: g31
  term: RTLS
  full: Real-Time Location Services（实时定位服务）
  source_chapter: "p119"
  definition: |
    基于 Wi-Fi 的实时定位能力。书里两条实现路径：AeroScout 标签 + Stellar AP 的 RSSI 测量交给定位引擎；以及话机侧用 Ekahau RTLS（8168s/8128）。定位资产和人员能直接换成业务价值——医院找轮椅、工厂找人。行业方案（尤其医疗）报价时建议主动加一行定位选件，多数竞品方案会漏。

- id: g32
  term: Smart Load Balancing
  full: Smart Load Balancing / Band Steering（智能负载均衡与频段引导）
  source_chapter: "p87"
  definition: |
    Stellar 的无线优化组合拳：Band Steering 把终端往 5GHz/6GHz 引导（可强制 5G）；Dynamic Load Balance 按 AP 客户数分担负载（新终端广播入网请求、由负载最轻的 AP 应答）；Smart Air Share 管控 11b/g 老终端和最低速率；另有客户端 SNR 阈值（默认 2.4G=18dB、5G=12dB，范围 0-40dB）拒绝弱信号终端。高密度场馆答"几百人同时上网怎么办"就靠这套参数，书 p247-261 的部署指引里都有推荐值。

- id: g33
  term: Starter Pack
  full: OmniVista 2500 Starter Pack（OV2500 起步授权包）
  source_chapter: "p130"
  definition: |
    OV2500 的起步 License：含 10 个 AOS 交换机 + 10 个 Stellar AP + 10 个 Guest + 10 个 BYOD，分 60 天评估版和不过期的生产版（在 License 生成网站 lds.al-enterprise.com 上选择）。给中小客户或 POC 场景的入门钥匙——先送 Starter Pack 跑起来，超量再加购增量 License，成交门槛立刻降低。

- id: g34
  term: Stellar Enterprise (On-Premise)
  full: OmniAccess Stellar Wi-Fi Enterprise Mode — In Premise
  source_chapter: "p51-58, p128"
  definition: |
    三种管理模式之一：用本地 OmniVista 2500 NMS 集中统一管理，单套最多 4000 AP，LAN/WLAN 一台平台管，支持 BYOD/Guest、UNP 角色策略、智能分析、WIPS、热图等全套 Enterprise 特性。数据与网管全在客户机房。面向安全敏感、要本地管控的中大型客户，与云模式互为替代选项。

- id: g35
  term: Stellar Enterprise Cloud
  full: OmniAccess Stellar Wi-Fi Cloud Mode（Enterprise 云管理模式）
  source_chapter: "p59-61, p128"
  definition: |
    三种管理模式之一：用 OmniVista Cirrus 4 或 Cirrus 10 云管平台集中管理（最多 4000 AP），功能面与本地模式基本对齐（集中升级、配置同步、内外部门户、BYOD、内嵌认证服务器等），License 走订阅制。适合多分支连锁、缺 IT 人手的客户——零部署、零机房 footprint，卖订阅收入的抓手。

- id: g36
  term: Stellar Express
  full: OmniAccess Stellar Wi-Fi Express Mode（免网管独立模式）
  source_chapter: "p42-50, p128"
  definition: |
    三种管理模式中的入门形态：AP 自组集群（PVM/SVM）、自带安全 Web 管理界面和配置向导、内置访客门户，单集群最多 255 AP；全书口径为无需购买 License、出厂含 5 个永久授权。DHCP 无 option 138 时 AP 默认就是这个模式，后续可升级到 Enterprise/Cloud（需恢复出厂）。客户说"我只要个简单 WiFi"时，5 分钟讲完 Express + 免授权就是最快成交路径。

- id: g37
  term: UNP
  full: Unified Network Profile（用户/终端网络档案；书中未展开全称，按 ALE 文档通行写法）
  source_chapter: "p64, p76, p96"
  definition: |
    OmniSwitch 侧的策略框架：按用户角色或 IoT 设备类型（Device Profiling 结果）自动套用网络策略，p64 将其与 Access Guardian 并列为有线无线统一接入的基石，p96 的 IoT 方案里按设备类别自动指派 UNP。对客户的话术价值：有线无线一套策略语言，终端插哪个口、连哪个 AP 策略都一致。

- id: g38
  term: UPAM
  full: Unified Policy Authentication Manager（统一策略认证管理器）
  source_chapter: "p121-122"
  definition: |
    OmniVista 内嵌的认证中枢：自带 RADIUS 服务器与 MAC 认证服务器，向上可对接 LDAP/AD 做角色映射，向下统一管员工 802.1X、访客（自助注册/员工赞助/社交登录 Google/Facebook/WeChat/Rainbow，还分 VIP/Gold/Silver 服务等级）和 BYOD。替代外置 AAA 的位置，硬件+认证打包进 OV2500/Cirrus 后，报价单可以砍掉第三方 AAA 一行。

- id: g39
  term: VoWLAN
  full: Voice over WLAN（无线语音）
  source_chapter: "p200-212"
  definition: |
    在 Wi-Fi 上跑语音业务。终端矩阵：Ascom 话机 8118/8128/8158s/8168s（支持 ALE NOE 与 SIP、无缝漫游、IMS3 批量部署服务器）加 Rainbow 等软终端；所有 Stellar AP 均支持语音。五步交付法 Prepare→Plan→Design→Implement→Operate，可背工程常数：语音覆盖 1 AP/255m²、每 AP 20-25 用户且保证 36Mbps 吞吐、漫游 RSSI 需 -62dBm 以上、优先 5GHz。答客户"无线打电话稳不稳"就靠这组数。

- id: g40
  term: WCF
  full: Web Content Filtering（网页内容过滤）
  source_chapter: "p90, p131"
  definition: |
    Stellar AP 通过 DNS 窥探拿到 FQDN，经 OmniVista 内置 BrightCloud SDK 做分类，再按角色（如 Guest 拒绝社交/P2P、Employee 放行社交拒绝 P2P）下发 ACL 放行或阻断。License 为 OV-AP-WCF，每 10 台 AP 一颗。对标上网行为审计需求时，"AP 上原生 WCF"省一台旁挂设备，酒店/学校场景好卖。

- id: g41
  term: Wi-Fi Bridge
  full: Wi-Fi Bridge（无线网桥）
  source_chapter: "p110-111"
  definition: |
    用无线链路替代物理布线连接两个局域网（典型：隔街楼宇、营地覆盖），不给 Wi-Fi 客户端提供服务。两端配置 SSID/频段/Passphrase 必须一致，指定一端为 Root；可用 VLAN 隔离桥上流量（AP1101/1201/1201H 不支持桥上 VLAN 打标）。客户不想挖路铺光纤时，网桥是低成本替代方案的话术。

- id: g42
  term: Wi-Fi Mesh
  full: Wi-Fi Mesh（无线网状网）
  source_chapter: "p112-113"
  definition: |
    AP 间无线回程组网且同时给客户端提供服务，可多 Root。规格限制要背：全网最多 16 台 AP、单 Root 最多 8 台从属、最多 4 跳、单跳点到多点最多 5 台、Mesh 网内每 AP 最多播 5 个 SSID；最佳实践 5GHz（6E 机型用 6GHz）、信道大于 100。Auto Mesh 功能让接有线的一台自动当 Root、未接线的自动入网（隐藏 SSID Stellar-MESH），临时场地快速开局的卖点。

- id: g43
  term: WIPS / wIDS
  full: Wireless Intrusion Prevention System / Wireless Intrusion Detection System（无线入侵防护/检测）
  source_chapter: "p54, p92"
  definition: |
    基于专用扫描射频做恶意 AP 防御：Rogue AP 定位与遏制（containment）、客户端拉黑、攻击检测，配 OmniVista 的仪表盘与报表（Rogue AP 策略、AP/客户端攻击检测策略、黑名单策略）。Express 与 Enterprise 模式都内置。客户问"隔壁公司 AP 冒充我们网络怎么办"，这就是答案，且不额外加盒子。

- id: g44
  term: WPA3
  full: Wi-Fi Protected Access 3
  source_chapter: "p105"
  definition: |
    Wi-Fi 联盟 2018 年发布的新安全标准，所有 Stellar AP 可软件升级支持。个人版用 SAE（对等同时认证）替换 PSK：128 位更强密钥、抗离线字典攻击、用户连接习惯不变；企业版可选 192 位 CNSA 模式（开启后仅允许 WPA3 终端入网，关闭则 WPA2/WPA3 混容）。老旧终端占比高的客户要提醒混合模式兼容，避免"升级即断网"的投诉。

- id: g45
  term: Zigbee
  full: Zigbee（低功耗物联网无线协议）
  source_chapter: "p98"
  definition: |
    家庭与楼宇自动化的常见 IoT 协议。多数 Stellar AP 内置 BLE 5.1/Zigbee 双协议无线电（除 AP1301 与 AP1230 系列外），可在 OmniVista 上统一管理 Zigbee 终端。书中用例是酒店客房数字门锁集中管理——客人手机发数字钥匙、门锁走 Zigbee，提升入住体验并减少制卡成本。智慧酒店、智慧楼宇方案里的关键连接件。
