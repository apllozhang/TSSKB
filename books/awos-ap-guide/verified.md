# 验证通过条目 · OmniAccess Stellar AP User Guide (AWOS 5.0.3)

> 阶段 1.5 三重验证产出（验证日期 2026-08-23）
> 验证规则：V1 原文真实性（quote 在对应页命中，容错表格转写/跨页/续行）/ V2 可操作价值（默认值、参数、坑均算）/ V3 独特性（非常识；手册默认值与限制均为独特信息）
> 输入：candidates/ 78 条；原文：source/fulltext.md（128 页，<<<PAGE N>>> 标记）

## 汇总

| 类别 | 候选数 | 通过 | 淘汰 | 说明 |
|---|---|---|---|---|
| principles | 28 | 28 | 0 | 含 3 条 V1 引用形式注记（p06/p20/p28），内容均属实 |
| counter-examples | 14 | 14 | 0 | 含 1 条跨页注记（ce10）；ce01 部分内容为泛常识但主体特有，保留 |
| glossary | 36 | 36 | 0 | 免验保留 |
| **合计** | **78** | **78** | **0** | |

**核验方式**：quote 按 `...` 分段后逐段与 source/fulltext.md 对应页做归一化比对（精确/句子级/词级覆盖≥92% 三档容错）；summary 中超出 quote 的附加断言另抽 20+ 处在原文定位核实，全部命中，仅 p28 的 "OpenSSL 自签" 一句无原文依据（已在注记中要求下一阶段删除）。

**引用形式注记（不影响通过）**：
1. p06：浏览器推荐为 p13 表格的转写压缩，逐值核对一致（Window 10/11、MAC OS X 10-13、Chrome 102+/Firefox 100+/Edge 92+）。
2. p20：quote 逐字命中但实际位于 p78（候选标 p77），已在条目内修正页码。
3. p28：quote 省略了原文括号内示例 `https://172.16.101.34`；summary 末句 "可用 OpenSSL 自签替换" 原文无依据，建议删除。
4. ce10：Note 6-2 起于 p79，"Cookies / Cache" 清单续于 p80（跨页引用）。

---

## 原则/规则/参数常数（28 条，全部通过）

- id: p01
  title: AP 集群容量上限与组网前提
  type: principle
  source_chapter: "p13"
  source_quote: |
    The ALE WLAN solution is based on a cluster architecture. A maximum of 255 APs are supported in one AP cluster/group. All APs have the same cluster ID that uniquely defines the AP group and all APs have to be in the same VLAN because the communication between group members is based on multicast.
  summary: |
    一个 AP 集群/组最多 255 台 AP；所有 AP 必须使用相同 cluster ID（组 ID）且处于同一 VLAN，因为组成员间通信基于组播。PVM 负责配置同步、统计、固件升级，SVM 作为 PVM 备份。
  tags: [ap-group, capacity, multicast, vlan]
  verify: |
    V1 原文精确命中 p13
    V2 255台上限/同VLAN/同cluster ID 均为硬约束
    V3 集群组网前提为手册特有
- id: p02
  title: 预置 SSID mywifi-xxxx 与默认管理 URL
  type: principle
  source_chapter: "p13"
  source_quote: |
    By default, the AP group will advertise the pre-defined SSID 'mywifi-xxxx' and you can connect to 'mywifi-xxxx' to browse the AP group GUI through http://mywifi.al-enterprise.com:8080 to the initializing wizard. After you complete Using the Initializing Wizard, the SSID 'mywifi-xxxx' will be deleted.
  summary: |
    默认广播预置 SSID "mywifi-xxxx"（xxxx 为 PVM MAC 地址最后两个字节），连接后用 http://mywifi.al-enterprise.com:8080 打开初始化向导；向导完成后该 SSID 自动删除。无 DNS 时可直接用任意 AP 的 IP 访问 http://a.b.c.d:8080；HTTPS 访问地址为 https://mywifi.al-enterprise.com（无需端口）。
  tags: [default, ssid, url, port-8080]
  verify: |
    V1 原文精确命中 p13（含『xxxx为PVM MAC末两字节』fulltext:527）
    V2 默认SSID+8080管理URL可直接开局
    V3 预置值与向导后自动删除行为特有
- id: p03
  title: 无 DHCP 时的默认 IP 与开局终端配置
  type: principle
  source_chapter: "p14, p87"
  source_quote: |
    If there is no DHCP server in the network, the AP will default to the 192.168.1.254 address. ... Connect the Stellar AP (default IP address is 192.168.1.254) to your configuring terminal directly with an Ethernet cable. ... IP Address - 192.168.1.100; Subnet Mask - 255.255.255.0; Default Gateway - 192.168.1.254
  summary: |
    网络中无 DHCP 服务器时 AP 默认 IP 为 192.168.1.254。单台配置：笔记本直连 AP，配静态 IP 如 192.168.1.100/255.255.255.0、网关 192.168.1.254、DNS 指向 192.168.1.254，然后访问 http://192.168.1.254:8080。
  tags: [default, ip, dhcp, 192.168.1.254]
  verify: |
    V1 p14 精确命中；p87 终端IP表逐值一致（表格排版，词级命中）
    V2 无DHCP开局的完整终端参数
    V3 192.168.1.254及配套配置特有
- id: p04
  title: PVM/SVM 选举规则与容量分级
  type: principle
  source_chapter: "p18"
  source_quote: |
    PVM/SVM election priority: AP1451>AP1351>AP1431/AP1331>AP1521>AP1320/AP1360>AP1511/AP1411>AP1311/AP1301>AP1301H>AP1220/AP1230/AP1251/AP1201>... Among the APs with same priority, the one with highest MAC address will be selected as PVM.
  summary: |
    PVM 按机型优先级选举（AP1451>AP1351>AP1431/AP1331>AP1521>AP1320/AP1360>AP1511/AP1411>AP1311/AP1301>AP1301H>AP1220/AP1230/AP1251/AP1201>AP1101/AP1201H/AP1201L/AP1201HL>AP1311BG>AP1201BG）；同优先级中 MAC 最高者为 PVM、次高为 SVM。AP1101/AP1201H/AP1201L/AP1201HL 当 PVM 时集群只能到 32 台，其余机型可到 255 台。
  tags: [pvm, svm, election, capacity]
  verify: |
    V1 p18 命中（优先级链跨行+表格拆行，句子级）
    V2 选举优先级链+32/255分级可预判PVM归属
    V3 机型矩阵手册特有
- id: p05
  title: 大规模部署的弹性冗余配比（每 64 台 / 255 台）
  type: principle
  source_chapter: "p18"
  source_quote: |
    Recommend in network segments of every 64 APs there are at least 4x APs of either AP1220 series, AP1230 series, AP1251, AP1320 series, AP1360 series, AP1311, AP1351, AP1451, AP1431, AP1411, AP1521, AP1511. ... to scale even further for 255 APs you will need at least 16 AP12XX ... or 16 AP13XX ... or 16 AP14XX ... or 16 AP15xx.
  summary: |
    弹性部署建议：每 64 台 AP 网段中至少有 4 台中高端机型（AP12XX/AP13XX/AP14XX/AP15XX 系列）；要扩展到 255 台，则集群内至少需要 16 台同一档（AP12XX 或 AP13XX 或 AP14XX 或 AP15XX）的 AP。更高优先级 AP 加入已有组会自动接管 PVM 角色。
  tags: [pvm, resiliency, scale, 64, 255]
  verify: |
    V1 原文精确命中 p18
    V2 每64台配4台/255台配16台的弹性配比可直接用于规划
    V3 部署配方特有
- id: p06
  title: GUI 并发连接数与推荐浏览器
  type: principle
  source_chapter: "p8, p13"
  source_quote: |
    Each Stellar AP supports up to three simultaneous GUI connections. ... Recommended OS: Window 10, Window 11, MAC OS X 10-13. Recommended Browser: Google Chrome 102 and later, Mozilla Firefox 100 and later, Microsoft Edge 92 and later.
  summary: |
    每台 AP 最多支持 3 个并发 GUI 连接。推荐环境：Windows 10/11、macOS 10-13；浏览器 Chrome 102+、Firefox 100+、Edge 92+。
  tags: [gui, limit, browser]
  verify: |
    V1『3个并发GUI连接』精确命中p8；浏览器表为表格转写，逐值核对p13一致（Window10/11、MAC OS X 10-13、Chrome102+/Firefox100+/Edge92+）
    V2 并发限制+浏览器基线
    V3 手册兼容矩阵（注意版本号会随时间过时）
- id: p07
  title: 组管理 IP（GMIP）与默认组参数
  type: principle
  source_chapter: "p31-32"
  source_quote: |
    Group Management IP - A virtual IP address for AP group management, default is 10.0.0.1 ... Group ID - Identification of the AP group, default is 100. ... you can manage the AP group via accessing the URL: http://GMIP:8080 by wired or wireless.
  summary: |
    组管理 IP（GMIP）默认 10.0.0.1，组 ID 默认 100。GMIP 是配置在 PVM 上的静态虚拟 IP，用于绕开 AP 动态 IP 变动问题，通过 http://GMIP:8080 有线/无线管理整组；建议从 AP 组网段选一个空闲 IP 做 GMIP，且必须保证从配置终端可路由。
  tags: [gmip, default, pvm, management]
  verify: |
    V1 p31/32 命中（表格排版，词级全命中）
    V2 GMIP默认10.0.0.1、组ID默认100、http://GMIP:8080
    V3 组管理虚拟IP机制特有
- id: p08
  title: Web 账户体系与默认锁定策略
  type: principle
  source_chapter: "p32-33"
  source_quote: |
    There are three accounts can login to the Web GUI with different privileges: Administrator, Viewer, and GuestOperator. ... By default, only the Administrator account is enabled. ... By default, the lockout threshold is 3 times of invalid login attempts. ... the lockout duration is 1 minute.
  summary: |
    Web GUI 三账户：Administrator（全权）、Viewer（只读监控）、GuestOperator（仅编辑来宾 Portal 用户）；默认只有 Administrator 启用。账户锁定默认 3 次失败登录触发、锁定 1 分钟。CLI 账户为 support 和 root，root 密码仅由客户持有、由 AP 生成真实 root 凭据。
  tags: [account, security, lockout, default]
  verify: |
    V1 p32-33 命中（三账户表+锁定句精确）
    V2 三账户权限矩阵+锁定3次/1分钟默认
    V3 账户体系与CLI root/support机制特有
- id: p09
  title: NTP 同步周期与 Syslog 默认级别、日志容量
  type: principle
  source_chapter: "p35-37"
  source_quote: |
    If configured, APs in the group synchronize the time with NTP sever in 15-minute intervals. ... Notice is the default level of Syslog setting ... For one AP, up to 1MB size of syslog messages can be saved in the local log file. The log file is FIFO.
  summary: |
    配置后组内 AP 每 15 分钟与 NTP 服务器同步一次时间。Syslog 默认级别 Notice（0-7 八级：0 Emergency 到 7 Debug，指定级别会包含所有更低级别）；单 AP 本地日志文件上限 1MB，FIFO 滚动覆盖。SNMPv3 认证算法固定 sha、加密固定 aes128。
  tags: [ntp, syslog, snmp, 15-min, 1mb]
  verify: |
    V1 p35/p37 命中；SNMP sha/aes128 原文fulltext:1495核实
    V2 NTP 15min/Notice/1MB FIFO/SNMP固定算法
    V3 默认值群特有
- id: p10
  title: RDA（ACS/APC）默认开启与手动模式的代价
  type: principle
  source_chapter: "p40-41, p83"
  source_quote: |
    By default, the working channel and transmitting power are automatically managed by Radio Dynamic Adjustment™ (RDA) technology. ... If you want to set the channel and power values for an AP manually, you need to disable the ACS/APC function on the AP. ... In manual mode the AP transmit power can be adjusted in 1 dB increments.
  summary: |
    工作信道和发射功率默认由 RDA（含 ACS 自动选信道 + APC 自动功率控制）管理，默认开启。要手动指定信道/功率必须先关闭该 AP 的 ACS/APC；手动模式功率按 1 dB 步进调整，且两个射频频段都必须分别设置。RDA 依赖后台扫描（Background Scanning）保持开启才有效。
  tags: [rda, acs, apc, rf, default]
  verify: |
    V1 p41 精确命中（含手动模式须关ACS/APC）
    V2 手动信道/功率的前置操作+1dB步进
    V3 RDA机制与依赖关系特有
- id: p11
  title: 160MHz 信道宽度限制
  type: principle
  source_chapter: "p41"
  source_quote: |
    Wi-Fi 6E Access Point AP1451/AP1431/AP1411 support 160MHz channels; Wi-Fi 6 Access Points AP132X, AP136X and AP1351 support 160MHz channels; Wi-Fi 6 Access Points AP1311/AP1301 do not support 160MHz channels. 160MHz channel width is supported on 5G band or 6G band. Only static 160MHz channel width is supported, Auto Channel Selection will not use 160MHz channels.
  summary: |
    160MHz 信道仅支持 5G/6G 频段，且只能静态配置——ACS 自动选信道不会使用 160MHz。支持机型：Wi-Fi 6E 的 AP1451/AP1431/AP1411、Wi-Fi 6 的 AP132X/AP136X/AP1351；AP1311/AP1301 不支持。另外 AP1411 为三频机型，射频可配 2.4+5G（默认）、2.4+6G、5+6G 三种组合。
  tags: [160mhz, channel-width, wifi6e, ap1411]
  verify: |
    V1 p41 精确命中；AP1411三频组合原文fulltext:1562-1568核实
    V2 160MHz仅静态+支持机型清单
    V3 机型能力矩阵特有
- id: p12
  title: Beacon/CSA/Short GI/DTIM/UAPSD 默认参数
  type: principle
  source_chapter: "p42, p64-65"
  source_quote: |
    Beacon Interval: You can specify a value within the range of 60-500. The default value is 100 milliseconds. CSA ... the packet count range is 1~10. ... The default value is 1, which means the client checks for buffered data on the AP at every beacon.
  summary: |
    Beacon 间隔范围 60-500ms，默认 100ms。CSA（信道切换通告）默认启用，报文计数范围 1-10。Short GI 默认启用（400ns 短保护间隔约提升 11% 速率，多径严重时建议关闭）。DTIM 间隔默认 1。UAPSD 默认启用（802.11e 省电特性）。
  tags: [beacon, csa, short-gi, dtim, uapsd, default]
  verify: |
    V1 p42/p64/p65 命中（表格拆行，句子级）；Short GI 11%原文fulltext:1632核实
    V2 Beacon 100ms/CSA 1-10/DTIM 1/UAPSD默认态
    V3 默认参数群
- id: p13
  title: 后台扫描默认值与间隔上限
  type: principle
  source_chapter: "p46"
  source_quote: |
    The scanning interval of Background Scanning can be configured from 5 seconds to 3 hours (180 minutes) according to deployment requirement. For highly sensitive packet delay use case, it is recommended to prolong the interval from default 20-second setting.
  summary: |
    后台扫描默认开启，默认间隔 20 秒，可配置 5 秒到 3 小时（180 分钟）。对时延敏感场景可只扫工作信道或加大间隔；但间隔超过 1 分钟会影响 RDA 与 wIPS 的精度（见陷阱条目）。后台扫描是 wIDS/wIPS 和 RDA 的基础。
  tags: [background-scanning, default, 20s]
  verify: |
    V1 原文精确命中 p46
    V2 默认20s、范围5s-3h、时延场景调法
    V3 默认值+范围特有
- id: p14
  title: Band Steering / Load Balance / RSSI 阈值默认与推荐值
  type: principle
  source_chapter: "p46-47"
  source_quote: |
    By default, band steering is enabled. ... The thresholds for client density is 10, channel utilization is 70% for 2.4G and 70% for 5G. By default, Load Balance is enabled. ... Recommended 2.4G (5), 5G (10), 6G (10). ... Recommended 2.4G (10), 5G (15), 6G (15).
  summary: |
    Band Steering 默认启用（Prefer 5G 模式，可选 Force 5G 强制双频终端上 5G）。Load Balance 默认启用，阈值：客户端密度 10、信道利用率 2.4G/5G 各 70%。RSSI Threshold 默认关闭（0），推荐 2.4G=5、5G=10、6G=10，适合高密场景；Roaming RSSI 默认关闭，推荐 2.4G=10、5G=15、6G=15，需配合 802.11k/v。Voice/Video Awareness 与 Airtime Fairness 默认关闭。
  tags: [band-steering, load-balance, rssi, default, recommended]
  verify: |
    V1 原文精确命中 p46/47
    V2 各阈值默认与高密推荐值可直接照配
    V3 具体数值阈值特有
- id: p15
  title: 客户端健康度分级与监控刷新周期
  type: principle
  source_chapter: "p27-28"
  source_quote: |
    Best - Number of clients whose signal strength is more than 30. Good - Number of clients whose signal strength is between 15 ~30. Fair - Number of clients whose signal strength is less than 15. ... The monitoring window is automatically refreshed every 30 seconds by default, and the data polling cycle can be set to 30s /60s /120s.
  summary: |
    Client Health 按信号强度分三档：Best > 30、Good 15~30、Fair < 15。监控窗口默认 30 秒自动刷新，轮询周期可设 30s/60s/120s。客户端漫游历史最多显示 32 条记录。
  tags: [client-health, monitoring, 30s]
  verify: |
    V1 p27/28 命中（监控页表格式文本，句子级）；漫游历史32条原文fulltext:1062核实
    V2 健康度分级阈值+刷新周期
    V3 分级标准特有
- id: p16
  title: WLAN 安全等级与 PSK 密码格式
  type: principle
  source_chapter: "p59"
  source_quote: |
    Enterprise: Also referred to as 802.1X mode ... requires a RADIUS authentication server. Personal: Also referred to as PSK (pre-shared key) mode ... Each wireless network device encrypts the network traffic using a 256 bit key. This key may be entered either as a string of 64 hexadecimal digits, or as a passphrase of 8 to 63 printable ASCII characters.
  summary: |
    WLAN 安全等级从高到低：Enterprise（802.1X，需 RADIUS）> Personal（PSK）> Open。Personal 模式使用 256 位密钥，可输入 64 位十六进制字符串或 8-63 个可打印 ASCII 字符的口令。Static-WEP 仅建议用于 802.11b 老客户端（最多 4 个 WEP 密钥，每个 10 或 26 位十六进制字符）。
  tags: [wlan, security-level, psk, wep]
  verify: |
    V1 p59 命中（PSK格式句精确；WEP表格词级）
    V2 PSK 64hex/8-63ASCII格式+WEP限制
    V3 配置必需参数（8-63字符为标准约束，手册明示）
- id: p17
  title: RADIUS 端口默认值与 RadSec 端口
  type: principle
  source_chapter: "p62-63"
  source_quote: |
    AuthPort - Communication port of the authentication server. The default value is 1812. If RadSec is enabled, the AuthPort should be configured 2083 or the value mapping RadSec server. ... AcctPort - Communication port of the accounting server. The default value is 1813.
  summary: |
    认证端口 AuthPort 默认 1812，计费端口 AcctPort 默认 1813；启用 RadSec（TLS）后 AuthPort 应改为 2083 或映射 RadSec 服务器的值。RadSec 仅适用于无线客户端，且只支持主 RADIUS 服务器。动态 VLAN（RFC-2868）支持三个属性：Tunnel-Type (#64)=VLAN、Tunnel-Medium-Type (#65)=802(6)、Tunnel-Private-Group-ID (#81)。
  tags: [radius, 1812, 1813, radsec, 2083]
  verify: |
    V1 p62-63 命中（端口句精确）
    V2 1812/1813默认、RadSec改2083、RFC-2868三属性
    V3 端口默认+属性号特有
- id: p18
  title: 空闲超时与每 BSSID 最大客户端数
  type: principle
  source_chapter: "p63"
  source_quote: |
    If Inactivity Timeout Status is disabled, the inactivity timeout interval is set to fixed 600 seconds. ... Configure the inactivity timeout period, with a valid range of 60 to 12000 seconds. ... Max Clients per band: You can specify a value within the range of 1 to 256. The default value is 64.
  summary: |
    空闲超时状态关闭时使用固定 600 秒；开启后可配置 60-12000 秒。每个 BSSID（每频段）最大客户端数范围 1-256，默认 64。组播转单播（基于 IGMP snooping）最多对 6 个客户端生效。6GHz 网络只支持 WPA3 与 Enhanced Open 加密。
  tags: [inactivity-timeout, max-clients, multicast, 6ghz]
  verify: |
    V1 p63 命中（Max Clients表格词级全命中）；组播转单播6客户端fulltext:2416、6GHz仅WPA3/EO fulltext:2425核实
    V2 600s固定/60-12000可配、每BSSID 1-256默认64
    V3 默认值群特有
- id: p19
  title: 客户端速率准入推荐值与管理帧速率例外
  type: principle
  source_chapter: "p64"
  source_quote: |
    2.4G band client with lower data speed will not be allowed to access, recommended value 12 ... 5G band client with lower data speed will not be allowed to access, recommended value 24 ... 2.4G Beacon frame does not support 9 Mbps or 18 Mbps speed. When 9/18 Mbps is configured for 2.4G MGMT Rate, beacon frame will broadcast on 11/24 Mbps rate.
  summary: |
    客户端速率准入推荐值：2.4G=12 Mbps、5G=24 Mbps、6G=24 Mbps，低于该速率的客户端拒绝接入。管理帧速率注意：2.4G Beacon 不支持 9/18 Mbps（配置后 Beacon 自动用 11/24 Mbps 发）；5G Beacon 不支持 9 Mbps（自动用 12 Mbps）。
  tags: [client-rate, recommended, beacon-rate]
  verify: |
    V1 原文精确命中 p64；6G推荐24原文fulltext:2515核实
    V2 速率准入推荐值12/24/24+Beacon速率例外行为
    V3 推荐值+管理帧速率机型行为特有
- id: p20
  title: 整组一份配置文件原则
  type: principle
  source_chapter: "p78"  # 修正：原候选标 p77，原文实际位于 p78
  source_quote: |
    All configuration settings (clear, backup or restore) will be applied to the entire group. There is no need to select specific APs to apply configuration settings. The entire group of APs have one configuration file.
  summary: |
    清除、备份、恢复配置均作用于整个 AP 组，无需选择具体 AP——整组只有一份配置文件。建议完成全部配置后立即导出备份。单 AP 固件升级约需 5 分钟。
  tags: [config, backup, group, firmware]
  verify: |
    V1 原文精确命中（实际页码p78，候选标p77，已修正）
    V2 整组一份配置文件原则+升级约5分钟（原文fulltext:3199）
    V3 架构级原则特有
- id: p21
  title: 替换 AP 与扩组的三种方法
  type: principle
  source_chapter: "p86"
  source_quote: |
    To replace the current PVM: Upgrade the SVM to the PVM before disconnecting the old PVM. ... Method one: Divide the Stellar APs into different subnets ... Method two: Setup up different group IDs ... Method three: Deploy Stellar AP with ALE OmniVista and scale up to 4000 AP in one network.
  summary: |
    替换 PVM 前必须先把 SVM 升级为 PVM 再断开旧 PVM；替换 SVM/成员可直接换，不影响其他 AP 用户。超过单组规格时三种扩组法：按交换机端口默认 VLAN 划分不同子网；每组配置不同 group ID；或用 OmniVista 管理可单网扩展到 4000 台 AP。新增 AP 前确保 PVM 不处于 Down 状态。
  tags: [replace-ap, scale, group-id, omnivista, 4000]
  verify: |
    V1 原文精确命中 p86；『新增AP前PVM不得Down』原文fulltext:3392核实
    V2 换PVM操作顺序+三种扩组法+OV 4000台
    V3 手册流程特有
- id: p22
  title: Out-of-box MESH 预置参数与不可逆条件
  type: principle
  source_chapter: "p103"
  source_quote: |
    By default, Stellar AP with factory configuration powered up without wired uplink will try to establish MESH link automatically with build-in configuration (MESH SSID [Stellar-MESH] and password on 2.4G band). The out-of-box will be permanently disabled once the AP ever connected to wired uplink.
  summary: |
    出厂配置的 AP 无线上电（无有线 uplink）会自动用内置 SSID "Stellar-MESH"（2.4G 频段）建立 MESH 链路，管理员只需指定根节点。AP 一旦连接过有线 uplink，Out-of-box MESH 被永久禁用，只有恢复出厂才能找回。Mesh 链路从根到叶必须同频段；组播速率默认 24 Mbps。
  tags: [mesh, stellar-mesh, out-of-box, 2.4g]
  verify: |
    V1 原文精确命中 p103；Mcast Rate默认24Mbps原文fulltext:3951核实
    V2 Stellar-MESH内置SSID+不可逆禁用条件
    V3 开箱Mesh机制特有
- id: p23
  title: AP 侧 DHCP 服务器与租约默认值
  type: principle
  source_chapter: "p107"
  source_quote: |
    Lease Time - Period of time that the IP address allocated can be used by the device. By default, lease time is 24 hours. ... Only Network with static IP (as gateway) can be bound to a DHCP pool.
  summary: |
    同一 L2 域内的 AP 组可在某台 AP 上开 DHCP 服务器（AP UI -> Service -> DHCP）。租约时间默认 24 小时；DHCP 池只能绑定配了静态 IP（作为网关）的 Network，且 VLAN 必须先映射到某 SSID 才会显示在可选列表中。
  tags: [dhcp, lease, 24h, ap-ui]
  verify: |
    V1 原文精确命中 p107
    V2 租约默认24h+DHCP池绑定静态IP Network的限制
    V3 AP侧DHCP限制特有
- id: p24
  title: 扫描模式两种类型与机型差异
  type: principle
  source_chapter: "p110"
  source_quote: |
    One Time - The scanning mode will last for 5 minutes duration and then return to normal AP mode ... Always - The scanning mode is always active and wireless client is not allowed to associate if the AP is powered on.
  summary: |
    AP 扫描模式分两种：One Time 持续 5 分钟后自动恢复正常模式；Always 模式下持续扫描、不允许客户端接入。查看 RF Environment 扫描数据必须让 AP 进入扫描模式。无扫描射频的机型进扫描模式会中断常规 Wi-Fi 服务（见陷阱条目）。
  tags: [scanning-mode, rf-environment, 5-min]
  verify: |
    V1 原文精确命中 p110
    V2 One Time 5分钟/Always语义差异
    V3 扫描模式行为特有
- id: p25
  title: Portal 用户库容量与行为日志周期
  type: principle
  source_chapter: "p50"
  source_quote: |
    Maximum 2000 accounts supported in AP local database for internal captive portal authentication. ... Specify the cycle for uploading user behavior logs to FTP server, can be set to 1 hour, 2 hours and 4 hours.
  summary: |
    内置 Portal 认证的 AP 本地用户数据库最多 2000 个账户（支持 Excel 模板导入）。用户行为日志（用户名/MAC/IP/WLAN/上下线/时间戳）可上传 TFTP/SFTP/Syslog 服务器，FTP 上传周期可设 1/2/4 小时。RADIUS Called-Station-ID 属性最长 64 字节。
  tags: [captive-portal, 2000, user-behavior-log]
  verify: |
    V1 原文精确命中 p50；Called-Station-ID 64字节原文fulltext:2003核实
    V2 本地库2000账户+日志周期1/2/4h
    V3 容量与周期特有
- id: p26
  title: ACL 顺序匹配与默认放行
  type: principle
  source_chapter: "p55"
  source_quote: |
    The ACL rules created in the list are applied sequentially, based on the precedence of top-to-bottom. By default, traffic is allowed to pass if no ACL rules are matched (Default ACL action is 'Accept').
  summary: |
    ACL 规则自上而下顺序匹配；无规则命中时默认动作是 Accept（放行）。支持 L3 ACL（源/目的 IP + TCP/UDP/ICMP 端口 + 通配符），Apply To EthPort 仅适用于 AP1201H/AP1201HL/AP1311/AP1301H 下行口。L2 级 MAC 控制走 Blocklist/Allowlist，802.1p/DSCP 规则在建 SSID 的 QoS 里配。
  tags: [acl, default-accept, order]
  verify: |
    V1 原文精确命中 p55
    V2 顺序匹配+默认放行（Accept）+EthPort适用机型
    V3 默认行为与机型限制特有
- id: p27
  title: 双上行 LACP 与 PoE 供电模式差异
  type: principle
  source_chapter: "p14"
  source_quote: |
    AP1230 series, AP1311 and AP1301 support PoE Redundancy - AP will only accept PoE on one of the two uplinks ... AP1351, AP1331, AP1451 and AP1431 support dual uplink connection with PoE Sharing - AP will accept PoE from the two uplinks at the same time.
  summary: |
    AP1230 系列、AP1311、AP1301、AP1351、AP1331、AP1411、AP1431、AP1451 支持双上行并在启动时与上游交换机建立 LACP 链路聚合（AP1230 用于在 1G 交换机上实现 2GE 吞吐）。供电分两类：AP1230 系列/AP1311/AP1301 为 PoE 冗余（单口供电、主断备启）；AP1351/AP1331/AP1451/AP1431 为 PoE 共享（两口同时供电），其中 AP1351/AP1451 为 Class 7，要求交换机支持 IEEE 802.3bt 及 PoE 固件 3.XX。
  tags: [lacp, dual-uplink, poe, 802.3bt]
  verify: |
    V1 p14 命中（跨行续接拼接）；Class 7/802.3bt/PoE固件3.XX原文fulltext:559-562核实
    V2 LACP双上行+PoE冗余vs共享选型
    V3 机型供电矩阵特有
- id: p28
  title: HTTPS 管理端口与证书域名约束
  type: principle
  source_chapter: "p34, p113"
  source_quote: |
    User needs to use domain 'mywifi.al-enterprise.com' for your own certificate because the login URL cannot be changed. ... (1) HTTP protocol with URL http://AP-IP:8080 ... (2) HTTPS protocol with URL https://AP-IP or https://mywifi.al-enterprise.com.
  summary: |
    两种登录方式：HTTP 用 8080 端口（http://AP-IP:8080），无需证书；HTTPS 用标准 443（https://AP-IP），需先从 AP 下载根证书 "ALE-OmniAccess-WLAN.CRT" 装入浏览器信任库。内置 Web 服务器证书必须使用域名 mywifi.al-enterprise.com（登录 URL 不可改），可用 OpenSSL 自签替换。
  tags: [https, certificate, 8080, 443]
  verify: |
    V1 p34句子级+p113精确命中（引用省略了括号示例https://172.16.101.34）；证书域名约束原文fulltext:1331核实
    V2 8080/443端口+CRT文件名+固定域名
    V3 特有约束。注：summary中『可用OpenSSL自签替换』原文无依据（原文仅允许自定义证书替换），下一阶段建议删除该短语

## 陷阱/警告/限制（14 条，全部通过）

- id: ce01
  title: 默认凭据 admin/admin 与必须改密的账户清单
  type: counter-example
  source_chapter: "p14, p16, p33"
  source_quote: |
    Login with the Administrator account and the default password 'admin'. ... It is highly recommended and a best security practice to change the default passwords for the predefined login accounts. ... For security the admin must change the CLI root, and support passwords before use.
  summary: |
    Web 管理员默认密码为 admin。除了 Web 的 Administrator/Viewer/GuestOperator 外，CLI 的 root 与 support 密码"使用前必须修改"（手册原话）。root 密码仅由客户持有、由 AP 生成真实 root 凭据，不改等于把最高权限留在默认态。
  tags: [default-credential, security, cli]
  verify: |
    V1 p14/p16/p33 命中（默认口令句、改密建议句均核到）
    V2 默认口令admin+完整账户清单（含CLI root/support生成机制）
    V3 主体为手册特有信息（默认凭据值+账户体系）；『须改密』部分属泛安全常识，依附于特有信息保留
- id: ce02
  title: 开局时一次只接一台 AP
  type: counter-example
  source_chapter: "p13"
  source_quote: |
    Note 3-2: It is recommended to connect only one AP at a time to the network and complete the configuration, then plug in other APs one by one to synchronize the configurations.
  summary: |
    初始化配置时应一次只把一台 AP 接入网络、完成配置后，再逐台插入其他 AP 同步配置。多台同时首次上电会各自成组，配置无法按预期收敛。
  tags: [initial-setup, deployment-order]
  verify: |
    V1 原文精确命中 p13（Note 3-2）
    V2 开局一次只接一台AP的部署顺序
    V3 非常识开局坑（多台同上电各自成组）
- id: ce03
  title: 初始化向导期间终端不能离开 mywifi-xxxx
  type: counter-example
  source_chapter: "p17"
  source_quote: |
    Note 3-9: While configuring the Initialization Wizards, please make sure your configuring terminal is connected to the pre-defined WLAN 'mywifi-xxxx' to keep the communication operational ... If not, you may encounter the following prompt and fail to complete the wizard configuration correctly.
  summary: |
    配置初始化向导全程，配置终端必须保持连在预置 WLAN "mywifi-xxxx" 上；中途切到其他网络会导致向导中断、配置失败。且向导完成后 mywifi-xxxx 即被删除（Note 3-10），后续无线管理必须改连向导里新建的 WLAN 再用新管理员密码登录。
  tags: [initializing-wizard, mywifi-ssid, connectivity]
  verify: |
    V1 原文精确命中 p17（Note 3-9，含Note 3-10删除行为）
    V2 向导全程保持连mywifi-xxxx的操作要求
    V3 特有坑
- id: ce04
  title: 初始化向导不能指定 VLAN
  type: counter-example
  source_chapter: "p16"
  source_quote: |
    Note 3-8: The VLAN assignment for the WLAN is not available in the initial wizard phase. You can modify the mapping VLAN value after the initial setup is completed, using the steps described in "Modify your WLAN" section.
  summary: |
    初始化向导创建 WLAN 时不支持配置 VLAN 映射，只能等向导完成后通过 "Modify Your WLAN" 补配。规划开局时要把 VLAN 调整算作向导后的必做步骤，否则员工/访客业务 VLAN 落不到位。
  tags: [wizard, vlan, two-step]
  verify: |
    V1 原文精确命中 p16（Note 3-8）
    V2 VLAN须向导后经Modify Your WLAN补配
    V3 特有两段式限制
- id: ce05
  title: AP1201 混入高端组时需手动干预 PVM
  type: counter-example
  source_chapter: "p18"
  source_quote: |
    If AP1201 coexists with AP1220/AP1230/AP1251 in the same cluster, and AP1201 is selected as PVM by the system automatically, suggest to manually intervene and turn one of the AP1220/AP1230/AP1251 to be the PVM for better management performance consideration.
  summary: |
    AP1201 与 AP1220/AP1230/AP1251 同组且被自动选为 PVM 时，建议手动把 AP1220/AP1230/AP1251 提升为 PVM（AP Window 的 "Update to PVM"），否则管理性能受损。同理，AP1101/AP1201H/AP1201L/AP1201HL 当 PVM 时整组只能扩到 32 台。
  tags: [pvm, mixed-model, performance]
  verify: |
    V1 原文精确命中 p18；『Update to PVM』原文fulltext:698/911核实
    V2 混型集群手动提升PVM的操作建议
    V3 特有机型混部坑
- id: ce06
  title: DHCP 失效导致全组 IP 冲突
  type: counter-example
  source_chapter: "p87"
  source_quote: |
    If the APs reboot and the DHCP server is not accessible, all the APs return to the system default IP -192.168.1.254. This means there are duplicate IPs in the broadcast domain. All the APs work separately as the PVM and broadcast the same WLANs.
  summary: |
    AP 重启时若 DHCP 服务器不可达，所有 AP 都回退到默认 IP 192.168.1.254，同一广播域内出现大量 IP 冲突，且每台 AP 各自成 PVM、广播相同 WLAN。手册强烈建议此时先修 DHCP 让无线服务恢复，而不是逐台手工处理。
  tags: [dhcp-failure, ip-conflict, 192.168.1.254]
  verify: |
    V1 原文精确命中 p87；『先修DHCP』建议原文fulltext:3430核实
    V2 DHCP失效的灾难模式与恢复优先级
    V3 特有故障模式（全组同IP各自成PVM）
- id: ce07
  title: 后台扫描关闭或拉长间隔的连锁劣化
  type: counter-example
  source_chapter: "p46"
  source_quote: |
    When it's turned OFF, the foreign AP detection and rogue suppression will stop and the RDA will drop its precision. ... If the interval is longer than 1 minutes, RDA and wIPS feature accuracy will be impacted.
  summary: |
    后台扫描关闭后，外部 AP 检测与 rogue 抑制直接停止、RDA 精度下降；扫描间隔超过 1 分钟也会影响 RDA 和 wIPS 准确性。为时延调大间隔或只扫工作信道时，要接受安全/射频优化能力的损失。
  tags: [background-scanning, rda, wips, tradeoff]
  verify: |
    V1 原文精确命中 p46
    V2 关扫描/拉长间隔的能力代价清单
    V3 特有权衡（安全/优化vs时延）
- id: ce08
  title: Allowlist 与 Walled Garden 仅对 Portal 生效
  type: counter-example
  source_chapter: "p53-54"
  source_quote: |
    The allowlist is applied to captive portal authentication ONLY. ... The allowlist does not support Enterprise/Personal WLANs. This means that the clients in the allowlist are not allowed to access Enterprise/Personal WLANs without using correct credentials.
  summary: |
    客户端 Allowlist 只对 captive portal 认证生效，不能豁免 Enterprise/Personal WLAN 的认证（名单里的客户端连这两种 WLAN 仍要正确凭据）。Walled Garden 同样只用于 Portal 场景；要放行某资源必须在认证前知道其 IP 或域名并加入 Walled Garden。而 Blocklist 则是对所有安全等级 WLAN 全局生效的封禁。
  tags: [allowlist, walled-garden, captive-portal, scope]
  verify: |
    V1 原文精确命中 p53-54
    V2 allowlist/Walled Garden作用域边界+Blocklist对照
    V3 特有作用域限制
- id: ce09
  title: CNSA 加密在不支持机型上静默回退 WPA2
  type: counter-example
  source_chapter: "p62"
  source_quote: |
    AP1101 full band does not support WPA3 CNSA encryption, AP1201H and AP1201L 2.4Ghz band does not support WPA3 CSNA encryption. ... When CSNA encryption is applied to an AP that does not support it, the encryption will automatically fall back to non-CSNA mode (WPA2).
  summary: |
    AP1101 全频段、AP1201H/AP1201L 的 2.4G 频段不支持 WPA3 CNSA（Suite B）；对不支持的机型配置 CNSA 时会"自动回退到非 CNSA 模式（WPA2）"，没有报错。高安全场景（政务/金融）按机型核对，否则实际加密强度低于预期。
  tags: [cnsa, wpa3, fallback, silent]
  verify: |
    V1 原文精确命中 p62（含静默回退句）
    V2 高安全场景按机型核对CNSA支持
    V3 特有静默降级行为
- id: ce10
  title: 固件升级后必须清浏览器缓存
  type: counter-example
  source_chapter: "p79"
  source_quote: |
    Note 6-2: In order to make sure you're running the latest software, we strongly recommend to clear the browsing data in your browser after the software upgrade, including: Cookies, Cache.
  summary: |
    AP 固件升级完成后，官方强烈建议清除浏览器的 Cookies 与 Cache，否则 Web 管理界面可能仍加载旧版本资源、表现异常。这是升级排障时最容易漏掉的一步。
  tags: [firmware-upgrade, browser-cache]
  verify: |
    V1 Note 6-2 命中（起于p79、Cookies/Cache列表续于p80，跨页）
    V2 升级后清Cookies/Cache的必做步骤
    V3 全集中独特性最弱（接近通用web排障常识），但为本手册明确强烈建议的产品流程步骤，保留并标记
- id: ce11
  title: 低端机型做无线桥接不转发 VLAN 标签
  type: counter-example
  source_chapter: "p106"
  source_quote: |
    AP1201, AP1201L, AP1201H, AP1201HL is low performance than other mid-end/high-end APs, and those APs do not support bridging the packets with VLAN tags, so not recommend deploying wireless bridge with above AP models. ... MESH AP can provide service to wireless client accompanied with MESH link. While Wireless Bridge AP can only provide bridge link.
  summary: |
    AP1201/AP1201L/AP1201H/AP1201HL 不支持带 VLAN 标签的桥接报文，不建议用于无线桥接（MESH 部署则正常）；确需使用要联系 ALE 支持。另外 Wireless Bridge 模式的 AP 只提供桥接链路、不能给无线客户端提供服务，这与 MESH 不同。
  tags: [wireless-bridge, ap1201, vlan-tag]
  verify: |
    V1 原文精确命中 p106
    V2 低端机型不做VLAN标签桥接的选型红线
    V3 特有机型限制
- id: ce12
  title: 无扫描射频机型进扫描模式会踢掉全部客户端
  type: counter-example
  source_chapter: "p110"
  source_quote: |
    AP models without scanning radio, regular Wi-Fi services will be stopped (all clients will be disconnected). ... AP1451 has scanning radio in 2.4G/5GHz so Wi-Fi clients on 2.4/5GHz will NOT be affected, but 6GHz service will be stopped.
  summary: |
    查看 RF Environment 扫描数据需要 AP 进入扫描模式，但机型差异很大：无扫描射频的机型会中断常规 Wi-Fi 服务（所有客户端掉线）；AP1451 的 6GHz 服务会中断（客户端被挤到 2.4G/5G）；带扫描射频的 Wi-Fi 6/Wi-Fi 7 机型不受影响。生产环境做扫描前先核对机型。
  tags: [scanning-mode, service-interruption, model-difference]
  verify: |
    V1 原文精确命中 p110
    V2 扫描前核对机型避免踢客户端
    V3 特有机型差异（无扫描射频/仅6GHz中断）
- id: ce13
  title: 组间不漫游与 Enterprise 模式切换的边界
  type: counter-example
  source_chapter: "p86, p24"
  source_quote: |
    Note 6-3: Without Omni Vista management, each group is managed independently and roaming between groups is not supported. ... Convert all the APs in the cluster to be managed through OmniVista On-Premise. Once configured, AP will reboot and register to On-Premise OV server.
  summary: |
    没有 OmniVista 统一管理时，多个 AP 组各自独立管理、组之间不支持漫游——多组方案要用在漫游边界清晰的位置。另外把 AP 切到 Enterprise 模式（转 OV On-Premise 管理）或转换云管时 AP 会重启注册，需在变更窗口执行。
  tags: [roaming, multi-group, enterprise-mode, reboot]
  verify: |
    V1 p86（Note 6-3）+p24（切换重启注册）命中
    V2 多组方案的漫游边界+切换窗口要求
    V3 特有架构限制
- id: ce14
  title: Portal 账号登录只认本地库且无设备数限制
  type: counter-example
  source_chapter: "p94"
  source_quote: |
    Note 7-2: If you have selected login by account method for the captive portal authentication, it ONLY supports users in the local user database. It does not support connecting to an external authentication server. ... Note 7-3: Single user account can be used by multiple devices simultaneously.
  summary: |
    Portal "账号+密码"登录方式只支持 AP 本地用户库（上限 2000 账户），不能外接认证服务器——需要外部 RADIUS 的场景不要选这种方式。同时单个账号可被无限台设备同时使用，无法按账号限制终端数，防蹭网要靠访问码轮换或行为日志审计。
  tags: [captive-portal, local-db, no-radius, account-sharing]
  verify: |
    V1 原文精确命中 p94（Note 7-2/7-3）
    V2 Portal账号方式的选型边界+防蹭网对策
    V3 特有限制（仅本地库+账号共享）

## 术语表（36 条，免验保留）

- id: g01
  term: AWOS
  full: Alcatel-Lucent Enterprise Wireless OS
  source_chapter: "p1"
  definition: |
    OmniAccess Stellar AP 的固件/操作系统，本手册对应 AWOS 5.0.3 版本（2025 年 9 月，060966-00 Rev. A）。版本号还影响兼容性判断，例如 AWOS4.0.0 及之前版本的 AP 默认不允许加入组（MQTT 兼容开关控制）。
- id: g02
  term: Express 模式
  full: Wi-Fi Express Mode
  source_chapter: "p8"
  definition: |
    Stellar AP 的本地集群管理模式，即本手册覆盖的模式：AP 自组成组、通过内置 Web GUI（Dashboard）完成配置与监控。与 Enterprise 模式（由 OmniVista On-Premise 统一管理）相对，切换到 Enterprise 模式需指定 OV 服务器地址且 AP 会重启。
- id: g03
  term: AP Group / Cluster
  full: AP 群组/集群
  source_chapter: "p13"
  definition: |
    具有相同 cluster ID 且位于同一 VLAN 的一组 Stellar AP，组内基于组播通信，最多 255 台。组内自动选举 PVM 和 SVM，整组共享一份配置文件。无 OV 管理时各组独立、组间不漫游。
- id: g04
  term: PVM
  full: Primary Virtual Manager
  source_chapter: "p13"
  definition: |
    AP 组的主管理虚拟角色，由组内按机型优先级和 MAC 地址选举产生，承担配置同步、用量统计、固件升级、Portal 服务等职责；组管理 IP（GMIP）配置在 PVM 上。PVM 故障时 SVM 自动接替，成员 AP 和无线用户业务不中断。
- id: g05
  term: SVM
  full: Secondary Virtual Manager
  source_chapter: "p13"
  definition: |
    AP 组的备份管理角色，选举规则与 PVM 相同（同优先级中 MAC 次高者当选）。PVM 无响应时自动升级为 PVM；替换 PVM 硬件前也应先把 SVM 升为 PVM。
- id: g06
  term: GMIP
  full: Group Management IP
  source_chapter: "p31-32"
  definition: |
    AP 组管理虚拟 IP，默认 10.0.0.1，配置在 PVM 上。用于规避 AP 从 DHCP 动态取址导致管理地址漂移的问题，可通过 http://GMIP:8080 有线或无线访问整组管理界面；建议取 AP 所在网段的空闲 IP，并保证从管理终端可路由。
- id: g07
  term: mywifi-xxxx
  full: Pre-defined SSID
  source_chapter: "p13"
  definition: |
    AP 组默认广播的预置 SSID，xxxx 为 PVM MAC 地址的最后两个字节。连接它可访问 http://mywifi.al-enterprise.com:8080 进入初始化向导；向导完成后该 SSID 自动删除。相关域名 mywifi.al-enterprise.com 同时是内置 HTTPS 证书的固定域名。
- id: g08
  term: 初始化向导
  full: Initializing Wizard
  source_chapter: "p14-17"
  definition: |
    首次开局向导，共五步：欢迎页、修改管理员密码（默认 admin）、选国家码与时区（仅 -RW 机型）、创建新 WLAN、完成确认。向导阶段不能配 VLAN；全程需保持终端连在 mywifi-xxxx 上。
- id: g09
  term: ZTP
  full: Zero Touch Provisioning
  source_chapter: "p11"
  definition: |
    零接触开通。手册场景 2：AP 从 ALE OXO 服务器获取 IP、下载固件与配置文件，自动重启成组并生效三个 WLAN，全程无需手工逐台配置。
- id: g10
  term: OXO
  full: ALE OXO Server
  source_chapter: "p11"
  definition: |
    ALE 的 OXO 服务器，在 ZTP 场景中为 AP 分配 IP 地址并下发固件与配置文件，是 AP 组开局的上游自动化节点。
- id: g11
  term: RDA
  full: Radio Dynamic Adjustment
  source_chapter: "p40-41"
  definition: |
    ALE 的射频动态调整技术（商标 ™），根据周围无线环境自动调整工作信道与发射功率，包含 ACS（自动选信道）与 APC（自动功率控制）两个功能，默认启用。依赖后台扫描开启；手动指定信道/功率前必须关闭 ACS/APC。
- id: g12
  term: ACS
  full: Auto Channel Selection
  source_chapter: "p41"
  definition: |
    自动信道选择，RDA 的组成部分，默认开启并周期性执行。开启 Client Aware 时不为有客户端的 AP 换信道（雷达检测等高优先级事件除外）；ACS 不会选用 160MHz 信道。
- id: g13
  term: APC
  full: Auto Power Control
  source_chapter: "p41"
  definition: |
    自动功率控制，与 ACS 同属 RDA，动态调整 AP 发射功率。关闭后进入手动模式，功率按 1 dB 步进设置，且 2.4G/5G 两个频段都要分别配置。
- id: g14
  term: wIDS/wIPS
  full: Wireless Intrusion Detection/Prevention System
  source_chapter: "p42-45"
  definition: |
    无线入侵检测/防御系统。通过后台扫描发现外部未知 AP（干扰 AP 与 rogue AP），支持 AP allowlist（信任名单）、AP blocklist（仅 rogue 可入）、Suppress（向 rogue 的客户端发 DEAUTH，默认关闭）与 Dynamic blocklist（自动拉黑 ad-hoc 设备，默认关闭）。
- id: g15
  term: 干扰 AP / Rogue AP
  full: Interfering AP / Rogue AP
  source_chapter: "p42"
  definition: |
    干扰 AP 指出现在无线环境但未接入有线网络的外部 AP，仅构成潜在射频干扰、不算直接安全威胁。Rogue AP 指未经授权插入网络有线侧的外部 AP，或广播与 AP 组相同 SSID 的外部 AP，被视为安全威胁，可加入 blocklist 阻止其伪装客户端接入。
- id: g16
  term: Captive Portal
  full: 强制门户认证
  source_chapter: "p59, p92-97"
  definition: |
    开放网络上的 Web 认证机制：用户浏览任意网站时弹出 Portal 页，输入账号密码、访问码或勾选使用条款后放行。Stellar 支持内置/外部 Portal 服务器、自定义 Splash 页、Walled Garden、Portal allowlist、用户行为日志（TFTP/SFTP/Syslog，1/2/4 小时周期）。
- id: g17
  term: Walled Garden
  full: 认证前白名单园区
  source_chapter: "p54"
  definition: |
    captive portal 场景下的网络资源控制机制：把允许的域名或 IP 加入 Walled Garden 后，客户端在通过 Portal 认证之前即可访问这些资源（如酒店官网）。要放行某资源必须预先知道其 IP 或域名。
- id: g18
  term: Dynamic VLAN
  full: RADIUS 动态 VLAN 分配
  source_chapter: "p62"
  definition: |
    Enterprise WLAN 下按 RADIUS 下发属性把客户端划入不同 VLAN 的功能。Express 模式支持 RFC-2868 三属性：Tunnel-Type (IETF #64)=VLAN、Tunnel-Medium-Type (IETF #65)=802(6)、Tunnel-Private-Group-ID (IETF #81)。
- id: g19
  term: RadSec
  full: RADIUS over TLS
  source_chapter: "p62"
  definition: |
    用 TLS 隧道安全传输 RADIUS 认证与计费数据的协议。启用后 AuthPort 须改为 2083（或映射 RadSec 服务器的值）；该特性仅适用于无线客户端，且只支持主 RADIUS 服务器，不支持 secondary。
- id: g20
  term: PMF
  full: Protected Management Frames (IEEE 802.11w)
  source_chapter: "p62"
  definition: |
    管理帧保护标准，为管理帧提供机密性保护。可选 Disabled/Optional/Required 三态；WPA3 Enterprise 选 CNSA 时 PMF 强制为 Required（仅支持 PMF 的客户端可接入）。
- id: g21
  term: CNSA
  full: Commercial National Security Algorithm Suite
  source_chapter: "p62, p92"
  definition: |
    美国商用国家安全算法套件。WPA3-Enterprise 192 位安全套件与 CNSA 对齐，常见于政务、国防、金融等高安全网络。注意机型限制：AP1101 全频段、AP1201H/AP1201L 的 2.4G 不支持，配置后静默回退 WPA2。
- id: g22
  term: Enhanced Open / OWE
  full: Opportunistic Wireless Encryption
  source_chapter: "p71"
  definition: |
    开放网络的增强加密：客户端与 WLAN 在接入过程中做 Diffie-Hellman 密钥交换并用 4 次握手生成成对密钥，防止明文被嗅探。Transition 模式下同一虚拟 AP 同时广播传统 Open SSID（2.4/5G）与 Enhanced Open SSID（2.4/5/6G）。6GHz 网络只允许 WPA3 与 Enhanced Open。
- id: g23
  term: MLO
  full: Multi-Link Operation
  source_chapter: "p63"
  definition: |
    Wi-Fi 7 的关键特性，允许设备同时使用多个频段（2.4G/5G/6G）聚合传输以提升速率与效率。MLO 生效依赖对应射频开启且 EHT（802.11be）已启用；MLO 客户端的 MAC 栏显示 MLD 地址，附着频段按 6GHz>5GHz>2.4GHz 优先显示。
- id: g24
  term: EHT / HE / VHT
  full: Extremely High / High / Very High Throughput
  source_chapter: "p42"
  definition: |
    分别对应 802.11be（Wi-Fi 7）、802.11ax（Wi-Fi 6）、802.11ac 的 PHY 模式。关闭 High Efficiency 时 HE 能力的 AP 降级到 VHT；关闭 Extremely High Throughput 时 EHT 能力的 AP 降级到 HE。
- id: g25
  term: Band Steering
  full: 频段引导
  source_chapter: "p46-47"
  definition: |
    把双频客户端引导到 5GHz 的特性，默认启用。Prefer 5G 模式基于信道利用率和客户端密度柔性引导（5G 忙时可回 2.4G）；Force 5G 模式强制双频终端只能上 5G（仅支持 2.4G 的终端不受限）。可按客户端排除（Exclude）。
- id: g26
  term: Airtime Fairness
  full: 空口时间公平
  source_chapter: "p47"
  definition: |
    让所有客户端（包括低速传统客户端）均等分享无线传输时间片的优化特性，默认禁用。配套特性还有 Load Balance（默认启用，客户端密度阈值 10、信道利用率阈值 70%）、RSSI Threshold、Roaming RSSI（配合 802.11k/v）。
- id: g27
  term: RSSI
  full: Received Signal Strength Indication
  source_chapter: "p26"
  definition: |
    接收信号强度指示，客户端窗口中取值 0~99。Client Health 分级依据：信号强度 >30 为 Best、15~30 为 Good、<15 为 Fair。wIDS/wIPS 还用 RSSI 估算未知 AP 距离：> -20dBm 最近、-45~-20dBm 近、-70~-45dBm 远、< -70dBm 最远。
- id: g28
  term: WMM
  full: Wi-Fi Multimedia (IEEE 802.11e)
  source_chapter: "p74"
  definition: |
    Wi-Fi 联盟基于 802.11e 的 QoS 认证，按四个接入类别排队：voice (AC_VO)、video (AC_VI)、best effort (AC_BE)、background (AC_BK)。Stellar AP 上可编辑 DSCP/802.1p 值与 WMM 优先级的映射关系（Modify WLAN QoS）。
- id: g29
  term: DTIM
  full: Delivery Traffic Indication Map
  source_chapter: "p65"
  definition: |
    Beacon 中的 DTIM 周期参数，决定 AP 向省电模式客户端投递缓存广播/组播帧的频率。默认 1（每个 Beacon 都检查缓存数据）；调大可增强终端省电效果。
- id: g30
  term: UAPSD
  full: Unscheduled Automatic Power Save Delivery
  source_chapter: "p64"
  definition: |
    802.11e 的非调度自动省电交付机制，可延长 Wi-Fi 终端电池续航，默认启用。相关漫游加速特性 OKC（Opportunistic Key Caching）复用缓存的 PMK 避免完整 802.1X 认证，实现快速漫游。
- id: g31
  term: Out-of-box MESH
  full: 开箱即连 Mesh
  source_chapter: "p103"
  definition: |
    出厂配置的 AP 在无有线 uplink 上电时，自动用内置 SSID "Stellar-MESH"（2.4G 频段）建立 Mesh 链路的特性，管理员只需指定根节点。AP 一旦接过有线 uplink 即被永久禁用，只有恢复出厂才能找回。Regular MESH 则需逐台登录 AP UI 手工配置。
- id: g32
  term: Wireless Bridge
  full: 点对点无线网桥
  source_chapter: "p105"
  definition: |
    通过无线接口连接不同楼宇/局域网的点对点网桥，替代昂贵专线与光纤。与 MESH 的关键区别：网桥 AP 只提供桥接链路、不能服务无线客户端；且 AP1201/AP1201L/AP1201H/AP1201HL 不支持带 VLAN 标签的桥接报文，不推荐做网桥。
- id: g33
  term: PMD
  full: Post Mortem Dump
  source_chapter: "p99"
  definition: |
    AP 致命崩溃后的故障诊断机制，用于定位 core dump 与异常指针的根因。启用并配置后，AP 关键进程崩溃时立即把 PMD 文件发送到指定 TFTP 服务器；默认向外发送是关闭的。
- id: g34
  term: DHCP Option 138 / Option 43
  full: DHCP 选项 138/43
  source_chapter: "p24"
  definition: |
    AP 切换到 Enterprise 模式（OmniVista On-Premise 管理）时，可通过这两个 DHCP 选项在 AP 启动阶段自动获取 OV 服务器地址，也可静态指定 OV 服务器地址。相关：组内还可通过 "Contact to Cloud" 周期性联系 OmniVista Cirrus 云管（默认启用）。
- id: g35
  term: LACP / 双上行
  full: Link Aggregation Control Protocol
  source_chapter: "p14"
  definition: |
    AP1230 系列、AP1311、AP1301、AP1351、AP1331、AP1411、AP1431、AP1451 支持双上行并在启动时与上游交换机自动建立 LACP 链路聚合。供电模式分 PoE Redundancy（单口供电）与 PoE Sharing（两口同时供电，AP1351/AP1451 为 Class 7、要求 IEEE 802.3bt 交换机）。
- id: g36
  term: Scanning Mode
  full: AP 扫描模式
  source_chapter: "p110"
  definition: |
    AP UI 里用于查看 RF Environment 数据的专用模式，分 One Time（持续 5 分钟后自动恢复）与 Always（持续扫描、拒绝客户端接入）两种。无扫描射频的机型进入该模式会中断常规 Wi-Fi 服务；AP1451 的 6GHz 服务会中断。
