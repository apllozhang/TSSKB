# OmniSwitch 6360 Hardware Users Guide — 全书概览

- 书名：OmniSwitch 6360 Hardware Users Guide（Part No. 060711-00, Rev. J）
- 出版：ALE，2025-12
- 页数：83 页（fulltext.md 页码标记 `<<<PAGE 1>>>`-`<<<PAGE 83>>>`）
- 性质：入门级三层千兆接入交换机硬件手册——10 个固定配置 1U 机型（10/24/48 口，非 PoE / PoE / 多千兆 PoE），全部内置单电源；除 P24X/PH24/P48X/PH48 外多为无风扇；含机架/壁挂安装、面板 LED、PoE（802.3af/at/bt）预算与优先级断电机制、CLI 硬件监控、法规附录
- 家族命名规律：`-10/-24/-48` 非 PoE；`P` 前缀 = PoE（802.3at）；`PX` = 2 个多千兆 802.3bt 口 + 大电源；`H` = combo 口可升级 10G（软件解锁）

## 章节结构与蒸馏重点

| 章 | 内容 | fulltext 页 | 蒸馏重点 |
|---|---|---|---|
| 前言 | 文档路线图 | 1-12 | 硬件手册定位（不含软件配置）；四阶段文档路线图 |
| Ch1 | 机型总表 + 可用性特性 | 13-16 | 10 机型端口构成对照；热插拔/自动监控（传感器 trap）/LED 三大可用性特性 |
| Ch2 | 快速入门 | 17-24 | 站点环境/电气要求（电涌防护 5 条军规、CDE 电缆放电）；开箱清单；气流间隙（前 6"/后 6"/侧 2"）；控制台 9600-8N1；首次登录六步（admin/switch、解锁会话、改密、时间、可选项、write memory）；无 RTC 需 NTP |
| Ch3 | 机箱与电源 | 25-57 | 逐机型前/后面板与规格表（尺寸/重量/功耗/PoE 预算/温度）；chassis vs ambient 温度语义；OK/VC/PWR 与端口 LED 语义；五大安装考量（Tmra/气流/载重/过流/接地）；盲板气流作用；机架安装（双人、法兰卡扣）；桌面/半宽 L 支架/壁挂套件；接地 lug（LCD8-10A-L、8AWG、30-60 in-lb）；show module/show temperature；温度 Warning/Danger 双阈值（Danger 关机不可配） |
| Ch4 | PoE 管理 | 58-69 | 规格与默认值；PoE 预算表（120-760W）；lanpower 命令族（service/power/maxpower/priority/4pair/8023bt/class-detection/capacitor-detection/priority-disconnect）；Fast/Perpetual PoE 机制（FPGA/CPLD 依赖）；Guard Band 拒载机制；Priority Disconnect 三场景裁决规则（优先级+物理端口号 1 高 48 低） |
| 附录 A | 法规与安全 | 70-83 | CE/WEEE/RoHS/Prop 65；安全/EMC/环境标准清单；多语言安全警告（雷暴/激光/ESD/接地/锂电/受限场所等） |

## 蒸馏策略（本书特调）

- **principles 收机型规格规律**：家族命名解码、PoE 预算-电源 wattage 对应、LED 语义、温度双阈值、Guard Band/Priority Disconnect 机制、Fast/Perpetual PoE 原理、接地规范
- **cases 收安装与配置流程**：开箱→上电→首次登录→解锁会话→改密→保存；机架/桌面/壁挂三类安装；PoE 激活/关断/优先级/预算配置
- **counter-examples 收警告与限制**：P10A-US 无 Fast/Perpetual PoE、无 RTC、Danger 阈值不可配、capacitor detection 不符 IEEE、lanpower port admin-state 不能首次激活、Class A 不可住宅、禁用延长线/雷暴作业等
- **frameworks**：6360 家族选型矩阵（口数 × PoE × 上行）、PoE 供电预算-优先级-保护三环体系
- **glossary**：10 机型逐条 + 端口/LED/命令/标准术语
