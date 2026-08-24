---
name: site-survey-troubleshooting
description: 何时用：网络性能不达标的现场处置——勘测类型选型（预测/被动/主动）、四类信号杀手归因、三步排障法与纠正措施。
source_book: DT00XTE360EN ACFE WLAN Basic Deployment
---

# 勘测与现场排障三步法

## R · 原文引用

> "Passive: Listen WLAN traffic; No authentication and 802.11 association; All frequencies are scanned ... Active: Associate survey tool to (multiple) access point; Measure packets loss, retransmission, physical rates ... Predictive: Simulation tool; Import site plan & RF characteristics of objects" (p529)

> "Step 1 – Get the floor plans: Identify potential issues: obstacles, walls, ceiling height … Step 2 – Site Survey observation: Identify Access Point model: same as original design? Identify RF overlap … Identify areas with no radio coverage … Step 3 – Corrective actions: Change Access Point model … Rework RF wireless design … Improve AP placement" (p537-540)

> "Signal degrades when going through: Concrete (walls), Wood (doors), Metal (cabinet, shelves…), Steel (building structure), Glass & Mirrors, Brick (fireplace), Water (liquid: fish tank; vapor: bathroom)" (p533)

## I · 方法论骨架

**1. 勘测类型选型矩阵（按项目阶段）**

| 类型 | 做法 | 测什么 | 适用阶段 |
|---|---|---|---|
| Predictive | 仿真：导入平面图+材质衰减建模，自动摆 AP | 覆盖预测 | 新建网/换网前规划 |
| Passive | 只听不发（不关联不认证），扫全频段 | AP 发现、信号强度、噪声 | 部署后射频体检/干扰 |
| Active | 勘测终端实际关联 AP | 被动指标+丢包、重传、物理速率 | 部署后客户端性能评估 |

排障项目用被动+主动组合。工具：Ekahau Site Survey（Windows）、WiFi Analyzer（Android）。
判读标尺（ALE）：dBm=RSSI−96；约 RSSI<20（−76dBm 以下）Bad 不宜音视频；>30 为 Desired。

**2. 四类信号杀手（归因清单）**
1. AP 摆位：正对墙/柱自己挡自己——障碍物两侧各放一台
2. 材质衰减：混凝土/木门/金属柜架/钢结构/玻璃镜面/砖/水体；实例：4 米穿 1-4 面墙 RSSI 掉到 −70dBm，不够 VoWLAN
3. 天线选错：定向=小扇区、全向=整圆，按覆盖形状选（外置天线 AP 型号尾数带 2，如 AP1322）
4. 同频/邻频干扰：吞吐下降、丢包、数据损坏——换信道

**3. 现场三步法 SOP**
- Step 0：定义问题（Where/When/Who/How 圈定范围与测试点）
- Step 1：拿平面图——标障碍物、需求区域（按优先级分级）、现有 AP 位置
- Step 2：实地观察五项——AP 型号与设计一致？AP 间 RF 重叠/同邻频干扰？覆盖空洞（AP 掉线/缺位）？发射功率是默认还是改过（默认 17dBm）？安装位置是否别扭？
- Step 3：纠正措施——换 AP 型号 / 改功率信道 / 收窄信道宽度 / 砍低速率逼终端贴近 AP / 挪 AP 或新增

## A1 · 书中案例（Lab 步骤精要）
- **c22/p526-540**：课程演示全流程——Predictive+Passive 组合开局 → Ekahau 被动勘测热图分析 → 按四类根因定位（摆位/材质/天线/干扰）→ 三步法出整改（含修改单 AP 发射功率、新增 Stellar AP、挪 AP 三个用例）→ 热图复验：干扰消除、盲区消除、RSSI 回推荐区间。

## A2 · 触发场景（含与相邻 skill 的区分）
- "Wi-Fi 慢/掉线/有死角"类投诉上门处理，或新建网前的勘测规划时用。
- **区分**：参数层调优（阈值/负载均衡/扫描）→ `rf-optimization-baseline`；漫游切换问题 → `roaming-rap-design`；认证连不上（有信号但进门失败）→ `ssid-authentication-suite` 的 CLI 链；本 skill 管"物理层与覆盖层的现场归因"。

## E · 可执行步骤
1. Step 0 用四问把模糊投诉收敛成可测问题与测试点。
2. 按项目阶段选勘测类型（新建=Predictive；体检=Passive；性能=Active；排障=组合）。
3. 拿平面图标注：障碍、需求区域分级、AP 位置。
4. 实地按五项观察清单逐项核对（型号/重叠/盲区/功率/位置）。
5. 归因到四类杀手之一，出对应纠正措施。
6. 复验：热图/实测 RSSI 回到 Desired 区间（参考 −65 以上理想、低于 −80 不宜音视频）。

## B · 边界与陷阱
- 覆盖问题不要用 RF 参数硬扛：Band Steering/负载均衡都假设覆盖对等，根因在覆盖就得改布放（与 rf skill 的陷阱互证）。
- "部分设备连不上"先查是否拿到 IP（DHCP 池满类似无线故障），再查无线层。
- 发射功率默认 17dBm，覆盖不足可加大，但加大功率也会放大同频干扰——与信道规划联动。
- 砍低速率会牺牲边缘弱终端体验，用于高密度场景逼终端贴近 AP，边缘覆盖区慎用。
- 天线类型错配在覆盖图上表现为"形状不对"的盲区，换天线前先核对定向/全向与型号尾数规则。

---
来源条目: f20, f21, f23, p64, c22, ce39 · 术语锚点: g36, g06, g40, g20, g47
