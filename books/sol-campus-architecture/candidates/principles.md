# principles — sol-campus-architecture（P1…）

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
