---
name: aos-mpls-deploy-license
description: 何时用：在 AOS/OmniSwitch 上从零部署 MPLS 骨干（装包、许可、Loopback0、十步流程）或排查许可导致的 MPLS 失效时。
source_book: DT00XTE324EN MPLS Concepts & Implementation
---

# AOS MPLS 部署流程与许可管理（十步法）

## R · 原文引用

> "Step 1: Install MPLS Package / Step 2: IP Interface Creation. / Step 3: Setup Routing for the interfaces using OSPF. / Step 4: Load LDP protocol. / Step 5: Enable MPLS/LDP on the interface / Step 6: Configure VPLS service"（p58-65）

> "A Loopback0 interface that will serve as the system IP address to identify the router as an MPLS router. This requirement is specific to the OmniSwitch."（p58）

> "IP/MPLS first supported release is 8.9R3 and supported on the OmniSwitch 6860N platform. ... MPLS is packaged into a Debian package which can be installed on the switch."（p59, p118）

> "MPLS will be enabled only if it receives the license status as 'permanent' or 'demo' license not yet expired. And temporarily disables the feature if the license status is invalid (no-license) or 'demo' license expire."（p92）

## I · 方法论骨架

十步固定次序（不可乱序）：
1. 全网安装 MPLS Debian 包：`pkgmgr install uosn-mpls-v1.deb`（包先拷到 /flash/working/pkg）
2. 创建互联 VLAN 与 IP 接口
3. 配 OSPF underlay，含每台交换机 Loopback0（OmniSwitch 特有：Loopback0 即系统 IP）
4. 安装许可（SILOS 服务器 + SWLIC 客户端）
5. `mpls load ldp` + 全局/接口两级使能 MPLS/LDP
6. 建 VPLS 服务（7-10：SDP/bind-sdp/SAP/验证，见 vpls-signaling-ldp-vs-bgp skill）

许可两类选型：
- 站点许可（Site-based）：浮动共享，1 份覆盖最多 4 个网络节点；一个节点可以是独立交换机或最多 8 台的虚拟机箱（VC）
- 节点许可（Node-based）：绑定单个 MPLS 节点，不绑硬件序列号/MAC

版本准入：首版支持 AOS 8.9R3，平台仅 OmniSwitch 6860N。

## A1 · 书中案例

Lab 1（p83-96）：四台 OS6860 环形骨干。互联 VLAN 70/79/80/89/90（mtu-ip 4094），每台 Loopback0=192.168.254.{7-10}；OSPF area 0.0.0.0 接口 type point-to-point；SILOS 许可服务器 listen-port 8883，各交换机 `license client site-id Master server-ip ...`；`mpls load ldp` 后逐接口 `mpls ldp interface "int_79" admin-state enable`。初始四台 show license-server info 均 NO LICENSE，接入 SILOS 后拿到 15/23 天 DEMO 许可。

## A2 · 触发场景（含与相邻 skill 的区分）

- 新项目在 OmniSwitch 上开 MPLS：本 skill 给出前置与顺序骨架。
- 已部署网络 MPLS 突发全网失效：先查许可（ce01 路径），再查配置。
- 区分：骨干就绪后叠加 VPLS 服务的 CLI 细节归 `vpls-signaling-ldp-vs-bgp`；标准化项目模板归 `mpls-reference-design`；LDP 行为规则解读归 `aos-mpls-operating-rules`。

## E · 可执行步骤

1. 软硬件准入核对：AOS ≥ 8.9R3、平台 OS6860N（p118）
2. 规划 loopback 段（如 192.168.254.0/24），核查全网唯一
3. 拷包 → `pkgmgr install uosn-mpls-v1.deb` → `pkgmgr verify` → `show pkgmgr` 确认
4. 建 VLAN/IP 接口，配 OSPF，确认 `sh ip routes` 全学到、LER 间全可达
5. 配 SILOS/SWLIC 许可：`show license-server usage/info`、`sh license-info` 确认 permanent 或未过期 demo、Connection Status=Connected
6. `mpls load ldp` → `mpls ldp admin-state enable` → 逐接口 `mpls interface ... enable` + `mpls ldp interface ... enable`
7. 验证：`show mpls ldp session` 双邻居 OPERATIONAL
8. `write memory flash-synchro`，备份 vcboot.cfg/vcsetup.cfg

## B · 边界与陷阱

- ce01：许可无效（no-license）或 demo 过期时 MPLS 被**临时禁用**——配置还在但功能停摆，排障入口是 `sh license-info` 而非配置检查。
- ce02：LSR ID（loopback）在 MPLS 域内不唯一会导致 "unpredictable behavior"（p125 加粗），上线清单必含唯一性核查。
- 只装包不够：LDP/BGP 模块还需分别 `mpls load ldp` / `ip load bgp` 才加载。
- 客户超 4 台节点时需买多份站点许可或改节点许可（ALE Licensing Portal 操作）。

---
来源条目: f01, p01, p02, p03, c01, ce01, ce02
