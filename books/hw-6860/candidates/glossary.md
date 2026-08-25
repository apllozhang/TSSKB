# glossary — 术语表（OmniSwitch 6860/6860E/6860N Hardware Users Guide）

格式：`- **术语**：中文解释 <<<PAGE N>>>`（页码为 fulltext.md 真实标记；按章分组）

## 基础代机型（Ch1/Ch3）

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
