---
name: license-quotation
description: 何时用：OV2500 / Cirrus 4 / Cirrus 10 三体系拼 License part number、选服务档位、做报价自查时。
source_book: DT00XPS288EN Stellar WLAN Presales
---

# License 三体系报价法（OV2500 / Cirrus 4 / Cirrus 10 Part Number 规则）

## R · 原文引用

> "OV 2500 / Stellar WLAN Mandatory License: AP License - OV2500-NG-AP … Optional License Modules: Guest License - OV2500-NG-GUEST; On-Boarding License - OV2500-NG-ONBOARDING; High Availability License - OV-NMS-HA; Web Content Filtering License - OV-AP-WCF."（p131）

> "License category: Low end Stellar models: APL, High end Stellar models: APH, OmniSwitch 63xx model: 63 … License level: BASE: BAS, BUSINESS: BIZ, PREMIUM: PRM. License duration: 1Y / 3Y / 5Y. Total number of license part numbers: 7 x 3 x 3 = 63."（p153）

> "OmniVista Cirrus 10 - TAC access: Not Available / For Partner / For End Customer. Hardware service (advanced replacement) and support: Not Available, sold separately / For Partner / For End Customer."（p155，注意书内此处把 Premium 缩写误印为 BAS）

> "PW2R-OVBYOD100N: P=Partner; W=Software support; 2=2 Years; R=(Maintenance) Renewal … SP5N-OAWAP1201: S=End Customer; P=(Support) Plus (with AVR); 5=5 Years; N=New."（p137）

## I · 方法论骨架

**铁律：先锁管理模式，再选对应 part number 表**——三套语法相近但互不通用。

| 体系 | 语法 | 要点 |
|---|---|---|
| OV2500（永久） | OV-AP-NM-X-N（X=10/20/50/100/500）；OV-GA-X-N / OV-BYOD-X-N（X=20/50/100/500/1000/5000/25000）；OV4-NMS-HA；OV-AP-WCF-10-N | 1 必选 + 4 选配；按档位向上取整；Starter Pack 免评估 60 天、附 10 Guest + 10 BYOD |
| Cirrus 4（旧云订阅） | OVC-AP-BAS-XY / OVC-AP-BIZ-XY / OVC-AP-XY（X=1/3/5 年） | 每 AP 1 License 附 50 Guest + 50 BYOD；Freemium 免费但不能做网络配置；单订阅 ≤5000 License |
| Cirrus 10（新 SaaS） | **OVCX-[类别7]-[级别3]-[时长3]** = 63 个 PN | 类别：APL（低端如 AP1x0x/AP1x1x/AP1x2x）/APH（其余，如 AP1431）/63/64/65/68/69；级别 BAS/BIZ/PRM；时长 1Y/3Y/5Y |

维保编码逐位：PW/SP 前缀（P=Partner/S=End Customer；W=软件支持/P=Support Plus 含 AVR）+ 年数 + R 续保/N 新购 + 产品缩写 + 数量。

报价四要素清单：AP 硬件（OAW-APxxxx-Region）+ License + 配件（支架 OAW-AP-MNT-X、PoE 供电器、天线 ANT-O/ANT-S）+ 维保合约（1/2/3/5 年）。

激活三步（云订阅）：eBuy 下单 → Subscription Manager 建订阅（拿 Subscription ID + 激活码）→ Cirrus 10 License Management 导入并逐台分配。

## A1 · 书中案例

- OVCX-68-BIZ-3Y：知道型号（OS6860N-P24Z→68）、级别、年限即出编码（f11/p23）。
- AP1431 → OVCX-APH-xxx-nY（类别判定示例，p154）。

## A2 · 触发场景（含与相邻 skill 的区分）

- 触发：拼云管或本地管报价单、客户问"Base 便宜能不能买"、续费老订阅、自查报价防漏项。
- 区分：本 skill 只管 License/维保编码；管理模式本身的选型逻辑去 `management-mode-selection`；Network Advisor 单独计价去 `network-advisor-aiops`。

## E · 可执行步骤

1. 确认客户网管平台（OV2500 / Cirrus 4 / Cirrus 10），选对应 PN 表。
2. Cirrus 10：盘点设备型号 → 归类 APL/APH/63-69 → 按"谁找 TAC、要不要硬件更换"定 BAS/BIZ/PRM → 定年限拼 OVCX 编码。
3. OV2500：AP 数/访客数/BYOD 数分档向上取整；WCF 按 ceil(AP 数/10) 买。
4. 四要素过单：AP、License、配件、维保（含 PW/SP 编码）。
5. 云订阅交付：eBuy → Subscription Manager → 云导入（当实施交接清单）。

## B · 边界与陷阱

- 混用体系 PN 会被 eBuy 退回或激活失败；Cirrus 4 存量续约须单独向 ALE 确认迁移政策，书中没讲清（ce01）。
- Freemium 只能看不能改、仅一次性升级——别当"免费云管"卖（ce02）。
- Base 档不含设备 TAC 与 AVR 硬件服务（Cirrus 4 与 10 皆然），压价翻车点（ce03）。
- Cirrus 10 排除 AP1101/AP1201H/L/LH，交换机须 8.9R——报价前先盘点存量（ce04）。
- WCF 零头也要整份（12 台买 1 份会 2 台没过滤）（ce14）。
- p155 Premium 缩写笔误（BAS→应为 PRM）；价格均为目录价，区域折扣另询。

---
来源条目: f07, f08, f09, f10, f11, f12, p15, p16, p17, p18, p19, p20, p21, p22, p23, p24, ce01, ce02, ce03, ce04, ce14；glossary: OV2500-NG-AP、OVCX-[Category]-[Level]-[Duration]、Freemium/Premium、Starter Pack、Maintenance Contract (PW/SP)、eBuy、OmniVista Cirrus 4、OmniVista Cirrus 10
