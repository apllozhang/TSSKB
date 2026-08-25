# DIGEST — OmniSwitch AOS 8.10R4 Network Configuration Guide 精华

本书是 ALE OmniSwitch 多产品线 AOS Release 8.10R4 的 1745 页特性配置手册（48 个功能章）。它没有叙事结构，是"某特性怎么配、默认值是什么、与其他特性怎么交互"的 CLI 查询底座。全书统一章法（F1）：Defaults→Quick Steps→Overview→Configuring→Example→Verifying——排障时按固定小节定位，Quick Steps 与 Application Example 提供可复制流程，"Interaction With Other Features"与 Limitations 提示跨功能约束。以下按十个技能单元摘要，页码均指原书。

## 一、知识地图（十技能单元）

1. **交换机基础**（aos-nc-switch-foundation）：端口参数/DDM/风暴控制/流控/违规恢复统一框架/MACsec/静态 MAC/TDR 诊断（Ch1-3，p56-108）。
2. **VLAN 与二层域**（aos-nc-vlan-l2）：VLAN/802.1Q/PVLAN/HA VLAN/MVRP/VLAN Stacking(QinQ)（Ch4-5/14/42，p115-129、140、442-447、1606-1622）。
3. **二层冗余与保护**（aos-nc-redundancy-protection）：STP/RSTP/MSTP、UDLD、LBD、静态/LACP 聚合、DHL、ERP(G.8032)、MRP（Ch2/6/8-13，p98-437）。
4. **骨干与 Fabric**（aos-nc-fabric-backbone）：SPBM/ISIS-SPB、MPLS/LDP、VPLS/VPWS、VXLAN、EVPN（Clos/Multi-site）（Ch7/15-18，p211-661）。
5. **IP/IPv6 服务**（aos-nc-ip-ipv6-services）：IP 接口/静态路由/VRF/GRE/IPIP、IPv6/ND、IPsec、DHCP Relay/Snooping/内部 Server/DHCPv6（Ch21-24/27-28，p709-926）。
6. **路由基础**（aos-nc-routing）：RIP、BFD、VRRP/tracking、SLB；OSPF/IS-IS/BGP 主体在 Advanced Routing 手册（Ch25-26/29-30，p842-1015）。
7. **组播**（aos-nc-multicast）：IPMS/IPMSv6（IGMP/MLD）、PIM/DVMRP/IPMSR、IPMVLAN/MVR（Ch31-32，p1032-1093）。
8. **QoS 与策略**（aos-nc-qos-policy）：分类标记/队列/policing/shaping、policy 三元组、条件组/map group、ACL、SIP snooping（Ch20/33-34，p704、1103-1176）。
9. **接入安全**（aos-nc-access-security）：AAA、Access Guardian/UNP、Captive Portal、BYOD(mDNS/SSDP)、L2 GRE、AppMon/AFP、LPS、镜像/sFlow/RMON（Ch35-41，p1210-1567）。
10. **OAM 与运维监测**（aos-nc-oam-monitoring）：Service OAM/CFM、EFM LINK OAM、Switch Health、日志、SAA、PPPoE-IA（Ch43-48，p1580-1715）。

## 二、十单元要点串讲

### 1. 交换机基础：违规恢复是统一底层
端口自协商禁用后 auto MDIX/speed/duplex 全失效（<<<PAGE 56>>>）。风暴控制按 bcast/uucast/mcast 分别限速，默认动作纯丢包不告警，要感知须显式配 action/trap，自动恢复靠 low-threshold（<<<PAGE 59>>>）。违规关停与恢复统一框架（F2）：十余个特性共用 shutdown/recovery/trap，排障先查 `show violation`（<<<PAGE 69>>>）；Administratively 关断插拔网线救不回，永久关断只能 clear violation（<<<PAGE 69-70>>>）。MACsec 三模式：静态 SA（两端手工配匹配 SAK）、动态 SAK(PSK)、动态 CAK(EAP 须 EAP-TLS)（<<<PAGE 83-85>>>）。静态 MAC 分 bridging/filtering，聚合口配在 linkagg ID（<<<PAGE 105-106>>>）。

### 2. VLAN 与二层域：演进框架选型
标准 VLAN→802.1Q→PVLAN→QinQ→VXLAN→EVPN 按隔离需求逐级选用（F17）。端口只能属一个 untagged VLAN；VLAN 在有活动端口前保持 inactive（<<<PAGE 115>>>）。PVLAN 主 VLAN 配置自动作用于二级 VLAN，IP 接口只能配主 VLAN（<<<PAGE 129>>>）。QinQ 隧道 ID 与 VLAN ID 一一对应，double tagging 与 VLAN translation 两法（<<<PAGE 1608>>>）。MVRP 动态声明 VLAN 成员，与 per-VLAN STP 互斥（<<<PAGE 444>>>）。HA VLAN 用静态 MAC(L2)/静态 ARP(L3) 实现服务器集群（<<<PAGE 140>>>）。

### 3. 二层冗余：分层防环选型
STP→UDLD→LBD→ERP/MRP→DHL→SPBM 分层选型（F3）。MSTP 仅 Flat 模式，MSTI 端口状态由 CST 统一算，单实例独立转发要调 path cost（<<<PAGE 164>>>）。聚合组成员必须同速，静态聚合与部分厂商不互通（<<<PAGE 341>>>）。DHL 每交换机一个会话两链路，未映射 VLAN 自动归 linkA（<<<PAGE 380-383>>>）。ERP Guard Timer 必须大于 R-APS 绕环时延否则可能成环（<<<PAGE 396>>>）；MRP 面向工业确定性重构，MRA 投票自动选 MRM（<<<PAGE 426-428>>>）。MST 模式下 LBD 只能开在 STP 禁用接口（<<<PAGE 328>>>）。

### 4. 骨干与 Fabric：SAP/SDP/Service 一次学四处用
SPBM=ISIS-SPB 控制面+MAC-in-MAC 数据面；BEB 学客户 MAC、BCB 只按 BMAC 转发；配置必须先骨干（六步）后服务（三步）（<<<PAGE 211, 245>>>）。SAP/SDP/Service 三件套抽象通用于 SPB/VPLS/VPWS/VXLAN（F5）。VPLS 需 PE 全网格 PW+Split Horizon（<<<PAGE 478>>>）。VXLAN VTEP 由 Loopback0 IP 标识（<<<PAGE 535>>>）。EVPN 用控制面通告 MAC/IP 替代泛洪学习；静态聚合必须手工配 ESI 否则失去多归属（<<<PAGE 587>>>）；部署模型库 Clos-3/5/Collapsed/Multi-site/Multi-PoD（F7）。

### 5. IP/IPv6 服务：VRF 隔离与 DHCP 全栈
`ip interface <name> address <ip> vlan <vid>` 是三层基本模型（<<<PAGE 709>>>）。VRF 分割 L3 实例可复用地址空间，跨 VRF 必须显式 route leak（<<<PAGE 756>>>）。DHCP 全栈（F12）：外部 relay→内部 relay（global/per-interface、Option-82）→Generic UDP Relay→内部 Server→Snooping（L2/L3、绑定表、信任口）→DHCPv6（relay/snooping/RA guard/ISF）。全局 Option-82 与 Snooping 互斥（<<<PAGE 925>>>）。IPsec 仅传输模式；机密性必须 ESP（<<<PAGE 819>>>）。

### 6. 路由基础：VRRP 时序与 BFD 分工
RIP 15 跳上限+120 秒 hold-down，大网不适用（<<<PAGE 842>>>）。VRRP Master_Down=(3×Adv)+Skew、Skew=(256-P)/256；优先级接近会接管抖动（<<<PAGE 980>>>）；IPv4 须先配接口地址才能使能（<<<PAGE 978>>>）。BFD：VRRP/静态路由只用 Echo（单跳），OSPF/IS-IS/BGP 用控制包（可多跳）（<<<PAGE 870>>>）。SLB 以 VIP 或 QoS condition 标识集群，WRR 分发+ping 健康探测（<<<PAGE 1012>>>）。

### 7. 组播：域内交换+域间路由+跨 VLAN 分发
IPMS(IGMP)/IPMSv6(MLD) 管 VLAN/service 域内交换；PIM/DVMRP 建路由库；IPMVLAN/MVR 跨 VLAN 单向分发（F13）。querier 最低 IP 当选（<<<PAGE 1033>>>）。IPMVLAN 模式（企业/Stacking）建后不可改必须删除重建；Stacking 模式仅一个 sender 口（<<<PAGE 1086-1087>>>）。

### 8. QoS 与策略：四步链+三元组+qos apply
分类→拥塞管理→拥塞避免→policing/shaping 四步链（F8）；policy=condition+action+rule，多策略命中取最高 precedence；每口 8 队列；四类策略列表（default/UNP/egress/AFP）。配置后不 `qos apply` 不生效是最常见坑（<<<PAGE 1149>>>）。IPv4/IPv6 条件不能混进同一 condition（<<<PAGE 1135>>>）。802.1Q tagged 口默认 untrusted（<<<PAGE 1134>>>）。SIP snooping 仅 IPv4/UDP、所有初始消息须过同一 trusted server（<<<PAGE 704>>>）。

### 9. 接入安全：认证→分类→角色→隔离
准入框架（F9）：802.1X/MAC/Captive Portal→RADIUS（唯一支持端口准入）→UNP 分类规则→profile（VLAN/service 映射+QoS 列表）→QMR。标准次序：RADIUS→profile→映射→分类→端口→使能→默认 profile（<<<PAGE 1211>>>）。认证服务器不逐台轮询，第一台找不到用户即失败（<<<PAGE 1475>>>）。AppMon（DPI）与 AFP（REGEX）互补（F11）；AFP 默认全局使能但端口全禁用（<<<PAGE 1457>>>）。LPS 不支持聚合口、学习窗口全局（<<<PAGE 1536>>>）。镜像配 unblocked-vlan 防 STP 中断；sFlow 默认 UDP 6343（<<<PAGE 1558, 1561>>>）。

### 10. OAM 与运维：先分层再定位
LINK OAM(802.3ah) 管单链路、Service OAM(802.1ag/Y.1731) 管端到端业务（F14）；MD 分层 0-7 对应组织边界，MEP 发起命令防域间泄漏（<<<PAGE 1655>>>）。EFM 5 秒无 OAMPDU 即失联（<<<PAGE 1674>>>）。Switch Health 资源阈值+采样；日志=级别+输出设备+格式+存储上限（<<<PAGE 1566, 1580>>>）。SAA 以 SPB 会话测量出 XML 历史（<<<PAGE 1700>>>）。PPPoE-IA 全局+端口两级必须同时使能（<<<PAGE 1715>>>）。

## 三、高价值章节页码索引

| 主题 | 页码 |
|---|---|
| 端口参数/风暴控制/流控 | 56-60 |
| 违规恢复统一框架 | 69-71 |
| MACsec（含 WAN） | 83-87 |
| UDLD | 98-99 |
| 静态 MAC/源学习 | 105-108 |
| VLAN/802.1Q/PVLAN | 115-129 |
| HA VLAN 服务器集群 | 140 |
| STP/RSTP/MSTP | 157-205 |
| SPBM 骨干与服务 | 211-280 |
| LBD | 325-329 |
| 静态/动态聚合 | 341-354 |
| DHL | 380-383 |
| ERP/ERPv2 | 395-419 |
| MRP | 426-437 |
| MVRP | 442-447 |
| MPLS/LDP | 453-461 |
| VPLS/VPWS | 478-505 |
| VXLAN 网关 | 533-536 |
| EVPN（含部署模型） | 583-661 |
| SIP Snooping | 704 |
| IP 接口/静态路由/隧道 | 709-721 |
| VRF/Route Leak | 712, 756-759 |
| IPv6/ND/RA 过滤 | 773-777 |
| IPsec | 819-823 |
| RIP/BFD | 842-870 |
| DHCP Relay/Snooping | 902-926 |
| 内部 DHCP Server | 893-894 |
| VRRP/Tracking | 978-993 |
| SLB | 1011-1015 |
| IPMS/IPMSv6 | 1032-1038 |
| IPMVLAN/MVR | 1086-1093 |
| QoS 全体系 | 1103-1176 |
| Policy Servers(LDAP) | 1175 |
| Access Guardian/UNP | 1210-1214 |
| Captive Portal | 1303 |
| L2 GRE 隧道 | 1353 |
| mDNS/SSDP | 1400 |
| AppMon/AFP | 1431-1458 |
| 认证服务器 | 1475-1525 |
| LPS | 1536-1542 |
| 端口镜像/sFlow/RMON/Health | 1558-1567 |
| VLAN Stacking(QinQ) | 1606-1622 |
| 日志 | 1580 |
| Service OAM/CFM | 1650-1665 |
| EFM LINK OAM | 1672-1674 |
| SAA | 1700 |
| PPPoE-IA | 1714-1715 |

## 四、一句话总纲

AOS 8 配置手册是 Quick Steps 驱动的 CLI 底座：先按功能章定位命令序列，再照 Defaults 表对默认值，所有"配了没反应"（qos apply 未提交、两级使能缺一、Option-82 与 Snooping 互斥、依赖功能未开）都靠 Interaction/Limitations 反例清单兜底。
