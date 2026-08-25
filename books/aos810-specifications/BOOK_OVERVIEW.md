# OmniSwitch AOS Release 8 Specifications Guide — 全书概览

- 书名：OmniSwitch AOS Release 8 Specifications Guide（8.10R4）
- 出版：ALE，2025-12，Part No. 060972-00 Rev. A
- 页数：98 页（fulltext.md 页码标记 `<<<PAGE N>>>`；正文页码形如 1-3/2-5/3-6/4-3）
- 性质：规格速查手册——按"特性 × 13 平台"矩阵给出最大值/支持项/RFC 清单，不含配置与 CLI（原书自述："This guide is designed to provide feature specification information only"）

## 章节结构与蒸馏重点

| 章 | 内容 | fulltext 页 | 蒸馏重点 |
|---|---|---|---|
| 前言 | About This Guide / Documentation Roadmap | 7-11 | 文档地图：首次使用→硬件指南+RN，基础→Switch Mgmt，入网→Net Config/Adv Routing，随时→CLI Reference |
| 1 | Switch Management Specifications | 12-26 | 各机型镜像文件名、会话数（Telnet 6/SSH 8/HTTP 4）、内存/Flash、USB 救援镜像、SNMP v1/v2/v3、VC 规格（成员数/VFL）、自动远程配置、NTP |
| 2 | Network Configuration Specifications | 27-76 | 以太网帧长（1553/9216）、MAC 容量（SM/RM/ER 三模式）、VLAN/PVLAN、STP、SPB（I-SID/BVLAN/SAP）、聚合、ERP、VXLAN/EVPN、IP/IPv6/VRF、IPsec、RIP/BFD、DHCP 全家、VRRP/SLB/IPMS(v6)、QoS、UNP/AG/AppMon、镜像/监控/sFlow/RMON/Health、VLAN Stacking、OAM、SAA、MRP |
| 3 | Advanced Routing Specifications | 77-86 | OSPF(v2/v3)/IS-IS/BGP 各平台区域·接口·LSDB·路由规模；组播边界/DVMRP/PIM/MBR |
| 4 | TCAM Profiles | 87-92 | 6870（Default/Metro/QoS ACL/IPv6 ACL/Bidir IPv6 ACL）、6570M（Default/Fabric）、6575（Default/Fabric/IPv6 ACL）三组 TCAM 资源分配表 |
| 附录 | License / FOSS | 95-98 | 法律条款，无技术蒸馏价值 |

## 蒸馏策略（本书特调）

- **glossary/principles 是主体**：把矩阵中的关键规格行提炼成"平台规模档位"条目（MAC/路由/ARP 的 SM·RM·ER、I-SID、UNP 用户、QoS 规则等）
- **counter-examples 收容量限制与不兼容**：各平台硬上限、VC 混搭限制、链路聚合 ID 保留、"不支持"矩阵项
- **frameworks**：文档地图、TCAM profile 机制、VC 规格"整机上限"语义
- **cases 为 0**：全书为纯规格表格，无任何配置流程，故 candidates/cases.md 不创建（按任务约定在报告中说明）
