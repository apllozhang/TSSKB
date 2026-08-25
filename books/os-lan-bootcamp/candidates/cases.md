# OmniSwitch R6/R8 Bootcamp Issue 25 — Lab 实操案例候选（cases）

> 每个 Case 含完整命令序列与验证步骤，页码来自 fulltext.md `<<<PAGE N>>>`。R6/R8 命令差异已标注。

## Day 1 系统管理

- **C1 硬件信息与运行状态检查（Hardware Information and Operation）**：
  1) `show hardware info`(R6)/`show hardware-info`(R8)、`show microcode`、`show chassis`、`show cmm`、`show power`(R6)/`show powersupply`(R8)、`show fan`、`show health`
  2) 会话管理：`show session config` → `session timeout cli 45`(R6)/`session cli timeout 45`(R8) → `write memory` → 复查；`session prompt default "switchX->"`
  验证：对比配置前后 session 配置输出。<<<PAGE 206-209>>>
- **C2 端口参数配置与计数器观察**：
  1) `interfaces 1/1 duplex full`(R6) / `interfaces 1/1/1 duplex full`(R8)；`speed 1000`；`admin up`(R6)/`admin-state enable`(R8)
  2) 验证：`show interfaces 1/1 status`、`show interfaces 1/1 accounting`、`show interfaces 1/1 counters`（R8 用 1/1/1 三段式）<<<PAGE 210>>>
- **C3 Working/Certified 目录与回滚实操**：
  1) `vlan 2`、`vlan 3`、`vlan 99` → `show vlan`
  2) `reload working no rollback-timeout`(R6)/`reload from working no rollback-timeout`(R8) 重启后确认 vlan 仍在（saved in boot.cfg）
  3) `ls /flash/working` 查看文件
  4) `reload working rollback-timeout 1`(R6) → `reload` 确认 → `show running-directory`
  验证：观察 `WARNING: "sysResetHardwareFlag" flag is SET` 与目录状态 CERTIFY NEEDED。<<<PAGE 215-217>>>
- **C4 配置快照 snapshot 保存与恢复**：
  1) `show configuration snapshot all` → `configuration snapshot all snapall` → `vi snapall`/`more snapall`
  2) `configuration snapshot vlan snapvlan` → `configuration syntax check snapvlan verbose`(R6)/`configuration syntax-check snapvlan verbose`(R8)
  3) 删除：`no vlan 2 3 99`(R6)/`no vlan 2-3`+`no vlan 99`(R8) → `write memory`
  4) 恢复：`configuration apply snapvlan` → `show vlan` 确认 VLAN 回来 <<<PAGE 229-230>>>
- **C5 CLI 帮助/补全/历史练习**：
  `?`、`v?`、`vlan ?`、`vlan port ?`、`sh<tab> vl<tab>`、`session cli-auto-complete-space enable`、`!!` 重复、`!22` 调第 22 条、`!show` 前缀匹配、`show history`(R6)/`history`(R8) <<<PAGE 233-235>>>
- **C6 目录与文件操作**：
  `pwd`、`ls`、`cd /flash/working`、`cd ..`、`cd certified`、`mkdir /flash/dir1`、`cp -r /flash/working/* /flash/dir1`(R6，R8 用 *.* )、`rm -r /flash/dir1`(R6)/`rm -rf`(R8) <<<PAGE 236-237>>>
- **C7 WebView/FTP 安全访问**：
  1) `show aaa authentication` → `aaa authentication http local`、`aaa authentication ftp local`
  2) `ip http ssl`(R6) → `show http`；R8 默认强制 SSL
  验证：浏览器登录交换机 WebView、FTP 连接（默认落 working 目录）。<<<PAGE 239-240>>>
- **C8 用户账户与分区权限**：
  1) `user userread password userread` → `user userread read-only ip`
  2) `user userwriteIP password userwriteIP` → `user userwriteIP read-write ip` → `write memory`
  3) `reload all` 后验证：`show user userread`；`user userread read-only all`/`read-only none`/`read-only domain-layer2` 分级测试 `show vlan`/`show chassis`/`vlan 2` 可用性
  验证：`show user` 列权限域。<<<PAGE 242-246>>>
- **C9 SSH 本地认证**：`show running-directory` → `show aaa authentication` → `aaa authentication ssh local`，用 SSH 客户端登录验证 <<<PAGE 246>>>

## Day 1 堆叠与 VC

- **C10 Stacking R6：Slot-ID 与角色选举（合并多个 stacking lab）**：
  1) 全部交换机 boot.slot.cfg 写 slot 1 同时上电 → `show stack topology` 观察 1001/1002/1003 PASS-THRU DUP-SLOT
  2) `stack set slot 1001 saved-slot 2`、`stack set slot 1002 saved-slot 3`、`stack set slot 1003 saved-slot 4` → `reload all`
  3) 验证：`show stack topology` 显示 1 PRIMARY/2 SECONDARY/3-4 IDLE RUNNING
  变体：按 MAC 法（15 秒内同时上电）、按 uptime 法（依次上电）观察 Primary 归属；`more boot.slot.cfg` 查看 slot 配置。<<<PAGE 251-262>>>
- **C11 Stacking 同步与 takeover**：
  1) 在 Primary 改配置 → `write memory` → `copy working certified flash-synchro` → `takeover`
  2) 验证：`show stack topology` 原 Primary 变 IDLE、Secondary 升 PRIMARY；`show running-directory` 看 Flash SYNCHRONIZED
  3) 拆堆叠：`stack set slot 1 mode standalone`、`stack set slot 2 mode standalone`、`rm boot.slot.cfg`、`cp labinit/boot.cfg working`、`cp labinit/pre_banner.txt switch`、`reload working no rollback-timeout` <<<PAGE 264-286>>>
- **C12 MAC Retention 配置**：`mac-retention status enable` → `mac-retention dup-mac-trap enable` → takeover 后 `show mac-retention status` 显示 MAC address source: Retained；`mac release` 主动释放 <<<PAGE 273>>>
- **C13 Virtual Chassis（R8）实验**：6900 出厂 auto-VC 流程：boot 提示 "Do you want to disable auto-configurations [Y/N]?" 输 N → 自动 VFL/Chassis ID 协商 → `show stack topology` 类命令查看 VC；禁 VC：`no virtual-chassis vf-link 0 member 2/1` 后逐口删 `no virtual-chassis vf-link 0`；恢复 `reload from virtual_dir no rollback-timeout` <<<PAGE 937-940, 927>>>
- **C14 诊断工具综合实验（Switch maintenance & Diagnostics）**：
  1) `swlog output console`/`swlog output flash`/`swlog output socket ipaddr 168.23.9.100`
  2) `command-log enable`、`show command-log`
  3) sFlow：`ip managed-interface Loopback0` … `sflow receiver 1 name Server1 address 192.168.1.100`、`sflow sampler 1 1/1-24 receiver 1 rate 512`、`sflow poller 1 1/1-24 receiver 1 interval 10` → `show sflow receiver/sampler/poller`
  4) 验证：`interfaces 1/1/1 admin-state enable` 后 `show interfaces 1/1/1 counters` 递增 <<<PAGE 326-356>>>

## Day 2 VLAN / 聚合 / STP / DHL / IP / LLDP

- **C15 VLAN 创建与静态指派（VLAN lab）**：
  1) `show vlan`（初始仅 VLAN 1，4094 VCM IPC）
  2) `vlan 20` → `vlan 20 port default 1/2`(R6)/`vlan 20 members port 1/1/2 untagged`(R8) → `interfaces 1/2 admin up`/`interface 1/1/2 admin-state enable`
  3) 验证：`show vlan 20 port`、`show vlan members port 1/1/1`、`show ip interface`
  要点：无成员 VLAN oper 状态 inactive。<<<PAGE 385-390>>>
- **C16 VLAN 规则与 mobile 口（动态 VLAN）**：
  `vlan 2 ip 10.1.20.0 255.255.255.0`、`vlan 3 mac-range 00:80:9f:00:00:00 00:80:9f:ff:ff:ff`、`vlan port mobile 1/1`、`vlan 3 mobile-tag enable` → `show vlan rules` 验证 ip-net/mac-range 命中 <<<PAGE 370-382>>>
- **C17 动态链路聚合 LACP（Link Aggregation lab）**：
  1) 6450: `lacp linkagg 5 size 2 actor admin key 5`；6860: `linkagg lacp agg 5 size 2 actor admin-key 5`
  2) 挂端口：6450 `lacp agg 1/11 actor admin key 5`+`lacp agg 1/12 actor admin key 5`；6860 `linkagg lacp port 1/1/23-24 actor admin-key 5`
  3) 激活：`interfaces 1/11-12 admin up` / `interfaces 1/1/23-24 admin-state enable`
  4) 验证：`show linkagg`（Oper State UP，Att/Sel 2/2）、`show linkagg agg 5`（Primary Port、LACP actor/partner Oper Key=5）；ping 对端 VLAN1 地址测连通；down 一个成员口看 ping 不丢 <<<PAGE 404-406>>>
- **C18 802.1Q 跨交换机多 VLAN 桥接（802.1q lab）**：
  1) 四台交换机 `vlan 20 30` 建 VLAN 并配 IP 接口（如 `ip interface int_20 address 192.168.20.7/24 vlan 20`）
  2) 打标签：R6 `vlan 20 30 802.1q 3/4`；R8 `vlan 20 members port 1/3/4 tagged`
  3) 验证：`show vlan 2 port`/`show vlan members`、跨交换机 ping 各 VLAN 网关 <<<PAGE 407-411, 380>>>
- **C19 静态聚合实验（扩展，含删除报错）**：
  1) 6860: `linkagg static agg 5 size 2` → `linkagg static port 1/1/23-24 agg 5`；6450: `static linkagg 5 size 2` → `static agg 1/11 agg num 5`
  2) `show linkagg`/`show linkagg agg 5`/`show linkagg port`
  3) 删除顺序：先 `no static agg no 1/11`、`no linkagg static port 1/1/23-24` 再删组；直接删非空组报 `ERROR: LAERR53 Static aggregate not empty deletion failed` <<<PAGE 999-1002>>>
- **C20 STP 根桥与端口状态实验（STP lab）**：
  1) 默认验证：`show spantree`（RSTP、priority 32768）、`show spantree ports` 看 FORW/BLK/BACK
  2) 改根：`bridge 1x1 vid priority`/`spantree vlan instance {port|linkagg} priority`
  3) 观察根路径开销：GE 默认 cost 4 推断根口位置
  4) 1x1 负载分担：6860-A 为 VLAN20 根、6860-B 为 VLAN30 根（`show spantree vlan 1`、`show spantree port forwarding/blocking`）<<<PAGE 418-464>>>
- **C21 MSTP 双实例负载分担（MSTP lab，双交换机对配置合并）****：
  1) 两台同配：`bridge mode flat` → `bridge protocol mstp` → `bridge mst region name myregion` → `bridge mst region revision level 1` → `bridge cist protocol mstp` → `bridge msti 1 vlan 1-15` → `bridge msti 2 vlan 16-20`（R8 对应 spantree mst/msti 语法）
  2) A 机：`bridge cist priority 4096`、`bridge msti 1 priority 4096`、`bridge msti 2 priority 8192`、`bridge msti 1 1/1 priority 1`、`bridge msti 2 1/1 priority 15`…；B 机对调（8192/8192/4096，端口优先级互换）
  3) 验证：`show spantree mst port 1/1`/`1/11`（A: MST1 ROOT/FORW VLAN1-15、MST2 ALT/BLK；B 相反）、`show spantree msti 3`、`show spantree mst region`
  注意：切 MSTP 会 reset flat 优先级与路径开销。<<<PAGE 444-472>>>
- **C22 DHL Active-Active 实验**：
  1) 建 VLAN 并双上行打标签：`vlan 20`、`vlan 30`、`ip interface int_20/int_30 …`、`vlan 20 802.1q 1/3`+`vlan 20 802.1q 1/4` 等
  2) 建会话：`dhl num 1` → `dhl num 1 linka port 1/3 linkb port 1/4` → `dhl num 1 vlan-map linkb 30` → `dhl num 1 admin-state enable`
  3) 验证：`show dhl`、`show dhl num 1`（Protected Vlans 1 20 30；LinkA Active 1 20 / LinkB Active 30）、`show vlan 20 port`（1/4 dhl-blocking）
  4) 故障切换：`dhl num 1 mac-flushing raw` → 客户端 ping –t 期间 `interfaces 1/1/3 admin-state disable`，观察是否丢包 <<<PAGE 487-489>>>
- **C23 DHCP Server & DHCP Relay 实验（IP lab）**：
  1) 客户端网关可达性预检（每 client ping 网关）
  2) 中继：`ip helper address {Server}`（可多地址/按 vlan）；`ip udp relay DNS`
  3) 验证：`show ip helper`、客户端获取地址
  相关：Loopback0 配置 `ip interface Loopback0 address <ip>`。<<<PAGE 492-499, 743>>>
- **C24 LLDP 实验与 MED 网络策略**：
  1) `lldp 1/3 notification enable`（R8: `lldp port 1/1/4 notification enable`）；`lldp 1/3 tlv management port-description enable`
  2) 验证：`show lldp statistics`、`show lldp remote-system`（邻机系统名/能力/VLAN）、`show lldp 1/9 config`
  3) 话机策略：`vlan 10`、`vlan port mobile 1/10`、`vlan 10 mobile-tag enable`、`lldp 1/10 tlv med network-policy enable`、`lldp network-policy 1 application voice vlan 10 l2-priority 7 dscp 46`、`lldp 1/10 med network-policy 1` → `show lldp remote-system med inventory` 看话机型号/固件 <<<PAGE 511-520>>>

## Day 3 VRRP / QoS / ACL / AG / PoE

- **C25 VRRP 主备与抢占实验**：
  1) 6860-A/B 同配：`ip vrrp 1 interface int_20` → `ip vrrp 1 interface int_20 address 192.168.20.254` → `ip vrrp 1 interface int_20 admin-state enable`（vrrp2/VLAN30 同理）
  2) 验证：`show ip vrrp 1`（Priority 100、Virtual MAC 00-00-5E-00-01-01）；`show ip vrrp statistics` 显示 A Master、B Backup（同优先级比 router-id）
  3) Tracking：`ip vrrp track 3 admin-state enable priority 30 port 1/1/3` → `ip vrrp 1 interface int_20 track-association 3`；断跟踪口后优先级 100-30=70 让位
  4) Group：`ip vrrp group 2` + `group association` 统一参数 <<<PAGE 529-537>>>
- **C26 QoS 端口调度与队列观察**：
  1) `qos port 1/1 monitor` → `show qos queue 1/9` → `qos stats reset egress`/`qos stats interval`
  2) 调度：`qos port <slot/port> servicing mode wrr` 或 `qos default servicing mode wrr`
  验证：`show qos queue` 看各 CoS 队列计数 <<<PAGE 547, 578>>>
- **C27 QoS 标记与限速策略（QoS lab）**：
  1) `policy condition Traffic destination port 3/2 802.1p 4` → `policy action SetBits 802.1p 7` → `policy rule Rule2 condition Traffic action SetBits`
  2) L3 优先：`policy condition cond3 source ip 10.10.2.3` → `policy action action2 priority 7` → `policy rule my_rule condition cond3 action action2`
  3) 验证：`show active policy rules`、`show policy classify l3 source ip … destination ip …`
  4) 管理：`qos reset` 清空策略、`show policy condition c1`/`no policy condition c1` <<<PAGE 574-593>>>
- **C28 Egress 策略列表**：`policy list eggress1 type egress rules rule1 rule2 rule3` → `show active policy rules` <<<PAGE 575>>>
- **C29 Auto-QoS 话机信任**：`policy mac group alaPhones` → `qos phones [priority | trusted]` → `qos nms priority` <<<PAGE 581-582>>>
- **C30 ACL L2 拒绝主机**：`qos default bridged disposition accept` → `policy condition Cond-Deny-Host1 source mac D4:85:64:EC:33:EF source vlan 5` → `policy action Act-deny-Host1 disposition deny` → `policy rule Rule-Deny-Host1 … log` → `qos apply`；`show qos log` 看命中 <<<PAGE 612>>>
- **C31 ACL L3 网段拒绝与白名单**：
  1) 拒绝：`policy network group netgroup1 192.168.82.0 mask 255.255.255.0 192.60.83.0` → condition/action deny → `policy rule lab_rule1 … precedence 65535` → `qos apply`
  2) 白名单：`qos default routed disposition deny` + 两条精确 accept 规则（allow-host1 / subnet-100）→ `qos apply` <<<PAGE 613-614>>>
- **C32 ACL 服务组与监控**：`policy service telnet1 protocol 6 destination ip port 23`、`policy service ftp1 destination tcp port 21`、`policy service group tel-ftp telnet1 ftp1`、`policy mac group macgrp2 …`、`policy port group visitor_ports 2/1 3/1-24` → `show policy network group`/`service`/`mac group`/`port group`；规则调序：`policy rule telnet_rule precedence 1000 condition c1 action accept log` <<<PAGE 621-622>>>
- **C33 Access Guardian 部署（AG lab）**：
  1) 端口：R6 `vlan port mobile 3/1` + `vlan port 3/1 802.1x enable`；R8 `unp port 1/1/1 port-type BRIDGE`
  2) UNP 策略列表：`policy list list_name type unp`、`aaa user-network-profile name profile_name policy-list-name list_name`(R6) / `unp profile profile_name qos-policy-list …`(R8)、`unp profile profile_name map vlan vlan_id`
  3) 分类规则：R8 `unp classification mac-address 00:11:22:33:44:55 port 1/1/5 PROFILE1 Pr1`、`unp classification mac-oui 00:11:22 PROFILE1 myProfile1`、`unp classification lldp med-endpoint ip-phone p PROFILE1 myProfile1`、`unp classification authentication-type 802.1X/MAC …`；R6 对应 `aaa classification-rule mac-address … user-network-profile name …`
  4) Radius 档案：`aaa profile ap-1` → `aaa profile ap-1 device-authentication mac rad1 rad2` / `device-authentication 802.1x rad1 rad2` → `unp port 1/1/5 aaa-profile ap-1`（可按 linkagg/范围）
  5) 验证：`unp domain 2 description grp2`、`aaa test-radius-server My_radius type authentication user employee password password` 联调；`show unp port` 类命令 <<<PAGE 642-677>>>
- **C34 UNP Location/Period 策略**：`system location <string>`、`unp policy validity-location "Alcatel" port 1/1/10`；`unp policy validity-period "Office-Time" days MONDAY time-zone CET hours 9:00 to 17:00` <<<PAGE 649-650>>>
- **C35 PoE R6 管理实验**：
  1) `show power` → `lanpower start 1`（PoE 默认 oper down 需手工启动）
  2) 端口：`lanpower start 1/2`、`lanpower 1/9 power 18000`、`lanpower 1/22 priority critical`、`lanpower 1 capacitor-detection enable`、`lanpower 1 priority-disconnect enable`
  3) 验证：`show lanpower 1`（各口 mW、优先级、预算余量）<<<PAGE 700-703>>>
- **C36 PoE R8 管理实验**：`show powersupply` → `lanpower slot 1/1 service start` → `lanpower port 1/1/1 admin-state enable`、`lanpower port 1/1/24 power 18000`、`lanpower port 1/1/6 priority critical`、`lanpower slot 1/1 maxpower 400`、capacitor-detection/priority-disconnect → `show lanpower slot 1/1` <<<PAGE 705-708>>>
- **C37 EEE 节能**：`interfaces 1/1 eee enable` <<<PAGE 710>>>

## Day 4 路由与安全

- **C38 RIP 骨干实验（含重分发/版本/认证 add-on）**：
  1) 预备：骨干 VLAN 217/218/278 + linkagg 18（`linkagg lacp agg 18 size 2 actor admin-key 18` + 挂口）+ IP 接口
  2) `ip load rip` → `ip rip admin-state enable` → 按接口 `ip rip interface int_217` + `admin-state enable`
  3) 验证：`show ip rip interface`（Send v2/Recv both）、`show ip rip peer`、`show ip rip routes`
  4) 重分发：`ip route-map rip_1 sequence-number 50 action permit` + `match ip-address 0.0.0.0/0` → `ip redist local into rip route-map rip_1 admin-state enable`、`ip redist static into rip …`
  5) Add-on：send-version/recv-version 切 v1/v2、metric、auth-type MD5；timers `ip rip update-timer 45`/`invalid-timer 270`/`garbage-timer 180`/`holddown-timer 10` <<<PAGE 733-745, 726-731>>>
- **C39 OSPF 骨干与区域实验（OSPF lab）**：
  1) `ip load ospf` → `ip router router-id 192.168.254.1` → `ip ospf area 0.0.0.0` → 各接口 `ip ospf interface int_217` + `area 0.0.0.0` + `admin-state enable` → `ip ospf admin-state enable`
  2) 验证：`show ip ospf`、`show ip ospf area 0.0.0.0`、`show ip ospf interface`、`show ip routes`、`show ip ospf routes`、`show ip ospf lsdb`、`show ip ospf neighbor`
  3) 保存：`write memory` + `configuration snapshot all save-ospf-backbone`
  4) 重分发：localIntoOspf/staticIntoOspf route-map（match 192.168.100.0/24 与 0.0.0.0/0）→ `show ip ospf ext-lsdb`
  5) 认证：simple（`auth-type simple`+`auth-key alcatel`）与 MD5（`md5 1`+`md5 1 key alcatel`）后 `show ip ospf neighbor` 重建邻接
  6) 偏好：`show ip route-pref` → `ip route-pref rip 8` <<<PAGE 779-792, 768-769>>>
- **C40 虚链路与外部聚合（配置型）**：`ip ospf virtual-link 2.2.2.2 192.168.10.2`（transit area + 对端 router-id）；ASBR 聚合 `ip access-list extip address 150.215.0.0/16 action permit redist-control aggregate` + route-map redist rip into ospf <<<PAGE 763, 768>>>
- **C41 LLDP Rogue Detection 配置**：`lldp 1/1 trust-agent enable`、`lldp 1/1 trust-agent violation-action trap|shutdown` → 验证 `show lldp trusted remote-agent`、违规后 `interfaces <slot>/<port> clear-violation-all` <<<PAGE 802>>>
- **C42 Learned Port Security 实验**：
  1) `port-security 1/1 enable` → `port-security max-filtering 0` → `port-security 1/1 violation shutdown` → `port-security convert-to-static enable`（当前 MAC 固化）
  2) 换设备触发违规：`show port-security`（violation RESTRICT 默认）、300 秒自动清或 `port-security slot/port release`
  3) 进阶：`port-security <s/p> maximum num`、`mac-range low high`（8 段）、`learn-trap-threshold num` <<<PAGE 805-809, 850-852>>>
- **C43 PBR 防火墙重定向**：
  1) `policy condition Traffic10 source ip 10.10.0.0 mask 255.255.0.0` → `policy action Firewall permanent gateway ip 192.168.99.254` → `policy rule Redirect_All …`
  2) 回程防环：`policy condition TrafficFromFW source IP 10.10.0.0 … source port 2/1` → action To_Internet permanent gateway IP 192.168.10.254 → rule Redirect_Internet <<<PAGE 813-814>>>
- **C44 UserPorts 防欺骗与阻断**：`policy port group UserPorts 1/1-24 2/1-24 3/1 4/1` → `qos user-port filter spoof rip ospf bgp`；病毒端口：`policy service tcp135/tcp445/udp137` + DropServices 组；port-disable 动作 + `interfaces violation-recovery-time <num>`、`violation-recovery-trap enable`；`show qos log` 查 "Spoofed traffic triggered user-port shutdown" <<<PAGE 816-818>>>
- **C45 ARP 防毒与加固**：`ip dos arp-poison restricted-address 192.168.100.152` → `show ip dos arp-poison`（攻击计数）；`ip directed-broadcast off`、`no ip service telnet`、`no ip service port 23` <<<PAGE 819-824>>>
- **C46 DHCP Snooping + Option 82 + Port Mapping 组合**：
  1) `ip helper dhcp-snooping enable` → `ip helper dhcp-snooping vlan 24` → 端口角色 `ip helper dhcp-snooping port slot/port [block/trust/client-only]`
  2) `ip helper dhcp-snooping option-82 data-insertion format ascii {base-mac|system-…}`；验证 `show ip helper`
  3) 映射：`port mapping 1 user-port 1/1-2 network-port 3/2` → `port mapping 1 dynamic-proxy-arp enable` → `port mapping 1 enable` → `show port mapping 1 status`、`show ip dynamic-proxy-arp` <<<PAGE 829-839>>>
- **C47 VRF 创建与路由泄漏**：
  1) `vrf create IpOne` → `vrf IpOne` 进上下文 → `ip interface intf100 address 100.1.1.1/24 vlan 100` → `show vrf`、`show ip interface`；`vrf default` 返回
  2) 泄漏：`ip route-map R1 action permit` + `match protocol static` → `ip export route-map R1`；`ip route-map R2 match protocol static` → `ip import vrf V1 route-map R2` → `ip route-pref import 100` <<<PAGE 859-864>>>

## Day 5 组播 / ERP / IFAB

- **C48 组播交换 IPMS 实验（Multicast switching lab）**：
  1) `show ip multicast` 确认默认 disabled → `ip multicast admin-state enable`(R8) → `ip multicast querying enable` → `ip multicast querier-forwarding enable`
  2) 验证：客户端加组后 `show ip multicast group`（端口级成员）、`show ip multicast neighbor`、`show ip multicast forward`（入/出端口表）；确认仅必要端口转发而非全 VLAN 洪泛 <<<PAGE 877-883, 916-918>>>
- **C49 PIM-SM 实验**：
  1) RP/BSR 侧（6900）：`ip load pim` → `ip pim sparse admin-state enable` → 接口 `ip pim interface int_217/int_218/int_110` → `ip pim cbsr 192.168.110.1` → `ip pim candidate-rp 192.168.110.1 231.1.1.0/24`
  2) 验证：`show ip pim cbsr`、`show ip pim candidate-rp`、`show ip pim neighbor`、`show ip pim group-map`、`show ip pim groute 225.0.0.101`、`show ip pim sgroute 192.168.100.100 225.0.0.101`、`show ip mroute` <<<PAGE 908-913, 923>>>
- **C50 ERP 环网实验（6560x2 + 6900x2）**：
  1) （可选先拆 6900 VC：reload from working → 删 vf-link）
  2) 各节点 `vlan 50 name "Ring1"`（Service VLAN，承载 R-APS/CCM）+ `vlan 60 name "subnet60"`（Protected VLAN）；ring 口 tag 50 untag 60
  3) RPL owner（6900-A）：`erp-ring 1 port1 1/3 port2 2/1 service-vlan 50 level 2` → `erp-ring 1 rpl-node port 1/3` → `erp-ring 1 wait-to-restore-timer 1` → `erp-ring 1 enable`；其余节点仅 ring 定义+enable
  4) 激活各 ring 口 `interfaces … admin-state enable`
  5) 验证：`show erp`（Ring State Pending，rpl 标记）；`show erp statistics ring 1`；ping –t 中断链路观察 Protected 切换与恢复 WTR；结束 `reload from virtual_dir` 恢复 VC <<<PAGE 926-932>>>
- **C51 Intelligent Fabric（Auto-fabric）实验**：
  1) `show auto-fabric config` → `auto-fabric discovery start` → `auto-fabric admin-state enable` → `auto-fabric config-save admin-state enable`
  2) 验证：`show linkagg port`（Auto-LACP agg 127 attached）、`show vlan`（Auto-MVRP 动态 VLAN，type dyn）、MVRP 状态 `show mvrp port 1/1/4`（Discovery Status Enabled）<<<PAGE 943-951, 27306-27330>>>

## 扩展：升级 / MVRP / SLB / MacSec / BGP / ISIS

- **C52 代码升级实验（Installing & Upgrading Code）**：
  1) `show aaa authentication` → `aaa authentication ftp local` 开 FTP
  2) `show microcode working`/`show microcode certified` 对比版本
  3) FTP 上传镜像（binary 模式）至 /flash/working
  4) `reload working no rollback-timeout`(R6)/`reload from working no rollback-timeout`(R8) → 验证后 `copy working certified` <<<PAGE 962-965>>>
- **C53 MVRP 实验**：
  1) 前置：`spantree mode flat`（R6 `bridge mode flat`）→ `mvrp enable` → 端口 `mvrp port 1/3 enable`、`mvrp linkagg 5 enable`
  2) 限额：`mvrp maximum vlan 150`(6450)/`mvrp maximum-vlan 150`(6860)
  3) 动态 VLAN：6450-B `vlan 40` + `vlan 40 802.1q 1/3`+`1/4` → 6860 `show vlan` 出现 type dyn 的 VLAN 40
  4) 验证：`show mvrp port 1/1/4 statistics`（Join/Empty 计数）、`show mvrp port 1/1/4`（timers）、`show mvrp port 1/1/4 last-pdu-origin`；结束回 1x1：`spantree mode per-vlan`/恢复 flat 前状态 <<<PAGE 968-971>>>
- **C54 SLB 实验（VIP/WRR/探针三合一）**：
  1) 基础：`ip slb admin-state enable`(R8) → `ip slb cluster Web vip 128.241.130.204` → `ip slb server ip <ip> cluster Web`（多台）；服务器 loopback 配 VIP
  2) WRR：`ip slb server ip 192.168.100.99 cluster cl1 weight 1` … weight 3、备份机 weight 0 → `show ip slb cluster WorldWideWeb server …`
  3) QoS Condition 集群：`policy condition cond1 source port 1/1 destination tcp port 80` → `ip slb cluster Firewall condition cond1 L3`（或 L2）
  4) 探针：`ip slb probe http_test http` → `ip slb probe http http_test period 10` → server 挂 probe http_test <<<PAGE 976-987, 995>>>
- **C55 MACsec 静态 SA 配置（示例模式）**：接口下 `interface 1/1/25 macsec sci-tx key-chain …`/`sci-tx encryption`/`sci-rx 0x2 …` 成对配置两端密钥链；删除按 `no interface 1/1/25 macsec sci-tx key-chain` 等逐项 <<<PAGE 1049>>>
- **C56 BGP 基本邻接与策略**：
  1) `ip router router-id` → `ip load BGP` → `ip bgp status enable` → `ip bgp autonomous-system 100` → `ip bgp neighbor 100.10.1.1` + `remote-as` + `status enable`（可 `md5 key`）
  2) `ip bgp neighbor 100.10.1.1 update-source Loopback0`、`ebgp-multihop`
  3) 验证：`show ip bgp neighbors`
  4) 策略：`ip bgp policy aspath-list/prefix-list/community-list … action permit|deny`；偏好 `ip route-pref BGP 8` <<<PAGE 1080-1088>>>
- **C57 IS-IS 基本配置**：`ip load isis` → `ip isis admin-state enable` → `ip isis area-id 49.0001` → `ip isis activate-ipv4` → `ip isis vlan 5 address-family v4 admin-state enable`；层级 `ip isis vlan 10 level-capability level-1/2`；验证 `show isis status`、`show ip isis adjacency`、`show ip isis route`、`show ip isis spf` <<<PAGE 1105-1106>>>
