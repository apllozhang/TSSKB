# GLOSSARY · SPB 解决方案（sol-spb）

> 页码为原书 `<<<PAGE N>>>` 标记。按基础协议/数据面标识/节点角色/服务路由/组播/自动化安全/运维分组，精选 45 条。

## 基础与协议
- **SPB（Shortest Path Bridging）**：IEEE 802.1aq 最短路径桥接，IS-IS 替代 STP 构建全链路可用的无环多路 fabric <<<PAGE 6>>>
- **SPB-M / SPBM**：SPB MAC-in-MAC 模式（802.1ah 封装）<<<PAGE 5>>>
- **SPB-V**：SPB Q-in-Q 模式 <<<PAGE 5>>>
- **IS-IS**：中间系统到中间系统链路状态协议，SPB 唯一控制面协议 <<<PAGE 6>>>
- **RFC 6329**：定义 SPB 的 IS-IS 扩展（NLPID 与一组 TLV）<<<PAGE 11>>>
- **PBB（Provider Backbone Bridging）**：IEEE 802.1ah，MAC-in-MAC 封装 <<<PAGE 5>>>
- **Q-in-Q（Provider Bridging）**：IEEE 802.1ad 双标签封装，服务实例上限 4096 <<<PAGE 6>>>
- **STP/RSTP/MSTP**：生成树协议族，靠禁用链路防环 <<<PAGE 5>>>
- **OSPF**：开放最短路径优先，VPN Lite 与部署指南外部路由所用 <<<PAGE 5>>>
- **BGP4**：边界 BEB 与外部实体（如防火墙）交换路由的常用协议 <<<PAGE 34>>>
- **VRRP**：虚拟路由冗余协议，双 BEB 网关冗余 <<<PAGE 50>>>
- **LACP / linkagg**：链路聚合控制协议/聚合链路；auto-LACP 默认开启 <<<PAGE 37>>>
- **LLDP**：链路层发现协议，Auto-VC/LACP/SPB 邻居探测基础 <<<PAGE 36>>>
- **802.1ag（CFM）**：连通性故障管理，SPB 中用于 L2 ping/L2 trace；CCM 不支持 <<<PAGE 45>>>
- **802.1AE（MACSec）**：MAC 层点到点认证与加密，硬件线速 <<<PAGE 55>>>
- **802.1x / MAC 认证**：端口接入认证，RADIUS 返回 filter-id 动态定 UNP <<<PAGE 8>>>

## 数据面与标识
- **BVLAN（B-VID）**：骨干传输 VLAN，最多 16 个，控制 BVLAN 承载 IS-IS 消息 <<<PAGE 9>>>
- **ISID（I-SID）**：24 位服务实例标识，最多 16M 租户/服务 <<<PAGE 9>>>
- **BMAC（B-SA/B-DA）**：骨干源/目的 MAC，骨干内转发唯一依据 <<<PAGE 9>>>
- **CMAC**：客户 MAC，只在 BEB 边缘学习，不进骨干 <<<PAGE 9>>>
- **ECT（Equal-Cost Tree）**：等价树，每节点每 BVLAN 一棵；ECT-ID 用于建树平局裁决 <<<PAGE 11>>>
- **FDB**：转发表；BVLAN 域 FDB 由控制面预填充 <<<PAGE 9>>>
- **同余性（Congruy）**：组播与单播走同一路径的性质；head-end 与 tandem (S,G) 具备 <<<PAGE 15>>>
- **路径对称性（Symmetry）**：X→Y 与 Y→X 路径一致，利于 OAM 单向时延推算 <<<PAGE 12>>>
- **源 ID（Source ID）**：20 位节点标识，源自 system ID 低位，tandem 复制标记 BUM 源 <<<PAGE 18>>>
- **桥优先级（Bridge Priority）**：16 位，路径计算平局裁决 <<<PAGE 18>>>
- **RPFC（Reverse-Path Forwarding Check）**：按 FDB 校验入帧源 BMAC 可达性以破瞬态环 <<<PAGE 51>>>
- **LBD（Loopback Detection）**：接入层环路检测，应启用在所有 UNI 口 <<<PAGE 51>>>

## 节点与端口角色
- **BEB（Backbone Edge Bridge）**：骨干边缘桥，封装/解封装、学 CMAC，服务与 SAP 只在其上配置 <<<PAGE 10>>>
- **BCB（Backbone Core Bridge）**：骨干核心桥，纯中转，不学 CMAC、不配服务、无需 IP <<<PAGE 10>>>
- **SAP（Service Access Point）**：UNI 侧逻辑端口，绑定物理口+流量类型到服务 <<<PAGE 14>>>
- **SDP（Service Distribution Point）**：NNI 侧逻辑端口，控制面动态创建指向远端 BEB <<<PAGE 14>>>
- **CE（Customer Edge）**：客户边缘设备，接入冗余四档模型主体 <<<PAGE 48>>>
- **L2Profile**：定义 SAP 上各 L2 控制协议 peer/drop/tunnel 处理 <<<PAGE 24>>>
- **VC（Virtual Chassis）**：虚拟机箱，多台堆叠为单逻辑设备 <<<PAGE 53>>>

## 服务与路由
- **L2 服务**：多站点单一 any-to-any 桥接域 VPN <<<PAGE 20>>>
- **L3 服务**：多站点单一 any-to-any 路由域 VPN，各站不同子网 <<<PAGE 29>>>
- **VPN Lite**：L2 SPB 服务之上叠加 OSPF/BGP/静态路由，用于边界对接外部 <<<PAGE 29>>>
- **L3 VPN**：借 IS-IS TLV 直接携带客户 VRF 路由，域内推荐 <<<PAGE 30>>>
- **VRF**：虚拟路由转发实例，租户 L3 隔离载体 <<<PAGE 29>>>
- **VLAN 翻译**：同一服务下不同 SAP 封装互通，服务级+SAP 级双开关 <<<PAGE 23>>>
- **单次直通路由**：新代 ASIC 将 IP 接口直接绑 SPB 服务，无需回环 <<<PAGE 26>>>
- **两次路由**：外部物理回环或内部前面板回环经 dummy VLAN 中转 <<<PAGE 26>>>
- **路由泄漏（Route Leaking）**：shared_services VRF 与客户 VRF 经全局表互导共享路由 <<<PAGE 34>>>
- **PBR（Policy-Based Router）**：部署指南中集中做 VRF 间策略路由的交换机角色 <<<PAGE 63>>>

## BUM 与组播
- **BUM**：广播/未知单播/组播流量统称 <<<PAGE 15>>>
- **Head-end 复制**：入端 BEB 复制多份单播，省资源费带宽 <<<PAGE 15>>>
- **Tandem (S,G) 复制**：按源-组独立组播 SPT，每链路一份副本，默认模式 <<<PAGE 15>>>
- **Tandem (*,G) 复制**：每 BVLAN 一棵共享树，根按桥优先级，不保证最短路 <<<PAGE 16>>>
- **IGMP Snooping**：组播侦听，与 head-end 复制组合可达最优 <<<PAGE 16>>>

## 自动化与安全
- **iFab（Intelligent Fabric）**：ALE 自动化特性集合统称 <<<PAGE 6>>>
- **Auto-Fabric**：出厂默认自动建网特性组（VC/RCD/LACP/SPB/MVRP/IP）<<<PAGE 36>>>
- **UNP（User Network Profile）**：用户网络画像，分类/认证规则映射到 VLAN 或服务 <<<PAGE 8>>>
- **动态 SAP / 动态服务**：按认证或 VLAN 标签即时生成 SAP 或整个 UNP+服务 <<<PAGE 38>>>
- **Base Service Number（BSN）**：动态服务 ISID 下限基数（默认 10,000,000）<<<PAGE 42>>>
- **Domain ID**：动态服务 ISID 公式的租户偏移量，保多租户隔离 <<<PAGE 42>>>
- **Service Modulo**：VLAN→服务映射取模基数，默认 512，隔离需求建议 4096 <<<PAGE 42>>>
- **微分段（Micro-segmentation）**：UNP 内 ACL/QoS 限制同 VPN 内横向流量 <<<PAGE 8>>>
- **带内管理**：管理 IP 直接挂控制 BVLAN，经 spb-mgmt 协议传路由 <<<PAGE 44>>>

## 运维
- **MEP / MIP**：802.1ag 维护端点/中间点；MIP 自动创建 <<<PAGE 45>>>
- **LBM/LBR、LTM/LTR**：L2 ping 与 L2 trace 消息/应答 <<<PAGE 46>>>
- **SAA（Service Assurance Agent）**：时延/抖动/丢包自动测试 <<<PAGE 47>>>
- **Overload 状态**：让节点退出中转的维护手段，可定时回退 <<<PAGE 48>>>
- **Graceful Restart**：主备切换保邻接保转发的平滑重启 <<<PAGE 48>>>
- **DHL（Dual-Home Link）**：无 STP/LAG 的双归属快速倒换特性 <<<PAGE 49>>>
- **链路度量（Link Metric）**：1-16M 整数，默认 10，按速率反比设置且两端同改 <<<PAGE 54>>>
- **mac-move**：重复 MAC 在同服务内反复学习/冲刷的失稳现象 <<<PAGE 52>>>
