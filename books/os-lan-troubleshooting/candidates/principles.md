# principles.md · OmniSwitch LAN Troubleshooting (DT00XTE221EN) 原则/参数候选条目

- id: p01
  title: 排障文档先行：拓扑图/清单/基线是排障的前提
  type: principle
  source_chapter: "p53"
  source_quote: |
    "Documentation is critical to being able to troubleshoot a network: Logical topology diagram, Inventory, Design documents, IP Addresses, Physical topology diagram, Interconnections, Configuration management, Blue print, Baseline performance levels"
  summary: |
    能否高效排障取决于手头有没有九类文档：逻辑拓扑图、设备清单、设计文档、IP 地址表、物理拓扑图、互连关系（哪台设备的哪个口连对端哪个口）、配置管理、蓝图、性能基线。排障前先确认"对网络完整、准确、最新的视图"存在；没有就先用命令重建（LAB1 即要求用 show lldp remote-system、show vlan members、show linkagg port 等画出物理/逻辑拓扑）。
  tags: [documentation, topology, baseline]

- id: p02
  title: 给 ALE 技术支持开案的最小信息与严重级别
  type: principle
  source_chapter: "p54"
  source_quote: |
    "ALE Technical Support: Service & Support Organization and Processes, including the Escalation Procedure as well as the Minimum Information Required to open a new eService Request"
  summary: |
    升级到厂商前必须备齐：eService Request 开案所需最小信息、Case Severity 定义、请求状态查询路径、开案必须提供的内容、升级（escalate）流程。LAB1 前置练习即要求在 TKC 检索 "Minimum Information Needed to open a Data case issue" 一文。原则：一线先查 TKC/自带文档，开案时信息齐全可直接缩短处理周期。
  tags: [support, eservice, escalation, tkc]

- id: p03
  title: TKC 用例结构与自然语言检索
  type: principle
  source_chapter: "p31"
  source_quote: |
    "Case Description: Topology, Scenario, Environment, Diagnosis ... Resolution: Configuration, Hot Fix, Firmware upgrade ...
    In the search box, you can use natural language to write your search."
  summary: |
    TKC（Technical Knowledge Center，经 Partner Portal/My Portal 进入）是技术支持写的用例库。每篇用例固定结构：Case Description（拓扑/场景/环境/诊断）+ Resolution（配置/热补丁/固件升级）。检索时可直接用自然语言描述现象；过滤器支持 Research、Solution、Dates、Article type 四类。排障第一步先查是否已有现成解法（LAB1 的 Problem N1/N2 就是示例）。
  tags: [tkc, knowledge-base, search]

- id: p04
  title: show system 输出判读要点（版本/uptime/时间）
  type: principle
  source_chapter: "p97"
  source_quote: |
    "Up Time: 1 days 3 hours 51 minutes ... The amount of time the switch has been running since the last system reboot. The current system date and time. Useful to analyse log and command log"
  summary: |
    show system 三大判读点：当前软件版本（对照已知问题库）、Up Time（距上次重启的时长——短 uptime 意味着刚发生过重启，是重要线索）、Date & Time（与日志/命令日志时间戳对齐的前提，不对可用 system date/system time 修正，NTP 环境用 ntp client admin-state enable + system timezone，见 p372）。
  tags: [show-system, uptime, ntp]

- id: p05
  title: operational status DOWN 但 POWER ON 指向软件问题
  type: principle
  source_chapter: "p100"
  source_quote: |
    "Chassis are up and operational. The operational status can be DOWN while the power status is ON, indicating a possible software issue
    -> show module status ... -> show module long"
  summary: |
    show module status 判读原则：CMM 与 NI 之间任何不一致都会引发问题；电源状态 POWER ON 而运行状态 DOWN，说明上电正常但软件没起来——优先怀疑软件/微码而非硬件。show module long 可看模块详细信息作进一步比对。同类思路适用于 show chassis 的 Admin Status=POWER ON + Operational Status 判读。
  tags: [module-status, hardware, software-issue]

- id: p06
  title: 硬件信息对照 release note：U-Boot/FPGA 有最低版本门槛
  type: principle
  source_chapter: "p102"
  source_quote: |
    "Analyse requirements on the release note and compare to hardware-info result ... Upgrade uboot and/or FGPA if mandatory
    -> update uboot cmm all file /flash/u-boot.8.9.R04.70.tar.gz
    -> update fpga-cpld cmm all file fpga_kit_8757
    Note: AOS must be upgraded prior to performing an FPGA/CPLD or U-boot upgrade."
  summary: |
    show hardware-info 输出的 U-Boot、FPGA/CPLD 版本要与目标 AOS 版本的 release note 比对：release note 列出内存要求、UBoot 和 FPGA 最低版本要求、升级说明。命中门槛才升级（update uboot / update fpga-cpld）。顺序铁律：先升 AOS，再做 FPGA/CPLD 或 U-Boot 升级，顺序颠倒会出问题。
  tags: [hardware-info, release-note, uboot, fpga, upgrade-order]

- id: p07
  title: show health CPU 水位与高 CPU 四大根因
  type: principle
  source_chapter: "p103"
  source_quote: |
    "High CPU utilizations may cause: Software issue, network is not well scaled, Virus/attack, Too many messages.
    • Extensive logging • MAC learning • Too many frames or packets are trapped to CPU (Loop –routing or bridging)
    -> show health -> show health all cpu -> show health slot <chassis/slot> -> show health port <chassis/slot/port>"
  summary: |
    show health 给出当前/1 分钟/1 小时/1 天均值四个维度，可下钻到 slot 与 port。若各项都未超阈值但整体高，则继续隔离到具体 NI 或端口。高 CPU 四大根因：异常进程（死循环=软件缺陷；大量计算=网络规模设计不当）、DoS 攻击、子系统间消息过多（大量日志、MAC 学习、总线故障、硬件中断）、过多报文上 CPU（路由/桥接环路）。定位到具体进程后转 f06 流程并联系 TAC。
  tags: [cpu, show-health, root-cause]

- id: p08
  title: 温度保护双阈值：Warning 发 trap，Danger 关模块
  type: principle
  source_chapter: "p105"
  source_quote: |
    "Two thresholds: Warning (CMM sends out a trap), Danger (All (NI) modules are shut down, requires a manual boot)
    -> show temperature ... 1/CMMA 38 15 to 67 77 67 UNDER THRESHOLD"
  summary: |
    工作温度是交换机整体可用性的关键因素。show temperature 显示当前值、正常范围、Danger 阈值与状态；两个阈值两级行为：到 Warning 阈值 CMM 发 trap 告警；到 Danger 阈值所有 NI 模块关断且需要手动重启恢复。预防原则：遵守机箱气流建议（见各型号 Hardware Users Guide），风扇/电源气流方向不匹配会触发告警（LED 表现见 p107）。
  tags: [temperature, thermal, trap, fan]

- id: p09
  title: 面板 LED 判读速查（OK/PS/三色灯）
  type: principle
  source_chapter: "p107"
  source_quote: |
    "OK LED: SOLID GRN Operational... BLINK GRN This switch is functioning as the master chassis within a VC. Solid Amber: System Diagnostics and/or AOS bootup failed
    PS LED: SOLID GRN Both power supplies are functional. Solid Amber: One power supply is functional"
  summary: |
    启动过程 LED 闪烁变色是各阶段信号，最终应稳定。OK 灯：常绿=正常（VC 中为 slave 模式运行）；闪绿=本机是 VC master；常琥珀=系统诊断或 AOS 启动失败；闪琥珀=过渡态（诊断或启动中）。PS 灯：常绿=双电源正常；常琥珀=单电源；灭=无电源。OK 与 PS 同时闪琥珀=缺风扇盘或电源与风扇盘气流方向不匹配。9900 CMM 另有 PRI/FAB/TEMP 等灯（p108）：如 FAB 常绿=所有 fabric OK、TEMP 闪琥珀=至少一个风扇故障、常红（硬件 FAIL）需换件。
  tags: [led, hardware, status-indicator]

- id: p10
  title: show interfaces 端口级判读（错误计数器与双工）
  type: principle
  source_chapter: "p121"
  source_quote: |
    "operational status up ? ... Speed and duplex match the other side ? Check several times Error Frames, CRC Error Frames, Alignment Errors ... Collision Frames incrementing ? If full duplex -> verify the duplex setting on the other side. Check the Bytes Received is incrementing when end stations try to ping each other."
  summary: |
    沿数据路径逐端口判读 show interfaces：operational down→查物理链路、NI、CMM（show ni/show cmm）；速率/双工必须与对端一致；多次采样 Error Frames/CRC/Alignment 错误帧计数，持续增长→查线缆健康与涉及的网卡；全双工下 Collision 计数仍增长→查对端双工设置（大概率一端被强制成半双工）；终端互 ping 时 Bytes Received 不增长→查网卡。Last Time Link Changed 与 Number of Status Change 可看链路抖动（p182）。
  tags: [show-interfaces, error-counters, duplex, crc]

- id: p11
  title: 终端侧排障命令五件套
  type: principle
  source_chapter: "p123"
  source_quote: |
    "On client side: Check the hardware, Ipconfig /all ... Try to ping and tracert, Check ARP cache using 'arp -a', Perform a DNS check 'nslookup', Check the route list table : 'route print'"
  summary: |
    客户端侧先自查再怪网络：ipconfig /all 看媒体状态（网线是否连接）、物理地址、IP 是否合法、掩码与默认网关；ping/tracert 定位断点在哪一跳；arp -a 看 ARP 缓存是否学到网关/对端；nslookup 排除 DNS 因素；route print 核对本机路由表。原则：把"本机配置问题"从网络故障中先排除掉，再进交换机侧排查。
  tags: [client-side, ipconfig, arp, dns, route-print]

- id: p12
  title: show vlan member 判读三要素（VLAN 归属/端口类型/STP 状态）
  type: principle
  source_chapter: "p124"
  source_quote: |
    "show vlan member (R8): Verify the ports are in the correct VLAN, Verify spanning tree status (forwarding instead of blocking or inactive), Verify port type match what it is connecting to (default or qtagged enabled)"
  summary: |
    show vlan members 每行输出判读三要素：端口是否在正确的 VLAN；端口类型（default/untagged 与 qtagged）是否与所连对象匹配（接终端用 default，交换机间 trunk 用 qtagged）；STP 状态是否为 forwarding——本应转发的口在 blocking/inactive 要转 STP 章节继续查。配合 show configuration snapshot all 可顺带排查 deny ACL（QoS 小节）这类隐性断流配置。
  tags: [vlan, port-type, stp-status]

- id: p13
  title: ARP 排障五步法与 debug ip packet 判读
  type: principle
  source_chapter: "p127"
  source_quote: |
    "1. Make sure that the MAC address of device A and device B are learned on the right port and in correct VLAN
    ... 5. Check that the device has resolved the ARP entry to the gateway IP address
    -> show mac-learning port 'chassis/slot/port' -> show arp ... -> show ip interface vlan <num>"
  summary: |
    ARP 问题五步：1) show mac-learning port 确认 A/B 的 MAC 学在正确端口与 VLAN；2) 确认路由实例的 MAC（show ip interface vlan <num> 取接口名，再 show ip interface <string> 看 Router MAC）；3) 核对终端网关指向正确的 IP；4) 终端 ARP 网关时交换机应生成 ARP 缓存条目——show arp 确认；5) 终端 arp -a 确认已解析网关 ARP。MAC 已学但 ARP 不解析→上 debug ip packet start ip-address <ip> start 看 ARP 请求是否到交换机、交换机是否回（p128 输出 1 R / 1 S 行判读）；交换机有回但终端没有→在交换机与终端间接 sniffer。全部正常仍不通→终端配静态 MAC。
  tags: [arp, mac-learning, debug-ip-packet, gateway]

- id: p14
  title: 静默设备对策：静态 MAC 与加大 MAC 老化时间
  type: principle
  source_chapter: "p129"
  source_quote: |
    "Increase MAC Address aging time can also be increased, Add silent devices MAC address in the MAC address table as permanent
    -> mac-learning {vlan vlan_id {port chassis/slot/port | linkagg agg_id}} static mac-address mac_address [bridging | filtering]
    -> mac-learning aging-time {seconds | default}"
  summary: |
    有些设备（如静默服务器、旧网卡）不主动发流量，启动时 ARP 完成后不再发包，MAC 表项老化后被淹掉导致单播泛洪或不可达。对策：加大 MAC 老化时间（mac-learning aging-time），或把静默设备 MAC 配成永久静态表项（bridging 转发/filtering 过滤）。反向操作注意（p129）：clear arp-cache 会触发全网重新 ARP 学习，高峰期在核心交换机上执行会造成短暂中断，须避开业务时段。
  tags: [mac-learning, aging-time, static-mac, arp-cache]

- id: p15
  title: swlog 架构参数（文件数/尺寸/syslog 上限）
  type: principle
  source_chapter: "p146"
  source_quote: |
    "Switch events can be logged to Switch console, Local text file (Configurable default file size 1250 Kbytes - R8), Multiple remote devices (syslog) 12 max - R8, Loopback0 have to be configured
    -> swlog output socket ipaddr 168.23.9.100"
  summary: |
    事件日志三目的地：console、本地 flash 文件（R8 默认单文件 1250KB，swlog output flash-file-size 12500 可改）、远程 syslog（R8 最多 12 台，需要配置 Loopback0 作为源）。/flash 下可存 swlog_chassis1 到 .6 共 8 个滚动文件，swlog_archive 归档目录最多 40 个文件（p147）。show swlog 看运行状态与阈值（默认 90 percent 时覆盖告警）；swlog clear / swlog clear all 清空；swlog output socket console enable 可把控制台日志也送 syslog（p146）。
  tags: [swlog, syslog, logging, flash]

- id: p16
  title: swlog 严重级别与按应用（appid/subapp）调级
  type: principle
  source_chapter: "p151"
  source_quote: |
    "Default severity level is info. The numeric equivalent for info is 6 ... swlog appid ospf_0 subapp all level 8 ... or swlog appid ospf_0 subapp hello level debug3
    -> swlog appid ospf_0 subapp ?"
  summary: |
    默认全局级别 info（数值 6）。可按应用 ID 单独调级：swlog appid <appid> subapp <all|子应用|编号> level <级别>。例：OSPF 全部子应用 debug3 = level 8，或只对 hello 子应用 debug3。OSPF 子应用编号表（p151/p244）：1=ERROR 2=WARNING 3=RECV 4=SEND 5=FLOOD 6=SPF 7=LSDB 8=RDB 9=AGE 10=VLINK 11=REDIST 12=SUMMARY 13=DBEXCH 14=HELLO 15=AUTH 16=STATE 17=AREA 18=INTF 19=CONFIG 20=INFO 21=SETUP 22=TIME 23=MIP 24=TM 25=RESTART 26=HELPER 27=HOST 28=AUTOCONFIG。排障后必须调回 info。
  tags: [swlog, severity-level, appid, subapp, ospf]

- id: p17
  title: show log swlog 三大过滤技巧（grep/时间戳/reverse）
  type: principle
  source_chapter: "p152"
  source_quote: |
    "Timestamps: show log swlog [timestamp mm/dd/yyyy hh:mm:ss] ... Application: show log swlog |grep [appid] |grep [subapp]
    Reverse: show log swlog [timestamp ...] [slot chassis/slot] [reverse]"
  summary: |
    日志检索三板斧：1) grep 过滤——show log swlog |grep ospf（可级联 |grep 子应用），排障最常用；2) 时间戳定位——timestamp mm/dd/yyyy hh:mm:ss 从指定时刻起看（依赖交换机时间准确，故先 show system 核对时钟）；3) reverse 反序——最新日志排前面，配合 LAB4 的 show log swlog | grep failure 用法快速命中错误行。_readable 事件（p154）：swlog appid all subapp all level event + show log events 输出客户可读事件（CUSTLOG），格式为 <时间> : <CMM>/<NI> : <模块名> : <描述>。
  tags: [swlog, log-filter, grep, timestamp, custlog]

- id: p18
  title: VC 启动与配置同步机制（vcsetup.cfg/vcboot.cfg）
  type: principle
  source_chapter: "p161"
  source_quote: |
    "Upon boot-up, a switch will read its local vcsetup.cfg file and attempt to connect to the other neighbor switches ... they will discover the topology, elect a Master ... All Slaves, if they do not have a local copy of vcboot.cfg, or if their local copy does not match ... will download the vcboot.cfg from the Master chassis and reboot"
  summary: |
    VC 启动协商机制：开机读本地 vcsetup.cfg→经 VFL 连邻居→交换 vcsetup.cfg 参数→发现拓扑、选举 Master→VFL 上周期性健康检查→按 Master 的 vcboot.cfg 同步配置；slave 没有 vcboot.cfg 或与 Master 不一致时从 Master 下载并以其重启。排障要点：两台成员的 vcsetup.cfg 必须在 vf-link-mode、member-port、chassis-group 上互相兼容；解析失败的交换机会进入 error mode——vcsetup.cfg 损坏或读不出有效机箱号时，前面板所有用户口（含 VFL 成员口）保持 disabled。Auto-VC 判定链（p159-160）：vcsetup.cfg 不存在且是出厂新机→对 auto VFL 端口自动检测、自动分 VFL ID 与聚合、自动分 chassis-id 并自动建组（certified 模式启动）。
  tags: [virtual-chassis, vcsetup, vcboot, error-mode, auto-vc]

- id: p19
  title: VC debug status 的 NOK 码速查
  type: principle
  source_chapter: "p195"
  source_quote: |
    "NOK_08: There are no virtual-fabric member ports configured on this switch ... NOK_09: There are no virtual-fabric member interfaces operationally up ... NOK_14: The virtual-fabric links configured on this switch are not operationally up ... NOK_17: The virtual-chassis manager protocol did not discover any peer switch within the discovery time window (i.e. 4 minutes)"
  summary: |
    debug show virtual-chassis status 按 L0-L8 层级输出参数状态，NOK 码定位故障层：NOK_08=没有配置 VFL 成员端口（查 show virtual-chassis vf-link member-port | grep "<chassis-id>/"）；NOK_09=VFL 成员端口没有 operationally up（加查 show interfaces port 状态）；NOK_14=配置的 VFL 链路未全部 up（多条链路必须全 up 才报 OK）；NOK_17=chassis ready 后 4 分钟发现窗口内没发现任何对等体（可能无对端、VFL 不通或 VCM 协议包不通）。p164 另一实例：VFL Ports Configured 报 NOK_08、VFL LACP 报 NOK_14 的组合即指向 VFL 成员口配置缺失。
  tags: [virtual-chassis, nok-code, vfl, debug]

- id: p20
  title: STP 阻塞端口判读：转发态异常的两大原因
  type: principle
  source_chapter: "p180"
  source_quote: |
    "In any LAN with physical path redundancy there must be at least one port in blocking status ... If ports that should be in a blocking state are now forwarding, there are two likely causes: A physical failure in a link that was previously forwarding. BPDUs from the root are being dropped."
  summary: |
    物理有冗余的 LAN 中必须至少有一个阻塞端口——平时就应记录"稳定网络中哪些口该阻塞"（网络图上标出每个物理环与破环的阻塞口），排障时比对状态是否改变。本应阻塞的口变成转发的两大原因：原本转发的链路发生物理故障（拓扑重算）、根桥 BPDU 被丢弃（按普通丢包问题排查）。show spantree vlan <id> ports 的输出列（Op St / Path Cost / Desig Role / Loop Guard / Desig Bridge ID）用于核对端口角色与指定桥。
  tags: [stp, blocking-port, bpdu, topology-change]

- id: p21
  title: STP 参数与拓扑变化计数判读
  type: principle
  source_chapter: "p179"
  source_quote: |
    "Timers need to be consistent across a physical link running STP ... If topology changes are incrementing quickly, the devices participating in spanning tree cannot agree who is the root bridge. This can be caused by dropped BPDUs, a bridge that tries to change its role, or a physical link going in and out of service."
  summary: |
    show spantree vlan <id> 判读要点：Designated Root 与 Root Port 是否指向预期的根；Max Age=20/Forward Delay=15/Hello=2 等定时器必须跨链路一致；Topology Changes 快速递增说明参与 STP 的设备无法就根桥达成一致——根因可能是 BPDU 被丢、某桥试图改角色、物理链路反复 up/down；Topology age 反映距上次拓扑变化的时间。若开了 Auto Fabric，spantree 模式会被强制成 flat（p178 附注）。
  tags: [stp, timers, topology-changes, root-bridge]

- id: p22
  title: MAC flapping 检测三板斧
  type: principle
  source_chapter: "p181"
  source_quote: |
    "MAC address flapping is mostly caused by a layer 2 loop in the network (which are not detected by STP)
    The command 'show mac-learning mac-address <mac>' show if the MAC address is flapping between two ports.
    -> show interfaces | grep Number ... 1/1/4 has flapped 3655 times and port 1/1/10 has flapped 2656 times"
  summary: |
    MAC 在两个端口间反复漂移多由 STP 检测不到的 L2 环路引起。检测：1) show mac-learning mac-address <mac> 执行两次，看表项 Interface 是否在两端口间切换；2) show interfaces | grep Number——Number of Status Change 大数值端口即 flapping 口（如 3655 次）；3) show interfaces | grep Last + show system 对时间，确定当前正在 flap 的端口。深挖用 swlog appid slNi subapp macmove level debug2，show log swlog |grep MACMOVE 看 INS/DEL 在两个 c/s/p 间来回（p175/p202）。
  tags: [mac-flapping, loop, mac-learning, slni-macmove]

- id: p23
  title: BPDU 统计 debug（debug stp bpdu-stats）
  type: principle
  source_chapter: "p183"
  source_quote: |
    "-> debug stp bpdu-stats 1 start ... -> debug stp bpdu-stats show 1
    Port rxCfg rxRstp rxMstp rxTcn | txCfg txRstp txMstp txTcn
    Precaution must be taken when using the following commands as it might dump a lot of information on the screen"
  summary: |
    疑似 BPDU 丢失/单向链路时用 BPDU 收发统计：debug stp bpdu-stats <实例> start 开始采集→debug stp bpdu-stats show <实例> 输出每端口 rxCfg/rxRstp/rxMstp/rxTcn 与 tx 四列→stop 停止。判读：某端口只有 tx 没有 rx→对端 BPDU 没回来（单向链路或对端不发）；rxRstp 有数而本端不该收到该类型→模式配置混乱。注意该命令输出量大，限定实例并尽快停止。
  tags: [stp, bpdu, debug, unidirectional-link]

- id: p24
  title: STP 防故障设计九原则
  type: principle
  source_chapter: "p187"
  source_quote: |
    "Decide which bridge will be root using Priority parameter ... Avoid using VLAN 1 as default VLAN ... A single blocking port transitioning to forwarding by error can meltdown a big part of the network
    The only parameters that you may want to change are the bridge priority ... and the port cost or priority"
  summary: |
    设计期减少 STP 故障面：1) 用 priority 明确决定根桥位置（网络中心、性能强、可靠、按 VLAN 分布规划，p188）；2) 记录根与冗余在哪、每个 VLAN 哪些口该阻塞；3) 尽量减少阻塞口数量；4) 不要调 STP 定时器（影响直径与稳定性），只允许动桥优先级与端口 cost/priority；5) 避免用 VLAN 1 当默认 VLAN；6) 修剪不用的 VLAN、避免单 VLAN 横跨全网、管理流量不走上层 VLAN；7) 配 Loop Guard、UDLD（单向链路上有阻塞口时 50% 概率成环）、LBD 环回检测、qos user-port filter/shutdown bpdu、Root Guard 限制端口角色；8) 尽量依赖 L3 路由协议；9) 单个阻塞口误转发的破坏力足以瘫痪大半个网络——所有原则都为此服务。
  tags: [stp, design, loop-guard, udld, best-practice]

- id: p25
  title: MSTP 三致性检查
  type: principle
  source_chapter: "p184"
  source_quote: |
    "All devices should use the same region name ... All VLANs within an MSTI must be tagged on all interswitch links otherwise MSTP becomes unpredictable ... All switches participating in the same region must have an identical MSTP configuration."
  summary: |
    MSTP 排障三致性：同 region 所有设备 region 名一致；同一 MSTI 内的 VLAN 必须在所有交换机间链路上 tagged，否则 MSTP 行为不可预测；同 region 各交换机的 MSTP 配置必须完全相同（VLAN-MSTI 映射不一致会分裂 region）。查 show spantree msti 与 show spantree msti vlan-map。TCN 专项（p185）：TCN 至少每 1-4 分钟来一次时，追查 TCN 从哪个 VLAN 哪个端口进来（它会重启全局 MAC 老化定时器引发泛洪），用 show spantree vlan <id> 看 Topology Changes 计数。
  tags: [mstp, region, vlan-map, tcn]

- id: p26
  title: L3 丢包验证：QoS 规则计数判读
  type: principle
  source_chapter: "p215"
  source_quote: |
    "6860_A-> show active policy rule ... Packets = 20, Bytes = 23650
    -> show qos log ... rule 'rule1' matched:accept svlan 8 port 1/1/23 ... (ICMP 8:0) 192.168.8.10 -> 192.168.7.10"
  summary: |
    show active policy rule 的 Matches/Packets/Bytes 计数证明报文确实到达本设备并命中规则；show qos log 给出每次命中的明细（规则名、svlan、端口、MAC 对、ICMP 类型与 IP 对）。排丢包时在路径两端设备分别部署相同计数规则：两端计数相等→该段不丢；上游有计数下游没有→丢在这段。改完配置记得 qos apply 生效、clear qos log 清旧日志。注意策略只匹配 ingress（见 ce13）。
  tags: [qos, policy-rule, packet-count, packet-loss]

- id: p27
  title: DHCP 中继排障判据（relay statistics 的 Tx Server 计数）
  type: principle
  source_chapter: "p219"
  source_quote: |
    "show configuration snapshot ip-dhcp-relay, show ip dhcp relay statistics, show ip udp relay ... debug ip packet protocol udp start timeout 60"
  summary: |
    DHCP/UDP 排障命令族 + 判据：show ip dhcp relay statistics 的 Reception From Client 计数在涨说明客户端请求到达中继；Forw Delay/Max Hops/Agent Info/Invalid Gateway 违规计数定位报文合法性；Server Specific Statistics 的 Tx Server Total Count=0 说明中继没有向服务器转发（LAB3 根因即 destination 地址配错）。抓包级验证用 debug ip packet protocol udp start timeout 60——输出中 UDP 67,67（服务器方向）与 UDP 67,68（客户端方向）的 R/S 行可看完整 DHCP 中继链路（p220）。辅以 show log swlog | grep -E "dhcp"。
  tags: [dhcp, dhcp-relay, udp, statistics]

- id: p28
  title: RIP 典型错误条件与版本/认证兼容规则
  type: principle
  source_chapter: "p231"
  source_quote: |
    "RIP v1 and RIP v2 misinterpretation ... If a RIP-2 router receives a RIP-1 Request it responds with a RIP-1 Response ... RIP auth-type or auth-key misinterpretation: Both RIP routers should have the same authentication parameters"
  summary: |
    RIP 排障检查点：物理链路 up；目的路由在两台路由器上都存在；边缘设备/路由器子网掩码正确；VLAN 的 Forwarding 标志不是 No；v1/v2 兼容——RIP-2 收到 RIP-1 请求会回 RIP-1 响应，但配成只发 v2 时对 RIP-1 请求不响应，RIP-1 收 v2 报文会忽略 v2 字段（配了认证则丢弃路由）；认证两端 auth-type/auth-key 必须一致。show ip rip interface 看 Send/Receive-Version 与 AuthType（p233）；show ip rip peer 看邻居收包与版本（p235）；show ip rip 看 update=30s/invalid=180s/garbage=120s 定时器；show ip rip routes 看路由状态（A=Active, H=Holddown, G=Garbage）。
  tags: [rip, version-compatibility, authentication, timers]

- id: p29
  title: OSPF 接口参数判读（show ip ospf interface）
  type: principle
  source_chapter: "p240"
  source_quote: |
    "Interface IP Address = 172.16.17.1 ... OSPF Interface State = BDR ... Area Id = 0.0.0.0 ... Hello Interval (seconds) = 10 ... Dead Interval (seconds) = 40 ... # of Full State Neighbors = 1"
  summary: |
    邻居起不来的参数核对清单：Admin/Operational Status；OSPF Interface State（DR/BDR/DROther）；Area Id 两端一致；Hello Interval=10s / Dead Interval=40s（广播网默认）两端一致；Authentication Type/Key 两端一致；MTU 1500；Metric Cost。末尾四个邻居计数（Init/2-Way/Exchange/Full）是快速健康度指标——Full=0 且其他也 0 说明 Hello 都没过。配套命令族（p241-242）：show ip ospf（全局状态）、show ip ospf neighbor、show ip ospf border-routers、show ip ospf ext-lsdb（外部 LSA）、show ip ospf area [range|stub]、show ip ospf lsdb（LSDB）、show ip ospf virtual-link/virtual-neighbor（虚链路）、show ip redist、show ip ospf routes。
  tags: [ospf, interface-parameters, hello-dead-interval, lsdb]

- id: p30
  title: OSPF 日志错误样例判读（BAD LSA/超大 LSA/状态翻转）
  type: principle
  source_chapter: "p245"
  source_quote: |
    "swlogd: ospf_0 ERROR error(2) ... Unable to send oversized LSA(1,192.18.0.1,192.18.0.1): size 3588 > limit 1452
    swlogd ospf_nbr.c ospfNbrStateMachine 0 ospf_0 STATE EVENT: ... OSPF neighbor state change for 172.25.136.2, router-id 172.25.136.2: FULL to DOWN"
  summary: |
    三类高价值 OSPF 日志：1) "Unable to send oversized LSA ... size 3588 > limit 1452"——LSA 尺寸超过接口 MTU 限制发不出去（对应 OVNA 的 OSPF LSA message size exceeds MTU 异常，p321），查 MTU；2) "HELLO from x.x.x.x discarded...invalid helloInterval 10"——Hello 间隔不匹配，报文被丢弃（p247/LAB4），对齐两端 hello-interval；3) "Simple password auth failure! pktKey = alcatell, intfKey = alcatel" + "Discarding packet ... authentication failure"——认证密钥不匹配（p287/LAB4），日志直接给出两侧密钥值，改 auth-key 即可。检索方式 show log swlog | grep ospf_0 或 | grep failure。
  tags: [ospf, log-analysis, lsa, authentication, hello-interval]

- id: p31
  title: VRRP 定时器公式与虚拟 MAC 应答规则
  type: principle
  source_chapter: "p250"
  source_quote: |
    "Skew_Time: ( 256 - Priority) / 256 ... Master_Down_Interval: (3 * Advertisement_Interval ) + Skew_time
    When a host sends an ARP request ... the Master Router must respond using the Virtual MAC Address (not its physical MAC Address)"
  summary: |
    VRRP 机制参数：Advertisement Interval 为 VRRP 通告间隔，同一 VRID 的所有路由器必须一致；Skew_Time=(256-Priority)/256 防止多台同时抢 Master；Master_Down_Interval=3×AdvInterval+Skew_Time，是 Backup 判 Master 失效的时长。主机 ARP 请求虚拟 IP 时，Master 必须以虚拟 MAC（00-00-5E-00-01-<VRID>）应答而非自身物理 MAC——抓包看到物理 MAC 应答即配置异常。LAB4 实例（p282）：VRID Errors 计数 41 且 Backup 状态异常，根因是对端把虚拟地址配成了 192.168.30.154（应为 .254），两台虚拟 IP 不一致互认为非法 VRID 报文。
  tags: [vrrp, timers, virtual-mac, priority]

- id: p32
  title: 组播 L2 设计五规则（querier/forwarding/zapping/TTL）
  type: principle
  source_chapter: "p258"
  source_quote: |
    "There should be 1 dedicated querier in the network ... Querier-forwarding should be enabled only on switches located between multicast sources and the querier ... Zapping should be enabled only on edge devices ... IGMP messages must be sent with TTL equal 1"
  summary: |
    IPMS（IP 组播交换）部署五规则：全网只部署 1 个 querier（多 querier 时选举一个其余 inactive，浪费且易错）；querier-forwarding 只在位于组播源与 querier 之间的交换机上启用；zapping（快速换台优化）只在边缘设备启用；proxying 可在所有设备启用；IGMP 报文 TTL 必须为 1（跨网段送达失败常因中间设备转发了 TTL=1 报文或改了 TTL）。监测：show ip multicast 全局开关（Status/Querying/Proxying/Spoofing/Zapping/Querier Forwarding/Robustness=2/Query Interval=125s）、show interfaces flood rate 峰值洪泛速率。
  tags: [multicast, igmp, querier, ipms, ttl]

- id: p33
  title: DVMRP DF 选举与转发排错判读
  type: principle
  source_chapter: "p265"
  source_quote: |
    "If there are multiple DVMRP routers on a subnet ... One of the routers will be selected as the designated forwarder for each source/group pair ... Election by: Lowest metric, As tie breaker, lowest IP address"
  summary: |
    同一网段多台 DVMRP 路由器会重复转发组播包，因此每个源/组对选举一个 DF（指定转发者）：先比最低 metric，平手比最低 IP 地址。收不到组播流时先从源到接收端走一遍组播路径（p266）：debug 输出 tDvmrp:: Lookup S,G、A new (S,G) entry、Forward on N tunnels 可看转发向量是否建立；show ip dvmrp neighbor 看 GenID/版本/active 状态与 Expires；show ip mroute 看上游邻居与路由来源；swlog appid dvmrp_0 subapp routes|ipmrm 提取细节。
  tags: [dvmrp, designated-forwarder, multicast-routing, debug]

- id: p34
  title: PIM-SM 监控命令族与 debug 分区
  type: principle
  source_chapter: "p269"
  source_quote: |
    "-> show ip pim ... -> show ip pim neighbor ... -> show ip pim candidate-rp ... -> show ip pim interface ... -> show ip pim group-map ... -> show ip pim groute/sgroute
    swlog appid pim_0 subapp hello level <warning/info/debug3/...>"
  summary: |
    PIM 排障命令分工：show ip pim 全局参数（Keepalive=210s、Register Suppress=60s、SPT 状态）；show ip pim neighbor 邻居与 Expires（Hello 间隔 30s、J/P 间隔 60s）；show ip pim candidate-rp 参选 RP 的组范围与优先级；show ip pim interface 各口 DR 选举与 Hello/J-P 间隔；show ip pim group-map 组到 RP 的映射；show ip pim sgroute（S,G）表与 RPF 接口；show ip pim notifications 邻居丢失/非法 Register/非法 J-P 通知。debug 按子应用分区：hello（邻居收发）、boot-strap（BSR 与 RP 集合）、crp（在 BSR 上看 C-RP 通告与最优 RP 哈希）、sm-join-prune（JOIN/PRUNE 与 (S,G) 状态迁移）。LAB4 根因示例（p291）：单播通而组播不通，show ip pim interface 发现 6900 的 int_217 没启用 PIM，ip pim interface int_217 即恢复。
  tags: [pim, rp, bsr, sgroute, join-prune]

- id: p35
  title: QoS 配置生命周期命令（apply/revert/flush/reset）
  type: principle
  source_chapter: "p297"
  source_quote: |
    "qos apply: Applies configured global QoS and policy settings ... qos revert: Deletes any QoS configuration that has not been applied ... qos flush: Deletes all pending policy information ... qos reset: Resets the QoS configuration to its defaults."
  summary: |
    QoS 四个管理动作区分：qos apply 把已配置的全局 QoS 与策略应用到当前配置（生效并写入 flash）；qos revert 删除尚未 apply 的 QoS 配置（回到上次 applied 状态）；qos flush 清除全部待定策略信息；qos reset 恢复默认 QoS 配置。默认 QoS 使能。监测：show qos config 全局配置、show policy rule 策略规则、show active policy rule 激活规则与命中计数、show qos log 命中日志（上限 10000 行，qos log lines 30 调整）、qos log level 1-8（默认 5）、debug qos rule/internal verbose log 细分调试点、qos stats interval 30（默认 60s）+ show qos statistics。
  tags: [qos, policy, qos-apply, monitoring]

- id: p36
  title: UNP/802.1X 排障：RADIUS 连通性测试先行
  type: principle
  source_chapter: "p309"
  source_quote: |
    "RADIUS test tool allows the user to test the RADIUS server from the OmniSwitch: aaa test-radius-server <server_name> type authentication user <username> password <password> method pap
    Access-Accept from <server_IP_address> Port 1812 Time: 212 ms ... Filter-ID = employee"
  summary: |
    认证类故障先测服务器链路：aaa test-radius-server 从交换机直接发起认证测试，输出 Access-Accept/Reject、往返时延与返回属性（如 Filter-ID 对应 UNP profile）。限制：测试方法只支持 MD5 或 PAP，服务器侧可能未开放这两个方法，需要额外配置 RADIUS 服务器。随后 show unp user 看用户认证状态（Port/Username/MAC/IP/VLAN/Profile/Status=Active/Source）；再核 UNP 全家桶配置（p311-312）：show unp global configuration、show unp port [802.1x statistics|configured-vlans]、show unp profile map、show unp classification[-rule]、show aaa device-authentication/accounting/config/profile、show captive-portal、show quarantine mac group。服务器侧与抓包作最后佐证。
  tags: [unp, 8021x, radius, aaa-test, authentication]

- id: p37
  title: 镜像类排障工具的边界（RPM 专用 VLAN 与不镜像流量）
  type: principle
  source_chapter: "p305"
  source_quote: |
    "RPM VLAN has to be configured on the source, destination and intermediate switches ... No other traffic is allowed on that VLAN
    The following types of traffic will not be mirrored: Link Aggregation Control Packets (LACP), 802.1AB (LLDP), 802.1x port authentication, 802.3ag (OAM), Layer 3 control packets, GARP"
  summary: |
    远程端口镜像（RPM）用专用镜像 VLAN 把流量跨网传到远端交换机：源、目的与沿途交换机都要配该 VLAN，且该 VLAN 不允许承载其他任何流量。抓包结论解读时要知道六类流量不会被镜像：LACP、LLDP、802.1X 认证、802.3ag OAM、L3 控制报文、GARP——"抓不到"不等于"不存在"。基于策略的镜像（p306-307）用 policy action mirror 按条件镜像（源/目的地址、地址对、协议、VLAN 分类），同一时间只支持 1 个会话；端口镜像与端口监控不能配在同一端口。
  tags: [mirroring, rpm, policy-mirroring, capture-limits]

- id: p38
  title: 源地址固定：ip service source-ip 指定应用发包接口
  type: principle
  source_chapter: "p379"
  source_quote: |
    "If a switch is running with several IP interfaces, you can force the Syslog packets to be generated from a specific IP interface.
    sw1 (6900-A) -> ip service source-ip loopback0 swlog ... swlog Loopback0"
  summary: |
    交换机多 IP 接口时，防火墙/ACL/NAT 场景下 syslog 等应用可能因源地址不定而被丢弃。ip service source-ip <接口> <应用> 把指定应用的发包源固定到该接口（典型用 Loopback0 管理地址）；show ip service source-ip 列出 dns/ftp/ldap/ntp/radius/sflow/snmp/ssh/swlog/tacacs/telnet/tftp 各应用当前绑定的接口。OVNA 纳管多 IP 交换机时尤其要固定 syslog 源，与 Device Management 里登记的设备 IP 保持一致，否则设备匹配不上、异常归档错位。
  tags: [source-ip, syslog, loopback, management-plane]

- id: p39
  title: OVNA 系统要求与端口清单
  type: principle
  source_chapter: "p347"
  source_quote: |
    "Processor: Quad-core, RAM: 8 GB, HDD: 50 GB ... Linux OS: Ubuntu 22.04 Server Edition, Debian 11 or 12, Red Hat Enterprise Linux 9.3
    Ports: TCP 80/443 (HTTP/S for WebUI), UDP/TCP 10514/TCP 6514 (syslog/syslog-TLS), UDP 22 (SSH/SFTP ...), TCP 443 (Setup Installation and Cloud Services) ... Internet access is mandatory."
  summary: |
    OVNA 部署硬性参数：四核/8GB/50GB（200 台设备内；1000 台 120GB、2000 台 210GB，p389）；OS 支持矩阵 Ubuntu 22.04 / Debian 11/12 / RHEL 9.3；端口 TCP 80/443（WebUI）、UDP+TCP 10514（syslog）与 TCP 6514（syslog over TLS）、22（SSH/SFTP 到设备与本机访问）、443 还承担安装与云服务；必须能访问互联网（k3s 与镜像下载）。纳管设备版本门槛（p316）：OS 6xxx/9xxx 需 AOS 8.7.R2+，OS2xxx 需 AOS 5.2.R1+，Stellar AP 需 AWOS 4.0.3 MR-3+，也支持第三方设备。许可按设备 IP 计（NETAD-SWITCH/AP/TP-1Y/3Y/5Y），30 天试用期限 5 交换机+5 AP，激活即开始倒计时并带 30 天宽限（p340-341）。
  tags: [ovna, system-requirements, ports, licensing]

- id: p40
  title: 用 logger 命令注入测试日志驱动 OVNA 演练
  type: principle
  source_chapter: "p380"
  source_quote: |
    "The logger command provides an easy way to add log entries from the command line to the switch to make tests.
    YUKON #-> logger -t swlogd ipni dos WARN: VRF 0: DoS type ping overload from 10.130.7.124\/54:5f:50:b0:6d:7b on port 1\/1\/1"
  summary: |
    验证 OVNA 告警链路不必制造真实故障：su 进维护 shell 后用 Linux logger 命令按 OVNA 异常模式注入一条日志（如 DoS ping overload 或 PMD generated），经 syslog 到 OVNA 触发模式匹配，即可走完"检测→Rainbow/Teams 通知→处置动作→Anomaly History 留档"全链路。前置条件：交换机与 OVNA、外网连通（ping 测试），NTP 对时（否则通知与日志时间对不上）。事后 show log swlog |grep 关键词验证注入成功。预设异常类别参考（p321）：网络环、端口 flap、DDoS、风暴、VC takeover、OSPF/BGP 状态变化、电源/POE 故障、IP 重复、高 CPU/内存、TCAM 异常等。
  tags: [ovna, logger, anomaly-simulation, testing]
