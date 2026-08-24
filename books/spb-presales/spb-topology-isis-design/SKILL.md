---
name: spb-topology-isis-design
description: 做 SPB 网络拓扑设计（2-tier/3-tier 选型）、IS-IS 控制面规划（BVLAN/DIS/ECT 选路）或解释"满链路利用还无环"机制时使用。
source_book: DT00XPS279EN SPB Presales
---

# SPB 拓扑设计与 IS-IS 控制面规划

## R · 原文引用

> "3-TIER: Access Switch: 802.1Q VLAN on LAG, STP or DHL towards BEB; Aggregation Switch: BEB role, VLAN to I-SID, IS-IS for MAC learning, IS-IS for SPB paths, PBB for data plane; Core Switch: BCB role, learns BEB addresses."（p32）

> "Shortest path bridge VLAN: No spanning tree control; No source @mac learning of Customer (only BMAC); No flooding of unknown destination or multicast frames; Each B-VLAN calculates its own Shortest Path Tree; Control BVLAN carries IS-IS control packets. AOS support: 16 BVLANs."（p39）

> "Metric (link cost) lower = higher priority; Lowest Hop Count = higher priority; when equal: 16 predefined ECT algorithms, byte-by-byte XOR ECT-MASK. Up to 16 paths; head-end assignment of traffic."（p41-43）

## I · 方法论骨架

**① 拓扑层级选型（f08/p05）**

| | 3-tier | 2-tier |
|---|---|---|
| 核心 | 纯 BCB（只学 BEB 地址，no-touch） | 无 BCB，核心即 BEB |
| 汇聚/核心 | BEB（VLAN→I-SID 映射、IS-IS、PBB） | BEB 之间部分/全网状 |
| 接入 | 802.1Q on LAG，STP 或 DHL 上联 | 同左 |
| 冗余 | 双 BCB | VC 虚拟机箱多机箱 BEB |
| 适用 | 大型/需独立核心转发层 | 中小型扁平化省一层 |

远程站点可经 MPLS/VXLAN 域延伸 SPB。

**② IS-IS 控制面常数（可背）**
- 默认控制目的 MAC：`01:80:c2:00:00:14`；邻接类型 P2P 与 P2MP（p06）。
- 路径三特性：对称（往返同路）、同路（单组播同路）、RPFC 无环（基于源 BMAC 反向路径检查）（p07）。
- DIS 选举（P2MP）：最高接口优先级，平局取最高 BMAC；**无备份，重选约 3 秒**（p08/ce03）。

**③ BVLAN 六规则（p09/ce05）**：不跑 STP / 不学客户 MAC / 不洪泛未知与组播 / 每 BVLAN 独立 SPT / Control BVLAN 承载 IS-IS 控制 / **AOS 上限 16 个、推荐只规划 4 个**。Control BVLAN 可兼作带内管理网（BEB 与 BCB 均支持，管理路由可重分发进 IS-IS，p10）。

**④ ECT 选路三级决胜（f09/p11-13）**：metric 低者优 → 跳数少者优 → 16 个 ECT 算法（ECT-MASK 与路径各节点 BridgeID 逐字节 XOR，取最低路径 ID）。同一算法同管单播与组播（保证同构）；新建 BVLAN 自动分配下一个可用 ECT-ID（可改）；链路故障时依赖该链路的 ECT 被剔除、次低者接管（p43 示例：链路 1-4 故障 → ECT-1/ECT-3 出局、ECT-2 胜出）。流量由头端在最多 16 条等价路径间分配。

**⑤ 封装常数（p14）**：B-TAG EtherType `0x88a8`、I-TAG `0x88e7`；B-VID 12 位、I-SID 24 位（1-1600 万）；PCP 各 3 位。BridgeID = 2 字节优先级 + 6 字节系统 BMAC。

## A1 · 书中案例

p32-33 两版参考拓扑逐层给出角色与冗余手段；p43 用"链路 1to4 故障"演示 ECT 剔除与接管；p40 演示 Control BVLAN 带内管理子网把 NMS 路由引进 IS-IS SPB。

## A2 · 触发场景

- 拿到园区/城网需求做 SPB 拓扑设计（层级、冗余、BVLAN/ECT 规划）；
- 客户或评审问"SPB 凭什么满链路利用还无环"（ECT+RPFC 机制级回答）；
- 抓包排障：识别控制 MAC、分析路径对称性。
与相邻 skill 区分：服务面（SAP/封装业务/组播模式/QoS）走 `spb-edge-services`；机型规格上限走 `spb-license-spec-sizing`；防环兜底 LBD 的部署清单也在 edge-services。

## E · 可执行步骤

1. 按规模定层级：中小型 2-tier（核心 BEB 网状+VC 冗余），大型 3-tier（汇聚 BEB+核心 BCB 双机冗余）。
2. 规划 4 个左右 BVLAN（含 1 个 Control BVLAN 兼带内管理），为每个 BVLAN 分配 ECT-ID 实现多路分担；业务扩展全部走 I-SID。
3. 控制面校验：共享网段预判 DIS 归属并加固该节点；核对每节点 mesh 度不超机型 IS-IS 邻接上限。

## B · 边界与陷阱

- **BVLAN 上限 16、推荐 4**（ce05）：给每类业务/每条路径独立 BVLAN 的方案落不了地；ECT 16 路调优复杂度被教材一笔带过，实际收益有限。
- **DIS 无备份**（ce03）：P2MP 共享网段 DIS 是逻辑单点，故障重选约 3 秒中断；高可用敏感场景改 P2P 设计。
- **BVLAN 无 STP 兜底**（ce15）：骨干防环全靠对称同构 SPT+RPFC；SPB 域外部物理环（如经接入侧绕回）会放大成广播风暴，必须在接入端口显式启用 LBD（见 edge-services skill）。
- 讲"无环"时锚定 RPFC 机制，勿只说"IS-IS 算路所以无环"。

---
来源条目: f08, f09, p05, p06, p07, p08, p09, p10, p11, p12, p13, p14, ce03, ce05, ce15, g04, g05, g06, g07, g10, g12, g18, g27
