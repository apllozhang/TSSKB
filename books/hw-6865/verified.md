# Verified 候选（V1 原文真实性核对 + V2/V3 抽查）

## cases

## 电源托盘与机箱组装
- **C1** 侧装电源托盘两步：①确认四类支架位置正确且"Front Chassis 与 Front Tray 支架"对齐（支架可能出厂预装）②托盘与机箱孔位对齐后用附带螺丝紧固成单一组件 <<<PAGE 13>>>/<<<PAGE 14>>>
- **C2** 后装电源托盘：先拆除出厂预装的侧装支架；将托盘 tab 插入机箱后板槽位，托盘面与后板贴平后插入并拧紧附带的 2 颗 M4（机箱后部预装 4 颗 M4 供侧装用）+ 4 颗 M3X6 螺丝 <<<PAGE 14>>>/<<<PAGE 15>>>
- **C4** 桌面脚安装（提供底部 1/2 RU 间隙）：按机箱/托盘侧面螺纹孔装脚；不同机型用孔位不同（U28X 用 mounting holes 'B' 4 孔 + 4 颗 M4X6；U12X/P16X 用 'C' 4 孔或 'D'4+'E'1 共 5 颗 M4X6）<<<PAGE 16>>>/<<<PAGE 17>>>
## 电源安装
- **C5** 侧装托盘装电源四步：①电源滑入托盘、底部后侧 tab 插入托盘底部槽位 ②对齐并拧紧前面拇指螺丝 ③电源-机箱连接线（DB-15）分别插入电源与机箱后部 DB-15 ④冗余配置在托盘另一侧重复 <<<PAGE 18>>>/<<<PAGE 19>>>
- **C6** 后装托盘装电源：电源按图方向摆放，DB-15 两侧导向销插入机箱后部导向孔，推入至连接器完全就位后拧紧拇指螺丝；冗余在另一侧重复 <<<PAGE 19>>>/<<<PAGE 20>>>
- **C7** 上电纪律：全部电源与电源-机箱电缆安装完毕且交换机就绪后才接电源——"Do not connect to a power source until all power supplies and power supply-to-chassis cables are installed and the switch is ready to boot."（插上电源线即自动上电，无开关）<<<PAGE 19>>>/<<<PAGE 20>>>
## 机架 / 桌面 / DIN / DNV 安装
- **C10** OS6865-REAR-MNT 后固定套件（U28X）四步：装侧导轨 → 装前支架 → 后支架滑入侧导轨 → 固定；孔位分"机箱+后电源托盘"与"仅机箱"两种模式（A/B/C/D 孔组，M4X6 螺丝）<<<PAGE 22>>>/<<<PAGE 23>>>
- **C11** 桌面安装两步：放置前核对全部环境/间隙要求 → 用适合桌面材质的螺栓/螺丝把组件固定到桌面 <<<PAGE 24>>>/<<<PAGE 25>>>
- **C12** DIN 导轨装电源四步：DIN 卡扣用 M4X6 螺丝装到电源 → 卡扣底部钩住 DIN 导轨下沿 → 上推压缩卡扣底部张力弹簧 → 卡扣顶部越过导轨后释放弹簧确认上下均锁定 <<<PAGE 25>>>
- **C15** DIN 导轨拆机箱两步：下拉 strap 释放卡扣底部 → 底部旋离导轨后整体抬起 <<<PAGE 27>>>
- **C16** DNV 全架安装（OS6865-DNV-FRCK 套件）四步：①装侧导轨+后支架+电源托盘（侧导轨 7×M4X8、托盘 4×M4X8、支撑板）②装电源 ③装电源盖 ④总装（盖 4×M3X6、填充板 2×M3X6、滑板 2×M3X6）<<<PAGE 28>>>/<<<PAGE 29>>>/<<<PAGE 30>>>
- **C17** DNV 半架安装（OS6865-DNV-HRCK 套件）六步：①装/对齐前后机箱-托盘支架 ②托盘与机箱紧固 ③装前支架与侧导轨（前支架 4×M4X6 孔'B'）④拇指螺丝装电源（拇指螺丝朝前）⑤装电源盖 ⑥总装 <<<PAGE 31>>>-<<<PAGE 34>>>
## DC 电源接线
- **C19** DC 线束接电源：连接器插入电源接口直至"咔哒"锁紧（表示就位），再拧紧固定螺丝 <<<PAGE 51>>>
- **C20** DC 三线接线五步：①剥线 6-7.5mm（12AWG 三线，先确保未接电源）②小平口螺丝刀插入圆形孔旋松开夹打开地线槽 ③地线推入至触底（约半英寸）④旋紧孔上螺丝夹紧（拉线不应脱出）⑤正/负线重复 ②-④ <<<PAGE 52>>>/<<<PAGE 53>>>
- **C21** DC 线扎纪律：红黑双绞线按图"1.5 圈/25mm、半圈/12.5mm"间距绑扎 <<<PAGE 51>>>
## 首次上电与登录
- **C22** 上电与确认：电源线插入电源前面板再插接地插座（禁延长线）→ 自动上电启动 → 接冗余电源线 → 启动完成前不判断 LED 状态："Be sure the boot process is complete before checking LED status." <<<PAGE 38>>>
- **C23** 首次登录六步清单：console 登录（admin/switch）→ 解锁会话类型 → 改密码 → 设时区 → 设日期时间 → 设可选项并保存 <<<PAGE 39>>>/<<<PAGE 41>>>
- **C24** 解锁会话类型：远程会话（Telnet/FTP/WebView/SNMP）默认锁定；全部解锁 `aaa authentication default local`，单独解锁如 `aaa authentication telnet local` <<<PAGE 39>>>/<<<PAGE 40>>>
- **C25** 改密码四步：以 admin 登录 → `password` 回车 → 输入新密码 → 再输一次确认；密码实时存本地用户库、重启保留，无需额外保存命令 <<<PAGE 40>>>
- **C26** 时间设置：`system timezone` + `system daylight-savings-time`（默认 UTC）；`system time hh:mm:ss` + `system date mm/dd/yyyy` <<<PAGE 40>>>/<<<PAGE 41>>>
- **C27** 可选参数：`system contact`（管理联系人）与 `system name`（系统名，自由文本描述）<<<PAGE 41>>>
## PoE 配置
- **C28** PoE 物理激活：`lanpower slot 2/1 service start`（逐 slot）；端口曾被管理断电后重启用 `lanpower port 1/1/1-16 admin-state enable` <<<PAGE 58>>>
- **C29** 关 PoE：单口 `lanpower port 1/1/12 admin-state disable`；整 slot `lanpower slot 1/1 service stop` <<<PAGE 59>>>
- **C30** Fast PoE 开启：`lanpower slot 1/1 fpoe enable`；Perpetual PoE 开启：`lanpower slot 1/1 ppoe enable` <<<PAGE 59>>>
- **C31** 调口/槽功率上限：`lanpower power`（须带 chassis/slot/port 全三段）；`lanpower slot 1/1 maxpower 150`（slot 上限降为 150W，注意调低可致低优先级口断电）<<<PAGE 59>>>/<<<PAGE 60>>>
- **C32** 设口优先级：`lanpower port 1/1/6 priority critical`（关键任务 PD 专用口）<<<PAGE 61>>>
- **C33** 电容检测开关：`lanpower slot 1/1 capacitor-detection enable`（仅传统 IP 话机兼容用）<<<PAGE 61>>>
- **C34** Priority Disconnect 开关：`lanpower slot 1/1 priority-disconnect disable|enable`（默认启用）<<<PAGE 62>>>
- **C35** Dying Gasp Link OAM 配置三命令：`efm-oam admin-state enable` → `efm-oam port 1/1/23-24 admin-state enable` → `efm-oam port 1/1/23-24 propagate-events dying-gasp enable` <<<PAGE 54>>>
- **C36** PoE 状态查看：`show powersupply`（电源类型/状态）；`show lanpower slot`（PoE 状态与新 PD 可用功率）<<<PAGE 57>>>

## counter-examples

## 环境与气流限制
- **X1** 65°C 气流硬阈值："Switches operating in an environment at or above 65°C require air flow. Switches operating in an environment below 65°C do not require airflow." <<<PAGE 11>>>
- **X2** 74°C 必须封闭机柜/机架："When operating at 74°C ambient temperature the switch must be installed in a suitable closed rack or cabinet enclosure." <<<PAGE 9>>>
- **X3** DNV 盖降额限制：装 DNV 电源盖后温度上限无论有无气流都降到 55°C："With DNV Power Supply Cover (with or without airflow): -40°C to 55°C" <<<PAGE 42>>>/<<<PAGE 45>>>/<<<PAGE 47>>>
- **X4** 桌面放置方向错误风险："be sure that the top of the switch, with the larger heat sinks, is facing out and away from the mounting surface."（大散热片面贴桌面=散热失效）<<<PAGE 11>>>
- **X5** 桌面无脚禁用："Do not attempt to operate the switch on a tabletop surface without these feet properly installed."（桌脚提供底部 1/2 RU 间隙）<<<PAGE 16>>>/<<<PAGE 24>>>
- **X6** 机架底部间隙："be sure that the bottom of the chassis is not in direct contact with any equipment below." <<<PAGE 11>>>
- **X7** 垂直 DIN 安装防火面限制："When mounted vertically, suitable for mounting on concrete or other non-combustible surfaces only (as shown)." <<<PAGE 25>>>/<<<PAGE 27>>>
- **X8** 高温烫手警告："Caution: An operating Omniswitch may be hot to the touch." <<<PAGE 9>>>
## 电气与电源警告
- **X9** 禁用延长线："Each supplied AC power cord is 2 meters (approx. 6.5 feet). Do not use extension cords." <<<PAGE 10>>>/<<<PAGE 38>>>
- **X10** 非 ALE 电源线自证责任："If using a non-ALE provided power cord the installer shall confirm it meets the minimum electrical requirements of the power source." <<<PAGE 10>>>
- **X11** 拆装电源必先断源："Whenever connecting or disconnecting a power supply to/from a chassis, the power supply must be disconnected from the power source." <<<PAGE 17>>>
- **X12** 就绪前禁止上电："Do not connect to a power source until all power supplies and power supply-to-chassis cables are installed and the switch is ready to boot." <<<PAGE 19>>>/<<<PAGE 20>>>
- **X13** DC 接线孔位错插后果："If the wire leads are plugged into the wrong holes, the power supply will not work properly and damage to the unit may result." <<<PAGE 52>>>
- **X14** DC 极性标签陷阱："This rule always applies to both -24V, and -48V input voltages, regardless of the polarity signs shown on the power supply specification labels such as: -48V, +24V, or -24V."（正接正、负接负，勿看标签极性符号反接）<<<PAGE 53>>>
- **X15** DC 长线属本地规范管辖："Installation of a DC cable that is more than 3 meters in length is subject to LOCAL CODES and AUTHORITIES."（>3m 须联系电工与 AHJ）<<<PAGE 51>>>
- **X16** DC 过流保护额定值："The branch circuit overcurrent protection must be rated 15A."；且必须使用两根 12 AWG 铜导体 <<<PAGE 51>>>
- **X17** 电涌违规范即失保："Failure to follow the above recommendations could result in voiding the warranty of the affected ALE product." <<<PAGE 11>>>
- **X18** CDE 静电放电风险："Category 5e, Category 6, and Category 6a cables can store large amounts of static electricity... this build up of electricity could lead to a Cable Discharge Event (CDE)."（接线前先对地放电）<<<PAGE 11>>>
- **X19** 室外裸线禁令："Never install exposed network cables outdoors." <<<PAGE 37>>>
- **X21** 多电源检修断电："Your switch may be equipped with multiple power supplies (redundant power supply configurations). To reduce the risk of electrical shock, be sure to disconnect all power connections before servicing or moving the unit." <<<PAGE 73>>>
- **X22** 运行中勿触电源内部："keep your hands and fingers out of the power supply and do not touch the mother board while the interruptor is functioning."（防触电）<<<PAGE 76>>>
- **X23** EMC 用 DC 地线强制："For EMC/EMI, each DC/DC power supply requires that the ground wire is connected from each DC/DC power supply to Earth Ground." <<<PAGE 74>>>
## PoE 限制
- **X24** lanpower port admin-state 不能首次激活："You cannot use the lanpower port admin-state command to initially activate PoE on a port."（仅用于重新激活被 slot service 断电的口；首次激活必须用 lanpower slot service）<<<PAGE 58>>>
- **X25** 开 Class 检测会复位全部 PoE 口："Enabling class detection will reset all PoE ports." <<<PAGE 58>>>
- **X26** 电容检测不符 IEEE："The capacitive detection method should only be enabled to support legacy IP phones. This feature is not compatible with IEEE specifications." <<<PAGE 61>>>
- **X27** 调低 slot 上限可致断电："Decreasing the slot-wide power could cause lower priority ports to lose power if the new value is less than the total PoE power currently being consumed." <<<PAGE 60>>>
- **X28** MCU 固件升级必断 PD 电："The power to the PD devices will be interrupted if the PoE controller (MCU) firmware itself is being upgraded."（Perpetual PoE 的例外）<<<PAGE 59>>>
- **X29** LLDP PD 在 Fast PoE 下受限："LLDP-based PoE devices will not function as expected until the switch has completed the boot-up process." <<<PAGE 59>>>
- **X30** 双电同源风险："Connect each power supply to a separate independent power source to avoid simultaneous power failures." <<<PAGE 54>>>
- **X31** 高温预算降额：双电源在 65°C/74°C 下 PoE 预算从 300W 腰斩到 150W（P16X/U12X）——高温机房 PoE 规划必须按降额后预算 <<<PAGE 56>>>
## 操作与人身安全警告
- **X32** 双人搬运纪律："Two people are required when lifting the chassis. Due to its weight, lifting the chassis unassisted can cause personal injury."（屈膝直背）<<<PAGE 72>>>
- **X34** 激光辐射警告："Lasers emit invisible radiation from the aperture opening when no fiber-optic cable is connected. When removing cables do not stare into the open apertures."（空口装保护盖）<<<PAGE 72>>>
- **X35** ESD 腕带生效条件："For the grounding wrist strap to be effective in eliminating ESD, the power supplies must be installed in the chassis and plugged into grounded AC outlets." <<<PAGE 75>>>
- **X36** 受限场所要求："This equipment should be installed in a location that restricts access."（仅持钥匙/安防措施的维护人员可进）<<<PAGE 74>>>
- **X37** 锂电池更换纪律："There is a danger of an explosion if the lithium battery is incorrectly replaced. Replace the battery only with the same or equivalent type recommended by the manufacturer."（旧电池须寄回工厂更换）<<<PAGE 76>>>
- **X38** 半双工不支持："Does not support half-duplex connections."（三机型 RJ45 口均同）<<<PAGE 44>>>/<<<PAGE 46>>>/<<<PAGE 48>>>
- **X39** 密码丢失后果严重："Be sure to remember or securely record all new passwords; overriding configured passwords on an OmniSwitch is restricted." <<<PAGE 40>>>
- **X40** 解锁远程会话即开放远程访问："Unlocking session types grants switch access to non-local sessions (e.g., Telnet). As a result, anyone with the correct user login and password will have remote access to the switch." <<<PAGE 40>>>
- **X41** Class A 住宅禁用（多市场）："To avoid electromagnetic interference, this product should not be installed or used in residential environments."（台湾 BSMI 及其他华人市场版警告；另有 CISPR22/VCCI/Korea 同义条款）<<<PAGE 71>>>
- **X42** FCC 擅改设备失权："Changes and modifications made to the equipment without approval of the manufacturer could void the user's authority to operate this equipment."（建议只用屏蔽接地线缆）<<<PAGE 70>>>
- **X43** 接地 lug 规范强制："To ground the equipment properly, connect a Panduit Corporation UL listed Lug, P/N: LCD8-10AL to the two threaded holes located on the rear using 8AWG copper conductors... Torque to between 30-60 inch pounds."（含抗氧化处理要求）<<<PAGE 73>>>
- **X44** 接地线径规定："Use 22AWG solid copper conductor for ground leads connecting the frame to ground and DC return." <<<PAGE 73>>>
- **X45** 墙装强度前提："Be sure that the wall section and wall attachment screws (not provided) have the required strength to easily support the chassis assembly, mounting brackets, and power supplies." <<<PAGE 34>>>

## frameworks

- **F1** 6865 三机型选型矩阵（PoE 密度 vs 上行密度）：
  | 机型 | 形态 | 10G SFP+ | 1G SFP | 75W HPoE/bt 口 | 30W PoE+ 口 | VFL | 定位 |
  |---|---|---|---|---|---|---|---|
  | P16X | 半宽 2RU | 2 | 2 | 4 | 8 | 无 | PoE 供电密集（话机/AP/摄像头） |
  | U12X | 半宽 2RU | 2 | 6 | 4 | 0 | 无 | 光纤上行紧凑型 |
  | U28X | 全宽 1RU | 4 | 20 | 4 | 0 | 2×QSFP+ | 大量光纤上行 + 少量 PoE |
  共性：无风扇、1588v2、双电源（1主1备）、TMRA -40~74°C（有气流）<<<PAGE 42>>>-<<<PAGE 48>>>
- **F2** 加固交换机"环境-电源-PoE 预算"三环校验框架（选型/部署前逐环过）：
  ① 环境环：现场最高温决定气流需求（≥65°C 需气流、74°C 需封闭机柜）与顶部间隙档位（1/2 RU vs 1 RU）；DNV 盖一律按 55°C 降额 <<<PAGE 9>>>/<<<PAGE 11>>>/<<<PAGE 42>>>
  ② 电源环：AC(BP 180W) vs DC(BP-D 140/180W，-24V 输入预算再低 20-40W)；单/双电源；双电必须分电路分源 <<<PAGE 49>>>/<<<PAGE 50>>>/<<<PAGE 56>>>
  ③ PoE 环：预算=电源组合×温度档（60/65/74°C）查表（如双 BP@65°C 仅 150W）；再叠加 Guard Band（口上限 vs 剩余预算）与 Priority Disconnect（优先级+端口号 1 高 28 低）裁决规则 <<<PAGE 56>>>/<<<PAGE 57>>>/<<<PAGE 63>>>
  三环联动的铁律：任何一环升档（更热/更少电源/更大 PD）都要重查另两环。
- **F3** 五种安装形态决策树（6865 特有）：
  机架（默认，侧装托盘；U28X 加 REAR-MNT 后固定套件 / 双托盘用 TRAY-1U）→ 桌面（后装托盘+桌脚，散热片面朝外）→ DIN 导轨（工业柜，电源与机箱可分别上轨，垂直装仅限不可燃表面）→ 墙装（自备螺丝锚入墙柱）→ DNV 船用（FRCK 全架/HRCK 半架套件+电源盖，温度限 55°C）<<<PAGE 13>>>/<<<PAGE 21>>>/<<<PAGE 25>>>/<<<PAGE 28>>>/<<<PAGE 34>>>
- **F4** Dying Gasp 掉电告警部署框架（三通道覆盖）：
  ① SNMP：`snmp station` 配置接收站（仅前 3 个生效，含槽位/电源类型/时间）② Syslog：`swlog output socket` 加服务器（前 3 个，固定文案 "Dying Gasp Power Failure Event Occurred"）③ Link OAM：`efm-oam` + `propagate-events dying-gasp enable`（发 4 个 802.3ah PDU）；资源约束：并发 PDU 口数 = 10 - 已配 SNMP/Syslog 服务器数，上行口优先 <<<PAGE 54>>>/<<<PAGE 55>>>

## glossary

- **OmniSwitch 6865-P16X**：16 口 PoE 加固型，2 SFP+ + 2 SFP + 4×75W HPoE/bt + 8×PoE+，半宽 2RU，待机 30W <<<PAGE 42>>>/<<<PAGE 44>>>
- **OmniSwitch 6865-U12X**：12 口上行型加固交换机，2 SFP+ + 6 SFP + 4 HPoE 口，半宽 2RU，待机 29W <<<PAGE 45>>>/<<<PAGE 46>>>
- **OmniSwitch 6865-U28X**：28 口上行型加固交换机，4 SFP+ + 20 SFP + 4 HPoE + 2 QSFP+ VFL，全宽 1RU，待机 50W <<<PAGE 47>>>/<<<PAGE 48>>>
- **加固型（Hardened）**：面向严苛电气与宽温环境（-40~74°C）设计的交换机品类 <<<PAGE 42>>>
- **TMRA**：最大额定环境温度（Tmra），封闭机架内按此折减 <<<PAGE 9>>>
- **DNV**：挪威船级社（Det Norske Veritas）；DNV 2.4 为船用认证标准，装 DNV 电源盖后温度限 55°C <<<PAGE 42>>>/<<<PAGE 68>>>
- **VFL（QSFP+ VFL Ports）**：U28X 后部 29/30 口的 QSFP+ 虚拟光纤链路端口 <<<PAGE 49>>>
- **1588v2**：IEEE 精密时间同步协议，全 6865 家族支持（电力/工业场景用）<<<PAGE 43>>>
- **半宽 2RU / 全宽 1RU**：P16X/U12X 为 8.5 英寸宽 2RU 机箱；U28X 为 17.2 英寸宽 1RU 机箱 <<<PAGE 42>>>/<<<PAGE 47>>>

## 电源与供电（Ch2）
- **OS6865-BP**：180W 模块化 AC 电源（100-240VAC，+56VDC/3.22A 输出），最多装 2 个 <<<PAGE 49>>>
- **OS6865-BP-D**：180W/140W 模块化 DC 电源（-20~-28V/12A 或 -36~-72V/6A 输入；-56V 输出两档），最多装 2 个 <<<PAGE 50>>>
- **DB-15 连接器（带导向销）**：电源与机箱之间的供电连接接口，后装托盘靠导向销定位 <<<PAGE 19>>>/<<<PAGE 50>>>
- **电源托盘（Power Supply Tray）**：承载 1-2 个外置电源的托架，可侧装（机架用）或后装（桌面用）<<<PAGE 13>>>
- **Dying Gasp**：掉电告别机制——全电源丢失瞬间维持电力发 SNMP trap/Syslog/Link OAM PDU 后关机 <<<PAGE 53>>>
- **SELV**：安全特低电压电路；DC 电源须接可靠接地的 -24V/-48V SELV 源 <<<PAGE 51>>>
- **AHJ（Authority Having Jurisdiction）**：有管辖权的地方电气管理机构；DC 线超 3 米须咨询 <<<PAGE 51>>>
- **DC 回流（DC Return）**：DC 回流导体应接设备机框，各电源共用回流连接 <<<PAGE 51>>>
- **12AWG**：DC 供电线要求的铜导体线规（双导体）；接地引脚线用 22AWG <<<PAGE 51>>>/<<<PAGE 73>>>
- **Panduit LCD8-10AL**：后部接地双螺孔用的 UL 认证接地 lug 型号，配 8AWG 铜导线、扭矩 30-60 in-lb <<<PAGE 73>>>
- **CDE（Cable Discharge Event）**：电缆静电放电事件——Cat5e/6/6a 可蓄静电，接线前先对地放电 <<<PAGE 11>>>
- **UPS**：不间断电源；带 IP 话机的 PoE 交换机交换机与电源均应接 UPS <<<PAGE 56>>>

## PoE（Ch3）
- **PoE 预算（PoE Power Budget）**：按电源数量/类型与环境温度三档查表的可供电总瓦数 <<<PAGE 56>>>/<<<PAGE 57>>>
- **HPoE 口（75W）**：P16X/U12X/U28X 上支持 75W HPoE 或 60W 802.3bt 的 RJ45 口 <<<PAGE 44>>>/<<<PAGE 46>>>/<<<PAGE 48>>>
- **PD（Powered Device）**：受电设备，如 AP、IP 话机、摄像头 <<<PAGE 57>>>
- **PSE**：供电设备（交换机侧），浪涌保护器串接在 PSE 与 PD 之间 <<<PAGE 11>>>
- **Class 检测（Class Detection）**：按 802.3at 电流特征把 PD 分为 Class 0-4 并按类限功率；默认关闭，开启会复位全部 PoE 口 <<<PAGE 57>>>/<<<PAGE 58>>>
- **Fast PoE**：上电数秒即供电（PoE 默认态固化在 FPGA 镜像、配置存控制器 EEPROM），不等 AOS 启动完成 <<<PAGE 59>>>
- **Perpetual PoE**：软重启/重载期间 PD 供电不间断；MCU 固件升级例外 <<<PAGE 59>>>
- **Guard Band**：剩余预算小于端口最大功率或 PD 类最大值时拒载新 PD 的保护带机制 <<<PAGE 63>>>
- **Priority Disconnect**：预算不足时按端口优先级（low/high/critical）+物理端口号（1 最高→28 最低）裁决新 PD 去留；默认启用 <<<PAGE 61>>>/<<<PAGE 62>>>
- **电容检测（Capacitor Detection）**：为老式 IP 话机兼容提供的检测法，不符 IEEE 规范，默认禁用 <<<PAGE 61>>>
- **lanpower slot service**：逐 slot 物理激活/停止 PoE 供电的命令（首次激活唯一途径）<<<PAGE 56>>>/<<<PAGE 58>>>
- **lanpower power / lanpower slot maxpower**：分别设单口/整槽最大功率上限（不做功率预留）<<<PAGE 59>>>/<<<PAGE 60>>>
- **lanpower priority**：设端口优先级（low/high/critical）<<<PAGE 60>>>/<<<PAGE 61>>>
- **lanpower slot fpoe / ppoe**：开启 Fast PoE / Perpetual PoE <<<PAGE 59>>>
- **lanpower slot priority-disconnect**：开关 priority disconnect（默认启用）<<<PAGE 62>>>
- **lanpower capacitor-detection**：开关电容检测 <<<PAGE 61>>>
- **show powersupply / show lanpower slot**：查看电源状态 / PoE 状态与可用功率 <<<PAGE 57>>>

## 链路与告警（Ch2）
- **Link OAM / 802.3ah**：链路层操作管理维护协议；Dying Gasp 经其 PDU 的 Dying Gasp bit 上报 <<<PAGE 54>>>
- **efm-oam propagate-events dying-gasp**：让端口在 Dying Gasp 事件时发 802.3ah PDU 的命令 <<<PAGE 54>>>
- **SNMP trap**：SNMP 告警陷阱；Dying Gasp 发给前 3 个已配 SNMP 站 <<<PAGE 54>>>
- **swlog output socket**：添加 Syslog 服务器（接收 Dying Gasp 消息）的命令 <<<PAGE 54>>>

## 安装部件与套件（Ch1）
- **OS6865-REAR-MNT**：U28X 机架后固定套件（侧导轨+前/后支架）<<<PAGE 21>>>/<<<PAGE 22>>>
- **OS6865-TRAY-1U**：1U 空间并排安装两个电源托盘的机架套件 <<<PAGE 21>>>/<<<PAGE 24>>>
- **OS6865-DIN-MNT**：机箱 DIN 导轨安装套件（平支架+DIN 卡扣）<<<PAGE 26>>>
- **OS6865-DNV-FRCK / HRCK**：DNV 全架/半架安装套件（含 DNV 电源托盘 182343-10、电源盖、填充板、滑板）<<<PAGE 28>>>
- **DIN 导轨（DIN Rail）**：工业控制柜标准安装导轨；电源与机箱可分别安装/拆卸 <<<PAGE 25>>>/<<<PAGE 26>>>
- **张力弹簧卡扣（Tension Spring Clip）**：DIN 卡扣底部弹簧，上推压缩后挂钩/脱钩 <<<PAGE 25>>>
- **桌脚（Table Mount Feet）**：提供桌面安装底部 1/2 RU 间隙的必备脚垫 <<<PAGE 16>>>
- **机架法兰（Rack Mount Flanges）**：机架安装前左右必装的法兰板 <<<PAGE 16>>>
- **DB9-RJ45 连接器**：随箱附带的控制台串口转接头 <<<PAGE 12>>>
- **拇指螺丝（Thumb Screw）**：电源免工具固定螺丝 <<<PAGE 18>>>/<<<PAGE 19>>>

## LED 与管理（Ch1）
- **OK LED**：稳绿=正常运行、闪绿=诊断中、稳琥珀=软件错误 <<<PAGE 38>>>
- **VC LED**：灭=启动中、闪绿=VC Master、闪琥珀=VC Slave；闪烁次数=VC 单元号（每 5 秒停顿）<<<PAGE 38>>>
- **PS1/PS2 LED**：灭=电源不在位、稳绿=正常、稳琥珀=电源故障 <<<PAGE 38>>>
- **端口 LED 颜色语义**：RJ45 绿=非 PoE 链路、琥珀=PoE 链路；SFP 琥珀=100M；闪烁=有活动 <<<PAGE 38>>>
- **aaa authentication**：解锁会话类型（console/telnet/ftp/http/snmp/ssh）的命令族 <<<PAGE 39>>>
- **admin/switch**：出厂默认管理员登录名/密码 <<<PAGE 39>>>
- **system timezone / system time / system date**：时区（默认 UTC）/时间/日期设置命令 <<<PAGE 40>>>/<<<PAGE 41>>>
- **system contact / system name**：管理联系人/系统名可选参数命令 <<<PAGE 41>>>

## 标准与合规（附录 A）
- **IEEE 802.3 / 802.3af / 802.3at**：PoE 支持的标准栈（含 Hi-Pot 2250VDC 测试）<<<PAGE 56>>>/<<<PAGE 67>>>
- **ISA 12.12.01 (UL 1604)**：危险场所工业安全标准 <<<PAGE 67>>>
- **IEC 61850-3 / IEEE 1613**：变电站/电力环境 EMC 标准 <<<PAGE 67>>>
- **EN 50121-4 / IEC 62236-4**：铁路应用 EMC 标准 <<<PAGE 68>>>
- **NEMA TS-2**：交通控制设备标准 <<<PAGE 68>>>
- **UL 62368-1 / IEC 62368-1**：音视频与信息技术设备安全标准 <<<PAGE 65>>>
- **FCC Part 15 Class A**：商用环境电磁干扰限值（住宅环境可能干扰，需自费整改）<<<PAGE 70>>>
- **Prop 65**：加州 65 号提案警告（铅化合物致癌/生殖危害）<<<PAGE 69>>>
- **WEEE**：欧盟废弃电子电气设备指令（分类回收标志）<<<PAGE 70>>>
- **RoHS（中国/台湾）**：有害物质限制表 <<<PAGE 68>>>/<<<PAGE 69>>>
- **ESD 腕带（Wrist Strap）**：防静电腕带，接机箱右上接地 lug；电源须装好并接接地插座才有效 <<<PAGE 75>>>
- **受限场所（Restricted Access Location）**：仅持钥匙/安防措施的维护人员可进入的安装位置 <<<PAGE 74>>>

## principles

## 定位与家族架构
- **P1** 加固型定位：6865 系列为面向严苛电气与宽温环境的 GigE/10G 交换机："The Alcatel-Lucent Enterprise OmniSwitch 6865 series are Gigabit Ethernet (GigE) and 10 Gb Ethernet (GigE) switches designed for demanding electrical and severe temperature environments." <<<PAGE 42>>>
- **P2** 三机型分工：P16X=16 口 PoE 型（4×75W HPoE/bt + 8×PoE+ + 2 SFP+ + 2 SFP）；U12X=12 口上行型（2 SFP+ + 6 SFP + 4 HPoE）；U28X=28 口全宽上行型（4 SFP+ + 20 SFP + 4 HPoE + 2 QSFP+ VFL）<<<PAGE 44>>>/<<<PAGE 46>>>/<<<PAGE 48>>>
- **P3** 全家族无风扇：三机型 Fans 均为 None，散热完全依赖机箱散热片与外部气流 <<<PAGE 42>>>/<<<PAGE 45>>>/<<<PAGE 47>>>
- **P4** 机箱形态两档：P16X/U12X 为半宽 2RU（8.5" 宽、10.24" 深）；U28X 为全宽 1RU（17.2" 宽、10.6" 深）<<<PAGE 42>>>/<<<PAGE 47>>>
- **P5** 电源拓扑为"外置托盘 + DB-15 电缆"：1 主 + 1 备共 2 电源，装在侧装/后装托盘上经 DB-15 连接线接到机箱，非内置槽位 <<<PAGE 42>>>/<<<PAGE 19>>>
- **P6** 前面板统一维护接口：Console(RJ45) + USB Type A（仅维护用，可下代码/存配置）位于最左 <<<PAGE 44>>>/<<<PAGE 46>>>/<<<PAGE 48>>>
- **P8** 待机功耗阶梯：P16X=30W、U12X=29W、U28X=50W <<<PAGE 43>>>/<<<PAGE 46>>>/<<<PAGE 48>>>
## 温度与气流机制（加固型核心）
- **P9** TMRA 三档温度包络：有气流 -40~74°C；无气流 -40~65°C；装 DNV 电源盖后无论有无气流均降为 -40~55°C <<<PAGE 42>>>/<<<PAGE 45>>>/<<<PAGE 47>>>
- **P11** 74°C 必须封闭机柜："When operating at 74°C ambient temperature the switch must be installed in a suitable closed rack or cabinet enclosure." <<<PAGE 9>>>
- **P12** 存储温度上限 85°C、湿度 5%-95% 无凝结、海拔 4000m，三机型一致 <<<PAGE 43>>>/<<<PAGE 45>>>/<<<PAGE 47>>>
- **P13** 顶部间隙温度分档：机架安装顶部 <65°C 留 0.875"(1/2 RU)、≥65°C 留 1.75"(1 RU)；桌面安装顶/底各 0.875"（靠桌脚保证）；侧 2"、前/后 6" <<<PAGE 11>>>/<<<PAGE 12>>>
- **P14** 桌面安装方向军规：大散热片面朝外、远离安装面："be sure that the top of the switch, with the larger heat sinks, is facing out and away from the mounting surface." <<<PAGE 11>>>
## 电源与 Dying Gasp 机制
- **P15** 双电源型号：OS6865-BP（AC 100-240V，输出 +56VDC/3.22A=180W）与 OS6865-BP-D（DC 输入 -20~-28V/12A 或 -36~-72V/6A，输出 -56V 140W/180W 两档）<<<PAGE 49>>>/<<<PAGE 50>>>
- **P16** 无总开关设计："The switch does not provide an on/off switch. Instead, the switch powers on when a power cord is plugged into the power supply's front panel and plugged into a power source." <<<PAGE 19>>>/<<<PAGE 20>>>
- **P17** Dying Gasp 机制：全电源丢失时交换机维持电力足够发出告别消息再关机："If the switch loses all power it will maintain power long enough to send a Dying Gasp message before completely shutting down. An SNMP trap, Syslog message and Link OAM PDUs will be generated." <<<PAGE 53>>>
- **P18** Dying Gasp 触发场景三则：仅主电失败（单电源）；主后备先后失败；后备主先后失败；规避法="Connect each power supply to a separate independent power source to avoid simultaneous power failures." <<<PAGE 54>>>
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
- **P35** Guard Band 不作用已在电 PD：预算缩减（如拔电源）场景改由 priority disconnect 裁决 <<<PAGE 64>>>
## 安装与安全机制
- **P36** 电涌防护军规（同 6360 五条）：全设备等电位接地（接地电阻 ≤0.01Ω）；室外/近交流线路用 STP Cat5e+；室外铜口必须串接浪涌保护器；防室外设备传浪涌电流给上游；Cat5e/6/6a 线可蓄静电须先对地放电防 CDE；违者可致失保："Failure to follow the above recommendations could result in voiding the warranty." <<<PAGE 10>>>/<<<PAGE 11>>>
- **P37** 电源托盘双形态：侧装托盘配机架应用、后装托盘配桌面应用——"Side mounted tray assemblies are typically used for rack mount applications; rear mounted tray assemblies are typically used for table mount applications." <<<PAGE 13>>>
- **P38** LED 语义体系：OK（稳绿=正常/闪绿=诊断中/稳琥珀=软件错误）；VC（灭=启动中/闪绿=VC Master/闪琥珀=VC Slave，闪烁次数=单元号，每 5 秒停顿）；PS1/PS2（灭=不在位/稳绿=正常/稳琥珀=电源故障）<<<PAGE 38>>>
- **P39** 端口 LED 用颜色区分 PoE：RJ45 口绿=非 PoE 链路、琥珀=PoE 设备已接（闪烁=有活动）；SFP/SFP+ 口琥珀=100M 链路 <<<PAGE 38>>>
- **P40** 接地规范：后部两螺孔接 Panduit LCD8-10AL lug、8AWG 铜导线、压接用 CT-940CH、扭矩 30-60 in-lb <<<PAGE 73>>>
