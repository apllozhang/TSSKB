# frameworks 候选 — DT00XTE216 OmniSwitch LAN Core Switching (Edition 15)

> 来源：fulltext.md（页码以 <<<PAGE N>>> 为准）。每条含原文摘录与适用说明。

---

## F-01 ERP 环网配置五步法（方法论框架）
- 页码：<<<PAGE 45>>>、<<<PAGE 46>>>、<<<PAGE 47>>>-<<<PAGE 49>>>
- 摘录："ERP CONFIGURATION Step by Step — Create ERP Ring, Service VLAN & MEG Level / Configure the RPL Port / Add Protected VLAN(s) / Enable the ERP Ring"；"Define a MEG Level (Management Entity Group) Value from 0 to 7. Must be identical on all the switches belonging to the ERP Ring"（p47）
- 内容：建立 ERPv2 环网的完整决策序列：①建环+Service VLAN+MEG Level（全网一致）→②唯一 RPL 端口与 RPL Owner→③加入受保护 VLAN→④admin-state enable。适合作为环网部署 checklist。

## F-02 ERP 状态机三态模型（idle / Protection / Pending）
- 页码：<<<PAGE 40>>>-<<<PAGE 42>>>、<<<PAGE 56>>>
- 摘录："idle: the RPL port is blocking... Protection: on link failure... the RPL node is now forwarding... Pending: The node is recovering from failure. When a node is in pending state, the WTR timer will be running"（p56 Notes）；稳态 NR/RB、故障 SF、恢复 NR+WTR（默认 5 分钟）见 p40-42
- 内容：用 R-APS 消息（NR/RB、SF）+ WTR/Guard 定时器解释环网三态转换，可提炼为故障定位与收敛判断的通用状态机框架。

## F-03 MACsec 部署模式决策树（Static SA / Dynamic PSK / Dynamic EAP）
- 页码：<<<PAGE 67>>>、<<<PAGE 75>>>、<<<PAGE 76>>>、<<<PAGE 78>>>-<<<PAGE 80>>>
- 摘录："Available Modes — Static SA Mode – Switch-to-Switch links / Dynamic SA Mode – Switch-to-Switch links / Switch-to-Host links (Using EAP)"（p67）；Static 模式管理步骤 "Get or generate Random Keys → Create security keys → Create key-chain → Associate security key to key-chain → Configure sci-tx/sci-rx... enable MACsec"（p75）；Dynamic PSK 步骤见 p78
- 内容：按"对端是交换机还是主机、是否能用 MKA 动态协商"选择三种模式；Static 不支持 OS6860N（p75 注）。

## F-04 MACsec 密钥轮换策略（时间 + 流量双触发）
- 页码：<<<PAGE 77>>>、<<<PAGE 89>>>
- 摘录："MACsec supports protocol key-rotation based on: Session time (in min) for SAK regeneration (5 minutes – 120 minutes) / Exchange data... (5GB –1000GB). Both values can be configurable in the same command, and whichever happens first will trigger the key exchange."
- 内容：安全运营中 SAK 轮换的双重门限设计：`macsec key-rotation max-session-time` + `max-exchange-data`，先到先触发。

## F-05 OSPF Area 设计决策框架（Standard/Stub/Totally Stubby/NSSA 边界）
- 页码：<<<PAGE 253>>>-<<<PAGE 254>>>、<<<PAGE 267>>>-<<<PAGE 270>>>
- 摘录："Main benefit of creating areas > reduce the number of routes to propagate"（p254）；Stub "Type 5 LSAs are not propagated into the stub area. Instead, R2 (ABR) injects a Type 3 LSA containing a default route"（p268）；Totally Stubby "Neither do the Type 3 LSAs. All routing out of the area relies on a single default route"（p269）；NSSA "Stub & Totally Stubby... Con: Neither type can contain an ASBR... Type 7 LSAs = Type 5 LSAs in disguise"（p270）
- 内容：按"区域内是否需要外部路由/是否有 ASBR/能接受多少 LSA"四象限选型。

## F-06 OSPF 配置七步法（含重分发）
- 页码：<<<PAGE 275>>>-<<<PAGE 280>>>
- 摘录："0) CONFIGURING THE ROUTER-ID ... 1) LOADING THE SOFTWARE ip load ospf 2) CREATING AN AREA 3) SPECIFYING AN AREA TYPE 4) CREATING AN OSPF INTERFACE 5) ASSIGNING AN INTERFACE TO AN AREA ... 6) REDISTRIBUTING LOCAL & EXTERNAL ROUTES 7) ENABLING OSPF"
- 内容：AOS R8 上启用 OSPF 的标准顺序，router-id 先行、最后统一 enable。

## F-07 路由重分发两步法（先 Route Map 后 Redistribution）
- 页码：<<<PAGE 272>>>-<<<PAGE 273>>>、<<<PAGE 300>>>
- 摘录："STEP 1: Configuring Route Maps — A Route Map is composed of Action / Match / Set"；"STEP 2: Configuring Route Redistribution... Redistribution configured > Router becomes ASBR"（p273）；"Route map: Criteria that is used to control redistribution of routes between protocols"（p300）
- 内容：Route Map（name+sequence+action+match+set）→ `ip redist <src> into <dst> route-map` 的通用重分发工作流。

## F-08 MSTP 配置六步法
- 页码：<<<PAGE 121>>>-<<<PAGE 126>>>
- 摘录："MSTP CONFIGURATION Step by Step — Select the Flat Spanning Tree mode / Select the MSTP protocol / Configure MST regions (name, revision level) / Configure MSTIs / Map VLANs to MSTI / Manage Switch Priority"
- 内容：flat 模式 → MSTP 协议 → region name+revision（三要素一致才同域：name/revision/VLAN 映射，p123）→ 建 MSTI → 映射 VLAN → 调优先级实现负载分担。

## F-09 Learned Port Security 配置四步法与违例决策
- 页码：<<<PAGE 190>>>-<<<PAGE 193>>>
- 摘录："Steps to Configuring LPS: Enable LPS on a port / Set the number of learned Mac's / Set the time limit for LPS / Select the violation mode"；"Violation options — Block only traffic that violates LPS port restrictions... Shutdown the port"（p190）
- 内容：端口安全部署框架：maximum（默认 1）、max-filtering（默认 5）、violation restrict/shutdown、convert-to-static 固定当前设备。

## F-10 环路防护/环网替换选型：STP vs SPB 决策框架
- 页码：<<<PAGE 521>>>-<<<PAGE 523>>>、<<<PAGE 565>>>
- 摘录："Unused links... Sub-optimal paths... Lack of a coordinated control plane... Slow convergence"（p521）；SPB-M 优势 "All network links are use with no loops / Spanning Tree Protocol replacement / Uses the shortest path end to end / 100's ms convergence times"（p523）
- 内容：从链路利用率、路径最优性、控制平面、收敛时间四个维度对比 STP 与 SPB-M，指导园区核心是否引入 SPB。

## F-11 SPB 骨干搭建四任务框架
- 页码：<<<PAGE 547>>>、<<<PAGE 548>>>
- 摘录："Backbone configuration entails the following tasks: Creating one or more BVLANs with their associated ECT-IDs... Defining the control BVLAN / Defining one or more SPB IS-IS interfaces / Enabling the SPB IS-IS protocol"
- 内容：BVLAN+ECT 分配（每 BVLAN 用不同 ECT 最大化分流，p548 best practice）→ control BVLAN（仅协议禁用时改，p548）→ ISIS network port → 全局 enable。

## F-12 iFab 零触摸部署流水线（Auto-VC→RCD→LACP→Routing→SPB→Profiling→MVRP）
- 页码：<<<PAGE 624>>>、<<<PAGE 626>>>-<<<PAGE 638>>>
- 摘录："1- Auto-VC 2- Automatic remote configuration 3- Auto-LACP 4- Auto-Routing 5- Auto-SPB Fabric 6- Auto-Network Profiling 7- Auto-MVRP"；"If not established configuration deleted & disabled"（p624）
- 内容：出厂交换机七阶段自动化框架；任一阶段邻居建立失败则自动回退删除配置。BVLAN 默认 4000-4015/ECT 1-16、控制 BVLAN 4000（p633）。

## F-13 VRF 部署与路由泄漏（Route Leak）框架
- 页码：<<<PAGE 458>>>-<<<PAGE 462>>>、<<<PAGE 468>>>-<<<PAGE 470>>>
- 摘录："VRF names are case sensitive... A default VRF instance is automatically configured"（p458）；"VRF Route Leak forwards routes from one VRF routing table to another VRF routing table... Route maps are used to import and export routes from the VRFs to the GRT (Global Routing Table)"（p461）
- 内容：vrf create → 接口归属 → 源 VRF export route-map → 目标 VRF import vrf <name> route-map，用于共享服务/跨租户受控互访。

## F-14 BGP 邻居策略匹配流程（policy list → route-map → peer in/out）
- 页码：<<<PAGE 505>>>-<<<PAGE 508>>>
- 摘录："AS Path, Community and Prefix lists / Route map... Route-maps evaluation... NO-> Routes dropped + Evaluation stopped"（p506 流程图）
- 内容：aspath-list/community-list/prefix-list 定义匹配条件 → route-map 组合 → `ip bgp neighbor <ip> route-map <name> in|out` 挂到邻居，控制出入路由。

## F-15 SLB 服务器负载均衡部署框架（VIP/权重/健康探测）
- 页码：<<<PAGE 655>>>-<<<PAGE 658>>>、<<<PAGE 665>>>
- 摘录："Enable SLB globally... Configure the SLB cluster / Assign physical servers to the SLB cluster / Modify optional parameters... Distribution algorithm / Health monitoring"（p655）；WRR "Aggregate weight of all servers should not exceed 32"（p656）；8.9R4 auto-bypass/wait-to-restore（p665）
- 内容：VIP 集群 → server+weight（0 为备份）→ probe 健康监测 → auto-bypass 容灾的完整框架。
