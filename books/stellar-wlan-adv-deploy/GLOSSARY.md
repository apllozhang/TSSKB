# 术语词典 GLOSSARY

| 术语 | 全称 | 出处 | 定义 |
|---|---|---|---|
| **QoE (Quality of Experience)** |  | p122-p134, p158 | 体验质量分析。OmniVista Cirrus 用 Successful Connects / Time To Connect / Roaming / Coverage / Available Capacity / Device Uptime 六指标评估终端真实体验。 |
| **Time To Connect** |  | p128, p158 | QoE 指标，客户端完成关联、授权、DHCP、Portal 四阶段的总耗时；阈值 2-20s，默认 2s。 |
| **Available Capacity** |  | p129, p158 | QoE 指标，RF 信道可用容量高于阈值的时间占比；阈值 10%-50%，默认 10%。 |
| **Failure Classifier（失败分类器）** |  | p128-p133 | QoE 各指标失败原因归类，如 Asymmetry Downlink/Uplink、Weak Signal、DHCP、Association、Wi-Fi Interference 等，用于下钻定位。 |
| **Network Analytics（网络分析）** |  | p137-p145 | 按信道分布/信道利用率/设备健康（CPU、内存、闪存）/设备在线率四个维度评估 AP 与交换机的分析应用，可下钻到单设备与端口级。 |
| **Client Analytics（客户端分析）** |  | p146-p153 | 客户端维度的分析应用：连接数曲线、频段/SSID/AP 分布、吞吐消费、连接时长、每用户设备数。 |
| **Health Thresholds（健康阈值）** |  | p139, p298 | 设备 CPU/内存/闪存使用的告警百分比阈值，可在 Network Analytics 或 Edit Device 中按设备调整；演练基准 70%。 |
| **Heat Map（热力图）** |  | p176-p178 | 基于 AP 信号强度生成的可视化覆盖图，按站点或 AP 展示；生成最少需 3 台 Stellar AP。客户端密度热力图红/黄/绿对应高/中/低密度。 |
| **Access Role Profile (ARP)** |  | p91, p108 | 访问角色配置，定义终端的 ACL/QoS 与带宽限制（如 ARP_DEFAULT 受限、ARP_PASS 全通）；可由认证结果、IoT 分类或手工指派。注意与地址解析协议 ARP 无关。 |
| **Access Auth Profile** |  | p93 | 定义有线端口认证方法（802.1X/MAC/Portal）、所用 AAA Server Profile 与默认访问角色，并绑定 AP 组/交换机端口。 |
| **Unified Policy / Policy List** |  | p94 | 统一接入策略：以映射条件（如 Authentication Type = MAC）决定认证源、访问角色与 Web 重定向；多个策略组成 Policy List 挂到 SSID。 |
| **UPAM / UPAMRadiusServer** |  | p66, p107 | OmniVista 内置的统一策略与准入模块（含内置 RADIUS 服务器 UPAMRadiusServer），承载员工/访客账号、门户与本地认证数据库。 |
| **Captive Portal（强制门户）** |  | p70-p71, p170, p219-p220 | Web 认证页。OV-UPAM Captive Portal 类型配合 Guest Access Strategy、门户模板（Captive Portal Template）使用；记录在 Access Records > Captive Portal Records，含 Auth result 与 Reject Reason。eag 进程负责门户逻辑。 |
| **Walled Garden（围墙花园）** |  | p76 | SSID 访问角色中允许终端在认证前访问的白名单域名集合。 |
| **Wireless Client Social Login** |  | p76 | 允许无线客户端通过社交平台账号（Facebook WiFi 或 Google）认证的 SSID 选项。 |
| **UAPSD** |  | p77 | 非调度自动省电 delivery，IEEE 802.11e 定义的 QoS 省电机制，延长移动终端电池寿命；SSID 基本选项之一。 |
| **Client Isolation（客户端隔离）** |  | p77 | 阻断同一 AP 同一 SSID 内客户端之间互访的 SSID 安全选项，访客网络常用。 |
| **Bandwidth Contract（带宽契约）** |  | p78 | SSID 级、按每射频共享的总带宽上限（区别于按用户的 Bandwidth Control）。 |
| **Broadcast/Multicast Optimization** |  | p78-p79 | 广播优化含 Broadcast Filter All（除 DHCP/ARP 外全丢广播）与 Broadcast Filter ARP（广播 ARP 转单播）；组播优化把组播转单播，高负载（信道利用率 90% 或 6 个高吞吐客户端）自动停。 |
| **GTK / Broadcast Key Rotation** |  | p78 | 组临时密钥及其周期轮换（默认 15 分钟，1 分钟-24 小时），用于防组密钥破解；仅 Enterprise SSID 适用。 |
| **WMM** |  | p80-p81 | Wi-Fi 多媒体，四访问类别（Voice/Video/Best Effort/Background）的无线 QoS 框架，配合 802.1p/DSCP 标记。 |
| **DSCP / 802.1p** |  | p80-p81 | IP 层与二层 CoS 优先级标记。推荐语音 46(EF)/5、视频 34(AF41)/4、背景 18(AF21)/2、尽力而为 0/0。 |
| **Hotspot 2.0 (Passpoint)** |  | p82-p83 | 基于 802.11u(GAS/ANQP) 与 EAP-SIM/EAP-AKA 的无缝安全公众 Wi-Fi 机制；在 WPA2-Enterprise SSID 的高级 WLAN 配置中启用。 |
| **WiFi4EU** |  | p82-p83 | 欧盟公共场馆免费 Wi-Fi 计划；SSID 用 HTTPS Captive Portal，会话超时需可配至 12 小时；配置入口在 Guest SSID > Guest Access Strategy。 |
| **IoT Device Profiling（IoT 设备画像）** |  | p102-p108 | OmniVista 通过 MAC OUI 与 DHCP 指纹（option 55/60）识别终端类型并归入分类；分类可绑定 Access Role Profile 做强制控制（ARP Enforcement）。 |
| **MAC OUI** |  | p103, p297 | MAC 地址的厂商组织唯一标识前缀，IoT 识别手段之一；也用于 WIPS 里限定"其他厂商设备"的匹配条件。 |
| **DHCP Fingerprinting（DHCP 指纹）** |  | p103 | 利用 DHCP option 55（参数请求列表）与 option 60（厂商标识）的组合特征识别设备类型。 |
| **WiFi Bridge** |  | p113-p114 | 点对点无线桥接，替代物理布线连接两栋楼；可用 VLAN 分隔桥上流量，但不能向 Wi-Fi 客户端提供服务；AP1101/1201/1201H 不支持桥上 VLAN 打标。 |
| **WiFi Mesh** |  | p113-p115 | 无线网状组网：Root AP 接 LAN，Repeater 经无线回传；限制为全网 16 AP、8 从 AP、4 跳、单跳 5 AP、每 AP 5 SSID；最佳实践 5GHz 信道>100。 |
| **Auto Mesh** |  | p116 | 快速 Mesh 部署特性：接 LAN 的 Root 与未接 LAN 的 AP 自动以隐藏 SSID "Stellar-MESH"（5GHz）完成组网。 |
| **Root AP / Parent Address** |  | p115, p120 | Mesh 中的根节点（可多台）；Mesh Topology 监控中 Repeater 的 Parent Address 即其上游 Root AP 的 MAC。 |
| **WIPS / Rogue AP** |  | p297 | 无线入侵防护。可按"广播相同 SSID 名"与"非本厂商 MAC OUI"等条件把 AP 分类为 Rogue（流氓 AP）；支持攻击检测、黑名单（如 1 分钟认证失败 5 次）与 Containment（遏制，演练中禁用）。 |
| **MSP Portal / Organization** |  | p47 | OmniVista Cirrus 多租户入口页；每个 Organization 是独立租户（含站点、设备、许可证），角色分 Viewer/Admin。删除组织是不可逆操作。 |
| **Site / Building / Floor** |  | p48-p50 | 云管组织下的位置层级：站点 > 楼栋 > 楼层；设备必须归属站点，楼层可挂平面图用于热力图与定位。 |
| **Device Catalog（设备目录）** |  | p52, p97, p224 | 云管设备清单，创建设备（录序列号）、查看激活状态并对设备执行 Edit/SSH/Web UI/配置管理等 Actions；含 Wired Ports、CLI 模板、值映射等页签。 |
| **AP Group（接入点组）** |  | p61, p245 | AP 的配置分组，绑定 Provisioning Configuration 与 RF Profile；SSID 通过 VLAN/Tunnel Mapping 挂到组；改组会清空 AP 现有配置。 |
| **Provisioning Configuration（配给配置）** |  | p61, p193, p316 | AP 组级参数集：RF Profile、时区、SSH/AP Web 开关及凭据等；删除前须先解除与 AP 组的绑定。 |
| **RF Profile** |  | p261, p280-p281 | 射频管理模板：Band Steering、Load Balance、背景扫描、国家码、Air Time Fairness 及每射频信道/带宽/功率/RSSI 门限。AP 侧落盘于 /tmp/config/rfprofile.conf。 |
| **Call Home / Activation Status** |  | p55, p64-p65 | 设备周期性向云管注册的机制。激活状态流转：Waiting for first Contact → Connected to OV → Provisioning → OV Managed。交换机可 cloud-agent admin-state restart 加速，AP 可重启触发；show cloud-agent status / ocloud_show 查询。 |
| **OV Managed / Full Management vs Analytics Only** |  | p55, p224 | OV Managed 表示设备已完全受管；管理模式可选 Analytics Only（仅分析）或 Full Management（全管理）。 |
| **Golden Configuration（黄金配置）** |  | p145, p229-p230 | 被标记为基准的交换机 running 配置，可周期或即时审计比对；支持 Mark/Unmark as Golden Config 与备份恢复。 |
| **Network Events / Traps** |  | p179-p181, p254 | 设备通知事件，分 AP Traps、Switch Traps 与 QoE Analytics 三类；条目含 Severity（Normal/Warning/Minor/Major/Critical）、Ack 状态、重复次数；可 Acknowledge 或 Delete。 |
| **Collect Support Info（支持信息收集）** |  | p236, p254-p255 | 收集设备日志包供 ALE 排障：AP 为 tar.gz 快照（配置+日志）；交换机可选 swlog、cfg、Tech Support（L2/L3/Engineering Complete 分级）。 |
| **Device Troubleshooting（设备排障命令）** |  | p235, p257 | 云管向设备远程下发预置命令（如 setDateTime）的工具，可编辑命令参数，稍后回读执行结果。 |
| **Reports（Regular / Analytics Data）** |  | p173-p175, p298 | 报表两类：Regular 用预置模板+组件布局；Analytics Data 选指标/列/范围导出 CSV 或 PDF。均可即时生成或排程（如每周一 8:00 Client Health 周报）。 |
| **Access Records（访问记录）** |  | p168-p172, p185-p186 | 含 Authentication Records（UPAM 认证记录，在线/历史）、Captive Portal Records（门户登录，含 Auth result/Reject Reason）、自助注册请求（Self-Registration）与 Guest/BYOD 记住设备。 |
| **VoWLAN** |  | p300-p311 | 无线语音。部署遵循 Prepare/Plan/Design/Implement/Operate 五阶段；终端含 NOE/SIP 话机（8118/8128/8158s/8168s）、Rainbow/OTC 软终端；支持 802.11r/k/v 漫游辅助。 |
| **IMS3** |  | p302, p310 | ALE 话机批量部署与管理服务器，用于话机安装、模板下发与配置管理。 |
| **RSSI / SNR** |  | p158, p272-p273, p308 | 接收信号强度指示与信噪比。语音要求 RSSI≥-67dBm（wlanconfig 值≥29）、SNR≥25；正确漫游一般需 -62dBm 或更好。QoE Coverage 阈值默认 -66dBm。 |
| **TTS / GTTT（Guest Tunnel）** |  | p76, p320-p322 | 访客隧道终结交换机（Tunnel Termination Switch）。SSID 可选择 VLAN 或 Tunnel 映射（Tunnel ID + TTS IP），把访客流量经隧道送到远端 OS6860-GTTS 集中出口；配置时选 GTTT 映射方法并应用到设备组。（附录 p320-322 原文编码损坏，细节待对照原版确认） |
| **STA / sta_list** |  | p269 | STA 即无线终端。AP CLI 的 ssudo sta_list 列出各 SSID 下终端的 MAC/IP/在线时长/收发计数/认证方式/Final_role/VLAN/Tunnel，是客户端排障第一命令。 |
| **Final_role** |  | p269, p271 | 终端认证后最终生效的访问角色，决定 ACL 与带宽；排障时核对是否与设计一致（如 __employee0、__guest0）。 |
| **adme** |  | p264 | AP 间邻居发现/管理进程；adme show 输出邻居 AP 的信道、RSSI、发射功率，是漫游排障（邻居可见性/信号）的关键命令。 |
| **eag** |  | p219-p220 | AP 上负责 Captive Portal 的进程；eag_cli show user all 看门户用户状态，/var/log/eag.log 看门户时序日志（IP 获取、重定向下发）。 |
| **br-wan** |  | p238 | AP 的有线侧桥接口，AP 与接入交换机间全部流量经此；tcpdump 抓有线包（如 DNS）就指定该接口。 |
| **Miniboot** |  | p46 | OmniSwitch 底层启动模式；复位/重启过程中误按回车会进入并中断正常重启。 |
| **DPSK（Device Specific PSK）** |  | p296 | 按设备分发 PSK：SSID 无全局口令，按 MAC（如打印机/树莓派）各配专属 passphrase，配合 WPA2_PSK_AES 使用。 |
| **Band Steering / Load Balance** |  | p261, p296 | RF Profile 功能：前者引导双频终端优先上 5GHz，后者在 AP 间自动动态负载均衡客户端（综合演练要求启用）。 |
| **Ekahau RTLS / Site Survey** |  | p302, p311 | 第三方无线勘测与实时定位工具（Ekahau Survey PRO、AirMagnet）；话机支持 Ekahau RTLS 定位，运营阶段用于语音覆盖勘测。 |
| **MLO / Wi-Fi 7 关键特性** |  | p32-p33 | Wi-Fi 7（802.11be）的倍增能力：多链路操作 MLO、320MHz 信道、4096-QAM、Multi RU、前导码打孔、AFC，峰值 46Gbps；Stellar 对应 AP15xx 系列。 |