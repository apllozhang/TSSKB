# counter-examples · OmniVista 2500 NMS 4.9R2 Installation and Upgrade Guide
# 来源: D:\Claude code\TSSKB\books\ov2500-install\source\fulltext.md（页码为 PDF 页码）
# 性质: 升级/部署/HA 操作中的踩坑点与官方明确警告的错误做法

- id: ce01
  title: 用 SSH 远程执行升级导致升级不完整
  type: counter-example
  source_chapter: "p60"
  source_quote: |
    "You must perform the OmniVista upgrade directly from the VM Console. If you access OmniVista remotely using an SSH client, upgrading the installation can result in incomplete upgrades and missing any pending actions, such as pressing the enter key to continue the upgrade."
  summary: |
    错误做法：用 putty 等 SSH 客户端远程跑升级。后果：升级流程中有多个"按回车继续"的交互提示，SSH 会话中断或不可见时会漏掉这些动作，造成升级不完整。正确做法：全程在 Hypervisor 控制台（VM Console）操作；确需 SSH 时配置周期 keepalive。HA 转 Cluster 过程同理——转换进行中禁止 SSH 登录 VM，必须等登录界面出现后从控制台登录（p44）。
  tags: [upgrade, ssh, console, incomplete-upgrade]

- id: ce02
  title: 直接关闭宿主机（Hypervisor）给 VM 断电
  type: counter-example
  source_chapter: "p8"
  source_quote: |
    "Never simply power off the VM during any maintenance operation by shutting off the Hypervisor (e.g., hardware upgrade). Always shut down the VM first from the OmniVista Virtual Appliance Menu (Power Off option)."
  summary: |
    错误做法：硬件升级等维护时直接关宿主机让 OmniVista VM"陪葬"断电。正确顺序：先 Watchdog 停全部服务，再从 VA 菜单 Power Off 关闭 VM（附录A p292）。扩展数据分区等长操作期间同样禁止对 VM 断电或复位，直到操作完成。
  tags: [power-off, hypervisor, data-integrity]

- id: ce03
  title: VM 快照管理不当：不删旧快照、升级后长期保留快照
  type: counter-example
  source_chapter: "p8"
  source_quote: |
    "VM snapshots can cause performance issues on the running VM. When upgrading OmniVista, it is recommended that you delete any previous snapshots, take a new snapshot of the current VM configuration, then perform the upgrade. After OmniVista is successfully upgraded, it is recommended that you also delete the snapshot taken prior to the upgrade."
  summary: |
    两个坑：(1) 快照本身会拖累运行中 VM 的性能，叠加多个旧快照更糟；(2) 升级后把升级前快照长期留着，性能持续受损。正确节奏：升级/HA 转换前删除所有旧快照→拍一个新快照→执行操作→成功并验证后再删掉这个快照。长期备份应遵循虚拟化软件自身的备份方案，而不是靠快照。
  tags: [snapshot, upgrade, performance]

- id: ce04
  title: 4.7R1 不打 Patch 2 直接升级 4.8R1
  type: counter-example
  source_chapter: "p143"
  source_quote: |
    "You must upgrade from OV 2500 NMS 4.7R1 to the 4.7R1 Patch 2 release before you can upgrade to 4.8R1. Upgrading to the patch first requires you to create a custom repository for the 4.7R1 Patch 2 image. If you are already running the 4.7R1 Patch 2 release, you can directly upgrade to 4.8R1."
  summary: |
    错误做法：4.7R1 GA 直接跳 4.8R1。升级矩阵强制经过 4.7R1 Patch 2，且该补丁不在默认仓库，必须先建自定义仓库（名称 PatchRepo，URL 为 https://ovrepo.fluentnetworking.com/ov/patch）并切换启用后才能下载；补丁装完还要把仓库切回 ALE Central Repo 再升 4.8R1。另注意 4.7R1→Patch2 的 HA 升级是全程完全停机（不像后续版本只在 failover 时停 5-10 分钟）。
  tags: [upgrade, 4.7R1, patch, custom-repository]

- id: ce05
  title: 4.9R1→4.9R2 升级跳过"To New Release→Exit"步骤或直接选升级到 4.9R2
  type: counter-example
  source_chapter: "p63"
  source_quote: |
    "This step is required to successfully upgrade to the 4.9R2 release. DO NOT SKIP THIS STEP FOR ANY REASON. Enter 3 - To New Release and press Enter... then enter 0 - Exit... Do not select the option to upgrade to 4.9R2."
  summary: |
    4.9R1 升 4.9R2 的特殊坑：升级 4.9R2 自动包含强制的 4.9R1 Patch 1，必须先进入"3 - To New Release"菜单后立刻"0 - Exit"返回（刷新补丁索引），再选"2 - To 4.9R1（升级当前版本最新补丁）"，让系统在检查 4.9R1 补丁时检测到 4.9R2 包并提示自动升级。直接在 To New Release 里选"Upgrade to 4.9R2"或跳过刷新步骤都会导致升级失败。官方以"任何理由都不得跳过"强调此步。
  tags: [upgrade, 4.9R2, workflow, patch1]

- id: ce06
  title: 升级时选"Upgrade from downloaded package"（选项4）
  type: counter-example
  source_chapter: "p63"
  source_quote: |
    "You must select 2 - Download and Upgrade. Option 4 - Upgrade from a downloaded package is not supported."
  summary: |
    升级系统选项菜单里虽然列出"Download Only""Upgrade from a Download Package"，但在线升级场景必须选"2 - Download and Upgrade"，选项 4 不受支持。（例外：使用离线仓库 Offline Repo 时，Download and Upgrade 是唯一支持的方式，Download Only 与 Upgrade from a Download Package 均不支持，p317。）
  tags: [upgrade, repository, not-supported]

- id: ce07
  title: HA 补丁升级时提前重启 Standby 节点（或新流程中该重启时不重启）
  type: counter-example
  source_chapter: "p155"
  source_quote: |
    "Connect to the Standby Node and upgrade the node to 4.7R1 Patch 2. (As part of the upgrade process, do not reboot the Standby Node until the Active Node is upgraded.)... When the upgrade process is complete for the Standby Node, do not reboot the VM when prompted to do so. Wait until after upgrading the Active Node to reboot both VMs."
  summary: |
    两套流程的重启时机相反，极易混淆：(1) 4.7R1→Patch2 老流程（以及 4.5Rx/4.6Rx HA 升级）——先升 Active 再升 Standby，Standby 升完提示重启时必须忍住不重启，等两台都升完一起重启，否则集群状态不一致；(2) 4.8R1 及以后新流程——先升 Standby，升完必须立即按 r 重启并 failover，屏幕上的黄色 WARNING"另一节点未升级前勿重启"此时应忽略（p167）。
  tags: [ha, upgrade, reboot-timing, patch]

- id: ce08
  title: 维护模式期间在 Standby 升级阶段做的配置变更会丢失
  type: counter-example
  source_chapter: "p69"
  source_quote: |
    "During the Standby Node upgrade process, OmniVista UI monitoring and UPAM authentications are available. However, any user-configured changes and network updates (such as Authentication Records, SNMP Traps, Device up/down status) made in the database are lost."
  summary: |
    误解：HA 升级期间管理功能"可用"就当作正常使用窗口。实际上 Standby 节点升级阶段（以及 failover 时点）产生的用户配置变更和网络状态更新——认证记录、SNMP trap、设备 up/down 状态——会被丢弃。升级窗口内应冻结一切配置变更；对比之下，原 Active 节点升级阶段做的变更会被保留（p76）。
  tags: [ha, maintenance-mode, data-loss, upgrade]

- id: ce09
  title: KVM 上扩盘：新盘选错总线类型或被前两块盘槽位坑
  type: counter-example
  source_chapter: "p280"
  source_quote: |
    "If you have a KVM deployment, when adding new storage, select Bus Type = SATA for new storage in KVM Settings. OmniVista only supports new storage in the SATA format. OmniVista on KVM does not detect the first two disks but does detect the third disk onward."
  summary: |
    KVM 专属坑：扩容盘必须是 SATA 总线（VirtIO 不识别）；且 OmniVista on KVM 检测不到前两块新盘、从第三块开始才识别。标准 workaround：先加两块 1KB 的占位 SATA 盘（disk1、disk2），再加真正有容量的 SATA disk3，用 disk3 扩容，且永远不要移除那两块占位盘。部署初期两块系统盘按手册选 VirtIO 并设置 Discard Mode=unmap（p33）。
  tags: [kvm, disk, sata, extend]

- id: ce10
  title: 试图通过扩展现有虚拟磁盘容量来扩容
  type: counter-example
  source_chapter: "p64"
  source_quote: |
    "Extending the data partition requires the installation of a second hard disk. If you are prepared to install a new hard disk, you can extend the hard disk now... Resizing of the existing hard disk is not supported."
  summary: |
    错误做法：直接在 Hypervisor 里把现有虚拟盘改大。OmniVista 不支持编辑既有虚拟盘容量，扩容唯一途径是新增第二块（或多块）虚拟磁盘，再从 VA 菜单 Extend Data Partition 并入。升级后登录时若提示 HDD2 容量低于当前规模要求，可先回车跳过后补扩容，但官方强烈建议按配置表补齐。
  tags: [disk, extend, not-supported]

- id: ce11
  title: 集群初始化后修改 Peer Node 信息或本节点 IP
  type: counter-example
  source_chapter: "p303"
  source_quote: |
    "Enter 17 and press Enter to change the IP address and Hostname (maximum of 15 characters) of the Peer Node. It is not recommended to re-configure the Peer Node once a cluster is initialized. If you change the configuration, you must take a backup of OmniVista and contact Customer Support to re-configure the Cluster."
  summary: |
    错误做法：集群建好后随手改对端节点信息（Configure Peer Node's Information）或本节点 IP/端口（Configure IPs and Ports）。官方不推荐；真要改必须先做 OmniVista 备份并联系客服重配集群，否则集群可能失联。相对地，改 Cluster IP、Captive Portal 虚拟 IP、OV Web 端口等集群级参数是支持的（仅限 Active 节点操作，新 IP 须与节点同子网）。
  tags: [ha, cluster, ip-change, support]

- id: ce12
  title: 把从集群移除的节点拿来复用
  type: counter-example
  source_chapter: "p299"
  source_quote: |
    "Note that this command can only be issued on the Active Node. This command is generally used if there is a problem with the Standby Node and you wish to permanently remove it. Once the Node is removed from the Cluster, it is essentially unusable... it retains the HA Menu, so you cannot have it join another Cluster."
  summary: |
    误解：Remove Peer Node From Cluster 之后这台 VM 还能再加入别的集群。实际上被移除节点基本报废：浏览器连不上、保留 HA 菜单无法 Join 另一个集群；只能让新节点加入现存 Active 节点组成新集群配置。替换故障节点的正确路径：HA 单节点运行期间准备新 VM、把数据分区扩到与旧节点一致，再 Join Cluster（p60）。
  tags: [ha, cluster, node-replacement]

- id: ce13
  title: 转集群时改动已有 Captive Portal 配置
  type: counter-example
  source_chapter: "p46"
  source_quote: |
    "If Captive Portal was already configured on the Node you are converting, it is recommended that you keep the existing configuration. If you do change the existing Captive Portal configuration, you must manually re-configure all Captive Portal related device configurations (including the Global Settings in the Unified Profile application)."
  summary: |
    独立转 HA 时如果节点上已配了 Captive Portal，转换向导里应保持原配置直接回车接受默认值；一旦改动，所有与 Captive Portal 相关的设备配置（含 Unified Profile 应用的 Global Settings）都要手动重配。L3 集群另有限制：原 Standalone 的 Captive Portal 会被直接禁用（p50）。
  tags: [ha, captive-portal, conversion]

- id: ce14
  title: 数据同步未完成时就在节点上做配置
  type: counter-example
  source_chapter: "p296"
  source_quote: |
    "The data sync status indicates whether the data between two nodes is in sync. If it is, the field will indicate "Up to Date"... If a data sync is in progress, it is highly recommended to wait for a data sync to complete before doing performing any configuration on a Node."
  summary: |
    升级、扩盘、日常运维前都必须先看 Show OV Cluster Status：Data Sync 显示百分比（正在同步）时严禁在该节点做任何配置，否则变更可能被同步覆盖或造成分叉；必须等到显示"Up to Date"再操作。扩盘后禁用维护模式引发的重新同步也要等 10-20 分钟（p313）。
  tags: [ha, data-sync, cluster-status]

- id: ce15
  title: 附加网卡配在已被管理设备所在的子网
  type: counter-example
  source_chapter: "p285"
  source_quote: |
    "Avoid configuring this network card on the same subnet as any existing devices that are already managed by the main OmniVista IP address. Doing so may cause your existing devices to fail to send traps/packets to OmniVista... The new adapter must be the same Adapter Type as first NIC."
  summary: |
    用 Configure Other Network Cards 加第二块网卡做跨子网发现时的坑：(1) 新网卡 IP 不能与主 OV IP 已管理的设备同子网，否则现有设备可能无法向 OmniVista 发送 trap/报文；(2) 新网卡必须与第一块网卡同型号（eth1 与 eth0 同类型）；(3) 通过新网卡发现的设备，其 trap station 需手动改到新网卡 IP——因为 OmniVista 配 trap 时默认写主 OV IP。
  tags: [nic, subnet, trap, discovery]

- id: ce16
  title: 把 L3 failover 后 AP 短暂"down"当真故障
  type: counter-example
  source_chapter: "p42"
  source_quote: |
    "When a failover occurs, the AP tries to establish a session with the other OmniVista server in the L3 HA installation. During this time, OmniVista will show that the AP is down (anywhere from 5 to 10 minutes); however, the AP remains up in the network."
  summary: |
    L3 HA failover 后 OmniVista 界面会把 AP 显示为 down 长达 5-10 分钟，实际 AP 在网络中仍正常工作，只是在与另一台 OV 服务器重建会话。排障时不要据此误判 AP 故障或急于重启设备。同理，L3 升级前若不停掉 ov1 上的 ovactivemq 服务，AP 会因看到该服务而尝试连旧节点导致重启——升级 ov1 前必须先停 ovactivemq 并等 10-15 分钟确认所有 AP/客户端在新 Active 上 UP（p92-93）。
  tags: [layer3, failover, stellar-ap, false-alarm]

- id: ce17
  title: 在 Hyper-V 上使用 Live Migration 或新版 Hyper-V 跑 VM Manager
  type: counter-example
  source_chapter: "p19"
  source_quote: |
    "OmniVista does not support Hyper-V Live Migration. Also note that the OmniVista VM Manager application is supported only on Hyper-V 2012, 2012 R2, and 2016; it is not supported on Hyper-V 2019 or higher."
  summary: |
    Hyper-V 部署的两个不支持项：(1) OmniVista 不支持 Hyper-V 动态迁移（Live Migration），不要用 vMotion 类功能挪 VM；(2) OmniVista VM Manager 应用只支持 Hyper-V 2012/2012 R2/2016，在 2019 及以上版本不支持。规划虚拟化平台版本时要同时核对这两条。
  tags: [hyperv, live-migration, vm-manager, compatibility]

- id: ce18
  title: 首次部署时就在 Hypervisor 里预加好扩展磁盘
  type: counter-example
  source_chapter: "p10"
  source_quote: |
    "When deploying the OmniVista VA for the first time, do not add the new disks in the hypervisor until after OmniVista is configured and rebooted. Note that editing the size of existing virtual disks is not supported."
  summary: |
    想一步到位的新手常见操作：部署 VA 前就把扩容盘挂好。官方明确要求首次部署时不要提前加盘，必须等 OmniVista 完成初始配置并重启之后再从 Hypervisor 添加。同样，三平台部署完 VM 后、进入"Completing the OmniVista Installation"之前，应先配好额外 NIC 再继续（p18/p24/p34）。
  tags: [deployment, disk, first-install, timing]
