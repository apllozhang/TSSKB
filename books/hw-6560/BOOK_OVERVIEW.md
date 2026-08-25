# OmniSwitch 6560 Hardware Users Guide — 全书概览

- 书名：OmniSwitch 6560 Hardware Users Guide（Part No. 060474-10, Rev. P）
- 出版：ALE，2025-12
- 页数：111 页（fulltext.md 页码标记 `<<<PAGE 1>>>`-`<<<PAGE 111>>>`）
- 性质：多千兆接入交换机硬件手册——12 个 1U 机型（24/48 口千兆 + 2.5G/5G 多千兆 bt 口 + 4×SFP+ + 2×20G QSFP+ VFL；纯 10G 的 X10），可插拔 PoE 电源（300/600/920W，双电源负载分担），非 PoE 机型内置电源+模块化备份电源槽（BPS）；含 DNV 船用安装与 EMC 滤波器、DC 电源接线、Dying Gasp、PoE bt 全套
- 家族命名规律：`P*=PoE`；`Z8/Z24/Z16`=多千兆（2.5G/bt）口数；`E`=增强版（含 5G 口）；`X4`=4×SFP+ 上行机型；`X10`=8×SFP+ + 2×QSFP+ 纯上联机型

## 章节结构与蒸馏重点

| 章 | 内容 | fulltext 页 | 蒸馏重点 |
|---|---|---|---|
| 前言 | 文档路线图 | 1-11 | 四阶段文档体系 |
| Ch1 | 机型总表 + 可用性 | 12-14 | 12 机型端口构成；电源冗余/热插拔/监控三大特性 |
| Ch2 | 快速入门 | 15-22 | 电涌五条军规；气流间隙前 6"/后 6"/侧 2"；9600-8N1；首次登录六步 |
| Ch3 | 机箱/安装/电源/DG | 23-82 | 逐机型面板与规格（Tmra 统一 0-45°C）；VC ID LED；2.5G 口双 LED（Speed+PoE）；10G 需许可的 SFP(+) 口；机架法兰卡扣/桌面/DNV 安装+OS-DNV-FILTER（10k-150kHz 传导发射滤波）；6 款电源（BP-P 300W/BP-PH 600W/BP-PX 920W/BP 150W AC/BP-D 150W DC/内置 65W）；PN 版本与 8.8R1 门槛；DC 线束接线（12AWG、绿黄/黑/红、-48VDC、15A 过流、CBN）；电源装/拆（锁扣）；温度双阈值（Warning 用户可配！）；Dying Gasp 三通道 |
| Ch4 | PoE | 83-96 | bt 全规格（Class 0-8、bt 口 3000-95000mW）；PoE 预算表（按机型×电源×数量）；lanpower 命令族；Guard Band/Priority Disconnect |
| 附录 A | 法规 | 97-111 | 安全/EMC/环境标准；多语言安全警告 |

## 蒸馏策略（本书特调）

- **principles 收多千兆与电源体系**：Z 命名解码、E 版 5G 口、10G 许可口、电源负载分担与 PN 版本门槛、PoE 预算矩阵、2.5G 双 LED、Warning 阈值可配（与 6360/6465 不同）
- **cases 收安装与电源流程**：机架/桌面/DNV+滤波器、电源装拆（锁扣）、DC 线束接线、PoE 配置族
- **counter-examples 收限制**：10G 需许可、PN 版本不兼容（BP-P 不支持 E 机型/新 PN 需 8.8R1）、混插 wattage 电源不支持（但 BP+BP-D 可混）、Danger 不可配等
- **frameworks**：6560 家族选型矩阵（口构成 × PoE 预算）、电源-PoE 预算联动框架
- **glossary**：12 机型 + 6 电源 + 端口/LED/命令/标准术语
