# DIGEST — OmniSwitch 6865 Hardware Users Guide 精华

本书是 ALE 加固型（hardened）千兆/10G 工业交换机 OS6865 家族的硬件手册（76 页，3 个固定配置机型 P16X/U12X/U28X）。核心卖点：无风扇宽温 -40~74°C、五种安装形态（机架/桌面/DIN 导轨/墙装/DNV 船用）、外置托盘式双电源（AC 180W/DC 180·140W）、75W HPoE/60W bt 口、Dying Gasp 掉电告别与 1588v2 精密时间同步。全书沿"安装→上电→供电→PoE"生命周期展开。

## 一、知识地图（三技能单元）

1. **机型与端口体系**（os6865-model-ports）：三机型选型矩阵、HPoE/bt 口位、宽温三档包络、工业合规族（Ch1/Ch2，p9-50）。
2. **安装与供电**（os6865-install-power）：五形态决策树、电源托盘/DB-15、DC 极性军规、高温降额预算（Ch1/Ch2，p13-57）。
3. **运维与排障**（os6865-ops-troubleshoot）：lanpower 全族、DG 三通道、Priority Disconnect 四场景、LED 启动判读（Ch1-Ch3，p38-64）。

## 二、三单元要点串讲

### 1. 机型与端口：PoE 密度 vs 上行密度
三机型（F1，<<<PAGE 42>>>-<<<PAGE 48>>>）：P16X=半宽 2RU，2 SFP+ + 2 SFP + 4×75W HPoE/bt + 8×PoE+，供电密集；U12X=半宽 2RU，2 SFP+ + 6 SFP + 4 HPoE，光纤上行紧凑；U28X=全宽 1RU，4 SFP+ + 20 SFP + 4 HPoE + 2×QSFP+ VFL（唯一可 VC 堆叠）。无风扇（P3），TMRA 三档（P9）：有气流 74°C/无气流 65°C/DNV 盖一律 55°C；74°C 必须封闭机柜（<<<PAGE 9>>>）。1588v2 全家族支持，工业合规覆盖变电站（IEC 61850-3）/铁路（EN 50121-4）/交通（NEMA TS-2）/船用（DNV 2.4）。

### 2. 安装与供电：五形态与三环校验
安装形态决策树（F3）：机架（侧装托盘，U28X 加 REAR-MNT）→桌面（后装托盘+桌脚，散热片面朝外）→DIN 导轨（垂直装仅限不可燃表面）→墙装→DNV 全/半架。供电=外置托盘+DB-15（P5）：AC OS6865-BP 180W / DC OS6865-BP-D（-24V 输入预算再低 20-40W）。三环校验框架（F2）：环境环（温度定气流与间隙档）→电源环（AC/DC×单双×分电路）→PoE 环（电源×温度档查表，双 BP@60°C=300W、@65°C=150W 腰斩）。DC 极性军规（P21，<<<PAGE 53>>>）：无论 -24V/-48V 一律正接正负接负，勿看标签极性符号。

### 3. 运维与排障：两级激活与 DG 三通道
PoE 两级激活（P27）：软件默认使能，仍须逐 slot `lanpower slot service start`。Priority Disconnect 四场景裁决（P33）：同级按物理口号 **1 最高→28 最低**。Guard Band：剩余预算<口上限拒新 PD（调低口上限放行）；不作用已在电 PD（P35）。Fast PoE（FPGA 固化数秒供电）/Perpetual PoE（软重启不断电，MCU 升级例外，P29/P30）。DG 三通道（F4，<<<PAGE 54>>>）：SNMP 前 3 站+Syslog 前 3 服务器+4×802.3ah PDU；并发 PDU 口数=10−服务器数。LED 判读纪律：启动完成前不判断 LED 状态（<<<PAGE 38>>>）；VC LED 闪烁次数=单元号（每 5 秒停顿）。

## 三、本书在知识库中的位置

6865 定位工业/交通/电力/船舶等严苛环境接入，与 hw-6465（工业加固）、hw-6560（多千兆办公）构成加固-办公两线。跨书易混点：①Priority Disconnect 端口号 1 高 28 低，与 6860 相反；②6865 无温度双阈值（无 Danger 关机），高温防护靠 TMRA 分级+预算降额，与 6860/6870 不同；③6865 HPoE 口 75W/60W bt 双兼容，与 6860 E 代非 bt 合规的私有 HPoE 不同；④供电为外置托盘 DB-15，非内置电源舱。

## 来源
OmniSwitch 6865 Hardware Users Guide（Part No. 060435-10, Rev. Y, 2025-12）。verified.md：cases C1-C36；principles P1-P40；counter-examples X1-X45；frameworks F1-F4；glossary 约 60 条。
