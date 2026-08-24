---
name: rf-scenario-baseline
description: 何时用：酒店客房/高密场馆/会议室/户外四类场景做 AP 数量估算、出推荐配置基线或交付验收 checklist 时。
source_book: DT00XPS288EN Stellar WLAN Presales
---

# RF 与场景化配置基线（客房 / 场馆 / 会议室 / 户外）

## R · 原文引用

> "AP quantity = M/2+N+(M+N)*5%. Explanation: M: number of rooms with normal walls. N: number of rooms with load-bearing wall. 5%: represents the redundant backup. Example: 20 rooms M, 10 rooms N • AP quantity = 21,5. Rounded up to 22 AP1301H."（p243）

> "Load-bearing wall signal attenuation = 30 dBm. Worst case: 5GHz signal in area in the room without AP = -80 dBm → No access; 2.4GHz = -70 dBm → Extremely poor. AP installation: 1 access point per room."（p245）

> "Venue capacity: 1500. Estimated concurrent users: less the 50% → Around 750 active users … Number of APs: 8-10."（p249）

> "Small room 40-60 AP1231/1321 1; Medium room 80-120 AP1231/1321 2; Lecture hall / Conference room 160-200 AP1231/1321 4."（p258）

## I · 方法论骨架

每个场景给"数量估算 + 推荐配置基线"两件套，配置表同构"特性→推荐值→理由"，精髓是**同一特性在不同场景取值相反且有据**。

**数量估算：**

| 场景 | 估算规则 |
|---|---|
| 客房/病房（AP1301H） | **M/2 + N + (M+N)×5%**，向上取整；普通墙 15dB 可隔房装，承重墙 30dB 必须一房一台 |
| 高密场馆 | 容量 × 并发率（约 50%）→ 750 并发 ≈ 8-10 台三射频 AP1231/1321；2.4G 只用 1/6/11、部分 AP 关 2.4G |
| 会议室 | 40-60 客户端→1 台；80-120→2 台；160-200→4 台（并发 100%、每端 ≥2Mbps） |
| 户外 | 并发按 20% 估；AP1361（-40~+65°C）约 6-8 台/200 并发；开阔区抱杆装最高点、802.3at PoE |

**配置基线对照（核心差异）：**

| 特性 | 客房 (p247) | 场馆 (p252) | 会议室 (p261) |
|---|---|---|---|
| RSSI 门限 | 2.4G=20 / 5G=15 | 30 / 30 | 30 / 30 |
| ACS | 开 | **关**（手动锁信道） | 开 |
| 功率 | APC 关、手动 | ≤15dBm | ≤10dBm |
| 信道带宽 | HT20/HT20 | HT20/**HT40** | HT20/**HT80** |
| 强制 5G | 引导开 | 引导+强制开 | 引导+强制开 |
| 限速 | 2/4Mbps | 2/4Mbps | 2/4Mbps |
| BG-S / Load Balance | 关 / 开 | 关 / 开 | 关 / 开 |
| GI | — | Wi-Fi5=0.8us / Wi-Fi6=1.6us | — |

安装规范三件套：壁挂 ≥1.5 米、避开电视/金属柜遮挡、不可装承重墙侧面；场馆吊顶优先（屋顶 ≤5 米）、房间宽 ≤30 米可壁挂。

## A1 · 书中案例

- 客房公式完整实例：20 普通 + 10 承重 = 22 台 AP1301H + 配置基线（c18）。
- 酒店装后审计：信道重叠靠缩信道宽度整改（ce17）。
- 场馆 AP1231 三射频 + 2.5G 上联 + OS6560（802.3bt）防有线瓶颈（c09/p31）。

## A2 · 触发场景（含与相邻 skill 的区分）

- 触发：出 AP 数量与配置初稿、答"配置怎么定的"质疑、做交付验收 checklist、承重墙报价分档。
- 区分：语音场景常数去 `vowlan-deployment`；机型选谁去 `ap-selection-matrix`；本 skill 管"多少台、怎么配"。

## E · 可执行步骤

1. 判场景类型（客房/场馆/会议室/户外），套对应估算规则出数量。
2. 客房先做墙体分级勘察：逐层标注承重墙，按公式分档报价（普通墙/承重墙两套数量）。
3. 按基线表生成场景配置（RSSI/ACS/APC/带宽/限速）。
4. 把装后审计（Ekahau）写进交付标准。
5. 验收按"特性→推荐值→理由"表逐项核对。

## B · 边界与陷阱

- 不区分墙体按"隔房一台"报低价：承重墙楼栋 AP 用量翻倍、预算工期双爆（ce19）。
- 教材 p243 将 AP1301H 误标 802.11ac，以 p17（Wi-Fi 6）为准（ce23）。
- 基线表是"性能优先"：关 BG-S 后 WIPS/APC/快速漫游/Voice-Video awareness 连带失效；有安全/语音诉求须换开 BG-S 的配置档；客房 ATF 关闭是为保护无 AP 房间体验（ce22）。
- 高密同质环境默认信道宽度同频干扰严重，主动预配窄信道（客房 HT20）。

---
来源条目: f20, f21, p29, p30, p31, p32, p33, p34, c02, c09, c18, ce17, ce19, ce22, ce23；glossary: Smart Load Balancing、Access Guardian、WIPS/wIDS
