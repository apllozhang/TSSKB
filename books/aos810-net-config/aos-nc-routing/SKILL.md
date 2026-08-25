---
name: AOS 8 路由基础（RIP/VRRP/BFD/静态路由/SLB）
description: 需要在 OmniSwitch AOS 8 上配置 RIP（含 SHA256 认证）、VRRP 网关冗余与 tracking、BFD 快速故障检测联动、静态路由/默认网关、SLB 服务器负载均衡集群时使用。OSPF/IS-IS/BGP 主体在 Advanced Routing 手册，本书相关基础条目归此。
source_book: OmniSwitch AOS Release 8.10R4 Network Configuration Guide
---

## R（触发场景）
- 小型纯交换网或分支用 RIP 做动态路由
- 默认网关要冗余：VRRP 主备/抢占/跟踪上联
- 路由协议收敛太慢，要毫秒级检测故障：BFD 联动 OSPF/BGP/VRRP/静态路由
- 本地服务器池要做负载均衡：SLB 集群 + 健康探测

## I（核心理念）
静态路由/递归静态路由/默认路由/黑洞路由均由 `ip static-route` 系列配置（P110，<<<PAGE 709>>>），是其余动态路由的底座。VRRP 选举虚拟路由器 master 转发虚拟 IP 流量，master 失效由最高优先级 backup 接管（P139，<<<PAGE 979>>>）；时序公式 Master_Down_Interval=(3×Adv_Interval)+Skew_Time、Skew=(256-Priority)/256，优先级越低等待越长避免抖动（P141，<<<PAGE 980>>>）。BFD 毫秒级检测转发面故障，异步控制包与 Echo 两种模式分工：VRRP/静态路由只用 Echo，OSPF/IS-IS/BGP 用控制包；Echo 单跳、控制包可多跳（P127，<<<PAGE 870>>>）。SLB 集群以 VIP（L3）或 QoS condition（L2/L3）标识虚拟服务器，分发算法为加权轮询 WRR（P145/P147，<<<PAGE 1012>>>）。

## A1（决策框架）
1. **路由选型**：小网/分支 RIP（15 跳上限与 120 秒 hold-down 慢收敛，大网不适用，X48，<<<PAGE 842>>>）；OSPF/IS-IS/BGP 主体配置另查 Advanced Routing 手册，本书提供 VRF 内路由实例与重分发基础
2. **网关冗余选 VRRP**：IPv4 须先配接口地址才能使能（C46，<<<PAGE 978>>>）；上联故障要联动降优先级用 VRRP tracking（可达性/BFD）
3. **快速检测选 BFD**：跨网段 VRRP/静态路由只能用控制包模式，误配 Echo 会检测失效（X50，<<<PAGE 870>>>）
4. **服务器负载均衡选 SLB**：L3 模式 VIP 需服务器配 loopback；L2/L3 均可用 QoS condition cluster

## A2（操作步骤）
- **RIP**：载入→`ip rip` 全局/接口使能→定时器调优→重分发→认证（RIPv2 可 SHA256）；验证 show ip rip（cases·C40，<<<PAGE 842>>>）
- **VRRP 虚拟路由器**：`ip vrrp 23 interface ipv4-100`→`ip vrrp 23 interface ipv4-100 address 192.168.173.1`→对端同样两步→`ip vrrp 23 interface ipv4-100 admin-state enable`；验证 `show ip vrrp`/`show ipv6 vrrp`（cases·C46，<<<PAGE 978>>>）
- **VRRP tracking**：建 tracking policy（监控 IP 可达/BFD）→关联到虚拟路由器（cases·C47，<<<PAGE 993>>>）
- **BFD**：配会话参数（传输/接收间隔、检测倍数）→宿主协议（OSPF/BGP/VRRP/静态）挂 BFD；验证 show bfd（cases·C41，<<<PAGE 869>>>）
- **SLB 集群**：使能 SLB→`slb cluster <id> vip <ip> name ...`→`slb cluster <id> server <ip> weight n`→ping 周期/超时/重试→上下线 cluster/server→（可选）probe 探测关联；验证 show slb（cases·C48，<<<PAGE 1011>>>）

## E（实证案例）
- VRRP 虚拟路由器两台对配（C46，<<<PAGE 978>>>）
- SLB 集群+WRR+健康探测（C48，<<<PAGE 1011>>>）
- BFD 会话挂接宿主协议（C41，<<<PAGE 869>>>）

## B（反例/坑）
- RIP 15 跳上限：直连=1 跳，>15 跳路由删除；默认 30 秒广播更新（P122，<<<PAGE 842>>>）
- RIPv2 的不兼容特性（next hop/认证/组播更新）只在组播更新时可用，广播回退 RIPv1 兼容格式（X49/P124，<<<PAGE 843>>>）
- BFD Echo 仅单跳、控制包可多跳；Demand 模式不支持（X50/X51，<<<PAGE 870>>>）
- VRRP backup 优先级接近会产生接管时序冲突：先接管者未必最高优先级，随后被抢占产生抖动（X57，<<<PAGE 980>>>）
- 虚拟 MAC：v2=00-00-5E-00-01-VRID，v3/IPv6=00-00-5E-00-02-VRID；IPv6 用 ND 替代 ARP（P142，<<<PAGE 981>>>）
- 成为 master 时发免费 ARP；接口 IP 被虚路由共享时路由机制不再发免费 ARP（P143，<<<PAGE 981>>>）
- VRRP 支持 BFD 联动 tracking 与 UNP 动态 SPB SAP（P144，<<<PAGE 980>>>）

## 来源
OmniSwitch AOS 8.10R4 Network Configuration Guide 第 21 章 IP 静态路由（<<<PAGE 709>>>）、第 25 章 RIP（<<<PAGE 842-844>>>）、第 26 章 BFD（<<<PAGE 869-870>>>）、第 29 章 VRRP（<<<PAGE 978-993>>>）、第 30 章 SLB（<<<PAGE 1011-1015>>>）。条目来源：cases C40/C41/C46-C48；principles P110/P122-P124/P127/P139-P147；counter-examples X48-X51/X57。
