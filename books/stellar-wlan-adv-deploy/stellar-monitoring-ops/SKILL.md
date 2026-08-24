---
name: stellar-monitoring-ops
description: 何时用：设备已上线进入运维期，需要看监控/告警/热力图/拓扑、做升级备份、收集支持信息时用。
source_book: DT00XTE361EN Stellar WLAN Advanced Deployment
---

# Stellar 监控告警与设备生命周期运维

## R · 原文引用

> "Scheduled Upgrades: Creation of scheduled upgrade, Management of scheduled update... Configuration Backups: Start immediate Backup on the selected device... Scope selection: switch, site, floor." (p233)

> "Green - Device connectivity is up and there are no trap notifications. Orange - connectivity is unknown or warning/major traps... Red - connectivity is up with critical trap notifications... Solid-Grey - connectivity is down." (p247-248)

> "Minimum of 3 Stellar APs required to generate a Heat Map." (p177)

> "Note that when a device is upgraded, it will reboot with the new image. It will then become unavailable during this upgrade duration and all the end clients connected to this device will be disconnected." (p253)

## I · 方法论骨架

运维期四大抓手 + 两个读图能力：
1. **升级计划**：四步向导（Schedule Setting → 设备选择 → Set Software Version → Review），按站点/AP 组/单 AP 维度；升级=重启=终端断连，必须纳入变更通知。
2. **配置备份**：可含安全文件，可按交换机/站点/楼层排程。
3. **远程排障**：Device Troubleshooting 下发预置命令（可改参数）；Collect Support Info 收日志包（AP 为 tar.gz 快照，交换机 swlog/cfg/Tech Support 分 L2/L3/Engineering Complete 层级）。
4. **事件与告警**：Network Events 分 AP Traps / Switch Traps / QoE Analytics 三类，按 Severity（Normal→Critical）浏览、Acknowledge。
5. **读图**：拓扑状态色（绿=正常、橙=未知或 warning/major、红=critical、蓝=minor/normal、灰=失联；约 2 秒刷新）；热力图（按站点/AP，最少 3 台 Stellar AP；密度红/黄/绿=高/中/低）。
6. **报表**：Regular 模板报表与 Analytics Data 报表（选指标/列/范围导出 PDF/CSV），可即时或排程（如周一 8:00 周报，结果邮件自动下发）。

## A1 · 书中案例（Lab 精要）

Lab 走读五大运维动作（p250-257）：① 升级计划四步向导只演示不执行（默认 6 小时升级窗口）；② Network Events 浏览三类事件；③ Collect Support Info 从 Uploading 变 Collected 后下载；④ Alerts 顶部汇总+底部 Entry List，新告警红点提示；⑤ 给 AP 下发 setDateTime 命令几分钟后回读结果。监控侧（p183-187）：Clients 仪表盘查树莓派 RSSI/噪声底/吞吐/PHY 速率；Authentication Records 与 Captive Portal Records（看 Auth result 与 Reject Reason）；创建 Analytics Data Report（Wireless Client Sessions、PDF、Last 7 days、Instant），报表邮件自动送达。设备目录与拓扑（p242-249）：Actions 全集（Edit Device/SSH/Web UI/Configuration Management），拓扑悬停看链路类型与楼层，点设备看 7 天 trap。

## A2 · 触发场景（含与相邻 skill 的区分）

- 网络已交付，要建例行监控（阈值、报表、告警）或做变更（升级、备份）→ 本 skill。
- 用户报体验问题要"分析定位根因"（QoE 六指标下钻）→ stellar-qoe-analytics。
- 已知具体故障要登 AP 用 CLI 排（sta_list、抓包）→ stellar-troubleshooting-cli。
- 要逆向拆除整套云管配置 → stellar-deployment-checklist（含组织清理流程）。

## E · 可执行步骤

1. 建监控基线：Edit Device / Health Thresholds 设 CPU/内存/闪存阈值（演练基准 70%），按业务收紧（如 2.4G 射频利用率 20%、客户端健康 90%、可用容量 25%）。
2. 排报表：Network > Reports > Create Report，选 Analytics Data Report、指标、范围、Instant 或排程，收邮件取件。
3. 日常巡检：拓扑应用按颜色扫一遍设备与链路状态；Network Events 按 Severity 过滤未 Ack 事件。
4. 升级：确认目标版本与窗口已批准 → 四步向导创建计划 → 变更通知中注明"升级窗口内设备重启、终端断连"。
5. 故障取证：Device Troubleshooting 下发命令；必要时 Collect Support Info（交换机按需选 Tech Support 层级）交技术支持。
6. 看覆盖：站点部署 ≥3 台 Stellar AP 后生成热力图，核对覆盖与客户端密度分布。

## B · 边界与陷阱

- 升级必然重启且终端断连（默认 6 小时窗口），生产创建计划前必须确认版本确实需要、窗口已批准；训练/演示环境止步于 Review 点 Cancel——原文明确 "Use this section only as a configuration guide, and do not complete this upgrade process."（p252）
- 热力图硬性前提：少于 3 台 Stellar AP 无法生成。
- 拓扑"红"仍表示连通（只是有 critical 告警），"灰"才是失联，别读反。
- SSH/Web UI 访问 AP 需先在 Provisioning Configuration 启用并设凭据。
- 客户端仪表盘里设备名与 IPv4 需几分钟才浮现，别急着判"数据缺失"。

---
来源条目: f07, c06, c07, c08, p12, p17, p18, p21, ce12, g35, g41, g42, g43, g44, g45, g46
