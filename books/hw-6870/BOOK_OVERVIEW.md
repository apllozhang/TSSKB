# OmniSwitch 6870 Hardware Users Guide — 全书概览

- 书名：OmniSwitch 6870 Hardware Users Guide（Part No. 060931-00, Rev. D）
- 出版：ALE，2025-12
- 页数：fulltext.md 页码标记 `<<<PAGE 1>>>`-`<<<PAGE 85>>>`
- 性质：千兆/多千兆接入交换机硬件手册——9 个 1U 机型（24/48 口非 PoE、P24M/P48M 模块化 95W bt PoE、P24Z/P48Z 60W bt PoE、V12 全光、CNI-U2/LNI-U6 上行扩展机箱）；上行覆盖 SFP28(25G)/QSFP28(100G)/QSFP56(200G)；M 系列带 Uplink Module Slot 上行模块槽；6 型电源（250W AC/DC、550W、600W/1200W/2000W PoE 型，后置可热插拔、负载分担、可混插不同瓦数）；PoE 802.3af/at/bt（Class 0-8，最高 95W/口）
- 家族命名规律：`P`=PoE 电机型；`M`=Modular（带上行模块槽 + 95W bt + QSFP56）；`Z`=固定配置多千兆 60W bt；`V`=全光纤口；CNI/LNI=上行扩展节点

## 章节结构与蒸馏重点

| 章 | 内容 | fulltext 页 | 蒸馏重点 |
|---|---|---|---|
| Ch1 | 机型总表 + 可用性特性 | 12-13 | 9 机型端口构成对照；三大可用性特性（电源冗余/热插拔/硬件监控=自动 trap+LED+show 命令） |
| Ch2 | 快速入门 | 14-21 | 站点环境/电气要求；电涌防护五条军规+CDE；开箱清单；气流间隙（前/后 6"、侧 2"、顶底免）；控制台 115200-8N1 rollover 线（注意与 6360/6865 的 9600 不同）；多电源须"数秒内相继插电"；首次登录六步（含 system location 与 write memory） |
| Ch3 | 机箱与电源 | 22-60 | 逐机型前/后面板与规格（Tmra 0-45°C；chassis vs ambient 温度语义）；LED 全表（OK/VC/PS/GRN 省电模式、RJ45 用 4 色 LED 区分 10M-10G 速率）；机架安装（弹簧夹法兰 CLICK、后支架）；独立桌面安装（禁止倒放/侧放）；6 型电源规格与 LED；负载分担与混插；DC 三线（绿黄=地/黑=return/红=-48V）；接地 lug（LCD8-10A-L、8AWG、30-60 in-lb）；show module/show temperature；温度 Warning/Danger 双阈值；Dying Gasp |
| Ch4 | PoE 管理 | 61-71 | 911/UPS 纪律；802.3af/at/bt Class 0-8 功率表（15.4-99W）；PoE 预算表（600W/1200W/2000W 电源 × 机型 × 单/双 × 高低压输入）；lanpower 命令族；4pair 与 8023bt 使能；Guard Band；Priority Disconnect；show lanpower |
| 附录 A | 法规与安全 | 72-85 | CE/FCC Class A/RoHS/Prop 65；Class 1M 激光；多语言安全警告（盲板/雷暴/激光/电压/断电/接地/DC/受限场所/ESD/锂电/三电源线） |

## 蒸馏策略（本书特调）

- **principles 收 6870 特有机制**：M/Z 命名与 QSFP56/200G 上行、混插电源负载分担、高低压输入双档预算、4 色 RJ45 LED 速率指示、bt Class 5-8、Dying Gasp、温度双阈值
- **cases 收安装与配置流程**：弹簧夹法兰安装、机架双人六步、桌面四脚、电源装/拆（锁片）、DC 三线、首次登录（含 write memory）、PoE 全命令流
- **counter-examples 收警告限制**：115200 波特率、多电源快速相继上电、1200W/2000W 高压输入才得全功率、Class 1M、倒放侧放禁令、lanpower port admin-state 限制等
- **frameworks**：6870 九机型选型矩阵、PoE 预算-电源-电压输入联动框架
- **glossary**：机型/电源/LED/命令/标准术语
