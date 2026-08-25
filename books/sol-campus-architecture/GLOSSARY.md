# GLOSSARY · 园区架构指南（sol-campus-architecture）

> 页码为原书 `<<<PAGE N>>>` 标记。按设计理念/LAN/WLAN/漫游/专项用例/管理安全/POL 分组，精选 45 条。

## 设计理念
- **Digital Age Networking**：ALE 网络理念：自治网络、IoT 安全接入、业务流程自动化三支柱 <<<PAGE 5>>>
- **园区网四目标**：高可用、可扩展、安全、性能 <<<PAGE 5>>>
- **两层折叠核心（Two-Layered Collapsed Core）**：核心汇聚合并单层，适合中小园区 <<<PAGE 7>>>
- **三层模型（Three-Tier Model）**：核心/汇聚/接入，适合大型复杂园区 <<<PAGE 7>>>
- **虚拟机箱（VC/Stack）**：多台交换机经 VFL 环形互联为单逻辑设备，Master/Slave 选举 <<<PAGE 8>>>

## LAN 技术
- **VLAN**：逻辑分段广播域，分管理 VLAN 与用户 VLAN <<<PAGE 8>>>
- **MVRP**：多 VLAN 注册协议，按需动态创建/传播 VLAN，收敛广播与 STP 域 <<<PAGE 9>>>
- **Trunking（802.1Q）**：单链路承载多 VLAN 打标流量 <<<PAGE 9>>>
- **LACP / LAG**：链路聚合控制协议/聚合组，带宽与冗余 <<<PAGE 9>>>
- **SPB**：IEEE 802.1aq 最短路径桥接，大园区扁平 L2 与多租户 <<<PAGE 9>>>
- **EVPN**：以太网 VPN，BGP 信令在 L3 网上延伸 L2，支持多归属 <<<PAGE 10>>>
- **MPLS**：标签交换，流量工程与 QoS 强项 <<<PAGE 10>>>
- **OSPF**：链路状态 IGP，分区域（Area 0 骨干）扩展 <<<PAGE 11>>>
- **BGP**：路径向量协议，自治域间路由与 EVPN 信令 <<<PAGE 11>>>
- **IS-IS**：链路状态 IGP，运营商核心常用，双栈 <<<PAGE 12>>>
- **RIP**：距离向量协议，仅小型/教学网，不推荐大规模 <<<PAGE 12>>>

## WLAN 基础
- **OmniAccess Stellar**：ALE 无控制器 Wi-Fi 7/6E/6/5 AP 产品族 <<<PAGE 5>>>
- **AWOS**：Stellar AP 操作系统 <<<PAGE 5>>>
- **RF 规划**：覆盖/容量/信道/安装密度/功率天线/预测热图/RDA 七要素设计流程 <<<PAGE 12>>>
- **Floor Plan**：OmniVista 楼层规划仿真应用 <<<PAGE 12>>>
- **RDA（Radio Dynamic Adjustment）**：射频动态调整（含 DFS/TPC）<<<PAGE 14>>>
- **NMP（Neighbor Management Protocol）**：AP 间空口/有线广播管理信息发现协议 <<<PAGE 5>>>
- **分布式控制面**：控制功能分散到所有 AP、无物理控制器的架构 <<<PAGE 15>>>
- **本地桥接（Bridging）**：AP 直接将 802.11 帧转 802.3 上交换网 <<<PAGE 16>>>
- **L2GRE 隧道**：二层通用路由封装，功能类似 VXLAN 的 L2 overlay <<<PAGE 17>>>
- **Wi-Fi Express / Enterprise / Cloud**：Stellar 三种管理模式 <<<PAGE 18>>>
- **AP 组 / RF Profile**：OmniVista 管 AP 的基本单位 / 绑定 AP 组的射频参数集 <<<PAGE 18>>>
- **PoE / PoE+ / Hi-PoE / PSE / PD**：以太网供电族；Stellar AP 下行口可作 PSE <<<PAGE 14>>>

## AP 接入与漫游
- **defaultWLANProfile / defaultWLANAccessProfile**：VLAN 域/服务域内置 AP 管理 UNP 画像 <<<PAGE 23>>>/<<<PAGE 24>>>
- **ap-mode**：UNP 端口开启 AP 检测模式 <<<PAGE 23>>>
- **LLDP-MED**：媒体终端 LLDP 扩展，AP 自证身份的 TLV 载体 <<<PAGE 19>>>
- **DHCP Option 138**：向 AP 下发 OmniVista 服务器地址的选项 <<<PAGE 20>>>
- **MQTT**：AP 与 OmniVista 间的管理通道协议 <<<PAGE 20>>>
- **Trust Tag**：交换机信任 AP 客户端 VLAN 标签并按需建 VLAN 的机制 <<<PAGE 21>>>
- **客户端上下文（Client Context）**：AP 间共享的漫游所需客户端信息 <<<PAGE 26>>>
- **L2 / L3 漫游**：同子网保 IP / 跨子网经 L2GRE 隧道保 IP <<<PAGE 27>>>
- **快速漫游（Fast Roaming）**：802.11r/802.11k 预认证加速切换 <<<PAGE 27>>>
- **VLAN 池（VLAN Pooling）**：一个 ARP 关联多个 VLAN，多用户 VLAN 首选 <<<PAGE 28>>>
- **WMM（802.11e）**：四队列无线 QoS <<<PAGE 29>>>
- **带宽契约（Bandwidth Contract）**：按角色或 SSID 限上下行带宽 <<<PAGE 29>>>

## 专项用例
- **Auto Mesh**：自动组网 mesh；16 AP/8 跳上限 <<<PAGE 29>>>
- **点对点网桥（Wi-Fi Bridge）**：双 AP 专线互连两地网络，WPA2/WPA3 PSK 保护 <<<PAGE 30>>>
- **RAP（Remote Access Point）**：远程 AP，经双 VPN 安全接入公司网 <<<PAGE 31>>>
- **拆分隧道（Split Tunnelling）**：RAP 场景互联网流量直出 <<<PAGE 31>>>
- **VoWLAN**：无线语音；5GHz、每 AP 20-25 语音客户端等约束 <<<PAGE 32>>>
- **mDNS / SSDP**：服务发现协议；ALE Relay 跨网段转发（gateway/responder 两模式）<<<PAGE 32>>>
- **BLE 资产追踪**：BLE 标签+AP 定位+云位置引擎 <<<PAGE 34>>>

## 管理与安全
- **OmniVista Enterprise / Cirrus**：本地 NMS / 云 NMS <<<PAGE 35>>>
- **L2 HA / L3 HA**：OmniVista 双机高可用两种架构（Cluster IP/跨子网双址）<<<PAGE 35>>>
- **Call-home / Device Catalog**：AP 回连激活服务器与序列号设备目录 <<<PAGE 36>>>
- **UPAM（Unified Policy Access Manager）**：OmniVista 内嵌 RADIUS+captive portal 统一策略平台 <<<PAGE 19>>>
- **UNP / ARP**：OmniSwitch 用户网络画像 / Stellar 接入角色画像 <<<PAGE 36>>>
- **Access Guardian**：内嵌于交换机/AP 的认证+访问控制框架 <<<PAGE 37>>>
- **IoT 指纹（IoT Fingerprinting）**：按设备行为特征识别认证 IoT <<<PAGE 38>>>
- **WPA3 / SAE / Enhanced Open**：无线加密标准与免密自动加密开放网络 <<<PAGE 39>>>
- **BYOD**：自带设备；声明注册+时限/数量限制策略 <<<PAGE 40>>>
- **Quarantine Manager / QMR**：告警触发隔离应用与补救特性 <<<PAGE 40>>>
- **WCF（Web Content Filtering）**：按 URL/关键词/类别过滤网页访问 <<<PAGE 41>>>
- **wIDS/wIPS / DEAUTH 遏制**：无线入侵检测防御；向流氓 AP 客户端发解除认证帧 <<<PAGE 41-42>>>

## Hybrid POL
- **Hybrid POL（HPOL）**：ALE 混合无源光局域网方案（POL+以太 LAN）<<<PAGE 44>>>
- **POL（Passive Optical LAN）**：无源光局域网，单纤点对多点分发 <<<PAGE 45>>>
- **ONT（Optical Network Terminal）**：光网络终端；SFP ONT 与普通 ONT 两形态 <<<PAGE 45>>>
- **分光（Split Levels）**：POL 光分配层级 <<<PAGE 45>>>
