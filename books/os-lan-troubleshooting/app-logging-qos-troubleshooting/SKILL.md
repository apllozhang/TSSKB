---
name: app-logging-qos-troubleshooting
description: 何时用：需要读/调 swlog 日志、用 QoS 策略计数定位流量、端口抓包与镜像、UNP/802.1X 认证排障、固定 syslog 源地址。
source_book: DT00XTE221EN OmniSwitch LAN Troubleshooting
---

# 应用与日志排障（swlog / QoS / 镜像 / UNP）

## R · 原文引用

> "Switch events can be logged to Switch console, Local text file (Configurable default file size 1250 Kbytes - R8), Multiple remote devices (syslog) 12 max - R8, Loopback0 have to be configured -> swlog output socket ipaddr 168.23.9.100" (p146)

> "Default severity level is info. The numeric equivalent for info is 6 ... swlog appid ospf_0 subapp all level 8 ... or swlog appid ospf_0 subapp hello level debug3" (p151)

> "policy condition cond1 source ip 192.168.8.10 icmptype 8 / policy rule rule1 condition cond1 action action1 log / qos apply" (p214)

> "aaa test-radius-server <server_name> type authentication user <username> password <password> method pap ... Access-Accept from <server_IP_address> Port 1812 Time: 212 ms ... Filter-ID = employee" (p309)

## I · 方法论骨架

1. **swlog 架构**（p15/g19）：三目的地——console、本地 flash（R8 默认 1250KB/文件，swlog output flash-file-size 12500 可改；/flash/swlog_chassis1~.6 共 8 个滚动文件 + swlog_archive 40 个归档）、远程 syslog（最多 12 台，需 Loopback0 源）。show swlog 看状态与 90% 覆盖告警阈值。
2. **调级机制**（p16）：默认全局 info（=6）。`swlog appid <appid> subapp <all|子应用|编号> level <级别>` 按应用单独调级。OSPF 子应用编号表：3=RECV 4=SEND 5=FLOOD 6=SPF 7=LSDB 13=DBEXCH 14=HELLO 15=AUTH 16=STATE 28=AUTOCONFIG 等（p151/p244）。**排障后必须调回 info**。
3. **日志检索三板斧**（p17）：grep（show log swlog |grep ospf，可级联）；时间戳（timestamp mm/dd/yyyy hh:mm:ss，前提 show system 核对时钟）；reverse（最新在前）。可读事件层：swlog appid all subapp all level event + show log events 输出 CUSTLOG 格式。
4. **QoS 生命周期四命令**（p35）：qos apply（生效并写 flash）/ qos revert（删未 apply 的）/ qos flush（清全部待定）/ qos reset（恢复默认）。监测：show active policy rule（命中计数）、show qos log（命中明细，上限 10000 行）、qos log level 1-8（默认 5）。
5. **镜像工具边界**（p37/ce14）：RPM 专用镜像 VLAN 不能捎带业务流量；六类流量设计上不被镜像——LACP、LLDP、802.1X、OAM、L3 控制报文、GARP；"抓不到"不等于"不存在"。策略镜像同时只支持 1 会话；端口镜像与端口监控不能同端口。
6. **UNP/802.1X 认证排障**（p36/g23/g24）：RADIUS 连通性测试先行（aaa test-radius-server）；随后 show unp user（Active/In progress）→ show unp port/profile map/classification → show aaa/captive-portal/quarantine。Access Guardian 框架四块：认证/分类/角色访问/限制阻断。
7. **源地址固定**（p38）：多 IP 设备用 `ip service source-ip loopback0 swlog` 等命令把 syslog/radius/snmp/ssh 等应用发包源固定，防火墙/ACL 场景防丢包，OVNA 纳管时必须与登记 IP 一致。

## A1 · 书中案例（LAB 故障根因）

- **ce04（LAB2/LAB4 收尾实证）**：LAB4 专门列出收尾命令 swlog appid ospf_0 subapp all level info，LAB2 同样收尾——不调回 debug 级日志持续高速写 flash，本身就制造高 CPU/日志风暴次生故障。
- **ce12/g23（RADIUS 假阴性）**：aaa test-radius-server 失败就断定服务器坏——测试工具只支持 MD5/PAP，服务器侧可能未开放这两个方法。
- TKC 案例 N2（c01，方法论 skill）：UNP 用户卡 "In progress" 是已知缺陷形态，LAB1 用 `unp user flush port <口>` 清理（另见 c02 的 l2 skill）。

## A2 · 触发场景（含与相邻 skill 的区分）

- 触发：任何需要看日志/调日志级的排障（本 skill 是全书的工具层）；丢包计数验证；需要抓包取证；802.1X/UNP 认证失败；syslog 发不出去。
- 区分：本 skill 提供**工具**，各协议 skill（stp/l3/multicast）提供**判读对象**——读 OSPF 日志的语义在 l3 skill，调级与检索手法在本 skill。QoS 计数找丢包段的完整流程在 l3-routing-vrrp skill。

## E · 可执行步骤

1. 排障前：show system 核对时钟 → show swlog 确认日志输出目的地。
2. 检索：show log swlog |grep <appid> [timestamp ...] [reverse]；要人可读事件用 level event + show log events。
3. 调级：`swlog appid <appid> subapp <subapp> level debug2|debug3` → 复现 → 检索 → **`... level info` 收尾**（写进 SOP）。
4. 丢包计数：policy condition（source ip + icmptype）→ policy action → policy rule ... log → qos apply → show active policy rule / show qos log；改配置后 clear qos log 清旧日志。
5. 抓包：`port-monitoring 1 source port <口> capture-type full enable file /flash/capture.cap` → FTP 取回 Wireshark 分析 → `no port-monitoring 1`。远程用 RPM 专用 VLAN。
6. 认证排障：`aaa test-radius-server <srv> type authentication user <u> password <p> method pap` → show unp user → show unp port/profile/classification → 服务器侧日志佐证。
7. 固定源地址：`ip service source-ip loopback0 swlog`，show ip service source-ip 核对各应用绑定。

## B · 边界与陷阱

- **ce04**：debug 级忘记调回 info 是最高频收尾遗漏，会制造次生故障。
- **ce03**：debug ip packet 必须带过滤维度并尽快 stop。
- **ce12**：RADIUS 测试失败先怀疑方法不匹配（MD5/PAP 前提），再怀疑服务器。
- **ce13**：QoS 策略只匹配 ingress，出向分析改用 port-monitoring。
- **ce14**：RPM VLAN 不得复用；六类控制流量抓不到是设计行为。
- qos apply 前配置不生效——改完策略没 apply 是"配置没起作用"的头号原因（p35）。
- syslog 上限 12 台且必须配 Loopback0（p15）。

---
来源条目: p15, p16, p17, p35, p36, p37, p38, ce03, ce04, ce12, ce14, g19, g23, g24, g31, g32, g40
