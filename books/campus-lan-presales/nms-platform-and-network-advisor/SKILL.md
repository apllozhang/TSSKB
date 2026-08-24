---
name: nms-platform-and-network-advisor
description: 按运维成熟度与数据驻留选 OV2500/Cirrus/Terra，配三层许可报价，并用 Network Advisor 三步循环讲 AI 运维。
source_book: DT00XPS281EN Campus LAN Presales
---

# 网管平台选型与 Network Advisor AI 运维

## R · 原文引用

> "OV CIRRUS OVERVIEW — SaaS model • Subscription based service • Zero Deployment/Zero footprint from Cloud … each OV tenant can support up to 5000 devices / up to 4000 APs" (p217)

> "OMNIVISTA 2500 NMS - LICENSE TYPES — Device Licenses: Alcatel-Lucent Enterprise Devices / Third Party Devices / OmniAccess Stellar APs. Starter Pack License is free (OV4-START-NEW)" (p194)

> "OMNIVISTA NETWORK ADVISOR — Identify: Detect issues/anomalies & trigger immediate alert … with AI & Machine Learning. Mitigate: Propose a solution & the ability to fix the issue in one tap. Optimize: Network fine tuning … Leverage Rainbow CPaaS" (p240)

## I · 方法论骨架

**平台选型判据：运维成熟度 × 数据驻留**

| 平台 | 形态 | 容量 | 适合 |
|---|---|---|---|
| OV2500 | 本地 VM（ESXi/Hyper-V/KVM），内嵌 UPAM Radius | 10000 设备 / 4000 AP / 5000 VM | 有机房/虚拟化、数据不出境、要本地管控 |
| OV Cirrus | 云 SaaS，零部署 | 单租户 5000 设备 / 4000 AP | 无机房无运维团队的 SMB/分支 |
| OV Terra | 大企业平台 | 教材未展开（待确认，投标另查） | 大企业场景 |
| Network Advisor | 独立订阅 AI 运维，不强依赖上述平台 | 2000 设备 | 叠加销售、续费理由 |

**报价三件套**：
- OV2500 三层许可：设备许可（ALE/第三方/AP 各一类，**VC 按物理成员数计**，三方按管理 IP 计）+ 服务许可（VM/Guest/BYOD/HA/Web 过滤）+ 扩展许可。Starter Pack（10 设备）免费起步，HA 许可主机侧一份即可。
- Cirrus 三维：功能档（Essential/Advanced/Core/Access Points）× 年限（1/3/5 年）× 服务包（Base/Premium/Business），经 Business Store/CPQ 或 eBUY 下单；Freemium 免费层（自注册、仅清单+一次性升级、许可上限 5000）作获客入口。
- Network Advisor 计价：**设备数 = 许可数**；牌价 AP $50/1y、$100/3y、$150/5y；交换机与三方设备 $100/$200/$300；锚点约为**网络总价的 1.8%**（列表价）；含 30 天宽限；版本门槛 AOS 8.7R2+（OS2xxx 5.2.R1+，AP AWOS 4.0.3 MR-3+）。

**AI 运维叙事三步循环**：Identify（AI/ML 学基线、异常即告警，预置 30-40+ 类异常：环路、端口抖动、DDoS、VC takeover、CPU/内存高等）→ Mitigate（一键/自动修复，手机端可操作，Rainbow/Teams 推送）→ Optimize（持续调优）。
**异议应对**（"已有网管为何还买"）：按网络问题生命周期四段介入——事前审计与持续采集、早期检测预防修复、瞬时介入降影响、事后主动取证（p241）。

**预测分析换算**（p272）：报表取最近 24h→预测 12h；7d→3d；4w→2w，用于容量规划配置。

## A1 · 书中案例

p246 书中算例：客户 50 台 Stellar AP + 42 台 OmniSwitch 订 1 年 Network Advisor——许可数直接等于设备数，追加在硬件 BOM 末尾，总价约为网络成本 1.8%。

## A2 · 触发场景（含与相邻 skill 的区分）

- 触发：客户问网管怎么选/怎么收费；"已有网管为何还买 Advisor"；续费 pitch 需要 AI 叙事。
- 区分：本 skill 管**平台选型与网管/AI 运维报价**；准入安全（UPAM 角色、QMR 隔离处置）在 `security-unified-access`；BOM 通用规则与 WWPL 在 `license-wwpl-pricing`。

## E · 可执行步骤

1. 两个问题定平台：数据能不能出域？有没有运维团队/虚拟化平台？
2. 数设备清单定基础许可，按用到的功能（BYOD/访客/HA）加服务许可行，VC 按物理台数乘。
3. Cirrus 报价三步：设备类型定档 → 预算定年限 → 服务级别定 bundle。
4. Advisor 叠加：按设备数加订阅行，用 1.8% 锚点验价，按 Identify→Mitigate→Optimize 讲故事。
5. 核对版本门槛与容量红线（2500 的 10000 设备、Advisor 的 2000 台、Cirrus 的 5000）。

## B · 边界与陷阱

- ce15：网管 license 不吃 VC 的账——VC of 4 就是 4 个许可；跨大版本 license key 不通用，OV2500 付费升级（UPG/U SKU）前先备份。
- Freemium 无配置能力，只能做清单与一次性升级，别当正式网管承诺。
- Terra 容量/许可细节书中未展开（待确认），投标前另查 datasheet。
- Advisor 牌价（USD/EUR 双币）随 WWPL 月度变动，报价前对当月表。

---
来源条目: f14, f15, f16, f17, f18, p25, p26, p27, p42, ce15, g25, g27, g28, g29
