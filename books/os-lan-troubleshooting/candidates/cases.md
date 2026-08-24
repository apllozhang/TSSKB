# cases.md · OmniSwitch LAN Troubleshooting (DT00XTE221EN) Lab/案例候选条目

- id: c01
  title: LAB1 前置：TKC 检索两个已知缺陷（linkagg 重载后 DOWN / UNP 卡 In progress）
  type: case
  source_chapter: "p132"
  source_quote: |
    "Problem N1: After reloading of OS6900-V48C8 the 10GIG Uplink to OS6560-P48Z16 stays DOWN ... Version Build 8.8.56.R02/8.9.73.R01/8.9.106.R02
    Problem N2: VC-8 OS6560 running AOS 8.5.265.R02 ... Some UNP users remain in 'In progress' State (for untagged traffic) and clients connected to these ports face reachability issues."
  summary: |
    LAB1 开场练习：用 TKC 自然语言检索两个真实案例。案例 N1——2 台 OS6900-V48C8 组 VC，OS6560-P48Z16 经 linkagg 上联；VC 整体重载后 linkagg 中 1 条或 2 条 10G 链路保持 DOWN，涉及版本 8.8.56.R02/8.9.73.R01/8.9.106.R02（已知软件缺陷，查 TKC 取修复版本）。案例 N2——8 台 OS6560 VC（AOS 8.5.265.R02）配了 UNP 端口，部分 UNP 用户（untagged 流量）停留在 In progress 状态，所连客户端出现可达性问题。训练点：先查库再排障， TKC 用例结构（描述+版本+解决方案）能直接命中版本相关缺陷。
  tags: [tkc, lab1, known-defect, linkagg, unp]

- id: c02
  title: LAB1 主案例：Client10 ping 不通 employee 认证后的 Client5
  type: case
  source_chapter: "p140"
  source_quote: |
    "Client 10 is running a specific application which need static ip address ... First, authenticated Client 5 as employees. In this case, Client 10 can't ping client 5. Second, authenticated Client 5 as contractor. In this case, Client 5 cannot get an IP address."
  summary: |
    场景：RADIUS（192.168.100.102）+ UNP 认证环境；Client10 静态 IP。现象一：Client5 以 employee（VLAN20）认证成功但 Client10 ping 不通 Client5。排查与根因（p141-143）：show vlan members 发现 6360-A 端口 1/1/1 在 vlan 1 中 inactive——端口被禁用；interfaces 1/1/1 admin-state enable 后链路 up。仍不通继续查路由：6360 侧与 6860-B 的 show ip interface 显示 int_30（vlan30）状态 DOWN——6860-B 上 vlan 30 的 IP 接口未启用，导致到 contractor 网段无路由。修复组合（p143）：sw5 上 interfaces 1/1/1 admin-state enable + unp user flush port 1/1/1（清掉卡住的 UNP 会话）+ sw8 上 ip interface int_30 admin-state enable。现象二（contractor 拿不到 IP）同根因：vlan 30 接口 down 使 DHCP 中继无归属。教训：认证 OK 不等于路径通，逐段核 VLAN/端口/接口三元状态。
  tags: [lab1, unp, vlan, ip-interface, connectivity]

- id: c03
  title: LAB2 案例1：6360 虚拟机箱组建失败（static 模式 + 端口编号错）
  type: case
  source_chapter: "p191"
  source_quote: |
    "Customer complains that the virtual chassis is not working. Troubleshoot this case and describe the procedure used to solve it."
  summary: |
    场景：6360 两台组 VC 不工作。排查（p194-198）：show virtual-chassis topology 各自成 Master 单机；debug show virtual-chassis status 报 NOK_08（无 VFL 成员口配置）、NOK_09（VFL 成员口未 up）、NOK_14（VFL 链路未 up）、NOK_17（4 分钟发现窗口内没发现对等体）；cat /flash 下 vcsetup.cfg.1.err 错误文件给出确切原因：A 台 "virtual-chassis vf-link-mode static —— ERROR: This configuration is not supported for stackport platform"；B 台同样的 static 错误加 "chassis-id 2 vf-link 0 member-port 3/1/27 —— ERROR: Chassis id needs to be consistent with chassis/slot/port"（B 台编号应为 2/1/27 而非 3/1/27）。修复：A 台 virtual-chassis vf-link-mode auto→write memory（出现 chassis 2 missing 警告确认继续）→ B 台手工重写 vcsetup.cfg（auto 模式 + auto-vf-link-port 2/1/27、2/1/28）→ reload from working no rollback-timeout→show virtual-chassis topology 验证 1=Master/2=Slave Running。要点：stackport 平台（6360）必须 auto 模式；member-port 的 chassis 段必须与本机 chassis-id 一致。
  tags: [lab2, virtual-chassis, vcsetup, vfl, nok-code]

- id: c04
  title: LAB2 案例2：6860-B/6870-A 链路 flap 与访问迟缓（VLAN 278 无 STP 成环）
  type: case
  source_chapter: "p199"
  source_quote: |
    "Fri Jul 16 00:30:47 : ipni dos WARN message: +++ VRF 0: DoS type invalid ip from 192.168.30.8/00:00:5e:00:01:02 on port 1/1/3 +++ to 224.0.0.18 ...
    CPU 98 ... arp info overwritten for 172.16.78.8 by 9424e1:e8b413 port 1/1/15 ... port 1/1/16"
  summary: |
    场景：6860-B 上持续刷 "DoS type invalid ip ... to 224.0.0.18（VRRP 组播）" 告警，访问交换机变慢。排查（p199-203）：6860-B show health CPU 98%；6860-B 无 MACMOVE 日志，转到 6870-A（console 无法进则经 EMP IP SSH）：控制台刷 "arp info overwritten for 172.16.78.8 by ... port 1/1/15/port 1/1/16" 交替——同一 IP 的 ARP 在两端口间被反复覆盖；开 swlog appid slNi subapp 20 level debug2 后 show log swlog |grep MACMOVE 确认 MAC 94:24:e1:e8:b4:13 在 1/1/15 与 1/1/16 之间每毫秒级漂移；show spantree 发现 VLAN 278 STP 状态 OFF；show vlan 278 members 确认 1/1/15、1/1/16 都在该 VLAN。根因：VLAN 278 未启用 STP，两端口直连成 L2 环，VRRP/ARP 报文环流触发 invalid-ip DoS 告警与 CPU 飙高。修复：interfaces 1/1/15-16 admin-state disable→spantree Vlan 278 admin-state enable→两端口放回 vlan 1→重新 enable→日志级别改回 info。教训：DoS invalid ip 刷屏 + CPU 高时先想环，not 攻击。
  tags: [lab2, stp, loop, mac-flapping, dos-alert, high-cpu]

- id: c05
  title: LAB3 案例1：DHL 双上联链路全部 dhl-blocking
  type: case
  source_chapter: "p223"
  source_quote: |
    "Both DHL link from 6360 to distribution are in dhl-blocking state?
    20 0/7 tagged forwarding ... 57 0/7 untagged dhl-blocking ... 58 0/8 untagged dhl-blocking"
  summary: |
    场景：6360 经两条 DHL 链路（0/7、0/8）上联汇聚，客户已因此禁用 DHL；启用时所有相关 VLAN 全部 dhl-blocking。排查（p225-226）：show vlan members 看 VLAN 20/30 在两条链路分别 forwarding/dhl-blocking 属正常负载分担，但 57（0/7）与 58（0/8）双双 blocking；sh vlan 57-58 members 发现 6860-B 侧 vlan 57 在 0/78 tagged、在 0/8 untagged——两条 DHL 链路上的 native（untagged）VLAN 不一致（DHL 要求两条链路的默认 VLAN 相同才能配对做 VLAN 分担）。修复：6860-B 上 linkagg lacp agg 8 admin-state disable→vlan 57 members linkagg 8 untagged（统一为 untagged）→enable；6360 侧同样 dhl 1 admin-state disable→vlan 57 members linkagg 8 untagged→dhl 1 admin-state enable。验证 sh vlan members 恢复 0/7、0/8 分别 forwarding。要点：DHL 排障先核两条链路的 native VLAN 一致性。
  tags: [lab3, dhl, native-vlan, linkagg]

- id: c06
  title: LAB3 案例2：四个客户端 DHCP 拿不到地址（中继目的地配错）
  type: case
  source_chapter: "p223"
  source_quote: |
    "Clients 5, 6, 9 and 10 can't obtain an IP address and DNS server address automatically.
    From Interface Any to Server 172.168.100.102 -(no the good address) ... Tx Server: Total Count = 0"
  summary: |
    场景：DHCP 服务器（192.168.100.102）在培训服务器上，Clients 5/6/9/10 无法自动获取 IP 与 DNS。排查（p227）：show ip dhcp relay statistics——Reception From Client 计数在涨（客户端请求到达了中继），但对服务器 172.168.100.102 的 Tx Server Total Count=0：中继根本没有往服务器转发；注意地址 172.168.100.102 是错的（应为 192.168.100.102，172 vs 192 一字之差）。修复：no ip dhcp relay destination 172.168.100.102→ip dhcp relay destination 192.168.100.102→复查 statistics（计数清零重新累计）；6860-B 上同样处理。判据沉淀：客户端请求计数涨 + Tx Server 为 0 = 中继目的地配置错误或服务器不可达。
  tags: [lab3, dhcp-relay, dhcp, typo, statistics]

- id: c07
  title: LAB4 案例1：VRRP 双机状态异常（未启用 + 虚拟 IP 配错 + 接口 down 三连）
  type: case
  source_chapter: "p278"
  source_quote: |
    "sw7: 1 int_20 Master 148199 ... 2 int_30 Initialize 0 0 0
    sw8: VRID Errors: 41 ... 2 int_30 Master 4090 1 0"
  summary: |
    场景：VRRP 不工作。排查（p282-284）：sw7 show ip vrrp 显示 VRID 2 (int_30) Admin Status=Disabled——sh con sn vrrp 确认配置里根本没有 admin-state enable 行；补 ip vrrp 2 interface "int_30" admin-state enable。sw8 侧 sh ip vrrp 发现 VRID2 虚拟地址是 192.168.30.154 而 sw7 是 .254——虚拟 IP 不一致导致 VRID Errors=41（收到"别人的"VRRP 报文）；修正流程 disable→no 掉重建（priority 150 + address 192.168.30.254）时又报 "ERROR: At least one IP address must be associated with the virtual router"——show ip interface vlan 30 显示 int_30 状态 DOWN；ip interface int_30 admin-state enable 后 VRID2 变 Master、Adv. Rcvd 开始计数。三个叠加根因：VRID 未启用、虚拟 IP 两端不一致、VLAN 接口 down。判据：VRID Errors 计数>0 优先怀疑虚拟 IP/VRID 不匹配；Initialize 状态优先查接口与 admin-state。
  tags: [lab4, vrrp, virtual-ip, vrid-errors, ip-interface]

- id: c08
  title: LAB4 案例2：OSPF 路由大量消失（认证密钥 + Hello 间隔双错叠加）
  type: case
  source_chapter: "p279"
  source_quote: |
    "Some routes are not anymore available on the routing table. Previous Total 22 routes ... New Total 17 routes
    ospfAuthCheckSimple: Intf 172.16.17.1: Simple password auth failure! pktKey = alcatell, intfKey = alcatel
    HELLO from 172.16.17.1 discarded...invalid helloInterval 10"
  summary: |
    场景：6900-A 路由表从 22 条掉到 17 条，经 6870-A（172.16.17.7）方向的 OSPF 路由全部消失。排查（p285-289）：先 sh system 核对两台日期时间（排障前置）；sh ip ospf neighbor——6900 只剩 int_212 一个 Full 邻居，int_217 邻居没了；两台 swlog appid ospf_0 subapp all level debug3 后 grep failure，日志直接给答案第一层：ospfAuthCheckSimple 报 pktKey=alcatell vs intfKey=alcatel（一字母之差的密钥不一致）；sw7 改 ip ospf interface int_217 auth-key alcatel 后部分恢复但 172.16.17.x 邻居仍不成——继续 show log swlog | grep 172.16.17.1 发现第二层：HELLO discarded...invalid helloInterval 10，sh ip ospf interface int_217 两边对比 20s vs 10s；sw7 改 ip ospf interface int_217 hello-interval 10 后邻居 Full、路由表回 22 条。收尾把两台日志级别改回 info。教训：修完一层要复测， OSPF 邻居不成常是多错叠加；debug3 日志会直接打印两侧不一致的值。
  tags: [lab4, ospf, authentication, hello-interval, route-loss]

- id: c09
  title: LAB4 案例3：单播通而组播不通（6900 上联口漏配 PIM）
  type: case
  source_chapter: "p280"
  source_quote: |
    "Client 1 can ping client 9 but multicast traffic is not routed to client 9.
    Client 1 on 6900a is a multicast server (Security Camera). It sends the stream on Multicast group 231.1.1.1 ... Client 9 is the receiver"
  summary: |
    场景：Client1（6900-A，VLAN110，端口 1/1/1）是监控摄像头源，向组 231.1.1.1 发流；Client9（6360 VC，VLAN30，端口 1/1/2）是接收端；单播互 ping 正常但组播流不到。排查（p291-292）：从 6360-A traceroute 192.168.110.50 确认到源的单播路径经 192.168.57.7→172.16.17.1（PIM-SM 的 RPF/join 沿单播路径走，逐跳要有 (S,G) 状态）；show ip pim interface 逐台核——6870-A 五个口 PIM enabled，而 6900-A 只有 int_212 与 int-110，路径上的 int_217 没启用 PIM，join 到不了源侧。修复：sw1 上 ip pim interface int_217，再让 Client1 发流、Client9 收流验证。要点：组播不通先 traceroute 单播路径，再沿路径逐接口核 PIM 使能状态。
  tags: [lab4, multicast, pim, rpf, traceroute]

- id: c10
  title: LAB5 用例1：模拟 DDoS 攻击告警与一键处置
  type: case
  source_chapter: "p380"
  source_quote: |
    "We are going to simulate a DDOS attack on the switch ... logger -t swlogd ipni dos WARN: VRF 0: DoS type ping overload from 10.130.7.124/54:5f:50:b0:6d:7b on port 1/1/1
    The notification message proposes remediation action ... choose Disable Port as the recommended action"
  summary: |
    场景：OVNA 已纳管 6900A（登记 Loopback0 地址 192.168.254.1，syslog 源经 ip service source-ip loopback0 swlog 固定）。演练：su 进维护 shell 用 logger 注入一条 DoS ping overload 日志→show log swlog |grep overload 确认→syslog 送 OVNA 命中 DDoS 模式→Rainbow 气泡收到含设备 IP/主机名、MAC、端口的通知并给出处置选项→选 Disable Port→OVNA 经 SSH 下发 interfaces port 1/1/1 admin-state disable→6900 控制台日志可见 "CLI log, user: admin (192.168.100.103), cmd: interfaces port 1/1/1 admin-state disable, result: SUCCESS" 与链路 down 事件→sh interfaces 1/1/1 status 确认 dis→OVNA Anomaly History 留档。完整闭环：检测→通知→决策→执行→留痕。
  tags: [lab5, ovna, ddos, rainbow, remediation]

- id: c11
  title: LAB5 用例2：模拟核心转储（PMD）触发日志收集建议
  type: case
  source_chapter: "p383"
  source_quote: |
    "We are going to simulate a switch crash that generates a PMD file ... logger -t OS6900A -s swlogd PMD main ALRT: PMD generated at /flash/pmd/pmd-etherCmm-11.04.2022-14.54.53
    The notification proposes to collect log & PMD files and invites you to contact ALE Customer Support Team"
  summary: |
    场景：模拟交换机崩溃产生 PMD（崩溃转储）文件。logger 注入 "PMD generated at /flash/pmd/pmd-etherCmm-..." 日志→show log swlog |grep pmd 验证→OVNA 识别为 OmniSwitch 内部错误类异常→通知到 Rainbow 气泡，建议动作是收集日志与 PMD 文件并联系 ALE 客户支持。与 DDoS 用例的差异点：软件崩溃类异常不提供端口关闭这类网络侧自愈动作，处置方向转向证据收集与升级 TAC——体现了 OVNA 按异常类别区分修复建议（remediation）的设计。
  tags: [lab5, ovna, pmd, core-dump, log-collection]

- id: c12
  title: LAB5 用例3：链路聚合成员口 down 告警
  type: case
  source_chapter: "p384"
  source_quote: |
    "sw1 -> show linkagg port ... 1/1/5 Dynamic 1005 ATTACHED 17 UP UP YES
    interfaces 1/1/5 admin-state disable ... 1/1/5 Convergence port down ... Sync Out port=1/1/5(4) partner:Out actor:In"
  summary: |
    场景：人工禁用 linkagg 成员口 1/1/5 触发链路聚合异常。先 show linkagg port 记录基线（1/1/5 动态聚合 ATTACHED 到 agg 17，Oper UP）；interfaces 1/1/5 admin-state disable 后，日志链完整呈现：ifAdminStatus 置 down→portMgrNi LINKSTS 1/1/5 DOWN→linkAggNi "Convergence port down" 与 LACP 状态机 Sync Out（partner:Out actor:In）→linkAggCmm 收到 agg 17 的端口离开请求→OVNA 侧 LinkAgg Down 异常与通知。恢复：重新 enable，链路 up 后异常消除。价值：linkagg 故障时日志的因果链样板，可用于人工排障时对读日志。
  tags: [lab5, ovna, linkagg, lacp, link-down]

- id: c13
  title: LAB5 用例4：交换机本地登录认证失败告警（Acknowledge 处置）
  type: case
  source_chapter: "p385"
  source_quote: |
    "Pod24sw2 login: amdin ... Authentication failure : Invalid login name or password
    SES MIP EVENT: CUSTLOG CMM Authentication failure detected: user admin
    You can simply Acknowledge the notification"
  summary: |
    场景：故意用错误用户名（amdin/admin 拼错）登录 6900A 控制台。交换机日志产生两条：CUSTLOG "Authentication failure detected: user admin" 与 login[pid] pam_authenticate call failed→OVNA 识别为用户认证失败异常→Rainbow 通知→此类事件无破坏性处置动作，直接 Acknowledge（确认收到）即可，Anomaly History 留档。展示 OVNA 三类处置动词的最轻一级：Disable Port（执行变更）、Collect Logs（取证）、Acknowledge（仅确认）。
  tags: [lab5, ovna, authentication-failure, acknowledge]

- id: c14
  title: LAB1 环境预检：培训 Pod 复用导致的客户端配置漂移
  type: case
  source_chapter: "p134"
  source_quote: |
    "As this pod may have been used previously for another training course, first check that the clients are correctly configured to run the lab... If this is not the case, please configure them accordingly."
  summary: |
    LAB1 的方法层案例：排障前先排除环境噪音。Pod 可能被上一期培训用过，客户端配置（静态 IP/认证设置）可能残留，先逐台核 Client10 静态 IP、Client5 的 802.1X 凭据（employee/contractor 双账号对应 VLAN20/30 与 UNP profile）是否符合本 Lab 前提，再开始正式排障。对应通用原则：复用环境、共享实验室、变更窗口后的"配置漂移"是高频干扰源，排障第一步是把被测环境校准到已知基线，避免把环境问题误诊为网络故障。
  tags: [lab1, environment-check, baseline, configuration-drift]
