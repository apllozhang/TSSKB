---
name: AOS 8 二层冗余与保护（STP/聚合/DHL/UDLD/LBD/ERP/MRP）
description: 需要在 OmniSwitch AOS 8 上配置生成树（STP/RSTP/MSTP）、静态/LACP 链路聚合、双归链路 DHL、UDLD 单向链路检测、环回检测 LBD、ERP(G.8032)/MRP 工业环网时使用。
source_book: OmniSwitch AOS Release 8.10R4 Network Configuration Guide
---

## R（触发场景）
- 二层组网要防环：选 STP/RSTP/MSTP 还是环网协议
- 上联带宽不够/单链故障：做链路聚合（静态或 LACP）
- 接入交换机双上联两台核心，要 Active-Active 或 Active-Standby 保护（DHL）
- 光纤单通导致 STP 环路：部署 UDLD
- 接入侧私接小交换机成环：部署 LBD
- 电信以太环网（G.8032 ERP）或工业环网（MRP）保护切换

## I（核心理念）
二层高可靠防环分层选型（F3，<<<PAGE 157>>>/<<<PAGE 395>>>/<<<PAGE 211>>>）：STP/RSTP/MSTP（通用树）→UDLD（单向链路）→LBD（环回）→ERP/MRP（电信/工业环网）→DHL（双归）→SPBM（ISIS 最短路径，见 aos-nc-fabric-backbone）。环网保护双体系（F16，<<<PAGE 395>>>/<<<PAGE 426>>>）：ERP(G.8032，RPL owner+WTR/Guard+R-APS) 面向电信以太，MRP(IEC 62439-2，MRM/MRC/MRA 投票+测试帧) 面向工业环。STP 拓扑计算三步：选根桥（最低桥 ID）→每桥算到根最优路径→阻塞成环节路（P43，<<<PAGE 157>>>）。

## A1（决策框架）
1. **通用防环**：小网 RSTP；多 VLAN 独立路径选 MSTP（VLAN 映射 MSTI，Flat 模式最多 17 实例含 CIST）；per-VLAN 模式是 AOS 私有，跨厂商互通受限（P45/P46/X21，<<<PAGE 164>>>）
2. **带宽/链路冗余**：对端是 OmniSwitch 或支持 LACP 用动态聚合；跨厂商对接慎用静态聚合（X31，<<<PAGE 341>>>）
3. **双上联保护**：两链路分属不同 VLAN 组、要 Active-Active 用 DHL；DHL 会话使能后两链路 STP 自动禁用（P69，<<<PAGE 382>>>）
4. **环网**：电信以太选 ERP（RPL owner+WTR+Guard 定时器）；工业确定性重构选 MRP（MRM/MRC，或 MRA 投票自动选 MRM）（P78/P79，<<<PAGE 426-428>>>）
5. **单向链路**：点对点光纤用 UDLD Aggressive 模式，其他场景 Normal（P22，<<<PAGE 98>>>）

## A2（操作步骤）
- **MST 区域**：`spantree mst region <name>`+revision+VLAN-MSTI 映射（cases·C12，<<<PAGE 202>>>）；单 MSTI 调优：对特定 MSTI 配端口 path cost/priority 使该 MSTI VLAN 走独立路径（cases·C13，<<<PAGE 205>>>）；端口参数（edge port、root guard、限 TCN/BPDU）见章内 Configuring STP Port Parameters（cases·C14，<<<PAGE 189>>>）
- **静态聚合**：`linkagg static agg <id> size n`→`linkagg static port agg <id> port <slot/port>`（两端都要）；验证 show linkagg（cases·C24，<<<PAGE 342>>>）
- **动态 LACP 聚合**：建动态组→成员口 actor 参数（LACP 模式/slow-fast 超时）→partner 参数；验证 show linkagg dynamic（cases·C25，<<<PAGE 354>>>）
- **DHL Active-Active 九步**：`vlan 100-110`→两链路同默认 VLAN untagged→其余 VLAN tagged→`dhl 10`→`dhl 10 pre-emption-time 500`→`dhl 10 mac-flushing mvrp`→`dhl 10 linka linkagg 5 linkb port 1/1/10`→`dhl 10 vlan-map linkb 11-20`→`dhl 10 admin-state enable`（cases·C26，<<<PAGE 383>>>）
- **LBD**：全局 enable→边缘口 enable→（可选）remote-origin enable→transmission timer（默认 30s）→违规口 autorecovery；验证 `show loopback-detection`（cases·C19，<<<PAGE 329>>>）
- **ERP 标准 VLAN 环**：`vlan 1001`+members port tagged→`erp-ring 1 port1 1/1/1 port2 1/1/2 service-vlan 1001 level 1`→`erp-ring 1 rpl-node port 1/1/1`→加保护 VLAN 11-20→`erp-ring 1 enable`→`show erp`（cases·C20，<<<PAGE 403>>>）
- **MRP 环**：配 MRM（含测试帧周期）与 MRC 角色、冗余域；MRA 自动选举替代手工指定（cases·C23，<<<PAGE 437>>>）
- **UDLD**：Normal 模式仅显式证据关停、未确定标记 Undetermined；Aggressive 超时即关端（P22，<<<PAGE 98>>>）；机制为邻居数据库+echo detection 窗口（P23，<<<PAGE 99>>>）

## E（实证案例）
- per-VLAN RSTP 四交换样例（C11，<<<PAGE 197>>>）
- DHL Active-Active 九步（C26，<<<PAGE 383>>>）
- ERP 标准 VLAN 环（C20，<<<PAGE 403>>>）；ERP+VLAN Stacking（C21，<<<PAGE 403>>>）
- ERPv2 主环+子环+共享链路（C22，<<<PAGE 419>>>）

## B（反例/坑）
- MST 模式下 LBD 只能开在 STP 禁用的接口上；LBD 帧不打 tag 发送（P61/X28，<<<PAGE 328>>>）
- 聚合组任一成员口环回，整组 shutdown（X29，<<<PAGE 328>>>）；remote-origin LBD 双端都开时结果不确定（X30，<<<PAGE 327>>>）
- 聚合组成员必须同速，混速无法成组；负载分担非 IP 按 MAC、IP 报文按 IP 地址（X32/P64，<<<PAGE 341>>>）
- 静态聚合不能与部分厂商设备对接（X31，<<<PAGE 341>>>）
- DHL：未同时挂到 linkA/linkB 的 VLAN 不受保护；每交换机仅一个会话、每会话仅两链路；VLAN 数≤128/组；raw flooding 的 MAC≤1000（X33/X34，<<<PAGE 382>>>）；未映射到 linkB 的 VLAN 自动归 linkA（P70，<<<PAGE 383>>>）
- ERP Guard Timer 必须大于 R-APS 绕环最大时延，否则可能成环（X35/P75，<<<PAGE 396>>>）
- ERPv2 子环不能使用共享链路；共享链路只能属于一个主环（X36，<<<PAGE 395>>>）
- MSTP 仅 Flat 模式支持；MSTI 端口状态由 CST 统一算，不调 path cost 无法让单实例独立转发（X23/P47，<<<PAGE 164>>>）
- MSTP 恢复流程要点：恢复侧发 R-APS(NR) 并启 Guard→RPL owner 启 WTR→超时阻塞 RPL 并发 R-APS(NR,RB)→各节点 flush MAC 回 idle（P74，<<<PAGE 398>>>）

## 来源
OmniSwitch AOS 8.10R4 Network Configuration Guide 第 2 章 UDLD（<<<PAGE 98-99>>>）、第 6 章 Spanning Tree（<<<PAGE 157-205>>>）、第 8 章 LBD（<<<PAGE 325-329>>>）、第 9/10 章链路聚合（<<<PAGE 341-354>>>）、第 11 章 DHL（<<<PAGE 380-383>>>）、第 12 章 ERP（<<<PAGE 395-419>>>）、第 13 章 MRP（<<<PAGE 426-437>>>）。条目来源：cases C11-C14/C19-C26；principles P21-P24/P42-P48/P58-P70/P72-P82；counter-examples X21-X23/X28-X36；frameworks F3/F16。
