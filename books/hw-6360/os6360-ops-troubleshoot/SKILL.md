---
name: OmniSwitch 6360 运维与排障（LED 诊断/温度/规格红线）
description: 需要巡检 OS6360 硬件状态（show module/temperature）、按 LED 诊断故障、处置温度告警、完成首次登录六步、核对规格红线与安全禁令时使用。
source_book: OmniSwitch 6360 Hardware Users Guide
---

## R（触发场景）
- 新机首次登录：console 连接、解锁会话、改密、设时间、保存配置
- 日常巡检：槽位/温度/电源/PoE 四板斧命令
- 面板灯异常：OK/VC/PWR 琥珀或灭，端口 LED 颜色含义
- 温度 trap 或自动关机后的处置
- 核对安全红线：激光/ESD/雷暴/住宅禁用等

## I（核心理念）
硬件健康监控三层框架（F3，<<<PAGE 15>>>/<<<PAGE 45>>>/<<<PAGE 55-57>>>）：物理层=面板 LED（OK/VC/PWR 三系统灯+端口灯分色）；传感层=自动监控（超 Warning 发 trap 不停机、超 Danger 自动关机不可配）；CLI 层=用户驱动四板斧（show module/show temperature/show powersupply/show lanpower）。首次登录六步闭环（P37）：console（9600-8N1）→admin/switch→解锁会话→改密→时间/可选项→write memory。会话解锁安全模型（P38）：出厂仅 console 可用，Telnet/FTP/WebView/SNMP 全锁死需 `aaa authentication` 逐类解锁。

## A1（决策框架）
1. **LED 快诊**：OK 琥珀=系统/风扇/温度故障；PWR 稳琥珀=12V 故障、闪琥珀=54V/PoE 故障；VC 灭=关机或非 VC 成员（P13，<<<PAGE 45>>>）
2. **端口灯分色**：RJ45 绿=非 PoE 链路、琥珀=PoE 链路；SFP 口绿=上行、琥珀=VFL（P14，<<<PAGE 46>>>）
3. **温度双阈值处置**：Warning→发 trap 查气流/室温；Danger→已自动关机，处理后手动重启（P23，<<<PAGE 56-57>>>）
4. **巡检命令分层**：槽位用 show module/long、温度用 show temperature（UNDER THRESHOLD 为正常）、电源用 show powersupply、PoE 用 show lanpower（P24，<<<PAGE 55-57>>>）

## A2（操作步骤）
- **首次登录六步**：console→admin/switch→`aaa authentication default local`（或逐类，一次一类）→`password`（实时落盘）→`system timezone/time/date`+可选 contact/name/location→`show system`→`write memory`（C5，<<<PAGE 21-24>>>）
- **硬件巡检**：`show module`/`show module long`→`show temperature` 看 Current/Range/Danger/Thresh/Status→超阈处置（C13，<<<PAGE 55-57>>>）
- **PoE 监控**：`show lanpower 1` 看逐口 Maximum/Actual/Status/Priority/Class+槽预算余量；尾部 `*` 号=4pair 口跑在 2pair 模式（C24，<<<PAGE 61>>>/<<<PAGE 68>>>）
- **PoE 关断两级**：单口 `lanpower port admin-state disable`；整槽 `lanpower slot service stop`；admin-state enable 仅复活（C15，<<<PAGE 62>>>）

## E（实证案例）
- 无 RTC 机型用 NTP 同步时间的理由（X2，<<<PAGE 23>>>）
- Priority Disconnect 三场景裁决：同级按端口号（1 高 48 低）、新 PD 高级断低级口、低级被拒（P35，<<<PAGE 66-68>>>）
- Fast PoE 的 LLDP 盲区：LLDP 协商的 PD 要等 AOS 启动完成（X7，<<<PAGE 63>>>）

## B（反例/坑）
- **本机型注意**：无实时时钟，断电重启后时间停在关机时刻——必须配 NTP（X2，<<<PAGE 23>>>）
- Danger 阈值出厂固化不可配（X3，<<<PAGE 57>>>）；Danger 关机后不会自动恢复，需手动重启（C13，<<<PAGE 57>>>）
- aaa authentication 一次只能解锁一类会话（X9，<<<PAGE 22>>>）；密码覆盖受限，丢失无法直接绕过（X10，<<<PAGE 22>>>）
- Class 1M 激光：开盖勿用光学仪器直视，空光口勿盯并装保护盖（X20，<<<PAGE 77>>>）
- ESD 腕带强制（X19）；雷暴禁止插拔线缆作业（X13）；Class A 数字设备不得用于住宅（X24）；受限访问场所安装（X25）

## 来源
OmniSwitch 6360 Hardware Users Guide Ch2 首次登录（<<<PAGE 20-24>>>）、Ch3 监控与温度（<<<PAGE 55-57>>>）、Ch4 PoE 监控（<<<PAGE 60-69>>>）、附录 A 安全法规（<<<PAGE 70-83>>>）。条目来源：cases C5/C13/C15/C24；principles P13/P14/P23/P24/P37-P40；counter-examples X2/X3/X9/X10/X13/X19/X20/X24/X25；frameworks F3。
