# 《OmniSwitch AOS Release 810R04 CLI Reference User Guide》总览

- 版本：AOS Release 8.10R4（Part No. 060971-00, Rev. A, December 2025）
- 规模：6240 页（全文页码标记 `<<<PAGE N>>>`），70 个命令章，目录命令条目约 2480 条（含 show 命令）
- 性质：**命令参考字典**，非教程。每章按"命令 → 语法 → 参数 → 默认值 → 支持平台矩阵（6360/6465/6560/6570M/6860/6860N/6865/6870/6900/6575/6920/9900）→ 用法指南 → 示例 → Release History → 相关命令 → MIB Objects"固定结构展开。
- 页码约定：本库页码取 PDF 全文标记 `<<<PAGE N>>>`（正文第 1 章始于 `<<<PAGE 67>>>`，对应书内页 1-1；前置目录约占 PAGE 1-66）。

## 蒸馏策略（命令地图型，不做全量蒸馏）

1. **以章为最小导航单元**：70 章全部登记（见 glossary.md），每章一条，含起始页码与命令域归属。
2. **命令域分组**：把 70 章归入 10 个命令域（见 candidates/frameworks.md），形成"域 → 章 → 命令"三级导航。
3. **代表章定点深读**：每域选 1-2 个代表章（VLAN Management、SPB、QoS Policy、Access Guardian、OSPF、BGP、PoE、Link Aggregation、Virtual Chassis、VLAN Stacking 等）提炼命令族语义与关键默认值（见 candidates/principles.md）。
4. **限制与反例**：从代表章的 Usage Guidelines/Notes 提取平台限定、互斥、前置条件（见 candidates/counter-examples.md）。
5. **不做**：逐命令语法全量搬运（原书即是字典，可直接按页码回查）；cases.md 跳过（命令字典无业务流程案例）。

## 70 章清单（章名 | 起始页码标记 | 命令域 | 目录命令条目数估计）

| 章 | 章名 | 起始页 | 命令域 | 条目数 |
|---|---|---|---|---|
| 1 | Ethernet Port Commands | 67 | D1 端口与 PoE | 85 |
| 2 | Power over Ethernet (PoE) Commands | 254 | D1 端口与 PoE | 38 |
| 3 | UDLD Commands | 327 | D1 端口与 PoE | 12 |
| 4 | Source Learning Commands | 351 | D2 二层与 VLAN | 33 |
| 5 | VLAN Management Commands | 427 | D2 二层与 VLAN | 13 |
| 6 | High Availability VLAN Commands | 455 | D2 二层与 VLAN | 10 |
| 7 | VLAN Stacking Commands | 476 | D2 二层与 VLAN | 40 |
| 8 | Distributed Spanning Tree Commands | 567 | D3 冗余与环网 | 50 |
| 9 | MPLS Commands | 689 | D4 SPB/MPLS 骨干与服务 | 26 |
| 10 | Shortest Path Bridging Commands | 743 | D4 SPB/MPLS 骨干与服务 | 43 |
| 11 | Service Manager Commands | 839 | D4 SPB/MPLS 骨干与服务 | 83 |
| 12 | Loopback Detection Commands | 1070 | D3 冗余与环网 | 11 |
| 13 | Link Aggregation Commands | 1092 | D3 冗余与环网 | 46 |
| 14 | Virtual Chassis Commands | 1198 | D5 VC/自动织构与数据中心 | 32 |
| 15 | Ethernet Ring Protection Commands | 1268 | D3 冗余与环网 | 16 |
| 16 | Media Redundancy Protocol Commands | 1306 | D3 冗余与环网 | 11 |
| 17 | MVRP Commands | 1340 | D2 二层与 VLAN | 23 |
| 18 | 802.1AB Commands | 1390 | D9 监测与 OAM | 40 |
| 19 | SIP Commands | 1486 | D5 VC/自动织构与数据中心 | 18 |
| 20 | Automatic Fabric Commands | 1523 | D5 VC/自动织构与数据中心 | 12 |
| 21 | IP Commands | 1549 | D6 IP 与路由 | 113 |
| 22 | IPv6 Commands | 1793 | D6 IP 与路由 | 68 |
| 23 | IPsec Commands | 1948 | D8 安全与准入 | 11 |
| 24 | RIP Commands | 1974 | D6 IP 与路由 | 41 |
| 25 | BFD Commands | 2058 | D6 IP 与路由 | 16 |
| 26 | DHCP Relay Commands | 2092 | D6 IP 与路由 | 116 |
| 27 | VRRP Commands | 2334 | D6 IP 与路由 | 24 |
| 28 | OSPF Commands | 2392 | D6 IP 与路由 | 57 |
| 29 | OSPFv3 Commands | 2513 | D6 IP 与路由 | 46 |
| 30 | IS-IS Commands | 2610 | D6 IP 与路由 | 62 |
| 31 | BGP Commands | 2744 | D6 IP 与路由 | 194 |
| 32 | Server Load Balancing Commands | 3160 | D6 IP 与路由 | 31 |
| 33 | IP Multicast Switching Commands | 3227 | D7 组播 | 106 |
| 34 | IP Multicast VLAN Commands | 3471 | D7 组播 | 12 |
| 35 | DVMRP Commands | 3495 | D7 组播 | 23 |
| 36 | PIM Commands | 3542 | D7 组播 | 99 |
| 37 | Multicast Routing Commands | 3769 | D7 组播 | 14 |
| 38 | QoS Commands | 3797 | D10 QoS 与策略 | 70 |
| 39 | QoS Policy Commands | 3953 | D10 QoS 与策略 | 111 |
| 40 | Policy Server Commands | 4190 | D10 QoS 与策略 | 9 |
| 41 | AAA Commands | 4205 | D8 安全与准入 | 119 |
| 42 | Access Guardian Commands | 4470 | D8 安全与准入 | 199 |
| 43 | Application Monitoring and Enforcement | 4934 | D10 QoS 与策略 | 37 |
| 44 | Application Fingerprinting Commands | 5016 | D10 QoS 与策略 | 12 |
| 45 | FIP Snooping Commands | 5039 | D5 VC/自动织构与数据中心 | 22 |
| 46 | FCoE/FC Gateway Commands | 5090 | D5 VC/自动织构与数据中心 | 27 |
| 47 | VXLAN Snooping Commands | 5152 | D5 VC/自动织构与数据中心 | 20 |
| 48 | Port Mapping Commands | 5195 | D5 VC/自动织构与数据中心 | 9 |
| 49 | Learned Port Security Commands | 5212 | D8 安全与准入 | 18 |
| 50 | Port Mirroring and Monitoring | 5256 | D9 监测与 OAM | 9 |
| 51 | sFlow Commands | 5277 | D9 监测与 OAM | 13 |
| 52 | RMON Commands | 5305 | D9 监测与 OAM | 4 |
| 53 | Switch Logging Commands | 5313 | D11 系统与管理 | 14 |
| 54 | Health Monitoring Commands | 5347 | D9 监测与 OAM | 6 |
| 55 | Ethernet OAM Commands | 5358 | D9 监测与 OAM | 46 |
| 56 | LINK OAM Commands | 5432 | D9 监测与 OAM | 23 |
| 57 | CPE Test Head Commands | 5503 | D9 监测与 OAM | 31 |
| 58 | PPPoE Intermediate Agent | 5571 | D8 安全与准入 | 12 |
| 59 | Service Assurance Agent Commands | 5597 | D9 监测与 OAM | 19 |
| 60 | CMM Commands | 5645 | D11 系统与管理 | 29 |
| 61 | Chassis Management and Monitoring | 5697 | D11 系统与管理 | 91 |
| 62 | Network Time Protocol Commands | 5884 | D11 系统与管理 | 25 |
| 63 | Session Management Commands | 5936 | D11 系统与管理 | 35 |
| 64 | File Management Commands | 5999 | D11 系统与管理 | 21 |
| 65 | Web Management Commands | 6040 | D11 系统与管理 | 11 |
| 66 | Configuration File Manager Commands | 6060 | D11 系统与管理 | 11 |
| 67 | SNMP Commands | 6079 | D11 系统与管理 | 26 |
| 68 | OmniVista Cirrus Commands | 6132 | D11 系统与管理 | 10 |
| 69 | OpenFlow Commands | 6151 | D11 系统与管理 | 8 |
| 70 | DNS Commands | 6169 | D11 系统与管理 | 6 |

注：条目数为目录中以"省略号+章-页"结尾的命令条目统计（含子命令与 show 命令），为估计值；第 19 章 SIP 的域归属为建议值（章名缩写在目录中未展开，待确认）。
