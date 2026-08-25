# frameworks — sol-mpls-reference（决策框架 / 思维模型）

## F1 标签分发/控制/保留模式选型框架
三组正交决策：分发方式（DoD 按需 vs DU 主动）、控制模式（ILD 独立即刻通告 vs OLD 有序等下游标签）、保留模式（CLR 只留有效下一跳 vs LLR 全保留）。用途：解释/规划 LDP 行为与收敛特性；AOS 支持态为 DU+ILD+LLR。
- 引用："An LSR can use different modes to distribute label bindings to LDP neighbors... There are also two modes of control for label creation... There is also retention modes..." <<<PAGE 13-14>>>

## F2 L2VPN 服务选型框架（VPLS vs VPWS × EPL vs EVPL × 信令 LDP vs BGP）
决策链：连通需求（E-LAN 多点 vs E-LINE 点对点）→ VPLS 需全互联 PW + MAC 学习，VPWS 透明转发不学 MAC → VPWS 再分 EPL（整端口）/EVPL（按 C-VLAN 复用多条 PW）→ 信令选 T-LDP（手工 SDP/far-end）或 MP-BGP l2vpn-vpls（自动发现+信令一体，单 AS 需 full-mesh 或 RR）。
- 引用："The method of establishing VPLS with BGP accomplishes both auto-discovery and signaling." <<<PAGE 21>>>；"MEF 6.3 defines two types of P2P Ethernet VPWS services - EPL and EVPL." <<<PAGE 22>>>

## F3 MPLS 部署定位框架（园区 vs 城域）
决策变量：网络层级覆盖范围。园区中小型网：IP/MPLS 从接入到核心端到端；城域/Smart City：核心+汇聚跑 MPLS，接入层保持标准以太交换。共同前提：先 IGP 底层 + /32 loopback 唯一 Router-ID。
- 引用："For metro ethernet networks such as smart city networks, IP/MPLS network can be configured at the core and distribution layers of a three-tier network architecture." <<<PAGE 24-25>>>

## F4 双层标签服务模型框架（transport × service 二层解耦）
封装模型：服务只在 LER 存在（SAP/AC 面向 CE，SDP/VC 面向远端）；transport LSP（FEC=loopback）+ service tunnel（FEC=service id）标签栈叠加；传输隧道可换承载（LDP/RSVP-TE/静态）而不动服务层。用途：故障域隔离与排错分层（transport 层用 show mpls *，service 层用 show service *，OAM 用 mpls ping/trace）。
- 引用："There are two FECs associated with providing VPN services. One FEC for the service tunnel, which is the service identifier, and another is for the transport tunnel, which is the loopback interface for each LSR." <<<PAGE 20>>>

## F5 QoS/TTL 透明性选型框架（uniform vs pipe）
决策变量：是否让客户标记穿透运营商域。QoS：uniform 客户 DSCP 复制到 EXP 再回写；pipe 运营商自定 EXP、客户 DSCP 不动。TTL：uniform 复制 IP TTL 逐跳递减（traceroute 可见骨干）；pipe IP TTL 不变（L3VPN 仅两端各减 1、L2VPN 完全不变）。
- 引用："In uniform mode, the IP precedence value... is copied to the EXP bits... In pipe mode, the EXP value is set according to the Service Provider's policy and is independent of the customer's QoS markings." <<<PAGE 18>>>
