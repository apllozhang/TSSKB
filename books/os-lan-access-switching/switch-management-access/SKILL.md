---
name: switch-management-access
description: 何时用：首次登录/远程管理 OmniSwitch（SSH/WebView/AAA/用户库）、Lightning 开局或管理会话规划时。
source_book: DT00XTE215EN Access Switching
---

# 交换机管理接入：登录 / AAA / 用户库 / 开局

## R · 原文引用

"The Local userDB file is named userTable9. Path: flash/system directory. By default: 2 users 'admin and default'. Login: admin Password: switch. Up to 64 users can be configured... Beginning in 8.10R4 changing the default password will be mandatory."（p38-39）

"aaa authentication {console | telnet | ftp | http | snmp | ssh | default} server1 [server2...] [local] [exit-on-fail {enable | disable}]"（p41）

"The easy configuration process (Lightning configuration) starts if: Only first or second physical port connected with the client, no other ports connected / No prior switch configuration exist / No DHCP address assignment occurs after boot up."（p51）

"Completion: Recognize partial keywords... Eg: sh vl for show vlan. Built-in Filtering: -> show vlans | more / -> show mac-learning | grep 00:20:da:55:56:76."（p77）

## I · 方法论骨架

- **首次登录**：默认 admin/switch（另有 default 账户）；本地用户库 userTable9 存 /flash/system，上限 64 用户，权限按命令域/族划分。8.10R3 起提示改默认密码、8.10R4 强制。
- **ASA（管理面准入）**：按 console/telnet/ftp/http/snmp/ssh/default 七类服务分别指定认证链（RADIUS/LDAP/local 排队）；exit-on-fail enable=只用第一台可用服务器，disable=逐台 fail-through。
- **会话规格**：Telnet 6 / FTP 4 / SSH+SFTP 8 / HTTP 4，五类合计（含 console）20，SNMP 50——规划带外管理规模按此。
- **WebView**：内置 Web 管理，R8 强制 SSL（webview force-ssl enable 默认）；仅单机视图。
- **Lightning 开局**：仅当"只连 1/1/1-2、无配置、无 DHCP、无 RCL/NMS"四条件同时满足才进 Quick Config 向导（默认 VLAN1 192.168.0.1/24）；首次 write memory 后默认 IP 失效。
- **CLI 行规**：sh vl 式缩写、|more/grep/egrep/sort 管道、? 帮助、history；目录操作沿用 Unix（pwd/cd/mkdir/cp/rm）。

## A1 · 书中案例（Lab 配置精要）

远程访问 Lab（p54-63）：先 `show aaa authentication` 确认 SSH/HTTP 用本地库（若 denied 用 `aaa authentication ssh local`）；Tera Term SSH 登录（admin/switch）；改不活动超时 `session cli timeout 60` 并 write memory；WebView（https://管理IP）在 Security>ASA 改 CLI/HTTP 超时，Layer2>VLAN 建 VLAN 59（Student）再删，CLI 用 show vlan 双向验证。

## A2 · 触发场景（含与相邻 skill 的区分）

- 怎么登上交换机、谁来能登、开局向导、管理会话数够不够——本 skill。
- 端口上终端用户的 802.1X/MAC 准入（Access Guardian）→ access-guardian-unp；本 skill 只管"管理员→交换机"方向。
- 登录后的配置保存/目录 → aos-config-management。

## E · 可执行步骤

1. 首登：admin/switch；8.10R4 前主动改密码（user password-refresh 可强制下次刷新）。
2. 核对/配置认证链：`show aaa authentication` → `aaa authentication ssh|http|default <srv1> [<srv2>] [local] [exit-on-fail …]`；拒绝 HTTP 管理：`no aaa authentication http`。
3. 会话参数：`session cli timeout <秒>`；write memory 保存。
4. 远程访问：SSH（首选）/ WebView（https，R8 强制 SSL）。
5. 带外：EMP 口直连 CMM（无 EMP 的 6360/6465/6560 用 USB-Ethernet dongle 等效）；VC 场景配 master EMP 地址。
6. 新机开局：满足四条件走 Lightning Quick Config（https://192.168.0.1），完成即 write memory 固化。
7. CLI 提效：缩写（sh vl）、管道过滤、? 帮助。

## B · 边界与陷阱

- 默认口令 admin/switch 在 8.10R4 起强制修改，自动化脚本别写死。
- exit-on-fail 语义反直觉：enable 是"只用第一台可用"，disable 才是逐台尝试（fail-through）——多 RADIUS 容灾场景要 disable。
- Lightning 触发条件四个全满足才进；曾 write memory 过的机器不再有默认 IP。
- WebView 仅单机视图，VC/多机管理需 OmniVista（Thin Client 模式下配置全部在 OV 2500，本地 write memory 不落盘）。
- 会话总数 20（含 console），SNMP 50，监控平台接入数按此规划。

---
来源条目: p01, p09, p10, p11, p12, c01, g06, g07, g14, g15, g16, g17
