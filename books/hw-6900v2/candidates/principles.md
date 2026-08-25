# principles — OmniSwitch 6900 Hardware Users Guide（硬件机制/架构/规格要点候选）

格式：编号 P# ｜ 要点 ｜ 页码（fulltext.md 真实 `<<<PAGE N>>>` 标记）

## 定位与家族架构

- **P1** 定位双栖：汇聚层 + 数据中心机柜顶："The OmniSwitch 6900 (OS6900) is a family of aggregation switches that can also be installed as top-of-rack boxes in data centers." <<<PAGE 12>>>
- **P2** 命名解码三轴：介质前缀（T=10GBaseT/X=SFP+/V=SFP28/D=QSFP-DD）+ 下行口数（48/24/32/72）+ 上行后缀（C6=6×QSFP28、C4E=4×QSFP28+8×SFP28、C8=8×QSFP28、C2=2×QSFP28）<<<PAGE 12>>>
- **P3** 十机型端口谱系：V72=48×SFP28+6×100G；C32=32×100G；C32E=32×100G+2×SFP+；T48C6=48×10GBaseT+6×100G；X48C6=48×SFP+ +6×100G；X48C4E=40×SFP+ +8×SFP28+6×100G；V48C8=48×SFP28+8×100G+2×SFP+；T24C2/X24C2=24 下行+2×SFP+ +2×100G；OS6920-D32=32×QSFP-DD 400G <<<PAGE 12>>>
- **P4** OS6920-D32 单口多形态：QSFP-DD 口支持 400G/2X200G/4X100G，向下兼容 QSFP56(200G)、QSFP28(100G)、QSFP+(40G) <<<PAGE 46>>>
- **P5** 全家族统一管理接口三件套：RJ45 10/100/1000 EMP 带外管理口 + console（USB 或 RJ45 按机型）+ USB 2.0 高速口（480Mbps），多数机型另有 Reset 按钮 <<<PAGE 12>>>
- **P6** 端口组速率约束机制：V72/X48C4E/V48C8 的 SFP28 口按 4 口一组锁定速率——"Ports within a port group must all run at either 10G speed or 25G speed."（组内 1G/10G 可混，但 25G 不能与 10G 混；V48C8 端口组编号非连续，如组 1=1,2,3,6）<<<PAGE 28>>>/<<<PAGE 38>>>/<<<PAGE 40>>>
- **P7** 全家族统一环境包络：Tmra 0-45°C、存储 -40~70°C、湿度 5%-95%；例外——OS6920 后→前气流限 0-35°C <<<PAGE 14>>>/<<<PAGE 29>>>等/<<<PAGE 47>>>
- **P8** 机箱深度三档：T48C6/X48C6/T24C2/X24C2 为 47.3cm；V72/C32/C32E/X48C4E/V48C8 为 51.5-53.6cm；OS6920-D32 深 59cm（23.23"）——决定机架深度与后支撑需求 <<<PAGE 29>>>等/<<<PAGE 35>>>等/<<<PAGE 47>>>
- **P9** 功耗谱系：桌面级 X24C2=75/197W → 中档 T48C6=139/315W → 高档 V48C8=226/532W、C32=145/543W → OS6920-D32 最高 1400W <<<PAGE 45>>>等/<<<PAGE 35>>>/<<<PAGE 41>>>/<<<PAGE 31>>>/<<<PAGE 47>>>
- **P10** chassis vs ambient 温度语义 + 机型差异："Due to different airflow characteristics, chassis temperatures will vary by model."（机箱温度恒高于室温且随机型变化）<<<PAGE 29>>>等

## 可用性与冗余机制

- **P11** 1+1 电源冗余模型："OS6900 switches provide 1+1 redundant hot-swappable power supplies and a hot-swappable fan tray."（第二电源装入后处于 standby 角色）<<<PAGE 12>>>/<<<PAGE 59>>>
- **P12** 热插拔三件：电源、光模块、风扇托盘——"The following hardware components can be hot-swapped: Power supplies / Transceivers / Fan tray." <<<PAGE 13>>>
- **P13** 三大可用性支柱：Power Supply Redundancy、Hot-Swapping、Hardware Monitoring（自动 trap + LED + 用户 show 命令）<<<PAGE 13>>>

## 气流机制（本书核心）

- **P14** 双向气流架构："The switch supports both Front-to-Rear and Rear-to-Front airflow depending on the fan tray and power supplies installed. The airflow direction of the power supplies and fan tray must be the same." <<<PAGE 50>>>
- **P15** 气流失配三段式后果：错误+trap 显示 → 若启动时检测到则 OK/PS LED 绿琥珀交替闪、GRN 闪绿且"the switch continuously reboots until the issue is corrected"；若运行中热插入失配件则 OK/PS 闪琥珀，到温度 Danger 阈值才重启 <<<PAGE 50>>>/<<<PAGE 52>>>
- **P16** 紫色防差错编码："To help users avoid mismatched fan trays and power supplies, rear-to-front components are marked with purple color coding. (Front-to-rear components use standard product colors.)" <<<PAGE 52>>>
- **P17** 气流路径双向设计：前→后=顶部前进风口吸入→穿越模块舱与电路板→后部风扇/电源排风；后→前=反向（后部吸入、前顶排出）<<<PAGE 51>>>
- **P18** 盲板气流机制："When blank cover panels are missing, air does not take the direct route from the air intake vents... normal airflow is disrupted and an extra task is placed on the fan tray to cool the chassis." <<<PAGE 53>>>

## 电源机制

- **P19** 六型电源两代阵营：V 系（650W AC/DC，配 V72/C32/C32E/X48C4E/V48C8）与 X 系（400W 或 200/400W AC/DC，配 T48C6/X48C6/T24C2/X24C2）+ OS6920 专用（1500W AC/1600W DC）；每型均分 F（前→后）/R（后→前）两气流版本 <<<PAGE 60>>>-<<<PAGE 65>>>
- **P20** 电源混插两条规则："Do not mix OS6900-V72/C32/C32E/X48C4E/V48C8 power supplies with OS6900-T48C6/X48C6/T24C2/X24C2 power supplies. Mixing an AC and DC power supply in the same chassis is supported."（代际不可混、AC+DC 可混）<<<PAGE 60>>>-<<<PAGE 65>>>
- **P21** 无总开关设计："Connecting an installed power supply to a power source will boot the switch. Likewise, disconnecting all installed power supplies from a power source will power off the switch." <<<PAGE 59>>>
- **P22** OS6920 电源双压输入：AC 1500W 在 100-127V 输出 12V/83.33A、220-240V 输出 12V/125A（高压输入得全功率）；"The system hold time for this power supply at 100% load is less than 20ms." <<<PAGE 64>>>
- **P23** 电源 LED 三态（全家族统一）：稳绿=正常供电、稳红=电源故障、灭=无 AC/DC 输入 <<<PAGE 60>>>-<<<PAGE 65>>>
- **P24** DC 供电纪律（OS6920 级）：接地 -40~-75V SELV 源；分支过流保护 50A；6AWG 铜导体；现场布线含断开装置；电源源须在受限进入场所；回流导体为 Isolated DC Return（DC-I）；设备设计装于 CBN <<<PAGE 66>>>
- **P25** IEC 60945 认证线缆：OS6900-X48C6 配 OS6900X-BPD-F 且需 IEC 60945（船用）认证时须用 OS-DNV-DC-PWR 线缆（双磁环）<<<PAGE 63>>>
- **P26** 冗余 AC 分电路原则："It is recommended that each AC outlet resides on a separate circuit." <<<PAGE 15>>>

## 风扇托盘机制

- **P27** 多风扇托盘架构：机箱后部 5 或 6 个独立风扇托盘（V72/C32/C32E/X48C4E/V48C8/OS6920 为 6 个；T48C6/X48C6/T24C2/X24C2 为 5 个），是机箱主温控部件 <<<PAGE 28>>>等
- **P28** 风扇托盘必装件："The fan tray is a required component. Never attempt to operate the switch without a fan tray installed." <<<PAGE 70>>>
- **P29** 风扇托盘分气流方向型号（F/R 后缀）且随机型专用："Do not attempt to install incompatible fan models in a chassis." <<<PAGE 70>>>/<<<PAGE 71>>>
- **P30** 60 秒更换窗口："The switch should not run without a fan tray more than 60 seconds to prevent over heating." <<<PAGE 72>>>

## LED 机制

- **P31** 系统 LED 五组：PS1/PS2（绿/琥珀/灭）；Diag（绿=正常/琥珀=自检故障）；Fan（绿/琥珀）；LOC（闪琥珀=远程定位激活）<<<PAGE 48>>>
- **P32** 端口速率 LED 分色：RJ45/SFP+（琥珀=1G、绿=10G）；SFP28（绿=25G、琥珀=10G、1G）；QSFP28 V/C 系（蓝=100G、琥珀=40G、LED1-4 白=4X25G、绿=4X10G）<<<PAGE 48>>>
- **P33** QSFP-DD 十二态色表：青=400G、紫=200G、蓝=100G、橙=40G、紫/绿=2X200G、蓝/绿=2X100G、黄/绿=2X50G、蓝/绿×3=4X100G、黄/绿×3=4X50G、白/绿×3=4X25G、全绿=4X10G、红=端口故障 <<<PAGE 48>>>

## 监控与温度机制

- **P34** 温度双阈值机制：Warning 超限→发 trap 业务继续（查气流阻塞/室温/风扇状态 `show fan`）；Danger 超限→自动关机直到人工处理并手动启动，Danger 出厂固化不可配置 <<<PAGE 75>>>
- **P35** 风扇自动监控："If any of the switch's fans unexpectedly shuts down, the switch sends out a trap and the FAN LED on the chassis front panel displays amber." <<<PAGE 75>>>
- **P36** 硬件监控命令族：`show module` / `show module long` / `show temperature` / `show fan` <<<PAGE 74>>>/<<<PAGE 75>>>

## 管理口机制

- **P37** EMP 线缆类型规则：EMP 接交换机用直通线（straight-through）、接计算机/工作站用交叉线（crossover）<<<PAGE 18>>>
- **P38** EMP 默认带外地址：IP 192.168.1.1 / 掩码 255.255.255.0；改址用 `ip interface emp address … mask …`，改前必须先走 console；未解锁会话类型前无法经 EMP 远程访问 <<<PAGE 22>>>
- **P39** console 流控机制："No hardware handshaking (RTS, CTS) is used. Instead, software flow control (XON, XOFF) is required."（RJ45 console 8 针定义：3=TXD、6=RXD、4/5=GND）<<<PAGE 76>>>
- **P40** 电涌防护军规五条：全设备等电位接地（≤0.01Ω）；室外/近交流线路用 STP Cat5e+；室外铜口串接浪涌保护器；防室外设备传浪涌给上游；Cat5e/6/6a 蓄静电须先对地放电防 CDE；违者可失保 <<<PAGE 15>>>/<<<PAGE 16>>>
