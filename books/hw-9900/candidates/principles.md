# principles — OmniSwitch 9900 Series Hardware Users Guide（硬件机制/架构/规格要点候选）

格式：编号 P# ｜ 要点 ｜ 页码（fulltext.md 真实 `<<<PAGE N>>>` 标记）

## 机箱架构

- **P1** 双机箱规格：OS9907 为 11RU（7 槽=2 CMM+5 NI，49.02×44.2×58.42cm，32.83kg）；OS9912 为 17RU（12 槽=2 CMM+10 NI，76.57cm 高，64.36kg）——同深 23 英寸、同环境包络（0-45°C、湿度 10-90%、海拔 4000m）<<<PAGE 5>>>/<<<PAGE 6>>>/<<<PAGE 11>>>
- **P2** OS9907 slot2 双角色设计："Slot 2 Supports a CMM (for 1+1 CMM redundancy) or NI module (to maximize port count)"——但要性权衡："when an NI is installed in slot 2, CMM redundancy is not provided." <<<PAGE 7>>>/<<<PAGE 16>>>
- **P3** slot2 NI 半速陷阱（9907）："When an XNI module (i.e. OS99-XNI-U48) is inserted in slot 2 only the first 8 ports will be active."（slot2 兼容 CMM 的架构代价）<<<PAGE 7>>>
- **P4** CFM 藏于风扇之后："CFMs are located behind the chassis fan trays. To access a CFM, remove the fan tray in front of the module."（CFM1/2 可用，CFM3/4 预留未激活）<<<PAGE 10>>>/<<<PAGE 15>>>/<<<PAGE 20>>>
- **P5** 电源 N+1 负载分担："Slots PS1 through PS4 Support up to four load-sharing chassis power supplies, offering N+1 redundancy." <<<PAGE 8>>>/<<<PAGE 13>>>
- **P6** 风扇 N+1 与单向气流：3 风扇托盘常驻（9907 每托 3 风扇、9912 每托 5 风扇）、Airflow Direction "Front-to-back only"（与 6900 的双向气流不同）；功耗 112W/200W <<<PAGE 9>>>/<<<PAGE 14>>>/<<<PAGE 28>>>
- **P7** 拇指螺丝材质过渡："Modules are transitioning to ship with aluminum-headed thumbscrews instead of violet color, plastic thumbscrews. The thumbscrews are mechanically identical and only differ in color."（现场识别勿困惑）<<<PAGE 6>>>/<<<PAGE 12>>>
- **P8** ESD 双接地点：机箱前部 Wrist Strap Grounding Connector + 后部 Grounding Block；ESD 腕带生效前提是电源已装并接接地插座 <<<PAGE 8>>>/<<<PAGE 9>>>/<<<PAGE 72>>>

## CMM 管理模块机制

- **P9** CMM 职责："The CMM manages system functions in the chassis. This includes controlling and monitoring NIs, fabric modules (CFMs) and power distribution."；OS99-CMM 带 2×40G QSFP+ 上行，功耗 64W <<<PAGE 16>>>
- **P10** CMM2 升级版：4×100G QSFP28 上行/VFL 口，功耗 74W；版本门槛——"The OS99-CMM2 requires a minimum AOS version of 8.10R2 and cannot be mixed with the existing OS99-CMM in the same chassis." <<<PAGE 17>>>
- **P11** CMM 双 console：RJ45 + Micro-USB（需装驱动）；EMP RJ45 10/100/1000 带外管理 + USB Type A 存储口 <<<PAGE 16>>>/<<<PAGE 17>>>
- **P12** CMM LED 组合诊断语义：PRI（稳绿=主/闪绿=备/稳黄=停运/闪黄=软件升级中）；VC（稳蓝=Master/稳黄=Slave）；FAB 闪黄=CFM 电源故障或 PCIe 上报失败（NI 全断电但仍可 console/EMP 登录）；PRI/VC/FAB/PS/TEMP 五灯同时闪黄=全部 CFM PCIe 硬链路失效（主 CMM 拒绝登录、console 每 5 秒报 "PCIe link failure"）<<<PAGE 18>>>
- **P13** QSFP 上行 LED 多维编码：Off=管理 Down 或无收发器；绿(A)=40G/100G；绿(A/B/C/D)=4X10G/4X25G 分支；蓝=VFL；白=QSFP28 特殊态 <<<PAGE 19>>>

## 交换矩阵（CFM）机制

- **P14** CFM 带宽叠加模型："Each CFM installed provides additional fabric bandwidth to chassis management and the Network Interface (NI) modules."；带宽阶梯：OS9907-CFM=2.56 Tbps、OS9907-CFM2=12.8 Tbps（需 AOS ≥8.9R1、不可与 CFM 混插）、OS9912-CFM=25.6 Tbps；功耗 119W/119W/222W <<<PAGE 20>>>/<<<PAGE 21>>>
- **P15** CFM 经中板连接："The modules connect to the chassis mid-plane and are located just behind the system fan trays."（NI 走背板、CFM 走中板）<<<PAGE 20>>>/<<<PAGE 36>>>等
- **P16** OS9907 组合兼容矩阵：CMM+CMM/CFM+CFM=支持；CMM+CMM/CFM2+CFM2=支持；CMM2+CMM2/CFM2+CFM2=支持；其余三种组合（CFM 与 CFM2 混插、CMM2 配旧 CFM、CMM 与 CMM2 混插）均 Not Supported <<<PAGE 22>>>
- **P17** VC-of-2 双机箱虚拟化：9907 支持两机箱互联，仅三种对等组合支持（CMM+CFM ↔ CMM+CFM；CMM+CFM2 ↔ CMM+CFM2；CMM2+CFM2 ↔ CMM2+CFM2），"All other combination Not Supported" <<<PAGE 22>>>

## NI 模块体系

- **P18** 11 种 NI 模块谱系：铜口（XNI-48 1/10GBaseT 402W、GNI-48 千兆 56W）；光口（XNI-U48 48×SFP+ 305W、GNI-U48 48×SFP 70W、XNI-U24 24×SFP+ 153W）；PoE（GNI-P48 48 口 PoE+8×HPoE 54W、XNI-P48Z16 32 口 at+16 口多千兆 at 402W、XNI-P24Z8 16+8 口 187W、XNI-UP24Q2 12×SFP+ +12×HPoE 多千兆+2×QSFP+ 117W）；高速（CNI-U8 8×QSFP28 117W、CNI-U20 20×100G 314W、XNI-U12Q 12×SFP+ +1×QSFP+）<<<PAGE 23>>>-<<<PAGE 26>>>
- **P19** HPoE 口规则（PoE 模块通用）："Ports 1 through 8 support HPoE (75W). These ports are labeled 'HPoE' on the chassis front panel."（前 8 口为大功率口）<<<PAGE 24>>>
- **P20** 9912 不支持的 NI 清单：XNI-P48Z16、XNI-P24Z8、XNI-UP24Q2、XNI-U12Q 均标注 "Not supported in an OS9912 chassis."（选型必查）<<<PAGE 24>>>/<<<PAGE 25>>>/<<<PAGE 26>>>
- **P21** CNI-U20 分支口："13-20 support splitter function"（100G 口可分支）<<<PAGE 26>>>
- **P22** NI 模块 LED 体系：背光状态 LED（稳蓝=HW OK/闪蓝=启动中或故障）；Speed LED（稳绿=HW OK/闪绿=SW 心跳正常/稳黄=SW 故障/稳红=HW 故障）；端口 LED 绿=非 PoE 链路、黄=PoE 链路（PoE 模块）<<<PAGE 27>>>

## 电源与功率机制

- **P23** 双电源型号：OS99-PS-A（AC，100-240V 输入，输出两档 1200W/21.4A 或 3000W/53.5A）；OS99-PS-D（DC，-40~-72V 输入 75A，输出 2500W/44.6A@56V）；均热插拔、均为 System+PoE 供电 <<<PAGE 29>>>/<<<PAGE 30>>>
- **P24** 电源三不混："Mixing of AC and DC power supplies is not supported. Mixing of Hi (240VAC) and Low (110VAC) input is not supported."（与 6900 的 AC+DC 可混相反）<<<PAGE 29>>>/<<<PAGE 63>>>
- **P25** 分路保护建议："ALE recommends using circuit breakers that are rated for 30A (AC) and 110A (DC) per power supply."（DC 侧实接规范另有 75A 过流 + 双 10AWG 导体）<<<PAGE 29>>>/<<<PAGE 30>>>
- **P26** 机箱功率预算动态机制："As soon as a component is inserted and its connectors make contact with the chassis mid-plane, additional power requirements take effect. If there is not adequate power, the incoming component may not power on."——加模块/拔电源前必须 `show chassis` 查 Power Left（例：2041W 可用）<<<PAGE 49>>>
- **P27** DC 长线与连接器规范：DC 线 >3m 属本地规范管辖（联系电工与 AHJ）；须配 FCI 10080598-2ED0006LF 4P PWRBLADE 连接器 <<<PAGE 31>>>
- **P28** 冗余 AC 分电路原则："It is recommended that each AC outlet resides on a separate circuit." <<<PAGE 33>>>

## PoE 机制

- **P29** PoE 模块四件套：GNI-P48、XNI-P48Z16、XNI-P24Z8、XNI-UP24Q2；标准栈 802.3af/at；HPoE 75W + 802.3at 30W；HPoE 口默认 75000mW、at 口 30000mW、slot 默认 1800W <<<PAGE 50>>>
- **P30** PoE 激活两级模型：软件默认 administratively enabled，但必须逐 slot `lanpower slot service start`（"PoE must be activated via the lanpower start command"）<<<PAGE 50>>>/<<<PAGE 52>>>
- **P31** 端口优先方向反转（对比接入交换机）："PoE Physical Port Priority 48 (Highest) -> 1 (Lowest)"——9912/9907 平台端口号越大优先级越高，与 6865/6870 的"1 最高"相反 <<<PAGE 55>>>
- **P32** Priority Disconnect 四场景裁决：禁用→一律拒新 PD；启用+同级→按物理端口号（48 高 1 低）；启用+新 PD 最高优先级→必得电、先断最低优先级口、同级断端口优先级数字最低（即端口号最大）口；启用+新 PD 最低→拒 <<<PAGE 55>>>/<<<PAGE 56>>>
- **P33** Class 检测默认关、开启复位全部 PoE 口："Enabling class detection will reset all PoE ports."；Class 0-4 梯度 0.44-30W <<<PAGE 52>>>
- **P34** 三级端口优先级：low（默认先断）/high/critical，`lanpower port priority` 逐口设置；capacitor-detection 默认关、不符 IEEE；priority-disconnect 默认开 <<<PAGE 50>>>/<<<PAGE 54>>>
- **P35** 端口/槽最大功率语义：只设上限不做预留："Changing the maximum power available to a slot or port does not reserve or immediately allocate that power." <<<PAGE 53>>>
- **P36** 911/UPS 供电纪律：带 IP 话机的 PoE 交换机应全程电源冗余并接 UPS <<<PAGE 50>>>

## 热插拔与安全机制

- **P37** 热插拔节律双标准：拆件间隔 30 秒；插件间隔 5 分钟且 LED 无错才可进行下一件——"All component removals must have a 30 second interval... All component insertions must have a five minute interval AND an LED state indicating that no errors have occurred." <<<PAGE 63>>>
- **P38** 单件不可热拆原则："Hot swapping CMMs, CFMs, or power supplies is supported ONLY if more than one of these components is installed."（单 CMM/单 CFM/单电源时拆即断业务）<<<PAGE 63>>>
- **P39** CFM 热换三纪律：一次只换一个；风扇托盘全数在位；"CFM hot swap should be completed within 120 seconds." <<<PAGE 63>>>
- **P40** NI 热换只限同类："Network Interface (NI) modules can only be hot swapped with like modules."；先断全部网线、拔全部光模块、等 30 秒再插替代件 <<<PAGE 63>>>
