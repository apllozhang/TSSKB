# counter-examples.md — 限制/陷阱候选（X1…，英文原句）
来源：《OmniSwitch AOS Release 8.10R4 Advanced Routing Configuration Guide》。页码为 `<<<PAGE N>>>` 真实标记。

## OSPF / OSPFv3

- **X1 Stub 区域两条硬限制（无虚链路、无 ASBR）**：Two restrictions on the use of stub areas are: Virtual links cannot be configured through stub areas. AS boundary routers cannot be placed internal to stub areas. <<<PAGE 27>>>（OSPFv3 同文见 <<<PAGE 64>>>）
- **X2 NSSA/完全末节区域内同样禁虚链路，且区域类型必须全网一致**：AS-external LSAs are not flooded into an NSSA and virtual links are not allowed in an NSSA. …All routers in an NSSA must have their OSPF area defined as an NSSA. To configure otherwise will ensure that the router will be unsuccessful in establishing an adjacent in the OSPF domain. <<<PAGE 28>>><<<PAGE 65>>>
- **X3 虚链路是"最后手段"，不连续骨干是劣构**：This is not an ideal OSPF configuration, and maximum effort should be made to avoid this situation. …Accepted network design theory states that virtual links are the option of last resort. <<<PAGE 26>>><<<PAGE 39>>>
- **X4 单路由器不建议带超过三个区域**：standard networking design does not recommended that more than three areas be handled on a single router. <<<PAGE 33>>><<<PAGE 70>>>
- **X5 ECMP 只看度量不看带宽，可能选中慢链路**：So it is possible for OSPF to decide two paths have an equal cost even though one may contain faster links than another. <<<PAGE 29>>>
- **X6 接口名不能含空格**：The interface name cannot have spaces. <<<PAGE 21>>><<<PAGE 36>>><<<PAGE 73>>>
- **X7 MD5 key ID 与 key string 必须两条命令分别设置**：Note that setting the key ID and key string must be done in two separate commands. <<<PAGE 37>>>
- **X8 被动接口上已存在的邻接会立即拆除**：if a OSPF-enabled interface is configured as passive where an adjacency already exists, the adjacency drops almost immediately. <<<PAGE 46>>>
- **X9 多区域域中被动接口只会生成在 Area ID 最小的区域**：If there are multiple areas configured in an OSPF domain, the passive OSPF interfaces will be created in the area with the lowest-numbered Area ID, which is usually the Backbone Area. <<<PAGE 46>>>
- **X10 从内存移除 OSPF/OSPFv3/IS-IS 必须手改 boot.cfg 并重启**：To remove OSPF from the router memory, it is necessary to manually edit the boot.cfg file. …For the operation to take effect the switch needs to be rebooted. <<<PAGE 33>>><<<PAGE 70>>><<<PAGE 102>>>
- **X11 接口参数可一次配多个但只能逐个恢复默认**：Although you can configure several parameters at once, you can only reset them to the default one at a time. <<<PAGE 39>>>
- **X12 OSPF stub default-metric 当前仅支持 ToS 0**：At this time, only the default metric of ToS 0 is supported. <<<PAGE 35>>>
- **X13 NBMA 的 DR eligibility 配置必须与其他路由器接口优先级一致**：the neighbor eligibility configuration for a router on every other router should match the routers interface priority configuration. <<<PAGE 29>>>

## IS-IS

- **X14 IS-IS GR 当前仅支持 helper 模式**：In the current release, only the graceful restart helper mode is supported. <<<PAGE 116>>>
- **X15 IS-IS GR 仅在堆叠备/空闲交换机的活动口上支持**：Graceful restart is only supported on active ports (i.e., interfaces), which are on the secondary or idle switches in a stack during a takeover. It is not supported on ports on a primary switch in a stack. <<<PAGE 116>>>
- **X16 次 CMM 路由 MAC 不同或 VLAN 端口在主模块时，STP 重收敛可能中断 GR 转发**：If the secondary module has a different router MAC than the primary module, or if one or more ports of a VLAN belonged to the primary module, spanning tree re-convergence might disrupt forwarding state, even though IS-IS performs a graceful restart. <<<PAGE 116>>>
- **X17 route map 的 tag 参数当前版本不支持**：The tag parameter is not supported in the current release. <<<PAGE 110>>>
- **X18 metric 大于 64 必须先开 wide-metrics**：Wide metrics need to be enabled, if a metric of more than 64 is configured. <<<PAGE 115>>>
- **X19 每路由器最多 3 个 area ID**：Each router can have a maximum of 3 area IDs assigned to it. <<<PAGE 102>>>
- **X20 L1 内部路由不能汇总（只有外部重分发路由可以）**：It is not possible to summarize IS-IS internal routes at Level-1, although it is possible to summarize external (redistributed) routes. <<<PAGE 104>>>
- **X21 点到点链路两端口 L1 未配认证时，无论 L2 配置如何 L1 hello 都裸奔**：On a point-to-point link with both levels enabled, if no authentication is configured for Level 1, the hello packets are sent without any password regardless of the Level 2 authentication configurations. <<<PAGE 107>>>
- **X22 retransmit 间隔须大于往返时延否则无谓重传**：The retransmit interval should be greater than the expected round-trip delay between two devices. This will avoid any needless retransmission of PDUs. <<<PAGE 110>>>
- **X23 切换 multi-topology 模式会复位全部 IS-IS 邻接**：Changing the multi-topology mode with this command will result in internal disabling and re-enabling of IS-IS protocol, with the new mode of operation. This causes IS-IS adjacencies to be reset. <<<PAGE 120>>>
- **X24 encrypt-key 只接受系统生成的合法值**：Only valid system generated values are accepted as encrypt-key. <<<PAGE 106>>>

## BGP

- **X25 一批全局命令改前必须先禁用 BGP（AS 号、本地优先、MED、同步、RR、cluster-id 等）**：Many BGP global commands require the user to disable the protocol before changing parameters. <<<PAGE 139>>>
- **X26 CIDR 斜杠写法不支持于 CLI，需写全掩码**：Although CIDR is supported by the router, CIDR route notation is not supported on the CLI command line. For example, in order to enter the route "198.16.10.0/24" input "198.16.10.0 255.255.255.0". <<<PAGE 137>>>
- **X27 MP-BGP 当前不支持 IPv6 dampening、IPv6 聚合、VPN/MPLS 标签等多协议能力**（注意：IPv6 aggregate 的配置小节后文出现，存在文档内部矛盾）：Some features that are not supported in the current release of Multiprotocol BGP include: IPv6 route-flap dampening…IPv6 route aggregation…Other multiprotocol capabilities for VPNs, MPLS label exchanges. <<<PAGE 177>>>
- **X28 AS 正则常见错误：数字超界、逗号被当分隔符、括号嵌套、^ 不在首/$ 不在尾、重复符不能作用于行首**：66543 Number is too large. AS numbers must be in the range 1 to 65535. / Parthentheses may not be nested. / The "^" metacharacter must occur first in the pattern… <<<PAGE 136>>>
- **X29 dampening 参数必须整条按序一次输入，不能单独改**：To change one variable to a number different than its default value, you must enter all of the variables with the ip bgp dampening command in the correct order. <<<PAGE 157>>>
- **X30 无聚合内至少一条更精确路由则聚合不成立**：You cannot aggregate an address (for example, 100.10.0.0) if you do not have at least one more-specific route of the address (for example, 100.10.20.0) in the BGP routing table. <<<PAGE 152>>>
- **X31 RR 冗余过多会推高内存**：Using many redundant reflectors is not recommended as it places demands on the memory required to store routes for all redundant reflectors' peers. <<<PAGE 163>>>
- **X32 同步开启会给 AS 内非 BGP 路由器带来大负担**：since routes learned over external BGP can be numerous, enabling synchronization can place an extra burden on non-BGP routers. <<<PAGE 144>>>
- **X33 BGP 软件不随启动自动加载，须手动 ip load bgp**：The BGP software is not loaded automatically when the router is booted. The user must manually load the software into memory. <<<PAGE 125>>>
- **X34 BGP peer 不会动态学习，必须逐个显式配置**：BGP peers are not dynamically learned. BGP peers must be explicitly configured on the router using the ip bgp neighbor command. <<<PAGE 147>>>
- **X35 部分 peer 命令（如定时器）不自动复位会话，需手动 clear 才生效**：there are some peer commands (such as those configuring timer values) that do not reset the peer. If you want these parameters to take effect, then you must manually restart the BGP peer using the ip bgp neighbor clear command. <<<PAGE 149>>>
- **X36 纯 IPv6 网络必须显式配置 router-id 与 IPv4 primary 地址（AGGREGATOR 用）**：In homogeneous IPv6 networks (i.e., in the absence of IPv4 interface configuration), the router's router ID and the primary address must be explicitly configured prior to configuring the BGP protocol. <<<PAGE 179>>>
- **X37 IPv4 地址对等且已建会话时不能关 IPv4 unicast**：However, in IPv6 environments where the BGP speakers have established peering using their IPv4 addresses, IPv4 unicasting may not be disabled. <<<PAGE 180>>>
- **X38 GTSM 与 eBGP multihop 互斥，同配报错；GTSM 须两端同配**：When GTSM is enabled, eBGP multihop must be disabled or vise-versa. Attempting to configure GTSM when eBGP multihop is configured or vice-versa will display an error message. …GTSM must be manually configured on all the participating switch in the peering session. <<<PAGE 212>>>
- **X39 route map policy 引用的子策略必须先创建，否则报错**：Conditions added to a route map policy must have already been created using their respective policy commands. If you attempt to add non-existent policies to a route map policy, an error message is returned. <<<PAGE 205>>>
- **X40 VPLS 能力依赖 MPLS license 与 MPLS BGP 二进制，启用前必须先禁 BGP**：To enable VPLS capabilities in BGP, MPLS license must be installed first. …BGP protocol must be disabled using the ip bgp admin-state command before enabling VPLS capabilities in BGP. <<<PAGE 214>>>
- **X41 BGP 邻居模板当前仅支持 EVPN 族命令**：Currently, BGP neighbor template is supported only for EVPN family commands. <<<PAGE 218>>>
- **X42 模板不会覆盖已存在的个体 peer 配置，想生效须先删个体配置**：Once the template is applied on the peer, the template configurations will not override the existing BGP peer configuration until the individual BGP peer configuration is present. To apply the BGP neighbor template configuration on the peer, first remove the individual peer configuration. <<<PAGE 218>>>
- **X43 VRF 内 BGP peer 默认上限 32**：By default, maximum of 32 peers per VRF is supported. <<<PAGE 144>>>

## DVMRP / PIM / MBR

- **X44 每接口仅支持一个组播路由协议（PIM 与 DVMRP 不能同接口共存）**：Only one multicast routing protocol is supported per interface. This means that you cannot enable both PIM and DVMRP on the same interface. <<<PAGE 238>>><<<PAGE 266>>>
- **X45 协议未加载即配置会报 "application is not loaded"**：If DVMRP is not loaded and you enter a configuration command, the following message displays: ERROR: The specified application is not loaded. <<<PAGE 237>>><<<PAGE 265>>>
- **X46 组播边界地址必须是 239/8 管理作用域段**：The boundary address must be an administratively-scoped multicast address from 239.0.0.0 to 239.255.255.255. <<<PAGE 224>>>
- **X47 修改 prune-lifetime 可能令已接收的 prune 提前/延后过期，只能谨慎改**：the value of ip dvmrp prune-lifetime should only be modified with caution. …received prunes may expire sooner or later than the neighbor expects. <<<PAGE 243>>>
- **X48 show ip dvmrp prune 只显示发出的 prune 不显示收到的**：However, note that this command does not display received prunes. <<<PAGE 243>>>
- **X49 隧道两端（源地址接口与隧道接口）都要使能 DVMRP 否则不 operational**：DVMRP needs to be enabled on the IP interface of the source address of the tunnel and also on the configured tunnel interface. The tunnel will be operational only when the DVMRP interface is also operational. <<<PAGE 244>>>
- **X50 flash-interval 必须小于 report-interval**：Routing Table Change messages are sent between transmissions of the complete routing tables…For this reason, the Flash Interval value must be lower than the Route Report interval. <<<PAGE 241>>>
- **X51 老版本 DVMRP 用 Route Report 而非 Probe 做邻居发现（互通注意）**：Older versions of DVMRP use Route Report messages to perform neighbor discovery rather than the Probe messages used in DVMRP Version 3. <<<PAGE 233>>><<<PAGE 240>>>
- **X52 邻居有初始大流量冲击问题时建议把 subord-default 改 false**：if neighbors in the DVMRP domain have difficulty handling large initial bursts of traffic, it is recommended that the subordinate neighbor status is changed to false. <<<PAGE 237>>>
- **X53 OmniSwitch PIM 只兼容 SMv2，不兼容 SMv1**：The OmniSwitch supports PIM-DM and PIM-SMv2 but is not compatible with PIM-SMv1. <<<PAGE 254>>>
- **X54 Hello 报文无法区分 DM/SM 邻居，DM 不应与 SM 直接交互**：A PIM router cannot differentiate a PIM-DM neighbor and a PIM-SM neighbor based on Hello messages, and PIM-DM is not intended to interact directly with a PIM-SM router. <<<PAGE 258>>>
- **X55 SPT 状态关闭则 SPT 切换不发生**：SPT status must be enabled for SPT switchover to occur. If the SPT status is disabled, the SPT switchover will not occur. <<<PAGE 262>>>
- **X56 SSM 默认地址段（232/8、FF3x::/32）不会自动启用，须手动配置**：The PIM-Source-Specific Multicast (SSM) mode for the default SSM address range is not enabled automatically and needs to be configured manually to support SSM. <<<PAGE 264>>><<<PAGE 282>>>
- **X57 IGMP 代理场景必须 v3 否则 PIM-SSM 不工作**：For networks using IGMP proxy, be sure that the IGMP proxy version is set to Version 3. Otherwise, PIM-SSM will not function. <<<PAGE 264>>>
- **X58 改 max-rps 前必须先全局禁用 PIM-SM**：PIM must be globally disabled on the switch before changing the maximum number of RPs. <<<PAGE 271>>>
- **X59 C-RP 配置在未使能 PIM 的接口上会报错**：If you attempt to configure an interface that is not PIM enabled as a C-RP, you will receive the following error message: ERROR: PIM is not enabled on this Interface. <<<PAGE 270>>>
- **X60 每交换机只支持一个 RP 地址**：Only one RP address is supported per switch. If multiple candidate-RP entries are defined, they must use the same RP address. <<<PAGE 270>>>
- **X61 priority 与 override 参数互斥，配了 priority 则 override 失效**：As specifying the priority value obsoletes the override option, you can use only the priority parameter or the override parameter. <<<PAGE 268>>><<<PAGE 273>>>
- **X62 Anycast-RP 地址不能与 Router ID 相同（建议用 Loopback0 之外的接口）**：The Router ID used by the unicast routing protocols must not be the same as the IP address being used for this Anycast-RP address. <<<PAGE 275>>>
- **X63 Anycast-RP 静态 RP 配置必须配在域内所有 PIM 路由器，不只是 RP 成员**：This static configuration must exist on all PIM routers in the PIM domain, not just those routers that are participating in the Anycast-RP set. <<<PAGE 275>>>
- **X64 register-packing 配 Anycast-RP 时仅当 RP set 全体支持才启用；建议全 domain force-enable**：PIM register packing should be enabled only if it is supported by all PIM anycast RP members in the RP set for the RP address. <<<PAGE 278>>>
- **X65 Register/Join-Prune 打包仅 SM 支持（DM 无周期 Join，不支持）**：This feature will only work with PIM-SM, PIM-SSM and PIM-BIDIR. This feature will not be supported with PIM-DM. <<<PAGE 280>>><<<PAGE 295>>>
- **X66 register-mtu 过大且 RP 不支持时会产生分片重组，不建议调大**：It is not recommended to configure to a large value unless it is known that all the RP routers in the domain can support the MTU size. <<<PAGE 279>>>
- **X67 Join/Prune 实际最大尺寸取接口 IP MTU 与配置值的较小者**：the actual maximum size used for PIM Join/Prune messages will be the smaller of the IP MTU value of the interface and the configured PIM interface Join/Prune MTU value. <<<PAGE 280>>>
- **X68 MBR 不支持 PIM-SSM，也不支持 PIM 与其他协议或多个 PIM 域之间互通**：Interoperability between PIM and other protocols or between multiple PIM domains is not supported. In addition, PIM support refers only to PIM-DM and PIM-SM (PIM-SSM is not supported). <<<PAGE 299>>>
- **X69 MBR 使能但 PIM/DVMRP 未各有一个 enabled 接口前不 operational**：It is possible for MBR to be enabled, but until both PIM and DVMRP have enabled at least one interface and are active, then MBR functionality is still not operational. <<<PAGE 300>>>
- **X70 MBR 的 DVMRP 默认路由不能向 MBONE 通告**：When enabling this type of advertisement, make sure that the default route is not advertised on the MBONE. <<<PAGE 302>>>
- **X71 高级路由特性需购买附加包，且平台支持随机型差异（见规格与发布说明）**：The routing protocols described in this manual are purchased as an add-on package to the base switch software. <<<PAGE 12>>>
