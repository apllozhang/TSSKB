---
name: multicast-troubleshooting
description: 何时用：组播流不通/断流，IGMP 加组异常，DVMRP/PIM 邻居或 RP 问题，单播通而组播不通的场景。
source_book: DT00XTE221EN OmniSwitch LAN Troubleshooting
---

# 组播排障（L2 IPMS → DVMRP → PIM 分层）

## R · 原文引用

> "-> show ip multicast ... -> show ip multicast group ... -> show ip multicast forward ... swlog appid dvmrp_0 subapp ipmrm level ... swlog appid pim_0 subapp hello level" (p257)

> "There should be 1 dedicated querier in the network ... Querier-forwarding should be enabled only on switches located between multicast sources and the querier ... Zapping should be enabled only on edge devices ... IGMP messages must be sent with TTL equal 1" (p258)

> "If there are multiple DVMRP routers on a subnet ... One of the routers will be selected as the designated forwarder for each source/group pair ... Election by: Lowest metric, As tie breaker, lowest IP address" (p265)

> "Client 1 can ping client 9 but multicast traffic is not routed to client 9 ... It sends the stream on Multicast group 231.1.1.1" (p280)

## I · 方法论骨架

1. **分层排查**（f13）：L2/IPMS 层（show ip multicast 全局开关 / group 组注册成员 / forward 转发表 / source 源表；debug ip packet show-multicast on board ni <#> 看 IGMP 查询收发）→ DVMRP 层（show ip dvmrp [neighbor/route/prune/interface/nexthop]；swlog appid dvmrp_0 subapp routes|ipmrm level debug3）→ PIM 层（show ip pim [neighbor/candidate-rp/interface/group-map/sgroute/notifications]；debug 按 subapp 细分：hello/boot-strap/crp/sm-join-prune）。
2. **L2 设计五规则**（p32）：全网只 1 个 querier；querier-forwarding 只在源与 querier 之间的交换机上启用；zapping 只在边缘设备；proxying 可全网；IGMP 报文 TTL 必须 1。监测：show ip multicast 看 Status/Querying/Proxying/Spoofing/Zapping/Robustness=2/Query Interval=125s，show interfaces flood rate。
3. **DVMRP DF 选举**（p33）：同网段多台 DVMRP 按（源,组）对选唯一转发者——先比最低 metric，平手比最低 IP。收不到流时从源到接收端走一遍组播路径，debug 看 tDvmrp::Lookup S,G、A new (S,G) entry、Forward 判转发向量是否建立；show ip mroute 看上游邻居。
4. **PIM-SM 命令分工**（p34/g28）：show ip pim（全局，Keepalive=210s）；neighbor（Hello 30s、J/P 60s）；candidate-rp（参选 RP 组范围与优先级）；interface（DR 选举）；group-map（组→RP 映射）；sgroute（(S,G) 表与 RPF 接口）；notifications（邻居丢失/非法 Register/非法 J-P）。RPF 跟随单播路由表。

## A1 · 书中案例（LAB 故障根因）

- **c09（LAB4 案例3，p280-292）**：Client1（监控摄像头源，组 231.1.1.1）发流，Client9 收不到；单播互 ping 正常。排查：从 6360-A traceroute 192.168.110.50 确认单播路径经 192.168.57.7→172.16.17.1（PIM-SM 的 RPF/join 沿单播路径走）；show ip pim interface 逐台核——6870-A 五个口 PIM enabled，而 6900-A 路径上的 int_217 没启用 PIM，join 到不了源侧。修复：`ip pim interface int_217`，发流验证。方法沉淀：组播不通先 traceroute 单播路径，再沿路径逐接口核 PIM 使能状态。

## A2 · 触发场景（含与相邻 skill 的区分）

- 触发：组播流不通或断流、IGMP 加组/离开异常、频道切换问题、PIM 邻居丢失、RP/BSR 选举异常、组播引起广播洪泛。
- 区分：**单播也不通 → l3-routing-vrrp**（先修单播，RPF 依赖单播路由）；纯 L2 同网段组播泛洪 → 本 skill 的 IPMS 层；组播风暴引发 CPU 高/环路 → 先按 stp-loop 查环。

## E · 可执行步骤

1. 先验证单播路径通（ping/traceroute 到源），不通先修单播。
2. L2 层：show ip multicast 核全局开关与 querier 位置 → show ip multicast group 核接收端加组 → show ip multicast forward/source 核转发表 → 按五规则核查设计（querier 唯一、forwarding 位置、zapping 边缘、TTL=1）。
3. 需要看 IGMP 报文：debug ip packet show-multicast on board ni <#>。
4. DVMRP 环境：show ip dvmrp neighbor/route/prune → swlog appid dvmrp_0 subapp routes level debug3 看转发向量与 DF 选举。
5. PIM 环境：traceroute 单播路径 → 沿路径逐台 show ip pim interface 核 PIM enabled 与 DR → show ip pim neighbor / candidate-rp / group-map 核 RP 可达 → show ip pim sgroute 核 (S,G) 与 RPF 接口 → 需要时按 subapp（hello/boot-strap/crp/sm-join-prune）分别调 debug3。
6. 修复后源发流、接收端验证，**日志调回 info**。

## B · 边界与陷阱

- "单播通组播不通"几乎总是 PIM 未在路径某接口启用或 RPF 不通（c09），逐跳核 show ip pim interface 比全局 debug 更快。
- 多 querier 不会报错而是选举+其余 inactive，浪费且易错——设计期就核（p32）。
- IGMP 报文 TTL 必须为 1；跨网段送达失败常因中间设备转发了 TTL=1 报文或改了 TTL。
- querier-forwarding 配错位置（不在源与 querier 之间）是隐性断流源。
- debug 分区很细，先明确查哪层（hello=邻居、boot-strap/crp=RP 选举、sm-join-prune=加入剪枝）再调级，用完回 info。

---
来源条目: f13, p32, p33, p34, g28, g29, g30, c09
