# Verified 候选（V1 原文真实性核对 + V2/V3 抽查）

## cases

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

## counter-examples

## X-01 ERP：RPL 节点缺失或多个 = 非法配置；RPL 只能配在已禁用的环上
- 页码：<<<PAGE 55>>>
- 摘录："The RPL node can be configured only on a preexisting disabled ring. The non-existence of a RPL node or the existence of multiple RPL nodes is considered as incorrect configuration."
- 教训：每环有且只有一个 RPL；先建环（未 enable）再配 rpl-node。
## X-02 ERP：每环建议最多 16 节点，环数受机型限制
- 页码：<<<PAGE 55>>>
- 摘录："The maximum number of rings per node that can be created depends on switch model... A maximum number of 16 nodes per ring is recommended."
- 教训：超规模环网不可预期，需查 Network Configuration Guide。
## X-03 MACsec Static 模式不支持 OS6860N；VFL 堆叠口不支持 MACsec
- 页码：<<<PAGE 75>>>、<<<PAGE 72>>>
- 摘录："* MACsec - Static mode is not supported on OS6860N."（p75）；"MACsec not supported on OS6870-24 VFL stacking port 25/26 & OS6870-48 VFL stacking port 49/50"（p72）
- 教训：选型前核对平台矩阵；堆叠口链路不能加密。
## X-04 MACsec：64X10G 分支光模块/扩展模块不支持；9900 多板卡仅 Static
- 页码：<<<PAGE 71>>>
- 摘录："Expansion modules (Not supported on any 4X10G splitter transceivers)"；"OS9900-CMM 4X10G (Static mode only) / OS9900-XNI-48/P48 10G ports (Static mode only)" 等
- 教训：动态模式覆盖因板卡而异，部署前逐板卡确认。
## X-05 MVRP 仅支持 STP flat 模式；端口类型受限
- 页码：<<<PAGE 154>>>、<<<PAGE 160>>>
- 摘录："MVRP is supported only in STP flat mode"（p154）；"MVRP can be configured only on fixed, 802.1 Q and aggregate ports. It cannot be configured on mirror, unp, VPLS Access, and VLAN Stacking User ports"（p160 Notes）
- 教训：1x1 per-VLAN 模式下 MVRP 无法启用。
## X-06 MVRP 动态 VLAN 删不掉（会被自动重建）
- 页码：<<<PAGE 163>>>
- 摘录："sw5 -> no vlan 40 / ERROR: Dynamic vlan 40 cannot be deleted... The mvrp status is equal to the dyn. That means the VLAN 40 has been automatically re-created."
- 教训：必须先在源端删 VLAN 或禁用 MVRP，否则动态 VLAN 反复重建。
## X-07 MVRP：动态 VLAN 不建 IP 接口、不映射 MSTI；改 max-vlan 需重启 MVRP
- 页码：<<<PAGE 163>>>、<<<PAGE 161>>>
- 摘录："there's no ip interface creation nor association with MSTI"（p163）；"If the VLAN limit to be set is less than the current number of dynamically learned VLANs, then the new configuration will take effect only after the MVRP is disabled and enabled again"（p161）
- 教训：MVRP 只管二层连通，L3/MSTP 需手工补配。
## X-08 MSTP：1X1 与 MSTP 不能共存，必须 flat 模式
- 页码：<<<PAGE 143>>>
- 摘录："1X1 and MSTP cannot be configured at the same time; and the switch must be configured in flat Spanning Tree mode."
- 教训：切 MSTP 前先 `spantree mode flat`，实验后记得还原 per-vlan（p149）。
## X-09 MSTP 优先级必须是 4096 的倍数
- 页码：<<<PAGE 146>>>
- 摘录："Priority has to be multiple of 4096 (8192, 12288, 16384, …, 61440)"
- 教训：随意填值不生效。
## X-10 Port Mapping：一个端口只能属于一个会话
- 页码：<<<PAGE 202>>>
- 摘录："sw5 -> port-mapping 2 user-port 2/1/1 / ERROR: port user already part of an existing PMAP session"
- 教训：跨会话复用端口直接报错（单向会话的 network 口除外，见 p199）。
## X-11 LPS 不支持链路聚合端口；交换机自身多 MAC 会挤占学习额度
- 页码：<<<PAGE 190>>>、<<<PAGE 206>>>-<<<PAGE 207>>>
- 摘录："Not supported on Link Aggregate ports"（p190）；"there's 3 mac addresses: 1 from client 3 and 2 from 6560. The 6560 uses different mac addresses for Layer 2 traffic, like LLDP or STP and another one... for Layer3 traffic"（p206）
- 教训：对端交换机的 LLDP/STP/IP 多个源 MAC 会导致 restrict 误过滤，需关协议或 flush 后重学。
## X-12 LPS：convert-to-static 必须在设备 MAC 已学到之后执行
- 页码：<<<PAGE 208>>>
- 摘录："Please notice that the device must be learned on the LPS port before to enter the command port-security convert-to-static"
- 教训：先发流量再固化，否则无 MAC 可转静态。
## X-13 链路聚合加端口前必须清掉端口上的 VLAN 配置
- 页码：<<<PAGE 316>>>
- 摘录："sw5 -> linkagg lacp port 2/1/3 actor admin-key 8 / ERROR: Port cannot be added to Linkagg, please remove other configuration on this port"；随后 `no vlan 58/20/30 members port 2/1/3` 再加成功
- 教训：端口有 VLAN membership 时不能入聚合组。
## X-14 OSPF：单端先开认证会立刻丢邻居（Auth type mismatch）
- 页码：<<<PAGE 353>>>
- 摘录："+++ ospfAuthCheck: Intf 172.16.17.1: Auth type 1 mismatch! recvd pkt = (0)"；邻居从 2 个掉到 1 个，双端配置一致后恢复 Full
- 教训：生产开认证需两端窗口期内同步操作。
## X-15 OSPF：Hello Interval 不一致导致邻居无法 Full
- 页码：<<<PAGE 293>>>-<<<PAGE 294>>>
- 摘录："HELLO from 192.168.0.2 discarded...invalid helloInterval 10"（本端 20/对端 10）；"# of Full State Neighbors = 0"
- 教训：邻居参数（hello/dead/area/认证）必须完全一致；用 swlog debug 定位。
## X-16 OSPF stub 区域：两端 area type 必须一致；stub 内看不到外部路由
- 页码：<<<PAGE 355>>>-<<<PAGE 356>>>
- 摘录："sw7 -> ip ospf area 4.4.4.4 type stub" 与 "sw3 -> ip ospf area 4.4.4.4 type stub" 双端同配；"Switches in Stub Areas do not have external routes in their routing database"（p355 Notes）；6560 路由表无 AS-Ext，仅默认路由（p356）
- 教训：一端 stub 一端 normal 邻居起不来；stub 内依赖 ABR 默认路由出行。
## X-17 RIP：local/static 路由默认不通告，漏重分发=路由缺失
- 页码：<<<PAGE 228>>>
- 摘录："Only learned RIP routes and Loopback0 interface are advertised by default. Local and or static routes must be redistributed."
- 教训：RIP 网络里直连网段不自动外宣，必须 route-map+redist。
## X-18 递归静态路由的网关随目标路由变化，需防环路
- 页码：<<<PAGE 225>>>
- 摘录："The gateway to reach the 2.2.2.2 network has changed through RIP; so, the gateway to reach the 172.30.0.0 network has also changed"
- 教训：follows 目标路由翻动时静态路由随之漂移，设计时要确保 follow 目标稳定。
## X-19 私有 VLAN：一个 Primary VLAN 只能有一个 Isolated VLAN
- 页码：<<<PAGE 109>>>
- 摘录："There can be only one Isolated VLAN within one Primary VLAN."
- 教训：需要多组互不相通的用户时应使用多个 community，而不是多个 isolated。
## X-20 私有 VLAN 删除顺序（先成员后主 VLAN）
- 页码：<<<PAGE 112>>>
- 摘录："no pvlan 252 members port 1/1/1 / no pvlan 250 members linkagg 78 / no pvlan 250"
- 教训：直接删 primary 前需清理成员引用；实验后 `write memory flash-synchro` 保存。
## X-21 MACsec 与 ERP/组播等特性并存的许可前置：无 license 时功能不可用
- 页码：<<<PAGE 87>>>
- 摘录："If the licence MACsec is not available on the switch, refer to the appendix section to install it."
- 教训：实验/部署前 `show license-info` 预检，避免配置到一半失败。
## X-22 VRF：VLAN 只能属于一个 VRF；default 与自定义 VRF 的 import 需 all-routes
- 页码：<<<PAGE 460>>>、<<<PAGE 470>>>
- 摘录："Once a VLAN is associated with a specific VRF instance, configuring an interface for that VLAN within the context of any other instance, is not allowed. Use of Duplicate VLAN numbers is not supported"（p460）
- 教训：VLAN/VRF 归属是单向一对一，跨 VRF 复用同 VLAN 号会冲突。
## X-23 VRF 隔离的本意：不配 route leak 时跨 VRF 永远不通
- 页码：<<<PAGE 467>>>
- 摘录："Ping each other to test connection between them. What happens and why?"（两 VRF 客户端互 ping 失败）；"We will not be able to ping an IP interface of another VRF instance from one VRF instance within the same switch even the leaked routes are existed. This is due to security reason"（p468）
- 教训：即使路由已泄漏，交换机本机跨 VRF 接口 ping 也不通（安全设计），只能由客户端侧经验证。
## X-24 SPB：ISID 全局必须一致，BVLAN 映射也须一致
- 页码：<<<PAGE 555>>>
- 摘录："The ISID number is globally significant and must match across all BEBs connecting a given service. The BVLAN that the service is mapped must also match across all BEBs... Each ISID can be attached to one BVLAN only."
- 教训：service 号本地随意但 ISID/BVLAN 全局强一致，错配服务不通。
## X-25 SPB：control BVLAN 只能在协议禁用时修改；BVLAN 上无 STP
- 页码：<<<PAGE 548>>>
- 摘录："Control BVLAN can only be changed when protocol is disabled. There is no Spanning Tree on BVLANs"
- 教训：生产改 control BVLAN 需先 `spb isis admin-state disable`；BVLAN 域不要指望 STP 防环。
## X-26 SPB：BVLAN 数量不要超过物理等价路径数
- 页码：<<<PAGE 610>>>
- 摘录："There is no advantage in creating more BVLANs than the number of equal-cost-paths in the physical topology. Moreover... creates an additional unnecessary load in the CP"
- 教训：盲目建满 16 个 BVLAN 反而拖慢收敛。
## X-27 SPB：不同 VLAN 映射同一服务会导致 MAC 漂移（mac-move）
- 页码：<<<PAGE 610>>>
- 摘录："Duplicate MAC addresses in different VLANs do not collide, however, if these VLANs are mapped to the same SPB service... those MACs will be constantly learned, re-learned and flushed. This is known as a 'mac-move' and should be avoided"
- 教训：一个 VLAN 一个 ISID/SAP，避免虚拟化环境重复 MAC 引起震荡。
## X-28 动态服务默认 Service Modulo 512 会把不同 VLAN 混入同一服务
- 页码：<<<PAGE 601>>>
- 摘录："using the default Service Modulo of 512 can result in up to 8 different VLAN tags being mapped to the same service... it will result in different VLAN traffic being bridged in the same L2 domain. To ensure L2 isolation, we can change the Service Modulo to 4096"
- 教训：多租户/需隔离场景必改 modulo。
## X-29 聚合口 hash 在 SPB 场景熵不足
- 页码：<<<PAGE 611>>>
- 摘录："SPB backbone ports use MAC-in-MAC encapsulation which means MAC addresses are the BMACs... In most cases this does not create enough entropy and the load will not be spread evenly... a 'tunnel-protocol' option can be selected"
- 教训：SPB+LAG 必开 tunnel-protocol 哈希内层 CMAC/IP。
## X-30 Overload 状态开启后即使无替代路径也不转发
- 页码：<<<PAGE 605>>>
- 摘录："once the overload state is enabled on a node no traffic will transit through the node even if there are no alternative paths"
- 教训：维护隔离是硬隔离，确认冗余路径后再设 overload。

## frameworks

## F-01 ERP 环网配置五步法（方法论框架）
- 页码：<<<PAGE 45>>>、<<<PAGE 46>>>、<<<PAGE 47>>>-<<<PAGE 49>>>
- 摘录："ERP CONFIGURATION Step by Step — Create ERP Ring, Service VLAN & MEG Level / Configure the RPL Port / Add Protected VLAN(s) / Enable the ERP Ring"；"Define a MEG Level (Management Entity Group) Value from 0 to 7. Must be identical on all the switches belonging to the ERP Ring"（p47）
- 内容：建立 ERPv2 环网的完整决策序列：①建环+Service VLAN+MEG Level（全网一致）→②唯一 RPL 端口与 RPL Owner→③加入受保护 VLAN→④admin-state enable。适合作为环网部署 checklist。
## F-02 ERP 状态机三态模型（idle / Protection / Pending）
- 页码：<<<PAGE 40>>>-<<<PAGE 42>>>、<<<PAGE 56>>>
- 摘录："idle: the RPL port is blocking... Protection: on link failure... the RPL node is now forwarding... Pending: The node is recovering from failure. When a node is in pending state, the WTR timer will be running"（p56 Notes）；稳态 NR/RB、故障 SF、恢复 NR+WTR（默认 5 分钟）见 p40-42
- 内容：用 R-APS 消息（NR/RB、SF）+ WTR/Guard 定时器解释环网三态转换，可提炼为故障定位与收敛判断的通用状态机框架。
## F-03 MACsec 部署模式决策树（Static SA / Dynamic PSK / Dynamic EAP）
- 页码：<<<PAGE 67>>>、<<<PAGE 75>>>、<<<PAGE 76>>>、<<<PAGE 78>>>-<<<PAGE 80>>>
- 摘录："Available Modes — Static SA Mode – Switch-to-Switch links / Dynamic SA Mode – Switch-to-Switch links / Switch-to-Host links (Using EAP)"（p67）；Static 模式管理步骤 "Get or generate Random Keys → Create security keys → Create key-chain → Associate security key to key-chain → Configure sci-tx/sci-rx... enable MACsec"（p75）；Dynamic PSK 步骤见 p78
- 内容：按"对端是交换机还是主机、是否能用 MKA 动态协商"选择三种模式；Static 不支持 OS6860N（p75 注）。
## F-04 MACsec 密钥轮换策略（时间 + 流量双触发）
- 页码：<<<PAGE 77>>>、<<<PAGE 89>>>
- 摘录："MACsec supports protocol key-rotation based on: Session time (in min) for SAK regeneration (5 minutes – 120 minutes) / Exchange data... (5GB –1000GB). Both values can be configurable in the same command, and whichever happens first will trigger the key exchange."
- 内容：安全运营中 SAK 轮换的双重门限设计：`macsec key-rotation max-session-time` + `max-exchange-data`，先到先触发。
## F-05 OSPF Area 设计决策框架（Standard/Stub/Totally Stubby/NSSA 边界）
- 页码：<<<PAGE 253>>>-<<<PAGE 254>>>、<<<PAGE 267>>>-<<<PAGE 270>>>
- 摘录："Main benefit of creating areas > reduce the number of routes to propagate"（p254）；Stub "Type 5 LSAs are not propagated into the stub area. Instead, R2 (ABR) injects a Type 3 LSA containing a default route"（p268）；Totally Stubby "Neither do the Type 3 LSAs. All routing out of the area relies on a single default route"（p269）；NSSA "Stub & Totally Stubby... Con: Neither type can contain an ASBR... Type 7 LSAs = Type 5 LSAs in disguise"（p270）
- 内容：按"区域内是否需要外部路由/是否有 ASBR/能接受多少 LSA"四象限选型。
## F-06 OSPF 配置七步法（含重分发）
- 页码：<<<PAGE 275>>>-<<<PAGE 280>>>
- 摘录："0) CONFIGURING THE ROUTER-ID ... 1) LOADING THE SOFTWARE ip load ospf 2) CREATING AN AREA 3) SPECIFYING AN AREA TYPE 4) CREATING AN OSPF INTERFACE 5) ASSIGNING AN INTERFACE TO AN AREA ... 6) REDISTRIBUTING LOCAL & EXTERNAL ROUTES 7) ENABLING OSPF"
- 内容：AOS R8 上启用 OSPF 的标准顺序，router-id 先行、最后统一 enable。
## F-07 路由重分发两步法（先 Route Map 后 Redistribution）
- 页码：<<<PAGE 272>>>-<<<PAGE 273>>>、<<<PAGE 300>>>
- 摘录："STEP 1: Configuring Route Maps — A Route Map is composed of Action / Match / Set"；"STEP 2: Configuring Route Redistribution... Redistribution configured > Router becomes ASBR"（p273）；"Route map: Criteria that is used to control redistribution of routes between protocols"（p300）
- 内容：Route Map（name+sequence+action+match+set）→ `ip redist <src> into <dst> route-map` 的通用重分发工作流。
## F-08 MSTP 配置六步法
- 页码：<<<PAGE 121>>>-<<<PAGE 126>>>
- 摘录："MSTP CONFIGURATION Step by Step — Select the Flat Spanning Tree mode / Select the MSTP protocol / Configure MST regions (name, revision level) / Configure MSTIs / Map VLANs to MSTI / Manage Switch Priority"
- 内容：flat 模式 → MSTP 协议 → region name+revision（三要素一致才同域：name/revision/VLAN 映射，p123）→ 建 MSTI → 映射 VLAN → 调优先级实现负载分担。
## F-09 Learned Port Security 配置四步法与违例决策
- 页码：<<<PAGE 190>>>-<<<PAGE 193>>>
- 摘录："Steps to Configuring LPS: Enable LPS on a port / Set the number of learned Mac's / Set the time limit for LPS / Select the violation mode"；"Violation options — Block only traffic that violates LPS port restrictions... Shutdown the port"（p190）
- 内容：端口安全部署框架：maximum（默认 1）、max-filtering（默认 5）、violation restrict/shutdown、convert-to-static 固定当前设备。
## F-10 环路防护/环网替换选型：STP vs SPB 决策框架
- 页码：<<<PAGE 521>>>-<<<PAGE 523>>>、<<<PAGE 565>>>
- 摘录："Unused links... Sub-optimal paths... Lack of a coordinated control plane... Slow convergence"（p521）；SPB-M 优势 "All network links are use with no loops / Spanning Tree Protocol replacement / Uses the shortest path end to end / 100's ms convergence times"（p523）
- 内容：从链路利用率、路径最优性、控制平面、收敛时间四个维度对比 STP 与 SPB-M，指导园区核心是否引入 SPB。
## F-11 SPB 骨干搭建四任务框架
- 页码：<<<PAGE 547>>>、<<<PAGE 548>>>
- 摘录："Backbone configuration entails the following tasks: Creating one or more BVLANs with their associated ECT-IDs... Defining the control BVLAN / Defining one or more SPB IS-IS interfaces / Enabling the SPB IS-IS protocol"
- 内容：BVLAN+ECT 分配（每 BVLAN 用不同 ECT 最大化分流，p548 best practice）→ control BVLAN（仅协议禁用时改，p548）→ ISIS network port → 全局 enable。
## F-12 iFab 零触摸部署流水线（Auto-VC→RCD→LACP→Routing→SPB→Profiling→MVRP）
- 页码：<<<PAGE 624>>>、<<<PAGE 626>>>-<<<PAGE 638>>>
- 摘录："1- Auto-VC 2- Automatic remote configuration 3- Auto-LACP 4- Auto-Routing 5- Auto-SPB Fabric 6- Auto-Network Profiling 7- Auto-MVRP"；"If not established configuration deleted & disabled"（p624）
- 内容：出厂交换机七阶段自动化框架；任一阶段邻居建立失败则自动回退删除配置。BVLAN 默认 4000-4015/ECT 1-16、控制 BVLAN 4000（p633）。
## F-13 VRF 部署与路由泄漏（Route Leak）框架
- 页码：<<<PAGE 458>>>-<<<PAGE 462>>>、<<<PAGE 468>>>-<<<PAGE 470>>>
- 摘录："VRF names are case sensitive... A default VRF instance is automatically configured"（p458）；"VRF Route Leak forwards routes from one VRF routing table to another VRF routing table... Route maps are used to import and export routes from the VRFs to the GRT (Global Routing Table)"（p461）
- 内容：vrf create → 接口归属 → 源 VRF export route-map → 目标 VRF import vrf <name> route-map，用于共享服务/跨租户受控互访。
## F-14 BGP 邻居策略匹配流程（policy list → route-map → peer in/out）
- 页码：<<<PAGE 505>>>-<<<PAGE 508>>>
- 摘录："AS Path, Community and Prefix lists / Route map... Route-maps evaluation... NO-> Routes dropped + Evaluation stopped"（p506 流程图）
- 内容：aspath-list/community-list/prefix-list 定义匹配条件 → route-map 组合 → `ip bgp neighbor <ip> route-map <name> in|out` 挂到邻居，控制出入路由。
## F-15 SLB 服务器负载均衡部署框架（VIP/权重/健康探测）
- 页码：<<<PAGE 655>>>-<<<PAGE 658>>>、<<<PAGE 665>>>
- 摘录："Enable SLB globally... Configure the SLB cluster / Assign physical servers to the SLB cluster / Modify optional parameters... Distribution algorithm / Health monitoring"（p655）；WRR "Aggregate weight of all servers should not exceed 32"（p656）；8.9R4 auto-bypass/wait-to-restore（p665）
- 内容：VIP 集群 → server+weight（0 为备份）→ probe 健康监测 → auto-bypass 容灾的完整框架。

## glossary

> 术语 | 中文解释 | 首次出现页码（聚焦本书核心专题：ERP/MACsec/PVLAN/MSTP/MVRP/安全/OSPF/路由重分发/组播/SPB）

## ERP / 环网

| 术语 | 解释 | 页码 |
|---|---|---|
| ERP (Ethernet Ring Protection) | 以太网环网保护协议，环内防环并实现约 50ms 快速故障恢复 | <<<PAGE 37>>> |
| RPL (Ring Protection Link) | 环保护链路，环内正常状态下被阻塞以防环路的那条链路 | <<<PAGE 38>>> |
| RPL Owner | 持有 RPL 端口的交换机，负责稳态阻塞/故障时解阻塞 RPL 口 | <<<PAGE 38>>> |
| R-APS message | 环自动保护倒换消息，在 Service VLAN 内传递 | <<<PAGE 38>>> |
| SF (Signal Fail) | R-APS 消息类型，检测到链路/节点故障时宣告 | <<<PAGE 38>>> |
| NR / RB (No Request / RPL Blocked) | 无请求消息及 RPL 已阻塞标记，恢复完成时由 RPL Owner 发出 | <<<PAGE 40>>> |
| WTR (Wait To Restore) timer | 等待恢复定时器，默认 5 分钟，防链路抖动引发反复倒换 | <<<PAGE 42>>> |
| Guard Timer | 守护定时器（默认 50 厘秒），丢弃过期 R-APS 防误倒换 | <<<PAGE 56>>> |
| Service VLAN | 环级 VLAN，承载 R-APS 消息和 ETH CCM | <<<PAGE 38>>> |
| Protected VLAN | 加入 ERP 环、转发状态由 ERP 决定的业务 VLAN | <<<PAGE 38>>> |
| MEG Level | ERP 管理实体组级别 0-7，环内所有交换机必须一致 | <<<PAGE 47>>> |
| Laddered / Subtending Ring | 主环+子环的梯形结构，子环借主环虚通道闭合 | <<<PAGE 43>>> |

## MACsec

| 术语 | 解释 | 页码 |
|---|---|---|
| MACsec (IEEE 802.1AE) | 二层链路加密与认证标准，点到点保护直连节点间流量 | <<<PAGE 67>>> |
| SecTag | MACsec 报文头（8/16 字节），含密钥信息、包号与安全通道标识（EtherType 0x88E5） | <<<PAGE 68>>> |
| ICV (Integrity Check Value) | GCM-AES 生成的 16 字节完整性校验值 | <<<PAGE 68>>> |
| SCI (Secure Channel Identifier) | 安全通道标识，收发通道各一，需与对端交叉匹配 | <<<PAGE 69>>> |
| SAK (Secure Association Key) | 安全关联密钥，加密数据平面流量 | <<<PAGE 69>>> |
| Key-chain | 密钥链，聚合多个 security key 供 sci-tx/sci-rx 引用 | <<<PAGE 69>>> |
| Static SA Mode | 手工配置最多 4 把 SA 密钥的交换机间静态模式 | <<<PAGE 75>>> |
| MKA (MACsec Key Agreement) | IEEE 802.1X-2010 密钥协商协议，动态生成 SAK | <<<PAGE 76>>> |
| CAK (Connectivity Association Key) | 连接关联密钥，保护 MKA 控制平面；EAP 模式经 RADIUS VSAs 下发 | <<<PAGE 76>>> |
| Key rotation | SAK 轮换，按会话时长（5-120 分钟）或流量（5-1000GB）先到先换 | <<<PAGE 77>>> |

## Private VLAN / MSTP / MVRP

| 术语 | 解释 | 页码 |
|---|---|---|
| Private VLAN (PVLAN) | 在单广播域内划分子域实现二层隔离的特性 | <<<PAGE 98>>> |
| Primary / Secondary VLAN | PVLAN 主 VLAN（对外）与从 VLAN（isolated/community 两类） | <<<PAGE 99>>> |
| Isolated VLAN | 隔离型二级 VLAN，成员间二层完全不通，仅到 promiscuous 口；每 Primary 仅一个 | <<<PAGE 99>>>、<<<PAGE 109>>> |
| Community VLAN | 社区型二级 VLAN，同社区可互通、跨社区不通 | <<<PAGE 99>>> |
| Promiscuous port | 混杂端口，属 Primary VLAN，可与所有端口通信 | <<<PAGE 100>>> |
| PVLAN ISL | 跨交换机延伸 PVLAN 域的级联口，同时承载主/从 VLAN | <<<PAGE 100>>> |
| MSTP (IEEE 802.1s) | 多生成树协议，多 VLAN 映射到少量实例 | <<<PAGE 115>>> |
| MSTI (MST Instance) | 多生成树实例（最多 16 个），VLAN 按需映射 | <<<PAGE 116>>> |
| CIST / IST | 公共与内部生成树（实例 0），未映射 VLAN 默认归属，承载全部实例 BPDU | <<<PAGE 115>>>、<<<PAGE 118>>> |
| MST Region | 多生成树区域，name+revision+VLAN 映射三要素一致才同域 | <<<PAGE 117>>> |
| Flat / per-vlan (1x1) mode | 单树 flat 模式（MSTP/MVRP 前置）与每 VLAN 一树模式，二者互斥 | <<<PAGE 122>>>、<<<PAGE 143>>> |
| MVRP (IEEE 802.1ak) | 多 VLAN 注册协议，跨桥接网动态传播 VLAN 成员（近似 GVRP） | <<<PAGE 152>>> |
| Registrar / Applicant mode | MVRP 端口注册模式（normal/fixed/forbidden）与申请者模式 | <<<PAGE 154>>>、<<<PAGE 155>>> |
| Dynamic VLAN (dyn) | 由 MVRP 自动学习创建的 VLAN，不建 IP 接口、不映射 MSTI | <<<PAGE 162>>>、<<<PAGE 163>>> |

## 网络安全

| 术语 | 解释 | 页码 |
|---|---|---|
| DoS Filtering | 交换机内置 DoS 攻击过滤（PoD/SYN/Land/Teardrop/ICMP>100pps 等） | <<<PAGE 168>>> |
| ARP Poisoning Detection | ARP 欺骗检测，识别未请求应答/伪造请求，restricted-address 每接口最多 2 个 | <<<PAGE 176>>>、<<<PAGE 177>>> |
| Local Proxy ARP | 本地代理 ARP，per-VLAN 用路由口 MAC 应答所有请求 | <<<PAGE 179>>> |
| ARP filter | ARP 过滤，按 sender/target 与 allow/block 控制代理应答 | <<<PAGE 180>>> |
| Port Mapping | 端口映射会话，user 口彼此隔离仅经 network 口通信，最多 8 会话 | <<<PAGE 182>>> |
| MFF (MAC Forced Forwarding, RFC 4562) | MAC 强制转发，同子网主机 ARP 一律指向网关（DHCP snooping+port mapping+动态代理 ARP） | <<<PAGE 185>>> |
| Storm Control (flood-limit) | 风暴控制，按 bcast/mcast/uucast 限速（pps/mbps/cap%），违例 shutdown/trap | <<<PAGE 188>>> |
| LPS (Learned Port Security) | 学习型端口安全：限 MAC 数量/学习窗/违例 restrict 或 shutdown；不支持聚合口 | <<<PAGE 190>>> |
| convert-to-static | 将端口已学动态 MAC 固化为静态，锁定当前设备 | <<<PAGE 193>>> |
| pkt-relay | LPS 报文中继，学习期被截获报文重注入转发路径 | <<<PAGE 196>>> |
| UDP Relay | 通用 UDP 端口中继，按服务端口转发到指定 VLAN/IP | <<<PAGE 170>>> |

## IP 路由 / OSPF

| 术语 | 解释 | 页码 |
|---|---|---|
| Loopback0 | 环回接口，管理/协议标识用，RIP/OSPF 自动通告（BGP 不） | <<<PAGE 216>>> |
| Recursive static route (follows) | 递归静态路由，下一跳跟随某目标主机路由动态解析 | <<<PAGE 224>>> |
| RIP | 距离矢量协议，跳数度量，16 跳不可达，UDP 520，更新 30s/失效 180s | <<<PAGE 227>>> |
| Router database / route-pref | 路由数据库与协议优先级（Local 1/Static 2/OSPF 110/RIP 120/EBGP 190…） | <<<PAGE 223>>>、<<<PAGE 299>>> |
| Router ID | OSPF 路由器标识：手工指定 > Loopback0 > 最高接口 IP | <<<PAGE 240>>> |
| DR / BDR / DROther | 指定/备份指定路由器（优先级+RouterID 选举）与普通路由器；组播 224.0.0.5/224.0.0.6 | <<<PAGE 242>>> |
| DBD / LSR / LSU / LSAck | OSPF 数据库描述/请求/更新/确认包，邻接同步四件套 | <<<PAGE 245>>>、<<<PAGE 246>>> |
| LSA Type 1/2 | 路由器 LSA（每路由器域内泛洪）与网络 LSA（DR 生成） | <<<PAGE 260>>>、<<<PAGE 261>>> |
| LSA Type 3 (Summary) | 汇总 LSA，ABR 生成跨区域通告网段；也承载区域路由汇总 | <<<PAGE 262>>>、<<<PAGE 286>>> |
| LSA Type 4 (Summary ASBR) | ASBR 汇总 LSA，ABR 通告到 ASBR 的位置 | <<<PAGE 264>>> |
| LSA Type 5 (External) | 外部 LSA，ASBR 重分发的域外路由；外部聚合由 ASBR 完成 | <<<PAGE 263>>>、<<<PAGE 287>>> |
| LSA Type 7 (NSSA) | NSSA 外部 LSA，ABR 转换为 Type 5 出域 | <<<PAGE 265>>> |
| ABR / ASBR / BB / IR | 区域边界路由器（汇总）/自治系统边界路由器（重分发）/骨干/内部路由器 | <<<PAGE 256>>>-<<<PAGE 258>>> |
| Stub / Totally Stubby Area | 末梢区域（拒 Type4/5，ABR 注入 Type3 默认路由）/完全末梢（再拒 Type3） | <<<PAGE 268>>>、<<<PAGE 269>>> |
| NSSA | 非纯末梢区域，允许 ASBR 用 Type7 引入外部路由 | <<<PAGE 270>>> |
| ECMP | 等价多路径，按流负载分担，AOS 最多 4 条，不支持逐包 | <<<PAGE 285>>> |
| Virtual Link / Transit Area | 虚链路与穿越区域，跨非骨干区延伸 Area 0 | <<<PAGE 289>>> |
| Graceful Restart (Grace LSA) | 平滑重启，重启期间邻居维持邻接避免全网 SPF；OSPF/ISIS 默认关、BGP 默认开 | <<<PAGE 361>>>、<<<PAGE 363>>> |
| Route Map (action/match/set) | 路由图：动作+匹配+修改，重分发过滤核心；序列自上而下命中即停 | <<<PAGE 300>>>、<<<PAGE 304>>> |

## 组播

| 术语 | 解释 | 页码 |
|---|---|---|
| Class D / 01:00:5E | 组播地址 224.0.0.0-239.255.255.255，IP 低 23 位映射组播 MAC | <<<PAGE 375>>> |
| IPMS (IP Multicast Switching) | IP 组播交换，硬件 IGMP 侦听按端口转发 | <<<PAGE 377>>> |
| IGMP (v1/v2/v3) | 因特网组管理协议；v2 加 Leave/特定组查询，v3 加源过滤；TTL=1 本地段协议 | <<<PAGE 381>>>、<<<PAGE 382>>> |
| IGMP Querier / querier-forwarding | 查询器（每 LAN 一个）与查询器转发（组播定向到查询器交换机） | <<<PAGE 380>>>、<<<PAGE 389>>> |
| IGMP Throttling (max-group) | 每端口/VLAN/全局限制学习组数，动作 none/drop/replace | <<<PAGE 396>>> |
| RPF (Reverse Path Forwarding) | 逆向路径转发校验，只在指向源的接口收包 | <<<PAGE 413>>>、<<<PAGE 426>>> |
| PIM-SM / PIM-DM | 稀疏模式（显式加入+RP 共享树）/密集模式（泛洪-剪枝 3 分钟循环、无 RP） | <<<PAGE 426>>>、<<<PAGE 434>>> |
| RP (Rendezvous Point) | 汇聚点，共享树根，源以 Register 单播封装发往 | <<<PAGE 428>>> |
| RPT / SPT switchover | 共享树/最短路径树；末跳 DR 收到首包后自动发起 SPT 切换 | <<<PAGE 428>>>-<<<PAGE 430>>> |
| BSR / C-RP | 自举路由器/候选 RP 的动态 RP 发现机制（优先级→hash→IP 选 RP） | <<<PAGE 431>>>、<<<PAGE 432>>> |
| Anycast RP (RFC 4610) | 多 RP 共享任播 Loopback 地址实现负载分担与 IGP 级快速切换；仅 PIM-SM、最多 8 台 | <<<PAGE 643>>>-<<<PAGE 645>>> |

## VRF / BGP

| 术语 | 解释 | 页码 |
|---|---|---|
| VRF | 虚拟路由转发，一台物理交换机多路由实例、地址可重叠；VLAN 只能归属一个 VRF | <<<PAGE 453>>>、<<<PAGE 460>>> |
| GRT / VRF Route Leak | 全局路由表及经 route-map 的 VRF 间路由导入导出 | <<<PAGE 461>>> |
| BGP-4 (RFC 4271) | 边界网关协议，AS 间路径矢量协议，TCP 179 | <<<PAGE 476>>> |
| IBGP / EBGP | AS 内/AS 间 BGP 邻居关系；IBGP 学的路由不再传给其他 IBGP 邻居（水平分割） | <<<PAGE 478>>>、<<<PAGE 501>>> |
| AS-PATH / Next-HOP / Origin | BGP 必选属性：AS 列表/下一跳/来源（IGP>EGP>Incomplete） | <<<PAGE 484>>>-<<<PAGE 487>>> |
| Local Preference / MED | 选出口偏好（越高越优）与入流量入口建议（越低越优、仅两 AS 间传递） | <<<PAGE 488>>>、<<<PAGE 491>>> |
| Community (NO-EXPORT/NO-ADVERTISE) | 路由打标分组属性，控制通告范围 | <<<PAGE 494>>>、<<<PAGE 496>>> |
| BGP synchronization | 同步：IBGP 学的路由须 IGP 可达才通告给 EBGP | <<<PAGE 502>>> |

## SPB / iFab / 其他

| 术语 | 解释 | 页码 |
|---|---|---|
| SPB / SPB-M (IEEE 802.1aq) | 最短路径桥接（MAC-in-MAC 变体），IS-IS 控制平面，全链路可用 | <<<PAGE 523>>>、<<<PAGE 525>>> |
| PBB (IEEE 802.1ah) | 运营商骨干桥接，MAC-in-MAC 封装（Ethertype 0x88E7） | <<<PAGE 526>>>、<<<PAGE 567>>> |
| BEB / BCB | 骨干边缘桥（封装/解封装、终结服务）/骨干核心桥（仅按 BMAC 转发、不学客户 MAC） | <<<PAGE 527>>> |
| BVLAN (B-VID) | 骨干 VLAN，承载控制与服务流量，最多 16 个；其上无 STP | <<<PAGE 527>>>、<<<PAGE 569>>> |
| I-SID | 24 位服务实例标识，区分租户/VPN，可达 16M | <<<PAGE 527>>>、<<<PAGE 565>>> |
| ECT / ECT-ID | 等价树及编号，用于各 BVLAN 建 SPT 时的 tie-break 分流 | <<<PAGE 569>>> |
| SAP / SDP | 服务接入点（物理口+封装值绑定服务）/服务分发点（通向远端 BEB，自动创建） | <<<PAGE 527>>>、<<<PAGE 572>>> |
| Head-End / Tandem replication | SPB BUM 复制模式：头端多单播复制（默认）/串联按组播 FDB 分叉复制 | <<<PAGE 539>>>、<<<PAGE 573>>> |
| LBD (Loopback Detection) | 环回检测，发探测帧防接入层环路，检测到即关闭端口 | <<<PAGE 609>>> |
| VPN Lite / L3 VPN (SPB) | SPB 上叠跑 OSPF/BGP 的边界方案 / IS-IS TLV 携带 VRF 路由的域内方案 | <<<PAGE 534>>>、<<<PAGE 536>>>、<<<PAGE 592>>> |
| iFab (Auto-VC/RCD/LACP/Routing/SPB/Profiling/MVRP) | 出厂默认七阶段零触摸自动化家族；失败自动回退 | <<<PAGE 624>>> |
| DIS / Pseudo node | IS-IS 指定中间系统/伪节点（对应 OSPF DR，可抢占；Hello 9s，DIS 3s） | <<<PAGE 689>>>、<<<PAGE 690>>> |
| NSAP (Area/System-ID/NSEL) | IS-IS 的 OSI 地址结构，本地管理 AFI=49，最小 8 字节 | <<<PAGE 686>>> |
| DHL (Dual-Home Link) | 双归链路，无 STP/LAG 的接入-核心快速倒换冗余 | <<<PAGE 318>>>、<<<PAGE 607>>> |
| Virtual Chassis (VC) / VFL | 虚拟机箱/虚拟机箱链路，多台堆叠为一逻辑设备 | <<<PAGE 134>>> |
| SLB / VIP / WRR | 服务器负载均衡：集群虚拟 IP（代理 ARP 应答）与加权轮询（权重 0 备份、总权重≤32） | <<<PAGE 653>>>-<<<PAGE 656>>> |
| write memory flash-synchro | 保存配置并同步备份 Flash 的 AOS 命令 | <<<PAGE 112>>> |
| working / certified directory | AOS 双镜像目录，reload from working/certified 支持升级回滚 | <<<PAGE 53>>>、<<<PAGE 680>>> |

## principles

## ERP（以太网环网保护）
### P-01 ERP 基本原理与 RPL 阻塞机制
- 页码：<<<PAGE 37>>>、<<<PAGE 38>>>、<<<PAGE 40>>>
- 摘录："Protection switching mechanism / Maintains a loop-free topology in a ring / Fast recovery times (~50 ms)... AOS OmniSwitch supports ERPv2"（p37）；"Ring Protection Link (RPL): Link between 2 ring switches that is blocked to prevent a loop... RPL Owner: Blocks traffic on the RPL Port during normal ring operations"（p38）；稳态 "Blocked RPL port... NR (No Request) RB (RPL blocked)"（p40）
- 内容：环内唯一被阻塞的链路是 RPL，由 RPL Owner 在稳态阻塞，防止二层环路。
### P-02 R-APS 消息体系（SF/NR/NR-RB）
- 页码：<<<PAGE 38>>>、<<<PAGE 41>>>、<<<PAGE 42>>>
- 摘录："R-APS (Ring-Automatic Protection Switching) Messages — Signal Fail (SF): Declared when a failed link or node is detected / No Request (NR): Declared when there are no outstanding conditions"（p38）；故障时 "Adjacent ports are blocked / Signal Failure (SF) R-APS message is sent / RPL Owner unblocks RPL port"（p41）；恢复 "Adjacent nodes remove SF and send NR... RPL Owner starts a Wait To Restore (WTR) timer (default: 5 minutes)... RPL Owner sends NR/RB"（p42）
- 内容：SF 触发保护倒换、NR+WTR 触发回切、NR/RB 重新阻塞 RPL。
### P-03 ERP 恢复的 WTR/Guard 定时器
- 页码：<<<PAGE 42>>>、<<<PAGE 56>>>
- 摘录："RPL Owner starts a Wait To Restore (WTR) timer (default: 5 minutes)"（p42）；show erp 输出列 "WTR Timer (min) 5, Guard Timer (csec) 50"（p56）
- 内容：WTR 默认 5 分钟防抖动回切；Guard 定时器 50 厘秒用于丢弃过期 R-APS 消息防震荡。
### P-04 Laddered Ring（ERPV2 子环）虚通道原理
- 页码：<<<PAGE 43>>>
- 摘录："The Main ring is a fully closed ring... The Subtended ring does not include any shared links with the main ring. The Main ring acts as a virtual channel to close the Subtended ring. R-APS messages are sent over the virtual channel using the S-tag (Service VLAN) of the subtended ring"
- 内容：子环借主环虚通道闭合，R-APS 用子环 Service VLAN 的 S-tag 传递。
### P-05 ERP 环规模与端口约束
- 页码：<<<PAGE 55>>>
- 摘录："A maximum number of 16 nodes per ring is recommended... Physical switch ports and logical link aggregate ports can be configured as ERP ring ports"；"The non-existence of a RPL node or the existence of multiple RPL nodes is considered as incorrect configuration"
- 内容：每环最多建议 16 节点；环端口可为物理口或链路聚合逻辑口；每环有且仅有一个 RPL。
## MACsec
### P-06 MACsec（IEEE 802.1AE）目标与保护范围
- 页码：<<<PAGE 67>>>、<<<PAGE 86>>>
- 摘录："Prevents DoS/ M-in-M/playback attacks, intrusion, wire-tapping, masquerading... Secure most of the traffic on Ethernet links – LLDP frames, LACP frames, DHCP/ARP packets"；"IEEE standard (802.1AE-2006) for encryption over Ethernet. Encrypt and authenticate all traffic in a LAN with GCM-AES-128"（p86）
- 内容：点到点链路加密+认证，覆盖二三层及控制协议帧。
### P-07 MACsec 报文结构与防重放
- 页码：<<<PAGE 68>>>
- 摘录："MACsec packet Specific EtherType (0x88E5) / 8-byte or 16-byte SecTag header containing information about the decryption key, a packet number and Secure Channel Identifier / Payload (which may be optionally encrypted) / Integrity Check Value (ICV) generated by GCM-AES of size 16 bytes / Packets are numbered to avoid replay"
- 内容：SecTag+可选加密载荷+16 字节 ICV，包编号防重放。
### P-08 SCI/SA/SAK 安全关联模型
- 页码：<<<PAGE 69>>>
- 摘录："Each node has at least one transmit, and one receive secure channel, Each associated with a Secure Channel Identifier (SCI)... Within each secure channel, secure associations (SA) are defined. The SAs hold the encryption keys (SAK – Secure Association Key) identified by their association number (AN), along with a packet number (PN)"
- 内容：发收各一条安全通道（SCI 标识），通道内 SA 持有 SAK；对端 rx-SCI 必须匹配本端 tx-SCI（key-chain 交叉配置）。
### P-09 MKA 动态密钥协商原理（CAK+SAK）
- 页码：<<<PAGE 76>>>、<<<PAGE 79>>>
- 摘录："Secure-Channel (SCI-TX/SCI-RX) and Secure-Association-Key (SAK) are exchanged... dynamically using MKA (MACsec Key Agreement Protocol)... The MKA protocol selects one of the nodes as the key server, which creates a dynamic SAK"；两把密钥 "A connectivity association key (CAK) that secures control plane traffic / A randomly-generated secure association key (SAK) that secures data plane traffic"（p76）；EAP 模式 "The CAK is delivered in the RADIUS vendor-specific attributes (VSAs) MS-MPPE-Send-Key and MS-MPPE-Recv-Key"（p79）
- 内容：PSK 派生 CAK→key server 生成 SAK；EAP 模式由 802.1X/RADIUS 下发密钥材料。
### P-10 MACsec 平台支持差异与 128/256 位边界
- 页码：<<<PAGE 71>>>-<<<PAGE 72>>>
- 摘录："Dynamic (128/256-bit) MACsec is supported on the OS6570M, OS6870, and OS99-CMM2. All other switches support 128-bit"；"MACsec not supported on OS6870-24 VFL stacking port 25/26"（p72）；"128-bit platforms (e.g. 6465 or 6860E) in the access-layer can work with the 6900-X48E supporting both 128 and 256-bit in the distribution/core"
- 内容：不同型号/板卡支持 Static/Dynamic/密钥长度不同，VFL 堆叠口不支持。
### P-11 MACsec 需免费 site license + Security Admin 权限域
- 页码：<<<PAGE 73>>>、<<<PAGE 82>>>
- 摘录："MACsec feature requires a site license, this license can be generated free of cost. There is no reboot required after applying the license"（p73）；"MACsec feature is now part of the security domain... user securityadmin password Switch@123 read-write MACsec OR ... domain-security"（p82）
- 内容：许可免费用、应用后免重启；命令权限纳入 security 域。
## Private VLAN
### P-12 Private VLAN 域模型（Primary/Isolated/Community）
- 页码：<<<PAGE 98>>>、<<<PAGE 99>>>、<<<PAGE 109>>>
- 摘录："Partitions single broadcast domain into several broadcast sub-domains... Provides network-wide isolation per primary VLAN"（p98）；"Isolated Vlan: Cannot communicate with each other at L2 / Community Vlan: Can communicate each other at L2 but not with other communities"（p99）；"There can be only one Isolated VLAN within one Primary VLAN... There can be multiple distinct Community VLANs"（p109）
- 内容：一个 Primary VLAN 携带一个 Isolated + 多个 Community 二级 VLAN。
### P-13 PVLAN 四类端口角色
- 页码：<<<PAGE 100>>>
- 摘录："Promiscuous ports: Part of the primary VLAN, Can communicate to all ports in all Vlans / Isolated ports: Can only communicate to promiscuous ports / Community ports: Can communicate to ports in the same community or promiscuous ports / PVLAN ISL Ports: Extend a PVLAN domain across different switches. Carries both primary and secondary traffic"
- 内容：混杂口全通、隔离口仅到混杂口、社区口限本社区、ISL 口跨交换机延伸。
### P-14 PVLAN 二层流量透传规则（主 VLAN 转发、副 VLAN 限制）
- 页码：<<<PAGE 104>>>
- 摘录："Community Vlan 101 / Isolated Vlan 103 → Primary Vlan ... Traffic not authorized / Traffic authorized"
- 内容：出方向流量经 Primary VLAN 转发；未授权的二级 VLAN 间流量被丢弃。
### P-15 UNP 端口的 PVLAN 运行时角色判定
- 页码：<<<PAGE 106>>>
- 摘录："The UNP ports are designated as isolated or community ports during runtime based on the first MAC address learned on the port... If the first MAC address learned on the a UNP port is classified into any standard VLAN (non-PVLAN), then the UNP port cannot be designated as an isolated or community port"
- 内容：UNP 口按首个学到的 MAC 的 VLAN 分类决定 isolated/community 角色。
## MSTP
### P-16 MSTP Region 判定三要素与域间表现
- 页码：<<<PAGE 117>>>、<<<PAGE 123>>>
- 摘录："A MSTP region is A collection of switches Sharing the same view of physical topology... MSTP Region seen as one switch for the rest of the world"（p117）；"To belong to the same region, switches must have the same: Region name / Revision level / VLAN to MSTI mapping"（p123）
- 内容：name+revision+VLAN 映射一致才同域；对外呈现为单台虚拟交换机（CST 交互）。
### P-17 MSTP 实例与 CIST/IST 关系
- 页码：<<<PAGE 116>>>、<<<PAGE 118>>>、<<<PAGE 119>>>
- 摘录："If a VLAN is not mapped to any MSTI, it is associated to the MSTI 0 (aka IST)"（p116）；"BPDUs are carried through the network via the MSTI 0 (aka IST)... One BPDU is exchanged for all instances over default VLAN... The maximum hop count supported is 40, default is 20"（p118）；"Up to 16 other instances are supported by Alcatel-Lucent AOS"（p119）
- 内容：MSTI0=CIST 承载 BPDU；单 BPDU 携带全部实例；最多 16 个附加实例。
### P-18 MSTP 32 位路径开销与优先级语义
- 页码：<<<PAGE 142>>>、<<<PAGE 148>>>
- 摘录："Multiple STP uses a 32-bit Path Cost value vs the 16-bit path cost value that 802.1d/802.1w use by default"（p142 Tips）；"in Multiple Spanning Tree the bridge priority is the assigned Bridge Priority value PLUS the MSTI instance value"（p148 Tips）
- 内容：MST 开销 32 位（lab 中显示 20000/18000/36000）；bridge ID = 配置优先级 + MSTI 号（如 32768+1=32769）。
### P-19 MSTP 负载分担设计（按实例差异化根桥优先级）
- 页码：<<<PAGE 126>>>、<<<PAGE 130>>>
- 摘录："Tips: Manage switches priority values to have a different switch assumes the Root spantree role for each MSTI"（p126）；Example 2 "Traffic Load Sharing"：CIST A=4096、MSTI1 B=4096、MSTI2 C=4096（p130）
- 内容：不同实例选不同根桥，实现 VLAN 组流量分流；优先级须为 4096 的倍数（p146 Notes）。
## MVRP
### P-20 MVRP 协议原理与报文模型
- 页码：<<<PAGE 152>>>、<<<PAGE 153>>>
- 摘录："IEEE 802.1ak / Implements the MRP Protocol / Controls and signals dynamic VLAN registration entries across the bridged network. Close to the GVRP protocol... Re-declaration during topology change (only for affected VLANs)"（p152）；"MVRP sends one PDU that includes the state of all 4094 VLANs on a port... MVRP also includes the transmission of a TCN for individual VLANs"（p153）
- 内容：基于 STP 拓扑传播动态 VLAN 注册，一个 PDU 携带端口全部 4094 VLAN 状态。
### P-21 MVRP 注册模式与申请者模式
- 页码：<<<PAGE 154>>>、<<<PAGE 155>>>
- 摘录："mvrp {port ... | linkagg ...} registration {normal | fixed | forbidden}"；"The applicant mode determines whether MVRP PDU exchanges are allowed on a port depending on the Spanning Tree state of the port — participant | non-participant | active"（p155）
- 内容：三种 registrar 模式控制本端口 VLAN 注册行为；applicant 模式控制是否主动声明。
### P-22 MVRP 动态 VLAN 生成与删除生命周期
- 页码：<<<PAGE 161>>>-<<<PAGE 163>>>
- 摘录："By default, the maximum number of dynamic VLANs that can be created using MVRP is 256"（p161）；"ERROR: Dynamic vlan 40 cannot be deleted... The mvrp status is equal to the dyn. That means the VLAN 40 has been automatically re-created"（p163 Tips）；"there's no ip interface creation nor association with MSTI"（p163 Notes）
- 内容：MVRP 自动建 VLAN（type=dyn）并动态打 tagged 端口；MVRP 禁用后动态 VLAN 消失；动态 VLAN 不建 IP 接口也不映射 MSTI。
### P-23 MVRP 四定时器
- 页码：<<<PAGE 156>>>、<<<PAGE 162>>>
- 摘录："mvrp timer join ... 250 ms to 1073741773 ms / leave ... 750 ms... / leaveall ... / periodic-timer 1 to 2147483647 ms"；实测默认 "Join Timer 600, Leave Timer 1800, LeaveAll Timer 30000, Periodic 1"（p162）
- 内容：join/leave/leaveall/periodic 四个定时器的取值范围与默认值。
## 网络安全
### P-24 DoS 过滤检测能力清单
- 页码：<<<PAGE 168>>>
- 摘录："filter the following DoS attacks — Ping of Death, SYN attack, Land attack, Teardrop, Bonk, Boink, Pepsi / Detect ARP flooding: QoS rate-limits ARP packets to the CPU / Detect any packet with invalid source or destination IP address / Detect Multicast IP and MAC address mismatch / Detect Ping overload: rate of ICMP requests... over a period of 5 seconds... exceeds 100 pkts/sec"
- 内容：交换机内置的 DoS 攻击指纹与速率检测机制（ICMP>100pps 判攻击）。
### P-25 ARP 防御（未解析下一跳丢弃机制）
- 页码：<<<PAGE 175>>>
- 摘录："Creates a drop-entry as soon as it attempts to resolve an ARP... The entry is removed either when the ARP is resolved, or after 12 attempts have been made, once every 5 secs. (~1 minute)... Duplicate request received during the time... is dropped. Avoids CPU utilization climb"
- 内容：解析期间去重丢弃，12×5s 后超时，保护 CPU。
### P-26 ARP 欺骗检测原理
- 页码：<<<PAGE 176>>>、<<<PAGE 177>>>
- 摘录："Identifies unsolicited ARP Replies from an attacker, false ARP requests and unsolicited ARP replies / Sends out ARP Requests for certain configurable restricted addresses and its own interface addresses / ARP Reply will be accepted only if the Switch had originated a corresponding ARP Request"；restricted-address "Maximum of two IP addresses per IP interface"（p177）
- 内容：只认可自己发起请求的应答；对受限地址主动探测；每接口最多配 2 个受限地址；`ip dos arp-poison restricted-address`。
### P-27 本地代理 ARP（Local Proxy ARP）与 ARP 过滤
- 页码：<<<PAGE 179>>>、<<<PAGE 180>>>
- 摘录："All ARP requests received on VLAN member ports are answered with the MAC address of the VLAN's virtual IP router port"（p179）；"Blocks the switch from providing ARP replies for the specified IP address(es). It is generally used in conjunction with the Local proxy ARP application"（p180）
- 内容：per-VLAN 代理应答 + `arp filter` sender/target 维度 allow/block 精细化控制。
### P-28 ARP 表项属性（动态老化/静态/alias）
- 页码：<<<PAGE 178>>>
- 摘录："Dynamic addresses remain in the table until they time out (Default 300 sec.) / Static entries are permanent... Use the alias keyword to specify that the switch will act as an alias (proxy) for this IP address"
- 内容：`arp <ip> <mac> [alias]` 静态映射与代理。
### P-29 Port Mapping 双向/单向语义
- 页码：<<<PAGE 182>>>、<<<PAGE 199>>>
- 摘录："User-port: no direct user-to-user traffic, only user-to-network"；双向模式 Network-port "no direct network-to-network traffic, only network-to-user"（p182）；"Network ports of a unidirectional port mapping session can be shared with other unidirectional sessions but cannot be shared with any sessions configured in the bidirectional mode"（p199）
- 内容：会话内 user 口彼此隔离；方向模式决定 network 口间能否互通，最多 8 会话。
### P-30 MAC Forced Forwarding（MFF，RFC 4562）
- 页码：<<<PAGE 185>>>、<<<PAGE 186>>>
- 摘录："Described in RFC 4562 / Control unwanted broadcast traffic and host-to-host communication... Prohibits MAC address resolution between hosts located within the same subnet... Dynamic Proxy ARP uses: Port Mapping / DHCP snooping / Local proxy ARP"；"Once a DHCP lease is offered to a L2 client, stores the router IP advertised in the DHCP ACK. An ARP reply with the access router @MAC is sent for all subsequent ARP requests"
- 内容：借 DHCP ACK option 3 网关 IP，把同子网主机 ARP 一律应答为网关 MAC，强制上行。
### P-31 Storm Control 限速与动作
- 页码：<<<PAGE 188>>>、<<<PAGE 397>>>
- 摘录："flood-limit {bcast | mcast | uucast | all} rate {pps pps_num| mbps mbps_num | cap% cap_num...} [low-threshold] ... action {shutdown | trap | default}"；阈值三种单位 "rate % num: rate in % of the port speed / mbps / pps"（p397）
- 内容：按广播/组播/未知单播分类限速，违例可 shutdown 或 trap。
### P-32 Learned Port Security 学习控制与违例
- 页码：<<<PAGE 190>>>、<<<PAGE 191>>>、<<<PAGE 207>>>
- 摘录："Limit the max number of L2 addresses that can be learned on a port... Not supported on Link Aggregate ports"（p190）；"Shutdown. Stops all traffic on a port after violation / Filtering. Only stops traffic from violating device"（p191）；"you can specify up to 100 mac addresses to be learned per port by LPS"（p207）
- 内容：MAC 数量/时间窗/静态化三重控制；违例 restrict 或 shutdown；不支持聚合口。
### P-33 LPS 违例自动恢复与报文中继（pkt-relay）
- 页码：<<<PAGE 196>>>、<<<PAGE 209>>>
- 摘录："by default all the packets trapped on LPS port will be reinjected back to the switch once the MAC is successfully learned"（p196）；"By default, there's a timer of 300 seconds to clear automatically the violation... Global Recovery Maximum: 10"（p209）
- 内容：学习期丢包通过 pkt-relay 重注入；违例默认 300s 自动恢复、最多自动恢复 10 次。
### P-34 DoS 防御下的 SNMP 认证 Trap 三模式
- 页码：<<<PAGE 173>>>
- 摘录："If mode is set to standard (default): only the standard authenticationFailure... private: only alaAuthenticationFailure... both... The alaAuthenticationFailure includes the IP address of the client causing the authentication failure"
- 内容：`snmp authentication-trap mode {standard|private|both}`，私有 trap 带客户端 IP。
## IP 路由基础
### P-35 IP 接口与 Loopback0 原理
- 页码：<<<PAGE 214>>>、<<<PAGE 216>>>
- 摘录："IP forwarding is enabled when at least one IP interface is configured on a VLAN / The first interface bound to a VLAN becomes the primary interface"（p214）；"Loopback0: Identify a consistent address for network management purposes / Not bound to any VLAN / Always remain operationally active... Automatically advertised by RIP and OSPF protocols when the interface is created (not by BGP)"（p216）
- 内容：Loopback0 用途清单（PIM RP、sFlow、RADIUS 源、router-id、BGP peering 等）。
### P-36 递归静态路由（follows）
- 页码：<<<PAGE 224>>>、<<<PAGE 225>>>
- 摘录："Nexthop (or gateway) address no longer must be tied to a particular INTERFACE / Capability to tie the destination route to the best route used to reach a particular host... May be an INTERFACE or a dynamically learned route"；"ip static-route 172.30.0.0/16 follows 2.2.2.2 metric 1"（p225）
- 内容：下一跳随目标主机路由动态变化的静态路由。
### P-37 RIP 协议规格与四定时器
- 页码：<<<PAGE 227>>>、<<<PAGE 231>>>、<<<PAGE 232>>>
- 摘录："Distance Vector Protocol (uses hop count)... Hop count limit of 16 is considered unreachable... Maximum network diameter = 15 / Generates updates every 30 seconds / Routes timeout after 180 seconds / Uses UDP port 512 [520]";Timer：Update 默认 30（1..120）、Invalid 180（3..360）、Garbage 120（0..180）、Hold-down 0（0..120）；约束 "update cannot exceed 1/3 of invalid... invalid cannot be less than 3x of update"（p231）
- 内容：RIP 度量、更新、失效与垃圾回收机制及定时器联动约束。
### P-38 AOS 路由协议优先级（route-pref）
- 页码：<<<PAGE 299>>>、<<<PAGE 503>>>
- 摘录："Local 1 / Static 2 / OSPF 110 / ISISL1 115 / ISISL2 118 / RIP 120 / EBGP 190 / IBGP 200 / Import 210"（p299）；可改 "ip route-pref BGP 8"（p503）
- 内容：RIB 选路次序，可手工调整。
## OSPF
### P-39 OSPF 邻接状态机（Down→Full 七态）
- 页码：<<<PAGE 241>>>、<<<PAGE 244>>>-<<<PAGE 247>>>
- 摘录："Down / Init / 2-Way / Exstart / Exchange / Loading / Full"；"Hello interval: 10 seconds (keep-alive function) / Dead interval: 40 seconds"（p241）；DBD→LSR→LSU→LSAck 交换过程（p245-246）
- 内容：Hello 保活、DBD 摘要比对、LSR/LSU 精确同步的完整状态机。
### P-40 DR/BDR 选举规则与组播地址
- 页码：<<<PAGE 242>>>、<<<PAGE 243>>>、<<<PAGE 247>>>
- 摘录："The DR & BDR are elected according to: IP interface priority (highest priority) / Router ID (highest value)"（p243）；"R4 sends a multicast to the DR and the BDR (destination @: 224.0.0.6) / The DR informs the other routers... (destination @: 224.0.0.5 = all OSPF routers)"（p247）
- 内容：优先级+RouterID 选举；AllSPFRouters 224.0.0.5 / AllDRouters 224.0.0.6。
### P-41 OSPF LSA 类型职责
- 页码：<<<PAGE 260>>>-<<<PAGE 265>>>
- 摘录："Type 1 Router LSA: Each router within the area floods router LSA... always stays within the area"；"Type 2 Network LSA: Only generated by DR (multi-access network)"；"Type 3 Summary LSA: Generated by the ABR... inform other areas about networks from an area"（p262）；"Type 5 External LSA: Generated by the ASBR"（p263）；"Type 4 Summary ASBR LSA: Generated by the ABR... inform other routers where to find the ASBR"（p264）；"Type 7 NSSA LSA... LSA – Type 7 carries exact same information as LSA – Type 5 but is not blocked in NSSA areas... The ABR (1) convert the LSA – Type 7 to LSA – Type 5"（p265）
- 内容：1/2/3/4/5/7 类 LSA 的生成者、传播范围与转换关系。
### P-42 四类 OSPF 区域的 LSA 差异
- 页码：<<<PAGE 267>>>-<<<PAGE 270>>>
- 摘录：Standard "Type 3 & 5 are flooded throughout the backbone and all standard areas"（p267）；Stub "Type 5 LSAs are not propagated... Instead, R2 (ABR) injects a Type 3 LSA containing a default route"（p268）；Totally Stubby "External routes + Type 3 LSAs are not forwarded... All routing out of the area relies on a single default route"（p269）；NSSA "Type 7 LSAs = Type 5 LSAs in disguise. This allows an ASBR to advertise external links to an ABR"（p270）
- 内容：四种区域允许进入的 LSA 集合与默认路由注入行为。
### P-43 OSPF Router 四类型（BB/IR/ABR/ASBR）
- 页码：<<<PAGE 256>>>-<<<PAGE 258>>>
- 摘录："Routers that are entirely within the backbone area are called Backbone Router (BB)... wholly within an area are called Internal Routers (IR)"（p256）；ABR "Condense the topological information of their attached areas for distribution to the backbone... Summarize sub networks"（p257）；ASBR "Router that is running multiple routing protocols... Able to import and translate different protocols into OSPF (redistribution)"（p258）
- 内容：按接口所属区域/是否重分发划分四种路由器角色。
### P-44 ECMP 与负载分担
- 页码：<<<PAGE 285>>>
- 摘录："Next-hop packet forwarding to a single destination can occur over multiple 'best paths'... Same destination / Same metric / Different next-hops / ECMP Per-Flow Load Balancing... Up to 4 ECMP routes supported. *Per packet Load Balancing is not supported"
- 内容：等价多径按流分担，最多 4 条，不支持逐包。
### P-45 汇总（Summarization）与聚合（Aggregation）分工
- 页码：<<<PAGE 286>>>、<<<PAGE 287>>>
- 摘录："Summary routes are carried by LSA – Type 3 (Summary LSA). Internal routes summarization done on the ABR"（p286）；"Internal routes: Summarization > External routes: Aggregation... Aggregated routes are carried by LSA – Type 5 (External ASBR LSA). External routes aggregation done on the ASBR"（p287）
- 内容：域内路由在 ABR 汇总（Type3），外部路由在 ASBR 聚合（Type5）。
### P-46 OSPF 接口认证与 Virtual Link
- 页码：<<<PAGE 288>>>、<<<PAGE 289>>>
- 摘录："neighbours can communicate only if: They use the same type of authentication / They have a matching password or key. 2 types: Simple (clear-text) / MD5 (Encrypted...)"（p288）；"all areas must be connected to the backbone area (Area 0). Not possible? Solution: Virtual Link... The crossed area is called Transit Area"（p289）
- 内容：认证两端必须匹配；虚链路经 transit area 延伸 Area 0。
### P-47 Graceful Restart 原理（Grace LSA + helper）
- 页码：<<<PAGE 359>>>-<<<PAGE 362>>>
- 摘录："Router remains on forwarding path when restarting / Neighbors must participate... Grace LSAs are sent to neighbors either before (planned) or after (unplanned) restart. Contain a 'grace period'... Are 'link-local'"（p361）；"It does not send any LSA/LSP because it still has incomplete routing information"（p362）；"Graceful restart is disabled for OSPF and ISIS and enabled for BGP by default"（p363）
- 内容：重启期间邻居保持邻接、重启方静默同步 LSDB 后再刷新 Grace LSA。
### P-48 Route Map 顺序匹配与 deny 语义
- 页码：<<<PAGE 304>>>、<<<PAGE 305>>>
- 摘录："Route 10.10.0.0/16 will match sequence-number 1. Since one of the actions is deny, switch stops processing and does not redistribute the route / Route 11.11.0.0/16 will not match sequence-number 1. Therefore, the processing goes to sequence-number 2..."（p304）；"ip route-map routemap1 match ip-address 10.0.0.0/8 + match tag 4 + match tag 5 = match the subnet 10.0.0.0/8 and [tag 4 or tag 5]"（p305）
- 内容：序列号自上而下、命中即停；同序列多 match 为 AND、同 match 多值为 OR。
## 组播
### P-49 组播地址与 MAC 映射
- 页码：<<<PAGE 375>>>
- 摘录："Based on Class 'D' IP address values From 224.0.0.0 to 239.255.255.255... Least Significant 23 bits of IP address mapped onto MAC address. IP MultiCast address 224.1.2.3 = 01:00:5E:01:02:03"；保留段 224.0.0.x / 224.0.1.x / 232/8 SSM / 239/8 管理域
- 内容：Class D 范围、知名组地址（224.0.0.5 OSPF、224.0.0.6 DR、224.0.0.13 PIM、224.0.0.18 VRRP 等）与 23 位映射。
### P-50 IGMP 版本能力演进
- 页码：<<<PAGE 381>>>、<<<PAGE 382>>>
- 摘录："IGMP v1: Membership Query / Membership Report / IGMP v2: ... Group-Specific Query, V2 Membership report (Fast Leave), Leave group / IGMP v3: ... V3 Membership report (Explicit Host Tracking)"（p381）；"IGMP is a protocol confined to the local segment... always has a Time-To-Live (TTL) of 1. Host Membership Queries are sent to 224.0.0.1. 'Leave Group'... to 224.0.0.2"（p382）
- 内容：v2 引入 Leave/特定组查询，v3 引入源过滤；本地段协议、TTL=1。
### P-51 IPMS 与组播路由的分工
- 页码：<<<PAGE 377>>>、<<<PAGE 385>>>、<<<PAGE 386>>>
- 摘录："Only the client which join a multicast group received the multicast packet, and the multicast packet stream will not flood to other ports"（p377）；"IPMS: Intercepts IGMP packets to track membership by port rather than by network... Performance is significantly improved because forwarding decisions are made by hardware"（p385）；"Based on the IGMP query and report messages that are snooped, the switch forwards multicast traffic only to the ports that requested it"（p386）
- 内容：IPMS=硬件 IGMP 侦听按端口转发；跨 VLAN 才需 DVMRP/PIM 路由。
### P-52 IGMP Throttling（max-group 三级限制）
- 页码：<<<PAGE 396>>>
- 摘录："Configures the maximum group limit learned per VLAN, per port or globally... Per port limit overrides VLAN and global configuration / Actions: None / Drop. Drops the incoming membership request / Replace. Replaces an existing membership"
- 内容：port > VLAN > global 的限组优先级和三种动作。
### P-53 DVMRP 逆向路径组播与 Flood-Prune-Graft
- 页码：<<<PAGE 413>>>、<<<PAGE 416>>>、<<<PAGE 417>>>
- 摘录："If a packet arrived on an upstream interface that would be used to transmit packets back to the source, it is forwarded... Otherwise... discarded"（p413）；"Multicast traffic is flooded to all downstream routers... will send a DVMRP prune message"（p416）；"Graft is only used after a prune. Waits for 'graft ack'... When prune times out, upstream router starts flooding traffic again (7200 sec.)"（p417）
- 内容：RPF 校验 + 泛洪/剪枝/嫁接机制，prune 超时 7200s。
### P-54 PIM-SM 共享树（RPT）与最短路径树（SPT）切换
- 页码：<<<PAGE 426>>>、<<<PAGE 428>>>-<<<PAGE 430>>>
- 摘录："PIM-SM is not a flood and prune mechanism. It requires explicit joins... uses a Rendezvous Point (RP) as a shared tree... Each source sends multicast data packets encapsulated in unicast packets to RP (Register message)"（p426/428）；"Once the last-hop router receives traffic form the RP along the RPT, it sends a PIM join message towards the source... forms the shortest path tree (SPT)... The switchover is initiated automatically by the last DR. SPT status is enabled by default"（p429-430）
- 内容：RPF 原则、Register 封装、DR 发起 SPT 切换并 Prune RPT。
### P-55 BSR 与 C-RP 选举算法
- 页码：<<<PAGE 431>>>、<<<PAGE 432>>>
- 摘录："C-RP periodically sends out C-RP advertisements... BSR then periodically sends its RP set... in the form of a Bootstrap message"；RP 选择 "All devices with the best priority (lowest value) / Highest Hash value using the group address, the RP address... / RP with the highest IP address"（p432）
- 内容：C-BSR 优先级+IP 选 BSR，BSR 汇聚 RP-Set，按优先级→hash→IP 逐级选 RP。
### P-56 PIM-DM 特性与区别
- 页码：<<<PAGE 434>>>、<<<PAGE 435>>>
- 摘录："Designed for networks with many receivers / Flood and Prune operation similar to DVMRP... No periodic joins transmitted, only explicitly triggered prunes and grafts / No Rendezvous Point (RP)"；"Prunes timeout in 3 minutes. Flood & Prune process repeats every 3 minutes"（p435）
- 内容：密集模式的 3 分钟泛洪-剪枝循环，无 RP。
### P-57 Anycast RP 原理（RFC 4610）
- 页码：<<<PAGE 643>>>、<<<PAGE 644>>>、<<<PAGE 645>>>
- 摘录："Provide fast convergence when a PIM rendezvous point (RP) router fails and RP load-sharing... Uses a single statically defined RP address (set on a Loopback interface)... Senders and Receivers exchange messages with the nearest RP. Determined by the Unicast routing table (IGP). In case of a failure, the convergence is the same as the IGP"（p644）；"only be supported with PIM-SM... Maximum of 8 Anycast RP routers... SPT must be enabled"（p645）
- 内容：多 RP 共享一个 Loopback 任播地址，IGP 收敛即 RP 切换。
## VRF/BGP/SPB
### P-58 VRF 实例隔离与 VLAN 绑定规则
- 页码：<<<PAGE 453>>>、<<<PAGE 460>>>
- 摘录："Multiple routing instances within the same physical switch... Ability to use duplicate IP addresses across VRF instances"（p453）；"A single IP interface, as well as the VLAN associated with the interface, can only belong to one VRF instance at a time... A VRF instance can have multiple VLAN associations"（p460）
- 内容：VLAN↔VRF 多对一单向归属，VRF 间地址可复用。
### P-59 BGP 路径向量与选路次序
- 页码：<<<PAGE 480>>>、<<<PAGE 497>>>
- 摘录："Path Vector Protocol. BGP advertisement is made of: Prefix / Attribute"（p480）；"Route selection process: Highest Local preference / Shortest AS-Path / lowest origin (IGP>EGP>Incomplete) / Lowest MED / Closer Next-Hop / EBGP > IBGP > IGP / Lowest RID"（p497）
- 内容：BGP 最优路径判定顺序，可作排障对照表。
### P-60 BGP 属性分类与关键属性语义
- 页码：<<<PAGE 482>>>-<<<PAGE 494>>>
- 摘录："Can be: Well-known mandatory / Well-known discretionary / Optional transitive / Optional nontransitive"（p482）；AS-PATH "List of traversed ASes"（p484）；Local Pref "Specify a most preferred path to exit an AS"（p488）；MED "Lower MED value is preferred. Default = 0... Only shared between two autonomous systems"（p492）；Community "NO-EXPORT / NO-ADVERTISE / <AS:Community#>"（p496）
- 内容：四大属性类别及 LP/AS-Path/Origin/MED/Community 的作用域。
### P-61 IBGP 水平分割与同步
- 页码：<<<PAGE 501>>>、<<<PAGE 502>>>
- 摘录："Routes learned via IBGP should never be Propagated to other IBGP peers"（p501）；"A BGP router should not advertise, a route learned by IBGP, to an EBGP peer unless the route is local or is learned from an IGP"（p502）
- 内容：IBGP 全互联需求的根因；`ip bgp synchronization`。
### P-62 SPB 控制平面（IS-IS + ECT）与数据平面（MAC-in-MAC）
- 页码：<<<PAGE 525>>>、<<<PAGE 567>>>、<<<PAGE 569>>>、<<<PAGE 570>>>
- 摘录："Control Plane IEEE 802.1aq ISIS–L1... No learning of Access LAN @MAC and paths accross core SPB-M switches"（p525）；PBB 头字段 "B-VID... ISID: Service Instance Identifier. The ISID is a 24-bit number... B-SA and B-DA... traffic is forwarded based on the destination BMAC (B-DA). Inner customer MACs are not learnt"（p567）；"every node builds a topology tree rooted on itself"（p569）；"An SPB network supports up to 16 BVLANs and each node builds a SPF tree for each BVLAN... network paths are deterministic and frames are delivered in the order they were sent"（p569-570）
- 内容：IS-IS 预填充 FDB、每节点每 BVLAN 一棵 SPF 树、路径对称/帧有序。
### P-63 SPB BUM 三种复制模式对比
- 页码：<<<PAGE 539>>>、<<<PAGE 573>>>、<<<PAGE 574>>>
- 摘录："Head-End (default mode): Customer BUM traffic is encapsulated... and send to ALL destinations / Tandem: ... a special B-MAC Destination Address"（p539）；对比表 "Head-end: Bandwidth efficiency Low / Resource High / Congruency Yes；Tandem (S,G): Bandwidth High / Resource Low / Congruency Yes；Tandem (*,G): Congruency No"（p574 Table 1）
- 内容：按带宽/资源/同径性选择复制模式；head-end 与 tandem 按 per-service 选，(S,G)/(*,G) 按 per-BVLAN 选（p577）。
### P-64 SPB L3 服务两种变体（VPN Lite vs L3 VPN）
- 页码：<<<PAGE 534>>>-<<<PAGE 537>>>、<<<PAGE 592>>>
- 摘录："VPN-Lite: 'Default Gateway' Point To Point routing... Run routing protocols on L3 VPN IP interfaces"（p535）；"L3/IP-VPN: VRF L3 routes exchanged via dedicated ISIS/SPB TLV... No need to run routing protocols on L3 VPN IP interfaces"（p536-537）；选型 "L3 VPN is recommended within the SPB domain and VPN Lite is needed only on border nodes connecting to the outside world"（p592）
- 内容：域内用 L3 VPN（IS-IS TLV 携带 VRF 路由），边界用 VPN Lite 对接外部路由协议。
### P-65 动态服务 ISID/BVLAN 计算公式
- 页码：<<<PAGE 600>>>、<<<PAGE 601>>>
- 摘录："ISID Number = Base Service Number + Domain ID + (VLAN Number % Service Modulo) / BVLAN Index = ISID Number % (Total number of BVLANs)... Default: Base Service Number = 10,000,000 / Domain ID = 0 / Service Modulo = 512"；"using the default Service Modulo of 512 can result in up to 8 different VLAN tags being mapped to the same service... change the Service Modulo to 4096"（p601）
- 内容：iFab 动态服务编号推导规则与 512 取模的隔离隐患。
### P-66 IS-IS NSAP 寻址与 DIS 选举
- 页码：<<<PAGE 686>>>、<<<PAGE 689>>>、<<<PAGE 690>>>、<<<PAGE 694>>>
- 摘录："IS-IS uses unique addressing (OSI NSAP addresses)... Level 1 routing uses the system ID. Level 2 routing uses the area address... The AFI should be set to 49 for locally administered IS-IS configurations"（p686）；"DIS: The IS in a LAN that is designated... treats the LAN as a pseudo node"（p689）；Hello "every 9 seconds from L1 and L2 routers, if they are not the DIS... every 3 seconds from the DIS"（p690）；"Highest interface priority / Highest interface MAC address"（p694）
- 内容：NSAP 结构（Area-ID/System-ID/NSEL）、DIS 类似 DR 但可抢占。
### P-67 SLB VIP 与 Proxy ARP 机制
- 页码：<<<PAGE 653>>>、<<<PAGE 654>>>、<<<PAGE 662>>>
- 摘录："Cluster is identified and accessed at layer 3 by using a Virtual IP (VIP) address"；"SLB cluster automatically creates a proxy ARP for the VIP with the switch's MAC address"（p654）；"Proxy ARP to 10.0.0.250 is used in a bridged network and will force the bridged packet to be routed"（p662）
- 内容：VIP 必须与服务器同网段；桥接网络靠代理 ARP 截获流量强制路由。

## glossary

| 术语 | 解释 | 页码 |
|---|---|---|
| ERP (Ethernet Ring Protection) | 以太网环网保护协议，环内防环并实现约 50ms 快速故障恢复 | <<<PAGE 37>>> |
| RPL (Ring Protection Link) | 环保护链路，环内正常状态下被阻塞以防环路的那条链路 | <<<PAGE 38>>> |
| RPL Owner | 持有 RPL 端口的交换机，负责稳态阻塞/故障时解阻塞 RPL 口 | <<<PAGE 38>>> |
| R-APS message | 环自动保护倒换消息，在 Service VLAN 内传递 | <<<PAGE 38>>> |
| SF (Signal Fail) | R-APS 消息类型，检测到链路/节点故障时宣告 | <<<PAGE 38>>> |
| NR / RB (No Request / RPL Blocked) | 无请求消息及 RPL 已阻塞标记，恢复完成时由 RPL Owner 发出 | <<<PAGE 40>>> |
| WTR (Wait To Restore) timer | 等待恢复定时器，默认 5 分钟，防链路抖动引发反复倒换 | <<<PAGE 42>>> |
| Guard Timer | 守护定时器（默认 50 厘秒），丢弃过期 R-APS 防误倒换 | <<<PAGE 56>>> |
| Service VLAN | 环级 VLAN，承载 R-APS 消息和 ETH CCM | <<<PAGE 38>>> |
| Protected VLAN | 加入 ERP 环、转发状态由 ERP 决定的业务 VLAN | <<<PAGE 38>>> |
| MEG Level | ERP 管理实体组级别 0-7，环内所有交换机必须一致 | <<<PAGE 47>>> |
| Laddered / Subtending Ring | 主环+子环的梯形结构，子环借主环虚通道闭合 | <<<PAGE 43>>> |
| MACsec (IEEE 802.1AE) | 二层链路加密与认证标准，点到点保护直连节点间流量 | <<<PAGE 67>>> |
| SecTag | MACsec 报文头（8/16 字节），含密钥信息、包号与安全通道标识（EtherType 0x88E5） | <<<PAGE 68>>> |
| ICV (Integrity Check Value) | GCM-AES 生成的 16 字节完整性校验值 | <<<PAGE 68>>> |
| SCI (Secure Channel Identifier) | 安全通道标识，收发通道各一，需与对端交叉匹配 | <<<PAGE 69>>> |
| SAK (Secure Association Key) | 安全关联密钥，加密数据平面流量 | <<<PAGE 69>>> |
| Static SA Mode | 手工配置最多 4 把 SA 密钥的交换机间静态模式 | <<<PAGE 75>>> |
| MKA (MACsec Key Agreement) | IEEE 802.1X-2010 密钥协商协议，动态生成 SAK | <<<PAGE 76>>> |
| CAK (Connectivity Association Key) | 连接关联密钥，保护 MKA 控制平面；EAP 模式经 RADIUS VSAs 下发 | <<<PAGE 76>>> |
| Private VLAN (PVLAN) | 在单广播域内划分子域实现二层隔离的特性 | <<<PAGE 98>>> |
| Primary / Secondary VLAN | PVLAN 主 VLAN（对外）与从 VLAN（isolated/community 两类） | <<<PAGE 99>>> |
| Isolated VLAN | 隔离型二级 VLAN，成员间二层完全不通，仅到 promiscuous 口；每 Primary 仅一个 | <<<PAGE 99>>>、<<<PAGE 109>>> |
| Community VLAN | 社区型二级 VLAN，同社区可互通、跨社区不通 | <<<PAGE 99>>> |
| Promiscuous port | 混杂端口，属 Primary VLAN，可与所有端口通信 | <<<PAGE 100>>> |
| PVLAN ISL | 跨交换机延伸 PVLAN 域的级联口，同时承载主/从 VLAN | <<<PAGE 100>>> |
| MSTP (IEEE 802.1s) | 多生成树协议，多 VLAN 映射到少量实例 | <<<PAGE 115>>> |
| MSTI (MST Instance) | 多生成树实例（最多 16 个），VLAN 按需映射 | <<<PAGE 116>>> |
| CIST / IST | 公共与内部生成树（实例 0），未映射 VLAN 默认归属，承载全部实例 BPDU | <<<PAGE 115>>>、<<<PAGE 118>>> |
| MST Region | 多生成树区域，name+revision+VLAN 映射三要素一致才同域 | <<<PAGE 117>>> |
| Flat / per-vlan (1x1) mode | 单树 flat 模式（MSTP/MVRP 前置）与每 VLAN 一树模式，二者互斥 | <<<PAGE 122>>>、<<<PAGE 143>>> |
| MVRP (IEEE 802.1ak) | 多 VLAN 注册协议，跨桥接网动态传播 VLAN 成员（近似 GVRP） | <<<PAGE 152>>> |
| Registrar / Applicant mode | MVRP 端口注册模式（normal/fixed/forbidden）与申请者模式 | <<<PAGE 154>>>、<<<PAGE 155>>> |
| Dynamic VLAN (dyn) | 由 MVRP 自动学习创建的 VLAN，不建 IP 接口、不映射 MSTI | <<<PAGE 162>>>、<<<PAGE 163>>> |
| ARP Poisoning Detection | ARP 欺骗检测，识别未请求应答/伪造请求，restricted-address 每接口最多 2 个 | <<<PAGE 176>>>、<<<PAGE 177>>> |
| Local Proxy ARP | 本地代理 ARP，per-VLAN 用路由口 MAC 应答所有请求 | <<<PAGE 179>>> |
| Port Mapping | 端口映射会话，user 口彼此隔离仅经 network 口通信，最多 8 会话 | <<<PAGE 182>>> |
| MFF (MAC Forced Forwarding, RFC 4562) | MAC 强制转发，同子网主机 ARP 一律指向网关（DHCP snooping+port mapping+动态代理 ARP） | <<<PAGE 185>>> |
| Storm Control (flood-limit) | 风暴控制，按 bcast/mcast/uucast 限速（pps/mbps/cap%），违例 shutdown/trap | <<<PAGE 188>>> |
| LPS (Learned Port Security) | 学习型端口安全：限 MAC 数量/学习窗/违例 restrict 或 shutdown；不支持聚合口 | <<<PAGE 190>>> |
| convert-to-static | 将端口已学动态 MAC 固化为静态，锁定当前设备 | <<<PAGE 193>>> |
| pkt-relay | LPS 报文中继，学习期被截获报文重注入转发路径 | <<<PAGE 196>>> |
| UDP Relay | 通用 UDP 端口中继，按服务端口转发到指定 VLAN/IP | <<<PAGE 170>>> |
| Loopback0 | 环回接口，管理/协议标识用，RIP/OSPF 自动通告（BGP 不） | <<<PAGE 216>>> |
| Recursive static route (follows) | 递归静态路由，下一跳跟随某目标主机路由动态解析 | <<<PAGE 224>>> |
| Router database / route-pref | 路由数据库与协议优先级（Local 1/Static 2/OSPF 110/RIP 120/EBGP 190…） | <<<PAGE 223>>>、<<<PAGE 299>>> |
| Router ID | OSPF 路由器标识：手工指定 > Loopback0 > 最高接口 IP | <<<PAGE 240>>> |
| DBD / LSR / LSU / LSAck | OSPF 数据库描述/请求/更新/确认包，邻接同步四件套 | <<<PAGE 245>>>、<<<PAGE 246>>> |
| LSA Type 1/2 | 路由器 LSA（每路由器域内泛洪）与网络 LSA（DR 生成） | <<<PAGE 260>>>、<<<PAGE 261>>> |
| LSA Type 3 (Summary) | 汇总 LSA，ABR 生成跨区域通告网段；也承载区域路由汇总 | <<<PAGE 262>>>、<<<PAGE 286>>> |
| LSA Type 4 (Summary ASBR) | ASBR 汇总 LSA，ABR 通告到 ASBR 的位置 | <<<PAGE 264>>> |
| LSA Type 5 (External) | 外部 LSA，ASBR 重分发的域外路由；外部聚合由 ASBR 完成 | <<<PAGE 263>>>、<<<PAGE 287>>> |
| LSA Type 7 (NSSA) | NSSA 外部 LSA，ABR 转换为 Type 5 出域 | <<<PAGE 265>>> |
| ABR / ASBR / BB / IR | 区域边界路由器（汇总）/自治系统边界路由器（重分发）/骨干/内部路由器 | <<<PAGE 256>>>-<<<PAGE 258>>> |
| Stub / Totally Stubby Area | 末梢区域（拒 Type4/5，ABR 注入 Type3 默认路由）/完全末梢（再拒 Type3） | <<<PAGE 268>>>、<<<PAGE 269>>> |
| NSSA | 非纯末梢区域，允许 ASBR 用 Type7 引入外部路由 | <<<PAGE 270>>> |
| ECMP | 等价多路径，按流负载分担，AOS 最多 4 条，不支持逐包 | <<<PAGE 285>>> |
| Virtual Link / Transit Area | 虚链路与穿越区域，跨非骨干区延伸 Area 0 | <<<PAGE 289>>> |
| Graceful Restart (Grace LSA) | 平滑重启，重启期间邻居维持邻接避免全网 SPF；OSPF/ISIS 默认关、BGP 默认开 | <<<PAGE 361>>>、<<<PAGE 363>>> |
| Route Map (action/match/set) | 路由图：动作+匹配+修改，重分发过滤核心；序列自上而下命中即停 | <<<PAGE 300>>>、<<<PAGE 304>>> |
| Class D / 01:00:5E | 组播地址 224.0.0.0-239.255.255.255，IP 低 23 位映射组播 MAC | <<<PAGE 375>>> |
| IPMS (IP Multicast Switching) | IP 组播交换，硬件 IGMP 侦听按端口转发 | <<<PAGE 377>>> |
| IGMP Querier / querier-forwarding | 查询器（每 LAN 一个）与查询器转发（组播定向到查询器交换机） | <<<PAGE 380>>>、<<<PAGE 389>>> |
| IGMP Throttling (max-group) | 每端口/VLAN/全局限制学习组数，动作 none/drop/replace | <<<PAGE 396>>> |
| RPF (Reverse Path Forwarding) | 逆向路径转发校验，只在指向源的接口收包 | <<<PAGE 413>>>、<<<PAGE 426>>> |
| PIM-SM / PIM-DM | 稀疏模式（显式加入+RP 共享树）/密集模式（泛洪-剪枝 3 分钟循环、无 RP） | <<<PAGE 426>>>、<<<PAGE 434>>> |
| RP (Rendezvous Point) | 汇聚点，共享树根，源以 Register 单播封装发往 | <<<PAGE 428>>> |
| RPT / SPT switchover | 共享树/最短路径树；末跳 DR 收到首包后自动发起 SPT 切换 | <<<PAGE 428>>>-<<<PAGE 430>>> |
| BSR / C-RP | 自举路由器/候选 RP 的动态 RP 发现机制（优先级→hash→IP 选 RP） | <<<PAGE 431>>>、<<<PAGE 432>>> |
| Anycast RP (RFC 4610) | 多 RP 共享任播 Loopback 地址实现负载分担与 IGP 级快速切换；仅 PIM-SM、最多 8 台 | <<<PAGE 643>>>-<<<PAGE 645>>> |
| VRF | 虚拟路由转发，一台物理交换机多路由实例、地址可重叠；VLAN 只能归属一个 VRF | <<<PAGE 453>>>、<<<PAGE 460>>> |
| GRT / VRF Route Leak | 全局路由表及经 route-map 的 VRF 间路由导入导出 | <<<PAGE 461>>> |
| BGP-4 (RFC 4271) | 边界网关协议，AS 间路径矢量协议，TCP 179 | <<<PAGE 476>>> |
| IBGP / EBGP | AS 内/AS 间 BGP 邻居关系；IBGP 学的路由不再传给其他 IBGP 邻居（水平分割） | <<<PAGE 478>>>、<<<PAGE 501>>> |
| AS-PATH / Next-HOP / Origin | BGP 必选属性：AS 列表/下一跳/来源（IGP>EGP>Incomplete） | <<<PAGE 484>>>-<<<PAGE 487>>> |
| Local Preference / MED | 选出口偏好（越高越优）与入流量入口建议（越低越优、仅两 AS 间传递） | <<<PAGE 488>>>、<<<PAGE 491>>> |
| Community (NO-EXPORT/NO-ADVERTISE) | 路由打标分组属性，控制通告范围 | <<<PAGE 494>>>、<<<PAGE 496>>> |
| BGP synchronization | 同步：IBGP 学的路由须 IGP 可达才通告给 EBGP | <<<PAGE 502>>> |
| SPB / SPB-M (IEEE 802.1aq) | 最短路径桥接（MAC-in-MAC 变体），IS-IS 控制平面，全链路可用 | <<<PAGE 523>>>、<<<PAGE 525>>> |
| PBB (IEEE 802.1ah) | 运营商骨干桥接，MAC-in-MAC 封装（Ethertype 0x88E7） | <<<PAGE 526>>>、<<<PAGE 567>>> |
| BEB / BCB | 骨干边缘桥（封装/解封装、终结服务）/骨干核心桥（仅按 BMAC 转发、不学客户 MAC） | <<<PAGE 527>>> |
| BVLAN (B-VID) | 骨干 VLAN，承载控制与服务流量，最多 16 个；其上无 STP | <<<PAGE 527>>>、<<<PAGE 569>>> |
| I-SID | 24 位服务实例标识，区分租户/VPN，可达 16M | <<<PAGE 527>>>、<<<PAGE 565>>> |
| ECT / ECT-ID | 等价树及编号，用于各 BVLAN 建 SPT 时的 tie-break 分流 | <<<PAGE 569>>> |
| SAP / SDP | 服务接入点（物理口+封装值绑定服务）/服务分发点（通向远端 BEB，自动创建） | <<<PAGE 527>>>、<<<PAGE 572>>> |
| Head-End / Tandem replication | SPB BUM 复制模式：头端多单播复制（默认）/串联按组播 FDB 分叉复制 | <<<PAGE 539>>>、<<<PAGE 573>>> |
| LBD (Loopback Detection) | 环回检测，发探测帧防接入层环路，检测到即关闭端口 | <<<PAGE 609>>> |
| VPN Lite / L3 VPN (SPB) | SPB 上叠跑 OSPF/BGP 的边界方案 / IS-IS TLV 携带 VRF 路由的域内方案 | <<<PAGE 534>>>、<<<PAGE 536>>>、<<<PAGE 592>>> |
| DIS / Pseudo node | IS-IS 指定中间系统/伪节点（对应 OSPF DR，可抢占；Hello 9s，DIS 3s） | <<<PAGE 689>>>、<<<PAGE 690>>> |
| NSAP (Area/System-ID/NSEL) | IS-IS 的 OSI 地址结构，本地管理 AFI=49，最小 8 字节 | <<<PAGE 686>>> |
| DHL (Dual-Home Link) | 双归链路，无 STP/LAG 的接入-核心快速倒换冗余 | <<<PAGE 318>>>、<<<PAGE 607>>> |
| Virtual Chassis (VC) / VFL | 虚拟机箱/虚拟机箱链路，多台堆叠为一逻辑设备 | <<<PAGE 134>>> |
| SLB / VIP / WRR | 服务器负载均衡：集群虚拟 IP（代理 ARP 应答）与加权轮询（权重 0 备份、总权重≤32） | <<<PAGE 653>>>-<<<PAGE 656>>> |
| write memory flash-synchro | 保存配置并同步备份 Flash 的 AOS 命令 | <<<PAGE 112>>> |
| working / certified directory | AOS 双镜像目录，reload from working/certified 支持升级回滚 | <<<PAGE 53>>>、<<<PAGE 680>>> |
