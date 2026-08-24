---
name: network-advisor-aiops
description: 何时用：向运维负责人论证 AI 运维价值、报 Network Advisor 订阅价格或核对部署门槛时。
source_book: DT00XPS288EN Stellar WLAN Presales
---

# Network Advisor AI 运维（价值叙事 + 定价 + 隐性成本）

## R · 原文引用

> "Identify: Detect issues/anomalies & trigger immediate alert. Understand the normal network behavior with Artificial Intelligence & Machine Learning. Mitigate: Propose a solution & the ability to fix the issue in one tap. Optimize: Network fine tuning for better quality of experience. Leverage Rainbow CPaaS."（p227）

> "WHERE CAN THE ALE OMNIVISTA NETWORK ADVISOR HELP YOU? Network Issues Lifecycle … Facilitate the capture of information. Audit the configuration. Continuous Data Collection. Early Detection. Instantaneous intervention. Minimize impact & side effects."（p228）

> "NETAD-AP-1Y Network Advisor - 1 year subscription for one OmniAccess Stellar Access Point 50 USD 48 EURO; NETAD-SWITCH-1Y … 100 USD 96 EURO."（p231）

> "Virtual Appliance to be acquired separately (not sold by ALE) … License duration start decreasing as soon as they have been activated. A 30 days grace period is attached … Limits: 2000 Network devices."（p230/p232）

## I · 方法论骨架

**三循环价值叙事**：Identify（AI/ML 学正常行为、预置异常库（持续更新，p219-220 实列 17 个具名异常）即时告警）→ Mitigate（Rainbow/Teams 气泡一键修复或自动纠正）→ Optimize（微调体验 + Rainbow CPaaS 连接应用与其他 AI）。按客户痛点选切入循环。

**问题生命周期四阶段映射**（对运维负责人最有效）：事前持续采集+配置审计 → 早期检测+管理员通知 → 事中即时干预、最小化影响 → 事后主动采集支撑关单。把能力摆到客户工作流时间轴上，而非罗列功能。

**定价（每个 IP 一份 License，牌价）**：

| PN | 1Y | 3Y | 5Y |
|---|---|---|---|
| NETAD-AP | $50 / €48 | $100 / €96 | $150 / €143 |
| NETAD-SWITCH / NETAD-TP | $100 / €96 | $200 / €191 | $300 / €286 |

报价锚点：1 年订阅约占总网成本 **1.8%**。独立服务，不需要 OV Cirrus/2500。

## A1 · 书中案例

- 完整报价演练（p233）：50 台 AP1311（€696/台）+ 42 台交换机（2×6900X24-F + 40×6360-P24X）硬件 €244,728；订阅 NETAD-AP-1Y×50 + NETAD-SWITCH-1Y×21 = €4,416 ≈ 1.8%（注意：42 台交换机只订了 21 份许可）（c17）。

## A2 · 触发场景（含与相邻 skill 的区分）

- 触发：客户抱怨"出问题才发现"；运维工具选型；给整网方案加 AI 运维项并报价。
- 区分：本 skill 管 Network Advisor 独立产品；网管平台（OV2500/Cirrus）及其 License 去 `license-quotation`。

## E · 可执行步骤

1. 按客户痛点选切入循环（被动救火→Identify；关单慢→生命周期论证）。
2. 盘设备数：AP 数 × €48 + 交换机/第三方数 × €96（1 年），对总网价算占比（参考 1.8% 锚点）。
3. 核对版本门槛：OS 6xxx/9xxx ≥ AOS 8.7.R2、2xxx ≥ 5.2.R1、AP ≥ AWOS 4.0.3 MR-3。
4. 报价附三张检查单：版本核对、虚拟机规格（四核/8GB/50GB 自购）、激活时机。
5. License 在客户上线节点再激活（激活即倒计时，30 天宽限）。

## B · 边界与陷阱

- 四类隐性成本：虚拟机自购、老设备先升版、2000 设备上限、激活即倒计时（ce21）。
- 牌价无区域折扣，区域价另询；超 2000 台不推（ce21/ce23）。
- "40+ 预置异常"表述未获原文支持，引用统一说"预置异常库（持续更新）"（verified.md 笔误标注）。

---
来源条目: f16, f17, p35, c17, ce21；glossary: Network Advisor、Rainbow、CPaaS 相关词条
