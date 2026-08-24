---
name: spb-edge-services
description: 设计 SPB 服务接入面（SAP 封装、E-LINE 伪线、L2 控制帧处置、边缘 QoS、BUM 组播复制模式、LBD 防环）时使用。
source_book: DT00XPS279EN SPB Presales
---

# SPB 边缘服务面设计（SAP / QoS / 组播 / 防环）

## R · 原文引用

> "SAPs can only be created on access interfaces... Different encapsulation types on the same access port: Untagged, Tagged, QinQ. Multiple services for one CVLAN or one service for multiple CVLANs."（p54-55）

> "L2 Protocol Default Treatment: STP Tunnel; 802.1X Drop; 802.1AB Drop; 802.3AD Peer; GVRP Tunnel; AMAP Drop; MVRP Tunnel. Peer: interact with the peer switch. Drop: discards unconditionally. Tunnel: control packet encapsulated across the SPB network."（p63）

> "Traffic is classified at the SAP level... No further classification within the SPB backbone due to MAC-in-MAC encapsulation. Trusted SAPs: Tagged traffic priority derived from tags. Untrusted SAPs: Set the CoS marking to a user-defined value."（p64）

> "SPB supports two BUM traffic distribution methods: Head-End (native mode); Tandem (optimized). Head-End: one copy of each packet is sent to each BEB where the ISID exists. Tandem (S,G): more bandwidth-efficient."（p65-69）

## I · 方法论骨架

**① SAP 创建与封装（p16/p17）**
- 硬约束：SAP 只能建在 access 角色接口（物理口或 LAG）。
- 同一口可混用 Untagged / Tagged / QinQ；映射弹性：一 CVLAN 多服务，或多 CVLAN 合一服务。
- 动态 SAP 由 UNP profile 认证派生（见微分段 skill）。

**② L2 控制帧三态处置（f10/p19）**

| 协议 | 默认 | 三态含义 |
|---|---|---|
| STP / GVRP / MVRP | Tunnel | 封装透传过 SPB，两端无感知 |
| 802.3AD (LACP) | Peer | 边缘与对端正常交互协议 |
| 802.1X / 802.1AB (LLDP) / AMAP | Drop | 无条件丢弃 |

设计法：每个 SAP 关联 L2 Profile，按"该协议应透传/拦截/终结"逐项决策。

**③ 边缘 QoS 决策矩阵（f11/p20）**：分类只在 SAP 入口一次，骨干因 Mac-in-MAC 零再分类。Trusted 沿用报文标签 CoS（untagged 用端口默认优先级）；Untrusted 由管理员强制改写。特例：经 Tunnel 透传的 L2 控制 BPDU 恒定最高优先级。

**④ BUM 组播复制模式（f12/p21/p22）**

| 模式 | 机制 | 判据 |
|---|---|---|
| Head-End（默认） | 入口 BEB 对每个远端 BEB 各复制一份、走单播树 | 接收端稀疏、组播带宽低 |
| Tandem (S,G) | 每 I-SID 每源建源树（组 BMAC） | 带宽敏感，省带宽 |
| Tandem (*,G) | 每 BVLAN 共享树、最低 BridgeID 作根 | 资源敏感，省表项 |

第三维度：服务级 IGMP snooping 开启后只复制给有 IGMP 客户端的 SAP/SDP。

**⑤ E-LINE 伪线特性（p15）**：两 SAP 间透明电路、SAP 不学源 MAC、组播固定 Head-End、无洪泛复制。**⑥ LBD 环路检测（p23）**：无需 STP，周期发探测帧；判定：同机关最高 PortID 口，跨机关最高 BridgeID 机上的口；动作：shutdown/Trap/日志/定时或手工恢复。

## A1 · 书中案例

p55 示例：VLAN 10/20/30/31/32 分别映射 Service 1000/2000/3000，演示同口多封装混用；p67-68 演示 IP 组播优化开/关前后 BUM 洪泛范围差异；p65 表明 Head-End 是 AOS 原生默认，视频类业务必须显式改 Tandem。

## A2 · 触发场景

- 做 SPB 业务接入设计：SAP 封装规划、遗留控制协议透传决策、边缘 QoS 定型；
- 视频监控/IPTV 等组播密集业务的复制模式选型；
- 排障"链路通但 802.1X/LLDP 认证或邻接建不起来"（默认 Drop 所致）；
- 混合组网开局防环清单（LBD）。
与相邻 skill 区分：骨干拓扑/BVLAN/ECT 走 `spb-topology-isis-design`；L3 路由叠加走 `spb-l3-integration`；机型容量上限走 `spb-license-spec-sizing`。

## E · 可执行步骤

1. 逐 SAP 列三张表：封装（Untagged/Tagged/QinQ + VLAN 映射）、控制帧处置（Tunnel/Drop/Peer）、QoS 信任模式（Trusted/Untrusted + CoS）。
2. 按业务选 BUM 模式：两点透明互联用 E-LINE；稀疏组播 Head-End + IGMP snooping；密集组播 Tandem（带宽紧选 S,G、表项紧选 *,G）。
3. 开局启用 LBD（桥口+业务接入口），配自动恢复定时器与告警，列入标准开局清单。

## B · 边界与陷阱

- **默认 Drop 静默吞包**（ce10）：802.1X/LLDP/AMAP 默认丢弃，远端设备互联时表现为"链路通但协议不通"；需跨 SPB 传 STP 控制时学 Metz 做法——专门建一条点对点 SPB 服务承载。
- **骨干不能二次 QoS 分类**（ce09）：入口标记混乱 = 全网 QoS 失真且核心无法补救；接入侧先统一 802.1p 规范再上 SPB。
- **Head-End 带宽放大**（ce04）：接收者多或组播流量大的 I-SID 用 Head-End 会随节点数线性放大，视频类直接打爆骨干；且不开 IGMP snooping 时 IP 组播洪泛所有 SAP/SDP。
- **伪线不是普通交换口**（ce12）：E-LINE 不学源 MAC、无 Tandem 选项，依赖源 MAC 学习的统计/定位手段失效；要完整 L2 行为改用 E-LAN。
- BVLAN 无 STP 兜底，不开 LBD 遇外部物理环即广播风暴（ce15）。

---
来源条目: f10, f11, f12, p15, p16, p17, p19, p20, p21, p22, p23, ce04, ce09, ce10, ce12, g03, g08, g11, g15, g16, g20, g28, g29, g33, g34, g37
