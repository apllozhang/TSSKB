---
name: vowlan-deployment
description: 何时用：无线语音（VoWLAN）项目做容量估算、漫游设计、终端盘点或答技术质疑时。
source_book: DT00XPS288EN Stellar WLAN Presales
---

# VoWLAN 语音部署（容量常数 + 五步法 + 终端门槛）

## R · 原文引用

> "VOICE OVER WLAN DEPLOYMENT STEPS: Identify the Voice usages … Prepare / Plan / Design / Implement / Operate."（p206）

> "Requirements for Voice: 1 access point / 255 m². Number of users per AP – Average of 20-25 users."（p207）

> "RF Management • 5GHz prefered (robust, best performance) • Capacity planning • 20 to 25 clients per APs, providing 36 Mbps user throughput • Generally a -62dBm RSSI (or better) is required to ensure a correct roaming."（p208）

> "Roaming assistance with 802.11r/k/v protocols • iOS 8 and above • Samsung Galaxy S7 minimum • S9 minimum for 802.11v. Voice over WLAN quality may vary depending on the hardware/Operating System."（p203）

## I · 方法论骨架

**五步部署法**（每步有输入输出物，可当 WBS）：

| 步骤 | 动作 | 输出物 |
|---|---|---|
| Prepare (p207) | 站点勘察、RF 环境分析、算 AP 数量布点 | AP 布点图 |
| Plan (p208) | 语音业务/安全级别/射频策略/漫游策略 | 规划书 |
| Design (p209) | 非重叠信道、WMM QoS、DSCP/802.1p 打标贯穿无线-边缘-核心、语音专用 VLAN、可选 DPI 语音管控 | 设计文档 |
| Implement (p210) | 布线、RADIUS/DNS/DHCP/IMS3、模板化下发话机 | 配置模板 |
| Operate (p211) | SNR 监控、VoIP 审计、Ekahau 复测 | 运维报告 |

**容量常数（可背底牌）**：1 AP / 255 m²；20-25 并发语音用户/AP；36 Mbps 用户吞吐；漫游阈值 RSSI ≥ -62dBm；5GHz 优先；能力相近终端规划专用 SSID；前台等关键位置做 AP 冗余。

**漫游协议适配矩阵**：OKC 仅 WPA2-Enterprise；802.11r 适用 Personal + Enterprise。跨 AP Group L3 漫游走 CTX 上下文同步。

**终端盘点**：专用话机 8118/8128/8158s/8168s（Ascom，NOE+SIP，8168s 工业级，OT8168s/OT8128 支持 Ekahau RTLS）+ IMS3 批量部署服务器；软终端 Rainbow UCaaS / OXO-OXE 集成 / 非 ALE 软电话——门槛 iOS 8+、三星 S7+、11v 需 S9+。

## A1 · 书中案例

- 千床医院 VoWLAN：保留 OXE 话机、AP1321 覆盖、双认证（c01）。
- 渡轮/酒店计划在 Wi-Fi 上承载 Rainbow VoIP（c02/c05）。

## A2 · 触发场景（含与相邻 skill 的区分）

- 触发：客户要上无线语音/无绳话机；没有勘察数据被追问"AP 数怎么算的"；BYOD 软电话质量扯皮。
- 区分：本 skill 管语音专属常数与五步法；一般数据场景（客房/场馆/会议室）的数量与配置去 `rf-scenario-baseline`；RTLS 定位细节去 `special-topologies`。

## E · 可执行步骤

1. 盘终端：专用话机（8118 系列）还是软终端（列机型/OS 清单，标 11r/k/v 支持）。
2. 快速估量：面积 ÷ 255 m² 得 AP 下限；用户数 ÷ 20-25 校核；按 36Mbps/用户核带宽。
3. 设计：5GHz 优先 + 专用 SSID + WMM/DSCP 端到端打标 + 语音 VLAN；认证方式套漫游矩阵（Personal→11r）。
4. 关键区域（前台/护士站）冗余覆盖。
5. 验收：按 -62dBm 漫游阈值 Ekahau 复测，VoIP 审计进交付标准。

## B · 边界与陷阱

- OKC/11r 选错认证方式漫游必卡：Personal 场景写 OKC 不受支持；部分老终端反而不支持 11r，必要时分 SSID 隔离（ce12）。
- 软终端质量随终端硬件/OS 浮动——方案加"终端准入清单"，旧终端不承诺语音体验，先划清责任（ce20）。
- 所有 Stellar AP 支持语音，但 AP 须升到最新版本（p204）。

---
来源条目: f14, f15, p26, p27, p28, p08, c01, c11, ce12, ce20；glossary: VoWLAN、802.11r/k/v、Rainbow、RTLS、WIPS/wIDS
