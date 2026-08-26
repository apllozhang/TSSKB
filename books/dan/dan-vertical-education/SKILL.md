---
name: DAN 教育（高校与 K-12 数字化校园）
description: 查教育行业 DAN 方案：校园网自动运维、教学/科研/IoT 设备安全接入、学生成功分析、资产追踪与占用管理、校园安全时使用。
source_book: dan（dan-edu p1-7）
---

## R（何时用）
- 面向高校、研究机构、K-12 学校的 DAN 方案宣讲与投标
- 教育客户痛点：IT 预算紧、有线无线多套管理、BYOD 与教学 IoT 爆发、校园安防（CCTV/门禁）、资产丢失
- 查教育场景三支柱落地说法与行业特色能力（学生成功分析、占用管理、contact tracing）

## I（核心理念）
教育 DAN 用新一代网络基础设施支撑教育数字化转型：让教育者用上下一代数字学习工具，提升学生成功率和保留率，同时降低生均成本（<<<PAGE 2>>>）。

三支柱在教育语境（<<<PAGE 2>>>）：
- **Autonomous Network**：在复杂高校/研究环境及预算有限的学校，自动配置消除人工差错、提升运维效率
- **IoT onboarding**：把智能板、3D 打印机、机器人、投影仪及校园运营类设备安全可靠地自动开通
- **Business Innovation**：用自动化工作流改善校园安全与高效运营

## A1（选型/决策要点）
1. 多群体权限模型：学生（在线课程/LMS/协作）、教师（成绩/学籍/科研系统）、行政（财务/安防系统）分角色授权，只访问被授权应用（<<<PAGE 3>>>）
2. 大流量场景（科研数据、视频社交、在线课程/AR 学习）→ 用 SPB 最大化链路利用率，兼顾性能与弹性（<<<PAGE 3>>>）
3. 校园 IoT 分类接入：教学科研设备、学生个人设备、运营设备（HVAC/照明/喷淋/洗手间传感器）、安防设备（摄像头/门锁/烟感）统一 containment 三步法（<<<PAGE 4>>>）
4. 设备识别库 29+ million 条，自动识别自动下发配置（<<<PAGE 4>>>）
5. 资产与安全管理选 OmniAccess Stellar Asset Tracking：设备定位防丢防盗 + 实时占用管理 + 历史 contact tracing（<<<PAGE 5>>>）
6. 流程自动化：Location Services 数据接 Rainbow，用 triggers/rules/actions 自动化重复任务（<<<PAGE 6>>>）
7. 管理交付形态按预算选：本地 / 云 / 混合（<<<PAGE 7>>>）

## A2（规格细节速查表）—— 教育痛点 → DAN 对应方案组件
| 教育痛点 | DAN 对应方案组件 | 页码 |
|---|---|---|
| IT 预算有限、人工配置易错 | Autonomous Network 自动开通 + iFab 自动化部署与 MAC 简化 | <<<PAGE 3>>> |
| 有线无线两套系统两套策略 | 单一 NMS 统一管理，OmniSwitch LAN + OmniAccess Stellar WLAN | <<<PAGE 3>>> |
| 科研/视频/在线课程大带宽 | SPB（Shortest Path Bridging）最大化链路、弹性 fabric | <<<PAGE 3>>> |
| 教学设备（智能板/3D 打印/机器人）接入难 | IoT containment：Discover and classify（29+ million 设备库） | <<<PAGE 4>>> |
| 校园运营设备（HVAC/照明/ vending/停车传感器）分散 | Virtual segmentation 虚拟分段容器化 | <<<PAGE 4>>> |
| 校园安防（CCTV/门锁/烟感）早期告警 | IoT 自动安全上线 + continuous monitoring 持续监控 | <<<PAGE 2>>>/<<<PAGE 4>>> |
| 设备资产丢失损耗（投影仪等） | OmniAccess Stellar Asset Tracking 实时/历史定位（Wi-Fi+Bluetooth） | <<<PAGE 5>>> |
| 人群聚集超限、传染病暴露风险 | 实时 occupancy management + 历史 contact tracing 自动告警 | <<<PAGE 5>>> |
| 学生成功/流失判断缺数据 | 采集聚集、出勤、应用使用等指标，喂给自动化工作流辅助评估 | <<<PAGE 5>>> |
| 重复性任务靠人工跑 | Rainbow 工作流：triggers × rules → actions | <<<PAGE 6>>> |

- 文档版本：DID00375398EN（2023 年 3 月）（<<<PAGE 7>>>）

## E（适用场景案例）
- 预算有限的学区：自动网络配置消除手工差错，把有限 IT 人力解放出来（<<<PAGE 2>>>）
- 研究/教学混合的大学：SPB fabric 同时承载粒子加速、天文图像处理等科研流量与视频娱乐流量（<<<PAGE 3>>>）
- 校园安防升级：摄像头、门锁、烟雾探测器等 IoT 自动安全上线并持续监控，危险情况早期告警（<<<PAGE 4>>>）
- 疫情/化学品暴露场景：contact tracing 定位密接人员并跟进通知（<<<PAGE 5>>>）

## B（限制与注意事项）
- "评估哪些学生可能辍学"的能力原文明确说"仍有一段长路要走"，属方向性描述，不可当现成产品功能承诺（<<<PAGE 5>>>）
- 学生行为数据采集涉及隐私合规，落地前需与校方确认脱敏与授权机制
- 本彩页为营销文档，具体 SKU/组网规模需结合产品数据表单元

来源：dan · dan-edu（DID00375398EN，2023-03），p1-7
