---
name: OmniSwitch 9900 运维与排障（热插拔节律/组件更换/LED 诊断/PoE lanpower/排障红线）
description: 需要执行 OS9900 组件热插拔（拆 30 秒/插 5 分钟节律、CFM 120 秒窗口、NI 同类替换）、拆除与更换流程、按 CMM/NI LED（PRI/FAB/五灯同闪）诊断故障、PoE lanpower 命令族与 Priority Disconnect（48 高 1 低）排障时使用。
source_book: OmniSwitch 9900 Series Hardware Users Guide
---

## R（触发场景）
- 现场更换 CMM/CFM/NI/电源/风扇托盘：执行热插拔节律（拆件间隔 30s、插件间隔 5 分钟+LED 无错）
- CFM 热换：先拆风扇托盘、120 秒内完成、一次只换一块
- NI 模块热换：同类替换（like modules）流程
- LED 诊断：PRI/VC/FAB/PS/TEMP 组合判读（含五灯同闪 PCIe 失效）
- PoE 供电排障：lanpower 命令族、Priority Disconnect 裁决、预算不足断电分析

## I（核心理念）
热插拔节律双标准（P37，<<<PAGE 63>>>）：所有拆件间隔 30 秒；所有插件间隔 5 分钟且 LED 无错才能进行下一件——这是 9900 区别于 1U 交换机的机箱级纪律。三重热换限制（P38-P40，<<<PAGE 63>>>）：单件不可热拆；CFM 热换 120 秒窗口且风扇全在位、一次一块；NI 只能同类热换（先断网线拔光模块等 30 秒）。LED 组合诊断语义（P12，<<<PAGE 18>>>）：PRI/FAB 状态编码故障域，五灯同闪=全部 CFM PCIe 硬链路失效（拒绝登录、console 每 5 秒报错）。PoE 机制三要点：默认 operational disabled（装好不等于供电）；功率上限只设限不预留；Priority Disconnect 端口优先方向为 **48（最高）→1（最低）**，与接入系列相反（P31/P32/X37/X38，<<<PAGE 50>>>/<<<PAGE 52>>>/<<<PAGE 53>>>/<<<PAGE 55>>>）。

## A1（行动框架）
1. 更换作业先过三关：该组件是否多于一件（单件禁拆）→ 热插拔节律表（拆 30s/插 5min+LED 无错）→ 功率预算（`show chassis` Power Left）
2. LED 诊断分级：单灯异常→查对应组件；FAB 闪黄→CFM 电源/PCIe；五灯同闪→整机矩阵失效走支援
3. PoE 变更走预算：`show lanpower slot` 查逐口用量 → 调整上限/优先级 → 留意 Priority Disconnect 裁决方向
4. 更换后验证：主 CMM 四绿（PRI/PS/FAB/TEMP）+ `show chassis` 复核

## A2（操作步骤）
- **NI 热换完整流程**：断模块全部网线→拔全部光模块→等 30 秒→插同类替代模块→回插光模块→重接网线（C27，<<<PAGE 63>>>）
- **CFM 热换**：一次只换一个、风扇托盘全数在位、120 秒内完成（P39/X20，<<<PAGE 63>>>）
- **拆 CFM**：先拆遮挡的风扇托盘→松上下拇指螺丝、锁杆外拉释放→滑出并全程托承重量（C25，<<<PAGE 59>>>-<<<PAGE 61>>>）
- **拆电源四步**：双端拔线→松拇指螺丝→手柄下拉 open→一手拉一手托底取出；空槽装盲板（C23，<<<PAGE 57>>>/<<<PAGE 58>>>）
- **拆风扇托盘**：松拇指螺丝→拉出下把手脱开底部→向外向下拉出脱离顶部 tab；尽快装回（C24，<<<PAGE 58>>>/<<<PAGE 59>>>）
- **PoE 首次激活**：`lanpower slot 2/1 service start`（唯一途径，admin-state 不能首启）（C15/X33，<<<PAGE 52>>>）
- **PoE 调整**：单口 `lanpower port 1/1/6 priority critical`；槽上限 `lanpower slot 3/1 maxpower 400`（上限不预留）（C17/C18，<<<PAGE 53>>>/<<<PAGE 54>>>）
- **Priority Disconnect 开关**：`lanpower slot 2/1 priority-disconnect disable|enable`（默认启用）（C20，<<<PAGE 55>>>）
- **状态查看**：`show powersupply`（逐槽 Type/Status）+ `show lanpower slot 1/4`（逐口用量/优先级/预算）（C22，<<<PAGE 50>>>/<<<PAGE 51>>>）
- **CMM LED 判读**：PRI 稳绿=主/闪绿=备/稳黄=停运/闪黄=升级中；VC 稳蓝=Master；NI 背光稳蓝=HW OK/闪蓝=启动或故障；Speed LED 稳红=HW 故障（P12/P22，<<<PAGE 18>>>/<<<PAGE 27>>>）

## E（实证案例）
- Priority Disconnect 四场景裁决（P32，<<<PAGE 55>>>/<<<PAGE 56>>>）：禁用→一律拒新 PD；启用+同级→按物理端口号 48 高 1 低；启用+新 PD 最高优先级→必得电、先断最低优先级口；启用+新 PD 最低→拒
- 调低 slot 上限致低优先级口断电（新值低于当前总消耗时）（C17/X36，<<<PAGE 53>>>）
- 开 Class 检测复位全部 PoE 口（仅老式 IP 话机用、默认关）（C19/X34，<<<PAGE 52>>>/<<<PAGE 54>>>）
- FAB 闪黄时 NI 全断电但仍可 console/EMP 登录定位（P12，<<<PAGE 18>>>）

## B（反例与坑）
- **Priority Disconnect 端口优先方向为 48（最高）→1（最低），与 6865/6870/6560 等接入系列（1 高 48 低）相反**——跨平台直接套用优先级规划，预算不足时断电的口正好相反（X38/P31，<<<PAGE 55>>>）
- 热插拔节律红线：拆件间隔不足 30 秒、插件间隔不足 5 分钟或 LED 未示无错即进行下一件（X21/P37，<<<PAGE 63>>>）
- 单 CMM/单 CFM/单电源时热拆即断业务（X11，<<<PAGE 63>>>）
- CFM 热换超 120 秒、一次换多块、风扇未全在位（X20，<<<PAGE 63>>>）
- NI 非同类模块热换（"can only be hot swapped with like modules"）；换前不断线不拔光模块不等 30 秒（X22/C27，<<<PAGE 63>>>）
- 三风扇托盘常驻："Three fan trays are required at all times"，运维拆除须尽快装回（X19/C24，<<<PAGE 28>>>/<<<PAGE 59>>>）
- PoE 默认 operational disabled，装好即供电的预期会落空；lanpower port admin-state 不能用于首次激活（X37/X33，<<<PAGE 50>>>/<<<PAGE 52>>>）
- 开 Class 检测会复位全部 PoE 口（生产操作前评估影响面）（X34，<<<PAGE 52>>>）
- 排障红线：运行中勿触电源内部/主板；雷暴禁插拔作业；空光口不可见激光勿直视（X40/X41/X42，<<<PAGE 69>>>/<<<PAGE 70>>>/<<<PAGE 73>>>）
- 密码丢失后果：OmniSwitch 覆盖已配置密码受限制（X46，<<<PAGE 48>>>）；解锁远程会话即向所有持凭证者开放远程访问（X47，<<<PAGE 47>>>）

来源：OmniSwitch 9900 Series Hardware Users Guide（Ch3 PoE + Ch4 拆除部件 + LED 诊断，p50-63；附录 A，p68-73）
