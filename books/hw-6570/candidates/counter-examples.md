# counter-examples — OmniSwitch 6570M Hardware Users Guide（警告/限制/不兼容候选）

格式：编号 X# ｜ 警告或限制要点（含英文原句）｜ 页码

## 平台与电源限制

- **X1** 全机型不支持半双工："The OS6570M-12 does not support half-duplex connections."（12D/U28 同句） <<<PAGE 21>>>/<<<PAGE 23>>>/<<<PAGE 25>>>
- **X2** 双冗余电源必须同规格："both power supplies must have identical output wattage and identical nominal output voltage. Use of dissimilar power supplies could result in unexpected behavior and is not supported."（12D；U28 双舱同理适用） <<<PAGE 24>>>
- **X3** 温度阈值固化不可改："The threshold values are factory-set and cannot be modified."（Warning/Danger 均不可配） <<<PAGE 45>>>
- **X4** Danger 超限必须手动重启："the switch will power off until the temperature conditions have been addressed and the switch is manually booted."——不会自动恢复 <<<PAGE 46>>>
- **X5** aaa authentication 一次一类："You cannot specify more than one session type in a single command line." <<<PAGE 18>>>
- **X6** 密码覆盖受限："Be sure to remember or securely record all new passwords; overriding configured passwords on an OmniSwitch is restricted." <<<PAGE 18>>>
- **X7** 非本机文档范围："it is not intended as a software users guide"——软件配置需查 AOS 8 各软件手册 <<<PAGE 8>>>

## 安装与环境警告

- **X8** 禁延长线："Do not use extension cords."（电源要求与上电流程两处） <<<PAGE 13>>>/<<<PAGE 16>>>
- **X9** 非 ALE 电源线需自证合规："If using a non-ALE provided power cord the installer shall confirm it meets the minimum electrical requirements of the power source."（ALE 线 UL 认可 IEC 62368-1） <<<PAGE 13>>>
- **X10** 违反电涌军规可能失保："Failure to follow the above recommendations could result in voiding the warranty of the affected ALE product."（五条：接地 0.01 欧姆以下/STP/浪涌保护器/室外线缆防雷电流上传/CDE 静电放电先接地） <<<PAGE 14>>>
- **X11** 室外禁裸线缆："Never install exposed network cables outdoors." <<<PAGE 15>>>/<<<PAGE 54>>>
- **X12** 气流遮挡致失效："Restricted airflow can cause your switch to overheat, which can lead to switch failure." <<<PAGE 28>>>
- **X13** 密闭多机架环温偏高："If installed in a closed or multi-rack assembly, the operating ambient temperature of the environment may be greater than the room's ambient temperature."——按 Tmra 留余量 <<<PAGE 28>>>
- **X14** 机架螺丝自备："insert a rack mount screw (not provided)"——ALE 不随机提供机架螺丝；DUO-MNT 并排安装需双人抬举 <<<PAGE 29>>>/<<<PAGE 34>>>
- **X15** 盲板必须常装："Because they regulate airflow and help protect internal chassis components, blank cover plates should remain installed at empty module slots and power supply bays at all times."（拆电源不回装须盖盲板） <<<PAGE 43>>>/<<<PAGE 54>>>

## 电气与作业安全

- **X16** 雷暴作业禁令："To avoid a shock hazard, do not connect or disconnect any cables or perform installation, maintenance, or reconfiguration of this product during an electrical storm." <<<PAGE 55>>>
- **X17** 运行中勿触背板："keep your hands and fingers out of power supply bays and do not touch the backplane while the switch is operating." <<<PAGE 56>>>
- **X18** 搬运前断全部电源："be sure to disconnect all power connections before servicing or moving the unit."（多电源设备逐路全断） <<<PAGE 56>>>
- **X19** 接地完整性双要求："The power cord must be connected to a properly wired and earth receptacle. Any equipment to which this product will attached must also be connected to properly wired receptacles." <<<PAGE 56>>>
- **X20** DC 电源接地强制（EMC/EMI）："each DC/DC power supply requires that the ground wire is connected from each DC/DC power supply to Earth Ground." <<<PAGE 57>>>
- **X21** ESD 防护强制："Because electrostatic discharge (ESD) can damage switch components, you must follow proper procedures to eliminate ESD from your person and the surrounding area before handling switch components."（随机附防静电腕带） <<<PAGE 57>>>
- **X22** 锂电池更换须返厂："There is a danger of explosion if the lithium battery is incorrectly replaced. Replace only with the same or equivalent type recommended by the manufacturer... Return the module with the lithium battery to Alcatel-Lucent." <<<PAGE 58>>>

## 激光与场所限制

- **X23** Class 1M 激光警告："CLASS 1M LASER RADIATION WHEN OPEN. DO NOT VIEW DIRECTLY WITH OPTICAL INSTRUMENTS."（三机型面板同注） <<<PAGE 21>>>/<<<PAGE 23>>>/<<<PAGE 25>>>/<<<PAGE 54>>>
- **X24** 空光口勿直视："Lasers emit invisible radiation from the aperture opening when no fiber-optic cable is connected... install protective aperture covers to fiber ports with no cable connected." <<<PAGE 55>>>
- **X25** 受限场所安装："This equipment should be installed in a location that restricts access. A restricted access location is one where access is secure and limited to service personnel..."（DC 接线前提亦含 restricted access location） <<<PAGE 40>>>/<<<PAGE 57>>>
- **X26** Class A 住宅禁用："To avoid electromagnetic interference, this product should not be installed or used in residential environments."（Class A 数字设备，多国声明一致） <<<PAGE 53>>>/<<<PAGE 54>>>

---
合计：26 条（X1-X26）。
