---
name: OmniSwitch 6865 机型与端口体系（加固型三机型/HPoE 75W/无风扇宽温/DNV 船用）
description: 需要选型 OS6865 三机型（P16X/U12X/U28X）、核对加固型端口构成（75W HPoE/bt 口、SFP+ 上行、QSFP+ VFL）、理解无风扇宽温分级（-40~74°C）与半宽 2RU/全宽 1RU 形态时使用。
source_book: OmniSwitch 6865 Hardware Users Guide
---

## R（触发场景）
- 加固场景选型：在 P16X/U12X/U28X 三机型中按 PoE 密度 vs 上行密度选
- 解码命名：P=PoE 电机型、U=上行口密集、数字=端口总数、X=含 SFP+ 10G 上行
- 核对 75W HPoE / 60W bt 口位与 SFP/SFP+/QSFP+ 上行构成
- 宽温部署核对：-40~74°C（需气流）/65°C（免气流）/55°C（DNV 盖）三档
- 工业合规核对（IEC 61850-3 变电站/EN 50121-4 铁路/NEMA TS-2 交通/DNV 2.4 船用）

## I（核心理念）
6865 是加固型（hardened）千兆/10G 交换机家族（P1，<<<PAGE 42>>>）："designed for demanding electrical and severe temperature environments"。三机型分工（F1，<<<PAGE 42>>>-<<<PAGE 48>>>）：P16X=PoE 供电密集（4×75W HPoE/bt + 8×PoE+）；U12X=光纤上行紧凑型；U28X=大量光纤上行 + 2×QSFP+ VFL。四条家族铁律：全无风扇（P3，散热全靠机箱散热片+外部气流）；机箱两档（半宽 2RU/全宽 1RU，P4）；TMRA 三档温度包络（P9：有气流 -40~74°C、无气流 -40~65°C、DNV 盖一律 55°C）；1588v2 精密时间同步全家族支持（电力/工业场景）。

## A1（行动框架）
1. 选型三问（F1）：现场要给多少 75W 大功率 PD？→P16X；要多少路上行？→U12X（8 光）/U28X（24 光+2 VFL）；要不要 VC 堆叠？→仅 U28X 有 QSFP+ VFL
2. 温度档核对（F2 环境环）：现场最高温 <65°C 免气流；≥65°C 必须气流；74°C 还必须封闭机柜/机架（X2，<<<PAGE 9>>>）；装 DNV 盖一律按 55°C 降额（X3）
3. 顶部间隙按温度分档：机架 <65°C 留 1/2 RU、≥65°C 留 1 RU；侧 2"/前后 6"（P13，<<<PAGE 11>>>/<<<PAGE 12>>>）
4. 端口功率域核对：HPoE 口默认 75000mW、bt 口 60000mW、PoE+ 口 30000mW（P26，<<<PAGE 56>>>）

## A2（操作步骤）
- **面板识别**：P16X=2 SFP+ + 2 SFP + 4 HPoE/bt + 8 PoE+（半宽 2RU）；U12X=2 SFP+ + 6 SFP + 4 HPoE；U28X=4 SFP+ + 20 SFP + 4 HPoE + 2 QSFP+ VFL（29/30 口）（P2，<<<PAGE 44>>>/<<<PAGE 46>>>/<<<PAGE 48>>>）
- **LED 判读**：OK（稳绿=正常/闪绿=诊断中/稳琥珀=软件错误）；VC（闪绿=Master/闪琥珀=Slave，闪烁次数=单元号，每 5 秒停顿）；PS1/PS2（稳绿=正常/稳琥珀=故障/灭=不在位）（P38，<<<PAGE 38>>>）
- **端口 LED 颜色**：RJ45 绿=非 PoE 链路、琥珀=PoE 设备已接、闪烁=有活动；SFP 琥珀=100M（P39，<<<PAGE 38>>>）
- **console 连接**：RJ45 Console 口 + 随箱 DB9-RJ45 转接头，9600-8N1（<<<PAGE 12>>>/<<<PAGE 39>>>）
- **待机功耗核对**：P16X=30W、U12X=29W、U28X=50W（P8）

## E（实证案例）
- P16X 16 口 PoE 部署构成：4×75W HPoE/bt + 8×PoE+ + 2 SFP+ + 2 SFP，面向话机/AP/摄像头密集供电（F1，<<<PAGE 42>>>/<<<PAGE 44>>>）
- U28X 大规模光纤上行：4 SFP+ + 20 SFP + 4 HPoE + 2×QSFP+ VFL，全宽 1RU（17.2" 宽），VC 堆叠走 VFL（<<<PAGE 47>>>/<<<PAGE 49>>>）
- 高温机房部署核对链：74°C →必须封闭机柜+气流+顶部 1 RU 间隙（X1/X2，<<<PAGE 9>>>/<<<PAGE 11>>>）

## B（反例与坑）
- 65°C 是气流硬阈值：低于 65°C 免气流、≥65°C 必须气流（X1，<<<PAGE 11>>>）；74°C 必须封闭机柜（X2，<<<PAGE 9>>>）
- DNV 电源盖降额：装盖后无论有无气流上限都降到 55°C（X3，<<<PAGE 42>>>/<<<PAGE 45>>>/<<<PAGE 47>>>）
- 三机型均不支持半双工（X38，<<<PAGE 44>>>/<<<PAGE 46>>>/<<<PAGE 48>>>）
- 高温下 PoE 预算腰斩：P16X/U12X 双电源 65°C/74°C 从 300W 降到 150W——选型勿按常温预算外推（X31，<<<PAGE 56>>>）
- 激光辐射：空光口勿直视，拆线后加盖（X34，<<<PAGE 72>>>）
- 跨书易混：6865 的 HPoE 口为 75W/60W bt 双兼容，与 6860 E 代"not 802.3bt compliant"的私有 HPoE 不同，对 bt PD 互通性更好

来源：OmniSwitch 6865 Hardware Users Guide（Ch1 p9-12/p38 + Ch2 p42-50）
