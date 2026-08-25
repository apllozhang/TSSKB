# Verified 候选（V1 原文真实性核对 + V2/V3 抽查）

## counter-examples

## 端口级与许可限制
- **X1** 6560 X4 系列 10G 解锁口：24X4/P24X4 口 25/26、48X4/P48X4 口 49/50 需 OS6560-SW-PERF 许可才跑 10G，默认 1G <<<PAGE 82>>>
- **X2** SFP-10G-LRM 在 6560 上仅限特定口：48X4/P48X4 的 49-50（需 PERF 许可）与 51/52、P48Z16(904044-90) 的 49-52、X10 的 1-8 <<<PAGE 82>>>
- **X3** 6560 的 SFP-10G-C7M 排除口：(P)24Z24、(P)24Z8、(P)24X4 及 (P)48X4 的口 53/54；X10 整机不支持 40G DAC <<<PAGE 82>>>
- **X4** 6860E-U28 上行口限 1G：所有 6860 上行口用 SFP-GIG-T 只跑 1G；用户口 1-28 支持 10/100/1000；手工设 10M 必须先插模块再设速 <<<PAGE 89>>>
- **X5** 6860E-U28 上 DUAL 系列仅用户口 100/1000：上行口仅 1G；SFP-10G-GIG-SR/LR 不支持 U28 的 1G SFP 用户口（1-28）<<<PAGE 89>>>
- **X6** 6860N SFP28 口模块禁用清单：SFP-GIG-T/SFP-1G-T 不支持 SFP28 口；DUAL-BX/SFP-100 系列在 SFP28 口仅 1G；SFP-10G-T 在 SFP28 口支持 1G+10G <<<PAGE 92>>>
- **X7** 6900 每机箱 SFP-10G-T 上限 38 只 <<<PAGE 102>>>
- **X8** 6360 的 10G 口位因型号而异：SFP-10G 支持口 P10(11-12)/P24(25-28)/PH24(25-28)/P48(49-52)/P24X(25-28)/P48X(49-52)；另一组（P24/PH24 27-28、P48 51-52、P24X 25-28、P48X 49-52）适用于 XGS-PON ONT——插错口位不识别 <<<PAGE 76>>>
- **X9** 6570M 10G 口仅 U28 的 25-30 支持 XGS-PON ONT；SFP-GIG-T 不支持 U28 combo 口 <<<PAGE 85>>>/<<<PAGE 84>>>
## 平台级 N/S（选型红线）
- **X10** 6920 只认 40G 及以上：全部 SFP/SFP+/SFP28 模块与 50G SFP56 均 N/S（含 SFP-10G/25G 全系），仅 QSFP+/QSFP28/QSFP56/QSFP-DD 可用（均 8.10R4 起）<<<PAGE 103>>>/<<<PAGE 104>>>
- **X11** 6900-V72/C32/C32E 不支持任何 1G/100FX SFP（全系 N/S），10G SFP 仅 V72 支持 <<<PAGE 97>>>/<<<PAGE 98>>>
- **X12** 6560 不支持 40G LR/ER/CLR/PSM4/LM4 光模块与 QSFP-4X10G 拆分（仅 SR/AOC/VFL 用 DAC）；QSFP-40G-C7M 在 6560 标注 Not supported <<<PAGE 81>>>
- **X13** 6860（除 U28）与 6860E-U28 的差异：DUAL 系列 6860 主型 N/S 而 U28 支持；100 系列 SFP 仅 U28 支持 <<<PAGE 87>>>
- **X16** 6870-P24M/P48M（万兆铜主机型）不支持任何 1G/100 SFP（N/A 列）——1G 接入必须靠 P24Z/48/V12 等机型 <<<PAGE 94>>>
- **X17** SFP-50G 系列仅 6870-LNI-U6 支持（8.10R2），其余平台全 N/S <<<PAGE 96>>>
- **X18** QSFP-200G 仅 6870 的 P24M/P48M/V12（上联口）与 6920 支持，24/48/P24Z/P48Z 数据口不支持 <<<PAGE 96>>>/<<<PAGE 104>>>
- **X19** 400G QSFP-DD 全系仅 6920（OS6900-D32）支持 <<<PAGE 104>>>
- **X21** GPON ONT（3FE46541AA）在 6860/6865/6870/6920/9900 全不支持；XGS ONT（3FE49327AA）仅 6360/6465T/6560/6570M(U28)/6860N-P48M+XNI-U4 支持 <<<PAGE 89>>>/<<<PAGE 93>>>等
- **X22** 9900 板卡级差异巨大：1G SFP 仅 XNI-U48/GNI-U48/XNI-U24 支持；100G QSFP 仅 CMM2/CNI-U8/CNI-U20 支持（且 CMM/CMM2 的 QSFP 要 8.9R3）<<<PAGE 105>>>-<<<PAGE 107>>>
- **X24** "或"版本须看硬件代次：SFP-10G-ZR 在 6560 写 8.4.1.R02 or 8.6R1（2019-05 后采购需 8.6R1+）；6860 写 8.2.1 or 8.6R1；6900-V72 写 8.5R2 or 8.6R1——同型号模块不同批次最低版本不同 <<<PAGE 81>>>/<<<PAGE 88>>>/<<<PAGE 98>>>
- **X25** SFP-GIG-T/SFP-10G-T/SFP-DUAL-MM-N 双版本：新序列号/硬件修订分别需 8.9R3（AP 序列号、A53 修订）/8.10R2（V1.0 修订）<<<PAGE 20>>>/<<<PAGE 34>>>/<<<PAGE 25>>>
- **X26** QSFP-40G-C 9900↔6900 互连必须关 9900 侧自协商 <<<PAGE 48>>>
- **X27** QSFP-100G-A20M 必须关自协商+FEC RS <<<PAGE 55>>>
- **X31** DVM 无 DDM 的模块清单：全部 DAC（SFP-10G-C/QSFP-40G-C/100G-C/200G·400G 拆分线）、铜口 T 系列、SFP-GIG-##CWD、SFP-100-LC-MM/SM15、SFP-DUAL-SM10、QSFP-40G-SR-BD、QSFP-100G-A20M——这些口无法用 DDM 做光功率监控 <<<PAGE 20>>>-<<<PAGE 63>>>
- **X32** 停购物料仍在兼容表（No longer purchasable）：SFP-GIG-EZX/##CWD/EXTND、DUAL-MM/SM10、100-BX20 系列、SFP-10G-24DWD80、QSFP-40G-SR-BD/LM4、部分 iSFP 停购件——存量可继续用，新项目不可选 <<<PAGE 20>>>-<<<PAGE 73>>>
- **X33** 6860N-P48M/P24M 的 25G 模块在扩展模块 OS68-XNI-U4 上 N/S（25G 仅限主板 SFP28 上联口）；VNI-U4/QNI-U2/CNI-U1 模块的光模块支持范围各自独立 <<<PAGE 91>>>
- **X34** 6860N-U28 的 100 系列与 DUAL 系列支持、但 P24Z/P48Z 不支持——同家族机型光模块清单不通用 <<<PAGE 90>>>-<<<PAGE 92>>>
- **X35** 6465T 不支持 BX20/BX40 双纤双向 1G 模块与 XGS ONT（12 口以外）<<<PAGE 78>>>/<<<PAGE 79>>>

---
合计：35 条（X1-X35）。

## frameworks

- **F1** 光模块选型三查法（本手册用法）：一查 Ch1 规格表定速率/距离/连接器/DDM/功耗（距离按光纤类型 OM2/3/4 或 SMF 档位筛选）→ 二查 Ch2 兼容矩阵定"平台 × 最低 AOS 版本"（注意硬件修订双版本与端口级脚注）→ 三查脚注排除项（VFL 例外、SFP28 自协商、每机箱上限、PERF 许可口）。采购口诀：PN 配对（BX 必须 D/U 成对）、版本对齐（新件 8.9R3/8.10R2 门槛）、停购替代。 <<<PAGE 18>>>-<<<PAGE 107>>>
- **F2** 速率代际 × 距离档位矩阵：列=封装（SFP→SFP+→SFP28→QSFP+→SFP56→QSFP28→QSFP56→QSFP-DD），行=距离档（DAC 0.4-7m→AOC 10-20m→MMF SR 档 70-400m→MMF ESR 300m→SMF CLR/FR 2km→LR 10km→ER/LH40 40km→DR4 500m→LH70 70km→ZR 80km→EZX 120km）；选型时先定距离再定封装，同距离多封装时用功耗与 DDM 支持度决胜（如 2km 档 25G-CLR/50G-FR/100G-CLR4/CWDM4/200G-FR4/400G-FR4 全家族覆盖）。 <<<PAGE 18>>>-<<<PAGE 63>>>
- **F3** 兼容矩阵平台分型框架：全谱系型（6860N/6870/6900-X：1G~200G 全列）／上联收窄型（6560：1G+10G+40G-SR/AOC；6570M：+25G）／工业型（6465/6865/6575 用 iSFP PN 体系）／40G+ 专用型（6920 只有 QSFP；V72/C32 无 1G）／板卡拼图型（9900/6860N 按板卡逐列）。同一模块跨平台最低版本差异大（如 100G-SR4：6860N 8.7R2 / 6900 8.5R2 / 6870 8.10R2 / 6920 8.10R4），多平台混采要按最高版本对齐。 <<<PAGE 75>>>-<<<PAGE 107>>>

---
合计：3 条（F1-F3）。

## glossary

- **SFP MSA（Multi Source Agreement）**：光模块多源协议规范——20 针接口+识别串口的通用标准 <<<PAGE 13>>>
- **DDM（Digital Diagnostic Monitoring）**：数字诊断监控（温度/电压/电流/光功率）；DAC 与铜口模块普遍不支持 <<<PAGE 18>>>等
- **Bail Wire Delatch / 铰链面 / 弹出器按钮**：SFP 三种释放机构 <<<PAGE 15>>>/<<<PAGE 16>>>
- **Type-B MPO 交叉线**：QSFP↔QSFP 直连 MPO trunk 必用的交叉极性（8 芯使用）<<<PAGE 17>>>
- **MPO-LC Splitter**：40G MPO 拆 4×10G LC 的分支线 <<<PAGE 17>>>
- **DAC（Direct Attach Copper）**：无源直连铜缆（同轴拆分线）；有源版本称 AOC <<<PAGE 34>>>等
- **AOC（Active Optical Cable）**：有源光缆（模块+线缆一体）<<<PAGE 49>>>

## 1G SFP（Ch1）
- **SFP-GIG-SX**：千兆多模 850nm，300m(62.5µ)/550m(50µ)，LC，DDM 支持 <<<PAGE 18>>>
- **SFP-GIG-LX**：千兆单模 1310nm 10km，LC，DDM 支持 <<<PAGE 18>>>
- **SFP-GIG-LH40**：千兆 40km 1310nm，0~+5dBm，接收灵敏度 -22dBm <<<PAGE 19>>>
- **SFP-GIG-LH70**：千兆 70km 1550nm <<<PAGE 19>>>
- **SFP-GIG-EZX**：千兆 120km 超长距 1550nm，灵敏度 -35dBm（已停购）<<<PAGE 19>>>-<<<PAGE 20>>>
- **SFP-GIG-##CWD**：千兆 CWDM 粗波分，8 波长 1470-1610nm，62km，无 DDM（已停购）<<<PAGE 20>>>
- **SFP-GIG-T**：千兆铜口 RJ45 10/100/1000BASE-T 100m；新序列号 APxx 需 ≥8.9R3 <<<PAGE 20>>>
- **SFP-1G-T**：千兆铜口（仅 1000BASE-T，802.3ab）<<<PAGE 21>>>
- **SFP-GIG-EXTND**：千兆多模延长 2km（已停购）<<<PAGE 21>>>
- **SFP-GIG-BX-D / BX-U**：千兆单纤双向 10km 配对（D 发 1490/收 1310，U 反之）<<<PAGE 21>>>/<<<PAGE 22>>>
- **SFP-GIG-BX-D20 / U20 / D40 / U40**：单纤双向 20km/40km 配对变体 <<<PAGE 22>>>-<<<PAGE 24>>>

## 双速与 100FX（Ch1）
- **SFP-DUAL-MM / MM-N**：100FX+1000LX 双速多模（550m@1G/2km@100M）；MM-N 新件 SPG-DR-FX-CDFD-AL2 需 ≥8.9R3 <<<PAGE 25>>>
- **SFP-DUAL-SM10**：双速单模 10km（无 DDM，已停购）<<<PAGE 26>>>
- **SFP-DUAL-BX-D / U**：双速单纤双向 10km（1550/1310nm 配对）<<<PAGE 26>>>
- **SFP-100-BX20LT / BX20NU**：100M 单纤双向 20km SC 口（ITU-T G.983，已停购）<<<PAGE 28>>>
- **SFP-100-BXLC-D / U**：100M 单纤双向 20km LC 口配对 <<<PAGE 29>>>
- **SFP-100-LC-MM**：100FX 多模 2km，无 DDM <<<PAGE 30>>>
- **SFP-100-LC-SM15 / SM40**：100FX 单模 15km/40km <<<PAGE 30>>>/<<<PAGE 31>>>

## 10G SFP+（Ch1）
- **SFP-10G-SR**：10G 多模 850nm 300m（OM3），1W <<<PAGE 32>>>
- **SFP-10G-LR**：10G 单模 10km 1310nm <<<PAGE 32>>>
- **SFP-10G-ER**：10G 40km 1550nm，1.5W，损伤阈值 4dBm <<<PAGE 33>>>
- **SFP-10G-LRM**：10G 多模延长 220m（802.3aq）<<<PAGE 33>>>
- **SFP-10G-ZR**：10G 80km 1550nm，过载 -7dBm <<<PAGE 34>>>
- **SFP-10G-T**：10G 铜口 RJ45 30m CAT6a/7，2.5W，无 DDM；硬件修订 A53 需 8.9R3、V1.0 需 8.10R2 <<<PAGE 34>>>
- **SFP-10G-C（60cm/1/3/7m）**：10G DAC；iSFP-10G-C 与商用 PN 同件可互换 <<<PAGE 34>>>/<<<PAGE 25>>>
- **SFP-10G-24DWD80**：10G 80km DWDM 1558.17nm（已停购）<<<PAGE 35>>>
- **SFP-10G-GIG-SR / GIG-LR**：10G/1G 双速（OM3 300m@10G；LR 10km）<<<PAGE 36>>>
- **SFP-10G-BX-D / U（10/40km）**：10G 单纤双向 1330/1270nm 配对；不支持 VFL <<<PAGE 37>>>/<<<PAGE 38>>>
- **SFP-10G-CWDM**：10G CWDM 40km 1551nm，-40~85°C <<<PAGE 39>>>

## 25G SFP28（Ch1）
- **SFP-25G-SR**：25G 多模 850nm（OM2 20m/OM3 70m/OM4 100m），802.3by <<<PAGE 40>>>
- **SFP-25G-ESR**：25G 扩展多模 OM4 300m <<<PAGE 41>>>
- **SFP-25G-LR**：25G 单模 10km（802.3cc）<<<PAGE 41>>>
- **SFP-25G-CLR**：25G 单模 2km <<<PAGE 42>>>
- **SFP-25G-A20M**：25G AOC 20m <<<PAGE 42>>>
- **SFP-25G-C（1/3/5m）**：25G DAC <<<PAGE 42>>>
- **SFP-25G-BX-D40 / U40**：25G 单纤双向 40km（1310/1270nm），-40~85°C <<<PAGE 43>>>

## 40G QSFP+（Ch1）
- **QSFP-40G-SR**：40G SR4 MPO-12 多模（OM3 100m/OM4 150m），支持 4X10G 拆分；DDM 仅 V/T/mA/Input <<<PAGE 44>>>
- **QSFP-40G-SR-BD**：40G 双向双通道 LC 多模（BiDi），3.5W，无 DDM、不支持 VFL（已停购）<<<PAGE 44>>>/<<<PAGE 45>>>
- **QSFP-40G-LR**：40G LR4 LC 单模 10km（4 波长 1264.5-1337.5nm）<<<PAGE 45>>>
- **QSFP-40G-ER**：40G ER4 LC 单模 40km（802.3bm）<<<PAGE 45>>>
- **QSFP-40G-LM4**：40G 多模 LC（OM3 140m，已停购）<<<PAGE 46>>>
- **QSFP-40G-CLR**：40G 单模 2km（LR4 Lite 类）<<<PAGE 46>>>
- **QSFP-40G-PSM4**：40G 并行单模 MPO-12 10km，支持 4X10G 拆分 <<<PAGE 47>>>
- **QSFP-40G-C（40cm/1/3/7m）**：40G DAC；7m 跨厂商需验证、9900↔6900 要关自协商 <<<PAGE 47>>>/<<<PAGE 48>>>
- **QSFP-4X10G-SR**：40G 拆 4×10G 光模块（MPO，OM3 300m）<<<PAGE 48>>>
- **QSFP-4X10G-C（1/3/5m）**：40G→4×10G DAC 拆分线 <<<PAGE 48>>>
- **QSFP-40G-AOC20M**：40G AOC 20m（多数平台限 VFL 连接）<<<PAGE 49>>>
- **OS6860-CBL-40/100/300**：20G VFL 专用 QSFP DAC（40cm/1m/3m）<<<PAGE 49>>>/<<<PAGE 50>>>

## 50G SFP56（Ch1）
- **SFP-50G-SR**：50G 多模 850nm OM4 100m，3.3W <<<PAGE 51>>>
- **SFP-50G-FR**：50G 单模 2km（1311nm）<<<PAGE 51>>>
- **SFP-50G-LR**：50G 单模 10km <<<PAGE 52>>>
- **SFP-50G-C（50cm/1/3m）**：50G DAC（-20~75°C）<<<PAGE 52>>>

## 100G QSFP28（Ch1）
- **QSFP-100G-SR4**：100G SR4 MPO 多模（OM3 70m/OM4 100m），支持 4X25G 拆分 <<<PAGE 53>>>
- **QSFP-100G-LR4**：100G LR4 LC 单模 10km（4 波长 1294.53-1310.19nm）<<<PAGE 53>>>
- **QSFP-100G-CLR4**：100G LR4-Lite 2km <<<PAGE 54>>>
- **QSFP-100G-ER4**：100G 4WDM-40 40km，过载 -3.5dBm，4.5W <<<PAGE 54>>>
- **QSFP-100G-A20M**：100G AOC 20m（需关自协商+FEC RS，无 DDM）<<<PAGE 55>>>
- **QSFP-100G-CWDM4**：100G CWDM4 2km <<<PAGE 55>>>
- **QSFP-100G-C（40cm/1/3/5m）**：100G DAC <<<PAGE 55>>>
- **QSFP-4X25G-C**：100G→4×25G DAC 拆分线 <<<PAGE 56>>>
- **QSFP-100G-SR1.2**：100G 双波长 SWDM（850/908nm）OM4 100m，配 400G-SR4.2 拆分（8.10R4 新品）<<<PAGE 56>>>
- **QSFP-100G-PSM4**：100G 并行单模 MPO 2km（8.10R4 新品）<<<PAGE 56>>>

## 200G QSFP56（Ch1）
- **QSFP-200G-SR4**：200G SR4 MPO OM4 100m，4.5W <<<PAGE 58>>>
- **QSFP-200G-FR4**：200G FR4 LC 2km，6W <<<PAGE 58>>>
- **QSFP-200G-A20M**：200G AOC 20m <<<PAGE 59>>>
- **QSFP-200G-C（50cm/1/3m）**：200G DAC <<<PAGE 59>>>
- **QSFP-2XQ100-C**：200G QSFP56→2×100G QSFP56 无源拆分线（1/3m）<<<PAGE 59>>>
- **QSFP-2XQ200-C**：400G QSFP-DD→2×200G QSFP56 无源拆分线（1/3m）<<<PAGE 59>>>

## 400G QSFP-DD（Ch1，均 8.10R4、仅 6920）
- **QSFPD-400G-C（50cm/1/3m）**：400G DAC <<<PAGE 61>>>
- **QSFPD-400G-DR4**：400G MPO-12 500m，10W <<<PAGE 61>>>
- **QSFPD-400G-FR4**：400G LC 2km（1271/1291/1311/1331nm），10W <<<PAGE 61>>>-<<<PAGE 62>>>
- **QSFPD-400G-LR4**：400G LC 10km <<<PAGE 62>>>
- **QSFPD-400G-A10M**：400G AOC 10m <<<PAGE 62>>>
- **QSFP-400G-SR4.2**：400G 多模双波长（850/908nm）OM4 100m，可拆 4×QSFP-100G-SR1.2，12W <<<PAGE 63>>>
- **QSFPD-2Q100-C**：400G QSFP-DD→2×100G QSFP28 无源拆分线（1/3m）<<<PAGE 63>>>

## PON 与工业模块（Ch1）
- **3FE46541AA（G-010S-A）**：GPON SFP ONT，1×GE UNI <<<PAGE 64>>>
- **3FE49327AA（XS-010S-Q）**：XGS-PON ONT SFP，1×10GE <<<PAGE 64>>>
- **iSFP 系列（-40~85°C）**：工业级全家族——iSFP-GIG-SX/LX/LH40/LH70/T/BX-D/U、iSFP-10G-SR/LR/ER/ZR/C、iSFP-100-MM/SM15/SM40/BXLC-D/U、iSFP-GIG-EZX、OS6865-CBL-40/100/300（工业 40G DAC）；iSFP-10G-C 与商用 SFP-10G-C 同件互换 <<<PAGE 65>>>-<<<PAGE 73>>>

## 兼容矩阵语义（Ch2）
- **最低 AOS 版本（Minimum Release）**：兼容矩阵单元格语义=该平台支持该模块的最低软件版本；"or"双值为硬件代次分界 <<<PAGE 75>>>等
- **N/S（Not Supported）**：该平台不支持该模块 <<<PAGE 75>>>等
- **VFL 连接（专用/例外）**：QSFP-40G-AOC20M/CBL 系列限 VFL 用；BX 系列等标注不支持 VFL <<<PAGE 88>>>等
- **平台兼容矩阵 14 张**：6360/6465(含 ENH-240)/6465T/6560(E)/6570M/6575/6860/6860N(含 OS68-XNI·VNI·QNI·CNI 扩展)/6865/6870(含 CNI-U2·LNI-U6)/6900-V72·C32·C32E/6900/6920/9900(含 CMM·CMM2·GNI·XNI·CNI 板卡) <<<PAGE 75>>>-<<<PAGE 107>>>

---
合计：78 条。

## principles

## MSA 与识别机制
- **P1** SFP MSA 标准接口：20 针插座 + 笼式外壳，模块内置串行接口提供能力/接口/厂商等识别信息——这是交换机识别模块与读取 DDM 的物理基础："Each SFP module contains a serial interface to provide identification information that describes the SFP capabilities." <<<PAGE 13>>>
- **P2** 认证模块红线：仅兼容矩阵中的 ALE 认证 PN 可用，他用模块导致不可预期行为、性能无保障且失保 <<<PAGE 1>>>
- **P3** 光/铜模块可同机混插，全部支持热插拔（hot-swappable），覆盖短距与长距场景 <<<PAGE 11>>>
## 安装与安全纪律
- **P4** 拔插间隔纪律：拔出模块后同端口至少等 10 秒再插入，给软件留出拔出检测时间："wait for a minimum of 10 seconds before re-inserting any transceiver into the same port." <<<PAGE 14>>>
- **P5** 三种释放机构对应操作：铰链式开到 90° 拉出（插入时须闭合）、bail wire 拉下压杆拔出（插入时闭合）、弹出器按钮用随机工具顶出后再夹出；任何时候不得强行插拔 <<<PAGE 15>>>/<<<PAGE 16>>>
- **P6** OS6865 机框特性：笼体有轻微压力，模块难拔时左右轻晃同时稳拉 <<<PAGE 14>>>
- **P7** 三大安全注意：ESD（腕带贴皮肤接机壳/接地柱）、防尘（不用的模块套回橡胶防尘帽）、激光（Class 1 激光，规范使用外可能有害辐射；25G/40G/50G/200G/400G 章节另有 CLASS 1M 开盖勿直视警示）<<<PAGE 14>>>/<<<PAGE 40>>>等
- **P8** QSFP 拔除用橡胶/金属释放手柄直拉 <<<PAGE 16>>>
- **P10** 40G MPO 拆 4×10G：MTP-LC 母头 splitter，8 芯对应 4 个 LC，LC 可手工重排收发 <<<PAGE 17>>>
- **P11** DAC 三级长度体系：1G 无 DAC；10G DAC 60cm-7m；25G/50G 0.5-5m；40G 40cm-7m；100G 40cm-5m；200G/400G 0.5-3m——机柜内布线用 DAC、跨柜用 AOC/光纤 <<<PAGE 34>>>-<<<PAGE 63>>>
- **P12** AOC 有源光缆跨柜短距：10G 无（用光模块）；25G A20M 20m；40G AOC20M 20m；100G A20M 20m；200G A20M 20m；400G A10M 10m <<<PAGE 42>>>-<<<PAGE 62>>>
## DDM 与协商机制
- **P15** 双速模块手工定速原则：dual-speed 收发器建议两端手工配速防止速率失配（100BASE-FX/1000BASE-LX 双态）："it's recommended to manually configure the speed on both ends to prevent speed mismatch." <<<PAGE 25>>>
- **P16** SFP28 口与 1G 模块不协商：6860N/6900 的 SFP28 口不支持与 1G 模块自协商，必须在对端交换机禁用自协商："SFP28 ports do not support auto-negotiation with 1G transceivers. Always disable auto-negotiation on the peer switch." <<<PAGE 92>>>/<<<PAGE 102>>>
- **P17** 10G-T 新旧件版本双轨：老 PN（903866-90 HW Rev -43/-54）配任意 AOS；新 Rev A53 需 ≥8.9R3、Rev V1.0 需 ≥8.10R2；SFP-GIG-T/SFP-DUAL-MM-N 新序列号（APxx…）需 ≥8.9R3——同型号模块看硬件修订/序列号定最低版本 <<<PAGE 24>>>/<<<PAGE 34>>>/<<<PAGE 25>>>
- **P18** 2019 年 5 月采购分界：BX-D/U 等模块 2019-05 之后采购的最低版本提到 8.6R1 <<<PAGE 82>>>/<<<PAGE 99>>>
- **P20** 拆分模式牺牲自动 VFL：6870 的 QSFP-100G-SR4 在 splitter 模式不支持 Auto-VFL <<<PAGE 96>>>
- **P21** VFL 连接专用/禁用模块清单：QSFP-40G-AOC20M 与 OS6860-CBL 系列为"VFL 连接专用"（AOC20M 仅 20G VFL、CBL 为 20G VFL 线）；SFP-10G-BX 系列与 QSFP-40G-SR-BD 明确"不支持 VFL 连接"——VFL 口选件要看此标注 <<<PAGE 88>>>/<<<PAGE 49>>>/<<<PAGE 37>>>/<<<PAGE 44>>>
- **P22** QSFP-40G-C7M 跨厂商验证：7m DAC 仅在 OmniSwitch 之间验证过，接他厂设备建议先验证再上量 <<<PAGE 48>>>
- **P23** 功耗梯度（每口散热预算）：1G/10G 光模块 ≤1-1.5W；10G-T 铜口 2.5W@30m；25G 1.2-1.5W；40G 1.5-3.5W；50G 2-3.3W；100G 3.5-4.5W；200G 4.5-6W；400G 高达 10-12W——高密 400G 要先核电源与风冷 <<<PAGE 32>>>-<<<PAGE 63>>>
- **P24** 温度两档：商用 0~70°C（个别 -5/-20/85 端点）；工业 iSFP 系列 -40~85°C（配 6575/6465 工业平台）；部分长距模块（LH40/LH70/EZX）上限收窄到 -10/-5~70°C <<<PAGE 18>>>-<<<PAGE 73>>>
- **P25** 单双纤配对原则：BX（Bi-Directional）系列必须 D/U 成对使用（一端 D 发 1490/收 1310，另一端 U 反之）——设计单纤链路时两端 PN 必须配对下单："Designed for use with SFP-GIG-BX-U." <<<PAGE 21>>>-<<<PAGE 24>>>等
- **P26** 距离档位体系（SMF）：LR/CLR=10/2km，LH40/ER/ER4=40km，LH70=70km，ZR=80km，EZX=120km；MMF 按 OM2/OM3/OM4 递减表选型（如 25G-SR：OM2 20m/OM3 70m/OM4 100m）<<<PAGE 18>>>-<<<PAGE 57>>>
- **P27** 100G A20M 特例：需禁用自协商并把 FEC 配成 RS <<<PAGE 55>>>
- **P28** 6865 平台用 iSFP 工业模块体系（6575 同），而 6360/6560/6860/6870 等商用平台用对应商用 PN——同代际两套 PN 并行 <<<PAGE 77>>>/<<<PAGE 93>>>等
- **P29** 10G-GIG-SR/LR 双速（10G/1G 自适应）按光纤分级：OM1 33m@10G、OM2 82m、OM3 300m；1G 时 OM1 275m/OM2·OM3 550m——旧布线升级 10G 的过渡件 <<<PAGE 36>>>
- **P30** 兼容矩阵双列最小版本语义（如"8.7R2 or 8.9R3"）：前者为老硬件最低版、后者为新硬件修订最低版，二者满足其一即可 <<<PAGE 75>>>/<<<PAGE 98>>>等

---
合计：30 条（P1-P30）。
