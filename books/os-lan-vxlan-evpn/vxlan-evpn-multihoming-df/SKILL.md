---
name: vxlan-evpn-multihoming-df
description: 何时用：CE 双归/多归多台 Leaf（LACP/静态 LAG）、ESI 编码、DF 选举与切换演练时。
source_book: DT00XTE325EN VxLAN/EVPN
---

# EVPN 多归属与 DF（ESI / LACP / ETag / DF carving）

## R · 原文引用

> All-active: ...active/active connectivity of multi-homed devices. LAG is required to be configured between the PE switches and the multi-homed CE device. This is to avoid receiving duplicate packets and for loop prevention.（p182；p141 "All-active or Single-active"）

> AOS (auto-generated) ESI model: 03:Access port MAC(6):ff:ff:ff for physical access port; 03:CE-MAC(6):ff:<Key-Id>(2) for LACP ports.（p142/184-185）

> The default procedure for DF election is referred to as "service carving"... a modulo-based algorithm, which is DF = EVI mod N, where N is the number of PEs in the candidate list. By default, the DF election is pre-emptive.（p182-183）

> On a static lingkagg, ESI has to be provided for an Ethernet segment.（p156；p185 范围表：Physical Port=Auto、LACP LAG=Auto、Static LAG=Manual）

## I · 方法论骨架

1. **模式选型**：all-active（主主，PE-CE 间必须 LAG 防重复包防环，单播按 LACP 哈希）vs single-active（主备，DF 独占一切流量，非 DF 把口拉 down）。**8.10R1 首版仅支持 single-active**。
2. **AOS 默认行为**：物理口默认单归属（SH）；LACP 口默认 MH single-active；静态 LAG 例外——必须手工提供 ESI。
3. **ESI 编码**（RFC 7432 Type 0x3，MAC-based，10 字节=Type 1 + MAC 6 + 本地标识 3）：物理口 `03:<端口MAC>:ff:ff:ff`；LACP 口 `03:<CE-MAC>:ff:<Key-Id>`（admin-key 体现在 Key-Id）。手工 ESI 两端必须一致、全网唯一。
4. **DF 选举**：RT4 发现同 ES 成员后进行，避免 BUM 重复泛洪。默认过程 service carving，算法 DF = EVI mod N（N=候选 PE 数），默认抢占式；可每 VLAN 多 DF 分摊。
5. **冗余接入选型**：Virtual Chassis（配置简单、数据面收敛快、hypervisor 用标准 LACP）vs EVPN MH（配置排障复杂、控制面收敛慢、hypervisor 用静态 bonding）——小规模单机房优先 VC，跨 leaf/多租户用 EVPN MH。
6. **机制链**：RT4 发现对端 → DF 选举 → DF 管 BUM → RT1A/RT1B 支撑 aliasing（负载分担）/backup path/mass withdraw/split horizon 四特性。

## A1 · 书中案例

- Lab3 动态 LACP 跨设备多归属（p153-156）：两 Leaf 各建 `linkagg lacp agg 3 size 2` + `actor admin-key 3`，CE 侧同 agg 挂两口；`service access linkagg 3 evpn-ethernet-segment enable` 自动生成 ESI 03:2c:fa:a2:a2:f2:ad:00:03:00；`service 100 sap linkagg 3:10`。切换演练：断 Leaf1 的 1/1/3 后 ES 角色翻转（sw2 变 MH-SA[L-A]）、永久 ping 不中断、MAC 迁到 sw2 的 sap:0/3。
- Lab3 静态 LAG 手工 ESI（p156-158）：`linkagg static agg 7 size 2` → `service access linkagg 7 evpn-ethernet-segment enable esi 01:01:01:02:04`（呈现 MH-SA[L-M]）→ `service 200 sap linkagg 7:20`；client7 经 sap:0/7 学到、对端经 sdp:32768 学到。
- 架构指南三视图验证（p200-201）：本地单归属 ES 用 `sap-info`（PE 列带 * 为 DF）；本地多归属 ES 用 `carving-info`（EVI 1000→DF 1.1.1.10、EVI 2000→DF 1.1.1.20，mod 分摊效果）；远端 ES 用 `aliasing-info`（Primary/Backup/Others）。

## A2 · 触发场景（含与相邻 skill 的区分）

- 触发：CE/主机/虚拟化双归接入、ESI 规划、DF 或 BUM 重复泛洪排查、VC vs EVPN MH 选型讨论。
- 区分：单归属业务开通 → `vxlan-evpn-service-provisioning`（本 skill 的多归属是在其三部曲上加 LAG/ESI）；BUM 复制机制与 mac mobility 震荡 → `vxlan-evpn-bum-troubleshooting`。

## E · 可执行步骤

1. 动态 LACP：Leaf 侧 `linkagg lacp agg <id> size <n> admin-state enable` + `actor admin-key <k>`，成员口 `linkagg lacp port <port> actor admin-key <k>`；CE 侧同一 agg 挂多口。
2. 启 ES：`service access linkagg <id> evpn-ethernet-segment enable`（LACP 自动 ESI；静态 LAG 必须追加 `esi <10字节>`）。
3. 挂业务：`service <id> sap linkagg <id>:<VLAN>`。
4. 验证三视图：`show service evpn ethernet-segment`（L/R + A/M 标志）→ 本地 `<esi> sap-info`（* = DF，# = 对端缺 ETag 配置）→ 本地 MH 用 `carving-info` → 远端用 `aliasing-info`。
5. 切换演练：断 active 侧成员口 → 确认 `sh linkagg port` 状态机（ATTACHED→CONFIGURED）、ES 角色翻转、ping 不中断、MAC 迁移。

## B · 边界与陷阱

- **8.10R1 仅 single-active**：客户要 all-active 就改方案或等版本。
- **静态 LAG 漏配 esi**：ES 无法正确标识，多归属机制整个不成立——这是静态 LAG 场景第一核对项。
- **命令本地/远端之分**：对远端 ES 执行 sap-info/carving-info 直接报 `ERROR: Command Not supported for Remote ES`；先看 ethernet-segment 总表 ES-Location 是 Local[Auto] 还是 Remote 再选命令，远端用 aliasing-info。
- sap-info 出现 `#` 号 = 对端 PE 缺 ETag 配置（Missing ETAG between Peer-PE nodes）。
- 多归属 ES 场景必须配 DAG 才能保证主机无缝切换（网关跟着任播走）。
- 手工 ESI 两端不一致 = 两个不同 ES，DF/aliasing 全部失效且难查。

---
来源条目: f08, p07, p16, p17, p19, ce05, ce08, c04, c05, c09, g01, g03, g05, g06, g07
