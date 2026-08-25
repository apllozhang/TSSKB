---
name: EVPN Multi-Homing 五机制（DF 选举/Split Horizon/Local Bias/Aliasing/Mass Withdraw）
description: 需要设计或排障 EVPN 多归属接入——单活/全活模式选择、ESI 配置（自动/手工）、DF 选举与 service carving、防环防重复包三件套、aliasing 负载分担、mass withdraw 快收敛、多归属 SAP 一致性时使用。
source_book: EVPN Architecture Guide（evpn-architecture-guide-en.pdf）
---

## R（触发场景）
- CE 双归/多归 PE 接入设计：选 single-active 还是 all-active
- 规划 ESI：LACP LAG 自动生成 vs 静态 LAG 手工 5 字节
- 排查多归属 BUM 重复包/环路/黑洞
- DF 选举与 failover 行为分析（含组播状态同步）

## I（核心理念）
Multi-homing 框架（F4，<<<PAGE 32>>>）：模式（SH/SA/AA）→ LACP vs 静态 LAG（决定 ESI 自动/手工）→ DF 选举（service carving：DF=EVI mod N，<<<PAGE 33>>>）→ 防环三件套（split horizon/local bias/ES pruning）→ 流量优化（aliasing/backup path/mass withdraw）。LAG 是多归属防重复包与防环的前提（P13，<<<PAGE 32>>>）；DF 防止 BUM 从 fabric 到 CE 重复洪泛（P14，<<<PAGE 32>>>）。VXLAN 下 split horizon 靠维护同 ES 对端 PE IP 列表而非 ESI label（P17，<<<PAGE 34>>>）。

## A1（行动框架）
1. 模式选型：全活（aliasing 按流负载分担，P19，<<<PAGE 34>>>）或单活（Primary/Backup PE 列表主撤路无缝切换，<<<PAGE 35-36>>>）；R-T1A ESI Label 扩展社区 flags=1 表 single-active、0 表 all-active（C5，<<<PAGE 32-33>>>）
2. ESI 配置分档（P41，<<<PAGE 41>>>）：物理口 auto（0x3+Port_MAC+0xFFFFFF）；LACP LAG auto（0x3+CE_MAC+0xFF+AggID）；静态 LAG 必须手工 5 字节
3. 防环规则落地：split horizon——路由信息永不原路返回（P16，<<<PAGE 34>>>）；local bias——发往本 PE 上全活 ES 的流量总走本地接入（P18，<<<PAGE 34>>>）
4. 组播状态保障：多归属场景 R-T7/R-T8 同步 IGMP Join/Leave 防 DF 切换丢状态（P39，<<<PAGE 36>>>）

## A2（操作步骤）
- **静态 LAG ESI 手工配置**（C15，<<<PAGE 64>>>）：`service access linkagg 20 vlan-xlation enable evpn-ethernet-segment enable esi 01:01:01:02:04`
- **多归属 SAP 一致性检查**（X22，<<<PAGE 66>>>）：确保 SAP 在 MH-ES 所有 peer 节点配置一致，否则 CE 侧流量哈希到缺配节点即黑洞
- **开局验证流程**（C5，<<<PAGE 32-33>>>）：R-T4 发现同 ES PE→DF 选举→R-T1A/1B 通告冗余模式；`show service evpn ethernet-segment` 核对

## E（实证案例）
- 多归属开局全流程：R-T4 发现→DF 选举→冗余模式通告（C5，<<<PAGE 32-33>>>）
- DF change 丢包场景与 SMET-by-all-PEs 补救：远端 PE 在收到新 PE 的 SMET 路由前持续发旧 PE 致丢包（C6，<<<PAGE 36>>>）
- MAC duplication 场景：同 MAC 两主机/环路致反复通告-撤销拖垮控制面，靠 hold-down+retry-time 解除（C10，<<<PAGE 39>>>）

## B（反例与坑）
- 无 R-T6/7/8 时多归属 IGMP 状态问题：全活不保证 Join/Leave 到 DF；单活 DF failover 丢 IGMP 状态（X13，<<<PAGE 36>>>）
- DF change 期间组播丢包不可避免，需 SMET 补救（X14，<<<PAGE 36>>>）
- MAC duplication 连续通告/撤销降级全网性能（X15，<<<PAGE 39>>>）
- SAP 配置不一致导致 CE 侧黑洞（X22，<<<PAGE 66>>>）
- 8-bit 本地段 ID 限制 ES 上限 256 个（X18，<<<PAGE 43>>>）
- SMET-by-all-PEs 用核心带宽换丢包，仅流量丢失敏感场景推荐（X19/P25，<<<PAGE 43-44>>>）
- Duplicate IP 可能是人为错误或欺骗攻击（X16，<<<PAGE 39>>>）

来源：EVPN Architecture Guide（p32-44/p64-66）
