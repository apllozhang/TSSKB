# DIGEST · OmniSwitch VxLAN/EVPN 实施精华（不读全书版）

> 原书：ALE Training Services《VxLAN/EVPN》（DT00XTE325EN），213 页，AOS 售后 Experienced 路径 1 天实操课。本文只保留"拿去就能用"的部分，数字均带原书页码。

## 一、一页看懂 VxLAN/EVPN 实施

AOS 教 VxLAN/EVPN 有一套独有的**五步配置法**（p59，同一张步骤图在 p59/p62/p66/p68 逐段展开，贯穿 p59-149）：

1. **Underlay**——L3 路由底座（OSPF/eBGP，Loopback0 互通）
2. **Overlay**——MP-BGP EVPN 会话（全网同 AS、iBGP、可选 RR）
3. **Service Access**——接入口/聚合口启用以太网段（ESI）
4. **Service**——EVPN-VXLAN 业务实例化（VNI 虚拟桥）
5. **SAP**——业务接入点绑定 VLAN

为什么值得迁？传统 DC 四痛点（p164/167）：STP 冗余链路被阻塞浪费资源、12 位 VLAN 上限 4096、运维复杂、静态首跳网关导致流量绕行（traffic tromboning）。VXLAN 用 MAC-in-UDP + 24 位 VNI（16M 网络）解决数据面；裸 VXLAN 仍靠 flood-and-learn，MP-BGP EVPN 补上主动式控制面。

AOS 实现模型四件套（p184-185）：全端口 ESI 实例化、ESI+ETag 粒度路由、RD/RT 自动生成、on-demand 按需导入（BGP RIB 全网分发，只有被查找的目的才进硬件 FDB）。

## 二、五步主线（配 CLI 要点）

**第一步：Underlay（p60/p80/p186）**
一切从 Loopback0 开始——VTEP 身份、OSPF router-id、BGP router-id、update-source 四合一。推荐组合 **OSPF underlay + iBGP overlay**（p186）。OSPF 收敛参数包六条：单区域、互联口 point-to-point（免 DR 等待）、BFD 200ms（`ip bfd transmit 200 / receive 200 / echo-interval 200`）、`spf-timer delay 0 / hold 0`、ECMP、MTU 预留 50 字节 VXLAN 头。若用 BGP underlay 必须 eBGP：Spine 共享一个 AS、每台 Leaf 唯一 AS（p60）。

**第二步：Overlay（p84）**
四条命令起 EVPN：`ip load bgp` → `ip bgp autonomous-system 65000`（全网同 AS）→ `ip bgp address-family evpn` → 对每个对端 Loopback 配 `neighbor <ip> remote-as 65000 update-source Loopback0 activate-evpn admin-state enable`。`activate-evpn` 是逐邻居开关，漏一条该邻居就不交换 EVPN 路由。规模化上 RR（p132/136）：N 台 Leaf 全互联要 N(N-1)/2 条会话（10 台=45 条），惯例 Spine 兼任 RR，配 `cluster-id` + `route-reflector-client`，冗余用单集群双 RR。

**第三、四、五步：业务三部曲（p67/p69/p71）**
```
service access port 1/1/7 evpn-ethernet-segment enable
service 100 vxlan vnid 1000 bgp-evpn enable
service 100 sap port 1/1/7:10
```
对端 Leaf 重复同样三条。映射惯例：service 100 ↔ EVI/VNI 1000 ↔ ETag 10。三层叠加（非对称 IRB + DAG，p99/p105/p109）：每业务挂 `ip interface` 地址 + `ip anycast-gateway-mac auto`（自动生成 00:00:5E:00:01:XX）+ `anycast-gateway-address 192.168.x.254`。非对称 IRB 硬前提：每个 EVI 在**所有**交换机（含 Spine）实例化——Spine 用 dummy 口占位，这是最常见翻车点（p105）。

**多归属**（在三部曲上加 LAG/ESI，p141-158）：动态 LACP 口 `service access linkagg 3 evpn-ethernet-segment enable` 自动生成 ESI（`03:<CE-MAC>:ff:<Key-Id>`）；静态 LAG 例外，必须手工补 `esi <10字节>`，两端一致全网唯一（p156）。DF 选举默认 service carving：**DF = EVI mod N**（N=候选 PE 数），默认抢占式（p182-183）。

**BUM**：EVPN 下用 RT3 IMET 自动发现远端 VTEP 建头端复制（HER）列表（p41）；8.10R1 仅支持 HER（p180）。Proxy ARP 默认启用（p110/124），PE 收 ARP 先查本地缓存，命中代答、未命中才泛洪。

## 三、参数速查表

| 项目 | 值 | 页码 |
|---|---|---|
| VXLAN UDP 端口 | 4789 | 架构章 |
| VXLAN 头开销 | 50 字节（underlay MTU 必须预留） | p186 |
| 业务默认 MTU / VPN IP-MTU | 9194 / 1500 | p67 |
| VNI 长度 | 24 bit，约 16M 网络 | p167 |
| RD 公式 | SystemIP:EVI（基于 Loopback0） | p148 |
| RT 公式 | target:AS:EVI | p148 |
| ES-Import RT | 从 ESI 自动编码，加在 RT4 | p148 |
| ESI 编码 | 物理口 `03:端口MAC:ff:ff:ff`；LACP 口 `03:CE-MAC:ff:Key-Id` | p142/p184 |
| DF 算法 | EVI mod N，默认抢占 | p182-183 |
| Anycast 虚拟 MAC | 00:00:5E:00:01:XX（XX=VRF 级虚拟路由器 ID） | p99 |
| BFD 默认包 | transmit/receive/echo 均 200ms | p80 |

**RT 类型总表**（p148 章节与架构指南）：RT1 以太网 AD（aliasing/备份路径/水平分割/批量撤销；RT1A per-ES ETag=0xFFFFFFFF，RT1B per-EVI）；RT2 MAC/IP（主机可达+ARP 抑制）；RT3 IMET（VTEP 发现+BUM 复制）；RT4 ES（同 ES 发现+DF 选举）；RT5 IP 前缀（RFC 9136）；RT6-8 SMET/IGMP-MLD（RFC 9251）。基础通告主要用 RT1-RT4。

## 四、Lab 实施精要

- **Lab1 四节点底座**（p78-86）：Spine Loopback 1.1.1.10/11、Leaf 1.1.1.1/2；互联 VLAN 101/102/110/111/112 子网 172.16.1xy.0/24；验证链 `sh ip ospf neighbor` 全 Full → `sh ip routes` 双等价路径 → `show ip bgp neighbors` established + evpn advertised。
- **Lab2 双业务+三层**（p102-117）：service 100/200（VNI 1000/2000）共用口 1/1/7，SAP `1/1/7:10` 与 `1/1/7:20`；三层每 Leaf 挂 ip interface（Leaf1=.1、Leaf2=.2）+ anycast .254。验证五连：`show service evpn` → `ethernet-segment` → `debug evpn show bgp route-type rt3`（4 条 IMET）→ `<esi> sap-info` → `evi 1000 tunnel-ports`（动态 SDP 32768 建到远端 1.1.1.2）。注意 p113 教材笔误：client 9/10 网关原文误写 192.168.30.254，应为 192.168.20.254，照抄必不通。
- **Lab3 跨设备多归属**（p153-158）：两 Leaf 各建 `linkagg lacp agg 3 size 2` + `actor admin-key 3`，CE 侧同 agg 挂两口，自动 ESI 03:2c:fa:a2:a2:f2:ad:00:03:00；切换演练断 Leaf1 成员口，ES 角色翻转、ping 不中断、MAC 迁到对端 sap。静态 LAG 用 `linkagg static agg 7` + 手工 ESI。验证三视图：本地单归属 `sap-info`（* = DF）、本地多归属 `carving-info`、远端 `aliasing-info`（p200-201）。

## 五、学习路径（5 个 skill 顺序）

1. `vxlan-evpn-five-step-architecture`——总路线、迁移论证、版本边界（先建立框架）
2. `vxlan-evpn-underlay-bgp-design`——底座与 BGP/RR（先让 Loopback 可达、会话建立）
3. `vxlan-evpn-service-provisioning`——L2/L3 业务、IRB/DAG、RD/RT（再开业务）
4. `vxlan-evpn-multihoming-df`——双归/ESI/DF（业务可靠接入）
5. `vxlan-evpn-bum-troubleshooting`——BUM/ARP 抑制/排障分层（最后学转发面行为与排障）

排障统一分层（课堂验证链，p64-74）：ES → service → SAP → RT3 → MAC → SDP 隧道 → Proxy ARP → 端到端 ping，逐层核对。

## 六、版本边界与陷阱（8.10R1）

EVPN 首版 **8.10R1、仅 OS6900**，四项不支持（p173/p179/p180/p182 逐条命中）：**RT5、对称 IRB、tandem 组播复制、all-active 多归属**。客户需求命中任一项就改方案或核对目标版本 release notes（培训环境为 8.10R2，能力随 release 滚动放开）。

高频陷阱清单：

- **Spine 漏配业务**：非对称 IRB 要求全 PE 全业务实例化，Spine 忘配 dummy 口则 IRB 路由上下文不完整。
- **`activate-evpn` 漏一条**：该邻居只建普通 BGP 会话，不交换 EVPN 路由。
- **MTU 隐性丢包**：不预留 50 字节会出现大帧静默丢、小包正常。
- **on-demand 模型**：`sh mac-learning evpn-vxlan` 表项少于 BGP RT2 路由数是正常现象（p184/p117），拿 `debug evpn show bgp route-type rt2` 对比，别拿硬件 FDB 数当路由健康指标。
- **Proxy ARP 空表 ≠ 故障**：表项会老化（p203），先两端互 ping 造流量再回查。
- **静态 LAG 漏配 esi**：ES 无法标识，多归属整个不成立；手工 ESI 两端不一致 = 两个 ES，DF/aliasing 全失效且难查。
- **远端 ES 命令报错**：sap-info/carving-info 仅限本地 ES，远端用 aliasing-info（p200-201）。
- **MAC 震荡防护**：`mac-mobility loop-protection` 须配在所有 Leaf，漏一台该 Leaf 仍会被打爆；根因（ES 网环路或主机重 MAC）要另查。

---

*由 cangjie-skill 流水线从 DT00XTE325EN 蒸馏生成*
