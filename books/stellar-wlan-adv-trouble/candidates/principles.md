# 原则/参数 · OmniAccess Stellar WLAN Advanced Troubleshooting (DT00XTE478EN)

> 来源：source/fulltext.md（页码即教材 PDF 页码）

- id: p01
  title: 排障前置条件——全网设备同步到同一 NTP 服务器
  type: principle
  source_chapter: "p22"
  source_quote: |
    Before troubleshooting: NTP server configured in the network. Synchronize all equipment with the same NTP server: Stellar APs, OmniVista, Access Switches.
  summary: |
    开始排障前必须确认网络里配置了 NTP 服务器，且 Stellar AP、OmniVista、接入交换机全部同步到同一个 NTP。没有 NTP 时各设备日志时间戳互不对齐，同一错误在三台设备上会显示不同时间，无法把多设备日志串成一条时间线做关联分析。这是教材明列的第一条工具使用前提。

  tags: [ntp, prerequisite, log-correlation]

- id: p02
  title: AP 本地接入三通道的参数（串口 115200 8N1 / SSH 开关 / Web UI 端口）
  type: principle
  source_chapter: "p23-26"
  source_quote: |
    Console: Speed 115 200, Data bits 8, Stop bits 1, Parity None, Flow ctrl None. File: /var/config/public_group.conf - ssh_connect = 1 (SSH enabled), ssh_connect = 0 (SSH disabled). Login to the AP web UI: https://<AP_IP> or http://<AP_IP>:8080. In OmniVista Cirrus - Enable "AP web" in the Provisioning Configuration List.
  summary: |
    三种登入 Stellar AP 的方式与关键参数：串口控制台参数为 115200 波特、8 数据位、1 停止位、无校验、无流控；SSH 由配置文件 /var/config/public_group.conf 中的 ssh_connect 控制（1 启用、0 禁用，Enterprise 模式需在 AP Group 里激活 SSH 并自定义密码，可用 putty/teraterm 连接）；AP Web UI 地址为 https://<AP_IP> 或 http://<AP_IP>:8080，云管理模式必须先在 OmniVista Cirrus 的 Provisioning Configuration 里开启"AP web"才能登录。

  tags: [console, ssh, web-ui, access]

- id: p03
  title: 在 AP 上抓有线包的 tcpdump 三步与语法
  type: principle
  source_chapter: "p30"
  source_quote: |
    Step 1 - CLI connection to the AP with "support" account. ssudo tcpdump -i br-wan -w testcapture.pcap udp port 53. You are listening to the interface br-wan - which is the wired interface - connecting the Stellar AP to the network. Step 2 - Transfer the captured file on your PC/laptop (SFTP tool, WinSCP). Step 3 - Open and read the file with Wireshark.
  summary: |
    用 support 账号 CLI 登录 AP，执行 ssudo tcpdump -i br-wan -w testcapture.pcap udp port 53：br-wan 是连接 AP 与有线网络的接口，-w 指定保存文件，过滤表达式按需替换（示例抓 DNS）。抓完后用 SFTP 工具（如 WinSCP）把 pcap 文件传回电脑，再用 Wireshark 打开分析。抓有线侧流量（DHCP、DNS、RADIUS 等）就用这条路径。

  tags: [tcpdump, packet-capture, br-wan, syntax]

- id: p04
  title: Air Capture（空口抓包）操作五要素与 10MB/5 分钟上限
  type: principle
  source_chapter: "p31-32"
  source_quote: |
    Step 1 - Cluster web UI: In "AP" window, click on the AP which will perform the Air capture. Step 2 - In RF Environment, select the Radio to capture. Click on Start Capture. Select the Channel. Enter the TFTP server where the capture will be sent. Option: Filter the capture (MAC, Frame type). Warning: Capture file limited to 10MB or 5min of capture.
  summary: |
    空口抓包流程：在集群 Web UI（云模式则先在 Cirrus 开启 AP Web 再登录 AP Web UI）选中执行抓包的 AP，在 RF Environment 里选射频，点 Start Capture 后依次指定信道、输入接收抓包文件的 TFTP 服务器地址，可选按 MAC 或帧类型过滤，停止后文件发到 TFTP，再用 Wireshark 打开。硬性限制：抓包文件最大 10MB 或最长 5 分钟，超限即止，规划过滤条件时要按此预算。

  tags: [air-capture, tftp, limit, rf-environment]

- id: p05
  title: AP 配置备份/恢复——复现故障与技术支持共享的标准件
  type: principle
  source_chapter: "p33"
  source_quote: |
    Backup the configuration of one or multiple Stellar AP. Used to re-create the issue. Shared with the technical support. Step 1 - Cluster web UI: In "AP" window, click on "Backup All Configuration". Download the file "pub-config.tar" locally. Step 2 - Re-create the issue: In your own setup, "Restore All Configuration" using the .tar file. Extract the config-pub.tar file. Check the configuration offline.
  summary: |
    在集群 Web UI 的 AP 窗口点"Backup All Configuration"，把生成的 pub-config.tar 下载到本地。用途有二：其一在自己的环境用"Restore All Configuration"恢复该配置以复现客户问题；其二解包 config-pub.tar 后离线逐项检查配置。该文件也是开技术支持工单时的标准共享材料。

  tags: [backup, restore, config-analysis]

- id: p06
  title: LED 状态判读表（单三色 LED 家族与多 LED 型号）
  type: principle
  source_chapter: "p41-44"
  source_quote: |
    Flashing Green: System Running, Default SSID broadcasted. Solid Green: System Running, Single band working. Solid Blue: System Running, Dual band working. Flashing Blue & Red: OS upgrading. Flashing Blue, Red & Green: Use for location of AP. Solid Red: System startup. AP1251/AP1360: 7 LEDs - SYS ON: Power On - System Running; ENET0/1 Solid: Ethernet Link UP; 5G/2.4G Solid: SSID created and running; PSE ON: PSE Enabled.
  summary: |
    AP12XX/13XX/14XX/15X1 用单颗三色 LED：闪绿=运行中且广播默认 SSID，纯绿=单频段工作，纯蓝=双频工作，蓝红闪=固件升级中，三色闪=用于 AP 定位，纯红=系统启动中。AP1251/AP1360 系列用 7 颗独立 LED 分别指示 SYS（常亮运行/闪烁加载升级）、2.4G/5G（SSID 创建运行）、ENET0/1（链路 up）、SFP、PSE（PoE 供电）；AP1201H 另有 PoE 状态灯：橙常亮=受电设备在线、橙闪烁=离线、灭=PSE 禁用。LED 是"AP 到底活没活着、单双频是否都在跑"的第一道免登录检查。

  tags: [led, hardware, status]

- id: p07
  title: support 账号与默认密码 aos2016
  type: principle
  source_chapter: "p45-46"
  source_quote: |
    Log in with support account. Login: support. Password: aos2016. In Enterprise mode, activate SSH login in the AP Group and define a custom password.
  summary: |
    CLI 排障的入口账号是 support，教材实验室环境默认密码 aos2016。Enterprise 模式下需在 AP Group 中激活 SSH 登录并自定义密码。tcpdump、top、ps、各类 ssudo 命令都以该账号执行。

  tags: [support-account, credential, cli]

- id: p08
  title: 系统信息命令集（showsysinfo / showver / getmode / show_cluster）
  type: principle
  source_chapter: "p45-48"
  source_quote: |
    support@AP-0E:E0:~$ showsysinfo - Company Name, SN, Device Model, MAC, Country, Software Version, Hardware Version. showver: 3.0.7.20. getmode: CLUSTER / OV / OVNG. show_cluster - List of Stellar APs in the cluster; IP address of the OmniVista server.
  summary: |
    四条基础信息命令：showsysinfo 输出序列号、型号、MAC、国家码、软硬件版本等（同样内容也出现在日志收集包里）；showver 看精确构建版本；getmode 区分管理模式——返回 CLUSTER 为 Express 模式、OV 为 Cloud 模式、OVNG 为另一云形态；show_cluster 列出集群内全部 AP（MAC/IP/角色/版本）及 OmniVista 服务器 IP，Cloud 模式下对应 getovinfo。核对国家码和版本是否与预期一致是硬件诊断第一步。

  tags: [cli, showsysinfo, getmode, cluster]

- id: p09
  title: 意外重启核查（date 对时 + uptime 看运行时长）
  type: principle
  source_chapter: "p50"
  source_quote: |
    Restart reason - Why did the AP reboot? Check in the AP log collection: Date - Check Stellar AP system time and date, Check Stellar AP synchronization to the NTP server. Is it the same time? Uptime - Check Stellar AP uptime. Unexpected Stellar AP reboot?
  summary: |
    排查 AP 为何重启时在 AP 日志收集包里查两项：日期（先跑 date 确认 AP 系统时间与 NTP 同步、时间一致，否则日志时间线不可信）和 uptime（当前运行时长，判断是否发生过计划外重启）。重启原因与重启前后的日志要靠对齐后的时间戳来定位。

  tags: [reboot, uptime, date, ntp]

- id: p10
  title: CPU/内存与进程状态诊断（top + ps，R/S 正常、X/Z 异常）
  type: principle
  source_chapter: "p51-53"
  source_quote: |
    High CPU utilization - Impact performances of the Stellar AP: speed, features not working as intended. Process Status - OK: R (Running), S (Interruptible Sleep); Issue: X (Dead) and Z (Zombie process). Too many Zombie processes will consume large portion of memory. Share these processes with the Technical Support when opening a ticket.
  summary: |
    用 top 看 AP 全局内存、CPU 占用和进程列表（Linux 命令，各进程的 %CPU 一眼定位元凶），用 ps 看单进程状态。判定标准：R（运行）和 S（可中断睡眠）为正常；X（死亡）和 Z（僵尸）为异常，僵尸进程过多会吃掉大量内存。高 CPU 会拖慢 AP 速度、功能不达预期。开技术支持工单时应把进程列表一并附上。

  tags: [cpu, memory, process, top, ps]

- id: p11
  title: Captive Portal 客户端与日志检查（eag_cli show user all + eag.log 三阶段）
  type: principle
  source_chapter: "p55-56"
  source_quote: |
    Note: "eag" process related to the Captive Portal. eag_cli show user all - ID, UserName, UserIP, UserMAC, SessionTime, OutputFlow, InputFlow, AuthType, ESSID. Check List: Is the client authenticated on the Captive Portal? For how long is the client connected? Does the client send/receive data to the network?
  summary: |
    Captive Portal 由 eag 进程负责。eag_cli show user all 列出全部门户用户，核对三件事：客户端是否已通过门户认证（有无表项）、连接了多久（SessionTime）、有无收发数据（OutputFlow/InputFlow，全零说明认证后不通）。再看 cat /var/log/eag.log 的三阶段痕迹：客户端首联时 IP 未知（userip 0.0.0.0）无法发重定向，随后获取 IP，最后发出 PortalRedirect 重定向 URL——卡在哪一段就查哪一段。

  tags: [captive-portal, eag, log]

- id: p12
  title: Express 集群健康三查（PVC 身份 / 成员表 / cluster 进程）
  type: principle
  source_chapter: "p58-59"
  source_quote: |
    cluster_mgt -x show=self: ClusterID, MAC, role PVC, status RUN. Check: Is a PVC found in the cluster? Is it supposed to be this PVC? Check the "cluster" process on the AP - Are both processes running? Two existing "cluster_mgt" threads indicates abnormal behavior (one running, one sleeping).
  summary: |
    集群排障三查：cluster_mgt -x show=self / show=pvc 确认集群里选出了 PVC、且是否本该是它，AP 角色与状态是否 RUN；show_cluster 确认所有成员 AP 都在列表里；ps | grep cluster 确认 cluster_mgt 与 cluster_cor 两个进程都在运行——若出现两个 cluster_mgt 线程（一个运行一个睡眠）即为异常行为。

  tags: [cluster, pvc, express-mode]

- id: p13
  title: 无线接口检查（iwconfig）与 athXYY 接口命名规则
  type: principle
  source_chapter: "p63"
  source_quote: |
    Check List: SSID broadcasted on the selected radio(s)? Transmission Power as selected in the RF profile? Encryption activated? BSSID is present? If there is no MAC address for "Access Point", the SSID is not broadcasted. athXYY: X = 0: 2.4GHz Radio, X = 1: 5GHz Radio, X = 2: 6GHz Radio, Y = [1...16]: SSID ID.
  summary: |
    iwconfig 列出各无线接口，核对清单：SSID 是否在选定射频上广播、发射功率是否等于 RF profile 配置值、加密是否开启、BSSID 是否存在——Access Point 一栏没有 MAC 地址就说明该 SSID 根本没广播出来。接口名 athXYY 自带语义：第一位 X 为频段（0=2.4GHz、1=5GHz、2=6GHz），后两位 YY 是 SSID 编号 1-16，如 ath001 即 2.4GHz 上的 1 号 SSID、ath102 即 5GHz 上的 2 号 SSID。

  tags: [iwconfig, ath-naming, ssid, bssid]

- id: p14
  title: RF profile 落地核对清单（cat /tmp/config/rfprofile.conf）
  type: principle
  source_chapter: "p64"
  source_quote: |
    Check List: Global parameters: same as configured? Band Steering, Load Balance, Scanning, Country Code, Air Time Fairness. Per Radio parameters: same as configured? Channel selection: auto or manual? Channel Width? Power selection: auto or manual? cat /tmp/config/rfprofile.conf - "bandSteering":"enable", "LoadBalance":"enable", "countryCode":"FR", "channelWidth":20, "powerSetting":"AUTO", "signalStrengthThreshold":0.
  summary: |
    用 cat /tmp/config/rfprofile.conf 查看 AP 实际生效的 RF 配置，与网管侧配置逐项比对。全局项：Band Steering、Load Balance、背景扫描（scanningInterval/Duration）、国家码、Air Time Fairness；每射频项：信道选择是 AUTO 还是手动、信道宽度、功率选择是 AUTO 还是手动，以及 signalStrengthThreshold（低信号踢除阈值）与 roamingSignalStrengthThreshold（漫游阈值）。很多"客户端被踢/不漫游"问题就出在这几个值上。

  tags: [rf-profile, config-check, threshold]

- id: p15
  title: 信道与发射功率核查（iwlist channel / iwlist txpower）
  type: principle
  source_chapter: "p65"
  source_quote: |
    iwlist ath001 channel - 57 channels in total; available frequencies... Current Frequency: 2.437 GHz (Channel 6). iwlist ath001 txpower - 8 available transmit-powers: 0, 5, 7, 9, 11, 13, 15, 17 dBm. Current Tx-Power=17 dBm (50 mW).
  summary: |
    iwlist athXXX channel 列出该接口全部可用频率并显示当前信道（2.4GHz 一般 1-13 信道，具体随国家码）；iwlist athXXX txpower 列出可选发射功率档位（如 0/5/7/9/11/13/15/17 dBm）及当前值。两条命令合用可确认"SSID 在哪个信道、功率是否为 RF profile 所选"，也是定位"当前 Tx-Power=3dBm 最小值"这类功率被压低问题的直接手段。

  tags: [iwlist, channel, txpower]

- id: p16
  title: VoWLAN 信号判定阈值（RSSI ≥ -67dBm 即 RSSI 值 ≥29；SNR ≥ 25）
  type: principle
  source_chapter: "p78-79"
  source_quote: |
    For VoWLAN deployment in 802.11ac: RSSI must be -67dBm (or better). Meaning RSSI >= 29. For VoWLAN deployment in 802.11AC: SNR >= 25. RSSI 10 = -86 Bad - too many packets loss; KO: Voice or real-time applications. RSSI 29 = -67 Recommendation for voice and real-time application. RSSI 43 = -53 Perfect.
  summary: |
    Stellar 的 RSSI 是正值刻度（换算 dBm = RSSI 值 - 96）：RSSI 10=-86dBm 属"差"，丢包过多，语音和实时应用不可用；RSSI 29=-67dBm 是语音与实时应用的推荐下限；RSSI 43=-53dBm 为完美信号；介于两者之间对邮件/上网够用但语音质量受损。802.11ac 语音部署（VoWLAN）硬指标：RSSI ≥ 29（即 -67dBm 或更好）且 SNR ≥ 25。评估覆盖是否够语音，用 wlanconfig 输出的 RSSI/MINRSSI/MAXRSSI 对照此表。

  tags: [rssi, snr, vowlan, threshold]

- id: p17
  title: 客户端总表检查（ssudo sta_list 六字段清单）
  type: principle
  source_chapter: "p75"
  source_quote: |
    ssudo sta_list - SSID, STA_MAC, IPv4, IPv6, OnlineTime, RX, TX, FREQ, AUTH, Final_role, VLANID, TUNNELID, FARENDIP. Check List: Client in the correct VLAN? Client got an IP address in the correct subnet? Stability of the client connection - uptime value. Client receives/transmits data - RX and TX counters. Correct authentication method? Correct Access Role Profile assigned - Final_role?
  summary: |
    ssudo sta_list 按 SSID 分组列出 AP 上全部客户端，逐项核对：VLANID 与 IPv4 是否落在正确 VLAN/子网、OnlineTime 判断连接是否稳定（频繁清零即反复掉线）、RX/TX 计数器判断是否真的在收发数据、AUTH 是否用了预期的认证方式（802.1X/MAC/Portal）、Final_role 是否分到了正确的访问角色档案。这是客户端排障的第一条命令。

  tags: [sta-list, client, vlan, final-role]

- id: p18
  title: 客户端认证属性详查（ssudo wam_debug sta_list）
  type: principle
  source_chapter: "p77"
  source_quote: |
    Depending on the authentication method used (802.1X, MAC, Captive Portal), does the client receive the correct parameters from the Stellar AP? Check List: Same parameters as the sta_list command - IP address, VLAN, Association Time, AccessRole Profile assigned. Correct Captive Portal URL? Is the Authentication a success? Correct Access Role Profile after authentication success?
  summary: |
    wam_debug sta_list 以 JSON 输出每个客户端的完整属性：关联时间、分配 VLAN（assignedVLAN）、MAC 认证结果（macAuthResult）、802.1X 认证结果、Captive Portal 认证结果（CPAuthResult）与各认证来源下发的 Access Role 和重定向 URL（redirectURLFromMACAuth 等）。用于判断：认证到底成没成功、成功后角色对不对、门户 URL 是否正确。三种认证来源各有一组字段，按客户端所用方式对应查看。

  tags: [wam-debug, authentication, access-role]

- id: p19
  title: 客户端空口信号与 OS 识别（wlanconfig athXX list + kes_syslog grep tid）
  type: principle
  source_chapter: "p76, p78"
  source_quote: |
    wlanconfig ath12 list - ADDR, AID, CHAN, TXRATE, RXRATE, RSSI, MINRSSI, MAXRSSI... SNR: 57, Operating band: 5GHz, HT Capability: Yes, VHT Capability: Yes. cat /proc/kes_syslog | grep tid - [TID_DHCP_PROTOCOL] ip:[10.7.0.41], mac:[d4:6e:0e:18:60:38], hostname:[StellarClient0], ostype:[iOS].
  summary: |
    wlanconfig athXX list 看单个无线接口上的客户端空口指标：RSSI/MINRSSI/MAXRSSI、SNR、TX/RX 速率、信道、HT/VHT 能力——对照 VoWLAN 阈值判断信号是否达标。cat /proc/kes_syslog | grep tid 从 DHCP 事件日志里识别客户端身份：IP、MAC、主机名和操作系统类型（ostype），用于确认客户端是否成功走完 DHCP、终端类型是否与故障相关。

  tags: [wlanconfig, signal, ostype, kes-syslog]

- id: p20
  title: 客户端关联/断连日志（kes_syslog 按 MAC 过滤，读 disassoc reason）
  type: principle
  source_chapter: "p80"
  source_quote: |
    cat /proc/kes_syslog | grep <client-MAC>. Check the association / disassociation exchange between Stellar AP and client. Check the disassociation reason in case of an unexpected disconnection of the client. [MLME] [ieee80211_recv_disassoc] Received Disassoc with reason 8 (OS moved the client to another AP using non-aggressive load balance), recv rssi 63.
  summary: |
    用 cat /proc/kes_syslog | grep <客户端MAC> 抓该客户端的全部事件：AUTH 帧（算法、序号）、关联/解关联交换、MLME 处理痕迹。关键是读非预期掉线时的 disassociation reason——例如 reason 8 表示"OS 用非激进的负载均衡把客户端移到了别的 AP"，即系统主动行为而非故障。日志里还带 recv rssi 等现场值，可还原掉线瞬间的信号状况。

  tags: [kes-syslog, disassoc-reason, association]

- id: p21
  title: RADIUS 配置核对点（AAA_server.conf 关键字段）
  type: principle
  source_chapter: "p89"
  source_quote: |
    cat /var/config/AAA_server.conf - "accountingPort":1813, "retries":2, "ipAddress":"10.130.5.250", "type":"Radius", "timeout":5, "authenticationPort":1812, "secret":"...". cat /var/config/wlanservice.conf - "securityLevel":"Enterprise", "encryptionType":"wpa2-aes", "aaaProfile":"employee0". cat /var/config/AAA_profile.conf - "primaryServer":"radius".
  summary: |
    AP 侧 RADIUS 三份配置文件连看：AAA_server.conf 定义服务器（IP、认证端口默认 1812、计费端口默认 1813、共享密钥 secret、超时 timeout=5、重试 retries=2）；wlanservice.conf 确认 SSID 的安全级别（Enterprise）、加密类型（如 wpa2-aes）和绑定的 aaaProfile；AAA_profile.conf 确认该 profile 的 primaryServer 指向正确的服务器。三处任一与 RADIUS 服务器实际配置不一致，认证就会失败。

  tags: [radius, aaa, port-1812, secret]

- id: p22
  title: AP 网络连通性检查四命令（ifconfig / route / ping / traceroute）
  type: principle
  source_chapter: "p94-95"
  source_quote: |
    ifconfig br-wan - Check the IP address and mask of the LAN interface. Traffic exchanged between the AP and the network? - Sent/Received packets. route -n - What is the gateway of the default route? Is it the correct default route? ssudo ping 10.130.5.50 - The Stellar AP can ping the OmniVista server. ssudo traceroute 10.130.5.50 - Check the path taken by the traffic.
  summary: |
    网络层排障的命令组合：ifconfig br-wan 看 AP 有线口 IP/掩码及 RX/TX 报文计数（判断与网络有无流量）；route -n 看默认路由网关是否正确；ssudo ping 逐个测网关、NTP/DHCP/DNS 服务器、防火墙、OmniVista 的可达性；ssudo traceroute 看流量实际路径、是否先送网关、路由协议是否需要调整。traceroute 跳数与时延（ttl=62, time=0.818ms）可作为参考。

  tags: [ifconfig, route, ping, traceroute, connectivity]

- id: p23
  title: 邻居 AP 判读（adme show：radioid/channel/rssi/txpower）
  type: principle
  source_chapter: "p69, p96"
  source_quote: |
    adme show - mac, ip, ov_ip, state, name, version, radiocnt, radioid, channel, rssi, txpower. Look for the Stellar APs managed by the same OV or in the same cluster. If a geographic neighbor: Is not seen, move it closer or increase it's transmission power. Is seen with a weak power signal (RSSI), move it or increase it's transmission power. RSSI < 20 is considered bad signal.
  summary: |
    adme show 输出 AP 看到的邻居表，每行一个邻居（含本机）：radioid 0=2.4GHz、1=5GHz，附信道、RSSI、发射功率。判读规则：同一 OmniVista 或同集群管理的 AP 应出现在表里；地理上的邻居看不到、或 RSSI < 20（差信号），都会导致漫游失败/客户端掉线，处理办法是挪近 AP 或加大其发射功率。教材示例中 RSSI 79 为"信号极好、近邻"，RSSI 15 为"邻居信号差"。

  tags: [adme, neighbor-ap, roaming, rssi]

- id: p24
  title: 时间与 DNS 配置核对（/tmp/TZ、resolv.conf、kes_syslog grep ntp）
  type: principle
  source_chapter: "p97"
  source_quote: |
    cat /etc/resolv.conf - nameserver 10.0.0.51, search ale-training.com. cat /tmp/TZ - UTC+08. Wrong time zone. cat /proc/kes_syslog | grep ntp - time was synced from pool.ntp.org.
  summary: |
    服务器配置核查三件套：cat /etc/resolv.conf 确认 DNS 服务器地址与搜索域；cat /tmp/TZ 看时区设置（教材示例 UTC+08 与实际场景不符，即"时区错误"）；cat /proc/kes_syslog | grep ntp 确认 AP 确实从 NTP 服务器（如 pool.ntp.org）完成过同步。时区错而时间同步正常，日志时间仍会整体偏移，跨设备对齐时要把这一项排查掉。

  tags: [dns, timezone, ntp, resolv-conf]

- id: p25
  title: syslog 不上报三步验证法（配置→进程→logger 实测）
  type: principle
  source_chapter: "p101"
  source_quote: |
    1) Syslog configuration on the AP? cat /var/config/syslog.conf - "log_remote":1, "log_ip":10.130.5.222, "log_port":514. 2) Syslog process running? ps | grep - /sbin/logread -f -r 10.130.5.222 514. 3) Test syslog communication: "logger" command sends a syslog packet to the remote syslog server. logger -p emerg "Just for test!" Message received on syslog server?
  summary: |
    OmniVista 会配置 AP 向外部 syslog 服务器发送日志，排查链路三步：先 cat /var/config/syslog.conf 确认 log_remote=1 且 log_ip/log_port（默认 514/UDP）指向正确服务器；再 ps | grep <服务器IP> 确认 logread -f -r 进程在跑；最后 logger -p emerg "Just for test!" 发一条测试报文，看服务器端是否收到。三步分别排除配置错、进程挂、网络不通。

  tags: [syslog, logread, logger, three-step]

- id: p26
  title: OmniVista Cirrus/Terra 接管的网络前置参数（防火墙端口与 DHCP 选项）
  type: principle
  source_chapter: "p170, p179"
  source_quote: |
    Open Firewall ports: 9093, 30123, 30124, 30125. And to allow outbound traffic from local network: 443, 80, 123, 53. Enable DHCP standard options: 1, 2, 6, 28, 42, 43. And, when using proxy: 129, 130, 131, 132, 133, 138. NTP server: At least 1 configured. Software version: AWOS 4.0.6 GA or higher (Cirrus) / AWOS 4.0.7.14 or higher (Terra).
  summary: |
    AP 交给 OmniVista 云管/本地管之前的网络硬前置：Cirrus 需在防火墙开 9093、30123-30125 端口，并放行出向 443/80/123/53；DHCP 启用标准选项 1、2、6、28、42、43（走代理再加 129-133、138）；至少配一台 NTP。Stellar AP 侧 AWOS 版本 Cirrus 要求 4.0.6 GA+、Terra 要求 4.0.7.14+，且 AP1101、AP1201L/H/HL 不受支持。OmniSwitch 需 8.9RX/8.10RX。云管"AP 上线失败"先查这组参数。

  tags: [omnivista, firewall, dhcp-options, prerequisite]
