---
name: stellar-ap-toolbox
description: 何时用：需要登录 Stellar AP 取证（串口/SSH/Web）、抓有线或空口报文、备份配置离线分析时，用本 skill 拿对参数与命令语法。
source_book: DT00XTE478EN Stellar WLAN Advanced Troubleshooting
---

# Stellar AP 排障工具箱：登录通道 · 抓包 · 配置备份

## R · 原文引用

> Console: Speed 115 200, Data bits 8, Stop bits 1, Parity None, Flow ctrl None. File: /var/config/public_group.conf - ssh_connect = 1 (SSH enabled), ssh_connect = 0 (SSH disabled). Login to the AP web UI: https://<AP_IP> or http://<AP_IP>:8080. In OmniVista Cirrus - Enable "AP web" in the Provisioning Configuration List. (p23-26)

> Step 1 - CLI connection to the AP with "support" account. ssudo tcpdump -i br-wan -w testcapture.pcap udp port 53. You are listening to the interface br-wan - which is the wired interface - connecting the Stellar AP to the network. Step 2 - Transfer the captured file on your PC/laptop (SFTP tool, WinSCP). Step 3 - Open and read the file with Wireshark. (p30)

> Step 2 - In RF Environment, select the Radio to capture. Click on Start Capture. Select the Channel. Enter the TFTP server where the capture will be sent. Option: Filter the capture (MAC, Frame type). Warning: Capture file limited to 10MB or 5min of capture. (p31)

> Backup the configuration of one or multiple Stellar AP. Used to re-create the issue. Shared with the technical support. Download the file "pub-config.tar" locally. "Restore All Configuration" using the .tar file. Extract the config-pub.tar file. Check the configuration offline. (p33)

## I · 方法论骨架

**三通道登录参数表**

| 通道 | 参数/开关 | 备注 |
|---|---|---|
| 串口控制台 | 115200 波特 / 8 数据位 / 1 停止位 / 无校验 / 无流控 | 设备没 IP 时的唯一入口 |
| SSH | /var/config/public_group.conf 中 `ssh_connect=1` 启用、0 禁用 | Enterprise 模式需在 AP Group 激活 SSH 并自定义密码；CLI 凭据 support / aos2016（实验室默认） |
| Web UI | `https://<AP_IP>` 或 `http://<AP_IP>:8080` | 云管理模式必须先在 OmniVista Cirrus 的 Provisioning Configuration 里开启 "AP web" |

**抓包路径二选一**

- 有线侧（DHCP/DNS/RADIUS）：`ssudo tcpdump -i br-wan -w testcapture.pcap <过滤式>`，br-wan 是 AP 有线桥接口；SFTP（WinSCP）回传 → Wireshark 分析。
- 空口侧（关联/认证/被踢）：集群 Web UI → 选 AP → RF Environment → 选射频 → Start Capture → 指定信道 + TFTP 服务器，可选 MAC/帧类型过滤。**硬上限 10MB 或 5 分钟**，规划过滤条件要按此预算。

**配置备份双用途**：集群 Web UI → AP 窗口 → Backup All Configuration → 下载 pub-config.tar。用途一：自有环境 Restore All Configuration 复现故障；用途二：解包 config-pub.tar 离线逐项核对；同时是技术支持工单的标准共享材料。

## A1 · 书中案例

- tcpdump 示例用 DNS 过滤（`udp port 53`）演示三步流程，抓 DHCP/RADIUS 换过滤式即可（p30）。
- Air Capture 云模式同流程：先在 Cirrus 开 AP Web，再登录 AP Web UI 操作（p31-32）。
- 配置备份是 p12 复现法四类采集清单中 "Stellar AP 配置备份" 一项的标准件（p33）。

## A2 · 触发场景（含与相邻 skill 的区分）

- 需要"看到报文"才能定性的故障：DHCP 不下发、认证无响应、疑似被踢（比对 disassoc/deauth）。
- 与 `network-side-trouble` 的区分：那边是"查连通性与配置核对"，本 skill 是"取证工具本身的参数与用法"。
- 与 `client-connection-trouble` 的区分：那边是客户端症状决策链；本 skill 提供其依赖的 tcpdump/Air Capture 手段。

## E · 可执行步骤

1. 选登录通道：无 IP 走串口（115200 8N1）；有 IP 走 SSH（确认 ssh_connect=1）或 Web（云模式先开 AP web）。
2. CLI 用 support 账号登录（默认密码 aos2016；生产环境 Enterprise 模式自定义密码）。
3. 有线抓包：`ssudo tcpdump -i br-wan -w <文件>.pcap <过滤>`；WinSCP 回传；Wireshark 打开。
4. 空口抓包：Web UI → RF Environment → Start Capture → 信道 + TFTP + 过滤；预算控制在 10MB/5min 内。
5. 备份配置：Backup All Configuration → pub-config.tar；需要时解包 config-pub.tar 离线比对。

## B · 边界与陷阱

- 云管理模式下 Web UI 登不上，十有八九是没在 Cirrus 开 "AP web"，先查开关再怀疑网络。
- tcpdump 默认接口不是 eth0，Stellar 的有线桥接口叫 **br-wan**，抓错接口什么都看不到（客户端侧抓 DHCP 时教材另用 `tcpdump -i eth0 -s0`）。
- Air Capture 超过 10MB/5min 自动停止，不加过滤容易浪费预算在无关流量上。
- aos2016 只是训练环境默认密码，生产环境以 AP Group 自定义密码为准，别拿它当通用后门。

---
来源条目: p02, p03, p04, p05, p07, p01（术语 g05 br-wan, g28 Air Capture, g30 Wireshark, g17 eag, g12 OmniVista Cirrus）
