---
name: 园区 LAN/WLAN 设计（分层模型/Stellar 无控制器/AP 双域发现/漫游判定）
description: 需要设计园区网（两层折叠 vs 三层、VC/VLAN/MVRP/LACP、互联技术与路由协议选型）或 WLAN（RF 规划、分布式控制面、VLAN 域/服务域两套 AP 发现命令、漫游判定矩阵、VLAN 池、VoWLAN/QoS）时使用。
source_book: ALE Mobile Campus Architecture Guide（sol-campus-architecture DOC1）
---

## R（触发场景）
- 园区新建/改造：选两层折叠核心还是三层模型，规划接入层构件
- 部署 Stellar WLAN：RF 规划、管理模式选择、AP 接入交换机配置
- 处理 AP 发现（VLAN 域 vs SPB 服务域两套命令集）、客户端 VLAN 接纳
- 分析漫游类型（L2/L3/快速漫游）与用户 VLAN 规划（VLAN 池）
- 高密/语音场景 QoS 与容量约束

## I（核心理念）
园区设计栈（F1，<<<PAGE 6>>>）：四目标（可用/扩展/安全/性能）→ 拓扑模型 → 接入层构件 → 互联技术选型 → 动态路由。WLAN 框架（F2，<<<PAGE 15>>>）：管理面集中（OmniVista）+ 控制面分布（AP 间 NMP 同步）+ 数据面本地桥接优先、按 ARP 动态切 L2GRE 隧道。分布式控制面消除单点/瓶颈并降 CapEx/OpEx（P22/P23，<<<PAGE 15-16>>>）；数据面默认本地桥接保性能，仅安全/集中审查场景隧道化（P24/P25，<<<PAGE 16-17>>>）。AP 接入双域（F3，<<<PAGE 23>>>）：VLAN 域与服务域两条对称的发现-分类-映射路径。漫游框架（F4，<<<PAGE 26>>>）：客户端上下文共享 → 三分支判定矩阵；子网收敛 /24 + VLAN 池是容量底座。

## A1（行动框架）
1. 拓扑选型：中小园区两层折叠（少跳数少部件，P3，<<<PAGE 7>>>）；大型复杂园区三层（模块化可扩展，P4，<<<PAGE 7>>>）
2. 接入层基线：VC/Stack 扩密度保控制面韧性（P5，<<<PAGE 8>>>）+ VLAN 动态分配（P6，<<<PAGE 8>>>）+ MVRP 按需传播（P7，<<<PAGE 9>>>）+ Trunk/LACP（P11/P12，<<<PAGE 9>>>）
3. 互联与路由选型（P13-P16，<<<PAGE 10-12>>>）：大园区扁平 L2 多租户→SPB；跨广域 L2 互联+多归属→EVPN；流量工程/QoS→MPLS；OSPF 分区/BGP 互联/IS-IS 大核心，RIP 不推荐大规模
4. WLAN 规划七要素（P17/P18，<<<PAGE 12-13>>>）：覆盖/容量/信道/安装密度/功率天线/预测热图/RDA，用 OmniVista Floor Plan 仿真验证；管理模式按规模递进 Express→Enterprise→Cloud（P27，<<<PAGE 18>>>）；按 AP 组+RF Profile 组织（P28/P29，<<<PAGE 18>>>）
5. 用户 VLAN 规划：子网收敛 /24（P38，<<<PAGE 28>>>）+ VLAN 池首选（P39，<<<PAGE 28>>>）+ 无线客户端独立 VLAN ID（P9，<<<PAGE 8>>>）+ AP 管理与有线管理 VLAN 分开、每 VLAN 最多 64 AP（P8，<<<PAGE 8>>>）

## A2（操作步骤）
- **VLAN 域 AP 发现**（C1，<<<PAGE 23>>>）：`vlan 125 name "AP Management VLAN"` → 上联口 tagged → `unp profile defaultWLANProfile map vlan 125` → `unp port 1/1/1 port-type bridge` → 按需 `ap-mode` → `mvrp enable` → 配 system name/location 供 LLDP 传位置
- **服务域（SPB）AP 发现**（C2，<<<PAGE 25>>>）：`service l2profile "ap-SvcUnp" 802.1ab peer` → `unp port 1/1/1 port-type access` + `l2-profile` + `ap-mode` → `unp profile defaultWLANAccessProfile map service-type spb tag-value 0 isid 1000 bvlan 4000` → 客户端画像 `unp profile spb10 map service-type spb tag-value 10 isid 1010 bvlan 4000` → `unp classification vlan-tag 10 profile1 spb10`
- **AP 安全模式认证时序**（C3，<<<PAGE 20>>>）：LLDP-MED 自证→UNP 归入画像回发 LLDP→802.1x 认证→DHCP+Option 138 得 OmniVista 地址→MQTT 建管通道
- **Trust Tag 接纳客户端**（C4，<<<PAGE 21>>>）：信任 AP 客户端 SSID VLAN tag→匹配本地 VLAN→无则自动创建→MVRP 分发
- **漫游判定矩阵**（C5，<<<PAGE 26>>>）：新 AP 无上下文→按新客户端；上下文+ARP 匹配→L2 漫游；上下文+VLAN 不匹配→L3 漫游（L2GRE 回家乡 AP）
- **L2GRE 隧道部署**（C6，<<<PAGE 17>>>）：接入/汇聚交换机各配端点→UNP 分类→画像映射 L2 GRE 服务→封装至汇聚解封装上 perimeter
- **高密/语音 QoS**（P40-P43，<<<PAGE 28-32>>>）：角色定 VLAN+QoS；带宽契约+每 AP 客户端限额；组播超阈值转单播；VoWLAN 优先 5GHz、每 AP 限 20-25 语音客户端保 36 Mbps

## E（实证案例）
- VLAN 域与服务域两套完整配置流程互为镜像（C1/C2，<<<PAGE 23>>>/<<<PAGE 25>>>）
- L3 漫游走包：客户端上下文共享→VLAN 不匹配→L2GRE 隧道保原 IP 免重认证（C5/C6，<<<PAGE 26>>>/<<<PAGE 17>>>）
- 单 AP 故障邻 AP 自动补位（加功率保覆盖）验证分布式韧性（X6，<<<PAGE 15>>>）

## B（反例与坑）
- 静态 VLAN 指定不可行；全量建 VLAN 拖垮扩展性与稳定性（X1/X2，<<<PAGE 8-9>>>）
- 集中控制器三宗罪：单点/瓶颈/时延，且购置维护电费持续成本高（X4/X5，<<<PAGE 15-16>>>）
- OmniVista 不逐台管 AP，必须按 AP 组（X7，<<<PAGE 18>>>）
- 单 VLAN 按 AP 组分组在会场高密场景失效——用 VLAN 池（X8，<<<PAGE 28>>>）
- 2.4GHz 不适合语音；语音客户端超 20-25/AP 掉质量（X9/X10，<<<PAGE 32>>>）
- 组播低速率广播发送效率低，应动态转单播（X12，<<<PAGE 29>>>）
- 端口只能属于一个 untagged VLAN，但可属多个 tagged（X3，<<<PAGE 9>>>）

来源：ALE Mobile Campus Architecture Guide（sol-campus-architecture DOC1，p5-32）
