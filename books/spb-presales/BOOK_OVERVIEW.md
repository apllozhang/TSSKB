# BOOK_OVERVIEW · OmniSwitch LAN SPB Presales (DT00XPS279EN Issue 05)

> 教材: Alcatel-Lucent Enterprise Training Services, 2025-02 · 147 页 · 参训者指南
> 定位: 售前工程师的 SPB（最短路径桥接）技术推销课 —— 为什么卖 SPB、SPB 怎么工作、怎么跟 OV2500 一起交付、有哪些成功案例

## 一、结构（书的骨架）

1. **Why SPB?** (p5-19) —— 卖点总动员：瑞士军刀定位（STP 替换/多租户/微分段/IoT）、全产品线覆盖、非 IP 转发更安全、互操作向后兼容、自动化三件套（auto backbone/services/attachment）、可与现网并行渐进迁移
2. **SPB Mac-in-Mac** (p20-44) —— 架构与控制面：IEEE 802.1aq/PBB 组件（BEB/BCB/BVLAN/I-SID/SAP/SDP）、IS-IS 邻接与最短路径树、ECT 16 等价树算法、2-tier/3-tier 拓扑设计
3. **SPB Data Plane** (p45-77) —— 802.1ah 封装字段、服务模型（E-LAN/E-LINE 伪线）、静态/动态 SAP（UNP 联动）、VLAN 翻译、L2 Profiles、SAP QoS（trusted/untrusted）、组播复制（Head-End vs Tandem S,G / *,G）、LBD 环回检测、机型规格表
4. **SPB Layer 3 Services** (p78-98) —— 三种 L3 集成方式：Outline 物理环回线 / 前面板口 inline / service-based 单遍 inline；VPN-Lite（VRF+静态/OSPF over ISID）与 L3 VPN（ISIS TLV 传路由、GRT、ISID-per-VRF），附完整 AOS 配置样例
5. **OV2500 SPB Provisioning** (p99-113) —— 服务创建/监控/L2 Profile/SPB Profile/拓扑视图
6. **成功案例** (p114-125) —— Linköping 大学（spine-leaf 改造）、美国 NDOT（路边网络 SPB 到边缘、环网+加固型）、法国 Metz（80 栋楼 STP→SPB 无中断迁移）
7. **OmniFabric Overview** (p126-140) —— SPB/EVPN/MPLS 三技术一张表定位对比 + 机型支持矩阵 + 按行业用例选技术

## 二、解释（核心论点）

这本书的 persuasion 逻辑是一条完整的售前攻防线：
- **对抗性开场**：用 STP 的四大罪（次优路径/阻塞浪费带宽/逐跳配置/慢收敛）引出 SPB 的对称同构无环最短路径；
- **安全性叙事**：Mac-in-Mac 封装让核心不学客户 MAC、非 IP 转发天然免疫 IP 扫描/DOS/中间人 —— 把"老技术 Ethernet"包装成"安全优势"；
- **降本叙事**：单协议（IS-IS 同时管 L2+L3/IPv4+IPv6）、边缘-only 配置（核心零触碰）、与 802.1Q/QinQ/OSPF/BGP 互操作可分阶段迁移 —— 每一条都在回应 CIO 的预算质疑；
- **L3 章节是"消灭独立路由层"的论证**：BEB 同时当桥和路由器，VPN-Lite 简版到 L3 VPN 全版给了两档选择；
- **OmniFabric 章是技术中立防御**：当客户指定 EVPN/MPLS 时，ALE 用"同一 AOS 全支持"化解厂商锁定质疑，同时用对比表（SPB 培训成本低/协议开销低/排障快）把天平拉回 SPB。

## 三、批判（局限与盲点）

- 全书对 SPB 的宣传未提规模上限的实操代价：16 个 BVLAN、ECT 调优的实际复杂度被一笔带过；
- 成功案例全是 2020 年前的欧洲/北美公共部门，缺少超大规模数据中心场景（该书自己也承认 DC 用 EVPN）；
- L3 VPN 配置样例基于 OS6900/9900 高端机型，中低端机型（6860N 等）service-based inline 支持矩阵需要查最新 AOS 规格书；
- OV2500 章节是 GUI 截图导览，无故障排查深度（那是售后课 DT00WTE323 的事）。

## 四、应用（对售前的可执行价值）

- 客户问"为什么要换掉 STP"→ 用 p7-17 卖点弹药库 + p23 STP vs SPB 对比页；
- 客户问"SPB 和 EVPN/MPLS 怎么选"→ p134 对比表 + p138 行业用例矩阵直接成单页输出；
- 投标需要 L3 方案 → p79-97 三种路由集成方式 + 配置样例可转技术方案书章节；
- 案例背书 → p114-125 三个故事各有侧重（教育/交通/政务）。

## 五、术语速览（详词典见 GLOSSARY.md）

BEB/BCB（边缘桥/核心桥）、BVLAN（骨干 VLAN，AOS 支持 16 个）、I-SID（24 位服务实例标识）、SAP/SDP（UNI/NNI 逻辑端口）、ECT（等价树算法，16 个）、PBB/Mac-in-Mac（802.1ah 封装）、VPN-Lite / L3 VPN（两种 VRF over SPB 模式）、Head-End/Tandem（组播复制模式）、OmniFabric（SPB+EVPN+MPLS 统一织物品牌）
