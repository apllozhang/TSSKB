# 术语词典

| 术语 | 全称/中文 | 释义 |
|---|---|---|
| SPB / SPB-M | Shortest Path Bridging (Mac-in-Mac mode)，最短路径桥接 | IEEE 802.1aq，用 IS-IS 做控制面的以太网织构；SPB-M 为 MAC-in-MAC 封装模式 |
| iFab | Intelligent Fabric，智能织构 | ALE 基于 SPB 的网络方案品牌 |
| IS-IS | Intermediate System to Intermediate System | SPB 的唯一控制协议，链路状态路由协议 |
| BEB | Backbone Edge Bridge，骨干边缘网桥 | SPB 网络边缘节点，业务（ISID）的进出点；轨交中即车站/中心的骨干接入点 |
| BCB | Backbone Core Bridge，骨干核心网桥 | SPB 骨干中间转发节点 |
| B-MAC / C-MAC | Backbone / Customer MAC | MAC-in-MAC 外层骨干 MAC 与内层客户 MAC |
| B-VLAN (BVLAN) | Backbone VLAN | 骨干 VLAN，承载 SPB 隧道，每 BVLAN 生成一棵 SPT |
| I-SID | Backbone Service Instance Identifier | SPB 服务实例编号，逻辑上标识一个 VPN/容器（E-LAN/LINE/TREE） |
| ECT-ALGORITHM | Equal Cost Tree algorithm | 32 位 SPF 平局裁决规则集，不同 ECT-ID 使 BVLAN 生成不同 SPT |
| SPT | Shortest Path Tree，最短路径树 | SPF 计算出的转发树 |
| LSDB | Link State Database，链路状态数据库 | IS-IS 拓扑数据库 |
| SAP | Service Access Point | SPB 侧的业务接入点（UNI），按 VLAN 标签映射 ISID |
| UNI | User-Network Interface | 用户网络接口；文中分 SAP UNI 与 VLAN UNI 两种挂接形态 |
| Hairpin | 发卡环 | BEB 上把标准 VLAN 口与 SAP 口对接的环回接法，用于路由或 ERP VLAN 映射 |
| BUM | Broadcast, Unknown unicast, Multicast | 广播、未知单播、组播流量统称，涉及复制模式选择 |
| Head-End 复制 | — | BUM 在入口 BEB 复制成多份单播；省资源费带宽 |
| Tandem (S,G) / (*,G) | — | 骨干内建组播树复制：(S,G) 为源树、与单播同径；(*,G) 为共享树、根在 bridge priority 决定的节点 |
| PIM / SSM / RP | Protocol Independent Multicast / Source Specific Multicast / Rendezvous Point | L3 组播协议族；轨交设计 RP 放 OCC，SSM 让同站源收直连 |
| IGMP Snooping | — | 监听 IGMP 报告按需转发组播，Head-End 模式的优化配套 |
| ERP / ERPv2 | Ethernet Ring Protection（ITU-T G.8032） | 以太环网保护，站点接入网常用；R-APS 为其控制报文 |
| R-APS | Ring Automated Protection Switching | G.8032 环保护协议报文 |
| STP / MSTP | Spanning Tree Protocol / Multiple STP | 生成树防环协议；按站分 MSTP region 隔离 STP 域 |
| LBD | Loopback Detection，环回检测 | 周期发探测帧检测成环并 shutdown 端口，保护骨干 |
| MVRP | Multiple VLAN Registration Protocol | VLAN 动态注册协议，接入侧新建 VLAN 自动上联 |
| VRRP | Virtual Router Redundancy Protocol | 默认网关冗余协议；站点 BEB 或 OCC/BCC 组冗余对 |
| VRF | Virtual Routing and Forwarding | L3 路由实例，每个需 L3 隔离的系统一个 VRF |
| LAG | Link Aggregation Group | 链路聚合；tunnel-protocol 选项让哈希可用 C-MAC/IP |
| VC | Virtual Chassis，虚拟机箱 | 多台堆叠为单一逻辑设备、单一控制面 |
| ISSU | In-Service Software Upgrade | 不中断业务软件升级 |
| OCC / BCC | Operations Control Center / Backup Control Center | 运营控制中心 / 备份控制中心，可主主或主备 |
| ATC / ATP / ATO / ATS | Automatic Train Control / Protection / Operation / Supervision | 列车自动控制四件套：防护、驾驶、监控 |
| AFC | Automatic Fare Collection，自动售检票 | 含售票机、闸机、刷卡终端 |
| PIS / PA(PAS) | Passenger Information System / Passenger Announcement (Public Address) | 乘客信息系统 / 广播系统 |
| CCTV / VS | Closed-Circuit Television / Video Surveillance | 视频监控，通常是轨交网最大流量源 |
| TDS | Time Distribution System | 时间同步系统（常配 IEEE 1588v2） |
| ITS | Intelligent Transportation System | 智能交通系统（道路场景） |
| TMS / TIS / VSL | Traffic Management / Traveler Information System / Variable Speed Limit | 交通管理 / 出行者信息 / 可变限速（ITS 场景） |
| NAC | Network Admission Control | 网络准入控制（802.1x/MAC 认证/Captive Portal） |
| UNP / NP | User Network Profile / Network Profile | 认证返回或预定义的设备策略档案，绑 VLAN/服务并携带 ACL/QoS |
| MACsec | IEEE 802.1AE | MAC 层点到点认证与加密，硬件线速 |
| OAM / 802.1ag | Operations and Maintenance | 以太网运维：L2 ping（LBM/LBR）、L2 trace（LTM/LTR）、MEP/MIP 维护点 |
| MEP / MIP | Maintenance End / Intermediate Point | 维护域端点/中间点 |
| CCM | Continuity Check Message | 连续性检查报文，SPB 场景下不与 802.1ag 配套使用 |
| SAA | Service Assurance Agent | 时延/抖动/丢包性能测试代理，saa auto-create 全网自动铺 |
| OOBMN / EMP | Out-of-Band Management Network / Ethernet Management Port | 带外管理网 / 专用管理以太网口 |
| GR | Graceful Restart，优雅重启 | 主控切换期间保邻接、保 FDB、由邻居回灌 LSDB |
| Overload state | 过载状态 | IS-IS 通告本节点不做中转，等效快速抬高全部链路 metric，用于优雅下线维护 |
| DoS / DDoS | Denial of Service / Distributed DoS | 拒绝服务攻击；OmniSwitch 内置过滤（Land、Ping of Death、ARP Flood 等） |
| IDS | Intrusion Detection System | 入侵检测系统，与 OmniVista 经 Syslog 联动隔离 |
| Common Criteria / EAL / NDcPP | 通用准则 / 评估保证级 / 网络设备协作保护轮廓 | 独立安全认证体系，OmniSwitch 达 EAL-2 |
| FIPS 140-2 | — | 美加密码模块标准 |
| JITC | Joint Interoperability Test Command | 美国防部互操作认证 |
| EN 50121 / NEMA TS-2 | — | 轨道旁 / 路边机柜的电磁兼容与工业环境标准 |
| DIN mount / IP-30 | — | 导轨安装 / 防护等级，加固交换机特征 |
| HPoE | High Power over Ethernet | 大功率以太网供电（60W，供 PTZ 摄像机等） |
| SPOF | Single Point of Failure | 单点故障 |
| EOL / LOD | End-of-Life / Last Order Day | 停产 / 最后订购日；10 年 LTS 须在 LOD 前 ≥6 个月下单 |
| WFQ / SP / WRED / EF / AF / BE | 加权公平队列 / 严格优先 / 加权随机早期检测 / 加速转发 / 确保转发 / 尽力而为 | QoS 队列与每跳行为（PHB）术语 |
