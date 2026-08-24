---
name: spb-stp-migration-cases
description: 需要分阶段迁移方案（双域并行/STP 无中断割接）或调用教育/交通/政务三个成功案例做售前背书时使用。
source_book: DT00XPS279EN SPB Presales
---

# SPB 迁移方法论与成功案例弹药库

## R · 原文引用

> "IT CAN RUN IN PARALLEL WITH YOUR CURRENT DESIGN — SPB Domain (HVAC, Security), Legacy Domain (Desktop, Telephony), Phased migration."（p13）

> "Loops without SPBs are controlled by unique and independent STP instances. BEBs adjoining two loops are configured with two STP instances in Root Bridge and Next Best Root. A point-to-point SPB service is dedicated to transporting STP control... Several BVLANs will be included to allow several active paths to be maintained."（p123）

> "KEY HIGHLIGHTS: No service disruption during the transition; All links are used; Replacement of Spanning Tree protocols; Configuration of SPB access services at the edge only."（p124）

## I · 方法论骨架

**① 双域并行分阶段迁移框架（f06）**：网络划分为 SPB 域与 Legacy 域长期共存，按业务逐批搬迁（先 HVAC/安防等 IoT 流量，后桌面/语音），每步可回退——消除割接风险顾虑。与互操作三承诺构成"能共存 → 可分批"完整论证链。

**② STP→SPB 无中断施工法（f17/p36，Metz 工程细则）**：
1. 核心网先全部 SPB 化（该区域不再有 L2 环）；
2. 未迁移接入环各自跑独立 STP 实例自治防环；
3. 横跨两环的 BEB 配双 STP 实例（Root Bridge + Next Best Root）受控桥接；
4. 专门建一条点对点 SPB 服务传输 STP 控制帧；
5. 取消 transit VLAN（SPB 按服务映射），部署多 BVLAN 维持多条活跃路径。

**③ 案例论证三段式（f18）**：背景量化 → 痛点编号 → 收益分组（对应客户质疑）。三个案例各有侧重：

| 案例 | 行业 | 规模量化 | 弹药点 |
|---|---|---|---|
| Linköping 大学（c01） | 教育 | 书中未给型号/规模数字 | spine-leaf 改造 + 具名高管证言（"incredibly simple to configure and manage"） |
| 美国 NDOT（c02） | 交通 | 三层架构：NOC（OV2500）/光纤环 OS6900/加固 OS6860E、OS6865 | 路边网络企业级化、SPB to the edge、MTTR 下降 |
| 法国 Metz（c03） | 政务/智慧城市 | 80 栋楼、100km 自有光纤、200 交换机、100 AP、万级设备 L2 | 迁移零中断 + 痛点全清单（transit VLAN/集中 VRRP/大广播域） |

## A1 · 书中案例

Metz 是全书最完整叙事（p120-124）：p121 背景（都会区与市政厅共享 IT）、p122 五条编号痛点、p123 施工架构（即上方五步）、p124 收益归四组——带宽与稳定、时延与弹性、配置与监控简化、简单低影响迁移。NDOT（p118-119）是同模板的交通行业变体。

## A2 · 触发场景

- 客户担心"换网 = 割接风险"，需要分阶段迁移论证；
- 现网是 STP 多环环境，要出无中断迁移施工细则；
- 投标需要行业对标案例（教育/交通/政务任选其一做背书页）。
与相邻 skill 区分：只讲卖点不管迁移走 `spb-presales-battlecard`；选 EVPN/MPLS 走 `spb-vs-evpn-mpls-selection`；LBD/控制帧处置细节走 `spb-edge-services`。

## E · 可执行步骤

1. 迁移方案按双域并行框架写：SPB 域与 Legacy 域共存图 + 分批搬迁顺序表（IoT 流量先行）。
2. 现网含多环时套 Metz 五步施工法，明确"SPB 区域无环、遗留区域 STP 自治、交界点受控桥接、服务级搬迁"。
3. 案例背书按三段式模板选最贴近行业的案例改写，引用规模数字只用书中量化值，勿自行补数。

## B · 边界与陷阱

- **"替代 STP"≠全网灭 STP**（ce14）：教材自己的参考设计里接入交换机上行仍用 STP 或 DHL；Metz 迁移期还专门传 STP 控制。话术精确化为"核心/骨干消除阻塞链路、全链路利用"，否则验收时被质疑承诺兑现度。
- Linköping 案例书中无设备型号与规模数字，引用时勿编造。
- 三个案例均为早期欧洲/北美公共部门项目，缺超大规模场景佐证；面向大 DC 客户勿硬套。
- DHL 是书中出现但未展开的叫法，向客户解释时标注来源待确认。

---
来源条目: f06, f17, f18, p36, c01, c02, c03, ce14, g09
