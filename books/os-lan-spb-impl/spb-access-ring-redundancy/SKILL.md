---
name: spb-access-ring-redundancy
description: 何时用：接入交换机双上联（DHL）、ERP 环过 SPB 延伸、BEB 经共享网 multi-access 接入时。
source_book: DT00XTE323EN SPB Concepts & Implementation
---

# 接入冗余与环保护（Multi-Access / DHL / ERP）

## R · 原文引用

> "-> erp-ring ring_id port1 {chassis/slot/port | linkagg agg_id} port2 {...} service-vlan vlan_id level level_num -> erp-ring ring_id rpl-node {...} -> erp-ring ring_id sap-neighbor {...} -> erp-ring ring_id port1 ... access-tagged ... spb-remote-system switch_mac_address service-vlan vlan_id level level_num -> erp-ring ring_id enable" (p243)

> "The Dual-Home Link (DHL) is an AOS feature on access switches. DHL provides fast failover between core and edge switches without implementing Spanning Tree. A DHL Active-Active configuration consists of: A DHL session. Only one session per switch is allowed. Two DHL links... A VLAN-to-link mapping that specifies which of the VLANs each DHL link will service." (p250)

> "-> spb isis interface port 2/1 type multi-access -> spb isis interface linkagg 5 priority 90 — Default: 64. DIS: Highest interface priority; Tiebreaker: highest @BMAC ... No DIS backup; New DIS election without significant disruption (3s)" (p229)

## I · 方法论骨架

三种接入冗余/共享形态，按场景选：
1. **DHL**（p29）：接入交换机双上联两台 BEB，不跑 STP；每机仅一个会话，linkA/linkB + vlan-map 定向 VLAN；切换时 `mac-flushing raw`。
2. **ERP（G.8032）**（f13）：环网经 BEB SAP 口延伸过 SPB 云。分工：环内节点配 port1/port2 + service-vlan + MEG level，RPL owner 加 rpl-node 与 wait-to-restore-timer，靠 BEB 的节点配 sap-neighbor；BEB 侧建服务/SAP 并用 `access-tagged ... spb-remote-system <对端 B-MAC>` 把环另一端接过 SPB。
3. **Multi-Access 共享网**（p13）：跨共享 LAN/微波 PMP/跨 SPB 域时，接口从默认 P2P 改 `type multi-access`，DIS 选举按优先级（默认 64）定、同分取最高 B-MAC，重选约 3 秒；同一台机可混配 P2P 与 multi-access。

## A1 · 书中案例（Lab 配置序列精要）

Lab7b DHL 双归属（c13，p250）：
```
! Sw3（接入）
dhl 1
dhl 1 linka port 1/1/7 linkb port 1/1/8
dhl 1 vlan-map linkb 40
dhl 1 mac-flushing raw
dhl 1 admin-state enable
! BEB 侧服务 + SAP，核心侧内联网关 + VRRP 交叉优先级
service spb 4003 isid 4003 bvlan 2002 description Finance admin-state enable
service spb 4003 sap port 1/1/7:30 admin-state enable stats enable
ip vrrp 30 interface L3vpnvlan30 priority 200 / address 192.168.30.254 / admin-state enable
```
Lab7c ERP 环过 SPB（c14，p256）：环内 `erp-ring 1 port1 1/1/3 port2 1/1/27 service-vlan 1000 level 1` + `rpl-node port 1/1/27` + `wait-to-restore-timer 1` + `sap-neighbor port 1/1/3`；BEB 侧同口挂三 SAP（1000 控制 / 30 / 40 业务）+ `erp-ring 1 port1 access-tagged 1/1/3 spb-remote-system <BMAC> service-vlan 1000 level 1`。
Lab7a 共享网（c12，p246）：先 disable 原 P2P 口，再 `spb isis interface port 1/1/3 type multi-access`（Sw7 加 `priority 127` 抢 DIS）；验证 `show spb isis adjacency`（一口多邻接）；附完整回滚序列。

## A2 · 触发场景（含与相邻 skill 的区分）

- 接入交换机要双上联免 STP、现网 ERP 环要跨 SPB 机房延伸、BEB 间经运营商共享以太网/微波互联时用本 skill。
- 与 `spb-bum-protection` 的区分：LBD 只检测封口不成方案，DHL/ERP 是带倒换的成套冗余；与 `spb-backbone-deploy` 的区分：multi-access 是骨干接口形态的改造（P2P→共享），但成套 Lab 场景（含回滚）集中在本 skill。

## E · 可执行步骤

1. **DHL 部署**：接入机 `dhl 1` → 指定 linka/linkb（物理口或 linkagg）→ `vlan-map` 把定向 VLAN 绑到指定链路 → `mac-flushing raw` → `admin-state enable`；`show dhl 1` 看 Active Vlans 分配。
2. **ERP 部署**：环内节点按 A1 模板配 ring/rpl/sap-neighbor；BEB 侧建服务（ERP 控制 VLAN 的服务必须建在**控制 BVLAN** 上）+ 三类 SAP + spb-remote-system 形式；`show erp` / `show erp statistics` 验证，断纤看 RPL 阻塞恢复与 WTR 计时。
3. **Multi-Access 改造**：disable 原 P2P 骨干口 → 各机出线到共享网 → `type multi-access`（需要控制 DIS 则加 priority）→ 验证一口多邻接；保留回滚序列（`no spb isis interface port X` + 原口重新 enable）。

## B · 边界与陷阱

- **ERP/SPB 六条铁律**（p23/ce08）：每 SVLAN 最多 2 个 ERP 型 NNI 关联；环不能建在 802.1q tag 口或 STP 型 NNI 上；BEB 不能做 RPL 节点；RPL 口不能在 SPB 网内也不能做 SAP neighbor；ERP 服务 VLAN 的 SPB 服务必须配在控制 BVLAN；多环共存时各环 VLAN 范围（含服务 VLAN）互斥、服务 ID 不跨环。
- DHL 每交换机只允许一个会话（p29）；VLAN 池需同时 tag 到两条链路。
- multi-access 无 DIS 备份，重选 3 秒（p13）；改 SAP 后需 disable/enable 端口重启分类（c13）。
- spb-remote-system 填的是对端 BEB 的 B-MAC（`show spb isis info` 获取）。

---
来源条目: f13, p13, p23, p29, c12, c13, c14, ce08, g10, g11, g15, g31
