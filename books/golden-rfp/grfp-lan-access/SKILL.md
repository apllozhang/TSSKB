---
name: 接入交换机机型硬指标对比（2260/2360/6360/6465 端口/PoE/功耗/温度/MTBF 抽样表）
description: 写标书硬件规格章节或做接入交换机选型对比时使用：OmniSwitch 2260/2360/6360/6465 四个机型族 Golden RFP 的端口配置、PoE budget、交换容量/Mpps、功耗、工作温度、MTBF、虚拟化堆叠等硬指标抽样对比，含工业级 6465 的 -40~75°C 与 MACsec 卖点。
source_book: OmniSwitch 2260 / 2360 / 6360 / 6465 Golden RFP
---

## R（何时用）
- 标书要填"设备参数响应表"：端口数、PoE 功率、背板容量、Mpps、MTBF、温度
- 客户选型：桌面接入 vs 无风扇静音 vs 工业 hardened 的分界判断
- 需要同一指标跨四个机型横向比较表

## I（核心理念）
四族定位差异本身就是选型逻辑：**2260** = WebSmart 轻管理千兆（无风扇紧凑型，半宽机架，低成本桌面/IoT）；**2360** = 可堆叠 SME 接入（4 台虚拟化堆叠，X 型号带 SFP+ 上联与光口全 SFP 版本）；**6360** = 园区工作组接入（8 台 virtual chassis，Multi-Gig + 10G PoE 型号覆盖 WiFi 6/7 AP 供电）；**6465** = 工业加固无风扇（DIN 导轨、-40~75°C、全口 MACsec+1588v2，交通/铁路/电力场景）。所有文档共同的反造假口径："The above minimum port count requirements cannot be combo ports. All ports must be capable to operate simultaneously"——最小端口数不许算 combo 口。

## A1（决策要点）
1. 要静音壁挂/半宽 → 2260-10/P10（21.7cm 半宽、fan-less）；要光接入 → 2360-U24X/U48X（24/48 个 SFP 100/1000Base-FX）；要多 gig 上联 → 6360 Multi-Gig 型号；户外/机柜外 → 6465。
2. PoE 档位从低到高：2260-P10 75W → P24 195W → P48 370W；2360-P24 195W（P48 更高）；6360 12 口 PoE 120W → 28 口 PoE 180W → 52 口 350W → 10G PoE 380W → MultiGig 760W；6465 150W → 240W → 285W。
3. 堆叠规模：2260 不堆叠；2360 至多 4 单元（10G 堆叠带宽、216 端口上限）；6360 至多 8 元素单 IP 管理。
4. 认证类卖点按档位：仅 6465 有 MACsec（256-bit）+1588v2 全口、双告警干接点（IN/OUT）、AC/DC 双电源。

## A2（细节速查表）

**2260 代表型号**（sources/grfp-2260.md）
| 项目 | OS2260-10 | OS2260-P10 | OS2260-P24 | OS2260-P48 |
|---|---|---|---|---|
| 端口 | 8×GE+4×SFP | 同左 PoE+ | 24×PoE++4×SFP | 48×PoE++6×SFP |
| 形态 | 1RU 半宽 fan-less | 同左 | 1RU（P24/P48 变速风扇） | 1RU |
| 容量 | ASIC 128G / 转发 24Gbps / 17.9 Mpps | 同左 | 128G / 56Gbps / 41.7 Mpps | 216G / 108Gbps / 80.4 Mpps |
| PoE | — | 75W，perpetual+fast | 195W，perpetual+fast | 370W |
| 温度/湿度 | 0–45°C / 5–95% | 同左 | 同左 | 同左 |
| MTBF@25°C | 2,174k h | 1,042k h | 693k h | 625k h |
| 功耗 idle→满载 | 5.3→15.3W | 7.6→17W | 24.5→40.7W | 35.2→63.2W |
| 三层上限 | IPv4/IPv6 各 2 条静态路由、8/2 个接口；62 VLANs、16k MAC、延迟<4μs、jumbo 12KB（同族共享节） ||||

**2360 代表型号**（法文版源，数字已复核）
| 项目 | OS2360-24 | OS2360-P24 | OS2360-U24X | OS2360-U48X |
|---|---|---|---|---|
| 端口 | 24×GE + 2×SFP(+) | 24×PoE+ 同上 | 24×SFP 光口 + 2×SFP+ | 48×SFP 光口 + 2×SFP+ |
| 容量 | 128G / 92Gbps / 68.4 Mpps | 同左 | 168G / 168Gbps / 125 Mpps | 216G / 216Gbps / 160.7 Mpps |
| PoE | — | 195W perpetual+fast | — | — |
| 功耗 idle→满载 | 13.1→29.5W | 24.5→40.7W | 35.2→77.3W | 44.2→115.8W |
| 特有 | 虚拟 chassis ≤4 台（1+N 冗余管理器）、32 条 IPv4+16 条 IPv6 静态路由、24/4 个 L3 接口、1024 VLANs、CPU 攻击防护、VC 分裂检测恢复 ||||

（2360 非 X 型号标注 fan-less："L'équipement DOIT être sans ventilateur"；U 型为光口版本带风扇与更高功耗。）

**6360 代表型号**（基于 AOS 8.10R4）
| 项目 | 12口 | 12口PoE | 28口PoE | 52口MultiGig 10G PoE |
|---|---|---|---|---|
| 端口 | 8×GE+2 uplink+2 SFP | 同左 802.3at | 24×GE PoE+2 combo+2 SFP+ | 46×GE PoE(at)+2×2.5G PoE(bt)+2 combo+2 SFP+ |
| 容量 | 24 Gbps / 17.9 Mpps | 同左 | 92 Gbps / 68.5 Mpps | 182 Gbps / 217 Mpps |
| PoE | — | 120W | 180W | 760W |
| MTBF | 1,179k h | 1,094k h | 1,447k h | 789k h |
| 共性 | 全系 1RU、0–45°C、5–95% 湿度、non-blocking、RJ45 console+USB2.0、热插拔光口；≥28 口型号支持 8 元素 virtual chassis；电源模块 30W 内置 → 950W 内置 AC 全谱系 ||||

**6465 工业三型号共性卖点**
| 项目 | 要点 |
|---|---|
| 环境 | Ambient -40°C ~ +75°C；DIN/Wall/Panel 三种安装；fan-less |
| 尺寸 | 6/12 口：≤15×8×15cm 半掌大小；28 口 19 英寸上架 |
| 安全 | 全口 256-bit MACsec；全口 1588v2（28 口的 2×SFP+ 除外） |
| 倒换 | Power-redundancy hot swap（in-service）；28 口 AC/DC 双路模块电源 |
| PoE | 150W / 240W / 285W；802.3bt 60W 口若干（6 口型 2 个、12 口型 4 个、28 口型 8 个） |
| 堆叠 | virtual-fabric ≤4 元素单 IP，前面板 VC 配置 LED |
| MTBF | 最高 2,103,668 h（28 口 switch only，含 PSU 后 1,136,119h） |

## E（场景案例/怎么用）
- 标书"PoE 供电能力"一栏：按上面 A2 表直接引用，注意每行补一句 "Perpetual and fast PoE+ support"（2260/2360/6360 均为标准条目）。
- 交通行业项目：6465 组合拳 = -40~75°C + DIN 导轨 + MACsec 全口 + 1588v2 授时 + 告警干接点，逐条对招标书的工业要求。
- 酒店/宿舍光纤到房：2360-U48X（48 SFP 光口 + 160.7 Mpps）直接应答全光接入需求。

## B（限制与坑）
- **2360 文档是法文版**（omniswitch-2360-golden-rfp-fr），抄数字注意逗号小数点（"68,4 Mpps"=68.4）与 "Minimum"/"Maximum" 在原文个别行混用（如 P10 写 "Minimum ystem power consumption idle of 7.6W"，语义应为 maximum idle）——引用功耗数值前对照英文同族 2260 复核。
- 2260 文档同样存在 OCR 错误（"108bGbps"、"power pupply"、"Minimum MTBF"），以数据手册终审。
- 2260 是 WebSmart 定位，三层只有静态路由且条数极少（IPv4/IPv6 各 2 条），别在路由型标书里错用。
- 6360 的 12 口型号 fan-less、28 口及以上也是 Fanless，但 PoE 大功率型号散热依赖机箱设计，现场高温部署仍建议核对安装指南而非只看 RFP 行。
- 电源模块清单按型号严格对应（如 6465 用 OS6465-BPN/BPR PSU，MTBF 数值随是否配 PSU 大幅变化），报价勿漏配。

来源：OmniSwitch 2260 Golden RFP V5.1 / OmniSwitch 2360 Golden RFP 5.1 (FR) / OmniSwitch 6360 & 6465 Golden RFP（AOS 8.10R4）（sources/grfp-{2260,2360,6360,6465}.md）
