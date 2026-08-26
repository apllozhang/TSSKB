---
name: 轨交骨干架构选型（环网拓扑/OCC-BCC/L2 对比 L3 VPN/站点双归/规格表）
description: 设计轨交 SPB 骨干网总体架构时使用：环网为天然冗余拓扑、OCC/BCC 双中心、集中式与分层控制、L2 VPN 与 L3 VPN 两种站点架构的取舍（VLAN/ISID 本地化、hairpin、VRRP 网关）、站点双归两种方式对比，以及 ISID/FDB/L3 规格对各设计的约束。
source_book: Transportation Networks Design Guide & SPB-based Transportation Networks Design Guide
---

## R（何时用）
- 新线或改造线的骨干网架构设计：定拓扑、定控制中心、定每站架构（L2 还是 L3）
- 评估网络能扩展到多少车站/终端，选型核对 ISID/FDB/L3 规格
- 双中心（OCC/BCC）与站点双归方案比选
- 评审别人方案里 VLAN/ISID 的规划方式是否可扩展

## I（核心理念）
环是沿线路冗余互联节点的天然拓扑，OCC 为主控中心、BCC 为灾备，二者可主主或主备（通用版 p18-19）。站点架构二选一：L2 VPN 把站点 VLAN 1:1 映射 ISID，全网 VLAN 数受 OCC/BCC BEB 的 ISID/FDB/ARP 规格封顶；L3 VPN 在站点 BEB 做 VRRP 网关，站点接入 VLAN 仅本地有效，只有共享的上行 VLAN 映射 ISID，路由靠 IS-IS 特殊 TLV 随骨干自动扩散，不需要额外路由协议——IP 可汇总、MAC 不可汇总，所以 L3 天然更可扩展（通用版 p21-24）。站点接入网双归到两台不同 BEB 消除单点，两种做法：同站双 BEB（多花设备、省光纤、运维简单）与本地+远端 BEB（省设备、多光纤、运维复杂）（通用版 p24-25）。

## A1（决策要点）
1. 拓扑默认环形：多线运营时先定控制架构——集中式（所有线归一个 OCC）或分层式（线路中心+总控）（通用版 p19-20）
2. L2/L3 站点架构选型：小规模、每站 VLAN 少可 L2；追求车站数量与终端数量扩展性选 L3 VPN（通用版 p24）
3. L3 设计三件套：站点 BEB 组成 VRRP 对当默认网关；接入 VLAN 只在本地有意义；上联 VLAN 全站共享并经 hairpin 映射 ISID，hairpin 端口速率须不低于骨干 NNI（通用版 p23-24）
4. 双归方式按"设备预算 vs 光纤芯数 vs 运维能力"三角权衡（通用版 p24-25）
5. 规格核查顺序：L2 设计查 OCC/BCC 节点的 ISID 数、FDB、ARP（全网终端 MAC 都落在那两台）；L3 设计只需查各 BEB 本站规模（通用版 p26-28）
6. 规模大时骨干才上 SPB，站点接入网用传统以太网（STP/ERP/LAG），非所有节点都要 SPB（通用版 p26）

## A2（细节速查表）

| 维度 | L2 VPN 设计 | L3 VPN 设计 | 页码 |
|---|---|---|---|
| 路由位置 | 全部在 OCC/BCC（VRRP 对） | 站点 BEB（VRRP 对）当默认网关 | 通用版 p21/p23 |
| VLAN 语义 | 站点 VLAN 全局有效，1:1 映射 ISID | 接入 VLAN 仅本地有效；上联 VLAN 全站共享映射 ISID | 通用版 p21/p23 |
| ISID 消耗 | 每站每 VLAN 一个，受 OCC/BCC ISID 规格封顶 | 每系统一个，数量极小 | 通用版 p26-27 |
| MAC/FDB | 全网终端 MAC 集中在 OCC/BCC BEB | MAC 只在本站内已知 | 通用版 p27 |
| 路由/ARP | 路由与全部终端 ARP 集中 OCC/BCC | 每站 BEB 携带本站 ARP；VRF 存在于每台 BEB | 通用版 p28 |
| 路由协议 | — | VRF 路由经 IS-IS TLV 扩散，无需附加协议 | 通用版 p24 |

| 规格（SPB 机型） | OS10K | OS9900 | OS6900 | OS6860 | OS6865 | 页码 |
|---|---|---|---|---|---|---|
| ISID | 1K | Future | X20/X40/T20/T40:1K；X72/Q32:8K | 2K | 2K | 通用版 p27 |
| FDB | 32K/槽 | 128K/槽 | X20/X40/T20/T40:128K；X72/Q32:228K | 48K | 48K | 通用版 p27 |
| L3 表 | 16K（U32S:12K） | 512K | 16K/12K | 64K | 64K | 通用版 p28 |
| ARP 表 | 16K/8K | 24K | 8K-48K | VC 取最低 16K | 16K | 通用版 p28 |
| VRF | 64 | 64 | 64 | 64 | 64 | 通用版 p28 |

## E（场景案例）
- 17 站轻轨+OCC+BCC 的环网参考拓扑（通用版 p19）
- L3 VPN hairpin：上联 VLAN 走 hairpin 一侧做路由、SAP 一侧进 SPB，站点接入 VLAN 与 BVLAN 同跑在两台 BEB 互联链路上（通用版 p23-24）
- 站点内双 BEB 双归 vs 本地+远端 BEB 双归的设备/光纤/运维三维对比（通用版 p24-25）
- L2 设计因 OCC/BCC 节点 ISID/FDB/ARP 三张表同时见顶而扩展受限的推导（通用版 p26-28）

## B（限制与坑）
- L2 设计把全网 VLAN/ISID 都开在 OCC/BCC 两台节点上——车站数、终端数双双被规格卡死（通用版 p26-28）
- 多站共享 VLAN/ISID 的 L2 方案：BUM 流量与组播复制开销爆炸，明确不推荐（通用版 p21、p38-39）
- hairpin 端口速率低于骨干 NNI——上行方向成瓶颈，属硬性要求（通用版 p24）
- 通用版文档内嵌的评审批注指出：VLAN UNI 型 hairpin 的官方支持性、"支持多少 SPB 节点"的官方口径当时均未定论，落地前须向 ALE 确认（通用版 p24、p26）
- 双归多 BEB 带来成环风险，必须配套防环方案（见 transit-attachment 单元）（通用版 p25）

## 来源
Transportation Networks Design Guide（p18-28）+ SPB-based Transportation Networks Design Guide（p12-20，内容基本对应）
