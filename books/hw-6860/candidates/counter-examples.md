# counter-examples — OmniSwitch 6860/6860E/6860N Hardware Users Guide（警告/限制/不兼容候选）

格式：编号 X# ｜ 警告或限制要点（含英文原句）｜ 页码

## 平台与端口限制

- **X1** N 型 SFP28 四口组禁混速："The OS6860N-U28 doesn't support a mix of 1G/10G and 25G speeds on the 4-port group of ports 31-34. Ports within the port group must all run at either 1G/10G speed or 25G speed."（P48Z 51-54、P24Z 27-30 及 OS68-VNI-U4 模块同则；1G 与 10G 混跑允许） <<<PAGE 48>>>/<<<PAGE 50>>>/<<<PAGE 53>>>/<<<PAGE 57>>>
- **X2** HPoE 口非 bt 合规：E-P24/E-P48 口 1-4 为"HPoE (60W - not 802.3bt compliant)"、E-P24Z8 17-24 为 75W 非 bt——对严格 bt PD 互通需留意 <<<PAGE 43>>>/<<<PAGE 45>>>/<<<PAGE 46>>>
- **X3** OS-BPS 停支持：面板图注"OmniSwitch Backup Power Supply (OS-BPS) (No longer supported.)"——老机箱备份电源槽不再可用 <<<PAGE 29>>>/<<<PAGE 31>>>/<<<PAGE 33>>>/<<<PAGE 35>>>
- **X4** 2000W 电源仅限两款 M 机：OS6860N-BPXL 仅配 OS6860N-P48M/P24M；P48Z/P24Z 表列"Not Supported" <<<PAGE 69>>>/<<<PAGE 93>>>

## 电源限制

- **X5** 不支持电源插入即禁全部业务口："Inserting an unsupported power supply will result in the switching and PoE ports being disabled until the correct power supply is inserted." <<<PAGE 69>>>
- **X6** N 电源软件门槛："OS6860N power supplies are supported beginning with AOS release 8.7R1." <<<PAGE 69>>>
- **X7** PoE 电源禁混 wattage："Mixing different wattage power supplies in a chassis is not supported."（600/920/2000 之间不可混；冗余须同型号） <<<PAGE 73>>>-<<<PAGE 77>>>
- **X8** 混插或不支持电源发告警："If unlike power supplies are mixed or if an unsupported power supply is used, a console message and a trap are generated." <<<PAGE 94>>>
- **X9** 150W 双兄弟例外：BP（AC）与 BP-D（DC）可同箱——"Mixing the OS6860-BP-D with the OS6860-BP in the same chassis is supported."（唯一允许混插组合） <<<PAGE 71>>>/<<<PAGE 72>>>
- **X10** 2000W 电源 115V 降额：100-120VAC 输入仅 1000W/18.35A，200-240VAC 才达 2000W/36.7A——按市电核对预算 <<<PAGE 77>>>
- **X11** priority disconnect 电源档上限：920W 电源最多 780W/只、600W 最多 450W/只——预算超限部分不参与抢占 <<<PAGE 99>>>

## Fast PoE / Perpetual PoE 限制

- **X12** Fast PoE 固件前提："Fast PoE requires the proper FPGA/CPLD version, refer to the release notes for additional information." <<<PAGE 96>>>
- **X13** Fast PoE 新机须先做初始 PoE 配置："Factory default switches that don't have any PoE configuration must have an initial PoE configuration completed." <<<PAGE 96>>>
- **X14** Fast PoE 启动期禁改配置："The PoE configuration cannot be modified until the switch is up and the PoE software module is completely initialized." <<<PAGE 96>>>
- **X15** Fast PoE 下 LLDP PD 异常："LLDP-based PoE devices will not function as expected until the switch has completed the boot-up process and the switch is in a state to respond to LLDP requests." <<<PAGE 96>>>
- **X16** Perpetual PoE 固件前提与 MCU 升级断电："Perpetual PoE requires the proper FPGA/CPLD version... The power to the PD devices will be interrupted if the PoE controller (MCU) firmware itself is being upgraded." <<<PAGE 96>>>

## PoE 通用限制

- **X17** class detection 开启复位全口："Enabling class detection will reset all PoE ports on the chassis." <<<PAGE 95>>>
- **X18** admin-state 不能首次激活 PoE："You cannot use the lanpower port admin-state command to initially activate PoE on a port."（须 lanpower slot service） <<<PAGE 95>>>
- **X19** 电容检测不符 IEEE："The capacitive detection method should only be enabled to support legacy IP phones. This feature is not compatible with IEEE specifications." <<<PAGE 98>>>
- **X20** 调低槽预算可掉电："Decreasing the slot-wide power could cause lower priority ports to lose power if the new value is less than the total PoE power currently being consumed." <<<PAGE 97>>>
- **X21** maxpower 不预留功率："Changing the maximum power available to a slot or port does not reserve or immediately allocate that power." <<<PAGE 97>>>
- **X22** Guard Band 不护已上电 PD："The Guard Band functionality does not apply to PDs that are already powered up."——预算缩减时 priority disconnect 生效 <<<PAGE 102>>>

## 登录与温度限制

- **X23** aaa authentication 一次一类："You cannot specify more than one session type in a single command line." <<<PAGE 25>>>
- **X24** 密码覆盖受限："overriding configured passwords on an OmniSwitch is restricted." <<<PAGE 25>>>
- **X25** Danger 阈值固化不可配："The danger threshold is factory-set and cannot be configured by the user."；超限须手动重启 <<<PAGE 87>>>

## 安装与电气警告

- **X26** 禁延长线："Do not use extension cords."；非 ALE 电源线需安装者自证合规 <<<PAGE 18>>>/<<<PAGE 19>>>
- **X27** 违反电涌军规可能失保："Failure to follow the above recommendations could result in voiding the warranty of the affected ALE product."（五条军规） <<<PAGE 20>>>
- **X28** 气流遮挡致失效："Restricted airflow can cause your switch to overheat, which can lead to switch failure."（Never obstruct chassis air vents） <<<PAGE 61>>>
- **X29** 缺盲板破坏风道："When blank cover panels are missing, air does not take the direct route from the air intake vents... an extra task is placed on the power supply fans to cool the chassis."；盲板须常装 <<<PAGE 62>>>
- **X30** 机架螺丝自备+双人作业："Alcatel-Lucent Enterprise does not provide rack-mount screws. Use the screws supplied by the rack vendor."；重设备下置防头重脚轻 <<<PAGE 64>>>
- **X31** 桌面禁倒放/侧放："Never attempt to operate a switch while it is placed on its top or side." <<<PAGE 68>>>
- **X32** 雷暴作业禁令："do not connect or disconnect any cables or perform installation, maintenance, or reconfiguration of this product during an electrical storm." <<<PAGE 111>>>
- **X33** 运行中勿触背板："keep your hands and fingers out of power supply bays and do not touch the backplane while the switch is operating." <<<PAGE 112>>>
- **X34** 多电源设备搬运前全断："be sure to disconnect all power connections before servicing or moving the unit." <<<PAGE 112>>>
- **X35** Class 1M 激光："CLASS 1M LASER RADIATION WHEN OPEN. DO NOT VIEW DIRECTLY WITH OPTICAL INSTRUMENTS."；空光口勿直视并加盖 <<<PAGE 29>>>/<<<PAGE 110>>>/<<<PAGE 111>>>
- **X36** ESD 腕带强制："you must follow proper procedures to eliminate ESD from your person and the surrounding area before handling switch components." <<<PAGE 113>>>
- **X37** 锂电池更换须返厂（西班牙语安全节）："Hay un peligro de la explosión si la batería del litio en su chasis se substituye incorrectamente... Devuelva el módulo con la batería del litio a Alcatel-Lucent." <<<PAGE 114>>>
- **X38** 受限场所安装："This equipment should be installed in a location that restricts access."（DC 前提亦含） <<<PAGE 78>>>/<<<PAGE 113>>>
- **X39** Class A 住宅禁用："To avoid electromagnetic interference, this product should not be installed or used in residential environments." <<<PAGE 110>>>

---
合计：39 条（X1-X39）。
