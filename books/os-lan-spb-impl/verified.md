# verified.md · 阶段 1.5 三重验证通过条目

来源: OmniSwitch LAN SPB Concepts & Implementation (DT00XTE323EN, Edition 12)
验证规则: V1 原文真实性（quote 在对应页命中；CLI 序列允许跨页关键命令截取）× V2 可操作价值 × V3 独特性
验证方法: 脚本化 quote 片段比对 source/fulltext.md（`<<<PAGE N>>>` 分页），0 命中或低命中条目逐页人工复核

## 汇总

| 类型 | 候选 | 通过 | 淘汰 | 通过率 |
|---|---|---|---|---|
| frameworks | 14 | 13 | 1 (f14) | 93% |
| principles | 35 | 35 | 0 | 100% |
| cases | 18 | 18 | 0 | 100% |
| counter-examples | 14 | 14 | 0 | 100% |
| glossary | 40 | 40（免验保留） | 0 | — |
| **合计** | **121** | **120** | **1** | **99%** |

V1 抽查备注（人工复核项）:
- f05 (p31): 原文为表格文本（SPB/EVPN/MPLS 三列逐行），quote 为忠实压缩；p33 收敛 50ms/100ms、成本 $$$/$$、p35 案例矩阵（视频监控/赌场/园区/ITS→SPB、大型 DC→EVPN、Rail E&U→IP-MPLS）均逐条命中。
- f06 (p61/62): 两层/三层拓扑图文字全部命中（含 "No need for BCB nodes"、"STP or DHL towards BEB"、MPLS/VXLAN 远端扩展注记）。
- f11 (p305): OV-init 快照、Pod#-OV2500.4xx、预配 SNMPv2 无 License 均命中。
- f04 (p85): unicast-table/spf/database/nodes 命令链逐条命中。
- c05 (p167/169): 服务与内联接口在 p167、VRRP 命令在 p169——CLI 序列跨页，属允许范围。
- c12/c13/c14 (p246-258): multi-access/DHL/erp-ring 命令序列均命中。
- 其余条目脚本比对 2/2 至 4/4 片段命中声称页码（部分同时命中复述页，如 p326 混合端口 Lab 复用 p83 规则）。

---

## frameworks（13/14 通过）

- **f01** SPB 配置分层总框架 — V1 p65 命中（p88/89 复述）✓；V2 全书配置主线，任何交付按此分层 ✓；V3 BEB/BCB 职责切分 + AOS 配置层级，SPB 特有 ✓
- **f02** SPB 骨干部署四步流程 — V1 p83 ✓；V2 可直接照做的部署顺序（含先禁 IS-IS 再设控制 BVLAN）✓；V3 AOS CLI 特有 ✓
- **f03** L2 服务开通五步流程 — V1 p105/108 ✓；V2 开通标准顺序，BEB-only 原则明确 ✓；V3 AOS 语法（service spb X isid Y bvlan Z）✓
- **f04** SPB IS-IS 验证命令序列 — V1 p85 ✓；V2 排障链自底向上，验收即用 ✓；V3 show spb isis 族命令为 AOS 特有 ✓
- **f05** SPB/EVPN/MPLS 选型框架 — V1 p31 表格 + p33 量化 + p35 案例矩阵（人工复核）✓；V2 选型决策直接可用 ✓；V3 ALE 官方定位矩阵，含 50ms/100ms 收敛与成本量化 ✓
- **f06** 两层 vs 三层设计拓扑 — V1 p61/62 ✓；V2 组网设计判据（小网 BEB 全互联、大网引入 BCB）✓；V3 VC 双机冗余 + MPLS/VXLAN 域扩展为 ALE 方案特有 ✓
- **f07** IP over SPB 三方案递进 — V1 p156 ✓；V2 叠路由三路线选择 ✓；V3 IPVPN TLV 免路由协议为 SPB 特有 ✓
- **f08** L3-VPN 四步流程（bind→export→import→redist）— V1 p193-197 ✓；V2 配置心法四步，route-map 过滤齐全 ✓；V3 spb ipvpn 命令族 AOS 特有 ✓
- **f09** BUM 分发模式选择框架 — V1 p138-141/145 ✓；V2 三模式选型 + 配置层级 ✓；V3 Head-End/Tandem S,G / *,G 为 SPB 特有 ✓
- **f10** UNP 动态服务决策与编号计算 — V1 p274/275/279 ✓；V2 三个确定性公式可直接套用 ✓；V3 10,000,000 + 域ID×10,000 + (tag mod 512) 为 AOS 独有算法 ✓
- **f11** OV2500 编排上线流程 — V1 p305（人工复核）✓；V2 快照→License→SNMP→发现→拓扑五步可照做 ✓；V3 OV-init 快照、EVAL License 口令、community-map 序列均为本课程环境特有 ✓
- **f12** OAM 排障流程（mac-ping + SAA）— V1 p147 ✓；V2 两层排障与验收方法 ✓；V3 mac-ping 按 BVLAN 探测、saa spb auto-start 为 AOS 特有 ✓
- **f13** ERP/SPB 互操作部署流程 — V1 p243/256-258 ✓；V2 环内节点/BEB 两侧分工模板 ✓；V3 spb-remote-system access-tagged 形式 AOS 特有 ✓

## principles（35/35 通过）

- **p01** BVLAN 五特性 + AOS 上限 16 — V1 p66 ✓；V2 行为边界与容量约束直接约束设计 ✓；V3 AOS 16 BVLAN 上限特有 ✓
- **p02** BVLAN/ECT 全网一致性 — V1 p83/326 ✓；V2 部署纪律 + ECT 分散最佳实践 ✓；V3 ECT 逐 BVLAN 指派 SPB 特有 ✓
- **p03** 控制 BVLAN 只能协议禁用时改；BVLAN 自动禁 STP — V1 p83/326 ✓；V2 排障"改不动先查协议状态" ✓；V3 AOS 行为细节 ✓
- **p04** ECT 16 算法自动分配 — V1 p70 ✓；V2 平局裁决可预测路径 ✓；V3 掩码 XOR BridgeID 机制 SPB 特有 ✓
- **p05** 选优顺序 metric→跳数→ECT — V1 p70 ✓；V2 路径调优基础 ✓；V3 两侧取最大值规则 SPB 特有 ✓
- **p06** metric 两侧不一致取最大 — V1 p129 ✓；V2 引流必须两端同步改，否则无效 ✓；V3 SPB 特有行为 ✓
- **p07** service/ISID/BVLAN 本地性与全局性 + 容量 — V1 p109 ✓；V2 编号纪律 + 范围语法（4001:3）✓；V3 AOS 容量与范围语法特有 ✓
- **p08** SAP 只能建在 access 口 + 封装标识 — V1 p97/98 ✓；V2 封装写法表（:0/:all/QinQ）即查即用 ✓；V3 AOS 语法特有 ✓
- **p09** vlan-xlation 默认关、绑 IP 接口隐式启用锁定 — V1 p100/163 ✓；V2 规划期须确认翻译需求 ✓；V3 隐式启用+锁定为 AOS 特有陷阱规则 ✓
- **p10** L2 Profile 控制帧默认动作表 — V1 p115 ✓；V2 默认动作表可直接查 ✓；V3 def-access-profile 动作集 AOS 特有 ✓
- **p11** CoS 分类只在边缘 — V1 p118 ✓；V2 QoS 设计要点（隧道 BPDU 最高优先级）✓；V3 MAC-in-MAC 不重分类 SPB 特有 ✓
- **p12** LBD 机制与定时器 — V1 p120-123 ✓；V2 配置三件套 + 定时器 ✓；V3 私有 MAC 0x01-20-DA-02-01-71 特有 ✓
- **p13** 默认 P2P / multi-access DIS 选举 — V1 p229 ✓；V2 共享网改造必读 ✓；V3 默认值/3 秒重选为 AOS 细节 ✓
- **p14** Overload 引流 — V1 p130 ✓；V2 维护软隔离两用法 ✓；V3 overload-on-boot AOS 应用场景 ✓
- **p15** 组播模式配置层级 — V1 p145 ✓；V2 配置纪律（逐服务/全局/逐 BVLAN）✓；V3 tandem sgmode/gmode AOS 特有 ✓
- **p16** 组播组 B-MAC 编码规则 — V1 p142 ✓；V2 可从组 B-MAC 反推源节点与 I-SID ✓；V3 编码公式 SPB 特有 ✓
- **p17** IPMS 逐服务显式启用 — V1 p145 ✓；V2 不开则组播全泛洪，开法明确 ✓；V3 AOS 命令特有 ✓
- **p18** 内联 IP 接口三条硬规则 — V1 p163/201 ✓；V2 前置条件+副作用清单 ✓；V3 隐式 vlan-xlation 行为特有 ✓
- **p19** UNP 分类七级优先序 — V1 p267 ✓；V2 规则设计顺序表 ✓；V3 AOS 优先序特有 ✓
- **p20** System Default 编号公式与可调参数 — V1 p275/279 ✓；V2 公式 + service-base/service-mod 调参 ✓；V3 AOS 独有 ✓
- **p21** multi-untag-sap 支持范围 — V1 p271 ✓；V2 平台选型硬约束清单 ✓；V3 仅列出的新平台支持，AOS 特有 ✓
- **p22** 持久 SAP 与 mac-mobility — V1 p272/273 ✓；V2 静默设备/VRRP 场景配置法 ✓；V3 每口 8 profile 上限 AOS 特有 ✓
- **p23** ERP/SPB 约束清单 — V1 p242 ✓；V2 六条铁律检查表 ✓；V3 AOS 互操作约束特有 ✓
- **p24** Hybrid 一口双角色 — V1 p315/316 ✓；V2 省端口的落地命令 ✓；V3 8.9.R03 起的特性，AOS 特有 ✓
- **p25** E-Tree Leaf/Root 语义与版本约束 — V1 p318/330 ✓；V2 隔离设计 + Root 侧普通服务配法 ✓；V3 8.9.R03 全 Leaf 行为特有 ✓
- **p26** mac-ping 固定超时与目标限制 — V1 p147 ✓；V2 使用限制明确 ✓；V3 AOS 私有 ping 特有 ✓
- **p27** SAA 默认参数集 — V1 p150 ✓；V2 阈值/间隔默认值表即查即用 ✓；V3 saa spb auto-start 特有 ✓
- **p28** IS-IS 运行参数默认值 — V1 p76/231 ✓；V2 计时器/GR 默认基线 ✓；V3 AOS 默认值集（SPF Wait 100/300/1000 等）✓
- **p29** DHL 组成与限制 — V1 p250 ✓；V2 双上联免 STP 方案 + 五条配置 ✓；V3 DHL 为 AOS 特有特性 ✓
- **p30** 伪线服务行为规则 — V1 p94/95/235 ✓；V2 E-LINE 交付规则（关学习/强制 head-end）✓；V3 pseudo-wire enable 语法特有 ✓
- **p31** VPN-Lite 回环口准则 — V1 p175 ✓；V2 回环对 VLAN 协调规则 ✓；V3 VRF-I-SID 约束特有 ✓
- **p32** 控制 BVLAN 带内管理 — V1 p66/67 ✓；V2 spb-mgmt 三件套 + 双向重分发 ✓；V3 IS-IS 免 ARP 通告机制 SPB 特有 ✓
- **p33** VRRP 优先级分工 — V1 p169 ✓；V2 交叉优先级负载分担模板 ✓；V3 AOS vrrp 语法 + over SPB 场景 ✓
- **p34** UNP 平台能力与 quarantine 限制 — V1 p262 ✓；V2 NAC 规划须绕开的缺口 ✓；V3 AOS 功能边界特有 ✓
- **p35** SNMP 纳管参数准则 — V1 p309 ✓；V2 六条命令序列 ✓；V3 保留字禁用/community-map mode 为 AOS 特有 ✓

## cases（18/18 通过）

- **c01** Lab1 骨干从零部署 — V1 p83/84 ✓；V2 完整命令序列可直接照做 ✓；V3 AOS CLI ✓
- **c02** Lab2 L2 服务部署 — V1 p109/110 ✓；V2 接入+BEB 双侧完整配置 + 验证命令 ✓；V3 AOS CLI ✓
- **c03** Lab3 协议分析与保护 — V1 p129-132 ✓；V2 五个保护实验组合序列（倒换/metric/overload/LBD/L2 Profile）✓；V3 AOS CLI 与实验现象 ✓
- **c04** L3VPN 内联接口两命令 — V1 p161/162 ✓；V2 最小配置模板 ✓；V3 AOS CLI ✓
- **c05** Lab4 VRRP 双网关 — V1 p167/169（跨页，人工复核）✓；V2 服务+接口+VRRP 完整序列 ✓；V3 AOS CLI ✓
- **c06** VPN-Lite 静态+OSPF 对拍 — V1 p176 ✓；V2 标准块配置模板 ✓；V3 AOS vrf 语法 ✓
- **c07** Lab5 VPN-Lite 实操 — V1 p180/181 ✓；V2 四节点 OSPF + route-map 重分发全序列 ✓；V3 AOS CLI ✓
- **c08** L3-VPN 三件套对拍 — V1 p202 ✓；V2 最小五步模板 ✓；V3 spb ipvpn 命令族 ✓
- **c09** Lab6 L3-VPN 实操 — V1 p212 ✓；V2 先停 OSPF 再 bind 的改造序列 + 验证链 ✓；V3 AOS CLI ✓
- **c10** 三节点全网配置与三级表对拍 — V1 p217 ✓；V2 排障"路由学到没有"标准参照 ✓；V3 show spb ipvpn route-table 输出解读 ✓
- **c11** L3 ECMP 双 I-SID — V1 p219 ✓；V2 同 VRF 双 bind 等价多路径配置 ✓；V3 "+" 双下一跳标记 AOS 特有 ✓
- **c12** Lab7a 多点共享网 — V1 p248（人工复核，Lab 起于 p246）✓；V2 含完整回滚序列 ✓；V3 type multi-access/priority 127 AOS CLI ✓
- **c13** Lab7b DHL 双归属 — V1 p252 ✓；V2 接入双上联全流程（DHL+服务+SAP+VRRP）✓；V3 dhl 命令族 AOS 特有 ✓
- **c14** Lab7c ERP 环过 SPB — V1 p256/257 ✓；V2 环内/BEB 双侧模板 + 验证 ✓；V3 erp-ring spb-remote-system 语法特有 ✓
- **c15** Lab8 UNP 三场景 — V1 p281/286 ✓；V2 动态服务/802.1x/静默设备三段实操 ✓；V3 unp 命令族 + RADIUS Filter-ID 联动 ✓
- **c16** Lab9 OV2500 纳管 — V1 p306/309 ✓；V2 带内管理+SNMP+发现+拓扑全流程 ✓；V3 EVAL License 参数与 OV 操作路径特有 ✓
- **c17** Lab10 混合端口 + E-Tree — V1 p331 ✓；V2 两个 Day3 特性落地序列 + ping 矩阵验证 ✓；V3 hybrid enable / e-tree enable AOS 特有 ✓
- **c18** 老硬件 Outline 回环 — V1 p353/358 ✓；V2 两种回环法配置（双口对接/单口 loopback + rtr-port）✓；V3 rtr-port tagged vlan 形式 AOS 特有 ✓

## counter-examples（14/14 通过）

- **ce01** 控制 BVLAN 启用状态不可改 — V1 p83/326 ✓；V2 正确顺序（先 disable）✓；V3 AOS 行为特有 ✓
- **ce02** metric 两侧不一致取最大 — V1 p129 ✓；V2 单侧降级行不通，须两端同步 ✓；V3 SPB 特有 ✓
- **ce03** LBD 关整个 linkagg — V1 p131 ✓；V2 故障面评估要点 ✓；V3 AOS 行为特有 ✓
- **ce04** LBD 封口裁决规则（BridgeID/PortID）— V1 p122/123 ✓；V2 可预判哪个口被封 ✓；V3 裁决规则特有 ✓
- **ce05** 绑 IP 接口后 vlan-xlation 锁定 — V1 p163/201 ✓；V2 规划期确认，事后改不了 ✓；V3 AOS 隐式行为 ✓
- **ce06** 同 I-SID 不能既 bind 又 redist 到同一 VRF — V1 p198 ✓；V2 多部门互通设计约束 ✓；V3 L3-VPN 冲突规则特有 ✓
- **ce07** VPN-Lite 两 VRF 不能共享 I-SID — V1 p175 ✓；V2 隔离边界明确 ✓；V3 AOS 约束 ✓
- **ce08** ERP/SPB 六条禁区 — V1 p242 ✓；V2 检查表逐条可用 ✓；V3 互操作禁区特有 ✓
- **ce09** E-Tree 8.9.R03 全 Leaf — V1 p318/330 ✓；V2 两端都配 e-tree 会得死网 ✓；V3 版本行为特有 ✓
- **ce10** mac-ping 目标/超时限制 — V1 p147 ✓；V2 组播路径用 multicast-table 查 ✓；V3 AOS 限制特有 ✓
- **ce11** 回环口独占性 — V1 p359 ✓；V2 端口预算扣除 ✓；V3 loopback 模式 linkagg 只能删组解除，AOS 特有 ✓
- **ce12** SNMP 用户名保留字 — V1 p309 ✓；V2 建号失败排坑 ✓；V3 admin/diag/user 禁用 AOS 特有 ✓
- **ce13** UNP 隔离用户不能重定向补救 — V1 p262 ✓；V2 NAC 设计绕开 ✓；V3 AOS 功能缺口 ✓
- **ce14** 人为环路故障模型（MAC 漂移/ping 断）— V1 p131/132 ✓；V2 双上联必须配 DHL/ERP/LBD 的教训 ✓；V3 教材特有实验现象（MAC 双侧漂移）✓

## glossary（40 条免验保留）

按流水线规则 glossary 免三重验证，40 条全部保留，进入下一阶段。
