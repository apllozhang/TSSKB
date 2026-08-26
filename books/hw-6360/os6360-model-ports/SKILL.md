---
name: OmniSwitch 6360 机型与端口体系（命名解码/面板/上联/VFL）
description: 需要解读 OS6360 机型命名（P/PX/H 后缀）、查 10 个机型的端口构成与 PoE 预算、确认 combo 口/SFP+ 软件可配口/VFL 角色、规划上联与 VC 堆叠时使用。
source_book: OmniSwitch 6360 Hardware Users Guide
---

## R（触发场景）
- 拿到 OS6360-P48X/PH24 之类型号名，要快速解码端口构成、PoE 能力与上联形态
- 选型时在 10/24/48 口 × 非 PoE/PoE/多千兆 PoE 之间比选，核对 PoE 预算（120-760W）
- 确认 combo 口两种介质二选一、SFP+ 口怎么在 1G 上行/10G/VFL 之间切换
- 判断某机型是否无风扇、内置电源 wattage 多少、H 后缀"可升级 10G"是什么意思
- 规划 Virtual Chassis（VC）时核对 VC LED 语义与机型角色

## I（核心理念）
6360 家族选型三轴矩阵（F1，<<<PAGE 13>>>/<<<PAGE 60>>>）：轴一=下行口数（10/24/48），轴二=PoE 能力（无 → P=802.3at → PX=2×多千兆 bt 口+950W 电源），轴三=上行升级（X/H 后缀 combo 口可软件升 10G）。家族命名解码（P1）：`-10/-24/-48` 非 PoE；`P*`=802.3at PoE；`P*X`=2 个多千兆 802.3bt 口（47-48）+大电源；`PH*`=combo 口可软件升级 10G（"Upgradeable to 10G"）。上行口三段式结构（P2，<<<PAGE 13>>>）：全家族统一为"2×RJ45/SFP combo + 2×SFP+ 软件可配口"，SFP+ 口可在"1G SFP 上行"与"10G SFP+ 上行或 VFL"两种角色间软件切换。电源全部内置不可热换，wattage 随 PoE 递增（30→950W，P5）。无风扇分级（P4）：-10/P10/24/P24/48 无风扇；P24X/PH24/P48X/PH48 大功率 PoE 机型带风扇。

## A1（决策框架）
1. **先定下行口数**：10 口（半宽机箱、独享壁挂能力）/24 口/48 口三档（F1，<<<PAGE 13>>>）
2. **再按 PD 总功率选 PoE 档**：预算与内置电源一一对应——P10=120W、P24=180W、P24X/PH24=380W、P48=350W、P48X/PH48=760W（P26，<<<PAGE 60>>>）
3. **最后定上联档**：要 10G 上联选 X/H 机型；H 后缀 combo 口可软件升级 10G（P1，<<<PAGE 14>>>）
4. **多千兆 AP 场景**：P48X/PH48 的 47-48 口为 2.5G 802.3bt 口，接 Wi-Fi6 AP（<<<PAGE 42>>>）
5. **堆叠需求**：VC 通过 SFP+ 软件可配口建链，VC LED 闪绿=Master/闪琥珀=Slave、闪烁次数即节点 ID（P13，<<<PAGE 45>>>）

![OS6360 机型前/后面板示意（原文 p26，每机型一页：p26-44）](images/fig-panel-model-p26.png)

## A2（操作步骤）
- **机型速查**：对照 Ch1 机型总表（<<<PAGE 13-15>>>）与 Ch3 逐机型面板图/规格表（<<<PAGE 26-45>>>）
- **combo 口使用**：RJ45 与 SFP/SFP+ 共享口对（25-26/49-50），两种介质二选一（<<<PAGE 30>>>）
- **SFP+ 软件可配口切换**：在 1G SFP 上行与 10G SFP+/VFL 角色间软件切换（P2，<<<PAGE 13>>>）
- **VFL 部署**：SFP+ 口配为 VFL（Virtual Fabric Link）第二角色，端口 LED 琥珀色指示 VFL（P14，<<<PAGE 46>>>）
- **VC 规划**：VC 配置参考 Switch Management Guide（C1，<<<PAGE 17>>>）；用 VC LED 判断本机角色与节点 ID（<<<PAGE 45>>>）

## E（实证案例）
- 10 口机型独享半宽机箱+壁挂（OS6360-WALL-MNT，C10，<<<PAGE 54>>>）
- P48X 面板：46 口 at + 2 口多千兆 bt（2.5G）+ 10G combo，950W 电源/760W 预算（<<<PAGE 42>>>）
- P10A-US 靠 PN 区分的变体（904324-90，X1，<<<PAGE 28>>>）

## B（反例/坑）
- **本机型注意**：OS6360-P10A-US（PN 904324-90）不支持 Fast/Perpetual PoE——面板丝印与其他 P10 相同，只能靠 PN 区分（X1，<<<PAGE 28>>>/<<<PAGE 63>>>）
- SFP+ 软件可配口的 10G 能力仅 X/H 机型具备，普通 P 机型 SFP+ 口只有 1G SFP 上行或 VFL（P1/P2，<<<PAGE 13>>>）
- combo 口 RJ45 与 SFP 是同一口位的两种介质，不能同时用（<<<PAGE 30>>>）
- 电源全部内置不可热换、不可扩——预算选型在购机时一次定死（P5，<<<PAGE 26-44>>>）
- 6360 无 VC 专用堆叠口，VC 建在 SFP+ 可配口上，占用上联资源（<<<PAGE 13>>>）

## 来源
OmniSwitch 6360 Hardware Users Guide Ch1 机型总表（<<<PAGE 13-16>>>）、Ch3 逐机型面板与规格（<<<PAGE 25-57>>>）。条目来源：principles P1-P5/P13/P14；cases C1/C10；counter-examples X1；frameworks F1；glossary 10 机型逐条。
