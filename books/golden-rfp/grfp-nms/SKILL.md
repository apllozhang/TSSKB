---
name: OmniVista NMS 10.5 Golden RFP 精粹（SaaS 网管/多租户/UPAM 准入/QoE 分析/IoT 使能 72 条）
description: 投标网管平台、NMS 或统一管理项目时使用：OmniVista NMS 10.5（OVCX 云 + OVTX 本地双形态）Golden RFP 的 72 条编号需求精粹——微服务架构与订阅模式、多租户 MSP 分级、LAN 管理（GRE/VLAN/IP manager）、REST API 可编程、安全合规（RADsec/2FA/SSO）、QoE 与 30 天分析报表、内置 RADIUS+LDAP+DPI 到 L7 的 NAC 能力。
source_book: OmniVista NMS 10.5 Golden RFP (10.5.2, January 2026)
---

## R（何时用）
- 标书含网管平台章节，需要逐条应答 NMS 需求
- 客户问云管 vs 本地部署（Cirrus/Terra）能力差异
- 配合 LAN/WLAN 项目报统一管理与 NAC 模块（UPAM）

## I(核心理念)
OmniVista release 10 是一套代码两个交付形态：云上 OmniVista Cirrus 10（OVCX，区域数据中心托管）+ 本地 OmniVista Terra 10（OVTX），特性集等效。底层卖点：微服务架构免停机持续升级、"always up-to-date"自动补丁、订阅制按设备类别计费、有线无线"unified management"。文档共 11 章 72 条编号需求（1 Ordering → 11 NAC），每条 "The NMS platform shall …" + C/PC/NC。两处边界要背下来：Scope 明说**不含 Stellar WLAN 特性**；IoT 章开头注明 **Stellar 特有的 IoT 需求另见它文**。

## A1（决策要点)
1. 形态选择：客户要数据主权/内网隔离 → OVTX 本地版（req #10：私网环境单/多租户单/多站点且不依赖第三方组件）；客户要多国多站点全球化 → OVCX 云（req #8-9：US/EU 合规框架+区域 DC）。
2. 计费口径：licensing 按设备类别（req #4）+ SaaS 订阅生命周期自服务（req #1-3）。
3. MSP 场景必引第 4 章：单一 supervisor 账号下库存/用户/告警多租户管理 + RBAC 外部认证（req #20-23）。
4. NAC 对比话术：内置 RADIUS 不作为独立售卖项（req #60 原文 "RADIUS must not be proposed as separated feature"）——这是和分离式 NAC 产品的正面差异点。

## A2（细节速查表）

| 章 | 条目范围 | 高价值条目抽样 |
|---|---|---|
| 1 订购激活 | #1-4 | Quote-to-Cash 自服务流程；订阅生命周期灵活管理；按设备类别计费 |
| 2 架构总览 | #5-15 | 微服务高可用(#5)；SOC1/SOC2 合规节能数据中心(#7)；本地版免第三方组件的多租户多站点(#10/#13)；有线无线 unified management(#15) |
| 3 部署 | #16-19 | plug-and-play + Zero-touch Provisioning(#17)；设备分组配置(#18)；从老 OmniVista 迁移到 release 10 的简易流程(#19) |
| 4 多租户 | #20-24 | MSP 单监控账号统管库存/用户/告警(#20)；组织-租户两级角色视图(#21-22)；RBAC+外部认证(#23)；地理信息服务(#24) |
| 5 LAN 管理 | #25-29 | L2 GRE 隧道终结服务覆盖各类终端(#25)；VLAN manager(L2)/IP manager(L3)(#26-27)；全 IPv6 支持(#28)；纳管后基于交换机配置的自动化下发(#29) |
| 6 可编程 | #30-33 | 安全 RESTful API(#30)；第三方集成(#31)；API 鉴权(#32)；OpenAPI 文档带用例(#33) |
| 7 安全隐私 | #34-39 | 设备到云管理流量加密(#34)；证书认证加密(#35)；RADsec client(#36)；管理员双因素(#37)；企业 IdP SSO(#38)；强密码策略(#39) |
| 8 维护运维 | #40-42 | 自动定时固件升级减少维护窗口(#40)；统一 LAN+WLAN 拓扑可视化及设备操作(#41)；自动化即时配置备份含安全配置(#42) |
| 9 监控分析 | #43-54 | 实时 KPI 定制仪表盘(#43)；WLAN 用户 QoE 指标与根因分析(#44-45)；live+历史客户端分析≥30 天(#47)；信道/频段分布报表(#48)；应用使用分析(#49)；计划任务报表(#51)；告警模板(#52)；可配置数据保存期(#53)；≥4 台远程 syslog(#54) |
| 10 IoT | #55-58 | IoT 资产清单含上下文识别(#55)；策略管控(#56)；最简安全 onboarding 免第三方组件(#57)；集成诊断工具箱(#58) |
| 11 NAC | #59-72 | 一体化 NAC：802.1x/MAC/证书认证(#59)；内置 RADIUS+Captive Portal 且 RADIUS 不单独售卖(#60)；≥1 内置 RADIUS + 1 内置 LDAP(#61)；外部身份源集成与角色映射(#62)；属性分组 profile(#63)；动态过滤 ID（VLAN/Private Groups）支撑扩展 WLAN 用户组(#64)；LAN/WLAN 统一准入策略(#65)；DPI 应用识别至 L7 含 HTTPS 并可做 QoS/封堵(#66)；内置员工访客账户库(#67)；Guest GRE 隔离(#68)；外置+内嵌 Captive Portal 双支持(#69)；位置+时段策略(#70)、分级服务(#71)、时长/流量配额(#72) |

## E（场景案例/怎么用）
- 投 MSP 托管项目：把 #20-24 与 #34-39 组合成"多租户运营 + 安全合规"两段应答。
- 客户招标写"网管须支持应用层管控"：引 #66（L7 DPI 含 HTTPS、带宽管理/阻断），注意这是 NMS 平台能力而非交换机 ACL。
- 竞品说他们 NAC 更全：反手引 #60+#61——RADIUS/LDAP/Captive Portal 全内置不开票，再引 #69 的内外部 portal 双兼容讲开放性。

## B(限制与坑)
- **只管平台不管无线特性**：Scope 明示 "does not cover Stellar WLAN features"，涉及 AP 能力的条目回 grfp-wlan 单元应答。
- IoT 章明确排除 Stellar 特有需求（原文注明指向其他材料），别当全能 IoT 应答模板。
- 文中个别编号用 "should"（非 shall）：#2、#45、#40、#42 等，严格评标时 should 类承诺弹性更高，引用时保留原措辞。
- 版本演进快：10.4.3(2024-12) → 10.5.1(2025-09) → 10.5.2(2026-01)，与 OVCX/OVTX 版本同步绑定；对标书写的旧版本要先确认降级影响。
- OCR 断词（如 "platorm"、"3th-party"），对外引用英文条款前修正拼写。

来源：omnivista-ng-10.5-golden-rfp-en.docx（sources/grfp-ovng.md，Release Version 表 + Scope + 全部 72 条）
