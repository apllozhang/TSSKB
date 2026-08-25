# glossary — 术语表（OmniSwitch 6360 Hardware Users Guide）

格式：`- **术语**：中文解释 <<<PAGE N>>>`（页码为 fulltext.md 真实标记；按章分组）

## 机型家族（Ch1）

- **OS6360-10**：10 口非 PoE 半宽 1U（10×RJ45+2×SFP，30W 内置电源，无风扇）<<<PAGE 13>>>
- **OS6360-P10**：8 口 802.3at PoE + 2 口非 PoE + 2×SFP，165W 内置电源，PoE 预算 120W，无风扇 <<<PAGE 13>>>/<<<PAGE 28>>>
- **OS6360-P10A-US**：PN 904324-90 的 P10 变体，不支持 Fast/Perpetual PoE（丝印相同靠 PN 区分）<<<PAGE 28>>>
- **OS6360-24**：24×RJ45 非 PoE + 2 combo + 2×SFP+，65W 内置电源，无风扇 <<<PAGE 13>>>/<<<PAGE 30>>>
- **OS6360-P24**：24 口 802.3at PoE 机型，260W 电源，PoE 预算 180W，无风扇 <<<PAGE 13>>>/<<<PAGE 32>>>
- **OS6360-P24X**：24 口 at + 2×SFP+ combo，550W 电源，PoE 预算 380W，带风扇 <<<PAGE 14>>>/<<<PAGE 34>>>
- **OS6360-PH24**：P24X 同级但 combo 口可软件升级 10G（"Upgradeable to 10G"），550W 电源/380W 预算 <<<PAGE 14>>>/<<<PAGE 36>>>
- **OS6360-48**：48×RJ45 非 PoE + 2 combo + 2×SFP+，120W 内置电源 <<<PAGE 14>>>/<<<PAGE 38>>>
- **OS6360-P48**：48 口 802.3at PoE，550W 电源，PoE 预算 350W <<<PAGE 14>>>/<<<PAGE 40>>>
- **OS6360-P48X**：46 口 at + 2 口多千兆 802.3bt（2.5G）+ 10G combo，950W 电源，PoE 预算 760W <<<PAGE 14>>>/<<<PAGE 42>>>
- **OS6360-PH48**：P48X 同级且 combo 口可升级 10G，950W 电源/760W 预算 <<<PAGE 15>>>/<<<PAGE 44>>>

## 端口与面板（Ch3）

- **Combo 口**：RJ45 与 SFP/SFP+ 共享的上联口对（25-26/49-50），两种介质二选一 <<<PAGE 30>>>
- **VFL 口**：SFP+ 软件可配口的第二角色（Virtual Fabric Link），端口 LED 琥珀色指示 <<<PAGE 13>>>/<<<PAGE 46>>>
- **SFP+ software configurable ports**：可在 1G SFP 上行与 10G SFP+/VFL 之间软件切换的上联口 <<<PAGE 13>>>
- **Chassis Grounding Lug**：后面板接地耳，配 Panduit LCD8-10A-L、8AWG 铜线、30-60 in-lb 扭矩 <<<PAGE 55>>>
- **Tmra（Maximum Rated Ambient Temperature）**：最大额定环境温度（全家族 0-45°C），机架内需按温升折减 <<<PAGE 27>>>/<<<PAGE 46>>>
- **Chassis vs Ambient Temperature**：机箱温度=内置传感器读数（阈值判断用），环境温度≈室温，前者通常更高 <<<PAGE 27>>>
- **OK LED**：绿=诊断与 AOS 启动 OK；闪绿=进行中；琥珀=系统/风扇/温度故障 <<<PAGE 45>>>
- **VC LED**：闪绿=VC Master、闪琥珀=Slave，闪烁次数即节点 ID；灭=关机或非 VC 成员 <<<PAGE 45>>>
- **PWR LED**：绿=12V 主电正常；稳琥珀=12V 故障；闪琥珀=54V/PoE 故障；灭=电源不在位 <<<PAGE 45>>>

## 安装部件与套件（Ch3）

- **Blank Cover Panel**：空槽盲板，箭头朝上安装；调节气流并保护内部元件，须常装 <<<PAGE 47>>>/<<<PAGE 48>>>
- **Rack Mount Flange**：免工具卡扣式机架法兰（弹簧夹 out/in 位 + "CLICK" 锁定 + 螺丝固定）<<<PAGE 49>>>
- **OS6360-RM-19-L**：半宽机型 19" 机架 L 支架套件 <<<PAGE 52>>>
- **OS6360-WALL-MNT**：10/P10 壁挂套件（四托架朝下，紧固件自备）<<<PAGE 53>>>/<<<PAGE 54>>>
- **Rubber feet**：桌面安装用四只橡胶脚垫（包装内附）<<<PAGE 51>>>
- **Relay Rack**：中继机架，需按机架厂商规范安装固定 <<<PAGE 49>>>/<<<PAGE 52>>>

## PoE 体系（Ch4）

- **PoE（Power over Ethernet）**：通过以太网口在线供电，PoL/Inline Power 为同义词 <<<PAGE 58>>>
- **PD（Powered Device）**：受电设备（IP 话机/AP/摄像头等），以太网缆为唯一电源 <<<PAGE 58>>>
- **PSE（Power Source Equipment）**：供电设备，负责检测 PD、分级、按需供电与回收 <<<PAGE 58>>>
- **PoE Budget**：整机 PoE 功率预算，按机型 120-760W <<<PAGE 60>>>
- **PoE Class Detection**：PD 分级检测（Class 0-8：15.4/4.0/7.0/15.4/30/45/60/75/90-99W），默认关闭，开启会复位全部 PoE 口 <<<PAGE 61>>>/<<<PAGE 62>>>
- **802.3bt**：bt 标准（Class 5-8，双 Type），`lanpower 8023bt` 使能 <<<PAGE 62>>>
- **4pair（PoH）**：4 对供电模式，支持 60/75/95W 每口，`lanpower 4pair` 使能 <<<PAGE 62>>>
- **Fast PoE**：上电数秒即供电（PoE 默认态固化于 FPGA、配置存控制器 EEPROM），不等 AOS 启动完成 <<<PAGE 63>>>
- **Perpetual PoE**：软重启/重载期间 PD 供电不间断（MCU 固件升级除外）<<<PAGE 63>>>
- **Guard Band**：保护带拒载机制——剩余预算低于端口上限或 PD 类最大值即拒绝新 PD <<<PAGE 65>>>
- **Priority Disconnect**：预算不足时按端口优先级+物理端口号裁决新 PD 供电资格的机制（默认启用）<<<PAGE 66>>>
- **Port Priority**：端口优先级 low（默认）/high/critical 三级 <<<PAGE 64>>>
- **Capacitor Detection**：电容检测法，仅供 legacy IP 话机、不符 IEEE，默认禁用 <<<PAGE 65>>>
- **2pair 模式标记**：show lanpower 输出端口 maxpower 后缀 `*` 表示 4pair 口运行在 2pair 模式 <<<PAGE 61>>>

## CLI 命令（Ch2-Ch4）

- **show module / show module long**：查看槽位基本/详细信息 <<<PAGE 55>>>/<<<PAGE 56>>>
- **show temperature**：查看温度传感器 Current/Range/Danger/Thresh/Status <<<PAGE 56>>>
- **show powersupply**：查看电源类型与状态（Total Power/Type/Status/Location）<<<PAGE 60>>>
- **show lanpower slot**：查看逐口 PoE 状态与槽预算 <<<PAGE 61>>>/<<<PAGE 68>>>
- **lanpower slot service**：slot 级 PoE 启停（start/stop），首次激活必用 <<<PAGE 62>>>
- **lanpower port admin-state**：端口级 PoE 使能/禁用（仅复活已断电口，不能首次激活）<<<PAGE 62>>>
- **lanpower port power**：设置端口最大功率（mW）<<<PAGE 63>>>
- **lanpower slot maxpower**：设置槽级最大功率（W）<<<PAGE 64>>>
- **lanpower port priority**：设置端口优先级（low/high/critical）<<<PAGE 64>>>
- **lanpower slot priority-disconnect**：启用/禁用优先级断电 <<<PAGE 66>>>
- **lanpower slot class-detection**：启用分级检测（复位全 PoE 口）<<<PAGE 62>>>
- **aaa authentication**：解锁会话类型（default local 全解；telnet/http/ftp 单类）<<<PAGE 22>>>
- **write memory**：保存配置 <<<PAGE 24>>>
- **system timezone / system time / system date**：时区/DST、时间、日期设置 <<<PAGE 23>>>
- **system contact / system name / system location**：管理联系人/系统名/位置 <<<PAGE 23>>>
- **show system**：查看当前系统配置改动 <<<PAGE 24>>>

## 安全与法规（附录 A）

- **CDE（Cable Discharge Event）**：线缆静电放电事件，Cat5e/6/6a 布线接端口前应先对地放电 <<<PAGE 18>>>
- **ESD / Wrist Strap**：静电放电与防静电腕带（触件前必须消除人身与周围静电）<<<PAGE 81>>>
- **Class 1M Laser**：开盖时 1M 类激光辐射，勿用光学仪器直视 <<<PAGE 77>>>
- **Restricted Access Location**：受限访问场所（钥匙/安保限服务人员进入）<<<PAGE 81>>>
- **WEEE**：欧盟废弃电子电气设备指令，产品报废需单独回收处理 <<<PAGE 70>>>
- **RoHS**：有害物质限制（中/台罗表）<<<PAGE 71>>>/<<<PAGE 72>>>
- **California Proposition 65**：加州 65 号提案铅暴露警告 <<<PAGE 73>>>
- **Hi-Pot Test**：耐压测试（所有以太网口 2250V DC）<<<PAGE 75>>>
- **Class A 数字设备**：FCC/VCCI/BSMI Class A，仅限商业环境，住宅使用可能产生干扰 <<<PAGE 75>>>/<<<PAGE 77>>>

## 通用概念（Ch1-Ch2）

- **Hot-Swapping**：不断电增删更换部件的能力 <<<PAGE 15>>>
- **Hardware Monitoring**：内置传感器自动监控 + LED 视觉状态 + 用户 show 命令三层 <<<PAGE 15>>>/<<<PAGE 16>>>
- **Trap**：超阈值等错误事件自动发送并打印到控制台的消息 <<<PAGE 15>>>/<<<PAGE 56>>>
- **Warning / Danger Threshold**：温度警告阈值（发 trap 不停机）/危险阈值（自动关机、不可配）<<<PAGE 56>>>/<<<PAGE 57>>>
- **UPS**：不间断电源，PoE+IP 话机场景强制建议（911 要求）<<<PAGE 58>>>
- **STP/UTP**：屏蔽/非屏蔽双绞线；室外或近交流线路建议 STP Cat5e+ <<<PAGE 18>>>

---
合计：约 62 条。
