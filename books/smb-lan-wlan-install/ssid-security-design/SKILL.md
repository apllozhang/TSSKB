---
name: SSID 规划与认证策略设计
description: 当需要创建员工/访客 SSID、配置密码或 802.1X/外部 RADIUS 认证、部署 Captive Portal 访客门户或 AP 内置 DHCP 时使用本技能。
source_book: DT00XTE301 LAN & WLAN Installation & Configuration for SMB
---

## R（触发场景）
- 要按员工/访客两类人群分别建 SSID 并映射到不同 VLAN
- 访客需要 Captive Portal 门户认证、访客账号或行为日志审计
- 需要 802.1X/外部 RADIUS 企业认证，或 AP 内置 DHCP 分段地址

## I（核心理念）
SSID 是用户分流入口：客户端连上 SSID 即自动落入预定义 VLAN，再叠加带宽/优先级/访问范围差异化策略。认证三档：Personal 密码（员工轻量）、Enterprise 802.1X（UPAM 或外部 RADIUS）、Open + Captive Portal（访客，账号/接入码/条款三选一）。Cirrus 侧用 ARP（Access Role Profile）六元组集中描述用户策略，其裁决顺序：外部源 > 内部用户库 > 认证策略 > SSID 默认。

## A1（行动框架）
1. 员工 SSID（Express）：WLAN > New > 名称 EmployeesX、Security Personal、密码 superuser > Advanced > VLAN ID 20 > Save；客户端 `ifconfig` 确认落在 192.168.20.x（C11，<<<PAGE 221>>>–<<<PAGE 224>>>）。
2. 访客 SSID（Express）：WLAN > New > GuestsX、Security Open、Captive Portal Yes、VLAN 30 > Access > Authentication 选 Account > Add 建访客账号（设起止日期）> 客户端访问任意 non-https URL 触发门户 > 登录后取 192.168.30.x（C12，<<<PAGE 225>>>–<<<PAGE 228>>>）。
3. AP 内置 DHCP：AP > 点 AP IP > Network > AP Networks > vlan10 行 Manage 填 IP 192.168.10.3/24 > Service > DHCP > Create（Pool 名、地址范围、网关/DNS）> Action > Bind Network 绑到 vlan（C13，<<<PAGE 229>>>–<<<PAGE 233>>>）。
4. 外部 RADIUS（Enterprise SSID）：WLAN > New > Security Enterprise > AuthServer 填 RADIUS IP（192.168.1.250）+ AuthSecret > Advanced > VLAN 10 > Save（C16，<<<PAGE 235>>>）。
5. 访客审计与受限管理：
   - Access > Authentication > Client Behavior Tracking，Log To 选 TFTP/SFTP/Syslog 填服务器与周期；日志含时间、客户端 MAC/IP、AP MAC、SSID、ONLINE/OFFLINE（C14，<<<PAGE 233>>>）。
   - System > General > Account Management > Operator Enable 设密码，重登选 GuestOperator 只管访客账号（C15，<<<PAGE 234>>>）。

## A2（进阶应用）
- Cirrus SSID 五步向导（F05，<<<PAGE 365>>>、<<<PAGE 372>>>、<<<PAGE 405>>>、<<<PAGE 413>>>）：通用设置（名称/Usage/频段/加密）→ 认证策略（UPAM/外部 RADIUS/LDAP）→ 访问策略 → 默认 VLAN/隧道 + ACL/QoS → AP Group 指派与排程；Guest 版增加 Guest Access Strategy（门户定制 + 登录方式）。
- ARP 裁决顺序（F06，<<<PAGE 382>>>、<<<PAGE 385>>>）：外部源（RADIUS Filter-ID / LDAP/AD）> 内部用户库 > 认证策略中的 ARP > SSID 默认 ARP（`__SSID名`）。ARP 六元组 = VLAN / QoS / 防火墙 ACL / L7 应用规则 / 位置 / 时段（P41，<<<PAGE 376>>>）。
- 三角色差异化策略（P38，<<<PAGE 217>>>）：Employees = VLAN10 全访问高带宽；Guests = VLAN20 仅 internet 常规带宽低优先级；Phones = VLAN30 话音低带宽高优先级。
- Walled Garden：访客认证前白名单放行指定站点（如酒店官网）（P49，<<<PAGE 235>>>、<<<PAGE 410>>>）。
- MAC 认证可回传 Filter-ID 指定套用的 ARP（glossary·<<<PAGE 384>>>、<<<PAGE 385>>>）。
- GRE Tunnel（Use Tunnel）：SSID 用户经 GRE 隧道集中到远端解封的映射方式（glossary·<<<PAGE 369>>>）。
- DHCP Pool 容量即并发上限：40 个地址 = 最多 40 台同时在线（C13，<<<PAGE 229>>>–<<<PAGE 233>>>）。

## E（实证案例）
- Employees SSID 密码认证 + VLAN20，客户端落 192.168.20.70-79，网关 192.168.20.7 为交换机 VLAN20 IP 接口（C11，<<<PAGE 221>>>–<<<PAGE 224>>>）。
- Guests SSID 内置 Captive Portal + 访客账号 Guest/superuser，non-https URL 重定向门户（C12，<<<PAGE 225>>>–<<<PAGE 228>>>）。
- UPAM 统一策略认证：内嵌 RADIUS 服务器 + Captive Portal，覆盖 MAC/802.1X/Portal 三类认证（P40，<<<PAGE 367>>>、<<<PAGE 188>>>）。

## B（边界与陷阱）
- Captive Portal 重定向必须访问 non-https URL（如 http://2.2.2.2）；访问 https 站点不触发重定向，Debian 树莓派不会自动弹门户，易误判门户故障（CE11，<<<PAGE 422>>>）。
- 访客账号用户名/密码区分大小写（'Guest' ≠ 'guest'），大小写不符是门户登录失败首因（CE12，<<<PAGE 226>>>）。
- SSID→VLAN 是自动预定义映射，规划时先定 VLAN 再建 SSID，避免客户端落错网段（P36，<<<PAGE 215>>>）。

## 来源
- case·Employees SSID 创建（<<<PAGE 221>>>–<<<PAGE 224>>>）
- case·Guests SSID + Captive Portal + 访客账号（<<<PAGE 225>>>–<<<PAGE 228>>>）
- case·AP 内置 DHCP 服务器（<<<PAGE 229>>>–<<<PAGE 233>>>）
- case·访客行为日志（<<<PAGE 233>>>）
- case·GuestOperator 受限账号（<<<PAGE 234>>>）
- case·外部 RADIUS 认证 SSID（<<<PAGE 235>>>）
- framework·SSID 创建向导五步流程（<<<PAGE 365>>>、<<<PAGE 372>>>、<<<PAGE 405>>>、<<<PAGE 413>>>）
- framework·ARP 优先级裁决规则（<<<PAGE 382>>>、<<<PAGE 385>>>）
- principle·SSID→VLAN 自动映射（<<<PAGE 215>>>）
- principle·AP 内置 QoS/ACL 三角色用例（<<<PAGE 217>>>）
- principle·Captive Portal 三种认证方式（<<<PAGE 226>>>）
- counter·门户重定向需 non-https（<<<PAGE 422>>>）
- counter·账号字段区分大小写（<<<PAGE 226>>>）
