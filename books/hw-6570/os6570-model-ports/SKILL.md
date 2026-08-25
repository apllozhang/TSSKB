---
name: OmniSwitch 6570M 机型与端口体系（12/12D/U28 选型、SFP+ 上联堆叠、combo）
description: 需要在 OS6570M-12/12D/U28 三机型间选型、解码端口面板（铜光混合/combo/Uplink-Stacking SFP+）、核对半宽双机并排与待机功耗、规划 Virtual Chassis 堆叠口时使用。
source_book: OmniSwitch 6570M Hardware Users Guide
---

## R（触发场景）
- 6570M 家族选型：12（铜口小规模）/12D（直流场景）/U28（全光密集）三选一
- 解码面板端口：铜口/SFP/SFP+ 口位、combo 21-24、Uplink/Stacking 双角色口
- 规划 Virtual Chassis 堆叠链路口位（12 口机 11-12，U28 机 25-30）
- 半宽机双机 1U 并排（DUO-MNT）的端口/空间核算

## I（核心理念）
6570M 选型三轴矩阵（F1，<<<PAGE 11>>>/<<<PAGE 22>>>/<<<PAGE 26>>>/<<<PAGE 35>>>）：轴一=下行口形态（12/12D=8 铜口+2 SFP 混合，柜边小汇聚；U28=20 纯 SFP+4 combo 全光，光纤入柜）；轴二=供电制式（12=内置 AC、12D=内置 DC 宽压）；轴三=上联与堆叠需求（12/12D=2 个 SFP+、U28=6 个 SFP+）。核心机制：Uplink/Stacking SFP+ 口为 1G/10G 双角色——同一口既做上联又做 Virtual Chassis 堆叠链路（P2，<<<PAGE 11>>>/<<<PAGE 21>>>/<<<PAGE 25>>>）；U28 combo 口同口位光铜互斥（P3）。本家族无 PoE、全机型不支持半双工（X1，<<<PAGE 21>>>/<<<PAGE 23>>>/<<<PAGE 25>>>）。

## A1（行动框架）
1. 按物理环境定包络：12/12D=半宽 21.72cm×28.07cm×1.7kg；U28=全宽 44cm×35cm×4.08kg（P5，<<<PAGE 22>>>/<<<PAGE 24>>>/<<<PAGE 26>>>）
2. 按业务定端口：铜口接终端选 12/12D；全光汇聚选 U28（20×SFP + 4 combo 21-24 + 6×SFP+ 25-30）
3. 按堆叠定上联口预算：12 口机堆叠占 11-12 两口；U28 有 6 个 SFP+ 可分摊上联与堆叠（P2）
4. 半宽空间利用框架（F2，<<<PAGE 28>>>-<<<PAGE 34>>>/<<<PAGE 5>>>）：两台 12 并排=16 铜口+4 SFP+4 SFP+ 上联/堆叠口，深度 28cm 仍省机架空间
5. 按功耗定供电：待机 12=23W、12D=24W、U28=71W——光口密度推高基线（P6，<<<PAGE 22>>>/<<<PAGE 24>>>/<<<PAGE 26>>>）

## A2（操作步骤）
- 面板核对：12/12D=8×10/100/1000Base-T + 2×100/1000Base-X SFP + 2×SFP+（11-12）；U28=20×SFP + 4×combo（21-24）+ 6×SFP+（25-30）（P1，<<<PAGE 11>>>）
- combo 口使用：同口位 SFP 光口与 RJ45 铜口二选一，不可同时（P3，<<<PAGE 11>>>/<<<PAGE 25>>>）
- VC 识别：U28 独有 Virtual Chassis ID LED；VC LED 稳绿=master/稳琥珀=slave/闪琥珀以次数报 unit 号（P26，<<<PAGE 25>>>/<<<PAGE 27>>>）
- 端口 LED 判读：稳绿=有效链路、闪绿=链路活动，全绿色系无 PoE 维度（P27，<<<PAGE 27>>>）

## E（实证案例）
- U28 全光上联型面板构成与双电源舱布局（P1/P18，<<<PAGE 11>>>/<<<PAGE 25>>>）
- 半宽双机并排后端口总量核算（F2，<<<PAGE 32>>>-<<<PAGE 34>>>）

## B（反例与坑）
- 全机型不支持半双工连接（X1，<<<PAGE 21>>>/<<<PAGE 23>>>/<<<PAGE 25>>>）
- combo 口光铜互斥，按两口配置会失效（P3，<<<PAGE 25>>>）
- 上联/堆叠共用 SFP+ 口：堆叠占口后上联带宽同步受挤，规划时先留堆叠口（P2）
- 待机功耗梯度差 3 倍：U28 71W，按 12 机型 23W 估算供电会低估（P6）

来源：OmniSwitch 6570M Hardware Users Guide（Ch1/Ch3，p11-34）
