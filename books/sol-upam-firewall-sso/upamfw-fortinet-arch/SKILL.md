---
name: Fortinet FortiGate 集成架构与前提（RSSO/RADIUS Accounting 直发机制/配置前置项）
description: 需要理解 OmniVista UPAM 与 Fortinet FortiGate 单点登录集成的架构与准备工作时使用：RADIUS Accounting 直发（不经 UPAM 代理）、FortiAuthenticator 汇聚多防火墙场景、UDP 1813 放行、Accounting Interim Interval 与设备 IP 出现时机、两侧配置任务总清单。
source_book: OmniVista 2500 UPAM and Fortinet Single Sign-On Application Note
---

## R（触发场景）
- 动手配置前先理清 Fortinet 集成的数据流：accounting 消息从哪发、到哪收
- 规划多防火墙部署：直接发 FortiGate 还是经 FortiAuthenticator 汇聚
- 排查"防火墙迟迟识别不到用户 IP"——理解首包/后续 accounting 报文差异
- 清点两侧配置任务清单，估计工作量与依赖顺序

## I（核心理念）
Fortinet 侧的机制核心是一句话：AAA Server Profile 里认证指向 UPAM，记账（accounting）指向 FortiGate/FortiAuthenticator；记账报文由交换机或 AP **直接**发给防火墙，UPAM 不做代理（<<<PAGE 5>>>）。防火墙从 RADIUS Accounting 消息里提取用户名与角色（Filter-Id），策略即可按角色而非仅按 IP 下发。多防火墙部署时可把 accounting 统一发 FortiAuthenticator，免得每个 FortiGate 配一套 AAA profile。设备 IP 通常在认证后第一笔 accounting 里就有（DHCP 需时间，有的场景要等第二笔起），interim interval 调小可加快防火墙侧信息更新。

## A1（行动框架）
1. 画数据流：终端 →(802.1x/MAC/Portal 认证)→ 交换机/AP →(RADIUS 认证)→ UPAM（可再代理外部库）；交换机/AP →(RADIUS Accounting, UDP 1813)→ FortiGate 或 FortiAuthenticator（<<<PAGE 5>>>）
2. 定接收端：单防火墙 → FortiGate 本体；多防火墙 → FortiAuthenticator 统一收（<<<PAGE 5>>>）
3. 核对前提：中间防火墙放行 UDP 1813；交换机/AP 能解析所填服务器名（不行就填 IP）；默认 ARP 已建好并映射到交换机/AP 组（<<<PAGE 6>>>/<<<PAGE 8>>>）
4. 记 interim interval 决策：默认 600 秒，或交给 RADIUS 服务器侧下发（<<<PAGE 7>>>）

## A2（细节速查）
| 要点 | 说明/默认值 | 来源 | 页码 |
|---|---|---|---|
| 认证/记账分离 | AAA profile：认证指 UPAMRadiusServer，记账指 FortiGate/FortiAuthenticator | Fortinet | p5/p7 |
| Accounting 路径 | 交换机/AP 直发，不经 UPAM 代理 | Fortinet | p5 |
| 端口 | UDP 1813，中间设备需放行 | Fortinet | p6 |
| 服务器名解析 | 配名字则网络设备需能查 DNS，否则配 IP | Fortinet | p6 |
| FortiAuthenticator 价值 | 多防火墙场景统一记账入口，免多套 AAA profile | Fortinet | p5 |
| Interim Interval | 默认 600 秒；可改由 RADIUS 服务器侧设置 | Fortinet | p7 |
| 设备 IP 出现时机 | 多数在认证后首笔 accounting 即含；有时仅第二笔起才有 | Fortinet | p7 |
| 角色字段 | Filter-Id = UPAM 的 Access Role Profile（ARP）/uNP 值 | Fortinet | p13 |
| 侧任务清单 | OV 侧 4 步；FortiGate 侧 7 步 | Fortinet | p5 |

## E（场景案例）
- IoT 设备经交换机 MAC 认证后，accounting 直达 FortiGate，防火墙拿到"192.168.10.1: IoT_Camera"式映射（<<<PAGE 4>>> Figure 2）
- 多 FortiGate 企业网把 accounting 全部改发 FortiAuthenticator，AAA profile 只维护一份（<<<PAGE 5>>>）

## B（限制与坑）
- 最常见的坑：把 accounting 当成 UPAM 转发——实际是网络设备直发，抓包/排障要在交换机/AP 与防火墙之间看（<<<PAGE 5>>>）
- 填了服务器名但交换机/AP 没有 DNS → 记账发不出去，建议直接填 IP（<<<PAGE 6>>>）
- 中间路径上任何防火墙没放行 UDP 1813 → 防火墙侧静默收不到（<<<PAGE 6>>>）
- 设备 IP 只在第二笔 accounting 出现的场景，600 秒 interim 意味着最长等几分钟才有用户映射（<<<PAGE 7>>>）

## 来源
来源：OmniVista 2500 UPAM and Fortinet Single Sign-On Application Note（Mechanism/Procedure overview 及各配置章节的机制性说明，p4-7、p13）
