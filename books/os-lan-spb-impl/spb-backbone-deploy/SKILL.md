---
name: spb-backbone-deploy
description: 何时用：从零搭建或验收 SPB 骨干（BVLAN/ECT/IS-IS/BCB-BEB 拓扑设计与四步部署）时。
source_book: DT00XTE323EN SPB Concepts & Implementation
---

# SPB 骨干部署与拓扑设计（BVLAN / ECT / IS-IS）

## R · 原文引用

> "Backbone configuration entails the following tasks: Creating one or more BVLANs with their associated ECT-IDs... Defining the control BVLAN; Defining one or more SPB IS-IS interfaces; Enabling the SPB IS-IS protocol" (p83)

> "BVLAN configuration and ECT algorithm assignment must match on each SPB bridge to ensure proper ISIS-SPB neighbour discovery and shortest path calculations throughout the backbone SPB network. When creating multiple BVLANs for each node, it is best practice to use different ECT algorithm for each BVLAN to maximize the traffic distribution." (p83)

> "SPB DESIGN TWO-TIER TOPOLOGY — Core Switch: No need for BCB nodes; Backbone edge bridge (BEB) role; BEB nodes in partial or full mesh topology... Redundancy achieved through BEB nodes made of two or more physical chassis in VC topology. Access Switch: 802.1Q VLAN on LAG; STP or DHL towards BEB." (p61；三层设计见 p62：BCB 居核心只学 B-MAC，BEB 做汇聚)

> "SPB: Main use case Datacenter, Campus, IoT Networks; Scalability Large; Ease of deployment Simple to Moderate; Protocol Overhead Low — IS-IS only; Troubleshooting Simple & Fast." (p31 选型矩阵；p33：MPLS 收敛 50ms/成本 $$$，SPB 收敛 100ms/成本 $$)

## I · 方法论骨架

1. **职责分层**（f01）：控制面（BVLAN + IS-IS + NNI 口）配在 BEB 与 BCB；数据面（access 口 + SAP）只配在 BEB。BCB 永不感知服务。
2. **拓扑选型**（f06）：小网两层——BEB 全互联，无需 BCB，冗余靠 VC 双机；大网三层——BCB 居核心，BEB 做汇聚，冗余靠双 BCB。
3. **路径选优三级序**（p05）：metric 低者优先 → 跳数少者优先 → ECT 平局裁决；两侧 metric 不一致取最大值（p06）。
4. **部署四步**（f02）：建 BVLAN（含 ECT）→ 定控制 BVLAN → 配 IS-IS 接口 → 全局启用 IS-IS。
5. **带内管理**（p32）：控制 BVLAN 上挂 IP 接口，ISIS-SPB 直接通告路由并做 MAC-IP 映射（免 ARP）。

## A1 · 书中案例（Lab 配置序列精要）

Lab1 骨干从零部署（c01，p83，每节点执行）：
```
spb bvlan 2000
spb isis bvlan 2000 ect-id 1
spb bvlan 2001
spb isis bvlan 2001 ect-id 2
spb bvlan 2002
spb isis bvlan 2002 ect-id 3
spb isis admin-state disable
spb isis control-bvlan 2000
spb isis interface port 1/1/5-6
spb isis interface port 1/1/25
interface port 1/1/5-6 admin-state enable
spb isis admin-state enable
```
带内管理三件套（p67）：`spb isis control-bvlan 4001` → `ip interface "spb-mgmt" address 172.30.1.1/24 vlan 4001` → 出域用静态路由或 `ip redist <ospf> into spb-mgmt` 双向重分发。

## A2 · 触发场景（含与相邻 skill 的区分）

- 新建 SPB 网、扩骨干节点、改路径代价、规划 BVLAN/ECT 编号时用本 skill。
- 与 `spb-l2-service` 的区分：本 skill 只管骨干可达（B-MAC 层），不碰 VLAN/SAP/客户业务；与 `spb-oam-troubleshoot` 的区分：本 skill 是"配"，排障命令链的完整用法归 OAM skill。

## E · 可执行步骤

1. 定拓扑：估规模，小网两层（BEB 互联）或大网三层（引入 BCB）。
2. 规划 BVLAN：≤16 个，每 BVLAN 不同 ECT-ID（如 2000/ect1、2001/ect2、2002/ect3），控制 BVLAN 单独一个。
3. 每节点执行 f02 四步命令序列（见 A1）。
4. 启用后按 f04 验证链自底向上检查：`show spb isis bvlans` → `interface` → `adjacency` → `info` → `unicast-table bvlan X` → `spf bvlan X` → `database`/`nodes`。
5. 配控制 BVLAN 带内管理 IP（为后续 OV2500 纳管铺路）。
6. 调路径：两端同步改 `spb isis interface port X metric N`（默认 10），改完看 `show spb isis spf`，做完两端同步恢复。

## B · 边界与陷阱

- **控制 BVLAN 只能在协议禁用时改**（ce01）：改不动先查 `spb isis admin-state` 是否 enable；正确顺序 disable → 改 → enable。
- **BVLAN 自动禁 STP、不学客户 MAC、不泛洪**（p01/p03）：别指望 STP 在骨干做环保护。
- **metric 单侧降级行不通**（ce02）：一侧 10 一侧 40 时按 40 算整条链路；引流必须两端同步改。
- BVLAN/ECT 指派全网必须一致（p02），否则邻居发现与 SPF 异常。
- IS-IS 开机自动加载，无需 `ip load`（g01）；接口默认 metric 10、Hello 9s×3（p28）。

---
来源条目: f01, f02, f05, f06, p01, p02, p03, p04, p05, p06, p28, p32, c01, ce01, ce02, g01, g02, g03, g04, g05, g07, g08, g14, g20, g25, g26, g28
