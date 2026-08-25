# DIGEST — OmniSwitch 6560 Hardware Users Guide 精华

本书是 ALE 多千兆（2.5G/5G 802.3bt）接入交换机 OS6560 家族的硬件手册（111 页，13 个 1U 机型）。核心卖点：Wi-Fi6/Wi-Fi7 时代的多千兆 bt 供电接入 + 20G QSFP+ VFL。全书沿"选型→安装→上电→PoE→监控"生命周期展开。

## 一、知识地图（三技能单元）

1. **机型与端口体系**（os6560-model-ports）：Z/E 命名解码、多千兆口位、10G 许可口、VFL（Ch1/Ch3，p12-49）。
2. **安装与供电**（os6560-install-power）：机架/桌面/DNV 船用、三档可热换电源（300/600/920W）、PoE 预算联动、DC 接线（Ch2-Ch4，p51-95）。
3. **运维与排障**（os6560-ops-troubleshoot）：lanpower 全家桶、Dying Gasp 三通道、温度双阈值、LED 诊断（Ch2-Ch4，p19-96）。

## 二、三单元要点串讲

### 1. 机型与端口：多千兆三轴矩阵
命名（<<<PAGE 12-13>>>）：`P`=PoE；`Z8/Z24/Z16`=2.5G bt 口数；`E`=增强版指定口段升 5G；`X4`=4×SFP+ 上行；`X10`=纯上联。10G 许可口：X4 家族 49-50 口 SFP(+) 默认 1G，10G 需软件许可（<<<PAGE 30-44>>>）。双 PX 电源 PoE 预算最高 1565W（<<<PAGE 87>>>）。陷阱：BP-P 300W 电源不配 E 机型与新 PN 的 P48Z16；新 PN（904072/904073-90）需 AOS ≥8.8R1（<<<PAGE 60>>>）。

### 2. 安装与供电：可热换电源与混插规则
与 6360（内置电源）不同，6560 为可热换模块化电源：BP-P 300W/BP-PH 600W/BP-PX 920W 三档，同 wattage 双电源负载分担（<<<PAGE 60-63>>>）。混插规则：wattage 禁混（发 trap 告警）；唯一例外 BP（AC）+BP-D（DC）150W 可同箱（<<<PAGE 64-65>>>）。DNV 船用套件仅限 P48X4/X10：OS-DNV-MNT 托架+OS-DNV-FILTER EMC 滤波器（10kHz-150kHz）（<<<PAGE 58-67>>>）。DC 接线三芯 12AWG（绿黄=地/黑=return/红=-48V）+15A 过流+SELV（<<<PAGE 68-69>>>）。

### 3. 运维与排障：PoE 语义与失电通告
lanpower 命令族（<<<PAGE 89-95>>>）：slot service 两级激活（admin-state 仅复活）；power/maxpower 上限不预留；priority 三级；Priority Disconnect 同级按物理口号 **1 高 48 低** 裁决；Guard Band 余量低于口上限即拒新 PD（解法=降口上限）。Dying Gasp 三通道：SNMP trap（前 3 站）+Syslog（前 3 服务器）+4 个 802.3ah OAM PDU 上联口优先（<<<PAGE 78-82>>>）。温度双阈值：Warning 用户可配不停机，Danger 固化关机需手动重启（<<<PAGE 76>>>）。

## 三、本书在知识库中的位置

与 hw-6360（入门千兆）、hw-6465（工业加固）构成接入家族三线——6560 定位多千兆 bt 旗舰、可热换电源、预算上限 1565W。跨书易混点：本机型 Priority Disconnect 为"端口号 1 高 48 低"（接入系列通用），与 hw-9900 的"48 高 1 低"相反；电源可混插场景仅 BP+BP-D。

## 来源
OmniSwitch 6560 Hardware Users Guide（Rev. P, 2025-12）。verified.md：cases C1-C22；principles P1-P34；counter-examples X1-X27；frameworks F1-F3；glossary 约 60 条。
