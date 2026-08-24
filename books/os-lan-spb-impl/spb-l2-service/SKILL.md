---
name: spb-l2-service
description: 何时用：在已建好的 SPB 骨干上开通 L2 服务（VLAN/SAP/I-SID 映射、vlan-xlation、L2 Profile、伪线）时。
source_book: DT00XTE323EN SPB Concepts & Implementation
---

# L2 服务开通（SAP / I-SID / vlan-xlation / L2 Profile）

## R · 原文引用

> "Configuration steps will be: 1. Creating VLANs on access switches 2. Create the Service Access Port 3. Create the Service Access Profile (Optional) 4. Create the Service I-SID 5. Create the Service SAP" (p108)

> "The service number is only locally significant and can differ across different BEBs. The ISID number is globally significant and must match across all BEBs connecting a given service. The BVLAN that the service is mapped must also match across all BEBs... Each ISID can be attached to one BVLAN only." (p109)

> "SAPs can only be created on access interfaces. A switch can support either multiple services for one CVLAN, or one service for multiple CVLANs." (p97/98；封装写法 p99：`:20` 单 VLAN、`:0` 未打标、`:all` 全部、`:30.32` QinQ)

> "E-LINE connection between two local SAPs or between two SAPs across the SPB network. Also known as SPB Point-to-Point Transparent Circuit • Transparent packets forwarding • No source @mac learning on the SAP • Head-end multicast mode" (p94)

## I · 方法论骨架

1. **五步开通序**（f03）：接入交换机建客户 VLAN → BEB 声明 service access port → 可选 L2 Profile → 建 service（spb X isid Y bvlan Z）→ 挂 SAP。服务只建在需要交付的 BEB 上，不建在 BCB。
2. **编号三纪律**（p07）：service 号本机有效；I-SID 与 BVLAN 全网一致；一个 I-SID 只绑一个 BVLAN；不同服务映射不同 BVLAN 实现负载分担。
3. **SAP 封装语法**（p08）：SAP = access 口（物理口或 linkagg）+ 封装标识；同一口可多 SAP 分属不同服务。
4. **vlan-xlation**（p09）：两端 CVLAN 不同时出向改写 tag；服务级与口级均可配，默认关。
5. **控制帧治理**（p10）：L2 Profile 决定 STP/GVRP/MVRP tunnel、802.1X/LLDP/AMAP drop、LACP peer。
6. **QoS 只在边缘**（p11）：分类只在 SAP 完成，进骨干后 MAC-in-MAC 不再重分类。

## A1 · 书中案例（Lab 配置序列精要）

Lab2 L2 服务部署（c02，p108）：
```
! 接入交换机
vlan 2
vlan 2 members port 1/1/1 untagged
vlan 2 members port 1/1/3 tagged
! BEB（Sw7 & Sw8 两侧）
service spb 2001 isid 2001 bvlan 2001 description vlan2 admin-state enable
service spb 2002 isid 2002 bvlan 2002 description vlan3 admin-state enable
service access port 1/1/3
service spb 2001 sap port 1/1/3:2 admin-state enable stats enable
service spb 2002 sap port 1/1/3:3 admin-state enable stats enable
```
伪线 E-LINE（p30/p94）：`service 100 spb isid 1000 bvlan 4000 pseudo-wire enable`（自动关 MAC 学习、强制 head-end 组播；disable 恢复 E-LAN）。

## A2 · 触发场景（含与相邻 skill 的区分）

- 新 VLAN 跨骨干延伸、两站点 CVLAN 编号不一致、客户控制帧要透传或拦截、点对点透明电路需求时用本 skill。
- 与 `spb-backbone-deploy` 的区分：本 skill 前提是骨干已建好（IS-IS 邻接 UP）；与 `ip-over-spb` 的区分：本 skill 只做 L2 透传，一旦要配 IP 接口/网关即转 `ip-over-spb`；与 `unp-dynamic-ov2500` 的区分：本 skill 是静态 SAP，终端动态归档归 UNP。

## E · 可执行步骤

1. 接入交换机：建客户 VLAN，用户口 untagged、上联口 tagged。
2. BEB：`service access port <p>` 声明接入侧端口。
3. （可选）`service l2profile <name> <proto> {tunnel|peer|drop}` + `service access port <p> l2profile <name>`。
4. `service spb <svc> isid <isid> bvlan <bvid> admin-state enable`（I-SID/BVLAN 全网一致；范围语法 `service spb 11-13 isid 1001-1003 bvlan 4001:3`）。
5. `service spb <svc> sap port <p>:<encap> admin-state enable stats enable`。
6. 两端 CVLAN 不同则配 `service <svc> vlan-xlation enable`（或口级）。
7. 验证：`show spb isis services`、`show service sdp spb`、`show mac-learning domain spb`（本地 MAC 落 sap:、远端 MAC 落 sdp:）。

## B · 边界与陷阱

- **绑 IP 接口后 vlan-xlation 被隐式启用并锁定**（p09/ce05）：L3 场景想改翻译状态必须先解绑接口；规划期确认翻译需求。
- 容量（p07）：AOS 每 BVLAN 1024 个 I-SID、每 I-SID 4094 个 VLAN。
- L2 Profile 默认动作表（p10）：静态口 def-access-profile——STP/GVRP/MVRP tunnel、802.1X/LLDP/AMAP drop、LACP peer；动态 UNP 口默认不同（STP drop）。
- 伪线服务强制 head-end 组播、无 MAC 学习（p30），改回 E-LAN 用 `pseudo-wire disable`。
- CoS：隧道化未打标 BPDU 自动最高优先级（p11）。

---
来源条目: f03, p07, p08, p09, p10, p11, p30, c02, ce05, g09, g13, g19, g21, g30, g33, g34, g38
