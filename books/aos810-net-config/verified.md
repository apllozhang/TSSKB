# Verified 候选（V1 原文真实性核对 + V2/V3 抽查）

## cases

## 端口与基础（Ch1-3）
- **C1** 端口基础参数批量配置：`interfaces 2/3 autoneg enable`、`interfaces 2/1-3 crossover mdi`、`interfaces 2/1 speed 100`、`interfaces 2/1 duplex full`、`interfaces 2/3 link-trap enable`、`interfaces 2/3 admin-state disable`（支持单口/范围/整槽）。验证：show 系列命令。 <<<PAGE 56>>>
- **C2** DDM 监控启用：`interfaces ddm enable` + `interfaces ddm-trap enable`（阈值越界告警）。注意光模块必须支持 DDM。 <<<PAGE 58>>>
- **C3** 风暴控制与动作：`interfaces 2/1/1 flood-limit bcast rate mbps 100`；动作 `interfaces 1/1/1 flood-limit bcast action shutdown`；自动恢复 `interfaces 1/1/1 flood-limit bcast rate mbps 60 low-threshold 40`。 <<<PAGE 59>>>
- **C4** 流控配置：`interfaces ... pause tx-and-rx`（tx/rx/tx-and-rx 三态）。 <<<PAGE 60>>>
- **C5** 违规恢复调优：`violation recovery-time 600`（全局）、`violation port 1/2/1 recovery-time 200`（按口）；默认 300 秒。 <<<PAGE 71>>>
- **C6** 静态 MAC（bridging/filtering）：`mac-learning vlan 1 port 1/1 static mac-address 00:00:02:CE:10:37 bridging`；删除用 no 形式；聚合口写 linkagg ID。验证：`show mac-learning`。 <<<PAGE 106>>>
## VLAN/PVLAN（Ch4-5）
- **C7** VLAN 创建与打标成员：`vlan 755 name "IP Finance Network"`、`vlan 10-15` 批量建、`vlan 5 members port 1/4/3 tagged`、`vlan 755 members linkagg 10 untagged`、`vlan 7 admin-state disable`、`no vlan 200`。验证：`show vlan port`。 <<<PAGE 116>>>
- **C8** 跨交换机 VLAN 桥接（tagged+untagged 混跑）：两交换互联口对 VLAN1 untagged、VLAN2/3 tagged，实现单链多 VLAN。 <<<PAGE 118>>>
- **C9** PVLAN 部署：建 Primary VLAN→建 isolated/community 二级 VLAN 关联主 VLAN→配 promiscuous/ISL 口→二级 VLAN 关联用户口。验证：`show pvlan`、`show pvlan mapping`、`show pvlan members`。 <<<PAGE 128>>>
- **C10** HA VLAN 服务器集群：建 VLAN→加入集群口→分配 cluster 模式→配虚 MAC（L2 用静态 MAC、L3 用静态 ARP，可加 IGMP 组播地址）。验证：show HA VLAN status（章 5 各 Example）。 <<<PAGE 140>>>
## 生成树（Ch6）
- **C11** per-VLAN RSTP 样例网络：四交换、VLAN 255、802.1w；根桥以最低桥 ID（priority+MAC）选出，路径成本决定 forwarding/blocking。配置步骤见章内 Example Network Configuration Steps。 <<<PAGE 197>>>（6-45 页）
- **C12** MST 区域配置：`spantree mst region <name>`+revision+VLAN-MSTI 映射（Sample MST Region Configuration 节）。 <<<PAGE 202>>>（6-48 页）
- **C13** MSTI 调优：对特定 MSTI 配端口 path cost/priority，使该 MSTI VLAN 走独立路径而不影响 CIST（Sample MSTI Configuration）。 <<<PAGE 205>>>（6-50 页）
- **C14** Root Guard/边缘口等端口参数：`spantree port ... `（edge port、root guard、限制 TCN 传播、限 BPDU 发送，章内 Configuring STP Port Parameters 各节）。 <<<PAGE 189>>>（6-35 页）
- **C15** SPBM 骨干六步（每台交换机）：`system name BEB-1`→`spb bvlan 4001`/`spb bvlan 4002`→`spb isis bvlan 4001 ect-id 1`（每 BVLAN 全网同 ECT）→`spb isis control-bvlan 4001`→`spb isis interface port 1/1-3`→`spb isis admin-state enable`。 <<<PAGE 245>>>
- **C16** SPB 服务三步：`service access port 1/12`→`service 1 spb isid 500 bvlan 4001 admin-state enable`→`service 1 sap port 1/12:10 admin-state enable`（`:10` 匹配 CVLAN10、`:0` untagged、`:all` 全部 tagged）。验证：show isis/spb service 系列。 <<<PAGE 245>>>
- **C17** SPB 伪线（E-LINE）与 RFP：配置两端 SAP+伪线服务，再配 remote fault propagation 把远端故障传播到接入口（章 Configuring an SPB Pseudo-Wire Service / RFP 节）。 <<<PAGE 269>>>（7-68 页）
- **C18** IP over SPB（inline routing L3 VPN）：在服务上建基于服务的 IP 接口或用前面板口+外部环回，两 VRF 场景见章内 IPv4/IPv6 Inter-ISID 例。 <<<PAGE 280>>>（7-79 页）
## 环网（Ch8/12/13）
- **C19** LBD 使能：全局 enable→边缘口 enable→（可选）remote-origin enable→配 transmission timer（默认 30s）→违规口 autorecovery 定时器；验证 `show loopback-detection` 系列（章 Configuring LBD）。 <<<PAGE 329>>>（8-8 页）
- **C20** ERP 标准 VLAN 环：`vlan 1001`+`vlan 1001 members port 1/1/1-2 tagged`→`erp-ring 1 port1 1/1/1 port2 1/1/2 service-vlan 1001 level 1`→`erp-ring 1 rpl-node port 1/1/1`→加保护 VLAN 11-20→`erp-ring 1 enable`→`show erp`。 <<<PAGE 403>>>
- **C21** ERP+VLAN Stacking：`ethernet-service svlan 1001`→`ethernet-service service-name CustomerA svlan 1001`→`ethernet-service nni port 1/1/1(2)`→`ethernet-service svlan 1001 nni port ...`→`erp-ring 1 ... level 5`→rpl-node→`erp-ring 1 enable`。 <<<PAGE 403>>>
- **C22** ERPv2 主环+子环+共享链路：主环节点、子环节点、interconnection 节点分别配置，secondary RPL node 配置见章内（Sample ERPv2 Ring Configuration）。 <<<PAGE 419>>>（12-23 页）
- **C23** MRP 环：配 MRM（含测试帧周期）与 MRC 角色、冗余域；MRA 自动选举替代手工指定（章 Configuring an MRP Ring）。 <<<PAGE 437>>>（13-12 页）
## 聚合/DHL/MVRP（Ch9-11/14）
- **C24** 静态聚合：`linkagg static agg <id> size n`→`linkagg static port agg <id> port <slot/port>`（两端都要）。验证：show linkagg。 <<<PAGE 342>>>（9-7 页）
- **C25** 动态 LACP 聚合：建动态组→成员口 actor 参数（LACP 模式/slow-fast 超时等）→partner 参数（章 Configuring Dynamic Link Aggregate Groups）。验证：show linkagg dynamic。 <<<PAGE 354>>>（10-7 页）
- **C26** DHL Active-Active 九步：`vlan 100-110`→两链路同默认 VLAN（`vlan 100 members port 1/1/10 untagged`）→其余 VLAN tagged→`dhl 10`→`dhl 10 pre-emption-time 500`→`dhl 10 mac-flushing mvrp`→`dhl 10 linka linkagg 5 linkb port 1/1/10`→`dhl 10 vlan-map linkb 11-20`→`dhl 10 admin-state enable`。 <<<PAGE 383>>>
## MPLS/L2VPN/VXLAN/EVPN（Ch15-18）
- **C28** MPLS+LDP 快配：`mpls enable`→载入 LDP 软件→`ldp enable`→全局定时器→接口使能 LDP→（可选）GR/session protection/MD5 认证。验证：show mpls/ldp。 <<<PAGE 453>>>（15-3 页）
- **C30** VPWS(LDP)：同 VPLS 流程但点到点，两端各一 SAP+SDP 绑定。验证：show vpws。 <<<PAGE 505>>>（16-37 页）
- **C31** VXLAN 网关：Loopback0 IP（VTEP 标识）→建 VXLAN service(VNI)→配 SAP→配 SDP→服务绑定 SDP→（可选）改 UDP 端口。验证：show vxlan service/sdp。 <<<PAGE 536>>>（17-18 页）
- **C32** EVPN on VXLAN：底层 BGP(EVPN 地址族)+Loopback0→使能服务 EVPN→access 口 ES 操作→SAP→（对称 IRB）fabric-vpn 服务+路由重分发；RR 与两 Clos 层建议见章内部署模型。验证：show evpn 系列。 <<<PAGE 596>>>（18-15 页）
- **C33** EVPN 多站（Multi-site）：边界节点 manual RT 配置+DCI 互联需求（章 Multi-site Sample Topology / Manual RT Configuration）。 <<<PAGE 612>>>（18-87 页）
- **C34** IP 转发快配：建 VLAN→加端口→`ip interface vlan-20 address 171.11.1.1 vlan 20`→静态/默认/黑洞路由。 <<<PAGE 709>>>
- **C35** VRF 部署：`vrf <name>`→VRF profile→IP 接口划入 VRF→VRF 内路由协议实例；Management VRF 需注意管理应用联动。验证：show vrf。 <<<PAGE 756>>>（22-2 页）
- **C36** VRF Route Leak：`ip route ... next-hop vrf` 类配置跨 VRF 泄露前缀（章 Quick Steps for Configuring VRF Route Leak）。 <<<PAGE 712>>>（21-44 页）
- **C38** IPsec AH 策略：`ipsec` master key→policy（AH/HMAC-SHA1）→SA→绑定接口/流（章 Quick Steps for Configuring an IPsec AH Policy）。 <<<PAGE 819>>>（24-3 页）
- **C40** RIP：载入→`ip rip` 全局/接口使能→定时器调优→重分发→认证（RIPv2 可 SHA256）。验证：show ip rip。 <<<PAGE 842>>>（25-6 页）
- **C41** BFD：配会话参数（传输/接收间隔、检测倍数）→宿主协议（OSPF/BGP/VRRP/静态）挂 BFD。验证：show bfd。 <<<PAGE 869>>>（26-15 页）
## DHCP（Ch27-28）
- **C42** DHCP Relay 六步：`ip dhcp relay admin-state enable`→`ip dhcp relay destination 128.100.16.1`→（可选）`ip dhcp relay per-interface-mode`→`ip dhcp relay interface ipv4-v200 destination 128.100.16.1`→`ip dhcp relay forward-delay 30`+`ip dhcp relay maximum-hops 10`→`ip dhcp relay insert-agent-information`。验证：`show ip dhcp relay interface`。 <<<PAGE 902>>>
- **C44** 内部 DHCP Server：写 policy file+dhcpd 配置文件→数据库文件路径→使能（章 Quick Steps to Configure Internal DHCP Server）。验证：show dhcp server。 <<<PAGE 893>>>（28-2 页）
- **C45** DHCPv6 Relay/Snooping/RA Guard：使能 relay 服务→relay 接口→max hops；snooping 绑定表+ISF 源过滤；RA guard 端口策略（章 DHCPv6 各节）。 <<<PAGE 917>>>（27-35 页）
## VRRP/SLB/组播（Ch29-32）
- **C46** VRRP 虚拟路由器：`ip vrrp 23 interface ipv4-100`→`ip vrrp 23 interface ipv4-100 address 192.168.173.1`→对端同样两步→`ip vrrp 23 interface ipv4-100 admin-state enable`（IPv4 须先配地址才能使能）。验证：`show ip vrrp`/`show ipv6 vrrp`。 <<<PAGE 978>>>
- **C47** VRRP tracking：建 tracking policy（监控 IP 可达/BFD）→关联到虚拟路由器（章 Creating VRRP Tracking Policies）。 <<<PAGE 993>>>（29-24 页）
- **C48** SLB 集群：使能 SLB→`slb cluster <id> vip <ip> name ...`→`slb cluster <id> server <ip> weight n`→ping 周期/超时/重试→上下线 cluster/server→（可选）probe 探测关联。验证：show slb。 <<<PAGE 1011>>>（30-10 页）
- **C49** IPMS：全局使能→IGMP 版本/静态 querier/静态组→query interval/robustness 等参数→（IPMSv6 对应 MLD 系列）。验证：show ipms / ipmsv6。 <<<PAGE 1038>>>（31-10 页）
- **C50** IPMVLAN（MVR）：`ipmvlan <id>` 使能→分配 IPv4/IPv6 地址→sender 口（NNI，仅 1 个）→receiver 口/CVLAN 关联→静态 IGMP 组。验证：show ipmvlan。 <<<PAGE 1093>>>（32-10 页）
## QoS（Ch33）
- **C52** 条件组：network group/service group/MAC group/port group 建好后挂到单个 condition，免逐地址建条件；map group 做标记映射。验证：show policy group/map。 <<<PAGE 1176>>>（33-59 页）
- **C53** ACL 安全策略：L2/L3/IPv6 ACL 条件+drop/accept 动作入 policy rule，`qos apply` 生效（章 Using Access Control Lists）。 <<<PAGE 1142>>>（33-69 页）
- **C54** 端口限速/整形与 tri-color：policy 带宽 policing（sr/tcm 三色）+端口 bandwidth policing（章 Configuring Policy/Port Bandwidth Policing）。 <<<PAGE 1118>>>（33-28 页）
## AG/UNP（Ch35）
- **C55** Access Guardian 十二步快配：RADIUS 服务器定义（`aaa radius-server rad1_mac host 10.135.60.44 hash-key secret ...`）→`aaa device-authentication mac rad1_mac`→`aaa mac session-timeout enable`→`unp profile na_employee`→`unp profile na_employee qos-policy-list naEmpList`→默认 profile `unp profile def_unp`→`unp profile map na_employee vlan 100`→分类规则 `unp classification mac-range ... profile1 na_employee`→`unp port 1/1/20 port-type bridge`→`unp port 1/1/1 mac-authentication`→`unp port 1/1/1 classification`→端口默认 profile。验证：show unp 系列。 <<<PAGE 1210>>>
- **C56** Captive Portal：操作模式→配置 profile→替换证书→自定义 web 页→认证流程（章 Quick Steps for Configuring Captive Portal Authentication）。 <<<PAGE 1303>>>（35-103 页）
- **C57** L2 GRE 隧道（BYOD/AP 流量）：tunnel access switch 与 tunnel aggregation switch 两侧配置+外部环回 SAP+SDP 绑定（章 Quick Steps for Configuring L2 GRE Tunneling）。 <<<PAGE 1353>>>（35-133 页）
- **C58** mDNS/SSDP 零配置（BYOD）：使能 mDNS/SSDP relay→VLAN/service 域配置→（可选）filtering 规则（章 Quick Steps for Zero Configuration mDNS and SSDP）。 <<<PAGE 1400>>>（35-190 页）
## 诊断/运维（Ch39-48）
- **C59** 端口镜像：`port-mirroring 6 source 1/2/3-9 destination 1/2/10 unblocked-vlan 7`。验证：`show port-mirroring status 6`。 <<<PAGE 1558>>>
- **C60** sFlow 三段：`sflow receiver 1 name Golden address 198.206.181.3`→`sflow sampler 1 port 2/1/1-5 receiver 1 rate 2048 sample-hdr-size 128`→`sflow poller 1 port 1/2/6-10 receiver 1 interval 30`。验证：`show sflow receiver`。 <<<PAGE 1561>>>
- **C61** VLAN Stacking 服务：`ethernet-service svlan <id>`→服务名关联→NNI 口→SAP/UNI 口封装→UNI profile（章 Quick Steps for Configuring VLAN Stacking）。 <<<PAGE 1622>>>（42-8 页）
- **C62** Service OAM：`cfm domain`→MA→MEP/虚拟 MEP→loopback/linktrace/帧时延测量（章 Quick Steps for Configuring Ethernet OAM）。 <<<PAGE 1650>>>（44-8 页）
- **C63** EFM LINK OAM：`efm-oam enable`→端口使能→errored-frame(-seconds-summary) 窗口/阈值/notify（样例 `efm-oam port 1/1/1 errored-frame window 32 threshold 10 notify enable`）→远端环回。验证：show efm-oam。 <<<PAGE 1672>>>
- **C64** PPPoE-IA：`pppoe-ia enable`→（可选）`pppoe-ia ignore-slot`（AOS6 格式 Circuit-ID）→`pppoe-ia port 1/1/1 enable`→trust/client 口→access-node-id/circuit-id/remote-id。验证：show pppoe-ia。 <<<PAGE 1715>>>

---
合计：64 条（C1-C64）。

## counter-examples

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
- **X55** 非信任口带 Option-82 的包默认丢弃（客户端侧私自插 82 的场景会断）。<<<PAGE 925>>>
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

## frameworks

- **F1** AOS 配置手册统一章法（Defaults→Quick Steps→Overview→Configuring→Example→Verifying）：所有功能章都按此骨架组织，排障与学习时可按固定小节定位；"Quick Steps" 与 "Application Example" 提供可复制流程，"Interaction With Other Features" 提示跨功能约束。<<<PAGE 1>>>（全书体例）
- **F2** 违规关停与恢复统一框架（Violation Recovery）：各特性（STP/QoS/LPS/UDLD/NetSec/NI/LLDP/LinkMon/LFP/RFP）共用一套 shutdown/recovery/trap 机制，分 Discard 与 Admin-Down 两类；排障先查 `show violation` 而非逐特性查。 <<<PAGE 69>>>
- **F3** 二层高可靠防环体系：STP/RSTP/MSTP（通用树）→ UDLD（单向链路）→ LBD（环回）→ ERP/MRP（电信/工业环网）→ DHL（双归）→ SPBM（ISIS 最短路径），按场景分层选型。<<<PAGE 157>>>/<<<PAGE 395>>>/<<<PAGE 211>>>
- **F4** SPBM 双平面框架：控制面 ISIS-SPB（ECT 对称最短路径树+控制面 MAC 学习）+ 数据面 802.1ah MAC-in-MAC（BEB 封装、BCB 按 BMAP 转发）；服务模型=BVLAN 承载多 I-SID，SAP 定义接入分类。 <<<PAGE 211>>>
- **F5** 服务模型三件套（SAP/SDP/Service）：SPB、VPLS、VPWS、VXLAN 共用"接入点 SAP+隧道分发点 SDP+服务实例"抽象，学会一次即可迁移到四种 VPN。 <<<PAGE 212>>>/<<<PAGE 478>>>/<<<PAGE 533>>>
- **F6** EVPN 控制面框架：MP-BGP EVPN 地址族（RT1-8 分工：AD/主机/含组播/ES/前缀/选择性组播）+ ES/ESI 多归属（DF 选举、别名、水平分割）+ VRF tenancy（非对称/对称 IRB、fabric-vpn、DAG、OISM）。 <<<PAGE 583>>>
- **F7** 数据中心叠加网络部署模型库：Clos-3/Collapsed Core/Clos-5/Multi-site/Multi-PoD，配 RR 冗余与 underlay 建议，形成可复用的拓扑-配置映射。 <<<PAGE 654>>>（18-76 页）
- **F8** QoS 四步处理链（分类→拥塞管理→拥塞避免→ policing/shaping）+ 策略三元组（condition/action/rule）+ 四类列表（default/UNP/egress/AFP）+ 条件组/map group/ACL 扩展。 <<<PAGE 1103>>>/<<<PAGE 1133>>>
- **F9** 网络准入框架（Access Guardian）：认证（802.1X/MAC/Captive Portal→RADIUS/UPAM/CPPM）→分类（UNP 规则/端口默认）→角色（profile：VLAN/service 映射+QoS 列表）→限制/隔离（QMR 隔离修复）；BYOD（mDNS/SSDP）与 IoT profiling 是外延。 <<<PAGE 1212>>>
- **F10** AAA 服务器选型矩阵：RADIUS（管理+准入）/TACACS+（管理含 SNMP）/LDAP（管理含 SNMP）+备份服务器策略+授权回落本地库。 <<<PAGE 1475>>>
- **F11** 应用感知框架：AppMon（DPI 签名+应用列表+QoS 执行）与 AFP（REGEX 指纹+分类器库+trap/UNP 列表）互补，前者面向 OVNG DPI 生态、后者面向服务器侧端口。 <<<PAGE 1431>>>/<<<PAGE 1457>>>
- **F12** DHCP 全栈框架：外部 relay（路由器）→内部 relay（global/per-interface、Option-82）→Generic UDP Relay→内部 DHCP Server（policy/配置/数据库文件）→Snooping（L2/L3、绑定表、信任口）→DHCPv6（relay/snooping/RA guard/ISF）。 <<<PAGE 903>>>/<<<PAGE 925>>>
- **F13** 组播分发框架：IPMS(IGMP)/IPMSv6(MLD) 做 VLAN/service 域内组播交换，PIM/DVMRP 做域间路由，IPMVLAN/MVR 做跨 VLAN 单向分发，EVPN RT6-8/OISM 做叠加层优化。 <<<PAGE 1032>>>/<<<PAGE 1086>>>
- **F14** OAM 分层框架：LINK OAM(802.3ah，单链路发现/监控/环回) 与 Service OAM(802.1ag/Y.1731，MD/MA/MEP 层级+CC/LB/LT+时延测量) 互补，CFM MD 分层 0-7 对应运营商/客户组织边界。 <<<PAGE 1655>>>
- **F15** 可观测性框架：端口镜像/端口监控（抓包面）+ sFlow（采样流量统计）+ RMON（探针）+ Switch Health（资源阈值）+ 日志/健康监测组合成完整诊断工具箱。 <<<PAGE 1558>>>/<<<PAGE 1561>>>
- **F16** 环网保护双体系：ERP(G.8032，RPL owner+WTR/Guard+R-APS) 面向电信以太，MRP(IEC 62439-2，MRM/MRC/MRA 投票+测试帧) 面向工业环；ERPv2 扩展多环/子环/共享链路。 <<<PAGE 395>>>/<<<PAGE 426>>>
- **F17** VLAN 演进框架：标准 VLAN→802.1Q trunk→PVLAN（子域隔离）→VLAN Stacking/QinQ（运营商隧道）→VXLAN/EVI（数据中心叠加）→EVPN（控制面化），按规模与隔离需求逐级选用。 <<<PAGE 115>>>/<<<PAGE 1606>>>/<<<PAGE 583>>>
- **F18** 安全接入纵深框架：端口级（LPS/端口安全/风暴控制/过滤 MAC）→链路级（MACsec）→网络级（IPsec/DoS 过滤/IPv6 DoS）→身份级（AG/UNP/Captive Portal/Quarantine）四层递进。 <<<PAGE 83>>>/<<<PAGE 1536>>>/<<<PAGE 819>>>/<<<PAGE 1212>>>

---
合计：18 条（F1-F18）。

## glossary

- **Autonegotiation（自协商）**：链路两端自动协商速率/双工/流控的机制，关闭后 auto 参数失效 <<<PAGE 56>>>
- **Crossover/MDI/MDIX**：直通/交叉线序模式；MDIX 为交换机侧标准，MDI 为终端侧标准 <<<PAGE 56>>>
- **Duplex Mode（双工模式）**：full/half/auto，全双工可同时收发 <<<PAGE 57>>>
- **Link Trap（链路 Trap）**：端口状态变化时向网管站发送的 SNMP 通告 <<<PAGE 57>>>
- **Port Alias（端口别名）**：单端口描述字符串，含空格需引号 <<<PAGE 58>>>
- **Max Frame Size（最大帧长）**：端口可转发最大字节数（如 9216 巨帧） <<<PAGE 58>>>
- **Flood Rate Limiting（泛洪限速/风暴控制）**：对 bcast/uucast/mcast 分别按 mbps/pps/百分比限速，超限丢包 <<<PAGE 59>>>
- **Low Threshold（低阈值自动恢复）**：违规速率回落后端口自动退出 STORM violated 状态 <<<PAGE 59>>>
- **EPP（增强端口性能）**：特定平台的端口性能优化开关 <<<PAGE 61>>>（1-8 页）
- **TDR（时域反射电缆诊断）**：发测试脉冲定位铜缆断点/长度/阻抗异常 <<<PAGE 66>>>（1-14 页）
- **Violation Recovery（违规恢复）**：特性关停端口的统一恢复机制（手动/定时/次数/wait-to-restore/trap） <<<PAGE 69>>>
- **Wait-to-Restore Timer**：端口恢复后延迟通知特性的稳定等待定时器 <<<PAGE 69>>>
- **Link Monitoring（链路监控）**：按窗口监测端口错误与翻动并可自动关停 <<<PAGE 74>>>（1-21 页）
- **LFP（链路故障传播）**：把远端/对侧故障传播到本地接口触发关停 <<<PAGE 78>>>（1-25 页）
- **MACsec（介质访问控制安全，802.1AE）**：以太链路点到点加密/认证/防重放 <<<PAGE 83>>>
- **SecTag**：MACsec 帧中 8/16 字节头，含解密密钥信息、包号、安全信道标识 <<<PAGE 83>>>
- **SCI（安全信道标识）**：标识单向发送/接收安全信道 <<<PAGE 83>>>
- **MKA（MACsec 密钥协商，802.1X-2010）**：协商生成并周期轮换 SAK 的协议 <<<PAGE 84>>>
- **CAK/CKN**：连通性关联密钥及其名称，PSK 或 EAP 派生，保护控制面 <<<PAGE 84>>>
- **Key Server（密钥服务器）**：MKA 选出的生成分发 SAK 的节点 <<<PAGE 84>>>
- **WAN MACsec**：面向广域链路的 MACsec 应用形态 <<<PAGE 87>>>（1-36 页）
- **UDLD（单向链路检测）**：二层协议检测光纤/铜缆单向链路并关停端口 <<<PAGE 98>>>
- **Normal/Aggressive Mode（UDLD 模式）**：正常模式仅显式证据关停；激进模式超时即关停（推荐仅点对点） <<<PAGE 98>>>
- **Echo Detection（回声检测）**：UDLD 学习到新邻居后的请求-回应验证窗口机制 <<<PAGE 99>>>
- **Source Learning（源学习）**：从数据帧源 MAC 构建 MAC 表 <<<PAGE 105>>>
- **Static MAC（静态 MAC）**：手工绑定端口+VLAN 的永久地址，bridging/filtering 两种行为 <<<PAGE 105>>>
- **Filtering MAC**：静态 MAC 的丢弃行为，用于阻断攻击 <<<PAGE 105>>>
- **MAC Aging Time（MAC 老化时间）**：动态表项老化周期 <<<PAGE 108>>>（3-7 页）
- **VLAN ID/VID**：802.1Q 唯一标识 VLAN 的编号 <<<PAGE 115>>>
- **VPA（VLAN 端口关联）**：端口与 VLAN 的成员关系记录 <<<PAGE 115>>>
- **Default VLAN（默认 VLAN）**：端口无 tag 流量归属的 VLAN，出厂全口在 VLAN 1 <<<PAGE 115>>>
- **802.1Q Tagging（打标/Trunking）**：4 字节标签携带 VID+优先级，单链多 VLAN <<<PAGE 118>>>
- **Tagged/Untagged Port**：按 VID 打标转发 / 无标转发的成员模式 <<<PAGE 118>>>
- **VLAN IP Interface（VLAN 路由接口）**：绑定 VLAN 的三层接口 <<<PAGE 121>>>（4-10 页）
- **PVLAN（私有 VLAN）**：主 VLAN+isolated/community 二级 VLAN 的子域隔离 <<<PAGE 128>>>
- **Promiscuous Port（混杂口）**：PVLAN 主 VLAN 的上联/互通口 <<<PAGE 128>>>
- **Isolated/Community VLAN（隔离/团体二级 VLAN）**：isolated 成员彼此隔离；community 成员互通 <<<PAGE 128>>>
- **ISL Port（PVLAN 互连口）**：跨交换机延伸 PVLAN 域的级联口 <<<PAGE 128>>>
- **HA VLAN（高可用 VLAN）**：把发往单 MAC 的流量复制到多端口的服务器集群 VLAN <<<PAGE 140>>>
- **Server Cluster（服务器集群）**：L2/L3 两种模式，多实例共享请求算法 <<<PAGE 140>>>
- **Virtual MAC（虚 MAC）**：集群对外的虚拟地址（如 00:95:2a:05:ff:4a 例） <<<PAGE 141>>>

## 生成树（Ch6）
- **Root Bridge（根桥）**：全网选举的树根，最低桥 ID 者当选 <<<PAGE 157>>>
- **Root Path Cost（根路径成本）**：到根最优路径端口成本之和 <<<PAGE 157>>>
- **Designated Bridge/Port（指定桥/指定口）**：为 LAN 提供到根最短路径的桥及其端口 <<<PAGE 158>>>
- **Root Port（根口）**：本桥到根成本最低的口，根桥无根口 <<<PAGE 158>>>
- **Alternate/Backup Port（替代/备份口）**：802.1w 区分的两种阻塞角色口 <<<PAGE 158>>>
- **BPDU（桥协议数据单元）**：承载桥 ID/根 ID/成本等拓扑计算信息的二层帧 <<<PAGE 159>>>（6-7 页）
- **Bridge Priority（桥优先级）**：与 MAC 合成桥 ID 决定根选举 <<<PAGE 161>>>（6-29 页）
- **Flat Mode（扁平模式）**：整交换机单棵树的 STP 运行模式 <<<PAGE 164>>>
- **Per-VLAN Mode（每 VLAN 模式）**：AOS 私有的每 VLAN 一棵树模式 <<<PAGE 164>>>
- **MSTI（多生成树实例）**：VLAN 集合映射到的独立树实例，Flat 模式下最多 16 个+CIST <<<PAGE 164>>>
- **MST Region（MST 区域）**：区域名+revision+VLAN 映射一致的交换机组，对外呈现单树 <<<PAGE 167>>>（6-16 页）
- **CST/CIST/IST（公共/公共内部/内部生成树）**：MSTP 的层级树概念 <<<PAGE 167>>>（6-17 页）
- **SPB/SPBM（最短路径桥ging/MAC 模式）**：IEEE 802.1aq，ISIS 驱动的最短路径以太网 <<<PAGE 211>>>
- **ISIS-SPB**：带 SPB TLV 扩展的 IS-IS 链路状态协议，建对称 SPT <<<PAGE 211>>>
- **PBB/PBBN（运营商骨干桥/网络，802.1ah）**：MAC-in-MAC 封装与骨干网 <<<PAGE 211>>>
- **BEB（骨干边缘桥）**：学习并封装客户帧的边缘节点 <<<PAGE 211>>>
- **BCB（骨干核心桥）**：只按 BMAC 转发不学客户 MAC 的核心节点 <<<PAGE 211>>>
- **BMAC（骨干 MAC）**：802.1ah 外层目的地址，指向目的 BEB <<<PAGE 212>>>
- **BVLAN（骨干 VLAN）**：SPB 传输 VLAN，不学 MAC 不泛洪 <<<PAGE 211>>>
- **Control BVLAN（控制 BVLAN）**：承载 ISIS-SPB 控制报文的指定 BVLAN <<<PAGE 245>>>
- **I-SID（服务实例标识）**：SPB 服务编号，绑定 BVLAN <<<PAGE 212>>>
- **ECT（等价树算法）**：16 个预定义算法在等价路径间打破平局 <<<PAGE 214>>>
- **SPT（最短路径树）**：每桥以自己为根计算的转发树 <<<PAGE 214>>>
- **IP over SPB / Inline Routing**：基于服务的 L3 VPN 接口形态 <<<PAGE 224>>>（7-19 页）
- **SPB over Shared Ethernet**：SPB 骨干跑在共享/其他网络之上的形态 <<<PAGE 229>>>（7-24 页）
- **SPB In-Band Management**：经 BVLAN 带内管理交换机 <<<PAGE 231>>>（7-26 页）

## 环网与保护（Ch8/12/13）
- **LBD（环回检测）**：周期探测帧检测 L2 环路并关停端口 <<<PAGE 325>>>
- **Remote-origin LBD（远端源环回检测）**：处理远端系统发来的 LBD 帧 <<<PAGE 326>>>
- **Transmission Timer（LBD 传输定时器）**：探测帧发送周期，默认 30 秒 <<<PAGE 325>>>
- **ERP（以太网环保护）**：ITU-T G.8032 环网保护切换 <<<PAGE 395>>>
- **RPL（环保护链路）**：环上被阻塞防环的链路 <<<PAGE 395>>>
- **RPL Owner（RPL 拥有者）**：阻塞/解阻塞 RPL 的指定节点 <<<PAGE 395>>>
- **R-APS（环自动保护切换消息）**：SF/NR/NR,RB 等环状态协议报文 <<<PAGE 395>>>
- **WTR Timer（等待恢复定时器）**：环恢复后延迟回切的分钟级定时器 <<<PAGE 396>>>
- **Guard Timer（守护定时器）**：丢弃过时 R-APS 的定时器，须大于绕环时延 <<<PAGE 396>>>
- **ERPv2**：支持多环/子环/共享链路/R-APS 虚信道的版本 <<<PAGE 395>>>
- **Sub-ring/Major Ring（子环/主环）**：ERPv2 的环层级 <<<PAGE 399>>>（12-17 页）
- **MRP（介质冗余协议）**：工业环网确定性重构协议 <<<PAGE 426>>>
- **MRM（介质冗余管理器）**：环上控制拓扑的节点，发 MRP_Test <<<PAGE 428>>>
- **MRC（介质冗余客户端）**：响应 MRM 重构帧、转发测试帧 <<<PAGE 428>>>
- **MRA（介质冗余自动管理器）**：可投票竞选 MRM 的角色 <<<PAGE 428>>>
- **Redundancy Domain（冗余域）**：MRP 环的域标识，每域两个环口 <<<PAGE 428>>>
- **Link Aggregation（链路聚合）**：多物理链路捆成虚拟链路 <<<PAGE 341>>>
- **Static/Dynamic Aggregate Group（静态/动态聚合组）**：手工/802.3ad LACP 协商两种 <<<PAGE 341>>>
- **Actor/Partner（本端/对端）**：LACP 两侧角色命名 <<<PAGE 352>>>
- **Linkagg ID**：聚合组编号，VLAN/MAC/QoS 配置的挂载单位 <<<PAGE 341>>>
- **DHL（双归链路）**：Active-Active/Active-Standby 两种双上联保护 <<<PAGE 380>>>（11-3 页）
- **Pre-emption Time（DHL 抢占时间）**：主链恢复后回切等待，默认 30 秒 <<<PAGE 383>>>
- **MAC Flushing（MAC 冲刷）**：DHL 切换时清 MAC 的方式（raw/mvrp） <<<PAGE 382>>>

## MVRP（Ch14）
- **MVRP（多 VLAN 注册协议，802.1ak/MRP 应用）**：动态声明/撤销 VLAN 成员 <<<PAGE 442>>>
- **Dynamic VLAN（动态 VLAN）**：由 MVRP 注册学到的 VLAN <<<PAGE 442>>>
- **Applicant Mode（申请者模式）**：端口声明 VLAN 的姿态（normal/active 等） <<<PAGE 446>>>（14-9 页）
- **Registrar Mode（注册者模式）**：端口处理声明的方式（fixed/forbidden/normal） <<<PAGE 446>>>（14-8 页）
- **Leave Timer/Join Timer**：MVRP 注册/注销定时器 <<<PAGE 447>>>（14-10 页）

## MPLS/L2VPN（Ch15-16）
- **MPLS（多协议标签交换）**：32 位标签头逐跳交换的转发技术 <<<PAGE 457>>>
- **Label Stack（标签栈）**：报文可携带多层标签，处理只看栈顶 <<<PAGE 457>>>
- **LSR（标签交换路由器）**：核心按标签转发的路由器 <<<PAGE 457>>>
- **LER（标签边缘路由器）**：压入/弹出标签的边缘节点 <<<PAGE 458>>>
- **LSP（标签交换路径）**：单向的标签隧道，双工需两条 <<<PAGE 457>>>
- **FEC（转发等价类）**：同一 LSP 承载的等价流分组 <<<PAGE 458>>>
- **LDP（标签分发协议）**：UDP hello+TCP 会话分发 FEC-标签绑定 <<<PAGE 458>>>
- **Hello Adjacency（LDP Hello 邻接）**：hello 建立的邻居关系 <<<PAGE 458>>>
- **Targeted Peer（定向对端）**：扩展发现机制找到的非直连 LSR <<<PAGE 458>>>
- **LDP Graceful Restart（LDP 平滑重启）**：CMM 冗余下会话不中断的机制 <<<PAGE 461>>>（15-11 页）
- **VPLS（虚拟专用 LAN 服务）**：多点任意互通 L2VPN <<<PAGE 478>>>
- **VPWS（虚拟专用线服务）**：点到点 L2VPN <<<PAGE 478>>>
- **PW（伪线）**：PE 间的仿真链路，VPLS 需全网格 <<<PAGE 478>>>
- **Attachment Circuit（接入电路）**：CE-PE 间的物理/逻辑链路 <<<PAGE 478>>>
- **Split Horizon（水平分割，PW）**：PW 收到的包不再从 PW 发出 <<<PAGE 478>>>
- **BGP VPLS Auto-discovery**：BGP 自动发现 VPLS 成员免去手工配置 <<<PAGE 480>>>
- **Route Reflector（路由反射器）**：减少 BGP full-mesh 的集中反射节点 <<<PAGE 480>>>

## VXLAN/EVPN（Ch17-18）
- **VXLAN（虚拟可扩展 LAN）**：MAC-in-UDP/IP 叠加网络封装 <<<PAGE 533>>>
- **VNI（VXLAN 网络标识）**：24 位段 ID <<<PAGE 533>>>
- **VTI（VXLAN 隧道接口）**：由 SDP+绑定提供的 UDP 隧道 <<<PAGE 533>>>
- **VTEP（VXLAN 隧道端点）**：封装/解封点，AOS 用 Loopback0 IP 标识 <<<PAGE 533>>>
- **VXLAN Gateway（VXLAN 网关）**：桥接 VXLAN 与传统 VLAN 域的设备 <<<PAGE 533>>>
- **UDP 4789**：VXLAN 默认目的端口（可配） <<<PAGE 535>>>
- **EVPN（以太网 VPN）**：BGP MP-BGP 扩展通告 MAC/IP 可达性 <<<PAGE 583>>>
- **EVI（EVPN 实例）**：跨 PE 的转发/路由实例，含 RD/RT <<<PAGE 583>>>
- **RT-1/2/3/4/5/6/7/8（EVPN 路由类型）**：AD、主机、含组播、ES、前缀、选择性组播、成员报告/离开同步 <<<PAGE 584>>>
- **All-Active Multihoming（全活多归属）**：多 PE 同时转发的冗余模型 <<<PAGE 583>>>
- **MAC Mobility（MAC 移动性）**：主机迁移的序列号仲裁机制 <<<PAGE 606>>>（18-36 页）
- **BUM Traffic（广播/未知单播/组播）**：需要泛洪处理的流量类别 <<<PAGE 583>>>
- **Ingress Replication（入向复制）**：以单播复制替代组播的 BUM 分发 <<<PAGE 584>>>
- **Multi-site/Multi-PoD**：跨数据中心/多 PoD 的 EVPN 部署模型 <<<PAGE 661>>>（18-83 页）

## 二层发现与语音（Ch19-20）
- **IP Interface（IP 接口）**：绑定 VLAN 的三层接口 <<<PAGE 709>>>
- **Router ID（路由器 ID）**：路由协议标识 <<<PAGE 711>>>（21-20 页）
- **GRE（通用路由封装）**：IP over IP 隧道封装 <<<PAGE 721>>>（21-40 页）
- **VRF（虚拟路由转发）**：同机多路由实例隔离 L3 <<<PAGE 756>>>
- **VRF Profile**：VRF 属性模板 <<<PAGE 758>>>（22-7 页）
- **Management VRF（管理 VRF）**：承载管理流量的专用 VRF <<<PAGE 759>>>（22-8 页）
- **IPv6 Link-local Address**：FE80::/10 链路内地址 <<<PAGE 774>>>
- **Unique Local IPv6 Unicast**：FC00::/7 站点本地可路由地址 <<<PAGE 774>>>
- **Anycast**：送达组内最近一员的地址 <<<PAGE 774>>>
- **ND（邻居发现）**：IPv6 的 ARP/RA/重复检测等机制 <<<PAGE 773>>>
- **RA Filtering（路由通告过滤）**：过滤恶意/多余 RA <<<PAGE 777>>>（23-13 页）
- **JITC Mode**：美军兼容模式，禁 Site-Local 地址 <<<PAGE 774>>>

## IPsec/RIP/BFD（Ch24-26）
- **IPsec**：网络层安全服务体系 <<<PAGE 819>>>
- **ESP（封装安全载荷）**：协议号 50，加密+可选认证 <<<PAGE 820>>>
- **AH（认证头）**：只认证不加密 <<<PAGE 820>>>
- **Transport Mode（传输模式）**：AOS 唯一支持的模式 <<<PAGE 819>>>
- **SPI（安全参数索引）**：32 位 SA 选择符 <<<PAGE 820>>>
- **SA（安全关联）**：SPI+目的地址+协议确定的单向策略实例 <<<PAGE 820>>>
- **HMAC-MD5/HMAC-SHA1**：认证散列算法 <<<PAGE 821>>>（24-7 页）
- **Master Key（IPsec 主密钥）**：SA 密钥体系的根 <<<PAGE 823>>>（24-10 页）
- **RIP（路由信息协议）**：距离向量 IGP，跳数度量 <<<PAGE 842>>>
- **Hold-down Timer（RIP 抑制定时器）**：路由失效前的怀疑期 <<<PAGE 842>>>
- **SHA256 Authentication（RIPv2）**：强认证选项 <<<PAGE 844>>>（25-18 页）
- **BFD（双向转发检测）**：毫秒级转发面故障检测 <<<PAGE 869>>>
- **Asynchronous Mode/Echo Function（BFD 模式）**：控制包/回声两种检测 <<<PAGE 870>>>
- **Detect Time Multiplier**：检测倍数，超时=倍数×最小接收间隔 <<<PAGE 869>>>
- **DHCP Relay（DHCP 中继）**：跨网段转发 DHCP 的代理，UDP 67/68 <<<PAGE 903>>>
- **Forward Delay/Maximum Hops**：中继转发时延与跳数上限校验 <<<PAGE 903>>>
- **Per-interface Mode（按接口中继模式）**：每个 IP 接口独立中继配置 <<<PAGE 903>>>
- **Generic UDP Relay（通用 UDP 中继）**：按端口转 UDP 到 VLAN/service/IP <<<PAGE 904>>>
- **Circuit ID/Remote ID**：Option-82 的两个子选项 <<<PAGE 926>>>
- **DHCP Snooping（DHCP 窥探）**：过滤非法 DHCP 报文并建绑定表 <<<PAGE 925>>>
- **Trusted Port（信任口）**：允许服务器报文的口 <<<PAGE 925>>>
- **Binding Table（绑定表）**：MAC-IP-端口-租期绑定数据库 <<<PAGE 926>>>
- **ISF（IPv6 源过滤）**：按绑定表校验源地址 <<<PAGE 921>>>（27-41 页）
- **VRRP（虚拟路由器冗余协议）**：默认网关冗余 <<<PAGE 979>>>
- **VRID（虚拟路由器 ID）**：虚拟路由器编号 <<<PAGE 979>>>
- **Virtual Router Master/Backup（主/备虚拟路由器）**：转发者与候补 <<<PAGE 979>>>
- **IP Address Owner（IP 地址拥有者）**：虚拟 IP 即其接口 IP 的路由器，必为 master <<<PAGE 980>>>
- **VRRP Advertisement（VRRP 通告）**：master 发往 224.0.0.18 的组播 <<<PAGE 980>>>
- **Skew Time**：(256-优先级)/256，防同时抢主的退避 <<<PAGE 980>>>
- **Preemption（抢占）**：高优先级 backup 抢占 master <<<PAGE 980>>>
- **Accept Mode（接受模式）**：backup 是否响应虚拟 IP 流量 <<<PAGE 987>>>（29-17 页）
- **VRRP Tracking（VRRP 跟踪）**：监控对象降优先级的策略 <<<PAGE 993>>>（29-24 页）
- **Condition Cluster（条件集群）**：以 QoS 条件标识的集群 <<<PAGE 1012>>>
- **Server Health Monitoring（服务器健康监测）**：ping 探测集群成员活性 <<<PAGE 1015>>>（30-9 页）
- **IPMS（IP 组播交换）**：IGMP 驱动的二层组播 <<<PAGE 1032>>>
- **Multicast Group Address（组播组地址）**：D 类 224/4，239/8 管理域 <<<PAGE 1032>>>
- **IGMP Querier（IGMP 查询者）**：定期查询成员的设备，最低 IP 当选 <<<PAGE 1033>>>
- **IGMP Version 1/2/3**：组成员管理协议版本 <<<PAGE 1036>>>（31-13 页）
- **DVMRP（距离向量组播路由协议）**：另一种组播路由协议 <<<PAGE 1033>>>
- **IPMSR（IP 组播交换与路由）**：IPMS+组播路由的组合 <<<PAGE 1033>>>
- **IPMVLAN（IP 组播 VLAN）**：专用组播分发 VLAN <<<PAGE 1086>>>
- **MVR（组播 VLAN 注册）**：多用户 VLAN 共享单一组播 VLAN <<<PAGE 1086>>>
- **Sender/Receiver Port（发送/接收口）**：IPMVLAN 的源口（NNI，唯一）与收听口 <<<PAGE 1087>>>
- **Enterprise/VLAN Stacking Mode（IPMVLAN 模式）**：面向普通口/QinQ 口两种模式 <<<PAGE 1086>>>

## QoS（Ch33）
- **Classification（分类）**：识别流并指派 CoS <<<PAGE 1105>>>
- **802.1p Priority**：以太标签 TCI 中的 3 位优先级 <<<PAGE 1105>>>
- **Trusted Port（QoS 信任口）**：采信报文已有标记的口 <<<PAGE 1108>>>（33-9 页）
- **Queue Set/QSet Profile（队列集/模板）**：每口队列调度参数组 <<<PAGE 1114>>>（33-11/13 页）
- **Lossless TC（无损流量类）**：PFC 支撑的不丢类 <<<PAGE 1120>>>（33-20 页）
- **PFC（基于优先级的流控）**：按优先级暂停的无损机制 <<<PAGE 1120>>>（33-20 页）
- **Tri-Color Marking（三色标记）**：sr/tcm 双速/单速三色限速 <<<PAGE 1125>>>（33-25 页）
- **Policy List（策略列表）**：default/UNP/egress/AFP 四类规则组 <<<PAGE 1134>>>
- **qos apply**：策略生效的提交命令 <<<PAGE 1147>>>
- **Condition Group（条件组）**：network/service/MAC/port group 地址组 <<<PAGE 1169>>>（33-59 页）
- **PolicyView**：ALE 的策略管理应用 <<<PAGE 1133>>>
- **Access Guardian（准入卫士）**：认证+合规+访问控制框架 <<<PAGE 1212>>>
- **UNP Classification Rules（UNP 分类规则）**：MAC 范围/IP/端口等无认证分类 <<<PAGE 1211>>>
- **UNP Port Type（bridge/access）**：VLAN 域或 service 域接入形态 <<<PAGE 1211>>>
- **MAC Authentication（MAC 认证）**：以 MAC 作用户名密码的认证 <<<PAGE 1213>>>
- **Application Signature Kit（应用签名包）**：应用特征库文件 <<<PAGE 1431>>>
- **Threat-Insight**：AppMon 内的威胁监控/强制 <<<PAGE 1449>>>（36-22 页）
- **AFP（应用指纹识别）**：REGEX 签名识别应用 <<<PAGE 1457>>>
- **REGEX Signature File**：/flash/app-signature/app-regex.txt <<<PAGE 1457>>>
- **AFP Mode（AFP 模式）**：端口级采样识别模式 <<<PAGE 1458>>>（37-6 页）
- **AAA Server（认证授权计费服务器）**：RADIUS/TACACS+/LDAP <<<PAGE 1475>>>
- **RADIUS**：最通用 AAA 协议，唯一支持端口准入 <<<PAGE 1475>>>
- **TACACS+**：含 SNMP 管理访问的 AAA 协议 <<<PAGE 1475>>>
- **RADIUS over TLS/RADSEC**：加密 RADIUS 传输 <<<PAGE 1488>>>（38-18 页）
- **RADIUS Health Check**：服务器活性探测 <<<PAGE 1488>>>（38-18 页）
- **Kerberos Snooping**：监听 Kerberos 票据识别用户 <<<PAGE 1525>>>（38-50 页）
- **LPS Learning Window（LPS 学习窗口）**：全局学习时限 <<<PAGE 1536>>>
- **Packet Relay（包中继）**：LPS 口上中继违规报文 <<<PAGE 1542>>>（40-21 页）
- **Port Mirroring（端口镜像）**：复制流量到分析口 <<<PAGE 1558>>>
- **Unblocked VLAN（镜像豁免 VLAN）**：防 STP 阻断镜像会话 <<<PAGE 1558>>>
- **Port Monitoring（端口监控）**：落盘抓包会话 <<<PAGE 1559>>>
- **RMON（远程监控）**：SNMP 探针统计 <<<PAGE 1567>>>（41-11 页）
- **Switch Health（交换机健康）**：资源阈值与采样监控 <<<PAGE 1566>>>
- **VLAN Stacking/QinQ**：外层 SVLAN 隧道客户流量 <<<PAGE 1606>>>
- **Double Tagging/VLAN Translation**：双打标/标签替换两种 QinQ 封装法 <<<PAGE 1608>>>
- **Ethernet Service OAM/CFM（802.1ag/Y.1731）**：端到端业务运维体系 <<<PAGE 1655>>>
- **MD Level（维护域级别 0-7）**：运营商 0-2、提供商 3-4、客户 5-7 <<<PAGE 1655>>>
- **EVC（以太网虚连接）**：卖给客户的服务实例（UNI+VLAN） <<<PAGE 1655>>>
- **Frame Delay Measurement（帧时延测量）**：Y.1731 性能测量 <<<PAGE 1665>>>（44-13 页）
- **Virtual MEP（虚拟 MEP）**：虚拟端口上的 UP MEP <<<PAGE 1655>>>
- **EFM LINK OAM（802.3ah）**：单链路运维协议 <<<PAGE 1673>>>
- **OAMPDU**：LINK OAM 慢协议报文 <<<PAGE 1673>>>
- **Remote Loopback（远端环回）**：对端环回测试定位故障 <<<PAGE 1673>>>
- **Errored Frame/Frame Seconds Summary**：链路监控的三类错误窗口 <<<PAGE 1673>>>
- **CPE Test Head（CPE 测试头）**：L2 SAA 性能测试框架 <<<PAGE 1690>>>（46-5 页）
- **CPE Test Group（CPE 测试组）**：批量测试调度 <<<PAGE 1710>>>（46-13 页）
- **PPPoE-IA（PPPoE 中间代理）**：插入线路标识 VSA 的接入代理 <<<PAGE 1714>>>
- **Access Node/Access Loop（接入节点/接入环）**：IA 所在交换机与用户物理线路 <<<PAGE 1714>>>
- **Circuit ID/Remote ID**：PPPoE-IA 插入的线路/远端标识 <<<PAGE 1715>>>

## principles

## 以太网端口与链路（Ch1）
- **P1** 端口自协商关闭后 auto MDIX/auto speed/auto duplex 失效："If autonegotiation is disabled, auto MDIX, auto speed, and auto duplex are not accepted." <<<PAGE 56>>>
- **P2** MDIX 是集线器/交换器侧标准，MDI 是终端侧标准："Setting crossover configuration to mdix configures the interface ... which is the standard for hubs and switches." <<<PAGE 56>>>
- **P3** `clear interfaces ... l2-statistics cli` 只清 CLI 计数、SNMP 累计值保留："only those statistics that are maintained by the switch CLI are cleared; SNMP values are not cleared." <<<PAGE 57>>>
- **P4** DDM 通过读取光模块 EEPROM 监控温度/电压/电流/光功率五项指标，阈值分 Warning/Alarm 高低四档："Digital Diagnostics Monitoring allows the switch to monitor the status of a transceiver by reading the information contained on the transceiver's EEPROM." <<<PAGE 58>>>
- **P5** 风暴控制按 bcast/uucast/mcast 三类分别限速，超阈值即丢包："When the threshold value is reached, packets are dropped." <<<PAGE 59>>>
- **P6** 风暴低阈值自动解除机制：违规速率降到 low-threshold 以下时端口自动退出 STORM violated 状态："When the rate of violating traffic received on the port goes below the low threshold value, the port is removed from the violating state." <<<PAGE 59>>>
- **P7** 全双工 PAUSE 流控与自协商的从属关系："if autonegotiation and flow control are both enabled for an interface, then autonegotiation determines how the interface processes PAUSE frames." <<<PAGE 60>>>
- **P8** 违规恢复体系=手动 clear violation+自动恢复定时器+最大恢复次数+wait-to-restore+SNMP trap 五件套："The OmniSwitch allows features to shutdown an interface when a violation occurs on that interface." <<<PAGE 69>>>
- **P9** 两种关断方式（Filtering 保链路灯/Administratively 灭灯）恢复路径不同："Disconnecting/reconnecting the interface link or a link down/up event will not recover a port that was administratively disabled." <<<PAGE 69>>>
- **P10** 永久关断状态只能用 clear violation（或 interfaces reset）恢复："An interface is already in a permanent shutdown state. In this case, the only method for recovery is to use the clear violation command." <<<PAGE 70>>>
- **P11** 使用违规恢复机制的特性清单：STP/QoS/LPS/UDLD/NetSec/NI/LLDP/LinkMon/LFP/RFP，各有 Discard 或 Admin-Down 类型。<<<PAGE 70>>>
- **P12** 违规自动恢复默认 300 秒，且不支持聚合口只支持成员口："The interface violation recovery mechanism is not supported on link aggregates, but is supported on the link aggregate member ports." <<<PAGE 71>>>
- **P13** MACsec 提供 IEEE 802.1 点到点链路安全，防 DoS/中间人/重放/窃听："MACsec (MAC Security) provides point-to-point security on Ethernet links between directly connected nodes." <<<PAGE 83>>>
- **P14** MACsec 帧结构：EtherType 0x88E5 + 8/16 字节 SecTag + 可选加密载荷 + GCM-AES 16 字节 ICV："a MACsec packet starts with an Ethernet header with etherType 0x88E5, followed by an 8-byte or 16-byte SecTag header." <<<PAGE 83>>>
- **P15** 安全信道（SC）单向、以 SCI 标识；收发两端需配对匹配 SCI-Tx/SCI-Rx："A single secure channel is unidirectional." <<<PAGE 83>>>
- **P16** SA 内含 SAK 与包号（PN），接收侧用 PN 做重放保护："the packet number from the SecTag header will be checked against the packet number locally stored ... to perform replay protection." <<<PAGE 83>>>
- **P17** 默认加密套件 128-bit AES-GCM；SAK 会话密钥由 MKA 协议（802.1X-2010 扩展）协商："The MKA ... is an extension to 802.1X, which provides the required session keys." <<<PAGE 84>>>
- **P18** 动态 SAK(PSK) 模式：CAK 保护控制面、随机 SAK 保护数据面，key server 由协商选出并周期换钥："The MKA protocol selects one of the nodes as the key server, which creates a dynamic SAK and shares it with the node at the other end." <<<PAGE 84>>>
- **P19** 动态 CAK(EAP) 模式：802.1X 认证成功后由 RADIUS 下发 MSK，CAK/CKN 从 MSK+Session-Id 派生，必须用 EAP-TLS 双向认证："802.1x-authentication using EAP-TLS must be used as mutual authentication protocol for MACsec Dynamic mode." <<<PAGE 85>>>
- **P20** switch-to-host 场景交换机永远是 key server，客户端只能单 MKA 实体："The client is never a key server and can only interact with a single MKA entity." <<<PAGE 85>>>
## UDLD（Ch2）
- **P21** UDLD 是二层协议，检测光纤/铜缆单向链路并 admin-shutdown 受影响端口，防止 STP 环路："Unidirectional links can create hazardous situations such as Spanning-Tree topology loops." <<<PAGE 98>>>
- **P22** Normal 模式只依赖显式信息，未确定时标记 Undetermined 不关端口；Aggressive 模式定时器超时即关端："the lack of information is not always due to a defective link, this mode is optional and is recommended only for point-to-point links." <<<PAGE 98>>>
- **P23** UDLD 两大机制：邻居数据库（Hello/探测缓存老化）与回声检测（echo detection 窗口内无回应则按模式处置）。<<<PAGE 99>>>
- **P24** 缓存同步：端口禁用/UDLD 关闭/重启时清缓存并通知邻居 flush，实现缓存同步。<<<PAGE 99>>>
## 源地址学习/MAC（Ch3）
- **P25** MAC 表条目只有两种来源：动态学习与静态配置："New MAC address table entries are created in one of two ways: they are dynamically learned or statically assigned." <<<PAGE 105>>>
- **P26** 静态 MAC 适用沉默设备（silent devices），保证流量定向转发："These types of devices do not send packets, so their source MAC address is never learned." <<<PAGE 105>>>
- **P27** 静态 MAC 两种行为：bridging（默认）与 filtering（丢弃以阻断攻击）。<<<PAGE 105>>>
- **P28** 静态 MAC 永久有效，重启与老化均不删除："a static MAC address remains in use even if the MAC ages out or the switch is rebooted." <<<PAGE 105>>>
- **P29** 聚合口上的静态 MAC 配在 linkagg ID 而非物理口："Static MAC Addresses are not assigned to physical ports that belong to a link aggregate." <<<PAGE 106>>>
## VLAN（Ch4）
- **P30** VLAN 通过软件分割广播域，免去物理改线："VLAN configuration and port assignment is handled through switch software." <<<PAGE 115>>>
- **P31** VLAN 操作状态在至少一个活动端口加入前保持 inactive，STP/路由接口随之不激活："The operational status of a VLAN remains inactive until at least one active switch port is assigned to the VLAN." <<<PAGE 115>>>
- **P32** 802.1Q tag 为 4 字节：前 2 字节标识 802.1Q，后 2 字节携带 VID+优先级。<<<PAGE 118>>>
- **P33** 入方向分类规则：带 tag 必须匹配端口默认 VLAN 或已打标 VLAN，否则丢弃；无 tag 进端口默认 VLAN。<<<PAGE 118>>>
- **P34** 一个端口只能属于一个 untagged VLAN（即默认 VLAN），可属于任意多个 tagged VLAN："A port can only be assigned to one untagged VLAN." <<<PAGE 118>>>
- **P35** 删除 VLAN 时路由接口被移除、VPA 丢弃；若是端口默认 VLAN 则端口回落到 VLAN 1。<<<PAGE 116>>>
- **P36** VLAN admin-state 禁用时端口归属保留但不转发流量。<<<PAGE 116>>>
- **P38** 主 VLAN 上配置的 admin 状态/STP 状态/IP 接口自动作用于全部关联二级 VLAN："When the status is changed for the Primary VLAN ID, the change is automatically applied to the Secondary VLANs." <<<PAGE 129>>>
## 高可用 VLAN/服务器集群（Ch5）
- **P39** HA VLAN 把发往单一目的 MAC 的流量复制到多个出端口实现服务器集群冗余："High availability (HA VLAN)s send traffic intended for a single destination MAC address to multiple switch ports." <<<PAGE 140>>>
- **P40** L2 集群用静态 MAC 实现、L3 集群用静态 ARP 实现："The L2 mode is currently supported in AOS using the static mac-address command and L3 mode by the static ARP command." <<<PAGE 140>>>
- **P41** 出端口可静态配置或通过 IGMP report 注册，组播依据目的 MAC/IP 可配置。<<<PAGE 140>>>
## 生成树（Ch6）
- **P42** AOS 支持 802.1D STP、802.1w RSTP、802.1Q-2005 MSTP；RSTP 让阻塞口跳过 listening/learning 直接转发："RSTP expedites topology changes by allowing blocked ports to transition directly into a forwarding state." <<<PAGE 157>>>
- **P43** 拓扑计算原理：选根桥→每桥计算到根最优路径→阻塞成环节路；根路径成本=接收端口路径成本之和，最低者为指定桥。<<<PAGE 157>>>
- **P44** 端口角色五类：Root/Designated/Backup/Alternate/Disabled；backup 与 alternate 的区分是 802.1w 为快速切换引入。<<<PAGE 158>>>
- **P45** MST 把 VLAN 集合映射到 MSTI，Flat 模式下最多 17 个实例（含 CIST 实例 0）。<<<PAGE 164>>>
- **P46** Flat 模式是整交换机单棵树（跨 VLAN 比较）；Per-VLAN 模式是每 VLAN 一棵树（AOS 私有实现）。<<<PAGE 164>>>
- **P47** MSTP 下端口状态由 CST 算法统一计算，但可对单个 MSTI 配 priority/path cost 使端口在该 MSTI 转发而在其他实例阻塞。<<<PAGE 164>>>
- **P48** Flat 模式下 CIST 被禁则对所有 VLAN 禁用；单 VLAN 禁用只把该 VLAN 端口移出算法。<<<PAGE 120>>>
## SPBM（Ch7）
- **P49** SPBM=ISIS-SPB 控制面 + 802.1ah MAC-in-MAC 数据面，IEEE 802.1aq："SPBM provides a mechanism to automatically define a shortest path tree (SPT) bridging configuration through a Layer 2 Ethernet network." <<<PAGE 211>>>
- **P50** 角色分工：BEB 学习并封装客户帧，BCB 只按 BMAC 转发不学客户 MAC："the BCB does not have to learn any of the customer MAC addresses." <<<PAGE 211>>>
- **P51** BVLAN 不学源 MAC、不泛洪未知流量，只按 ISIS-SPB 填充的 FDB 转发："Unlike standard VLANs, BVLANs do not learn source MAC addresses or flood unknown destination or multicast frames." <<<PAGE 211>>>
- **P52** 每个 SPB 桥以自己为根计算 SPT，因此任意两点间都是最短路径，克服 STP 根桥次优路径问题："each bridge can provide the shortest path to every other bridge in the network." <<<PAGE 214>>>
- **P54** 环路抑制靠 BVLAN 严格入向源 MAC 检查（异常来源即丢弃），MAC 学习由控制面完成。<<<PAGE 214>>>
- **P55** I-SID 标识 SPB 服务并绑定 BVLAN，一个 BVLAN 可承载多个 I-SID；SAP 把接入端口与特定客户流量（CVLAN/untagged/all）绑定到服务。<<<PAGE 212>>>
- **P57** SAP 封装值语义：`port:x` 只映射 CVLAN x，`:0` 映射 untagged，`:all` 映射全部 tagged。<<<PAGE 245>>>
## 环回检测（Ch8）
- **P58** LBD 周期发探测帧，任何 LBD 使能口收到本机帧即判环并 shutdown 端口+trap+日志。<<<PAGE 325>>>
- **P59** remote-origin LBD 需全局+端口两级同时使能默认 LBD 和远端 LBD 四个条件才工作。<<<PAGE 326>>>
- **P60** 传输定时器默认 30 秒；被 block 端口停止一切收发。<<<PAGE 325>>>
- **P61** 与 STP 交互：MST 模式下 LBD 只能在 STP 禁用的接口上使能；LBD 帧不打 tag 发送。<<<PAGE 328>>>
- **P62** 与聚合交互：任一成员口检测到环，整个 linkagg 全部 shutdown。<<<PAGE 328>>>
## 链路聚合（Ch9/10）
- **P63** 聚合组被 AOS 当作虚拟物理口，VLAN/802.1Q/QoS 均可套用。<<<PAGE 341>>>
- **P64** 负载分担：非 IP 按 MAC、IP 报文按 IP 地址；组内端口必须同速："Ports must be of the same speed within the same link aggregate group." <<<PAGE 341>>>
- **P65** 静态聚合与部分厂商设备不互通："Static aggregate groups cannot be created between an OmniSwitch and some switches from other vendors." <<<PAGE 341>>>
- **P66** 动态聚合用 IEEE 802.3ad LACP，靠 LACPDU 双向协商最优配置并持续监测维护。<<<PAGE 352>>>
- **P67** 动态聚合组由唯一 MAC 标识（交换机生成，可改）。<<<PAGE 352>>>
## 双归链路 DHL（Ch11）
- **P68** DHL Active-Active：linkA/linkB 各映射一组 VLAN 同时活，故障时 VLAN 切换到另一链路，替代 STP 收敛。<<<PAGE 383>>>
- **P69** DHL 会话使能后两链路上的 STP 自动禁用。<<<PAGE 382>>>
- **P70** 未映射到 linkB 的 VLAN 自动归 linkA（默认全在 linkA）。<<<PAGE 383>>>
## ERP（Ch12）
- **P72** ERP 基于 ITU-T G.8032，用 R-APS 协议在以太环上防环："Loop prevention is achieved by allowing the traffic to flow on all but one of the links within the protected Ethernet ring." <<<PAGE 395>>>
- **P73** RPL owner 阻塞 RPL；故障时 R-APS(SF) 触发解阻塞进入保护模式，全网 flush 动态 MAC。<<<PAGE 397>>>
- **P74** 恢复流程：恢复侧发 R-APS(NR) 并启 Guard Timer→RPL owner 启 WTR→超时后阻塞 RPL 并发 R-APS(NR,RB)→各节点 flush MAC 回到 idle 模式。<<<PAGE 398>>>
- **P75** WTR 用于确认环稳定后才回到阻塞态；Guard Timer 防止接收过时 R-APS，取值须大于 R-APS 绕环最大转发时延。<<<PAGE 396>>>
- **P76** ERPv2 支持多环/梯形网、R-APS Virtual Channel、revertive/non-revertive；子环不能用共享链路。<<<PAGE 395>>>
- **P77** 链路监测用 ETH CC OAM（CFM），本实现叠加 link up/down 事件加快收敛。<<<PAGE 395>>>
- **P78** MRP 面向工业环网，对单一链路/节点故障做确定性重构："MRP is designed to react deterministically on a single failure of an inter-switch link or switch in the ring." <<<PAGE 426>>>
- **P79** 角色模型：一个 MRM+多个 MRC；MRA 通过投票（MRP_Test 帧携带优先级+MRP_TestMgrNAck）自动选出 MRM，其余转 MRC。<<<PAGE 428>>>
- **P80** MRM 控制：双向周期发 MRP_Test；能收到自己发的测试帧说明环闭合→阻塞一口；收不到则两口全转发。<<<PAGE 428>>>
- **P81** 环口三态：Disabled/Blocked（仅放行 MRP 控制帧与 LLDP/PTP 等）/Forwarding。<<<PAGE 426>>>
- **P82** 冗余域=环；每域恰好两个环口，域 ID 用于多环设备区分帧。<<<PAGE 428>>>
## MVRP（Ch14）
- **P83** MVRP 作为 MRP 应用在专用组播 MAC 上收发声明，动态创建/撤销 VLAN 注册："MVRP allows both end stations and bridges ... to issue and revoke declarations relating to membership of VLANs." <<<PAGE 442>>>
- **P84** 动态 VLAN 的所有端口对该 VLAN 都是 tagged 口。<<<PAGE 442>>>
- **P85** 转发声明≠加入：端口转发从其他口学到的声明，但只有本口收到声明才加入该 VLAN。<<<PAGE 442>>>
- **P86** 与 STP 交互：MVRP 仅支持 Flat 模式；拓扑变化时 MVRP 学到的动态 VPA 一并删除。<<<PAGE 444>>>
- **P87** MPLS 用 32 位标签头（20 位 Label）逐跳标签交换建立点到点通道。<<<PAGE 457>>>
- **P88** LSP 单向：双工业务需要两条 LSP；LSP 物理路径不受 IGP 最短路径约束。<<<PAGE 457>>>
- **P89** 标签栈处理永远只看栈顶标签，查表得到下一跳+栈操作（swap/pop/push）。<<<PAGE 457>>>
- **P92** VPLS 是多点 L2VPN，需 PE 间全网格伪线；VPWS 只是点对点，不含 L2/L3 功能："VPLS is a superset of VPWS." <<<PAGE 478>>>
- **P93** VPLP 防环规则 Split Horizon：从 PW 收到的包绝不再从 PW 发出；全网格+水平分割保证广播可达且无环。<<<PAGE 478>>>
- **P95** VPLS 每服务实例维护 FIB，未知目的泛洪到全部 LSP 直到目标回应学习到 MAC。<<<PAGE 480>>>
- **P96** VXLAN 把 VM 的以太帧封装进带 UDP 头的 IP 包在三层网传输；OmniSwitch 作 VXLAN 网关连接 VXLAN 与传统 VLAN 域。<<<PAGE 533>>>
- **P100** 本地二层流量直接桥接不走隧道，封装过程对 VM 透明。<<<PAGE 534>>>
## EVPN（Ch18）
- **P101** EVPN 是 BGP 扩展，用控制面通告 MAC/IP 可达性，替代数据面泛洪学习："Since the MAC learning is handled in the control plane with EVPN architecture, it avoids the flooding in Layer 2." <<<PAGE 583>>>
- **P102** EVPN 以 all-active 多归属提供多路径转发与冗余；DF/NDF 分工：仅 DF 转发 BUM，保证无环。<<<PAGE 583>>>
- **P103** 路由类型分工：RT1(AD/快速收敛/别名负载分担)、RT2(MAC/IP 通告/移动性/ARP 抑制)、RT3(含组播路由/ingress replication 建 BUM 泛洪域)、RT4(ES 路由/DF 选举)、RT5(IP 前缀/L3VPN)、RT6-8(选择性组播/IGMP 同步)。<<<PAGE 584>>>
- **P104** AOS ESI 模型：物理口/LACP 自动生成 Type 0x3 MAC-based ESI；静态聚合必须手工配 ESI。<<<PAGE 587>>>
- **P105** AOS 单归设备也用非零 ESI，享受控制面 FDB 管理，且可与其他厂商互通。<<<PAGE 583>>>
- **P107** RD 自动生成：8 字节=2 字节 Type(0x1)+6 字节值；值域分 service(0x0)/ESI(0x1)/prefix(0x2) 三类对象。<<<PAGE 588>>>
## IP（Ch21）
- **P108** IP 无连接不可靠，靠 TCP 补可靠；ARP/VRRP/ICMP/组播是配套的基础协议。<<<PAGE 709>>>
- **P109** IP 接口绑定 VLAN：`ip interface <name> address <ip> vlan <vid>` 是三层路由基本模型。<<<PAGE 709>>>
- **P110** 静态路由/递归静态路由/默认路由/黑洞路由均由 `ip static-route` 系列配置（章内各节）。<<<PAGE 709>>>
## VRF（Ch22）
- **P111** VRF 在同一物理交换机上分割 L3 实例，类比 VLAN 分割 L2："Similar to using VLANs to segment Layer 2 traffic, VRF instances are used to segment Layer 3 traffic." <<<PAGE 756>>>
- **P112** 每个 VRF 独立路由表+独立路由协议实例，可重复使用 IP 地址空间。<<<PAGE 756>>>
- **P113** AOS VRF 不要求 BGP/MPLS 骨干，可经 GRE/IP-IP 隧道点对点承载。<<<PAGE 756>>>
## IPv6（Ch23）
- **P114** IPv6 增强：128 位地址、无状态自动配置、任播、简化头、ND 协议替代 ARP/广播。<<<PAGE 773>>>
- **P115** 地址类型：link-local（仅链路内有效不可路由）、unicast、unique local、multicast、anycast（前缀不可辨识）。<<<PAGE 774>>>
- **P116** IPv4/IPv6 共存机制：双栈、同 VLAN 双协议接口、IPv6-over-IPv4 隧道、IPv4 内嵌地址。<<<PAGE 773>>>
- **P117** JITC 模式下禁配 Site-Local（FEC0::/10）地址。<<<PAGE 774>>>
## IPsec（Ch24）
- **P119** OmniSwitch IPsec 仅支持传输模式（Transport Mode）：头插在 IP 头与上层协议头之间。<<<PAGE 819>>>
- **P120** ESP 由 IP 协议号 50 标识；SPI+目的地址+协议唯一确定 SA；认证先校验后解密。<<<PAGE 820>>>
- **P122** RIP 以跳数为度量，直连=1 跳，>15 跳路由删除；默认 30 秒广播更新。<<<PAGE 842>>>
- **P124** RIPv2 增强（next hop/认证/组播更新）只有组播时才可用，以兼容 RIPv1。<<<PAGE 843>>>
## BFD（Ch26）
- **P127** 异步控制包模式与 Echo 模式：VRRP/静态路由只用 Echo，OSPF/IS-IS/BGP 用控制包；Echo 单跳、控制包可多跳。<<<PAGE 870>>>
## DHCP Relay/安全（Ch27）
- **P129** DHCP Relay 用 UDP 67/68，校验 forward-delay 与 maximum-hops，不满足即丢弃；多目的地址时全发。<<<PAGE 903>>>
- **P130** relay 转发模式分 global 与 per-interface 两级。<<<PAGE 903>>>
- **P131** DHCP 三种地址分配：automatic（永久）/dynamic（租期）/manual（管理员指定由 DHCP 传达）。<<<PAGE 904>>>
- **P132** DHCP Relay Agent 可跨 VLAN 域与 SPB service 域中继；Generic UDP Relay 按预配端口转至 VLAN/SPB/IP。<<<PAGE 904>>>
- **P133** 外部路由器 relay 场景：子网地址由路由器插入请求，交换机无需 IP。<<<PAGE 905>>>
- **P134** L3 DHCP Snooping 必须借助 relay（客户端与服务器不同 VLAN）；L2 模式无需 relay 与 IP 接口。<<<PAGE 925>>>
- **P137** 全局 Option-82 使能与任意级别 Snooping 互斥；交换机级与 VLAN 级 Snooping 互斥。<<<PAGE 925>>>
- **P138** 内部 DHCP Server 由 policy file+配置文件+数据库文件驱动，与 VRF/DHCP Snooping/IP 接口交互（章内 Interaction 节）。<<<PAGE 894>>>（正文页 28-4 附近，标记 <<<PAGE 894>>> 前后）
## VRRP（Ch29）
- **P139** VRRP 选举虚拟路由器 master 转发虚拟 IP 流量，master 失效最高优先级 backup 接管。<<<PAGE 979>>>
- **P141** Master_Down_Interval=(3×Adv_Interval)+Skew_Time，Skew=(256-Priority)/256，优先级越低等待越长避免抖动。<<<PAGE 980>>>
- **P142** 虚拟 MAC：v2=00-00-5E-00-01-VRID，v3/IPv6=00-00-5E-00-02-VRID；ND 替代 ARP 用于 IPv6。<<<PAGE 981>>>
- **P143** 成为 master 时发免费 ARP；接口 IP 被虚路由共享时路由机制不再发免费 ARP，防表未稳先导流。<<<PAGE 981>>>
- **P144** VRRP 支持 BFD 联动 tracking 与 UNP 动态 SPB SAP（章内 Interaction 节）。<<<PAGE 980>>>
## SLB（Ch30）
- **P145** SLB 集群以 VIP（L3，需服务器配 loopback）或 QoS condition（L2/L3）标识虚拟服务器。<<<PAGE 1012>>>
- **P147** 分发算法为加权轮询 WRR，按服务器相对权重分配请求；健康监测依赖 ping 探测（周期/超时/重试可配）。<<<PAGE 1012>>>
- **P148** 组播组地址为 D 类 224.0.0.0-239.255.255.255，239/8 为管理域（边界保留）。<<<PAGE 1032>>>
- **P150** 多个组播路由器共存时最低 IP 者当选 querier。<<<PAGE 1033>>>
- **P151** 组播路由协议包：PIM-SM/DM 与 DVMRP，建立组播路由库，IPMS 依其决策+端口成员请求转发。<<<PAGE 1033>>>
- **P156** QoS 四步序：分类标记→拥塞管理（入队调度）→拥塞避免（随机丢弃防 tail drop）→限速整形。<<<PAGE 1103>>>
- **P158** 策略=条件+动作；流不匹配任何策略则用端口默认 QoS；多策略命中取最高 precedence。<<<PAGE 1133>>>
- **P159** 每端口 8 条队列，入队依据策略+ToS/802.1p+端口信任状态。<<<PAGE 1133>>>
- **P160** 策略来源决定修改权：PolicyView(LDAP) 建的只能 PolicyView 改，CLI/WebView 建的只能本端改。<<<PAGE 1133>>>
- **P161** 四类策略列表：default/UNP/egress/AFP（AFP 仅 OS6900）。<<<PAGE 1134>>>
- **P163** 条件配置约束：IPv4/IPv6 条件不能混用；destination VLAN 条件仅组播规则可用。<<<PAGE 1135>>>
- **P164** policy condition/action/rule 配置后必须 `qos apply` 才激活。<<<PAGE 1149>>>
- **P165** LDAP 策略服务器通过 PolicyView 下发策略，交换机按 aaa ldap-server 系列配置主机/端口/检索库/SSL。<<<PAGE 1175>>>（章 Server Overview，34-3 页附近）
- **P167** 认证路径：802.1X(EAP over RADIUS) 用于 supplicant；MAC 认证用于非 supplicant（MAC 作 username/password 送 RADIUS）。<<<PAGE 1213>>>
- **P168** 认证失败或无 profile 返回时回落到 UNP 端口默认 profile 与分类规则。<<<PAGE 1213>>>
- **P169** UNP 分类规则基于端口/设备属性（源 MAC、domain ID、IP 等），无需认证。<<<PAGE 1213>>>
- **P170** profile 属性（VLAN/service 映射、QoS policy list 等）应用于划入该 profile 的设备流量。<<<PAGE 1210>>>
- **P171** bridge 口走 VLAN profile、access 口走 service profile；先配 RADIUS→profile→映射→分类规则→端口→认证/分类使能→默认 profile 的标准次序。<<<PAGE 1211>>>
- **P172** MAC 会话定时器决定登录后会话保持时长（默认 12 小时）。<<<PAGE 1210>>>
- **P173** AppMon 以 DPI 签名实时识别应用流，施加应用级 QoS 标记与安全策略。<<<PAGE 1431>>>
- **P174** AppMon 组件链：签名 kit 文件→应用池→应用列表（按名或组）→应用组→QoS 策略。<<<PAGE 1431>>>
- **P175** 监控流程：端口采样→签名匹配→更新流数据库→应用记录；强制流程再叠加 QoS 执行。<<<PAGE 1432>>>
- **P176** AFP 用 REGEX 签名（/flash/app-signature/app-regex.txt）匹配采样 IP 包，命中即生成多组分类器入库并联动 QoS/trap/UNP 列表。<<<PAGE 1457>>>
- **P177** AFP 默认全局使能但所有端口禁用；端口使能才触发采样。<<<PAGE 1457>>>
## 认证服务器（Ch38）
- **P178** AAA 服务器矩阵：RADIUS（管理访问除 SNMP+端口准入均支持）、TACACS+（含 SNMP，不支持端口准入）、LDAP（含 SNMP，不支持端口准入）。<<<PAGE 1475>>>
- **P179** 每台服务器可配一台同型备份；每种认证方式可列跨类型备份列表；交换机用第一台可用服务器，找不到用户即失败（不自动轮询下台）。<<<PAGE 1475>>>
- **P180** 管理访问的权限（授权）优先从服务器取，未配置则回落本地用户库。<<<PAGE 1475>>>
## 端口映射（Ch39）
- **P181** 端口映射会话把源口流量复制到目的口，可单向/双向、可禁未知单播泛洪（章 Quick Steps）。<<<PAGE 1503>>>（39-3 页附近）
## LPS（Ch40）
- **P182** LPS 限制端口源 MAC 学习：学习窗口时长+最大 bridged/filtered 数量+授权 MAC 范围。<<<PAGE 1536>>>
- **P183** 违规处理三选一：阻断违规流量/停止学习/管理关闭端口。<<<PAGE 1536>>>
- **P184** 学习窗口全局生效不能按口配；窗口关闭时动态 MAC 可转静态或伪静态（不老化不 flush 不存 running-config）。<<<PAGE 1536>>>
- **P185** MAC 四类型：static/pseudo-static/dynamic bridged/dynamic filtered；bridged 满后新地址按 filtered 学。<<<PAGE 1537>>>
- **P186** LPS 支持 fixed/802.1Q/UNP/SAP 口，不支持 linkagg 及成员口。<<<PAGE 1536>>>
## 诊断（Ch41）
- **P187** 端口镜像会话=source+destination+可选 unblocked-vlan（防 STP 变化中断镜像）。<<<PAGE 1558>>>
- **P188** sFlow 三件套：receiver（IP/端口/超时）+sampler（采样率/头长）+poller（轮询间隔）；默认 UDP 6343、datagram 1400 字节、版本 5。<<<PAGE 1561>>>
- **P189** 端口监控（port-monitoring）持久会话落盘数据文件（默认 64K、可覆盖、capture brief）。<<<PAGE 1559>>>
- **P190** Switch Health 通过资源阈值+采样间隔监控 CPU/内存等并出统计。<<<PAGE 1566>>>（41-12 页附近）
## VLAN Stacking（Ch42）
- **P191** QinQ 组件：PE bridge/transit bridge/SVLAN 隧道/NNI/UNI；SVLAN tag 附加在全部客户流量上透明穿越城域网。<<<PAGE 1606>>>
- **P192** 隧道 ID 与 VLAN ID 一一对应，创建隧道即向 VLAN Manager 建同名 VLAN："tunnel and VLAN are interchangeable terms." <<<PAGE 1608>>>
- **P193** 封装两法：double tagging（外插 SVLAN 成双 tag）与 VLAN translation（替换 CVLAN 为 SVLAN）。<<<PAGE 1608>>>
## 日志（Ch43）
- **P194** 日志体系：级别筛选+输出设备（console/memory/remote...)+文件大小+格式+存储上限（章 Commands Overview）。<<<PAGE 1580>>>（43-3 页附近）
## Service OAM/CFM（Ch44）
- **P195** Service OAM(802.1ag/Y.1731) 管端到端业务实例，Link OAM(802.3ah) 管单链路，二者互补定位故障。<<<PAGE 1655>>>
- **P196** MD 分层 0-7：5-7 客户、3-4 运营商、0-2 操作员；MEP 发起 OAM 命令防域间泄漏，MIP 被动应答。<<<PAGE 1655>>>
- **P197** 机制：CC 连续性检查/loopback/linktrace；RFP 把连通故障事件传播到 MEP 所在接口。<<<PAGE 1655>>>
## EFM LINK OAM（Ch45）
- **P198** 802.3ah 用慢协议 OAMPDU 承载控制与状态，单链路传递不被网桥转发。<<<PAGE 1673>>>
- **P199** 发现阶段交换能力与配置，仅当双方 loopback/链路检测/链路事件设置匹配才建立 OAM 连接；5 秒无 OAMPDU 即失联（keepalive）。<<<PAGE 1674>>>
- **P200** 功能集：发现/链路监控（errored frame 等三窗口阈值）/远端故障检测/远端环回定位。<<<PAGE 1673>>>
## PPPoE-IA（Ch47）
- **P201** PPPoE-IA 在接入交换机为 PPPoE 发现报文插入 VSA（电路信息）标识用户线路："PPPoE-IA is a means by which the discovery packets of PPPoE are tagged at the access switch ... using Vendor Specific Attributes (VSA)." <<<PAGE 1714>>>
- **P202** access loop 标识：直连用户=chassis/slot/port，多用户共享口=端口+CVLAN 组合。<<<PAGE 1714>>>
- **P203** 全局与端口两级都必须使能 PPPoE-IA 才生效；参数配置与使能状态解耦。<<<PAGE 1715>>>
## SAA（Ch48）
- **P204** SAA 以 SPB 会话做服务保障测量，可生成 XML 历史文件（章 Overview/Configuring）。<<<PAGE 1700>>>（48-4 页附近）

---
合计：204 条（P1-P204）。
