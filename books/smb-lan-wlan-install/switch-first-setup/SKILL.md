---
name: 交换机开箱与基础管理配置
description: 当新到货一台 OmniSwitch 需要首次开通、配管理 IP、开远程管理，或需要用 Lightning Config 批量快速交付时使用本技能。
source_book: DT00XTE301 LAN & WLAN Installation & Configuration for SMB
---

## R（触发场景）
- 新交换机上电，需要开通端口、配置管理 IP 并保存配置
- 需要开启 SSH/HTTP 远程管理或检查会话超时
- 多台新交换机开箱，希望 5 分钟内完成单台基础配置（Lightning Config）

## I（核心理念）
OmniSwitch 出厂默认凭据是 admin/switch（8.10R4 起强制改密），Console 是最后一道兜底管理通道。各管理通道（Console/Telnet/SSH/HTTP）的认证相互独立，默认 SSH/HTTP 是 deny 状态，必须逐项用 `aaa authentication` 打开。开箱场景优先走 Lightning Config 向导，CLI 是通用兜底。

## A1（行动框架）
1. Console 连接：串口参数 115200 / 8N1 / 无流控（P12，<<<PAGE 65>>>），Tera Term/Putty 登录 admin/switch（P06，<<<PAGE 60>>>）。
2. 开通端口：
   ```
   -> interfaces 1/1/6 admin-state enable
   -> interfaces 1/1/1 admin-state enable
   ```
3. 配管理 IP 并验证保存：
   ```
   -> ip interface int_1 address 192.168.1.2/24 vlan 1
   -> show ip interface
   -> write memory flash-synchro
   ```
   （C01，<<<PAGE 95>>>–<<<PAGE 96>>>）
4. 开远程管理：
   ```
   -> aaa authentication ssh local
   -> aaa authentication http local
   -> show aaa authentication
   -> show webview
   -> show session config   // Inactivity Timer：CLI 45 / HTTP 15 分钟
   ```
   （C05，<<<PAGE 107>>>–<<<PAGE 111>>>）
5. Lightning Config 路线（新机开箱）：笔记本设 DHCP → 网线接 port 1 → 上电等 3 分钟 → Chrome 访问 `https://192.168.0.1/`（本机约获 192.168.0.200）→ admin/switch + 接受自签证书 → RECOMMENDED DEFAULTS → LIGHTNING CONFIG 填 IP/网关 → 改 admin 密码（8 位以上含大小写/数字/特殊字符，勿用 `!` 或 `$`）→ 保存为 working（C26，<<<PAGE 481>>>–<<<PAGE 490>>>）。

## A2（进阶应用）
- Lightning Config 触发有五项前置：仅第 1/2 物理口接客户端、无既有配置、上电后无 DHCP 分配、无 RCL/OmniVista NMS 连接（F07，<<<PAGE 75>>>）；任一不满足则退回常规配置。
- 模板批量交付：IMPORT .json 模板 → Lightning Config → SAVE CONFIGURATION（C26，<<<PAGE 481>>>–<<<PAGE 490>>>）。
- 多服务器认证链：`aaa authentication console server1 [server2...] [local] [exit-on-fail {enable|disable}]`；exit-on-fail enable 时只查首台可用服务器，disable 时逐台回退（P08，<<<PAGE 63>>>）。
- 会话规格上限：Telnet 6 / FTP 4 / SSH+SFTP 8 / HTTP 4 / 总 20 / SNMP 50（P10，<<<PAGE 67>>>）。
- EMP 带外管理口绕过业务板直连 CMM：`ip interface master emp address 172.25.167.203 mask 255.255.255.224`；无 EMP 机型可用 USB Ethernet Dongle 等效（P11，<<<PAGE 66>>>）。
- WebView 默认强制 HTTPS/TLS1.2（`webview force-ssl enable`，P09，<<<PAGE 68>>>–<<<PAGE 69>>>）。

## E（实证案例）
- 首次登录 OS6360 开通 1/1/6（AP 口）与 1/1/1（客户端口），配 192.168.1.2/24 后 `show ip interface` 验证、`write memory flash-synchro` 保存（C01，<<<PAGE 95>>>–<<<PAGE 96>>>）。
- `aaa authentication ssh local` 前 SSH 默认被 deny，配置后经 `show aaa authentication` 确认（C05，<<<PAGE 107>>>–<<<PAGE 109>>>）。
- Lightning Config 全流程含 .json 模板导入（C26，<<<PAGE 481>>>–<<<PAGE 490>>>）。

## B（边界与陷阱）
- Lightning Config 前禁止把新交换机接入网络/互联/接 DHCP 服务器：多台未配置交换机默认都是 192.168.0.1 会 IP 冲突；且"Do NOT skip the Recommended Defaults!"（CE13，<<<PAGE 477>>>、<<<PAGE 486>>>、<<<PAGE 484>>>）。
- 教学或托管环境的"默认配置"并非空配置，重置后所有端口 disabled，不通时先 `interfaces x admin-state enable`（CE01，<<<PAGE 89>>>）。
- 密码勿用 `!` 或 `$` 字符（C26，<<<PAGE 481>>>–<<<PAGE 490>>>）。
- 本地用户库 userTable9 存于 flash/system，最多 64 用户（P06，<<<PAGE 60>>>–<<<PAGE 61>>>）。

## 来源
- case·首次登录并开通 OS6360 端口与管理 IP（<<<PAGE 95>>>–<<<PAGE 96>>>）
- case·开启 SSH/HTTP 远程管理（<<<PAGE 107>>>–<<<PAGE 111>>>）
- case·Lightning Config 完整实操含模板导入（<<<PAGE 481>>>–<<<PAGE 490>>>）
- framework·Lightning Config 触发条件与部署流程（<<<PAGE 75>>>、<<<PAGE 474>>>–<<<PAGE 490>>>）
- principle·默认凭据与强制改密策略（<<<PAGE 60>>>–<<<PAGE 61>>>）
- principle·ASA 认证服务禁用语义（<<<PAGE 58>>>–<<<PAGE 59>>>）
- principle·WebView 安全默认（<<<PAGE 68>>>–<<<PAGE 69>>>）
- counter·Lightning Config 前禁止接入网络（<<<PAGE 477>>>、<<<PAGE 486>>>）
- counter·R-Lab 重置后端口全禁用（<<<PAGE 89>>>）
