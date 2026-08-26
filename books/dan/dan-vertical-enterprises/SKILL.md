---
name: DAN 企业（通用企业数字化转型网络）
description: 查通用企业 DAN 三支柱口径（2023 版）、IoT containment 三步法、Asset Tracking/占用管理/contact tracing、Rainbow 工作流自动化时使用。
source_book: dan（dan-ent p1-6）
---

## R（何时用）
- 非特定行业的企业客户做 DAN 方案导入（行业归属不明确时默认用本单元）
- 查 2023 版三支柱标准总结口径（Summary 段落）
- 查通用企业的 IoT 安全接入、资产追踪与工作流自动化能力清单

## I（核心理念）
通用企业版彩页（2023-03）给出 DAN 的标准三支柱话术（<<<PAGE 2>>>）：

- **Autonomous Network**：自动开通网络服务、自动化关键任务运维、改善用户体验
- **IoT onboarding**：通过安全 provisioning 与管理扩大数字化规模
- **Business Innovation**：用自动化工作流替代劳动密集、重复性任务

**过去要几天才能开通的网络服务，现在几秒、无错完成；网络从复杂昂贵的底层设施变成新营收来源**（<<<PAGE 2>>>）。

## A1（选型/决策要点）
1. 网络手工配置慢且易错 → iFab 自动化部署 + MAC 简化；未来由机器学习向管理员建议配置变更（<<<PAGE 3>>>）
2. 有线无线底座：OmniSwitch LAN（OS 加固）+ OmniAccess Stellar WLAN（免集中控制器），单一 NMS 统一策略（<<<PAGE 3>>>）
3. IoT 接入一律走三步法：29+ million 设备库识别 → 虚拟分段容器化 → 持续监控异常处置（<<<PAGE 4>>>）
4. 资产与安全诉求 → Stellar Asset Tracking：定位防丢 + 占用管理 + contact tracing（<<<PAGE 5>>>）
5. 流程自动化 → Location Services 接 Rainbow，triggers/rules/actions 联动（<<<PAGE 5>>>）
6. 管理部署形态：本地 / 云 / 混合，按客户偏好（<<<PAGE 6>>>）

## A2（规格细节速查表）—— 企业痛点 → DAN 对应方案组件
| 企业痛点 | DAN 对应方案组件 | 页码 |
|---|---|---|
| 网络配置要数天/数周、人工易错 | Autonomous Network 自动配置开通 + iFab 自动化部署 | <<<PAGE 3>>> |
| 有线无线两套管理、两套策略 | 单一 NMS 统一服务管理与全网可视 | <<<PAGE 3>>> |
| 海量 IoT 难配置、易被黑 | IoT containment 三步法（discover/segment/monitor） | <<<PAGE 4>>> |
| 无法识别接入设备型号 | 29+ million 条设备指纹数据库自动识别并下发配置 | <<<PAGE 4>>> |
| 被黑 IoT 横向渗透全网 | Virtual segmentation 容器隔离 + 异常自动断开/转容器核查 | <<<PAGE 4>>> |
| 设备/资产丢失年度损耗大 | OmniAccess Stellar Asset Tracking 实时/历史定位（Wi-Fi+Bluetooth） | <<<PAGE 5>>> |
| 区域人员密度超限无感知 | 实时 occupancy management，超限自动告警 | <<<PAGE 5>>> |
| 密接/暴露事件难追溯 | 历史 contact tracing + 跟进通知 | <<<PAGE 5>>> |
| 重复任务靠人工执行 | Rainbow 工作流（triggers × rules → actions） | <<<PAGE 5>>> |
| 室内外/工业环境部署受限 | 部署灵活性：indoor / outdoor / industrial；管理本地/云/混合 | <<<PAGE 6>>> |

- 文档版本：DID19061201EN（2023 年 3 月）（<<<PAGE 6>>>）

## E（适用场景案例）
- IT 团队小、预算有限的企业：自动化消除手工配置差错、提升运维效率（<<<PAGE 3>>>）
- 大量哑终端（打印机、摄像头、传感器等）接入的企业园区：三步法安全上线（<<<PAGE 4>>>）
- 疫情后关注聚集与暴露追溯的办公场所：占用管理 + contact tracing（<<<PAGE 5>>>）
- 想让网络数据变现、产生新营收流的企业：位置数据 + Rainbow 工作流开发新数字服务（<<<PAGE 5>>>/<<<PAGE 6>>>）

## B（限制与注意事项）
- 本单元与 APAC 白皮书内容高度同源，差异化信息少；深入理论框架查 dan-wp-enterprises / dan-wp-apac
- "机器学习建议配置变更"仍是未来方向表述（<<<PAGE 3>>>）
- 营销彩页，无具体产品 SKU 与规格参数

来源：dan · dan-ent（DID19061201EN，2023-03），p1-6
