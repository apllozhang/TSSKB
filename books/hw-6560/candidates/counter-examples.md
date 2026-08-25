# counter-examples — OmniSwitch 6560 Hardware Users Guide（警告/限制/不兼容候选）

格式：编号 X# ｜ 警告或限制要点（含英文原句）｜ 页码

## 平台与电源限制

- **X1** SFP(+) 口 10G 需许可："(49-50) SFP(+) (1G/10G) ports (10G speed requires license)"——24X4/48X4 及 P 版的 49-50 口默认 1G，10G 要软件许可 <<<PAGE 30>>>/<<<PAGE 32>>>/<<<PAGE 42>>>/<<<PAGE 44>>>
- **X2** BP-P 300W 电源对 E 机型/新 PN 不支持："OS6560E-P24Z8 ... Not Supported"；P48Z16 仅 903954-90 老版支持 BP-P（新 PN Not Supported）<<<PAGE 60>>>/<<<PAGE 87>>>
- **X3** 新 PN 电源版本门槛："OS6560-BP-PH (904072-90) requires a minimum AOS version of 8.8R1."；"OS6560-BP-PX (904073-90) requires a minimum AOS version of 8.8R1." <<<PAGE 60>>>
- **X4** PoE 电源禁混插 wattage："Mixing different wattage power supplies in a chassis is not supported."（300/600/920 之间不可混）<<<PAGE 61>>>/<<<PAGE 62>>>/<<<PAGE 63>>>
- **X5** 混插或不支持电源会告警："If unlike power supplies are mixed or if an unsupported power supply is used, a console message and a trap are generated." <<<PAGE 88>>>
- **X6** 150W 双兄弟例外：BP（AC）与 BP-D（DC）可同箱混用："Mixing the OS6560-BP with the OS6560-BP-D in the same chassis is supported."（唯一允许的混插组合）<<<PAGE 64>>>/<<<PAGE 65>>>
- **X7** Danger 阈值不可配："The danger threshold is factory-set and cannot be configured by the user."（Warning 阈值本机用户可配，且设太低会误告警）<<<PAGE 76>>>
- **X8** admin-state 不能首次激活 PoE："You cannot use the lanpower port admin-state command to initially activate PoE on a port."（必须 lanpower slot service）<<<PAGE 89>>>
- **X9** Class 检测开启复位全口："Enabling class detection will reset all PoE ports on the chassis." <<<PAGE 89>>>
- **X10** 电容检测不符 IEEE："The capacitive detection method should only be enabled to support legacy IP phones. This feature is not compatible with IEEE specifications." <<<PAGE 91>>>
- **X11** aaa authentication 一次一类："You cannot specify more than one session type in a single command line." <<<PAGE 21>>>
- **X12** 密码覆盖受限："overriding configured passwords on an OmniSwitch is restricted." <<<PAGE 21>>>

## 安装与环境警告

- **X13** 禁延长线："Do not use extension cords."；室外禁裸线缆："Never install exposed network cables outdoors." <<<PAGE 15>>>/<<<PAGE 18>>>
- **X14** 违反电涌五条军规可能失保："Failure to follow the above recommendations could result in voiding the warranty of the affected ALE product."（含 CDE 线缆先接地）<<<PAGE 16>>>
- **X15** 气流遮挡致失效："Restricted airflow can cause your switch to overheat, which can lead to switch failure."（Never obstruct chassis air vents）<<<PAGE 17>>>/<<<PAGE 51>>>
- **X16** 桌面摆放限制："Never attempt to operate a switch while it is placed on its top or side." <<<PAGE 57>>>
- **X17** 盲板必须常装："Because they regulate airflow and help protect internal chassis components, blank cover plates should remain installed at empty module slots and power supply bays at all times." <<<PAGE 52>>>/<<<PAGE 105>>>
- **X18** 雷暴作业禁令："To avoid a shock hazard, do not connect or disconnect any cables or perform installation, maintenance, or reconfiguration of this product during an electrical storm." <<<PAGE 106>>>
- **X19** 机架螺丝自备："Alcatel-Lucent Enterprise does not provide rack-mount screws. Use the screws supplied by the rack vendor."；双人作业强制 <<<PAGE 53>>>

## 电气与激光安全

- **X20** DC 接线五前提："Connect to a reliably ground -48VDC Selv source... The branch circuit overcurrent protection must be rated 15A. Use 12AWG copper conductors... readily accessible disconnect device... restricted access location." <<<PAGE 68>>>
- **X21** 运行中勿触电源舱/背板："keep your hands and fingers out of power supply bays and do not touch the backplane while the switch is operating."；多电源设备维护前断全部电源 <<<PAGE 107>>>
- **X22** 接地红线：电源线必须接正确接地插座；DC/DC 电源地线必须接大地（EMC/EMI）；CBN 共模接地网安装 <<<PAGE 107>>>/<<<PAGE 108>>>/<<<PAGE 68>>>
- **X23** Class 1M 激光："CLASS 1M LASER RADIATION WHEN OPEN. DO NOT VIEW DIRECTLY WITH OPTICAL INSTRUMENTS."；未接光纤勿盯孔位 <<<PAGE 24>>>等/<<<PAGE 105>>>/<<<PAGE 106>>>
- **X24** ESD 腕带强制："Because electrostatic discharge (ESD) can damage switch components, you must follow proper procedures to eliminate ESD from your person and the surrounding area before handling switch components." <<<PAGE 108>>>
- **X25** 锂电池爆炸风险："Hay un peligro de la explosión si la batería del litio en su chasis se substituye incorrectamente."（同型号更换并返厂）<<<PAGE 110>>>

## 使用场所限制

- **X26** Class A 住宅禁令："Warning: To avoid electromagnetic interference, this product should not be installed or used in residential environments."（FCC/VCCI/BSMI）<<<PAGE 104>>>/<<<PAGE 105>>>
- **X27** 受限访问场所："This equipment should be installed in a location that restricts access... limited to service personnel who have a special key"；仅专业电气/机械人员安装维护 <<<PAGE 108>>>/<<<PAGE 106>>>

---
合计：27 条（X1-X27）。
