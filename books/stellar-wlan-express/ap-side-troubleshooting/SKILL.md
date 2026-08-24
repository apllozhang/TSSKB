---
name: ap-side-troubleshooting
description: 何时用：AP 不上电、拿不到 IP、入不了集群、客户端无 IP 或端口报错等单体/链路故障排障时。
source_book: DT00XTE455EN Stellar WLAN Express
---

# AP 侧与链路排障案例库（三域分类）

## R · 原文引用

> "AP TROUBLESHOOTING - CASE 1: AP can't be powered up. CASE 2: AP fails to get an IP address from the DHCP server. CASE 4: AP can't join a cluster. CLIENT TROUBLESHOOTING - CASE 7: Client can't get an IP. PERFORMANCE TROUBLESHOOTING - CASE 11: Low throughput/latency. CASE 13: AP not supplied with PoE." (p126-160)

> "Step 1: Connect to the AP, using the web GUI with the default IP address 192.168.1.254. Step 2: If you can't access the AP using the web GUI, access the AP using the console. Baud Rate: 115200. Step 3: use 'ssudo tcpdump –i br-wan –s0 –w X.pcap' commands to capture the DHCP messages." (p129-132)

> "Check that the cluster ID value is similar on the AP and on the PVM. Use the command 'cluster_mgt –x show=self'... If the AP is in 'joining' state, it must be joined manually. Check if the cluster has already reached the maximum number of APs allowed (32/64/255 APs depending on the AP models)." (p136-138)

## I · 方法论骨架

排障章 15 案按故障对象分三域，**接单先归域再套案例**，每案固定"现象→分步检查→命令验证"：

- **AP 侧域**：无法上电（LED 判读）、DHCP 拿不到 IP（三步递进救援）、ping 不通/Web 打不开、入不了集群（四查）。
- **客户端侧域**：拿不到 IP（抓包定位 VLAN/信道错配）、连不上 AP/集群（黑名单/MaxClients，见 ssid-portal-auth skill）、认证与 Portal（见 ssid-portal-auth skill）。
- **性能侧域**：低吞吐/高时延五查（见 rf-survey-tuning skill）、AP 端口报错三板斧、PoE 不供电五查。

通用救援梯度：**Web（默认 IP 192.168.1.254）→ Console（115200-8-N-1）→ tcpdump 抓包（/tmp 存 pcap，tftp 上送 Wireshark）**。集群通信判据：端口 32767 = PVM 下发报文，32768 = AP→PVM 报文。

## A1 · 书中案例

- **Case 1 AP 不上电**（p128）：LED 全灭查电源（基准 12W/802.3at/48V DC，双源 DC 优先）；LED 非绿按九态表判读：蓝常亮=已上电、绿常亮=加载系统、闪=网络异常或未建 SSID、红蓝交替=升级中、三灯交替=定位模式。
- **Case 2 DHCP 拿不到 IP**（p129-132）：三步递进——默认 IP 直连 Web 改回 DHCP 模式 → Console 查 `cat /etc/config/network` 的 option proto（残留 static 是经典根因）→ tcpdump 抓 DHCP 报文，正常应见 Discover-Offer-Request-ACK 完整四步。
- **Case 4 入不了集群**（p136-138）：四查——cluster ID 与 PVM 一致（`cluster_mgt -x show=self`）→ 同网段 + tcpdump 抓 32767 验 PVM 报文可达 → joining 状态需在 PVM Web 手工批准 → 集群是否达型号组合上限（32/64/255）+ 抓 32768 确认 AP 有在发。
- **Case 7 客户端拿不到 IP**（p144-147）：抓 DHCP 报文分三类——同一报文反复重发=VLAN ID 配错；终端没发=查终端静态残留；发了 AP 收不到=空中抓 beacon 比对信道与配置是否一致。
- **Case 11/12 性能与端口**（p155-156）：低吞吐五查（详见 rf-survey-tuning）；端口三板斧=换线缆、`ifconfig br-wan` 确认有 IP、`ethtool eth0` 查协商。
- **Case 13 PoE 不供电**（p157）：五查=交换机 PoE 开关 → 线长换 100m 内短线 → 水晶头不达标整根换 → 交换机不合 802.3af/at 换机 → 对调正常 AP 验证。

## A2 · 触发场景（含与相邻 skill 的区分）

- 触发：工单"AP 灯不亮/失联/进不了集群""客户端连上了没网""端口报错""PoE 不供电"。
- 区分：这是**故障处置**入口——归域后部分案例会路由出去：认证/Portal/黑名单类归 `ssid-portal-auth`；覆盖弱/吞吐低的射频侧五查归 `rf-survey-tuning`；集群规划与 255 上限的**设计层**归 `express-cluster-onboarding`。本 skill 管单体与链路层的"救活"，不管优化与规划。

## E · 可执行步骤

通用救援梯度：
1. Web 直连默认 IP **192.168.1.254**（PC 配同网段）。
2. Web 不通走 Console：**115200-8-N-1**，先核线缆再怀疑设备。
3. 仍不通 `cd /tmp` 后 `tcpdump -i br-wan -s 0 -w X.pcap` 抓包，tftp 上送 Wireshark 分析。

按域套案例：
4. 不上电：LED 判读 → 电源三参数（12W/48V DC/DC 优先）→ PoE 五查。
5. 拿不到 IP：三步递进 + 检查 `option proto` 残留 static。
6. 入不了集群：四查（cluster ID → 子网/32767 → joining 手工批准 → 上限/32768）。
7. 客户端无 IP：抓包三分法（VLAN/终端残留/信道错配 beacon 比对）。
8. 端口报错：换线 → ifconfig br-wan → ethtool eth0。

Console 常用命令速查：lighttpd（Web 进程，`ps | grep lighttpd`，`/etc/init.d/lighttpd start` 重建）、wam（无线接入管理，按 athXX 端口）、`athstats -i wifi0/1`（PHY 错误）、`wlanconfig athXX list`（连接帧与信号）、sfe（会话跟踪）。

## B · 边界与陷阱

- **option proto 残留 static**：改过静态地址的设备入新网不发 DHCP 请求——用 ifconfig br-wan 读出现地址借道 Web 改回 DHCP；入网前先恢复。
- **joining 卡死先数集群规模**：可能是 255 上限静默撞墙（设计问题），也可能是需 PVM 手工批准（操作问题），勿混。
- 集群上限随在网型号组合浮动（32/64/255），排障勿默认 255。
- 32767/32768 两端口是跨防火墙部署的必放行项，也是判断"谁没说话"的分向器：32767 无包=收不到 PVM 消息查网络；32768 无包=AP 没在发，重启 AP。
- 引用校注：p157 原文 "802.3af or 802.3af" 为教材笔误，应为 af/at，引用时保留校注。
- tcpdump 命令原文为 "ssudo"，实际使用 sudo。

---
来源条目: f09, c06, c07, c08, c11, c13, p12, p13, ce09, ce15, g34
