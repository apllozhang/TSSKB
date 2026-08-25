---
name: OmniSwitch 6870 运维与排障（lanpower 4pair·bt/温度双阈值/Dying Gasp/LED 诊断/上电七步）
description: 需要 PoE 激活与 bt Class 5-8 使能（lanpower 4pair/8023bt）、Guard Band 与 Priority Disconnect 排查、Dying Gasp 配置、show 巡检与温度双阈值处置、更换电源与首次上电入网七步时使用。
source_book: OmniSwitch 6870 Hardware Users Guide
---

## R（触发场景）
- PoE 上线：slot service 激活、4pair 60-95W 与 bt Class 5-8 使能、限额与优先级
- 新 PD 拒载排查（Guard Band）或预算不足裁口（Priority Disconnect）
- 掉电可观测性：Dying Gasp 三通道配置
- 巡检与告警处置：show module/temperature；Warning/Danger 双阈值
- 首次上电入网七步流程或电源热插拔更换

## I（核心理念）
6870 运维围绕 bt 供电全栈（P26，<<<PAGE 62>>>/<<<PAGE 65>>>）：802.3af/at/bt，Class 0-8 梯度（Class 5=45W/6=60W/7=75W/8=90-99W，4 对线 Type 3/4）；4pair 与 8023bt 两级使能（P29）：`lanpower 4pair` 开 60/75/95W（802.3at 4 对+PoH）、`lanpower 8023bt` 开 bt 双 Type。两级裁决与家族通用：Guard Band（剩余预算<口上限/类最大值即拒载，不作用已在电 PD，P34）与 Priority Disconnect 四场景（优先级+物理口号 **1 最高→48 最低**，P33）。温度双阈值（P19，<<<PAGE 58>>>/<<<PAGE 59>>>）：Warning 用户可配发 trap 业务继续；Danger 出厂固化超限自动关机须手动启动。三大可用性支柱（P10）：电源冗余/热插拔/硬件监控（自动 trap+LED+show 命令）。

## A1（行动框架）
1. 上电-入网标准七步（F3，<<<PAGE 17>>>-<<<PAGE 21>>>/<<<PAGE 65>>>）：安装（双人/盲板）→多电源数秒内相继插电→观察 OK/PS LED 至启动完成→console 115200-8N1 rollover 登录 admin/switch→解锁会话→改密+时区/时间/contact/name/location→write memory；PoE 机型追加 slot service start
2. PoE 上线五级：slot service start→4pair→8023bt→power/maxpower 限额→priority 关键口
3. 拒载排查：show lanpower slot 查剩余预算→Guard Band 对照口上限/类最大值→调低口上限放行
4. 温度告警处置顺序（X32）：Warning→查气流阻塞/室温/阈值是否过低；Danger→查气流与室温后手动开机
5. 电源热插拔更换：拆前断源→按锁片直拉→新电源插至 click 锁定→插线即开机

## A2（操作步骤）
- **巡检三板斧**：show module / show module long / show temperature（含各槽位 Danger/Thresh/Status）（C17，<<<PAGE 58>>>）
- **PoE 物理激活**：`lanpower slot 2/1 service start`（首次激活唯一途径）；断电口重启用 `lanpower port admin-state enable`（C19，<<<PAGE 65>>>）
- **开高功率**：`lanpower 4pair`（60/75/95W）；`lanpower 8023bt`（bt Type3/4 Class 5-8）（C21，<<<PAGE 65>>>）
- **调限额与优先级**：`lanpower port 1/1/24 power 3000`；`lanpower slot 3/1 maxpower 400`；`lanpower port 1/1/6 priority critical`（C22/C23，<<<PAGE 66>>>/<<<PAGE 67>>>）
- **Guard Band 放行**：余 50W、口上限 75W 拒载时 `lanpower power 1/1/1 power 10000` 降口上限 10W 即放行 4W PD（C26，<<<PAGE 68>>>）
- **Priority Disconnect 开关**：`lanpower slot 2/1 priority-disconnect disable|enable`（默认启用）（C25，<<<PAGE 69>>>）
- **DG 三命令**：`efm-oam admin-state enable`→`efm-oam port 1/1/23-24 admin-state enable`→`propagate-events dying-gasp enable`；配 snmp station+swlog output socket（C18，<<<PAGE 60>>>）
- **状态查看**：`show powersupply`；`show lanpower slot 1/1` 逐口最大功率/实际用量/优先级/Class+槽预算剩余（C27，<<<PAGE 63>>>/<<<PAGE 64>>>/<<<PAGE 71>>>）
- **首次登录**：admin/switch→aaa authentication 解锁（一条命令一个会话类型）→password 改密→system timezone/time/date→contact/name/location→write memory（C3-C6，<<<PAGE 18>>>/<<<PAGE 21>>>）

## E（实证案例）
- Guard Band 放行小 PD 实战（C26/P34，<<<PAGE 67>>>/<<<PAGE 68>>>）：剩余 50W、口上限 75W→拒载 4W PD；调口上限至 10W→放行
- Priority Disconnect 四场景（P33，<<<PAGE 69>>>/<<<PAGE 70>>>）：禁用→一律拒新 PD；启用+同级→按物理口号 1 最高→48 最低；新 PD 最高级→必得电、先断最低级口、同级断端口号最大口；新 PD 最低级→拒
- 95W bt 全链部署：P48M+双 2000W(230V)=3309W，lanpower 4pair+8023bt 两级使能后 Class 8 PD 按类供电（P27/P29，<<<PAGE 63>>>/<<<PAGE 65>>>）

## B（反例与坑）
- **Priority Disconnect 端口号方向（本机型）**：1 最高→48 最低（P33，<<<PAGE 68>>>/<<<PAGE 69>>>）——与 6860 的"端口号越大越高"相反，跨书迁移配置须核对
- lanpower port admin-state 不能首次激活 PoE（X25，<<<PAGE 65>>>）；Class 检测开启复位全机 PoE 口（X26）；电容检测不符 IEEE 仅限老式话机（X27，<<<PAGE 67>>>）
- 调低 slot 上限可致低优先级口断电（X28，<<<PAGE 66>>>）；maxpower 不预留（P31，<<<PAGE 67>>>）
- Guard Band 不保已在电 PD：预算缩减（如拔电源）由 priority disconnect 裁决（X29，<<<PAGE 68>>>）
- Z 系列不支持 2000W 电源，预算规划勿套用 M 系列（X30，<<<PAGE 47>>>/<<<PAGE 63>>>）
- Danger 阈值固化不可配，超限自动关机须手动启动（X31，<<<PAGE 59>>>）
- 解锁远程会话即开放远程访问；密码覆盖受限须安全记录（X40/X39，<<<PAGE 19>>>/<<<PAGE 20>>>）；一条命令只能解锁一类会话（X41）
- 雷暴禁拆装线缆；锂电更换须返厂（X21/X37，<<<PAGE 80>>>/<<<PAGE 84>>>）
- console 波特率全系 115200（rollover 线）——与 6360/6865 的 9600 不同，与 6860 仅 N 型 115200 也不同（<<<PAGE 17>>>）

来源：OmniSwitch 6870 Hardware Users Guide（Ch2 p14-21 + Ch3 p47-60 + Ch4 p61-71）
