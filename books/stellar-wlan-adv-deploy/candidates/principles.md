# principles · 原则/参数（stellar-wlan-adv-deploy / DT00XTE361）

```yaml
- id: p01
  title: QoE Time To Connect 阈值：2-20 秒，默认 2 秒
  type: principle
  source_chapter: "p158"
  source_quote: |
    "The threshold can be configured from 2s to 20s. The default threshold value is 2s."
  summary: |
    连接耗时（Time To Connect）为关联/授权/DHCP/Portal 四阶段耗时之和，超过阈值即记为失败，超时最长的阶段被标记为失败原因。可配范围 2s-20s，默认 2s。
  tags: [QoE, 阈值, Time-To-Connect]

- id: p02
  title: QoE Roaming 阈值：0.2-2 秒，默认 0.2 秒
  type: principle
  source_chapter: "p158"
  source_quote: |
    "The threshold (which is the max target time it takes for a client to roam) can be configured from 0.2s to 2s. The default threshold value is 0.2s."
  summary: |
    漫游指标统计阈值时间内两 AP 间漫游成功占比；最大目标漫游耗时可配 0.2s-2s，默认 0.2s。
  tags: [QoE, 阈值, 漫游]

- id: p03
  title: QoE Coverage 阈值：-90 至 -55 dBm，默认 -66 dBm
  type: principle
  source_chapter: "p158"
  source_quote: |
    "The threshold can be configured from -90 dBm to -55 dBm. The default threshold value is -66 dBm."
  summary: |
    覆盖指标统计客户端信号高于阈值的时间占比；信号不达标按分类器归因（Asymmetry Downlink / Asymmetry Uplink / Weak Signal / Others）。
  tags: [QoE, 阈值, 覆盖, RSSI]

- id: p04
  title: QoE Available Capacity 阈值：10%-50%，默认 10%
  type: principle
  source_chapter: "p158"
  source_quote: |
    "Tracks the percentage of time the available RF channel capacity was greater than the defined threshold. The threshold can be configured from 10% to 50%. The default threshold value is 10%."
  summary: |
    可用容量指标统计 RF 信道可用容量高于阈值的时间占比；失败原因分类为 Wi-Fi 干扰、客户端数量、客户端使用量等。
  tags: [QoE, 阈值, 容量]

- id: p05
  title: WMM QoS 四类的推荐 DSCP/802.1p 映射
  type: principle
  source_chapter: "p80-p81"
  source_quote: |
    "Recommended Settings: Best Effort 0/0; Background 2/18-AF21; Voice 5/46-EF; Video 4/34-AF41. (p81)"
  summary: |
    WMM（Wi-Fi 多媒体，基于 802.11e）四队列推荐映射：Best Effort→802.1p 0/DSCP 0；Background→2/18(AF21)；Video→4/34(AF41)；Voice→5/46(EF)。上下行可分别配置 802.1p/DSCP 标记。示例上行映射：Voice 46、Video 32、Best Effort 0、Background 8。
  tags: [QoS, WMM, DSCP, 802.1p]

- id: p06
  title: 广播密钥轮换周期默认 15 分钟（1 分钟-24 小时）
  type: principle
  source_chapter: "p78"
  source_quote: |
    "Rotate the keys periodically to avoid key cracking. Default period: 15 min – Range 1 min – 24 hours."
  summary: |
    企业级 SSID 可周期轮换组密钥（GTK）防止破解，默认 15 分钟，可配 1 分钟到 24 小时；仅适用于 Enterprise 类型。
  tags: [SSID, 安全, GTK, 广播优化]

- id: p07
  title: 组播优化的两个自动停用上限
  type: principle
  source_chapter: "p79"
  source_quote: |
    "Upper limit of multicast optimization: Multicast Based Channel Utilization: default value 90%; Number of Clients: default value 6."
  summary: |
    组播优化把组播转单播（用 PTK 加密、走更高速率），但高负载时自动停止：基于组播的信道利用率达 90%（RF 环境太差），或高吞吐客户端数达 6（CPU 负载过高）即停。
  tags: [组播优化, SSID, 参数]

- id: p08
  title: WiFi4EU 会话超时可配至 12 小时
  type: principle
  source_chapter: "p82"
  source_quote: |
    "Networks with WiFi4EU SSID use an HTTPS Captive Portal. Session timeout should be configurable up to 12 hours."
  summary: |
    WiFi4EU（欧盟公共场馆免费 Wi-Fi 计划）SSID 必须使用 HTTPS Captive Portal，会话超时需可配置到最长 12 小时；配置入口在 Guest SSID > Guest Access Strategy。
  tags: [WiFi4EU, Captive-Portal, 公共Wi-Fi]

- id: p09
  title: WiFi Mesh 容量限制与最佳实践
  type: principle
  source_chapter: "p114-p115"
  source_quote: |
    "UP TO 8 SLAVE APS; UP TO 4 HOPS; UP TO 5 APS IN A SINGLE HOP IN A PEER TO MULTI PEER CONNECTION; UP TO 16 APS IN THE MESH NETWORK; ALL APS CAN BROADCAST UP TO 5 SSIDS FOR CLIENTS. WIFI MESH – BEST PRACTICE: BAND: 5 GHZ; CHANNEL > 100."
  summary: |
    Mesh 硬性限制：全网最多 16 台 AP、每 Root 最多 8 台从 AP、最多 4 跳、单跳点对多点最多 5 台、每台 AP 最多向客户端广播 5 个 SSID。最佳实践：Mesh 回传用 5GHz、信道选 100 以上（避开常用客户端信道）。
  tags: [Mesh, 容量限制, 最佳实践]

- id: p10
  title: Bridge/Mesh 三要素两端必须一致
  type: principle
  source_chapter: "p114-p115"
  source_quote: |
    "SSID ... Must be the same on both APs; Band ... Must be the same on both APs; Passphrase ... Must be the same on both APs."
  summary: |
    Bridge 与 Mesh 链路的 SSID、频段、密码三要素在两端 AP 必须完全一致才能建链；Mesh 另有 Is Root 选项指定根节点（可多 Root）。
  tags: [Mesh, Bridge, 配置规则]

- id: p11
  title: IoT 设备识别：MAC OUI + DHCP 指纹
  type: principle
  source_chapter: "p103"
  source_quote: |
    "MAC OUI: allows devices to be recognized by identifying their MAC addresses. DHCP FingerPrinting... DHCP option 55 (the parameter request list) and option 60 (the vendor identifier)."
  summary: |
    OmniVista 识别 IoT 终端靠两招：MAC OUI（厂商前缀）与 DHCP 指纹（option 55 参数请求列表 + option 60 厂商标识）。识别结果归入预置或自定义分类，分类可绑定 Access Role Profile 做 ARP 强制（Enforcement）；未知类型可向 Device Profile 服务查询。
  tags: [IoT, DHCP指纹, MAC-OUI, 设备画像]

- id: p12
  title: 热力图最少需要 3 台 AP
  type: principle
  source_chapter: "p177"
  source_quote: |
    "Visual Heat Map of deployed Stellar APs — Per Site, Per Access Point. * Minimum of 3 Stellar APs required to generate a Heat Map."
  summary: |
    生成可视化热力图（按站点/按 AP）至少需要部署 3 台 Stellar AP；当前客户端密度热力图用颜色表示密度：高=红、中=黄、低=绿，按任意时刻检测到的设备数计算（p178）。
  tags: [热力图, 监控, 部署要求]

- id: p13
  title: 排障前先做 NTP 全网时间同步
  type: principle
  source_chapter: "p191"
  source_quote: |
    "NTP server configured in the network. Synchronize all equipment with the same NTP server: Stellar APs, OmniVista, Access Switches."
  summary: |
    排障铁律：没有 NTP 时 AP、交换机、OmniVista 日志时间戳互相对不上，跨设备日志关联无法进行。排障前先确认网络已配置 NTP 服务器，且 AP、OmniVista、接入交换机都同步到同一台。
  tags: [排障, NTP, 日志关联]

- id: p14
  title: Stellar AP 串口控制台参数 115200 8N1
  type: principle
  source_chapter: "p192"
  source_quote: |
    "Speed: 115 200; Data bits: 8; Stop bits: 1; Parity: None; Flow ctrl: None."
  summary: |
    AP 串口控制台连接参数固定：波特率 115200、8 数据位、1 停止位、无校验、无流控。默认 CLI 账号 support/aos2016；企业（云管）模式需在 AP 组的 Provisioning Configuration 里先启用 SSH 并设密码。
  tags: [串口, 排障, AP, 参数]

- id: p15
  title: VoWLAN 信号标准：RSSI ≥ -67 dBm（值 29）、SNR ≥ 25
  type: principle
  source_chapter: "p272-p273"
  source_quote: |
    "For VoWLAN deployment in 802.11ac: RSSI must be -67dBm (or better). Meaning RSSI ≥ 29. ... For VoWLAN deployment in 802.11AC: SNR ≥ 25."
  summary: |
    语音与实时应用要求：802.11ac 下客户端 RSSI 至少 -67dBm（wlanconfig 显示的 RSSI 值 ≥ 29），SNR ≥ 25。RSSI 换算参考表：RSSI 10≈-86dBm（丢包严重，语音/实时不可用），20≈-76dBm（邮件/上网可用），29≈-67dBm（语音推荐），35≈-61dBm（理想）。
  tags: [VoWLAN, RSSI, SNR, 语音]

- id: p16
  title: VoWLAN 规划常数：-62dBm 漫游门限、每 AP 20-25 语音用户、1AP/255m²
  type: principle
  source_chapter: "p307-p308"
  source_quote: |
    "1 access point / 255 m²; Number of users per AP – Average of 20-25 users; ... Generally a -62dBm RSSI (or better) is required to ensure a correct roaming; 20 to 25 clients per Aps, providing 36 Mbps user throughput."
  summary: |
    语音覆盖规划常数：每 255m² 一台 AP；每 AP 平均 20-25 个用户（保证每用户 36Mbps 吞吐）；正确漫游一般要求 RSSI -62dBm 或更好；RF 管理优先 5GHz（更稳健、性能最佳）；接入交换机需千兆用户端口，语音用独立 VLAN 保障带宽与 QoS。
  tags: [VoWLAN, 容量规划, 漫游门限]

- id: p17
  title: 设备升级必然带来重启与终端断连
  type: principle
  source_chapter: "p253"
  source_quote: |
    "Note that when a device is upgraded, it will reboot with the new image. It will then become unavailable during this upgrade duration and all the end clients connected to this device will be disconnected."
  summary: |
    升级计划的影响评估原则：设备升级即重启，升级窗口内设备不可用，其上所有终端断线。排升级时间窗（如 6 小时窗口）与目标版本时必须把这点纳入变更通知。升级计划四步：Schedule Setting（频率/起止/升级时长）→ AP 组或单 AP 选择 → 软件版本（可全组统一或分组指定）→ Review。
  tags: [升级, 变更影响, 运维]

- id: p18
  title: 演练用监控阈值基准：健康 70%、2.4G 利用率 20%、客户端健康 90%、可用容量 25%
  type: principle
  source_chapter: "p298"
  source_quote: |
    "Set all the health thresholds of your network devices to 70%. Lower the Radio Utilization threshold of the 2.4GHz to 20%... the 2.4G client health threshold should be set at 90%... Have an Available Capacity set to 25%."
  summary: |
    综合演练给出一组可借鉴的场景化阈值：全网设备健康（CPU/内存/闪存）70%；因 2.4GHz 只跑打印机，射频利用率阈值收紧到 20%、2.4G 客户端健康阈值 90%（打印机要求常在线）；可用容量 25%（无线用量超过 75% 即告警）。启示：阈值应对齐业务用途，而非全用默认。
  tags: [阈值, 监控, 场景化配置]

- id: p19
  title: 实验环境凭据与连接基线
  type: principle
  source_chapter: "p46-p47"
  source_quote: |
    "Use the login 'admin' and the password 'switch'. ... Use the login 'support' and password 'aos2016' (default). ... Login: pod##@ale-training.com... Password: Superuser01!"
  summary: |
    ALE 远程实验室凭据基线：OmniSwitch 默认 admin/switch；Stellar AP 默认 support/aos2016；OmniVista Cirrus 云管账号 pod##@ale-training.com（会话密码由讲师经 LMS 下发）。云管地址 https://eu.manage.ovcirrus.com。无线客户端（树莓派）VNC 账号 user/superuser。
  tags: [凭据, 远程实验室, 默认账号]

- id: p20
  title: 漫游失败三大原因判据
  type: principle
  source_chapter: "p264"
  source_quote: |
    "REASONS FOR ROAMING FAILURE: APs must be seen as neighbors; No Roaming from an untagged VLAN to a tagged VLAN; RSSI too low between source AP and destination AP."
  summary: |
    判漫游失败先查三件事：① 两 AP 必须互相看见（adme show 邻居表）；② 同一 SSID 在两 AP 的 VLAN 封装方式必须一致（untagged VLAN 与 tagged VLAN 之间不能漫游）；③ 源/目标 AP 间 RSSI 过低。成功验证看 AP 日志 wam.log 中的 L2/L3 roaming-success 条目（p265）。
  tags: [漫游, 排障, VLAN]

- id: p21
  title: 拓扑图设备与链路状态颜色语义
  type: principle
  source_chapter: "p247-p248"
  source_quote: |
    "Green - Device connectivity is up and there are no trap notifications. Orange - connectivity is unknown or warning/major traps... Red - connectivity is up with critical trap notifications. Blue - minor or normal trap notifications... Solid-Grey - connectivity is down."
  summary: |
    拓扑状态色约定：绿=连通且无告警；橙=连通状态未知或收到 warning/major 告警；红=连通但有 critical 告警；蓝=连通但有 minor/normal 通知；灰=设备失联；无圈=无管理连通信息。链路：绿=全部 up，红=全部 down；多链路聚合成一条线显示，悬停可看明细。刷新约 2 秒（p231）。
  tags: [拓扑, 状态色, 监控]

- id: p22
  title: 无线接口命名规则 athXYY
  type: principle
  source_chapter: "p260"
  source_quote: |
    "athXYY — X = 0 : 2.4GHz Radio; X = 1 : 5GHz Radio; X = 2 : 6GHz Radio; Y = [1…16] : SSID ID."
  summary: |
    AP CLI 里虚拟无线接口命名可直接解读：第一位数字 0/1/2 对应 2.4/5/6GHz 射频，后两位是 SSID 编号（1-16）。例如 ath001 = 2.4GHz 上的 1 号 SSID，ath101 = 5GHz 上的 1 号 SSID。
  tags: [CLI, 接口命名, 排障]

- id: p23
  title: Captive Portal 首连时序：先拿 IP 才能重定向
  type: principle
  source_chapter: "p220"
  source_quote: |
    "Client first connection to the Captive Portal. Client IP address unknown. Redirection URL can not be sent. ... Client IP address retrieved. Stellar AP sends redirection URL to the client."
  summary: |
    eag.log 揭示的门户重定向时序：客户端首次关联时 IP 为 0.0.0.0，AP 无法下发重定向 URL；须等 DHCP 完成、客户端 IP 获取后（eag_ipinfo_get 后日志），AP 才发送 Portal 重定向。排障"打不开认证页"应先确认客户端是否已拿到 IP。eag_cli show user all 可看认证状态、会话时长与收发流量（p219）。
  tags: [Captive-Portal, 排障, 时序]

- id: p24
  title: 抓包两条路径：AP 有线口 tcpdump 与 AP Web 空口抓包
  type: principle
  source_chapter: "p238-p240"
  source_quote: |
    "ssudo tcpdump –i br-wan -w test-capture.pcap udp port 53 ... All the traffic exchanged between the AP and the access switch is going through this interface. (p238)"
  summary: |
    有线侧抓包：SSH 登 AP，tcpdump 指定 br-wan 接口（AP 与接入交换机的全部流量都走它），如抓 DNS：ssudo tcpdump -i br-wan -w test-capture.pcap udp port 53，再用 SFTP（WinSCP）取出 pcap 用 Wireshark 打开。空口抓包：在 Provisioning Configuration 启用 "AP web"，登录 https://AP_IP，RF Environment 里选信道、可按 MAC/帧类型过滤，抓包文件送往 TFTP 服务器。第三方空口抓取建议 >5 分钟（p200）。
  tags: [抓包, tcpdump, Wireshark, 排障]
```
