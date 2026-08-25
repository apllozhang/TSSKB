# GLOSSARY — OmniSwitch AOS 8.10R4 Network Configuration Guide 核心术语

从 verified 术语库精选约 150 条，按主题分组。协议/命令保留英文，页码为原书页码。

## 端口与链路基础

- **Autonegotiation（自协商）**：链路两端自动协商速率/双工/流控，关闭后 auto 参数失效（<<<PAGE 56>>>）
- **Crossover/MDI/MDIX**：直通/交叉线序模式；MDIX 为交换机侧标准（<<<PAGE 56>>>）
- **Duplex Mode（双工模式）**：full/half/auto（<<<PAGE 57>>>）
- **Link Trap（链路 Trap）**：端口状态变化的 SNMP 通告（<<<PAGE 57>>>）
- **Port Alias（端口别名）**：单端口描述字符串，不能配范围（<<<PAGE 58>>>）
- **Max Frame Size（最大帧长）**：如 9216 巨帧（<<<PAGE 58>>>）
- **Flood Rate Limiting（风暴控制）**：对 bcast/uucast/mcast 分别限速，超限丢包（<<<PAGE 59>>>）
- **Low Threshold（低阈值自动恢复）**：违规速率回落后自动退出 STORM violated（<<<PAGE 59>>>）
- **PAUSE（流控）**：tx/rx/tx-and-rx 三态，与自协商有从属关系（<<<PAGE 60>>>）
- **DDM（数字诊断监控）**：读光模块 EEPROM 监控温度/电压/电流/光功率（<<<PAGE 58>>>）
- **TDR（时域反射）**：发测试脉冲定位铜缆断点/长度（<<<PAGE 66>>>）
- **Link Monitoring（链路监控）**：按窗口监测端口错误与翻动并可自动关停（<<<PAGE 74>>>）
- **LFP（链路故障传播）**：把远端故障传播到本地接口触发关停（<<<PAGE 78>>>）
- **Violation Recovery（违规恢复）**：特性关停端口的统一恢复机制（<<<PAGE 69>>>）
- **Wait-to-Restore Timer**：端口恢复后延迟通知特性的稳定等待定时器（<<<PAGE 69>>>）
- **EPP（增强端口性能）**：特定平台的端口性能优化开关（<<<PAGE 61>>>）

## MACsec

- **MACsec（802.1AE）**：以太链路点到点加密/认证/防重放（<<<PAGE 83>>>）
- **SecTag**：MACsec 帧 8/16 字节头，含密钥信息/包号/信道标识（<<<PAGE 83>>>）
- **SCI（安全信道标识）**：标识单向安全信道（<<<PAGE 83>>>）
- **MKA（MACsec 密钥协商）**：协商并周期轮换 SAK 的协议（<<<PAGE 84>>>）
- **CAK/CKN**：连通性关联密钥及其名称（<<<PAGE 84>>>）
- **Key Server（密钥服务器）**：MKA 选出的生成分发 SAK 的节点（<<<PAGE 84>>>）
- **WAN MACsec**：面向广域链路的 MACsec 形态（<<<PAGE 87>>>）

## MAC 学习与 VLAN

- **Source Learning（源学习）**：从源 MAC 构建转发表（<<<PAGE 105>>>）
- **Static MAC / Filtering MAC**：静态绑定地址；bridging 转发/filtering 丢弃两种行为（<<<PAGE 105>>>）
- **MAC Aging Time（MAC 老化时间）**：动态表项老化周期（<<<PAGE 108>>>）
- **VID / VPA / Default VLAN**：VLAN 编号 / 端口成员关系 / 无 tag 流量归属 VLAN（<<<PAGE 115>>>）
- **802.1Q Tagging / Tagged-Untagged Port**：4 字节标签与两种成员模式（<<<PAGE 118>>>）
- **VLAN IP Interface（VLAN 路由接口）**：绑定 VLAN 的三层接口（<<<PAGE 121>>>）
- **PVLAN（私有 VLAN）**：主 VLAN+isolated/community 二级 VLAN 子域隔离（<<<PAGE 128>>>）
- **Promiscuous Port / ISL Port**：PVLAN 上联互通口 / 跨交换机延伸口（<<<PAGE 128>>>）
- **HA VLAN / Server Cluster / Virtual MAC**：服务器集群 VLAN 及其虚地址（<<<PAGE 140-141>>>）

## 生成树与 SPBM

- **Root Bridge / Root Path Cost / Root Port / Designated Port**：STP 选举体系（<<<PAGE 157-158>>>）
- **Alternate/Backup Port**：802.1w 区分的两种阻塞角色口（<<<PAGE 158>>>）
- **BPDU**：承载拓扑计算信息的二层帧（<<<PAGE 159>>>）
- **Bridge Priority（桥优先级）**：与 MAC 合成桥 ID（<<<PAGE 161>>>）
- **Flat Mode / Per-VLAN Mode**：单树 / 每 VLAN 一树（AOS 私有）两种模式（<<<PAGE 164>>>）
- **MSTI / MST Region / CST-CIST-IST**：MSTP 实例、区域与层级树概念（<<<PAGE 164, 167>>>）
- **SPB/SPBM（802.1aq）**：ISIS 驱动的最短路径以太网（<<<PAGE 211>>>）
- **ISIS-SPB**：带 SPB TLV 扩展的 IS-IS，建对称 SPT（<<<PAGE 211>>>）
- **PBB/PBBN（802.1ah）**：MAC-in-MAC 封装与骨干网（<<<PAGE 211>>>）
- **BEB / BCB / BMAC / BVLAN**：边缘桥 / 核心桥 / 骨干 MAC / 骨干 VLAN（<<<PAGE 211-212>>>）
- **Control BVLAN**：承载 ISIS-SPB 控制报文的 BVLAN（<<<PAGE 245>>>）
- **I-SID**：SPB 服务编号，绑定 BVLAN（<<<PAGE 212>>>）
- **ECT（等价树算法）**：16 个预定义算法打破等价路径平局（<<<PAGE 214>>>）
- **SPT（最短路径树）**：每桥以自己为根的转发树（<<<PAGE 214>>>）
- **IP over SPB / Inline Routing**：基于服务的 L3 VPN 接口形态（<<<PAGE 224>>>）

## 环网/聚合/双归

- **LBD（环回检测）/ Remote-origin LBD**：周期探测帧检测环路；默认传输 30 秒（<<<PAGE 325-326>>>）
- **ERP（G.8032）/ RPL / RPL Owner / R-APS**：以太环保护体系（<<<PAGE 395>>>）
- **WTR Timer / Guard Timer**：等待恢复 / 丢弃过时 R-APS 定时器（<<<PAGE 396>>>）
- **ERPv2 / Sub-ring / Major Ring**：多环/子环/主环层级（<<<PAGE 395, 399>>>）
- **MRP / MRM / MRC / MRA**：工业环网协议及其角色（投票自动选 MRM）（<<<PAGE 426-428>>>）
- **Redundancy Domain（冗余域）**：MRP 环域标识，每域两环口（<<<PAGE 428>>>）
- **Link Aggregation / Static-Dynamic Group / Linkagg ID**：链路聚合体系（<<<PAGE 341>>>）
- **Actor/Partner**：LACP 两侧角色命名（<<<PAGE 352>>>）
- **DHL（双归链路）**：Active-Active/Active-Standby 双上联保护（<<<PAGE 380>>>）
- **Pre-emption Time / MAC Flushing**：DHL 回切等待（默认 30 秒）/ 切换清 MAC（raw/mvrp）（<<<PAGE 382-383>>>）

## MVRP 与 MPLS/L2VPN

- **MVRP（多 VLAN 注册协议）**：动态声明/撤销 VLAN 成员（<<<PAGE 442>>>）
- **Dynamic VLAN / Applicant-Registrar Mode / Join-Leave Timer**：MVRP 机制要素（<<<PAGE 442-447>>>）
- **MPLS / Label Stack / LSR / LER / LSP / FEC**：标签交换体系（<<<PAGE 457-458>>>）
- **LDP / Hello Adjacency / Targeted Peer / LDP GR**：标签分发协议要素（<<<PAGE 458-461>>>）
- **VPLS / VPWS / PW / Attachment Circuit / Split Horizon**：L2VPN 体系（<<<PAGE 478>>>）
- **BGP VPLS Auto-discovery / Route Reflector**：自动发现与反射（<<<PAGE 480>>>）

## VXLAN/EVPN

- **VXLAN / VNI / VTI / VTEP / UDP 4789**：MAC-in-UDP 叠加封装体系；VTEP 由 Loopback0 标识（<<<PAGE 533-535>>>）
- **VXLAN Gateway**：桥接 VXLAN 与传统 VLAN 域的设备（<<<PAGE 533>>>）
- **EVPN / EVI / RT1-8**：BGP 以太 VPN 及路由类型分工（<<<PAGE 583-584>>>）
- **All-Active Multihoming**：多 PE 同时转发的冗余模型（<<<PAGE 583>>>）
- **MAC Mobility / BUM / Ingress Replication**：移动性仲裁 / 泛洪流量 / 单播复制（<<<PAGE 583-584, 606>>>）
- **Multi-site / Multi-PoD**：跨数据中心部署模型（<<<PAGE 661>>>）

## IP/IPv6/IPsec

- **IP Interface / Router ID**：三层接口模型与路由标识（<<<PAGE 709, 711>>>）
- **GRE**：IP over IP 隧道封装（<<<PAGE 721>>>）
- **VRF / VRF Profile / Management VRF**：L3 实例隔离体系（<<<PAGE 756-759>>>）
- **Link-local / Unique Local / Anycast / ND / RA Filtering / JITC Mode**：IPv6 寻址与邻居体系（<<<PAGE 773-777>>>）
- **ESP / AH / Transport Mode / SPI / SA / Master Key**：IPsec 要素；AOS 仅传输模式、AH 不加密（<<<PAGE 819-823>>>）

## 路由与网关冗余

- **RIP / Hold-down Timer / SHA256 Authentication**：距离向量路由要素（<<<PAGE 842-844>>>）
- **BFD / Asynchronous-Echo Mode / Detect Time Multiplier**：毫秒级故障检测体系（<<<PAGE 869-870>>>）
- **VRRP / VRID / Master-Backup / IP Address Owner / Skew Time / Preemption / Accept Mode / VRRP Tracking**：网关冗余体系（<<<PAGE 979-993>>>）
- **Condition Cluster / Server Health Monitoring**：SLB 集群标识与 ping 探测（<<<PAGE 1012-1015>>>）

## DHCP

- **DHCP Relay / Forward Delay / Maximum Hops / Per-interface Mode**：中继体系（<<<PAGE 903>>>）
- **Generic UDP Relay**：按端口转 UDP 到 VLAN/service/IP（<<<PAGE 904>>>）
- **Circuit ID/Remote ID**：Option-82 两个子选项（<<<PAGE 926>>>）
- **DHCP Snooping / Trusted Port / Binding Table / ISF**：窥探体系与 IPv6 源过滤（<<<PAGE 921-926>>>）

## 组播

- **IPMS / IPMSR / DVMRP**：二层组播交换与路由组合（<<<PAGE 1032-1033>>>）
- **Multicast Group Address / IGMP Querier / IGMP v1-3**：D 类地址、查询者选举、版本体系（<<<PAGE 1032-1036>>>）
- **IPMVLAN / MVR / Sender-Receiver Port / Enterprise-VLAN Stacking Mode**：组播 VLAN 分发体系（<<<PAGE 1086-1087>>>）

## QoS 与策略

- **Classification / 802.1p Priority / Trusted Port**：分类标记要素（<<<PAGE 1105, 1108>>>）
- **Queue Set/QSet Profile**：每口队列调度参数组（<<<PAGE 1114>>>）
- **PFC / Lossless TC**：基于优先级的流控与无损类（<<<PAGE 1120>>>）
- **Tri-Color Marking**：sr/tcm 三色限速（<<<PAGE 1125>>>）
- **Policy List（default/UNP/egress/AFP）/ qos apply / Condition Group / PolicyView**：策略体系要素（<<<PAGE 1133-1176>>>）

## 接入安全与认证

- **Access Guardian（准入卫士）**：认证+合规+访问控制框架（<<<PAGE 1212>>>）
- **UNP Classification Rules / UNP Port Type (bridge/access)**：无认证分类规则与端口形态（<<<PAGE 1211>>>）
- **MAC Authentication（MAC 认证）**：以 MAC 作用户名密码（<<<PAGE 1213>>>）
- **AAA Server / RADIUS / TACACS+ / RADSEC / RADIUS Health Check / Kerberos Snooping**：认证服务器矩阵；仅 RADIUS 支持端口准入（<<<PAGE 1475-1525>>>）
- **Application Signature Kit / Threat-Insight**：AppMon DPI 签名包与威胁监控（<<<PAGE 1431, 1449>>>）
- **AFP / REGEX Signature File / AFP Mode**：REGEX 指纹识别体系（<<<PAGE 1457-1458>>>）
- **LPS Learning Window / Packet Relay**：端口安全学习窗口与违规报文中继（<<<PAGE 1536, 1542>>>）

## 诊断与 OAM

- **Port Mirroring / Unblocked VLAN / Port Monitoring / RMON / Switch Health**：镜像、落盘抓包、探针、资源阈值（<<<PAGE 1558-1567>>>）
- **VLAN Stacking/QinQ / Double Tagging / VLAN Translation**：运营商隧道封装两法（<<<PAGE 1606-1608>>>）
- **Service OAM/CFM / MD Level 0-7 / EVC / Virtual MEP / Frame Delay Measurement**：端到端业务运维体系（<<<PAGE 1655-1665>>>）
- **EFM LINK OAM / OAMPDU / Remote Loopback / Errored Frame 三窗口**：单链路运维体系（<<<PAGE 1673>>>）
- **CPE Test Head / CPE Test Group**：L2 SAA 性能测试框架（<<<PAGE 1690, 1710>>>）
- **PPPoE-IA / Access Node / Access Loop / Circuit-Remote ID**：接入代理与线路标识（<<<PAGE 1714-1715>>>）
- **SAA**：以 SPB 会话做服务保障测量，可出 XML 历史（<<<PAGE 1700>>>）
