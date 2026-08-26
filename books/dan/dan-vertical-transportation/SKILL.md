---
name: DAN 交通（轨道、机场、智慧公路、港口）
description: 查交通行业 DAN 方案：轨道双网融合、机场多租户多服务、抗恶劣环境设备（WPA3/加固）、Stellar 4000 AP 单集群、港口物联网拓扑时使用。
source_book: dan（dan-trans p1-7）
---

## R（何时用）
- 面向铁路（城轨/干线/高铁）、公路管理局、机场、港口、物流货运客户的 DAN 方案宣讲
- 交通痛点：关键任务网（信号/SCADA/安防）与业务网（售检票/商业 Wi-Fi）分离、海量 IoT、恶劣环境部署、多租户隔离
- 查 DAN 中最"硬"的技术规格：WPA3、OS 加固交换机、4000 AP 单集群、室内外加固型设备

## I（核心理念）
交通各子行业挑战共通：**提升安全与安保、用 IoT 提高运营效率、改善乘客体验**，同时应对客流与数据量的指数增长（<<<PAGE 2>>>）。

关键背景判断（<<<PAGE 2>>>）：
- 轨道运营商传统上部署多张网：关键任务（控制、信号、安防、SCADA）与业务（售检票、闸机、站台 Wi-Fi、零售）分立
- 机场需要多服务、多租户网络，各租户（值机柜台、安检、行李、运营、乘客 Wi-Fi、零售）各有安全/QoS/带宽要求
- 智慧公路靠 ITS（Intelligent Transportation Systems）提升安全效率与可持续性
- 港口正迈向更自主的船舶与系统，IoT 是关键推手

**最终形态：一张物理网承载多服务多租户**——Autonomous Network 在所有活跃物理链路间创建虚拟连接并选最优路径，抗物理损坏，为每个用户/设备/IoT 管理分段与自动化（<<<PAGE 4>>>）。

## A1（选型/决策要点）
1. 轨道客户：把关键任务网与业务网合并到一张物理网 → 用虚拟分段实现"物理合一、逻辑隔离"（<<<PAGE 4>>>）
2. 机场客户：多租户各取所需的安全/QoS/带宽 → Autonomous Network 单基础设施托管多服务多租户（<<<PAGE 4>>>）
3. 恶劣环境（隧道、站台、场站、港区）→ 室内外加固型（ruggedised）交换机与 AP（<<<PAGE 4>>>）
4. 安全规格：OmniAccess Stellar AP 支持 WPA3；OmniSwitch 采用 secure diversified code 实现 OS 加固（<<<PAGE 4>>>）
5. 大规模 Wi-Fi：Stellar WLAN 单集群可扩展至 4000 AP、免集中物理控制器，覆盖绝大多数交通部署（<<<PAGE 4>>>）
6. 有线无线同一套上线原则（same onboarding principles）→ 真 end-to-end 方案（<<<PAGE 4>>>）
7. 海量 IoT 走 containment 三步法 + 29+ million 设备库（<<<PAGE 5>>>）
8. 位置服务：Asset Tracking（Bluetooth）找设备找资产，降损耗（<<<PAGE 6>>>）
9. 流程自动化：Location Services 接 Rainbow triggers/rules/actions（<<<PAGE 6>>>）

## A2（规格细节速查表）—— 交通痛点 → DAN 对应方案组件
| 交通痛点 | DAN 对应方案组件 | 页码 |
|---|---|---|
| 关键任务网与业务网分立、重复建设 | Autonomous Network 单物理网多服务多租户 + 虚拟分段 | <<<PAGE 2>>>/<<<PAGE 4>>> |
| 网络物理损坏风险（隧道/场站） | 全链路虚拟连接选最优路径，resilient to physical damage | <<<PAGE 4>>> |
| 隧道/户外/港区恶劣环境 | 室内外 ruggedised 交换机与 AP | <<<PAGE 4>>> |
| 乘客与零售租户 Wi-Fi 隔离 | 多租户各自安全/QoS/带宽 + 统一上线原则（有线无线同源） | <<<PAGE 2>>>/<<<PAGE 4>>> |
| 大规模 AP 部署上限担忧 | Stellar WLAN 单集群 4000 AP，免集中物理控制器 | <<<PAGE 4>>> |
| 无线安全合规 | OmniAccess Stellar AP 支持 WPA3 | <<<PAGE 4>>> |
| 交换机被攻击面大 | OmniSwitch secure diversified code / OS hardened | <<<PAGE 4>>> |
| 海量 IoT（摄像头/传感/SCADA）上线难 | IoT containment 三步法 + 29+ million 设备库 | <<<PAGE 5>>> |
| IoT 异常威胁全网 | 虚拟分段隔离 + 自动断开/通知/转容器核查 | <<<PAGE 5>>> |
| 设备资产（含场站设施）损耗高 | OmniAccess Stellar Asset Tracking（Bluetooth 定位） | <<<PAGE 6>>> |
| 重复运维任务多 | Rainbow 工作流 triggers/rules/actions 自动化 | <<<PAGE 6>>> |
| 两套管理系统负担 | 单一 NMS 统一有线无线管理与可视 | <<<PAGE 4>>> |

- 文档版本：DID00374401EN（2023 年 3 月）（<<<PAGE 7>>>）

## E（适用场景案例）
- 智慧城轨/干线铁路：乘客信息系统、站台 Wi-Fi 与信号/SCADA 网合一承载（<<<PAGE 4>>> 场景图）
- 智慧公路与隧道：控制中心 + 隧道覆盖 + ITS 信息通信技术组合，降拥堵提安全（<<<PAGE 2>>>/<<<PAGE 4>>>）
- 智慧机场：值机、安检、行李、运营、乘客 Wi-Fi、零售多租户一张网（<<<PAGE 2>>>）
- 智慧港口：浮标、集装箱跟踪、岸吊守护、地下水水位、垃圾容器等经 IoT 网关汇聚，网络层与应用层双加密，接 OXE 通信与应急通知（<<<PAGE 5>>> 场景图）
- IT 团队提升 SLA：自动化简化网络，减人工差错，改善旅行者体验（<<<PAGE 4>>>）

## B（限制与注意事项）
- 4000 AP 单集群为 Stellar WLAN 平台口径，具体型号与软件版本约束查无线产品单元
- 港口图中的 OXE（通信平台）、防火墙、应急通知服务器为组合方案组件，非 DAN 本体
- 轨道信号等 SIL 级安全业务是否可承载，需按当地铁路安全规范单独评估，彩页未涉及
- 无风扇/工作温度等加固参数未给出，查硬件单元

来源：dan · dan-trans（DID00374401EN，2023-03），p1-7
