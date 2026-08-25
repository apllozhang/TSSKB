---
name: EVPN 控制面（BGP EVPN/Route Types/主动学习/Underlay-Overlay 设计）
description: 需要理解或设计 MP-BGP EVPN for VXLAN——为什么 EVPN 取代洪泛学习、R-T1~R-T8 各自用途、service interface 模型选择（VLAN-based/bundle/VLAN-aware/enhanced）、ARP 抑制与 proxy ARP、OSPF underlay+iBGP overlay+RR 推荐设计时使用。
source_book: EVPN Architecture Guide（evpn-architecture-guide-en.pdf）
---

## R（触发场景）
- 论证 VXLAN/EVPN 选型（对客户讲 STP/VLAN 模型五大痛点）
- 设计 underlay/overlay：协议选型、RR 冗余、BFD/TTL security
- 选择 service interface 模型与 RD/RT 策略（自动派生）
- 解读 R-T1~R-T8 路由类型与扩展社区

## I（核心理念）
演进决策链（F1，<<<PAGE 5-9>>>）：STP 阻塞链路→routed underlay；4096 VLAN 上限→24-bit VNI（约 1600 万）；洪泛学习→控制平面主动学习（"endpoint reachability information is advertised intelligently through the control plane within MP-BGP NLRI updates"，P1，<<<PAGE 7>>>）；单一控制平面同时承载 L2/L3 服务（P3，<<<PAGE 9>>>）。控制面学到的 MAC 不老化，以对端撤路为生命周期（P5，<<<PAGE 13>>>）。设计选型框架（F2，<<<PAGE 45>>>）：推荐 OSPF underlay+iBGP overlay+冗余 RR（same cluster-id 省内存，P29，<<<PAGE 46>>>）。

## A1（行动框架）
1. Underlay 基线（P26/P27，<<<PAGE 45-46>>>）：单区域 OSPF+p2p 网络类型（免 DR 选举等待）+BFD 毫秒收敛；EVPN-VXLAN 只跑一个 underlay VRF（默认 VRF，P32，<<<PAGE 46>>>）
2. Overlay 基线：spine 兼任 RR、冗余 RR 同 cluster-id、TTL Security max-hop 0（直连断则邻居断，P30，<<<PAGE 46>>>）；VXLAN MTU 由底层承担封装开销（AOS 自动调，P31，<<<PAGE 46>>>）
3. Service 模型选择（P23，<<<PAGE 42>>>）：优先 enhanced VLAN-bundle（每 EVI 仅一条 R-T3 省路由数，P24，<<<PAGE 41>>>）；互操作需求回退 VLAN-based
4. 路由类型速查（<<<PAGE 11-13>>>）：R-T1（ES 可达，aliasing/split horizon/mass withdraw）、R-T2（MAC/IP，ARP 抑制）、R-T3（IMET，VTEP 自动发现+ingress replication 列表）、R-T4（ES 路由+DF 选举）、R-T5（IP 前缀）、R-T6（SMET 组播兴趣）、R-T7/8（多归属 IGMP 同步）
5. 主机/前缀路由分工：/32 用 R-T2、前缀用 R-T5（P12，<<<PAGE 15>>>）

## A2（操作步骤）
- **SPF 提速**（P28，<<<PAGE 50>>>）：OSPF SPF delay/hold 调 0 立即算路；BFD transmit/receive 200ms（C16，<<<PAGE 50>>>）
- **ARP 抑制保持默认开启**（P6，<<<PAGE 21>>>）：proxy ARP 代答减少 BUM；例外场景才禁用（Gratuitous ARP/ARP probe 检测主机、排障需全可见，X8，<<<PAGE 21>>>）
- **自动 RD/RT**（P22，<<<PAGE 40>>>）：RD=Loopback0+Type+Object（Service/ESI/Prefix）；RT 由 ASN+Etag(VNI) 派生
- **验证命令族**（C18，<<<PAGE 60-71>>>）：`show ip bgp neighbors` → `show service evpn` → `show service evpn ethernet-segment` → `show ip evpn proxy-arp` → `show ip routes`

## E（实证案例）
- DC spine-leaf 2-tier/3-tier（5-stage Super-Spine DCI）拓扑论证（C1/C2，<<<PAGE 8>>>）
- 全册端到端配置案例（2 spine+6 leaf）：OSPF underlay 10 步→BGP RR overlay 5 步→逐段验证（C14，<<<PAGE 48-72>>>）
- Proxy ARP 表老化后的恢复：重新发起主机通信生成表项（C19，<<<PAGE 72>>>）

## B（反例与坑）
- STP 阻塞链路浪费资源、L2 无 TTL 致环路与广播风暴、12-bit VLAN 上限（X1/X2/X3，<<<PAGE 5>>>）
- 静态首跳网关导致 traffic tromboning 绕行（X4，<<<PAGE 5>>>）
- VXLAN 洪泛学习需组播底层且持续洪泛伤扩展性（X5/X6，<<<PAGE 7>>>/<<<PAGE 9>>>）
- 广播帧走 EVI 隧道不推荐——依赖 FDB 学习与 ARP 抑制减少洪泛（X7，<<<PAGE 14>>>）
- VLAN-aware 模型多归属两端 VLAN ID 必须一致（X24，<<<PAGE 20>>>）
- 8-bit 本地段 ID 限制 ES 数量上限 256（X18，<<<PAGE 43>>>）

来源：EVPN Architecture Guide（p5-46/p48-72）
