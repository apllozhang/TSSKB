---
name: ap-selection-matrix
description: 何时用：客户给出 Wi-Fi 代际/环境/规模需求，需要锁定具体 Stellar AP 型号与配件编码时。
source_book: DT00XPS288EN Stellar WLAN Presales
---

# AP 选型三维矩阵（代际 × 形态 × 市场分层）

## R · 原文引用

> "OMNIACCESS STELLAR LINEUP – WI-FI 6: Wi-Fi 6 Indoor MLE AP132x / Wi-Fi 6 Outdoor Rugged AP136x / Wi-Fi 6 Indoor SMB AP1311 / Wi-Fi 6 Indoor SMB AP1301 / Wi-Fi 6 Indoor MLE AP1351 / Wi-Fi 6 Indoor MLE AP1331 / Wi-Fi 6 Indoor Hosp. AP1301H"（p11）

> "In your project, identify: The client devices (type, number, authentication); The type of traffic (applications); The environment (indoor/outdoor, low/high density, open/complex environment); The capacity (number of clients, % of concurrent clients, uplink bandwidth required)."（p239）

> "Access points compatible with external antennas have their reference ends with '2' (ex. AP1322, AP1362). Note: All OmniAccess Stellar Access Points are equipped with an internal antenna."（p32）

> "OMNIACCESS STELLAR AP1521 • Tri radio • 5GHz radio: 2.88Gbps (4x4:4SS/EHT160) • 6GHz radio: 5.76Gbps (2x2:2SS/EHT320) • 1 x 1/2.5/5/10GE multi-gigabit uplink … Mid-range Wi-Fi 7 AP."（p27）

## I · 方法论骨架

三维逐层收窄选型：**第一维 Wi-Fi 代际**（按预算与终端能力：Wi-Fi 5/6/6E/7）→ **第二维形态**（Indoor 室内 / Outdoor Rugged 室外三防 -40~+65°C / Hosp. 客房病房壁挂）→ **第三维市场分层**（MLE 中大型 / SMB 中小 / 特化行业）。

配套速判规则：

| 规则 | 内容 | 用途 |
|---|---|---|
| 需求五问（p239） | 终端、流量、环境、容量、覆盖场景 | 勘察前访谈提纲 |
| 尾数"2"规则 | 型号以 2 结尾（AP1322/AP1362）支持外接天线 | 零成本检查 |
| 下单编码 | OAW-APxxxx-Region（RW/JP/ME/US） | 区域码错→注册失败 |
| 关键机型档位 | 客房 AP1301H / 三射频高密 AP1231、AP1321 / 室外 AP1361、AP1251 / Wi-Fi 7 AP1511(入门)、AP1521(中档 10GE) | 按场景对号 |
| Offices 基准（p239） | 500+ 客户端、50%+ 并发、10G+ 上行 → AP1231/AP13xx/14xx/15xx | 场景→选型对照 |

机型规格速记：AP1301H 双频 2x2 + 专用扫描射频、1024 客户端、下行 PoE-PSE 出电 + 3×1GE + USB + 控制台直通（每房一台、房内有线终端接入）；AP1231 三射频 Wi-Fi 5（2×1733Mbps + 800Mbps、768 客户端、2.5GE 口）；AP1511/AP1521 Wi-Fi 7 差异在 5G 2x2 vs 4x4、上联 5GE vs 10GE。

## A1 · 书中案例

- 轮渡客舱/医院病房用 AP1301H（下联出电服务房内有线终端）；船桥室外 AP1251（c05/c08/c18）。
- 高密场馆 1500 人×50% 并发 → 8-10 台三射频 AP1231/AP1321（c09/p249）。
- 零售 40+ 门店 150 台 AP1301/1311/1251 由 Cirrus 10 管理（c07）。

## A2 · 触发场景（含与相邻 skill 的区分）

- 触发：客户需求访谈后要出 AP 清单和型号；或答标被问"为什么选这个型号"。
- 区分：只锁硬件型号用本 skill；管理模式（Express/OV2500/Cirrus）选型去 `management-mode-selection`；数量估算（客房公式/场馆估算）去 `rf-scenario-baseline`。

## E · 可执行步骤

1. 用需求五问收集：终端类型数量认证、应用流量、室内外/密度、并发比例与上行带宽。
2. 定代际：按终端 Wi-Fi 能力与预算（Wi-Fi 7 仅 AP1511/AP1521，中高档）。
3. 定形态：室外三防→AP1361/AP1251；客房病房→AP1301H；高密室内→三射频 AP1231/AP1321。
4. 定档位：SMB 入门 AP1301/1311 vs MLE AP132x/1351。
5. 需外接天线？尾数必须是"2"。
6. 下单写全 OAW-APxxxx-Region，核对区域码与目标国国家码一致。

## B · 边界与陷阱

- AP1301/AP1230 系列不支持 Zigbee（IoT 项目勿报入门机型，ce09）。
- AP1101 不支持 RAP；AP1101/AP1201/AP1201H 桥接不打 VLAN 标（ce10）。
- 教材 p243 将 AP1301H 误标 802.11ac，以 p17 硬件章（Wi-Fi 6）为准；p95 出现不存在的"AP1421"（应为 AP1521）（ce23）。
- Wi-Fi 7 内容浅、无竞品对比数据；投标前用 MyPortal WPL 复核在售机型。

---
来源条目: f01, f18, p01, p18, c07, c08, c09, c10, ce09, ce10, ce23；glossary: OAW-APxxxx-Region、BLE Beaconing、EDUROAM、Wi-Fi 7 相关词条
