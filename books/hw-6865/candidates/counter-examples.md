# counter-examples — OmniSwitch 6865 Hardware Users Guide（警告/限制候选）

格式：编号 X# ｜ 警告/限制要点（尽量保留英文原句）｜ 页码（fulltext.md 真实 `<<<PAGE N>>>` 标记）

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
- **X20** 雷暴作业禁令："To avoid a shock hazard, do not connect or disconnect any cables or perform installation, maintenance, or reconfiguration of this product during an electrical storm." <<<PAGE 72>>>
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
- **X33** 专业安装者要求："Alcatel-Lucent Enterprise products must be installed by a professional installer." / "Only personnel knowledgeable in basic electrical and mechanical procedures should install or maintain this equipment." <<<PAGE 9>>>/<<<PAGE 72>>>
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
