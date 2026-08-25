# GLOSSARY · OmniSwitch 6865 Hardware Users Guide

> 页码为原书 `<<<PAGE N>>>` 标记。按机型/电源/PoE/安装/LED/合规分组，精选 45 条。

## 机型与形态
- **OmniSwitch 6865-P16X**：16 口 PoE 加固型，2 SFP+ + 2 SFP + 4×75W HPoE/bt + 8×PoE+，半宽 2RU，待机 30W <<<PAGE 42>>>/<<<PAGE 44>>>
- **OmniSwitch 6865-U12X**：12 口上行型，2 SFP+ + 6 SFP + 4 HPoE，半宽 2RU，待机 29W <<<PAGE 45>>>/<<<PAGE 46>>>
- **OmniSwitch 6865-U28X**：28 口上行型，4 SFP+ + 20 SFP + 4 HPoE + 2 QSFP+ VFL，全宽 1RU，待机 50W <<<PAGE 47>>>/<<<PAGE 48>>>
- **加固型（Hardened）**：面向严苛电气与宽温环境（-40~74°C）设计的交换机品类 <<<PAGE 42>>>
- **半宽 2RU / 全宽 1RU**：P16X/U12X 为 8.5 英寸宽 2RU；U28X 为 17.2 英寸宽 1RU <<<PAGE 42>>>/<<<PAGE 47>>>
- **TMRA**：最大额定环境温度，封闭机架内按此折减 <<<PAGE 9>>>
- **VFL（QSFP+ VFL Ports）**：U28X 后部 29/30 口的 QSFP+ 虚拟光纤链路端口 <<<PAGE 49>>>
- **1588v2**：IEEE 精密时间同步协议，全家族支持（电力/工业场景）<<<PAGE 43>>>
- **DNV**：挪威船级社；DNV 2.4 船用认证，装 DNV 电源盖后温度限 55°C <<<PAGE 42>>>/<<<PAGE 68>>>

## 电源与供电（Ch2）
- **OS6865-BP**：180W 模块化 AC 电源（100-240VAC，+56VDC/3.22A 输出），最多 2 个 <<<PAGE 49>>>
- **OS6865-BP-D**：180W/140W 模块化 DC 电源（-20~-28V/12A 或 -36~-72V/6A 输入），最多 2 个 <<<PAGE 50>>>
- **电源托盘（Power Supply Tray）**：承载 1-2 个外置电源的托架，侧装（机架）/后装（桌面）<<<PAGE 13>>>
- **DB-15 连接器（带导向销）**：电源与机箱之间供电接口 <<<PAGE 19>>>/<<<PAGE 50>>>
- **Dying Gasp**：掉电告别机制——全电源丢失瞬间发 SNMP trap/Syslog/Link OAM PDU 后关机 <<<PAGE 53>>>
- **DC 极性军规**：无论 -24V/-48V 输入，正接正负接负，不受电源标签极性符号影响 <<<PAGE 53>>>
- **SELV / AHJ**：安全特低电压源；DC 线超 3 米须咨询地方电气管理机构 <<<PAGE 51>>>
- **DC 回流（DC Return）**：DC 回流导体接设备机框，各电源共用 <<<PAGE 51>>>
- **12AWG / 22AWG**：DC 供电线双导体线规 / 接地引线线规 <<<PAGE 51>>>/<<<PAGE 73>>>
- **Panduit LCD8-10AL**：后部接地 lug（8AWG、30-60 in-lb）<<<PAGE 73>>>
- **CDE（Cable Discharge Event）**：电缆静电放电，接线前先对地放电 <<<PAGE 11>>>

## PoE（Ch3）
- **PoE 预算（PoE Power Budget）**：按电源数量/类型与温度三档查表的可供电总瓦数 <<<PAGE 56>>>/<<<PAGE 57>>>
- **HPoE 口（75W）**：支持 75W HPoE 或 60W 802.3bt 的 RJ45 口 <<<PAGE 44>>>/<<<PAGE 46>>>/<<<PAGE 48>>>
- **PD / PSE**：受电设备（AP/话机/摄像头）/供电设备 <<<PAGE 57>>>/<<<PAGE 11>>>
- **Class 检测**：按 802.3at 分 Class 0-4 限功率；默认关闭，开启复位全部 PoE 口 <<<PAGE 57>>>/<<<PAGE 58>>>
- **Fast PoE / Perpetual PoE**：上电数秒供电（FPGA 固化）/软重启不断 PD 电（MCU 升级例外）<<<PAGE 59>>>
- **Guard Band**：剩余预算小于口上限/类最大值时拒载新 PD <<<PAGE 63>>>
- **Priority Disconnect**：预算不足按优先级+物理口号（1 最高→28 最低）裁决；默认启用 <<<PAGE 61>>>/<<<PAGE 62>>>
- **电容检测（Capacitor Detection）**：老式 IP 话机兼容检测法，不符 IEEE，默认禁用 <<<PAGE 61>>>
- **lanpower slot service**：逐 slot 物理激活/停止 PoE（首次激活唯一途径）<<<PAGE 56>>>/<<<PAGE 58>>>
- **lanpower power / slot maxpower**：单口/整槽功率上限（不做预留）<<<PAGE 59>>>/<<<PAGE 60>>>
- **lanpower priority**：三级口优先级 low/high/critical（默认 low）<<<PAGE 60>>>/<<<PAGE 61>>>
- **lanpower slot fpoe / ppoe**：开启 Fast PoE / Perpetual PoE <<<PAGE 59>>>
- **lanpower slot priority-disconnect**：开关 priority disconnect（默认启用）<<<PAGE 62>>>
- **show powersupply / show lanpower slot**：电源状态 / PoE 状态与可用功率 <<<PAGE 57>>>
- **UPS / 911 纪律**：带 IP 话机的 PoE 交换机须电源冗余+UPS <<<PAGE 56>>>

## 链路与告警（Ch2）
- **Link OAM / 802.3ah**：链路层 OAM 协议；DG 经其 PDU 上报 <<<PAGE 54>>>
- **efm-oam propagate-events dying-gasp**：口级 DG OAM PDU 使能命令 <<<PAGE 54>>>
- **snmp station / swlog output socket**：DG 接收端配置（前 3 生效）<<<PAGE 54>>>
- **DG PDU 并发限额**：同时发 PDU 口数=10−已配 SNMP/Syslog 服务器数 <<<PAGE 54>>>/<<<PAGE 55>>>

## 安装部件与套件（Ch1）
- **OS6865-REAR-MNT**：U28X 机架后固定套件（侧导轨+前/后支架）<<<PAGE 21>>>/<<<PAGE 22>>>
- **OS6865-TRAY-1U / OS6865-DIN-MNT**：1U 并排装两托盘的机架套件 / DIN 导轨安装套件（电源与机箱可分别拆装）<<<PAGE 21>>>/<<<PAGE 24>>>/<<<PAGE 26>>>
- **OS6865-DNV-FRCK / HRCK**：DNV 全架/半架套件（含电源托盘 182343-10、电源盖）<<<PAGE 28>>>
- **桌脚（Table Mount Feet）**：提供桌面底部 1/2 RU 间隙的必备脚垫 <<<PAGE 16>>>
- **DB9-RJ45 连接器 / 拇指螺丝**：随箱串口转接头 / 电源免工具固定螺丝 <<<PAGE 12>>>/<<<PAGE 18>>>

## LED 与管理（Ch1）
- **OK LED**：稳绿=正常/闪绿=诊断中/稳琥珀=软件错误 <<<PAGE 38>>>
- **VC LED**：闪绿=Master/闪琥珀=Slave；闪烁次数=VC 单元号（每 5 秒停顿）<<<PAGE 38>>>
- **PS1/PS2 LED**：灭=不在位/稳绿=正常/稳琥珀=故障 <<<PAGE 38>>>
- **端口 LED 颜色**：RJ45 绿=非 PoE/琥珀=PoE；SFP 琥珀=100M；闪烁=活动 <<<PAGE 38>>>
- **admin/switch / aaa authentication**：默认登录与会话解锁（一次一类）<<<PAGE 39>>>

## 标准与合规（附录 A）
- **ISA 12.12.01 (UL 1604)**：危险场所工业安全标准 <<<PAGE 67>>>
- **IEC 61850-3 / IEEE 1613**：变电站/电力环境 EMC 标准 <<<PAGE 67>>>
- **EN 50121-4 / IEC 62236-4**：铁路应用 EMC 标准 <<<PAGE 68>>>
- **NEMA TS-2**：交通控制设备标准 <<<PAGE 68>>>
- **UL 62368-1 / FCC Part 15 Class A**：设备安全/商用 EMC（住宅禁用）<<<PAGE 65>>>/<<<PAGE 70>>>
- **受限场所（Restricted Access Location）**：仅持钥匙/安保措施的维护人员可进入 <<<PAGE 74>>>
