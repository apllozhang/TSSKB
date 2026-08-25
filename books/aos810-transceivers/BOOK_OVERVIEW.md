# OmniSwitch AOS Release 8 Transceivers Guide — 全书概览

- 书名：OmniSwitch AOS Release 8 Transceivers Guide（8.10R4）
- 出版：ALE，2025-12，Part No. 060973-00 Rev. A
- 页数：107 页（fulltext.md 页码标记 `<<<PAGE N>>>`；正文页码 1-1~1-63 与 2-64~2-97）
- 性质：光模块/线缆规格与兼容性手册——两章结构：Ch1 按速率/类型列出每款模块的连接器/标准/波长/光功率/灵敏度/距离/温度/功耗/DDM；Ch2 按 14 个平台（含扩展模块）给出"模块 × 最低 AOS 版本"兼容矩阵
- 红线（封面警示）：使用非 ALE 认证 PN 的模块被禁止且不保修："Use of any transceivers other than the ALE-certified part numbers listed in the Compatibility Matrices is prohibited and unsupported."

## 章节结构与蒸馏重点

| 节 | 内容 | fulltext 页 | 蒸馏重点 |
|---|---|---|---|
| Ch1 前言 | SFP MSA、安装拆卸 | 11-17 | MSA 20 针定义；ESD/防尘/激光安全；拔出后 ≥10 秒再插；三种释放机构（铰链/bail wire/弹出器） |
| Ch1 | 40/100G 光缆 | 17 | QSFP-QSFP MPO 用 Type-B 交叉；MPO-LC splitter 8 芯 4×10G |
| Ch1 | 1G/双速/100FX | 18-31 | SX/LX/LH40/LH70/EZX(120km)/CWDM/T 铜口/单双纤 BX 系列（10/20/40km 配对） |
| Ch1 | 10G SFP+ | 32-39 | SR/LR/ER/LRM/ZR(80km)/T(30m)/DAC/CWDM/双速 GIG-SR·LR/BX |
| Ch1 | 25G SFP28 | 40-43 | SR/ESR(OM4 300m)/LR/CLR(2km)/AOC/DAC/BX-D40·U40 |
| Ch1 | 40G QSFP+ | 44-50 | SR/SR-BD/LR/ER/LM4/CLR/PSM4/DAC/4X10G 拆分/AOC/20G VFL 线缆 |
| Ch1 | 50G SFP56 | 51-52 | SR/FR(2km)/LR/DAC（LNI-U6 专用） |
| Ch1 | 100G QSFP28 | 53-57 | SR4/LR4/CLR4/ER4/CWDM4/A20M/DAC/4X25G 拆分/SR1.2/PSM4 |
| Ch1 | 200G QSFP56 | 58-60 | SR4/FR4/A20M/DAC/2XQ100·2XQ200 拆分线 |
| Ch1 | 400G QSFP-DD | 61-63 | C(DAC)/DR4(500m)/FR4(2km)/LR4(10km)/A10M/SR4.2(100m OM4，可拆 4×100G SR1.2)/2Q100 |
| Ch1 | GPON/工业 | 64-73 | 3FE46541AA(GPON ONT)/3FE49327AA(XGS-PON)；iSFP 系列 -40~85°C |
| Ch2 | 兼容矩阵 | 74-107 | 6360/6465/6465T/6560(E)/6570M/6575/6860/6860N(含 68 系扩展模块)/6865/6870/6900-V72·C32·C32E/6900/6920/9900（含 99 系板卡） |

## 蒸馏策略（本书特调）

- **glossary 大头**：把规格表逐型号转成术语条目（型号→速率/波长/距离/连接器/DDM），按速率分组
- **principles 收通用机制**：MSA/安装纪律/DDM 语义/双速模块手工定速/SFP28 自协商禁用/拆分模式/VFL 限制等跨型号规律
- **counter-examples 收兼容限制**：端口级限定、VFL 例外、per-platform N/S、许可依赖、2019 年 5 月后购件升版、每机箱数量上限
- **frameworks**：兼容矩阵查询法（型号→平台→最低版本三查）、距离档位选型
- **cases 为 0**：全书无配置流程（仅物理安装说明，已并入 principles），不创建 cases.md
