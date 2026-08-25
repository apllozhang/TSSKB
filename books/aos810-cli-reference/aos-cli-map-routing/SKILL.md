---
name: AOS 8 CLI 命令地图——路由域（IP/IPv6/IPsec/RIP/BFD/DHCP/VRRP/OSPF/IS-IS/BGP，第 21-32 章）
description: 需要在 OmniSwitch AOS 8 上配置 IP/IPv6 接口与路由、RIP/OSPF/OSPFv3/IS-IS/BGP、BFD、VRRP、DHCP Relay、IPsec、SLB 时，用本地图定位 CLI Reference 对应章节与代表命令。
source_book: OmniSwitch AOS Release 810R04 CLI Reference User Guide
---

## R（触发场景）
- 查路由类命令语法/默认值/平台矩阵（ip ospf、ip bgp、ipv6 等）
- 路由协议命令敲了不生效——忘了 `ip load <protocol>` 先加载模块
- OSPF 定时器、BGP ECMP 等关键默认值核对
- DHCP Relay / IPsec / VRRP / BFD / SLB 章节定位

## I（核心理念）
本域是全书体量最大的命令域（<<<PAGE 1549-3227>>>），两条通用规律：其一，路由协议命令生效前需 `ip load <protocol>` 加载对应模块（X8，RIP/OSPF/IS-IS/BGP/VRRP）；其二，部分全局参数类命令要求先停协议再改。BGP 章 194 条为全书第二大章，命令分 Global/Aggregate/Network/Neighbor/Address-family/VRF 组（P20）；OSPF 章按 Global/Area/Interface/BFD/VRF 分组（P17）。

## A1（决策框架）
1. **单播底座**（接口/静态路由/ARP/DNS/UDP 中继）→ 第 21 章 IP（113 条）
2. **IPv6**→ 第 22 章；**IPsec**→ 第 23 章
3. **IGP/网关/检测**：RIP→24；BFD→25；VRRP→27；OSPF→28；OSPFv3→29；IS-IS→30
4. **EGP 与负载均衡**：BGP→31；SLB→32
5. **DHCP 中继/option82**→ 第 26 章（116 条）
6. 记住先 `ip load <protocol>`，再配协议命令

## A2（操作步骤）·章节清单与代表命令
- **Ch21 IP（<<<PAGE 1549>>>，约 113 条）**：`ip interface`、`ip route`、`ip domain`、ARP、`ip helper` 等单播底座（P16）
- **Ch22 IPv6（<<<PAGE 1793>>>，约 68 条）**：`ipv6` 地址/邻居发现/路由与过渡
- **Ch23 IPsec（<<<PAGE 1948>>>，约 11 条）**：`ipsec`/IKE 隧道加密
- **Ch24 RIP（<<<PAGE 1974>>>，约 41 条）**：`ip rip` 距离矢量
- **Ch25 BFD（<<<PAGE 2058>>>，约 16 条）**：`ip bfd`（为路由协议提供毫秒级故障检测）
- **Ch26 DHCP Relay（<<<PAGE 2092>>>，约 116 条）**：`bootp relay`/DHCP 中继、option82、监督
- **Ch27 VRRP（<<<PAGE 2334>>>，约 24 条）**：`ip vrrp`（首跳网关备份）
- **Ch28 OSPF（<<<PAGE 2392>>>，约 57 条）**：`ip ospf spf-timer [delay seconds] [hold seconds]`（0-65535，默认 delay=5/hold=10；任一为 0 则立即触发 SPF）（P18）；`ip ospf interface hello-interval`（0-65535 秒，默认 broadcast/P2P=10、NBMA/P2MP=30）（P19）；`ip load ospf` 前置（X8）
- **Ch29 OSPFv3（<<<PAGE 2513>>>，约 46 条）**
- **Ch30 IS-IS（<<<PAGE 2610>>>，约 62 条）**：SPB 控制面基础
- **Ch31 BGP（<<<PAGE 2744>>>，约 194 条）**：`ip bgp maximum-paths`（ECMP 开关，默认 disabled；启用后忽略 router-id 判等装全部等价路径；要求先停 BGP）（P22）；`ip bgp default local-preference`；BGP-4+MP-BGP（IPv6 前缀与邻居），peer 与 neighbor 术语互换（P20）
- **Ch32 SLB（<<<PAGE 3160>>>，约 31 条）**：`slb`（VIP/实服务组/健康检查）

## E（实证案例）
- 命令地图型 skill，不搬运案例；原书每条命令自带 Example，按章首页码回查（cases 原件未创建）

## B（反例/坑）
- 路由协议命令生效前需 `ip load <protocol>` 加载模块（X8，第 24/27/28/30/31 章）
- `ip ospf spf-timer`/`hello-interval` 平台：6360/6465 不支持，6560 起支持（X2，<<<PAGE 2409>>>/<<<PAGE 2434>>>）
- `ip ospf interface hello-interval` 设 0 的语义是创建被动接口（不发 hello），并非更快收敛（X23，<<<PAGE 2434>>>）
- `ip bgp default local-preference`/`maximum-paths` 平台：6360/6465/6575 不支持（X3，<<<PAGE 2759>>>/<<<PAGE 2776>>>）
- `ip bgp maximum-paths` 同样要求先停 BGP 再配（P22）

## 来源
OmniSwitch AOS Release 810R04 CLI Reference User Guide 第 21-32 章（<<<PAGE 1549-3227>>>）。条目来源：principles P16-P22；counter-examples X2/X3/X8/X23；frameworks F6。
