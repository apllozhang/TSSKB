# OmniSwitch 6465 Hardware Users Guide — 全书概览

- 书名：OmniSwitch 6465 Hardware Users Guide（Part No. 060510-10, Rev. V）
- 出版：ALE，2025-12
- 页数：99 页（fulltext.md 页码标记 `<<<PAGE 1>>>`-`<<<PAGE 99>>>`）
- 性质：工业级（加固型）交换机硬件手册——6 个机型两条线：OS6465-P6/P12/P12(ENH-240)/P28 为无风扇 DIN 导轨工业线（-40~75°C，奇数口/P28 口 1-8 支持 60W/bt），OS6465T-12/T-P12 为运输/交通半宽线（T 后缀，宽温但风扇 45°C 自启、不含工业认证）；外置 ROJ 端子式电源（75/180/480W AC + 180W DC）+ 告警继电器 + Dying Gasp；PoE 预算随环境温度降额（70-75°C 完全停 PoE）
- 家族命名规律：`P*=PoE`（奇数口 60W bt）；`ENH-240`=240W 增强预算变体；`T`=运输版半宽机型（内置电源+风扇）；`P28`=1U 机架 24+4 机型

## 章节结构与蒸馏重点

| 章 | 内容 | fulltext 页 | 蒸馏重点 |
|---|---|---|---|
| 前言 | 文档路线图 | 1-11 | 四阶段文档体系 |
| Ch1 | 机型总表 + 可用性 | 12-13 | 6 机型端口构成；电源冗余/load sharing（仅 P28 负载分担）；热插拔/监控 |
| Ch2 | 快速入门 | 14-20 | 电涌五条军规；冗余 AC 建议分路供电；9600-8N1；首次登录流程 |
| Ch3 | 机箱/安装/电源/告警 | 21-69 | 逐机型面板与宽温规格；DIN 导轨装/卸；机架（全宽/半宽单机/双机并排 DUO 套件）；侧挂；DNV 船用三套件；6 款电源规格（BPNX 480W/BPN-H 180W/BPN 75W/BPR AC 180W/BPRD DC 180W/内置 65·185W）；ROJ 电源线接线（线色/扭矩 3.5 in-lb）；powersupply type 手工配置；热换电源流程；接地；告警继电器（输入/输出/事件映射/自动清除 8 类事件）；温度双阈值；Dying Gasp（SNMP trap/Syslog/Link OAM PDU 三通道 + 上联口优先） |
| Ch4 | PoE | 70-84 | 预算随温度降额表（60°C/60-70°C/70-75°C 三档）；lanpower 命令族（与 6360 同构但仅 802.3at+HPoE 60W）；Guard Band/Priority Disconnect |
| 附录 A | 法规 | 85-99 | 工业认证体系（ISA/IEC 60068/DNV/EN 50121 铁路/NEMA TS-2，T 机型除外）；NEBS GR-1089-CORE OSP 隔离要求；安全警告 |

## 蒸馏策略（本书特调）

- **principles 收工业特性**：宽温双阈值体系、PoE 温度降额、电源冗余 vs 负载分担、ROJ 接线规范、告警继电器机制、Dying Gasp 三通道、powersupply type 手工识别
- **cases 收工业安装**：DIN 装/卸、双机并排、DNV 三套件、ROJ 接线、告警配置、电源热换
- **counter-examples 收工业红线**：24V 检测电路缺陷、混用电源不支持、BPNX 无工业认证且标签错误、70-75°C 停 PoE、T 机型无工业认证、BPN+ENH-240 需 8.9R2、NEBS OSP 禁连等
- **frameworks**：6465 双线家族结构（工业线/运输线）、告警-监控-断电告警体系
- **glossary**：6 机型 + 6 电源 + 安装套件 + 告警/DG/命令术语
