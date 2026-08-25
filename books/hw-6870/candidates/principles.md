# principles — OmniSwitch 6870 Hardware Users Guide（硬件机制/架构/规格要点候选）

格式：编号 P# ｜ 要点 ｜ 页码（fulltext.md 真实 `<<<PAGE N>>>` 标记）

## 家族与端口架构

- **P1** 九机型三分类：非 PoE 固定（-24/-48/V12/CNI-U2/LNI-U6）；`P*M` 模块化（95W bt 多千兆 + QSFP56 200G + 1 上行模块槽）；`P*Z` 固定（60W bt 多千兆到 2.5G + QSFP28 100G + 6 SFP28）<<<PAGE 12>>>
- **P2** 上行速率阶梯：SFP28 支持 1G/10G/25G（25G 推荐用于 VFL）；QSFP28 支持 40G/100G/4X10G/4X25G；QSFP56 支持 40G/100G/200G/4X10G/4X25G <<<PAGE 23>>>/<<<PAGE 25>>>/<<<PAGE 35>>>
- **P3** M 系列独占 Uplink Module Slot（上行模块槽），P24M/P48M/V12 三机型具备，上行形态可后置扩展 <<<PAGE 12>>>/<<<PAGE 25>>>/<<<PAGE 31>>>/<<<PAGE 35>>>
- **P4** V12 全光机型：12× SFP28（25G 推荐 VFL）+ 2× QSFP56 200G + 上行模块槽，无铜口 <<<PAGE 12>>>/<<<PAGE 35>>>
- **P5** 上行扩展双节点：CNI-U2（2× QSFP28 100G）与 LNI-U6（6× SFP56 50G）作为纯上行星型扩展机箱 <<<PAGE 12>>>/<<<PAGE 37>>>/<<<PAGE 38>>>
- **P6** 全家族统一环境包络：Tmra 0-45°C、存储 -40~85°C、湿度 5%-95% 无凝结、1U（4.4cm 高）<<<PAGE 24>>>-<<<PAGE 36>>>
- **P7** 机箱深度两档：非 PoE/V12 为 35cm（13.78"）；P 系列深 44.2cm（17.40"）——机架深度规划须区分 <<<PAGE 24>>>/<<<PAGE 26>>>/<<<PAGE 28>>>等
- **P8** 待机/满载功耗阶梯：-24=71/100.9W；P24M=219.6/313.2W；P24Z=90.2/173.6W；-48=73/105.2W；P48M=251.8/343.9W；P48Z=92.4/215W；V12=73/157.8W <<<PAGE 24>>>-<<<PAGE 36>>>
- **P9** chassis 与 ambient 温度语义区分："Chassis temperature refers to the sensor reading of the internal switch temperature (threshold or danger). Ambient temperature refers to the approximate room temperature."（机箱温度恒高于室温）<<<PAGE 24>>>等

## 可用性特性

- **P10** 三大可用性支柱：Power Supply Redundancy（双电源负载分担）、Hot-Swapping（不断电增删部件）、Hardware Monitoring（自动：内置传感器超阈值立即发 trap；LED；用户主动 show 命令）<<<PAGE 13>>>

## 电源机制

- **P11** 六型电源矩阵：PS-250W-AC(12V/20.8A)、PS-250W-DC(-42~-60V/8A)、PS-550W-AC(V12 专用)、PS-600W/1200W/2000W-AC-POE(54.5V 输出，P 系列用)；250W 仅 -24/-48/V12；2000W 仅 P24M/P48M <<<PAGE 47>>>/<<<PAGE 48>>>-<<<PAGE 53>>>
- **P12** 负载分担与混插："If a second power supply is installed the two power supplies will load share." / "Mixing different wattage power supplies in a chassis is supported." <<<PAGE 47>>>/<<<PAGE 51>>>-<<<PAGE 53>>>
- **P13** 无总开关设计："The chassis does not provide an on/off switch. Connecting an installed power supply to a power source will boot the switch."（拔掉全部电源线即关机）<<<PAGE 47>>>/<<<PAGE 56>>>
- **P14** PoE 电源高压输入才有全功率：1200W 与 2000W 电源 "High power PoE wattages for this power supply are available at voltage inputs between 190-240VAC."（100-120V 输入时降额）<<<PAGE 52>>>/<<<PAGE 53>>>
- **P15** 电源双 LED 语义（PoE 型为 DC+AC 双灯）：绿闪+绿=仅待机输出；绿+绿=正常；红+绿=故障/关断；绿闪+红=AC 不在位 <<<PAGE 51>>>-<<<PAGE 53>>>
- **P16** 250W AC 单 LED 五态：绿=正常；琥珀=AC 线拔出或掉电（另一电源仍在）/严重事件关断；绿闪=Smart on 待机；琥珀闪=带告警运行；灭=全电源无 AC <<<PAGE 48>>>/<<<PAGE 49>>>
- **P17** DC 三线色彩语义：绿黄=ground、黑=return、红=-48VDC；回流导体为 Isolated DC Return（DC-I）；设备设计安装于 CBN（共同联结网络）<<<PAGE 54>>>
- **P18** 冗余 AC 分电路原则："It is recommended that each AC outlet resides on a separate circuit." <<<PAGE 14>>>

## 温度与监控机制

- **P19** 温度双阈值机制：Warning（用户可配）超限→发 trap 但业务继续，应查气流/室温/阈值设置；Danger 超限→自动关机直到人工处理并手动启动，且 Danger 出厂固化："The danger threshold is factory-set and cannot be configured by the user." <<<PAGE 58>>>/<<<PAGE 59>>>
- **P20** 硬件监控命令：`show module`（槽位基本信息）、`show module long`（详情）、`show temperature`（Current/Range/Danger/Thresh/Status 五列）<<<PAGE 58>>>
- **P21** Dying Gasp 机制与三通道：全电源丢失时维持电力发 SNMP trap（前 3 站，含槽位/电源类型/时间）+ Syslog "Dying Gasp Power Failure Event Occurred"（前 3 服务器）+ 4 个 802.3ah OAM PDU（Dying Gasp bit 置位，上行口优先）<<<PAGE 59>>>/<<<PAGE 60>>>

## LED 机制

- **P22** 系统 LED 五组：OK（稳绿=诊断与启动 OK/闪绿=进行中/稳琥珀=失败）；VC（稳绿=Master/稳琥珀=Slave/灭=未知）；PS（稳绿=正常/稳琥珀=单双电源故障/灭=无电源）；GRN（稳绿=省电模式/灭=正常模式）；VC ID（多灯数值相加=VC ID）<<<PAGE 38>>>
- **P23** RJ45 口四色速率 LED：绿=10/100/1000、蓝=2.5G、品红=5G、琥珀=10G（稳/闪=链路/活动）；LED2 琥珀=PoE 使能 <<<PAGE 39>>>
- **P24** SFP28/QSFP28/QSFP56 端口 LED 两色：绿=有效上行、琥珀=有效 VFL <<<PAGE 39>>>

## PoE 机制

- **P25** 911/UPS 供电纪律："It's recommended that PoE-enabled switches with attached IP telephones should have operational power supply redundancy at all times for 911 emergency requirements." <<<PAGE 61>>>
- **P26** PoE 标准栈：802.3/802.3af/802.3at/802.3bt；每口范围 at 口 3000-30000mW、bt 口 3000-95000mW；Class 0-8 梯度表（Class 5=45W/6=60W/7=75W/8=90-99W，4 对线 Type 3/4）<<<PAGE 62>>>/<<<PAGE 65>>>
- **P27** PoE 预算四变量模型：机型 × 电源瓦数（600/1200/2000W）× 单/双电源 × 电压输入档（双值条目=低压/高压输入），如 P24M 双 1200W=1516W/1880W、双 2000W=1516W/2280W；P48M 双 2000W 最高 3309W；Z 系列不支持 2000W 电源 <<<PAGE 63>>>
- **P28** PoE 激活两级模型：软件默认 administratively enabled，但必须逐 slot `lanpower slot service start` 物理激活："you must issue the lanpower slot service command on a slot-by-slot basis before any connected PDs will receive inline power." <<<PAGE 65>>>
- **P29** 4pair 与 8023bt 使能链：`lanpower 4pair` 开 60/75/95W（802.3at 4 对 + PoH）；`lanpower 8023bt` 开 bt 双 Type 四 Class（5-8）<<<PAGE 65>>>
- **P30** Class 检测默认关：不开启也按预算供电；严格按类限功率需 `lanpower slot class-detection` 显式开启，且开启复位全机 PoE 口："Enabling class detection will reset all PoE ports on the chassis." <<<PAGE 65>>>
- **P31** 端口/槽最大功率语义：只设上限不做预留："Changing the maximum power available to a slot or port does not reserve or immediately allocate that power." <<<PAGE 67>>>
- **P32** 三级端口优先级：low（默认，先断）/high（次保）/critical（尽量保），`lanpower port priority` 逐口设置 <<<PAGE 67>>>
- **P33** Priority Disconnect 四场景裁决：禁用→一律拒新 PD；启用+同级→按物理端口号（1 最高→48 最低）；启用+新 PD 最高优先级→新 PD 必得电，先断最低优先级口、同级断物理端口号最大口；启用+新 PD 最低→拒新 PD <<<PAGE 69>>>/<<<PAGE 70>>>
- **P34** Guard Band 拒载机制：剩余预算 < 端口最大功率或 PD 类最大值即拒载，即使实际只需 4W（例：余 50W、口上限 75W→拒；调上限 10W→放行）；不作用已在电 PD，预算缩减场景由 priority disconnect 裁决 <<<PAGE 67>>>/<<<PAGE 68>>>
- **P35** 电容检测默认禁用："The capacitive detection method should only be enabled to support legacy IP phones. This feature is not compatible with IEEE specifications." <<<PAGE 67>>>

## 安装与安全机制

- **P36** 电涌防护军规五条：全设备等电位接地（≤0.01Ω）；室外/近交流线路用 STP Cat5e+；室外铜口串接浪涌保护器；防室外设备传浪涌给上游；Cat5e/6/6a 蓄静电须先对地放电防 CDE；违者可失保 <<<PAGE 15>>>
- **P37** 盲板气流机制："If your switch is not fully populated and blank cover panels are not installed over empty slot locations, airflow is adversely affected."（气流改道、风扇加负、内部件暴露）<<<PAGE 40>>>
- **P38** 接地规范：后部两螺纹孔（paint-free 保证金属接触）接 Panduit LCD8-10A-L lug、10-32 3/8" 螺丝、8AWG 铜导线、扭矩 30-60 in-lb，作为电源线接地的补充 <<<PAGE 54>>>/<<<PAGE 57>>>
- **P39** 气流间隙三向要求：前 6"、后 6"、左右各 2"，顶底免间隙："No clearance is necessary at the top or bottom of the chassis." <<<PAGE 16>>>/<<<PAGE 17>>>
- **P40** 机架安装五大考量（IEC 纪律）：Tmra（封闭机架内温度高于室温）、Reduced Air Flow、Mechanical Loading（防不均衡载荷）、Circuit Overloading、Reliable Earthing（经电源排接入尤须注意）<<<PAGE 39>>>
