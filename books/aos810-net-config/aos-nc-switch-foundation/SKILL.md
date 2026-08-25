---
name: AOS 8 交换机基础（端口参数/DDM/风暴控制/违规恢复/MACsec/静态 MAC）
description: 需要在 OmniSwitch AOS 8 上做以太端口基础配置（自协商/速率/双工/别名/巨帧）、DDM 光模块监控、风暴控制、流控、Link Monitoring/TDR 诊断、违规关停与恢复体系、MACsec 链路加密、静态 MAC 绑定时使用。
source_book: OmniSwitch AOS Release 8.10R4 Network Configuration Guide
---

## R（触发场景）
- 新上架交换机端口基础参数：自协商/速率/双工/MDI/别名/链路 trap/管理性关断
- 光模块要监控温度/电压/光功率并告警：DDM
- 广播/未知单播/组播风暴要限速并自动恢复：flood limiting
- 端口被某特性关停了要排查与恢复：violation recovery 体系
- 链路层要加密认证：MACsec（含 WAN MACsec）
- 沉默设备（服务器/打印机）流量定向：静态 MAC

## I（核心理念）
AOS 配置手册统一章法（F1，<<<PAGE 1>>>）：所有功能章按 Defaults→Quick Steps→Overview→Configuring→Example→Verifying 组织，排障按固定小节定位。违规关停与恢复统一框架（F2，<<<PAGE 69>>>）：STP/QoS/LPS/UDLD/NetSec/NI/LLDP/LinkMon/LFP/RFP 共用一套 shutdown/recovery/trap 机制，分 Discard 与 Admin-Down 两类；排障先查 `show violation` 而非逐特性查。恢复五件套：手动 clear violation+自动恢复定时器+最大恢复次数+wait-to-restore+SNMP trap（P8，<<<PAGE 69>>>）。MACsec 提供 802.1 点到点链路安全（防 DoS/中间人/重放/窃听），默认 128-bit AES-GCM，SAK 由 MKA 协商（P13/P17，<<<PAGE 83-84>>>）。

## A1（决策框架）
1. **端口参数**：保持自协商开启；一旦禁用，auto MDIX/auto speed/auto duplex 全部失效（P1，<<<PAGE 56>>>）
2. **风暴控制**：按 bcast/uucast/mcast 三类分别限速，超阈值丢包；要自动恢复配 low-threshold（P5/P6，<<<PAGE 59>>>）
3. **关停恢复路径**：Filtering 关停（链路灯保留）插拔网线可恢复；Administratively 关停（灭灯）插拔/链路翻动无效，永久关停只能 `clear violation` 或 `interfaces reset`（P9/P10，<<<PAGE 69-70>>>）
4. **链路加密选 MACsec 模式**：动态 SAK(PSK)（CAK 保护控制面、key server 周期换钥）；动态 CAK(EAP)（须 EAP-TLS 双向认证，CAK 从 MSK 派生）；静态 SA（两端手工配匹配 SAK）（P18/P19，<<<PAGE 84-85>>>）
5. **静态 MAC**：沉默设备用 bridging（定向转发）；阻断攻击用 filtering（P26/P27，<<<PAGE 105>>>）

## A2（操作步骤）
- **端口批量配置**：`interfaces 2/3 autoneg enable`、`interfaces 2/1-3 crossover mdi`、`interfaces 2/1 speed 100`、`interfaces 2/1 duplex full`、`interfaces 2/3 link-trap enable`、`interfaces 2/3 admin-state disable`（支持单口/范围/整槽）；验证 show 系列（cases·C1，<<<PAGE 56>>>）
- **DDM**：`interfaces ddm enable`+`interfaces ddm-trap enable`（阈值越界告警）；光模块必须支持 DDM（cases·C2，<<<PAGE 58>>>）
- **风暴控制与动作**：`interfaces 2/1/1 flood-limit bcast rate mbps 100`；动作 `interfaces 1/1/1 flood-limit bcast action shutdown`；自动恢复 `interfaces 1/1/1 flood-limit bcast rate mbps 60 low-threshold 40`（cases·C3，<<<PAGE 59>>>）
- **流控**：`interfaces ... pause tx-and-rx`（tx/rx/tx-and-rx 三态）（cases·C4，<<<PAGE 60>>>）
- **违规恢复调优**：`violation recovery-time 600`（全局）、`violation port 1/2/1 recovery-time 200`（按口）；默认 300 秒（cases·C5，<<<PAGE 71>>>）
- **静态 MAC**：`mac-learning vlan 1 port 1/1 static mac-address 00:00:02:CE:10:37 bridging`；删除用 no 形式；聚合口写 linkagg ID；验证 `show mac-learning`（cases·C6，<<<PAGE 106>>>）
- **诊断**：TDR 时域反射定位铜缆断点/长度（<<<PAGE 66>>>）；Link Monitoring 按窗口监测端口错误与翻动并可自动关停（<<<PAGE 74>>>）；LFP 把远端故障传播到本地接口触发关停（<<<PAGE 78>>>）

## E（实证案例）
- 端口基础参数批量配置（C1，<<<PAGE 56>>>）
- 风暴控制三态（限速/shutdown/low-threshold 自动恢复）（C3，<<<PAGE 59>>>）
- 静态 MAC bridging 绑定（C6，<<<PAGE 106>>>）

## B（反例/坑）
- 端口别名只能配单口，不能配范围或整机（X2，<<<PAGE 58>>>）
- 默认风暴动作是纯丢包不告警；不显式配 action/trap 就无感知（X4，<<<PAGE 59>>>）
- 管理性关断的端口靠插拔网线/链路翻动无法恢复（X5，<<<PAGE 69>>>）
- 永久关断口自动恢复定时器无效，只能 clear violation/interfaces reset（X6，<<<PAGE 71>>>）
- 违规恢复机制不作用于聚合口本身，只作用成员口（X7/P12，<<<PAGE 71>>>）；违规不叠加：已被别的特性关停或链路不在 up 状态时不再施加新的违规关停（X8，<<<PAGE 70>>>）
- 全双工 PAUSE 流控与自协商有从属关系：两者都开时由自协商决定 PAUSE 处理（P7，<<<PAGE 60>>>）
- `clear interfaces ... l2-statistics cli` 只清 CLI 计数，SNMP 累计值保留（P3，<<<PAGE 57>>>）
- MACsec 需要站点 license（不绑序列号/MAC）（X9，<<<PAGE 83>>>）；静态 SA 两端必须配完全匹配的 SAK 名与值，漏一端即断（X10，<<<PAGE 84>>>）；动态 CAK(EAP) 强制 EAP-TLS/PEAP，非双向认证无法派生 CAK（X11/P19，<<<PAGE 85>>>）；switch-to-host 场景交换机永远是 key server（P20，<<<PAGE 85>>>）
- 静态 MAC 只支持固定端口，端口必须先属于目标 VLAN；同 VLAN 内源地址撞静态 MAC 的包被丢弃；配在 down 口上显示无效（带星号）（X12-X14，<<<PAGE 105>>>）；静态 MAC 永久有效，重启与老化均不删除，聚合口配在 linkagg ID（P28/P29，<<<PAGE 105-106>>>）
- DDM 依赖光模块支持，并非全部模块可用（X3/P4，<<<PAGE 58>>>）

## 来源
OmniSwitch AOS 8.10R4 Network Configuration Guide 第 1 章 Ethernet Ports（<<<PAGE 56-87>>>）、第 3 章 Source Learning（<<<PAGE 105-108>>>）。条目来源：cases C1-C6；principles P1-P29；counter-examples X1-X14；frameworks F1/F2/F18。
