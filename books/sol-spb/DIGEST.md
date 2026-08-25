# DIGEST — SPB 解决方案（sol-spb）精华

本书是 ALE SPB（IEEE 802.1aq 最短路径桥接）解决方案三部曲（86 页）：架构技术白皮书（p1-56）+ 部署指南 Ed.2025（p57-82）+ 方案简报（p83-86）。核心主张：用 IS-IS 单协议控制面 + 802.1ah MAC-in-MAC 数据面取代 STP/MPLS 协议栈，全链路可用、100ms 级收敛、16M 服务实例、仅边缘供给。

## 一、知识地图（四技能单元）

1. **架构机制**（sol-spb-architecture）：双平面（DP/CP）框架、BEB/BCB 分工、BVLAN/ECT 建树、BUM 三模式、RPFC/LBD 防环（p5-18/p48-54）。
2. **L2/L3 服务**（sol-spb-l2-l3-services）：Service→ISID→BVLAN 三层标识、SAP/VLAN 翻译/L2Profile、两代 ASIC 路由形态、L3 VPN vs VPN Lite、路由泄漏（p20-35）。
3. **部署流程**（sol-spb-deployment-flow）：11 步落地清单、VRF+VRRP+PBR+OSPF 全套、S-Hook 混合域对接、iFab 自动化与动态服务公式（p36-43/p57-82）。
4. **定位与案例**（sol-spb-positioning-cases）：四大价值主张、三场景、七行业用例、NDOT/IDC Frontier/UTS 证言（p83-86）。

## 二、四单元要点串讲

### 1. 架构：为什么 SPB 能取代 STP
STP 三宗罪：禁链路费带宽、非根间绕次优路径、秒级收敛且瞬态成环（<<<PAGE 5>>>）。SPB 由 IS-IS 跑 Dijkstra，每节点以自己为根建树，"no network link is disabled, all paths are available"（<<<PAGE 7>>>）。数据面只查 FDB（BVLAN 域 FDB 由控制面预填充，不泛洪学习）；骨干内只按 BMAC 转发，CMAC 只在 BEB 学（<<<PAGE 9>>>）。每节点每 BVLAN 一棵 SPF 树，ECT-ID 打破平局（<<<PAGE 11-12>>>）。BUM 三模式选型（<<<PAGE 16>>>）：head-end 省资源费带宽、tandem (S,G) 默认、tandem (*,G) 共享树不走最短路。防环双机制：预防（ECT 树）+缓解（RPFC 按对称性校验源 BMAC，<<<PAGE 51>>>）。

### 2. 服务：三层标识与 L2/L3 分档
Service（本地）→ISID（全局 24 位）→BVLAN（承载）；SAP 是 UNI 侧虚拟端口，SDP 动态生成；服务只在 BEB 配、BCB 零感知（<<<PAGE 13>>>）。L2 服务三步：`service N spb isid X bvlan Y`+SAP（<<<PAGE 20>>>）。L3 两档：域内 L3 VPN（IS-IS TLV 直传 VRF 路由，单协议）；边界 VPN Lite（叠 OSPF，4 服务×8 BEB=64 个 OSPF 配置的爆炸是其代价，<<<PAGE 34>>>）。共享服务走 VRF 路由泄漏，前提地址不重叠。两代 ASIC：新代单次直通路由，老代需外部/内部回环经 dummy VLAN（<<<PAGE 26>>>）。

### 3. 部署：11 步与自动化
参考架构 2×BCB 全网格+N×BEB 双归 LAG+PBR（<<<PAGE 63>>>）。11 步：拓扑/LAG→VLAN→LBD→BVLAN→服务→SAP→VRF→VRRP→/30 连 PBR→VRRP tracking→OSPF→策略（<<<PAGE 62>>>）。VRRP 虚地址统一 .1、末位=BEB 号；上行断优先级 120−25=95 触发切换（<<<PAGE 74>>>/<<<PAGE 78>>>）。混代场景 S-Hook：VLAN 域 LAG 与服务域 LAG 挂接（<<<PAGE 81>>>）。iFab 自动化：Auto-VC/RCD/LACP/SPB/MVRP/IP 六阶段+动态服务（ISID=BSN+Domain ID+VLAN%Modulo，默认 BSN 10,000,000；Modulo 隔离需求从 512 调 4096，<<<PAGE 42-43>>>）。

### 4. 定位：卖点与案例
收敛 2-3s→100ms；对标 MPLS 话术=单协议 vs 协议栈（<<<PAGE 83>>>）。四大价值：可扩展/安全（ZTNA 构件）/简单/可靠（<<<PAGE 84>>>）。三场景：园区 STP 替代、DC any-to-any+私有云、MAN 对标 MPLS。七行业用例（<<<PAGE 85>>>）；NDOT（可扩展+快速上线）、IDC Frontier（扩展性+SLA 弹性）证言（<<<PAGE 86>>>）。

## 三、本书在知识库中的位置
与 os-lan-spb-impl（配置实现细节）、spb-presales（售前材料）互补：本书是"架构原理+官方部署流程+价值主张"的一手来源。跨书易混点：tandem (S,G) 为默认 BUM 模式（按服务选择），tandem (*,G) 按 BVLAN 选择且不保证最短路；EVPN 书的 ingress replication 对应本书 head-end 复制思路但机制不同（BGP vs IS-IS）。

## 来源
SPB 三文档（Tech Brief + Deployment Guide Ed.2025 + Solution Brief，共 86 页）。verified.md：C1-C28；X1-X30；F1-F6；P1-P60；glossary 约 80 条。注：DOC3（p83-86）内容未入 verified.md，页码取自 fulltext.md 原文标记。
