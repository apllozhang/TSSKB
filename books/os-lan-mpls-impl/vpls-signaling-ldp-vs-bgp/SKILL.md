---
name: vpls-signaling-ldp-vs-bgp
description: 何时用：在 AOS MPLS 骨干上叠加 VPLS 时做 LDP/BGP 信令选型，或需要照抄两种信令的完整配置序列时。
source_book: DT00XTE324EN MPLS Concepts & Implementation
---

# VPLS 双信令实施：LDP vs BGP 选型与配置序列

## R · 原文引用

> "Step 7: Create a static SDP and trigger a message to LDP to establish a target peer with the far-end IP address / Step 8: Create a binding of an SDP to the service (VPLS) and trigger a message to mpls CMM to establish a VC label / Step 9: Configure access ports and create SAP on the access port for MPLS-VPLS"（p67-70）

> "With auto-discovery, there is no need to configure each VPLS router with all remote endpoints of VPLS tunnels"（p72）

> "Since these services are usually configured for a single AS, using MP-BGP will require either a full-mesh of peerings between LERs, or using Route Reflectors (RR). The use of RR in the BGP signaled VPLS network is not currently supported in AOS implementation."（p132-133）

> "ip bgp autonomous-system 65724 / ip bgp address-family l2vpn-vpls / ip bgp neighbor 192.168.254.8 remote-as 65724 / ip bgp neighbor 192.168.254.8 update-source Loopback0 / ip bgp neighbor 192.168.254.8 activate l2vpn-vpls"（p74, p110）

## I · 方法论骨架

选型决策（f04 + ce07）：
- LDP 信令（T-LDP）：配置简单，无自动发现——n 台 PE 需 n(n-1)/2 条伪线、每端 n-1 条 SDP；新增站点要改所有旧站点。3-4 站点以内可选。
- BGP 信令：自动发现+信令一步完成，扩容只加邻居；但 AOS 不支持 RR，IBGP 邻居仍须全互联。
- 分界线：多站点/会持续扩容选 BGP；少量站点、想省 BGP 运维选 LDP。

LDP 信令四步（f02）：建服务 → 静态 SDP 互指对端 loopback（触发 T-LDP 定向会话）→ bind-sdp 协商 VC 标签 → access port + SAP 接入。

BGP 信令路径（f03）：`ip load bgp` → AS 号 + address-family l2vpn-vpls + 全互联邻居（五要素：同 AS / 对端 loopback / update-source Loopback0 / 每邻居 activate l2vpn-vpls / admin-state enable）→ `service N vpls vplsid X signaling bgp ve-id Y`，无需手工 SDP，BGP 自动生成绑定（显示为 sdp:32768:x）。

## A1 · 书中案例

- Lab 2（p97-105，LDP）：sw7/sw8 各建服务 2/3（vplsid 200/300），SDP 78 互指对端 192.168.254.x，bind-sdp 后 SAP `1/1/3:2`；跨站点 VLAN 对不齐时补两级 vlan-xlation 恢复。验证：`show mac-learning domain vpls` 看到远端 MAC 从 sdp: 接口学到；P 节点 sw9/sw10 该表为空。
- Lab 3（p106-114，BGP）：恢复 Lab 1 备份后，sw7/sw8 配 IBGP（AS 65724），服务定义换 `signaling bgp`，sw7 全部 ve-id 1、sw8 ve-id 2；MAC 表远端接口显示 sdp:32768:2/3。
- SDP 复用（p78）：一服务绑多 SDP（`service 1 bind-sdp 20 30` 一次绑两条）；一条 SDP 被多服务复用（同一对 PE 多个 VPLS 共一条 T-LDP 会话）。
- 实验环境：R-Lab POD（8 交换机 + 10 VM，p16-19），6860-A/B 即 sw7/sw8，RDP 接入 rdp.al-mydemo.com。

## A2 · 触发场景（含与相邻 skill 的区分）

- 已有 MPLS 骨干，要开通二层 VPN 业务：本 skill。
- 售前被问"多点 VPLS 用哪种信令"：本 skill 的选型框架 + `aos-mpls-capability-limits` 的不支持清单。
- 区分：骨干/许可前置归 `aos-mpls-deploy-license`；项目级标准化模板（rtr-port/BFD 写法）归 `mpls-reference-design`；Split Horizon、标签栈等运行规则解读归 `aos-mpls-operating-rules`。

## E · 可执行步骤

LDP 路线（两端 PE 对称）：
```
service 2 vpls vplsid 200 signaling ldp admin-state enable
service sdp 78 vpls far-end 192.168.254.8        # 对端互指
service 2 bind-sdp 78
service access port 1/1/3
service 2 sap port 1/1/3:2
service 2 vlan-xlation enable                     # 需要转换时
service access port 1/1/3 vlan-xlation enable     # 先端口级再服务级
```
验证：`show mac-learning domain vpls`（sap: 与 sdp: 两类接口 MAC）。

BGP 路线（每台 PE）：
```
ip load bgp
ip bgp autonomous-system 65724
ip bgp address-family l2vpn-vpls
ip bgp neighbor <对端loopback> remote-as 65724
ip bgp neighbor <对端loopback> update-source Loopback0
ip bgp neighbor <对端loopback> activate l2vpn-vpls
ip bgp admin-state enable
service 2 vpls vplsid 200 signaling bgp ve-id 1 admin-state enable
```
验证：`show ip bgp neighbors`（established + Activate L2VPN vpls = enabled）、`show ip bgp l2vpn-vpls`。

## B · 边界与陷阱

- ce07：LDP-VPLS 配置量按全网状增长，n(n-1)/2 条伪线；新站点要改所有旧站点。
- AOS 无 RR（f04）：BGP 路线必须 IBGP 全互联，规模上限受邻居数限制。
- ce08：SAP 配成 `:0`（untagged）时出口流量永远 untagged，不会替客户打标签——对端期望 tagged 就会单通，靠两级 vlan-xlation 对齐。
- ve-id 必须每台 PE 唯一（Lab 中 sw7=1、sw8=2）。
- 每个邻居都要单独 `activate l2vpn-vpls`，漏一条该邻居不传 VPLS 路由。

---
来源条目: f02, f03, f04, p16, p17, c02, c03, c04, c07, ce07, ce08
