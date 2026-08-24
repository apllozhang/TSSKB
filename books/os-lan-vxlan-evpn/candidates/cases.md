# cases.md · Lab / 配置案例提取
# 来源: OmniSwitch LAN VxLAN/EVPN Concepts & Implementation (DT00XTE325EN, Edition 01)
# 规则: 每条含原文引用与页码；CLI 命令保留原文；宁多勿漏，待后续独立验证阶段筛选

```yaml
- id: c01
  title: Lab1——OSPF Underlay + iBGP Overlay 从零搭建（2 Spine + 2 Leaf）
  type: case
  source_chapter: "p78-86"
  source_quote: |
    [互联规划表 p78] VLAN 110 Spine1-Spine2 172.16.110.0/24 1/1/25 / 101 Spine1-Leaf1 172.16.101.0/24 1/1/27 / 102 Spine1-Leaf2 172.16.102.0/24 1/1/28 / 111 Spine2-Leaf1 ... / 112 Spine2-Leaf2 ...
    sw10 (Spine-1) -> ip interface "Loopback0" address 1.1.1.10
    sw10 (Spine-1) -> ip router router-id 1.1.1.10
    sw10 (Spine-1) -> ip interface "vl101" address 172.16.101.10/24 vlan 101 rtr-port port 1/1/27 tagged
    sw10 (Spine-1) -> ip bfd transmit 200 / receive 200 / echo-interval 200
    sw10 (Spine-1) -> ip ospf interface "vl101" type point-to-point / bfd-state enable
    sw10 (Spine-1) -> ip ospf spf-timer delay 0 / hold 0
    sw1 (Leaf_1) -> ip load bgp / ip bgp autonomous-system 65000 / ip bgp address-family evpn
    sw1 (Leaf_1) -> ip bgp neighbor 1.1.1.10 remote-as 65000 / update-source Loopback0 / activate-evpn
  summary: |
    四节点 fabric 底座完整流程（p78-86）：①互联规划表——VLAN110(S1-S2)/101/102(S1-L1/L2)/111/112(S2-L1/L2)，子网 172.16.1xy.0/24，两端口号对称（p78）；②每台先 session cli timeout 200 / session prompt / system name 定制，再配 Loopback0（sw10=1.1.1.10、sw11=1.1.1.11、sw1=1.1.1.1、sw2=1.1.1.2）兼做 OSPF/BGP router-id（p78-79）；③互联口 router VLAN 口 + BFD 200ms + OSPF p2p + bfd-state + SPF 0/0（p80-82 全四台 CLI）；④overlay 全网 AS65000，每台与其余三台 Loopback 建 iBGP EVPN 会话（p85-86）。验证链：sh ip ospf neighbor 全 Full（p82）→ sh ip routes 看 Leaf 双等价路径（ECMP + 标记，p83-84）→ show ip bgp neighbors established + evpn advertised（p85-86）。
  tags: [lab, part1, ospf, underlay, bgp, overlay, ibgp, bfd, spine, leaf]

- id: c02
  title: Lab2——EVPN-VXLAN 业务五步开通 + Spine dummy 口补实例化
  type: case
  source_chapter: "p102-108"
  source_quote: |
    sw1 (Leaf_1) -> interfaces 1/1/7 admin-state enable
    sw1 (Leaf_1) -> service access port 1/1/7 evpn-ethernet-segment enable
    sw1 (Leaf_1) -> service 100 vxlan vnid 1000 bgp-evpn enable
    sw1 (Leaf_1) -> service 200 vxlan vnid 2000 bgp-evpn enable
    -> service 100 sap port 1/1/7:10
    -> service 200 sap port 1/1/7:20
    sw10 (Spine-1) -> service access port 1/1/24 evpn-ethernet-segment enable
    sw10 (Spine-1) -> service 100 vxlan vnid 1000 bgp-evpn enable
    sw10 (Spine-1) -> service 100 sap port 1/1/24:10
  summary: |
    双 Leaf 开两条 L2 业务：service 100/VNI 1000（VLAN10）与 service 200/VNI 2000（VLAN20），单归属口 1/1/7 收两个 tagged VLAN（SAP 1/1/7:10 与 1/1/7:20，ETag=VLAN 号）。非对称 IRB 前提 Spine 也用 dummy 口 1/1/24 补建同样两条（p105-106）。验证五连（p103-108）：show service evpn（双业务 Up，SAP/Bind Count=1；Spine 初始 Total Services: 0）；show service evpn ethernet-segment（本地 SH[L-A] + 远端 SH[R]，RT/EVI Count=2）；debug evpn show bgp route-type rt3（4 条 IMET=2 EVI×2 Leaf）；ethernet-segment <esi> sap-info（ETag-EVI 映射 10↔1000、20↔2000）；evi 1000 tunnel-ports（动态 SDP 32768:100，远端 1.1.1.2）。注意对远端 ES 执行 sap-info 会报错（p107，见 ce05）。
  tags: [lab, part2, provisioning, service, sap, vnid, dummy-port, verification, rt3]

- id: c03
  title: Lab2——非对称 IRB + DAG + Proxy ARP + CE 侧与客户端配置
  type: case
  source_chapter: "p109-117"
  source_quote: |
    sw1 (Leaf_1) -> ip interface leaf1svc100 service 100 address 192.168.10.1/24
    sw1 (Leaf_1) -> ip interface leaf1svc200 service 200 address 192.168.20.1/24
    sw2 (Leaf_2) -> ip interface leaf2svc100 service 100 address 192.168.10.2/24
    sw1 (Leaf_1) -> ip anycast-gateway-mac auto
    sw1 (Leaf_1) -> ip interface leaf1svc100 anycast-gateway-address 192.168.10.254
    sw1 (Leaf_1) -> ip interface leaf1svc200 anycast-gateway-address 192.168.20.254
    sw5 (CE-1) -> vlan 10 members port 1/1/1 untagged
    sw5 (CE-1) -> vlan 10 members port 1/1/7 tagged
  summary: |
    三层叠加案例（p109-117）：①IRB——每业务挂一个 ip interface service <id>，Leaf1 用 .1、Leaf2 用 .2 各自独立主机地址（非 anycast 部分）；②DAG——ip anycast-gateway-mac auto + 每 IRB 口 anycast-gateway-address .254，两 Leaf 网关 IP/虚拟 MAC 完全一致，sh ip interface 出现 A=Anycast IP 标志（p109）；③CE 侧——sw5/sw6 建 vlan 10/20，主机口 1/1/1、1/1/2 untagged，上联 1/1/7 双 tagged（p111-112）；客户端参数：client5 192.168.10.50/24 GW 192.168.10.254 DNS 10.0.0.51（p112；注意 p113 client9/10 的网关原文误写 192.168.30.254，见 ce07）。验证：show service 100 proxy-arp config 四参数；sh ip evpn proxy-arp evi 1000 出本地表项（192.168.10.50↔bc:24:11:dd:29:a9）；client5 ping client6 同子网、ping client10 跨子网；sh mac-learning evpn-vxlan 看 sap/sdp 表项；Spine 的 evpn-vxlan MAC 表为 0（不学主机 MAC，p115-116）；RT2 表含 MAC+IP 双条目（p117）。
  tags: [lab, part2, irb, asymmetric, dag, anycast, proxy-arp, ce-config, verification]

- id: c04
  title: Lab3——动态 LACP 跨设备多归属（single-active）与故障切换演练
  type: case
  source_chapter: "p153-156"
  source_quote: |
    sw1 (Leaf_1) -> linkagg lacp agg 3 size 2 admin-state enable
    sw1 (Leaf_1) -> linkagg lacp agg 3 actor admin-key 3
    sw1 (Leaf_1) -> linkagg lacp port 1/1/3 actor admin-key 3
    sw1 (Leaf_1) -> service access linkagg 3 evpn-ethernet-segment enable
    sw1 (Leaf_1) -> service 100 sap linkagg 3:10
    sw3 (CE_2) -> linkagg lacp port 1/1/3 actor admin-key 3
    sw3 (CE_2) -> linkagg lacp port 1/1/4 actor admin-key 3
    sw3 (CE_2) -> vlan 10 members linkagg 3 tagged
    • Disable the port 1/1/3 on leaf_1. Ping still working.
  summary: |
    CE-2 双归 Leaf1（1/1/3）+Leaf2（1/1/4）的跨设备动态 LACP：两 Leaf 各建 agg 3（actor admin-key 3），CE 侧同一个 agg 3 挂两口；service access linkagg 3 evpn-ethernet-segment enable 后自动生成 MH-SA 的 ESI 03:2c:fa:a2:a2:f2:ad:00:03:00（CE-MAC+Key-Id 编码）。初始状态 sw1 为 MH-SA[L-A] 且 sap-info 中 1.1.1.1 带 * 号=DF，sw2 侧为 Remote-ES（p154）。切换演练（p155-156）：断开 Leaf1 的 1/1/3 后链路转 CONFIGURED/DOWN，ES 角色翻转——sw2 变 MH-SA[L-A]、sw1 变 Remote；client3↔client5 的永久 ping 不中断；MAC 表迁到 sap:0/3@1.1.1.2（sw2 视图，p156）。sh linkagg port 状态机：ATTACHED/RESERVED→故障侧 CONFIGURED。
  tags: [lab, part3, lacp, mlag, multihoming, single-active, esi, df, failover]

- id: c05
  title: Lab3——静态链路聚合手工 ESI 多归属
  type: case
  source_chapter: "p156-158"
  source_quote: |
    • Since we are using static link aggregation on LEAF-1 we will define the ESI ID.
    • On a static lingkagg, ESI has to be provided for an Ethernet segment
    sw1 (Leaf_1) -> linkagg static agg 7 size 2
    sw1 (Leaf_1) -> linkagg static port 1/1/5 agg 7
    sw7 (CE-4) -> vlan 20 members linkagg 7 tagged
    sw7 (CE-4) -> vlan 20 members port 1/1/1 untagged
    sw1 (Leaf_1) -> service access linkagg 7 evpn-ethernet-segment enable esi 01:01:01:02:04
    sw1 (Leaf_1) -> service 200 sap linkagg 7:20
  summary: |
    静态聚合场景：Leaf-1 与 CE-4 各配 linkagg static agg 7（CE 侧 1/1/5-6 两口），启用 ES 时必须显式带 esi 01:01:01:02:04（静态 LAG 无自动 ESI）。系统呈现为 MH-SA[L-M]（M=Manual），完整 ESI 显示 03:a1:01:01:01:02:04:ff:ff:01（p157）。业务挂 SAP linkagg 7:20（service 200/VNI 2000/VLAN20）；client7 192.168.20.70/24 GW 192.168.20.254（p156）。验证：show service evpn ethernet-segment 出现新 ES 条目（0/7 接口）；sw1 的 sh mac-learning evpn-vxlan 出现经 sap:0/7 学习的 client7 MAC（200:2000 行）；sw2 侧同一 MAC 经 sdp:32768 学到；client7 ping client5/6 跨 VNI 互通（p157-158）。
  tags: [lab, part3, static-lag, manual-esi, multihoming, provisioning, verification]

- id: c06
  title: 架构指南——2 Spine + 4 Leaf 参考设计（underlay/overlay 全量配置）
  type: case
  source_chapter: "p187-197"
  source_quote: |
    [规划表 p188] VLAN 100 SPINE-1/2 100.100.100.0/24; v11-14 SPINE-1→LEAF-1..4 11-14.x; v21-24 SPINE-2→LEAF-1..4
    SPINE-1: ip interface "Loopback0" address 1.1.1.1
    ip interface "v11" address 11.11.11.1/24 vlan 11 rtr-port port 1/1/50A tagged
    ip bfd transmit 200 / receive 200 / echo-interval 200
    debug ip ospf set subsecond 1 / debug ip ospf set bfdsubsecond 1
    ip bgp autonomous-system 65000 / ip bgp address-family evpn
    ip bgp neighbor 1.1.1.2 remote-as 65000 / update-source Loopback0 / activate-evpn
  summary: |
    设计文档级完整参考（p187-197）：6 节点 fabric——SPINE-1=1.1.1.1、SPINE-2=1.1.1.2、LEAF-1..4=1.1.1.10/20/30/40；互联子网 v100(S-S)、v11-v14(S1-L1..4)、v21-v24(S2-L1..4) 每链路独立 /24（p188）。与课堂 Lab 的差异点：rtr-port 挂聚合口 1/1/49A-53A tagged；OSPF 加 debug ip ospf set subsecond 1 / bfdsubsecond 1 亚秒级；BGP overlay 每台与其余 5 台全互联 iBGP EVPN（6 台×5 邻居，p193-197）。主机规划表（p187）：VLAN10 VM1/3/5=192.168.10.10/20/30、VLAN20 VM2/4/6=192.168.20.10/20/30，网关统一 .254。验证 show ip bgp neighbors 全 established（p197）。
  tags: [architecture-guide, reference-design, underlay, overlay, ospf, bgp, 6-node, subsecond]

- id: c07
  title: 架构指南——业务开通/IRB/DAG/Proxy ARP/MAC mobility 收尾全套
  type: case
  source_chapter: "p198-204"
  source_quote: |
    SPINE-1: service access port 1/1/48 evpn-ethernet-segment enable
    service 100 vxlan vnid 1000 bgp-evpn enable
    service 100 sap port 1/1/48:10
    LEAF-4: service access linkagg 30 evpn-ethernet-segment enable esi 01:01:01:02:04
    ip interface leaf4svc100 service 100 address 192.168.10.4/24
    ip anycast-gateway-mac auto
    ip interface leaf4svc100 anycast-gateway-address 192.168.10.254
    > service bgp-evpn mac-mobility loop-protection {enable | disable} (retry-time [seconds] | threshold [count] | timeout [seconds])
  summary: |
    参考设计后半段（p198-204）：①Spine 用 dummy 口 1/1/48 建两条业务（非对称 IRB 全实例化）；②接入分工——LEAF-1 物理口 1/1/1 + 动态 agg 20 双接入、LEAF-2/3 仅 agg 20（三 Leaf 共享一个 MH-ES，Peer-VTEP-List 1.1.1.10/20/30）、LEAF-4 静态 agg 30 手工 ESI；③IRB——4 台 Leaf 每业务一个 ip interface（.1-.4 各自不同）；④DAG——全部 Leaf anycast-gateway-mac auto + 两业务 .254；⑤MAC mobility 全局启用 loop-protection（带 retry-time/threshold/timeout）。验证命令全集（p199-205）：show service evpn / ethernet-segment / <esi> sap-info / carving-info / aliasing-info、show service X proxy-arp config、show ip evpn proxy-arp evi/summary、show mac-learning evpn-vxlan、debug evpn show bgp route-type rt1a|rt1b|rt2|rt3|rt4。
  tags: [architecture-guide, provisioning, irb, dag, mac-mobility, verification-commands]

- id: c08
  title: 课堂演示——单业务（service 100/VNI 1000）端到端最小验证链
  type: case
  source_chapter: "p64-74"
  source_quote: |
    -> interfaces 1/1/7 admin-state enable
    -> service access port 1/1/7 evpn-ethernet-segment enable
    -> service 100 vxlan vnid 1000 bgp-evpn enable
    -> service 100 sap port 1/1/7:10
    sw2 (Leaf_2) -> debug evpn show bgp route-type rt3 [两侧各含 1.1.1.1 与 1.1.1.2 两条]
    sw1 (Leaf_1) -> sh mac-learning evpn-vxlan [sap:1/1/7 学本地 CE，sdp:32768 学远端]
    sw1 (Leaf_1) -> sh service evpn evi 1000 tunnel-ports ... Sdp-Id 32768:100 Far-End-Info 1.1.1.2
  summary: |
    Part1 课堂把五步法浓缩成两 Leaf 间最小可验证流（p64-74）：Leaf1 依次启用 access port/业务/SAP 后，show service 显示 Adm Up 但 Oper Down（对端未配，单边状态）；对端 Leaf2 配同样三条后——RT3 互收（debug evpn show bgp route-type rt3 双方各见 1.1.1.1/1.1.1.2 两条 VXLAN 封装路由，Encap=12）；MAC 表 sap 学本地 CE MAC、sdp:32768 学远端 MAC（sh mac-learning evpn-vxlan 的 [SvcId:Evi] 100:1000 行）；tunnel-ports 显示动态 SDP 32768:100 建到远端 1.1.1.1/1.1.1.2，业务 Oper 转 Up（p74）。适合直接当开局 checklist：一条业务不通时按"ES→service→SAP→RT3→MAC→SDP 隧道"顺序逐层核对。
  tags: [demo, part1, minimal-config, verification, rt3, mac-learning, sdp, troubleshooting-flow]

- id: c09
  title: 架构指南——三 Leaf 共享 ES 的 DF 选举与 aliasing 验证场景
  type: case
  source_chapter: "p200-201"
  source_quote: |
    > show service evpn ethernet-segment 03:78:24:59:55:25:e6:ff:ff:ff sap-info
    Etag-Value RT [EVI] Adm Oper PE(s)
    10 1000 Up Up 1.1.1.10*
    20 2000 Up Up 1.1.1.10*
    > show service evpn ethernet-segment 03:2c:fa:a2:c0:d4:d3:00:14:00 carving-info
    EVI DF nDFs
    1000 1.1.1.10 1.1.1.20,1.1.1.30
    2000 1.1.1.20 1.1.1.10,1.1.1.30
    > show service evpn ethernet-segment 03:78:24:59:64:69:98:ff:ff:ff aliasing-info
    EVI ETAGS Primary Backup Others
    1000 10,20 1.1.1.10 1.1.1.20 1.1.1.30
  summary: |
    多归属控制面三视图验证（p200-201）：本地单归属 ES 用 sap-info——ETag↔EVI 映射表，PE(s) 列带 * 号者为 DF（Legend "*: DF Node"，另有 "#: Missing ETAG configuration between Peer-PE nodes" 提示对端 ETag 缺配）；本地多归属 ES 用 carving-info——展示 service carving 结果，EVI 1000 的 DF=1.1.1.10、EVI 2000 的 DF=1.1.1.20（不同 EVI 分摊到不同 PE，mod 算法效果），nDFs 列出非 DF；远端 ES 用 aliasing-info——Primary/Backup/Others 支撑负载分担与快速切换。三条命令本地/远端各有适用对象，用错即报 Not supported（p107/p155）。
  tags: [architecture-guide, df, carving, aliasing, verification, multihoming, etag]
```
