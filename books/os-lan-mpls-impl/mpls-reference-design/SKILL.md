---
name: mpls-reference-design
description: 何时用：售前出 AOS MPLS 方案架构（园区/城域模板）、写标准化交付配置或需要按层次排障的 show 命令手册时。
source_book: DT00XTE324EN MPLS Concepts & Implementation
---

# AOS MPLS 参考设计与最佳实践（场景模板 + 配置规范 + 验证命令）

## R · 原文引用

> "Enterprise Campus Networks: A two or three-tier architecture for a small and medium campus networks is best suited. It will provide VPN services end-to-end and IP/MPLS will be implemented from the access to the core layer. / Metro Ethernet Networks (Smart City): ... IP/MPLS network can be configured at the core and distribution layers of a three-tier network architecture. At the access layer, ethernet standard switching will be configured."（p133-134）

> "Configure IGP (OSPF/IS-IS) as an underlay in your network / Configure a (/32) loopback interface on each switch ... / Configure the OSPF/IS-IS network type as point-to-point ... / Use routed interfaces / Use Bidirectional Forwarding Detection (BFD) for fast detection and convergence / Consider using /31 contiguous (/31) addresses for point-to-point links"（p136）

> "-> ip interface IFtoR2 address 10.1.2.1/24 vlan 12 rtr-port port 1/1/1 tagged / -> service sdp 102 vpls far-end 1.1.1.6 / -> service 1 bind-sdp 102 103"（p136-138）

> "# Use this command to display FTN (FEC-To-NHLF) table information. -> show mpls ftn-table / # Use this command to view Incoming label mapping (ILM) table entries. -> show mpls ilm-table"（p139-145）

## I · 方法论骨架

两个经验证的架构模板（f06）：
1. 中小园区：二/三层架构，IP/MPLS 从接入层直达核心层，端到端 VPN 业务。
2. 城域以太（智能城市等）：三层架构，MPLS 域收敛到核心+汇聚，接入层保持标准以太交换。
定位：面向企业与城域客户的高性价比方案。

最佳实践七条（p04）：OSPF/IS-IS underlay；每台 /32 loopback 宣告进 IGP；loopback 兼作 Router-ID 且全网唯一；互联链路网络类型 point-to-point；用路由接口（routed interface）；启用 BFD；P2P 链路建议 /31 地址。

规范配置与 Lab 的差异：互联用 `rtr-port tagged` 路由口、BFD 全局 `ip bfd admin-state enable` + OSPF 接口 `bfd-state enable` 两级、一条 `bind-sdp 102 103` 绑多 SDP、业务配置只落在建全网状伪线的 PE/LER。

验证命令族谱（p18）：包/许可 → MPLS 全局/接口 → 标签表 → LDP → 业务 → BGP → MAC，按层次下钻。

## A1 · 书中案例

- LDP 规范样例（c05，p136-138，R1 视角）：Loopback0=1.1.1.1/32（兼 router-id），SDP 102/103 指向 1.1.1.6/1.1.1.7，`service 1 sap port 1/1/4:0`，一次绑两条 SDP。
- BGP 规范样例（c06，p138-139）：标准序列多了 `ip bgp mpls` 全局命令（Lab 3 中没有），其余同 Lab 3；同样只配在 R1/R6/R7。
- 验证命令族谱（p18）：`show pkgmgr`、`show license-server usage`、`show mpls`、`show mpls ftn-table`（入向 PUSH 视角）、`show mpls ilm-table`（入标签 SWAP/POP）、`show mpls forwarding-table`、`show mpls vpls-mesh`、`show mpls ldp session [tx-labels/rx-labels]`、`show service [vpls|sdp|bind-sdp]`、`show ip bgp l2vpn-vpls [path]`（path 含 VE-ID/VBO/VBS/LabelBase）、`show mac-learning domain vpls`。

## A2 · 触发场景（含与相邻 skill 的区分）

- 售前写方案书选架构模板、界定 MPLS 域边界：本 skill。
- 交付时直接抄标准化配置（比 Lab 更规范）：本 skill 的 c05/c06 模板。
- 运维排障需要命令清单：本 skill 的验证命令族谱。
- 区分：从零部署的前置流程与许可归 `aos-mpls-deploy-license`；信令选型逻辑归 `vpls-signaling-ldp-vs-bgp`；本 skill 偏"模板与规范"，出方案/写配置基线时优先用。

## E · 可执行步骤

1. 按客户类型套模板：园区→端到端 MPLS；城域→MPLS 只到核心+汇聚，接入标准交换。
2. 基线配置（每台）：
```
ip interface Loopback0 address 1.1.1.1/32
ip router router-id 1.1.1.1
ip interface IFtoR2 address 10.1.2.1/24 vlan 12 rtr-port port 1/1/1 tagged
ip ospf interface IFtoR2 type point-to-point
ip bfd admin-state enable
pkgmgr install uosn-mpls-v1.deb
mpls ldp interface IFtoR2 admin-state enable
```
3. VPLS 侧按信令选型叠加 c05（LDP：SDP+bind-sdp）或 c06（BGP：含 `ip bgp mpls`）模板。
4. 验证按族谱层次下钻：许可/包 → `show mpls` → 标签表 → LDP 会话 → `show service` → BGP → MAC 表。

## B · 边界与陷阱

- 教材示例互联地址实际用 /24（可读性取舍），最佳实践推荐 /31——交付按 /31，教学示例勿照抄。
- 最佳实践的 BFD 是全局+OSPF 接口两级使能，只配一边不生效。
- BGP 规范样例的 `ip bgp mpls` 是参考设计独有命令，Lab 3 未出现，照抄 c06 时别漏。
- 业务配置只落 PE/LER：P 节点（样例中 R2-R5）零 service 配置，别过度配置。
- 能力边界（RSVP/VPWS/RR 等六项不支持）见 `aos-mpls-capability-limits`，方案书引用特性前先核对该清单。

---
来源条目: f06, p04, p18, c05, c06
