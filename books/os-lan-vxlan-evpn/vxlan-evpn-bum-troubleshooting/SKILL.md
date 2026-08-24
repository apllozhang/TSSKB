---
name: vxlan-evpn-bum-troubleshooting
description: 何时用：处理 BUM 复制（HER/组播）、ARP 抑制、MAC 移动/震荡，以及按层定位 EVPN 不通时。
source_book: DT00XTE325EN VxLAN/EVPN
---

# BUM 复制、MAC Mobility 与故障排查（HER / Proxy ARP / 验证命令链）

## R · 原文引用

> Head end replication: One copy of each frame is sent to each known remote VTEP with a unicast IP header. Requires that the VTEP know of all the IPs of the remote VTEPs participating in a VNI, or they will not receive any traffic.（p41；p180 "Only ingress (head-end) replication is supported in the initial release 8.10R1"）

> Enabling the proxy ARP will check for the local proxy-ARP cache and generates an ARP reply if target IP is found, otherwise those ARP requests will be flooded... By default, Proxy ARP is enabled for an EVPN enabled service.（p110/124；p203 "In case Proxy ARP Table is empty, it has probably timed out"）

> When the host moves..., it sends a new R-T2 with the MAC mobility extended community with an incremented sequence number of 1... the PEs retain the R-T2 with the highest sequence number.（p127/177）

> If a CE MAC address is constantly moving between two different Ethernet segments... This is called MAC duplications... leads to degradation of the EVPN network performance.（p177）

## I · 方法论骨架

1. **BUM 两机制**：①头端复制 HER——入端 VTEP 给每个已知远端 VTEP 逐份单播，EVPN 下用 RT3 IMET 自动发现建 ingress replication list；②Tandem 组播——标准 IP 组播，AOS 网关用 PIM-BIDIR（RFC 5015 双向共享树），每 VNI 一个组播组。**8.10R1 EVPN 仅支持 HER**。ARP/BOOTP/DHCP 都按 BUM 处理。
2. **控制面 MAC 学习三步**（p121-123）：ARP 广播→入 PE 泛洪+本地学源 MAC→RT2（仅 MAC，或 snooping 到 IP 后 MAC+IP）经 RR 转发全网→应答单播返回。全程无数据面泛洪学习。
3. **Proxy ARP/ARP 抑制**：PE 收 ARP 先查本地 proxy-ARP 缓存，命中代答、未命中才泛洪；默认启用。四默认参数：arp-suppression=complete、flood-unknown-unicast-suppression=discard、unicast-forward=disable、arp-probe=enable。表项来源：ARP/GARP、DHCP snooping、IPv6 ND、静态。
4. **MAC mobility**：RT2 带 mobility 扩展团体，序列号首通告=0，移动后+1，各 PE 保留最高序列号、亚秒收敛。
5. **MAC duplication 防护**：MAC 在两 ES 反复横跳（根因：ES 网环路或两主机重号）→ RT2 无休止通告/撤销拖垮控制面。全局 `service bgp-evpn mac-mobility loop-protection`（retry-time/threshold/timeout），达阈值 hold-down，**须配在所有 Leaf**。
6. **排障分层顺序**（沿用课堂验证链）：ES→service→SAP→RT3→MAC→SDP 隧道→Proxy ARP→端到端 ping。

## A1 · 书中案例

- Proxy ARP 排障（p203/110/113-114）：`sh ip evpn proxy-arp evi 1000` 初始 Total count: 0，两主机互 ping 后出现 192.168.10.50↔bc:24:11:dd:29:a9 等表项——空表先造流量再回查，仍空才往 RT2 携带 IP、snooping 方向查。
- HER silent failure（p41）：裸 VXLAN（无 EVPN）场景，本端 VTEP 漏学一台远端 VTEP IP，该 VTEP 收不到该 VNI 任何泛洪流量（未知单播/广播/组播全静默丢弃，表现为"部分方向不通"）——排障优先核对 VTEP 对等列表完整性；EVPN 下这正是 RT3 的价值。
- MAC 表双通道（p73/116）：`sh mac-learning evpn-vxlan` 本地 MAC 挂 sap:1/1/7，远端 MAC 挂 sdp:32768——确认控制面学习链是否闭环。

## A2 · 触发场景（含与相邻 skill 的区分）

- 触发：广播/未知单播不通、ARP 代答异常、主机迁移后不通、MAC 震荡告警、BUM 复制方式选型（HER vs 组播）。
- 区分：不通的根因在业务/网关配置 → `vxlan-evpn-service-provisioning`（先核 dummy 口、网关笔误）；根因在多归属/DF → `vxlan-evpn-multihoming-df`；底座路由/BGP → `vxlan-evpn-underlay-bgp-design`。本 skill 管"转发平面的 BUM 行为与控制面学习链排障"。

## E · 可执行步骤

1. 按层核对：`show service evpn`（业务 Up）→ `debug evpn show bgp route-type rt3`（双方互见对端 Loopback）→ `sh mac-learning evpn-vxlan`（sap/sdp 双侧表项）→ `sh service evpn evi <id> tunnel-ports`（SDP 32768 建到远端）。
2. ARP 类故障：先两端互 ping 造流量 → `sh ip evpn proxy-arp evi <id>` 回查 → `show service <id> proxy-arp config` 核四参数 → 仍空查 RT2 是否带 IP（`debug evpn show bgp route-type rt2`）。
3. 防震荡：所有 Leaf 全局配 `service bgp-evpn mac-mobility loop-protection enable retry-time <s> threshold <n> timeout <s>`。
4. HER 规模评估：远端 VTEP 数 ×每 VNI 复制份数估带宽；需要组播承载时核对版本（8.10R1 不支持 tandem）。
5. 端到端验证：同子网 ping + 跨子网 ping + `sh ip evpn proxy-arp summary` 统计。

## B · 边界与陷阱

- **Proxy ARP 空表 ≠ 故障**：表项会老化，先造流量再下结论。
- **MAC duplication 根因二分**：先查 ES 网络后门环路，再查两主机是否真配了相同 MAC；loop-protection 只是把伤害 hold-down，不解决环路本身。
- loop-protection 漏配一台 Leaf，该 Leaf 仍会被震荡路由打爆——必须全网 Leaf 一致配置。
- 裸 VXLAN（无 EVPN 控制面）下 HER 漏学 VTEP 是静默失败，无告警无日志，只能靠对等列表核对发现。
- BUM 组播方案（PIM-BIDIR、每 VNI 一组）在 8.10R1 EVPN 上不可用，别写进当前版本交付方案。

---
来源条目: f06, p10, p14, p15, ce03, ce04, ce09, g02, g13, g17, g23
