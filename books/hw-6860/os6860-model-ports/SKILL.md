---
name: OmniSwitch 6860 机型命名与端口体系（三代 15 机型/20G VC/SFP28 25G/上联模块）
description: 需要解码 OS6860/6860E/6860N 三代命名（P/E/N/U28/Z/M）、核对面板端口构成（20G VC 口、N 代 QSFP28 VFL、SFP28 四口组禁混速）、选配上联模块（XNI/QNI/VNI/CNI）与堆叠 VC 口规划时使用。
source_book: OmniSwitch 6860/6860E/6860N Hardware Users Guide
---

## R（触发场景）
- 6860 家族选型：在基础/E/N 三代 15 机型中按业务选机型
- 解码命名：P=PoE、E=协处理器增强、N=下一代、U28=全光、Z=多千兆、M=带上联模块槽
- 核对面板端口：20G VC 堆叠口、QSFP28 VFL、SFP28 25G 上联、多千兆铜口
- 为 N-M 型选上联模块（OS68-XNI/QNI/VNI/CNI）或规划 VC 堆叠链路
- 排查"N 型 25G 光口不亮"类问题（SFP28 四口组限速）

## I（核心理念）
6860 家族是同一 1U 44cm 包络内的三代演进（F1/F4，<<<PAGE 14>>>/<<<PAGE 15>>>）：基础代=千兆铜 + 4×SFP+ 10G 上联 + 2×20G VC 口；E 代加内置协处理器（OK2 双系统灯）+ 后面板 EMP 带外口 + 私有 HPoE 60/75W（"not 802.3bt compliant"，P4，<<<PAGE 43>>>/<<<PAGE 46>>>）；N 代全面 bt 95W + 2.5G-10G 多千兆铜口 + SFP28 25G 上联 + QSFP28 VFL，M 型带上联模块槽（P1/P6，<<<PAGE 50>>>-<<<PAGE 56>>>）。选型口诀：普通办公选基础，要协处理器/EMP/私有 60W 选 E，Wi-Fi6 时代 2.5G-5G AP 与 25G 上联选 N。

## A1（行动框架）
1. 三代选型三问（F1）：要协处理器/EMP？→E；要 25G 上联/多千兆 bt 95W？→N；都不需要→基础代
2. 下行口形态定机型：24/48 千兆铜（基础/E）→U28 全光→Z 多千兆混合→M 模块化上联
3. 上行核对：基础/E=4×SFP+(10G)；N=QSFP28×2 VFL + SFP28×4（四口组 31-34 禁 1G/10G 与 25G 混跑，X1，<<<PAGE 48>>>/<<<PAGE 53>>>）
4. VC 堆叠链路：基础/E 用 2×20G VC 口；N 代升级为 2×QSFP28 VFL（P3，<<<PAGE 48>>>/<<<PAGE 50>>>）
5. N-M 型上联模块四选一：OS68-XNI-U4（4×SFP+）/QNI-U2（2×QSFP+ 40G）/VNI-U4（4×SFP28 25G，同四口组限速）/CNI-U1（1×QSFP28 40/100G）（<<<PAGE 56>>>-<<<PAGE 58>>>）

## A2（操作步骤）
- **上联模块装拆**：插入 Slot 2→滑入就位→captive 螺丝固定；拆=松螺丝→握牢直拉（C15，<<<PAGE 84>>>）
- **N 型端口 LED 判读**：绿=千兆链路、琥珀=PoE、蓝=2.5G、蓝+黄=5G、品红=10G；LED2 琥珀=PoE Active；VFL 口绿=uplink/琥珀=VFL（P16，<<<PAGE 60>>>）
- **上电后 LED 快查**：OK1 绿+PRI 绿（master）/琥珀（slave）+PS 绿；E 型另看 OK2 绿（P17，<<<PAGE 23>>>）
- **console 连接**：Micro USB-to-USB 线（随机附带），9600-8N1；N 型 115200（C2，<<<PAGE 22>>>）

## E（实证案例）
- E 代 HPoE 机型口功率域核对：E-P24/E-P48 口 1-4 为 60W HPoE、E-P24Z8 口 17-24 为 75W，均非 bt 合规（X2/P4，<<<PAGE 43>>>/<<<PAGE 45>>>/<<<PAGE 46>>>）
- N-P48M 全口 bt 95W 高功率部署：36×2.5G + 12×100M-10G 均 95W 档，260W 待机/8.5kg，需后支架（P6/P10，<<<PAGE 51>>>/<<<PAGE 52>>>）
- OS68-VNI-U4 四口 SFP28 模块组内限速：组内须全跑 1G/10G 或全跑 25G（X1，<<<PAGE 57>>>）

## B（反例与坑）
- N 型 SFP28 四口组禁混速：31-34 口（P48Z/P24Z 及 VNI-U4）不可 1G/10G 与 25G 混跑；1G 与 10G 混跑允许（X1，<<<PAGE 48>>>/<<<PAGE 50>>>/<<<PAGE 53>>>/<<<PAGE 57>>>）
- HPoE 非 bt 合规：E 代 60/75W 口对严格 bt PD 互通需留意（X2，<<<PAGE 43>>>/<<<PAGE 46>>>）
- OS-BPS 备份电源槽已停支持："No longer supported"，面板图保留但不可用（X3，<<<PAGE 29>>>/<<<PAGE 31>>>）
- 2000W 电源仅 N-P48M/P24M 两款；P48Z/P24Z 标 Not Supported（X4，<<<PAGE 69>>>）
- N 机型/N 电源需 AOS ≥8.7R1 才支持（X6，<<<PAGE 69>>>）
- N 型 M/Z 机箱 44cm 深（基础/E 为 35cm），机柜深度与后支架须提前核对（P10，<<<PAGE 30>>>/<<<PAGE 52>>>）
- Class 1M 激光：空光口勿直视、不用光学仪器看，加盖（X35，<<<PAGE 29>>>/<<<PAGE 110>>>）

来源：OmniSwitch 6860/6860E/6860N Hardware Users Guide（Ch1 p14-17 + Ch3 p27-60 + 上联模块 p84-85）
