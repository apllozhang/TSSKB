# OmniSwitch 6575 Hardware Users Guide — 全书概览

- 书名：OmniSwitch 6575 Hardware Users Guide（Part No. 060975-00, Rev. A）
- 出版：ALE，2025-12
- 页数：86 页（fulltext.md 页码标记 `<<<PAGE 1>>>`-`<<<PAGE 86>>>`）
- 性质：工业/极端环境无风扇交换机硬件手册——3 个机型按安装形态分化：OS6575-P12（DIN 导轨/壁装，8×802.3bt 60W + 4×SFP+ 上联/VFL）、OS6575-U28（1U 机架，4 combo PoE+ 90W + 20×SFP + 4×SFP+ VFL，双后装电源）、OS6575-MP16（壁装工业机，M12/M23 防水连接器，at/bt 混合 + 4 口 Port Bypass 旁路）；Tmra 全家族 -40~75°C；含 Alarm Relay 干接点告警、ROJ 剥线电源线接线、M12/M23 pinout 与配件线缆、PoE 温度阶梯预算表
- 家族命名规律：`P12`=PoE 12 口紧凑机（DIN）；`U28`=上联密集 28 口 1U 机；`MP16`=Multi-Purpose/M12 16 口工业机
- 注意：附录 A（fulltext 72-86 页）页眉误印为"OmniSwitch 6465"，内容为 6575 附录（含工业合规章节）

## 章节结构与蒸馏重点

| 章 | 内容 | fulltext 页 | 蒸馏重点 |
|---|---|---|---|
| 前言 | 文档路线图 | 1-10 | 四阶段文档体系 |
| Ch1 | 机型总表 + 可用性 | 11-12 | 3 机型全无风扇；MP16 Port Bypass 断电旁路特性 |
| Ch2 | 快速入门 | 13-19 | 电涌五条军规；console rollover 线 9600-8N1；首次登录六步 |
| Ch3 | 机箱/安装/电源/告警 | 20-55 | U28 前装/后装（REAR-MNT+TRAY-1U）；DIN/壁装；4 款电源（BPNS 150W/BPNSX 480W 外置、BPR/BPRD 180W 模块后装）；ROJ 线色与 3.5 in-lb 力矩；powersupply type 手动配置；Alarm Relay in/out 干接点与 VC 同步；温度阈值（-45~93/98）；M12/M23 pinout 与 10 款配件线缆 |
| Ch4 | PoE | 56-71 | at/bt 规格；温度阶梯预算表（预算随 Tmra 降档）；48V 以下禁 PoE；Guard Band；Priority Disconnect 四情形 |
| 附录 A | 法规 | 72-86 | 工业合规（ISA/DNV/铁路 EN 50121-4/NEMA TS-2/MIL-STD-810F）；NEBS GR-1089 OSP 隔离；星形垫圈/CBN |

## 蒸馏策略（本书特调）

- **principles 收工业特性与预算阶梯**：无风扇 -40~75°C、Port Bypass、Alarm Relay、输入电压分档 PoE 档位（U28 50-57V=at/44-57V=af/24-60V=无 PoE）、PoE 温度阶梯预算、M12 X-code PoE pinout
- **cases 收安装与接线流程**：后装电源（导柱+拇指螺丝）、ROJ 交流/直流接线（线色+力矩）、Alarm Relay 配置族、PoE 配置族
- **counter-examples 收限制**：48VDC 以下禁 PoE、电源禁混规格、class detection 复位全口、NEMA 插头不得提前带电插拔等
- **frameworks**：6575 家族选型矩阵（按安装形态）、温度-预算联动框架、告警链路框架
- **glossary**：3 机型 + 4 电源 + M12/M23 术语 + 告警/PoE 命令 + 工业标准
