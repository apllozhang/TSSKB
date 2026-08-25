# GLOSSARY · OmniSwitch 6860/6860E/6860N Hardware Users Guide

> 页码为原书 `<<<PAGE N>>>` 标记。按机型/上联模块/电源/LED/安装/PoE/监控/法规分组，精选 50 条。

## 基础代机型
- **OS6860-24/48/P24/P48**：基础代四机型，24/48 千兆 + 4×SFP+ + 2×20G VC 口；P=at PoE 版；满系统 46/57/75/89W <<<PAGE 14>>>/<<<PAGE 30>>>-<<<PAGE 36>>>

## 增强代机型（E）
- **OS6860E-24/E-48**：协处理器增强非 PoE，后板 EMP，48W/60W <<<PAGE 14>>>/<<<PAGE 38>>>/<<<PAGE 40>>>
- **OS6860E-U28**：E 代全光 28 口 + 4×SFP+ + 2×20G VC，73W <<<PAGE 14>>>/<<<PAGE 42>>>
- **OS6860E-P24/E-P48/E-P24Z8**：E 代 PoE 三机型，口 1-4 为 HPoE 60W（非 bt 合规）；P24Z8 为 16×at + 8×2.5G 75W HPoE + 2×20G QSFP VC <<<PAGE 14>>>/<<<PAGE 44>>>/<<<PAGE 46>>>
- **OS6860E-P24Z8**：16×at + 8×2.5G 75W HPoE（非 bt）+ 2×20G QSFP VC，48W <<<PAGE 14>>>/<<<PAGE 46>>>
- **built-in co-processor**：E 型内置协处理器——增强网络服务+独立 OK2 诊断 <<<PAGE 14>>>/<<<PAGE 59>>>

## 下一代机型（N）
- **OS6860N-U28**：N 代全光，24×SFP + 4×SFP+(25-28) + 2×QSFP28 VFL(29-30) + 4×SFP28(31-34)，143W <<<PAGE 14>>>/<<<PAGE 48>>>
- **OS6860N-P48Z / P48M**：36×bt 60W + 12×100M-5G bt 95W（37-48）/P48M=36×2.5G + 12×100M-10G bt 95W + 上联槽，147W（44cm 深）/260W/8.5kg <<<PAGE 14>>>/<<<PAGE 50>>>/<<<PAGE 51>>>
- **OS6860N-P24Z / P24M**：12×bt 60W + 12×多千兆 95W / 24×100M-10G bt 95W 全口高档 + 2×QSFP28，142W/176W <<<PAGE 15>>>/<<<PAGE 53>>>/<<<PAGE 55>>>

## 上联模块（N-M 型）
- **OS68-XNI-U4**：4×SFP+（1G/10G）上联模块 <<<PAGE 56>>>
- **OS68-QNI-U2**：2×QSFP+（40G）上联模块 <<<PAGE 57>>>
- **OS68-VNI-U4**：4×SFP28（1G/10G/25G）上联模块——组内禁 1G/10G 与 25G 混跑 <<<PAGE 57>>>
- **OS68-CNI-U1**：1×QSFP28（40G/100G）上联模块 <<<PAGE 58>>>
- **Uplink Module Slot（Slot 2）**：M 型上联模块槽位 <<<PAGE 51>>>/<<<PAGE 55>>>
- **VFL**：QSFP28 虚拟光纤链路口（N 代 VC 堆叠升级形态，LED 琥珀=VFL）<<<PAGE 48>>>/<<<PAGE 60>>>
- **20G VC 口**：基础/E 代"(2) 20G Virtual Chassis link ports"堆叠口 <<<PAGE 14>>>

## 电源体系（Ch3）
- **OS6860-BP（PS-150W-AC）**：150W AC 非 PoE 电源；可与 BP-D 混插 <<<PAGE 71>>>
- **OS6860-BP-D（PS-150W-DC）**：150W DC 非 PoE 电源，-36~-72VDC <<<PAGE 72>>>
- **OS6860-BP-PH（PS-600W-AC-P）**：600W AC PoE 电源 <<<PAGE 73>>>
- **OS6860-BP-PX（PS-920W-AC-P）**：920W AC PoE 电源 <<<PAGE 75>>>
- **OS6860N-BPPH / N-BPPX**：N 代 600W/920W PoE 电源（AC OK+DC OK 双 LED），需 AOS ≥8.7R1 <<<PAGE 74>>>/<<<PAGE 76>>>
- **OS6860N-BPXL**：N 代 2000W PoE 电源（仅 P48M/P24M），115V 降额 1000W，C19 电源线 <<<PAGE 77>>>
- **Lock Tab**：电源锁扣——插入 click 锁定、按中心解锁直拉 <<<PAGE 80>>>/<<<PAGE 81>>>
- **OS-BPS**：备份电源槽——"No longer supported" <<<PAGE 29>>>/<<<PAGE 31>>>
- **FANTRAY NONPOE**：非 PoE 机型风扇托盘（占一个 150W 电源位）<<<PAGE 85>>>
- **DC Cable Harness / CBN / DC-1 / LCD8-10A-L**：DC 三芯线束（绿黄地/黑 return/红 -48V）/共模网络/隔离回流/接地 lug（30-60 in-lb）<<<PAGE 78>>>/<<<PAGE 79>>>/<<<PAGE 83>>>

## LED 体系（Ch3）
- **OK1 / OK2**：主系统/外部 CPU（E 型）诊断启动灯 <<<PAGE 23>>>/<<<PAGE 58>>>/<<<PAGE 59>>>
- **PRI / VC LED**：VC 角色灯——绿=master/琥珀=slave <<<PAGE 23>>>/<<<PAGE 58>>>
- **PS LED 五态 / 电源单 LED 六态**：按双电/单电细分绿琥珀组合；电源稳绿/闪绿待机/闪红邻舱有电/闪绿红告警/稳红故障/灭全停 <<<PAGE 59>>>/<<<PAGE 72>>>
- **6860N 端口五色 LED**：绿=链路/琥珀=PoE/蓝=2.5G/蓝+黄=5G/品红=10G <<<PAGE 60>>>

## 安装与快速入门（Ch2-Ch3）
- **弹簧夹法兰（Rack Mount Flanges）**：clip out→tab 入槽→CLICK→螺丝固定 <<<PAGE 64>>>/<<<PAGE 65>>>
- **Rear Bracket / Guide**：N-P48Z/P48M 后支架与导轨（总长 26.4 in）<<<PAGE 65>>>/<<<PAGE 67>>>
- **盲板（Blank Cover Panels）**：箭头朝上，缺盲板破坏风道 <<<PAGE 62>>>/<<<PAGE 63>>>
- **Micro USB-to-USB cable**：console 线（随机附带）；串口 9600-8N1，N 型 115200 <<<PAGE 20>>>/<<<PAGE 22>>>
- **EMP**：E/N 型后板带外管理口，默认 192.168.1.1/24 <<<PAGE 22>>>/<<<PAGE 24>>>
- **Airflow Considerations**：前 6"/后 6"/侧 2" 间隙，上下免 <<<PAGE 21>>>
- **CDE（Cable Discharge Event）**：电缆静电放电，接线前先瞬时接地 <<<PAGE 19>>>
- **admin/switch / aaa authentication**：默认登录与会话解锁命令（一次一类）<<<PAGE 23>>>/<<<PAGE 25>>>

## 监控与 Dying Gasp（Ch3）
- **show module / show temperature / show powersupply**：巡检三板斧；温度按 VC 逐机箱逐传感器 <<<PAGE 86>>>/<<<PAGE 87>>>/<<<PAGE 91>>>
- **Dying Gasp**：临终告警三通道（SNMP trap/Syslog/802.3ah OAM PDU）<<<PAGE 69>>>/<<<PAGE 70>>>
- **DG PDU 端口挤占公式**：同时发 PDU 口数上限=10−已配 SNMP/Syslog 服务器数 <<<PAGE 70>>>
- **efm-oam propagate-events dying-gasp**：DG 触发 OAM PDU 的口级使能命令 <<<PAGE 70>>>
- **温度双阈值**：Warning 用户可配不停机 / Danger 固化关机须手动重启 <<<PAGE 87>>>

## PoE（Ch4）
- **PD / PSE / PoE**：受电设备/供电设备；PoE=PoL=Inline Power 同义 <<<PAGE 89>>>
- **HPoE**：私有高功率口（E 代 60/75W，not 802.3bt compliant）<<<PAGE 43>>>/<<<PAGE 46>>>
- **lanpower slot service start/stop**：PoE 整槽启停（首次激活必用）<<<PAGE 95>>>
- **lanpower power / slot maxpower / priority**：口/槽功率上限与三级优先级（low/high/critical）<<<PAGE 96>>>/<<<PAGE 97>>>
- **lanpower power-rule**：PoE 定时开关规则命令 <<<PAGE 98>>>
- **Priority Disconnect**：预算不足按优先级+物理口号裁决（920W→780W、600W→450W 每电源）<<<PAGE 99>>>
- **物理口号优先级**：本机型 24/48 口最高→1 最低（端口号越大越高，与接入系列相反）<<<PAGE 100>>>
- **Guard Band**：剩余预算低于口 maxpower 即拒新 PD <<<PAGE 102>>>
- **Fast PoE / Perpetual PoE**：上电数秒供电（FPGA 固化）/软重启不断 PD 电（MCU 升级例外）<<<PAGE 96>>>
- **Class / capacitor detection**：等级检测（开则复位全口）/电容检测（不符 IEEE）<<<PAGE 95>>>/<<<PAGE 98>>>

## 法规与标准（附录 A）
- **UL 60950-1 / UL 62368-1 / Hi-Pot Test**：新旧双安全标准并行合规；IEEE 802.3 耐压全部以太网口 2250V DC <<<PAGE 107>>>/<<<PAGE 108>>>
- **Class 1M Laser / Class A**：激光勿直视（空口加盖）/住宅禁用 Class A <<<PAGE 29>>>/<<<PAGE 110>>>
