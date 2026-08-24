# glossary · OmniVista 2500 NMS 4.9R2 Installation and Upgrade Guide
# 来源: D:\Claude code\TSSKB\books\ov2500-install\source\fulltext.md（页码为 PDF 页码）

- id: g01
  title: OmniVista 2500 NMS（OV2500）
  type: glossary
  source_chapter: "p1"
  source_quote: |
    "Installation and Upgrade Guide for OmniVista 2500 NMS, Version 4.9R2"
  summary: |
    ALE（阿尔卡特朗讯企业）的网管平台（NMS，网络管理系统），本手册的主角，用于管理 AOS 交换机、第三方设备和 Stellar 无线 AP。当前手册针对 4.9R2 版本（2025 年 5 月，Part Number 060957-00 Rev. B）。通过 Web UI（https://<服务器IP>）访问，首次登录需激活许可。
  tags: [product, nms, ale]

- id: g02
  title: VA（Virtual Appliance，虚拟设备）
  type: glossary
  source_chapter: "p8"
  source_quote: |
    "OV 2500 NMS 4.9R2 is distributed as a Virtual Appliance only. There are no other standalone installers (e.g., Windows/Linux)."
  summary: |
    OV2500 唯一的交付形态：预封装的虚拟机镜像（ESXi 用 OVF+VMDK，Hyper-V 用导入包，KVM 用 qcow2 双盘），部署到 Hypervisor 后开机经向导完成配置。没有裸机安装器。文档中 VA 也常代指这台 OmniVista 虚拟机本身。
  tags: [va, virtual-appliance, deployment]

- id: g03
  title: Standalone Installation（独立安装）
  type: glossary
  source_chapter: "p11"
  source_quote: |
    "OV 2500 NMS 4.9R2 can be installed in a Standalone or High-Availability configuration."
  summary: |
    单机部署模式：一台 VA 承担全部网管功能。内存要求低于 HA（如 Medium 档 36GB vs 40GB），但升级期间完全不可管理（1-4 小时停机）。可后续转换为 HA 安装（需 HA License 且来源版本 ≥4.3R2）。
  tags: [standalone, installation]

- id: g04
  title: HA Installation（High-Availability，高可用安装）
  type: glossary
  source_chapter: "p11"
  source_quote: |
    "A High-Availability Installation consists of two VMs (Node 1 and Node 2), with one node acting as the Active OV Server (Node 1) and the other as a Standby OV Server (Node 2). If Node 1 fails, OmniVista will automatically failover to Node 2."
  summary: |
    双机热备模式：两台 VM 组成集群，一台 Active 一台 Standby，Active 故障时自动切换到 Standby。需要 HA License，最多管 4000 台设备，必须 Medium 及以上规格。分 Layer 2 与 Layer 3 两种配置。升级采用滚动方式，仅在 failover 阶段中断 5-10 分钟。
  tags: [ha, high-availability, cluster]

- id: g05
  title: Cluster（集群）
  type: glossary
  source_chapter: "p40"
  source_quote: |
    "Once you have installed both VMs, you can convert them to a High-Availability Cluster Configuration."
  summary: |
    OV2500 HA 的实现形态：恰好两节点组成的集群，通过 VA 菜单 12（Convert to Cluster，Node 1 发起）和 13（Join Cluster，Node 2 加入）建立，集群有名称（字母数字）。集群级配置（Cluster IP、虚拟 IP、维护模式、Manual Failover 等）只能在 Active 节点的 Configure Cluster 菜单操作，且对两节点同时生效。
  tags: [cluster, ha]

- id: g06
  title: Node 1 / Node 2（节点 1 / 节点 2）
  type: glossary
  source_chapter: "p11"
  source_quote: |
    "two VMs (Node 1 and Node 2), with one node acting as the Active OV Server (Node 1) and the other as a Standby OV Server (Node 2). They are referred to as "Peer Nodes" in the installation process."
  summary: |
    HA 的两台 VM。Node 1 通常是原独立安装机（转集群时先 Convert to Cluster），Node 2 后加入（Join Cluster，需输入 Node 1 物理 IP 和 cliadmin 密码）。注意 L3 集群的 Active 角色由系统随机分配，不一定是 Node 1（p59）。手册示例主机名常为 ov1/ov2（≤15 字符、小写）。
  tags: [node, ha]

- id: g07
  title: Active Node / Standby Node（主用/备用节点）
  type: glossary
  source_chapter: "p11"
  source_quote: |
    "one node acting as the Active OV Server... the other as a Standby OV Server... If Node 1 fails, OmniVista will automatically failover to Node 2."
  summary: |
    Active 节点对外提供全部网管服务（所有服务 Running）；Standby 节点实时同步数据但 upam/nginx 服务停止（预期行为，p52）。HA 升级从升级 Standby 开始，完成后角色互换属正常。可通过 Manual Failover 手动切换，或用 Preferred Active Node 设定故障恢复后的主用节点（默认不设，p302）。
  tags: [active, standby, role]

- id: g08
  title: Failover（故障切换/手动切换）
  type: glossary
  source_chapter: "p40"
  source_quote: |
    "In the event of a failover, the Standby Node becomes the Active Node and network devices, again, communicate to it through the Cluster IP address."
  summary: |
    Active→Standby 的角色接管。故障时自动发生；HA 升级流程中在 Standby 节点升级重启后按回车触发；也可通过 Configure Cluster - 15 Manual Failover 手动发起。切换期间 UI 监控和 UPAM 认证中断约 5-10 分钟，切换后 UI 顶部会出现"Communication Failure"横幅（L3 下横幅含新 Active 链接，p302）。
  tags: [failover, ha, switchover]

- id: g09
  title: Cluster IP（集群虚拟 IP）
  type: glossary
  source_chapter: "p40"
  source_quote: |
    "you configure a virtual Cluster IP address. Both the Active and Standby Nodes are reached through the Cluster IP address. Network devices communicate with the Active Node through the Cluster IP address."
  summary: |
    Layer 2 HA 专属的对外虚拟 IP：设备和管理员始终访问 Cluster IP，实际由当前 Active 节点应答，failover 后自动漂移。最佳实践是把原独立安装的 OV IP 腾出来当 Cluster IP，设备无需改地址。可配的伴生虚拟 IP 还有 Captive Portal Virtual IP 和 Additional OV Web Virtual IP（均须与对应静态 IP 同子网）。禁用 Cluster IP 会连带禁用这两个虚拟 IP（p298）。
  tags: [cluster-ip, virtual-ip, layer2]

- id: g10
  title: Layer 2 / Layer 3 HA Configuration（二/三层 HA 配置）
  type: glossary
  source_chapter: "p40"
  source_quote: |
    "Layer 2 Configuration - both OmniVista Server VMs must be on the same subnet... Layer 3 Configuration - the OmniVista Server VMs are on different subnets, with a unique IP address for each server."
  summary: |
    两种 HA 拓扑：L2 要求两节点同子网，靠 Cluster IP 对外，设备零改动；L3 允许两节点跨子网、各有独立 IP，设备需能与两节点同时通信，须配 Preferred Node，且 sFlow/Policy 等依赖设备回连的功能受限、Captive Portal 被禁用、AP 需为 AP13XX+AWOS5.0+。L2 不能转 L3，L3 只能新建。
  tags: [layer2, layer3, topology]

- id: g11
  title: Maintenance Mode（维护模式）
  type: glossary
  source_chapter: "p64"
  source_quote: |
    "you must first enable Maintenance Mode on the Active Node (ov1). This will enable Maintenance Mode on both nodes in the Cluster."
  summary: |
    HA 升级和扩盘前的集群级状态（Configure Cluster 菜单 18），在 Active 节点一次启用/禁用即双节点生效。启用后进入维护窗口：独立安装的停机时间从启用维护模式起算。注意：Standby 升级完成后出现"请禁用维护模式"的提醒时不要立即禁用，要等两节点都升级完（p188）。
  tags: [maintenance-mode, ha, upgrade]

- id: g12
  title: Data Sync / "Up to Date"（数据同步状态）
  type: glossary
  source_chapter: "p67"
  source_quote: |
    "The data sync status indicates whether the data between two nodes is in sync. If it is, the field will indicate "Up to Date". If it is in the process of syncing, a percentage will be displayed... The speed of a data sync depends on the amount of data and the network speed between the two Nodes."
  summary: |
    Show OV Cluster Status 命令显示的两节点数据同步状态：显示"Up to Date"表示已同步，显示百分比表示同步中。任何升级、扩盘、节点配置操作前都必须确认 Up to Date；同步速度取决于数据量和节点间网速（推荐 1Gbps/1ms）。
  tags: [data-sync, cluster-status]

- id: g13
  title: VA Menu / HA Virtual Appliance Menu（虚拟设备菜单）
  type: glossary
  source_chapter: "p272"
  source_quote: |
    "To access the Virtual Appliance Menu for a VM, launch the Hypervisor Console... You can also access the Virtual Appliance Menu by connecting via SSH using port 2222, user cliadmin."
  summary: |
    OV2500 的运维控制台菜单，装好后 cliadmin 登录即见。独立版 Virtual Appliance Menu（选项含 Configure the Virtual Appliance、Run Watchdog、Upgrade/Backup/Restore、Convert/Join Cluster 等，附录A）；转 HA 后变为 HA Virtual Appliance Menu（新增 Show OV Cluster Status、Configure Cluster、Configure Current Node，附录B）。可从 Hypervisor 控制台或 SSH 端口 2222 访问。升级必须走控制台而非 SSH。
  tags: [va-menu, console, cli]

- id: g14
  title: Watchdog（服务看护命令集）
  type: glossary
  source_chapter: "p286"
  source_quote: |
    "The Watchdog command set is used to start and stop managed services used by OmniVista. If you stop certain framework services (e.g., ActiveMQ, Apache Tomcat)... the web server will shut down, and you will have to restart the service manually."
  summary: |
    VA 菜单选项 3/5，管理 OmniVista 全部后台服务：查看所有服务状态（升级/健康检查必用）、启停全部或单个服务（可带依赖树）、启停 Watchdog 本体、以及 Choose Service Profile（按需裁剪 Stellar/UPAM/应用可视化/IoT/sFlow 服务省内存）。停 ActiveMQ/Tomcat 等框架服务会连带关停 Web 服务器，需手动恢复。
  tags: [watchdog, services, operations]

- id: g15
  title: cliadmin
  type: glossary
  source_chapter: "p272"
  source_quote: |
    "1. Enter the login (cliadmin) and press Enter. 2. Enter the password and press Enter. The password is the one you created when you first launched the VM Console at the beginning of the installation process."
  summary: |
    VA 的管理账号：安装向导第 3 步设置其密码（丢失无法找回，须妥善保存）。用于登录 VA 菜单（控制台或 SSH 2222 端口）、SFTP（端口 22）取备份/日志/上传证书、Node 2 加入集群时的"Cluster Password"。相关联的还有 root、admin（UI 登录）、ftp、mongodb 等独立密码，均可从菜单修改。
  tags: [cliadmin, account, credentials]

- id: g16
  title: Network Size（网络规模档位）
  type: glossary
  source_chapter: "p37"
  source_quote: |
    "Ranges include: Low (fewer than 500 devices); Medium (500 to 2,000 devices); High (2,000 to 5,000 devices); Very High (5,000 to 10,000 devices)."
  summary: |
    安装时选择的管理规模档位，决定内存分配和可管理设备数：Low<500、Medium 500-2000、High 2000-5000、Very High 5000-10000。OmniVista 按所选档位分配内存，且禁止选择超出 VA 实际配置（内存/磁盘）的档位。后续可在 Configure Network Size 里改档或重应用（>256 台 Stellar AP 升级后必须重应用一次）。
  tags: [network-size, capacity]

- id: g17
  title: Extend Data Partition（扩展数据分区）
  type: glossary
  source_chapter: "p280"
  source_quote: |
    "By default, OmniVista is partitioned as follows: HDD1:50GB and HDD2:512GB. If you are managing more than 500 devices, it is recommended that you increase the provisioned hard disk."
  summary: |
    扩容数据盘的标准操作。独立安装路径：Configure the Virtual Appliance - 9 Configure Network Size - 4 Extend Data Partition；HA 路径：Configure Current Node - 17 Extend Partitions（选 OmniVista Data Partition，两节点都要做）。完整流程为停服务→备份/快照→VA 菜单关机→Hypervisor 加新盘→开机→菜单扩容。只支持加新盘，不支持改现有盘；KVM 有 SATA/前两盘不识别的特殊规则。
  tags: [extend, partition, storage]

- id: g18
  title: ALE Central Repo / Custom Repository（软件仓库）
  type: glossary
  source_chapter: "p288"
  source_quote: |
    "By default, the OV Virtual Appliance points to the external ALE Central Repository, which contains the latest OV software. However, you can configure up to three (3) custom repositories... Only one (1) repository can be enabled at a time."
  summary: |
    升级软件源。默认指向 ALE Central Repo（ovrepo.fluentnetworking.com）；可另配最多 3 个自定义仓库，同一时刻只能启用 1 个。典型用例：4.7R1 Patch 2 补丁仓库 PatchRepo（https://ovrepo.fluentnetworking.com/ov/patch）。多数升级流程强制要求把仓库切回"ALE Central Repo"这个默认名。仓库 URL 填写时不带 https:// 前缀。
  tags: [repository, upgrade, software-source]

- id: g19
  title: Captive Portal / UPAM（门户/准入认证）
  type: glossary
  source_chapter: "p34"
  source_quote: |
    "OmniVista supports configuration of three (3) IPs: the OmniVista IP, the Captive Portal IP and an additional OmniVista Web Management IP."
  summary: |
    Captive Portal 是无线访客/用户认证门户，由 UPAM（统一策略与准入管理，负责 BYOD/认证，如 802.1X、Portal 认证）承载，因此有独立 IP 与端口（默认 HTTP 8080 / HTTPS 8443，默认 FQDN ov2500-upam-cportal.al-enterprise.com）。三种部署方式推荐"独立子网+独立网卡"。HA 下仅 L2 支持虚拟门户 IP；L3 集群中 Captive Portal 被禁用。Standby 节点 upam 服务停止为预期；升级停机期间依赖 UPAM 认证的新客户端无法入网。
  tags: [captive-portal, upam, authentication]

- id: g20
  title: Stellar AP / AWOS
  type: glossary
  source_chapter: "p8"
  source_quote: |
    "If your network includes Stellar APs, they must be running one of the certified AWOS Releases specified in the OmniVista 2500 NMS Release Notes. If necessary, upgrade these devices after the OmniVista upgrade."
  summary: |
    Stellar 是 ALE 的无线 AP 产品线，AWOS 是其操作系统。版本强绑定：AP 必须跑 Release Notes 认证的 AWOS 版本，一般在 OmniVista 升级完成后再通过 Resource Manager - Upgrade Image 界面刷 AP 固件。规模常数：各档网络下 Stellar AP 上限 500/2000/4000/4000 台；>256 台时 OV 升级后须重应用内存设置；L3 冗余仅 AP13XX+（AWOS 5.0+）支持。
  tags: [stellar-ap, awos, wireless, firmware]

- id: g21
  title: AOS
  type: glossary
  source_chapter: "p9"
  source_quote: |
    "Total Number of Managed Devices (AOS, Third-Party, and Stellar APs)"
  summary: |
    ALE Operating System，ALE 有线交换机/路由设备的操作系统，本手册中 AOS 设备即有线交换机，与第三方设备、Stellar AP 并列为三类被管设备。规模换算示例：High 档 4000 台 Stellar AP 时最多再支持 500 台 AOS 交换机。L3 HA 下依赖设备回连 OV 的功能（sFlow、Policy、IoT 对 AOS）受限。
  tags: [aos, switch, wired]

- id: g22
  title: NTP Client（NTP 时间同步客户端）
  type: glossary
  source_chapter: "p283"
  source_quote: |
    "Configure NTP Client: 1. Enter 13 and press Enter to configure an NTP Server... Enter the IP address of the NTP Server and press Enter... You can enable the server when you create it, or enable it at a later time using option 5."
  summary: |
    VA 菜单的 NTP 服务器配置项（附录A 菜单 14，HA 节点在附录B Configure Current Node - 8）：输入 NTP 服务器 IP 即可创建，创建时可即时启用或稍后启用。HA 双节点与被管网络保持时间一致是日志、证书、集群同步的基础；高级模式还提供 ntpdate/ntpq/ntpstat 只读排查命令（p292）。
  tags: [ntp, time-sync]

- id: g23
  title: Technical Support Code（技术支持密码）
  type: glossary
  source_chapter: "p34"
  source_quote: |
    "Press Enter, then enter and confirm a Technical Support Code Password. This is a password that will be used by Technical Support to access the VM, if necessary."
  summary: |
    安装向导第 2 步设置的专用密码，供 ALE 技术支持在必要时访问 VM。安装结束时还会被提示输入。后续可在 Change Password 菜单（附录A 选项 5 - 4）修改。与 cliadmin/admin 等密码一样：丢失无法找回，必须安全保存。
  tags: [support, password, security]

- id: g24
  title: VM Snapshot（虚拟机快照）
  type: glossary
  source_chapter: "p8"
  source_quote: |
    "Take a VM Snapshot of the current OmniVista VA. Note that VM snapshots can cause performance issues on the running VM."
  summary: |
    升级和 HA 转换前的官方回退手段，但有代价：快照会拖累运行中 VM 的性能。标准用法是"一次性保险"：操作前删旧快照、拍新快照，操作成功验证后立即删除。不能当长期备份用，长期备份应遵循虚拟化平台自身的备份方案。
  tags: [snapshot, rollback, upgrade]

- id: g25
  title: Evaluation License（评估许可）
  type: glossary
  source_chapter: "p323"
  source_quote: |
    "An Evaluation License provides full OV 2500 NMS feature functionality but is valid only for 90 Days (starting from the date the license is generated)."
  summary: |
    90 天全功能试用许可（自生成日起算），单文件覆盖所有设备许可与服务许可。通过 ALE 许可门户生成（Customer ID 99999 / Order Number evaluation / Passcode omnivista，邮箱 4 位码验证），下载 .dat 文件后在 License - Add/Import License 界面导入。首次登录 OmniVista 会强制要求激活许可（正式或评估）。
  tags: [license, evaluation, trial]

- id: g26
  title: ovactivemq（ActiveMQ 消息服务）
  type: glossary
  source_chapter: "p92"
  source_quote: |
    "Upgrading the ov1 Node requires stopping the OmniVista ActiveMQ (ovactivemq) service before beginning the upgrade process. You must stop this service immediately after the ov2 Node upgrade is completed... This helps to avoid the possibility of APs rebooting and attempting to connect to the ov1 Node."
  summary: |
    OmniVista 的 ActiveMQ 消息中间件服务。AP 通过它发现并与当前 Active 节点保持会话。L3 HA 升级中，新 Active（ov2）就位后必须立即在旧节点 ov1 上停掉 ovactivemq（Stop a Service，不带 stop-tree），否则 AP 看到该服务仍会尝试连 ov1 而导致 AP 重启；停完等 10-15 分钟确认所有 AP/客户端在新节点 UP 后再升级 ov1。
  tags: [activemq, service, layer3-upgrade]

- id: g27
  title: upam / nginx（Standby 节点停用的服务）
  type: glossary
  source_chapter: "p52"
  source_quote: |
    "on Node 2, all services should be running except upam and nginx. It is the expected behavior on the Standby Node that these services will be "Stopped"."
  summary: |
    健康检查的关键判据服务：upam（准入认证服务）和 nginx（Web 前端/反向代理）只在 Active 节点运行，Standby 节点上显示 Stopped 是预期而非故障；使用自定义 RADIUS 证书时 ovradius 在备节点也可能停止。手动 failover 后原 Active 节点的这三个服务同样转为停止（p302）。
  tags: [upam, nginx, services, standby]

- id: g28
  title: Preferred Active Node（首选主用节点）
  type: glossary
  source_chapter: "p302"
  source_quote: |
    "The Preferred Active Node is the Node that will be set following a system failure. When the system returns, the Preferred Active Node will be the Active Node when the system returns... By default, no Preferred Active Node is set."
  summary: |
    集群偏好设置（Configure Cluster - 14）：指定系统故障恢复后应由哪个节点出任 Active；默认不设置，由系统自行决定。L3 HA 安装必须配置此项（通过 cliadmin 菜单，p42）。清除设置则回到"系统自动决定"行为。
  tags: [preferred-node, ha, failover]
