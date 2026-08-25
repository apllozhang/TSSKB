# cases — 配置流程案例（OmniSwitch AOS 8.10R4）

格式：编号 C# ｜ 场景 ｜ 命令序列（-> 为 AOS CLI 提示符）｜ 验证命令 ｜ 页码

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

## SPBM（Ch7）

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
- **C27** MVRP：全局 enable→限制最大动态 VLAN 数→注册模式/applicant 模式→定时器→限制注册/通告（章 Configuring MVRP）。验证：show mvrp。 <<<PAGE 447>>>（14-7 页）

## MPLS/L2VPN/VXLAN/EVPN（Ch15-18）

- **C28** MPLS+LDP 快配：`mpls enable`→载入 LDP 软件→`ldp enable`→全局定时器→接口使能 LDP→（可选）GR/session protection/MD5 认证。验证：show mpls/ldp。 <<<PAGE 453>>>（15-3 页）
- **C29** VPLS(LDP 信令)：建 VPLS 服务→配 SAP（接入侧封装）→配 SDP（MPLS 隧道）→SDP 绑定到服务；多 PE 全网格。验证：show sdp/vpls。 <<<PAGE 478>>>（16-9 页）
- **C30** VPWS(LDP)：同 VPLS 流程但点到点，两端各一 SAP+SDP 绑定。验证：show vpws。 <<<PAGE 505>>>（16-37 页）
- **C31** VXLAN 网关：Loopback0 IP（VTEP 标识）→建 VXLAN service(VNI)→配 SAP→配 SDP→服务绑定 SDP→（可选）改 UDP 端口。验证：show vxlan service/sdp。 <<<PAGE 536>>>（17-18 页）
- **C32** EVPN on VXLAN：底层 BGP(EVPN 地址族)+Loopback0→使能服务 EVPN→access 口 ES 操作→SAP→（对称 IRB）fabric-vpn 服务+路由重分发；RR 与两 Clos 层建议见章内部署模型。验证：show evpn 系列。 <<<PAGE 596>>>（18-15 页）
- **C33** EVPN 多站（Multi-site）：边界节点 manual RT 配置+DCI 互联需求（章 Multi-site Sample Topology / Manual RT Configuration）。 <<<PAGE 612>>>（18-87 页）

## 三层（Ch21-26）

- **C34** IP 转发快配：建 VLAN→加端口→`ip interface vlan-20 address 171.11.1.1 vlan 20`→静态/默认/黑洞路由。 <<<PAGE 709>>>
- **C35** VRF 部署：`vrf <name>`→VRF profile→IP 接口划入 VRF→VRF 内路由协议实例；Management VRF 需注意管理应用联动。验证：show vrf。 <<<PAGE 756>>>（22-2 页）
- **C36** VRF Route Leak：`ip route ... next-hop vrf` 类配置跨 VRF 泄露前缀（章 Quick Steps for Configuring VRF Route Leak）。 <<<PAGE 712>>>（21-44 页）
- **C37** IPv6 路由：`ipv6 interface`+地址（link-local 自动生成）→IPv6 静态路由→（可选）隧道 over IPv4、RA 过滤、DoS 检测。 <<<PAGE 774>>>（23-4 页）
- **C38** IPsec AH 策略：`ipsec` master key→policy（AH/HMAC-SHA1）→SA→绑定接口/流（章 Quick Steps for Configuring an IPsec AH Policy）。 <<<PAGE 819>>>（24-3 页）
- **C39** IPsec discard 策略+默认丢弃：配置 discard policy 丢弃如 RIPng 报文（章 Additional Examples: Discarding RIPng Packets）。 <<<PAGE 822>>>（24-23 页）
- **C40** RIP：载入→`ip rip` 全局/接口使能→定时器调优→重分发→认证（RIPv2 可 SHA256）。验证：show ip rip。 <<<PAGE 842>>>（25-6 页）
- **C41** BFD：配会话参数（传输/接收间隔、检测倍数）→宿主协议（OSPF/BGP/VRRP/静态）挂 BFD。验证：show bfd。 <<<PAGE 869>>>（26-15 页）

## DHCP（Ch27-28）

- **C42** DHCP Relay 六步：`ip dhcp relay admin-state enable`→`ip dhcp relay destination 128.100.16.1`→（可选）`ip dhcp relay per-interface-mode`→`ip dhcp relay interface ipv4-v200 destination 128.100.16.1`→`ip dhcp relay forward-delay 30`+`ip dhcp relay maximum-hops 10`→`ip dhcp relay insert-agent-information`。验证：`show ip dhcp relay interface`。 <<<PAGE 902>>>
- **C43** DHCP Snooping：`dhcp-snooping admin-state enable`→服务器口设 trusted→（可选）bypass Option-82 校验/绑定表静态条目。 <<<PAGE 926>>>
- **C44** 内部 DHCP Server：写 policy file+dhcpd 配置文件→数据库文件路径→使能（章 Quick Steps to Configure Internal DHCP Server）。验证：show dhcp server。 <<<PAGE 893>>>（28-2 页）
- **C45** DHCPv6 Relay/Snooping/RA Guard：使能 relay 服务→relay 接口→max hops；snooping 绑定表+ISF 源过滤；RA guard 端口策略（章 DHCPv6 各节）。 <<<PAGE 917>>>（27-35 页）

## VRRP/SLB/组播（Ch29-32）

- **C46** VRRP 虚拟路由器：`ip vrrp 23 interface ipv4-100`→`ip vrrp 23 interface ipv4-100 address 192.168.173.1`→对端同样两步→`ip vrrp 23 interface ipv4-100 admin-state enable`（IPv4 须先配地址才能使能）。验证：`show ip vrrp`/`show ipv6 vrrp`。 <<<PAGE 978>>>
- **C47** VRRP tracking：建 tracking policy（监控 IP 可达/BFD）→关联到虚拟路由器（章 Creating VRRP Tracking Policies）。 <<<PAGE 993>>>（29-24 页）
- **C48** SLB 集群：使能 SLB→`slb cluster <id> vip <ip> name ...`→`slb cluster <id> server <ip> weight n`→ping 周期/超时/重试→上下线 cluster/server→（可选）probe 探测关联。验证：show slb。 <<<PAGE 1011>>>（30-10 页）
- **C49** IPMS：全局使能→IGMP 版本/静态 querier/静态组→query interval/robustness 等参数→（IPMSv6 对应 MLD 系列）。验证：show ipms / ipmsv6。 <<<PAGE 1038>>>（31-10 页）
- **C50** IPMVLAN（MVR）：`ipmvlan <id>` 使能→分配 IPv4/IPv6 地址→sender 口（NNI，仅 1 个）→receiver 口/CVLAN 关联→静态 IGMP 组。验证：show ipmvlan。 <<<PAGE 1093>>>（32-10 页）

## QoS（Ch33）

- **C51** QoS 策略四步：`policy condition cond3 source ip 10.10.2.3`→`policy action action2 priority 7`→`policy rule my_rule condition cond3 action action2`→`qos apply`。验证：`show policy rule`。 <<<PAGE 1147>>>
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
