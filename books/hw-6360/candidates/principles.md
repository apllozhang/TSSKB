# principles — OmniSwitch 6360 Hardware Users Guide（硬件机制/架构/规格要点候选）

格式：编号 P# ｜ 要点 ｜ 页码（fulltext.md 真实 `<<<PAGE N>>>` 标记）

## 家族与端口架构

- **P1** 家族命名解码：10 个 1U 固定配置机型按"口数 + PoE 前缀 + 上行特性"展开——`-10/-24/-48` 非 PoE；`P*`=802.3at PoE；`P*X`=2 个多千兆 802.3bt 口（47-48）+ 950W 电源；`PH*`=combo 口可软件升级 10G（"Upgradeable to 10G"）<<<PAGE 13>>>/<<<PAGE 14>>>/<<<PAGE 15>>>
- **P2** 上行口三段式结构：全家族统一为"2× RJ45/SFP(combo) + 2× SFP+ 软件可配口"，SFP+ 口可在"1G SFP 上行"与"10G SFP+ 上行或 VFL"两种角色间切换："2 x SFP+ software configurable ports: a) 2 x SFP uplinks b) 2 x SFP+ uplink or VFL ports." <<<PAGE 13>>>
- **P3** 10 口机型为半宽机箱（8.5 in 宽），24/48 口机型为全宽 19"（17.3 in）；10 口机型端口分区为 8+2（PoE 前 8 口）+2 SFP <<<PAGE 26>>>/<<<PAGE 27>>>/<<<PAGE 30>>>
- **P4** 无风扇设计分级：OS6360-10/P10/24/P24/48 为 Fan less（无风扇）；P24X/PH24/P48X/PH48（大功率 PoE 机型）带风扇 <<<PAGE 13>>>/<<<PAGE 14>>>
- **P5** 电源全部内置不可热换：单一 Internal AC Power Supply，wattage 随 PoE 能力递增——30W(-10)/65W(-24)/120W(-48)/165W(P10)/260W(P24)/550W(P24X·PH24·P48)/950W(P48X·PH48) <<<PAGE 26>>>/<<<PAGE 30>>>/<<<PAGE 32>>>/<<<PAGE 34>>>/<<<PAGE 36>>>/<<<PAGE 38>>>/<<<PAGE 40>>>/<<<PAGE 42>>>/<<<PAGE 44>>>

## 可用性特性

- **P6** 三大可用性支柱：Hot-Swapping（不断电增删部件）、Hardware Monitoring（内置传感器自动监控，超阈值立即发 trap 到控制台）、LED 视觉状态；另加用户主动 `show` 命令监控："If an error is detected (e.g., over-threshold temperature), the switch immediately sends a trap to the user." <<<PAGE 15>>>/<<<PAGE 16>>>

## 环境与电气规格

- **P7** 全家族统一环境包络：工作温度 0-45°C（Tmra）、存储 -40~70°C、湿度 5%-95% 无凝结、电压 100-240V 50-60Hz <<<PAGE 27>>>/<<<PAGE 29>>>等
- **P8** chassis 与 ambient 温度语义区分："Chassis temperature refers to the sensor reading of the internal switch temperature (threshold or danger). Ambient temperature refers to the approximate room temperature."（机箱温度恒高于室温）<<<PAGE 27>>>等
- **P9** 待机功耗阶梯：-10/P10=13W、-24/P24=21W、P24X/PH24=34W、-48=46W、P48=47W、P48X/PH48=60W——PoE 预算核算要叠加 <<<PAGE 27>>>-<<<PAGE 45>>>
- **P10** 气流间隙三向要求：前面 6 in、后面 6 in、左右各 2 in，顶底免间隙："No clearance is necessary at the top or bottom of the chassis." <<<PAGE 19>>>/<<<PAGE 20>>>
- **P11** 电涌防护五条军规：①全链路等电位接地（接地电阻 ≤0.01Ω）；②室外/近交流线路用 STP Cat5e 以上；③室外铜口必须串接浪涌保护器；④防止室外设备把浪涌电流传给上游交换机；⑤ Cat5e/6/6a 线缆可蓄静电，接线前先对地放电防 CDE："It is recommended that installers momentarily ground all copper Ethernet cables (especially in new cable runs) to a suitable and safe earth ground before connecting them to the port." <<<PAGE 18>>>
- **P12** 电源线纪律：每电源一个接地插座；ALE 电源线 2m 长、UL 认证（IEC 62368-1），禁止延长线："Do not use extension cords." <<<PAGE 17>>>

## 面板与 LED 机制

- **P13** 三颗系统 LED 语义：OK（绿=诊断/启动正常，闪绿=进行中，琥珀=系统/风扇/温度故障）；VC（闪绿=Master，闪琥珀=Slave，闪烁次数即 VC ID，灭=关机或不在 VC 中）；PWR（绿=12V 主电正常，稳琥珀=12V 故障，闪琥珀=54V/PoE 故障，灭=无电源）<<<PAGE 45>>>
- **P14** 端口 LED 用颜色区分 PoE 状态：RJ45 口绿=非 PoE 链路（闪=有活动），琥珀=PoE 链路（闪=有活动）；SFP 口绿=上行、琥珀=VFL 角色 <<<PAGE 46>>>
- **P15** 前面板 Class 1M 激光警示固定出现于每机型："CAUTION - CLASS 1 M LASER RADIATION WHEN OPEN. DO NOT VIEW DIRECTLY WITH OPTICAL INSTRUMENTS" <<<PAGE 26>>>等
- **P16** 后面板标准两件套：机箱接地 lug + 内置电源连接器（部分机型顺序互换）<<<PAGE 26>>>/<<<PAGE 38>>>

## 安装机制

- **P17** 机架安装五大考量（IEC 机架纪律）：Elevated Operating Ambient（封闭机架内温度高于室温，按 Tmra 折减）、Reduced Air Flow、Mechanical Loading（防不均衡载荷）、Circuit Overloading（防过流）、Reliable Earthing（经电源排接入时尤须注意接地可靠性）<<<PAGE 46>>>
- **P18** 盲板气流机制：空槽位不装盲板会迫使气流改道、加重电源风扇负担并暴露内部敏感元件："If your switch is not fully populated and blank cover panels are not installed over empty slot locations, airflow is adversely affected." <<<PAGE 47>>>/<<<PAGE 48>>>
- **P19** 机架法兰免工具卡扣：弹簧夹置 out 位→插 tab 入槽→按压至"CLICK"入 in 位→附赠螺丝固定，两侧对称安装 <<<PAGE 49>>>/<<<PAGE 50>>>
- **P20** 壁挂仅限 10/P10 半宽机型（OS6360-WALL-MNT 套件），四托架朝下安装、建议机箱侧立面板朝侧："it is recommended that the chassis assembly is oriented sideways, with the chassis front panel facing to the side." <<<PAGE 53>>>/<<<PAGE 55>>>
- **P21** 机箱接地规范：后板 lug 用 Panduit LCD8-10A-L、8AWG 铜导线、扭矩 30-60 in-lb，作为电源线接地的补充（paint-free 区域保证金属接触）<<<PAGE 55>>>
- **P22** 双人搬运纪律贯穿全书：机架安装、壁挂安装均明确"Two people are required"<<<PAGE 48>>>/<<<PAGE 54>>>

## 监控与温度机制

- **P23** 温度双阈值机制：Warning 阈值超限→发 trap 但业务继续（应立即查气流/室温）；Danger 阈值超限→交换机自动关机，需人工处理后再手动启动，且 Danger 阈值出厂固化不可配置："The Danger threshold is factory-set and cannot be configured by the user." <<<PAGE 56>>>/<<<PAGE 57>>>
- **P24** 硬件监控三板斧命令：`show module`（槽位基本信息）、`show module long`（详情）、`show temperature`（温度/Range/Danger/Thresh/Status 五列）<<<PAGE 55>>>/<<<PAGE 56>>>

## PoE 机制

- **P25** PoE 标准栈：802.3/802.3af/802.3at/802.3bt；每口功率范围 at 口 3000-30000mW、bt 口 3000-95000mW；Class 检测支持（Class 0-8 功率 15.4-99W 梯度表）<<<PAGE 59>>>/<<<PAGE 61>>>
- **P26** PoE 预算-机型对应表：P10=120W、P24=180W、P24X/PH24=380W、P48=350W、P48X/PH48=760W <<<PAGE 60>>>
- **P27** PoE 激活两级模型：软件层默认 administratively enabled，但物理供电子系统必须逐 slot 用 `lanpower slot service` 启动后 PD 才真正得电："you must issue the lanpower slot service command on a slot-by-slot basis before any connected PDs will receive inline power." <<<PAGE 62>>>
- **P28** 4pair/bt 使能链：`lanpower 4pair` 开 60/75/95W（802.3at 4 对 + PoH）；`lanpower 8023bt` 开 bt 双 Type 四 Class（5-8 类：45/60/75/90-99W）<<<PAGE 62>>>
- **P29** Class 检测默认关：不开启也供电（按预算），严格按类限功率需 `lanpower slot class-detection` 显式开启，且开启会复位全机 PoE 口："Enabling class detection will reset all PoE ports on the chassis." <<<PAGE 61>>>/<<<PAGE 62>>>
- **P30** Fast PoE 机制：PoE 子系统默认态固化进 FPGA 镜像、PoE 配置存于控制器 EEPROM，上电数秒即可供电而不等 AOS 启动完成；依赖正确 FPGA/CPLD 版本；LLDP 协商的 PD 仍要等启动完成 <<<PAGE 63>>>
- **P31** Perpetual PoE 机制：软重启/重载期间对 PD 供电不间断；同样依赖 FPGA/CPLD；但 PoE 控制器（MCU）固件自身升级时供电必断："The power to the PD devices will be interrupted if the PoE controller (MCU) firmware itself is being upgraded." <<<PAGE 63>>>
- **P32** 端口/槽最大功率语义：`lanpower port power`/`lanpower slot maxpower` 只设上限不做预留——"Changing the maximum power available to a slot or port does not reserve or immediately allocate that power."（未用功率仍回到总预算池）<<<PAGE 64>>>
- **P33** 三级端口优先级：low（默认，先断）/high（次保）/critical（尽量保），`lanpower port priority` 逐口设置 <<<PAGE 64>>>
- **P34** Guard Band 拒载机制：新 PD 上线时若剩余预算 < 端口最大功率或 PD 类最大值，则拒绝供电——即使该 PD 实际只需 4W（例：余 50W、口上限 75W→拒载；把口上限调成 10W 即可放行）<<<PAGE 65>>>/<<<PAGE 66>>>
- **P35** Priority Disconnect 裁决规则（预算不足时新 PD 去留）：①禁用→一律拒绝新 PD；②启用+同级→按物理端口号（1 最高，48 最低）裁决；③启用+新 PD 优先级最高→新 PD 必得电，系统先断最低优先级口、同级再断端口号最大的口；④启用+新 PD 优先级最低→拒绝新 PD <<<PAGE 66>>>/<<<PAGE 67>>>/<<<PAGE 68>>>
- **P36** 911/UPS 供电纪律：带 IP 话机的 PoE 交换机应始终保持电源冗余并接 UPS："operational power supply redundancy at all times for 911 emergency requirements." <<<PAGE 58>>>

## 首次登录机制

- **P37** 首次登录六步闭环：console 登录（admin/switch）→解锁会话类型→改密→设时区/时间→可选参数（contact/name/location）→`write memory` 保存 <<<PAGE 21>>>
- **P38** 会话解锁安全模型：出厂仅 console 可用，Telnet/FTP/WebView/SNMP 全锁死，需 `aaa authentication` 逐类解锁（一次命令只能解锁一类）："All other session types (Telnet, FTP, WebView, and SNMP) are locked out until they are manually unlocked by the user." <<<PAGE 22>>>
- **P39** 密码实时落盘：新密码即时写入本地用户库并重启保持，无需额外保存命令；覆盖已配置密码受限 <<<PAGE 22>>>/<<<PAGE 23>>>
- **P40** 控制台固定参数：9600 波特、无校验、8 数据位、1 停止位，DCE 连接 <<<PAGE 20>>>

---
合计：40 条（P1-P40）。
