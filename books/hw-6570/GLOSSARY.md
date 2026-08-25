# GLOSSARY · OmniSwitch 6570M Hardware Users Guide

> 页码为原书 `<<<PAGE N>>>` 标记。按机型/端口/安装/电源/DC 接地/监控 LED/DG/CLI/法规分组。

- **OS6570M-12**：半宽定配置机，8×10/100/1000Base-T + 2×100/1000Base-X SFP + 2×SFP+ 上联/堆叠，内置 AC 电源+外部电源连接器，待机 23W <<<PAGE 11>>>/<<<PAGE 21>>>/<<<PAGE 22>>>
- **OS6570M-12D**：12 的 DC 版（内置 DC 30W），待机 24W，存储温度 -40~85°C <<<PAGE 11>>>/<<<PAGE 23>>>/<<<PAGE 24>>>
- **OS6570M-U28**：全宽全光上联型，20×SFP + 4×SFP/RJ45 combo（21-24）+ 6×SFP+（25-30），双电源舱，待机 71W，独有 VC ID LED <<<PAGE 11>>>/<<<PAGE 25>>>/<<<PAGE 26>>>
- **Uplink/Stacking SFP+ 口**：1G/10G 双角色口——上联与 Virtual Chassis 堆叠共用（12 口机 11-12，U28 25-30）<<<PAGE 11>>>/<<<PAGE 21>>>/<<<PAGE 25>>>
- **combo 口**：同口位 SFP 光口与 RJ45 铜口二选一（U28 21-24）<<<PAGE 11>>>/<<<PAGE 25>>>
- **Hot-Swapping**：热插拔——不断电、不中断其他组件地加/换硬件 <<<PAGE 12>>>
- **Availability Features**：可用性特性——电源冗余/热插拔/硬件监控 <<<PAGE 11>>>/<<<PAGE 12>>>

## 快速入门（Ch2）
- **Electrical Surge Warning**：电涌警告五条军规（接地/STP/浪涌保护器/室外雷电流/CDE），违者可能失保 <<<PAGE 14>>>
- **CDE（Cable Discharge Event）**：电缆静电放电事件——接线前先将铜缆瞬时接地 <<<PAGE 14>>>
- **Console port**：控制台串口，默认 DCE，9600/8N1 <<<PAGE 15>>>/<<<PAGE 16>>>
- **EMP（Ethernet Management Port）**：带外管理口——对交换机直通线、对计算机交叉线 <<<PAGE 16>>>
- **aaa authentication**：会话类型解锁命令（一次一类）<<<PAGE 17>>>/<<<PAGE 18>>>
- **admin/switch**：出厂默认登录名/密码 <<<PAGE 17>>>
- **system timezone / contact / name / location**：时区与管理信息配置命令 <<<PAGE 18>>>/<<<PAGE 19>>>
- **show system / write memory**：查看/保存配置命令 <<<PAGE 19>>>

## 机箱与 LED（Ch3）
- **Tmra**：环境工作温度 0-50°C，通常低于内部温度 <<<PAGE 22>>>/<<<PAGE 28>>>
- **Warning Threshold（Thresh）**：内部温度警告阈值——12/12D 85°C、U28 69°C，超限发 trap 不停机 <<<PAGE 22>>>/<<<PAGE 26>>>/<<<PAGE 46>>>
- **Danger Threshold**：危险阈值——12/12D 88°C、U28 74°C，超限关机待手动重启；出厂固化 <<<PAGE 22>>>/<<<PAGE 26>>>/<<<PAGE 46>>>
- **OK LED**：稳绿=诊断与 AOS 启动 OK/闪绿=进行中/稳琥珀=失败 <<<PAGE 27>>>
- **VC LED**：稳绿=master/稳琥珀=slave/闪琥珀（12 口机）报 unit 号/灭=关机或非 VC <<<PAGE 27>>>
- **Virtual Chassis ID LED**：VC 识别灯，U28 前面板独有 <<<PAGE 25>>>
- **PS1/PS2 LED**：U28 三态（绿/琥珀/灭）；12 口机两态（绿/灭）<<<PAGE 27>>>
- **1/CMMA / UNDER THRESHOLD**：show temperature 传感器标识与正常状态值 <<<PAGE 45>>>

## 安装套件（Ch3）
- **OS6570M-RM-19-L**：单半宽机 19 英寸机架套件（L 支架长短臂任意侧）<<<PAGE 30>>>
- **OS6570M-DUO-MNT**：双半宽并排套件（slot/slide 支架+中央支架+盖板拇指螺丝）<<<PAGE 32>>>
- **Rack mount screw (not provided)**：机架螺丝不随机提供 <<<PAGE 29>>>
- **Rubber table-mounting feet**：桌面橡胶脚垫 <<<PAGE 15>>>
- **Minimum Clearances**：12 口上下 1 英寸（有邻设备）/侧 2 英寸；U28 上下 1.75 英寸/侧 2 英寸 <<<PAGE 28>>>

## 电源体系（Ch3）
- **Internal AC Power Supply（65W）**：12 机内置，100-240V/50-60Hz→12V/5.42A <<<PAGE 35>>>
- **Internal DC Power Supply（30W）**：12D 机内置，36-72VDC→12V/5.42A <<<PAGE 35>>>
- **OS6570-12-BP（PS-60W-AC/DA-60Z12）**：12 机外置备份电源，100-240VAC→12V/5A <<<PAGE 36>>>
- **OS6570-12-BP-D（PS-30W-DC/DDR-30L-12）**：12D 外置备份，18-75VDC 宽压→12V/2.5A，双态 LED <<<PAGE 37>>>
- **OS6570-BP（PS-150W-AC）**：U28 用 150W AC 电源，六态 LED <<<PAGE 38>>>
- **OS6570-BP-D（PS-150W-DC）**：U28 用 150W DC 电源，-36~-72VDC，六态 LED <<<PAGE 39>>>
- **Lock Tab**：电源锁扣——插入 click 锁定/按向中心后直拉 <<<PAGE 38>>>/<<<PAGE 41>>>/<<<PAGE 42>>>
- **Power Supply Tray**：电源托盘，AC/DC 通用，4+2+2 螺丝+扎带 <<<PAGE 44>>>
- **External Power Connector**：12/12D 后部外置备份电源连接器 <<<PAGE 11>>>/<<<PAGE 22>>>
- **150W 六态 LED**：稳绿/闪绿待机/闪红本舱无 AC/闪绿红告警/稳红故障/灭全停 <<<PAGE 38>>>/<<<PAGE 39>>>

## DC 接线与接地（Ch3）
- **DC Cable Harness**：三芯 12AWG——绿黄=地/黑=return/红=-48VDC <<<PAGE 40>>>
- **-48VDC SELV / DC-1 / CBN**：安全特低电压源/隔离直流回流/共模连接网络 <<<PAGE 40>>>
- **LCD8-10A-L**：Panduit UL 认证接地 lug，配 10-32 螺丝与 8AWG 铜线 <<<PAGE 40>>>/<<<PAGE 45>>>
- **Branch circuit overcurrent protection 15A**：DC 支路过流保护 15A 前提 <<<PAGE 40>>>

## 监控与 Dying Gasp（Ch3）
- **show module / show module long**：槽位基础/详细查看命令 <<<PAGE 45>>>
- **show temperature**：温度五列查看（Current/Range/Danger/Thresh/Status）<<<PAGE 45>>>
- **Dying Gasp**：失电通告——SNMP trap（前 3 站）+Syslog（前 3 服务器）+4×802.3ah OAM PDU（上联口优先）<<<PAGE 46>>>/<<<PAGE 47>>>
- **efm-oam propagate-events dying-gasp**：口级 DG OAM PDU 使能命令 <<<PAGE 47>>>
- **snmp station / swlog output socket**：DG 告警接收端配置命令 <<<PAGE 46>>>/<<<PAGE 47>>>

## 法规与安全（附录 A）
- **Class A**：A 级数字设备，住宅环境禁用 <<<PAGE 53>>>/<<<PAGE 54>>>
- **Class 1M Laser**：开盖时勿用光学仪器直视 <<<PAGE 21>>>/<<<PAGE 54>>>
- **Hi-Pot Test**：以太网口 2250V DC 耐压（IEEE 802.3）<<<PAGE 52>>>
- **Restricted Access Location**：受限访问场所 <<<PAGE 40>>>/<<<PAGE 57>>>
- **ESD / Wrist Strap**：静电放电防护与腕带 <<<PAGE 57>>>/<<<PAGE 13>>>
- **Lithium Battery Warning**：锂电池错换有爆炸风险，须返厂 ALE <<<PAGE 58>>>
- **GR-63-CORE**：电信设备环境耐用性标准 <<<PAGE 52>>>
- **WEEE / RoHS / Prop 65**：回收/有害物质/加州铅警告 <<<PAGE 48>>>-<<<PAGE 50>>>

---
合计：52 条。
