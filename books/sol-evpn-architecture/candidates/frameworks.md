# frameworks — sol-evpn-architecture（决策框架 / 思维模型）

## F1 EVPN 演进决策链：为什么选 EVPN（问题→方案映射框架）
传统模型的五类问题（资源低效 / 稳定性 / 可扩展性 / 运维复杂度 / tromboning）逐项映射到 VXLAN/EVPN 能力。用途：向客户论证技术选型。
- 数据：STP 阻塞链路 → routed underlay；4096 上限 → 24-bit VNI（约 1600 万）；洪泛学习 → 控制平面学习。<<<PAGE 5-9>>>
- 引用："Modern data centers required an evolution from the traditional flood-and-learn and VLAN segmentation networking due to the limitations placed on such model." <<<PAGE 5>>>

## F2 Underlay/Overlay 设计选型框架
决策变量：underlay 协议（OSPF/IS-IS/eBGP）× overlay（iBGP/eBGP）× RR 拓扑（全网状 vs 冗余 RR）。AOS 推荐态：OSPF 单区域 + p2p + BFD + 冗余 RR（同 cluster-id）+ iBGP overlay + TTL security 0。EVPN-VXLAN 限定单一 underlay VRF。
- 引用："Typically, the options which are configured in Data Center topologies, include OSPF/IS-IS underlay with an iBGP overlay, or eBGP for both underlay and overlay. The recommended topology to be used is an OSPF underlay with iBGP overlay." <<<PAGE 45>>>

## F3 IRB 模型选型框架（非对称 vs 对称 × host-based vs prefix-based）
决策变量：是否全 PE 配全 EVI、ARP/MAC-VRF 维护范围、SBD(L3EVI) 是否存在。判定：对称 IRB + interface-ful SBD 模型为主流推荐；prefix-based 只能走对称；host-based 两者皆可。RFC 9136 三模型（interface-less / interface-ful SBD / interface-ful unnumbered）按 overlay index 类型区分。
- 引用："The Symmetric IRB model is simpler for configuration and deployment and offers better scalability... and therefore is the prevalent and recommended configuration." <<<PAGE 24>>>

## F4 Multi-homing 模式与防环机制框架
决策链：单归属(SH) / 单活(SA) / 全活(AA) → LACP vs 静态 LAG（决定 ESI 自动/手工）→ DF 选举（service carving: DF = EVI mod N）→ 防环三件套（split horizon / local bias / ES pruning）→ 流量优化（aliasing 负载分担、backup path 主备、mass withdraw 快收敛）。
- 引用："The default algorithm used is a modulo-based algorithm, which is (DF = EVI mod N), where N is the number of PEs in the RT list." <<<PAGE 33>>>

## F5 BUM 复制与外部连通性设计框架
BUM：tandem replication（组播底层、核心高效、配置复杂）vs ingress replication（R-T3、简单、单播复制低效；AOS 仅支持后者）。外部连通：border leaf 位置 → Fabric-VPN + GRM 注入 → 路由汇总策略（route-map + ACL 只放聚合）→ 双 leaf 防回声（import 优先级）。
- 引用："Each of these methods have their pros and cons." <<<PAGE 29>>>；"A route-map policy needs to be defined with a specific ACL. This ACL will contain only the aggregate route for each IRB subnets." <<<PAGE 48>>>
