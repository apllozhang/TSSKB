# frameworks — 体系框架（OmniSwitch AOS 8.10R4）

格式：编号 F# ｜ 框架名 ｜ 结构与运用 ｜ 页码

- **F1** AOS 配置手册统一章法（Defaults→Quick Steps→Overview→Configuring→Example→Verifying）：所有功能章都按此骨架组织，排障与学习时可按固定小节定位；"Quick Steps" 与 "Application Example" 提供可复制流程，"Interaction With Other Features" 提示跨功能约束。<<<PAGE 1>>>（全书体例）
- **F2** 违规关停与恢复统一框架（Violation Recovery）：各特性（STP/QoS/LPS/UDLD/NetSec/NI/LLDP/LinkMon/LFP/RFP）共用一套 shutdown/recovery/trap 机制，分 Discard 与 Admin-Down 两类；排障先查 `show violation` 而非逐特性查。 <<<PAGE 69>>>
- **F3** 二层高可靠防环体系：STP/RSTP/MSTP（通用树）→ UDLD（单向链路）→ LBD（环回）→ ERP/MRP（电信/工业环网）→ DHL（双归）→ SPBM（ISIS 最短路径），按场景分层选型。<<<PAGE 157>>>/<<<PAGE 395>>>/<<<PAGE 211>>>
- **F4** SPBM 双平面框架：控制面 ISIS-SPB（ECT 对称最短路径树+控制面 MAC 学习）+ 数据面 802.1ah MAC-in-MAC（BEB 封装、BCB 按 BMAP 转发）；服务模型=BVLAN 承载多 I-SID，SAP 定义接入分类。 <<<PAGE 211>>>
- **F5** 服务模型三件套（SAP/SDP/Service）：SPB、VPLS、VPWS、VXLAN 共用"接入点 SAP+隧道分发点 SDP+服务实例"抽象，学会一次即可迁移到四种 VPN。 <<<PAGE 212>>>/<<<PAGE 478>>>/<<<PAGE 533>>>
- **F6** EVPN 控制面框架：MP-BGP EVPN 地址族（RT1-8 分工：AD/主机/含组播/ES/前缀/选择性组播）+ ES/ESI 多归属（DF 选举、别名、水平分割）+ VRF tenancy（非对称/对称 IRB、fabric-vpn、DAG、OISM）。 <<<PAGE 583>>>
- **F7** 数据中心叠加网络部署模型库：Clos-3/Collapsed Core/Clos-5/Multi-site/Multi-PoD，配 RR 冗余与 underlay 建议，形成可复用的拓扑-配置映射。 <<<PAGE 654>>>（18-76 页）
- **F8** QoS 四步处理链（分类→拥塞管理→拥塞避免→ policing/shaping）+ 策略三元组（condition/action/rule）+ 四类列表（default/UNP/egress/AFP）+ 条件组/map group/ACL 扩展。 <<<PAGE 1103>>>/<<<PAGE 1133>>>
- **F9** 网络准入框架（Access Guardian）：认证（802.1X/MAC/Captive Portal→RADIUS/UPAM/CPPM）→分类（UNP 规则/端口默认）→角色（profile：VLAN/service 映射+QoS 列表）→限制/隔离（QMR 隔离修复）；BYOD（mDNS/SSDP）与 IoT profiling 是外延。 <<<PAGE 1212>>>
- **F10** AAA 服务器选型矩阵：RADIUS（管理+准入）/TACACS+（管理含 SNMP）/LDAP（管理含 SNMP）+备份服务器策略+授权回落本地库。 <<<PAGE 1475>>>
- **F11** 应用感知框架：AppMon（DPI 签名+应用列表+QoS 执行）与 AFP（REGEX 指纹+分类器库+trap/UNP 列表）互补，前者面向 OVNG DPI 生态、后者面向服务器侧端口。 <<<PAGE 1431>>>/<<<PAGE 1457>>>
- **F12** DHCP 全栈框架：外部 relay（路由器）→内部 relay（global/per-interface、Option-82）→Generic UDP Relay→内部 DHCP Server（policy/配置/数据库文件）→Snooping（L2/L3、绑定表、信任口）→DHCPv6（relay/snooping/RA guard/ISF）。 <<<PAGE 903>>>/<<<PAGE 925>>>
- **F13** 组播分发框架：IPMS(IGMP)/IPMSv6(MLD) 做 VLAN/service 域内组播交换，PIM/DVMRP 做域间路由，IPMVLAN/MVR 做跨 VLAN 单向分发，EVPN RT6-8/OISM 做叠加层优化。 <<<PAGE 1032>>>/<<<PAGE 1086>>>
- **F14** OAM 分层框架：LINK OAM(802.3ah，单链路发现/监控/环回) 与 Service OAM(802.1ag/Y.1731，MD/MA/MEP 层级+CC/LB/LT+时延测量) 互补，CFM MD 分层 0-7 对应运营商/客户组织边界。 <<<PAGE 1655>>>
- **F15** 可观测性框架：端口镜像/端口监控（抓包面）+ sFlow（采样流量统计）+ RMON（探针）+ Switch Health（资源阈值）+ 日志/健康监测组合成完整诊断工具箱。 <<<PAGE 1558>>>/<<<PAGE 1561>>>
- **F16** 环网保护双体系：ERP(G.8032，RPL owner+WTR/Guard+R-APS) 面向电信以太，MRP(IEC 62439-2，MRM/MRC/MRA 投票+测试帧) 面向工业环；ERPv2 扩展多环/子环/共享链路。 <<<PAGE 395>>>/<<<PAGE 426>>>
- **F17** VLAN 演进框架：标准 VLAN→802.1Q trunk→PVLAN（子域隔离）→VLAN Stacking/QinQ（运营商隧道）→VXLAN/EVI（数据中心叠加）→EVPN（控制面化），按规模与隔离需求逐级选用。 <<<PAGE 115>>>/<<<PAGE 1606>>>/<<<PAGE 583>>>
- **F18** 安全接入纵深框架：端口级（LPS/端口安全/风暴控制/过滤 MAC）→链路级（MACsec）→网络级（IPsec/DoS 过滤/IPv6 DoS）→身份级（AG/UNP/Captive Portal/Quarantine）四层递进。 <<<PAGE 83>>>/<<<PAGE 1536>>>/<<<PAGE 819>>>/<<<PAGE 1212>>>

---
合计：18 条（F1-F18）。
