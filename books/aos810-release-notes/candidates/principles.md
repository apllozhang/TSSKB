# principles — OmniSwitch AOS 8.10R4 Release Notes（新特性机制候选）

格式：编号 P# ｜ 机制要点 ｜ 页码（fulltext.md 真实 `<<<PAGE N>>>` 标记）｜ 英文原句摘录（可选）

## 管理与安全机制

- **P1** Secure Boot 通过启动期认证校验保证只运行可信软件，需 U-Boot/ONIE/BIOS 升级 + Secure Boot 专用镜像三件配合："Secure Boot is a important security mechanism that ensures an OmniSwitch boots with only verified and trusted software." <<<PAGE 34>>>
- **P2** U-Boot 平台（6360/6465/6560/6570M）升级 8.10R4 前必须先把 U-Boot 升到 8.10.37.R04，否则装了 Secure Boot 镜像会回落 Certified 镜像启动："If a Secure Boot image is loaded on a switch that doesn't have the 8.10R4 U-boot version installed, it will reboot from the Certified image." <<<PAGE 104>>>
- **P3** 首访强制改密：8.10R4 起 admin/switch 默认口令登录必须改密且符合 password-policy，REST API/脚本必须适配："Any REST APIs or scripts must be modified to account for the required password change." <<<PAGE 27>>>
- **P4** su 账户口令只有 admin 能配、可授权其他用户、reset-to-factory 会重置、忘记口令只能恢复出厂："The super-user password cannot be recovered. In the case of a forgotten password a factory reset will need to be performed." <<<PAGE 26>>>
- **P5** ALE CA 设备证书机制：每台设备唯一密钥对 + 内部 CA 签 X.509，有效期 5 年、到期前 1 年内更新，单 PEM 文件存证书+私钥+链；已装自定义 CA 证书的升级后继续沿用不替换 <<<PAGE 27>>>
- **P6** Crypto Strong Security 开启后用户创建只允许强算法（SHA224/256/384 及 AES 变体），禁 SHA/MD5/SHADES/MD5DES/SHAAES <<<PAGE 28>>>
- **P7** ssh-rsa（SHA-1 签名）默认禁用，替代为 rsa-sha2-256/512 与 ecdsa-sha2-nistp256/384/521；可用 `ssh strong-hmacs enable` 探测服务器弱密钥 <<<PAGE 16>>>
- **P8** 8.10R4 默认 TLS 版本从 1.0 升到 1.2，并可配 TLS 1.3（RADIUS/LDAP/SYSLOG NG/SNMP 客户端与 WebView）："The default TLS version is also changed from 1.0 to 1.2." <<<PAGE 33>>>
- **P9** PKIX SSH（CAC/PIV 智能卡）：独立 PKIX SSH 服务器 + X.509v3 证书/公钥映射本地用户 + 持久信任库与 CRL 吊销检查 <<<PAGE 33>>>
- **P10** IP 分片攻击防护新增 tear-drop（重叠/畸形分片丢弃）与 icmp-frag-drop（分片 ICMP 丢弃）两类 DoS 控制 <<<PAGE 34>>>
- **P11** IPv6 DoS 检测运行于 NI、上报 CMM 生成统计/日志/SNMP trap，支持 8 种攻击类型（Ping of Death/Land/Loopback Source/无效地址/Ping Overload/NDP Flood/分片 Tear-Drop/ICMP 分片丢弃）："IPv6 DoS detection operates on the Network Interface (NI) and reports events to the Chassis Management Module (CMM)." <<<PAGE 38>>>
- **P12** MACsec 站点许可从 8.6R1 起强制（免费生成），升级后未装许可特性禁用，装许可无需重启："After upgrading, the feature will be disabled until a license is installed. There is no reboot required after applying the license." <<<PAGE 15>>>
- **P13** MKA VLAN Tag/TPID 机制：中间节点不支持 MACsec 时，MKA 控制包需打 VLAN 标签在 NNI/业务 VLAN 中隧道化，否则被中间 NNI 接口丢弃："these packets are getting dropped on the intermediate NNI interfaces." <<<PAGE 35>>>
- **P14** MACsec 平台密钥长度分层：9900-CMM2/CNI-U20、6870、6570M、6575 为 Dynamic 256-bit；6860N 仅 Dynamic 128-bit；6900-X48C4E 仅 Dynamic；6560/6465/6860(E) Static+Dynamic 128-bit（见 Appendix B 端口矩阵） <<<PAGE 62>>>/<<<PAGE 63>>>
- **P15** 802.1X max-req 从 1-3 扩到 1-50，覆盖 PC 启动/瞬时网络导致的 EAP-Response 延迟场景 <<<PAGE 33>>>

## L2/L3 与业务机制

- **P16** Router Mode（6870）：capability profile 切换扩容转发表——64K MAC/312K IPv4 路由/156K IPv6 路由/24K ARP/8K IPv6 主机 <<<PAGE 26>>>
- **P17** Edge-router Mode（6900 除 V72/C32）：比 router-mode 更大 MAC 规模，启用后必须保存配置并重启生效；V72/C32 不能与启用 edge-router 的 6900 混 VC <<<PAGE 37>>>/<<<PAGE 38>>>
- **P18** DHL Active-Standby：LACP 聚合内一条成员 Active 一条 Standby 的确定性冗余，故障即秒级接替，不依赖 STP，支持 pre-empt 与 pre-empt timer 回切 <<<PAGE 37>>>
- **P19** IPv6 BGP 路由聚合：合并多条明细属性为单条聚合路由向邻居通告（admin-state/as-set/community/local-preference/metric/summary-only） <<<PAGE 29>>>
- **P20** PIM over GRE：PIM 可在 GRE 隧道接口上建邻并转发组播，覆盖原生组播不可达的远程网络："allowing multicast routing adjacency formation and traffic forwarding between remote networks where native multicast is not supported." <<<PAGE 29>>>
- **P21** sFlow BGP Gateway：流样本携带扩展网关字段（next-hop/AS/communities/local-pref），采集器拿到的是路由归因后的流量 <<<PAGE 30>>>
- **P22** EVPN 多站点部署模型库：Clos-3/Collapsed Core/Clos-5/DCI/Multi-PoD/Multi-site，选择取决于规模、泛洪域、PoD/站点间 L2/L3 无缝切换（greenfield）与 VXLAN→VLAN L3 无缝（brownfield） <<<PAGE 30>>>
- **P23** 手工 RD/RT 配置：多站点/PoD 各自 RT 体系下选择性导入导出 EVPN 路由，配合 E-Tree 拓扑避免 PoD 内 leaf 间无谓的东西向隧道 <<<PAGE 33>>>
- **P24** PEG（PIM EVPN Gateway）：边界 leaf 桥接 EVPN 网络与外部 PIM 域，OISM 优化 fabric 内跨子网组播；DR 选举支持原生 PIM hello 与 DF 选举算法两种 <<<PAGE 31>>>
- **P25** ERP over SPB 单播客户端 MAC flush 问题：SAP 口 flush 正确但不传播到 BEB 的 SDP 口导致残留 MAC——需 `erp-ring spb-remote-flush` 让 flush 事件传播到 SDP："Stale MAC entries flush can be achieved by enabling the SPB remote flush feature for MAC flush." <<<PAGE 31>>>
- **P26** SPB 引入 6570M/6575：6570M 需 premium bundle 许可、6575 默认支持；default 与 Fabric TCAM profile 都支持，推荐 Fabric TCAM 获得更好性能与扩展性 <<<PAGE 31>>>
- **P27** Multi-Site SPB 层级（PoC）：站点内 ISIS Level-1、站点间 Site Border Node（SBN）以唯一 site-id 构建 Level-2，突破平面 SPB 500-1000 节点上限，支持 L2VPN/L3VPN/组播窥探与 ECT 负载分担："The overall limitation for number of nodes supported in a flat SPB network typically is in the range of 500 to 1000 nodes." <<<PAGE 40>>>
- **P28** SPB BVLAN 收敛原则：业务分散在 >4 条 BVLAN 时应收敛到 4 条以内，减少控制面地址更新规模、提升稳定性与收敛 <<<PAGE 65>>>
- **P29** BVLAN 判活网络级语义：`show spb isis bvlans` 的 In Use=Yes 是全网视图，远端节点挂了服务本机也显示活跃——活跃 BVLAN 即使本机无服务也不能删："Even if the service is not local to a node the node can act as a transit node for the active BVLAN. For this reason the BVLAN cannot be deleted from the network." <<<PAGE 66>>>
- **P30** LPS on VXLAN：LPS 从端口/linkagg 扩展到 EVPN VXLAN SAP，限单归属（single-homing）场景 <<<PAGE 32>>>
- **P31** Telemetry 推送管道：交换机本地 Redis 存 DPI/流数据 → IPFIX（RFC 7011）封装 → 导出 Telegraf/InfluxDB/Grafana，近实时可视与 AI/自动化供数 <<<PAGE 39>>>
- **P32** Threat-Insight 集成 AppMon：每流威胁智能三属性——DGA Score（算法生成域名）、MITM Score（TLS 中间人概率）、JA3 Fingerprint（Client Hello 指纹），v4/v6 流表实时分析 <<<PAGE 36>>>
- **P33** RoCEv2 无损以太（6900/6920）：PFC+ETS+DCBX 符合 MSFT 要求；LLDP 扩展 DCBX TLV 与 802.3 最大帧长 TLV；ECN profile + DCQCN 拥塞控制 <<<PAGE 36>>>
- **P34** 快速收敛（Improved Convergence）：SFP/SFP+/QSFP+/QSFP28 光口可更快收敛；铜口、VFL 口、splitter 口、6865-P16X/U12X 口 3/4、6570M-12/12D 口 9/10 除外 <<<PAGE 15>>>
- **P35** LACP 组数扩容：6570M 从 32 提到 96（`linkagg lacp agg size`） <<<PAGE 26>>>
- **P36** Premium（捆绑）许可：单许可文件含多个子许可（SPB/AR/25G/50G/VxLAN-EVPN），按 MAC/序列号生成；VC 内 Match=各成员子许可必须一致才生效、Local-Only=仅本机生效："Match - Sub-Licenses on all units of a VC must match for feature to operational." <<<PAGE 20>>>/<<<PAGE 32>>>
- **P37** ISSU 机理：VC 按 chassis-id 从低到高逐台从 ISSU 目录重启，Slave 全部完成后 Master 重启引发 takeover，原 Master 回来变 Slave；模块化机箱则是备 CMM 先升转主、原主再升："Each element of the VC is upgraded individually allowing hosts and switches which are dual-homed to the VC to maintain connectivity." <<<PAGE 67>>>
- **P38** 标准升级认证回滚机制：working 目录 reload 试验成功后 `copy running certified` 固化；出问题用 `reload from certified no rollback-timeout` 回退 <<<PAGE 73>>>
- **P39** ONIE 机型 CPLD 升级语义：kit 内含多 CPLD updater，命令按平台/CPLD 类型逐个升级需多次执行，升级后手动 reload 进 "ONIE: Update ONIE" 模式（不得按键），完成后只回 Certified 目录不回 running <<<PAGE 82>>>
- **P40** 出厂首启 VC 自动化副作用：vcboot.cfg/vcsetup.cfg 只写 working 不写 certified → 下次重启 Running Configuration 落到 certified、脱离出厂默认模式且 chassis-id=1，可能在 VC 里引发 chassis-id 冲突，需 `reset-to-factory` 纠正 <<<PAGE 15>>>
- **P41** NTP 遵循 RFC 不再同步 stratum 16（未同步）服务器，OmniSwitch 之间级联对时的存量部署会断同步 <<<PAGE 16>>>
- **P42** Celona AP autoclass 降级问题机理：PD 侧硬件信号错误使 Class 6/8 设备被识别为 Class 4 限到 30W，交换机无法纠正，禁用 autoclass 规避："Since this is a hardware behavior on the Celona side and cannot be corrected by the switch, the workaround is to disable autoclass." <<<PAGE 34>>>
- **P43** ERP 与 MACsec 交互语义：MACsec/MKA 单侧关闭时 R-APS 仍可从不受影响端口交换，ERP 环可能回到 Idle/RPL 阻塞——属预期行为（8.10R4 文档化） <<<PAGE 90>>>/<<<PAGE 91>>>
- **P44** DHL 无缝切换规模边界：4000 VLAN/大 MAC 场景下无缝 failover 支持 128 VLAN/1000 MAC，超出需把 pre-empt timer 从默认 30 秒提到 60 秒防残留 MAC："DHL supports up to 128 VLANs and 1000 MACs for seamless failover." <<<PAGE 97>>>
- **P45** OS6920 400G 平台定位：1RU 32×400G QSFP-DD、低时延 L2/L3，本版无 VC 支持 <<<PAGE 21>>>
- **P46** OS6575 工业平台特性：-40°C~75°C 加固无风扇，P12（8×bt+4×SFP+ VFL，360W PoE）、U28（1U 机架，210W）、MP16（M12 连接器墙装，Bypass 功能，无 VC，120W）；支持 VC 最多 4 机箱（P12/U28）<<<PAGE 21>>>
- **P47** 认证升级双通道：HSP（Hitless Security Patch Upgrade）与 Signed AOS Image 平台覆盖见 Feature Matrix，签名镜像要求 U-Boot 支撑（6570M 8.9R4 起）<<<PAGE 53>>>
- **P48** 许可分层模型：Data Center 许可（本版均不支持 DCB/FIP/FCoE）→ Feature/Performance 许可（MACsec/10G/MPLS/50G）→ Metro 许可（8.9R1 起 6560 收费）→ Advanced Routing 许可（6560 版限 2 OSPF 区域、无 VRF/ISIS/隧道；8.10R4 加 BGP）→ Premium 捆绑 <<<PAGE 19>>>/<<<PAGE 20>>>

---
合计：48 条（P1-P48）。
