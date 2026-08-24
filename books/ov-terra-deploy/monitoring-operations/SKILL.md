---
name: 监控运维
description: 当需要日常运维 OmniVista 管理的网络：QoE 分析、Heat Map、软件升级计划、备份管理、设备排障与支持信息收集时使用。
source_book: DT00XTE317 OmniVista Cirrus/Terra Deployment and Configuration
---

## R（触发场景）
- 客户抱怨无线体验差，需要 QoE 指标定位（连接失败原因、弱信号、信道利用率）
- 需要规划 AP/交换机软件批量升级窗口
- 需要配置定期备份、给 TAC 收集支持信息、远程重启/重置设备

## I（核心理念）
运维的三个抓手：①体验度量——QoE Analytics 用连接/漫游/信号/信道指标及失败原因量化体验，Heat Map 可视化覆盖；②变更管理——Scheduled Upgrade 分窗口分批升级，Golden Configuration 周期审计配置合规；③故障处置——Ping/Reboot/Reset、support info 收集、activation log 排查构成标准动作集。

## A1（行动框架）
1. **QoE 分析**：看连接时间/漫游时间（失败原因分类 Association/Authorization/DHCP/Portal）、平均 RSSI（Weak Signal/Asymmetry）、信道利用率（干扰/客户端数）、设备平均 uptime（<<<PAGE 296>>><<<PAGE 297>>>）。
2. **Heat Map**：按站点/AP 展示覆盖与客户端密度（红高/黄中/绿低）（<<<PAGE 337>>>）。
3. **软件升级计划**：Set occurrence、starting and end date → Select Site / AP Group(s) / Access Point → Software version（全 AP Group 统一或按组）→ Review and Create Upgrade Schedule；管理操作 Execute/Activate/Deactivate/Edit/Delete（<<<PAGE 356>>><<<PAGE 357>>>）。
4. **备份管理**：Create an Instant Backup（Security files 可选）；Scheduled Backups，Scope 可选 switch/site/floor；文件管理 View/Download/Delete（<<<PAGE 355>>>）。
5. **Golden Configuration 审计**：周期审计与即时审计，无偏离则 Compliant（<<<PAGE 195>>><<<PAGE 196>>><<<PAGE 351>>>）。
6. **设备排障**：Ping Device（及 From device）、Reboot Device、Reset Device（仅 AP）、Collect support info、Troubleshoot device、View activation log；AP 下载 tar.gz 快照（配置+日志），交换机选 Swlog/Cfg/Tech-support 文件下载 tar.gz（<<<PAGE 348>>><<<PAGE 358>>><<<PAGE 359>>>）。

## A2（进阶应用）
- 升级窗口设计：per AP Group 指定不同版本，实现灰度升级（<<<PAGE 357>>>）。
- 排障组合拳：QoE 定位问题域（如 Authorization 失败）→ Heat Map 确认位置 → Collect support info / tar.gz 快照取证（<<<PAGE 296>>><<<PAGE 337>>><<<PAGE 358>>>）。
- 激活类问题看 Activation Log 与状态机（Device Catalog，<<<PAGE 146>>><<<PAGE 147>>>）。

## E（实证案例）
- **案例 1**：用户反馈"连不上 Wi-Fi"，QoE Analytics 失败原因显示 Authorization 阶段失败——问题在认证服务器/凭证而非射频（<<<PAGE 296>>><<<PAGE 297>>>）。
- **案例 2**：批量升级 500 台 AP：建 Upgrade Schedule，先升级试点 AP Group，确认后再全量 Execute（<<<PAGE 356>>><<<PAGE 357>>>）。
- **案例 3**：开 Case 前 TAC 要日志：AP 侧 Collect support info 下载 tar.gz 快照（配置+日志）；交换机侧选 Swlog/Cfg/Tech-support 打包 tar.gz（<<<PAGE 358>>><<<PAGE 359>>>）。

## B（边界与陷阱）
- **Heat Map 最低 3 AP**：少于 3 台 Stellar AP 无法生成热图（<<<PAGE 337>>>）。
- **Reset 仅限 AP**：Reset Device 不适用于交换机（<<<PAGE 358>>>）。

## 来源
- principles·QoE 分析指标与失败原因分类（<<<PAGE 296>>><<<PAGE 297>>>）
- principles·Golden Configuration 合规检查（<<<PAGE 195>>><<<PAGE 196>>><<<PAGE 351>>>）
- cases·软件升级计划（<<<PAGE 356>>><<<PAGE 357>>>）
- cases·备份管理（<<<PAGE 355>>>）
- cases·设备排障与支持信息收集（<<<PAGE 348>>><<<PAGE 358>>><<<PAGE 359>>>）
- counter-examples·Heat Map 至少需要 3 个 AP（<<<PAGE 337>>>）
