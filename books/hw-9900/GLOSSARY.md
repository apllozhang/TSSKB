# GLOSSARY · OmniSwitch 9900 Series Hardware Users Guide

> 页码为原书 `<<<PAGE N>>>` 标记。按机箱/CMM-CFM/NI/电源风扇/安装登录/PoE/热插拔/法规分组，精选 52 条。

## 机箱（Ch1）
- **OS9907**：11RU 模块化机箱，7 槽（2 CMM+5 NI），32.83kg，23 英寸深 <<<PAGE 5>>>/<<<PAGE 6>>>
- **OS9912**：17RU 模块化机箱，12 槽（2 CMM+10 NI），64.36kg <<<PAGE 11>>>
- **slot2 双角色**：9907 上 slot2 可装 CMM（1+1 冗余）或 NI（扩端口但失冗余）<<<PAGE 7>>>/<<<PAGE 16>>>/<<<PAGE 17>>>
- **中板（Mid-plane）**：CFM 与机箱连接结构（NI 走 backplane）<<<PAGE 20>>>
- **VC-of-2**：两台 OS9907 虚拟化为一台虚拟机箱，仅三种对称组合 <<<PAGE 22>>>
- **N+1 冗余**：4 电源负载分担/3 风扇托盘冗余 <<<PAGE 8>>>/<<<PAGE 28>>>
- **铝头拇指螺丝**：替代紫色塑料头的新形态，机械性能相同 <<<PAGE 6>>>/<<<PAGE 12>>>
- **Wrist Strap Grounding Connector**：机箱前/后部 ESD 腕带接地点 <<<PAGE 8>>>/<<<PAGE 9>>>

## CMM 与 CFM（Ch1）
- **CMM（Chassis Management Module）**：机箱管理模块，管控 NI/CFM/配电；2 槽 1+1 冗余 <<<PAGE 16>>>
- **OS99-CMM**：初代管理模块，2×40G QSFP+ 上行，64W，仅 9907 支持 <<<PAGE 16>>>
- **OS99-CMM2**：新一代管理模块，4×100G QSFP28 上行/VFL，74W，需 AOS ≥8.10R2，不可与 CMM 混插 <<<PAGE 17>>>
- **CFM（Chassis Fabric Module）**：交换矩阵模块，藏于风扇托盘之后经中板连接 <<<PAGE 10>>>/<<<PAGE 20>>>
- **OS9907-CFM / CFM2**：9907 矩阵（2.56T / 12.8T 每块，119W；CFM2 需 AOS ≥8.9R1）<<<PAGE 20>>>
- **OS9912-CFM**：9912 矩阵（25.6T 每块，222W）<<<PAGE 21>>>
- **CFM3/4 预留**：预留未激活槽位，不可当可用槽规划 <<<PAGE 5>>>/<<<PAGE 10>>>/<<<PAGE 15>>>
- **组合兼容矩阵**：仅 CMM+CMM/CFM+CFM、CMM+CMM/CFM2+CFM2、CMM2+CMM2/CFM2+CFM2 三种支持 <<<PAGE 22>>>
- **PRI LED**：CMM 主备灯（稳绿=主/闪绿=备/稳黄=停运/闪黄=升级中）<<<PAGE 18>>>
- **FAB LED**：CFM 状态灯（稳绿=正常/稳黄=降级/闪黄=CFM 电源或 PCIe 失败）<<<PAGE 18>>>
- **五灯同闪（PCIe link failure）**：PRI/VC/FAB/PS/TEMP 同闪黄=全部 CFM PCIe 硬链路失效 <<<PAGE 18>>>
- **Micro-USB console**：CMM 第二 console 口，需装驱动 <<<PAGE 16>>>/<<<PAGE 17>>>

## NI 模块（Ch1）
- **OS99-XNI-48**：48 口 1/10GBaseT 模块，402W <<<PAGE 23>>>
- **OS99-XNI-U48**：48 口 1/10G SFP+ 模块，305W（slot2 只活 8 口）<<<PAGE 23>>>/<<<PAGE 7>>>
- **OS99-GNI-48**：48 口 10/100/1000BaseT + 2×10G，56W <<<PAGE 23>>>
- **OS99-GNI-P48**：48 口千兆 PoE 模块（前 8 口 HPoE 75W），54W <<<PAGE 24>>>
- **OS99-GNI-U48**：48 口 1G SFP 模块，70W <<<PAGE 24>>>
- **OS99-XNI-P48Z16**：32 口 at PoE + 16 口多千兆 PoE，402W；不支持 9912 <<<PAGE 24>>>
- **OS99-XNI-P24Z8**：16+8 口 PoE 组合模块，187W；不支持 9912 <<<PAGE 25>>>
- **OS99-XNI-U24**：24 口 1/10G SFP+ 模块，153W <<<PAGE 25>>>
- **OS99-CNI-U8**：8 口 10/25/40/100G QSFP28 模块，117W <<<PAGE 25>>>
- **OS99-CNI-U20**：20 口 100G QSFP28（13-20 口支持 splitter），314W <<<PAGE 26>>>
- **OS99-XNI-UP24Q2**：12×SFP+ +12×多千兆 HPoE +2×QSFP+；不支持 9912 <<<PAGE 26>>>
- **OS99-XNI-U12Q**：12×SFP+ +1×QSFP+；不支持 9912 <<<PAGE 26>>>
- **HPoE 口**：PoE 模块前 8 口、面板标 "HPoE"、75W <<<PAGE 24>>>
- **Speed LED（NI）**：稳绿=HW OK/闪绿=SW 心跳/稳黄=SW 故障/稳红=HW 故障 <<<PAGE 27>>>
- **9912 不支持 NI 清单**：XNI-P48Z16 / XNI-P24Z8 / XNI-UP24Q2 / XNI-U12Q <<<PAGE 24>>>-<<<PAGE 26>>>

## 电源与风扇（Ch1/Ch2）
- **OS99-PS-A**：AC 电源（100-240V；输出 1200W/21.4A 或 3000W/53.5A 两档），System+PoE <<<PAGE 29>>>
- **OS99-PS-D**：DC 电源（-40~-72VDC/75A；输出 2500W/44.6A@56V）<<<PAGE 30>>>
- **电源三不混**：AC/DC 不可混、Hi(240V)/Lo(110V) 输入不可混 <<<PAGE 29>>>/<<<PAGE 63>>>
- **分路保护额定值**：每电源建议 30A（AC）/110A（DC）断路器 <<<PAGE 29>>>
- **FCI 10080598-2ED0006LF**：DC 电源要求的 4P PWRBLADE 专用连接器 <<<PAGE 31>>>
- **10AWG**：DC 供电双铜导体线规（分支过流 75A）<<<PAGE 30>>>
- **AHJ（Authority Having Jurisdiction）**：DC 线 >3m 时须咨询的管辖机构 <<<PAGE 31>>>
- **风扇托盘（Fan Tray）**：3 件常驻、N+1 冗余、仅前→后气流；9907 每托 3 扇、9912 每托 5 扇 <<<PAGE 28>>>

## 安装与登录（Ch2）
- **三人机架作业**：两人抬一人拧 <<<PAGE 36>>>/<<<PAGE 69>>>
- **锁杆（Lock Levers）**：CFM/NI 闭锁机构（90 度全闭锁定）<<<PAGE 38>>>/<<<PAGE 42>>>
- **满载搬运禁令**："Do not attempt to move or install a fully loaded chassis" <<<PAGE 32>>>
- **9600-8N1**：console 默认串口参数（RJ45 或 Micro-USB）<<<PAGE 44>>>
- **EMP 线缆规则 / 默认地址**：直通线接交换机/交叉线接计算机；默认 192.168.1.1/24 <<<PAGE 45>>>/<<<PAGE 46>>>
- **admin/switch**：出厂默认账号/密码 <<<PAGE 46>>>
- **aaa authentication**：解锁会话类型命令族（解锁前 EMP 不能远程访问）<<<PAGE 47>>>
- **show chassis / Power Left**：机箱信息与可用功率预算 <<<PAGE 49>>>
- **DB9-RJ45 Connector**：随箱 console 转接头 <<<PAGE 34>>>

## PoE（Ch3）
- **lanpower slot service**：逐 slot 首次激活/停止 PoE 的唯一途径 <<<PAGE 50>>>/<<<PAGE 52>>>
- **lanpower power / slot maxpower**：单口/整槽功率上限（slot 默认 1800W；不预留）<<<PAGE 50>>>/<<<PAGE 53>>>
- **lanpower priority**：口优先级 low/high/critical（默认 low）<<<PAGE 50>>>/<<<PAGE 54>>>
- **lanpower capacitor-detection**：电容检测（仅老式 IP 话机、默认关、开启复位全部 PoE 口）<<<PAGE 50>>>/<<<PAGE 52>>>/<<<PAGE 54>>>
- **Priority Disconnect**：预算不足时按优先级+物理端口号裁决——**48（最高）→1（最低），与接入系列相反** <<<PAGE 55>>>
- **PoE 默认 operational disabled**：装好不等于供电，须 lanpower start 激活 <<<PAGE 50>>>
- **HPoE（75W）**：前 8 口 75000mW；at 口 30000mW <<<PAGE 50>>>
- **show powersupply / show lanpower slot**：电源与 PoE 逐口/预算状态 <<<PAGE 50>>>/<<<PAGE 51>>>

## 热插拔（Ch4）
- **热插拔节律**：拆件间隔 30 秒、插件间隔 5 分钟+LED 无错 <<<PAGE 63>>>
- **同类替换（like modules）**：NI 热换只能同型号 <<<PAGE 63>>>
- **CFM 120 秒窗口**：CFM 热换须 120 秒内完成、一次一块 <<<PAGE 63>>>
- **单件不可热拆**：单 CMM/CFM/电源拆即断业务 <<<PAGE 63>>>

## 安全与法规（附录 A）
- **Panduit LCD8-10AL / CT-940CH**：接地 lug 及压接工具，8AWG、30-60 in-lb <<<PAGE 70>>>/<<<PAGE 71>>>
- **ESD 腕带生效条件**：电源已装机并接接地插座才有效 <<<PAGE 72>>>
- **受限场所（Restricted Access Location）**：仅限持钥匙/安保措施的维护人员进入 <<<PAGE 71>>>
- **CLASS 1 LASER PRODUCT**：CMM/NI 面板激光标识；空口勿直视 <<<PAGE 16>>>等/<<<PAGE 70>>>
- **Tmra**：最大额定环境温度 <<<PAGE 32>>>

---
合计：52 条。
