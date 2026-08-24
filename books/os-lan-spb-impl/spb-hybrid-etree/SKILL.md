---
name: spb-hybrid-etree
description: 何时用：单口同时做桥接与 SAP（Hybrid）、或要客户间隔离的有根多点服务（E-Tree Leaf/Root）时。
source_book: DT00XTE323EN SPB Concepts & Implementation
---

# 混合接入端口与 E-Tree 服务

## R · 原文引用

> "Hybrid SAP and Bridge Port Hybrid access port feature allows a single port to function both as an access port and a bridging port. Hybrid configured port: a bridge port with a default VLAN and tagged VLAN for bridging; a SAPs for services with mapped tagged VLANs. -> service access port 1/1/3-10 hybrid enable" (p315/316)

> "SAPs are designated as either leaf SAP or Root SAP. A leaf SAP cannot communicate with another Leaf SAP in the service spanning multiple BEBs whereas Leaf SAP to Root SAP traffic is allowed... Note: Conventional SAPs are called Root SAPs. Note: As of 8.9.R03, all SAPs created for E-Tree service are only of type Leaf" (p318)

## I · 方法论骨架

1. **Hybrid 一口双角色**（p24）：分类发生在入口——SAP VLAN 打标流量按服务域处理，常规打标/未打标流量按 VLAN 域桥接；解决聚合交换机下联口不再拆两个物理口。
2. **E-Tree 隔离语义**（p25）：Leaf↔Leaf 不通，Leaf↔Root 与 Root↔Root 全通（SAP 级 PVLAN）；`service X spb isid N bvlan V e-tree enable` 或 UNP profile 的 e-tree 选项。
3. **Root 落点规则**：8.9.R03 起 e-tree 服务新建 SAP 全为 Leaf；Root 侧必须落在对端 BEB 上、以同 I-SID 的普通（非 e-tree）服务形态出现。

## A1 · 书中案例（Lab 配置序列精要）

Lab10（c17，p328/331）：
```
! Hybrid：VLAN3 走桥接域、VLAN2 走服务域，同一口
service access port 1/1/3 hybrid enable
service spb 2002 sap port 1/1/3:2 admin-state enable stats enable
! E-Tree：Sw1/Sw8 为 Leaf 侧
service 2004 spb isid 2004 bvlan 2004 description vlan4 e-tree enable
service 2004 sap port 1/1/3:4 stats enable
! Sw7 为 Root 侧：同 I-SID、普通 E-LAN 服务（无 e-tree 选项）
service 2004 spb isid 2004 bvlan 2004 description vlan4 admin-state enable
```
验证：`show spb isis services` + ping 矩阵——Leaf↔Leaf 断、Leaf↔Root 通。

## A2 · 触发场景（含与相邻 skill 的区分）

- 端口预算紧张要一口混跑桥接流量与 SPB 业务、或同一服务内租户之间要互相隔离（如政企接入、监控汇聚）时用本 skill。
- 与 `spb-l2-service` 的区分：那是标准 E-LAN 任意互通的开通流程，本 skill 处理两个 Day3 增强——端口形态（hybrid）与隔离模型（e-tree）；底层 service/sap 语法复用 `spb-l2-service`。
- 与 `unp-dynamic-ov2500` 的区分：UNP profile 的 e-tree 选项归动态服务 skill，本 skill 覆盖静态配置形态。

## E · 可执行步骤

1. **Hybrid**：BEB 上 `service access port <p> hybrid enable` → 同一口照常挂 SAP（`service spb X sap port <p>:<vid>`）→ 桥接 VLAN 正常配 vlan members。
2. **E-Tree**：Leaf 侧 BEB 建 `service <id> spb isid <n> bvlan <v> e-tree enable` + SAP；Root 侧 BEB 用同 I-SID/BVLAN 建普通服务（不加 e-tree）+ SAP。
3. 验证：`show spb isis services` 确认两形态并存；按 ping 矩阵测 Leaf↔Leaf（应断）与 Leaf↔Root（应通）。
4. 关闭：`service access port <p> hybrid disable`；E-Tree 逆向改造需重建服务。

## B · 边界与陷阱

- **两端都配 e-tree = 全 Leaf 死网**（ce09）：8.9.R03 起 e-tree 服务的 SAP 一律 Leaf，Root 必须在对端建成普通服务。
- **用户报障"同服务两站不通"先查是否都是 Leaf**——这是 E-Tree 的设计语义而非故障（ce09）。
- Hybrid 为 8.9.R03 起特性（p24），旧版本需升级。
- Hybrid 分类在入口按 VLAN tag 判定（p324），规划时要明确哪些 VLAN 归服务域、哪些归桥接域，避免重叠。

---
来源条目: p24, p25, c17, ce09, g18
