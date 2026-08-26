---
name: Stellar Mesh 监控与排障（SSH：rfprofile.conf / iwlist / iwconfig / wlanconfig，链路质量与客户端指标）
description: 需要监控 mesh 集群运行状态、核对 RF 配置是否一致、查 mesh 链路信道与 DFS 雷达检测、评估链路质量（Link Quality/SNR/Bit Rate）、列出 mesh SSID 接口与客户端状态排障时使用。
source_book: Network Solution Guide — OmniAccess Stellar Bridging/Multi-Point Meshing Guidelines (AWOS 4.0.4 / OV2500 Cirrus 4.6.2)
---

## R（何时使用）
- mesh 链路性能劣化，需要看链路质量、信号强度、SNR、协商速率
- 核对各 AP 实际收到的 RF 配置是否与设计一致（rfprofile.conf）
- 排查信道利用率、UNII-2 DFS 子带雷达检测告警
- 确认 mesh SSID 接口（athXX）与所带客户端的速率/RSSI/能力

## I（核心理念)
**监控主战场在 AP 的 SSH 控制台**，Enterprise 模式下所有 mesh AP 的无线指标都从这里取（P27，<<<PAGE 27>>>）。前提：AP Group 预先启用 root 账户 SSH。

**链路质量三件套**：Link Quality（基于信号强度与 SNR 的链路健壮度）、Signal level、协商 Bit Rate（链路速率估计）。链路质量骤降说明前提没守住——距离超标、频率配置错、安装不当、室外 nLoS（P30，<<<PAGE 30>>>）。

**DRM 只在 root 生效**：mesh SSID 上远端客户端的动态射频管理由 root AP 统一处理，别在 mesh AP 上找 DRM 逻辑（P29，<<<PAGE 29>>>）。

## A1（决策要点）
1. **开启 SSH**（P27，<<<PAGE 27>>>）：`OV2500 -> Network -> AP Registration -> AP Group -> 选 mesh AP Group -> Edit`，SSH Login 对 root 账户启用并设密码
2. **核对 RF 配置**（P27-29，<<<PAGE 27>>>）：`cd /tmp/config && more rfprofile.conf`；重点字段：bandSteering/bandSteeringForce5g、LoadBalance、countryCode、airtimeFairnessAt2G/5G、perBandInfo（channelWidth 2.4G=20 / 5G=80、powerSetting、channelLists 如 [100,104,108,112]、chainmask、MuMIMO、highEfficiency、beaconInterval）
3. **监控信道**（P29-30，<<<PAGE 29>>>）：`iwlist athXX channel` 看当前信道与可用频率；UNII-2 DFS 子带的雷达检测会直接打在 AP 控制台（如 `_GOLSOH_Radar found on channel 52`）；据此精调信道设置优化 mesh 体验
4. **监控链路**（P30，<<<PAGE 30>>>）：`iwconfig athXX`（mesh backhaul 接口如 athap1）看 ESSID、频率、Bit Rate、Tx-Power、Link Quality（如 50/94）、Signal level（如 -76dBm）、Noise level
5. **监控 mesh SSID 接口**（P31，<<<PAGE 31>>>）：`iwconfig` 全量列出接口，找出双频承载客户端 SSID 的接口（示例 ath01=2.4GHz、ath11=5GHz，ESSID "SSID storage"）
6. **监控客户端**（P32，<<<PAGE 32>>>）：`wlanconfig athXX list` 看关联客户端的 TX/RX 速率、RSSI（含 MIN/MAX）、SNR、工作频段、能力（HT/VHT/MU）、关联时长、电源模式

## A2（细节速查表）
| 任务 | 命令/位置 | 关键输出 | 页码 |
|---|---|---|---|
| 开启 SSH | OV2500 -> Network -> AP Registration -> AP Group -> Edit；SSH Login=Enabled（root 账户 + 密码） | — | <<<PAGE 27>>> |
| RF 配置核对 | `cd /tmp/config; more rfprofile.conf` | bandSteering、countryCode、perBandInfo（channelWidth/channelLists/powerSetting/MuMIMO/highEfficiency） | <<<PAGE 27-29>>> |
| 信道监控 | `iwlist athXX channel` | 当前信道（如 Channel 104 / 5.52GHz）、可用频率列表 | <<<PAGE 30>>> |
| DFS 雷达检测 | AP 控制台直接显示 | `Radar found on channel 52 (5260MHz)` | <<<PAGE 30>>> |
| 链路监控 | `iwconfig athap1`（backhaul 接口） | ESSID、Bit Rate（如 780Mb/s）、Tx-Power、Link Quality=50/94、Signal=-76dBm、Noise=-95dBm | <<<PAGE 30>>> |
| SSID 接口发现 | `iwconfig` 全量 | ath01（11ng，2.4G）、ath11（11ac，5G）等 | <<<PAGE 31>>> |
| 客户端监控 | `wlanconfig athXX list` | ADDR/AID/CHAN/TXRATE/RXRATE/RSSI/SNR/HT-VHT-MU 能力/ASSOCTIME/电源模式 | <<<PAGE 32>>> |
| DRM 生效层级 | root AP 统一处理 mesh SSID 远端客户端 | — | <<<PAGE 29>>> |
| 链路质量口径 | 信号强度 + SNR；Bit Rate 为速率估计 | 质量骤降→查距离/频率/安装/nLoS | <<<PAGE 30>>> |

## E（场景案例）
- 书中实例链路：athap1（ESSID Stellar-MESH，5.52GHz/信道 104，802.11ac，Bit Rate 780Mb/s，Link Quality 50/94，Signal -76dBm）——Link Quality 50/94 说明链路尚可但有衰减（P30，<<<PAGE 30>>>）
- 同 AP 上客户端接口对比：ath11（5GHz 客户端）Link Quality 94/94、Signal -23dBm 远好于 ath01（2.4GHz）的 53/94、-75dBm，可据此引导双频终端优先走 5GHz（P31，<<<PAGE 31>>>）
- 客户端清单实例：2.4GHz 客户端 72M 收发速率、RSSI 63、SNR 63、11NG_HT20 模式、无 VHT/MU 能力（P32，<<<PAGE 32>>>）
- 信道调优闭环：iwlist 看各信道利用率 + 控制台 DFS 检测记录 → 调整 channelLists（P29-30，<<<PAGE 29>>>）

## B（限制与坑）
- **SSH 不预开就没法监控**——必须在 mesh 专用 AP Group 里提前启用 root 账户 SSH（P27，<<<PAGE 27>>>）
- Link Quality 骤降基本都指向前提违规（距离、频率、安装、nLoS），先查物理层再怀疑软件（P30，<<<PAGE 30>>>）
- Bit Rate 是链路速率估计值，拿来对比排障可以，别当合同承诺速率（P30，<<<PAGE 30>>>）
- DRM 只在 root 层处理 mesh SSID 的远端客户端，mesh AP 上看不到独立的 DRM 行为（P29，<<<PAGE 29>>>）
- mesh 接口命名要分清：backhaul（athap1 类）与客户端 SSID 接口（ath01/ath11 类）监控命令相同但含义不同，看错对象会误判（P30-31，<<<PAGE 30>>>）
- rfprofile.conf 是 AP 实际生效配置，与 OV2500 设计值对不上时以排障视角先看这份文件（P27-29，<<<PAGE 27>>>）

来源：OmniAccess Stellar Bridging/Multi-Point Meshing Guidelines，p27-32（Monitoring Mesh：RF 配置/链路/SSID/客户端）
