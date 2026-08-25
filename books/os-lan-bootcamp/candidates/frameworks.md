# OmniSwitch R6/R8 Bootcamp Issue 25 — 体系框架候选（frameworks）

- **F1 五天课程主线**：Day1 硬件+系统管理+堆叠/VC+诊断 → Day2 VLAN/LACP/STP/DHL/IP/LLDP → Day3 VRRP/QoS/ACL/AG/IoT/PoE → Day4 RIP/OSPF/GR/AOS 安全/VRF → Day5 组播/ERP/IFAB。页码：议程 Day1-5 逐日排列 <<<PAGE 8-13>>>；扩展模块（SLB/BGP/ERP/VRF/PIM）补充议程 <<<PAGE 13>>>
- **F2 OmniSwitch 产品组合分层框架**：按 Size（Small/Medium/Large/Hardened）×能力（Value L2+ / L2+ Basic L3 / Advanced L3）把 6350/6465/6560/6860(E)/6865/6900/9900 放入同一矩阵。原句："Positioning in the Stackable portfolio… Small/Medium/Hardened/Large" <<<PAGE 23, 30, 41, 51>>>
- **F3 速率-层级演进图**：接入 100M→1G→2.5G、汇聚 1G→2.5G→10G、核心 10G→25G→40G→100G 对应机型升级路径。原句："100M->1G->2,5G / 1G->2,5G>10G / 10G->25G->40G->100G" <<<PAGE 21>>>
- **F4 AOS Flash 目录框架**：Flash = working + certified（+R8 用户自定义目录）+network/switch/boot.params/swlog；双目录互为回滚。原句："Working Directory / Certified Directory / Flash Directory" <<<PAGE 126-127, 145>>>
- **F5 Auto-fabric 零接触部署体系（七步）**：Auto-VC → RCL 远程配置 → Auto-LACP → Auto-Routing → Auto-SPB Fabric → Auto-Network Profiling → Auto-MVRP；失败即删除并禁用配置。原句："AUTO-FABRIC PLUG-N-PLAY ZERO TOUCH DEPLOYMENT" <<<PAGE 155, 936>>>
- **F6 ACFE 认证双轨框架**：Newcomer Track（从零到 ACFE/ACSE）与 Experienced Track（续证两年）。原句："Newcomer Track… Experienced Track" <<<PAGE 3-4>>>
- **F7 STP 协议/模式矩阵**：协议 802.1D/802.1w(默认)/802.1s/ERPv2 × 模式 flat/1x1(per-VLAN 默认)。原句："Spanning Tree Protocols supported… Spanning Tree Operating Modes supported" <<<PAGE 415>>>
- **F8 QoS 分层模型（R8）**：QSet（每口 8 单播+4 组播队列）→ QSI 实例 → QSet Profile（8SP / 1EF+7SP / 1EF+7WFQ）→ 分类引擎（L2-L4 条件）→ 策略三元组（condition/action/rule）。原句："Queue Set (Qset) framework / Packet Classification… POLICY CONDITION… POLICY ACTION" <<<PAGE 544-552>>>
- **F9 AOS 安全体系（Consistent AOS Network Security）**：LLDP Rogue Detection、LPS、PBR、高级 ACL 组（UserPorts/DropServices/port-disable）、BPDU Guard、DOS Protection、ARP Poisoning、MACsec、DHCP Snooping+Option82、Port Mapping、Storm Control、OmniVista 安全应用。原句："Use the Advanced AOS Security mechanisms in order to protect the core network as well as data" <<<PAGE 799>>>
- **F10 Access Guardian/UNP 分类模型**：认证（802.1X/MAC/无）→ RADIUS Filter-ID 下发 UNP → 失败降级链（分类规则/默认 UNP/Captive Portal/阻断）→ UNP = VLAN+QoS/ACL 策略列表+Location+Period；R8 端口 16 级分类优先序。原句："Access Guardian (Release 8) - Conceptual Flow / UNP Port classification rules 1..16" <<<PAGE 635-638>>>
- **F11 IoT 设备画像框架**：签名收集器（DHCP Option 55/60 + MAC OUI）→ 本地 profiler（签名库比对）→ UNP 档案自动指派 → 已知/未知设备库运营。原句："Device Profiling consists of three main components: A local signature collector, A local profiler, UNP profiling" <<<PAGE 686-690>>>
- **F12 Virtual Chassis 组件框架**：VFL/控制 VLAN/Chassis ID/Group ID/Chassis Priority + vcsetup.cfg/vcboot.cfg 双文件 + Master 选举五级 + RCD/VCSP 防脑裂。原句："VIRTUAL CHASSIS CONCEPT & COMPONENTS" <<<PAGE 292-307>>>
- **F13 OSPF 区域类型框架**：Backbone(0.0.0.0) / Stub / Totally Stubby / NSSA / Transit，对应 LSA 类型 1-7/9-11 的产生与抑制规则。原句："OSPF - Area types… Default Route / External AS / Inter-Area Routes" <<<PAGE 759-762>>>
- **F14 组播三层框架**：IGMP（成员管理，本段有效）→ IPMS（二层硬件交换）→ PIM-SM/DM、DVMRP（三层路由）；SPT/RP/BSR 角色分工。原句："Multicast - Switching vs. Routing Decision / Forwarding tables created by DVMRP, PIM-SM, PIM-DM and IPMS" <<<PAGE 874>>>
- **F15 Intelligent Fabric（SPB 织构）体系**：以 SPB 替代 STP 做二层织构、IS-IS 承载、Auto-fabric 自动化开通（6865/6900 IFAB 定位）。原句："SPB - Simplified service provisioning, better link utilization compared to STP / iFab Inside" <<<PAGE 73, 68>>>
- **F16 冗余方案选型框架**：STP（50% 带宽）→ LACP（链路冗余）→ VC（链路+设备冗余+统一管理）→ DHL（链路+设备冗余 100% 带宽）；三层另有 VRRP。原句："Comparison with Other Protocols… STP / 802.3Ad LACP / VC / DHL Active-Active" <<<PAGE 481>>>
- **F17 CodeGuardian 三层加固体系**：IV&V 源码验证 → 软件多样化（5 衍生镜像）→ 安全交付（随机下载/年度订阅）。原句："The LGS CodeGuardian™ technology hardens the OmniSwitch software on three levels" <<<PAGE 109-111, 1141>>>
- **F18 ALE 生命周期管理体系**：ProActive Lifecycle（OmniVista 2500 云端资产/软件/保修状态）+ CodeGuardian（软件完整性）组成运维闭环。原句："Alcatel-Lucent ProActive Lifecycle Management… works in conjunction with the Alcatel-Lucent OmniVista® 2500 Network Management System (NMS)" <<<PAGE 1139-1140>>>
