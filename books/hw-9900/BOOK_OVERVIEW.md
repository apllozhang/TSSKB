# OmniSwitch 9900 Series Hardware Users Guide — 全书概览

- 书名：OmniSwitch 9900 Series Hardware Users Guide（Part No. 060409-10, Rev. S）
- 出版：ALE，2025-12
- 页数：fulltext.md 页码标记 `<<<PAGE 1>>>`-`<<<PAGE 74>>>`
- 性质：核心/园区骨干模块化机箱（modular chassis）硬件手册——两款机箱：OS9907（11RU，7 槽：2 CMM + 5 NI）与 OS9912（17RU，12 槽：2 CMM + 10 NI）；均配 4 CFM 交换矩阵槽（CFM3/4 预留未启用，藏于风扇托盘之后）、3 风扇托盘（N+1 冗余，仅前→后气流）、4 电源槽（N+1 负载分担，AC 3000W/DC 2500W）；CMM/CMM2 双管理模块（1+1 冗余，slot2 可换 NI 换端口）；11 种 NI 模块（1G/10G/25G/100G、PoE/HPoE）；支持 VC-of-2 双机箱虚拟化
- 关键组合规则：CMM2 需 AOS ≥8.10R2、CFM2 需 ≥8.9R1；CMM 与 CMM2 不可同箱混插；部分 NI 模块不支持 OS9912

## 章节结构与蒸馏重点

| 章 | 内容 | fulltext 页 | 蒸馏重点 |
|---|---|---|---|
| Ch1 | 机箱与电源 | 5-31 | 两机箱规格（重量 32.83/64.36kg）与槽位布局；CMM/CMM2 面板与 LED 全表（PRI/VC/FAB/PS/TEMP + PCIe 失效组合闪烁语义）；CFM/CFM2 带宽（2.56/12.8/25.6 Tbps）；OS9907 CMM/CFM 支持组合表与 VC-of-2 配置表；11 种 NI 模块规格与 NI LED；风扇托盘（N+1、仅前→后）；OS99-PS-A（AC 1200/3000W 两档）/OS99-PS-D（DC 2500W）；DC 接线（75A 过流、10AWG、4P PWRBLADE 连接器） |
| Ch2 | 快速入门与安装 | 32-49 | 安装五大考量；电涌防护五条军规；不可墙装；独立/机架安装（三人搬运、先下后上）；装 CFM（先拆风扇托盘、锁杆三步）、装风扇托盘（上 tab 先入）、装 NI 模块、装电源流程；console 9600-8N1（Micro-USB 需驱动）；EMP 线缆规则与默认 IP 192.168.1.1；首次登录七步；show chassis 查 Power Left 做机箱功率预算 |
| Ch3 | PoE | 50-56 | 4 种 PoE 模块（GNI-P48/XNI-P48Z16/XNI-P24Z8/XNI-UP24Q2）；HPoE 75W/802.3at 30W；slot 默认 1800W；lanpower 命令族；Priority Disconnect（注意端口优先 48 高 → 1 低，与接入交换机相反） |
| Ch4 | 拆除部件 | 57-62 | 拆电源/风扇托盘/CFM/NI 模块流程；热插拔通用纪律（拆间隔 30s、插间隔 5 分钟+无错 LED；单 CMM/CFM/电源不可热拆；CFM 热换 ≤120s；NI 只能同类替换） |
| 附录 A | 法规与安全 | 63-74 | FCC/CE/UL 60950/RoHS/Prop 65/WEEE；多语言安全警告（双人搬运/雷暴/激光/断电/接地 lug 30-60 in-lb/ESD 腕带/受限场所/锂电） |

## 蒸馏策略（本书特调）

- **principles 收机箱架构机制**：槽位分区（CMM/NI/CFM/风扇/电源）、N+1 冗余模型、CFM 带宽叠加、CMM/CFM 组合兼容矩阵、VC-of-2、机箱功率预算（show chassis Power Left）、端口优先方向反转
- **cases 收安装与拆除双流程**：装 CFM/风扇/NI/电源、拆同四件、首次登录七步、PoE 命令流
- **counter-examples 收机箱级硬约束**：AC/DC 电源不可混、Hi/Lo 输入不可混、CMM 与 CMM2 不可混、单件不可热拆、CFM 120s、风扇托盘 3 件常驻、墙装禁令、slot2 NI 只活 8 口等
- **frameworks**：9907 vs 9912 选型矩阵、CMM/CFM 兼容组合决策表、机箱功率预算三步法
- **glossary**：机箱/CMM/CFM/NI/电源/风扇/命令/标准术语
