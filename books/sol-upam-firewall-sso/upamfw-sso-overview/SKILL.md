---
name: UPAM 防火墙 SSO 集成总览（零信任/FSSO 与 User-ID/角色推送原理）
description: 需要理解 OmniVista UPAM 为什么以及如何与第三方下一代防火墙（Fortinet、Palo Alto）做单点登录集成时使用：零信任动因、UPAM 平台能力、AD 集成与 BYOD/IoT 集成两条路线的分界、RADIUS Accounting 与 Syslog 两种身份推送机制对比。
source_book: OmniVista 2500 UPAM and Fortinet Single Sign-On Application Note + OmniVista UPAM and Palo Alto Networks User-ID Integration Guide
---

## R（触发场景）
- 评审或规划"局域网认证身份同步给防火墙"方案，先搞清整体原理与路线选型
- 回答"为什么不让防火墙自己认用户"——需要零信任视角论证
- 判断某类终端（AD 域机 vs BYOD/IoT）应该走哪条集成路径
- 对比 Fortinet（RADIUS Accounting）与 PAN（Syslog）两种机制，做产品侧选型说明

## I（核心理念）
传统防火墙按"接在哪里"定信任：内网隐式可信。移动办公与 IoT 时代这套失效——BYOD 可能带毒、IoT 设备天然有漏洞、内部用户也可能恶意，所以今天的范式是零信任（Zero Trust）：无论从哪里接入，永不信任、始终验证（两份笔记 p3）。而验证的核心是先确定身份。UPAM 是 OmniSwitch/OmniAccess Stellar 的统一接入管理平台，内置 captive portal 与 RADIUS 服务器（两份笔记 p3）。集成的本质：终端在 LAN/WLAN 认证一次，UPAM 侧把"用户/角色 + IP"的映射推给防火墙，防火墙即可按角色（而非仅 IP）做策略、日志与取证。两大分支：企业 AD 设备首选直接在 AD 上集成；BYOD/IoT 设备（往往没有 AD 账号）则直接以 UPAM 为集成点（两份笔记 p4），这是两份笔记的主题。

## A1（行动框架）
1. 选集成路线（两份笔记 <<<PAGE 4>>>）：终端是 AD 域设备 → 走 AD/NPAS 集成（防火墙厂商文档，本笔记不展开）；终端是 BYOD/IoT、直接对 UPAM 本地库或外部 RADIUS 认证 → 走本笔记的 UPAM 集成路线
2. 选推送机制（Fortinet <<<PAGE 5>>>、PAN <<<PAGE 4-5>>>）：Fortinet → RADIUS Accounting（UDP 1813，由交换机/AP 直发）；PAN → Syslog（UDP 514，由 UPAM 发）
3. 身份落点二选一：用户名（MAC 认证时就是 MAC 地址）或角色（Filter-Id / uNP / ARP）——按角色做策略最省事，按用户名做日志取证最完整（PAN <<<PAGE 12>>>）

## A2（细节速查）
| 要点 | 说明 | 来源 | 页码 |
|---|---|---|---|
| 零信任动因 | 内网隐式信任过时；BYOD/IoT/恶意内部用户是三大风险 | 两份笔记 | p3 |
| UPAM 能力 | captive portal + RADIUS；MAC/802.1x/Portal 认证；本地库或 AD/LDAP/外部 RADIUS；邮件/短信/社交登录发号 | 两份笔记 | p3 |
| FSSO 定义 | 用户对第三方系统认证后即被透明识别到 FortiGate/FortiAuthenticator/FortiCache | Fortinet | p3 |
| PAN User-ID | PAN 防火墙标准特性，利用多种信息源识别用户 | PAN | p3 |
| 集成收益 | 可视性、最小权限的细粒度策略、按用户/角色的日志报表与取证 | 两份笔记 | p3/结论页 |
| AD 路线 vs UPAM 路线 | 域设备集成点在 AD；BYOD/IoT（无 AD 账号）集成点在 UPAM | 两份笔记 | p4 |
| Fortinet 推送通道 | RADIUS Accounting 消息，交换机/AP 直发 FortiGate（1813）或 FortiAuthenticator | Fortinet | p5 |
| PAN 推送通道 | UPAM 外部 syslog 日志（UDP 514），防火墙解析字段 | PAN | p4-5 |
| 多防火墙场景 | Fortinet：发给 FortiAuthenticator 可免配多套 AAA profile | Fortinet | p5 |

## E（场景案例）
- IoT 摄像头/传感器走 MAC 认证、角色 IoT_Camera/IoT_Sensor 推给防火墙的参考拓扑（两份笔记 <<<PAGE 4>>> Figure 2）
- AD 域用户 Joe/Finance、Jane/Marketing 走 AD 集成的对照拓扑（两份笔记 <<<PAGE 4>>> Figure 1）
- 角色映射后防火墙策略直接引用角色（如 sensor、iot_stb），无需在防火墙建用户（PAN <<<PAGE 12>>>）

## B（限制与坑）
- 集成不改变接入认证本身：交换机/AP 上的 MAC/802.1x/Portal 配置仍是前提（两份笔记 p4-5）
- 域设备走 AD 集成效果更好，硬把所有用户塞进 UPAM 集成不是最佳实践（两份笔记 p4）
- MAC 认证场景下"用户名"就是 MAC 地址，直接拿用户名做策略可读性差——角色（Filter-Id）更合适（PAN p12）

## 来源
来源：OmniVista 2500 UPAM and Fortinet Single Sign-On Application Note（About/Use case/Mechanism，p3-5）；OmniVista UPAM and Palo Alto Networks User-ID Integration Guide（§1-6，p3-5）
