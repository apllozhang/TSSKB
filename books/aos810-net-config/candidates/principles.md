# principles — OmniSwitch AOS 8.10R4 Network Configuration Guide（原理与机制候选）

格式：编号 P# ｜ 机制要点 ｜ 页码（fulltext.md 真实 `<<<PAGE N>>>` 标记）｜ 英文原句摘录（可选）

## 以太网端口与链路（Ch1）

- **P1** 端口自协商关闭后 auto MDIX/auto speed/auto duplex 失效："If autonegotiation is disabled, auto MDIX, auto speed, and auto duplex are not accepted." <<<PAGE 56>>>
- **P2** MDIX 是集线器/交换器侧标准，MDI 是终端侧标准："Setting crossover configuration to mdix configures the interface ... which is the standard for hubs and switches." <<<PAGE 56>>>
- **P3** `clear interfaces ... l2-statistics cli` 只清 CLI 计数、SNMP 累计值保留："only those statistics that are maintained by the switch CLI are cleared; SNMP values are not cleared." <<<PAGE 57>>>
- **P4** DDM 通过读取光模块 EEPROM 监控温度/电压/电流/光功率五项指标，阈值分 Warning/Alarm 高低四档："Digital Diagnostics Monitoring allows the switch to monitor the status of a transceiver by reading the information contained on the transceiver's EEPROM." <<<PAGE 58>>>
- **P5** 风暴控制按 bcast/uucast/mcast 三类分别限速，超阈值即丢包："When the threshold value is reached, packets are dropped." <<<PAGE 59>>>
- **P6** 风暴低阈值自动解除机制：违规速率降到 low-threshold 以下时端口自动退出 STORM violated 状态："When the rate of violating traffic received on the port goes below the low threshold value, the port is removed from the violating state." <<<PAGE 59>>>
- **P7** 全双工 PAUSE 流控与自协商的从属关系："if autonegotiation and flow control are both enabled for an interface, then autonegotiation determines how the interface processes PAUSE frames." <<<PAGE 60>>>
- **P8** 违规恢复体系=手动 clear violation+自动恢复定时器+最大恢复次数+wait-to-restore+SNMP trap 五件套："The OmniSwitch allows features to shutdown an interface when a violation occurs on that interface." <<<PAGE 69>>>
- **P9** 两种关断方式（Filtering 保链路灯/Administratively 灭灯）恢复路径不同："Disconnecting/reconnecting the interface link or a link down/up event will not recover a port that was administratively disabled." <<<PAGE 69>>>
- **P10** 永久关断状态只能用 clear violation（或 interfaces reset）恢复："An interface is already in a permanent shutdown state. In this case, the only method for recovery is to use the clear violation command." <<<PAGE 70>>>
- **P11** 使用违规恢复机制的特性清单：STP/QoS/LPS/UDLD/NetSec/NI/LLDP/LinkMon/LFP/RFP，各有 Discard 或 Admin-Down 类型。<<<PAGE 70>>>
- **P12** 违规自动恢复默认 300 秒，且不支持聚合口只支持成员口："The interface violation recovery mechanism is not supported on link aggregates, but is supported on the link aggregate member ports." <<<PAGE 71>>>
- **P13** MACsec 提供 IEEE 802.1 点到点链路安全，防 DoS/中间人/重放/窃听："MACsec (MAC Security) provides point-to-point security on Ethernet links between directly connected nodes." <<<PAGE 83>>>
- **P14** MACsec 帧结构：EtherType 0x88E5 + 8/16 字节 SecTag + 可选加密载荷 + GCM-AES 16 字节 ICV："a MACsec packet starts with an Ethernet header with etherType 0x88E5, followed by an 8-byte or 16-byte SecTag header." <<<PAGE 83>>>
- **P15** 安全信道（SC）单向、以 SCI 标识；收发两端需配对匹配 SCI-Tx/SCI-Rx："A single secure channel is unidirectional." <<<PAGE 83>>>
- **P16** SA 内含 SAK 与包号（PN），接收侧用 PN 做重放保护："the packet number from the SecTag header will be checked against the packet number locally stored ... to perform replay protection." <<<PAGE 83>>>
- **P17** 默认加密套件 128-bit AES-GCM；SAK 会话密钥由 MKA 协议（802.1X-2010 扩展）协商："The MKA ... is an extension to 802.1X, which provides the required session keys." <<<PAGE 84>>>
- **P18** 动态 SAK(PSK) 模式：CAK 保护控制面、随机 SAK 保护数据面，key server 由协商选出并周期换钥："The MKA protocol selects one of the nodes as the key server, which creates a dynamic SAK and shares it with the node at the other end." <<<PAGE 84>>>
- **P19** 动态 CAK(EAP) 模式：802.1X 认证成功后由 RADIUS 下发 MSK，CAK/CKN 从 MSK+Session-Id 派生，必须用 EAP-TLS 双向认证："802.1x-authentication using EAP-TLS must be used as mutual authentication protocol for MACsec Dynamic mode." <<<PAGE 85>>>
- **P20** switch-to-host 场景交换机永远是 key server，客户端只能单 MKA 实体："The client is never a key server and can only interact with a single MKA entity." <<<PAGE 85>>>

## UDLD（Ch2）

- **P21** UDLD 是二层协议，检测光纤/铜缆单向链路并 admin-shutdown 受影响端口，防止 STP 环路："Unidirectional links can create hazardous situations such as Spanning-Tree topology loops." <<<PAGE 98>>>
- **P22** Normal 模式只依赖显式信息，未确定时标记 Undetermined 不关端口；Aggressive 模式定时器超时即关端："the lack of information is not always due to a defective link, this mode is optional and is recommended only for point-to-point links." <<<PAGE 98>>>
- **P23** UDLD 两大机制：邻居数据库（Hello/探测缓存老化）与回声检测（echo detection 窗口内无回应则按模式处置）。<<<PAGE 99>>>
- **P24** 缓存同步：端口禁用/UDLD 关闭/重启时清缓存并通知邻居 flush，实现缓存同步。<<<PAGE 99>>>

## 源地址学习/MAC（Ch3）

- **P25** MAC 表条目只有两种来源：动态学习与静态配置："New MAC address table entries are created in one of two ways: they are dynamically learned or statically assigned." <<<PAGE 105>>>
- **P26** 静态 MAC 适用沉默设备（silent devices），保证流量定向转发："These types of devices do not send packets, so their source MAC address is never learned." <<<PAGE 105>>>
- **P27** 静态 MAC 两种行为：bridging（默认）与 filtering（丢弃以阻断攻击）。<<<PAGE 105>>>
- **P28** 静态 MAC 永久有效，重启与老化均不删除："a static MAC address remains in use even if the MAC ages out or the switch is rebooted." <<<PAGE 105>>>
- **P29** 聚合口上的静态 MAC 配在 linkagg ID 而非物理口："Static MAC Addresses are not assigned to physical ports that belong to a link aggregate." <<<PAGE 106>>>

## VLAN（Ch4）

- **P30** VLAN 通过软件分割广播域，免去物理改线："VLAN configuration and port assignment is handled through switch software." <<<PAGE 115>>>
- **P31** VLAN 操作状态在至少一个活动端口加入前保持 inactive，STP/路由接口随之不激活："The operational status of a VLAN remains inactive until at least one active switch port is assigned to the VLAN." <<<PAGE 115>>>
- **P32** 802.1Q tag 为 4 字节：前 2 字节标识 802.1Q，后 2 字节携带 VID+优先级。<<<PAGE 118>>>
- **P33** 入方向分类规则：带 tag 必须匹配端口默认 VLAN 或已打标 VLAN，否则丢弃；无 tag 进端口默认 VLAN。<<<PAGE 118>>>
- **P34** 一个端口只能属于一个 untagged VLAN（即默认 VLAN），可属于任意多个 tagged VLAN："A port can only be assigned to one untagged VLAN." <<<PAGE 118>>>
- **P35** 删除 VLAN 时路由接口被移除、VPA 丢弃；若是端口默认 VLAN 则端口回落到 VLAN 1。<<<PAGE 116>>>
- **P36** VLAN admin-state 禁用时端口归属保留但不转发流量。<<<PAGE 116>>>
- **P37** PVLAN 把主 VLAN 划分为 isolated/community 二级 VLAN 子广播域，同时保留 L3 配置："A PVLAN divides a VLAN (Primary) into sub-VLANs (Secondary) to partition the single broadcast domain." <<<PAGE 128>>>
- **P38** 主 VLAN 上配置的 admin 状态/STP 状态/IP 接口自动作用于全部关联二级 VLAN："When the status is changed for the Primary VLAN ID, the change is automatically applied to the Secondary VLANs." <<<PAGE 129>>>

## 高可用 VLAN/服务器集群（Ch5）

- **P39** HA VLAN 把发往单一目的 MAC 的流量复制到多个出端口实现服务器集群冗余："High availability (HA VLAN)s send traffic intended for a single destination MAC address to multiple switch ports." <<<PAGE 140>>>
- **P40** L2 集群用静态 MAC 实现、L3 集群用静态 ARP 实现："The L2 mode is currently supported in AOS using the static mac-address command and L3 mode by the static ARP command." <<<PAGE 140>>>
- **P41** 出端口可静态配置或通过 IGMP report 注册，组播依据目的 MAC/IP 可配置。<<<PAGE 140>>>

## 生成树（Ch6）

- **P42** AOS 支持 802.1D STP、802.1w RSTP、802.1Q-2005 MSTP；RSTP 让阻塞口跳过 listening/learning 直接转发："RSTP expedites topology changes by allowing blocked ports to transition directly into a forwarding state." <<<PAGE 157>>>
- **P43** 拓扑计算原理：选根桥→每桥计算到根最优路径→阻塞成环节路；根路径成本=接收端口路径成本之和，最低者为指定桥。<<<PAGE 157>>>
- **P44** 端口角色五类：Root/Designated/Backup/Alternate/Disabled；backup 与 alternate 的区分是 802.1w 为快速切换引入。<<<PAGE 158>>>
- **P45** MST 把 VLAN 集合映射到 MSTI，Flat 模式下最多 17 个实例（含 CIST 实例 0）。<<<PAGE 164>>>
- **P46** Flat 模式是整交换机单棵树（跨 VLAN 比较）；Per-VLAN 模式是每 VLAN 一棵树（AOS 私有实现）。<<<PAGE 164>>>
- **P47** MSTP 下端口状态由 CST 算法统一计算，但可对单个 MSTI 配 priority/path cost 使端口在该 MSTI 转发而在其他实例阻塞。<<<PAGE 164>>>
- **P48** Flat 模式下 CIST 被禁则对所有 VLAN 禁用；单 VLAN 禁用只把该 VLAN 端口移出算法。<<<PAGE 120>>>

## SPBM（Ch7）

- **P49** SPBM=ISIS-SPB 控制面 + 802.1ah MAC-in-MAC 数据面，IEEE 802.1aq："SPBM provides a mechanism to automatically define a shortest path tree (SPT) bridging configuration through a Layer 2 Ethernet network." <<<PAGE 211>>>
- **P50** 角色分工：BEB 学习并封装客户帧，BCB 只按 BMAC 转发不学客户 MAC："the BCB does not have to learn any of the customer MAC addresses." <<<PAGE 211>>>
- **P51** BVLAN 不学源 MAC、不泛洪未知流量，只按 ISIS-SPB 填充的 FDB 转发："Unlike standard VLANs, BVLANs do not learn source MAC addresses or flood unknown destination or multicast frames." <<<PAGE 211>>>
- **P52** 每个 SPB 桥以自己为根计算 SPT，因此任意两点间都是最短路径，克服 STP 根桥次优路径问题："each bridge can provide the shortest path to every other bridge in the network." <<<PAGE 214>>>
- **P53** SPB 用 16 个预定义 ECT 算法在等价路径间打破平局；同一 BVLAN 全网须配同 ECT 保证路径一致对称："The same ECT algorithm is configured for the same BVLAN ID on each SPB switch." <<<PAGE 214>>>
- **P54** 环路抑制靠 BVLAN 严格入向源 MAC 检查（异常来源即丢弃），MAC 学习由控制面完成。<<<PAGE 214>>>
- **P55** I-SID 标识 SPB 服务并绑定 BVLAN，一个 BVLAN 可承载多个 I-SID；SAP 把接入端口与特定客户流量（CVLAN/untagged/all）绑定到服务。<<<PAGE 212>>>
- **P56** 配置顺序原则：先全网配骨干（BVLAN/ECT/control-bvlan/ISIS 接口/enable），后配服务："the SPBM backbone is configured on every switch first, then the SPBM service architecture is configured second." <<<PAGE 245>>>
- **P57** SAP 封装值语义：`port:x` 只映射 CVLAN x，`:0` 映射 untagged，`:all` 映射全部 tagged。<<<PAGE 245>>>

## 环回检测（Ch8）

- **P58** LBD 周期发探测帧，任何 LBD 使能口收到本机帧即判环并 shutdown 端口+trap+日志。<<<PAGE 325>>>
- **P59** remote-origin LBD 需全局+端口两级同时使能默认 LBD 和远端 LBD 四个条件才工作。<<<PAGE 326>>>
- **P60** 传输定时器默认 30 秒；被 block 端口停止一切收发。<<<PAGE 325>>>
- **P61** 与 STP 交互：MST 模式下 LBD 只能在 STP 禁用的接口上使能；LBD 帧不打 tag 发送。<<<PAGE 328>>>
- **P62** 与聚合交互：任一成员口检测到环，整个 linkagg 全部 shutdown。<<<PAGE 328>>>

## 链路聚合（Ch9/10）

- **P63** 聚合组被 AOS 当作虚拟物理口，VLAN/802.1Q/QoS 均可套用。<<<PAGE 341>>>
- **P64** 负载分担：非 IP 按 MAC、IP 报文按 IP 地址；组内端口必须同速："Ports must be of the same speed within the same link aggregate group." <<<PAGE 341>>>
- **P65** 静态聚合与部分厂商设备不互通："Static aggregate groups cannot be created between an OmniSwitch and some switches from other vendors." <<<PAGE 341>>>
- **P66** 动态聚合用 IEEE 802.3ad LACP，靠 LACPDU 双向协商最优配置并持续监测维护。<<<PAGE 352>>>
- **P67** 动态聚合组由唯一 MAC 标识（交换机生成，可改）。<<<PAGE 352>>>

## 双归链路 DHL（Ch11）

- **P68** DHL Active-Active：linkA/linkB 各映射一组 VLAN 同时活，故障时 VLAN 切换到另一链路，替代 STP 收敛。<<<PAGE 383>>>
- **P69** DHL 会话使能后两链路上的 STP 自动禁用。<<<PAGE 382>>>
- **P70** 未映射到 linkB 的 VLAN 自动归 linkA（默认全在 linkA）。<<<PAGE 383>>>
- **P71** 跨模块 DHL 建议配置 MAC flush（MVRP 或 raw flooding）改善收敛。<<<PAGE 382>>>

## ERP（Ch12）

- **P72** ERP 基于 ITU-T G.8032，用 R-APS 协议在以太环上防环："Loop prevention is achieved by allowing the traffic to flow on all but one of the links within the protected Ethernet ring." <<<PAGE 395>>>
- **P73** RPL owner 阻塞 RPL；故障时 R-APS(SF) 触发解阻塞进入保护模式，全网 flush 动态 MAC。<<<PAGE 397>>>
- **P74** 恢复流程：恢复侧发 R-APS(NR) 并启 Guard Timer→RPL owner 启 WTR→超时后阻塞 RPL 并发 R-APS(NR,RB)→各节点 flush MAC 回到 idle 模式。<<<PAGE 398>>>
- **P75** WTR 用于确认环稳定后才回到阻塞态；Guard Timer 防止接收过时 R-APS，取值须大于 R-APS 绕环最大转发时延。<<<PAGE 396>>>
- **P76** ERPv2 支持多环/梯形网、R-APS Virtual Channel、revertive/non-revertive；子环不能用共享链路。<<<PAGE 395>>>
- **P77** 链路监测用 ETH CC OAM（CFM），本实现叠加 link up/down 事件加快收敛。<<<PAGE 395>>>

## MRP（Ch13）

- **P78** MRP 面向工业环网，对单一链路/节点故障做确定性重构："MRP is designed to react deterministically on a single failure of an inter-switch link or switch in the ring." <<<PAGE 426>>>
- **P79** 角色模型：一个 MRM+多个 MRC；MRA 通过投票（MRP_Test 帧携带优先级+MRP_TestMgrNAck）自动选出 MRM，其余转 MRC。<<<PAGE 428>>>
- **P80** MRM 控制：双向周期发 MRP_Test；能收到自己发的测试帧说明环闭合→阻塞一口；收不到则两口全转发。<<<PAGE 428>>>
- **P81** 环口三态：Disabled/Blocked（仅放行 MRP 控制帧与 LLDP/PTP 等）/Forwarding。<<<PAGE 426>>>
- **P82** 冗余域=环；每域恰好两个环口，域 ID 用于多环设备区分帧。<<<PAGE 428>>>

## MVRP（Ch14）

- **P83** MVRP 作为 MRP 应用在专用组播 MAC 上收发声明，动态创建/撤销 VLAN 注册："MVRP allows both end stations and bridges ... to issue and revoke declarations relating to membership of VLANs." <<<PAGE 442>>>
- **P84** 动态 VLAN 的所有端口对该 VLAN 都是 tagged 口。<<<PAGE 442>>>
- **P85** 转发声明≠加入：端口转发从其他口学到的声明，但只有本口收到声明才加入该 VLAN。<<<PAGE 442>>>
- **P86** 与 STP 交互：MVRP 仅支持 Flat 模式；拓扑变化时 MVRP 学到的动态 VPA 一并删除。<<<PAGE 444>>>

## MPLS/L2VPN（Ch15/16）

- **P87** MPLS 用 32 位标签头（20 位 Label）逐跳标签交换建立点到点通道。<<<PAGE 457>>>
- **P88** LSP 单向：双工业务需要两条 LSP；LSP 物理路径不受 IGP 最短路径约束。<<<PAGE 457>>>
- **P89** 标签栈处理永远只看栈顶标签，查表得到下一跳+栈操作（swap/pop/push）。<<<PAGE 457>>>
- **P90** LER 提供 VPN 服务，VPWS/VPLS 用 LDP（VPLS 也可 BGP）信令在边缘建立服务实例。<<<PAGE 458>>>
- **P91** LDP 邻接：UDP hello（携带 LSR ID）建 Hello adjacency，TCP 会话成 peer，Label Mapping 分发 FEC-标签绑定，hold/keepalive 定时器监测活性。<<<PAGE 458>>>
- **P92** VPLS 是多点 L2VPN，需 PE 间全网格伪线；VPWS 只是点对点，不含 L2/L3 功能："VPLS is a superset of VPWS." <<<PAGE 478>>>
- **P93** VPLP 防环规则 Split Horizon：从 PW 收到的包绝不再从 PW 发出；全网格+水平分割保证广播可达且无环。<<<PAGE 478>>>
- **P94** BGP VPLS 自动发现免去手工配置全部远端；RR 减少 AS 内 full-mesh peering，VPLS RR 仅支持 IPv4 地址族。<<<PAGE 480>>>
- **P95** VPLS 每服务实例维护 FIB，未知目的泛洪到全部 LSP 直到目标回应学习到 MAC。<<<PAGE 480>>>

## VXLAN（Ch17）

- **P96** VXLAN 把 VM 的以太帧封装进带 UDP 头的 IP 包在三层网传输；OmniSwitch 作 VXLAN 网关连接 VXLAN 与传统 VLAN 域。<<<PAGE 533>>>
- **P97** VNI 是 24 位段标识，只有同段 VM 可互通；同 VNI 的 VLAN 流量在网关处封装/解封。<<<PAGE 533>>>
- **P98** VTI 由 SDP+服务绑定提供；VTEP 由 Loopback0 IP 地址标识。<<<PAGE 533>>>
- **P99** 封装外层：外层 IP 源=本端 VTEP Loopback0，目的=对端 Loopback0；UDP 目的端口默认 4789（可配）。<<<PAGE 535>>>
- **P100** 本地二层流量直接桥接不走隧道，封装过程对 VM 透明。<<<PAGE 534>>>

## EVPN（Ch18）

- **P101** EVPN 是 BGP 扩展，用控制面通告 MAC/IP 可达性，替代数据面泛洪学习："Since the MAC learning is handled in the control plane with EVPN architecture, it avoids the flooding in Layer 2." <<<PAGE 583>>>
- **P102** EVPN 以 all-active 多归属提供多路径转发与冗余；DF/NDF 分工：仅 DF 转发 BUM，保证无环。<<<PAGE 583>>>
- **P103** 路由类型分工：RT1(AD/快速收敛/别名负载分担)、RT2(MAC/IP 通告/移动性/ARP 抑制)、RT3(含组播路由/ingress replication 建 BUM 泛洪域)、RT4(ES 路由/DF 选举)、RT5(IP 前缀/L3VPN)、RT6-8(选择性组播/IGMP 同步)。<<<PAGE 584>>>
- **P104** AOS ESI 模型：物理口/LACP 自动生成 Type 0x3 MAC-based ESI；静态聚合必须手工配 ESI。<<<PAGE 587>>>
- **P105** AOS 单归设备也用非零 ESI，享受控制面 FDB 管理，且可与其他厂商互通。<<<PAGE 583>>>
- **P106** ETag=VLAN ID，SAP 挂载产生 ETag 级路由汇总，路由撤收可按 ETag 批量进行。<<<PAGE 588>>>
- **P107** RD 自动生成：8 字节=2 字节 Type(0x1)+6 字节值；值域分 service(0x0)/ESI(0x1)/prefix(0x2) 三类对象。<<<PAGE 588>>>

## IP（Ch21）

- **P108** IP 无连接不可靠，靠 TCP 补可靠；ARP/VRRP/ICMP/组播是配套的基础协议。<<<PAGE 709>>>
- **P109** IP 接口绑定 VLAN：`ip interface <name> address <ip> vlan <vid>` 是三层路由基本模型。<<<PAGE 709>>>
- **P110** 静态路由/递归静态路由/默认路由/黑洞路由均由 `ip static-route` 系列配置（章内各节）。<<<PAGE 709>>>

## VRF（Ch22）

- **P111** VRF 在同一物理交换机上分割 L3 实例，类比 VLAN 分割 L2："Similar to using VLANs to segment Layer 2 traffic, VRF instances are used to segment Layer 3 traffic." <<<PAGE 756>>>
- **P112** 每个 VRF 独立路由表+独立路由协议实例，可重复使用 IP 地址空间。<<<PAGE 756>>>
- **P113** AOS VRF 不要求 BGP/MPLS 骨干，可经 GRE/IP-IP 隧道点对点承载。<<<PAGE 756>>>

## IPv6（Ch23）

- **P114** IPv6 增强：128 位地址、无状态自动配置、任播、简化头、ND 协议替代 ARP/广播。<<<PAGE 773>>>
- **P115** 地址类型：link-local（仅链路内有效不可路由）、unicast、unique local、multicast、anycast（前缀不可辨识）。<<<PAGE 774>>>
- **P116** IPv4/IPv6 共存机制：双栈、同 VLAN 双协议接口、IPv6-over-IPv4 隧道、IPv4 内嵌地址。<<<PAGE 773>>>
- **P117** JITC 模式下禁配 Site-Local（FEC0::/10）地址。<<<PAGE 774>>>

## IPsec（Ch24）

- **P118** IPsec 在网络层提供访问控制/完整性/认证/抗重放/机密性；ESP 提供加密+可选认证，AH 只认证不加密。<<<PAGE 819>>>
- **P119** OmniSwitch IPsec 仅支持传输模式（Transport Mode）：头插在 IP 头与上层协议头之间。<<<PAGE 819>>>
- **P120** ESP 由 IP 协议号 50 标识；SPI+目的地址+协议唯一确定 SA；认证先校验后解密。<<<PAGE 820>>>
- **P121** 加密算法 AES-CBC(128/192/256) 与 3DES；认证 HMAC-MD5(128bit)/HMAC-SHA1(160bit)。<<<PAGE 820>>>

## RIP（Ch25）

- **P122** RIP 以跳数为度量，直连=1 跳，>15 跳路由删除；默认 30 秒广播更新。<<<PAGE 842>>>
- **P123** 定时器体系：120 秒无更新进 hold-down，超时删路由。<<<PAGE 842>>>
- **P124** RIPv2 增强（next hop/认证/组播更新）只有组播时才可用，以兼容 RIPv1。<<<PAGE 843>>>

## BFD（Ch26）

- **P125** BFD 是轻量 Hello 协议专做转发面故障检测，毫秒级，不依赖具体路由协议，CPU 开销低于收紧协议定时器。<<<PAGE 869>>>
- **P126** BFD 无邻居发现，由宿主协议（OSPF/BGP/VRRP/静态路由）请求建会话；检测时间=Detect Multiplier×Min Rx Interval。<<<PAGE 869>>>
- **P127** 异步控制包模式与 Echo 模式：VRRP/静态路由只用 Echo，OSPF/IS-IS/BGP 用控制包；Echo 单跳、控制包可多跳。<<<PAGE 870>>>
- **P128** Echo 无需对端配置 BFD（不是会话），只在本端使能即可。<<<PAGE 870>>>

## DHCP Relay/安全（Ch27）

- **P129** DHCP Relay 用 UDP 67/68，校验 forward-delay 与 maximum-hops，不满足即丢弃；多目的地址时全发。<<<PAGE 903>>>
- **P130** relay 转发模式分 global 与 per-interface 两级。<<<PAGE 903>>>
- **P131** DHCP 三种地址分配：automatic（永久）/dynamic（租期）/manual（管理员指定由 DHCP 传达）。<<<PAGE 904>>>
- **P132** DHCP Relay Agent 可跨 VLAN 域与 SPB service 域中继；Generic UDP Relay 按预配端口转至 VLAN/SPB/IP。<<<PAGE 904>>>
- **P133** 外部路由器 relay 场景：子网地址由路由器插入请求，交换机无需 IP。<<<PAGE 905>>>
- **P134** L3 DHCP Snooping 必须借助 relay（客户端与服务器不同 VLAN）；L2 模式无需 relay 与 IP 接口。<<<PAGE 925>>>
- **P135** Snooping 使能后默认激活：绑定表维护、源 MAC 与 CHADDR 校验、Option-82 插入、回复只回原请求口。<<<PAGE 926>>>
- **P136** 非信任口收到含 Option-82 的包默认丢弃，可配置 bypass。<<<PAGE 925>>>
- **P137** 全局 Option-82 使能与任意级别 Snooping 互斥；交换机级与 VLAN 级 Snooping 互斥。<<<PAGE 925>>>

## 内部 DHCP 服务器（Ch28）

- **P138** 内部 DHCP Server 由 policy file+配置文件+数据库文件驱动，与 VRF/DHCP Snooping/IP 接口交互（章内 Interaction 节）。<<<PAGE 894>>>（正文页 28-4 附近，标记 <<<PAGE 894>>> 前后）

## VRRP（Ch29）

- **P139** VRRP 选举虚拟路由器 master 转发虚拟 IP 流量，master 失效最高优先级 backup 接管。<<<PAGE 979>>>
- **P140** IP 地址拥有者（owner）可用时必为 master；仅 master 周期性发通告到 224.0.0.18。<<<PAGE 980>>>
- **P141** Master_Down_Interval=(3×Adv_Interval)+Skew_Time，Skew=(256-Priority)/256，优先级越低等待越长避免抖动。<<<PAGE 980>>>
- **P142** 虚拟 MAC：v2=00-00-5E-00-01-VRID，v3/IPv6=00-00-5E-00-02-VRID；ND 替代 ARP 用于 IPv6。<<<PAGE 981>>>
- **P143** 成为 master 时发免费 ARP；接口 IP 被虚路由共享时路由机制不再发免费 ARP，防表未稳先导流。<<<PAGE 981>>>
- **P144** VRRP 支持 BFD 联动 tracking 与 UNP 动态 SPB SAP（章内 Interaction 节）。<<<PAGE 980>>>

## SLB（Ch30）

- **P145** SLB 集群以 VIP（L3，需服务器配 loopback）或 QoS condition（L2/L3）标识虚拟服务器。<<<PAGE 1012>>>
- **P146** L3 模式改写源/目的 IP 并递减 TTL；L2 模式不改包仅同 VLAN 桥接（仅 condition 集群）。<<<PAGE 1012>>>
- **P147** 分发算法为加权轮询 WRR，按服务器相对权重分配请求；健康监测依赖 ping 探测（周期/超时/重试可配）。<<<PAGE 1012>>>

## IPMS（Ch31）

- **P148** 组播组地址为 D 类 224.0.0.0-239.255.255.255，239/8 为管理域（边界保留）。<<<PAGE 1032>>>
- **P149** IPMS 跟踪 IGMP 请求的源 VLAN/SPB service/VPLS service；转发前验证组播包来自预期端口。<<<PAGE 1032>>>
- **P150** 多个组播路由器共存时最低 IP 者当选 querier。<<<PAGE 1033>>>
- **P151** 组播路由协议包：PIM-SM/DM 与 DVMRP，建立组播路由库，IPMS 依其决策+端口成员请求转发。<<<PAGE 1033>>>

## IPMVLAN/MVR（Ch32）

- **P152** IPMV 在 L2 分布交换机上以专用组播 VLAN 分发流量，用户 VLAN 无需路由器即可接收。<<<PAGE 1086>>>
- **P153** MVR 单一网络级组播 VLAN 被多用户 VLAN 共享，IGMP join/leave 走用户 VLAN，流走组播 VLAN，隔离带宽与安全。<<<PAGE 1086>>>
- **P154** 组播流量只从分发 VLAN 流向客户 VLAN，客户自产组播只走客户 VLAN 由路由器控制。<<<PAGE 1086>>>
- **P155** Stacking 模式：NNI=唯一 sender 口，UNI=receiver 口可多个；绑定方法用 IP 地址或 CVLAN-tag 二选一。<<<PAGE 1087>>>

## QoS（Ch33）

- **P156** QoS 四步序：分类标记→拥塞管理（入队调度）→拥塞避免（随机丢弃防 tail drop）→限速整形。<<<PAGE 1103>>>
- **P157** CoS 判定基于 IP precedence(3bit)/DSCP(6bit PHB)/802.1p(3bit) 三类技术。<<<PAGE 1105>>>
- **P158** 策略=条件+动作；流不匹配任何策略则用端口默认 QoS；多策略命中取最高 precedence。<<<PAGE 1133>>>
- **P159** 每端口 8 条队列，入队依据策略+ToS/802.1p+端口信任状态。<<<PAGE 1133>>>
- **P160** 策略来源决定修改权：PolicyView(LDAP) 建的只能 PolicyView 改，CLI/WebView 建的只能本端改。<<<PAGE 1133>>>
- **P161** 四类策略列表：default/UNP/egress/AFP（AFP 仅 OS6900）。<<<PAGE 1134>>>
- **P162** tagged 口默认 untrusted；VLAN Stacking 口默认 trusted 且默认分类 802.1p，可用内层 VLAN/内层 802.1p 条件分类。<<<PAGE 1134>>>
- **P163** 条件配置约束：IPv4/IPv6 条件不能混用；destination VLAN 条件仅组播规则可用。<<<PAGE 1135>>>
- **P164** policy condition/action/rule 配置后必须 `qos apply` 才激活。<<<PAGE 1149>>>

## 策略服务器（Ch34）

- **P165** LDAP 策略服务器通过 PolicyView 下发策略，交换机按 aaa ldap-server 系列配置主机/端口/检索库/SSL。<<<PAGE 1175>>>（章 Server Overview，34-3 页附近）

## Access Guardian/UNP（Ch35）

- **P166** Access Guardian=认证+设备合规+访问控制框架：认证→分类→角色访问→限制/阻断四步。<<<PAGE 1212>>>
- **P167** 认证路径：802.1X(EAP over RADIUS) 用于 supplicant；MAC 认证用于非 supplicant（MAC 作 username/password 送 RADIUS）。<<<PAGE 1213>>>
- **P168** 认证失败或无 profile 返回时回落到 UNP 端口默认 profile 与分类规则。<<<PAGE 1213>>>
- **P169** UNP 分类规则基于端口/设备属性（源 MAC、domain ID、IP 等），无需认证。<<<PAGE 1213>>>
- **P170** profile 属性（VLAN/service 映射、QoS policy list 等）应用于划入该 profile 的设备流量。<<<PAGE 1210>>>
- **P171** bridge 口走 VLAN profile、access 口走 service profile；先配 RADIUS→profile→映射→分类规则→端口→认证/分类使能→默认 profile 的标准次序。<<<PAGE 1211>>>
- **P172** MAC 会话定时器决定登录后会话保持时长（默认 12 小时）。<<<PAGE 1210>>>

## AppMon/AFP（Ch36/37）

- **P173** AppMon 以 DPI 签名实时识别应用流，施加应用级 QoS 标记与安全策略。<<<PAGE 1431>>>
- **P174** AppMon 组件链：签名 kit 文件→应用池→应用列表（按名或组）→应用组→QoS 策略。<<<PAGE 1431>>>
- **P175** 监控流程：端口采样→签名匹配→更新流数据库→应用记录；强制流程再叠加 QoS 执行。<<<PAGE 1432>>>
- **P176** AFP 用 REGEX 签名（/flash/app-signature/app-regex.txt）匹配采样 IP 包，命中即生成多组分类器入库并联动 QoS/trap/UNP 列表。<<<PAGE 1457>>>
- **P177** AFP 默认全局使能但所有端口禁用；端口使能才触发采样。<<<PAGE 1457>>>

## 认证服务器（Ch38）

- **P178** AAA 服务器矩阵：RADIUS（管理访问除 SNMP+端口准入均支持）、TACACS+（含 SNMP，不支持端口准入）、LDAP（含 SNMP，不支持端口准入）。<<<PAGE 1475>>>
- **P179** 每台服务器可配一台同型备份；每种认证方式可列跨类型备份列表；交换机用第一台可用服务器，找不到用户即失败（不自动轮询下台）。<<<PAGE 1475>>>
- **P180** 管理访问的权限（授权）优先从服务器取，未配置则回落本地用户库。<<<PAGE 1475>>>

## 端口映射（Ch39）

- **P181** 端口映射会话把源口流量复制到目的口，可单向/双向、可禁未知单播泛洪（章 Quick Steps）。<<<PAGE 1503>>>（39-3 页附近）

## LPS（Ch40）

- **P182** LPS 限制端口源 MAC 学习：学习窗口时长+最大 bridged/filtered 数量+授权 MAC 范围。<<<PAGE 1536>>>
- **P183** 违规处理三选一：阻断违规流量/停止学习/管理关闭端口。<<<PAGE 1536>>>
- **P184** 学习窗口全局生效不能按口配；窗口关闭时动态 MAC 可转静态或伪静态（不老化不 flush 不存 running-config）。<<<PAGE 1536>>>
- **P185** MAC 四类型：static/pseudo-static/dynamic bridged/dynamic filtered；bridged 满后新地址按 filtered 学。<<<PAGE 1537>>>
- **P186** LPS 支持 fixed/802.1Q/UNP/SAP 口，不支持 linkagg 及成员口。<<<PAGE 1536>>>

## 诊断（Ch41）

- **P187** 端口镜像会话=source+destination+可选 unblocked-vlan（防 STP 变化中断镜像）。<<<PAGE 1558>>>
- **P188** sFlow 三件套：receiver（IP/端口/超时）+sampler（采样率/头长）+poller（轮询间隔）；默认 UDP 6343、datagram 1400 字节、版本 5。<<<PAGE 1561>>>
- **P189** 端口监控（port-monitoring）持久会话落盘数据文件（默认 64K、可覆盖、capture brief）。<<<PAGE 1559>>>
- **P190** Switch Health 通过资源阈值+采样间隔监控 CPU/内存等并出统计。<<<PAGE 1566>>>（41-12 页附近）

## VLAN Stacking（Ch42）

- **P191** QinQ 组件：PE bridge/transit bridge/SVLAN 隧道/NNI/UNI；SVLAN tag 附加在全部客户流量上透明穿越城域网。<<<PAGE 1606>>>
- **P192** 隧道 ID 与 VLAN ID 一一对应，创建隧道即向 VLAN Manager 建同名 VLAN："tunnel and VLAN are interchangeable terms." <<<PAGE 1608>>>
- **P193** 封装两法：double tagging（外插 SVLAN 成双 tag）与 VLAN translation（替换 CVLAN 为 SVLAN）。<<<PAGE 1608>>>

## 日志（Ch43）

- **P194** 日志体系：级别筛选+输出设备（console/memory/remote...)+文件大小+格式+存储上限（章 Commands Overview）。<<<PAGE 1580>>>（43-3 页附近）

## Service OAM/CFM（Ch44）

- **P195** Service OAM(802.1ag/Y.1731) 管端到端业务实例，Link OAM(802.3ah) 管单链路，二者互补定位故障。<<<PAGE 1655>>>
- **P196** MD 分层 0-7：5-7 客户、3-4 运营商、0-2 操作员；MEP 发起 OAM 命令防域间泄漏，MIP 被动应答。<<<PAGE 1655>>>
- **P197** 机制：CC 连续性检查/loopback/linktrace；RFP 把连通故障事件传播到 MEP 所在接口。<<<PAGE 1655>>>

## EFM LINK OAM（Ch45）

- **P198** 802.3ah 用慢协议 OAMPDU 承载控制与状态，单链路传递不被网桥转发。<<<PAGE 1673>>>
- **P199** 发现阶段交换能力与配置，仅当双方 loopback/链路检测/链路事件设置匹配才建立 OAM 连接；5 秒无 OAMPDU 即失联（keepalive）。<<<PAGE 1674>>>
- **P200** 功能集：发现/链路监控（errored frame 等三窗口阈值）/远端故障检测/远端环回定位。<<<PAGE 1673>>>

## PPPoE-IA（Ch47）

- **P201** PPPoE-IA 在接入交换机为 PPPoE 发现报文插入 VSA（电路信息）标识用户线路："PPPoE-IA is a means by which the discovery packets of PPPoE are tagged at the access switch ... using Vendor Specific Attributes (VSA)." <<<PAGE 1714>>>
- **P202** access loop 标识：直连用户=chassis/slot/port，多用户共享口=端口+CVLAN 组合。<<<PAGE 1714>>>
- **P203** 全局与端口两级都必须使能 PPPoE-IA 才生效；参数配置与使能状态解耦。<<<PAGE 1715>>>

## SAA（Ch48）

- **P204** SAA 以 SPB 会话做服务保障测量，可生成 XML 历史文件（章 Overview/Configuring）。<<<PAGE 1700>>>（48-4 页附近）

---
合计：204 条（P1-P204）。
