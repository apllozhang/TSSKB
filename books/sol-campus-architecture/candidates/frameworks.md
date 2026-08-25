# frameworks — sol-campus-architecture（F1…）

- **F1 园区三层设计栈框架**：需求四目标（可用/扩展/安全/性能）→ 拓扑模型（两层折叠 vs 三层）→ 接入层构件（VC/Stack、VLAN+MVRP、Trunk、LACP）→ 互联技术选型（SPB/EVPN/MPLS 对比矩阵）→ 动态路由（OSPF/BGP/IS-IS/RIP）；全书 LAN 章节即按此栈逐层展开 <<<PAGE 6>>>
- **F2 Stellar 无控制器 WLAN 框架**：管理面集中（OmniVista Enterprise/Cirrus）+ 控制面分布（AP 间 over-the-air/over-the-LAN 经 NMP 同步 RF 与客户端上下文）+ 数据面本地桥接优先、按 ARP 动态切换 L2GRE 隧道；三种管理模式（Express/Enterprise/Cloud）与 AP 组/RF Profile 两级组织结构 <<<PAGE 15>>>
- **F3 AP 接入双域框架**：VLAN 域（bridge 口 + defaultWLANProfile map vlan + MVRP + Trust Tag）与服务域/SPB（access 口 + l2profile peer + defaultWLANAccessProfile map service-type spb + vlan-tag 分类规则）两条对称的发现-分类-映射路径，命令集互为镜像 <<<PAGE 23>>>
- **F4 漫游与用户移动框架**：客户端上下文共享 → 漫游判定矩阵（无上下文/上下文+ARP 匹配/上下文+VLAN 不匹配）→ L2 漫游（默认常开）/L3 漫游（L2GRE 回家乡 AP）/快速漫游（802.11r/k 预认证）；子网规划（/24 + VLAN 池）为该框架的容量底座 <<<PAGE 26>>>
- **F5 统一接入安全框架**：UPAM 中央 RADIUS+captive portal → 认证谱系（IoT 指纹/MAC、802.1x 员工、访客四式、SSID 分段、BYOD 声明）→ 角色（UNP/ARP）定 VLAN+ACL+QoS → 事后处置（Quarantine Manager+QMR 隔离补救、WCF 过滤、wIDS/wIPS 检测遏制）；安全贯穿"接入-授权-运行-处置"全生命周期 <<<PAGE 36>>>
- **F6 Hybrid POL 混合架构框架**：Nokia POL 光分配网（单纤点对多点+ONT）作物理承载 + ALE 以太接入交换机/Stellar AP 作服务边缘；按"是否需全层冗余与高级特性"分两档推荐架构；收益模型 = 铜缆/机房/有源设备/能耗四类成本节约 + 2.5G→10/40G 演进能力 <<<PAGE 45>>>
