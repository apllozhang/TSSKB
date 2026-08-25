# DIGEST — OmniSwitch 6570M Hardware Users Guide 精华

本书是 ALE 紧凑型交换机 OS6570M 家族硬件手册（59 页，3 个定配置机型：12/12D/U28）。核心卖点：半宽双机并排省机位 + 全光上联型 U28 + Dying Gasp 三通道失电通告。无 PoE、无光模块专章，全书沿"选型→安装→上电→监控"生命周期展开。

## 一、知识地图（三技能单元）

1. **机型与端口体系**（os6570-model-ports）：12/12D/U28 三轴选型、Uplink/Stacking SFP+ 双角色口、combo 互斥、半宽空间利用（Ch1/Ch3，p11-34）。
2. **安装与供电**（os6570-install-power）：三套机架方案（全宽法兰/RM-19-L/DUO-MNT）、双层电源架构（12/12D 内置+外置备份）与 U28 双 150W 舱、DC 线束、supplemental 接地（Ch2-Ch3，p13-45）。
3. **运维与排障**（os6570-ops-troubleshoot）：Dying Gasp 三通道、温度双阈值固化（12 口 85/88°C vs U28 69/74°C）、OK/VC/PS LED 与 150W 六态灯、安全红线（Ch2-Ch3+附录 A，p16-58）。

## 二、三单元要点串讲

### 1. 机型与端口：三轴选型矩阵
命名（<<<PAGE 11>>>）：`12`=8 铜口+2 SFP+2 SFP+ 半宽机；`12D`=DC 版（内置 DC 30W，18-75VDC 宽压）；`U28`=28 口全光上联型（20×SFP+4 combo+6×SFP+，双电源舱，独有 VC ID LED）。核心机制：SFP+ 口为"Uplink/Stacking"双角色——上联与 Virtual Chassis 堆叠共用（12 口机 11-12、U28 25-30）（<<<PAGE 21>>>/<<<PAGE 25>>>）。半宽双机并排（DUO-MNT）=16 铜口+4 SFP+4 SFP+ 上联/堆叠，仍省机架深度。陷阱：全机型不支持半双工；combo 口光铜互斥（<<<PAGE 21>>>-<<<PAGE 25>>>）。

### 2. 安装与供电：双层电源与三套机架
12/12D 为双层电源架构：内置（AC 65W/DC 30W）+ External Power Connector 外置备份（OS6570-12-BP 60W AC / 12-BP-D 30W DC 宽压 18-75VDC）（<<<PAGE 35>>>-<<<PAGE 37>>>）；U28 为双 150W 舱（OS6570-BP/BP-D），可冗余/负载分担，双电源必须同 wattage 同额定电压（<<<PAGE 24>>>）。机架三方案：全宽法兰（U28）、单半宽 RM-19-L、双半宽 DUO-MNT 并排；一律先下孔后上孔紧固，机架螺丝自备（<<<PAGE 29>>>-<<<PAGE 34>>>）。DC 线束三芯 12AWG（绿黄=地/黑=return/红=-48V）+15A 过流+SELV 前提五条（<<<PAGE 40>>>）。

### 3. 运维与排障：DG 三通道与温度双阈值
Dying Gasp 三通道（<<<PAGE 46>>>/<<<PAGE 47>>>）：SNMP trap（前 3 站）+Syslog（前 3 服务器）+4 个 802.3ah OAM PDU（Dying Gasp 位置位，上联口优先发送）。温度双阈值出厂固化（<<<PAGE 45>>>-<<<PAGE 46>>>）：Warning 超限发 trap 业务不停；Danger 超限自动关机且必须手动重启。阈值按机型分化：12/12D 85/88°C、U28 69/74°C——光口机热预算更紧（<<<PAGE 22>>>/<<<PAGE 26>>>）。LED 三层：OK 三态/VC 四态（闪琥珀报 unit 号）/PS 按机型两套语义；150W 电源六态灯含"闪红=本舱无 AC 邻舱有电"的冗余态（<<<PAGE 27>>>/<<<PAGE 38>>>/<<<PAGE 39>>>）。

## 三、本书在知识库中的位置

与 hw-6560（多千兆 bt 旗舰）、hw-6575（工业无风扇）构成紧凑/专用三线——6570M 定位无 PoE 紧凑接入与全光上联。跨书易混点：6560 温度 Warning 阈值用户可配，6570M 均固化不可改；6560 DG 与本机同为三通道（含 OAM PDU），而 6575 仅双通道（无 OAM PDU）；本机 12D 的 BP-D 30W 外置备份与 U28 的 BP-D 150W 舱同名不同物，选型时按主机型号对配。

## 来源
OmniSwitch 6570M Hardware Users Guide（Part No. 060828-10, Rev. G, 2025-12）。verified.md：cases C1-C17；principles P1-P36；counter-examples X1-X26；frameworks F1-F3；glossary 约 75 条。
