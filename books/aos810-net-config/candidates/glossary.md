# glossary — 术语表（OmniSwitch AOS 8.10R4 Network Configuration Guide）

格式：`- **术语**：中文解释 <<<PAGE N>>>`（页码为 fulltext.md 真实标记；解释据原书语境整理）

## 端口与物理层（Ch1-2）

- **Autonegotiation（自协商）**：链路两端自动协商速率/双工/流控的机制，关闭后 auto 参数失效 <<<PAGE 56>>>
- **Crossover/MDI/MDIX**：直通/交叉线序模式；MDIX 为交换机侧标准，MDI 为终端侧标准 <<<PAGE 56>>>
- **Duplex Mode（双工模式）**：full/half/auto，全双工可同时收发 <<<PAGE 57>>>
- **Link Trap（链路 Trap）**：端口状态变化时向网管站发送的 SNMP 通告 <<<PAGE 57>>>
- **Port Alias（端口别名）**：单端口描述字符串，含空格需引号 <<<PAGE 58>>>
- **Max Frame Size（最大帧长）**：端口可转发最大字节数（如 9216 巨帧） <<<PAGE 58>>>
- **DDM（数字诊断监控）**：读取光模块 EEPROM 的温度/电压/电流/收发光功率与阈值 <<<PAGE 58>>>
- **Flood Rate Limiting（泛洪限速/风暴控制）**：对 bcast/uucast/mcast 分别按 mbps/pps/百分比限速，超限丢包 <<<PAGE 59>>>
- **Low Threshold（低阈值自动恢复）**：违规速率回落后端口自动退出 STORM violated 状态 <<<PAGE 59>>>
- **PAUSE Frame（流控帧）**：全双工下临时抑制对端发送的 802.3x 帧，tx/rx/tx-and-rx 三种姿态 <<<PAGE 60>>>
- **EPP（增强端口性能）**：特定平台的端口性能优化开关 <<<PAGE 61>>>（1-8 页）
- **EEE（节能以太网，802.3az）**：空闲链路低功耗模式 <<<PAGE 61>>>（1-10 页）
- **Split-Mode（分离模式）**：将端口拆分为多个低速端口的形态 <<<PAGE 61>>>（1-10 页）
- **Breakout（分支模式）**：高速端口拆分为多端口的接口形态 <<<PAGE 61>>>（1-10 页）
- **Combo Port（组合口）**：共享 PHY 的光/电复用端口 <<<PAGE 62>>>（1-12 页）
- **TDR（时域反射电缆诊断）**：发测试脉冲定位铜缆断点/长度/阻抗异常 <<<PAGE 66>>>（1-14 页）
- **Violation Recovery（违规恢复）**：特性关停端口的统一恢复机制（手动/定时/次数/wait-to-restore/trap） <<<PAGE 69>>>
- **Wait-to-Restore Timer**：端口恢复后延迟通知特性的稳定等待定时器 <<<PAGE 69>>>
- **Link Monitoring（链路监控）**：按窗口监测端口错误与翻动并可自动关停 <<<PAGE 74>>>（1-21 页）
- **LFP（链路故障传播）**：把远端/对侧故障传播到本地接口触发关停 <<<PAGE 78>>>（1-25 页）
- **PTP（IEEE 1588 精确时间协议）**：端口时间戳与 peer-to-peer 透明时钟 <<<PAGE 79>>>（1-28 页）
- **MACsec（介质访问控制安全，802.1AE）**：以太链路点到点加密/认证/防重放 <<<PAGE 83>>>
- **SecTag**：MACsec 帧中 8/16 字节头，含解密密钥信息、包号、安全信道标识 <<<PAGE 83>>>
- **SCI（安全信道标识）**：标识单向发送/接收安全信道 <<<PAGE 83>>>
- **SA/SAK（安全关联/安全关联密钥）**：SA 持有 AN 编号密钥与包号；SAK 为会话密钥 <<<PAGE 83>>>
- **MKA（MACsec 密钥协商，802.1X-2010）**：协商生成并周期轮换 SAK 的协议 <<<PAGE 84>>>
- **CAK/CKN**：连通性关联密钥及其名称，PSK 或 EAP 派生，保护控制面 <<<PAGE 84>>>
- **Key Server（密钥服务器）**：MKA 选出的生成分发 SAK 的节点 <<<PAGE 84>>>
- **WAN MACsec**：面向广域链路的 MACsec 应用形态 <<<PAGE 87>>>（1-36 页）
- **UDLD（单向链路检测）**：二层协议检测光纤/铜缆单向链路并关停端口 <<<PAGE 98>>>
- **Normal/Aggressive Mode（UDLD 模式）**：正常模式仅显式证据关停；激进模式超时即关停（推荐仅点对点） <<<PAGE 98>>>
- **Echo Detection（回声检测）**：UDLD 学习到新邻居后的请求-回应验证窗口机制 <<<PAGE 99>>>
- **Probe-Timer/Echo-Wait-Timer**：UDLD 探测周期与回声等待定时器 <<<PAGE 100>>>（2-7 页）

## MAC 学习与 VLAN（Ch3-5）

- **Source Learning（源学习）**：从数据帧源 MAC 构建 MAC 表 <<<PAGE 105>>>
- **Static MAC（静态 MAC）**：手工绑定端口+VLAN 的永久地址，bridging/filtering 两种行为 <<<PAGE 105>>>
- **Filtering MAC**：静态 MAC 的丢弃行为，用于阻断攻击 <<<PAGE 105>>>
- **MAC Aging Time（MAC 老化时间）**：动态表项老化周期 <<<PAGE 108>>>（3-7 页）
- **VLAN ID/VID**：802.1Q 唯一标识 VLAN 的编号 <<<PAGE 115>>>
- **VPA（VLAN 端口关联）**：端口与 VLAN 的成员关系记录 <<<PAGE 115>>>
- **Default VLAN（默认 VLAN）**：端口无 tag 流量归属的 VLAN，出厂全口在 VLAN 1 <<<PAGE 115>>>
- **802.1Q Tagging（打标/Trunking）**：4 字节标签携带 VID+优先级，单链多 VLAN <<<PAGE 118>>>
- **Tagged/Untagged Port**：按 VID 打标转发 / 无标转发的成员模式 <<<PAGE 118>>>
- **VLAN IP Interface（VLAN 路由接口）**：绑定 VLAN 的三层接口 <<<PAGE 121>>>（4-10 页）
- **PVLAN（私有 VLAN）**：主 VLAN+isolated/community 二级 VLAN 的子域隔离 <<<PAGE 128>>>
- **Promiscuous Port（混杂口）**：PVLAN 主 VLAN 的上联/互通口 <<<PAGE 128>>>
- **Isolated/Community VLAN（隔离/团体二级 VLAN）**：isolated 成员彼此隔离；community 成员互通 <<<PAGE 128>>>
- **ISL Port（PVLAN 互连口）**：跨交换机延伸 PVLAN 域的级联口 <<<PAGE 128>>>
- **HA VLAN（高可用 VLAN）**：把发往单 MAC 的流量复制到多端口的服务器集群 VLAN <<<PAGE 140>>>
- **Server Cluster（服务器集群）**：L2/L3 两种模式，多实例共享请求算法 <<<PAGE 140>>>
- **Virtual MAC（虚 MAC）**：集群对外的虚拟地址（如 00:95:2a:05:ff:4a 例） <<<PAGE 141>>>

## 生成树（Ch6）

- **STP/RSTP/MSTP**：802.1D/802.1w/802.1Q-2005 三代生成树 <<<PAGE 157>>>
- **Root Bridge（根桥）**：全网选举的树根，最低桥 ID 者当选 <<<PAGE 157>>>
- **Root Path Cost（根路径成本）**：到根最优路径端口成本之和 <<<PAGE 157>>>
- **Designated Bridge/Port（指定桥/指定口）**：为 LAN 提供到根最短路径的桥及其端口 <<<PAGE 158>>>
- **Root Port（根口）**：本桥到根成本最低的口，根桥无根口 <<<PAGE 158>>>
- **Alternate/Backup Port（替代/备份口）**：802.1w 区分的两种阻塞角色口 <<<PAGE 158>>>
- **BPDU（桥协议数据单元）**：承载桥 ID/根 ID/成本等拓扑计算信息的二层帧 <<<PAGE 159>>>（6-7 页）
- **Bridge Priority（桥优先级）**：与 MAC 合成桥 ID 决定根选举 <<<PAGE 161>>>（6-29 页）
- **Hello Time/Max-Age/Forward Delay**：BPDU 周期、信息老化、端口状态迁移延迟三参数 <<<PAGE 161>>>（6-30 页）
- **Flat Mode（扁平模式）**：整交换机单棵树的 STP 运行模式 <<<PAGE 164>>>
- **Per-VLAN Mode（每 VLAN 模式）**：AOS 私有的每 VLAN 一棵树模式 <<<PAGE 164>>>
- **PVST+（每 VLAN 生成树+）**：与 Cisco PVST+ 互通的模式 <<<PAGE 173>>>（6-23 页）
- **MSTI（多生成树实例）**：VLAN 集合映射到的独立树实例，Flat 模式下最多 16 个+CIST <<<PAGE 164>>>
- **MST Region（MST 区域）**：区域名+revision+VLAN 映射一致的交换机组，对外呈现单树 <<<PAGE 167>>>（6-16 页）
- **CST/CIST/IST（公共/公共内部/内部生成树）**：MSTP 的层级树概念 <<<PAGE 167>>>（6-17 页）
- **Edge Port（边缘口）**：接终端不参与拓扑计算的口 <<<PAGE 184>>>（6-43 页）
- **Root Guard（根保护）**：限制端口角色的防意外根桥机制 <<<PAGE 184>>>（6-44 页）
- **Loop Guard（环保护）**：防根口因单向故障失守的机制 <<<PAGE 180>>>（6-37 页）
- **TCN（拓扑变更通知）**：拓扑变化通告及其传播限制 <<<PAGE 184>>>（6-44 页）
- **AVC（自动 VLAN 容纳）**：限制 TCN/BPDU 波及范围的特性 <<<PAGE 174>>>（6-33 页）
- **Path Cost Mode（路径成本模式）**：长短两种成本基准 <<<PAGE 174>>>（6-33 页）

## SPB（Ch7）

- **SPB/SPBM（最短路径桥ging/MAC 模式）**：IEEE 802.1aq，ISIS 驱动的最短路径以太网 <<<PAGE 211>>>
- **ISIS-SPB**：带 SPB TLV 扩展的 IS-IS 链路状态协议，建对称 SPT <<<PAGE 211>>>
- **PBB/PBBN（运营商骨干桥/网络，802.1ah）**：MAC-in-MAC 封装与骨干网 <<<PAGE 211>>>
- **BEB（骨干边缘桥）**：学习并封装客户帧的边缘节点 <<<PAGE 211>>>
- **BCB（骨干核心桥）**：只按 BMAC 转发不学客户 MAC 的核心节点 <<<PAGE 211>>>
- **BMAC（骨干 MAC）**：802.1ah 外层目的地址，指向目的 BEB <<<PAGE 212>>>
- **BVLAN（骨干 VLAN）**：SPB 传输 VLAN，不学 MAC 不泛洪 <<<PAGE 211>>>
- **Control BVLAN（控制 BVLAN）**：承载 ISIS-SPB 控制报文的指定 BVLAN <<<PAGE 245>>>
- **I-SID（服务实例标识）**：SPB 服务编号，绑定 BVLAN <<<PAGE 212>>>
- **SAP（服务接入点）**：端口+封装值（CVLAN/0/all）定义的服务接入分类 <<<PAGE 212>>>
- **ECT（等价树算法）**：16 个预定义算法在等价路径间打破平局 <<<PAGE 214>>>
- **SPT（最短路径树）**：每桥以自己为根计算的转发树 <<<PAGE 214>>>
- **SPB Pseudo-Wire（SPB 伪线/E-LINE）**：SPB 上的透明点到点服务 <<<PAGE 218>>>（7-15 页）
- **RFP（远端故障传播）**：把 SPB 服务远端故障传播到本地接口 <<<PAGE 218>>>（7-16 页）
- **IP over SPB / Inline Routing**：基于服务的 L3 VPN 接口形态 <<<PAGE 224>>>（7-19 页）
- **SPB over Shared Ethernet**：SPB 骨干跑在共享/其他网络之上的形态 <<<PAGE 229>>>（7-24 页）
- **SPB In-Band Management**：经 BVLAN 带内管理交换机 <<<PAGE 231>>>（7-26 页）

## 环网与保护（Ch8/12/13）

- **LBD（环回检测）**：周期探测帧检测 L2 环路并关停端口 <<<PAGE 325>>>
- **Remote-origin LBD（远端源环回检测）**：处理远端系统发来的 LBD 帧 <<<PAGE 326>>>
- **Transmission Timer（LBD 传输定时器）**：探测帧发送周期，默认 30 秒 <<<PAGE 325>>>
- **ERP（以太网环保护）**：ITU-T G.8032 环网保护切换 <<<PAGE 395>>>
- **RPL（环保护链路）**：环上被阻塞防环的链路 <<<PAGE 395>>>
- **RPL Owner（RPL 拥有者）**：阻塞/解阻塞 RPL 的指定节点 <<<PAGE 395>>>
- **R-APS（环自动保护切换消息）**：SF/NR/NR,RB 等环状态协议报文 <<<PAGE 395>>>
- **SF/NR（信号失败/无请求）**：环节点状态声明 <<<PAGE 395>>>
- **WTR Timer（等待恢复定时器）**：环恢复后延迟回切的分钟级定时器 <<<PAGE 396>>>
- **Guard Timer（守护定时器）**：丢弃过时 R-APS 的定时器，须大于绕环时延 <<<PAGE 396>>>
- **ERPv2**：支持多环/子环/共享链路/R-APS 虚信道的版本 <<<PAGE 395>>>
- **Sub-ring/Major Ring（子环/主环）**：ERPv2 的环层级 <<<PAGE 399>>>（12-17 页）
- **MRP（介质冗余协议）**：工业环网确定性重构协议 <<<PAGE 426>>>
- **MRM（介质冗余管理器）**：环上控制拓扑的节点，发 MRP_Test <<<PAGE 428>>>
- **MRC（介质冗余客户端）**：响应 MRM 重构帧、转发测试帧 <<<PAGE 428>>>
- **MRA（介质冗余自动管理器）**：可投票竞选 MRM 的角色 <<<PAGE 428>>>
- **Redundancy Domain（冗余域）**：MRP 环的域标识，每域两个环口 <<<PAGE 428>>>
- **Ring-Closed/Ring-Open（环闭合/断开态）**：MRP 正常/故障两种状态 <<<PAGE 426>>>
- **MIM/MIC（MRP 互连管理器/客户端）**：跨环互连域的角色 <<<PAGE 431>>>（13-8 页）

## 聚合与双归（Ch9-11）

- **Link Aggregation（链路聚合）**：多物理链路捆成虚拟链路 <<<PAGE 341>>>
- **Static/Dynamic Aggregate Group（静态/动态聚合组）**：手工/802.3ad LACP 协商两种 <<<PAGE 341>>>
- **LACP/LACPDU**：动态聚合控制协议及其帧 <<<PAGE 352>>>
- **Actor/Partner（本端/对端）**：LACP 两侧角色命名 <<<PAGE 352>>>
- **Linkagg ID**：聚合组编号，VLAN/MAC/QoS 配置的挂载单位 <<<PAGE 341>>>
- **DHL（双归链路）**：Active-Active/Active-Standby 两种双上联保护 <<<PAGE 380>>>（11-3 页）
- **linkA/linkB**：DHL 会话的两条链路 <<<PAGE 382>>>
- **Pre-emption Time（DHL 抢占时间）**：主链恢复后回切等待，默认 30 秒 <<<PAGE 383>>>
- **MAC Flushing（MAC 冲刷）**：DHL 切换时清 MAC 的方式（raw/mvrp） <<<PAGE 382>>>

## MVRP（Ch14）

- **MVRP（多 VLAN 注册协议，802.1ak/MRP 应用）**：动态声明/撤销 VLAN 成员 <<<PAGE 442>>>
- **MRPDU**：MRP 系协议报文 <<<PAGE 442>>>
- **Dynamic VLAN（动态 VLAN）**：由 MVRP 注册学到的 VLAN <<<PAGE 442>>>
- **Applicant Mode（申请者模式）**：端口声明 VLAN 的姿态（normal/active 等） <<<PAGE 446>>>（14-9 页）
- **Registrar Mode（注册者模式）**：端口处理声明的方式（fixed/forbidden/normal） <<<PAGE 446>>>（14-8 页）
- **Leave Timer/Join Timer**：MVRP 注册/注销定时器 <<<PAGE 447>>>（14-10 页）

## MPLS/L2VPN（Ch15-16）

- **MPLS（多协议标签交换）**：32 位标签头逐跳交换的转发技术 <<<PAGE 457>>>
- **Label Stack（标签栈）**：报文可携带多层标签，处理只看栈顶 <<<PAGE 457>>>
- **LSR（标签交换路由器）**：核心按标签转发的路由器 <<<PAGE 457>>>
- **LER（标签边缘路由器）**：压入/弹出标签的边缘节点 <<<PAGE 458>>>
- **LSP（标签交换路径）**：单向的标签隧道，双工需两条 <<<PAGE 457>>>
- **FEC（转发等价类）**：同一 LSP 承载的等价流分组 <<<PAGE 458>>>
- **LDP（标签分发协议）**：UDP hello+TCP 会话分发 FEC-标签绑定 <<<PAGE 458>>>
- **Hello Adjacency（LDP Hello 邻接）**：hello 建立的邻居关系 <<<PAGE 458>>>
- **Targeted Peer（定向对端）**：扩展发现机制找到的非直连 LSR <<<PAGE 458>>>
- **LDP Graceful Restart（LDP 平滑重启）**：CMM 冗余下会话不中断的机制 <<<PAGE 461>>>（15-11 页）
- **LSP Ping/Traceroute**：MPLS 路径连通性诊断 <<<PAGE 460>>>（15-15 页）
- **VPLS（虚拟专用 LAN 服务）**：多点任意互通 L2VPN <<<PAGE 478>>>
- **VPWS（虚拟专用线服务）**：点到点 L2VPN <<<PAGE 478>>>
- **PW（伪线）**：PE 间的仿真链路，VPLS 需全网格 <<<PAGE 478>>>
- **CE/PE（客户/运营商边缘）**：VPN 业务边界设备 <<<PAGE 478>>>
- **Attachment Circuit（接入电路）**：CE-PE 间的物理/逻辑链路 <<<PAGE 478>>>
- **Split Horizon（水平分割，PW）**：PW 收到的包不再从 PW 发出 <<<PAGE 478>>>
- **BGP VPLS Auto-discovery**：BGP 自动发现 VPLS 成员免去手工配置 <<<PAGE 480>>>
- **SDP（服务分发点）**：MPLS/GRE 隧道端点抽象，服务绑定单位 <<<PAGE 528>>>（16-19 页）
- **Route Reflector（路由反射器）**：减少 BGP full-mesh 的集中反射节点 <<<PAGE 480>>>

## VXLAN/EVPN（Ch17-18）

- **VXLAN（虚拟可扩展 LAN）**：MAC-in-UDP/IP 叠加网络封装 <<<PAGE 533>>>
- **VNI（VXLAN 网络标识）**：24 位段 ID <<<PAGE 533>>>
- **VTI（VXLAN 隧道接口）**：由 SDP+绑定提供的 UDP 隧道 <<<PAGE 533>>>
- **VTEP（VXLAN 隧道端点）**：封装/解封点，AOS 用 Loopback0 IP 标识 <<<PAGE 533>>>
- **VXLAN Gateway（VXLAN 网关）**：桥接 VXLAN 与传统 VLAN 域的设备 <<<PAGE 533>>>
- **UDP 4789**：VXLAN 默认目的端口（可配） <<<PAGE 535>>>
- **EVPN（以太网 VPN）**：BGP MP-BGP 扩展通告 MAC/IP 可达性 <<<PAGE 583>>>
- **EVI（EVPN 实例）**：跨 PE 的转发/路由实例，含 RD/RT <<<PAGE 583>>>
- **ES/ESI（以太网段/标识）**：多归属链路组及其 10 字节标识 <<<PAGE 583>>>
- **DF/NDF（指定/非指定转发器）**：多归属段上 BUM 转发职责分工 <<<PAGE 583>>>
- **RT-1/2/3/4/5/6/7/8（EVPN 路由类型）**：AD、主机、含组播、ES、前缀、选择性组播、成员报告/离开同步 <<<PAGE 584>>>
- **All-Active Multihoming（全活多归属）**：多 PE 同时转发的冗余模型 <<<PAGE 583>>>
- **Aliasing（别名）**：非 DF PE 也通告可达性实现负载分担 <<<PAGE 585>>>
- **IRB（集成路由桥接）**：叠加网 L2/L3 一体转发 <<<PAGE 595>>>
- **Asymmetric/Symmetric IRB（非对称/对称 IRB）**：是否经 fabric-vpn 集中路由的两种模型 <<<PAGE 595>>>（18-17 页）
- **DAG（分布式任播网关）**：各叶节点同 IP/MAC 的网关 <<<PAGE 601>>>（18-27 页）
- **OISM（优化子网间组播）**：叠加网跨子网组播优化 <<<PAGE 604>>>（18-32 页）
- **MAC Mobility（MAC 移动性）**：主机迁移的序列号仲裁机制 <<<PAGE 606>>>（18-36 页）
- **BUM Traffic（广播/未知单播/组播）**：需要泛洪处理的流量类别 <<<PAGE 583>>>
- **Ingress Replication（入向复制）**：以单播复制替代组播的 BUM 分发 <<<PAGE 584>>>
- **RD/RT（路由区分器/目标）**：VPN 路由命名与导入导出控制 <<<PAGE 583>>>
- **Clos-3/Clos-5（三级/五级 Clos）**：叶脊/超脊拓扑模型 <<<PAGE 654>>>（18-76 页）
- **Multi-site/Multi-PoD**：跨数据中心/多 PoD 的 EVPN 部署模型 <<<PAGE 661>>>（18-83 页）

## 二层发现与语音（Ch19-20）

- **802.1AB/LLDP（链路层发现协议）**：邻居能力通告 <<<PAGE 2330>>>（19-4 页）
- **LLDPDU**：LLDP 报文单元 <<<PAGE 2331>>>（19-6 页）
- **TLV（类型长度值）**：mandatory/802.1/802.3/MED/proprietary 各类信息单元 <<<PAGE 2330>>>（19-4 页）
- **LLDP-MED（媒体终端设备）**：语音/策略/位置等媒体扩展 <<<PAGE 2331>>>（19-5 页）
- **Transmit Interval/Hold Multiplier**：LLDP 发送周期与保持倍数 <<<PAGE 2340>>>（19-14 页）
- **SIP Snooping（SIP 监听）**：监听 SIP 会话识别语音流并施 QoS <<<PAGE 2400>>>（20-5 页）
- **Trusted SIP Server（信任 SIP 服务器）**：被监听信任的呼叫控制服务器 <<<PAGE 2401>>>（20-8 页）
- **RTCP/RTP**：媒体传输与质量控制协议，阈值监控 <<<PAGE 2402>>>（20-10 页）
- **SOS Call（紧急呼叫）**：按用户字符串识别并优先标记 <<<PAGE 2401>>>（20-9 页）

## 三层基础（Ch21-23）

- **IP Interface（IP 接口）**：绑定 VLAN 的三层接口 <<<PAGE 709>>>
- **Loopback0 Interface**：VTEP/BGP/管理标识用的环回接口 <<<PAGE 709>>>（21-9 页）
- **Static/Recursive Static Route（静态/递归静态路由）**：手工路由与经下一跳解析的路由 <<<PAGE 709>>>（21-11 页）
- **Default Route（默认路由）**：0.0.0.0/0 兜底路由 <<<PAGE 710>>>（21-12 页）
- **Blackhole Route（黑洞路由）**：显式丢弃路由 <<<PAGE 710>>>（21-13 页）
- **IP Routed Port（路由口）**：按三层口使用的物理端口 <<<PAGE 710>>>（21-14 页）
- **ARP（地址解析协议）**：IP-MAC 映射 <<<PAGE 710>>>（21-14 页）
- **Gratuitous ARP（免费 ARP）**：主动宣告 IP-MAC 的 ARP <<<PAGE 710>>>（21-18 页）
- **Router ID（路由器 ID）**：路由协议标识 <<<PAGE 711>>>（21-20 页）
- **Route Preference（路由优先级）**：路由来源优先级 <<<PAGE 711>>>（21-21 页）
- **TTL（生存时间）**：IP 跳数限制 <<<PAGE 711>>>（21-21 页）
- **Route Map Redistribution（路由图重分发）**：按策略注入路由 <<<PAGE 711>>>（21-21 页）
- **IP-Directed Broadcast（定向广播）**：发往远端网广播地址的包 <<<PAGE 716>>>（21-28 页）
- **DoS Filtering（拒绝服务过滤）**：控制面/转发面攻击过滤 <<<PAGE 717>>>（21-29 页）
- **ICMP**：错误/测试/信息报文协议（ping 依赖） <<<PAGE 712>>>（21-35 页）
- **GRE（通用路由封装）**：IP over IP 隧道封装 <<<PAGE 721>>>（21-40 页）
- **IP-in-IP**：IP 内嵌 IP 的隧道 <<<PAGE 721>>>（21-40 页）
- **Tunnel Interface（隧道接口）**：隧道端点的逻辑接口 <<<PAGE 722>>>（21-42 页）
- **VRF Route Leak（VRF 路由泄露）**：跨 VRF 选择性注入路由 <<<PAGE 712>>>（21-44 页）
- **VRF（虚拟路由转发）**：同机多路由实例隔离 L3 <<<PAGE 756>>>
- **VRF Profile**：VRF 属性模板 <<<PAGE 758>>>（22-7 页）
- **Management VRF（管理 VRF）**：承载管理流量的专用 VRF <<<PAGE 759>>>（22-8 页）
- **IPv6 Link-local Address**：FE80::/10 链路内地址 <<<PAGE 774>>>
- **Unique Local IPv6 Unicast**：FC00::/7 站点本地可路由地址 <<<PAGE 774>>>
- **Anycast**：送达组内最近一员的地址 <<<PAGE 774>>>
- **ND（邻居发现）**：IPv6 的 ARP/RA/重复检测等机制 <<<PAGE 773>>>
- **LPND（本地代理邻居发现）**：代答同网段邻居请求 <<<PAGE 777>>>（23-13 页）
- **RA Filtering（路由通告过滤）**：过滤恶意/多余 RA <<<PAGE 777>>>（23-13 页）
- **NUD（邻居不可达检测）**：邻居可达性验证机制 <<<PAGE 777>>>（23-13 页）
- **Neighbor Cache Limit（邻居缓存上限）**：ND 表项容量控制 <<<PAGE 777>>>（23-13 页）
- **DNSSL/RDNSS**：RA 携带的 DNS 域名后缀/服务器选项 <<<PAGE 799>>>（23-36 页）
- **Prefix64**：RA 中通告的 NAT64 前缀 <<<PAGE 798>>>（23-35 页）
- **JITC Mode**：美军兼容模式，禁 Site-Local 地址 <<<PAGE 774>>>

## IPsec/RIP/BFD（Ch24-26）

- **IPsec**：网络层安全服务体系 <<<PAGE 819>>>
- **ESP（封装安全载荷）**：协议号 50，加密+可选认证 <<<PAGE 820>>>
- **AH（认证头）**：只认证不加密 <<<PAGE 820>>>
- **Transport Mode（传输模式）**：AOS 唯一支持的模式 <<<PAGE 819>>>
- **SPI（安全参数索引）**：32 位 SA 选择符 <<<PAGE 820>>>
- **SA（安全关联）**：SPI+目的地址+协议确定的单向策略实例 <<<PAGE 820>>>
- **AES-CBC/3DES**：加密算法族 <<<PAGE 820>>>
- **HMAC-MD5/HMAC-SHA1**：认证散列算法 <<<PAGE 821>>>（24-7 页）
- **Discard Policy（丢弃策略）**：IPsec 定义的显式丢包策略 <<<PAGE 820>>>（24-9 页）
- **Master Key（IPsec 主密钥）**：SA 密钥体系的根 <<<PAGE 823>>>（24-10 页）
- **RIP（路由信息协议）**：距离向量 IGP，跳数度量 <<<PAGE 842>>>
- **RIPv1/RIPv2**：有类/无类+认证+组播版本 <<<PAGE 843>>>
- **Hold-down Timer（RIP 抑制定时器）**：路由失效前的怀疑期 <<<PAGE 842>>>
- **Forced Hold-Down**：强制抑制区间 <<<PAGE 842>>>（25-9 页）
- **SHA256 Authentication（RIPv2）**：强认证选项 <<<PAGE 844>>>（25-18 页）
- **BFD（双向转发检测）**：毫秒级转发面故障检测 <<<PAGE 869>>>
- **Asynchronous Mode/Echo Function（BFD 模式）**：控制包/回声两种检测 <<<PAGE 870>>>
- **Detect Time Multiplier**：检测倍数，超时=倍数×最小接收间隔 <<<PAGE 869>>>
- **BFD Session（BFD 会话）**：两邻接系统间的检测实例 <<<PAGE 869>>>

## DHCP/SLB（Ch27-30）

- **DHCP Relay（DHCP 中继）**：跨网段转发 DHCP 的代理，UDP 67/68 <<<PAGE 903>>>
- **Forward Delay/Maximum Hops**：中继转发时延与跳数上限校验 <<<PAGE 903>>>
- **Per-interface Mode（按接口中继模式）**：每个 IP 接口独立中继配置 <<<PAGE 903>>>
- **Generic UDP Relay（通用 UDP 中继）**：按端口转 UDP 到 VLAN/service/IP <<<PAGE 904>>>
- **Option-82（中继代理信息选项）**：插入电路/远程标识的 DHCP 选项 <<<PAGE 911>>>（27-22 页）
- **Circuit ID/Remote ID**：Option-82 的两个子选项 <<<PAGE 926>>>
- **DHCP Snooping（DHCP 窥探）**：过滤非法 DHCP 报文并建绑定表 <<<PAGE 925>>>
- **Trusted Port（信任口）**：允许服务器报文的口 <<<PAGE 925>>>
- **Binding Table（绑定表）**：MAC-IP-端口-租期绑定数据库 <<<PAGE 926>>>
- **DHCPv6 Relay/Snooping**：IPv6 对应的中继与窥探 <<<PAGE 917>>>（27-35 页）
- **ISF（IPv6 源过滤）**：按绑定表校验源地址 <<<PAGE 921>>>（27-41 页）
- **IPv6 DHCP Guard**：过滤非法 RA/DHCPv6 报文 <<<PAGE 922>>>（27-44 页）
- **Policy File（DHCP 服务器策略文件）**：地址池/选项策略定义 <<<PAGE 893>>>（28-6 页）
- **DHCP Server Database file**：租期持久化数据库 <<<PAGE 896>>>（28-10 页）
- **VitalQIP Server**：可对接的 IP 地址管理系统 <<<PAGE 894>>>（28-4 页）
- **VRRP（虚拟路由器冗余协议）**：默认网关冗余 <<<PAGE 979>>>
- **VRID（虚拟路由器 ID）**：虚拟路由器编号 <<<PAGE 979>>>
- **Virtual Router Master/Backup（主/备虚拟路由器）**：转发者与候补 <<<PAGE 979>>>
- **IP Address Owner（IP 地址拥有者）**：虚拟 IP 即其接口 IP 的路由器，必为 master <<<PAGE 980>>>
- **VRRP Advertisement（VRRP 通告）**：master 发往 224.0.0.18 的组播 <<<PAGE 980>>>
- **Skew Time**：(256-优先级)/256，防同时抢主的退避 <<<PAGE 980>>>
- **Preemption（抢占）**：高优先级 backup 抢占 master <<<PAGE 980>>>
- **Accept Mode（接受模式）**：backup 是否响应虚拟 IP 流量 <<<PAGE 987>>>（29-17 页）
- **VRRP Tracking（VRRP 跟踪）**：监控对象降优先级的策略 <<<PAGE 993>>>（29-24 页）
- **SLB（服务器负载均衡）**：集群虚拟化分发请求 <<<PAGE 1012>>>
- **VIP（虚拟 IP）**：集群对外 IP 标识 <<<PAGE 1012>>>
- **Condition Cluster（条件集群）**：以 QoS 条件标识的集群 <<<PAGE 1012>>>
- **WRR（加权轮询）**：按权重分配请求的分发算法 <<<PAGE 1012>>>（30-8 页）
- **Server Health Monitoring（服务器健康监测）**：ping 探测集群成员活性 <<<PAGE 1015>>>（30-9 页）
- **SLB Probe（SLB 探测）**：自定义健康探测 <<<PAGE 1021>>>（30-17 页）

## 组播（Ch31-32）

- **IPMS（IP 组播交换）**：IGMP 驱动的二层组播 <<<PAGE 1032>>>
- **IPMSv6/MLD**：IPv6 组播侦听者发现 <<<PAGE 1045>>>（31-30 页）
- **Multicast Group Address（组播组地址）**：D 类 224/4，239/8 管理域 <<<PAGE 1032>>>
- **IGMP Querier（IGMP 查询者）**：定期查询成员的设备，最低 IP 当选 <<<PAGE 1033>>>
- **IGMP Version 1/2/3**：组成员管理协议版本 <<<PAGE 1036>>>（31-13 页）
- **IGMP Static Group/Querier（静态组/查询者）**：手工配置的组播状态 <<<PAGE 1036>>>（31-14/15 页）
- **IGMP Robustness Variable（健壮性变量）**：报文重发系数 <<<PAGE 1043>>>（31-26 页）
- **IGMP Spoofing/Zapping**：伪装报文防御/快速换台优化 <<<PAGE 1044>>>（31-27/28 页）
- **PIM-SM/PIM-DM（协议无关组播稀疏/密集模式）**：组播路由协议 <<<PAGE 1033>>>
- **DVMRP（距离向量组播路由协议）**：另一种组播路由协议 <<<PAGE 1033>>>
- **IPMSR（IP 组播交换与路由）**：IPMS+组播路由的组合 <<<PAGE 1033>>>
- **IPMVLAN（IP 组播 VLAN）**：专用组播分发 VLAN <<<PAGE 1086>>>
- **MVR（组播 VLAN 注册）**：多用户 VLAN 共享单一组播 VLAN <<<PAGE 1086>>>
- **Sender/Receiver Port（发送/接收口）**：IPMVLAN 的源口（NNI，唯一）与收听口 <<<PAGE 1087>>>
- **Enterprise/VLAN Stacking Mode（IPMVLAN 模式）**：面向普通口/QinQ 口两种模式 <<<PAGE 1086>>>

## QoS（Ch33）

- **QoS（服务质量）**：按流差异化转发的机制总称 <<<PAGE 1103>>>
- **Classification（分类）**：识别流并指派 CoS <<<PAGE 1105>>>
- **CoS（服务等级）**：0-7 优先级值 <<<PAGE 1105>>>
- **IP Precedence/ToS**：3 位优先级/服务类型字段 <<<PAGE 1105>>>
- **DSCP/PHB（差分服务码点/每跳行为）**：6 位码点及其转发行为 <<<PAGE 1105>>>
- **802.1p Priority**：以太标签 TCI 中的 3 位优先级 <<<PAGE 1105>>>
- **Trusted Port（QoS 信任口）**：采信报文已有标记的口 <<<PAGE 1108>>>（33-9 页）
- **Queue Set/QSet Profile（队列集/模板）**：每口队列调度参数组 <<<PAGE 1114>>>（33-11/13 页）
- **Congestion Management/Avoidance（拥塞管理/避免）**：排队调度与随机丢弃 <<<PAGE 1103>>>
- **Lossless TC（无损流量类）**：PFC 支撑的不丢类 <<<PAGE 1120>>>（33-20 页）
- **PFC（基于优先级的流控）**：按优先级暂停的无损机制 <<<PAGE 1120>>>（33-20 页）
- **ECN（显式拥塞通知）**：标记而非丢包的拥塞告知 <<<PAGE 1161>>>（33-91 页）
- **Policing/Shaping（限速/整形）**：丢弃式/缓存式速率控制 <<<PAGE 1124>>>（33-24 页）
- **Tri-Color Marking（三色标记）**：sr/tcm 双速/单速三色限速 <<<PAGE 1125>>>（33-25 页）
- **Policy Condition/Action/Rule（策略条件/动作/规则）**：策略三元组 <<<PAGE 1133>>>
- **Policy List（策略列表）**：default/UNP/egress/AFP 四类规则组 <<<PAGE 1134>>>
- **qos apply**：策略生效的提交命令 <<<PAGE 1147>>>
- **Condition Group（条件组）**：network/service/MAC/port group 地址组 <<<PAGE 1169>>>（33-59 页）
- **Map Group（映射组）**：标记映射表 <<<PAGE 1176>>>（33-66 页）
- **ACL（访问控制列表）**：L2/L3/IPv6/组播过滤型策略 <<<PAGE 1142>>>（33-69 页）
- **TCAM Profile（TCAM 模板）**：硬件查表分区方案 <<<PAGE 1151>>>（33-78 页）
- **Policy Based Routing（策略路由）**：按策略改下一跳 <<<PAGE 1153>>>（33-87 页）
- **Policy Based Mirroring（策略镜像）**：按策略多目的镜像 <<<PAGE 1151>>>（33-85 页）

## 准入与应用识别（Ch34-38）

- **LDAP Policy Server（LDAP 策略服务器）**：集中下发 QoS 策略的目录服务器 <<<PAGE 1175>>>（34-3 页）
- **PolicyView**：ALE 的策略管理应用 <<<PAGE 1133>>>
- **Access Guardian（准入卫士）**：认证+合规+访问控制框架 <<<PAGE 1212>>>
- **UNP（通用网络剖面）**：按设备属性动态套用 VLAN/service/QoS 的框架 <<<PAGE 1213>>>
- **UNP Profile（UNP 剖面）**：属性集合（VLAN/service 映射、QoS 列表等） <<<PAGE 1210>>>
- **UNP Classification Rules（UNP 分类规则）**：MAC 范围/IP/端口等无认证分类 <<<PAGE 1211>>>
- **UNP Port Type（bridge/access）**：VLAN 域或 service 域接入形态 <<<PAGE 1211>>>
- **UNP Dynamic SAP**：认证/分类结果动态生成的 SAP <<<PAGE 1246>>>（35-34 页）
- **802.1X/Supplicant（请求者）**：基于端口的网络接入控制与客户端 <<<PAGE 1213>>>
- **MAC Authentication（MAC 认证）**：以 MAC 作用户名密码的认证 <<<PAGE 1213>>>
- **EAP/EAP-TLS/PEAP**：可扩展认证协议及双向认证框架 <<<PAGE 1213>>>
- **Captive Portal（强制门户）**：Web 重定向认证 <<<PAGE 1313>>>（35-101 页）
- **CPPM/UPAM（ClearPass/统一策略管理器）**：外部策略服务器 <<<PAGE 1212>>>
- **BYOD（自带设备）**：访客/个人设备准入方案 <<<PAGE 1233>>>（35-172 页）
- **mDNS/SSDP**：苹果/Windows 即插即用发现协议 <<<PAGE 1241>>>（35-185/186 页）
- **IoT Device Profiling（物联网设备画像）**：本地签名库设备识别 <<<PAGE 1281>>>（35-220 页）
- **QMR（隔离管理与修复）**：Quarantine Manager and Remediation <<<PAGE 1266>>>（35-9 页）
- **OmniAccess Stellar AP Integration**：无线 AP 发现/隧道集成 <<<PAGE 1363>>>（35-114 页）
- **L2 GRE Tunneling（二层 GRE 隧道）**：AP 流量二层延伸 <<<PAGE 1377>>>（35-127 页）
- **Switch Supplicant（交换机请求者）**：交换机自身 802.1X 客户端+X509 证书 <<<PAGE 1468>>>（35-144 页）
- **Router Domain Authentication（路由域认证）**：对路由器接入的认证 <<<PAGE 1364>>>（35-94 页）
- **AppMon（应用监控与强制）**：DPI 签名识别应用并施加 QoS/安全 <<<PAGE 1431>>>
- **Application Signature Kit（应用签名包）**：应用特征库文件 <<<PAGE 1431>>>
- **Application List/Group（应用列表/组）**：监控对象集合 <<<PAGE 1431>>>
- **Threat-Insight**：AppMon 内的威胁监控/强制 <<<PAGE 1449>>>（36-22 页）
- **AFP（应用指纹识别）**：REGEX 签名识别应用 <<<PAGE 1457>>>
- **REGEX Signature File**：/flash/app-signature/app-regex.txt <<<PAGE 1457>>>
- **AFP Mode（AFP 模式）**：端口级采样识别模式 <<<PAGE 1458>>>（37-6 页）
- **AAA Server（认证授权计费服务器）**：RADIUS/TACACS+/LDAP <<<PAGE 1475>>>
- **RADIUS**：最通用 AAA 协议，唯一支持端口准入 <<<PAGE 1475>>>
- **TACACS+**：含 SNMP 管理访问的 AAA 协议 <<<PAGE 1475>>>
- **RADIUS over TLS/RADSEC**：加密 RADIUS 传输 <<<PAGE 1488>>>（38-18 页）
- **RADIUS Health Check**：服务器活性探测 <<<PAGE 1488>>>（38-18 页）
- **Kerberos Snooping**：监听 Kerberos 票据识别用户 <<<PAGE 1525>>>（38-50 页）
- **PKI/PKIX-SSH**：证书体系与证书 SSH 管理 <<<PAGE 1518>>>（38-43/46 页）

## 诊断与运维（Ch39-48）

- **Port Mapping（端口映射）**：流量复制到诊断口的会话 <<<PAGE 1503>>>（39-3 页）
- **LPS（学习型端口安全）**：限窗限量的源 MAC 学习控制 <<<PAGE 1536>>>
- **LPS Learning Window（LPS 学习窗口）**：全局学习时限 <<<PAGE 1536>>>
- **Pseudo-static MAC（伪静态 MAC）**：不老化不落 running-config 的学习地址 <<<PAGE 1537>>>
- **Security Violation Mode（违规模式）**：block/停止学习/admin-down 三选一 <<<PAGE 1541>>>（40-20 页）
- **Packet Relay（包中继）**：LPS 口上中继违规报文 <<<PAGE 1542>>>（40-21 页）
- **Port Mirroring（端口镜像）**：复制流量到分析口 <<<PAGE 1558>>>
- **Remote Port Mirroring/RPMIR（远程镜像）**：跨交换镜像 <<<PAGE 1564>>>（41-16/21 页）
- **Unblocked VLAN（镜像豁免 VLAN）**：防 STP 阻断镜像会话 <<<PAGE 1558>>>
- **Port Monitoring（端口监控）**：落盘抓包会话 <<<PAGE 1559>>>
- **sFlow**：采样流统计协议（receiver/sampler/poller） <<<PAGE 1561>>>
- **RMON（远程监控）**：SNMP 探针统计 <<<PAGE 1567>>>（41-11 页）
- **Switch Health（交换机健康）**：资源阈值与采样监控 <<<PAGE 1566>>>
- **VLAN Stacking/QinQ**：外层 SVLAN 隧道客户流量 <<<PAGE 1606>>>
- **SVLAN/CVLAN（业务/客户 VLAN）**：外层/内层标签 <<<PAGE 1606>>>
- **PE/Transit Bridge（运营商边缘/中转桥）**：QinQ 隧道端点与核心 <<<PAGE 1606>>>
- **NNI/UNI（网络侧/用户侧接口）**：QinQ 网络口与客户口 <<<PAGE 1606>>>
- **UNI Profile（UNI 模板）**：UNI 口封装行为模板 <<<PAGE 1616>>>（42-20 页）
- **Double Tagging/VLAN Translation**：双打标/标签替换两种 QinQ 封装法 <<<PAGE 1608>>>
- **Wire-Rate Hardware Loopback Test**：线速硬件环回测试 <<<PAGE 1615>>>（42-33 页）
- **Switch Logging（交换机日志）**：级别/设备/格式/上限可配的日志体系 <<<PAGE 1580>>>（43-3 页）
- **Readable Customer Event Logs**：面向客户的可读事件日志 <<<PAGE 1583>>>（43-9 页）
- **Ethernet Service OAM/CFM（802.1ag/Y.1731）**：端到端业务运维体系 <<<PAGE 1655>>>
- **MD/MA/MEP/MIP（维护域/关联/端点/中间点）**：CFM 层级组件 <<<PAGE 1655>>>
- **MD Level（维护域级别 0-7）**：运营商 0-2、提供商 3-4、客户 5-7 <<<PAGE 1655>>>
- **EVC（以太网虚连接）**：卖给客户的服务实例（UNI+VLAN） <<<PAGE 1655>>>
- **CC/LBM/LBR/LTM/LTR（连续性检查/环回/链路追踪）**：CFM 机制族 <<<PAGE 1655>>>
- **Frame Delay Measurement（帧时延测量）**：Y.1731 性能测量 <<<PAGE 1665>>>（44-13 页）
- **Virtual MEP（虚拟 MEP）**：虚拟端口上的 UP MEP <<<PAGE 1655>>>
- **EFM LINK OAM（802.3ah）**：单链路运维协议 <<<PAGE 1673>>>
- **OAMPDU**：LINK OAM 慢协议报文 <<<PAGE 1673>>>
- **Remote Loopback（远端环回）**：对端环回测试定位故障 <<<PAGE 1673>>>
- **Errored Frame/Frame Seconds Summary**：链路监控的三类错误窗口 <<<PAGE 1673>>>
- **CPE Test Head（CPE 测试头）**：L2 SAA 性能测试框架 <<<PAGE 1690>>>（46-5 页）
- **L2 SAA Test**：二层服务保障测试 <<<PAGE 1693>>>（46-9 页）
- **CPE Test Group（CPE 测试组）**：批量测试调度 <<<PAGE 1710>>>（46-13 页）
- **PPPoE-IA（PPPoE 中间代理）**：插入线路标识 VSA 的接入代理 <<<PAGE 1714>>>
- **PAD 消息（PPPoE 主动发现）**：PADI/PADO/PADR/PADS 族 <<<PAGE 1714>>>
- **Access Node/Access Loop（接入节点/接入环）**：IA 所在交换机与用户物理线路 <<<PAGE 1714>>>
- **Circuit ID/Remote ID**：PPPoE-IA 插入的线路/远端标识 <<<PAGE 1715>>>
- **SAA（服务保障代理）**：SPB 会话质量测量+XML 历史 <<<PAGE 1700>>>（48-4 页）

---
合计：约 260 条（按章分组）。
