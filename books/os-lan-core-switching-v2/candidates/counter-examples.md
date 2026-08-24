# counter-examples 候选 — DT00XTE216 OmniSwitch LAN Core Switching (Edition 15)

> 陷阱、配置错误、协议边界与失败案例。

## X-01 ERP：RPL 节点缺失或多个 = 非法配置；RPL 只能配在已禁用的环上
- 页码：<<<PAGE 55>>>
- 摘录："The RPL node can be configured only on a preexisting disabled ring. The non-existence of a RPL node or the existence of multiple RPL nodes is considered as incorrect configuration."
- 教训：每环有且只有一个 RPL；先建环（未 enable）再配 rpl-node。

## X-02 ERP：每环建议最多 16 节点，环数受机型限制
- 页码：<<<PAGE 55>>>
- 摘录："The maximum number of rings per node that can be created depends on switch model... A maximum number of 16 nodes per ring is recommended."
- 教训：超规模环网不可预期，需查 Network Configuration Guide。

## X-03 MACsec Static 模式不支持 OS6860N；VFL 堆叠口不支持 MACsec
- 页码：<<<PAGE 75>>>、<<<PAGE 72>>>
- 摘录："* MACsec - Static mode is not supported on OS6860N."（p75）；"MACsec not supported on OS6870-24 VFL stacking port 25/26 & OS6870-48 VFL stacking port 49/50"（p72）
- 教训：选型前核对平台矩阵；堆叠口链路不能加密。

## X-04 MACsec：64X10G 分支光模块/扩展模块不支持；9900 多板卡仅 Static
- 页码：<<<PAGE 71>>>
- 摘录："Expansion modules (Not supported on any 4X10G splitter transceivers)"；"OS9900-CMM 4X10G (Static mode only) / OS9900-XNI-48/P48 10G ports (Static mode only)" 等
- 教训：动态模式覆盖因板卡而异，部署前逐板卡确认。

## X-05 MVRP 仅支持 STP flat 模式；端口类型受限
- 页码：<<<PAGE 154>>>、<<<PAGE 160>>>
- 摘录："MVRP is supported only in STP flat mode"（p154）；"MVRP can be configured only on fixed, 802.1 Q and aggregate ports. It cannot be configured on mirror, unp, VPLS Access, and VLAN Stacking User ports"（p160 Notes）
- 教训：1x1 per-VLAN 模式下 MVRP 无法启用。

## X-06 MVRP 动态 VLAN 删不掉（会被自动重建）
- 页码：<<<PAGE 163>>>
- 摘录："sw5 -> no vlan 40 / ERROR: Dynamic vlan 40 cannot be deleted... The mvrp status is equal to the dyn. That means the VLAN 40 has been automatically re-created."
- 教训：必须先在源端删 VLAN 或禁用 MVRP，否则动态 VLAN 反复重建。

## X-07 MVRP：动态 VLAN 不建 IP 接口、不映射 MSTI；改 max-vlan 需重启 MVRP
- 页码：<<<PAGE 163>>>、<<<PAGE 161>>>
- 摘录："there's no ip interface creation nor association with MSTI"（p163）；"If the VLAN limit to be set is less than the current number of dynamically learned VLANs, then the new configuration will take effect only after the MVRP is disabled and enabled again"（p161）
- 教训：MVRP 只管二层连通，L3/MSTP 需手工补配。

## X-08 MSTP：1X1 与 MSTP 不能共存，必须 flat 模式
- 页码：<<<PAGE 143>>>
- 摘录："1X1 and MSTP cannot be configured at the same time; and the switch must be configured in flat Spanning Tree mode."
- 教训：切 MSTP 前先 `spantree mode flat`，实验后记得还原 per-vlan（p149）。

## X-09 MSTP 优先级必须是 4096 的倍数
- 页码：<<<PAGE 146>>>
- 摘录："Priority has to be multiple of 4096 (8192, 12288, 16384, …, 61440)"
- 教训：随意填值不生效。

## X-10 Port Mapping：一个端口只能属于一个会话
- 页码：<<<PAGE 202>>>
- 摘录："sw5 -> port-mapping 2 user-port 2/1/1 / ERROR: port user already part of an existing PMAP session"
- 教训：跨会话复用端口直接报错（单向会话的 network 口除外，见 p199）。

## X-11 LPS 不支持链路聚合端口；交换机自身多 MAC 会挤占学习额度
- 页码：<<<PAGE 190>>>、<<<PAGE 206>>>-<<<PAGE 207>>>
- 摘录："Not supported on Link Aggregate ports"（p190）；"there's 3 mac addresses: 1 from client 3 and 2 from 6560. The 6560 uses different mac addresses for Layer 2 traffic, like LLDP or STP and another one... for Layer3 traffic"（p206）
- 教训：对端交换机的 LLDP/STP/IP 多个源 MAC 会导致 restrict 误过滤，需关协议或 flush 后重学。

## X-12 LPS：convert-to-static 必须在设备 MAC 已学到之后执行
- 页码：<<<PAGE 208>>>
- 摘录："Please notice that the device must be learned on the LPS port before to enter the command port-security convert-to-static"
- 教训：先发流量再固化，否则无 MAC 可转静态。

## X-13 链路聚合加端口前必须清掉端口上的 VLAN 配置
- 页码：<<<PAGE 316>>>
- 摘录："sw5 -> linkagg lacp port 2/1/3 actor admin-key 8 / ERROR: Port cannot be added to Linkagg, please remove other configuration on this port"；随后 `no vlan 58/20/30 members port 2/1/3` 再加成功
- 教训：端口有 VLAN membership 时不能入聚合组。

## X-14 OSPF：单端先开认证会立刻丢邻居（Auth type mismatch）
- 页码：<<<PAGE 353>>>
- 摘录："+++ ospfAuthCheck: Intf 172.16.17.1: Auth type 1 mismatch! recvd pkt = (0)"；邻居从 2 个掉到 1 个，双端配置一致后恢复 Full
- 教训：生产开认证需两端窗口期内同步操作。

## X-15 OSPF：Hello Interval 不一致导致邻居无法 Full
- 页码：<<<PAGE 293>>>-<<<PAGE 294>>>
- 摘录："HELLO from 192.168.0.2 discarded...invalid helloInterval 10"（本端 20/对端 10）；"# of Full State Neighbors = 0"
- 教训：邻居参数（hello/dead/area/认证）必须完全一致；用 swlog debug 定位。

## X-16 OSPF stub 区域：两端 area type 必须一致；stub 内看不到外部路由
- 页码：<<<PAGE 355>>>-<<<PAGE 356>>>
- 摘录："sw7 -> ip ospf area 4.4.4.4 type stub" 与 "sw3 -> ip ospf area 4.4.4.4 type stub" 双端同配；"Switches in Stub Areas do not have external routes in their routing database"（p355 Notes）；6560 路由表无 AS-Ext，仅默认路由（p356）
- 教训：一端 stub 一端 normal 邻居起不来；stub 内依赖 ABR 默认路由出行。

## X-17 RIP：local/static 路由默认不通告，漏重分发=路由缺失
- 页码：<<<PAGE 228>>>
- 摘录："Only learned RIP routes and Loopback0 interface are advertised by default. Local and or static routes must be redistributed."
- 教训：RIP 网络里直连网段不自动外宣，必须 route-map+redist。

## X-18 递归静态路由的网关随目标路由变化，需防环路
- 页码：<<<PAGE 225>>>
- 摘录："The gateway to reach the 2.2.2.2 network has changed through RIP; so, the gateway to reach the 172.30.0.0 network has also changed"
- 教训：follows 目标路由翻动时静态路由随之漂移，设计时要确保 follow 目标稳定。

## X-19 私有 VLAN：一个 Primary VLAN 只能有一个 Isolated VLAN
- 页码：<<<PAGE 109>>>
- 摘录："There can be only one Isolated VLAN within one Primary VLAN."
- 教训：需要多组互不相通的用户时应使用多个 community，而不是多个 isolated。

## X-20 私有 VLAN 删除顺序（先成员后主 VLAN）
- 页码：<<<PAGE 112>>>
- 摘录："no pvlan 252 members port 1/1/1 / no pvlan 250 members linkagg 78 / no pvlan 250"
- 教训：直接删 primary 前需清理成员引用；实验后 `write memory flash-synchro` 保存。

## X-21 MACsec 与 ERP/组播等特性并存的许可前置：无 license 时功能不可用
- 页码：<<<PAGE 87>>>
- 摘录："If the licence MACsec is not available on the switch, refer to the appendix section to install it."
- 教训：实验/部署前 `show license-info` 预检，避免配置到一半失败。

## X-22 VRF：VLAN 只能属于一个 VRF；default 与自定义 VRF 的 import 需 all-routes
- 页码：<<<PAGE 460>>>、<<<PAGE 470>>>
- 摘录："Once a VLAN is associated with a specific VRF instance, configuring an interface for that VLAN within the context of any other instance, is not allowed. Use of Duplicate VLAN numbers is not supported"（p460）
- 教训：VLAN/VRF 归属是单向一对一，跨 VRF 复用同 VLAN 号会冲突。

## X-23 VRF 隔离的本意：不配 route leak 时跨 VRF 永远不通
- 页码：<<<PAGE 467>>>
- 摘录："Ping each other to test connection between them. What happens and why?"（两 VRF 客户端互 ping 失败）；"We will not be able to ping an IP interface of another VRF instance from one VRF instance within the same switch even the leaked routes are existed. This is due to security reason"（p468）
- 教训：即使路由已泄漏，交换机本机跨 VRF 接口 ping 也不通（安全设计），只能由客户端侧经验证。

## X-24 SPB：ISID 全局必须一致，BVLAN 映射也须一致
- 页码：<<<PAGE 555>>>
- 摘录："The ISID number is globally significant and must match across all BEBs connecting a given service. The BVLAN that the service is mapped must also match across all BEBs... Each ISID can be attached to one BVLAN only."
- 教训：service 号本地随意但 ISID/BVLAN 全局强一致，错配服务不通。

## X-25 SPB：control BVLAN 只能在协议禁用时修改；BVLAN 上无 STP
- 页码：<<<PAGE 548>>>
- 摘录："Control BVLAN can only be changed when protocol is disabled. There is no Spanning Tree on BVLANs"
- 教训：生产改 control BVLAN 需先 `spb isis admin-state disable`；BVLAN 域不要指望 STP 防环。

## X-26 SPB：BVLAN 数量不要超过物理等价路径数
- 页码：<<<PAGE 610>>>
- 摘录："There is no advantage in creating more BVLANs than the number of equal-cost-paths in the physical topology. Moreover... creates an additional unnecessary load in the CP"
- 教训：盲目建满 16 个 BVLAN 反而拖慢收敛。

## X-27 SPB：不同 VLAN 映射同一服务会导致 MAC 漂移（mac-move）
- 页码：<<<PAGE 610>>>
- 摘录："Duplicate MAC addresses in different VLANs do not collide, however, if these VLANs are mapped to the same SPB service... those MACs will be constantly learned, re-learned and flushed. This is known as a 'mac-move' and should be avoided"
- 教训：一个 VLAN 一个 ISID/SAP，避免虚拟化环境重复 MAC 引起震荡。

## X-28 动态服务默认 Service Modulo 512 会把不同 VLAN 混入同一服务
- 页码：<<<PAGE 601>>>
- 摘录："using the default Service Modulo of 512 can result in up to 8 different VLAN tags being mapped to the same service... it will result in different VLAN traffic being bridged in the same L2 domain. To ensure L2 isolation, we can change the Service Modulo to 4096"
- 教训：多租户/需隔离场景必改 modulo。

## X-29 聚合口 hash 在 SPB 场景熵不足
- 页码：<<<PAGE 611>>>
- 摘录："SPB backbone ports use MAC-in-MAC encapsulation which means MAC addresses are the BMACs... In most cases this does not create enough entropy and the load will not be spread evenly... a 'tunnel-protocol' option can be selected"
- 教训：SPB+LAG 必开 tunnel-protocol 哈希内层 CMAC/IP。

## X-30 Overload 状态开启后即使无替代路径也不转发
- 页码：<<<PAGE 605>>>
- 摘录："once the overload state is enabled on a node no traffic will transit through the node even if there are no alternative paths"
- 教训：维护隔离是硬隔离，确认冗余路径后再设 overload。
