---
name: Voice over WLAN 部署
description: 当需要规划/部署 VoWLAN（语音覆盖勘测、AP 密度、QoS 映射、漫游与 802.11r/k/v、话机容量）或优化语音质量时使用。
source_book: DT00XTE310 OmniSwitch LAN Access & OmniAccess Stellar WLAN Express
---

## R（触发场景）
- 要为 8158s/8168s WLAN 话机或 Rainbow/OTC 软终端规划 Wi-Fi 语音覆盖
- 通话出现断续、漫游掉线、单向通话，需要按语音指标门限排障
- 需要决定 802.11r/k/v 开不开、2.4G 还是 5G、RAP 还是本部 AP

## I（核心理念）
VoWLAN 是"覆盖设计 + QoS + 漫游"三件事：覆盖按 -70dBm 小区交叠 8dB 设计，QoS 把 Voice 映射到 WMM/802.1p 6 / DSCP 46，漫游靠 802.11r/k/v 与 CNCS 上下文判定 L2/L3。语音对延迟、抖动、丢包、重传有硬门限，规划阶段就要算清 AP 密度与每 AP 语音流数。

## A1（行动框架）
1. **按五阶段方法论推进**：Prepare → Plan → Design → Implement → Operate（<<<PAGE 252>>>、<<<PAGE 964>>>）：先识别语音与音视频用途，运营阶段持续监控维护。
2. **Preparation 现场勘测**：Site survey → 分析 RF 环境 → 找干扰源；容量基准：办公区 1 AP / 255 m²、每 AP 平均 20-25 用户（<<<PAGE 253>>>）。
3. **RF 门限设计**（<<<PAGE 928>>>-<<<PAGE 931>>>）：覆盖要求 RSSI ≥ -70dBm；漫游要求 -62~-64dBm；AP 边界交叠约 8dB；SNR ≥ 25dB、Noise < -92dBm、RSSI > -67dBm。
4. **QoS 映射**：Voice DSCP 46 → 802.1p 6；Video 40 → 4；BE 0 → 0；Background 8 → 1（<<<PAGE 874>>>、<<<PAGE 932>>>）。话机侧建议 Voice 流量 DSCP 46、Voice 信令 DSCP 26（<<<PAGE 933>>>）。
5. **容量核算**（<<<PAGE 892>>>）：AP13XX (11ax) 每流 400Kbps、最高 35 条语音流（18 并发 G.711/Opus NB）；AP12XX (11ac) 13Mbps、32 流；Rainbow Audio/Video HD 105Mbps（3Mbps/流）/35 流。
6. **验收指标**：往返时延 < 250ms、802.11 重传 < 15%、Jitter < 100ms、丢包 < 2%（MOS≈4 / R-value 80-90）（<<<PAGE 933>>>、<<<PAGE 1007>>>-<<<PAGE 1008>>>）。

## A2（进阶应用）
- **漫游机制**：802.11r Fast Transition 先握手换钥再漫游（over-the-air FT 为默认）；802.11k 邻居报告省去全信道扫描；802.11v 由 AP 主动建议漫游目标（<<<PAGE 938>>>-<<<PAGE 940>>>）。漫游类型判定：CNC 表中 VLAN 与目标 AP Access Role VLAN 一致 → L2 漫游，否则 L3（<<<PAGE 917>>>）。
- **L3 漫游隧道**：跨子网漫游时新 AP 向 Home AP 建 L2 GRE 隧道，用户 IP 不变且 QoS/ACL 策略保留（<<<PAGE 894>>>、<<<PAGE 843>>>）。
- **语音走 5GHz**：2.4GHz 受蓝牙/微波炉/雷达干扰，语音实现可行但不推荐（<<<PAGE 908>>>-<<<PAGE 909>>>、<<<PAGE 913>>>）。
- **Mesh 语音限制**：语音 mesh 最多 4 跳/4 方向，到达 mesh 点带宽 /3、每方向 /4，根 AP 约 15 台话机中转上限；Mesh 中 VoIP 只能 Best Effort（11r/PMK 限制）（<<<PAGE 899>>>）。
- **RAP 远程话机**：Tunnel 模式全流量走 VPN（AP1201H 加密性能约 100Mbps，本部同型 433Mbps）；Local breakout 本地流量不回传（<<<PAGE 904>>>）。

## E（实证案例）
- 智能手机 EIRP 不对称：手机 5GHz 仅约 11dBm，是 AP 的 1/8 距离短板；降 AP 功率迁就手机会导致 AP 数量暴涨，手机 VoWLAN 只能 Best Effort（<<<PAGE 931>>>）。
- 81x8s 话机兼容性：8158s/8168s 当前版本拒绝 AP 的 802.11v 请求，需按终端能力分 SSID（<<<PAGE 940>>>）。
- RAP 三禁区实例：总部勿用 RAP（VPN 隧道约束）、加密带宽约打 2.3 折、同地两台 RAP 间 8168s 不支持切换（<<<PAGE 904>>>）。

## B（边界与陷阱）
- **802.11r 兼容性**：不支持 11r 的设备可能无法关联 11r WLAN；ALE 建议为支持 11r/k/v 的设备单设 WLAN（<<<PAGE 938>>>）。
- **2.4GHz 信道聚合（HT40）反模式**：仅适合少数 AP 的热点，多 AP 大部署因 3 信道限制自扰（<<<PAGE 908>>>-<<<PAGE 909>>>）；语音勿走 2.4GHz（<<<PAGE 913>>>）。
- **RAP 禁区**：总部不建议部署 RAP；同地两台 RAP 间 8168s 无法 handover（<<<PAGE 904>>>）。
- 话机 1x1 单天线走视距+分集，MU-MIMO 空间流复用对语音终端帮助有限（<<<PAGE 912>>>）。

## 来源
- frameworks·F3 五阶段方法论（<<<PAGE 252>>>、<<<PAGE 964>>>）
- frameworks·F4 Preparation 工作框架（<<<PAGE 253>>>）
- principles·P4 MU-MIMO 原理（<<<PAGE 912>>>）
- principles·P20 802.11r/k/v（<<<PAGE 938>>>-<<<PAGE 940>>>）
- principles·P21 语音小区 RSSI 门限（<<<PAGE 928>>>-<<<PAGE 931>>>）
- principles·P22 智能手机 EIRP 不对称（<<<PAGE 931>>>）
- principles·P23 WMM/DSCP/802.1p 映射（<<<PAGE 874>>>、<<<PAGE 932>>>-<<<PAGE 933>>>）
- principles·P24 质量门限（<<<PAGE 933>>>、<<<PAGE 1007>>>-<<<PAGE 1008>>>）
- principles·P25 语音 AP 容量基准（<<<PAGE 892>>>）
- principles·P26 Mesh 带宽衰减（<<<PAGE 899>>>）
- principles·P19 L3 漫游 GRE 隧道（<<<PAGE 894>>>、<<<PAGE 843>>>）
- principles·P41 漫游判定逻辑（<<<PAGE 917>>>）
- principles·P42 RAP 两模式（<<<PAGE 904>>>）
- counter-examples·X12 802.11r 兼容性（<<<PAGE 938>>>、<<<PAGE 940>>>）
- counter-examples·X13 RAP 三禁区（<<<PAGE 904>>>）
- counter-examples·X16 2.4GHz 语音反模式（<<<PAGE 908>>>-<<<PAGE 909>>>、<<<PAGE 913>>>）
