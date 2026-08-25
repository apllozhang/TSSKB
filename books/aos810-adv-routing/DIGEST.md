# DIGEST — OmniSwitch AOS 8.10R4 Advanced Routing Guide 精华

本书是 ALE OmniSwitch AOS Release 8.10R4 的高级路由手册（313 页，8 个协议章），覆盖 OSPF/OSPFv3、IS-IS、BGP（含 IPv6 MP-BGP/EVPN/VPLS）、组播地址边界、DVMRP、PIM 与 MBR。全书有三条公共骨架贯穿各章：**统一配置范式**（准备网络 → ip load → enable → 区域/area-id → 接口挂接 → 可选特性 → show 验证）、**Route Map 策略框架**（Action/Match/Set 跨四章复用）、**优雅重启模型**（重启方通告 + helper 维持 + 宽限期）。高级路由协议需购买附加包（<<<PAGE 12>>>）。以下按五个技能单元摘要，页码均指原书。

## 一、知识地图（五技能单元）

1. **OSPF/OSPFv3**（aos-ar-ospf-ospfv3）：区域分层、Stub/NSSA/Totally Stubby、虚链路、认证、被动接口、NBMA、GR（Ch1-2，p20-88）。
2. **IS-IS**（aos-ar-isis）：area-id/NET、Level-1/2 层级、分层认证、L1→L2 泄漏、汇总、M-ISIS 多拓扑（Ch3，p89-121）。
3. **BGP 与策略**（aos-ar-bgp）：七步上线、EBGP/IBGP、RR/联邦、聚合/dampening、IPv6 MP-BGP、GTSM、EVPN/VPLS、邻居模板（Ch4，p123-218）。
4. **组播高级**（aos-ar-multicast-advanced）：239/8 地址边界域复用、DVMRP（含隧道）、PIM DM/SM/SSM、Anycast RP、IPv6 PIM、MBR（Ch5-8，p220-303）。
5. **路由策略工具箱**（aos-ar-policy-toolbox）：Route Map 三类语句与逻辑语义、三段式重分发模板、IP 访问列表、AS 正则、四类 BGP 原子策略（跨章，p40-48/133-134/201-210）。

## 二、五单元要点串讲

### 1. OSPF/OSPFv3：区域即知识隔离
泛洪保证全区域一致 LSDB、各自算 SPF（<<<PAGE 24>>>）。区域隔离拓扑知识，骨干区负责区间分发，ABR 每区域跑一份 SPF 并浓缩拓扑（P6-P10）。末节区域三档递进：Stub（无外部 LSA）→ Totally Stubby（再滤 Type-3，实现=Stub+`summary disable`，P19）→ NSSA（Type-7 选择性导入）。虚链路是最后手段（X3）。认证三套（simple/MD5/keychain-SHA256），MD5 的 key ID 与 key string 必须两条命令（X7）。被动接口会立即拆除已有邻接（X8），多区域域中只生成在最小 Area ID（X9）。OSPFv3 整体 ipv6 镜像（F10），但 Loopback0 不会自动通告须配 point-to-point（P40）、静态邻居用链路本地地址（P41）。

### 2. IS-IS：路由器整体属单区域
两层层级（L1 区内/L2 区间），与 OSPF 最大差异是路由器不按接口分域（P47）。NSAP=Area ID+System ID+NSEL。邻接三要素：认证、IS 类型、MTU（P45）。认证四层（全局/level/电路/电路级）低层覆盖全局（P50）；点到点口 L1 未配认证则 L1 hello 裸奔（X21）。L1→L2 泄漏经 route map（C17）；内部路由不能在 L1 汇总（X20）；metric>64 须先开 wide-metrics（X18）。双栈域内有 v4-only/v6-only 设备必须 M-ISIS（否则黑洞，P54），切换多拓扑会复位全部邻接（X23）。

### 3. BGP：策略即商业关系
TCP 179 增量更新；AS_PATH 兼做环路检测（P60/P61）。选路两大属性：Local Preference（AS 内越高越优先）与 MED（仅同邻居 AS 间比较、绝不外传，P71）。iBGP 扩展：RR 按来源反射（外部→全部、non-client→client、client→全部，P66），冗余 RR 用 cluster-id 且 RR 间全互联；联邦子 AS 间走 EBGP 但属性保留（P69）。聚合需至少一条更精确路由（X30）；dampening 参数必须整条按序输入（X29）。全局命令（AS 号/本地优先等）改前须禁 BGP（X25）；CLI 不吃 CIDR 斜杠（X26）。IPv6 走 MP-BGP，v6 前缀可跑在 v4 会话上（activate-ipv6+ipv6-nexthop）；纯 v6 域必须显式配 router-id 与 IPv4 primary（X36）。GTSM 与 multihop 互斥且两端同配（X38）。

### 4. 组播：三范式 + 域隔离
密集（泛洪-剪枝）/稀疏（显式 Join+RP）/SSM（免 RP 直连源）三范式按接收者分布与源可知性选型（F7）。地址边界让 239/8 同段在多域并发复用（C33）；PIM-SM 五要素体系：RP 解封装 Register、BSR 分发 RP-set、DR 双侧职责、RPT/SPT 双树、末跳 DR 收首包即 SPT 切换（F8）。RP 供给三选一（C-RP+BSR/静态/Anycast）；Anycast RP 收敛与 IGP 同级但静态 RP 须全网配（X63）且 RP 地址不能与 Router ID 相同（X62）。MBR 同机跑 DVMRP+PIM 实例打通两域，但每接口只能一个组播协议（X44）且不支持 SSM（X68）。

### 5. 策略工具箱：一套语法四处使用
Route Map = Action（序列+permit/deny）+ Match + Set；序列间 OR、同类 match OR、异类 AND（P27）；无 match 即全量（P28）；deny 不等于其余默认放行（P30）。三段式模板：deny 排除 → permit+set 主逻辑 → permit 兜底（C6）。BGP 加四类原子列表（aspath/community/prefix/prefix6）绑 peer in/out，改后 clear soft（P78/P89）。AS 正则按 token 匹配（P76），元字符错误是最常见翻车点（X28）。

## 三、高价值章节页码索引

| 主题 | 页码 |
|---|---|
| OSPF 原理/区域/角色 | 24-33 |
| OSPF 配置任务列表 | 31-48 |
| Stub/NSSA/虚链路 | 26-39 |
| 认证（simple/MD5/keychain） | 37-38 |
| 三区域应用例 | 49-53 |
| OSPFv3 全章 | 55-88 |
| IS-IS 全章 | 89-121 |
| M-ISIS 多拓扑 | 120-121 |
| BGP 原理/属性 | 123-146 |
| AS 正则/策略 | 133-134, 201-210 |
| RR/联邦 | 161-165 |
| dampening/聚合 | 152-159 |
| BGP GR | 172 |
| IPv6 MP-BGP | 177-200 |
| GTSM | 212-213 |
| EVPN/VPLS/模板 | 214-218 |
| 组播地址边界 | 220-228 |
| DVMRP | 229-244 |
| PIM（DM/SM/SSM/RP 体系） | 247-296 |
| MBR | 297-303 |

## 四、一句话总纲

AOS 高级路由的学好抓手是"三个统一"：配置范式统一（load→enable→区域→接口挂接→show）、策略框架统一（route map 一套语法打 OSPF/IS-IS/BGP）、GR 模型统一（通告+helper+宽限期）；排障先对三张反例清单——邻接起不来查区域类型/认证/MTU 一致性，路由没来查重分发 deny 语义与协议使能前提，策略不生效查子策略创建顺序与 clear soft。
