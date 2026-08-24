# verified.md · 三重验证通过条目（阶段 1.5）

## 汇总

| 类型 | 候选 | 通过 | 淘汰 | 说明 |
|---|---|---|---|---|
| frameworks | 10 | 10 | 0 | 五步法/Underlay/Overlay/业务开通/IRB/RR/多归属/架构模型全过 |
| principles | 21 | 21 | 0 | 参数、RD/RT 公式、DF 算法、ESI 编码、版本边界全过 |
| cases | 9 | 9 | 0 | 3 个 Lab + 架构指南 + 课堂演示，CLI 均命中原文 |
| counter-examples | 9 | 8 | 1 | ce06 淘汰（V3 常识 + V1 引用系转述） |
| glossary | 28 | 28 | 0 | 免验保留 |
| **合计** | **77** | **76** | **1** | |

验证方法：对每条的 source_quote 关键片段在 `source/fulltext.md` 全文 grep 核对（V1），逐条评估可操作价值（V2）与独特性（V3）。抽查覆盖全部 49 条非 glossary 候选的引用片段，均能定位到对应页（个别为原文等价变体，如 p91 对比表实际为双列排版、p67 MTU 输出含对齐空格，语义一致）。

---

## frameworks（10/10 通过）

- **f01 EVPN 五步配置法总框架**（p59）——V1："EVPN CONFIGURATION STEPS – PART 1/5" 命中（全文 21 处步骤图贯穿 p59-149）；V2：全书实施总路线图；V3：AOS 特有的五段式课程主线组织。通过。
- **f02 Step1 Underlay 配置与路由选型**（p60）——V1："Spine nodes share a single AS"/"For BGP underlay use eBGP"/"Support for ECMP" 均命中；V2：选型+执行顺序；V3：eBGP underlay 的 AS 规划规则。通过。
- **f03 Step2 Overlay 四步流程**（p84）——V1："Load and enable BGP. Set the ASN..." 命中（两处）；V2：可直接照抄的配置序列+验证标准；V3：AOS CLI 套路。通过。
- **f04 Step3-5 业务开通三部曲**（p67/p69）——V1：三条 CLI 命中（17 处 evpn-ethernet-segment enable）；V2：三条命令开一条业务；V3：service↔VNI↔ETag 映射。通过。
- **f05 IRB 选型框架**（p91）——V1：p91 对比表逐行命中（"Ingress PE performs MAC and IP lookup"/"RT5 support mandatory" 等）；V2：非对称/对称决策表；V3：含 AOS 仅支持 host-based 非对称的实现边界。通过。
- **f06 MAC 学习与 Proxy ARP 三段流程**（p121-124）——V1："Route Reflectors re-advertised"/"ARP request for 10.2"/"Snoop IP by leaf 1" 命中；V2：控制面学习+ARP 抑制流程与验证命令；V3：纯控制面学习链条。通过。
- **f07 路由反射器架构**（p132/p136）——V1：N(N-1)/2 公式与 45 peerings 命中；V2：RR 部署框架+专属命令；V3：Spine 兼任 RR 的实践惯例。通过。
- **f08 多归属框架**（p141/p182）——V1：MULTIHOMING/all-active/single-active/LAG 防环均命中；V2：模式选型+机制链；V3：DF 选举+四特性+8.10R1 仅 single-active。通过。
- **f09 EVPN 总体架构模型**（p164-167）——V1：四痛点逐条命中（"Inefficient use of resources"/"Operational complexity and administrative tax"/"Traffic tromboning"）；V2：迁移论证与选型四收益；V3：痛点→VXLAN→控制面分层的完整论证链。通过。
- **f10 AOS 实现模型**（p184-185）——V1："Instantiating an ESI"/"ESI+ETag aware routes"/"on-demand model" 命中；V2：ESI 生成范围表（静态 LAG 须手工）；V3：AOS 私有增强四件套，全网独有。通过。

## principles（21/21 通过）

- **p01 VXLAN 封装参数**（p31）——V1：UDP 4789/50 字节/24bit/16M 命中；V2：MTU 规划必需；V3：参数包。通过。
- **p02 Loopback0 身份原则**（p33/p79）——V1："Identified by the Loopback0 IP address" 命中；V2：router-id/update-source 惯例+取值示例；V3：AOS 编址惯例。通过。
- **p03 Underlay 收敛六条**（p80/p186）——V1：单区域 OSPF/p2p/BFD/SPF 0 全命中（spf-timer delay 0 多处 CLI）；V2：标准参数包可直接套用；V3：AOS 特有参数组合。通过。
- **p04 eBGP underlay AS 规划**（p60）——V1：命中；V2：AS 编号规划规则；V3：与 overlay 同 AS 的对照。通过。
- **p05 iBGP overlay 五要素**（p84-85）——V1：四步文本+CLI 命中，AFI=25/SAFI=70 亦命中（p51）；V2：固定配置套路+验证点；V3：activate-evpn 逐邻居启用。通过。
- **p06 业务默认参数**（p67）——V1："MTU : 9194, VPN IP-MTU : 1500" 命中（原文含对齐空格，等价）；V2：默认值核对表；V3：9194/Unknown-Mac-Route Ena 等 AOS 出厂值。通过。
- **p07 接入默认行为**（p102/p198）——V1："single-homing is activated by default" 命中（2 处）；V2：SH/MH-SA 默认判定；V3：AOS 简化模型私有行为。通过。
- **p08 非对称 IRB 全实例化**（p105/p109）——V1：两段引用均命中；V2：硬性前提+dummy 口方案；V3：Spine 补实例化的隐含成本。通过。
- **p09 DAG 编址规则**（p99/p109）——V1：.254/anycast-gateway-mac auto/00:00:5E:00:01 均命中；V2：DAG 配置三规则；V3：虚拟 MAC 格式与 RT2 双 MAC 通告。通过。
- **p10 Proxy ARP 默认与四参数**（p110）——V1："Proxy ARP is enabled for an EVPN" 命中；V2：四参数默认值+验证命令；V3：AOS 默认行为。通过。
- **p11 RT1-RT8 总表**（p52）——V1：各 Route Type 描述与 RFC 9136/9251 引用命中；V2：速查表；V3：RT1 per-ES/per-EVI 细分+基础路由 RT1-RT4 标注。通过（属任务说明明示的"独特"类）。
- **p12 RD/RT 构造规则**（p148/p185）——V1："RD= <System IP>:<EVI>"/"RT= target:<AS number>:<EVI>" 命中；V2/V3：任务说明点名的 RD/RT 公式类。通过。
- **p13 ETag 三种服务模型**（p175-176/p185）——V1：VLAN-based/bundle/aware 三段定义及 "MUST be set to 0" 命中；V2：模型选型；V3：AOS hybrid 实现独有。通过。
- **p14 MAC mobility 序列号与环回保护**（p127/p177）——V1：序列号 0→1 机制与 loop-protection 命令均命中；V2：三参数配置；V3：hold-down 判定逻辑。通过。
- **p15 BUM 复制两机制**（p40-42/p180）——V1：HER/Tandem/PIM-BIDIR/"one multicast group is used per VNI"/"Only ingress (head-end) replication is supported in the initial release 8.10R1" 均命中；V2/V3：复制方式选型+版本边界。通过。
- **p16 DF 选举规则**（p182-183）——V1："service carving"/"DF = EVI mod N"/pre-emptive 均命中；V2/V3：任务说明点名的 DF 算法类。通过。
- **p17 ESI 编码规则**（p142/p184-185）——V1："03:Access port MAC(6):ff:ff:ff"/"03:CE-MAC(6):ff:<Key-Id>(2)" 命中；V2/V3：AOS Type 0x3 编码公式独有。通过。
- **p18 VXLAN 学习模型**（p38）——V1："Each VNI has a virtual bridge instance" 等四行命中；V2：虚拟桥/虚端口模型+禁学习风险；V3：AOS 数据面模型。通过。
- **p19 VC vs EVPN MH 选型**（p187）——V1：Virtual Chassis 对比命中（3 处）；V2：接入冗余方案决策表；V3：收敛速度/hypervisor 配置差异的对比颗粒度。通过。
- **p20 on-demand 原则**（p184）——V1：两段引用命中；V2：解释"BGP 有路由但 MAC 表没有"的正常现象与核对方法；V3：AOS 私有 FDB 策略。通过。
- **p21 同子网/跨子网转发流程**（p181-182）——V1：8 步/6 步流程片段与 "ingress replication list" 命中；V2：排障时按步定位；V3：流程步骤数与假设条件。通过。

## cases（9/9 通过）

- **c01 Lab1 OSPF+iBGP 搭建**（p78-86）——V1：session cli timeout 200/spf-timer/neighbor update-source 等全量 CLI 命中；V2：四节点底座完整流程+验证链；V3：互联规划表与地址惯例。通过。
- **c02 Lab2 业务开通+dummy 口**（p102-108）——V1：service 100/200 三部曲 CLI 命中；V2：双业务开通+验证五连；V3：Spine dummy 口补实例化。通过。
- **c03 Lab2 IRB+DAG+Proxy ARP**（p109-117）——V1：ip interface service/anycast-gateway 命令与 CE 侧 vlan members 命中；V2：三层叠加全套+验证；V3：.1/.2 独立地址 + .254 anycast 的双轨编址。通过。
- **c04 Lab3 动态 LACP 跨设备多归属**（p153-156）——V1：linkagg lacp agg 3 序列与故障切换描述命中；V2：完整配置+切换演练；V3：MH-SA ESI 编码实例与 DF* 标志。通过。
- **c05 Lab3 静态 LAG 手工 ESI**（p156-158）——V1：linkagg static agg 7/esi 01:01:01:02:04/vlan 20 members linkagg 7 tagged 命中；V2/V3：静态 LAG 必须手工 ESI 的唯一完整示例。通过。
- **c06 架构指南 6 节点参考设计**（p187-197）——V1：100.100.100.0/24、11.11.11.1/24 v11、subsecond 调优等命中；V2：设计文档级全量配置；V3：与课堂 Lab 的差异点（聚合口/subsecond/全互联）。通过。
- **c07 架构指南业务收尾全套**（p198-204）——V1：dummy 1/1/48、linkagg 30 esi、mac-mobility loop-protection 命中；V2：验证命令全集；V3：三 Leaf 共享 ES + Peer-VTEP-List 场景。通过。
- **c08 课堂最小验证链**（p64-74）——V1：三条命令+tunnel-ports/rt3/mac-learning 命中；V2：可直接当开局 checklist 的逐层核对顺序；V3：单边配置 Oper Down→对端配置转 Up 的状态演进。通过。
- **c09 三 Leaf DF 选举与 aliasing 验证**（p200-201）——V1：carving-info/aliasing-info 命令与 EVI 1000→1.1.1.10、EVI 2000→1.1.1.20 输出命中；V2：多归属三视图验证法；V3：mod 算法分摊效果实例。通过。

## counter-examples（8/9 通过）

- **ce01 Spine 漏配业务须 dummy 口**（p105）——V1："dummy operational port" 命中（2 处）；V2：忘配后果+规避；V3：非对称 IRB 隐含成本。通过。
- **ce02 8.10R1 四项功能边界**（p173/p179/p180/p182）——V1：四句 "will not be supported in the initial release 8.10R1" 全部逐句命中；V2：售前/交付核对表；V3：任务说明点名的版本能力边界类。通过。
- **ce03 Proxy ARP 空表先造流量**（p203）——V1："it has probably timed out" 命中；V2：官方处置口径+排障顺序；V3：表项老化的非直觉行为。通过。
- **ce04 MAC duplication 拖垮控制面**（p177）——V1："MAC duplications"/"same address is present in two hosts" 命中；V2：loop-protection 处置+全 Leaf 配置提醒；V3：震荡机制与根因二分。通过。
- **ce05 远端 ES 不支持 sap-info**（p107/p155）——V1："ERROR: Command Not supported for Remote ES" 命中（3 处）；V2：本地/远端命令选择规则；V3：# 号 Missing ETAG 提示。通过。
- **ce07 教材网关笔误**（p113）——V1："Gateway:192.168.30.254" 命中（2 处，client 9/10）；V2：DAG 排障第一步核对项；V3：书中真实笔误的警示价值。通过。
- **ce08 静态 LAG 无自动 ESI**（p156/p185）——V1：原文两行提示+范围表（Static LAG → Manual ESI）命中；V2：漏配 esi 多归属不成立；V3：自动/手工 ESI 适用范围表。通过。
- **ce09 头端复制漏学 VTEP 静默丢流量**（p41）——V1："they will not receive any traffic" 命中；V2：裸 VXLAN 排障优先核对项；V3：silent failure 模式与 RT3 价值的因果链。通过。

## glossary（28/28 免验保留）

按流水线规则 glossary 免三重验证，全部保留进入下一阶段。

---

淘汰记录见 `rejected/counter-examples.md`（ce06 一条）。
