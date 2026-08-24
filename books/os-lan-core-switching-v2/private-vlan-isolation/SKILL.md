---
name: Private VLAN 二层隔离设计
description: 需要在同一广播域内实现用户组间隔离（isolated/community）或跨交换机延伸 PVLAN 域时使用本技能。
source_book: DT00XTE216 OmniSwitch LAN Core Switching Ed15
---

## R（触发场景）
- 同一 VLAN 内要求部分主机互不通（如访客网、机房托管区隔离）
- 需要 community 组内互通、组间隔离的多租户二层设计
- PVLAN 域要跨多台交换机延伸

## I（核心理念）
Private VLAN 把一个广播域切成多个子域：Primary VLAN 对外，Secondary VLAN 分 isolated（成员间二层完全不通）与 community（组内通、组间不通）。转发模型上，出向流量经 Primary VLAN 转发，未授权的二级 VLAN 间流量被丢弃；所有 secondary 的 MAC 实际学在 primary VLAN 上。

## A1（行动框架）
1. 定义主/从 VLAN：`pvlan 100 admin-state enable` / `pvlan 100 secondary 101 type community` / `pvlan 100 secondary 103 type isolated`（<<<PAGE 103>>>）
2. 加成员端口：`pvlan 100 members port 1/1/20 untagged`（<<<PAGE 103>>>）
3. 验证：`show pvlan mapping`、`show pvlan members`（port-type: promiscuous/community/isolated）、`show mac-learning`（全部学在 VLAN 100）（<<<PAGE 103>>>）
4. 跨交换机：ISL 口 `pvlan 100 members linkagg 1 isl`，可先用 `linkagg lacp agg 1 size 2...` 建聚合承载（<<<PAGE 105>>>）
5. 删除顺序：先清成员（`no pvlan 252 members port ...`、`no pvlan 250 members linkagg ...`）再 `no pvlan 250`；收尾 `write memory flash-synchro`（<<<PAGE 112>>>）

## A2（进阶应用）
- 端口四角色：promiscuous（属 primary，全通）/ isolated（仅到 promiscuous）/ community（限本社区）/ ISL（跨交换机承载主+从全部流量）（<<<PAGE 100>>>）
- UNP 端口运行时按首个学到的 MAC 的 VLAN 分类决定 isolated/community 角色；若首 MAC 落在非 PVLAN 的标准 VLAN，则无法指定角色（<<<PAGE 106>>>）
- 需要多组互不相通的用户时用多个 community，因为一个 Primary 只能有一个 Isolated VLAN（<<<PAGE 109>>>）

## E（实证案例）
- C-07 双交换机部署：`pvlan 250 members linkagg 78 isl`，端口改入 community 251 后 Client7 ping Client8 成功，改入 isolated 252 后 ping 失败（<<<PAGE 110>>>-<<<PAGE 112>>>）
- C-08 域内配置示例：`show mac-learning` 证明 secondary 的 MAC 学在 VLAN 100（<<<PAGE 103>>>）

## B（边界与陷阱）
- 一个 Primary VLAN 只能有一个 Isolated VLAN（<<<PAGE 109>>>）
- 直接删 primary 前必须清理成员引用，否则删不掉（<<<PAGE 112>>>）

## 来源
- principle·P-12 域模型（<<<PAGE 98>>>、<<<PAGE 99>>>、<<<PAGE 109>>>）
- principle·P-13 四类端口角色（<<<PAGE 100>>>）
- principle·P-14 二层透传规则（<<<PAGE 104>>>）
- principle·P-15 UNP 运行时角色（<<<PAGE 106>>>）
- case·C-07/C-08/C-09；counter·X-19/X-20
