# counter-examples — OmniSwitch 6900 Hardware Users Guide（警告/限制候选）

格式：编号 X# ｜ 警告/限制要点（尽量保留英文原句）｜ 页码（fulltext.md 真实 `<<<PAGE N>>>` 标记）

## 气流与端口限制（本书特有重点）

- **X1** 气流方向必须一致："The airflow direction of the power supplies and fan tray must be the same."（电源与风扇托盘方向不同即失配）<<<PAGE 50>>>
- **X2** 气流失配循环重启："Eventually the mismatched configuration will cause the chassis to reboot to avoid overheating."（启动时失配=OK/PS 绿琥珀交替闪+持续重启；运行中热插失配件=OK/PS 闪琥珀+到 Danger 阈值重启）<<<PAGE 50>>>/<<<PAGE 52>>>
- **X3** 端口组速率不可混（V72）："The OS6900-V72 doesn't support a mix of 10G and 25G speeds on the 4-port groups of ports 1-48."（12 个 4 口组内必须同为 10G 或 25G）<<<PAGE 28>>>
- **X4** 端口组速率不可混（X48C4E/V48C8）："Ports within a port group must all run at either 1G/10G speed or 25G speed. Mixing 1G and 10G speeds is supported."（V48C8 端口组编号非连续，规划前必查分组表）<<<PAGE 38>>>/<<<PAGE 40>>>
- **X5** DAC 与 QSFP 混插禁令（T48C6/X48C6）："Mixing Direct-attached cables (DAC) and QSFPs is not supported on ports 52 and 53. If both ports are populated they must be of the same type." <<<PAGE 34>>>/<<<PAGE 36>>>
- **X6** OS6920 后→前气流温度降额：后→前气流 Tmra 仅 0-35°C（前→后为 0-45°C）："The installation site must maintain a temperature between 0° and 35° Celsius... for the OmniSwitch 6920 with back-to-front airflow." <<<PAGE 14>>>/<<<PAGE 47>>>
- **X7** 气流阻塞后果："Restricted airflow can cause your switch to overheat, which can lead to switch failure." / "Never obstruct chassis air vents." <<<PAGE 17>>>/<<<PAGE 50>>>

## 电源限制

- **X8** 两代电源不可混："Do not mix OS6900-V72/C32/C32E/X48C4E/V48C8 power supplies with OS6900-T48C6/X48C6/T24C2/X24C2 power supplies."（650W 系与 400W 系外观相近但互不兼容）<<<PAGE 60>>>-<<<PAGE 65>>>
- **X9** AC+DC 混插允许（正面对照）："Mixing an AC and DC power supply in the same chassis is supported." <<<PAGE 60>>>等
- **X10** 拆电源先断源："When removing a power supply, first disconnect the power cord from the power source." <<<PAGE 69>>>
- **X11** 无电源开关语义：接电即开机、断全部电源线即关机 <<<PAGE 59>>>
- **X12** OS6920 AC 低压输入降额：100-127V 时 12V 输出仅 83.33A（220-240V 为 125A）；且 "The system hold time for this power supply at 100% load is less than 20ms." <<<PAGE 64>>>
- **X13** DC 过流与线规（OS6920）："The branch circuit overcurrent protection must be rated 50A. Use 6AWG copper conductors."（远大于 V/X 系 12AWG）<<<PAGE 66>>>
- **X14** DC 源必须在受限场所："The power source must be installed in a restricted access location." <<<PAGE 66>>>
- **X15** DC 地线 EMC 强制："For EMC/EMI, each DC/DC power supply requires that the ground wire is connected from each DC/DC power supply to Earth Ground." <<<PAGE 87>>>
- **X16** IEC 60945 场景专用线缆：X48C6+OS6900X-BPD-F 需 IEC 60945 认证时必须用 OS-DNV-DC-PWR 线缆（双磁环）<<<PAGE 63>>>
- **X17** 禁用延长线："each supplied AC power cord is 2 meters (approx. 6.5 feet). Do not use extension cords." <<<PAGE 15>>>/<<<PAGE 20>>>
- **X18** 多电源快速上电："be sure to plug in each power supply in rapid succession, (i.e., within a few seconds of each other)." <<<PAGE 20>>>
- **X19** 电涌违规范即失保："Failure to follow the above recommendations could result in voiding the warranty of the affected ALE product." <<<PAGE 16>>>
- **X20** CDE 静电放电风险："Category 5e, Category 6, and Category 6a cables can store large amounts of static electricity... could lead to a Cable Discharge Event (CDE)." <<<PAGE 15>>>/<<<PAGE 16>>>

## 风扇与安装限制

- **X21** 风扇托盘必装："The fan tray is a required component. Never attempt to operate the switch without a fan tray installed." <<<PAGE 70>>>
- **X22** 60 秒更换窗口："The switch should not run without a fan tray more than 60 seconds to prevent over heating." <<<PAGE 72>>>
- **X23** 风扇型号不可乱装："Do not attempt to install incompatible fan models in a chassis."（风扇分 F/R 气流方向且随机型专用）<<<PAGE 71>>>
- **X24** 仅前法兰安装禁令："Never rack mount OS6900 switches using only the front-installed rack mount flanges. Due to the chassis overall depth, OS6900 switches must be mounted using additional support braces (available from Alcatel-Lucent) or by attaching flanges to the mid portion of the chassis... Failure to properly mount the switch may result in the chassis sagging in the rack or damage to the switch and its components." <<<PAGE 55>>>/<<<PAGE 56>>>
- **X25** 后支撑强制："Because of the overall chassis depth, additional support braces are used to support the rear of the chassis and prevent sagging in the rack. These braces are required for all rack-mount installations." <<<PAGE 54>>>
- **X26** 禁止倒放/侧放："Chassis must be placed 'right side up.' Never attempt to operate a switch while it is placed on its top or side." <<<PAGE 58>>>
- **X27** 盲板必须常装："Because they regulate airflow and help protect internal chassis components, blank cover panels should be installed over empty module slots and power supply bays at all times." <<<PAGE 53>>>/<<<PAGE 85>>>
- **X28** 机架螺丝自备："Alcatel-Lucent does not provide rack-mount screws. Use the screws supplied by the rack vendor."；双人机架纪律 <<<PAGE 54>>>
- **X29** 专业安装者要求："Alcatel-Lucent switches must be installed by a professional installer." <<<PAGE 14>>>

## 功能未启用与设备限制

- **X30** 预留口未激活（C32E/V48C8/OS6920）："SFP+ ports (Ports 33-34 - 1G/10G) - Not currently functional"（同型还有 V48C8 57-58 口、OS6920 33 口）——规划时不可当可用口 <<<PAGE 32>>>/<<<PAGE 40>>>/<<<PAGE 46>>>
- **X31** 双 EMP 口仅一个可用（T48C6/X48C6）："Only top port is functional." <<<PAGE 34>>>/<<<PAGE 36>>>
- **X32** EMP 远程访问前置条件："Although you have configured the EMP with valid IP address information, you will not be able to access the switch through this port (i.e. TELNET, FTP, HTTP, SSH or SNMP) until you have unlocked these remote session types." <<<PAGE 22>>>

## 温度与人身安全

- **X33** Danger 阈值不可配置："The danger threshold is factory-set and cannot be configured by the user."（超限自动关机须手动启动）<<<PAGE 75>>>
- **X34** 运行中勿触电源槽/背板："To reduce the risk of electrical shock, keep your hands and fingers out of power supply bays and do not touch the backplane while the switch is operating." <<<PAGE 86>>>
- **X35** 多电源检修全断电："Your switch is equipped with multiple power supplies. To reduce the risk of electrical shock, be sure to disconnect all power connections before servicing or moving the unit."（西语版：可能有三根电源线）<<<PAGE 86>>>/<<<PAGE 90>>>
- **X36** 雷暴作业禁令："To avoid a shock hazard, do not connect or disconnect any cables or perform installation, maintenance, or reconfiguration of this product during an electrical storm." <<<PAGE 85>>>
- **X37** Class 1M 激光警告："CLASS 1M LASER RADIATION WHEN OPEN. DO NOT VIEW DIRECTLY WITH OPTICAL INSTRUMENTS." <<<PAGE 84>>>
- **X38** 不可见激光辐射："Lasers emit invisible radiation from the aperture opening when no fiber-optic cable is connected. When removing cables do not stare into the open apertures."（空口装保护盖）<<<PAGE 86>>>
- **X39** 锂电池规格与处置：CR1220 型（适用 X48C6/T48C6/X48C4E/V48C8）；"There is danger of explosion if the Lithium battery in your chassis is incorrectly replaced."；UN3091 分类不得入生活垃圾 <<<PAGE 80>>>/<<<PAGE 81>>>
- **X40** 室外裸线禁令："Never install exposed network cables outdoors." <<<PAGE 18>>>/<<<PAGE 85>>>
- **X41** Class A 住宅禁用："To avoid electromagnetic interference, this product should not be installed or used in residential environments."（台湾 BSMI 版；另有 FCC/CISPR22/VCCI/Korea 同义条款）<<<PAGE 84>>>
- **X42** FCC 擅改失权："Changes and modifications made to the equipment without approval of the manufacturer could void the user's authority to operate this equipment." <<<PAGE 83>>>
- **X43** 接地 lug 规范强制：Panduit LCD8-10A-L + 10-32 3/8" 螺丝 + 8AWG，扭矩 30-60 in-lb <<<PAGE 66>>>/<<<PAGE 73>>>
- **X44** 密码丢失后果："Be sure to remember or securely record all new passwords; overriding configured passwords on an OmniSwitch is restricted." <<<PAGE 23>>>
- **X45** ESD 纪律："you must follow proper procedures to eliminate ESD from your person and the surrounding area before handling switch components." <<<PAGE 88>>>
- **X46** 受限场所要求："This equipment should be installed in a location that restricts access." <<<PAGE 88>>>
