---
name: rf-optimization-baseline
description: 何时用：RF Profile 创建下发与回退、抄官方参数基线（负载均衡/扫描/信道功率）、RSSI 判读，以及 RF 调参引发的隐蔽故障处置。
source_book: DT00XTE360EN ACFE WLAN Basic Deployment
---

# RF 管理与优化基线（参数推荐表 + 闭环流程）

## R · 原文引用

> "Smart Load Balance / Band Steering: Enable ... Signal Strength/Client SNR Threshold: Keep default threshold. Low value recommendation is 10, many weak client can associated, overall throughput is low. High value recommendation 25, weak client cannot associate, overall throughput is better. ... Channel & Power: Auto Mode ... Channel Width: Keep Default settings, Narrow width for dense AP deployment, Large width for sparse AP deployment" (p451)

> "The RF profile is contained in the Provisioning configuration of your AP Group. This is where we are changing it. ... Assign the default RF Profile back to the Provisioning Configuration associated to your AP Group" (p463)

> "During scanning wireless clients are impacted – no 802.11 data. Scanning is required for WIPS ... Default interval = 20 sec – Range 5-10800 sec; Default Duration = 50 ms – Range 50-110 ms" (p448)

> "To function properly, band steering generally assumes that the coverage areas on both the 2.4 GHz bands and 5 GHz bands are the same ... band steering will prove problematic if coverage on 5 GHz is significantly weaker and has coverage holes" (p459)

## I · 方法论骨架

**1. RF Profile 闭环：创建 → 绑定 → 验证 → 回退**
- 创建：通用设置（国家码）→ Smart Load Balance 段 → Per Band Info 按频段细配
- 绑定：AP Group > Provisioning Configuration 换 RF Profile 生效；Device Catalog 可对单 AP 覆盖
- 验证：客户端行为 + QoE > Analytics（关联失败列表）+ `cat /tmp/config/rfprofile.conf` + `cat /proc/kes_syslog | grep ACS`
- 回退：Provisioning Config 换回 Default RF Profile

**2. 架构原理（DRM 分布式射频管理）**
每 AP 空口做邻居发现、LAN 侧共享射频上下文（信道利用率/干扰/客户端数/功率）；每台 AP 自主采取 RF 动作（尝试-等待-重试），作用域限邻居，不依赖 AP Group 或管理 VLAN。ACS/APC 基于该上下文自动决策。

**3. 官方参数基线表（可直接照抄）**

| 参数 | 推荐值/状态 | 备注 |
|---|---|---|
| Band Steering | Enable（前提双频覆盖对等） | 默认关，见陷阱 |
| 关联 RSSI/SNR 阈值 | 低 10 / 高 25 二选一 | 10 放弱终端拉低吞吐；25 拒弱终端保吞吐 |
| 关联 RSSI（负载均衡版） | 2.4G=5，5G=10 | p445 推荐 |
| Dynamic Load Balance | Enable | |
| 背景扫描 | Enable（仅 WIPS 所需），间隔 20s / 时长 50ms 保持默认 | |
| Voice and Video Awareness | Enable | 检测 SIP/H.323 跳过扫描 |
| SGI | Enable（约 +11% 速率） | 环境差/客户端密集时关 |
| 信道/功率 | Auto（ACS/APC） | 优于静态 |
| 信道宽度 | 保持默认；密集=窄、稀疏=宽 | 2.4G 20(默认)/40；5G 20/40(默认)/80/160；6G 20-160 |
| 功率范围 | 3-23dBm（或 Auto） | |
| 最小数据速率 | 2.4G=12、5G=24、6G=24 Mbps | Smart Air Share |
| 频段引导差值阈值 | 10 | 5G-2.4G 客户端数差 |
| 信道过载定义 | 1 分钟平均介质利用率 >70% | |

**4. RSSI 判读标尺（ALE 专属）**
dBm = RSSI − 96（RSSI 10=−86dBm、20=−76、43=−53）。低端（约 RSSI<20）Bad 不宜音视频；>30 为 Desired。口径注意：Cirrus 显示平均值，AP CLI 为瞬时值。

**5. 开关语义**
- Client-aware 开：ACS 有在线客户端不换信道；关：换到更优信道但打断客户端
- MU-MIMO：AP 同时多用户通信；High Efficiency 关闭时 11ax AP 降级 VHT
- Exclude MAC OUI：把扫描枪/MIPT 话机等排除在 Band Steering 之外

## A1 · 书中案例（Lab 步骤精要）
- **c18/p456-466**：建 My_RF_Profile（FR-France）→ 读客户端 RSSI（-41dBm=51）→ Association RSSI Threshold 全频段设 90 保存 → 经 My-Provisioning-Config 下发 → 客户端无法关联，QoE 关联失败列表显示 "RSSI threshold not met" → 改回 Default RF Profile 恢复。

## A2 · 触发场景（含与相邻 skill 的区分）
- 网络已上线，要做射频调优、设阈值、开负载均衡/扫描，或调参后出现"全网连不上/闪断/性能下降"时用。
- **区分**：终端漫游行为与跨 AP 切换 → `roaming-rap-design`；WIPS 依赖扫描但安全分类策略 → `wips-security-deployment`；现场覆盖差/盲区的勘测归因 → `site-survey-troubleshooting`；本 skill 管"参数层"。

## E · 可执行步骤
1. 先抄基线表起步，仅按业务取舍改阈值（10 vs 25 类权衡）。
2. 任何修改走闭环：改 Profile → 换绑 Provisioning → QoE 验证 → 异常即回 Default。
3. 开 Band Steering 前确认双频覆盖对等；做不到就配 Exclude MAC OUI 或不开。
4. 语音视频网络保持 Client-aware 开启、Voice/Video Awareness 开启。
5. 阈值类变更渐进设置，变更后立即看 QoE 关联失败数。
6. 深入验证用 AP CLI：rfprofile.conf 看下发值、kes_syslog grep ACS 看选信道日志。

## B · 边界与陷阱
- Band Steering 默认禁用有原因：5G 覆盖弱/有洞时把终端逼进弱信号区；Force 5G/6G 更是 2.4G 关联直接被忽略（ce24）。
- 关联 RSSI 阈值设高于客户端信号=全网拒联，隐蔽全局故障；变更后用 QoE 验证并回退（ce25）。
- 扫描与性能互斥：扫描期不传数据；保默认 20s/50ms 平衡点，高要求场景用专用扫描 AP（ce26）。
- Client-aware 关闭时 ACS 换信道打断在线客户端，语音/瘦终端闪断（ce27）。
- Band Steering/负载均衡类功能都假设覆盖对等——覆盖问题回到勘测解决，不要用参数硬扛。

---
来源条目: f16, f17, p47, p48, p49, p50, p51, p52, p53, p54, p55, c18, ce24, ce25, ce26, ce27 · 术语锚点: g45, g18, g47, g49, g50, g09, g08
