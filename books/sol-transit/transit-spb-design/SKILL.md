---
name: SPB 骨干设计细节（环网单 BVLAN/LAG tunnel-protocol/VC 独立控制面/link metric/QoS 映射）
description: 细化轨交 SPB 骨干设计参数时使用：环网为什么只配 1 个 BVLAN（对径节点才有双路）、SPB 骨干 LAG 必开 tunnel-protocol 哈希、虚拟 chassis 的取舍、link metric 反比速率表与 OCC-BCC 链路调优、SAP 信任模式与 CoS 端到端保序、八大流量等级映射表。
source_book: Transportation Networks Design Guide & SPB-based Transportation Networks Design Guide
---

## R（何时用）
- 确定 BVLAN 数量、ECT 规划与负载分担策略
- 配置 SPB 骨干 LAG 哈希、link metric、QoS 分类与队列
- 决定骨干节点是否用虚拟 chassis（VC）堆叠
- 排查环网链路利用率不均、故障后收敛偏慢、QoS 标记被改写等问题

## I（核心理念）
环上多数节点对之间只有一条最短路径，只有对径（antipode）节点才双路等价——所以环网配多于 2 个 BVLAN 没有收益，推荐单 BVLAN；故障时两棵 SPT 都得重算（无快速重路由），双 BVLAN 反而拖慢收敛（通用版 p29-30）。SPB 骨干端口是 MAC-in-MAC 封装，LAG 哈希只能看到 B-MAC，随机性不足，AOS 8.3.1R01 起必须开 tunnel-protocol 选项用 C-MAC/IP/端口做哈希（通用版 p30-31）。link metric 默认恒为 10（不分速率），手工调成与速率成反比可引导流量走高容量链路，并把 OCC-BCC 互联链路调大避免站间流量穿越；LAG 成员故障时 metric 不自动变化，纯冗余型 LAG 不要为带宽调低 metric（通用版 p31-33）。QoS 在 SAP 入口分类后贯穿骨干不变（封装所致也无法在骨干内再分类），hairpin 的 VLAN 侧必须 trust CoS 而非 DSCP 才能端到端保序（通用版 p33-34）。

## A1（决策要点）
1. BVLAN 规划：环网默认 1 个；确需分担再考虑 2 个，明确代价是双份 SPT 资源与 CPU（通用版 p29-30）
2. 所有 SPB 骨干 LAG 开启 tunnel-protocol 哈希选项（brief 用 C-MAC，extended 用 IP+TCP/UDP，二选一是全局设置）（通用版 p30-31）
3. VC 取舍：本指南设计倾向不用 VC 以保控制面故障独立、可跑不同软件版本；要用时 VC 与 SPB 邻居间用 LAG 互联、每个成员口连到 VC 不同槽位（通用版 p31）
4. metric 三招：按速率反比设表；OCC-BCC 链路调大 metric 隔离站间流量；链路两端都要改（相邻不相等也建邻接，但按大值算）（通用版 p31-33）
5. 带宽型 LAG 成员故障会饱和且 metric 不回退——用脚本动态调 metric，或改单条高容量链路/按 BVLAN 分流的多链路（通用版 p33）
6. QoS：SAP 处一次分类定终身；trusted SAP 拷贝 CVLAN 的 CoS，untrusted 打固定值；hairpin VLAN 侧 trust CoS（通用版 p33-34）

## A2（细节速查表）

| 链路速率 | 建议 metric | 页码 |
|---|---|---|
| 100G | 1000 | 通用版 p32 |
| 50G | 2000 | 通用版 p32 |
| 40G | 2500 | 通用版 p32 |
| 25G | 4000 | 通用版 p32 |
| 10G | 10000 | 通用版 p32 |
| 1G | 100000 | 通用版 p32 |
| 100M | 1000000 | 通用版 p32 |

| 流量等级 | PHB | CoS | 队列 | WRED | 示例系统 | 页码 |
|---|---|---|---|---|---|---|
| Network Management | AF | 7 | WFQ | 否 | SSH/SNMP/HTTPS | 通用版 p34 |
| Network Control | AF | -- | WFQ | 否 | IS-IS、OAM | 通用版 p34 |
| Real-Time | EF | 5 | SP | 否 | 电话 | 通用版 p34 |
| Business Critical | AF | 4 | WFQ | 否 | 售检票、收费、门禁、TMS、消防报警 | 通用版 p34 |
| Broadcast | AF | 3 | WFQ | 否 | PA 广播、PIS | 通用版 p34 |
| Streaming | AF | 2 | WFQ | 否 | 视频监控 | 通用版 p34 |
| Bulk | AF | 1 | WFQ | 是 | Infotainment | 通用版 p34 |
| Best Effort | BE | 0 | WFQ | 是 | Internet 上网 | 通用版 p34 |

| 设计项 | 结论 | 页码 |
|---|---|---|
| 环网 BVLAN 数 | 推荐 1 个，最多 2 | 通用版 p29-30 |
| SPB LAG 哈希 | 8.3.1R01 起开 tunnel-protocol（C-MAC 或 IP+端口） | 通用版 p30-31 |
| VC | 默认不用；用则 LAG 连每个槽位 | 通用版 p31 |
| metric 默认值 | 恒 10，与速率无关；范围 1-16M | 通用版 p31 |
| metric 生效规则 | 两端都改；不一致时按较大值 | 通用版 p32 |
| 骨干内再分类 | 不可能（MAC-in-MAC 遮蔽 L2-L4 信息） | 通用版 p34 |

## E（场景案例）
- 环拓扑最短路径示意：仅对径节点双等价路径，其余全单路（通用版 p30）
- OCC-BCC 链路 metric 调大后，站间流量不再绕行控制中心链路（通用版 p33）
- VC 接入 SPB：邻居到 VC 的 LAG 成员口分布到各槽位，主控切换时表项更新量大减（通用版 p31）
- 带宽型 LAG 成员口故障导致饱和、需 Python 脚本动态调整 metric 的补救（通用版 p33）

## B（限制与坑）
- 环网配多个 BVLAN 期望负载分担——多数节点对只有单路，收益边缘化，CPU 翻倍（通用版 p29-30）
- 故障后靠第二个 BVLAN 提速——没有 FRR，双 SPT 重算反而更慢（通用版 p29-30）
- SPB 骨干 LAG 用默认 B-MAC 哈希——随机性不足导致成员链路负载倾斜（通用版 p30-31）
- LAG metric 不随成员故障自适应——纯冗余 LAG 误按总带宽调 metric 会造成故障期饱和（通用版 p33）
- hairpin/外部路由器侧用 DSCP 信任——CoS 端到端保不住，应 trust CoS（通用版 p34）
- 通用版文档评审批注质疑高关键环境是否应推荐 VC（ISSU 问题），采用前需再评估（通用版 p31）

## 来源
Transportation Networks Design Guide（p29-34）+ SPB-based Transportation Networks Design Guide（p21-26，内容基本对应）
