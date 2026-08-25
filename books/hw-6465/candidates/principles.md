# principles — OmniSwitch 6465 Hardware Users Guide（硬件机制/架构/规格要点候选）

格式：编号 P# ｜ 要点 ｜ 页码（fulltext.md 真实 `<<<PAGE N>>>` 标记）

## 家族与端口架构

- **P1** 双线家族结构：工业线 OS6465-P6/P12/P12(ENH-240)/P28（无风扇、DIN 导轨、-40~75°C）+ 运输线 OS6465T-12/T-P12（T 后缀，半宽、内置电源、风扇 45°C 自启）："Fixed-configuration, fanless, din-mountable chassis" <<<PAGE 12>>>
- **P2** 60W/bt 口位规律：P6/P12 奇数口支持 60W/802.3bt（"Odd-numbered ports support 60W/802.3bt"）；P28 为口 1-8 支持 60W/bt；偶数口与其余口为 802.3at 30W <<<PAGE 12>>>/<<<PAGE 22>>>/<<<PAGE 31>>>
- **P3** 上行口分档：P6=2×SFP(100/1000Base-X)、P12=4×SFP、T 机型=2 combo + 2×SFP、P28=2×SFP + 4×SFP+(1G/10G)——仅 P28 有 10G 能力 <<<PAGE 12>>>/<<<PAGE 31>>>/<<<PAGE 33>>>/<<<PAGE 35>>>
- **P4** ENH-240 变体机制：同 P12 面板但输入范围扩至 20-60Vdc/10A、50-57V 时 240W PoE，面板标注"ENH-240"区分 <<<PAGE 12>>>/<<<PAGE 28>>>/<<<PAGE 30>>>
- **P5** 电源冗余 vs 负载分担："Only the OmniSwitch 6465-P28 supports power supply load sharing for Power over Ethernet, other models support power supply redundancy only."（第二电源在其他机型上仅做冗余备份）<<<PAGE 13>>>/<<<PAGE 50>>>
- **P6** 无电源开关语义：接电即开机、断全部电源即关机："the chassis does not provide an on/off switch. Connecting a power supply to a power source will boot the switch." <<<PAGE 50>>>

## 宽温与降额机制

- **P7** 三层温度指标体系：Ambient（Tmra，环境）/Internal Range（内部工作范围）/Warning(Thresh)+Danger 阈值——如 P6：环境 -40~75°C、内部 -45~93°C、Warning 93°C/Danger 94°C <<<PAGE 24>>>
- **P8** 各机型阈值梯度：P6 93/94、P12 95/97、ENH-240 84/89、P28 80/86、T-12 75/83、T-P12 78/85（°C，Warning/Danger）——ENH-240 因功率密度高阈值反而最低 <<<PAGE 24>>>-<<<PAGE 36>>>
- **P9** PoE 预算温度降额机制：P6/P12/ENH-240 按环境温度三档降额——≤60°C 全额（45/150/240W）、60-70°C 降额（30/130/240W，需 100 CFM 气流）、70-75°C 完全停止 PoE（"No PoE Provided"）<<<PAGE 74>>>
- **P10** P28 预算随电源组合变化：单 PS-I180 AC/DC@48V=112W（DC@24V 仅 72W）；双 AC 或双 DC@48V=285W；任何含 DC@24V 的组合=205W <<<PAGE 74>>>
- **P11** P28 DNV 电源盖降额：装 DNV 电源罩后环境上限从 75°C 收窄到 55°C："With DNV Power Supply Cover: -40°C to 55°C" <<<PAGE 32>>>
- **P12** T 机型风扇自启点：45°C 风扇自动开启，风扇开时环境上限 60°C、关时 45°C："Fan will turn on automatically at 45°C." <<<PAGE 34>>>/<<<PAGE 36>>>

## 输入电源机制

- **P13** 工业线宽压输入：P6/P12 为 24-60Vdc（ENH-240 20-60Vdc），按电压档定功率——50-57V 满 PoE（150/240W）、44-57V 限 af（120W）、24-60V 仅系统不带 PoE（1.5A）<<<PAGE 24>>>/<<<PAGE 27>>>/<<<PAGE 30>>>
- **P14** 双电源一致性强约束："both power supplies must have identical output wattage and identical nominal output voltage. Use of dissimilar power supplies could result in unexpected behavior and is not supported." <<<PAGE 24>>>/<<<PAGE 27>>>/<<<PAGE 30>>>
- **P15** 电源类型不可自动识别："The OmniSwitch 6465 cannot auto-detect the type of power supply connected. The type of power supply connected must be configured"——须用 `powersupply type` 手工配置（如 type ale lo-ac），否则系统与 PoE 信息显示/利用错误 <<<PAGE 60>>>
- **P16** 电源连接器前置：P6/P12/P28 电源接口在机箱前部（P28 后托盘式安装），两连接器可双电源 <<<PAGE 22>>>/<<<PAGE 50>>>

## 可用性与监控机制

- **P17** 可用性四件套：电源冗余、热插拔、自动监控（传感器 trap）、LED + 用户 show 命令 <<<PAGE 13>>>
- **P18** 告警继电器双线模型：单路告警输入（外接温度/接近/门磁传感器，5-12VDC）+ 单路告警输出继电器（NO/C/NC，最大 220VDC/250VAC、2A、60W）；系统事件、trap、SWLog 均可映射到输出 <<<PAGE 63>>>
- **P19** 告警 VC 同步机制：独立运行时输入/事件映射本地输出；VC 中输入/事件跨机箱同步——"The alarm output on any of the chassis can be set by the alarm input, trap, or system events of any other chassis."（支持多输入→单输出、单输入→多输出冗余）<<<PAGE 63>>>
- **P20** 告警自动清除 8 类事件：电源故障/温度超阈/Link-Down/Port-Health/Port-violation（风暴）/System-Health（CPU/内存/flash）/认证失败/告警输入——条件恢复即自动清除，也可 `alarm clear status` 手工清 <<<PAGE 65>>>
- **P21** Dying Gasp 三通道机制：整机失电瞬间残电发出 SNMP trap（前 3 个已配 SNMP 站，含槽号/电源主备/时间）+ Syslog（"Dying Gasp Power Failure Event Occurred"，前 3 个服务器）+ 4 个 802.3ah Link OAM PDU（置 Dying Gasp 位）<<<PAGE 68>>>
- **P22** Dying Gasp PDU 端口优先级：不可能所有 OAM 口都发出，顺序为上联口优先、其余口次之："1. Uplink ports 2. All other ports" <<<PAGE 69>>>
- **P23** 触发场景与防护建议：主电源坏（仅单电源时）、主备先后或备主先后全失；"Connect each power supply to a separate independent power source to avoid simultaneous power failures." <<<PAGE 68>>>
- **P24** 温度双阈值行为与 6360 同构：Warning 发 trap 不停机、Danger 自动关机需手动重启且不可配置 <<<PAGE 66>>>/<<<PAGE 67>>>

## LED 机制

- **P25** 系统 LED 组：OK（绿/闪绿/琥珀=启动失败）；VC（稳绿=master、稳琥珀=slave、闪琥珀次数=单元号）；PS1/PS2（绿=正常、琥珀=故障、灭=不在位）；Alarm In/Out（琥珀=有告警）<<<PAGE 36>>>/<<<PAGE 37>>>
- **P26** 电源自带 DC OK LED：绿=直流输出正常、红=直流故障（BPNX/BPN-H/BPN 三款相同定义）<<<PAGE 51>>>/<<<PAGE 52>>>/<<<PAGE 53>>>
- **P27** 端口 LED 颜色分 PoE：RJ45 绿=非 PoE、琥珀=PoE；SFP 与 SFP+ 各自绿系两态 <<<PAGE 37>>>

## 安装机制

- **P28** DIN 导轨快装机构：顶部卡扣先挂轨→下旋到底部卡扣"snaps in place"；拆卸下拉卡扣（难够到可用长螺丝刀）→向外旋出<<<PAGE 39>>>
- **P29** 间隙矩阵按安装方式分：DIN（P6/P12）上下方有设备才留 1 in、两侧 2 in、前后免；P28 机架上下各 1.75 in（1RU）；DNV 罩机型 1RU<<<PAGE 38>>>
- **P30** 双机并排套件（DUO-MNT）：slot/slide 托架前后拼接两台半宽机箱、板+拇指螺丝锁定后作为整体上机架 <<<PAGE 43>>>/<<<PAGE 44>>>
- **P31** DNV（船级社）三套件分工：OS6465-REAR-MNT（P28 侧轨+后托架）、OS6465-DNV-RACK（P28 电源托盘+电源罩）、OS6465-DNV-DIN（P6/P12 电源左右罩+DIN 卡扣）<<<PAGE 46>>>
- **P32** ROJ 电源线双色规：AC 输入北美黑(L)/白(N)/绿(PG)，国际棕/蓝/绿黄（ROJ 30/33mm）；DC 输出红(V-)/黑(V+)/绿(PG)——接线扭矩输出端 3.5 in-lb、输入端按电源标注 <<<PAGE 58>>>/<<<PAGE 59>>>/<<<PAGE 60>>>
- **P33** 接地规范同家族：Panduit LCD8-10A-L、8AWG 铜、30-60 in-lb、无漆区金属接触；NEBS 场景还要求星形垫圈防松、CBN 共模接地网、裸导线压接前清洁涂抗氧化剂 <<<PAGE 62>>>/<<<PAGE 93>>>

## PoE 机制

- **P34** PoE 规格栈（工业线）：802.3at + HPoE；普通口 3000-30000mW、HPoE 口（奇数/1-8 口）3000-60000mW；Class 表含 bt 5-8 类但端口按 60W 封顶 <<<PAGE 72>>>/<<<PAGE 76>>>
- **P35** lanpower 命令族与 6360 同构：service 两级激活（slot service start 才真正供电；admin-state 仅复活）、power/maxpower 上限不预留、priority 三级、capacitor-detection 仅 legacy 话机、Guard Band 拒载（余量<口上限即拒）、Priority Disconnect（同级按物理口号 1 高 8 低裁决）<<<PAGE 77>>>-<<<PAGE 84>>>
- **P36** T-P12 内置 185W 双输出：12V/5.42A 系统 + 54.5V/2.2A PoE 分路；T-12 内置 65W 仅系统 <<<PAGE 56>>>

---
合计：36 条（P1-P36）。
