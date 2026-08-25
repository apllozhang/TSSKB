# OmniSwitch 6860/6860E/6860N Hardware Users Guide — 全书概览

- 书名：OmniSwitch 6860/6860E/6860N Hardware Users Guide（Part No. 060390-10, Rev. W）
- 出版：ALE，2025-12
- 页数：115 页（fulltext.md 页码标记 `<<<PAGE 1>>>`-`<<<PAGE 115>>>`）
- 性质：VC 堆叠接入交换机硬件手册——15 个 1U 机型三代同堂：基础 OS6860（24/48 铜 + 4×SFP+ + 2×20G VC 口）、增强 E（内置协处理器 + 后面板 EMP，含 60W/75W HPoE"非 bt 合规"口与 U28 全光型）、下一代 N（QSFP28 VFL + SFP28 25G 上联，多千兆 bt 95W 全面化，M 型带上插上联模块槽）；7 款电源（150W AC/DC 到 2000W）；Fast PoE / Perpetual PoE；风扇托盘；DG PDU 端口数受 SNMP/Syslog 服务器数挤占
- 家族命名规律：`P*=PoE`；`E`=协处理器增强（含 EMP）；`N`=下一代（25G/多千兆 bt）；`U28`=全光上联型；`Z*=多千兆口`；`M`=带上联模块槽的模块化机型
- 注意：后部 OS-BPS 备份电源槽已标"No longer supported"（面板图保留但不再支持）

## 章节结构与蒸馏重点

| 章 | 内容 | fulltext 页 | 蒸馏重点 |
|---|---|---|---|
| 前言 | 文档路线图 | 1-13 | 四阶段文档体系 |
| Ch1 | 机型总表 + 可用性 | 14-17 | 15 机型三代端口构成；热插拔三件套（电源/光模块/插拔模块） |
| Ch2 | 快速入门 | 18-26 | 电涌五条军规；前后 6"/侧 2" 且上下免间隙；console 为 Micro USB（N 型 115200）；EMP 默认 IP 192.168.1.1/24；首次登录七步（多 EMP 设 IP） |
| Ch3 | 机箱/安装/电源/风扇 | 27-88 | 15 机型逐面板与规格（Tmra 统一 0-45°C/13000ft）；N 型 SFP28 四口组禁 1G/10G 与 25G 混跑；6860N 端口 LED 五色（蓝=2.5G/蓝黄=5G/品红=10G）；弹簧夹法兰+N-P48Z/P48M 后支架；7 款电源与混插规则（BP+BP-D 唯一例外、不支持电源插入即禁全部交换与 PoE 口、N 电源需 AOS 8.7R1+）；DG PDU 上限=10-SNMP/Syslog 服务器数；DC 接线族；上联模块装拆；FANTRAY NONPOE；show temperature 按 VC 机箱逐行 |
| Ch4 | PoE | 89-103 | 逐机型口功率域表；N 型预算矩阵（双 2000W 达 3390W）；Fast PoE/Perpetual PoE 机制与限制；power-rule 定时；priority disconnect 上限（920W→780W/600W→450W）；物理口号 24/48 最高→1 最低 |
| 附录 A | 法规 | 104-115 | UL 60950/62368 双标准；ETS 300 019 环境分级；多语言安全警告 |

## 蒸馏策略（本书特调）

- **principles 收三代机型演化与电源体系**：E=协处理器+N=25G 演化轴、HPoE"not 802.3bt compliant"注记、SFP28 四口组限速、五色端口 LED、七款电源矩阵与 N 专属双 LED、DG PDU 端口挤占公式、Fast/Perpetual PoE
- **cases 收安装与配置流程**：法兰+后支架机架、电源装拆、上联模块装拆、桌面、盲板、EMP 设 IP、PoE 全族配置
- **counter-examples 收限制**：SFP28 混速禁令、不支持电源即禁口、混 wattage 禁、OS-BPS 停支持、Fast PoE 四限制、Perpetual PoE MCU 升级断电等
- **frameworks**：6860 三代选型矩阵、PoE 预算-priority disconnect 上限联动、VC 高可用框架
- **glossary**：15 机型 + 7 电源 + 4 上联模块 + LED/命令/标准术语
