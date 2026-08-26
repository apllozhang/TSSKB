---
name: DAN 酒店（宾客体验与智慧客房）
description: 查酒店行业 DAN 方案：宾客 Wi-Fi 与角色化接入、智慧客房 IoT（多标准 IoT Hub）、OmniVista Cirrus 云管 pay-as-you-go、LBS 位置营销与儿童看护、会议室工作流示例时使用。
source_book: dan（dan-hosp p1-8）
---

## R（何时用）
- 面向酒店集团、单体酒店、酒店集成商与 MSP 的 DAN 方案宣讲
- 酒店痛点：宾客多设备上网体验、客房自动化差异化、IT 预算有限、多分店管理、想用位置数据增收
- 查 DAN 最完整的 IoT 多标准支持口径（Ethernet/Wi-Fi/BLE/Zigbee + IoT Hub）与工作流实例

## I（核心理念）
酒店业宾客体验是第一差异化要素，Wi-Fi、忠诚度计划与面向宾客的 App 位列数字化投入前三；宾客带着多台设备入住，只求"连上、放松、如在家"（<<<PAGE 2>>>）。

**网络不能再是成本中心**：要成为宾客体验交付与增值服务的主动组件，为酒店带来新营收（<<<PAGE 2>>>）。

三支柱落点：自动化的网络让 IT 聚焦新宾客服务；IoT 自动安全上线支撑智慧客房与酒店运营；自动化工作流提升员工效率与宾客数字互动（<<<PAGE 2>>>）。

## A1（选型/决策要点）
1. 角色化接入：宾客、员工、IoT 各自带 profile 自动连网，访问级别/安全/QoS 按角色区分（如酒店内部应用仅授权员工可访问）（<<<PAGE 4>>>）
2. IT 预算有限的酒店 → OmniVista Cirrus 云管（NMS as a Service），pay-as-you-go，免前置投资与本地设备，适合酒店业主/集成商/MSP 多店管理（<<<PAGE 4>>>）
3. 智慧客房与酒店 IoT：Ethernet、Wi-Fi、BLE、Zigbee 由 ALE 网络设备原生支持；其余标准经 IoT Hub 控制器 + 标准 API 与第三方网关集成（<<<PAGE 5>>>）
4. 位置增收：LBS（wayfinding + geonotifications 云端管理）做室内导航与基于位置的促销推送；Asset Tracking 做员工调度、贵重资产与宾客车辆追踪、家庭组儿童看护（<<<PAGE 6>>>）
5. 工作流自动化典型编排：会议排期触发 → 按起止时间配置会议室 AP → 自动创建/删除/启停 SSID、开关 Wi-Fi 射频、把密钥发给组织者并通知网管（<<<PAGE 7>>>）
6. 数据变现下一步：网络统计与 PMS/CRM 宾客数据结合，做超个性化服务（知道宾客常待哪里、偏好什么，定制专属优惠）（<<<PAGE 7>>>）
7. 室内外全覆盖：Stellar WLAN 全场无缝 Wi-Fi（含室外），为位置类新服务创造前提（<<<PAGE 3>>>）

## A2（规格细节速查表）—— 酒店痛点 → DAN 对应方案组件
| 酒店痛点 | DAN 对应方案组件 | 页码 |
|---|---|---|
| 宾客/员工/IoT 混跑、权限不清 | 角色 profile 自动接入：不同访问级别、安全与 QoS | <<<PAGE 4>>> |
| IT 预算与人力有限、多店管理 | OmniVista Cirrus 云管（pay-as-you-go，免前置投资） | <<<PAGE 4>>> |
| 客房自动化设备制式繁多 | 多标准 IoT：Ethernet/Wi-Fi/BLE/Zigbee 原生 + IoT Hub 集成其他标准（API/第三方网关） | <<<PAGE 5>>> |
| 客房传感器、门锁、kiosk、机器人上线难 | IoT containment 三步法 + 29+ million 设备库 | <<<PAGE 5>>> |
| IoT 被黑危及宾客与运营 | 虚拟分段隔离 + 异常自动断开/转容器核查 | <<<PAGE 5>>> |
| 宾客找路难、促销触达差 | LBS：wayfinding 室内导航 + geonotifications 位置推送 | <<<PAGE 6>>> |
| 贵重资产/宾客车辆找不到 | Asset Tracking 实时定位（Wi-Fi+Bluetooth） | <<<PAGE 6>>> |
| 儿童离开安全区域无感知 | 家庭组位置看护 + 离开指定区域告警 | <<<PAGE 6>>> |
| 会议/活动网络开通靠人工 | Rainbow 工作流：会议排期触发自动配置 AP/SSID/密钥分发 | <<<PAGE 7>>> |
| 营销粗放、复购低 | 位置分析 + PMS/CRM 数据融合的超个性化服务 | <<<PAGE 7>>> |
| 有线无线两套管理 | 单一 NMS 统一服务管理与全网可视 | <<<PAGE 4>>> |

- 文档版本：00370818en（2021 年 1 月）（<<<PAGE 8>>>）

## E（适用场景案例）
- 连锁酒店多分店：集成商/MSP 用 OmniVista Cirrus 一朵云管多店，免本地网管服务器（<<<PAGE 4>>>）
- 智慧客房：高速 Wi-Fi + 非侵入式客房自动化（传感器、门锁、IPTV、数字标牌）组合成差异化卖点（<<<PAGE 5>>>）
- 会议室/大宴会厅办会：排期即自动开通活动 Wi-Fi，会后自动回收（trigger-rule-action 全示例）（<<<PAGE 7>>>）
- 宾客 App 场景：地图引路到客房、路过酒吧收 happy hour 券、家人位置互相可见（<<<PAGE 6>>>）

## B（限制与注意事项）
- 本彩页为 2021 年 1 月版，早于 2023 版其他行业彩页，部分口径（如设备库规模）以新版为准核对
- 位置营销与 PMS/CRM 融合涉及宾客隐私（GDPR/个保法），落地需脱敏与授权设计
- IoT Hub 对非原生标准的支持依赖第三方网关，具体兼容清单需查产品资料
- "hyper-personalized services"原文表述为 next step 方向，非现成功能

来源：dan · dan-hosp（00370818en，2021-01），p1-8
