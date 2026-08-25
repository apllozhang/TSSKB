---
name: OmniSwitch 6575 运维与排障（Alarm Relay、Dying Gasp、PoE 语义、LED 诊断、安全红线）
description: 需要配置 OS6575 Alarm Relay 干接点告警（in/out/event 映射与 VC 同步）、Dying Gasp 接收端、lanpower PoE 全流程（slot service/优先级/Guard Band/Priority Disconnect）、show 巡检与 LED 诊断、遵守 NEBS/激光/ESD 安全红线时使用。
source_book: OmniSwitch 6575 Hardware Users Guide
---

## R（触发场景）
- 告警链路建设：Alarm Relay 输入联动输出、系统事件（如认证失败）映射干接点
- 失电通告：Dying Gasp SNMP trap/Syslog 双通道接收端配置
- PoE 运维：首次激活、逐口功率/优先级调节、Guard Band 拒载解锁、Priority Disconnect 裁决
- 巡检排障：show module/temperature/powersupply/lanpower、告警 LED 判读、温度超限处置
- 安全红线：NEBS OSP 隔离、激光/ESD/锂电池警告

## I（核心理念）
工业高可用三支柱框架（F3，<<<PAGE 12>>>/<<<PAGE 48>>>/<<<PAGE 50>>>-<<<PAGE 52>>>）：链路侧=MP16 Port Bypass 断电旁路；供电侧=双同规格电源+独立电路+UPS+Dying Gasp 双通道（SNMP trap/Syslog 各前 3 目标）+Alarm Relay 干接点外送（NO/NC 触点 220VDC/250VAC/2A）；运行侧=无风扇宽温+温度双阈值（93/98°C：Warning 发 trap→Danger 关机手动恢复）+Alarm in/out/event 三源映射（VC 内跨机同步）。DG 本机仅双通道，无 802.3ah OAM PDU（P30，<<<PAGE 52>>>）。PoE 语义核心：Priority Disconnect 四情形规则+Guard Band 余量判据（P37/P38）。

## A1（行动框架）
1. 告警三源映射：输入（传感器 5-12VDC）→动作（output/trap/SWLog 三选）→系统事件绑定；VC 内任一机可驱动任一机输出（P24/P25，<<<PAGE 48>>>）
2. PoE 首启两步前置：先 powersupply type 声明电源→再 lanpower slot service start（C22/X7，<<<PAGE 46>>>/<<<PAGE 64>>>）
3. 预算管理三命令：lanpower port power（口限额）/lanpower slot maxpower（槽上限，不预留）/lanpower priority（low/high/critical）（C24/C25，<<<PAGE 64>>>/<<<PAGE 65>>>）
4. 拒载分诊：Guard Band=剩余预算<口 maxpower 即拒新 PD，解法=调低口上限（C26/P37，<<<PAGE 67>>>）；Priority Disconnect 禁用后新 PD 一律按预算拒供（C27，<<<PAGE 68>>>）
5. 巡检三命令：show module→show temperature（UNDER THRESHOLD 正常）→show powersupply（Total Power/PS Type/Status）（C20，<<<PAGE 50>>>/<<<PAGE 62>>>）

## A2（操作步骤）
- **告警输入→输出联动**：alarm in temperature-alarm-in action alarm-out admin-state enable→alarm out alarm-out-1 admin-state enable→alarm map temperature-alarm-in out alarm-out-1（C18，<<<PAGE 49>>>）
- **系统事件→输出映射（认证失败例）**：alarm event auth-fail-event event authentication-failure admin-state enable→alarm out set-alarm-out-chassis-1→alarm map … out …；show alarm event config/show alarm status/alarm clear status 核对清除（C19，<<<PAGE 49>>>）
- **触点接线**：NO/C/NC 三针——触发时 NO 闭合、NC 断开（P26，<<<PAGE 49>>>）；输入针 1 正/针 2 地（P24）
- **DG 接收配置**：snmp station+swlog output socket（C21，<<<PAGE 52>>>）
- **PoE 首次激活与核对**：powersupply type→lanpower slot 1/1 service start→show lanpower 1/1 逐口核对 Maximum/Actual/Status/Priority/On-Off/Class 与槽预算（C22，<<<PAGE 46>>>/<<<PAGE 64>>>/<<<PAGE 71>>>）
- **PoE 关断两级**：单口 lanpower port admin-state disable；整槽 lanpower slot service stop；admin-state enable 仅复活被断口（C23，<<<PAGE 64>>>）
- **告警四态 LED 组合判读**：输入+动作 alarm out→双 On；输入+动作 trap/SWLog→仅 Input On；系统事件触发输出→仅 Output On（P27，<<<PAGE 48>>>）；Alarm In/Out LED 各 Solid Red=检测到触发（P21，<<<PAGE 27>>>）

## E（实证案例）
- 温度告警输入驱动干接点外送 PLC（C18，<<<PAGE 49>>>）
- 认证失败事件→告警输出映射与实时状态核对（C19，<<<PAGE 49>>>）
- Guard Band 解锁小功率 PD：lanpower power 1/1/1 power 10000 调低口上限后正常上电（C26，<<<PAGE 67>>>）
- Priority Disconnect 四情形：禁用拒新 PD；同级按物理口号 1 最高→8 最低裁决；新 PD 最高级→自动断最低级口接纳；新 PD 最低级→被拒存量不停（P38，<<<PAGE 68>>>-<<<PAGE 70>>>）

## B（反例与坑）
- admin-state 不能首次激活 PoE，必须 lanpower slot service（X7，<<<PAGE 64>>>）
- class detection 开启复位全口 PoE（X6，<<<PAGE 64>>>）
- 电容检测不符 IEEE，仅限老 IP 话机（X8，<<<PAGE 66>>>）
- 调低槽预算可致低优先级口掉电；maxpower 不预留功率（X9/X10，<<<PAGE 65>>>）
- Guard Band 不适用于已上电 PD——但拔电源缩减预算时 priority disconnect 会生效掉口（X11，<<<PAGE 67>>>）
- Danger 阈值固化不可配；超限关机须手动重启（X16/X17，<<<PAGE 51>>>）
- NEBS 红线：楼内端口禁金属直连 OSP；AC 电源必须接 SPD（X25/X26，<<<PAGE 80>>>）
- Class 1M 激光勿直视、空光口加盖；运行中勿触背板；雷暴禁作业；锂电池返厂（X31/X29/X33，<<<PAGE 80>>>-<<<PAGE 85>>>）
- aaa 一次一类；密码覆盖受限（X14/X15，<<<PAGE 17>>>/<<<PAGE 18>>>）

来源：OmniSwitch 6575 Hardware Users Guide（Ch3-Ch4+附录 A，p46-71、p77-85）
