# 原则/参数 · OmniAccess Stellar WLAN Express (DT00XTE455EN)

> 来源：source/fulltext.md（页码即教材 PDF 页码）。Express 模式的默认值、集群规则、射频与硬件参数、内置服务规则均在此。

- id: p01
  title: Express 集群规模硬上限 255 台，第 256 台不纳管
  type: principle
  source_chapter: "p81"
  source_quote: |
    "A Group can not contain more than 255 APs. The 256th AP is not taken into account and will stay in 'joining' mode. To have more than 255 APs on a network it is necessary to configure several Group-ids or to configure two separate VLANs."
  summary: |
    Express 模式单集群（同 Group ID）最多 255 台 AP，这是硬性上限：第 256 台 AP 不会被接管，永远停留在 joining 状态。扩容只有两条路——再建新的 Group ID，或拆分 VLAN（一 VLAN 一 Group ID）。项目规划时按 255 台为界做分域设计，不要指望把 AP 全塞进一个组。

  tags: [cluster-limit, 255-aps, group-id, joining]

- id: p02
  title: PVM 选举规则：先比最高型号，再比最高 MAC
  type: principle
  source_chapter: "p80"
  source_quote: |
    "In the case of a VLAN with several APs started at the same time an election process is perform to select the PVM. Highest Model Type. Highest MAC address. AP with the second highest MAC is designated as the SVM."
  summary: |
    同一 VLAN 内多台 AP 同时启动时的选举判据有先后：第一排序键是 AP 型号等级（Highest Model Type，高端型号优先担任 PVM），型号相同时比 MAC 地址大小（最高者任 PVM）。MAC 第二高的 AP 自动成为 SVM。p82 进一步给出可担任 PVM/SVM 的型号清单（AP1230、1301/1301H/1311、1320、1331、1351、1360、1411/1431/1451、1511/1521）。混合组网时可用该规则预判哪台会成为管理节点。

  tags: [pvm-election, svm, model-type, mac-address]

- id: p03
  title: 集群之间不做 L2/L3 漫游
  type: principle
  source_chapter: "p81"
  source_quote: |
    "Limitations: No Layer 3 Roaming. No Layer 2 Roaming between clusters."
  summary: |
    Express 集群的明确能力边界：集群之间既无三层漫游也无二层漫游。终端从一个 Group 的覆盖区走到另一个 Group 的覆盖区，会经历完整的断开重连，不保持会话。做多集群设计（超 255 台或分域）时必须把这条写进预期：漫游只在集群内部发生，跨集群的移动场景要么合并集群，要么接受重连。

  tags: [roaming, cluster-boundary, limitation]

- id: p04
  title: 集群实际 AP 上限随在网型号而变（32/64/255）
  type: principle
  source_chapter: "p138"
  source_quote: |
    "If the AP still can't join the cluster, check if the cluster has already reached the maximum number of APs allowed (32/64/255 APs depending on the AP models present in the cluster)."
  summary: |
    入集群排障时的检查点：集群最大 AP 数不是恒定 255，而是取决于集群内在网 AP 的型号组合，可能被压到 32/64/255 三档之一。也就是说混入低端型号会拉低整组上限。AP 卡在 joining/无法入组时，除了查 Group ID 与子网，还要核对当前集群规模是否已达到该型号组合允许的上限。

  tags: [cluster-max, model-dependent, 32-64-255]

- id: p05
  title: 集群通过单一 Group Mgt IP 完成同步与管理
  type: principle
  source_chapter: "p84"
  source_quote: |
    "Via a single IP interface (Group Mgt IP): Configuration synchronization. Group Management Interface. Notifications. APs of the groups exchange admin synchronization and RF coordination, hardware resources use, etc. Network AP Discovery: APs establish WLAN adjacencies to take into account their radio environment."
  summary: |
    集群对外的管理面收敛到单一 IP 接口（Group Mgt IP），承载三件事：配置同步、组管理界面、通知。集群内部成员间持续交换管理同步与射频协调信息；成员各自承担数据面管理、认证管理、本地 ACL 等本地职责；并通过建立 WLAN 邻接关系互相感知射频环境。运维上只需记住 Group Mgt IP 一个入口即可管理整组。

  tags: [group-mgt-ip, synchronization, single-interface]

- id: p06
  title: 远程集群管理的边界：防火墙放行组管理 IP，不支持远程镜像升级
  type: principle
  source_chapter: "p86"
  source_quote: |
    "AP Group can be managed remotely (opening the Firewall settings for AP Group Management IP). All operations supported (except AP Group image upgrade)."
  summary: |
    远程管理整个 AP Group 的前提条件与例外：需要在防火墙上为 AP Group Management IP 开放相应设置；开放后除"AP Group 镜像/固件升级"以外的全部操作都支持远程执行（架构为对 PVM/SVM 的 get/set）。规划远程运维时要预留防火墙变更窗口，并把固件升级排进现场/本地操作。

  tags: [remote-management, firewall, image-upgrade-exception]

- id: p07
  title: Bridge 四属性配置原则：三同 + 单根
  type: principle
  source_chapter: "p113"
  source_quote: |
    "SSID: Must be the same on both APs. Band: Must be the same on both APs. Is Root: Specify the root AP of the wireless bridge, 1 AP must be set as Root. Passphrase: Must be the same on both APs."
  summary: |
    无线桥两端 AP 的四个属性中，SSID、Band、Passphrase 三项必须完全一致，Is Root 必须且只能有一端为 Yes（单根原则）。任何一项不满足桥就建不起来。排障时按"三同一根"逐项核对两端配置即可定位多数桥接失败。

  tags: [bridge-attributes, single-root, config-match]

- id: p08
  title: Mesh 允许多根，且节点可同时服务客户端
  type: principle
  source_chapter: "p112, p114"
  source_quote: |
    "Is Root: Specify the root node of the wireless Mesh. Multiple APs can be defined as root. WIFI MESH PROPERTIES: VLANs can be used to separate & secure traffic coming from Wi-FI clients connected on different SSID. Can provide service (WiFi) to WiFi clients."
  summary: |
    Mesh 与 Bridge 的两个关键差异：（1）根节点数量——Bridge 只能一个根，Mesh 可以把多台 AP 都定义为 root（多出口回程，提高可靠性）；（2）服务能力——Bridge 链路纯粹做回程不能给客户端提供 WiFi，Mesh 节点可以在回程之外同时广播 SSID 服务客户端，且可用 VLAN 按不同 SSID 分离加固客户端流量。选型口诀：只要延伸覆盖就用 Mesh，只做两点连线就用 Bridge。

  tags: [mesh-multi-root, client-service, mesh-vs-bridge]

- id: p09
  title: Mesh/Bridge 回程最佳实践：5GHz（或 6GHz）、信道大于 100
  type: principle
  source_chapter: "p113-114"
  source_quote: |
    "WIFI MESH – BEST PRACTICE: BAND: 5 GHZ (OR 6GHZ). CHANNEL > 100."
  summary: |
    教材对 Mesh/Bridge 回程链路的固定建议（两页重复强调）：频段选 5GHz，有 6GHz 能力的设备选 6GHz；信道选 100 以上（5GHz 高段）。目的是让回程避开拥挤的 2.4GHz 和低段 5GHz，同时不与客户端业务信道互相干扰。配置回程 SSID 时直接套用这条参数。

  tags: [best-practice, backhaul, 5ghz, channel-above-100]

- id: p10
  title: Auto Mesh 默认参数：隐藏 SSID "Stellar-MESH"、5GHz、非 LAN 即非根
  type: principle
  source_chapter: "p115"
  source_quote: |
    "DEFAULT SSID: STELLAR-MESH. DEFAULT BAND: 5 GHZ. If a Stellar AP is: Connected to the LAN, Configured as MESH root, It will Broadcast an hidden SSID « Stellar-MESH », Band: 5 GHz. If a Stellar AP is: Not connected to the LAN, It will Have MESH enabled as non-root."
  summary: |
    Auto Mesh 的出厂行为规则：手工配置好 Mesh root 的那台 AP（接 LAN）会自动广播隐藏 SSID "Stellar-MESH"（5GHz）作为回程；任何未接 LAN 的 Stellar AP 上电即自动启用 Mesh 非根模式并连入该隐藏 SSID。也就是说部署时只需要配置根节点，其余节点零配置入网。识别现场是否走了 Auto Mesh，就搜隐藏 SSID "Stellar-MESH"。

  tags: [auto-mesh, default-ssid, stellar-mesh, zero-config]

- id: p11
  title: Enterprise/Cloud 模式统一 4000 台上限，Cloud 功能等同 OV2500
  type: principle
  source_chapter: "p42, p44"
  source_quote: |
    "ENTERPRISE MODE: Centralized management via the OmniVista 2500 NMS, Up to 4000 APs. CLOUD MODE: Centralized management via the cloud platform OmniVista Cirrus NMS, Up to 4000 APs, OmniVista Cirrus = similar features as OmniVista 2500."
  summary: |
    从 Express 迁出时的规模基线：Enterprise（OV2500 网管）与 Cloud（OmniVista Cirrus 云管）模式都支持最多 4000 台 AP，分布在无数量上限的 AP Group 里；Cirrus 的功能集与 OV2500 基本相同，差别只在本地部署与云端。选型时可按"255 以内 Express、超 255 看有无网管/云偏好"决策。

  tags: [4000-aps, enterprise-mode, cloud-mode, ov2500, cirrus]

- id: p12
  title: AP 供电规格：最大 12W、48V DC、DC 与 PoE 双源时 DC 优先
  type: principle
  source_chapter: "p128"
  source_quote: |
    "Maximum (worst-case) power consumption: 12 W (802.3at PoE or DC). 48 V DC (nominal) 802.3af/802.3at compliant source. When both power sources are available, DC power takes priority."
  summary: |
    供电排障的基准参数：AP 最坏情况功耗 12W（802.3at PoE 或 DC 供电）；DC 供电额定 48V，兼容 802.3af/802.3at 电源；当 PoE 与 DC 同时在场时，DC 优先。上电异常时先按这三条核对电源输出能力与供电方式，再查 LED。

  tags: [power-spec, 12w, 48vdc, dc-priority, poe]

- id: p13
  title: AP LED 状态判读表（颜色×闪烁=九种状态）
  type: principle
  source_chapter: "p128"
  source_quote: |
    "Blue ON: Power on. Green ON: Bootloader-OS loading. Flash: System running, Network abnormal (Interface down). Flash: Network normal, without SSID created. ON: single band working, either 2.4Ghz or 5Ghz. ON: dual bands working. Red and Blue LED alternate flashing; OS is upgrading. 3 LEDs alternate flashing; Used for locating an AP."
  summary: |
    上电排障的判读标准：蓝色常亮=已上电；绿色常亮=Bootloader 加载系统；闪烁=系统运行中网络异常（接口 down）/网络正常但未建 SSID；常亮（单频工作）=2.4G 或 5G 只起来一个频段；常亮（双频工作）=两个频段都正常；红蓝交替闪=系统升级中；三灯交替闪=定位 AP 用。AP"点不亮"时按此表核对 LED 颜色再决定下一步查电源还是查网络。

  tags: [led, status-indicator, power-troubleshooting]

- id: p14
  title: AP 出厂默认管理 IP 192.168.1.254
  type: principle
  source_chapter: "p129"
  source_quote: |
    "Connect to the AP, using the web GUI with the default IP address 192.168.1.254. Configure the IP address of the PC in the same subnet than the AP. If the AP can be joined on the web GUI, ensure that the IP address is set to DHCP."
  summary: |
    AP 拿不到 DHCP 地址时的兜底入口：出厂默认 IP 为 192.168.1.254。操作法：把运维 PC 配到同网段，浏览器直连该 IP 进 Web 界面，确认 IP 模式已设为 DHCP。这是"DHCP 失联仍可救"的官方路径，也适用于新开箱设备的直接接管。

  tags: [default-ip, 192-168-1-254, web-gui, rescue]

- id: p15
  title: Console 串口参数固定 115200-8-N-1
  type: principle
  source_chapter: "p130"
  source_quote: |
    "Access the AP using the console. Baud Rate: 115200. Data Bits: 8. Parity: None. Stop bits: 1."
  summary: |
    Web 与 SSH 全部失联时走 Console 的终端参数：波特率 115200、数据位 8、无校验、1 停止位。连不上串口时先核这四项与线缆质量（p135），再怀疑设备。

  tags: [console, serial, 115200, 8-n-1]

- id: p16
  title: 集群通信端口：32767 承载 PVM 报文，32768 承载 AP→PVM 报文
  type: principle
  source_chapter: "p137-138"
  source_quote: |
    "Use the command 'ssudo tcpdump –i br-wan –s 0 port 32767' to capture the PVM's messages. Use the command 'ssudo tcpdump –i br-wan –s 0 port 32768' to capture the messages sent by the AP to the PVM."
  summary: |
    集群协议的两个关键端口号：UDP/TCP 32767 用于 PVM 下发的报文，32768 用于成员 AP 发往 PVM 的报文。入组排障时分别用 tcpdump 抓这两个端口判断集群通信是否在跑：32767 抓不到说明收不到 PVM 消息（查网络环境），32768 抓不到说明 AP 根本没在发（重启 AP）。跨防火墙部署集群时这两个端口必须放行。

  tags: [cluster-ports, 32767, 32768, tcpdump]

- id: p17
  title: AP 默认发射功率 17dBm，覆盖不足时应上调
  type: principle
  source_chapter: "p174"
  source_quote: |
    "4: Default transmit power (17dBm), Increase for best coverage. 5: Move AP to optimize RF coverage."
  summary: |
    勘测观测环节的基准值：Stellar AP 默认发射功率为 17dBm。现场发现覆盖不足时，纠正动作之一就是核对功率是否还停留在默认值，需要覆盖就上调；另一动作是挪 AP 位置优化射频覆盖。排障五问里"发射功率是默认还是改过"的判定即以 17dBm 为参照。

  tags: [transmit-power, 17dbm, default-value, coverage]

- id: p18
  title: 信号衰减实测基准：4 米穿 1-4 堵墙后 RSSI 跌到 -70dBm，不够 VoWLAN
  type: principle
  source_chapter: "p168"
  source_quote: |
    "Distance = 4 meters. 1 to 4 walls crossed. RSSI = -70dBm. Not enough for VoWLAN. Signal degrades when going through: Concrete (walls), Wood (doors), Metal (cabinet, shelves,…), Steel (building structure), Glass & Mirrors, Brick (fireplace), Water (liquid: fish tank; vapor: bathroom)."
  summary: |
    教材给出的直观衰减量级：仅 4 米距离、穿越 1 到 4 堵墙，RSSI 就掉到 -70dBm——这个电平已不足以承载 VoWLAN（无线语音）。衰减大户按材质排序：混凝土（墙）、木材（门）、金属（柜子/货架）、钢结构（建筑骨架）、玻璃与镜面、砖（壁炉）、水（鱼缸液体/浴室水汽）。覆盖设计与"为什么这里信号差"的解释都拿这条做基准。

  tags: [rssi, -70dbm, attenuation, materials, vowlan]

- id: p19
  title: 天线选型原则：按覆盖形状选定向或全向
  type: principle
  source_chapter: "p169"
  source_quote: |
    "Directional antenna: Small Area covered. Omnidirectional antenna: No [large] Area covered. Wrong type of antennas. Use the appropriate type of antenna based on the environment."
  summary: |
    天线选错是信号问题的经典根因：定向天线覆盖一小片定向区域，全向天线覆盖周围一圈。把定向天线当全向用（或反之）会出现"该覆盖的地方没信号、不该覆盖的地方很强"。原则是按环境所需覆盖形状选型；Stellar 全系 AP 标配内置全向天线，外置天线型号（型号尾数 2）才可换定向/异形天线（见 p30）。

  tags: [antenna, directional, omnidirectional, selection]

- id: p20
  title: 同频/邻频干扰的症状与对策：一律换信道
  type: principle
  source_chapter: "p170"
  source_quote: |
    "Co-channel Interference. Adjacent channel Interference. Loss of throughput → Change AP channel. Packets loss. Corrupted data → Change AP channel."
  summary: |
    两类射频干扰的判定与处理：同频干扰（Co-channel，多 AP 抢同一信道）与邻频干扰（Adjacent，相邻信道部分重叠）。症状是吞吐下降、丢包、数据损坏。教材给的对策统一而干脆：给受影响 AP 换信道。勘测时用 Ekahau（Windows）或 WiFi Analyzer（Android）确认干扰类型后执行。

  tags: [co-channel, adjacent-channel, interference, channel-change]

- id: p21
  title: 低吞吐/高时延五查清单（限速→协商速率→ACS→干扰→ISP）
  type: principle
  source_chapter: "p155"
  source_quote: |
    "If low throughput/latency is observed, check the following points: Is there a speed limit in the WLAN configuration. Check the wireless mode that the client supports and the negotiation speed. Is the ACS function enabled? If not, enable it. Is there too much interference in the air? If so, change to another channel. Check the bandwidth with your ISP."
  summary: |
    性能投诉的标准检查顺序：先查 WLAN 配置里是否设了限速；再查客户端支持的无线模式与实际协商速率；确认 ACS（自动信道选择）是否开启，没开就开；空中干扰过大就换信道；最后核对 ISP 出口带宽。五步由近及远（配置→终端→信道→空口→出口），避免一上来就怪网络。

  tags: [low-throughput, acs, speed-limit, isp, checklist]

- id: p22
  title: 覆盖优化五招与"删低速率逼终端贴近 AP"
  type: principle
  source_chapter: "p175"
  source_quote: |
    "Change Access Point model: AP with better antenna, outdoor AP,… Rework RF wireless design: modify transmit powers, change radio channels,… Rework channel width: limit adjacent / co-channel interference. Remove lower data rates: force devices to use closer APs with better signal strength. Improve AP placement: improve RF signal delivery."
  summary: |
    勘测后的纠正措施全集：换 AP 型号（更好天线/户外型）、重做射频设计（改发射功率/换信道）、收窄信道宽度压制邻频同频干扰、删除低数据速率（强制终端漫游到信号更好的近处 AP，而不是黏在远端 AP 的低速率上）、改进 AP 布放。其中"删低速率"是最反直觉也最有效的一招——低速率留着只会让边缘终端赖着不走。

  tags: [corrective-actions, low-data-rates, rf-design, channel-width]

- id: p23
  title: AP 型号规格选型基线（SSID 数/客户端数/端口与 PoE 分档）
  type: principle
  source_chapter: "p13-25"
  source_quote: |
    "AP1301: Dual radio, 2.4GHz 573Mbps, 5GHz 1.2Gbps, 1 full band (radio) dedicated to radio scanning, Up to 16 SSID (8 per radio), 512 clients per AP, PoE 802.3af compliant, Full function at 802.3af PoE source. AP1451: Tri radio, Up to 48 SSID (16 BSSID per radio), 1536 clients per AP, 2 x 10GE uplink, PoE IEEE 802.3bt compliant."
  summary: |
    硬件章（p13-25）给出的全系选型参数，可归成四条分档规律：SSD 数与客户端数随档位走——入门（AP1301/1311/1411）16 SSID/512 客户端，中端（AP1320/1331/1360）32 SSID/1024 客户端，高端（AP1351/1451）24-48 SSID/1536 客户端；供电随性能走——入门 802.3af 即全功能，中高端要 802.3at/bt；上联口随档位从 1GE 到 2.5/5/10GE 乃至多速率口；多数型号含 BLE5.1/ZigBee 物联网射频与专用扫描射频（1 full band dedicated to radio scanning）。选型先定 SSID/终端规模档，再核供电与上联。

  tags: [ap-models, ssid-limit, client-limit, poe-class, uplink]

- id: p24
  title: 外置天线型号命名规则：尾数 2；全系标配内置全向天线
  type: principle
  source_chapter: "p30"
  source_quote: |
    "Access points compatible with external antennas have their reference ends with '2' (ex. AP1322, AP1362). Note: All OmniAccess Stellar Access Points are equipped with an internal antenna (omni-directional coverage pattern). Gain more control over the energy radiated. Tailor the shape based on the coverage needed."
  summary: |
    识别可接外置天线的 AP 的口诀：型号以"2"结尾（AP1322、AP1362 等）。所有 Stellar AP 出厂都带内置全向天线；上外置天线的目的是精细控制能量辐射方向、按覆盖需求定制天线形状（定向/异形覆盖）。配件选型时先看尾数再查对应天线的 datasheet 与 Product Line Matrix。

  tags: [external-antenna, naming-rule, omni-antenna, accessories]

- id: p25
  title: Wi-Fi 世代性能参数演进表（4→7：46Gbps/320MHz/4096-QAM/MLO）
  type: principle
  source_chapter: "p35"
  source_quote: |
    "Wi-Fi Generations: Wi-Fi 4 (2007, 802.11n, 1.2 Gbps, 2.4/5 GHz, WPA2), Wi-Fi 5 (2013, 802.11ac, 3.5 Gbps), Wi-Fi 6 (2019, 802.11ax, 9.6 Gbps, WPA3), Wi-Fi 6E (2021, 2.4/5/6 GHz), Wi-Fi 7 (2024, 802.11be, 46 Gbps, Up to 320 MHz, 4096-QAM, 16x16 MU-MIMO, MLO)."
  summary: |
    对客户讲清"为什么换新 AP"的参数基线：最大速率从 Wi-Fi 4 的 1.2Gbps 一路到 Wi-Fi 7 的 46Gbps；频段 6E 起增加 6GHz；信道宽度到 Wi-Fi 7 支持最高 320MHz；调制从 64-QAM 进化到 4096-QAM；MIMO 从 4x4 到 16x16；Wi-Fi 6 起强制 WPA3、引入 TWT 省电，Wi-Fi 7 增加 MLO 多链路操作与低时延。结合 p8-11 的 Stellar 型号谱系（Wi-Fi 5 到 Wi-Fi 7）可直接映射产品代际。

  tags: [wifi-generations, 802-11be, mlo, 4096-qam, spectrum]

- id: p26
  title: Express 模式内置能力清单（安全/射频/系统三组关键项）
  type: principle
  source_chapter: "p41"
  source_quote: |
    "Scale up to 255 APs in mixed AP Cluster. Authentication 802.1X, WPA, WPA2, WPA3. Encryption WEP, TKIP, AES. Built-in User Database. External Radius Server Support. ACLs per SSID. Disconnect/Blacklist Clients. WIPS protection. Dynamic Frequency Selection. Transmit Power Control. Built-in DHCP/DNS/NAT. Wireless MESH. Certificate Management."
  summary: |
    Express 虽无网管，能力并不残缺，售前答疑直接引用：混合型号集群至 255 台；认证 802.1X/WPA/WPA2/WPA3，加密 WEP/TKIP/AES；内置用户数据库，也支持外接 RADIUS；每 SSID 的 ACL、断开/拉黑客户端、WIPS 防护；射频侧 DFS 动态选频、TPC 发射功率控制、信道与功率可手工指定；系统侧内置 DHCP/DNS/NAT、无线 Mesh、证书管理、多语言 GUI（含简中）、OXO Connect R2.1 ZTP 集成、远程集群管理。

  tags: [express-features, security, radio, built-in-services, ztp]
