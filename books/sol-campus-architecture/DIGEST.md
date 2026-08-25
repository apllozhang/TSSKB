# DIGEST — 园区架构指南（sol-campus-architecture）精华

本书是 ALE Mobile Campus Architecture Guide（p1-43）+ Hybrid POL 彩页（p44-47）合册（47 页）。主线：园区网四目标（可用/扩展/安全/性能）下，LAN 分层设计 + Stellar 无控制器 WLAN + NMS/安全 + POL 混合光园区的全栈设计参考。

## 一、知识地图（三技能单元）

1. **LAN/WLAN 设计**（sol-campus-lan-wlan-design）：拓扑模型、接入构件、互联与路由选型、RF 规划、分布式控制面、AP 双域发现、漫游判定、VLAN 池与 QoS（p5-32）。
2. **NMS 与安全**（sol-campus-nms-security）：OmniVista 三形态与 HA、AP onboarding、UPAM 统一接入、认证谱系、角色化策略、隔离与 wIDS/wIPS（p33-42）。
3. **Hybrid POL**（sol-campus-hybrid-pol）：POL+以太混合架构、两档推荐架构、降本模型（p44-47）。

## 二、三单元要点串讲

### 1. LAN/WLAN：分层栈与无控制器 Wi-Fi
两层折叠核心适合中小网（少部件少跳数），三层模型适合大型复杂网（<<<PAGE 7>>>）。接入层基线：VC 堆叠、VLAN 动态分配+MVRP（勿全量建 VLAN）、Trunk/LACP（<<<PAGE 8-9>>>）。互联选型：SPB 大园区扁平 L2、EVPN 跨广域 L2+多归属、MPLS 流量工程；RIP 不推荐（<<<PAGE 10-12>>>）。Stellar 无控制器三面分离：管理面集中 OmniVista、控制面分布（AP 间 NMP over-the-air/over-the-LAN）、数据面本地桥接优先按 ARP 动态切 L2GRE（<<<PAGE 15-17>>>）。AP 发现双域命令集互为镜像：VLAN 域（bridge 口+defaultWLANProfile map vlan）vs 服务域（access 口+l2profile peer+defaultWLANAccessProfile map service-type spb）（<<<PAGE 23>>>/<<<PAGE 25>>>）。漫游三分支判定：无上下文→新客户端；上下文+ARP 匹配→L2；VLAN 不匹配→L3 漫游 L2GRE 回家乡 AP（<<<PAGE 26>>>）。用户 VLAN：/24+VLAN 池首选（<<<PAGE 28>>>）。

### 2. NMS 与安全：角色化全生命周期
OmniVista 三管理模式（Express/Enterprise/Cloud）按规模递进；HA 选型：L2 HA 复用 Cluster IP 零改造，L3 HA 跨子网但 sFlow/策略执行受限、Preferred Node 走 CLI（<<<PAGE 35-36>>>）。安全框架五段：UPAM 中央认证→谱系（IoT 指纹/802.1x/访客四式/BYOD）→角色（UNP/ARP）定 VLAN+ACL+QoS→Quarantine+QMR 处置→wIDS/wIPS（干扰 AP 非威胁、流氓 AP 才遏制且默认关闭）（<<<PAGE 36-42>>>）。

### 3. Hybrid POL：光承载+以太边缘
Nokia POL 单纤点对多点+ONT 作承载，ALE 交换机/AP 作服务边缘；省铜缆/机房/有源设备/能耗四类成本，密集部署可去汇聚层（<<<PAGE 45>>>）。两档选型：需全层冗余/SPB/MACsec/高密 PoE→SFP ONT+OmniSwitch；基础特性→纯 ONT+Stellar AP（<<<PAGE 46>>>）。

## 三、本书在知识库中的位置
上游对接 campus-lan-presales（售前视角），下游细分到 stellar-wlan-* 系列（AP 部署细节）、ov2500-*（OmniVista 操作）、sol-spb/sol-evpn（互联技术深潜）。跨书易混点：Stellar 的 ARP（Access Role Profile）与 OmniSwitch 的 UNP 是同层概念两套实现；L2GRE 隧道功能类似 VXLAN 但用于 WLAN 漫游，勿与 EVPN VXLAN 混谈。

## 来源
ale_campus-architecture-guide-en.pdf（p1-43）+ ale-hybrid-pol-solution-brochure-en.pdf（p44-47）。verified.md：C1-C15；X1-X22；F1-F6；P1-P66；glossary 约 80 条。
