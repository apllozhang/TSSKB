# cases (Lab) · OmniSwitch LAN Access Switching (DT00XTE215EN)
# 来源: source/fulltext.md（页码为教材 PDF 页 / <<<PAGE N>>> 标记）

```yaml
- id: c01
  title: Lab 远程交换机访问（SSH + WebView 建删 VLAN）
  type: case
  source_chapter: "p54-63"
  source_quote: |
    "sw3 (6560-A) -> session cli timeout 60
    sw3 (6560-A) -> write memory
    File /flash/working/vcsetup.cfg replaced. File /flash/working/vcboot.cfg replaced.
    sw3 (6560-A) -> show aaa authentication ... Service type = Ssh / 1st authentication server = local
    Vlan : 59 / Description : Student / sw3 (6560-A) -> show vlan"
  summary: |
    首个 Lab：先用 show aaa authentication 确认 SSH/HTTP 用本地库认证（若 denied 用 aaa
    authentication ssh local），Tera Term SSH 登录（admin/switch）；改 CLI 不活动超时 session cli
    timeout 60 并 write memory；再走 WebView（https://管理IP，R8 强制 SSL）在 Security>ASA 改
    CLI/HTTP 超时，Layer2>VLAN 建 VLAN 59（Student）再删，CLI 用 show vlan 双向验证。
  tags: [Lab, SSH, WebView, aaa, session-timeout]

- id: c02
  title: Lab Working/Running/Certified 目录全流程实验
  type: case
  source_chapter: "p79-88"
  source_quote: |
    "sw3 (6560-A) -> vlan 2 / vlan 3 / vlan 99
    sw3 (6560-A) -> write memory  ... Running configuration : CERTIFY NEEDED
    sw3 (6560-A) -> reload all ... Running configuration : CERTIFIED
    sw3 (6560-A) -> write memory / ERROR: Write memory is not permitted when switch is running in certified mode
    sw3 (6560-A) -> mkdir lab / -> cp working/*.* lab / -> reload from lab no rollback-timeout
    sw3 (6560-A) -> copy running certified"
  summary: |
    目录机制实验主线：建 VLAN 2/3/99（只在 RAM）→ show running-directory 看到 NOT SYNCHRONIZED →
    write memory 后变 CERTIFY NEEDED → reload all 回退 certified、VLAN 全丢 → reload from working
    找回 → certified 模式下 write memory 报错 → mkdir lab 建 user 目录、cp working/*.* lab（
    boot.md5 Permission denied 可忽略）→ reload from lab → copy running certified 固化。附 USB
    备份：usb enable / usb backup admin-state enable / write memory flash-synchro（拔 U 盘前必须
    usb disable）。
  tags: [Lab, 目录管理, reload, certified, USB]

- id: c03
  title: Lab Virtual Chassis-6360 双机组建与监控
  type: case
  source_chapter: "p112-122"
  source_quote: |
    "sw5 (6360-A) -> virtual-chassis chassis-group 1
    sw5 (6360-A) -> virtual-chassis chassis-id 1 configured-chassis-priority 200
    sw6 (6360-B) -> virtual-chassis chassis-id 1 configured-chassis-id 2
    sw5 (6360-A) -> virtual-chassis vf-link-mode auto / auto-vf-link-port 1/1/27 (P10: 1/1/11)
    sw5 (6360-A) -> interfaces 1/1/27-28 admin-state enable
    sw5 (6360-A) -> write memory flash-synchro / -> ssh-chassis admin@2"
  summary: |
    6360-A（chassis-id 1、priority 200）与 6360-B（configured-chassis-id 2）组 VC：两边同
    chassis-group 1 → 配 auto VFL 口（P24 用 1/1/27-28/2/1/27-28，P10 用 11-12）→ write memory
    后各 reload（priority/chassis-id 改动必须重启生效；B 端 write memory 会警告 Chassis 1
    missing）→ 激活端口后 B 自动重启入 VC。监控：show virtual-chassis topology（"+"=未保存）、
    show virtual-chassis vf-link member-port、show virtual-chassis consistency、ssh-chassis
    admin@2 登从机、write memory flash-synchro 同步。
  tags: [Lab, VC, 6360, vf-link, flash-synchro]

- id: c04
  title: Lab VLAN 建网、VLAN 间路由与动态 VLAN（UNP/MAC）
  type: case
  source_chapter: "p144-157"
  source_quote: |
    "sw5 (6360-A) -> ip interface int_1 address 192.168.10.5/24 vlan 1
    sw5 (6360-A) -> vlan 50 / -> ip interface int_50 address 192.168.50.5/24 vlan 50
    sw5 (6360-A) -> vlan 50 members port 1/1/2 untagged
    sw5 (6360-A) -> unp profile employee / unp profile employee map vlan 40
    sw5 (6360-A) -> unp classification mac-address 00:50:56:90:ee:0a profile1 employee
    sw5 (6360-A) -> unp port 2/1/1 port-type bridge / unp user flush port 2/1/1"
  summary: |
    VLAN Lab：先看 VLAN 1 默认态（无成员 oper down）→ 建 IP 接口并绑 VLAN（可合写一条命令）→
    激活成员口让接口 UP → 建 VLAN 50 + 客户机静态 IP，show ip routes 出现两条 LOCAL 网段实现
    VLAN 间路由 → 动态 VLAN：unp profile employee map vlan 40 + MAC 分类规则 + unp port
    port-type bridge，flush 后 show unp user 看到 2/1/1 自动进 VLAN 40（unpUntag）→ 收尾
    no ip interface/no vlan/no unp 系列清理（VLAN 1 不可删）。
  tags: [Lab, VLAN, ip-interface, inter-vlan, UNP]

- id: c05
  title: Lab 基础维护与诊断工具（swlog/命令日志/镜像/监控/健康/RMON）
  type: case
  source_chapter: "p187-195"
  source_quote: |
    "sw7 (6870-A)-> swlog appid all subapp all level event / -> show log events
    sw7 (6870-A)-> command-log enable / -> show command-log
    sw7 (6870-A)-> port-mirroring 1 source port 1/1/1 destination port 1/1/10 / port-mirroring 1 enable
    sw7 (6870-A)-> port-monitoring 1 source port 1/1/1 enable / port-monitoring 1 pause / resume / disable
    sw7 (6870-A)-> show health / -> show rmon probes stats 1"
  summary: |
    在 6870-A 上依次演练：swlog enable/disable 与 show log swlog（CTRL+C 停）；Readable Event 用
    level event + show log events 输出客户可读事件；command-log enable 后建删 VLAN 验证审计；
    端口镜像 1 复制 1/1/1→1/1/10；端口监控抓包到 /flash/pmonitor.enc（可暂停/恢复，show
    port-monitoring file 回显）；show health 看 CPU/内存；show rmon probes [history|stats] 看探针。
  tags: [Lab, 诊断, swlog, command-log, port-mirroring, health, rmon]

- id: c06
  title: Lab LACP 动态聚合（6360 VC ↔ 6870-A）与故障演练
  type: case
  source_chapter: "p209-217"
  source_quote: |
    "sw5 (OS6360-A) -> linkagg lacp agg 7 size 2 actor admin-key 7
    sw5 (6360-A) -> linkagg lacp port 1/1/3 actor admin-key 7 / linkagg lacp port 2/1/4 actor admin-key 7
    sw7 (OS6870-A) -> linkagg lacp port 1/1/3-4 actor admin-key 7
    sw5 (6360-A) -> vlan 57 members linkagg 7 untagged
    sw7 (6870-A) -> interface 1/1/3 admin-state disable / show linkagg port"
  summary: |
    两端各建 linkagg 7（size 2、admin-key 7，admin-key 仅本地意义），VC 侧跨机箱 1/1/3+2/1/4，
    6870 侧 1/1/3-4；单边配好时 show linkagg 显示 DOWN（Att/Sel 0 0），对端配完即 UP。把默认
    VLAN 改为 57（vlan 57 members linkagg 7 untagged），两端客户端 192.168.57.105/107 互 ping，
    再 disable 成员口 1/1/3 演示单链路存活冗余（show linkagg port 看 DOWN/UP）。
  tags: [Lab, LACP, linkagg, 冗余测试]

- id: c07
  title: Lab 802.1Q 打标签（跨三交换机多 VLAN 单链路）
  type: case
  source_chapter: "p218-224"
  source_quote: |
    "sw5 (6360-A) -> vlan 58 members port 2/1/3 untagged
    sw5 (6360-A) -> vlan 20 members linkagg 7 tagged / vlan 30 members linkagg 7 tagged
    sw5 (6360-A) -> vlan 20 members port 2/1/3 tagged / vlan 30 members port 2/1/3 tagged
    sw7 (6870-A) -> ip interface int_20 address 192.168.20.7/24 vlan 20
    A PHYSICAL PORT ALWAYS HAS 1 VLAN (THE DEFAULT VLAN FOR THE PORT) THAT BRIDGES TRAFFIC (LEVEL 2)"
  summary: |
    先建 VLAN 58 做物理口默认（untagged 桥接）VLAN，再在链路两端把 VLAN 20/30 以 tagged 加到
    linkagg 7/78 与级联口（2/1/3、1/1/3）；6870/6860 分别做 VLAN 20/30 网关。show vlan members
    port 验证一口同时承载 tagged 20/30 + untagged 58（6860-B 上 20/30 因 STP 阻塞属正常）。
    Client5(VLAN20)/Client6(VLAN30) 互 ping 验证 L2/L3 混合路径，最后 write memory flash-synchro。
  tags: [Lab, 802.1Q, tagged, trunk, VLAN]

- id: c08
  title: Lab STP 根桥控制、端口状态与 1x1 负载分担
  type: case
  source_chapter: "p238-248"
  source_quote: |
    "sw7 (6870-A) -> spantree vlan 20 priority 20000 / spantree vlan 30 priority 20000
    sw5 (6360-A) -> show spantree vlan 20 ports ... 2/1/3 BLK ... ALT / 0/7 FORW ... ROOT
    sw5 (6360-A) -> linkagg lacp agg 7 admin-state disable
    sw7 (6870-A) -> spantree vlan 30 priority 32768 / Sw8 (6860-B)-> spantree vlan 30 priority 20000"
  summary: |
    用 spantree vlan N priority 20000 把 6870-A 设为 VLAN 20/30 根桥（Bridge ID==Designated
    Root 即为根）；show spantree vlan 20 ports 分析根口/指定口/ALT 阻塞口，默认全 32768 时比
    最小 MAC。禁用 linkagg 7 演示 RSTP 亚秒收敛（Topology age 归零、阻塞口转 FORW）。第三段做
    1x1 负载分担：VLAN 20 根=6870（pri 20000）、VLAN 30 根=6860（6870 恢复 32768），两上行口
    各为一个 VLAN 转发。
  tags: [Lab, STP, 根桥, blocking, 1x1负载分担]

- id: c09
  title: Lab DHL Active-Active 双活配置与切换测试
  type: case
  source_chapter: "p261-266"
  source_quote: |
    "sw5 (6360-A) -> linkagg lacp agg 8 size 2 actor admin-key 8 / linkagg lacp port 1/1/4 actor admin-key 8
    sw5 (6360-A) -> vlan 57 members linkagg 8 untagged / vlan 20 members linkagg 8 tagged
    sw5 (6360-A) -> dhl 1 / dhl 1 linka linkagg 7 linkb linkagg 8 / dhl 1 vlan-map linkb 30
    sw5 (6360-A) -> dhl 1 admin-state enable / dhl 1 mac-flushing raw
    sw5 (6360-A) -> linkagg lacp agg 7 admin-state disable ... 0/8 tagged forwarding"
  summary: |
    前置：先清端口上的 VLAN 成员再入聚合（否则报错），新建 6360↔6860 的 linkagg 8 并把 57 设为
    untagged 默认、20/30 tagged。DHL：dhl 1 建会话，linkA=linkagg 7（去 6870）、linkB=linkagg 8
    （去 6860），vlan-map linkb 30（VLAN 30 走 B，其余走 A），enable（DHL 口 STP 自动关）+ mac-
    flushing raw。show dhl 1 看 Protected/Active VLAN；ping 中禁用 linkagg 7 验证无缝切换（0/8
    变 forwarding），恢复后等 30 秒 pre-emption 回切。
  tags: [Lab, DHL, active-active, failover]

- id: c10
  title: Lab DHCP Server & DHCP Relay（全局中继）
  type: case
  source_chapter: "p289-293"
  source_quote: |
    "sw7 (6870-A) -> ip dhcp relay destination 192.168.100.102
    sw7 (6870-A) -> ip dhcp relay admin-state enable
    sw5 (6360-A) -> vlan 20 members port 1/1/1 untagged / interfaces 1/1/1-2 admin-state enable
    sw7 (6870-A) -> show ip dhcp relay statistics / Reception From Client : Total Count = 43"
  summary: |
    先 show ip routes + ping 确认两台核心（6870/6860）可达 DHCP 服务器 192.168.100.102；两台分别
    ip dhcp relay destination + admin-state enable（全局模式，Relay Mode=Global）；确认 6360 上
    客户端口正确挂在 VLAN 20/30；客户端改自动获取 IP/DNS 后 show ip dhcp relay statistics 的
    Reception/Tx 计数增长验证中继成功。注：多 DHCP 服务器分网段时可改 per-interface 模式。
  tags: [Lab, DHCP, relay, statistics]

- id: c11
  title: Lab VRRP 主备网关与手动优先级/故障切换
  type: case
  source_chapter: "p305-312"
  source_quote: |
    "sw7 (6870-A) -> ip vrrp 1 interface int_20 / ip vrrp 1 interface int_20 address 192.168.20.254
    sw7 (6870-A) -> ip vrrp 1 interface int_20 admin-state enable
    THE VRRP INSTANCE MUST BE DISABLED BEFORE CHANGING THE PRIORITY
    sw7 (6870-A) -> ip vrrp 1 interface int_20 admin-state disable / priority 150 / admin-state enable"
  summary: |
    6870/6860 各建 VRID 1（int_20，虚 IP 192.168.20.254）与 VRID 2（int_30，192.168.30.254）。
    默认优先级同为 100 时比 router ID，6870 全做 Master；客户端网关改 .254 后 arp -a 可见虚拟
    MAC 00-00-5E-00-01-01。负载分担：改优先级必须先 admin-state disable → priority 150 →
    enable，6870 主备 VLAN 20、6860 主备 VLAN 30。重启 Master 演示 Backup 秒级接管（Become
    Master 计数 +1）。
  tags: [Lab, VRRP, master/backup, 虚拟IP, failover]

- id: c12
  title: Lab QoS：端口默认优先级、信任与策略限速
  type: case
  source_chapter: "p344-350"
  source_quote: |
    "sw5 (6360-A) -> qos port 1/1/1 default 802.1p 7
    sw5 (6360-A) -> qos port 1/1/1 trusted / qos apply
    sw5 (6360-A) -> policy condition client_traffic source vlan 20
    sw5 (6360-A) -> policy action priority_5 802.1p 5 / policy action priority_5 maximum bandwidth 100k
    sw5 (6360-A) -> policy rule rule1 condition client_traffic action priority_5 / qos apply
    C:\> ping -l 65000 192.168.30.xx ... Red Packets = 148"
  summary: |
    先 qos flush 复位。实验一：qos port default 802.1p 7 给未打标流量最高优先级，trusted 口保留
    原值（需 qos apply）。实验二：condition(source vlan 20)+action(802.1p 5)+rule 组合并 apply，
    show active policy rule 看命中计数；加 maximum bandwidth 100k 后普通 ping 仍 Green，大包
    ping -l 65000 出现 Red（TCM 三色丢弃）。收尾演示 policy rule disable / no policy * 清理与
    policy rule log + show qos log 日志法。
  tags: [Lab, QoS, policy, 限速, TCM]

- id: c13
  title: Lab ACL：L2/L3/ICMP 过滤与服务组（HTTP/FTP 分权）
  type: case
  source_chapter: "p369-374"
  source_quote: |
    "sw5 (6360-A) -> policy condition cond1 source mac <Client 5 MAC address>
    sw5 (6360-A) -> policy action DenyTraffic disposition deny / policy rule Filter1 condition cond1 action DenyTraffic
    sw5 (6360-A) -> policy condition ftpfromvlan20 source vlan 20 destination ip-port 20-21 ip-protocol 6
    sw5 (6360-A) -> policy service http1 destination ip-port 80 protocol 6 ... policy service group http from cli http1 http2 http3 http4 http5
    sw5 (6360-A) -> policy port group Userports 1/1/1-2 / qos user-port shutdown bpdu"
  summary: |
    按员工(VLAN20 禁 FTP)/承包商(VLAN30 禁 HTTP) 用例：L2 拒绝按源 MAC；ICMP 过滤按
    ip-protocol 1 + destination ip；FTP 按 destination ip-port 20-21 protocol 6；HTTP 用 5 条
    policy service(80/8080/8000/443/4343) 组成 service group 再入条件，规则 precedence 65535。
    每轮 qos apply 后在 Client5/9 分别验证 FTP/HTTP 可达性差异。安全收尾：policy port group
    UserPorts 防源 IP 欺骗（自动对路由流量生效），qos user-port shutdown bpdu 使用户口收到 STP
    帧即关闭。
  tags: [Lab, ACL, policy, service-group, UserPorts]

- id: c14
  title: Lab Access Guardian（RADIUS+802.1X+UNP）完整认证流
  type: case
  source_chapter: "p397-406"
  source_quote: |
    "sw5 (6360-A) -> aaa radius-server my_radius host 192.168.100.102 key alcatel-lucent
    sw5 (6360-A) -> aaa device-authentication 802.1x my_radius / aaa accounting mac my_radius
    sw5 (6360-A) -> policy list deny_employees type unp enable / policy list deny_employees rules deny_ftp_employee
    sw5 (6360-A) -> unp profile UNP-employee qos-policy-list deny_employees / map vlan 20
    sw5 (6360-A) -> unp port 1/1/1 802.1x-authentication / mac-authentication
    -> aaa test-radius-server my_radius type authentication user employee password password"
  summary: |
    声明 RADIUS（含 802.1x/mac 认证与计费、source-ip Loopback0）；ACL 规则改 no default-list 后
    装入 policy list（type unp）；建 UNP-employee/UNP-contractor 各挂 qos-policy-list 并 map
    vlan 20/30；端口开 802.1x+mac 认证。客户端启用 IEEE 802.1X（PEAP-MSCHAPv2）后 unp user
    flush port 1/1/1 重认证：employee 登录进 VLAN 20+deny_employees 角色、contractor 进 VLAN
    30，show unp user [status|details] 全程可见；RADIUS 无 MAC 条目时该用户 Status=Block。
    aaa test-radius-server 可独立验证服务器连通与 Filter-Id 返回。
  tags: [Lab, Access Guardian, 802.1x, RADIUS, UNP]

- id: c15
  title: Lab LLDP 邻居发现与管理 TLV 增强
  type: case
  source_chapter: "p422-426"
  source_quote: |
    "sw5 (6360-A) -> lldp port 1/1/3 notification enable
    sw5 (6360-A) -> lldp port 1/1/3 tlv management port-description enable
    all -> lldp chassis tlv management system-name enable / system-description enable
    all -> lldp chassis tlv management management-address enable
    sw7 (6870-A) -> show lldp statistics / show lldp remote-system"
  summary: |
    三台交换机互联口逐个开 notification（拓扑变化通知）与 port-description TLV；再在 chassis
    级开 system-name/system-description/system-capabilities/management-address 四个管理 TLV。
    show lldp statistics 看每口 Tx/Rx；show lldp remote-system 对比开 TLV 前后（前：System
    Name=(null)，后：Pod20sw7、管理 IP 192.168.254.7 等）；show lldp local-system 看本机
    30s 发送间隔、TTL×4 等参数。注意 LLDP 只能在端口/槽位/整机级配，不能配在 linkagg 上。
  tags: [Lab, LLDP, TLV, 邻居发现]
```
