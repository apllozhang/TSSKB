---
name: spb-ov2500-delivery
description: 用 OmniVista 2500 做 SPB 服务的图形化开通/监控/POC 演示，或排布"骨干一次配好、服务边缘增删"的配置工单分工时使用。
source_book: DT00XPS279EN SPB Presales
---

# OmniVista 2500 服务交付与配置分层

## R · 原文引用

> "SPB - SERVICE CREATION: Basic — Select/edit/add devices; UNP Profiling (Optional Steps); Advanced (if required); Service - Creation."（p104）

> "Control Plane (NNI ports) SPB Core level, On BEB + BCB. Data Plane (UNI ports) SPB Access level, Only on BEB. Services: UNP Access Port, UNP Profiles, Access Port SAP, Pseudo-wire, Service. L2 Profiles (optional), Loopback Detection (LBD) (optional)."（p73）

> "ISID - A service instance identifier... The valid range is 256 - 16777214. Tag Value - If the traffic is untagged, the SAP is created with 0 as the encapsulation value (for example, 1/12:0)."（p109）

## I · 方法论骨架

**① AOS 配置两层分单法（f13）**：把 SPB 配置拆成两张独立工单——
- **SPB Core level**（NNI 口，BEB+BCB 都配）：IS-IS 接口、BVLAN、Control BVLAN 等骨干控制面，一次配好基本不动；
- **SPB Access level**（仅 BEB）：静态/动态 SAP、UNP profile、伪线、服务，以及可选的 L2 Profile 与 LBD，日常增删只发生在这里。

**② OV2500 服务创建向导（f16）**：Basic 选设备 → UNP Profiling（可选）→ Advanced（按需）→ 创建。要点是"必选项最小化、可选项显式分层"，管理员不必一次面对全部参数。

**③ 四大功能分区（p100）**：服务配置（Service Configuration）/ L2 Profiles / 全局设置（先选交换机）/ OneTouch 模式。

**④ SPB Profile 模板（p109/p32）**：Tag/ISID/BVLAN/组播模式/VLAN 翻译一次定义多处套用。参数规则：**I-SID 有效范围 256-16777214**（避开 0-255 保留段）；untagged 流量 SAP 封装值记 0（如 1/12:0）；BVLAN 必须填已存在的骨干 VLAN。

**⑤ 监控面**：设备/SAP/SDP 三级信息表（SDP ID 由 OV2500 动态生成）、SPB 拓扑视图含 LACP 链路明细；服务参数含 Mcast Mode（Headend/Tandem）、VLAN Translation、VPN MTU 等。

## A1 · 书中案例

p100-112 全流程 GUI 演示：Global Settings 选交换机 → 创建服务（Tunnel ID/Service ID/BVLAN/Mcast Mode 等字段）→ 创建 L2 Profile（控制帧 Tunnel/Drop/Peer 三态选择）→ 服务监控三级表 → SPB Profile 模板 → 拓扑视图。售前话术落点："边缘只配一次、核心零触碰（No-touch core），GUI 全流程可视化"。

## A2 · 触发场景

- POC 或交付演示：用 OV2500 向客户展示 SPB 服务从创建到监控的全路径；
- 实施方案排配置工作量：按 Core/Access 两张工单表分工；
- 规划 SPB Profile 模板参数（I-SID 取值避开保留段）。
与相邻 skill 区分：控制帧三态、组播模式等参数的业务含义见 `spb-edge-services`；UNP 微分段机制见 `spb-micro-segmentation`；本 skill 只管"怎么配、在哪儿配、怎么演示"。

## E · 可执行步骤

1. 排配置工单：先排 Core level 清单（骨干一次成型），再排 Access level 清单（服务随需增删），与 edge-only 论证互为印证。
2. 建 SPB Profile 模板：定 Tag Value、I-SID（256-16777214）、BVLAN、组播模式、VLAN 翻译，多处复用。
3. 演示路径：Global Settings 选设备 → 服务创建向导（Basic/可选 UNP/按需 Advanced）→ 拓扑视图看 SAP/SDP/LACP 状态收尾。

## B · 边界与陷阱

- OV2500 章节是 GUI 导览，无故障排查深度（售后归 DT00WTE323 课程），勿拿它承诺排障能力。
- I-SID 取值避开 0-255 保留段；untagged SAP 记 0 是工具表示法，别当真实 VLAN 规划。
- 书中界面字段是 2025-02 快照，实际版本字段名与默认值以现场 OV2500 版本为准。

---
来源条目: f13, f16, p32, c12, g24
