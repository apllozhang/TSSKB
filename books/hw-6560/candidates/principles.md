# principles — OmniSwitch 6560 Hardware Users Guide（硬件机制/架构/规格要点候选）

格式：编号 P# ｜ 要点 ｜ 页码（fulltext.md 真实 `<<<PAGE N>>>` 标记）

## 家族与端口架构

- **P1** 家族命名解码：`P`=PoE（at/bt）；`Z8/Z24/Z16`=多千兆 2.5G/802.3bt 口数（8/24/16）；`E`=增强版含 5G 口（E-P24Z8 口 21-24、E-P48Z16 口 33-36 为 2.5G/5G）；`X4`=4×SFP+ 上行；`X10`=8×SFP+ + 2×20G QSFP+ VFL 纯上联 <<<PAGE 12>>>/<<<PAGE 13>>>/<<<PAGE 26>>>/<<<PAGE 36>>>
- **P2** 多千兆口速率梯度：Z 口支持 100/1000/2.5G（E 版部分口至 5G），全部为 802.3bt PoE；基础口为 10/100/1000 at——同一机箱两种 PoE 标准并存 <<<PAGE 12>>>/<<<PAGE 13>>>
- **P3** 10G 许可口机制：24X4/48X4（及 P 版）口 49-50 为"SFP(+) (1G/10G) ports (10G speed requires license)"——硬件同口，10G 速率需软件许可解锁，默认 1G <<<PAGE 30>>>/<<<PAGE 32>>>/<<<PAGE 42>>>/<<<PAGE 44>>>
- **P4** 20G QSFP+ VFL 口：Z24/Z16 家族与 X10 统一配 2 个 20G QSFP+ VFL 口；X4 家族无 QSFP 但 48X4 多 2 个纯 10G SFP+（53-54）<<<PAGE 12>>>/<<<PAGE 13>>>
- **P5** 全家族统一物理包络：1U、44cm 宽、35cm 深、Tmra 0-45°C、存储 -40~85°C、湿度 5-95%——机房条件无差异化 <<<PAGE 25>>>-<<<PAGE 47>>>
- **P6** 待机功耗梯度（体现多千兆成本）：P24X4=44W、24X4=44W、X10=49W、P24Z8=67W、E-P24Z8=74W、P48X4=107W、P48Z16=107W、E-P48Z16=119W、Z24 系列 116W——2.5G/5G 口使待机功耗翻倍 <<<PAGE 25>>>-<<<PAGE 47>>>

## 电源体系

- **P7** 两套电源架构：PoE 机型=双可插拔 PSU 负载分担（"If a second power supply is installed the two power supplies will load share"）；非 PoE 机型（24X4/48X4/X10）=内置 65W + 模块化备份电源槽（BPS，可插 BP/BP-D 150W）<<<PAGE 42>>>/<<<PAGE 44>>>/<<<PAGE 46>>>/<<<PAGE 60>>>
- **P8** PoE 电源三档：OS6560-BP-P 300W（54.5V/5.5A）、BP-PH 600W（54.5V/11A）、BP-PX 920W（54.5V/16.88A）；系统功率均封顶 110W，其余全给 PoE——同 wattage 双电源负载分担 <<<PAGE 61>>>/<<<PAGE 62>>>/<<<PAGE 63>>>
- **P9** 电源 PN 版本双轨：BP-PH 有 903852-90/904071-90/904072-90 三版、BP-PX 有 903853-90/904073-90 两版——新版（904072-90/904073-90）需最低 AOS 8.8R1 且支持的机型范围更广 <<<PAGE 60>>>/<<<PAGE 62>>>/<<<PAGE 63>>>
- **P10** PoE 预算矩阵（机型×电源×数量）：如 P48X4：1×BP-P=200W/2=462W；1×PH=477W/2=1000W；1×PX=785W/2=1440W；E-P48Z16 双 PX 达 1565W；双电源预算约为单电源 2 倍（负载分担放大）<<<PAGE 87>>>
- **P11** PN 门槛特例：P48Z16 903954-90（老版）用 BP-P/PH/PX；其他 PN 版仅支持 PH/PX（BP-P Not Supported）；E-P24Z8/E-P48Z16 不支持 BP-P——按 PN 查表选电源 <<<PAGE 34>>>/<<<PAGE 60>>>/<<<PAGE 87>>>
- **P12** 无电源开关语义：接电即开机、断全部电源即关机（与 6465 同）<<<PAGE 60>>>/<<<PAGE 71>>>
- **P13** 电源 LED 双灯制（PoE PSU）：AC OK（绿/红）+ DC OK（绿/红）分离指示；BP/BP-D 单 LED 六态（稳绿供电/闪绿待机/闪红无 AC（他机在位）/闪绿红告警/稳红故障/灭全停）<<<PAGE 61>>>-<<<PAGE 65>>>
- **P14** DC 电源规范：-36~-72VDC 输入；12AWG 三芯线束（绿黄=地、黑=return、红=-48VDC）；支路过流保护 15A；需易达断路装置；电池回流为隔离直流回流（DC-1）<<<PAGE 65>>>/<<<PAGE 68>>>/<<<PAGE 69>>>

## 面板与 LED 机制

- **P15** 四颗系统 LED：OK（绿/闪绿/琥珀=启动失败）；VC（稳绿=master/稳琥珀=slave）；PWR 四态语义按电源在场数区分（绿=双电正常或单电正常、琥珀=一或双故障、灭=无电源）；另前面板独立 Virtual Chassis ID LED <<<PAGE 48>>>
- **P16** 2.5G 口双 LED 机制：Speed LED1（绿=2.5G 链路/闪绿=活动；琥珀=100/1000 链路/闪琥珀=活动）+ PoE LED2（琥珀=PoE 使能/灭=禁用）——速率与 PoE 状态分灯显示 <<<PAGE 49>>>
- **P17** 千兆口 LED 颜色分 PoE：绿=非 PoE、琥珀=PoE（闪=活动），与家族惯例一致 <<<PAGE 48>>>

## 安装与 DNV 机制

- **P18** 机架法兰免工具卡扣与 6360 同构：弹簧夹 out→tab 入槽→"CLICK"锁定→螺丝固定<<<PAGE 54>>>/<<<PAGE 55>>>
- **P19** DNV（船用）体系仅限 P48X4/X10：OS-DNV-MNT 套件（侧轨+前后托架）固定机箱后部 + OS-DNV-FILTER EMC 滤波器串在电源与机箱之间——"contains circuitry to eliminate low end conducted emissions from 10kHz to 150KHz" <<<PAGE 58>>>/<<<PAGE 59>>>/<<<PAGE 67>>>
- **P20** DNV 滤波器规格：C14 入/C15 出、100-240VAC/15-7.5A、36" 输出线、自然对流散热、IP22（控制室）、工作海拔 4000m、UL94 V-2 阻燃 <<<PAGE 67>>>
- **P21** 盲板/气流/接地规范同家族：盲板箭头朝上常装；前 6"/后 6"/侧 2" 间隙；LCD8-10A-L+8AWG+30-60 in-lb；DC 场景 CBN 共模接地 <<<PAGE 51>>>/<<<PAGE 52>>>/<<<PAGE 74>>>/<<<PAGE 68>>>
- **P22** 气流遮挡致失效："Restricted airflow can cause your switch to overheat, which can lead to switch failure." <<<PAGE 51>>>

## 监控与温度机制

- **P23** 温度双阈值行为：Warning 超限发 trap 不停机——注意 6560 的 Warning 阈值是"user-configurable"（用户可配，且排障项含"Verifying that the warning threshold has not been manually set too low"）；Danger 超限自动关机需手动重启且出厂固化不可配 <<<PAGE 76>>>
- **P24** 硬件监控命令族：show module / show module long / show temperature / show powersupply / show lanpower（另可用 WebView 网页管理）<<<PAGE 75>>>/<<<PAGE 87>>>/<<<PAGE 84>>>
- **P25** Dying Gasp 三通道：整机失电发 SNMP trap（前 3 站：槽号/主备电源/时间）+ Syslog"Dying Gasp Power Failure Event Occurred"（前 3 服务器）+ 4 个 802.3ah OAM PDU（Dying Gasp 位置位）；PDU 发送上联口优先 <<<PAGE 78>>>/<<<PAGE 80>>>/<<<PAGE 81>>>/<<<PAGE 82>>>
- **P26** DG 触发场景与防护：单电源失效、主备先后全失；"Connect each power supply to a separate independent power source to avoid simultaneous power failures." <<<PAGE 79>>>
- **P27** 双人机架纪律与重物下置（"install the switch at the bottom of the rack whenever possible"）；桌面安装禁侧放/倒放 <<<PAGE 53>>>/<<<PAGE 57>>>

## PoE 机制

- **P28** bt 全规格栈：802.3/af/at/bt；at 口 3000-30000mW、bt 口 3000-95000mW；Class 0-8 全表（15.4/4/7/15.4/30/45/60/75/90-99W）<<<PAGE 85>>>/<<<PAGE 88>>>
- **P29** 4pair/802.3bt 使能：lanpower 4pair 开 60/75/95W（PoH）；lanpower 8023bt 开 bt 类型（Class 5-8）<<<PAGE 89>>>
- **P30** lanpower 命令族与 6360 同构：service 两级激活、admin-state 仅复活、power/maxpower 上限不预留、priority 三级、class-detection 复位全口、capacitor-detection 仅 legacy 话机、Guard Band 拒载、Priority Disconnect（同级按物理口号 1 高 48 低）<<<PAGE 89>>>-<<<PAGE 95>>>
- **P31** BPS 显示：show lanpower 输出含"BPS power: Not Available"行——非 PoE 机型备份电源状态并入 PoE 命令输出 <<<PAGE 88>>>
- **P32** 混插 wattage 电源会告警："PoE units support different wattage power supplies. If unlike power supplies are mixed or if an unsupported power supply is used, a console message and a trap are generated."<<<PAGE 88>>>
- **P33** 911/UPS 纪律：IP 话机 PoE 交换机保持电源冗余并接 UPS <<<PAGE 83>>>

## 首次登录机制

- **P34** 首次登录六步与会话解锁模型与 6360 同构：admin/switch→aaa authentication（一次一类）→password（实时保存）→时间/时区→可选项→write memory <<<PAGE 19>>>-<<<PAGE 22>>>

---
合计：34 条（P1-P34）。
