---
name: site-survey-remediation
description: 何时用：WiFi 整网表现不佳需要现场勘测（选被动/主动/预测）、排查覆盖盲区/干扰/布点问题并落地纠正动作时用本 skill。
source_book: DT00XTE478EN Stellar WLAN Advanced Troubleshooting
---

# WiFi 勘测与纠正措施：类型选型 · 三步法 · 五类发现 · 五类动作

## R · 原文引用

> Passive: Listen WLAN traffic, No authentication and 802.11 association, All frequencies are scanned, Detects Access Points, Measure signal strength, Measure noise. Active: Associate survey tool to (multiple) access point, Measure packets loss, retransmission, physical rates. Predictive: Simulation tool, Import site plan & RF characteristics of objects, No field measurements. Predictive: Pre-deployment, place new APs; Passive: Post-deployment, RF analysis; Active: Post-deployment, clients performance analysis. (p106-107)

> Step 1 - Get the floor plans: Identify potential issues: obstacles, walls, ceiling height; Identify areas where WiFi is required; Locate Access Point. Step 2 - Site Survey observation: Identify AP model same as original design? RF overlap - Co/Adjacent channel interference? Areas with no radio coverage? Step 3 - Corrective actions: Change AP model, Rework RF wireless design, Rework channel width, Remove lower data rates, Improve AP placement. (p114-117)

> Distance = 4 meters. 1 to 4 walls crossed. RSSI = -70dBm. Not enough for VoWLAN. Signal degrades when going through: Concrete (walls), Wood (doors), Metal (cabinet, shelves), Steel (building structure), Glass & Mirrors, Brick (fireplace), Water. (p110)

> Co-channel Interference. Adjacent channel Interference. - Loss of throughput -> Change AP channel. - Packets loss. - Corrupted data -> Change AP channel. (p112)

## I · 方法论骨架

**勘测类型选择矩阵**

| 类型 | 做什么 | 阶段 |
|---|---|---|
| Predictive 预测 | 导入平面图 + 物体 RF 特性做仿真、自动摆 AP，不做实地测量 | 部署前（新网/换网） |
| Passive 被动 | 只监听不关联，扫全频段，发现 AP、测信号强度与噪声 | 部署后（RF 分析） |
| Active 主动 | 勘测工具真实关联 AP，另可测丢包、重传、物理速率 | 部署后（客户端性能分析） |

选型口诀：排障时被动 + 主动组合使用。

**现场三步法**

1. **拿图纸**：标出障碍物/墙体/层高、所需覆盖区域（按高/中优先级）、AP 位置。
2. **勘测观察五项**：AP 型号与原设计一致？AP 间 RF 重叠造成同频/邻频干扰？无覆盖区域（AP 宕机 or 没布）？发射功率默认值还是定制值？AP 位置是否别扭？
3. **纠正动作五类**：换 AP 型号（更强天线/户外型）/ 重做 RF 设计（调功率、换信道）/ 收窄信道宽度抑干扰 / **移除低数据速率（逼终端贴近信号更好的 AP，常被忽略的优化项）**/ 改善布放。

**干扰三症状 → 处置**：吞吐下降、丢包、数据损坏 = 同频/邻频干扰 → Change AP channel；用 Ekahau / WiFi Analyzer 信道视图定位重叠信道。

**布点与材料**：AP 正对混凝土柱/墙 = 背后死区，遮挡墙两侧各布一台；实测 4 米穿 1-4 面墙 RSSI 即掉到 −70dBm（上网够、语音不够，语音需 −67dBm 以上）。衰减源清单：混凝土墙、木门、金属柜/货架、钢结构、玻璃镜子、砖砌体、水（鱼缸/浴室水汽）。天线类型匹配环境：走廊/长条用定向（小扇区），开放办公用全向（约 20 米整圆）；可外接天线的型号末位为 "2"。

## A1 · 书中案例

教材现场案例（p115-116）同时出现四类发现：无覆盖区域、缺 AP、遮挡区、发射功率仍是默认值 17dBm 未按覆盖调大——对应纠正动作为调功率 + 加 AP + 挪 AP 的组合。

## A2 · 触发场景（含与相邻 skill 的区分）

- 整网/整区域"表现不佳"（覆盖、干扰、布点问题）→ 本 skill；单客户端连不上/掉线 → `client-connection-trouble`；漫游切换失败 → `wireless-rf-roaming-trouble`。
- 本 skill 的输出（勘测发现）会调用其他 skill 的动作：干扰换信道与 RF profile 相关、功率调整在 RF profile 中落地。

## E · 可执行步骤

1. 按阶段选勘测类型（部署前预测；部署后被动查 RF、主动查性能；排障组合两者）。
2. 拿平面图标三样：障碍物、优先覆盖区、AP 位置。
3. 实地按五项观察清单逐项记录（型号/干扰/盲区/功率默认值/位置）。
4. 干扰三症状确认后用 Ekahau/WiFi Analyzer 找重叠信道。
5. 按五类纠正动作出整改方案：换型号 → 调 RF 设计 → 收窄信道宽度 → 砍低速率 → 改布放；遮挡墙两侧补 AP。
6. 语音场景按 RSSI≥−67dBm 验收覆盖，按材料衰减清单高估穿损留裕量。

## B · 边界与陷阱

- 默认发射功率 17dBm 只是出厂值，覆盖不足时要按勘测结果调大，别当"标准配置"不动。
- "移除低数据速率"反直觉但是正经优化项：低速率留着会让终端黏在远端差信号 AP 上。
- 天线类型装反（定向进开放区、全向进走廊）造成"一半区域没信号、另一半过剩"，盲区先查天线。
- 距离近不代表信号好：4 米穿几面墙就到 −70dBm，语音场景必须留裕量。
- 预测勘测不做实地测量，不能替代部署后的被动/主动验证。

---
来源条目: f06, f07, ce25, ce26, ce27, ce28, ce29, ce30（术语 g24 同频/邻频干扰, g25 三类勘测, g29 Ekahau, g35 Wi-Fi 代际）
