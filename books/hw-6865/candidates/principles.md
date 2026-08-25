# principles — OmniSwitch 6865 Hardware Users Guide（硬件机制/架构/规格要点候选）

格式：编号 P# ｜ 要点 ｜ 页码（fulltext.md 真实 `<<<PAGE N>>>` 标记）

## 定位与家族架构

- **P1** 加固型定位：6865 系列为面向严苛电气与宽温环境的 GigE/10G 交换机："The Alcatel-Lucent Enterprise OmniSwitch 6865 series are Gigabit Ethernet (GigE) and 10 Gb Ethernet (GigE) switches designed for demanding electrical and severe temperature environments." <<<PAGE 42>>>
- **P2** 三机型分工：P16X=16 口 PoE 型（4×75W HPoE/bt + 8×PoE+ + 2 SFP+ + 2 SFP）；U12X=12 口上行型（2 SFP+ + 6 SFP + 4 HPoE）；U28X=28 口全宽上行型（4 SFP+ + 20 SFP + 4 HPoE + 2 QSFP+ VFL）<<<PAGE 44>>>/<<<PAGE 46>>>/<<<PAGE 48>>>
- **P3** 全家族无风扇：三机型 Fans 均为 None，散热完全依赖机箱散热片与外部气流 <<<PAGE 42>>>/<<<PAGE 45>>>/<<<PAGE 47>>>
- **P4** 机箱形态两档：P16X/U12X 为半宽 2RU（8.5" 宽、10.24" 深）；U28X 为全宽 1RU（17.2" 宽、10.6" 深）<<<PAGE 42>>>/<<<PAGE 47>>>
- **P5** 电源拓扑为"外置托盘 + DB-15 电缆"：1 主 + 1 备共 2 电源，装在侧装/后装托盘上经 DB-15 连接线接到机箱，非内置槽位 <<<PAGE 42>>>/<<<PAGE 19>>>
- **P6** 前面板统一维护接口：Console(RJ45) + USB Type A（仅维护用，可下代码/存配置）位于最左 <<<PAGE 44>>>/<<<PAGE 46>>>/<<<PAGE 48>>>
- **P7** 全家族支持 1588v2（精密时间协议），面向工业/电力场景 <<<PAGE 43>>>/<<<PAGE 46>>>/<<<PAGE 48>>>
- **P8** 待机功耗阶梯：P16X=30W、U12X=29W、U28X=50W <<<PAGE 43>>>/<<<PAGE 46>>>/<<<PAGE 48>>>

## 温度与气流机制（加固型核心）

- **P9** TMRA 三档温度包络：有气流 -40~74°C；无气流 -40~65°C；装 DNV 电源盖后无论有无气流均降为 -40~55°C <<<PAGE 42>>>/<<<PAGE 45>>>/<<<PAGE 47>>>
- **P10** 65°C 气流分界线："Switches operating in an environment at or above 65°C require air flow. Switches operating in an environment below 65°C do not require airflow." <<<PAGE 11>>>
- **P11** 74°C 必须封闭机柜："When operating at 74°C ambient temperature the switch must be installed in a suitable closed rack or cabinet enclosure." <<<PAGE 9>>>
- **P12** 存储温度上限 85°C、湿度 5%-95% 无凝结、海拔 4000m，三机型一致 <<<PAGE 43>>>/<<<PAGE 45>>>/<<<PAGE 47>>>
- **P13** 顶部间隙温度分档：机架安装顶部 <65°C 留 0.875"(1/2 RU)、≥65°C 留 1.75"(1 RU)；桌面安装顶/底各 0.875"（靠桌脚保证）；侧 2"、前/后 6" <<<PAGE 11>>>/<<<PAGE 12>>>
- **P14** 桌面安装方向军规：大散热片面朝外、远离安装面："be sure that the top of the switch, with the larger heat sinks, is facing out and away from the mounting surface." <<<PAGE 11>>>

## 电源与 Dying Gasp 机制

- **P15** 双电源型号：OS6865-BP（AC 100-240V，输出 +56VDC/3.22A=180W）与 OS6865-BP-D（DC 输入 -20~-28V/12A 或 -36~-72V/6A，输出 -56V 140W/180W 两档）<<<PAGE 49>>>/<<<PAGE 50>>>
- **P16** 无总开关设计："The switch does not provide an on/off switch. Instead, the switch powers on when a power cord is plugged into the power supply's front panel and plugged into a power source." <<<PAGE 19>>>/<<<PAGE 20>>>
- **P17** Dying Gasp 机制：全电源丢失时交换机维持电力足够发出告别消息再关机："If the switch loses all power it will maintain power long enough to send a Dying Gasp message before completely shutting down. An SNMP trap, Syslog message and Link OAM PDUs will be generated." <<<PAGE 53>>>
- **P18** Dying Gasp 触发场景三则：仅主电失败（单电源）；主后备先后失败；后备主先后失败；规避法="Connect each power supply to a separate independent power source to avoid simultaneous power failures." <<<PAGE 54>>>
- **P19** Dying Gasp 三通道内容：SNMP trap（发前 3 个已配 SNMP 站，含槽位/电源类型/时间）；Syslog "Dying Gasp Power Failure Event Occurred"（发前 3 个 Syslog 服务器）；4 个 802.3ah Link OAM Information PDU（Dying Gasp 位置位）<<<PAGE 54>>>
- **P20** Dying Gasp PDU 端口限额公式："The maximum number of ports which can send out a dying gasp PDU simultaneously is limited to ten ports minus the number of syslog/snmp servers configured."（例：2 SNMP+1 Syslog → 最多 7 口）；发送顺序上行口优先 <<<PAGE 54>>>/<<<PAGE 55>>>
- **P21** DC 极性军规：无论 -24V 还是 -48V 输入，源设备正极接电源正极、负极接负极，不受电源标签极性符号影响："This rule always applies to both -24V, and -48V input voltages, regardless of the polarity signs shown on the power supply specification labels." <<<PAGE 53>>>
- **P22** DC 供电纪律五条：接可靠接地 -24V/-48V SELV 源；DC 回流导体接机框；分支过流保护 15A；双 12AWG 铜导线；现场布线须含易触及的断开装置 <<<PAGE 51>>>
- **P23** 冗余 AC 双电路原则："It is recommended that each power supply resides on a separate circuit."（单电路故障时另一电源存活）<<<PAGE 10>>>

## PoE 机制

- **P24** 911/UPS 供电纪律："It's recommended that PoE-enabled switches with attached IP telephones have operational power supply redundancy at all times for 911 emergency requirements." 交换机与电源均应接 UPS <<<PAGE 56>>>
- **P25** PoE 预算三变量模型：电源数量 × 电源类型（AC/DC·48V/24V）× 环境温度（60/65/74°C 三档）共同决定可用预算——如 P16X/U12X 双 BP 电源 60°C 得 300W、65°C/74°C 降至 150W；U28X 双电源 60°C 得 280W <<<PAGE 56>>>/<<<PAGE 57>>>
- **P26** HPoE 口默认上限 75000mW、802.3bt 口 60000mW、PoE 口 30000mW，可用 `lanpower power` 调整；默认优先级 low；capacitor detection 默认禁用；priority disconnect 默认启用 <<<PAGE 56>>>
- **P27** PoE 激活两级模型：软件默认 administratively enabled，但必须逐 slot `lanpower slot service start` 物理激活："you must issue the lanpower slot service command on a slot-by-slot basis before any connected devices will receive inline power." <<<PAGE 58>>>
- **P28** Class 检测按 802.3at 分级（Class 0-4：0.44W→30W 梯度）；默认关闭时仍按预算供电，严格按类限功率需显式开启且开启会复位全 slot PoE 口："Enabling class detection will reset all PoE ports." <<<PAGE 57>>>/<<<PAGE 58>>>
- **P29** Fast PoE 机制：PoE 子系统默认态固化进 FPGA 镜像、配置存控制器 EEPROM，上电数秒即可供电不等 AOS 启动完成；LLDP 协商的 PD 仍要等启动完成 <<<PAGE 59>>>
- **P30** Perpetual PoE 机制：软重启/重载期间 PD 供电不间断；PoE 控制器（MCU）固件自身升级时仍必断电："The power to the PD devices will be interrupted if the PoE controller (MCU) firmware itself is being upgraded." <<<PAGE 59>>>
- **P31** 端口/槽最大功率语义：只设上限不做预留："Changing the maximum power available to a slot or port does not reserve or immediately allocate that power."（未用功率仍回总预算池）<<<PAGE 60>>>
- **P32** 三级端口优先级：low（默认，先断）→ high（次保）→ critical（尽量保），`lanpower port priority` 逐口设置 <<<PAGE 60>>>/<<<PAGE 61>>>
- **P33** Priority Disconnect 四场景裁决：禁用→一律拒新 PD；启用+同级→按物理端口号（1 最高→28 最低）；启用+新 PD 优先级最高→新 PD 必得电、先断最低优先级口、同级断端口号最大的口；启用+新 PD 最低→拒新 PD <<<PAGE 62>>>/<<<PAGE 63>>>
- **P34** Guard Band 拒载机制：剩余预算 < 端口最大功率或 PD 类最大值即拒载，即使实际只需 4W（例：余 50W、口上限 75W→拒；调口上限 10W→放行）<<<PAGE 63>>>/<<<PAGE 64>>>
- **P35** Guard Band 不作用已在电 PD：预算缩减（如拔电源）场景改由 priority disconnect 裁决 <<<PAGE 64>>>

## 安装与安全机制

- **P36** 电涌防护军规（同 6360 五条）：全设备等电位接地（接地电阻 ≤0.01Ω）；室外/近交流线路用 STP Cat5e+；室外铜口必须串接浪涌保护器；防室外设备传浪涌电流给上游；Cat5e/6/6a 线可蓄静电须先对地放电防 CDE；违者可致失保："Failure to follow the above recommendations could result in voiding the warranty." <<<PAGE 10>>>/<<<PAGE 11>>>
- **P37** 电源托盘双形态：侧装托盘配机架应用、后装托盘配桌面应用——"Side mounted tray assemblies are typically used for rack mount applications; rear mounted tray assemblies are typically used for table mount applications." <<<PAGE 13>>>
- **P38** LED 语义体系：OK（稳绿=正常/闪绿=诊断中/稳琥珀=软件错误）；VC（灭=启动中/闪绿=VC Master/闪琥珀=VC Slave，闪烁次数=单元号，每 5 秒停顿）；PS1/PS2（灭=不在位/稳绿=正常/稳琥珀=电源故障）<<<PAGE 38>>>
- **P39** 端口 LED 用颜色区分 PoE：RJ45 口绿=非 PoE 链路、琥珀=PoE 设备已接（闪烁=有活动）；SFP/SFP+ 口琥珀=100M 链路 <<<PAGE 38>>>
- **P40** 接地规范：后部两螺孔接 Panduit LCD8-10AL lug、8AWG 铜导线、压接用 CT-940CH、扭矩 30-60 in-lb <<<PAGE 73>>>
