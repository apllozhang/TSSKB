# principles — OmniSwitch 6575 Hardware Users Guide（硬件机制/架构/规格要点候选）

格式：编号 P# ｜ 要点 ｜ 页码（fulltext.md 真实 `<<<PAGE N>>>` 标记）

## 家族与端口架构

- **P1** 家族三机型按安装形态分化：OS6575-P12（"fanless, din-mountable"，8×10/100/1000Base-T 802.3bt 60W + 4×SFP+ Uplink/VFL）；OS6575-U28（"fanless, rack-mountable...1U"，4×PoE+ 90W combo + 20×SFP + 4×SFP+ VFL）；OS6575-MP16（"fanless, wall-mountable"，M12 连接器 16 口）——全部无风扇 <<<PAGE 11>>>
- **P2** MP16 四段端口阵列：1-4 纯 10/100（M12 D-code）、5-8 为 802.3at 30W PoE（D-code）、9-12 为 802.3bt 60W（M12 X-code）、13-16 为带 Bypass 功能的 10/100/1000（X-code）——一口一段功能，速率与 PoE 等级按段固定 <<<PAGE 11>>>/<<<PAGE 25>>>
- **P3** Port Bypass 断电旁路（MP16 独有）："automatically connects two network ports if the device loses power or fails which allows traffic to continue uninterrupted"——单交换机故障不中断关键链路 <<<PAGE 12>>>/<<<PAGE 25>>>
- **P4** Uplink/VFL 双角色口：P12 的 9-12 与 U28 的 29-32 标注"10G SFP+ Uplink / VFL"——上联与 Virtual Fabric Link 堆叠共用；U28 LED 绿=uplink/琥珀=VFL 分色指示 <<<PAGE 11>>>/<<<PAGE 21>>>/<<<PAGE 23>>>/<<<PAGE 28>>>
- **P5** 工业连接器体系（MP16）：Console/USB/Alarm 全部 M12 A-code 公头、Power 为 M23 5-pin、数据口 M12 D-code（10/100）与 X-code（千兆）——全防水加固，非 RJ45 <<<PAGE 25>>>/<<<PAGE 53>>>-<<<PAGE 55>>>
- **P6** M12 X-code PoE pinout 分组：1-4 脚 TXD1/RXD2 带 PoE-(G1)/PoE+(G1)、5-8 脚 BID4/BID3 带 PoE-(G2)/PoE+(G2)——千兆四对线两对组各承载双极性 PoE；D-code PoE 为 1/3 脚 PoE+、2/4 脚 PoE- <<<PAGE 54>>>
- **P7** 全家族 Tmra 工业级：-40~75°C（三机型一致）；存储 -40~85°C；湿度 5-95%——比机房交换机宽一档 <<<PAGE 22>>>/<<<PAGE 24>>>/<<<PAGE 26>>>
- **P8** 包络分化：P12=17×9.1×16.1cm/2.5kg（最小）；MP16=17.5×27×8cm/3.4kg（超薄挂墙）；U28=44×29.5×4.34cm/5.6kg（1U） <<<PAGE 22>>>/<<<PAGE 24>>>/<<<PAGE 26>>>
- **P9** 输入电压域分化：P12=24-57VDC max 8A；U28=24-60VDC max 3.5A；MP16=20-110VDC 超宽压——直流直挂/电池场景全适配 <<<PAGE 22>>>/<<<PAGE 24>>>/<<<PAGE 26>>>

## 电源与输入分档机制

- **P10** U28 输入电压三档 PoE 档位："50 - 57V: (3.5A), 150W max, PoE 802.3AT；44 - 57V: (3.5A), 120W max, PoE 802.3 AF；24 - 60V: (1.5A), Non-PoE, system only"——输入电压决定 PoE 等级与总功率 <<<PAGE 24>>>
- **P11** 48V 禁 PoE 红线（三机型面板注记）："Under 48VDC, PoE not supported."——第三方电源同理"For PoE support 48V or higher is required" <<<PAGE 21>>>/<<<PAGE 23>>>/<<<PAGE 25>>>/<<<PAGE 61>>>
- **P12** 四款电源矩阵：OS6NN5-BPNS（XDR-150E-48）150W 外置 AC（85-260VAC→54.5V，仅 P12）；OS6NN5-BPNSX（XDR-480E-48）480W 外置 AC（85-264VAC→54.5V/8.8A，P12+U28）；OS6575-BPR（PS-I180AC-P）180W 模块 AC（100-240VAC→+56V/3.22A，U28 后装最多 2）；OS6575-BPRD（PS-I180DC-P）180W 模块 DC（-20~-28V/12A 或 -36~-72V/6A→-56V，U28） <<<PAGE 36>>>/<<<PAGE 37>>>/<<<PAGE 38>>>/<<<PAGE 39>>>/<<<PAGE 40>>>
- **P13** 电源手动配置机制："The OmniSwitch 6575 cannot auto-detect the type of power supply connected."——必须 powersupply N name ... type ... 手动声明，否则系统与 PoE 功率信息错乱 <<<PAGE 46>>>
- **P14** 无电源开关语义："the chassis does not provide an on/off switch"——接电即开机、断全部电源即关机 <<<PAGE 36>>>
- **P15** 外置电源 ROJ（Removed Outer Jacket）接线制：输入线 L=黑/棕、N=白/蓝、PG=绿/绿黄条纹（30/33mm 剥线）；输出线 V-=红、V+=黑、PG=绿带 ring 端子——注意本机 V- 为红、V+ 为黑（与常规红正黑负相反） <<<PAGE 42>>>/<<<PAGE 43>>>
- **P16** ROJ 输出线接线力矩 3.5 in-lb；输入端子按电源标签力矩；地线用附带螺丝固定到电源并连到交换机电源连接器地端子 <<<PAGE 43>>>/<<<PAGE 44>>>/<<<PAGE 45>>>
- **P17** Pluggable Type A 电源线纪律："please make sure that the power socket is located near the equipment and is easily accessible"——插座须近设备且易达 <<<PAGE 45>>>
- **P18** 电源 DC OK LED 双态制：四款电源统一 Solid Green=DC power is good / Solid Red=There is a DC power issue <<<PAGE 37>>>/<<<PAGE 38>>>/<<<PAGE 39>>>/<<<PAGE 40>>>
- **P19** 双冗余电源同规格强制（三机型注记）："both power supplies must have identical output wattage and identical nominal output voltage. Use of dissimilar power supplies could result in unexpected behavior and is not supported." <<<PAGE 21>>>/<<<PAGE 23>>>/<<<PAGE 25>>>

## LED 与告警机制

- **P20** PS LED 三态带主备语义：稳绿="Main power supply and secondary power supply functioning normally"；稳琥珀=主或备之一正常；灭=不在位——与端口级 PoE 指示分离 <<<PAGE 27>>>
- **P21** Alarm In/Out LED：各一枚，Solid Red 分别表示"Alarm input detected"/"Alarm output detected" <<<PAGE 27>>>
- **P22** GRN（Leaf）省电模式灯：稳绿=Power Saving Mode、灭=Normal Operating Mode——绿色交换机节能态可视化 <<<PAGE 27>>>
- **P23** M12/RJ45 端口双色分 PoE：稳/闪绿=有效链路（非 PoE）；稳/闪琥珀=有效链路（PoE）——家族惯例 <<<PAGE 27>>>
- **P24** Alarm Relay 双通道机制：单线告警输入（外接温度/接近/门磁传感器，5-12VDC，针 1 正/针 2 地）+ 单线告警输出（继电器干接点，Max 220VDC/250VAC、2A、60W，NO/C/NC 三针）；通告方式=alarm output/trap/SWLog 三选 <<<PAGE 48>>>
- **P25** Alarm Relay VC 同步："On VC: The alarm input, traps, and system events are synced across all the chassis of the VC"——任一机的输入/事件可驱动任一机的输出；支持多对一、一对多映射 <<<PAGE 48>>>
- **P26** 告警继电器动作语义："When the alarm relay output is triggered, the normally open (NO) contact will close and the normally closed (NC) contact will open." <<<PAGE 49>>>
- **P27** 告警四态 LED 组合表：输入+动作为 alarm out→双 On；输入+动作 trap/SWLog→仅 Input On；系统事件触发输出→仅 Output On <<<PAGE 48>>>

## 温度与监控机制

- **P28** 温度双阈值（宽域设计）：show temperature 例 1/CMMA Current 33、Range -45 to 93、Thresh 93、Danger 98——阈值随 -40~75°C 环境域拉宽；Danger 阈值"factory-set and cannot be configured by the user" <<<PAGE 50>>>/<<<PAGE 51>>>
- **P29** Warning 超限发 trap 不停机、Danger 超限关机待手动重启——与家族一致；处置=查气流遮挡+查室温 <<<PAGE 50>>>/<<<PAGE 51>>>
- **P30** Dying Gasp 双通道（本书仅 SNMP+Syslog）：整机失电发 SNMP trap（前 3 站，含槽号/主备电源/时间）+ Syslog"Dying Gasp Power Failure Event Occurred"（前 3 服务器）；三触发场景同家族 <<<PAGE 52>>>

## PoE 机制

- **P31** PoE 规格栈：IEEE 802.3at/bt；at 口 3000-30000mW、bt 口 3000-90000mW（书表印"802.3ab"为 802.3bt 之误，Class 5-8 佐证）；三机型全支持 <<<PAGE 58>>>
- **P32** PoE 默认值六项：service=Disabled；端口功率 at=30000mW/HPoE=60000mW；priority=low；capacitor-detection=Disabled；priority-disconnect=Enabled <<<PAGE 59>>>
- **P33** PoE 温度阶梯预算（本书核心特色）：预算随 Tmra 分档降级——P12+1×BPNSX：≤50°C 330W→50-60°C 280W→60-70°C 238W→70-75°C 140W；U28+1×BPR(D)：75W→45W→30W→15W；高温场景预算可缩水过半 <<<PAGE 60>>>/<<<PAGE 61>>>
- **P34** 双电源预算增量不翻倍且高温可保持：P12 双 BPNSX 全温度域恒 360W（>70°C 时 180W）；U28 双 BPR(D) 210/150/110/75W；BPNSX 在 U28 上单双均恒 120W（受机内分配上限）<<<PAGE 60>>>
- **P35** MP16 预算封顶：150W 电源=52W 恒定（单双同）；480W 电源=120W 恒定——机内 PoE 路径上限主导，加电源不扩预算 <<<PAGE 61>>>
- **P36** PoE Class 0-8 全表（af 0-3：15.4/4/7/15.4W；at 4：30W；bt 5-8：45/60/75/90-99W）与 Pairs/Type 列 <<<PAGE 63>>>
- **P37** Guard Band 机制："If the amount of power remaining is less than the port's configured maximum PoE power value or the PD's class maximum power then the switch will not power up the PD"——剩余预算低于端口最大值即拒供（即使 PD 实际只需更少）；解法=调低端口 maxpower（如 10000mW）<<<PAGE 67>>>
- **P38** Priority Disconnect 四情形规则：禁用时新 PD 一律拒供；使能+同级→按物理口号（1 最高→8 最低）裁决；使能+新 PD 最高级→自动断最低级口（同级则断最高端口号）接纳；使能+新 PD 最低级→新 PD 被拒、存量不停 <<<PAGE 68>>>-<<<PAGE 70>>>
- **P39** 911/UPS 纪律："PoE-enabled switches with attached IP telephones should have operational power supply redundancy at all times for 911 emergency requirements... plugged into an Uninterruptible Power Source (UPS)." <<<PAGE 56>>>

## 供电配置机制

- **P40** powersupply type 命令例：`powersupply 1 name ALE-75W-ps1 type ale lo-ac`——命名+型号双参数；PoE 配置前置条件 <<<PAGE 46>>>/<<<PAGE 57>>>

---
合计：40 条（P1-P40）。
