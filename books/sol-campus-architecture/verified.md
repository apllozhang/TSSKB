# Verified 候选（V1 原文真实性核对 + V2/V3 抽查）

## cases

- **C1 VLAN 域 AP 发现配置流程**：`vlan 125 name "AP Management VLAN"` → 上联口打标 `vlan 125 members port 1/1/24 tagged` → `unp profile defaultWLANProfile map vlan 125` → AP 口设 UNP bridge `unp port 1/1/1 port-type bridge` → 按需 `unp port 1/1/1 ap-mode` → `mvrp enable` 传播管理与客户端 VLAN → 可选关认证/配 QoS 策略列表/认证旗标 → 配 system name/location/端口 alias 供 LLDP 向 AP 传位置信息 <<<PAGE 23>>>
- **C2 服务域（SPB）AP 发现配置流程**：`service l2profile "ap-SvcUnp" 802.1ab peer` → `unp port 1/1/1 port-type access` + `l2-profile ap-SvcUnp` + `ap-mode` → `unp profile defaultWLANAccessProfile map service-type spb tag-value 0 isid 1000 bvlan 4000` → 为客户端建服务画像 `unp profile spb10 map service-type spb tag-value 10 isid 1010 bvlan 4000` → 分类规则 `unp classification vlan-tag 10 profile1 spb10` <<<PAGE 25>>>
- **C3 AP 安全模式认证时序**：AP 发 LLDP-MED TLV 自证身份 → 交换机 UNP 规则归入 defaultWLANProfile 并回发带 Port VLAN ID 与位置的 LLDP → EAP Identity Request/Response → 802.1x 服务器认证成功 → AP 经 DHCP 拿地址并从 Option 138 得 OmniVista 地址 → MQTT 建管通道接收配置 <<<PAGE 20>>>
- **C4 Trust Tag 接纳客户端 VLAN**：AP 上线的客户端 DHCP 流量带 SSID 对应 VLAN tag → 交换机信任该标签并匹配本地 VLAN → 无则自动创建 → MVRP 向邻居分发 <<<PAGE 21>>>
- **C5 漫游判定操作矩阵**：新 AP 无客户端上下文→按新客户端处理；有上下文且 WLAN 服务/ARP 与 VLAN 映射一致→L2 漫游；有上下文但 VLAN 不匹配→L3 漫游（L2GRE 隧道回家乡 AP）<<<PAGE 26>>>
- **C6 L2GRE 隧道建立流程**：隧道接入交换机与汇聚交换机各配端点 → UNP 口收到的流量按 L2/L3 方法分类进 UNP 画像 → 画像映射 L2 GRE 服务 → GRE 封装送到汇聚交换机 → 解封装后进 VLAN 域上 perimeter/Internet <<<PAGE 17>>>
- **C7 mDNS 网关模式部署**：边缘交换机把 mDNS/SSDP 流量转发到网关交换机 → 网关按预配置 VLAN 共享列表在所有 VLAN 复制转发 <<<PAGE 33>>>
- **C8 mDNS Responder 模式部署**：核心交换机跑 Responder → 边缘交换机配 standard 型 L2GRE 隧道指向 Responder → 独立建 server policy 与 client policy → service rule 关联两者决定"哪些服务共享给哪些请求" <<<PAGE 33>>>
- **C9 RAP 远程接入流程**：AP 启动连 OmniVista Cirrus 按 MAC 识别 → 下发 VPN 服务器公网 IP、VPN 客户端 IP、SSID/射频参数与 OmniVista Enterprise 地址 → 双 VPN 建立后 OmniVista 2500 下发完整配置 → 远端用户连 SSID 经隧道入公司网，可拆分隧道直上互联网 <<<PAGE 31>>>
- **C10 OmniVista HA 部署选型**：Standalone 单机无故障切换；L2 HA 双 VM 同子网 + 虚拟 Cluster IP（原单机 IP 可复用）；L3 HA 双节点跨子网各持 IP，设备需同时配置双节点地址，Preferred Node 须在 CLI admin 菜单设置 <<<PAGE 35>>>
- **C11 AP Onboarding 流程**：AP 初联自动回连 Cirrus Activation Server → 序列号对 Device Catalog 校验 → 发证书建 VPN → 注册/授权/按 AP 组模板自动下发配置 <<<PAGE 36>>>
- **C12 WCF 配置三步**：建 WCF Profile（可含多条过滤条件）→ 给 ARP 或 SSID 挂 WCF Profile → 将 ARP/SSID 应用到 AP <<<PAGE 41>>>
- **C13 Mesh 建网约束**：有线上联者为 mesh root、无线上联者为 pure mesh；每 AP 最多 5 SSID + 5 条点对多点连接；全网最多 16 台 AP、任一链路最深 8 跳 <<<PAGE 29>>>
- **C14 访客认证四方式部署**：嵌入式 Captive Portal 自注册 / 社交登录（Facebook、Google、Rainbow、微信）/ 员工或访客操作员赞助审批 / SMS（Plivo）取凭证；默认记录保留一个月，可外接日志服务器延长 <<<PAGE 39>>>
- **C15 BYOD 注册管控**：用户经 UPAM Captive Portal 声明设备 → 挂符合安全策略的 ARP → 施加时限、会话超时、每人 1–10 台限制；认证源可选本地库/AD(LDAP)/代理外部 RADIUS <<<PAGE 40>>>

## counter-examples

- **X1 静态 VLAN 指定不可行**："static VLAN assignment of User VLANs is impractical and not recommended" <<<PAGE 8>>>
- **X2 全量建 VLAN 拖垮扩展性与稳定性**："Creating and tagging all possible VLANs is not recommended because this unnecessarily creates large L2 broadcast and STP domains which can lead to network scalability and stability problems" <<<PAGE 9>>>
- **X3 端口只能属于一个 untagged VLAN**："A port can only be assigned to one untagged VLAN… but it can be assigned to as many 802.1Q-tagged VLANs as necessary" <<<PAGE 9>>>
- **X4 集中控制器架构的三宗罪**："centralized controller-based architectures, which inherently suffer from various limitations such as single points of failure, traffic bottlenecks, and increased latency" <<<PAGE 15>>>
- **X5 集中控制器的持续成本**："the distributed control plane reduces both capital expenditures (CapEx) and operational expenditures (OpEx). The absence of a centralized controller eliminates the substantial initial costs… and the ongoing expenses related to its maintenance, power consumption, and cooling" <<<PAGE 16>>>
- **X6 单 AP 失败时邻 AP 自动补位（反衬集中式）**："if one AP fails, the neighboring APs can dynamically adjust their settings, such as increasing transmit power, to maintain seamless coverage" <<<PAGE 15>>>
- **X7 OmniVista 不逐台管 AP**："OmniVista does not manage individual APs"，必须经 AP 组管理 <<<PAGE 18>>>
- **X8 单 VLAN 按 AP 组分组的失败场景**："it becomes problematic in situations where large numbers of users congregate in a specific location, such as conference hall or large meetings room" <<<PAGE 28>>>
- **X9 2.4GHz 不适合语音**："utilizing the 5GHz frequency band is highly recommended due to its robust performance and lower interference compared to the 2.4GHz band" <<<PAGE 32>>>
- **X10 语音客户端超量掉质量**："limiting voice clients to 20-25 per Access Point (AP) ensures sufficient bandwidth and a stable 36 Mbps throughput" <<<PAGE 32>>>
- **X11 mDNS 传统模式的同网段安全风险**："traditionally, both the source and destination must be on the same SSID, posing a security risk. This setup often involves guest or BYOD devices, which may introduce threats to the network" <<<PAGE 32>>>
- **X12 组播低速率的效率问题**："Since multicast traffic is transmitted at lower broadcast rates, transforming multicast streams into unicast traffic can improve transmission efficiency" <<<PAGE 29>>>
- **X13 网桥模式 AP 不再服务客户端**："the access points forego the provision of regular WLAN services for client association" <<<PAGE 30>>>
- **X14 L3 HA 功能缺失**："Certain features, such as sFlow, policy enforcement, and specific device management functions, are not fully supported in a Layer 3 HA setup" <<<PAGE 36>>>
- **X15 L3 HA 冗余设置不能走界面**："redundancy settings such as setting a Preferred Node must be made through the CLI admin menu" <<<PAGE 36>>>
- **X16 安全不应绑定物理端口**："Rather than being tied to a specific switch port, security settings at the network edge are applied dynamically to each user or device based on predefined 'roles'" <<<PAGE 37>>>
- **X17 未注册设备不得入网**："it is issued the necessary certificates… ensuring that only registered devices are permitted to join the network"（onboarding 按序列号白名单）<<<PAGE 36>>>
- **X18 干扰 AP 不是直接安全威胁**："An interfering AP is visible within the wireless environment but is not connected to the wired network. While it may cause RF interference, it is not considered a direct security threat" <<<PAGE 41>>>
- **X19 流氓 AP 遏制默认关闭**："If an AP is classified as rogue, and containment is enabled (default is disabled), the detecting AP will send DEAUTH frames" <<<PAGE 42>>>
- **X20 传统资产盘点靠猜**："enterprises have had to rely on indirect methods such as feedback from users or speculative assessments… can lead to either under-procurement or over-procurement" <<<PAGE 34>>>
- **X21 Hybrid POL 并非处处适用，定位大园区**："ALE HPOL is the ideal solution for enterprises and organizations with large premises… over long distances, for medium to high user density" <<<PAGE 46>>>
- **X22 纯 ONT 架构能力受限**："Redundancy at all network layers is not required / Basic network features / Unified access is not required / Only PoE/PoE+ / Low IP port density"（对比 SFP ONT 架构）<<<PAGE 46>>>

## frameworks

- **F1 园区三层设计栈框架**：需求四目标（可用/扩展/安全/性能）→ 拓扑模型（两层折叠 vs 三层）→ 接入层构件（VC/Stack、VLAN+MVRP、Trunk、LACP）→ 互联技术选型（SPB/EVPN/MPLS 对比矩阵）→ 动态路由（OSPF/BGP/IS-IS/RIP）；全书 LAN 章节即按此栈逐层展开 <<<PAGE 6>>>
- **F2 Stellar 无控制器 WLAN 框架**：管理面集中（OmniVista Enterprise/Cirrus）+ 控制面分布（AP 间 over-the-air/over-the-LAN 经 NMP 同步 RF 与客户端上下文）+ 数据面本地桥接优先、按 ARP 动态切换 L2GRE 隧道；三种管理模式（Express/Enterprise/Cloud）与 AP 组/RF Profile 两级组织结构 <<<PAGE 15>>>
- **F3 AP 接入双域框架**：VLAN 域（bridge 口 + defaultWLANProfile map vlan + MVRP + Trust Tag）与服务域/SPB（access 口 + l2profile peer + defaultWLANAccessProfile map service-type spb + vlan-tag 分类规则）两条对称的发现-分类-映射路径，命令集互为镜像 <<<PAGE 23>>>
- **F4 漫游与用户移动框架**：客户端上下文共享 → 漫游判定矩阵（无上下文/上下文+ARP 匹配/上下文+VLAN 不匹配）→ L2 漫游（默认常开）/L3 漫游（L2GRE 回家乡 AP）/快速漫游（802.11r/k 预认证）；子网规划（/24 + VLAN 池）为该框架的容量底座 <<<PAGE 26>>>
- **F5 统一接入安全框架**：UPAM 中央 RADIUS+captive portal → 认证谱系（IoT 指纹/MAC、802.1x 员工、访客四式、SSID 分段、BYOD 声明）→ 角色（UNP/ARP）定 VLAN+ACL+QoS → 事后处置（Quarantine Manager+QMR 隔离补救、WCF 过滤、wIDS/wIPS 检测遏制）；安全贯穿"接入-授权-运行-处置"全生命周期 <<<PAGE 36>>>
- **F6 Hybrid POL 混合架构框架**：Nokia POL 光分配网（单纤点对多点+ONT）作物理承载 + ALE 以太接入交换机/Stellar AP 作服务边缘；按"是否需全层冗余与高级特性"分两档推荐架构；收益模型 = 铜缆/机房/有源设备/能耗四类成本节约 + 2.5G→10/40G 演进能力 <<<PAGE 45>>>

## glossary

- **Digital Age Networking**：ALE 网络理念：自治网络、IoT 安全接入、业务流程自动化三支柱 <<<PAGE 5>>>
- **两层折叠核心模型（Two-Layered Collapsed Core）**：核心与汇聚合并为单层，适合中小园区 <<<PAGE 7>>>
- **三层模型（Three-Tier Model）**：核心/汇聚/接入三层，适合大型复杂园区 <<<PAGE 7>>>
- **核心/汇聚/接入层**：高速骨干 / 聚合与策略 / 终端接入与分段 <<<PAGE 7>>>
- **虚拟机箱（VC/Stack）**：多台交换机经 VFL 环形互联为单逻辑设备，Master/Slave 选举 <<<PAGE 8>>>
- **LAN/WAN/MAN**：局域网 / 广域网 / 城域网 <<<PAGE 7>>>

## LAN 技术
- **VLAN**：逻辑分段广播域，接入层分管理 VLAN 与用户 VLAN <<<PAGE 8>>>
- **MVRP**：多 VLAN 注册协议，按需动态创建/传播 VLAN，收敛广播与 STP 域 <<<PAGE 9>>>
- **Trunking（802.1Q）**：单链路承载多 VLAN 打标流量 <<<PAGE 9>>>
- **LACP / LAG**：链路聚合控制协议 / 聚合组，带宽与冗余 <<<PAGE 9>>>
- **SPB**：IEEE 802.1aq 最短路径桥接，大园区扁平 L2 与多租户 <<<PAGE 9>>>
- **EVPN**：以太网 VPN，BGP 信令在 L3 网上延伸 L2，支持多归属 <<<PAGE 10>>>
- **MPLS**：标签交换，流量工程与 QoS 强项 <<<PAGE 10>>>
- **OSPF**：链路状态 IGP，分区域（Area 0 骨干）扩展 <<<PAGE 11>>>
- **BGP**：路径向量协议，自治域间路由与 EVPN 信令 <<<PAGE 11>>>
- **IS-IS**：链路状态 IGP，运营商核心常用，双栈 <<<PAGE 12>>>
- **RIP**：距离向量协议，仅小型/教学网，不推荐大规模 <<<PAGE 12>>>
- **LSDB/LSA/LSP**：链路状态数据库 / 通告 / 报文 <<<PAGE 11>>>

## WLAN 基础
- **OmniAccess Stellar**：ALE 无控制器 Wi-Fi 7/6E/6/5 AP 产品族（含户外加固型）<<<PAGE 5>>>
- **AWOS**：Stellar AP 操作系统 <<<PAGE 5>>>
- **AOS**：OmniSwitch 操作系统 <<<PAGE 6>>>
- **RF 规划**：覆盖/容量/信道/安装密度/功率天线/预测热图/RDA 七要素设计流程 <<<PAGE 12>>>
- **Floor Plan**：OmniVista 楼层规划仿真应用 <<<PAGE 12>>>
- **Wi-Fi 热图（Heatmap）**：实时信号与用户密度可视化 <<<PAGE 14>>>
- **RDA（Radio Dynamic Adjustment）**：射频动态调整技术（含 DFS/TPC）<<<PAGE 14>>>
- **NMP（Neighbor Management Protocol）**：AP 间空口/有线广播管理信息发现协议 <<<PAGE 5>>>
- **over-the-air / over-the-LAN**：AP 邻居交换的两种通道 <<<PAGE 5>>>
- **分布式控制面**：控制功能分散到所有 AP、无物理控制器的架构 <<<PAGE 15>>>
- **本地桥接（Bridging）**：AP 直接将 802.11 帧 转 802.3 上交换网的转发方式 <<<PAGE 16>>>
- **L2GRE 隧道**：二层通用路由封装，功能类似 VXLAN 的 L2 overlay <<<PAGE 17>>>
- **Wi-Fi Express / Enterprise / Cloud**：Stellar 三种管理模式（默认小规模 / 本地 NMS / Cirrus 云订阅）<<<PAGE 18>>>
- **AP 组**：OmniVista 管理 AP 的基本单位 <<<PAGE 18>>>
- **RF Profile**：信道/功率/带宽等射频参数集，绑定 AP 组 <<<PAGE 18>>>
- **PoE / PoE+ / Hi-PoE / PSE / PD**：以太网供电族与供电/受电角色；Stellar AP 下行口可作 PSE <<<PAGE 14>>>

## AP 接入与漫游
- **defaultWLANProfile**：VLAN 域内置 AP 管理 UNP 画像 <<<PAGE 23>>>
- **defaultWLANAccessProfile**：服务域内置 AP 管理 UNP 画像 <<<PAGE 24>>>
- **ap-mode**：UNP 端口开启 AP 检测模式 <<<PAGE 23>>>
- **LLDP-MED**：媒体终端 LLDP 扩展，AP 自证身份的 TLV 载体 <<<PAGE 19>>>
- **DHCP Option 138**：向 AP 下发 OmniVista 服务器地址的选项 <<<PAGE 20>>>
- **MQTT**：AP 与 OmniVista 间的管理通道协议 <<<PAGE 20>>>
- **Trust Tag**：交换机信任 AP 客户端流量 VLAN 标签并按需建 VLAN 的机制 <<<PAGE 21>>>
- **漫游（Roaming）**：客户端在 AP 间无缝切换 <<<PAGE 25>>>
- **家乡 AP / 外来 AP（home/foreign）**：L3 漫游中客户端原始关联与新关联 AP <<<PAGE 27>>>
- **客户端上下文（Client Context）**：AP 间共享的漫游所需客户端信息 <<<PAGE 26>>>
- **快速漫游（Fast Roaming）**：802.11r/802.11k 预认证加速切换 <<<PAGE 27>>>
- **L2 / L3 漫游**：同子网漫游保 IP / 跨子网漫游经 L2GRE 隧道保 IP <<<PAGE 27>>>
- **SSID / BSSID**：网络名 / 每 AP 唯一基本服务集标识 <<<PAGE 28>>>
- **VLAN 池（VLAN Pooling）**：一个 ARP 关联多个 VLAN，多用户 VLAN 场景首选 <<<PAGE 28>>>
- **WMM（802.11e）**：四队列无线 QoS（Voice/Video/Best Effort/Background）<<<PAGE 29>>>
- **DPI**：深度包识别，支撑应用可见与角色管控 <<<PAGE 29>>>
- **带宽契约（Bandwidth Contract）**：按角色或 SSID 限上下行带宽 <<<PAGE 29>>>

## 专项用例
- **Auto Mesh**：自动组网 mesh；mesh root / pure mesh AP、16 AP/8 跳上限 <<<PAGE 29>>>
- **点对点网桥（Wi-Fi Bridge）**：双 AP 专线互连两地网络，WPA2/WPA3 PSK 保护 <<<PAGE 30>>>
- **RAP（Remote Access Point）**：远程 AP，经双 VPN 安全接入公司网 <<<PAGE 31>>>
- **拆分隧道（Split Tunnelling）**：RAP 场景互联网流量直出 <<<PAGE 31>>>
- **VoWLAN**：无线语音；5GHz、每 AP 20–25 语音客户端等设计约束 <<<PAGE 32>>>
- **mDNS / SSDP**：服务发现协议；ALE Relay 跨网段转发（gateway/responder 两模式）<<<PAGE 32>>>
- **BLE 资产追踪（Asset Tracking）**：BLE 标签 + AP 定位 + 云位置引擎 <<<PAGE 34>>>

## 管理与安全
- **OmniVista Enterprise / Cirrus**：本地 NMS / 云 NMS <<<PAGE 35>>>
- **L2 HA / L3 HA**：OmniVista 双机高可用两种架构（Cluster IP / 跨子网双址）<<<PAGE 35>>>
- **Call-home / Device Catalog**：AP 回连激活服务器与序列号设备目录 <<<PAGE 36>>>
- **统一接入（Unified Access）**：有线无线一致的安全与策略框架 <<<PAGE 36>>>
- **UNP / ARP**：OmniSwitch 用户网络画像 / Stellar 接入角色画像 <<<PAGE 36>>>
- **UPAM（Unified Policy Access Manager）**：OmniVista 内嵌 RADIUS+captive portal 统一策略平台 <<<PAGE 19>>>
- **Access Guardian**：内嵌于交换机/AP 的认证+访问控制框架 <<<PAGE 37>>>
- **NAC**：网络准入控制；可对接 ISE、ClearPass、NPS <<<PAGE 36>>>
- **IoT 指纹（IoT Fingerprinting）**：按设备行为特征识别认证 IoT <<<PAGE 38>>>
- **802.1X / EAP**：端口认证框架与承载协议 <<<PAGE 20>>>
- **WPA2 / WPA3 / SAE**：无线加密标准；WPA3 的对等同时认证抗离线字典攻击 <<<PAGE 39>>>
- **Enhanced Open（OWE）**：免密自动加密的开放网络，适合访客 <<<PAGE 39>>>
- **BYOD**：自带设备；声明注册 + 时限/数量限制策略 <<<PAGE 40>>>
- **Quarantine Manager / QMR**：告警触发隔离应用与补救特性 <<<PAGE 40>>>
- **WCF（Web Content Filtering）**：按 URL/关键词/类别过滤网页访问 <<<PAGE 41>>>
- **wIDS/wIPS**：无线入侵检测/防御；干扰 AP 与流氓 AP 分类 <<<PAGE 41>>>
- **DEAUTH 遏制**：向流氓 AP 客户端发解除认证帧阻断连接 <<<PAGE 42>>>

## Hybrid POL
- **Hybrid POL（HPOL）**：ALE 混合无源光局域网方案（POL+以太 LAN）<<<PAGE 44>>>
- **POL（Passive Optical LAN）**：无源光局域网，单纤点对多点分发 <<<PAGE 45>>>
- **ONT（Optical Network Terminal）**：光网络终端；SFP ONT 与普通 ONT 两形态 <<<PAGE 45>>>
- **分光（Split Levels）**：POL 光分配层级 <<<PAGE 45>>>

## principles

## LAN 设计
- **P1 园区网四目标**："The key goals of any campus network architecture are to ensure high availability, scalability, security, and performance" <<<PAGE 5>>>
- **P2 Digital Age Networking 三支柱**：自治网络（自动安全连接人/流程/应用/物）、IoV 安全分段接入、业务流程自动化创新 <<<PAGE 5>>>
- **P3 两层折叠核心适合中小网**："Its simplified design reduces network complexity… requires fewer hardware components… reduces the number of hops data must traverse" <<<PAGE 7>>>
- **P4 三层模型适合大型复杂网**："modular structure enhances scalability… The core layer's high availability and fault tolerance ensure continuous network operation" <<<PAGE 7>>>
- **P5 接入层堆叠/VC 扩端口密度并保控制面韧性**："An election process designates one unit as the Master… In the event of a Master failure, the Slave seamlessly assumes control" <<<PAGE 8>>>
- **P6 接入 VLAN 动态分配，静态指定不可行**："static VLAN assignment of User VLANs is impractical and not recommended"；VLAN 按 Network Profile 规则随设备/用户动态变化 <<<PAGE 8>>>
- **P7 不要全量建 VLAN，用 MVRP 收敛广播/STP 域**："Creating and tagging all possible VLANs is not recommended because this unnecessarily creates large L2 broadcast and STP domains"；MVRP 按需动态创建并上联打标，"eliminating Moves, Adds and Changes" <<<PAGE 9>>>
- **P8 AP 管理 VLAN 与有线管理 VLAN 分开**："Different Management VLANs for Access Switches and WLAN Access Points are recommended"；AP 管理 VLAN 单独 ID、每 VLAN 最多 64 台 AP <<<PAGE 8>>>
- **P9 无线客户端建议独立 VLAN ID**："it is recommended to reserve a separate VLAN ID for wireless clients" <<<PAGE 8>>>
- **P10 同一 SSID 跨 AP 组可配不同 VLAN，助力 L3 漫游**："Different VLANs can be assigned to the same SSID across various AP groups, which can facilitate Layer 3 roaming" <<<PAGE 8>>>
- **P11 Trunk 统一 VLAN 分发保策略一致性**：802.1Q 打标使 "devices to maintain their VLAN assignments as they move within the network" <<<PAGE 9>>>
- **P12 LACP 是接入层韧性与带宽基线**：自动聚合、故障自动重路由、"treating multiple links as a single logical connection" 简化管理 <<<PAGE 9>>>
- **P13 SPB 用于大园区扁平化扩展**："For large campuses, it allows networks to scale efficiently with thousands of VLANs while simplifying management through a flat Layer 2 topology" <<<PAGE 10>>>
- **P14 EVPN 价值在跨广域 L2 互联与多归属**："facilitates the extension of VLANs across a wide area network… support of multi-homing enables a customer edge device to connect to multiple provider edge devices" <<<PAGE 10>>>
- **P15 MPLS 价值在流量工程与 QoS**："flexibility to route data via optimal paths tailored for specific traffic types" <<<PAGE 11>>>
- **P16 动态路由选型按规模**：OSPF 分区可扩展、BGP 多 ISP 互联与 EVPN 信令、IS-IS 大型核心；RIP "is not recommended for advanced or expansive network setups" <<<PAGE 12>>>
## WLAN 设计
- **P17 RF 规划先行，用工具仿真验证**：OmniVista Floor Plan "allows administrators to simulate and visualize RF environments accurately" <<<PAGE 12>>>
- **P18 容量规划按用户/应用画像**："considering factors such as location, usage patterns, and application types" <<<PAGE 13>>>
- **P19 AP 安装位置按场景**：室内首选吸顶（覆盖广无遮挡）、壁挂方向性覆盖、室外抱杆/外墙 <<<PAGE 13>>>
- **P20 PoE 简化布线与供电**："Stellar APs leverage Power over Ethernet (PoE) for simplified installation" <<<PAGE 14>>>
- **P21 RDA 自动调优射频**：DFS/TPC 自动选道调功率，"without disrupting connected clients" <<<PAGE 15>>>
- **P22 分布式控制面消除单点与瓶颈**："decentralizes the control functions, dispersing them across all APs… removes the single point of failure associated with centralized control systems" <<<PAGE 15>>>
- **P23 分布式控制面降 CapEx/OpEx**："The absence of a centralized controller eliminates the substantial initial costs… scales naturally with the addition of new APs" <<<PAGE 16>>>
- **P24 数据面默认本地桥接保性能**："directly bridging most data traffic at the AP level… significantly reduces latency, avoids potential throughput bottlenecks" <<<PAGE 16>>>
- **P25 安全或集中审查场景才隧道化**："When security policies demand centralized traffic inspection, tunneling effectively channels traffic through a central point… particularly useful for managing guest traffic" <<<PAGE 17>>>
- **P26 桥接/隧道按角色动态二选一**："flexibility to dynamically choose between bridging and tunneling based on the Access Role Profile (ARP) assigned to users" <<<PAGE 17>>>
- **P27 三种管理模式按规模递进**：Wi-Fi Express（默认小场景）/ Enterprise（本地 OmniVista 最大扩展）/ Cloud（Cirrus 订阅）<<<PAGE 18>>>
- **P28 按 AP 组管理而非单 AP**："OmniVista does not manage individual APs"，组级统一配置与策略下发 <<<PAGE 18>>>
- **P29 RF Profile 承接 RF 规划结果并绑定 AP 组**："RF profile is to be created following the RF planning survey and is linked to an AP group" <<<PAGE 18>>>
- **P30 AP+交换机同厂协同价值**：UPAM 统一有线无线认证、"automating essential tasks such as automatic AP discovery, provisioning, and VLAN creation" <<<PAGE 19>>>
- **P31 AP 安全模式多层验证**：LLDP-MED 识别 + 802.1x 认证 + DHCP Option 138 取 OmniVista 地址 + MQTT 建管通道 <<<PAGE 20>>>
- **P32 信任标签（Trust Tag）自动接纳 AP 客户端 VLAN**："If the switch does not have a matching VLAN, it will automatically create the necessary VLAN to handle the AP's client traffic" <<<PAGE 21>>>
- **P33 AP 管理流量 untagged、客户端流量 tagged 分离**："management traffic remains distinct from user data" <<<PAGE 21>>>
- **P34 漫游由客户端上下文共享驱动**：AP 间 over-the-air/over-the-LAN 交换 "client-specific contexts, containing critical information required to efficiently manage client transitions" <<<PAGE 26>>>
- **P35 漫游三分支判定**：新 AP 无上下文→新客户端；上下文+ARP 匹配→L2 漫游；上下文有但 VLAN 不匹配→L3 漫游 <<<PAGE 26>>>
- **P36 L3 漫游用 L2GRE 隧道保原 IP**："use a Layer 2 GRE tunnel to maintain the client's original IP address… without needing to reauthenticate" <<<PAGE 27>>>
- **P37 快速漫游靠预认证**：802.11r/802.11k "pre-authenticating clients with neighboring APs before the actual handoff occurs" <<<PAGE 27>>>
- **P38 子网收敛到 /24 利于管理与控制广播域**："limit subnet sizes to what is commonly known as a class C network… supports up to 253 devices per subnet" <<<PAGE 28>>>
- **P39 VLAN 池是用户 VLAN 首选法**："ALE advises using VLAN pools as the preferred method for managing user VLANs whenever multiple user VLANs are present" <<<PAGE 28>>>
- **P40 QoS 按角色动态施加**：角色同时定 VLAN 与 QoS 策略，语音视频优先 <<<PAGE 28>>>
- **P41 带宽契约与客户端限额治高密**："define 'bandwidth contracts' at the user/device role level or the SSID level… configure the maximum number of clients per band or per AP" <<<PAGE 29>>>
- **P42 组播转单播动态优化**：IGMP snooping 限制复制，"transforming multicast streams into unicast traffic can improve transmission efficiency"，超阈值自动回退 <<<PAGE 29>>>
- **P43 VoWLAN 硬指标**：优先 5GHz、每 AP 限 20–25 个语音客户端保 36 Mbps 吞吐、专用 SSID+漫游特性+QoS 优先 <<<PAGE 32>>>
- **P44 Mesh 适用于布线难场景**：露营地、历史保护建筑、室外临时活动 <<<PAGE 30>>>
- **P45 点对点网桥用 WPA2/WPA3 PSK 保护**："broadcasting a secure SSID configured with WPA2 or WPA3 PSK" <<<PAGE 30>>>
- **P46 RAP 双 VPN 通道安全回源**：先连 Cirrus 取配置，再与公司 VPN 服务器及 OmniVista 2500 建隧道，可拆分隧道 <<<PAGE 31>>>
- **P47 mDNS/SSDP 跨网段转发由防火墙审查**："allows devices to discover each other across different subnets. This enables a firewall to inspect multicast traffic between subnets" <<<PAGE 32>>>
- **P48 BLE 资产追踪复用 WLAN 基础设施**："leverages the existing Stellar infrastructure… with APs with built-in Bluetooth Low Energy (BLE) interfaces" <<<PAGE 34>>>
## NMS 与安全
- **P49 L2 HA 复用原 IP 零改造**："the existing IP address of the Standalone server can be reused as the Cluster IP, ensuring that no additional reconfiguration of devices is needed" <<<PAGE 35>>>
- **P50 L3 HA 跨子网但功能受限**："Certain features, such as sFlow, policy enforcement, and specific device management functions, are not fully supported in a Layer 3 HA setup" <<<PAGE 36>>>
- **P51 AP onboarding 走 call-home 验序列号发证书**："authenticated by verifying the device's serial number against the organization's Device Catalog" <<<PAGE 36>>>
- **P52 安全内建于网络并按角色施加，而非绑端口**："Security configurations at the network edge are dynamically applied based on 'roles' assigned to each user or device… rather than being statically linked to specific switch ports" <<<PAGE 36>>>
- **P53 UNP/ARP 内嵌于接入设备实现一致性策略**："integration of the User Network Profile (UNP for OmniSwitch) or Access Role Profile (ARP for Stellar) within the access layer switches and Access Points" <<<PAGE 36>>>
- **P54 统一策略源 UPAM 兼容外部认证与第三方 NAC**：内置 RADIUS+captive portal，可对 AD/LDAP/外部 RADIUS 认证，可代理对接 ClearPass/ISE <<<PAGE 37>>>
- **P55 IoT 指纹认证免手工配置保安全**："IoT fingerprinting authentication allows organizations to identify and authenticate IoT devices based on their unique network behavior" <<<PAGE 38>>>
- **P56 WPA3 优先但兼顾存量**："WPA3 is preferred when higher security is a priority"；WPA2 兼容旧设备 <<<PAGE 39>>>
- **P57 访客认证方式按场景选**：自注册、社交登录、员工赞助、SMS-Plivo；Enhanced Open 用于免密便捷场景 <<<PAGE 39>>>
- **P58 SSID 即分段**：不同 SSID 对应不同安全设置/VLAN/访问控制（如 Faculty vs Student）<<<PAGE 40>>>
- **P59 BYOD 分两类设备施策**：公司发放设备预置画像；外部设备走声明注册 + 时限/会话/数量（1–10 台/人）限制 <<<PAGE 40>>>
- **P60 隔离与处置闭环**：Quarantine Manager 依 syslog/SNMP trap 触发规则，"the device can be immediately quarantined or placed on a Candidate List"，QMR 提供补救路径 <<<PAGE 40>>>
- **P61 流氓 AP 判定与遏制**：rogue AP 接入有线或仿冒 SSID 才是威胁；遏制开启后 "the detecting AP will send DEAUTH frames to clients associated with the rogue AP" <<<PAGE 42>>>
## Hybrid POL
- **P62 POL+以太混合省铜缆省机房**："reduction of the copper cabling horizontal runs, and eliminates the need of dedicated telecom closets and cooling systems" <<<PAGE 45>>>
- **P63 POL 边缘交换机补 IP 密度与 PoE 预算**："provide for LAN networking services, and for higher IP port density and HPoE budget where needed" <<<PAGE 45>>>
- **P64 混合架构可去汇聚层**："point-to-multipoint optical infrastructure leads to the removal of the distribution switching layer in dense installations" <<<PAGE 45>>>
- **P65 两种推荐架构按需求分档**：需全层冗余/SPB/MACsec/高密 PoE → SFP ONT + OmniSwitch 接入；仅需基础特性 → 纯 ONT + Stellar AP <<<PAGE 46>>>
- **P66 光纤投资面向未来**："Guarantees evolution from 2.5 Gbps to 10/40 Gbps networks" <<<PAGE 46>>>
