---
name: stellar-ssid-advanced
description: 何时用：配置 SSID 的高级选项——QoS/WMM 映射、密钥轮换、广播组播优化、访客门户与公共 Wi-Fi 时用。
source_book: DT00XTE361EN Stellar WLAN Advanced Deployment
---

# WLAN 高级选项：QoS、密钥轮换、广播优化与访客门户

## R · 原文引用

> "Recommended Settings: Best Effort 0/0; Background 2/18-AF21; Voice 5/46-EF; Video 4/34-AF41." (p81)

> "Rotate the keys periodically to avoid key cracking. Default period: 15 min – Range 1 min – 24 hours." (p78)

> "Upper limit of multicast optimization: Multicast Based Channel Utilization: default value 90%; Number of Clients: default value 6." (p79)

> "Networks with WiFi4EU SSID use an HTTPS Captive Portal. Session timeout should be configurable up to 12 hours." (p82)

## I · 方法论骨架

SSID 高级选项四组参数：
1. **QoS（WMM/DSCP/802.1p）**：WMM 四队列推荐映射——Voice 5/46(EF)、Video 4/34(AF41)、Best Effort 0/0、Background 2/18(AF21)；上下行可分别标记（示例上行：Voice 46、Video 32、BE 0、BG 8）。
2. **安全**：GTK/广播密钥周期轮换防破解（默认 15 分钟，1 分钟-24 小时，仅 Enterprise SSID）；客户端隔离（同 AP 同 SSID 内互访阻断，访客常用）。
3. **广播/组播优化**：Broadcast Filter All（除 DHCP/ARP 全丢）/ Broadcast Filter ARP（广播 ARP 转单播）；组播优化把组播转单播（PTK 加密、更高速率），但有两个自动停用上限——组播信道利用率 90%、高吞吐客户端数 6。
4. **访客与公众 Wi-Fi**：OV-UPAM Captive Portal + Guest Access Strategy + 门户模板；Walled Garden 白名单（认证前可访问域名）；社交登录（Facebook WiFi/Google）；WiFi4EU SSID 必须 HTTPS 门户、会话超时可配至 12 小时；Hotspot 2.0（Passpoint，基于 802.11u 与 EAP-SIM/AKA）。SSID 级带宽契约（Bandwidth Contract）与按用户的 Bandwidth Control 区分。
另：访客流量可选隧道集中出口——SSID 的 VLAN/Tunnel Mapping 选 Tunnel（Tunnel ID + TTS IP），由远端 OS6860-GTTS 终结。

## A1 · 书中案例（Lab 精要）

基础 Lab（p70-71）配 GuestsX：SSID 选 OV-UPAM Captive Portal 类型，绑 Guest Access Strategy 与门户模板，VLAN 30；树莓派验证 Guest 拿 192.168.30.70-79。综合演练（p293-295）进阶用法：GuestsX 内部门户+限 1Mbit/s+封 SSH/Telnet+客户端隔离+周一至周三调度+账号限时限量；打印机 SSID 用 WPA2 PSK + 按设备 PSK（DPSK，按 MAC 各配专属 passphrase）。

## A2 · 触发场景（含与相邻 skill 的区分）

- SSID 骨架（加密、VLAN、调度）已会配，要调优 QoS 标记、组播行为、访客体验 → 本 skill。
- 从零搭建整套多 SSID 交付 → stellar-deployment-checklist。
- 门户打不开/访客认证失败排障（先查 IP 再查门户）→ stellar-troubleshooting-cli。
- 语音 SSID 的专门规划（36Mbps/用户、802.11r/k/v）→ stellar-vowlan。

## E · 可执行步骤

1. QoS：在 SSID 高级选项按推荐表配 WMM→802.1p/DSCP 映射（Voice 5/46、Video 4/34、BE 0/0、BG 2/18），上下行分开标。
2. 安全：Enterprise SSID 开广播密钥轮换（默认 15 分钟即可）；访客 SSID 开客户端隔离。
3. 优化：按需开 Broadcast Filter ARP/All；开组播优化前记住 90%/6 两个自动停用上限，避免误判"优化失效"。
4. 访客：Guest SSID > Guest Access Strategy 选 OV-UPAM 门户，配门户模板、Walled Garden、会话时长与带宽限制；需要社交登录则启用对应选项。
5. 公共场馆：WiFi4EU SSID 用 HTTPS 门户且超时可配至 12 小时；无缝公众漫游考虑 Hotspot 2.0。
6. 限速：区分 SSID 级 Bandwidth Contract（整射频共享）与按用户 Bandwidth Control。
7. 访客集中出口：需要统一审计/出口时把 SSID 映射从 VLAN 改为 Tunnel（Tunnel ID + TTS IP）。

## B · 边界与陷阱

- 组播优化"突然失效"多为自动停用（信道利用率达 90% 或 6 个高吞吐客户端），是设计行为而非故障。
- 密钥轮换仅 Enterprise 类型 SSID 可用，PSK SSID 没有。
- WiFi4EU 的 12 小时超时是合规硬要求，只给 4 小时会不达标。
- Guest Tunnel（TTS/GTTT）附录原文（p320-322）字体编码损坏，隧道终结侧细节以可读片段整理，落地前待对照原版 PDF 确认。

---
来源条目: p05, p06, p07, p08, g13, g14, g15, g16, g17, g18, g19, g20, g21, g22, g23, g24, g50, g60
