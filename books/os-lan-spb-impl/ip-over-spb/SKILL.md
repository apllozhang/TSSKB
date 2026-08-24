---
name: ip-over-spb
description: 何时用：在 SPB 上叠三层（VRRP 网关冗余 / VPN-Lite / L3-VPN 配置模板与选型、老硬件回环）时。
source_book: DT00XTE323EN SPB Concepts & Implementation
---

# IP over SPB 三方案（VRRP 冗余 / VPN-Lite / L3-VPN）

## R · 原文引用

> "VPN Lite: A VPN Lite L3 Service is created by overlaying a L3 routing protocol on top of the L2 WAN SPB service... L3 VPN: SPB L3 VPN leverages the existing SPB IS-IS instance to carry customer VPN routes without requiring an additional routing protocol such as OSPF. This is accomplished with additional IS-IS TLVs extensions" (p156)

> "Routes exchanged by importing and exporting between VRF and SPB-ISIS via GRT table -> spb ipvpn bind vrf default isid 4001 gateway 10.1.2.1 all-routes -> vrf default ip export route-map net1 -> vrf default ip import isid 4001 route-map net3" (p193)

> "When creating an IP interface for an SPB service: An SPB service with the specified ID must exist... VLAN translation is implicitly enabled when a service is assigned to an IP interface... Both an IPv4 and IPv6 interface can be assigned to the same SPB service as long as both interface types are in the same VRF instance." (p163)

## I · 方法论骨架

三方案按"是否另跑路由协议"递进（f07）：
1. **方案一 VRRP 冗余**：无路由协议。两台 BEB 对同一服务各建内联 IP 接口 + 交叉优先级 VRRP。
2. **方案二 VPN-Lite**：在绑服务的接口上跑 OSPF/BGP/静态，SPB 当物理媒体；适合与传统路由协议对接（g39）。
3. **方案三 L3-VPN**：IS-IS IPVPN TLV 直接携带 VRF 路由，免路由协议，简单性/扩展性/收敛全面占优（p199）。

公共最小配置（c04）：先有服务，再 `ip interface <name> address A/M service <id>` 绑接（接口地址即网关）。
L3-VPN 四步心法（f08）：bind → export → import → redist（可选泄漏），全程可用 route-map 过滤。
选型判据：需要 OSPF/BGP 对接 → VPN-Lite；纯 SPB 域内 → L3-VPN。

## A1 · 书中案例（Lab 配置序列精要）

L3-VPN 最小五步（c08，p202）：
```
spb bvlan 4001
service spb 10 isid 1000 bvlan 4001 admin-state enable
vrf 1 ip interface L3vpn1 address 10.5.1.1/24 service 10
spb ipvpn bind vrf 1 isid 1000 gateway 10.5.1.1 all-routes
vrf 1 ip export all-routes
vrf 1 ip import isid 1000 all-routes
```
VPN-Lite OSPF 块（c06/c07，p176/180）：`ip load ospf` → `ip ospf area 0.0.0.0` → `ip ospf interface L3vpn999` → 接口 enable + 入 area → `ip ospf admin-state enable`，加 route-map 重分发 `ip redist local into ospf route-map local`。
VRRP 交叉优先级（c05，p169）：Sw1 `ip vrrp 2 interface L3vpnvlan2 priority 200 / address 192.168.2.254 / admin-state enable`（vlan3 prio 100），Sw2 相反。
ECMP（c11，p219）：同一 VRF 绑两个 I-SID（各配服务+接口+bind），import 两条 I-SID 后 show ip routes 出现 "+" 双下一跳。

## A2 · 触发场景（含与相邻 skill 的区分）

- 业务要网关冗余、跨 SPB 路由互通、多 VRF 隔离、等价多路径、老平台（6900-X20 等）无内联路由能力时用本 skill。
- 与 `spb-l2-service` 的区分：本 skill 所有方案的第一步都是建 L2 服务，但一旦 `ip interface ... service X` 出现即进入本 skill；与 `spb-oam-troubleshoot` 的区分："路由学到没有"的三级表对拍（c10）本 skill 已内含，通用 OAM 归排障 skill。

## E · 可执行步骤

1. 建底层服务：`service spb <svc> isid <isid> bvlan <bvid> admin-state enable`。
2. 建内联接口：`ip interface <if> address <ip/m> service <svc>`（vrf 场景加 vrf 前缀）。
3. 按方案分支：
   - VRRP：两台 BEB 各配 `.1`/`.2` + 同 VRID 同 `.254` 虚地址，优先级交叉；`show ip vrrp` 验证 Master/Backup。
   - VPN-Lite：接口上跑 OSPF 五件套或静态路由；`show ip ospf interface` / `show ip routes` 验证。
   - L3-VPN：四步 bind→export→import→（可选）redist；验证链 `show spb ipvpn bind` → `show ip global-route-table` → `show spb ipvpn route-table` → `show ip routes`（IMPORT 标记）。
4. 从 VPN-Lite 切 L3-VPN：先 `ip ospf admin-state disable` 再 bind（避免双路由源，c09）。
5. 老平台：双口对接回环或单口 `interfaces port X loopback` + `ip interface ... rtr-port port X tagged vlan Y`（c18）。

## B · 边界与陷阱

- **内联接口三条硬规则**（p18）：service 必须先存在；绑定瞬间 vlan-xlation 隐式启用且锁定不可改（ce05）；IPv4/IPv6 同绑一个服务必须同 VRF。
- **同 I-SID 不能既 bind 又 redist 到同一 VRF**（ce06）：多部门互通的泄漏路径必须绕开已绑定组合。
- **VPN-Lite 两 VRF 不能共享同一 I-SID**（ce07/ce11 之外的 p31）：I-SID 即 L3 隔离边界；回环对 VLAN 必须专属且两侧一致。
- 老平台回环口独占（ce11）：loopback 模式下端口不能再承担其他功能，linkagg 回环只能删组解除；端口预算要扣除。
- VPN-Lite 收敛受协议叠加拖累（IS-IS 先收敛 OSPF 才能收敛，g39），对收敛敏感选 L3-VPN。

---
来源条目: f07, f08, p18, p31, p33, c04, c05, c06, c07, c08, c09, c10, c11, c18, ce05, ce06, ce07, ce11, g16, g22, g39, g40
