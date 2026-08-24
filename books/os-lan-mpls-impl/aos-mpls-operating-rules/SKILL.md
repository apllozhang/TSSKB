---
name: aos-mpls-operating-rules
description: 何时用：解读 AOS 的 show mpls/ldp 输出（标签、会话、模式）、理解 SAP/SDP 服务模型或排查标签栈/QoS 行为时。
source_book: DT00XTE324EN MPLS Concepts & Implementation
---

# AOS MPLS 运行原理与服务模型（标签规则 / LDP 行为 / SAP-SDP）

## R · 原文引用

> "Service Access Point (SAP): A UNI-side logical port which binds a physical port and spcific customer traffic types to a service. ... Service Distribution Point (SDP): An NNI-side logical port which binds a service to a far-end router over which MPLS encapsulated packets are distributed."（p131，OCR 拼写原样）

> "Any directly connected route is allocated the special label Implicit NULL, i.e. 3. Any other route is allocated a label starting at 16 ... Labels from 0 to 15 are in fact special labels reserved in RFC 3032."（p100, p122）

> "In a VPN implementation, the top label is the transport label and the bottom label is the service label. This is implemented through label stacking, which is sorted in a Last-In, First-Out (LIFO) fashion."（p38, p123）

> "A PE must never send a packet on a PW if that packet has been received from a PW. ... The fact that there is always a full mesh of PWs between the PE devices ensures that every destination within the VPLS will be reached."（p133）

## I · 方法论骨架

服务模型（f05 + p14）：一个 MPLS 服务=一个 VPN/租户，只建在 LER 上；LER 四组件——SAP（UNI 侧，绑物理口+客户流量类型，可复用）、SDP（NNI 侧，绑远端）、服务隧道（FEC=vplsid）、传输隧道（FEC=loopback）。VPLS 的 PE 须按实例做 MAC 学习/桥接/复制。

标签规则（p05）：直连路由=隐式 NULL(3)；其他从 16 起（AOS 配置 16~1048575）；0-15 为 RFC 3032 保留。标签仅本地唯一，不同 LSR 可重号。

双层标签栈（p13）：栈顶=传输标签，栈底=服务标签；iLER 先压服务再压传输，中间 LSR 只 swap 传输标签，eLER 依次弹出。多数厂商栈深 4-6。

LDP 行为（p08-p10）：AOS 默认 DU+ILD+LLR；hold-time 两端取较小值、接口级覆盖全局；多链路单会话属正常，LDP ID=loopback:标签空间（:0 为 per-platform）。

PHP（p12）：eLER 发隐式 NULL 让倒数第二跳弹传输标签，省一次查表——Lab 中直连网段 Out-Label=3 即此。

## A1 · 书中案例

- Lab 1 输出解读（c01）：forwarding-table 直连网段 Out-Label=3（impl-null/PHP），远端 loopback 是 52480+ 的标签；等价路径两条带 + 标记（ECMP）。
- Lab 2 输出解读（c02/p14）：`show mac-learning domain vpls` 在 sw7 看到 `sap:1/1/3:2` 与 `sdp:78:2` 两类接口 MAC；P 节点 sw9/sw10 该表为空——服务只存在 LER 的直接证据。
- LDP 会话输出（p10）：`show mpls ldp neighbor` 显示 192.168.254.10:0，即 per-platform 标签空间；`show mpls ldp session` 显示 Advertisement mode=Downstream Unsolicited、Label retention=Liberal（p08）。
- 定时器实测（p09）：Hello 5s / Hold 15s / Targeted Hello 15s / Targeted Hold 45s / Keepalive 10s 超时 30s，Graceful Restart 使能。

## A2 · 触发场景（含与相邻 skill 的区分）

- 拿到 show mpls/ldp/mac-learning 输出要判断"正常还是故障"：本 skill。
- 设计/讲解阶段要弄清 SAP/SDP/双层隧道为什么这么配：本 skill 的模型。
- 区分：怎么把服务配出来（CLI 序列）归 `vpls-signaling-ldp-vs-bgp`；部署顺序与许可归 `aos-mpls-deploy-license`；排障命令用哪条归 `mpls-reference-design` 的命令族谱。

## E · 可执行步骤

1. 读 forwarding-table：Out-Label=3 → 直连+PHP；16+ 大标签 → 远端 FEC，正常。
2. 读 LDP 邻居：LDP ID 为 loopback:0 属 per-platform；两 LSR 间只有一个会话（多物理链路）属正常。
3. 调 hold-time：两端同时改（取小者生效），需要区分接口时用接口级覆盖全局。
4. 判断配置落点：先列出哪些 PE 是 LER；service/sap/sdp 只配 LER，P 节点零 service 配置。
5. 验证 VPLS 转发：`show mac-learning domain vpls` 应同时出现 sap:（本端）与 sdp:（远端）接口 MAC。
6. 互通排障：标签逐跳核对传输标签 swap 路径，两端核对服务标签（vplsid 一致）。

## B · 边界与陷阱

- ce03：PHP 弹顶层标签时 EXP 位一并丢失；标准解法显式 NULL 在 AOS 不支持——QoS 承诺只能落在 DSCP，不能落在 EXP。
- ce04：LDP 使能范围例外——LER 上朝向 CE 的接口**不能**使能 LDP，业务走 SAP 接入。
- ce06：LDP Graceful Restart（RFC 3478）只对计划内接管（手工 takeover）有效，CMM 意外故障或链路 down 时无效——高可用话术要区分这两种场景。
- ce02：loopback 不唯一 → 行为不可预测，读会话输出前先核查全网唯一。
- 与异厂商互通时核对 LDP 模式（AOS 默认 DU/ILD/LLR），模式不匹配会话起不来。

---
来源条目: f05, p05, p08, p09, p10, p12, p13, p14, p15, c01, ce02, ce03, ce04, ce06
