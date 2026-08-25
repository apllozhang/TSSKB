# counter-examples — OmniSwitch 6575 Hardware Users Guide（警告/限制/不兼容候选）

格式：编号 X# ｜ 警告或限制要点（含英文原句）｜ 页码

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

- **X28** 雷暴作业禁令："do not connect or disconnect any cables or perform installation, maintenance, or reconfiguration of this product during an electrical storm." <<<PAGE 81>>>
- **X29** 运行中勿触背板/电源舱："keep your hands and fingers out of power supply bays and do not touch the backplane while the switch is operating." <<<PAGE 82>>>
- **X30** 多电源设备搬运前全断："be sure to disconnect all power connections before servicing or moving the unit." <<<PAGE 82>>>
- **X31** Class 1M 激光："CLASS 1M LASER RADIATION WHEN OPEN. DO NOT VIEW DIRECTLY WITH OPTICAL INSTRUMENTS."；空光口勿直视并加盖 <<<PAGE 21>>>/<<<PAGE 80>>>/<<<PAGE 81>>>
- **X32** ESD 腕带强制："you must follow proper procedures to eliminate ESD from your person and the surrounding area before handling switch components." <<<PAGE 84>>>
- **X33** 锂电池更换须返厂："There is a danger of the explosion if the lithium battery in your chassis is substituted incorrectly... Return the module with the lithium battery to Alcatel-Lucent."（西班牙语安全节） <<<PAGE 85>>>
- **X34** 受限场所安装："This equipment should be installed in a location that restricts access."（正文与 NEBS 均要求） <<<PAGE 80>>>/<<<PAGE 83>>>
- **X35** Class A 住宅禁用："To avoid electromagnetic interference, this product should not be installed or used in residential environments." <<<PAGE 79>>>

---
合计：35 条（X1-X35）。
