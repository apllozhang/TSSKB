# BOOK_OVERVIEW — OmniSwitch AOS Release 8.10R4 Advanced Routing Configuration Guide

- 313 页，Part No. 060970-00 Rev A，December 2025，ALE（Alcatel-Lucent Enterprise）
- 面向 OmniSwitch 6360/6465/6560/6570M/6575/6860/6865/6870/6900/6920/9900 系列交换机
- 高级路由协议为基础交换软件的附加购买包（add-on package）
- 全文：`fulltext.md`，页码标记 `<<<PAGE N>>>`，共 313 页

## 章节结构（正文实际章节）

| 章 | 主题 | 内容要点 | 页范围（正文页码 N） |
|---|---|---|---|
| 1 | Configuring OSPF | OSPF 区域/路由器分类/虚链路/Stub 区域/ECMP/NBMA/GR（冗余 CMM）；被动接口 Route Map、静态邻居、BGP→OSPF 重分发、应用例 | 约正文页 25–60 |
| 2 | Configuring OSPFv3 | OSPFv3 区域/虚链路/Stub/NSSA/ECMP/GR、重分发、应用例 | 约正文页 65–98 |
| 3 | Configuring IS-IS | IS-IS 报文/区域/Level、认证、Route Map 重分发、GR（堆叠）、Multi-Topology IS-IS (M-ISIS)、IPv4/IPv6 | 约正文页 99–130 |
| 4 | Configuring BGP（本书最重章，约占 1/3 篇幅） | AS/iBGP vs eBGP/Community/RR/联邦/策略(Route Map)/路由抖动抑制/CIDR、Peer 配置、聚合、本地网络、Route Reflection、联邦、重分发、GR、IPv6 BGP（MP-BGP）、Routing Policies、GTSM、VPLS BGP 信令、BGP EVPN、BGP Neighbor Template、VRF 内 BGP Peer 数量提升 | 约正文页 131–225 |
| 5 | Multicast Address Boundaries | IANA 组播地址、组播地址边界（过滤外发组播）、并发组播地址 | 约正文页 226–235 |
| 6 | DVMRP | 逆向路径组播/邻居发现/路由报告/依赖下游与毒性反转/剪枝/嫁接/DVMRP 隧道 | 约正文页 236–250 |
| 7 | PIM | PIM-SM（RP 树、Register、SPT 切换）、PIM-DM、SSM、Bootstrap/RP 发现、Join/Prune 打包、IPv6 PIM 全套、RP-Switchover | 约正文页 251–300 |
| 8 | Multicast Border Router (MBR) | PIM↔DVMRP 边界、PIM 路由通知、DVMRP 默认路由通告 | 约正文页 301–306 |

附录 A 为许可证；Index 无正文。

## 提取注意事项

- 页码标记只有全书连续页号 `<<<PAGE 1>>>`–`<<<PAGE 313>>>`，正文页脚的 "4-15" 为章内页码，两者需区分；候选条目统一引用 `<<<PAGE N>>>` 的 N。
- 命令行均为 AOS CLI（如 `ip ospf`、`router bgp`、`ip pim`、`ipv6 pim`、`ip dvmrp` 等）。
- 本书无独立 VRF-Lite / 隧道专章；VRF 仅在 BGP 章（Increase BGP Peer Support in VRF）出现，隧道仅 DVMRP tunnel 小节。
