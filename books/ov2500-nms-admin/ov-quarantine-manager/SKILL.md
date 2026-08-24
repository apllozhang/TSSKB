---
name: Quarantine Manager 攻击隔离
description: 需要检测并遏制网络攻击终端（DoS/端口扫描/流氓 AP/病毒），配置内置或自定义隔离规则、Responder（邮件/外部程序），以及管理 Candidates/Banned/Never Banned 三列表时使用。
source_book: DT00XTE311 OmniVista 2500 NMS Administration R4
---

## R（触发场景）
- 交换机上报 DoS Trap（Teardrop/Ping of Death/Port Scan）或第三方 IPS/防火墙告警，要自动隔离源设备
- WLAN 出现 Rogue AP/Station 需要处置
- 需要理解"进了候选名单"和"被隔离"的区别，避免误判

## I（核心理念）
Quarantine Manager 是"检测 → 规则 → 执行 → 响应"闭环：检测来源开放（AOS AlaDosTrap、Syslog、第三方 IPS/IDP、Brick Firewall、OA WLAN Rogue Alert）；规则默认全部禁用，需要显式启用；执行手段从 VLAN 隔离到端口关断分级；三列表模型决定设备命运——Candidates 只是"等管理员决策"，Banned 才是真隔离。

## A1（行动框架）
1. **启用内置规则族**（默认全禁用，<<<PAGE 304>>>）：
   - Alcatel DOS Trap Rule：Teardrop / Ping of Death / Port Scan
   - Fortinet：Anomaly / Signature / Virus（Fortigate 上配 Pass 的项会被忽略）
   - OA WLAN：Rogue AP Active / Rogue AP Detected / Station w/ Rogue AP
2. **自定义规则四要素**（<<<PAGE 305>>>）：名称、描述、触发表达式、提取表达式（取源地址）、动作（入 Candidates 或 Banned）
3. **执行手段**（<<<PAGE 307/298>>>）：VLAN MAC Rule（`vlan 999 <mac_address>`）、VLAN DHCP MAC Rule、ACL（condition IP source <> action <>）、IP<->MAC 绑定、SNMP Set message；第三方交换机可 Port Shutdown，无线侧可 end user block listing
4. **三列表处置**（<<<PAGE 308-310>>>）：Candidates——流量继续放行，等管理员 Release/Ban/Never-ban；Banned——"it remains quarantined until the Network Administrator manually releases it."；Never Banned——OV 服务器与已发现交换机被隐式加入
5. **Responder**（<<<PAGE 311>>>）：配置邮件通知（可基于变量拼内容）或让 AQM 在 OV 服务器上执行外部程序/脚本

## A2（进阶应用）
- 遏制与 UNP 体系联动：攻击检测的终端可通过 VLAN/ACL 执行手段与 Unified Access 端口策略组合（参考 <<<PAGE 303-307>>> 框架）
- 邮件链路复用全局 SMTP 配置（Administration > Preferences > System Settings > Email），先 Send Test E-mail 验证（<<<PAGE 191>>>）

## E（实证案例）
- 内置规则族盘点（AlaDosTrap/Fortinet/OA WLAN）与自定义规则四要素——cases·QM 内置规则（<<<PAGE 304-305>>>）
- QM Responder 邮件变量与外部程序执行——cases·QM Responder（<<<PAGE 311>>>）

## B（边界与陷阱）
- "By Default all of the rules are disabled."——以为开了其实没开是最常见错觉（<<<PAGE 304>>>）
- Candidates 语义陷阱："If a device is placed on the Candidates List, traffic to and from that device will continue until the Network Administrator decides what action should take place."（<<<PAGE 308>>>）
- Banned 不会自动解封，必须管理员手动 Release（<<<PAGE 309>>>）

## 来源
- frameworks·检测-规则-执行-Responder 框架（<<<PAGE 303-310>>>）
- principles·遏制执行机制（<<<PAGE 307/298>>>）、三列表语义（<<<PAGE 308-310>>>）
- cases·内置规则族/Responder（<<<PAGE 304-305/311>>>）
- counter-examples·默认禁用/Candidates 语义（<<<PAGE 304/308>>>）
