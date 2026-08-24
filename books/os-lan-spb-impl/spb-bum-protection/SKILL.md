---
name: spb-bum-protection
description: 何时用：选配 BUM 组播分发模式、开 IPMS 抑制泛洪、部署 LBD 防接入环路、overload 维护引流时。
source_book: DT00XTE323EN SPB Concepts & Implementation
---

# BUM 组播与接入保护（三模式 / LBD / Overload）

## R · 原文引用

> "SPBM supports two BUM traffic distribution methods for replicating and forwarding multicast frames • Head-End (native mode) • Tandem (optimized)" (p138-141；Head-End 为默认，入口 BEB 按对端单播 B-MAC 逐份复制)

> "Periodically sends out frames from all loopback detection enabled ports • Based on specific multicast frames D-MAC: ALU proprietary MAC 0x01-20-DA-02-01-71... Actions: Port shutdown / Trap / Event log / Port recovery: Automatically after a configurable timer or manually. Global LBD Transmission Timer : 10 sec, Global LBD Auto-recovery Timer : 300 sec" (p120)

> "The Overload state mechanism allows ISIS-SPB to inform its neighbors that the ISIS instance is nearing or exceeding its capabilities. When peers see that a switch is advertising in this state, they will select an alternate path around the overloaded switch." (p130)

## I · 方法论骨架

1. **BUM 三模式选型**（f09）：Head-End（默认，稀疏场景省资源）→ Tandem S,G（每 I-SID 每源建树，带宽效率高）→ Tandem *,G（每 BVLAN 共享一棵树，资源最省）。
2. **配置层级**（p15）：`service spb [X|all] multicast-mode {head-end|tandem}` 逐服务或全局；tandem 子模式逐 BVLAN 配 `spb isis bvlan N tandem-multicast-mode {sgmode|gmode}`；同一 BVLAN 全网必须同模式。
3. **IPMS 逐服务显式启用**（p17）：不开则组播无差别泛洪到全部 SAP/SDP。
4. **LBD 三件套**（p12）：全局 enable → 端口 enable → show statistics；封口裁决可预判（ce04）。
5. **Overload 两用法**（p14）：维护引流（`spb isis overload timeout N`）与开机保护（`overload-on-boot`）。

## A1 · 书中案例（Lab 配置序列精要）

Lab3 保护实验组合（c03，p127-132）：
```
! metric 引流（两端同步）
spb isis interface port 1/1/6 metric 40
! overload 软隔离
spb isis overload timeout 120
! 环路检测
loopback-detection enable
loopback-detection service-access port 1/1/3 enable
! L2 Profile
service l2profile Drop-GVRP GVRP drop
service access port 1/1/3 l2profile Drop-GVRP
```
人为环路故障模型（ce14，p131）：Sw8 增 SAP 1/1/4:2 + Sw5 tag VLAN2 并行口 + `spantree vlan 2 admin-state disable` → Client5 MAC 在 Sw7/Sw8 双侧漂移、ping 中断；随后 LBD 自动 shutdown 环路口恢复。

## A2 · 触发场景（含与相邻 skill 的区分）

- 组播流量大要优化复制、ARP/DHCP 泛洪要抑制、接入口可能成环、核心要下电维护先引流时用本 skill。
- 与 `spb-backbone-deploy` 的区分：metric/ECT 选路调优归骨干 skill，本 skill 管 BUM 复制与环路防护；与 `spb-access-ring-redundancy` 的区分：DHL/ERP 是双上联的成套冗余方案，LBD 是兜底检测——教材实验里 LBD 用在无冗余方案的并行路径上；与 `spb-oam-troubleshoot` 的区分：本 skill 是预防性配置，连通性验证（mac-ping/SAA）归 OAM。

## E · 可执行步骤

1. 评估组播规模：稀疏/低带宽保持默认 head-end；高带宽组播改 tandem 并逐 BVLAN 选 sgmode/gmode。
2. 开 IPMS：`ip multicast service <svc> admin-state enable`（逐服务，两端 BEB 都要）。
3. 部署 LBD：全局 `loopback-detection enable` → 接入口 `loopback-detection service access port <p> enable` → `show loopback-detection statistics port <p>`。
4. 维护前引流：路径外节点无关，路径上的核心执行 `spb isis overload timeout 120`，permanent ping 验证无感切换。
5. 排查组播路径：`show spb isis multicast-table`，按组 B-MAC 反推源节点与 I-SID（p16 编码规则）。

## B · 边界与陷阱

- **LBD 在 linkagg 上封整组**（ce03）：任一成员口成环，整个聚合组 shutdown；评估故障面与 300 秒自动恢复是否可接受。
- **LBD 封口裁决规则**（ce04）：跨机关较高 BridgeID 那台的口，同机关较高 PortID 的口——预判被封口，别误判设备故障。
- **接入层并行双路径无 STP/LBD 兜底必成环**（ce14）：SPB 骨干无环不等于接入无环；生产双上联必须配 DHL/ERP/LBD 之一。
- 组播组 B-MAC 目标不能作为 mac-ping 目标（见 OAM skill）；组播路径用 multicast-table 查。
- tandem 模式全网同 BVLAN 必须一致，混配会异常（p15）。

---
来源条目: f09, p12, p14, p15, p16, p17, c03, ce03, ce04, ce14, g06, g17, g23, g35, g36
