# DIGEST · SPB 实施精华——不读全书，只看这一篇

> 教材：OmniSwitch LAN SPB Concepts & Implementation（DT00XTE323EN，367 页，ALE 售后 Experienced 路径 3 天实操课）
> 这篇 Digest 把 8 个已蒸馏 skill 的干货串成一条交付主线：骨干 → L2 服务 → IP over SPB → 保护与冗余 → 动态服务与编排。命令与页码均出自原书。

## 一、一页看懂 SPB 实施

这门课的骨架就是 SPB 交付生命周期，3 天 = 三个阶段：

- **Day 1 打骨干（p3-151）**：BVLAN/ECT/IS-IS 部署（Lab1，p83）、L2 服务开通（Lab2，p108）、协议分析与保护（Lab3，p127-132）、BUM 流量与排障（p138-150）。骨干只跑 IS-IS 一个协议，收敛约 100ms、成本低于 MPLS（p33）。
- **Day 2 加路由（p152-258）**：IP over SPB 三方案——VRRP 冗余（p169）、VPN-Lite（p176/180）、L3-VPN（p193/202），外加接入冗余（DHL/ERP/multi-access，p229-256）。
- **Day 3 上自动化（p259-344）**：UNP 动态 SAP（p274-286）、OV2500 编排纳管（p304-309）、Hybrid 口与 E-Tree（p315-331）。

一句话：**Day1 让 B-MAC 通，Day2 让 IP 路由通，Day3 让服务自动开通、网管看得见。**

职责分层记死一条（p61-62）：控制面（BVLAN+IS-IS+NNI 口）配在 BEB 与 BCB；数据面（access 口+SAP）只配在 BEB，BCB 永不感知服务。小网两层——BEB 全互联免 BCB，冗余靠 VC 双机；大网三层——BCB 居核心只学 B-MAC。

## 二、从零搭 SPB 的八步主线

1. **骨干四步**（Lab1，p83）：建 BVLAN（含 ECT）→ 定控制 BVLAN → 配 IS-IS 接口 → 全局启用。BVLAN/ECT 指派全网必须一致（p83），不同 BVLAN 配不同 ECT-ID 做流量分担。
2. **L2 服务五步**（p108）：接入机建 VLAN → BEB 声明 service access port → 可选 L2 Profile → 建 service（spb X isid Y bvlan Z）→ 挂 SAP。I-SID 与 BVLAN 全网一致、一个 I-SID 只绑一个 BVLAN（p109）。
3. **叠三层**（p156-202）：要 OSPF/BGP 对接选 VPN-Lite；纯 SPB 域内选 L3-VPN（IS-IS IPVPN TLV 直带 VRF 路由，免路由协议，p199）。
4. **保护**（p120-141）：LBD 防接入环、IPMS 抑制泛洪、BUM 三模式选型（head-end/tandem S,G/tandem *,G）、overload 维护引流。
5. **冗余**（p229-256）：接入双上联用 DHL，ERP 环过 SPB 用 sap-neighbor+spb-remote-system，共享网改 multi-access。
6. **动态服务**（p274-286）：UNP profile 驱动动态 SAP，未命中流量按公式自动建服务。
7. **编排**（p304-309）：OV2500 靠控制 BVLAN 带内管理 + SNMP 发现全网。
8. **增强接入**（p315-331）：Hybrid 一口双角色、E-Tree 客户隔离。

调路径的规矩：`spb isis interface port X metric N`（默认 10）**必须两端同步改**——单侧降级按大值算整条链路（p28）。

## 三、配置模板速查

**骨干四步**（每节点执行，p83）：
```
spb bvlan 2000
spb isis bvlan 2000 ect-id 1
spb isis admin-state disable
spb isis control-bvlan 2000
spb isis interface port 1/1/5-6
spb isis admin-state enable
```

**L2 五步**（p108）：
```
vlan 2                                ! 接入机，用户口 untagged、上联口 tagged
service access port 1/1/3             ! BEB
service spb 2001 isid 2001 bvlan 2001 description vlan2 admin-state enable
service spb 2001 sap port 1/1/3:2 admin-state enable stats enable
```
SAP 封装：`:20` 单 VLAN、`:0` 未打标、`:all` 全部、`:30.32` QinQ（p99）。

**L3-VPN 五行**（p202）：
```
service spb 10 isid 1000 bvlan 4001 admin-state enable
vrf 1 ip interface L3vpn1 address 10.5.1.1/24 service 10
spb ipvpn bind vrf 1 isid 1000 gateway 10.5.1.1 all-routes
vrf 1 ip export all-routes
vrf 1 ip import isid 1000 all-routes
```
心法四步：bind → export → import → redist（可选泄漏），全程可挂 route-map。

## 四、动态服务与 E-Tree 一页

**UNP 编号公式**（p274/275）——System Default 自动建服务的三个确定性算式：
- I-SID = 10,000,000 + 域ID×10,000 + (VLAN tag mod 512)
- Service ID 从 32768 递增
- BVLAN = 计算出的 I-SID mod 8 做索引

分类七级优先序（p267）：MAC+VLAN > MAC > MAC段+VLAN > MAC段 > IP+VLAN > IP > VLAN tag——vlan-tag 兜底规则会吞掉所有未命中流量，精确规则要排前面。静默设备（打印机）用静态 profile 生成持久 SAP，VRRP 场景加 `mac-mobility`（p272/273）。每口最多 8 个 SPB 服务 profile。

**E-Tree 与 Hybrid 口**（p315-318）：E-Tree 语义是 Leaf↔Leaf 不通、Leaf↔Root 全通（SAP 级 PVLAN）。8.9.R03 起 e-tree 服务新建 SAP 一律 Leaf——**Root 必须落在对端 BEB、以同 I-SID 的普通服务形态建**，两端都配 e-tree 就是全 Leaf 死网。Hybrid 口 `service access port <p> hybrid enable` 让一个口同时做桥接（VLAN 域）和 SAP（服务域），入口按 VLAN tag 分类（p324），解决端口预算紧张不拆两个口的问题。

## 五、验证与排障命令手册

**两层排障法**（p147-150）：
1. mac-ping 点测：先 `show spb isis info` 拿对端 B-MAC → `mac-ping dst-mac e8:e7:32:a4:77:7d vlan 4015`，看 reply 出接口与时延。目标不能是广播/组播/空地址，每包超时固定 1 秒不可配。
2. SAA 持续探测：`saa spb auto-start` 自动为每个 BVLAN/B-MAC 对建会话，`show saa statistics aggregate` 看 RTT/Jitter/丢包；默认 1 分钟/轮、RTT 阈值 500us、Jitter 100us；对 LAG 目的会遍历所有成员链路。

**IS-IS 逐层验证链**（自底向上，p85）：
`show spb isis bvlans` → `interface` → `adjacency` → `info` → `unicast-table bvlan X` → `spf bvlan X` → `database`/`nodes`——第一层异常处即故障域。

**三个对拍技巧**：换路操作前后各抓一次 `show spb isis unicast-table` 对拍（p127-128 用法）；L3VPN 路由查三级表 `show spb ipvpn route-table` → `show ip global-route-table` → `show ip routes`（看 IMPORT 标记）；组播路径用 `show spb isis multicast-table`（组播 B-MAC ping 不了）。

## 六、学习路径

按交付顺序读 8 个 skill，每个独立可用：

1. `spb-backbone-deploy`——骨干从零部署与拓扑设计
2. `spb-l2-service`——L2 服务开通（SAP/I-SID/vlan-xlation/L2 Profile）
3. `ip-over-spb`——三方案叠三层与选型
4. `spb-bum-protection`——BUM 组播与接入保护
5. `spb-access-ring-redundancy`——DHL/ERP/multi-access 冗余
6. `spb-oam-troubleshoot`——mac-ping/SAA/验证链（排障独立可用）
7. `unp-dynamic-ov2500`——UNP 动态服务与 OV2500 编排
8. `spb-hybrid-etree`——Hybrid 口与 E-Tree

前 3 个是主线必读；4-6 按场景查；7-8 是 Day3 自动化增强。

## 七、实施陷阱清单

骨干与服务层：
- 控制 BVLAN 只能在 `spb isis admin-state disable` 时改（改不动先查协议状态）。
- BVLAN 自动禁 STP、不学客户 MAC、不泛洪——别指望 STP 在骨干做环保护。
- metric 单侧改无效，引流必须两端同步。
- 绑 IP 接口瞬间 vlan-xlation 隐式启用且锁定不可改；规划期先定翻译需求。
- 同一 I-SID 不能既 bind 又 redist 到同一 VRF；VPN-Lite 两个 VRF 不能共享同一 I-SID。

保护与冗余：
- LBD 在 linkagg 上封整组；封口裁决规则是跨机关较高 BridgeID、同机关较高 PortID——预判被封口，别误判设备故障。
- 接入层并行双路径无 STP/LBD 兜底必成环：SPB 骨干无环不等于接入无环（p131 实验复现）。
- ERP 六条铁律（p23）：BEB 不能做 RPL 节点；ERP 服务必须配在**控制 BVLAN**；环不能建在 802.1q tag 口；每 SVLAN 最多 2 个 ERP NNI；多环 VLAN 范围互斥。
- DHL 每交换机只允许一个会话。

动态与增强：
- UNP：SNMP 用户名禁用 admin/diag/user（建号失败先查保留字）；隔离用户不能靠重定向补救。
- E-Tree：两端都配 e-tree = 全 Leaf 死网；用户报"同服务两站不通"先查是否都是 Leaf——这是设计语义，不是故障。
- 老平台（6900-X20 等）无内联路由能力，回环口独占且 linkagg 回环只能删组解除，端口预算要扣除。

---

*由 cangjie-skill 流水线从 DT00XTE323EN 蒸馏生成。*
