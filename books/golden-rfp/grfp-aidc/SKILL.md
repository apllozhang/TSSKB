---
name: AI 数据中心 Golden RFP 精粹（RoCEv2 无损以太网/自适应路由/8 卡 GPU 服务器/Clos 与 Rail 优化拓扑/双 NOS）
description: 投标或方案设计 AI 训练集群、GPU 数据中心网络时使用：ALE AI-DC Golden RFP（v1, 2026-05, Phase 2）的核心需求——后端计算 fabric 的无损 RoCEv2 与亚毫秒硬件链路倒换、OC8100 GPU 服务器规格、51.2T/25.6T Spine 与 Leaf 交换机参数、前端 EVPN-VXLAN 多租户、双 NOS（ASON/AOS-X）与 OmniVista Orchestra 编排，含 C/PC/NC 应答硬规则。
source_book: Alcatel-Lucent AI DC Solution Golden RFP v1
---

## R(何时用)
- 投标智算中心 / GPU 集群网络项目，需要逐条应答 AI-DC 需求
- 设计后端训练网 + 前端存储网 + 带外管理网三网架构
- 选型 GPU 服务器与 400G/800G 交换机并解释"为什么必须无损以太网"

## I（核心理念）
AI 负载的流量模型与传统 DC 根本不同：all-reduce / all-gather / all-to-all 集合通信在 GPU 间产生同步大突发，"A small number of slow or congested flows is sufficient to stall an entire training job"，作业完成时间 JCT 取决于尾延迟和丢包行为而非平均吞吐（Introduction）。由此推出五条设计铁律：① RoCEv2 无损以太网；② 自适应路由 + 动态负载均衡防哈希极化；③ ASIC 内硬件链路倒换（检测后 <1ms，不惊动控制面）；④ 可编程带内遥测 INT 诊断尾延迟；⑤ 三网分离——backend 计算 / frontend 存储+通用 / OOB 管理，单编排平台统管。

方案构成：OmniCompute OC8100 GPU 服务器（AMD 8×MI325X）；前端用 OS6920-D32 与 OS6900 系列；后端用 OS7900 系列（ONIE 出厂，可装 ASON=ALE SONiC 或 AOS-X）；管理网用 OS6900-T48C6；编排用 OmniVista Orchestra（本地部署，原生管 SONiC/AOS-X 交换机与 GPU 服务器）。

## A1（决策要点）
1. **Spine 档位**：51.2 Tbps（2RU，64×OSFP800 800G，5nm 单 die）vs 25.6 Tbps 400G（64×QSFP56-DD，Tomahawk 4 级，投资保护渐进迁移）。
2. **Leaf 档位**：25.6 Tbps（32×OSFP800 ToR 直连 GPU 400G NIC）vs 12.8 Tbps 400G（32×QSFP-DD，650ns 时延，850k IPv4 ALPM / 8192 VRF）。
3. **拓扑双选**：classic Clos vs rail-optimized，投标方须两种都给 BOM、线缆清单与收敛比（Solution-level req #7）。
4. **NOS 双轨**：back-end 必须是 hardened SONiC 发行版（SAI 硬件抽象层）+ 同硬件上的专有 NOS 并行可选；front-end 用单一容器化专有 NOS。NOS 架构要求为"容器化单体 OS 不可接受"。
5. **规模验证点**：8 GPU 单机柜试点 → 256 GPU 八机柜生产 pod，两个规模点都要 BOM 与布线图（req #11）。

## A2（细节速查表）

**解决方案级硬指标**（Solution-level requirements）
| 条目 | 要点 |
|---|---|
| #2 | 后端支持 RoCEv2 无损传输（InfiniBand Spec Vol.1 Annex A17 定义） |
| #3 | 所有 GPU-GPU 路径 cut-through 转发 |
| #4 | 硬件 DLB 按 egress queue 配置，依据实时端口负载+队列占用重平衡 |
| #5 | 硬件链路倒换 link-down 检测后 <1ms 重导向，无需控制面收敛 |
| #6 | 数据面可编程 INT：line-rate 导出 per-packet/per-flow 记录、片上触发器（队列深度阈值/ECN 标记/丢包），免外置探针 |
| #9 | 管理网独立 L2/L3 网络，仅承载 BMC/串口集中器/编排流量 |
| #15 | 全部交换机双风道 SKU（front-to-back port intake / back-to-front port exhaust） |
| #16 | 电源热插拔负载分担，同机箱兼容 AC 或 HVDC 输入 |

**GPU 服务器（OC8100）关键参数**（AI compute server 章）
| 参数 | 数值 |
|---|---|
| 形态/散热 | 8RU 风冷，AMD MI325X×8（OCP OAM 规范） |
| 显存 | 每 GPU ≥256GB HBM3e、带宽 ≥6TB/s，整机 2TB |
| Scale-up | 8 卡全互联 coherent fabric，任意两卡 ≥128GB/s 双向，每卡 7 条点对点链路 |
| 算力 | FP32 163 TFLOPS / FP16 1300 / FP8 2610（GPU 厂商公布基准） |
| Scale-out | 8×单口 400G QSFP112 NIC（一 GPU 一口，rail 优化拓扑），NIC 硬件 RoCEv2/PFC/ECN |
| 前端 | 2×双口 200G QSFP112 |
| 主机 | 2×x86（≥64 核/路、3.3GHz、400W TDP）、≥1.5TB DDR5-5600 ECC |
| 电源/散热 | 6×3300W 钛金 PSU 4+2 冗余、15 个 N+1 风扇模组 |
| 管理 | 独立 BMC（开源固件，SOL/Redfish/IPMI 2.0）+ 专用 1G RJ45 |
| 环境 | 10–35°C（ASHRAE A2）、峰值 ≤10kW/机柜位、实际工作 6–8kW |

**51.2T Spine 代表条目**：64×OSFP800（每电 lane 100G PAM4），breakout 至 2×400G…8×50G；单片 5nm die、全双工非阻塞 51.2Tbps；自适应路由+DLB per queue+GLB 跨 spine，per-flowlet 硬件决策；VXLAN RIOT（同口路由+桥接）line-rate；端到端拥塞控制 PFC(802.1Qbb)/ECN(RFC3168)/DCQCN/HPCC 免外置控制器；SyncE(G.8262)+PTP 1588v2+1PPS/10MHz/ToD 面板接口；硬件 e-fuse 保护笼位；≤44×64.92×8.7cm / ≤22kg；jumbo 9416 字节。

**公共软件基线**（Common switch software features，前后端 NOS 各答一遍）：容器化模块化 NOS + SAI 抽象；**PFC watchdog 防 PAUSE 死锁自恢复**（原文警告无 watchdog 会 "permanent fabric stall"）；ECN per queue/port 统计经 streaming telemetry 导出；WRED；8 硬件队列 SP/DWRR；EVPN 需同时支持 Type 1/2/4/5 路由（只有 Type 2 视为 NC）；anycast gateway 对称 IRB；ESI 多归属 active-active；ARP/ND suppression；BGP Unnumbered 免逐链路配 IP；ECMP hash key/hash seed 可配置抗极化；REST API 必须 YANG/OpenConfig 或文档化 JSON schema，"Read-only CLI scraping is not acceptable"；Management VRF 与业务转发隔离。

## E（场景案例/怎么用）
- 客户问"为什么 leaf 到 spine 要 800G"：引 leaf ToR 直收 GPU 400G scale-out NIC 上行，引 OC8100 规格 8×400G 表项。
- 标书评审答"空白判负"提醒：本卷明确 blank/dash/"see datasheet"=NC，响应表务必逐格填。
- 写无双 NOS 方案的差距说明：SONiC 硬化发行版要求属 back-end 强制条目（req #13），缺则至少 PC 并写清替代路径。

## B（限制与坑）
- 版本：v1（2026 年 5 月），基于 AI-DC Offer Phase 2；Datasheets 一节写明"Links to be added once published"，引用数据表前要找正式发布链接。
- Solution-level 表里 #18 出现两次（电源线 IEC C19/C20 与编排平台无损以太网 GUI/REST 配置），引用编号时注意原文编号重复。
- GPU 型号锁定 AMD MI325X 生态（Infinity Fabric 互联）；对标 NVIDIA 生态需求需另行论证，不能直接标 C。
- 温度参数分风道方向（FtB 0–40°C / BtF 0–35°C 等），机柜布局设计要先定风向再定温区。
- 文中个别小节标注"该要求适用于前后端两套 NOS 且要各答一遍"，容易漏答一半。

来源：Alcatel-Lucent AI DC Solution Golden RFP v1（sources/grfp-aidc.md，全文约 1100 行）
