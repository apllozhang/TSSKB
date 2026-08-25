---
name: IP 路由（静态/RIP/OSPF/GR + BGP/IS-IS/IPv6/SLB 扩展）
description: 需要配置 OmniSwitch 静态路由与路由偏好、RIP 四定时器与重分发、OSPF 区域/LSA/虚链路/Graceful Restart/BFD/ECMP、BGP 邻接与策略、IS-IS、IPv6 基础或 SLB 服务器负载均衡时使用本技能。
source_book: DT00CTE120 OmniSwitch R6/R8 Bootcamp Issue 25
---

## R（触发场景）
- 园区三层层间互通：静态/RIP/OSPF 选型与配置
- OSPF 区域设计（Stub/NSSA/虚链路）、路由汇总与重分发
- 计划主控重启要求转发不中断（Graceful Restart）
- 快速故障检测（BFD）、等价多路径（ECMP）
- 对接外部 AS（BGP）或扁平化大型二层底座（IS-IS）
- 本地服务器集群负载均衡（SLB VIP/WRR/探针）
- IPv6 地址规划基础

## I（核心理念）
路由体系的骨架是偏好值：AOS 默认 Local 1 / Static 2 / OSPF 10 / RIP 100 / BGP 200，可手工调整（P147，<<<PAGE 769>>>），静态永远优先于动态（P135，<<<PAGE 714-716>>>）。RIP 是距离向量（跳数 16 不可达、30 秒全表更新），四定时器 update 30/invalid 180/garbage 120/holddown 0 且 invalid≥3×update 由 AOS 强制（P138/P140，<<<PAGE 724, 730-731>>>）。OSPF 三数据库（邻接表/LSDB/路由表）+ SPF 并行计算（P142，<<<PAGE 753>>>）；区域类型本质是"允许进入的 LSA 集合"（F13/P144，<<<PAGE 759-762>>>）。GR 的契约是重启方保持转发、邻居做 helper 不重算 SPF，Grace LSA（Type 9 Opaque）携宽限期（P148/P149，<<<PAGE 772-775>>>）。重分发范式全书统一："先 route-map 后 redist"（P141，<<<PAGE 726-727>>>）。

## A1（决策/选型）
1. IGP 选型：小网络 RIP（v2 组播 224.0.0.9、带认证，P139，<<<PAGE 724>>>）；中大型 OSPF；超大型/SPB 底座用 IS-IS（直接跑在 802.3/802.2 二层，P202，<<<PAGE 1093-1096>>>）
2. OSPF 区域裁剪：Stub（拒 Type5）/ Totally Stubby（仅默认路由）/ NSSA（Type7 注入本区外部）（P144，<<<PAGE 760>>>）；不接骨干的区域走 virtual-link（P146，<<<PAGE 763>>>）
3. GR 默认状态：OSPF/ISIS 默认关、BGP 默认开（X65，<<<PAGE 776>>>）
4. SLB 双模式：VIP 模式（L3 路由/桥接代理 ARP）vs QoS Condition 模式（按策略条件截流，如防火墙集群）（P196，<<<PAGE 981-985>>>）

## A2（操作步骤）
1. 静态路由：普通下一跳 / 递归 `follows`（网关随动态路由变化，6.7.1 无此选项）/ 出接口型（P136/P137，<<<PAGE 719-721>>>）；`show ip router database` 看含未用路由（<<<PAGE 718, 720>>>）
2. RIP：`ip load rip` → `ip rip admin-state enable` → `ip rip interface int_217` + `admin-state enable`；验证 `show ip rip interface/peer/routes`；重分发 `ip route-map rip_1 sequence-number 50 action permit` + `match ip-address 0.0.0.0/0` → `ip redist local into rip route-map rip_1 admin-state enable`；定时器 `ip rip update-timer 45`/`invalid-timer 270`/`garbage-timer 180`/`holddown-timer 10`；版本/MD5 认证按需（C38，<<<PAGE 733-745>>>）
3. OSPF 骨干：`ip load ospf` → `ip router router-id 192.168.254.1`（可被 Loopback0 覆盖，P143，<<<PAGE 754>>>）→ `ip ospf area 0.0.0.0` → 各接口 `ip ospf interface int_217` + area + enable → `ip ospf admin-state enable`；验证 `show ip ospf/area/interface/routes/lsdb/neighbor`；保存 `configuration snapshot all save-ospf-backbone`（C39，<<<PAGE 779-792>>>）
4. OSPF 重分发与外部聚合：localIntoOspf/staticIntoOspf route-map（match 192.168.100.0/24 与 0.0.0.0/0）→ `show ip ospf ext-lsdb`；ASBR 聚合 `ip access-list extip address 150.215.0.0/16 action permit redist-control aggregate`；虚链路 `ip ospf virtual-link 2.2.2.2 192.168.10.2`（C39/C40，<<<PAGE 763, 768, 779-792>>>）
5. OSPF 认证：simple（`auth-type simple`+`auth-key alcatel`）或 MD5（`md5 1`+`md5 1 key alcatel`）后邻居重建（C39，<<<PAGE 779-792>>>）
6. 偏好调整：`show ip route-pref` → `ip route-pref rip 8`（C39，<<<PAGE 768-769>>>）
7. BGP：`ip router router-id` → `ip load BGP` → `ip bgp status enable` → `ip bgp autonomous-system 100` → `ip bgp neighbor 100.10.1.1` + remote-as + status enable（可 `md5 key`）；`update-source Loopback0`、`ebgp-multihop`；策略三列表 aspath-list/community-list/prefix-list 配合 route-map（C56/P199/P200，<<<PAGE 1080-1088>>>）
8. IS-IS：`ip load isis` → `ip isis admin-state enable` → `ip isis area-id 49.0001`（AFI=49 本地管理，P203，<<<PAGE 1094-1095>>>）→ `ip isis activate-ipv4` → `ip isis vlan 5 address-family v4 admin-state enable`；层级 `ip isis vlan 10 level-capability level-1/2`；验证 `show isis status`、`show ip isis adjacency/route/spf`（C57/P206，<<<PAGE 1105-1106>>>）；PDU 四类 Hello/LSP/PSNP/CSNP 与 DIS 可抢占选举（P204/P205，<<<PAGE 1096-1103>>>）
9. SLB：`ip slb admin-state enable`(R8) → `ip slb cluster Web vip 128.241.130.204`（VIP 须与服务器同网段，集群自动 proxy ARP，P194，<<<PAGE 975>>>）→ `ip slb server ip <ip> cluster Web`；WRR `weight 1/3`、备份机 `weight 0`（总权重 ≤32，P195，<<<PAGE 977-979>>>）；QoS Condition 集群 `ip slb cluster Firewall condition cond1 L3`；探针 `ip slb probe http_test http` + `period 10`（20 个/switch，P197，<<<PAGE 986-987>>>）（C54，<<<PAGE 976-987, 995>>>）
10. IPv6 基础：128bit、:: 仅一次、FE80::/10 链路本地、EUI-64（插 FFFE 翻 U/L 位）（P208-P210，<<<PAGE 1133-1138>>>）

## E（实证案例）
- C38 RIP 骨干：linkagg 18 承载 + 重分发本地/静态 + 定时器调优（<<<PAGE 733-745>>>）
- C39 OSPF 骨干：区域/认证/重分发/route-pref 全要素（<<<PAGE 779-792>>>）
- C54 SLB 三合一：VIP + WRR 权重 + HTTP 探针（<<<PAGE 976-987, 995>>>）
- C56/C57 BGP 邻接与 IS-IS 基础（<<<PAGE 1080-1088, 1105-1106>>>）

## B（反例与坑）
- RIP invalid 必须 ≥3×update（AOS 强制）；默认不通告本地/静态路由，必须重分发（X62/X63，<<<PAGE 730, 726>>>）；默认收 v1/v2 发 v2、无认证（X64，<<<PAGE 745, 748>>>）
- OSPF/ISIS 的 GR 默认关、BGP 默认开（X65，<<<PAGE 776>>>）；递归静态路由 6.7.1 不可用（X66，<<<PAGE 719>>>）
- IBGP 学到的路由不应再传 IBGP 邻居（全互联或路由反射器，X67/P201，<<<PAGE 1082>>>）
- SLB WRR 权重总和 ≤32；weight 0 为备份（P195，<<<PAGE 977-979>>>）
- IS-IS 用 802.3/802.2 而非 Ethernet II——与 IP 流量混跑时注意抓包过滤（P202，<<<PAGE 1093-1096>>>）

## 来源
- principles·P135-P149/P193-P210；frameworks·F13；cases·C38-C40/C54/C56/C57；counter-examples·X62-X67
