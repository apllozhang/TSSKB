# cases.md · Lab / 配置案例提取
# 来源: OmniSwitch LAN SPB Concepts & Implementation (DT00XTE323EN, Edition 12)
# 规则: 每条含原文引用与页码；CLI 命令保留原文；宁多勿漏，待后续独立验证阶段筛选

```yaml
- id: c01
  title: Lab1——SPB-M 骨干从零部署（4 节点部分网状，BVLAN+IS-IS）
  type: case
  source_chapter: "p83"
  source_quote: |
    "-> spb bvlan 2000
    -> spb isis bvlan 2000 ect-id 1
    -> spb bvlan 2001
    -> spb isis bvlan 2001 ect-id 2
    -> spb bvlan 2002
    -> spb isis bvlan 2002 ect-id 3
    -> spb isis admin-state disable
    -> spb isis control-bvlan 2000
    -> spb isis interface port 1/1/5-6
    -> spb isis interface port 1/1/25
    -> interface port 1/1/5-6 admin-state enable
    -> spb isis admin-state enable"
  summary: |
    骨干部署 Lab 的完整命令序列（每节点执行）：三步建 BVLAN 2000/2001/2002 并分别指 ECT 1/2/3（控制 BVLAN 专用 2000，业务用 2001/2002 走两条不同路径）；先禁用 IS-IS 再设 control-bvlan 2000；按物理连线把互联口配成 SPB IS-IS 接口（物理口或 linkagg，可用 port 范围 1/1/5-6）；最后全局 spb isis admin-state enable。验证见 p85 命令序列（bvlans/adjacency/info/unicast-table/spf/database/nodes），p86 留问题"Do the path are identical for each BVLAN?"引导观察 ECT 分流。
  tags: [lab, backbone, bvlan, isis, spb-m, day1]

- id: c02
  title: Lab2——L2 服务部署（VLAN 2/3 跨 SPB 骨干延展）
  type: case
  source_chapter: "p108"
  source_quote: |
    "Switch 5 -> vlan 2 / -> vlan 2 members port 1/1/1 untagged / -> vlan 2 members port 1/1/3 tagged
    Switch 7 & 8 -> service spb 2001 isid 2001 bvlan 2001 description vlan2 admin-state enable
    -> service spb 2002 isid 2002 bvlan 2002 description vlan3 admin-state enable
    Switch 7 -> service access port 1/1/3 / -> service access port 1/1/7
    -> service spb 2001 sap port 1/1/3:2 admin-state enable stats enable
    -> service spb 2002 sap port 1/1/3:3 admin-state enable stats enable
    -> service spb 2001 sap port 1/1/7:2 admin-state enable stats enable
    Switch 8 -> service spb 2001 sap port 1/1/3:2 admin-state enable stats enable"
  summary: |
    L2 服务完整开通样例：接入交换机（Sw5/6/3）建客户 VLAN 并 untag 用户口、tag 上联口；BEB（Sw7/8）上 service spb 2001 isid 2001 bvlan 2001 建 VLAN2 服务、2002 建 VLAN3 服务（ISID/BVLAN 全网一致）；service access port 声明接入侧端口；service spb 2001 sap port 1/1/3:2 把 VLAN2 流量挂进服务。验证（p111-112）：show spb isis services、show service sdp spb、show mac-learning domain spb——可看到本地 MAC 落 sap:1/1/3:2、远端 MAC 落 sdp:32775:2001。
  tags: [lab, l2-service, sap, isid, vlan, day1]

- id: c03
  title: Lab3——协议分析与保护（链路倒换/metric 调整/overload/LBD/L2 Profile）
  type: case
  source_chapter: "p127"
  source_quote: |
    "Switch 7 -> spb isis interface port 1/1/6 metric 40
    Switch 8 -> spb isis interface port 1/1/6 metric 40
    -> spb isis overload timeout 120
    -> loopback-detection enable
    -> loopback-detection service-access port 1/1/3 enable
    -> service spb 2001 sap port 1/1/4:2 admin-state enable stats enable
    -> spantree vlan 2 admin-state disable
    -> service l2profile Drop-GVRP GVRP drop
    -> service access port 1/1/3 l2profile Drop-GVRP"
  summary: |
    五个保护实验的组合序列：①弹性测试——permanent ping 中断开 Sw7→Sw8 接口，用 show spb isis unicast-table 对拍确认所有 BVLAN 换到 1/1/5；②metric 引流——两侧同时把 port 1/1/6 metric 改 40，SPF 表 metric/跳数从 20/2 变 30/3；③overload——在路径上的 OS6900 执行 spb isis overload timeout 120 让流量绕行；④环路与 LBD——人为制造二次路径（Sw8 增 SAP + Sw5 tag VLAN2 + 关 VLAN2 生成树）复现环路（ping 断、MAC 双侧漂移），再启用 LBD 自动 shutdown 环路口恢复业务；⑤L2 Profile——自定义 Drop-GVRP 丢弃 GVRP 控制帧并挂到 access 口。
  tags: [lab, protection, metric, overload, lbd, l2-profile, day1]

- id: c04
  title: L3VPN 内联接口基础配置（service + ip interface 两命令）
  type: case
  source_chapter: "p161"
  source_quote: |
    "-> service service_id spb isid instance_id bvlan bvlan_id vlan-xlation
    -> ip interface if_name address ip_address/mask vlan vlan_id service service_id
    A service-based interface is used to provide in-line routing. Specify the service parameter to create an L3 VPN interface that is required for IP Routing over SPB.
    -> service 10 spb isid 1000 bvlan 4001 vlan-xlation
    -> ip interface L3VPN1 address 10.10.10.1/24 service 10"
  summary: |
    所有 IP over SPB（VPN-Lite/L3-VPN/VRRP 冗余共用的最小配置）：两条命令建内联 L3 接口——先 service 10 spb isid 1000 bvlan 4001 建服务，再 ip interface L3VPN1 address 10.10.10.1/24 service 10 把 IP 接口绑到服务；接口地址即网关地址，用于把 VRF 绑定到 SPB 服务实例。新平台（6860N/6900-X48C6/9900 等）单遍处理无需回环线缆（p159）。
  tags: [l3vpn, inline-routing, ip-interface, configuration]

- id: c05
  title: Lab4——IP Routing over SPB 路由冗余（VRRP 双网关交叉优先级）
  type: case
  source_chapter: "p167"
  source_quote: |
    "Switch 1 & 2 -> service spb 2001 isid 2001 bvlan 2001 description vlan2 admin-state enable
    -> ip interface L3vpnvlan2 address 192.168.2.1/24 service 2001
    -> ip interface L3vpnvlan3 address 192.168.3.1/24 service 2002
    Switch 7 -> service access port 1/1/3 vlan-xlation enable / -> service 2001 vlan-xlation enable
    Switch 1 -> ip vrrp 2 interface L3vpnvlan2 priority 200 / -> ip vrrp 2 interface L3vpnvlan2 address 192.168.2.254 / -> ip vrrp 2 interface L3vpnvlan2 admin-state enable
    Switch 1 -> ip vrrp 3 interface L3vpnvlan3 priority 100 ... Switch 2 -> ip vrrp 2 ... priority 100 / ip vrrp 3 ... priority 200"
  summary: |
    在 Lab2 的 L2 服务上直接叠网关冗余：核心 Sw1/Sw2 上对既有服务 2001/2002 各建内联 IP 接口（.1/.2），BEB Sw7/8 侧对 access 口与服务开启 vlan-xlation；VRRP 按 VLAN 交叉——Sw1 做 vlan2（VRID 2, prio 200）主、vlan3（VRID 3, prio 100）备，Sw2 相反，虚网关统一 .254。验证 show ip vrrp / show ip vrrp statistics 看 Master/Backup 状态，客户端网关改 .254 后断上联测倒换。
  tags: [lab, vrrp, routing-redundancy, vlan-xlation, day2]

- id: c06
  title: VPN-Lite 内联静态+OSPF 双机配置对拍样例
  type: case
  source_chapter: "p176"
  source_quote: |
    "spb bvlan 4001
    service spb 10 isid 1000 bvlan 4001 admin-state enable
    vrf 1 ip interface L3vpn1 address 10.5.1.1/24 service 10
    vrf 1 ip static-route 192.168.3.0/24 gateway 10.5.1.2
    vrf 1 ip load ospf
    vrf 1 ip ospf interface L3vpn1 / vrf 1 ip ospf interface L3vpn1 admin-state enable
    vrf 1 ip ospf area 0.0.0.0 / vrf 1 ip ospf interface L3vpn1 area 0.0.0.0
    vrf 1 ip ospf admin-state enable"
  summary: |
    VPN-Lite 在 VRF 1 内的标准块配置（两台 OS9900 对拍，仅地址/路由不同）：建 BVLAN→建服务 isid 1000→VRF 内建绑服务的 IP 接口→（左机）静态路由指向对端网关 或（右机）ospf 五件套：ip load ospf、接口入 area 0.0.0.0、使能接口与全局。同一接口上静态与 OSPF 二选一演示了 VPN-Lite "SPB 当物理媒体、路由协议照常跑"的模型。
  tags: [vpn-lite, ospf, static-route, vrf, sample-config]

- id: c07
  title: Lab5——VPN-Lite over SPB 实操（4 节点共享 I-SID + OSPF 邻接）
  type: case
  source_chapter: "p180"
  source_quote: |
    "Switch 1 -> service spb 2009 isid 2009 bvlan 2000 description vlan999 admin-state enable
    -> ip interface L3vpn999 address 10.132.2.1/24 service 2009
    Switch 2/7/8 -> ... ip interface L3vpn999 address 10.132.2.{2|7|8}/24 service 2009
    Switch 1,2,7 & 8 -> ip load ospf / -> ip ospf area 0.0.0.0 / -> ip ospf interface L3vpn999
    -> ip ospf interface L3vpn999 admin-state enable / -> ip ospf interface L3vpn999 area 0.0.0.0
    -> ip ospf admin-state enable
    -> ip route-map local sequence-number 10 action permit
    -> ip route-map local sequence-number 10 match ip-address 0.0.0.0/0
    -> ip redist local into ospf route-map local"
  summary: |
    四台交换机共用服务 2009/I-SID 2009/BVLAN 2000 建 VPN-Lite 平面（L3vpn999 接口 .1/.2/.7/.8 同网段），在绑服务的接口上跑 OSPF area 0，并用 route-map local 匹配本地路由重分发进 OSPF（ip redist local into ospf）。本地业务 VLAN（Sw7 vlan7、Sw8 vlan8、Sw1 vlan10、Sw2 vlan20）经各自 ip interface 进路由域。验证 show ip ospf interface / show ip routes，测试含显示路径、路由表、MAC-SAP 映射与断口弹性四步（p182）。
  tags: [lab, vpn-lite, ospf, redistribution, day2]

- id: c08
  title: L3-VPN 内联配置对拍样例（bind/export/import 三件套）
  type: case
  source_chapter: "p202"
  source_quote: |
    "spb bvlan 4001
    service spb 10 isid 1000 bvlan 4001 admin-state enable
    vrf 1 ip interface L3vpn1 address 10.5.1.1/24 service 10
    spb ipvpn bind vrf 1 isid 1000 gateway 10.5.1.1 all-routes
    vrf 1 ip export all-routes
    vrf 1 ip import isid 1000 all-routes"
  summary: |
    L3-VPN 的最小五步（两机对拍只差地址）：建 BVLAN/服务/绑服务的 VRF 接口后，加三条 VPN-Lite 没有的命令——spb ipvpn bind vrf 1 isid 1000 gateway <本端接口IP> all-routes 建立 VRF↔I-SID 绑定；vrf 1 ip export all-routes 导出本地路由到 GRT；vrf 1 ip import isid 1000 all-routes 导回远端路由。不需要任何路由协议。与 p06（VPN-Lite）同为标准配置对拍模板。
  tags: [l3vpn, spb-ipvpn, bind, export, import, sample-config]

- id: c09
  title: Lab6——L3-VPN over SPB 实操（先停 OSPF 再绑 I-SID 2009）
  type: case
  source_chapter: "p211"
  source_quote: |
    "Switch 1,2, 7 & 8 -> ip ospf admin-state disable
    Switch 1 -> spb ipvpn bind vrf default isid 2009 gateway 10.132.2.1 all-routes
    Switch 2 -> spb ipvpn bind vrf default isid 2009 gateway 10.132.2.2 all-routes
    Switch 7 -> spb ipvpn bind vrf default isid 2009 gateway 10.132.2.7 all-routes
    Switch 8 -> spb ipvpn bind vrf default isid 2009 gateway 10.132.2.8 all-routes
    -> ip route-map local-to-spb sequence-number 50 action permit
    -> ip route-map local-to-spb sequence-number 50 match protocol local
    -> ip export route-map local-to-spb
    -> ip import isid 2009 all-routes"
  summary: |
    在 VPN-Lite Lab 基础上切到 L3-VPN 的改造序列：四台机先关 OSPF（避免双路由源），沿用服务 2009/I-SID 2009，逐台 spb ipvpn bind vrf default isid 2009 gateway <本端 10.132.2.x> all-routes；再建 route-map local-to-spb（match protocol local）过滤导出 ip export route-map local-to-spb；最后 ip import isid 2009 all-routes 收远端路由。验证链（p213）：show spb ipvpn bind → show ip global-route-table → show spb ipvpn route-table → show ip routes（IMPORT 协议路由）→ show ip export/import → show spb ipvpn redist。
  tags: [lab, l3vpn, ipvpn-bind, route-map, day2]

- id: c10
  title: Inline/Outline 三节点全网配置与 show 输出对拍
  type: case
  source_chapter: "p217"
  source_quote: |
    "spb bvlan 4001 / spb bvlan 4000 / spb isis control-bvlan 4000
    service spb 10 isid 1000 bvlan 4001 admin-state enable
    vrf default ip interface L3vpn2 address 10.5.1.3/24 service 10
    spb ipvpn bind vrf default isid 1000 gateway 10.5.1.3 all-routes
    vrf default ip export all-routes / vrf default ip import isid 1000 all-routes
    sw1 -> show spb ipvpn route-table / sw1 -> show ip global-route-table / sw1 -> show ip routes
    192.168.3.0/24  10.5.1.2  IMPORT"
  summary: |
    三台设备（.1/.2/.3 各带一对业务网段）共用 I-SID 1000 的完整配置 + 三级表对拍样例：show spb ipvpn route-table 看 I-SID 学到的远端路由（含源桥 B-MAC），show ip global-route-table 看 GRT 汇聚（isid/vrf 两类来源），show ip routes 看导入本 VRF 后的最终路由（IMPORT 标记）。配置含独立控制 BVLAN 4000 + 业务 BVLAN 4001 的分离设计，是排障"路由学到没有"的标准参照。
  tags: [l3vpn, three-node, show-output, grt, verification]

- id: c11
  title: L3 ECMP VPN——单 VRRF 双 I-SID 等价多路径配置
  type: case
  source_chapter: "p219"
  source_quote: |
    "spb bvlan 4001 / spb bvlan 4002
    service spb 10 isid 1000 bvlan 4001 admin-state enable
    service spb 20 isid 1001 bvlan 4002 admin-state enable
    vrf default ip interface L3vpn21 address 10.5.1.3/24 service 10
    vrf default ip interface L3vpn31 address 10.5.2.3/24 service 20
    spb ipvpn bind vrf default isid 1000 gateway 10.5.1.3 all-routes
    spb ipvpn bind vrf default isid 1001 gateway 10.5.2.3 all-routes
    (vrf default) ip import isid 1000 all-routes / (vrf default) ip import isid 1001 all-routes
    2.2.2.2/32 +10.5.1.2 IMPORT / +10.5.2.2 IMPORT"
  summary: |
    同一 VRF 绑两个 I-SID（1000/BVLAN4001、1001/BVLAN4002）实现 L3 等价多路径：每节点建两组服务+两个绑服务的接口+两次 bind，import 两个 I-SID 后 show ip routes 出现 "+" 标记的双下一跳（10.5.1.2/10.5.2.2）。p220 附完整 show ip global-route-table / show spb ipvpn route-table 输出，演示流量在两个 BVLAN 路径间分担。
  tags: [ecmp, l3vpn, multiple-isid, load-balancing]

- id: c12
  title: Lab7a——多点共享网（Multi-Access）SPB 拓扑改造
  type: case
  source_chapter: "p246"
  source_quote: |
    "Switch 3 -> vlan 2000-2002 members port 1/1/3-4 tagged / -> vlan 2000-2002 members port 1/1/7-8 tagged
    Switch 1 -> spb isis interface port 1/1/3 type multi-access / -> interfaces 1/1/3 admin-state enable
    Switch 7 -> spb isis interface port 1/1/7 type multi-access priority 127
    Switch 8 -> spb isis interface port 1/1/8 type multi-access
    ! Rollback: -> no spb isis interface port 1/1/3 / -> spb isis interface port 1/1/25 admin-state enable"
  summary: |
    用 Sw3 模拟共享 LAN（4 口透传 BVLAN 2000-2002）把四台 BEB 接入同一广播域：先把各机原 P2P 骨干口 disable（spb isis interface port X admin-state disable + 物理口 disable），再各出一条线到 Sw3 并配 type multi-access（Sw7 加 priority 127 抢 DIS）；验证 show spb isis adjacency（一口多邻接）/ show spb isis interfaces port X（Type: Multi-Access, Desg IS 即 DIS）。实验末尾给了完整回滚序列恢复 P2P 骨干（no spb isis interface + 重新 enable 原端口）。
  tags: [lab, multi-access, dis, shared-network, rollback, day2]

- id: c13
  title: Lab7b——DHL 双归属冗余接入（Case 1：Finance/Marketing 动态归属）
  type: case
  source_chapter: "p250"
  source_quote: |
    "Switch 3 -> vlan 30 name Finance / -> vlan 40 name Marketing
    -> dhl 1
    -> dhl 1 linka port 1/1/7 linkb port 1/1/8
    -> dhl 1 vlan-map linkb 40
    -> dhl 1 mac-flushing raw
    -> dhl 1 admin-state enable
    Switch 1, 2, 7 & 8 -> service spb 4003 isid 4003 bvlan 2002 description Finance admin-state enable
    -> service spb 4004 isid 4004 bvlan 2002 description Marketing admin-state enable
    Switch 7 -> service spb 4003 sap port 1/1/7:30 admin-state enable stats enable
    Switch 1 -> ip interface L3vpnvlan30 address 192.168.30.1/24 service 4003
    -> ip vrrp 30 interface L3vpnvlan30 priority 200 / address 192.168.30.254 / admin-state enable"
  summary: |
    接入双归属全流程：Sw3 用 DHL 双上联 Sw7（linkA 1/1/7）与 Sw8（linkB 1/1/8），vlan-map 把 VLAN 40 定向到 linkB；BEB 侧对两个新服务（4003 Finance/4004 Marketing）各挂 SAP（Sw7 1/1/7:30/:40、Sw8 1/1/8:30/:40），改 SAP 后需 disable/enable 端口重启分类；核心 Sw1/Sw2 建内联网关 + VRRP 交叉优先级（30 在 Sw1 主、40 在 Sw2 主）。验证 show dhl 1（Active Vlans: LinkA 1 30 / LinkB 40）；终端从 VLAN30 迁到 VLAN40 只需 vlan 40 members port 1/1/1 untagged + 改 IP。
  tags: [lab, dhl, redundant-access, vrrp, vlan-map, day2]

- id: c14
  title: Lab7c——ERP 环过 SPB 延伸（Case 2：环网接入映射到 SAP）
  type: case
  source_chapter: "p256"
  source_quote: |
    "Switch 5 -> vlan 1000 name erp-service / -> erp-ring 1 port1 1/1/3 port2 1/1/27 service-vlan 1000 level 1
    -> erp-ring 1 rpl-node port 1/1/27 / -> erp-ring 1 wait-to-restore-timer 1
    -> erp-ring 1 sap-neighbor port 1/1/3 / -> erp-ring 1 enable
    Switch 7 -> service 4003 spb isid 4003 bvlan 2002 description Finance
    -> service access port 1/1/3
    -> service 2009 sap port 1/1/3:1000
    -> service 4003 sap port 1/1/3:30 / -> service 4004 sap port 1/1/3:40
    -> erp-ring 1 port1 access-tagged 1/1/3 spb-remote-system switch_mac_address service-vlan 1000 level 1
    -> erp-ring 1 enable"
  summary: |
    ERP 环 + SPB 双侧配置模板：环内节点（Sw5 为 RPL owner，Sw6 普通）建保护 VLAN 30/40 与服务 VLAN 1000，erp-ring 1 port1/port2 + service-vlan 1000 + MEG level 1 成环，靠 BEB 的节点加 sap-neighbor；BEB 侧（Sw7/8）在同一 access 口上挂三个 SAP——1000（ERP 控制）、30/40（业务），并用带 spb-remote-system <对端 B-MAC> 的 access-tagged 形式把环的另一端"接到"远端 BEB。验证 show erp / show erp ring 1 / show erp statistics；倒换测试观察 RPL 端口阻塞恢复与 wait-to-restore 计时。
  tags: [lab, erp, g8032, rpl, sap-neighbor, day2]

- id: c15
  title: Lab8——UNP 三场景（动态服务/802.1x 认证/静默设备）
  type: case
  source_chapter: "p279"
  source_quote: |
    "-> unp port 1/1/1 port-type access
    -> unp system-default service-base 1000
    -> service 4005 spb isid 4005 bvlan 2002 description Training stats enable vlan-xlation enable
    -> unp port 1/1/1 802.1x-authentication
    -> unp profile UNP-employee
    -> unp profile UNP-employee map service-type static tag-value 0 service-id 4005
    -> aaa radius-server AAA host 192.168.100.102 key alcatel-lucent
    -> aaa device-authentication 802.1x AAA
    -> spb bvlan 2007 / -> spb isis bvlan 2007 ect-id 5
    -> service spb 2007 isid 1111 bvlan 2007 description Silent admin-state enable
    -> unp profile unp-profile-silent
    -> unp profile unp-profile-silent map service-type spb tag-value 90 isid 1111 bvlan 2007 vlan-xlation
    -> unp port 1/1/4 profile unp-profile-silent
    -> unp classification mac-address "@mac Silent-A" profile1 unp-profile-silent"
  summary: |
    UNP 三段实操：①动态服务——unp port 1/1/1 port-type access + 改 service-base 1000 后，未分类流量自动生成 systemDefault1000 动态服务（show service spb 见 ServiceId 32768* Dynamic）；②802.1x——服务 4005 + profile UNP-employee（map service-type static tag-value 0 service-id 4005）+ RADIUS（Filter-ID 返回 profile 名），aaa test-radius-server 可单测认证链路，show unp user 看 employee Active；③静默设备——新建 BVLAN 2007（ect 5）/服务 isid 1111，静态指派 profile 到端口（不老化 SAP），MAC 分类规则把 Silent-A/B 归入，mac-learning flush dynamic 后 SAP 仍在（show unp user details port 1/1/4 验证 SAP :90 / Service 2007 存活）。
  tags: [lab, unp, dynamic-service, 8021x, radius, silent-device, day3]

- id: c16
  title: Lab9——OV2500 纳管 SPB（带内管理+License+发现+拓扑）
  type: case
  source_chapter: "p304"
  source_quote: |
    "-> ip interface "spb-mgmt" address 172.30.1.x/24 vlan 2000
    -> ping 192.168.100.107 (OV)
    -> ip static-route 0.0.0.0/0 gateway 192.168.100.108 metric 2
    -> aaa authentication snmp local
    -> user snmpuser password "Superuser=1" read-write all no auth
    -> snmp security no-security
    -> snmp community-map public user snmpuser enable
    -> snmp station 192.168.100.107 snmpuser v2 enable
    -> Network -> Managed Devices -> Discover New Devices (Start IP: 172.30.1.1 End IP: 172.30.1.8)
    -> Network -> Topology -> Map Level Action -> SPB Network -> Poll Latest Data"
  summary: |
    OV2500 编排全流程命令化样例：①SPB 侧带内管理——每台交换机控制 BVLAN 2000 上建 spb-mgmt 接口（172.30.1.x），Sw1 加默认静态路由到防火墙；②SNMP 六条命令（本地认证/读写用户/no-security/community-map/station/trap absorption）；③OV 侧从 OV-init 快照开机、改密、lds.al-enterprise.com 生成 EVAL-OV2500 License（Customer ID 99999 / Order Number evaluation / Passcode omnivista，90 天）导入；④按 172.30.1.1-8 建发现范围跑 Discover Now；⑤Topology→SPB Network→Poll Latest Data 查看多 BVLAN 拓扑。
  tags: [lab, ov2500, in-band-management, snmp, discovery, license, day3]

- id: c17
  title: Lab10——混合接入端口 + E-Tree 客户隔离
  type: case
  source_chapter: "p328"
  source_quote: |
    "-> service access port 1/1/3 hybrid enable
    -> service spb 2002 sap port 1/1/3:2 admin-state enable stats enable
    (E-Tree)
    -> spb bvlan 2001 admin-state enable / -> spb bvlan 2004 admin-state enable
    -> spb isis bvlan 2001 ect-id 1 / -> spb isis bvlan 2004 ect-id 4
    -> spb isis control-bvlan 2001 / -> spb isis interface port 1/1/5-6 / -> spb isis admin-state enable
    -> service access port 1/1/3
    -> service 2004 spb isid 2004 bvlan 2004 description vlan4 e-tree enable
    -> service 2004 sap port 1/1/3:4 stats enable
    BEB3 -> service 2004 spb isid 2004 bvlan 2004 description vlan4 admin-state enable"
  summary: |
    两个 Day3 特性的落地序列：①混合端口——接入交换机 VLAN3 走桥接域、VLAN2 走服务域，BEB 上 service access port 1/1/3 hybrid enable 后同一口同时承载 VLAN 3 桥接与 SAP 2002 sap port 1/1/3:2；②E-Tree——Sw1/Sw8（Leaf 侧）用 service 2004 ... e-tree enable 建 E-Tree 服务（SAP 全 Leaf，Client5↔Client6 相互隔离），Sw7（Root 侧）同 I-SID 2004 但建成普通 E-LAN 服务（无 e-tree 选项）做根，Client3（挂 Root）可与两端互通。验证 show spb isis services + ping 矩阵（Leaf↔Leaf 断、Leaf↔Root 通）。
  tags: [lab, hybrid-port, e-tree, leaf, root, isolation, day3]

- id: c18
  title: 老硬件 Outline 路由——物理回环口与面板口回环模式配置
  type: case
  source_chapter: "p352"
  source_quote: |
    "物理回环（两个物理口对接）:
    -> vlan 500
    -> vlan 500 members port 1/1/11 tagged
    -> vrf default ip interface l3vpn1 address 10.5.1.1/24 vlan 500
    -> spb bvlan 4001
    -> service spb 10 spb isid 1000 bvlan 4001 admin-state enable
    -> service access port 1/1/12
    -> service spb 10 sap port 1/1/12:500
    面板口回环模式（单口）:
    -> interfaces port 1/1/18 loopback
    -> service access port 1/1/18 vlan-xlation enable
    -> service 10 spb isid 1000 bvlan 500 vlan-xlation enable
    -> service 10 sap port 1/1/18:200
    -> ip interface L3VPN address 10.10.10.1/24 rtr-port port 1/1/18 tagged vlan 200"
  summary: |
    不支持单遍内联的老平台（OS6900-X20/T20/Q32/X72、6860/E 等，p348-349）实现 IP over SPB 的两种回环法：①双物理口对接——一口做 VRF 路由口（VLAN 500 tagged + vrf ip interface），另一口做 SAP 侧（service access port + sap port :500），VLAN ID 协调 VRF↔I-SID 映射；②单面板口回环模式——interfaces port 1/1/18 loopback 后同一口既属 L3 VPN VLAN 又做 access 口，IP 接口用 rtr-port port 1/1/18 tagged vlan 200 形式绑定（IPv6 同理 ipv6 interface ... rtr-port），必须开 vlan-xlation，多口可组静态回环 linkagg 做冗余提速。
  tags: [outline-routing, loopback, legacy-hardware, rtr-port, l3vpn]
```
