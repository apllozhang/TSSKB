# frameworks.md · OmniSwitch LAN Troubleshooting (DT00XTE221EN) 框架/流程候选条目

- id: f01
  title: 结构化排障总流程（报告→收集症状→隔离→纠正→验证→记录）
  type: framework
  source_chapter: "p51"
  source_quote: |
    "Flow chart of a structured troubleshooting approach
    Gather symptom -> Isolate the problem -> Implement Corrective action -> Problem Fixed ?
    ... Document the solution and save the change"
  summary: |
    全书排障主方法论流程图：1) 问题报告；2) 收集症状；3) 隔离问题；4) 实施纠正动作；5) 验证是否修复——未修复或引发新问题则回退/换方案重试；6) 修复后记录解决方案并保存变更。配套的完整流程步骤（p52）为 Identify→Re-Create→Isolate→Locate→Solve→Verify→Document：先提问收集信息确认问题存在并可复现，不可复现则回到第一步继续追问；用 OSI 模型定位层级、设备与物理位置；制定并实施变更计划（驱动/配置/设计）；充分测试验证；最后记录原始问题、过程、诊断与解决方案并跟进相关人。
  tags: [troubleshooting, methodology, workflow]

- id: f02
  title: OSI 分层排障六种切入方法
  type: framework
  source_chapter: "p57"
  source_quote: |
    "Three different approaches use OSI as a troubleshooting framework: Bottom-Up, Top-Down, Divide and Conquer
    ... Three other approaches: Follow the path, Spot the differences, Move the problem"
  summary: |
    六种排障切入方法。基于 OSI 的三种：自底向上（物理层往上逐层查，适合硬件/线缆类问题但耗时长）、自顶向下（应用层往下，适合软件导向问题）、二分法（从中间层开始按症状定位方向，适合复杂/新问题）。另外三种：跟踪路径（沿数据包从源到目的的实际转发路径查）、找差异（对比正常设备/进程与异常设备/进程的配置差异）、移动问题（把组件物理换位，观察问题是否跟着组件走）。方法选择依据（p58）：先判断问题类型和分析症状，结合既往经验——老问题直接套经验，新问题按硬件/线缆/软件导向选层。
  tags: [troubleshooting, osi-model, methodology]

- id: f03
  title: OSI 各层故障症状-原因对照表
  type: framework
  source_chapter: "p61"
  source_quote: |
    "Physical layer Symptoms: Performance lower than baseline, Loss of connectivity... Causes: Power-related, Hardware Faults, Cabling faults, Attenuation/Noise, Interface configuration, Exceeding design limits"
  summary: |
    按层建立"症状→可能原因"索引，用于快速定位故障域。物理层（p61）：性能低于基线/断连/瓶颈/高 CPU/控制台报错 ← 电源、硬件、布线、衰减噪声、接口配置、超设计极限。数据链路层（p62）：网络层及以上无功能/低于基线/过量广播 ← 地址映射错误、成帧错误、STP 失败或环路、接口配置不当、ARP 缓存问题、速率双工不匹配。网络层（p63）← 路由表/邻居/拓扑库、IP 地址错误或重复、路由协议错误、ICMP 过滤。传输层（p64）← 重传、分片、端口、ACL、NAT。会话/表示/应用层（p65）← DNS/NetBIOS 解析、高层协议（HTTP/SMTP/FTP）故障。
  tags: [troubleshooting, osi-model, symptoms]

- id: f04
  title: 启动序列排障与密码恢复/USB 恢复流程
  type: framework
  source_chapter: "p76"
  source_quote: |
    "Step1. Power cycle the switch ... Break the boot sequence ... 'Hit any key to stop autoboot:'
    => setAdminPasswordDefault ... => boot (6900) / => reset (6860)"
  summary: |
    启动类故障处置流程。密码恢复（U-Boot 型号）：断电重启→在 "Hit any key to stop autoboot:" 处打断→setAdminPasswordDefault→重启（6900 用 boot，6860 用 reset 或等 90 秒自动进 CLI）。密码恢复（ONIE 型号 OS6860N/6900，仅能从 console 做，p78-79）：重启选 ONIE→DIAG 模式→blkid 找分区→cd /mnt/ssd5/system→rm userTable8 删除本地用户库→reboot→再 modify running working 切目录后从 certified 重启（p80）。USB 恢复 CMM（p83-85）：Trescue.img 放 U 盘根目录、交换机目录结构放 U 盘→打断启动→run rescue（重格闪存，约 10 分钟）→验证 certified/working 微码。ONIE USB 恢复（p87-90）：blkid→mount /dev/sda1→cp 镜像到 /var/tmp→onie-nos-install。改启动目录（p92）：u-boot 下 setenv bootfile working/Uos.img→saveenv→run bootcmd。
  tags: [boot-sequence, password-recovery, usb-recovery, uboot, onie]

- id: f05
  title: 交换系统硬件排障命令链（system→chassis→module→health→环境）
  type: framework
  source_chapter: "p97"
  source_quote: |
    "sw1 (6900-A) -> show system ... Up Time: 1 days 3 hours ...
    -> show chassis / show cmm / show running-directory / show microcode
    -> show module status / show hardware-info / show health / show temperature"
  summary: |
    系统层排障自上而下的命令链：show system（版本/uptime/系统时间，时间可用于对齐日志）→ show chassis / show cmm（序列号、硬件版本、CMM 状态）→ show running-directory + show microcode [loaded|certified]（核对运行目录与微码版本）→ show module status / show module long（CMM 与 NI 一致性；operational DOWN 但 POWER ON 指向软件问题）→ show hardware-info（CPU/闪存/RAM/FPGA/U-Boot 版本，与 release note 比对）→ show health（CPU/内存水位）→ show transceivers / show powersupply / show fan / show temperature（光模块、电源、风扇、温度双阈值）→ 面板 LED 判读（OK/PS 灯状态表，p107-108）。
  tags: [switch-system, hardware, show-commands, health-check]

- id: f06
  title: 高 CPU 排障流程（show health → 维护 shell top/ps）
  type: framework
  source_chapter: "p110"
  source_quote: |
    "The most common causes for high CPU utilization: An abnormal process... A process is doing extensive calculations... AOS is under a DoS attack. Too many frames or packets are trapped to CPU
    Use the commands 'top' and 'ps' in the maintenance shell"
  summary: |
    高 CPU 排障流程：1) show health / show health all cpu 确认水位与 1 分钟/1 小时/1 天趋势；2) 若超阈值，尝试隔离到具体 NI 或端口（show health slot/port）；3) su 进维护 shell，用 top（N/M/P/T 键分别按 pid/内存/CPU/时间排序，-b 批处理，-d 间隔）和 ps -T 定位吃 CPU 的进程/线程；4) 结合网络知识判断该消耗是否异常（异常进程死循环=软件问题、网络未按规模设计、DoS 攻击、大量日志/MAC 学习/上 CPU 的环流量）；5) 找到可疑进程后联系 ALE 技术支持获取处置流程，不要自行处理。
  tags: [cpu, maintenance-shell, top, ps, dos]

- id: f07
  title: 二层连通性排障三层走法（物理→配置→ARP）
  type: framework
  source_chapter: "p118"
  source_quote: |
    "Issues that could cause the communication to fail: Physical problems (Bad, missing, or miswired cables, Bad ports...) Misconfiguration (Missing or wrong VLANs, Native VLAN mismatch, VLANs not allowed on linkagg...) ARP problems"
  summary: |
    二层排障按三类故障源展开。物理问题（p120-121）：沿数据路径检查 LED；对每端口 show interfaces 查 operational status、速率双工是否与对端匹配、多次采样 Error Frames/CRC/Alignment 是否增长（增长→查线缆与网卡）、全双工下 Collision 增长→查对端双工配置、ping 时 Bytes Received 是否增长（不增→查网卡）。配置错误（p123-124）：客户端侧 ipconfig /all、ping/tracert、arp -a、nslookup、route print；交换机侧 show configuration snapshot all 核 VLAN 创建/端口 VLAN 归属/ACL，show vlan member 核端口类型（default/qtagged）与 STP 状态。ARP 问题（p126-129）：按 MAC 学习→网关指向→ARP 解析→debug ip packet 抓 ARP 收发五步走。
  tags: [layer2, connectivity, arp, vlan, physical]

- id: f08
  title: STP 桥接环路排障八步清单
  type: framework
  source_chapter: "p173"
  source_quote: |
    "Example of checklist recapitulating some of the actions available to troubleshoot stp
    1. Retrieve general information about network topology ... 2. Turn on events to monitor the network"
  summary: |
    环路排障清单：1) 取回网络拓扑信息（逻辑 VLAN/广播域 + 物理互连端口号）；2) 打开事件监控——swlog 提升到 debug2（portMgrCmm/intfCmm/VlanMgrCmm/portMgrNi/VlanMgrNi），加大 flash 文件尺寸 swlog output flash-file-size 12500；3) 核查 MAC 地址是否反复 flush/重学；4) 收集 STP 配置细节——所有设备同一 STP 模式（1x1/FLAT/MSTP）、根桥与备份根位置、非默认 cost/priority、阻塞端口位置（show spantree / show spantree vlan）；5) 核对定时器/根 ID/根端口（timers 必须跨链路一致；Topology Changes 快速递增=设备无法就根桥达成一致，可能因 BPDU 丢弃）；6) 判读端口状态——本应阻塞的端口转为转发，两大原因：原先转发的链路物理故障、根的 BPDU 被丢（按普通丢包排查）；7) MAC flapping 定位（show mac-learning mac-address 看是否在两端口间跳动；show interfaces | grep Number / Last 找 flap 端口；debug stp bpdu-stats 统计 BPDU 收发）；8) MSTP 专项——region 名一致、MSTI 内 VLAN 全部 tagged、同 region 配置完全相同。应急止血（p172）：优先禁用"本应阻塞"的端口。
  tags: [stp, bridging-loop, mac-flapping, checklist]

- id: f09
  title: Virtual Chassis 排障流程（拓扑→一致性→vcsetup.cfg→NOK 码）
  type: framework
  source_chapter: "p162"
  source_quote: |
    "-> show virtual-chassis topology ... -> show virtual-chassis consistency ... -> cat vcsetup.cfg ... -> debug show virtual-chassis status"
  summary: |
    VC 排障四层递进：1) show virtual-chassis topology——各机箱角色（Master/Slave）、运行状态、Chassis ID/Priority/Group；2) show virtual-chassis consistency——核对带星号（必一致）参数：Chassis Type、Chas ID、Group、Hello Interval、Control Vlan、License；3) 逐台 cat vcsetup.cfg 比对（chassis-id、vf-link-mode、member-port、chassis-group、EMP 地址）；4) debug show virtual-chassis status——按 L0-L8 层级看哪层失败（VFL Ports Configured→VFL Intf Oper Status→VFL LACP→VCM Synchronization），对照 NOK_08/09/14/17 错误码说明定位；5) 辅以 show virtual-chassis vf-link 看 VFL 主备端口/状态，debug show virtual-chassis connection 看 IPC 内部连接；6) 检查 /flash 下 vcsetup.cfg.*.err 错误文件（记录了启动时配置解析失败的行号与原因）。
  tags: [virtual-chassis, vc, vfl, nok-code]

- id: f10
  title: L3/IP 连接问题排障决策树（本机→交换机→服务器）
  type: framework
  source_chapter: "p209"
  source_quote: |
    "Basic IP troubleshooting Methodology: Local host configuration OK? -> Switch configuration OK? -> Server configuration OK? -> Can you connect using IP addresses?"
  summary: |
    隔离本地主机与远程主机间连接问题的决策树：1) 先修本机 TCP/IP 配置、地址解析（ARP/DNS 或其他 Windows 网络服务）问题；2) 本机配置 OK 仍不通→修交换机接口配置/ACL 问题；3) 再修 IP 地址、子网划分、默认网关路由表或 ARP 缓存问题（含 DHCP 设置与目标地址）；4) 都 OK→核服务器配置；5) 最终验证能否用 IP 地址直连。配套命令族（p208）：show ip traffic/interface/routes/route-pref/redist/access-list/route-map/router database/protocols/router-id/service，配合 ping 与 traceroute。IP 网络问题九大类原因（p207）：本地连通性、配置、DHCP/BOOTP、物理层、IP 重复、首跳 L3、路径中 L3 连通、名称解析、路由环路/协议问题、资源（内存缓冲 CPU）、包过滤防火墙、MTU 不匹配。
  tags: [layer3, ip, decision-tree, ping, traceroute]

- id: f11
  title: 丢包排障双工具流程（QoS 策略计数 + 端口抓包）
  type: framework
  source_chapter: "p214"
  source_quote: |
    "On switch A, applying policies that will 'count' icmp request from laptop 192.168.8.10
    policy condition cond1 source ip 192.168.8.10 icmptype 8
    policy rule rule1 condition cond1 action action1 log"
  summary: |
    定位丢包点的两步法。第一步：沿路径在交换机上部署"计数策略"——policy condition（按 source ip + icmptype 8 请求 / icmptype 0 回复分别匹配）→ policy action → policy rule 加 log → qos apply；用 show active policy rule 看 Packets/Bytes 计数、show qos log 看命中明细，对比两端计数找出丢包段。第二步：QoS 策略只作用于入向流量（p216），要看出向 ICMP 或大包（1000 字节 ping）时用端口抓包：port-monitoring 1 source port 1/1/1 capture-type full enable file /flash/capture.cap→FTP 取回 pcap 用 Wireshark 分析→no port-monitoring 1 停止，再对照 QoS 计数与抓包结果定位丢包位置。
  tags: [packet-loss, qos, policy, port-monitoring, capture]

- id: f12
  title: OSPF 邻居/路由排障流程（状态机→接口参数→debug 日志）
  type: framework
  source_chapter: "p246"
  source_quote: |
    "Example : SW1 & SW2 are not in FULL state! Modify the log level to have the maximum verbosity
    SW1 -> swlog appid ospf_0 subapp all level debug3 ... Check the Hello Interval on both switches"
  summary: |
    OSPF 排障流程：1) show ip ospf neighbor 看 Full/2-Way/Init 状态与邻居是否存在；2) show ip ospf interface 核对关键参数——Hello/Dead Interval、认证类型与密钥、Area ID、MTU、子网掩码、DR/BDR；3) 两台都开 swlog appid ospf_0 subapp all level debug3 拿最大详细度日志；4) show log swlog | grep ospf_0 读具体丢弃原因（invalid helloInterval / authentication failure / oversized LSA / neighbor state change）；5) 对症修复（对齐 timer 或密码）后验证邻居 Full、show ip ospf routes / show ip routes 路由回来；6) 排查完把日志级别改回 info。典型错误条件（p238）：Hello/Dead timer 不匹配、认证密码/类型/密钥不匹配、区域不匹配、Area 类型或 ID 不匹配、接口子网掩码不同。邻居状态机参考（p239）：Down→Init→2-Way（选 DR/BDR）→Exstart→Exchange（DBD）→Loading（LSR/LSU/LSAck）→Full。
  tags: [ospf, neighbor, adjacency, swlog, debug]

- id: f13
  title: 组播排障流程（L2 IPMS→DVMRP→PIM 分层 debug）
  type: framework
  source_chapter: "p257"
  source_quote: |
    "->show ip multicast ... -> show ip multicast group ... -> show ip multicast forward
    ... swlog appid dvmrp_0 subapp ipmrm level ... swlog appid pim_0 subapp hello level"
  summary: |
    组播不通的分层排查：1) L2/IPMS 层——show ip multicast 看 Querier/Proxying/Zapping 全局开关、show ip multicast group 看组注册成员、show ip multicast forward/source 看转发表与源表、debug ip packet show-multicast on board ni <#> 看 IGMP 查询报文收发；2) 设计规则核查（p258）：全网应只有 1 个 querier、querier-forwarding 只在源与 querier 之间的交换机上启用、zapping 只在边缘设备启用、IGMP 报文 TTL 必须为 1；3) DVMRP 层——show ip dvmrp [neighbor/route/prune/interface/nexthop]，debug 用 swlog appid dvmrp_0 subapp routes|ipmrm level debug3 看转发向量与 DF 选举；4) PIM 层——show ip pim [neighbor/candidate-rp/interface/group-map/sgroute/notifications]，debug 按 subapp 细分：hello（邻居建立）、boot-strap（BSR 选举）、crp（在 BSR 上看 C-RP 通告）、sm-join-prune（JOIN/PRUNE 与 RP）。
  tags: [multicast, igmp, dvmrp, pim, ipms]

- id: f14
  title: VRRP 排障流程（状态→统计→配置三角核对）
  type: framework
  source_chapter: "p251"
  source_quote: |
    "->show ip vrrp 1 ... Priority = 100 ... Virtual MAC = 00-00-5E-00-01-01
    -> show ip vrrp statistics ... VRID VLAN State UpTime Become Master Adv. Rcvd"
  summary: |
    VRRP 排障三角：1) show ip vrrp——核对 Admin Status（Enabled？）、VRID/接口/虚拟 IP 地址是否两台一致、Priority、Preempt、通告间隔；2) show ip vrrp statistics——看三错误计数（Checksum/Version/VRID Errors，VRID Errors 涨说明收到不匹配的 VRRP 报文，通常是虚拟 IP 配错）与各 VRID 状态（Master/Backup/Initialize，Initialize 常意味着接口 down 或未 enable）、Become Master 次数、Adv. Rcvd 计数；3) show configuration snapshot vrrp 逐行比对两台配置。机制参考（p250）：Master 用虚拟 MAC 应答主机 ARP；Skew_Time=(256-Priority)/256；Master_Down_Interval=3×AdvInterval+Skew_Time；通告间隔必须全网同 VRID 一致。深挖时 swlog appid vrrp_0 subapp all level debug3 看通告发送。
  tags: [vrrp, gateway-redundancy, statistics]

- id: f15
  title: Network Advisor（OVNA）安装部署三步流程
  type: framework
  source_chapter: "p346"
  source_quote: |
    "Step by Steps: Step 1 - System Requirements ... Step 2 - Package Installation ... Step 3 - OVNA Configuration
    $ sudo dpkg -i ale-ovna.deb ... $ sudo ale-ovna install"
  summary: |
    OVNA 部署三步：1) 系统要求——四核 CPU/8GB RAM/50GB 盘（200 台内；1000 台 120GB、2000 台 210GB）、Ubuntu 22.04 或 Debian 11/12 或 RHEL 9.3、端口 TCP 80/443（WebUI）、UDP/TCP 10514 与 TCP 6514 TLS（syslog）、TCP 22（SSH）、必须可上外网；2) 包安装——Debian 系 sudo dpkg -i ale-ovna.deb，RHEL 系 sudo rpm -ivh ale-ovna.rpm（RHEL 需先 systemctl disable firewalld --now 以便 k3s 文件安装），再 sudo ale-ovna install（交互选 IP、是否代理、是否 syslog over TLS）；3) Web 配置——浏览器开 https://<IP> 选 New to OVNA/Start Setup：公司与管理员信息→2FA→时区→通知渠道（Rainbow Bubble 或 Teams 频道 + SMTP）→OmniVista 同步（可关）→许可（30 天试用）→Submit。升级用 ale-ovna update（跨版本先装新包）；同主版本小升级加 -c；迁移=备份→新机安装→导入备份→补配置→导许可（p360-368）。
  tags: [ovna, network-advisor, installation, deployment]

- id: f16
  title: OVNA 纳管设备与告警处置流程（LAB5 工作流）
  type: framework
  source_chapter: "p333"
  source_quote: |
    "Each time a new device of type Switch is added, the application will push the following commands to the switch:
    -> swlog output socket <ip_address> 10514 vrf-name <vrf>
    -> interfaces ddm enable ... -> interfaces ddm-trap enable"
  summary: |
    纳管与处置闭环：1) Device Management→Add device（主机名/IP/类型/SSH 端口/登录凭据/Category）；OVNA 自动向交换机推送 syslog 指向 10514、DDM 与 DDM trap 使能三条命令，show swlog 应出现 Log Device 2；2) 多 IP 设备建议用 ip service source-ip loopback0 swlog 固定 syslog 源地址；3) 设备 syslog→OVNA 模式匹配命中→脚本执行（必要时 SSH 到设备取更多信息）→通知（Rainbow/Teams）带修复建议→用户在气泡/频道里选择处置动作（如 Disable Port、Collect Logs、Acknowledge）→OVNA 通过 SSH 脚本执行→结果日志回传→Anomaly History 留档；4) 验证处置：交换机 show log swlog | grep <端口> 能看到 CLI 下发记录与链路 down 事件，show interfaces status 确认端口已禁用。
  tags: [ovna, anomaly, remediation, syslog, device-management]

- id: f17
  title: Microsoft Teams Bot 对接 OVNA 四阶段流程
  type: framework
  source_chapter: "p406"
  source_quote: |
    "Phase 1 of 4: Creating the Entra App and Teams Bot ... Phase 2 of 4: Creating the Teams App
    Phase 3 of 4: Get your IDs ... Phase 4 of 4: Enable Graph API authorizations"
  summary: |
    Teams 集成四阶段（须在装 OVNA 前完成，产出的 ID 在 OVNA 安装向导中要用）：阶段 1 建 Entra 应用与 Bot——dev.teams.microsoft.com→Tools→Bot Management→New bot→命名（此名同时是 Entra 应用名与 Teams 显示名）→填公网可达的 bot endpoint（https://.../msteams，默认端口 10510）→建 Client secret（值只显示一次必须立即保存）→记录 Bot ID；阶段 2 建 Teams 应用——Apps→New App→填 Basic information（描述/开发者/URL/Application ID=Bot ID）→App Features 挂 Bot（勾 Personal+Team scope）→Publish→Download the app package（ZIP）→本地部署（频道 +→Manage your Apps→Upload an app）或组织级发布；阶段 3 取 ID——entra.microsoft.com→App registrations→Overview 记 Application (client) ID 与 Directory (tenant) ID；阶段 4 加 Graph API 权限（Team.ReadBasic.All、Channel.Create、Group.ReadWrite.All 等十条）并 Grant admin consent。
  tags: [teams-bot, ovna, entra, integration]
