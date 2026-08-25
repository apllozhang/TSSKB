# DIGEST — OmniSwitch 6360 Hardware Users Guide 精华

本书是 ALE 入门级三层千兆接入交换机 OS6360 的硬件手册（83 页，10 个 1U 固定配置机型）。全书围绕"选型→安装→上电→PoE→监控"的硬件生命周期展开：Ch1 机型总表、Ch2 快速入门、Ch3 机箱与电源、Ch4 PoE 管理、附录 A 法规。所有机型电源内置不可热换，PoE 预算在购机时一次定死。以下按三个技能单元摘要，页码均指原书。

## 一、知识地图（三技能单元）

1. **机型与端口体系**（os6360-model-ports）：命名解码（P/PX/H）、10 机型端口与预算对照、combo/SFP+ 可配口/VFL、VC（Ch1/Ch3，p13-16、26-57）。
2. **安装与电源**（os6360-install-power）：机架/桌面/半宽/壁挂四形态、间隙与接地、PoE 三环体系（预算/优先级/保护）（Ch2-Ch4，p17-69）。
3. **运维与排障**（os6360-ops-troubleshoot）：LED 三层诊断、温度双阈值、首次登录六步、show 四板斧、安全红线（Ch2-Ch4+附录 A，p20-83）。

## 二、三单元要点串讲

### 1. 机型与端口：三轴选型矩阵
家族命名：`-10/-24/-48` 非 PoE；`P`=802.3at；`PX`=2×多千兆 bt 口+950W 电源；`PH`=combo 可软件升 10G（<<<PAGE 13-15>>>）。上行三段式：2×combo + 2×SFP+ 软件可配口（1G 上行 / 10G/VFL 双角色）（<<<PAGE 13>>>）。PoE 预算与电源一一对应：P10=120W、P24=180W、P24X/PH24=380W、P48=350W、P48X/PH48=760W（<<<PAGE 60>>>）。陷阱：P10A-US（PN 904324-90）丝印相同但不支持 Fast/Perpetual PoE（<<<PAGE 28>>>）。无风扇机型为 10/P10/24/P24/48，大功率 PoE 机型带风扇（<<<PAGE 13-14>>>）。

### 2. 安装与电源：PoE 三环体系
安装四形态：全宽机架法兰（双人+先下孔后上孔）、半宽 L 支架（OS6360-RM-19-L）、桌面脚垫、壁挂（仅 10/P10）（<<<PAGE 48-55>>>）。间隙前 6"/后 6"/侧 2"（<<<PAGE 19>>>）；接地 LCD8-10A-L+8AWG+30-60 in-lb（<<<PAGE 55>>>）。PoE 三环（<<<PAGE 62-68>>>）：预算环（service 两级激活、maxpower 不预留、Guard Band 余量<口上限即拒新 PD）；优先级环（low/high/critical+端口号 1 高 48 低）；保护环（Priority Disconnect 四情形）。Guard Band 解锁口诀：降口上限放行小 PD（<<<PAGE 65>>>）。Fast PoE 固化于 FPGA 上电数秒供电；Perpetual PoE 软重启不断电（MCU 升级除外）（<<<PAGE 63>>>）。

### 3. 运维与排障：三层监控框架
物理层 LED：OK/VC/PWR 三系统灯+端口分色（绿=非 PoE/琥珀=PoE，SFP 琥珀=VFL）（<<<PAGE 45-46>>>）。传感层：超 Warning 发 trap、超 Danger 自动关机（阈值固化不可配、需手动重启）（<<<PAGE 56-57>>>）。CLI 层四板斧：show module/temperature/powersupply/lanpower（<<<PAGE 55-57>>>）。首次登录六步+会话逐类解锁模型（<<<PAGE 21-24>>>）。红线：无 RTC 须 NTP（<<<PAGE 23>>>）、admin-state 不能首次激活 PoE（<<<PAGE 62>>>）、Class 检测复位全口（<<<PAGE 62>>>）、禁延长线/雷暴作业/住宅使用（<<<PAGE 17>>>/<<<PAGE 78>>>/<<<PAGE 75>>>）。

## 三、本书在知识库中的位置

与 aos810 软件手册（配置/管理）互补提供 6360 硬件底座；与 hw-6465（工业加固）、hw-6560（多千兆 bt）构成接入家族三线——6360 定位入门千兆、内置单电源、预算上限 760W。跨书易混点：Priority Disconnect 同级裁决在 6360 为"端口号 1 高 48 低"；混插规则本机型不适用（电源内置）。

## 来源
OmniSwitch 6360 Hardware Users Guide（Part No. 060711-00, Rev. J, 2025-12）。verified.md：cases C1-C24；principles P1-P40；counter-examples X1-X25；frameworks F1-F3；glossary 约 62 条。
