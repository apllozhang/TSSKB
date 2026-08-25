# DIGEST — OmniSwitch 6575 Hardware Users Guide 精华

本书是 ALE 工业/极端环境无风扇交换机 OS6575 家族硬件手册（86 页，3 个机型按安装形态分化：P12/U28/MP16）。核心卖点：无风扇 -40~75°C 宽温 + M12/M23 防水连接器 + Port Bypass 断电旁路 + Alarm Relay 干接点 + PoE 温度阶梯预算。全书沿"选型→安装→电源接线→告警→PoE"生命周期展开。

## 一、知识地图（三技能单元）

1. **机型与端口体系**（os6575-model-ports）：P12/U28/MP16 三轴选型、MP16 四段阵列与 M12/M23 pinout、Uplink/VFL 双角色口（Ch1/Ch3，p11-26、p53-55）。
2. **安装与供电**（os6575-install-power）：U28 前装/后装、DIN/壁装、4 款电源与 ROJ 端子接线、powersupply type 手动声明、温度阶梯 PoE 预算（Ch2-Ch4，p13-47、p56-68）。
3. **运维与排障**（os6575-ops-troubleshoot）：Alarm Relay in/out/event 映射与 VC 同步、Dying Gasp 双通道、lanpower PoE 语义（Guard Band/Priority Disconnect）、LED 诊断、NEBS 安全红线（Ch3-Ch4+附录 A，p46-71、p77-85）。

## 二、三单元要点串讲

### 1. 机型与端口：按形态分化的工业三机
命名（<<<PAGE 11>>>）：`P12`=DIN 导轨 PoE 紧凑机（8×bt 60W RJ45+4×SFP+）；`U28`=1U 机架全光机（4 combo PoE+ 90W+20×SFP+4×SFP+）；`MP16`=壁装工业机（M12 连接器四段阵列：纯数据/at 30W/bt 60W/Bypass 各 4 口）。MP16 独有 Port Bypass——失电自动直连两口保通信（<<<PAGE 12>>>/<<<PAGE 25>>>）。输入电压域分化：P12=24-57V、U28=24-60V 三档（50-57V=at 150W/44-57V=af 120W/24-60V=无 PoE）、MP16=20-110V 超宽压（<<<PAGE 22>>>-<<<PAGE 26>>>）。红线：48V 以下禁 PoE。

### 2. 安装与供电：ROJ 接线制与温度阶梯预算
四款电源（<<<PAGE 36>>>-<<<PAGE 40>>>）：BPNS 150W/BPNSX 480W 外置 AC（ROJ 剥线端子制），BPR/BPRD 180W 模块（U28 后装 DB-15 导柱+拇指螺丝）。ROJ 线色注意 V-=红、V+=黑（反直觉），输出端子力矩 3.5 in-lb。电源类型不能自动检测，必须 powersupply type 手动声明（PoE 配置前置）。核心特色温度阶梯预算（<<<PAGE 60>>>/<<<PAGE 61>>>）：预算随 Tmra 四档降级——P12+1×BPNSX 从 ≤50°C 的 330W 降至 70-75°C 的 140W；U28+1×BPR(D) 从 75W 降至 15W；MP16 预算恒定封顶（52W/120W），加电源只保冗余不扩容。

### 3. 运维与排障：告警干接点与 PoE 语义
Alarm Relay（<<<PAGE 48>>>/<<<PAGE 49>>>）：输入单线 5-12VDC（外接温度/门磁/接近传感器）→输出继电器干接点（NO/C/NC，Max 220VDC/250VAC/2A），动作可选 output/trap/SWLog；VC 内跨机同步，支持多对一/一对多映射。Dying Gasp 本机仅双通道：SNMP trap（前 3 站）+Syslog（前 3 服务器），无 OAM PDU（<<<PAGE 52>>>）。温度双阈值 93/98°C，Danger 固化且关机须手动重启。PoE 语义：首启必 lanpower slot service；Guard Band=剩余预算低于口 maxpower 即拒新 PD（解法=降口上限）；Priority Disconnect 四情形按优先级+物理口号（1 高 8 低）裁决。

## 三、本书在知识库中的位置

与 hw-6465（工业加固）、hw-6560（多千兆旗舰）、hw-6570M（紧凑接入）构成家族矩阵——6575 定位极端环境专用线：无风扇宽温+防水连接器+旁路。跨书易混点：DG 通道数 6560/6570M 为三通道（含 802.3ah OAM PDU），6575 仅双通道；6575 的 Priority Disconnect 口号裁决为"1 高 8 低"（低密度口序），与 hw-9900 的"48 高 1 低"相反；MP16 的 M12 口不能插普通 RJ45 网线，须配专用转接线缆族。

## 来源
OmniSwitch 6575 Hardware Users Guide（Part No. 060975-00, Rev. A, 2025-12）。verified.md：cases C1-C27；principles P1-P40；counter-examples X1-X35；frameworks F1-F3；glossary 约 85 条。
