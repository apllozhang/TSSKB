# counter-examples.md · 陷阱 / 警告 / 反例提取
# 来源: OmniSwitch LAN VxLAN/EVPN Concepts & Implementation (DT00XTE325EN, Edition 01)
# 规则: 每条含原文引用与页码；宁多勿漏，待后续独立验证阶段筛选

```yaml
- id: ce01
  title: 陷阱——非对称 IRB 下 Spine 漏配业务，必须用 dummy 口补实例化
  type: counter-example
  source_chapter: "p105"
  source_quote: |
    Since we will be using asymmetric IRB in this configuration example, it is required to have all the services instantiated in all the switches and to have an operational physical or logical port provisioned for all services.
    Since we do not have all the services enabled on Spine switches, we will use a dummy operational port "1/1/24" for that purpose.
  summary: |
    非对称 IRB 的隐含成本：每个 EVI 必须在所有交换机（含 Spine）实例化且要有 operational 端口。Spine 本没有业务口，教材用 dummy 口占位（Lab 用 1/1/24，p105-106；架构指南用 1/1/48，p198 且原文注明"The service configuration for the dummy port has been highlighted in red"）。忘配的直接后果：Spine 上业务缺失，IRB 全网路由上下文不完整。规避方案：对称 IRB 无此要求（业务只配有主机的 PE，p179），但 8.10R1 不支持——见 ce02。
  tags: [asymmetric-irb, dummy-port, spine, instantiation, pitfall]

- id: ce02
  title: 陷阱——8.10R1 首版四项功能边界（RT5 / 对称 IRB / tandem 复制 / all-active 均不支持）
  type: counter-example
  source_chapter: "p173, p179, p180, p182"
  source_quote: |
    [p173] R-T5 will not be supported in the initial release 8.10R1 of BGP-EVPN and will be supported in a future release.
    [p179] Symmetric IRB will not be supported in the initial release 8.10R1 of BGP-EVPN and will be supported in a future release.
    [p180] Only ingress (head-end) replication is supported in the initial release 8.10R1
    [p182] All-active will not be supported in the initial release 8.10R1 of BGP-EVPN and will be supported in a future release.
  summary: |
    售前/交付核对表：MP-BGP EVPN 首个支持版本为 8.10R1、仅 OS6900 平台（p163）；首版不支持——①RT5 IP 前缀路由（L3VPN/外联 summarization）；②对称 IRB（含 fabric-vpn 服务那套，p97 只是配置入口示意）；③组播 tandem 复制（BUM 只能 ingress replication）；④all-active 多归属（只能 single-active）。客户要其中任一项就得改方案或等版本。另注意：培训环境是 8.10R2（p48），且 8.10R1 的能力表在后续 release 会滚动放开，交付前以目标版本 release notes 复核。
  tags: [8.10r1, release-limit, rt5, symmetric-irb, ingress-replication, all-active, compatibility]

- id: ce03
  title: 陷阱——Proxy ARP 表查出来是空的，先怀疑超时再查故障
  type: counter-example
  source_chapter: "p203"
  source_quote: |
    In case Proxy ARP Table is empty, it has probably timed out. Please try to send communication between the hosts and this should generate entries in the table.
  summary: |
    show ip evpn proxy-arp evi X 空表的官方处置口径：表项会老化，先让两台主机互 ping（触发 ARP/GARP），再回查应生成条目。教材 Lab 同样演示：初始 Total count: 0（p110），client 通信后出现 192.168.10.50 等本地表项（p113-114）。排障顺序：先造流量→再看表→仍空才往 RT2 携带 IP、snooping 源方向查。
  tags: [proxy-arp, aging, empty-table, troubleshooting, pitfall]

- id: ce04
  title: 陷阱——MAC 在两个 ES 间反复横跳（duplication）会拖垮 EVPN 控制面
  type: counter-example
  source_chapter: "p177"
  source_quote: |
    If a CE MAC address is constantly moving between two different Ethernet segments, it will cause the address to be learned on a different PE each time. This is called MAC duplications and can be a result of a loop in the ES network or if the same address is present in two hosts of the service.
    Such a behavior leads to a continuous exchange of the MAC being advertised and withdrawn in the control plane among all the PEs in the EVPN network and leads to degradation of the EVPN network performance.
  summary: |
    现象：同一 MAC 在两 ES 间反复学习→RT2 无休止通告/撤销震荡，全网 PE 性能劣化。根因两类：ES 网络存在后门环路，或两台主机真配了相同 MAC。处置：全局启用 service bgp-evpn mac-mobility loop-protection（retry-time/threshold/timeout，p127/p204）——PE 检测到 timeout 内移动计数达 threshold 即判定 duplication，该 MAC 进入 hold-down、停止收发其 BGP MAC 路由，retry-time 到期后解禁重来（p177）。实施提醒：命令要在所有 Leaf 上配（p127 原文 "on all switches: ALL LEAF SWITCHES"）。
  tags: [mac-duplication, mac-mobility, loop-protection, loop, control-plane, pitfall]

- id: ce05
  title: 陷阱——对远端 ES 执行 sap-info 直接报错（命令只支持本地 ES）
  type: counter-example
  source_chapter: "p107, p155"
  source_quote: |
    Sw2 (Leaf_2) -> show service evpn ethernet-segment 03:78:24:59:2b:32:b8:ff:ff:ff sap-info
    ERROR: Command Not supported for Remote ES
  summary: |
    ES 视图命令分本地/远端两类，对象搞错就报 "ERROR: Command Not supported for Remote ES"（p107 与 p154-155 两处实验均演示）。正确用法：sap-info / carving-info 只对本地 ES（Interface 列为端口号）有效；远端 ES（Interface 列为对端 VTEP IP、Description=Remote-ES）要用 aliasing-info。排障前先看 ethernet-segment 总表里该 ES 的 ES-Location 是 Local[Auto] 还是 Remote 再选命令。另外注意 sap-info 的 Legend 提示 "#: Missing ETAG configuration between Peer-PE nodes"——出现 # 号说明对端 PE 缺 ETag 配置。
  tags: [remote-es, sap-info, aliasing-info, command-error, troubleshooting, pitfall]

- id: ce06
  title: 反例——传统 STP+VLAN 模型与裸 VXLAN flood-and-learn 的固有问题
  type: counter-example
  source_chapter: "p164, p166"
  source_quote: |
    • Inefficient use of resources: The use of Spanning Tree Protocol (STP) led to inefficient use of resources due to blocked redundant links ...
    • Scalability issues since VLAN segmentation allows for a 12-bit VLAN ID, which has an upper limit of 4096 VLANs.
    • Traffic tromboning issues: Inter-VLAN traffic flows could suffer a "trombone" effect ... due to having a static first-hop router.
    [p166] in case the destination MAC address is unknwon, each switch learns of a connected host and will flood this traffic ... Constant flooding over the fabric ... can present a challenge for scalability.
  summary: |
    EVPN 的"反面教材"论证链（给客户讲为什么迁移）：传统 L2 四宗罪——①STP 阻塞冗余链路浪费带宽、收敛慢、版本互通问题；②12bit VLAN 上限 4096，虚拟化/容器场景不够用；③主机移动要全网逐台配 VLAN、逐链路打 tag；④静态首跳网关导致东西向流量 tromboning 绕行。裸 VXLAN（RFC 7348，无控制面）也不彻底：数据面 flood-and-learn、依赖 IP 组播承载 BUM，常态化泛洪威胁扩展性（p29 "No control plane / Flooding and Learning paradigm"、p167）。结论：这两类是上 MP-BGP EVPN 主动学习控制面的直接动因。
  tags: [stp, vlan-limit, tromboning, flood-and-learn, vxlan, why-evpn, counter-example]

- id: ce07
  title: 陷阱——教材原文客户端网关笔误（192.168.20.x 主机配了 192.168.30.254 网关）
  type: counter-example
  source_chapter: "p113"
  source_quote: |
    • Configure client 9
    IP V4 Adress :192.168.20.50
    Network :255.255.255.0
    Gateway:192.168.30.254
    • Configure client 10
    IP V4 Adress :192.168.20.60
    Network :255.255.255.0
    Gateway:192.168.30.254
  summary: |
    教材 p113 原文把 client 9/10（192.168.20.0/24 网段）的网关写成 192.168.30.254，而 Leaf 上 service 200 的 anycast-gateway-address 是 192.168.20.254（p109）——照抄必然跨网关不通。这是书中的真实笔误（同页 client5/6 的 192.168.10.254 是正确写法）。通用教训：客户端网关必须逐字等于所在 VLAN 业务在 Leaf 上配置的 anycast 网关地址；DAG 场景排障第一步就是核对主机网关与 anycast-gateway-address 一致。
  tags: [typo, default-gateway, anycast, client-config, dag, troubleshooting]

- id: ce08
  title: 陷阱——静态 LAG 上 ESI 不会自动生成，漏配 esi 参数多归属不成立
  type: counter-example
  source_chapter: "p156, p185"
  source_quote: |
    • Since we are using static link aggregation on LEAF-1 we will define the ESI ID.
    • On a static lingkagg, ESI has to be provided for an Ethernet segment
    [p185 范围表] Access Port Type / Auto ESI / Manual ESI: Physical Port Yes No; LACP LAG Yes No; Static LAG No Yes
  summary: |
    ESI 自动生成只覆盖物理口和 LACP LAG；静态 LAG 在 service access linkagg <id> evpn-ethernet-segment enable 时必须显式追加 esi 参数（Lab：esi 01:01:01:02:04，p156；架构指南 LEAF-4 同款，p199），否则 ES 无法正确标识、多归属机制不成立。手工 ESI 在 ethernet-segment 表中标志为 [L-M]（Local-Manual，p157）。另注意手工 ESI 两端必须一致（全网唯一标识同一 ES，p142/p168）。
  tags: [static-lag, esi, manual-configuration, multihoming, pitfall]

- id: ce09
  title: 陷阱——头端复制漏学一台远端 VTEP，该 VTEP 整体收不到 BUM 流量
  type: counter-example
  source_chapter: "p41"
  source_quote: |
    HEAD END REPLICATION
    One copy of each frame is sent to each known remote VTEP with a unicast IP header
    Requires that the VTEP know of all the IPs of the remote VTEPs participating in a VNI, or they will not receive any traffic
  summary: |
    纯 VXLAN 头端复制的 silent failure 模式：本端 VTEP 必须掌握同 VNI 全部远端 VTEP 的 IP，任何一台没学到就不会收到该 VNI 的任何泛洪流量（未知单播/广播/组播全部静默丢弃，主机表现为"部分方向不通"）。这正是 RT3 IMET 自动发现的价值所在——EVPN 用 RT3 建 ingress replication list 免去手工维护（p52/p180）。排障裸 VXLAN（无 EVPN）时优先核对 VTEP 对等列表完整性。
  tags: [head-end-replication, vtep-discovery, rt3, bum, silent-failure, pitfall]
```
