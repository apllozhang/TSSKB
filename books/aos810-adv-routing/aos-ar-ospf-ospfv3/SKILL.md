---
name: AOS 8 OSPF/OSPFv3 区域设计与高级特性（Stub/NSSA/虚链路/认证/GR）
description: 需要在 OmniSwitch AOS 8 上配置 OSPF/OSPFv3（区域规划、Stub/NSSA/Totally Stubby、虚链路、接口认证 simple/MD5/keychain、被动接口、NBMA 静态邻居、优雅重启 GR）时使用。
source_book: OmniSwitch AOS Release 8.10R4 Advanced Routing Guide
---

## R（触发场景）
- 新上线 OSPF/OSPFv3：VLAN→IP 接口→router-id→load/enable→区域→接口挂区的标准九步
- 区域设计：骨干+普通区域、Stub/Totally Stubby/NSSA 选型、ABR 汇总（area range）
- 骨干不连续要用虚链路修复；或 NBMA 网络要配静态邻居
- 接口认证（simple/MD5/keychain-SHA256）、被动接口批量生成、CMM 冗余优雅重启（GR）

## I（核心理念）
链路状态统一原理骨架（F2）：本地状态经泛洪保证全区域一致 LSDB，各路由器以自身为根算 SPF 树得路由表（P1/P2）。区域分层体系（F3）：区域隔离拓扑知识以减少路由流量（P6），骨干区 Area 0.0.0.0 负责区间分发（P7），路由器按 Internal/ABR/Backbone/ASBR 四角色分类（P9），ABR 为每个所连区域跑一份 SPF 并浓缩拓扑（P10）。OSPFv3 是 v2 的 IPv6 扩展、GR 默认使能（P34），命令族整体 ipv6 镜像（F10）。IGP 配置统一骨架（F1）：准备网络 → ip load → admin-state enable → 建区域 → 接口挂区 → 可选特性 → show 验证。

## A1（决策框架）
1. **末节区域选型**：Stub（无外部 LSA、默认路由出域，P12）→ Totally Stubby（再滤 Type-3，实现=Stub+关汇总，P19）→ NSSA（Type-7 LSA 选择性导入外部，P13）
2. **骨干不连续**：虚链路两端互指对端 Router ID + 共同 transit 区（C4）；但虚链路是最后手段，不连续骨干是劣构设计（X3）
3. **认证选型**：simple / MD5（key ID 与 key string 两条命令，P25）/ keychain（可 SHA256，支持密钥轮转）（P24/C5）
4. **终端网段**：被动接口通告网段但不建邻接（P20）；或用 route map 重分发 local 为 internal 批量生成被动接口（P21/C7）
5. **非广播网络**：NBMA 需全互联+静态邻居（P16/C8），eligible 决定是否参与 DR 选举
6. **冗余 CMM**：`ip ospf restart-support planned-unplanned` 让 helper 在接管期间维持 LSA 与邻接（P17/P18/C9）

## A2（操作步骤）
- **OSPF 九步上线**：`vlan 5` / `ip interface vlan-5 ...` / `vlan 5 members port 1/2/1` / `ip router router-id 1.1.1.1` / `ip load ospf` + `ip ospf admin-state enable` / `ip ospf area 0.0.0.0` / `ip ospf interface vlan-5` / `ip ospf interface vlan-5 area 0.0.0.0` / `... admin-state enable` → `show ip ospf [area|interface]`（C1，<<<PAGE 21>>>）
- **OSPFv3 九步**：`ipv6 interface test vlan 1` → `ipv6 address 2001::/64 eui-64 test` → router-id → `ipv6 load ospf` + enable → area → 接口挂区 enable（C10，<<<PAGE 57>>>）
- **Totally Stubby**：ABR 上 `ip ospf area 1.1.1.1 type stub` + `summary disable` + `default-metric 0`；区内路由器配 `type stub`（C3，<<<PAGE 35-36>>>）
- **虚链路**：Router A `ip ospf virtual-link 0.0.0.1 2.2.2.2`；Router B 互指；`show ip ospf virtual-link`（C4，<<<PAGE 39>>>）
- **认证**：simple：`auth-type simple` + `auth-key test`；MD5：`auth-type md5` + `md5 7` + `md5 7 key "test"`；keychain：`security key ... algorithm sha256` + `security key-chain 1 key 125` + `auth-type key-chain 1`（C5，<<<PAGE 37-38>>>）
- **NBMA 邻居**：`ip ospf interface vlan-213 type non-broadcast` → `ip ospf neighbor 1.1.1.8 eligible`（C8，<<<PAGE 47>>>）
- **GR**：`ip ospf restart-support planned-unplanned`（可选 restart-interval / helper / strict-lsa-checking）（C9，<<<PAGE 48>>>）
- **OSPFv3 特有**：NSSA translator 三件套 `nssa-translator role always|candidate` / `stab-interval 60` / `nssa-summarize c000::/64`（C12）；Loopback0 通告须 `type point-to-point`（P40/C13）；静态邻居用链路本地地址 fe80::（P41）

## E（实证案例）
- OSPF 三区域三路由器应用例（C2，<<<PAGE 49-53>>>）
- Totally Stubby 两路由器配置（C3，<<<PAGE 35-36>>>）
- 虚链路创建与验证（C4，<<<PAGE 39>>>）
- 认证三套（simple/MD5/keychain-SHA256）（C5，<<<PAGE 37-38>>>）
- OSPFv3 三区域应用例（C11，<<<PAGE 84-88>>>）与 NSSA 参数（C12，<<<PAGE 72>>>）

## B（反例/坑）
- Stub 区域禁虚链路、禁内部 ASBR（X1，<<<PAGE 27, 64>>>）；NSSA 同样禁虚链路且区域类型必须全网一致否则邻接建不起来（X2，<<<PAGE 28, 65>>>）
- 虚链路是最后手段，最大努力避免（X3，<<<PAGE 26, 39>>>）
- 单路由器不建议带超过三个区域（X4，<<<PAGE 33, 70>>>）
- ECMP 只看度量不看线速，可能选中慢链路（X5，<<<PAGE 29>>>）
- 接口名不能含空格（X6，<<<PAGE 21>>>）
- MD5 key ID 与 key string 必须两条命令分别设置（X7，<<<PAGE 37>>>）
- 被动接口上已有邻接会立即拆除（X8）；多区域域中被动接口只生成在 Area ID 最小的区域（X9）（<<<PAGE 46>>>）
- 从内存移除 OSPF/OSPFv3 必须手改 boot.cfg 并重启（X10，<<<PAGE 33, 70>>>）
- 接口参数可一次配多个但只能逐个恢复默认（X11，<<<PAGE 39>>>）
- NBMA 邻居 eligibility 必须与其他路由器接口优先级一致（X13，<<<PAGE 29>>>）
- 配置重分发即自动成为 ASBR（P22）；iBGP→OSPF 重分发默认禁止，需 `ip ospf redist-bgp-internal`（P23，<<<PAGE 48>>>）

## 来源
OmniSwitch AOS 8.10R4 Advanced Routing Guide 第 1 章 OSPF（<<<PAGE 20-53>>>）、第 2 章 OSPFv3（<<<PAGE 55-88>>>）。条目来源：cases C1-C13；principles P1-P25/P34-P41；counter-examples X1-X13；frameworks F1/F2/F3/F6/F10。
