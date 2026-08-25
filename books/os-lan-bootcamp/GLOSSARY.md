# GLOSSARY — OmniSwitch R6/R8 Bootcamp Issue 25 术语词典

> 从 verified.md 332 条术语中精选约 150 条，按五天主题分组，页码均出自原书。

## 硬件与产品线
- **OmniSwitch 6350**：入门级 L2+ 千兆堆叠交换机，SMB/分支场景 <<<PAGE 22-28>>>
- **OmniSwitch 6450**：L2+/基础 L3 千兆堆叠交换机，可选 10G 上联 <<<PAGE 113-121>>>
- **OmniSwitch 6465**：紧凑型工业加固交换机（-40~+75℃、DIN 导轨、1588v2/MACsec）<<<PAGE 42-49>>>
- **OmniSwitch 6560**：多千兆（mGIG）L2+/基础 L3 交换机，支持 2.5G/802.3bt <<<PAGE 30-39>>>
- **OmniSwitch 6860/6860E**：高级 L3 GE 接入/汇聚交换机，E 型带协处理器与 60W HPoE <<<PAGE 52-59>>>
- **OmniSwitch 6865**：下一代工业加固 L3 交换机（SPB、1588v2、75W HPoE）<<<PAGE 66-74>>>
- **OmniSwitch 6900 系列**：数据中心 TOR/园区核心（X/T/Q32/X72/V72/C32）<<<PAGE 78-94>>>
- **OmniSwitch 9907/9900**：7 槽模块化低时延机箱，直连架构无背板 <<<PAGE 96-107>>>
- **CMM**：Control Management Module，控制管理模块 <<<PAGE 99, 128>>>
- **NI**：Network Interface，业务线卡/网络接口模块 <<<PAGE 100-104>>>
- **CFM**：Chassis Fabric Module，机箱交换网板 <<<PAGE 105>>>
- **EMP**：Ethernet Management Port，带外以太网管理口 <<<PAGE 99, 153>>>
- **BPS（Omni BPS）**：备电柜，N+1/N+N 模式最多备 8 台 <<<PAGE 60-64>>>
- **SFP/SFP+/QSFP+/QSFP28**：光模块封装（1G/10G/40G/100G）<<<PAGE 91-94>>>
- **DAC**：直连铜缆（1/3/5/7 米）<<<PAGE 91>>>
- **MGIG（mGIG）**：多千兆以太网（2.5G/5G/10G BASE-T）<<<PAGE 30-35>>>
- **HPoE**：高功率 PoE（60/75W，802.3bt 级）<<<PAGE 33, 54>>>
- **1588v2 (PTP)**：精密时间协议 <<<PAGE 43, 68>>>
- **ISSU**：不中断升级 <<<PAGE 20, 290>>>
- **CodeGuardian**：LGS 交换机软件三级加固技术 <<<PAGE 108-111>>>
- **Diversified Image**：CodeGuardian 衍生镜像（每版本 5 种）<<<PAGE 110-111>>>
- **ProActive Lifecycle Management**：OmniVista 2500 云端资产生命周期管理 <<<PAGE 1139-1140>>>
- **RCD**：Remote Chassis Detection，经 EMP 的 VC 脑裂检测 <<<PAGE 306>>>
- **VCSP**：Virtual Chassis Split Detection，经 helper 链路的分裂检测 <<<PAGE 307>>>
- **SSP**：Split Stack Protection，R6 堆叠分裂保护 <<<PAGE 274-275>>>

## AOS 系统与文件系统
- **AOS**：Ale Operating System（R6/R7/R8 三大版本系）<<<PAGE 5, 122>>>
- **Working Directory**：可写运行目录 <<<PAGE 126, 145>>>
- **Certified Directory**：只读认证目录，升级回退基准 <<<PAGE 126, 145>>>
- **Running Directory**：当前启动来源目录（R8 概念）<<<PAGE 146>>>
- **boot.cfg / boot.params**：配置文件 / 启动参数文件 <<<PAGE 127-128>>>
- **MiniBoot/BootROM**：引导加载器 <<<PAGE 128>>>
- **Trescue.img**：USB 灾难恢复镜像 <<<PAGE 139>>>
- **aossignature**：USB auto-copy 触发标志文件 <<<PAGE 140>>>
- **rollback-timeout**：重启回滚计时（no 表示不回滚）<<<PAGE 132, 149>>>
- **flash-synchro**：跨 CMM/堆叠成员同步 flash <<<PAGE 267-268, 285>>>
- **write memory / copy working certified**：保存配置 / 认证目录 <<<PAGE 148, 133>>>
- **modify running-directory**：R8 切换运行目录命令 <<<PAGE 148>>>
- **Configuration Snapshot**：配置快照文本，可 apply 恢复 <<<PAGE 164, 229-230>>>
- **WebView**：内置 Web 管理界面 <<<PAGE 169-170>>>
- **RCL（Remote Configuration Loading）**：开箱 DHCP+TFTP 自动装载 <<<PAGE 157-158, 941>>>
- **Bash shell**：R8 CLI 底层 shell（别名/管道/busybox）<<<PAGE 150-151>>>

## 账户与 AAA
- **admin 账户**：默认全权限（密码 switch，仅 console）<<<PAGE 176, 242>>>
- **default 账户**：新用户权限模板 <<<PAGE 176, 242>>>
- **AAA**：认证/授权/计费框架（RADIUS/LDAP/TACACS+）<<<PAGE 184-187>>>
- **End-User Profile**：R6 终端用户档案 <<<PAGE 177, 182>>>
- **NTP / Stratum**：网络时间协议 / 层级数 <<<PAGE 189>>>

## 堆叠与虚拟机箱
- **Stack / Slot-ID**：堆叠 / 成员槽号（boot.slot.cfg 保存）<<<PAGE 251, 256>>>
- **Pass-Through**：槽号冲突时的透传角色 <<<PAGE 255, 257>>>
- **takeover**：堆叠/VC 主备切换命令 <<<PAGE 260, 285>>>
- **MAC Retention**：堆叠主 MAC 保持机制 <<<PAGE 270-273>>>
- **Virtual Chassis (VC)**：R8 多机虚拟化成单交换机 <<<PAGE 289-290>>>
- **VFL**：Virtual Fabric Link，虚拟机箱互联链路 <<<PAGE 292>>>
- **Chassis ID / Group ID**：VC 机箱号与机组号 <<<PAGE 293>>>
- **vcsetup.cfg / vcboot.cfg / virtual_dir**：VC 双文件 / VC 配置目录 <<<PAGE 294, 932>>>
- **Auto-VC**：出厂自动 VFL/Chassis ID 协商 <<<PAGE 938-940>>>

## 诊断
- **swlog**：交换机日志（console/flash/syslog 三输出）<<<PAGE 325-332>>>
- **appid/subapp**：日志应用标识与级别控制 <<<PAGE 330-331>>>
- **command-log**：命令及结果日志（/flash/command.log）<<<PAGE 333-335>>>
- **Port Mirroring / RPM**：端口镜像 / 远程镜像（2 会话、128:1）<<<PAGE 336-338>>>
- **Port Monitoring**：本机抓包（Sniffer ENC 格式、前 64 字节）<<<PAGE 341-342>>>
- **RMON**：远程监控四组（统计/历史/告警/事件）<<<PAGE 343-344>>>
- **show health**：CPU/内存利用率与健康阈值 <<<PAGE 345-346>>>
- **sFlow**：RFC3176 流采样（receiver/sampler/poller 三要素）<<<PAGE 347-350>>>

## VLAN 与二层
- **VLAN / 默认 VLAN（VLAN 1）**：广播域 / 不可删的出厂 VLAN <<<PAGE 360, 385>>>
- **Static / Dynamic VLAN**：静态指派 / 规则动态指派 <<<PAGE 362-371>>>
- **Mobile Port / Mobile Tag**：R6 动态 VLAN 端口 / 多 VLAN 打标签机制 <<<PAGE 367, 381-383>>>
- **VLAN Rules**：VLAN 分类规则（MAC/网络地址/协议）<<<PAGE 368-370>>>
- **802.1Q Tag / 802.1p**：VLAN 标签（12bit VID）+ 3bit 优先级 <<<PAGE 377-379>>>
- **Inter-VLAN Routing / Virtual Router Port**：VLAN 间路由 / IP 接口旧称 <<<PAGE 372-373>>>
- **MVRP**：多 VLAN 注册协议（802.1ak，动态注册/裁剪）<<<PAGE 479, 967-971>>>
- **Dynamic VLAN（MVRP）**：MVRP 自动创建的 VLAN（type dyn）<<<PAGE 970>>>

## 链路聚合
- **Link Aggregation / LACP（802.3ad）**：链路聚合 / 聚合控制协议 <<<PAGE 394, 396>>>
- **OmniChannel**：ALE 静态聚合，仅限 OmniSwitch 间 <<<PAGE 396-397>>>
- **Actor Admin Key**：聚合端口关联键（两端一致）<<<PAGE 398, 404>>>
- **Primary Port**：聚合组主端口（组播默认出口）<<<PAGE 402, 405>>>
- **hash-control**：哈希算法控制（brief/extended/non-ucast）<<<PAGE 401-402>>>
- **DHL（Dual Home Link）**：双归属 Active-Active 上行冗余 <<<PAGE 476-481>>>
- **MAC Flushing**：DHL 变更后清陈旧 MAC（None/MVRP Enhanced/RAW）<<<PAGE 479-480>>>

## 生成树
- **STP / RSTP / MSTP**：802.1D / 802.1w（默认）/ 802.1s <<<PAGE 414-415, 437>>>
- **Flat / 1x1（Per-VLAN）模式**：每机一棵树 / 每 VLAN 一棵树（默认）<<<PAGE 427-429>>>
- **Root Bridge / Bridge Priority**：根桥 / 桥优先级（默认 32768）<<<PAGE 414, 425>>>
- **Alternate / Backup Port**：RSTP 替代/备份端口 <<<PAGE 423>>>
- **Path Cost**：路径开销（16/32bit 两套默认值）<<<PAGE 425, 432>>>
- **PVST+**：Cisco 每 VLAN 生成树互操作（须 1x1 模式）<<<PAGE 433-434>>>
- **CIST / MSTI**：公共内部生成树（实例 0）/ MST 实例（最多 16）<<<PAGE 438>>>
- **MST Region / Digest**：MST 域（名+修订+映射表）/ 映射摘要 <<<PAGE 440-443>>>

## IP 接口与 LLDP
- **Loopback0**：常驻环回管理接口（不绑 VLAN 恒 up）<<<PAGE 492>>>
- **ip managed-interface**：按应用指定源接口（R8）<<<PAGE 493>>>
- **DHCP Relay（ip helper）/ UDP Relay**：DHCP 中继 / 指定 UDP 端口中继 <<<PAGE 498-499>>>
- **LLDP（802.1AB）/ TLV**：链路层发现协议 / 信息单元 <<<PAGE 509-510>>>
- **LLDP-MED / Network Policy**：媒体终端扩展 / 语音策略 TLV（VLAN+802.1p+DSCP）<<<PAGE 513-515>>>
- **trust-agent**：LLDP 可信代理（Rogue 检测）<<<PAGE 801-802>>>
- **ECMP**：等价多路径 <<<PAGE 718, 723>>>

## VRRP
- **VRRP / VRID**：虚拟路由器冗余协议（RFC 2338）/ 虚拟路由器标识 <<<PAGE 522-524>>>
- **Virtual MAC**：00-00-5E-00-01-{VRID} <<<PAGE 524, 536>>>
- **Skew Time**：(256-Priority)/256，防多备同升 <<<PAGE 527>>>
- **VRRP Tracking / VRRP Group**：跟踪联动优先级 / 集体管理组 <<<PAGE 531-533>>>
- **HSRP**：Cisco 热备协议（与 VRRP 不兼容）<<<PAGE 524>>>

## QoS 与 ACL
- **CoS Queue**：每出端口 8 个服务等级队列 <<<PAGE 545-546>>>
- **Strict Priority / WRR / DRR / WFQ**：调度算法族 <<<PAGE 547, 552>>>
- **EF**：快速转发队列（限速保护）<<<PAGE 551-552>>>
- **QSet / QSI**：R8 队列组 / 队列组实例 <<<PAGE 548-549>>>
- **Policy Condition / Action / Rule**：策略三元组 <<<PAGE 544-545>>>
- **Precedence / Validity Period**：规则优先级（0-65535）/ 生效时段 <<<PAGE 573, 565>>>
- **Network/MAC/Service/Port Group**：策略复用组 <<<PAGE 569, 608>>>
- **Disposition（accept/drop/deny）**：策略处置动作 <<<PAGE 609>>>
- **qos apply / qos reset**：策略应用/清空 <<<PAGE 612, 592>>>
- **ToS/DSCP**：三层标记 <<<PAGE 543, 590>>>
- **SIP Snooping**：SIP 信令侦听自动语音 QoS <<<PAGE 601>>>
- **ACL / established / tcpflags**：访问控制 / TCP 已建连接 / TCP 标志条件 <<<PAGE 604-618>>>

## Access Guardian / UNP / IoT
- **Access Guardian (AG)**：端口自动感知多客户端认证 <<<PAGE 627, 630>>>
- **UNP**：Universal Network Profile 用户网络档案 <<<PAGE 631-632>>>
- **Filter-ID**：RADIUS 属性下发 UNP 名 <<<PAGE 632>>>
- **UNP Classification Rule**：设备分类规则（R8 十六级）<<<PAGE 638, 652-656>>>
- **Location / Period Policy**：按位置/时段限制角色 <<<PAGE 649-650>>>
- **Captive Portal**：Web 强制门户（终结策略）<<<PAGE 635, 1014>>>
- **IoT Device Profiling / DHCP Fingerprinting / MAC OUI**：设备画像 / DHCP 指纹 / 厂商标识 <<<PAGE 685-690>>>

## PoE
- **PoE（802.3af）/ PoE+（802.3at）**：15.4W / 30W 供电 <<<PAGE 694-695>>>
- **PSE / PD / PD Classification**：供电端 / 受电端 / 分级 <<<PAGE 695>>>
- **lanpower**：PoE 管理命令族 <<<PAGE 700-708>>>
- **Port Priority（low/high/critical）**：PoE 端口优先级 <<<PAGE 701>>>
- **Capacitor Detection / Priority Disconnect / Power Budget**：电容检测 / 新 PD 拒绝 / 总预算 <<<PAGE 702-703>>>

## 路由（静态/RIP/OSPF/BGP/IS-IS）
- **Static Route / Recursive（follows）/ Interface 型**：静态路由三形态 <<<PAGE 714-721>>>
- **Route Preference（ip route-pref）**：协议路由偏好 <<<PAGE 769>>>
- **RIP / RIP Timers**：路由信息协议 / update-invalid-garbage-holddown 四定时器 <<<PAGE 722-731>>>
- **Route Map（redistribution）**：路由图与重分发 <<<PAGE 726-727, 768>>>
- **OSPF / Router ID / Area**：链路状态协议 / 标识 / 区域 <<<PAGE 750-756>>>
- **LSDB / LSA Type 1-7 / Opaque LSA（9-11）**：链路状态库 / 通告类型（Type9 用于 GR）<<<PAGE 753-762>>>
- **ABR / ASBR**：区域边界 / 自治系统边界路由器 <<<PAGE 760-761>>>
- **Stub / Totally Stubby / NSSA / Virtual Link**：区域类型 / 虚链路 <<<PAGE 760-763>>>
- **Graceful Restart (GR) / Grace LSA / Helper**：优雅重启三件套 <<<PAGE 770-776>>>
- **BFD**：双向转发检测 <<<PAGE 711, 716>>>
- **BGP / IBGP / update-source**：边界网关协议 / 内部 BGP / 邻居更新源 <<<PAGE 1079-1082>>>
- **aspath-list / community-list / prefix-list**：BGP 策略三列表 <<<PAGE 1086-1088>>>
- **IS-IS / Level-1/Level-2 / DIS / LSP / CSNP/PSNP**：IS-IS 体系术语 <<<PAGE 1090-1101>>>
- **NSAP 地址 / AFI 49**：OSI 寻址 / 本地管理标识 <<<PAGE 1094-1095>>>

## VRF
- **VRF / Default VRF**：虚拟路由转发 / 默认实例 <<<PAGE 853-859>>>
- **VRF Route Leak / GRT**：VRF 间及与全局路由表的路由泄漏 <<<PAGE 863-864>>>

## 安全（LPS/PBR/Snooping/MACsec）
- **Learned Port Security (LPS)**：学习端口安全 <<<PAGE 803-809>>>
- **port-security violation restrict/shutdown**：违规过滤/关口 <<<PAGE 805>>>
- **convert-to-static / learn-trap-threshold**：MAC 固化 / 学习告警阈值 <<<PAGE 807-809>>>
- **PBR / permanent gateway**：策略路由 / 固定网关动作 <<<PAGE 810-813>>>
- **UserPorts / DropServices / port-disable action**：保留端口组 / 服务组 / 关口动作 <<<PAGE 816-818>>>
- **ARP Poisoning Detection / restricted-address**：ARP 毒化检测 / 受限地址 <<<PAGE 822-824>>>
- **MACsec（802.1AE）/ Static-Dynamic SA / SCI**：链路加密 / 安全关联模式 / 通道标识 <<<PAGE 825-827, 1049>>>
- **DHCP Snooping / Binding Table / Option 82**：DHCP 侦听 / 绑定库 / 中继选项 <<<PAGE 828-832>>>
- **Port Mapping / Dynamic Proxy ARP**：用户口-网络口映射 / 代理 ARP <<<PAGE 837-839>>>
- **Storm Control（flood rate）**：风暴控制 <<<PAGE 886>>>
- **BPDU Guard**：BPDU 保护 <<<PAGE 799>>>

## 组播
- **Class D 地址 / 01:00:5e MAC 映射**：组播地址与 23 位 MAC 映射 <<<PAGE 867>>>
- **IGMP（v1/v2/v3）/ Querier / Fast Leave / SSM**：成员管理协议族 <<<PAGE 870-872>>>
- **IPMS**：IP 组播交换（二层硬件侦听转发）<<<PAGE 869, 873-878>>>
- **Querier Forwarding / IGMP Proxying / IGMP Relay**：送查询者 / 代理 / 报文中继 <<<PAGE 877-884>>>
- **max-group（Throttling）**：端口/VLAN 组数限制 <<<PAGE 885>>>
- **PIM-SM / RP / BSR(CBSR) / Candidate-RP / SPT**：稀疏模式组播路由族 <<<PAGE 907-909>>>
- **groute / sgroute**：组路由 / 源组路由查看 <<<PAGE 912-913>>>

## ERP 与 Intelligent Fabric
- **ERP（G.8032）/ APS**：以太网环网保护 / 自动保护倒换协议 <<<PAGE 415, 926>>>
- **RPL / RPL Owner / R-APS Channel**：环保护链路 / 属主 / 协议信道 <<<PAGE 928-929>>>
- **Service VLAN / Protected VLAN / MEG Level**：ERP 业务/受保护 VLAN / 维护等级 <<<PAGE 928-930>>>
- **WTR（Wait To Restore） / Guard Timer / Pending-Protected 状态**：ERP 定时器与状态 <<<PAGE 929-930>>>
- **Intelligent Fabric (iFab) / Auto-fabric**：智能织构 / 零接触自动发现 <<<PAGE 68, 154-155, 933>>>
- **Auto-LACP / Auto-Routing / Auto-MVRP / Auto Network Profiling**：自动聚合/路由/VLAN 注册/档案 <<<PAGE 155, 943-944>>>
- **SPB（Shortest Path Bridging）**：最短路径桥接织构技术 <<<PAGE 68, 73>>>

## SLB 与 IPv6
- **SLB / VIP / SLB Cluster**：服务器负载均衡 / 虚拟 IP / 集群 <<<PAGE 972-976>>>
- **WRR（weight）/ SLB Probe / QoS Condition Cluster**：加权轮询 / 健康探针 / 条件集群 <<<PAGE 977-987>>>
- **IPv6 / :: 缩写 / Link-Local（FE80::/10）/ EUI-64 / NDP**：IPv6 基础族 <<<PAGE 1130-1138>>>

## 认证与课程
- **ACFE / ACSE**：ALE 认证资深组网工程师 / 交换专家 <<<PAGE 3>>>
- **Newcomer / Experienced Track**：新学员培养与老学员续证两轨 <<<PAGE 3-4>>>
- **DT00CTE120EN**：本 Bootcamp 课程编号 <<<PAGE 5>>>
