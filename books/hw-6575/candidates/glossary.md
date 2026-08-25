# glossary — 术语表（OmniSwitch 6575 Hardware Users Guide）

格式：`- **术语**：中文解释 <<<PAGE N>>>`（页码为 fulltext.md 真实标记；按章分组）

## 机型家族（Ch1/Ch3）

- **OS6575-P12**：无风扇 DIN 导轨机，8×10/100/1000Base-T 802.3bt 60W + 4×SFP+ Uplink/VFL，24-57VDC/8A 输入，系统功耗 50W，2.5kg <<<PAGE 11>>>/<<<PAGE 21>>>/<<<PAGE 22>>>
- **OS6575-U28**：无风扇 1U 机架机，4×PoE+ 90W combo + 20×100FX/1G SFP + 4×SFP+ Uplink/VFL，双后装电源，24-60VDC 输入，待机 60W <<<PAGE 11>>>/<<<PAGE 23>>>/<<<PAGE 24>>>
- **OS6575-MP16**：无风扇壁装工业机，M12/M23 连接器，4×10/100 + 4×at 30W + 4×bt 60W + 4×Bypass 千兆口，20-110VDC 宽压，3.4kg <<<PAGE 11>>>/<<<PAGE 25>>>/<<<PAGE 26>>>
- **Port Bypass**：断电旁路特性（MP16 13-16 口）——失电或故障时自动直连两口保通信 <<<PAGE 12>>>/<<<PAGE 25>>>
- **Uplink / VFL**：上联/虚拟 fabric 链路双角色 SFP+ 口（LED 绿=uplink/琥珀=VFL） <<<PAGE 11>>>/<<<PAGE 28>>>
- **Availability Features**：可用性三特性——电源冗余/热插拔/硬件监控 <<<PAGE 12>>>

## 快速入门（Ch2）

- **Grounding wrist strap**：接地防静电腕带（安装三件套之一） <<<PAGE 13>>>
- **Electrical Surge Warning**：电涌警告五条军规（接地 0.01Ω/STP/浪涌保护器/室外防雷/CDE） <<<PAGE 14>>>
- **CDE（Cable Discharge Event）**：电缆静电放电——Cat5e/6/6a 储静电，接线前先瞬时接地 <<<PAGE 14>>>
- **Serial Default Settings**：console 默认 9600/无流控/8N1，rollover 线 <<<PAGE 15>>>
- **rollover cable**：反转线——本家族 console 线型 <<<PAGE 15>>>
- **admin/switch**：出厂默认登录名/密码 <<<PAGE 16>>>
- **aaa authentication**：会话类型解锁命令（一次一类） <<<PAGE 17>>>
- **system timezone / daylight-savings-time**：时区/夏令时命令（默认 UTC） <<<PAGE 18>>>
- **show system / write memory**：查看/保存配置命令 <<<PAGE 19>>>

## 机箱与 LED（Ch3）

- **Tmra**：环境工作温度 -40~75°C（三机型一致，工业级） <<<PAGE 22>>>/<<<PAGE 24>>>/<<<PAGE 26>>>
- **PS LED**：电源灯三态——绿=主备均正常/琥珀=仅其一正常/灭=不在位 <<<PAGE 27>>>
- **Alarm In / Alarm Out LED**：告警输入/输出灯，Solid Red 表示各自检测到触发 <<<PAGE 27>>>
- **GRN（Leaf）LED**：省电模式灯——绿=Power Saving Mode/灭=Normal <<<PAGE 27>>>
- **1/CMMA**：show temperature 传感器标识（Range -45~93/Danger 98/Thresh 93） <<<PAGE 50>>>
- **Warning/Danger Threshold**：温度警告/危险阈值——Danger 出厂固化不可配，超限关机待手动重启 <<<PAGE 50>>>/<<<PAGE 51>>>

## 安装套件（Ch3）

- **OS6575-REAR-MNT**：U28 后装套件——2 侧轨+2 后支架+1 支撑支架+18×M4X8MM 螺丝 <<<PAGE 31>>>
- **OS6575-TRAY-1U**：U28 1U 电源托盘（4×M4 螺丝安装） <<<PAGE 31>>>
- **DIN Rail Bracket**：P12 DIN 导轨安装支架选件 <<<PAGE 22>>>/<<<PAGE 33>>>
- **Wall Bracket**：P12 壁装支架选件；MP16 用自带 Mounting Holes <<<PAGE 22>>>/<<<PAGE 34>>>/<<<PAGE 26>>>
- **Rack mount screw (not provided)**：机架螺丝不随机提供 <<<PAGE 30>>>

## 电源体系（Ch3）

- **OS6NN5-BPNS（XDR-150E-48）**：150W 外置 AC 电源（85-260VAC→54.5VDC），配 P12 <<<PAGE 37>>>
- **OS6NN5-BPNSX（XDR-480E-48）**：480W 外置 AC 电源（85-264VAC→54.5V/8.8A），配 P12/U28 <<<PAGE 38>>>
- **OS6575-BPR（PS-I180AC-P）**：180W 模块 AC 电源（100-240VAC→+56V/3.22A），U28 后装最多 2 个 <<<PAGE 39>>>
- **OS6575-BPRD（PS-I180DC-P）**：180W 模块 DC 电源（-20~-28V/12A 或 -36~-72V/6A→-56V），U28 <<<PAGE 40>>>
- **ROJ（Removed Outer Jacket）**：剥外皮电源线制——外置电源输入/输出均为裸线端子接线 <<<PAGE 42>>>
- **V- / V+ 端子**：输出线极性——红=V-、黑=V+（本机红负黑正）、绿=保护地（ring 端子） <<<PAGE 42>>>/<<<PAGE 43>>>
- **L / N / PG 端子**：输入线端子——L=黑/棕、N=白/蓝、PG=绿/绿黄条纹 <<<PAGE 42>>>/<<<PAGE 45>>>
- **3.5 inch-pounds**：输出端子接线力矩；输入端子按电源标签 <<<PAGE 43>>>/<<<PAGE 45>>>
- **DB-15 连接器 / Guide Pins**：后装电源与机箱对接的连接器及两侧导柱 <<<PAGE 41>>>
- **NEMA 5-15**：AC 插头标准——未到提示步骤不得插入带电插座 <<<PAGE 43>>>/<<<PAGE 45>>>
- **powersupply type 命令**：手动声明电源型号（不能自动检测），如 type ale lo-ac <<<PAGE 46>>>
- **Thumb Screw**：后装电源固定拇指螺丝 <<<PAGE 41>>>

## Alarm Relay（Ch3）

- **Alarm Relay**：告警继电器——系统事件/告警输入的输出/trap/SWLog 通告机制 <<<PAGE 48>>>
- **Alarm Input**：单线告警输入（5-12VDC，外接温度/门磁/接近传感器） <<<PAGE 48>>>
- **Alarm Output**：单线继电器干接点输出（Max 220VDC/250VAC/2A/60W） <<<PAGE 48>>>
- **NO / C / NC**：常开/公共/常闭触点——触发时 NO 闭合、NC 断开 <<<PAGE 48>>>/<<<PAGE 49>>>
- **alarm in/out/map/event 命令族**：告警输入定义/输出使能/映射/事件绑定配置 <<<PAGE 49>>>
- **show alarm event config / show alarm status / alarm clear status**：告警配置/实时状态/清除命令 <<<PAGE 49>>>
- **VC 同步**：VC 内告警输入/trap/系统事件跨机同步，支持多对一/一对多映射 <<<PAGE 48>>>

## Dying Gasp（Ch3）

- **Dying Gasp**：临终告警——失电时发 SNMP trap（前 3 站）+ Syslog（前 3 服务器） <<<PAGE 52>>>
- **Dying Gasp Power Failure Event Occurred**：DG Syslog 消息原文 <<<PAGE 52>>>
- **snmp station / swlog output socket**：DG 告警接收端配置命令 <<<PAGE 52>>>

## M12/M23 连接器与线缆（Ch3）

- **M23 5-pin（Power）**：MP16 电源连接器——PWR-1±/FGND/PWR-2± 双路输入 <<<PAGE 25>>>/<<<PAGE 53>>>
- **M12 A-code**：Console/USB/Alarm 公头连接器（TX/RX/GND；D+/D-/VCC；DO-NO/DO-NC/DO-Comm） <<<PAGE 25>>>/<<<PAGE 53>>>
- **M12 D-code**：10/100 口连接器（TX±/RX±，PoE 版 1/3 脚 PoE+、2/4 脚 PoE-） <<<PAGE 25>>>/<<<PAGE 54>>>
- **M12 X-code**：千兆口连接器（8 脚四对差分，PoE 版 G1/G2 两对组各 PoE±） <<<PAGE 25>>>/<<<PAGE 54>>>
- **M23-PWRCONN-5P**：M23 电源插座配件（5 只装，不带线） <<<PAGE 55>>>
- **M12-USB-2P / M12-CONSOLE-5P**：M12 转 USB / RS232 console 配件线缆 <<<PAGE 55>>>
- **M12-ALARM-6P**：M12 转裸线告警线缆（1m 6 只装） <<<PAGE 55>>>
- **M12-DC-M/RJ45F/RJ45M-8P**：D-code 转 D-code/RJ45 配件线缆族 <<<PAGE 55>>>
- **M12-XC-M/RJ45F/RJ45M-8P**：X-code 转 X-code/RJ45 配件线缆族 <<<PAGE 55>>>

## PoE（Ch4）

- **PoE/PoL/Inline Power**：以太网供电同义术语族 <<<PAGE 56>>>
- **PD / PSE**：受电设备/供电设备 <<<PAGE 56>>>
- **802.3at / 802.3bt**：PoE+ 30W / PoE++ 90W 标准；本机 at 口 3000-30000mW、bt 口 3000-90000mW <<<PAGE 58>>>
- **PoE 温度阶梯预算表**：按机型×电源×数量×温度带（≤50 至 70-75°C 四档）的预算矩阵 <<<PAGE 60>>>/<<<PAGE 61>>>
- **lanpower slot service start/stop**：PoE 整槽启停（首次激活必用） <<<PAGE 64>>>
- **lanpower port admin-state enable/disable**：单口 PoE 复活/关断（不能首次激活） <<<PAGE 64>>>
- **lanpower power / lanpower slot maxpower**：口/槽功率上限命令 <<<PAGE 64>>>/<<<PAGE 65>>>
- **lanpower priority**：口优先级 low/high/critical（默认 low） <<<PAGE 65>>>
- **lanpower class-detection**：等级检测使能（开启复位全口） <<<PAGE 64>>>
- **lanpower capacitor-detection**：电容检测法（仅老 IP 话机，不符 IEEE） <<<PAGE 66>>>
- **Guard Band**：保护带机制——剩余预算低于口 maxpower 即拒供新 PD <<<PAGE 67>>>
- **Priority Disconnect**：优先级断开——预算不足时按优先级+物理口号裁决新 PD 供电 <<<PAGE 68>>>
- **show lanpower slot**：PoE 逐口状态/槽预算查看命令 <<<PAGE 63>>>/<<<PAGE 71>>>
- **show powersupply**：电源类型/状态/总功率查看命令 <<<PAGE 62>>>
- **911/UPS 纪律**：带 IP 话机的 PoE 交换机须常备电源冗余并接 UPS <<<PAGE 56>>>

## 法规与工业标准（附录 A）

- **NEBS GR-1089-CORE**：电信设备电气防护——楼内端口禁金属直连 OSP、AC 须接 SPD <<<PAGE 80>>>
- **CBN（Common Bonding Network）**：共模连接网络——NEBS 安装要求 <<<PAGE 80>>>
- **Star washers**：星形垫圈——防接地连接松动 <<<PAGE 80>>>
- **ISA 12.12.01 / UL 508 / EN50021**：工业安全标准（危险场所/工业控制设备） <<<PAGE 77>>>
- **DNV 2.4**：船级社认证；**EN 50121-4 / IEC 62236-4**：铁路 EMC；**NEMA TS-2**：交通控制；**MIL-STD-810F**：军标冲击 <<<PAGE 77>>>
- **IEC 60529 IPXX**：防护等级标准；**IEC 61850-3 / IEEE 1613**：变电站/电力自动化 EMC <<<PAGE 77>>>
- **Class A / Class 1M Laser / ESD / WEEE / RoHS / Prop 65**：通用法规警告族（住宅禁用/激光/静电/回收/有害物质） <<<PAGE 74>>>/<<<PAGE 79>>>/<<<PAGE 80>>>/<<<PAGE 84>>>
