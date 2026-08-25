---
name: AOS 8 路由策略工具箱（Route Map/重分发/AS 正则/策略列表）
description: 需要在 OmniSwitch AOS 8 上用 route map 控制路由重分发（OSPF/IS-IS/BGP/local 互注）、设计 Action/Match/Set 逻辑、用 IP 访问列表聚合地址、写 AS Path 正则、创建 aspath/community/prefix 列表等策略原子件时使用。
source_book: OmniSwitch AOS Release 8.10R4 Advanced Routing Guide
---

## R（触发场景）
- 要在协议间重分发路由（OSPF↔BGP、local→OSPF、IS-IS↔IS-IS 泄漏等）并精细过滤
- 要设计 route map：序列号、permit/deny、match 条件组合（AND/OR 语义）、set 动作
- 要写 AS Path 正则过滤 BGP 路由，或建 aspath-list/community-list/prefix-list 原子策略
- 排查"重分发没生效/多分发了"：deny 语义、无 match 兜底、子策略未建等坑

## I（核心理念）
Route Map 重分发统一模型（F4，跨 OSPF/OSPFv3/IS-IS/BGP 四章复用）：route map 由 Action（名称+序列号+permit/deny）/Match/Set 三类语句构成（P26）；序列之间隐含 OR，同类型 match 之间 OR、不同类型之间 AND（P27）；无 match 语句则重分发所有路由（P28）；未配序列号默认取 50（P29）。deny 某路由不等于默认放行其余——每条路由都要有明确的 permit/deny 规则（P30）。set metric 支持 add/subtract/replace/none 四种效果（P31）。BGP 策略体系（F5）在此之上加四类原子策略列表 + peer 的 in/out 绑定（P78）。

## A1（决策框架）
1. **先建原子件再组 route map**：IP 访问列表/prefix-list/aspath-list 先创建，route map 引用不存在的子策略直接报错（X39）
2. **设计过滤逻辑**：sequence 10 deny（match 排除项）→ sequence 20 permit（match+set 主逻辑）→ sequence 30 permit 兜底（set 通用属性），C6 三段式是标准模板
3. **协议间搬运**：`ip redist <src> into <dst> route-map <name>`，源/目的协议都必须已加载并使能（P33）
4. **BGP 侧绑定方向**：策略绑到 peer 的 in（学习）/out（通告）方向，改动后 `clear soft in|out` 重应用（P78/P89）
5. **被动接口批量生成**：local 路由 + set metric-type internal 重分发进 OSPF（P21/C7）

## A2（操作步骤）
- **三段式模板（OSPF→BGP）**：`ip route-map ospf-to-bgp sequence-number 10 action deny`（match tag 5 + route-type external type2）→ sequence 20 permit（match ipv4-interface intf_ospf + set metric 255）→ sequence 30 permit（set tag 8）→ `ip redist ospf into bgp route-map ospf-to-bgp`（C6，<<<PAGE 44-45>>>）
- **被动接口批量**：`ip route-map "R1" action permit` + `match ip-address 10.10.0.0/16` + `set metric-type internal` → `ip redist local into ospf route-map R1 admin-state enable` → `show ip ospf interface`（C7，<<<PAGE 46>>>）
- **IS-IS L1→L2 泄漏**：`ip route-map is2is sequence-number 1 action permit` + `match route-type level1` + `set level level2` → `ip redist isis into isis route-map is2is status enable`（C17，<<<PAGE 115>>>）
- **BGP 原子策略**：`ip bgp policy aspath-list aspathfilter "^100 200$" action permit`；community-list + match-type exact；prefix-list + ge/le → `ip bgp neighbor 172.22.2.0 in-aspathlist ...` / `route-map mapfilter in|out` → `clear soft in|out`（C29，<<<PAGE 201-210>>>）
- **验证**：`show ip route-map` / `show ip redist` / `show ip bgp policy ...`

## E（实证案例）
- OSPF→BGP 三段式重分发（deny→permit+set→兜底）（C6，<<<PAGE 44-45>>>）
- 用 route map 批量生成 OSPF 被动接口（C7，<<<PAGE 46>>>）
- IS-IS L1→L2 泄漏（C17，<<<PAGE 115>>>）
- BGP 五类策略创建 + peer 绑定 + soft 重应用（C29，<<<PAGE 201-210>>>）

## B（反例/坑）
- deny 某路由不等于默认放行其余路由，每条都要显式规则（P30，<<<PAGE 42, 168>>>）
- 无 match 语句的 route map 会重分发所有路由（P28，<<<PAGE 77, 111>>>）
- route map 引用的子策略（访问列表等）必须先创建否则报错（X39，<<<PAGE 205>>>）
- 重分发要求源/目的协议均已加载并使能（P33，<<<PAGE 43>>>）
- 配置重分发即自动成为 ASBR（P22）；iBGP→OSPF 重分发默认禁止需显式开启（P23，<<<PAGE 48>>>）
- AS 正则按 token 匹配 AS 号而非字符（P76）；元字符错误：数字超 65535、逗号当分隔符、括号嵌套、^ 不在首/$ 不在尾（X28，<<<PAGE 136>>>）
- IS-IS route map 的 tag 参数当前版本不支持（X17，<<<PAGE 110>>>）
- BGP 部分 peer 命令改后须手动 clear 才生效（X35，<<<PAGE 149>>>）

## 来源
OmniSwitch AOS 8.10R4 Advanced Routing Guide 第 1 章 Route Map 与重分发（<<<PAGE 40-48>>>）、第 2/3 章对应节（<<<PAGE 76-78, 110-115>>>）、第 4 章策略节（<<<PAGE 133-134, 166-169, 201-210>>>）。条目来源：cases C6/C7/C17/C29；principles P21-P33/P76/P78/P89；counter-examples X17/X28/X35/X39；frameworks F4/F5。
