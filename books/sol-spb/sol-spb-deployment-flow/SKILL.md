---
name: SPB 部署指南落地流程（11 步/VRF+VRRP+PBR/S-Hook/自动化）
description: 需要按 ALE 官方部署指南在中型园区落地 SPB（VLAN→LBD→BVLAN→服务→SAP→VRF→VRRP→PBR→OSPF→策略 11 步）、配置 VRRP tracking、处理 AP/untagged 接入、做 VLAN 域与 SPB 域 S-Hook 挂接、或利用 iFab 自动化（Auto-VC/RCD/LACP/SPB/动态服务）时使用。
source_book: SPB Deployment Guide Ed.2025（sol-spb DOC2）+ Tech Brief 自动化章节
---

## R（触发场景）
- 中型园区从零部署 SPB，需要参考架构与步骤清单
- 规划 VRF 分段、VRRP 网关冗余、PBR 集中策略与 OSPF 上联
- 混合场景：VLAN 域老设备与 SPB 域对接（S-Hook）
- 利用出厂 Auto-Fabric/动态服务做近零接触开局

## I（核心理念）
中型园区参考架构（F6，<<<PAGE 63>>>）：2×BCB 全网格 + N×BEB 双归 LAG + PBR 策略路由器；VRF 按部门分段、VRRP 虚网关 .1（末位=BEB 号）、/30 点对点连 PBR、OSPF 按 VRF 分 area、PBR 集中策略，可平滑加 BCB 扩展。VRRP tracking 联动上行链路：上行断则优先级 120−25=95，对端接管（P59，<<<PAGE 78>>>）。自动化分层（F5，<<<PAGE 36>>>）：Auto-Fabric 六阶段打底 → UNP+认证动态 SAP → 动态服务按 VLAN 标签即时生成（ISID=BSN+Domain ID+VLAN%Modulo 公式，P36，<<<PAGE 42>>>）。

## A1（行动框架）
1. 部署 11 步总清单（C24，<<<PAGE 62>>>）：物理拓扑/LAG → VLANs → LBD → 控制与业务 BVLAN → SPB 服务 → BEB 上 SAP → VRF 分段 → VRRP → VRF-PBR 点对点 → VRRP Tracking → OSPF → 网络策略
2. 命名规范先行（P55，<<<PAGE 64>>>）：ACC-31（BEB3 第 1 台接入）、linkagg 13（BCB-1↔BEB-3）；BEB-1/2 名号让给 BCB，避免认知混淆（X30，<<<PAGE 64>>>）
3. VRF 间隔离由 PBR 强制，VRF 内再叠 DHCP snooping/DAI（P60，<<<PAGE 80>>>）
4. 自动化开局：近零接触（P32，<<<PAGE 36>>>）→ 动态服务避免预置全 4096 VLAN（P35，<<<PAGE 42>>>）

## A2（操作步骤）
- **落地命令链**（C25，<<<PAGE 67>>>）：`vlan 1000` → `loopback-detection enable` + `loopback-detection service-access linkagg 31 enable` → `spb bvlan 4000-4002 admin-state enable` → 配控制 BVLAN 前先 `spb isis admin-state disable` → `spb isis interface linkagg 16` → `service 1000 spb isid 1000 bvlan 4001 vlan-xlation enable` → `service access linkagg 31 vlan-xlation enable` → `service 1000 sap linkagg 31:1000` → ping + `show spb isis spf bvlan 4001` 验路径
- **VRF+VRRP+OSPF+策略全套**（C27，<<<PAGE 74>>>）：`vrf create corp` 等五 VRF → VRF 内 IP 接口挂 service → VRRP 三命令建 .1 虚网关 → PBR 侧 /30 互联（接口名 corp3-pbr 格式，P58，<<<PAGE 77>>>）→ `ip vrrp track 1 … priority 25` + track-association → 各 VRF 独立 area、本地网段聚合经 route-map 重分发 → PBR 上 policy 拒 Guest 访问其它 VRF
- **AP 直挂 BEB**（C26，<<<PAGE 73>>>）：管理服务 `service 2000 sap port 1/1/31:0` 映射 untagged；SSID 流量另建 tagged SAP（`service 1016 sap port 1/1/31:1016`）
- **S-Hook 对接**（C28，<<<PAGE 81>>>）：VLAN 域 LAG-125 打 tagged VLAN，服务域 LAG-127 建 `service N sap linkagg 127:N`，实现两域 S 形挂钩
- **Auto-Fabric 序列**（C12-C16，<<<PAGE 36-38>>>）：Auto-VC（LLDP 选举 Master 生成 vcsetup.cfg）→ Auto-RCD（DHCP→TFTP/OmniVista 取配置固件）→ Auto-LACP（探测 LACP PDU 自动配聚合，兼容第三方）→ Auto-SPB（默认建 BVLAN 4000-4003 映射 ECT 1-4）→ Auto-IP（侦听 OSPF/IS-IS Hello 自动配平邻接）
- **动态 SAP/服务**（C17-C20，<<<PAGE 38-43>>>）：六个 UNP 绑 ISID + SAMPLE_FLOW 模板走 802.1x→filter-id、MAC 兜底、无匹配落 RESTRICTED；静默设备静态绑 UNP（P34，<<<PAGE 39>>>）；VLAN 101 默认参数演算 ISID=10,000,101→BVLAN 4001

## E（实证案例）
- 部署指南全流程命令落地与路径验证（C25，<<<PAGE 67>>>）
- 五 VRF+VRRP+PBR 策略全套配置（C27，<<<PAGE 74>>>）
- 两代 ASIC 混合场景 S-Hook 替代配置（C28，<<<PAGE 81>>>）
- 多租户 Domain ID：客户 A/B/C 建 Domain 1/2/3，VLAN 标签重叠仍隔离（C20，<<<PAGE 43>>>）

## B（反例与坑）
- 预置全部 4096 VLAN 服务是坏实践，控制面无谓负载（X16，<<<PAGE 42>>>）
- 默认 Service Modulo 512 可致 8 个 VLAN 混桥同一 L2 域，隔离需求调 4096（X17，<<<PAGE 43>>>）
- 静默设备（节能模式）丢服务绑定致 WAKE-ON-LAN 不可达——静态绑 UNP（X18，<<<PAGE 39>>>）
- 多 VLAN 映射同一服务破坏隔离并引发 mac-move（虚拟化重复 MAC 场景尤甚）——VLAN 与服务一对一（P26/X21/X22，<<<PAGE 52>>>）
- 单链路也建 linkagg、引用逻辑名，扩成员口不改其它配置（P33，<<<PAGE 37>>>）

来源：SPB Deployment Guide Ed.2025（sol-spb DOC2，p57-82）+ Tech Brief 自动化章节（p36-43）
