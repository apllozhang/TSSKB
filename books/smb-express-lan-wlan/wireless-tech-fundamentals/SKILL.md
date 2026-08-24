---
name: 无线技术基础（Wi-Fi 4/5/6/6E/7）
description: 当需要理解或向他人解释 Wi-Fi 代际差异（速率/频段/加密/MIMO）、Wi-Fi 6 高效率技术与 Wi-Fi 7 新特性、为选型和容量规划提供依据时使用。
source_book: DT00XTE310 OmniSwitch LAN Access & OmniAccess Stellar WLAN Express
---

## R（触发场景）
- 选型或答辩时被问"Wi-Fi 6 比 Wi-Fi 5 强在哪、Wi-Fi 7 值不值得上"
- 高密度场景需要理解 OFDMA/BSS Coloring/TWT 如何提升并发效率
- 看到终端规格 2x2 MIMO、4096-QAM 等术语需要准确解释

## I（核心理念）
Wi-Fi 每代升级都在五个维度同步演进：速率、频段、加密、信道宽度、调制与 MIMO。Wi-Fi 6 的核心是"高效率"（OFDMA 子载波调度、BSS Coloring 同频染色、TWT 目标唤醒时间），Wi-Fi 7 的核心是 MLO 多链路并发与 320MHz/4096-QAM 带宽扩张。

## A1（行动框架）
1. **代际对照速查**（<<<PAGE 49>>>）：Wi-Fi 4（802.11n）1.2 Gbps → Wi-Fi 5 3.5 Gbps → Wi-Fi 6 9.6 Gbps → Wi-Fi 7 46 Gbps；安全 WPA2→WPA3；信道宽度至 320MHz；调制 4096-QAM、OFDMA；MIMO 16x16 MU-MIMO。
2. **Wi-Fi 7 五大增强**（<<<PAGE 48>>>）：320MHz 更宽信道；MU-MIMO 至 16x16:16；MLO（Multi-Link Operation）提升可靠性/效率/性能；4096-QAM 原始速率 +20%；AFC（Automated Frequency Coordination）。
3. **Wi-Fi 6 高效率三件套**（<<<PAGE 911>>>）：OFDMA 接入、BSS Coloring、上下行多用户 MIMO 流（至 8）、TWT；Stellar AP 另有专用扫描射频与集成 Bluetooth/Zigbee（<<<PAGE 47>>>）。
4. **MU-MIMO 解读**（<<<PAGE 912>>>）：MxN 定义 M=发射天线数、N=接收天线数（如 2x2/3x3/4x4）；802.11ac/ax 起可在每条空间流上复用多用户。

## A2（进阶应用）
- **容量换算依据**：语音容量基准按代际区分——AP13XX（11ax）每流 400Kbps、35 条流；AP12XX（11ac）32 条流（<<<PAGE 892>>>）。
- **终端能力差异**：话机多为 1x1 单天线，走视距+分集，不吃 MU-MIMO 红利（<<<PAGE 912>>>）；手机 EIRP 低造成上下行不对称（<<<PAGE 931>>>）。
- **DFS（802.11h）**：5GHz 检测雷达自动避让信道，规划信道时纳入考量（<<<PAGE 927>>>）。

## E（实证案例）
- 用代际对照表说明为何语音项目至少选 11ax AP：AP13XX 35 条语音流 vs AP12XX 32 条且每流带宽更高（<<<PAGE 892>>>、<<<PAGE 49>>>）。
- Wi-Fi 6 三件套 + 专用扫描射频解释高密办公场景 Stellar 的并发能力（<<<PAGE 47>>>、<<<PAGE 911>>>）。

## B（边界与陷阱）
- HT40 信道聚合只适合 2.4GHz 少 AP 热点，多 AP 大部署因 3 信道限制自扰（<<<PAGE 908>>>-<<<PAGE 909>>>）。
- DFS 信道遇雷达会避让，时延敏感业务规划时注意（<<<PAGE 927>>>）。

## 来源
- principles·P1 Wi-Fi 代际性能对比（<<<PAGE 49>>>）
- principles·P2 Wi-Fi 7 关键技术（<<<PAGE 48>>>）
- principles·P3 Wi-Fi 6 高效率技术（<<<PAGE 47>>>、<<<PAGE 910>>>-<<<PAGE 911>>>）
- principles·P4 MU-MIMO 原理（<<<PAGE 912>>>）
- principles·P25 语音 AP 容量基准（<<<PAGE 892>>>）
- principles·P22 智能手机 EIRP 不对称（<<<PAGE 931>>>）
- counter-examples·X16 2.4GHz 信道聚合反模式（<<<PAGE 908>>>-<<<PAGE 909>>>）
