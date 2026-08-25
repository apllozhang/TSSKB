---
name: OmniSwitch 6870 机型命名与端口体系（九机型/QSFP56 200G/M 模块化上联槽/bt 95W）
description: 需要解码 OS6870 九机型命名（M/Z/V/CNI/LNI）、核对面板端口（多千兆 RJ45、SFP28 25G、QSFP28 100G、QSFP56 200G、Uplink Module Slot）、规划 VFL 堆叠与 95W bt AP 接入时使用。
source_book: OmniSwitch 6870 Hardware Users Guide
---

## R（触发场景）
- 6870 家族选型：在九机型中按 PoE 等级 × 上行速率 × 模块化三轴选型
- 解码命名：P=PoE、M=Modular（上行模块槽+95W bt+QSFP56）、Z=固定多千兆 60W bt、V=全光、CNI/LNI=上行扩展节点
- 核对面板端口：多千兆 RJ45（2.5G-10G）、SFP28/QSFP28/QSFP56 上行、VFL
- 规划 Wi-Fi6/WiFi7 AP 95W bt 供电接入或 200G 上行
- 判读 RJ45 四色速率 LED 与 VFL 口状态

## I（核心理念)
6870 是九机型三分类家族（P1，<<<PAGE 12>>>）：非 PoE 固定（-24/-48/V12/CNI-U2/LNI-U6）；P*M 模块化（95W bt 多千兆 + 2×QSFP56 200G + Uplink Module Slot）；P*Z 固定（60W bt 多千兆至 2.5G + 6×SFP28 + 2×QSFP28 100G）。上行速率阶梯（P2，<<<PAGE 23>>>/<<<PAGE 25>>>）：SFP28=1G/10G/25G（25G 推荐 VFL）→QSFP28=40G/100G→QSFP56=40G/100G/200G。选型决策三问（F1）：要不要 95W AP？→M；要不要 200G/后配上行？→M/V12；预算型 60W PoE？→Z。

## A1（行动框架）
1. 三分类定位（F1）：纯千兆非 PoE=24/48；95W bt+200G+模块槽=P24M/P48M；60W bt 固定=P24Z/P48Z；全光=V12；上行扩展=CNI-U2/LNI-U6
2. 下行核对：M 系列 24 口至 10G（P24M）/48 口至 5G（P48M）；Z 系列至 2.5G；下行 PoE M=95W bt、Z=60W bt
3. 上行核对：24/48=4×SFP28+2×QSFP28；Z=6×SFP28+2×QSFP28；M/V12=2×QSFP56；CNI-U2=2×QSFP28、LNI-U6=6×SFP56(50G)
4. VFL 规划：VFL 口可作 VC 堆叠或普通上行；SFP28 口 25G 推荐用于 VFL（X45，<<<PAGE 23>>>）
5. 环境包络核对：全家族 Tmra 0-45°C、1U 4.4cm、湿度 5-95%（P6）

## A2（操作步骤）
- **面板识别**：逐机型端口构成查 F1 表（<<<PAGE 12>>>/<<<PAGE 23>>>-<<<PAGE 38>>>）
- **RJ45 四色速率 LED 判读**：绿=10/100/1000、蓝=2.5G、品红=5G、琥珀=10G；LED2 琥珀=PoE 使能（P23，<<<PAGE 39>>>）
- **光口 LED 两色**：绿=有效上行、琥珀=有效 VFL（P24，<<<PAGE 39>>>）
- **系统 LED 五组**：OK（稳绿=诊断与启动 OK/闪绿=进行中/琥珀=失败）；VC（绿=Master/琥珀=Slave/灭=未知）；PS（绿=正常/琥珀=单双故障/灭=无电源）；GRN（绿=省电模式）；VC ID（多灯数值相加=单元号）（P22，<<<PAGE 38>>>/<<<PAGE 39>>>）
- **温度语义区分**：chassis 温度=机箱内部传感器（恒高）；ambient=近似室温（P9，<<<PAGE 24>>>）
- **console 连接**：rollover 线，115200-8N1（注意与 6360/6865 的 9600 不同）（<<<PAGE 17>>>）

## E（实证案例）
- 95W bt 高密 AP 部署：P48M 48 口多千兆（至 5G）95W bt + 2×QSFP56 + 上行模块槽，待机 251.8W、双 2000W 电源预算最高 3309W（<<<PAGE 31>>>/<<<PAGE 63>>>）
- 预算型 60W PoE：P48Z 48 口多千兆（至 2.5G）60W bt + 6×SFP28 + 2×QSFP28，待机 92.4W，不支持 2000W 电源（X30，<<<PAGE 33>>>）
- 全光接入：V12=12×SFP28（25G 推荐 VFL）+ 2×QSFP56 + 上行模块槽，无铜口（P4，<<<PAGE 35>>>）

## B（反例与坑）
- Z 系列不支持 2000W 电源（PS-2000W-AC-POE-2 仅 P24M/P48M），预算规划不可套用（X30，<<<PAGE 47>>>/<<<PAGE 63>>>）
- 全部 RJ45 机型不支持半双工（X38，<<<PAGE 23>>>）
- 待机功耗梯度大：-24=71W → P48M=251.8W，机柜供电与散热规划按 M 系列高功耗预留（P8）
- Class 1M 激光：空光口勿直视、禁光学仪器，加盖（X33/X34，<<<PAGE 23>>>/<<<PAGE 81>>>）
- 跨书易混：6870 的 SFP28 允许 1G/10G/25G 同口组混跑（无 6860 N 型四口组禁混速限制）；QSFP56 200G 为本家族独有上行档
- M 系列上联形态可后置扩展（Uplink Module Slot），但 V12/CNI/LNI 无铜口，纯光部署需另配光电转换

来源：OmniSwitch 6870 Hardware Users Guide（Ch1 p12-13 + Ch3 p22-39）
