---
name: rf-survey-tuning
description: 何时用：WiFi 覆盖差/信号弱/吞吐低时做勘测选型、现场观测与射频纠正，及 AP 硬件选型时。
source_book: DT00XTE455EN Stellar WLAN Express
---

# 射频勘测与调优（含 AP 硬件选型）

## R · 原文引用

> "Predictive: Pre-deployment, place new APs. Passive: Post-deployment, RF analysis. Active: Post-deployment, clients performance analysis." (p164-165)

> "Step 2 – Site Survey observation: Identify Access Point model: same as original design? Identify RF overlap… No radio coverage… transmission power: Default or customized value? Step 3 – Corrective actions: Change Access Point model… Rework RF wireless design… Rework channel width… Remove lower data rates… Improve AP placement." (p172-175)

> "Distance = 4 meters. 1 to 4 walls crossed. RSSI = -70dBm. Not enough for VoWLAN. Signal degrades when going through: Concrete (walls), Wood (doors), Metal (cabinet, shelves,…), Steel (building structure), Glass & Mirrors, Brick (fireplace), Water (liquid: fish tank; vapor: bathroom)." (p168)

## I · 方法论骨架

1. **勘测类型 × 项目阶段映射**：部署前规划用预测勘测（软件仿真，导入平面图建模，无实测）；部署后看射频环境用被动勘测（只听不关联，测信号/噪声/发现 AP）；部署后看客户端真实性能用主动勘测（关联 AP，加测丢包/重传/物理速率）。工具：Ekahau（Windows）、WiFi Analyzer（Android）。
2. **现场排障三步 SOP**：Step1 拿平面图（标障碍/墙/层高，圈需 WiFi 区域，定位 AP）→ Step2 观测五问（型号是否与设计一致？RF 是否重叠？无覆盖是缺 AP 还是掉电？功率默认还是改过？位置是否别扭？）→ Step3 纠正措施。
3. **量化基准**：默认发射功率 17dBm（覆盖不足应上调）；4 米穿 1-4 堵墙 RSSI 掉到 -70dBm，已不够 VoWLAN；衰减大户按材质排序为混凝土/木材/金属/钢构/玻璃镜面/砖/水。
4. **覆盖优化五招**：换 AP 型号（更好天线/户外型）、重做射频设计（功率/信道）、收窄信道宽度压干扰、**删低速率逼终端贴近期 AP**（反直觉但最有效）、优化布放。
5. **性能五查（低吞吐/高时延）**：WLAN 限速 → 客户端模式与协商速率 → ACS 开关（没开就开）→ 空中干扰换信道 → ISP 带宽。由近及远，先排配置再怀疑空口与出口。
6. **选型基线**：SSID/客户端数按档位走（入门 16 SSID/512 客户端、中端 32/1024、高端 24-48/1536）；供电入门 802.3af 全功能、中高端 802.3at/bt；上联 1GE→10GE 分档；多数型号含 BLE5.1/ZigBee 射频与专用扫描射频。外置天线型号尾数为 2（如 AP1322/1362），全系标配内置全向天线。

## A1 · 书中案例

- 五点标注整改实例（p173-174，AP1511）：Ekahau 热图标出——（1）无邻频/同频干扰，正常；（2）无覆盖区，AP 缺失需补点；（3）遮挡区需挪位；（4）功率停在默认 17dBm，可上调；（5）挪 AP 优化覆盖。观测五问直接转成五条纠正动作。
- 布放错误实例（p167）：AP 正对混凝土墙/柱安装，墙后整片死区；修正为遮挡墙两侧各放一台，或死区补一台。
- 天线错配实例（p169）：长走廊用全向（能量一半浪费在走廊外）、开阔区用定向（扇区外没信号）——设备正常、覆盖形状错。

## A2 · 触发场景（含与相邻 skill 的区分）

- 触发："WiFi 表现不佳"类工单、新建网部署前规划、部署后验收、客户问"该买哪档 AP/要不要换 Wi-Fi 7"。
- 区分：认证失败、Portal 不弹等业务问题用 `ssid-portal-auth`；AP 不上电、拿不到 IP 等单体故障用 `ap-side-troubleshooting`；**回程要用无线解决**（桥接/组网）用 `bridge-mesh-deployment`。本 skill 管覆盖、信号、干扰、信道与硬件选型；同频/邻频干扰对策（换信道）与 ACS 检查也在此。

## E · 可执行步骤

部署前：
1. 做预测勘测：导入平面图与物体射频特性，自动布放 AP，出设计。
2. 按覆盖与容量需求选型：先定 SSID/终端规模档，再核供电（af/at/bt）与上联口；异形覆盖选尾数 2 的外置天线型号配定向天线。

部署后勘测（三步 SOP）：
3. 拿平面图标问题点、需求区、AP 位置。
4. 现场观测五问 + 热图工具（Ekahau/WiFi Analyzer）确认干扰类型。
5. 套纠正措施：补点/挪位/换型号、上调功率（基准 17dBm）、错开信道、收窄带宽、删低速率。

性能投诉：
6. 按五查清单走：限速配置 → 协商速率 → ACS 开启 → 换信道 → ISP 带宽。

覆盖验收：
7. 以 RSSI 门槛判定（-70dBm 不够 VoWLAN；语音级覆盖需更预留）。
8. 射频自动化开关按需启用：DRM/DFS/TPC、Band Steering、Load Balancing、黏性客户端规避、后台扫描、Rogue AP 检测。

## B · 边界与陷阱

- **AP 别装在障碍物正前方**：正对混凝土墙/柱会墙后整片死区，勘测优先标注"AP 在、信号无"的遮挡区。
- **天线类型按覆盖形状选**：定向覆盖小片定向区域，全向覆盖周边一圈；选错=设备正常但覆盖错位。
- **删低速率不是砍功能**：留着低速率只会让边缘终端赖在远端 AP 上，删掉才能逼漫游。
- 同频/邻频干扰症状（吞吐降、丢包、数据损坏）对策统一是换信道；设计期就应错开信道并收窄带宽。
- 引用校注：p169 全向天线原文 OCR 为 "No Area covered"，按幻灯片语义应为 No [Large]，沿用括号标注。
- Wi-Fi 代际话术基线（p35 语境）：Wi-Fi 4 1.2Gbps/WPA2 → Wi-Fi 6 9.6Gbps/WPA3 → Wi-Fi 7 46Gbps/320MHz/4096-QAM/MLO，可与 Stellar 型号谱系（Wi-Fi 5-7）直接映射。

---
来源条目: f07, f08, c14, p17, p18, p19, p21, p22, p23, p24, ce10, ce11, g13-g19, g26, g27, g28, g30, g31, g32, g35
