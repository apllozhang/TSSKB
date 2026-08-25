# GLOSSARY — OmniSwitch AOS Release 8 Transceivers Guide 核心术语

从 verified 术语库精选 78 条，按主题分组（模块型号为主）。型号/PN/协议保留英文，页码为原书页码。

## 通用概念与机构

- **SFP MSA（Multi Source Agreement）**：光模块多源协议——20 针接口+识别串口的通用标准（<<<PAGE 13>>>）
- **DDM（Digital Diagnostic Monitoring）**：数字诊断监控（温度/电压/电流/光功率）；DAC 与铜口模块普遍不支持（<<<PAGE 18>>>等）
- **Bail Wire Delatch / 铰链面 / 弹出器按钮**：SFP 三种释放机构（<<<PAGE 15, 16>>>）
- **Type-B MPO 交叉线**：QSFP↔QSFP 直连 MPO trunk 必用的交叉极性（8 芯使用）（<<<PAGE 17>>>）
- **MPO-LC Splitter**：40G MPO 拆 4×10G LC 的分支线（<<<PAGE 17>>>）
- **DAC（Direct Attach Copper）**：无源直连铜缆（同轴拆分线）；有源版本称 AOC（<<<PAGE 34>>>等）
- **AOC（Active Optical Cable）**：有源光缆（模块+线缆一体）（<<<PAGE 49>>>）

## 1G SFP

- **SFP-GIG-SX**：千兆多模 850nm，300m(62.5µ)/550m(50µ)，LC，DDM 支持（<<<PAGE 18>>>）
- **SFP-GIG-LX**：千兆单模 1310nm 10km，LC，DDM 支持（<<<PAGE 18>>>）
- **SFP-GIG-LH40**：千兆 40km 1310nm，0~+5dBm，灵敏度 -22dBm（<<<PAGE 19>>>）
- **SFP-GIG-LH70**：千兆 70km 1550nm（<<<PAGE 19>>>）
- **SFP-GIG-EZX**：千兆 120km 超长距 1550nm，灵敏度 -35dBm（已停购）（<<<PAGE 19-20>>>）
- **SFP-GIG-##CWD**：千兆 CWDM 粗波分，8 波长 1470-1610nm，62km，无 DDM（已停购）（<<<PAGE 20>>>）
- **SFP-GIG-T**：千兆铜口 RJ45 10/100/1000BASE-T 100m；新序列号 APxx 需 ≥8.9R3（<<<PAGE 20>>>）
- **SFP-1G-T**：千兆铜口（仅 1000BASE-T，802.3ab）（<<<PAGE 21>>>）
- **SFP-GIG-EXTND**：千兆多模延长 2km（已停购）（<<<PAGE 21>>>）
- **SFP-GIG-BX-D / BX-U**：千兆单纤双向 10km 配对（D 发 1490/收 1310，U 反之）（<<<PAGE 21, 22>>>）
- **SFP-GIG-BX-D20 / U20 / D40 / U40**：单纤双向 20km/40km 配对变体（<<<PAGE 22-24>>>）

## 双速与 100FX

- **SFP-DUAL-MM / MM-N**：100FX+1000LX 双速多模（550m@1G/2km@100M）；MM-N 新件需 ≥8.9R3（<<<PAGE 25>>>）
- **SFP-DUAL-SM10**：双速单模 10km（无 DDM，已停购）（<<<PAGE 26>>>）
- **SFP-DUAL-BX-D / U**：双速单纤双向 10km（1550/1310nm 配对）（<<<PAGE 26>>>）
- **SFP-100-BX20LT / BX20NU**：100M 单纤双向 20km SC 口（ITU-T G.983，已停购）（<<<PAGE 28>>>）
- **SFP-100-BXLC-D / U**：100M 单纤双向 20km LC 口配对（<<<PAGE 29>>>）
- **SFP-100-LC-MM**：100FX 多模 2km，无 DDM（<<<PAGE 30>>>）
- **SFP-100-LC-SM15 / SM40**：100FX 单模 15km/40km（<<<PAGE 30, 31>>>）

## 10G SFP+

- **SFP-10G-SR**：10G 多模 850nm 300m（OM3），1W（<<<PAGE 32>>>）
- **SFP-10G-LR**：10G 单模 10km 1310nm（<<<PAGE 32>>>）
- **SFP-10G-ER**：10G 40km 1550nm，1.5W，损伤阈值 4dBm（<<<PAGE 33>>>）
- **SFP-10G-LRM**：10G 多模延长 220m（802.3aq）（<<<PAGE 33>>>）
- **SFP-10G-ZR**：10G 80km 1550nm，过载 -7dBm（<<<PAGE 34>>>）
- **SFP-10G-T**：10G 铜口 RJ45 30m CAT6a/7，2.5W，无 DDM；新修订需 8.9R3/8.10R2（<<<PAGE 34>>>）
- **SFP-10G-C（60cm/1/3/7m）**：10G DAC；iSFP-10G-C 与商用 PN 同件可互换（<<<PAGE 34, 25>>>）
- **SFP-10G-24DWD80**：10G 80km DWDM 1558.17nm（已停购）（<<<PAGE 35>>>）
- **SFP-10G-GIG-SR / GIG-LR**：10G/1G 双速（OM3 300m@10G；LR 10km）（<<<PAGE 36>>>）
- **SFP-10G-BX-D / U（10/40km）**：10G 单纤双向 1330/1270nm 配对；不支持 VFL（<<<PAGE 37, 38>>>）
- **SFP-10G-CWDM**：10G CWDM 40km 1551nm，-40~85°C（<<<PAGE 39>>>）

## 25G SFP28

- **SFP-25G-SR**：25G 多模 850nm（OM2 20m/OM3 70m/OM4 100m），802.3by（<<<PAGE 40>>>）
- **SFP-25G-ESR**：25G 扩展多模 OM4 300m（<<<PAGE 41>>>）
- **SFP-25G-LR**：25G 单模 10km（802.3cc）（<<<PAGE 41>>>）
- **SFP-25G-CLR**：25G 单模 2km（<<<PAGE 42>>>）
- **SFP-25G-A20M**：25G AOC 20m（<<<PAGE 42>>>）
- **SFP-25G-C（1/3/5m）**：25G DAC（<<<PAGE 42>>>）
- **SFP-25G-BX-D40 / U40**：25G 单纤双向 40km（1310/1270nm），-40~85°C（<<<PAGE 43>>>）

## 40G QSFP+

- **QSFP-40G-SR**：40G SR4 MPO-12 多模（OM3 100m/OM4 150m），支持 4X10G 拆分（<<<PAGE 44>>>）
- **QSFP-40G-SR-BD**：40G 双向双通道 LC 多模（BiDi），3.5W，无 DDM、不支持 VFL（已停购）（<<<PAGE 44, 45>>>）
- **QSFP-40G-LR**：40G LR4 LC 单模 10km（4 波长 1264.5-1337.5nm）（<<<PAGE 45>>>）
- **QSFP-40G-ER**：40G ER4 LC 单模 40km（802.3bm）（<<<PAGE 45>>>）
- **QSFP-40G-LM4**：40G 多模 LC（OM3 140m，已停购）（<<<PAGE 46>>>）
- **QSFP-40G-CLR**：40G 单模 2km（LR4 Lite 类）（<<<PAGE 46>>>）
- **QSFP-40G-PSM4**：40G 并行单模 MPO-12 10km，支持 4X10G 拆分（<<<PAGE 47>>>）
- **QSFP-40G-C（40cm/1/3/7m）**：40G DAC；7m 跨厂商需验证、9900↔6900 要关自协商（<<<PAGE 47, 48>>>）
- **QSFP-4X10G-SR**：40G 拆 4×10G 光模块（MPO，OM3 300m）（<<<PAGE 48>>>）
- **QSFP-4X10G-C（1/3/5m）**：40G→4×10G DAC 拆分线（<<<PAGE 48>>>）
- **QSFP-40G-AOC20M**：40G AOC 20m（多数平台限 VFL 连接）（<<<PAGE 49>>>）
- **OS6860-CBL-40/100/300**：20G VFL 专用 QSFP DAC（40cm/1m/3m）（<<<PAGE 49, 50>>>）

## 50G SFP56

- **SFP-50G-SR**：50G 多模 850nm OM4 100m，3.3W（<<<PAGE 51>>>）
- **SFP-50G-FR**：50G 单模 2km（1311nm）（<<<PAGE 51>>>）
- **SFP-50G-LR**：50G 单模 10km（<<<PAGE 52>>>）
- **SFP-50G-C（50cm/1/3m）**：50G DAC（-20~75°C）（<<<PAGE 52>>>）

## 100G QSFP28

- **QSFP-100G-SR4**：100G SR4 MPO 多模（OM3 70m/OM4 100m），支持 4X25G 拆分（<<<PAGE 53>>>）
- **QSFP-100G-LR4**：100G LR4 LC 单模 10km（4 波长 1294.53-1310.19nm）（<<<PAGE 53>>>）
- **QSFP-100G-CLR4**：100G LR4-Lite 2km（<<<PAGE 54>>>）
- **QSFP-100G-ER4**：100G 4WDM-40 40km，过载 -3.5dBm，4.5W（<<<PAGE 54>>>）
- **QSFP-100G-A20M**：100G AOC 20m（需关自协商+FEC RS，无 DDM）（<<<PAGE 55>>>）
- **QSFP-100G-CWDM4**：100G CWDM4 2km（<<<PAGE 55>>>）
- **QSFP-100G-C（40cm/1/3/5m）**：100G DAC（<<<PAGE 55>>>）
- **QSFP-4X25G-C**：100G→4×25G DAC 拆分线（<<<PAGE 56>>>）
- **QSFP-100G-SR1.2**：100G 双波长 SWDM（850/908nm）OM4 100m，配 400G-SR4.2 拆分（8.10R4 新品）（<<<PAGE 56>>>）
- **QSFP-100G-PSM4**：100G 并行单模 MPO 2km（8.10R4 新品）（<<<PAGE 56>>>）

## 200G QSFP56 与 400G QSFP-DD

- **QSFP-200G-SR4**：200G SR4 MPO OM4 100m，4.5W（<<<PAGE 58>>>）
- **QSFP-200G-FR4**：200G FR4 LC 2km，6W（<<<PAGE 58>>>）
- **QSFP-200G-A20M**：200G AOC 20m（<<<PAGE 59>>>）
- **QSFP-200G-C（50cm/1/3m）**：200G DAC（<<<PAGE 59>>>）
- **QSFP-2XQ100-C**：200G QSFP56→2×100G QSFP56 无源拆分线（1/3m）（<<<PAGE 59>>>）
- **QSFP-2XQ200-C**：400G QSFP-DD→2×200G QSFP56 无源拆分线（1/3m）（<<<PAGE 59>>>）
- **QSFPD-400G-C（50cm/1/3m）**：400G DAC（<<<PAGE 61>>>）
- **QSFPD-400G-DR4**：400G MPO-12 500m，10W（<<<PAGE 61>>>）
- **QSFPD-400G-FR4**：400G LC 2km（1271/1291/1311/1331nm），10W（<<<PAGE 61-62>>>）
- **QSFPD-400G-LR4**：400G LC 10km（<<<PAGE 62>>>）
- **QSFPD-400G-A10M**：400G AOC 10m（<<<PAGE 62>>>）
- **QSFP-400G-SR4.2**：400G 多模双波长（850/908nm）OM4 100m，可拆 4×QSFP-100G-SR1.2，12W（<<<PAGE 63>>>）
- **QSFPD-2Q100-C**：400G QSFP-DD→2×100G QSFP28 无源拆分线（1/3m）（<<<PAGE 63>>>）
- （400G 全系仅 6920 支持、均 8.10R4 起）

## PON 与工业模块

- **3FE46541AA（G-010S-A）**：GPON SFP ONT，1×GE UNI（<<<PAGE 64>>>）
- **3FE49327AA（XS-010S-Q）**：XGS-PON ONT SFP，1×10GE（<<<PAGE 64>>>）
- **iSFP 系列（-40~85°C）**：工业级全家族——iSFP-GIG-SX/LX/LH40/LH70/T/BX-D/U、iSFP-10G-SR/LR/ER/ZR/C、iSFP-100 系列、OS6865-CBL 工业 40G DAC；iSFP-10G-C 与商用 SFP-10G-C 同件互换（<<<PAGE 65-73>>>）

## 兼容矩阵语义（Ch2）

- **最低 AOS 版本（Minimum Release）**：矩阵单元格语义=该平台支持该模块的最低软件版本；"or"双值为硬件代次分界（<<<PAGE 75>>>等）
- **N/S（Not Supported）**：该平台不支持该模块（<<<PAGE 75>>>等）
- **VFL 连接（专用/例外）**：QSFP-40G-AOC20M/CBL 系列限 VFL 用；BX 系列等标注不支持 VFL（<<<PAGE 88>>>等）
- **平台兼容矩阵 14 张**：6360/6465(含 ENH-240)/6465T/6560(E)/6570M/6575/6860/6860N(含 OS68 扩展模块)/6865/6870(含 CNI·LNI)/6900-V72·C32·C32E/6900/6920/9900(含板卡)（<<<PAGE 75-107>>>）
