# OmniSwitch 6865 Hardware Users Guide — 全书概览

- 书名：OmniSwitch 6865 Hardware Users Guide（Part No. 060435-10, Rev. Y）
- 出版：ALE，2025-12
- 页数：fulltext.md 页码标记 `<<<PAGE 1>>>`-`<<<PAGE 76>>>`
- 性质：加固型（hardened）千兆/10G 工业交换机硬件手册——3 个固定配置机型（P16X / U12X / U28X），全部无风扇，宽温 -40~74°C（需气流）/-40~65°C（免气流），支持机架/桌面/DIN 导轨/墙装/DNV（船级社）五种安装；双电源（1 主 1 备，AC OS6865-BP 180W 或 DC OS6865-BP-D 180W/140W，DB-15 外接托盘式）；PoE 802.3af/at（含 75W HPoE / 60W 802.3bt 口）；Dying Gasp 掉电告别机制
- 家族命名规律：`P`=PoE 电机型、`U`=上行口密集机型；数字=端口总数；`X`=含 SFP+ 10G 上行

## 章节结构与蒸馏重点

| 章 | 内容 | fulltext 页 | 蒸馏重点 |
|---|---|---|---|
| 前言 | 文档路线图 | 1-8 | 硬件手册定位；四阶段文档路线图（首用→基本功能→入网→CLI 随查） |
| Ch1 | 快速入门与安装 | 9-41 | 安装五大考量（Tmra 74°C 需封闭机柜）；电涌防护与 CDE 电缆放电；气流阈值 65°C（≥65°C 必须气流）；最小间隙表（顶部 1/2~1RU、侧 2"、前/后 6"）；电源托盘侧装/后装两种形态；机架/桌面/DIN 导轨（电源与机箱分别拆装步骤）/DNV 全/半架安装；控制台 9600-8N1；首次登录六步；LED 语义（OK/VC/PS1/PS2 与端口） |
| Ch2 | 机箱与电源 | 42-55 | 三机型规格表（2RU/1RU、无风扇、TMRA 分级、海拔 4000m）；前面板端口构成（P16X：2 SFP+ + 2 SFP + 4×75W HPoE/bt + 8×PoE+；U12X：2 SFP+ + 6 SFP + 4 HPoE；U28X：4 SFP+ + 20 SFP + 4 HPoE + 2 QSFP+ VFL）；OS6865-BP/BP-D 电源规格；DC 三线接线（剥线 6-7.5mm、极性军规、15A 过流、12AWG）；Dying Gasp 三通道（SNMP trap/Syslog/Link OAM PDU）与端口优先级限额 |
| Ch3 | PoE | 56-64 | 911/UPS 供电纪律；PoE 预算-温度-电源组合表（双电源 300W/150W 分档）；Class 0-4 检测；lanpower 命令族（service/power/maxpower/priority/fpoe/ppoe/capacitor-detection/priority-disconnect）；Fast/Perpetual PoE；优先级三级；Guard Band 拒载；Priority Disconnect 三场景 |
| 附录 A | 法规与安全 | 65-76 | CE/FCC Class A/RoHS；工业合规（ISA 12.12.01、IEC 61850-3、EN 50121-4 铁路、DNV 2.4、NEMA TS-2）；多语言安全警告（双人搬运/雷暴/激光/接地 lug 30-60 in-lb/ESD 腕带/受限场所/锂电） |

## 蒸馏策略（本书特调）

- **principles 收加固特性与机制**：无风扇宽温分级、TMRA-气流-电源三变量预算表、Dying Gasp 三通道、Guard Band/Priority Disconnect、极性军规
- **cases 收五类安装流程**：侧/后装电源托盘、机架（REAR-MNT/TRAY-1U 套件）、DIN 导轨、DNV 全/半架、DC 接线、首次登录、PoE 激活
- **counter-examples 收警告限制**：65°C 气流阈值、无电源开关、lanpower port admin-state 不能首次激活、capacitor detection 不符 IEEE、DC >3m 属本地规范、住宅禁用 Class A、垂直 DIN 仅限不可燃表面等
- **frameworks**：6865 三机型选型矩阵（PoE vs 上行密度）、加固交换机"环境-电源-PoE 预算"三环校验
- **glossary**：机型/部件/套件/命令/标准术语
