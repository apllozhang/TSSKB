---
name: 轨交组播设计（Head-End 与 Tandem 复制模式/PIM-SM RP 在 OCC/复制流量推演表）
description: 设计轨交 CCTV/PA/PIS 等组播业务的复制方式时使用：SPB 三种 BUM 复制模式（Head-End、Tandem (S,G)、Tandem (*,G)）的带宽与资源权衡、L3 组播 PIM/SSM 选型、RP 放 OCC 的理由，以及"源在 OCC / 源在车站"两类场景下各设计的环上总复制流量推演表（N×(N+1) 爆炸警告）。
source_book: Transportation Networks Design Guide & SPB-based Transportation Networks Design Guide
---

## R（何时用）
- 规划 CCTV、乘客广播、PIS 等组播/广播业务的承载方式
- 选 Head-End 还是 Tandem 复制模式，决定 ISID 的复制配置
- L3 组播模式选型（PIM-SM/BIDIR/SSM）与 RP 位置设计
- 估算不同设计下组播对环链路带宽的占用（链路容量规划的前置输入）

## I（核心理念）
SPB 对 BUM（广播/未知单播/组播）有三种复制模式：Head-End 在入口 BEB 复制成多份单播（省资源、费带宽）；Tandem (S,G) 建独立组播 SPT、任一链路只发一份（最省带宽、费资源）；Tandem (*,G) 按 BVLAN 建共享树、根在 bridge priority 决定的节点（折中，适合流量都过 OCC 根的场景）（通用版 p35-36）。轨交组播两类典型形态：源在 OCC 收看在车站（PIS/PA/Infotainment），源在车站收看在 OCC（CCTV）（通用版 p37）。L3 用 PIM-SM 且 RP 放 OCC——反正源或收端总有一头在 OCC；应用支持时叠开 SSM 让同站源收直连、绕开 RP（通用版 p37-38）。最要命的坑：L2 设计+全站共享 VLAN/ISID+Head-End 复制，站源组播总流量按 N×(N+1) 随站数平方爆炸，必须换 Tandem——而这套设计本身就因 BUM 泛洪不被推荐（通用版 p39）。

## A1（决策要点）
1. 复制模式选型：组播流量大的系统（CCTV）选 Tandem (S,G)；组播少、源多收少的场景 Head-End（配 IGMP Snooping，AOS 8.4.1R01 起）即可；流量都过根桥且不需一致性时可选 Tandem (*,G)（通用版 p35-36）
2. L3 组播基准配置：PIM-SM + RP 在 OCC；应用支持就加 SSM 解决同站源收（通用版 p37-38）
3. 同站源收的本地组播（站内 CCTV 大屏）不上环，不计入环容量（通用版 p37）
4. 源在 OCC 场景优先"Tandem:1"或"L3 RP 在 OCC:1"这类单份上环的形态（通用版 p38）
5. 任何"全站共享 VLAN/ISID 的 L2 设计"直接判负——即便没有组播，广播与未知单播也要全网泛洪（通用版 p39）

## A2（细节速查表）

| 复制模式 | 工作机制 | 带宽效率 | 资源占用 | 与单播 SPT 一致 | 适用 | 页码 |
|---|---|---|---|---|---|---|
| Head-End | 入口 BEB 复制为多份单播 | 低 | 低 | 是 | 组播流量小；源多收少（配 IGMP Snooping） | 通用版 p35-36 |
| Tandem (S,G) | 独立组播 SPT，分叉点复制 | 高 | 高（额外 SPT+组播 FDB） | 是 | 组播流量大；源少收多 | 通用版 p35-36 |
| Tandem (*,G) | 每 BVLAN 一棵共享树 | 高 | 低-中 | 否 | 流量集中过根桥（OCC 为根）；与三方设备互通 | 通用版 p35-36 |

| 场景（N 站，1 源） | 设计 | IP 层复制 | 环上总流量（Tandem） | 环上总流量（Head-End） | 页码 |
|---|---|---|---|---|---|
| 源在 OCC | L2，各站独立 VLAN/ISID | 每站一份(N) | N | 2N | 通用版 p38 |
| 源在 OCC | L2，全站共享 VLAN/ISID | 无 | 1 | N+1 | 通用版 p38 |
| 源在 OCC | L3 VPN，RP 在 OCC | 无 | 1 | N+1 | 通用版 p38 |
| 每站 1 源 | L2，各站独立 VLAN/ISID | 无 | N | 2N | 通用版 p39 |
| 每站 1 源 | L2，全站共享 VLAN/ISID | 无 | N | **N×(N+1)** | 通用版 p39 |
| 每站 1 源 | L3 VPN，RP 在 OCC | 无 | N | 无 | 通用版 p39 |

| L3 组播要点 | 说明 | 页码 |
|---|---|---|
| 支持模式 | PIM Sparse/Dense/BIDIR/SSM | 通用版 p37 |
| RP 位置 | OCC（源或收端必有一头在 OCC） | 通用版 p37-38 |
| L2 设计下的 L3 组播 | 源收不同子网即触发，至少在 OCC BEB 路由 | 通用版 p37 |

## E（场景案例）
- 轻轨案例：CCTV ISID 用 Tandem (S,G)、PIM-SM RP 在 OCC、SSM 直收同站源的组合配置（通用版 p41）
- 表 9/表 10 全形态推演：同一业务在不同设计下环流量从 1 份到 N×(N+1) 份的量级差异（通用版 p38-39）
- Tandem (*,G) 以 OCC 为根桥、PIS/PA 这类"OCC 发全网收"业务的适配（通用版 p36）

## B（限制与坑）
- Head-End 用于站源 CCTV + 共享 VLAN/ISID——流量平方级爆炸（通用版 p39）
- L2 共享 VLAN/ISID 设计即便无组播也逃不掉 BUM 全网泛洪（通用版 p39）
- 组播密集系统误用 Head-End——原文明确推荐 Tandem（通用版 p39）
- 通用版文档评审批注提示：该章节数字当时尚未经实验室验证，且现实项目常在车站配录像机本地存储、只上传选中流，实际流量模型可能与表 9/10 不同，规划前应核实（通用版 p37、p41）
- 8.4.1R01 前 Head-End 无 IGMP Snooping 配套，优化条件不成立（通用版 p36）

## 来源
Transportation Networks Design Guide（p35-39）+ SPB-based Transportation Networks Design Guide（p26-29，表 9/10 相同；Head-End 优化条件在该版写作时标注为 Multicast Optimization Phase II，需联系 ALE 确认可用性）
