---
name: ip-services-basic
description: 何时用：在 OmniSwitch 上配 IP 接口/Loopback、DHCP Relay、静态路由或 VRRP 网关冗余时。
source_book: DT00XTE215EN Access Switching
---

# IP 服务基础：IP 接口 / DHCP / 静态路由 / VRRP

## R · 原文引用

"ip vrrp 1 interface int_20 / ip vrrp 1 interface int_20 address 192.168.20.254 / ip vrrp 1 interface int_20 priority 100 preempt interval 100 / ip vrrp 1 interface int_20 admin-state enable / -> ip vrrp track 3 admin-state enable priority 30 port 1/1/3 / -> ip vrrp 1 interface int_20 track-association 3"（p301-303）

"Two types of DHCP relay agents: global and per-interface... They are mutually exclusive. By default, the DHCP Relay feature is disabled. Max number of hops = 16, Forward Delay(seconds) = 0, DHCP Relay Opt82 Format = Base MAC"（p275-277）

"Multicast - 224.0.0.18 / Virtual MAC address: 00-00-5E-00-01-{VRID} / At least two virtual routers must be configured on the LAN - a master router and a backup router."（p297-302）

## I · 方法论骨架

L3 服务三件套 + 冗余：
- **IP 接口**：`ip interface <名> address <IP/掩码> vlan <N>`（可合写一条）；IP routing 只要有任一 IP 接口绑定 VLAN 即激活。
- **Loopback0**：名字固定即 /32 环回口，不绑 VLAN、有任一 active VLAN 即恒 UP，创建即被 RIP/OSPF 宣告（BGP 除外）；作 NMS/RADIUS/NTP/sFlow 稳定源地址（ip service source-ip loopback0 <应用>）。
- **静态路由**：`ip static-route 0.0.0.0/0 gateway <下一跳> metric N`；下一跳接口必须 up；静态默认优于动态；metric 定主备。
- **VRRP**：VRID+虚拟 IP 共享，priority 大者为 master（默认 100）；虚拟 MAC 00-00-5E-00-01-{VRID} 保证切换不需终端重 ARP；track 策略可联动端口故障降优先级。
- **DHCP Relay**：global 与 per-interface 两模式互斥，默认关闭，默认跳数 16、Option-82 格式 Base MAC。

## A1 · 书中案例（Lab 配置精要）

- **VRRP 主备（p305-312）**：6870/6860 各建 VRID 1（int_20，虚 IP 192.168.20.254）与 VRID 2（int_30，.30.254）。默认优先级同为 100 时比 router ID，6870 全 Master；客户端网关改 .254 后 arp -a 见 00-00-5E-00-01-01。改优先级三步：admin-state disable → priority 150 → enable，实现 6870 主 VLAN20、6860 主 VLAN30 的分担；重启 Master 演示 Backup 秒级接管（Become Master 计数 +1）。
- **DHCP Relay（p289-293）**：先 show ip routes + ping 确认两核心可达服务器 192.168.100.102；两台分别 `ip dhcp relay destination 192.168.100.102` + `ip dhcp relay admin-state enable`（全局模式）；客户端改自动获取后 show ip dhcp relay statistics 的 Reception/Tx 计数增长验证。

## A2 · 触发场景（含与相邻 skill 的区分）

- VLAN 间路由、默认路由/主备路由、网关冗余、跨网段 DHCP——本 skill。
- 只做 L2 划 VLAN/trunk/聚合 → vlan-link-redundancy。
- 两台核心机组 VC（无需 VRRP）→ virtual-chassis-deployment。
- 按流量条件改转发路径（PBR）→ qos-acl-policy。

## E · 可执行步骤

IP 接口与环回：
1. `ip interface int_20 address 192.168.20.7/24 vlan 20`。
2. 管理地址：`ip interface Loopback0 address 10.0.0.1/32`；`ip service source-ip loopback0 <应用>`。
3. `show ip interfaces` / `show ip routes`（LOCAL 网段即 VLAN 间路由）。
静态路由（主备默认路由）：
1. `ip static-route 0.0.0.0/0 gateway 1.1.1.1 metric 1`
2. `ip static-route 0.0.0.0/0 gateway 2.2.2.2 metric 2`；show ip router database 可见 inactive 备路。
VRRP：
1. `ip vrrp 1 interface int_20` → `… address <虚IP>` →（可选）`… priority 150 preempt interval 100` → `… admin-state enable`。
2. 跟踪：`ip vrrp track 3 admin-state enable priority 30 port 1/1/3` → `ip vrrp 1 interface int_20 track-association 3`。
3. 验证：`show ip vrrp [statistics]`、终端 arp -a 查虚拟 MAC。
DHCP Relay：
1. `ip dhcp relay destination <服务器IP>` → `ip dhcp relay admin-state enable`（全局）；或 per-interface 模式（两者互斥）。
2. `show ip dhcp relay statistics` 看收发计数。

## B · 边界与陷阱

- **VRRP 优先级在实例运行中改无效**：必须先 admin-state disable → 改 → enable（教材大写 Warning）。
- **VLAN 无活动成员则 IP 接口 DOWN 且不进路由宣告**——先 show vlan members 排 L2 再查路由。
- V2 同 VRID 实例须用相同 interval；preempt 默认允许，no pre-empt 可关。
- DHCP relay 全局/接口模式只能选一，混配不生效；默认关闭别忘 admin-state enable。
- 静态路由下一跳接口 down 则路由失效（database 里变 inactive）。

---
来源条目: f11, p33, p34, p35, p36, ce06, ce11, c10, c11, g25, g26, g27
