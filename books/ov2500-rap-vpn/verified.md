# 验证通过条目 · ov2500-rap-vpn（阶段 1.5 三重验证）

## 顶部汇总

| 类别 | 候选 | 通过 | 淘汰 | 说明 |
|---|---|---|---|---|
| 原则/规则/参数 | 20 | 20 | 0 | 全部通过 V1/V2/V3 |
| 陷阱/警告（反例） | 12 | 12 | 0 | 全部通过 V1/V2/V3 |
| 术语表 | 20 | 20 | 0 | 免验保留（规则约定）；抽检 9 条 quote 均命中原文 |
| **合计** | **52** | **52** | **0** | |

- 验证方法：V1 逐条比对 fulltext.md 中 `<<<PAGE N>>>` 页内原文（非抽查，32 条 principles/counter-examples 的 quote 全部逐句核对）；V2 按"VPN 配置参数 / 容量 / 排障决策树均算"的口径判定；V3 按产品专属、外部不可得知的信息判定。
- 页码修正 2 处（内容真实、出处页码标错，已就地修正，未淘汰）：
  - p06：quote 中 "The number of Virtual NICs supported..." 一句出自 p13，其余出自 p14，出处修正为 p13-14。
  - ce02：quote 第二句 "Remember, do not include the *.mf File..." 出自 p16（非 p24）；p24 有等价表述（"Delete the *.mf File ... before importing the files in Step 2"）。出处修正为 p14, p16（p24 等价）。
- 推断性表述标注 2 处（quote 真实，summary 含合理推断，下游引用时注意）：ce09"只能重部署"、ce02"导入失败或校验报错"为推断，原文未明说后果。
- 内容重叠提示（未构成淘汰理由）：ce01 与 p03 的版本矩阵重叠；p07 与 ce02 的 *.mf 提示重叠。蒸馏阶段可按用途分工（原则=正向操作，反例=踩坑警示）。

---

## 一、原则/规则/参数（20 条通过）

### p01 · 两种 VPN 模式的选择规则：OVE 全隧道 vs OVC 仅数据隧道
- 出处：p4-5（quote 命中 p4 L105-110、L121-126、L131；p5 L164）
- V1：quote 逐句命中，含 "technically not considered a RAP" 原句
- V2：直接决定要不要配 Management VPN Server 与密钥导出路径，是方案设计第一道分岔
- V3：OVC 管理的远程 AP"技术上不算 RAP"为厂商口径，外部无从得知
- 内容：
  - summary：模式选择规则：远程 AP 由企业本地 OVE 管理时，才是真正意义的 RAP，需要管理隧道 + 数据隧道两条 VPN；由 OVC 云管理时技术上不算 RAP（管理通道走 OVC 云内 OpenVPN，无需配置 Management VPN Server），只有需要把数据流量送回企业总部时才另建 Data VPN 隧道。配套的可达性原则（p4）：本地 AP 通过 DHCP option 138 获得 OV 地址被直接管理；远程站点 AP 对企业 OV 不可直达，连接与管理通信必须走 VPN 隧道。协议清单：管理隧道 WireGuard（OVE 模式）/ OpenVPN（OVC 模式），数据隧道为 WireGuard 配置下的 L2GRE 隧道。
  - tags: [VPN模式, RAP, OVE, OVC, WireGuard, OpenVPN]

### p02 · 两种模式下 RAP 的注册与建隧道流程
- 出处：p4-5（quote 命中 p4 L128-136、L139-142；p5 L162-168）
- V1：五步/四步流程原句逐句命中
- V2：交付顺序清单——先 Device Catalog 注册、再导密钥、后建隧道，顺序错则隧道建不起来
- V3：开箱首连 OVC Device Registration Server 取回 OVE IP 的机制为产品专属
- 内容：
  - summary：OVE 管理流程五步：①开箱首连 OVC Device Registration Server，取回 RAP 参数（含目标 OVE IP）；②密钥与参数导出到总部 RAP VPN Server；③建立 Wireguard 管理 VPN 隧道，经隧道接受 OVE 管理；④在 OVE 上配置 RAP→VPN Server 的 Data VPN 隧道并导出密钥；⑤数据隧道建立后承载终端业务。管理员需先在 OVC Device Catalog 把 AP 注册为 RAP，以便预置 VPN VA 公网 IP / OVE 内网 IP / 安全密钥（Security Keys）——这是本书密钥预置的唯一出处。OVC 管理流程四步（p5）：①开箱首连 OVC Device Registration Server 确认注册；②AP 建 OpenVPN 连接由 OVC 管理；③在 OVC 上配置 Data VPN 隧道并导出密钥参数到总部 VPN Server；④隧道承载业务。WLAN 服务配置在管理方（OVE 或 OVC）侧完成。
  - tags: [注册流程, 密钥导出, Wireguard, OpenVPN]

### p03 · 平台与版本前置条件
- 出处：p5（quote 命中 L180-189；KVM 部署见 p37 L815）
- V1：版本矩阵原句逐字命中
- V2：开工前核对清单（ESXi/Hyper-V/AWOS/VA 版本配套），任何一项不满足即返工
- V3：具体版本号组合（如 ESXi 5.5 被排除、VA 4.9.2.2 与 OV2500 4.9R2/OVC 4.9.2 认证配套）为厂商兼容性口径
- 备注：与 ce01（ESXi 5.5 反例）信息重叠，蒸馏时分工
- 内容：
  - summary：前置条件清单：ESXi 支持 6.5/6.7/7.0.2/8.0（5.5 明确不支持）；Hyper-V 支持 2016/2019/2022；Stellar RAP 需 AWOS 5.0.2 及以上（最新特性也要求 5.0.2+）；RAP VPN VA 版本 4.9.2.2；该 VA 与 OV2500 4.9R2、OVC 4.9.2 认证配套。另支持在 Ubuntu 22.04 LTS + KVM 上部署。
  - tags: [版本兼容, ESXi, Hyper-V, AWOS, KVM]

### p04 · Freemium 账号、Device Catalog 注册与 VPN Server 参数定义
- 出处：p6-12（quote 命中 p10 L311-321、p11 L335-336；其余细节 p6 L213-215、p7 L241-247、p8 L264-270、p10 L304-307、p12 L364-365）
- V1：三段参数定义原句命中
- V2：四个 VPN Server 参数的准确语义（Public IP=公网出口、VPN IP=须与客户端池同网段）+ "先定 VPN Server 再加 AP"的顺序约束，直接防返工
- V3：参数语义与菜单路径（Network→Inventory→Device Catalog、Create New/Choose Existing）为产品专属
- 内容：
  - summary：添加 RAP 前先建 OmniVista Cirrus Freemium 账号（registration.ovcirrus.com 注册，邮件验证链接来自 noreply@ovcirrus.com，邮件正文含设备 OS 软件下载链接）。规划规则：Device Catalog（Network→Inventory→Device Catalog）加 AP 时要填第 3 步才部署的 VPN Server 信息，必须先确定 VPN Server 配置再开工。VPN Settings 首次用 Create New，保存后后续 AP 可直接 Choose Existing 复用。参数定义：Server's Public IP = RAP 连接 VPN Server 的公网地址（企业网流向远端的出口接口）；Port = 公网端口；Server's VPN IP = 虚拟网络内私网 IP，必须与客户端地址池同网段（远端流量进入企业网的隧道接口）；Client VPN IP Address Pool = 分配给 RAP 的地址段（IP 范围 + 简写掩码/子网掩码）。批量导入用 CSV，模板中 RAP 字段须为 TRUE 才能携带 VpnSettingName。
  - tags: [Freemium, Device-Catalog, VPN参数, CSV导入]

### p05 · VPN VA 容量配置按 RAP 数量分档
- 出处：p13（quote 命中 L389-398，逐字）
- V1：4 档容量 + 250 台建议二台原句逐字命中
- V2：容量规划表，直接对应 vCPU/内存资源配置与扩容决策（超过 250 台加第二台）
- V3：具体分档数值为厂商推荐口径，外部不可得知
- 内容：
  - summary：VPN VA 规格 4 档：1-100 台 AP → 4 vCPU / 2GB 内存；100-250 → 6 vCPU / 4GB；250-500 → 8 vCPU / 8GB；500-1000 → 12 vCPU / 16GB。更高规模按每 RAP 的 CPU/内存折算；超过 250 台 RAP 时建议部署第二台 VPN VA Server 分担。
  - tags: [容量规划, vCPU, 内存, 扩容]

### p06 · 网卡与吞吐规划（1G vs 10G、NIC Teaming）
- 出处：p14（**修正：原标 p14；quote 末句 "The number of Virtual NICs..." 实出自 p13 L384-385，出处应为 p13-14**）
- V1：吞吐两句 + 10G 两句命中 p14 L411-418（含原文拼写 "100Mpbs" 均一致）；末句命中 p13
- V2：每 RAP 10-20 / 20-100 Mbps 两档吞吐估算 + 500 台上 10G、双 10G Teaming 的选型依据
- V3：吞吐基准数值与"虚拟网卡数仅受 hypervisor 限制"为手册口径
- 内容：
  - summary：每台 RAP 预期 VPN 吞吐估算：Local Breakout 承担全部上网需求时 10-20 Mbps；全部流量走 VPN 隧道时 20-100 Mbps。超过 500 台 AP 标配 10G 网卡；需要更高吞吐用 2 块 10G 网卡做 NIC Teaming。虚拟网卡数量仅受 hypervisor 限制，RAP VPN VA 自身不设限。
  - tags: [吞吐规划, 网卡选型, NIC-Teaming]

### p07 · VMware 部署要点与 ESXi 桥接网卡 VLAN/混杂模式设置
- 出处：p14-20（quote 命中 p20 L517-526 逐字；*.mf/Thin 见 p14 L433-435、p18 L486；vSwitch 继承见 p20 L529-531）
- V1：VLAN 0 / VLAN 4095 / 混杂模式 / Override 三项 Accept 原句逐字命中
- V2：ESXi 端口组具体设置值（0=untagged、4095=tagged、三项安全策略 Accept），照做即可
- V3：VLAN 0/4095 承载桥接流量的约定是该 VA 的专属配置手法
- 备注：与 ce02（*.mf 反例）信息重叠，蒸馏时分工
- 内容：
  - summary：VMware 部署：解压 OVF 包后只用 OVF 文件 + 两块 VMDK（disk 1/disk 2），导入前删除 *.mf 文件；磁盘置备（Disk provisioning）选 Thin；接受许可协议后完成部署。桥接流量专用网卡（无管理 IP 的接口）的 ESXi 端口组规则：非标记 VLAN 流量走隧道配 VLAN 0；标记 VLAN 流量走隧道配 VLAN 4095；必须为该网卡启用混杂模式（Promiscuous Mode）。若勾选 Override，混杂模式、MAC 地址变更（MAC address changes）、伪传输（Forged transmits）三项都要设为 Accept；端口组继承 vSwitch 时须确保 vSwitch0 三项均为 Accept，或在端口组直接设 Accept。
  - tags: [VMware, ESXi, VLAN0, VLAN4095, 混杂模式]

### p08 · Hyper-V 部署：三网卡角色与 Trunk 配置
- 出处：p24-32（quote 命中 p29 L655-659、p31 L682-683、p32 L694-697 逐字；流程细节 p24 L581-585、p25 L600、p27 L625-633、p30 L670-671、p32 L698-701）
- V1：Eth0/Eth1/Eth2 角色句、VLAN 70 句、MAC 欺骗句、Set-VMNetworkAdaptervlan 命令逐字命中（命令含换行拼接一致）
- V2：PowerShell 建网卡循环、Trunk 命令（AllowedVlanIdList "201,202"、NativeVlanId 0）、验证命令全套可直接执行
- V3：三网卡角色命名与具体命令组合为本书专属
- 内容：
  - summary：Hyper-V 导入 OVF 包（ovnmse-vpn-4.9.2.2.ovf + 两块 vmdk，同样先删 *.mf，导入类型选 Copy the Virtual Machine）后：先删除原网卡，再用 PowerShell 循环创建 3 块网卡（Add-VMNetworkadapter，命名 Eth0/Eth1/Eth2），并建 External 虚拟交换机绑物理网卡。角色分配：Eth0 公网口（启用 VLAN 识别映射公网 VLAN，如 70）、Eth1 私网口（映射私网 VLAN，如 1000）、Eth2 桥接口（高级特性启用 MAC 地址欺骗），Eth2 再用 Set-VMNetworkAdapterVlan 配 Trunk 模式（示例 AllowedVlanIdList "201,202"、NativeVlanId 0），最后用 Get-VMNetworkAdapterVlan 验证后开机。
  - tags: [Hyper-V, 三网卡, MAC地址欺骗, Trunk]

### p09 · Hyper-V NIC Teaming 兼容模式矩阵
- 出处：p36-37（quote 为兼容表 9 行的忠实压缩，逐行核对 L750-813；Server Manager 建组 p33 L712-714、挂交换机 p35 L734-736）
- V1：5 行抽样（含全部 No 行与 LACP/Dynamic 行）与表格逐行一致；summary 中"Stand-By None 或 NIC1/NIC2 均通过"亦与 L754-757 一致
- V2：组队前查表选组合（Switch Independent 下只能 Address Hash），防配错返工
- V3：实测兼容矩阵（哪些组合 Worked?=No）是本书独有的实验结论
- 内容：
  - summary：二层交换模式为 Switch Independent（交换机独立）时，只有 Address Hash 负载均衡可用（Stand-By 适配器为 None 或 NIC1/NIC2 均测试通过）；Hyper-V Port 与 Dynamic 两种负载均衡均不通过。二层为 Linkagg static（静态链路聚合）或 LACP 时，Address Hash / Hyper-V Port / Dynamic 三种负载均衡均通过（表中 Stand-By 均为 None）。NIC Teaming 需在 Server Manager→NIC Teaming 建组后，把虚拟交换机挂到 Teaming 接口、VM 网卡改用该交换机。
  - tags: [NIC-Teaming, Hyper-V, LACP, 负载均衡]

### p10 · KVM/Ubuntu 22.04 部署要点（3 网卡 Macvtap、qcow2 unmap）
- 出处：p37-50（quote 命中 p49 L976-982、p50 L994-996 逐字；apt/Generic Linux 2022/Customize 见 p37 L820-824、p40 L868-869、p44 L915-916）
- V1：Macvtap 三要素与 unmap 两句原句逐字命中
- V2：网卡三元组（Macvtap/宿主网卡名/default）与两块盘 Discard=unmap 为部署必做项
- V3：Macvtap 格式限定与 unmap 缩盘手法是该 VA 的 KVM 专属要求
- 内容：
  - summary：KVM 部署流程：Ubuntu 22.04 先 apt update，装 qemu-kvm / libvirt-clients / libvirt-daemon-system / virtinst / bridge-utils；导入两块 qcow2 磁盘（disk 0001/0002），OS 选 Generic Linux 2022；勾选 Customize configuration before install。必须配置 3 块网卡，格式统一为：Network Source = Macvtap device、Device name = Ubuntu 宿主机网卡名、Device Model = default。开始安装前，对两块 VirtIO 磁盘在 Advanced options→Performance options 中把 Discard Mode 设为 unmap 以缩减 qcow2 磁盘占用。
  - tags: [KVM, Ubuntu, Macvtap, qcow2]

### p11 · VPN VA 初装与网络配置（含数据隧道网卡禁配 IP、OV 回程路由）
- 出处：p51-59, p76-77（quote 命中 p55 L1088-1090、p51 L1009-1010 逐字；初装 p52-53、NIC 配置 p54-55、SSH p59-60、回程路由菜单 p76-77 L1614-1631）
- V1：L2 隧道禁配 IP + 混杂模式句、E1000 默认句逐字命中
- V2：菜单路径（2→8→3 加回程路由 10.255.255.0/24）、每步 Apply 的操作链，含排障高频回程路由问题
- V3：第三网卡禁 IP 的 L2 约束与 E1000 默认值为该 VA 专属
- 备注：禁配 IP 与 ce05 反例互为正反表述，蒸馏时分工
- 内容：
  - summary：初装：保留 OVF 默认的 Guest OS / VM 兼容性 / 网卡类型（E1000）；控制台自动登录后依次完成键盘布局（默认 US）、空格翻页接受最终用户协议、设置 Admin 密码，重启后以 admin 登录主菜单。网络配置：NIC1 配 VPN 公网 IPv4（示例 10.255.222.97/24），NIC2 配连接 OVE 服务器的接口 IP；第三块网卡专用于 Data Tunnel，因为是二层（L2）隧道严禁配置 IP，且需在 hypervisor 为其开启混杂模式。随后按需配置网络路由、DNS、默认网关，并配置 SSH 服务（用于 SFTP 上传 VPN 设置文件，端口可自定义）；每步改完都要 Apply Configuration Changes 生效。回程路由（p76-77）：需在 VA 菜单 2→8→3（Add Route v4）添加路由，使 OmniVista 能到达 VPN VA 连接企业网的网卡网段（如 10.255.255.0/24），再用 2-Show Current Routes 核对。
  - tags: [初装, E1000, L2隧道禁IP, SSH, 回程路由]

### p12 · VPN 设置文件的生命周期：导出时机、上传路径、同步规则
- 出处：p61-63, p69（quote 命中 p62 L1237-1239、L1248-1250、p63 L1261-1262 逐字；PublicKey/AllowedIPs 示例 L1243-1245）
- V1：四段引用（无需 Registered 即可导出、SFTP 路径、禁改名、改配置必重传）逐字命中
- V2：文件同步的完整生命周期规则，配错即隧道与目录不一致
- V3：vpn_profile 目录全路径与 WireGuard Peer 文件格式为产品专属
- 备注：正向规则与 ce04（三类失效场景反例）互为补充
- 内容：
  - summary：导出：Device Catalog 界面点 Export VPN Settings，AP 加入目录即可导出，无需等 Registered 状态；文件内容为全部 RAP 对端（Peer）的 WireGuard PublicKey 与 AllowedIPs（如 10.180.2.7/32），按 VPN Settings Name 命名（如 LAB4.conf）。上传：SFTP 到 VPN VA 的 /opt/OmniVista_2500_NMS/data/vpn_conf/vpn_profile 目录。同步规则：文件名不可改；导出后又向 Device Catalog 加 AP，必须重做导出/SFTP/在 VA 重新配置；任何 VPN 设置修改都必须重新生成文件并重新上传。
  - tags: [VPN设置文件, SFTP, 同步规则, WireGuard密钥]

### p13 · VPN 服务创建与端点绑定：管理隧道选 None，数据隧道选无 IP 桥接网卡
- 出处：p63-70（quote 命中 p64 L1281-1285、p66 L1321-1322、p70 L1422-1423）
- V1：三段引用原句命中（省略处为菜单导航文字，不影响语义）
- V2：两步绑定的菜单路径 + 端点接口选择的关键差异（Regular VPN→None；数据→无 IP eth2），是建隧道的临门一脚
- V3：接口选择规则（管理 None / 数据桥接网卡）为该 VA 菜单专属逻辑
- 内容：
  - summary：两步绑定规则：①Network Services→Configure a Network Service→VPN，创建 VPN 服务（命名如 vpn_management / vpn_data），绑定 VPN VA 公网 IP 所在网卡及公网端口号；②VPN Endpoints→Configure a VPN Endpoint，把 VPN 设置文件挂到该服务。端点接口选择是关键差异：管理隧道（Regular VPN）接口选 None；数据隧道必须选无 IP 的桥接网卡（如 eth2）承接桥接流量。配置后 Apply Configuration Changes 生效。
  - tags: [VPN服务, 端点绑定, eth2]

### p14 · Data VPN 配置五步流程（AP Group 绑定为必做项）
- 出处：p67-70（quote 命中 p67 L1343、p68 L1376、p67 L1340-1342、p69 L1402-1403 逐字）
- V1：四段引用逐字命中
- V2：五步操作链 + "AP Group 不绑定则隧道建不起来"的强制项标注
- V3：L2GRE 承载数据流量与导出文件含 192.168.1.2/32 样例为本书口径
- 内容：
  - summary：数据隧道五步：①Network→AP Registration→Data VPN Server 新增（参数：Name / Server 公网 IP / Port / Server VPN IP / Client VPN IP 地址池，其中 Server's VPN IP 必须与客户端池同网段）；②编辑 AP Group（Network→AP Registration→AP Group）并绑定 Data VPN Server——不绑定则数据隧道建不起来（必做）；③Data VPN Servers 界面导出 VPN 设置文件（含全部 RAP 的公钥与 AllowedIPs，如 192.168.1.2/32）；④SFTP 上传到 vpn_profile 目录（不改名）；⑤配置 Data VPN 服务与端点，桥接接口选无 IP 的 eth2。RAP 与 VPN Server 之间最终建立 L2GRE 隧道承载员工数据流量。
  - tags: [Data-VPN, AP-Group, L2GRE, 五步流程]

### p15 · 隧道 SSID 配置参数与 tagged/untagged VLAN
- 出处：p71-73（quote 命中 p71 L1452-1461 逐字；AOS 命令 p73 L1508-1522；p6 L218）
- V1：SSID 参数块逐字命中（含 "will be supported with AWOS 4.0.1" 原句）
- V2：SSID 关键参数值（Use Tunnel 勾选、Tunnel ID 0、选 Data VPN Server profile）+ AOS 8.x/6.x 四条交换机命令，可直接照配
- V3：Tunnel ID 0 的含义与 Support of Entropy/Allow Local Breakout 默认值为产品参数
- 备注："AWOS 4.0.1" 口径疑为文档笔误，见 ce11
- 内容：
  - summary：数据隧道 SSID 关键参数：Use Tunnel 勾选、Tunnel ID 填 0、GRE Tunnel Server IP/数据 VPN Server 选前一步创建的 profile、Allowed Band = All、加密 WPA3_AES、Support of Entropy 禁用、Allow Local Breakout 默认禁用；认证策略配 RADIUS（如 UPAMRadiusServer）。保存并关联 AP Group 后，OV2500 自动把配置推送给 RAP。VLAN 适配（p6、p71-73）：标记与非标记流量都能走 VPN 隧道，按 SSID 的 VLAN 字段配置；交换机侧命令——AOS 8.x：tagged 用 vlan [vlan_num] member port [port_num] tagged，untagged 用 ... untagged；AOS 6.x：tagged 用 vlan [vlan_num] 802.1q [port_num]，untagged 用 vlan [vlan_num] port default [port_num]。
  - tags: [SSID, Tunnel-ID-0, WPA3, tagged-untagged, AOS命令]

### p16 · Local Breakout 静态路由三条硬规则
- 出处：p73-74（quote 命中 p73 L1533-1534、p74 L1557-1558、L1563-1565 逐字）
- V1：三段引用逐字命中
- V2：三条硬约束（单 VLAN+Tunnel ID 0 / 跨 SSID 累积 / 子网唯一）+ 禁配隧道 VLAN 网段路由，是 Local Breakout 的配置红线
- V3：路由跨 SSID 累积语义与自动路由机制为产品行为，外部不可得知
- 备注：与 ce07（三类路由错误反例）互为正反表述
- 内容：
  - summary：①隧道内只允许一个 VLAN 开启 Local Breakout，且该隧道 Tunnel ID 必须为 0；启用前须先把 Data VPN Server 应用到 AP Group。②静态路由在 AP 上跨所有 SSID 累积生效：SSID1 用 Tunnel Profile T1 配路由 A/B、SSID2 用 T2 配路由 C/D，则 A/B/C/D 对两个 SSID 都适用。③同一 AP 上每个目的 IP 子网只能配置一次，跨 SSID 也不得重复（同一子网 X 的路由已存在于某 SSID，就不得在同一 AP 的任何 SSID 再配）。④不要为进入隧道的 VLAN 对应网段手工配静态路由，AP 会自动生成（例：VLAN 41 / 192.168.41.0）。
  - tags: [Local-Breakout, 静态路由, 路由累积, Tunnel-ID-0]

### p17 · License 要求：下行口认证需 Premium/Business 账号及三类 Profile 配置
- 出处：p74-75（quote 命中 p75 L1592-1601 逐字；Tunnel Profile 流程 p74 L1572-1578、p75 L1589-1590）
- V1：账号门槛句 + 最多 3 口（Eth1-Eth3）+ 忽略不支持端口句逐字命中
- V2：账号等级门槛决定功能可用性（售前/交付核对项），三类 Profile 的配置顺序可直接照做
- V3：Premium/Business 才能配下行口认证、支持的三个具体型号（AP1201H/1201HL/AP1311）为商业与产品口径
- 内容：
  - summary：账号等级门槛：只有 Premium 或 Business 账号才能给 Stellar AP1201H / AP1201HL / AP1311 的下行口（Downlink Port）分配 Access Auth Profile；分配时可选最多 3 个以太口（Eth1-Eth3，视型号），OmniVista 只应用到组内受支持的 AP/端口，不支持的自动忽略。本书无独立证书章节，证书/密钥相关仅两处：Device Catalog 注册 RAP 时预置 Security Keys（p4），VPN 设置文件中的 WireGuard PublicKey/AllowedIPs（p62/p68）。1201H 下行口隧道化（p74-75）：先在 Unified Access→Template→Tunnel Profile 建 Tunnel Profile，再到 Access Role Profile 选该 Profile 并以 Map to VLAN and Tunnel 方式应用到 AP Group，最后创建 Access Auth Profile（Unified Access→Template→Access Auth Profile）应用到 AP/AP Group。
  - tags: [License, Premium-Business, Access-Auth-Profile, Tunnel-Profile, 1201H]

### p18 · DS-Lite ISP 场景的 TCPMSS/MTU 参数表与修改入口
- 出处：p78（quote 为两张参数表的忠实文本化，数值逐项核对 L1652-1671；修改入口 L1673-1682）
- V1：TCPMSS（N/A/1380/1352 与 N/A/1380/1300）及 MTU（1500/1546/1376）九个数值与表格逐项一致
- V2：DS-Lite 场景直接查表调参，且给出三个参数各自的界面修改入口（Freemium VPN Servers / Data VPN Server / SSIDs）
- V3：具体数值组合为厂商调优口径，外部不可得知
- 内容：
  - summary：ISP 路由器使用 DS-Lite（Dual Stack Lite）时按表调参：管理 VPN Profile 的 TCPMSS——GRE 不适用 / WG 1380 / WG+DS-Lite 1352；Data VPN Profile 的 TCPMSS——GRE 不适用 / WG 1380 / WG+DS-Lite 1300；数据 VPN/GRE 隧道 MTU——GRE 1500 / WG 1546 / WG+DS-Lite 1376。修改入口：管理 VPN TCPMSS 在 OV Cirrus Freemium 的 VPN Servers 界面；数据 VPN TCPMSS 在 OV2500/OV Cirrus 的 Network→AP Registration→Data VPN Server；隧道 MTU 在 WLAN→SSIDs 界面。
  - tags: [DS-Lite, TCPMSS, MTU, 参数表]

### p19 · VPN VA 升级七步流程与约 5 分钟停机窗口
- 出处：p79-80（quote 命中 p79 L1694-1695、L1706、p80 L1727-1728、L1730 逐字；七步 L1696-1720）
- V1：备份目录句、关停旧 VA 句、断连窗口句、8GB 默认盘句逐字命中
- V2：升级步骤顺序（新 VA 先 dis-connected 部署、旧 VA 跑到第 4 步）+ 停机窗口（约 5 分钟）直接用于割接方案
- V3：断连发生在第 4-7 步的范围界定与 8GB 默认硬盘为手册口径
- 内容：
  - summary：升级前必须备份 /opt/OmniVista_2500_NMS/data/vpn_conf/vpn_profile 目录下的 VPN 设置文件。七步：①部署新 VPN VA 4.9.2.2；②三块网卡选与旧 VA 相同端口组但全部保持 disconnected；③配置除 VPN Endpoints 外的所有项（NIC/路由/DNS/网关/SSH/VPN 服务）；④关停旧 VPN VA（4.9.1 Build 3，一直运行到这一步）；⑤三块网卡改为 connected；⑥把备份的 VPN profile 导入新 VA 同目录；⑦按旧 VA 相同配置设置 VPN Endpoints。RAP 断连发生在第 4-7 步之间，停机约 5 分钟；流程同样适用于 VMware 与 Hyper-V；RAP VPN VA 4.9.2 默认硬盘 8GB。
  - tags: [升级, 备份, 停机窗口, 8GB]

### p20 · 排障决策清单（隧道/注册/DHCP/LAN 四类故障定位）
- 出处：p81-82（quote 命中 p81 L1742-1745、L1747、L1749-1750、L1773-1775 逐字，含原文命令拼写 "ssudo sta_list"；命令与输出示例 L1795-1871）
- V1：四段引用逐字命中；summary 中 wg show 输出（endpoint 198.206.185.132:9093、keepalive 5 秒）、ip -d link 三接口 MTU（1476/1462/1420）均与原文一致
- V2：五类故障的逐条排查命令（wg/ifconfig wg1/sta_list/brctl show/cat rap.conf 等），典型排障决策树，V2 的样板条目
- V3：命令输出基线（MTU 数值、br-g1 桥接关系）为实测样例，外部无从得知
- 内容：
  - summary：四类故障定位树：①管理隧道 down——在 VPN VA 上用 wg 查隧道接口是否创建（RAP 不可达时不在此执行）、AP 的 IP 是否在导入 VA 的 VPN.conf 中、防火墙是否双向放行（企业外部↔VPN-VA）。②管理隧道 up 但 AP 未注册到 OV——从 OV ping AP 地址、检查 OV 上是否配了到 AP wg0 子网的静态路由。③数据隧道 down——两侧 wg 查接口、配置是否已推送到 AP 的 /tmp/config/datavpn.conf、Data VPN Server 是否已映射到 AP Group、ifconfig wg1 是否拿到 IP、该 IP 是否在导入的 Data-VPN.conf、防火墙双向放行。④双隧道 up 但客户端拿不到 DHCP——sta_list 查关联与 TUNNELID/FARENDIP、brctl show 查桥接（ath0x 应关联 br-g1）、企业接入交换机是否学到客户端 MAC、检查 DHCP relay（ip helper、dhcp-snooping）。⑤客户端上不了 LAN——vSwitch 混杂模式默认 Reject 须改 Accept，Override 勾选时三项都须 Accept。日志与命令：VA 菜单收集 VPN VA 日志；RAP 日志经 OV（OVE/OVC）→Administration→Audit→Collect Support Info；cat /etc/config/rap.conf 查管理配置、cat /var/config/datavpn.conf 查数据配置；wg show 检查公钥/监听端口/对端 endpoint/allowed ips/握手时间/收发增量（示例 endpoint 198.206.185.132:9093，persistent keepalive 每 5 秒）；ip -d link 确认 gre0/gretap0/wg0 存在且 MTU 低于 1500（示例 gre0=1476、gretap0=1462、wg0=1420）。
  - tags: [排障, wg命令, DHCP, 混杂模式, 日志收集]

---

## 二、陷阱/警告（反例，12 条通过）

### ce01 · ESXi 5.5 不被支持
- 出处：p5（quote 命中 L180 逐字）
- V1：命中；V2：虚拟化平台选型/迁移前核对项；V3：5.5 被排除为该 VA 的兼容口径
- 备注：与 p03 版本矩阵重叠，保留理由是反例视角（规划老环境迁移时的专项警示）
- summary：陷阱：在 ESXi 5.5 老环境上部署 RAP VPN VA。前置条件明确 6.5/6.7/7.0.2/8.0 可用，5.5 被排除；Hyper-V 则要求 2016/2019/2022。规划迁移或新建 hypervisor 时先核对版本。
- tags: [版本兼容, ESXi]

### ce02 · 导入虚拟机时未删除 *.mf 文件
- 出处：**修正：p14（L433-435）+ p16（L462-463）；原标 p24 处实为等价表述（L583-585）**
- V1：两段 quote 均逐字命中原文（p14 + p16），p24 另有等价句
- V2：两条部署路径（VMware/Hyper-V）均强制的前置动作，漏做即卡在导入步骤
- V3：*.mf 必删 + 只保留 ovf 与两块 vmdk（ovnmse-vpn-4.9.2.2-disk001/002）为本书明确要求
- 备注（推断标注）："否则导入失败或校验报错"为合理推断，原文未明说后果
- summary：陷阱：把 OVF 包里自带的 *.mf 清单文件一并选入导入。VMware 与 Hyper-V 两条路径都被强调：导入前只保留 OVF 文件 + 两块 VMDK，*.mf 必须先从目录删除。
- tags: [OVF导入, mf文件]

### ce03 · RAP VPN VA 不支持冗余——不能按 HA 设计
- 出处：p14（quote 命中 L424-426 逐字）
- V1：命中；V2：架构设计红线——按单点设备评估 SLA 与割接窗口；V3："不支持冗余"为 Known Limitations 明文，外部不可得知
- summary：陷阱：给 VPN VA 做双机热备/高可用设计。已知限制明确 RAP VPN VA 不支持冗余；规模增长（超过 250 台 RAP）官方建议是部署第二台 VPN VA 分担（p13），而非主备冗余。
- tags: [无冗余, 高可用, 容量拆分]

### ce04 · VPN 设置文件三类失效场景：改名、改配置不重传、导出后又加 AP
- 出处：p61-63, p69（quote 命中 p61 L1222-1224、p62 L1250、p63 L1261-1262、p69 L1399 逐字）
- V1：四段引用逐字命中；V2：三类失效场景即三条运维检查项；V3：失效触发条件为产品行为
- summary：三个常见踩坑：①手工改名 VPN 设置文件导致 VA 识别失败；②修改 VPN 设置后未重新导出并 SFTP 上传；③导出后又加 AP，新 AP 的公钥不在旧文件里，必须重做"导出→SFTP→VA 重配"全流程。管理隧道与数据隧道的设置文件同规则。
- tags: [VPN设置文件, 改名, 配置漂移]

### ce05 · 给数据隧道桥接网卡误配 IP 地址
- 出处：p55, p69（quote 命中 p55 L1088-1090、p69 L1402-1403 逐字）
- V1：命中；V2：第三网卡（Eth2）禁 IP + 开混杂模式为配置红线；V3：L2 桥接禁 IP 的要求为该方案专属
- summary：陷阱：按习惯给第三块网卡配 IP。数据隧道是二层（L2）桥接，该网卡必须无 IP，且要在 hypervisor 开混杂模式；VPN Endpoints 配数据隧道时也要选对这块无 IP 网卡（如 eth2）。
- tags: [L2隧道, 网卡误配IP, 桥接]

### ce06 · vSwitch 混杂模式默认 Reject 且 Override 未全设 Accept
- 出处：p20, p81（quote 命中 p20 L524-526、p81 L1787-1789、L1791-1792 逐字）
- V1：命中；V2：排障章节"客户端不通 LAN"首要检查项，含默认值 Reject 与 Override 陷阱两层；V3：默认值与三项安全策略组合为 ESXi 承载该 VA 的专属坑
- summary：陷阱一：ESXi vSwitch/端口组的混杂模式出厂默认 Reject，不开启则双隧道都 up、客户端仍无法访问同网段任何设备/网关。陷阱二：只在端口组开了混杂模式但 Override 勾选未生效，或三项（Promiscuous Mode、MAC address changes、Forged transmits）没有全部设为 Accept；端口组"Inherit from vSwitch"时若 vSwitch0 是 Reject 同样失效。
- tags: [混杂模式, vSwitch, Override]

### ce07 · Local Breakout 静态路由三类重叠/重复错误
- 出处：p73-74, p84（quote 命中 p73 L1544-1546、p74 L1567-1569、p84 L1932-1934 逐字）
- V1：命中；V2：三类错误各自对应一种真实故障（AP 混乱/性能降级、子网冲突、AP 与本地网失联），配置前避让清单；V3：AP 自动生成隧道 VLAN 路由、跨 SSID 累积语义为产品行为
- summary：三类错误：①为进入隧道的 VLAN 网段手工配路由——AP 会自动生成，显式再配会让 AP 混乱、性能下降；②跨 SSID 重复——静态路由在 AP 上跨所有 SSID 累积，同一目的子网在同一 AP 的任何 SSID 上都只能出现一次；③Local Breakout 路由与 AP 本地网络网段重叠——AP 自己访问本地网段的包会被推进隧道发往总部，导致 AP 与本地网失联。
- tags: [Local-Breakout, 路由重叠, 跨SSID重复]

### ce08 · Hyper-V NIC Teaming 选了不兼容的负载均衡组合
- 出处：p36-37（quote 四行 No 记录与表格 L758-773 逐行一致）
- V1：命中；V2：组队前查兼容矩阵（Switch Independent 仅 Address Hash 可用）；V3：实测 Worked?=No 的组合为本书实验结论
- 备注：与 p09（正向矩阵）同源，保留反例视角（"哪些组合千万别选"）
- summary：陷阱：二层交换模式为 Switch Independent 时选 Hyper-V Port 或 Dynamic 负载均衡——实测均不通过，不管是否配 Stand-By 适配器。该模式下只有 Address Hash 可用。
- tags: [NIC-Teaming, 负载均衡, 兼容矩阵]

### ce09 · KVM 部署跳过 qcow2 Discard unmap 设置
- 出处：p50（quote 命中 L994-996 逐字；Macvtap 要求在 p49 L976-983）
- V1：命中；V2：Begin Installation 前的唯一时机窗口，漏做即丢掉缩盘效果；V3：unmap 缩盘与 3 网卡 Macvtap 为该 VA 的 KVM 专属要求
- 备注（推断标注 + 页码微瑕）："一旦开始安装就无法回头补设，只能重部署"为推断（原文仅强调"安装前做"）；summary 的"同页还要求 3 块网卡 Macvtap"实际在 p49（与 p50 相邻），引用时按 p49-50 理解
- summary：陷阱：KVM/Ubuntu 部署时直接点 Begin Installation，忘记对两块 VirtIO 磁盘把 Discard Mode 设为 unmap。
- tags: [KVM, qcow2, unmap, 返工]

### ce10 · Local Breakout 的 DNS 三类故障（AP 双 DNS、绕隧道、运营商不匹配）
- 出处：p83-84（quote 命中 p83 L1885-1887、p84 L1912-1913、L1921-1922 逐字；运营商样例 219.141.136.10 见 L1914-1921）
- V1：三段引用逐字命中；V2：三类 DNS 故障各配症状与解法（配正确的总部 DNS），Local Breakout 开启后的排障地图；V3：AP 随机选用双 DNS 导致 OVC 掉线等机制为产品行为
- summary：开启 Local Breakout 后的三类 DNS 故障：①AP 双 DNS——AP 本地拿到 DNS A、又经数据隧道从总部拿到 DNS B，随机选用，若 B 解析不了 OVC 的 FQDN，AP 会从 OVC 掉线；解决：配正确的总部 DNS。②客户端 DNS 绕隧道——Local Breakout 含 192.168.10.0/24 路由而客户端 DNS 是 192.168.10.177，DNS 请求也被送进总部隧道，变慢。③本地无该 DNS——本地找不到 192.168.10.177 则直接无法上网；或拿到的是异地运营商 DNS（如 219.141.136.10），解析和访问都慢。解决：为客户端配置正确的总部 DNS 服务器。
- tags: [Local-Breakout, DNS故障, 掉线]

### ce11 · AWOS 版本口径不一致：5.0.1 / 5.0.2 / 4.0.1 三处说法
- 出处：p6-7, p71（quote 三段分别命中 p6 L216-217、p7 L245-246、p71 L1461 逐字）
- V1：三段引用逐字命中（矛盾为原文真实存在，非提取错误）
- V2：交付时按最严口径 5.0.2+ 核对，防止照抄文档错误版本号
- V3：文档内部矛盾点，只有通读全书才能发现，独特性最强的反例之一
- summary：陷阱：文档内三处版本口径打架——RAP 功能要求 AWOS 5.0.2+（p6 与 p5 前置条件），Freemium 注册邮件的软件下载说明写最低 AWOS 5.0.1（p7），SSID 界面又写 Local Breakout "将在 AWOS 4.0.1 支持"（p71，疑为文档笔误）。交付时应以最严格的 5.0.2+ 为准。
- tags: [版本口径, AWOS, 文档矛盾]

### ce12 · CSV 批量导入时 RAP 字段未设 TRUE 导致 VPN 设置缺失
- 出处：p12（quote 命中 L364-365 逐字）
- V1：命中；V2：批量导入的隐性失败模式（导入成功但无隧道配置），防批量返工；V3：RAP=TRUE 才携带 VpnSettingName 为模板字段级规则
- 备注（推断标注）："只能逐台补配或重导"为推断，原文未明说补救方式
- summary：陷阱：批量导入模板里 RAP 列填了 FALSE/留空，却期望 VpnSettingName 生效。规则是：要携带 VPN Setting 信息，RAP 字段必须为 TRUE。
- tags: [CSV导入, RAP字段, 批量配置]

---

## 三、术语表（20 条，免验保留）

按流水线规则 glossary 免三重验证、全部保留。抽检 9 条（g01/g04/g10/g11/g12/g14/g15/g18/g20）quote 均在标注页命中原文，未见异常。

g01 RAP · g02 OVE · g03 OVC · g04 VPN VA · g05 Management VPN · g06 Data VPN · g07 WireGuard（wg/wg0/wg1） · g08 OpenVPN · g09 L2GRE 隧道 · g10 DHCP option 138 · g11 Device Catalog · g12 Freemium 账号 · g13 Device Registration/Activation Server · g14 Client VPN IP Address Pool · g15 Local Breakout · g16 NIC Teaming · g17 Promiscuous Mode 与 MAC 地址欺骗 · g18 DS-Lite 及 TCPMSS/MTU · g19 AWOS / Stellar AP · g20 三类 Profile（Tunnel / Access Role / Access Auth）

（完整条目以 candidates/glossary.md 为准，本文件不重复展开。）
