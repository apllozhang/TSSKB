---
name: vlan-link-redundancy
description: 何时用：在 OmniSwitch 上配置 VLAN/802.1Q trunk、LACP 聚合、STP 根桥控制或 DHL 双归属冗余时。
source_book: DT00XTE215EN Access Switching
---

# VLAN 与链路冗余：802.1Q / LACP / STP / DHL

## R · 原文引用

"-> vlan 2 members port <chassis/slot/port> untagged / -> vlan 4 admin-state enable / -> vlan 10-15 100-105 200 name \"Training Network\" / -> show vlan members"（p127）

"-> linkagg lacp agg <agg_num> size <size> admin-state enable / -> linkagg lacp agg <agg_num> actor admin-key <actor_admin_key> / -> linkagg lacp port <chassis/slot/port> actor admin-key <actor_admin_key>"（p201）

"Supports two Spanning Tree operating modes: flat (single STP instance per switch) / per-VLAN (single STP instance per VLAN) (By default on OmniSwitch). STP (802.1d): Convergence time: 50 secs / RSTP (802.1w): < 1 sec"（p227）

"-> dhl 1 / -> dhl 1 linka linkagg 1 linkb linkagg 2 / -> dhl 1 vlan-map linkb 30 / -> dhl 1 admin-state enable / -> dhl 1 mac-flushing raw"（p257-259）

## I · 方法论骨架

L2 建网四层递进：
- **VLAN**：vlan N → members port … untagged|tagged → 可批量/命名（多词加引号）。物理口恒有且仅有一个 untagged 桥接 VLAN（端口默认 VLAN），其余 VLAN tagged 传送——trunk 两端对同一组 VLAN 打标签。
- **LACP 聚合**：linkagg lacp agg N size X + actor admin-key → 物理口按同 admin-key 入组。admin-key 仅本地有效，不必等于组号。VLAN 挂聚合口：vlan N members linkagg N untagged|tagged。
- **STP**：模式（flat=整机单实例 / per-vlan=1x1，默认后者）→ 协议（stp/rstp/mstp）→ 按 VLAN 调 bridge priority（0-65535，默认 32768，越小越优）→ 必要时 path-cost-mode。
- **DHL**：接入双上行两核心的无 STP 双活：每 VLAN 只在一条链路转发（防环），故障整体切换。每机仅 1 会话、2 链路（linkA/linkB）。

## A1 · 书中案例（Lab 配置精要）

- **802.1Q trunk（p218-224）**：先 vlan 58 members port 2/1/3 untagged 做默认 VLAN，再 vlan 20/30 members linkagg 7 tagged 与 port 2/1/3 tagged；一口同载 tagged 20/30 + untagged 58；两端各做 VLAN 20/30 网关，Client5/6 跨 VLAN ping 验证。
- **LACP + 故障演练（p209-217）**：6360 VC 侧跨机箱 linkagg lacp agg 7 size 2 actor admin-key 7（1/1/3+2/1/4），6870 侧 1/1/3-4 同 key；单边配好 show linkagg 显示 DOWN，对端配完即 UP；disable 成员口演示单链路存活。
- **STP 根桥（p238-248）**：spantree vlan 20 priority 20000 设 6870 为根（Bridge ID==Designated Root）；show spantree vlan 20 ports 看 ROOT/ALT/BLK；1x1 负载分担：VLAN20 根=6870(20000)、VLAN30 根=6860，两上行口各转一个 VLAN。
- **DHL（p261-266）**：清端口 VLAN 成员再入聚合；dhl 1 linka linkagg 7 linkb linkagg 8、vlan-map linkb 30、admin-state enable、mac-flushing raw；ping 中禁 linkagg 7 验证无缝切换，恢复等 30 秒 pre-emption 回切。

## A2 · 触发场景（含与相邻 skill 的区分）

- 划 VLAN、打 trunk、聚合带宽/冗余、防环与根桥规划、接入双上行双活——本 skill。
- VLAN 建好后要配网关 IP/DHCP/VRRP → ip-services-basic。
- 端口要按"设备身份"动态进 VLAN（认证分类）→ access-guardian-unp。
- 聚合两端是 VC 内跨机箱端口 → 先看 virtual-chassis-deployment。

## E · 可执行步骤

VLAN：`vlan N` → `vlan N members port <c/s/p> untagged|tagged` → `show vlan members` 验证。
Trunk：默认 VLAN untagged + 业务 VLAN tagged，两端对称。
LACP：
1. `linkagg lacp agg N size X admin-state enable`，记 admin-key。
2. 端口清残留 VLAN 成员（no vlan N members port …）后 `linkagg lacp port <口> actor admin-key K`。
3. `vlan N members linkagg N untagged|tagged`；show linkagg / show linkagg port 验证。
STP：
1. `spantree mode per-vlan`（默认）→ `spantree [cist|vlan N] protocol rstp`。
2. 根桥：`spantree vlan N priority 20000`；验证 `show spantree vlan N ports active`。
DHL：
1. `dhl 1` → `dhl 1 linka linkagg A linkb linkagg B`（两链路同属一个默认 VLAN）。
2. `dhl 1 vlan-map linkb <VLAN>`（其余自动走 A）→ `dhl 1 admin-state enable` → `dhl 1 mac-flushing raw|mvrp`。
3. `show dhl 1` 看 Protected/Active VLAN。

## B · 边界与陷阱

- **端口带 VLAN 成员身份加不进 linkagg**：报 "Port cannot be added to Linkagg"——先 no vlan N members port 清干净再入组。
- **VLAN 1 不能删除**，只能停用/移端口；清理脚本要把 VLAN 1 剔除。
- **VLAN 无活动成员 → IP 接口 DOWN 且不被 L3 路由宣告**（比 down 更严重）：排障先 show vlan members。
- **静态聚合仅限 OmniSwitch 之间**；对接服务器/存储/第三方必须 LACP（组内同速）。
- **DHL 回切延迟**：链路恢复后等 pre-emption timer（默认 30 秒，0-600 可配）才回切，勿误判故障；DHL 口上 STP 自动禁用；mobile/802.1x/GVRP/UNI 口不支持 DHL。
- hash-control 默认按型号分 brief/extended（6900/6465/6360=brief），分流不均时切 extended。
- STP 路径成本两套：16bit（1G=4、10G=2）用于 802.1d/w，32bit 用于 MSTP；path-cost-mode auto 随协议选。

---
来源条目: f06, f08, f09, f10, p19, p20, p27, p28, p29, p30, p31, p32, ce05, ce10, ce11, ce12, ce13, c04, c06, c07, c08, c09, g20, g22, g23, g24
