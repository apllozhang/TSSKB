# OmniSwitch R6/R8 Bootcamp Issue 25 — 原理与机制候选（principles）

> 来源：books/os-lan-bootcamp/fulltext.md，页码为 `<<<PAGE N>>>` 标记。摘录保留英文原句供验证阶段特征词匹配。

## 一、产品与硬件（Day 1）

- **P1 OmniSwitch 家族定位分层**：堆叠（6350/6450/6560/6465）、加固（6465/6865）、模块化（6900/9900）三层产品线。原句："Stackable switch / Hardened Access Switch / Modular Switch" <<<PAGE 19>>>
- **P2 全线速率演进主线**：接入 100M→1G→2.5G，汇聚 1G→2.5G→10G，核心 10G→25G→40G→100G。原句："Speed increase at all layers of the enterprise" <<<PAGE 21>>>
- **P3 OS6350 定位**：入门 L2+ GE，SMB 市场，高级 L2 + 基础 L3（IPv4/IPv6），Auto-QoS、8 硬件队列。原句："Advanced L2 features with basic L3 routing for both IPv4 and IPv6" <<<PAGE 27>>>
- **P4 OS6560 MGIG 机型**：24Z8/24Z24/P48Z16 支持 100/1G/2.5G（802.3bt 75W），SFP+ 上联/堆叠二合一。原句："8 RJ-45 100/1G/2.5G Base T ports / PoE 802.3af/at/bt ports (up to 75W on a port)" <<<PAGE 33>>>
- **P5 OS6560 电源复用 6860 体系**：模块化 300/600/900W 电源负载分担，1RU 内实现冗余。原句："Re-use existing power supplies from the OS6860 PoE family… Allows for load sharing between supplies" <<<PAGE 39>>>
- **P6 OS6465 工业加固交换机**：-40~+75℃、DIN 导轨、1588v2 与 MACsec 全端口。原句："Designed for industrial applications / Operating Temperature -40 to +75 ℃" <<<PAGE 42-43>>>
- **P7 OS6860E 增强型差异**：内置协处理器跑 DPI/应用指纹（约 1000 签名发现、100 签名线速匹配），前 4 口 60W PoE，仅 E 型有 EMP 口。原句："Specialized built-in co-processor board… With AOS 8.1.1 the Application Monitoring / Fingerprinting function will run on it" <<<PAGE 52-56>>>
- **P8 OS6860E-P24Z8 2.5G 限制**：2.5G 端口需手动配置速率且成对修改。原句："Speed change on 2.5G Ports configurable only in pairs (17, 18), (19, 20)" <<<PAGE 55>>>
- **P9 Omni BPS 备电柜两种模式**：N+1（SINGLE）防电源模块故障、N+N（FULL）防市电线路故障。原句："N+1 also called SINGLE backup / Protects against switch primary PSU failure not against AC power line failure" <<<PAGE 63-64>>>
- **P10 OS6900 演进路线**：2011 10G 模块化 → 2015 40G 高密度 → 2018 25G/100G（X72/V72/C32）。原句："OS6900 evolution: 25G/100G" <<<PAGE 78>>>
- **P11 OS6900-Q32 线速条件**：每管道 ≤240Gbps 才线速，40G 口可分裂为 4x10G（a/b/c/d 子端口编号）。原句："Q32 is wire rate when each pipeline is 240 Gbps or less / The port numbering scheme changes by using letters a, b, c, d" <<<PAGE 85>>>
- **P12 V72/C32 独立镜像**：使用 Yos.img，与其余 OS6900（Tos.img）不同。原句："The OS6900-V72/C32 uses a different image file (Yos.img) than all other OS6900 models (Tos.img)" <<<PAGE 86-87>>>
- **P13 OS9907 无背板直连架构**：每槽直连交换网板，两阶段容量翻倍演进。原句："Innovative direct-connect architecture - Backplane less - Each slot connects to the fabric directly" <<<PAGE 98>>>
- **P14 OS9900 系统供电优先**：系统上电优先，剩余功率全部给 PoE，最高 10800W。原句："System power for board bring up takes priority / After system bring up all remaining power is available for PoE!" <<<PAGE 106-107>>>
- **P15 CodeGuardian 三层加固**：源码独立验证（IV&V）、软件多样化（每版本 5 种衍生镜像）、安全交付（随机下载）。原句："Three tiered approach offering - Independent verification and validation of source code - Software diversification to prevent exploitation - Secure delivery of software to customer" <<<PAGE 109-111>>>

## 二、AOS 系统与配置管理（Day 1）

- **P16 管理访问方式全集**：CLI（console/Telnet）、WebView、SNMP、SSH、FTP/SFTP、TFTP、USB 灾难恢复。原句："Management tools include: CLI… WebView… SNMP… Secure Shell (SSH)" <<<PAGE 124>>>
- **P17 Flash 双目录体系（R6）**：working 与 certified 各存一套 *.img 与 boot.cfg，认证版本作为升级回退备份。原句："2 versions are present on flash; working and certified / A certified version (SW + conf) will be used as a backup" <<<PAGE 126>>>
- **P18 启动流程**：BootROM 硬件初始化→MiniBoot→按 boot.params 选镜像→拷入 RAM 运行。原句："Bootstrap Basic Operation - Hardware Initialization - Memory Diagnostics - Miniboot Selection" <<<PAGE 128>>>
- **P19 目录不一致时的运行规则**：working 与 certified 不同则从 certified 启动；改运行配置需先切回 working。原句："If Working and Certified directories are different, then the switch runs from Certified" <<<PAGE 130-131>>>
- **P20 从 working 重启并回写认证的完整链路**：reload working no rollback-timeout → copy running-config working → copy working certified。原句："-> reload working no rollback-timeout / -> copy working certified" <<<PAGE 132-133>>>
- **P21 R8 用户自定义目录**：可建任意命名的配置目录，可直接保存配置。原句："These directories can have any name… Configuration changes CAN be saved directly to any user-defined directory" <<<PAGE 145>>>
- **P22 R8 运行目录概念**：running directory 是启动来源目录；running configuration 驻留 RAM。原句："Directory from which the switch booted from / It resides in the OmniSwitch RAM" <<<PAGE 146>>>
- **P23 配置回滚机制**：reload from working/user-defined no rollback-timeout 可指定无回滚计时重启。原句："->reload from working no rollback-timeout / ->reload from <userdefined> no rollback-timeout" <<<PAGE 147>>>
- **P24 modify running-directory 切换**：从 certified 启动时无法保存配置，需 modify running-directory working + write memory。原句："When the switch boots from the Certified directory, changes made to the switch cannot be saved" <<<PAGE 148>>>
- **P25 R8 Bash shell 管理**：命令别名存 boot.cfg、内建 Unix 管道过滤。原句："Bash shell is used for all user input / Unix piping mechanisms built into bash redirections" <<<PAGE 150>>>
- **P26 EMP 地址存 boot.cfg**：EMP IP 双 CMM 共享、CMM 自身 IP 存 NVRAM 随板卡走。原句："The EMP IP address is shared between both CMMs and stored in the boot.cfg file" <<<PAGE 153>>>
- **P27 Auto-fabric 七步零接触**：Auto-VC、远程配置、Auto-LACP、Auto-Routing、Auto-SPB、Auto-Network Profiling、Auto-MVRP。原句："AUTO-FABRIC PLUG-N-PLAY ZERO TOUCH DEPLOYMENT 1- Auto-VC … 7- Auto-MVRP" <<<PAGE 155>>>
- **P28 开箱自动配置（RCL）流程**：无 boot.cfg 时 DHCP 取址，DHCP 选项返回 TFTP 服务器与指令文件名，解析执行固件/配置/脚本。原句："DHCP Server will return the path and the filename of an instruction file containing Firmware, Configuration file, Script file" <<<PAGE 157-158>>>
- **P29 OXO 零接触**：OmniPCX Office 通过 DHCP Option 43 下发厂商类与配置文件自动部署 6250-P/6450-P。原句："OmniSwitch vendor class and switch type via DHCP Option 43 / Configuration file download from OXO using DHCP/TFTP" <<<PAGE 161>>>
- **P30 配置快照（snapshot）**：configuration snapshot 捕获配置文本，configuration apply 恢复。原句："Snapshot feature captures switch configurations in a text file / configuration apply filename" <<<PAGE 164>>>
- **P31 CLI 辅助特性**：前缀识别、? 帮助、TAB 补全、30 条历史、100 条命令日志、别名。原句："Command History (up to 30 commands) / Command Logging (up to 100 commands; detailed information)" <<<PAGE 165>>>
- **P32 默认账户体系**：admin 全权限仅 console（密码 switch），default 为新用户模板。原句："Admin - Full privileges - By default, access only allowed through console port / Default - Default privileges given to new user" <<<PAGE 176>>>
- **P33 两类账户**：网管员账户按功能域授权（read-only/read-write + families/domains）；终端用户账户挂 end-user profile 限定端口/VLAN。原句："Network administrator accounts… End-user or customer login accounts - Configured with end-user profiles" <<<PAGE 177>>>
- **P34 密码与锁定策略**：复杂度、历史（0-24）、长度（0-14）、最小/最大年龄、锁定阈值窗口时长。原句："History - Retain 0 to 24 passwords in history / Min Password Length - 0 to 14 char" <<<PAGE 180-181>>>
- **P35 ASA/AAA 认证链**：aaa authentication <service> 后可列最多 3 个备份服务器（含 local），按序轮询。原句："The switch uses the first available server in the list / Up to 3 backups may be specified (including local)" <<<PAGE 185>>>
- **P36 RADIUS 认证与计费分离**：radius-server 定义服务器，accounting session 上报用户行为；源 IP 默认 Loopback0。原句："Interface Loopback0 address if configured, used for the source IP field" <<<PAGE 186>>>
- **P37 NTP 三角色**：交换机可作 NTP 客户端/服务器/对等体，R6/R8 最多 3 个服务器。原句："OmniSwitch can act as an NTP Client, Server, or Peer / 3 max on R6/R8" <<<PAGE 189>>>

## 三、堆叠与虚拟机箱（Day 1）

- **P38 R6 堆叠基本属性**：同家族 2-8 台（6350 最多 4 台）、PoE/非 PoE 可混、单 IP 管理。原句："All of the models in the same family are stackable - Only 6350, or 6450 - 2 to 8 switches in a stack" <<<PAGE 251-252>>>
- **P39 堆叠四角色**：Primary/Secondary/Idle/Pass-Through；Slot-ID 冲突时后来者进 Pass-Through 不阻流量。原句："In case of Slot-ID duplication, the second stared switch gets 'Pass-through' role - It is not part of the stack, but does not block the traffic" <<<PAGE 255>>>
- **P40 Slot-ID 动态分配两法**：无 boot.slot.cfg 时按 15 秒窗口内 MAC 地址法或按启动时间法分配。原句："All switches are interconnected and boot up within a 15s timer (MAC @ method)" <<<PAGE 256>>>
- **P41 stack set slot 修正 Pass-Through**：改 saved-slot 后重启生效。原句："-> stack set slot <current_slot> saved-slot <new_slot>" <<<PAGE 258-259>>>
- **P42 takeover 主备切换**：可从主或备发起，主复位、备升主、最低 Slot 的 Idle 升备；切换前必须同步。原句："takeover - Can be launched from the Primary or Secondary switch / A synchronization has to be done before takeover" <<<PAGE 260>>>
- **P43 堆叠三级同步链**：write memory（RAM→working）→ copy working certified → copy flash-synchro（跨成员同步并自动认证）。原句："-> copy flash-synchro – automatic certification / -> write memory flash-synchro" <<<PAGE 264-268>>>
- **P44 MAC Retention**：堆叠在多次 takeover 后保持主交换机 MAC，避免 STP/LACP/IP 全面重启。原句："Allows a stack of switches to retain the MAC address of the Primary switch… even after multiple takeovers" <<<PAGE 271-272>>>
- **P45 Split Stack Protection（SSP）**：堆叠链双断时经上游 helper 交换机转发 SSP PDU，备份子堆叠关用户端口防双主。原句："If Back-up unit receives SSP PDU, it goes into Split Stack protection mode - Does not assume Primary role - Shuts down ports" <<<PAGE 275>>>
- **P46 虚拟机箱（VC）核心价值**：多台物理交换机经 VFL 互联成单一路由/网桥，单管理 IP，接入-核心间免 STP/VRRP。原句："Virtual Chassis = Group of Switches - Appears as a single router or bridge / No STP/VRRP between Access and Core" <<<PAGE 290>>>
- **P47 VC 组件术语**：VFL（虚拟网链）、Master/Slave、控制 VLAN、Chassis ID、Group ID、Chassis Priority。原句："Single or Aggregated group of ports that connects the switches of the Virtual Chassis" <<<PAGE 292-293>>>
- **P48 VC 模式文件要求**：vcsetup.cfg（机箱 ID/组/VFL）+ vcboot.cfg（通用 VC 配置）须在运行目录。原句："2 files are required for a chassis to operate in Virtual Chassis mode: vcsetup.cfg… vcboot.cfg" <<<PAGE 294>>>
- **P49 Master 选举五级 Criteria**：现任 Master > chassis priority > 最长在线 > 最小 Chassis ID > 最小 MAC。原句："1) Current Master Chassis 2) Higher chassis priority value 3) Longest chassis uptime 4) Smallest Chassis ID value 5) Smallest Chassis MAC address" <<<PAGE 296>>>
- **P50 VC 主备切换与 MAC 保持**：仅 Master 重载，Slave 不受影响；原 Master 回来不重选举；MAC retention 恒开。原句："When the 'original' master comes back, no re-election ('new' Master stays Master) / 'MAC retention' is always enabled" <<<PAGE 297>>>
- **P51 各机型 VC 规格**：6900 最多 6 台 mesh、5 VFL/机箱、16 端口/VFL；6860 最多 8 台 ring、专用 2x20G VFL 口。原句："Max 6 x 6900 per VC - Mesh topology - 5 VFL per chassis / Max. 8 x 6860s per Virtual Chassis - Ring topology" <<<PAGE 299-300>>>
- **P52 6860/6865 混合 VC**：混合上限仍 8 台 ring；6865 10G 口可作 auto-VFL。原句："OS6860/OS6865 mixed VC is supported up to VC of 8 units in ring topology" <<<PAGE 301>>>
- **P53 VC 脑裂检测两法**：RCD（经 EMP 口周期通告，EMP 为必备）与 VCSP（经 helper 的链路聚合发 VCSP PDU，不依赖 EMP）。原句："Remote Chassis Detection (RCD) - Each chassis sends periodic updates via the EMP port / Virtual Chassis Split Detection (VCSP) - EMP Ports not mandatory" <<<PAGE 306-307>>>

## 四、诊断工具（Day 1）

- **P54 swlog 三输出**：console、flash（R6 两文件/R8 最多 8 文件）、syslog socket（R6 4 台/R8 12 台远端）。原句："Switch events can be logged to Switch console -> swlog output console / Local text file -> swlog output flash" <<<PAGE 326-327>>>
- **P55 日志按 appid/子模块调级**：如 swlog appid ospf_0 subapp hello level debug3；默认级别 info(6)。原句："Default severity level is info. The numeric equivalent for info is 6" <<<PAGE 329-331>>>
- **P56 command-log**：与 history 不同，记录命令+结果+用户+IP，存 /flash/command.log，须显式启用。原句："Logs commands and output - Different than command history - Creates command.log file in /flash directory" <<<PAGE 334>>>
- **P57 端口镜像规格**：每机/每堆叠 2 会话、N 对 1 最高 128:1、端口容量须一致。原句："2 per standalone switch and per stack / N-to-1 Mirroring Supported 128 to 1 all models / Port requirements - must be of identical capacity" <<<PAGE 337>>>
- **P58 远程端口镜像（RPM）**：专用 RPM VLAN 承载镜像流量至远端交换机；LACP/LLDP/802.1x/OAM/L3 控制包不被镜像。原句："Achieved by using a dedicated remote port mirroring VLAN / The following types of traffic will not be mirrored" <<<PAGE 338>>>
- **P59 基于策略的镜像**：policy action mirror 按流镜像，可镜像并丢弃原流量。原句："Mirroring is done based on a QoS policy instead of a specific port" <<<PAGE 339-340>>>
- **P60 端口监控（Port Monitoring）**：本机抓包存 Sniffer ENC 格式，截前 64 字节，每机 1 会话。原句："Captures first 64-bytes of frame / Session supported per switch or stack: 1" <<<PAGE 342>>>
- **P61 RMON 四组**：Ethernet Statistics、History、Alarms、Events。原句："4 groups supported: Ethernet Statistics… History Group… Alarms Group… Events Group" <<<PAGE 344>>>
- **P62 show health 资源监控**：CPU/内存收发利用率 1 分/1 时均值与阈值告警。原句："Monitors switch resource utilization and thresholds" <<<PAGE 346>>>
- **P63 sFlow 采样体系**：交换机内嵌 agent + 远端 collector，RFC 3176，用于流量计量/异常检测/容量规划。原句："Traffic flows monitoring and sampling technology embedded within switches / sFlow Agent software process running as part of the switch software" <<<PAGE 348-349>>>

## 五、VLAN 与二层（Day 2）

- **P64 VLAN 本质**：广播域划分，端口经静态/移动认证/802.1q/移动标签入 VLAN。原句："VLAN - Virtual LAN - A broadcast domain / Ports become members of VLANs by Static Configuration, Mobility/Authentication, 802.1q, VLAN Mobile Tag" <<<PAGE 360>>>
- **P65 静态 VLAN 指派**：端口默认 VLAN；出厂全部端口属 VLAN 1。原句："VLAN is assigned to the data port (aka the default VLAN of the port). By default, all ports belong to VLAN 1." <<<PAGE 363>>>
- **P66 动态 VLAN 依规则匹配**：mobile/UNP 口按 VLAN 规则（MAC/网络地址/协议/DHCP）匹配入 VLAN，优先级 MAC>MAC Range>Network>Protocol>Default。原句："1. MAC Address 2. MAC Range 3. Network Address 4. Protocol 5. Default (No Match -> port default VLAN)" <<<PAGE 367-368>>>
- **P67 802.1x 认证 VLAN**：用户经 RADIUS/LDAP/TACACS+ 认证后 MAC 关联目标 VLAN/UNP。原句："Successful login - The client MAC is associated with the correct VLAN or UNP" <<<PAGE 371>>>
- **P68 VLAN 间路由触发**：VLAN 挂 IP 接口即激活路由；VLAN 无活跃端口则操作状态 down。原句："IP routing is active as soon as at least one IP interface is associated with a VLAN" <<<PAGE 373>>>
- **P69 802.1Q 标签结构**：4 字节 tag 含 12bit VLAN ID（4096 个）+3bit 802.1p 优先级。原句："4096 unique VLAN Tags / 802.1P - Three bit field within 802.1Q header - Allows up to 8 different priorities" <<<PAGE 379>>>
- **P70 Mobile Tag 机制**：允许 mobile 口同时收多 VLAN 打标签流量，按 tag 分类，优先于一切 VLAN 规则。原句："Takes precedence over all VLAN Rules / Allows mobile ports to receive 802.1Q tagged packets" <<<PAGE 382>>>
- **P71 VLAN 1 不可删**：默认 VLAN 所有端口初始归属，只能禁用不能删除。原句："This VLAN CANNOT be deleted, but it can be disabled if so desired." <<<PAGE 385>>>

## 六、链路聚合（Day 2）

- **P72 聚合收益与形态**：多物理口合为单逻辑链路，静态 OmniChannel 或动态 802.3ad LACP。原句："Method of aggregating (combining) more than 2 ports/links so that the switch will 'see' them as one logical link" <<<PAGE 394>>>
- **P73 聚合规模规格**：组大小 2/4/8/16；一端口只能属一个聚合组。原句："Number of links per group supported: 2, 4, 8 or16 / One port can only belong to one link aggregation" <<<PAGE 395>>>
- **P74 静态 vs 动态**：静态仅限 OmniSwitch 间、两端参数必须一致；LACP 用 LACPDU 协商、可跨厂商。原句："Static - Port parameters MUST be exactly the same at both ends… Only works between Alcatel-Lucent OmniSwitches / Dynamic - IEEE 802.3ad LACP" <<<PAGE 396>>>
- **P75 actor admin key 两端一致**：动态聚合按 admin key 关联端口，key 值仅本地意义但两端需匹配。原句："Actor admin key must be configured to the same value on both ends of the link aggregation group" <<<PAGE 398-404>>>
- **P76 哈希算法两档**：brief 仅 IP 对、extended 加 UDP/TCP 端口更均匀。原句："Brief Mode: UDP/TCP ports not included / Extended - UDP/TCP ports to be included in the hashing algorithm" <<<PAGE 401>>>
- **P77 组播默认走主端口**：可开 non-ucast 哈希把组播分担到全部成员。原句："Multicast traffic is by default forwarded through the primary port of the Link Aggregation Group" <<<PAGE 402>>>

## 七、STP/RSTP/MSTP（Day 2）

- **P78 STP 目的与默认**：防环+自动重构；OmniSwitch 默认开启 STP。原句："Prevent network loops / Automatic reconfiguration in case of a topology change / STP runs by default on the OmniSwitches" <<<PAGE 414>>>
- **P79 根桥选举四判据**：最低 Root Bridge ID > 最低路径开销 > 最低发送者 Bridge ID > 最低端口 ID。原句："Root bridge decisions based on: Lowest Root Bridge ID - Lowest Root Path Cost - Lowest Sender Bridge ID - Lowest Sender Port ID" <<<PAGE 420-425>>>
- **P80 STP 五状态 vs RSTP 三状态**：802.1D 阻塞/侦听/学习/转发/禁用合并为 802.1w discarding，亚秒收敛。原句："IEEE 802.1D states disabled, blocking, and listening have been merged into a unique 802.1w discarding state" <<<PAGE 420-422>>>
- **P81 RSTP 端口角色**：Root/Designated/Alternate/Backup/Disabled。原句："Alternate Port - Offers an alternate path to the root bridge… Backup Port - Provides a backup connection for the designated port" <<<PAGE 423>>>
- **P82 两种运行模式**：flat（每机一棵树）与 1x1/per-VLAN（每 VLAN 一棵树，默认）。原句："Flat Mode - One STP instance for the entire switch / 1x1 mode - Single STP instance enabled for each VLAN" <<<PAGE 427-429>>>
- **P83 1x1 实例上限**：R6=252、R7=128、R8=100。原句："Maximum VLAN (or Spanning Tree) instances per switch: R6 = 252 R7 = 128 R8 = 100" <<<PAGE 429>>>
- **P84 路径开销 16/32bit**：STP/RSTP 用 16bit（1G=4），MSTP 用 32bit（1G=20000），默认 auto。原句："16-bit when STP/RSTP protocol is active / 32-bit when MSTP protocol is active" <<<PAGE 432>>>
- **P85 PVST+ 互操作**：检测到 PVST+ BPDU 端口自动转 PVST+ 口；需 1x1 模式。原句："Any user port can detect a PVST+ BPDU and become PVST+ port automatically" <<<PAGE 433-434>>>
- **P86 MSTP 实例模型**：CIST(实例 0，默认含全部 VLAN)+最多 16 个 MSTI；一帧 BPDU 携带全部实例。原句："Instance 0 - Always configured on any 802.1s switch… By default, all VLANs are mapped to the CIST / Up to 16 other instances are supported" <<<PAGE 438>>>
- **P87 MST 域三要素**：域名、修订级别、VLAN-实例映射表（BPDU 只传摘要 digest）。原句："Attributes: Region Name - Region Revision Level - VLAN-Instance Mapping table / Only a digest of the VLANs−to−instance mapping table is sent" <<<PAGE 443>>>
- **P88 MST 域边界与跳数**：收到异域/802.1D BPDU 的口成 Region Boundary Port；最大跳数 40 默认 20。原句："The maximum hop count supported is 40, default is 20" <<<PAGE 439-443>>>
- **P89 MSTP 配置最小集**：flat 模式+协议 mstp+region name/revision+msti vlan 映射。原句："-> bridge mode flat / -> bridge protocol mstp / -> bridge mst region name {mst_region_name}" <<<PAGE 444>>>

## 八、DHL 双归属（Day 2）

- **P90 DHL Active-Active 原理**：VLAN 集在两条活跃上行链路间分配，靠 VLAN-链路映射防环，故障时剩余链路接管全部 VLAN。原句："DHL Active-Active splits a number of VLANs between two active links / The forwarding status of each VLAN is modified by DHL to prevent network loops" <<<PAGE 477-478>>>
- **P91 DHL 会话结构**：每机仅一个会话、两条链路（物理口或 linkagg）、公共 VLAN 池、VLAN-链路映射。原句："A DHL session. Only one session per switch is allowed" <<<PAGE 478>>>
- **P92 Pre-emption 定时器与 MAC 冲刷**：0-600 秒；因 DHL 口禁用 STP，需 None/MVRP Enhanced/RAW Flooding 三法清陈旧 MAC。原句："Spanning Tree is automatically disabled on DHL ports / 3 available mechanisms to avoid stale MAC address entries" <<<PAGE 479>>>
- **P93 DHL 与其他冗余方案对比**：STP 50% 带宽、LACP 仅链路冗余、VC 全冗余统一管理、DHL 链路+交换机冗余 100% 带宽。原句："Link redundancy 100% Bandwidth… Switch redundancy" <<<PAGE 481>>>

## 九、高级 IP 接口 / DHCP / LLDP（Day 2）

- **P94 Loopback0 常驻管理口**：不绑 VLAN 恒 up，RIP/OSPF 自动通告（BGP 不），用作 RP、sFlow agent、RADIUS 源 IP、OSPF router-id 等。原句："IP interface with a consistent address for network management purposes - Not bound to any VLAN - Always remains operationally active" <<<PAGE 492>>>
- **P95 可选主管理接口**：ip managed-interface 按应用指定源接口。原句："Applications will be able to choose the source interface IP" <<<PAGE 493>>>
- **P96 DHCP Relay**：ip helper address 指向 DHCP 服务器；ip udp relay 转发 DNS 等指定 UDP 端口。原句："-> ip helper address {Server Addr} / -> ip udp relay DNS" <<<PAGE 498-499>>>
- **P97 LLDP（802.1AB）**：二邻发现协议，默认全交换机使能收发；PDU 为 TLV 结构。原句："L2 discovery protocol - Exchange information with neighboring devices… Enabled by default on the OmniSwitches" <<<PAGE 509-510>>>
- **P98 LLDP-MED 语音扩展**：网络策略（VLAN+802.1p+DSCP）、位置、PoE 管理、库存 TLV；IP 话机经 network-policy 自动入语音 VLAN。原句："Provides VoIP-specific extensions to base LLDP protocol / LAN policy discovery (VLAN, Layer 2 priority, Layer 3 QoS)" <<<PAGE 514-517>>>

## 十、VRRP（Day 3）

- **P99 VRRP 规格要点**：RFC 2338、组播 224.0.0.18、协议号 112、TTL 255、虚拟 MAC 00-00-5E-00-01-{VRID}、最多 255 虚拟路由器。原句："Virtual MAC address: 00-00-5E-00-01-{VRID}" <<<PAGE 524>>>
- **P100 Master/Backup 机制**：最高优先级（默认 100、IP 拥有者直接 Master）为 Master 负责转发与 ARP 应答。原句："It is the router with the highest priority (default = 100; max= 255) / A router becomes the Master if it is the owner of the Virtual router IP address" <<<PAGE 526>>>
- **P101 Master_Down_Interval 与 Skew_Time**：3×通告间隔+偏移；偏移=(256-Priority)/256 防止多 Backup 同时升主。原句："Calculated as: ( 3 * Advertisement_Interval ) + Skew_time" <<<PAGE 527>>>
- **P102 VRRP 负载分担**：两虚拟路由器互为主备，主机按不同默认网关分摊。原句："VRRP can assist in load balancing outgoing traffic" <<<PAGE 528>>>
- **P103 VRRP Tracking**：基于 ADDRESS/IPV4-INTERFACE/PORT/VLAN 策略降优先级触发切换。原句："the VRRP router will adjust to become Master or Slave depending on the associated action" <<<PAGE 531>>>
- **P104 VRRP Group 集体管理**：组内统一改优先级/通告间隔/抢占。原句："Changes the advertising interval value of all the virtual routers on the group" <<<PAGE 533>>>

## 十一、QoS（Day 3）

- **P105 QoS 定义与作用面**：管带宽、可按时段调度；影响接受/丢弃、队列优先、下一跳、整形、802.1p/ToS/DSCP 标记、镜像、超速染色。原句："QoS policies can affect such things as Accept/Drop behavior of a packet - Queuing priority - Next hop for routing - Bandwidth shaping" <<<PAGE 542-543>>>
- **P106 分类引擎位置**：解析器后硬件分类，L2(MAC/VLAN/端口)/L3/L4(SIP/DIP/端口/协议) 条件。原句："CLASSIFICATION ENGINE… L2 (source & dest) - MAC, VLAN… L3/L4 - SIP, DIP, TCP,UDP,IP proto" <<<PAGE 544>>>
- **P107 策略三元组与容量**：Condition+Action+Rule（可选生效时段）；条件/动作各 2048，规则 512(6350/6450)~8192(6900/10K)。原句："Rules (<condition> + <action> + <time valid, optional>) / Conditions = 2048 Actions = 2048" <<<PAGE 545>>>
- **P108 R6 调度三算法**：Strict Priority、WRR（1-15 包，0=严格）、DRR（0-15，按体量 1=10KB）。原句："Weighted Round Robin - User can specify the number of packets to be dequeued (from 1 to 15)" <<<PAGE 547>>>
- **P109 R8 QSet/QSI 模型**：每口 8 单播队列+4 组播队列；QSet Profile 定义 SP/WFQ/EF 组合（Profile1=8SP，Profile2=1EF+7SP，Profile3=1EF+7WFQ）。原句："A QSet is a set of 8 egress Queues that are associated with each port or link Aggregate / 4 Multicast Queues per port - No user configuration" <<<PAGE 548-552>>>
- **P110 策略组复用**：network group/mac group/service group/port group 供条件复用。原句："policy network group netgroup3 173.21.4.0 mask 255.255.255.0 10.10.5.3" <<<PAGE 569>>>
- **P111 Egress 策略列表**：R8 出方向过滤仅支持 policy list type egress。原句："Egress Filtering is only supported on" <<<PAGE 575>>>
- **P112 信任与默认标记**：端口默认 802.1p/DSCP=0；交换口默认不信任，可用 qos phones trusted/qos nms priority 设信任源。原句："By default, the port defaults for 802.1p and ToS/DSCP are 0 / By default, switched ports are not trusted." <<<PAGE 581-590>>>
- **P113 SIP Snooping**：硬件侦听 SIP 信令动态学习 IP 话机 RTP 流并自动加 QoS；默认转发的 SIP 包不受策略。原句："By default, the SIP packets forwarded by hardware are not subject to any" <<<PAGE 601>>>
- **P114 策略删除约束**：被规则引用的 condition/action 不可删。原句："A condition… cannot be deleted if it is currently being used by a policy rule" <<<PAGE 593-594>>>

## 十二、ACL（Day 3）

- **P115 ACL 在策略体系中的位置**：ACL 即策略的过滤子集，与 QoS 共用 condition/action/rule。原句："ACLs are basically a type of QoS policy, and the commands used to configure ACLs are a subset of the switch's QoS commands" <<<PAGE 607-618>>>
- **P116 ACL 作用域**：整机全局、仅入方向、L1-L4 硬件过滤；规则 precedence 0-65535 大者先。原句："Each policy is global to the switch and has a precedence (0..65535) – higher comes first / At ingress only" <<<PAGE 607>>>
- **P117 默认 disposition 全 accept**：bridged/routed/multicast 全局默认与规则默认均为 accept。原句："Global bridged disposition… accept / Global routed disposition… accept" <<<PAGE 610-618>>>
- **P118 established 条件**：检查 ACK/RST 位放行已建 TCP 连接的回程。原句："TCP header information is examined to determine if the ACK or RST flag bit is set" <<<PAGE 615>>>
- **P119 白名单式 L3 ACL 范式**：全局 deny + 精确 accept 规则实现内部防火墙。原句："Globally denies routed traffic on the switch / Allows communication to and from Host1 to subnet 192.168.100.0/0" <<<PAGE 614>>>

## 十三、Access Guardian / UNP / IoT（Day 3）

- **P120 AG 端口自动感知**：同口混布 802.1X 与非 802.1X 设备；R6 需 mobile+802.1x 口、R8 需 UNP bridge 口。原句："Auto-sensing, multi-client authentication on a port - Automatic detection of 802.1X and non-802.1X devices" <<<PAGE 630>>>
- **P121 UNP 角色化访问控制**：VLAN+策略列表(QoS/ACL)+（R8 加 location/period）；用户档案随人走。原句："User Security Profiles follows the user / Security Profiles dynamically applied to switch port" <<<PAGE 631>>>
- **P122 RADIUS Filter-ID 下发 UNP**：Access-Accept 携 UNP 名；无返回时可降级分类规则/默认 UNP/Captive Portal/阻断。原句："Filter-ID = \"UNP-name\" / New connection RADIUS Access-Accept + UNP name" <<<PAGE 632>>>
- **P123 非 supplicant MAC 认证流程**：交换机以源 MAC 为用户名/密码构造 RADIUS 请求。原句："Switch builds auth. Request using source MAC as login/password" <<<PAGE 633>>>
- **P124 R8 分类规则 16 级优先序**：Port>Port+VLAN tag>Domain 组合>MAC>OUI>Range>LLDP>Auth-type>IP>VLAN tag。原句："UNP Port classification rules 1. Port 2. Port + VLAN tag 3. Domain + VLAN tag…" <<<PAGE 638>>>
- **P125 UNP 配置五步**：分类规则→认证服务器→设备分类策略→UNP 档案→端口。原句："Configure UNP Classification Rules / Configure Authentication Server / Configure Device classification policies… Configure UNP profiles / Configure ports" <<<PAGE 640>>>
- **P126 Location/Period 策略（R8）**：按接入位置与时间窗限制角色，不满足自动转未授权角色。原句："the location policy is used to restrict the network access based on the location of the user/device" <<<PAGE 649-650>>>
- **P127 IoT 设备画像三组件**：本地签名收集器+本地 profiler+UNP 画像；用 DHCP 指纹（Option 55/60）与 MAC OUI 识别。原句："IoT device profiling uses DHCP FingerPrinting and MAC OUI to identify IoT devices" <<<PAGE 686-688>>>
- **P128 画像结果联动 UNP**：识别分类后自动指派 UNP；维护已知/未知设备库供管理员补录。原句："When a device gets identified and categorized, the UNP profile can be automatically assigned to the device" <<<PAGE 690>>>

## 十四、PoE（Day 3）

- **P129 动态 PoE 供给**：按需供电至预算上限，优于 IEEE 可选分类。原句："OmniSwitch uses dynamic PoE - Delivers what's needed, up to total budget" <<<PAGE 694>>>
- **P130 PD 分级体系**：802.3af Class 0-3（15.4W 顶）、802.3at Class 4（PSE 34.2W/PD 25.5W）；分级靠 PD 固定电阻。原句："The class of a PD is determined by the PSE via a fixed resistance in the PD" <<<PAGE 695>>>
- **P131 端口优先级三级**：low/high/critical，电力不足按序断电保 critical。原句："Critical: In the event of a power management issue, inline power to critical ports is maintained as long as possible" <<<PAGE 701>>>
- **P132 Capacitor detection 仅老话机**：非 802.3af 兼容，只用于旧 IP 话机。原句："not compatible with IEEE specification 802.3af / It should only be enabled to support legacy IP phones" <<<PAGE 702>>>
- **P133 Priority disconnect**：预算不足时决定新 PD 授电与否。原句："used by the system software in determining whether an incoming PD will be granted or denied power" <<<PAGE 702>>>
- **P134 R8 PoE 命令体系**：lanpower slot/port 两级，service start、admin-state、power 毫瓦、priority。原句："-> lanpower slot 1/1 service start / -> lanpower port 1/1/24 power 18000" <<<PAGE 705>>>

## 十五、路由 RIP/OSPF/GR（Day 4）

- **P135 静态路由优先**：默认静态优于动态；metric 区分主备默认路由。原句："Static routes always have priority over dynamic routes" <<<PAGE 714-716>>>
- **P136 递归静态路由**：follows 指定宿主，网关随动态路由变化；6.7.1 无此选项。原句："Nexthop (or gateway) address no longer must be tied to a particular INTERFACE / Option not available in AOS 6.7.1" <<<PAGE 719-720>>>
- **P137 出接口静态路由**：interface 形式在下一跳常变时手工指定出口。原句："Configure the router to use the exit INTERFACE to handover the packet to neighbor device" <<<PAGE 721>>>
- **P138 RIP 基础参数**：距离向量、跳数 16 不可达、30 秒全表更新、UDP 520、报文 512B/20 路由。原句："Hop count limit of 16 is considered unreachable / Generates updates every 30 seconds / Uses UDP port 520" <<<PAGE 724>>>
- **P139 RIP v1/v2 差异**：v1 有类广播无认证；v2 带掩码/下一跳、组播 224.0.0.9、支持认证。原句："RIP II… Carries additional subnet mask information - Updates sent as Multicasts (224.0.0.9) - Supports authentication" <<<PAGE 724>>>
- **P140 RIP 四定时器**：update 30/invalid 180/garbage 120/holddown 0，且 invalid≥3×update 由 AOS 强制。原句："AOS to enforce the constraint that invalid cannot be less than 3x of update" <<<PAGE 730-731>>>
- **P141 RIP 默认只通告学习路由**：本地/静态路由需 route-map+redist 重分发。原句："Only learned RIP routes and Loopback0 interface are advertised by default. Local routes must be redistributed." <<<PAGE 726>>>
- **P142 OSPF 三数据库**：邻接表、LSDB、OSPF 路由表，SPF 并行计算。原句："Uses three databases: Adjacency Table. List of neighbors / Link State Database. List of routes / OSPF Routing Table. Best routes" <<<PAGE 753>>>
- **P143 Router ID 选择**：默认启动时主地址→首个 up 接口，可 Loopback0 或手工 router-id 覆盖。原句："Can be overridden by the interface 'Loopback0'" <<<PAGE 754>>>
- **P144 OSPF 区域类型**：Stub（无 Type5）、Totally Stubby（仅默认路由）、NSSA（本区可注入外部 Type7）、Transit。原句："Stub areas - Do not carry external routes / Totally stubby areas… only receive the default route from the backbone / Not-so-stubby areas - Allow external routes to be advertised from the area" <<<PAGE 760>>>
- **P145 LSA 类型谱**：1 路由器/2 网络(DR)/3-4 汇总(ABR)/5 外部(ASBR)/7 NSSA 外部/9-11 Opaque（Type9 用于 GR）。原句："AOS software uses Type 9 for graceful restart capability" <<<PAGE 761-762>>>
- **P146 虚链路**：不接骨干的区域经 transit area 建 virtual-link。原句："If an area cannot be physically connected to the backbone, then a virtual-link can be created" <<<PAGE 763>>>
- **P147 AOS 路由偏好默认值**：Local 1/Static 2/OSPF 10/RIP 100/BGP 200，可改。原句："Protocol Route Preference Value… Local 1 Static 2 OSPF 10 RIP 100 BGP 200" <<<PAGE 769>>>
- **P148 GR 原理**：重启路由器保持转发，helper 维持邻接不重算 SPF；Grace LSA 携宽限期。原句："Router remains on forwarding path when restarting / Neighbors must participate in graceful restart" <<<PAGE 772-774>>>
- **P149 GR 三态流程**：发 Grace LSA→同步 LSDB 期间不发 LSA→同步后发更新 LSA 并老化清除 Grace LSA。原句："It does not send any LSA/LSP because it still has incomplete routing information" <<<PAGE 775>>>

## 十六、AOS 网络安全（Day 4）

- **P150 LLDP Rogue Detection**：每口仅一个可信 LLDP agent，超时/重复/多 agent 即违规（trap/shutdown）。原句："Only one trusted LLDP agent on a port / Port will be moved to violation state" <<<PAGE 801-802>>>
- **P151 LPS 目标与支持面**：限制端口学 MAC 数/时窗；支持固定/mobile/tag/认证口，不支持聚合口。原句："Limit the max number of L2 addresses that can be learned on a port… Not supported on Link Aggregate ports" <<<PAGE 804>>>
- **P152 LPS 违规两动作**：restrict 仅滤违规流量、shutdown 全口阻断；默认学 1 MAC、滤 5、违规 restrict。原句："Shutdown. Stops all traffic on a port after violation / Filtering. Only stops traffic from violating device" <<<PAGE 805-806>>>
- **P153 mac-range 白名单与转静态**：每口最多 8 段 MAC 范围；convert-to-static 固化动态 MAC。原句："up to eight MAC ranges per port / Converting the dynamically learned MAC addresses… to static MAC addresses" <<<PAGE 807>>>
- **P154 PBR 硬件重定向**：policy action permanent gateway 覆盖路由表，可本地/远程下一跳。原句："QoS policies that will override the normal routing mechanism for traffic matching the policy condition / Done in hardware" <<<PAGE 811-812>>>
- **P155 PBR 防环路技巧**：回程流量加 source port 条件避免防火墙来回打环。原句："Adding the source port to the condition allows traffic to not get caught in a loop" <<<PAGE 814>>>
- **P156 UserPorts 保留组**：默认防 IP 欺骗（源 IP 与端口网段不符即丢），可扩展过滤 rip/ospf/bgp/bpdu 等。原句："Used by default to prevent spoofed IP addresses on ports / -> qos user-port {filter | shutdown} {spoof|bgp|bpdu|rip|ospf|…}" <<<PAGE 816>>>
- **P157 DropServices 与 port-disable**：服务组批量丢弃（如 tcp135/445）；动作 port-disable 命中即管理性关闭端口，配恢复定时器。原句："Used in conjunction with UserPorts to drop TCP/UDP packets / policy action a1 port-disable" <<<PAGE 817-818>>>
- **P158 DOS 过滤能力**：Ping of Death/SYN/Land/Teardrop 等；ICMP 速率 5 秒窗 >100pps 判攻击。原句："System measures the rate of ICMP requests received over a period of 5 seconds, and detects a DoS attack if the measured rate exceeds 100 pkts/sec" <<<PAGE 821>>>
- **P159 ARP 防御与毒化检测**：未决 ARP 丢弃表防 CPU 过载；仅接受自己请求过的 Reply；受限地址每接口最多 2 个。原句："Creates a drop-entry as soon as it attempts to resolve an ARP / ARP Reply will be accepted only if the Switch had originated a corresponding ARP Request" <<<PAGE 822-824>>>
- **P160 MACsec（802.1AE）**：链路层点对点加密认证，防 DoS/中间人/窃听；Static SA（交换机间）与 Dynamic SA（PSK/EAP）模式。原句："IEEE 802.1AE standard that provides encryption and packet Authentication to IEEE 802.1 frames / MACSec-enabled links are secured by matching security keys" <<<PAGE 826-827>>>
- **P161 DHCP Snooping 双层**：信任口全放行、非信任口只收 Discover/Request；维护绑定库（MAC/IP/租期/VLAN）。原句："Filters DHCP packets between untrusted sources and a trusted DHCP server / Builds and maintains a binding table (database)" <<<PAGE 829-830>>>
- **P162 Option 82**：中继在客户端报文插入 Circuit ID（VLAN+端口）与 Remote ID（路由口 MAC）。原句："Enables the relay agent to insert identifying information into client-originated DHCP packets / Circuit ID: VLAN ID and slot/port… Remote ID: MAC address of the router interface" <<<PAGE 832>>>
- **P163 Port Mapping**：用户口-网络口单向/双向映射隔离终端；可配动态代理 ARP 打通三层数据面。原句："port mapping <id> user-port <slot/port> network-port <slot/port> / port mapping 1 dynamic-proxy-arp enable" <<<PAGE 837-839>>>
- **P164 Storm Control**：广播/组播/未知单播按 %、mbps、pps 三种阈值限洪泛。原句："Configuration of different thresholds for each type of storm/flood traffic / rate % num: rate in % of the port speed" <<<PAGE 886>>>

## 十七、VRF（Day 4）

- **P165 VRF 多实例**：同一物理交换机多个路由实例、可重复 IP；默认 VRF 开机即有。原句："Multiple routing instances within the same physical switch / Ability to use duplicate IP addresses across VRF instances" <<<PAGE 855-859>>>
- **P166 VRF 规模与感知面**：8(6855-U24X)~64（高端）；静态/RIP/OSPF/BGP/PIM/VRRP/QoS/AAA 等均 VRF-aware。原句："64 VRF on OS9000E, 6860(E), 6865, 6900, 9900 and 10K" <<<PAGE 855-856>>>
- **P167 VRF-VLAN 绑定约束**：一接口+其 VLAN 同时只能属一个 VRF；VRF 可挂多 VLAN。原句："A single IP interface, as well as the VLAN associated with the interface, can only belong to one VRF instance at a time" <<<PAGE 861>>>
- **P168 VRF Route Leak**：经 route-map 在 VRF 与 GRT 间导入导出，import 路由偏好可调。原句："VRF Route Leak forwards routes from one VRF routing table to another VRF routing table / -> ip export route-map R1 / -> ip import vrf V1 route-map R2" <<<PAGE 863-864>>>

## 十八、组播（Day 5）

- **P169 组播地址映射**：D 类 224.0.0.0-239.255.255.255，MAC 取 01:00:5e+IP 低 23 位。原句："Least significant 23 bits of IP address are mapped onto the 3 last octets of the MAC address / 224.1.2.3 -> 01:00:5e:01:02:03" <<<PAGE 867>>>
- **P170 IGMP 本地域协议**：TTL=1 永不被路由器转发；查询发 224.0.0.1、离开发 224.0.0.2。原句："IGMP is a protocol confined to the local segment of the LAN and is never forwarded by any router. Always has a Time-To-Live (TTL) of 1" <<<PAGE 871>>>
- **P171 IGMP v1/v2/v3 消息差异**：v2 加 Leave/特定组查询，v3 加源过滤（SSM）。原句："IGMP Source-Specific Join (v3 only) / V3 Membership report (Explicit Host Tracking)" <<<PAGE 872>>>
- **P172 IPMS 硬件交换**：snooping IGMP 按端口建转发表，仅发请求端口；默认禁用。原句："the switch forwards multicast traffic only to the ports that requested it / IPMS is disabled by default" <<<PAGE 875-878>>>
- **P173 Querier forwarding**：流源接在非查询者交换机时启用，全部组播送往查询者。原句："Querier-forwarding feature should be enabled if a streaming device is connected to a switch, which is not a querier" <<<PAGE 879>>>
- **P174 IGMP Throttling**：全局/VLAN/端口三级 max-group，动 none/drop/replace，端口级覆盖。原句："Per port limit overrides VLAN and global configuration" <<<PAGE 885>>>
- **P175 IGMP Relay（helper）**：把 IGMP 报告封装 IP 发往指定主机，不依赖 PIM 传播。原句："Encapsulates IGMP packets in an IP packet to a special device/server" <<<PAGE 884>>>
- **P176 PIM-SM 最小配置**：ip load pim→接口→cbsr→candidate-rp→sparse enable。原句："-> ip pim cbsr <interface_address> / -> ip pim candidate-rp rp_address group-address/prefix_length" <<<PAGE 908>>>
- **P177 PIM SPT 与 RP 阈值**：SPT 默认启用；rp-threshold 决定何时切换源树。原句："-> ip pim spt status enable / -> ip pim rp-threshold value" <<<PAGE 909>>>

## 十九、ERP 与 Intelligent Fabric（Day 5 / 扩展）

- **P178 ERP 机制**：G.8032 环网保护，APS 协议协调防环；RPL owner 负责阻塞/解阻塞。原句："This implementation of ERP uses the Automatic Protection Switching (APS) protocol to coordinate the prevention of network loops within a bridged Ethernet ring" <<<PAGE 926-929>>>
- **P179 ERP 环要素与状态**：ring ID+两口+Service VLAN+MEG level 为必配；RPL 节点只能配在已禁用的环上；状态 Pending（RPL 阻塞、拓扑稳定）/Protected（故障转发）。原句："The RPL node can be configured only on a preexisting disabled ring / Pending: the RPL port is blocking… Protected: on link failure" <<<PAGE 929-930>>>
- **P180 环规模建议**：每环建议最多 16 节点，环数依机型。原句："A maximum number of 16 nodes per ring is recommended." <<<PAGE 929>>>
- **P181 Auto-VC**：无 vcsetup.cfg 时自动 VFL 端口检测、自动 Chassis ID、最低 MAC 为 Master。原句："Auto Chassis ID selection only occurs when there is no vcsetup.cfg / Master selection is then run based on lowest MAC address" <<<PAGE 940>>>
- **P182 RCL 远程配置加载**：Auto-VC 后运行，VLAN 1 和 127 各试 3 次 DHCP 取指令文件；auto-config-abort 取消。原句："RCL tries 6 times, 3 each on VLAN 1 and 127 to get DHCP and download instruction file" <<<PAGE 941>>>
- **P183 Auto-LACP**：LLDP 私有 TLV 发现对端并协商成聚合（默认聚合 127、admin-key 65535）。原句："Propriatery TLV used to detect the peer and, in return, receive peer's system ID / If LACP negotiation succeeds, form a link aggregation" <<<PAGE 943>>>
- **P184 Auto-Routing**：侦听 OSPF/IS-IS Hello 学区域/类型/定时器并自动加载协议建邻接。原句："Protocol network configuration is learned through Hello packets - Determine area, area type, and timers" <<<PAGE 944>>>
- **P185 Auto-fabric CLI 管理**：discovery start、admin-state enable、config-save admin-state enable。原句："-> auto-fabric discovery start / -> auto-fabric admin-state enable" <<<PAGE 951>>>
- **P186 SPB 织构理念**：以 SPB 替代 STP 简化业务开通、提高链路利用率（6865/6900 IFAB）。原句："SPB - Simplified service provisioning, better link utilization compared to STP" <<<PAGE 73>>>

## 二十、代码升级 / MVRP / SLB / 静态聚合（扩展）

- **P187 升级流程铁律**：传镜像入 working→reload from working no rollback-timeout→验证→copy working certified。原句："Reboot the switch forcing it to load from the now upgraded WORKING directory… -> copy working certified" <<<PAGE 965>>>
- **P188 FTP 传输模式**：镜像必须 binary、配置文件必须 ASCII。原句："If you are transferring a switch image file, you must specify the binary transfer mode on your FTP client." <<<PAGE 965>>>
- **P189 USB 灾难恢复**：U 盘建 6900/certified 与 6900/working 目录放备份，根目录放 Trescue.img，miniboot 下 run rescue。原句："Enter the 'run rescue' command from miniboot/uboot and follow the recovery prompts" <<<PAGE 139>>>
- **P190 USB auto-copy**：根目录 aossignature 文件+xxxx/working 目录，自动校验拷贝并从 working 重启，完成后自动禁用防重复升级。原句："Once the switch reboots the auto-copy feature is automatically disabled to prevent another upgrade" <<<PAGE 140>>>
- **P191 MVRP 前提与作用**：裁剪广播/未知单播并动态建管 VLAN；须全局使能且 STP flat 模式。原句："MVRP is used primarily to prune unnecessary broadcast and unknown unicast traffic, and dynamically create and manage VLANs / In order to have MVRP enabled, switch must be in spanning-tree flat mode" <<<PAGE 968>>>
- **P192 MVRP 动态 VLAN 上限**：默认 256，调低需重启 MVRP 生效。原句："By default, the maximum number of dynamic VLANs that can be created using MVRP is 256" <<<PAGE 969>>>
- **P193 SLB 概念**：一组物理服务器逻辑为一个虚拟服务器（VIP 或 QoS 条件集群），线速 L3/L4 分发。原句："Method to logically manage a group of physical servers as one large virtual server (SLB cluster)" <<<PAGE 974-975>>>
- **P194 SLB VIP 代理 ARP**：VIP 须与服务器同网段，集群自动以交换机 MAC 代理 ARP。原句："SLB cluster automatically creates a proxy ARP for the VIP with the switch's MAC address" <<<PAGE 975>>>
- **P195 SLB 权重轮询**：WRR 权重总和 ≤32，weight 0 为备份服务器。原句："Aggregate weight of all servers should not exceed 32" <<<PAGE 977-979>>>
- **P196 SLB 双模式**：VIP 模式（L3 路由/桥接代理 ARP）与 QoS Condition 模式（按策略条件截流如防火墙）。原句："SLB Cluster QoS Condition - Traffic not destined to the server / I.e : firewall server simply inspects the packet" <<<PAGE 981-985>>>
- **P197 SLB 健康监测**：链路状态+ICMP ping+内容验证探针（20 个/switch：ftp/http/https/mail/nntp 等）。原句："Health Monitoring of the servers based on - Ethernet link state detection - IPv4 ICMP ping - Content Verification Probe" <<<PAGE 986-987>>>
- **P198 静态聚合命令差异**：R6 static linkagg/static agg vs R8 linkagg static agg/port；删除前须先清空成员口。原句："you cannot delete a link aggregation group if there" <<<PAGE 999-1002>>>

## 二十一、BGP / IS-IS / 安全认证 / IPv6（扩展）

- **P199 BGP 基本配置链**：router-id→ip load BGP→autonomous-system→neighbor remote-as→status enable；eBGP 多跳与 update-source Loopback0。原句："-> ip bgp neighbor 100.10.1.1 update-source Loopback0 / -> ip bgp neighbor 100.10.1.1 ebgp-multihop" <<<PAGE 1080-1081>>>
- **P200 BGP 策略过滤三列表**：aspath-list/community-list/prefix-list 配合 route-map。原句："-> ip bgp policy aspath-list “100 300 150” permit/deny / -> ip bgp policy community-list 600:1 permit/deny / -> ip bgp policy prefix-list 172.31.0.0 /16 permit/deny" <<<PAGE 1086-1088>>>
- **P201 IBGP 通告原则**：IBGP 学到的路由不应再通告给其他 IBGP 邻居（需全互联或路由反射器）。原句："Routes learned via IBGP should never be" <<<PAGE 1082>>>
- **P202 IS-IS 特性**：链路状态+SPF、两级区域层次、直接跑在二层（802.3/802.2）。原句："IS-IS uses Ethernet 802.3/802.2 instead of the Ethernet II used for IP traffic" <<<PAGE 1093-1096>>>
- **P203 NSAP 寻址**：Area ID+System ID(6B)+NSEL；本地管理 AFI=49；最小 8 字节。原句："The AFI should be set to 49 for locally administered IS-IS configurations" <<<PAGE 1094-1095>>>
- **P204 IS-IS 四类 PDU**：Hello（建邻/选 DIS）、LSP、PSNP（请求/确认）、CSNP（数据库全量同步）。原句："There are 4 types of PDUs: Hello (ESH, ISH, and IIH)… LSP… PSNP… CSNP" <<<PAGE 1096>>>
- **P205 DIS 选举**：仅在有邻接的路由器中按最高优先级/最高 MAC，可抢占，L1/L2 独立选举。原句："DIS election is based on priority and/or the highest MAC address and is preemptive" <<<PAGE 1098-1103>>>
- **P206 IS-IS CLI 模型**：全局 area-id/enable 后按 vlan 使能（ip isis vlan 5 address-family v4）。原句："-> ip isis area-id 49.0001 / -> ip isis vlan 5 / -> ip isis vlan 5 address-family v4" <<<PAGE 1105>>>
- **P207 安全认证章节**：802.1X/MAC 认证、RADIUS/LDAP/TACACS+ 服务器与 aaa test-radius-server 联调命令。原句："-> aaa test-radius-server My_radius type authentication user employee password password" <<<PAGE 677>>>
- **P208 IPv6 地址表示**：128bit，:: 双冒号仅一次；单播/组播/任播三类。原句："Successive fields of 0 can be represented as ::, but only once per address." <<<PAGE 1133-1134>>>
- **P209 链路本地地址**：FE80::/10+64bit 接口 ID，自动生成，用于 ND/路由发现，通信须指定出接口。原句："Link-local addresses have a scope limited to the link and are dynamically created on all IPv6 interfaces" <<<PAGE 1137>>>
- **P210 EUI-64 接口标识**：MAC 中插 FFFE 并翻转 U/L 位。原句："A modified EUI-64 address is formed by 'complementing' the 7th most significant bit (Universal/Local bit)… and inserting 'FFFE'" <<<PAGE 1138>>>
