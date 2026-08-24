# DIGEST · Campus LAN 售前精华（不读全书版）

> 原书：DT00XPS281EN Campus LAN Presales, Edition 29, 2025-12, 480 页
> 这篇长文把全书压缩成"一页看懂 + 七步工作法 + 两张速查表 + 三坑警示"，读完可直接上手接待客户。

---

## 一、一页看懂 Campus LAN 售前

这本教材解决一个问题：**客户给一张平面图或需求清单，你如何在半小时内变成可投标的架构图 + 机型 BOM + 报价框架**。

全书六章，真正的主干是三段：

1. **技术卖点（p49-181）**——每节都收口到"这个特性在竞标时挡谁"：DHL 挡 Cisco 堆叠双活、SPB 挡 EVPN 复杂度、ERP 挡传输网环网专柜；
2. **设计选型（p283-347）**——决策表驱动：先定层级，再对功能矩阵筛机型，再套参考架构模板（p288-298 分层方法 + p300-303 机型定位表，15 分钟出草图）；
3. **License 报价（p321-347）**——WWPL 价表结构、供货分级、折扣类别，让售前自己会查价、会算维护合约。

网管三件套（OV2500 本地 / Cirrus 云 / Terra 大企业）按客户"运维成熟度 × 数据驻留"分层推销，Network Advisor 用 AI 叙事加码续费理由（p240-246）。产品组合全览（p348-456）是查数用的字典，不必通读。

一句话：**这是"从需求到订单"的售前作业手册，教选型判断和商务规则，不教配置命令**（配置是售后 Bootcamp DT00XTE220 的事）。

---

## 二、从需求到 BOM 的七步工作法

11 个 skill 串起来就是一条完整的售前作业流水线：

**第 1 步 · 分层设计**（`campus-design-tiering-and-ha`）
二维定位法：架构轴（2-tier 时延 1.5-6µs vs 3-tier >12µs，p289-291）× 拓扑轴（Star/Tree/Ring/Mesh/Spine-Leaf/POD，p288）。单楼宇要低时延选两层，多楼宇要分段扩展选三层。同时按六方案横比定冗余技术路线。

**第 2 步 · 高可用路线**（同上，细节分流到 `dhl-erp-ring-protection`）
判 SLA：要求 50ms 电信级 → ERPv2（环周长 <1200km、节点 <16 前提下，p122-128）；接入双活不要堆叠 → DHL；多租户核心 → SPB。SPB 约 300ms 收敛，别拿去应时敏标（ce07）。

**第 3 步 · 机型定位**（`omniswitch-model-selection`）
三张表按序过：p300 层级定位表（Yes/No 铁律）→ p301 功能矩阵（招标硬条款逐条映射，带 ** 的记下待补 license）→ p357 组合定位图。容量常数背参数（6860N 758.9Mpps/1.02T，6870 1488Mpps/2T，6900 6.4T，9900 25.6/51.2T）。核心层做 VC vs 机箱对比（p303）。

**第 4 步 · 功能矩阵筛机型**
SPB 从 6560/E 起步（需许可）、MPLS 仅 6860N/6870/6900、ISSU 仅 6360-24/48 及以上；DHL 机型支持看 p301 矩阵而非 p54 宣传口径（矛盾点，下文详）。堆叠设计（台数/VFL/防脑裂）细化为设计页（`virtual-chassis-design`，p59-74）。

**第 5 步 · 套参考架构模板**（`campus-reference-architectures`）
四大模板 + 垂直案例（p296-319）：SMB 一体化 / 紧凑核心（VC）/ 分布式环网（ERPv2+DHL）/ 密集核心（9900），外加多千兆无线边缘、双核心、城域、DC POD。判定信号对号入座，改端口出图，30 分钟出 BOM 骨架。

**第 6 步 · 网管与安全配套**（`nms-platform-and-network-advisor`、`security-unified-access`、`ifab-zero-touch-automation`、`video-surveillance-design`）
网管两问定平台：数据能不能出域？有没有运维团队？准入安全用 Access Guardian 四环节（认证→分类→角色授权→限制阻断，p147），卖点是"内建交换机、不要独立 NAC 盒子"；哑终端用画像闭环（指纹→类别→UNP 自动下发）。分支无人运维场景叠 iFab 零接触（注意 8.10R2 起改 opt-in，p137）。

**第 7 步 · License 报价出 BOM**（`license-wwpl-pricing`）
BOM 五件套：整机型号 / 电源 / 堆叠接口线缆光模块 / 软件 License / 电源线。后缀规则：-ZZ 不含电源线、-00 不含电源（p328）。功能矩阵带 ** 的项忘加 license 等于不支持，构成应标偏离。

---

## 三、机型速查表

| 机型 | 层级定位（p300） | 关键能力 | 适用场景 |
|---|---|---|---|
| OS2260 | 入门接入 | 无堆叠、80.4Mpps、2 条静态路由；不在美国销售 | 微型办公室、哑终端接入 |
| OS2360 | 入门接入 | 可堆叠、133.9Mpps、10G 上联；不在美国销售 | 小型接入 |
| OS6360 | 接入 | 208Mpps/140G；VC 4 台（24/48 型）；MACsec 免费 | 标准千兆 PoE 接入 |
| OS6465 | 接入（加固） | 131Mpps/176G；PROFINET Class B；VC 仅单机 | 工业加固场景 |
| OS6560/E | 接入+汇聚 | 241Mpps/324G；SPB 需许可；多千兆 Z 型 | Wi-Fi 6 多千兆边缘、汇聚 |
| OS6570M | 接入+汇聚 | 210Mpps；Metro Ethernet 内置 | 城域/园区汇聚 |
| OS6860N | 接入+汇聚+核心 | 758.9Mpps/1.02T；VC 8 台远程堆叠；95W PoE；AppMon | 多千兆无线边缘、中型核心 |
| OS6870 | 接入+汇聚+核心 | 1488Mpps/2T；8 台 VC 混搭；VXLAN EVPN（PRM 许可） | 紧凑核心、高规格汇聚 |
| OS6900 | 汇聚+核心（不做接入） | 6.4T；6 台 VC mesh；MPLS | 园区核心、DC POD |
| OS9900（9907/9912） | 汇聚+核心 | 25.6/51.2T；9907 双机 VC；GNI 板可接入 | 密集核心、超大园区 |

容量数字均基于 Ed29 时点（p300-303、p357、p443-444），投标前对最新 datasheet。

---

## 四、高可用方案对比一页表（p129）

| 方案 | 带宽利用率 | 交换机冗余 | 统一管理 | 定位 |
|---|---|---|---|---|
| **VC（官方 preferred）** | 100% | 有 | 有 | L2 主主首选 |
| STP | 50% | 无 | 无 | 兜底 |
| LACP | 100% | 无 | 无 | 纯链路聚合 |
| DHL Active-Active | 100% | 有 | 无 | 接入双归（不堆叠也能双活） |
| ERPv2 环网 | 100% | 有 | 无 | 环拓扑，<50ms 电信级 |
| SPB | 100% 全链路 UP | — | 无 | 核心层多租户，~300ms |

选型口诀：L2 双活默认推 VC；客户拒绝堆叠则 DHL；光纤成环要 50ms 则 ERPv2；多租户大网核心则 SPB。VC 最大单点风险是脑裂，方案必预置 RCD 或 VCSP 防裂机制之一（p71-74）；无 EMP 口机型做 RCD 须加指定 USB 适配器（ASIX 8817 / RTL8153），售前最易漏配。

---

## 五、报价三坑与规则（p326-346）

**坑 1 · WWPL 三坑（ce13）**：①升级件（UPG/U SKU）不打折；②价格随时可变不另行通知，旧价目表报价可能废标或亏本——每月从 MyPortal 拉当月 WWPL（含 Addendum）；③Contact 级（已发布未上市）交期无期，标书写"交期待确认"。供货分级：Standard 2 周 ARO、Extended 4 周、Contact 须询 ALE。

**坑 2 · Sales Category 折扣级**：WWPL 每个条目带折扣级字母（A/B/C…/NA），实际折扣按合同或渠道伙伴确认，列表价 ≠ 成交价；USD/EUR 双币，报价前对当月表。

**坑 3 · Demo 与 MACsec 许可**：Demo license 仅 MPLS、每客户一次、30 天、节点上一跑 MPLS 即激活倒计时——实验室顺手敲命令就耗光唯一额度（ce12）。MACsec 站点许可 OS-SW-MACSEC 零费用但必须显式下单；8.6R1 起不装即禁用，升级步骤里必须排进 license 安装（ce11）。

另外两条防漏行：网管许可不吃 VC 的账（VC of 4 就是 4 个许可，ce15）；带 ** 的功能项（SPB/MPLS/AR/PRM/PERF）逐行加 license。

---

## 六、学习路径（11 个 skill 阅读顺序）

1. `campus-design-tiering-and-ha` —— 总纲：分层 + 高可用横比，其他 skill 都挂在它下面
2. `omniswitch-model-selection` —— 三张表选机型，与第 1 步配合作业
3. `campus-reference-architectures` —— 成品模板库，前两个学会后拿来就用
4. `virtual-chassis-design` —— VC 深挖：台数/VFL/防脑裂
5. `dhl-erp-ring-protection` —— DHL 与 ERPv2：50ms 承诺的条件
6. `spb-vxlan-core-fabric` —— SPB/VXLAN：多租户与 EVPN 应对
7. `security-unified-access` —— AG 四环节、UNP、画像、MACsec 端口表
8. `ifab-zero-touch-automation` —— 零接触自动化与 8.10R2 行为变更
9. `nms-platform-and-network-advisor` —— 网管三平台 + Advisor 报价
10. `license-wwpl-pricing` —— 商务收口：BOM 五件套与三坑
11. `video-surveillance-design` —— 垂直行业选修：安防弱电项目才读

前三步看完即可应付常规需求；4-6 是技术答辩弹药；7-10 是配套与商务；11 按项目类型选修。

---

## 七、边界与数据时效警示

- **Ed29 时点**：全书端口数/Mpps/价格层级基于 Edition 29（2025-12），产品换代快，投标前必须对最新 WWPL 与 datasheet。
- **原文矛盾点（引用需注版）**：
  - p59 对 OS6465 同时标 VC 8 台与 4 台（p22 称 4 台）；
  - p54 称"DHL 除 9900 全支持"，p301 矩阵 6570M/6900/9900 均 No——DHL 只按接入/汇聚层机型承诺；
  - p301 矩阵 9900 MPLS 标 No，p443/444 写 9907/9912 支持 MPLS（ce09）。
  冲突时一律以最新 datasheet/release notes 为准。
- **Roadmap 陷阱（ce14）**：6870 的 MPLS/SPB-MS/50G、9912 的 VC 属"硬件就绪软件未交付"，带星号特性不可承诺。
- **竞品盲区**：原书几乎不提 Cisco/HPE/华为对比，竞标弹药要自己补。
- **Terra 平台与视频监控细节**：OV Terra 容量/许可书中未展开（待确认）；视频监控章节（p457-473）无 Genetec 对接与 ONVIF 口径，投标前以 ALE 方案页核实。

---

*由 cangjie-skill 流水线从 DT00XPS281EN 蒸馏生成*
