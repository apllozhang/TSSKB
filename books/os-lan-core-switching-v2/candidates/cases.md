# cases 候选 — DT00XTE216 OmniSwitch LAN Core Switching (Edition 15)

> 实战案例/操作步骤，含 CLI 序列（`>>>`/`->` 命令）与验证方法。

## C-01 ERP 主环（Ring 1）全流程实验：建目录→VLAN→环配置→验证→断链测试
- 页码：<<<PAGE 53>>>-<<<PAGE 58>>>
- 摘录：`sw7 (6870-A) -> erp-ring 1 port1 1/1/3 port2 1/1/27 service-vlan 1001 level 2` / `erp-ring 1 enable`；RPL owner 上 `erp-ring 1 rpl-node port 1/1/27` + `erp-ring 1 wait-to-restore-timer 1`（p55）；验证 `show erp`（Ring State: idle, Ring Node: rpl/non-rpl）；测试 `interfaces 1/1/3 admin-state disable` 观察 ping 不中断（p58）
- 要点：VLAN 1001=Service VLAN，20/30=Protected VLAN；主环 4 节点配置与断链/回切验证。

## C-02 ERP 子环（Ring 2）与 sub-ring-port 配置
- 页码：<<<PAGE 59>>>-<<<PAGE 61>>>
- 摘录：`sw5 -> erp-ring 2 sub-ring-port 1/1/5 service-vlan 1002 level 2` / `erp-ring 2 rpl-node port 1/1/5`；`show erp` 显示 Ring 2 只有一个 ring port（`2 1/1/5 -`）（p60）；VLAN 40 跨子环打 tagged
- 要点：子环节点用 sub-ring-port 单口接入，RPL 在子环上唯一。

## C-03 ERP 实验后恢复（删除工作目录并 reload working）
- 页码：<<<PAGE 62>>>-<<<PAGE 63>>>
- 摘录：`rm -r labERP` → 逐项确认 → `reload from working no rollback-timeout`
- 要点：用户自定义目录实验的标准回收流程。

## C-04 MACsec Dynamic PSK 模式完整配置（6870-A ↔ 6860-B）
- 页码：<<<PAGE 87>>>-<<<PAGE 90>>>
- 摘录：前置 `show interfaces 1/1/27 capability` 查 MACsec Supported/256-bit、`show license-info`（p87）；`security key 1 algorithm aes-cmac-128 hex-key 0x... keyed-name 0x...` → `security key-chain 1` → `security key-chain 1 key 1`（p89）；`interfaces port 1/1/27 macsec mode dynamic key-chain 1 encryption` + `key-rotation max-session-time 10` + `max-exchange-data 20` + `macsec admin-state enable`；验证 `show interfaces macsec dynamic`（Operation Status UP）
- 要点：PSK 双端一致，轮换 10 分钟/20GB。

## C-05 MACsec Static SA 模式配置（sci-tx/sci-rx 交叉 key-chain）
- 页码：<<<PAGE 92>>>-<<<PAGE 94>>>
- 摘录：4 个 aes-gcm-128 密钥 → key-chain 1(key1-2)/key-chain 2(key3-4)；`interface 1/1/25 macsec admin-state enable sci-tx key-chain 1 encryption sci-rx key-chain 2 encryption`（sw7）与对端 tx/rx 互换（sw8）；删除序列 `interface port 1/1/25 macsec admin-state disable → no interfaces port 1/1/25 macsec → no security key-chain 1/2`（p94）
- 要点：本端 tx key-chain = 对端 rx key-chain；`security key-chain gen-random-key` 生成随机密钥。

## C-06 MACsec license 手工安装
- 页码：<<<PAGE 91>>>
- 摘录：`cat > licence.dat`（回车粘贴+CTRL+D）→ `license apply file licence.dat order-id "05200622"` → `show license-info` 出现 MACSEC PERM
- 要点：免费 site license 的落地操作。

## C-07 Private VLAN 双交换机部署与连通性对比测试
- 页码：<<<PAGE 110>>>-<<<PAGE 112>>>
- 摘录：`pvlan 250 admin-state enable` / `pvlan 250 members linkagg 78 isl`（ISL 跨交换机）；`pvlan 250 secondary 251 type community` / `secondary 252 type isolated`（p110）；`pvlan 251 members port 1/1/1 untagged` 后 Client7 ping Client8 成功（community）；改 `pvlan 252 members port 1/1/1 untagged` 后 ping 失败（isolated）（p111-112）；删除 `no pvlan 250 ...`
- 要点：一次实验验证 community 可通、isolated 不可通；show pvlan mapping/members 验证。

## C-08 PVLAN 域内配置示例（含 show pvlan/mac-learning）
- 页码：<<<PAGE 103>>>
- 摘录：`pvlan 100 admin-state enable / pvlan 100 secondary 101 type community / pvlan 100 secondary 103 type isolated / pvlan 100 members port 1/1/20 untagged...`；`show pvlan mapping`、`show pvlan members`（port-type: promiscuous/community/isolated）、`show mac-learning`（全部学在 VLAN 100）
- 要点：secondary VLAN 的 MAC 实际学在 primary VLAN，验证转发模型。

## C-09 PVLAN+链路聚合跨交换机扩展示例
- 页码：<<<PAGE 105>>>
- 摘录：`linkagg lacp agg 1 size 2...` + `pvlan 100 members linkagg 1 isl`
- 要点：ISL 用 linkagg 承载 primary+secondary 全部流量。

## C-10 MSTP 实验：6360 虚拟机箱+MST 域+实例+负载分担
- 页码：<<<PAGE 141>>>-<<<PAGE 149>>>
- 摘录：`spantree mode flat` → `spantree mst region name lab_region` → `spantree mst region revision-level 1` → `spantree protocol mstp`（p141）；`spantree msti 1 / msti 2` + `spantree msti 1 vlan 20 / msti 2 vlan 30`（p143）；`show spantree msti vlan-map`（CIST: 1-19,21-29,31-4094）；负载分担 `spantree msti 1 priority 16384`（sw7）/ `msti 2 priority 16384`（sw8）（p146）；回退 `spantree mode per-vlan` + `no spantree mst region name` + `no spantree msti 1/2`（p149）
- 要点：完整 MSTP 生命周期含验证与还原。

## C-11 MSTP 官方双交换机配置示例（含端口优先级）
- 页码：<<<PAGE 128>>>
- 摘录：`spantree cist priority 4096 / msti 1 priority 4096 / msti 2 priority 8192` + 端口级 `spantree msti 1 1/1/1 priority 1 / msti 2 1/1/1 priority 15`
- 要点：交换机优先级+端口优先级双层控制根/根口。

## C-12 MSTP 流量分担三交换机示例
- 页码：<<<PAGE 130>>>、<<<PAGE 129>>>
- 摘录：A/B/C 各自在一个 MSTI 上 priority 4096 做根；`show spantree mst port` 显示 DESG FORW / ALT BLK 角色分配（p129）
- 要点：不同 VLAN 组走不同链路的验证输出。

## C-13 MVRP 动态 VLAN 传播实验
- 页码：<<<PAGE 160>>>-<<<PAGE 164>>>
- 摘录：`spantree mode flat` + `mvrp enable` + `mvrp linkagg 7 enable / mvrp port 2/1/3 enable`（p160）；`mvrp maximum-vlan 150`（p161）；6360 建 VLAN 40 后 6870/6860 `show vlan` 出现 `40 dyn`，`show vlan 40 members` 端口 dynamic tagged（p162）；`no vlan 40` 报 "ERROR: Dynamic vlan 40 cannot be deleted"（p163）；禁用 `mvrp ... disable` 后 VLAN 40 消失；回退 `spantree mode per-vlan`
- 要点：动态 VLAN 全生命周期演示。

## C-14 Port Mapping 双向会话实验（user→指定 network 口）
- 页码：<<<PAGE 202>>>
- 摘录：`port-mapping 1 user-port 1/1/1 network-port linkagg 7` + `enable` → client 只能 ping 到 linkagg 7 对端 6870-A；`port-mapping 2 user-port 1/1/2 network-port 2/1/3` → 只能 ping 6860-B；`port-mapping 1 user-port 2/1/1` 追加端口；`port-mapping 2 user-port 2/1/1` 报 "ERROR: port user already part of an existing PMAP session"
- 要点：会话隔离与端口独占验证；删除 `no port-mapping 1`。

## C-15 MAC Forced Forwarding（dynamic-proxy-arp）CLI 示例
- 页码：<<<PAGE 186>>>
- 摘录：`port-mapping 1 user-port 1/1/1-2 network-port linkagg 8` / `port-mapping 1 dynamic-proxy-arp enable` / `dhcp-snooping vlan 20 admin-state enable` / `port-mapping 1 enable`；`show port-mapping status`（Direction: bi, DPA Status: enable）
- 要点：MFF 三件套（port-mapping+DHCP snooping+动态代理 ARP）。

## C-16 Learned Port Security 三阶段实验（限1 MAC→静态化→shutdown）
- 页码：<<<PAGE 207>>>-<<<PAGE 210>>>
- 摘录：`port-security port 1/1/8 admin-state enable`（默认 maximum 1, violation RESTRICT, max-filtering 5）→ show port-security 显示多余 MAC filtering（p207）；`port-security port 1/1/8 convert-to-static` 固定当前设备（p208）；`violation shutdown` + `max-filtering 0` → 再学即 "Port-security Violation on PORT 1/1/8 : Shutting down port"（p209）；`show violation`（Recovery Time 300）；`violation port 1/1/8 recovery-time 30` 修改；`clear violation port 1/1/8` 手工恢复（p210）
- 要点：含 L2 协议干扰排除（关 STP/LLDP 后 flush mac-learning）。

## C-17 LPS 标准绑定示例（maximum 1 + shutdown + convert-to-static）
- 页码：<<<PAGE 193>>>
- 摘录：`port-security port 1/1/1 admin-state enable / maximum 1 / violation shutdown / convert-to-static enable`
- 要点：一次成型的最小端口安全模板。

## C-18 UDP Relay 配置与统计
- 页码：<<<PAGE 170>>>-<<<PAGE 171>>>
- 摘录：`ip udp relay port port_num [description]` / `ip udp relay service {tftp|tacacs|ntp|...} vlan vlan_id / address ip_address`；`show ip udp relay`（DNS port 53 → Vlan 20）、`show ip udp relay statistics`
- 要点：按服务/端口指定 VLAN 与服务器单播地址。

## C-19 静态路由与默认路由（含备份 metric）
- 页码：<<<PAGE 222>>>
- 摘录：`ip static-route 134.1.21.0/24 gateway 10.1.1.1` / `ip static-route 0.0.0.0/0 gateway 10.1.1.1` / metric 1 与 metric 2 双默认路由互备
- 要点：`show ip router database` 中 inactive 静态路由展示（p223）。

## C-20 RIP 最小配置与重分发
- 页码：<<<PAGE 228>>>
- 摘录：`ip load rip` → `ip rip interface if_name admin-state enable` → `ip rip admin-state enable`；重分发 `ip route-map rip_1 sequence-number 50 action permit / match ip-address 0.0.0.0/0` + `ip redist local into rip route-map rip_1 admin-state enable` + `ip redist static into rip...`
- 要点：默认只通告学到的 RIP 路由和 Loopback0，本地/静态路由必须重分发。

## C-21 OSPF Backbone 搭建（Loopback0+router-id+area 0+接口入域）
- 页码：<<<PAGE 325>>>-<<<PAGE 330>>>
- 摘录：`ip interface Loopback0 address 192.168.254.1` → `ip load ospf` → `ip router router-id 192.168.254.1` → `ip ospf area 0.0.0.0` → `ip ospf interface int_217` → `ip ospf interface int_217 area 0.0.0.0` → `admin-state enable` → `ip ospf admin-state enable`；验证 `show ip ospf`（# of Full State Nbrs=1）、`show ip ospf lsdb`（rtr/net LSA）、`show ip ospf interface`（DR/BDR）
- 要点：骨干区邻居、LSDB、DR 选举三步验证。

## C-22 OSPF 多区域+Virtual Link 打通被分割的骨干
- 页码：<<<PAGE 332>>>-<<<PAGE 339>>>
- 摘录：区域配置 `ip ospf area 1.1.1.1` + 接口入域（p332）；虚链路 `sw1 -> ip ospf virtual-link 1.1.1.1 192.168.254.2`（对端用 Loopback0 router-id）双向配置（p338）；验证 `show ip ospf virtual-link`（State P2P/Full, up）与跨骨干路由表
- 要点：两个独立骨干经 transit area 用虚链路互联的完整案例。

## C-23 OSPF local/static 路由重分发实验
- 页码：<<<PAGE 347>>>-<<<PAGE 352>>>
- 摘录：`ip route-map localIntoOspf sequence-number 10 action permit / match ip-address 192.168.120.0/24 permit` + `ip redist local into ospf route-map localIntoOspf admin-state enable`（p347）；静态默认路由重分发 `staticIntoOspf ... match ip-address 0.0.0.0/0 permit` + `ip redist static into ospf...`（p351）；验证 `show ip ospf routes` 中 Type 列出现 AS-Ext (E2)
- 要点：local/static → OSPF 的两类重分发与 E2 路由识别。

## C-24 OSPF Simple/MD5 接口认证配置
- 页码：<<<PAGE 353>>>-<<<PAGE 354>>>
- 摘录：Simple：`ip ospf interface int_217 auth-type simple` + `auth-key alcatel`（双端）；MD5：`auth-type md5` + `md5 1` + `md5 1 key alcatel`；单端配置后出现 "ospfAuthCheck: Intf 172.16.17.1: Auth type 1 mismatch!"，双端配好后 Full
- 要点：认证不匹配的日志证据与恢复。

## C-25 OSPF Stub Area 配置与验证
- 页码：<<<PAGE 355>>>-<<<PAGE 356>>>
- 摘录：`ip ospf area 4.4.4.4 type stub`（双端一致）；6560 上 `show ip ospf routes` 只有 Intra/Inter + 一条 `0.0.0.0/0 ... Inter` 默认路由（ABR 注入）
- 要点：stub 内路由表被默认路由替代的实证。

## C-26 OSPF 故障排查：swlog 提升日志级别定位 Hello 不匹配
- 页码：<<<PAGE 292>>>-<<<PAGE 294>>>
- 摘录：`swlog appid ospf_0 subapp all level debug3`（subapp 列表 1=ERROR...14=HELLO...）；`show log swlog | grep ospf_0` 显示 "HELLO from 192.168.0.2 discarded...invalid helloInterval 10"（本端 20 对端 10）；改一致后 Full State Nbrs=1
- 要点：日志分级排障法（OSPF 邻居无法 Full 的经典案例）。

## C-27 DHCP Relay（IP Helper）配置与验证
- 页码：<<<PAGE 368>>>-<<<PAGE 369>>>
- 摘录：`ip dhcp relay destination 192.168.100.102` + `ip dhcp relay admin-state enable`；`show ip dhcp relay`（Max hops 16、Opt82 Format Base MAC）；`show ip dhcp relay statistics`（Reception From Client / Tx Server 计数）
- 要点：可 per-VLAN 配置以对接不同 DHCP 服务器（p369 Tips）。

## C-28 IPMS 组播交换开关实验（ flooding vs 按需转发）
- 页码：<<<PAGE 405>>>-<<<PAGE 409>>>
- 摘录：默认 `show ip multicast` Status=disabled，发送组播后端口计数显示 M-cast Frames 泛洪到全 VLAN（p406）；`ip multicast admin-state enable`（三台）+ 服务器侧 `ip multicast querying enable` + 其余 `ip multicast querier-forwarding enable`（p407-408）；`show ip multicast group/forward` 精确到 231.1.1.5 的端口级表项
- 要点：前后对比证明 IPMS 只发向加入端口。

## C-29 DVMRP 最小配置
- 页码：<<<PAGE 419>>>
- 摘录：`ip load dvmrp` → `ip dvmrp interface <name>` → `ip dvmrp admin-state enable` → `write memory`
- 要点：与 PIM 二选一（每接口仅一个组播协议）。

## C-30 PIM-SM 全网配置（cbsr+candidate-rp+接口启用）
- 页码：<<<PAGE 447>>>-<<<PAGE 449>>>
- 摘录：`ip load pim` + `ip pim sparse admin-state enable`（4 台）；`ip pim interface int_217/int_212/int_110...`；`ip pim cbsr 192.168.110.1` 等；`ip pim candidate-rp 192.168.110.1 231.1.1.0/24`（分组 RP）；验证 `show ip pim neighbor / group-map`（BSR 学到 6 条 RP）、`show ip pim sgroute`（S,G 建立）
- 要点：BSR 域内多 RP 分组任播配置。

## C-31 Anycast RP 配置（Loopback1 共享地址 + static-rp + anycast-rp 集）
- 页码：<<<PAGE 648>>>-<<<PAGE 649>>>
- 摘录：RP1/RP2 均 `ip interface "Loopback1" address 10.10.10.1`；全网所有 PIM 路由器 `ip pim static-rp 231.0.0.0/8 10.10.10.1`；RP 上 `ip pim anycast-rp 10.10.10.1 192.168.254.1`（自身 Loopback0）+ 对端 `... 192.168.254.7`
- 要点：静态 RP 配置必须全域所有 PIM 路由器（含非 RP）。

## C-32 VRF 创建与双 VRF 隔离/泄漏实验
- 页码：<<<PAGE 466>>>-<<<PAGE 470>>>
- 摘录：`vrf create ipone` → `ip interface int_190 address 192.168.190.1/24 vlan 190`；两 VRF 客户端默认互 ping 失败（p467）；泄漏 `ip route-map "vlan190" sequence-number 50 action permit / match ip-address 192.168.190.0/24 redist-control all-subnets permit` + `ip export route-map vlan190` + `ip import vrf iptwo route-map vlan200`（p468）；`show ip global-route-table`（vrf ipone/iptwo 条目）；default↔VRF 泄漏 `ip import vrf default all-routes`（p470）
- 要点：GRT 作为中转的 VRF 互访与 default VRF 泄漏。

## C-33 BGP eBGP 双 AS 互联与重分发实验
- 页码：<<<PAGE 512>>>-<<<PAGE 517>>>
- 摘录：`ip load bgp` → `ip bgp autonomous-system 100` → `ip bgp neighbor 192.168.12.2 remote-as 200` → `admin-state enable` → `ip bgp admin-state enable`（p515）；重分发 `ip route-map switch1bgp sequence-number 10 action permit` + `ip redist ospf into bgp route-map switch1bgp` + `ip redist local into bgp...`（p516）；验证路由表出现 EBGP 路由（p517）
- 要点：两个 AS 各跑 OSPF，BGP 传 AS 间路由。

## C-34 BGP 邻居基于 Loopback0 建立与 MD5
- 页码：<<<PAGE 499>>>-<<<PAGE 500>>>
- 摘录：`ip bgp neighbor 100.10.1.1 update-source Loopback0` / `ebgp-multihop`；`ip bgp neighbor <ip> md5 key` + `status enable`；`show ip bgp neighbors`（Oper state: estab）
- 要点：IBGP/EBGP 用环回口加固会话。

## C-35 SPB 骨干+L2 服务部署实验（BVLAN/ISIS/SAP/I-SID）
- 页码：<<<PAGE 548>>>-<<<PAGE 556>>>
- 摘录：骨干 `spb bvlan 2000/2001/2002` + `spb isis bvlan 2000 ect-id 1...`（p548）；`spb isis admin-state disable` → `spb isis control-bvlan 2000` → 各口 `spb isis interface port 1/1/x` → `spb isis admin-state enable`（p548）；服务 `service spb 2001 isid 2001 bvlan 2001 description vlan2 admin-state enable`；接入 `service access port 1/1/3` + `service spb 2001 sap port 1/1/3:2 admin-state enable stats enable`（p555-556）；验证 `show mac-learning domain spb`（CMAC 绑定 sap:/sdp: 接口）（p558）
- 要点：ISID 全局一致、service 号本地有效；跨 BEB 的 L2 VPN 打通。

## C-36 SPB 监控命令族（adjacency/spf/nodes/unicast-table）
- 页码：<<<PAGE 549>>>-<<<PAGE 550>>>
- 摘录：`show spb isis bvlans / interface / adjacency [detail] / info / unicast-table bvlan 2000 / spf bvlan 2000 [bmac <BMAC>] / database / nodes`
- 要点：SPB 骨干健康检查命令清单。

## C-37 iFab Auto-Fabric 管理命令
- 页码：<<<PAGE 639>>>
- 摘录：`auto-fabric protocols lacp|spb|mvrp|loopback-detection admin-state disable`、`show auto-fabric config`、`auto-fabric discovery start`、`auto-fabric admin-state enable`、`auto-fabric config-save admin-state enable`
- 要点：自动化协议的开关与保存策略。

## C-38 软件升级流程（含 uboot/FPGA）
- 页码：<<<PAGE 676>>>-<<<PAGE 680>>>
- 摘录：升级步骤链 "Analyse Requirements on the release note → FTP the Upgrade Files → Upgrade the image → Verify → Certify → Upgrade uboot and/or FPGA if mandatory"；`update uboot cmm all file u-boot.8.4.1.R03.141.tar.gz` / `update fpga-cpld cmm all file fpga_kit_3312` / `reload from working no rollback-timeout` / `copy running certified`（p680）
- 要点：certified 前可回滚的升级安全网。

## C-39 IS-IS 最小配置
- 页码：<<<PAGE 697>>>
- 摘录：`ip load isis` → `ip isis admin-state enable` → `ip isis area-id 49.0001` → `ip isis activate-ipv4` → `ip isis vlan 5` → `ip isis vlan 5 address-family v4` → `ip isis vlan 5 admin-state enable`
- 要点：单区域 IS-IS 启用模板；`show ip isis adjacency/route/spf`（p698）。

## C-40 SLB 集群配置（VIP+WRR+probe）
- 页码：<<<PAGE 655>>>-<<<PAGE 658>>>、<<<PAGE 667>>>
- 摘录：`ip slb admin-state enable` → `ip slb cluster Web vip 128.241.130.204` → `ip slb server ip 128.241.130.127 cluster Web`；备份场景 `weight 1` + `weight 0`（p657）；探测 `ip slb probe http_test http` + `ip slb cluster C1 vip ... ` + `ip slb server ip ... probe http_test`（p667）
- 要点：服务器 loopback 装 VIP（Windows/Linux 附录 p671-672）。
