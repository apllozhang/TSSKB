---
name: PoE 管理与功率预算
description: 当需要给 AP/话机/IP 电话等 PD 设备供电、规划 PoE 功率预算、设置端口供电优先级或排查供电不足时使用。
source_book: DT00XTE310 OmniSwitch LAN Access & OmniAccess Stellar WLAN Express
---

## R（触发场景）
- 新接 AP、IP 话机上电不启动，需要检查供电状态与功率预算
- 交换机功率预算吃紧，需要决定断电优先级或调预算上限
- 关键端口（如上联 AP 口）要求断电时最后被切

## I（核心理念）
PoE 管理的本质是"功率也是一种资源预算"：802.3af/at/bt 四档标准决定单口上限，整机 Power Budget 决定总量，Dynamic PoE Allocation 按需分配提升效率，端口优先级（low/high/critical）决定功率不足时谁先被断电。

## A1（行动框架）
1. **查电源与预算**：`show powersupply`；`show lanpower slot 1/1` 看 Actual Used / Power Budget（实例：AP 口 Actual Used 7000mW、Class 4，<<<PAGE 176>>>）。
2. **启动槽位 PoE 服务**：`lanpower slot 1/1 service start`。
3. **端口级开关**：`lanpower port 1/1/1 admin-state enable`。
4. **设定单口功率（mW）**：`lanpower port 1/1/24 power 18000`。
5. **设定槽位预算上限（W）**：`lanpower slot 1/1 maxpower 400`。
6. **设定端口优先级**：`lanpower port 1/1/6 priority critical`（<<<PAGE 153>>>-<<<PAGE 157>>>）。

## A2（进阶应用）
- **标准选型对照**（<<<PAGE 150>>>）：802.3af（PD 12.95W / PSE 15.40W / 350mA）→ 802.3at Type2（25.50/30.0W / 600mA）→ 802.3bt Type3（51/60W）→ Type4（71/100W / 960mA per pair）；Energy Management 分 class 三/四/六/八级。
- **动态分配**：Dynamic PoE Allocation 只下发 PD 实际需要的功率，直到总预算封顶，是最省电的用法（<<<PAGE 150>>>）。
- **Fast PoE / Perpetual PoE**：开机未完成启动即供电 / 交换机重启期间不断电；两者都需升级 FPGA/CPLD，OS6360-P10A 不支持（<<<PAGE 147>>>-<<<PAGE 148>>>）。
- **EEE 节能（802.3az）**：空闲时芯片低功耗；仅铜口 100/1000M 适用，光口 U 型号不支持（<<<PAGE 149>>>）。

## E（实证案例）
- PoE 管理命令集实战：service start → 端口 enable → 单口 18000mW → 槽位 maxpower 400W → critical 优先级 → show 验证（<<<PAGE 153>>>-<<<PAGE 157>>>）。
- AP 上线时观测到 Actual Used 7000mW、Class 4，用于验证 PD 分级协商（<<<PAGE 176>>>）。

## B（边界与陷阱）
- 功率不足时按 low → high → critical 顺序断电，默认 low；关键上联/话机口务必显式设 critical（<<<PAGE 154>>>）。
- Fast PoE / Perpetual PoE 依赖 FPGA/CPLD 升级，且 OS6360-P10A 不支持（<<<PAGE 147>>>-<<<PAGE 148>>>）。
- EEE 只对铜口 100/1000M 生效（<<<PAGE 149>>>）。

## 来源
- cases·C9 PoE 管理与监控命令集（<<<PAGE 153>>>-<<<PAGE 157>>>、<<<PAGE 176>>>）
- principles·P5 PoE 标准演进与功率预算（<<<PAGE 150>>>）
- principles·P6 端口优先级与断电顺序（<<<PAGE 154>>>）
- principles·P7 动态分配（<<<PAGE 150>>>）
- principles·P8 Fast PoE / Perpetual PoE（<<<PAGE 147>>>-<<<PAGE 148>>>）
- principles·P9 EEE 节能以太网（<<<PAGE 149>>>）
