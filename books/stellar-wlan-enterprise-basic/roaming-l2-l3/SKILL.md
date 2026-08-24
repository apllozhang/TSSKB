---
name: roaming-l2-l3
description: 何时用：规划或排障 WLAN 漫游——L2/L3 判定、快速漫游（OKC/802.11r）、RSSI 阈值调优、粘性终端时。
source_book: DT00XTE368EN Stellar WLAN Enterprise Basic
---

# L2 移动性与漫游

## R · 原文引用

> "Client context exists on the new AP? No: No Roaming, new client. Yes: WLAN service and Access Role Profile exist in the Client Context on the new AP? No: No Roaming. Yes: Client Context VLAN ID = VLAN ID mapped to the Access Role Profile on the new AP? Yes: L2 Roaming; No: L3 Roaming." (p412)

> "L2 Roaming always enabled. L3 Roaming disabled by default... OKC can be enabled with WPA2/WPA3 Enterprise only. 802.11r (Fast Roaming) can be enabled with WPA2/WPA3 encryption only." (p407/414)

> "Recommended value for 2.4GHz: RSSI = 10. Recommended value for 5GHz: RSSI = 15... If the RSSI threshold is too low, the client remains on a low signal strength site. If too high, the client roams too much that could result to packet loss." (p424)

> "In some cases, Stellar APs are geographical neighbors but can't see each other (i.e: radio waves blocked by corridor with right angles...). The client context can't be shared. No roaming. Solution: On both AP, add statically the neighbor Stellar AP." (p423)

## I · 方法论骨架

1. **漫游判定树**：新 AP 有 Client Context 且含对应 WLAN Service/Access Role → VLAN 一致走 L2（默认开），不一致走 L3（默认关，GRE 隧道）；上下文缺失=按新客户端重新接入。
2. **Client Context 是原材料**：SSID/VLAN/角色/策略 + 快速漫游密钥缓存（PMKSA、FT R0/R1）随 Add/Del 消息在 AP 间共享。
3. **漫游设计四查**：模式（VLAN 定 L2/L3）→ 覆盖（Heat Map 按频段核重叠）→ 邻居（互不可见则配静态 Neighbor AP）→ 粘性终端（RSSI 阈值 + 802.11k/11v）。
4. **快速漫游约束**：OKC 仅 WPA2/WPA3 Enterprise；802.11r 需 WPA2/WPA3 加密（Personal/Enterprise 均可）；开错组合直接配不上。

## A1 · 书中案例（Lab 精要）

教材配"走到直角走廊必掉线"案例：两台 AP 地理相邻但电波互不可见，客户端上下文无法共享、漫游不发生——在两台 AP 上互配静态 Neighbor AP 后上下文改走 LAN 共享，漫游恢复。背景扫描冲突案例：漫游到正在做背景扫描的 AP 时实时业务被打断（语音除外，AP 语音感知会暂停扫描），解法为关背景扫描或加装专用扫描 AP。

## A2 · 触发场景（含与相邻 skill 的区分）

- "移动中掉线""固定区域必断""终端粘弱信号 AP""频繁切换丢包"——用本 skill。
- 覆盖本身有空洞（不走动也差）——先回 site-survey-ekahau 三步法；L3 漫游/隧道涉及分支回传——与 rap-remote-deployment 的 GRE 条目区分（L3 漫游隧道在 home/foreign AP 之间，RAP 隧道在 AP 与总部 VPN Server 之间）。

## E · 可执行步骤

1. 确认漫游模式：按 home/foreign AP 的 VLAN 映射选 L2（默认）或 L3（Advanced WLAN Service 开启）。
2. 核安全级别与快速漫游组合：Enterprise SSID 开 OKC；WPA2/WPA3 加密 SSID 可开 802.11r（按 SSID）。
3. 用 OV2500 Heat Map 按 2.4/5/6 GHz 分别确认 AP 间信号重叠——无重叠无漫游。
4. 怀疑互不可见：两台 AP 上互配静态 Neighbor AP（两边都要配）。
5. 治理粘性终端：RF Profile 设 Roaming RSSI Threshold（起点 2.4G=10、5G=15，范围 0-100），配合 802.11k/11v 引导。
6. 高实时业务网络设计期决策：关背景扫描或部署专用扫描 AP。

## B · 边界与陷阱

- RSSI 阈值双向失败：太低=粘弱信号不切换；太高=频繁切换丢包。症状对号："信号差不断线"查偏低，"频繁掉线"查偏高。
- 漫游决定权在终端，网络侧只能引导（11k/11v + 阈值）。
- L3 漫游默认关闭，忘了开会出现跨 VLAN 移动按新客户端处理（IP 变、会话断）。
- Express 模式漫游仅限同集群内 L2。
- 背景扫描只对语音豁免，视频会议/流媒体会被打断。

---
来源条目: f13, f14, p31, p32, ce11, ce12, ce13, g39, g40, g41
