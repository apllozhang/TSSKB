# glossary.md · OmniSwitch LAN Troubleshooting (DT00XTE221EN) 术语候选条目

- id: g01
  title: TKC（Technical Knowledge Center，技术知识中心）
  type: term
  source_chapter: "p24"
  source_quote: |
    "Technical Knowledge Center – a Database composed of technical articles. These articles are written by the Technical Support."
  summary: |
    ALE 技术支持维护的用例知识库，经 Partner Portal / My Portal 访问。用例固定结构：Case Description（拓扑/场景/环境/诊断）+ Resolution（配置/热补丁/固件升级）。支持自然语言检索与 Research/Solution/Dates/Article type 过滤器。售后排障第一步的查库对象。
  tags: [tkc, knowledge-base, support]

- id: g02
  title: Spacewalkers（ALE 开放技术社区）
  type: term
  source_chapter: "p34"
  source_quote: |
    "It's an Open Technical Community providing a great place to connect with other members ... who share the same passion on Alcatel-Lucent Enterprise Network Solutions"
  summary: |
    ALE 面向合作伙伴与用户的开放技术社区（www.spacewalkers.com）：论坛提问与标记已解决（Mark as resolved）、新闻、博客、资源/直播栏目、开发者中心（API）。排障的第二查证渠道（论坛历史帖）与求助渠道。
  tags: [community, forum, spacewalkers]

- id: g03
  title: AOS（Alcatel-Lucent Enterprise Operating System，AOS R8）
  type: term
  source_chapter: "p1"
  source_quote: |
    "OMNISWITCH LAN - R8.X TROUBLESHOOTING - EDITION 13 PARTICIPANT'S GUIDE"
  summary: |
    OmniSwitch 交换机网络操作系统，本课程基于 R8.X（第 13 版教材）。文件体系含 certified/working/user 目录、vcboot.cfg/vcsetup.cfg、按机型命名的镜像文件（Uos.img、Tos.img、kaos.img、Nosa.img、Wos.img、Yos.img、Mhost.img 等，p70/99）。文档族：Hardware Users Guide、Switch Management Guide、Network Configuration Guide、Advanced Routing Configuration Guide、CLI Reference Guide、Transceivers Guide（p10）。
  tags: [aos, omniswitch, r8, documentation]

- id: g04
  title: CMM（Control Management Module，控制管理模块）
  type: term
  source_chapter: "p98"
  source_quote: |
    "sw1 (6900-A) -> show cmm ... CPLD 1: 2.0 ... CPU Model Type: Intel Atom 3558 ... ONIE Version: 2019.08.00.03"
  summary: |
    交换机的管理模块（主控），运行 AOS 控制面。show cmm 看型号、硬件版本、CPLD/FPGA 版本、CPU、管理 MAC；模块化机型（9900）支持主备 CMM（PRI 灯指示 Primary/Secondary）。与 NI（网络接口模块）之间状态不一致是常见故障源（p100）。
  tags: [cmm, hardware, management-module]

- id: g05
  title: NI（Network Interface module，网络接口模块）
  type: term
  source_chapter: "p100"
  source_quote: |
    "Management Module of the switch (CMM) ... NI Network Interface ... Monitor & synchronizes"
  summary: |
    承载业务端口的线卡模块。show module status 看 CMM 与各 NI 的 Operational/Admin 状态与 MAC；每块 NI 分布式运行大部分 L2 与基础 L3 进程（分布式软件架构是故障切换时业务不中断的基础，p502）。CPU 高时可用 show health slot <chassis/slot> 下钻到具体 NI。
  tags: [ni, line-card, distributed]

- id: g06
  title: Working / Certified / User 目录（闪存双目录机制）
  type: term
  source_chapter: "p70"
  source_quote: |
    "Rollback Based on the working, certified and User-defined directories ... FLASH MEMORY: WORKING, CERTIFIED, NETWORK"
  summary: |
    AOS 闪存目录机制：certified（已认证的稳定配置与镜像）、working（工作目录，改动先落这里）、network、用户自定义目录（可存多套配置）。show running-directory 显示当前运行目录与同步状态；modify running working/certified 切换运行目录；copy certified working 同步。回滚能力即建立在目录对上——配置改坏可从 certified 重启恢复。
  tags: [flash, working, certified, rollback]

- id: g07
  title: U-Boot（引导加载程序）
  type: term
  source_chapter: "p71"
  source_quote: |
    "Bootstrap Basic Operation (U-Boot): Hardware Initialization, Memory Diagnostics, Image selection, AOS is copied and loaded into RAM"
  summary: |
    OmniSwitch（非 ONIE 机型，如 6360/6560/6860）的引导程序。启动流程：硬件初始化→内存诊断→按 bootfile 环境变量选镜像→AOS 复制进 RAM 运行。运维入口：启动时 "Hit any key to stop autoboot:" 打断进 u-boot 提示符，可 setAdminPasswordDefault 做密码恢复、setenv bootfile working/Uos.img + saveenv 改启动目录（p92）、printenv 查看环境变量。版本门槛见 release note 与 show hardware-info 的 U-Boot Version 字段。
  tags: [uboot, bootloader, boot-sequence]

- id: g08
  title: ONIE（Open Network Install Environment）
  type: term
  source_chapter: "p72"
  source_quote: |
    "How to Exit From ONIE Menu of OS6860N and OS6900 switches: Step1. Press 'c' for command-line ... Enter command 'exit'"
  summary: |
    开放网络安装环境，OS6860N 与 OS6900 等机型采用。启动菜单可选 ALE OS - certified 或 ONIE（含 Install/Rescue/Uninstall/Update 与 DIAG 诊断模式）。运维用途：从 console 进 ONIE 做 USB 恢复（mount /dev/sda1→onie-nos-install /var/tmp/Uosn.img，p87-90）与密码恢复（DIAG 模式 rm userTable8，p78-79）。show cmm/show hardware-info 可见 ONIE Version。
  tags: [onie, boot-menu, recovery, os6860n]

- id: g09
  title: vcsetup.cfg / vcboot.cfg（VC 配置对）
  type: term
  source_chapter: "p163"
  source_quote: |
    "! File: /flash/working/vcsetup.cfg ... virtual-chassis chassis-id 1 configured-chassis-id 1 ... virtual-chassis chassis-id 1 vf-link 0 member-port 1/2/1"
  summary: |
    虚拟机箱的两个关键文件：vcsetup.cfg 定义每台成员的机箱号、VFL 模式与成员口、机箱组、优先级、EMP 地址（启动早期读取，用于建 VC）；vcboot.cfg 是 VC 形成后的整机运行配置，由 Master 下发给不一致的 Slave 并以其重启（p161）。文件内 [SAVED INFO] 区禁止修改；解析错误会写入 vcsetup.cfg.N.err 文件。
  tags: [vcsetup, vcboot, virtual-chassis, config]

- id: g10
  title: VC（Virtual Chassis，虚拟机箱/堆叠）
  type: term
  source_chapter: "p158"
  source_quote: |
    "Virtual Chassis = Group of Switches which appears as a single router or bridge ... No STP/VRRP between Access and Core ... Upgrade via ISSU ... No license needed"
  summary: |
    多台交换机虚拟成单一逻辑设备：单点管理、跨机箱冗余、接入到核心无需 STP/VRRP、支持 ISSU 升级、无需许可。成员经专用或可选 SFP+/QSFP 端口互连，Mesh 或 Ring 拓扑。规模上限按机型（p514）：8×OS6560、8×OS6865/6860E/N、4×OS6360、4×OS6465、6×OS6900、2×OS9900。Master/Slave 选举依据（p521）：最高优先级→最长 uptime（差>10 分钟才算）→最小 chassis ID→最小 MAC。
  tags: [virtual-chassis, stacking, vc]

- id: g11
  title: VFL（Virtual Fabric Link，虚拟机箱互连链路）
  type: term
  source_chapter: "p165"
  source_quote: |
    "OS6860-> show virtual-chassis vf-link ... Primary Config Active ... Port Port Port Vlan Type Speed
    1/0 Up 1/1/30 2 2 1 21G"
  summary: |
    VC 成员机箱之间的互连链路（内部以 LACP 聚合），可专用堆叠口（如 6360/6560 的 20G VFL 口、6860 的 QSFP）或复用业务 SFP+/QSFP 口。分 static 模式（手工配 member-port，OS6900 风格）与 auto 模式（auto-vf-link-port，stackport 平台如 6360 必须用 auto，见 ce07）。VFL 链路速率不可混用（p515）。排障主命令 show virtual-chassis vf-link / vf-link member-port。
  tags: [vfl, stacking-link, lacp]

- id: g12
  title: EMP（Ethernet Management Port，以太网管理口）
  type: term
  source_chapter: "p528"
  source_quote: |
    "Setup EMP network to allow distinction between a switch down and VFL trunk down ... Each switch sends / receives RCD announcements to and from its peers over the EMP port"
  summary: |
    带外管理以太网口，配独立管理 IP（vcsetup.cfg 中 ip interface local chassis-id N emp address ...）。双重价值：1) 业务面瘫痪时（如环路打挂 in-band 管理）的带外访问通道（LAB2 用 EMP SSH 登 6870）；2) 承载 RCD（Remote Chassis Detection）协议做 VC 脑裂检测。无 EMP 机型组成的 VC 需指定管理 VLAN+IP 接口替代（p534）。
  tags: [emp, out-of-band, management-port, rcd]

- id: g13
  title: RCD / VCSP / SSP（VC 脑裂检测与保护机制）
  type: term
  source_chapter: "p527"
  source_quote: |
    "Failures on VFL links cause potential MAC/IP duplication. 2 mechanisms: Out of Band: EMP Remote Chassis Detection (RCD); In Band: VC Split Protocol"
  summary: |
    VFL 双断导致 VC 分裂、两侧出现重复 MAC/IP 的两套"Master"。两大防护机制：RCD（带外，经 EMP 口互发通告，区分"整机 down"与"VFL 断"，仅 OS6860E/6900/9900 等有 EMP 机型）；VCSP（VC Split Protocol，带内，需上游/下游 helper 交换机，每台成员建议各出一端口加入去往 helper 的 VCSP LAG）。检测到分裂后：含原 Master 的子 VC 保持 MASTER，另一子 VC 自动进入 Protection 模式——关闭所有用户口（仅留 VFL/LAG）。OS6465/6360 等堆叠平台对应协议为 SSP（Split Stack Protection，p539-540）。
  tags: [vc-split, rcd, vcsp, ssp, split-brain, protection-mode]

- id: g14
  title: ISSU（In-Service Software Upgrade，不中断升级）
  type: term
  source_chapter: "p532"
  source_quote: |
    "issu from new-image command executed ... Master sends ISSU command to each Slave as per Chassis Id sequence ... When Slave is ready, Master issues VC Takeover and reboot"
  summary: |
    VC 不中断业务升级序列：Master 先校验新镜像与当前版本兼容性→Slave 从 Master 拷贝镜像与 vcboot.cfg→按 Chassis ID 顺序逐台 Slave 重启（ready 后下一台）→全部就绪后 Master 执行 VC Takeover 并重启，指定 Slave 接管 Master 角色。VC 的核心高可用卖点之一（p158："Upgrade via ISSU, Minimize network impact"）。
  tags: [issu, upgrade, vc, takeover]

- id: g15
  title: STP / RSTP / MSTP（生成树协议族）
  type: term
  source_chapter: "p169"
  source_quote: |
    "IEEE Standard supported: 802.1D (STP), 802.1w (RSTP), 802.1Q 2005 (MSTP) ... Spanning Tree operating mode: flat Mode (single STP instance per switch), per-Vlan Mode (single STP instance per VLAN)"
  summary: |
    维持无环拓扑的自配置算法族：STP(802.1D)、RSTP(802.1w 快速收敛)、MSTP(802.1Q-2005 多生成树)。AOS 运行模式分 flat（每机箱单实例）与 per-VLAN（每 VLAN 单实例）；MSTI 上限：flat 模式 16 个 MSTI+IST0，per-VLAN 按 VC 规模 100/128/252 实例（机型相关，p169）。端口角色 RP/DP/ALT，根桥由最低桥 ID（优先级+MAC）选出，默认优先级 32768。
  tags: [stp, rstp, mstp, loop-prevention]

- id: g16
  title: BPDU / TCN（网桥协议数据单元 / 拓扑变化通知）
  type: term
  source_chapter: "p183"
  source_quote: |
    "Port rxCfg rxRstp rxMstp rxTcn | txCfg txRstp txMstp txTcn ... -> debug stp bpdu-stats 1 start"
  summary: |
    BPDU 是 STP/RSTP/MSTP 的协议报文（配置/拓扑/协商）；TCN 是拓扑变化通知，收到 TC 的交换机会缩短 MAC 老化引发泛洪。排障意义：本应阻塞的口变转发=BPDU 被丢或链路故障（p180）；TC 每 1-4 分钟一次=网络频繁拓扑变化，查哪个 VLAN/端口进来（p185）；debug stp bpdu-stats 统计每端口收发分类计数（p183）。
  tags: [bpdu, tcn, stp, topology-change]

- id: g17
  title: 根桥（Root Bridge）与桥优先级
  type: term
  source_chapter: "p188"
  source_quote: |
    "Factors to Consider When Choosing a Root Bridge: Location ... Processing Power and Memory ... Reliability ... Network Design"
  summary: |
    生成树拓扑的原点，由优先级（默认 32768）+MAC 决定。选根四要素：位置（网络中心，缩短控制帧传播与收敛时间）、处理能力与内存（根桥负担最重）、可靠性、网络设计（多 VLAN 可多根分布）。运维铁律：用 priority 明确"设计"根桥，不要让选举随机发生；根桥位置漂移是很多"网络变慢"的隐性根因（p187 设计原则）。
  tags: [root-bridge, priority, stp-design]

- id: g18
  title: Loop Guard / UDLD / LBD（环路防护三件套）
  type: term
  source_chapter: "p187"
  source_quote: |
    "Think about additional features: Loop-guard ... Configure the UDLD (UniDirectional Link Detection) ... Loopback Detection (LBD) ... qos user-port {filter | shutdown} bpdu"
  summary: |
    STP 的补强特性：Loop Guard（限制端口角色，防非预期成为根口/指定口的 Root Guard 同族）；UDLD（单向链路检测——单向链路+阻塞口场景有 50% 概率成桥接环，p187）；LBD（环回检测）；qos user-port filter/shutdown bpdu（对用户口收 BPDU 做过滤或关停，防私接交换机）。设计期就该启用的防环冗余层。
  tags: [loop-guard, udld, lbd, root-guard, safety-net]

- id: g19
  title: swlog / appid / subapp（交换机日志体系）
  type: term
  source_chapter: "p146"
  source_quote: |
    "Switch events can be logged to Switch console, Local text file, Multiple remote devices (syslog) ... show swlog ... Console Display Level: info"
  summary: |
    AOS 事件日志系统：输出到 console、flash（/flash/swlog_chassis1~.6，归档 40 文件）、远程 syslog（最多 12 台，需 Loopback0）。日志按应用（appid，如 ospf_0/vrrp_0/pim_0/slNi/portMgrCmm）与子应用（subapp，如 hello/auth/macmove）组织，可 per-app 调级别（swlog appid X subapp Y level debug3）。查看：show swlog（状态）/ show log swlog（内容，支持 grep/timestamp/reverse）。可读事件层：level event + show log events（CUSTLOG，p154）。
  tags: [swlog, logging, appid, syslog]

- id: g20
  title: MAC flapping（MAC 漂移/摆动）
  type: term
  source_chapter: "p181"
  source_quote: |
    "MAC address flapping is mostly caused by a layer 2 loop in the network (which are not detected by STP) ... show mac-learning mac-address 00:13:72:19:5e:1f"
  summary: |
    同一 MAC 地址的出端口在两个（或多个）端口间反复切换，多由 STP 检测不到的 L2 环路引起，伴随 ARP 反复覆盖、DoS invalid-ip 告警、CPU 升高（LAB2 完整案例）。检测：show mac-learning mac-address 多次采样看出端口变化；swlog appid slNi subapp macmove level debug2 后 show log swlog |grep MACMOVE 看 INS/DEL 记录的端口交替。
  tags: [mac-flapping, loop, slni, macmove]

- id: g21
  title: DHL（Dual Home Link，双归属链路 Active-Active）
  type: term
  source_chapter: "p509"
  source_quote: |
    "DHL Active-Active splits a number of VLANs between two active links ... Two DHL links are both active ... Available on OS6360, OS6560, OS6860"
  summary: |
    AOS 特有的接入双上联方案：接入交换机两条上联链路同时活跃，按 VLAN 拆分负载（Link A VLAN 集 / Link B VLAN 集），不用 STP 即可防环并实现快速故障切换。每交换机一个 DHL 会话（链路 A+B）；可配在普通端口或链路聚合口。约束：两条链路的 native（untagged）VLAN 必须一致（LAB3 根因）；上联非核心设备会成环，需 LPS/Loop Guard/BPDU Shutdown 防护（p511）。状态显示为 forwarding/dhl-blocking。
  tags: [dhl, dual-home, active-active, access-uplink]

- id: g22
  title: Linkagg / LACP（链路聚合）
  type: term
  source_chapter: "p117"
  source_quote: |
    "REMINDER: ... Link Aggregation 1/1/23-24 ... 802.1q ... Client 7 pings Client 5 on the same VLAN (subnet)"
  summary: |
    多条物理链路捆绑为一条逻辑链路（LAG），动态聚合遵循 802.3ad LACP。show linkagg port 看成员口状态（ATTACHED、Agg 编号、Oper、Prim）。排障语境：VLAN 必须被允许在 linkagg 上（p118 列为常见错配）；linkagg 成员口 down 的日志链（LAB5 用例3：Convergence port down、LACP Sync Out）；TKC 案例 N1 即 VC 重载后 linkagg 成员保持 DOWN 的软件缺陷。
  tags: [linkagg, lacp, lag, 802-3ad]

- id: g23
  title: UNP（Universal Network Profile，通用网络档案）
  type: term
  source_chapter: "p134"
  source_quote: |
    "Once authenticated, a Universal Network Profile (UNP) is applied to the network users. (ex: Client 5) ... employee -> VLAN 20 UNP-employee deny_employee 802.1x"
  summary: |
    按用户/设备身份动态下发的网络档案：VLAN + Policy List（ACL/QoS），认证途径含 802.1X、MAC、Captive Portal，来源可为 RADIUS Filter-Id 或本地分类规则。用户初始 UNP/VLAN 生命周期内不变，仅角色（role）动态变化（p564）。排障命令族：show unp user（认证状态 Active/In progress）、show unp port/global/profile map/classification、aaa test-radius-server。已知缺陷形态：UNP 用户卡 In progress（TKC 案例 N2，LAB1 用 unp user flush 清理）。
  tags: [unp, user-profile, access-guardian, 8021x]

- id: g24
  title: Access Guardian（接入卫士安全框架）
  type: term
  source_chapter: "p559"
  source_quote: |
    "Access Guardian Security framework: Authentication (802.1x, MAC, Captive Portal, RADIUS server), Classification (UNP profile rules...), Role-Based Access (UNP profiles, QoS policy lists...), Restrict or Block (Restricted roles, Re-authentication, Quarantine, Remediation, filter MAC)"
  summary: |
    AOS 统一接入安全框架，四大块：认证（802.1X/MAC/Captive Portal/RADIUS）、分类（UNP 规则）、基于角色的访问（profile+policy list）、限制与阻断（受限角色、重认证、隔离、修复、MAC 过滤）。R8 支持机型 OS9900/6900/6860E/N/6865/6560/6465/6360。BYOD 场景与 UPAM（User Profile Application Manager，与 OmniVista 2500 协作）联动（p558）。
  tags: [access-guardian, security, framework]

- id: g25
  title: VRRP（Virtual Router Redundancy Protocol，虚拟路由器冗余协议）
  type: term
  source_chapter: "p249"
  source_quote: |
    "Virtual Router VRID = 1 on VLAN = 1 ... Priority = 100 ... Virtual MAC = 00-00-5E-00-01-01"
  summary: |
    默认网关冗余协议：多台路由器共用虚拟 IP+虚拟 MAC（00-00-5E-00-01-<VRID>），Master 响应 ARP 并发通告（目的组播 224.0.0.18）。关键参数：Priority（默认 100，大者胜）、Advertisement Interval（须全网同 VRID 一致）、Skew_Time=(256-P)/256、Master_Down=3×Adv+Skew。排障：show ip vrrp（admin/priority/地址）、show ip vrrp statistics（Checksum/Version/VRID 三错误计数与 Master/Backup/Initialize 状态）、debug 用 swlog appid vrrp_0 subapp all level debug3（用完回 info）。
  tags: [vrrp, gateway-redundancy, vrid]

- id: g26
  title: OSPF（开放最短路径优先）与 DR/BDR、LSDB、LSA
  type: term
  source_chapter: "p239"
  source_quote: |
    "Exstart State: DR & BDR form adjacencies ... Exchange State: Sharing Link State information Database Description (DBD) packets ... Full State: Master & Slave synchronized
    - Hello interval: 10 seconds (keep-alive function) - Dead interval: 40 seconds"
  summary: |
    链路状态路由协议。邻居状态机：Down→Init→2-Way（选 DR/BDR）→Exstart→Exchange(DBD)→Loading(LSR/LSU/LSAck)→Full。广播网默认 Hello 10s/Dead 40s（两端必须一致）。术语：DR/BDR（指定/备份指定路由器）、LSDB（链路状态数据库）、LSA（链路状态通告，尺寸超 MTU 会发送失败）。排障命令族见 p29；典型错配：timer、认证、area、掩码（p238）。
  tags: [ospf, dr, bdr, lsdb, lsa]

- id: g27
  title: RIP（路由信息协议）
  type: term
  source_chapter: "p235"
  source_quote: |
    "Status = Enabled, Update interval = 30, Invalid interval = 180, Garbage interval = 120, Holddown interval = 0, Forced Hold-Down Timer = 0"
  summary: |
    距离矢量路由协议，以跳数为度量。定时器：update 30s、invalid 180s、garbage 120s（show ip rip 可见）。v1/v2 兼容规则与认证一致性要求见 p28。排障：show ip rip [peer|interface|routes]（路由状态 A=Active/H=Holddown/G=Garbage）、show log swlog |grep rip、swlog appid rip_0 subapp 调级。
  tags: [rip, distance-vector, timers]

- id: g28
  title: PIM-SM（协议无关组播-稀疏模式）与 RP/BSR/C-RP
  type: term
  source_chapter: "p270"
  source_quote: |
    "show ip pim sparse: Status = enabled, Keepalive Period = 210, Max RPs = 32 ... show ip pim neighbor ... DR Priority"
  summary: |
    组播路由协议（共享树 RP 模型）。术语：RP（汇RP 点，* ,G 树根）、C-RP（候选 RP，向 BSR 通告）、BSR（自举路由器，收集并扩散 RP 集）、SPT（最短路径树，(S,G) 直连源）。接口参数：Hello 30s、Join/Prune 60s、DR 选举。排障命令族 show ip pim [neighbor|candidate-rp|interface|group-map|sgroute|notifications]；debug 分区 subapp hello/boot-strap/crp/sm-join-prune。RPF 跟随单播路由表（LAB4：单播通组播不通→沿 traceroute 路径逐口核 PIM 使能）。
  tags: [pim, pim-sm, rp, bsr, multicast]

- id: g29
  title: DVMRP（距离矢量组播路由协议）与 DF
  type: term
  source_chapter: "p265"
  source_quote: |
    "If there are multiple DVMRP routers on a subnet ... One of the routers will be selected as the designated forwarder for each source/group pair ... Election by: Lowest metric, As tie breaker, lowest IP address"
  summary: |
    早期组播路由协议，含 prune（修剪）机制与隧道。DF（Designated Forwarder）：同一网段多台 DVMRP 路由器时按（源,组）对选举唯一转发者，先比最低 metric、平手比最低 IP，避免重复包。排障：show ip dvmrp [neighbor|route|prune|interface|nexthop|tunnel]、show ip mroute；debug 用 swlog appid dvmrp_0 subapp routes/ipmrm。
  tags: [dvmrp, multicast, designated-forwarder, prune]

- id: g30
  title: IGMP / Querier / Proxying / Zapping（组播管理术语）
  type: term
  source_chapter: "p258"
  source_quote: |
    "There should be 1 dedicated querier in the network ... Querier-forwarding ... Zapping should be enabled only on edge devices ... IGMP messages must be sent with TTL equal 1"
  summary: |
    IGMP：主机组播成员管理协议（查询/报告/离开）。Querier：网段上周期发通用查询的路由器/交换机，全网只应一个（多则选举，其余 inactive）；Querier Forwarding：源与 querier 之间设备上启用，转发查询；Proxying：代理主机报告，可全网启用；Zapping：快速频道切换优化，仅边缘启用。IGMP 报文 TTL 必须 1。监测：show ip multicast [group|forward|source]、show interfaces flood rate、debug ip packet show-multicast。
  tags: [igmp, querier, multicast-l2, zapping, ipms]

- id: g31
  title: QoS 策略三要素（condition / action / rule）
  type: term
  source_chapter: "p214"
  source_quote: |
    "policy condition cond1 source ip 192.168.8.10 icmptype 8
    policy action action1
    policy rule rule1 condition cond1 action action1 log
    qos apply"
  summary: |
    AOS QoS 策略模型：condition（匹配条件，如 source ip + icmptype）、action（处置，如 mirror、disposition deny/drop）、rule（条件+动作绑定，含优先级 precedence 与 log 开关）。配置后必须 qos apply 才生效并写 flash；qos revert/flush/reset 分别回退未应用配置/清待定/恢复默认。排障用途：计数（show active policy rule 的 Matches/Packets/Bytes）与日志（show qos log）定位丢包；镜像（policy action mirror）。限制：仅 ingress 方向。
  tags: [qos, policy, condition, action, rule]

- id: g32
  title: Port Monitoring / Mirroring（端口监控与镜像）
  type: term
  source_chapter: "p216"
  source_quote: |
    "6860_A-> port-monitoring 1 source port 1/1/1 capture-type full enable file /flash/capture.cap
    ... no port-monitoring 1"
  summary: |
    把端口流量复制到抓包文件或镜像口：port-monitoring <会话> source port <口> capture-type full enable file /flash/capture.cap（full 支持大帧完整截取），FTP 取回 pcap 分析，no port-monitoring 停止。变体：基于端口的镜像（ingress/egress/双向，policy action mirror 策略镜像同时仅 1 会话）与 RPM 远程镜像（专用 VLAN 跨网传输）。约束：端口镜像与端口监控不能同端口；六类控制流量不镜像。
  tags: [port-monitoring, mirroring, capture, rpm]

- id: g33
  title: PMD 文件（崩溃转储）
  type: term
  source_chapter: "p383"
  source_quote: |
    "swlogd PMD main ALRT: PMD generated at /flash/pmd/pmd-etherCmm-11.04.2022-14.54.53"
  summary: |
    交换机软件崩溃时生成的转储文件，落 /flash/pmd/ 目录，日志报 "PMD generated at ..."。处置路径：OVNA 识别该异常后建议收集日志与 PMD 文件并联系 ALE 客户支持（LAB5 用例2）。是软件类故障升级 TAC 的关键证据。
  tags: [pmd, core-dump, crash, tac]

- id: g34
  title: OVNA（OmniVista Network Advisor，网络顾问）
  type: term
  source_chapter: "p316"
  source_quote: |
    "Detect anomalies on OmniSwitch, Stellar AP, Third-Party devices ... And propose remediations ... Real-time alerts with remediations, Rainbow or Teams bot ... Automatic logs collection"
  summary: |
    ALE 边缘计算（on-prem Linux 服务器）AI 运维应用：设备 syslog 模式匹配检测异常（预置几十类：环路/端口 flap/DDoS/风暴/OSPF/BGP 状态变化/电源 POE 故障/IP 重复/高 CPU 等，p321）、实时告警到 Rainbow 气泡或 Teams 频道并附修复建议、可一键执行处置（禁端口/收集日志/确认）、异常历史与报表。纳管版本门槛：AOS 8.7.R2+（OS6xxx/9xxx）。许可按设备 IP 计费（NETAD-*-1Y/3Y/5Y）。
  tags: [ovna, network-advisor, anomaly, remediation]

- id: g35
  title: Rainbow Bubble（Rainbow 气泡通知）
  type: term
  source_chapter: "p334"
  source_quote: |
    "RAINBOW BUBBLE MANAGEMENT: Primary Rainbow Bubble, Custom Rainbow Bubbles ... Anomalies association, Devices association, Scheduler"
  summary: |
    OVNA 的告警投递渠道之一（ALE Rainbow 协作平台的会话"气泡"）。分主气泡与自定义气泡：自定义气泡可绑定异常类别、设备集合与调度计划，实现分团队分域告警路由。通知内容含设备 IP/主机名、MAC、端口与修复动作选项（Disable Port/Collect Logs/Acknowledge），用户在气泡内直接决策（LAB5 用例1）。
  tags: [rainbow, bubble, notification, alerting]

- id: g36
  title: Anomaly / Anomaly History（OVNA 异常与异常历史）
  type: term
  source_chapter: "p320"
  source_quote: |
    "View the list of anomalies that Network Advisor is monitoring. Edit anomaly information. Create a custom anomaly. ... Display a history of detected anomalies that Customer can analyze to detect patterns of network behavior"
  summary: |
    OVNA 的核心对象：异常（anomaly）是匹配到某日志模式的检测事件，可编辑、可自建自定义异常、可删除自定义项；Anomaly Monitoring 看当前监控列表，Anomaly History 看历史检测记录（用于行为模式分析），Anomaly Report 生成报告送邮件或气泡。异常带 severity/remediation/版本等属性（p328 界面）。
  tags: [anomaly, anomaly-history, ovna]

- id: g37
  title: DDM（Digital Diagnostics Monitoring，光模块数字诊断）
  type: term
  source_chapter: "p333"
  source_quote: |
    "Each time a new device of type Switch is added, the application will push the following commands to the switch:
    -> swlog output socket <ip_address> 10514 vrf-name <vrf>
    -> interfaces ddm enable ... -> interfaces ddm-trap enable"
  summary: |
    光模块数字诊断监控（温度/光功率/电压等）。OVNA 纳管交换机时自动下发 interfaces ddm enable 与 interfaces ddm-trap enable，配合 syslog 上报实现光模块级异常（如 SFP Port Threshold Violation 异常，p321）的主动监测。show transceivers 看模块厂商/序列号/状态。
  tags: [ddm, transceiver, sfp, monitoring]

- id: g38
  title: ECMP（等价多路径）
  type: term
  source_chapter: "p142"
  source_quote: |
    "sw1 (6900-A) -> sh ip routes ... + = Equal cost multipath routes ... 192.168.30.0/24 +172.16.12.2 ... +172.16.17.7 ... OSPF"
  summary: |
    等价多路径路由：同前缀同代价多条路由并存负载分担（show ip routes 中 + 标记）。LAB4 中 192.168.30.0/24 与 192.168.254.8/32 从双路径退化为单路径即 OSPF 邻居故障的可视信号。设计语境（p547）：L3 冗余手段之一（与 VRRP、动态路由协议并列），提供备份路径+负载均衡。
  tags: [ecmp, routing, load-balancing]

- id: g39
  title: DHCP Relay / UDP Relay（DHCP 中继）
  type: term
  source_chapter: "p219"
  source_quote: |
    "show configuration snapshot ip-dhcp-relay ... show ip dhcp relay statistics ... show ip udp relay ... debug ip packet protocol udp start timeout 60"
  summary: |
    跨网段 DHCP：中继把客户端广播（UDP 67/68）转单播发往服务器（UDP 67/67）。配置 ip dhcp relay destination <服务器IP>（配错地址则 Tx Server=0，LAB3 根因）。统计按"从客户端收/转发延迟违规/最大跳数违规/Agent Info 违规/无效网关 IP/发往各服务器"分桶计数。Option 82/DHCP Snooping 与 IP Anti-Spoofing、Dynamic ARP Inspection 构成接入侧 DHCP 安全组（p469）。
  tags: [dhcp-relay, udp-relay, option82]

- id: g40
  title: DoS 防护统计（ipni dos / show ip dos statistics）
  type: term
  source_chapter: "p200"
  source_quote: |
    "sw8 (6860-B) -> show ip dos statistics ... port scan 0, ping of death 0, land 0 ... invalid-ip 265312529 ...
    +++ VRF 0: DoS type invalid ip from 192.168.30.8/00:00:5e:00:01:02 ... to 224.0.0.18"
  summary: |
    AOS 内置 DoS 检测（硬件早丢弃+L2 风暴控制属控制面保护，p552）：统计分 port scan/ping of death/land/loopback-src/invalid-ip/invalid-multicast/unicast dest-ip multicast-mac/ping overload/arp flood/arp poison/anti-spoof/gratuitous-arp/ip-options-filter。日志形态 "ipni dos WARN: DoS type <类型> from <IP/MAC> on port <口>"。判读警示：invalid-ip 天文数字+源为 VRRP 虚拟 MAC（00:00:5e）指向 L2 环路回灌而非攻击（LAB2/ce19）。
  tags: [dos, security, statistics, false-positive]

- id: g41
  title: SPB（最短路径桥接，802.1aq）
  type: term
  source_chapter: "p492"
  source_quote: |
    "ENTERPRISE SPB LAN CORE ... No STP ... Service Virtualization (ISID) for departmental isolation ... VXLAN support for DCI"
  summary: |
    基于 IS-IS 的最短路径桥接（SPB-M）：所有链路全 UP 无 STP 阻塞、ISID 服务虚拟化实现部门隔离/多租户、VLAN 跨园区扩展、L3 间部门可 VPN-lite/L3-VPN、VXLAN 支持 DCI。设计对比（p546）：与 VC/STP/LACP/DHL/ERP 并列的 L2 冗余方案，强在 100% 带宽+可扩展+流量隔离，弱在无统一管理。支持机型 OS6860N/6870/6900/9900。
  tags: [spb, is-is, isid, fabric]

- id: g42
  title: ERPv2（以太网环保护，G.8032）
  type: term
  source_chapter: "p542"
  source_quote: |
    "Supports a maximum of 64 ERP rings ... Major Ring: Controls a full physical ring ... Sub-Ring: Connects to a Major Ring at the Interconnection Nodes ... RPL"
  summary: |
    ITU G.8032 以太网环保护切换：主环（Major Ring，闭合物理环，自有 ERP 实例与 RPL 阻塞点）+ 子环（Sub-Ring，经互连节点挂在主环上、非闭合）；R-APS 控制信道可选虚拟通道；支持回切（Revertive）与不回切（Non-Revertive）模式；单机最多 64 环。园区多楼宇环形骨干的冗余方案（p489 用例：10/40G 分布式环网）。
  tags: [erp, erpv2, g8032, ring-protection]
