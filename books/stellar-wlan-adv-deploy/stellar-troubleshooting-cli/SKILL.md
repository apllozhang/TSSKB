---
name: stellar-troubleshooting-cli
description: 何时用：无线/客户端故障已定位到设备层，需登 Stellar AP 用 CLI 命令、抓包与判据逐层排查时用。
source_book: DT00XTE361EN Stellar WLAN Advanced Deployment
---

# Stellar AP 进阶排障 CLI 清单

## R · 原文引用

> "Check wireless configuration — Check List: SSID broadcasted on the selected radio(s)? Transmission Power as selected in the RF profile? Encryption activated? BSSID is present?" (p260)

> "REASONS FOR ROAMING FAILURE: APs must be seen as neighbors; No Roaming from an untagged VLAN to a tagged VLAN; RSSI too low between source AP and destination AP." (p264)

> "Client first connection to the Captive Portal. Client IP address unknown. Redirection URL can not be sent. ... Client IP address retrieved. Stellar AP sends redirection URL to the client." (p220)

> "ssudo tcpdump –i br-wan -w test-capture.pcap udp port 53 ... All the traffic exchanged between the AP and the access switch is going through this interface." (p238)

## I · 方法论骨架

排障前置铁律：**先 NTP 全网同步**（AP、OmniVista、交换机同一台 NTP），否则跨设备日志时间戳对不上。
接入手段：SSH（企业/云管模式需先在 AP 组 Provisioning 里启用并设密码）或串口（115200 8N1，无校验无流控；默认账号 support/aos2016）。
按层检查：
1. **无线配置**：iwconfig 看 SSID 是否在目标射频广播、功率与 RF Profile 一致、加密开启、BSSID 存在。接口命名 athXYY：X=0/1/2 对应 2.4/5/6GHz，YY=SSID 编号（ath001=2.4G 的 1 号 SSID）。
2. **RF 配置**：cat /tmp/config/rfprofile.conf 对照 Band Steering/Load Balance/扫描/国家码/信道/功率/门限。
3. **客户端**：ssudo sta_list（第一命令——VLAN/IP/时长/收发计数/认证方式/Final_role）；cat /proc/kes_syslog 看 DHCP 与关联；ssudo wlanconfig athXX list 看 RSSI/SNR（RSSI 值 29≈-67dBm、20≈-76dBm、10≈-86dBm）。
4. **漫游**：adme show 看邻居与 RSSI；wam.log 搜 L2/L3 roaming-start/success。漫游失败三判据：邻居互相可见；untagged/tagged VLAN 间不能漫游；源/目标 AP 间 RSSI 过低。
5. **门户**：eag_cli show user all；/var/log/eag.log——首连 IP 为 0.0.0.0 发不出重定向是正常时序，先查 IP 再查门户。
6. **抓包**：有线侧 ssudo tcpdump -i br-wan（AP 与接入交换机全部流量走 br-wan），pcap 经 SFTP 取出用 Wireshark；空口抓包在 Provisioning 启 "AP web" → RF Environment 选信道过滤，文件送 TFTP。
7. **系统**：top 看单进程 %CPU（案例 drm 81% 为死循环/软件问题）；ps 看 R/S 正常、X(Dead)/Z(Zombie) 异常——僵尸进程吃内存；date/uptime 核对 NTP 与意外重启。

## A1 · 书中案例（Lab 精要）

四个排障用例（p276-284、p214-217）：
- **看不到 SSID** 三问：SSID 是否真在该射频广播（iwconfig）？客户端射频与 SSID 频段兼容？AP 国家码被客户端支持？国家码错误的规避法：RF Profile 里手工指定一个双方兼容的信道，无需改国家码。
- **拿不到 IP**：客户端 Wireshark + AP tcpdump 双侧抓 DHCP 看丢在哪侧，sta_list 核对 VLAN 与 Final_role 是否过滤 DHCP。
- **频繁掉线**：iwlist txpower 查功率（案例 Tx-Power=3dBm 压到最小，RSSI 16/SNR 30 临近掉线）；RF Profile 的 signalStrengthThreshold 案例设 70，低于门限的客户端被主动踢——下调；空口抓包看去关联/去认证帧。
- **802.1X 失败**三段对照：客户端（账号/加密/证书）↔ AP（AAA_server.conf 的 IP/端口/共享密钥、wlanservice.conf 绑定的 aaaProfile）↔ RADIUS 服务器（用户库、共享密钥、NAS IP、防火墙放行 1812/1813）。
- **高 CPU/僵尸进程**：top 定位异常进程（81% 的 drm）→ 收集进程清单开票，不要只重启了事。

## A2 · 触发场景（含与相邻 skill 的区分）

- 现象明确（看不到 SSID、拿不到 IP、掉线、802.1X 失败、漫游断、门户打不开、CPU 高）→ 本 skill 对应用例。
- 还不知道问题在哪、要从体验指标入手 → stellar-qoe-analytics。
- 只想远程下发命令或收集日志包 → stellar-monitoring-ops。
- 语音掉话/单通等语音质量问题 → stellar-vowlan（RSSI/SNR 标准更严）。

## E · 可执行步骤

1. 前置：确认 NTP 全网同步；确认有 SSH（Provisioning 已启用）或串口参数 115200 8N1。
2. iwconfig 核对 SSID/功率/加密/BSSID；用 athXYY 规则定位目标接口。
3. cat /tmp/config/rfprofile.conf 对照 RF 设计（重点：信道、功率、signalStrengthThreshold、国家码）。
4. ssudo sta_list 看目标终端的 VLAN/IP/Final_role；kes_syslog 按 MAC 过滤关联与 DHCP 日志。
5. 按现象分支：
   - 漫游问题 → adme show 邻居表 + 三判据逐条过 + wam.log 搜 roaming-success；
   - 门户问题 → eag.log/eag_cli，先确认客户端已拿到 IP；
   - DHCP 问题 → br-wan tcpdump + 客户端侧 Wireshark 双侧对照；
   - 802.1X 问题 → 客户端/AP 配置文件/RADIUS 三段对照。
6. 仍不明：空口抓包（AP Web > RF Environment，>5 分钟）或系统层 top/ps 查异常进程。
7. 产出：进程清单、pcap、syslog 片段打包，配合 Collect Support Info 交技术支持。

## B · 边界与陷阱

- untagged 与 tagged VLAN 之间不能漫游：同一 SSID 多 AP 部署必须统一打标方式，这类失败是静默的。
- signalStrengthThreshold 设得过高会主动踢弱信号客户端（案例 70），"频繁掉线"别只盯功率。
- 低功率部署（如打印机紧邻 AP）是特例，通用覆盖照搬 3dBm 必掉线。
- 门户首连 IP 未知发不出重定向是正常时序，不是门户故障；先查 IP（DHCP/VLAN/Final_role 过滤）。
- 国家码不匹配表现为"看不见 SSID"，现象与根因错位；规避靠指定兼容信道。
- 僵尸/Dead 进程累积吃内存，发现后开票附进程清单，不要只重启。
- 演练环境踩坑：交换机重启阶段按键会进 Miniboot（排障重启时同样适用）。

---
来源条目: f11, c11, c12, c13, p13, p14, p20, p22, p23, p24, ce01, ce05, ce06, ce07, ce08, ce09, ce11, g51, g52, g53, g54, g55, g56
