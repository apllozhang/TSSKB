# glossary · OmniSwitch LAN Access Switching (DT00XTE215EN)
# 来源: source/fulltext.md（页码为教材 PDF 页 / <<<PAGE N>>> 标记）

```yaml
- id: g01
  title: Certified 目录（认证目录）
  type: term
  source_chapter: "p80"
  source_quote: |
    "The certified directory contains files that have been certified by an authorized user as the default
    files for the switch."
  summary: |
    Flash 上经授权用户认证的默认镜像+配置目录，是故障回退的基线。running 目录与 certified 内容
    不一致时冷启动自动回退到这里；运行于 certified 时配置不可保存。
  tags: [目录, certified, AOS]

- id: g02
  title: Working 目录（工作目录）
  type: term
  source_chapter: "p80"
  source_quote: |
    "The working directory is a holding place for new files. Files in the working directory must be tested
    before committing them to the certified directory."
  summary: |
    新镜像/配置的测试暂存目录。升级或改配流程：先在 working 验证（reload from working），
    验证通过 copy running certified 固化。
  tags: [目录, working, AOS]

- id: g03
  title: Running 目录 / Running configuration（运行目录/运行配置）
  type: term
  source_chapter: "p80"
  source_quote: |
    "The running directory is the directory where the configuration changes will be saved. The running
    configuration, stored in the RAM, contains the current operating parameters."
  summary: |
    running directory 是本次启动实际加载的目录（certified/working/user 之一）；running
    configuration 是 RAM 里的现行配置 = 启动目录内容 + 未保存改动。show running-directory 查看。
  tags: [目录, running, RAM]

- id: g04
  title: User-defined 目录（用户自定义目录）
  type: term
  source_chapter: "p67"
  source_quote: |
    "Additional User-defined directories: Created by the user (any name). Can be used to store additional
    switch configurations. Configuration changes CAN be saved directly to any user-defined directory"
  summary: |
    用户自建目录（任意命名），性质类似 working：可存整套装镜像+配置，可直接保存配置，也能
    reload from <目录> 启动，用于保存多套实验/回退点。
  tags: [目录, user-defined]

- id: g05
  title: vcboot.cfg / vcsetup.cfg
  type: term
  source_chapter: "p67"
  source_quote: |
    "Configuration files: vcboot.cfg vcsetup.cfg ... image files (AOS)"
  summary: |
    每个目录的两份文本配置：vcsetup.cfg 保存 Virtual Chassis 参数（chassis-id/group/VFL 等），
    vcboot.cfg 保存启动配置。write memory 同时替换两者；判断目录是否"一致"就是比镜像+vcboot.cfg。
  tags: [配置文件, vcboot, vcsetup]

- id: g06
  title: CMM（Chassis Management Module，机箱管理模块）
  type: term
  source_chapter: "p44"
  source_quote: |
    "Remotely manage the switch directly via the CMM (not available in all switches). The EMP port IP
    address of the master chassis (Virtual Chassis) ip interface master emp address 172.25.167.203"
  summary: |
    交换机的管理主控模块，带外管理（EMP 口）直连 CMM 绕过业务网板；show running-directory 里的
    Running CMM、CMM Slot 均指它。
  tags: [硬件, 管理, CMM]

- id: g07
  title: EMP（Ethernet Management Port，以太网管理口）
  type: term
  source_chapter: "p44"
  source_quote: |
    "ACCESS VIA THE EMP PORT: Bypass the network interface modules (NI). Remotely manage the switch
    directly via the CMM. USB Ethernet Dongle... This interface is treated just like an EMP interface."
  summary: |
    独立于业务面的带外管理网口；无 EMP 口的型号（6360/6465/6560）用 USB-Ethernet dongle 等效
    替代，所有 EMP 命令同样适用。VC 场景配 master 的 EMP 地址即可管理整个 VC，RCD 也走它。
  tags: [带外管理, EMP]

- id: g08
  title: Virtual Chassis（VC，虚拟机箱）
  type: term
  source_chapter: "p91"
  source_quote: |
    "Virtual Chassis = Group of switches which appears as a single router or bridge. Single Point of
    management / Single Logical Switch / No STP/VRRP between Access and Core switches / No license needed"
  summary: |
    多台交换机经 VFL 互联后对外呈现为一台逻辑设备：单一管理点、跨机箱冗余、免 STP/VRRP、无需
    许可。拓扑可为链形/环形/全互联，规模按型号 2-10 台不等。
  tags: [VC, 堆叠]

- id: g09
  title: VFL（Virtual Fabric Link，虚拟机箱互联链路）
  type: term
  source_chapter: "p91"
  source_quote: |
    "Switches inter-connected via dedicated or optional SFP+, QSFP ports. Mesh or Ring topology ... VFL"
  summary: |
    VC 成员间的专用互联链路，可用专用堆叠口或占用业务 SFP+/QSFP 口，支持 auto（自动检测+自动
    分配 VFL ID，须两端都是 auto 候选口）与 static 两种模式。show virtual-chassis vf-link 查看。
  tags: [VC, VFL, 堆叠链路]

- id: g10
  title: ISIS-VC（VC 内部路由/拓扑协议）
  type: term
  source_chapter: "p94"
  source_quote: |
    "VC topology managed by ISIS-VC. Private TLV report the switch's capability and numbering. Exchange
    IS-IS HELLO for adjacencies and updates. Maintains a loop-free topology for BUM traffic"
  summary: |
    VC 私有控制协议：基于 IS-IS HELLO 维护成员邻接与无环拓扑、承担 master 选举、在成员间建转
    发库并按 SPBM 式确定性打破等价路径。
  tags: [VC, ISIS-VC, 控制]

- id: g11
  title: RCD（Remote Chassis Detection，远程机箱检测）
  type: term
  source_chapter: "p99"
  source_quote: |
    "Out of Band: EMP Remote Chassis Detection (RCD). A switch sends an announcement whenever its chassis
    VC information changes. RCD protocol will detect this split topology."
  summary: |
    带外脑裂检测：经 EMP 管理网互发机箱 VC 信息通告，VFL 全断（split）时识别出伪 master 并让其
    关闭所有用户口防止 MAC/IP 重复。地址偏好：NVRAM 里的 CMM IP > EMP IP。
  tags: [VC, split, RCD]

- id: g12
  title: VCSP（VC Split Protection / VC Split Protocol）
  type: term
  source_chapter: "p100"
  source_quote: |
    "In Band: VC Split Protocol. Requires an upstream or downstream device to act as helper switch.
    Every VC member switch recommended to have one port as part of the VCSP LAG to the helper device"
  summary: |
    带内脑裂防护：借上/下游 helper 交换机，VC 成员各出一口组成 VCSP LAG 到 helper；用
    virtual-chassis split-protection [helper] admin-state/linkagg 命令启用。
  tags: [VC, split, VCSP]

- id: g13
  title: ISSU（In Service Software Upgrade，不中断升级）
  type: term
  source_chapter: "p101"
  source_quote: |
    "Used to upgrade the software on a VC with minimal network disruption. Each element is upgraded
    individually ... The Slaves are then reloaded from the ISSU directory in order from lowest to highest
    chassis ID"
  summary: |
    VC 逐台成员滚动升级机制：新代码放独立目录后由 issu 命令分发并按 chassis ID 从小到大逐台
    重启，网络冲击最小化。
  tags: [VC, ISSU, 升级]

- id: g14
  title: ASA（Authenticated Switch Access，交换机认证接入）
  type: term
  source_chapter: "p57"
  source_quote: |
    "Authenticated Switch Access (ASA) provides the ability to restrict which users can configure the
    switch remotely... ASA applies to Telnet, FTP, SNMP, SSH, HTTP, and the console and modem ports."
  summary: |
    管理面接入控制：按 console/telnet/ftp/http/snmp/ssh/default 七类服务分别指定本地库或
    RADIUS/LDAP 认证链，show aaa authentication 查看每类服务的认证服务器与 exit-on-fail 状态。
  tags: [管理安全, AAA, ASA]

- id: g15
  title: WebView（内嵌 Web 管理）
  type: term
  source_chapter: "p47"
  source_quote: |
    "The WebView application is embedded in the switch and is accessible via a web browser.
    webview force-ssl enable (default=enabled)"
  summary: |
    交换机内置的单机 Web 管理界面，默认启用且 R8 强制 SSL（HTTP 自动跳 HTTPS）；配置分
    Physical/L2/Networking/Service/Security/QoS/Device 七大组。仅限单台设备视图。
  tags: [管理, webview]

- id: g16
  title: Lightning Configuration（闪电配置/快速开局）
  type: term
  source_chapter: "p49"
  source_quote: |
    "The switch starts with default IP address, VLAN 1, lightning-config interface, IP 192.168.0.1/24 ...
    A Quick Config Dashboard window opens. We get access of the mandatory and pre-selected options"
  summary: |
    出厂零配置开局模式：仅 1/1/1-2 接入客户端时经 HTTPS 打开 Quick Config 向导（NTP/IP/网关/
    DNS/VMS 等），可导出/导入配置文件；首次 write memory 后默认 IP 失效。
  tags: [开局, 零配置]

- id: g17
  title: Thin Client 模式（瘦客户端）
  type: term
  source_chapter: "p76"
  source_quote: |
    "No configuration is stored on the switch. It will contact OmniVista 2500 to retrieve the config...
    In thin-client mode, no configuration is saved in the 'running' directory ... All configuration
    changes should be done in OV 2500."
  summary: |
    激活流程中声明的托管模式：交换机启动后向 OV 2500 注册拉取配置，本地不留配置、write memory
    不落盘，一切变更在 OV 2500 集中完成（仅留最小网络可达的 vcboot.cfg）。
  tags: [OV2500, 集中管理]

- id: g18
  title: UNP（User Network Profile，用户网络档案）
  type: term
  source_chapter: "p142"
  source_quote: |
    "UNP R8: VLAN ID / Policy List / ACL / QoS / Location / Period"
  summary: |
    统一的用户/设备接入档案：一个 profile 聚合 VLAN 映射、QoS/ACL 策略列表、位置与时段策略，
    通过分类规则或 RADIUS Filter-Id 命中后套用到端口上的用户。
  tags: [UNP, profile]

- id: g19
  title: Access Guardian（接入卫士）
  type: term
  source_chapter: "p377"
  source_quote: |
    "Role Based Access Control with UNP (Universal Network Profile). Auto-sensing, multi-client
    authentication on a port"
  summary: |
    ALE 的接入安全方案：端口上自动识别 802.1X（supplicant）或 MAC（非 supplicant）认证，经
    RADIUS 的 Filter-Id 返回 UNP，实现按人/设备角色下发 VLAN+QoS+ACL；服务器不可达可走
    auth-server-down profile。
  tags: [接入安全, 802.1x, UNP]

- id: g20
  title: 802.1Q / 802.1p（VLAN 标签与优先级）
  type: term
  source_chapter: "p139"
  source_quote: |
    "VLAN Tag: 802.3 MAC header change, 4096 unique VLAN Tags (addresses), VLAN ID == GID == VLAN Tag.
    802.1P: Three-bit field within 802.1Q header, Allows up to 8 different priorities"
  summary: |
    802.1Q 在以太帧头插 4 字节标签：12bit VLAN ID（4096 个）+3bit 802.1p 优先级（8 级）。
    trunk 口上每个 VLAN 可 tagged 传送，物理口保留一个 untagged 桥接 VLAN。
  tags: [VLAN, 标签, 优先级]

- id: g21
  title: Mobile Tag（移动标签）
  type: term
  source_chapter: "p416"
  source_quote: |
    "Mobile Tag: Allows mobile ports to receive 802.1Q tagged packets / Not supported on mobile ports(802.1Q
    Tag) / Triggers dynamic assignment of tagged mobile port traffic to one or more VLANs"
  summary: |
    与 802.1Q tag 相对的机制：普通 802.1Q 只能配在固定端口，mobile tag 允许 UNP mobile 口接收
    tagged 流并动态归入对应 VLAN——LLDP-MED 话机场景常用（UNP profile mobile-tag + map vlan）。
  tags: [UNP, mobile-tag, 语音]

- id: g22
  title: Linkagg / LACP 与 Actor Admin Key（链路聚合）
  type: term
  source_chapter: "p211"
  source_quote: |
    "The link aggregation number and ports are associated to a dynamic link aggregation using the actor
    admin key. Although in the above example the actor admin key matches the link aggregation number, this
    is not a requirement as the admin key has local significance only."
  summary: |
    把多条物理链路合成一条逻辑链路（增带宽/冗余）。静态 linkagg 仅限 OmniSwitch 间；动态
    linkagg lacp 按 802.3ad 用 LACPDU 协商可跨厂商。actor admin key 是端口入组的关联键，仅本地
    有效、不必等于组号。聚合口可像物理口一样挂 VLAN（tagged/untagged）。
  tags: [链路聚合, LACP, admin-key]

- id: g23
  title: STP 模式：flat 与 per-vlan（1x1）
  type: term
  source_chapter: "p227"
  source_quote: |
    "Supports two Spanning Tree operating modes: flat (single STP instance per switch) / per-VLAN (single
    STP instance per VLAN) (By default on OmniSwitch)"
  summary: |
    flat=整机一个 STP 实例；per-vlan（1x1）=每 VLAN 一个实例（OmniSwitch 默认）。1x1 下可按
    VLAN 设不同根桥实现上行链路负载分担。协议可选 802.1d(STP)/802.1w(RSTP)/802.1s(MSTP)。
  tags: [STP, 模式]

- id: g24
  title: DHL（Dual-Home Link，动态双归属）及 RAW/MVRP 冲刷
  type: term
  source_chapter: "p251"
  source_quote: |
    "High availability feature. Provides fast failover between Core/Aggregation and Access switches without
    using STP. DHL Active-Active splits VLANs between two active links"
  summary: |
    接入交换机双上行到两台核心的无 STP 双活方案：每 VLAN 只在一条链路转发（防环），故障时 VLAN
    整体切到另一条，带宽 100% 利用。每机 1 会话、2 链路；MAC 冲刷三选一——RAW Flooding（以旧
    MAC 为源广播触发重学习）、MVRP Enhanced（带 new 标志的 join）、none（默认，保留旧表项）。
  tags: [DHL, 高可用, mac-flushing]

- id: g25
  title: DHCP Relay（DHCP 中继 / IP Helper）与 Option 82
  type: term
  source_chapter: "p275"
  source_quote: |
    "Two types of DHCP relay agents: global and per-interface ... They are mutually exclusive.
    DHCP Relay Opt82 Format = Base MAC"
  summary: |
    把客户端的 DHCP 广播跨网段转给服务器；global 模式面向全网、per-interface 模式按 IP 接口
    指定服务器，两者互斥。默认携带 Option 82（格式 Base MAC）标识来源交换机。
  tags: [DHCP, relay, option82]

- id: g26
  title: Loopback0 接口
  type: term
  source_chapter: "p282"
  source_quote: |
    "Identify a consistent address for network management purposes. Not bound to any VLAN. Always remain
    operationally active ... Automatically advertised by RIP and OSPF"
  summary: |
    名字固定为 Loopback0 的 /32 环回接口：不绑 VLAN、恒 UP，自动被 RIP/OSPF 宣告，常作 NMS/
    RADIUS/NTP/sFlow 的稳定源地址与 router-id。
  tags: [环回, 管理地址]

- id: g27
  title: VRRP（虚拟路由冗余协议）/ VRID / 虚拟 MAC
  type: term
  source_chapter: "p297"
  source_quote: |
    "Protocol for electing a switch as the master virtual router. Default gateway = Virtual Router IP.
    Multicast - 224.0.0.18. Virtual MAC address: 00-00-5E-00-01-{VRID}"
  summary: |
    默认网关冗余协议（RFC 2338/2787）：同网段多台路由器共享 VRID+虚拟 IP，优先级最高者为
    master 转发并应答 ARP；虚拟 MAC 00-00-5E-00-01-{VRID} 使 master 切换无需终端重新 ARP。
    支持 track 策略联动端口/IP 降优先级。
  tags: [VRRP, 网关冗余]

- id: g28
  title: QSI / QSP（队列集实例/队列集模板）
  type: term
  source_chapter: "p319-320"
  source_quote: |
    "QSet Profile 1: Q1 = SP7, 100% BW ... Q8 = SP0 (8SP)
    -> qos qsi port 1/2/1 qsp 2 / qos qsp system-default 2"
  summary: |
    出口拥塞管理单元：QSP（QSet Profile）是队列调度模板（如 QSP1=8 个严格优先级队列、QSP2=1
    EF+7 SP），QSI 是端口/聚合上的实例。qos qsi port X qsp N 按口指定，qos qsp system-default
    N 改全局默认。
  tags: [QoS, 队列, 拥塞管理]

- id: g29
  title: 策略三元组：policy condition / action / rule
  type: term
  source_chapter: "p322-327"
  source_quote: |
    "A policy (or a policy rule) is made up of: 1. a condition 2. an action
    -> policy rule r1 precedence 200 condition c1 action a1 log"
  summary: |
    QoS/ACL 统一策略模型：condition 匹配 L1-L4 字段（含 group 复用），action 定义处置
    （priority/bandwidth/标记/redirect/mirror/disposition），rule 以 precedence 组装两者并可加
    log/trap/count/validity-period，qos apply 生效。
  tags: [QoS, ACL, policy]

- id: g30
  title: PBR（Policy Based Routing，策略路由）
  type: term
  source_chapter: "p335-336"
  source_quote: |
    "QoS policies that will override the normal routing mechanism for traffic matching the policy
    condition ... -> policy action <action_name> permanent gateway ip <ip address>"
  summary: |
    用 QoS 策略改写转发路径：action 里 permanent gateway ip 指定下一跳覆盖路由表（如把源
    10.10.0.0/16 全部引流到防火墙），硬件实现；条件里加 source port 防回流环路。支持
    6570M/6860/6865/6900/9900。
  tags: [PBR, 策略路由]

- id: g31
  title: RPM / 策略镜像（Remote & Policy Based Mirroring）
  type: term
  source_chapter: "p340-342"
  source_quote: |
    "Allows traffic to be carried over the network to a remote switch. Achieved by using a dedicated remote
    port mirroring VLAN. (p341) Mirroring is done based on a QoS policy instead of a specific port.
    -> policy action a1 ingress egress mirror 1/1/1"
  summary: |
    RPM 用专用镜像 VLAN 把流量跨交换机送到远端抓包口（该 VLAN 不许跑别的流量，LACP/LLDP/802.1x
    等控制包不被镜像）；策略镜像按 QoS condition（IP/MAC/协议/VLAN）决定镜像，action 加
    ingress/egress mirror <口>。
  tags: [镜像, RPM, 抓包]

- id: g32
  title: ACL disposition（accept/drop/deny）
  type: term
  source_chapter: "p354"
  source_quote: |
    "DISPOSITION accept | drop | deny ... policy action a1 disposition accept"
  summary: |
    ACL 动作里的处置三态：accept 放行（默认）、drop 丢弃、deny 拒绝。规则未命中任何策略的流
    默认被接受；配合 UserPorts 组可实现防 IP 欺骗、协议过滤与端口自动关闭。
  tags: [ACL, disposition]

- id: g33
  title: UserPorts / DropServices（保留策略组）
  type: term
  source_chapter: "p362-363"
  source_quote: |
    "UserPorts: Reserved Group. Used by default to prevent spoofed IP addresses on ports ... qos user-port
    {filter | shutdown} {spoof|bgp|bpdu|rip|ospf|vrrp|...}
    DropServices ... Any services belonging to this group will be dropped if seen on ports included in the
    UserPorts group"
  summary: |
    两个保留 port/service 组：把用户口加进 UserPorts 即获得防源 IP 欺骗（可扩展过滤
    rip/ospf/bpdu/dhcpserver 等，甚至违规自动 shutdown）；DropServices 里的服务（如 tcp135/
    445、udp137）在 UserPorts 口上一律丢弃——不用写规则即全局生效。
  tags: [ACL, 安全, 保留组]

- id: g34
  title: swlog（交换机日志）
  type: term
  source_chapter: "p161"
  source_quote: |
    "Event logging utility. Useful in maintaining and servicing the switch. Switch events can be logged to
    Switch console / Local text file / Multiple remote devices (syslog) 12 max"
  summary: |
    系统事件日志子系统：输出到 console/flash（swlog_chassis1~1.6 轮转+archive）/syslog（最多
    12 台）；按 appid/subapp 调级别，level event + show log events 输出客户可读事件。
  tags: [日志, swlog]

- id: g35
  title: sFlow 与 RMON（流量采样/远程监控）
  type: term
  source_chapter: "p184-185"
  source_quote: |
    "Traffic flows monitoring and sampling technology embedded within switches. One Sampler for each
    interface Collects packet samples. One Poller for each interface Collects counter samples.
    -> sflow sampler 1 port 1/1/6 receiver 1 rate 5 sample-hdr-size 64"
  summary: |
    sFlow（RFC 3176）：内嵌 agent 按口配 sampler（采包头，rate 抽样）与 poller（采计数器）发到
    receiver，用于流量画像/异常检测/容量规划。RMON：端口统计探针（以太统计/历史/告警/事件四
    组）供 OmniVista 等 NMS 拉取（show rmon probes）。
  tags: [sFlow, RMON, 监控]

- id: g36
  title: LLDP / LLDP-MED（链路层发现协议）
  type: term
  source_chapter: "p409-415"
  source_quote: |
    "IEEE 802.1AB - Link Layer Discovery Protocol (LLDP). L2 discovery protocol. Enabled by default on the
    OmniSwitches ... LLDP-MED: Provides VoIP-specific extensions to base LLDP protocol"
  summary: |
    邻居发现协议（802.1AB，默认收发开启），以 TLV 交换 chassis/port/系统信息；LLDP-MED 扩展
    面向话机：Network Policy TLV 下发 VLAN+L2 优先级+DSCP、位置、电源与资产清单（show lldp
    remote-system med inventory）。
  tags: [LLDP, 发现协议, 语音]

- id: g37
  title: PoE（以太网供电）与 FPoE / PPoE / EEE
  type: term
  source_chapter: "p429-433"
  source_quote: |
    "The PoE (Power over Ethernet) passes a voltage in addition to the data on an ethernet cable.
    Fast PoE ... Used to provide PoE power a few seconds after powering up the chassis.
    Perpetual PoE ... Provides uninterrupted power to the connected device (PD) even when the switch is
    restarting"
  summary: |
    网线同时传数据与电力（af 15.4W / at 30W / bt 最高 100W，型号带 P 表示支持）。FPoE 开机秒级
    供电、PPoE 重启期间不断电（均需升级 FPGA/CPLD）；EEE（802.3az）空闲低功耗仅限铜口
    100/1000M。lanpower 命令族管理预算/优先级。
  tags: [PoE, FPoE, PPoE, EEE]

- id: g38
  title: Auto Fabric / RCL（智能织物/自动远程配置）
  type: term
  source_chapter: "p460-465"
  source_quote: |
    "AUTO-FABRIC - PLUG-N-PLAY ZERO TOUCH DEPLOYMENT: 1- Auto-VC 2- Automatic remote configuration 3-
    Auto-LACP 4- Auto-Routing 5- Auto-SPB Fabric 6- Auto-Network Profiling 7- Auto-MVRP"
  summary: |
    零接触部署框架：开机自组 VC、经 RCL（在 VLAN 1/127 各试 3 次 DHCP 拉取指令/配置文件）下发
    配置，再自动发现 LACP/OSPF/ISIS/SPB（BVLAN 4000-4015）、生成网络档案并启用 MVRP；auto-
    fabric admin-state enable / auto-config-abort 管理。
  tags: [零配置, auto-fabric, RCL]

- id: g39
  title: write memory flash-synchro（同步保存命令）
  type: term
  source_chapter: "p71"
  source_quote: |
    "sw7 (OS6860-A) -> write memory flash-synchro = write memory + copy running certified"
  summary: |
    组合保存命令：一步完成"RAM→running 目录"和"running→certified"（VC 中还同步所有成员的
    Flash Between CMMs）。Lab 收尾的标准动作，等价于依次执行两条命令。
  tags: [保存命令, flash-synchro]

- id: g40
  title: ssh-chassis（VC 成员跳转登录）
  type: term
  source_chapter: "p102"
  source_quote: |
    "A user can access to remote CLI console of any VC with secure shell protocol (SSH).
    ssh-chassis <username>@<chassis-id>
    -> ssh-chassis admin@2 ... Local Chassis: 2"
  summary: |
    在 master CLI 上直接 SSH 到指定 chassis-id 成员的本机控制台（底层 ssh admin@127.10.x.65），
    提示符不变，用 show virtual-chassis topology 的 Local Chassis 值确认所在成员，logout 返回。
  tags: [VC, ssh-chassis, 运维]
```
