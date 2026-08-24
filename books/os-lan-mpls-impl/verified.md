# verified.md · OmniSwitch LAN MPLS Concepts & Implementation (DT00XTE324EN)

# 三重验证结果（阶段 1.5）
# V1 原文真实性：全部候选 quote 已在 fulltext.md 对应页命中（含跨行断句与 OCR 原样拼写，如 p131 "spcific"）。
# V2 可操作价值 / V3 独特性：淘汰 5 条（教科书级通用 MPLS 理论 3 条、与 f06 同源重复 2 条），详见 rejected/。
#
# 汇总：frameworks 6/6 通过 · principles 15/18 通过 · cases 7/9 通过 · counter-examples 8/8 通过 · glossary 25 免验保留
# 合计：41/66 通过 + 5 淘汰 + 25 免验 = 66

---

## Frameworks（6/6 通过）

### f01 AOS MPLS 骨干与 VPLS 部署总流程（十步法）
- V1：quote 命中 p58-65 的 Step 1-6 列表（"Install MPLS Package" 等在 fulltext 多处命中）。
- V2：pkgmgr 装包→IP 接口→OSPF→许可→LDP 两级使能→VPLS 的固定次序，是全书的实施主线，Lab 1 与参考设计均按此展开。
- V3：pkgmgr/uosn-mpls-v1.deb、SILOS 许可服务器、Loopback0 系统 IP 等均为 AOS 特有环节。

### f02 VPLS-LDP 信令配置流程（手工 SDP + 定向 LDP 会话）
- V1：Step 7-9 原文命中 p67-70。
- V2：service/sdp/bind-sdp/sap 四步 CLI 序列可直接照抄实施。
- V3：T-LDP 定向会话由静态 SDP 触发是 AOS（ALE/Nokia 系）特有建模方式。

### f03 VPLS-BGP 信令配置流程（自动发现与信令合一）
- V1：auto-discovery 段落在 fulltext 3 处命中。
- V2：ip bgp address-family l2vpn-vpls + signaling bgp ve-id 的完整 CLI 路径，含验证命令。
- V3：ve-id、BGP 生成 sdp:32768:x 绑定等 AOS 特有表现。

### f04 VPLS 信令选型框架：LDP vs BGP
- V1：RR 不支持句在 fulltext 第 3369 行（跨行断句）命中，p132-133。
- V2：给出"小规模 LDP / 多站点 BGP"的决策依据与配置量增长规律。
- V3：AOS 不支持 RR 这一能力边界是选型的硬约束，属本书独有信息。

### f05 MPLS 服务框架模型（SAP/SDP + 双层隧道）
- V1：SAP/SDP 定义在 p131 命中（原文 OCR 拼写 "spcific" 原样保留于 quote）。
- V2：解释所有 service 配置为何只落在 LER、SAP/SDP 如何分工，是读懂配置的前提模型。
- V3：SAP/SDP 术语体系为 ALE 特有（区别于 Cisco/Juniper 的接口建模）。

### f06 参考设计场景模板：企业园区与城域智能城市
- V1：p133-134 两段场景描述逐句命中。
- V2：售前可直接套用的两个经过验证的架构模板（园区端到端 MPLS / 城域核心汇聚 MPLS）。
- V3：AOS MPLS 的定位（企业+城域、性价比）与 MPLS 域边界划分建议来自 Reference Design Guide。

---

## Principles（15/18 通过；p06、p07、p11 淘汰）

### p01 MPLS 许可类型：站点许可浮动共享 4 节点 / 节点许可独立绑定
- V1：p52/p135 许可类型列表命中。V2：许可规划直接影响报价与部署。V3：4 节点浮动、VC 折算 8 台、ALE Licensing Portal 全是 ALE 特有规则。

### p02 MPLS 以 Debian 包动态安装，首版 8.9R3 仅 OS6860N
- V1：p59/p118 命中。V2：pkgmgr install/verify/show 的操作序列 + 版本/平台准入判断。V3：交换机功能走 Debian 包装卸是 AOS 独有做法。

### p03 Loopback0 作为系统 IP 是 OmniSwitch 的特有前置要求
- V1：p58 原句 "This requirement is specific to the OmniSwitch" 命中。V2：实施前置检查项。V3：教材自明"OmniSwitch 特有"。

### p04 MPLS 部署最佳实践七条
- V1：p136 七条逐句命中。V2：underlay/loopback/P2P 网络类型/BFD//31 的落地清单。V3：与 c05 的 rtr-port tagged 路由口、BFD 全局+OSPF 接口两级使能绑定后构成 AOS 语境。

### p05 标签分配规则：直连=隐式 NULL(3)，其余从 16 起，0-15 保留
- V1：p100/p122 命中。V2：解读 forwarding-table 输出（impl-null vs 52480+ 标签）的钥匙。V3：AOS 标签范围 16~1048575 为平台实测值，且"标签规则"属任务书认定的独特性类别。

### p08 AOS LDP 默认模式：DU + ILD + LLR
- V1：三处 "This is the default mode in AOS" 命中（p125-126）。V2：与对端/异厂商互通时核对模式。V3：三个维度的 AOS 默认值组合是平台特有信息。

### p09 LDP hold-time 协商规则与默认定时器
- V1：p125 协商句命中。V2："取小者生效 + 接口覆盖全局"直接指导定时器调整（只改一端可能不生效）。V3：AOS 默认值组（Hello 5s/Hold 15s/Targeted Hold 45s 等）来自 show mpls ldp 实测。

### p10 LDP 会话与 LDP ID 结构（多链路单会话、per-platform 标签空间）
- V1：p125 命中。V2：解释 show mpls ldp neighbor 输出（192.168.254.10:0 格式）与"多链路单会话属正常"的排障判断。V3：结合 AOS show 输出解读，保留。

### p12 PHP 倒数第二跳弹出机制与目的
- V1：p128 命中。V2：解读 Lab 中 Out-Label=3 的必然性，并与 ce03 的 EXP 丢失陷阱联动。V3：与 AOS 能力边界（显式 NULL 不支持）交叉引用，超出通用教材价值。

### p13 VPN 双层标签栈：传输标签在上、服务标签在下
- V1：p38/p123/p131 命中（LIFO 句命中）。V2：排査标签栈、理解 f05 服务模型的支撑规则。V3：与 SAP/SDP 双隧道 FEC 建模绑定，属本书体系内的核心规则。

### p14 服务模型三要点：只建在 LER、SAP/SDP 分工、按 VPLS 做 MAC 学习
- V1：p131/p133 命中（MAC learning, bridging and replication 在 fulltext 命中）。V2：直接决定配置落点（P 节点零 service 配置，Lab 中 sw9/sw10 空表为证）。V3：AOS 服务模型特有约束。

### p15 VPLS Split Horizon（水平分割）规则
- V1：p133 "must never send a packet on a PW" 命中。V2：解释 VPLS 骨干为何不跑 STP、为何必须全网状 PW，规划硬约束。V3：与 ce07 扩展性陷阱联动，构成选型闭环。

### p16 vlan-xlation 使能层级与命令（先端口级、再服务级）
- V1：p79-80 命令序列逐行命中。V2：两级使能是 Lab 2 故障恢复的实际手段。V3：service vlan-xlation / service access port ... vlan-xlation 为 AOS 特有 CLI。

### p17 BGP VPLS 邻居配置要点：同 AS 全互联 + update-source Loopback0 + activate l2vpn-vpls
- V1：p74/p110 命令逐行命中。V2：五要素邻居模板 + 验证命令，可直接交付。V3：每邻居单独 activate l2vpn-vpls、无 RR 只能全互联为 AOS 现状。

### p18 MPLS/VPLS 验证命令族谱（Reference Design Guide 汇总）
- V1：p139-145 注释与命令命中（FEC-To-NHLF、ftn-table、ilm-table 均命中）。V2：按层次组织的排障命令全集，运维手册级价值。V3：ftn-table/ilm-table/vpls-mesh 等为 AOS 特有视图。

---

## Cases（7/9 通过；c08、c09 淘汰）

### c01 Lab 1：四台 OS6860 部署 MPLS 骨干
- V1：p83-96 命令逐行命中（vlan 79 mtu-ip 4094、mpls load ldp 等）。V2：从 VLAN/OSPF/许可到 LDP 的完整可复现 CLI 流程 + 验证判据（双邻居 OPERATIONAL、impl-null、ECMP）。V3：SILOS/SWLIC 许可流程与 AOS 命令体系特有。

### c02 Lab 2：VPLS-LDP 信令部署
- V1：p97-105 命令逐行命中（sdp 78 far-end、bind-sdp 78、vlan-xlation）。V2：含弹性测试（断链 ping）与故障恢复手法，Lab 实操价值最高的一条。V3：AOS 特有 CLI 序列。

### c03 Lab 3：VPLS-BGP 信令部署
- V1：p106-114 命中（reload from working、autonomous-system 65724、ve-id 1）。V2：恢复骨干→IBGP→signaling bgp ve-id 的完整流程与 sh service 核对项。V3：BGP 自动生成 sdp:32768:x 绑定为 AOS 特有表现。

### c04 R-Lab 远程实验室 POD 拓扑
- V1：p16-19 命中（EMP 地址表在 fulltext 第 240-256 行以表格形式呈现，quote 为列内容归一；RDP 地址/账号命中）。V2：复现实验环境所需的资源与接入信息。V3：R-Lab POD 专属信息。

### c05 Reference Design 样例：LDP 骨干 + T-LDP VPLS 规范化配置
- V1：p136-138 逐行命中（IFtoR2、rtr-port tagged、bind-sdp 102 103）。V2：可直接做项目模板的标准化配置（比 Lab 更规范）。V3：rtr-port 路由口、一条命令绑多 SDP 等 AOS 写法。

### c06 Reference Design 样例：BGP VPLS 规范化配置
- V1：p138-139 逐行命中（ip bgp mpls 全文唯一处命中）。V2：多站点 BGP VPLS 的 CLI 清单模板。V3：ip bgp mpls 为参考设计样例独有的 AOS 命令。

### c07 SDP 复用样例：一服务多 SDP 与一 SDP 多服务
- V1：p78 命令逐行命中（sdp 20 far-end 10.10.10.2、bind-sdp 30）。V2：SDP 编号与复用规划（一条 T-LDP 会话承载多 VC）直接参考。V3：AOS 特有配置形态。

---

## Counter-examples（8/8 通过）

### ce01 许可状态无效或 demo 过期时 MPLS 被临时禁用
- V1：p92 命中。V2：全网 MPLS 突发失效的排查路径（sh license-info → SWLIC/SILOS 连接状态）。V3：AOS 许可机制特有陷阱。

### ce02 LSR ID（loopback）不唯一导致不可预测行为
- V1：p125 "unpredictable behavior" 命中。V2：上线清单加"全网 loopback 唯一性核查"。V3：教材加粗强调的规划陷阱。

### ce03 PHP 弹标签时 EXP（QoS）丢失，显式 NULL 又不被 AOS 支持
- V1：p128-129 命中（EXP bits are also removed）。V2：直接约束售前承诺——QoS 不能落在 EXP 上，要落到 DSCP。V3：AOS 能力边界（显式 NULL、QoS over EXP 均不支持）。

### ce04 朝向 CE 路由器的接口不能使能 LDP
- V1：p125 命中（fulltext 第 3130 行，"towards the CE" 跨行断句）。V2：LDP 使能范围的例外规则，误配后果明确。V3：与 AOS SAP 接入方式绑定的规则。

### ce05 AOS 首版 MPLS 不支持的特性清单（六项）
- V1：p127-133 各句分别命中（RSVP 第 3327 行附近、VPWS 第 3383 行跨行、RR 第 3369 行）。V2：方案设计禁引清单。V3：任务书明示"能力边界"属独特性，售前风险价值极高。

### ce06 LDP Graceful Restart 只对计划内接管有效
- V1：p130 "planned takeovers" 命中。V2：高可用承诺的话术边界（计划内维护 vs 突发故障）。V3：CMM 接管场景结合 AOS 实现的限制。

### ce07 LDP-VPLS 无自动发现，PE 增长带来全网状配置爆炸
- V1：p72 与 p132-133 两处命中（full-mesh of PWs 命中）。V2：n(n-1)/2 条伪线的规模估算公式与选型建议。V3：结合 AOS 无 RR 的双重边界。

### ce08 SAP 配成 untagged（:0）时出口永远 untagged
- V1：p79 命中（fulltext 第 1337-1338 行跨行）。V2：VLAN 封装不匹配单通故障的定位与设计约束。V3：AOS vlan-xlation 行为约束。

---

## Glossary（25 条，免验保留）

glossary.md 全部 25 条按规则免三重验证，整组保留，条目清单见 candidates/glossary.md。
