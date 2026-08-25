---
name: AOS 8 VLAN 与二层域（VLAN/PVLAN/QinQ/MVRP）
description: 需要在 OmniSwitch AOS 8 上创建/打标 VLAN、部署 Private VLAN、配置 VLAN Stacking(QinQ)/ethernet-service、HA VLAN 服务器集群、用 MVRP 动态注册 VLAN 时使用。
source_book: OmniSwitch AOS Release 8.10R4 Network Configuration Guide
---

## R（触发场景）
- 新建业务 VLAN、把端口按 tagged/untagged 接入，或跨交换机单链多 VLAN
- 同一 VLAN 内要把部分用户彼此隔开（PVLAN isolated/community）
- 运营商/城域场景：客户流量打外层 SVLAN 透明穿越（VLAN Stacking/QinQ、ethernet-service）
- 服务器集群要一个虚 MAC 对多条链路收流量（HA VLAN）
- 互联口上希望 VLAN 成员随对端自动声明/撤销（MVRP），不想手工配两边 trunk

## I（核心理念）
VLAN 演进框架（F17，<<<PAGE 115>>>/<<<PAGE 1606>>>/<<<PAGE 583>>>）：标准 VLAN→802.1Q trunk→PVLAN（子域隔离）→VLAN Stacking/QinQ（运营商隧道）→VXLAN/EVI（数据中心叠加）→EVPN（控制面化），按规模与隔离需求逐级选用。基本模型：端口只能属于一个 untagged VLAN（默认 VLAN）+任意多个 tagged VLAN；VLAN 在有活动端口前 oper 状态一直是 inactive（P31/P34，<<<PAGE 115, 118>>>）。QinQ 的隧道 ID 与 VLAN ID 一一对应，"tunnel and VLAN are interchangeable terms"（P192，<<<PAGE 1608>>>）。MVRP 是 MRP 应用，动态声明/撤销 VLAN 成员，学到的动态 VLAN 所有端口都是 tagged（P83/P84，<<<PAGE 442>>>）。

## A1（决策框架）
1. **普通隔离选标准 VLAN + 802.1Q**：单链多 VLAN 用 tagged 口（P32/P33：入向分类规则，带 tag 必须匹配端口默认 VLAN 或已打标 VLAN 否则丢弃，<<<PAGE 118>>>）
2. **VLAN 内二次隔离选 PVLAN**：主 VLAN+isolated（彼此隔离）/community（互通）二级 VLAN；上联走 promiscuous 口、跨交换机延伸走 ISL 口（<<<PAGE 128>>>）
3. **客户流量透明穿越选 VLAN Stacking**：double tagging（外插 SVLAN）或 VLAN translation（替换 CVLAN），NNI/UNI 分角色（P191/P193，<<<PAGE 1606, 1608>>>）
4. **服务器冗余选 HA VLAN**：把发往单一目的 MAC 的流量复制到多端口；L2 用静态 MAC、L3 用静态 ARP（P39/P40，<<<PAGE 140>>>）
5. **动态 VLAN 注册选 MVRP**：注意仅支持 STP Flat 模式，与 per-VLAN 模式互斥（P86，<<<PAGE 444>>>）

## A2（操作步骤）
- **VLAN 创建与成员**：`vlan 755 name "IP Finance Network"`、`vlan 10-15` 批量、`vlan 5 members port 1/4/3 tagged`、`vlan 755 members linkagg 10 untagged`、`no vlan 200`；验证 `show vlan port`（cases·C7，<<<PAGE 116>>>）
- **跨交换机 trunk**：互联口对 VLAN1 untagged、VLAN2/3 tagged，单链多 VLAN（cases·C8，<<<PAGE 118>>>）
- **PVLAN**：建 Primary VLAN→建 isolated/community 二级 VLAN 关联主 VLAN→配 promiscuous/ISL 口→二级 VLAN 关联用户口；验证 `show pvlan`/`show pvlan mapping`/`show pvlan members`（cases·C9，<<<PAGE 128>>>）。主 VLAN 的 admin/STP/IP 接口配置自动作用于全部二级 VLAN（P38，<<<PAGE 129>>>）
- **HA VLAN 集群**：建 VLAN→加入集群口→分配 cluster 模式→配虚 MAC（L2 静态 MAC、L3 静态 ARP，可加 IGMP 组播地址）；验证 show HA VLAN status（cases·C10，<<<PAGE 140>>>）
- **VLAN Stacking 服务**：`ethernet-service svlan <id>`→`ethernet-service service-name CustomerA svlan <id>`→NNI 口（`ethernet-service nni port ...`）→SAP/UNI 口封装→UNI profile（cases·C61，<<<PAGE 1622>>>）
- **MVRP**：全局/端口使能，applicant 声明模式（normal/active）、registrar 模式（fixed/forbidden/normal）、Join/Leave 定时器（<<<PAGE 442-447>>>）

## E（实证案例）
- VLAN 创建与打标成员（C7，<<<PAGE 116>>>）
- PVLAN 完整部署与验证（C9，<<<PAGE 128>>>）
- ERP+VLAN Stacking 组合（C21，<<<PAGE 403>>>，详见 aos-nc-redundancy-protection）
- VLAN Stacking 服务五步（C61，<<<PAGE 1622>>>）

## B（反例/坑）
- 删除 VLAN 连带删路由接口和全部 VPA；默认 VLAN 被删则端口回落 VLAN 1——误删业务风险（X15，<<<PAGE 116>>>）
- 带 802.1Q tag 的包若 VID 既非端口默认 VLAN 又非该口 tagged VLAN，直接丢弃（X17，<<<PAGE 118>>>）
- NNI 口 TPID 非 0x8100 时不允许再打普通 802.1q tag（X18，<<<PAGE 119>>>）
- PVLAN：主 VLAN VID 不能与现存 VLAN 冲突；UNP 口只能属一个 PVLAN 域；IP 接口只能配在主 VLAN 上（X19，<<<PAGE 129>>>）
- HA VLAN 一旦成型，标准 VLAN 命令失效（X20，<<<PAGE 140>>>）
- MVRP 与 per-VLAN STP 互斥；MVRP 配置后 STP 模式不能再改成 per-VLAN（X22，<<<PAGE 444>>>）
- 动态 VLAN 由 MVRP 学到的 VPA 在拓扑变化时一并删除（P86，<<<PAGE 444>>>）
- 转发声明≠加入：端口转发从其他口学到的声明，但只有本口收到声明才加入该 VLAN（P85，<<<PAGE 442>>>）

## 来源
OmniSwitch AOS 8.10R4 Network Configuration Guide 第 4 章 VLAN（<<<PAGE 115-129>>>）、第 5 章 HA VLAN（<<<PAGE 140>>>）、第 14 章 MVRP（<<<PAGE 442-447>>>）、第 42 章 VLAN Stacking（<<<PAGE 1606-1622>>>）。条目来源：cases C7/C8/C9/C10/C61；principles P30-P41/P83-P86/P191-P193；counter-examples X15-X20/X22；frameworks F17。
