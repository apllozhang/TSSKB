# counter-examples — OmniSwitch 6465 Hardware Users Guide（警告/限制/不兼容候选）

格式：编号 X# ｜ 警告或限制要点（含英文原句）｜ 页码

## 平台与电源限制

- **X1** 24V 输入检测电路已知缺陷："Currently an issue with the detection circuitry prevents the configuration of a power supply with 24V output on the switch, and doesn't allow the PS LEDs to be turned on."（P6/P12 以 24V 仅供系统可用，但无法配置电源类型且电源 LED 不亮）<<<PAGE 24>>>/<<<PAGE 27>>>
- **X2** 混用电源不受支持："Use of dissimilar power supplies could result in unexpected behavior and is not supported."（双电源必须同 wattage 同标称电压）<<<PAGE 24>>>/<<<PAGE 27>>>/<<<PAGE 30>>>
- **X3** BPNX 未做工业认证且标签错误："This power supply has not been submitted for validation to meet the industrial certification requirements. The label on power supply may incorrectly state output of 48VDC and 10A."（实际 54.5VDC/8.8A）<<<PAGE 51>>>
- **X4** BPN 75W 电源配 ENH-240 需新版本："To use this power supply for PoE with the OS6465-P12 (ENH-240), the latest 8.9R2 AOS version must be used." <<<PAGE 53>>>
- **X5** 70-75°C 高温停 PoE："Between 70°C to 75°C ... No PoE Provided"（工业线上限温度只能跑系统不能供电）<<<PAGE 74>>>
- **X6** 60-70°C 降额需强制气流："Between 60°C to 70°C (100 CFM air-flow)"（此档预算按 100 CFM 气流条件给出，无此气流条件不可按表套用）<<<PAGE 74>>>
- **X7** T 机型不满足工业认证："The 'T' models support an increased operating temperature range..., but they do not meet the Industrial Compliance Requirements listed in the Standards Compliance section." <<<PAGE 12>>>/<<<PAGE 90>>>
- **X8** P28 DNV 罩降额："With DNV Power Supply Cover: -40°C to 55°C"（装罩后环境上限从 75°C 收窄至 55°C）<<<PAGE 32>>>
- **X9** 电源类型必须手工配置："The OmniSwitch 6465 cannot auto-detect the type of power supply connected."（不配置则功率/PoE 信息错误）<<<PAGE 60>>>
- **X10** 仅 P28 支持电源负载分担："Only the OmniSwitch 6465-P28 supports power supply load sharing for Power over Ethernet, other models support power supply redundancy only." <<<PAGE 13>>>

## 接线与安装警告

- **X11** 接线确认前禁止通电："Do not insert the NEMA 5-15 plug or power connector into the power supply or any live power source until prompted to do so. Failure to follow these instructions may result in bodily injury and/or equipment damage." <<<PAGE 59>>>
- **X12** 只许用 ALE 配件："Only parts provided by Alcatel-Lucent Enterprise should be used when installing the power supplies." <<<PAGE 58>>>
- **X13** 插头式 A 型电源线须易达："The product uses a Pluggable Type A power cord; therefore, please make sure that the power socket is located near the equipment and is easily accessible." <<<PAGE 60>>>
- **X14** 禁延长线/室外裸线缆："Do not use extension cords."；"Never install exposed network cables outdoors." <<<PAGE 14>>>/<<<PAGE 16>>>
- **X15** 违反电涌防护可能失保："Failure to follow the above recommendations could result in voiding the warranty of the affected ALE product."（CDE 等）<<<PAGE 15>>>
- **X16** 雷暴作业禁令："To avoid a shock hazard, do not connect or disconnect any cables or perform installation, maintenance, or reconfiguration of this product during an electrical storm." <<<PAGE 94>>>
- **X17** NEBS/OSP 隔离红线："The intra-building port(s) of the equipment or subassembly MUST NOT be metallically connected to interfaces that connect to the OSP or its wiring... The addition of Primary Protectors is not sufficient protection"（楼内端口禁金属直连室外线路；AC 电源须接 SPD）<<<PAGE 93>>>

## 安全警告

- **X18** ESD 腕带强制："Because electrostatic discharge (ESD) can damage switch components, you must follow proper procedures to eliminate ESD from your person and the surrounding area before handling switch components." <<<PAGE 97>>>
- **X19** Class 1M 激光："CLASS 1M LASER RADIATION WHEN OPEN. DO NOT VIEW DIRECTLY WITH OPTICAL INSTRUMENTS."；未接光纤勿盯孔位并装保护盖 <<<PAGE 22>>>等/<<<PAGE 93>>>/<<<PAGE 94>>>
- **X20** 运行中勿触电源舱/背板："keep your hands and fingers out of power supply bays and do not touch the backplane while the switch is operating."；多电源设备维护前断开全部电源 <<<PAGE 95>>>
- **X21** 接地要求：电源线须接正确接地插座，相连设备同样；DC/DC 电源地线必须接大地（EMC/EMI）<<<PAGE 95>>>/<<<PAGE 96>>>
- **X22** 锂电池爆炸风险（西语原文）："Hay un peligro de la explosión si la batería del litio en su chasis se substituye incorrectamente."（须同型号并返厂更换）<<<PAGE 98>>>
- **X23** Class A 住宅禁令："Warning: To avoid electromagnetic interference, this product should not be installed or used in residential environments." <<<PAGE 92>>>
- **X24** 受限访问场所："This equipment should be installed in a location that restricts access."；仅专业电气/机械人员安装维护 <<<PAGE 93>>>/<<<PAGE 94>>>
- **X25** Danger 温度阈值不可配："The Danger threshold is factory-set and cannot be configured by the user."；Class 检测开启复位全 PoE 口；admin-state 不能首次激活 PoE <<<PAGE 67>>>/<<<PAGE 77>>>

---
合计：25 条（X1-X25）。
