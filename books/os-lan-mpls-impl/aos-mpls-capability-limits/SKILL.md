---
name: aos-mpls-capability-limits
description: 何时用：售前方案引用 MPLS 特性（TE/VPWS/RR/EXP QoS 等）之前核对 AOS 首版支持边界，避免设计踩坑时。
source_book: DT00XTE324EN MPLS Concepts & Implementation
---

# AOS 首版 MPLS 能力边界（六项不支持清单）

## R · 原文引用

> "Current implementation of IP/MPLS in AOS does not support RSVP."（p127）

> "Explicit NULL is currently not supported in AOS implementation. ... QOS over EXP bit is not supported in the current implementation of AOS. ... TTL manipulation is not supported for MPLS tag in the current implementation of AOS. ... VPWS is not supported in the current implementation of AOS. The use of RR in the BGP signaled VPLS network is not currently supported in AOS implementation."（p127-133）

> "The explicit NULL can be used in this case to solve this issue. ... Explicit NULL is currently not supported"（p128-129）

## I · 方法论骨架

Reference Design Guide 明确标注 AOS 首版（8.9R3）不支持的六项，每项给出替代路径：

| 不支持特性 | 影响 | 替代方案 |
|---|---|---|
| RSVP-TE | 无流量工程/带宽预留 | 只能 LDP 尾端隧道，按 IGP 最优路径 |
| 显式 NULL | PHP 时 EXP 无法保留 | 无直接替代（见下） |
| QoS over EXP | EXP 位不能承载 QoS | QoS 落 IP DSCP |
| MPLS TTL 操作 | 不能仿 IP TTL 隐藏骨干跳数 | traceroute 会暴露 MPLS 骨干 |
| VPWS | 无点对点二层专线（E-Pipe） | 用两点 VPLS 模拟 |
| BGP VPLS 的 RR | 邻居不能收敛到反射器 | IBGP 全互联 |

用法：任何引用 MPLS 特性的方案/标书，逐条过这张表；六项之一是硬需求时，要么换方案要么确认 AOS 后续版本（教材 p118 预告"后续版本可能补充"）。

## A1 · 书中案例

- ce03 场景：客户要求 MPLS 骨干端到端 QoS——因 PHP 弹标签丢 EXP 且显式 NULL 不支持，QoS 策略改落在 DSCP。
- ce07 场景：客户要做 10+ 站点 VPLS——BGP 信令本应用 RR 收敛邻居，AOS 不支持 RR，只能评估全互联邻居数是否可接受。
- VPWS 场景：客户要点对点二层专线——AOS 无 VPWS，用两台 PE 各配一个 VPLS（只有两个成员）模拟 E-Pipe。

## A2 · 触发场景（含与相邻 skill 的区分）

- 售前拿业界通用 MPLS 方案（常有 TE/VPWS/RR）套 AOS：本 skill 做禁引核对。
- 交付后发现 traceroute 暴露骨干跳数、QoS 不生效：本 skill 对应行的替代方案。
- 区分：部署怎么落地归 `aos-mpls-deploy-license`；信令怎么选归 `vpls-signaling-ldp-vs-bgp`（其中"无 RR 只能全互联"的选型约束源头在本 skill）；架构模板归 `mpls-reference-design`。本 skill 只回答"能不能做"。

## E · 可执行步骤

1. 方案评审时逐条核对六项清单，命中即在方案书中标注不支持并写替代路径。
2. QoS 设计：检查队列/标记策略是否依赖 EXP；改为 DSCP 体系的标记与队列映射。
3. 二层专线需求：确认是"任意两点互通"即可，改用两点 VPLS 实现。
4. 多站点 BGP VPLS：按全互联估算邻居数 n(n-1)/2，超运维能力则收敛站点数或拆域。
5. TE/带宽预留是硬需求：升级评估走 AOS 版本路线，当前版本不做承诺。

## B · 边界与陷阱

- 这份清单针对教材对应的首版（8.9R3）实现；教材 p118 明说后续版本可能补充，实际项目要用 `show mpls` 等命令在目标版本上复核，勿把"首版不支持"当永久结论。
- "临时禁用"类许可失效（MPLS 突发停摆）不属于本清单，归 `aos-mpls-deploy-license` 的 ce01 排查路径。
- PHP 丢 EXP 是协议行为、显式 NULL 不支持是平台行为，两者叠加才构成"EXP 路线走不通"，向客户解释时别混为一谈。

---
来源条目: ce03, ce05, ce07（交叉引用 f04）
