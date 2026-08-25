---
name: OmniSwitch 9900 机箱与模块体系（9907/9912 槽位/CMM-CFM 兼容矩阵/NI 谱系/VC-of-2）
description: 需要选型 OS9907（11RU 七槽）或 OS9912（17RU 十二槽）、核对 CMM/CMM2 与 CFM/CFM2 兼容组合矩阵、slot2 双角色权衡、11 种 NI 模块谱系与 9912 不支持清单、VC-of-2 双机箱虚拟化组合时使用。
source_book: OmniSwitch 9900 Series Hardware Users Guide
---

## R（触发场景）
- 核心/园区骨干选型：OS9907（11RU，2 CMM+5 NI）vs OS9912（17RU，2 CMM+10 NI）
- 管理模块与交换矩阵升级规划：CMM/CMM2、CFM/CFM2 的 AOS 版本门槛与混插禁令
- slot2 取舍：9907 上 slot2 装 CMM（1+1 冗余）还是装 NI（扩端口但只活 8 口且失冗余）
- NI 模块选型：11 种模块（铜/光/PoE/高速）与 9912 不支持的四款 NI
- 双机箱虚拟化 VC-of-2 的组合约束

## I（核心理念）
9907 vs 9912 选型矩阵（F1，<<<PAGE 5>>>/<<<PAGE 6>>>/<<<PAGE 11>>>/<<<PAGE 22>>>/<<<PAGE 24>>>-<<<PAGE 26>>>）：高度（11RU/17RU）、槽位数（7/12）、重量（32.83/64.36kg）、CFM 带宽阶梯，共性为 4 电源 N+1、仅前→后气流、23 英寸深。CMM/CFM 兼容组合决策表（F2，<<<PAGE 17>>>/<<<PAGE 20>>>/<<<PAGE 22>>>）：只有三种同箱组合支持（旧体系、CMM+CFM2、CMM2+CFM2 各自对称），一切新旧混插 Not Supported，升级路径只有整代切换。CFM 带宽叠加模型（P14，<<<PAGE 20>>>/<<<PAGE 21>>>）：每加一块 CFM 即增加矩阵带宽（2.56T→12.8T→25.6T），CFM 藏于风扇托盘之后、经中板连接（P4/P15）。slot2 双角色是 9907 的架构级权衡：装 NI 换端口密度，代价是 CMM 无冗余且 NI 只活前 8 口（P2/P3，<<<PAGE 7>>>/<<<PAGE 16>>>/<<<PAGE 17>>>）。

## A1（行动框架）
1. 机箱选型走 F1：端口规模定 9907/9912 → 查 9912 不支持 NI 清单（P48Z16/P24Z8/UP24Q2/U12Q）→ 核机架承重与 23" 深度
2. CMM/CFM 代际决策走 F2：现网 AOS 版本 → 目标组合（CMM2 需 ≥8.10R2、CFM2 需 ≥8.9R1）→ 整代切换不可混
3. slot2 冗余权衡：要 1+1 CMM 冗余则 slot2 装 CMM；要端口则接受"NI 只活 8 口+失冗余"
4. NI 选型按谱系四象限：铜（XNI-48/GNI-48）→ 光（XNI-U48/U24、GNI-U48）→ PoE（GNI-P48/P48Z16/P24Z8/UP24Q2）→ 高速（CNI-U8/U20、XNI-U12Q）
5. VC-of-2 规划：两箱必须对称组合（CMM+CFM ↔ CMM+CFM 等三种），其余 Not Supported

## A2（操作步骤）
- **核对槽位布局**：9907 NI 槽 3-7、9912 NI 槽 3-12；CFM1/2 可用、CFM3/4 预留未激活不可当可用槽（X8，<<<PAGE 5>>>/<<<PAGE 10>>>/<<<PAGE 15>>>）
- **CMM 面板核对**：CMM=2×40G QSFP+ 上行 64W；CMM2=4×100G QSFP28+VFL 74W；均带 RJ45+Micro-USB 双 console 与 EMP（P9-P11，<<<PAGE 16>>>/<<<PAGE 17>>>）
- **CFM 带宽与功耗**：OS9907-CFM=2.56T/119W、CFM2=12.8T/119W、OS9912-CFM=25.6T/222W（P14，<<<PAGE 20>>>/<<<PAGE 21>>>）
- **NI 规格核对**：功耗谱 56-402W（XNI-48 402W 最重）；HPoE 模块前 8 口 75W 面板标 "HPoE"（P18/P19，<<<PAGE 23>>>-<<<PAGE 26>>>）
- **CNI-U20 分支口**：13-20 口支持 splitter（P21，<<<PAGE 26>>>）
- **CMM LED 诊断语义**：PRI（稳绿=主/闪绿=备/稳黄=停运/闪黄=升级中）；FAB 闪黄=CFM 电源或 PCIe 失败；五灯同闪=全部 CFM PCIe 链路失效（P12，<<<PAGE 18>>>）
- **拇指螺丝识别**：新批次铝头替代紫色塑料头，机械性能相同勿困惑（P7，<<<PAGE 6>>>/<<<PAGE 12>>>）

## E（实证案例）
- OS9907 组合兼容矩阵三支持三禁止：CMM+CMM/CFM+CFM、CMM+CMM/CFM2+CFM2、CMM2+CMM2/CFM2+CFM2 支持；任何混插 Not Supported（P16/X3，<<<PAGE 22>>>）
- VC-of-2 三种对称组合（CMM+CFM ↔ CMM+CFM；CMM+CFM2 ↔ CMM+CFM2；CMM2+CFM2 ↔ CMM2+CFM2），其余 Not Supported（P17/X4，<<<PAGE 22>>>）
- slot2 装 XNI-U48 只活前 8 口（9907），CMM 冗余同时丢失（X6/X7，<<<PAGE 7>>>/<<<PAGE 16>>>/<<<PAGE 17>>>）
- QSFP 上行 LED 多维编码：Off=Down/无收发器；绿(A)=40G/100G；绿(A/B/C/D)=4X10G/4X25G 分支；蓝=VFL（P13，<<<PAGE 19>>>）

## B（反例与坑）
- CMM 与 CMM2 不可同箱混插（CMM2 需 AOS ≥8.10R2）；CFM 与 CFM2 不可混插（CFM2 需 ≥8.9R1）；组合矩阵三禁（X1/X2/X3，<<<PAGE 17>>>/<<<PAGE 20>>>/<<<PAGE 22>>>）
- 9912 不支持四种 NI：XNI-P48Z16 / XNI-P24Z8 / XNI-UP24Q2 / XNI-U12Q（X5，<<<PAGE 24>>>/<<<PAGE 25>>>/<<<PAGE 26>>>）
- CFM3/4 预留未激活（"currently inactive and reserved for future use"），不可当可用槽规划（X8，<<<PAGE 5>>>/<<<PAGE 10>>>/<<<PAGE 15>>>）
- slot2 装 NI 即失 CMM 冗余且 NI 只活 8 口——扩端口的隐性代价（X6/X7，<<<PAGE 7>>>/<<<PAGE 16>>>/<<<PAGE 17>>>）
- VC-of-2 双机箱只允许对称组合，非对称组合 Not Supported（X4，<<<PAGE 22>>>）
- 满配重量 32.83/64.36kg 起步：禁止满载搬运，先就位空机箱再逐件装模块（X25/C3，<<<PAGE 32>>>）
- PoE Priority Disconnect 端口优先方向为 48（最高）→1（最低），与 6865/6870/6560 等接入系列（1 高 48 低）相反——跨平台套用优先级规划会反噬，预算不足时被断电的口正好相反（X38/P31，<<<PAGE 55>>>）

来源：OmniSwitch 9900 Series Hardware Users Guide（Ch1 机箱与电源架构，p5-31）
