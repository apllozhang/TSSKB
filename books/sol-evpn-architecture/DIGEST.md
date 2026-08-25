# DIGEST — EVPN Architecture Guide（sol-evpn-architecture）精华

本书是 AOS 8.10R1-R3 在 OmniSwitch 6900 上的 MP-BGP EVPN for VXLAN 架构指南（73 页）：fundamentals（p9-40）+ AOS 差异化（p40-44）+ 参考设计（p44-48）+ 端到端配置案例（p48-72）四位一体。核心主张：控制平面主动学习取代洪泛学习，单一 BGP EVPN 控制面同时承载 L2/L3 服务。

## 一、知识地图（三技能单元）

1. **控制面**（sol-evpn-control-plane）：Why 论证、VXLAN/VNI/VTEP、R-T1~R-T8、RD/RT 自动派生、service 模型、ARP 抑制、underlay/overlay 设计（p5-46）。
2. **Multi-homing 五机制**（sol-evpn-multi-homing）：模式选型、ESI、DF/service carving、split horizon/local bias、aliasing、mass withdraw、组播状态同步（p32-44/p64-66）。
3. **IRB 与组播**（sol-evpn-irb-multicast）：对称/非对称 IRB、SBD(Fabric-VPN)、DAG、OISM/PEG、border leaf 外部连通（p23-31/p37-48）。

## 二、三单元要点串讲

### 1. 控制面：从洪泛学习到 NLRI 通告
传统模型五大痛点（STP 阻塞链路/L2 无 TTL 成环/4096 上限/运维复杂/tromboning，<<<PAGE 5>>>）逐项映射到 VXLAN（24-bit VNI 约 1600 万）与 EVPN（MP-BGP NLRI 智能通告可达性，<<<PAGE 7>>>）。控制面学的 MAC 不老化（<<<PAGE 13>>>）；ARP 抑制默认开、proxy ARP 代答减 BUM（<<<PAGE 20-21>>>）。路由类型分工：R-T1 ES 可达、R-T2 MAC/IP、R-T3 IMET 自动发现+ingress replication、R-T4 ES+DF 选举、R-T5 前缀、R-T6 SMET、R-T7/8 IGMP 同步（<<<PAGE 11-13>>>）。推荐设计：单区域 OSPF p2p+BFD underlay+iBGP overlay+冗余 RR（同 cluster-id）+TTL security 0（<<<PAGE 45-46>>>）。

### 2. Multi-homing：防环防重复五机制
LAG 是前提（<<<PAGE 32>>>）；DF=EVI mod N 的 service carving 按 EVI 分散 BUM 负载（<<<PAGE 33>>>）；split horizon（VXLAN 下靠对端 PE IP 列表）+ local bias（本 PE 的 BUM 只从本地 ES 出）防环（<<<PAGE 34>>>）；aliasing 让远端按流负载分担到全活 ES（<<<PAGE 34>>>）；mass withdraw 一条 ESI 撤路批量刷新 MAC（<<<PAGE 36>>>）。ESI 三档：物理口/LACP LAG 自动、静态 LAG 手工 5 字节（<<<PAGE 41>>>）。坑：多归属 SAP 不一致黑洞（<<<PAGE 66>>>）、DF change 丢包需 SMET 补救（<<<PAGE 36>>>）。

### 3. IRB 与组播：对称 IRB+DAG 是主干
对称 IRB 配置简扩展好为主流推荐，每 PE 只维护本地 ARP/MAC-VRF，每 VRF 一个 Fabric-VPN(SBD) 提供跨 EVI 可达（<<<PAGE 24-25>>>）。DAG 同一 anycast IP+MAC（每 VRF 一 VMAC，自动派生 00:00:5e:00:01:VRF-ID），免 VRRP、同 PE 流量不过 fabric（<<<PAGE 28-29>>>）。组播：AOS 仅 ingress replication；跨子网用 OISM（RFC 9625，Fabric-VPN+R-T6，8.10R3 EA），源发现选 R-T10 省带宽；外部 PIM 互通走 PEG（双 PEG 冗余+专用 L3 互联，<<<PAGE 37-39>>>）。外部连通：border leaf+GRM，对外只放聚合路由，双 leaf 调 import 优先级防回声（<<<PAGE 46-48>>>）。

## 三、本书在知识库中的位置
与 os-lan-vxlan-evpn（配置实现）、sol-spb（另一条 L2 fabric 路线）构成三角：EVPN=数据中心/跨广域 L2 的事实标准路线，SPB=园区/MAN 单协议路线。跨书易混点：SPB 用 IS-IS 传服务成员，EVPN 用 BGP NLRI；SPB head-end 复制对应 EVPN ingress replication 但发现机制不同（LLDP/IS-IS vs R-T3）。版本强绑定 8.10R1-R3、OmniSwitch 6900；OISM/PEG 为 EA 特性。

## 来源
evpn-architecture-guide-en.pdf（73 页）。verified.md：C1-C20；X1-X24；F1-F5；P1-P42；glossary 约 70 条。
