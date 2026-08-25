# Verified 候选（V1 原文真实性核对 + V2/V3 抽查）

## cases

## 上电与首次登录
- **C1** 上电流程：各电源线插入易达接地插座（禁延长线）；多电源数秒内先后插电；冗余 AC 每路独立电路；接电即自动开机 <<<PAGE 13>>>/<<<PAGE 16>>>
- **C2** 首次登录六步：console（rollover 线，9600/无流控/8N1，DCE）→admin/switch→aaa authentication 解锁会话→password 改密→system timezone/time/date→system contact/name/location→show system→write memory <<<PAGE 15>>>-<<<PAGE 19>>>
- **C3** 会话类型按类解锁：aaa authentication default local 全解锁；或 telnet/http/ftp local 逐条连续执行（一次只能一类） <<<PAGE 17>>>
## 机箱安装
- **C4** U28 前装机架流程：两侧装法兰→标记机架孔位→抬举对齐→先下孔螺丝后上孔螺丝紧固；螺丝自备 <<<PAGE 29>>>/<<<PAGE 30>>>
- **C5** U28 后装机架流程（OS6575-REAR-MNT 套件：2 侧轨+2 后支架+1 支撑支架+18×M4X8MM；另 OS6575-TRAY-1U 电源托盘）：装侧轨（各 7×M4，按孔位 A/C）+后支架+支撑支架（3×M4）→装电源托盘（4×M4）→装电源→整机入机架以拇指螺丝固定 <<<PAGE 31>>>/<<<PAGE 32>>>
- **C6** P12 DIN 导轨安装：DIN Rail Bracket 选件装于机箱→挂扣 DIN 导轨（"DIN Mounted Chassis"） <<<PAGE 33>>>
- **C7** P12 壁装流程：Wall Bracket 选件安装→挂壁（"The OmniSwitch-P12 is wall mountable"） <<<PAGE 34>>>
- **C8** MP16 壁装流程：利用机箱 Mounting Holes（后面板四角）直接螺丝挂壁 <<<PAGE 26>>>/<<<PAGE 35>>>
- **C9** 现场准备检查单：维持 -40~75°C 温湿度域；预留通风空间；每电源一个接地插座；2 米原装电源线；专业安装师负责接地与电气规范 <<<PAGE 13>>>/<<<PAGE 29>>>
- **C10** 开箱核对清单：机箱与电源按订单、光模块按订单、盲板、机架法兰、国别电源线、橡胶桌脚、螺丝、防静电袋与说明卡 <<<PAGE 15>>>
## 电源安装与 ROJ 接线
- **C11** 后装托盘电源安装流程（U28）：电源定向→DB-15 两侧导柱对准机箱后部导孔滑入→推至连接器完全就位→拧电源前端拇指螺丝→冗余配置在对侧连接器与螺孔重复 <<<PAGE 41>>>
- **C12** ROJ 输出线接线流程（电源→机箱）：红线插电源顶部前端 V- 端子与交换机电源连接器(-)端→黑线插 V+ 与(+)端→螺丝刀每端子拧 3.5 in-lb→绿线 ring 端子用附带螺丝固定电源地端并连交换机地端 <<<PAGE 43>>>/<<<PAGE 44>>>
- **C13** ROJ 输入线接线流程（市电→电源）：黑/棕线插底部前端 L 端子→白/蓝线插 N 端子→绿/绿黄条纹线插保护地端子→按电源标签力矩拧紧各端子 <<<PAGE 45>>>
- **C14** 最终上电连接：输出线插机箱前面板 PS1/PS2 电源连接器→AC 线 NEMA 5-15 头插易达 AC 源——插头在接到提示前不得插入电源或带电插座 <<<PAGE 45>>>/<<<PAGE 43>>>
- **C15** 电源热拔流程：从电源源侧拔插头→松开全部输入端子拆 AC 输入线→松开全部输出端子拆输出线→按接线流程装新电源（冗余下单电源可换不影响运行） <<<PAGE 46>>>
- **C16** 电源类型声明：powersupply 1 name ALE-75W-ps1 type ale lo-ac（逐电源声明；不能自动检测） <<<PAGE 46>>>
## 接地
- **C17** 机箱 supplemental 接地：Panduit LCD8-10A-L lug+10-32 螺丝装于接地耳无漆区→8AWG 铜线接大地→力矩 30-60 in-lb <<<PAGE 47>>>
## Alarm Relay 配置
- **C18** 告警输入→输出联动配置：alarm in temperature-alarm-in action alarm-out admin-state enable→alarm out alarm-out-1 admin-state enable→alarm map temperature-alarm-in out alarm-out-1 <<<PAGE 49>>>
- **C19** 系统事件→输出映射（认证失败例）：alarm event auth-fail-event event authentication-failure admin-state enable→alarm out set-alarm-out-chassis-1→alarm map auth-fail-event out set-alarm-out-chassis-1；show alarm event config 核对、show alarm status 看实时、alarm clear status 清除 <<<PAGE 49>>>
## 监控与 PoE 配置
- **C20** 硬件巡检流程：show module / show module long→show temperature（UNDER THRESHOLD 正常）→show powersupply（Total Power/PS Type/Status/Location）<<<PAGE 50>>>/<<<PAGE 62>>>
- **C21** DG 告警接收配置：snmp station 配 SNMP 站（trap 前 3 站生效）；swlog output socket 加 Syslog 服务器 <<<PAGE 52>>>
- **C22** PoE 首次激活流程：先 powersupply type 声明电源→lanpower slot 1/1 service start→show lanpower 1/1 核对逐口 Maximum/Actual/Status/Priority/On-Off/Class 与槽预算 <<<PAGE 46>>>/<<<PAGE 64>>>/<<<PAGE 71>>>
- **C23** PoE 关断两级：单口 lanpower port 1/1/4 admin-state disable；整槽 lanpower slot 1/1 service stop；admin-state enable 仅复活被断口 <<<PAGE 64>>>
- **C24** 端口/槽功率调节：lanpower port 1/1/4 power 3000（降口限额保预算）；lanpower slot 1/1 maxpower 400（调槽上限，注意调低可致低优先级口掉电） <<<PAGE 64>>>/<<<PAGE 65>>>
- **C25** 端口优先级设置：lanpower port 1/1/4 priority critical——低/高/关键三档，关键口在电力管理事件中最后断电 <<<PAGE 65>>>
- **C26** Guard Band 解锁小功率 PD：剩余预算 < 端口 maxpower 时 PD 不上电→lanpower power 1/1/1 power 10000 调低口上限至低于剩余预算→PD 正常上电 <<<PAGE 67>>>
- **C27** Priority Disconnect 开关：lanpower slot 2/1 priority-disconnect disable/enable——禁用后新 PD 一律按预算拒供不抢电 <<<PAGE 68>>>

---
合计：27 条（C1-C27）。

## counter-examples

## 供电与 PoE 限制
- **X1** 48VDC 以下禁 PoE（三机型面板注记）："Under 48VDC, PoE not supported."；第三方电源"For PoE support 48V or higher is required." <<<PAGE 21>>>/<<<PAGE 23>>>/<<<PAGE 25>>>/<<<PAGE 61>>>
- **X2** 双电源禁混规格："both power supplies must have identical output wattage and identical nominal output voltage. Use of dissimilar power supplies could result in unexpected behavior and is not supported."（三机型同注） <<<PAGE 21>>>/<<<PAGE 23>>>/<<<PAGE 25>>>
- **X3** 电源类型不能自动检测："The OmniSwitch 6575 cannot auto-detect the type of power supply connected. The type of power supply connected must be configured..."——不配置则系统与 PoE 功率显示/利用错误，且 PoE 配置前置 <<<PAGE 46>>>/<<<PAGE 57>>>
- **X4** NEMA 插头不得提前带电插拔："Do not insert the NEMA 5-15 plug or power connector into the power supply or any live power source until prompted to do so. Failure to follow these instructions may result in bodily injury and/or equipment damage." <<<PAGE 43>>>
- **X5** 只准用 ALE 原厂配件："Only parts provided by Alcatel-Lucent Enterprise should be used when installing the power supplies." <<<PAGE 42>>>
- **X6** class detection 开启复位全口："Enabling class detection will reset all PoE ports on the chassis." <<<PAGE 64>>>
- **X7** admin-state 不能首次激活 PoE："You cannot use the lanpower port admin-state command to initially activate PoE on a port."（须 lanpower slot service） <<<PAGE 64>>>
- **X8** 电容检测不符 IEEE："The capacitive detection method should only be enabled to support legacy IP phones. This feature is not compatible with IEEE specifications." <<<PAGE 66>>>
- **X9** 调低槽预算可掉电："Decreasing the slot-wide power could cause lower priority ports to lose power if the new value is less than the total PoE power currently being consumed." <<<PAGE 65>>>
- **X10** maxpower 不预留功率："Changing the maximum power available to a slot or port does not reserve or immediately allocate that power."——仅设上限，余量仍入总预算池 <<<PAGE 65>>>
- **X11** Guard Band 对已上电 PD 不适用："The Guard Band functionality does not apply to PDs that are already powered up."——但预算缩减（如拔电源）时 priority disconnect 会生效 <<<PAGE 67>>>
- **X12** 高温预算降档：温度阶梯预算表——如 P12+1×BPNSX 从 ≤50°C 的 330W 降至 70-75°C 的 140W；U28+1×BPR(D) 从 75W 降至 15W——高温环境不得按常温预算满配 <<<PAGE 60>>>
- **X13** MP16 加电源不扩预算：150W→52W 恒定、480W→120W 恒定（单双电源相同）——机内路径封顶，叠电源只为冗余 <<<PAGE 61>>>
## 登录与系统限制
- **X14** aaa authentication 一次一类："You cannot specify more than one session type in a single command line." <<<PAGE 17>>>
- **X15** 密码覆盖受限："Be sure to remember or securely record all new passwords; overriding configured passwords on an OmniSwitch is restricted." <<<PAGE 18>>>
- **X16** Danger 阈值固化不可配："The Danger threshold is factory-set and cannot be configured by the user." <<<PAGE 51>>>
- **X17** Danger 超限须手动重启："the switch will power off until the temperature conditions have been addressed and the switch is manually booted." <<<PAGE 51>>>
## 安装与电气警告
- **X18** 禁延长线："Do not use extension cords."；非 ALE 电源线需安装者自证合规 <<<PAGE 13>>>
- **X19** 违反电涌军规可能失保："Failure to follow the above recommendations could result in voiding the warranty of the affected ALE product."（接地 0.01Ω/STP/浪涌保护器/室外雷电流/CDE 五条） <<<PAGE 14>>>
- **X20** 室外禁裸线缆："Never install exposed network cables outdoors." <<<PAGE 15>>>/<<<PAGE 80>>>
- **X21** Type A 电源线插座须易达："The product uses a Pluggable Type A power cord; therefore, please make sure that the power socket is located near the equipment and is easily accessible." <<<PAGE 45>>>
- **X22** 密闭多机架环温偏高（General Mounting Recommendations：Tmra/气流/机械载荷/电路过载/可靠接地五项通则） <<<PAGE 29>>>
- **X23** 机架螺丝自备："insert a rack mount screw (not provided)" <<<PAGE 30>>>
- **X24** 盲板必须常装："Because they regulate airflow and help protect internal chassis components, blank cover plates should remain installed at empty module slots and power supply bays at all times." <<<PAGE 81>>>
## NEBS 与接地
- **X25** OSP 禁金属直连："The intra-building port(s)...MUST NOT be metallically connected to interfaces that connect to the OSP or its wiring... The addition of Primary Protectors is not sufficient protection"（GR-1089-CORE）<<<PAGE 80>>>
- **X26** AC 电源必须接 SPD："The AC power supply must be connected to a surge protection device (SPD)." <<<PAGE 80>>>
- **X27** 接地细则：星形垫圈防松（"Star washers must be used to prevent any connections from loosening"）、裸导体压接前清洁并涂抗氧化剂、CBN 共模连接网络、仅用铜导体接地 <<<PAGE 80>>>
## 作业与激光安全
- **X29** 运行中勿触背板/电源舱："keep your hands and fingers out of power supply bays and do not touch the backplane while the switch is operating." <<<PAGE 82>>>
- **X30** 多电源设备搬运前全断："be sure to disconnect all power connections before servicing or moving the unit." <<<PAGE 82>>>
- **X31** Class 1M 激光："CLASS 1M LASER RADIATION WHEN OPEN. DO NOT VIEW DIRECTLY WITH OPTICAL INSTRUMENTS."；空光口勿直视并加盖 <<<PAGE 21>>>/<<<PAGE 80>>>/<<<PAGE 81>>>
- **X32** ESD 腕带强制："you must follow proper procedures to eliminate ESD from your person and the surrounding area before handling switch components." <<<PAGE 84>>>
- **X33** 锂电池更换须返厂："There is a danger of the explosion if the lithium battery in your chassis is substituted incorrectly... Return the module with the lithium battery to Alcatel-Lucent."（西班牙语安全节） <<<PAGE 85>>>
- **X34** 受限场所安装："This equipment should be installed in a location that restricts access."（正文与 NEBS 均要求） <<<PAGE 80>>>/<<<PAGE 83>>>
- **X35** Class A 住宅禁用："To avoid electromagnetic interference, this product should not be installed or used in residential environments." <<<PAGE 79>>>

---
合计：35 条（X1-X35）。

## frameworks

- **F1** 6575 家族选型三轴矩阵：轴一=安装形态（P12=DIN 导轨/壁装配电柜；U28=19 英寸机架 1U；MP16=壁装工业现场）；轴二=端口与连接器（P12=8×bt 60W RJ45；U28=全光 24 SFP+4 combo；MP16=M12 防水四段阵列 at/bt/纯数据/bypass）；轴三=供电与 PoE（P12=外置 BPNS/BPNSX；U28=后装双 BPR/BPRD 或 BPNSX；MP16=20-110VDC 宽压直挂）。选型口诀：按物理环境定形态，按 PD 等级定 PoE 段（at 30W/bt 60W/bypass 保链路），再按温度查预算表选电源档（高温场预算减半，双电源既有冗余又保预算）。 <<<PAGE 11>>>/<<<PAGE 21>>>/<<<PAGE 23>>>/<<<PAGE 25>>>/<<<PAGE 60>>>
- **F2** 温度-PoE 预算联动框架：预算=机型×电源×数量×温度带四元函数。部署四查：一查 Tmra 所在温度带（≤50/50-60/60-70/70-75°C）；二查机型×电源×数量的预算表（注意 MP16/U28+BPNSX 有机内封顶，加电源不扩容）；三查输入电压档位（U28：50-57V=at 150W、44-57V=af 120W、24-60V=纯系统、<48V 一律禁 PoE）；四查 Guard Band（剩余预算须大于端口 maxpower 才上电，必要时调低口上限）。 <<<PAGE 24>>>/<<<PAGE 60>>>/<<<PAGE 61>>>/<<<PAGE 67>>>
- **F3** 工业高可用三支柱框架：链路侧=MP16 Port Bypass 断电旁路（13-16 口失电自动直连保通信）；供电侧=双同规格电源+独立电路+UPS（911 纪律）+Dying Gasp 双通道（SNMP trap/Syslog 各前 3 目标）+Alarm Relay 干接点外送（NO/NC 触点 220VDC/250VAC/2A）；运行侧=无风扇宽温（-40~75°C）+温度双阈值（93/98°C：Warning 发 trap→Danger 关机手动恢复）+Alarm in/out/event 三源映射（VC 内跨机同步）。 <<<PAGE 12>>>/<<<PAGE 48>>>/<<<PAGE 50>>>-<<<PAGE 52>>>

---
合计：3 条（F1-F3）。

## glossary

- **OS6575-P12**：无风扇 DIN 导轨机，8×10/100/1000Base-T 802.3bt 60W + 4×SFP+ Uplink/VFL，24-57VDC/8A 输入，系统功耗 50W，2.5kg <<<PAGE 11>>>/<<<PAGE 21>>>/<<<PAGE 22>>>
- **OS6575-U28**：无风扇 1U 机架机，4×PoE+ 90W combo + 20×100FX/1G SFP + 4×SFP+ Uplink/VFL，双后装电源，24-60VDC 输入，待机 60W <<<PAGE 11>>>/<<<PAGE 23>>>/<<<PAGE 24>>>
- **OS6575-MP16**：无风扇壁装工业机，M12/M23 连接器，4×10/100 + 4×at 30W + 4×bt 60W + 4×Bypass 千兆口，20-110VDC 宽压，3.4kg <<<PAGE 11>>>/<<<PAGE 25>>>/<<<PAGE 26>>>
- **Port Bypass**：断电旁路特性（MP16 13-16 口）——失电或故障时自动直连两口保通信 <<<PAGE 12>>>/<<<PAGE 25>>>
- **Uplink / VFL**：上联/虚拟 fabric 链路双角色 SFP+ 口（LED 绿=uplink/琥珀=VFL） <<<PAGE 11>>>/<<<PAGE 28>>>
- **Availability Features**：可用性三特性——电源冗余/热插拔/硬件监控 <<<PAGE 12>>>

## 快速入门（Ch2）
- **Grounding wrist strap**：接地防静电腕带（安装三件套之一） <<<PAGE 13>>>
- **Electrical Surge Warning**：电涌警告五条军规（接地 0.01Ω/STP/浪涌保护器/室外防雷/CDE） <<<PAGE 14>>>
- **CDE（Cable Discharge Event）**：电缆静电放电——Cat5e/6/6a 储静电，接线前先瞬时接地 <<<PAGE 14>>>
- **Serial Default Settings**：console 默认 9600/无流控/8N1，rollover 线 <<<PAGE 15>>>
- **rollover cable**：反转线——本家族 console 线型 <<<PAGE 15>>>
- **admin/switch**：出厂默认登录名/密码 <<<PAGE 16>>>
- **aaa authentication**：会话类型解锁命令（一次一类） <<<PAGE 17>>>
- **system timezone / daylight-savings-time**：时区/夏令时命令（默认 UTC） <<<PAGE 18>>>
- **show system / write memory**：查看/保存配置命令 <<<PAGE 19>>>

## 机箱与 LED（Ch3）
- **Tmra**：环境工作温度 -40~75°C（三机型一致，工业级） <<<PAGE 22>>>/<<<PAGE 24>>>/<<<PAGE 26>>>
- **PS LED**：电源灯三态——绿=主备均正常/琥珀=仅其一正常/灭=不在位 <<<PAGE 27>>>
- **Alarm In / Alarm Out LED**：告警输入/输出灯，Solid Red 表示各自检测到触发 <<<PAGE 27>>>
- **GRN（Leaf）LED**：省电模式灯——绿=Power Saving Mode/灭=Normal <<<PAGE 27>>>
- **1/CMMA**：show temperature 传感器标识（Range -45~93/Danger 98/Thresh 93） <<<PAGE 50>>>
- **Warning/Danger Threshold**：温度警告/危险阈值——Danger 出厂固化不可配，超限关机待手动重启 <<<PAGE 50>>>/<<<PAGE 51>>>

## 安装套件（Ch3）
- **OS6575-REAR-MNT**：U28 后装套件——2 侧轨+2 后支架+1 支撑支架+18×M4X8MM 螺丝 <<<PAGE 31>>>
- **OS6575-TRAY-1U**：U28 1U 电源托盘（4×M4 螺丝安装） <<<PAGE 31>>>
- **DIN Rail Bracket**：P12 DIN 导轨安装支架选件 <<<PAGE 22>>>/<<<PAGE 33>>>
- **Wall Bracket**：P12 壁装支架选件；MP16 用自带 Mounting Holes <<<PAGE 22>>>/<<<PAGE 34>>>/<<<PAGE 26>>>
- **Rack mount screw (not provided)**：机架螺丝不随机提供 <<<PAGE 30>>>

## 电源体系（Ch3）
- **OS6NN5-BPNS（XDR-150E-48）**：150W 外置 AC 电源（85-260VAC→54.5VDC），配 P12 <<<PAGE 37>>>
- **OS6NN5-BPNSX（XDR-480E-48）**：480W 外置 AC 电源（85-264VAC→54.5V/8.8A），配 P12/U28 <<<PAGE 38>>>
- **OS6575-BPR（PS-I180AC-P）**：180W 模块 AC 电源（100-240VAC→+56V/3.22A），U28 后装最多 2 个 <<<PAGE 39>>>
- **OS6575-BPRD（PS-I180DC-P）**：180W 模块 DC 电源（-20~-28V/12A 或 -36~-72V/6A→-56V），U28 <<<PAGE 40>>>
- **ROJ（Removed Outer Jacket）**：剥外皮电源线制——外置电源输入/输出均为裸线端子接线 <<<PAGE 42>>>
- **V- / V+ 端子**：输出线极性——红=V-、黑=V+（本机红负黑正）、绿=保护地（ring 端子） <<<PAGE 42>>>/<<<PAGE 43>>>
- **L / N / PG 端子**：输入线端子——L=黑/棕、N=白/蓝、PG=绿/绿黄条纹 <<<PAGE 42>>>/<<<PAGE 45>>>
- **3.5 inch-pounds**：输出端子接线力矩；输入端子按电源标签 <<<PAGE 43>>>/<<<PAGE 45>>>
- **DB-15 连接器 / Guide Pins**：后装电源与机箱对接的连接器及两侧导柱 <<<PAGE 41>>>
- **NEMA 5-15**：AC 插头标准——未到提示步骤不得插入带电插座 <<<PAGE 43>>>/<<<PAGE 45>>>
- **powersupply type 命令**：手动声明电源型号（不能自动检测），如 type ale lo-ac <<<PAGE 46>>>
- **Thumb Screw**：后装电源固定拇指螺丝 <<<PAGE 41>>>

## Alarm Relay（Ch3）
- **Alarm Relay**：告警继电器——系统事件/告警输入的输出/trap/SWLog 通告机制 <<<PAGE 48>>>
- **Alarm Input**：单线告警输入（5-12VDC，外接温度/门磁/接近传感器） <<<PAGE 48>>>
- **Alarm Output**：单线继电器干接点输出（Max 220VDC/250VAC/2A/60W） <<<PAGE 48>>>
- **NO / C / NC**：常开/公共/常闭触点——触发时 NO 闭合、NC 断开 <<<PAGE 48>>>/<<<PAGE 49>>>
- **alarm in/out/map/event 命令族**：告警输入定义/输出使能/映射/事件绑定配置 <<<PAGE 49>>>
- **show alarm event config / show alarm status / alarm clear status**：告警配置/实时状态/清除命令 <<<PAGE 49>>>
- **VC 同步**：VC 内告警输入/trap/系统事件跨机同步，支持多对一/一对多映射 <<<PAGE 48>>>

## Dying Gasp（Ch3）
- **Dying Gasp**：临终告警——失电时发 SNMP trap（前 3 站）+ Syslog（前 3 服务器） <<<PAGE 52>>>
- **Dying Gasp Power Failure Event Occurred**：DG Syslog 消息原文 <<<PAGE 52>>>
- **snmp station / swlog output socket**：DG 告警接收端配置命令 <<<PAGE 52>>>

## M12/M23 连接器与线缆（Ch3）
- **M23 5-pin（Power）**：MP16 电源连接器——PWR-1±/FGND/PWR-2± 双路输入 <<<PAGE 25>>>/<<<PAGE 53>>>
- **M12 A-code**：Console/USB/Alarm 公头连接器（TX/RX/GND；D+/D-/VCC；DO-NO/DO-NC/DO-Comm） <<<PAGE 25>>>/<<<PAGE 53>>>
- **M12 D-code**：10/100 口连接器（TX±/RX±，PoE 版 1/3 脚 PoE+、2/4 脚 PoE-） <<<PAGE 25>>>/<<<PAGE 54>>>
- **M12 X-code**：千兆口连接器（8 脚四对差分，PoE 版 G1/G2 两对组各 PoE±） <<<PAGE 25>>>/<<<PAGE 54>>>
- **M23-PWRCONN-5P**：M23 电源插座配件（5 只装，不带线） <<<PAGE 55>>>
- **M12-USB-2P / M12-CONSOLE-5P**：M12 转 USB / RS232 console 配件线缆 <<<PAGE 55>>>
- **M12-ALARM-6P**：M12 转裸线告警线缆（1m 6 只装） <<<PAGE 55>>>
- **M12-DC-M/RJ45F/RJ45M-8P**：D-code 转 D-code/RJ45 配件线缆族 <<<PAGE 55>>>
- **M12-XC-M/RJ45F/RJ45M-8P**：X-code 转 X-code/RJ45 配件线缆族 <<<PAGE 55>>>

## PoE（Ch4）
- **PoE/PoL/Inline Power**：以太网供电同义术语族 <<<PAGE 56>>>
- **PD / PSE**：受电设备/供电设备 <<<PAGE 56>>>
- **802.3at / 802.3bt**：PoE+ 30W / PoE++ 90W 标准；本机 at 口 3000-30000mW、bt 口 3000-90000mW <<<PAGE 58>>>
- **PoE 温度阶梯预算表**：按机型×电源×数量×温度带（≤50 至 70-75°C 四档）的预算矩阵 <<<PAGE 60>>>/<<<PAGE 61>>>
- **lanpower slot service start/stop**：PoE 整槽启停（首次激活必用） <<<PAGE 64>>>
- **lanpower port admin-state enable/disable**：单口 PoE 复活/关断（不能首次激活） <<<PAGE 64>>>
- **lanpower power / lanpower slot maxpower**：口/槽功率上限命令 <<<PAGE 64>>>/<<<PAGE 65>>>
- **lanpower priority**：口优先级 low/high/critical（默认 low） <<<PAGE 65>>>
- **lanpower class-detection**：等级检测使能（开启复位全口） <<<PAGE 64>>>
- **lanpower capacitor-detection**：电容检测法（仅老 IP 话机，不符 IEEE） <<<PAGE 66>>>
- **Guard Band**：保护带机制——剩余预算低于口 maxpower 即拒供新 PD <<<PAGE 67>>>
- **Priority Disconnect**：优先级断开——预算不足时按优先级+物理口号裁决新 PD 供电 <<<PAGE 68>>>
- **show lanpower slot**：PoE 逐口状态/槽预算查看命令 <<<PAGE 63>>>/<<<PAGE 71>>>
- **show powersupply**：电源类型/状态/总功率查看命令 <<<PAGE 62>>>
- **911/UPS 纪律**：带 IP 话机的 PoE 交换机须常备电源冗余并接 UPS <<<PAGE 56>>>

## 法规与工业标准（附录 A）
- **NEBS GR-1089-CORE**：电信设备电气防护——楼内端口禁金属直连 OSP、AC 须接 SPD <<<PAGE 80>>>
- **CBN（Common Bonding Network）**：共模连接网络——NEBS 安装要求 <<<PAGE 80>>>
- **Star washers**：星形垫圈——防接地连接松动 <<<PAGE 80>>>
- **ISA 12.12.01 / UL 508 / EN50021**：工业安全标准（危险场所/工业控制设备） <<<PAGE 77>>>
- **DNV 2.4**：船级社认证；**EN 50121-4 / IEC 62236-4**：铁路 EMC；**NEMA TS-2**：交通控制；**MIL-STD-810F**：军标冲击 <<<PAGE 77>>>
- **IEC 60529 IPXX**：防护等级标准；**IEC 61850-3 / IEEE 1613**：变电站/电力自动化 EMC <<<PAGE 77>>>
- **Class A / Class 1M Laser / ESD / WEEE / RoHS / Prop 65**：通用法规警告族（住宅禁用/激光/静电/回收/有害物质） <<<PAGE 74>>>/<<<PAGE 79>>>/<<<PAGE 80>>>/<<<PAGE 84>>>

## principles

## 家族与端口架构
- **P1** 家族三机型按安装形态分化：OS6575-P12（"fanless, din-mountable"，8×10/100/1000Base-T 802.3bt 60W + 4×SFP+ Uplink/VFL）；OS6575-U28（"fanless, rack-mountable...1U"，4×PoE+ 90W combo + 20×SFP + 4×SFP+ VFL）；OS6575-MP16（"fanless, wall-mountable"，M12 连接器 16 口）——全部无风扇 <<<PAGE 11>>>
- **P2** MP16 四段端口阵列：1-4 纯 10/100（M12 D-code）、5-8 为 802.3at 30W PoE（D-code）、9-12 为 802.3bt 60W（M12 X-code）、13-16 为带 Bypass 功能的 10/100/1000（X-code）——一口一段功能，速率与 PoE 等级按段固定 <<<PAGE 11>>>/<<<PAGE 25>>>
- **P3** Port Bypass 断电旁路（MP16 独有）："automatically connects two network ports if the device loses power or fails which allows traffic to continue uninterrupted"——单交换机故障不中断关键链路 <<<PAGE 12>>>/<<<PAGE 25>>>
- **P4** Uplink/VFL 双角色口：P12 的 9-12 与 U28 的 29-32 标注"10G SFP+ Uplink / VFL"——上联与 Virtual Fabric Link 堆叠共用；U28 LED 绿=uplink/琥珀=VFL 分色指示 <<<PAGE 11>>>/<<<PAGE 21>>>/<<<PAGE 23>>>/<<<PAGE 28>>>
- **P5** 工业连接器体系（MP16）：Console/USB/Alarm 全部 M12 A-code 公头、Power 为 M23 5-pin、数据口 M12 D-code（10/100）与 X-code（千兆）——全防水加固，非 RJ45 <<<PAGE 25>>>/<<<PAGE 53>>>-<<<PAGE 55>>>
- **P6** M12 X-code PoE pinout 分组：1-4 脚 TXD1/RXD2 带 PoE-(G1)/PoE+(G1)、5-8 脚 BID4/BID3 带 PoE-(G2)/PoE+(G2)——千兆四对线两对组各承载双极性 PoE；D-code PoE 为 1/3 脚 PoE+、2/4 脚 PoE- <<<PAGE 54>>>
- **P8** 包络分化：P12=17×9.1×16.1cm/2.5kg（最小）；MP16=17.5×27×8cm/3.4kg（超薄挂墙）；U28=44×29.5×4.34cm/5.6kg（1U） <<<PAGE 22>>>/<<<PAGE 24>>>/<<<PAGE 26>>>
- **P9** 输入电压域分化：P12=24-57VDC max 8A；U28=24-60VDC max 3.5A；MP16=20-110VDC 超宽压——直流直挂/电池场景全适配 <<<PAGE 22>>>/<<<PAGE 24>>>/<<<PAGE 26>>>
## 电源与输入分档机制
- **P10** U28 输入电压三档 PoE 档位："50 - 57V: (3.5A), 150W max, PoE 802.3AT；44 - 57V: (3.5A), 120W max, PoE 802.3 AF；24 - 60V: (1.5A), Non-PoE, system only"——输入电压决定 PoE 等级与总功率 <<<PAGE 24>>>
- **P11** 48V 禁 PoE 红线（三机型面板注记）："Under 48VDC, PoE not supported."——第三方电源同理"For PoE support 48V or higher is required" <<<PAGE 21>>>/<<<PAGE 23>>>/<<<PAGE 25>>>/<<<PAGE 61>>>
- **P12** 四款电源矩阵：OS6NN5-BPNS（XDR-150E-48）150W 外置 AC（85-260VAC→54.5V，仅 P12）；OS6NN5-BPNSX（XDR-480E-48）480W 外置 AC（85-264VAC→54.5V/8.8A，P12+U28）；OS6575-BPR（PS-I180AC-P）180W 模块 AC（100-240VAC→+56V/3.22A，U28 后装最多 2）；OS6575-BPRD（PS-I180DC-P）180W 模块 DC（-20~-28V/12A 或 -36~-72V/6A→-56V，U28） <<<PAGE 36>>>/<<<PAGE 37>>>/<<<PAGE 38>>>/<<<PAGE 39>>>/<<<PAGE 40>>>
- **P13** 电源手动配置机制："The OmniSwitch 6575 cannot auto-detect the type of power supply connected."——必须 powersupply N name ... type ... 手动声明，否则系统与 PoE 功率信息错乱 <<<PAGE 46>>>
- **P15** 外置电源 ROJ（Removed Outer Jacket）接线制：输入线 L=黑/棕、N=白/蓝、PG=绿/绿黄条纹（30/33mm 剥线）；输出线 V-=红、V+=黑、PG=绿带 ring 端子——注意本机 V- 为红、V+ 为黑（与常规红正黑负相反） <<<PAGE 42>>>/<<<PAGE 43>>>
- **P16** ROJ 输出线接线力矩 3.5 in-lb；输入端子按电源标签力矩；地线用附带螺丝固定到电源并连到交换机电源连接器地端子 <<<PAGE 43>>>/<<<PAGE 44>>>/<<<PAGE 45>>>
- **P17** Pluggable Type A 电源线纪律："please make sure that the power socket is located near the equipment and is easily accessible"——插座须近设备且易达 <<<PAGE 45>>>
- **P18** 电源 DC OK LED 双态制：四款电源统一 Solid Green=DC power is good / Solid Red=There is a DC power issue <<<PAGE 37>>>/<<<PAGE 38>>>/<<<PAGE 39>>>/<<<PAGE 40>>>
- **P19** 双冗余电源同规格强制（三机型注记）："both power supplies must have identical output wattage and identical nominal output voltage. Use of dissimilar power supplies could result in unexpected behavior and is not supported." <<<PAGE 21>>>/<<<PAGE 23>>>/<<<PAGE 25>>>
## LED 与告警机制
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
