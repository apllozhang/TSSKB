---
name: AOS 8 BGP 与路由策略（EBGP/IBGP/RR/联邦/IPv6 MP-BGP/dampening/聚合）
description: 需要在 OmniSwitch AOS 8 上配置 BGP（邻居建立、EBGP/IBGP、Route Reflector、联邦、聚合、dampening、IPv6 MP-BGP、GTSM、EVPN/VPLS 地址族、邻居模板）时使用。
source_book: OmniSwitch AOS Release 8.10R4 Advanced Routing Guide
---

## R（触发场景）
- 新上线 BGP：router-id/primary → ip load bgp → AS 号 → 邻居 remote-as → 使能七步
- iBGP 全互联太贵：要部署 Route Reflector（含冗余 cluster-id）或联邦
- 要做路由聚合（summary-only/as-set）、抖动抑制 dampening、属性策略（local-preference/MED/community）
- IPv6 对等（纯 v6 域或 IPv4 会话跑 v6 前缀）、GTSM 防攻击、EVPN/VPLS 地址族、邻居模板

## I（核心理念）
BGP 是 AS 间 EGP，跑在 TCP 179 上，增量更新使长会话更高效（P60）；AS_PATH 承担 AS 级环路检测（P61）。选路属性体系：Local Preference（AS 内、越高越优先）与 MED（仅同一邻居 AS 间比较、绝不向下一 AS 传播）（P71/P77）。iBGP 全互联规则由 RR 放松（P65），RR 通告按路由来源决定反射范围（P66）；联邦以子 AS 间 EBGP 模拟整体 IBGP（P69）。策略体系（F5）：aspath/community/prefix(prefix6)/route-map 四类原子策略先建后绑到 peer 的 in/out 方向，改动后 clear soft 重应用（P78/C29）。IPv6 由 MP-BGP 的 MP_REACH/MP_UNREACH_NLRI 承载，v6 前缀可跑在 v4 会话上（P80/P81）。

## A1（决策框架）
1. **邻居设计**：peer 必须逐个显式配置、不会动态学习（X34）；Loopback0 永久 up 适合作对等源（update-source + ebgp-multihop）（P88）
2. **iBGP 扩展选型**：中小型用 RR（冗余 RR 用 cluster-id、RR 间全互联，P68）；超大型用联邦（子 AS 间 EBGP、属性跨子 AS 保留，P69）；两者都嫌重才全互联
3. **路由整合**：聚合需至少一条更精确路由存在（X30）；不稳定路由用 dampening（半衰期折半、低于 reuse 重新通告，P73）
4. **安全加固**：GTSM（TTL 置 255 按剩余跳数丢弃，P83）与 eBGP multihop 互斥且须两端同配（X38）
5. **IPv6 选型**：双栈走 IPv4 会话 + activate-ipv6 + ipv6-nexthop（C26）；纯 IPv6 域必须显式配 router-id 与 IPv4 primary 地址（X36）

## A2（操作步骤）
- **七步上线**：`ip router router-id 1.1.1.1` + `ip router primary-address 1.1.1.1` → `ip load bgp` → `ip bgp autonomous-system 100` → `ip bgp admin-state enable` → `ip bgp neighbor 198.45.16.145` → `ip bgp neighbor ... remote-as 200` → `ip bgp neighbor ... admin-state enable`（C20，<<<PAGE 125>>>）
- **RR 四步**：`ip bgp admin-state disable` → `ip bgp client-to-client reflection` → 逐 client `ip bgp neighbor 190.17.20.16 route-reflector-client` → 冗余 `ip bgp cluster-id 190.17.21.16`（C23，<<<PAGE 162-163>>>）
- **联邦**：`ip bgp confederation-identifier 2` → `ip bgp confederation neighbor 190.17.20.16`（逐个加全）（C24，<<<PAGE 165>>>）
- **聚合**：`ip bgp aggregate-address 172.22.2.0 255.255.255.0` → `summary-only` → `as-set` → community/local-preference/metric → `admin-state enable`（C22，<<<PAGE 152>>>）
- **dampening**：`ip bgp dampening half-life 500 reuse 200 suppress 300 max-suppress-time 1800`（改任一参数须整条按序重输）；`ip bgp dampening clear` 清历史（C25，<<<PAGE 157-159>>>）
- **IPv6（v4 会话）**：`ip bgp neighbor 23.23.23.23` → remote-as 200 → `activate-ipv6` → `ipv6-nexthop 2001:100:3:4::1` → enable（C26，<<<PAGE 178>>>）；纯 v6 对等 `ipv6 bgp neighbor 2001::1` + update-source（C27）
- **策略绑定**：`ip bgp policy aspath-list aspathfilter "^100 200$" action permit` 等四类 → `ip bgp neighbor 172.22.2.0 in-aspathlist|route-map mapfilter in|out` → `clear soft in|out`（C29，<<<PAGE 201-210>>>）
- **GTSM**：`ip bgp neighbor 10.0.0.1 ttl-security 6`（直连对等用 0）；`show ip bgp neighbors` 验证（C30，<<<PAGE 212-213>>>）
- **EVPN/VPLS/模板**：`ip bgp address-family evpn` + `activate-evpn` + fabric 邻居 `evpn-nbr-type-fabric`；VPLS `address-family l2vpn-vpls`；模板 `ip bgp nbr-template Mytemplate`（C31，<<<PAGE 214-218>>>）

## E（实证案例）
- EBGP/IBGP 混合五 speaker 应用例（C21，<<<PAGE 173-175>>>）
- Route Reflection 四步与冗余 RR（C23，<<<PAGE 162-163>>>）
- IPv6 BGP 全场景应用例（双栈/纯 v6 域）（C28，<<<PAGE 195-198>>>）
- 五类策略创建 + peer 绑定 + soft 重应用（C29，<<<PAGE 201-210>>>）
- GTSM 配置验证（C30，<<<PAGE 212-213>>>）

## B（反例/坑）
- 一批全局命令（AS 号、本地优先、MED、RR、cluster-id）改前必须先禁用 BGP（X25，<<<PAGE 139>>>）
- CLI 不支持 CIDR 斜杠写法，必须写全掩码（X26，<<<PAGE 137>>>）
- AS 正则错误：数字超 65535、逗号当分隔符、括号嵌套、^ 不在首/$ 不在尾（X28，<<<PAGE 136>>>）
- dampening 参数必须整条按序一次输入（X29，<<<PAGE 157>>>）
- 聚合前 BGP 表内须至少一条更精确路由（X30，<<<PAGE 152>>>）
- 冗余 RR 过多推高内存（X31，<<<PAGE 163>>>）；同步开启给 AS 内非 BGP 路由器带来大负担（X32，<<<PAGE 144>>>）
- BGP 软件不随启动自动加载，须手动 ip load bgp（X33，<<<PAGE 125>>>）
- 部分 peer 命令（定时器等）不自动复位会话，须手动 clear（X35，<<<PAGE 149>>>）
- 纯 IPv6 网必须显式配 router-id 与 IPv4 primary 地址（X36）；IPv4 对等已建会话时不能关 IPv4 unicast（X37）（<<<PAGE 179-180>>>）
- GTSM 与 eBGP multihop 互斥，且须两端同配（X38，<<<PAGE 212>>>）
- route map 引用的子策略必须先创建否则报错（X39，<<<PAGE 205>>>）
- VPLS 依赖 MPLS license 与二进制，启用前须先禁 BGP（X40，<<<PAGE 214>>>）
- 邻居模板当前仅支持 EVPN 族命令（X41）；个体 peer 配置覆盖模板，想生效先删个体配置（X42）；VRF 内 peer 默认上限 32（X43）（<<<PAGE 218, 144>>>）
- MED 只在同一邻居 AS 间比较且绝不向下一 AS 传播（P71，<<<PAGE 143>>>）

## 来源
OmniSwitch AOS 8.10R4 Advanced Routing Guide 第 4 章 BGP（<<<PAGE 123-218>>>）。条目来源：cases C20-C31；principles P60-P90；counter-examples X25-X43；frameworks F5/F6。
