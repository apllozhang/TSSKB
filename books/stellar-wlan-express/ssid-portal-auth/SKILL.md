---
name: ssid-portal-auth
description: 何时用：配置/排查 SSID 业务、访客 Captive Portal 弹页、802.1X 认证、账户与容量问题时。
source_book: DT00XTE455EN Stellar WLAN Express
---

# SSID 业务与内置服务（Portal / 认证 / 账户）

## R · 原文引用

> "User Side: Whether the username and password are correct... AP Side: Check the WLAN's configuration. Whether it is reachable between AP and RADIUS Server using 'tools-ping' on the web page. Server Side: Check the RADIUS Server Client configuration, such as the shared key, RADIUS client IP or IP range, authentication port, certificate." (p140-141)

> "If guest portal cannot pop up after connecting to the 'Guest' SSID (open & portal), check the following: Whether the Captive Portal function in the WLAN is enabled... Check if the client MAC address is in the white list or if the client IP is in the walled garden list. Check if the client enters https URL. If so, enter a http URL because the https redirect for captive portal web page is not yet supported." (p142-143)

> "Check if the valid period of the user account has expired. If so, the user account is invalid and shall disappear from the account list." (p151)

## I · 方法论骨架

Express 的业务层围绕"SSID + 认证模式 + 内置服务"三条线：

1. **认证模式选型**：员工网走 802.1X/WPA2（内置用户数据库或外接 RADIUS）；访客网走开放加密 + Captive Portal（门户认证）。AP 本地还内置 DHCP/DNS/NAT 与防火墙规则，无外部基础设施也能放号出网。
2. **802.1X 失败三侧法**：用户侧（账号密码、终端认证类型匹配）→ AP 侧（WLAN 配置、tools-ping 验 AP 到 RADIUS 连通性）→ 服务器侧（共享密钥、client IP/网段、认证端口、证书），三方各自排干净再对报文。
3. **Portal 不弹页四查**：Portal 功能开关 → 认证开关 → 白名单/walled garden 命中 → https URL 限制；仍不弹用 `ps | grep eag` 查 EAG 进程。
4. **连接类排障递进**：密码 → blocklist 黑名单 → MaxClients 容量 → 终端残留记录 → wam 进程。

## A1 · 书中案例

- 802.1X 排障（Case 5）：先验账号密码与终端认证类型，再在 Web 用 tools-ping 验 AP→RADIUS 连通，最后核 RADIUS 服务器的 client 配置四项（shared key/IP/端口/证书），必要时两侧抓包对报文（p140-141）。
- Portal 不弹页（Case 6）：四查之后仍不弹，Console 执行 `ps | grep eag` 确认门户重定向模块存活（p142-143）。
- 连不上 AP/集群（Case 8）：密码核对 → Web 上查 blocklist 点红叉移除 → 看在线数是否顶到 MaxClients、顶到就调参 → 清终端保存的 WLAN 记录 → `ps | grep wam` 查 ath 端口进程，缺失用 `wam -P /var/run/wifi-athXX.pid -B /var/run/wam-athXX.conf` 重建，再不行 `cat /proc/kes_syslog | grep <clientMAC>` 跟踪（p148-150）。

## A2 · 触发场景（含与相邻 skill 的区分）

- 触发：部署员工/访客 SSID、访客反映"连上了但不出登录页"、802.1X 认证失败、老用户正常新用户连不上、访客账户"消失"。
- 区分：**AP 本身**上电/IP/入组故障用 `ap-side-troubleshooting`；吞吐差、信号弱等射频问题用 `rf-survey-tuning`；本 skill 只管业务层——认证、门户、账户、客户端接入策略。客户端能关联但拿不到 IP 属 VLAN/DHCP 链路问题，归 `ap-side-troubleshooting`（Case 7 抓包定位法）。

## E · 可执行步骤

员工 SSID + 802.1X：
1. WLAN 配置认证 802.1X，指向内置用户数据库或外部 RADIUS。
2. 验证路径：终端实连 → Web 界面 tools-ping RADIUS → 核服务器 client 四项。
3. 失败时按三侧顺序排查（用户→AP→服务器），最后 tcpdump 抓发往 RadiusIP 的报文看交互。

访客 SSID + Portal：
4. 建 Guest SSID（开放加密），启用 Captive Portal 功能与认证开关。
5. 建访客账户：设足够有效期（GuestOperator 受限角色可供前台自助开户，看不到全局配置）。
6. 弹页排障四查 + `ps | grep eag`；日志用 `cat /var/log/eag.log`。

连接类问题：
7. 按序：密码 → blocklist 移除 → MaxClients 调大 → 清终端记录 → wam 进程查/重建 → kes_syslog 跟踪。
8. 主动利用白名单/walled garden 给打印机、POS 等哑设备开免认证通道。

## B · 边界与陷阱

- **https 不重定向**：内置 Portal 不支持 https 跳转（版本限制）。访客默认打开 https 首页会"永远不弹页"，引导手动输 http 网址（如 http://neverssl.com）。
- **白名单/walled garden 命中即不弹页**——这是设计行为不是故障，排障先核这两个清单。
- **访客账户过期即从账户列表消失**：现场表现"昨天能上今天失败、列表查无此人"，易误判为被删号。排障顺序：账号密码 → 有效期 → EAG 进程。
- **MaxClients 顶满拒新连接**：表现"老用户正常、新用户连不上"，与密码错误/黑名单易混淆；高密场景（会议室/大堂）上线前按容量预算调参。
- Express 无 UPAM（网管级统一策略认证），对应能力由内置数据库 + 内置/外部门户替代。

---
来源条目: c09, c10, c12, ce06, ce07, ce13, ce14, g10, g11, g12, g29
