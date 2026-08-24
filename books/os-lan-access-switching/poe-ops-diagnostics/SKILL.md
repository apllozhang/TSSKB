---
name: poe-ops-diagnostics
description: 何时用：在 OmniSwitch 上配置 PoE 供电、用 swlog/抓包/健康检查排障，或做软件升级与 Auto Fabric 零配置时。
source_book: DT00XTE215EN Access Switching
---

# PoE 与运维工具：供电 / 日志 / 抓包 / 升级

## R · 原文引用

"-> update uboot cmm all file u-boot.8.4.1.R03.141.tar.gz / -> update fpga-cpld cmm all file fpga_kit_3312 / -> reload from working no rollback-timeout / -> copy running certified. Note: If there are any issues after upgrading the switch can be rolled back to the previous certified version."（p452-456）

"Switch events can be logged to Switch console / Local text file (Configurable default file size 1250 Kbytes) / Multiple remote devices (syslog) 12 max. Up to 8 Swlog logs files can be stored in the /flash directory."（p161-162）

"802.3af: 15.40 W (EPS max) / 802.3at Type 2: 30.0 W / 802.3bt Type 3: 60 W / Type 4: 100 W. Default priority level for a port is low... Critical: inline power to critical ports is maintained as long as possible."（p434-441）

## I · 方法论骨架

运维四块：
- **日志**：swlog 输出 console/flash（swlog_chassis1~1.6 轮转 8 个，单文件默认 1250KB）/syslog（≤12 台）；按 appid/subapp 调级（默认 info=6）。command-log 审计"谁改了配置"（100 条、须启用）。
- **抓包双工具**：port-mirroring（实时复制流量到分析口，4 会话/4 MTP）；port-monitoring（存 /flash 的 .enc 抓包，单会话、每帧 64 字节、默认 64KB 最大 2MB）。
- **监控**：show health（CPU/内存）；RMON 探针；sFlow 采样（sampler 采包头 + poller 采计数器 → receiver）。
- **PoE**：af=15.4W / at=30W / bt T3=60W / T4=100W（型号带 P 才支持）；端口优先级 low（默认先断）/high/critical（尽量保电）；FPoE 开机秒级供电、PPoE 重启不断电（均需 FPGA/CPLD 升级）。
- **升级**：读 release note → 传文件入 running 目录 → reload from working 验证 → copy running certified 固化；必要时先 update uboot / update fpga-cpld。

## A1 · 书中案例（Lab 配置精要）

诊断工具 Lab（p187-195，6870-A）：`swlog appid all subapp all level event` + `show log events` 输出客户可读事件；`command-log enable` 后建删 VLAN 用 `show command-log` 验证审计；`port-mirroring 1 source port 1/1/1 destination port 1/1/10` + enable；`port-monitoring 1 source port 1/1/1 enable` + pause/resume/disable，`show port-monitoring file` 回显；`show health`、`show rmon probes stats 1`。

## A2 · 触发场景（含与相邻 skill 的区分）

- "谁改的配置"、"端口流量抓下来看"、CPU/内存异常、供电预算与断电保护、整机软件升级——本 skill。
- 按流量条件跨机镜像（RPM/策略镜像）→ qos-acl-policy。
- 配置保存/回滚语义与目录操作 → aos-config-management（升级流程中的 reload/copy 命令语义见彼）。
- VC 整体不停机升级（ISSU）→ virtual-chassis-deployment。

## E · 可执行步骤

日志与审计：
1. 看日志：`show log swlog`（CTRL+C 停）；调级：`swlog appid <进程> subapp <子> level <1-8|debug3>`。
2. 审计：`command-log enable` → `show command-log`。
抓包：
3. 镜像：`port-mirroring <会话> source port <口> destination port <口>` + `port-mirroring <会话> enable`（源/目的同容量）。
4. 抓包文件：`port-monitoring <会话> source port <口> enable`，可 pause/resume/disable/timeout。
监控：
5. `show health` / `show rmon probes [history|stats]` / sflow sampler+poller → receiver。
PoE：
6. `lanpower …` 管预算/优先级；延迟上电 delayed-start 120-600 秒（5 的倍数，启用后不支持 FPoE/PPoE，须 write memory 才重启保留）。
升级：
7. 读 release note → 传镜像（FTP/SFTP/USB/WebView）→ `reload from working no rollback-timeout` 验证 → `copy running certified`；U-Boot/FPGA 先行 `update uboot …` / `update fpga-cpld …`。
零配置：
8. auto-fabric admin-state enable（Auto-VC/RCL 拉配置/Auto-LACP/Auto-SPB 等）。

## B · 边界与陷阱

- **port monitoring 与 port mirroring 不能落同一物理口**；monitoring 每机仅 1 会话、文件上限 2MB——排障前先规划口的角色。
- 镜像双向计 2 个 MTP 索引（共 4 个）；源/目的口容量必须一致。
- command.log 只留最近 100 条；日志开启期间文件不可删，删文件即删史。
- FPoE/PPoE 需升级 FPGA/CPLD；6360-P10A 不支持 FPoE/PPoE。
- 升级后异常可回滚旧 certified——固化前留足观察期。
- RCL/Auto Fabric 拉配置只在 VLAN 1/127 各试 3 次 DHCP，规划零配置网段时别拦这几个 VLAN。

---
来源条目: f14, p22, p23, p24, p25, p26, p39, ce08, c05, g34, g35, g37, g38
