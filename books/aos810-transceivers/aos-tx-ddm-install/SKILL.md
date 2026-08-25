---
name: 光模块安装纪律与 DDM/拆分/VFL/功耗温度运维
description: 需要执行光模块安装拆卸（ESD/防尘/激光安全/拔插间隔/释放机构）、用 DDM 做光功率监控、配置 breakout 拆分与 VFL 连接、核对功耗与温度预算时使用。
source_book: OmniSwitch AOS Release 8 Transceivers Guide (8.10R4)
---

## R（触发场景）
- 现场插拔光模块/DAC，要按规范操作避免损坏与误判
- 链路光功率劣化排查，要用 DDM 读温度/电压/电流/ Tx/Rx 功率
- 40G/100G/200G/400G 口要做 breakout 拆分（4X10G/4X25G/2X100G 等）
- VFL（VC 内部互联）口选线（AOC20M/CBL 专用件、BX 不支持）
- 高密 400G/长距模块上线前的电源与风冷预算核算

## I（核心理念）
SFP MSA 标准接口是识别与监控的物理基础（P1，<<<PAGE 13>>>）：20 针插座+笼式外壳，模块内置串行接口提供能力/接口/厂商识别信息——交换机据此识别模块并读 DDM。安装纪律四条（P4-P8，<<<PAGE 14-16>>>）：拔出后同端口至少等 10 秒再插；三种释放机构（铰链面开到 90°、bail wire 压杆、弹出器按钮）各有操作法，任何时候不得强行插拔；ESD 腕带+防尘帽+Class 1 激光安全。DDM 并非人人都有：全部 DAC、铜口 T 系列、SFP-GIG-##CWD、SFP-100-LC-MM/SM15、SFP-DUAL-SM10、QSFP-40G-SR-BD、QSFP-100G-A20M 无 DDM（X31）——这些口无法用 DDM 做光功率监控，排障要靠替代手段。拆分与 VFL 是两类特殊连接形态：拆分线家族（4X10G/4X25G/2XQ100/2XQ200/2Q100）物理拆带宽；VFL 连接有专用件与禁用件清单（P21）。

## A1（决策框架）
1. **插拔先看释放机构类型**：铰链式/ bail wire /弹出器按钮三选一，禁止蛮力
2. **监控选型**：需要光功率监控的链路避开无 DDM 模块清单（X31）
3. **VFL 口选件**：QSFP-40G-AOC20M 与 OS6860-CBL 系列为 VFL 专用（仅 20G VFL）；SFP-10G-BX 系列与 QSFP-40G-SR-BD 明确不支持 VFL——VFL 口选件先查此标注（P21，<<<PAGE 88>>>/<<<PAGE 49>>>/<<<PAGE 37>>>/<<<PAGE 44>>>）
4. **拆分场景**：40G→4×10G 用 MPO-LC splitter 或 QSFP-4X10G；100G→4×25G 用 QSFP-4X25G-C；200G→2×100G 用 2XQ100；400G→2×200G 用 2XQ200、→2×100G 用 2Q100；400G-SR4.2 可拆 4×QSFP-100G-SR1.2
5. **功耗温度预算**：按 P23 梯度（1G/10G ≤1-1.5W … 400G 10-12W）核电源；按 P24 温度档（商用 0-70°C / 工业 -40~85°C / 长距收窄）选址

## A2（操作步骤）
- **安装准备**：ESD 腕带贴皮肤接机壳/接地柱；不用的模块套回橡胶防尘帽；Class 1 激光规范操作（25G/40G/50G/200G/400G 另有 CLASS 1M 开盖勿直视警示）（P7，<<<PAGE 14>>>/<<<PAGE 40>>>）
- **拆卸与重插**：按释放机构操作（铰链面开 90° 拉出、插入时须闭合；bail wire 拉下压杆；弹出器用随机工具顶出再夹出）→ 同端口等 ≥10 秒再插（P4/P5，<<<PAGE 14-16>>>）；QSFP 用橡胶/金属释放手柄直拉（P8）；OS6865 笼体有轻微压力，难拔时左右轻晃稳拉（P6）
- **40G MPO 拆 4×10G**：MTP-LC 母头 splitter，8 芯对应 4 个 LC，LC 可手工重排收发（P10，<<<PAGE 17>>>）；QSFP↔QSFP 直连 MPO trunk 用 Type-B 交叉线（glossary，<<<PAGE 17>>>）
- **双速模块定速**：dual-speed 收发器两端手工配速防止速率失配（P15，<<<PAGE 25>>>）
- **SFP28 口接 1G**：对端交换机禁用自协商（P16，<<<PAGE 92>>>/<<<PAGE 102>>>）
- **功耗梯度速查**（P23）：10G-T 铜口 2.5W@30m；25G 1.2-1.5W；40G 1.5-3.5W；50G 2-3.3W；100G 3.5-4.5W；200G 4.5-6W；400G 10-12W——高密 400G 先核电源与风冷
- **温度档速查**（P24）：商用 0~70°C（个别 -5/-20/85 端点）；工业 iSFP -40~85°C；LH40/LH70/EZX 上限收窄到 -10/-5~70°C

## E（实证案例）
- 本书无配置流程案例（物理安装说明已并入条目）；"场景"即现场操作与运维：按 A2 步骤执行插拔/监控/拆分，模块级参数回 aos-tx-module-matrix、平台支持回 aos-tx-platform-compat 查证

## B（反例/坑）
- 拔出模块后不足 10 秒重插——软件来不及做拔出检测，可能识别异常（P4，<<<PAGE 14>>>）
- 无 DDM 模块清单：全部 DAC（SFP-10G-C/QSFP-40G-C/100G-C/200G·400G 拆分线）、铜口 T 系列、SFP-GIG-##CWD、SFP-100-LC-MM/SM15、SFP-DUAL-SM10、QSFP-40G-SR-BD、QSFP-100G-A20M（X31，<<<PAGE 20-63>>>）——这些链路的光功率劣化无法在交换机侧预警
- 40G SR4 的 DDM 仅 V/T/mA/Input 四项（不全量）（<<<PAGE 44>>>）
- 拆分模式牺牲自动 VFL：6870 QSFP-100G-SR4 splitter 模式不支持 Auto-VFL（P20，<<<PAGE 96>>>）
- VFL 用错件：AOC20M 仅 20G VFL、CBL 为 20G VFL 线；BX/SR-BD 不支持 VFL（P21）
- 100G A20M 需禁自协商+FEC RS，否则链路异常（P27/X27，<<<PAGE 55>>>）
- 高速模块发热量级差异大：同封装不同距离档功耗差数倍（SR4 4.5W vs FR4 6W vs 400G DR4 10W），高密部署按逐口功耗累加核预算（P23）

## 来源
OmniSwitch AOS Release 8 Transceivers Guide Ch1 前言（MSA/安装/安全，<<<PAGE 11-17>>>）、各速率节 DDM/功耗/温度列（<<<PAGE 18-63>>>）、Ch2 脚注（VFL/自协商，<<<PAGE 75-107>>>）。条目来源：principles P1/P4-P11/P15/P16/P20/P21/P23/P24/P27；counter-examples X26/X27/X31。
