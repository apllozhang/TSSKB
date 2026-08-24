---
name: ifab-zero-touch-automation
description: iFab 智能织构开箱自组网方案：Auto-VC/LACP/SPB/Routing 能力链与 8.10R2 opt-in 行为变更的施工注意。
source_book: DT00XPS281EN Campus LAN Presales
---

# iFab 智能织构与零接触自动化

## R · 原文引用

> "INTELLIGENT FABRIC — Addressing operational challenges: Automated deployment, Plug-n-play deployment, Self-healing network fabric, Preventing configuration errors. Auto-VC: Automated VC creation / Auto-LACP: LACP Link aggregates creation between neighbors / Auto-SPB Fabric: Automated SPB-M (L2) domains creation / Auto-Routing / Auto-Network Profile / Auto-MVRP" (p135)

> "Prompt to disable auto-fabric during the boot sequence giving user 10s to decide … input is [Y] (default) … Starting with 8.10R2 auto-fabric is opt-in !!" (p137)

## I · 方法论骨架

iFab 是一组自动化能力的叠加链，演进路线 **Stacking → Auto VC → Access Fabric → Intelligent Fabric**，逐级减少人工配置：

| 能力 | 自动完成 |
|---|---|
| Auto-VC | 邻居间自动建虚拟机箱 |
| Auto-LACP | 邻居间自动做链路聚合 |
| Auto-SPB Fabric | 自动建 SPB-M L2 域 |
| Auto-Routing | 自动配 L3 路由 |
| Auto-Network Profile / Auto-MVRP | 自动建档案 / 自动传播 VLAN |

**版本行为分水岭**：8.10R2 之前首次开机默认启用（boot 时 10 秒 Y/N 窗口，默认 Y）；**8.10R2 起改为 opt-in，需显式启用**。配套 AMS（AOS 微服务框架）支撑交换机社群间配置预下发与签名库共享——客户不用 OmniVista、只用第三方网管时，交换机之间仍能互相同步。

## A1 · 书中案例

p12/ce06 记载的双向踩坑实例：老版本新设备插入现网自动与邻居建 VC/起 SPB 织构造成意外合并；新版本按旧文档施工则自动化一直不生效、开通延迟。

## A2 · 触发场景（含与相邻 skill 的区分）

- 触发：客户痛点是"分支没人管、运维人力少"，要开箱即插即用、自愈织构；或交付侧排障"自动化为什么没跑起来"。
- 区分：本 skill 管 **自动组网行为与版本开关**；手动 VC 设计规则在 `virtual-chassis-design`；SPB 域设计在 `spb-vxlan-core-fabric`；SMB 场景的 OXO 零接触装机在 `campus-reference-architectures`（c06）。

## E · 可执行步骤

1. 盘点现场 AOS 版本，决定施工手册走"默认开"还是"显式开"。
2. 8.10R2 前环境：插电前想清楚 boot 10 秒窗口的选择，避免新设备误并入现网织构。
3. 8.10R2+ 环境：在启动流程或脚本中显式启用 auto-fabric。
4. 核对 auto-VFL 征用端口清单（6900 每台最后 5 口、6560 29/30 或 53/54、6360 11/12、27/28 或 51/52），确认不与规划的业务上联口冲突。
5. 无 OmniVista 的客户：用 AMS 的 cfg 预下发 + configuration apply network-sync 实现批量同步。

## B · 边界与陷阱

- ce06 双向坑：老版本误组网造成配置漂移/意外 VC 合并；新版本默认关闭，按旧文档施工自动化不生效。
- auto-VFL 征用的端口含扩展槽位（无论是否插模块），规划业务口时必须避开。
- "开机即成网"叙事对运维成熟的客户反而引发失控担忧，销售时按对象调整话术。

---
来源条目: f23, p12, ce06, g02, g18
