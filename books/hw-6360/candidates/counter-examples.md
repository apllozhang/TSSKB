# counter-examples — OmniSwitch 6360 Hardware Users Guide（警告/限制/不兼容候选）

格式：编号 X# ｜ 警告或限制要点（含英文原句）｜ 页码

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
