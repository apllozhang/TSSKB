---
name: OmniSwitch 产品与硬件平台选型（Bootcamp Day1）
description: 需要了解 OmniSwitch 全系产品定位（6350/6450/6560/6860/6900/9900）、速率演进选型、9900 模块化架构、电源冗余与 BPS 备电、硬件状态巡检命令时使用本技能。
source_book: DT00CTE120 OmniSwitch R6/R8 Bootcamp Issue 25
---

## R（触发场景）
- 新建园区/数据中心网络，需要按接入-汇聚-核心分层选择 OmniSwitch 机型
- 评估 2.5G/10G/25G/100G 速率演进路径与上联带宽规划
- 9900 模块化机箱的 CMM/NI/CFM 板卡设计与供电预算核算
- 电源冗余（N+1/N+N）与 Omni BPS 备电柜选型
- 到货验收或例行巡检，需要硬件信息/电源/风扇/健康状态检查命令

## I（核心理念）
OmniSwitch 家族分三层产品线：堆叠式（6350/6450/6560）、工业加固（6465/6865）、模块化（6900/9900）（P1，<<<PAGE 19>>>）。选型沿着"速率演进主线"走：接入 100M→1G→2.5G、汇聚 1G→2.5G→10G、核心 10G→25G→40G→100G（P2/F3，<<<PAGE 21>>>）。产品组合按 Size（Small/Medium/Large/Hardened）×能力（Value L2+/L2+ Basic L3/Advanced L3）放入同一矩阵（F2，<<<PAGE 23, 30, 41, 51>>>）。硬件运维的底层逻辑是"系统上电优先，剩余功率全部给 PoE"（9900 最高 10800W，P14，<<<PAGE 106-107>>>）；电源冗余的两种模式防的故障不同，选错模式等于没冗余（P9，<<<PAGE 63-64>>>）。

## A1（选型决策）
1. 入门/SMB：6350（L2+ GE、IPv4/IPv6 基础 L3、Auto-QoS、8 硬件队列，P3，<<<PAGE 27>>>）
2. 多千兆接入：6560 mGIG 机型（24Z8/24Z24/P48Z16，100/1G/2.5G + 802.3bt 75W，P4，<<<PAGE 33>>>；电源复用 6860 体系 300/600/900W 负载分担，P5，<<<PAGE 39>>>）
3. 高级 L3 接入/汇聚：6860/6860E——E 型带协处理器（约 1000 签名发现/100 签名线速匹配 DPI）、前 4 口 60W PoE、仅 E 型有 EMP 口（P7，<<<PAGE 52-56>>>）
4. 数据中心/核心：6900 系列——2011 10G → 2015 40G → 2018 25G/100G（X72/V72/C32）（P10，<<<PAGE 78>>>）；Q32 每管道 ≤240Gbps 才线速，40G 口可分裂 4x10G（a/b/c/d 子编号，P11，<<<PAGE 85>>>）
5. 机箱核心：9907/9900 无背板直连架构（每槽直连 CFM 交换网板，两阶段容量翻倍，P13，<<<PAGE 98>>>）
6. 工业场景：6465（-40~+75℃、DIN 导轨、1588v2/MACsec，P6，<<<PAGE 42-43>>>）或 6865（SPB、75W HPoE，<<<PAGE 66-74>>>）
7. 电源冗余：N+1（SINGLE）只防电源模块故障；N+N（FULL）才防市电线路故障（P9，<<<PAGE 63-64>>>）；BPS 备电柜最多备 8 台、一次只备份一台交换机（<<<PAGE 60-64>>>）

## A2（操作步骤）
- 硬件巡检命令集：`show hardware info`(R6)/`show hardware-info`(R8)、`show microcode`、`show chassis`、`show cmm`、`show power`(R6)/`show powersupply`(R8)、`show fan`、`show health`（C1，<<<PAGE 206-209>>>）
- 端口参数：`interfaces 1/1 duplex full`(R6)/`interfaces 1/1/1 duplex full`(R8)、`speed 1000`、`admin up`(R6)/`admin-state enable`(R8)；验证 `show interfaces 1/1 status/accounting/counters`（C2，<<<PAGE 210>>>）
- V72/C32 机型镜像为 Yos.img，与其余 6900（Tos.img）不同，升级时不可混用（P12，<<<PAGE 86-87>>>）
- 软件加固配套：CodeGuardian 三层（IV&V 源码验证 → 每版本 5 种衍生镜像 → 随机下载安全交付）（P15/F17，<<<PAGE 109-111>>>）；运维侧配合 ProActive Lifecycle（OmniVista 2500 每两周推送资产/软件/保修状态，F18，<<<PAGE 1139-1140>>>）

## E（实证案例）
- C1 硬件信息与运行状态检查：全家桶 show 命令 + session 超时配置对比验证（<<<PAGE 206-209>>>）
- C2 端口参数与计数器观察：R6/R8 双语法对照（<<<PAGE 210>>>）

## B（反例与坑）
- 6860 与 6850E 不可共用一台 BPS（X1，<<<PAGE 58, 61>>>）；BPS 一次只备份一台交换机（X3，<<<PAGE 63>>>）
- N+1 备电不防市电断电（X2，<<<PAGE 63>>>）
- 6860E-P24Z8 的 2.5G 口自动协商只到 1G，2.5G 须手工且成对修改（17,18）（19,20）（X7/P8，<<<PAGE 55>>>）
- 6860E 电源 600W 与 920W 不可混插（X8，<<<PAGE 55>>>）
- CodeGuardian 美加强制一年订阅、其余地区可选（X87，<<<PAGE 111>>>）；ProActive Lifecycle 需本地 OmniVista 2500（X88，<<<PAGE 1139>>>）

## 来源
- principles·P1-P15；frameworks·F2/F3/F17/F18；cases·C1/C2；counter-examples·X1/X2/X3/X7/X8/X84/X87/X88
