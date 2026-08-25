---
name: OmniSwitch 6865 运维与排障（lanpower/Guard Band/Dying Gasp 三通道/LED 启动判读）
description: 需要 PoE 激活与预算管控（lanpower/Fast·Perpetual PoE/Priority Disconnect 端口号 1 高 28 低）、配置 Dying Gasp 三通道掉电告警、show 巡检与 LED 启动判读、首次登录六步时使用。
source_book: OmniSwitch 6865 Hardware Users Guide
---

## R（触发场景）
- PoE 上线：逐 slot 物理激活、口/槽功率上限、三级优先级、Fast/Perpetual PoE 开启
- 新 PD 拒载排查（Guard Band）或预算不足裁口（Priority Disconnect 四场景）
- 掉电可观测性：Dying Gasp 三通道（SNMP/Syslog/Link OAM PDU）配置
- 首次上电：LED 判读时机（启动完成前不判断）与首次登录六步
- 电源/PoE 状态巡检：show powersupply / show lanpower slot

## I（核心理念）
6865 运维三支柱：①PoE 两级激活模型（P27，<<<PAGE 58>>>）——软件默认 administratively enabled，但必须逐 slot `lanpower slot service start` 物理激活才供电；②预算-温度-电源三变量联动（P25）——预算随温度档降额（65°C 腰斩），叠加 Guard Band（剩余预算<口上限拒新 PD）与 Priority Disconnect（优先级+端口号 1 最高→28 最低裁决，P33）两级裁决；③Dying Gasp 部署框架（F4，<<<PAGE 54>>>/<<<PAGE 55>>>）——全电源丢失瞬间维持电力发 SNMP trap（前 3 站）+Syslog（前 3 服务器）+4×802.3ah PDU；资源约束=并发 PDU 口数 10−已配服务器数，上行口优先。Fast PoE 上电数秒供电（FPGA 固化）；Perpetual PoE 软重启不断电，MCU 升级例外（P29/P30，<<<PAGE 59>>>）。

## A1（行动框架）
1. 首次上电判读纪律：启动完成前不判断 LED 状态（"Be sure the boot process is complete before checking LED status"，C22，<<<PAGE 38>>>）
2. 首次登录六步（C23，<<<PAGE 39>>>-<<<PAGE 41>>>）：console（admin/switch）→解锁会话→改密→时区→日期时间→可选项
3. PoE 上线三级：slot service start 物理激活→power/maxpower 调上限→priority 设关键口
4. 拒载排查：show lanpower slot 查剩余预算→Guard Band 对照口上限→必要时调低口上限放行
5. DG 三通道部署：snmp station + swlog output socket + efm-oam 三命令（F4）

## A2（操作步骤）
- **PoE 物理激活**：`lanpower slot 2/1 service start`；曾被断电的口重启用 `lanpower port admin-state enable`（C28，<<<PAGE 58>>>）
- **关 PoE**：单口 `lanpower port 1/1/12 admin-state disable`；整槽 `lanpower slot 1/1 service stop`（C29，<<<PAGE 59>>>）
- **Fast/Perpetual PoE**：`lanpower slot 1/1 fpoe enable` / `lanpower slot 1/1 ppoe enable`（C30，<<<PAGE 59>>>）
- **调限额与优先级**：`lanpower power`（须带 chassis/slot/port 全三段）；`lanpower slot 1/1 maxpower 150`；`lanpower port 1/1/6 priority critical`（C31/C32，<<<PAGE 59>>>-<<<PAGE 61>>>）
- **电容检测**：`lanpower slot 1/1 capacitor-detection enable`（仅老式 IP 话机，C33，<<<PAGE 61>>>）
- **Priority Disconnect 开关**：`lanpower slot 1/1 priority-disconnect disable|enable`（默认启用，C34，<<<PAGE 62>>>）
- **DG Link OAM 三命令**：`efm-oam admin-state enable`→`efm-oam port 1/1/23-24 admin-state enable`→`efm-oam port 1/1/23-24 propagate-events dying-gasp enable`（C35，<<<PAGE 54>>>）
- **状态查看**：`show powersupply`（电源类型/状态）；`show lanpower slot`（PoE 状态与新 PD 可用功率）（C36，<<<PAGE 57>>>）
- **改密码**：admin 登录→password→新密码→确认；实时存本地用户库、重启保留（C25，<<<PAGE 40>>>）

## E（实证案例）
- Priority Disconnect 四场景裁决（P33，<<<PAGE 62>>>/<<<PAGE 63>>>）：禁用→一律拒新 PD；启用+同级→按物理口号 1 最高→28 最低；新 PD 最高优先级→必得电、先断最低级口、同级断端口号最大的口；新 PD 最低→拒
- DG PDU 并发限额：2 SNMP+1 Syslog→最多 7 口同时发 PDU，上行口优先（P20，<<<PAGE 54>>>/<<<PAGE 55>>>）
- Class 检测抉择：默认关闭按预算供电；严格按类限功率需显式开启，代价=复位全部 PoE 口（P28，<<<PAGE 57>>>/<<<PAGE 58>>>）

## B（反例与坑）
- **Priority Disconnect 端口号方向（本机型）**：1 最高→28 最低（P33，<<<PAGE 62>>>）——与 6860 的"端口号越大越高"相反，跨书部署勿照搬
- lanpower port admin-state 不能首次激活 PoE，必须 slot service（X24，<<<PAGE 58>>>）；Class 检测开启复位全部 PoE 口（X25）
- 电容检测不符 IEEE，仅限老式 IP 话机（X26，<<<PAGE 61>>>）
- 调低 slot 上限可致低优先级口断电（X27，<<<PAGE 60>>>）；maxpower 不预留功率（P31，<<<PAGE 60>>>）
- Perpetual PoE 例外：MCU 固件升级必断 PD 电（X28，<<<PAGE 59>>>）；LLDP PD 在 Fast PoE 下须等启动完成（X29）
- 双电同源风险：两电源接同一源=同时故障，DG 直接触发（X30/P18，<<<PAGE 54>>>）
- 解锁远程会话即向远程开放访问（X40，<<<PAGE 40>>>）；密码覆盖受限，须安全记录（X39）
- 解锁会话一条命令只能一类（aaa authentication 逐类执行）
- 锂电池更换只能同型/等效型，旧电池寄回工厂（X37，<<<PAGE 76>>>）
- 跨书易混：6865 无温度双阈值机制（无 Danger 关机语义），与 6860/6870 的 Warning/Danger 双阈值不同，高温防护靠 TMRA 分级+预算降额

来源：OmniSwitch 6865 Hardware Users Guide（Ch1 p38-41 + Ch2 p51-55 + Ch3 p56-64）
