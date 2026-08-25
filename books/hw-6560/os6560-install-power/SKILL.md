---
name: OmniSwitch 6560 安装与供电体系（机架/DNV 船用/三档电源/PoE 预算）
description: 需要安装 OS6560（机架法兰/桌面/DNV 船用套件）、选配 PoE 电源（300/600/920W）与核对混插规则、规划 PoE 预算（双 PX 最高 1565W）、DC 接线与接地时使用。
source_book: OmniSwitch 6560 Hardware Users Guide
---

## R（触发场景）
- 新机上架：机架法兰/整机双人安装/桌面摆放/DNV 船用套件（P48X4/X10）
- PoE 供电规划：按 PD 总功率选 BP-P/PH/PX 电源档与数量
- 核对电源混插规则与 PN 版本兼容（BP-P 不配 E 机型）
- -48VDC 场景接线（BP-D/DC 线束）与 supplemental 接地

## I（核心理念）
电源-PoE 预算联动框架（F2，<<<PAGE 60>>>/<<<PAGE 87>>>/<<<PAGE 88>>>）：单电源预算≈wattage−系统 110W 封顶，双电源负载分担预算≈2×单电源（P48X4 双 PX=1440W）。部署三查：一查机型×电源×数量预算表；二查 PN 版本（老 903852/903853 vs 新 904071/904072/904073，新件需 AOS ≥8.8R1，P8/P9，<<<PAGE 60-63>>>）；三查混插规则（wattage 禁混 X4，BP+BP-D 唯一例外 X6，混插发 trap X5）。DNV 船用体系仅限 P48X4/X10：OS-DNV-MNT 套件+OS-DNV-FILTER EMC 滤波器串接电源与机箱之间，滤除 10kHz-150kHz 传导发射（P19/P20，<<<PAGE 58>>>/<<<PAGE 67>>>）。

## A1（行动框架）
1. 安装形态选择：标准机架（法兰 C3/C4）→桌面（C5，禁倒放侧放）→DNV 船用（C7）
2. 电源选型：非 PoE 机型=内置 65W+BPS 槽；PoE 机型按预算表选 P/PH/PX（F2）
3. 供电冗余：双电源各接独立电路+UPS（911 纪律 P33）；无电源开关语义=接电即开机（P12）
4. DC 场景：BP-D（-36~-72V）三芯 12AWG 线束+15A 过流+SELV+CBN 接地（P14，<<<PAGE 65-69>>>）

## A2（操作步骤）
- **机架安装**：法兰弹簧夹 out→tab 入槽→CLICK→螺丝固定（C3，<<<PAGE 54-55>>>）；整机双人作业、重物下置（C4/P27，<<<PAGE 53>>>/<<<PAGE 56>>>）
- **DNV 安装**：OS-DNV-MNT 侧轨+后托架固定→前托架入位→滤波器 C14 入/C15 出串接（C7，<<<PAGE 58-59>>>）
- **电源插拔**：插入至背板 click 锁定（C9）；拆=按锁扣向中心直拉（C10，<<<PAGE 70-73>>>）
- **DC 接线**：绿黄=地/黑=return/红=-48VDC；前提五条（X20，<<<PAGE 68>>>）
- **supplemental 接地**：LCD8-10A-L 接地耳+8AWG+30-60 in-lb（C8，<<<PAGE 74>>>）
- **盲板**：空槽常装、箭头朝上（C6/X17，<<<PAGE 52>>>）
- **PoE 激活**：show powersupply 确认→lanpower slot service start→逐项核对（C14，<<<PAGE 87-89>>>）

## E（实证案例）
- PoE 首次激活与逐口核对流程（C14，<<<PAGE 87-89>>>）
- Guard Band 拒载处置：降口上限放行 4W PD（C18，<<<PAGE 92>>>）
- DC 线束接线全流程（C11，<<<PAGE 68-69>>>）

## B（反例与坑）
- wattage 禁混：300/600/920 之间不可混插，混插或不支持电源发 console 告警+trap（X4/X5，<<<PAGE 61-63>>>/<<<PAGE 88>>>）
- BP-P 300W 不配 E 机型与新 PN 的 P48Z16（X2，<<<PAGE 60>>>/<<<PAGE 87>>>）
- 新 PN 电源需 AOS ≥8.8R1（X3，<<<PAGE 60>>>）
- 气流遮挡致过热失效；盲板必须常装（X15/X17，<<<PAGE 17>>>/<<<PAGE 52>>>）
- 禁延长线；电涌五条军规违反可能失保（X13/X14，<<<PAGE 15-16>>>）
- DC 维护红线：运行中勿触电源舱/背板；雷暴禁作业（X21/X18，<<<PAGE 106-107>>>）

来源：OmniSwitch 6560 Hardware Users Guide（安装 Ch3 + PoE Ch4，p51-95）
