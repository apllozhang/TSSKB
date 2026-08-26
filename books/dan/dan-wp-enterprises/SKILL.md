---
name: DAN 企业白皮书（全球版：Service Defined Network 与四大趋势）
description: 查 DAN 四大趋势（Connectivity/IoT/Augmented intelligence/Cloud economics）、Service Defined Network、UnP、IoT containment 三步法细节、NoD 订阅模式、LBS 变现时使用。
source_book: dan（dan-wp-global p1-14）
---

## R（何时用）
- 需要讲清 DAN 的理论框架（四大趋势 + Service Defined Network 基础）给技术决策层听
- 查 iFab/SPB/UnP/DPI 应用可视等连接层技术口径，或 IoT containment 三步法的原始权威表述
- 客户预算受限 → 查 Network on Demand (NoD) CAPEX 转 OPEX 订阅模式
- 查 LBS（位置服务）如何帮客户"以网养网"产生新营收（球场案例）

## I（核心理念）
DAN 首先是 business enabler：把业务需求自动翻译成网络服务开通，保障用户 QoE 并安全接入 IoT（<<<PAGE 3>>>）。其基础是 **Service Defined Network**——从一个用户或物体到授权应用的自动安全连接；过去要几天才能开通的服务，现在几秒、无错地自动化完成（<<<PAGE 3>>>）。

DAN 应对企业四大趋势（<<<PAGE 4>>>）：
- **Connectivity**：高可用 Service Defined Network，从数据中心到接入层，自动开通管理网络服务
- **IoT**：海量设备安全接入——fingerprinting、containment、inventory、行为分析
- **Augmented intelligence（增强智能）**：机器学习 + 数据分析，主动适应、异常告警、给出优化建议
- **Cloud economics**：pay-as-you-go 模式 + 位置等增值服务，让 IT 变成业务引擎、网络产生新营收

## A1（选型/决策要点）
1. 判断客户网络是否还停留在逐台 CLI 手工配置 → 用"部署应用只要几分钟、配置网络要几天"的反差引出 Service Defined Network（<<<PAGE 5>>>）
2. 连接层选型：iFab（基于 SPB / IEEE 802.1aq，充分利用所有物理链路）+ 接入层 Universal network Profiles (UnP) 统一下发策略，有线无线体验一致（<<<PAGE 5>>>）
3. WLAN 选型：AP 内嵌控制器的新一代 Wi-Fi，免物理集中控制器，分布式架构高性能、高可用、低 TCO（<<<PAGE 6>>>）
4. 管理选型：单一 NMS 统一有线无线策略，避免两套管理系统两套规则（<<<PAGE 6>>>）
5. IoT 场景走 containment 三步法（发现分类→虚拟分段→持续监控），设备识别用 1700 万条设备库自动匹配配置（<<<PAGE 8>>>）
6. 预算受限 → NoD 订阅模式（月度固定 OPEX），部署可选公有/私有云、单/多实例（<<<PAGE 11>>>）
7. 想让网络自我造血 → 引入 LBS：室内导航、地理围栏推送、资产追踪（<<<PAGE 11>>>/<<<PAGE 12>>>）

## A2（规格细节速查表）
| 主题 | 细节 | 页码 |
|---|---|---|
| Service Defined Network 定义 | 用户/物体到授权应用的自动安全连接；基于 SPB (IEEE 802.1aq) | <<<PAGE 5>>> |
| 接入策略 | Universal network Profiles (UnP)：部门/应用访问、安全、性能与 QoS 参数 | <<<PAGE 5>>> |
| WLAN 架构 | AP 内嵌 WLAN 控制，免集中控制器；分布式架构；低 TCO | <<<PAGE 6>>> |
| 统一管理 | 单一 NMS：网元、告警、统一接入安全策略、虚拟化、预测分析 | <<<PAGE 6>>> |
| 应用可视 | 内嵌 L2-L7 DPI；按应用做限速/阻断/优先级，有线无线全網生效 | <<<PAGE 6>>> |
| 设备识别库 | 1700 万（17 million）条设备数据库，自动识别并下发对应配置 | <<<PAGE 8>>> |
| IoT 三步法 | Discover & classify / Virtual segmentation / Continuous monitoring | <<<PAGE 8>>>/<<<PAGE 9>>> |
| 行为异常处置 | 突发大流量/大量 DNS 请求 → 断开设备、通知管理员、改道专用容器核查 | <<<PAGE 9>>> |
| 增强智能闭环 | Machine learning → Correlation → Change proposal → 管理员批准后 Automation 执行 | <<<PAGE 10>>> |
| NoD 模式 | Infrastructure as a Service，CAPEX 转月度固定 OPEX 订阅 | <<<PAGE 11>>> |
| LBS 技术 | 基于 Wi-Fi 与 Bluetooth 的室内定位；wayfinding、geo fence 触发动作 | <<<PAGE 12>>> |
| LBS 价值 | 资产优化、安全防护、员工调度三方向；帮客户增收或降本 | <<<PAGE 13>>> |
| Gartner 引用 | 2022 年 90% IT 领导者聚焦业务交易而非基础设施；2024 年 50% 企业应用 IoT 化 | <<<PAGE 5>>>/<<<PAGE 8>>> |

- 文档版本：00383852EN（2019 年 7 月）（<<<PAGE 14>>>）

## E（适用场景案例）
- 道路交通机构（美国 Nevada DOT）：5400 英里高速、1000+ 桥梁，为下一代 ITS 打底，安全接入增长中的 IoT（<<<PAGE 7>>>）
- 医疗网络（Inspira Health Network）：60+ 临床网点、合并扩张 + 电子病历联邦强制令，ALE 广组合与互操作性承接（<<<PAGE 7>>>）
- 智慧城市（巴西 Fortaleza，260 万人口）：300 km 光纤 + 9200+ IoT（含 CCTV），网络性能提升 10 倍，新服务开通从"天"级降到"分钟"级（<<<PAGE 9>>>）
- 球场 Wi-Fi 变现：入口分流、到座送餐、广告与促销推送，用 LBS 新营收反哺 Wi-Fi 更新（<<<PAGE 11>>>）
- 医院资产定位：轮椅、病床实时位置；行动不便旅客最近轮椅 + 最近员工调度（<<<PAGE 13>>>）

## B（限制与注意事项）
- 设备库口径是 1700 万；APAC 白皮书与 2023 版彩页已更新为 29+ million，对客户报价讲解时用新口径（见 dan-wp-apac 单元）
- 引用的 Gartner 预测多为 2018-2019 年发布，时间点已过，引用时注明出处年份
- 白皮书为 2019 年版愿景文档，部分"未来能力"（如 ML 自动建议配置）在后续版本中才落地表述，勿当现网已交付功能承诺

来源：dan · dan-wp-global（00383852EN，2019-07），p1-14
