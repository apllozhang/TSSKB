# Verified 候选（V1 原文真实性核对 + V2/V3 抽查）

## cases

## 机箱安装
- **C2** 独立安装流程：稳固平面承满配重量（32.83/64.36kg 起）；两人以上搬运空机箱正位放置；保证气流间隙与 AC 插座可达 <<<PAGE 36>>>
- **C3** 满载机箱搬运禁令+空箱组装策略："Do not attempt to move or install a fully loaded chassis."——先就位空机箱再逐件装模块 <<<PAGE 32>>>
## 组件安装
- **C4** 装 CFM 六步：①确认遮挡槽位的风扇托盘已拆 ②模块电路板元件面朝左，板边插入上下 card guides 并部分推入 ③到中板连接器时上下锁杆保持 open 推到停 ④同时压上下锁杆至竖直（locked）位使模块紧固中板 ⑤手紧上下 captive 螺丝 ⑥重复装其他 CFM 后回装风扇托盘 <<<PAGE 36>>>-<<<PAGE 38>>>
- **C5** 装风扇托盘三步：①手持上下把手、底部朝外斜角把顶部两 tab 插入槽位顶部 ②推底部入槽至 firmly seated ③手紧底部拇指螺丝 <<<PAGE 39>>>-<<<PAGE 41>>>
- **C6** 装 NI 模块三步：①电路板板边插入机箱左右两侧凹槽 ②锁杆 open 位推模块至背板连接器 ③向面板中心拉紧锁杆至 90 度全闭锁固，手紧左右拇指螺丝 <<<PAGE 42>>>
- **C7** 装电源四步：①拆电源槽盲板留存 ②一手扶前面、一手托底承重，手柄 down（open）位后滑至背板 ③手柄上翻竖直（locked）位锁定并拧紧拇指螺丝 ④插电源线并接易触及接地插座（禁延长线）<<<PAGE 43>>>/<<<PAGE 44>>>
## 上电与首次登录
- **C8** 上电流程：全部电源线插入接地插座自动开机；多电源数秒内相继插电保证启动全程供电；启动完成前不判 LED 状态 <<<PAGE 45>>>
- **C9** 启动成功判据（主 CMM LED）：PRI 稳绿 + PS 稳绿 + FAB 稳绿 + TEMP 稳绿；LED 持续报错则联系客服 <<<PAGE 45>>>
- **C10** 首次登录七步：console 登录（admin/switch，RJ45 或 Micro-USB）→ 设 EMP IP → 解锁会话类型 → 改密码 → 设时区 → 设日期时间 → 设可选项并 `write memory` <<<PAGE 45>>>/<<<PAGE 46>>>
- **C11** EMP 设 IP：console 先行 → `ip interface emp address 168.22.2.120 mask 255.255.255.0` → `show ip interface` 验证；默认 192.168.1.1/24；未解锁会话类型前 EMP 不能远程访问 <<<PAGE 46>>>/<<<PAGE 47>>>
- **C12** 解锁会话：全部 `aaa authentication default local`；单个如 `aaa authentication telnet local`（console/telnet/ftp/http/snmp/ssh）<<<PAGE 47>>>
- **C13** 改密码与可选项：`password` 两输入；`system timezone`/`system time`/`system date`；`system contact`/`system name`/`system location`；`show system` 查看；`write memory` 保存 <<<PAGE 47>>>-<<<PAGE 49>>>
## 机箱功率预算管理
- **C14** 变更前查预算：加 NI/冗余 CMM/PoE 设备或拔电源前 `show chassis` 看 Power Left（示例输出 2041W 可用于新组件与 PD）；功率不足时新组件可能不上电并引发电源错误中断数据流 <<<PAGE 49>>>
## PoE 配置
- **C15** PoE 物理激活：`lanpower slot 2/1 service start`（逐 slot 首次激活唯一途径）；被断电口重激活 `lanpower port 2/1/1-24 admin-state enable` <<<PAGE 52>>>
- **C16** 关 PoE：单口 `lanpower port 1/1/12 admin-state disable`；整 slot `lanpower slot 1/1 service stop` <<<PAGE 52>>>/<<<PAGE 53>>>
- **C17** 调口/槽上限：`lanpower power`（须全三段 chassis/slot/port）；`lanpower slot 3/1 maxpower 400`（slot 降 400W，可致低优先级口断电）<<<PAGE 53>>>
- **C18** 设口优先级：`lanpower port 1/1/6 priority critical`（关键任务 PD 专用口）<<<PAGE 54>>>
- **C19** 电容检测：`lanpower slot 3/1 capacitor-detection enable`（仅传统 IP 话机）<<<PAGE 54>>>
- **C20** Priority Disconnect 开关：`lanpower slot 2/1 priority-disconnect disable|enable`（默认启用）<<<PAGE 55>>>
- **C21** 定时供电规则：`lanpower power-rule` 可按日期/时间开关 PoE（详见 CLI Reference）<<<PAGE 53>>>
- **C22** 状态查看：`show powersupply`（逐槽 Total/Used/Voltage/Type/Status）；`show lanpower slot 1/4`（逐口最大功率/实际用量/状态/优先级/Class/Type + slot 预算与已分配 PoE 总量）<<<PAGE 50>>>/<<<PAGE 51>>>
## 组件拆除
- **C23** 拆电源四步：①电源线从电源源与电源面板双端拔出，松前面拇指螺丝 ②手柄下拉至水平（open）位 ③一手握手柄部分拉出、另一手托底承重取出 ④空槽装盲板；不托底会导致电源壳尾部坠落损坏设备 <<<PAGE 57>>>/<<<PAGE 58>>>
- **C24** 拆风扇托盘三步：①松拇指螺丝 ②持上下把手拉出下把手使底部脱开，再向外向下拉出直至脱离顶部 tab ③"Three fan trays are required at all times. For switches currently operating, complete any maintenance and reinstall the fan tray as quickly as possible." <<<PAGE 58>>>/<<<PAGE 59>>>
- **C25** 拆 CFM：先拆遮挡的风扇托盘 → 松模块上下拇指螺丝、锁杆外拉释放 → 持前面板/锁杆滑出，全程托承模块重量防坠落 <<<PAGE 59>>>-<<<PAGE 61>>>
- **C26** 拆 NI 模块：松左右拇指螺丝、锁杆向外压释放 → 持前面板/锁杆滑出并托承重量 <<<PAGE 62>>>
- **C27** NI 热换完整流程：断模块全部网线 → 拔全部光模块 → 等 30 秒 → 插同类替代模块（"can only be hot swapped with like modules"）→ 回插光模块 → 重接网线；随后按提示操作 <<<PAGE 63>>>

## counter-examples

## 组合与兼容硬约束（机箱级重点）
- **X1** CMM 与 CMM2 不可混插："the OS99-CMM2 requires a minimum AOS version of 8.10R2 and cannot be mixed with the existing OS99-CMM in the same chassis." <<<PAGE 17>>>
- **X2** CFM2 版本与混插限制："The OS9907-CFM2 requires a minimum AOS version of 8.9R1 and cannot be mixed with the existing OS9907-CFM in the same chassis." <<<PAGE 20>>>
- **X3** 组合矩阵三禁：CMM+CMM 配 CFM+CFM2 混插=Not Supported；CMM2+CMM2 配 CFM+CFM=Not Supported；CMM+CMM2 混插=Not Supported <<<PAGE 22>>>
- **X4** VC-of-2 组合限制：双机箱仅三种对等组合支持（CMM+CFM、CMM+CFM2、CMM2+CFM2 各自对称），"All other combination Not Supported" <<<PAGE 22>>>
- **X5** 9912 不支持四种 NI：XNI-P48Z16 / XNI-P24Z8 / XNI-UP24Q2 / XNI-U12Q 均注明 "Not supported in an OS9912 chassis." <<<PAGE 24>>>/<<<PAGE 25>>>/<<<PAGE 26>>>
- **X6** slot2 NI 只活 8 口（9907）："When an XNI module (i.e. OS99-XNI-U48) is inserted in slot 2 only the first 8 ports will be active." <<<PAGE 7>>>
- **X7** slot2 装 NI 即失 CMM 冗余："when an NI is installed in slot 2, CMM redundancy is not provided." <<<PAGE 16>>>/<<<PAGE 17>>>
- **X8** CFM3/4 预留未激活："Slots CFM 3 and CFM 4 are currently inactive and are reserved for future use."（不可当可用槽规划）<<<PAGE 5>>>/<<<PAGE 10>>>/<<<PAGE 15>>>
## 电源限制
- **X9** AC/DC 电源不可混："Mixing of AC and DC power supplies is not supported."（与 6900/6870 的"AC+DC 可混"相反）<<<PAGE 29>>>/<<<PAGE 63>>>
- **X10** 高低压输入不可混："Mixing of Hi (240VAC) and Low (110VAC) input is not supported." <<<PAGE 29>>>/<<<PAGE 63>>>
- **X11** 单件不可热拆："Hot swapping CMMs, CFMs, or power supplies is supported ONLY if more than one of these components is installed. If only one CMM, CFM or power supply is installed and any of these components is removed, switch functions will be disrupted until a replacement is installed." <<<PAGE 63>>>
- **X12** 拆装电源先断源："Whenever connecting or disconnecting a power supply to/from a chassis, the power supply must first be disconnected from the power source." <<<PAGE 43>>>/<<<PAGE 57>>>
- **X13** DC 过流与线规："The branch circuit overcurrent protection must be rated 75A. Use two 10 AWG copper conductors."；且必须装在受限进入场所 <<<PAGE 30>>>
- **X14** DC 长线属本地规范："Installation of a DC cable that is more than 3 meters in length is subject to LOCAL CODES and AUTHORITIES." <<<PAGE 31>>>
- **X15** DC 专用连接器："The power supply shall used with an 4P PWRBLADE CONNECTOR, FCI model 10080598-2ED0006LF." <<<PAGE 31>>>
- **X16** 禁用延长线："each supplied AC power cord is 2 meters (approx. 6.5 feet). Do not use extension cords." <<<PAGE 33>>>/<<<PAGE 44>>>
- **X17** 多电源快速上电："be sure to plug in each power supply in rapid succession, (i.e., within a few seconds of each other)." <<<PAGE 45>>>
- **X18** 功率预算不足后果："If there is not adequate power, the incoming component may not power on. Additional power errors may also occur, which can interrupt data flow on the switch."（加件/拔电前必查 show chassis Power Left）<<<PAGE 49>>>
## 风扇与热插拔限制
- **X19** 三风扇托盘常驻："Three fan trays are required at all times; removal of a fan tray is allowed for fan tray or CFM field replacement only." <<<PAGE 28>>>/<<<PAGE 59>>>
- **X20** CFM 热换 120 秒限时："CFM hot swap should be completed within 120 seconds." 且一次只换一个、风扇全在位 <<<PAGE 63>>>
- **X21** 拆插间隔纪律："All component removals must have a 30 second interval before initiating another hot swap activity. All component insertions must have a five minute interval AND an LED state indicating that no errors have occurred." <<<PAGE 63>>>
- **X22** NI 只能同类热换："Network Interface (NI) modules can only be hot swapped with like modules."；换前须断网线拔光模块等 30 秒 <<<PAGE 63>>>
- **X23** 拆电源不托底后果："Failure to support the chassis as it is being removed may cause the rear of the power supply casing to fall from the slot, resulting in damage to the equipment." <<<PAGE 58>>>
## 安装与环境限制
- **X24** 墙装禁令："Due to weight and airflow requirements, OS9900 switches cannot be wall mounted." <<<PAGE 36>>>
- **X25** 满载机箱搬运禁令："Do not attempt to move or install a fully loaded chassis. To avoid injury and/or damage to the product, two or more people are required when lifting." <<<PAGE 32>>>
- **X26** 双人/三人搬运纪律："Two people are required when lifting the chassis... bend your knees and keep your back straight."；机架安装"Use two additional people" <<<PAGE 36>>>/<<<PAGE 69>>>
- **X27** 倒放/侧躺禁令："The chassis must be placed 'right side up.' Never attempt to operate a switch while it is lying on its side or back." <<<PAGE 36>>>
- **X28** 盲板必须常装："Because they regulate airflow and help protect internal chassis components, blank cover panels should be installed over empty module slots and power supply bays at all times." <<<PAGE 35>>>
- **X29** 气流阻塞后果："Restricted airflow can cause the switch to overheat, which can lead to system failure and damage to the product." / "Never obstruct chassis or component air vents." <<<PAGE 34>>>
- **X30** 专业安装者要求："Alcatel-Lucent Enterprise products must be installed by a professional installer." <<<PAGE 32>>>
- **X31** 电涌违规范即失保 + CDE 风险："Failure to follow the above recommendations could result in voiding the warranty of the affected ALE product."；Cat5e/6/6a 可蓄静电致 Cable Discharge Event <<<PAGE 33>>>/<<<PAGE 34>>>
- **X32** 室外裸线禁令："Never install exposed network cables outdoors." <<<PAGE 44>>>
## PoE 限制
- **X33** lanpower port admin-state 不能首次激活："You cannot use the lanpower port admin-state command to initially activate PoE on a port."（首次必须 lanpower slot service）<<<PAGE 52>>>
- **X34** 开 Class 检测复位全部 PoE 口："Enabling class detection will reset all PoE ports." <<<PAGE 52>>>
- **X36** 调低 slot 上限可致断电："Decreasing the slot-wide power could cause lower priority ports to lose power if the new value is less than the total PoE power currently being consumed." <<<PAGE 53>>>
- **X37** PoE 默认 operational disabled："Default PoE operational status: Disabled (PoE must be activated via the lanpower start command.)"——装好即供电的预期会落空 <<<PAGE 50>>>
- **X38** 端口优先方向反转陷阱：本平台 "48 (Highest) -> 1 (Lowest)"（与 6865/6870 相反），跨平台套用优先级规划会反噬 <<<PAGE 55>>>
## 操作与人身安全
- **X40** 运行中勿触电源内部："keep your hands and fingers out of the power supply and do not touch the mother board while the switch is functioning."（西语版）<<<PAGE 73>>>
- **X41** 雷暴作业禁令："To avoid a shock hazard, do not connect or disconnect any cables or perform installation, maintenance, or reconfiguration of this product during an electrical storm." <<<PAGE 69>>>
- **X42** 不可见激光辐射："Lasers emit invisible radiation from the aperture opening when no fiber-optic cable is connected. When removing cables do not stare into the open apertures."（空口装保护盖；面板另有 CLASS 1 LASER PRODUCT 标识）<<<PAGE 70>>>
- **X43** ESD 腕带生效条件："For the grounding wrist strap to be effective in eliminating ESD, the power supplies must be installed in the chassis and plugged into grounded AC outlets." <<<PAGE 72>>>
- **X44** 受限场所要求："This equipment should be installed in a location that restricts access." <<<PAGE 71>>>
- **X45** 锂电池更换纪律："There is a danger of an explosion if the lithium battery in your chassis is incorrectly replaced."（只能同型/等效，寄回工厂换）<<<PAGE 73>>>
- **X46** 密码丢失后果："Be sure to remember or securely record all new passwords; overriding configured passwords on an OmniSwitch is restricted." <<<PAGE 48>>>
- **X47** 解锁远程会话即开放远程访问："Unlocking session types grants access to non-local sessions (e.g., Telnet). As a result, anyone with the correct user login and password will have remote access to the switch." <<<PAGE 47>>>
- **X48** EMP 远程访问前置：配好 EMP IP 后 "The switch cannot be accessed through this port (i.e. TELNET, FTP, HTTP, SSH or SNMP) until these remote session types have been unlocked." <<<PAGE 47>>>
- **X49** Class A 住宅禁用："To avoid electromagnetic interference, this product should not be installed or used in residential environments."（台湾 BSMI 版；另有 FCC/CISPR22/VCCI/Korea 同义条款）<<<PAGE 68>>>
- **X50** FCC 擅改失权："Changes and modifications made to the equipment without approval of the manufacturer could void the user's authority to operate this equipment." <<<PAGE 67>>>
- **X51** 接地 lug 规范强制："connect a Panduit Corporation UL listed Lug, P/N: LCD8-10AL to the two threaded holes located on the rear using 8AWG copper conductors. Use Panduit Corporation, P/N: CT-940CH for crimping. Torque to between 30-60 inch pounds."（接地引线 22AWG、安装时清洁打磨接地点并涂抗氧化剂）<<<PAGE 70>>>/<<<PAGE 71>>>

## frameworks

- **F1** 9907 vs 9912 机箱选型矩阵：
  | 维度 | OS9907 | OS9912 |
  |---|---|---|
  | 高度 | 11RU | 17RU |
  | 总槽位 | 7（2 CMM + 5 NI） | 12（2 CMM + 10 NI） |
  | slot2 双角色 | CMM 或 NI（NI 仅 8 口活、失 CMM 冗余） | 仅 CMM |
  | 风扇托盘 | 3×（每托 3 扇） | 3×（每托 5 扇） |
  | 重量 | 32.83kg | 64.36kg |
  | CFM 带宽/块 | 2.56T（CFM）/12.8T（CFM2） | 25.6T |
  | 9912 不支持 NI | — | P48Z16/P24Z8/UP24Q2/U12Q |
  | VC-of-2 | 支持（三组合） | — |
  共性：4 电源槽 N+1、CFM3/4 预留、仅前→后气流、23" 深 <<<PAGE 5>>>/<<<PAGE 6>>>/<<<PAGE 11>>>/<<<PAGE 22>>>/<<<PAGE 24>>>-<<<PAGE 26>>>
- **F2** CMM/CFM 兼容组合决策表（升级与采购防错）：
  支持的三种同箱组合：①CMM+CMM / CFM+CFM（旧体系）②CMM+CMM / CFM2+CFM2（CFM2 需 AOS≥8.9R1）③CMM2+CMM2 / CFM2+CFM2（CMM2 需 AOS≥8.10R2）；禁止：任何新旧混插。VC-of-2 双机箱只允许两箱对称（CMM+CFM↔CMM+CFM 等）。升级路径只有整代切换：先备份数据→确认 AOS 版本→整箱换 CMM2+CFM2 <<<PAGE 17>>>/<<<PAGE 20>>>/<<<PAGE 22>>>
- **F3** 机箱功率预算三步法（变更前必走）：
  ① 查现状：`show chassis` 看 Power Left（可用瓦数）② 算增量：新增组件功耗（CMM 64/74W、CFM 119W、NI 56-402W、风扇 112/200W、PoE PD 预算）+ PoE 模块 slot 默认 1800W ③ 执行纪律：组件插入中板即生效功率需求，不足则不上电甚至中断数据流；单电源不可热拔，四电源 N+1 负载分担；拆件间隔 30s、插件间隔 5 分钟+LED 无错 <<<PAGE 23>>>-<<<PAGE 26>>>/<<<PAGE 29>>>/<<<PAGE 49>>>/<<<PAGE 63>>>
- **F4** 组件安装/拆除标准作业序列（满载机箱从头搭建）：
  空机箱就位（三人）→ 装 CFM（先拆风扇托盘→锁杆三步→装回风扇）→ 装 NI 模块（锁杆 90 度闭锁）→ 装 CMM → `show chassis` 核功率余量 → 装电源（手柄 down 入位→up 锁定→数秒内相继插电）→ 判主 CMM 四绿（PRI/PS/FAB/TEMP）→ console 9600-8N1 首次登录七步；拆除逆序且各守纪律（电源托底、风扇托盘速装回、CFM≤120s、NI 同类替换）<<<PAGE 36>>>-<<<PAGE 45>>>/<<<PAGE 57>>>-<<<PAGE 63>>>

## glossary

- **OS9907**：11RU 模块化机箱，7 槽（2 CMM+5 NI），32.83kg，23 英寸深 <<<PAGE 5>>>/<<<PAGE 6>>>
- **OS9912**：17RU 模块化机箱，12 槽（2 CMM+10 NI），64.36kg <<<PAGE 11>>>
- **CMM（Chassis Management Module）**：机箱管理模块，管控 NI/CFM/配电；2 槽 1+1 冗余 <<<PAGE 16>>>
- **CFM（Chassis Fabric Module）**：机箱交换矩阵模块，藏于风扇托盘之后、经中板连接；4 槽中 CFM1/2 可用 <<<PAGE 10>>>/<<<PAGE 20>>>
- **中板（Mid-plane）**：CFM 与机箱连接的背中板结构（NI 走 backplane）<<<PAGE 20>>>
- **NI（Network Interface）模块**：网络接口模块，装前面板槽位（9907 有 3-7、9912 有 3-12）<<<PAGE 7>>>/<<<PAGE 13>>>
- **VC-of-2**：两台 OS9907 机箱虚拟化为一台虚拟机箱的配置 <<<PAGE 22>>>
- **N+1 冗余**：4 电源负载分担/3 风扇托盘冗余设计 <<<PAGE 8>>>/<<<PAGE 28>>>
- **铝头拇指螺丝**：模块固定螺丝新形态，替代紫色塑料头，机械性能相同 <<<PAGE 6>>>/<<<PAGE 12>>>
- **Wrist Strap Grounding Connector**：机箱前/后部 ESD 腕带接地点 <<<PAGE 8>>>/<<<PAGE 9>>>

## CMM 与 CFM（Ch1）
- **OS99-CMM**：初代管理模块，2×40G QSFP+ 上行，功耗 64W，仅 9907 支持 <<<PAGE 16>>>
- **OS99-CMM2**：新一代管理模块，4×100G QSFP28 上行/VFL，74W，需 AOS ≥8.10R2，不可与 CMM 混插 <<<PAGE 17>>>
- **Micro-USB console**：CMM 上的第二 console 口，需安装驱动 <<<PAGE 16>>>/<<<PAGE 17>>>
- **OS9907-CFM / CFM2**：9907 交换矩阵（2.56T / 12.8T 每块，119W；CFM2 需 AOS ≥8.9R1）<<<PAGE 20>>>
- **OS9912-CFM**：9912 交换矩阵（25.6T 每块，222W）<<<PAGE 21>>>
- **PRI LED**：CMM 主备状态灯（稳绿=主/闪绿=备/稳黄=停运/闪黄=升级中）<<<PAGE 18>>>
- **FAB LED**：CFM 状态灯（稳绿=正常/稳黄=降级运行/闪黄=CFM 电源或 PCIe 上报失败）<<<PAGE 18>>>
- **五灯同闪（PCIe link failure）**：PRI/VC/FAB/PS/TEMP 同时闪黄=全部 CFM PCIe 硬链路失效 <<<PAGE 18>>>

## NI 模块（Ch1）
- **OS99-XNI-48**：48 口 1/10GBaseT 模块，402W <<<PAGE 23>>>
- **OS99-XNI-U48**：48 口 1/10G SFP+ 模块，305W（slot2 只活 8 口）<<<PAGE 23>>>/<<<PAGE 7>>>
- **OS99-GNI-48**：48 口 10/100/1000BaseT + 2×10G，56W <<<PAGE 23>>>
- **OS99-GNI-P48**：48 口千兆 PoE 模块（前 8 口 HPoE 75W），54W（不含 PD）<<<PAGE 24>>>
- **OS99-GNI-U48**：48 口 1G SFP 模块，70W <<<PAGE 24>>>
- **OS99-XNI-P48Z16**：32 口 1/10G at PoE + 16 口多千兆 at PoE（前 8 口 HPoE），402W；不支持 9912 <<<PAGE 24>>>
- **OS99-XNI-P24Z8**：16+8 口 PoE 组合模块，187W；不支持 9912 <<<PAGE 25>>>
- **OS99-XNI-U24**：24 口 1/10G SFP+ 模块，153W <<<PAGE 25>>>
- **OS99-CNI-U8**：8 口 10/25/40/100G QSFP28 模块，117W <<<PAGE 25>>>
- **OS99-CNI-U20**：20 口 100G QSFP28 模块（13-20 口支持 splitter），314W <<<PAGE 26>>>
- **OS99-XNI-UP24Q2**：12×SFP+ +12×多千兆 HPoE(75W) +2×QSFP+，117W；不支持 9912 <<<PAGE 26>>>
- **OS99-XNI-U12Q**：12×SFP+ +1×QSFP+，117W；不支持 9912 <<<PAGE 26>>>
- **HPoE 口**：PoE 模块前 8 口、面板有 "HPoE" 标注、支持 75W <<<PAGE 24>>>
- **Speed LED（NI）**：模块最大端口速率指示灯 + HW/SW 心跳状态（稳绿=HW OK/闪绿=SW 心跳/稳黄=SW 故障）<<<PAGE 27>>>

## 电源与风扇（Ch1/Ch2/Ch4）
- **OS99-PS-A**：AC 电源（100-240V；输出 1200W/21.4A 或 3000W/53.5A 两档），热插拔，System+PoE <<<PAGE 29>>>
- **OS99-PS-D**：DC 电源（-40~-72VDC/75A；输出 2500W/44.6A@56V），热插拔 <<<PAGE 30>>>
- **分路保护额定值**：每电源建议 30A（AC）/110A（DC）断路器 <<<PAGE 29>>>
- **FCI 10080598-2ED0006LF**：DC 电源要求的 4P PWRBLADE 专用连接器 <<<PAGE 31>>>
- **10AWG**：DC 供电双铜导体线规 <<<PAGE 30>>>
- **AHJ（Authority Having Jurisdiction）**：有管辖权的地方电气机构（DC 线 >3m 时咨询）<<<PAGE 31>>>
- **风扇托盘（Fan Tray）**：3 件常驻、N+1 冗余、仅前→后气流；9907 每托 3 扇、9912 每托 5 扇 <<<PAGE 28>>>

## 安装与登录（Ch2）
- **三人机架作业**：两人抬一人拧（"Use two additional people"）<<<PAGE 36>>>
- **锁杆（Lock Levers）**：CFM/NI 模块闭锁机构（90 度全闭锁定）<<<PAGE 38>>>/<<<PAGE 42>>>
- **9600-8N1**：console 默认串口参数（RJ45 或 Micro-USB）<<<PAGE 44>>>
- **EMP 线缆规则**：接交换机用直通线、接计算机用交叉线 <<<PAGE 45>>>
- **EMP 默认地址**：192.168.1.1/255.255.255.0；改址命令 `ip interface emp` <<<PAGE 46>>>
- **admin/switch**：出厂默认账号/密码 <<<PAGE 46>>>
- **aaa authentication**：解锁会话类型命令族 <<<PAGE 47>>>
- **show chassis / Power Left**：机箱信息与可用功率预算查看 <<<PAGE 49>>>
- **DB9-RJ45 Connector**：随箱附带的 console 转接头 <<<PAGE 34>>>

## PoE（Ch3）
- **lanpower slot service**：逐 slot 物理激活/停止 PoE（首次激活唯一途径）<<<PAGE 50>>>/<<<PAGE 52>>>
- **lanpower power / lanpower slot maxpower**：单口/整槽功率上限（slot 默认 1800W；不预留）<<<PAGE 50>>>/<<<PAGE 53>>>
- **lanpower priority**：口优先级 low/high/critical（默认 low）<<<PAGE 50>>>/<<<PAGE 54>>>
- **lanpower capacitor-detection**：电容检测（仅老式 IP 话机、不符 IEEE、默认关）<<<PAGE 50>>>/<<<PAGE 54>>>
- **lanpower slot priority-disconnect**：优先级断电裁决开关（默认启用）<<<PAGE 50>>>/<<<PAGE 55>>>
- **lanpower power-rule**：按日期/时间的 PoE 供电规则命令 <<<PAGE 53>>>
- **Priority Disconnect**：预算不足时按优先级+物理端口号（48 最高→1 最低，与接入平台相反）裁决 <<<PAGE 55>>>
- **Class 检测**：Class 0-4 分级限功率；默认关；开启复位全部 PoE 口 <<<PAGE 51>>>/<<<PAGE 52>>>
- **show powersupply / show lanpower slot**：电源/PoE 逐口与预算状态命令 <<<PAGE 50>>>/<<<PAGE 51>>>
- **HPoE（75W）**：前 8 口 75000mW 大功率 PoE；at 口 30000mW <<<PAGE 50>>>

## 热插拔（Ch4）
- **热插拔节律**：拆件间隔 30 秒、插件间隔 5 分钟+LED 无错 <<<PAGE 63>>>
- **同类替换（like modules）**：NI 模块热换只能换同型号 <<<PAGE 63>>>
- **CFM 120 秒窗口**：CFM 热换须在 120 秒内完成 <<<PAGE 63>>>

## 标准与合规（附录 A）
- **UL 60950 / IEC 60950-1**：IT 设备安全标准 <<<PAGE 64>>>
- **IEEE 802.3 Hi-Pot + 1.5kV surge**：铜口耐压与浪涌要求 <<<PAGE 64>>>
- **FCC Part 15 Class A / CISPR 22**：Class A 电磁干扰限值 <<<PAGE 64>>>
- **CLASS 1 LASER PRODUCT**：CMM/NI 模块面板激光产品标识 <<<PAGE 16>>>等
- **Prop 65 / WEEE / RoHS（中国、台湾）**：加州警告/欧盟回收/有害物质限制 <<<PAGE 65>>>-<<<PAGE 67>>>
- **Panduit LCD8-10AL / CT-940CH**：接地 lug 及压接工具型号，8AWG、30-60 in-lb <<<PAGE 71>>>
- **22AWG**：机框接地与 DC 回流引线线规 <<<PAGE 70>>>
- **ESD 腕带**：防静电腕带（电源装好并接接地插座才有效）<<<PAGE 72>>>
- **受限场所（Restricted Access Location）**：仅持钥匙/安保措施的维护人员可进入 <<<PAGE 71>>>
- **Tmra**：最大额定环境温度（封闭机架折减依据）<<<PAGE 32>>>

## principles

- **P1** 双机箱规格：OS9907 为 11RU（7 槽=2 CMM+5 NI，49.02×44.2×58.42cm，32.83kg）；OS9912 为 17RU（12 槽=2 CMM+10 NI，76.57cm 高，64.36kg）——同深 23 英寸、同环境包络（0-45°C、湿度 10-90%、海拔 4000m）<<<PAGE 5>>>/<<<PAGE 6>>>/<<<PAGE 11>>>
- **P2** OS9907 slot2 双角色设计："Slot 2 Supports a CMM (for 1+1 CMM redundancy) or NI module (to maximize port count)"——但要性权衡："when an NI is installed in slot 2, CMM redundancy is not provided." <<<PAGE 7>>>/<<<PAGE 16>>>
- **P3** slot2 NI 半速陷阱（9907）："When an XNI module (i.e. OS99-XNI-U48) is inserted in slot 2 only the first 8 ports will be active."（slot2 兼容 CMM 的架构代价）<<<PAGE 7>>>
- **P4** CFM 藏于风扇之后："CFMs are located behind the chassis fan trays. To access a CFM, remove the fan tray in front of the module."（CFM1/2 可用，CFM3/4 预留未激活）<<<PAGE 10>>>/<<<PAGE 15>>>/<<<PAGE 20>>>
- **P5** 电源 N+1 负载分担："Slots PS1 through PS4 Support up to four load-sharing chassis power supplies, offering N+1 redundancy." <<<PAGE 8>>>/<<<PAGE 13>>>
- **P6** 风扇 N+1 与单向气流：3 风扇托盘常驻（9907 每托 3 风扇、9912 每托 5 风扇）、Airflow Direction "Front-to-back only"（与 6900 的双向气流不同）；功耗 112W/200W <<<PAGE 9>>>/<<<PAGE 14>>>/<<<PAGE 28>>>
- **P7** 拇指螺丝材质过渡："Modules are transitioning to ship with aluminum-headed thumbscrews instead of violet color, plastic thumbscrews. The thumbscrews are mechanically identical and only differ in color."（现场识别勿困惑）<<<PAGE 6>>>/<<<PAGE 12>>>
- **P8** ESD 双接地点：机箱前部 Wrist Strap Grounding Connector + 后部 Grounding Block；ESD 腕带生效前提是电源已装并接接地插座 <<<PAGE 8>>>/<<<PAGE 9>>>/<<<PAGE 72>>>
## CMM 管理模块机制
- **P9** CMM 职责："The CMM manages system functions in the chassis. This includes controlling and monitoring NIs, fabric modules (CFMs) and power distribution."；OS99-CMM 带 2×40G QSFP+ 上行，功耗 64W <<<PAGE 16>>>
- **P10** CMM2 升级版：4×100G QSFP28 上行/VFL 口，功耗 74W；版本门槛——"The OS99-CMM2 requires a minimum AOS version of 8.10R2 and cannot be mixed with the existing OS99-CMM in the same chassis." <<<PAGE 17>>>
- **P11** CMM 双 console：RJ45 + Micro-USB（需装驱动）；EMP RJ45 10/100/1000 带外管理 + USB Type A 存储口 <<<PAGE 16>>>/<<<PAGE 17>>>
- **P12** CMM LED 组合诊断语义：PRI（稳绿=主/闪绿=备/稳黄=停运/闪黄=软件升级中）；VC（稳蓝=Master/稳黄=Slave）；FAB 闪黄=CFM 电源故障或 PCIe 上报失败（NI 全断电但仍可 console/EMP 登录）；PRI/VC/FAB/PS/TEMP 五灯同时闪黄=全部 CFM PCIe 硬链路失效（主 CMM 拒绝登录、console 每 5 秒报 "PCIe link failure"）<<<PAGE 18>>>
- **P13** QSFP 上行 LED 多维编码：Off=管理 Down 或无收发器；绿(A)=40G/100G；绿(A/B/C/D)=4X10G/4X25G 分支；蓝=VFL；白=QSFP28 特殊态 <<<PAGE 19>>>
## 交换矩阵（CFM）机制
- **P14** CFM 带宽叠加模型："Each CFM installed provides additional fabric bandwidth to chassis management and the Network Interface (NI) modules."；带宽阶梯：OS9907-CFM=2.56 Tbps、OS9907-CFM2=12.8 Tbps（需 AOS ≥8.9R1、不可与 CFM 混插）、OS9912-CFM=25.6 Tbps；功耗 119W/119W/222W <<<PAGE 20>>>/<<<PAGE 21>>>
- **P15** CFM 经中板连接："The modules connect to the chassis mid-plane and are located just behind the system fan trays."（NI 走背板、CFM 走中板）<<<PAGE 20>>>/<<<PAGE 36>>>等
- **P16** OS9907 组合兼容矩阵：CMM+CMM/CFM+CFM=支持；CMM+CMM/CFM2+CFM2=支持；CMM2+CMM2/CFM2+CFM2=支持；其余三种组合（CFM 与 CFM2 混插、CMM2 配旧 CFM、CMM 与 CMM2 混插）均 Not Supported <<<PAGE 22>>>
- **P17** VC-of-2 双机箱虚拟化：9907 支持两机箱互联，仅三种对等组合支持（CMM+CFM ↔ CMM+CFM；CMM+CFM2 ↔ CMM+CFM2；CMM2+CFM2 ↔ CMM2+CFM2），"All other combination Not Supported" <<<PAGE 22>>>
## NI 模块体系
- **P18** 11 种 NI 模块谱系：铜口（XNI-48 1/10GBaseT 402W、GNI-48 千兆 56W）；光口（XNI-U48 48×SFP+ 305W、GNI-U48 48×SFP 70W、XNI-U24 24×SFP+ 153W）；PoE（GNI-P48 48 口 PoE+8×HPoE 54W、XNI-P48Z16 32 口 at+16 口多千兆 at 402W、XNI-P24Z8 16+8 口 187W、XNI-UP24Q2 12×SFP+ +12×HPoE 多千兆+2×QSFP+ 117W）；高速（CNI-U8 8×QSFP28 117W、CNI-U20 20×100G 314W、XNI-U12Q 12×SFP+ +1×QSFP+）<<<PAGE 23>>>-<<<PAGE 26>>>
- **P19** HPoE 口规则（PoE 模块通用）："Ports 1 through 8 support HPoE (75W). These ports are labeled 'HPoE' on the chassis front panel."（前 8 口为大功率口）<<<PAGE 24>>>
- **P20** 9912 不支持的 NI 清单：XNI-P48Z16、XNI-P24Z8、XNI-UP24Q2、XNI-U12Q 均标注 "Not supported in an OS9912 chassis."（选型必查）<<<PAGE 24>>>/<<<PAGE 25>>>/<<<PAGE 26>>>
- **P21** CNI-U20 分支口："13-20 support splitter function"（100G 口可分支）<<<PAGE 26>>>
- **P22** NI 模块 LED 体系：背光状态 LED（稳蓝=HW OK/闪蓝=启动中或故障）；Speed LED（稳绿=HW OK/闪绿=SW 心跳正常/稳黄=SW 故障/稳红=HW 故障）；端口 LED 绿=非 PoE 链路、黄=PoE 链路（PoE 模块）<<<PAGE 27>>>
## 电源与功率机制
- **P23** 双电源型号：OS99-PS-A（AC，100-240V 输入，输出两档 1200W/21.4A 或 3000W/53.5A）；OS99-PS-D（DC，-40~-72V 输入 75A，输出 2500W/44.6A@56V）；均热插拔、均为 System+PoE 供电 <<<PAGE 29>>>/<<<PAGE 30>>>
- **P24** 电源三不混："Mixing of AC and DC power supplies is not supported. Mixing of Hi (240VAC) and Low (110VAC) input is not supported."（与 6900 的 AC+DC 可混相反）<<<PAGE 29>>>/<<<PAGE 63>>>
- **P25** 分路保护建议："ALE recommends using circuit breakers that are rated for 30A (AC) and 110A (DC) per power supply."（DC 侧实接规范另有 75A 过流 + 双 10AWG 导体）<<<PAGE 29>>>/<<<PAGE 30>>>
- **P26** 机箱功率预算动态机制："As soon as a component is inserted and its connectors make contact with the chassis mid-plane, additional power requirements take effect. If there is not adequate power, the incoming component may not power on."——加模块/拔电源前必须 `show chassis` 查 Power Left（例：2041W 可用）<<<PAGE 49>>>
- **P27** DC 长线与连接器规范：DC 线 >3m 属本地规范管辖（联系电工与 AHJ）；须配 FCI 10080598-2ED0006LF 4P PWRBLADE 连接器 <<<PAGE 31>>>
- **P28** 冗余 AC 分电路原则："It is recommended that each AC outlet resides on a separate circuit." <<<PAGE 33>>>
## PoE 机制
- **P29** PoE 模块四件套：GNI-P48、XNI-P48Z16、XNI-P24Z8、XNI-UP24Q2；标准栈 802.3af/at；HPoE 75W + 802.3at 30W；HPoE 口默认 75000mW、at 口 30000mW、slot 默认 1800W <<<PAGE 50>>>
- **P31** 端口优先方向反转（对比接入交换机）："PoE Physical Port Priority 48 (Highest) -> 1 (Lowest)"——9912/9907 平台端口号越大优先级越高，与 6865/6870 的"1 最高"相反 <<<PAGE 55>>>
- **P32** Priority Disconnect 四场景裁决：禁用→一律拒新 PD；启用+同级→按物理端口号（48 高 1 低）；启用+新 PD 最高优先级→必得电、先断最低优先级口、同级断端口优先级数字最低（即端口号最大）口；启用+新 PD 最低→拒 <<<PAGE 55>>>/<<<PAGE 56>>>
- **P33** Class 检测默认关、开启复位全部 PoE 口："Enabling class detection will reset all PoE ports."；Class 0-4 梯度 0.44-30W <<<PAGE 52>>>
- **P34** 三级端口优先级：low（默认先断）/high/critical，`lanpower port priority` 逐口设置；capacitor-detection 默认关、不符 IEEE；priority-disconnect 默认开 <<<PAGE 50>>>/<<<PAGE 54>>>
- **P35** 端口/槽最大功率语义：只设上限不做预留："Changing the maximum power available to a slot or port does not reserve or immediately allocate that power." <<<PAGE 53>>>
- **P36** 911/UPS 供电纪律：带 IP 话机的 PoE 交换机应全程电源冗余并接 UPS <<<PAGE 50>>>
## 热插拔与安全机制
- **P37** 热插拔节律双标准：拆件间隔 30 秒；插件间隔 5 分钟且 LED 无错才可进行下一件——"All component removals must have a 30 second interval... All component insertions must have a five minute interval AND an LED state indicating that no errors have occurred." <<<PAGE 63>>>
- **P38** 单件不可热拆原则："Hot swapping CMMs, CFMs, or power supplies is supported ONLY if more than one of these components is installed."（单 CMM/单 CFM/单电源时拆即断业务）<<<PAGE 63>>>
- **P39** CFM 热换三纪律：一次只换一个；风扇托盘全数在位；"CFM hot swap should be completed within 120 seconds." <<<PAGE 63>>>
- **P40** NI 热换只限同类："Network Interface (NI) modules can only be hot swapped with like modules."；先断全部网线、拔全部光模块、等 30 秒再插替代件 <<<PAGE 63>>>
