# DIGEST · OmniSwitch AOS Release 8.10R04 CLI Reference User Guide

- 源文件：`Omniswitch AOS Release 810R04 CLI Reference User Guide.pdf`（6240 页，70 个命令章，约 2480 条命令）
- 定位：**命令字典，怎么查怎么用**。全书按功能章组织，每条命令给语法/参数/默认值/平台支持/示例。蒸馏策略为"命令地图"——不做全量摘录，而是把 70 章归入 5 个命令域技能，每个技能给出章→页码区间导航 + 代表命令语义，需要细节时按页码回查原书。
- 全书最大两章：Access Guardian（第 42 章，约 199 条，p4470）与 BGP（第 31 章，约 194 条，p2744）

## 五个命令域技能

| 技能 | 域 | 覆盖章 | 起始页 |
|---|---|---|---|
| aos-cli-map-l2-access | L2 接入域 | 第 1-8/12-17/20 章（端口/PoE/UDLD/MAC/VLAN/HAVLAN/QinQ/DSTP/LBD/聚合/VC/ERP/MRP/MVRP/Auto-Fabric） | p67 |
| aos-cli-map-fabric | Fabric 骨干域 | 第 9-11 章（MPLS/SPB/Service Manager） | p689 |
| aos-cli-map-routing | 路由域 | 第 21-32 章（IP/IPv6/IPsec/RIP/BFD/DHCP/VRRP/OSPF/OSPFv3/IS-IS/BGP/SLB） | p1549 |
| aos-cli-map-multicast-qos | 组播/QoS/策略/准入域 | 第 33-44/49/58 章（组播/QoS/PolicyServer/AAA/AG/AppMon/AFP/LPS/PPPoE-IA） | p3227 |
| aos-cli-map-mgmt-oam | 管理与 OAM 域 | 第 18-19/45-48/50-70 章（LLDP/监测/日志/健康/OAM/CMM/NTP/会话/文件/SNMP/Cirrus/OpenFlow/DNS 及 FCoE/VXLAN 散章） | p1390 |

## 使用方法

1. 先按功能域定位技能 → 技能 A2 段的章节清单找到章号与页码区间
2. 回查原书对应章的目录（或本书 GLOSSARY 70 章速查）定位具体命令
3. 平台限定先看技能 B 段（如 6360/6465 不支持 SPB/OSPF/BGP 等）

## 关键页码速查

- About/平台支持说明：p59-66
- CLI Quick Reference（按字母序命令索引）：p6184
- Index：p6236

一句话总纲：**先域后章再命令，平台限定提前查，默认值在原文。**
