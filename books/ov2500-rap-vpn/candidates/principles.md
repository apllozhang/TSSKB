# 候选条目 · 原则/规则/参数
来源：OV 2500 RAP and VPN VA Installation Guide (4.9R2 RevA, 84 页)
页码约定：pN 为 fulltext.md 中 <<<PAGE N>>> 的 PDF 页码（与 BOOK_OVERVIEW 一致）。

- id: p01
  title: 两种 VPN 模式的选择规则：OVE 全隧道 vs OVC 仅数据隧道
  type: principle
  source_chapter: "p4-5"
  source_quote: |
    "A Remote Access Point (RAP) is an AP with a management tunnel and a data tunnel to a remote OmniVista Enterprise (OVE) Server. An OmniVista Cirrus (OVC) Managed AP is technically not considered a RAP since there are no Management VPN Server details to be configured. An OVC managed AP already uses an OpenVPN connection for Management communications with a VPN Server in the OVC Cloud infrastructure. However, it is possible that an OVC Managed AP might need a Data VPN Tunnel to a VPN Server in the Enterprise."
  summary: |
    模式选择规则：远程 AP 由企业本地 OVE 管理时，才是真正意义的 RAP，需要管理隧道 + 数据隧道两条 VPN；由 OVC 云管理时技术上不算 RAP（管理通道走 OVC 云内 OpenVPN，无需配置 Management VPN Server），只有需要把数据流量送回企业总部时才另建 Data VPN 隧道。
    配套的可达性原则（p4）：本地 AP 通过 DHCP option 138 获得 OV 地址被直接管理；远程站点 AP 对企业 OV 不可直达，连接与管理通信必须走 VPN 隧道。协议清单：管理隧道 WireGuard（OVE 模式）/ OpenVPN（OVC 模式），数据隧道为 WireGuard 配置下的 L2GRE 隧道。
  tags: [VPN模式, RAP, OVE, OVC, WireGuard, OpenVPN]

- id: p02
  title: 两种模式下 RAP 的注册与建隧道流程
  type: principle
  source_chapter: "p4-5"
  source_quote: |
    "1. The first connection, out-of-the-box, is to the OVC Device Registration Server. It retrieves the setup parameters for RAP including the OVE IP to which it will connect. 2. The keys and parameters are exported to the RAP VPN Server at corporate HQ. 3. The RAP then establishes a Wireguard VPN tunnel over which it connects to be managed by OVE. 4. A Data VPN tunnel must be setup in OVE between the RAP and the VPN server."
  summary: |
    OVE 管理流程五步：①开箱首连 OVC Device Registration Server，取回 RAP 参数（含目标 OVE IP）；②密钥与参数导出到总部 RAP VPN Server；③建立 Wireguard 管理 VPN 隧道，经隧道接受 OVE 管理；④在 OVE 上配置 RAP→VPN Server 的 Data VPN 隧道并导出密钥；⑤数据隧道建立后承载终端业务。管理员需先在 OVC Device Catalog 把 AP 注册为 RAP，以便预置 VPN VA 公网 IP / OVE 内网 IP / 安全密钥（Security Keys）——这是本书密钥预置的唯一出处。
    OVC 管理流程四步（p5）：①开箱首连 OVC Device Registration Server 确认注册；②AP 建 OpenVPN 连接由 OVC 管理；③在 OVC 上配置 Data VPN 隧道并导出密钥参数到总部 VPN Server；④隧道承载业务。WLAN 服务配置在管理方（OVE 或 OVC）侧完成。
  tags: [注册流程, 密钥导出, Wireguard, OpenVPN]

- id: p03
  title: 平台与版本前置条件
  type: principle
  source_chapter: "p5"
  source_quote: |
    "ESXi versions 6.5, 6.7, 7.0.2, 8.0 are supported (ESXi 5.5 is not supported). Hyper-V 2016, 2019, and 2022. Supported Stellar RAP version is AWOS 5.0.2 and higher. RAP VPN VA version 4.9.2.2. The virtual appliance version 4.9.2.2 is certified for use with OmniVista 2500 4.9R2 and OmniVista Cirrus version 4.9.2."
  summary: |
    前置条件清单：ESXi 支持 6.5/6.7/7.0.2/8.0（5.5 明确不支持）；Hyper-V 支持 2016/2019/2022；Stellar RAP 需 AWOS 5.0.2 及以上（最新特性也要求 5.0.2+）；RAP VPN VA 版本 4.9.2.2；该 VA 与 OV2500 4.9R2、OVC 4.9.2 认证配套。另支持在 Ubuntu 22.04 LTS + KVM 上部署。
  tags: [版本兼容, ESXi, Hyper-V, AWOS, KVM]

- id: p04
  title: Freemium 账号、Device Catalog 注册与 VPN Server 参数定义
  type: principle
  source_chapter: "p6-12"
  source_quote: |
    "Server's Public IP - The VPN Server's Public IP address... And this is the interface through which traffic originating from inside the Enterprise Network flows to the Remote site. ... Server's VPN IP - The VPN Server's Private IP address within the virtual network (must be in the same network as the client pool). ... Client VPN IP Address Pool - The range of addresses available to assign to Remote APs."
  summary: |
    添加 RAP 前先建 OmniVista Cirrus Freemium 账号（registration.ovcirrus.com 注册，邮件验证链接来自 noreply@ovcirrus.com，邮件正文含设备 OS 软件下载链接）。规划规则：Device Catalog（Network→Inventory→Device Catalog）加 AP 时要填第 3 步才部署的 VPN Server 信息，必须先确定 VPN Server 配置再开工。VPN Settings 首次用 Create New，保存后后续 AP 可直接 Choose Existing 复用。
    参数定义：Server's Public IP = RAP 连接 VPN Server 的公网地址（企业网流向远端的出口接口）；Port = 公网端口；Server's VPN IP = 虚拟网络内私网 IP，必须与客户端地址池同网段（远端流量进入企业网的隧道接口）；Client VPN IP Address Pool = 分配给 RAP 的地址段（IP 范围 + 简写掩码/子网掩码）。批量导入用 CSV，模板中 RAP 字段须为 TRUE 才能携带 VpnSettingName。
  tags: [Freemium, Device-Catalog, VPN参数, CSV导入]

- id: p05
  title: VPN VA 容量配置按 RAP 数量分档
  type: principle
  source_chapter: "p13"
  source_quote: |
    "1 - 100 APs - 4 vCPUs, 2GB RAM; 100 - 250 APs - 6 vCPUs, 4GB RAM; 250 - 500 APs - 8 vCPUs, 8GB RAM; 500 - 1,000 APs - 12 vCPUs, 16GB RAM. Note: Higher scale is based on CPU/Memory calculated per RAP. For deployments with more than 250 RAPs, it is recommended that you deploy a second VPN VA Server."
  summary: |
    VPN VA 规格 4 档：1-100 台 AP → 4 vCPU / 2GB 内存；100-250 → 6 vCPU / 4GB；250-500 → 8 vCPU / 8GB；500-1000 → 12 vCPU / 16GB。更高规模按每 RAP 的 CPU/内存折算；超过 250 台 RAP 时建议部署第二台 VPN VA Server 分担。
  tags: [容量规划, vCPU, 内存, 扩容]

- id: p06
  title: 网卡与吞吐规划（1G vs 10G、NIC Teaming）
  type: principle
  source_chapter: "p14"
  source_quote: |
    "10 - 20Mbps expected VPN throughput per RAP, if local breakout is serving all internet needs. 20 - 100Mpbs expected VPN throughput per RAP, if all traffic is tunneled through VPN. 10G NIC is standard for more than 500 APs. For increased throughput use 2 x 10G NIC (NIC Teaming). ... The number of Virtual NICs supported by RAP VPN VA are limited only by the hypervisor."
  summary: |
    每台 RAP 预期 VPN 吞吐估算：Local Breakout 承担全部上网需求时 10-20 Mbps；全部流量走 VPN 隧道时 20-100 Mbps。超过 500 台 AP 标配 10G 网卡；需要更高吞吐用 2 块 10G 网卡做 NIC Teaming。虚拟网卡数量仅受 hypervisor 限制，RAP VPN VA 自身不设限。
  tags: [吞吐规划, 网卡选型, NIC-Teaming]

- id: p07
  title: VMware 部署要点与 ESXi 桥接网卡 VLAN/混杂模式设置
  type: principle
  source_chapter: "p14-20"
  source_quote: |
    "Configure VLAN 0 if you want Untagged VLAN traffic to be tunneled through VPN tunnels. Configure VLAN 4095 if you want Tagged VLAN traffic to be tunneled through VPN tunnels. On the ESXi VM, enable Promiscuous Mode for the above NIC. If the "Override" checkbox is enabled, make sure Promiscuous Mode, MAC address changes, and Forged transmits are set to "Accept"."
  summary: |
    VMware 部署：解压 OVF 包后只用 OVF 文件 + 两块 VMDK（disk 1/disk 2），导入前删除 *.mf 文件；磁盘置备（Disk provisioning）选 Thin；接受许可协议后完成部署。
    桥接流量专用网卡（无管理 IP 的接口）的 ESXi 端口组规则：非标记 VLAN 流量走隧道配 VLAN 0；标记 VLAN 流量走隧道配 VLAN 4095；必须为该网卡启用混杂模式（Promiscuous Mode）。若勾选 Override，混杂模式、MAC 地址变更（MAC address changes）、伪传输（Forged transmits）三项都要设为 Accept；端口组继承 vSwitch 时须确保 vSwitch0 三项均为 Accept，或在端口组直接设 Accept。
  tags: [VMware, ESXi, VLAN0, VLAN4095, 混杂模式]

- id: p08
  title: Hyper-V 部署：三网卡角色与 Trunk 配置
  type: principle
  source_chapter: "p24-32"
  source_quote: |
    "Use Eth0 for the public interface, Eth1 for the private interface, and Eth2 for the bridge interface. ... Select Enable virtual LAN identification on Eth0 and map to public VLAN (e.g., VLAN 70). ... Expand Eth2, under Advanced Features select the option Enable MAC address spoofing. ... Set-VMNetworkAdaptervlan -VMName OmniVista-VPN-4.9.2 -VMNetworkAdapterName "Eth2"-Trunk -AllowedVlanIdList "201,202" -NativeVlanId 0"
  summary: |
    Hyper-V 导入 OVF 包（ovnmse-vpn-4.9.2.2.ovf + 两块 vmdk，同样先删 *.mf，导入类型选 Copy the Virtual Machine）后：先删除原网卡，再用 PowerShell 循环创建 3 块网卡（Add-VMNetworkadapter，命名 Eth0/Eth1/Eth2），并建 External 虚拟交换机绑物理网卡。角色分配：Eth0 公网口（启用 VLAN 识别映射公网 VLAN，如 70）、Eth1 私网口（映射私网 VLAN，如 1000）、Eth2 桥接口（高级特性启用 MAC 地址欺骗），Eth2 再用 Set-VMNetworkAdapterVlan 配 Trunk 模式（示例 AllowedVlanIdList "201,202"、NativeVlanId 0），最后用 Get-VMNetworkAdapterVlan 验证后开机。
  tags: [Hyper-V, 三网卡, MAC地址欺骗, Trunk]

- id: p09
  title: Hyper-V NIC Teaming 兼容模式矩阵
  type: principle
  source_chapter: "p36-37"
  source_quote: |
    "Switch Independent / Switch Independent / Address Hash / None / Yes; Switch Independent / Switch Independent / Hyper-V Port / None / No; Switch Independent / Switch Independent / Dynamic / None / No; Linkagg static / Linkagg static / Dynamic / None / Yes; LACP / LACP / Dynamic / None / Yes"
  summary: |
    二层交换模式为 Switch Independent（交换机独立）时，只有 Address Hash 负载均衡可用（Stand-By 适配器为 None 或 NIC1/NIC2 均测试通过）；Hyper-V Port 与 Dynamic 两种负载均衡均不通过。二层为 Linkagg static（静态链路聚合）或 LACP 时，Address Hash / Hyper-V Port / Dynamic 三种负载均衡均通过（表中 Stand-By 均为 None）。NIC Teaming 需在 Server Manager→NIC Teaming 建组后，把虚拟交换机挂到 Teaming 接口、VM 网卡改用该交换机。
  tags: [NIC-Teaming, Hyper-V, LACP, 负载均衡]

- id: p10
  title: KVM/Ubuntu 22.04 部署要点（3 网卡 Macvtap、qcow2 unmap）
  type: principle
  source_chapter: "p37-50"
  source_quote: |
    "You have to setup 3 NICs with the VPN VA. The NIC format is below: Network Source: Macvtap device; Device name: Input the NIC name of Ubuntu; Device Model: default. ... Before beginning the installation (Step 18), reduce qcow2 disk size. Select VirtIO Disk 1 ... set the Discard Mode to unmap. Repeat for the VirtIO Disk 2."
  summary: |
    KVM 部署流程：Ubuntu 22.04 先 apt update，装 qemu-kvm / libvirt-clients / libvirt-daemon-system / virtinst / bridge-utils；导入两块 qcow2 磁盘（disk 0001/0002），OS 选 Generic Linux 2022；勾选 Customize configuration before install。必须配置 3 块网卡，格式统一为：Network Source = Macvtap device、Device name = Ubuntu 宿主机网卡名、Device Model = default。开始安装前，对两块 VirtIO 磁盘在 Advanced options→Performance options 中把 Discard Mode 设为 unmap 以缩减 qcow2 磁盘占用。
  tags: [KVM, Ubuntu, Macvtap, qcow2]

- id: p11
  title: VPN VA 初装与网络配置（含数据隧道网卡禁配 IP、OV 回程路由）
  type: principle
  source_chapter: "p51-59, p76-77"
  source_quote: |
    "To set up a Data Tunnel, you use the third NIC on the VA. You must not configure an IP address for this NIC because it will be a Layer 2 Tunnel. You also need to enable "Promiscuous Mode" for this NIC in your Hypervisor. ... Keep the default settings in the OVF for Guest OS, VM Compatibility and NIC type (E1000)"
  summary: |
    初装：保留 OVF 默认的 Guest OS / VM 兼容性 / 网卡类型（E1000）；控制台自动登录后依次完成键盘布局（默认 US）、空格翻页接受最终用户协议、设置 Admin 密码，重启后以 admin 登录主菜单。
    网络配置：NIC1 配 VPN 公网 IPv4（示例 10.255.222.97/24），NIC2 配连接 OVE 服务器的接口 IP；第三块网卡专用于 Data Tunnel，因为是二层（L2）隧道严禁配置 IP，且需在 hypervisor 为其开启混杂模式。随后按需配置网络路由、DNS、默认网关，并配置 SSH 服务（用于 SFTP 上传 VPN 设置文件，端口可自定义）；每步改完都要 Apply Configuration Changes 生效。
    回程路由（p76-77）：需在 VA 菜单 2→8→3（Add Route v4）添加路由，使 OmniVista 能到达 VPN VA 连接企业网的网卡网段（如 10.255.255.0/24），再用 2-Show Current Routes 核对。
  tags: [初装, E1000, L2隧道禁IP, SSH, 回程路由]

- id: p12
  title: VPN 设置文件的生命周期：导出时机、上传路径、同步规则
  type: principle
  source_chapter: "p61-63, p69"
  source_quote: |
    "Note that you do not have to wait until APs reach "Registered" status. Once APs are added to the Device Catalog you can export the VPN settings for the APs. ... SFTP the VPN Settings File (e.g., LAB4.conf) to the vpn_profile Directory (/opt/OmniVista_2500_NMS/data/vpn_conf/vpn_profile) on the VPN VA. ... Important Note: Do not change the name of the VPN Settings file. ... Any time you modify VPN settings you must generate a New VPN Settings File and FTP the file to the VPN Server."
  summary: |
    导出：Device Catalog 界面点 Export VPN Settings，AP 加入目录即可导出，无需等 Registered 状态；文件内容为全部 RAP 对端（Peer）的 WireGuard PublicKey 与 AllowedIPs（如 10.180.2.7/32），按 VPN Settings Name 命名（如 LAB4.conf）。上传：SFTP 到 VPN VA 的 /opt/OmniVista_2500_NMS/data/vpn_conf/vpn_profile 目录。同步规则：文件名不可改；导出后又向 Device Catalog 加 AP，必须重做导出/SFTP/在 VA 重新配置；任何 VPN 设置修改都必须重新生成文件并重新上传。
  tags: [VPN设置文件, SFTP, 同步规则, WireGuard密钥]

- id: p13
  title: VPN 服务创建与端点绑定：管理隧道选 None，数据隧道选无 IP 桥接网卡
  type: principle
  source_chapter: "p63-70"
  source_quote: |
    "Enter a name for the service after the underscore (e.g., vpn_management), then ... select the number of the NIC on which you want to create the service (e.g., 1). This is the NIC of the VPN VA Public IP address. Then ... enter the Port Number. ... select the interface for Regular VPN (e.g., 2 – None) ... select the interface for bridged traffic (e.g., 1 – eth2)"
  summary: |
    两步绑定规则：①Network Services→Configure a Network Service→VPN，创建 VPN 服务（命名如 vpn_management / vpn_data），绑定 VPN VA 公网 IP 所在网卡及公网端口号；②VPN Endpoints→Configure a VPN Endpoint，把 VPN 设置文件挂到该服务。端点接口选择是关键差异：管理隧道（Regular VPN）接口选 None；数据隧道必须选无 IP 的桥接网卡（如 eth2）承接桥接流量。配置后 Apply Configuration Changes 生效。
  tags: [VPN服务, 端点绑定, eth2]

- id: p14
  title: Data VPN 配置五步流程（AP Group 绑定为必做项）
  type: principle
  source_chapter: "p67-70"
  source_quote: |
    "Go to Network –> AP Registration -> Data VPN Server to add a Data VPN Server. ... Assign the Data VPN Server to the AP Group (mandatory to set up the Data VPN Tunnel). ... An L2GRE tunnel will be created between the Remote AP and the VPN Server and it will be used to tunnel the remote employee's data traffic. ... Be sure to select the right ethernet interface for bridging traffic (e.g., eth2 without IP Address)."
  summary: |
    数据隧道五步：①Network→AP Registration→Data VPN Server 新增（参数：Name / Server 公网 IP / Port / Server VPN IP / Client VPN IP 地址池，其中 Server's VPN IP 必须与客户端池同网段）；②编辑 AP Group（Network→AP Registration→AP Group）并绑定 Data VPN Server——不绑定则数据隧道建不起来（必做）；③Data VPN Servers 界面导出 VPN 设置文件（含全部 RAP 的公钥与 AllowedIPs，如 192.168.1.2/32）；④SFTP 上传到 vpn_profile 目录（不改名）；⑤配置 Data VPN 服务与端点，桥接接口选无 IP 的 eth2。RAP 与 VPN Server 之间最终建立 L2GRE 隧道承载员工数据流量。
  tags: [Data-VPN, AP-Group, L2GRE, 五步流程]

- id: p15
  title: 隧道 SSID 配置参数与 tagged/untagged VLAN
  type: principle
  source_chapter: "p71-73"
  source_quote: |
    "Allowed Band: All; Encryption Type: WPA3_AES; Default VLAN/Network: VLAN(s): untagged; Use Tunnel: checked; Tunnel ID:0; GRE Tunnel Server IP Address/data VPN Server: select profile created at previous section; Support of Entropy: Disabled; Allow Local Breakout: Disabled (will be supported with AWOS 4.0.1)"
  summary: |
    数据隧道 SSID 关键参数：Use Tunnel 勾选、Tunnel ID 填 0、GRE Tunnel Server IP/数据 VPN Server 选前一步创建的 profile、Allowed Band = All、加密 WPA3_AES、Support of Entropy 禁用、Allow Local Breakout 默认禁用；认证策略配 RADIUS（如 UPAMRadiusServer）。保存并关联 AP Group 后，OV2500 自动把配置推送给 RAP。
    VLAN 适配（p6、p71-73）：标记与非标记流量都能走 VPN 隧道，按 SSID 的 VLAN 字段配置；交换机侧命令——AOS 8.x：tagged 用 vlan [vlan_num] member port [port_num] tagged，untagged 用 ... untagged；AOS 6.x：tagged 用 vlan [vlan_num] 802.1q [port_num]，untagged 用 vlan [vlan_num] port default [port_num]。
  tags: [SSID, Tunnel-ID-0, WPA3, tagged-untagged, AOS命令]

- id: p16
  title: Local Breakout 静态路由三条硬规则
  type: principle
  source_chapter: "p73-74"
  source_quote: |
    "only one VLAN inside the tunnel (tunnel ID must be set to 0) can be enabled with Local Breakout. ... The static routes specified will be accumulated on an AP across all SSIDs assigned to the AP. ... make sure any destination IP subnet is specified only once. Each route applied on an AP should be for a different IP subnet, even across the SSIDs."
  summary: |
    ①隧道内只允许一个 VLAN 开启 Local Breakout，且该隧道 Tunnel ID 必须为 0；启用前须先把 Data VPN Server 应用到 AP Group。②静态路由在 AP 上跨所有 SSID 累积生效：SSID1 用 Tunnel Profile T1 配路由 A/B、SSID2 用 T2 配路由 C/D，则 A/B/C/D 对两个 SSID 都适用。③同一 AP 上每个目的 IP 子网只能配置一次，跨 SSID 也不得重复（同一子网 X 的路由已存在于某 SSID，就不得在同一 AP 的任何 SSID 再配）。④不要为进入隧道的 VLAN 对应网段手工配静态路由，AP 会自动生成（例：VLAN 41 / 192.168.41.0）。
  tags: [Local-Breakout, 静态路由, 路由累积, Tunnel-ID-0]

- id: p17
  title: License 要求：下行口认证需 Premium/Business 账号及三类 Profile 配置
  type: principle
  source_chapter: "p74-75"
  source_quote: |
    "If you have a Premium or Business Account, you can assign an Access Auth Profile to a Downlink Port on Stellar AP1201H, AP1201HL, and AP1311 Devices. ... you can select an Ethernet port(s) (up to 3 ports, depending on the AP model – Eth1, Eth2, Eth3). OmniVista will apply the profile to the selected ports on supported APs/ports in the AP Group and ignore unsupported APs/ports in the Group."
  summary: |
    账号等级门槛：只有 Premium 或 Business 账号才能给 Stellar AP1201H / AP1201HL / AP1311 的下行口（Downlink Port）分配 Access Auth Profile；分配时可选最多 3 个以太口（Eth1-Eth3，视型号），OmniVista 只应用到组内受支持的 AP/端口，不支持的自动忽略。本书无独立证书章节，证书/密钥相关仅两处：Device Catalog 注册 RAP 时预置 Security Keys（p4），VPN 设置文件中的 WireGuard PublicKey/AllowedIPs（p62/p68）。
    1201H 下行口隧道化（p74-75）：先在 Unified Access→Template→Tunnel Profile 建 Tunnel Profile，再到 Access Role Profile 选该 Profile 并以 Map to VLAN and Tunnel 方式应用到 AP Group，最后创建 Access Auth Profile（Unified Access→Template→Access Auth Profile）应用到 AP/AP Group。
  tags: [License, Premium-Business, Access-Auth-Profile, Tunnel-Profile, 1201H]

- id: p18
  title: DS-Lite ISP 场景的 TCPMSS/MTU 参数表与修改入口
  type: principle
  source_chapter: "p78"
  source_quote: |
    "TCPMSS: Management VPN Profile - GRE N/A, WG 1380, WG + DS-Lite 1352; Data VPN Profile - GRE N/A, WG 1380, WG + DS-Lite 1300. MTU: Data VPN/GRE Tunneling - GRE 1500, WG 1546, WG + DS-Lite 1376."
  summary: |
    ISP 路由器使用 DS-Lite（Dual Stack Lite）时按表调参：管理 VPN Profile 的 TCPMSS——GRE 不适用 / WG 1380 / WG+DS-Lite 1352；Data VPN Profile 的 TCPMSS——GRE 不适用 / WG 1380 / WG+DS-Lite 1300；数据 VPN/GRE 隧道 MTU——GRE 1500 / WG 1546 / WG+DS-Lite 1376。
    修改入口：管理 VPN TCPMSS 在 OV Cirrus Freemium 的 VPN Servers 界面；数据 VPN TCPMSS 在 OV2500/OV Cirrus 的 Network→AP Registration→Data VPN Server；隧道 MTU 在 WLAN→SSIDs 界面。
  tags: [DS-Lite, TCPMSS, MTU, 参数表]

- id: p19
  title: VPN VA 升级七步流程与约 5 分钟停机窗口
  type: principle
  source_chapter: "p79-80"
  source_quote: |
    "backup VPN Settings Files at the following directory: /opt/OmniVista_2500_NMS/data/vpn_conf/vpn_profile before upgrading. ... Shutdown the old VPN VA 4.9.1 Build 3. ... The RAP will be disconnected with the VPN VA from Step 4 to Step 7. The AP downtime happens in a short time ( ~ 5 minutes). ... The default Hard Disk size is 8GB for RAP VPN VA 4.9.2."
  summary: |
    升级前必须备份 /opt/OmniVista_2500_NMS/data/vpn_conf/vpn_profile 目录下的 VPN 设置文件。七步：①部署新 VPN VA 4.9.2.2；②三块网卡选与旧 VA 相同端口组但全部保持 disconnected；③配置除 VPN Endpoints 外的所有项（NIC/路由/DNS/网关/SSH/VPN 服务）；④关停旧 VPN VA（4.9.1 Build 3，一直运行到这一步）；⑤三块网卡改为 connected；⑥把备份的 VPN profile 导入新 VA 同目录；⑦按旧 VA 相同配置设置 VPN Endpoints。RAP 断连发生在第 4-7 步之间，停机约 5 分钟；流程同样适用于 VMware 与 Hyper-V；RAP VPN VA 4.9.2 默认硬盘 8GB。
  tags: [升级, 备份, 停机窗口, 8GB]

- id: p20
  title: 排障决策清单（隧道/注册/DHCP/LAN 四类故障定位）
  type: principle
  source_chapter: "p81-82"
  source_quote: |
    "If the AP Management VPN Tunnel is down: Check if tunnel interface was created using command "wg" on VPN VA ... Verify that the AP's IP Address is present in the VPN.conf file ... Verify that the firewall is not blocking traffic in both ways (from outside company, from VPN-VA). ... If both tunnels are UP but client does not get DHCP lease: Check if the client is present in the AP association list with command "ssudo sta_list""
  summary: |
    四类故障定位树：①管理隧道 down——在 VPN VA 上用 wg 查隧道接口是否创建（RAP 不可达时不在此执行）、AP 的 IP 是否在导入 VA 的 VPN.conf 中、防火墙是否双向放行（企业外部↔VPN-VA）。②管理隧道 up 但 AP 未注册到 OV——从 OV ping AP 地址、检查 OV 上是否配了到 AP wg0 子网的静态路由。③数据隧道 down——两侧 wg 查接口、配置是否已推送到 AP 的 /tmp/config/datavpn.conf、Data VPN Server 是否已映射到 AP Group、ifconfig wg1 是否拿到 IP、该 IP 是否在导入的 Data-VPN.conf、防火墙双向放行。④双隧道 up 但客户端拿不到 DHCP——sta_list 查关联与 TUNNELID/FARENDIP、brctl show 查桥接（ath0x 应关联 br-g1）、企业接入交换机是否学到客户端 MAC、检查 DHCP relay（ip helper、dhcp-snooping）。⑤客户端上不了 LAN——vSwitch 混杂模式默认 Reject 须改 Accept，Override 勾选时三项都须 Accept。
    日志与命令：VA 菜单收集 VPN VA 日志；RAP 日志经 OV（OVE/OVC）→Administration→Audit→Collect Support Info；cat /etc/config/rap.conf 查管理配置、cat /var/config/datavpn.conf 查数据配置；wg show 检查公钥/监听端口/对端 endpoint/allowed ips/握手时间/收发增量（示例 endpoint 198.206.185.132:9093，persistent keepalive 每 5 秒）；ip -d link 确认 gre0/gretap0/wg0 存在且 MTU 低于 1500（示例 gre0=1476、gretap0=1462、wg0=1420）。
  tags: [排障, wg命令, DHCP, 混杂模式, 日志收集]
