---
name: BGP 与 VRF 路由隔离泄漏
description: 需要部署 eBGP/iBGP 互联两个 AS，或在一台交换机上做多租户 VRF 隔离并受控泄漏路由时使用本技能。
source_book: DT00XTE216 OmniSwitch LAN Core Switching Ed15
---

## R（触发场景）
- 两个自治系统（AS）各自跑 IGP，需要在边界交换路由
- 多租户/多业务要共用一台交换机但路由表隔离、地址可重叠
- 部分租户间需要受控互访（VRF Route Leak）

## I（核心理念）
BGP 是路径矢量协议（TCP 179），靠属性而非单纯度量选路：Local Pref 选出口、AS-Path 防环、MED 引导入流量、Community 控制通告范围。VRF 在一台物理设备上切出多张路由表，隔离是默认、互通是例外——跨 VRF 流量必须经 GRT（全局路由表）以 route-map 为过滤器中转。

## A1（行动框架）
1. eBGP 基础：`ip load bgp` → `ip bgp autonomous-system 100` → `ip bgp neighbor 192.168.12.2 remote-as 200` → `admin-state enable` → `ip bgp admin-state enable`；注入本 AS 路由：`ip route-map switch1bgp sequence-number 10 action permit` + `ip redist ospf into bgp route-map switch1bgp` + `ip redist local into bgp ...`（<<<PAGE 512>>>-<<<PAGE 517>>>）
2. 邻居加固：`ip bgp neighbor 100.10.1.1 update-source Loopback0` / `ebgp-multihop`；`ip bgp neighbor <ip> md5 key` + `status enable`；`show ip bgp neighbors`（Oper state: estab）（<<<PAGE 499>>>-<<<PAGE 500>>>）
3. 策略：aspath-list/community-list/prefix-list 定义匹配 → route-map 组合 → `ip bgp neighbor <ip> route-map <name> in|out`（<<<PAGE 505>>>-<<<PAGE 508>>>）
4. VRF 创建：`vrf create ipone` → `ip interface int_190 address 192.168.190.1/24 vlan 190`（<<<PAGE 466>>>）
5. 路由泄漏：源 VRF `ip route-map "vlan190" sequence-number 50 action permit / match ip-address 192.168.190.0/24 redist-control all-subnets permit` + `ip export route-map vlan190`；目标 VRF `ip import vrf iptwo route-map vlan200`；验证 `show ip global-route-table`；default↔VRF 用 `ip import vrf default all-routes`（<<<PAGE 468>>>-<<<PAGE 470>>>）

## A2（进阶应用）
- 选路次序对照：Highest Local Pref → Shortest AS-Path → lowest Origin（IGP>EGP>Incomplete）→ Lowest MED → Closer Next-Hop → EBGP>IBGP>IGP → Lowest RID（<<<PAGE 497>>>）
- 属性作用域：Local Pref 选出口（越高越优）；MED 仅两 AS 间传递（越低越优，默认 0）；Community NO-EXPORT/NO-ADVERTISE 控制通告范围（<<<PAGE 488>>>、<<<PAGE 492>>>、<<<PAGE 496>>>）
- IBGP 水平分割：IBGP 学的路由不再传给其他 IBGP 邻居（全互联需求的根因）；同步：IBGP 路由须 IGP 可达才通告给 EBGP（<<<PAGE 501>>>、<<<PAGE 502>>>）
- VRF 归属规则：一个 VLAN/IP 接口同一时间只能属于一个 VRF，一个 VRF 可挂多个 VLAN；跨 VRF 复用同 VLAN 号不支持（<<<PAGE 460>>>）

## E（实证案例）
- C-33 eBGP 双 AS 互联：AS100/AS200 各跑 OSPF，BGP 重分发 OSPF+local 路由后对端路由表出现 EBGP 路由（<<<PAGE 512>>>-<<<PAGE 517>>>）
- C-32 双 VRF 隔离/泄漏：默认互 ping 失败 → route-map export/import 后 GRT 出现两侧条目（<<<PAGE 466>>>-<<<PAGE 470>>>）
- C-34 基于 Loopback0 建邻居 + MD5（<<<PAGE 499>>>-<<<PAGE 500>>>）

## B（边界与陷阱）
- VLAN 只能归属一个 VRF，重复 VLAN 号跨 VRF 不支持（<<<PAGE 460>>>）
- 即使路由已泄漏，交换机本机跨 VRF 接口互 ping 也不通（安全设计），连通性验证只能从客户端侧做（<<<PAGE 467>>>-<<<PAGE 468>>>）

## 来源
- framework·F-13 VRF 部署与泄漏框架（<<<PAGE 458>>>-<<<PAGE 462>>>、<<<PAGE 468>>>-<<<PAGE 470>>>）
- framework·F-14 BGP 邻居策略匹配流程（<<<PAGE 505>>>-<<<PAGE 508>>>）
- principle·P-58 VRF 隔离与 VLAN 绑定（<<<PAGE 453>>>、<<<PAGE 460>>>）
- principle·P-59 BGP 选路次序（<<<PAGE 480>>>、<<<PAGE 497>>>）
- principle·P-60 属性分类与语义（<<<PAGE 482>>>-<<<PAGE 494>>>）
- principle·P-61 IBGP 水平分割与同步（<<<PAGE 501>>>、<<<PAGE 502>>>）
- case·C-32/C-33/C-34；counter·X-22/X-23
