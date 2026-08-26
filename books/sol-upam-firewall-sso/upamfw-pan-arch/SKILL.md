---
name: PAN 集成架构与前提（User-ID/Syslog 解析机制/字段含义/超时与登出局限）
description: 需要理解 OmniVista UPAM 与 Palo Alto Networks 防火墙 User-ID 集成的架构与机制约束时使用：UPAM 外部 syslog 推送（UDP 514）、syslog 字段解析（deviceIP/username/filterID/changeType）、只解析 Accounting 消息导致登出不及时的局限、interim interval 须小于 45 分钟 User Identification Timeout。
source_book: OmniVista UPAM and Palo Alto Networks User-ID Integration Guide
---

## R（触发场景）
- 动手配置 PAN 集成前先理解机制：为什么走 syslog 而不是 RADIUS
- 解读 UPAM 发出的 syslog 报文，确认字段取值
- 排查"用户下线了防火墙还留着映射""策略引用角色不生效"这类机制性限制
- 规划 interim interval 与 User-ID 超时的参数关系

## I（核心理念）
PAN 侧机制：终端对 UPAM RADIUS 做 MAC/802.1x 认证，UPAM 把认证与记账事件以 syslog（UDP 514）发给 PAN 内置 syslog 接收器，防火墙上配 parse filter 从中提取角色（filterID）或用户名，形成 IP-用户/角色映射，供 User-ID 策略使用（<<<PAGE 4>>>）。关键约束有三条：① 设备 IP 只在 Accounting/Disconnect 消息里有（Access 消息通常没有，因为 DHCP 要等认证后才完成），所以必须开 interim accounting；② 每个 syslog 源只能挂一个 parse profile，笔记选了信息最全的 Accounting 过滤器，因此无法过滤 Disconnect——用户断线后不会立刻从防火墙登出，要等 User Identification Timeout（默认 45 分钟）内收不到 accounting 更新才登出；③ 故 interim interval 必须小于该超时（默认 600 秒满足）（<<<PAGE 5>>>）。

## A1（行动框架）
1. 画数据流：终端 →(802.1x/MAC)→ UPAM RADIUS（可代理外部 RADIUS）；UPAM →(Syslog Accounting, UDP 514)→ PAN 防火墙（区别于 Fortinet 方案：由 UPAM 发，且走 syslog 协议）（<<<PAGE 4>>>）
2. 决定解析目标：映射 username（防火墙本地库要建用户/组，MAC 认证时用户名=MAC，难维护）或映射 filterID 即角色（策略直接引用角色，无需建用户，但日志里只有角色没有真实用户名——可另发一份 syslog 到第三方服务器做取证关联，需时间同步）（<<<PAGE 12>>>）
3. 参数约束核对：interim interval（AAA profile 或 RADIUS 服务器侧设置）< User Identification Timeout（默认 45 分钟）（<<<PAGE 5>>>/<<<PAGE 7>>>）

## A2（细节速查）
| 要点 | 说明/默认值 | 来源 | 页码 |
|---|---|---|---|
| 推送协议 | Syslog，UDP 514，PAN 内置接收器 | PAN | p4/p9 |
| 发送方 | UPAM（区别于 Fortinet 方案的网络设备直发） | PAN | p4 |
| APMAC 字段 | RADIUS NAS（交换机/AP）的 MAC | PAN | p5 |
| authType | 认证机制：MAC 或 802.1x | PAN | p5 |
| changeType | Access（认证成功）/ Accounting（周期记账）/ Disconnect（下线） | PAN | p5 |
| deviceIP | 终端 IP；通常只在 Accounting/Disconnect 消息中 | PAN | p5 |
| filterID | uNP/ARP，即设备被分配的角色 | PAN | p5 |
| username | MAC 认证时即设备 MAC 地址 | PAN | p5 |
| parse profile 限制 | 每个 syslog 源只能一个解析配置 → 只配 Accounting 过滤器 | PAN | p5 |
| 登出机制 | 无 Disconnect 过滤 → 靠 User Identification Timeout 过期登出，默认 45 分钟 | PAN | p5 |
| interim interval | 默认 600s，须 < 45 分钟超时 | PAN | p5/p7 |
| 大小写 | 含大写的用户名在防火墙侧会转成小写 | PAN | p14 |
| 任务清单 | OV 侧 4 步；PAN 侧 7 步 | PAN | p6 |

## E（场景案例）
- IoT 摄像头/传感器 syslog 集成参考拓扑（Figure 2）：UPAM 向防火墙发 Syslog Accounting，防火墙得到 "192.168.10.1: IoT_Camera" 映射（<<<PAGE 4>>>）
- 角色映射替代用户名映射：filterId=sensor 直接进策略，防火墙本地库零用户（<<<PAGE 12>>>）
- 取证补救：UPAM 同时向另一台 syslog 服务器发日志，按时间关联还原"角色背后的真实用户名"（<<<PAGE 12>>>）

## B（限制与坑）
- 登出不及时是机制性局限：用户断线后映射最多保留 45 分钟（默认），期间策略仍按在线用户对待（<<<PAGE 5>>>）
- interim interval ≥ User-ID 超时的话，活跃用户也会被误登出——务必保持前者小于后者（<<<PAGE 5>>>）
- Access 消息里通常没有 IP：只靠认证日志做不了映射，必须开 interim accounting（<<<PAGE 5>>>）
- 角色映射方案下防火墙日志只见角色不见用户名，取证要靠外部 syslog + 时间同步（<<<PAGE 12>>>）
- 用户名大写会被转小写，策略里要用小写引用（<<<PAGE 14>>>）

## 来源
来源：OmniVista UPAM and Palo Alto Networks User-ID Integration Guide（§5-7 Use case/Mechanism/Procedure overview，p3-6；§14 角色映射讨论，p12）
