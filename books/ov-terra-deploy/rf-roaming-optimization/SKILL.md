---
name: 射频与漫游优化
description: 当需要调优 RF Profile（负载均衡/扫描/信道）、排查漫游问题（L2/L3、Fast Roaming、Sticky Client）、部署 WIPS，或配置 Mesh/Bridge/RAP 无线回程时使用。
source_book: DT00XTE317 OmniVista Cirrus/Terra Deployment and Configuration
---

## R（触发场景）
- 客户抱怨 Wi-Fi 信号好但体验差（漫游丢包、粘滞客户端）
- 需要 WIPS 入侵防护或 Rogue AP 反制
- 两地不便布线，需要 Mesh/Bridge 回程，或部署远程 AP（RAP）

## I（核心理念）
Stellar 射频管理是全分布式的（DRM）：每个 AP 空口发现邻居、LAN 上共享 RF 上下文、自主做射频决策，不依赖 AP Group 或管理 VLAN。漫游分 L2/L3，判定依据是 home/foreign AP 间的客户端 VLAN 是否一致，L3 漫游靠 L2 GRE 隧道。优化工作的核心抓手是 RF Profile 参数（Band Steering、DLB、扫描、Roaming RSSI 阈值）与 802.11k/v 引导。

## A1（行动框架）
1. **RF Profile 配置**（应用于 AP Group 或 AP 级）：国家码、Smart Load Balance、扫描、信道/功率设置（<<<PAGE 366>>><<<PAGE 367>>>）。
2. **负载均衡**：
   - Band Steering：引导客户端到 5G/6GHz，推荐 RSSI 门限 2.4G=5、5G=10（<<<PAGE 370>>>）
   - Dynamic Load Balance：信道平均介质利用率 1 分钟超 70% 判为 Overloaded；相邻 AP 各自基于负载设 timer，新客户端被引导至最轻负载 AP（<<<PAGE 371>>><<<PAGE 372>>>）
3. **背景扫描**：默认间隔 20s（范围 5-10800s）、时长 50ms（范围 50-110ms）；WIPS 必需扫描；支持 Dedicated AP scanning mode 与 Voice/Video Awareness（检测 SIP/H.323 绕过扫描）（<<<PAGE 373>>>）。
4. **漫游优化**：
   - Sticky Client Avoidance：802.11v（BSS Transition Management）+ 802.11k + Roaming RSSI 阈值；推荐 2.4GHz RSSI=10、5GHz RSSI=15（<<<PAGE 404>>><<<PAGE 416>>>）
   - RSSI 对照：OV 上是平均值、AP 上是瞬时值；RSSI 10≈-86dBm（Bad）… 25≈-71dBm（Desired and recommended）；AP CLI `wlanconfig ath002 list`，-24dBm=72 RSSI（<<<PAGE 378>>><<<PAGE 379>>>）
5. **WIPS**：分类 Interfering（任何空口发现的其他 AP）/ Rogue（按 Rogue AP Policy 判定）/ Friendly；Rogue AP Containment 默认启用，向 Rogue AP 的客户端发 de-auth；Rogue 判定策略含 Signal Strength Threshold（默认 -70dBm，范围 -50~-90）、Detect Valid SSID、Rogue SSID Keyword、Rogue OUI（<<<PAGE 384>>><<<PAGE 385>>>）。
6. **Mesh/Bridge 配置**：Device Catalog 选 AP → Actions > Edit Device > Mesh/Bridge Configuration；Mesh 监控显示拓扑、Root 角色与 Repeater 的 Parent Address（Root AP 的 MAC）（<<<PAGE 442>>><<<PAGE 443>>><<<PAGE 444>>>）。

## A2（进阶应用）
- **漫游判定**：L2 或 L3 按客户端在 home/foreign AP 间 VLAN 选择：无上下文→新客户端；上下文 + WLAN/ARP 匹配 + VLAN 匹配→L2；VLAN 不匹配→L3（基于 L2 GRE 隧道）。L2 漫游始终启用，L3 默认禁用（<<<PAGE 394>>><<<PAGE 400>>>）。
- **客户端上下文共享**：客户端关联时 AP 向所有空口相邻 AP 发 Add 消息，漫游时旧 AP 收到新 AP 的 Add 后触发 Del；上下文含 VLAN ID/ARP/Policy List/PMKSA cache；与 AP Group、管理 VLAN 无关（<<<PAGE 397>>><<<PAGE 399>>>）。
- **Mesh 拓扑限制**：最多 8 台 slave AP、4 跳、单跳最多 5 AP、全网最多 16 AP；所有 AP 可广播最多 5 个 SSID；最佳实践 BAND 5GHz、CHANNEL >100（<<<PAGE 439>>>）。Auto Mesh：LAN 上的 root AP 广播隐藏 SSID "Stellar-MESH"（5GHz），未连 LAN 的 AP 自动以 non-root 加入（<<<PAGE 440>>>）。
- **RAP（远程 AP）五步开通**：[PRE] 管理员预录入（OV Cirrus：序列号/RAP 模式/VPN Server 公网 IP/OV2500 IP/VPN Client IP；VPN Server：公网/私网 IP/密钥；OV2500：AP 设置）→ ① AP 启动按序列号注册 → ② OV Cirrus 下发 VPN 与 OV2500 参数 → ③ 建管理流量 VPN 隧道 → ④ 从 OV2500 取配置（SSID/射频）→ ⑤ 第二条 VPN（客户端流量）+ 客户端接入。配置三块：配 OV Cirrus、部署 ALE VPN Server VM（eth0 公网/eth1 私网，导入 VPN 设置）、配 OV2500（<<<PAGE 423>>>~<<<PAGE 429>>><<<PAGE 432>>>）。
- **Smart Air Share**：SSID 级最低速率控制，2.4G 建议 12、5G/6G 建议 24，提升 802.11a/n 客户端体验（<<<PAGE 369>>>）。

## E（实证案例）
- **案例 1**：走廊直角墙阻挡，两台地理相邻的 AP 互相看不见，客户端上下文无法共享、无法漫游——在 AP Registration > Access Point 视图给两台 AP 手工互加 Neighbor AP（两端都要加）后恢复（<<<PAGE 415>>>）。
- **案例 2**：Roaming RSSI 阈值设太低，客户端滞留在弱信号 AP；设太高则频繁漫游丢包——按推荐值（2.4G=10、5G=15）回调（<<<PAGE 416>>>）。
- **案例 3**：仓库不便布线，用 Mesh 回程：root AP 广播 Stellar-MESH 隐藏 SSID，其余 AP 自动入网，全网 16 AP 内、4 跳内规划（<<<PAGE 439>>><<<PAGE 440>>>）。

## B（边界与陷阱）
- **Fast Roaming 加密限制**：OKC（802.11k）仅 WPA2/WPA3 Enterprise；802.11r 仅 WPA2/WPA3 加密（Personal 或 Enterprise）；未启用 Fast Roaming 则走标准漫游（<<<PAGE 395>>><<<PAGE 402>>>）。
- **WIPS Client Blocklist 局限**：默认禁用；攻击者源 MAC 可以是 AP MAC/BSSID/网卡 MAC，拉黑仅当源 MAC 是真实无线客户端时才有意义（<<<PAGE 387>>>）。
- **扫描的安全/性能权衡**：扫描期间无线客户端无 802.11 数据；扫描间隔更高或时长更低→入侵更难检出但客户端性能更好（<<<PAGE 373>>><<<PAGE 376>>>）。
- **RSSI Bad 区间**：不建议跑音视频应用（<<<PAGE 379>>>）。
- **Bridge 模式 VLAN tagging 兼容性**：AP1101、AP1201、AP1201H 不兼容 Bridge 上的 VLAN tagging（<<<PAGE 437>>>）。
- **AP1101 不支持 RAP**（<<<PAGE 421>>>）。

## 来源
- principles·DRM 分布式射频管理架构（<<<PAGE 364>>><<<PAGE 365>>>）
- principles·Smart Load Balance（<<<PAGE 370>>><<<PAGE 371>>><<<PAGE 372>>>）
- principles·背景扫描机制与参数（<<<PAGE 373>>>）
- principles·RSSI 定义与数值对照（<<<PAGE 378>>><<<PAGE 379>>>）
- principles·WIPS 分类 Interfering/Rogue/Friendly（<<<PAGE 384>>><<<PAGE 385>>>）
- principles·漫游判定条件 L2/L3（<<<PAGE 400>>><<<PAGE 394>>>）
- principles·客户端上下文共享机制（<<<PAGE 397>>><<<PAGE 399>>>）
- principles·Fast Roaming 条件限制（<<<PAGE 395>>><<<PAGE 402>>>）
- principles·Sticky Client Avoidance 与 Roaming RSSI 阈值（<<<PAGE 404>>><<<PAGE 416>>>）
- principles·Mesh 拓扑限制（<<<PAGE 439>>>）
- principles·Auto Mesh 机制（<<<PAGE 440>>>）
- frameworks·RAP 远程 AP 五步开通序列（<<<PAGE 423>>>~<<<PAGE 432>>>）
- cases·Mesh/Bridge 配置操作路径（<<<PAGE 442>>><<<PAGE 443>>><<<PAGE 444>>>）
- counter-examples·地理相邻互相看不见的 AP（<<<PAGE 415>>>）
- counter-examples·Roaming RSSI 阈值设错的两类后果（<<<PAGE 416>>>）
- counter-examples·Fast Roaming / OKC 加密限制（<<<PAGE 395>>><<<PAGE 402>>>）
- counter-examples·WIPS Client Blocklist 局限（<<<PAGE 387>>>）
- counter-examples·扫描参数安全/性能权衡（<<<PAGE 373>>><<<PAGE 376>>>）
- counter-examples·RSSI Bad 区间不建议音视频（<<<PAGE 379>>>）
- counter-examples·Bridge 模式 VLAN tagging 兼容性（<<<PAGE 437>>>）
