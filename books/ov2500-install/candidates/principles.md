# principles · OmniVista 2500 NMS 4.9R2 Installation and Upgrade Guide
# 来源: D:\Claude code\TSSKB\books\ov2500-install\source\fulltext.md（页码为 PDF 页码，与 <<<PAGE N>>> 标记一致）

- id: p01
  title: 四档网络规模的最低系统配置常数表
  type: principle
  source_chapter: "p9"
  source_quote: |
    "Total Number of Managed Devices 500 / 2,000 / 5,000 / 10,000 ... Hypervisor Processor 2.4 GHz, 8 Logical Processors (12 for High/Very High) ... Minimum Reserved OmniVista VA RAM for Standalone 20GB / 36GB / 64GB / 64GB ... Minimum Reserved RAM for HA N/A / 40GB / 64GB / 64GB ... Minimum Storage Read/Write Speed 100 / 150 / 200 / 200 MB/s"
  summary: |
    容量规划核心常数。Low/Medium/High/Very High 四档：管理设备总数 500/2000/5000/10000（其中 Stellar AP 上限分别为 500/2000/4000/4000，AP 客户端关联 5 万/20 万/20 万/20 万，UPAM 认证客户端 2 万/5 万/7.5 万/10 万）。CPU 需 2.4GHz，Low/Medium 8 个逻辑处理器，High/Very High 12 个。内存（独立安装）20/36/64/64GB，HA 安装 40/64/64GB（Low 档不支持 HA）。磁盘分区 1 固定 50GB，分区 2 分别 512GB/1TB/2TB/2TB。存储读写速度至少 100/150/200/200 MB/s。
  tags: [capacity, sizing, cpu, memory, storage]

- id: p02
  title: HA 特性规模上限 4000 设备且必须 Medium 及以上规格
  type: principle
  source_chapter: "p11"
  source_quote: |
    "The High-Availability Feature supports up to 4,000 devices."
  summary: |
    HA（高可用）特性最多支持 4000 台设备；HA 安装必须建立在 Medium 或更高规格的 VA 上（Low 档不提供 HA 内存配置）。脚注补充：High 档 4000 台 Stellar AP 时最多支持 500 台 AOS 交换机；Very High 档 4000 台 AP 时 AOS 交换机可达 1000 台（HA Very High 可达 1500 台）。
  tags: [ha, capacity, limit]

- id: p03
  title: 仅以虚拟设备（VA）形式发行，支持三平台
  type: principle
  source_chapter: "p8"
  source_quote: |
    "OV 2500 NMS 4.9R2 is distributed as a Virtual Appliance only. There are no other standalone installers (e.g., Windows/Linux)... VMware ESXi: 6.5, 6.7 and 7.0.2, 8.0; MS Hyper-V: 2012 R2, 2016, 2019, and 2022; MS Hyper-V on Windows 10 Professional; Linux KVM/Ubuntu 22.04."
  summary: |
    4.9R2 只提供虚拟设备（VA）发行包，没有 Windows/Linux 独立安装器。支持的虚拟化平台：VMware ESXi 6.5/6.7/7.0.2/8.0；Microsoft Hyper-V 2012 R2/2016/2019/2022；Windows 10 专业版上的 Hyper-V；Linux KVM（Ubuntu 22.04）。
  tags: [distribution, hypervisor, esxi, hyperv, kvm]

- id: p04
  title: 内存与 CPU 分配规则：不超配、预留内存、CPU Shares 设 High
  type: principle
  source_chapter: "p10"
  source_quote: |
    "When provisioning RAM for a new VM for OmniVista, never allocate more memory than is available on the Host Server... it is recommended that you reserve that RAM for the OmniVista VM to prevent performance issues. Set CPU Shares to "High". Do not exceed the number of Logical Processors recommended for your network size."
  summary: |
    给 OmniVista VM 分配内存不得超过宿主机实际可用内存（例如 128GB 宿主机已分出 96GB 时再跑 OV 会出事故）；按网络规模表分配并建议在 Hypervisor 里"预留"该内存防止性能问题；CPU Shares 设为 High；逻辑处理器数量不要超过对应网络规模档位的推荐值（8 或 12）。
  tags: [memory, cpu, reservation, performance]

- id: p05
  title: 网络规模档位受 VA 实际配置硬约束
  type: principle
  source_chapter: "p8"
  source_quote: |
    "OmniVista will not allow you to configure a network size that cannot be supported by the VA configuration. For example, if you allocate 20GB of memory for the OmniVista VA, OmniVista will only allow you to configure a Low network size (fewer than 500 devices)."
  summary: |
    安装时选择的网络规模档位（Low/Medium/High/Very High）必须与 VA 实际配置匹配：内存或磁盘不足会导致 OV 不稳定，系统会直接拒绝配置超出 VA 配置的规模。例如只给 VA 分配 20GB 内存，则只能选 Low 档（500 台以下）。
  tags: [network-size, constraint, memory]

- id: p06
  title: SNMPv3 AES 性能依赖 Intel AES-NI 指令集
  type: principle
  source_chapter: "p10"
  source_quote: |
    "A recommended algorithm is AES ("Advanced Encryption Standard"). To get the best performance from your hypervisor, we recommend that you use Intel processors with the AES-NI instruction set enabled... AES-NI must be enabled in your hypervisor's BIOS... The AES-NI feature must not be "masked" by your hypervisor."
  summary: |
    OmniVista 与设备通信可用 SNMPv3，推荐 AES 算法。要获得最佳性能，建议用 2010 年后的 Intel CPU（Westmere 及以后）并在 Hypervisor 的 BIOS 中开启 AES-NI，且该特性未被 Hypervisor 屏蔽；VMware 和 Hyper-V 默认直通（pass-through）AES 加速。
  tags: [snmpv3, aes-ni, cpu, security]

- id: p07
  title: 默认磁盘布局与扩盘规则：只能加新盘，不能改现有盘
  type: principle
  source_chapter: "p10"
  source_quote: |
    "By default, OV 2500 NMS 4.8R2 is partitioned as follows: HDD1:50GB and HDD2:512GB. If you are managing more than 500 devices, it is recommended that you go to the Virtual Appliance Menu on the VA to increase the OmniVista disk space... editing the size of existing virtual disks is not supported."
  summary: |
    默认分区为 HDD1 50GB + HDD2 512GB；管理超过 500 台设备时建议通过 VA 菜单扩盘（独立安装走 Configure Network Size - Extend Data Partition，HA 安装走 Configure Current Node - Extend Partitions）。扩容只能从 Hypervisor 添加新虚拟磁盘，不支持编辑既有虚拟盘的容量。
  tags: [disk, partition, extend, storage]

- id: p08
  title: 首次部署 VA 时不要提前添加新磁盘
  type: principle
  source_chapter: "p10"
  source_quote: |
    "When deploying the OmniVista VA for the first time, do not add the new disks in the hypervisor until after OmniVista is configured and rebooted."
  summary: |
    首次部署 OmniVista VA 时，扩展用的新磁盘必须等 OmniVista 完成初始配置并重启之后再从 Hypervisor 添加，否则可能影响初始安装流程。
  tags: [deployment, disk, first-install]

- id: p09
  title: 升级矩阵：必须逐版本顺序升级到 4.9R2
  type: principle
  source_chapter: "p6-7"
  source_quote: |
    "If you are using release 4.7R1: 1. Upgrade to the 4.7R1 Patch 2 release. 2. Upgrade to 4.8R1. 3. Upgrade to 4.8R2. 4. Upgrade to 4.9R1... 5. Upgrade to 4.9R2."
  summary: |
    到 4.9R2 只能按升级矩阵逐级自动升级（从 VA 菜单执行），每级 Standalone/HA 均需完成：4.5R1→4.5R2→4.5R3→4.6R1→4.6R2→4.7R1→4.7R1 Patch 2→4.8R1→4.8R2→4.9R1→4.9R2。起点越新步数越少。4.7R1 Patch 2 需通过 Custom Repository（PatchRepo）获取。
  tags: [upgrade, upgrade-matrix, version]

- id: p10
  title: 每一步升级完成后必须验证服务与 Web GUI 再继续
  type: principle
  source_chapter: "p8"
  source_quote: |
    "As you complete each upgrade in the upgrade path, make sure all services are running and you can access the OmniVista Web GUI before proceeding to the next upgrade."
  summary: |
    长链路升级中，每完成一个版本升级都要确认：所有服务已运行（Watchdog 命令显示状态）、Build 号正确、能登录 OmniVista Web GUI，然后才能进入下一级升级。升级完成后还应拍新快照并删除旧快照。
  tags: [upgrade, verification, workflow]

- id: p11
  title: 旧于 4.5R1 的版本建议备份后全新安装
  type: principle
  source_chapter: "p8"
  source_quote: |
    "If your OmniVista is currently running a release older than 4.5R1, the sequential upgrade to the latest OmniVista release will take a very long time. Therefore, it is recommended that you take a backup of your existing OmniVista installation and start with a fresh installation of the latest OmniVista release."
  summary: |
    版本低于 4.5R1 时逐级升级耗时过长，官方建议：备份旧系统后直接全新安装最新版，再重新添加/发现设备并重做配置（Profile、Template、SSID 等），这样更快；代价是丢失历史统计数据（trap、统计等），如需保留可从旧系统导出。
  tags: [upgrade, migration, fresh-install]

- id: p12
  title: 升级必须在 VM Console 执行，升级窗口 1-4 小时
  type: principle
  source_chapter: "p60"
  source_quote: |
    "You must perform the OmniVista upgrade directly from the VM Console. If you access OmniVista remotely using an SSH client, upgrading the installation can result in incomplete upgrades... The upgrade can take anywhere from 1 to 4 hours depending on network speed, network size, and database size."
  summary: |
    升级操作必须在虚拟机控制台（Hypervisor Console）直接执行；远程 SSH 升级可能造成升级不完整、漏掉"按回车继续"等交互。若必须用 SSH 客户端（如 putty），需配置周期性 keepalive 保活。单节点升级通常 1-2 小时，视网速/规模/数据量最长 3-4 小时。
  tags: [upgrade, console, ssh, duration]

- id: p13
  title: 升级停机窗口：Standalone 全程不可管理，HA 仅切换时 5-10 分钟
  type: principle
  source_chapter: "p60"
  source_quote: |
    "During the upgrade time for an OmniVista Standalone installation, OmniVista is not available for any management functions... new clients cannot join the network if the Switch/AP is configured to do authentication from UPAM. The upgrade downtime may last between one and four hours... For an OmniVista High-Availability installation, OmniVista management functions remain available until the failover stage... not available for approximately 5 to 10 minutes."
  summary: |
    独立安装升级期间 OmniVista 完全不可管理（1-4 小时，从启用维护模式起算），但已部署网络不受影响，已上线设备和客户端继续工作；唯一例外是交换机/AP 从 UPAM 做认证时新客户端无法入网。HA 安装升级期间管理功能持续可用，仅在 failover 阶段中断约 5-10 分钟。
  tags: [upgrade, downtime, maintenance-window, ha]

- id: p14
  title: HA 升级标准工作流：先维护模式、先升 Standby、角色互换正常
  type: principle
  source_chapter: "p67"
  source_quote: |
    "1. Enable Maintenance Mode on the Active Node (ov1) 2. Connect to the Standby Node and upgrade the node to 4.9R2 3. When the Standby Node upgrade is complete, do a reboot and failover... 4. Connect to the previous Active Node (ov1) and upgrade the node to 4.9R2... After this upgrade process is complete, the Active Node at the beginning of the process is no longer the Active Node. This is a perfectly normal state."
  summary: |
    HA 升级固定流程（4.8R1 及以后版本）：验证集群数据同步 Up to Date → 在 Active 节点启用维护模式 → 先升级 Standby 节点 → Standby 重启并 failover 成为新 Active → 等其所有服务起来后升级原 Active 节点 → 验证。升级结束后原 Active 变为 Standby 属正常状态，如需还原可手动 failover（切换期间服务中断 5-10 分钟）。
  tags: [ha, upgrade, workflow, failover]

- id: p15
  title: 维护模式在 Active 节点一次启用即对两节点生效
  type: principle
  source_chapter: "p64"
  source_quote: |
    "Before performing the upgrade, you must first enable Maintenance Mode on the Active Node (ov1)... This will enable Maintenance Mode on both nodes in the Cluster."
  summary: |
    维护模式（Configure Cluster - Enable Maintenance Mode）只需在 Active 节点执行一次，即对集群两个节点同时生效；禁用同理，无需在 Standby 节点重复操作。这是 HA 升级和扩盘操作的前置条件。
  tags: [ha, maintenance-mode, cluster]

- id: p16
  title: L2 与 L3 两种 HA 拓扑的选型规则
  type: principle
  source_chapter: "p40"
  source_quote: |
    "Layer 2 Configuration - In a Layer 2 HA Configuration, both OmniVista Server VMs must be on the same subnet. In this configuration, you configure a virtual Cluster IP address... Layer 3 Configuration - In a Layer 3 HA Configuration the OmniVista Server VMs are on different subnets, with a unique IP address for each server."
  summary: |
    L2 HA：两台 VM 同子网，配一个虚拟 Cluster IP，内外都通过 Cluster IP 访问当前 Active；把现有独立安装的 IP 转成 Cluster IP 可避免全网设备重配地址。L3 HA：两台 VM 不同子网、各有独立 IP，设备需能同时与两个节点通信，failover 后设备自动改与新 Active 通信，但需要重新配置网络设备。新建集群时 L3 会随机指派 Active 节点（p59），需用 Show OV Cluster Status 确认。
  tags: [ha, layer2, layer3, cluster-ip]

- id: p17
  title: HA 转换的前置条件与 L2 转 L3 禁止
  type: principle
  source_chapter: "p40"
  source_quote: |
    "An HA license is required for a 4.9R2 HA Installation... You can convert a 4.9R2 Standalone Installation to a 4.9R2 HA Installation if the 4.9R2 Standalone installation was upgraded from a 4.3R2 or newer Standalone Installation. You cannot convert... if... upgraded from a 4.3R1 Standalone Installation. Converting an L2 HA installation to an L3 HA installation is not supported. Only a fresh L3 HA installation is supported."
  summary: |
    独立转 HA 的规则：必须先导入 HA License；全新 4.9R2 独立安装可转 HA；从 4.3R2 及更新版本升级而来的 4.9R2 独立安装也可转；从 4.3R1 升级来的不能转。L2 HA 不能转 L3 HA，L3 只能全新搭建（例外：可给全新 4.9R1 独立安装加第二个节点组成 L3，或 4.8R2 升到 4.9R1 后再转 L3）。
  tags: [ha, conversion, license, layer3]

- id: p18
  title: L3 HA 的功能限制与 AP 型号门槛
  type: principle
  source_chapter: "p42"
  source_quote: |
    "Features or functions that require devices to contact OmniVista are not supported in a Layer 3 Configuration (e.g., sFlow, Policy)... Configuring L3 Redundancy Settings is supported only on AP13XX and higher models running AWOS 5.0 or higher; it is not supported on AP11XX or AP12XX models. Configuring a Preferred Node through the cliadmin menu is required for an L3 HA installation."
  summary: |
    L3 HA 下凡需要设备主动回连 OmniVista 的功能都受限：sFlow（Top N Apps/Ports）和 Policy 对 AOS 不支持；IoT 对 AOS 需 failover 后重应用；Syslog 需外部服务器或配置双节点 IP；DNS/Provisioning 需 failover 后重配 DNS。L3 冗余设置仅 AP13XX 及以上型号、AWOS 5.0+ 支持（AP11XX/12XX 不支持），且 L3 必须通过 cliadmin 菜单配置 Preferred Node。Captive Portal 在 L3 下被禁用（p50）。
  tags: [ha, layer3, limitations, stellar-ap]

- id: p19
  title: HA 网络基础要求：1Gbps 带宽、1ms 延迟、最新网卡驱动
  type: principle
  source_chapter: "p42"
  source_quote: |
    "The Hypervisor's on which you are installing OmniVista must have the latest Network Adaptor drivers: Hyper-V: Broadcom b57nd60a.sys version 16.8 and later... VMware: Broadcom Tg3-3.133d.v55.1-101300361 and later. The recommended network bandwidth is 1Gbps. The recommended network latency is 1ms."
  summary: |
    HA 两节点间同步对网络质量敏感：推荐带宽 1Gbps、延迟 1ms；宿主机网卡驱动必须用最新版（Hyper-V 的 Broadcom b57nd60a.sys 16.8+，VMware 的 Broadcom Tg3-3.133d.v55.1-101300361+）。数据同步速度直接取决于数据量和两节点间网速。
  tags: [ha, network, bandwidth, latency, driver]

- id: p20
  title: 节点 Hostname 规则：最长 15 字符且全小写
  type: principle
  source_chapter: "p47"
  source_quote: |
    "Enter a Hostname for Node 1 and press Enter. The Hostname can be up to 15 characters but must be lower case ("ov1" not "OV1")."
  summary: |
    HA 转换时 Node 1/Node 2 的主机名最多 15 个字符，且必须全小写（"ov1" 而非 "OV1"）；集群名（Cluster Name）为字母数字组合。独立安装的默认主机名是 omnivista，可改，同样限 15 字符。
  tags: [ha, hostname, naming]

- id: p21
  title: 集群地址规划清单（转换前备齐）
  type: principle
  source_chapter: "p43"
  source_quote: |
    "To configure the Cluster, you will need IP addresses for the following: Node 1 - the physical IP address of the Active Node... Node 2... OV Virtual IP Address (Layer 2 Installation Only)... Captive Portal Virtual IP Address (Layer 2 Configuration Only)... Additional OV Web Virtual IP... must be on the same subnet as the Static Captive Portal IP address."
  summary: |
    转 HA 前需提前规划好：Node 1、Node 2 各自物理 IP；L2 专用的 OV 虚拟 IP（Cluster IP）；可选的 Captive Portal 虚拟 IP 与附加 OV Web 虚拟 IP（均仅 L2 可用，且必须与对应静态 IP 同子网）。转换 Node 1 时会先给节点分配新物理 IP，把原独立安装 IP 腾出来用作 Cluster IP，设备无需改地址。
  tags: [ha, ip-planning, cluster-ip]

- id: p22
  title: 外部仓库与云服务的 443 端口白名单及代理要求
  type: principle
  source_chapter: "p40"
  source_quote: |
    "a Proxy should be configured to enable OV 2500 NMS 4.9R2 to connect to these external sites (Port 443): ALE Central Repository - ovrepo.fluentnetworking.com; AV Repository - ep1.fluentnetworking.com; Fleet Supervision FQDN - myfleet.ovcirrus.com; Call Home Backend - us.fluentnetworking.com; Device Fingerprinting Service - api.fingerbank.org; Web Content Filtering - api.bcti.brightcloud.com."
  summary: |
    OmniVista 需通过 HTTPS（443 端口）访问 6 个外部站点：ALE 中央仓库 ovrepo.fluentnetworking.com、AV 签名库 ep1.fluentnetworking.com、Fleet Supervision（myfleet.ovcirrus.com）、Call Home 后端（us.fluentnetworking.com）、设备指纹服务（api.fingerbank.org）、网页内容过滤（api.bcti.brightcloud.com）。服务器不直连互联网时必须配代理（VA 菜单 Configure Proxy），否则升级和云特性不可用。离线升级需联系客服。
  tags: [network, proxy, firewall, repository, ports]

- id: p23
  title: Web 与管理端口默认值及合法范围
  type: principle
  source_chapter: "p275"
  source_quote: |
    "HTTP Port (Valid range: 1024 to 65535, Default = 80); HTTPS Port (Valid range: 1024 to 65535, Default = 443)... Captive Portal: HTTP Port (Valid range: 1024 to 65535, Default = 8080); HTTPS Port (Valid range: 1024 to 65535, Default = 8443)"
  summary: |
    端口常数：OV Web 默认 HTTP 80、HTTPS 443；Captive Portal 默认 HTTP 8080、HTTPS 8443；合法范围均为 1024-65535 且新端口不得与已配端口重复。其他管理通道：VA 菜单 SSH 用端口 2222（cliadmin 用户，p272），SFTP 文件传输用端口 22（上传 SSL 证书到 keys 目录、取备份和日志，p282）。
  tags: [ports, http, https, ssh, sftp]

- id: p24
  title: Standby 节点上 upam/nginx 服务停止是预期行为
  type: principle
  source_chapter: "p52"
  source_quote: |
    "Note that on Node 2, all services should be running except upam and nginx. It is the expected behavior on the Standby Node that these services will be "Stopped". The ovradius service may also be stopped when Custom RADIUS Certificates are used."
  summary: |
    健康检查判据：Standby 节点除 upam 和 nginx 外所有服务都应处于 Running；这两个服务在备节点上是"Stopped"属预期，不要误判为故障。使用自定义 RADIUS 证书时 ovradius 也可能停止。Active 节点则要求全部服务运行。
  tags: [ha, services, health-check, standby]

- id: p25
  title: 超过 256 台 Stellar AP 时升级后必须重新应用内存设置
  type: principle
  source_chapter: "p65"
  source_quote: |
    "If you are upgrading from a previous build and your network has more than 256 Stellar APs, you must re-apply your VA memory setting after completing the OmniVista upgrade... Select 2 - Display Current Configuration to verify your currently configured network size... Select 9 - Configure Network Size, then select your current memory configuration."
  summary: |
    从旧 build 升级后，如果网络中 Stellar AP 超过 256 台，必须重新走一遍 VA 内存设置：查看当前网络规模档位，重新选择相同档位（如 1-Low），确认并重启 Watchdog 服务，否则内存参数不生效。
  tags: [stellar-ap, upgrade, memory, post-upgrade]

- id: p26
  title: 修改 OV 服务器 IP 后网络侧需手动同步一整套配置
  type: principle
  source_chapter: "p276"
  source_quote: |
    "If you change the OV IP address in the VA Menu, the network is NOT touched. For wired devices, you must reconfigure the sFlow receiver, policy server, and SNMP trap station... For Stellar APs, you must reconfigure the DHCP Server, and reapply WLAN Services and Global Configurations in Unified Access."
  summary: |
    在 VA 菜单改 OV IP 只改服务器自身，网络设备不会被自动更新：有线设备需手动重配 sFlow 接收器、policy server、SNMP trap station，并从 Analytics、Policy View QoS、Notification 等应用重新推送配置；Stellar AP 需重配 DHCP 服务器并在 Unified Access 重新应用 WLAN 服务和全局配置。改 IP 后若 OmniVista 不可达，重启服务器。
  tags: [ip-change, network, sflow, trap, reconfiguration]

- id: p27
  title: 关机/重启必须先停服务，禁止直接断宿主机电源
  type: principle
  source_chapter: "p292"
  source_quote: |
    "Before powering off the VM, you must stop all OmniVista services using the Stop All Services option in the Run Watchdog Command. After all the services are stopped, enter 8 at the command line to power off the VM... Never simply power off the VM during any maintenance operation by shutting off the Hypervisor... Always shut down the VM first from the OmniVista Virtual Appliance Menu (Power Off option)."
  summary: |
    标准关机流程：先用 Watchdog 命令 Stop All Services（或 Shutdown Watchdog）停掉全部服务，再从 VA 菜单选 Power Off/Reboot。任何维护操作中都严禁通过关闭宿主机（Hypervisor）直接断电；HA 扩盘等操作全程不得对 VM 断电或复位，直到操作完成。
  tags: [power-off, shutdown, watchdog, safety]

- id: p28
  title: 内置备份策略参数与同版本恢复约束
  type: principle
  source_chapter: "p289"
  source_quote: |
    "Configure the maximum number of days that you want to retain backups (Range = 1 - 30, Default = 7), and the maximum number of backups that you want to retain (Range = 1 - 30, Default = 5)... You can only perform a restore using a backup from the same release... OmniVista will not allow you to perform a restore using a backup from a previous release."
  summary: |
    VA 菜单内置备份：保留天数 1-30（默认 7 天）、保留份数 1-30（默认 5 份），到期自动删除；可即时备份（Backup Now）或按 HH:mm 定时（间隔 1-30 天，默认 1 天），备份文件存于 backups 目录。恢复只允许同版本备份文件（如 4.5R3 备份只能恢复到 4.5R3）；跨系统恢复前需把目标机 OV/UPAM 的 IP 和端口改成与备份来源机一致，恢复后再改回。HA 安装的备份/恢复自 4.5R1 起才支持。
  tags: [backup, restore, retention, same-release]

- id: p29
  title: 4.6R2 起内存要求上调（Standalone 36GB / HA 40GB）
  type: principle
  source_chapter: "p177"
  source_quote: |
    "The reserved RAM requirement for standalone installations in a Medium network was increased to 36GB for OmniVista 4.6R2... The reserved RAM requirement for HA installations in a Medium network was increased to 40GB for OmniVista 4.6R2."
  summary: |
    从 4.6R2 版本起 Medium 网络规模的预留内存要求上调：独立安装 36GB、HA 安装 40GB。从 4.6R1/4.5Rx 升级到 4.6R2 及更高版本前，需先用 cliadmin 登录 VA 菜单 Power Off，从 Hypervisor 加内存，再开机等服务起来后开始升级。扩内存必须在关机状态下从 Hypervisor 侧操作。
  tags: [memory, upgrade, 4.6R2, ram-increase]

- id: p30
  title: 评估许可有效期 90 天及获取入口
  type: principle
  source_chapter: "p323"
  source_quote: |
    "An Evaluation License provides full OV 2500 NMS feature functionality but is valid only for 90 Days (starting from the date the license is generated). There is one file that contains all the Device (AOS, Third-Party, Stellar APs) and Service Licenses (VM, Guest, BYOD)."
  summary: |
    评估许可在生成日起 90 天内提供 OV2500 全部功能，单文件包含所有设备许可（AOS、第三方、Stellar AP）与服务许可（VM、Guest、BYOD）。通过 ALE 许可门户（lds.al-enterprise.com）申请：Customer ID 填 99999、Order Number 填 evaluation、Passcode 为 omnivista，邮箱收 4 位验证码，接受条款后生成许可文件并导入 OmniVista。
  tags: [license, evaluation, 90-days]

- id: p31
  title: 用服务档案（Service Profile）和交换文件节省资源
  type: principle
  source_chapter: "p287"
  source_quote: |
    "Choose Service Profile - Used to save memory if certain services are not required for your network... 2 - No Stellar, No UPAM... 3 - No Application Visibility... 4 - No IoT... 5 - No SFLOW. You can select multiple options... (e.g., 2 4 5)"
  summary: |
    Watchdog 菜单的服务档案可按需裁剪服务省内存：1-All Features（默认全开）；2-不开 Stellar/UPAM 服务；3-不开应用可视化；4-不开 IoT；5-不开 sFlow（Analytics 的 Top N）。2-5 可多选（空格分隔，如"2 4 5"），切换后所有 Watchdog 服务会重启。另有 Swap 文件功能：可添加 1-4096MB 的交换文件（p279）。
  tags: [service-profile, memory, swap, watchdog]
