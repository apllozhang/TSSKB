# GLOSSARY — OmniSwitch 6465 Hardware Users Guide 核心术语

从 verified 术语库精选 52 条，按主题分组。型号/部件号/命令保留英文，页码为原书页码。

## 机型（Ch1/Ch3）

- **OS6465-P6**：4 口 at PoE（奇数口 60W/bt）+2×SFP，工业无风扇 DIN，-40~75°C，24-60Vdc（<<<PAGE 12>>>/<<<PAGE 24>>>）
- **OS6465-P12**：8 口 at PoE（奇数口 60W）+4×SFP，工业无风扇 DIN（<<<PAGE 12>>>/<<<PAGE 27>>>）
- **OS6465-P12 (ENH-240)**：P12 增强 240W 预算变体，20-60Vdc/10A 输入，面板标注 ENH-240（<<<PAGE 12>>>/<<<PAGE 30>>>）
- **OS6465-P28**：22 口 at（1-8 口 60W/bt）+2×SFP+4×SFP+ 的 1U 机架工业机，唯一电源负载分担/热换（<<<PAGE 12>>>/<<<PAGE 31>>>）
- **OS6465T-12**：8 口非 PoE+2 combo+2×SFP 运输版半宽（内置 65W、风扇 45°C 自启）（<<<PAGE 12>>>/<<<PAGE 34>>>）
- **OS6465T-P12**：8 口 at PoE 运输版（内置 185W 双输出），无工业认证（<<<PAGE 12>>>/<<<PAGE 36>>>）
- **T 后缀**：运输/交通机型标记——宽温但不含工业认证（<<<PAGE 12>>>）
- **奇数口 60W 规则**：P6/P12 奇数编号口支持 60W/802.3bt，偶数口 30W（<<<PAGE 12>>>/<<<PAGE 22>>>）

## 电源体系（Ch3）

- **OS6465H-BPNX**：480W AC 电源（54.5VDC/8.8A），仅配 ENH-240，无工业认证、标签或误标（<<<PAGE 51>>>）
- **OS6465-BPN-H**：180W AC 电源（54.5VDC/3.5A），配 P6/P12/ENH-240（<<<PAGE 52>>>）
- **OS6465-BPN**：75W AC 电源（-48VDC/1.6A）；配 ENH-240 跑 PoE 需 ≥8.9R2（<<<PAGE 53>>>）
- **OS6465-BPR**：P28 专用模块化 180W AC 电源（+56VDC/3.22A），最多两只（<<<PAGE 54>>>）
- **OS6465-BPRD**：P28 专用模块化 180W DC 电源（-20~-28V 或 -36~-72V 输入）（<<<PAGE 55>>>）
- **内置 65W/185W 电源**：T-12 仅 12V 系统输出 / T-P12 双输出 12V+54.5V（<<<PAGE 56>>>）
- **ROJ 电源线**：Removed Outer Jacket 剥外皮端子线——输入黑/棕→L、白/蓝→N、绿/绿黄→PG；输出红(V-)/黑(V+)/绿(PG)（<<<PAGE 58-60>>>）
- **powersupply type 命令**：手工声明电源类型（系统不能自动识别）（<<<PAGE 60>>>）
- **电源负载分担 vs 冗余**：仅 P28 双电源负载分担，其余仅冗余（<<<PAGE 13>>>）
- **DC OK LED**：外置电源直流输出指示（绿=好/红=故障）（<<<PAGE 51>>>）

## 安装部件与套件（Ch3）

- **DIN Mounting Bracket / DIN 卡扣**：挂顶→下旋锁定；下拉释放拆卸（<<<PAGE 23>>>/<<<PAGE 39>>>）
- **OS6465T-RM-19-L**：半宽 T 机型单机机架 L 支架套件（<<<PAGE 41>>>）
- **OS6465T-DUO-MNT**：两台半宽机并排成 1U 套件（<<<PAGE 43>>>）
- **OS6465-WALL-MNT（WALL-KT5）**：P6/P12/T 侧挂/壁挂套件（<<<PAGE 45>>>）
- **OS6465-REAR-MNT**：P28 DNV 侧轨+后托架+支撑托架（<<<PAGE 46>>>）
- **OS6465-DNV-RACK**：P28 DNV 电源托盘+电源罩+filler 板（<<<PAGE 46>>>）
- **OS6465-DNV-DIN**：P6/P12 DNV 左右电源罩+DIN 卡扣（<<<PAGE 46>>>）
- **DNV**：挪威船级社船用标准（DNV 2.4 认证）；装电源罩后限温 55°C（<<<PAGE 46>>>/<<<PAGE 32>>>）
- **Grounding Lug**：接地耳（LCD8-10A-L、8AWG、30-60 in-lb）（<<<PAGE 62>>>）

## 面板与 LED（Ch3）

- **OK LED**：绿=正常/闪绿=进行中/琥珀=启动失败（<<<PAGE 36>>>）
- **VC LED**：稳绿=master/稳琥珀=slave/闪琥珀次数=单元号（<<<PAGE 37>>>）
- **PS1/PS2 LED**：绿=正常/琥珀=故障/灭=不在位（<<<PAGE 37>>>）
- **Alarm In/Out LED**：琥珀=检测到告警输入/输出（<<<PAGE 37>>>）
- **Ambient（Tmra）**：环境工作温度（工业线 -40~75°C）（<<<PAGE 24>>>）
- **Warning/Danger Threshold**：各机型 75-95/83-97°C；Danger 关机不可配（<<<PAGE 24-36>>>/<<<PAGE 67>>>）

## 告警与 Dying Gasp（Ch3）

- **Alarm Relay（告警继电器）**：单输入（5-12VDC 传感器）+单输出（NO/C/NC，220VDC/250VAC·2A·60W）（<<<PAGE 63>>>）
- **告警事件映射**：alarm in/out/event/map 命令绑定输入或事件到输出（<<<PAGE 63-64>>>）
- **告警自动清除**：8 类事件条件恢复即自动清除（<<<PAGE 65>>>）
- **Dying Gasp**：失电残电发 SNMP trap+Syslog+4×802.3ah OAM PDU（上联口优先）（<<<PAGE 68-69>>>）
- **efm-oam propagate-events dying-gasp**：使能 DG 经 Link OAM PDU 通告（<<<PAGE 68>>>）
- **snmp station / swlog output socket**：DG trap/Syslog 接收站配置（<<<PAGE 68>>>）

## PoE 体系（Ch4）

- **HPoE**：60W 口（奇数口/1-8 口），3000-60000mW（<<<PAGE 72>>>）
- **PoE 温度降额**：≤60°C 全额/60-70°C 降额（100 CFM）/70-75°C 停（<<<PAGE 74>>>）
- **100 CFM 气流条件**：60-70°C 降额档前提（<<<PAGE 74>>>）
- **lanpower slot service / port admin-state**：槽级启停（首启必用）/端口复活（<<<PAGE 77>>>）
- **lanpower power / slot maxpower**：口/槽上限，不预留（<<<PAGE 77-78>>>）
- **lanpower priority**：low/high/critical 三级（<<<PAGE 78>>>）
- **Guard Band**：剩余预算低于口上限即拒新 PD（<<<PAGE 80>>>）
- **Priority Disconnect**：优先级+物理口号（1 高 8 低）裁决新 PD（<<<PAGE 81-83>>>）
- **capacitor detection**：电容检测（仅 legacy 话机，不符 IEEE）（<<<PAGE 79>>>）
- **show module/temperature/powersupply/lanpower**：硬件巡检命令族（<<<PAGE 66>>>/<<<PAGE 75-76>>>）

## 安全与法规（附录 A）

- **工业认证体系**：ISA 12.12.01/UL 508/EN50021、IEC 60068-2、DNV 2.4、EN 50121-4、NEMA TS-2、MIL-STD-810F（T 机型不适用）（<<<PAGE 90>>>）
- **NEBS GR-1089-CORE**：楼内端口禁金属连 OSP；AC 须接 SPD（<<<PAGE 93>>>）
- **CBN（Common Bonding Network）**：共模接地网（NEBS 要求）（<<<PAGE 93>>>）
- **星形垫圈/抗氧化剂**：接地防松与裸导线压接处理（<<<PAGE 93>>>）
- **CDE / ESD / Class 1M Laser**：电缆放电/静电腕带/激光勿直视（<<<PAGE 15>>>/<<<PAGE 97>>>/<<<PAGE 22>>>）
- **Class A 设备**：商用环境限制，住宅禁用（<<<PAGE 92>>>）
- **Restricted Access Location**：受限访问场所（<<<PAGE 93>>>）
