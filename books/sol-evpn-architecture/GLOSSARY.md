# GLOSSARY · EVPN Architecture Guide（sol-evpn-architecture）

> 页码为原书 `<<<PAGE N>>>` 标记。按数据面/实例与标识/路由类型/扩展社区/IRB 与 DAG/组播/多归属/设计与运维分组，精选 48 条。

## 数据面基础
- **VXLAN**：RFC 7348 标准 L2 overlay，以太网帧封装进 UDP/IP 在 L3 网络隧道传输 <<<PAGE 6>>>
- **VNI (VXLAN Network Identifier)**：24-bit 标识 VXLAN segment，上限约 1600 万 <<<PAGE 6>>>
- **VTEP / VTI**：VXLAN 隧道端点（封装/解封装）/ 隧道接口 <<<PAGE 6>>>
- **VXLAN gateway**：VXLAN 与传统 VLAN 域之间透明桥接的设备 <<<PAGE 6>>>
- **BUM traffic**：Broadcast/Unknown-unicast/Multicast 流量 <<<PAGE 9>>>
- **MP-BGP EVPN**：RFC 7432/8365 控制平面协议，AFI 25(L2VPN)/SAFI 70(EVPN) <<<PAGE 9-10>>>

## 实例与标识
- **EVI (Ethernet VPN Instance)**：跨所有 PE 的 EVPN 转发/路由实例，含 RD/RT <<<PAGE 9>>>
- **BD (Broadcast Domain)**：广播域，可与 EVI 一一对应或一对多 <<<PAGE 10>>>
- **ES / ESI**：连接一组 PE 的以太链路组 / 其唯一 10 字节标识 <<<PAGE 10>>>
- **ETag (Ethernet Tag)**：标识特定广播域（如 VLAN），值为 SAP 关联 VLAN ID <<<PAGE 10>>>
- **MAC-VRF / IP-VRF**：单 EVI 的 MAC 表 / PE 的 IP 路由 VRF 表 <<<PAGE 10>>>
- **SAP**：PE 上绑定接入端口到服务的逻辑服务实体（虚拟端口）<<<PAGE 10>>>
- **PE / CE**：服务端点设备（与 VTEP 混用）/ 客户边缘设备 <<<PAGE 10>>>
- **RD (Route Distinguisher)**：8 字节，使重叠路由唯一；AOS 用 Loopback0 自动派生 <<<PAGE 19>>>
- **RT (Route Target)**：6 字节扩展社区，控制导入/导出；AOS 由 ASN+Etag(VNI) 派生 <<<PAGE 19>>>

## 路由类型
- **R-T1 (Ethernet A-D Route)**：多归属 ES 可达性；aliasing/split horizon/mass withdraw；分 per-ESI(R-T1A) 与 per-EVI(R-T1B) <<<PAGE 11-13>>>
- **R-T2 (MAC/IP Advertisement)**：端主机 MAC（及 IP）可达性；支撑 ARP 抑制 <<<PAGE 11>>>
- **R-T3 (IMET)**：按 VNI 自动发现 VTEP，构建 ingress replication 列表 <<<PAGE 11>>>
- **R-T4 (Ethernet Segment Route)**：发现同 ES 的 PE 并执行 DF 选举 <<<PAGE 11>>>
- **R-T5 (IP Prefix Route)**：IP 前缀通告（RFC 9136）；外部连通与路由汇总；8.10R2 起 <<<PAGE 11>>>
- **R-T6 (SMET)**：IGMP/MLD proxy，通告 (*,G)/(S,G) 组播兴趣 <<<PAGE 11>>>
- **R-T7 / R-T8**：多归属节点间 IGMP Join/Leave 状态同步 <<<PAGE 11>>>
- **R-T10**：MVPN 继承的源发现机制，PEG 拉流前的 (S,G) 信令 <<<PAGE 38-39>>>

## Service 模型与扩展社区
- **VLAN-based service model**：VLAN:MAC-VRF:VNI:EVI 一一对应；ETag=0；允许 VLAN 转换 <<<PAGE 19>>>
- **VLAN bundle / VLAN-aware service model**：多 VLAN 共享 BD（ETag=0 不许转换）/ EVI 内多 VLAN 各自成广播域 <<<PAGE 20>>>
- **Enhanced VLAN-bundle**：ALE 定义模型；每 EVI 仅一条 R-T3（ETag=0）省路由数 <<<PAGE 41>>>
- **ARP suppression / Proxy ARP**：PE 代答本地 ARP 抑制洪泛；AOS 默认开 <<<PAGE 20-21>>>
- **ES-Import RT EC**：随 R-T4 携带，仅同 ES 的 PE 导入 <<<PAGE 21>>>
- **ESI Label EC**：R-T1A 携带；指示冗余模式（flags 1=single-active, 0=all-active）<<<PAGE 21>>>
- **MAC Mobility EC**：序列号跟踪主机最新位置，亚秒级 VM 迁移收敛 <<<PAGE 22>>>
- **Default Gateway EC**：PE 以 R-T2 通告默认网关 MAC，网关分布式 <<<PAGE 22>>>
- **Router MAC EC**：携带始发路由器 MAC；MAC 作 overlay index 的对称 IRB 用 <<<PAGE 23>>>

## IRB 与 DAG
- **IRB**：EVPN 跨子网连通，本地 PE 直接路由 <<<PAGE 23>>>
- **Asymmetric / Symmetric IRB**：拉伸 EVI 三次查表（资源密集）/ 双端桥+路由（推荐）<<<PAGE 24-25>>>
- **SBD / Fabric-VPN**：每 VRF 一个 L3EVI，提供 VRF 内 IRB 服务间可达；AOS 记作 Fabric-VPN <<<PAGE 25>>>
- **Host-based / Prefix-based routing**：R-T2 /32（两模型皆可）/ R-T5 前缀（仅对称）<<<PAGE 26>>>
- **Overlay index**：R-T5 递归查找索引：网关 IP、MAC 或 ESI <<<PAGE 15>>>
- **DAG (Distributed Anycast Gateway)**：全 PE 同 anycast IP+MAC，免 VRRP 支持主机移动 <<<PAGE 28>>>
- **Anycast MAC auto-derivation**：00:00:5e:00:01:<VRF-ID> 或 site-based 派生 <<<PAGE 29>>>

## 组播
- **Ingress replication**：头端逐单播复制 BUM；AOS 唯一支持方式 <<<PAGE 29-30>>>
- **Tandem replication**：组播底层中继复制；核心高效需组播底层 <<<PAGE 29>>>
- **PMSI**：R-T3 附带隧道属性，标识 BUM 使用的 P-Tunnel <<<PAGE 15>>>
- **IPMS / IPMSv6**：OmniSwitch IGMP/MLD snooping 硬件线速组播交付 <<<PAGE 37>>>
- **OISM**：RFC 9625，Fabric-VPN+R-T6 跨子网组播，无需 PIM；8.10R3 EA <<<PAGE 37>>>
- **PEG (PIM EVPN Gateway)**：与外部 PIM 路由器互通的网关；双 PEG 需专用 L3 互联；8.10R3 EA <<<PAGE 38>>>
- **Default SBD-SMET route (*,*)**：内部源发现方式，PEG 借其收全部组播；带宽低效 <<<PAGE 38-39>>>

## 多归属
- **Multi-homing**：CE 经 LAG 连多 PE；single-active 与 all-active 两模式 <<<PAGE 32>>>
- **DF (Designated Forwarder)**：ES 内指定转发者，防 BUM 重复/环路 <<<PAGE 32-33>>>
- **Service carving**：按 EVI/VLAN 选多 DF 分散 BUM 负载；DF = EVI mod N <<<PAGE 33>>>
- **Split Horizon Group (SPG)**：non-DF SAP 的 BUM 出向过滤组 <<<PAGE 34>>>
- **Local Bias / ES Pruning**：本 PE 的流量总走本地接入；远端丢弃重复 BUM <<<PAGE 34>>>
- **Aliasing**：全活 ES 各 PE 通告 R-T1A/1B，远端按流负载分担 <<<PAGE 34>>>
- **Backup path**：单活 Primary/Backup 列表，主撤路无缝切换 <<<PAGE 35-36>>>
- **Mass withdraw**：R-T1A 以 EVI=0xFFFFFFFF 编码 ES 不可达，批量刷新 MAC <<<PAGE 36>>>

## 检测与运维
- **MAC duplication / hold-down**：MAC 反复迁移达阈值进 hold-down 停处理 BGP 通告 <<<PAGE 39>>>
- **DAD (Duplicate Address Detection)**：同 IP 不同 MAC 检测；N 次 IP-move 进 filtering state；ARP Confirm 探测旧主 <<<PAGE 39>>>
- **Silent host / Sticky bit**：静默主机静态绑 MAC 到 SAP 并以 sticky 位通告防误迁移 <<<PAGE 40>>>
- **AOS auto-ESI (Type 0x3)**：物理口/LACP LAG 自动 ESI；静态 LAG 手工 5 字节 <<<PAGE 41>>>
- **Auto-generated RD**：Loopback0+Type+Object（Service/ESI 8bit 段 ID 上限 256/Prefix）<<<PAGE 42-43>>>
- **GRM (Global Route Manager)**：VRF 间/VRF 与 Fabric-VPN 间路由重分发中介 <<<PAGE 47>>>
- **Border leaf**：对外部网络做网关的 PE；需路由汇总与防回声 <<<PAGE 46-48>>>
- **RR / TTL Security**：spine 兼任路由反射器（冗余 RR 同 cluster-id）/ BGP 直连保障 max-hop 0 <<<PAGE 46>>>
