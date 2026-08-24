---
name: stellar-vowlan
description: 何时用：规划或部署无线语音（VoWLAN）——话机/软终端 Wi-Fi 覆盖、容量与漫游参数时用。
source_book: DT00XTE361EN Stellar WLAN Advanced Deployment
---

# VoWLAN 语音无线部署五阶段

## R · 原文引用

> "These are the major steps for the deployment of VoWLAN in a WLAN Stellar environment... Prepare / Plan / Design / Implement / Operate." (p306)

> "1 access point / 255 m²; Number of users per AP – Average of 20-25 users; ... Generally a -62dBm RSSI (or better) is required to ensure a correct roaming; 20 to 25 clients per Aps, providing 36 Mbps user throughput." (p307-308)

> "For VoWLAN deployment in 802.11ac: RSSI must be -67dBm (or better). Meaning RSSI ≥ 29. ... For VoWLAN deployment in 802.11AC: SNR ≥ 25." (p272-273)

## I · 方法论骨架

五阶段流程（Prepare → Plan → Design → Implement → Operate）：
1. **Prepare**：明确覆盖/带宽需求；站点勘测分析 RF 环境与干扰源；按 1 AP/255m²、每 AP 20-25 用户算 AP 数量与布放；识别需双 AP 冗余的区域。
2. **Plan**：定义语音服务与带宽、"Voice" WLAN 与安全等级；RF 管理优先 5GHz；容量 20-25 客户端/AP、36Mbps 用户吞吐；漫游开 802.11r/k/v，同能力设备放专用 SSID；保证 AP 侧网络冗余。
3. **Design**：相邻 AP 用非重叠信道；QoS 端到端 WMM 队列标 DSCP/802.1p；可选 DPI 语音管控；语音专用 VLAN；接入交换机千兆端口。
4. **Implement**：布线、语音服务器、RADIUS/DNS/DHCP、IMS3 批量管话机、话机 SSID 与 OmniVista 配置。
5. **Operate**：监控语音覆盖（SNR/RF 扫描）、VoIP 审计、性能、勘测（Ekahau/AirMagnet）、专业服务支持。

量化标准：802.11ac 下客户端 RSSI ≥ -67dBm（wlanconfig 显示值 ≥ 29）、SNR ≥ 25；正确漫游一般要求 -62dBm 或更好。RSSI 换算参考：10≈-86dBm（语音不可用）、20≈-76dBm（上网可用）、29≈-67dBm（语音推荐）、35≈-61dBm（理想）。

## A1 · 书中案例（Lab 精要）

教材语音部分为规划方法论章节（p300-311），无独立配置 Lab；可操作锚点：话机侧 NOE/SIP 终端（8118/8128/8158s/8168s）与 Rainbow/OTC 软终端经 IMS3 服务器批量部署管理（p302, p310）；话机支持 Ekahau RTLS 定位；排障时用 ssudo wlanconfig athXX list 直接读客户端 RSSI 值对照 29/-67dBm 门槛（p272-273）。QoS 映射沿用 WMM 推荐表（Voice 5/46-EF），见 stellar-ssid-advanced。

## A2 · 触发场景（含与相邻 skill 的区分）

- 园区要上无线话机/软终端，需要覆盖与容量规划数字 → 本 skill 直接套常数。
- 已部署语音但掉话/单通，怀疑信号或漫游 → 本 skill 量化标准（-67dBm/SNR 25）+ stellar-troubleshooting-cli 的漫游三判据。
- 语音之外的普通数据 WLAN 交付 → stellar-deployment-checklist（-67dBm 语音标准别错用到数据场景，会过度建设）。
- QoS 标记细节 → stellar-ssid-advanced。

## E · 可执行步骤

1. 需求确认：话机数量、并发呼叫、覆盖区域清单。
2. 勘测：RF 环境与干扰源扫描；标注需双 AP 冗余的区域。
3. 容量计算：面积/255m² 与 20-25 用户/AP 两个口径取大者定 AP 数；布放优先 5GHz。
4. 设计：非重叠信道复用图；语音专用 VLAN；交换机千兆接入端口；端到端 QoS（Voice 标 EF/5）。
5. SSID/漫游：建 Voice SSID，开 802.11r/k/v；同能力话机归专用 SSID。
6. 验收测量：wlanconfig 逐点读 RSSI（值 ≥29 即 ≥-67dBm）与 SNR ≥25；漫游路径上确认 -62dBm 重叠带。
7. 运营：SNR/覆盖例行监控，VoIP 审计，必要时 Ekahau/AirMagnet 复勘。

## B · 边界与陷阱

- 语音标准比数据严得多：-67dBm/SNR≥25 是 802.11ac 语音门槛，拿 -76dBm（值 20）覆盖报告交差会掉话。
- -62dBm 是漫游正确性的经验门限，规划重叠覆盖时按它留余量。
- 每 AP 超 25 个语音客户端就难保 36Mbps/用户，宁可加 AP。
- 802.11r/k/v 只对支持的话机有效：混接老旧终端时应分 SSID，别在公共 SSID 上强开。
- QoS 只标无线侧不够，端到端（VLAN/交换机）都要认 EF/5。

---
来源条目: f09, p15, p16, g47, g48, g49, g59
