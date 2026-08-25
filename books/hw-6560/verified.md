# Verified 候选（V1 原文真实性核对 + V2/V3 抽查）

## cases

## 上电与首次登录
- **C1** 上电流程：各电源线插入易达接地插座；多电源数秒内先后插电；冗余 AC 建议每路独立电路 <<<PAGE 16>>>/<<<PAGE 19>>>
- **C2** 首次登录六步流程：console（9600-8N1 DCE）→admin/switch→aaa authentication 解锁会话→password 改密→system time/date/timezone→system contact/name/location→show system→write memory <<<PAGE 19>>>-<<<PAGE 22>>>
## 机箱安装
- **C3** 机架法兰安装流程：弹簧夹置 out→tab 入机箱槽→按压至"CLICK"锁定→螺丝固定→对侧重复 <<<PAGE 54>>>/<<<PAGE 55>>>
- **C4** 机架整机安装流程：双人作业（一人抬一人拧）→标记孔位→对齐→先下孔螺丝后上孔螺丝全紧固；重设备下置；机架螺丝自备 <<<PAGE 53>>>/<<<PAGE 56>>>
- **C5** 桌面安装流程：4 橡胶脚垫入底板孔→正放稳固平面（禁倒放/侧放）→接线缆 <<<PAGE 57>>>
- **C6** 盲板安装流程：电源槽盲板箭头朝上→插入空槽→附赠螺丝固定；空槽常盖 <<<PAGE 52>>>
- **C7** DNV 安装流程（P48X4/X10）：OS-DNV-MNT 套件侧轨+后托架固定机箱后部→前托架入位→OS-DNV-FILTER 滤波器串接在电源与机箱之间（C14 入/C15 出，随机架托架与线扣固定） <<<PAGE 58>>>/<<<PAGE 59>>>
- **C8** 机箱 supplemental 接地：LCD8-10A-L 接地耳+8AWG 铜线+30-60 in-lb（后板无漆区）；DC 场景双接地孔装 lug 接大地 <<<PAGE 74>>>/<<<PAGE 68>>>
## 电源安装与接线
- **C9** 电源安装流程：电源插入后部电源舱→滑入至背板就位（锁扣"click"锁定）→插电源线——接电即开机 <<<PAGE 70>>>/<<<PAGE 71>>>
- **C10** 电源拆卸流程：先从电源侧拔线→按锁扣向中心→直拉抽出；不回装则盖盲板 <<<PAGE 72>>>/<<<PAGE 73>>>
- **C11** DC 线束接线流程（BP-D）：三芯 12AWG 线束一端插电源三孔连接器（至 click）→另一端按极性接 -48VDC 熔丝面板（绿黄=地/黑=return/红=-48V）→绿黄线接大地；前提：-48VDC SELV 可靠接地源、15A 过流保护、易达断路装置、受限场所 <<<PAGE 68>>>/<<<PAGE 69>>>
- **C12** Dying Gasp OAM 配置：efm-oam admin-state enable→efm-oam port 1/1/23-24 admin-state enable→efm-oam port 1/1/23-24 propagate-events dying-gasp enable <<<PAGE 82>>>
- **C13** 硬件巡检流程：show module/long→show temperature（UNDER THRESHOLD 正常；Warning 查气流/室温/阈值是否被设低，Danger 关机处理后手动启动）→show powersupply <<<PAGE 75>>>/<<<PAGE 76>>>/<<<PAGE 87>>>
## PoE 配置
- **C14** PoE 首次激活流程：show powersupply 确认（如 920 AC UP）→lanpower slot 2/1 service start→show lanpower slot 1/1 核对逐口/Max Watts/预算/BPS 状态 <<<PAGE 87>>>/<<<PAGE 88>>>/<<<PAGE 89>>>
- **C15** PoE 关断两级：单口 lanpower port 1/1/12 admin-state disable；整槽 lanpower slot 1/1 service stop；admin-state enable 仅复活 <<<PAGE 89>>>
- **C16** 端口/槽功率配置：lanpower port 1/1/24 power 3000 限口；lanpower slot 3/1 maxpower 400 限槽（下调可致低优先级口失电）<<<PAGE 90>>>
- **C17** 优先级配置：lanpower port 1/1/6 priority critical（low/high/critical 三级）<<<PAGE 90>>>/<<<PAGE 91>>>
- **C18** Guard Band 拒载处置：余 50W/口上限 75W 拒 4W PD→lanpower power 1/1/1 power 10000 降上限放行 <<<PAGE 92>>>
- **C19** Priority Disconnect 开关：默认启用；lanpower slot 2/1 priority-disconnect disable/enable；同级按物理口号（1 最高 48 最低）裁决 <<<PAGE 93>>>/<<<PAGE 94>>>
- **C20** bt/4pair 使能：lanpower 4pair 开 60/75/95W；lanpower 8023bt 开 Class 5-8 <<<PAGE 89>>>
- **C21** Class 检测/电容检测：lanpower slot class-detection（复位全 PoE 口）；lanpower slot 3/1 capacitor-detection enable（仅 legacy 话机）<<<PAGE 89>>>/<<<PAGE 91>>>
- **C22** PoE 监控：show lanpower 1 输出逐口 Maximum/Actual/Status/Priority/On-Off/Class + 槽预算/已用/余量/电源数 <<<PAGE 96>>>

---
合计：22 条（C1-C22）。

## counter-examples

## 平台与电源限制
- **X1** SFP(+) 口 10G 需许可："(49-50) SFP(+) (1G/10G) ports (10G speed requires license)"——24X4/48X4 及 P 版的 49-50 口默认 1G，10G 要软件许可 <<<PAGE 30>>>/<<<PAGE 32>>>/<<<PAGE 42>>>/<<<PAGE 44>>>
- **X2** BP-P 300W 电源对 E 机型/新 PN 不支持："OS6560E-P24Z8 ... Not Supported"；P48Z16 仅 903954-90 老版支持 BP-P（新 PN Not Supported）<<<PAGE 60>>>/<<<PAGE 87>>>
- **X3** 新 PN 电源版本门槛："OS6560-BP-PH (904072-90) requires a minimum AOS version of 8.8R1."；"OS6560-BP-PX (904073-90) requires a minimum AOS version of 8.8R1." <<<PAGE 60>>>
- **X4** PoE 电源禁混插 wattage："Mixing different wattage power supplies in a chassis is not supported."（300/600/920 之间不可混）<<<PAGE 61>>>/<<<PAGE 62>>>/<<<PAGE 63>>>
- **X5** 混插或不支持电源会告警："If unlike power supplies are mixed or if an unsupported power supply is used, a console message and a trap are generated." <<<PAGE 88>>>
- **X6** 150W 双兄弟例外：BP（AC）与 BP-D（DC）可同箱混用："Mixing the OS6560-BP with the OS6560-BP-D in the same chassis is supported."（唯一允许的混插组合）<<<PAGE 64>>>/<<<PAGE 65>>>
- **X7** Danger 阈值不可配："The danger threshold is factory-set and cannot be configured by the user."（Warning 阈值本机用户可配，且设太低会误告警）<<<PAGE 76>>>
- **X8** admin-state 不能首次激活 PoE："You cannot use the lanpower port admin-state command to initially activate PoE on a port."（必须 lanpower slot service）<<<PAGE 89>>>
- **X9** Class 检测开启复位全口："Enabling class detection will reset all PoE ports on the chassis." <<<PAGE 89>>>
- **X10** 电容检测不符 IEEE："The capacitive detection method should only be enabled to support legacy IP phones. This feature is not compatible with IEEE specifications." <<<PAGE 91>>>
- **X11** aaa authentication 一次一类："You cannot specify more than one session type in a single command line." <<<PAGE 21>>>
- **X12** 密码覆盖受限："overriding configured passwords on an OmniSwitch is restricted." <<<PAGE 21>>>
## 安装与环境警告
- **X13** 禁延长线："Do not use extension cords."；室外禁裸线缆："Never install exposed network cables outdoors." <<<PAGE 15>>>/<<<PAGE 18>>>
- **X14** 违反电涌五条军规可能失保："Failure to follow the above recommendations could result in voiding the warranty of the affected ALE product."（含 CDE 线缆先接地）<<<PAGE 16>>>
- **X15** 气流遮挡致失效："Restricted airflow can cause your switch to overheat, which can lead to switch failure."（Never obstruct chassis air vents）<<<PAGE 17>>>/<<<PAGE 51>>>
- **X16** 桌面摆放限制："Never attempt to operate a switch while it is placed on its top or side." <<<PAGE 57>>>
- **X17** 盲板必须常装："Because they regulate airflow and help protect internal chassis components, blank cover plates should remain installed at empty module slots and power supply bays at all times." <<<PAGE 52>>>/<<<PAGE 105>>>
- **X18** 雷暴作业禁令："To avoid a shock hazard, do not connect or disconnect any cables or perform installation, maintenance, or reconfiguration of this product during an electrical storm." <<<PAGE 106>>>
- **X19** 机架螺丝自备："Alcatel-Lucent Enterprise does not provide rack-mount screws. Use the screws supplied by the rack vendor."；双人作业强制 <<<PAGE 53>>>
## 电气与激光安全
- **X20** DC 接线五前提："Connect to a reliably ground -48VDC Selv source... The branch circuit overcurrent protection must be rated 15A. Use 12AWG copper conductors... readily accessible disconnect device... restricted access location." <<<PAGE 68>>>
- **X21** 运行中勿触电源舱/背板："keep your hands and fingers out of power supply bays and do not touch the backplane while the switch is operating."；多电源设备维护前断全部电源 <<<PAGE 107>>>
- **X22** 接地红线：电源线必须接正确接地插座；DC/DC 电源地线必须接大地（EMC/EMI）；CBN 共模接地网安装 <<<PAGE 107>>>/<<<PAGE 108>>>/<<<PAGE 68>>>
- **X23** Class 1M 激光："CLASS 1M LASER RADIATION WHEN OPEN. DO NOT VIEW DIRECTLY WITH OPTICAL INSTRUMENTS."；未接光纤勿盯孔位 <<<PAGE 24>>>等/<<<PAGE 105>>>/<<<PAGE 106>>>
- **X24** ESD 腕带强制："Because electrostatic discharge (ESD) can damage switch components, you must follow proper procedures to eliminate ESD from your person and the surrounding area before handling switch components." <<<PAGE 108>>>
- **X25** 锂电池爆炸风险："Hay un peligro de la explosión si la batería del litio en su chasis se substituye incorrectamente."（同型号更换并返厂）<<<PAGE 110>>>
## 使用场所限制
- **X26** Class A 住宅禁令："Warning: To avoid electromagnetic interference, this product should not be installed or used in residential environments."（FCC/VCCI/BSMI）<<<PAGE 104>>>/<<<PAGE 105>>>
- **X27** 受限访问场所："This equipment should be installed in a location that restricts access... limited to service personnel who have a special key"；仅专业电气/机械人员安装维护 <<<PAGE 108>>>/<<<PAGE 106>>>

---
合计：27 条（X1-X27）。

## frameworks

- **F1** 6560 家族选型三轴矩阵：轴一=下行口构成（X4 家族=纯千兆 24/48 口；Z8/Z24/Z16=含 2.5G bt 口；E 版=部分口升 5G；X10=纯 8×SFP+ 上联）；轴二=PoE 与预算（非 PoE=内置 65W+BPS；PoE=按预算表选 300/600/920W 单/双电源，双 PX 最高 1565W）；轴三=上联形态（4×SFP+/2×20G QSFP+ VFL/纯 10G X10）。选型口诀：先按 AP/Wi-Fi6 多千兆需求定 Z 口数，再按 PD 总功率查预算表选电源档，最后核对 PN 版本兼容（BP-P 不配 E 机型/新 P48Z16）。 <<<PAGE 12>>>/<<<PAGE 13>>>/<<<PAGE 60>>>/<<<PAGE 87>>>
- **F2** 电源-PoE 预算联动框架：单电源预算≈电源 wattage−系统 110W 封顶；双电源负载分担预算≈2×单电源（如 P48X4：1×PX 785W→2×PX 1440W）。部署三查：一查机型×电源×数量的预算表；二查 PN 版本（老 903852/903853 vs 新 904071/904072/904073，新件需 AOS ≥8.8R1）；三查混插规则（wattage 禁混、BP+BP-D 唯一例外、混插发 trap）。 <<<PAGE 60>>>/<<<PAGE 87>>>/<<<PAGE 88>>>
- **F3** 高可用双支柱框架：供电侧=双电源负载分担+独立电路+UPS（911 纪律）+DG 失电三通道通告（SNMP/Syslog/OAM PDU 上联口优先）；运行侧=温度双阈值（Warning 可调预警不停机→Danger 固化关机保护）+自动监控 trap+LED 三层（系统 OK/VC/PWR、端口速率/PoE 分灯、电源 AC/DC 双灯）+show 命令/WebView 巡检。 <<<PAGE 78>>>-<<<PAGE 82>>>/<<<PAGE 76>>>/<<<PAGE 48>>>

---
合计：3 条（F1-F3）。

## glossary

- **OS6560-P24Z8**：16 口 at + 8 口 2.5G bt PoE + 2×SFP+，待机 67W <<<PAGE 12>>>/<<<PAGE 25>>>
- **OS6560E-P24Z8**：16 at + 4×2.5G bt（17-20）+ 4×2.5G/5G bt（21-24）+ 2×SFP+ 的 E 增强版，不支持 BP-P 电源 <<<PAGE 12>>>/<<<PAGE 26>>>/<<<PAGE 60>>>
- **OS6560-P24Z24**：24 口全 2.5G bt PoE + 4×SFP+ + 2×20G QSFP+ VFL，待机 116W <<<PAGE 12>>>/<<<PAGE 28>>>
- **OS6560-P48Z16**：32 at + 16 口 2.5G bt + 4×SFP+ + 2×QSFP+ VFL；有 903954-90（老版）与其余 PN（新版）两版 <<<PAGE 12>>>/<<<PAGE 34>>>
- **OS6560E-P48Z16**：32 at + 4×2.5G/5G bt（33-36）+ 12×2.5G bt（37-48）+ 4×SFP+ + 2×QSFP+ VFL，待机 119W <<<PAGE 12>>>/<<<PAGE 36>>>
- **OS6560-24Z8**：16 千兆 + 8×2.5G 非 PoE + 2×SFP+ <<<PAGE 12>>>/<<<PAGE 38>>>
- **OS6560-24Z24**：24×2.5G 非 PoE + 4×SFP+ + 2×QSFP+ VFL <<<PAGE 12>>>/<<<PAGE 40>>>
- **OS6560-24X4**：24 千兆非 PoE + 2×SFP(+)（10G 需许可）+ 4×SFP+；内置电源+BPS 槽 <<<PAGE 13>>>/<<<PAGE 42>>>
- **OS6560-P24X4**：24 口 at PoE + 2×SFP(+)（10G 需许可）+ 4×SFP+ <<<PAGE 13>>>/<<<PAGE 30>>>
- **OS6560-48X4**：48 千兆 + 2×SFP(+)（10G 需许可）+ 2×SFP+ + 2×纯 10G SFP+；内置电源+BPS 槽 <<<PAGE 13>>>/<<<PAGE 44>>>
- **OS6560-P48X4**：48 口 at PoE 版 48X4，双 PX 电源 PoE 预算最高 1440W <<<PAGE 13>>>/<<<PAGE 32>>>/<<<PAGE 87>>>
- **OS6560-X10**：8×SFP+ 1G/10G + 2×20G QSFP+ VFL 纯上联机型，内置 65W+模块化电源 <<<PAGE 13>>>/<<<PAGE 46>>>
- **Z 口（多千兆口）**：100/1000/2.5G（E 版至 5G）802.3bt PoE 口，Speed+PoE 双 LED <<<PAGE 12>>>/<<<PAGE 49>>>
- **10G 许可口**：SFP(+) 1G/10G 口位，10G 速率需软件许可（49-50 口）<<<PAGE 30>>>等

## 电源体系（Ch3）
- **OS6560-BP-P**：300W AC PoE 电源（PS-300W-AC-P），54.5V/5.5A，系统 110W 封顶；不配 E 机型与新 PN 的 P48Z16 <<<PAGE 61>>>/<<<PAGE 60>>>
- **OS6560-BP-PH**：600W AC PoE 电源（PS-600W-AC-P），54.5V/11A；PN 903852-90/904071-90/904072-90 三版，904072-90 需 ≥8.8R1 <<<PAGE 62>>>
- **OS6560-BP-PX**：920W AC PoE 电源（PS-920W-AC-P），54.5V/16.88A；903853-90/904073-90 两版，904073-90 需 ≥8.8R1 <<<PAGE 63>>>
- **OS6560-BP**：150W AC 电源（PS-150W-AC），配非 PoE 机型/BPS；可与 BP-D 混插 <<<PAGE 64>>>
- **OS6560-BP-D**：150W DC 电源（PS-150W-DC），-36~-72V 输入，配非 PoE 机型 <<<PAGE 65>>>
- **内置 AC 电源（65W）**：24X4/48X4/X10 的内置 12V/5.42A 系统电源 <<<PAGE 66>>>
- **BPS（Backup Power Supply Slot）**：非 PoE 机型后部模块化备份电源槽（标"BPS"）<<<PAGE 42>>>/<<<PAGE 44>>>/<<<PAGE 46>>>
- **锁扣（Lock Tab）**：可插拔电源的锁定片（插入 click 锁定/按住中心抽出）<<<PAGE 70>>>/<<<PAGE 72>>>
- **AC OK / DC OK LED**：PoE 电源双指示灯（绿/红）<<<PAGE 61>>>
- **BP/BP-D 单 LED 六态**：稳绿/闪绿待机/闪红无 AC/闪绿红告警/稳红故障/灭全停 <<<PAGE 64>>>/<<<PAGE 65>>>
- **负载分担（Load Sharing）**：双 PoE 电源共同分担供电（"the two power supplies will load share"）<<<PAGE 60>>>
- **DC 线束**：三芯 12AWG（绿黄=地/黑=return/红=-48VDC），15A 过流、SELV、DC-1 隔离回流 <<<PAGE 68>>>/<<<PAGE 69>>>

## 安装部件（Ch3）
- **Rack Mount Flange**：免工具卡扣机架法兰（out/in 位+CLICK）<<<PAGE 54>>>
- **OS-DNV-MNT**：P48X4/X10 船用安装套件（侧轨+前后托架）<<<PAGE 58>>>
- **OS-DNV-FILTER**：DNV EMC 滤波器——滤除 10kHz-150kHz 传导发射，串接电源与机箱之间；C14 入/C15 出 <<<PAGE 58>>>/<<<PAGE 67>>>
- **Blank Cover Panel**：空槽盲板（箭头朝上常装）<<<PAGE 52>>>
- **Virtual Chassis ID LED**：前面板 VC 标识灯 <<<PAGE 24>>>等

## 面板与 LED（Ch3）
- **OK LED**：绿=启动 OK、闪绿=进行中、琥珀=启动失败 <<<PAGE 48>>>
- **VC LED**：稳绿=master、稳琥珀=slave、灭=关机或非 VC <<<PAGE 48>>>
- **PWR LED**：绿=双电/单电正常、琥珀=一或双故障、灭=无电源 <<<PAGE 48>>>
- **2.5G 口双 LED**：Speed LED（绿=2.5G/琥珀=100-1000）+PoE LED（琥珀=PoE 开）<<<PAGE 49>>>

## 温度与 DG（Ch3）
- **Warning Threshold（可配）**：6560 温度告警阈值用户可配（"user-configurable warning threshold"），超限发 trap 不停机 <<<PAGE 76>>>
- **Danger Threshold**：危险阈值出厂固化，超限关机需手动重启 <<<PAGE 76>>>
- **Dying Gasp**：失电残电通告——SNMP trap（前 3 站）+Syslog（前 3 服务器）+4 个 802.3ah OAM PDU（上联口优先）<<<PAGE 78>>>-<<<PAGE 82>>>
- **efm-oam propagate-events dying-gasp**：使能 DG 经 OAM PDU 通告 <<<PAGE 82>>>
- **CBN（Common Bonding Network）**：共模接地网（DC 安装要求）<<<PAGE 68>>>

## PoE 体系（Ch4）
- **802.3bt 口功率范围**：3000-95000mW（at 口 3000-30000mW）<<<PAGE 85>>>
- **PoE 预算表**：机型×电源×数量三要素查表（如 P48X4 双 PX=1440W）<<<PAGE 87>>>
- **lanpower slot service / port admin-state**：slot 启停 / 端口复活（不能首启）<<<PAGE 89>>>
- **lanpower power / slot maxpower**：端口/槽上限（不预留）<<<PAGE 90>>>
- **lanpower priority**：low/high/critical 三级 <<<PAGE 90>>>
- **lanpower 4pair / 8023bt**：开 60/75/95W PoH / 开 bt Class 5-8 <<<PAGE 89>>>
- **Guard Band**：余量低于口上限即拒新 PD <<<PAGE 92>>>
- **Priority Disconnect**：优先级+物理口号（1 高 48 低）裁决新 PD <<<PAGE 93>>>/<<<PAGE 94>>>
- **BPS power 显示**：show lanpower 输出的备份电源状态行 <<<PAGE 88>>>

## CLI 与管理（Ch2-Ch4）
- **show module / long / temperature / powersupply / lanpower**：硬件巡检命令族 <<<PAGE 75>>>/<<<PAGE 87>>>/<<<PAGE 96>>>
- **WebView**：内嵌 Web 管理界面（OmniVista 或浏览器启动），可管 PoE 等硬件特性 <<<PAGE 84>>>
- **aaa authentication / password / system * / write memory**：首次登录六步命令 <<<PAGE 20>>>-<<<PAGE 22>>>
- **snmp station / swlog output socket**：DG trap/Syslog 接收站配置 <<<PAGE 80>>>/<<<PAGE 81>>>

## 安全与法规（附录 A）
- **CDE（Cable Discharge Event）**：线缆静电放电（Cat5e/6/6a 接前先接地）<<<PAGE 16>>>
- **ESD/Wrist Strap**：静电防护腕带 <<<PAGE 108>>>
- **Class 1M Laser**：开盖激光勿直视 <<<PAGE 24>>>等/<<<PAGE 105>>>
- **Restricted Access Location**：受限访问场所 <<<PAGE 108>>>
- **WEEE/RoHS/Prop 65**：回收/有害物/加州铅警告 <<<PAGE 97>>>-<<<PAGE 100>>>
- **Hi-Pot Test**：以太网口 2250V DC 耐压测试 <<<PAGE 102>>>
- **ETS 300 019**：环境标准（存储 1.1/运输 2.3/固定使用 3.1）<<<PAGE 103>>>
- **Class A 设备**：商用限制（住宅禁用）<<<PAGE 104>>>
- **Tmra**：最大额定环境温度（全家族 0-45°C）<<<PAGE 25>>>等
- **Chassis vs Ambient Temperature**：机箱传感器温度恒高于室温 <<<PAGE 25>>>等

---
合计：约 60 条。

## principles

- **P1** 家族命名解码：`P`=PoE（at/bt）；`Z8/Z24/Z16`=多千兆 2.5G/802.3bt 口数（8/24/16）；`E`=增强版含 5G 口（E-P24Z8 口 21-24、E-P48Z16 口 33-36 为 2.5G/5G）；`X4`=4×SFP+ 上行；`X10`=8×SFP+ + 2×20G QSFP+ VFL 纯上联 <<<PAGE 12>>>/<<<PAGE 13>>>/<<<PAGE 26>>>/<<<PAGE 36>>>
- **P2** 多千兆口速率梯度：Z 口支持 100/1000/2.5G（E 版部分口至 5G），全部为 802.3bt PoE；基础口为 10/100/1000 at——同一机箱两种 PoE 标准并存 <<<PAGE 12>>>/<<<PAGE 13>>>
- **P3** 10G 许可口机制：24X4/48X4（及 P 版）口 49-50 为"SFP(+) (1G/10G) ports (10G speed requires license)"——硬件同口，10G 速率需软件许可解锁，默认 1G <<<PAGE 30>>>/<<<PAGE 32>>>/<<<PAGE 42>>>/<<<PAGE 44>>>
- **P5** 全家族统一物理包络：1U、44cm 宽、35cm 深、Tmra 0-45°C、存储 -40~85°C、湿度 5-95%——机房条件无差异化 <<<PAGE 25>>>-<<<PAGE 47>>>
- **P6** 待机功耗梯度（体现多千兆成本）：P24X4=44W、24X4=44W、X10=49W、P24Z8=67W、E-P24Z8=74W、P48X4=107W、P48Z16=107W、E-P48Z16=119W、Z24 系列 116W——2.5G/5G 口使待机功耗翻倍 <<<PAGE 25>>>-<<<PAGE 47>>>
## 电源体系
- **P8** PoE 电源三档：OS6560-BP-P 300W（54.5V/5.5A）、BP-PH 600W（54.5V/11A）、BP-PX 920W（54.5V/16.88A）；系统功率均封顶 110W，其余全给 PoE——同 wattage 双电源负载分担 <<<PAGE 61>>>/<<<PAGE 62>>>/<<<PAGE 63>>>
- **P9** 电源 PN 版本双轨：BP-PH 有 903852-90/904071-90/904072-90 三版、BP-PX 有 903853-90/904073-90 两版——新版（904072-90/904073-90）需最低 AOS 8.8R1 且支持的机型范围更广 <<<PAGE 60>>>/<<<PAGE 62>>>/<<<PAGE 63>>>
- **P12** 无电源开关语义：接电即开机、断全部电源即关机（与 6465 同）<<<PAGE 60>>>/<<<PAGE 71>>>
- **P13** 电源 LED 双灯制（PoE PSU）：AC OK（绿/红）+ DC OK（绿/红）分离指示；BP/BP-D 单 LED 六态（稳绿供电/闪绿待机/闪红无 AC（他机在位）/闪绿红告警/稳红故障/灭全停）<<<PAGE 61>>>-<<<PAGE 65>>>
- **P14** DC 电源规范：-36~-72VDC 输入；12AWG 三芯线束（绿黄=地、黑=return、红=-48VDC）；支路过流保护 15A；需易达断路装置；电池回流为隔离直流回流（DC-1）<<<PAGE 65>>>/<<<PAGE 68>>>/<<<PAGE 69>>>
## 面板与 LED 机制
- **P15** 四颗系统 LED：OK（绿/闪绿/琥珀=启动失败）；VC（稳绿=master/稳琥珀=slave）；PWR 四态语义按电源在场数区分（绿=双电正常或单电正常、琥珀=一或双故障、灭=无电源）；另前面板独立 Virtual Chassis ID LED <<<PAGE 48>>>
- **P16** 2.5G 口双 LED 机制：Speed LED1（绿=2.5G 链路/闪绿=活动；琥珀=100/1000 链路/闪琥珀=活动）+ PoE LED2（琥珀=PoE 使能/灭=禁用）——速率与 PoE 状态分灯显示 <<<PAGE 49>>>
## 安装与 DNV 机制
- **P18** 机架法兰免工具卡扣与 6360 同构：弹簧夹 out→tab 入槽→"CLICK"锁定→螺丝固定<<<PAGE 54>>>/<<<PAGE 55>>>
- **P19** DNV（船用）体系仅限 P48X4/X10：OS-DNV-MNT 套件（侧轨+前后托架）固定机箱后部 + OS-DNV-FILTER EMC 滤波器串在电源与机箱之间——"contains circuitry to eliminate low end conducted emissions from 10kHz to 150KHz" <<<PAGE 58>>>/<<<PAGE 59>>>/<<<PAGE 67>>>
- **P20** DNV 滤波器规格：C14 入/C15 出、100-240VAC/15-7.5A、36" 输出线、自然对流散热、IP22（控制室）、工作海拔 4000m、UL94 V-2 阻燃 <<<PAGE 67>>>
- **P21** 盲板/气流/接地规范同家族：盲板箭头朝上常装；前 6"/后 6"/侧 2" 间隙；LCD8-10A-L+8AWG+30-60 in-lb；DC 场景 CBN 共模接地 <<<PAGE 51>>>/<<<PAGE 52>>>/<<<PAGE 74>>>/<<<PAGE 68>>>
- **P22** 气流遮挡致失效："Restricted airflow can cause your switch to overheat, which can lead to switch failure." <<<PAGE 51>>>
## 监控与温度机制
- **P24** 硬件监控命令族：show module / show module long / show temperature / show powersupply / show lanpower（另可用 WebView 网页管理）<<<PAGE 75>>>/<<<PAGE 87>>>/<<<PAGE 84>>>
- **P25** Dying Gasp 三通道：整机失电发 SNMP trap（前 3 站：槽号/主备电源/时间）+ Syslog"Dying Gasp Power Failure Event Occurred"（前 3 服务器）+ 4 个 802.3ah OAM PDU（Dying Gasp 位置位）；PDU 发送上联口优先 <<<PAGE 78>>>/<<<PAGE 80>>>/<<<PAGE 81>>>/<<<PAGE 82>>>
- **P26** DG 触发场景与防护：单电源失效、主备先后全失；"Connect each power supply to a separate independent power source to avoid simultaneous power failures." <<<PAGE 79>>>
- **P27** 双人机架纪律与重物下置（"install the switch at the bottom of the rack whenever possible"）；桌面安装禁侧放/倒放 <<<PAGE 53>>>/<<<PAGE 57>>>
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
