# counter-examples — OmniSwitch 6870 Hardware Users Guide（警告/限制候选）

格式：编号 X# ｜ 警告/限制要点（尽量保留英文原句）｜ 页码（fulltext.md 真实 `<<<PAGE N>>>` 标记）

## 环境与安装限制

- **X1** 禁止倒放/侧放运行："Never attempt to operate a switch while it is placed on its top or side." <<<PAGE 46>>>
- **X2** 气流阻塞后果："Restricted airflow can cause your switch to overheat, which can lead to switch failure."；"Never obstruct chassis air vents." <<<PAGE 16>>>/<<<PAGE 40>>>
- **X3** 盲板必须常装："Because they regulate airflow and help protect internal chassis components, blank cover plates should remain installed at empty module slots and power supply bays at all times." <<<PAGE 41>>>/<<<PAGE 79>>>
- **X4** 盲板方向限制：装电源槽盲板时箭头必须朝上："When installing blank cover panels over power supply slots, orient the cover panels with the arrows pointing up." <<<PAGE 41>>>
- **X5** 机架螺丝自备："Alcatel-Lucent does not provide rack-mount screws. Use the screws supplied by the rack vendor." <<<PAGE 42>>>
- **X6** 专业安装者要求："Switches must be installed by a professional installer. It is the responsibility of the installer to ensure that proper grounding is available and that the installation meets applicable local and national electrical codes." / "Only personnel knowledgeable in basic electrical and mechanical procedures should install or maintain this equipment." <<<PAGE 14>>>/<<<PAGE 80>>>
- **X7** 双人机架纪律："Two people are required to rack mount the switch: One person to lift the chassis into position and one person to secure the chassis to the rack using the rack mount screws." <<<PAGE 41>>>
- **X8** 顶部/底部免间隙但不可叠压："No clearance is necessary at the top or bottom of the chassis."（对照：桌面安装须用四脚垫起）<<<PAGE 17>>>/<<<PAGE 46>>>

## 电气与电源警告

- **X9** 禁用延长线："each supplied AC power cord is 2 meters (approx. 6.5 feet). Do not use extension cords." <<<PAGE 14>>>/<<<PAGE 17>>>
- **X10** 多电源须快速相继上电："If you have more than one power supply installed, be sure to plug in each power supply in rapid succession, (i.e., within a few seconds of each other). This ensures that there will be adequate power for all components throughout the boot process." <<<PAGE 18>>>
- **X11** 高压输入才得高 PoE 功率："High power PoE wattages for this power supply are available at voltage inputs between 190-240VAC."（1200W/2000W 电源在 100-120V 市电降额）<<<PAGE 52>>>/<<<PAGE 53>>>
- **X12** 拆电源前先断源："When removing a power supply, first disconnect the power cord from the power source."（锁片释放后直向后拉）<<<PAGE 56>>>
- **X13** 无电源开关语义："Connecting an installed power supply to a power source will boot the switch. Likewise, disconnecting all installed power supplies from a power source will power off the switch." <<<PAGE 47>>>
- **X14** DC 极性三线规则：Green/yellow=ground、Black=return、Red=-48VDC；"Observe proper polarity when connecting to a fuse panel." <<<PAGE 54>>>
- **X15** DC 强制受限场所："It must be installed in a restricted access location."（DC 供电机型）<<<PAGE 54>>>
- **X16** DC 过流与线规："The branch circuit overcurrent protection must be rated 15A. Use 12AWG copper conductors." <<<PAGE 54>>>
- **X17** DC 地线 EMC 强制："For EMC/EMI, each DC/DC power supply requires that the ground wire is connected from each DC/DC power supply to Earth Ground." <<<PAGE 82>>>
- **X18** 电涌违规范即失保："Failure to follow the above recommendations could result in voiding the warranty of the affected ALE product." <<<PAGE 15>>>
- **X19** CDE 静电放电风险："Category 5e, Category 6, and Category 6a cables can store large amounts of static electricity... could lead to a Cable Discharge Event (CDE)."（接线前先对地放电）<<<PAGE 15>>>
- **X20** 室外裸线禁令："Never install exposed network cables outdoors." <<<PAGE 17>>>/<<<PAGE 79>>>
- **X21** 雷暴作业禁令："To avoid a shock hazard, do not connect or disconnect any cables or perform installation, maintenance, or reconfiguration of this product during an electrical storm." <<<PAGE 80>>>
- **X22** 运行中勿触电源槽/背板："To reduce the risk of electrical shock, keep your hands and fingers out of power supply bays and do not touch the backplane while the switch is operating." <<<PAGE 81>>>
- **X23** 多电源检修全断电："Your switch is equipped with multiple power supplies. To reduce the risk of electrical shock, be sure to disconnect all power connections before servicing or moving the unit."（西语版特别提示可能有三根电源线）<<<PAGE 81>>>/<<<PAGE 85>>>
- **X24** 双电同源风险："Connect each power supply to a separate independent power source to avoid simultaneous power failures." <<<PAGE 59>>>

## PoE 限制

- **X25** lanpower port admin-state 不能首次激活："You cannot use the lanpower port admin-state command to initially activate PoE on a port."（首次必须 lanpower slot service）<<<PAGE 65>>>/<<<PAGE 66>>>
- **X26** 开 Class 检测复位全机 PoE 口："Enabling class detection will reset all PoE ports on the chassis." <<<PAGE 65>>>
- **X27** 电容检测不符 IEEE："The capacitive detection method should only be enabled to support legacy IP phones. This feature is not compatible with IEEE specifications." <<<PAGE 67>>>
- **X28** 调低 slot 上限可致断电："Decreasing the slot-wide power could cause lower priority ports to lose power if the new value is less than the total PoE power currently being consumed." <<<PAGE 66>>>
- **X29** Guard Band 不保已在电 PD："The Guard Band functionality does not apply to PDs that are already powered up."（预算缩减改由 priority disconnect 裁决）<<<PAGE 68>>>
- **X30** Z 系列电源限制：PS-2000W-AC-POE-2 仅支持 OS6870-P24M/P48M，P24Z/P48Z 标 N/A（预算规划不可套用 2000W）<<<PAGE 47>>>/<<<PAGE 63>>>

## 温度与监控限制

- **X31** Danger 阈值不可配置："The danger threshold is factory-set and cannot be configured by the user."（超限即自动关机须手动重启）<<<PAGE 59>>>
- **X32** 温度超限处置顺序：Warning→查气流阻塞/室温/阈值是否设得过低；Danger→查气流阻塞/室温后手动开机 <<<PAGE 58>>>/<<<PAGE 59>>>

## 操作与人身安全警告

- **X33** Class 1M 激光警告："CLASS 1M LASER RADIATION WHEN OPEN. DO NOT VIEW DIRECTLY WITH OPTICAL INSTRUMENTS."（全机型前面板固定标识）<<<PAGE 23>>>等
- **X34** 不可见激光辐射："Lasers emit invisible radiation from the aperture opening when no fiber-optic cable is connected. When removing cables do not stare into the open apertures."（空口装保护盖）<<<PAGE 81>>>
- **X35** ESD 纪律："Because electrostatic discharge (ESD) can damage switch components, you must follow proper procedures to eliminate ESD from your person and the surrounding area before handling switch components." <<<PAGE 83>>>
- **X36** 受限场所要求："This equipment should be installed in a location that restricts access." <<<PAGE 83>>>
- **X37** 锂电池更换纪律（西语警告）："Hay un peligro de la explosión si la batería del litio en su chasis se substituye incorrectamente."（只能换同型号/等效型号，旧电池寄回工厂）<<<PAGE 84>>>
- **X38** 半双工不支持："Does not support half-duplex connections."（全部 RJ45 机型）<<<PAGE 23>>>等
- **X39** 密码丢失后果："Be sure to remember or securely record all new passwords; overriding configured passwords on an OmniSwitch is restricted." <<<PAGE 20>>>
- **X40** 解锁远程会话即开放远程访问："When you unlock session types, you are granting switch access to non-local sessions (e.g., Telnet)." <<<PAGE 19>>>
- **X41** 单命令单会话类型："You cannot specify more than one session type in a single command line."（解锁多个须连发多条 aaa authentication）<<<PAGE 19>>>
- **X42** Class A 住宅禁用："To avoid electromagnetic interference, this product should not be installed or used in residential environments."（台湾 BSMI 版；另有 FCC/CISPR22/VCCI/Korea 同义条款）<<<PAGE 79>>>
- **X43** FCC 擅改失权："Changes and modifications made to the equipment without approval of the manufacturer could void the user's authority to operate this equipment."（建议只用屏蔽接地线缆）<<<PAGE 78>>>
- **X44** 接地lug规范强制："connect a Panduit Corporation UL listed Lug, (Part number LCD8-10A-L) to the two threaded holes... using protective earthing conductor wire and 8AWG copper conductors. Torque to between 30-60 inch pounds." <<<PAGE 54>>>
- **X45** VFL 推荐 25G：SFP28 口 "(25G recommended for VFL)"（VFL 应用建议跑 25G 速率）<<<PAGE 23>>>等
