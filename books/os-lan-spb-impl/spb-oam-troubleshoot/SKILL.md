---
name: spb-oam-troubleshoot
description: 何时用：SPB 骨干/服务验收与排障——mac-ping 连通测试、SAA 持续探测、IS-IS 逐层命令链时。
source_book: DT00XTE323EN SPB Concepts & Implementation
---

# SPB OAM 排障命令手册（mac-ping / SAA / 验证链）

## R · 原文引用

> "Mac-ping: Proprietary ping — The timeout for each ping request packet is 1 sec. (not configurable) -> sw2-> mac-ping dst-mac e8:e7:32:a4:77:7d vlan 4015 Reply from E8:E7:32:A4:77:7D - 1/1/5 : bytes=64 seq=1 time=109us" (p147)

> "-> saa spb auto-start ... SAA sessions are created for each VLAN/MAC pairing. If the destination MAC is on a link aggregation group, SAA traverse all paths of the Linkaggs" (p147/148)

> "SPB creation parameters: Auto-create: Enabled, Auto-start: Enabled, Interval(minutes): 1, Jitter Threshold (us): 100, RTT Threshold (us): 500, Payload-Size (bytes): 32, Num-pkts: 5, Inter-pkt-delay: 1000, Keep: Disabled" (p150)

> "• Destination MAC cannot be a broadcast, multicast, or NULL address" (p147)

## I · 方法论骨架

1. **两层排障法**（f12）：第一层 mac-ping 点测（先 `show spb isis info` 拿对端 B-MAC，再按 BVLAN 测连通与时延）；第二层 SAA 持续探测（自动为每个 BVLAN/B-MAC 对建会话，分钟级统计 RTT/Jitter，写 /flash/network/saa.xml）。
2. **IS-IS 逐层验证链**（f04）：配置（bvlans/vlan id）→ 接口（interface）→ 邻接（adjacency）→ 节点状态（info）→ 转发表（unicast-table）→ 路径（spf）→ 数据库（database/nodes），自底向上收敛故障层。
3. **前后对拍法**：故障切换/调优实验用 `show spb isis unicast-table` 前后对比确认换路（教材 p127-128 即此用法）。
4. **三层表对拍查路由**（L3 场景，源自 c10）：`show spb ipvpn route-table` → `show ip global-route-table` → `show ip routes`（IMPORT 标记）。

## A1 · 书中案例（Lab 配置序列精要）

mac-ping 实测（p147）：
```
show spb isis info                          ! 取对端 B-MAC
mac-ping dst-mac e8:e7:32:a4:77:7d vlan 4015
! 可选: priority|drop-eligible|count|interval|size|isid-check
```
SAA 部署与查看（p147-150）：
```
saa spb auto-start
show saa spb
show saa statistics aggregate               ! RTT/Jitter min/avg/max + 丢包
```
验证链示例（p85）：`show spb isis bvlans` / `show spb isis interface` / `show spb isis adjacency detail` / `show spb isis info` / `show spb isis unicast-table bvlan 2000` / `show spb isis spf bvlan 2000 [bmac <BMAC>]` / `show spb isis database [lsp-id]` / `show spb isis nodes`。

## A2 · 触发场景（含与相邻 skill 的区分）

- 部署后验收（逐对测通）、长期监控（阈值告警）、故障定位（邻接/转发/路径哪层断）时用本 skill。
- 与 `spb-backbone-deploy` 的区分：那个 skill 管"配上去"，本 skill 管"测出来"；验证链命令在部署 skill 的 E 步骤里被引用，完整用法与限制集中在此。
- L3VPN 的"路由学到没有"三级表对拍模板归 `ip-over-spb`（c10），本 skill 补充通用 OAM 工具。

## E · 可执行步骤

1. 点测连通：`show spb isis info` 取对端 B-MAC → `mac-ping dst-mac <BMAC> vlan <BVLAN>`，看 reply 的出接口与 time。
2. 持续监控：`saa spb auto-start` → `show saa statistics aggregate` 看 RTT/Jitter/丢包；阈值默认 RTT 500us / Jitter 100us。
3. 故障分层：按 f04 验证链从 bvlans 往 nodes 逐层执行，第一层异常处即故障域（如 adjacency 不 UP 查接口/物理，unicast-table 缺项查 IS-IS 通告）。
4. 换路确认：操作（断口/metric/overload）前后各抓一次 `show spb isis unicast-table bvlan X` 对拍。
5. 组播路径：用 `show spb isis multicast-table` 查表（不能用 mac-ping）。

## B · 边界与陷阱

- **mac-ping 目标不能是广播/组播/空地址**（p26/ce10）：必须先取对端单播 B-MAC；tandem 组播树地址 ping 不了。
- **每包超时固定 1 秒不可配**（p26/ce10）：时延基线注意此粒度。
- SAA 对 LAG 目的会遍历所有成员链路（f12）——聚合链路的每条路径都被覆盖，统计里会看到多条路径的结果。
- SAA 默认参数（p27）：1 分钟/轮、5 包、包间隔 1000us、载荷 32 字节；历史文件 /flash/network/saa.xml（文件名/周期可配）。
- 服务层验证另有 `show spb isis services` / `show service sdp spb` / `show mac-learning domain spb`（归 `spb-l2-service`）。

---
来源条目: f04, f12, p26, p27, ce10, g24, g32