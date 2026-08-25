---
name: AOS 8 IP 组播（IPMS/IPMSv6/PIM/组播 VLAN/MVR）
description: 需要在 OmniSwitch AOS 8 上配置二层组播交换 IPMS/IPMSv6（IGMP/MLD）、组播路由交互（PIM/DVMRP/IPMSR）、组播 VLAN（IPMVLAN/MVR，企业或 VLAN Stacking 模式）时使用。
source_book: OmniSwitch AOS Release 8.10R4 Network Configuration Guide
---

## R（触发场景）
- VLAN 内 IPTV/视频会议流量要不泛洪、按成员精确复制：IPMS（IGMP snooping）
- IPv6 组播环境：IPMSv6（MLD snooping）
- 跨网段组播源：组播路由（PIM-SM/DM、DVMRP）与 IPMSR 交互
- 多个用户 VLAN 共享一个组播 VLAN 做单向分发（MVR/IPMVLAN）

## I（核心理念）
组播分发框架（F13，<<<PAGE 1032>>>/<<<PAGE 1086>>>）：IPMS(IGMP)/IPMSv6(MLD) 做 VLAN/service 域内组播交换，PIM/DVMRP 做域间路由，IPMVLAN/MVR 做跨 VLAN 单向分发，EVPN RT6-8/OISM 做叠加层优化。组播组地址为 D 类 224.0.0.0-239.255.255.255，239/8 为管理域（P148，<<<PAGE 1032>>>）。多个组播路由器共存时最低 IP 者当选 IGMP querier（P150，<<<PAGE 1033>>>）。组播路由协议建立组播路由库，IPMS 依其决策+端口成员请求转发（P151，<<<PAGE 1033>>>）。

## A1（决策框架）
1. **域内组播交换选 IPMS/IPMSv6**：IGMP 版本（v1-3）按客户端与源端能力选；querier 可静态指定；静态组用于不发 report 的接收者
2. **跨域组播选路由交互**：PIM-SM/DM 或 DVMRP 建路由库，IPMSR=IPMS+组播路由组合
3. **跨 VLAN 分发选 IPMVLAN**：普通接入口用 Enterprise 模式；QinQ/运营商口用 VLAN Stacking 模式——模式建后不可改，必须删除重建（X58，<<<PAGE 1086>>>）
4. **叠加层（EVPN）组播优化**：RT3 ingress replication / RT6-8 选择性组播 / OISM，详见 aos-nc-fabric-backbone

## A2（操作步骤）
- **IPMS**：全局使能→IGMP 版本/静态 querier/静态组→query interval/robustness 等参数；IPMSv6 对应 MLD 系列；验证 show ipms / ipmsv6（cases·C49，<<<PAGE 1038>>>）
- **IPMVLAN（MVR）**：`ipmvlan <id>` 使能→分配 IPv4/IPv6 地址→sender 口（NNI，仅 1 个）→receiver 口/CVLAN 关联→静态 IGMP 组；验证 show ipmvlan（cases·C50，<<<PAGE 1093>>>）
- **组播路由交互**：PIM/DVMRP 配置见原书第 31 章（本书 verified 以 IPMS/IPMVLAN 为主，PIM 细节建议结合 Advanced Routing 手册）

## E（实证案例）
- IPMS 全局使能+IGMP 参数+静态组（C49，<<<PAGE 1038>>>）
- IPMVLAN sender/receiver 分发（C50，<<<PAGE 1093>>>）

## B（反例/坑）
- IPMVLAN 模式（企业/Stacking）建后不可改，必须删除重建（X58，<<<PAGE 1086>>>）
- Stacking 模式 IPMVLAN 仅允许一个 sender 口；IP 与 CVLAN-tag 两种绑定方式不要同时用（X59，<<<PAGE 1087>>>）
- sender 口是 NNI 且唯一，receiver 口才面向用户；模式选错只能推倒重来
- IGMP querier 最低 IP 当选；多路由器共存时注意 querier 漂移对转发表的影响（P150，<<<PAGE 1033>>>）

## 来源
OmniSwitch AOS 8.10R4 Network Configuration Guide 第 31 章 IP Multicast Switching（<<<PAGE 1032-1038>>>）、第 32 章 IP Multicast VLAN（<<<PAGE 1086-1093>>>）。条目来源：cases C49/C50；principles P148-P151；counter-examples X58/X59；frameworks F13。
