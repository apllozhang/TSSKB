---
name: PoE 供电管理（802.3af/at/bt 与功率预算）
description: 需要配置 OmniSwitch PoE 供电（lanpower 命令族）、HPoE 高功率端口、功率预算与端口优先级、电容检测或 EEE 节能时使用本技能。
source_book: DT00CTE120 OmniSwitch R6/R8 Bootcamp Issue 25
---

## R（触发场景）
- 新上 IP 话机/AP/摄像头，需要开通端口供电
- 功率预算紧张，需要按端口设优先级与限额
- 60W/75W 高功率设备（802.3bt）接入规划
- 老式话机不被识别，考虑电容检测
- 机房能耗优化（EEE）

## I（核心理念）
OmniSwitch 用动态 PoE：按需供电至预算上限，优于 IEEE 可选分类（P129，<<<PAGE 694>>>）。分级靠 PD 固定电阻：802.3af Class 0-3（15.4W 顶）、802.3at Class 4（PSE 34.2W/PD 25.5W）（P130，<<<PAGE 695>>>）；高功率 HPoE 60/75W 对应 802.3bt 级（<<<PAGE 33, 54>>>）。电力不足时的仲裁规则是端口优先级三级 low/high/critical——critical 尽量不断电（P131，<<<PAGE 701>>>）。最大的坑是默认值：PoE 操作状态默认 down，必须逐台 `lanpower start` 激活（X76，<<<PAGE 697-698>>>）。

## A1（决策/选型）
1. 功率等级：15.4W（af）→ 30W（at）→ 60W（6860E 前 4 口）→ 75W（6560 mGIG/802.3bt）（<<<PAGE 33, 54, 695>>>）
2. 关键设备（监控话机/核心 AP）标 critical，普通口保持 low/high（P131，<<<PAGE 701>>>）
3. 预算不足场景配 priority-disconnect 决定新 PD 授电与否（P133，<<<PAGE 702>>>）
4. 电容检测仅用于不支持标准分级的旧 IP 话机（P132，<<<PAGE 702>>>）

## A2（操作步骤）
1. R6 命令族：`show power` → `lanpower start 1`（整机开通）→ 端口级 `lanpower start 1/2`、`lanpower 1/9 power 18000`（毫瓦）、`lanpower 1/22 priority critical`、`lanpower 1 capacitor-detection enable`、`lanpower 1 priority-disconnect enable` → `show lanpower 1` 看各口 mW/优先级/预算余量（C35，<<<PAGE 700-703>>>）
2. R8 命令族（slot/port 两级）：`show powersupply` → `lanpower slot 1/1 service start` → `lanpower port 1/1/1 admin-state enable`、`lanpower port 1/1/24 power 18000`、`lanpower port 1/1/6 priority critical`、`lanpower slot 1/1 maxpower 400` → `show lanpower slot 1/1`（C36/P134，<<<PAGE 705-708>>>）
3. EEE 节能：`interfaces 1/1 eee enable`（C37，<<<PAGE 710>>>）

## E（实证案例）
- C35 R6 PoE 管理：启动、限额、优先级、预算观察（<<<PAGE 700-703>>>）
- C36 R8 PoE 管理：slot 级 service start 与 maxpower 预算控制（<<<PAGE 705-708>>>）

## B（反例与坑）
- PoE 操作状态默认 down，须逐台 `lanpower start` 激活（X76，<<<PAGE 697-698>>>）
- 电容检测不符合 802.3af 规范，只对旧 IP 话机开启（X77，<<<PAGE 702, 706>>>）
- PD 分级由 PSE 经 PD 固定电阻判定——分级错误时先查线序/PD 侧电阻（P130，<<<PAGE 695>>>）

## 来源
- principles·P129-P134；cases·C35/C36/C37；counter-examples·X76/X77
