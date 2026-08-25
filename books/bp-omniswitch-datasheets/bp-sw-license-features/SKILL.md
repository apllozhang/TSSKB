---
name: OmniSwitch 许可制特性（SW-PERF/PRM/AR 速度与路由许可 / "hardware capable" 陷阱）
description: 售前报价与方案核对 OmniSwitch 软件许可：6360/6370/6570M/6870 的 10G/25G/50G 速度许可、SW-AR 高级路由许可，以及 6570M 25G/MACsec/1588v2 "Hardware capable" 未交付陷阱时使用。
source_book: bp-omniswitch-datasheets（OS6360 p17 / OS6370 p26 / OS6570M p65-66 / OS6870 p111）
---

## R（触发场景）
- 分期建设：先买硬件后升 10G/25G 的许可路线报价
- 到货速度核对："硬件到货不等于速度全开"，SFP+ 默认 1G
- 需要 BGP/IS-IS/PIM/VRF 等高级路由特性的接入/城域方案
- 投标应答核对：数据表 "Hardware capable, requires future SW development" 条目

## I（核心理念）
许可经济学（F2 许可家族，<<<PAGE 17>>>/<<<PAGE 26>>>/<<<PAGE 65>>>/<<<PAGE 111>>>）：速度许可 SW-PERF（1G→10G）→ SW-PRM（25G）→ 50G（6870）；路由许可 SW-AR（OSPFv2/v3、BGP、IS-IS、PIM、VRF）。买硬件不买速度，后期按需激活（C9）。陷阱面：数据表脚注两类——"License purchase required"（花钱即得）与 "Hardware capable, requires future SW development"（硬件就绪但软件未开发，投标应答必须核实版本，X8）。

## A1（行动框架）
1. 盘点上联需求：当前 1G 够用 → 不买许可；两年内升 10G/25G → 报价分期许可行项
2. 按系列对号许可：6360 用 OS6360-SW-PERF；6370 用 SW-PERF4/PERF2（限 12/P12/PH24/PH48/P48X/48X 六型）；6570M 用 SW-PERF4（4x10G）/SW-PRM28（6x25G）；6870 50G 需许可
3. 路由特性核对：6570M 默认仅基础 L3，要 BGP/IS-IS 必须加 OS6570M-SW-AR
4. 投标前逐条核对星号与 Note：区分"许可可购"与"未来软件"两种脚注
5. 6870 按 bundle 下单时确认包内是否含许可（X21）

## A2（选型速查表）
| 许可 | 适用系列 | 激活能力 | 页码 |
|---|---|---|---|
| OS6360-SW-PERF | 6360 PH 型 | RJ45/SFP 口 1G→10G | <<<PAGE 17>>> |
| OS6370-SW-PERF4 / PERF2 | 6370-12/P12/PH24/PH48/P48X/48X | 4 口/2 口 SFP+ 1G→10G | <<<PAGE 26>>> |
| OS6570-SW-PERF4 | 6570M | 加 4x10G 上联/VFL | <<<PAGE 65>>> |
| OS6570-SW-PRM28 | 6570M | 6x25G 上联（SFP28） | <<<PAGE 65>>> |
| OS6570M-SW-AR | 6570M | OSPFv2/v3、BGP、IS-IS、PIM、VRF | <<<PAGE 65>>> |
| 50G speed license | 6870（上联模块 6x25/50G） | 25G→50G | <<<PAGE 111>>> |
| Hardware capable（非许可） | 6570M 的 MACsec、1588v2/PTP | 软件待开发，不可购买激活 | <<<PAGE 65>>> |

## E（选型决策案例）
- 预算只够先建 1G、两年后升 10G/25G：6370 SW-PERF4、6360 SW-PERF、6570M SW-PERF4/PRM28+SW-AR、6870 50G 许可——买硬件不买速度，后期按需激活（C9，<<<PAGE 26>>>/<<<PAGE 17>>>/<<<PAGE 65>>>/<<<PAGE 111>>>）

## B（反例与坑）
- 6570M 的 25G/MACsec/1588v2 是"硬件就绪、软件待开发"（"Hardware capable, requires future SW development"），投标应答需核实当前版本，勿写成已支持（X8，<<<PAGE 65>>>）
- 6360/6370/6570M 的 10G/25G 速度默认关闭（默认 1G），许可行项勿漏（X15，<<<PAGE 17>>>/<<<PAGE 26>>>/<<<PAGE 66>>>）
- 6870 50G 上联需许可（X16，<<<PAGE 111>>>）；6570M 高级路由需 SW-AR，默认只有基础 L3（X17，<<<PAGE 65>>>）
- 6370 NDcPP 认证"未来版本支持"，标书不能声称已认证（6360/6560 已 NDcPP EAL1 可对比）（X18，<<<PAGE 25>>>）
- 6870 按 bundle（##）下单，包内电源/许可内容需确认（X21，<<<PAGE 112>>>）

来源：bp-omniswitch-datasheets verified.md（C9/X8/X15-X18/X21/F2/P7/P10/P14）
