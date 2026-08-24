---
name: client-connection-trouble
description: 何时用：客户端"搜不到/连不上/拿不到 IP/频繁掉线"时，用本 skill 的决策链按序定位根因（含掉线误报判读与 VoWLAN 阈值）。
source_book: DT00XTE478EN Stellar WLAN Advanced Troubleshooting
---

# 客户端连接排障决策链：看不到 · 连不上 · 没地址 · 掉线

## R · 原文引用

> 1) Is the SSID broadcasted by the AP? 2) Which radio does the client support? Compatible with the SSID broadcasted? 3) Country Code of the AP? Supported by the client? Wrong country code: Set manually a compatible channel on the AP in RF profile. (p82)

> 2) Client assigned to the correct VLAN? Client supposed to get an IP in the scope of the VLAN 20? Does the Final_role filter DHCP traffic? (p84)

> 1) AP transmit power is too low? iwlist ath11 txpower - Current Tx-Power=3 dBm (1 mW). Transmit power set to minimum value. wlanconfig ath11 list - RSSI 16... Bad signal quality. High probability of disconnection. Increase AP transmit power in RF profile. (p85-86)

> [MLME] [ieee80211_recv_disassoc] Received Disassoc with reason 8 (OS moved the client to another AP using non-aggressive load balance), recv rssi 63, min rssi 55, max rssi 64. (p80)

## I · 方法论骨架

**决策链总图**

```
症状 → 第一命令 → 分支
搜不到 SSID   → iwconfig          → ① SSID 没广播（BSSID 无 MAC）？② 频段不兼容？③ 国家码不兼容？
关联成功没 IP → 双端抓包 + sta_list → ① DHCP 报文路径丢包？② VLAN 分错？③ Final_role 滤掉 DHCP？
频繁掉线     → iwlist txpower + kes_syslog → ① 功率被压最小？② 踢除阈值过高？③ 被踢 or 失联？④ reason 8 误报？
慢/语音差     → wlanconfig list    → RSSI/SNR 对照 VoWLAN 阈值
```

**核心命令判读表**

| 命令 | 字段 | 判读 |
|---|---|---|
| `ssudo sta_list` | VLANID/IPv4 | 是否落在正确 VLAN/子网 |
| | OnlineTime | 频繁清零=反复掉线 |
| | RX/TX | 全零=关联后不通 |
| | AUTH / Final_role | 认证方式与访问角色是否正确 |
| `ssudo wam_debug sta_list` | JSON | assignedVLAN / macAuthResult / CPAuthResult / redirectURLFromMACAuth——认证到底成没成、角色对不对 |
| `wlanconfig athXX list` | RSSI/MINRSSI/MAXRSSI/SNR | 对照阈值表；HT/VHT 能力 |
| `cat /proc/kes_syslog \| grep <MAC>` | disassoc reason | reason 8=负载均衡搬客户端，非故障 |

**VoWLAN 阈值（Stellar 正值刻度，dBm = RSSI 值 − 96）**

| RSSI 值 | 换算 | 判定 |
|---|---|---|
| 10 | −86dBm | 差，丢包过多，语音/实时应用不可用 |
| 29 | −67dBm | 语音与实时应用推荐下限（802.11ac VoWLAN 硬指标：RSSI≥29 且 SNR≥25） |
| 43 | −53dBm | 完美 |

**拿不到 IP 两分支**：① 客户端 Wireshark + AP tcpdump 双端比对 DHCP 四步——AP 侧收不到 Discover=无线段丢失；AP 有 Discover 而服务器无响应=上游问题。② 报文路径正常则查 sta_list 的 VLANID 是否正确、Final_role 是否把 DHCP 流量过滤（隐蔽根因：角色不含 DHCP 放行 → 永远拿不到地址）。

**掉线四分支**：① `iwlist athXX txpower` 显示最小档（如 3dBm/1mW）+ 客户端 RSSI 16 → RF profile 调大功率。② rfprofile.conf 的 `signalStrengthThreshold` 过高（如 70，约 −26dBm）→ 正常信号也被踢，调低。③ 兜底空口抓包 + 日志看有无 AP 主动 disassoc/deauth，区分"被踢"与"失联"。④ reason 8 = 系统负载均衡行为，不按故障处理。

## A1 · 书中案例

- ce09：Current Tx-Power=3dBm（1mW）+ RSSI 16，日志判读"信号质量差、断连概率高"，在 RF profile 调大功率解决（p85-86）。
- ce10：signalStrengthThreshold:70 → "Threshold too high. Decrease the value."（p87）。
- ce21：reason 8 日志原文带 recv rssi 63 / min 55 / max 64，可复核掉线瞬间信号（p80）。
- `cat /proc/kes_syslog | grep tid` 的 `[TID_DHCP_PROTOCOL] ip/hostname/ostype:[iOS]` 行可识别终端 OS 与主机名（p78）。

## A2 · 触发场景（含与相邻 skill 的区分）

- 用户报"连不上/总掉线/慢"→ 本 skill。
- 症状是 802.1X 认证失败（提示凭证/认证错误）→ `dot1x-radius-trouble`；Captive Portal 不弹页 → `stellar-ap-system-health` 的 eag 部分。
- 掉线原因指向漫游切换（换位置掉线）→ `wireless-rf-roaming-trouble`。
- 客户端侧确认正常、怀疑上游 → `network-side-trouble`。

## E · 可执行步骤

1. 搜不到 SSID：iwconfig 查该 SSID 的 BSSID 是否存在（无 MAC=未广播）→ 核对客户端支持频段 → showsysinfo 查国家码；国家码不匹配时在 RF profile 手动指定双方兼容信道。
2. 连不上先跑 `ssudo sta_list` 六字段核对，再 `wam_debug sta_list` 看认证 JSON。
3. 没地址：双端抓包比对 DHCP 四步 → 正常则查 VLANID 与 Final_role 是否滤 DHCP。
4. 掉线：iwlist txpower → wlanconfig list 看 RSSI → cat /tmp/config/rfprofile.conf 查 signalStrengthThreshold → grep 客户端 MAC 读 disassoc reason（reason 8 直接结案为负载均衡）。
5. 慢/语音差：wlanconfig list 的 RSSI/SNR 对照阈值表，低于 29/25 即覆盖不达标。

## B · 边界与陷阱

- **reason 8 误报**：负载均衡搬客户端是系统行为，别当射频故障修；先 grep reason 再行动。
- Stellar RSSI 是正值刻度，直接当 dBm 读会全错（换算 dBm = RSSI − 96）。
- Final_role 滤掉 DHCP 是最隐蔽的"永远拿不到 IP"根因，报文路径排查正常时必查此项。
- 信号阈值过高（70）时功率再正常也掉线——先查配置再动硬件。
- 802.1X 的客户端侧凭证错误表现与网络故障一模一样，先做四项自查再怀疑网络。

---
来源条目: p16, p17, p18, p19, p20, ce02, ce07, ce08, ce09, ce10, ce21（术语 g01 RSSI, g02 SNR, g03 BSSID, g31 Access Role Profile/Final_role）
