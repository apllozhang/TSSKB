# 失败模式/警告 · OmniAccess Stellar WLAN Advanced Troubleshooting (DT00XTE478EN)

> 来源：source/fulltext.md（页码即教材 PDF 页码）。本书核心是"连不上/慢/掉线"的根因清单与规避，条目宁多勿漏。

- id: ce01
  title: 主案例：Employee SSID 全员连不上——接入交换机 VLAN 配错
  type: counter-example
  source_chapter: "p11-13, p17-18"
  source_quote: |
    "Wifi client can not log into the SSID Employee". VLAN 10 on the SSID in OmniVista and VLAN 20 on the Access Switch "Building_A": Wrong VLAN configured on the Access Switch. Root cause: Wrong VLAN configuration on the Access switch "Building_A". Resolution: Update the tagged VLAN with the ID = 20.
  summary: |
    全书主用例：整段楼的客户端都登不进 Employee SSID。访谈四问锁定范围后取 AP 日志和交换机配置，比对发现 OmniVista 里 SSID 映射 VLAN 10、而接入交换机 Building_A 上配的是 VLAN 20，tagged VLAN 不一致导致认证后拿不到正确子网。教训：SSID 的 VLAN 映射必须与接入交换机的 tagged VLAN 逐台核对，"所有人连不上而 AP 本身正常"优先怀疑交换机侧 VLAN。

  tags: [vlan-mismatch, access-switch, cannot-connect]

- id: ce02
  title: 客户端看不到 SSID 的三个根因（未广播/频段不支持/国家码不兼容）
  type: counter-example
  source_chapter: "p82"
  source_quote: |
    1) Is the SSID broadcasted by the AP? 2) Which radio does the client support? Compatible with the SSID broadcasted? 3) Country Code of the AP? Supported by the client? Wrong country code: Set manually a compatible channel on the AP in RF profile.
  summary: |
    客户端搜不到 SSID 时按序查三点：AP 是否真的在广播（iwconfig 看该 SSID 的 ESSID 与 Access Point/BSSID 是否存在）；客户端支持的频段（2.4/5/6GHz）与 SSID 所在射频是否兼容；AP 国家码与客户端是否兼容——国家码不匹配时部分信道在客户端一侧不可用，表现为"别人看得到我看不到"，规避办法是在 RF profile 里手动指定一个双方都兼容的信道。

  tags: [ssid-hidden, country-code, radio-compatibility]

- id: ce03
  title: AP 生成不了热图——该频段没有无线接口/WLAN 配置
  type: counter-example
  source_chapter: "p67-68"
  source_quote: |
    Reminder: AP needs a wireless interface to send/receive a wireless signal and so, generate a Heat Map. There is no Heat Map generated on OmniVista. Check if the AP has a wireless interface. To create a Heat Map for a specific radio (ex: 2.4GHz), a wireless interface must exist for this radio. WLAN configuration only for the 5GHz radio - No Heat Map for 2.4GHz.
  summary: |
    OmniVista 上没有热图时别急着怪网管：热图依赖 AP 存在对应频段的无线接口。先用 iwconfig 检查 AP 有没有无线接口；若只想看 2.4GHz 的热图却发现没有，根因往往是 WLAN 配置只建在 5GHz 射频上——该频段无 SSID 即无接口即无热图。规避：给目标频段配置 WLAN 服务后再看热图。

  tags: [heat-map, wireless-interface, no-wlan]

- id: ce04
  title: 漫游失败三大根因（互不为邻居/RSSI 过低/VLAN tag 不一致）
  type: counter-example
  source_chapter: "p69"
  source_quote: |
    Reasons for roaming failure: APs must be seen as neighbors. No Roaming from an untagged VLAN to a tagged VLAN. RSSI too low between source AP and destination AP.
  summary: |
    客户端在 AP 间漫游失败的三个根因：源 AP 与目标 AP 没有互相看到（不在邻居表里）；两 AP 间 RSSI 太低（教材示例邻居 RSSI 15 即"坏信号"，正常应远高于此）；一侧是 untagged VLAN、另一侧是 tagged VLAN——这种配置组合之间不漫游。规避：保证同 SSID 在各 AP 上 VLAN 封装方式一致，并用 adme show 核对邻居关系与信号。

  tags: [roaming-failure, neighbor, vlan-tagging, rssi]

- id: ce05
  title: 地理相邻但射频互相看不见（直角走廊阻挡）——手动添加邻居 AP
  type: counter-example
  source_chapter: "p70"
  source_quote: |
    In some cases, Stellar APs are geographical neighbors but can't see each other (i.e: radio waves blocked by corridor with right angles,...). The client context can't be shared. No roaming. Solution: On both AP, add statically the neighbor Stellar AP from the list of known AP. The client context can be shared through the LAN and the client can roam.
  summary: |
    两台 AP 地理上相邻，但射频被直角走廊等结构阻挡，互相收不到对方信号。漫游所需的客户端上下文无法通过空口共享，客户端漫游失败。解决办法是在两台 AP 上互相对称地静态添加对方为已知邻居（Device Catalog > Action > View > Neighbor APs > Manage neighbor），让客户端上下文改走 LAN 传递，漫游即可恢复。

  tags: [roaming, rf-blocked, static-neighbor, client-context]

- id: ce06
  title: 漫游是否成功的验证方法（wam.log 搜 L2/L3 roaming 关键字）
  type: counter-example
  source_chapter: "p71"
  source_quote: |
    From AP Log collection, open wam.log. Search for: "L3 roaming-start", "L3 roaming-success", "L2 roaming-success".
  summary: |
    排查漫游问题时不要凭客户端感受下结论：从 AP 日志收集包里打开 wam.log，搜索"L3 roaming-start""L3 roaming-success""L2 roaming-success"三类关键字。只有 start 没有 success 说明漫游发起后失败；两类都搜不到说明漫游根本没触发（回头查邻居/信号/VLAN）。L2 与 L3 漫游日志分别对应同子网和跨子网漫游。

  tags: [roaming, wam-log, verification]

- id: ce07
  title: 客户端拿不到 IP（一）：DHCP 报文路径丢包——双端抓包比对
  type: counter-example
  source_chapter: "p83"
  source_quote: |
    Capture DHCP messages on the client (wireshark) and the AP (tcpdump). Open trace.pcap with wireshark. Analyze DHCP packets. Packet loss between AP and client? tcpdump -i eth0 -s0 -w trace.pcap.
  summary: |
    客户端关联成功却拿不到 IP，先确认 DHCP 报文有没有走完全程：客户端侧用 Wireshark 抓无线包，AP 侧在有线口执行 tcpdump -i eth0 -s0 -w trace.pcap 抓全部流量，两份 trace 比对 DHCP Discover/Offer/Request/ACK 序列——AP 侧收不到 Discover 说明无线段丢失，AP 侧有 Discover 而 DHCP 服务器无响应说明问题在上游网络或服务器。

  tags: [dhcp, no-ip, packet-capture, eth0]

- id: ce08
  title: 客户端拿不到 IP（二）：进错 VLAN 或 Final_role 过滤了 DHCP 流量
  type: counter-example
  source_chapter: "p84"
  source_quote: |
    2) Client assigned to the correct VLAN? Client supposed to get an IP in the scope of the VLAN 20? Does the Final_role filter DHCP traffic?
  summary: |
    DHCP 报文路径正常仍拿不到 IP 时查两处：客户端是否被分进了正确的 VLAN（用 sta_list 看 VLANID 与 IPv4 是否落在该 VLAN 的地址池范围）；以及客户端的 Final_role（访问角色档案）是否把 DHCP 流量过滤掉了。第二个是隐蔽根因：认证下发的角色若不含 DHCP 放行规则，客户端永远完不成地址获取。

  tags: [dhcp, final-role, vlan, filter]

- id: ce09
  title: 客户端频繁掉线（一）：AP 发射功率被压到最小值
  type: counter-example
  source_chapter: "p85-86"
  source_quote: |
    1) AP transmit power is too low? iwlist ath11 txpower - Current Tx-Power=3 dBm (1 mW). Transmit power set to minimum value. wlanconfig ath11 list - RSSI 16... Bad signal quality. High probability of disconnection. Increase AP transmit power in RF profile.
  summary: |
    客户端反复掉线的第一嫌疑：AP 发射功率过低。教材案例中 iwlist ath11 txpower 显示 Current Tx-Power=3dBm（仅 1mW，档位最小值），客户端 RSSI 只有 16，日志直接判读"信号质量差、断连概率高"。处理：在 RF profile 里把该射频发射功率调高。排查顺序永远是先 iwlist txpower 看功率、wlanconfig list 看客户端 RSSI，再谈其他。

  tags: [disconnection, txpower, rssi-16, rf-profile]

- id: ce10
  title: 客户端频繁掉线（二）：低信号踢除阈值设得过高
  type: counter-example
  source_chapter: "p87"
  source_quote: |
    2) High RSSI Threshold? Cause client to disconnect if their RSSI is below the Threshold. "signalStrengthThreshold":70. Threshold too high. Decrease the value. 3) Wireless capture and logs: AP deny the client? Check disassociation/deauthentication packets? Air Capture on the 5GHz radio.
  summary: |
    rfprofile.conf 里 signalStrengthThreshold=70（对应约 -26dBm 的极高信号门槛）意味着低于该信号强度的客户端会被 AP 主动踢下线——功率正常也掉线时查这个阈值，教材标注"阈值过高，调低"。第三步兜底：对相应频段做空口抓包并查 kes_syslog，看有没有 AP 主动发出的 disassociation/deauthentication 报文，区分"被踢"与"失联"。

  tags: [disconnection, signal-threshold, deauth, rf-profile]

- id: ce11
  title: 802.1X 认证失败（一）：客户端侧四项自查
  type: counter-example
  source_chapter: "p88"
  source_quote: |
    1) On Client side: Check: Username and password, Encryption type, Security type/key, Certificate on client (if any).
  summary: |
    802.1X 排查从客户端开始：核对输入的用户名密码、加密类型、安全类型/密钥、以及客户端上的证书（如部署了）。这四项任何一处与 SSID 配置不符都会在 EAP 早期阶段失败，表现与"网络故障"一模一样。先排除客户端侧的低级错误，再往 AP 和服务器走。

  tags: [802.1x, client-side, credential, certificate]

- id: ce12
  title: 802.1X 认证失败（二）：AP 侧 RADIUS 绑定与参数不一致
  type: counter-example
  source_chapter: "p89"
  source_quote: |
    Correct Radius server attached to the SSID? Compare Radius configuration to Radius server: IP and ports, Shared Secret key.
  summary: |
    AP 侧两个核对点：SSID 是否绑定了正确的 RADIUS 服务器（wlanservice.conf 的 aaaProfile 链到 AAA_profile.conf 再到 AAA_server.conf）；AP 上的 RADIUS 参数（服务器 IP、认证 1812/计费 1813 端口、共享密钥）与 RADIUS 服务器实际配置是否一致。共享密钥不匹配是最常见的静默失败——两边都"配置了"，就是对不上。

  tags: [802.1x, radius, shared-secret, aaa]

- id: ce13
  title: 802.1X 认证失败（三）：RADIUS 服务器侧七项核对
  type: counter-example
  source_chapter: "p90"
  source_quote: |
    Compare Radius configuration and database to client and AP configuration: Username/password, Shared Secret, Radius client IP, Radius station IP (IP address of the Stellar AP), Certificate, Authentication and accounting ports, Radius service enabled? Firewall allows authentication and accounts ports?
  summary: |
    服务器侧核对清单：用户数据库里的用户名密码、共享密钥、RADIUS client IP、RADIUS station IP（即 Stellar AP 的地址，必须被登记为合法客户端）、证书、认证与计费端口、RADIUS 服务是否启用、防火墙是否放行认证计费端口。任一项不匹配，AP 发来的请求会被直接丢弃，客户端侧只能看到超时。

  tags: [802.1x, radius-server, firewall, nas-ip]

- id: ce14
  title: AP 拿不到 IP（一）：IP 分配模式是静态而非 DHCP
  type: counter-example
  source_chapter: "p99"
  source_quote: |
    1) IP address assignment? Static or DHCP? How to set the IP assignment to DHCP: Reset AP to factory default. Log in to AP web UI and set the IP address mode to DHCP. cat /etc/config/network - option proto 'dhcp'. DHCP assignment.
  summary: |
    AP 自身拿不到地址先查分配模式：cat /etc/config/network 看 wan 接口的 proto 是 dhcp 还是 static。要切回 DHCP 有两条路：恢复出厂默认，或登录 AP Web UI 把 IP 地址模式设为 DHCP。排障时确认 proto='dhcp' 是抓包前的前提——模式本身错了，抓包只能看到徒劳的请求。

  tags: [ap-ip, dhcp, network-config]

- id: ce15
  title: AP 拿不到 IP（二）：上联口抓 DHCP 报文，服务器至少应回 DHCP-NAK
  type: counter-example
  source_chapter: "p100"
  source_quote: |
    2) Capture and analyze DHCP packets on the uplink port. What you should see. Check network connection between AP and DHCP server when no answer is received. Check that DHCP server sends at least DHCP-NAK packet for out-of-pool request.
  summary: |
    在上联口抓包分析 DHCP 交互：正常应看到 Discover-Offer-Request-ACK 全流程；完全没有回应时排查 AP 与 DHCP 服务器之间的网络连通性；一个重要判读点是——客户端请求的地址不在服务器地址池内时，健康的服务器至少应回 DHCP-NAK 拒绝报文。连 NAK 都没有，说明请求根本没到服务器（中间链路/VLAN/中继问题），而非地址池问题。

  tags: [dhcp-nak, uplink, packet-analysis]

- id: ce16
  title: AP 的 syslog 不上报——三步定位（配置/进程/连通）
  type: counter-example
  source_chapter: "p101"
  source_quote: |
    OmniVista configures the AP to send syslog messages to an external syslog server. 1) Syslog configuration on the AP? 2) Syslog process running? 3) Test syslog communication: "logger" command sends a syslog packet to the remote syslog server. Message received on syslog server?
  summary: |
    日志服务器上收不到 AP 日志时按序三查：syslog.conf 里 log_remote 是否为 1、log_ip/log_port 是否指向正确服务器（默认 514）；logread -f -r <IP> <port> 进程是否在运行；再用 logger -p emerg 发一条测试报文看服务器端是否收到。分别对应配置丢失、进程未起、网络不通三类根因，逐步收窄。

  tags: [syslog, logread, logger, no-logs]

- id: ce17
  title: AP 高 CPU 的四类根因（异常进程/死循环/过量日志/DoS 攻击）
  type: counter-example
  source_chapter: "p52"
  source_quote: |
    Most common causes for high CPU utilization: Abnormal process. Process infinite loop - Probably software issue. Process extensive calculations - Probably due to extensive logs/traces. Stellar AP under DoS attack. Identify the process causing high CPU usage. Share these processes with the Technical Support when opening a ticket.
  summary: |
    高 CPU 影响 AP 速度和功能表现，四类常见根因：异常进程；进程死循环（大概率软件缺陷）；进程做大量计算（大概率源于过量的日志/跟踪开启）；AP 遭受 DoS 攻击。处理路径固定：top 按 %CPU 找出元凶进程（记录 PID 和命令名），开技术支持工单时附上进程列表。教材示例中 /usr/sbin/drm 占 81% CPU 即为待上报的异常进程。

  tags: [high-cpu, dos, infinite-loop, top]

- id: ce18
  title: 僵尸/死亡进程堆积吃光内存
  type: counter-example
  source_chapter: "p53"
  source_quote: |
    OK: R (Running), S (Interruptible Sleep). Issue: X (Dead) and Z (Zombie process). Too many Zombie processes will consume large portion of memory.
  summary: |
    ps 输出中 R 与 S 状态属正常；X（Dead）和 Z（Zombie）是异常信号。僵尸进程过多会消耗大量内存，最终拖垮 AP。巡检或内存异常时用 ps 扫一遍状态列，出现成片 Z/X 即找到了根因方向（通常是父进程未回收子进程，属软件问题，需上报技术支持）。

  tags: [zombie-process, memory, ps]

- id: ce19
  title: 无 NTP 或时区配置错误——多设备日志时间线无法对齐
  type: counter-example
  source_chapter: "p22, p97"
  source_quote: |
    No NTP server - Error 10, AP Logs 11/11/2019 08:15:30, OmniVista Logs 15/11/2019 13:15:30, Access Switch Logs 15/11/2019 13:15:30. cat /tmp/TZ - UTC+08. Wrong time zone.
  summary: |
    教材用三台设备的"Error 10"演示了没有 NTP 的后果：AP 日志显示 11 日、OmniVista 和交换机显示 15 日，同一事件在时间轴上相差四天，关联分析直接失效。另一种变形是 NTP 同步正常但时区配错（如 /tmp/TZ 为 UTC+08 而实际不符），日志整体偏移。规避：全网统一 NTP 源，排障前先核 date 与 /tmp/TZ。

  tags: [ntp, timezone, log-misalignment]

- id: ce20
  title: AP 意外重启——用 date + uptime 先钉住事实再翻日志
  type: counter-example
  source_chapter: "p50"
  source_quote: |
    Restart reason - Why did the AP reboot? Date - Check Stellar AP system time and date. Check Stellar AP synchronization to the NTP server. Is it the same time? Uptime - Check Stellar AP uptime. Unexpected Stellar AP reboot?
  summary: |
    怀疑 AP 非计划重启时：uptime 看当前运行时长（远小于部署时长即发生过重启），date 核对系统时间与 NTP 是否一致（时间不可信则日志定位无意义），再去日志收集包里按对齐后的时间戳找重启原因。跳过对时直接翻日志是常见弯路。

  tags: [unexpected-reboot, uptime, restart-reason]

- id: ce21
  title: 客户端"无故"掉线——disassoc reason 8 是系统负载均衡在搬客户端
  type: counter-example
  source_chapter: "p80"
  source_quote: |
    [MLME] [ieee80211_recv_disassoc] Received Disassoc with reason 8 (OS moved the client to another AP using non-aggressive load balance), recv rssi 63, min rssi 55, max rssi 64.
  summary: |
    客户端掉线日志里的 reason code 是定性关键：reason 8 明确写着"OS 使用非激进的负载均衡把客户端移到另一个 AP"——这是系统主动行为，不是射频或配置故障，不应按掉线事故处理。日志同时带 recv rssi/min/max 现场值可复核信号。遇到用户报"总掉线"先 grep disassoc reason，把系统行为和真故障分开。

  tags: [disassoc-reason-8, load-balance, false-alarm]

- id: ce22
  title: Captive Portal 重定向失败——客户端 IP 未知时 URL 发不出去
  type: counter-example
  source_chapter: "p56"
  source_quote: |
    Client first connection to the Captive Portal. Client IP address unknown. Redirection URL can not be sent. Client information gathered. Client IP address retrieved. Stellar AP sends redirection URL to the client.
  summary: |
    eag.log 揭示门户首联的固定次序：客户端刚上线时 IP 未知（日志 userip 0.0.0.0），此阶段重定向 URL 无法发送；AP 要先通过 DHCP 过程拿到客户端 IP（日志里 eag_ipinfo_get 前后对比可见 IP 从 0.0.0.0 变为真实地址），随后才发出 PortalRedirect。门户页面转不出来的排查要点：卡在 IP 未知阶段说明 DHCP 没完成，应先查地址获取，而不是查门户本身。

  tags: [captive-portal, redirect, dhcp-order, eag-log]

- id: ce23
  title: Express 集群异常信号——出现两个 cluster_mgt 线程
  type: counter-example
  source_chapter: "p59"
  source_quote: |
    Check the "cluster" process on the AP. Are both processes running? Two existing "cluster_mgt" threads indicates abnormal behavior (one running, one sleeping).
  summary: |
    ps | grep cluster 正常应看到 cluster_mgt 与 cluster_cor 各一个进程。若 cluster_mgt 出现两个线程（一个 running 一个 sleeping），教材明确判定为异常行为，集群状态不可信。结合 show_cluster 核对成员是否齐全、cluster_mgt -x show=self 核对 PVC 角色，三查合一定位集群层故障。

  tags: [cluster, cluster-mgt, process-anomaly]

- id: ce24
  title: 邻居 AP 不可见或 RSSI<20——漫游断连的前置病灶
  type: counter-example
  source_chapter: "p96"
  source_quote: |
    If a geographic neighbor: Is not seen, move it closer or increase it's transmission power. Is seen with a weak power signal (RSSI), move it or increase it's transmission power. RSSI < 20 is considered bad signal. Roaming issue (client disconnection) if the Neighbor AP is not seen or the signal is too weak.
  summary: |
    adme show 里地理邻居看不到、或 RSSI 低于 20（判定为差信号），会直接导致漫游问题（客户端掉线）。处理手段二选一：把 AP 挪近，或调大其发射功率。判读时注意 radioid 0=2.4GHz、1=5GHz，同一邻居两个频段分别评估；教材示例 RSSI 79 为"信号极好的近邻"。

  tags: [neighbor-ap, rssi-20, roaming, disconnection]

- id: ce25
  title: AP 装在遮挡物正前方——混凝土柱/墙后出现死区
  type: counter-example
  source_chapter: "p109"
  source_quote: |
    Access Point placement: bad location (wall, pillar). Placement of AP in front of obstructing object - Concrete wall. Dead zone. Add a new AP. Place an AP on both side of the obstructing wall.
  summary: |
    AP 正对混凝土柱或墙安装时，背后必然出现死区。规避：在遮挡墙两侧各布一台 AP，或新增 AP 补盲。布点审查时先在平面图上标出障碍物，再核对 AP 位置是否处在遮挡物的"照射阴影"里——这是勘测阶段最容易提前发现的信号问题。

  tags: [ap-placement, dead-zone, obstruction]

- id: ce26
  title: 材料衰减清单——穿 1-4 面墙 4 米后 -70dBm 已不够语音
  type: counter-example
  source_chapter: "p110"
  source_quote: |
    Physical obstruction: Environment (multiple walls, materials). Distance = 4 meters. 1 to 4 walls crossed. RSSI = -70dBm. Not enough for VoWLAN. Signal degrades when going through: Concrete (walls), Wood (doors), Metal (cabinet, shelves), Steel (building structure), Glass & Mirrors, Brick (fireplace), Water (liquid: fish tank; vapor: bathroom).
  summary: |
    教材实测：仅 4 米距离但中间隔 1 到 4 面墙，RSSI 就掉到 -70dBm——上网邮件勉强可用，做 VoWLAN 语音已不达标（需 -67dBm 以上）。衰减源清单：混凝土墙、木门、金属柜/货架、钢结构、玻璃与镜子、砖砌体、水（鱼缸液体、浴室水汽）。覆盖设计时按材料估算穿损，宁可高估，语音场景尤其要留裕量。

  tags: [attenuation, material, -70dbm, vowlan]

- id: ce27
  title: 天线类型选错——定向天线覆盖形状不匹配环境
  type: counter-example
  source_chapter: "p111"
  source_quote: |
    Access Point Antennas: directional or omnidirectional. Wrong type of antennas. Directional antenna - Small Area covered. Omnidirectional antenna - No (20 meters) Area covered. Use the appropriate type of antenna based on the environment.
  summary: |
    定向天线只覆盖小扇区，全向天线覆盖整圆（示例 20 米），装反了类型就会出现"一半区域没信号、另一半信号过剩"。原则：按环境选天线——走廊/长条空间用定向，开放办公区用全向；支持外接天线的 AP 型号末位为"2"（如 AP1322、AP1362）。覆盖奇怪的盲区先看天线类型是否与空间形状匹配。

  tags: [antenna, directional, omnidirectional, coverage-shape]

- id: ce28
  title: 同频/邻频干扰三症状——吞吐下降、丢包、数据损坏，治法是换信道
  type: counter-example
  source_chapter: "p112"
  source_quote: |
    Access Point placement: RF interference. Co-channel Interference. Adjacent channel Interference. - Loss of throughput -> Change AP channel. - Packets loss. - Corrupted data -> Change AP channel.
  summary: |
    AP 间射频重叠过度产生同频（Co-channel）或邻频（Adjacent channel）干扰，三个典型症状：吞吐量下降、丢包、数据损坏。教材给出的处置直接明确：更换 AP 信道。勘测时用 Ekahau 或 WiFi Analyzer 的信道视图找出重叠的信道分配，重新规划信道复用模式（配合信道宽度收窄）。

  tags: [co-channel, adjacent-channel, interference, change-channel]

- id: ce29
  title: 勘测现场五类典型发现（盲区/遮挡/默认功率/型号不符/干扰）
  type: counter-example
  source_chapter: "p115-116"
  source_quote: |
    Identify AP model: same as original design? Identify RF overlap between Access Points: Co/Adjacent channel interference? Identify areas with no radio coverage: Access Point down? No Access Point placed? Access Point transmission power: Default or customized value? Access Point location: Troublesome placement? Default transmit power (17dBm) - Increase for best coverage.
  summary: |
    勘测观察阶段应逐项记录的五类问题：现场 AP 型号与原设计不一致；AP 间射频重叠造成同频/邻频干扰；无覆盖区域——区分 AP 宕机和根本没布 AP；发射功率仍是默认值（如 17dBm）而未按覆盖需求定制，需要调大；AP 位置别扭（被遮挡、位置不佳）。教材现场案例即同时出现了无覆盖、缺 AP、遮挡区和默认功率四项。

  tags: [survey-findings, default-power, coverage-gap]

- id: ce30
  title: 勘测纠正动作清单（换型号/重做 RF/收窄信道宽度/砍低速率/改放置）
  type: counter-example
  source_chapter: "p117"
  source_quote: |
    Step 3 - Corrective actions: Change Access Point model: AP with better antenna, outdoor AP. Rework RF wireless design: modify transmit powers, change radio channels. Rework channel width: limit adjacent / co-channel interference. Remove lower data rates: force devices to use closer APs with better signal strength. Improve AP placement: improve RF signal delivery.
  summary: |
    勘测结论落地为五类纠正动作：更换 AP 型号（更强天线/户外型）；重做射频设计（调整发射功率、更换信道）；收窄信道宽度抑制同频/邻频干扰；移除低数据速率——逼终端只能关联信号更好、距离更近的 AP，这是常被忽略的优化项；改善 AP 放置以改善射频送达。典型用例是调功率、加 AP、挪 AP 三件事的组合。

  tags: [corrective-actions, rf-design, low-rates, channel-width]
