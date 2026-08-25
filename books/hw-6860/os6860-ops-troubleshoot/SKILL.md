---
name: OmniSwitch 6860 运维与排障（lanpower 全族/Dying Gasp/温度双阈值/LED 诊断）
description: 需要 PoE 激活与预算管控（lanpower/Guard Band/Priority Disconnect）、配置 Dying Gasp 三通道掉电告警（PDU 口数=10−服务器数）、show 巡检与温度双阈值处置、五色 LED 诊断时使用。
source_book: OmniSwitch 6860/6860E/6860N Hardware Users Guide
---

## R（触发场景）
- PoE 上线：首次激活、逐口/槽功率上限、优先级与定时规则
- 新 PD 不上电排查（Guard Band 拒载）或预算不足裁口（Priority Disconnect）
- 掉电场景可观测性：Dying Gasp 三通道配置与 PDU 口数挤占
- 例行巡检：show module/temperature/powersupply/lanpower；温度告警处置
- LED 异常判读（五色端口灯/PS 五态/OK2）与首次登录七步

## I（核心理念)
三层预算闸门框架（F2，<<<PAGE 93>>>/<<<PAGE 99>>>/<<<PAGE 100>>>/<<<PAGE 102>>>）：层一=物理预算（机型×电源×数量矩阵）；层二=priority disconnect 抢占上限（920W 电源→780W/只、600W→450W/只，超限部分只供不抢，P41，<<<PAGE 99>>>）；层三=Guard Band（剩余预算须大于口 maxpower 才上电，P44）。DG 三通道（P35，<<<PAGE 69>>>/<<<PAGE 70>>>）：SNMP trap（前 3 站）+Syslog（前 3 服务器）+4×802.3ah OAM PDU（上联口优先）；PDU 口数挤占公式=10−已配服务器数（P36，本书独有）。温度双阈值（P34，<<<PAGE 87>>>）：Warning 可配发 trap 不停机，Danger 固化关机须手动重启。

## A1（行动框架）
1. 巡检三板斧：show module → show temperature（VC 内逐机箱独立阈值）→ show powersupply（C17，<<<PAGE 86>>>/<<<PAGE 87>>>/<<<PAGE 91>>>）
2. PoE 上线四级：lanpower slot service start 物理激活→maxpower/power 调上限→priority 设关键口→power-rule 定时
3. 新 PD 拒载排查：先查剩余预算 vs 口 maxpower（Guard Band）→调低口上限放行→再查 priority disconnect 上限
4. 温度告警处置：Warning→查气流/室温不停机；Danger→固化阈值关机，处置后手动重启
5. VC 高可用基线（F3）：双电源分电路+UPS+DG 三通道+Fast/Perpetual PoE
6. 首次登录七步（C2，<<<PAGE 22>>>-<<<PAGE 26>>>）：console→admin/switch→（E 型）EMP 设 IP→解锁会话→改密→时区时间→show system/write memory

## A2（操作步骤）
- **PoE 首次激活**：show powersupply 确认→lanpower slot 2/1 service start→show lanpower slot 核对预算（C20，<<<PAGE 91>>>/<<<PAGE 92>>>/<<<PAGE 95>>>）
- **关断两级**：单口 lanpower port admin-state disable；整槽 lanpower slot service stop；admin-state enable 仅复活（C21，<<<PAGE 96>>>）
- **调限额**：lanpower port power 3000 降口限额；lanpower slot maxpower 400 调槽上限；lanpower port priority critical 设关键口（C22，<<<PAGE 96>>>/<<<PAGE 98>>>）
- **Guard Band 放行**：PD 不上电时 lanpower power 1/1/1 power 10000 调低口上限至低于剩余预算（C23，<<<PAGE 102>>>）
- **Priority Disconnect 开关**：lanpower slot 2/1 priority-disconnect disable/enable（C24，<<<PAGE 99>>>）
- **DG 配置**：efm-oam admin-state enable→端口 enable→propagate-events dying-gasp enable；snmp station+swlog output socket 配接收端（C18/C19，<<<PAGE 70>>>）
- **EMP（E 型）**：默认 192.168.1.1/24；ip interface emp 改 IP→show ip interface 核对（C3，<<<PAGE 24>>>）
- **会话解锁**：aaa authentication default local 全解；或逐类 telnet/http/ftp local，一次一类（C4/X23，<<<PAGE 25>>>）

## E（实证案例）
- DG PDU 挤占实战：2 SNMP 站+1 Syslog 服务器→同时发 PDU 口数上限=10−3=7 口（P36，<<<PAGE 70>>>）
- show temperature VC 逐机箱读法：1/CMMA（15-93/Danger 93）与 2/CMMA（15-85/85）并列，堆叠内每台阈值独立（P33，<<<PAGE 87>>>）
- Guard Band 不护已上电 PD：拔电源等预算缩减场景改由 priority disconnect 裁决（X22，<<<PAGE 102>>>）

## B（反例与坑）
- **物理口号优先级方向（本机型特有）**：6860 的 Priority Disconnect 端口号越大优先级越高（24 口机 24 最高→1 最低；48 口机 48 最高→1 最低，P42，<<<PAGE 100>>>）——与 6360/6560/6865/6870 等接入系列的"1 高 N 低"相反，跨书配置勿照搬
- priority disconnect 电源档上限：920W→780W/只、600W→450W/只，超限部分不参与抢占（X11，<<<PAGE 99>>>）
- lanpower port admin-state 不能首次激活 PoE，必须 slot service（X18，<<<PAGE 95>>>）；class detection 开启复位全机 PoE 口（X17，<<<PAGE 95>>>）
- maxpower 不预留功率；调低槽上限可致低优先级口掉电（X21/X20，<<<PAGE 97>>>）
- 电容检测不符 IEEE，仅限老式 IP 话机（X19，<<<PAGE 98>>>）
- Fast PoE 四限制：需正确 FPGA/CPLD 版本；出厂机须先完成初始 PoE 配置；启动期禁改 PoE 配置；LLDP PD 须等启动完成（X12-X15，<<<PAGE 96>>>）；Perpetual PoE 的 MCU 固件升级必断 PD 电（X16，<<<PAGE 96>>>）
- Danger 阈值固化不可配，超限关机须手动重启（X25，<<<PAGE 87>>>）
- 密码覆盖受限，丢失密码恢复困难，须安全记录（X24，<<<PAGE 25>>>）
- 锂电池更换须返厂，禁自行拆换（X37，<<<PAGE 114>>>）

来源：OmniSwitch 6860/6860E/6860N Hardware Users Guide（Ch2 p18-26 + Ch3 p69-70/p86-91 + Ch4 p89-103）
