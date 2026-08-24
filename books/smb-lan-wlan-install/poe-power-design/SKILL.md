---
name: PoE 供电预算与端口配置
description: 当需要为 AP/话机/摄像头等受电设备规划 PoE 功率预算、配置端口供电优先级或选择 Fast/Perpetual PoE 特性时使用本技能。
source_book: DT00XTE301 LAN & WLAN Installation & Configuration for SMB
---

## R（触发场景）
- 接入交换机要给 AP、IP 话机、摄像头供电，需要核算功率预算
- 超预算时需要决定哪些端口先断电（优先级设计）
- 需要即时供电、重启不断电或延迟供电等特殊供电行为

## I（核心理念）
PoE 预算 = PSE 总供给能力 − 所有 PD 需求之和；PD 功率由 Class 分级决定（af 15.4W / at 30W / bt 60W / 100W 四档）。动态分配只按 PD 实际需求供电，可提高预算利用率。超预算时按 Low → High → Critical 顺序断电，关键设备必须设 critical。型号带字母 «P» 才支持 PoE。

## A1（行动框架）
1. 查电源与受电状态：
   ```
   -> show powersupply
   -> show lanpower slot 1/1        // 确认端口 Powered On 与 Class
   ```
2. 启动供电服务并开端口（端口默认 disabled）：
   ```
   -> lanpower slot 1/1 service start
   -> lanpower port 1/1/1 admin-state enable
   ```
3. 设端口功率上限与整机预算：
   ```
   -> lanpower port 1/1/24 power 18000     // mW
   -> lanpower slot 1/1 maxpower 400       // W
   ```
4. 关键端口设高优先级：`-> lanpower port 1/1/6 priority critical`
5. 特性开关：
   ```
   -> lanpower slot 1/1 capacitor-detection enable
   -> lanpower slot 1/1 priority-disconnect enable
   -> lanpower slot 1/1 delayed-start enable seconds 120
   -> lanpower fpoe enable / lanpower ppoe enable
   ```
   （C27，<<<PAGE 150>>>–<<<PAGE 154>>>、<<<PAGE 144>>>–<<<PAGE 145>>>）

## A2（进阶应用）
- 四标准功率对照（P01，<<<PAGE 147>>>）：af Type1 = PD 12.95W / PSE 15.4W / 350mA / 3 级；at Type2 = 25.5W / 30W / 600mA / 4 级；bt Type3 = 51W / 60W / 6 级；bt Type4 = 71W / 100W / 8 级。
- 特性选型（F10，<<<PAGE 144>>>–<<<PAGE 145>>>、<<<PAGE 154>>>）：
  - Fast PoE：上电数秒即供电，不等系统完全启动；
  - Perpetual PoE：交换机软重启期间对 PD 不断电；
  - delayed-start：lanpower 延迟启动 120–600 秒（5 的倍数），等系统稳定再供电。
- PoE 端口 LED 判读：琥珀 = 已连接且受电，绿 = 已连接但未受电（P44，<<<PAGE 143>>>）。
- 非 PoE 交换机环境可用 PoE Injector / Midspan 补供电（glossary·<<<PAGE 39>>>）。
- SMB 拓扑选型时按 PoE 能力分档（.bt 90W、最大摄像头数）（F14，<<<PAGE 491>>>–<<<PAGE 493>>>）。

## E（实证案例）
- `show lanpower slot 1/1` 确认 AP 口 1/1/6 Powered On、Class 4（C09，<<<PAGE 173>>>–<<<PAGE 175>>>）。
- Lightning Config 完成后主页 PoE Port Configuration 查看各口受电状态（C26，<<<PAGE 481>>>–<<<PAGE 490>>>）。
- AP 上联口设 `priority critical`，超预算时 AP 最后断电（P02，<<<PAGE 151>>>）。

## B（边界与陷阱）
- FPoE/PPoE 与 delayed-start 互斥，不能同时启用；OS6360 的 P10A 子型号不支持 FPoE/PPoE（CE18，<<<PAGE 154>>>、<<<PAGE 144>>>–<<<PAGE 145>>>）。
- 电容检测法不符合 802.3af 标准，只用于 legacy IP 话机，默认不开（P05，<<<PAGE 152>>>）。
- EEE（802.3az）仅适用铜缆 100/1000M 端口，不兼容光口"U"机型（P04，<<<PAGE 146>>>）。
- 型号不带 «P» 不支持 PoE；动态分配按 PD 实际需求供电（P03，<<<PAGE 147>>>–<<<PAGE 148>>>）。

## 来源
- case·PoE 端口级配置命令组（<<<PAGE 150>>>–<<<PAGE 154>>>、<<<PAGE 144>>>–<<<PAGE 145>>>）
- framework·PoE 供电特性选型（<<<PAGE 144>>>–<<<PAGE 145>>>、<<<PAGE 154>>>）
- principle·PoE 四标准功率等级对照（<<<PAGE 147>>>）
- principle·端口优先级与断电顺序（<<<PAGE 151>>>）
- principle·动态分配与型号标识（<<<PAGE 147>>>–<<<PAGE 148>>>）
- counter·FPoE/PPoE 与 delayed-start 互斥、P10A 限制（<<<PAGE 154>>>、<<<PAGE 144>>>–<<<PAGE 145>>>）
