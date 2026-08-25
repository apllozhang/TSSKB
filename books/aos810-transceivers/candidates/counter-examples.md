# counter-examples — 兼容限制/不支持项（OmniSwitch AOS 8.10R4 Transceivers Guide）

格式：编号 X# ｜ 限制要点 ｜ 页码

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
- **X14** 6570M 不支持 SFP-10G-LRM 与 10G-BX-D40/U40；SFP-25G 全系 8.10R4 才引入、25G-BX-D40/U40 不支持 <<<PAGE 84>>>
- **X15** 6465(ENH-240) 新平台砍掉 10G 光模块：iSFP-10G-SR/LR/ER/ZR 与两款 PON ONT 均 Not Supported <<<PAGE 77>>>
- **X16** 6870-P24M/P48M（万兆铜主机型）不支持任何 1G/100 SFP（N/A 列）——1G 接入必须靠 P24Z/48/V12 等机型 <<<PAGE 94>>>
- **X17** SFP-50G 系列仅 6870-LNI-U6 支持（8.10R2），其余平台全 N/S <<<PAGE 96>>>
- **X18** QSFP-200G 仅 6870 的 P24M/P48M/V12（上联口）与 6920 支持，24/48/P24Z/P48Z 数据口不支持 <<<PAGE 96>>>/<<<PAGE 104>>>
- **X19** 400G QSFP-DD 全系仅 6920（OS6900-D32）支持 <<<PAGE 104>>>
- **X20** QSFP-100G-PSM4 与 SR1.2 都是 8.10R4 新引入，此前版本一律不认 <<<PAGE 104>>>等
- **X21** GPON ONT（3FE46541AA）在 6860/6865/6870/6920/9900 全不支持；XGS ONT（3FE49327AA）仅 6360/6465T/6560/6570M(U28)/6860N-P48M+XNI-U4 支持 <<<PAGE 89>>>/<<<PAGE 93>>>等
- **X22** 9900 板卡级差异巨大：1G SFP 仅 XNI-U48/GNI-U48/XNI-U24 支持；100G QSFP 仅 CMM2/CNI-U8/CNI-U20 支持（且 CMM/CMM2 的 QSFP 要 8.9R3）<<<PAGE 105>>>-<<<PAGE 107>>>
- **X23** QSFP-4X25G-C 在 OS99-CNI-U8 上 8.7R1 起插入直接报错（QSFP-4X25G-C 不支持该板）<<<PAGE 107>>>

## 版本与硬件修订陷阱

- **X24** "或"版本须看硬件代次：SFP-10G-ZR 在 6560 写 8.4.1.R02 or 8.6R1（2019-05 后采购需 8.6R1+）；6860 写 8.2.1 or 8.6R1；6900-V72 写 8.5R2 or 8.6R1——同型号模块不同批次最低版本不同 <<<PAGE 81>>>/<<<PAGE 88>>>/<<<PAGE 98>>>
- **X25** SFP-GIG-T/SFP-10G-T/SFP-DUAL-MM-N 双版本：新序列号/硬件修订分别需 8.9R3（AP 序列号、A53 修订）/8.10R2（V1.0 修订）<<<PAGE 20>>>/<<<PAGE 34>>>/<<<PAGE 25>>>
- **X26** QSFP-40G-C 9900↔6900 互连必须关 9900 侧自协商 <<<PAGE 48>>>
- **X27** QSFP-100G-A20M 必须关自协商+FEC RS <<<PAGE 55>>>
- **X28** 6870 的 QSFP-100G-SR4 拆分模式不支持 Auto-VFL <<<PAGE 96>>>

## VFL 与其他限制

- **X29** VFL 例外模块：SFP-10G-BX-D/U(-40) 明确不支持 VFL 连接；QSFP-40G-SR-BD 同样不支持 <<<PAGE 37>>>/<<<PAGE 38>>>/<<<PAGE 44>>>
- **X30** 6560 的 QSFP-40G-AOC20M 仅限 VFL 连接、不能用于 4X10G 拆分 <<<PAGE 82>>>
- **X31** DVM 无 DDM 的模块清单：全部 DAC（SFP-10G-C/QSFP-40G-C/100G-C/200G·400G 拆分线）、铜口 T 系列、SFP-GIG-##CWD、SFP-100-LC-MM/SM15、SFP-DUAL-SM10、QSFP-40G-SR-BD、QSFP-100G-A20M——这些口无法用 DDM 做光功率监控 <<<PAGE 20>>>-<<<PAGE 63>>>
- **X32** 停购物料仍在兼容表（No longer purchasable）：SFP-GIG-EZX/##CWD/EXTND、DUAL-MM/SM10、100-BX20 系列、SFP-10G-24DWD80、QSFP-40G-SR-BD/LM4、部分 iSFP 停购件——存量可继续用，新项目不可选 <<<PAGE 20>>>-<<<PAGE 73>>>
- **X33** 6860N-P48M/P24M 的 25G 模块在扩展模块 OS68-XNI-U4 上 N/S（25G 仅限主板 SFP28 上联口）；VNI-U4/QNI-U2/CNI-U1 模块的光模块支持范围各自独立 <<<PAGE 91>>>
- **X34** 6860N-U28 的 100 系列与 DUAL 系列支持、但 P24Z/P48Z 不支持——同家族机型光模块清单不通用 <<<PAGE 90>>>-<<<PAGE 92>>>
- **X35** 6465T 不支持 BX20/BX40 双纤双向 1G 模块与 XGS ONT（12 口以外）<<<PAGE 78>>>/<<<PAGE 79>>>

---
合计：35 条（X1-X35）。
