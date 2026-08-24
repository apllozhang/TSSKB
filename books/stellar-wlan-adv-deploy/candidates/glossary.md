# glossary · 术语（stellar-wlan-adv-deploy / DT00XTE361）

```yaml
- id: g01
  term: QoE (Quality of Experience)
  definition: 体验质量分析。OmniVista Cirrus 用 Successful Connects / Time To Connect / Roaming / Coverage / Available Capacity / Device Uptime 六指标评估终端真实体验。
  source_chapter: "p122-p134, p158"
  tags: [监控, 分析]

- id: g02
  term: Time To Connect
  definition: QoE 指标，客户端完成关联、授权、DHCP、Portal 四阶段的总耗时；阈值 2-20s，默认 2s。
  source_chapter: "p128, p158"
  tags: [QoE]

- id: g03
  term: Available Capacity
  definition: QoE 指标，RF 信道可用容量高于阈值的时间占比；阈值 10%-50%，默认 10%。
  source_chapter: "p129, p158"
  tags: [QoE]

- id: g04
  term: Failure Classifier（失败分类器）
  definition: QoE 各指标失败原因归类，如 Asymmetry Downlink/Uplink、Weak Signal、DHCP、Association、Wi-Fi Interference 等，用于下钻定位。
  source_chapter: "p128-p133"
  tags: [QoE, 排障]

- id: g05
  term: Network Analytics（网络分析）
  definition: 按信道分布/信道利用率/设备健康（CPU、内存、闪存）/设备在线率四个维度评估 AP 与交换机的分析应用，可下钻到单设备与端口级。
  source_chapter: "p137-p145"
  tags: [监控, 分析]

- id: g06
  term: Client Analytics（客户端分析）
  definition: 客户端维度的分析应用：连接数曲线、频段/SSID/AP 分布、吞吐消费、连接时长、每用户设备数。
  source_chapter: "p146-p153"
  tags: [监控, 分析]

- id: g07
  term: Health Thresholds（健康阈值）
  definition: 设备 CPU/内存/闪存使用的告警百分比阈值，可在 Network Analytics 或 Edit Device 中按设备调整；演练基准 70%。
  source_chapter: "p139, p298"
  tags: [监控, 阈值]

- id: g08
  term: Heat Map（热力图）
  definition: 基于 AP 信号强度生成的可视化覆盖图，按站点或 AP 展示；生成最少需 3 台 Stellar AP。客户端密度热力图红/黄/绿对应高/中/低密度。
  source_chapter: "p176-p178"
  tags: [监控, 覆盖]

- id: g09
  term: Access Role Profile (ARP)
  definition: 访问角色配置，定义终端的 ACL/QoS 与带宽限制（如 ARP_DEFAULT 受限、ARP_PASS 全通）；可由认证结果、IoT 分类或手工指派。注意与地址解析协议 ARP 无关。
  source_chapter: "p91, p108"
  tags: [安全, 策略]

- id: g10
  term: Access Auth Profile
  definition: 定义有线端口认证方法（802.1X/MAC/Portal）、所用 AAA Server Profile 与默认访问角色，并绑定 AP 组/交换机端口。
  source_chapter: "p93"
  tags: [安全, 有线]

- id: g11
  term: Unified Policy / Policy List
  definition: 统一接入策略：以映射条件（如 Authentication Type = MAC）决定认证源、访问角色与 Web 重定向；多个策略组成 Policy List 挂到 SSID。
  source_chapter: "p94"
  tags: [安全, 策略]

- id: g12
  term: UPAM / UPAMRadiusServer
  definition: OmniVista 内置的统一策略与准入模块（含内置 RADIUS 服务器 UPAMRadiusServer），承载员工/访客账号、门户与本地认证数据库。
  source_chapter: "p66, p107"
  tags: [安全, 认证]

- id: g13
  term: Captive Portal（强制门户）
  definition: Web 认证页。OV-UPAM Captive Portal 类型配合 Guest Access Strategy、门户模板（Captive Portal Template）使用；记录在 Access Records > Captive Portal Records，含 Auth result 与 Reject Reason。eag 进程负责门户逻辑。
  source_chapter: "p70-p71, p170, p219-p220"
  tags: [认证, 访客]

- id: g14
  term: Walled Garden（围墙花园）
  definition: SSID 访问角色中允许终端在认证前访问的白名单域名集合。
  source_chapter: "p76"
  tags: [访客, 策略]

- id: g15
  term: Wireless Client Social Login
  definition: 允许无线客户端通过社交平台账号（Facebook WiFi 或 Google）认证的 SSID 选项。
  source_chapter: "p76"
  tags: [访客, 认证]

- id: g16
  term: UAPSD
  definition: 非调度自动省电 delivery，IEEE 802.11e 定义的 QoS 省电机制，延长移动终端电池寿命；SSID 基本选项之一。
  source_chapter: "p77"
  tags: [QoS, SSID]

- id: g17
  term: Client Isolation（客户端隔离）
  definition: 阻断同一 AP 同一 SSID 内客户端之间互访的 SSID 安全选项，访客网络常用。
  source_chapter: "p77"
  tags: [安全, SSID]

- id: g18
  term: Bandwidth Contract（带宽契约）
  definition: SSID 级、按每射频共享的总带宽上限（区别于按用户的 Bandwidth Control）。
  source_chapter: "p78"
  tags: [QoS, SSID]

- id: g19
  term: Broadcast/Multicast Optimization
  definition: 广播优化含 Broadcast Filter All（除 DHCP/ARP 外全丢广播）与 Broadcast Filter ARP（广播 ARP 转单播）；组播优化把组播转单播，高负载（信道利用率 90% 或 6 个高吞吐客户端）自动停。
  source_chapter: "p78-p79"
  tags: [SSID, 优化]

- id: g20
  term: GTK / Broadcast Key Rotation
  definition: 组临时密钥及其周期轮换（默认 15 分钟，1 分钟-24 小时），用于防组密钥破解；仅 Enterprise SSID 适用。
  source_chapter: "p78"
  tags: [安全]

- id: g21
  term: WMM
  definition: Wi-Fi 多媒体，四访问类别（Voice/Video/Best Effort/Background）的无线 QoS 框架，配合 802.1p/DSCP 标记。
  source_chapter: "p80-p81"
  tags: [QoS]

- id: g22
  term: DSCP / 802.1p
  definition: IP 层与二层 CoS 优先级标记。推荐语音 46(EF)/5、视频 34(AF41)/4、背景 18(AF21)/2、尽力而为 0/0。
  source_chapter: "p80-p81"
  tags: [QoS]

- id: g23
  term: Hotspot 2.0 (Passpoint)
  definition: 基于 802.11u(GAS/ANQP) 与 EAP-SIM/EAP-AKA 的无缝安全公众 Wi-Fi 机制；在 WPA2-Enterprise SSID 的高级 WLAN 配置中启用。
  source_chapter: "p82-p83"
  tags: [公众Wi-Fi, 认证]

- id: g24
  term: WiFi4EU
  definition: 欧盟公共场馆免费 Wi-Fi 计划；SSID 用 HTTPS Captive Portal，会话超时需可配至 12 小时；配置入口在 Guest SSID > Guest Access Strategy。
  source_chapter: "p82-p83"
  tags: [公众Wi-Fi]

- id: g25
  term: IoT Device Profiling（IoT 设备画像）
  definition: OmniVista 通过 MAC OUI 与 DHCP 指纹（option 55/60）识别终端类型并归入分类；分类可绑定 Access Role Profile 做强制控制（ARP Enforcement）。
  source_chapter: "p102-p108"
  tags: [IoT, 画像]

- id: g26
  term: MAC OUI
  definition: MAC 地址的厂商组织唯一标识前缀，IoT 识别手段之一；也用于 WIPS 里限定"其他厂商设备"的匹配条件。
  source_chapter: "p103, p297"
  tags: [IoT, 安全]

- id: g27
  term: DHCP Fingerprinting（DHCP 指纹）
  definition: 利用 DHCP option 55（参数请求列表）与 option 60（厂商标识）的组合特征识别设备类型。
  source_chapter: "p103"
  tags: [IoT, 画像]

- id: g28
  term: WiFi Bridge
  definition: 点对点无线桥接，替代物理布线连接两栋楼；可用 VLAN 分隔桥上流量，但不能向 Wi-Fi 客户端提供服务；AP1101/1201/1201H 不支持桥上 VLAN 打标。
  source_chapter: "p113-p114"
  tags: [Bridge, 组网]

- id: g29
  term: WiFi Mesh
  definition: 无线网状组网：Root AP 接 LAN，Repeater 经无线回传；限制为全网 16 AP、8 从 AP、4 跳、单跳 5 AP、每 AP 5 SSID；最佳实践 5GHz 信道>100。
  source_chapter: "p113-p115"
  tags: [Mesh, 组网]

- id: g30
  term: Auto Mesh
  definition: 快速 Mesh 部署特性：接 LAN 的 Root 与未接 LAN 的 AP 自动以隐藏 SSID "Stellar-MESH"（5GHz）完成组网。
  source_chapter: "p116"
  tags: [Mesh]

- id: g31
  term: Root AP / Parent Address
  definition: Mesh 中的根节点（可多台）；Mesh Topology 监控中 Repeater 的 Parent Address 即其上游 Root AP 的 MAC。
  source_chapter: "p115, p120"
  tags: [Mesh, 监控]

- id: g32
  term: WIPS / Rogue AP
  definition: 无线入侵防护。可按"广播相同 SSID 名"与"非本厂商 MAC OUI"等条件把 AP 分类为 Rogue（流氓 AP）；支持攻击检测、黑名单（如 1 分钟认证失败 5 次）与 Containment（遏制，演练中禁用）。
  source_chapter: "p297"
  tags: [安全, WIPS]

- id: g33
  term: MSP Portal / Organization
  definition: OmniVista Cirrus 多租户入口页；每个 Organization 是独立租户（含站点、设备、许可证），角色分 Viewer/Admin。删除组织是不可逆操作。
  source_chapter: "p47"
  tags: [云管]

- id: g34
  term: Site / Building / Floor
  definition: 云管组织下的位置层级：站点 > 楼栋 > 楼层；设备必须归属站点，楼层可挂平面图用于热力图与定位。
  source_chapter: "p48-p50"
  tags: [云管, 组织]

- id: g35
  term: Device Catalog（设备目录）
  definition: 云管设备清单，创建设备（录序列号）、查看激活状态并对设备执行 Edit/SSH/Web UI/配置管理等 Actions；含 Wired Ports、CLI 模板、值映射等页签。
  source_chapter: "p52, p97, p224"
  tags: [云管, 设备管理]

- id: g36
  term: AP Group（接入点组）
  definition: AP 的配置分组，绑定 Provisioning Configuration 与 RF Profile；SSID 通过 VLAN/Tunnel Mapping 挂到组；改组会清空 AP 现有配置。
  source_chapter: "p61, p245"
  tags: [云管, 配置]

- id: g37
  term: Provisioning Configuration（配给配置）
  definition: AP 组级参数集：RF Profile、时区、SSH/AP Web 开关及凭据等；删除前须先解除与 AP 组的绑定。
  source_chapter: "p61, p193, p316"
  tags: [云管, 配置]

- id: g38
  term: RF Profile
  definition: 射频管理模板：Band Steering、Load Balance、背景扫描、国家码、Air Time Fairness 及每射频信道/带宽/功率/RSSI 门限。AP 侧落盘于 /tmp/config/rfprofile.conf。
  source_chapter: "p261, p280-p281"
  tags: [RF, 配置]

- id: g39
  term: Call Home / Activation Status
  definition: 设备周期性向云管注册的机制。激活状态流转：Waiting for first Contact → Connected to OV → Provisioning → OV Managed。交换机可 cloud-agent admin-state restart 加速，AP 可重启触发；show cloud-agent status / ocloud_show 查询。
  source_chapter: "p55, p64-p65"
  tags: [云管, 上线]

- id: g40
  term: OV Managed / Full Management vs Analytics Only
  definition: OV Managed 表示设备已完全受管；管理模式可选 Analytics Only（仅分析）或 Full Management（全管理）。
  source_chapter: "p55, p224"
  tags: [云管]

- id: g41
  term: Golden Configuration（黄金配置）
  definition: 被标记为基准的交换机 running 配置，可周期或即时审计比对；支持 Mark/Unmark as Golden Config 与备份恢复。
  source_chapter: "p145, p229-p230"
  tags: [配置管理]

- id: g42
  term: Network Events / Traps
  definition: 设备通知事件，分 AP Traps、Switch Traps 与 QoE Analytics 三类；条目含 Severity（Normal/Warning/Minor/Major/Critical）、Ack 状态、重复次数；可 Acknowledge 或 Delete。
  source_chapter: "p179-p181, p254"
  tags: [监控, 事件]

- id: g43
  term: Collect Support Info（支持信息收集）
  definition: 收集设备日志包供 ALE 排障：AP 为 tar.gz 快照（配置+日志）；交换机可选 swlog、cfg、Tech Support（L2/L3/Engineering Complete 分级）。
  source_chapter: "p236, p254-p255"
  tags: [运维, 排障]

- id: g44
  term: Device Troubleshooting（设备排障命令）
  definition: 云管向设备远程下发预置命令（如 setDateTime）的工具，可编辑命令参数，稍后回读执行结果。
  source_chapter: "p235, p257"
  tags: [运维, 排障]

- id: g45
  term: Reports（Regular / Analytics Data）
  definition: 报表两类：Regular 用预置模板+组件布局；Analytics Data 选指标/列/范围导出 CSV 或 PDF。均可即时生成或排程（如每周一 8:00 Client Health 周报）。
  source_chapter: "p173-p175, p298"
  tags: [报表]

- id: g46
  term: Access Records（访问记录）
  definition: 含 Authentication Records（UPAM 认证记录，在线/历史）、Captive Portal Records（门户登录，含 Auth result/Reject Reason）、自助注册请求（Self-Registration）与 Guest/BYOD 记住设备。
  source_chapter: "p168-p172, p185-p186"
  tags: [监控, 认证]

- id: g47
  term: VoWLAN
  definition: 无线语音。部署遵循 Prepare/Plan/Design/Implement/Operate 五阶段；终端含 NOE/SIP 话机（8118/8128/8158s/8168s）、Rainbow/OTC 软终端；支持 802.11r/k/v 漫游辅助。
  source_chapter: "p300-p311"
  tags: [语音]

- id: g48
  term: IMS3
  definition: ALE 话机批量部署与管理服务器，用于话机安装、模板下发与配置管理。
  source_chapter: "p302, p310"
  tags: [语音, 运维]

- id: g49
  term: RSSI / SNR
  definition: 接收信号强度指示与信噪比。语音要求 RSSI≥-67dBm（wlanconfig 值≥29）、SNR≥25；正确漫游一般需 -62dBm 或更好。QoE Coverage 阈值默认 -66dBm。
  source_chapter: "p158, p272-p273, p308"
  tags: [RF, 语音]

- id: g50
  term: TTS / GTTT（Guest Tunnel）
  definition: 访客隧道终结交换机（Tunnel Termination Switch）。SSID 可选择 VLAN 或 Tunnel 映射（Tunnel ID + TTS IP），把访客流量经隧道送到远端 OS6860-GTTS 集中出口；配置时选 GTTT 映射方法并应用到设备组。（附录 p320-322 原文编码损坏，细节待对照原版确认）
  source_chapter: "p76, p320-p322"
  tags: [隧道, 访客, 待确认]

- id: g51
  term: STA / sta_list
  definition: STA 即无线终端。AP CLI 的 ssudo sta_list 列出各 SSID 下终端的 MAC/IP/在线时长/收发计数/认证方式/Final_role/VLAN/Tunnel，是客户端排障第一命令。
  source_chapter: "p269"
  tags: [CLI, 排障]

- id: g52
  term: Final_role
  definition: 终端认证后最终生效的访问角色，决定 ACL 与带宽；排障时核对是否与设计一致（如 __employee0、__guest0）。
  source_chapter: "p269, p271"
  tags: [安全, 排障]

- id: g53
  term: adme
  definition: AP 间邻居发现/管理进程；adme show 输出邻居 AP 的信道、RSSI、发射功率，是漫游排障（邻居可见性/信号）的关键命令。
  source_chapter: "p264"
  tags: [CLI, 漫游]

- id: g54
  term: eag
  definition: AP 上负责 Captive Portal 的进程；eag_cli show user all 看门户用户状态，/var/log/eag.log 看门户时序日志（IP 获取、重定向下发）。
  source_chapter: "p219-p220"
  tags: [CLI, 门户]

- id: g55
  term: br-wan
  definition: AP 的有线侧桥接口，AP 与接入交换机间全部流量经此；tcpdump 抓有线包（如 DNS）就指定该接口。
  source_chapter: "p238"
  tags: [CLI, 抓包]

- id: g56
  term: Miniboot
  definition: OmniSwitch 底层启动模式；复位/重启过程中误按回车会进入并中断正常重启。
  source_chapter: "p46"
  tags: [交换机, 陷阱]

- id: g57
  term: DPSK（Device Specific PSK）
  definition: 按设备分发 PSK：SSID 无全局口令，按 MAC（如打印机/树莓派）各配专属 passphrase，配合 WPA2_PSK_AES 使用。
  source_chapter: "p296"
  tags: [安全, SSID]

- id: g58
  term: Band Steering / Load Balance
  definition: RF Profile 功能：前者引导双频终端优先上 5GHz，后者在 AP 间自动动态负载均衡客户端（综合演练要求启用）。
  source_chapter: "p261, p296"
  tags: [RF]

- id: g59
  term: Ekahau RTLS / Site Survey
  definition: 第三方无线勘测与实时定位工具（Ekahau Survey PRO、AirMagnet）；话机支持 Ekahau RTLS 定位，运营阶段用于语音覆盖勘测。
  source_chapter: "p302, p311"
  tags: [勘测, 语音]

- id: g60
  term: MLO / Wi-Fi 7 关键特性
  definition: Wi-Fi 7（802.11be）的倍增能力：多链路操作 MLO、320MHz 信道、4096-QAM、Multi RU、前导码打孔、AFC，峰值 46Gbps；Stellar 对应 AP15xx 系列。
  source_chapter: "p32-p33"
  tags: [Wi-Fi7]
```
