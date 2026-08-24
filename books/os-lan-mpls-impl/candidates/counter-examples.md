# counter-examples.md · OmniSwitch LAN MPLS Concepts & Implementation (DT00XTE324EN)
# 来源: D:\Claude code\TSSKB\books\os-lan-mpls-impl (153 页教材，p115-146 为 Reference Design Guide)

- id: ce01
  title: 陷阱：许可状态无效或 demo 过期时 MPLS 被临时禁用
  type: counter-example
  source_chapter: "p92"
  source_quote: |
    "MPLS will be enabled only if it receives the license status as "permanent" or "demo" license not yet expired. And temporarily disables the feature if the license status is invalid (no-license) or "demo" license expire."
  summary: |
    MPLS 接口要 up 必须持有 permanent 或未过期 demo 许可；状态为 no-license 或 demo 过期时特性被临时禁用（不是删配置，而是功能停摆）。Lab 中四台交换机初始 show license-server info 显示 MPLS_Site/MPLS_Node 均 NO LICENSE，配置 SILOS 服务器并接入后才拿到 15/23 天的 DEMO 许可。交付现场若 MPLS 突然全网失效，先用 sh license-info / show license-server usage 查许可剩余天数，再查 SWLIC 与 SILOS 的连接状态（Connection Status 应为 Connected）。
  tags: [许可, demo过期, 故障排查, SILOS, SWLIC]

- id: ce02
  title: 陷阱：LSR ID（loopback 地址）在 MPLS 域内不唯一导致不可预测行为
  type: counter-example
  source_chapter: "p125"
  source_quote: |
    "It is important that the LSR ID, or the loopback address is unique in the MPLS domain to avoid any unpredictable behavior."
  summary: |
    教材以加粗强调：LSR ID（即 loopback 地址）必须在 MPLS 域内唯一，否则出现"不可预测行为"（unpredictable behavior）——LDP 邻接、标签绑定都会错乱，且现象不固定、难排查。规划阶段就应统一分配 loopback 段（Lab 用 192.168.254.0/24，参考设计用 1.1.1.x/32），并在最佳实践里再次要求 Router-ID 唯一（p136）。上线清单应包含"全网 loopback 唯一性核查"。
  tags: [LSR-ID, loopback, 唯一性, 规划陷阱]

- id: ce03
  title: 陷阱：PHP 隐式 NULL 弹标签时 EXP（QoS）位一并丢失，显式 NULL 又不被 AOS 支持
  type: counter-example
  source_chapter: "p128-129"
  source_quote: |
    "When the last LSR removes the top label, the EXP bits are also removed, thus removing any QoS values in the header. The explicit NULL can be used in this case to solve this issue. ... Explicit NULL is currently not supported in AOS implementation."
  summary: |
    PHP 用隐式 NULL（3）让倒数第二跳弹出传输标签，但弹标签时 EXP 位同时被移除，包头里的 QoS 标记丢失。标准解法是 eLER 改发显式 NULL（IPv4=0/IPv6=2），让 eLER 收到带标签的 NULL 并保留 EXP——但 AOS 当前实现不支持显式 NULL，且 QoS over EXP 本身也不支持（p130）。所以在 AOS 方案里不要承诺"靠 MPLS EXP 端到端承载 QoS"，QoS 策略要落在 IP DSCP 或其他机制上。
  tags: [PHP, EXP, QoS丢失, 显式NULL, 能力边界]

- id: ce04
  title: 陷阱：朝向 CE 路由器的接口不能使能 LDP
  type: counter-example
  source_chapter: "p125"
  source_quote: |
    "LDP should be enabled on all interfaces in the MPLS domain except towards the CE router (in the LER router)."
  summary: |
    LDP 使能范围的例外规则：MPLS 域内接口全部使能 LDP，唯独 LER 上朝向 CE 的接口不能使能。CE 侧不跑 MPLS，业务通过 SAP（service access port + sap port:vlan）接入而非 LDP。若误在 CE 互联口上开 LDP，轻则邻居异常，重则标签行为不可控。Lab 中 sw7/sw8 只在 int_70/79/80/89 等骨干口使能 mpls ldp interface，1/1/3、1/1/7 等业务口只做 service access port，正是此规则的体现。
  tags: [LDP, CE接口, 使能范围, 误配置]

- id: ce05
  title: 陷阱：AOS 首版 MPLS 不支持的特性清单（设计方案不能引用）
  type: counter-example
  source_chapter: "p127-133"
  source_quote: |
    "Current implementation of IP/MPLS in AOS does not support RSVP. ... Explicit NULL is currently not supported in AOS implementation. ... QOS over EXP bit is not supported in the current implementation of AOS. ... TTL manipulation is not supported for MPLS tag in the current implementation of AOS. ... VPWS is not supported in the current implementation of AOS. The use of RR in the BGP signaled VPLS network is not currently supported in AOS implementation."
  summary: |
    Reference Design Guide 明确标注当前 AOS 实现不支持的六项：RSVP-TE（无流量工程与带宽预留）、显式 NULL、基于 EXP 的 QoS、MPLS TTL 操作、VPWS（点对点伪线/E-Pipe）、BGP VPLS 中的路由反射器（RR）。售前/方案阶段拿业界通用 MPLS 方案套 AOS 时极易踩这六个坑：要 TE 得等后续版本，要点对点二层专线只能用 VPLS 两点互通模拟，要 RR 只能 IBGP 全互联。教材 p118 也预告"后续版本可能补充，届时更新本文档"。
  tags: [能力边界, 不支持特性, RSVP, VPWS, RR, 售前风险]

- id: ce06
  title: 陷阱：LDP Graceful Restart 只对计划内接管有效
  type: counter-example
  source_chapter: "p130"
  source_quote: |
    "This mechanism, as described in RFC 3478, helps to minimize disruption on MPLS traffic caused by a control plane restart by preserving the forwarding state information. This mechanism is supported only for planned takeovers (for example, the users performs the takeover), not unplanned takeovers (for example, the primary Chassis Management Modules (CMMs) unexpectedly fails) or when a link goes down between the two routers."
  summary: |
    LDP Graceful Restart（RFC 3478，配 NSF）只在计划内接管（如手工执行 takeover）时保留转发状态、减少流量中断；主用 CMM 意外故障（非计划接管）或两机之间链路 down 时该机制无效，MPLS 流量会中断收敛。做高可用承诺时要区分"计划内维护不丢包"与"突发故障需收敛"，Lab 2 的断链 ping 测试对应的正是后一种场景。show mpls ldp session 可见 Graceful restart = Enabled、Restarting mode = Helper。
  tags: [Graceful-Restart, 高可用, CMM, 计划内接管, 故障场景]

- id: ce07
  title: 陷阱：LDP-VPLS 无自动发现，PE 数量增长带来全网状手工配置爆炸
  type: counter-example
  source_chapter: "p72, p132-133"
  source_quote: |
    "With auto-discovery, there is no need to configure each VPLS router with all remote endpoints of VPLS tunnels" (p72)
    "A full-mesh of PWs needs to be established between LERs to form a VPLS." (p132-133)
  summary: |
    VPLS 的硬性要求是 LER 间伪线全网状（Split Horizon 防环依赖全网状，见 p133）。LDP 信令没有自动发现，每台 PE 都要为每个远端手工建 SDP 并 bind-sdp——n 台 PE 需要 n(n-1)/2 条伪线、每端 n-1 条 SDP 配置；新增一个站点要改所有旧站点。BGP 信令靠自动发现消除逐点配置（p72），但 AOS 不支持 RR，IBGP 邻居仍要全互联。规模估算时按此计算配置量：3-4 站点 LDP 尚可（Lab/参考设计均为 2-3 台 PE），更多站点应选 BGP。
  tags: [扩展性, 全网状, LDP-VPLS, 自动发现, 配置爆炸]

- id: ce08
  title: 陷阱：SAP 配成 untagged（:0）时出口流量永远 untagged
  type: counter-example
  source_chapter: "p79"
  source_quote: |
    ""ITAG" and "OTAG" refer to inner tag and outer tag, respectively
    E.g.: If the local SAP is configured for untagged traffic (slot/port:0), the egress traffic is always sent out as untagged."
  summary: |
    VLAN 转换的行为约束：SAP 用 slot/port:0（untagged）定义时，出口流量一律以 untagged 发出，不会替客户打上 VLAN 标签。若对端站点期望收到 tagged 流量，就会出现单通/不通。Lab 2 中 sw8 的 service 3 sap port 1/1/1:0（untagged 接 client 8）与对端 tagged SAP 的互通就依赖 vlan-xlation 两级使能（服务级+端口级）来对齐（p104-105）。设计 SAP 封装格式（:0 untagged / :vlan-id）时要两端一致或明确启用转换。
  tags: [SAP, untagged, VLAN转换, 封装不匹配, 排障]
