# principles — OmniSwitch 6860/6860E/6860N Hardware Users Guide（硬件机制/架构/规格要点候选）

格式：编号 P# ｜ 要点 ｜ 页码（fulltext.md 真实 `<<<PAGE N>>>` 标记）

## 家族三代架构

- **P1** 家族三代 15 机型：基础 OS6860（24/48/P24/P48：24/48 千兆 + 4×SFP+ + 2×20G VC 口）；增强 E（24/48/U28/P24/P48/P24Z8："Includes a built-in co-processor for Enhanced network services"+后面板 EMP）；下一代 N（U28/P48Z/P48M/P24Z/P24M：QSFP28 VFL + SFP28 25G 上联，M 型带上联模块槽）——同代 1U 44cm 包络三代演进 <<<PAGE 14>>>/<<<PAGE 15>>>
- **P2** E 增强机制："Includes a built-in co-processor for Enhanced network services"——外部 CPU 独立诊断/启动，对应 OK2 LED（"External CPU Diagnostics and AOS bootup OK"）+ 后面板 EMP 带外口 <<<PAGE 14>>>/<<<PAGE 22>>>/<<<PAGE 59>>>
- **P3** 20G VC 口体系：基础/E 代统一"(2) 20G Virtual Chassis link ports"；N 代升级为"(2) QSFP28 (VFL)"——VC 堆叠链路带宽代际翻倍路径 <<<PAGE 14>>>/<<<PAGE 48>>>/<<<PAGE 50>>>
- **P4** HPoE 非 bt 合规注记：E-P24/E-P48 的口 1-4 为"HPoE (60W - not 802.3bt compliant)"、E-P24Z8 的 17-24 为"(75W HPoE Ports - not 802.3bt compliant)"——私有 60/75W 高功率，早于 bt 标准的遗留实现 <<<PAGE 43>>>/<<<PAGE 45>>>/<<<PAGE 46>>>
- **P5** E-P24Z8 混合阵列：16×10/100/1000 at + 8×100/1000/2.5G 75W HPoE——同机 2.5G 多千兆与 HPoE 叠加的最早期形态 <<<PAGE 46>>>
- **P6** N 代 bt 95W 全面化：N-P48Z=36×bt 60W + 12×100M-5G bt 95W（37-48）；N-P48M=36×2.5G bt 95W + 12×100M-10G bt 95W + 上联槽；N-P24Z=12×bt 60W + 12×多千兆 95W；N-P24M=24×100M-10G bt 95W 全口最高档 <<<PAGE 50>>>/<<<PAGE 51>>>/<<<PAGE 53>>>/<<<PAGE 55>>>
- **P7** N 型 25G 上联体系：SFP28（1G/10G/25G）四口组（U28 31-34、P48Z/P24Z 51-54/27-30）+ QSFP28 VFL 两口；上联模块 M 型四选（OS68-XNI-U4 4×SFP+ / QNI-U2 2×QSFP+ 40G / VNI-U4 4×SFP28 / CNI-U1 1×QSFP28 40G/100G）<<<PAGE 48>>>/<<<PAGE 56>>>-<<<PAGE 58>>>
- **P8** 全家族统一环境包络：Tmra 0-45°C、海拔 13000ft、存储 -40~85°C、湿度 5-95%——机房级（比 6575 工业级窄）<<<PAGE 30>>>-<<<PAGE 56>>>
- **P9** 功耗梯度（满系统功率）：24=46W→48=57W→E24=48W→E48=60W→EU28=73W→P24=75W→P48=89W→E-P24=76W→E-P48=93W→E-P24Z8=48W→N-U28=143W→N-P48Z=147W→N-P24Z=142W→N-P48M=260W→N-P24M=176W——N 代多千兆+25G 使功耗翻两番 <<<PAGE 30>>>-<<<PAGE 56>>>
- **P10** 深度双包络：基础/E=35cm；N 型 M/Z=44cm（P48Z/P48M/P24Z/P24M）——深机箱需后支架辅助；最大整备重量 N-P48M 8.5kg <<<PAGE 30>>>/<<<PAGE 52>>>/<<<PAGE 20>>>

## 面板与 LED 机制

- **P11** 控制台三连接器：console（Micro USB-to-USB 线随机附带）+ USB（ALE U 盘/蓝牙 dongle，不随机）+ RS-232——N 型另加 EMP <<<PAGE 15>>>/<<<PAGE 21>>>
- **P12** N 型 console 波特率分化：9600（基础/E）vs 115200（6860N models）——升级终端仿真参数 <<<PAGE 22>>>
- **P13** PS LED 五态语义（按电源在场数细分）：稳绿 a=双电均正常/b=单电正常（另一舱空或装风扇托盘）；稳琥珀 a=双电一或全故障/b=单电故障；灭=无电源——含"fan tray 占舱"场景 <<<PAGE 59>>>
- **P14** BPS LED 遗留：绿=备份电源正常/琥珀=有故障运行/灭=不在位——对应已停支持的 OS-BPS 槽位 <<<PAGE 59>>>
- **P15** OK2 双系统灯（E 独有）：稳绿=External CPU 诊断与 AOS 启动 OK/闪绿=诊断进行中/稳琥珀=失败——主协处理器双启动状态分离 <<<PAGE 59>>>
- **P16** 6860N 五色端口 LED 制：绿=千兆链路、琥珀=PoE、蓝=2.5G（LED1，可降频闪烁）、蓝+黄=5G、品红=10G；LED2 琥珀=PoE Active——速率与 PoE 双灯多维显示；VFL/Uplink 口绿=uplink/琥珀=VFL <<<PAGE 60>>>
- **P17** 开机正常 LED 快查表：OK1 绿+PRI 绿（master）或琥珀（slave）+PS 绿+BPS 绿+GRN 绿+OK2 绿（E）——任一不符先确认启动完成再报修 <<<PAGE 23>>>

## 安装机制

- **P18** 气流间隙规范：前 6"/后 6"/侧 2"，顶部与底部免间隙（"Clearance is not required at the top and bottom of the chassis"）——侧进风设计的机架友好形态 <<<PAGE 21>>>/<<<PAGE 61>>>/<<<PAGE 62>>>
- **P19** 弹簧夹法兰机制（与 6360/6560 同构）：clip 置 out→tab 入机箱槽→按压至"CLICK"锁定→附带螺丝固定→对侧重复；N-P48Z/P48M 加 rear bracket guide+rear bracket（支架总长 26.4 in）<<<PAGE 64>>>/<<<PAGE 65>>>/<<<PAGE 67>>>
- **P20** 盲板气流机制："When blank cover panels are missing, air does not take the direct route from the air intake vents... an extra task is placed on the power supply fans"——缺盲板迫使电源风扇超负荷；箭头朝上安装 <<<PAGE 62>>>/<<<PAGE 63>>>
- **P21** 桌面安装纪律：四橡胶脚垫入底板孔+"right side up"摆放——"Never attempt to operate a switch while it is placed on its top or side." <<<PAGE 68>>>

## 电源体系

- **P22** 七款电源矩阵：非 PoE=OS6860-BP 150W AC / BP-D 150W DC（24/E24/48/E48/EU28/N-U28）；PoE=BP-PH 600W / BP-PX 920W（P24/E-P24/E-P24Z8 与 P48/E-P48/E-P24Z8）；N 专属=N-BPPH 600W / N-BPPX 920W / N-BPXL 2000W（四 N-PoE 机型，XL 仅 P48M/P24M）<<<PAGE 69>>>
- **P23** 不支持电源即禁口机制："Inserting an unsupported power supply will result in the switching and PoE ports being disabled until the correct power supply is inserted."——硬件级防呆 <<<PAGE 69>>>
- **P24** N 电源软件门槛："OS6860N power supplies are supported beginning with AOS release 8.7R1." <<<PAGE 69>>>
- **P25** 2000W 电源双电压降额：100-120VAC 输入=1000W/18.35A；200-240VAC=2000W/36.7A——大功率电源必须 230V 市电才满额（C19 电源线）<<<PAGE 77>>>
- **P26** 混插双规则：BP-D 与 BP（均 150W）可同箱（"Mixing the OS6860-BP-D with the OS6860-BP in the same chassis is supported."）；其余"Mixing different wattage power supplies in a chassis is not supported."冗余电源须同型号负载分担 <<<PAGE 71>>>/<<<PAGE 73>>>
- **P27** 电源 LED 双制：BP/BP-D/PH/PX 单 LED 六态（稳绿/闪绿待机/闪红邻舱有电/闪绿红告警/稳红故障/灭全停）；N-BPPH/N-BPPX/N-BPXL 双灯 AC OK+DC OK（各绿/红）<<<PAGE 72>>>-<<<PAGE 78>>>
- **P28** 无电源开关语义："The OS6860 does not provide an on/off switch. Connecting an installed power supply to a power source will boot the switch." <<<PAGE 69>>>
- **P29** 双电源舱 1+1 架构："The OS6860 chassis provides two bays for 1+1 redundant hot-swappable power supplies."非 PoE 机型可在一个 150W 电源位换单个可选风扇托盘 <<<PAGE 15>>>
- **P30** 风扇托盘定位："The OS6860 FANTRAY NONPOE provides supplemental system cooling for non-PoE OS6860 switches connected to the OmniSwitch Backup Power Shelf/System (BPS)."——与 BPS 配套的补充散热；绿=正常/灭=关或故障 <<<PAGE 85>>>

## DC 接线与接地

- **P31** DC 供电五前提：可靠接地 -48VDC SELV 源、15A 支路过流保护、12AWG 铜线、易达断路装置、受限场所；CBN 共模网络+DC-1 隔离回流；三芯绿黄=地/黑=return/红=-48VDC <<<PAGE 78>>>/<<<PAGE 79>>>
- **P32** 机箱 supplemental 接地：后部接地耳 10-32 螺丝+无漆区，Panduit LCD8-10A-L+8AWG 铜线，力矩 30-60 in-lb；DC 场景后板双接地孔同规格 <<<PAGE 78>>>/<<<PAGE 83>>>

## 监控与 Dying Gasp

- **P33** show temperature 按 VC 逐机箱逐传感器：例 1/CMMA（15-93/Danger 93/Thresh 96）与 2/CMMA（15-85/85/88）并列——堆叠内每台独立阈值 <<<PAGE 87>>>
- **P34** 温度双阈值行为：Warning 超限发 trap 不停机（查气流/室温）；Danger 超限关机待手动重启且"factory-set and cannot be configured by the user" <<<PAGE 87>>>
- **P35** DG 三通道：SNMP trap（前 3 站：槽号/主备/时间）+ Syslog"Dying Gasp Power Failure Event Occurred"（前 3 服务器）+ 4×802.3ah OAM PDU（DG 位置位，上联口优先）<<<PAGE 69>>>/<<<PAGE 70>>>
- **P36** DG PDU 端口挤占公式（本书独有）："The maximum number ports which can send out a dying gasp PDU simultaneously is limited to ten ports minus the number of Syslog/SNMP servers configured."（例：2 SNMP+1 Syslog→最多 7 口）——电容余量下通告通道资源分配 <<<PAGE 70>>>

## PoE 机制

- **P37** PoE 规格全栈：IEEE 802.3/af/at/bt；逐机型口功率域——6860=全口 3000-30000mW；E=口 1-4 3000-60000/其余 30000；E-P24Z8=1-16 30000/17-24 至 75000；N-P48Z=1-36 至 60000/37-48 至 95000；N-P48M/P24M=全口至 95000；N-P24Z=1-12 60000/13-24 95000 <<<PAGE 91>>>
- **P38** N 型预算矩阵：P48Z：1×600W=360W/2=900W，1×920W=660W/2=1500W（2000W 不支持）；P48M：1×2000W(115V)=665W、(230V)=1570W，2×(230V)=3390W（最高）；P24Z：512/960、705/1545；P24M：385/935、680/1515、750/1600、1660/2280 <<<PAGE 93>>>
- **P39** Fast PoE 机制："the default state of the PoE subsystem is set to enabled in the FPGA image and the PoE configuration is stored in the controller EEPROM"——上电数秒即供电，不等启动完成 <<<PAGE 96>>>
- **P40** Perpetual PoE 机制："provide uninterrupted power to connected power devices (PD) even when the switch is rebooting or reloading, such as on a soft reset"——软重启不断 PD 电 <<<PAGE 96>>>
- **P41** priority disconnect 电源档上限："For OS6860 switches using 920W power supplies, priority disconnect supports up to a maximum of 780W of PoE power (per power supply installed). For switches using 600W power supplies... up to a maximum of 450W" <<<PAGE 99>>>
- **P42** 物理口号优先级方向（注意与其他家族相反）："OS6860 Physical Port - 24 Port Models: 24 (Highest) -> 1 (Lowest)；48 Port Models: 48 (Highest) -> 1 (Lowest)"——端口号越大优先级越高 <<<PAGE 100>>>
- **P43** PoE power-rule 定时机制："The lanpower power-rule command allows user to set additional rules for PoE power (e.g., setting PoE to turn on or off on specific dates or at specific times)." <<<PAGE 98>>>
- **P44** Guard Band 与 Priority Disconnect 四情形规则同家族：剩余预算 < 口 maxpower 即拒新 PD（调低口上限解锁）；禁用/同级按物理口号/新 PD 最高级抢最低级/新 PD 最低级被拒 <<<PAGE 99>>>-<<<PAGE 101>>>/<<<PAGE 102>>>
- **P45** 911/UPS 纪律："PoE-enabled switches with attached IP telephones should have operational power supply redundancy at all times for 911 emergency requirements... plugged into an Uninterruptible Power Source (UPS)." <<<PAGE 89>>>

---
合计：45 条（P1-P45）。
