# Verified 候选（V1 原文真实性核对 + V2/V3 抽查）

## cases

- **C1 SPB 骨干配置四步**：建 BVLAN（配 ECT-ID）→ 定控制 BVLAN → 定义 SPB IS-IS 接口 → 启用 SPB IS-IS；样例拓扑提供 3 条等价路径，建 4 个 BVLAN（4000–4003，4000 专用于控制）<<<PAGE 16>>>
- **C2 骨干验证命令族**：`show spb isis interface`（L1 邻接、metric=10、Hello 9s/持失 27s）→ `show spb isis nodes`（system ID=BMAC、source ID、bridge priority）→ `show spb isis adjacency` → `show spb isis bvlans`（ECT 算法、(S,G)/(*,G)）→ `show spb isis unicast-table` → `show spb isis spf bvlan` <<<PAGE 18>>>
- **C3 L2 服务创建三步**：`service N spb isid X bvlan Y` → 物理口设为 SAP → 定义匹配客户流量的 SAP（如 `sap port 1/1/48:0` 映射 untagged）；只需在相关 BEB 上配置，BCB 免配置 <<<PAGE 20>>>
- **C4 L2 服务验证**：`show service spb`（BEB 视图/BCB 视图对比）、`show spb isis services`、`show service access`（SAP 类型与 L2Profile）、`show service spb ports`（SAP/SDP）、`show service mesh-sdp spb`、`show mac-learning domain spb`（BCB 不学 CMAC）<<<PAGE 22>>>
- **C5 VLAN 翻译双级开关**：服务级 `service service_id vlan-translation enable` + SAP 级 `service access port vlan-xlation enable`，用于同一服务下不同封装（服务器 tagged / 客户端 untagged）互通 <<<PAGE 23>>>
- **C6 L2Profile 控制 SAP 上 L2 协议处理**：`service l2profile name stp action…` 定义 peer/drop/tunnel，默认表见 Table 2（如 STP 在 def-access-profile 为 tunnel、在 unp-def-access-profile 为 drop）<<<PAGE 24>>>
- **C7 两代 ASIC 的三种路由形态判定**：单次直通（IP 接口直接绑服务）/ 外部物理回环（dummy VLAN + rtr-port + 双口线缆）/ 内部前面板回环（`1/1/51A` 指定为 loopback 口，单逻辑口兼具 VLAN 与 SAP 功能）<<<PAGE 26>>>
- **C8 外部物理回环配置**：为每个需路由的服务建 dummy VLAN（VLAN 11↔service 1），回环口 1/1/1 作 VLAN 口、1/1/2 作 SAP，IP 接口加 `rtr-port` 选项防止 VLAN 扩散并关 STP <<<PAGE 28>>>
- **C9 L3 VPN 服务五步**：建 L2 SPB 服务 → 建租户 VRF → 建 LAN/WAN 侧 IP 接口（WAN 直挂服务或挂 dummy VLAN）→ WAN 接口绑定服务 ISID → VRF 与 SPB IS-IS ISID 实例间路由导入/导出 <<<PAGE 31>>>
- **C10 L3 VPN 验证**：`show` 路由表中远端 LAN 网段为 IMPORT 路由、下一跳指向远端 BEB 的 WAN 地址；ARP 表动态学习远端 WAN 网关 <<<PAGE 33>>>
- **C11 共享服务路由泄漏五步**（边界 BEB）：shared_services VRF 经 route-map 过滤后导出至全局表 → 全局表导入客户 VRF → 客户路由导入 shared_services VRF → 从 SPB IS-IS 各客户 ISID 导入远端客户路由 → shared_services 路由重分发回各客户 ISID <<<PAGE 35>>>
- **C12 Auto-Fabric 启动序列**：Auto-VC → Auto-RCD → Auto-LACP → Auto-SPB → Auto-MVRP → Auto-IP；AOS 8.7R1 起 auto-SPB 默认建 BVLAN 4000–4003 映射 ECT 1–4、4000 为控制 BVLAN <<<PAGE 36>>>
- **C13 Auto-VC 触发条件**：无 vcsetup.cfg 时用 LLDP 在 auto-VFL 口探测同族设备，选举 Master，生成 vcsetup.cfg 后不再触发 <<<PAGE 36>>>
- **C14 Auto-RCD 取配置**：DHCP（untagged 默认 VLAN 或 VLAN 127，重试 3 次）→ 依 DHCP 选项从 TFTP 取指令文件或联络 OmniVista 2500 → 下载固件与 vcboot.cfg → 重启加载 <<<PAGE 37>>>
- **C15 Auto-LACP 与第三方互通**：LLDP 识别对端交换机后将同对 LACP 兼容口并入 linkagg；对端即使是第三方手工配了 LACP，"the OmniSwitch detects LACP PDUs and automatically configures its side of the linkagg" <<<PAGE 37>>>
- **C16 Auto-IP 邻居自动配平**：侦听 OSPFv2/OSPFv3/IS-IS Hello，按收到的 area/Hello/Dead 参数自动生成本地匹配配置建立邻接 <<<PAGE 38>>>
- **C17 动态 SAP（L2 场景）**：定义 EMPLOYEE/IoT/GUEST/WLAN/CCTV/RESTRICTED 六个 UNP 各绑 ISID；端口 1/1/10–16 用 SAMPLE_FLOW 模板走 802.1x→filter-id、MAC 认证兜底、无匹配落 RESTRICTED（仅最小网络连通供 onboard）<<<PAGE 38>>>
- **C18 静默设备静态绑定 UNP**：对长时间不发包的设备（如节能模式）在端口静态绑定 UNP，避免绑定丢失导致 WAKE-ON-LAN 不可达 <<<PAGE 39>>>
- **C19 动态服务编号演算**：VLAN 101、默认参数下 ISID = 10,000,000 + 0 + (101 % 512) = 10,000,101；BVLAN Index = 10,000,101 % 4 = 1 → 映射 BVLAN 4001 <<<PAGE 42>>>
- **C20 多租户 Domain ID 配置**：为客户 A/B/C 建 Domain 1/2/3，UNI 端口映射到对应 Domain，即使 VLAN 标签重叠也保持隔离 <<<PAGE 43>>>
- **C21 带内管理配置**：管理 IP 直接建在控制 BVLAN 上；网关节点（BEB-1/2）在 OSPF 与 spb-mgmt 协议间互相重分发并用 route-map 防环 <<<PAGE 44>>>
- **C22 OAM 配置**：BVLAN 级为所有 BVLAN 与 BEB 配虚 MEP（BCB 可选），MIP 自动创建；`saa auto create` 自动在所有 BEB/BCB/BVLAN 间建时延抖动丢包测试 <<<PAGE 45>>>
- **C23 L2 trace 排障**：LBM/LBR 做 L2 ping，LTM/LTR 做 L2 trace，输出含各跳 BMAC 与入出接口 <<<PAGE 46>>>
- **C24 部署指南总体步骤（0–11）**：物理拓扑/LAG → VLANs → LBD → 控制与业务 BVLAN → SPB 服务 → BEB 上 SAP → VRF 分段 → VRRP → VRF-PBR 点对点 → VRRP Tracking → OSPF → 网络策略 <<<PAGE 62>>>
- **C25 部署指南落地命令链**：`vlan 1000` → `loopback-detection enable` + `loopback-detection service-access linkagg 31 enable` → `spb bvlan 4000-4002 admin-state enable` → 配控制 BVLAN 前先 `spb isis admin-state disable` → `spb isis interface linkagg 16` → `service 1000 spb isid 1000 bvlan 4001 vlan-xlation enable` → `service access linkagg 31 vlan-xlation enable` → `service 1000 sap linkagg 31:1000` → ping 测试 + `show spb isis spf bvlan 4001` 验路径 <<<PAGE 67>>>
- **C26 AP 直挂 BEB SAP 的 untagged 处理**：AP 管理服务用 `service 2000 sap port 1/1/31:0` 映射 untagged，SSID 流量另建 tagged SAP（`service 1016 sap port 1/1/31:1016`）<<<PAGE 73>>>
- **C27 VRF+VRRP+OSPF+策略全套**：`vrf create corp` 等五个 VRF → VRF 内 IP 接口挂 service（`vrf corp ip interface "corp-wired" address 10.10.15.3 mask 255.255.255.0 service 1000`）→ VRRP 三命令建虚网关 .1 → PBR 侧 /30 互联 → `ip vrrp track 1 … priority 25` + track-association → 各 VRF 独立 OSPF area、本地网段聚合进 access-list 经 route-map 重分发 → PBR 上 policy condition/rule 拒绝 Guest 到其它 VRF <<<PAGE 74>>>
- **C28 S-Hook 替代配置（两代 ASIC 混合场景）**：VLAN 域 LAG-125 打 tagged VLAN，服务域 LAG-127 建 `service N sap linkagg 127:N`，实现 VLAN 域与 SPB 域的 S 形挂钩 <<<PAGE 81>>>

## counter-examples

- **X1 STP 禁用链路浪费带宽**："Unused links: Creating a loop-free topology by disabling network links results in inefficient bandwidth use and low Return on Investment (ROI)" <<<PAGE 5>>>
- **X2 STP 非根节点间走次优路径**："communication between non-root bridges may need to traverse a sub-optimal route transiting the root-bridge instead of alternative better routes over links that have been disabled" <<<PAGE 5>>>
- **X3 STP 收敛慢且瞬态成环**："typical convergence times are in the order of seconds. While STP re-converges to a new topology, transient loops may form, resulting in packet drops, link saturation, and session timeouts" <<<PAGE 5>>>
- **X4 以太网泛洪学习**："Ethernet's 'flood and learn' address learning floods unknown-unicast traffic until the destination address is learned from return traffic" <<<PAGE 6>>>
- **X5 全网学 MAC 不可扩展**："All nodes in the LAN learn all end-device MAC addresses thus posing a scalability challenge" <<<PAGE 6>>>
- **X6 Q-in-Q 服务实例上限**："IEEE 802.1ad (Provider Bridging, or Q-in-Q) is limited to a maximum of 4096 service instances" <<<PAGE 6>>>
- **X7 MPLS 协议栈负担**："unlike MPLS, which requires a 'stack' of protocols (for example: LDP, OSPF, MP-BGP, among others), SPB relies on a single protocol" <<<PAGE 6>>>
- **X8 head-end 复制费带宽**："Head-End replication can be inefficient in terms of bandwidth consumption" <<<PAGE 15>>>
- **X9 tandem (S,G) 费资源**："it is less efficient in terms of resource use because it requires an additional SPT and multicast FDB per ISID" <<<PAGE 15>>>
- **X10 tandem (*,G) 不走最短路**："This tree is not a Shortest Path tree and is not congruent with the unicast SPT… traffic will not generally follow the shortest path" <<<PAGE 16>>>
- **X11 第一代 ASIC 双次过交换矩阵**："routing between IP interfaces associated to two different SPB services… had to traverse the switch fabric twice. This required an external physical loopback connecting two different switch ports" <<<PAGE 26>>>
- **X12 VPN Lite 配置量爆炸**："4 customer services spanning 8 BEB nodes require 4 x OSPF instances per node: A total of 32 x OSPF configurations across all nodes… 64 x OSPF configurations all nodes included" <<<PAGE 34>>>
- **X13 路由协议叠加拖慢收敛**："VPN Lite convergence can be slower because the stacking of routing protocols has a compounding effect over convergence time: IS-IS must converge before OSPF can converge" <<<PAGE 34>>>
- **X14 L3 VPN 无法直连外部网络**："L3 VPN relies on SPB IS-IS and cannot directly interoperate with external networks" <<<PAGE 34>>>
- **X15 VRF 泄漏前提是地址不重叠**："As a pre-requisite, customer A's and B's address space must not overlap with each other nor with the shared services" <<<PAGE 34>>>
- **X16 预置全部 VLAN 服务是坏实践**："It may be tempting to pre-provision services for all 4096 VLANs. But this is a poor practice as it creates an unnecessary load on the control plane" <<<PAGE 42>>>
- **X17 默认 Service Modulo 造成 VLAN 混桥**："using the default Service Modulo of 512 can result in up to 8 different VLAN tags being mapped to the same service… it will result in different VLAN traffic being bridged in the same L2 domain" <<<PAGE 43>>>
- **X18 静默设备丢绑定**："These periods of inactivity can result in a loss of service binding, thus making the device effectively unreachable (for example for a WAKE-ON-LAN packet)" <<<PAGE 39>>>
- **X19 overload 后无备选路径则中断**："once the overload state is enabled on a node no traffic will transit through the node even if there are no alternative paths" <<<PAGE 48>>>
- **X20 多 BVLAN 超过等价路径数徒增负担**："having more BVLANs than equal-cost-paths in the physical topology creates an additional unnecessary load in the CP which results in increased resource utilization and convergence times" <<<PAGE 52>>>
- **X21 多 VLAN 映射同一服务破坏隔离**："Mapping different VLANs to the same SPB service makes inter-VLAN bridging possible, thus defeating the purpose of having different VLANs in the first place" <<<PAGE 52>>>
- **X22 虚拟化环境重复 MAC 引发 mac-move**："Duplicate MAC addresses in different VLANs do not collide, however, if these VLANs are mapped to the same SPB service… those MACs will be constantly learned, re-learned and flushed" <<<PAGE 52>>>
- **X23 MAC-in-MAC 下 LAG 哈希缺熵**："MAC addresses are the BMACs of BEB and BCB nodes while IP addresses and port numbers are not visible to the hashing logic. In most cases this does not create enough entropy" <<<PAGE 53>>>
- **X24 骨干内无法基于内层 L2–L4 再分类**："No further classification based on inner L2-L4 conditions is possible within the SPB backbone due to the MAC-in-MAC encapsulation" <<<PAGE 54>>>
- **X25 外部路由注入风险**："This creates an opportunity for a bad actor to inject malicious routes and poison the routing table to carry out DoS, MITM, or other attacks" <<<PAGE 56>>>
- **X26 STP 在 SPB 中的局限场景**（非冗余接入的后果）："Non-redundant: The CE is attached to a single BEB through a single link. Link, BEB or CE failure will result in loss of service to the site" <<<PAGE 49>>>
- **X27 光纤同沟双断**："fibre runs should use diverse physical paths to protect against fibre cuts which would typically interrupt both links otherwise" <<<PAGE 49>>>
- **X28 无 graceful restart 的切换代价**："a VC master or CMM takeover event would require neighbour nodes to tear down and re-establish adjacencies… resulting in some disruption to traffic flows" <<<PAGE 48>>>
- **X29 客户网配置错误可引发跨域广播风暴**："Configuration faults in customer networks can result in loops spanning both the SPB backbone and customer access network. This can result in broadcast storms" <<<PAGE 51>>>
- **X30 命名冲突的教训（部署指南）**："BEB-1 and BEB-2 names are not used because BCB-1 and BCB-2 occupy those numbers. Avoiding using the same numbers here will simplify understanding the network topology" <<<PAGE 64>>>

## frameworks

- **F1 SPB 双平面架构框架**：DP（802.1ah PBB：B-VID/ISID/B-SA/B-DA，只查 FDB）+ CP（RFC 6329 IS-IS：拓扑发现、SPT 计算、服务成员泛播、FDB 预填充）；DP/CP 职责分离是理解全书一切机制的骨架 <<<PAGE 9>>>
- **F2 服务框架三层标识体系**：Service（本地有效）→ ISID（全局服务/租户标识）→ BVLAN（承载与负载分担）；虚拟端口 SAP（UNI 侧绑定物理口+流量类型）与 SDP（NNI 侧动态指向远端 BEB）；服务只在 BEB 实例化、BCB 零感知 <<<PAGE 13>>>
- **F3 BUM 三模式选型矩阵**（Table 1）：head-end / tandem (S,G) / tandem (*,G) × 带宽效率 / 资源效率 / 同余性 / 建议场景（低组播带宽+多源少收 / 高组播带宽+少源多收 / 根桥为源宿或第三方互通）<<<PAGE 16>>>
- **F4 CE 接入冗余四级模型**：非冗余 → 冗余链路（LAG）→ 冗余链路+节点（DHL / 动态路由）→ 全冗余（CE 双机 + MSTP/VRRP）；L2 与 L3、L3-CE 与 L2-CE 分别套用；VC+LAG 可与所有档位组合 <<<PAGE 49>>>
- **F5 iFab 自动化分层框架**：Auto-Fabric 六阶段（VC/RCD/LACP/SPB/MVRP/IP）打底 → UNP+认证做动态 SAP → Dynamic Services 按 VLAN 标签即时生成 UNP/服务（BSN/Domain ID/Service Modulo 公式体系）<<<PAGE 36>>>
- **F6 中型园区部署参考架构**（部署指南）：2×BCB 全网格 + N×BEB 双归 LAG + PBR 策略路由器；VRF 按部门分段、VRRP 网关冗余（.1 虚地址 + 末位 BEB 号）、/30 点对点连 PBR、OSPF 按 VRF 分 area、PBR 集中策略；可平滑加 BCB 横向扩展 <<<PAGE 63>>>

## glossary

- **SPB（Shortest Path Bridging）**：IEEE 802.1aq 最短路径桥接，用 IS-IS 替代 STP 构建全链路可用的无环多路 fabric <<<PAGE 6>>>
- **SPB-M / SPBM**：SPB MAC-in-MAC 模式（802.1ah 封装）<<<PAGE 5>>>
- **SPB-V**：SPB Q-in-Q 模式 <<<PAGE 5>>>
- **IS-IS**：中间系统到中间系统链路状态协议，SPB 唯一控制面协议 <<<PAGE 6>>>
- **RFC 6329**：定义 SPB 的 IS-IS 扩展（NLPID 与一组 TLV）<<<PAGE 11>>>
- **PBB（Provider Backbone Bridging）**：IEEE 802.1ah，MAC-in-MAC 封装 <<<PAGE 5>>>
- **Q-in-Q（Provider Bridging）**：IEEE 802.1ad 双标签封装，服务实例上限 4096 <<<PAGE 6>>>
- **STP/RSTP/MSTP**：生成树协议族，靠禁用链路防环 <<<PAGE 5>>>
- **OSPF**：开放最短路径优先，VPN Lite 与部署指南外部路由所用 <<<PAGE 5>>>
- **BGP / MP-BGP**：边界网关协议；MPLS 传 VPN 路由需 MP-BGP <<<PAGE 4>>>
- **LDP**：标签分发协议，MPLS 协议栈成员 <<<PAGE 5>>>
- **802.1ag（CFM）**：连通性故障管理，SPB 中用于 L2 ping/L2 trace；CCM 不支持 <<<PAGE 45>>>
- **802.1AE（MACSec）**：MAC 层点到点认证与加密，硬件线速 <<<PAGE 55>>>
- **802.1x / MAC 认证**：端口接入认证，配合 RADIUS 返回 filter-id 动态定 UNP <<<PAGE 8>>>
- **VRRP**：虚拟路由冗余协议，双 BEB 网关冗余 <<<PAGE 50>>>
- **IGMP Snooping**：组播侦听，与 head-end 复制组合时可达最优 <<<PAGE 16>>>
- **LACP / linkagg**：链路聚合控制协议 / 聚合链路；auto-LACP 默认开启 <<<PAGE 37>>>
- **LLDP**：链路层发现协议，Auto-VC/LACP/SPB 的邻居探测基础 <<<PAGE 36>>>
- **DSCP**：差分服务代码点；SPB 骨干内不可见，两次路由场景应信 CoS <<<PAGE 54>>>

## 数据面与标识
- **BVLAN（B-VID）**：骨干传输 VLAN，最多 16 个，控制 BVLAN 承载 IS-IS 消息 <<<PAGE 9>>>
- **ISID（I-SID）**：24 位服务实例标识，最多 16M 租户/服务 <<<PAGE 9>>>
- **BMAC（B-SA/B-DA）**：骨干源/目的 MAC，骨干内转发唯一依据 <<<PAGE 9>>>
- **CMAC**：客户 MAC，只在 BEB 边缘学习，不进骨干 <<<PAGE 9>>>
- **ECT（Equal-Cost Tree）**：等价树，每节点每 BVLAN 一棵；ECT-ID 用于建树平局裁决 <<<PAGE 11>>>
- **FDB**：转发表；BVLAN 域 FDB 由控制面预填充 <<<PAGE 9>>>
- **SPF/SPT**：最短路径优先算法 / 最短路径树 <<<PAGE 11>>>
- **TLV**：类型-长度-值编码，IS-IS 携带 SPB 扩展信息的方式 <<<PAGE 11>>>
- **Ethertype 0x88E7**：PBB 骨干以太类型 <<<PAGE 10>>>
- **同余性（Congruy）**：组播与单播走同一路径的性质；head-end 与 tandem (S,G) 具备 <<<PAGE 15>>>
- **路径对称性（Symmetry）**：X→Y 与 Y→X 路径一致，利于 OAM 单向时延推算 <<<PAGE 12>>>
- **源 ID（Source ID）**：20 位节点标识，源自 system ID 低位字节，tandem 复制时标记 BUM 源 <<<PAGE 18>>>
- **桥优先级（Bridge Priority）**：16 位，路径计算平局裁决 <<<PAGE 18>>>
- **RPFC（Reverse-Path Forwarding Check）**：反向转发检查，按 FDB 校验入帧源 BMAC 可达性以破瞬态环 <<<PAGE 51>>>
- **LBD（Loopback Detection）**：接入层环路检测，发探测帧收到即关端口，应启用在所有 UNI 口 <<<PAGE 51>>>

## 节点与端口角色
- **BEB（Backbone Edge Bridge）**：骨干边缘桥，封装/解封装客户帧，学习 CMAC，服务与 SAP 只在其上配置 <<<PAGE 10>>>
- **BCB（Backbone Core Bridge）：骨干核心桥，纯中转，不学 CMAC、不配服务、无需 IP（管理除外）<<<PAGE 10>>>
- **SAP（Service Access Point）**：UNI 侧逻辑端口，绑定物理口+流量类型到服务 <<<PAGE 14>>>
- **SDP（Service Distribution Point）**：NNI 侧逻辑端口，由控制面动态创建指向远端 BEB <<<PAGE 14>>>
- **CE（Customer Edge）**：客户边缘设备，接入冗余四档模型的主体 <<<PAGE 48>>>
- **UNI/NNI**：用户网络接口 / 网络侧接口 <<<PAGE 14>>>
- **L2Profile**：定义 SAP 上各 L2 控制协议（STP/802.1x/MVRP 等）peer/drop/tunnel 处理 <<<PAGE 24>>>
- **VC（Virtual Chassis）**：虚拟机箱，多台堆叠为单逻辑设备，统一控制管理面 <<<PAGE 53>>>
- **VFL**：VC 内互联端口（auto-VFL）<<<PAGE 36>>>

## 服务与路由
- **L2 服务**：多站点单一 any-to-any 桥接域 VPN <<<PAGE 20>>>
- **L3 服务**：多站点单一 any-to-any 路由域 VPN，各站不同子网 <<<PAGE 29>>>
- **VPN Lite**：在 L2 SPB 服务之上叠加 OSPF/BGP/静态路由的 L3 方案，用于边界对接外部网络 <<<PAGE 29>>>
- **L3 VPN**：借 IS-IS TLV 直接携带客户 VRF 路由的方案，域内推荐 <<<PAGE 30>>>
- **VRF**：虚拟路由转发实例，租户 L3 隔离载体；low profile VRF 省资源 <<<PAGE 29>>>
- **VLAN 翻译（VLAN Translation）**：同一服务下不同 SAP 封装互通，服务级+SAP 级双开关 <<<PAGE 23>>>
- **单次直通路由（Single-pass inline routing）**：新代 ASIC 将 IP 接口直接绑 SPB 服务，无需回环 <<<PAGE 26>>>
- **两次路由（Two-pass routing）**：外部物理回环或内部前面板回环经 dummy VLAN 中转 <<<PAGE 26>>>
- **dummy VLAN / rtr-port**：两次路由中挂 IP 接口的过渡 VLAN；rtr-port 选项防 VLAN 扩散并关 STP <<<PAGE 28>>>
- **路由泄漏（Route Leaking）**：shared_services VRF 与客户 VRF 经全局表互导共享路由 <<<PAGE 34>>>
- **BGP4**：边界 BEB 与外部实体（如防火墙）交换路由的常用协议 <<<PAGE 34>>>
- **PBR（Policy-Based Router）**：部署指南中集中做 VRF 间策略路由的交换机角色 <<<PAGE 63>>>
- **edge routing（边缘路由）**：路由只在入/出 BEB 发生，骨干桥接 <<<PAGE 29>>>

## BUM 与组播
- **BUM**：广播/未知单播/组播流量统称 <<<PAGE 15>>>
- **Head-end 复制**：入端 BEB 复制多份单播，省资源费带宽 <<<PAGE 15>>>
- **Tandem (S,G) 复制**：按源-组独立组播 SPT，每链路一份副本，默认模式，按服务选择 <<<PAGE 15>>>
- **Tandem (*,G) 复制**：每 BVLAN 一棵共享树，根按桥优先级，不保证最短路，按 BVLAN 选择 <<<PAGE 16>>>
- **IGMP Snooping**：让 head-end 在多源少收场景最优的补充 <<<PAGE 16>>>

## 自动化与安全
- **iFab（Intelligent Fabric）**：ALE 自动化特性集合的统称 <<<PAGE 6>>>
- **Auto-Fabric**：出厂默认的自动建网特性组（VC/RCD/LACP/SPB/MVRP/IP）<<<PAGE 36>>>
- **Auto-RCD**：自动远程配置下载（DHCP→TFTP/OmniVista 取固件与配置）<<<PAGE 37>>>
- **Auto-SPB**：LLDP 探测 SPB 邻居后自动配骨干口与默认 BVLAN <<<PAGE 37>>>
- **Auto-MVRP**：无 SPB 邻居时启用 MVRP 动态学 VLAN <<<PAGE 37>>>
- **UNP（User Network Profile）**：用户网络画像，分类/认证规则映射到 VLAN 或服务 <<<PAGE 8>>>
- **UNP access 口 / bridge 口**：分别映射流量到 SPB 服务 / VLAN <<<PAGE 38>>>
- **动态 SAP / 动态服务（Dynamic Services）**：按认证或 VLAN 标签即时生成 SAP 或整个 UNP+服务 <<<PAGE 38>>>
- **Base Service Number（BSN）**：动态服务 ISID 下限基数（默认 10,000,000），隔离手工编号 <<<PAGE 42>>>
- **Domain ID**：动态服务 ISID 公式的租户偏移量，保多租户隔离 <<<PAGE 42>>>
- **Service Modulo**：VLAN→服务映射取模基数，默认 512，隔离需求下建议 4096 <<<PAGE 42>>>
- **Access Guardian（AG）**：ALE 分类与 NAC 框架，动态服务实例化的入口 <<<PAGE 8>>>
- **NAC**：网络准入控制 <<<PAGE 8>>>
- **RADIUS / filter-id**：认证服务器及其返回的画像匹配属性 <<<PAGE 38>>>
- **微分段（Micro-segmentation）**：UNP 内 ACL/QoS 限制同 VPN 内横向流量 <<<PAGE 8>>>
- **OOBM / EMP 口**：带外管理与专用管理口 <<<PAGE 43>>>
- **带内管理（In-band Management）**：管理 IP 直接挂控制 BVLAN，经 spb-mgmt 协议传路由 <<<PAGE 44>>>
- **mac-move**：重复 MAC 在同服务内反复学习/冲刷的失稳现象 <<<PAGE 52>>>
- **风暴控制（Storm Control）**：BUM 限速，超限丢包或关端口，默认开启 <<<PAGE 52>>>

## 运维
- **OAM**：操作与维护总称（802.1ag + SAA 等）<<<PAGE 12>>>
- **MEP / MIP**：维护关联端点 / 中间点；MIP 自动创建 <<<PAGE 45>>>
- **LBM/LBR、LTM/LTR**：L2 ping 与 L2 trace 的消息/应答 <<<PAGE 46>>>
- **SAA（Service Assurance Agent）**：时延/抖动/丢包自动测试 <<<PAGE 47>>>
- **Overload 状态**：让节点退出中转的维护手段，可定时回退 <<<PAGE 48>>>
- **Graceful Restart**：主备切换期间保邻接保转发的平滑重启 <<<PAGE 48>>>
- **DHL（Dual-Home Link）**：无 STP/LAG 的双归属快速倒换特性 <<<PAGE 49>>>
- **链路度量（Link Metric）**：1–16M 整数，默认 10，建议按速率反比设置且两端同改 <<<PAGE 54>>>
- **Trusted/Un-trusted SAP**：信任 SAP 拷贝入向 VLAN tag 的 CoS，非信任 SAP 强制用户定义值 <<<PAGE 54>>>
- **命名规范**：ACC-31（BEB3 第 1 台接入交换机）、linkagg 13（BCB-1↔BEB-3）<<<PAGE 64>>>

## principles

- **P1 用链路状态协议取代生成树，释放全部链路**：SPB 的无环拓扑由 IS-IS 运行 Dijkstra SPF 构建，"no network link is disabled, all paths are available and traffic between any pair of nodes follows the shortest path" <<<PAGE 7>>>
- **P2 每个节点都是自己树的根，路径天然最短**：STP 单根导致非根节点间绕行；SPB 中 "every node builds a topology tree rooted on itself" <<<PAGE 11>>>
- **P3 单协议原则：一个 IS-IS 搞定拓扑、地址学习与 VPN 路由**：MPLS 需要 LDP/OSPF/MP-BGP 协议栈，SPB "relies on a single protocol to provide this functionality: IS-IS" <<<PAGE 6>>>
- **P4 MAC-in-MAC 封装把客户 MAC 学习限制在边缘**：核心节点 "do not learn any end-device MAC addresses, thus increasing the network scalability and stability" <<<PAGE 7>>>
- **P5 多租户原生支持，租户间地址空间可重叠**："Customers, or IoT device groups, segregated into different VPNs are isolated… can use overlapping address space without conflict" <<<PAGE 7>>>
- **P6 服务标识用 24 位 ISID，突破 4096 上限**："SPB's scalability is not limited to 4096 tenants because its service identifier, the ISID, is a 24-bit field which can differentiate up to 16M services" <<<PAGE 7>>>
- **P7 动态服务实例化：服务随人/设备走**："The network configuration dynamically adapts to mobile users and devices or Virtual Machines (VMs) migrations without need for Move, Add or Change requests" <<<PAGE 8>>>
- **P8 短时服务更安全**：临时性服务 "cannot be scanned, DoSd, or otherwise hacked, while they're not active" <<<PAGE 8>>>
- **P9 仅边缘供给：核心零触碰**："SPB services need only be provisioned on edge nodes, not on core nodes… service MACs can be conducted during business hours" <<<PAGE 8>>>
- **P10 微分段防横向移动**：UNP 内的 ACL "can allow communication between the camera and surveillance servers but at the same time block camera-to-camera communication" <<<PAGE 8>>>
- **P11 非 IP 核心更安全**：核心节点无 IP 地址，IS-IS 不跑在 IP 之上，"protects it from IP-based attacks such as scanning, spoofing, DoS" <<<PAGE 9>>>
- **P12 数据面只查表不做决策**：DP "makes no decisions… It simply performs lookups on the Forwarding Data Base (FDB)" <<<PAGE 9>>>
- **P13 BVLAN 的 FDB 由控制面预填充，不用泛洪学习**："the BVLAN domain's FDB is pre-populated by the CP" <<<PAGE 9>>>
- **P14 骨干内只按 BMAC 转发，CMAC 不进入骨干**："traffic is forwarded based on the destination BMAC (B-DA). Inner customer MACs are not learnt or used for forwarding within the backbone" <<<PAGE 9>>>
- **P15 BCB 不学任何客户 MAC**：BCB "does not have to learn any of the customer MAC addresses. It mainly serves as a transit bridge" <<<PAGE 10>>>
- **P16 双重防环：预防 + 缓解**："SPB implements two loop avoidance mechanisms: loop prevention and loop mitigation" <<<PAGE 10>>>
- **P17 每节点每 BVLAN 建一棵 SPF 树，ECT-ID 用于打破平局**："Assigning different ECT-IDs to different BVLANs helps those BVLANs build different trees" <<<PAGE 12>>>
- **P18 按服务（而非按包）负载分担**："SPB networks do not balance loads on a packet-by-packet basis like IP networks do" <<<PAGE 11>>>
- **P19 路径确定性与帧有序送达**："network paths are deterministic and frames are delivered in the order they were sent… important for storage and real-time application traffic" <<<PAGE 12>>>
- **P20 路径对称性利于 OAM**："the path from node X to node Y is identical to the path from node Y to node X… one-way delay calculations can be easily derived from roundtrip delay measurements" <<<PAGE 12>>>
- **P21 服务成员信息经 IS-IS TLV 泛播，全网视图一致**："SPB service membership information is shared across the SPB backbone by way of IS-IS TLVs" <<<PAGE 13>>>
- **P22 SDP 动态生成，只为有 SAP 的远端 BEB 创建**："SDPs are dynamically created in the CP and only for those far-end BEBs with SAPs for the specific service" <<<PAGE 14>>>
- **P23 BUM 复制模式按带宽/资源取舍选择**：head-end 省资源费带宽、tandem (S,G) 省带宽费资源、tandem (*,G) 折中，"Refer to Table 1 to compare these three modes" <<<PAGE 16>>>
- **P24 head-end 复制与单播路径同轨（同余性）**："Head-end replicated BUM traffic simply uses the unicast FDB and therefore travels along the same path. This property is known as congruency" <<<PAGE 15>>>
- **P25 BVLAN 数量对齐物理等价路径数**："Only create as many BVLANs as there are equal-cost-paths in the physical topology" <<<PAGE 52>>>
- **P26 VLAN 与服务一对一映射，防止 mac-move**："we strongly recommend mapping different VLANs to different SPB services (ISIDs). This will require one SAP and ISID per access VLAN" <<<PAGE 52>>>
- **P27 服务号本地有效，ISID/BVLAN 全局一致**："The service number is only locally significant… The ISID number is globally significant and must match across all BEBs" <<<PAGE 21>>>
- **P28 L3 服务靠边缘路由**："Routing is only performed at ingress and egress BEBs and bridged between these… the WAN represents a single L3 hop" <<<PAGE 29>>>
- **P29 L3 VPN 复用 SPB IS-IS 传客户路由**：IS-IS 同时承担骨干可达性与 VPN 路由传递，"Using a single protocol instead of two, results in a network that is simpler to deploy and operate" <<<PAGE 30>>>
- **P30 域内选 L3 VPN、边界用 VPN Lite**："L3 VPN is recommended within the SPB domain and VPN Lite is needed only on border nodes connecting to the outside world" <<<PAGE 34>>>
- **P31 共享服务经 VRF 泄漏实现，前提地址空间不重叠**："customer A's and B's address space must not overlap with each other nor with the shared services" <<<PAGE 34>>>
- **P32 出厂默认即近零接触**："A factory-default Alcatel-Lucent OmniSwitch has these mechanisms enabled by default and will automatically attempt to create an SPB backbone and services" <<<PAGE 36>>>
- **P33 单链路也建 linkagg，引用逻辑名利于扩展**："by referencing the (logical) linkagg as opposed to the (physical) port in other configuration commands, those configuration commands do not need to change when additional member ports are added" <<<PAGE 37>>>
- **P34 静态绑定 UNP（而非 SAP）解决静默设备问题，配置更标准**："by statically binding a UNP instead of a SAP, the exact same UNP constructs can be used for both silent and non-silent devices… This is considered a best practice" <<<PAGE 39>>>
- **P35 动态服务按 VLAN 标签即时创建，避免预置 4096 服务**：预配全部 VLAN "is a poor practice as it creates an unnecessary load on the control plane" <<<PAGE 42>>>
- **P36 ISID 用公式派生保证无冲突**：ISID = Base Service Number + Domain ID + (VLAN % Service Modulo)；BSN 隔离手工与动态服务编号空间 <<<PAGE 42>>>
- **P37 Service Modulo 调成 4096 保证 L2 隔离**：默认 512 会让最多 8 个 VLAN 映射到同一服务，"To ensure L2 isolation, we can change the Service Modulo to 4096" <<<PAGE 43>>>
- **P38 Domain ID 保多租户动态隔离**："Isolation is achieved by creating a Domain ID for each customer and by the mapping customer's UNI ports to the Domain" <<<PAGE 43>>>
- **P39 管理流量独立 VRF**："management IP addresses should use a different VRF from the VRF used for service or customer traffic" <<<PAGE 55>>>
- **P40 带内管理直接挂控制 BVLAN，免回环**：控制 BVLAN 上的 IP 接口 "do not rely on ARP… IP-to-MAC mapping is resolved through IS-IS TLVs" <<<PAGE 44>>>
- **P41 overload 状态做无扰维护**："Setting the overload state on the node will signal other nodes not to use it as a transit node" <<<PAGE 48>>>
- **P42 graceful restart 平滑主备切换**：重启节点置 RR 位并沿用现有 FDB，邻居维持邻接并回灌 LSP 数据库 <<<PAGE 48>>>
- **P43 CE 接入冗余四档递进**：非冗余 → 冗余链路（LAG）→ 冗余链路+节点（DHL/路由协议）→ 全冗余（MSTP/VRRP）<<<PAGE 49>>>
- **P44 光纤走物理分离路径**："fibre runs should use diverse physical paths to protect against fibre cuts" <<<PAGE 49>>>
- **P45 RPFC 利用对称性破瞬态环**："RPFC verifies that incoming traffic's source BMAC is indeed reachable over the ingress interface according to the local FDB and discards non-conforming frames" <<<PAGE 51>>>
- **P46 LBD 应在所有 UNI 口启用**："LBD should be enabled on all UNI ports" <<<PAGE 51>>>
- **P47 VC 场景 LAG 成员跨槽分布**："one member (physical) port connects to every slot in the VC… will improve the network convergence time in the event of slot failure" <<<PAGE 53>>>
- **P48 LAG 哈希需启用 tunnel-protocol 才能利用内层信息**：MAC-in-MAC 使外层只剩 BMAC，"this does not create enough entropy"，启用后可按 CMAC 或 IP+端口哈希 <<<PAGE 53>>>
- **P49 链路度量按速率反比设置**：Table 3 建议 100G=1000 … 1G=100000，"help steer traffic towards links with higher capacity" <<<PAGE 54>>>
- **P50 度量必须两端同时改**："the metric must be adjusted on both sides of a link" <<<PAGE 54>>>
- **P51 QoS 分类只在 SAP 做，骨干内保持不变**："traffic is classified at the SAP and the classification does not change as traffic traverses the backbone" <<<PAGE 54>>>
- **P52 两次路由时标准 VLAN 口信任 CoS 而非 DSCP**："the standard VLAN port must best set to trust and use CoS and not DSCP to preserve CoS markings end-to-end" <<<PAGE 54>>>
- **P53 NAC 动态 SAP 让服务按需上线**："no service is instantiated on a BEB until an authorized user successfully authenticates… more difficult to hack… a service when it is not even connected" <<<PAGE 55>>>
- **P54 外部路由协议启用认证防路由投毒**："This risk can be mitigated by enabling routing protocol authentication (e.g. MD5 for OSPF or BGP)" <<<PAGE 56>>>
- **P55 命名规范降低运维认知负担**：接入交换机 "ACC-31"（BEB 号+序号）、linkagg "13"（BCB 号+BEB 号）<<<PAGE 64>>>
- **P56 ISID/VLAN/服务号同号便于心智映射**："Although we use the same number for the service, ISID, and VLAN in this guide to maintain a good mentale map… they serve different purposes" <<<PAGE 70>>>
- **P57 VRRP 虚地址统一用 .1，末位对应 BEB 号**："We reserve .1 for the VRRP interface"，BEB-3 用 .3、BEB-4 用 .4 <<<PAGE 74>>>
- **P58 PBR 上的 /30 点对点互联各 VRF**：接口名 "source-destination" 格式（corp3-pbr / pbr-corp3）<<<PAGE 77>>>
- **P59 VRRP tracking 联动上行链路**：上行断则优先级 120−25=95，"By decreasing the priority when the link fails, the second VRRP router takes over as the master" <<<PAGE 78>>>
- **P60 VRF 间隔离由 PBR 强制，VRF 内再叠加 DHCP snooping/DAI**："for additional intra-VRF security (e.g. guest-to-guest isolation), it is advised to implement DHCP snooping, dynamic ARP inspection" <<<PAGE 80>>>
