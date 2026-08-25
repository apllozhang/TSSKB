# Verified 候选（V1 原文真实性核对 + V2/V3 抽查）

## cases

## 上架前准备
- **C1** 安装前工具清单：接地腕带、Phillips 螺丝刀、平口螺丝刀；VC 配置另行参考 Switch Management Guide <<<PAGE 17>>>
- **C2** 站点准备流程：核对机箱规格表温湿度范围→预留前 6"/后 6"/侧 2" 气流间隙→确认每电源一个接地插座、电源线 2m 内可达且不接延长线 <<<PAGE 17>>>/<<<PAGE 19>>>
- **C3** 开箱清点流程：机箱（含电源）、按订单光模块、盲板、机架托架、国别电源线、橡胶桌脚、螺钉附件；就近开箱减少搬运 <<<PAGE 18>>>/<<<PAGE 19>>>
## 上电与首次登录
- **C5** 首次登录六步流程：console 连接→admin/switch 登录→`aaa authentication default local`（或逐类 telnet/http/ftp）解锁会话→`password` 改密（输两遍，实时保存）→`system timezone`/`system time`/`system date` 设时间→`system contact`/`system name`/`system location` 设可选信息→`show system` 核对→`write memory` 保存 <<<PAGE 21>>>-<<<PAGE 24>>>
## 机箱安装
- **C6** 机架安装流程（全宽 24/48 口）：双人作业→一人抬机对准机架孔位→第二人先穿每侧法兰底部螺丝并拧紧→再上顶部螺丝全部紧固；重设备放机架下部防头重脚轻；机架螺丝用机架厂商的（ALE 不提供）<<<PAGE 48>>>/<<<PAGE 50>>>/<<<PAGE 51>>>
- **C7** 机架法兰安装流程：弹簧夹拨到 out（脱开）位→tab 插入机箱槽→按压法兰至"CLICK"锁入 in 位→附赠螺丝固定→对侧重复 <<<PAGE 49>>>/<<<PAGE 50>>>
- **C8** 桌面独立安装流程：4 个橡胶脚垫插入底板孔→正放于稳固平面（禁止顶面/侧面朝上运行）→接网络与管理线缆<<<PAGE 51>>>
- **C9** 半宽机型机架安装流程（OS6360-RM-19-L L 支架套件）：长短托架可左右互换装于机箱前部两侧→法兰孔对机架孔→先下孔后上孔穿螺丝紧固；部分套件需先拆出厂螺丝 <<<PAGE 52>>>/<<<PAGE 53>>>
- **C10** 壁挂安装流程（仅 10/P10，OS6360-WALL-MNT）：两侧前部装朝下托架→后部再装两个朝下托架→双人定位并在墙上标记孔位→预钻孔→用承重达标的紧固件固定（穿通软墙面入墙 stud）；建议机箱侧立、面板朝侧 <<<PAGE 54>>>/<<<PAGE 55>>>
- **C11** 盲板安装流程：电源槽位盲板箭头朝上→插入空槽→附赠螺丝固定；空槽任何时候都应盖盲板 <<<PAGE 48>>>
## 接地与监控
- **C12** 机箱 supplemental 接地流程：后板 lug 无漆区装 Panduit LCD8-10A-L 接地耳→8AWG 铜导线→扭矩 30-60 in-lb<<<PAGE 55>>>
- **C13** 硬件状态巡检流程：`show module`/`show module long` 看槽位→`show temperature` 看各传感器 Current/Range/Danger/Thresh/Status（UNDER THRESHOLD 为正常）→超 Warning 阈值查气流与室温，超 Danger 关机处理后手动重启 <<<PAGE 55>>>-<<<PAGE 57>>>
## PoE 配置流程
- **C14** PoE 首次激活流程：`show powersupply` 确认电源 UP→`lanpower slot 2/1 service start` 启动 slot 供电→`show lanpower slot 1/1` 核对端口 Maximum/Actual/Status/Priority/Class 与预算余量 <<<PAGE 60>>>/<<<PAGE 61>>>/<<<PAGE 62>>>
- **C15** PoE 关断两级操作：单口 `lanpower port 1/1/12 admin-state disable`；整槽 `lanpower slot 1/1 service stop`；admin-state enable 仅用于复活被 service 命令断电的口 <<<PAGE 62>>>/<<<PAGE 63>>>
- **C16** 端口功率限额调整案例：`lanpower port 1/1/24 power 3000` 把 24 口上限压到 3000mW——既可给高耗 PD 放量也可省预算 <<<PAGE 63>>>
- **C17** 槽级预算调整案例：`lanpower slot 3/1 maxpower 400` 把 3/1 槽上限设 400W；下调若低于当前总耗，低优先级口立即失电 <<<PAGE 64>>>
- **C18** 端口优先级配置案例：`lanpower port 1/1/6 priority critical` 把 6 口设为最高级，留给关键 PD；断电顺序 low→high→critical <<<PAGE 64>>>
- **C19** Class 检测启用流程：`lanpower slot class-detection`（默认关）开启严格按类限功率——注意会复位全机 PoE 口 <<<PAGE 61>>>/<<<PAGE 62>>>
- **C20** 802.3bt/4pair 使能流程：`lanpower 4pair` 开 4 对 60/75/95W（PoH）；`lanpower 8023bt` 开 bt 类型（Class 5-8）<<<PAGE 62>>>
- **C21** 电容检测启用（legacy 话机专用）：`lanpower slot 3/1 capacitor-detection enable`；仅兼容老 IP 话机，不符 IEEE，需向销售/支持确认型号 <<<PAGE 65>>>
- **C22** Guard Band 拒载处置案例：余 50W、新 PD 只需 4W 但口上限 75W 被拒载→`lanpower power 1/1/1 power 10000` 把口上限降到 10W→PD 放行 <<<PAGE 65>>>/<<<PAGE 66>>>
- **C23** Priority Disconnect 开关流程：默认启用；`lanpower slot 2/1 priority-disconnect disable` 关闭（此后新 PD 一律拒载）、`... enable` 恢复 <<<PAGE 66>>>/<<<PAGE 67>>>
- **C24** PoE 运行监控流程：`show lanpower 1` 输出逐口 Maximum/Actual Used/Status/Priority/On/Off/Class + 槽上限/预算已用/余量/电源数；尾部 `*` 号表示 4pair 口正跑在 2pair 模式 <<<PAGE 61>>>/<<<PAGE 68>>>/<<<PAGE 69>>>

---
合计：24 条（C1-C24）。

## counter-examples

## 机型与功能限制
- **X1** 特定 PN 不支持 Fast/Perpetual PoE："The OmniSwitch 6360-P10 model (904324-90), orderable part number OS6360-P10A-US, does not support Fast or Perpetual PoE. The overlay remains as OS6360-P10 but this model is differentiated from other OS6360-10 models by part number 904324-90."——面板丝印相同，只能靠 PN 区分 <<<PAGE 28>>>/<<<PAGE 63>>>
- **X2** 无实时时钟，重启时间不准："The OS6360 does not contain a real-time clock. It is recommended to use NTP for time synchronization."（断电重启后时间停在关机时刻）<<<PAGE 23>>>
- **X3** Danger 温度阈值用户不可改："The Danger threshold is factory-set and cannot be configured by the user." <<<PAGE 57>>>
- **X4** 电容检测不符 IEEE，仅限 legacy 话机："The capacitive detection method should only be enabled to support legacy IP phones. This feature is not compatible with IEEE specifications." <<<PAGE 65>>>
- **X5** admin-state 不能用于首次激活 PoE："You cannot use the lanpower port admin-state command to initially activate PoE on a port."（必须先用 lanpower slot service）<<<PAGE 62>>>
- **X6** Class 检测开启会全槽复位："Enabling class detection will reset all PoE ports on the chassis." <<<PAGE 62>>>
- **X7** Fast PoE 的 LLDP 盲区："LLDP-based PoE devices will not function as expected until the switch has completed the boot-up process."；且 PoE 配置在软件完全初始化前不可修改 <<<PAGE 63>>>
- **X8** Perpetual PoE 也有断电场景："The power to the PD devices will be interrupted if the PoE controller (MCU) firmware itself is being upgraded." <<<PAGE 63>>>
- **X9** aaa authentication 一次只能解锁一类会话："You cannot specify more than one session type in a single command line." <<<PAGE 22>>>
- **X10** 密码覆盖受限："overriding configured passwords on an OmniSwitch is restricted."——密码丢失无法直接绕过 <<<PAGE 22>>>
## 安装与环境警告
- **X11** 禁用延长线："Do not use extension cords."；非 ALE 电源线须自行确认满足电源最低电气要求 <<<PAGE 17>>>
- **X12** 网线室外禁令："Never install exposed network cables outdoors. Install network cables per manufacturer requirements." <<<PAGE 20>>>/<<<PAGE 77>>>
- **X13** 雷暴作业禁令："To avoid a shock hazard, do not connect or disconnect any cables or perform installation, maintenance, or reconfiguration of this product during an electrical storm." <<<PAGE 78>>>
- **X14** 盲板必须常装："Because they regulate airflow and help protect internal chassis components, blank cover plates should remain installed at empty module slots and power supply bays at all times." <<<PAGE 77>>>
- **X15** 气流遮挡可致整机故障："Restricted airflow can cause your switch to overheat, which can lead to switch failure."（Never obstruct chassis air vents）<<<PAGE 19>>>/<<<PAGE 46>>>
- **X16** 桌面摆放姿势限制："Never attempt to operate a switch while it is placed on its top or side." <<<PAGE 51>>>
- **X17** 壁挂紧固件自备且须承重达标："Wall fasteners are not provided with your switch... Be sure to use fasteners that are approved for the full weight of the chassis assembly."；电源线不得用 U 形卡/线扣固定于建筑面或穿墙 <<<PAGE 54>>>/<<<PAGE 55>>>
- **X18** 违反电涌防护建议可能失保："Failure to follow the above recommendations could result in voiding the warranty of the affected ALE product."（CDE/接地五条军规）<<<PAGE 18>>>
## 电气与激光安全
- **X19** ESD 腕带强制："Because electrostatic discharge (ESD) can damage switch components, you must follow proper procedures to eliminate ESD from your person and the surrounding area before handling switch components."（腕带生效前提：电源已装入并接接地 AC 插座）<<<PAGE 81>>>/<<<PAGE 83>>>
- **X20** 激光辐射勿直视："CLASS 1M LASER RADIATION WHEN OPEN. DO NOT VIEW DIRECTLY WITH OPTICAL INSTRUMENTS."；未接光纤时拔线勿盯孔位并装保护盖 <<<PAGE 77>>>/<<<PAGE 78>>>
- **X21** 运行中勿触背板/电源舱："keep your hands and fingers out of power supply bays and do not touch the backplane while the switch is operating."；维护搬运前断开所有电源连接 <<<PAGE 78>>>/<<<PAGE 79>>>
- **X22** 接地红线：电源线必须接正确接地的插座，所连设备同样；DC/DC 电源地线必须接大地（EMC/EMI）<<<PAGE 80>>>
- **X23** 锂电池更换风险："Hay un peligro de la explosión si la batería del litio en su chasis se substituye incorrectamente."（错误更换锂电池有爆炸危险，须原厂同型号并返厂更换）<<<PAGE 82>>>
## 使用场所限制
- **X24** Class A 数字设备不得用于住宅："Operation of this equipment in a residential area is likely to cause interference"；台湾/中文市场明确"本產品不應安裝或使用於住宅環境" <<<PAGE 75>>>/<<<PAGE 77>>>
- **X25** 受限访问场所："This equipment should be installed in a location restricts access... limited to service personnel who have a special key"；仅专业电气/机械人员可安装维护 <<<PAGE 81>>>/<<<PAGE 78>>>

---
合计：25 条（X1-X25）。

## frameworks

- **F1** 6360 家族选型三轴矩阵：轴一=下行口数（10/24/48）；轴二=PoE 能力（无 → P=802.3at → PX=2×多千兆 bt 口+950W 电源）；轴三=上行升级（X/H 后缀 combo 口可软件升 10G）。运算法则：先定口数，再按 PD 总功率选 PoE 预算档（120/180/350/380/760W 与内置电源 wattage 一一对应），最后按上联带宽决定是否要 X/H（10G 升级）；10 口机型独享半宽机箱+壁挂能力。 <<<PAGE 13>>>/<<<PAGE 60>>>
- **F2** PoE 供电三环体系：外环=预算（slot maxpower/port power 上限 + Guard Band 拒载：余量 < 口上限即拒新 PD）；中环=优先级（low/high/critical 三级 + 物理端口号 1 高 48 低作为同级裁决）；内环=保护动作（Priority Disconnect：新 PD 高级→断低级口；同级→端口号大者让路；新 PD 低级→被拒；禁用→一律拒新）。排障思路：新 PD 不供电先查 service 是否 start，再查 Guard Band（降口上限放行），再查优先级裁决。 <<<PAGE 62>>>-<<<PAGE 68>>>
- **F3** 硬件健康监控三层框架：物理层=面板 LED（OK/VC/PWR 三系统灯 + 端口灯颜色分 PoE/VFL）；传感层=自动监控（温度超 Warning 发 trap 不停机、超 Danger 自动关机且不可配）；CLI 层=用户驱动（show module/show temperature/show powersupply/show lanpower 四板斧）。 <<<PAGE 15>>>/<<<PAGE 45>>>/<<<PAGE 55>>>-<<<PAGE 57>>>

---
合计：3 条（F1-F3）。

## glossary

- **OS6360-10**：10 口非 PoE 半宽 1U（10×RJ45+2×SFP，30W 内置电源，无风扇）<<<PAGE 13>>>
- **OS6360-P10**：8 口 802.3at PoE + 2 口非 PoE + 2×SFP，165W 内置电源，PoE 预算 120W，无风扇 <<<PAGE 13>>>/<<<PAGE 28>>>
- **OS6360-P10A-US**：PN 904324-90 的 P10 变体，不支持 Fast/Perpetual PoE（丝印相同靠 PN 区分）<<<PAGE 28>>>
- **OS6360-24**：24×RJ45 非 PoE + 2 combo + 2×SFP+，65W 内置电源，无风扇 <<<PAGE 13>>>/<<<PAGE 30>>>
- **OS6360-P24**：24 口 802.3at PoE 机型，260W 电源，PoE 预算 180W，无风扇 <<<PAGE 13>>>/<<<PAGE 32>>>
- **OS6360-P24X**：24 口 at + 2×SFP+ combo，550W 电源，PoE 预算 380W，带风扇 <<<PAGE 14>>>/<<<PAGE 34>>>
- **OS6360-PH24**：P24X 同级但 combo 口可软件升级 10G（"Upgradeable to 10G"），550W 电源/380W 预算 <<<PAGE 14>>>/<<<PAGE 36>>>
- **OS6360-48**：48×RJ45 非 PoE + 2 combo + 2×SFP+，120W 内置电源 <<<PAGE 14>>>/<<<PAGE 38>>>
- **OS6360-P48**：48 口 802.3at PoE，550W 电源，PoE 预算 350W <<<PAGE 14>>>/<<<PAGE 40>>>
- **OS6360-P48X**：46 口 at + 2 口多千兆 802.3bt（2.5G）+ 10G combo，950W 电源，PoE 预算 760W <<<PAGE 14>>>/<<<PAGE 42>>>
- **OS6360-PH48**：P48X 同级且 combo 口可升级 10G，950W 电源/760W 预算 <<<PAGE 15>>>/<<<PAGE 44>>>

## 端口与面板（Ch3）
- **Combo 口**：RJ45 与 SFP/SFP+ 共享的上联口对（25-26/49-50），两种介质二选一 <<<PAGE 30>>>
- **VFL 口**：SFP+ 软件可配口的第二角色（Virtual Fabric Link），端口 LED 琥珀色指示 <<<PAGE 13>>>/<<<PAGE 46>>>
- **SFP+ software configurable ports**：可在 1G SFP 上行与 10G SFP+/VFL 之间软件切换的上联口 <<<PAGE 13>>>
- **Chassis Grounding Lug**：后面板接地耳，配 Panduit LCD8-10A-L、8AWG 铜线、30-60 in-lb 扭矩 <<<PAGE 55>>>
- **Tmra（Maximum Rated Ambient Temperature）**：最大额定环境温度（全家族 0-45°C），机架内需按温升折减 <<<PAGE 27>>>/<<<PAGE 46>>>
- **Chassis vs Ambient Temperature**：机箱温度=内置传感器读数（阈值判断用），环境温度≈室温，前者通常更高 <<<PAGE 27>>>
- **OK LED**：绿=诊断与 AOS 启动 OK；闪绿=进行中；琥珀=系统/风扇/温度故障 <<<PAGE 45>>>
- **VC LED**：闪绿=VC Master、闪琥珀=Slave，闪烁次数即节点 ID；灭=关机或非 VC 成员 <<<PAGE 45>>>
- **PWR LED**：绿=12V 主电正常；稳琥珀=12V 故障；闪琥珀=54V/PoE 故障；灭=电源不在位 <<<PAGE 45>>>

## 安装部件与套件（Ch3）
- **Blank Cover Panel**：空槽盲板，箭头朝上安装；调节气流并保护内部元件，须常装 <<<PAGE 47>>>/<<<PAGE 48>>>
- **Rack Mount Flange**：免工具卡扣式机架法兰（弹簧夹 out/in 位 + "CLICK" 锁定 + 螺丝固定）<<<PAGE 49>>>
- **OS6360-RM-19-L**：半宽机型 19" 机架 L 支架套件 <<<PAGE 52>>>
- **OS6360-WALL-MNT**：10/P10 壁挂套件（四托架朝下，紧固件自备）<<<PAGE 53>>>/<<<PAGE 54>>>
- **Rubber feet**：桌面安装用四只橡胶脚垫（包装内附）<<<PAGE 51>>>
- **Relay Rack**：中继机架，需按机架厂商规范安装固定 <<<PAGE 49>>>/<<<PAGE 52>>>

## PoE 体系（Ch4）
- **PoE（Power over Ethernet）**：通过以太网口在线供电，PoL/Inline Power 为同义词 <<<PAGE 58>>>
- **PD（Powered Device）**：受电设备（IP 话机/AP/摄像头等），以太网缆为唯一电源 <<<PAGE 58>>>
- **PSE（Power Source Equipment）**：供电设备，负责检测 PD、分级、按需供电与回收 <<<PAGE 58>>>
- **PoE Budget**：整机 PoE 功率预算，按机型 120-760W <<<PAGE 60>>>
- **PoE Class Detection**：PD 分级检测（Class 0-8：15.4/4.0/7.0/15.4/30/45/60/75/90-99W），默认关闭，开启会复位全部 PoE 口 <<<PAGE 61>>>/<<<PAGE 62>>>
- **802.3bt**：bt 标准（Class 5-8，双 Type），`lanpower 8023bt` 使能 <<<PAGE 62>>>
- **4pair（PoH）**：4 对供电模式，支持 60/75/95W 每口，`lanpower 4pair` 使能 <<<PAGE 62>>>
- **Fast PoE**：上电数秒即供电（PoE 默认态固化于 FPGA、配置存控制器 EEPROM），不等 AOS 启动完成 <<<PAGE 63>>>
- **Perpetual PoE**：软重启/重载期间 PD 供电不间断（MCU 固件升级除外）<<<PAGE 63>>>
- **Guard Band**：保护带拒载机制——剩余预算低于端口上限或 PD 类最大值即拒绝新 PD <<<PAGE 65>>>
- **Priority Disconnect**：预算不足时按端口优先级+物理端口号裁决新 PD 供电资格的机制（默认启用）<<<PAGE 66>>>
- **Port Priority**：端口优先级 low（默认）/high/critical 三级 <<<PAGE 64>>>
- **Capacitor Detection**：电容检测法，仅供 legacy IP 话机、不符 IEEE，默认禁用 <<<PAGE 65>>>
- **2pair 模式标记**：show lanpower 输出端口 maxpower 后缀 `*` 表示 4pair 口运行在 2pair 模式 <<<PAGE 61>>>

## CLI 命令（Ch2-Ch4）
- **show module / show module long**：查看槽位基本/详细信息 <<<PAGE 55>>>/<<<PAGE 56>>>
- **show temperature**：查看温度传感器 Current/Range/Danger/Thresh/Status <<<PAGE 56>>>
- **show powersupply**：查看电源类型与状态（Total Power/Type/Status/Location）<<<PAGE 60>>>
- **show lanpower slot**：查看逐口 PoE 状态与槽预算 <<<PAGE 61>>>/<<<PAGE 68>>>
- **lanpower slot service**：slot 级 PoE 启停（start/stop），首次激活必用 <<<PAGE 62>>>
- **lanpower port admin-state**：端口级 PoE 使能/禁用（仅复活已断电口，不能首次激活）<<<PAGE 62>>>
- **lanpower port power**：设置端口最大功率（mW）<<<PAGE 63>>>
- **lanpower slot maxpower**：设置槽级最大功率（W）<<<PAGE 64>>>
- **lanpower port priority**：设置端口优先级（low/high/critical）<<<PAGE 64>>>
- **lanpower slot priority-disconnect**：启用/禁用优先级断电 <<<PAGE 66>>>
- **lanpower slot class-detection**：启用分级检测（复位全 PoE 口）<<<PAGE 62>>>
- **aaa authentication**：解锁会话类型（default local 全解；telnet/http/ftp 单类）<<<PAGE 22>>>
- **write memory**：保存配置 <<<PAGE 24>>>
- **system timezone / system time / system date**：时区/DST、时间、日期设置 <<<PAGE 23>>>
- **system contact / system name / system location**：管理联系人/系统名/位置 <<<PAGE 23>>>
- **show system**：查看当前系统配置改动 <<<PAGE 24>>>

## 安全与法规（附录 A）
- **CDE（Cable Discharge Event）**：线缆静电放电事件，Cat5e/6/6a 布线接端口前应先对地放电 <<<PAGE 18>>>
- **ESD / Wrist Strap**：静电放电与防静电腕带（触件前必须消除人身与周围静电）<<<PAGE 81>>>
- **Class 1M Laser**：开盖时 1M 类激光辐射，勿用光学仪器直视 <<<PAGE 77>>>
- **Restricted Access Location**：受限访问场所（钥匙/安保限服务人员进入）<<<PAGE 81>>>
- **WEEE**：欧盟废弃电子电气设备指令，产品报废需单独回收处理 <<<PAGE 70>>>
- **RoHS**：有害物质限制（中/台罗表）<<<PAGE 71>>>/<<<PAGE 72>>>
- **California Proposition 65**：加州 65 号提案铅暴露警告 <<<PAGE 73>>>
- **Hi-Pot Test**：耐压测试（所有以太网口 2250V DC）<<<PAGE 75>>>
- **Class A 数字设备**：FCC/VCCI/BSMI Class A，仅限商业环境，住宅使用可能产生干扰 <<<PAGE 75>>>/<<<PAGE 77>>>

## 通用概念（Ch1-Ch2）
- **Hot-Swapping**：不断电增删更换部件的能力 <<<PAGE 15>>>
- **Hardware Monitoring**：内置传感器自动监控 + LED 视觉状态 + 用户 show 命令三层 <<<PAGE 15>>>/<<<PAGE 16>>>
- **Trap**：超阈值等错误事件自动发送并打印到控制台的消息 <<<PAGE 15>>>/<<<PAGE 56>>>
- **Warning / Danger Threshold**：温度警告阈值（发 trap 不停机）/危险阈值（自动关机、不可配）<<<PAGE 56>>>/<<<PAGE 57>>>
- **UPS**：不间断电源，PoE+IP 话机场景强制建议（911 要求）<<<PAGE 58>>>
- **STP/UTP**：屏蔽/非屏蔽双绞线；室外或近交流线路建议 STP Cat5e+ <<<PAGE 18>>>

---
合计：约 62 条。

## principles

## 家族与端口架构
- **P1** 家族命名解码：10 个 1U 固定配置机型按"口数 + PoE 前缀 + 上行特性"展开——`-10/-24/-48` 非 PoE；`P*`=802.3at PoE；`P*X`=2 个多千兆 802.3bt 口（47-48）+ 950W 电源；`PH*`=combo 口可软件升级 10G（"Upgradeable to 10G"）<<<PAGE 13>>>/<<<PAGE 14>>>/<<<PAGE 15>>>
- **P2** 上行口三段式结构：全家族统一为"2× RJ45/SFP(combo) + 2× SFP+ 软件可配口"，SFP+ 口可在"1G SFP 上行"与"10G SFP+ 上行或 VFL"两种角色间切换："2 x SFP+ software configurable ports: a) 2 x SFP uplinks b) 2 x SFP+ uplink or VFL ports." <<<PAGE 13>>>
- **P4** 无风扇设计分级：OS6360-10/P10/24/P24/48 为 Fan less（无风扇）；P24X/PH24/P48X/PH48（大功率 PoE 机型）带风扇 <<<PAGE 13>>>/<<<PAGE 14>>>
- **P5** 电源全部内置不可热换：单一 Internal AC Power Supply，wattage 随 PoE 能力递增——30W(-10)/65W(-24)/120W(-48)/165W(P10)/260W(P24)/550W(P24X·PH24·P48)/950W(P48X·PH48) <<<PAGE 26>>>/<<<PAGE 30>>>/<<<PAGE 32>>>/<<<PAGE 34>>>/<<<PAGE 36>>>/<<<PAGE 38>>>/<<<PAGE 40>>>/<<<PAGE 42>>>/<<<PAGE 44>>>
## 可用性特性
- **P6** 三大可用性支柱：Hot-Swapping（不断电增删部件）、Hardware Monitoring（内置传感器自动监控，超阈值立即发 trap 到控制台）、LED 视觉状态；另加用户主动 `show` 命令监控："If an error is detected (e.g., over-threshold temperature), the switch immediately sends a trap to the user." <<<PAGE 15>>>/<<<PAGE 16>>>
- **P7** 全家族统一环境包络：工作温度 0-45°C（Tmra）、存储 -40~70°C、湿度 5%-95% 无凝结、电压 100-240V 50-60Hz <<<PAGE 27>>>/<<<PAGE 29>>>等
- **P8** chassis 与 ambient 温度语义区分："Chassis temperature refers to the sensor reading of the internal switch temperature (threshold or danger). Ambient temperature refers to the approximate room temperature."（机箱温度恒高于室温）<<<PAGE 27>>>等
- **P9** 待机功耗阶梯：-10/P10=13W、-24/P24=21W、P24X/PH24=34W、-48=46W、P48=47W、P48X/PH48=60W——PoE 预算核算要叠加 <<<PAGE 27>>>-<<<PAGE 45>>>
- **P10** 气流间隙三向要求：前面 6 in、后面 6 in、左右各 2 in，顶底免间隙："No clearance is necessary at the top or bottom of the chassis." <<<PAGE 19>>>/<<<PAGE 20>>>
- **P11** 电涌防护五条军规：①全链路等电位接地（接地电阻 ≤0.01Ω）；②室外/近交流线路用 STP Cat5e 以上；③室外铜口必须串接浪涌保护器；④防止室外设备把浪涌电流传给上游交换机；⑤ Cat5e/6/6a 线缆可蓄静电，接线前先对地放电防 CDE："It is recommended that installers momentarily ground all copper Ethernet cables (especially in new cable runs) to a suitable and safe earth ground before connecting them to the port." <<<PAGE 18>>>
- **P12** 电源线纪律：每电源一个接地插座；ALE 电源线 2m 长、UL 认证（IEC 62368-1），禁止延长线："Do not use extension cords." <<<PAGE 17>>>
## 面板与 LED 机制
- **P13** 三颗系统 LED 语义：OK（绿=诊断/启动正常，闪绿=进行中，琥珀=系统/风扇/温度故障）；VC（闪绿=Master，闪琥珀=Slave，闪烁次数即 VC ID，灭=关机或不在 VC 中）；PWR（绿=12V 主电正常，稳琥珀=12V 故障，闪琥珀=54V/PoE 故障，灭=无电源）<<<PAGE 45>>>
- **P14** 端口 LED 用颜色区分 PoE 状态：RJ45 口绿=非 PoE 链路（闪=有活动），琥珀=PoE 链路（闪=有活动）；SFP 口绿=上行、琥珀=VFL 角色 <<<PAGE 46>>>
- **P15** 前面板 Class 1M 激光警示固定出现于每机型："CAUTION - CLASS 1 M LASER RADIATION WHEN OPEN. DO NOT VIEW DIRECTLY WITH OPTICAL INSTRUMENTS" <<<PAGE 26>>>等
- **P16** 后面板标准两件套：机箱接地 lug + 内置电源连接器（部分机型顺序互换）<<<PAGE 26>>>/<<<PAGE 38>>>
## 安装机制
- **P17** 机架安装五大考量（IEC 机架纪律）：Elevated Operating Ambient（封闭机架内温度高于室温，按 Tmra 折减）、Reduced Air Flow、Mechanical Loading（防不均衡载荷）、Circuit Overloading（防过流）、Reliable Earthing（经电源排接入时尤须注意接地可靠性）<<<PAGE 46>>>
- **P18** 盲板气流机制：空槽位不装盲板会迫使气流改道、加重电源风扇负担并暴露内部敏感元件："If your switch is not fully populated and blank cover panels are not installed over empty slot locations, airflow is adversely affected." <<<PAGE 47>>>/<<<PAGE 48>>>
- **P19** 机架法兰免工具卡扣：弹簧夹置 out 位→插 tab 入槽→按压至"CLICK"入 in 位→附赠螺丝固定，两侧对称安装 <<<PAGE 49>>>/<<<PAGE 50>>>
- **P21** 机箱接地规范：后板 lug 用 Panduit LCD8-10A-L、8AWG 铜导线、扭矩 30-60 in-lb，作为电源线接地的补充（paint-free 区域保证金属接触）<<<PAGE 55>>>
- **P22** 双人搬运纪律贯穿全书：机架安装、壁挂安装均明确"Two people are required"<<<PAGE 48>>>/<<<PAGE 54>>>
## 监控与温度机制
- **P23** 温度双阈值机制：Warning 阈值超限→发 trap 但业务继续（应立即查气流/室温）；Danger 阈值超限→交换机自动关机，需人工处理后再手动启动，且 Danger 阈值出厂固化不可配置："The Danger threshold is factory-set and cannot be configured by the user." <<<PAGE 56>>>/<<<PAGE 57>>>
- **P24** 硬件监控三板斧命令：`show module`（槽位基本信息）、`show module long`（详情）、`show temperature`（温度/Range/Danger/Thresh/Status 五列）<<<PAGE 55>>>/<<<PAGE 56>>>
## PoE 机制
- **P25** PoE 标准栈：802.3/802.3af/802.3at/802.3bt；每口功率范围 at 口 3000-30000mW、bt 口 3000-95000mW；Class 检测支持（Class 0-8 功率 15.4-99W 梯度表）<<<PAGE 59>>>/<<<PAGE 61>>>
- **P26** PoE 预算-机型对应表：P10=120W、P24=180W、P24X/PH24=380W、P48=350W、P48X/PH48=760W <<<PAGE 60>>>
- **P27** PoE 激活两级模型：软件层默认 administratively enabled，但物理供电子系统必须逐 slot 用 `lanpower slot service` 启动后 PD 才真正得电："you must issue the lanpower slot service command on a slot-by-slot basis before any connected PDs will receive inline power." <<<PAGE 62>>>
- **P28** 4pair/bt 使能链：`lanpower 4pair` 开 60/75/95W（802.3at 4 对 + PoH）；`lanpower 8023bt` 开 bt 双 Type 四 Class（5-8 类：45/60/75/90-99W）<<<PAGE 62>>>
- **P29** Class 检测默认关：不开启也供电（按预算），严格按类限功率需 `lanpower slot class-detection` 显式开启，且开启会复位全机 PoE 口："Enabling class detection will reset all PoE ports on the chassis." <<<PAGE 61>>>/<<<PAGE 62>>>
- **P30** Fast PoE 机制：PoE 子系统默认态固化进 FPGA 镜像、PoE 配置存于控制器 EEPROM，上电数秒即可供电而不等 AOS 启动完成；依赖正确 FPGA/CPLD 版本；LLDP 协商的 PD 仍要等启动完成 <<<PAGE 63>>>
- **P31** Perpetual PoE 机制：软重启/重载期间对 PD 供电不间断；同样依赖 FPGA/CPLD；但 PoE 控制器（MCU）固件自身升级时供电必断："The power to the PD devices will be interrupted if the PoE controller (MCU) firmware itself is being upgraded." <<<PAGE 63>>>
- **P32** 端口/槽最大功率语义：`lanpower port power`/`lanpower slot maxpower` 只设上限不做预留——"Changing the maximum power available to a slot or port does not reserve or immediately allocate that power."（未用功率仍回到总预算池）<<<PAGE 64>>>
- **P33** 三级端口优先级：low（默认，先断）/high（次保）/critical（尽量保），`lanpower port priority` 逐口设置 <<<PAGE 64>>>
- **P34** Guard Band 拒载机制：新 PD 上线时若剩余预算 < 端口最大功率或 PD 类最大值，则拒绝供电——即使该 PD 实际只需 4W（例：余 50W、口上限 75W→拒载；把口上限调成 10W 即可放行）<<<PAGE 65>>>/<<<PAGE 66>>>
- **P35** Priority Disconnect 裁决规则（预算不足时新 PD 去留）：①禁用→一律拒绝新 PD；②启用+同级→按物理端口号（1 最高，48 最低）裁决；③启用+新 PD 优先级最高→新 PD 必得电，系统先断最低优先级口、同级再断端口号最大的口；④启用+新 PD 优先级最低→拒绝新 PD <<<PAGE 66>>>/<<<PAGE 67>>>/<<<PAGE 68>>>
- **P36** 911/UPS 供电纪律：带 IP 话机的 PoE 交换机应始终保持电源冗余并接 UPS："operational power supply redundancy at all times for 911 emergency requirements." <<<PAGE 58>>>
## 首次登录机制
- **P37** 首次登录六步闭环：console 登录（admin/switch）→解锁会话类型→改密→设时区/时间→可选参数（contact/name/location）→`write memory` 保存 <<<PAGE 21>>>
- **P38** 会话解锁安全模型：出厂仅 console 可用，Telnet/FTP/WebView/SNMP 全锁死，需 `aaa authentication` 逐类解锁（一次命令只能解锁一类）："All other session types (Telnet, FTP, WebView, and SNMP) are locked out until they are manually unlocked by the user." <<<PAGE 22>>>
- **P39** 密码实时落盘：新密码即时写入本地用户库并重启保持，无需额外保存命令；覆盖已配置密码受限 <<<PAGE 22>>>/<<<PAGE 23>>>
- **P40** 控制台固定参数：9600 波特、无校验、8 数据位、1 停止位，DCE 连接 <<<PAGE 20>>>

---
合计：40 条（P1-P40）。
