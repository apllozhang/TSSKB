---
name: ALE 光模块型号体系与速率距离矩阵（1G→400G）
description: 需要为 OmniSwitch 选光模块/DAC/AOC 型号、按速率（1G/10G/25G/40G/50G/100G/200G/400G）与距离档位（DAC/AOC/SR/LR/ER/ZR/EZX）选型、核对功耗温度 DDM 参数时使用。
source_book: OmniSwitch AOS Release 8 Transceivers Guide (8.10R4)
---

## R（触发场景）
- 新建/扩链路要定光模块 PN：多远距离、什么光纤、什么封装
- 机柜内短距用 DAC 还是跨柜用 AOC/光纤
- 单纤（BX BiDi）链路两端 PN 配对
- 400G/200G 新平台（6920/6870）模块选型
- 核对模块功耗（散热预算）、温度档（商用/工业）、DDM 支持度

## I（核心理念）
速率代际 × 距离档位矩阵（F2，<<<PAGE 18-63>>>）：列=封装（SFP→SFP+→SFP28→QSFP+→SFP56→QSFP28→QSFP56→QSFP-DD），行=距离档（DAC 0.4-7m→AOC 10-20m→MMF SR 70-400m→SMF CLR/FR 2km→LR 10km→ER/LH40 40km→DR4 500m→LH70 70km→ZR 80km→EZX 120km）；选型先定距离再定封装，同距离多封装时用功耗与 DDM 支持度决胜。光模块选型三查法（F1，<<<PAGE 18-107>>>）：一查 Ch1 规格表（速率/距离/连接器/DDM/功耗）→二查 Ch2 兼容矩阵（平台×最低 AOS 版本）→三查脚注排除项。距离档位体系（P26）：LR/CLR=10/2km、LH40/ER=40km、LH70=70km、ZR=80km、EZX=120km；MMF 按 OM2/OM3/OM4 递减表。单双纤配对原则（P25）：BX 系列 D/U 成对（一端 D 发 1490/收 1310，另一端 U 反之），设计单纤链路两端 PN 必须配对下单。

## A1（决策框架）
1. **先定距离与介质**：机柜内（≤7m）→DAC；跨柜短距（10-20m）→AOC；楼内多模→SR/ESR（按 OM2/3/4）；园区单模→CLR/FR 2km 或 LR 10km；城域→ER/LH40 40km；长途→ZR 80km/EZX 120km（EZX 已停购）
2. **再定速率封装**：1G SFP→10G SFP+→25G SFP28→40G QSFP+→50G SFP56→100G QSFP28→200G QSFP56→400G QSFP-DD
3. **单纤场景 BX 配对**：D/U 两端成对；100FX 与双速 DUAL 系列同理
4. **决胜参数**：功耗梯度（1G/10G ≤1-1.5W→400G 高达 10-12W，P23）；温度档（商用 0-70°C vs 工业 iSFP -40~85°C，P24）；DDM 支持度（DAC/铜口/部分 BiDi 无 DDM，X31）
5. **停购物料甄别**：EZX/##CWD/EXTND/DUAL-SM10/SR-BD 等已停购（No longer purchasable），存量可用新项目不选（X32）

## A2（操作步骤）·速率档代表型号速查
- **1G**：SFP-GIG-SX（多模 300/550m）、LX（单模 10km）、LH40（40km）、LH70（70km）、EZX（120km，停购）、T（铜口 100m）、BX-D/U 及 BX20/BX40 变体（单纤配对）（<<<PAGE 18-24>>>）
- **双速/100FX**：SFP-DUAL-MM/MM-N（100FX+1000LX）、DUAL-BX-D/U；SFP-100-LC-MM/SM15/SM40、BXLC-D/U（<<<PAGE 25-31>>>）
- **10G**：SR（OM3 300m，1W）、LR（10km）、ER（40km，1.5W）、LRM（220m）、ZR（80km）、T（铜口 30m，2.5W）、C（DAC 0.6-7m）、GIG-SR/LR 双速过渡件、BX-D/U 10/40km、CWDM（<<<PAGE 32-39>>>）
- **25G SFP28**：SR（OM4 100m）、ESR（OM4 300m）、LR（10km）、CLR（2km）、A20M、C（DAC 1/3/5m）、BX-D40/U40（<<<PAGE 40-43>>>）
- **40G QSFP+**：SR（OM4 150m，4X10G 拆分）、LR（10km）、ER（40km）、CLR（2km）、PSM4（MPO 10km）、C（DAC）、4X10G-SR/C 拆分件、AOC20M、OS6860-CBL 20G VFL 专用线（<<<PAGE 44-50>>>）
- **50G SFP56**：SR（OM4 100m，3.3W）、FR（2km）、LR（10km）、C（DAC）——仅 6870-LNI-U6 支持（<<<PAGE 51-52>>>）
- **100G**：SR4（OM4 100m，4X25G 拆分）、LR4（10km）、CLR4（2km）、ER4（40km，4.5W）、CWDM4（2km）、A20M（20m）、C（DAC）、SR1.2/PSM4（8.10R4 新品）（<<<PAGE 53-57>>>）
- **200G**：SR4（OM4 100m，4.5W）、FR4（2km，6W）、A20M、C、2XQ100/2XQ200 拆分线（<<<PAGE 58-60>>>）
- **400G QSFP-DD**（均 8.10R4、仅 6920）：C（DAC 0.5-3m）、DR4（500m，10W）、FR4（2km）、LR4（10km）、A10M（10m）、SR4.2（OM4 100m，可拆 4×SR1.2，12W）、2Q100-C 拆分线（<<<PAGE 61-63>>>）
- **PON/工业**：3FE46541AA（GPON ONT）、3FE49327AA（XGS-PON ONT）；iSFP 全家族 -40~85°C（配 6465/6865/6575 工业平台），iSFP-10G-C 与商用同件互换（<<<PAGE 64-73>>>）

## E（实证案例）
- 本书无配置流程案例（纯规格手册）；"场景"即选型决策：按 A1 五步走完得 PN，再到 aos-tx-platform-compat 核对该 PN 在目标平台的最低 AOS 版本

## B（反例/坑）
- 使用非 ALE 认证 PN 的模块被禁止、性能无保障且失保（P2，<<<PAGE 1>>>）
- 双速模块建议两端手工配速防速率失配（P15，<<<PAGE 25>>>）
- DAC 三级长度体系：1G 无 DAC；机柜内用 DAC、跨柜用 AOC/光纤（P11，<<<PAGE 34-63>>>）
- 长距模块温度上限收窄：LH40/LH70/EZX 上限收窄到 -10/-5~70°C（P24）
- 10G-ER 损伤阈值 4dBm、ZR 过载 -7dBm——长距链路做光功率预算时注意（<<<PAGE 33>>>/<<<PAGE 34>>>）
- 40G SR4 的 DDM 仅 V/T/mA/Input 四项；SR-BD/A20M/铜口 T 系列等无 DDM，无法用 DDM 做光功率监控（X31，<<<PAGE 20-63>>>）
- QSFP-QSFP MPO 直连必须 Type-B 交叉线（8 芯使用）（glossary，<<<PAGE 17>>>）
- 10G-GIG-SR/LR 双速按光纤分级：OM1 33m@10G、OM3 300m@10G——旧布线升级的过渡件（P29）

## 来源
OmniSwitch AOS Release 8 Transceivers Guide Ch1 各速率节（<<<PAGE 18-73>>>）。条目来源：principles P2/P11/P15/P23/P24/P25/P26/P29；counter-examples X31/X32；frameworks F1/F2；glossary 各速率组。
