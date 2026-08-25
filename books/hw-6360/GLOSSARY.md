# GLOSSARY — OmniSwitch 6360 Hardware Users Guide 核心术语

从 verified 术语库精选 50 条，按主题分组。型号/部件号/命令保留英文，页码为原书页码。

## 机型（Ch1/Ch3）

- **OS6360-10**：10 口非 PoE 半宽 1U，10×RJ45+2×SFP，30W 内置电源，无风扇（<<<PAGE 13>>>）
- **OS6360-P10**：8 口 802.3at PoE+2 非 PoE+2×SFP，165W 电源，预算 120W（<<<PAGE 13>>>/<<<PAGE 28>>>）
- **OS6360-P10A-US**：PN 904324-90 的 P10 变体，不支持 Fast/Perpetual PoE（<<<PAGE 28>>>）
- **OS6360-24**：24×RJ45 非 PoE+2 combo+2×SFP+，65W 电源，无风扇（<<<PAGE 13>>>/<<<PAGE 30>>>）
- **OS6360-P24**：24 口 at PoE，260W 电源，预算 180W（<<<PAGE 13>>>/<<<PAGE 32>>>）
- **OS6360-P24X**：24 口 at+2×SFP+ combo，550W 电源，预算 380W，带风扇（<<<PAGE 14>>>/<<<PAGE 34>>>）
- **OS6360-PH24**：P24X 同级且 combo 可软件升 10G（<<<PAGE 14>>>/<<<PAGE 36>>>）
- **OS6360-48**：48×RJ45 非 PoE+2 combo+2×SFP+，120W 电源（<<<PAGE 14>>>/<<<PAGE 38>>>）
- **OS6360-P48**：48 口 at PoE，550W 电源，预算 350W（<<<PAGE 14>>>/<<<PAGE 40>>>）
- **OS6360-P48X**：46 口 at+2 口多千兆 bt（2.5G）+10G combo，950W 电源，预算 760W（<<<PAGE 14>>>/<<<PAGE 42>>>）
- **OS6360-PH48**：P48X 同级且 combo 可升级 10G（<<<PAGE 15>>>/<<<PAGE 44>>>）

## 端口与面板（Ch3）

- **Combo 口**：RJ45 与 SFP/SFP+ 共享上联口对（25-26/49-50），二介质二选一（<<<PAGE 30>>>）
- **SFP+ software configurable ports**：1G SFP 上行与 10G SFP+/VFL 间软件切换（<<<PAGE 13>>>）
- **VFL 口**：SFP+ 口第二角色（Virtual Fabric Link），端口 LED 琥珀指示（<<<PAGE 13>>>/<<<PAGE 46>>>）
- **OK LED**：绿=启动正常/闪绿=进行中/琥珀=系统/风扇/温度故障（<<<PAGE 45>>>）
- **VC LED**：闪绿=Master、闪琥珀=Slave，闪烁次数即节点 ID（<<<PAGE 45>>>）
- **PWR LED**：绿=12V 正常/稳琥珀=12V 故障/闪琥珀=54V/PoE 故障/灭=无电源（<<<PAGE 45>>>）
- **Chassis Grounding Lug**：后面板接地耳，Panduit LCD8-10A-L、8AWG、30-60 in-lb（<<<PAGE 55>>>）
- **Tmra**：最大额定环境温度，全家族 0-45°C，机架内按温升折减（<<<PAGE 27>>>/<<<PAGE 46>>>）
- **Chassis vs Ambient Temperature**：机箱传感器温度（阈值判断用）恒高于室温（<<<PAGE 27>>>）

## 安装部件（Ch3）

- **Blank Cover Panel**：空槽盲板，箭头朝上，调节气流须常装（<<<PAGE 47>>>/<<<PAGE 48>>>）
- **Rack Mount Flange**：免工具卡扣法兰（弹簧夹 out/in+CLICK+螺丝）（<<<PAGE 49>>>）
- **OS6360-RM-19-L**：半宽机型 19" 机架 L 支架套件（<<<PAGE 52>>>）
- **OS6360-WALL-MNT**：10/P10 壁挂套件，紧固件自备（<<<PAGE 53>>>/<<<PAGE 54>>>）

## PoE 体系（Ch4）

- **PoE/PoL/Inline Power**：以太网在线供电同义术语（<<<PAGE 58>>>）
- **PD / PSE**：受电设备 / 供电设备（<<<PAGE 58>>>）
- **PoE Budget**：整机 PoE 预算，按机型 120-760W（<<<PAGE 60>>>）
- **PoE Class Detection**：Class 0-8 分级（15.4-99W），默认关，开启复位全 PoE 口（<<<PAGE 61>>>/<<<PAGE 62>>>）
- **802.3bt**：bt 标准（Class 5-8），`lanpower 8023bt` 使能（<<<PAGE 62>>>）
- **4pair（PoH）**：4 对供电，60/75/95W 每口（<<<PAGE 62>>>）
- **Fast PoE**：上电数秒即供电，PoE 默认态固化于 FPGA（<<<PAGE 63>>>）
- **Perpetual PoE**：软重启期间供电不间断（MCU 固件升级除外）（<<<PAGE 63>>>）
- **Guard Band**：剩余预算低于口上限即拒新 PD 的保护带机制（<<<PAGE 65>>>）
- **Priority Disconnect**：预算不足时按优先级+物理端口号（1 高 48 低）裁决新 PD（<<<PAGE 66>>>）
- **Port Priority**：low（默认）/high/critical 三级（<<<PAGE 64>>>）
- **Capacitor Detection**：电容检测，仅 legacy IP 话机、不符 IEEE（<<<PAGE 65>>>）
- **UPS / 911 纪律**：IP 话机 PoE 交换机须保持电源冗余并接 UPS（<<<PAGE 58>>>）

## CLI 命令（Ch2-Ch4）

- **show module / show module long**：槽位基本/详细信息（<<<PAGE 55>>>/<<<PAGE 56>>>）
- **show temperature**：传感器 Current/Range/Danger/Thresh/Status（<<<PAGE 56>>>）
- **show powersupply**：电源类型与状态（<<<PAGE 60>>>）
- **show lanpower slot**：逐口 PoE 状态与槽预算（<<<PAGE 61>>>/<<<PAGE 68>>>）
- **lanpower slot service**：slot 级 PoE 启停，首次激活必用（<<<PAGE 62>>>）
- **lanpower port admin-state**：端口级使能/禁用，仅复活已断电口（<<<PAGE 62>>>）
- **lanpower port power / slot maxpower**：口（mW）/槽（W）最大功率上限，不预留（<<<PAGE 63>>>/<<<PAGE 64>>>）
- **lanpower port priority**：端口优先级设置（<<<PAGE 64>>>）
- **lanpower slot priority-disconnect**：优先级断电开关（<<<PAGE 66>>>）
- **lanpower slot class-detection**：分级检测使能（复位全口）（<<<PAGE 62>>>）
- **aaa authentication**：会话类型解锁（一次一类）（<<<PAGE 22>>>）
- **system timezone/time/date、system contact/name/location**：时间与可选系统参数（<<<PAGE 23>>>）
- **write memory / show system**：保存 / 查看配置（<<<PAGE 24>>>）

## 监控与安全（Ch1-Ch2/附录 A）

- **Hot-Swapping**：不断电增删更换部件（<<<PAGE 15>>>）
- **Trap**：超阈值等错误事件自动发送并打印控制台（<<<PAGE 15>>>/<<<PAGE 56>>>）
- **Warning/Danger Threshold**：温度警告（trap 不停机）/危险（自动关机不可配）双阈值（<<<PAGE 56>>>/<<<PAGE 57>>>）
- **CDE（Cable Discharge Event）**：线缆静电放电，接线前先对地放电（<<<PAGE 18>>>）
- **ESD / Wrist Strap**：静电放电与防静电腕带（<<<PAGE 81>>>）
- **Class 1M Laser**：开盖激光辐射勿直视（<<<PAGE 77>>>）
- **Class A 数字设备**：仅限商业环境，住宅禁用（<<<PAGE 75>>>/<<<PAGE 77>>>）
- **Restricted Access Location**：受限访问场所（<<<PAGE 81>>>）
