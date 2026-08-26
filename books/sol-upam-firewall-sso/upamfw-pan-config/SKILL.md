---
name: PAN 集成配置步骤与验证排障（Zone User-ID/Syslog 监听/解析过滤器/Server Monitoring/验证命令）
description: 需要动手配置或排查 OmniVista UPAM 与 Palo Alto 防火墙 User-ID 集成时使用：OmniVista 侧 4 步（AAA profile、认证策略与 Access Policy、外部 syslog 日志、Access Auth Profile）、PAN 侧 7 步（Zone 开 User-ID、Interface Management 开 UDP Syslog Listener、Syslog Parse Profile、Server Monitoring、User-ID 策略、CLI/GUI 验证映射与策略）。
source_book: OmniVista UPAM and Palo Alto Networks User-ID Integration Guide
---

## R（触发场景）
- 按手册落地 UPAM ↔ PAN 集成，需要逐步操作路径与菜单入口
- 配完映射出不来：syslog 测试报"连不上"、`show user ip-user-mapping all` 空、策略不命中角色
- 新增角色（ARP/uNP）后需要在 PAN 侧补配解析与策略引用

## I（核心理念）
配置分两条线。OV 侧与 Fortinet 方案前半段相同（AAA profile → 策略链 → Access Auth Profile），差别在：AAA profile 的认证与记账**都**指向 UPAM（记账不再外发防火墙），并额外在 Settings → External Log Server 把日志以 syslog（UDP 514）发往 PAN。PAN 侧四件事：目标 Zone 开 User-ID；接口管理配置文件开 User-ID Syslog Listener 并登记 UPAM 的 IP；建 Syslog Parse Profile 告诉防火墙从 UPAM 日志里取 username 或 filterID；建 Syslog Sender 型 Server Monitoring 把三者串起来。策略里引用角色（filter-id）时全部用小写。

## A1（行动框架）
1. OV 侧四步：① AAA Server Profile：认证与记账均指 UPAMRadiusServer（按 802.1x/MAC 分别配；interim 默认 600s，须 < 防火墙 45 分钟超时）→ ② 建 Authentication Strategy（默认 ARP 先行）与 Access Policy（按 SSID/NAS IP/Location）→ ③ Settings → External Log Server：启用，Syslog 默认端口 514，可加第二台取证服务器 → ④ Access Auth Profile（default + pass-alternate）应用到交换机/AP 组（<<<PAGE 6-10>>>）
2. PAN 侧四步：① Network → Zones 对相关 Zone 勾 User-ID（可配 include/exclude ACL）→ ② Network Profiles → Interface Management 勾 User-ID Syslog Listener UDP，加入 UPAM IP，套到接收接口 → ③ Device → User Identification → User Mapping 齿轮 → Syslog Filters → Add：映射 username+deviceIP，或更简单地只映射 filterID（角色）→ ④ Server Monitoring → Add：类型 Syslog Sender、UDP、UPAM IP、选上面的解析过滤器，可补域名前缀（<<<PAGE 10-13>>>）
3. 策略与验证：Policies → Security → User 标签加入角色（小写）；CLI `show user ip-user-mapping all` 验证映射；Monitor → Logs → Traffic 验证策略命中（<<<PAGE 14>>>）

## A2（细节速查）
| 步骤 | 菜单/命令路径 | 关键参数 | 来源 | 页码 |
|---|---|---|---|---|
| AAA Server Profile | Unified Access → Template → AAA Server Profile，"+" | 认证+记账均指 UPAMRadiusServer；interim 默认 600s | PAN | p6-7 |
| Authentication Strategy | UPAM → Authentication → Authentication Strategy，"+" | 默认 ARP 须先建 | PAN | p8 |
| Access Policy | UPAM → Authentication → Access Policy，"+" | 按 SSID/NAS IP/Location 匹配 | PAN | p9 |
| 外部 syslog | UPAM → Settings → External Log Server | Syslog，端口 514；可加第二台服务器 | PAN | p9 |
| Zone 开 User-ID | Network → Zones | 勾选 User-ID；可选 include/exclude ACL | PAN | p10 |
| Syslog 监听 | Network Profiles → Interface Management | 勾 User-ID Syslog Listener UDP，登记 UPAM IP，套到接收接口 | PAN | p11 |
| 解析过滤器 | Device → User Identification → User Mapping → 齿轮 → Syslog Filters → Add | 映射 username/deviceIP 或 filterID（角色） | PAN | p11-13 |
| Server Monitoring | Device → User Identification → Server Monitoring → Add | 类型 Syslog Sender、UDP、UPAM IP、选过滤器；可配域名前缀与子网 include/exclude | PAN | p13 |
| User-ID 策略 | Policies → Security → User 标签 → Add | 角色（filter-id）全小写；用户名方案则逐个列或建本地组 | PAN | p14 |
| 验证映射 | CLI `show user ip-user-mapping all` | 大写用户名会显示为小写 | PAN | p14 |
| 验证策略 | Monitor → Logs → Traffic | 示例：integration_test 策略对 iot_stb 角色 block ping | PAN | p14 |

## E（场景案例）
- IoT 机顶盒角色管控：filter-id=iot_stb（set-top box）加入策略 Source，日志确认 ping 被阻（<<<PAGE 14>>>）
- MAC 认证 + 角色映射组合：无需在防火墙本地库创建任何用户即可按角色下发策略（<<<PAGE 12>>>）
- UPAM 日志双发：一份进 PAN 做映射，一份进独立 syslog 服务器留真实用户名备取证（<<<PAGE 9>>>/<<<PAGE 12>>>）

## B（限制与坑）
- UPAM 上测试 syslog 连接会报 "The server cannot connect"——PAN 不回应 syslog 连接测试，这是预期行为；仍要手工确认 UDP 514 连通（<<<PAGE 9>>>）
- Syslog Listener 忘了套到实际接收接口，或没登记 UPAM 的 IP → 日志被丢弃（<<<PAGE 11>>>）
- 策略里角色大小写：PAN 会把用户名转小写，策略用大写引用不命中（<<<PAGE 14>>>）
- 每个 syslog 源仅一个解析过滤器，只配了 Accounting：断线不会即时登出，靠 45 分钟超时（<<<PAGE 5>>>）
- 认证本地库时日志无域名，可在 Server Monitoring 里配域名前缀补齐（<<<PAGE 13>>>）

## 来源
来源：OmniVista UPAM and Palo Alto Networks User-ID Integration Guide（§7-18 Procedure overview 至 Verifying User-ID policies，p6-14）
