# 《OmniSwitch LAN Core Switching Ed15》蒸馏精华（DIGEST）

> 来源：DT00XTE216 OmniSwitch LAN Core Switching Ed15，全部知识点均带原书页码（<<<PAGE N>>> 格式）。

## 一、知识地图

本书覆盖 AOS（OmniSwitch）园区核心交换的四大版块，本知识库聚类为 12 个技能：

| 版块 | 技能（slug） | 核心问题 |
|---|---|---|
| 二层高可用 | erp-ring-protection | 环网 50ms 倒换 |
| | mstp-load-sharing | 多 VLAN 共享少量生成树+分流 |
| | mvrp-dynamic-vlan | VLAN 成员自动传播 |
| 二层安全与隔离 | macsec-link-encryption | 链路级加密 |
| | private-vlan-isolation | 广播域内分组隔离 |
| | arp-dos-defense | ARP 欺骗/DoS/强制上行 |
| | learned-port-security | 端口 MAC 锁定 |
| 三层路由 | ip-routing-fundamentals | 静态/RIP/IS-IS 与选路次序 |
| | ospf-area-redistribution | 区域设计与重分发 |
| | bgp-vrf-leak | AS 互联与多租户隔离 |
| | multicast-pim | 二层侦听与三层组播树 |
| Fabric 与平台 | spb-fabric | SPB 替代 STP 的全链路 Fabric |
| | switch-platform-ops | 聚合/SLB/升级回滚 |

一条主线贯穿全书：**AOS 的每个特性都是"admin-state enable 分层开关 + show 命令族验证"的组合**——先建对象、再挂成员、最后统一 enable，排障先看 show、再上 swlog debug。

## 二、十个最重要知识点串讲

**1. ERP 用"阻塞一条链路"换环网无环（<<<PAGE 37>>>-<<<PAGE 56>>>）。** 稳态下 RPL Owner 阻塞唯一的 RPL 端口；故障时 R-APS SF 消息传遍 Service VLAN，RPL 解阻塞完成约 50ms 倒换；恢复时 NR + WTR（默认 5 分钟）防抖回切，Guard 定时器（50 厘秒）丢弃过期 R-APS。每环有且仅有一个 RPL，且 RPL 只能配在未 enable 的环上（<<<PAGE 55>>>），否则视为非法配置。

**2. MSTP 同域三要素与负载分担（<<<PAGE 117>>>-<<<PAGE 146>>>）。** region name、revision level、VLAN-to-MSTI 映射三者完全一致才是同一个域，对外表现为一台交换机。CIST（实例 0）用单 BPDU 承载全部实例信息。负载分担的做法是让不同 MSTI 选不同根桥（优先级须为 4096 的倍数），例如 sw7 做 MSTI 1 根、sw8 做 MSTI 2 根，VLAN 20/30 各走一条上行（<<<PAGE 143>>>、<<<PAGE 146>>>）。

**3. MVRP 只管二层，动态 VLAN 有"生命"（<<<PAGE 152>>>-<<<PAGE 163>>>）。** 一个 PDU 携带端口全部 4094 个 VLAN 状态；学到的 VLAN 标记为 dyn，源端删 VLAN 或禁用 MVRP 前它删不掉且会被自动重建。动态 VLAN 不建 IP 接口、不映射 MSTI——三层和生成树分担要手工补配。MVRP 仅支持 STP flat 模式（<<<PAGE 154>>>）。

**4. MACsec 的密钥模型决定配置形态（<<<PAGE 67>>>-<<<PAGE 94>>>）。** 每节点收发各一条安全通道（SCI），通道内 SA 持有 SAK。Static 模式手工配 key-chain，本端 sci-tx 必须等于对端 sci-rx（交叉引用）；Dynamic PSK 由 MKA 协商 SAK，轮换双门限（会话 5-120 分钟、流量 5-1000GB）先到先触发。平台差异是最大的坑：OS6860N 不支持 Static、VFL 堆叠口不支持 MACsec、9900 部分板卡仅 Static（<<<PAGE 71>>>-<<<PAGE 75>>>）。

**5. Private VLAN 的转发模型：MAC 全学在 Primary 上（<<<PAGE 98>>>-<<<PAGE 112>>>）。** isolated 成员间二层完全不通、community 组内通组间不通，出向流量统一经 Primary VLAN 转发，未授权的二级 VLAN 间流量被丢弃。一个 Primary 只能有一个 Isolated，多组隔离需求应拆多个 community（<<<PAGE 109>>>）。跨交换机延伸用 ISL 口（可用 linkagg 承载）。

**6. AOS 路由优先级表与 Loopback0 约定（<<<PAGE 216>>>、<<<PAGE 299>>>）。** Local 1 / Static 2 / OSPF 110 / ISIS-L1 115 / ISIS-L2 118 / RIP 120 / EBGP 190 / IBGP 200 / Import 210，可手工调整。Loopback0 永久 up，被 RIP/OSPF 自动通告（BGP 不），是 router-id、BGP peering、PIM RP 的标准身份地址。

**7. OSPF 区域类型=允许进入的 LSA 集合（<<<PAGE 267>>>-<<<PAGE 270>>>、<<<PAGE 355>>>）。** Stub 拒 Type5、ABR 注入 Type3 默认路由；Totally Stubby 再拒 Type3；NSSA 用 Type7 引入外部路由（ABR 转成 Type5 出域）。配置七步法里 router-id 先行、最后统一 enable（<<<PAGE 275>>>）。两个高频故障：认证单端先开会立刻丢邻居（<<<PAGE 353>>>）；Hello interval 不一致邻居无法 Full，用 `swlog appid ospf_0 ... level debug3` 抓日志定位（<<<PAGE 292>>>-<<<PAGE 294>>>）。重分发范式"先 route-map 后 redist"同样适用于 RIP/BGP（<<<PAGE 228>>>、<<<PAGE 516>>>）。

**8. 组播分两层解：IPMS 管同 VLAN，PIM-SM 管跨网段（<<<PAGE 377>>>、<<<PAGE 426>>>）。** IPMS 硬件侦听 IGMP，只发向加入端口（开关前后泛洪对比见 <<<PAGE 405>>>-<<<PAGE 409>>>）；PIM-SM 显式加入 + RP 共享树，末跳 DR 自动发起 SPT 切换。RP 冗余首选 Anycast RP（RFC 4610）：多 RP 共享一个 Loopback 任播地址，IGP 收敛即 RP 切换，static-rp 必须配到全域所有 PIM 路由器（<<<PAGE 644>>>-<<<PAGE 649>>>）。

**9. BGP 属性选路次序是排障对照表（<<<PAGE 497>>>）。** Local Pref（高优）→ AS-Path（短优）→ Origin（IGP>EGP>Incomplete）→ MED（低优）→ Next-Hop 就近 → EBGP>IBGP → RID。IBGP 水平分割是全互联需求的根因（<<<PAGE 501>>>）。VRF 隔离默认、互通例外：跨 VRF 只能经 GRT 以 route-map 过滤中转，且交换机本机跨 VRF 接口互 ping 永远不通（安全设计， <<<PAGE 467>>>-<<<PAGE 468>>>）。

**10. SPB 用 IS-IS 换掉 STP 的"浪费"（<<<PAGE 521>>>-<<<PAGE 570>>>）。** 每节点对每个 BVLAN 建自根 SPF 树，全链路可用、路径对称、帧有序，百毫秒级收敛。BCB 只按 BMAC 转发不学客户 MAC。部署四任务：建 BVLAN+ECT、定 control BVLAN（仅协议禁用时改）、配 ISIS 接口、enable（<<<PAGE 547>>>）。硬约束：ISID/BVLAN 映射全局一致；BVLAN 上无 STP；BVLAN 数别超过等价路径数；不同 VLAN 映射同一服务会引发 mac-move 震荡（<<<PAGE 555>>>、<<<PAGE 610>>>）。

## 三、跨技能的三条工程心得

1. **enable 之前检查全局一致性**：MEG Level（ERP）、Region 三要素（MSTP）、密钥链交叉（MACsec Static）、ISID/BVLAN（SPB）、area type（OSPF stub）——凡是"多节点协同"的协议，错一处即整段不通，且报错往往不在出错的那台机器上。
2. **show 先行、swlog 兜底**：每个特性都有配套 show 族（show erp/show pvlan members/show spantree msti vlan-map/show ip ospf/show spb isis adjacency），先看状态再动配置；OSPF 邻居类故障用 swlog debug3 分级日志直接抓到 "invalid helloInterval" 级别的证据（<<<PAGE 292>>>）。
3. **回滚路径先于变更设计**：working/certified 双镜像（<<<PAGE 680>>>）、reload no rollback-timeout（<<<PAGE 62>>>）、实验后删目录重载，AOS 的变更文化是"先拿到可回退状态，再推进"。

## 四、使用建议

- 查部署步骤：直接进对应 skill 的 A1；查禁区先看各 skill 的 B 节。
- 术语速查：见同目录 GLOSSARY.md（按 ERP/MACsec/PVLAN/MSTP/MVRP/安全/路由/OSPF/组播/VRF-BGP/SPB 分组）。
