# GLOSSARY · OmniSwitch 6575 Hardware Users Guide

> 页码为原书 `<<<PAGE N>>>` 标记。按机型/端口/安装/电源/Alarm/DG/M12/M23/PoE/CLI/法规分组。

- **OS6575-P12**：无风扇 DIN 导轨机，8×10/100/1000Base-T 802.3bt 60W + 4×SFP+ Uplink/VFL，24-57VDC/8A，系统功耗 50W，2.5kg <<<PAGE 11>>>/<<<PAGE 21>>>/<<<PAGE 22>>>
- **OS6575-U28**：无风扇 1U 机架机，4×PoE+ 90W combo + 20×100FX/1G SFP + 4×SFP+ Uplink/VFL，双后装电源，24-60VDC，待机 60W <<<PAGE 11>>>/<<<PAGE 23>>>/<<<PAGE 24>>>
- **OS6575-MP16**：无风扇壁装工业机，M12/M23 连接器，4×10/100 + 4×at 30W + 4×bt 60W + 4×Bypass 千兆口，20-110VDC 宽压，3.4kg <<<PAGE 11>>>/<<<PAGE 25>>>/<<<PAGE 26>>>
- **Port Bypass**：断电旁路（MP16 13-16 口）——失电或故障时自动直连两口保通信 <<<PAGE 12>>>/<<<PAGE 25>>>
- **Uplink / VFL**：上联/虚拟 fabric 链路双角色 SFP+ 口（LED 绿=uplink/琥珀=VFL）<<<PAGE 11>>>/<<<PAGE 28>>>
- **M12 D-code / X-code**：10/100 与千兆数据口防水连接器（X-code 千兆四对差分+双 PoE 对组）<<<PAGE 25>>>/<<<PAGE 54>>>
- **M12 A-code**：Console/USB/Alarm 公头连接器 <<<PAGE 25>>>/<<<PAGE 53>>>

## 快速入门（Ch2）
- **Electrical Surge Warning**：电涌警告五条军规（接地 0.01Ω/STP/浪涌保护器/室外防雷/CDE），违者可能失保 <<<PAGE 14>>>
- **CDE（Cable Discharge Event）**：电缆静电放电——接线前先瞬时接地 <<<PAGE 14>>>
- **rollover cable**：反转线——本家族 console 线型（9600/无流控/8N1）<<<PAGE 15>>>
- **admin/switch**：出厂默认登录名/密码 <<<PAGE 16>>>
- **aaa authentication**：会话类型解锁命令（一次一类）<<<PAGE 17>>>
- **show system / write memory**：查看/保存配置命令 <<<PAGE 19>>>

## 机箱与 LED（Ch3）
- **Tmra**：环境工作温度 -40~75°C（三机型一致，工业级）<<<PAGE 22>>>/<<<PAGE 24>>>/<<<PAGE 26>>>
- **PS LED**：绿=主备均正常/琥珀=仅其一正常/灭=不在位 <<<PAGE 27>>>
- **Alarm In / Alarm Out LED**：各一枚，Solid Red=检测到触发 <<<PAGE 27>>>
- **GRN（Leaf）LED**：稳绿=Power Saving Mode/灭=Normal <<<PAGE 27>>>
- **Warning/Danger Threshold**：温度阈值 93/98°C，Danger 出厂固化不可配，超限关机待手动重启 <<<PAGE 50>>>/<<<PAGE 51>>>
- **1/CMMA / UNDER THRESHOLD**：show temperature 传感器标识与正常状态值 <<<PAGE 50>>>

## 安装套件（Ch3）
- **OS6575-REAR-MNT**：U28 后装套件——2 侧轨+2 后支架+1 支撑支架+18×M4X8MM <<<PAGE 31>>>
- **OS6575-TRAY-1U**：U28 1U 电源托盘（4×M4）<<<PAGE 31>>>
- **DIN Rail Bracket / Wall Bracket**：P12 DIN 导轨/壁装支架选件；MP16 用自带 Mounting Holes <<<PAGE 22>>>/<<<PAGE 26>>>/<<<PAGE 33>>>/<<<PAGE 34>>>
- **Rack mount screw (not provided)**：机架螺丝不随机提供 <<<PAGE 30>>>

## 电源体系（Ch3）
- **OS6NN5-BPNS（XDR-150E-48）**：150W 外置 AC 电源（85-260VAC→54.5VDC），配 P12 <<<PAGE 37>>>
- **OS6NN5-BPNSX（XDR-480E-48）**：480W 外置 AC 电源（85-264VAC→54.5V/8.8A），配 P12/U28 <<<PAGE 38>>>
- **OS6575-BPR（PS-I180AC-P）**：180W 模块 AC 电源（100-240VAC→+56V/3.22A），U28 后装最多 2 <<<PAGE 39>>>
- **OS6575-BPRD（PS-I180DC-P）**：180W 模块 DC 电源（-20~-28V/12A 或 -36~-72V/6A→-56V），U28 <<<PAGE 40>>>
- **ROJ（Removed Outer Jacket）**：剥外皮电源线制——外置电源输入/输出均为裸线端子接线 <<<PAGE 42>>>
- **V- / V+ 端子**：输出线极性——红=V-、黑=V+（红负黑正）、绿=保护地 ring 端子 <<<PAGE 42>>>/<<<PAGE 43>>>
- **L / N / PG 端子**：输入线端子——L=黑/棕、N=白/蓝、PG=绿/绿黄条纹 <<<PAGE 42>>>/<<<PAGE 45>>>
- **3.5 inch-pounds**：输出端子接线力矩；输入按电源标签 <<<PAGE 43>>>/<<<PAGE 45>>>
- **DB-15 连接器 / Guide Pins / Thumb Screw**：后装电源对接连接器、导柱与固定拇指螺丝 <<<PAGE 41>>>
- **NEMA 5-15**：AC 插头标准——未到提示步骤不得插入带电插座 <<<PAGE 43>>>/<<<PAGE 45>>>
- **powersupply type 命令**：手动声明电源型号（不能自动检测），如 type ale lo-ac <<<PAGE 46>>>
- **DC OK LED**：四款电源统一双态——稳绿=DC good/稳红=DC issue <<<PAGE 37>>>-<<<PAGE 40>>>

## Alarm Relay 与 DG（Ch3）
- **Alarm Relay**：系统事件/告警输入的 output/trap/SWLog 通告机制 <<<PAGE 48>>>
- **Alarm Input**：单线告警输入（5-12VDC，外接温度/门磁/接近传感器）<<<PAGE 48>>>
- **Alarm Output**：继电器干接点输出（Max 220VDC/250VAC/2A/60W）<<<PAGE 48>>>
- **NO / C / NC**：常开/公共/常闭触点——触发时 NO 闭合、NC 断开 <<<PAGE 48>>>/<<<PAGE 49>>>
- **VC 同步**：VC 内告警输入/trap/系统事件跨机同步，多对一/一对多映射 <<<PAGE 48>>>
- **Dying Gasp**：失电通告——SNMP trap（前 3 站）+Syslog（前 3 服务器），本机无 OAM PDU <<<PAGE 52>>>
- **snmp station / swlog output socket**：DG 告警接收端配置命令 <<<PAGE 52>>>

## M12/M23 配件线缆（Ch3）
- **M23 5-pin（Power）**：MP16 电源连接器——PWR-1±/FGND/PWR-2± 双路输入 <<<PAGE 25>>>/<<<PAGE 53>>>
- **M23-PWRCONN-5P**：M23 电源插座配件（5 只装，不带线）<<<PAGE 55>>>
- **M12-USB-2P / M12-CONSOLE-5P / M12-ALARM-6P**：M12 转 USB/RS232 console/裸线告警配件 <<<PAGE 55>>>
- **M12-DC-M/RJ45F/RJ45M-8P**：D-code 转 D-code/RJ45 配件线缆族 <<<PAGE 55>>>
- **M12-XC-M/RJ45F/RJ45M-8P**：X-code 转 X-code/RJ45 配件线缆族 <<<PAGE 55>>>

## PoE（Ch4）
- **802.3at / 802.3bt**：PoE+ 30W / PoE++ 90W 标准；本机 at 口 3000-30000mW、bt 口 3000-90000mW <<<PAGE 58>>>
- **48VDC 以下禁 PoE**：三机型面板注记红线；第三方电源须 ≥48V <<<PAGE 21>>>/<<<PAGE 23>>>/<<<PAGE 25>>>/<<<PAGE 61>>>
- **U28 输入电压三档**：50-57V=at 150W；44-57V=af 120W；24-60V=纯系统无 PoE <<<PAGE 24>>>
- **PoE 温度阶梯预算表**：机型×电源×数量×温度带（≤50 至 70-75°C 四档）预算矩阵 <<<PAGE 60>>>/<<<PAGE 61>>>
- **MP16 预算封顶**：150W→52W、480W→120W 恒定，加电源不扩容 <<<PAGE 61>>>
- **lanpower slot service start/stop**：整槽启停（首次激活必用）<<<PAGE 64>>>
- **lanpower port admin-state enable/disable**：单口复活/关断（不能首次激活）<<<PAGE 64>>>
- **lanpower power / lanpower slot maxpower**：口/槽功率上限（不预留）<<<PAGE 64>>>/<<<PAGE 65>>>
- **lanpower priority**：口优先级 low/high/critical（默认 low）<<<PAGE 65>>>
- **lanpower class-detection / capacitor-detection**：等级检测（开启复位全口）/电容检测（不符 IEEE，仅老话机）<<<PAGE 64>>>/<<<PAGE 66>>>
- **Guard Band**：剩余预算低于口 maxpower 即拒供新 PD <<<PAGE 67>>>
- **Priority Disconnect**：预算不足时按优先级+物理口号（1 高 8 低）裁决 <<<PAGE 68>>>
- **show lanpower slot / show powersupply**：PoE 逐口/电源状态查看命令 <<<PAGE 63>>>/<<<PAGE 71>>>/<<<PAGE 62>>>
- **911/UPS 纪律**：带 IP 话机的 PoE 交换机须常备电源冗余并接 UPS <<<PAGE 56>>>

## 工业与安全法规（附录 A）
- **NEBS GR-1089-CORE**：楼内端口禁金属直连 OSP；AC 须接 SPD <<<PAGE 80>>>
- **CBN / Star washers**：共模连接网络/星形垫圈防松 <<<PAGE 80>>>
- **ISA 12.12.01 / UL 508 / EN50021**：工业安全标准（危险场所/工业控制）<<<PAGE 77>>>
- **DNV 2.4 / EN 50121-4 / NEMA TS-2 / MIL-STD-810F**：船级社/铁路 EMC/交通控制/军标冲击 <<<PAGE 77>>>
- **IEC 60529 IPXX / IEC 61850-3 / IEEE 1613**：防护等级/变电站 EMC <<<PAGE 77>>>
- **Class A / Class 1M Laser / ESD / Restricted Access Location**：住宅禁用/激光/静电/受限场所 <<<PAGE 79>>>/<<<PAGE 80>>>/<<<PAGE 84>>>/<<<PAGE 83>>>
- **Lithium Battery Warning**：锂电池错换有爆炸风险，须返厂 ALE <<<PAGE 85>>>

---
合计：54 条。
