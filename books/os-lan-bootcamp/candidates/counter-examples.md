# OmniSwitch R6/R8 Bootcamp Issue 25 — 陷阱/限制/注意事项候选（counter-examples）

> 摘自 Note/Warning/Caution 框与正文限制描述，页码来自 fulltext.md `<<<PAGE N>>>`。

## 硬件/供电

- **X1 6860 与 6850E 不可共用一台 BPS**：可各自接同一型号 BPS，但不能共享。原句："OS6860 and OS6850E sharing one BPS is not supported" <<<PAGE 58, 61>>>
- **X2 N+1 备电只防电源模块故障**：SINGLE 备份不防市电线路断电。原句："Protects against switch primary PSU failure not against AC power line failure" <<<PAGE 63>>>
- **X3 BPS 一次只备份一台交换机**：原句："BPS can backup only one switch at a time" <<<PAGE 63>>>
- **X4 6450-10 只能与 6450-10 堆叠**：不能与其他 6450 机型混堆。原句："OS6450-10 switches can only be stacked with other OS6450-10 switches." <<<PAGE 253>>>
- **X5 6350-10/P10 不支持堆叠**：原句："(Stacking OS6350-10/P10 switches is not currently supported.)" <<<PAGE 252>>>
- **X6 6450-10/P10 不支持远程堆叠**：原句："OS6450-10 and 6450-P10 switches do not support remote stacking." <<<PAGE 253>>>
- **X7 6860E-P24Z8 2.5G 端口成对配置**：自动协商只到 1G，2.5G 须手工且成对。原句："Auto-neg supported for 10/100/1000 Mbps only. Manual configuration to choose between 1G & 2.5G speeds" <<<PAGE 55>>>
- **X8 6860E 电源不可混插**：600W 与 920W 不能混用。原句："Both 600W & 920 W Supported; Default : 600W; No Mix-n-match" <<<PAGE 55>>>
- **X9 6860 专用 VFL 口不能当普通口**：原句："Dedicated VFL ports (2 x 20G) - Cannot be used as normal ports" <<<PAGE 300>>>
- **X10 6900-T 固定 10GBase-T 口不能作 VFL**：须加扩展模块。原句："Fixed 10 Gbase-T not supported" <<<PAGE 299>>>
- **X11 EMP 口是 RCD 的硬前提**：6860 无 EMP 口故不能使用 RCD 防脑裂。原句："Limitation: EMP port mandatory to use this feature - For example, an OmniSwitch 6860 doesn't have such port!" <<<PAGE 306>>>

## 系统/配置管理

- **X12 certified 目录不可直接保存**：从 certified 启动时改动无法 write memory，也无法跨目录移动文件。原句："Changes cannot be saved directly to the Certified directory / changes made to the switch cannot be saved and files cannot be moved between directories" <<<PAGE 131, 145, 148, 218>>>
- **X13 R6 无 modify running-directory 命令**：原句："In release 6, the \"modify ...\" command cannot be used." <<<PAGE 224>>>
- **X14 FTP 默认连 working 目录且认证默认关**：须 `aaa authentication ftp local`。原句："By default, an FTP session connects to the 'working' directory / FTP Authentication has to be enabled" <<<PAGE 136, 964>>>
- **X15 USB 默认禁用；移除前必须 usb disable**：原句："USB support is disabled by default / CAUTION: Do usb disable before removing usb" <<<PAGE 138, 225>>>
- **X16 USB backup 与 auto-copy 互斥**：原句："Back-up cannot be enabled if auto-copy is enabled and auto-copy cannot be enabled if back-up is" <<<PAGE 141>>>
- **X17 admin 账户仅 console 可改密码**：原句："By default, access only allowed through console port / Cannot be modified except for password" <<<PAGE 176>>>
- **X18 所有远程访问默认关闭**：仅 console 恒开。原句："Access through console (local) port is always enabled / By default all remote access is disabled" <<<PAGE 184>>>
- **X19 新建 end-user profile 默认无任何权限**：删除仍被用户引用的 profile 会导致该用户无法登录。原句："By default, new profiles do not allow access to any ports or VLANs / If a profile is deleted, but the profile name is still associated with a user, the user will not be able to log into the switch" <<<PAGE 182>>>
- **X20 R8 WebView 默认强制 SSL，R6 不强制**：原句："by default SSL is forced on R8 omniswitches but not on R6 ones" <<<PAGE 240>>>
- **X21 *.img 文件勿移动/删除**：原句："Be careful not to move or delete any important files such as the *.img files." <<<PAGE 237>>>
- **X22 无 boot.cfg 的目录在 write memory 时会自动创建 boot.cfg**：原句："If the directory does not contain a boot.cfg file, note that it will be created when the write memory" <<<PAGE 216>>>
- **X23 RCL/自动配置限制**：无 IPv6 支持、路径 63/255 字符限制、无 EMP 支持、开机变慢。原句："Increased Boot-up time / No EMP port supported / Filename and path length limited to 63 and 255 characters / No IPv6 support" <<<PAGE 157>>>
- **X24 远程实验虚拟机键盘布局**：原句："All VM are configured with an English US keyboard, your current keyboard layout is not take into account." <<<PAGE 203>>>

## 堆叠/VC

- **X25 堆叠不超过 8 台且版本必须一致**：原句："Never attempt to operate more than 8 switches in a single stack / Make sure all switches are running the same software version" <<<PAGE 261>>>
- **X26 无法登录 Idle/Pass-Through 单元**：原句："It is not possible to log on Idle switches (nor pass-through)" <<<PAGE 262>>>
- **X27 Secondary 上仅允许 takeover 等极少数命令**：原句："Secondary: no configuration allowed" <<<PAGE 262>>>
- **X28 槽号必须唯一且建议从 1 连续分配**：原句："it is important that each element in a stack is assigned a unique slot number. Do not assign…" <<<PAGE 279>>>
- **X29 takeover 前必须完成同步**：原句："A synchronization has to be done before takeover" <<<PAGE 260>>>
- **X30 reload all 可能落在 certified 分区**：原句："/!\ It can be on 'Certified' partition!" <<<PAGE 260>>>
- **X31 VC 写配置在拓扑变化时受保护警告**：原句："The command write memory is protected by issuing a warning to prevent or warn purging the configuration" <<<PAGE 317>>>
- **X32 VC 仅限 AOS R8 且须同机型**：原句："Restrictions: AOS R8 Only / Same type of switches in a Virtual Chassis" <<<PAGE 290>>>
- **X33 VC 脑裂双 Master 风险**：VFL 断而两机存活会出现两个 Master 同 IP 同 MAC。原句："having 2 Masters can results in problems, because the 2 switches are using the same IP and MAC address in the network" <<<PAGE 305>>>

## 诊断

- **X34 command.log 在启用期间不可删**：原句："Cannot be deleted while command logging is enabled" <<<PAGE 334>>>
- **X35 端口镜像与端口监控不能同 NI**：原句："Port mirroring and monitoring cannot be configured on the same NI" <<<PAGE 339, 342>>>
- **X36 swlog socket 需先配 Loopback0**：原句："Loopback0 have to be configured" <<<PAGE 326>>>
- **X37 镜像会话目标端口容量必须一致**：原句："Port requirements - must be of identical capacity" <<<PAGE 337>>>

## 二层（VLAN/LAG/STP/DHL/MVRP）

- **X38 VLAN 1 不可删除**：原句："This VLAN CANNOT be deleted, but it can be disabled if so desired." <<<PAGE 385>>>
- **X39 管理状态 down 的接口不响应 ping**：原句："down, it cannot be connected to, will not reply to PING requests nor will it be advertised in any router" <<<PAGE 387>>>
- **X40 802.1Q 标签不适用于 mobile 口（用 Mobile Tag）**：原句："VLAN Mobile Tag … Not supported on mobile ports（802.1Q 列）" <<<PAGE 383>>>
- **X41 一个端口只能属于一个聚合组；组非空不能删**：原句："One port can only belong to one link aggregation / you cannot delete a link aggregation group if there" <<<PAGE 395, 1001>>>
- **X42 组播默认只走聚合主端口**：除非开 non-ucast 哈希。原句："Multicast traffic is by default forwarded through the primary port of the Link Aggregation Group" <<<PAGE 402, 887>>>
- **X43 1x1 与 MSTP 不能同时配置**：MSTP 须 flat 模式。原句："1X1 and MSTP cannot be configured at the same time; and the switch must be configured in flat Spanning Tree mode." <<<PAGE 471>>>
- **X44 切换 MSTP 会重置 flat 优先级与路径开销**：原句："WARNING: Changing to MSTP(802.1s) resets flat bridge priority and path" <<<PAGE 471>>>
- **X45 MSTP 链路须承载实例全部 VLAN**：否则不承载任何。原句："Ensure that a link carries all of the VLANs mapped to an instance, or do not carry any VLANs at all for this instance" <<<PAGE 444>>>
- **X46 MSTP 32bit 开销与 802.1d/w 默认 16bit 不兼容注意**：原句："16-bit path cost value that 802.1d/802.1w use by default." <<<PAGE 471-472>>>
- **X47 PVST+ 端口必须 1x1 模式**：原句："Ports must be configured in 1x1 mode" <<<PAGE 434>>>
- **X48 DHL 每机仅一会话；DHL 口上 STP 自动禁用**：原句："Only one session per switch is allowed / Spanning Tree is disabled on all the DHL enabled ports" <<<PAGE 478, 488>>>
- **X49 MVRP Enhanced 不支持 6250/6450**：DHL MAC 冲刷只能选 RAW。原句："the MVRP Enhanced is not supported on AOS OmniSwitches 6250 & 6450" <<<PAGE 479>>>
- **X50 MVRP 须 STP flat 模式且不能配在 mirror/mobile/VPLS 口**：原句："MVRP can be configured only on fixed, 802.1 Q and aggregate ports. It cannot be configured on mirror, mobile, VPLS Access, and VLAN Stacking User ports." <<<PAGE 968>>>
- **X51 MVRP 调低动态 VLAN 上限需重启 MVRP 生效**：原句："the new configuration will take effect only after the MVRP is disabled and enabled again" <<<PAGE 969>>>

## 三层与服务

- **X52 LLDP 不能按 linkagg 配置**：原句："LLDP is configured at port level (or NI or chassis), but not at linkagg level." <<<PAGE 519>>>
- **X53 VRRP 与 HSRP 不兼容**：原句："Not compatible with HSRP" <<<PAGE 524>>>
- **X54 VRRP 备份路由器优先级应彼此不同**：避免同时升主。原句："It is important to define different priorities on the backup routers." <<<PAGE 527>>>
- **X55 QoS 默认放行一切未匹配流量（accept）**：配错 disposition 可能全断。原句："Denies all bridged, routed or multicast traffic by default（配 deny 后）/ By default, bridged, routed, and multicast flows that do not match any policies are accepted" <<<PAGE 558, 586, 620>>>
- **X56 QoS phones/nms 信任仅前 8 个接口**：按 ifIndex 顺序。原句："Only supported on the first 8 interfaces in order of creation. Defined by their ifIndex" <<<PAGE 582>>>
- **X57 condition/action 被规则引用时不可删；参数互斥**：原句："an action cannot be deleted if it is currently being used by a policy rule… some action parameters are only supported with particular condition parameters" <<<PAGE 593-594>>>
- **X58 交换端口默认不信任标记**：原句："By default, switched ports are not trusted." <<<PAGE 590, 598>>>
- **X59 Egress 过滤仅限特定平台/方向**：原句："Egress Filtering is only supported on" <<<PAGE 575>>>
- **X60 6450 可对 UNP 直接限速，R8 不行**：原句："On the 6450 we can apply a bandwidth restriction directly to the UNP, this is not possible in release 8" <<<PAGE 676>>>
- **X61 Captive Portal/Profile/Block 是终结策略**：后不能跟其他策略。原句："Some policies (Captive portal, Profile, Block) are terminal policies (cannot be followed by other policies)" <<<PAGE 1014>>>

## 路由

- **X62 RIP invalid 必须 ≥3×update**：AOS 强制约束。原句："AOS to enforce the constraint that invalid cannot be less than 3x of update" <<<PAGE 730>>>
- **X63 RIP 默认不通告本地/静态路由**：必须重分发。原句："Only learned RIP routes and Loopback0 interface are advertised by default." <<<PAGE 726, 746>>>
- **X64 RIP 默认收 v1/v2 发 v2；默认无认证**：原句："By default, RIP is configured to accept either RIP v1 or RIP v2 updates, and sends out RIP v2" <<<PAGE 745, 748>>>
- **X65 OSPF/ISIS 的 GR 默认关、BGP 默认开**：原句："Note: Graceful restart is disabled for OSPF and ISIS and enabled for BGP by default" <<<PAGE 776>>>
- **X66 递归静态路由 6.7.1 不可用**：原句："Option not available in AOS 6.7.1" <<<PAGE 719>>>
- **X67 IBGP 学到的路由不应再传 IBGP 邻居**：原句："Routes learned via IBGP should never be" <<<PAGE 1082>>>
- **X68 VRF 名大小写敏感；VLAN 编号不可在 VRF 间重复使用**：原句："Note: VRF names are case sensitive / Use of Duplicate VLAN numbers is not supported" <<<PAGE 859, 861>>>
- **X69 一个 IP 接口+其 VLAN 同时只能属一个 VRF**：原句："A single IP interface, as well as the VLAN associated with the interface, can only belong to one VRF instance at a time" <<<PAGE 861>>>

## 组播/ERP

- **X70 IGMP 永不被路由器转发（TTL=1）**：原句："IGMP is a protocol confined to the local segment of the LAN and is never forwarded by any router." <<<PAGE 871>>>
- **X71 IPMS 默认禁用；组播交换须显式开启**：原句："Before you begin, notice that Multicast Switching is disabled by default" <<<PAGE 877, 916>>>
- **X72 ERP RPL 只能配在已禁用的环上；无 RPL 或多 RPL 均为错误配置**：原句："The RPL node can be configured only on a preexisting disabled ring. The non-existence of a RPL node or the existence of multiple RPL nodes is considered as incorrect configuration." <<<PAGE 929>>>
- **X73 每环建议 ≤16 节点**：原句："A maximum number of 16 nodes per ring is recommended." <<<PAGE 929>>>
- **X74 ERP 环数上限依机型**：原句："The maximum number of rings per node that can be created depends on switch model" <<<PAGE 929>>>
- **X75 SPT 状态默认启用**：PIM-SM 中 `SPT status is enabled by default` <<<PAGE 903>>>

## PoE/安全

- **X76 PoE 操作状态默认 down，须 lanpower start**：原句："Def PoE oper status - Disabled (PoE must be activated on a switch-by-switch basis (lanpower start)" <<<PAGE 697-698>>>
- **X77 电容检测不符合 802.3af、仅限老话机**：原句："not compatible with IEEE specification 802.3af / It should only be enabled to support legacy IP phones" <<<PAGE 702, 706>>>
- **X78 LPS 不支持聚合口**：原句："Not supported on Link Aggregate ports" <<<PAGE 804>>>
- **X79 LPS 默认违规 restrict、300 秒自动清**：原句："By default, the port violation is restricted… there's a timer of 300 seconds to clear automatically the violation." <<<PAGE 850, 852>>>
- **X80 端口默认只学 1 个 MAC**：接傻瓜交换机/集线器即违规。原句："By default, port security allows the switch to learn only a single MAC address" <<<PAGE 850>>>
- **X81 ARP 毒化受限地址每接口最多 2 个**：原句："Maximum of two IP addresses per IP interface" <<<PAGE 824>>>
- **X82 DHCP 非信任口丢弃 Offer/ACK**：只收 Discover/Request。原句："Untrusted ports only accept DHCP Discover and Request messages - DHCP Offer and ACK are dropped" <<<PAGE 830>>>
- **X83 MACsec 支持面限制**：6860 仅 10G 口；E-P24Z8 不支持 2.5G 口；99-CMM 仅 4x10G 模式。原句："OS6860(E) 10G ports on all E/non-E models / (not supported on 2.5G ports)" <<<PAGE 827>>>
- **X84 Stack/VC 镜像文件差异**：V72/C32 用 Yos.img 与其他 6900 的 Tos.img 不同。原句："The OS6900-V72/C32 uses a different image file (Yos.img)" <<<PAGE 86, 87>>>

## 升级/其他

- **X85 镜像传输必须 binary、配置必须 ASCII**：原句："If you are transferring a switch image file, you must specify the binary transfer mode" <<<PAGE 965>>>
- **X86 VC 成员若为非 E 型 6860 仍需有效 license key**：原句："If part of a VC, the OS6860 non-E models must still have a valid license key" <<<PAGE 59>>>
- **X87 CodeGuardian 美加强制订阅、其余地区可选**：原句："US & Canada: Mandatory CodeGuardian 1-year subscription license / Rest of the world: Optional" <<<PAGE 111>>>
- **X88 ProActive Lifecycle 需本地 OmniVista 2500**：属性每两周推送云。原句："By default, the product attributes are pushed from the OmniVista 2500 NMS every two weeks." <<<PAGE 1139>>>
- **X89 堆叠写入 protected 警告防清配置**：write memory 在拓扑变化时警告。原句："protected by issuing a warning to prevent or warn purging the configuration of the elements" <<<PAGE 315, 317>>>
