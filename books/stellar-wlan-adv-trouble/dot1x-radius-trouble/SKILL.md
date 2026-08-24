---
name: dot1x-radius-trouble
description: 何时用：802.1X/Enterprise SSID 认证失败（凭证对却连不上、认证超时）时，用本 skill 按客户端→AP→RADIUS 三段顺序核对。
source_book: DT00XTE478EN Stellar WLAN Advanced Troubleshooting
---

# 802.1X 认证失败三段排查法

## R · 原文引用

> 1) On Client side: Check Username and password, Encryption type, Security type/key, Certificate on client (if any). (p88)

> 2) On AP side: Correct Radius server attached to the SSID? Compare Radius configuration to Radius server: IP and ports, Shared Secret key. (p89)

> 3) On Radius server side: Compare Radius configuration and database to client and AP configuration: Username/password, Shared Secret, Radius client IP, Radius station IP (IP address of the Stellar AP), Certificate, Radius service enabled? Firewall allows authentication and accounts ports? (p90)

> cat /var/config/AAA_server.conf - "accountingPort":1813, "retries":2, "ipAddress":"10.130.5.250", "type":"Radius", "timeout":5, "authenticationPort":1812, "secret":"...". cat /var/config/wlanservice.conf - "securityLevel":"Enterprise", "encryptionType":"wpa2-aes", "aaaProfile":"employee0". (p89)

## I · 方法论骨架

**三段顺序（链路上三个可断点，任何一环不匹配都表现为"连不上"）**

```
① 客户端侧（四查）→ ② AP 侧（两查）→ ③ RADIUS 服务器侧（七查）
```

**① 客户端四查**：用户名密码 / 加密类型 / 安全类型与密钥 / 客户端证书（如部署）。任何一处与 SSID 配置不符都在 EAP 早期失败，表现与"网络故障"一样——先排除低级错误再往下游走。

**② AP 侧两查**：
- SSID 是否绑定了正确的 RADIUS 服务器。三份配置文件的绑定链：
  `wlanservice.conf`（securityLevel=Enterprise、encryptionType=wpa2-aes、aaaProfile=employee0）→ `AAA_profile.conf`（primaryServer）→ `AAA_server.conf`（IP、authPort 1812、acctPort 1813、secret、timeout 5、retries 2）。
- AP 上的参数（IP/端口/共享密钥）与 RADIUS 服务器实际配置一致。**共享密钥不匹配是最常见的静默失败**——两边都"配了"，就是对不上。

**③ 服务器侧七查**：用户数据库中的用户名密码 / 共享密钥 / RADIUS client IP / **RADIUS station IP（=Stellar AP 的地址，必须被登记为合法客户端）** / 证书 / 认证与计费端口 / RADIUS 服务已启用且防火墙放行 1812/1813。

## A1 · 书中案例

教材主用例即按此三段展开（p88-90）：客户端侧先排除凭证/证书问题；AP 侧 cat 三份 AAA 配置文件核对绑定链与默认值（1812/1813、timeout 5、retries 2）；服务器侧逐项比对——AP 的地址若未登记为合法 RADIUS 客户端，请求被直接丢弃，客户端侧只能看到超时。

## A2 · 触发场景（含与相邻 skill 的区分）

- Enterprise/802.1X SSID 认证失败、凭证确认无误仍连不上、认证请求"石沉大海"超时 → 本 skill。
- 与 `client-connection-trouble` 的区分：那边处理关联层与 IP 层（sta_list、DHCP、掉线）；本 skill 只管 EAP/RADIUS 认证链。判断方法：sta_list 的 AUTH 字段确认走了 802.1X、wam_debug 认证结果失败 → 进本 skill。
- 与 `stellar-ap-system-health` 门户部分的区分：Captive Portal（eag）认证用那边；802.1X/ MAC 认证失败用本 skill。

## E · 可执行步骤

1. 客户端四查：核对录入的用户名密码、加密类型、安全类型/密钥、证书。
2. AP 侧：依次 `cat /var/config/wlanservice.conf`、`/var/config/AAA_profile.conf`、`/var/config/AAA_server.conf`，确认 SSID → profile → server 绑定链正确、端口 1812/1813、secret 与服务器一致。
3. 服务器侧按七查清单逐项比对，重点是 Radius station IP 必须包含这台 AP 的地址、防火墙放行认证与计费端口、RADIUS 服务状态。
4. 仍失败：AP 上 `ssudo tcpdump -i br-wan port 1812 or port 1813` 看请求是否发出、有无响应（配合 stellar-ap-toolbox）。

## B · 边界与陷阱

- 共享密钥不匹配是静默失败：不报错、只见超时，核对时逐字符比。
- Radius station IP 要填 **Stellar AP 的地址**，不是客户端或 OmniVista 的地址——教材单独强调的核对点。
- 顺序纪律：先客户端低级错误、再 AP、最后服务器；跳段排查容易把客户端配错当成服务器故障。
- 防火墙只放行认证端口不放行计费端口（1813）也会造成部分功能异常，两端口都要查。

---
来源条目: f09, ce11, ce12, ce13, p21（术语 g20 RADIUS/AAA, g21 802.1X/EAP）
