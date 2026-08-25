---
name: OmniSwitch 6465 安装与电源（DIN/DNV/ROJ 接线/温度降额/PoE）
description: 需要安装 OS6465（DIN 导轨/机架/侧挂/DNV 船用）、接线 ROJ 剥线端子电源（线色/扭矩）、配置 powersupply type、核算 PoE 温度降额预算与 lanpower 命令族时使用。
source_book: OmniSwitch 6465 Hardware Users Guide
---

## R（触发场景）
- 工业柜 DIN 导轨装/卸、P28 机架安装、T 机型半宽/双机并排、侧挂壁挂
- 船用 DNV 三套件安装与电源罩限温
- ROJ 剥线电源输入/输出接线（线色/极性/扭矩）
- `powersupply type` 手工配置电源类型、电源热换
- 高温环境（60-75°C）PoE 预算降额核算与 Guard Band/Priority Disconnect 排查

## I（核心理念）
工业 PoE 降额三环体系（F2，<<<PAGE 24>>>/<<<PAGE 30>>>/<<<PAGE 74>>>）：环境温度环（≤60°C 全额/60-70°C 降额需 100 CFM/70-75°C 停 PoE）→ 输入电压环（50-57V 满额/44-57V 限 af/24V 仅系统）→ 电源配置环（powersupply type 手工声明+双电源同型号+仅 P28 负载分担）。安装形态五件套框架（F4，<<<PAGE 38-49>>>）：DIN 导轨→机架→侧挂/壁挂→DNV 船用→后托盘电源。电源类型不可自动识别（P15）：必须 `powersupply type` 手工配置，否则功率/PoE 信息错误。

## A1（决策框架）
1. **安装形态五选**（F4）：DIN 导轨卡扣（P6/P12）→ P28 全宽机架 → T 单机 L 支架/双机 DUO 并排 → WALL-MNT 侧挂壁挂 → DNV 船用三套件
2. **电源六选**：BPNX 480W（仅 ENH-240）/BPN-H 180W/BPN 75W（外置 ROJ）、BPR AC 180W/BPRD DC 180W（P28 模块）、内置 65/185W（T）（P12 电源矩阵）
3. **PoE 预算按"环境档→电压档→电源组合"三步查**（F2，<<<PAGE 74>>>）
4. **ROJ 接线纪律**：输出红=V-/黑=V+/绿=PG、扭矩 3.5 in-lb；输入黑棕=L/白蓝=N/绿绿黄=PG（P32，<<<PAGE 58-60>>>）
5. **混插禁令**：双电源必须同 wattage 同标称电压（P14，<<<PAGE 24>>>/<<<PAGE 27>>>/<<<PAGE 30>>>）

## A2（操作步骤）
- **DIN 装/卸**：顶部卡扣先挂轨→下旋到底部卡扣 snaps in；拆卸下拉卡扣（可用长螺丝刀）向外旋出（P28 机构，<<<PAGE 39>>>）
- **DNV 安装**：P28 装 REAR-MNT 侧轨/后托架+DNV-RACK 电源托盘/罩/filler 板；P6/P12 用 DNV-DIN 左右电源罩（C8，<<<PAGE 46-49>>>）
- **后托盘电源安装**：DB-15 两侧导柱对准导孔→推入就位→拧拇指螺丝→冗余对侧重复（C9，<<<PAGE 56>>>）
- **ROJ 接线**：输出线红入 V-/黑入 V+/地线固定接地端、3.5 in-lb；输入线黑棕 L/白蓝 N/绿绿黄 PG；确认前严禁插 NEMA 5-15（C10-C12，<<<PAGE 59-60>>>）
- **电源类型配置**：`powersupply 1 name ALE-75W-ps1 type ale lo-ac`（双电源逐一，C13，<<<PAGE 60>>>）
- **电源热换**：冗余下单电源可不断电更换——断电→拆输入/输出线→按流程装新（C14，<<<PAGE 61>>>）
- **接地**：LCD8-10A-L+8AWG+30-60 in-lb；NEBS 场景加星形垫圈/CBN/抗氧化剂（C15，<<<PAGE 62>>>）
- **PoE 激活与调整**：先配电源类型→`show powersupply`→`lanpower slot 1/1 service start`→port power/maxpower/priority 调整（C21/C22，<<<PAGE 75-79>>>）

## E（实证案例）
- Guard Band 拒载处置：余 50W/口上限 75W 拒 4W PD→降口上限 10W 放行（C23，<<<PAGE 80>>>）
- 上电纪律：多电源数秒内先后插电；冗余 AC 每路独立电路（C1，<<<PAGE 15>>>/<<<PAGE 17>>>）
- 温度降额实测：P6/P12/ENH-240 三档预算 45/30/0、150/130/0、240/240/0W（P9，<<<PAGE 74>>>）

## B（反例/坑）
- **本机型注意（与 6560 等跨书易混）**：6465 双电源同型号强制且仅 P28 负载分担——不存在 6560 式"BP+BP-D 唯一混插例外"，混用即不支持（X2，<<<PAGE 24>>>/<<<PAGE 27>>>/<<<PAGE 30>>>）
- 24V 输入有检测电路已知缺陷：无法配置电源类型且 PS LED 不亮（X1，<<<PAGE 24>>>/<<<PAGE 27>>>）
- 电源类型必须手工配置，系统不能自动识别——漏配则功率/PoE 信息全错（X9，<<<PAGE 60>>>）
- 70-75°C 完全停止 PoE；60-70°C 降额预算以 100 CFM 气流为前提（X5/X6，<<<PAGE 74>>>）
- BPNX 无工业认证、标签可能误标（X3）；BPN 75W 配 ENH-240 需 ≥8.9R2（X4）
- DNV 电源罩装后环境上限 75°C→55°C（X8，<<<PAGE 32>>>）
- 接线确认前禁止 NEMA 5-15 插电，违者可能触电/损坏（X11，<<<PAGE 59>>>）；只准用 ALE 原厂配件（X12）

## 来源
OmniSwitch 6465 Hardware Users Guide Ch2 快速入门（<<<PAGE 14-20>>>）、Ch3 安装/电源/告警（<<<PAGE 21-69>>>）、Ch4 PoE（<<<PAGE 70-84>>>）。条目来源：cases C1/C4-C15/C21-C23；principles P5/P6/P9-P16/P28-P35；counter-examples X1-X6/X8-X12；frameworks F2/F4。
