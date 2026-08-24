# glossary 候选 — DT00XTE216 OmniSwitch LAN Core Switching (Edition 15)

> 术语 | 中文解释 | 首次出现页码（聚焦本书核心专题：ERP/MACsec/PVLAN/MSTP/MVRP/安全/OSPF/路由重分发/组播/SPB）

## ERP / 环网

| 术语 | 解释 | 页码 |
|---|---|---|
| ERP (Ethernet Ring Protection) | 以太网环网保护协议，环内防环并实现约 50ms 快速故障恢复 | <<<PAGE 37>>> |
| RPL (Ring Protection Link) | 环保护链路，环内正常状态下被阻塞以防环路的那条链路 | <<<PAGE 38>>> |
| RPL Owner | 持有 RPL 端口的交换机，负责稳态阻塞/故障时解阻塞 RPL 口 | <<<PAGE 38>>> |
| R-APS message | 环自动保护倒换消息，在 Service VLAN 内传递 | <<<PAGE 38>>> |
| SF (Signal Fail) | R-APS 消息类型，检测到链路/节点故障时宣告 | <<<PAGE 38>>> |
| NR / RB (No Request / RPL Blocked) | 无请求消息及 RPL 已阻塞标记，恢复完成时由 RPL Owner 发出 | <<<PAGE 40>>> |
| WTR (Wait To Restore) timer | 等待恢复定时器，默认 5 分钟，防链路抖动引发反复倒换 | <<<PAGE 42>>> |
| Guard Timer | 守护定时器（默认 50 厘秒），丢弃过期 R-APS 防误倒换 | <<<PAGE 56>>> |
| Service VLAN | 环级 VLAN，承载 R-APS 消息和 ETH CCM | <<<PAGE 38>>> |
| Protected VLAN | 加入 ERP 环、转发状态由 ERP 决定的业务 VLAN | <<<PAGE 38>>> |
| MEG Level | ERP 管理实体组级别 0-7，环内所有交换机必须一致 | <<<PAGE 47>>> |
| Laddered / Subtending Ring | 主环+子环的梯形结构，子环借主环虚通道闭合 | <<<PAGE 43>>> |

## MACsec

| 术语 | 解释 | 页码 |
|---|---|---|
| MACsec (IEEE 802.1AE) | 二层链路加密与认证标准，点到点保护直连节点间流量 | <<<PAGE 67>>> |
| SecTag | MACsec 报文头（8/16 字节），含密钥信息、包号与安全通道标识（EtherType 0x88E5） | <<<PAGE 68>>> |
| ICV (Integrity Check Value) | GCM-AES 生成的 16 字节完整性校验值 | <<<PAGE 68>>> |
| SCI (Secure Channel Identifier) | 安全通道标识，收发通道各一，需与对端交叉匹配 | <<<PAGE 69>>> |
| SAK (Secure Association Key) | 安全关联密钥，加密数据平面流量 | <<<PAGE 69>>> |
| Key-chain | 密钥链，聚合多个 security key 供 sci-tx/sci-rx 引用 | <<<PAGE 69>>> |
| Static SA Mode | 手工配置最多 4 把 SA 密钥的交换机间静态模式 | <<<PAGE 75>>> |
| MKA (MACsec Key Agreement) | IEEE 802.1X-2010 密钥协商协议，动态生成 SAK | <<<PAGE 76>>> |
| CAK (Connectivity Association Key) | 连接关联密钥，保护 MKA 控制平面；EAP 模式经 RADIUS VSAs 下发 | <<<PAGE 76>>> |
| Key rotation | SAK 轮换，按会话时长（5-120 分钟）或流量（5-1000GB）先到先换 | <<<PAGE 77>>> |

## Private VLAN / MSTP / MVRP

| 术语 | 解释 | 页码 |
|---|---|---|
| Private VLAN (PVLAN) | 在单广播域内划分子域实现二层隔离的特性 | <<<PAGE 98>>> |
| Primary / Secondary VLAN | PVLAN 主 VLAN（对外）与从 VLAN（isolated/community 两类） | <<<PAGE 99>>> |
| Isolated VLAN | 隔离型二级 VLAN，成员间二层完全不通，仅到 promiscuous 口；每 Primary 仅一个 | <<<PAGE 99>>>、<<<PAGE 109>>> |
| Community VLAN | 社区型二级 VLAN，同社区可互通、跨社区不通 | <<<PAGE 99>>> |
| Promiscuous port | 混杂端口，属 Primary VLAN，可与所有端口通信 | <<<PAGE 100>>> |
| PVLAN ISL | 跨交换机延伸 PVLAN 域的级联口，同时承载主/从 VLAN | <<<PAGE 100>>> |
| MSTP (IEEE 802.1s) | 多生成树协议，多 VLAN 映射到少量实例 | <<<PAGE 115>>> |
| MSTI (MST Instance) | 多生成树实例（最多 16 个），VLAN 按需映射 | <<<PAGE 116>>> |
| CIST / IST | 公共与内部生成树（实例 0），未映射 VLAN 默认归属，承载全部实例 BPDU | <<<PAGE 115>>>、<<<PAGE 118>>> |
| MST Region | 多生成树区域，name+revision+VLAN 映射三要素一致才同域 | <<<PAGE 117>>> |
| Flat / per-vlan (1x1) mode | 单树 flat 模式（MSTP/MVRP 前置）与每 VLAN 一树模式，二者互斥 | <<<PAGE 122>>>、<<<PAGE 143>>> |
| MVRP (IEEE 802.1ak) | 多 VLAN 注册协议，跨桥接网动态传播 VLAN 成员（近似 GVRP） | <<<PAGE 152>>> |
| Registrar / Applicant mode | MVRP 端口注册模式（normal/fixed/forbidden）与申请者模式 | <<<PAGE 154>>>、<<<PAGE 155>>> |
| Dynamic VLAN (dyn) | 由 MVRP 自动学习创建的 VLAN，不建 IP 接口、不映射 MSTI | <<<PAGE 162>>>、<<<PAGE 163>>> |

## 网络安全

| 术语 | 解释 | 页码 |
|---|---|---|
| DoS Filtering | 交换机内置 DoS 攻击过滤（PoD/SYN/Land/Teardrop/ICMP>100pps 等） | <<<PAGE 168>>> |
| ARP Poisoning Detection | ARP 欺骗检测，识别未请求应答/伪造请求，restricted-address 每接口最多 2 个 | <<<PAGE 176>>>、<<<PAGE 177>>> |
| Local Proxy ARP | 本地代理 ARP，per-VLAN 用路由口 MAC 应答所有请求 | <<<PAGE 179>>> |
| ARP filter | ARP 过滤，按 sender/target 与 allow/block 控制代理应答 | <<<PAGE 180>>> |
| Port Mapping | 端口映射会话，user 口彼此隔离仅经 network 口通信，最多 8 会话 | <<<PAGE 182>>> |
| MFF (MAC Forced Forwarding, RFC 4562) | MAC 强制转发，同子网主机 ARP 一律指向网关（DHCP snooping+port mapping+动态代理 ARP） | <<<PAGE 185>>> |
| Storm Control (flood-limit) | 风暴控制，按 bcast/mcast/uucast 限速（pps/mbps/cap%），违例 shutdown/trap | <<<PAGE 188>>> |
| LPS (Learned Port Security) | 学习型端口安全：限 MAC 数量/学习窗/违例 restrict 或 shutdown；不支持聚合口 | <<<PAGE 190>>> |
| convert-to-static | 将端口已学动态 MAC 固化为静态，锁定当前设备 | <<<PAGE 193>>> |
| pkt-relay | LPS 报文中继，学习期被截获报文重注入转发路径 | <<<PAGE 196>>> |
| UDP Relay | 通用 UDP 端口中继，按服务端口转发到指定 VLAN/IP | <<<PAGE 170>>> |

## IP 路由 / OSPF

| 术语 | 解释 | 页码 |
|---|---|---|
| Loopback0 | 环回接口，管理/协议标识用，RIP/OSPF 自动通告（BGP 不） | <<<PAGE 216>>> |
| Recursive static route (follows) | 递归静态路由，下一跳跟随某目标主机路由动态解析 | <<<PAGE 224>>> |
| RIP | 距离矢量协议，跳数度量，16 跳不可达，UDP 520，更新 30s/失效 180s | <<<PAGE 227>>> |
| Router database / route-pref | 路由数据库与协议优先级（Local 1/Static 2/OSPF 110/RIP 120/EBGP 190…） | <<<PAGE 223>>>、<<<PAGE 299>>> |
| Router ID | OSPF 路由器标识：手工指定 > Loopback0 > 最高接口 IP | <<<PAGE 240>>> |
| DR / BDR / DROther | 指定/备份指定路由器（优先级+RouterID 选举）与普通路由器；组播 224.0.0.5/224.0.0.6 | <<<PAGE 242>>> |
| DBD / LSR / LSU / LSAck | OSPF 数据库描述/请求/更新/确认包，邻接同步四件套 | <<<PAGE 245>>>、<<<PAGE 246>>> |
| LSA Type 1/2 | 路由器 LSA（每路由器域内泛洪）与网络 LSA（DR 生成） | <<<PAGE 260>>>、<<<PAGE 261>>> |
| LSA Type 3 (Summary) | 汇总 LSA，ABR 生成跨区域通告网段；也承载区域路由汇总 | <<<PAGE 262>>>、<<<PAGE 286>>> |
| LSA Type 4 (Summary ASBR) | ASBR 汇总 LSA，ABR 通告到 ASBR 的位置 | <<<PAGE 264>>> |
| LSA Type 5 (External) | 外部 LSA，ASBR 重分发的域外路由；外部聚合由 ASBR 完成 | <<<PAGE 263>>>、<<<PAGE 287>>> |
| LSA Type 7 (NSSA) | NSSA 外部 LSA，ABR 转换为 Type 5 出域 | <<<PAGE 265>>> |
| ABR / ASBR / BB / IR | 区域边界路由器（汇总）/自治系统边界路由器（重分发）/骨干/内部路由器 | <<<PAGE 256>>>-<<<PAGE 258>>> |
| Stub / Totally Stubby Area | 末梢区域（拒 Type4/5，ABR 注入 Type3 默认路由）/完全末梢（再拒 Type3） | <<<PAGE 268>>>、<<<PAGE 269>>> |
| NSSA | 非纯末梢区域，允许 ASBR 用 Type7 引入外部路由 | <<<PAGE 270>>> |
| ECMP | 等价多路径，按流负载分担，AOS 最多 4 条，不支持逐包 | <<<PAGE 285>>> |
| Virtual Link / Transit Area | 虚链路与穿越区域，跨非骨干区延伸 Area 0 | <<<PAGE 289>>> |
| Graceful Restart (Grace LSA) | 平滑重启，重启期间邻居维持邻接避免全网 SPF；OSPF/ISIS 默认关、BGP 默认开 | <<<PAGE 361>>>、<<<PAGE 363>>> |
| Route Map (action/match/set) | 路由图：动作+匹配+修改，重分发过滤核心；序列自上而下命中即停 | <<<PAGE 300>>>、<<<PAGE 304>>> |

## 组播

| 术语 | 解释 | 页码 |
|---|---|---|
| Class D / 01:00:5E | 组播地址 224.0.0.0-239.255.255.255，IP 低 23 位映射组播 MAC | <<<PAGE 375>>> |
| IPMS (IP Multicast Switching) | IP 组播交换，硬件 IGMP 侦听按端口转发 | <<<PAGE 377>>> |
| IGMP (v1/v2/v3) | 因特网组管理协议；v2 加 Leave/特定组查询，v3 加源过滤；TTL=1 本地段协议 | <<<PAGE 381>>>、<<<PAGE 382>>> |
| IGMP Querier / querier-forwarding | 查询器（每 LAN 一个）与查询器转发（组播定向到查询器交换机） | <<<PAGE 380>>>、<<<PAGE 389>>> |
| IGMP Throttling (max-group) | 每端口/VLAN/全局限制学习组数，动作 none/drop/replace | <<<PAGE 396>>> |
| RPF (Reverse Path Forwarding) | 逆向路径转发校验，只在指向源的接口收包 | <<<PAGE 413>>>、<<<PAGE 426>>> |
| PIM-SM / PIM-DM | 稀疏模式（显式加入+RP 共享树）/密集模式（泛洪-剪枝 3 分钟循环、无 RP） | <<<PAGE 426>>>、<<<PAGE 434>>> |
| RP (Rendezvous Point) | 汇聚点，共享树根，源以 Register 单播封装发往 | <<<PAGE 428>>> |
| RPT / SPT switchover | 共享树/最短路径树；末跳 DR 收到首包后自动发起 SPT 切换 | <<<PAGE 428>>>-<<<PAGE 430>>> |
| BSR / C-RP | 自举路由器/候选 RP 的动态 RP 发现机制（优先级→hash→IP 选 RP） | <<<PAGE 431>>>、<<<PAGE 432>>> |
| Anycast RP (RFC 4610) | 多 RP 共享任播 Loopback 地址实现负载分担与 IGP 级快速切换；仅 PIM-SM、最多 8 台 | <<<PAGE 643>>>-<<<PAGE 645>>> |

## VRF / BGP

| 术语 | 解释 | 页码 |
|---|---|---|
| VRF | 虚拟路由转发，一台物理交换机多路由实例、地址可重叠；VLAN 只能归属一个 VRF | <<<PAGE 453>>>、<<<PAGE 460>>> |
| GRT / VRF Route Leak | 全局路由表及经 route-map 的 VRF 间路由导入导出 | <<<PAGE 461>>> |
| BGP-4 (RFC 4271) | 边界网关协议，AS 间路径矢量协议，TCP 179 | <<<PAGE 476>>> |
| IBGP / EBGP | AS 内/AS 间 BGP 邻居关系；IBGP 学的路由不再传给其他 IBGP 邻居（水平分割） | <<<PAGE 478>>>、<<<PAGE 501>>> |
| AS-PATH / Next-HOP / Origin | BGP 必选属性：AS 列表/下一跳/来源（IGP>EGP>Incomplete） | <<<PAGE 484>>>-<<<PAGE 487>>> |
| Local Preference / MED | 选出口偏好（越高越优）与入流量入口建议（越低越优、仅两 AS 间传递） | <<<PAGE 488>>>、<<<PAGE 491>>> |
| Community (NO-EXPORT/NO-ADVERTISE) | 路由打标分组属性，控制通告范围 | <<<PAGE 494>>>、<<<PAGE 496>>> |
| BGP synchronization | 同步：IBGP 学的路由须 IGP 可达才通告给 EBGP | <<<PAGE 502>>> |

## SPB / iFab / 其他

| 术语 | 解释 | 页码 |
|---|---|---|
| SPB / SPB-M (IEEE 802.1aq) | 最短路径桥接（MAC-in-MAC 变体），IS-IS 控制平面，全链路可用 | <<<PAGE 523>>>、<<<PAGE 525>>> |
| PBB (IEEE 802.1ah) | 运营商骨干桥接，MAC-in-MAC 封装（Ethertype 0x88E7） | <<<PAGE 526>>>、<<<PAGE 567>>> |
| BEB / BCB | 骨干边缘桥（封装/解封装、终结服务）/骨干核心桥（仅按 BMAC 转发、不学客户 MAC） | <<<PAGE 527>>> |
| BVLAN (B-VID) | 骨干 VLAN，承载控制与服务流量，最多 16 个；其上无 STP | <<<PAGE 527>>>、<<<PAGE 569>>> |
| I-SID | 24 位服务实例标识，区分租户/VPN，可达 16M | <<<PAGE 527>>>、<<<PAGE 565>>> |
| ECT / ECT-ID | 等价树及编号，用于各 BVLAN 建 SPT 时的 tie-break 分流 | <<<PAGE 569>>> |
| SAP / SDP | 服务接入点（物理口+封装值绑定服务）/服务分发点（通向远端 BEB，自动创建） | <<<PAGE 527>>>、<<<PAGE 572>>> |
| Head-End / Tandem replication | SPB BUM 复制模式：头端多单播复制（默认）/串联按组播 FDB 分叉复制 | <<<PAGE 539>>>、<<<PAGE 573>>> |
| LBD (Loopback Detection) | 环回检测，发探测帧防接入层环路，检测到即关闭端口 | <<<PAGE 609>>> |
| VPN Lite / L3 VPN (SPB) | SPB 上叠跑 OSPF/BGP 的边界方案 / IS-IS TLV 携带 VRF 路由的域内方案 | <<<PAGE 534>>>、<<<PAGE 536>>>、<<<PAGE 592>>> |
| iFab (Auto-VC/RCD/LACP/Routing/SPB/Profiling/MVRP) | 出厂默认七阶段零触摸自动化家族；失败自动回退 | <<<PAGE 624>>> |
| DIS / Pseudo node | IS-IS 指定中间系统/伪节点（对应 OSPF DR，可抢占；Hello 9s，DIS 3s） | <<<PAGE 689>>>、<<<PAGE 690>>> |
| NSAP (Area/System-ID/NSEL) | IS-IS 的 OSI 地址结构，本地管理 AFI=49，最小 8 字节 | <<<PAGE 686>>> |
| DHL (Dual-Home Link) | 双归链路，无 STP/LAG 的接入-核心快速倒换冗余 | <<<PAGE 318>>>、<<<PAGE 607>>> |
| Virtual Chassis (VC) / VFL | 虚拟机箱/虚拟机箱链路，多台堆叠为一逻辑设备 | <<<PAGE 134>>> |
| SLB / VIP / WRR | 服务器负载均衡：集群虚拟 IP（代理 ARP 应答）与加权轮询（权重 0 备份、总权重≤32） | <<<PAGE 653>>>-<<<PAGE 656>>> |
| write memory flash-synchro | 保存配置并同步备份 Flash 的 AOS 命令 | <<<PAGE 112>>> |
| working / certified directory | AOS 双镜像目录，reload from working/certified 支持升级回滚 | <<<PAGE 53>>>、<<<PAGE 680>>> |
