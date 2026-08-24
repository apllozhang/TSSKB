# DIGEST · 一篇读透 AOS MPLS 实施（不读全书版）

> 教材：ALE《OmniSwitch LAN MPLS Concepts & Implementation》（DT00XTE324EN，153 页）
> 本文是全书精华的读者向浓缩，数字均带页码，可直接回查原书。

## 一、一页看懂 AOS MPLS

**什么时候在 OmniSwitch 上用 MPLS？** 两个典型场景（p133-134）：一是中小园区，二/三层架构里 IP/MPLS 从接入直达核心，端到端跑 VPN 业务；二是城域以太（智能城市类项目），三层架构中 MPLS 域收敛到核心+汇聚，接入层保持标准以太交换。定位是"面向企业与城域客户的高性价比方案"。

**和 SPB/EVPN 的分工：** 教材口径很直接——AOS 的 IP/MPLS 首版只覆盖 L2 VPN（VPLS），L3 VPN（VPRN）不在本册（BOOK_OVERVIEW 批判部分）；需要二层多点互通、且已有 OSPF underlay 的网络，VPLS 是可选项。纯园区新建二层扁平化需求，SPB/EVPN 仍是主线；MPLS 更适合城域/多业务分域的场景。

**硬性准入（p59, p118）：** AOS ≥ 8.9R3，平台仅 OmniSwitch 6860N。MPLS 是独立 Debian 包（uosn-mpls-v1.deb），装在 /flash/working/pkg 后用 pkgmgr 安装——只装包不够，LDP/BGP 还要分别 `mpls load ldp` / `ip load bgp` 才加载。

## 二、部署十步主线（p58-70）

顺序固定，不可乱序：

1. 全网装 MPLS 包：`pkgmgr install uosn-mpls-v1.deb`
2. 创建互联 VLAN 与 IP 接口（Lab 中 VLAN 70/79/80/89/90，mtu-ip 4094，p83-96）
3. 配 OSPF underlay，**每台必配 Loopback0**——OmniSwitch 特有：Loopback0 即系统 IP，兼作 LSR ID，全网必须唯一，否则"行为不可预测"（p125 原文加粗）
4. 安装许可（SILOS 服务器 + SWLIC 客户端）：状态为 permanent 或未过期 demo 才使能；无效时 MPLS 被**临时禁用**——配置还在但功能停摆，排障入口是 `sh license-info` 而非查配置（p92）
5. `mpls load ldp` + 全局/接口两级使能
6. 建 VPLS 服务（7-9 步：SDP → bind-sdp → SAP，见下节）
10. 验证 + `write memory flash-synchro` 备份

许可两类（p118 附近）：站点许可浮动共享，1 份最多覆盖 4 节点（1 节点可以是 8 台以内虚拟机箱）；节点许可绑单个 MPLS 节点。客户超 4 台就得加买或改节点许可。

## 三、VPLS 双信令选型：LDP vs BGP

| 维度 | LDP 信令（T-LDP） | BGP 信令 |
|---|---|---|
| 自动发现 | 无，手工 SDP 互指 | 有，"无需逐台配远端"（p72） |
| 伪线数量 | n 台 PE 要 n(n-1)/2 条，新站点要改所有旧站点 | IBGP 邻居也须全互联（AOS 无 RR，p132-133） |
| 扩容 | 改全部旧站点 | 只加邻居 |
| 适用 | 3-4 站点以内、省 BGP 运维 | 多站点、持续扩容 |

**LDP 配置骨架**（两端对称，p97-105）：

```
service 2 vpls vplsid 200 signaling ldp admin-state enable
service sdp 78 vpls far-end 192.168.254.8
service 2 bind-sdp 78
service access port 1/1/3
service 2 sap port 1/1/3:2
```

**BGP 配置骨架**（每台 PE，p74, p110）：

```
ip load bgp
ip bgp autonomous-system 65724
ip bgp address-family l2vpn-vpls
ip bgp neighbor <对端loopback> remote-as 65724
ip bgp neighbor <对端loopback> update-source Loopback0
ip bgp neighbor <对端loopback> activate l2vpn-vpls
ip bgp admin-state enable
service 2 vpls vplsid 200 signaling bgp ve-id 1 admin-state enable
```

三个坑：ve-id 每台 PE 必须唯一（Lab 中 sw7=1、sw8=2）；每个邻居都要单独 `activate l2vpn-vpls`，漏一条该邻居不传 VPLS 路由；SAP 配 `:0`（untagged）时出口永远 untagged，对端要 tagged 就单通，靠两级 vlan-xlation 对齐（p78 附近案例）。参考设计的 BGP 模板还多一条 `ip bgp mpls` 全局命令，Lab 3 里没有——照抄规范模板时别漏（p138-139）。

## 四、参考设计两场景要点（p133-146）

**园区模板：** 端到端 MPLS（接入到核心），二/三层架构。

**城域模板：** 三层架构，MPLS 只到核心+汇聚，接入层标准以太交换。

**最佳实践七条（p136）：** OSPF/IS-IS underlay；每台 /32 loopback 进 IGP 且兼 Router-ID；IGP 网络类型 point-to-point；用路由接口（`rtr-port tagged`）；启用 BFD（注意是全局 `ip bfd admin-state enable` + OSPF 接口 `bfd-state enable` 两级，只配一边不生效）；P2P 链路用 /31（教材示例为可读性用 /24，交付按 /31）。

**配置落地铁律：** service/sap/sdp 只配在 PE/LER 上，P 节点零 service 配置（Lab 中 P 节点 sw9/sw10 的 mac-learning 表为空即直接证据）。

## 五、验证命令手册（按层次下钻，p139-145）

1. 包/许可：`show pkgmgr`、`show license-server usage/info`、`sh license-info`
2. MPLS 全局：`show mpls`
3. 标签表：`show mpls ftn-table`（入向 PUSH）、`show mpls ilm-table`（入标签 SWAP/POP）、`show mpls forwarding-table`（Out-Label=3 即直连+PHP，属正常）
4. LDP：`show mpls ldp session`（双邻居 OPERATIONAL，模式默认 DU+ILD+LLR）、`show mpls ldp neighbor`（LDP ID 为 loopback:0 即 per-platform）
5. 业务：`show mpls vpls-mesh`、`show service vpls|sdp|bind-sdp`
6. BGP：`show ip bgp neighbors`（established + L2VPN vpls enabled）、`show ip bgp l2vpn-vpls path`（含 VE-ID/LabelBase）
7. MAC：`show mac-learning domain vpls`——应同时看到 `sap:`（本端）与 `sdp:`（远端）接口的 MAC

## 六、AOS 能力边界：六项不支持（售前禁引核对，p127-133）

| 不支持 | 影响 | 替代 |
|---|---|---|
| RSVP-TE | 无流量工程/带宽预留 | 只能 LDP 隧道走 IGP 最优路径 |
| 显式 NULL | PHP 时 EXP 无法保留 | 无直接替代 |
| QoS over EXP | EXP 不承载 QoS | QoS 落 IP DSCP |
| MPLS TTL 操作 | traceroute 暴露骨干跳数 | 无 |
| VPWS | 无点对点二层专线 | 两点 VPLS 模拟 E-Pipe |
| BGP VPLS 的 RR | 邻居不能收敛到反射器 | IBGP 全互联 |

用法：任何方案/标书引用 MPLS 特性，先逐条过这张表；命中硬需求要么换方案要么确认 AOS 后续版本（p118 预告"后续版本可能补充"）。注意这是 8.9R3 首版清单，实际项目要在目标版本上用 `show mpls` 复核，别把"首版不支持"当永久结论。

---

**一句话收束：** 准入（8.9R3/6860N/许可）→ 十步部署（Loopback0 唯一是底线）→ 信令选型（小网 LDP、大网 BGP 全互联）→ 模板交付（业务只配 LER）→ 命令族谱分层验证 → 售前先过六项禁引清单。

*由 cangjie-skill 流水线从 DT00XTE324EN 蒸馏生成。*
