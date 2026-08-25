# DIGEST — MPLS Reference Design Guide 精华

本书是 AOS 的 IP/MPLS 参考设计指南（45 页，首支持 8.9R3/OmniSwitch 6860N，8.10R2 起支持 6900）。主线为 L2VPN（VPLS/VPWS）：从标签基础、LDP/T-LDP/MP-BGP 控制面、数据面操作、QoS/TTL 透明性、OAM，到 license 与全套配置验证。定位覆盖园区端到端与城域核心+汇聚两种形态。

## 一、知识地图（三技能单元）

1. **MPLS 基础体系**（sol-mpls-foundation）：32 位标签结构、双标签封装、LDP 发现/会话/模式（DU+ILD+LLR）、PHP、MD5 认证、AOS 支持边界（p5-17、p24-33）。
2. **L2VPN 业务**（sol-mpls-vpls-vpws）：VPLS/VPWS（EPL/EVPL）、SAP/SDP 服务模型、T-LDP vs BGP 信令、五步/四步配置（p15-22、p33-42）。
3. **QoS 与 OAM**（sol-mpls-qos-oam）：EXP uniform/pipe、TTL 透明性、PHP 与 explicit NULL 的 EXP 保留、LSP ping/traceroute、AOS 不支持清单（p16-19、p23-24、p44）。

## 二、三单元要点串讲

### 1. 基础：标签隧道换 BGP-free core
MPLS 用预分配标签做精确匹配转发，核心不承载大量路由（<<<PAGE 5>>>）。shim 标签 32 位（20-bit Label/EXP/S/TTL），Layer 2.5 协议（<<<PAGE 9>>>）。VPN 双层栈：transport 在顶、service 在底，中间 LSR 只看传输标签（<<<PAGE 10-21>>>）。LDP 依 IGP 而生：UDP 646 组播 hello 发现 → TCP 646 会话 → Initialization 协商；可靠性靠 hello/keepalive 双定时器（<<<PAGE 12>>>）。AOS 唯一支持 DU+ILD+LLR+MD5（<<<PAGE 13-17>>>）。部署前提：/32 loopback 唯一 Router-ID + p2p + BFD + /31 互联（<<<PAGE 28>>>）。

### 2. 业务：服务与传输解耦
服务只在有站点的 LER 创建：SAP 面向 CE、SDP 面向远端（<<<PAGE 20>>>）。VPLS（E-LAN）需全互联 PW + per-VPLS MAC 学习，防环靠 split horizon（PW 进 PW 出禁止）；VPWS（E-LINE）点对点透明转发不学 MAC，分 EPL/EVPL（C-VLAN 复用）（<<<PAGE 21-22>>>）。信令二选一：T-LDP 手工 SDP（抗链路故障保会话）或 MP-BGP l2vpn-vpls（自动发现+信令一体，单 AS 需 full-mesh 或 RR）。配置五步（LDP-VPLS）/四步（BGP-VPLS、VPWS）见 <<<PAGE 33-42>>>。

### 3. QoS/OAM：透明性选型与数据面验证
只有顶层标签的 EXP/TTL 被处理（<<<PAGE 18-19>>>）。uniform 客户标记穿透、pipe 运营商自定；TTL pipe 模式下 L3VPN 两端各减 1、L2VPN 完全不变。PHP 用 implicit NULL 省 eLER 查表但丢 EXP；explicit NULL 可保 EXP 但 AOS 不支持。数据面验证用 `mpls ping/trace ldp`（RFC 4379，127/8 目的、UDP 3503），控制面正常仍可测出转发故障（<<<PAGE 23-24、44>>>）。GR 仅保计划内接管（<<<PAGE 19>>>）。

## 三、本书在知识库中的位置
与 os-lan-mpls-impl（实现手册）、os-lan-spb-impl / sol-spb（SPM/SPB 替代路线）、os-lan-vxlan-evpn（数据中心 overlay）构成 ALE 二三层隧道全家桶。本书的独特价值是"为什么"与选型框架（五收益、F1-F5），以及明确的 AOS 能力边界清单。跨书易混点：explicit NULL、QoS over EXP、TTL manipulation 在 AOS 均不支持，规划时勿照搬通用 MPLS 教材。

## 来源
MPLS Reference Design Guide（mpls-reference-design-guide-en.pdf，45p）。verified.md：cases C1-C18；principles P1-P33；counter-examples X1-X18；frameworks F1-F5；glossary 48 条。
