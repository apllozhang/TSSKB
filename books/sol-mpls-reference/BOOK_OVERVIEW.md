# BOOK_OVERVIEW — MPLS Reference Design Guide (mpls-reference-design-guide-en.pdf, 45p)

## 主旨
为 AOS 的 IP/MPLS 实现提供 fundamentals、reference design、定位与部署指南：L2VPN（VPLS/VPWS）为主线，覆盖标签结构、LDP/T-LDP/MP-BGP 控制面、数据面操作、QoS/TTL、OAM、license 与全套配置验证。首支持版本 8.9R3（OmniSwitch 6860N），8.10R2 起支持 6900。

## 骨架
1. **Why（p5-6）**：MPLS 五收益——BGP-free core、简单精确匹配查找、自愈高可用、流量工程、统一基础设施多业务。
2. **Fundamentals（p7-10）**：术语（LER/LSR/LSP/FEC/LDP）；32-bit 标签结构（20-bit Label/EXP/S-bit/TTL）；保留标签 0-15（IPv4/IPv6 Explicit NULL、Router Alert、Implicit NULL）；LIFO 标签栈（transport top + service bottom，厂商普遍支持 4-6 层）。
3. **Control Plane（p10-15）**：IGP（OSPF/IS-IS）为前提；标签分配静态或动态（LDP/RSVP/BGP/SR）；FIB=FTN+ILM；LDP 消息体系/发现（UDP 646）/会话（TCP 646）/hold-timer 协商；LDP ID；DoD vs DU、ILD vs OLD、CLR vs LLR；LDP MD5 认证；T-LDP（远端 LER 间服务标签、单播发现、抗链路故障保会话）；MP-BGP 分发服务路由+标签与自动发现。
4. **Data Plane（p16-19）**：push/swap/pop；PHP（implicit NULL 3）与 explicit NULL 保 EXP；QoS uniform/pipe 模式；TTL uniform/pipe；LDP Graceful Restart（仅计划内接管）。
5. **Service Model（p20-23）**：SAP（AC）/SDP（VC）/service tunnel/transport tunnel 双 FEC 双标签封装流程；VPLS（E-LAN、全互联 PW、split horizon、MAC 学习）与 VPWS（E-LINE、EPL/EVPL、无 MAC 学习）；OAM（LSP ping/traceroute，RFC 4379，127/8 目的、UDP 3503、TTL 递增）。
6. **Positioning（p24-25）**：园区二/三层全 MPLS；Smart City 城域网核心+汇聚 MPLS、接入以太交换。
7. **Licensing（p26）**：Debian 包安装 + Site-based（浮动最多 4 节点）/Node-based license；SILOS 服务器/SWLIC 客户端。
8. **Configuration（p26-44）**：Best Practices（/32 loopback、p2p、BFD、/31 互联地址）；LDP backbone 五步；LDP-VPLS 五步（SDP/SAP/bind-sdp）；BGP-VPLS 四步（l2vpn-vpls AF、VE-ID）；VPWS 四步（vcid、spoke bind-sdp）；验证命令族（show mpls *、show service *、show ip bgp l2vpn-vpls、show mac-learning、mpls ping/trace）。
9. **Conclusion + References（p44-45）**。

## 批判与局限
- 当前 AOS 限制多：仅 DU + ILD + LLR + MD5；explicit NULL、EXP QoS、TTL manipulation、QoS-over-EXP 均不支持；GR 仅计划内接管。
- 无 L3VPN 配置（虽 MP-BGP 提及 L3 能力）；无故障排查章节。
- 案例均为作者构造参考拓扑（R1-R7、PE1/PE2），配大量真实命令输出。

## 提取方向
principles（BGP-free core、双标签封装、split horizon、best practices 等）、cases（LDP 会话建立、VPLS/VPWS 配置流程、OAM 实测输出等）、counter-examples（implicit NULL 丢 EXP、hold-timer 超时、认证不匹配、非计划接管等）、frameworks（标签分发模式选型、VPLS vs VPWS vs 信令选型、部署定位框架）、glossary 30+。
