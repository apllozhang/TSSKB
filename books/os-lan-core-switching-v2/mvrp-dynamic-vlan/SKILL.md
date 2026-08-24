---
name: MVRP 动态 VLAN 注册
description: 需要让 VLAN 成员信息跨交换网自动传播（免手工逐台打 tagged 口）时使用本技能。
source_book: DT00XTE216 OmniSwitch LAN Core Switching Ed15
---

## R（触发场景）
- VLAN 数量多、变更频繁，手工在每台上行口打 tagged 维护成本高
- 需要限制动态 VLAN 规模或控制端口注册行为（fixed/forbidden）
- 动态 VLAN 删除报错、MVRP 与 MSTP/IP 接口配合出现疑问

## I（核心理念）
MVRP（802.1ak）基于 STP 拓扑在桥接网内传播动态 VLAN 注册：一个 PDU 携带端口全部 4094 个 VLAN 状态，拓扑变化时只对受影响 VLAN 重新声明。它只解决二层连通——动态 VLAN 不建 IP 接口、不映射 MSTI，L3 和生成树负载分担要手工补配。

## A1（行动框架）
1. 前置：`spantree mode flat`（MVRP 仅支持 flat 模式）
2. 全局与端口启用：`mvrp enable` + `mvrp linkagg 7 enable` / `mvrp port 2/1/3 enable`（<<<PAGE 160>>>）
3. 可选限流：`mvrp maximum-vlan 150`（默认动态 VLAN 上限 256）（<<<PAGE 161>>>）
4. 验证：源端建 VLAN 40 后，下游 `show vlan` 出现 `40 dyn`，`show vlan 40 members` 端口为 dynamic tagged（<<<PAGE 162>>>）
5. 回退：`mvrp ... disable` 后动态 VLAN 消失；`spantree mode per-vlan`（<<<PAGE 163>>>）

## A2（进阶应用）
- 注册模式：`mvrp {port|linkagg} registration {normal|fixed|forbidden}`；applicant 模式（participant/non-participant/active）决定是否随 STP 状态主动声明（<<<PAGE 154>>>、<<<PAGE 155>>>）
- 四定时器：join/leave/leaveall/periodic，实测默认 Join 600、Leave 1800、LeaveAll 30000、Periodic 1（<<<PAGE 156>>>、<<<PAGE 162>>>）
- 端口类型限制：只能配在 fixed、802.1Q 和 aggregate 口，不能配 mirror/unp/VPLS Access/VLAN Stacking User 口（<<<PAGE 160>>>）

## E（实证案例）
- C-13 动态 VLAN 全生命周期：6360 建 VLAN 40 → 6870/6860 `show vlan` 出现 `40 dyn` → 删除报错 → 禁用 MVRP 后消失（<<<PAGE 160>>>-<<<PAGE 164>>>）

## B（边界与陷阱）
- 动态 VLAN 删不掉：`no vlan 40` 报 "ERROR: Dynamic vlan 40 cannot be deleted"——必须先在源端删 VLAN 或禁用 MVRP，否则被自动重建（<<<PAGE 163>>>）
- 动态 VLAN 不建 IP 接口、不映射 MSTI，L3/MSTP 需手工补配（<<<PAGE 163>>>）
- 新的 maximum-vlan 若小于当前已学动态 VLAN 数，须禁用再启用 MVRP 才生效（<<<PAGE 161>>>）
- MVRP 仅支持 STP flat 模式（<<<PAGE 154>>>）

## 来源
- principle·P-20 协议原理与报文模型（<<<PAGE 152>>>、<<<PAGE 153>>>）
- principle·P-21 注册/申请者模式（<<<PAGE 154>>>、<<<PAGE 155>>>）
- principle·P-22 动态 VLAN 生命周期（<<<PAGE 161>>>-<<<PAGE 163>>>）
- principle·P-23 四定时器（<<<PAGE 156>>>、<<<PAGE 162>>>）
- case·C-13；counter·X-05/X-06/X-07
