---
name: OmniSwitch 6465 运维与排障（告警继电器/Dying Gasp/LED/温度红线）
description: 需要配置 OS6465 告警继电器（输入/输出/事件映射/自动清除）、部署 Dying Gasp 三通道失电通告、巡检 show module/temperature、按 LED 诊断、核对工业红线（NEBS OSP/认证）时使用。
source_book: OmniSwitch 6465 Hardware Users Guide
---

## R（触发场景）
- 无人值守站点要把温度/门磁等外部传感器接告警输入、联动本地声光/PLC 输出
- 把系统事件（认证失败/电源故障/Link-Down 等）映射到继电器输出或 trap
- 站点失电要被网管感知：Dying Gasp 三通道（SNMP/Syslog/OAM PDU）
- 日常巡检 show module/temperature/powersupply；LED 异常判断
- 处置温度 Warning trap 或 Danger 关机；核对 NEBS/OSP 接线红线

## I（核心理念）
失电感知与告警双体系（F3，<<<PAGE 63>>>/<<<PAGE 65>>>/<<<PAGE 68>>>/<<<PAGE 69>>>）：预防侧=告警继电器（外部传感器输入 5-12VDC+8 类系统事件，独立/VC 两模式，映射到 NO/C/NC 输出，条件恢复自动清除）；亡故侧=Dying Gasp（残电三通道：SNMP trap 前 3 站+Syslog 前 3 服务器+4 个 802.3ah OAM PDU 上联口优先）。告警 VC 同步机制（P19）：VC 中任一机的输入/事件可驱动任一机的输出。温度双阈值与 6360 同构（P24）：Warning trap 不停机/Danger 自动关机需手动重启且不可配；各机型阈值梯度不同（P8：75-95/83-97°C）。

## A1（决策框架）
1. **本地告警选继电器输出**：传感器/事件→alarm map→NO/C/NC 干接点（220VDC/250VAC·2A·60W）接声光/PLC（P18，<<<PAGE 63>>>）
2. **远端失电感知选 DG**：SNMP trap+Syslog 站点配置+上联口 efm-oam PDU 三通道并行（P21，<<<PAGE 68>>>）
3. **VC 部署告警同步**：跨机箱输入/事件同步，支持多对一/一对多映射（P19，<<<PAGE 63>>>）
4. **告警不清自愈**：8 类事件条件恢复自动清除；其余 `alarm clear status` 手工清（P20，<<<PAGE 65>>>）
5. **LED 分层诊断**：OK（绿/闪绿/琥珀=失败）、PS1/PS2（绿/琥珀/灭）、Alarm In/Out（琥珀=检测到）（<<<PAGE 36-37>>>）

## A2（操作步骤）
- **告警输入→输出映射**：`alarm in temperature-alarm-in action alarm-out admin-state enable`→`alarm out alarm-out-1 admin-state enable`→`alarm map temperature-alarm-in out alarm-out-1`（C16，<<<PAGE 64>>>）
- **系统事件→输出**：`alarm event auth-fail-event event authentication-failure admin-state enable`→`alarm out ...`→`alarm map ...`→`show alarm event config`/`show alarm status` 核对（C17，<<<PAGE 64>>>）
- **手工清除**：`alarm clear status`（C18，<<<PAGE 65>>>）
- **DG OAM 通告**：`efm-oam admin-state enable`→`efm-oam port 1/1/23-24 admin-state enable`→`efm-oam port 1/1/23-24 propagate-events dying-gasp enable`（PDU 上联口优先）（C19，<<<PAGE 68-69>>>）
- **DG 接收端**：`snmp station` 配 trap 站（前 3 站生效）；`swlog output socket` 加 Syslog 服务器（<<<PAGE 68>>>）
- **硬件巡检**：show module/long→show temperature（UNDER THRESHOLD 正常）→Danger 关机处理后手动启动（C20，<<<PAGE 66-67>>>）

## E（实证案例）
- 认证失败事件驱动告警输出全流程（C17，<<<PAGE 64>>>）
- DG 触发场景：单电源失效/主备先后全失——双电源分独立电路降低触发概率（C1，<<<PAGE 15>>>）
- 各机型 Warning/Danger 阈值梯度：P6 93/94、P12 95/97、ENH-240 84/89、P28 80/86、T-12 75/83、T-P12 78/85°C（P8，<<<PAGE 24-36>>>）

## B（反例/坑）
- **本机型注意**：Danger 阈值出厂固化不可配（X25，<<<PAGE 67>>>）；且本机 24V 输入存在检测电路缺陷——PS LED 不亮不代表电源真坏（X1，<<<PAGE 24>>>）
- DG 的 OAM PDU 通道需先在端口使能 efm-oam 并开 propagate-events dying-gasp，否则对端收不到失电通告（C19）
- 告警输出触点上限 220VDC/250VAC·2A·60W，超限外接会损坏继电器（P18）
- NEBS 红线：楼内端口禁金属直连 OSP 室外线路，加 Primary Protectors 也不够；AC 须接 SPD（X17，<<<PAGE 93>>>）
- T 机型不满足工业认证清单（X7）；Class A 住宅禁用（X23）；雷暴禁作业（X16）；锂电池更换须返厂（X22）

## 来源
OmniSwitch 6465 Hardware Users Guide Ch3 告警/温度/DG（<<<PAGE 63-69>>>）、Ch4 PoE（<<<PAGE 70-84>>>）、附录 A 工业认证与 NEBS（<<<PAGE 85-99>>>）。条目来源：cases C1/C16-C20；principles P8/P17-P24/P26；counter-examples X1/X7/X16/X17/X22/X23/X25；frameworks F3。
