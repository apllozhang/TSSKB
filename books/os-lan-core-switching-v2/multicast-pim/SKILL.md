---
name: 组播（IPMS/IGMP/PIM/Anycast RP）
description: 需要部署二层组播优化（IPMS/IGMP 侦听）或三层组播路由（PIM-SM/BSR/Anycast RP）时使用本技能。
source_book: DT00XTE216 OmniSwitch LAN Core Switching Ed15
---

## R（触发场景）
- 视频/IPTV 流量在 VLAN 内泛洪，需要 IGMP 侦听按端口转发
- 跨 VLAN/跨网段组播，要选 DVMRP、PIM-SM 还是 PIM-DM，要设计 RP
- RP 单点故障风险大，需要 RP 冗余与负载分担（Anycast RP）

## I（核心理念）
组播分两层解：同 VLAN 内由 IPMS（硬件 IGMP 侦听）解决"只发给加入的端口"；跨网段才需要组播路由协议做 RPF 校验和树构建。PIM-SM 用显式加入 + RP 共享树（RPT），末跳 DR 收到首包后自动发起 SPT 切换获得最优路径；RP 是可用性与性能的关键点，BSR 做动态发现，Anycast RP（RFC 4610）用共享 Loopback 任播地址做到 IGP 级快速切换。

## A1（行动框架）
1. 二层 IPMS：`ip multicast admin-state enable`（全网）+ 服务器侧 `ip multicast querying enable` + 其余 `ip multicast querier-forwarding enable`；验证 `show ip multicast group/forward` 精确到组地址的端口表项（<<<PAGE 405>>>-<<<PAGE 409>>>）
2. PIM-SM：`ip load pim` + `ip pim sparse admin-state enable`（全网）→ `ip pim interface int_217 ...` → `ip pim cbsr 192.168.110.1` → `ip pim candidate-rp 192.168.110.1 231.1.1.0/24`（分组 RP）；验证 `show ip pim neighbor / group-map / sgroute`（<<<PAGE 447>>>-<<<PAGE 449>>>）
3. Anycast RP：RP1/RP2 均配 `ip interface "Loopback1" address 10.10.10.1`；全网所有 PIM 路由器（含非 RP）`ip pim static-rp 231.0.0.0/8 10.10.10.1`；各 RP 上 `ip pim anycast-rp 10.10.10.1 <自身 Loopback0>` + 指向对端（<<<PAGE 648>>>-<<<PAGE 649>>>）
4. DVMRP（小规模备选）：`ip load dvmrp` → `ip dvmrp interface <name>` → `ip dvmrp admin-state enable` → `write memory`（<<<PAGE 419>>>）

## A2（进阶应用）
- IGMP Throttling：per-port 限制覆盖 VLAN 与全局，动作 none/drop/replace（<<<PAGE 396>>>）
- IGMP 版本：v1 基础查询/报告；v2 加 Leave、特定组查询（Fast Leave）；v3 加源过滤（Explicit Host Tracking）；TTL=1 本地段协议，查询发 224.0.0.1、Leave 发 224.0.0.2（<<<PAGE 381>>>-<<<PAGE 382>>>）
- BSR 选 RP 算法：优先级（最小）→ hash（组地址+RP 地址）→ 最高 IP（<<<PAGE 431>>>-<<<PAGE 432>>>）
- PIM-DM：泛洪-剪枝 3 分钟循环、无 RP，适合接收者密集网络（<<<PAGE 434>>>-<<<PAGE 435>>>）
- DVMRP：RPF 校验 + flood/prune/graft，prune 超时 7200s（<<<PAGE 413>>>、<<<PAGE 416>>>-<<<PAGE 417>>>）
- Anycast RP 边界：仅 PIM-SM、最多 8 台、须启用 SPT（<<<PAGE 645>>>）
- 地址基础：Class D 224.0.0.0-239.255.255.255，IP 低 23 位映射 01:00:5E 组播 MAC；知名组如 224.0.0.5/6（OSPF）、224.0.0.13（PIM）、224.0.0.18（VRRP）（<<<PAGE 375>>>）

## E（实证案例）
- C-28 IPMS 开关对比：关闭时组播帧泛洪全 VLAN，开启后 `show ip multicast group/forward` 精确到 231.1.1.5 的端口级表项（<<<PAGE 405>>>-<<<PAGE 409>>>）
- C-30 PIM-SM 全网配置：BSR 域内多 RP 分组，`show ip pim group-map` 学到 6 条 RP、`sgroute` 显示 (S,G) 建立（<<<PAGE 447>>>-<<<PAGE 449>>>）
- C-31 Anycast RP：Loopback1 共享地址 + static-rp 全域下发 + anycast-rp 互指（<<<PAGE 648>>>-<<<PAGE 649>>>）

## B（边界与陷阱）
- 每接口仅能运行一个组播协议，DVMRP 与 PIM 二选一（<<<PAGE 419>>>）
- Anycast RP 的 static-rp 必须配置在全域所有 PIM 路由器（含非 RP 节点），漏配则部分节点找不到 RP（<<<PAGE 648>>>）

## 来源
- principle·P-49 组播地址映射（<<<PAGE 375>>>）
- principle·P-50 IGMP 版本演进（<<<PAGE 381>>>、<<<PAGE 382>>>）
- principle·P-51 IPMS 分工（<<<PAGE 377>>>、<<<PAGE 385>>>、<<<PAGE 386>>>）
- principle·P-52 IGMP Throttling（<<<PAGE 396>>>）
- principle·P-53 DVMRP（<<<PAGE 413>>>-<<<PAGE 417>>>）
- principle·P-54 PIM-SM RPT/SPT（<<<PAGE 426>>>-<<<PAGE 430>>>）
- principle·P-55 BSR/C-RP（<<<PAGE 431>>>、<<<PAGE 432>>>）
- principle·P-56 PIM-DM（<<<PAGE 434>>>、<<<PAGE 435>>>）
- principle·P-57 Anycast RP（<<<PAGE 643>>>-<<<PAGE 645>>>）
- case·C-28/C-29/C-30/C-31
