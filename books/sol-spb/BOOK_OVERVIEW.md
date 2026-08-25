# BOOK_OVERVIEW — sol-spb（SPB 解决方案，86 页）

## 书目构成（页码全册连续）

| 子文档 | 页码范围 | 内容 |
|---|---|---|
| DOC 1 spb-architecture-tech-brief-en.pdf（Tech Brief） | p1–56 | SPB 架构指南：问题引入、数据面/控制面、服务框架、BUM、L2/L3 服务、自动化、管理、OAM、冗余、设计准则、安全 |
| DOC 2 spb-deployment-guide-en.pdf（部署指南，Ed. 2025） | p57–82 | 中型企业落地全流程：拓扑/命名/地址规划 → VLAN/LBD/BVLAN/服务/SAP → VRF/VRRP/OSPF/策略，附 S-Hook 替代配置 |
| DOC 3 spb-solution-brief-en.pdf（方案简报） | p83–86 | 价值主张（可扩展/安全/简单/可靠）、三大场景（园区/数据中心/MAN）、行业用例与客户案例 |

## 核心主线

1. **为什么替代 STP**（p5–6）：STP 禁用链路、次优路径、秒级收敛；以太网泛洪学习与扁平地址空间限制扩展性；Q-in-Q 上限 4096 服务实例。
2. **SPB 本质**（p6–9）：IS-IS 单协议控制面 + 802.1ah MAC-in-MAC 数据面；多租户（24 位 ISID，16M 服务）；动态服务实例化；仅边缘供给；微分段（UNP/ACL）；非 IP 核心。
3. **机制细节**（p9–16）：BEB/BCB、BVLAN/ISID/BMAC、ECT 等价树、路径对称性与确定性、SAP/SDP 虚拟端口、三种 BUM 复制模式（head-end / tandem (S,G) / tandem (*,G)）。
4. **配置路径**（p16–35）：建骨干（BVLAN+ECT+IS-IS 接口）→ L2 服务（service+ISID+BVLAN+SAP）→ 路由概念（两代 ASIC 的单次/两次路由）→ L3 服务（VPN Lite vs L3 VPN）→ 共享服务与路由泄漏。
5. **自动化**（p36–43）：iFab（Auto-VC/RCD/LACP/SPB/MVRP/IP）、动态 SAP（UNP+802.1x/MAC 认证）、动态服务（ISID/BSN/Domain ID 公式）。
6. **运维与设计准则**（p43–56）：带内管理、802.1ag OAM、SAA、overload/graceful restart、CE 接入冗余四档、RPFC/LBD/风暴控制、BVLAN 数量=等价路径数、VLAN→Service 一对一映射、VC/LAG/链路度量/QoS、管理 VRF/MACSec/NAC/路由认证。
7. **部署指南实践**（p57–82）：2 BCB + 4 BEB 样例；命名规范（ACC-31、linkagg 13）；VRF+VRRP+PBR+OSPF 全套命令；Guest 拒绝策略示例；S-Hook 替代配置。
8. **方案简报**（p83–86）：收敛 2-3s→100ms；三大落地场景；7 个行业用例；NDOT/IDC Frontier/UTS 客户证言。

## 候选提取状态

- principles.md：P1…（目标 35–50 条）
- cases.md：C1…（部署/配置流程，目标 15–25 条）
- counter-examples.md：X1…（英文原句，目标 15–25 条）
- frameworks.md：F1…（目标 3–6 条）
- glossary.md：按主题分组（目标 40–60 条）
