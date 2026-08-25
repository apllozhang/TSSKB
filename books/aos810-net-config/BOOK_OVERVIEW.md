# OmniSwitch AOS Release 8.10R4 Network Configuration Guide — 全书概览

- 书名：OmniSwitch AOS Release 8 Network Configuration Guide（8.10R4）
- 出版：ALE（Alcatel-Lucent Enterprise），2025-12，Part No. 060969-00 Rev. A
- 页数：正文 1745 页（fulltext.md 页码标记 `<<<PAGE N>>>`）
- 性质：OmniSwitch 多产品线 AOS 8 特性配置手册（CLI 配置向导型文档）

## 章节结构与蒸馏重点

| 章 | 标题 | 正文起始页 | 蒸馏重点 |
|---|---|---|---|
| 1 | Configuring Ethernet Ports | <<<PAGE 51>>> | 端口参数/EEE/DDM/TDR 诊断/链路监控/Violation Recovery/Link Fault Propagation/MACsec(含 WAN MACsec) |
| 2 | Configuring UDLD | ~<<<PAGE 195>>> | 单向链路检测机制、probe/echo 定时器 |
| 3 | Managing Source Learning | ~<<<PAGE 225>>> | MAC 表、静态单播/组播 MAC、老化时间 |
| 4 | Configuring VLANs | ~<<<PAGE 260>>> | VLAN 创建/802.1Q 打标/Private VLAN 体系 |
| 5 | High Availability VLANs | ~<<<PAGE 380>>> | 服务器集群（L2/L3 cluster）、虚 MAC |
| 6 | Spanning Tree Parameters | ~<<<PAGE 430>>> | STP/RSTP/MSTP 拓扑计算、Flat/Per-VLAN 模式、PVST+ 互通、Loop-guard、Root Guard |
| 7 | Shortest Path Bridging (SPBM) | ~<<<PAGE 700>>> | ISIS-SPB 骨干、SPB 服务/I-SID/SAP/Pseudo-wire、IP over SPB、SPB over Shared Ethernet |
| 8 | Loopback Detection | ~<<<PAGE 965>>> | LBD 机制、remote-origin LBD、与 STP/链路聚合交互 |
| 9 | Static Link Aggregation | ~<<<PAGE 1000>>> | 静态聚合组 |
| 10 | Dynamic Link Aggregation | ~<<<PAGE 1040>>> | LACP 动态聚合、actor/partner 参数 |
| 11 | Dual-Home Links | ~<<<PAGE 1150>>> | DHL Active-Active/Active-Standby、推荐拓扑 |
| 12 | ERP | ~<<<PAGE 1210>>> | G.8032 环网、RPL owner、guard/wait-to-restore、ERPv2 子环、ERP over SPB |
| 13 | MRP | ~<<<PAGE 1330>>> | 工业环网 MRM/MRC/MRA、MRP Interconnect（MIM/MIC） |
| 14 | MVRP | ~<<<PAGE 1370>>> | VLAN 动态注册、applicant 模式、定时器 |
| 15 | MPLS | ~<<<PAGE 1410>>> | LDP 信令 LSP、LDP GR、MPLS ping/traceroute |
| 16 | L2VPN (VPLS/VPWS) | ~<<<PAGE 1470>>> | VPLS LDP/BGP 信令、SAP/SDP、VPWS |
| 17 | VXLAN Gateway | ~<<<PAGE 1720>>> | VXLAN 封装/VTEP、SDP 绑定、BIDIR-PIM 下层 |
| 18 | EVPN | ~<<<PAGE 1940>>> | BGP EVPN 路由类型、IRB（对称/非对称）、DAG、OISM、EVPN-VXLAN、Clos/Multi-site 部署模型 |
| 19 | 802.1AB (LLDP) | ~<<<PAGE 2330>>> | LLDPDU/TLV、LLDP-MED |
| 20 | SIP Snooping | ~<<<PAGE 2400>>> | SIP 监听、信任服务器、RTCP 阈值 |
| 21 | IP | ~<<<PAGE 2460>>> | IP 接口/静态路由/ARP/GARP/DoS 过滤/隧道(GRE,IPIP)/VRF Route Leak |
| 22 | Multiple VRF | ~<<<PAGE 2690>>> | VRF 实例/profile、Management VRF、特性交互 |
| 23 | IPv6 | ~<<<PAGE 2760>>> | IPv6 寻址/RA 过滤/NUD/DoS 检测/VRF leak |
| 24 | IPsec | ~<<<PAGE 2950>>> | ESP/AH 策略、SA、discard 策略 |
| 25 | RIP | ~<<<PAGE 3030>>> | RIPv1/v2、定时器、SHA256 认证 |
| 26 | BFD | ~<<<PAGE 3100>>> | BFD 会话/echo、与各 L3 协议联动 |
| 27 | DHCP Relay | ~<<<PAGE 3300>>> | 内部/外部 relay、Option-82、DHCP Snooping、Generic UDP Relay、DHCPv6 Relay/Snooping/RA Guard |
| 28 | Internal DHCP Server | ~<<<PAGE 3520>>> | 策略文件/配置文件/数据库 |
| 29 | VRRP | ~<<<PAGE 3750>>> | 虚拟路由器、优先级/preempt、VRRP tracking+BFD、V3 |
| 30 | Server Load Balancing | ~<<<PAGE 3890>>> | SLB 集群、WRR、健康探测 |
| 31 | IP Multicast Switching | ~<<<PAGE 3970>>> | IGMP v1-3 参数、IPMSv6/MLD、组播路由交互 |
| 32 | IP Multicast VLAN | ~<<<PAGE 4220>>> | IPMVLAN 企业模式/VLAN Stacking 模式 |
| 33 | QoS | ~<<<PAGE 4280>>> | 分类标记、QSet/队列、policing/shaping、policy 条件动作规则、ACL、条件组、map group、ECN |
| 34 | Policy Servers | ~<<<PAGE 4720>>> | LDAP 策略服务器 |
| 35 | Access Guardian (UNP) | ~<<<PAGE 4740>>> | 802.1X/MAB/设备分类/UNP profile/端口、Captive Portal、BYOD(mDNS/SSDP)、IoT profiling、Stellar AP、L2 GRE、QMR、Switch Supplicant |
| 36 | Application Monitoring (AppMon) | ~<<<PAGE 5600>>> | DPI 应用监控/强制、签名、Threat-Insight |
| 37 | Application Fingerprinting (AFP) | ~<<<PAGE 5680>>> | REGEX 指纹识别 |
| 38 | Authentication Servers | ~<<<PAGE 5750>>> | RADIUS/RADSEC/TACACS+/LDAP、PKI、PKIX-SSH、Kerberos Snooping |
| 39 | Port Mapping | ~<<<PAGE 6000>>> | 端口映射会话 |
| 40 | Learned Port Security | ~<<<PAGE 6030>>> | MAC 学习窗口、违规模式 |
| 41 | Diagnosing Switch Problems | ~<<<PAGE 6170>>> | 端口镜像/监控、sFlow、RMON、Switch Health |
| 42 | VLAN Stacking | ~<<<PAGE 6370>>> | QinQ SVLAN/CVLAN、SAP/UNI profile、硬件环回测试 |
| 43 | Switch Logging | ~<<<PAGE 6550>>> | 日志级别/输出/格式 |
| 44 | Ethernet OAM (Service OAM/CFM) | ~<<<PAGE 6590>>> | MD/MA/MEP、Loopback/Linktrace、帧时延测量 |
| 45 | EFM (LINK OAM) | ~<<<PAGE 6670>>> | 发现/链路监控/远端环回 |
| 46 | CPE Test Head | ~<<<PAGE 6710>>> | L2 SAA 测试/测试组 |
| 47 | PPPoE Intermediate Agent | ~<<<PAGE 6870>>> | PPPoE-IA、Circuit-ID/Remote-ID |
| 48 | Service Assurance Agent | ~<<<PAGE 6900>>> | SAA SPB 会话、XML 历史 |

（正文起始页为近似值，提取时以 fulltext.md 内真实 `<<<PAGE N>>>` 标记为准。）

## 文档体例规律（对蒸馏有用）

- 每章结构固定：In This Chapter → Defaults 表 → Quick Steps → Overview（原理）→ Configuring（逐参数 CLI）→ Application Example → Verifying。
- "Quick Steps" 与 "Application Example" 是 cases 的主要来源；"Overview/How ... Works" 是 principles 主要来源；"Interaction With Other Features"、"Configuration Guidelines"、"Limitations"、Defaults 表注记是 counter-examples 主要来源。
- CLI 命令均以 OmniSwitch AOS 语法给出（如 `vlan 10 port default 1/1/1`、-> 配置层级缩进）。
