---
name: AOS 8 骨干与 Fabric（SPBM/MPLS/VPLS/VXLAN/EVPN）
description: 需要在 OmniSwitch AOS 8 上配置 SPB/SPBM 骨干与 I-SID 服务、MPLS+LDP、VPLS/VPWS L2VPN、VXLAN 网关、EVPN over VXLAN（多归属/IRB/Clos/Multi-site）时使用。
source_book: OmniSwitch AOS Release 8.10R4 Network Configuration Guide
---

## R（触发场景）
- 园区/数据中心骨干要最短路径转发、免 STP 阻塞口：部署 SPBM
- 大二层跨机房/运营商承载：MPLS LDP + VPLS/VPWS
- 数据中心叠加网络：VXLAN 网关桥接传统 VLAN 域
- BGP EVPN 做控制面：多归属冗余、对称/非对称 IRB、Clos 或 Multi-site 部署

## I（核心理念）
SPBM 双平面框架（F4，<<<PAGE 211>>>）：控制面 ISIS-SPB（ECT 对称最短路径树+控制面 MAC 学习）+数据面 802.1ah MAC-in-MAC（BEB 封装、BCB 按 BMAP 转发）；服务模型=BVLAN 承载多 I-SID，SAP 定义接入分类。服务模型三件套（F5，<<<PAGE 212>>>/<<<PAGE 478>>>/<<<PAGE 533>>>）：SPB、VPLS、VPWS、VXLAN 共用"接入点 SAP+隧道分发点 SDP+服务实例"抽象，学会一次即可迁移到四种 VPN。EVPN 控制面框架（F6，<<<PAGE 583>>>）：MP-BGP EVPN 地址族（RT1-8）+ES/ESI 多归属（DF 选举、别名、水平分割）+VRF tenancy（非对称/对称 IRB、fabric-vpn、DAG、OISM）。EVPN 用控制面通告 MAC/IP 替代数据面泛洪学习（P101，<<<PAGE 583>>>）。

## A1（决策框架）
1. **园区骨干选 SPBM**：每桥以自己为根算 SPT，任意两点间最短路径，克服 STP 根桥次优路径（P52，<<<PAGE 214>>>）；配置必须先骨干后服务，顺序颠倒导致 ISIS 邻接异常（X25，<<<PAGE 245>>>）
2. **L2VPN 形态**：多点任意互通选 VPLS（PE 间全网格 PW+Split Horizon）；点到点选 VPWS（P92/P93，<<<PAGE 478>>>）
3. **数据中心叠加选 VXLAN+EVPN**：VTEP 由 Loopback0 IP 标识（X40，<<<PAGE 535>>>）；BUM 用 ingress replication（RT3）
4. **部署模型库（F7，<<<PAGE 654>>>）**：Clos-3/Collapsed Core/Clos-5/Multi-site/Multi-PoD，配 RR 冗余与 underlay 建议
5. **组播优化**：EVPN RT6-8/OISM 做选择性组播（见 aos-nc-multicast）

## A2（操作步骤）
- **SPBM 骨干六步（每台）**：`system name BEB-1`→`spb bvlan 4001`/`spb bvlan 4002`→`spb isis bvlan 4001 ect-id 1`（每 BVLAN 全网同 ECT）→`spb isis control-bvlan 4001`→`spb isis interface port 1/1-3`→`spb isis admin-state enable`（cases·C15，<<<PAGE 245>>>）
- **SPB 服务三步**：`service access port 1/12`→`service 1 spb isid 500 bvlan 4001 admin-state enable`→`service 1 sap port 1/12:10 admin-state enable`；SAP 封装 `:10` 匹配 CVLAN10、`:0` untagged、`:all` 全部 tagged；验证 show isis/spb service（cases·C16，<<<PAGE 245>>>）
- **SPB 伪线（E-LINE）与 RFP**：两端 SAP+伪线服务，再配 remote fault propagation 把远端故障传到接入口（cases·C17，<<<PAGE 269>>>）；IP over SPB（inline routing L3 VPN）见章内 Inter-ISID 例（cases·C18，<<<PAGE 280>>>）
- **MPLS+LDP**：`mpls enable`→载入 LDP 软件→`ldp enable`→全局定时器→接口使能 LDP→（可选）GR/session protection/MD5；验证 show mpls/ldp（cases·C28，<<<PAGE 453>>>）
- **VPWS(LDP)**：同 VPLS 流程但点到点，两端各一 SAP+SDP 绑定；验证 show vpws（cases·C30，<<<PAGE 505>>>）
- **VXLAN 网关**：Loopback0 IP（VTEP 标识）→建 VXLAN service(VNI)→配 SAP→配 SDP→服务绑定 SDP→（可选）改 UDP 端口（默认 4789）；验证 show vxlan service/sdp（cases·C31，<<<PAGE 536>>>）
- **EVPN on VXLAN**：底层 BGP(EVPN 地址族)+Loopback0→使能服务 EVPN→access 口 ES 操作→SAP→（对称 IRB）fabric-vpn 服务+路由重分发；验证 show evpn 系列（cases·C32，<<<PAGE 596>>>）
- **EVPN 多站**：边界节点 manual RT 配置+DCI 互联（cases·C33，<<<PAGE 612>>>）

## E（实证案例）
- SPBM 骨干六步+服务三步（C15/C16，<<<PAGE 245>>>）
- VXLAN 网关全流程（C31，<<<PAGE 536>>>）
- EVPN on VXLAN 对称 IRB（C32，<<<PAGE 596>>>）

## B（反例/坑）
- BCB 不学客户 MAC，排障时在核心抓不到客户 MAC 属正常（X26/P50，<<<PAGE 211>>>）
- BVLAN 不学源 MAC、不泛洪未知流量，只按 ISIS-SPB 填充的 FDB 转发；环路抑制靠严格入向源 MAC 检查（P51/P54，<<<PAGE 211, 214>>>）
- SAP `:all` 与 `:x` 同时配置时，更精确的 CVLAN 匹配优先，易误判分类结果（X27/P57，<<<PAGE 245>>>）
- 受限路径 LSP 不能跨 IGP 区域，也不能跨 AS 边界（X37，<<<PAGE 458>>>）；LSP 单向，双工需两条（P88，<<<PAGE 457>>>）
- VPLS 必须 PE 全网格 PW，漏配即部分站点不可达；Split Horizon 禁止 PW 到 PW 转发（X38，<<<PAGE 478>>>）；BGP VPLS RR 仅支持 IPv4 地址族（X39，<<<PAGE 480>>>）
- VXLAN Loopback0 未配/改动会破坏隧道；UDP 端口改了必须两端一致（X40，<<<PAGE 535>>>）；本地二层流量直接桥接不走隧道（P100，<<<PAGE 534>>>）
- EVPN 静态聚合口 ESI 不会自动生成，漏配失去多归属别名与负载分担（X41/P104，<<<PAGE 587>>>）；本地 ESI 对象上限 256 个（X42，<<<PAGE 589>>>）
- AOS 单归设备也用非零 ESI，享受控制面 FDB 管理且可与厂商互通（P105，<<<PAGE 583>>>）；RD 自动生成规则见 P107（<<<PAGE 588>>>）

## 来源
OmniSwitch AOS 8.10R4 Network Configuration Guide 第 7 章 SPBM（<<<PAGE 211-280>>>）、第 15 章 MPLS（<<<PAGE 453-461>>>）、第 16 章 L2VPN（<<<PAGE 478-505>>>）、第 17 章 VXLAN（<<<PAGE 533-536>>>）、第 18 章 EVPN（<<<PAGE 583-661>>>）。条目来源：cases C15-C18/C28/C30-C33；principles P49-P57/P87-P89/P92-P96/P100-P107；counter-examples X25-X27/X37-X42；frameworks F4-F7。
