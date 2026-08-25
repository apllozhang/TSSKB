---
name: Network Advisor 与 Smart Tool 场景选型（AI 异常自愈 / OT 免云免 CLI 现场工具）
description: 售前为客户配 AI 运维伴随（NetAdvisor 异常检测+一键修复、Rainbow/Teams 交互、第三方 syslog 纳管）或 OT 现场独立工具（OST：PoE 向导 60 秒修复、TDR 线缆测试、Lightning Config）时使用。
source_book: bp-nms-brochures（OmniVista Network Advisor p1-4 / OmniVista Smart Tool p22-23）
---

## R（触发场景）
- 客户要 AI/ML 异常检测与自动修复，告警"修不过来"
- 混合 ALE+第三方设备网络的智能运维
- OT/工厂/交通现场：云不可达、装维外包人员非网络专业
- 首装效率：交换机免 CLI 快速开局、线缆健康测试

## I（核心理念）
运维工具按"谁在用/在哪用"定位（F4，<<<PAGE 1>>>/<<<PAGE 2>>>/<<<PAGE 22>>>）：IT 网络团队日常运维 → Network Advisor（本地+云混合架构的 AI 伴随，识别风险→一键/自动修复→调优建议闭环，P1/P2）；OT 现场装维人员 → Smart Tool（standalone、cloud-independent、免 CLI，P36）。NetAdvisor 是加在 OmniSwitch/Stellar 之上的运维伴随服务，非网管替代品；第三方设备仅 syslog+手工定制规则（P4/X4）。

## A1（行动框架）
1. 问用户与场景：IT 团队日常运维 → NetAdvisor；OT 现场受限云连接/装维外包 → OST
2. NetAdvisor 前提核对：用户须有 Rainbow 账号（交互全靠 Bot/Bubble）；虚拟机自备（1000 设备 120GB / 2000 设备 210GB）；设备版本门槛 OS6xxx/9xxx AOS 8.7R2+、Stellar AWOS 4.0.3MR-3+、2260/2360 仅需 AOS 5.1R1（P5/P6）
3. NetAdvisor 订阅：NETAD-AP/SWITCH/TP-1Y/3Y/5Y 按被管设备类型单台订阅（P7）；不强制先买 Cirrus（X2）
4. OST 差异化能力启用：PoE 向导（60 秒诊断修复）、一键 PoE Power Cycle（保留人工确认）、TDR 线缆测试、Lightning Config 首装向导（P37/P38）

## A2（选型速查表）
| 工具 | 定位 | 关键能力 | 边界/前提 | 页码 |
|---|---|---|---|---|
| Network Advisor | AI/ML 运维伴随 | 异常检测/一键或自动修复/调优建议 | 用户需 Rainbow 账号；VM 自备；不依赖 Cirrus | <<<PAGE 1-3>>> |
| NetAdvisor 容量 | 2000 设备 | 1000 台=120GB / 2000 台=210GB 存储 | 8GB+ 虚拟机自购 | <<<PAGE 3>>> |
| NetAdvisor 第三方 | 混合网络纳管 | syslog 接入 | 仅 syslog+手工定制异常/修复规则 | <<<PAGE 1>>>/<<<PAGE 3>>> |
| NetAdvisor 协作 | Rainbow Bot/Bubble + Teams | 告警与修复在人机对话中完成 | 无 Rainbow 无法用 | <<<PAGE 2>>>/<<<PAGE 3>>> |
| Smart Tool (OST) | OT 现场独立工具，免云免 CLI | PoE 向导 60 秒 / PoE Power Cycle / TDR / LLDP 发现 | 手机/PC 直连交换机 | <<<PAGE 22-23>>> |
| Lightning Config | 交换机首装向导 | 快速安全开局 | 安装期零 CLI 依赖 | <<<PAGE 22>>>/<<<PAGE 23>>> |

## E（选型决策案例）
- 客户已有一批第三方交换机想上异常检测：NetAdvisor 走 syslog 纳管+手工定制规则，按 NETAD-TP-* 订阅；报价含自备虚拟机（C6，<<<PAGE 1>>>/<<<PAGE 3>>>/<<<PAGE 4>>>）
- 工厂/交通现场云不可达、装维外包：OST 独立工具，PoE 向导 60 秒修复+TDR 线缆测试，装维人员零网络背景可用（C8，<<<PAGE 22>>>/<<<PAGE 23>>>）

## B（反例与坑）
- NetAdvisor 虚拟机需自购，ALE 不卖，报价勿漏（X1，<<<PAGE 3>>>）
- NetAdvisor 用户必须有活跃 Rainbow 账号，无 Rainbow 无法交互（X3，<<<PAGE 3>>>）
- 第三方设备无深度遥测，异常/修复规则手工配（X4，<<<PAGE 3>>>）
- NetAdvisor 是运维伴随非网管替代，勿与 OmniVista 平台混为一谈（P1，<<<PAGE 1>>>）
- OST 一键 PoE 断电重启保留人工确认——监狱/赌场/银行等高保证场景的合规设计，勿当"不够自动"批评（P37，<<<PAGE 23>>>）

来源：bp-nms-brochures verified.md（C6/C8/X1-X4/F2/F4/P1-P7/P36-P38）
