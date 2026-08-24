# 候选条目 · 术语表
来源：OV 2500 RAP and VPN VA Installation Guide (4.9R2 RevA, 84 页)
页码约定：pN 为 fulltext.md 中 <<<PAGE N>>> 的 PDF 页码。

- id: g01
  title: RAP（Remote Access Point，远程接入 AP）
  type: glossary
  source_chapter: "p4"
  source_quote: |
    "A Remote Access Point (RAP) is an AP with a management tunnel and a data tunnel to a remote OmniVista Enterprise (OVE) Server."
  summary: |
    部署在居家/分支等远端站点、通过管理隧道 + 数据隧道回连企业 OVE 服务器的 Stellar AP。严格定义下只有 OVE 管理的远程 AP 才叫 RAP；OVC 管理的远程 AP 因无 Management VPN 配置在技术上不算 RAP。要求 AWOS 5.0.2 及以上。
  tags: [术语, RAP]

- id: g02
  title: OVE（OmniVista Enterprise）
  type: glossary
  source_chapter: "p4"
  source_quote: |
    "...a management tunnel and a data tunnel to a remote OmniVista Enterprise (OVE) Server."
  summary: |
    部署在企业本地的 OmniVista 网管服务器（OmniVista 2500 NMS 即其 4.9R2 版本形态）。本地 AP 经 DHCP option 138 找到它直接纳管；RAP 经 WireGuard 管理隧道回连后被 OVE 管理，Data VPN 与 WLAN 服务配置也在 OVE 侧完成。
  tags: [术语, OVE, 网管]

- id: g03
  title: OVC（OmniVista Cirrus）
  type: glossary
  source_chapter: "p4"
  source_quote: |
    "An OVC managed AP already uses an OpenVPN connection for Management communications with a VPN Server in the OVC Cloud infrastructure."
  summary: |
    OmniVista 的云管版本。OVC 管理的 AP 用 OpenVPN 连 OVC 云做管理通信；RAP 方案里 OVC 还承担两个角色：Device Registration/Activation Server（开箱首连注册）和 Freemium 账号（添加 RAP 到 Device Catalog、导出 VPN 设置文件）。VA 4.9.2.2 认证配套 OVC 4.9.2。
  tags: [术语, OVC, 云管]

- id: g04
  title: VPN VA（VPN Virtual Appliance，VPN 虚拟设备）
  type: glossary
  source_chapter: "p13"
  source_quote: |
    "A Virtual Private Network (VPN) Virtual Appliance (VA) is required for managing Remote Access APs and securely tunneling data from devices at remote locations."
  summary: |
    部署在企业总部 hypervisor 上的专有隧道终结点虚拟机（本书版本 4.9.2.2），承接 RAP 的管理隧道与数据隧道。可跑在 VMware ESXi、Hyper-V、Ubuntu 22.04+KVM 上；规格按 RAP 数量分 4 档（4vCPU/2GB 至 12vCPU/16GB）；不支持冗余；默认硬盘 8GB。通常配 3 块网卡：公网口、连 OVE 的私网口、无 IP 的 L2 桥接口。
  tags: [术语, VPN-VA, 虚拟设备]

- id: g05
  title: Management VPN（管理 VPN 隧道）
  type: glossary
  source_chapter: "p4"
  source_quote: |
    "The OVC Device Catalog provides options to register the AP as a RAP. This is required to setup the Management VPN to the RAP Virtual Appliance (VA) appliance located in corporate HQ."
  summary: |
    RAP 与总部 VPN VA 之间的 WireGuard 加密管理隧道，承载 OVE 对 RAP 的管理通信（OVC 模式不需要，走 OpenVPN）。建立前提：管理员在 OVC Device Catalog 把 AP 注册为 RAP 并预置 VPN VA 公网 IP/OVE 内网 IP/安全密钥；对应 VA 上的 vpn_management 服务与端点（接口选 None）。
  tags: [术语, 管理隧道, WireGuard]

- id: g06
  title: Data VPN（数据 VPN 隧道）
  type: glossary
  source_chapter: "p4-5, p67"
  source_quote: |
    "A Data VPN tunnel must be setup in OVE between the RAP and the VPN server. The tunnel keys and parameters can be exported to the VPN server at corporate HQ."
  summary: |
    RAP 与总部 VPN Server 之间承载终端用户业务流量的隧道，在 OVE（或 OVC）上配置、密钥参数导出到 VPN VA。实际承载体是 L2GRE 隧道，挂接 SSID（Use Tunnel + Tunnel ID 0 + Data VPN Server profile），可配 tagged/untagged VLAN 与 Local Breakout。对应 VA 上的 vpn_data 服务与端点（桥接接口选无 IP 的 eth2）。
  tags: [术语, 数据隧道, L2GRE]

- id: g07
  title: WireGuard（含 wg 命令与 wg0/wg1 接口）
  type: glossary
  source_chapter: "p4, p81-82"
  source_quote: |
    "The RAP then establishes a Wireguard VPN tunnel over which it connects to be managed by OVE. ... For wg show check the public key, listening port, peer endpoint, allowed ips, the time since handshake and that transfer and received are incrementing."
  summary: |
    RAP 方案的管理/数据 VPN 使用的加密隧道协议，配置文件为 [Peer] 段的 PublicKey + AllowedIPs（如 10.180.2.7/32）。wg 是其命令行工具（在 VPN VA 和 RAP 上查隧道接口）；wg0 为管理隧道接口、wg1 为数据隧道接口，排障时分别检查（示例 keepalive 每 5 秒，wg0 MTU 1420）。
  tags: [术语, WireGuard, wg命令]

- id: g08
  title: OpenVPN
  type: glossary
  source_chapter: "p4"
  source_quote: |
    "An OVC managed AP already uses an OpenVPN connection for Management communications with a VPN Server in the OVC Cloud infrastructure."
  summary: |
    OVC 管理 AP 使用的管理通道协议——AP 与 OVC 云内 VPN Server 建 OpenVPN 连接受管。区别于 RAP 场景的 WireGuard；这也是 OVC 管理的远程 AP 不需要另配 Management VPN 的原因。
  tags: [术语, OpenVPN, OVC]

- id: g09
  title: L2GRE 隧道（GRE 二层隧道）
  type: glossary
  source_chapter: "p67, p82"
  source_quote: |
    "An L2GRE tunnel will be created between the Remote AP and the VPN Server and it will be used to tunnel the remote employee's data traffic."
  summary: |
    Data VPN 建立后在 RAP 与 VPN Server 之间实际创建的二层 GRE 隧道，桥接远端员工数据流量（故桥接网卡无需 IP）。排障时用 ip -d link 检查 gre0/gretap0 接口（示例 MTU 1476/1462），MTU 须低于 1500。
  tags: [术语, GRE, L2隧道]

- id: g10
  title: DHCP option 138
  type: glossary
  source_chapter: "p4"
  source_quote: |
    "Typically, a local AP in the Enterprise learns its OV IP address via DHCP option 138."
  summary: |
    企业内本地 AP 通过 DHCP 下发的 138 选项获知 OV 网管地址从而被纳管。开箱 AP 若未得到 option 138，会先注册 OVC Activation Server——这正是把 AP 配置成 RAP 的入口。
  tags: [术语, DHCP, option-138]

- id: g11
  title: Device Catalog（设备目录）
  type: glossary
  source_chapter: "p8"
  source_quote: |
    "Remote APs are added using the Device Catalog application. You can add APs one-at-a-time or import multiple APs at once using a .csv file."
  summary: |
    OVC 中管理设备清单的应用（Network→Inventory→Device Catalog）。添加 RAP 时开启 Is this a Remote AP，填写 VPN Settings（公网 IP/端口/VPN IP/OVE 地址/客户端地址池）；支持单台添加或 CSV 批量导入（RAP 字段须 TRUE）；Export VPN Settings 按钮从这里导出隧道配置文件。
  tags: [术语, OVC, 设备目录]

- id: g12
  title: Freemium 账号
  type: glossary
  source_chapter: "p6"
  source_quote: |
    "OmniVista Cirrus offers a "Freemium" account which is used to add Remote APs."
  summary: |
    OmniVista Cirrus 的免费层账号，专门用于添加 RAP：在 registration.ovcirrus.com 注册（邮件验证，验证邮件附设备 OS 软件下载链接），登录后用 Device Catalog 加 RAP、导出 VPN 设置文件。与 Premium/Business 账号的差异在于功能门槛（如下行口 Access Auth Profile 需付费账号）。
  tags: [术语, Freemium, 账号]

- id: g13
  title: Device Registration Server / Activation Server（设备注册/激活服务器）
  type: glossary
  source_chapter: "p4, p6"
  source_quote: |
    "An out-of-the-box AP that is not supplied with DHCP option 138 will first register with the OVC Activation Server allowing it to be configured as a RAP. ... When the AP(s) is connected to the network, it automatically contacts the OmniVista Cirrus Activation Server, which downloads the necessary IP and VPN configurations..."
  summary: |
    OVC 云端的设备首连注册/激活服务。开箱 AP（未获 option 138）自动联系它：OVE 模式下取回 RAP 参数（含 OVE IP）并把 AP 加入本地 OVE 的受管设备列表；OVC 模式下确认注册身份。是两种模式共同的注册入口。
  tags: [术语, 注册服务器, 激活]

- id: g14
  title: Client VPN IP Address Pool（客户端 VPN 地址池）
  type: glossary
  source_chapter: "p11"
  source_quote: |
    "Client VPN IP Address Pool - The range of addresses available to assign to Remote APs. IP Range - Enter a starting and ending IP address range. Shorthand Mask - Enter a shorthand mask for the IP Range. Subnet Mask - Enter the subnet mask for the Client VPN IP Address Pool."
  summary: |
    分配给 RAP 的虚拟网络地址段（起始-结束 IP + 简写掩码或子网掩码）。硬性约束：Server's VPN IP（VPN Server 隧道接口私网 IP）必须与该池同网段，否则远端流量无法正确进入企业网。
  tags: [术语, 地址池, VPN参数]

- id: g15
  title: Local Breakout（本地分流/本地出口）
  type: glossary
  source_chapter: "p73"
  source_quote: |
    "Allow Local Breakout - Enables/Disables Local Breakout on the tunnel. If enabled, enter the Static Route(s) to be used for entering the Tunnel. All other traffic will go out through the local network."
  summary: |
    数据隧道上的分流功能：命中静态路由的流量进隧道去总部，其余流量直接从 AP 本地网络出局（典型用于上网流量本地出去）。约束：仅隧道内一个 VLAN 可启用（Tunnel ID 必须为 0）；路由跨 SSID 累积且目的子网不得重复；须避开与 AP 本地网段及隧道 VLAN 网段重叠。启用后每 RAP 吞吐约 10-20 Mbps（全隧道为 20-100 Mbps）。
  tags: [术语, Local-Breakout, 分流]

- id: g16
  title: NIC Teaming（网卡绑定/组队）
  type: glossary
  source_chapter: "p14"
  source_quote: |
    "10G NIC is standard for more than 500 APs. For increased throughput use 2 x 10G NIC (NIC Teaming). ... NIC Teaming is supported when deploying the VPN Virtual Appliance."
  summary: |
    把多块物理网卡绑成一条逻辑链路提升吞吐，VPN VA 部署支持该特性（典型 2x10G）。Hyper-V 上受兼容矩阵约束：Switch Independent 模式只能配 Address Hash 负载均衡，Hyper-V Port/Dynamic 均不通过；Linkagg static 与 LACP 下三种负载均衡均可。
  tags: [术语, NIC-Teaming, 网卡绑定]

- id: g17
  title: Promiscuous Mode 与 MAC 地址欺骗（混杂模式/MAC Spoofing）
  type: glossary
  source_chapter: "p20, p31"
  source_quote: |
    "On the ESXi VM, enable Promiscuous Mode for the above NIC. If the "Override" checkbox is enabled, make sure Promiscuous Mode, MAC address changes, and Forged transmits are set to "Accept". ... Expand Eth2, under Advanced Features select the option Enable MAC address spoofing."
  summary: |
    让虚拟网卡接收/发送非自身 MAC 帧的 hypervisor 安全选项，L2 桥接隧道必需：ESXi 上为桥接网卡开混杂模式（配 VLAN 0=untagged / 4095=tagged），三项安全策略全设 Accept；Hyper-V 上对 Eth2 启用 MAC address spoofing 并配 Trunk。漏配的典型症状是客户端无法访问同网段设备。
  tags: [术语, 混杂模式, MAC欺骗]

- id: g18
  title: DS-Lite（Dual Stack Lite，双栈精简）及 TCPMSS/MTU
  type: glossary
  source_chapter: "p78"
  source_quote: |
    "When configuring a RAP network that interacts with a DS-Lite router, the following general configuration guidelines are recommended: Management VPN Profile TCPMSS ... WG + DS-Lite 1352; Data VPN Profile TCPMSS ... WG + DS-Lite 1300; MTU Data VPN/GRE Tunneling ... WG + DS-Lite 1376"
  summary: |
    ISP 路由器把 IPv4 封装在 IPv6 隧道里传输的技术，额外封装开销要求调小报文尺寸：TCPMSS（TCP 最大报文段长度，控制 TCP 同步报文选项）在 WG+DS-Lite 时管理/数据 profile 分别为 1352/1300；MTU（链路最大传输单元，数据 VPN/GRE 隧道）为 1376。三个参数分别在不同界面修改（Freemium VPN Servers / Data VPN Server / SSIDs）。
  tags: [术语, DS-Lite, TCPMSS, MTU]

- id: g19
  title: AWOS / Stellar AP
  type: glossary
  source_chapter: "p4-5"
  source_quote: |
    "Components of the solution include: Stellar APs ... Supported Stellar RAP version is AWOS 5.0.2 and higher."
  summary: |
    Stellar 是 ALE 的 AP 产品线（如 AP1201H/AP1201HL/AP1311），AWOS 是其操作系统版本号体系。RAP 功能要求 AWOS 5.0.2 及以上（文档另有 5.0.1/4.0.1 两处口径，以 5.0.2 为准）。AP1201H 等带下行口的型号还可经 Tunnel Profile/Access Auth Profile 把下行口流量隧道化。
  tags: [术语, AWOS, Stellar]

- id: g20
  title: 三类 Profile：Tunnel Profile / Access Role Profile / Access Auth Profile
  type: glossary
  source_chapter: "p74-75"
  source_quote: |
    "Create a Tunnel Profile in Unified Access in OmniVista (Unified Access – Template - Tunnel Profile). ... select the Tunnel Profile you created in Step 1, and apply the profile to the AP Group with Mapping method: "Map to VLAN and Tunnel". ... If you have a Premium or Business Account, you can assign an Access Auth Profile to a Downlink Port on Stellar AP1201H, AP1201HL, and AP1311 Devices."
  summary: |
    Unified Access→Template 下的三种模板，用于 1201H 下行口隧道化：Tunnel Profile 定义隧道参数；Access Role Profile 引用 Tunnel Profile 并以"Map to VLAN and Tunnel"方式映射到 AP Group；Access Auth Profile 定义下行口接入认证（需 Premium/Business 账号，可指定 Eth1-Eth3 最多 3 个口，组内不支持的 AP/端口自动忽略）。
  tags: [术语, Profile, 下行口, Unified-Access]
