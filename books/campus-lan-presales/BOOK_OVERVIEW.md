# BOOK_OVERVIEW · Campus LAN Presales (DT00XPS281EN Edition 29)

> 教材: Alcatel-Lucent Enterprise Training Services, 2025-12 · 480 页 · 参训者指南
> 定位: ALE 园区网售前全科书 —— AOS 差异化特性 → 三大网管平台 → 方案设计与选型 → License 报价 → 全产品组合，一册打通"技术卖点→机型选择→商务下单"全链路

## 一、结构（书的骨架）

1. **Campus Network Solution 总览** (p8-48) —— AOS R8.9/9.0 新特性清单：弹性架构（DHL/VC）、SPB、ERP、智能织构 Ifab、统一接入、设备画像、安全
2. **AOS 关键差异化特性** (p49-181)
   - Part 1 弹性架构：DHL 双归属激活/激活、Virtual Chassis（含 remote stacking）、故障场景收敛数据
   - Part 2 SPB（售前版精要）+ ERP v2 环网（G.8032，<50ms）
   - Part 3 智能织构 Ifab、统一接入（UNP/AG/CP/BYOD）、设备画像（Device Profiling）、安全（MACsec/AppMon/NAC）
3. **园区网管** (p182-282)
   - Part 1 统一网管（OV2500/Cirrus/Terra 三平台定位）
   - Part 2 OmniVista Network Advisor（AI 运维伴侣：异常监测/一键修复/Rainbow·Teams 集成）
   - Part 3 统一接入管理（UPAM/Profiling）
4. **方案设计与选型** (p283-347) ★售前核心
   - 分层设计方法（2-tier/3-tier × Star/Ring/Tree/Mesh/Spine-Leaf 拓扑）
   - 机型×层级定位表（OS6360→OS9900 哪层能用谁）
   - 功能矩阵（VC/ISSU/SPB/DHL/ERP/Metro Ethernet/MPLS per model）
   - VC vs 物理机箱成本对比
   - 参考架构：SMB 一体化 / 紧凑核心 / 分布式环网 / 密集核心 / SPB 园区核心
   - **License 模型与报价**（WWPL 价格表结构、供货分级、折扣类别）
5. **产品组合全览** (p348-456) —— L2+ 可堆叠（OS2X60/6360）、L2/L3 可堆叠（6560/6570/6860N/6870）、高端模块化（6900/9900/10K），含端口/交换容量/PoE/价格层级
6. **视频监控插件** (p457-473) —— OmniSwitch Video Plugin（ONVIF 摄像机自动发现/组播优化）

## 二、解释（核心论点）

这本书本质是一本**"从需求到订单"的售前作业手册**：
- 技术章节不是教配置（那是售后 Bootcamp 的事），每节都收口到"这个特性在竞标时挡谁"——DHL 挡 Cisco 堆叠双活、SPB 挡 EVPN 复杂度、ERP 挡传输网环网专柜；
- 网管三件套（OV2500 本地/Cirrus 云/Terra 大企业）按"客户 IT 运维成熟度"分层推销，Network Advisor 用 AI 叙事加码续费理由；
- 设计章节给出**决策表驱动的选型法**：先定层级（接入/汇聚/核心/DC），再对功能矩阵筛机型，再套参考架构模板 —— 售前可照表复用；
- License 章把 ALE 商务规则（WWPL/EOS/Sales Category 折扣级/Standard-Extended-Contact 供货分级）摊开，让售前会自己查价、会算维护合约（PW/SP 编码规则）。

## 三、批判（局限与盲点）

- 产品数据（端口数/Mpps/价格层级）基于 Ed29 时点，换代快，投标前必须对最新 WWPL；
- 与 Bootcamp（DT00XTE220）特性章节重叠度高，本书增量价值集中在 p283-347 选型设计 + p348-456 产品组合 + License 流程；
- 竞品对比（Cisco/HPE/华为）几乎不出现，弹药要自己补；
- 视频监控插件章节较薄，无与物理安防平台（如 Genetec）对接细节。

## 四、应用（对售前的可执行价值）

- 客户给一张平面图/需求清单 → 用 p288-298 分层方法 + p300-303 机型定位表 15 分钟出架构草图；
- 报价请求 → p321-347 License 章 + WWPL 查询路径 + 维护合约编码规则，可直接生成 BOM 框架；
- 竞标技术分册 → p49-181 差异化特性 + p314-319 参考架构直接改写成分册章节；
- 客户问"为什么不做整机箱" → p303 VC vs Chassis 对比表。

## 五、术语速览（详词典见 GLOSSARY.md）

DHL（Dual Home Link 双归属）、VC（Virtual Chassis 虚拟机箱）、ERP（Ethernet Ring Protection G.8032 环网保护）、Ifab（Intelligent Fabric 智能织构）、UNP（Universal Network Profile）、AG（Access Guardian）、UPAM（统一认证）、AppMon（应用监测/DPI）、WWPL（WorldWide Price List）、Sales Category（折扣级）、ARO（After Receipt of Order 供货周期）
