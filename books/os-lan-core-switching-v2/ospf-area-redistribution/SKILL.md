---
name: OSPF 区域设计与路由重分发
description: 需要部署 OSPF（区域规划、stub/NSSA、虚链路、认证）或做 local/static 路由重分发进 OSPF 时使用本技能。
source_book: DT00XTE216 OmniSwitch LAN Core Switching Ed15
---

## R（触发场景）
- 园区/骨干要划分 OSPF 区域，纠结 Standard/Stub/Totally Stubby/NSSA 选型
- 区域无法直连 Area 0，需要 Virtual Link
- 直连/静态路由要注入 OSPF（重分发 + route-map），或邻居起不来要排障

## I（核心理念）
OSPF 分区的收益是减少 LSA 传播量：区域类型决定允许进入的 LSA 集合（Stub 拒 Type5 注默认路由，Totally Stubby 再拒 Type3，NSSA 用 Type7 引外部路由）。重分发的通用范式是"先 route-map 后 redist"：route-map 序列自上而下、命中即停，执行 `ip redist` 的路由器即成为 ASBR。邻居建立的前提是 hello/dead/area/认证参数完全一致。

## A1（行动框架）
1. 七步法（<<<PAGE 275>>>-<<<PAGE 280>>>）：①配 router-id（`ip interface Loopback0 address 192.168.254.1` → `ip router router-id 192.168.254.1`）②`ip load ospf` ③`ip ospf area 0.0.0.0` ④指定区域类型 ⑤`ip ospf interface int_217` ⑥`ip ospf interface int_217 area 0.0.0.0` ⑦`admin-state enable` → `ip ospf admin-state enable`（<<<PAGE 325>>>-<<<PAGE 330>>>）
2. 验证三步：`show ip ospf`（# of Full State Nbrs）、`show ip ospf lsdb`（rtr/net LSA）、`show ip ospf interface`（DR/BDR）（<<<PAGE 325>>>-<<<PAGE 330>>>）
3. 多区域+虚链路：`ip ospf area 1.1.1.1` + 接口入域；两端配 `ip ospf virtual-link 1.1.1.1 192.168.254.2`（对端 router-id）；`show ip ospf virtual-link`（State P2P/Full, up）（<<<PAGE 332>>>-<<<PAGE 339>>>）
4. 重分发：`ip route-map localIntoOspf sequence-number 10 action permit / match ip-address 192.168.120.0/24 permit` → `ip redist local into ospf route-map localIntoOspf admin-state enable`（默认路由 match 0.0.0.0/0）；验证 `show ip ospf routes` 出现 AS-Ext (E2)（<<<PAGE 347>>>-<<<PAGE 352>>>）
5. 认证：Simple `auth-type simple` + `auth-key alcatel`；MD5 `auth-type md5` + `md5 1` + `md5 1 key alcatel`，双端一致（<<<PAGE 353>>>-<<<PAGE 354>>>）
6. Stub：`ip ospf area 4.4.4.4 type stub`（双端一致），区域內路由表只剩 Intra/Inter + ABR 注入的 Inter 默认路由（<<<PAGE 355>>>-<<<PAGE 356>>>）

## A2（进阶应用）
- 邻居排障：`swlog appid ospf_0 subapp all level debug3` + `show log swlog | grep ospf_0`，可抓到 "HELLO ... discarded ... invalid helloInterval" 类证据（<<<PAGE 292>>>-<<<PAGE 294>>>）
- LSA 速查：Type1 每路由器域内泛洪 / Type2 DR 生成 / Type3 ABR 汇总（域内路由在 ABR 做 summarization）/ Type4 通告 ASBR 位置 / Type5 ASBR 外部（外部路由在 ASBR 做 aggregation）/ Type7 NSSA 专用由 ABR 转 Type5 出域（<<<PAGE 260>>>-<<<PAGE 267>>>、<<<PAGE 286>>>-<<<PAGE 287>>>）
- ECMP：等价路径最多 4 条、按流分担、不支持逐包（<<<PAGE 285>>>）
- Graceful Restart：重启期间邻居维持邻接避免全网 SPF；OSPF/ISIS 默认关、BGP 默认开（<<<PAGE 359>>>-<<<PAGE 363>>>）
- route-map 组合逻辑：同序列多 match 为 AND，同 match 多值为 OR（<<<PAGE 305>>>）

## E（实证案例）
- C-22 两个独立骨干经 transit area 用虚链路互联，`show ip ospf virtual-link` State P2P/Full（<<<PAGE 332>>>-<<<PAGE 339>>>）
- C-23 local/static 两类重分发，E2 路由识别（<<<PAGE 347>>>-<<<PAGE 352>>>）
- C-26 swlog 日志分级定位 Hello interval 不匹配（本端 20 对端 10），改一致后 Full（<<<PAGE 292>>>-<<<PAGE 294>>>）

## B（边界与陷阱）
- 单端先开认证会立刻丢邻居（"Auth type 1 mismatch!"），生产开认证需两端窗口期内同步（<<<PAGE 353>>>）
- Hello interval 等邻居参数不一致导致无法 Full，用 swlog debug 定位（<<<PAGE 293>>>-<<<PAGE 294>>>）
- Stub 区域两端 area type 必须一致，一端 stub 一端 normal 邻居起不来；stub 内看不到外部路由（<<<PAGE 355>>>-<<<PAGE 356>>>）
- route-map 命中 deny 序列即停止且不重分发该路由（<<<PAGE 304>>>）

## 来源
- framework·F-05 Area 设计决策框架（<<<PAGE 253>>>-<<<PAGE 254>>>、<<<PAGE 267>>>-<<<PAGE 270>>>）
- framework·F-06 配置七步法（<<<PAGE 275>>>-<<<PAGE 280>>>）
- framework·F-07 重分发两步法（<<<PAGE 272>>>-<<<PAGE 273>>>、<<<PAGE 300>>>）
- principle·P-39/P-40/P-41/P-42/P-43/P-44/P-45/P-46/P-47/P-48（<<<PAGE 240>>>-<<<PAGE 305>>>、<<<PAGE 359>>>-<<<PAGE 363>>>）
- case·C-21/C-22/C-23/C-24/C-25/C-26；counter·X-14/X-15/X-16
