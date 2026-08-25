---
name: OmniSwitch 汇聚与核心/DC 选型（OS6860/6865/6870/6900/6920/9900）
description: 售前选接入旗舰（6860/6870）、工业 L3 汇聚（6865）、固定核心（6900）、400G AI/HPC（6920-D32）、模块化核心（9900），核对 PoE 预算天花板、ISSU、MACsec E 后缀与 9900 线卡 75W 口位时使用。
source_book: bp-omniswitch-datasheets（OS6860 p82-98 / OS6865 p99-109 / OS6870 p110-124 / OS6900 p125-137 / OS6920 p138-144 / OS9900 p145-158）
---

## R（触发场景）
- 接入旗舰/汇聚：6860（95W+200G 堆叠）vs 6870（OmniFabric 高端）
- 核心层：固定 6900 vs 模块化 9900 取舍；线卡扩容投资保护
- AI/GPU 集群与 RoCEv2 存储无损网络：6920-D32
- 医院/生产网不中断升级：ISSU 与 CMM 虚拟机化写进技术条款

## I（核心理念）
高性能线三层（F1）：6860 是接入旗舰（95W PoE + 200G 堆叠 + SPB/VxLAN/MPLS 全 fabric，PoE 预算天花板 3.4kW，P11/P12）；6870 是 OmniFabric 高端接入（premium 95W/advanced 60W 分档，256bit MACsec 全端口）；6900 是固定核心（1RU 6.4Tb/s、VC 6 台）；6920-D32 是 400G AI/HPC（12.8Tb/s、RoCEv2+PFC 无损）；9900 是模块化旗舰（OS9907 10800W PoE、线卡混插扩容、CMM 虚拟机化升级不掉线）。加密认 E 后缀：6900 只有 X48E/C32E 全口 MACsec（C5/X9）。

## A1（行动框架）
1. 定层级：接入旗舰/移动与 IoT 密集 → 6860；要三 fabric 合一 + AI 遥测 → 6870；中型园区/DC ToR → 6900；大型园区要 GbE 密度+PoE 核心 → 9900；GPU/存储无损 → 6920-D32
2. 核对 PoE 预算与口位：6860N 双 BPXL 3390W（仅 230VAC）；9900 PoE 线卡仅前 8 口 75W——高功率 AP 映射指定口段（C11）
3. 核对加密：全口 MACsec 认 6860/6870 全系、6900 的 X48E/C32E
4. 不中断升级：6900 VC 1+N 冗余+ISSU、9900 CMM 虚拟机化、6370 ISSU
5. 6920 场景确认：单一型号 D32 无接入能力，接入层另配（X13）

## A2（选型速查表）
| 系列 | 定位 | 关键规格 | PoE/加密 | 堆叠/VC | 页码 |
|---|---|---|---|---|---|
| OS6860（E/N） | 接入旗舰 | N 型 95W+10G 多千兆+SFP28 25G；E 型 60/75W；premium 模块化上联 4x10G~1x100G | 3.4kW 天花板；全系 MACsec | 200G 堆叠；E 型 40G QSFP+ | <<<PAGE 82-85>>> |
| OS6865 | 工业 L3 旗舰 | -40~74°C，SPB-M VPN，1588v2，auto-fabric | 每型 4 口 75W | 专用 20G VC 口（U28X） | <<<PAGE 99>>> |
| OS6870（premium/advanced） | OmniFabric 高端接入 | premium：24x10G/48x5G 多千兆、上联 2x100G 或 6x25/50G（50G 需许可）；advanced：2.5G/60W、固定 2x100G VFL | 全端口 256bit MACsec；premium 95W | 100G（adv）/200G（premium/U32） | <<<PAGE 110-111>>> |
| OS6900 | 固定核心/DC | 1RU 6.4Tb/s，最高 128x10G/80x25G/32x100G | 仅 X48E/C32E 全口 MACsec | VC 6 台+ISSU | <<<PAGE 125-127>>> |
| OS6920-D32 | 400G AI/HPC | 32x400G QSFP-DD，12.8Tb/s，RoCEv2+PFC 无损；Azure Local 认证 | 无 PoE | 无 VC | <<<PAGE 138-139>>> |
| OS9900（9907/9912） | 模块化机箱 | 9907 11RU：288 GbE/240 SFP+/108 QSFP28；9912 17.25RU；线卡扩容投资保护 | 10800W/7920W；PoE 线卡前 8 口 75W+40 口 30W | 双机箱 VC（960x10G 未来支持） | <<<PAGE 145-147>>> |

## E（选型决策案例）
- 核心选择：中型园区/DC ToR 用 6900（1RU 6.4T）；大型园区要 GbE 密度+PoE 核心用 9900（288 GbE+10800W，线卡后续扩容）（C3，<<<PAGE 125>>>/<<<PAGE 145>>>/<<<PAGE 147>>>）
- GPU 集群/RoCEv2 存储：6920-D32 32x400G 可拆分灵活配 spine/super-spine/border-leaf，Azure Local 混云认证是差异化（C4，<<<PAGE 138>>>）
- 需要加密的校园/DC 上行：认准 E 后缀与 256bit——6900 只有 X48E/C32E；6870 升级到 256bit 且含用户口（C5，<<<PAGE 127>>>/<<<PAGE 111>>>）
- 医院/生产网：6900 虚拟机箱+ISSU、9900 CMM 虚拟机化，业务连续写进技术条款（C10，<<<PAGE 127>>>/<<<PAGE 146>>>/<<<PAGE 24>>>）

## B（反例与坑）
- 6900 非 E 型号（V48/X24/T24/C32）无全口 MACsec，加密需求认准 X48E/C32E（X9，<<<PAGE 127>>>）
- 9900 双机箱 VC 960 口规格属"未来支持"，尚未交付（X10，<<<PAGE 147>>>）
- 9900 PoE 线卡仅前 8 口 75W/线卡 1800W，核心直连大功率 AP 要算口位（X11，<<<PAGE 147>>>）
- 6860N 3390W 最高预算仅 230VAC 下可达，115V 站点达不到（X20/X22，<<<PAGE 84>>>/<<<PAGE 85>>>）
- 6870 按捆绑包（bundle ##）下单，需确认包内电源/许可内容（X21，<<<PAGE 112>>>）
- 6920 单一型号 D32、无 GbE/PoE 接入能力，接入层必须另配（X13，<<<PAGE 138>>>）

来源：bp-omniswitch-datasheets verified.md（C3/C4/C5/C10/C11/X9-X13/X20-X22/F1/P11-P14/P19-P24）
