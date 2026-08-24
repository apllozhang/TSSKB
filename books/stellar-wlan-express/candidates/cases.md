# 案例 · OmniAccess Stellar WLAN Express (DT00XTE455EN)

> 来源：source/fulltext.md（页码即教材 PDF 页码）。配置演示章节多为截图驱动，文字以幻灯片要点为主；排障 Case 1-15 为分步操作实例。

- id: c01
  title: 配置演示：创建 Employee SSID 与账户并验证连接
  type: case
  source_chapter: "p72-73"
  source_quote: |
    "CREATION OF AN EMPLOYEE SSID & ACCOUNT. CONNECTION TO THE EMPLOYEE SSID."
  summary: |
    教材 SSID 章的标准演示一：在 AP Web 界面上创建员工 SSID 与对应账户（截图步骤），随后用终端连接该 Employee SSID 验证配置生效。文字内容仅两页标题，操作细节在截图中；可复用的骨架是"建 SSID → 建账户 → 终端实连验证"三段式，员工网通常配 802.1X/WPA2 加密与每 SSID ACL（见 p41 能力清单）。

  tags: [ssid, employee, config-demo, verification]

- id: c02
  title: 配置演示：创建 Guest SSID 并验证连接
  type: case
  source_chapter: "p74-75"
  source_quote: |
    "CREATION OF A GUEST SSID & ACCOUNT. CONNECTION TO THE GUEST SSID."
  summary: |
    标准演示二：创建访客 SSID 与访客账户，再连接验证。访客路径与内置 Captive Portal（p93）联动：客户端关联 Guest SSID 后被重定向到门户页认证。演示骨架同 c01（建 SSID → 建账户 → 验证），区别在开放加密 + Portal 认证组合。排障时结合 Case 6（Portal 不弹页）与 Case 9（Portal 认证失败）排查。

  tags: [ssid, guest, captive-portal, config-demo]

- id: c03
  title: 配置实例：跨街楼宇 WiFi Bridge 点对点回程
  type: case
  source_chapter: "p112-113"
  source_quote: |
    "USE CASE: Buildings separated by a street, LAN EXTENSION NOT POSSIBLE. WIFI BRIDGE. SSID: STELLAR-BRIDGE. BAND: 5 GHZ. IS ROOT: YES. PASSPHRASE: ALCATEL123! [对端] SSID: STELLAR-BRIDGE. BAND: 5 GHZ. IS ROOT: NO. PASSPHRASE: ALCATEL123!"
  summary: |
    教材给出的完整 Bridge 配置实例。场景：两栋楼隔着一条街，无法铺线，用无线桥延伸 LAN。两端参数对照：根端 SSID=STELLAR-BRIDGE、Band=5GHz、Is Root=Yes、Passphrase=ALCATEL123!；非根端同 SSID、同频段、同密码、Is Root=No。演示了"三同一根"原则（p07）的落地写法，可直接照抄到实际项目再改密码。

  tags: [bridge, config-example, root-ap, lan-extension]

- id: c04
  title: 配置实例：营地覆盖 WiFi Mesh（回程+访客双 SSID）
  type: case
  source_chapter: "p112, p114"
  source_quote: |
    "USE CASE: Coverage of a camping. SSID: WIFI GUESTS, BAND: 2.4 GHZ & 5 GHZ, SECURITY: OPEN. SSID: STELLAR-MESH, BAND: 5 GHZ, IS ROOT: YES, PASSPHRASE: ALCATEL123! [Mesh 节点] SSID: WIFI GUESTS, BAND: 2.4 GHZ & 5 GHZ, SECURITY: OPEN. SSID: STELLAR-MESH, BAND: 5 GHZ, IS ROOT: NO, PASSPHRASE: ALCATEL123!"
  summary: |
    Mesh 完整实例：场景为露营地整场覆盖。根节点与 Mesh 节点各自同时广播业务 SSID "WIFI GUESTS"（2.4+5GHz 双频、开放加密、走 Portal），并通过 SSID "STELLAR-MESH"（5GHz、加密、根端 Is Root=Yes）建立回程。展示了 Mesh 区别于 Bridge 的核心能力——回程与客户端服务并存（p08），以及业务/回程 SSID 分离的规划手法。

  tags: [mesh, camping, guest-wifi, backhaul, config-example]

- id: c05
  title: 部署场景：Auto Mesh 通电即入网
  type: case
  source_chapter: "p115"
  source_quote: |
    "AUTO MESH. Aim: quick & easy deployment of a Mesh topology. If a Stellar AP is: Not connected to the LAN. It will Have MESH enabled as non-root. Broadcast an hidden SSID « Stellar-MESH ». Band: 5 GHz."
  summary: |
    Auto Mesh 快速部署场景：现场只配置一台接 LAN 的 AP 为 Mesh root，它自动广播隐藏 SSID "Stellar-MESH"（5GHz）；其余 AP 不接线、摆到需要覆盖的位置直接通电，即自动以非根身份入网。适合弱电条件差、需要快速拉开覆盖的仓库/营地类项目。回程遵循最佳实践 5GHz/信道>100（p09）。

  tags: [auto-mesh, rapid-deployment, non-root, stellar-mesh]

- id: c06
  title: 排障案例 1：AP 无法上电（LED 判读法）
  type: case
  source_chapter: "p128"
  source_quote: |
    "AP can't be powered up. When the AP is powered up, the AP LED is 'Green'. However, if the LED is off or LED has a different color, please perform the following troubleshooting. Step 1: If LED is off, please check POE or adapter power output. Maximum (worst-case) power consumption: 12 W (802.3at PoE or DC). When both power sources are available, DC power takes priority."
  summary: |
    AP 点不亮的两步排障：第一步 LED 全灭——查 PoE 或电源适配器输出，基准是最大功耗 12W（802.3at PoE 或 DC）、DC 额定 48V、双电源并存时 DC 优先（p12）；第二步 LED 非绿色——按 LED 状态表（p13）判读：蓝常亮=已上电、绿常亮=加载系统、闪=网络异常或未建 SSID、红蓝交替=升级中、三灯交替=定位模式。先分清"没电"还是"有电但状态异常"再动手。

  tags: [power, led, case-1, troubleshooting]

- id: c07
  title: 排障案例 2：AP 从 DHCP 拿不到 IP（三步递进）
  type: case
  source_chapter: "p129-132"
  source_quote: |
    "Step 1: Connect to the AP, using the web GUI with the default IP address 192.168.1.254. Step 2: If you can't access the AP using the web GUI, access the AP using the console. Baud Rate: 115200. Check the IP mode of the AP ('option proto') using the command 'cat/etc/config/network'. Step 3: use 'ssudo tcpdump –i br-wan –s0 –w X.pcap' commands to capture the DHCP messages."
  summary: |
    DHCP 失联的三步递进救援：Step1 用默认 IP 192.168.1.254 直连 Web（PC 配同网段），确认 IP 模式为 DHCP；Step2 Web 进不去就走 Console（115200-8-N-1），cat /etc/config/network 查 option proto——若是 static，用 ifconfig br-wan 拿到现地址登 Web 改回 DHCP；Step3 仍不行则 cd /tmp 后 tcpdump 抓 DHCP 报文存 X.pcap，tftp 上送后用 Wireshark 分析：正常应见完整 Discover-Offer-Request-ACK 四步交互，报文残缺则查 DHCP 服务器配置与链路。

  tags: [dhcp, case-2, default-ip, console, tcpdump]

- id: c08
  title: 排障案例 4：AP 无法加入集群（四查）
  type: case
  source_chapter: "p136-138"
  source_quote: |
    "Check that the cluster ID value is similar on the AP and on the PVM. Use the command 'cluster_mgt –x show=self' to check the cluster ID. Check that the AP's IP address and PVC's IP address are in the same subnet. If the AP is in 'joining' state, it must be joined manually. Check if the cluster has already reached the maximum number of APs allowed (32/64/255 APs depending on the AP models)."
  summary: |
    入组失败按序四查：（1）Group/Cluster ID 是否与 PVM 一致——Console 用 cluster_mgt -x show=self 核对，不一致在 Web 上改；（2）AP 与 PVM 是否同网段，并用 tcpdump 抓 32767 端口验证 PVM 报文可达，长时间停留 Initializing 就重启 AP；（3）AP 停在 joining 状态需在 PVM 的 Web 界面手工批准加入；（4）核对集群是否已达该型号组合允许的上限（32/64/255，见 p04），并抓 32768 端口确认 AP 有没有向 PVM 发消息，无消息则重启 AP。

  tags: [cluster-join, case-4, cluster-id, 32767, manual-join]

- id: c09
  title: 排障案例 5：802.1X 认证失败（用户/AP/服务器三侧排查）
  type: case
  source_chapter: "p140-141"
  source_quote: |
    "User Side: Whether the username and password are correct. Make sure the terminals match the RADIUS Server authentication type. AP Side: Check the WLAN's configuration. Whether it is reachable between AP and RADIUS Server using 'tools-ping' on the web page. Server Side: Check the RADIUS Server Client configuration, such as the shared key, RADIUS client IP or IP range, authentication port, certificate."
  summary: |
    802.1X 失败按三侧排查：用户侧——账号密码、终端无线安全类型/证书等配置、终端与 RADIUS 认证类型匹配；AP 侧——核对 WLAN 配置，用 Web 界面的 tools-ping 验证 AP 到 RADIUS 服务器的连通性，必要时 tcpdump 抓发往 RadiusIP 的报文看认证交互细节；服务器侧——核对 RADIUS 的客户端配置（共享密钥、RADIUS client IP/网段、认证端口、证书），仍失败就在服务器侧抓包。要点是先把三方各自排干净再对报文。

  tags: [802-1x, radius, case-5, three-sided, tools-ping]

- id: c10
  title: 排障案例 6：连上 Guest SSID 后 Portal 页面不弹出
  type: case
  source_chapter: "p142-143"
  source_quote: |
    "If guest portal cannot pop up after connecting to the 'Guest' SSID (open & portal), check the following: Whether the Captive Portal function in the WLAN is enabled. Whether the Captive Portal authentication switch is turned on. Check if the client MAC address is in the white list or if the client IP is in the walled garden list. Check if the client enters https URL. If so, enter a http URL."
  summary: |
    Portal 不弹页的四查：（1）该 WLAN 是否启用了 Captive Portal 功能；（2）Portal 认证开关是否打开；（3）客户端是否命中白名单（MAC）或 walled garden（IP）——命中即不重定向，属预期行为；（4）客户端访问的是否为 https URL——内置 Portal 尚不支持 https 重定向，改输 http URL 即可。四查过后仍不弹，用 Console 执行 ps | grep eag 确认 EAG 进程（门户重定向模块）是否存活。

  tags: [captive-portal, redirection, case-6, eag, walled-garden]

- id: c11
  title: 排障案例 7：客户端拿不到 IP（抓包定位 VLAN 与信道错配）
  type: case
  source_chapter: "p144-147"
  source_quote: |
    "Capture the DHCP messages from the AP and client. If the DHCP messages of the client are incomplete and if the wireshark trace shows the same DHCP message repeated multiple times: Check that the VLAN ID of the WLAN is correct. If the client sends DHCP messages, but the AP can't receive the DHCP messages, capture the beacon frame on air and check if the channel in the beacon frame is the same than the one configured."
  summary: |
    客户端拿不到 IP 的定位法：在 AP 上 tcpdump 抓 DHCP 报文送 tftp 后用 Wireshark 看。三类结论：（1）同一报文反复重发、交互不完整——多半是 WLAN 的 VLAN ID 配错，上 Web 核对并修正 VLAN；（2）客户端根本没发 DHCP——查终端是否用 DHCP、有无静态 IP 残留；（3）客户端发了但 AP 收不到——空中抓 beacon 帧，比对信标里的信道与 AP 配置信道是否一致，不一致改信道配置。这条案例把"终端-空口-VLAN"三层故障用一份抓包切开。

  tags: [client-dhcp, case-7, vlan-id, beacon, channel-mismatch]

- id: c12
  title: 排障案例 8：客户端连不上 AP/集群（黑名单与 MaxClients）
  type: case
  source_chapter: "p148-150"
  source_quote: |
    "Check the password. Access the AP using the web GUI and check if the AP is in the blocklist. If the client is in the blocklist, click the red cross to delete the AP from the blocklist. Check if the clients count reached the maximum number of clients allowed. If the limit is already reached, modify the 'MaxClients' parameter. Use the command 'ps | grep wam' to check if the wam process of the ath port exists."
  summary: |
    客户端连不上的递进排查：先核密码；再查客户端是否被拉进 blocklist（黑名单），在 Web 上点红叉移除；接着看在线客户端数是否顶到 MaxClients 上限，顶到就调大该参数；然后清掉终端网卡里保存的 WLAN 记录重连；最后上 Console 用 ps | grep wam 检查客户端所在 ath 端口的 wam 进程是否存在，缺失就用 wam -P /var/run/wifi-athXX.pid -B /var/run/wam-athXX.conf 重建；仍不行用 cat /proc/kes_syslog | grep <clientMAC> 跟踪连接过程。

  tags: [blocklist, maxclients, case-8, wam-process, connection]

- id: c13
  title: 排障案例 11：低吞吐/高时延五查与案例 12 端口错误
  type: case
  source_chapter: "p155-156"
  source_quote: |
    "Low throughput/latency: Is there a speed limit in the WLAN configuration. Check the wireless mode that the client supports and the negotiation speed. Is the ACS function enabled? If not, enable it. Is there too much interference in the air? If so, change to another channel. Check the bandwidth with your ISP. AP port errors: Check if the connected cable is good and stable. Check the eth0 port configuration by using the command 'ethtool eth0'."
  summary: |
    性能类两案合参。低吞吐/时延（Case 11）按五查清单走：WLAN 限速→客户端模式与协商速率→ACS 开关→空中干扰换信道→ISP 带宽（详见 p21）。AP 端口报错（Case 12）三板斧：查线缆质量与稳定性（不稳就换）、ifconfig br-wan 确认有 IP 并可达、ethtool eth0 查端口协商配置。两案共同点是先排除配置侧限速/协商，再怀疑物理层。

  tags: [low-throughput, case-11, port-errors, case-12, ethtool]

- id: c14
  title: 勘测实例：五点标注的现场整改（AP1511 部署）
  type: case
  source_chapter: "p173-174"
  source_quote: |
    "Identify Access Point model: same as original design? Stellar AP1511 As originally planned. 1 No Adjacent / Co-channel Interference. 2 No coverage, AP missing. 3 Obstructed areas. 4 Default transmit power (17dBm), Increase for best coverage. 5 Move AP to optimize RF coverage."
  summary: |
    现场观测的落地实例：在 Ekahau 热图上对一处 AP1511 部署标出五个发现与动作——（1）该区域无邻频/同频干扰，正常；（2）存在无覆盖区，原因是 AP 缺失，需补点；（3）有遮挡区，需挪位；（4）发射功率停在默认 17dBm，为覆盖可上调；（5）把 AP 挪到更优位置优化覆盖。演示了 Step 2 观测五问如何转成 Step 3 的具体纠正动作（对照 f08 流程与 p22 措施集）。

  tags: [survey-example, ekahau, heatmap, ap1511, corrective-actions]
