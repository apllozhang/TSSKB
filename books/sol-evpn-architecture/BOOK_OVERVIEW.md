# BOOK_OVERVIEW — EVPN Architecture Guide (evpn-architecture-guide-en.pdf, 73p)

## 主旨
为 AOS（Alcatel-Lucent Operating Software）8.10R1/R2/R3 在 OmniSwitch 6900 上的 MP-BGP EVPN for VXLAN 提供 fundamentals、reference design 与 deployment guidelines 三位一体的架构指南。

## 骨架（Adler 结构四步）
1. **Why（p5-8）**：传统 STP + VLAN 模型的五大痛点（资源低效、稳定性、4096 VLAN 上限、运维复杂度、traffic tromboning）→ VXLAN 数据面 → 洪泛学习不足 → 需要智能控制平面（EVPN）。
2. **Fundamentals（p9-40）**：EVPN 术语（EVI/BD/ES/ESI/ETag/MAC-VRF/IP-VRF）；控制平面（AFI 25 / SAFI 70）；8 种 Route-Types（R-T1 A-D、R-T2 MAC/IP、R-T3 IMET、R-T4 ES、R-T5 IP Prefix、R-T6 SMET、R-T7/8 IGMP 同步）；RD/RT；三种 service interface model；ARP suppression / proxy ARP；扩展社区（ES-Import、ESI Label、Tunnel Encap、MAC mobility、Default Gateway、DF Election、Router MAC）；IRB（对称/非对称、host-based/prefix-based、三种 RFC 9136 模型）；DAG；数据面（BUM 的 ingress replication、bridging、routing 步骤级 walk-through）；multi-homing（DF election/service carving、split horizon、local bias、aliasing、backup path、mass withdraw）；multicast 优化（OISM、PEG）；MAC/IP mobility（duplicate-MAC hold-down、DAD）；silent hosts。
3. **AOS Differentiators（p40-44）**：自动 ESI 生成（Type 0x3）、Enhanced VLAN-bundle service interface（ALE 定义）、自动 RD/RT 编码（Loopback + Object Type/ID）、SMET by all PEs。
4. **Design（p44-48）**：spine-leaf 拓扑、OSPF underlay + iBGP overlay（RR 冗余、TTL security）、external connectivity（border leaf + GRM、路由汇总、防 echo）。
5. **Configuration Example（p48-72）**：6 leaf + 2 spine 全套配置（OSPF/BFD/BGP RR/LAG/Fabric-VPN/service/SAP/IRB/DAG/OSPF 外部路由/proxy ARP），每步配 verification 命令。
6. **Conclusion + References（p72-73）**：EVPN 为 DC/campus/DCI 事实标准；ALE VC/UNP 等生态。

## 关键术语群
VXLAN/VNI/VTEP/VTI；EVI/BD/ES/ESI/ETag；R-T1~R-T8；RD/RT；对称/非对称 IRB、SBD(Fabric-VPN)、L3EVI；DAG(anycast IP/MAC)；DF/service carving/split horizon/local bias/aliasing；ARP suppression/proxy ARP；OISM/IPMS/PEG/SMET；MAC mobility/DAD/sticky MAC。

## 批判与局限
- 版本强绑定（8.10R1-R3、OmniSwitch 6900），部分特性 EA（OISM、PEG）；VLAN-aware bundle、tandem replication 等未支持。
- 只覆盖"most common, validated and recommended architectures"，非全选项手册。
- 无故障排查章节，验证命令限于部署后状态确认。
- 案例均为作者构造的参考拓扑（非客户实战案例），但含大量"作者亲自使用"的配置-验证流程。

## 提取方向
- principles：BUM 抑制、控制面学习、DF/split horizon 规则、RR/underlay 最佳实践、DAG 原则、路由汇总等。
- cases：intra-subnet/inter-subnet 报文 walk-through、DF change 场景、DAD 场景、配置实例各段。
- counter-examples：STP/VLAN 痛点、proxy ARP 禁用场景、DF change 丢包、路由 echo、SAP 配置不一致黑洞、(*,*) SBD-SMET 带宽浪费等。
- frameworks：underlay/overlay 设计决策框架、IRB 模型选型框架、BUM 复制方式选型、multi-homing 模式选型、外部连通性设计框架。
- glossary：40+ 术语，全部带真实页码。
