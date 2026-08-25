# counter-examples — OmniSwitch 9900 Series Hardware Users Guide（警告/限制候选）

格式：编号 X# ｜ 警告/限制要点（尽量保留英文原句）｜ 页码（fulltext.md 真实 `<<<PAGE N>>>` 标记）

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
- **X35** 电容检测不符 IEEE："The capacitive detection method should only be enabled to support legacy IP phones. This feature is not compatible with IEEE specifications." <<<PAGE 54>>>
- **X36** 调低 slot 上限可致断电："Decreasing the slot-wide power could cause lower priority ports to lose power if the new value is less than the total PoE power currently being consumed." <<<PAGE 53>>>
- **X37** PoE 默认 operational disabled："Default PoE operational status: Disabled (PoE must be activated via the lanpower start command.)"——装好即供电的预期会落空 <<<PAGE 50>>>
- **X38** 端口优先方向反转陷阱：本平台 "48 (Highest) -> 1 (Lowest)"（与 6865/6870 相反），跨平台套用优先级规划会反噬 <<<PAGE 55>>>

## 操作与人身安全

- **X39** 多电源检修全断电："Your switch is equipped with multiple power supplies. To reduce the risk of electrical shock, be sure to disconnect all power connections before servicing or moving the unit." <<<PAGE 70>>>
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
