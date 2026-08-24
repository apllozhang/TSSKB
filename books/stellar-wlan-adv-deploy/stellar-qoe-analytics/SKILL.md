---
name: stellar-qoe-analytics
description: 何时用：在 OmniVista Cirrus 上用 QoE/网络/客户端三大分析定位无线体验问题时，按此仪表盘工作流与阈值体系操作。
source_book: DT00XTE361EN Stellar WLAN Advanced Deployment
---

# Stellar 云管分析三件套：QoE / 网络分析 / 客户端分析

## R · 原文引用

> "OmniVista Cirrus provides six metrics to be monitored: Successful Connects, Time To Connect, Roaming, Coverage, Available Capacity, Device Uptime." (p158)

> "QOE DASHBOARD — Filters / Thresholds / Summary / Details / Shortcuts" (p125)

> "NETWORK ANALYTICS — Channel Distribution (2.4/5/6GHz), Channel Utilization, Network Devices Health (CPU, Memory, Flash), Network Devices Uptime." (p138)

> "CLIENT ANALYTICS — Connected Clients Over Time; Client Distribution per frequency bands / across managed Access Point / on Access Point per client range." (p147)

## I · 方法论骨架

云管可观测性分三层，由粗到细：
1. **QoE（体验质量）**——从终端视角回答"用户体验好不好"：六指标 + 失败分类器。
   - Successful Connects（成功连接数，计数器无阈值）
   - Time To Connect（关联/授权/DHCP/Portal 四阶段总耗时；阈值 2-20s，默认 2s）
   - Roaming（漫游成功率；阈值 0.2-2s，默认 0.2s）
   - Coverage（信号高于阈值的时间占比；阈值 -90~-55dBm，默认 -66dBm）
   - Available Capacity（RF 信道可用时间占比；阈值 10%-50%，默认 10%）
   - Device Uptime（设备在线率；交换机仅有这一项 QoE 指标）
2. **网络分析**——从设备视角回答"网络健康吗"：信道分布与利用率 → AP/交换机 CPU/内存/闪存健康 → 单设备下钻（客户端数、吞吐、发射功率、端口帧统计/PoE）。
3. **客户端分析**——从负载视角回答"谁在用、怎么用"：连接数时间曲线、频段/AP/SSID/OS 分布、吞吐消费、会话时长、每用户设备数；用于判断加 AP、换型号、查异常流量。

## A1 · 书中案例（Lab 精要）

Lab 前提：树莓派先连上 Employee SSID 产生数据。① QoE：Network > Analytics > QoE，确认站点选择，逐项看六指标，Configure Thresholds 调阈值，More details 看失败分类器（时间窗扩到 Last 7 days，最近一小时没有失败样本时看不到失败分类器）。② Network Analytics：点具体信道跳转到使用该信道 AP 的 RF Details。③ Client Analytics：按小时点选柱状图，下方各分布组件联动。（p156-163）

## A2 · 触发场景（含与相邻 skill 的区分）

- 用户投诉"上网慢/连不上/漫游断"，但不知道从哪查起 → 先走本 skill 的 QoE 仪表盘定位失败指标与分类器。
- 已定位到 AP 层面具体故障（如掉线、802.1X 失败、看不到 SSID）→ 转 stellar-troubleshooting-cli（CLI 排障清单）。
- 只是调整监控告警阈值、看报表 → 转 stellar-monitoring-ops。
- 语音场景的专门标准（-67dBm/SNR≥25）→ 转 stellar-vowlan。

## E · 可执行步骤

1. 打开 Network > Analytics > QoE，Filters 选站点、设备类型（AP 或交换机）、时间范围（建议先 Last 7 days）。
2. Thresholds 按站点核对/调整各指标阈值（参考默认：TTC 2s / Roaming 0.2s / Coverage -66dBm / Capacity 10%）。
3. Summary 区看六指标汇总与失败阶段占比，圈定异常指标。
4. 对异常指标点 More details 下钻：按连接模式/设备类型/OS/SSID 的失败会话明细，读失败分类器（DHCP、Association、Weak Signal、Asymmetry Downlink/Uplink、Wi-Fi Interference 等）定位原因。
5. 切 Network Analytics：先看全局信道分布与利用率，再设备过滤器切 AP 看健康（Health Thresholds 可改百分比），点单台 AP 看趋势、客户端数、吞吐、功率；交换机看帧统计/错误/PoE。
6. 切 Client Analytics：连接曲线 → 分布（频段/AP/每 AP 客户端数区间）→ 吞吐 → 时长 → 每用户设备数，判断是否粘 AP、是否需加 AP 或换型号。
7. 经 Shortcuts 跳转相关页面继续处理。

## B · 边界与陷阱

- 失败分类器要有失败样本才显示：时间范围太短（如最近一小时）会"看不到问题"，先扩窗到 7 天。
- 交换机只有 Device Uptime 一项 QoE 指标，别在交换机上找其他五项。
- 阈值是按站点配置的，多站点不能一刀切；阈值应对齐业务用途（参考 stellar-deployment-checklist 的场景化阈值 70%/20%/90%/25%）。
- QoE 是 Cirrus 云管专属指标体系，脱离 OmniVista Cirrus 不适用。

---
来源条目: f01, f02, f03, f04, c05, p01, p02, p03, p04, g01, g02, g03, g04, g05, g06, g07
