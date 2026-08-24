# verified · OmniVista 2500 NMS 4.9R2 Installation and Upgrade Guide（阶段 1.5 三重验证通过集）

> 输入: candidates/（principles 31 · counter-examples 18 · glossary 28，共 77 条）
> 原文: source/fulltext.md（326 页，页码与 <<<PAGE N>>> 标记一致）
> 验证: V1 原文真实性（引文分片在对应页命中；表格/列表/跨页拼接逐条人工复核；summary 关键常数全文检索抽查）；V2 可操作价值；V3 独特性（ce 类升级陷阱默认全独特）

## 汇总

| 类型 | 候选 | 通过 | 淘汰 | 说明 |
|---|---|---|---|---|
| principles | 31 | 30 | 1 | p08 淘汰（与 ce18 逐字同源重复） |
| counter-examples | 18 | 18 | 0 | 引文全部真实，升级陷阱类全独特 |
| glossary | 28 | 28 | 0 | 免验保留 |
| 合计 | 77 | 76 | 1 | |

## 页码修正（11 条：引文真实但 source_chapter 引用偏差，已就地修正）

| id | 原页码 | 修正为 | 原因 |
|---|---|---|---|
| p05 | p8 | p8-9 | 引文跨 p8 页底与 p9 页顶 |
| p12 | p60 | p60-61 | 时长句在 p61 |
| p13 | p60 | p60-61,67 | HA 5-10 分钟句在 p67 |
| p15 | p64 | p68 | p64 无此内容，正文在 p68（及后续各版本章节） |
| p16 | p40 | p41 | L2/L3 定义段在 p41 |
| p17 | p40 | p40-41 | 转换规则横跨两页 |
| p27 | p292 | p292,8 | 停服务流程 p292；never-power-off 句在 p8 |
| p29 | p177 | p177,183 | Standalone 句 p177，HA 句 p183 |
| ce05 | p63 | p62 | 步骤 3 原文在 p62（p63 为后续步骤） |
| ce07 | p155 | p155,160 | 概述句 p155，详述步骤句 p160（同一流程） |
| ce10 | p64 | p64-65 | 主引文在 p65，HDD2 提示上下文在 p64 |

其他核对注记：p07 引文中的 "4.8R2" 系原文自身笔误（手册照录），非候选提取错误；p04 引文对应原文处 PDF 提取缺字（"o not exceed"），语义无损。

---

## principles（30 条）

- id: p01
  title: 四档网络规模的最低系统配置常数表
  type: principle
  source_chapter: "p9"
  source_quote: |
    "Total Number of Managed Devices 500 / 2,000 / 5,000 / 10,000 ... Hypervisor Processor 2.4 GHz, 8 Logical Processors (12 for High/Very High) ... Minimum Reserved OmniVista VA RAM for Standalone 20GB / 36GB / 64GB / 64GB ... Minimum Reserved RAM for HA N/A / 40GB / 64GB / 64GB ... Minimum Storage Read/Write Speed 100 / 150 / 200 / 200 MB/s"
  summary: |
    容量规划核心常数。Low/Medium/High/Very High 四档：管理设备总数 500/2000/5000/10000（其中 Stellar AP 上限分别为 500/2000/4000/4000，AP 客户端关联 5 万/20 万/20 万/20 万，UPAM 认证客户端 2 万/5 万/7.5 万/10 万）。CPU 需 2.4GHz，Low/Medium 8 个逻辑处理器，High/Very High 12 个。内存（独立安装）20/36/64/64GB，HA 安装 40/64/64GB（Low 档不支持 HA）。磁盘分区 1 固定 50GB，分区 2 分别 512GB/1TB/2TB/2TB。存储读写速度至少 100/150/200/200 MB/s。
  tags: [capacity, sizing, cpu, memory, storage]

  verify: V1 p9 命中（配置表逐值核对：500/2000/5000/10000、2.4GHz 8/12 逻辑核、20/36/64/64GB、N/A/40/64/64GB、分区 50GB+512GB/1TB/2TB/2TB、100/150/200/200 MB/s 及脚注 4000AP+500/1000/1500 AOS 全部一致）；V2 容量规划核心常数表；V3 产品专属常数
- id: p02
  title: HA 特性规模上限 4000 设备且必须 Medium 及以上规格
  type: principle
  source_chapter: "p11"
  source_quote: |
    "The High-Availability Feature supports up to 4,000 devices."
  summary: |
    HA（高可用）特性最多支持 4000 台设备；HA 安装必须建立在 Medium 或更高规格的 VA 上（Low 档不提供 HA 内存配置）。脚注补充：High 档 4000 台 Stellar AP 时最多支持 500 台 AOS 交换机；Very High 档 4000 台 AP 时 AOS 交换机可达 1000 台（HA Very High 可达 1500 台）。
  tags: [ha, capacity, limit]

  verify: V1 p11 逐字命中（含脚注 Medium-or-higher 与 AP/AOS 混合上限核对）；V2 HA 选型常数；V3 产品专属上限
- id: p03
  title: 仅以虚拟设备（VA）形式发行，支持三平台
  type: principle
  source_chapter: "p8"
  source_quote: |
    "OV 2500 NMS 4.9R2 is distributed as a Virtual Appliance only. There are no other standalone installers (e.g., Windows/Linux)... VMware ESXi: 6.5, 6.7 and 7.0.2, 8.0; MS Hyper-V: 2012 R2, 2016, 2019, and 2022; MS Hyper-V on Windows 10 Professional; Linux KVM/Ubuntu 22.04."
  summary: |
    4.9R2 只提供虚拟设备（VA）发行包，没有 Windows/Linux 独立安装器。支持的虚拟化平台：VMware ESXi 6.5/6.7/7.0.2/8.0；Microsoft Hyper-V 2012 R2/2016/2019/2022；Windows 10 专业版上的 Hyper-V；Linux KVM（Ubuntu 22.04）。
  tags: [distribution, hypervisor, esxi, hyperv, kvm]

  verify: V1 p8 逐字命中（bullet 列表逐条核对：ESXi 6.5/6.7/7.0.2/8.0、Hyper-V 2012R2-2022、Win10 Pro Hyper-V、KVM Ubuntu 22.04）；V2 平台兼容矩阵；V3 '仅 VA 交付、无独立安装器'为关键交付形态信息
- id: p04
  title: 内存与 CPU 分配规则：不超配、预留内存、CPU Shares 设 High
  type: principle
  source_chapter: "p10"
  source_quote: |
    "When provisioning RAM for a new VM for OmniVista, never allocate more memory than is available on the Host Server... it is recommended that you reserve that RAM for the OmniVista VM to prevent performance issues. Set CPU Shares to "High". Do not exceed the number of Logical Processors recommended for your network size."
  summary: |
    给 OmniVista VM 分配内存不得超过宿主机实际可用内存（例如 128GB 宿主机已分出 96GB 时再跑 OV 会出事故）；按网络规模表分配并建议在 Hypervisor 里"预留"该内存防止性能问题；CPU Shares 设为 High；逻辑处理器数量不要超过对应网络规模档位的推荐值（8 或 12）。
  tags: [memory, cpu, reservation, performance]

  verify: V1 p10 命中（原文 PDF 提取自身缺字 'o not exceed'，非候选错误）；V2 资源分配规则；V3 CPU Shares=High/预留内存为官方规定（个别子句偏通用虚拟化常识，整体保留）
- id: p05
  title: 网络规模档位受 VA 实际配置硬约束
  type: principle
  source_chapter: "p8-9"  # 页码修正（原 p8）
  source_quote: |
    "OmniVista will not allow you to configure a network size that cannot be supported by the VA configuration. For example, if you allocate 20GB of memory for the OmniVista VA, OmniVista will only allow you to configure a Low network size (fewer than 500 devices)."
  summary: |
    安装时选择的网络规模档位（Low/Medium/High/Very High）必须与 VA 实际配置匹配：内存或磁盘不足会导致 OV 不稳定，系统会直接拒绝配置超出 VA 配置的规模。例如只给 VA 分配 20GB 内存，则只能选 Low 档（500 台以下）。
  tags: [network-size, constraint, memory]

  verify: V1 命中（跨页拼接）；V2 档位与 VA 配置硬约束；V3 产品拒绝行为
- id: p06
  title: SNMPv3 AES 性能依赖 Intel AES-NI 指令集
  type: principle
  source_chapter: "p10"
  source_quote: |
    "A recommended algorithm is AES ("Advanced Encryption Standard"). To get the best performance from your hypervisor, we recommend that you use Intel processors with the AES-NI instruction set enabled... AES-NI must be enabled in your hypervisor's BIOS... The AES-NI feature must not be "masked" by your hypervisor."
  summary: |
    OmniVista 与设备通信可用 SNMPv3，推荐 AES 算法。要获得最佳性能，建议用 2010 年后的 Intel CPU（Westmere 及以后）并在 Hypervisor 的 BIOS 中开启 AES-NI，且该特性未被 Hypervisor 屏蔽；VMware 和 Hyper-V 默认直通（pass-through）AES 加速。
  tags: [snmpv3, aes-ni, cpu, security]

  verify: V1 p10 逐字命中（pass-through 句亦核对）；V2 SNMPv3 性能依赖；V3 AES-NI/BIOS/2010 后 CPU 细节独特
- id: p07
  title: 默认磁盘布局与扩盘规则：只能加新盘，不能改现有盘
  type: principle
  source_chapter: "p10"
  source_quote: |
    "By default, OV 2500 NMS 4.8R2 is partitioned as follows: HDD1:50GB and HDD2:512GB. If you are managing more than 500 devices, it is recommended that you go to the Virtual Appliance Menu on the VA to increase the OmniVista disk space... editing the size of existing virtual disks is not supported."
  summary: |
    默认分区为 HDD1 50GB + HDD2 512GB；管理超过 500 台设备时建议通过 VA 菜单扩盘（独立安装走 Configure Network Size - Extend Data Partition，HA 安装走 Configure Current Node - Extend Partitions）。扩容只能从 Hypervisor 添加新虚拟磁盘，不支持编辑既有虚拟盘的容量。
  tags: [disk, partition, extend, storage]

  verify: V1 p10 逐字命中（原文即写 '4.8R2'，系手册自身笔误，候选照录无误）；V2 默认布局+两平台扩盘菜单路径；V3 产品专属
- id: p09
  title: 升级矩阵：必须逐版本顺序升级到 4.9R2
  type: principle
  source_chapter: "p6-7"
  source_quote: |
    "If you are using release 4.7R1: 1. Upgrade to the 4.7R1 Patch 2 release. 2. Upgrade to 4.8R1. 3. Upgrade to 4.8R2. 4. Upgrade to 4.9R1... 5. Upgrade to 4.9R2."
  summary: |
    到 4.9R2 只能按升级矩阵逐级自动升级（从 VA 菜单执行），每级 Standalone/HA 均需完成：4.5R1→4.5R2→4.5R3→4.6R1→4.6R2→4.7R1→4.7R1 Patch 2→4.8R1→4.8R2→4.9R1→4.9R2。起点越新步数越少。4.7R1 Patch 2 需通过 Custom Repository（PatchRepo）获取。
  tags: [upgrade, upgrade-matrix, version]

  verify: V1 p6-7 命中（升级矩阵逐级核对）；V2 到 4.9R2 唯一路径；V3 逐级矩阵独特
- id: p10
  title: 每一步升级完成后必须验证服务与 Web GUI 再继续
  type: principle
  source_chapter: "p8"
  source_quote: |
    "As you complete each upgrade in the upgrade path, make sure all services are running and you can access the OmniVista Web GUI before proceeding to the next upgrade."
  summary: |
    长链路升级中，每完成一个版本升级都要确认：所有服务已运行（Watchdog 命令显示状态）、Build 号正确、能登录 OmniVista Web GUI，然后才能进入下一级升级。升级完成后还应拍新快照并删除旧快照。
  tags: [upgrade, verification, workflow]

  verify: V1 p8 逐字命中；V2 多跳升级链检查点；V3 单看偏常识，但绑定本产品 10 跳升级链+Watchdog/Build 核对，作为 SOP 步骤保留
- id: p11
  title: 旧于 4.5R1 的版本建议备份后全新安装
  type: principle
  source_chapter: "p8"
  source_quote: |
    "If your OmniVista is currently running a release older than 4.5R1, the sequential upgrade to the latest OmniVista release will take a very long time. Therefore, it is recommended that you take a backup of your existing OmniVista installation and start with a fresh installation of the latest OmniVista release."
  summary: |
    版本低于 4.5R1 时逐级升级耗时过长，官方建议：备份旧系统后直接全新安装最新版，再重新添加/发现设备并重做配置（Profile、Template、SSID 等），这样更快；代价是丢失历史统计数据（trap、统计等），如需保留可从旧系统导出。
  tags: [upgrade, migration, fresh-install]

  verify: V1 p8 逐字命中（含统计数据丢失与导出的说明核对）；V2 旧版本迁移决策规则；V3 4.5R1 阈值独特
- id: p12
  title: 升级必须在 VM Console 执行，升级窗口 1-4 小时
  type: principle
  source_chapter: "p60-61"  # 页码修正（原 p60）
  source_quote: |
    "You must perform the OmniVista upgrade directly from the VM Console. If you access OmniVista remotely using an SSH client, upgrading the installation can result in incomplete upgrades... The upgrade can take anywhere from 1 to 4 hours depending on network speed, network size, and database size."
  summary: |
    升级操作必须在虚拟机控制台（Hypervisor Console）直接执行；远程 SSH 升级可能造成升级不完整、漏掉"按回车继续"等交互。若必须用 SSH 客户端（如 putty），需配置周期性 keepalive 保活。单节点升级通常 1-2 小时，视网速/规模/数据量最长 3-4 小时。
  tags: [upgrade, console, ssh, duration]

  verify: V1 命中（时长句 p61）；V2 控制台强制+时长窗口；V3 SSH 会话陷阱独特
- id: p13
  title: 升级停机窗口：Standalone 全程不可管理，HA 仅切换时 5-10 分钟
  type: principle
  source_chapter: "p60-61,67"  # 页码修正（原 p60）
  source_quote: |
    "During the upgrade time for an OmniVista Standalone installation, OmniVista is not available for any management functions... new clients cannot join the network if the Switch/AP is configured to do authentication from UPAM. The upgrade downtime may last between one and four hours... For an OmniVista High-Availability installation, OmniVista management functions remain available until the failover stage... not available for approximately 5 to 10 minutes."
  summary: |
    独立安装升级期间 OmniVista 完全不可管理（1-4 小时，从启用维护模式起算），但已部署网络不受影响，已上线设备和客户端继续工作；唯一例外是交换机/AP 从 UPAM 做认证时新客户端无法入网。HA 安装升级期间管理功能持续可用，仅在 failover 阶段中断约 5-10 分钟。
  tags: [upgrade, downtime, maintenance-window, ha]

  verify: V1 命中（HA 句 p67）；V2 停机窗口规划依据；V3 独立 1-4 小时 vs HA 5-10 分钟数字独特
- id: p14
  title: HA 升级标准工作流：先维护模式、先升 Standby、角色互换正常
  type: principle
  source_chapter: "p67"
  source_quote: |
    "1. Enable Maintenance Mode on the Active Node (ov1) 2. Connect to the Standby Node and upgrade the node to 4.9R2 3. When the Standby Node upgrade is complete, do a reboot and failover... 4. Connect to the previous Active Node (ov1) and upgrade the node to 4.9R2... After this upgrade process is complete, the Active Node at the beginning of the process is no longer the Active Node. This is a perfectly normal state."
  summary: |
    HA 升级固定流程（4.8R1 及以后版本）：验证集群数据同步 Up to Date → 在 Active 节点启用维护模式 → 先升级 Standby 节点 → Standby 重启并 failover 成为新 Active → 等其所有服务起来后升级原 Active 节点 → 验证。升级结束后原 Active 变为 Standby 属正常状态，如需还原可手动 failover（切换期间服务中断 5-10 分钟）。
  tags: [ha, upgrade, workflow, failover]

  verify: V1 p67 命中（编号步骤拼接核对，含角色互换句）；V2 HA 升级标准 SOP；V3 顺序+角色互换属正常独特
- id: p15
  title: 维护模式在 Active 节点一次启用即对两节点生效
  type: principle
  source_chapter: "p68"  # 页码修正（原 p64）
  source_quote: |
    "Before performing the upgrade, you must first enable Maintenance Mode on the Active Node (ov1)... This will enable Maintenance Mode on both nodes in the Cluster."
  summary: |
    维护模式（Configure Cluster - Enable Maintenance Mode）只需在 Active 节点执行一次，即对集群两个节点同时生效；禁用同理，无需在 Standby 节点重复操作。这是 HA 升级和扩盘操作的前置条件。
  tags: [ha, maintenance-mode, cluster]

  verify: V1 命中（页码修正 p64→p68）；V2 维护模式操作前置；V3 单点启用双节点生效行为独特
- id: p16
  title: L2 与 L3 两种 HA 拓扑的选型规则
  type: principle
  source_chapter: "p41"  # 页码修正（原 p40）
  source_quote: |
    "Layer 2 Configuration - In a Layer 2 HA Configuration, both OmniVista Server VMs must be on the same subnet. In this configuration, you configure a virtual Cluster IP address... Layer 3 Configuration - In a Layer 3 HA Configuration the OmniVista Server VMs are on different subnets, with a unique IP address for each server."
  summary: |
    L2 HA：两台 VM 同子网，配一个虚拟 Cluster IP，内外都通过 Cluster IP 访问当前 Active；把现有独立安装的 IP 转成 Cluster IP 可避免全网设备重配地址。L3 HA：两台 VM 不同子网、各有独立 IP，设备需能同时与两个节点通信，failover 后设备自动改与新 Active 通信，但需要重新配置网络设备。新建集群时 L3 会随机指派 Active 节点（p59），需用 Show OV Cluster Status 确认。
  tags: [ha, layer2, layer3, cluster-ip]

  verify: V1 命中（页码修正 p40→p41；L3 随机指派 Active 见 p59 已核对）；V2 L2/L3 拓扑选型依据；V3 两拓扑差异独特
- id: p17
  title: HA 转换的前置条件与 L2 转 L3 禁止
  type: principle
  source_chapter: "p40-41"  # 页码修正（原 p40）
  source_quote: |
    "An HA license is required for a 4.9R2 HA Installation... You can convert a 4.9R2 Standalone Installation to a 4.9R2 HA Installation if the 4.9R2 Standalone installation was upgraded from a 4.3R2 or newer Standalone Installation. You cannot convert... if... upgraded from a 4.3R1 Standalone Installation. Converting an L2 HA installation to an L3 HA installation is not supported. Only a fresh L3 HA installation is supported."
  summary: |
    独立转 HA 的规则：必须先导入 HA License；全新 4.9R2 独立安装可转 HA；从 4.3R2 及更新版本升级而来的 4.9R2 独立安装也可转；从 4.3R1 升级来的不能转。L2 HA 不能转 L3 HA，L3 只能全新搭建（例外：可给全新 4.9R1 独立安装加第二个节点组成 L3，或 4.8R2 升到 4.9R1 后再转 L3）。
  tags: [ha, conversion, license, layer3]

  verify: V1 命中（页码修正→p40-41；两条 L3 例外 p41 已核对）；V2 转 HA 前置校验清单；V3 4.3R2 版本门槛独特
- id: p18
  title: L3 HA 的功能限制与 AP 型号门槛
  type: principle
  source_chapter: "p42"
  source_quote: |
    "Features or functions that require devices to contact OmniVista are not supported in a Layer 3 Configuration (e.g., sFlow, Policy)... Configuring L3 Redundancy Settings is supported only on AP13XX and higher models running AWOS 5.0 or higher; it is not supported on AP11XX or AP12XX models. Configuring a Preferred Node through the cliadmin menu is required for an L3 HA installation."
  summary: |
    L3 HA 下凡需要设备主动回连 OmniVista 的功能都受限：sFlow（Top N Apps/Ports）和 Policy 对 AOS 不支持；IoT 对 AOS 需 failover 后重应用；Syslog 需外部服务器或配置双节点 IP；DNS/Provisioning 需 failover 后重配 DNS。L3 冗余设置仅 AP13XX 及以上型号、AWOS 5.0+ 支持（AP11XX/12XX 不支持），且 L3 必须通过 cliadmin 菜单配置 Preferred Node。Captive Portal 在 L3 下被禁用（p50）。
  tags: [ha, layer3, limitations, stellar-ap]

  verify: V1 p42 逐字命中；V2 L3 功能受限清单+AP 门槛；V3 AP13XX/AWOS5.0 门槛独特
- id: p19
  title: HA 网络基础要求：1Gbps 带宽、1ms 延迟、最新网卡驱动
  type: principle
  source_chapter: "p42"
  source_quote: |
    "The Hypervisor's on which you are installing OmniVista must have the latest Network Adaptor drivers: Hyper-V: Broadcom b57nd60a.sys version 16.8 and later... VMware: Broadcom Tg3-3.133d.v55.1-101300361 and later. The recommended network bandwidth is 1Gbps. The recommended network latency is 1ms."
  summary: |
    HA 两节点间同步对网络质量敏感：推荐带宽 1Gbps、延迟 1ms；宿主机网卡驱动必须用最新版（Hyper-V 的 Broadcom b57nd60a.sys 16.8+，VMware 的 Broadcom Tg3-3.133d.v55.1-101300361+）。数据同步速度直接取决于数据量和两节点间网速。
  tags: [ha, network, bandwidth, latency, driver]

  verify: V1 p42 逐字命中（两个驱动版本号核对：b57nd60a.sys 16.8+、Tg3-3.133d.v55.1-101300361+）；V2 HA 网络基线；V3 1Gbps/1ms+驱动版本独特
- id: p20
  title: 节点 Hostname 规则：最长 15 字符且全小写
  type: principle
  source_chapter: "p47"
  source_quote: |
    "Enter a Hostname for Node 1 and press Enter. The Hostname can be up to 15 characters but must be lower case ("ov1" not "OV1")."
  summary: |
    HA 转换时 Node 1/Node 2 的主机名最多 15 个字符，且必须全小写（"ov1" 而非 "OV1"）；集群名（Cluster Name）为字母数字组合。独立安装的默认主机名是 omnivista，可改，同样限 15 字符。
  tags: [ha, hostname, naming]

  verify: V1 p47 逐字命中；V2 主机名输入约束；V3 15 字符小写规则独特
- id: p21
  title: 集群地址规划清单（转换前备齐）
  type: principle
  source_chapter: "p43"
  source_quote: |
    "To configure the Cluster, you will need IP addresses for the following: Node 1 - the physical IP address of the Active Node... Node 2... OV Virtual IP Address (Layer 2 Installation Only)... Captive Portal Virtual IP Address (Layer 2 Configuration Only)... Additional OV Web Virtual IP... must be on the same subnet as the Static Captive Portal IP address."
  summary: |
    转 HA 前需提前规划好：Node 1、Node 2 各自物理 IP；L2 专用的 OV 虚拟 IP（Cluster IP）；可选的 Captive Portal 虚拟 IP 与附加 OV Web 虚拟 IP（均仅 L2 可用，且必须与对应静态 IP 同子网）。转换 Node 1 时会先给节点分配新物理 IP，把原独立安装 IP 腾出来用作 Cluster IP，设备无需改地址。
  tags: [ha, ip-planning, cluster-ip]

  verify: V1 p43 逐字命中；V2 转 HA 前地址规划清单；V3 虚拟 IP 同子网约束独特
- id: p22
  title: 外部仓库与云服务的 443 端口白名单及代理要求
  type: principle
  source_chapter: "p40"
  source_quote: |
    "a Proxy should be configured to enable OV 2500 NMS 4.9R2 to connect to these external sites (Port 443): ALE Central Repository - ovrepo.fluentnetworking.com; AV Repository - ep1.fluentnetworking.com; Fleet Supervision FQDN - myfleet.ovcirrus.com; Call Home Backend - us.fluentnetworking.com; Device Fingerprinting Service - api.fingerbank.org; Web Content Filtering - api.bcti.brightcloud.com."
  summary: |
    OmniVista 需通过 HTTPS（443 端口）访问 6 个外部站点：ALE 中央仓库 ovrepo.fluentnetworking.com、AV 签名库 ep1.fluentnetworking.com、Fleet Supervision（myfleet.ovcirrus.com）、Call Home 后端（us.fluentnetworking.com）、设备指纹服务（api.fingerbank.org）、网页内容过滤（api.bcti.brightcloud.com）。服务器不直连互联网时必须配代理（VA 菜单 Configure Proxy），否则升级和云特性不可用。离线升级需联系客服。
  tags: [network, proxy, firewall, repository, ports]

  verify: V1 p40 逐字命中（6 个域名逐一核对）；V2 防火墙白名单/代理配置依据；V3 域名清单独特
- id: p23
  title: Web 与管理端口默认值及合法范围
  type: principle
  source_chapter: "p275"
  source_quote: |
    "HTTP Port (Valid range: 1024 to 65535, Default = 80); HTTPS Port (Valid range: 1024 to 65535, Default = 443)... Captive Portal: HTTP Port (Valid range: 1024 to 65535, Default = 8080); HTTPS Port (Valid range: 1024 to 65535, Default = 8443)"
  summary: |
    端口常数：OV Web 默认 HTTP 80、HTTPS 443；Captive Portal 默认 HTTP 8080、HTTPS 8443；合法范围均为 1024-65535 且新端口不得与已配端口重复。其他管理通道：VA 菜单 SSH 用端口 2222（cliadmin 用户，p272），SFTP 文件传输用端口 22（上传 SSL 证书到 keys 目录、取备份和日志，p282）。
  tags: [ports, http, https, ssh, sftp]

  verify: V1 p275 命中（端口表核对：80/443/8080/8443、范围 1024-65535；SSH 2222 见 p272、SFTP 22 见 p60/66 另行核对）；V2 端口常数；V3 默认值+范围独特
- id: p24
  title: Standby 节点上 upam/nginx 服务停止是预期行为
  type: principle
  source_chapter: "p52"
  source_quote: |
    "Note that on Node 2, all services should be running except upam and nginx. It is the expected behavior on the Standby Node that these services will be "Stopped". The ovradius service may also be stopped when Custom RADIUS Certificates are used."
  summary: |
    健康检查判据：Standby 节点除 upam 和 nginx 外所有服务都应处于 Running；这两个服务在备节点上是"Stopped"属预期，不要误判为故障。使用自定义 RADIUS 证书时 ovradius 也可能停止。Active 节点则要求全部服务运行。
  tags: [ha, services, health-check, standby]

  verify: V1 p52 逐字命中；V2 备节点健康检查判据；V3 upam/nginx 预期停止行为独特
- id: p25
  title: 超过 256 台 Stellar AP 时升级后必须重新应用内存设置
  type: principle
  source_chapter: "p65"
  source_quote: |
    "If you are upgrading from a previous build and your network has more than 256 Stellar APs, you must re-apply your VA memory setting after completing the OmniVista upgrade... Select 2 - Display Current Configuration to verify your currently configured network size... Select 9 - Configure Network Size, then select your current memory configuration."
  summary: |
    从旧 build 升级后，如果网络中 Stellar AP 超过 256 台，必须重新走一遍 VA 内存设置：查看当前网络规模档位，重新选择相同档位（如 1-Low），确认并重启 Watchdog 服务，否则内存参数不生效。
  tags: [stellar-ap, upgrade, memory, post-upgrade]

  verify: V1 p65 命中；V2 升级后置动作；V3 256 台 AP 阈值独特
- id: p26
  title: 修改 OV 服务器 IP 后网络侧需手动同步一整套配置
  type: principle
  source_chapter: "p276"
  source_quote: |
    "If you change the OV IP address in the VA Menu, the network is NOT touched. For wired devices, you must reconfigure the sFlow receiver, policy server, and SNMP trap station... For Stellar APs, you must reconfigure the DHCP Server, and reapply WLAN Services and Global Configurations in Unified Access."
  summary: |
    在 VA 菜单改 OV IP 只改服务器自身，网络设备不会被自动更新：有线设备需手动重配 sFlow 接收器、policy server、SNMP trap station，并从 Analytics、Policy View QoS、Notification 等应用重新推送配置；Stellar AP 需重配 DHCP 服务器并在 Unified Access 重新应用 WLAN 服务和全局配置。改 IP 后若 OmniVista 不可达，重启服务器。
  tags: [ip-change, network, sflow, trap, reconfiguration]

  verify: V1 p276 逐字命中；V2 改 IP 后网络侧联动清单；V3 手动同步范围独特
- id: p27
  title: 关机/重启必须先停服务，禁止直接断宿主机电源
  type: principle
  source_chapter: "p292,8"  # 页码修正（原 p292）
  source_quote: |
    "Before powering off the VM, you must stop all OmniVista services using the Stop All Services option in the Run Watchdog Command. After all the services are stopped, enter 8 at the command line to power off the VM... Never simply power off the VM during any maintenance operation by shutting off the Hypervisor... Always shut down the VM first from the OmniVista Virtual Appliance Menu (Power Off option)."
  summary: |
    标准关机流程：先用 Watchdog 命令 Stop All Services（或 Shutdown Watchdog）停掉全部服务，再从 VA 菜单选 Power Off/Reboot。任何维护操作中都严禁通过关闭宿主机（Hypervisor）直接断电；HA 扩盘等操作全程不得对 VM 断电或复位，直到操作完成。
  tags: [power-off, shutdown, watchdog, safety]

  verify: V1 命中（Stop All Services/enter 8 在 p292，never-power-off 句在 p8）；V2 标准关机 SOP；V3 停服务→菜单关机流程产品专属（'禁止直接断电'子句偏常识）
- id: p28
  title: 内置备份策略参数与同版本恢复约束
  type: principle
  source_chapter: "p289"
  source_quote: |
    "Configure the maximum number of days that you want to retain backups (Range = 1 - 30, Default = 7), and the maximum number of backups that you want to retain (Range = 1 - 30, Default = 5)... You can only perform a restore using a backup from the same release... OmniVista will not allow you to perform a restore using a backup from a previous release."
  summary: |
    VA 菜单内置备份：保留天数 1-30（默认 7 天）、保留份数 1-30（默认 5 份），到期自动删除；可即时备份（Backup Now）或按 HH:mm 定时（间隔 1-30 天，默认 1 天），备份文件存于 backups 目录。恢复只允许同版本备份文件（如 4.5R3 备份只能恢复到 4.5R3）；跨系统恢复前需把目标机 OV/UPAM 的 IP 和端口改成与备份来源机一致，恢复后再改回。HA 安装的备份/恢复自 4.5R1 起才支持。
  tags: [backup, restore, retention, same-release]

  verify: V1 p289 命中（HA 备份 4.5R1 起支持见 p318 另行核对）；V2 备份策略常数；V3 同版本恢复约束独特
- id: p29
  title: 4.6R2 起内存要求上调（Standalone 36GB / HA 40GB）
  type: principle
  source_chapter: "p177,183"  # 页码修正（原 p177）
  source_quote: |
    "The reserved RAM requirement for standalone installations in a Medium network was increased to 36GB for OmniVista 4.6R2... The reserved RAM requirement for HA installations in a Medium network was increased to 40GB for OmniVista 4.6R2."
  summary: |
    从 4.6R2 版本起 Medium 网络规模的预留内存要求上调：独立安装 36GB、HA 安装 40GB。从 4.6R1/4.5Rx 升级到 4.6R2 及更高版本前，需先用 cliadmin 登录 VA 菜单 Power Off，从 Hypervisor 加内存，再开机等服务起来后开始升级。扩内存必须在关机状态下从 Hypervisor 侧操作。
  tags: [memory, upgrade, 4.6R2, ram-increase]

  verify: V1 命中（HA 句 p183）；V2 升级前扩内存动作；V3 4.6R2 上调阈值独特
- id: p30
  title: 评估许可有效期 90 天及获取入口
  type: principle
  source_chapter: "p323"
  source_quote: |
    "An Evaluation License provides full OV 2500 NMS feature functionality but is valid only for 90 Days (starting from the date the license is generated). There is one file that contains all the Device (AOS, Third-Party, Stellar APs) and Service Licenses (VM, Guest, BYOD)."
  summary: |
    评估许可在生成日起 90 天内提供 OV2500 全部功能，单文件包含所有设备许可（AOS、第三方、Stellar AP）与服务许可（VM、Guest、BYOD）。通过 ALE 许可门户（lds.al-enterprise.com）申请：Customer ID 填 99999、Order Number 填 evaluation、Passcode 为 omnivista，邮箱收 4 位验证码，接受条款后生成许可文件并导入 OmniVista。
  tags: [license, evaluation, 90-days]

  verify: V1 p323 逐字命中（门户参数 99999/evaluation/omnivista/4 位码 p323-325 逐一核对）；V2 试用许可获取路径；V3 门户参数独特
- id: p31
  title: 用服务档案（Service Profile）和交换文件节省资源
  type: principle
  source_chapter: "p287"
  source_quote: |
    "Choose Service Profile - Used to save memory if certain services are not required for your network... 2 - No Stellar, No UPAM... 3 - No Application Visibility... 4 - No IoT... 5 - No SFLOW. You can select multiple options... (e.g., 2 4 5)"
  summary: |
    Watchdog 菜单的服务档案可按需裁剪服务省内存：1-All Features（默认全开）；2-不开 Stellar/UPAM 服务；3-不开应用可视化；4-不开 IoT；5-不开 sFlow（Analytics 的 Top N）。2-5 可多选（空格分隔，如"2 4 5"），切换后所有 Watchdog 服务会重启。另有 Swap 文件功能：可添加 1-4096MB 的交换文件（p279）。
  tags: [service-profile, memory, swap, watchdog]
  verify: V1 p287 命中（swap 1-4096MB 见 p279 另行核对）；V2 内存裁剪选项；V3 服务档案多选语法独特

## counter-examples（18 条）

- id: ce01
  title: 用 SSH 远程执行升级导致升级不完整
  type: counter-example
  source_chapter: "p60"
  source_quote: |
    "You must perform the OmniVista upgrade directly from the VM Console. If you access OmniVista remotely using an SSH client, upgrading the installation can result in incomplete upgrades and missing any pending actions, such as pressing the enter key to continue the upgrade."
  summary: |
    错误做法：用 putty 等 SSH 客户端远程跑升级。后果：升级流程中有多个"按回车继续"的交互提示，SSH 会话中断或不可见时会漏掉这些动作，造成升级不完整。正确做法：全程在 Hypervisor 控制台（VM Console）操作；确需 SSH 时配置周期 keepalive。HA 转 Cluster 过程同理——转换进行中禁止 SSH 登录 VM，必须等登录界面出现后从控制台登录（p44）。
  tags: [upgrade, ssh, console, incomplete-upgrade]

  verify: V1 p60 逐字命中；V2 升级操作纪律；V3 SSH 升级不完整陷阱（升级陷阱类全独特）
- id: ce02
  title: 直接关闭宿主机（Hypervisor）给 VM 断电
  type: counter-example
  source_chapter: "p8"
  source_quote: |
    "Never simply power off the VM during any maintenance operation by shutting off the Hypervisor (e.g., hardware upgrade). Always shut down the VM first from the OmniVista Virtual Appliance Menu (Power Off option)."
  summary: |
    错误做法：硬件升级等维护时直接关宿主机让 OmniVista VM"陪葬"断电。正确顺序：先 Watchdog 停全部服务，再从 VA 菜单 Power Off 关闭 VM（附录A p292）。扩展数据分区等长操作期间同样禁止对 VM 断电或复位，直到操作完成。
  tags: [power-off, hypervisor, data-integrity]

  verify: V1 p8 逐字命中；V2 数据保护顺序；V3 宿主机断电禁忌
- id: ce03
  title: VM 快照管理不当：不删旧快照、升级后长期保留快照
  type: counter-example
  source_chapter: "p8"
  source_quote: |
    "VM snapshots can cause performance issues on the running VM. When upgrading OmniVista, it is recommended that you delete any previous snapshots, take a new snapshot of the current VM configuration, then perform the upgrade. After OmniVista is successfully upgraded, it is recommended that you also delete the snapshot taken prior to the upgrade."
  summary: |
    两个坑：(1) 快照本身会拖累运行中 VM 的性能，叠加多个旧快照更糟；(2) 升级后把升级前快照长期留着，性能持续受损。正确节奏：升级/HA 转换前删除所有旧快照→拍一个新快照→执行操作→成功并验证后再删掉这个快照。长期备份应遵循虚拟化软件自身的备份方案，而不是靠快照。
  tags: [snapshot, upgrade, performance]

  verify: V1 p8 逐字命中；V2 快照管理节奏；V3 升级前后快照时序独特
- id: ce04
  title: 4.7R1 不打 Patch 2 直接升级 4.8R1
  type: counter-example
  source_chapter: "p143"
  source_quote: |
    "You must upgrade from OV 2500 NMS 4.7R1 to the 4.7R1 Patch 2 release before you can upgrade to 4.8R1. Upgrading to the patch first requires you to create a custom repository for the 4.7R1 Patch 2 image. If you are already running the 4.7R1 Patch 2 release, you can directly upgrade to 4.8R1."
  summary: |
    错误做法：4.7R1 GA 直接跳 4.8R1。升级矩阵强制经过 4.7R1 Patch 2，且该补丁不在默认仓库，必须先建自定义仓库（名称 PatchRepo，URL 为 https://ovrepo.fluentnetworking.com/ov/patch）并切换启用后才能下载；补丁装完还要把仓库切回 ALE Central Repo 再升 4.8R1。另注意 4.7R1→Patch2 的 HA 升级是全程完全停机（不像后续版本只在 failover 时停 5-10 分钟）。
  tags: [upgrade, 4.7R1, patch, custom-repository]

  verify: V1 p143 逐字命中（PatchRepo 名称与 ov/patch URL 见 p146 另行核对）；V2 补丁前置动作；V3 Patch2 强制+自建仓库独特
- id: ce05
  title: 4.9R1→4.9R2 升级跳过"To New Release→Exit"步骤或直接选升级到 4.9R2
  type: counter-example
  source_chapter: "p62"  # 页码修正（原 p63）
  source_quote: |
    "This step is required to successfully upgrade to the 4.9R2 release. DO NOT SKIP THIS STEP FOR ANY REASON. Enter 3 - To New Release and press Enter... then enter 0 - Exit... Do not select the option to upgrade to 4.9R2."
  summary: |
    4.9R1 升 4.9R2 的特殊坑：升级 4.9R2 自动包含强制的 4.9R1 Patch 1，必须先进入"3 - To New Release"菜单后立刻"0 - Exit"返回（刷新补丁索引），再选"2 - To 4.9R1（升级当前版本最新补丁）"，让系统在检查 4.9R1 补丁时检测到 4.9R2 包并提示自动升级。直接在 To New Release 里选"Upgrade to 4.9R2"或跳过刷新步骤都会导致升级失败。官方以"任何理由都不得跳过"强调此步。
  tags: [upgrade, 4.9R2, workflow, patch1]

  verify: V1 命中（页码修正 p63→p62，'DO NOT SKIP' 原文在 p62）；V2 4.9R1→4.9R2 升级关键步骤；V3 To New Release→0 Exit 强制刷新独特
- id: ce06
  title: 升级时选"Upgrade from downloaded package"（选项4）
  type: counter-example
  source_chapter: "p63"
  source_quote: |
    "You must select 2 - Download and Upgrade. Option 4 - Upgrade from a downloaded package is not supported."
  summary: |
    升级系统选项菜单里虽然列出"Download Only""Upgrade from a Download Package"，但在线升级场景必须选"2 - Download and Upgrade"，选项 4 不受支持。（例外：使用离线仓库 Offline Repo 时，Download and Upgrade 是唯一支持的方式，Download Only 与 Upgrade from a Download Package 均不支持，p317。）
  tags: [upgrade, repository, not-supported]

  verify: V1 p63 逐字命中（Offline Repo 例外见 p317 另行核对）；V2 升级菜单选择规则；V3 选项 4 不支持独特
- id: ce07
  title: HA 补丁升级时提前重启 Standby 节点（或新流程中该重启时不重启）
  type: counter-example
  source_chapter: "p155,160"  # 页码修正（原 p155）
  source_quote: |
    "Connect to the Standby Node and upgrade the node to 4.7R1 Patch 2. (As part of the upgrade process, do not reboot the Standby Node until the Active Node is upgraded.)... When the upgrade process is complete for the Standby Node, do not reboot the VM when prompted to do so. Wait until after upgrading the Active Node to reboot both VMs."
  summary: |
    两套流程的重启时机相反，极易混淆：(1) 4.7R1→Patch2 老流程（以及 4.5Rx/4.6Rx HA 升级）——先升 Active 再升 Standby，Standby 升完提示重启时必须忍住不重启，等两台都升完一起重启，否则集群状态不一致；(2) 4.8R1 及以后新流程——先升 Standby，升完必须立即按 r 重启并 failover，屏幕上的黄色 WARNING"另一节点未升级前勿重启"此时应忽略（p167）。
  tags: [ha, upgrade, reboot-timing, patch]

  verify: V1 命中（概述句 p155、详述句 p160 属同一流程）；V2 HA 升级重启时机；V3 新旧两套流程重启时机相反独特
- id: ce08
  title: 维护模式期间在 Standby 升级阶段做的配置变更会丢失
  type: counter-example
  source_chapter: "p69"
  source_quote: |
    "During the Standby Node upgrade process, OmniVista UI monitoring and UPAM authentications are available. However, any user-configured changes and network updates (such as Authentication Records, SNMP Traps, Device up/down status) made in the database are lost."
  summary: |
    误解：HA 升级期间管理功能"可用"就当作正常使用窗口。实际上 Standby 节点升级阶段（以及 failover 时点）产生的用户配置变更和网络状态更新——认证记录、SNMP trap、设备 up/down 状态——会被丢弃。升级窗口内应冻结一切配置变更；对比之下，原 Active 节点升级阶段做的变更会被保留（p76）。
  tags: [ha, maintenance-mode, data-loss, upgrade]

  verify: V1 p69 逐字命中；V2 升级窗口冻结要求；V3 Standby 阶段变更丢失/Active 阶段保留的对比独特
- id: ce09
  title: KVM 上扩盘：新盘选错总线类型或被前两块盘槽位坑
  type: counter-example
  source_chapter: "p280"
  source_quote: |
    "If you have a KVM deployment, when adding new storage, select Bus Type = SATA for new storage in KVM Settings. OmniVista only supports new storage in the SATA format. OmniVista on KVM does not detect the first two disks but does detect the third disk onward."
  summary: |
    KVM 专属坑：扩容盘必须是 SATA 总线（VirtIO 不识别）；且 OmniVista on KVM 检测不到前两块新盘、从第三块开始才识别。标准 workaround：先加两块 1KB 的占位 SATA 盘（disk1、disk2），再加真正有容量的 SATA disk3，用 disk3 扩容，且永远不要移除那两块占位盘。部署初期两块系统盘按手册选 VirtIO 并设置 Discard Mode=unmap（p33）。
  tags: [kvm, disk, sata, extend]

  verify: V1 p280 逐字命中（1KB 占位盘 workaround 见 p280/312 另行核对）；V2 KVM 扩盘操作；V3 SATA 总线+前三盘检测怪癖独特
- id: ce10
  title: 试图通过扩展现有虚拟磁盘容量来扩容
  type: counter-example
  source_chapter: "p64-65"  # 页码修正（原 p64）
  source_quote: |
    "Extending the data partition requires the installation of a second hard disk. If you are prepared to install a new hard disk, you can extend the hard disk now... Resizing of the existing hard disk is not supported."
  summary: |
    错误做法：直接在 Hypervisor 里把现有虚拟盘改大。OmniVista 不支持编辑既有虚拟盘容量，扩容唯一途径是新增第二块（或多块）虚拟磁盘，再从 VA 菜单 Extend Data Partition 并入。升级后登录时若提示 HDD2 容量低于当前规模要求，可先回车跳过后补扩容，但官方强烈建议按配置表补齐。
  tags: [disk, extend, not-supported]

  verify: V1 命中（页码修正 p64→p64-65，主引文在 p65）；V2 扩容正确途径；V3 改现有盘不支持独特
- id: ce11
  title: 集群初始化后修改 Peer Node 信息或本节点 IP
  type: counter-example
  source_chapter: "p303"
  source_quote: |
    "Enter 17 and press Enter to change the IP address and Hostname (maximum of 15 characters) of the Peer Node. It is not recommended to re-configure the Peer Node once a cluster is initialized. If you change the configuration, you must take a backup of OmniVista and contact Customer Support to re-configure the Cluster."
  summary: |
    错误做法：集群建好后随手改对端节点信息（Configure Peer Node's Information）或本节点 IP/端口（Configure IPs and Ports）。官方不推荐；真要改必须先做 OmniVista 备份并联系客服重配集群，否则集群可能失联。相对地，改 Cluster IP、Captive Portal 虚拟 IP、OV Web 端口等集群级参数是支持的（仅限 Active 节点操作，新 IP 须与节点同子网）。
  tags: [ha, cluster, ip-change, support]

  verify: V1 p303 逐字命中；V2 集群变更边界；V3 改 Peer Node 须备份+联系客服独特
- id: ce12
  title: 把从集群移除的节点拿来复用
  type: counter-example
  source_chapter: "p299"
  source_quote: |
    "Note that this command can only be issued on the Active Node. This command is generally used if there is a problem with the Standby Node and you wish to permanently remove it. Once the Node is removed from the Cluster, it is essentially unusable... it retains the HA Menu, so you cannot have it join another Cluster."
  summary: |
    误解：Remove Peer Node From Cluster 之后这台 VM 还能再加入别的集群。实际上被移除节点基本报废：浏览器连不上、保留 HA 菜单无法 Join 另一个集群；只能让新节点加入现存 Active 节点组成新集群配置。替换故障节点的正确路径：HA 单节点运行期间准备新 VM、把数据分区扩到与旧节点一致，再 Join Cluster（p60）。
  tags: [ha, cluster, node-replacement]

  verify: V1 p299 逐字命中；V2 节点替换正确路径；V3 被移除节点不可复用独特
- id: ce13
  title: 转集群时改动已有 Captive Portal 配置
  type: counter-example
  source_chapter: "p46"
  source_quote: |
    "If Captive Portal was already configured on the Node you are converting, it is recommended that you keep the existing configuration. If you do change the existing Captive Portal configuration, you must manually re-configure all Captive Portal related device configurations (including the Global Settings in the Unified Profile application)."
  summary: |
    独立转 HA 时如果节点上已配了 Captive Portal，转换向导里应保持原配置直接回车接受默认值；一旦改动，所有与 Captive Portal 相关的设备配置（含 Unified Profile 应用的 Global Settings）都要手动重配。L3 集群另有限制：原 Standalone 的 Captive Portal 会被直接禁用（p50）。
  tags: [ha, captive-portal, conversion]

  verify: V1 p46 逐字命中；V2 转换向导操作纪律；V3 Captive Portal 保持原配置约束独特
- id: ce14
  title: 数据同步未完成时就在节点上做配置
  type: counter-example
  source_chapter: "p296"
  source_quote: |
    "The data sync status indicates whether the data between two nodes is in sync. If it is, the field will indicate "Up to Date"... If a data sync is in progress, it is highly recommended to wait for a data sync to complete before doing performing any configuration on a Node."
  summary: |
    升级、扩盘、日常运维前都必须先看 Show OV Cluster Status：Data Sync 显示百分比（正在同步）时严禁在该节点做任何配置，否则变更可能被同步覆盖或造成分叉；必须等到显示"Up to Date"再操作。扩盘后禁用维护模式引发的重新同步也要等 10-20 分钟（p313）。
  tags: [ha, data-sync, cluster-status]

  verify: V1 p296 逐字命中；V2 集群操作前置检查；V3 同步中禁配置独特
- id: ce15
  title: 附加网卡配在已被管理设备所在的子网
  type: counter-example
  source_chapter: "p285"
  source_quote: |
    "Avoid configuring this network card on the same subnet as any existing devices that are already managed by the main OmniVista IP address. Doing so may cause your existing devices to fail to send traps/packets to OmniVista... The new adapter must be the same Adapter Type as first NIC."
  summary: |
    用 Configure Other Network Cards 加第二块网卡做跨子网发现时的坑：(1) 新网卡 IP 不能与主 OV IP 已管理的设备同子网，否则现有设备可能无法向 OmniVista 发送 trap/报文；(2) 新网卡必须与第一块网卡同型号（eth1 与 eth0 同类型）；(3) 通过新网卡发现的设备，其 trap station 需手动改到新网卡 IP——因为 OmniVista 配 trap 时默认写主 OV IP。
  tags: [nic, subnet, trap, discovery]

  verify: V1 p285 逐字命中；V2 附加网卡规划；V3 同子网陷阱+网卡同型约束独特
- id: ce16
  title: 把 L3 failover 后 AP 短暂"down"当真故障
  type: counter-example
  source_chapter: "p42"
  source_quote: |
    "When a failover occurs, the AP tries to establish a session with the other OmniVista server in the L3 HA installation. During this time, OmniVista will show that the AP is down (anywhere from 5 to 10 minutes); however, the AP remains up in the network."
  summary: |
    L3 HA failover 后 OmniVista 界面会把 AP 显示为 down 长达 5-10 分钟，实际 AP 在网络中仍正常工作，只是在与另一台 OV 服务器重建会话。排障时不要据此误判 AP 故障或急于重启设备。同理，L3 升级前若不停掉 ov1 上的 ovactivemq 服务，AP 会因看到该服务而尝试连旧节点导致重启——升级 ov1 前必须先停 ovactivemq 并等 10-15 分钟确认所有 AP/客户端在新 Active 上 UP（p92-93）。
  tags: [layer3, failover, stellar-ap, false-alarm]

  verify: V1 p42 逐字命中（ovactivemq 停用细节 p92-93 另行核对）；V2 failover 排障判据；V3 AP 假 down 5-10 分钟窗口独特
- id: ce17
  title: 在 Hyper-V 上使用 Live Migration 或新版 Hyper-V 跑 VM Manager
  type: counter-example
  source_chapter: "p19"
  source_quote: |
    "OmniVista does not support Hyper-V Live Migration. Also note that the OmniVista VM Manager application is supported only on Hyper-V 2012, 2012 R2, and 2016; it is not supported on Hyper-V 2019 or higher."
  summary: |
    Hyper-V 部署的两个不支持项：(1) OmniVista 不支持 Hyper-V 动态迁移（Live Migration），不要用 vMotion 类功能挪 VM；(2) OmniVista VM Manager 应用只支持 Hyper-V 2012/2012 R2/2016，在 2019 及以上版本不支持。规划虚拟化平台版本时要同时核对这两条。
  tags: [hyperv, live-migration, vm-manager, compatibility]

  verify: V1 p19 逐字命中；V2 虚拟化平台版本规划；V3 Live Migration 不支持+VM Manager 版本上限独特
- id: ce18
  title: 首次部署时就在 Hypervisor 里预加好扩展磁盘
  type: counter-example
  source_chapter: "p10"
  source_quote: |
    "When deploying the OmniVista VA for the first time, do not add the new disks in the hypervisor until after OmniVista is configured and rebooted. Note that editing the size of existing virtual disks is not supported."
  summary: |
    想一步到位的新手常见操作：部署 VA 前就把扩容盘挂好。官方明确要求首次部署时不要提前加盘，必须等 OmniVista 完成初始配置并重启之后再从 Hypervisor 添加。同样，三平台部署完 VM 后、进入"Completing the OmniVista Installation"之前，应先配好额外 NIC 再继续（p18/p24/p34）。
  tags: [deployment, disk, first-install, timing]
  verify: V1 p10 逐字命中（含同页拼接句 'editing...not supported'）；V2 首装加盘时机；V3 提前加盘禁忌独特（与 p08 同源，本条以反例框架保留）

## glossary（免验保留）（28 条）

- id: g01
  title: OmniVista 2500 NMS（OV2500）
  type: glossary
  source_chapter: "p1"
  source_quote: |
    "Installation and Upgrade Guide for OmniVista 2500 NMS, Version 4.9R2"
  summary: |
    ALE（阿尔卡特朗讯企业）的网管平台（NMS，网络管理系统），本手册的主角，用于管理 AOS 交换机、第三方设备和 Stellar 无线 AP。当前手册针对 4.9R2 版本（2025 年 5 月，Part Number 060957-00 Rev. B）。通过 Web UI（https://<服务器IP>）访问，首次登录需激活许可。
  tags: [product, nms, ale]

  verify: 免验保留（glossary 类不执行三重验证；引文经抽查与原文一致）
- id: g02
  title: VA（Virtual Appliance，虚拟设备）
  type: glossary
  source_chapter: "p8"
  source_quote: |
    "OV 2500 NMS 4.9R2 is distributed as a Virtual Appliance only. There are no other standalone installers (e.g., Windows/Linux)."
  summary: |
    OV2500 唯一的交付形态：预封装的虚拟机镜像（ESXi 用 OVF+VMDK，Hyper-V 用导入包，KVM 用 qcow2 双盘），部署到 Hypervisor 后开机经向导完成配置。没有裸机安装器。文档中 VA 也常代指这台 OmniVista 虚拟机本身。
  tags: [va, virtual-appliance, deployment]

  verify: 免验保留（glossary 类不执行三重验证；引文经抽查与原文一致）
- id: g03
  title: Standalone Installation（独立安装）
  type: glossary
  source_chapter: "p11"
  source_quote: |
    "OV 2500 NMS 4.9R2 can be installed in a Standalone or High-Availability configuration."
  summary: |
    单机部署模式：一台 VA 承担全部网管功能。内存要求低于 HA（如 Medium 档 36GB vs 40GB），但升级期间完全不可管理（1-4 小时停机）。可后续转换为 HA 安装（需 HA License 且来源版本 ≥4.3R2）。
  tags: [standalone, installation]

  verify: 免验保留（glossary 类不执行三重验证；引文经抽查与原文一致）
- id: g04
  title: HA Installation（High-Availability，高可用安装）
  type: glossary
  source_chapter: "p11"
  source_quote: |
    "A High-Availability Installation consists of two VMs (Node 1 and Node 2), with one node acting as the Active OV Server (Node 1) and the other as a Standby OV Server (Node 2). If Node 1 fails, OmniVista will automatically failover to Node 2."
  summary: |
    双机热备模式：两台 VM 组成集群，一台 Active 一台 Standby，Active 故障时自动切换到 Standby。需要 HA License，最多管 4000 台设备，必须 Medium 及以上规格。分 Layer 2 与 Layer 3 两种配置。升级采用滚动方式，仅在 failover 阶段中断 5-10 分钟。
  tags: [ha, high-availability, cluster]

  verify: 免验保留（glossary 类不执行三重验证；引文经抽查与原文一致）
- id: g05
  title: Cluster（集群）
  type: glossary
  source_chapter: "p40"
  source_quote: |
    "Once you have installed both VMs, you can convert them to a High-Availability Cluster Configuration."
  summary: |
    OV2500 HA 的实现形态：恰好两节点组成的集群，通过 VA 菜单 12（Convert to Cluster，Node 1 发起）和 13（Join Cluster，Node 2 加入）建立，集群有名称（字母数字）。集群级配置（Cluster IP、虚拟 IP、维护模式、Manual Failover 等）只能在 Active 节点的 Configure Cluster 菜单操作，且对两节点同时生效。
  tags: [cluster, ha]

  verify: 免验保留（glossary 类不执行三重验证；引文经抽查与原文一致）
- id: g06
  title: Node 1 / Node 2（节点 1 / 节点 2）
  type: glossary
  source_chapter: "p11"
  source_quote: |
    "two VMs (Node 1 and Node 2), with one node acting as the Active OV Server (Node 1) and the other as a Standby OV Server (Node 2). They are referred to as "Peer Nodes" in the installation process."
  summary: |
    HA 的两台 VM。Node 1 通常是原独立安装机（转集群时先 Convert to Cluster），Node 2 后加入（Join Cluster，需输入 Node 1 物理 IP 和 cliadmin 密码）。注意 L3 集群的 Active 角色由系统随机分配，不一定是 Node 1（p59）。手册示例主机名常为 ov1/ov2（≤15 字符、小写）。
  tags: [node, ha]

  verify: 免验保留（glossary 类不执行三重验证；引文经抽查与原文一致）
- id: g07
  title: Active Node / Standby Node（主用/备用节点）
  type: glossary
  source_chapter: "p11"
  source_quote: |
    "one node acting as the Active OV Server... the other as a Standby OV Server... If Node 1 fails, OmniVista will automatically failover to Node 2."
  summary: |
    Active 节点对外提供全部网管服务（所有服务 Running）；Standby 节点实时同步数据但 upam/nginx 服务停止（预期行为，p52）。HA 升级从升级 Standby 开始，完成后角色互换属正常。可通过 Manual Failover 手动切换，或用 Preferred Active Node 设定故障恢复后的主用节点（默认不设，p302）。
  tags: [active, standby, role]

  verify: 免验保留（glossary 类不执行三重验证；引文经抽查与原文一致）
- id: g08
  title: Failover（故障切换/手动切换）
  type: glossary
  source_chapter: "p40"
  source_quote: |
    "In the event of a failover, the Standby Node becomes the Active Node and network devices, again, communicate to it through the Cluster IP address."
  summary: |
    Active→Standby 的角色接管。故障时自动发生；HA 升级流程中在 Standby 节点升级重启后按回车触发；也可通过 Configure Cluster - 15 Manual Failover 手动发起。切换期间 UI 监控和 UPAM 认证中断约 5-10 分钟，切换后 UI 顶部会出现"Communication Failure"横幅（L3 下横幅含新 Active 链接，p302）。
  tags: [failover, ha, switchover]

  verify: 免验保留（glossary 类不执行三重验证；引文经抽查与原文一致）
- id: g09
  title: Cluster IP（集群虚拟 IP）
  type: glossary
  source_chapter: "p40"
  source_quote: |
    "you configure a virtual Cluster IP address. Both the Active and Standby Nodes are reached through the Cluster IP address. Network devices communicate with the Active Node through the Cluster IP address."
  summary: |
    Layer 2 HA 专属的对外虚拟 IP：设备和管理员始终访问 Cluster IP，实际由当前 Active 节点应答，failover 后自动漂移。最佳实践是把原独立安装的 OV IP 腾出来当 Cluster IP，设备无需改地址。可配的伴生虚拟 IP 还有 Captive Portal Virtual IP 和 Additional OV Web Virtual IP（均须与对应静态 IP 同子网）。禁用 Cluster IP 会连带禁用这两个虚拟 IP（p298）。
  tags: [cluster-ip, virtual-ip, layer2]

  verify: 免验保留（glossary 类不执行三重验证；引文经抽查与原文一致）
- id: g10
  title: Layer 2 / Layer 3 HA Configuration（二/三层 HA 配置）
  type: glossary
  source_chapter: "p40"
  source_quote: |
    "Layer 2 Configuration - both OmniVista Server VMs must be on the same subnet... Layer 3 Configuration - the OmniVista Server VMs are on different subnets, with a unique IP address for each server."
  summary: |
    两种 HA 拓扑：L2 要求两节点同子网，靠 Cluster IP 对外，设备零改动；L3 允许两节点跨子网、各有独立 IP，设备需能与两节点同时通信，须配 Preferred Node，且 sFlow/Policy 等依赖设备回连的功能受限、Captive Portal 被禁用、AP 需为 AP13XX+AWOS5.0+。L2 不能转 L3，L3 只能新建。
  tags: [layer2, layer3, topology]

  verify: 免验保留（glossary 类不执行三重验证；引文经抽查与原文一致）
- id: g11
  title: Maintenance Mode（维护模式）
  type: glossary
  source_chapter: "p64"
  source_quote: |
    "you must first enable Maintenance Mode on the Active Node (ov1). This will enable Maintenance Mode on both nodes in the Cluster."
  summary: |
    HA 升级和扩盘前的集群级状态（Configure Cluster 菜单 18），在 Active 节点一次启用/禁用即双节点生效。启用后进入维护窗口：独立安装的停机时间从启用维护模式起算。注意：Standby 升级完成后出现"请禁用维护模式"的提醒时不要立即禁用，要等两节点都升级完（p188）。
  tags: [maintenance-mode, ha, upgrade]

  verify: 免验保留（glossary 类不执行三重验证；引文经抽查与原文一致）
- id: g12
  title: Data Sync / "Up to Date"（数据同步状态）
  type: glossary
  source_chapter: "p67"
  source_quote: |
    "The data sync status indicates whether the data between two nodes is in sync. If it is, the field will indicate "Up to Date". If it is in the process of syncing, a percentage will be displayed... The speed of a data sync depends on the amount of data and the network speed between the two Nodes."
  summary: |
    Show OV Cluster Status 命令显示的两节点数据同步状态：显示"Up to Date"表示已同步，显示百分比表示同步中。任何升级、扩盘、节点配置操作前都必须确认 Up to Date；同步速度取决于数据量和节点间网速（推荐 1Gbps/1ms）。
  tags: [data-sync, cluster-status]

  verify: 免验保留（glossary 类不执行三重验证；引文经抽查与原文一致）
- id: g13
  title: VA Menu / HA Virtual Appliance Menu（虚拟设备菜单）
  type: glossary
  source_chapter: "p272"
  source_quote: |
    "To access the Virtual Appliance Menu for a VM, launch the Hypervisor Console... You can also access the Virtual Appliance Menu by connecting via SSH using port 2222, user cliadmin."
  summary: |
    OV2500 的运维控制台菜单，装好后 cliadmin 登录即见。独立版 Virtual Appliance Menu（选项含 Configure the Virtual Appliance、Run Watchdog、Upgrade/Backup/Restore、Convert/Join Cluster 等，附录A）；转 HA 后变为 HA Virtual Appliance Menu（新增 Show OV Cluster Status、Configure Cluster、Configure Current Node，附录B）。可从 Hypervisor 控制台或 SSH 端口 2222 访问。升级必须走控制台而非 SSH。
  tags: [va-menu, console, cli]

  verify: 免验保留（glossary 类不执行三重验证；引文经抽查与原文一致）
- id: g14
  title: Watchdog（服务看护命令集）
  type: glossary
  source_chapter: "p286"
  source_quote: |
    "The Watchdog command set is used to start and stop managed services used by OmniVista. If you stop certain framework services (e.g., ActiveMQ, Apache Tomcat)... the web server will shut down, and you will have to restart the service manually."
  summary: |
    VA 菜单选项 3/5，管理 OmniVista 全部后台服务：查看所有服务状态（升级/健康检查必用）、启停全部或单个服务（可带依赖树）、启停 Watchdog 本体、以及 Choose Service Profile（按需裁剪 Stellar/UPAM/应用可视化/IoT/sFlow 服务省内存）。停 ActiveMQ/Tomcat 等框架服务会连带关停 Web 服务器，需手动恢复。
  tags: [watchdog, services, operations]

  verify: 免验保留（glossary 类不执行三重验证；引文经抽查与原文一致）
- id: g15
  title: cliadmin
  type: glossary
  source_chapter: "p272"
  source_quote: |
    "1. Enter the login (cliadmin) and press Enter. 2. Enter the password and press Enter. The password is the one you created when you first launched the VM Console at the beginning of the installation process."
  summary: |
    VA 的管理账号：安装向导第 3 步设置其密码（丢失无法找回，须妥善保存）。用于登录 VA 菜单（控制台或 SSH 2222 端口）、SFTP（端口 22）取备份/日志/上传证书、Node 2 加入集群时的"Cluster Password"。相关联的还有 root、admin（UI 登录）、ftp、mongodb 等独立密码，均可从菜单修改。
  tags: [cliadmin, account, credentials]

  verify: 免验保留（glossary 类不执行三重验证；引文经抽查与原文一致）
- id: g16
  title: Network Size（网络规模档位）
  type: glossary
  source_chapter: "p37"
  source_quote: |
    "Ranges include: Low (fewer than 500 devices); Medium (500 to 2,000 devices); High (2,000 to 5,000 devices); Very High (5,000 to 10,000 devices)."
  summary: |
    安装时选择的管理规模档位，决定内存分配和可管理设备数：Low<500、Medium 500-2000、High 2000-5000、Very High 5000-10000。OmniVista 按所选档位分配内存，且禁止选择超出 VA 实际配置（内存/磁盘）的档位。后续可在 Configure Network Size 里改档或重应用（>256 台 Stellar AP 升级后必须重应用一次）。
  tags: [network-size, capacity]

  verify: 免验保留（glossary 类不执行三重验证；引文经抽查与原文一致）
- id: g17
  title: Extend Data Partition（扩展数据分区）
  type: glossary
  source_chapter: "p280"
  source_quote: |
    "By default, OmniVista is partitioned as follows: HDD1:50GB and HDD2:512GB. If you are managing more than 500 devices, it is recommended that you increase the provisioned hard disk."
  summary: |
    扩容数据盘的标准操作。独立安装路径：Configure the Virtual Appliance - 9 Configure Network Size - 4 Extend Data Partition；HA 路径：Configure Current Node - 17 Extend Partitions（选 OmniVista Data Partition，两节点都要做）。完整流程为停服务→备份/快照→VA 菜单关机→Hypervisor 加新盘→开机→菜单扩容。只支持加新盘，不支持改现有盘；KVM 有 SATA/前两盘不识别的特殊规则。
  tags: [extend, partition, storage]

  verify: 免验保留（glossary 类不执行三重验证；引文经抽查与原文一致）
- id: g18
  title: ALE Central Repo / Custom Repository（软件仓库）
  type: glossary
  source_chapter: "p288"
  source_quote: |
    "By default, the OV Virtual Appliance points to the external ALE Central Repository, which contains the latest OV software. However, you can configure up to three (3) custom repositories... Only one (1) repository can be enabled at a time."
  summary: |
    升级软件源。默认指向 ALE Central Repo（ovrepo.fluentnetworking.com）；可另配最多 3 个自定义仓库，同一时刻只能启用 1 个。典型用例：4.7R1 Patch 2 补丁仓库 PatchRepo（https://ovrepo.fluentnetworking.com/ov/patch）。多数升级流程强制要求把仓库切回"ALE Central Repo"这个默认名。仓库 URL 填写时不带 https:// 前缀。
  tags: [repository, upgrade, software-source]

  verify: 免验保留（glossary 类不执行三重验证；引文经抽查与原文一致）
- id: g19
  title: Captive Portal / UPAM（门户/准入认证）
  type: glossary
  source_chapter: "p34"
  source_quote: |
    "OmniVista supports configuration of three (3) IPs: the OmniVista IP, the Captive Portal IP and an additional OmniVista Web Management IP."
  summary: |
    Captive Portal 是无线访客/用户认证门户，由 UPAM（统一策略与准入管理，负责 BYOD/认证，如 802.1X、Portal 认证）承载，因此有独立 IP 与端口（默认 HTTP 8080 / HTTPS 8443，默认 FQDN ov2500-upam-cportal.al-enterprise.com）。三种部署方式推荐"独立子网+独立网卡"。HA 下仅 L2 支持虚拟门户 IP；L3 集群中 Captive Portal 被禁用。Standby 节点 upam 服务停止为预期；升级停机期间依赖 UPAM 认证的新客户端无法入网。
  tags: [captive-portal, upam, authentication]

  verify: 免验保留（glossary 类不执行三重验证；引文经抽查与原文一致）
- id: g20
  title: Stellar AP / AWOS
  type: glossary
  source_chapter: "p8"
  source_quote: |
    "If your network includes Stellar APs, they must be running one of the certified AWOS Releases specified in the OmniVista 2500 NMS Release Notes. If necessary, upgrade these devices after the OmniVista upgrade."
  summary: |
    Stellar 是 ALE 的无线 AP 产品线，AWOS 是其操作系统。版本强绑定：AP 必须跑 Release Notes 认证的 AWOS 版本，一般在 OmniVista 升级完成后再通过 Resource Manager - Upgrade Image 界面刷 AP 固件。规模常数：各档网络下 Stellar AP 上限 500/2000/4000/4000 台；>256 台时 OV 升级后须重应用内存设置；L3 冗余仅 AP13XX+（AWOS 5.0+）支持。
  tags: [stellar-ap, awos, wireless, firmware]

  verify: 免验保留（glossary 类不执行三重验证；引文经抽查与原文一致）
- id: g21
  title: AOS
  type: glossary
  source_chapter: "p9"
  source_quote: |
    "Total Number of Managed Devices (AOS, Third-Party, and Stellar APs)"
  summary: |
    ALE Operating System，ALE 有线交换机/路由设备的操作系统，本手册中 AOS 设备即有线交换机，与第三方设备、Stellar AP 并列为三类被管设备。规模换算示例：High 档 4000 台 Stellar AP 时最多再支持 500 台 AOS 交换机。L3 HA 下依赖设备回连 OV 的功能（sFlow、Policy、IoT 对 AOS）受限。
  tags: [aos, switch, wired]

  verify: 免验保留（glossary 类不执行三重验证；引文经抽查与原文一致）
- id: g22
  title: NTP Client（NTP 时间同步客户端）
  type: glossary
  source_chapter: "p283"
  source_quote: |
    "Configure NTP Client: 1. Enter 13 and press Enter to configure an NTP Server... Enter the IP address of the NTP Server and press Enter... You can enable the server when you create it, or enable it at a later time using option 5."
  summary: |
    VA 菜单的 NTP 服务器配置项（附录A 菜单 14，HA 节点在附录B Configure Current Node - 8）：输入 NTP 服务器 IP 即可创建，创建时可即时启用或稍后启用。HA 双节点与被管网络保持时间一致是日志、证书、集群同步的基础；高级模式还提供 ntpdate/ntpq/ntpstat 只读排查命令（p292）。
  tags: [ntp, time-sync]

  verify: 免验保留（glossary 类不执行三重验证；引文经抽查与原文一致）
- id: g23
  title: Technical Support Code（技术支持密码）
  type: glossary
  source_chapter: "p34"
  source_quote: |
    "Press Enter, then enter and confirm a Technical Support Code Password. This is a password that will be used by Technical Support to access the VM, if necessary."
  summary: |
    安装向导第 2 步设置的专用密码，供 ALE 技术支持在必要时访问 VM。安装结束时还会被提示输入。后续可在 Change Password 菜单（附录A 选项 5 - 4）修改。与 cliadmin/admin 等密码一样：丢失无法找回，必须安全保存。
  tags: [support, password, security]

  verify: 免验保留（glossary 类不执行三重验证；引文经抽查与原文一致）
- id: g24
  title: VM Snapshot（虚拟机快照）
  type: glossary
  source_chapter: "p8"
  source_quote: |
    "Take a VM Snapshot of the current OmniVista VA. Note that VM snapshots can cause performance issues on the running VM."
  summary: |
    升级和 HA 转换前的官方回退手段，但有代价：快照会拖累运行中 VM 的性能。标准用法是"一次性保险"：操作前删旧快照、拍新快照，操作成功验证后立即删除。不能当长期备份用，长期备份应遵循虚拟化平台自身的备份方案。
  tags: [snapshot, rollback, upgrade]

  verify: 免验保留（glossary 类不执行三重验证；引文经抽查与原文一致）
- id: g25
  title: Evaluation License（评估许可）
  type: glossary
  source_chapter: "p323"
  source_quote: |
    "An Evaluation License provides full OV 2500 NMS feature functionality but is valid only for 90 Days (starting from the date the license is generated)."
  summary: |
    90 天全功能试用许可（自生成日起算），单文件覆盖所有设备许可与服务许可。通过 ALE 许可门户生成（Customer ID 99999 / Order Number evaluation / Passcode omnivista，邮箱 4 位码验证），下载 .dat 文件后在 License - Add/Import License 界面导入。首次登录 OmniVista 会强制要求激活许可（正式或评估）。
  tags: [license, evaluation, trial]

  verify: 免验保留（glossary 类不执行三重验证；引文经抽查与原文一致）
- id: g26
  title: ovactivemq（ActiveMQ 消息服务）
  type: glossary
  source_chapter: "p92"
  source_quote: |
    "Upgrading the ov1 Node requires stopping the OmniVista ActiveMQ (ovactivemq) service before beginning the upgrade process. You must stop this service immediately after the ov2 Node upgrade is completed... This helps to avoid the possibility of APs rebooting and attempting to connect to the ov1 Node."
  summary: |
    OmniVista 的 ActiveMQ 消息中间件服务。AP 通过它发现并与当前 Active 节点保持会话。L3 HA 升级中，新 Active（ov2）就位后必须立即在旧节点 ov1 上停掉 ovactivemq（Stop a Service，不带 stop-tree），否则 AP 看到该服务仍会尝试连 ov1 而导致 AP 重启；停完等 10-15 分钟确认所有 AP/客户端在新节点 UP 后再升级 ov1。
  tags: [activemq, service, layer3-upgrade]

  verify: 免验保留（glossary 类不执行三重验证；引文经抽查与原文一致）
- id: g27
  title: upam / nginx（Standby 节点停用的服务）
  type: glossary
  source_chapter: "p52"
  source_quote: |
    "on Node 2, all services should be running except upam and nginx. It is the expected behavior on the Standby Node that these services will be "Stopped"."
  summary: |
    健康检查的关键判据服务：upam（准入认证服务）和 nginx（Web 前端/反向代理）只在 Active 节点运行，Standby 节点上显示 Stopped 是预期而非故障；使用自定义 RADIUS 证书时 ovradius 在备节点也可能停止。手动 failover 后原 Active 节点的这三个服务同样转为停止（p302）。
  tags: [upam, nginx, services, standby]

  verify: 免验保留（glossary 类不执行三重验证；引文经抽查与原文一致）
- id: g28
  title: Preferred Active Node（首选主用节点）
  type: glossary
  source_chapter: "p302"
  source_quote: |
    "The Preferred Active Node is the Node that will be set following a system failure. When the system returns, the Preferred Active Node will be the Active Node when the system returns... By default, no Preferred Active Node is set."
  summary: |
    集群偏好设置（Configure Cluster - 14）：指定系统故障恢复后应由哪个节点出任 Active；默认不设置，由系统自行决定。L3 HA 安装必须配置此项（通过 cliadmin 菜单，p42）。清除设置则回到"系统自动决定"行为。
  tags: [preferred-node, ha, failover]
  verify: 免验保留（glossary 类不执行三重验证；引文经抽查与原文一致）
