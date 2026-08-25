# Verified 候选（V1 原文真实性核对 + V2/V3 抽查）

## cases

## 上电与首次登录
- **C1** 上电流程：各电源线插入易达接地插座（禁延长线）；多电源数秒内先后插电；冗余 AC 每路独立电路；接电即自动开机 <<<PAGE 18>>>/<<<PAGE 22>>>
- **C2** 首次登录七步：console（Micro USB，9600-8N1；N 型 115200）→admin/switch→（E 型）EMP 设 IP→aaa authentication 解锁会话→password 改密→system timezone/time/date→system contact/name/location→show system→write memory <<<PAGE 22>>>-<<<PAGE 26>>>
- **C3** EMP 地址配置（E 型）：默认 192.168.1.1/255.255.255.0；ip interface emp address 168.22.2.120 mask 255.255.255.0 修改→show ip interface 核对；解锁会话前经 EMP 的 Telnet/FTP/HTTP/SSH/SNMP 均不可入 <<<PAGE 24>>>
- **C4** 会话类型按类解锁：aaa authentication default local 全解锁；或 telnet/http/ftp local 逐条执行（一次一类） <<<PAGE 25>>>
- **C6** 机架整机安装流程：双人作业（一人抬一人拧）→标记孔位→法兰对齐机架柱→先下孔螺丝后上孔螺丝全紧固；重设备下置；机架螺丝自备；N-P48Z/P48M 后支架滑入导轨并固定机架 <<<PAGE 64>>>/<<<PAGE 66>>>/<<<PAGE 67>>>
- **C7** 桌面安装流程：4 橡胶脚垫入底板孔→正放（禁倒放/侧放）→接线缆；桌面须承载整备重量（至 8.16kg） <<<PAGE 68>>>
- **C8** 盲板安装流程：电源槽盲板箭头朝上→插入空槽→附带螺丝固定；空槽必须常盖 <<<PAGE 63>>>
- **C9** 现场准备检查单：0-45°C/95% 湿度域；前后 6"/侧 2" 间隙（上下免）；每电源一个接地插座；2 米原装线；专业安装师负责接地 <<<PAGE 18>>>/<<<PAGE 21>>>
- **C10** 开箱核对清单：机箱与电源按订单、光模块按订单、盲板、机架法兰、Micro USB-to-USB 线、国别电源线、橡胶脚垫、螺丝、防静电袋 <<<PAGE 20>>>
## 电源安装与 DC 接线
- **C11** 电源安装流程：电源插入后部电源舱→滑入至背板锁扣"click"锁定→插电源线（接电即开机）——四款电源及风扇托盘步骤通用 <<<PAGE 79>>>/<<<PAGE 80>>>
- **C12** 电源拆卸流程：先从电源源侧拔线→拔出电源线→按锁扣向中心→直拉抽出；不回装则盖盲板 <<<PAGE 81>>>/<<<PAGE 82>>>
- **C13** DC 线束接线流程（BP-D）：三芯 12AWG 线束插电源三孔（至 click）→另一端按极性接 -48VDC 熔丝面板（绿黄=地/黑=return/红=-48V）→绿黄接大地；前提：-48VDC SELV/15A/12AWG/易达断路/受限场所 <<<PAGE 78>>>/<<<PAGE 79>>>
- **C14** 机箱 supplemental 接地：Panduit LCD8-10A-L lug+10-32 螺丝装后部接地耳无漆区→8AWG 铜线接大地→力矩 30-60 in-lb <<<PAGE 83>>>
## 上联模块与风扇托盘
- **C15** 上联模块安装流程：模块插入 Slot 2→滑入至就位→captive 螺丝固定；拆卸：松螺丝→握牢直拉抽出（M 型 OS68-XNI/QNI/VNI/CNI 四款通用）<<<PAGE 84>>>
- **C16** 风扇托盘装拆：按电源装拆步骤执行（锁扣同构）——FANTRAY NONPOE 仅非 PoE 机型，占一个 150W 电源位 <<<PAGE 85>>>
## 监控与 Dying Gasp 配置
- **C17** 硬件巡检流程：show module / show module long→show temperature（VC 内逐机箱 CMMA/Slot 行，UNDER THRESHOLD 正常）→show powersupply（如 1/1 920 AC UP Internal）<<<PAGE 86>>>/<<<PAGE 87>>>/<<<PAGE 91>>>
- **C18** Dying Gasp OAM 配置：efm-oam admin-state enable→efm-oam port 1/1/23-24 admin-state enable→efm-oam port 1/1/23-24 propagate-events dying-gasp enable——同时发 PDU 的口上限=10−已配 SNMP/Syslog 服务器数 <<<PAGE 70>>>
- **C19** DG 告警接收配置：snmp station 配 SNMP 站（trap 前 3 站）；swlog output socket 加 Syslog 服务器（前 3 服务器）<<<PAGE 70>>>
## PoE 配置
- **C20** PoE 首次激活流程：show powersupply 确认（如 920 AC UP）→lanpower slot 2/1 service start→show lanpower slot 1/1 核对逐口/槽预算（Max Watts 780/BPS power: Not Available） <<<PAGE 91>>>/<<<PAGE 92>>>/<<<PAGE 95>>>
- **C21** PoE 关断两级：单口 lanpower port 1/1/12 admin-state disable；整槽 lanpower slot 1/1 service stop；admin-state enable 仅复活 <<<PAGE 96>>>
- **C22** 端口/槽功率与优先级调节：lanpower port 1/1/24 power 3000 降口限额；lanpower slot 3/1 maxpower 400 调槽上限（调低可致低优先级口掉电）；lanpower port 1/1/6 priority critical 设关键口 <<<PAGE 96>>>-<<<PAGE 98>>>
- **C23** Guard Band 解锁小功率 PD：剩余预算 < 口 maxpower 时 PD 不上电→lanpower power 1/1/1 power 10000 调低口上限至低于剩余预算→PD 上电 <<<PAGE 102>>>
- **C24** Priority Disconnect 开关：lanpower slot 2/1 priority-disconnect disable/enable——920W 电源上限 780W/电源、600W 上限 450W/电源 <<<PAGE 99>>>
- **C25** PoE 定时规则：lanpower power-rule 按日期/时间开关 PoE 供电（详见 CLI Reference） <<<PAGE 98>>>

---
合计：25 条（C1-C25）。

## counter-examples

## 平台与端口限制
- **X1** N 型 SFP28 四口组禁混速："The OS6860N-U28 doesn't support a mix of 1G/10G and 25G speeds on the 4-port group of ports 31-34. Ports within the port group must all run at either 1G/10G speed or 25G speed."（P48Z 51-54、P24Z 27-30 及 OS68-VNI-U4 模块同则；1G 与 10G 混跑允许） <<<PAGE 48>>>/<<<PAGE 50>>>/<<<PAGE 53>>>/<<<PAGE 57>>>
- **X2** HPoE 口非 bt 合规：E-P24/E-P48 口 1-4 为"HPoE (60W - not 802.3bt compliant)"、E-P24Z8 17-24 为 75W 非 bt——对严格 bt PD 互通需留意 <<<PAGE 43>>>/<<<PAGE 45>>>/<<<PAGE 46>>>
- **X3** OS-BPS 停支持：面板图注"OmniSwitch Backup Power Supply (OS-BPS) (No longer supported.)"——老机箱备份电源槽不再可用 <<<PAGE 29>>>/<<<PAGE 31>>>/<<<PAGE 33>>>/<<<PAGE 35>>>
- **X4** 2000W 电源仅限两款 M 机：OS6860N-BPXL 仅配 OS6860N-P48M/P24M；P48Z/P24Z 表列"Not Supported" <<<PAGE 69>>>/<<<PAGE 93>>>
## 电源限制
- **X5** 不支持电源插入即禁全部业务口："Inserting an unsupported power supply will result in the switching and PoE ports being disabled until the correct power supply is inserted." <<<PAGE 69>>>
- **X6** N 电源软件门槛："OS6860N power supplies are supported beginning with AOS release 8.7R1." <<<PAGE 69>>>
- **X7** PoE 电源禁混 wattage："Mixing different wattage power supplies in a chassis is not supported."（600/920/2000 之间不可混；冗余须同型号） <<<PAGE 73>>>-<<<PAGE 77>>>
- **X8** 混插或不支持电源发告警："If unlike power supplies are mixed or if an unsupported power supply is used, a console message and a trap are generated." <<<PAGE 94>>>
- **X9** 150W 双兄弟例外：BP（AC）与 BP-D（DC）可同箱——"Mixing the OS6860-BP-D with the OS6860-BP in the same chassis is supported."（唯一允许混插组合） <<<PAGE 71>>>/<<<PAGE 72>>>
- **X10** 2000W 电源 115V 降额：100-120VAC 输入仅 1000W/18.35A，200-240VAC 才达 2000W/36.7A——按市电核对预算 <<<PAGE 77>>>
- **X11** priority disconnect 电源档上限：920W 电源最多 780W/只、600W 最多 450W/只——预算超限部分不参与抢占 <<<PAGE 99>>>
## Fast PoE / Perpetual PoE 限制
- **X12** Fast PoE 固件前提："Fast PoE requires the proper FPGA/CPLD version, refer to the release notes for additional information." <<<PAGE 96>>>
- **X13** Fast PoE 新机须先做初始 PoE 配置："Factory default switches that don't have any PoE configuration must have an initial PoE configuration completed." <<<PAGE 96>>>
- **X14** Fast PoE 启动期禁改配置："The PoE configuration cannot be modified until the switch is up and the PoE software module is completely initialized." <<<PAGE 96>>>
- **X15** Fast PoE 下 LLDP PD 异常："LLDP-based PoE devices will not function as expected until the switch has completed the boot-up process and the switch is in a state to respond to LLDP requests." <<<PAGE 96>>>
- **X16** Perpetual PoE 固件前提与 MCU 升级断电："Perpetual PoE requires the proper FPGA/CPLD version... The power to the PD devices will be interrupted if the PoE controller (MCU) firmware itself is being upgraded." <<<PAGE 96>>>
## PoE 通用限制
- **X17** class detection 开启复位全口："Enabling class detection will reset all PoE ports on the chassis." <<<PAGE 95>>>
- **X18** admin-state 不能首次激活 PoE："You cannot use the lanpower port admin-state command to initially activate PoE on a port."（须 lanpower slot service） <<<PAGE 95>>>
- **X19** 电容检测不符 IEEE："The capacitive detection method should only be enabled to support legacy IP phones. This feature is not compatible with IEEE specifications." <<<PAGE 98>>>
- **X20** 调低槽预算可掉电："Decreasing the slot-wide power could cause lower priority ports to lose power if the new value is less than the total PoE power currently being consumed." <<<PAGE 97>>>
- **X21** maxpower 不预留功率："Changing the maximum power available to a slot or port does not reserve or immediately allocate that power." <<<PAGE 97>>>
- **X22** Guard Band 不护已上电 PD："The Guard Band functionality does not apply to PDs that are already powered up."——预算缩减时 priority disconnect 生效 <<<PAGE 102>>>
## 登录与温度限制
- **X23** aaa authentication 一次一类："You cannot specify more than one session type in a single command line." <<<PAGE 25>>>
- **X24** 密码覆盖受限："overriding configured passwords on an OmniSwitch is restricted." <<<PAGE 25>>>
- **X25** Danger 阈值固化不可配："The danger threshold is factory-set and cannot be configured by the user."；超限须手动重启 <<<PAGE 87>>>
## 安装与电气警告
- **X26** 禁延长线："Do not use extension cords."；非 ALE 电源线需安装者自证合规 <<<PAGE 18>>>/<<<PAGE 19>>>
- **X27** 违反电涌军规可能失保："Failure to follow the above recommendations could result in voiding the warranty of the affected ALE product."（五条军规） <<<PAGE 20>>>
- **X28** 气流遮挡致失效："Restricted airflow can cause your switch to overheat, which can lead to switch failure."（Never obstruct chassis air vents） <<<PAGE 61>>>
- **X29** 缺盲板破坏风道："When blank cover panels are missing, air does not take the direct route from the air intake vents... an extra task is placed on the power supply fans to cool the chassis."；盲板须常装 <<<PAGE 62>>>
- **X30** 机架螺丝自备+双人作业："Alcatel-Lucent Enterprise does not provide rack-mount screws. Use the screws supplied by the rack vendor."；重设备下置防头重脚轻 <<<PAGE 64>>>
- **X31** 桌面禁倒放/侧放："Never attempt to operate a switch while it is placed on its top or side." <<<PAGE 68>>>
- **X32** 雷暴作业禁令："do not connect or disconnect any cables or perform installation, maintenance, or reconfiguration of this product during an electrical storm." <<<PAGE 111>>>
- **X33** 运行中勿触背板："keep your hands and fingers out of power supply bays and do not touch the backplane while the switch is operating." <<<PAGE 112>>>
- **X34** 多电源设备搬运前全断："be sure to disconnect all power connections before servicing or moving the unit." <<<PAGE 112>>>
- **X35** Class 1M 激光："CLASS 1M LASER RADIATION WHEN OPEN. DO NOT VIEW DIRECTLY WITH OPTICAL INSTRUMENTS."；空光口勿直视并加盖 <<<PAGE 29>>>/<<<PAGE 110>>>/<<<PAGE 111>>>
- **X36** ESD 腕带强制："you must follow proper procedures to eliminate ESD from your person and the surrounding area before handling switch components." <<<PAGE 113>>>
- **X37** 锂电池更换须返厂（西班牙语安全节）："Hay un peligro de la explosión si la batería del litio en su chasis se substituye incorrectamente... Devuelva el módulo con la batería del litio a Alcatel-Lucent." <<<PAGE 114>>>
- **X38** 受限场所安装："This equipment should be installed in a location that restricts access."（DC 前提亦含） <<<PAGE 78>>>/<<<PAGE 113>>>
- **X39** Class A 住宅禁用："To avoid electromagnetic interference, this product should not be installed or used in residential environments." <<<PAGE 110>>>

---
合计：39 条（X1-X39）。

## frameworks

- **F1** 6860 三代选型矩阵：轴一=代际（基础=at PoE+20G VC 口最省钱；E=协处理器+EMP+HPoE 60/75W 私有高功率；N=bt 95W 多千兆+25G SFP28+QSFP28 VFL，M 型带上联模块槽）。轴二=下行口形态（24/48 铜、U28 全光、Z 多千兆混合、M 模块化上联）。轴三=电源档（非 PoE=150W AC/DC；PoE=600/920W；N 大功率=2000W 仅 M 型、230V 才满额）。选型口诀：普通办公选基础，要协处理器/EMP/私有 60W 选 E，Wi-Fi6/2.5G-5G AP 与 25G 上联选 N；预算按 N 型矩阵查（双 920W 最高 1500-1545W，P48M 双 2000W 达 3390W）。 <<<PAGE 14>>>/<<<PAGE 15>>>/<<<PAGE 69>>>/<<<PAGE 93>>>
- **F2** PoE 预算-抢占上限联动框架：三层预算闸门——层一=物理预算（机型×电源×数量矩阵，双电源约 2.4-2.7 倍于单电源；2000W 电源 115V 打对折）；层二=priority disconnect 上限（920W→780W/只、600W→450W/只，超限部分只供不抢）；层三=Guard Band（剩余预算须大于口 maxpower 才上电）。部署四查：查矩阵定预算、查电源档定抢占上限、调口 maxpower 解 Guard Band、按 24/48 口模型设优先级（端口号越大越高，与其他家族相反）。 <<<PAGE 93>>>/<<<PAGE 99>>>/<<<PAGE 100>>>/<<<PAGE 102>>>
- **F3** VC 堆叠高可用框架：链路侧=2×20G VC 口（N 代 QSFP28 VFL）+VC LED/闪琥珀报 unit 号；供电侧=1+1 双电源负载分担+独立电路+UPS（911 纪律）+DG 三通道（SNMP/Syslog 前 3 目标+4×OAM PDU，同时发 PDU 口数=10−服务器数，上联口优先）；PoE 侧=Fast PoE（上电数秒供电，FPGA 默认使能）+Perpetual PoE（软重启不断 PD 电）+per-slot service/maxpower/priority 三级管控；运行侧=温度双阈值（Warning trap→Danger 关机手动恢复，VC 内逐机箱独立）+五色端口 LED+show module/temperature/powersupply/lanpower 巡检。 <<<PAGE 15>>>/<<<PAGE 69>>>/<<<PAGE 70>>>/<<<PAGE 87>>>/<<<PAGE 96>>>
- **F4** 三代端口演化框架（讲解用）：基础代（千兆铜+SFP+ 10G 上联+20G VC）→E 代（+协处理器/EMP/OK2 双系统灯/HPoE 60-75W 私有高功率/E-P24Z8 首入 2.5G）→N 代（bt 95W 全覆盖、2.5G-10G 多千兆铜口、SFP28 25G 四口组〔组内禁 1G/10G 与 25G 混跑〕、QSFP28 VFL、M 型上联模块化）。讲选型史或替换规划时按此轴展开。 <<<PAGE 14>>>/<<<PAGE 46>>>/<<<PAGE 48>>>/<<<PAGE 56>>>

---
合计：4 条（F1-F4）。

## glossary

- **OS6860-24**：基础非 PoE，24 千兆 + 4×SFP+ + 2×20G VC 口，满系统 46W <<<PAGE 14>>>/<<<PAGE 30>>>
- **OS6860-48**：48 千兆版，57W <<<PAGE 14>>>/<<<PAGE 32>>>
- **OS6860-P24**：24 口 802.3at PoE 版，75W <<<PAGE 14>>>/<<<PAGE 34>>>
- **OS6860-P48**：48 口 at PoE 版，89W <<<PAGE 14>>>/<<<PAGE 36>>>

## 增强代机型（E）
- **OS6860E-24 / E-48**：协处理器增强非 PoE，48W/60W，后板 EMP <<<PAGE 14>>>/<<<PAGE 38>>>/<<<PAGE 40>>>
- **OS6860E-U28**：E 代全光 28 口（1000Base-X/100Base-FX）+4×SFP+ +2×20G VC，73W <<<PAGE 14>>>/<<<PAGE 42>>>
- **OS6860E-P24 / E-P48**：E 代 PoE，口 1-4 为 HPoE 60W（非 bt 合规）+其余 at；76W/93W <<<PAGE 14>>>/<<<PAGE 44>>>/<<<PAGE 46>>>
- **OS6860E-P24Z8**：16×at + 8×100/1000/2.5G 75W HPoE（非 bt），4×SFP+(10G)+2×20G QSFP VC，48W <<<PAGE 14>>>/<<<PAGE 46>>>/<<<PAGE 47>>>
- **built-in co-processor**：E 型内置协处理器——增强网络服务+独立 OK2 诊断 <<<PAGE 14>>>/<<<PAGE 59>>>

## 下一代机型（N）
- **OS6860N-U28**：N 代全光，24×SFP(100M/1G)+4×SFP+(25-28)+2×QSFP28 VFL(29-30)+4×SFP28 31-34，143W <<<PAGE 14>>>/<<<PAGE 48>>>/<<<PAGE 49>>>
- **OS6860N-P48Z**：36×bt 60W + 12×100M-5G bt 95W（37-48）+2×QSFP28+4×SFP28，147W，44cm 深 <<<PAGE 14>>>/<<<PAGE 50>>>/<<<PAGE 51>>>
- **OS6860N-P48M**：模块化上联，36×2.5G bt 95W + 12×100M-10G bt 95W + QSFP28×2 + 上联槽，260W/8.5kg <<<PAGE 15>>>/<<<PAGE 51>>>/<<<PAGE 52>>>
- **OS6860N-P24Z**：12×bt 60W + 12×多千兆 95W + QSFP28×2 + SFP28×4，142W <<<PAGE 15>>>/<<<PAGE 53>>>/<<<PAGE 54>>>
- **OS6860N-P24M**：24×100M-10G bt 95W 全口高档 + QSFP28×2 + 上联槽，176W <<<PAGE 15>>>/<<<PAGE 55>>>/<<<PAGE 56>>>

## 上联模块（N-M 型）
- **OS68-XNI-U4**：4×SFP+（1G/10G）上联模块 <<<PAGE 56>>>
- **OS68-QNI-U2**：2×QSFP+（40G）上联模块 <<<PAGE 57>>>
- **OS68-VNI-U4**：4×SFP28（1G/10G/25G）上联模块——组内禁 1G/10G 与 25G 混跑 <<<PAGE 57>>>
- **OS68-CNI-U1**：1×QSFP28（40G/100G）上联模块 <<<PAGE 58>>>
- **Uplink Module Slot（Slot 2）**：M 型上联模块槽位 <<<PAGE 51>>>/<<<PAGE 55>>>

## 快速入门（Ch2）
- **Micro USB-to-USB cable**：console 线（随机附带）；另配 USB 口（ALE U 盘/蓝牙）与 RS-232 <<<PAGE 15>>>/<<<PAGE 20>>>/<<<PAGE 21>>>
- **Serial Default Settings**：9600-8N1；6860N 为 115200 <<<PAGE 22>>>
- **EMP（E/N 型）**：后板带外管理口——连交换机直通线/连计算机交叉线；默认 192.168.1.1/24 <<<PAGE 22>>>/<<<PAGE 24>>>
- **ip interface emp**：EMP 改 IP 命令；show ip interface 核对 <<<PAGE 24>>>
- **admin/switch**：默认登录名/密码 <<<PAGE 23>>>/<<<PAGE 24>>>
- **aaa authentication**：会话解锁命令（一次一类） <<<PAGE 25>>>
- **show system / write memory**：查看/保存配置 <<<PAGE 26>>>
- **CDE（Cable Discharge Event）**：电缆静电放电——接线前先瞬时接地 <<<PAGE 19>>>
- **Airflow Considerations**：前 6"/后 6"/侧 2" 间隙，上下免 <<<PAGE 21>>>

## LED 体系（Ch3）
- **OK1 / OK2**：主系统/外部 CPU（E 型）诊断启动灯——绿 OK/闪绿进行中/琥珀失败 <<<PAGE 23>>>/<<<PAGE 58>>>/<<<PAGE 59>>>
- **PRI**：VC 角色灯——绿=master/琥珀=slave <<<PAGE 23>>>
- **PS LED**：电源五态——按双电/单电、正常/故障分四种绿琥珀组合+灭 <<<PAGE 59>>>
- **BPS LED**：备份电源灯（OS-BPS 已停支持）——绿/琥珀/灭 <<<PAGE 59>>>
- **GRN（Power Save）**：省电特性激活灯 <<<PAGE 23>>>/<<<PAGE 59>>>
- **VC LED**：稳绿=master/稳琥珀=slave/灭=关机或非 VC <<<PAGE 58>>>
- **6860N 端口五色 LED**：绿=链路/琥珀=PoE/蓝=2.5G/蓝+黄=5G/品红=10G；LED2 琥珀=PoE Active <<<PAGE 60>>>
- **VFL/Uplink LED**：绿=uplink/琥珀=VFL <<<PAGE 60>>>

## 安装（Ch3）
- **Rack Mount Flanges**：弹簧夹免工具法兰——clip out→tab 入槽→CLICK→螺丝固定 <<<PAGE 64>>>/<<<PAGE 65>>>
- **Rear Bracket / Rear Bracket Guide**：N-P48Z/P48M 后支架与导轨（支架总长 26.4 in） <<<PAGE 65>>>/<<<PAGE 67>>>
- **Blank Cover Panels**：盲板——箭头朝上安装，缺盲板破坏风道 <<<PAGE 62>>>/<<<PAGE 63>>>
- **Rubber feet**：桌面安装橡胶脚垫（四只入底板孔） <<<PAGE 68>>>

## 电源体系（Ch3）
- **OS6860-BP（PS-150W-AC）**：150W AC 非 PoE 电源，90-264VAC→12.5A，六态单 LED；可与 BP-D 混插 <<<PAGE 71>>>
- **OS6860-BP-D（PS-150W-DC）**：150W DC 非 PoE 电源，-36~-72VDC；可与 BP 混插 <<<PAGE 72>>>
- **OS6860-BP-PH（PS-600W-AC-P）**：600W AC PoE 电源（P24/E-P24/E-P24Z8） <<<PAGE 73>>>
- **OS6860-BP-PX（PS-920W-AC-P）**：920W AC PoE 电源（P48/E-P48/E-P24Z8） <<<PAGE 75>>>
- **OS6860N-BPPH（YPEB0600AM）**：N 代 600W PoE 电源，AC OK+DC OK 双 LED；需 AOS ≥8.7R1 <<<PAGE 74>>>
- **OS6860N-BPPX（YPEB0920AM）**：N 代 920W PoE电源，双 LED <<<PAGE 76>>>
- **OS6860N-BPXL（YPEE2000CM-1A01P10）**：N 代 2000W PoE 电源（仅 P48M/P24M），115V 降额 1000W，C19 电源线 <<<PAGE 77>>>
- **Lock Tab**：电源锁扣——插入 click 锁定、按中心解锁直拉 <<<PAGE 80>>>/<<<PAGE 81>>>
- **OS-BPS（Backup Power Supply）**：备份电源槽——"No longer supported" <<<PAGE 29>>>/<<<PAGE 31>>>
- **OS6860 FANTRAY NONPOE**：非 PoE 机型风扇托盘（占一个 150W 电源位，配 BPS 用），绿=正常/灭=关或故障 <<<PAGE 85>>>
- **DC Cable Harness / CBN / DC-1 / LCD8-10A-L**：DC 三芯线束（绿黄地/黑 return/红 -48V）/共模网络/隔离回流/接地 lug（30-60 in-lb） <<<PAGE 78>>>/<<<PAGE 79>>>/<<<PAGE 83>>>

## 监控与 Dying Gasp（Ch3）
- **show module / show module long**：槽位信息查看命令 <<<PAGE 86>>>
- **show temperature**：温度查看——VC 内逐机箱（1/CMMA、2/CMMA）逐行 <<<PAGE 87>>>
- **Dying Gasp**：临终告警三通道（SNMP trap/Syslog/802.3ah OAM PDU） <<<PAGE 69>>>/<<<PAGE 70>>>
- **DG PDU 端口挤占公式**：同时发 DG PDU 口数上限=10−已配 Syslog/SNMP 服务器数 <<<PAGE 70>>>
- **efm-oam propagate-events dying-gasp**：DG 触发 OAM PDU 的口级使能命令 <<<PAGE 70>>>
- **snmp station / swlog output socket**：DG 接收端配置命令 <<<PAGE 70>>>

## PoE（Ch4）
- **PD / PSE**：受电设备/供电设备；PoE=PoL=Inline Power 同义 <<<PAGE 89>>>
- **HPoE**：私有高功率口（E 代 60/75W，not 802.3bt compliant） <<<PAGE 43>>>/<<<PAGE 46>>>
- **逐机型口功率域**：如 N-P48M/P24M 全口 3000-95000mW；详见规格表 <<<PAGE 91>>>
- **Fast PoE**：上电数秒即供 PoE——FPGA 默认使能+配置存控制器 EEPROM；四条限制 <<<PAGE 96>>>
- **Perpetual PoE**：软重启/重载期间 PD 不断电；MCU 固件升级会断 <<<PAGE 96>>>
- **lanpower slot service start/stop**：PoE 整槽启停（首次激活必用） <<<PAGE 95>>>
- **lanpower port admin-state enable/disable**：单口复活/关断 <<<PAGE 95>>>/<<<PAGE 96>>>
- **lanpower power / slot maxpower**：口/槽功率上限命令 <<<PAGE 96>>>/<<<PAGE 97>>>
- **lanpower priority**：口优先级 low/high/critical（默认 low） <<<PAGE 97>>>
- **lanpower power-rule**：PoE 定时开关规则命令 <<<PAGE 98>>>
- **lanpower class-detection / capacitor-detection**：等级检测（开则复位全口）/电容检测（不符 IEEE） <<<PAGE 95>>>/<<<PAGE 98>>>
- **Priority Disconnect**：预算不足时按优先级+物理口号裁决（上限 920W→780W、600W→450W 每电源） <<<PAGE 99>>>
- **物理口号优先级**：24 口机 24 最高→1 最低；48 口机 48 最高→1 最低 <<<PAGE 100>>>
- **Guard Band**：剩余预算低于口 maxpower 即拒新 PD <<<PAGE 102>>>
- **show lanpower slot / show powersupply**：PoE/电源状态查看命令 <<<PAGE 91>>>/<<<PAGE 92>>>/<<<PAGE 103>>>
- **911/UPS 纪律**：IP 话机场景须常备电源冗余+UPS <<<PAGE 89>>>

## 法规与标准（附录 A）
- **UL 60950-1 / UL 62368-1**：新旧双安全标准并行合规 <<<PAGE 107>>>
- **ETS 300 019**：环境分级（Storage 1.1/Transportation 2.3/Stationary 3.1） <<<PAGE 108>>>
- **Hi-Pot Test**：IEEE 802.3 耐压——全部以太网口 2250V DC <<<PAGE 108>>>
- **Class A / Class 1M Laser / ESD / WEEE / RoHS / Prop 65**：通用法规警告族 <<<PAGE 106>>>/<<<PAGE 110>>>-<<<PAGE 114>>>
- **TEC, India / Morocco**：印摩认证（联系获取） <<<PAGE 107>>>

## principles

## 家族三代架构
- **P1** 家族三代 15 机型：基础 OS6860（24/48/P24/P48：24/48 千兆 + 4×SFP+ + 2×20G VC 口）；增强 E（24/48/U28/P24/P48/P24Z8："Includes a built-in co-processor for Enhanced network services"+后面板 EMP）；下一代 N（U28/P48Z/P48M/P24Z/P24M：QSFP28 VFL + SFP28 25G 上联，M 型带上联模块槽）——同代 1U 44cm 包络三代演进 <<<PAGE 14>>>/<<<PAGE 15>>>
- **P2** E 增强机制："Includes a built-in co-processor for Enhanced network services"——外部 CPU 独立诊断/启动，对应 OK2 LED（"External CPU Diagnostics and AOS bootup OK"）+ 后面板 EMP 带外口 <<<PAGE 14>>>/<<<PAGE 22>>>/<<<PAGE 59>>>
- **P3** 20G VC 口体系：基础/E 代统一"(2) 20G Virtual Chassis link ports"；N 代升级为"(2) QSFP28 (VFL)"——VC 堆叠链路带宽代际翻倍路径 <<<PAGE 14>>>/<<<PAGE 48>>>/<<<PAGE 50>>>
- **P4** HPoE 非 bt 合规注记：E-P24/E-P48 的口 1-4 为"HPoE (60W - not 802.3bt compliant)"、E-P24Z8 的 17-24 为"(75W HPoE Ports - not 802.3bt compliant)"——私有 60/75W 高功率，早于 bt 标准的遗留实现 <<<PAGE 43>>>/<<<PAGE 45>>>/<<<PAGE 46>>>
- **P6** N 代 bt 95W 全面化：N-P48Z=36×bt 60W + 12×100M-5G bt 95W（37-48）；N-P48M=36×2.5G bt 95W + 12×100M-10G bt 95W + 上联槽；N-P24Z=12×bt 60W + 12×多千兆 95W；N-P24M=24×100M-10G bt 95W 全口最高档 <<<PAGE 50>>>/<<<PAGE 51>>>/<<<PAGE 53>>>/<<<PAGE 55>>>
- **P8** 全家族统一环境包络：Tmra 0-45°C、海拔 13000ft、存储 -40~85°C、湿度 5-95%——机房级（比 6575 工业级窄）<<<PAGE 30>>>-<<<PAGE 56>>>
- **P9** 功耗梯度（满系统功率）：24=46W→48=57W→E24=48W→E48=60W→EU28=73W→P24=75W→P48=89W→E-P24=76W→E-P48=93W→E-P24Z8=48W→N-U28=143W→N-P48Z=147W→N-P24Z=142W→N-P48M=260W→N-P24M=176W——N 代多千兆+25G 使功耗翻两番 <<<PAGE 30>>>-<<<PAGE 56>>>
- **P10** 深度双包络：基础/E=35cm；N 型 M/Z=44cm（P48Z/P48M/P24Z/P24M）——深机箱需后支架辅助；最大整备重量 N-P48M 8.5kg <<<PAGE 30>>>/<<<PAGE 52>>>/<<<PAGE 20>>>
## 面板与 LED 机制
- **P11** 控制台三连接器：console（Micro USB-to-USB 线随机附带）+ USB（ALE U 盘/蓝牙 dongle，不随机）+ RS-232——N 型另加 EMP <<<PAGE 15>>>/<<<PAGE 21>>>
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
- **P24** N 电源软件门槛："OS6860N power supplies are supported beginning with AOS release 8.7R1." <<<PAGE 69>>>
- **P25** 2000W 电源双电压降额：100-120VAC 输入=1000W/18.35A；200-240VAC=2000W/36.7A——大功率电源必须 230V 市电才满额（C19 电源线）<<<PAGE 77>>>
- **P26** 混插双规则：BP-D 与 BP（均 150W）可同箱（"Mixing the OS6860-BP-D with the OS6860-BP in the same chassis is supported."）；其余"Mixing different wattage power supplies in a chassis is not supported."冗余电源须同型号负载分担 <<<PAGE 71>>>/<<<PAGE 73>>>
- **P27** 电源 LED 双制：BP/BP-D/PH/PX 单 LED 六态（稳绿/闪绿待机/闪红邻舱有电/闪绿红告警/稳红故障/灭全停）；N-BPPH/N-BPPX/N-BPXL 双灯 AC OK+DC OK（各绿/红）<<<PAGE 72>>>-<<<PAGE 78>>>
- **P28** 无电源开关语义："The OS6860 does not provide an on/off switch. Connecting an installed power supply to a power source will boot the switch." <<<PAGE 69>>>
- **P29** 双电源舱 1+1 架构："The OS6860 chassis provides two bays for 1+1 redundant hot-swappable power supplies."非 PoE 机型可在一个 150W 电源位换单个可选风扇托盘 <<<PAGE 15>>>
- **P30** 风扇托盘定位："The OS6860 FANTRAY NONPOE provides supplemental system cooling for non-PoE OS6860 switches connected to the OmniSwitch Backup Power Shelf/System (BPS)."——与 BPS 配套的补充散热；绿=正常/灭=关或故障 <<<PAGE 85>>>
## DC 接线与接地
- **P31** DC 供电五前提：可靠接地 -48VDC SELV 源、15A 支路过流保护、12AWG 铜线、易达断路装置、受限场所；CBN 共模网络+DC-1 隔离回流；三芯绿黄=地/黑=return/红=-48VDC <<<PAGE 78>>>/<<<PAGE 79>>>
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
