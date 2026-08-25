# Verified 候选（V1 原文真实性核对 + V2/V3 抽查）

## cases

## 上电与首次登录
- **C1** 上电流程：多电源时数秒内先后插电（rapid succession）；冗余 AC 建议每路接独立电路（"It is recommended that each AC outlet resides on a separate circuit"） <<<PAGE 15>>>/<<<PAGE 17>>>
- **C2** 首次登录六步流程：console（9600-8N1，DCE）→admin/switch→aaa authentication 解锁会话（default local 或逐类）→password 改密（实时保存）→system time/date/timezone→system contact/name/location→show system→write memory <<<PAGE 16>>>-<<<PAGE 20>>>
## 机箱安装
- **C4** 全宽机架安装流程（P28）：两侧装托架→标记机架孔→抬机对齐→先穿每侧底部螺丝紧固→再上其余螺丝（自备机架螺丝）<<<PAGE 40>>>/<<<PAGE 41>>>
- **C5** 半宽单机机架流程（OS6465T-RM-19-L）：长短 L 托架装前部两侧（可互换）→法兰孔对机架孔→先下孔后上孔穿螺丝紧固 <<<PAGE 41>>>/<<<PAGE 42>>>
- **C7** 侧挂/壁挂流程（OS6465-WALL-MNT，P6/P12/T 机型）：2 个侧托架各 3 颗 M4X8→2 个后托架各 M4X8→贴安装面标记打孔→每托架用 2×M5X15 螺栓+4 垫圈+2 螺母固定 <<<PAGE 45>>>/<<<PAGE 46>>>
- **C8** DNV 船用安装流程（P28）：装侧轨/后托架/电源托盘（各按 M4X8 定位）→装电源（托盘+拇指螺丝）→盖电源罩→装 filler 板与滑托架完成总成；P6/P12 用 DNV-DIN 左右电源罩+DIN 卡扣 <<<PAGE 46>>>-<<<PAGE 49>>>
## 电源安装与接换
- **C9** 后托盘电源安装流程：电源 DB-15 两侧导柱对准机箱后导孔→推入至连接器完全就位→拧前部拇指螺丝→冗余配置时对侧连接器/螺孔重复 <<<PAGE 56>>>/<<<PAGE 57>>>
- **C10** ROJ 输出线接线流程：红线入 V- 端子（电源顶前+机箱负端）、黑线入 V+（正端）→每端子扭矩 3.5 in-lb→地线用附赠螺丝固定到电源与机箱接地端（松动方孔内夹片即开）<<<PAGE 59>>>
- **C11** ROJ 输入线接线流程：黑/棕→L、白/蓝→N、绿/绿黄→保护地（电源底前）→按电源标注扭矩紧固；确认前严禁插 NEMA 5-15 入电 <<<PAGE 60>>>
- **C12** 最终上电连接：输出线插机箱 PS1/PS2→NEMA 5-15 插易达插座（Pluggable Type A，插座须近设备）<<<PAGE 60>>>
- **C13** 电源类型配置流程：`powersupply 1 name ALE-75W-ps1 type ale lo-ac`（双电源逐一配置）——系统不能自动识别，不配则功率/PoE 信息错误 <<<PAGE 60>>>/<<<PAGE 61>>>
- **C14** 电源热换流程：冗余时任一电源可不断电更换——断电源→松输入端子拆线→松输出端子拆线→按接线流程装新电源 <<<PAGE 61>>>
- **C15** 机箱 supplemental 接地：LCD8-10A-L 接地耳+8AWG 铜线+30-60 in-lb（前或后 lug 无漆区）<<<PAGE 62>>>
## 告警与监控配置
- **C16** 告警输入→输出映射流程：`alarm in temperature-alarm-in action alarm-out admin-state enable`→`alarm out alarm-out-1 admin-state enable`→`alarm map temperature-alarm-in out alarm-out-1` <<<PAGE 64>>>
- **C17** 系统事件→告警输出流程（认证失败示例）：`alarm event auth-fail-event event authentication-failure admin-state enable`→`alarm out set-alarm-out-chassis-1`→`alarm map auth-fail-event out set-alarm-out-chassis-1`→`show alarm event config` 核对→触发后 `show alarm status` 查看 <<<PAGE 64>>>
- **C18** 告警手工清除：`alarm clear status`（8 类事件条件恢复时自动清除）<<<PAGE 65>>>
- **C19** Dying Gasp OAM 通告配置：`efm-oam admin-state enable`→`efm-oam port 1/1/23-24 admin-state enable`→`efm-oam port 1/1/23-24 propagate-events dying-gasp enable`（PDU 上联口优先）<<<PAGE 68>>>/<<<PAGE 69>>>
- **C20** 硬件巡检流程：show module / show module long 看槽位→show temperature 看传感器（UNDER THRESHOLD 正常）→超 Warning 查气流与室温，Danger 关机处理后手动启动 <<<PAGE 66>>>/<<<PAGE 67>>>
## PoE 配置
- **C21** PoE 首次激活流程：先 `powersupply type` 配好电源→`show powersupply` 确认→`lanpower slot 1/1 service start` 激活→`show lanpower slot` 核对（Max Watts 按温度档显示）<<<PAGE 60>>>/<<<PAGE 75>>>/<<<PAGE 76>>>/<<<PAGE 77>>>
- **C22** 端口功率/优先级配置：`lanpower port 1/1/4 power 3000` 限 3W；`lanpower slot 1/1 maxpower 400` 槽上限；`lanpower port 1/1/4 priority critical` 关键口 <<<PAGE 77>>>/<<<PAGE 78>>>-<<<PAGE 79>>>
- **C23** Guard Band 拒载处置：余 50W、口上限 75W 拒 4W PD→`lanpower power 1/1/1 power 10000` 降到 10W 放行 <<<PAGE 80>>>
- **C24** Priority Disconnect 开关与理解：默认启用；`lanpower slot 2/1 priority-disconnect disable/enable`；同级新 PD 按物理口号裁决（1 最高 8 最低）<<<PAGE 82>>>/<<<PAGE 83>>>

---
合计：24 条（C1-C24）。

## counter-examples

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

## frameworks

- **F1** 6465 双线家族选型框架：工业线（P6/P12/ENH-240=无风扇 DIN、-40~75°C、奇数口 60W bt；P28=1U 机架 24 口+4×SFP+、双可热换电源）／运输线（T-12/T-P12=半宽、内置电源、风扇 45°C 自启、-10~60°C、无工业认证）。选型三问：场景是工厂导轨（工业线+按环境温度查 PoE 降额表）还是车载/路侧（T 线宽温但注意无工业认证）；供电形态（宽压 DC 24-60V 端子式 vs AC）；PoE 总量（ENH-240 240W > P12 150W > P6 45W；P28 双电源最高 285W）。 <<<PAGE 12>>>/<<<PAGE 74>>>
- **F2** 工业 PoE 降额三环体系：环境温度环（≤60°C 全额 / 60-70°C 降额需 100 CFM / 70-75°C 停 PoE）→ 输入电压环（50-57V 满额 / 44-57V 限 af / 24V 仅系统）→ 电源配置环（powersupply type 手工声明 + 双电源同型号约束 + 仅 P28 负载分担）。装机核算顺序：先定环境档→再核输入电压→最后按电源组合查预算表。 <<<PAGE 24>>>/<<<PAGE 30>>>/<<<PAGE 74>>>
- **F3** 失电感知与告警双体系：预防侧=告警继电器（外部传感器输入 5-12VDC + 8 类系统事件，独立/VC 两模式，事件映射到 NO/C/NC 输出，条件恢复自动清除）；亡故侧=Dying Gasp（残电三通道：SNMP trap 前 3 站 + Syslog 前 3 服务器 + 4 个 802.3ah OAM PDU 上联口优先）。运维含义：无人值守站点用告警继电器接本地声光/PLC，用 DG 告知网管失电，双电源分路供电降低 DG 触发概率。 <<<PAGE 63>>>/<<<PAGE 65>>>/<<<PAGE 68>>>/<<<PAGE 69>>>
- **F4** 安装形态五件套框架：DIN 导轨（P6/P12 标配卡扣）→ 机架（P28 全宽 / T 单机 L 支架 / T 双机 DUO 并排）→ 侧挂/壁挂（WALL-MNT 四托架）→ DNV 船用（REAR-MNT + DNV-RACK/DIN 套件，罩内 55°C 限温）→ 后托盘电源（导柱+拇指螺丝）。按部署环境（柜内导轨/机架/墙面/船舱）选套件并核对各自间隙矩阵。 <<<PAGE 38>>>-<<<PAGE 49>>>

---
合计：4 条（F1-F4）。

## glossary

- **OS6465-P6**：4 口 at PoE（奇数口 60W/bt）+ 2×SFP 工业无风扇 DIN 机型，-40~75°C，24-60Vdc <<<PAGE 12>>>/<<<PAGE 24>>>
- **OS6465-P12**：8 口 at PoE（奇数口 60W）+ 4×SFP 工业无风扇 DIN 机型 <<<PAGE 12>>>/<<<PAGE 27>>>
- **OS6465-P12 (ENH-240)**：P12 增强 240W 预算变体，20-60Vdc/10A 输入，面板标注 ENH-240 <<<PAGE 12>>>/<<<PAGE 30>>>
- **OS6465-P28**：22 口 at（1-8 口 60W/bt）+ 2×SFP + 4×SFP+ 的 1U 机架工业机型，唯一支持电源负载分担/热换 <<<PAGE 12>>>/<<<PAGE 31>>>
- **OS6465T-12**：8 口非 PoE + 2 combo + 2×SFP 运输版半宽机型（内置 65W、风扇 45°C 自启）<<<PAGE 12>>>/<<<PAGE 34>>>
- **OS6465T-P12**：8 口 at PoE 运输版（内置 185W 双输出），无工业认证 <<<PAGE 12>>>/<<<PAGE 36>>>
- **T 后缀**：运输/交通场景机型标记——宽温但不含工业认证（"do not meet the Industrial Compliance Requirements"）<<<PAGE 12>>>
- **奇数口 60W 规则**：P6/P12 奇数编号 RJ45 口支持 60W/802.3bt（HPoE），偶数口 30W <<<PAGE 12>>>/<<<PAGE 22>>>

## 电源体系（Ch3）
- **OS6465H-BPNX**：480W AC 电源（PS-I275AC-P/SDR-480-48），100-240VAC→54.5VDC/8.8A，仅配 ENH-240，无工业认证、标签或误标 48V/10A <<<PAGE 51>>>
- **OS6465-BPN-H**：180W AC 电源（PS-I185AC-P/SDR-240-55），54.5VDC/3.5A，配 P6/P12/ENH-240 <<<PAGE 52>>>
- **OS6465-BPN**：75W AC 电源（PS-I75AC/SDR-75-48），-48VDC/1.6A；配 ENH-240 跑 PoE 需 ≥8.9R2 <<<PAGE 53>>>
- **OS6465-BPR**：P28 专用模块化 180W AC 电源（PS-I180AC-P），100-240VAC→+56VDC/3.22A，最多两只 <<<PAGE 54>>>
- **OS6465-BPRD**：P28 专用模块化 180W DC 电源（PS-I180DC-P），-20~-28V/12A 或 -36~-72V/6A 输入 <<<PAGE 55>>>
- **内置 65W/185W 电源**：T-12（仅 12V 系统输出）/T-P12（12V+54.5V 双输出）内置电源 <<<PAGE 56>>>
- **ROJ 电源线**：Removed Outer Jacket 剥外皮端子线——AC 输入黑/白/绿（国际棕/蓝/绿黄）、DC 输出红(V-)/黑(V+)/绿(PG)，输出端子扭矩 3.5 in-lb <<<PAGE 58>>>-<<<PAGE 60>>>
- **DC OK LED**：外置电源直流输出指示（绿=好/红=故障）<<<PAGE 51>>>
- **powersupply type 命令**：手工声明电源类型（系统不能自动识别）<<<PAGE 60>>>
- **电源负载分担 vs 冗余**：仅 P28 双电源为 PoE 负载分担，其余机型双电源仅冗余 <<<PAGE 13>>>

## 安装部件与套件（Ch3）
- **DIN Mounting Bracket / DIN 卡扣**：导轨安装卡扣（挂顶→下旋锁定；下拉释放拆卸）<<<PAGE 23>>>/<<<PAGE 39>>>
- **OS6465T-RM-19-L**：半宽 T 机型单机 19" 机架 L 支架套件 <<<PAGE 41>>>
- **OS6465T-DUO-MNT**：两台半宽机箱并排成 1U 的套件（slot/slide 托架+板+拇指螺丝）<<<PAGE 43>>>
- **OS6465-WALL-MNT（WALL-KT5）**：P6/P12/T 侧挂/壁挂套件（侧托架+后托架+M5 螺栓）<<<PAGE 45>>>
- **OS6465-REAR-MNT**：P28 DNV 侧轨+后托架+支撑托架套件 <<<PAGE 46>>>
- **OS6465-DNV-RACK**：P28 DNV 电源托盘（182343-10）+电源罩+filler 板套件 <<<PAGE 46>>>
- **OS6465-DNV-DIN**：P6/P12 DNV 左右电源罩+DIN 卡扣套件 <<<PAGE 46>>>
- **DNV**：挪威船级社（Det Norske Veritas）船用标准（DNV 2.4 认证）<<<PAGE 46>>>/<<<PAGE 90>>>
- **DNV 电源罩限温**：装罩后环境上限降为 55°C <<<PAGE 32>>>

## 面板与 LED（Ch3）
- **OK LED**：绿=诊断/启动正常，闪绿=进行中，琥珀=启动失败 <<<PAGE 36>>>
- **VC LED**：稳绿=master、稳琥珀=slave、闪琥珀次数=单元号、灭=关机或非 VC <<<PAGE 37>>>
- **PS1/PS2 LED**：绿=电源正常，琥珀=故障，灭=不在位 <<<PAGE 37>>>
- **Alarm In/Out LED**：琥珀=检测到告警输入/输出 <<<PAGE 37>>>
- **Alarm Connectors**：前面板告警接线端子 <<<PAGE 22>>>
- **Grounding Lug**：接地耳（LCD8-10A-L、8AWG、30-60 in-lb）<<<PAGE 62>>>

## 温度与告警体系（Ch3）
- **Ambient（Tmra）**：环境工作温度（工业线 -40~75°C）<<<PAGE 24>>>
- **Internal Temperature Range**：内部传感器温度工作范围 <<<PAGE 24>>>
- **Warning/Danger Threshold**：温度告警/危险阈值（各机型 75-95/83-97°C，Danger 关机不可配）<<<PAGE 24>>>-<<<PAGE 36>>>/<<<PAGE 67>>>
- **Alarm Relay（告警继电器）**：单输入（5-12VDC 外部传感器）+ 单输出（NO/C/NC，220VDC/250VAC·2A·60W）事件通知机制 <<<PAGE 63>>>
- **告警事件映射**：alarm in/out/event/map 命令把输入或系统事件绑定到输出继电器（standalone 与 VC 均支持）<<<PAGE 63>>>/<<<PAGE 64>>>
- **告警自动清除**：电源/温度/Link-Down/Port-Health/System-Health/Port-violation/认证失败/告警输入 8 类事件条件恢复即自动清除 <<<PAGE 65>>>
- **Dying Gasp**：整机失电时残电发 SNMP trap+Syslog+4 个 802.3ah OAM PDU（上联口优先）<<<PAGE 68>>>/<<<PAGE 69>>>
- **efm-oam propagate-events dying-gasp**：使能失电事件经 Link OAM PDU 通告对端 <<<PAGE 68>>>

## PoE 体系（Ch4）
- **HPoE**：60W 口（奇数口/1-8 口），3000-60000mW 范围 <<<PAGE 72>>>
- **PoE 温度降额**：预算随环境温度三档变化（≤60°C 全额/60-70°C 降额/70-75°C 停）<<<PAGE 74>>>
- **100 CFM 气流条件**：60-70°C 降额档的前提散热条件 <<<PAGE 74>>>
- **lanpower slot service / port admin-state**：slot 级 PoE 启停 / 端口级复启（不能首次激活）<<<PAGE 77>>>
- **lanpower power / slot maxpower**：端口/槽最大功率（不预留）<<<PAGE 77>>>/<<<PAGE 78>>>
- **lanpower priority**：端口优先级 low/high/critical <<<PAGE 78>>>
- **Guard Band**：剩余预算低于口上限即拒新 PD 的保护机制 <<<PAGE 80>>>
- **Priority Disconnect**：预算不足时按优先级+物理口号（1 高 8 低）裁决 <<<PAGE 81>>>-<<<PAGE 83>>>
- **capacitor detection**：电容检测（仅 legacy 话机，不符 IEEE）<<<PAGE 79>>>
- **PoE Class**：0-8 级功率分级（15.4/4/7/15.4/30/45/60/75/90-99W）<<<PAGE 76>>>

## CLI 命令（Ch2-Ch4）
- **show module / long / temperature / powersupply / lanpower**：槽位/温度/电源/PoE 状态查看族 <<<PAGE 66>>>/<<<PAGE 75>>>/<<<PAGE 76>>>
- **alarm 命令族**：alarm in/out/event/map/clear status 告警配置与清除 <<<PAGE 64>>>/<<<PAGE 65>>>
- **snmp station / swlog output socket**：配置 DG trap/syslog 接收站 <<<PAGE 68>>>
- **efm-oam**：链路 OAM 使能（DG PDU 通道）<<<PAGE 68>>>/<<<PAGE 69>>>
- **aaa authentication / password / system time/date/timezone / write memory**：首次登录六步命令 <<<PAGE 17>>>-<<<PAGE 20>>>

## 安全与法规（附录 A）
- **工业认证体系**：ISA 12.12.01（UL 1604）/UL 508/EN50021 安全、IEC 60068-2 系列环境、GR-63-CORE、MIL-STD-810F 冲击、DNV 2.4、EN 50121-4 铁路、NEMA TS-2（T 机型不适用）<<<PAGE 90>>>
- **NEBS GR-1089-CORE**：楼内端口禁金属连 OSP 室外线路；AC 须接 SPD <<<PAGE 93>>>
- **CBN（Common Bonding Network）**：共模接地网（NEBS 安装要求）<<<PAGE 93>>>
- **星形垫圈/抗氧化剂**：接地连接防松与裸导线压接前处理（NEBS）<<<PAGE 93>>>
- **CDE（Cable Discharge Event）**：线缆静电放电，接线前先对地放电 <<<PAGE 15>>>
- **ESD/Wrist Strap**：静电防护腕带（触件前必用）<<<PAGE 97>>>
- **Class 1M Laser**：开盖激光辐射勿直视 <<<PAGE 22>>>等
- **Restricted Access Location**：受限访问场所 <<<PAGE 93>>>
- **WEEE / RoHS / Prop 65**：报废回收/有害物质/加州铅警告 <<<PAGE 85>>>-<<<PAGE 87>>>
- **Class A 设备**：商用环境限制（住宅禁用）<<<PAGE 92>>>

---
合计：约 60 条。

## principles

## 家族与端口架构
- **P1** 双线家族结构：工业线 OS6465-P6/P12/P12(ENH-240)/P28（无风扇、DIN 导轨、-40~75°C）+ 运输线 OS6465T-12/T-P12（T 后缀，半宽、内置电源、风扇 45°C 自启）："Fixed-configuration, fanless, din-mountable chassis" <<<PAGE 12>>>
- **P2** 60W/bt 口位规律：P6/P12 奇数口支持 60W/802.3bt（"Odd-numbered ports support 60W/802.3bt"）；P28 为口 1-8 支持 60W/bt；偶数口与其余口为 802.3at 30W <<<PAGE 12>>>/<<<PAGE 22>>>/<<<PAGE 31>>>
- **P3** 上行口分档：P6=2×SFP(100/1000Base-X)、P12=4×SFP、T 机型=2 combo + 2×SFP、P28=2×SFP + 4×SFP+(1G/10G)——仅 P28 有 10G 能力 <<<PAGE 12>>>/<<<PAGE 31>>>/<<<PAGE 33>>>/<<<PAGE 35>>>
- **P4** ENH-240 变体机制：同 P12 面板但输入范围扩至 20-60Vdc/10A、50-57V 时 240W PoE，面板标注"ENH-240"区分 <<<PAGE 12>>>/<<<PAGE 28>>>/<<<PAGE 30>>>
- **P5** 电源冗余 vs 负载分担："Only the OmniSwitch 6465-P28 supports power supply load sharing for Power over Ethernet, other models support power supply redundancy only."（第二电源在其他机型上仅做冗余备份）<<<PAGE 13>>>/<<<PAGE 50>>>
- **P6** 无电源开关语义：接电即开机、断全部电源即关机："the chassis does not provide an on/off switch. Connecting a power supply to a power source will boot the switch." <<<PAGE 50>>>
- **P8** 各机型阈值梯度：P6 93/94、P12 95/97、ENH-240 84/89、P28 80/86、T-12 75/83、T-P12 78/85（°C，Warning/Danger）——ENH-240 因功率密度高阈值反而最低 <<<PAGE 24>>>-<<<PAGE 36>>>
- **P9** PoE 预算温度降额机制：P6/P12/ENH-240 按环境温度三档降额——≤60°C 全额（45/150/240W）、60-70°C 降额（30/130/240W，需 100 CFM 气流）、70-75°C 完全停止 PoE（"No PoE Provided"）<<<PAGE 74>>>
- **P10** P28 预算随电源组合变化：单 PS-I180 AC/DC@48V=112W（DC@24V 仅 72W）；双 AC 或双 DC@48V=285W；任何含 DC@24V 的组合=205W <<<PAGE 74>>>
- **P11** P28 DNV 电源盖降额：装 DNV 电源罩后环境上限从 75°C 收窄到 55°C："With DNV Power Supply Cover: -40°C to 55°C" <<<PAGE 32>>>
- **P12** T 机型风扇自启点：45°C 风扇自动开启，风扇开时环境上限 60°C、关时 45°C："Fan will turn on automatically at 45°C." <<<PAGE 34>>>/<<<PAGE 36>>>
## 输入电源机制
- **P14** 双电源一致性强约束："both power supplies must have identical output wattage and identical nominal output voltage. Use of dissimilar power supplies could result in unexpected behavior and is not supported." <<<PAGE 24>>>/<<<PAGE 27>>>/<<<PAGE 30>>>
- **P15** 电源类型不可自动识别："The OmniSwitch 6465 cannot auto-detect the type of power supply connected. The type of power supply connected must be configured"——须用 `powersupply type` 手工配置（如 type ale lo-ac），否则系统与 PoE 信息显示/利用错误 <<<PAGE 60>>>
- **P16** 电源连接器前置：P6/P12/P28 电源接口在机箱前部（P28 后托盘式安装），两连接器可双电源 <<<PAGE 22>>>/<<<PAGE 50>>>
## 可用性与监控机制
- **P17** 可用性四件套：电源冗余、热插拔、自动监控（传感器 trap）、LED + 用户 show 命令 <<<PAGE 13>>>
- **P18** 告警继电器双线模型：单路告警输入（外接温度/接近/门磁传感器，5-12VDC）+ 单路告警输出继电器（NO/C/NC，最大 220VDC/250VAC、2A、60W）；系统事件、trap、SWLog 均可映射到输出 <<<PAGE 63>>>
- **P19** 告警 VC 同步机制：独立运行时输入/事件映射本地输出；VC 中输入/事件跨机箱同步——"The alarm output on any of the chassis can be set by the alarm input, trap, or system events of any other chassis."（支持多输入→单输出、单输入→多输出冗余）<<<PAGE 63>>>
- **P20** 告警自动清除 8 类事件：电源故障/温度超阈/Link-Down/Port-Health/Port-violation（风暴）/System-Health（CPU/内存/flash）/认证失败/告警输入——条件恢复即自动清除，也可 `alarm clear status` 手工清 <<<PAGE 65>>>
- **P21** Dying Gasp 三通道机制：整机失电瞬间残电发出 SNMP trap（前 3 个已配 SNMP 站，含槽号/电源主备/时间）+ Syslog（"Dying Gasp Power Failure Event Occurred"，前 3 个服务器）+ 4 个 802.3ah Link OAM PDU（置 Dying Gasp 位）<<<PAGE 68>>>
- **P24** 温度双阈值行为与 6360 同构：Warning 发 trap 不停机、Danger 自动关机需手动重启且不可配置 <<<PAGE 66>>>/<<<PAGE 67>>>
## LED 机制
- **P26** 电源自带 DC OK LED：绿=直流输出正常、红=直流故障（BPNX/BPN-H/BPN 三款相同定义）<<<PAGE 51>>>/<<<PAGE 52>>>/<<<PAGE 53>>>
- **P27** 端口 LED 颜色分 PoE：RJ45 绿=非 PoE、琥珀=PoE；SFP 与 SFP+ 各自绿系两态 <<<PAGE 37>>>
## 安装机制
- **P28** DIN 导轨快装机构：顶部卡扣先挂轨→下旋到底部卡扣"snaps in place"；拆卸下拉卡扣（难够到可用长螺丝刀）→向外旋出<<<PAGE 39>>>
- **P29** 间隙矩阵按安装方式分：DIN（P6/P12）上下方有设备才留 1 in、两侧 2 in、前后免；P28 机架上下各 1.75 in（1RU）；DNV 罩机型 1RU<<<PAGE 38>>>
- **P30** 双机并排套件（DUO-MNT）：slot/slide 托架前后拼接两台半宽机箱、板+拇指螺丝锁定后作为整体上机架 <<<PAGE 43>>>/<<<PAGE 44>>>
- **P31** DNV（船级社）三套件分工：OS6465-REAR-MNT（P28 侧轨+后托架）、OS6465-DNV-RACK（P28 电源托盘+电源罩）、OS6465-DNV-DIN（P6/P12 电源左右罩+DIN 卡扣）<<<PAGE 46>>>
- **P32** ROJ 电源线双色规：AC 输入北美黑(L)/白(N)/绿(PG)，国际棕/蓝/绿黄（ROJ 30/33mm）；DC 输出红(V-)/黑(V+)/绿(PG)——接线扭矩输出端 3.5 in-lb、输入端按电源标注 <<<PAGE 58>>>/<<<PAGE 59>>>/<<<PAGE 60>>>
- **P33** 接地规范同家族：Panduit LCD8-10A-L、8AWG 铜、30-60 in-lb、无漆区金属接触；NEBS 场景还要求星形垫圈防松、CBN 共模接地网、裸导线压接前清洁涂抗氧化剂 <<<PAGE 62>>>/<<<PAGE 93>>>
## PoE 机制
- **P34** PoE 规格栈（工业线）：802.3at + HPoE；普通口 3000-30000mW、HPoE 口（奇数/1-8 口）3000-60000mW；Class 表含 bt 5-8 类但端口按 60W 封顶 <<<PAGE 72>>>/<<<PAGE 76>>>
- **P35** lanpower 命令族与 6360 同构：service 两级激活（slot service start 才真正供电；admin-state 仅复活）、power/maxpower 上限不预留、priority 三级、capacitor-detection 仅 legacy 话机、Guard Band 拒载（余量<口上限即拒）、Priority Disconnect（同级按物理口号 1 高 8 低裁决）<<<PAGE 77>>>-<<<PAGE 84>>>
- **P36** T-P12 内置 185W 双输出：12V/5.42A 系统 + 54.5V/2.2A PoE 分路；T-12 内置 65W 仅系统 <<<PAGE 56>>>

---
合计：36 条（P1-P36）。
