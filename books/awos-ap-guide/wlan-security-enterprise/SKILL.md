---
name: wlan-security-enterprise
description: 何时用：配 WLAN 安全等级、PSK/802.1X/RadSec、WPA3/CNSA 选型、动态 VLAN、HTTPS 证书或 ACL 时。
source_book: AWOS 5.0.3 Stellar AP User Guide
---

# WLAN 安全与高级认证

## R · 原文引用

> Enterprise: Also referred to as 802.1X mode ... requires a RADIUS authentication server. Personal: Also referred to as PSK (pre-shared key) mode ... This key may be entered either as a string of 64 hexadecimal digits, or as a passphrase of 8 to 63 printable ASCII characters. (p59)

> AuthPort - Communication port of the authentication server. The default value is 1812. If RadSec is enabled, the AuthPort should be configured 2083 or the value mapping RadSec server. ... AcctPort - ... The default value is 1813. (p62-63)

> AP1101 full band does not support WPA3 CNSA encryption, AP1201H and AP1201L 2.4Ghz band does not support WPA3 CSNA encryption. ... When CSNA encryption is applied to an AP that does not support it, the encryption will automatically fall back to non-CSNA mode (WPA2). (p62)

## I · 方法论骨架

安全选型阶梯：**Open（+Enhanced Open）→ Personal/PSK → Enterprise(802.1X) → WPA3-Enterprise CNSA**，逐级核对机型能力与端口/属性细节。

1. 先定安全等级，再按机型清单核对加密能力（CNSA 有静默回退）。
2. Enterprise 模式下配 RADIUS：端口默认 1812/1813，RadSec 改 2083；动态 VLAN 用 RFC-2868 三属性。
3. 管理面安全：HTTPS + 固定域名证书；ACL 顺序匹配、默认放行。

## A1 · 书中案例

- 酒店类开放网络：Open + Captive Portal，或升级 Enhanced Open（OWE）防嗅探；Transition 模式同时广播传统 Open SSID 与 Enhanced Open SSID。
- 高安全政务/金融：WPA3-Enterprise + CNSA（Suite B 192 位），PMF 自动强制 Required——但 AP1101 全频段、AP1201H/L 的 2.4G 不支持。
- 老客户端兜底：Static-WEP 仅用于 802.11b 老终端，最多 4 个 WEP 密钥（每个 10 或 26 位十六进制）。

## A2 · 触发场景（含与相邻 skill 的区分）

- 触发：建/改 WLAN 的安全等级；对接 RADIUS；RadSec 部署；6GHz 网络加密选型；替换 HTTPS 证书；业务访问控制（ACL）。
- 区分：Portal 页面/用户库/白名单容量 → `ssid-radio-tuning`；开局改密与账户体系 → `cluster-bootstrap-pvm`。本文管"加密与认证协议"，那边管"页面与容量"。

## E · 可执行步骤

1. 选安全等级：Enterprise（802.1X，需 RADIUS）> Personal（PSK：64 位十六进制或 8-63 个可打印 ASCII）> Open。
2. 配 PSK：按格式输入口令；256 位密钥自动派生。
3. 配 RADIUS：AuthPort 默认 1812、AcctPort 默认 1813；启用 RadSec 后 AuthPort 改 2083。注意 RadSec 仅适用于无线客户端、只支持主 RADIUS 服务器。
4. 动态 VLAN：在 RADIUS 侧下发三属性——Tunnel-Type (#64)=VLAN、Tunnel-Medium-Type (#65)=802(6)、Tunnel-Private-Group-ID (#81)。
5. WPA3/CNSA：先核对机型支持清单；WPA3 Enterprise 选 CNSA 时 PMF 强制 Required（仅支持 PMF 的客户端可接入）。6GHz 只允许 WPA3 与 Enhanced Open。
6. HTTPS 管理：HTTP 用 http://AP-IP:8080 免证书；HTTPS 用 https://AP-IP（443），先下载根证书 ALE-OmniAccess-WLAN.CRT 装入浏览器信任库；自定义证书必须用域名 mywifi.al-enterprise.com（登录 URL 不可改）。
7. ACL：规则自上而下顺序匹配，无命中默认 Accept（放行）；L3 ACL 支持源/目的 IP + TCP/UDP/ICMP 端口 + 通配符；Apply To EthPort 仅适用 AP1201H/AP1201HL/AP1311/AP1301H 下行口。L2 级 MAC 控制走 Blocklist/Allowlist，802.1p/DSCP 规则在 SSID 的 QoS 里配。
8. wIDS/wIPS 加固（可选）：AP allowlist 信任名单、blocklist（仅 rogue 可入）、Suppress 发 DEAUTH（默认关闭）、Dynamic blocklist 自动拉黑 ad-hoc（默认关闭）。

## B · 边界与陷阱

- **CNSA 静默回退 WPA2**：不支持机型配置后无报错直接降级——高安全场景必须逐机型核对。
- **RadSec 限制**：仅无线客户端、仅主 RADIUS 服务器，不支持 secondary。
- **证书域名固定**：mywifi.al-enterprise.com 不可改，自定义证书 CN 必须匹配。
- **RADIUS Called-Station-ID 属性最长 64 字节**。
- **漫游快速化依赖**：OKC 快速漫游复用缓存 PMK；MLO（Wi-Fi 7 多链路）依赖射频开启 + EHT 启用，客户端 MAC 栏显示 MLD 地址（附着频段按 6G>5G>2.4G 优先显示）。
- 关闭 High Efficiency → HE 机型降级 VHT；关闭 EHT → EHT 机型降级 HE。

---
来源条目: p16, p17, p26, p28, ce09, g14, g15, g18, g19, g20, g21, g22, g23, g30
