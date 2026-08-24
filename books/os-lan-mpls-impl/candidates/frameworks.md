# frameworks.md · OmniSwitch LAN MPLS Concepts & Implementation (DT00XTE324EN)
# 来源: D:\Claude code\TSSKB\books\os-lan-mpls-impl (153 页教材，p115-146 为 Reference Design Guide)

- id: f01
  title: AOS MPLS 骨干与 VPLS 部署总流程（十步法）
  type: framework
  source_chapter: "p58-65, p68"
  source_quote: |
    "Step 1:  Install MPLS Package
    Step 2: IP Interface Creation.
    Step 3: Setup Routing for the interfaces using OSPF.
    Step 4: Load LDP protocol.
    Step 5: Enable MPLS/LDP on the interface
    Step  6: Configure VPLS service"
  summary: |
    AOS 上部署 MPLS 的固定次序：1) 全网安装 MPLS Debian 包（pkgmgr install uosn-mpls-v1.deb）；2) 创建互联 VLAN 与 IP 接口；3) 配 OSPF/IS-IS underlay，含每台交换机的 Loopback0；4) 安装许可（SILOS 服务器 + SWLIC 客户端）；5) mpls load ldp 并在全局与接口两级使能 MPLS/LDP；6) 建 VPLS 服务；7-10) SDP/bind-sdp/SAP/验证。前置条件：稳定 IP 拓扑 + Loopback0 作为系统 IP（OmniSwitch 特有要求）。此流程在 Lab 1（p83-96）与 Reference Design Guide（p136-138）中均按此骨架展开。
  tags: [MPLS, 部署流程, LDP, 骨干, AOS]

- id: f02
  title: VPLS-LDP 信令配置流程（手工 SDP + 定向 LDP 会话）
  type: framework
  source_chapter: "p67-70"
  source_quote: |
    "Step 7: Create a static SDP and trigger a message to LDP to establish a target peer with the far-end IP address
    Step 8: Create a binding of an SDP to the service (VPLS) and trigger a message to mpls CMM to establish a VC label
    Step 9: Configure access ports and create SAP on the access port for MPLS-VPLS"
  summary: |
    骨干就绪后叠加 VPLS 的四步：a) service N vpls vplsid X signaling ldp 建服务；b) service sdp M vpls far-end <对端 loopback> 建静态 SDP，触发与远端建立 T-LDP（定向 LDP）会话；c) service N bind-sdp M 把 SDP 绑定到服务、协商 VC 标签；d) service access port 声明接入端口后用 service N sap port slot/port:vlan 挂业务。SDP 必须在两端 PE 互指对端 loopback（Lab 中 sw7/sw8 各配 SDP 78 指向对方 192.168.254.x）。验证：show mac-learning domain vpls 应看到远端 MAC 从 sdp: 接口学到。
  tags: [VPLS, LDP, SDP, SAP, 配置流程]

- id: f03
  title: VPLS-BGP 信令配置流程（自动发现与信令合一）
  type: framework
  source_chapter: "p72-76"
  source_quote: |
    "The VPLS BGP Signalling feature enables the auto discovery of PE's or tunnel end point in the same VPLS instance.
    Auto-discovery:
    With auto-discovery, there is no need to configure each VPLS router with all remote endpoints of VPLS tunnels"
  summary: |
    BGP 方式在 LDP 骨干之上叠加：1) ip load bgp；2) 配 AS 号、address-family l2vpn-vpls、与各 PE 建邻居（remote-as 同 AS、update-source Loopback0、activate l2vpn-vpls、admin-state enable）；3) service N vpls vplsid X signaling bgp ve-id Y——每台 PE 只配本端 ve-id，无需手工 SDP；4) SAP 接入。BGP 自动发现同一 VPLS 实例的全部 PE 并建立伪线（Lab 中 BGP 生成的绑定显示为 sdp:32768:x）。验证：show ip bgp neighbors 看 established、show ip bgp l2vpn-vpls 看发现的 peer。
  tags: [VPLS, BGP, 自动发现, l2vpn-vpls, 配置流程]

- id: f04
  title: VPLS 信令选型框架：LDP vs BGP
  type: framework
  source_chapter: "p132-133, p72"
  source_quote: |
    "The multiprotocol capabilities of BGP enables the auto discovery of PE's or tunnel end-point in the same VPLS instance. The method of establishing VPLS with BGP accomplishes both auto-discovery and signaling. Since these services are usually configured for a single AS, using MP-BGP will require either a full-mesh of peerings between LERs, or using Route Reflectors (RR). The use of RR in the BGP signaled VPLS network is not currently supported in AOS implementation."
  summary: |
    选型要点：LDP 信令（T-LDP 方式）配置简单，但每台 PE 必须手工为每个远端建 SDP，节点数增多时配置量按全网状伪线增长；BGP 信令一步完成自动发现+信令，扩容只加邻居，但要求 LER 间 IBGP 全互联，而 AOS 当前不支持路由反射器（RR），全互联规模也有上限。教材两种方式都完整给出（Lab 2 / Lab 3），小规模可用 LDP，多站点建议 BGP。BGP 侧另有 ip bgp mpls 命令（p139 参考设计样例中出现）。
  tags: [VPLS, 选型, LDP, BGP, RR, 扩展性]

- id: f05
  title: MPLS 服务框架模型（SAP/SDP + 双层隧道）
  type: framework
  source_chapter: "p50, p131"
  source_quote: |
    "Service Access Point (SAP): A UNI-side logical port which binds a physical port and spcific customer traffic types to a service. It is the point where the customer traffic ingress/egress the MPLS network.
    Service Distribution Point (SDP): An NNI-side logical port which binds a service to a far-end router over which MPLS encapsulated packets are distributed."
  summary: |
    一个 MPLS 服务代表一个 VPN/租户，只建在服务该业务的 LER 上。LER 上四个组件：SAP（UNI 侧逻辑口，绑定物理端口与客户流量类型，同一物理口可复用多个 SAP）、SDP（NNI 侧逻辑口，绑定服务到远端路由器）、服务隧道（FEC=服务标识 vplsid）、传输隧道（FEC=各 LSR 的 loopback）。转发时 iLER 先 push 服务标签再压传输标签，中间 LSR 只处理传输标签，到 eLER 两层依次弹出送到对应 SAP。这正是"传输标签在上、服务标签在下"堆栈结构（p38）的服务模型解释。
  tags: [SAP, SDP, 服务模型, 隧道, VPN]

- id: f06
  title: 参考设计场景模板：企业园区与城域智能城市
  type: framework
  source_chapter: "p133-134, p28"
  source_quote: |
    "Enterprise Campus Networks
    A two or three-tier architecture for a small and medium campus networks is best suited. It will provide VPN services end-to-end and IP/MPLS will be implemented from the access to the core layer.
    Metro Ethernet Networks (Smart City)
    For metro ethernet networks such as smart city networks, IP/MPLS network can be configured at the core and distribution layers of a three-tier network architecture. At the access layer, ethernet standard switching will be configured."
  summary: |
    Reference Design Guide 给出两类经过验证的落地模板：1) 中小园区网络：二或三层架构，IP/MPLS 从接入层一直部署到核心层，提供端到端 VPN 业务；2) 城域以太网（智能城市等）：三层架构中核心层与汇聚层跑 IP/MPLS，接入层用标准以太交换。AOS MPLS 定位是企业与城域客户的高性价比方案（p133 开头）。售前做方案时可直接套用这两个架构模板，再叠加 f01-f03 的配置流程。
  tags: [参考设计, 园区网, 城域以太网, 智能城市, 架构模板]
