# glossary — 术语表（OmniSwitch 6465 Hardware Users Guide）

格式：`- **术语**：中文解释 <<<PAGE N>>>`（页码为 fulltext.md 真实标记；按章分组）

## 机型家族（Ch1/Ch3）

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
