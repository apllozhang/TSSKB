# cases.md · OmniSwitch LAN MPLS Concepts & Implementation (DT00XTE324EN)
# 来源: D:\Claude code\TSSKB\books\os-lan-mpls-impl (153 页教材，p115-146 为 Reference Design Guide)

- id: c01
  title: Lab 1：四台 OS6860 部署 MPLS 骨干（VLAN+OSPF+许可+LDP 全流程）
  type: case
  source_chapter: "p83-96"
  source_quote: |
    "sw7 (6860-A) -> vlan 79 mtu-ip 4094
    sw7 (6860-A) -> vlan 79 members port 1/1/30 untagged
    sw7 (6860-A) -> ip interface "int_79" address 172.16.79.7/24 vlan 79
    sw7 (6860-A) -> ip interface Loopback0 address 192.168.254.7
    sw7 (6860-A) -> ip ospf interface "int_79" type point-to-point
    sw7 (6860-A) -> mpls load ldp
    sw7 (6860-A) -> mpls ldp admin-state enable
    sw7 (6860-A) -> mpls interface "int_79" admin-state enable
    sw7 (6860-A) -> mpls ldp interface "int_79" admin-state enable"
  summary: |
    拓扑：sw7/sw8/sw9/sw10 四台 6860 组成环形骨干，互联链路用 VLAN 70/79/80/89/90（172.16.x.0/24），每台配 Loopback0=192.168.254.{7-10}。步骤：建骨干 VLAN（mtu-ip 4094）并挂 untagged 端口→配 IP 接口→ping 验证→OSPF area 0.0.0.0（接口 type point-to-point + bfd-state enable）→确认 MPLS 包已装（show pkgmgr）→配置 SILOS 许可服务器（license server ... listen-port 8883）与各交换机 SWLIC 客户端（license client site-id Master server-ip ...）→mpls load ldp 全局使能→接口级 mpls interface + mpls ldp interface 使能。验证：show mpls ldp session 双邻居 OPERATIONAL、forwarding-table 中直连网段 Out-Label=3（impl-null/PHP）、远端 loopback 有 52480+ 标签、等价路径出现两条（+ 标记 ECMP）。最后 write memory flash-synchro 并备份 vcboot.cfg/vcsetup.cfg 到 labMpls 目录。
  tags: [Lab, MPLS骨干, 6860, OSPF, LDP, 许可, ECMP]

- id: c02
  title: Lab 2：VPLS-LDP 信令部署（服务/SDP/SAP/vlan-xlation/弹性测试）
  type: case
  source_chapter: "p97-105"
  source_quote: |
    "service 2 vpls vplsid 200 signaling ldp description "vpls service with LDP signaling" admin-state enable
    sw7 (6860-A) -> service sdp 78 vpls far-end 192.168.254.8 description "VPLS Peer for ldp signaling"
    sw8 (6860-B) -> service sdp 78 vpls far-end 192.168.254.7
    sw7 (6860-A) -> service 2 bind-sdp 78 description "Bind to SDP 78 for service 2"
    sw7 (6860-A) -> service access port 1/1/3
    sw7 (6860-A) -> service 2 sap port 1/1/3:2
    sw7 (6860-A) -> service 2 vlan-xlation enable
    sw7 (6860-A) -> service access port 1/1/3 vlan-xlation enable"
  summary: |
    在 Lab 1 骨干上叠加两个 VPLS（服务 2/vplsid 200 对应 VLAN2，服务 3/vplsid 300 对应 VLAN3）。PE 侧：sw7/sw8 各建服务→SDP 78 互指对端 loopback→bind-sdp 绑定两个服务→access port + SAP（port:vlan 形式，如 1/1/3:2；untagged 用 :0 如 sw8 的 1/1/1:0）。CE 侧（6360-A/B、6560-A）只做普通二层：VLAN 2/3 + tagged 上联口 + 本地 vlan2/vlan3 三层接口作网关。客户端 3/5/6/8/9/10 配 IP 后验证：show mac-learning domain vpls 在 sw7 看到本端 sap:1/1/3:2 学到的 MAC 与远端经 sdp:78:2 学到的 MAC；sw9/sw10（P 节点）该表为空。连通故障时补两端 vlan-xlation（服务级+端口级）恢复。弹性测试：client 9↔8 连续 ping 期间断开/恢复 sw7 的 1/1/29 与 1/1/30，观察是否有丢包（骨干双路径 ECMP）。
  tags: [Lab, VPLS, LDP, SDP, SAP, vlan-xlation, 弹性测试]

- id: c03
  title: Lab 3：VPLS-BGP 信令部署（IBGP 邻居 + ve-id 自动发现）
  type: case
  source_chapter: "p106-114"
  source_quote: |
    "cp labMpls/vcboot.cfg working
    reload from working no rollback-timeout
    sw7 (6860-A) -> ip bgp autonomous-system 65724
    sw7 (6860-A) -> ip bgp address-family l2vpn-vpls
    sw7 (6860-A) -> ip bgp neighbor 192.168.254.8 remote-as 65724
    sw7 (6860-A) -> ip bgp neighbor 192.168.254.8 update-source Loopback0
    sw7 (6860-A) -> ip bgp neighbor 192.168.254.8 activate l2vpn-vpls
    service 2 vpls vplsid 200 signaling bgp ve-id 1 description "VPLS instance 200 with bgp signaling" admin-state enable"
  summary: |
    先从 Lab 1 备份恢复骨干配置（cp labMpls/* working + reload from working no rollback-timeout），CE 配置保留。PE 侧 sw7/sw8 各配 IBGP（同 AS 65724、互指 loopback、update-source Loopback0、activate l2vpn-vpls），show ip bgp neighbors 确认 established。服务定义换成 signaling bgp 并带 ve-id（sw7 全部用 ve-id 1，sw8 用 ve-id 2），无需手工 SDP/bind-sdp——BGP 自动发现生成伪线，MAC 表中远端接口显示 sdp:32768:2/3。sh service 2 输出可核对：Signaling=BGP、SAP Count、SDP Bind Count、Vlan Translation=Yes、MTU=1500。客户端测试与 Lab 2 相同（跨 site ping、按 MAC 定位 sap/sdp 接口）。
  tags: [Lab, VPLS, BGP, ve-id, 自动发现, l2vpn-vpls]

- id: c04
  title: R-Lab 远程实验室 POD 拓扑（8 交换机 + 10 VM + 服务器群）
  type: case
  source_chapter: "p16-19"
  source_quote: |
    "6900-A EMP 10.4.Pod#.1
    6900-B EMP 10.4.Pod#.2
    6560-A EMP 10.4.Pod#.3
    6360-A EMP 10.4.Pod#.5
    6860-A EMP 10.4.100+Pod#.7
    6860-B EMP 10.4.100+Pod#.8
    • 10 VM (Clients)
    • DHCP Server, Radius Server: 192.168.100.102
    • OmniVista 2500: 192.168.100.107"
  summary: |
    每个 POD 的物理资源：8 台交换机——6900-A/B（核心，型号 6900T24C2 或 6900T20）、6560-A、6360-A/B（接入）、6860-A/B（MPLS 实验骨干，编号 sw7/sw8）；另有 10 台 VM 客户端、AAA/DHCP/RADIUS/Web/FTP 服务器（192.168.100.102）、OmniVista 2500（192.168.100.107）、pfSense 防火墙/NAT（192.168.100.108）。EMP 带外管理地址按表分配（6860 用 10.4.100+Pod#.x 段）。接入方式：浏览器 RDP（https://rdp.al-mydemo.com/），账号 LanpodXa/Xb。三个 MPLS Lab 均在此环境执行，Lab 中 sw7/sw8=6860-A/B、sw5/sw6=6360-A/B、sw3=6560-A、sw9/sw10=6860-C/D 扩展节点。
  tags: [R-Lab, 拓扑, POD, 实验环境, OmniVista]

- id: c05
  title: Reference Design 样例：LDP 骨干 + T-LDP VPLS 规范化配置（R1 视角）
  type: case
  source_chapter: "p136-138"
  source_quote: |
    "-> ip interface Loopback0 address 1.1.1.1/32
    -> ip interface IFtoR2 address 10.1.2.1/24 vlan 12 rtr-port port 1/1/1 tagged
    -> ip ospf interface IFtoR2 type point-to-point
    -> pkgmgr install uosn-mpls-v1.deb
    -> mpls ldp interface IFtoR2 admin-state enable
    -> service sdp 102 vpls far-end 1.1.1.6
    -> service sdp 103 vpls far-end 1.1.1.7
    -> service 1 vpls vplsid 100 signaling ldp
    -> service 1 vlan-xlation enable
    -> service 1 sap port 1/1/4:0
    -> service 1 bind-sdp 102 103"
  summary: |
    参考设计指南的标准化配置（比 Lab 更规范，可直接做项目模板）：loopback 用 /32（1.1.1.1，兼作 router-id：ip router router-id 1.1.1.1）；互联接口用 rtr-port tagged 路由端口（对照最佳实践"use routed interfaces"）；ip bfd admin-state enable 全局 + OSPF 接口 bfd-state enable；MPLS 接口与 LDP 接口逐个使能；VPLS 侧 service+vlan-xlation+SAP(:0 untagged)+对每个远端 LER 建 SDP（102/103 指向 1.1.1.6/1.1.1.7）并一次 bind-sdp 102 103 绑两条。教材注明：业务配置只做在建立全网状伪线的 PE/LER 节点（示例拓扑中为 R1/R6/R7）。
  tags: [ReferenceDesign, 配置模板, rtr-port, T-LDP, VPLS-LDP]

- id: c06
  title: Reference Design 样例：BGP VPLS 规范化配置（R1 视角）
  type: case
  source_chapter: "p138-139"
  source_quote: |
    "-> ip load bgp
    -> ip bgp mpls
    -> ip bgp autonomous-system 65724
    -> ip bgp address-family l2vpn-vpls
    -> ip bgp neighbor 1.1.1.6 remote-as 65724
    -> ip bgp neighbor 1.1.1.6 update-source "Loopback0"
    -> ip bgp neighbor 1.1.1.6 activate l2vpn-vpls
    -> ip bgp neighbor 1.1.1.7 activate l2vpn-vpls
    -> ip bgp admin-state enable
    -> service 2 vpls vplsid 11 signaling bgp ve-id 1
    -> service 2 vlan-xlation enable
    -> service 2 sap port 1/1/4:0"
  summary: |
    BGP VPLS 标准序列，与 Lab 3 的差异点：参考设计样例多了 ip bgp mpls 一条全局命令；每个远端 PE（1.1.1.6、1.1.1.7）都要建邻居并 activate l2vpn-vpls（AOS 不支持 RR，只能全互联）；服务定义 signaling bgp ve-id 1，之后同样 vlan-xlation + SAP，全程无手工 SDP。此配置同样只落在 PE/LER（R1/R6/R7）。可直接作为多站点 BGP VPLS 交付的 CLI 清单模板。
  tags: [ReferenceDesign, 配置模板, BGP-VPLS, ip-bgp-mpls, 全互联]

- id: c07
  title: SDP 复用样例：一服务多 SDP 与一 SDP 多服务
  type: case
  source_chapter: "p78"
  source_quote: |
    "-> service sdp 20 vpls far-end 10.10.10.2 description "VPLS Peer for ldp signaling"
    -> service sdp 30 vpls far-end 20.20.20.2
    -> service 1 bind-sdp 20 description "Bind to SDP 20 for service 1"
    -> service 1 bind-sdp 30 description "Bind to SDP 30 for service 1"
    -> service 2 vpls vplsid 2000 signaling ldp admin-state enable
    -> service 1 bind-sdp 20
    -> service 2 bind-sdp 20"
  summary: |
    教材"其他配置样例"页给出两种复用形态：1) 一个 VPLS 服务绑多条 SDP（service 1 同时 bind-sdp 20/30，指向两个远端 10.10.10.2、20.20.20.2），实现多站点全网状；2) 一条 SDP 被多个 VPLS 服务复用（SDP 20 同时绑定 service 1 和 service 2），即同一对 PE 间跑多个 VPLS 只需一条 T-LDP 会话承载多个 VC。规划 SDP 编号与复用关系时参考。
  tags: [SDP, bind-sdp, 复用, 多站点, VPLS-LDP]

- id: c08
  title: Reference Design 场景：中小企业园区 MPLS 端到端
  type: case
  source_chapter: "p133 (Figure 7)"
  source_quote: |
    "AOS implmentation of IP/MPLS is best suited for enterprise and metro ethernet customers such as smart city networks. It provides a very cost-effective solution.
    Enterprise Campus Networks
    A two or three-tier architecture for a small and medium campus networks is best suited. It will provide VPN services end-to-end and IP/MPLS will be implemented from the access to the core layer."
  summary: |
    场景模板一（配 Figure 7 架构图）：中小园区网络采用二层或三层架构，IP/MPLS 从接入层一直实施到核心层，端到端提供 VPN 业务。适用判断：客户需要在园区内隔离多个业务/租户（VPLS L2 VPN）、且愿意全网统一 MPLS 管理域时选此模板；配合 c05/c06 的配置模板即可出方案。AOS 定位强调"性价比"（cost-effective）。
  tags: [ReferenceDesign, 园区网, 端到端VPN, 场景模板]

- id: c09
  title: Reference Design 场景：城域以太网/智能城市三层架构
  type: case
  source_chapter: "p133-134 (Figure 8)"
  source_quote: |
    "Metro Ethernet Networks (Smart City)
    For metro ethernet networks such as smart city networks, IP/MPLS network can be configured at the core and distribution layers of a three-tier network architecture. At the access layer, ethernet standard switching will be configured."
  summary: |
    场景模板二（配 Figure 8 架构图）：城域以太网（典型如智能城市）采用三层网络架构，核心层与汇聚层配置 IP/MPLS，接入层保持标准以太交换。与园区模板的差异：MPLS 域收敛到核心+汇聚，接入不跑 MPLS（成本与复杂度控制），业务通过汇聚层 PE 的 SAP/SAP:VLAN 接入 VPLS。售前面向城域/智慧城市项目时用此模板界定 MPLS 域边界。
  tags: [ReferenceDesign, 城域以太网, 智能城市, 三层架构, 场景模板]
