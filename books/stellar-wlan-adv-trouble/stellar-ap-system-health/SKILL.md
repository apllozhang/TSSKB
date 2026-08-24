---
name: stellar-ap-system-health
description: 何时用：AP 本身可疑——LED 异常、疑似重启、高 CPU/内存、Captive Portal 不弹页、Express 集群异常时，用本 skill 的免登录与命令判读表体检。
source_book: DT00XTE478EN Stellar WLAN Advanced Troubleshooting
---

# Stellar AP 基础层排障：LED · 系统 · 进程 · 门户 · 集群

## R · 原文引用

> Flashing Green: System Running, Default SSID broadcasted. Solid Green: System Running, Single band working. Solid Blue: System Running, Dual band working. Flashing Blue & Red: OS upgrading. Solid Red: System startup. AP1251/AP1360: 7 LEDs - SYS ON: Power On - System Running; ENET0/1 Solid: Ethernet Link UP; 5G/2.4G Solid: SSID created and running; PSE ON: PSE Enabled. (p41-44)

> High CPU utilization - Impact performances of the Stellar AP: speed, features not working as intended. Process Status - OK: R (Running), S (Interruptible Sleep); Issue: X (Dead) and Z (Zombie process). Too many Zombie processes will consume large portion of memory. Share these processes with the Technical Support when opening a ticket. (p51-53)

> eag_cli show user all - ID, UserName, UserIP, UserMAC, SessionTime, OutputFlow, InputFlow, AuthType, ESSID. Check List: Is the client authenticated on the Captive Portal? For how long is the client connected? Does the client send/receive data to the network? (p55)

> Check the "cluster" process on the AP - Are both processes running? Two existing "cluster_mgt" threads indicates abnormal behavior (one running, one sleeping). (p59)

## I · 方法论骨架

**LED 免登录第一道体检表（单三色 LED 家族 AP12XX/13XX/14XX/15X1）**

| 状态 | 含义 |
|---|---|
| 闪绿 | 运行中，默认 SSID 广播中 |
| 纯绿 | 运行中，仅单频段工作 |
| 纯蓝 | 运行中，双频工作 |
| 蓝红闪 | 固件升级中 |
| 蓝/红/绿三色闪 | AP 定位模式 |
| 纯红 | 系统启动中 |

AP1251/AP1360 用 7 颗独立 LED：SYS（常亮=运行/闪烁=加载升级）、2.4G/5G（SSID 创建运行）、ENET0/1（链路 up）、SFP、PSE（PoE 供电）。AP1201H 的 PoE 灯：橙常亮=受电在线、橙闪=离线、灭=PSE 禁用。

**系统四命令**

| 命令 | 看什么 |
|---|---|
| showsysinfo | SN/型号/MAC/**国家码**/软硬件版本 |
| showver | 精确构建版本（如 3.0.7.20） |
| getmode | CLUSTER=Express / OV=Cloud / OVNG |
| show_cluster | 集群成员（MAC/IP/角色/版本）+ OmniVista 服务器 IP（云模式用 getovinfo） |

**进程健康判定**：top 按 %CPU 找元凶、看全局内存；ps 看状态列——**R/S 正常，X（Dead）/Z（Zombie）异常**；僵尸进程堆积吃内存。开票必附进程列表。

**高 CPU 四根因**：异常进程 / 进程死循环（疑软件缺陷）/ 过量日志与跟踪引发的计算 / DoS 攻击。

**重启核查顺序纪律**：先 `date`（对时，时间不可信则日志定位无意义）→ `uptime`（判断是否计划外重启）→ 才去日志收集包按对齐后时间戳找重启原因。

**Captive Portal 三查**：`eag_cli show user all` 核对——是否已认证（有无表项）、连了多久（SessionTime）、有无收发数据（OutputFlow/InputFlow 全零=认证后不通）；再看 `cat /var/log/eag.log` 三阶段痕迹定位卡点。

**Express 集群三查**：`cluster_mgt -x show=self / show=pvc`（PVC 选出且角色正确、状态 RUN）→ `show_cluster`（成员齐全）→ `ps | grep cluster`（cluster_mgt 与 cluster_cor 各一个；**出现两个 cluster_mgt 线程=异常**）。

## A1 · 书中案例

- 教材示例 `/usr/sbin/drm` 占 81% CPU，即 top 定位元凶后随工单上报的典型（p52）。
- eag.log 三阶段：客户端首联 IP 未知（userip 0.0.0.0）→ 获取 IP → 发出 PortalRedirect。**卡在 IP 未知阶段 = DHCP 未完成，先查地址获取而非门户本身**（p56）。
- p50 重启核查：uptime 远小于部署时长即发生过非计划重启，先对时再翻日志。

## A2 · 触发场景（含与相邻 skill 的区分）

- 症状是"AP 整体不对劲"（灯不对、疑似重启、变慢、功能失灵）→ 本 skill；症状是"单个客户端连不上/掉线"→ `client-connection-trouble`。
- 门户相关：用户 complaining 转不出认证页 → 本 skill 的 eag 部分；802.1X 认证失败（无门户）→ `dot1x-radius-trouble`。
- LED 显示纯红（启动中）长时间不变化 → 硬件/启动问题，本 skill 优先；LED 正常但 AP 不上线 → `network-side-trouble`。

## E · 可执行步骤

1. 到场先看 LED，按表判读单双频/升级/启动状态，免登录定性。
2. SSH/串口进 CLI（见 stellar-ap-toolbox），跑 showsysinfo / showver / getmode / show_cluster，核对国家码与版本与预期一致。
3. 怀疑重启：date → uptime → 日志收集包按时间戳找原因。
4. 性能异常：top 找元凶进程（记 PID/命令名/%CPU）→ ps 查状态列扫 X/Z → 记录后随工单上报，勿自行 kill 系统进程。
5. 门户故障：eag_cli show user all 三查 → cat /var/log/eag.log 定位三阶段卡点 → 卡在 IP 未知转 `client-connection-trouble` 的 DHCP 排查。
6. Express 集群异常：三查依次执行，两个 cluster_mgt 线程即判异常。

## B · 边界与陷阱

- 跳过 date/uptime 对时直接翻日志找重启原因——时间线错位，结论不可信。
- 僵尸进程属软件问题（父进程未回收子进程），正确动作是上报工单附进程列表，不是反复重启掩盖。
- "过量日志/跟踪开启"引发计算型高 CPU 这一根因容易被忽略——排查时检查是否开了 debug/trace。
- 双 cluster_mgt 线程（一运行一睡眠）是产品特定的异常信号，别当成正常冗余。
- LED 表只覆盖教材所列型号；其他型号先查对应快速指南。

---
来源条目: p06, p08, p09, p10, p11, p12, ce17, ce18, ce20, ce22, ce23（术语 g09 PVC, g10 Cluster, g11 getmode 三态, g16 Captive Portal, g17 eag, g23 PoE/PSE, g33 僵尸进程）
