# DIGEST — Ethernet Ring Protection Switching Application Note 精华

本书是基于 ITU-T G.8032/Y.1344（2020 Cor.1）的 ERP v2（ERPS）应用笔记（17 页），面向关键业务网络客户与售前：讲清单环正常/故障/RPL 故障/恢复四状态节点行为、多环设计与三原则、协议交互、收敛预算与产品组合。ALE 全系 OmniSwitch（含 hardened/VC）支持。

## 一、知识地图（两技能单元）

1. **环保护机制**（sol-erp-ring-mechanism）：RPL/RPL Owner/R-APS 消息体系、hold-off/guard/WTR 定时器、DNF 位、revertive/non-revertive、50ms 四前提（p5-15）。
2. **多环设计与协议交互**（sol-erp-multi-ring-design）：多环三原则、R-APS Virtual Channel、STP/DHL/multi-ring 选型对比、NNI/UNI、产品组合（p13-17）。

## 二、两单元要点串讲

### 1. 机制：定时器体系驱动的状态机
防环原则 = 任一时刻只阻塞一条环链路（<<<PAGE 7>>>）。正常态 RPL Owner 阻塞 RPL 并周期发 (NR, RB)。单链故障：hold-off（0-10s 过滤间歇故障）→ 检测节点三连动作（本地阻塞/flush/双向发 SF）→ 全环各 flush 两次，靠 (Node ID, Blocked Port ID) 去重 → RPL Owner 收首个 SF 解阻 RPL（<<<PAGE 8-9>>>）。RPL 自身故障例外：SF 带 DNF 位、全环不 flush（<<<PAGE 11>>>）。恢复：guard 屏蔽过期消息防环 → 低 ID 端先解阻 → WTR（>guard）后 (NR, RB) 触发全网回切+一次性 flush；non-revertive 则等管理员 clear（<<<PAGE 11-12>>>）。

### 2. 多环：三原则 + Virtual Channel
接入接环三选一：STP（不推荐）、DHL（仅单节点）、multi-ring + ERP v2（推荐）（<<<PAGE 13>>>）。多环三原则：R-APS 不跨环共享、每端口单环控制、每环独立 RPL（<<<PAGE 13>>>）。子环跨互联节点共享链路必须用 R-APS Virtual Channel，多子环用不同 VLAN；互联链路本身归 major ring 管（<<<PAGE 14>>>）。50ms 保护切换有四前提（无拥塞/全 idle/节点<16/光纤<1200km）且明确不是端到端收敛（<<<PAGE 14-15>>>）。VC+LACP 可加弹性但收敛变慢（<<<PAGE 15>>>）。NNI 可作 ERP 口、UNI 不可；9900/6900 至 6865/6465T 全系支持（<<<PAGE 16>>>）。

## 三、本书在知识库中的位置
与 sol-mpls-reference（L2VPN 专线）、sol-spb / os-lan-spb-impl（SPB 路由型二层）、os-lan-vxlan-evpn（数据中心）共同构成 ALE 二层冗余方案谱系——ERP 定位亚秒环保护、低控制面开销、配置简单，是城域/工业环网首选。跨书易混点：50ms 是保护切换时间而非端到端收敛，与 MPLS FRR 的 50ms 语义同理；ERP 口自动禁 STP 但 BPDUs 仍会泛洪。

## 来源
Ethernet Ring Protection Switching Application Note（ethernet-ring-protection-switching-application-note-en.pdf，17p，2023-06 版）。verified.md：cases C1-C14；principles P1-P20；counter-examples X1-X17；frameworks F1-F4；glossary 29 条。
