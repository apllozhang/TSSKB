# BOOK_OVERVIEW — Ethernet Ring Protection Switching Application Note (ethernet-ring-protection-switching-application-note-en.pdf, 17p)

## 主旨
基于 ITU-T G.8032/Y.1344 (2020 Cor.1) 的 ERP v2（ERPS）机制参考指南：面向关键业务网络（mission-critical）客户与售前，讲清环网正常/故障/恢复各状态下节点行为，并给出多环设计、协议交互、产品组合与配置示例。

## 骨架
1. **Abstract/Intro（p5）**：ERP 提供亚秒收敛、低控制面开销、配置简单；ALE 全系 OmniSwitch（含 hardened/VC）支持。
2. **Basic concept（p5-6）**：环 = 至少双环口的节点闭合环；平时仅阻塞 RPL 防环；RPL Owner（可选 RPL Neighbour）负责阻塞；故障时解阻 RPL 保连通；R-APS 协议协调；多环 = major ring + sub-rings。
3. **Principle of operation（p7-12）**：两大原则（环避免 + 以太网流转发）。正常态：节点 Idle，RPL Owner 发 (NR, RB)。单链故障：hold-off（0-10s）→ 本地阻塞 + FDB flush + 双向发 R-APS SF；收到首次 SF 全环 flush（共两次）；靠 (Node ID, Blocked Port ID) 对去重防反复 flush；RPL Owner 收 SF 解阻 RPL。RPL 自身故障例外：SF 带 DNF 位，全环不 flush。恢复：guard timer 防过期消息成环；低优先级 ID 端先解阻；revertive 模式 WTR 定时器后 RPL Owner 重阻 RPL 并发 (NR, RB)，全网 flush；非 revertive 需管理员 clear。
4. **Interconnected rings（p13-14）**：接入/汇聚连接方式对比（STP 不推荐、DHL 适用单节点、多环推荐）；多环三原则（R-APS 不跨环共享、每端口单环控制、每环独立 RPL）；R-APS Virtual Channel。
5. **Convergence（p14-15）**：50ms 成立四条件（无拥塞/全 idle/节点<16/光纤<1200km）；收敛时间分解；VC+LACP 组合提弹性但加时延；50ms ≠ 端到端收敛；与 MPLS FRR 类比澄清。
6. **协议交互（p15-16）**：ERP 口自动禁 STP，非环口 STP 照跑；STP 域单点故障→建议 sub-ring 补全网冗余；802.1ad VLAN stacking（NNI 可作 ERP 口，UNI 不可）。
7. **Portfolio + 配置附录（p16-17）**：9900/6900/6860E-N/6560/6570M/6865/6465T；major ring ERP#1 + sub-ring ERP#2 配置图。

## 批判与局限
- 应用笔记体裁：配置细节主要在图 13 中（文本无逐条 CLI）。
- 50ms 条件苛刻且明确声明非端到端；对超规格场景只说"may take longer"无量化。
- 2023 年 6 月版本文档。

## 提取方向
principles（防环/flush/DNF/guard/WTR 等机制规则）、cases（故障与恢复状态机走查、多环设计、配置拓扑）、counter-examples（STP 弊端、过期 R-APS、反复 flush、VC 加时延等）、frameworks（接入连接方式选型、恢复模式选型、收敛预算框架）、glossary 15-25 条。
