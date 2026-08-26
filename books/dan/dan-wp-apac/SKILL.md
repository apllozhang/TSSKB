---
name: DAN 企业白皮书（APAC 版：三支柱口径与 APAC 案例）
description: 查 DAN 三支柱 2022 版表述（Autonomous Network / IoT / Business Innovation）、29+ million 设备库、Stellar Location Services（Asset Tracking / LBS / Rainbow 工作流）及 APAC 案例（UTS、东南亚机场、柬埔寨高校）时使用。
source_book: dan（dan-wp-apac p1-11）
---

## R（何时用）
- 需要 2022 年更新的三支柱官方口径（比 2019 全球版白皮书新）做方案引用
- 亚太客户售前：要 UTS（澳洲高校）、东南亚机场、柬埔寨教育机构等同区域案例
- 查 OmniAccess Stellar Asset Tracking / LBS / Rainbow 工作流联动的具体能力描述
- 对比 29+ million 设备识别库与旧版 17 million 口径差异时

## I（核心理念）
APAC 版白皮书（2022-02）把 DAN 归纳为三支柱（<<<PAGE 4>>>）：

- **Autonomous Network**：自动开通网络服务、自动化关键任务运维，iFab 简化 MAC；未来借助机器学习自动适配业务变化，向管理员建议配置变更
- **IoT onboarding**：以安全 IoT 开通与管理扩大数字化规模，接入海量 IoT 设备作为数字业务流程底座
- **Business Innovation**：用自动化工作流（triggers / rules / actions）把人力密集、重复性工作交给网络

**网络服务 = 从用户或物体到授权应用的自动安全连接**（<<<PAGE 5>>>）。

## A1（选型/决策要点）
1. 有线无线底座：OmniSwitch LAN + OmniAccess Stellar WLAN，超快收敛、安全接入控制、保证 QoS、OS 加固交换机（<<<PAGE 5>>>）
2. WLAN 选型：AP 内嵌控制、免物理集中控制器；单一 NMS 统一有线无线管理与策略（<<<PAGE 5>>>/<<<PAGE 6>>>）
3. 应用管控：内嵌 L2-L7 DPI 采集应用数据，按应用限速/阻断/优先级，有线无线一致执行（<<<PAGE 6>>>）
4. IoT 接入走三步法，设备识别库为 29+ million 条（<<<PAGE 8>>>）
5. 位置类需求拆分：找物找人选 Asset Tracking；室内导航 + 推送选 LBS（wayfinding + geonotifications，云端应用管理）（<<<PAGE 10>>>）
6. 流程自动化：Location Services 数据接入 Rainbow，用 triggers-rules-actions 组合自动执行重复任务（<<<PAGE 10>>>）
7. 管理交付形态：本地 / 云 / 混合按客户偏好；云管可选 OmniVista Cirrus（含访客接入、BYOD、分析，无额外费用）（<<<PAGE 10>>>/<<<PAGE 11>>>）

## A2（规格细节速查表）
| 主题 | 细节 | 页码 |
|---|---|---|
| 三支柱口径 | Autonomous Network / IoT / Business Innovation（2022 版） | <<<PAGE 4>>> |
| Autonomous Network 组件 | OmniSwitch LAN + OmniAccess Stellar WLAN、iFab、单一 NMS、ultra-fast convergence、OS hardened switch | <<<PAGE 5>>> |
| 统一管理（NMS） | 统一服务管理 + 全网可视：网元、告警、统一接入安全策略、虚拟化、预测分析 | <<<PAGE 6>>> |
| 应用可视 | L2-L7 DPI；按应用 QoS 强制（限速/阻断/优先级）；内嵌分析引擎出报告 | <<<PAGE 6>>> |
| 设备识别库 | 29+ million 条设备数据库，自动识别并自动下发配置 | <<<PAGE 8>>> |
| IoT 三步法 | Discover and classify / Virtual segmentation / Continuous monitoring；异常行为自动断开或转容器核查 | <<<PAGE 8>>>/<<<PAGE 9>>> |
| Asset Tracking | Wi-Fi + Bluetooth 实时与历史定位；热点追踪、历史 contact tracing | <<<PAGE 10>>> |
| LBS | Wayfinding（室内导航）+ Geonotifications（地理推送），云端应用 + 分析仪表盘 | <<<PAGE 10>>> |
| Rainbow 工作流 | triggers / rules / actions 自动化；与位置数据联动 | <<<PAGE 10>>> |
| 云管 | OmniVista Cirrus NMS-as-a-Service：统一云管 + 本地交换机/AP；内置访客接入、BYOD、分析 | <<<PAGE 10>>>/<<<PAGE 11>>> |
| 管理部署形态 | on-premises / cloud / hybrid | <<<PAGE 11>>> |

- 文档版本：DID19120801EN（2022 年 2 月）（<<<PAGE 11>>>）

## E（适用场景案例）
- 悉尼科技大学（UTS）：十亿澳元校区扩建，高密度城市环境建安全 WLAN，LDAP/AD/RADIUS 集成，应用带宽与优先级设定后配置自动化（<<<PAGE 7>>>）
- 东南亚繁忙机场：新航站楼启用后客流翻倍，LAN/WLAN + IoT containment 多层安全，安全简化设备上线，防网络攻击（<<<PAGE 9>>>）
- 柬埔寨教育机构：BYOD 增长 + 在线测评普及，部署 OmniVista Cirrus 云管，免服务器与升级运维，内置访客/BYOD/分析（<<<PAGE 10>>>）
- Inspira Health Network（医疗）：60+ 临床网点扩张 + 电子病历强制令，广组合与互操作承接（<<<PAGE 7>>>）

## B（限制与注意事项）
- 与 dan-wp-global（2019 版）内容大量重叠，差异主要在：三支柱口径取代四趋势框架、设备库 17M→29+M、新增 Stellar Location Services / Rainbow / OmniVista Cirrus 表述；引用优先用本版
- 东南亚机场与柬埔寨案例未披露客户实名，对外引用按"某东南亚枢纽机场/某柬埔寨高校"口径
- iFab 在本版仍基于机器学习的"未来将自动适配"表述，属愿景而非已交付功能（<<<PAGE 5>>>）

来源：dan · dan-wp-apac（DID19120801EN，2022-02），p1-11
