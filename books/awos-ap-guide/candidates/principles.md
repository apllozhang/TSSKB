# 原则/规则/参数常数 · OmniAccess Stellar AP User Guide (AWOS 5.0.3)

> 来源：source/fulltext.md（页码即手册 PDF 页码）

- id: p01
  title: AP 集群容量上限与组网前提
  type: principle
  source_chapter: "p13"
  source_quote: |
    The ALE WLAN solution is based on a cluster architecture. A maximum of 255 APs are supported in one AP cluster/group. All APs have the same cluster ID that uniquely defines the AP group and all APs have to be in the same VLAN because the communication between group members is based on multicast.
  summary: |
    一个 AP 集群/组最多 255 台 AP；所有 AP 必须使用相同 cluster ID（组 ID）且处于同一 VLAN，因为组成员间通信基于组播。PVM 负责配置同步、统计、固件升级，SVM 作为 PVM 备份。
  tags: [ap-group, capacity, multicast, vlan]

- id: p02
  title: 预置 SSID mywifi-xxxx 与默认管理 URL
  type: principle
  source_chapter: "p13"
  source_quote: |
    By default, the AP group will advertise the pre-defined SSID 'mywifi-xxxx' and you can connect to 'mywifi-xxxx' to browse the AP group GUI through http://mywifi.al-enterprise.com:8080 to the initializing wizard. After you complete Using the Initializing Wizard, the SSID 'mywifi-xxxx' will be deleted.
  summary: |
    默认广播预置 SSID "mywifi-xxxx"（xxxx 为 PVM MAC 地址最后两个字节），连接后用 http://mywifi.al-enterprise.com:8080 打开初始化向导；向导完成后该 SSID 自动删除。无 DNS 时可直接用任意 AP 的 IP 访问 http://a.b.c.d:8080；HTTPS 访问地址为 https://mywifi.al-enterprise.com（无需端口）。
  tags: [default, ssid, url, port-8080]

- id: p03
  title: 无 DHCP 时的默认 IP 与开局终端配置
  type: principle
  source_chapter: "p14, p87"
  source_quote: |
    If there is no DHCP server in the network, the AP will default to the 192.168.1.254 address. ... Connect the Stellar AP (default IP address is 192.168.1.254) to your configuring terminal directly with an Ethernet cable. ... IP Address - 192.168.1.100; Subnet Mask - 255.255.255.0; Default Gateway - 192.168.1.254
  summary: |
    网络中无 DHCP 服务器时 AP 默认 IP 为 192.168.1.254。单台配置：笔记本直连 AP，配静态 IP 如 192.168.1.100/255.255.255.0、网关 192.168.1.254、DNS 指向 192.168.1.254，然后访问 http://192.168.1.254:8080。
  tags: [default, ip, dhcp, 192.168.1.254]

- id: p04
  title: PVM/SVM 选举规则与容量分级
  type: principle
  source_chapter: "p18"
  source_quote: |
    PVM/SVM election priority: AP1451>AP1351>AP1431/AP1331>AP1521>AP1320/AP1360>AP1511/AP1411>AP1311/AP1301>AP1301H>AP1220/AP1230/AP1251/AP1201>... Among the APs with same priority, the one with highest MAC address will be selected as PVM.
  summary: |
    PVM 按机型优先级选举（AP1451>AP1351>AP1431/AP1331>AP1521>AP1320/AP1360>AP1511/AP1411>AP1311/AP1301>AP1301H>AP1220/AP1230/AP1251/AP1201>AP1101/AP1201H/AP1201L/AP1201HL>AP1311BG>AP1201BG）；同优先级中 MAC 最高者为 PVM、次高为 SVM。AP1101/AP1201H/AP1201L/AP1201HL 当 PVM 时集群只能到 32 台，其余机型可到 255 台。
  tags: [pvm, svm, election, capacity]

- id: p05
  title: 大规模部署的弹性冗余配比（每 64 台 / 255 台）
  type: principle
  source_chapter: "p18"
  source_quote: |
    Recommend in network segments of every 64 APs there are at least 4x APs of either AP1220 series, AP1230 series, AP1251, AP1320 series, AP1360 series, AP1311, AP1351, AP1451, AP1431, AP1411, AP1521, AP1511. ... to scale even further for 255 APs you will need at least 16 AP12XX ... or 16 AP13XX ... or 16 AP14XX ... or 16 AP15xx.
  summary: |
    弹性部署建议：每 64 台 AP 网段中至少有 4 台中高端机型（AP12XX/AP13XX/AP14XX/AP15XX 系列）；要扩展到 255 台，则集群内至少需要 16 台同一档（AP12XX 或 AP13XX 或 AP14XX 或 AP15XX）的 AP。更高优先级 AP 加入已有组会自动接管 PVM 角色。
  tags: [pvm, resiliency, scale, 64, 255]

- id: p06
  title: GUI 并发连接数与推荐浏览器
  type: principle
  source_chapter: "p8, p13"
  source_quote: |
    Each Stellar AP supports up to three simultaneous GUI connections. ... Recommended OS: Window 10, Window 11, MAC OS X 10-13. Recommended Browser: Google Chrome 102 and later, Mozilla Firefox 100 and later, Microsoft Edge 92 and later.
  summary: |
    每台 AP 最多支持 3 个并发 GUI 连接。推荐环境：Windows 10/11、macOS 10-13；浏览器 Chrome 102+、Firefox 100+、Edge 92+。
  tags: [gui, limit, browser]

- id: p07
  title: 组管理 IP（GMIP）与默认组参数
  type: principle
  source_chapter: "p31-32"
  source_quote: |
    Group Management IP - A virtual IP address for AP group management, default is 10.0.0.1 ... Group ID - Identification of the AP group, default is 100. ... you can manage the AP group via accessing the URL: http://GMIP:8080 by wired or wireless.
  summary: |
    组管理 IP（GMIP）默认 10.0.0.1，组 ID 默认 100。GMIP 是配置在 PVM 上的静态虚拟 IP，用于绕开 AP 动态 IP 变动问题，通过 http://GMIP:8080 有线/无线管理整组；建议从 AP 组网段选一个空闲 IP 做 GMIP，且必须保证从配置终端可路由。
  tags: [gmip, default, pvm, management]

- id: p08
  title: Web 账户体系与默认锁定策略
  type: principle
  source_chapter: "p32-33"
  source_quote: |
    There are three accounts can login to the Web GUI with different privileges: Administrator, Viewer, and GuestOperator. ... By default, only the Administrator account is enabled. ... By default, the lockout threshold is 3 times of invalid login attempts. ... the lockout duration is 1 minute.
  summary: |
    Web GUI 三账户：Administrator（全权）、Viewer（只读监控）、GuestOperator（仅编辑来宾 Portal 用户）；默认只有 Administrator 启用。账户锁定默认 3 次失败登录触发、锁定 1 分钟。CLI 账户为 support 和 root，root 密码仅由客户持有、由 AP 生成真实 root 凭据。
  tags: [account, security, lockout, default]

- id: p09
  title: NTP 同步周期与 Syslog 默认级别、日志容量
  type: principle
  source_chapter: "p35-37"
  source_quote: |
    If configured, APs in the group synchronize the time with NTP sever in 15-minute intervals. ... Notice is the default level of Syslog setting ... For one AP, up to 1MB size of syslog messages can be saved in the local log file. The log file is FIFO.
  summary: |
    配置后组内 AP 每 15 分钟与 NTP 服务器同步一次时间。Syslog 默认级别 Notice（0-7 八级：0 Emergency 到 7 Debug，指定级别会包含所有更低级别）；单 AP 本地日志文件上限 1MB，FIFO 滚动覆盖。SNMPv3 认证算法固定 sha、加密固定 aes128。
  tags: [ntp, syslog, snmp, 15-min, 1mb]

- id: p10
  title: RDA（ACS/APC）默认开启与手动模式的代价
  type: principle
  source_chapter: "p40-41, p83"
  source_quote: |
    By default, the working channel and transmitting power are automatically managed by Radio Dynamic Adjustment™ (RDA) technology. ... If you want to set the channel and power values for an AP manually, you need to disable the ACS/APC function on the AP. ... In manual mode the AP transmit power can be adjusted in 1 dB increments.
  summary: |
    工作信道和发射功率默认由 RDA（含 ACS 自动选信道 + APC 自动功率控制）管理，默认开启。要手动指定信道/功率必须先关闭该 AP 的 ACS/APC；手动模式功率按 1 dB 步进调整，且两个射频频段都必须分别设置。RDA 依赖后台扫描（Background Scanning）保持开启才有效。
  tags: [rda, acs, apc, rf, default]

- id: p11
  title: 160MHz 信道宽度限制
  type: principle
  source_chapter: "p41"
  source_quote: |
    Wi-Fi 6E Access Point AP1451/AP1431/AP1411 support 160MHz channels; Wi-Fi 6 Access Points AP132X, AP136X and AP1351 support 160MHz channels; Wi-Fi 6 Access Points AP1311/AP1301 do not support 160MHz channels. 160MHz channel width is supported on 5G band or 6G band. Only static 160MHz channel width is supported, Auto Channel Selection will not use 160MHz channels.
  summary: |
    160MHz 信道仅支持 5G/6G 频段，且只能静态配置——ACS 自动选信道不会使用 160MHz。支持机型：Wi-Fi 6E 的 AP1451/AP1431/AP1411、Wi-Fi 6 的 AP132X/AP136X/AP1351；AP1311/AP1301 不支持。另外 AP1411 为三频机型，射频可配 2.4+5G（默认）、2.4+6G、5+6G 三种组合。
  tags: [160mhz, channel-width, wifi6e, ap1411]

- id: p12
  title: Beacon/CSA/Short GI/DTIM/UAPSD 默认参数
  type: principle
  source_chapter: "p42, p64-65"
  source_quote: |
    Beacon Interval: You can specify a value within the range of 60-500. The default value is 100 milliseconds. CSA ... the packet count range is 1~10. ... The default value is 1, which means the client checks for buffered data on the AP at every beacon.
  summary: |
    Beacon 间隔范围 60-500ms，默认 100ms。CSA（信道切换通告）默认启用，报文计数范围 1-10。Short GI 默认启用（400ns 短保护间隔约提升 11% 速率，多径严重时建议关闭）。DTIM 间隔默认 1。UAPSD 默认启用（802.11e 省电特性）。
  tags: [beacon, csa, short-gi, dtim, uapsd, default]

- id: p13
  title: 后台扫描默认值与间隔上限
  type: principle
  source_chapter: "p46"
  source_quote: |
    The scanning interval of Background Scanning can be configured from 5 seconds to 3 hours (180 minutes) according to deployment requirement. For highly sensitive packet delay use case, it is recommended to prolong the interval from default 20-second setting.
  summary: |
    后台扫描默认开启，默认间隔 20 秒，可配置 5 秒到 3 小时（180 分钟）。对时延敏感场景可只扫工作信道或加大间隔；但间隔超过 1 分钟会影响 RDA 与 wIPS 的精度（见陷阱条目）。后台扫描是 wIDS/wIPS 和 RDA 的基础。
  tags: [background-scanning, default, 20s]

- id: p14
  title: Band Steering / Load Balance / RSSI 阈值默认与推荐值
  type: principle
  source_chapter: "p46-47"
  source_quote: |
    By default, band steering is enabled. ... The thresholds for client density is 10, channel utilization is 70% for 2.4G and 70% for 5G. By default, Load Balance is enabled. ... Recommended 2.4G (5), 5G (10), 6G (10). ... Recommended 2.4G (10), 5G (15), 6G (15).
  summary: |
    Band Steering 默认启用（Prefer 5G 模式，可选 Force 5G 强制双频终端上 5G）。Load Balance 默认启用，阈值：客户端密度 10、信道利用率 2.4G/5G 各 70%。RSSI Threshold 默认关闭（0），推荐 2.4G=5、5G=10、6G=10，适合高密场景；Roaming RSSI 默认关闭，推荐 2.4G=10、5G=15、6G=15，需配合 802.11k/v。Voice/Video Awareness 与 Airtime Fairness 默认关闭。
  tags: [band-steering, load-balance, rssi, default, recommended]

- id: p15
  title: 客户端健康度分级与监控刷新周期
  type: principle
  source_chapter: "p27-28"
  source_quote: |
    Best - Number of clients whose signal strength is more than 30. Good - Number of clients whose signal strength is between 15 ~30. Fair - Number of clients whose signal strength is less than 15. ... The monitoring window is automatically refreshed every 30 seconds by default, and the data polling cycle can be set to 30s /60s /120s.
  summary: |
    Client Health 按信号强度分三档：Best > 30、Good 15~30、Fair < 15。监控窗口默认 30 秒自动刷新，轮询周期可设 30s/60s/120s。客户端漫游历史最多显示 32 条记录。
  tags: [client-health, monitoring, 30s]

- id: p16
  title: WLAN 安全等级与 PSK 密码格式
  type: principle
  source_chapter: "p59"
  source_quote: |
    Enterprise: Also referred to as 802.1X mode ... requires a RADIUS authentication server. Personal: Also referred to as PSK (pre-shared key) mode ... Each wireless network device encrypts the network traffic using a 256 bit key. This key may be entered either as a string of 64 hexadecimal digits, or as a passphrase of 8 to 63 printable ASCII characters.
  summary: |
    WLAN 安全等级从高到低：Enterprise（802.1X，需 RADIUS）> Personal（PSK）> Open。Personal 模式使用 256 位密钥，可输入 64 位十六进制字符串或 8-63 个可打印 ASCII 字符的口令。Static-WEP 仅建议用于 802.11b 老客户端（最多 4 个 WEP 密钥，每个 10 或 26 位十六进制字符）。
  tags: [wlan, security-level, psk, wep]

- id: p17
  title: RADIUS 端口默认值与 RadSec 端口
  type: principle
  source_chapter: "p62-63"
  source_quote: |
    AuthPort - Communication port of the authentication server. The default value is 1812. If RadSec is enabled, the AuthPort should be configured 2083 or the value mapping RadSec server. ... AcctPort - Communication port of the accounting server. The default value is 1813.
  summary: |
    认证端口 AuthPort 默认 1812，计费端口 AcctPort 默认 1813；启用 RadSec（TLS）后 AuthPort 应改为 2083 或映射 RadSec 服务器的值。RadSec 仅适用于无线客户端，且只支持主 RADIUS 服务器。动态 VLAN（RFC-2868）支持三个属性：Tunnel-Type (#64)=VLAN、Tunnel-Medium-Type (#65)=802(6)、Tunnel-Private-Group-ID (#81)。
  tags: [radius, 1812, 1813, radsec, 2083]

- id: p18
  title: 空闲超时与每 BSSID 最大客户端数
  type: principle
  source_chapter: "p63"
  source_quote: |
    If Inactivity Timeout Status is disabled, the inactivity timeout interval is set to fixed 600 seconds. ... Configure the inactivity timeout period, with a valid range of 60 to 12000 seconds. ... Max Clients per band: You can specify a value within the range of 1 to 256. The default value is 64.
  summary: |
    空闲超时状态关闭时使用固定 600 秒；开启后可配置 60-12000 秒。每个 BSSID（每频段）最大客户端数范围 1-256，默认 64。组播转单播（基于 IGMP snooping）最多对 6 个客户端生效。6GHz 网络只支持 WPA3 与 Enhanced Open 加密。
  tags: [inactivity-timeout, max-clients, multicast, 6ghz]

- id: p19
  title: 客户端速率准入推荐值与管理帧速率例外
  type: principle
  source_chapter: "p64"
  source_quote: |
    2.4G band client with lower data speed will not be allowed to access, recommended value 12 ... 5G band client with lower data speed will not be allowed to access, recommended value 24 ... 2.4G Beacon frame does not support 9 Mbps or 18 Mbps speed. When 9/18 Mbps is configured for 2.4G MGMT Rate, beacon frame will broadcast on 11/24 Mbps rate.
  summary: |
    客户端速率准入推荐值：2.4G=12 Mbps、5G=24 Mbps、6G=24 Mbps，低于该速率的客户端拒绝接入。管理帧速率注意：2.4G Beacon 不支持 9/18 Mbps（配置后 Beacon 自动用 11/24 Mbps 发）；5G Beacon 不支持 9 Mbps（自动用 12 Mbps）。
  tags: [client-rate, recommended, beacon-rate]

- id: p20
  title: 整组一份配置文件原则
  type: principle
  source_chapter: "p77"
  source_quote: |
    All configuration settings (clear, backup or restore) will be applied to the entire group. There is no need to select specific APs to apply configuration settings. The entire group of APs have one configuration file.
  summary: |
    清除、备份、恢复配置均作用于整个 AP 组，无需选择具体 AP——整组只有一份配置文件。建议完成全部配置后立即导出备份。单 AP 固件升级约需 5 分钟。
  tags: [config, backup, group, firmware]

- id: p21
  title: 替换 AP 与扩组的三种方法
  type: principle
  source_chapter: "p86"
  source_quote: |
    To replace the current PVM: Upgrade the SVM to the PVM before disconnecting the old PVM. ... Method one: Divide the Stellar APs into different subnets ... Method two: Setup up different group IDs ... Method three: Deploy Stellar AP with ALE OmniVista and scale up to 4000 AP in one network.
  summary: |
    替换 PVM 前必须先把 SVM 升级为 PVM 再断开旧 PVM；替换 SVM/成员可直接换，不影响其他 AP 用户。超过单组规格时三种扩组法：按交换机端口默认 VLAN 划分不同子网；每组配置不同 group ID；或用 OmniVista 管理可单网扩展到 4000 台 AP。新增 AP 前确保 PVM 不处于 Down 状态。
  tags: [replace-ap, scale, group-id, omnivista, 4000]

- id: p22
  title: Out-of-box MESH 预置参数与不可逆条件
  type: principle
  source_chapter: "p103"
  source_quote: |
    By default, Stellar AP with factory configuration powered up without wired uplink will try to establish MESH link automatically with build-in configuration (MESH SSID [Stellar-MESH] and password on 2.4G band). The out-of-box will be permanently disabled once the AP ever connected to wired uplink.
  summary: |
    出厂配置的 AP 无线上电（无有线 uplink）会自动用内置 SSID "Stellar-MESH"（2.4G 频段）建立 MESH 链路，管理员只需指定根节点。AP 一旦连接过有线 uplink，Out-of-box MESH 被永久禁用，只有恢复出厂才能找回。Mesh 链路从根到叶必须同频段；组播速率默认 24 Mbps。
  tags: [mesh, stellar-mesh, out-of-box, 2.4g]

- id: p23
  title: AP 侧 DHCP 服务器与租约默认值
  type: principle
  source_chapter: "p107"
  source_quote: |
    Lease Time - Period of time that the IP address allocated can be used by the device. By default, lease time is 24 hours. ... Only Network with static IP (as gateway) can be bound to a DHCP pool.
  summary: |
    同一 L2 域内的 AP 组可在某台 AP 上开 DHCP 服务器（AP UI -> Service -> DHCP）。租约时间默认 24 小时；DHCP 池只能绑定配了静态 IP（作为网关）的 Network，且 VLAN 必须先映射到某 SSID 才会显示在可选列表中。
  tags: [dhcp, lease, 24h, ap-ui]

- id: p24
  title: 扫描模式两种类型与机型差异
  type: principle
  source_chapter: "p110"
  source_quote: |
    One Time - The scanning mode will last for 5 minutes duration and then return to normal AP mode ... Always - The scanning mode is always active and wireless client is not allowed to associate if the AP is powered on.
  summary: |
    AP 扫描模式分两种：One Time 持续 5 分钟后自动恢复正常模式；Always 模式下持续扫描、不允许客户端接入。查看 RF Environment 扫描数据必须让 AP 进入扫描模式。无扫描射频的机型进扫描模式会中断常规 Wi-Fi 服务（见陷阱条目）。
  tags: [scanning-mode, rf-environment, 5-min]

- id: p25
  title: Portal 用户库容量与行为日志周期
  type: principle
  source_chapter: "p50"
  source_quote: |
    Maximum 2000 accounts supported in AP local database for internal captive portal authentication. ... Specify the cycle for uploading user behavior logs to FTP server, can be set to 1 hour, 2 hours and 4 hours.
  summary: |
    内置 Portal 认证的 AP 本地用户数据库最多 2000 个账户（支持 Excel 模板导入）。用户行为日志（用户名/MAC/IP/WLAN/上下线/时间戳）可上传 TFTP/SFTP/Syslog 服务器，FTP 上传周期可设 1/2/4 小时。RADIUS Called-Station-ID 属性最长 64 字节。
  tags: [captive-portal, 2000, user-behavior-log]

- id: p26
  title: ACL 顺序匹配与默认放行
  type: principle
  source_chapter: "p55"
  source_quote: |
    The ACL rules created in the list are applied sequentially, based on the precedence of top-to-bottom. By default, traffic is allowed to pass if no ACL rules are matched (Default ACL action is 'Accept').
  summary: |
    ACL 规则自上而下顺序匹配；无规则命中时默认动作是 Accept（放行）。支持 L3 ACL（源/目的 IP + TCP/UDP/ICMP 端口 + 通配符），Apply To EthPort 仅适用于 AP1201H/AP1201HL/AP1311/AP1301H 下行口。L2 级 MAC 控制走 Blocklist/Allowlist，802.1p/DSCP 规则在建 SSID 的 QoS 里配。
  tags: [acl, default-accept, order]

- id: p27
  title: 双上行 LACP 与 PoE 供电模式差异
  type: principle
  source_chapter: "p14"
  source_quote: |
    AP1230 series, AP1311 and AP1301 support PoE Redundancy - AP will only accept PoE on one of the two uplinks ... AP1351, AP1331, AP1451 and AP1431 support dual uplink connection with PoE Sharing - AP will accept PoE from the two uplinks at the same time.
  summary: |
    AP1230 系列、AP1311、AP1301、AP1351、AP1331、AP1411、AP1431、AP1451 支持双上行并在启动时与上游交换机建立 LACP 链路聚合（AP1230 用于在 1G 交换机上实现 2GE 吞吐）。供电分两类：AP1230 系列/AP1311/AP1301 为 PoE 冗余（单口供电、主断备启）；AP1351/AP1331/AP1451/AP1431 为 PoE 共享（两口同时供电），其中 AP1351/AP1451 为 Class 7，要求交换机支持 IEEE 802.3bt 及 PoE 固件 3.XX。
  tags: [lacp, dual-uplink, poe, 802.3bt]

- id: p28
  title: HTTPS 管理端口与证书域名约束
  type: principle
  source_chapter: "p34, p113"
  source_quote: |
    User needs to use domain 'mywifi.al-enterprise.com' for your own certificate because the login URL cannot be changed. ... (1) HTTP protocol with URL http://AP-IP:8080 ... (2) HTTPS protocol with URL https://AP-IP or https://mywifi.al-enterprise.com.
  summary: |
    两种登录方式：HTTP 用 8080 端口（http://AP-IP:8080），无需证书；HTTPS 用标准 443（https://AP-IP），需先从 AP 下载根证书 "ALE-OmniAccess-WLAN.CRT" 装入浏览器信任库。内置 Web 服务器证书必须使用域名 mywifi.al-enterprise.com（登录 URL 不可改），可用 OpenSSL 自签替换。
  tags: [https, certificate, 8080, 443]
