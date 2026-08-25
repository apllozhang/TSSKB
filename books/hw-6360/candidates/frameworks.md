# frameworks — OmniSwitch 6360 Hardware Users Guide（体系框架候选）

格式：编号 F# ｜ 框架名 ｜ 结构与运用 ｜ 页码

- **F1** 6360 家族选型三轴矩阵：轴一=下行口数（10/24/48）；轴二=PoE 能力（无 → P=802.3at → PX=2×多千兆 bt 口+950W 电源）；轴三=上行升级（X/H 后缀 combo 口可软件升 10G）。运算法则：先定口数，再按 PD 总功率选 PoE 预算档（120/180/350/380/760W 与内置电源 wattage 一一对应），最后按上联带宽决定是否要 X/H（10G 升级）；10 口机型独享半宽机箱+壁挂能力。 <<<PAGE 13>>>/<<<PAGE 60>>>
- **F2** PoE 供电三环体系：外环=预算（slot maxpower/port power 上限 + Guard Band 拒载：余量 < 口上限即拒新 PD）；中环=优先级（low/high/critical 三级 + 物理端口号 1 高 48 低作为同级裁决）；内环=保护动作（Priority Disconnect：新 PD 高级→断低级口；同级→端口号大者让路；新 PD 低级→被拒；禁用→一律拒新）。排障思路：新 PD 不供电先查 service 是否 start，再查 Guard Band（降口上限放行），再查优先级裁决。 <<<PAGE 62>>>-<<<PAGE 68>>>
- **F3** 硬件健康监控三层框架：物理层=面板 LED（OK/VC/PWR 三系统灯 + 端口灯颜色分 PoE/VFL）；传感层=自动监控（温度超 Warning 发 trap 不停机、超 Danger 自动关机且不可配）；CLI 层=用户驱动（show module/show temperature/show powersupply/show lanpower 四板斧）。 <<<PAGE 15>>>/<<<PAGE 45>>>/<<<PAGE 55>>>-<<<PAGE 57>>>

---
合计：3 条（F1-F3）。
