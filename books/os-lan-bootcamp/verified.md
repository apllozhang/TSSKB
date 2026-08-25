# Verified 候选（V1 原文真实性核对 + V2/V3 抽查）

## cases

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

## counter-examples

## 硬件/供电
- **X1 6860 与 6850E 不可共用一台 BPS**：可各自接同一型号 BPS，但不能共享。原句："OS6860 and OS6850E sharing one BPS is not supported" <<<PAGE 58, 61>>>
- **X2 N+1 备电只防电源模块故障**：SINGLE 备份不防市电线路断电。原句："Protects against switch primary PSU failure not against AC power line failure" <<<PAGE 63>>>
- **X3 BPS 一次只备份一台交换机**：原句："BPS can backup only one switch at a time" <<<PAGE 63>>>
- **X4 6450-10 只能与 6450-10 堆叠**：不能与其他 6450 机型混堆。原句："OS6450-10 switches can only be stacked with other OS6450-10 switches." <<<PAGE 253>>>
- **X5 6350-10/P10 不支持堆叠**：原句："(Stacking OS6350-10/P10 switches is not currently supported.)" <<<PAGE 252>>>
- **X6 6450-10/P10 不支持远程堆叠**：原句："OS6450-10 and 6450-P10 switches do not support remote stacking." <<<PAGE 253>>>
- **X7 6860E-P24Z8 2.5G 端口成对配置**：自动协商只到 1G，2.5G 须手工且成对。原句："Auto-neg supported for 10/100/1000 Mbps only. Manual configuration to choose between 1G & 2.5G speeds" <<<PAGE 55>>>
- **X8 6860E 电源不可混插**：600W 与 920W 不能混用。原句："Both 600W & 920 W Supported; Default : 600W; No Mix-n-match" <<<PAGE 55>>>
- **X9 6860 专用 VFL 口不能当普通口**：原句："Dedicated VFL ports (2 x 20G) - Cannot be used as normal ports" <<<PAGE 300>>>
- **X10 6900-T 固定 10GBase-T 口不能作 VFL**：须加扩展模块。原句："Fixed 10 Gbase-T not supported" <<<PAGE 299>>>
- **X11 EMP 口是 RCD 的硬前提**：6860 无 EMP 口故不能使用 RCD 防脑裂。原句："Limitation: EMP port mandatory to use this feature - For example, an OmniSwitch 6860 doesn't have such port!" <<<PAGE 306>>>
## 系统/配置管理
- **X12 certified 目录不可直接保存**：从 certified 启动时改动无法 write memory，也无法跨目录移动文件。原句："Changes cannot be saved directly to the Certified directory / changes made to the switch cannot be saved and files cannot be moved between directories" <<<PAGE 131, 145, 148, 218>>>
- **X13 R6 无 modify running-directory 命令**：原句："In release 6, the \"modify ...\" command cannot be used." <<<PAGE 224>>>
- **X14 FTP 默认连 working 目录且认证默认关**：须 `aaa authentication ftp local`。原句："By default, an FTP session connects to the 'working' directory / FTP Authentication has to be enabled" <<<PAGE 136, 964>>>
- **X15 USB 默认禁用；移除前必须 usb disable**：原句："USB support is disabled by default / CAUTION: Do usb disable before removing usb" <<<PAGE 138, 225>>>
- **X16 USB backup 与 auto-copy 互斥**：原句："Back-up cannot be enabled if auto-copy is enabled and auto-copy cannot be enabled if back-up is" <<<PAGE 141>>>
- **X17 admin 账户仅 console 可改密码**：原句："By default, access only allowed through console port / Cannot be modified except for password" <<<PAGE 176>>>
- **X18 所有远程访问默认关闭**：仅 console 恒开。原句："Access through console (local) port is always enabled / By default all remote access is disabled" <<<PAGE 184>>>
- **X19 新建 end-user profile 默认无任何权限**：删除仍被用户引用的 profile 会导致该用户无法登录。原句："By default, new profiles do not allow access to any ports or VLANs / If a profile is deleted, but the profile name is still associated with a user, the user will not be able to log into the switch" <<<PAGE 182>>>
- **X20 R8 WebView 默认强制 SSL，R6 不强制**：原句："by default SSL is forced on R8 omniswitches but not on R6 ones" <<<PAGE 240>>>
- **X21 *.img 文件勿移动/删除**：原句："Be careful not to move or delete any important files such as the *.img files." <<<PAGE 237>>>
- **X22 无 boot.cfg 的目录在 write memory 时会自动创建 boot.cfg**：原句："If the directory does not contain a boot.cfg file, note that it will be created when the write memory" <<<PAGE 216>>>
- **X23 RCL/自动配置限制**：无 IPv6 支持、路径 63/255 字符限制、无 EMP 支持、开机变慢。原句："Increased Boot-up time / No EMP port supported / Filename and path length limited to 63 and 255 characters / No IPv6 support" <<<PAGE 157>>>
- **X24 远程实验虚拟机键盘布局**：原句："All VM are configured with an English US keyboard, your current keyboard layout is not take into account." <<<PAGE 203>>>
## 堆叠/VC
- **X25 堆叠不超过 8 台且版本必须一致**：原句："Never attempt to operate more than 8 switches in a single stack / Make sure all switches are running the same software version" <<<PAGE 261>>>
- **X26 无法登录 Idle/Pass-Through 单元**：原句："It is not possible to log on Idle switches (nor pass-through)" <<<PAGE 262>>>
- **X27 Secondary 上仅允许 takeover 等极少数命令**：原句："Secondary: no configuration allowed" <<<PAGE 262>>>
- **X28 槽号必须唯一且建议从 1 连续分配**：原句："it is important that each element in a stack is assigned a unique slot number. Do not assign…" <<<PAGE 279>>>
- **X29 takeover 前必须完成同步**：原句："A synchronization has to be done before takeover" <<<PAGE 260>>>
- **X30 reload all 可能落在 certified 分区**：原句："/!\ It can be on 'Certified' partition!" <<<PAGE 260>>>
- **X31 VC 写配置在拓扑变化时受保护警告**：原句："The command write memory is protected by issuing a warning to prevent or warn purging the configuration" <<<PAGE 317>>>
- **X32 VC 仅限 AOS R8 且须同机型**：原句："Restrictions: AOS R8 Only / Same type of switches in a Virtual Chassis" <<<PAGE 290>>>
- **X33 VC 脑裂双 Master 风险**：VFL 断而两机存活会出现两个 Master 同 IP 同 MAC。原句："having 2 Masters can results in problems, because the 2 switches are using the same IP and MAC address in the network" <<<PAGE 305>>>
## 诊断
- **X34 command.log 在启用期间不可删**：原句："Cannot be deleted while command logging is enabled" <<<PAGE 334>>>
- **X35 端口镜像与端口监控不能同 NI**：原句："Port mirroring and monitoring cannot be configured on the same NI" <<<PAGE 339, 342>>>
- **X36 swlog socket 需先配 Loopback0**：原句："Loopback0 have to be configured" <<<PAGE 326>>>
- **X37 镜像会话目标端口容量必须一致**：原句："Port requirements - must be of identical capacity" <<<PAGE 337>>>
## 二层（VLAN/LAG/STP/DHL/MVRP）
- **X38 VLAN 1 不可删除**：原句："This VLAN CANNOT be deleted, but it can be disabled if so desired." <<<PAGE 385>>>
- **X39 管理状态 down 的接口不响应 ping**：原句："down, it cannot be connected to, will not reply to PING requests nor will it be advertised in any router" <<<PAGE 387>>>
- **X40 802.1Q 标签不适用于 mobile 口（用 Mobile Tag）**：原句："VLAN Mobile Tag … Not supported on mobile ports（802.1Q 列）" <<<PAGE 383>>>
- **X41 一个端口只能属于一个聚合组；组非空不能删**：原句："One port can only belong to one link aggregation / you cannot delete a link aggregation group if there" <<<PAGE 395, 1001>>>
- **X42 组播默认只走聚合主端口**：除非开 non-ucast 哈希。原句："Multicast traffic is by default forwarded through the primary port of the Link Aggregation Group" <<<PAGE 402, 887>>>
- **X43 1x1 与 MSTP 不能同时配置**：MSTP 须 flat 模式。原句："1X1 and MSTP cannot be configured at the same time; and the switch must be configured in flat Spanning Tree mode." <<<PAGE 471>>>
- **X44 切换 MSTP 会重置 flat 优先级与路径开销**：原句："WARNING: Changing to MSTP(802.1s) resets flat bridge priority and path" <<<PAGE 471>>>
- **X45 MSTP 链路须承载实例全部 VLAN**：否则不承载任何。原句："Ensure that a link carries all of the VLANs mapped to an instance, or do not carry any VLANs at all for this instance" <<<PAGE 444>>>
- **X46 MSTP 32bit 开销与 802.1d/w 默认 16bit 不兼容注意**：原句："16-bit path cost value that 802.1d/802.1w use by default." <<<PAGE 471-472>>>
- **X47 PVST+ 端口必须 1x1 模式**：原句："Ports must be configured in 1x1 mode" <<<PAGE 434>>>
- **X48 DHL 每机仅一会话；DHL 口上 STP 自动禁用**：原句："Only one session per switch is allowed / Spanning Tree is disabled on all the DHL enabled ports" <<<PAGE 478, 488>>>
- **X49 MVRP Enhanced 不支持 6250/6450**：DHL MAC 冲刷只能选 RAW。原句："the MVRP Enhanced is not supported on AOS OmniSwitches 6250 & 6450" <<<PAGE 479>>>
- **X50 MVRP 须 STP flat 模式且不能配在 mirror/mobile/VPLS 口**：原句："MVRP can be configured only on fixed, 802.1 Q and aggregate ports. It cannot be configured on mirror, mobile, VPLS Access, and VLAN Stacking User ports." <<<PAGE 968>>>
- **X51 MVRP 调低动态 VLAN 上限需重启 MVRP 生效**：原句："the new configuration will take effect only after the MVRP is disabled and enabled again" <<<PAGE 969>>>
## 三层与服务
- **X52 LLDP 不能按 linkagg 配置**：原句："LLDP is configured at port level (or NI or chassis), but not at linkagg level." <<<PAGE 519>>>
- **X53 VRRP 与 HSRP 不兼容**：原句："Not compatible with HSRP" <<<PAGE 524>>>
- **X54 VRRP 备份路由器优先级应彼此不同**：避免同时升主。原句："It is important to define different priorities on the backup routers." <<<PAGE 527>>>
- **X55 QoS 默认放行一切未匹配流量（accept）**：配错 disposition 可能全断。原句："Denies all bridged, routed or multicast traffic by default（配 deny 后）/ By default, bridged, routed, and multicast flows that do not match any policies are accepted" <<<PAGE 558, 586, 620>>>
- **X56 QoS phones/nms 信任仅前 8 个接口**：按 ifIndex 顺序。原句："Only supported on the first 8 interfaces in order of creation. Defined by their ifIndex" <<<PAGE 582>>>
- **X57 condition/action 被规则引用时不可删；参数互斥**：原句："an action cannot be deleted if it is currently being used by a policy rule… some action parameters are only supported with particular condition parameters" <<<PAGE 593-594>>>
- **X58 交换端口默认不信任标记**：原句："By default, switched ports are not trusted." <<<PAGE 590, 598>>>
- **X59 Egress 过滤仅限特定平台/方向**：原句："Egress Filtering is only supported on" <<<PAGE 575>>>
- **X60 6450 可对 UNP 直接限速，R8 不行**：原句："On the 6450 we can apply a bandwidth restriction directly to the UNP, this is not possible in release 8" <<<PAGE 676>>>
- **X61 Captive Portal/Profile/Block 是终结策略**：后不能跟其他策略。原句："Some policies (Captive portal, Profile, Block) are terminal policies (cannot be followed by other policies)" <<<PAGE 1014>>>
## 路由
- **X62 RIP invalid 必须 ≥3×update**：AOS 强制约束。原句："AOS to enforce the constraint that invalid cannot be less than 3x of update" <<<PAGE 730>>>
- **X63 RIP 默认不通告本地/静态路由**：必须重分发。原句："Only learned RIP routes and Loopback0 interface are advertised by default." <<<PAGE 726, 746>>>
- **X64 RIP 默认收 v1/v2 发 v2；默认无认证**：原句："By default, RIP is configured to accept either RIP v1 or RIP v2 updates, and sends out RIP v2" <<<PAGE 745, 748>>>
- **X65 OSPF/ISIS 的 GR 默认关、BGP 默认开**：原句："Note: Graceful restart is disabled for OSPF and ISIS and enabled for BGP by default" <<<PAGE 776>>>
- **X66 递归静态路由 6.7.1 不可用**：原句："Option not available in AOS 6.7.1" <<<PAGE 719>>>
- **X67 IBGP 学到的路由不应再传 IBGP 邻居**：原句："Routes learned via IBGP should never be" <<<PAGE 1082>>>
- **X68 VRF 名大小写敏感；VLAN 编号不可在 VRF 间重复使用**：原句："Note: VRF names are case sensitive / Use of Duplicate VLAN numbers is not supported" <<<PAGE 859, 861>>>
- **X69 一个 IP 接口+其 VLAN 同时只能属一个 VRF**：原句："A single IP interface, as well as the VLAN associated with the interface, can only belong to one VRF instance at a time" <<<PAGE 861>>>
## 组播/ERP
- **X70 IGMP 永不被路由器转发（TTL=1）**：原句："IGMP is a protocol confined to the local segment of the LAN and is never forwarded by any router." <<<PAGE 871>>>
- **X71 IPMS 默认禁用；组播交换须显式开启**：原句："Before you begin, notice that Multicast Switching is disabled by default" <<<PAGE 877, 916>>>
- **X72 ERP RPL 只能配在已禁用的环上；无 RPL 或多 RPL 均为错误配置**：原句："The RPL node can be configured only on a preexisting disabled ring. The non-existence of a RPL node or the existence of multiple RPL nodes is considered as incorrect configuration." <<<PAGE 929>>>
- **X73 每环建议 ≤16 节点**：原句："A maximum number of 16 nodes per ring is recommended." <<<PAGE 929>>>
- **X74 ERP 环数上限依机型**：原句："The maximum number of rings per node that can be created depends on switch model" <<<PAGE 929>>>
- **X75 SPT 状态默认启用**：PIM-SM 中 `SPT status is enabled by default` <<<PAGE 903>>>
## PoE/安全
- **X76 PoE 操作状态默认 down，须 lanpower start**：原句："Def PoE oper status - Disabled (PoE must be activated on a switch-by-switch basis (lanpower start)" <<<PAGE 697-698>>>
- **X77 电容检测不符合 802.3af、仅限老话机**：原句："not compatible with IEEE specification 802.3af / It should only be enabled to support legacy IP phones" <<<PAGE 702, 706>>>
- **X78 LPS 不支持聚合口**：原句："Not supported on Link Aggregate ports" <<<PAGE 804>>>
- **X79 LPS 默认违规 restrict、300 秒自动清**：原句："By default, the port violation is restricted… there's a timer of 300 seconds to clear automatically the violation." <<<PAGE 850, 852>>>
- **X80 端口默认只学 1 个 MAC**：接傻瓜交换机/集线器即违规。原句："By default, port security allows the switch to learn only a single MAC address" <<<PAGE 850>>>
- **X81 ARP 毒化受限地址每接口最多 2 个**：原句："Maximum of two IP addresses per IP interface" <<<PAGE 824>>>
- **X82 DHCP 非信任口丢弃 Offer/ACK**：只收 Discover/Request。原句："Untrusted ports only accept DHCP Discover and Request messages - DHCP Offer and ACK are dropped" <<<PAGE 830>>>
- **X83 MACsec 支持面限制**：6860 仅 10G 口；E-P24Z8 不支持 2.5G 口；99-CMM 仅 4x10G 模式。原句："OS6860(E) 10G ports on all E/non-E models / (not supported on 2.5G ports)" <<<PAGE 827>>>
- **X84 Stack/VC 镜像文件差异**：V72/C32 用 Yos.img 与其他 6900 的 Tos.img 不同。原句："The OS6900-V72/C32 uses a different image file (Yos.img)" <<<PAGE 86, 87>>>
## 升级/其他
- **X85 镜像传输必须 binary、配置必须 ASCII**：原句："If you are transferring a switch image file, you must specify the binary transfer mode" <<<PAGE 965>>>
- **X86 VC 成员若为非 E 型 6860 仍需有效 license key**：原句："If part of a VC, the OS6860 non-E models must still have a valid license key" <<<PAGE 59>>>
- **X87 CodeGuardian 美加强制订阅、其余地区可选**：原句："US & Canada: Mandatory CodeGuardian 1-year subscription license / Rest of the world: Optional" <<<PAGE 111>>>
- **X88 ProActive Lifecycle 需本地 OmniVista 2500**：属性每两周推送云。原句："By default, the product attributes are pushed from the OmniVista 2500 NMS every two weeks." <<<PAGE 1139>>>
- **X89 堆叠写入 protected 警告防清配置**：write memory 在拓扑变化时警告。原句："protected by issuing a warning to prevent or warn purging the configuration of the elements" <<<PAGE 315, 317>>>

## frameworks

- **F1 五天课程主线**：Day1 硬件+系统管理+堆叠/VC+诊断 → Day2 VLAN/LACP/STP/DHL/IP/LLDP → Day3 VRRP/QoS/ACL/AG/IoT/PoE → Day4 RIP/OSPF/GR/AOS 安全/VRF → Day5 组播/ERP/IFAB。页码：议程 Day1-5 逐日排列 <<<PAGE 8-13>>>；扩展模块（SLB/BGP/ERP/VRF/PIM）补充议程 <<<PAGE 13>>>
- **F2 OmniSwitch 产品组合分层框架**：按 Size（Small/Medium/Large/Hardened）×能力（Value L2+ / L2+ Basic L3 / Advanced L3）把 6350/6465/6560/6860(E)/6865/6900/9900 放入同一矩阵。原句："Positioning in the Stackable portfolio… Small/Medium/Hardened/Large" <<<PAGE 23, 30, 41, 51>>>
- **F3 速率-层级演进图**：接入 100M→1G→2.5G、汇聚 1G→2.5G→10G、核心 10G→25G→40G→100G 对应机型升级路径。原句："100M->1G->2,5G / 1G->2,5G>10G / 10G->25G->40G->100G" <<<PAGE 21>>>
- **F4 AOS Flash 目录框架**：Flash = working + certified（+R8 用户自定义目录）+network/switch/boot.params/swlog；双目录互为回滚。原句："Working Directory / Certified Directory / Flash Directory" <<<PAGE 126-127, 145>>>
- **F5 Auto-fabric 零接触部署体系（七步）**：Auto-VC → RCL 远程配置 → Auto-LACP → Auto-Routing → Auto-SPB Fabric → Auto-Network Profiling → Auto-MVRP；失败即删除并禁用配置。原句："AUTO-FABRIC PLUG-N-PLAY ZERO TOUCH DEPLOYMENT" <<<PAGE 155, 936>>>
- **F6 ACFE 认证双轨框架**：Newcomer Track（从零到 ACFE/ACSE）与 Experienced Track（续证两年）。原句："Newcomer Track… Experienced Track" <<<PAGE 3-4>>>
- **F7 STP 协议/模式矩阵**：协议 802.1D/802.1w(默认)/802.1s/ERPv2 × 模式 flat/1x1(per-VLAN 默认)。原句："Spanning Tree Protocols supported… Spanning Tree Operating Modes supported" <<<PAGE 415>>>
- **F8 QoS 分层模型（R8）**：QSet（每口 8 单播+4 组播队列）→ QSI 实例 → QSet Profile（8SP / 1EF+7SP / 1EF+7WFQ）→ 分类引擎（L2-L4 条件）→ 策略三元组（condition/action/rule）。原句："Queue Set (Qset) framework / Packet Classification… POLICY CONDITION… POLICY ACTION" <<<PAGE 544-552>>>
- **F9 AOS 安全体系（Consistent AOS Network Security）**：LLDP Rogue Detection、LPS、PBR、高级 ACL 组（UserPorts/DropServices/port-disable）、BPDU Guard、DOS Protection、ARP Poisoning、MACsec、DHCP Snooping+Option82、Port Mapping、Storm Control、OmniVista 安全应用。原句："Use the Advanced AOS Security mechanisms in order to protect the core network as well as data" <<<PAGE 799>>>
- **F10 Access Guardian/UNP 分类模型**：认证（802.1X/MAC/无）→ RADIUS Filter-ID 下发 UNP → 失败降级链（分类规则/默认 UNP/Captive Portal/阻断）→ UNP = VLAN+QoS/ACL 策略列表+Location+Period；R8 端口 16 级分类优先序。原句："Access Guardian (Release 8) - Conceptual Flow / UNP Port classification rules 1..16" <<<PAGE 635-638>>>
- **F11 IoT 设备画像框架**：签名收集器（DHCP Option 55/60 + MAC OUI）→ 本地 profiler（签名库比对）→ UNP 档案自动指派 → 已知/未知设备库运营。原句："Device Profiling consists of three main components: A local signature collector, A local profiler, UNP profiling" <<<PAGE 686-690>>>
- **F12 Virtual Chassis 组件框架**：VFL/控制 VLAN/Chassis ID/Group ID/Chassis Priority + vcsetup.cfg/vcboot.cfg 双文件 + Master 选举五级 + RCD/VCSP 防脑裂。原句："VIRTUAL CHASSIS CONCEPT & COMPONENTS" <<<PAGE 292-307>>>
- **F13 OSPF 区域类型框架**：Backbone(0.0.0.0) / Stub / Totally Stubby / NSSA / Transit，对应 LSA 类型 1-7/9-11 的产生与抑制规则。原句："OSPF - Area types… Default Route / External AS / Inter-Area Routes" <<<PAGE 759-762>>>
- **F14 组播三层框架**：IGMP（成员管理，本段有效）→ IPMS（二层硬件交换）→ PIM-SM/DM、DVMRP（三层路由）；SPT/RP/BSR 角色分工。原句："Multicast - Switching vs. Routing Decision / Forwarding tables created by DVMRP, PIM-SM, PIM-DM and IPMS" <<<PAGE 874>>>
- **F15 Intelligent Fabric（SPB 织构）体系**：以 SPB 替代 STP 做二层织构、IS-IS 承载、Auto-fabric 自动化开通（6865/6900 IFAB 定位）。原句："SPB - Simplified service provisioning, better link utilization compared to STP / iFab Inside" <<<PAGE 73, 68>>>
- **F16 冗余方案选型框架**：STP（50% 带宽）→ LACP（链路冗余）→ VC（链路+设备冗余+统一管理）→ DHL（链路+设备冗余 100% 带宽）；三层另有 VRRP。原句："Comparison with Other Protocols… STP / 802.3Ad LACP / VC / DHL Active-Active" <<<PAGE 481>>>
- **F17 CodeGuardian 三层加固体系**：IV&V 源码验证 → 软件多样化（5 衍生镜像）→ 安全交付（随机下载/年度订阅）。原句："The LGS CodeGuardian™ technology hardens the OmniSwitch software on three levels" <<<PAGE 109-111, 1141>>>
- **F18 ALE 生命周期管理体系**：ProActive Lifecycle（OmniVista 2500 云端资产/软件/保修状态）+ CodeGuardian（软件完整性）组成运维闭环。原句："Alcatel-Lucent ProActive Lifecycle Management… works in conjunction with the Alcatel-Lucent OmniVista® 2500 Network Management System (NMS)" <<<PAGE 1139-1140>>>

## glossary

- **ACFE**：ALE 认证资深组网工程师（F/E 级），新学员五年训练营的培养目标之一 <<<PAGE 3>>>
- **ACSE**：ALE 认证资深交换专家认证 <<<PAGE 3>>>
- **Newcomer / Experienced Track**：新学员从零培养与老学员续证两条学习轨道 <<<PAGE 3-4>>>
- **Knowledge Hub**：ALE 培训与认证历史查询门户（enterprise-education.csod.com）<<<PAGE 3>>>
- **DT00CTE120EN**：本 Bootcamp 课程编号 <<<PAGE 5>>>

## 硬件与产品线
- **OmniSwitch 6350**：入门级 L2+ 千兆堆叠交换机，SMB/分支场景 <<<PAGE 22-28>>>
- **OmniSwitch 6450**：L2+/基础 L3 千兆堆叠交换机，可选 10G 上联 <<<PAGE 113-121>>>
- **OmniSwitch 6465**：紧凑型工业加固交换机（-40~+75℃、DIN 导轨、1588v2/MACsec）<<<PAGE 42-49>>>
- **OmniSwitch 6560**：多千兆（mGIG）L2+/基础 L3 交换机，支持 2.5G/802.3bt <<<PAGE 30-39>>>
- **OmniSwitch 6860/6860E**：高级 L3 GE 接入/汇聚交换机，E 型带协处理器与 60W HPoE <<<PAGE 52-59>>>
- **OmniSwitch 6865**：下一代工业加固 L3 交换机（SPB、1588v2、75W HPoE）<<<PAGE 66-74>>>
- **OmniSwitch 6900 系列**：数据中心 TOR/园区核心（X/T/Q32/X72/V72/C32 机型）<<<PAGE 78-94>>>
- **OmniSwitch 9907/9900**：7 槽模块化低时延机箱，直连架构无背板 <<<PAGE 96-107>>>
- **CMM**：Control Management Module，交换机控制管理模块（9900/9000 系列的主控）<<<PAGE 99, 128>>>
- **NI**：Network Interface，业务线卡/网络接口模块 <<<PAGE 100-104>>>
- **CFM**：Chassis Fabric Module，9900 机箱交换网板 <<<PAGE 105>>>
- **EMP**：Ethernet Management Port，带外以太网管理口 <<<PAGE 99, 153>>>
- **VFL**：Virtual Fabric Link，虚拟机箱互联链路 <<<PAGE 292>>>
- **BPS（Omni BPS）**：高级备电柜，N+1/N+N 模式最多备 8 台 <<<PAGE 60-64>>>
- **SFP/SFP+/QSFP+/QSFP28**：光模块封装类型（1G/10G/40G/100G）<<<PAGE 91-94>>>
- **DAC**：Direct Attach Copper 直连铜缆（1/3/5/7 米）<<<PAGE 91>>>
- **Combo 口**：RJ45/SFP 复用端口 <<<PAGE 25, 166>>>
- **MGIG（mGIG）**：多千兆以太网（2.5G/5G/10G BASE-T）<<<PAGE 30-35>>>
- **EEE**：Energy Efficient Ethernet 节能以太网（802.3az）<<<PAGE 52, 710>>>
- **HPoE**：高功率 PoE（60/75W，802.3bt 级）<<<PAGE 33, 54>>>
- **1588v2 (PTP)**：精密时间协议，工业/电力场景时钟同步 <<<PAGE 43, 68>>>
- **ISSU**：In-Service Software Upgrade 不中断升级 <<<PAGE 20, 290>>>
- **CodeGuardian**：LGS 提供的交换机软件三级加固技术 <<<PAGE 108-111>>>
- **IV&V**：独立验证与确认（源码安全审计）<<<PAGE 110>>>
- **Diversified Image**：CodeGuardian 软件多样化衍生镜像（每版本 5 种）<<<PAGE 110-111>>>
- **ProActive Lifecycle Management**：基于 OmniVista 2500 的云端资产生命周期管理 <<<PAGE 1139-1140>>>
- **RCD**：Remote Chassis Detection，经 EMP 的 VC 脑裂检测 <<<PAGE 306>>>
- **VCSP**：Virtual Chassis Split Detection，经 helper 链路的 VC 分裂检测 <<<PAGE 307>>>
- **SSP**：Split Stack Protection，R6 堆叠分裂保护 <<<PAGE 274-275>>>

## AOS 系统与文件系统
- **AOS**：Ale Operating System，OmSwitch 操作系统（R6/R7/R8 三大版本系）<<<PAGE 5, 122>>>
- **Working Directory**：可写运行目录，配置改动保存目标 <<<PAGE 126, 145>>>
- **Certified Directory**：只读认证目录，升级回退基准 <<<PAGE 126, 145>>>
- **Running Directory**：当前启动来源目录（R8 概念）<<<PAGE 146>>>
- **boot.cfg**：配置文件，重启后恢复配置 <<<PAGE 127, 216>>>
- **boot.params**：启动参数文件（镜像选择等）<<<PAGE 127-128>>>
- **MiniBoot/BootROM**：引导加载器与底层硬件初始化 <<<PAGE 128>>>
- **Trescue.img**：USB 灾难恢复镜像 <<<PAGE 139>>>
- **aossignature**：USB auto-copy 触发标志文件 <<<PAGE 140>>>
- **Rollback**：配置回滚（reload 时以 certified 为备份）<<<PAGE 126, 147>>>
- **rollback-timeout**：重启回滚计时（no rollback-timeout 表示不回滚）<<<PAGE 132, 149>>>
- **flash-synchro**：跨 CMM/堆叠成员同步 flash <<<PAGE 267-268, 285>>>
- **show microcode**：查看各目录软件版本 <<<PAGE 143, 962>>>
- **write memory**：保存运行配置到运行目录 <<<PAGE 148, 264>>>
- **copy working certified**：把 working 内容认证到 certified <<<PAGE 133, 965>>>
- **modify running-directory**：R8 切换运行目录命令 <<<PAGE 148>>>
- **Configuration Snapshot**：配置快照文本，可 apply 恢复 <<<PAGE 164, 229-230>>>
- **Pre-banner**：登录前自定义提示文本（pre_banner.txt）<<<PAGE 168>>>
- **WebView**：内置 Web 管理界面 <<<PAGE 169-170>>>
- **OmniVista**：ALE 网管平台（2500 系列/高级应用/PolicyView）<<<PAGE 171-173>>>
- **ELM**：Embedded Lightweight Module，OmniVista 内嵌管理模块 <<<PAGE 171>>>
- **RCL（Remote Configuration Loading）**：开箱 DHCP+TFTP 指令文件自动装载 <<<PAGE 157-158, 941>>>
- **Instruction File**：RCL 下载的升级指令文件（固件/配置/脚本/服务器）<<<PAGE 158>>>
- **Bash shell**：R8 CLI 底层 shell（别名/管道/busybox）<<<PAGE 150-151>>>
- **Alias**：命令别名，存 boot.cfg <<<PAGE 150, 165>>>

## 账户与 AAA
- **admin 账户**：默认全权限账户（密码 switch，仅 console）<<<PAGE 176, 242>>>
- **default 账户**：新用户权限模板（非登录账户）<<<PAGE 176, 242>>>
- **ASA**：Authenticated Switch Access，管理接口认证框架 <<<PAGE 184>>>
- **AAA**：认证/授权/计费框架（RADIUS/LDAP/TACACS+）<<<PAGE 184-187>>>
- **RADIUS**：远程认证拨入用户服务 <<<PAGE 186, 662>>>
- **TACACS+**：终端访问控制器访问协议_plus <<<PAGE 184, 493>>>
- **End-User Profile**：R6 终端用户档案（限定端口/VLAN 权限）<<<PAGE 177, 182>>>
- **Password Policy**：密码复杂度/历史/年龄/锁定策略 <<<PAGE 180-181>>>
- **Account Lockout**：失败登录锁定（阈值/窗口/时长）<<<PAGE 181>>>
- **NTP**：网络时间协议（客户端/服务器/对等体，RFC1305）<<<PAGE 189-190>>>
- **Stratum**：NTP 层级数 <<<PAGE 189>>>

## 堆叠与虚拟机箱
- **Stack**：多台同家族交换机组建成单一管理实体 <<<PAGE 251>>>
- **Slot-ID**：堆叠成员槽号（boot.slot.cfg 保存）<<<PAGE 256, 251>>>
- **Pass-Through**：槽号冲突时的透传角色 <<<PAGE 255, 257>>>
- **takeover**：堆叠/VC 主备切换命令 <<<PAGE 260, 285>>>
- **MAC Retention**：堆叠主 MAC 保持机制 <<<PAGE 270-273>>>
- **boot.slot.cfg**：堆叠槽号配置文件 <<<PAGE 251, 286>>>
- **Virtual Chassis (VC)**：R8 多机虚拟化成单交换机 <<<PAGE 289-290>>>
- **Master/Slave Chassis**：VC 主/从机箱 <<<PAGE 292>>>
- **Chassis ID / Group ID**：VC 机箱号与机组号（决定组虚拟 MAC）<<<PAGE 293>>>
- **Control VLAN**：VC 内部通信保留 VLAN（仅 VFL 口）<<<PAGE 292>>>
- **vcsetup.cfg / vcboot.cfg**：VC 建立所需两文件 <<<PAGE 294>>>
- **virtual_dir**：VC 配置目录（reload from virtual_dir 恢复 VC）<<<PAGE 932>>>
- **Auto-VC**：出厂自动 VFL/Chassis ID 协商 <<<PAGE 938-940>>>
- **Demo License**：VC 出厂默认演示许可 <<<PAGE 938>>>

## 诊断
- **swlog**：交换机日志（console/flash/syslog 三输出）<<<PAGE 325-332>>>
- **appid/subapp**：日志应用/子应用标识与级别控制 <<<PAGE 330-331>>>
- **command-log**：命令及结果日志（/flash/command.log）<<<PAGE 333-335>>>
- **Port Mirroring**：端口镜像（2 会话、128:1）<<<PAGE 336-337>>>
- **RPM（Remote Port Mirroring）**：跨交换机远程镜像（专用 VLAN）<<<PAGE 338>>>
- **Policy Based Mirroring**：基于 QoS 策略的镜像 <<<PAGE 339-340>>>
- **Port Monitoring**：本机抓包（Sniffer ENC 格式、前 64 字节）<<<PAGE 341-342>>>
- **RMON**：远程监控（统计/历史/告警/事件四组）<<<PAGE 343-344>>>
- **show health**：CPU/内存资源利用率与健康阈值 <<<PAGE 345-346>>>
- **sFlow**：RFC3176 流采样监控（agent+collector）<<<PAGE 347-350>>>
- **sFlow Receiver/Sampler/Poller**：接收器/采样器/轮询器三要素 <<<PAGE 350>>>

## VLAN 与二层
- **VLAN**：虚拟局域网（广播域）<<<PAGE 360>>>
- **默认 VLAN（VLAN 1）**：出厂全部端口所属、不可删 <<<PAGE 363, 385>>>
- **Static VLAN**：端口手工指定 VLAN <<<PAGE 362-364>>>
- **Dynamic VLAN**：按规则/认证动态指派 VLAN <<<PAGE 365-371>>>
- **Mobile Port**：R6 动态 VLAN 端口类型 <<<PAGE 367, 370>>>
- **VLAN Rules**：VLAN 分类规则（MAC/网络地址/协议等）<<<PAGE 368-370>>>
- **802.1Q Tag**：VLAN 标签（12bit VID+3bit 802.1p）<<<PAGE 377-379>>>
- **802.1p**：VLAN 标签内 3bit 优先级字段 <<<PAGE 379>>>
- **Mobile Tag**：mobile 口收多 VLAN 打标签机制 <<<PAGE 381-383>>>
- **Tagged/Untagged 端口**：打标签/不打标签的 VLAN 成员口 <<<PAGE 363, 380>>>
- **Inter-VLAN Routing**：虚拟路由口间三层互通 <<<PAGE 372-374>>>
- **Virtual Router Port**：VLAN 上 IP 接口的旧称 <<<PAGE 373, 385>>>
- **Source Learning**：VLAN 内源学习 <<<PAGE 374, 385>>>
- **MVRP**：多 VLAN 注册协议（802.1ak，动态 VLAN 注册/裁剪）<<<PAGE 479, 967-971>>>
- **MVRP Registrar/Applicant Mode**：MVRP 端口注册/申请模式 <<<PAGE 970>>>
- **Dynamic VLAN（MVRP）**：MVRP 自动创建的 VLAN（type dyn）<<<PAGE 970>>>

## 链路聚合
- **Link Aggregation**：多物理口合为单逻辑链路 <<<PAGE 394>>>
- **LACP（802.3ad）**：链路聚合控制协议 <<<PAGE 396, 398>>>
- **LACPDU**：LACP 协议数据单元 <<<PAGE 396>>>
- **OmniChannel（静态聚合）**：ALE 静态聚合，仅限 OmniSwitch 间 <<<PAGE 396-397>>>
- **Actor Admin Key**：聚合端口关联键（两端一致）<<<PAGE 398, 404>>>
- **Primary Port**：聚合组主端口（组播默认出口）<<<PAGE 402, 405>>>
- **hash-control**：哈希算法控制（brief/extended/non-ucast）<<<PAGE 401-402>>>
- **DHL（Dual Home Link）**：双归属链路 Active-Active 上行冗余 <<<PAGE 476-481>>>
- **RPL（DHL 中）**：Pre-Emption timer 恢复等待定时器 <<<PAGE 479>>>
- **MAC Flushing**：DHL 变更后清陈旧 MAC（None/MVRP Enhanced/RAW）<<<PAGE 479-480>>>

## 生成树
- **STP（802.1D）**：生成树协议防环 <<<PAGE 414, 419>>>
- **RSTP（802.1w）**：快速生成树（默认），亚秒收敛 <<<PAGE 415, 421>>>
- **MSTP（802.1s）**：多生成树，多实例映射 VLAN <<<PAGE 415, 437>>>
- **Flat Mode**：每机一棵生成树 <<<PAGE 427-428>>>
- **1x1 / Per-VLAN Mode**：每 VLAN 一棵树（默认）<<<PAGE 427, 429-430>>>
- **Root Bridge**：根桥（最低 Bridge ID 选举）<<<PAGE 414, 419-420>>>
- **Bridge Priority**：桥优先级（默认 32768）<<<PAGE 425, 461>>>
- **Root Port / Designated Port**：根端口/指定端口 <<<PAGE 414, 423>>>
- **Alternate / Backup Port**：RSTP 替代/备份端口 <<<PAGE 423>>>
- **BPDU**：桥协议数据单元 <<<PAGE 419, 428>>>
- **Path Cost**：路径开销（16/32bit 两套默认值）<<<PAGE 425, 432>>>
- **PVST+**：Cisco 每 VLAN 生成树互操作 <<<PAGE 433-434>>>
- **CIST**：公共内部生成树（MSTP 实例 0）<<<PAGE 438, 442>>>
- **MSTI**：多生成树实例（最多 16 个）<<<PAGE 438>>>
- **MST Region**：MST 域（同名+同修订+同映射表）<<<PAGE 440, 443>>>
- **Region Boundary Port**：域边界端口 <<<PAGE 443>>>
- **Digest**：VLAN-实例映射表摘要（BPDU 携带）<<<PAGE 443>>>
- **CST Root / CIST Regional Root**：全网根/区域根 <<<PAGE 441-442>>>

## IP 接口与 DHCP
- **Loopback0**：常驻环回管理接口 <<<PAGE 492>>>
- **ip managed-interface**：按应用指定源接口（R8）<<<PAGE 493>>>
- **Local Proxy ARP**：本网段代理 ARP <<<PAGE 491, 495>>>
- **ARP Filter**：ARP 报文过滤 <<<PAGE 497>>>
- **DHCP Relay（ip helper）**：DHCP 中继 <<<PAGE 498, 743>>>
- **UDP Relay**：指定 UDP 端口中继（如 DNS）<<<PAGE 499>>>
- **ip interface**：三层虚拟 IP 接口 <<<PAGE 373, 496>>>
- **ECMP**：等价多路径 <<<PAGE 718, 723>>>

## LLDP
- **LLDP（802.1AB）**：链路层发现协议 <<<PAGE 509>>>
- **LLDPDU**：LLDP 协议数据单元 <<<PAGE 510>>>
- **TLV**：Type Length Value 信息单元 <<<PAGE 510>>>
- **LLDP-MED**：媒体终端设备扩展 <<<PAGE 513-514>>>
- **Network Policy**：LLDP-MED 网络策略 TLV（VLAN+优先级+DSCP）<<<PAGE 514-515>>>
- **trust-agent**：LLDP 可信代理（ Rogue 检测）<<<PAGE 801-802>>>

## VRRP
- **VRRP**：虚拟路由器冗余协议（RFC 2338）<<<PAGE 522-524>>>
- **Virtual Router ID (VRID)**：虚拟路由器标识 <<<PAGE 524, 529>>>
- **Master/Backup Router**：主/备虚拟路由器 <<<PAGE 526>>>
- **Virtual MAC**：00-00-5E-00-01-{VRID} <<<PAGE 524, 536>>>
- **Preempt**：抢占模式 <<<PAGE 529-530>>>
- **Advertisement Interval**：VRRP 通告间隔 <<<PAGE 527>>>
- **Skew Time**：(256-Priority)/256，防多备同升 <<<PAGE 527>>>
- **VRRP Tracking**：跟踪对象联动优先级 <<<PAGE 531-532>>>
- **VRRP Group**：VRRP 集体管理组 <<<PAGE 533>>>
- **HSRP**：Cisco 热备协议（与 VRRP 不兼容）<<<PAGE 524>>>

## QoS
- **QoS**：服务质量（带宽/时延/丢弃管理）<<<PAGE 542>>>
- **CoS Queue**：每出端口 8 个服务等级队列 <<<PAGE 545-546>>>
- **Strict Priority (SP)**：严格优先调度 <<<PAGE 547, 550>>>
- **WRR**：加权轮询调度 <<<PAGE 547>>>
- **DRR**：差额轮询调度 <<<PAGE 547>>>
- **WFQ**：加权公平队列（R8 QSet Profile 3）<<<PAGE 552>>>
- **EF**：Expedited Forwarding 快速转发队列（限速保护）<<<PAGE 551-552>>>
- **QSet / QSI**：R8 队列组/队列组实例 <<<PAGE 548-549>>>
- **Policy Condition**：策略条件（L2-L4 匹配）<<<PAGE 544, 568>>>
- **Policy Action**：策略动作（标记/限速/重定向/镜像）<<<PAGE 544, 571>>>
- **Policy Rule**：策略规则（条件+动作+可选时段）<<<PAGE 545, 573>>>
- **Precedence**：规则优先级（0-65535，大者先）<<<PAGE 573, 607>>>
- **Validity Period**：规则生效时段 <<<PAGE 565>>>
- **Network/MAC/Service/Port Group**：策略复用组 <<<PAGE 569, 608>>>
- **Disposition（accept/drop/deny）**：策略处置动作 <<<PAGE 609>>>
- **qos apply / qos reset**：策略应用/清空 <<<PAGE 612, 592>>>
- **ToS/DSCP**：三层服务类型/差分服务码点标记 <<<PAGE 543, 590>>>
- **Trusted Port（qos phones trusted）**：信任端口标记 <<<PAGE 581, 590>>>
- **SIP Snooping**：SIP 信令侦听自动语音 QoS <<<PAGE 601>>>
- **Bandwidth Shaping**：带宽整形 <<<PAGE 543>>>
- **Starvation**：严格优先下低队列饿死风险 <<<PAGE 550-551>>>

## ACL 与安全
- **ACL**：访问控制列表（QoS 策略过滤子集）<<<PAGE 604-607, 618>>>
- **established**：TCP ACK/RST 已建连接条件 <<<PAGE 607, 615>>>
- **tcpflags**：TCP 标志位条件 <<<PAGE 611, 618>>>
- **Access Guardian (AG)**：端口自动感知多客户端认证 <<<PAGE 627, 630>>>
- **UNP**：Universal Network Profile 用户网络档案 <<<PAGE 631-632, 645>>>
- **Filter-ID**：RADIUS 属性下发 UNP 名 <<<PAGE 632>>>
- **Group Mobility（R6）**：UNP 前身的移动分组分类 <<<PAGE 636, 652>>>
- **UNP Classification Rule**：设备分类规则（R8 十六级）<<<PAGE 638, 652-656>>>
- **UNP Port（port-type BRIDGE）**：R8 UNP 桥接端口 <<<PAGE 643>>>
- **Location Policy**：按位置限制的 UNP 策略 <<<PAGE 649>>>
- **Period Policy**：按时段限制的 UNP 策略 <<<PAGE 650>>>
- **aaa profile（device-authentication）**：设备认证档案 <<<PAGE 662>>>
- **Captive Portal**：Web 强制门户（终结策略）<<<PAGE 635, 1014>>>
- **Learned Port Security (LPS)**：学习端口安全（限 MAC 数/列表）<<<PAGE 803-809>>>
- **port-security violation restrict/shutdown**：LPS 违规过滤/关口 <<<PAGE 805>>>
- **convert-to-static**：动态 MAC 转静态 <<<PAGE 807>>>
- **learn-trap-threshold**：学习告警阈值 <<<PAGE 809>>>
- **PBR（Policy Based Routing）**：策略路由硬件重定向 <<<PAGE 810-814>>>
- **permanent gateway**：PBR 动作指定固定网关 <<<PAGE 812-813>>>
- **UserPorts**：保留端口组（防欺骗等）<<<PAGE 816>>>
- **DropServices**：保留服务组（批量丢弃）<<<PAGE 817>>>
- **port-disable action**：命中即关闭端口动作 <<<PAGE 817>>>
- **violation-recovery-time**：违规端口自动恢复定时 <<<PAGE 818>>>
- **Directed Broadcast**：定向广播（建议关闭）<<<PAGE 819>>>
- **Early ARP Discard**：早期 ARP 丢弃（CPU 保护）<<<PAGE 819>>>
- **DoS Filtering**：拒绝服务攻击过滤 <<<PAGE 821>>>
- **ARP Defense / ARP Poisoning Detection**：ARP 防御与毒化检测 <<<PAGE 822-824>>>
- **restricted-address（arp-poison）**：ARP 毒化受限地址 <<<PAGE 824>>>
- **MACsec（802.1AE）**：二层链路加密认证 <<<PAGE 825-827>>>
- **Static SA / Dynamic SA（PSK/EAP）**：MACsec 安全关联模式 <<<PAGE 826>>>
- **SCI（sci-tx/sci-rx）**：MACsec 安全通道标识配置 <<<PAGE 1049>>>
- **DHCP Snooping**：DHCP 侦听（信任口/绑定库）<<<PAGE 828-830>>>
- **Option 82**：DHCP 中继选项（Circuit ID/Remote ID）<<<PAGE 832>>>
- **Binding Table**：DHCP 侦听绑定数据库 <<<PAGE 829>>>
- **Port Mapping**：用户口-网络口映射隔离 <<<PAGE 837-839>>>
- **Dynamic Proxy ARP**：端口映射配套代理 ARP <<<PAGE 839>>>
- **Storm Control（flood rate）**：风暴控制（bcast/mcast/unknown-unicast）<<<PAGE 886>>>
- **BPDU Guard**：BPDU 保护 <<<PAGE 799>>>
- **IoT Device Profiling**：IoT 设备画像 <<<PAGE 685-690>>>
- **DHCP Fingerprinting**：DHCP 指纹（Option 55/60）<<<PAGE 688>>>
- **MAC OUI**：组织唯一标识符（设备厂商标识）<<<PAGE 687-688>>>
- **Signature DB**：本地设备签名库 <<<PAGE 686>>>

## PoE
- **PoE（802.3af）**：以太网供电 15.4W <<<PAGE 694-695>>>
- **PoE+（802.3at）**：增强供电 30W（Class 4 34.2W PSE）<<<PAGE 695>>>
- **PSE / PD**：供电设备/受电设备 <<<PAGE 695>>>
- **PD Classification**：受电设备分级（电阻识别）<<<PAGE 695>>>
- **lanpower**：PoE 管理命令族 <<<PAGE 700-708>>>
- **Port Priority（low/high/critical）**：PoE 端口优先级 <<<PAGE 701>>>
- **Capacitor Detection**：电容检测法（旧话机）<<<PAGE 702>>>
- **Priority Disconnect**：预算不足时新 PD 拒绝机制 <<<PAGE 702>>>
- **Power Budget**：PoE 总预算 <<<PAGE 694, 703>>> 

## 路由（静态/RIP/OSPF/GR/BGP/ISIS）
- **Static Route**：静态路由 <<<PAGE 714-717>>>
- **Recursive Static Route（follows）**：递归静态路由 <<<PAGE 719-720>>>
- **Interface Static Route**：出接口型静态路由 <<<PAGE 721>>>
- **show ip router database**：路由数据库（含未用路由）<<<PAGE 718, 720>>>
- **Route Preference（ip route-pref）**：协议路由偏好 <<<PAGE 769>>>
- **RIP（v1/v2/RIPng）**：路由信息协议 <<<PAGE 722-724>>>
- **Distance Vector**：距离矢量算法 <<<PAGE 724>>>
- **Poison Reverse**：毒性逆转 <<<PAGE 725>>>
- **RIP Timers（update/invalid/garbage/holddown）**：RIP 四定时器 <<<PAGE 730-731>>>
- **Route Map（redistribution）**：路由图与重分发 <<<PAGE 726-727, 768>>>
- **OSPF**：开放式最短路径优先（RFC 2328）<<<PAGE 750-753>>>
- **Router ID**：OSPF 路由器标识 <<<PAGE 754, 780>>>
- **Area / Backbone Area**：OSPF 区域/骨干区域 0.0.0.0 <<<PAGE 755, 756>>>
- **DR（Designated Router）**：指定路由器 <<<PAGE 755>>>
- **Adjacency / Neighbor**：邻接/邻居 <<<PAGE 753, 757>>>
- **LSDB**：链路状态数据库 <<<PAGE 753, 757>>>
- **SPF**：最短路径优先算法 <<<PAGE 753, 1093>>>
- **LSA Type 1-7**：链路状态通告类型 <<<PAGE 761>>>
- **Opaque LSA（Type 9-11）**：扩展 LSA（GR 用 Type 9）<<<PAGE 762>>>
- **ABR / ASBR**：区域边界/自治系统边界路由器 <<<PAGE 760-761>>>
- **Stub / Totally Stubby / NSSA**：末节/完全末节/次末节区域 <<<PAGE 760, 764-766>>>
- **Virtual Link**：OSPF 虚链路 <<<PAGE 763>>>
- **default-originate**：ABR 向 stub 区注入默认路由 <<<PAGE 764-765>>>
- **area range（summarization）**：ABR 区域间路由汇总 <<<PAGE 767>>>
- **Graceful Restart (GR)**：优雅重启（转发不中断）<<<PAGE 770-775>>>
- **Grace LSA**：GR 宽限期通告 <<<PAGE 774-775>>>
- **Helper（restart-helper）**：GR 辅助路由器 <<<PAGE 776>>>
- **restart-interval**：GR 宽限时长 <<<PAGE 776>>>
- **BFD**：双向转发检测 <<<PAGE 711, 716>>>
- **BGP（AS/neighbor/eBGP multihop）**：边界网关协议 <<<PAGE 1079-1081>>>
- **IBGP**：内部 BGP（学到的路由不再传 IBGP）<<<PAGE 1082>>>
- **aspath-list / community-list / prefix-list**：BGP 策略列表 <<<PAGE 1086-1088>>>
- **update-source**：BGP 邻居更新源（Loopback0）<<<PAGE 1081>>>
- **IS-IS**：中间系统到中间系统路由协议 <<<PAGE 1090-1093>>>
- **NSAP 地址（Area ID/System ID/NSEL）**：OSI 网络地址 <<<PAGE 1094-1095>>>
- **AFI 49**：本地管理 IS-IS 地址标识 <<<PAGE 1094>>>
- **Level-1 / Level-2**：IS-IS 区域内/区域间层级 <<<PAGE 1094, 1106>>>
- **DIS（Designated IS）**：IS-IS 指定中间系统 <<<PAGE 1097, 1102>>>
- **Pseudo Node**：广播网伪节点 <<<PAGE 1097>>>
- **LSP（IS-IS Link-State Packet）**：IS-IS 链路状态报文 <<<PAGE 1096, 1099>>>
- **CSNP / PSNP**：完全/部分序列号报文 <<<PAGE 1096, 1100-1101>>>
- **Route Leaking**：IS-IS 两级路由泄漏 <<<PAGE 1092>>>

## VRF
- **VRF**：虚拟路由转发（多路由实例）<<<PAGE 853-855>>>
- **Default VRF**：默认路由实例 <<<PAGE 859>>>
- **VRF-aware**：协议的 VRF 感知能力 <<<PAGE 856>>>
- **VRF Route Leak（export/import route-map）**：VRF 与 GRT 间路由泄漏 <<<PAGE 863-864>>>
- **GRT**：全局路由表 <<<PAGE 863-864>>>
- **PE（Provider Edge）**：运营商边缘设备 <<<PAGE 857>>>

## 组播
- **IP Multicast**：IP 组播（单源到多接收）<<<PAGE 866-867>>>
- **Class D 地址**：组播地址范围 224.0.0.0-239.255.255.255 <<<PAGE 867>>>
- **01:00:5e MAC 映射**：组播 IP 到 MAC 的 23 位映射 <<<PAGE 867>>>
- **IGMP（v1/v2/v3）**：互联网组管理协议 <<<PAGE 870-872>>>
- **Querier**：IGMP 查询者 <<<PAGE 871, 879>>>
- **Leave Group / Fast Leave**：v2 离组/快速离开 <<<PAGE 872>>>
- **Source-Specific Join（SSM）**：v3 源特定加入 <<<PAGE 872, 908>>>
- **IPMS**：IP 组播交换（二层硬件 IGMP snooping 转发）<<<PAGE 869, 873-878>>>
- **Querier Forwarding**：组播送查询者机制 <<<PAGE 879>>>
- **IGMP Proxying**：IGMP 代理 <<<PAGE 877>>>
- **Helper Address（IGMP Relay）**：IGMP 报文中继地址 <<<PAGE 884>>>
- **max-group（Throttling）**：端口/VLAN 组数限制 <<<PAGE 885>>>
- **DVMRP**：距离矢量组播路由协议 <<<PAGE 890-896>>>
- **PIM-SM / PIM-DM**：协议无关组播 稀疏/密集模式 <<<PAGE 907-909>>>
- **RP（Rendezvous Point）**：汇聚点 <<<PAGE 492, 908>>>
- **BSR / CBSR**：自举路由器/候选 BSR <<<PAGE 908-909>>>
- **Candidate-RP**：候选汇聚点 <<<PAGE 908, 923>>>
- **SPT（Shortest Path Tree）**：最短路径树切换 <<<PAGE 903, 909>>>
- **static-rp**：静态 RP 配置 <<<PAGE 909>>>
- **groute / sgroute**：组路由/源组路由查看 <<<PAGE 912-913>>>
- **Flood Unknown**：未知组播洪泛开关 <<<PAGE 877, 886>>>

## ERP 与 Intelligent Fabric
- **ERP（G.8032/ERPv2）**：以太网环网保护 <<<PAGE 415, 926-929>>>
- **APS**：自动保护倒换协议 <<<PAGE 926>>>
- **RPL / RPL Owner**：环保护链路及其属主节点 <<<PAGE 929>>>
- **R-APS Channel**：环保护协议信道（Service VLAN 承载）<<<PAGE 928>>>
- **Service VLAN / Protected VLAN**：ERP 业务 VLAN/受保护 VLAN <<<PAGE 928>>>
- **MEG Level**：以太网维护实体组等级（ERP 用）<<<PAGE 929-930>>>
- **WTR（Wait To Restore）**：等待恢复定时器 <<<PAGE 929-930>>>
- **Guard Timer**：ERP 守护定时器 <<<PAGE 930>>>
- **Pending / Protected 状态**：ERP 环状态 <<<PAGE 930>>>
- **Intelligent Fabric (iFab)**：智能织构体系 <<<PAGE 68, 933>>>
- **Auto-fabric**：零接触自动织构发现流程 <<<PAGE 154-155, 951>>>
- **Auto-LACP / Auto-Routing / Auto-MVRP**：自动聚合/路由/VLAN 注册 <<<PAGE 155, 943-944>>>
- **SPB（Shortest Path Bridging）**：最短路径桥接织构技术 <<<PAGE 68, 73>>>
- **Auto Network Profiling**：自动用户/网络档案 <<<PAGE 155, 936>>>

## SLB
- **SLB**：服务器负载均衡 <<<PAGE 972-975>>>
- **VIP（Virtual IP）**：集群虚拟 IP <<<PAGE 974-975>>>
- **SLB Cluster**：服务器集群 <<<PAGE 974, 976>>>
- **WRR（weight）**：加权轮询分发 <<<PAGE 977-979>>>
- **QoS Condition Cluster**：按策略条件定义的集群 <<<PAGE 981, 984-985>>>
- **SLB Probe**：健康检查探针（http/ftp/mail 等）<<<PAGE 987, 995>>>
- **Proxy ARP（SLB）**：VIP 代理 ARP <<<PAGE 975, 983>>>

## IPv6
- **IPv6**：128bit 地址协议 <<<PAGE 1130-1131>>>
- **:: 缩写**：连续零段缩写（仅一次）<<<PAGE 1133>>>
- **Unicast / Multicast / Anycast**：单播/组播/任播 <<<PAGE 1134>>>
- **Link-Local Address（FE80::/10）**：链路本地地址 <<<PAGE 1136-1137>>>
- **Global Unicast**：全球单播地址 <<<PAGE 1135>>>
- **EUI-64**：由 MAC 生成接口标识（插 FFFE 翻 U/L 位）<<<PAGE 1138>>>
- **NDP（Neighbor Discovery）**：邻居发现（用 link-local）<<<PAGE 1137>>>

## principles

## 一、产品与硬件（Day 1）
- **P1 OmniSwitch 家族定位分层**：堆叠（6350/6450/6560/6465）、加固（6465/6865）、模块化（6900/9900）三层产品线。原句："Stackable switch / Hardened Access Switch / Modular Switch" <<<PAGE 19>>>
- **P2 全线速率演进主线**：接入 100M→1G→2.5G，汇聚 1G→2.5G→10G，核心 10G→25G→40G→100G。原句："Speed increase at all layers of the enterprise" <<<PAGE 21>>>
- **P3 OS6350 定位**：入门 L2+ GE，SMB 市场，高级 L2 + 基础 L3（IPv4/IPv6），Auto-QoS、8 硬件队列。原句："Advanced L2 features with basic L3 routing for both IPv4 and IPv6" <<<PAGE 27>>>
- **P4 OS6560 MGIG 机型**：24Z8/24Z24/P48Z16 支持 100/1G/2.5G（802.3bt 75W），SFP+ 上联/堆叠二合一。原句："8 RJ-45 100/1G/2.5G Base T ports / PoE 802.3af/at/bt ports (up to 75W on a port)" <<<PAGE 33>>>
- **P5 OS6560 电源复用 6860 体系**：模块化 300/600/900W 电源负载分担，1RU 内实现冗余。原句："Re-use existing power supplies from the OS6860 PoE family… Allows for load sharing between supplies" <<<PAGE 39>>>
- **P6 OS6465 工业加固交换机**：-40~+75℃、DIN 导轨、1588v2 与 MACsec 全端口。原句："Designed for industrial applications / Operating Temperature -40 to +75 ℃" <<<PAGE 42-43>>>
- **P7 OS6860E 增强型差异**：内置协处理器跑 DPI/应用指纹（约 1000 签名发现、100 签名线速匹配），前 4 口 60W PoE，仅 E 型有 EMP 口。原句："Specialized built-in co-processor board… With AOS 8.1.1 the Application Monitoring / Fingerprinting function will run on it" <<<PAGE 52-56>>>
- **P8 OS6860E-P24Z8 2.5G 限制**：2.5G 端口需手动配置速率且成对修改。原句："Speed change on 2.5G Ports configurable only in pairs (17, 18), (19, 20)" <<<PAGE 55>>>
- **P9 Omni BPS 备电柜两种模式**：N+1（SINGLE）防电源模块故障、N+N（FULL）防市电线路故障。原句："N+1 also called SINGLE backup / Protects against switch primary PSU failure not against AC power line failure" <<<PAGE 63-64>>>
- **P10 OS6900 演进路线**：2011 10G 模块化 → 2015 40G 高密度 → 2018 25G/100G（X72/V72/C32）。原句："OS6900 evolution: 25G/100G" <<<PAGE 78>>>
- **P11 OS6900-Q32 线速条件**：每管道 ≤240Gbps 才线速，40G 口可分裂为 4x10G（a/b/c/d 子端口编号）。原句："Q32 is wire rate when each pipeline is 240 Gbps or less / The port numbering scheme changes by using letters a, b, c, d" <<<PAGE 85>>>
- **P12 V72/C32 独立镜像**：使用 Yos.img，与其余 OS6900（Tos.img）不同。原句："The OS6900-V72/C32 uses a different image file (Yos.img) than all other OS6900 models (Tos.img)" <<<PAGE 86-87>>>
- **P13 OS9907 无背板直连架构**：每槽直连交换网板，两阶段容量翻倍演进。原句："Innovative direct-connect architecture - Backplane less - Each slot connects to the fabric directly" <<<PAGE 98>>>
- **P14 OS9900 系统供电优先**：系统上电优先，剩余功率全部给 PoE，最高 10800W。原句："System power for board bring up takes priority / After system bring up all remaining power is available for PoE!" <<<PAGE 106-107>>>
- **P15 CodeGuardian 三层加固**：源码独立验证（IV&V）、软件多样化（每版本 5 种衍生镜像）、安全交付（随机下载）。原句："Three tiered approach offering - Independent verification and validation of source code - Software diversification to prevent exploitation - Secure delivery of software to customer" <<<PAGE 109-111>>>
## 二、AOS 系统与配置管理（Day 1）
- **P16 管理访问方式全集**：CLI（console/Telnet）、WebView、SNMP、SSH、FTP/SFTP、TFTP、USB 灾难恢复。原句："Management tools include: CLI… WebView… SNMP… Secure Shell (SSH)" <<<PAGE 124>>>
- **P17 Flash 双目录体系（R6）**：working 与 certified 各存一套 *.img 与 boot.cfg，认证版本作为升级回退备份。原句："2 versions are present on flash; working and certified / A certified version (SW + conf) will be used as a backup" <<<PAGE 126>>>
- **P18 启动流程**：BootROM 硬件初始化→MiniBoot→按 boot.params 选镜像→拷入 RAM 运行。原句："Bootstrap Basic Operation - Hardware Initialization - Memory Diagnostics - Miniboot Selection" <<<PAGE 128>>>
- **P19 目录不一致时的运行规则**：working 与 certified 不同则从 certified 启动；改运行配置需先切回 working。原句："If Working and Certified directories are different, then the switch runs from Certified" <<<PAGE 130-131>>>
- **P20 从 working 重启并回写认证的完整链路**：reload working no rollback-timeout → copy running-config working → copy working certified。原句："-> reload working no rollback-timeout / -> copy working certified" <<<PAGE 132-133>>>
- **P21 R8 用户自定义目录**：可建任意命名的配置目录，可直接保存配置。原句："These directories can have any name… Configuration changes CAN be saved directly to any user-defined directory" <<<PAGE 145>>>
- **P22 R8 运行目录概念**：running directory 是启动来源目录；running configuration 驻留 RAM。原句："Directory from which the switch booted from / It resides in the OmniSwitch RAM" <<<PAGE 146>>>
- **P23 配置回滚机制**：reload from working/user-defined no rollback-timeout 可指定无回滚计时重启。原句："->reload from working no rollback-timeout / ->reload from <userdefined> no rollback-timeout" <<<PAGE 147>>>
- **P24 modify running-directory 切换**：从 certified 启动时无法保存配置，需 modify running-directory working + write memory。原句："When the switch boots from the Certified directory, changes made to the switch cannot be saved" <<<PAGE 148>>>
- **P25 R8 Bash shell 管理**：命令别名存 boot.cfg、内建 Unix 管道过滤。原句："Bash shell is used for all user input / Unix piping mechanisms built into bash redirections" <<<PAGE 150>>>
- **P26 EMP 地址存 boot.cfg**：EMP IP 双 CMM 共享、CMM 自身 IP 存 NVRAM 随板卡走。原句："The EMP IP address is shared between both CMMs and stored in the boot.cfg file" <<<PAGE 153>>>
- **P27 Auto-fabric 七步零接触**：Auto-VC、远程配置、Auto-LACP、Auto-Routing、Auto-SPB、Auto-Network Profiling、Auto-MVRP。原句："AUTO-FABRIC PLUG-N-PLAY ZERO TOUCH DEPLOYMENT 1- Auto-VC … 7- Auto-MVRP" <<<PAGE 155>>>
- **P28 开箱自动配置（RCL）流程**：无 boot.cfg 时 DHCP 取址，DHCP 选项返回 TFTP 服务器与指令文件名，解析执行固件/配置/脚本。原句："DHCP Server will return the path and the filename of an instruction file containing Firmware, Configuration file, Script file" <<<PAGE 157-158>>>
- **P29 OXO 零接触**：OmniPCX Office 通过 DHCP Option 43 下发厂商类与配置文件自动部署 6250-P/6450-P。原句："OmniSwitch vendor class and switch type via DHCP Option 43 / Configuration file download from OXO using DHCP/TFTP" <<<PAGE 161>>>
- **P30 配置快照（snapshot）**：configuration snapshot 捕获配置文本，configuration apply 恢复。原句："Snapshot feature captures switch configurations in a text file / configuration apply filename" <<<PAGE 164>>>
- **P31 CLI 辅助特性**：前缀识别、? 帮助、TAB 补全、30 条历史、100 条命令日志、别名。原句："Command History (up to 30 commands) / Command Logging (up to 100 commands; detailed information)" <<<PAGE 165>>>
- **P32 默认账户体系**：admin 全权限仅 console（密码 switch），default 为新用户模板。原句："Admin - Full privileges - By default, access only allowed through console port / Default - Default privileges given to new user" <<<PAGE 176>>>
- **P33 两类账户**：网管员账户按功能域授权（read-only/read-write + families/domains）；终端用户账户挂 end-user profile 限定端口/VLAN。原句："Network administrator accounts… End-user or customer login accounts - Configured with end-user profiles" <<<PAGE 177>>>
- **P34 密码与锁定策略**：复杂度、历史（0-24）、长度（0-14）、最小/最大年龄、锁定阈值窗口时长。原句："History - Retain 0 to 24 passwords in history / Min Password Length - 0 to 14 char" <<<PAGE 180-181>>>
- **P35 ASA/AAA 认证链**：aaa authentication <service> 后可列最多 3 个备份服务器（含 local），按序轮询。原句："The switch uses the first available server in the list / Up to 3 backups may be specified (including local)" <<<PAGE 185>>>
- **P36 RADIUS 认证与计费分离**：radius-server 定义服务器，accounting session 上报用户行为；源 IP 默认 Loopback0。原句："Interface Loopback0 address if configured, used for the source IP field" <<<PAGE 186>>>
- **P37 NTP 三角色**：交换机可作 NTP 客户端/服务器/对等体，R6/R8 最多 3 个服务器。原句："OmniSwitch can act as an NTP Client, Server, or Peer / 3 max on R6/R8" <<<PAGE 189>>>
## 三、堆叠与虚拟机箱（Day 1）
- **P38 R6 堆叠基本属性**：同家族 2-8 台（6350 最多 4 台）、PoE/非 PoE 可混、单 IP 管理。原句："All of the models in the same family are stackable - Only 6350, or 6450 - 2 to 8 switches in a stack" <<<PAGE 251-252>>>
- **P39 堆叠四角色**：Primary/Secondary/Idle/Pass-Through；Slot-ID 冲突时后来者进 Pass-Through 不阻流量。原句："In case of Slot-ID duplication, the second stared switch gets 'Pass-through' role - It is not part of the stack, but does not block the traffic" <<<PAGE 255>>>
- **P40 Slot-ID 动态分配两法**：无 boot.slot.cfg 时按 15 秒窗口内 MAC 地址法或按启动时间法分配。原句："All switches are interconnected and boot up within a 15s timer (MAC @ method)" <<<PAGE 256>>>
- **P41 stack set slot 修正 Pass-Through**：改 saved-slot 后重启生效。原句："-> stack set slot <current_slot> saved-slot <new_slot>" <<<PAGE 258-259>>>
- **P42 takeover 主备切换**：可从主或备发起，主复位、备升主、最低 Slot 的 Idle 升备；切换前必须同步。原句："takeover - Can be launched from the Primary or Secondary switch / A synchronization has to be done before takeover" <<<PAGE 260>>>
- **P43 堆叠三级同步链**：write memory（RAM→working）→ copy working certified → copy flash-synchro（跨成员同步并自动认证）。原句："-> copy flash-synchro – automatic certification / -> write memory flash-synchro" <<<PAGE 264-268>>>
- **P44 MAC Retention**：堆叠在多次 takeover 后保持主交换机 MAC，避免 STP/LACP/IP 全面重启。原句："Allows a stack of switches to retain the MAC address of the Primary switch… even after multiple takeovers" <<<PAGE 271-272>>>
- **P45 Split Stack Protection（SSP）**：堆叠链双断时经上游 helper 交换机转发 SSP PDU，备份子堆叠关用户端口防双主。原句："If Back-up unit receives SSP PDU, it goes into Split Stack protection mode - Does not assume Primary role - Shuts down ports" <<<PAGE 275>>>
- **P46 虚拟机箱（VC）核心价值**：多台物理交换机经 VFL 互联成单一路由/网桥，单管理 IP，接入-核心间免 STP/VRRP。原句："Virtual Chassis = Group of Switches - Appears as a single router or bridge / No STP/VRRP between Access and Core" <<<PAGE 290>>>
- **P47 VC 组件术语**：VFL（虚拟网链）、Master/Slave、控制 VLAN、Chassis ID、Group ID、Chassis Priority。原句："Single or Aggregated group of ports that connects the switches of the Virtual Chassis" <<<PAGE 292-293>>>
- **P48 VC 模式文件要求**：vcsetup.cfg（机箱 ID/组/VFL）+ vcboot.cfg（通用 VC 配置）须在运行目录。原句："2 files are required for a chassis to operate in Virtual Chassis mode: vcsetup.cfg… vcboot.cfg" <<<PAGE 294>>>
- **P49 Master 选举五级 Criteria**：现任 Master > chassis priority > 最长在线 > 最小 Chassis ID > 最小 MAC。原句："1) Current Master Chassis 2) Higher chassis priority value 3) Longest chassis uptime 4) Smallest Chassis ID value 5) Smallest Chassis MAC address" <<<PAGE 296>>>
- **P50 VC 主备切换与 MAC 保持**：仅 Master 重载，Slave 不受影响；原 Master 回来不重选举；MAC retention 恒开。原句："When the 'original' master comes back, no re-election ('new' Master stays Master) / 'MAC retention' is always enabled" <<<PAGE 297>>>
- **P51 各机型 VC 规格**：6900 最多 6 台 mesh、5 VFL/机箱、16 端口/VFL；6860 最多 8 台 ring、专用 2x20G VFL 口。原句："Max 6 x 6900 per VC - Mesh topology - 5 VFL per chassis / Max. 8 x 6860s per Virtual Chassis - Ring topology" <<<PAGE 299-300>>>
- **P52 6860/6865 混合 VC**：混合上限仍 8 台 ring；6865 10G 口可作 auto-VFL。原句："OS6860/OS6865 mixed VC is supported up to VC of 8 units in ring topology" <<<PAGE 301>>>
- **P53 VC 脑裂检测两法**：RCD（经 EMP 口周期通告，EMP 为必备）与 VCSP（经 helper 的链路聚合发 VCSP PDU，不依赖 EMP）。原句："Remote Chassis Detection (RCD) - Each chassis sends periodic updates via the EMP port / Virtual Chassis Split Detection (VCSP) - EMP Ports not mandatory" <<<PAGE 306-307>>>
## 四、诊断工具（Day 1）
- **P54 swlog 三输出**：console、flash（R6 两文件/R8 最多 8 文件）、syslog socket（R6 4 台/R8 12 台远端）。原句："Switch events can be logged to Switch console -> swlog output console / Local text file -> swlog output flash" <<<PAGE 326-327>>>
- **P55 日志按 appid/子模块调级**：如 swlog appid ospf_0 subapp hello level debug3；默认级别 info(6)。原句："Default severity level is info. The numeric equivalent for info is 6" <<<PAGE 329-331>>>
- **P56 command-log**：与 history 不同，记录命令+结果+用户+IP，存 /flash/command.log，须显式启用。原句："Logs commands and output - Different than command history - Creates command.log file in /flash directory" <<<PAGE 334>>>
- **P57 端口镜像规格**：每机/每堆叠 2 会话、N 对 1 最高 128:1、端口容量须一致。原句："2 per standalone switch and per stack / N-to-1 Mirroring Supported 128 to 1 all models / Port requirements - must be of identical capacity" <<<PAGE 337>>>
- **P58 远程端口镜像（RPM）**：专用 RPM VLAN 承载镜像流量至远端交换机；LACP/LLDP/802.1x/OAM/L3 控制包不被镜像。原句："Achieved by using a dedicated remote port mirroring VLAN / The following types of traffic will not be mirrored" <<<PAGE 338>>>
- **P59 基于策略的镜像**：policy action mirror 按流镜像，可镜像并丢弃原流量。原句："Mirroring is done based on a QoS policy instead of a specific port" <<<PAGE 339-340>>>
- **P60 端口监控（Port Monitoring）**：本机抓包存 Sniffer ENC 格式，截前 64 字节，每机 1 会话。原句："Captures first 64-bytes of frame / Session supported per switch or stack: 1" <<<PAGE 342>>>
- **P61 RMON 四组**：Ethernet Statistics、History、Alarms、Events。原句："4 groups supported: Ethernet Statistics… History Group… Alarms Group… Events Group" <<<PAGE 344>>>
- **P62 show health 资源监控**：CPU/内存收发利用率 1 分/1 时均值与阈值告警。原句："Monitors switch resource utilization and thresholds" <<<PAGE 346>>>
- **P63 sFlow 采样体系**：交换机内嵌 agent + 远端 collector，RFC 3176，用于流量计量/异常检测/容量规划。原句："Traffic flows monitoring and sampling technology embedded within switches / sFlow Agent software process running as part of the switch software" <<<PAGE 348-349>>>
## 五、VLAN 与二层（Day 2）
- **P64 VLAN 本质**：广播域划分，端口经静态/移动认证/802.1q/移动标签入 VLAN。原句："VLAN - Virtual LAN - A broadcast domain / Ports become members of VLANs by Static Configuration, Mobility/Authentication, 802.1q, VLAN Mobile Tag" <<<PAGE 360>>>
- **P65 静态 VLAN 指派**：端口默认 VLAN；出厂全部端口属 VLAN 1。原句："VLAN is assigned to the data port (aka the default VLAN of the port). By default, all ports belong to VLAN 1." <<<PAGE 363>>>
- **P66 动态 VLAN 依规则匹配**：mobile/UNP 口按 VLAN 规则（MAC/网络地址/协议/DHCP）匹配入 VLAN，优先级 MAC>MAC Range>Network>Protocol>Default。原句："1. MAC Address 2. MAC Range 3. Network Address 4. Protocol 5. Default (No Match -> port default VLAN)" <<<PAGE 367-368>>>
- **P67 802.1x 认证 VLAN**：用户经 RADIUS/LDAP/TACACS+ 认证后 MAC 关联目标 VLAN/UNP。原句："Successful login - The client MAC is associated with the correct VLAN or UNP" <<<PAGE 371>>>
- **P68 VLAN 间路由触发**：VLAN 挂 IP 接口即激活路由；VLAN 无活跃端口则操作状态 down。原句："IP routing is active as soon as at least one IP interface is associated with a VLAN" <<<PAGE 373>>>
- **P69 802.1Q 标签结构**：4 字节 tag 含 12bit VLAN ID（4096 个）+3bit 802.1p 优先级。原句："4096 unique VLAN Tags / 802.1P - Three bit field within 802.1Q header - Allows up to 8 different priorities" <<<PAGE 379>>>
- **P70 Mobile Tag 机制**：允许 mobile 口同时收多 VLAN 打标签流量，按 tag 分类，优先于一切 VLAN 规则。原句："Takes precedence over all VLAN Rules / Allows mobile ports to receive 802.1Q tagged packets" <<<PAGE 382>>>
- **P71 VLAN 1 不可删**：默认 VLAN 所有端口初始归属，只能禁用不能删除。原句："This VLAN CANNOT be deleted, but it can be disabled if so desired." <<<PAGE 385>>>
## 六、链路聚合（Day 2）
- **P72 聚合收益与形态**：多物理口合为单逻辑链路，静态 OmniChannel 或动态 802.3ad LACP。原句："Method of aggregating (combining) more than 2 ports/links so that the switch will 'see' them as one logical link" <<<PAGE 394>>>
- **P73 聚合规模规格**：组大小 2/4/8/16；一端口只能属一个聚合组。原句："Number of links per group supported: 2, 4, 8 or16 / One port can only belong to one link aggregation" <<<PAGE 395>>>
- **P74 静态 vs 动态**：静态仅限 OmniSwitch 间、两端参数必须一致；LACP 用 LACPDU 协商、可跨厂商。原句："Static - Port parameters MUST be exactly the same at both ends… Only works between Alcatel-Lucent OmniSwitches / Dynamic - IEEE 802.3ad LACP" <<<PAGE 396>>>
- **P75 actor admin key 两端一致**：动态聚合按 admin key 关联端口，key 值仅本地意义但两端需匹配。原句："Actor admin key must be configured to the same value on both ends of the link aggregation group" <<<PAGE 398-404>>>
- **P76 哈希算法两档**：brief 仅 IP 对、extended 加 UDP/TCP 端口更均匀。原句："Brief Mode: UDP/TCP ports not included / Extended - UDP/TCP ports to be included in the hashing algorithm" <<<PAGE 401>>>
- **P77 组播默认走主端口**：可开 non-ucast 哈希把组播分担到全部成员。原句："Multicast traffic is by default forwarded through the primary port of the Link Aggregation Group" <<<PAGE 402>>>
## 七、STP/RSTP/MSTP（Day 2）
- **P78 STP 目的与默认**：防环+自动重构；OmniSwitch 默认开启 STP。原句："Prevent network loops / Automatic reconfiguration in case of a topology change / STP runs by default on the OmniSwitches" <<<PAGE 414>>>
- **P79 根桥选举四判据**：最低 Root Bridge ID > 最低路径开销 > 最低发送者 Bridge ID > 最低端口 ID。原句："Root bridge decisions based on: Lowest Root Bridge ID - Lowest Root Path Cost - Lowest Sender Bridge ID - Lowest Sender Port ID" <<<PAGE 420-425>>>
- **P80 STP 五状态 vs RSTP 三状态**：802.1D 阻塞/侦听/学习/转发/禁用合并为 802.1w discarding，亚秒收敛。原句："IEEE 802.1D states disabled, blocking, and listening have been merged into a unique 802.1w discarding state" <<<PAGE 420-422>>>
- **P81 RSTP 端口角色**：Root/Designated/Alternate/Backup/Disabled。原句："Alternate Port - Offers an alternate path to the root bridge… Backup Port - Provides a backup connection for the designated port" <<<PAGE 423>>>
- **P82 两种运行模式**：flat（每机一棵树）与 1x1/per-VLAN（每 VLAN 一棵树，默认）。原句："Flat Mode - One STP instance for the entire switch / 1x1 mode - Single STP instance enabled for each VLAN" <<<PAGE 427-429>>>
- **P83 1x1 实例上限**：R6=252、R7=128、R8=100。原句："Maximum VLAN (or Spanning Tree) instances per switch: R6 = 252 R7 = 128 R8 = 100" <<<PAGE 429>>>
- **P84 路径开销 16/32bit**：STP/RSTP 用 16bit（1G=4），MSTP 用 32bit（1G=20000），默认 auto。原句："16-bit when STP/RSTP protocol is active / 32-bit when MSTP protocol is active" <<<PAGE 432>>>
- **P85 PVST+ 互操作**：检测到 PVST+ BPDU 端口自动转 PVST+ 口；需 1x1 模式。原句："Any user port can detect a PVST+ BPDU and become PVST+ port automatically" <<<PAGE 433-434>>>
- **P86 MSTP 实例模型**：CIST(实例 0，默认含全部 VLAN)+最多 16 个 MSTI；一帧 BPDU 携带全部实例。原句："Instance 0 - Always configured on any 802.1s switch… By default, all VLANs are mapped to the CIST / Up to 16 other instances are supported" <<<PAGE 438>>>
- **P87 MST 域三要素**：域名、修订级别、VLAN-实例映射表（BPDU 只传摘要 digest）。原句："Attributes: Region Name - Region Revision Level - VLAN-Instance Mapping table / Only a digest of the VLANs−to−instance mapping table is sent" <<<PAGE 443>>>
- **P88 MST 域边界与跳数**：收到异域/802.1D BPDU 的口成 Region Boundary Port；最大跳数 40 默认 20。原句："The maximum hop count supported is 40, default is 20" <<<PAGE 439-443>>>
- **P89 MSTP 配置最小集**：flat 模式+协议 mstp+region name/revision+msti vlan 映射。原句："-> bridge mode flat / -> bridge protocol mstp / -> bridge mst region name {mst_region_name}" <<<PAGE 444>>>
## 八、DHL 双归属（Day 2）
- **P90 DHL Active-Active 原理**：VLAN 集在两条活跃上行链路间分配，靠 VLAN-链路映射防环，故障时剩余链路接管全部 VLAN。原句："DHL Active-Active splits a number of VLANs between two active links / The forwarding status of each VLAN is modified by DHL to prevent network loops" <<<PAGE 477-478>>>
- **P91 DHL 会话结构**：每机仅一个会话、两条链路（物理口或 linkagg）、公共 VLAN 池、VLAN-链路映射。原句："A DHL session. Only one session per switch is allowed" <<<PAGE 478>>>
- **P92 Pre-emption 定时器与 MAC 冲刷**：0-600 秒；因 DHL 口禁用 STP，需 None/MVRP Enhanced/RAW Flooding 三法清陈旧 MAC。原句："Spanning Tree is automatically disabled on DHL ports / 3 available mechanisms to avoid stale MAC address entries" <<<PAGE 479>>>
- **P93 DHL 与其他冗余方案对比**：STP 50% 带宽、LACP 仅链路冗余、VC 全冗余统一管理、DHL 链路+交换机冗余 100% 带宽。原句："Link redundancy 100% Bandwidth… Switch redundancy" <<<PAGE 481>>>
## 九、高级 IP 接口 / DHCP / LLDP（Day 2）
- **P94 Loopback0 常驻管理口**：不绑 VLAN 恒 up，RIP/OSPF 自动通告（BGP 不），用作 RP、sFlow agent、RADIUS 源 IP、OSPF router-id 等。原句："IP interface with a consistent address for network management purposes - Not bound to any VLAN - Always remains operationally active" <<<PAGE 492>>>
- **P95 可选主管理接口**：ip managed-interface 按应用指定源接口。原句："Applications will be able to choose the source interface IP" <<<PAGE 493>>>
- **P96 DHCP Relay**：ip helper address 指向 DHCP 服务器；ip udp relay 转发 DNS 等指定 UDP 端口。原句："-> ip helper address {Server Addr} / -> ip udp relay DNS" <<<PAGE 498-499>>>
- **P97 LLDP（802.1AB）**：二邻发现协议，默认全交换机使能收发；PDU 为 TLV 结构。原句："L2 discovery protocol - Exchange information with neighboring devices… Enabled by default on the OmniSwitches" <<<PAGE 509-510>>>
- **P98 LLDP-MED 语音扩展**：网络策略（VLAN+802.1p+DSCP）、位置、PoE 管理、库存 TLV；IP 话机经 network-policy 自动入语音 VLAN。原句："Provides VoIP-specific extensions to base LLDP protocol / LAN policy discovery (VLAN, Layer 2 priority, Layer 3 QoS)" <<<PAGE 514-517>>>
## 十、VRRP（Day 3）
- **P99 VRRP 规格要点**：RFC 2338、组播 224.0.0.18、协议号 112、TTL 255、虚拟 MAC 00-00-5E-00-01-{VRID}、最多 255 虚拟路由器。原句："Virtual MAC address: 00-00-5E-00-01-{VRID}" <<<PAGE 524>>>
- **P100 Master/Backup 机制**：最高优先级（默认 100、IP 拥有者直接 Master）为 Master 负责转发与 ARP 应答。原句："It is the router with the highest priority (default = 100; max= 255) / A router becomes the Master if it is the owner of the Virtual router IP address" <<<PAGE 526>>>
- **P101 Master_Down_Interval 与 Skew_Time**：3×通告间隔+偏移；偏移=(256-Priority)/256 防止多 Backup 同时升主。原句："Calculated as: ( 3 * Advertisement_Interval ) + Skew_time" <<<PAGE 527>>>
- **P102 VRRP 负载分担**：两虚拟路由器互为主备，主机按不同默认网关分摊。原句："VRRP can assist in load balancing outgoing traffic" <<<PAGE 528>>>
- **P103 VRRP Tracking**：基于 ADDRESS/IPV4-INTERFACE/PORT/VLAN 策略降优先级触发切换。原句："the VRRP router will adjust to become Master or Slave depending on the associated action" <<<PAGE 531>>>
- **P104 VRRP Group 集体管理**：组内统一改优先级/通告间隔/抢占。原句："Changes the advertising interval value of all the virtual routers on the group" <<<PAGE 533>>>
## 十一、QoS（Day 3）
- **P105 QoS 定义与作用面**：管带宽、可按时段调度；影响接受/丢弃、队列优先、下一跳、整形、802.1p/ToS/DSCP 标记、镜像、超速染色。原句："QoS policies can affect such things as Accept/Drop behavior of a packet - Queuing priority - Next hop for routing - Bandwidth shaping" <<<PAGE 542-543>>>
- **P106 分类引擎位置**：解析器后硬件分类，L2(MAC/VLAN/端口)/L3/L4(SIP/DIP/端口/协议) 条件。原句："CLASSIFICATION ENGINE… L2 (source & dest) - MAC, VLAN… L3/L4 - SIP, DIP, TCP,UDP,IP proto" <<<PAGE 544>>>
- **P107 策略三元组与容量**：Condition+Action+Rule（可选生效时段）；条件/动作各 2048，规则 512(6350/6450)~8192(6900/10K)。原句："Rules (<condition> + <action> + <time valid, optional>) / Conditions = 2048 Actions = 2048" <<<PAGE 545>>>
- **P108 R6 调度三算法**：Strict Priority、WRR（1-15 包，0=严格）、DRR（0-15，按体量 1=10KB）。原句："Weighted Round Robin - User can specify the number of packets to be dequeued (from 1 to 15)" <<<PAGE 547>>>
- **P109 R8 QSet/QSI 模型**：每口 8 单播队列+4 组播队列；QSet Profile 定义 SP/WFQ/EF 组合（Profile1=8SP，Profile2=1EF+7SP，Profile3=1EF+7WFQ）。原句："A QSet is a set of 8 egress Queues that are associated with each port or link Aggregate / 4 Multicast Queues per port - No user configuration" <<<PAGE 548-552>>>
- **P110 策略组复用**：network group/mac group/service group/port group 供条件复用。原句："policy network group netgroup3 173.21.4.0 mask 255.255.255.0 10.10.5.3" <<<PAGE 569>>>
- **P111 Egress 策略列表**：R8 出方向过滤仅支持 policy list type egress。原句："Egress Filtering is only supported on" <<<PAGE 575>>>
- **P112 信任与默认标记**：端口默认 802.1p/DSCP=0；交换口默认不信任，可用 qos phones trusted/qos nms priority 设信任源。原句："By default, the port defaults for 802.1p and ToS/DSCP are 0 / By default, switched ports are not trusted." <<<PAGE 581-590>>>
- **P113 SIP Snooping**：硬件侦听 SIP 信令动态学习 IP 话机 RTP 流并自动加 QoS；默认转发的 SIP 包不受策略。原句："By default, the SIP packets forwarded by hardware are not subject to any" <<<PAGE 601>>>
- **P114 策略删除约束**：被规则引用的 condition/action 不可删。原句："A condition… cannot be deleted if it is currently being used by a policy rule" <<<PAGE 593-594>>>
## 十二、ACL（Day 3）
- **P115 ACL 在策略体系中的位置**：ACL 即策略的过滤子集，与 QoS 共用 condition/action/rule。原句："ACLs are basically a type of QoS policy, and the commands used to configure ACLs are a subset of the switch's QoS commands" <<<PAGE 607-618>>>
- **P116 ACL 作用域**：整机全局、仅入方向、L1-L4 硬件过滤；规则 precedence 0-65535 大者先。原句："Each policy is global to the switch and has a precedence (0..65535) – higher comes first / At ingress only" <<<PAGE 607>>>
- **P117 默认 disposition 全 accept**：bridged/routed/multicast 全局默认与规则默认均为 accept。原句："Global bridged disposition… accept / Global routed disposition… accept" <<<PAGE 610-618>>>
- **P118 established 条件**：检查 ACK/RST 位放行已建 TCP 连接的回程。原句："TCP header information is examined to determine if the ACK or RST flag bit is set" <<<PAGE 615>>>
- **P119 白名单式 L3 ACL 范式**：全局 deny + 精确 accept 规则实现内部防火墙。原句："Globally denies routed traffic on the switch / Allows communication to and from Host1 to subnet 192.168.100.0/0" <<<PAGE 614>>>
## 十三、Access Guardian / UNP / IoT（Day 3）
- **P120 AG 端口自动感知**：同口混布 802.1X 与非 802.1X 设备；R6 需 mobile+802.1x 口、R8 需 UNP bridge 口。原句："Auto-sensing, multi-client authentication on a port - Automatic detection of 802.1X and non-802.1X devices" <<<PAGE 630>>>
- **P121 UNP 角色化访问控制**：VLAN+策略列表(QoS/ACL)+（R8 加 location/period）；用户档案随人走。原句："User Security Profiles follows the user / Security Profiles dynamically applied to switch port" <<<PAGE 631>>>
- **P122 RADIUS Filter-ID 下发 UNP**：Access-Accept 携 UNP 名；无返回时可降级分类规则/默认 UNP/Captive Portal/阻断。原句："Filter-ID = \"UNP-name\" / New connection RADIUS Access-Accept + UNP name" <<<PAGE 632>>>
- **P123 非 supplicant MAC 认证流程**：交换机以源 MAC 为用户名/密码构造 RADIUS 请求。原句："Switch builds auth. Request using source MAC as login/password" <<<PAGE 633>>>
- **P124 R8 分类规则 16 级优先序**：Port>Port+VLAN tag>Domain 组合>MAC>OUI>Range>LLDP>Auth-type>IP>VLAN tag。原句："UNP Port classification rules 1. Port 2. Port + VLAN tag 3. Domain + VLAN tag…" <<<PAGE 638>>>
- **P125 UNP 配置五步**：分类规则→认证服务器→设备分类策略→UNP 档案→端口。原句："Configure UNP Classification Rules / Configure Authentication Server / Configure Device classification policies… Configure UNP profiles / Configure ports" <<<PAGE 640>>>
- **P126 Location/Period 策略（R8）**：按接入位置与时间窗限制角色，不满足自动转未授权角色。原句："the location policy is used to restrict the network access based on the location of the user/device" <<<PAGE 649-650>>>
- **P127 IoT 设备画像三组件**：本地签名收集器+本地 profiler+UNP 画像；用 DHCP 指纹（Option 55/60）与 MAC OUI 识别。原句："IoT device profiling uses DHCP FingerPrinting and MAC OUI to identify IoT devices" <<<PAGE 686-688>>>
- **P128 画像结果联动 UNP**：识别分类后自动指派 UNP；维护已知/未知设备库供管理员补录。原句："When a device gets identified and categorized, the UNP profile can be automatically assigned to the device" <<<PAGE 690>>>
## 十四、PoE（Day 3）
- **P129 动态 PoE 供给**：按需供电至预算上限，优于 IEEE 可选分类。原句："OmniSwitch uses dynamic PoE - Delivers what's needed, up to total budget" <<<PAGE 694>>>
- **P130 PD 分级体系**：802.3af Class 0-3（15.4W 顶）、802.3at Class 4（PSE 34.2W/PD 25.5W）；分级靠 PD 固定电阻。原句："The class of a PD is determined by the PSE via a fixed resistance in the PD" <<<PAGE 695>>>
- **P131 端口优先级三级**：low/high/critical，电力不足按序断电保 critical。原句："Critical: In the event of a power management issue, inline power to critical ports is maintained as long as possible" <<<PAGE 701>>>
- **P132 Capacitor detection 仅老话机**：非 802.3af 兼容，只用于旧 IP 话机。原句："not compatible with IEEE specification 802.3af / It should only be enabled to support legacy IP phones" <<<PAGE 702>>>
- **P133 Priority disconnect**：预算不足时决定新 PD 授电与否。原句："used by the system software in determining whether an incoming PD will be granted or denied power" <<<PAGE 702>>>
- **P134 R8 PoE 命令体系**：lanpower slot/port 两级，service start、admin-state、power 毫瓦、priority。原句："-> lanpower slot 1/1 service start / -> lanpower port 1/1/24 power 18000" <<<PAGE 705>>>
## 十五、路由 RIP/OSPF/GR（Day 4）
- **P135 静态路由优先**：默认静态优于动态；metric 区分主备默认路由。原句："Static routes always have priority over dynamic routes" <<<PAGE 714-716>>>
- **P136 递归静态路由**：follows 指定宿主，网关随动态路由变化；6.7.1 无此选项。原句："Nexthop (or gateway) address no longer must be tied to a particular INTERFACE / Option not available in AOS 6.7.1" <<<PAGE 719-720>>>
- **P137 出接口静态路由**：interface 形式在下一跳常变时手工指定出口。原句："Configure the router to use the exit INTERFACE to handover the packet to neighbor device" <<<PAGE 721>>>
- **P138 RIP 基础参数**：距离向量、跳数 16 不可达、30 秒全表更新、UDP 520、报文 512B/20 路由。原句："Hop count limit of 16 is considered unreachable / Generates updates every 30 seconds / Uses UDP port 520" <<<PAGE 724>>>
- **P139 RIP v1/v2 差异**：v1 有类广播无认证；v2 带掩码/下一跳、组播 224.0.0.9、支持认证。原句："RIP II… Carries additional subnet mask information - Updates sent as Multicasts (224.0.0.9) - Supports authentication" <<<PAGE 724>>>
- **P140 RIP 四定时器**：update 30/invalid 180/garbage 120/holddown 0，且 invalid≥3×update 由 AOS 强制。原句："AOS to enforce the constraint that invalid cannot be less than 3x of update" <<<PAGE 730-731>>>
- **P141 RIP 默认只通告学习路由**：本地/静态路由需 route-map+redist 重分发。原句："Only learned RIP routes and Loopback0 interface are advertised by default. Local routes must be redistributed." <<<PAGE 726>>>
- **P142 OSPF 三数据库**：邻接表、LSDB、OSPF 路由表，SPF 并行计算。原句："Uses three databases: Adjacency Table. List of neighbors / Link State Database. List of routes / OSPF Routing Table. Best routes" <<<PAGE 753>>>
- **P143 Router ID 选择**：默认启动时主地址→首个 up 接口，可 Loopback0 或手工 router-id 覆盖。原句："Can be overridden by the interface 'Loopback0'" <<<PAGE 754>>>
- **P144 OSPF 区域类型**：Stub（无 Type5）、Totally Stubby（仅默认路由）、NSSA（本区可注入外部 Type7）、Transit。原句："Stub areas - Do not carry external routes / Totally stubby areas… only receive the default route from the backbone / Not-so-stubby areas - Allow external routes to be advertised from the area" <<<PAGE 760>>>
- **P145 LSA 类型谱**：1 路由器/2 网络(DR)/3-4 汇总(ABR)/5 外部(ASBR)/7 NSSA 外部/9-11 Opaque（Type9 用于 GR）。原句："AOS software uses Type 9 for graceful restart capability" <<<PAGE 761-762>>>
- **P146 虚链路**：不接骨干的区域经 transit area 建 virtual-link。原句："If an area cannot be physically connected to the backbone, then a virtual-link can be created" <<<PAGE 763>>>
- **P147 AOS 路由偏好默认值**：Local 1/Static 2/OSPF 10/RIP 100/BGP 200，可改。原句："Protocol Route Preference Value… Local 1 Static 2 OSPF 10 RIP 100 BGP 200" <<<PAGE 769>>>
- **P148 GR 原理**：重启路由器保持转发，helper 维持邻接不重算 SPF；Grace LSA 携宽限期。原句："Router remains on forwarding path when restarting / Neighbors must participate in graceful restart" <<<PAGE 772-774>>>
- **P149 GR 三态流程**：发 Grace LSA→同步 LSDB 期间不发 LSA→同步后发更新 LSA 并老化清除 Grace LSA。原句："It does not send any LSA/LSP because it still has incomplete routing information" <<<PAGE 775>>>
## 十六、AOS 网络安全（Day 4）
- **P150 LLDP Rogue Detection**：每口仅一个可信 LLDP agent，超时/重复/多 agent 即违规（trap/shutdown）。原句："Only one trusted LLDP agent on a port / Port will be moved to violation state" <<<PAGE 801-802>>>
- **P151 LPS 目标与支持面**：限制端口学 MAC 数/时窗；支持固定/mobile/tag/认证口，不支持聚合口。原句："Limit the max number of L2 addresses that can be learned on a port… Not supported on Link Aggregate ports" <<<PAGE 804>>>
- **P152 LPS 违规两动作**：restrict 仅滤违规流量、shutdown 全口阻断；默认学 1 MAC、滤 5、违规 restrict。原句："Shutdown. Stops all traffic on a port after violation / Filtering. Only stops traffic from violating device" <<<PAGE 805-806>>>
- **P153 mac-range 白名单与转静态**：每口最多 8 段 MAC 范围；convert-to-static 固化动态 MAC。原句："up to eight MAC ranges per port / Converting the dynamically learned MAC addresses… to static MAC addresses" <<<PAGE 807>>>
- **P154 PBR 硬件重定向**：policy action permanent gateway 覆盖路由表，可本地/远程下一跳。原句："QoS policies that will override the normal routing mechanism for traffic matching the policy condition / Done in hardware" <<<PAGE 811-812>>>
- **P155 PBR 防环路技巧**：回程流量加 source port 条件避免防火墙来回打环。原句："Adding the source port to the condition allows traffic to not get caught in a loop" <<<PAGE 814>>>
- **P156 UserPorts 保留组**：默认防 IP 欺骗（源 IP 与端口网段不符即丢），可扩展过滤 rip/ospf/bgp/bpdu 等。原句："Used by default to prevent spoofed IP addresses on ports / -> qos user-port {filter | shutdown} {spoof|bgp|bpdu|rip|ospf|…}" <<<PAGE 816>>>
- **P157 DropServices 与 port-disable**：服务组批量丢弃（如 tcp135/445）；动作 port-disable 命中即管理性关闭端口，配恢复定时器。原句："Used in conjunction with UserPorts to drop TCP/UDP packets / policy action a1 port-disable" <<<PAGE 817-818>>>
- **P158 DOS 过滤能力**：Ping of Death/SYN/Land/Teardrop 等；ICMP 速率 5 秒窗 >100pps 判攻击。原句："System measures the rate of ICMP requests received over a period of 5 seconds, and detects a DoS attack if the measured rate exceeds 100 pkts/sec" <<<PAGE 821>>>
- **P159 ARP 防御与毒化检测**：未决 ARP 丢弃表防 CPU 过载；仅接受自己请求过的 Reply；受限地址每接口最多 2 个。原句："Creates a drop-entry as soon as it attempts to resolve an ARP / ARP Reply will be accepted only if the Switch had originated a corresponding ARP Request" <<<PAGE 822-824>>>
- **P160 MACsec（802.1AE）**：链路层点对点加密认证，防 DoS/中间人/窃听；Static SA（交换机间）与 Dynamic SA（PSK/EAP）模式。原句："IEEE 802.1AE standard that provides encryption and packet Authentication to IEEE 802.1 frames / MACSec-enabled links are secured by matching security keys" <<<PAGE 826-827>>>
- **P161 DHCP Snooping 双层**：信任口全放行、非信任口只收 Discover/Request；维护绑定库（MAC/IP/租期/VLAN）。原句："Filters DHCP packets between untrusted sources and a trusted DHCP server / Builds and maintains a binding table (database)" <<<PAGE 829-830>>>
- **P162 Option 82**：中继在客户端报文插入 Circuit ID（VLAN+端口）与 Remote ID（路由口 MAC）。原句："Enables the relay agent to insert identifying information into client-originated DHCP packets / Circuit ID: VLAN ID and slot/port… Remote ID: MAC address of the router interface" <<<PAGE 832>>>
- **P163 Port Mapping**：用户口-网络口单向/双向映射隔离终端；可配动态代理 ARP 打通三层数据面。原句："port mapping <id> user-port <slot/port> network-port <slot/port> / port mapping 1 dynamic-proxy-arp enable" <<<PAGE 837-839>>>
- **P164 Storm Control**：广播/组播/未知单播按 %、mbps、pps 三种阈值限洪泛。原句："Configuration of different thresholds for each type of storm/flood traffic / rate % num: rate in % of the port speed" <<<PAGE 886>>>
## 十七、VRF（Day 4）
- **P165 VRF 多实例**：同一物理交换机多个路由实例、可重复 IP；默认 VRF 开机即有。原句："Multiple routing instances within the same physical switch / Ability to use duplicate IP addresses across VRF instances" <<<PAGE 855-859>>>
- **P166 VRF 规模与感知面**：8(6855-U24X)~64（高端）；静态/RIP/OSPF/BGP/PIM/VRRP/QoS/AAA 等均 VRF-aware。原句："64 VRF on OS9000E, 6860(E), 6865, 6900, 9900 and 10K" <<<PAGE 855-856>>>
- **P167 VRF-VLAN 绑定约束**：一接口+其 VLAN 同时只能属一个 VRF；VRF 可挂多 VLAN。原句："A single IP interface, as well as the VLAN associated with the interface, can only belong to one VRF instance at a time" <<<PAGE 861>>>
- **P168 VRF Route Leak**：经 route-map 在 VRF 与 GRT 间导入导出，import 路由偏好可调。原句："VRF Route Leak forwards routes from one VRF routing table to another VRF routing table / -> ip export route-map R1 / -> ip import vrf V1 route-map R2" <<<PAGE 863-864>>>
## 十八、组播（Day 5）
- **P169 组播地址映射**：D 类 224.0.0.0-239.255.255.255，MAC 取 01:00:5e+IP 低 23 位。原句："Least significant 23 bits of IP address are mapped onto the 3 last octets of the MAC address / 224.1.2.3 -> 01:00:5e:01:02:03" <<<PAGE 867>>>
- **P170 IGMP 本地域协议**：TTL=1 永不被路由器转发；查询发 224.0.0.1、离开发 224.0.0.2。原句："IGMP is a protocol confined to the local segment of the LAN and is never forwarded by any router. Always has a Time-To-Live (TTL) of 1" <<<PAGE 871>>>
- **P171 IGMP v1/v2/v3 消息差异**：v2 加 Leave/特定组查询，v3 加源过滤（SSM）。原句："IGMP Source-Specific Join (v3 only) / V3 Membership report (Explicit Host Tracking)" <<<PAGE 872>>>
- **P172 IPMS 硬件交换**：snooping IGMP 按端口建转发表，仅发请求端口；默认禁用。原句："the switch forwards multicast traffic only to the ports that requested it / IPMS is disabled by default" <<<PAGE 875-878>>>
- **P173 Querier forwarding**：流源接在非查询者交换机时启用，全部组播送往查询者。原句："Querier-forwarding feature should be enabled if a streaming device is connected to a switch, which is not a querier" <<<PAGE 879>>>
- **P174 IGMP Throttling**：全局/VLAN/端口三级 max-group，动 none/drop/replace，端口级覆盖。原句："Per port limit overrides VLAN and global configuration" <<<PAGE 885>>>
- **P175 IGMP Relay（helper）**：把 IGMP 报告封装 IP 发往指定主机，不依赖 PIM 传播。原句："Encapsulates IGMP packets in an IP packet to a special device/server" <<<PAGE 884>>>
- **P176 PIM-SM 最小配置**：ip load pim→接口→cbsr→candidate-rp→sparse enable。原句："-> ip pim cbsr <interface_address> / -> ip pim candidate-rp rp_address group-address/prefix_length" <<<PAGE 908>>>
- **P177 PIM SPT 与 RP 阈值**：SPT 默认启用；rp-threshold 决定何时切换源树。原句："-> ip pim spt status enable / -> ip pim rp-threshold value" <<<PAGE 909>>>
## 十九、ERP 与 Intelligent Fabric（Day 5 / 扩展）
- **P178 ERP 机制**：G.8032 环网保护，APS 协议协调防环；RPL owner 负责阻塞/解阻塞。原句："This implementation of ERP uses the Automatic Protection Switching (APS) protocol to coordinate the prevention of network loops within a bridged Ethernet ring" <<<PAGE 926-929>>>
- **P179 ERP 环要素与状态**：ring ID+两口+Service VLAN+MEG level 为必配；RPL 节点只能配在已禁用的环上；状态 Pending（RPL 阻塞、拓扑稳定）/Protected（故障转发）。原句："The RPL node can be configured only on a preexisting disabled ring / Pending: the RPL port is blocking… Protected: on link failure" <<<PAGE 929-930>>>
- **P180 环规模建议**：每环建议最多 16 节点，环数依机型。原句："A maximum number of 16 nodes per ring is recommended." <<<PAGE 929>>>
- **P181 Auto-VC**：无 vcsetup.cfg 时自动 VFL 端口检测、自动 Chassis ID、最低 MAC 为 Master。原句："Auto Chassis ID selection only occurs when there is no vcsetup.cfg / Master selection is then run based on lowest MAC address" <<<PAGE 940>>>
- **P182 RCL 远程配置加载**：Auto-VC 后运行，VLAN 1 和 127 各试 3 次 DHCP 取指令文件；auto-config-abort 取消。原句："RCL tries 6 times, 3 each on VLAN 1 and 127 to get DHCP and download instruction file" <<<PAGE 941>>>
- **P183 Auto-LACP**：LLDP 私有 TLV 发现对端并协商成聚合（默认聚合 127、admin-key 65535）。原句："Propriatery TLV used to detect the peer and, in return, receive peer's system ID / If LACP negotiation succeeds, form a link aggregation" <<<PAGE 943>>>
- **P184 Auto-Routing**：侦听 OSPF/IS-IS Hello 学区域/类型/定时器并自动加载协议建邻接。原句："Protocol network configuration is learned through Hello packets - Determine area, area type, and timers" <<<PAGE 944>>>
- **P185 Auto-fabric CLI 管理**：discovery start、admin-state enable、config-save admin-state enable。原句："-> auto-fabric discovery start / -> auto-fabric admin-state enable" <<<PAGE 951>>>
- **P186 SPB 织构理念**：以 SPB 替代 STP 简化业务开通、提高链路利用率（6865/6900 IFAB）。原句："SPB - Simplified service provisioning, better link utilization compared to STP" <<<PAGE 73>>>
## 二十、代码升级 / MVRP / SLB / 静态聚合（扩展）
- **P187 升级流程铁律**：传镜像入 working→reload from working no rollback-timeout→验证→copy working certified。原句："Reboot the switch forcing it to load from the now upgraded WORKING directory… -> copy working certified" <<<PAGE 965>>>
- **P188 FTP 传输模式**：镜像必须 binary、配置文件必须 ASCII。原句："If you are transferring a switch image file, you must specify the binary transfer mode on your FTP client." <<<PAGE 965>>>
- **P189 USB 灾难恢复**：U 盘建 6900/certified 与 6900/working 目录放备份，根目录放 Trescue.img，miniboot 下 run rescue。原句："Enter the 'run rescue' command from miniboot/uboot and follow the recovery prompts" <<<PAGE 139>>>
- **P190 USB auto-copy**：根目录 aossignature 文件+xxxx/working 目录，自动校验拷贝并从 working 重启，完成后自动禁用防重复升级。原句："Once the switch reboots the auto-copy feature is automatically disabled to prevent another upgrade" <<<PAGE 140>>>
- **P191 MVRP 前提与作用**：裁剪广播/未知单播并动态建管 VLAN；须全局使能且 STP flat 模式。原句："MVRP is used primarily to prune unnecessary broadcast and unknown unicast traffic, and dynamically create and manage VLANs / In order to have MVRP enabled, switch must be in spanning-tree flat mode" <<<PAGE 968>>>
- **P192 MVRP 动态 VLAN 上限**：默认 256，调低需重启 MVRP 生效。原句："By default, the maximum number of dynamic VLANs that can be created using MVRP is 256" <<<PAGE 969>>>
- **P193 SLB 概念**：一组物理服务器逻辑为一个虚拟服务器（VIP 或 QoS 条件集群），线速 L3/L4 分发。原句："Method to logically manage a group of physical servers as one large virtual server (SLB cluster)" <<<PAGE 974-975>>>
- **P194 SLB VIP 代理 ARP**：VIP 须与服务器同网段，集群自动以交换机 MAC 代理 ARP。原句："SLB cluster automatically creates a proxy ARP for the VIP with the switch's MAC address" <<<PAGE 975>>>
- **P195 SLB 权重轮询**：WRR 权重总和 ≤32，weight 0 为备份服务器。原句："Aggregate weight of all servers should not exceed 32" <<<PAGE 977-979>>>
- **P196 SLB 双模式**：VIP 模式（L3 路由/桥接代理 ARP）与 QoS Condition 模式（按策略条件截流如防火墙）。原句："SLB Cluster QoS Condition - Traffic not destined to the server / I.e : firewall server simply inspects the packet" <<<PAGE 981-985>>>
- **P197 SLB 健康监测**：链路状态+ICMP ping+内容验证探针（20 个/switch：ftp/http/https/mail/nntp 等）。原句："Health Monitoring of the servers based on - Ethernet link state detection - IPv4 ICMP ping - Content Verification Probe" <<<PAGE 986-987>>>
- **P198 静态聚合命令差异**：R6 static linkagg/static agg vs R8 linkagg static agg/port；删除前须先清空成员口。原句："you cannot delete a link aggregation group if there" <<<PAGE 999-1002>>>
## 二十一、BGP / IS-IS / 安全认证 / IPv6（扩展）
- **P199 BGP 基本配置链**：router-id→ip load BGP→autonomous-system→neighbor remote-as→status enable；eBGP 多跳与 update-source Loopback0。原句："-> ip bgp neighbor 100.10.1.1 update-source Loopback0 / -> ip bgp neighbor 100.10.1.1 ebgp-multihop" <<<PAGE 1080-1081>>>
- **P200 BGP 策略过滤三列表**：aspath-list/community-list/prefix-list 配合 route-map。原句："-> ip bgp policy aspath-list “100 300 150” permit/deny / -> ip bgp policy community-list 600:1 permit/deny / -> ip bgp policy prefix-list 172.31.0.0 /16 permit/deny" <<<PAGE 1086-1088>>>
- **P201 IBGP 通告原则**：IBGP 学到的路由不应再通告给其他 IBGP 邻居（需全互联或路由反射器）。原句："Routes learned via IBGP should never be" <<<PAGE 1082>>>
- **P202 IS-IS 特性**：链路状态+SPF、两级区域层次、直接跑在二层（802.3/802.2）。原句："IS-IS uses Ethernet 802.3/802.2 instead of the Ethernet II used for IP traffic" <<<PAGE 1093-1096>>>
- **P203 NSAP 寻址**：Area ID+System ID(6B)+NSEL；本地管理 AFI=49；最小 8 字节。原句："The AFI should be set to 49 for locally administered IS-IS configurations" <<<PAGE 1094-1095>>>
- **P204 IS-IS 四类 PDU**：Hello（建邻/选 DIS）、LSP、PSNP（请求/确认）、CSNP（数据库全量同步）。原句："There are 4 types of PDUs: Hello (ESH, ISH, and IIH)… LSP… PSNP… CSNP" <<<PAGE 1096>>>
- **P205 DIS 选举**：仅在有邻接的路由器中按最高优先级/最高 MAC，可抢占，L1/L2 独立选举。原句："DIS election is based on priority and/or the highest MAC address and is preemptive" <<<PAGE 1098-1103>>>
- **P206 IS-IS CLI 模型**：全局 area-id/enable 后按 vlan 使能（ip isis vlan 5 address-family v4）。原句："-> ip isis area-id 49.0001 / -> ip isis vlan 5 / -> ip isis vlan 5 address-family v4" <<<PAGE 1105>>>
- **P207 安全认证章节**：802.1X/MAC 认证、RADIUS/LDAP/TACACS+ 服务器与 aaa test-radius-server 联调命令。原句："-> aaa test-radius-server My_radius type authentication user employee password password" <<<PAGE 677>>>
- **P208 IPv6 地址表示**：128bit，:: 双冒号仅一次；单播/组播/任播三类。原句："Successive fields of 0 can be represented as ::, but only once per address." <<<PAGE 1133-1134>>>
- **P209 链路本地地址**：FE80::/10+64bit 接口 ID，自动生成，用于 ND/路由发现，通信须指定出接口。原句："Link-local addresses have a scope limited to the link and are dynamically created on all IPv6 interfaces" <<<PAGE 1137>>>
- **P210 EUI-64 接口标识**：MAC 中插 FFFE 并翻转 U/L 位。原句："A modified EUI-64 address is formed by 'complementing' the 7th most significant bit (Universal/Local bit)… and inserting 'FFFE'" <<<PAGE 1138>>>
