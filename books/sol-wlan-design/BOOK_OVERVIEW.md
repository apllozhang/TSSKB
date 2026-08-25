# BOOK_OVERVIEW — sol-wlan-design

## 书册构成（页码全册连续）

| DOC | 源文档 | 页码范围 | 性质 |
|---|---|---|---|
| 1 | ale-omniaccess-stellar-high-density-design-guidelines-en.pdf（OmniAccess Stellar 高密设计指南） | p1-44 | 体育场等极高密 Wi-Fi 的容量规划、AP 布置、端到端架构与微调模板 |
| 2 | omniaccess-stellar-wireless-fine-tuning-best-practices-techbrief-en.pdf（无线微调最佳实践） | p45-72 | Enterprise 模式下 RF 管理、负载均衡、漫游、组播/QoS 参数级微调手册 |
| 3 | omniaccess-stellar-wlan-specific-deployment-assistance-datasheet-en.pdf（部署协助服务数据表） | p73-75 | ALE 专业服务：预测勘测、辅导、培训认证的服务定义 |

## DOC 1 主线（p1-44）
- 需求分析驱动：5 万座体育场案例（50,000 座/20,000m²/每人 2 台设备），容量规划先行（p5-7）
- RF 面向容量：信道复用规则、强制 5GHz、低发射功率、20MHz 带宽、DFS 信道用于看台、Airtime Fairness、专用扫描射频（p8-9）
- 客户端画像：90% 双频、90% 手机、Wi-Fi 6 占 20-35%、2x2:2 MIMO 为主；SSID 矩阵（访客/媒体 VIP/售票/监控/员工/BYOD/IT），最多 7 个 SSID（p9-10）
- VHD 吞吐基线：HE20 单用户 80Mbps→60 并发时 37Mbps（25% VHD 折减）（p11）
- AP 计数标准：看台 120 终端/AP（150 座/AP）、其余 1 AP/100m²；30% 并发率；低性能 Wi-Fi 6 AP 不用于 >5000 座（p12-13）
- 安装策略：屋顶定向（AP1322+扇区天线，1 AP/180 座）、座椅下/扶手（NEMA 盒）、假天花板（p13-17）
- 端到端架构：双 6900 冗余核心（40G 保底/100G 峰值）、OmniVista 2500 HA、Cirrus 10 云分析（QoE/热图/密度图）、LAN 带宽公式（p18-25）
- 附录：访客 SSID 与监控 SSID 的 RF/SSID/AP Group 三级配置模板 + 454 AP 的 BOM（p27-44）

## DOC 2 主线（p45-72）
- RF 管理自动化优先：Calibration/Optimization，RDA（ACS+APC）默认开启勿关；宽信道（80/160MHz）带来 CCI 与 3dB 噪声惩罚（p48-51）
- 容量设计 vs 覆盖设计：ALE 主张容量型（更多 AP、更低功率、小蜂窝）；SSID×同信道 AP 的空口开销矩阵（12 AP 同信道×10 SSID = 50% 开销）（p50-53）
- Smart Load Balance：Band Steering（Apple 黑名单风险）、Force 5G、关联/漫游 RSSI 阈值（22/-74dBm、25/-71dBm）、最低数据速率（2.4G 12M/5G 24M）、Airtime Fairness（p54-56）
- 漫游与粘滞客户端：802.11k/v/r + OKC + FDB Update（p57-58）
- 组播/广播优化：IGMP Snooping、Broadcast Key Rotation、Broadcast Filter ARP（AP 作 ARP 代理）（p59-60）
- 语音 QoE：语音专用 5GHz SSID、背景扫描 110ms、DRM 信道细分（5G Low 8 信道/5G High 11 信道）、WMM↔802.1p/DSCP 映射（p61-63）
- OmniVista Cirrus 10.1 AI 分析：QoE 评分、信道分布 widget、Successful Connects 指标（p64-65）
- 附录 A/B/C：RF Profile、AP Group、SSID 三级参数默认值与推荐值对照表（p66-72）

## DOC 3 主线（p73-75）
部署协助专业服务：项目启动会、数据分析、Ekahau 预测勘测、现场勘测、部署辅导、DT00WTE278 课程与 ACSE 认证；前置条件（ACFE 认证、至少一次办公部署经验、HLD 已完成）、5 天交付、PS-PAER-5-NET 订购。

## 提取配额完成情况
- principles.md：P1-P46（目标 35-50 ✔）
- cases.md：C1-C21（目标 15-25 ✔）
- counter-examples.md：X1-X16（目标 12-20 ✔）
- frameworks.md：F1-F4（目标 3-6 ✔）
- glossary.md：55 条（目标 45-60 ✔）
