---
name: network-side-trouble
description: 何时用：AP 自身拿不到 IP、疑似上游网络（VLAN/DHCP/路由/DNS/syslog）或 AP 要接入 OmniVista 云管上线失败时，用本 skill 分段排查。
source_book: DT00XTE478EN Stellar WLAN Advanced Troubleshooting
---

# 网络侧排障：AP 取址 · 连通性 · 服务器 · 云管前置

## R · 原文引用

> 1) IP address assignment? Static or DHCP? How to set the IP assignment to DHCP: Reset AP to factory default. Log in to AP web UI and set the IP address mode to DHCP. cat /etc/config/network - option proto 'dhcp'. DHCP assignment. (p99)

> Capture and analyze DHCP packets on the uplink port. Check network connection between AP and DHCP server when no answer is received. Check that DHCP server sends at least DHCP-NAK packet for out-of-pool request. (p100)

> ifconfig br-wan - Check the IP address and mask of the LAN interface. Traffic exchanged between the AP and the network? - Sent/Received packets. route -n - What is the gateway of the default route? Is it the correct default route? ssudo ping 10.130.5.50 - The Stellar AP can ping the OmniVista server. (p94-95)

> Open Firewall ports: 9093, 30123, 30124, 30125. And to allow outbound traffic from local network: 443, 80, 123, 53. Enable DHCP standard options: 1, 2, 6, 28, 42, 43. Software version: AWOS 4.0.6 GA or higher (Cirrus) / AWOS 4.0.7.14 or higher (Terra). (p170, p179)

## I · 方法论骨架

**AP 拿不到 IP 两步法**

1. 查分配模式：`cat /etc/config/network` 看 wan 接口 `option proto` 是 dhcp 还是 static。切回 DHCP 两条路：恢复出厂默认，或登录 AP Web UI 改 IP 地址模式。
2. 上联口抓包（DHCP-NAK 判据）：
   - 正常：Discover → Offer → Request → ACK 全流程。
   - 完全无回应 → 查 AP 与 DHCP 服务器之间的连通性。
   - **健康服务器对池外请求至少回 DHCP-NAK；连 NAK 都没有 = 报文根本没到服务器（链路/VLAN/中继问题），而非地址池问题。**

**连通性四命令（AP 视角分段）**

| 命令 | 判读 |
|---|---|
| `ifconfig br-wan` | IP/掩码；RX/TX 报文计数判断与网络有无流量 |
| `route -n` | 默认路由网关是否正确 |
| `ssudo ping <目标>` | 逐个测：网关 → NTP/DHCP/DNS 服务器 → 防火墙 → OmniVista |
| `ssudo traceroute <目标>` | 流量实际路径，是否先送网关、路由是否需调整 |

**时间/DNS 三件套**：`cat /etc/resolv.conf`（DNS 与搜索域）→ `cat /tmp/TZ`（时区，错则日志整体偏移）→ `cat /proc/kes_syslog | grep ntp`（确认完成过 NTP 同步）。

**syslog 不上报三步验证**（分别排除配置错/进程挂/网络不通）：
1. `cat /var/config/syslog.conf`：log_remote=1、log_ip/log_port（默认 514）正确。
2. `ps | grep logread`：`/sbin/logread -f -r <IP> <port>` 进程在跑。
3. `logger -p emerg "Just for test!"` 实测，服务器端是否收到。

**OmniVista 云管/本地管上线前置（硬门槛）**：防火墙开 9093、30123-30125；放行出向 443/80/123/53；DHCP 选项 1/2/6/28/42/43（代理另加 129-133、138）；至少 1 台 NTP；AWOS 版本 Cirrus ≥4.0.6 GA、Terra ≥4.0.7.14；AP1101、AP1201L/H/HL 不受支持。

## A1 · 书中案例

- 全书主案例的网络侧成因（p11-18）：OmniVista 里 SSID 映射 VLAN 10、接入交换机 Building_A 配 VLAN 20，tagged 不一致 → 认证后拿不到正确子网，全员连不上 Employee SSID。Resolution：更新交换机 tagged VLAN ID=20。
- ce15 的 NAK 判据：教材要求"至少应回 DHCP-NAK"，把"地址池问题"与"路径不通"一刀分开（p100）。

## A2 · 触发场景（含与相邻 skill 的区分）

- AP 本身起不来网（拿不到 IP、ping 不通网管）→ 本 skill；客户端拿不到 IP（AP 正常）→ `client-connection-trouble`。
- AP 换到云管后不上线/不上报 → 本 skill 的前置参数清单 + syslog 三步。
- SSID 的 VLAN 映射与交换机 tagged VLAN 核对（ce01 型问题）→ 本 skill；无线侧 SSID/射频配置 → `wireless-rf-roaming-trouble`。

## E · 可执行步骤

1. AP 无地址：`cat /etc/config/network` 查 proto → 不对则改回 DHCP（出厂重置或 Web UI）。
2. 仍无地址：上联口 `tcpdump` 抓 DHCP，按 NAK 判据分流：无 NAK → 查中间链路/VLAN/中继；有 Offer 不 ACK → 查地址池。
3. 有地址但不通：ifconfig br-wan → route -n → ssudo ping 逐跳（网关/NTP/DNS/OmniVista）→ ssudo traceroute 看路径。
4. 日志缺失：syslog 三步（配置 → logread 进程 → logger 实测）。
5. 云管上线失败：核对防火墙端口组、出向端口、DHCP 选项、NTP、AWOS 版本与不支持型号清单。

## B · 边界与陷阱

- "连 NAK 都没有"最容易被误判为地址池耗尽——NAK 判据说明是路径不通。
- proto=static 模式下抓包只能看到徒劳的请求，确认模式是抓包前提。
- 时区错但 NTP 同步正常时，日志时间仍整体偏移（教材示例 /tmp/TZ=UTC+08 标注 Wrong time zone），跨设备对齐前必查 /tmp/TZ。
- 云管前置里 AP1101/AP1201L/H/HL 硬件就不支持，先查型号再查配置。
- ce01 教训：全员连不上而 AP 本身正常，优先怀疑接入交换机侧 VLAN，别先动无线配置。

---
来源条目: p22, p24, p25, p26, ce01, ce14, ce15, ce16（术语 g05 br-wan, g12 OmniVista Cirrus, g13 OmniVista Terra, g22 DHCP-NAK）
