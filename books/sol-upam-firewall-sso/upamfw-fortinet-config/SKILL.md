---
name: Fortinet 集成配置步骤与验证排障（RSSO 连接器/Filter-Id 用户组/角色策略/两条诊断命令）
description: 需要动手配置或排查 OmniVista UPAM 与 FortiGate 的 SSO 集成时使用：OmniVista 侧 4 步（注册 RADIUS 服务器、AAA profile、认证策略与 Access Policy、Access Auth Profile）、FortiGate 侧 7 步（接口开 RADIUS Accounting、RSSO 连接器、CLI 指定 User-Name/Filter-Id 属性、RSSO 用户组、角色防火墙策略、GUI/CLI 验证映射与策略）。
source_book: OmniVista 2500 UPAM and Fortinet Single Sign-On Application Note
---

## R（触发场景）
- 按手册落地 UPAM ↔ FortiGate 集成，需要逐步操作路径与菜单入口
- 配完不生效：用户映射看不到、策略命中不了角色，需要验证命令定位
- 新增一个角色（ARP）后要在防火墙侧补配对应的用户组与策略

## I（核心理念）
配置分两条线，先 OV 后 FortiGate。OV 侧把 FortiGate 当"记账用 RADIUS 服务器"注册，再通过 AAA profile → Authentication Strategy/Access Policy → Access Auth Profile 这条模板链把它挂到认证流里。FortiGate 侧三件事：接口监听 1813、建 RSSO（RADIUS Single Sign-On）连接器并指定 User-Name 与角色（Filter-Id）属性、把 Filter-Id 值做成 RSSO 用户组并写进防火墙策略的 Source。验证收口在两条命令：GUI 的 Firewall Users 面板与 CLI 的 `diagnose firewall auth list`。

## A1（行动框架）
1. OV 侧四步（有依赖顺序）：① 注册 FortiGate/FortiAuthenticator 为 RADIUS 服务器（名字+共享密钥）→ ② 建 AAA Server Profile（认证指 UPAM、记账指 FortiGate，按 802.1x/MAC/Portal 分别配，interim 默认 600s）→ ③ 建 Authentication Strategy（需先有默认 ARP）与 Access Policy（按 SSID/NAS IP/Location 路由请求）→ ④ 建 Access Auth Profile（含 default 与 pass-alternate）并应用到交换机/AP 组（<<<PAGE 6-9>>>）
2. FortiGate 侧五步：① 接口开 RADIUS Accounting → ② Security Fabric → External Fabric Connectors 建 RADIUS SSO Agent（Use RADIUS Shared Secret 填 OV 侧同一密钥，开 Send RADIUS responses）→ ③ SSH 进 CLI 编辑 RSSO 连接器指定 User-Name 与 Filter-Id 属性 → ④ User & Authentication → User Groups 建 RSSO 型组，RADIUS Attribute Value 填 UPAM 侧 ARP 名 → ⑤ Policy & Objects 里建策略，Source 同时选地址对象与 RSSO 用户组（<<<PAGE 10-14>>>）
3. 验证两步：Dashboard → Users & Devices → Firewall Users 看映射（或 `diagnose firewall auth list`）；Log & Report → Forward Traffic 看策略是否正确识别 user/group（<<<PAGE 15-16>>>）

## A2（细节速查）
| 步骤 | 菜单/命令路径 | 关键参数 | 来源 | 页码 |
|---|---|---|---|---|
| 注册 RADIUS 服务器 | Security → Authentication Server → RADIUS，"+" | FortiGate IP 或名称 + shared secret | Fortinet | p6 |
| AAA Server Profile | Unified Access → Template → AAA Server Profile，"+" | 认证=UPAMRadiusServer；记账=FortiGate；interim 默认 600s | Fortinet | p7 |
| Authentication Strategy | UPAM → Authentication → Authentication Strategy，"+" | 默认 ARP 须先建好 | Fortinet | p8 |
| Access Policy | UPAM → Authentication → Access Policy，"+" | 按 SSID/NAS IP/Location 匹配策略 | Fortinet | p8-9 |
| Access Auth Profile | Unified Access → Unified Profile → Templates → Access Auth Profile | default + pass-alternate，应用到交换机/AP 组 | Fortinet | p9 |
| 接口开记账 | Network → Interfaces → 编辑接口 | Administrative Access 勾 RADIUS Accounting，监听 1813 | Fortinet | p10 |
| RSSO 连接器 | Security Fabric → External Fabric Connectors → Create New → RADIUS Single Sign-On Agent | Use RADIUS Shared Secret（同 OV 密钥）；Send RADIUS responses | Fortinet | p11-12 |
| 指定属性 | SSH CLI 编辑 RSSO 连接器 | User-Name 与角色（Filter-Id）属性 | Fortinet | p12 |
| 用户组 | User & Authentication → User Groups → Create New | 类型选 RSSO；Attribute Value = ARP 名（即 Filter-Id），按角色重复建组 | Fortinet | p13 |
| 角色防火墙规则 | Policy & Objects → Firewall Policy → Create New | Source = 地址对象 + RSSO 用户组 | Fortinet | p14 |
| 验证映射 | Dashboard → Users & Devices → Firewall Users；CLI `diagnose firewall auth list` | — | Fortinet | p15 |
| 验证策略 | Log & Report → Forward Traffic | 查看条目右侧面板的 user/group | Fortinet | p16 |

## E（场景案例）
- IoT 设备 MAC 认证：Access Auth Profile 用 IOT_Default 作 default/pass-alternate，认证后 FortiGate 侧 Firewall Users 面板出现用户与角色映射（<<<PAGE 9>>>/<<<PAGE 15>>>）
- 多角色放行：为 IoT_Camera、IoT_Sensor 各建一个 RSSO 用户组，Source 里按需叠加，策略即按角色区分放行（<<<PAGE 13-14>>>）
- 取证：Forward Traffic 日志里按用户/角色过滤活动，而不只是 IP（<<<PAGE 16>>>/<<<PAGE 17>>>）

## B（限制与坑）
- 指定 User-Name/Filter-Id 属性这步 GUI 做不了，必须 SSH 到防火墙用 CLI（<<<PAGE 12>>>）
- 共享密钥两处必须一致：OV 注册 RADIUS 服务器处与 RSSO Agent 的 Use RADIUS Shared Secret（<<<PAGE 6>>>/<<<PAGE 11>>>）
- RSSO 用户组的 Attribute Value 必须逐字等于 UPAM 侧 ARP/uNP 名，写错则映射归不进组、策略不命中（<<<PAGE 13>>>）
- 默认 ARP 没先建 → Authentication Strategy 建不起来；ARP 未映射到交换机/AP 组 → 角色下发不生效（<<<PAGE 8>>>）
- 服务器名解析不了 DNS 的设备（无 DNS 的交换机/AP）会发不出 accounting，改填 IP（<<<PAGE 6>>>）

## 来源
来源：OmniVista 2500 UPAM and Fortinet Single Sign-On Application Note（Procedure overview 至 Verifying user-based policies，p5-16）
