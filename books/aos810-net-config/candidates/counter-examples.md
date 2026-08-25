# counter-examples — 限制/陷阱/注意事项（OmniSwitch AOS 8.10R4）

格式：编号 X# ｜ 陷阱要点 ｜ 英文原句（可选）｜ 页码

## 端口与链路（Ch1）

- **X1** 自协商禁用后无法再用 auto MDIX/speed/duplex："If autonegotiation is disabled, auto MDIX, auto speed, and auto duplex are not accepted." <<<PAGE 56>>>
- **X2** 端口别名只能配单口，不能配范围或整机："You cannot configure an entire switch or a range of ports." <<<PAGE 58>>>
- **X3** DDM 依赖光模块支持，并非全部模块可用："Not all transceivers support DDM." <<<PAGE 58>>>
- **X4** 默认风暴动作是纯丢包不告警；不显式配 action/trap 就无感知："no action is taken, packets above the threshold are dropped." <<<PAGE 59>>>
- **X5** 管理性关断的端口靠插拔网线/链路翻动无法恢复："Disconnecting/reconnecting the interface link or a link down/up event will not recover a port that was administratively disabled." <<<PAGE 69>>>
- **X6** 永久关断口自动恢复定时器无效，只能 clear violation/interfaces reset："The timer value does not apply to interfaces that are in a permanent shutdown state." <<<PAGE 71>>>
- **X7** 违规恢复机制不作用于聚合口本身，只作用成员口。<<<PAGE 71>>>
- **X8** 违规不叠加：已被别的特性关停、或链路不在 up 状态时不再施加新的违规关停。<<<PAGE 70>>>
- **X9** MACsec 需要站点 license（不绑序列号/MAC）。<<<PAGE 83>>>
- **X10** 静态 SA 模式两端必须配完全匹配的 SAK 名与值，漏一端即断："Each SAK name and value must have a corresponding matching value on the interface at the other end." <<<PAGE 84>>>
- **X11** 动态 CAK(EAP) 模式强制 EAP-TLS/PEAP；非双向认证无法派生 CAK："802.1x-authentication using EAP-TLS must be used as mutual authentication protocol." <<<PAGE 85>>>

## MAC/VLAN（Ch3-5）

- **X12** 静态 MAC 只支持固定端口；端口必须先属于目标 VLAN："The specified slot/port must already belong to the specified VLAN." <<<PAGE 105>>>
- **X13** 同 VLAN 内源地址撞静态 MAC 的包被丢弃；同一源地址不支持出现在同 VLAN 多个端口。<<<PAGE 105>>>
- **X14** 静态 MAC 配在 down 口上显示为无效（带星号），链路恢复才有效。<<<PAGE 105>>>
- **X15** 删除 VLAN 会连带删路由接口和全部 VPA，默认 VLAN 被删则端口回落 VLAN 1——误删业务风险。<<<PAGE 116>>>
- **X16** VLAN 在有活动端口前 oper 状态一直是 inactive，STP/路由接口也不活："The operational status of a VLAN remains inactive until at least one active switch port is assigned to the VLAN." <<<PAGE 115>>>
- **X17** 带 802.1Q tag 的包若 VID 既非端口默认 VLAN 又非该口 tagged VLAN，直接丢弃。<<<PAGE 118>>>
- **X18** NNI 口 TPID 非 0x8100 时不允许再打普通 802.1q VLAN tag。<<<PAGE 119>>>
- **X19** PVLAN：主 VLAN 的 VID 不能与现存 VLAN 冲突；UNP 口只能属于一个 PVLAN 域；IP 接口只能配在主 VLAN 上。<<<PAGE 129>>>
- **X20** HA VLAN 一旦成型标准 VLAN 命令失效："Once these types of ports are assigned, the standard VLAN commands no longer apply." <<<PAGE 140>>>

## 生成树/SPB（Ch6-7）

- **X21** per-VLAN 模式是 AOS 私有实现，与其他厂商互通受限（章内互通小节讨论 PVST+ 互操作）。<<<PAGE 164>>>
- **X22** MVRP 与 per-VLAN STP 互斥："If MVRP is configured in the system with STP flat mode, then STP mode cannot be changed to per-VLAN mode." <<<PAGE 444>>>
- **X23** MSTP 仅 Flat 模式支持；MSTI 的端口状态由 CST 统一算，不调 path cost 无法让单实例独立转发。<<<PAGE 164>>>
- **X24** SPB ECT 不同 BVLAN 全网不一致会导致路径不 congruent/对称，流量黑洞风险。<<<PAGE 214>>>
- **X25** SPBM 配置顺序颠倒（先服务后骨干）会导致 ISIS 邻接/SPT 参与异常："Following this order of configuration is highly recommended." <<<PAGE 245>>>
- **X26** BCB 不学客户 MAC，排障时在核心抓不到客户 MAC 属正常现象。<<<PAGE 211>>>
- **X27** SAP `:all` 与 `:x` 同时配置时，更精确的 CVLAN 匹配优先（VLAN10 流量进 service1 而非 service2），易误判分类结果。<<<PAGE 245>>>

## 环网/聚合（Ch8-13）

- **X28** MST 模式下 LBD 只能开在 STP 禁用的接口上。<<<PAGE 328>>>
- **X29** 聚合组任一成员口环回，整组 shutdown（连带故障面大）。<<<PAGE 328>>>
- **X30** remote-origin LBD 双端都开时，先收到远端帧的一端 shutdown（结果不确定）。<<<PAGE 327>>>
- **X31** 静态聚合不能与部分厂商设备对接："Static aggregate groups cannot be created between an OmniSwitch and some switches from other vendors." <<<PAGE 341>>>
- **X32** 聚合组成员必须同速，混速无法成组。<<<PAGE 341>>>
- **X33** DHL：未同时挂到 linkA/linkB 的 VLAN 不受保护；两链路必须同默认 VLAN 且该 VLAN 属保护集。<<<PAGE 382>>>
- **X34** DHL 每交换机仅一个会话、每会话仅两链路；会话使能中不得改链路归属；VLAN 数≤128/组；raw flooding 的 MAC≤1000。<<<PAGE 382>>>
- **X35** ERP Guard Timer 必须大于 R-APS 绕环最大时延，否则可能成环："This calculated value is required to prevent any looping scenarios within the ring." <<<PAGE 396>>>
- **X36** ERPv2 子环不能使用共享链路；共享链路只能属于一个主环。<<<PAGE 395>>>

## VPN/叠加（Ch15-18）

- **X37** 受限路径 LSP 不能跨 IGP 区域，也不能跨 AS 边界："They cannot cross an autonomous system (AS) boundary." <<<PAGE 458>>>
- **X38** VPLS 必须 PE 全网格 PW，漏配即部分站点不可达；Split Horizon 禁止 PW 到 PW 转发。<<<PAGE 478>>>
- **X39** BGP VPLS RR 仅支持 IPv4 地址族做反射。<<<PAGE 480>>>
- **X40** VXLAN VTEP 由 Loopback0 IP 标识，Loopback0 未配/改动会破坏隧道；UDP 端口改了必须两端一致（默认 4789）。<<<PAGE 535>>>
- **X41** EVPN 静态聚合口 ESI 不会自动生成，漏配将失去多归属别名与负载分担："It is required to manually configure the network unique ESI for the static LinkAgg." <<<PAGE 587>>>
- **X42** EVPN 本地 ESI 对象上限 256 个（8-bit local segment ID）。<<<PAGE 589>>>

## 三层（Ch21-26）

- **X43** VRF 内 IP 地址空间独立但跨 VRF 泄露须显式 route leak，天然隔离导致"配了通不了"的常见误判。<<<PAGE 756>>>
- **X44** link-local 地址不可跨链路路由；跨链路通信必须配全局单播地址。<<<PAGE 774>>>
- **X45** JITC 模式下 FEC0::/10 Site-Local 地址禁配。<<<PAGE 774>>>
- **X46** OmniSwitch IPsec 只支持传输模式，无隧道模式："The OmniSwitch currently supports the Transport Mode of operation." <<<PAGE 819>>>
- **X47** AH 不提供加密，误当机密性方案是典型错用："Unlike ESP, AH does not provide confidentiality." <<<PAGE 819>>>
- **X48** RIP 15 跳上限与 120 秒 hold-down 造成慢收敛，大网不适用。<<<PAGE 842>>>
- **X49** RIPv2 的不兼容特性只在组播更新时可用，广播回退到 RIPv1 兼容格式。<<<PAGE 843>>>
- **X50** BFD Echo 仅单跳；控制包可多跳——跨网段 VRRP/静态路由误配 Echo 会检测失效。<<<PAGE 870>>>
- **X51** BFD Demand 模式不支持。<<<PAGE 870>>>

## DHCP/VRRP/组播（Ch27-32）

- **X52** L3 Snooping 必须让客户端与服务器分居不同 VLAN，否则 relay 不介入、snooping 失效。<<<PAGE 925>>>
- **X53** 全局 Option-82 使能时任意级别 DHCP Snooping 都不可用；交换机级与 VLAN 级 Snooping 互斥。<<<PAGE 925>>>
- **X54** Snooping 丢非信任口的服务器报文——服务器口漏配 trusted 直接断 DHCP。<<<PAGE 925>>>
- **X55** 非信任口带 Option-82 的包默认丢弃（客户端侧私自插 82 的场景会断）。<<<PAGE 925>>>
- **X56** VRRP：本机 CMM 兼任 master 时 ping 虚 IP 不回应，只有外部路由器发起才回——排障常见误判。<<<PAGE 979>>>
- **X57** backup 优先级接近会产生接管时序冲突，先接管者未必最高优先级，随后被抢占产生抖动。<<<PAGE 980>>>
- **X58** IPMVLAN 模式（企业/Stacking）建后不可改，必须删除重建："An IPMVLAN configured in a specific mode must first be deleted, then re-created in the other mode." <<<PAGE 1086>>>
- **X59** Stacking 模式 IPMVLAN 仅允许一个 sender 口；IP 与 CVLAN-tag 两种绑定方式不要同时用。<<<PAGE 1087>>>

## QoS/AG（Ch33-35）

- **X60** policy 配置后不 `qos apply` 不生效（最常见的"配了没反应"）。<<<PAGE 1149>>>
- **X61** LDAP/PolicyView 创建的 QoS 对象不能在 CLI 改，反之亦然。<<<PAGE 1133>>>
- **X62** IPv4 与 IPv6 条件不能组合进同一 condition；destination VLAN 条件仅组播规则可用；source ip+ARP 组合仅 OS6860/E 支持。<<<PAGE 1135>>>
- **X63** 有效的规则也可能因依赖功能（如路由）未开而无法执行。<<<PAGE 1134>>>
- **X64** 802.1Q tagged 口默认 untrusted——上联口语音/视频标记不生效的常见原因。<<<PAGE 1134>>>

## SIP 监听（Ch20）

- **X65** SIP Snooping 一揽子限制：仅 IPv4、仅 UDP（含 UDP/TCP），不支持 TLS/SCTP/MPLS、不支持 SCTP/加密 RTCP/SDP、不支持 DNS/FQDN、无 VRF/NAT 感知："Only SIP over IPv4 is supported, no support for IPV6." <<<PAGE 704>>>
- **X66** 所有初始 SIP 消息必须过同一 SIP Server，端到端直连会话不支持；电话侧 outbound proxy 必须与交换机 trusted call server 一致。<<<PAGE 704>>>
- **X67** 边缘口 SIP IP 与 RTP IP 不一致时 TCAM 表项不建，QoS 不生效。<<<PAGE 704>>>
- **X68** TCAM 装表前的早发媒体流得不到 QoS 待遇。<<<PAGE 704>>>

## 其他（Ch36-47）

- **X69** LPS 不支持 linkagg/聚合成员口；学习窗口是全局值不能按口调。<<<PAGE 1536>>>
- **X70** 认证服务器不逐台轮询：第一台可用服务器上找不到用户即判失败，"The switch uses the first available authentication server to attempt to authenticate users. If user information is not found on the first available server, the authentication attempts fails." <<<PAGE 1475>>>
- **X71** TACACS+/LDAP 不支持端口准入（Access Guardian 只认 RADIUS）。<<<PAGE 1475>>>
- **X72** LINK OAM 5 秒收不到 OAMPDU 邻接即丢，keepalive 间隔配置不当会频繁掉 OAM 会话。<<<PAGE 1674>>>
- **X73** PPPoE-IA 不支持镜像目的口；全局+端口两级必须同时使能否则不生效。<<<PAGE 1715>>>
- **X74** MAC 认证把 MAC 同时作用户名密码，服务器侧格式不匹配（大小写/分隔符）会全军覆没（章 Device Authentication）。 <<<PAGE 1214>>>

---
合计：74 条（X1-X74）。
