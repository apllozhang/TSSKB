# 《OmniSwitch R6/R8 Bootcamp Issue 25（DT00CTE120）》蒸馏精华（DIGEST）

> 来源：Bootcamp Issue 25 DT00CTE120（1207 页五天训练营 Participant's Guide），全部知识点带原书页码（<<<PAGE N>>> 格式）。

## 一、本书定位

这是 ALE 新人 ACFE/ACSE 培养的主教材：五天全科训练营，从硬件认知一路讲到 SPB 织构，每天都是"Overview 原理 + Lab 完整 CLI 实操"的结构（F1，<<<PAGE 8-13>>>）。与参考书不同，它的最大价值在 Lab 的完整命令序列与验证输出——每个特性都能对照着敲一遍。本知识库将其聚类为 12 个技能。

## 二、12 个技能摘要

| # | 技能（slug） | 对应天 | 一句话核心 |
|---|---|---|---|
| 1 | aos-bootcamp-switch-fundamentals | Day1 | 产品三层线（堆叠/加固/模块化）×速率演进主线；电源冗余 N+1 只防模块故障；9900 无背板直连 |
| 2 | aos-flash-config-management | Day1+扩展 | working/certified 双目录互为回滚；升级四步"传 working→reload 验证→copy certified"；snapshot 文本恢复 |
| 3 | aos-stacking-virtual-chassis | Day1 | 堆叠四角色与 Slot-ID 唯一性；VC 五级选举；脑裂双 Master 同 IP 同 MAC，RCD/VCSP 双保险 |
| 4 | aos-vlan-l2-foundations | Day2 | VLAN 四途径入组、动态分类五级优先序；Loopback0 是管理锚点；LLDP-MED 让话机自动上线 |
| 5 | aos-lacp-stp-redundancy | Day2 | 聚合靠 admin key 两端一致；MSTP 同域三要素+双实例分流；DHL 双上行 100% 带宽 |
| 6 | aos-vrrp-first-hop-redundancy | Day3 | 虚拟 MAC 00-00-5E-00-01-{VRID}；Skew_Time=(256-Priority)/256 错峰升主；Tracking 扣优先级触发切换 |
| 7 | aos-qos-policy-engine | Day3 | QoS 与 ACL 同一策略三元组引擎；默认全 accept+端口不信任是两大事故源；R8 QSet 三 Profile |
| 8 | aos-access-guardian-unp-bootcamp | Day3 | UNP=VLAN+策略列表随人走；RADIUS Filter-ID 下发、失败走降级链；R8 十六级分类+IoT 指纹画像 |
| 9 | aos-poe-power | Day3 | 动态按需供电至预算上限；默认 oper down 须 lanpower start；critical 优先级最后断电 |
| 10 | aos-ip-routing-rip-ospf | Day4+扩展 | 偏好值 Local 1/Static 2/OSPF 10/RIP 100 定乾坤；区域=LSA 集合；GR 靠 helper 契约；BGP/IS-IS/SLB/IPv6 扩展并入 |
| 11 | aos-security-vrf-macsec | Day4+扩展 | AOS 安全组合拳"默认收紧、显式信任"；VRF 隔离是默认、互通是例外（route-map 泄漏） |
| 12 | aos-multicast-erp-spb | Day5+扩展 | 组播两层解（IPMS 本段/PIM-SM 跨段）；ERP 牺牲一条 RPL 换全环无环；Auto-fabric 七步零接触 |

## 三、五天页码索引表

| 天 | 主题 | 页码 | 主要技能 |
|---|---|---|---|
| Day 1 | 硬件产品线 + System Management（目录/回滚/CLI/远程访问，7 个 Lab）+ Stacking R6 + Virtual Chassis + 诊断 | <<<PAGE 18-356>>> | 1 / 2 / 3 |
| Day 2 | VLAN + LACP + 802.1q + STP/MSTP + DHL + 高级 IP 接口/DHCP Relay + LLDP | <<<PAGE 358-521>>> | 4 / 5 |
| Day 3 | VRRP + QoS + ACL + Access Guardian(UNP)/IoT + PoE | <<<PAGE 522-710>>> | 6 / 7 / 8 / 9 |
| Day 4 | IP 路由 RIP/OSPF（GR）+ AOS 网络安全（LPS 等）+ VRF | <<<PAGE 711-864>>> | 10 / 11 |
| Day 5 | IP 组播（PIM-SM）+ 二层高级（ERP）+ Intelligent Fabric（SPB + Lab） | <<<PAGE 865-960>>> | 12 |
| 扩展 | 代码升级 / MVRP / SLB / 静态聚合 / AG Captive Portal / MACsec / BGP / ISIS / 安全认证 / IPv6 | <<<PAGE 961-1138>>> | 2 / 5 / 8 / 10 / 11 / 12 |
| 附录 | ProActive Lifecycle / CodeGuardian / 全系列机型速查 | <<<PAGE 1139-1207>>> | 1 |

## 四、贯穿五天的三条主线

**1. 一切变更先设计回滚路径。** Day 1 的 working/certified 双目录是全书的方法论地基（<<<PAGE 126-133>>>）：Lab 里每次实验都以 `reload working no rollback-timeout` 收尾、升级以"验证后才 `copy working certified`"收口（<<<PAGE 962-965>>>）。堆叠/VC 的 takeover 同样要求先 `copy flash-synchro` 同步（<<<PAGE 260>>>）。

**2. enable 分层开关 + show 族验证。** AOS 的配置节奏统一是"先建对象（VLAN/聚合/接口/策略）→ 挂成员 → 最后统一 admin-state enable"，验证一律走配套 show 命令族——从 `show stack topology` 到 `show ip pim sgroute`，每个特性都有状态对照表。

**3. 默认值是最大的坑。** 全书反例高度集中于默认行为：远程访问默认全关（<<<PAGE 184>>>）、IPMS 默认禁用（<<<PAGE 877>>>）、PoE 默认 oper down（<<<PAGE 697>>>）、QoS 默认全 accept 而端口默认不信任（<<<PAGE 558, 590>>>）、LPS 默认只学 1 个 MAC（<<<PAGE 850>>>）、端口默认不信任 DHCP Offer/ACK（<<<PAGE 830>>>）。上线清单的第一件事就是把这批默认值过一遍。

## 五、使用建议

- 查部署步骤：进对应 skill 的 A2；查禁区先看各 skill 的 B 节。
- R6/R8 命令差异（如 `vlan port default` vs `vlan members port`、`lacp linkagg` vs `linkagg lacp agg`）在各 skill 的 A2 中成对标注。
- 术语速查见同目录 GLOSSARY.md（按五天主题分组）。
