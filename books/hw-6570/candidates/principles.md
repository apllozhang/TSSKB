# principles — OmniSwitch 6570M Hardware Users Guide（硬件机制/架构/规格要点候选）

格式：编号 P# ｜ 要点 ｜ 页码（fulltext.md 真实 `<<<PAGE N>>>` 标记）

## 家族与端口架构

- **P1** 家族三机型：OS6570M-12（8×10/100/1000Base-T + 2×100/1000Base-X SFP + 2×Uplink/Stacking SFP+ 1G/10G + 内置 AC + 外部电源连接器）；OS6570M-12D（同端口、内置 DC）；OS6570M-U28（20×100/1000Base-X SFP + 4×SFP/RJ45 combo + 6×Uplink/Stacking SFP+ + 双电源舱）——"Fixed-configuration chassis" <<<PAGE 11>>>
- **P2** Uplink/Stacking 双角色口：SFP+ 口标注"Uplink/Stacking SFP+ Ports (1G/10G)"——同一对/组口既做上联又做 Virtual Chassis 堆叠链路（12 口机 11-12，U28 机 25-30 共 6 个） <<<PAGE 11>>>/<<<PAGE 21>>>/<<<PAGE 25>>>
- **P3** combo 口机制：U28 的 21-24 口为"100/1000Base-X SFP or 10/100/1000Base-T RJ45 combo ports"——一口两位（光/铜），同口位光铜互斥 <<<PAGE 11>>>/<<<PAGE 25>>>
- **P4** U28 全光上联型面板：1-20 纯 SFP 下联 + 21-24 combo + 25-30 SFP+，且独有前面板 Virtual Chassis ID LED——全光+堆叠定位 <<<PAGE 25>>>
- **P5** 半宽/全宽双包络：12/12D=21.72cm 宽×28.07cm 深×1.7kg（半宽）；U28=44cm 宽×35cm 深×4.08kg（不含电源，全宽 19 英寸）——半宽机可两台并排占 1U <<<PAGE 22>>>/<<<PAGE 24>>>/<<<PAGE 26>>>
- **P6** 待机功耗梯度：12=23W、12D=24W、U28=71W——光口密度推高基线功耗 <<<PAGE 22>>>/<<<PAGE 24>>>/<<<PAGE 26>>>

## 可用性体系

- **P7** 可用性三特性定义：Power Supply Redundancy（多电源冗余/负载分担）、Hot-Swapping（不断电加/换件）、Hardware Monitoring（"the switch immediately sends a trap to the user"）<<<PAGE 12>>>
- **P8** 监控三层：自动（内置传感器超阈值发 trap 到 console）+ LED（前后面板视觉状态）+ 用户驱动（show 命令）<<<PAGE 12>>>

## 温度机制

- **P9** 温度阈值按机型分化：12/12D 内部 Warning 85°C / Danger 88°C；U28 Warning 69°C / Danger 74°C——光口机热预算更紧，阈值低 16°C <<<PAGE 22>>>/<<<PAGE 24>>>/<<<PAGE 26>>>
- **P10** Tmra 统一 0-50°C；存储温度分化：12=-20~60°C、12D/U28=-40~85°C；湿度一律 5-95% 非凝结 <<<PAGE 22>>>/<<<PAGE 24>>>/<<<PAGE 26>>>
- **P11** 内部温度 vs Tmra 语义："Internal temperature refers to the sensor reading... Ambient temperature (Tmra) refers to the approximate room temperature. The ambient temperature will typically be lower." <<<PAGE 22>>>/<<<PAGE 24>>>/<<<PAGE 26>>>
- **P12** 温度双阈值行为：Warning 超限发 trap 且"switch operations remain active"（处置=查气流遮挡/室温）；Danger 超限"the switch will power off until...manually booted"——阈值出厂固化不可改 <<<PAGE 45>>>/<<<PAGE 46>>>
- **P13** show temperature 输出结构：Chassis/Device（1/CMMA）｜Current｜Range（15 to 85）｜Danger（88）｜Thresh（85）｜Status（UNDER THRESHOLD） <<<PAGE 45>>>

## 电源体系

- **P14** 双层电源架构（12/12D）：内置电源（12=AC 65W、12=DC 30W，均 12V/5.42A 输出）+ External Power Connector 外部电源连接器（可插 OS6570-12-BP 60W AC 或 OS6570-12-BP-D 30W DC 备份） <<<PAGE 11>>>/<<<PAGE 35>>>
- **P15** 外置备份电源对：OS6570-12-BP（DA-60Z12，100-240VAC→12V/5A 60W）配 12；OS6570-12-BP-D（DDR-30L-12，18-75VDC 宽压输入→12V/2.5A 30W）配 12D——AC/DC 各随其主机型 <<<PAGE 35>>>/<<<PAGE 36>>>/<<<PAGE 37>>>
- **P16** 12D 外置 DC 宽压输入：18-75VDC（Tolerances Included）——比 U28 的 150W DC（-36~-72VDC）范围更宽，适配电池直挂场景 <<<PAGE 37>>>/<<<PAGE 39>>>
- **P17** 30W DC 双态 LED：Solid Green=DC power is good；Solid Red=There is a DC power issue <<<PAGE 37>>>
- **P18** U28 双 150W 电源：OS6570-BP（PS-150W-AC，100-240VAC/3-1.5A→150W/12.5A，0.88kg）与 OS6570-BP-D（PS-150W-DC，-36~-72VDC/1.8-6A→150W/12.5A）——双舱可冗余/负载分担 <<<PAGE 35>>>/<<<PAGE 38>>>/<<<PAGE 39>>>
- **P19** 150W 电源六态 LED 语义：稳绿=供电正常；闪绿=待机可接管（"power supply is on standby"）；闪红=本电源无 AC 但邻舱有电；闪绿红=告警；稳红=故障；灭=全机无任何电源输入 <<<PAGE 38>>>/<<<PAGE 39>>>
- **P20** 无电源开关语义："The chassis does not provide an on/off switch. Connecting a the power supplies to a power source will boot the switch." <<<PAGE 42>>>
- **P21** 电源热插拔锁扣机制：插入滑至背板"the lock tab will click and hold"；拆卸按锁扣向中心（"Pressing the lock tab toward the center of the power supply"）后直拉 <<<PAGE 41>>>/<<<PAGE 42>>>/<<<PAGE 43>>>
- **P22** 电源托盘通用化："The same power supply tray is used for both AC and DC power supplies"——4 螺丝固定托盘+2 螺丝支架+2 螺丝盖板+附赠扎带理线 <<<PAGE 44>>>

## DC 接线与接地机制

- **P23** DC 供电五条安全前提：可靠接地 -48VDC SELV 源、支路过流保护 15A、12AWG 铜导线、易达断路装置、受限场所安装 <<<PAGE 40>>>
- **P24** DC 三芯极性约定：Green/yellow=ground、Black=return、Red=-48VDC；"The battery return conductor is an Isolated DC Return (DC-1)"；产品按 CBN（Common Bonding Network）设计 <<<PAGE 40>>>
- **P25** 机箱 supplemental 接地：前/后接地耳用 10-32 螺丝+无漆区金属接触；Panduit LCD8-10A-L lug + 8AWG 铜线；后板双接地孔同样规格——补充而非替代电源线接地 <<<PAGE 40>>>/<<<PAGE 45>>>

## LED 与面板机制

- **P26** 四组状态 LED：OK 三态（稳绿=诊断与 AOS 启动 OK/闪绿=进行中/稳琥珀=启动失败）；VC 四态（稳绿=master/稳琥珀=slave/闪琥珀=12 口机型以闪烁次数报 unit 号/灭=关机或不在 VC）；PS1/PS2 按机型两套语义（U28 三态含琥珀故障；12 口机仅绿=正常/灭=不在位）<<<PAGE 27>>>
- **P27** 端口 LED 全绿色系：千兆/SFP/SFP+ 口均稳绿=有效链路、闪绿=链路活动——无 PoE 琥珀色维度（本家族无 PoE） <<<PAGE 27>>>

## Dying Gasp 机制

- **P28** DG 三通道：整机失电时发 SNMP trap（前 3 个已配 SNMP 站，含槽号/主备电源类型/失效时间）+ Syslog"Dying Gasp Power Failure Event Occurred"（前 3 服务器）+ 4 个 802.3ah OAM Information PDU（Dying Gasp 位置位，发往 link OAM 使能且 operational 的口）<<<PAGE 46>>>/<<<PAGE 47>>>
- **P29** DG PDU 优先级："Dying gasp packets will be sent in the following order based on port priority: 1. Uplink ports 2. All other ports"——电容余量优先保上联通告 <<<PAGE 47>>>
- **P30** DG 触发三场景：唯一电源失效；主后备先后失效；后备主先后失效——"Connect each power supply to a separate independent power source to avoid simultaneous power failures." <<<PAGE 46>>>

## 安装机制

- **P31** 机架安装五项通则：Tmra（密闭多机架环温高于室温）、Reduced Air Flow、Mechanical Loading（防不均衡装载）、Circuit Overloading（过载对过流保护影响）、Reliable Earthing（尤其经电源排接线时）<<<PAGE 28>>>
- **P32** 间隙按机型分化：12 口机上下各 1 英寸（仅当有邻设备；无邻设备 N/A）+ 侧 2 英寸；U28 上下各 1.75 英寸（1RU）+ 侧 2 英寸；前后均 N/A <<<PAGE 28>>>
- **P33** 三套机架方案：全宽法兰（U28）；单半宽 OS6570M-RM-19-L（L 支架长短任意侧）；双半宽 OS6570M-DUO-MNT（slot/slide 支架+前后中央支架+盖板拇指螺丝，两台半宽并排成 19 英寸）<<<PAGE 29>>>/<<<PAGE 30>>>/<<<PAGE 32>>>
- **P34** 先下孔后上孔紧固纪律："insert a rack mount screw (not provided) through the bottom hole of each bracket. Tighten both screws until they are secure"——先承重后定位，三套方案一致 <<<PAGE 29>>>/<<<PAGE 34>>>
- **P35** EMP 线缆规则：EMP to a Switch=Straight-through；EMP to a Computer or Workstation=Crossover——带外管理口线序按对端设备类型选 <<<PAGE 16>>>
- **P36** 多电源上电时序："plug in each power supply in rapid succession, (i.e., within a few seconds of each other)"——保证启动全程供电充足 <<<PAGE 16>>>

---
合计：36 条（P1-P36）。
