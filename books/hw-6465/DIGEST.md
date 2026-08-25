# DIGEST — OmniSwitch 6465 Hardware Users Guide 精华

本书是 ALE 工业级（加固型）交换机 OS6465 的硬件手册（99 页，6 机型双线：工业线 P6/P12/P12(ENH-240)/P28 无风扇 DIN/机架 + 运输线 T-12/T-P12 半宽）。全书核心是"宽温 + 端子电源 + 告警继电器 + Dying Gasp"的工业特性栈，以及 PoE 预算随环境温度降额的独特机制。以下按三个技能单元摘要，页码均指原书。

## 一、知识地图（三技能单元）

1. **机型与端口体系**（os6465-model-ports）：工业线/运输线双家族、奇数口 60W bt 规律、上联分档、ENH-240 变体（Ch1/Ch3，p12-13、21-36）。
2. **安装与电源**（os6465-install-power）：DIN/机架/侧挂/DNV 五形态、6 款电源与 ROJ 接线、powersupply type、PoE 温度降额（Ch2-Ch4，p14-84）。
3. **运维与排障**（os6465-ops-troubleshoot）：告警继电器、Dying Gasp 三通道、LED/温度诊断、NEBS 红线（Ch3/附录 A，p63-99）。

## 二、三单元要点串讲

### 1. 机型与端口：双线家族
工业线无风扇 -40~75°C，T 运输线半宽内置电源、风扇 45°C 自启且无工业认证（<<<PAGE 12>>>）。60W 口位：P6/P12 奇数口、P28 口 1-8 支持 60W/bt，其余 at 30W（<<<PAGE 12>>>/<<<PAGE 22>>>/<<<PAGE 31>>>）。仅 P28 有 10G 上联（4×SFP+）与双可热换电源/负载分担（<<<PAGE 13>>>）。预算：P6=45W/P12=150W/ENH-240=240W/P28 最高 285W（<<<PAGE 74>>>）。

### 2. 安装与电源：ROJ 接线与温度降额
安装五件套：DIN 卡扣、P28 机架、T 半宽/双机 DUO 并排、WALL-MNT、DNV 三套件（装罩限温 55°C）（<<<PAGE 38-49>>>）。电源不能自动识别，必须 `powersupply type` 手工声明（<<<PAGE 60>>>）；双电源必须同 wattage 同电压，仅 P28 负载分担（<<<PAGE 13>>>/<<<PAGE 24>>>）。ROJ 线色：输出红 V-/黑 V+/绿 PG、3.5 in-lb；输入黑棕 L/白蓝 N/绿绿黄 PG（<<<PAGE 58-60>>>）。PoE 降额三环：≤60°C 全额/60-70°C 降额需 100 CFM/70-75°C 停 PoE；叠加输入电压环（50-57V 满额/44-57V 限 af/24V 仅系统）（<<<PAGE 74>>>）。陷阱：24V 检测电路缺陷、BPNX 无工业认证且标签误标、BPN 配 ENH-240 需 8.9R2（<<<PAGE 24>>>/<<<PAGE 51>>>/<<<PAGE 53>>>）。

### 3. 运维与排障：告警双体系
告警继电器：输入 5-12VDC 传感器+8 类系统事件→alarm map→NO/C/NC 干接点（220VDC/250VAC·2A），VC 内跨机同步，8 类事件条件恢复自动清除（<<<PAGE 63-65>>>）。Dying Gasp 三通道：SNMP trap（前 3 站）+Syslog（前 3 服务器）+4×802.3ah OAM PDU 上联口优先（<<<PAGE 68-69>>>）。温度双阈值固化，各机型梯度 75-97°C（<<<PAGE 24-36>>>/<<<PAGE 67>>>）。NEBS 红线：楼内端口禁金属直连 OSP、AC 须接 SPD（<<<PAGE 93>>>）。

## 三、本书在知识库中的位置

与 hw-6575（工业无风扇）同属工业线：6465 为 DIN/机架混合形态+端子电源，6575 为无风扇+M12 防水连接器。跨书易混点：混插规则——6465 双电源同型号强制、无混插例外（6560 有 BP+BP-D 例外）；Priority Disconnect 同级裁决在 6465 为"端口号 1 高 8 低"。

## 来源
OmniSwitch 6465 Hardware Users Guide（Part No. 060510-10, Rev. V, 2025-12）。verified.md：cases C1-C24；principles P1-P36；counter-examples X1-X25；frameworks F1-F4；glossary 约 60 条。
