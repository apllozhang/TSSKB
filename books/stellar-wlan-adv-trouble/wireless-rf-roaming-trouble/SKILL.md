---
name: wireless-rf-roaming-trouble
description: 何时用：SSID/RF 配置没生效、热图异常、客户端漫游失败或邻居 AP 看不见时，用本 skill 核对无线接口、RF profile 落地与邻居表。
source_book: DT00XTE478EN Stellar WLAN Advanced Troubleshooting
---

# 无线层与漫游排障：接口 · RF profile · 邻居 · 漫游验证

## R · 原文引用

> Check List: SSID broadcasted on the selected radio(s)? Transmission Power as selected in the RF profile? Encryption activated? BSSID is present? If there is no MAC address for "Access Point", the SSID is not broadcasted. athXYY: X = 0: 2.4GHz Radio, X = 1: 5GHz Radio, X = 2: 6GHz Radio, Y = [1...16]: SSID ID. (p63)

> Reasons for roaming failure: APs must be seen as neighbors. No Roaming from an untagged VLAN to a tagged VLAN. RSSI too low between source AP and destination AP. (p69)

> In some cases, Stellar APs are geographical neighbors but can't see each other (i.e: radio waves blocked by corridor with right angles,...). Solution: On both AP, add statically the neighbor Stellar AP from the list of known AP. The client context can be shared through the LAN and the client can roam. (p70)

> adme show - mac, ip, ov_ip, state, name, version, radiocnt, radioid, channel, rssi, txpower. If a geographic neighbor: Is not seen, move it closer or increase it's transmission power. Is seen with a weak power signal (RSSI), move it or increase it's transmission power. RSSI < 20 is considered bad signal. (p69, p96)

## I · 方法论骨架

**无线接口核对（iwconfig + athXYY 命名）**

接口名自带语义：athXYY 中 X=频段（0=2.4GHz、1=5GHz、2=6GHz），YY=SSID 编号 1-16（ath001=2.4GHz 的 1 号 SSID，ath102=5GHz 的 2 号 SSID）。核对四项：SSID 是否在选定射频广播、发射功率是否等于 RF profile 值、加密是否开启、**BSSID 是否存在——Access Point 栏无 MAC 地址 = 该 SSID 根本没广播**。

**RF profile 落地核对**（`cat /tmp/config/rfprofile.conf`，与网管侧配置逐项比对）

- 全局项：bandSteering、LoadBalance、scanning、countryCode、Air Time Fairness
- 每射频项：信道 AUTO/手动、channelWidth（如 20）、powerSetting、signalStrengthThreshold、roamingSignalStrengthThreshold
- 实际信道与功率验证：`iwlist athXXX channel`（当前信道）+ `iwlist athXXX txpower`（档位 0/5/7/9/11/13/15/17dBm 及当前值）

**邻居表判读**（`adme show`，radioid 0=2.4G、1=5G 分频段评估）

- 同 OmniVista/同集群管理的 AP 应出现在表里。
- 地理邻居**看不到**或 **RSSI < 20**（差信号）→ 漫游病灶。处置二选一：挪近 AP 或调大其发射功率。（参考：RSSI 79=极好近邻，15=差。）

**漫游失败三根因**：① 源/目标 AP 互不为邻居；② 两 AP 间 RSSI 过低；③ **untagged VLAN 与 tagged VLAN 之间不漫游**（产品限制，保证同 SSID 各 AP 的 VLAN 封装一致）。

**漫游成功验证**：AP 日志收集包 wam.log 搜 `L3 roaming-start` / `L3 roaming-success` / `L2 roaming-success`——只有 start 无 success=漫游发起后失败；都搜不到=漫游根本没触发（回查邻居/信号/VLAN）。

## A1 · 书中案例

- 直角走廊阻挡（p70）：两台 AP 地理相邻但射频互相看不见，客户端上下文无法空口共享 → 漫游失败。解法：两台 AP 对称静态添加对方为已知邻居（Device Catalog > Action > View > Neighbor APs > Manage neighbor），上下文改走 LAN 传递。
- 热图生成不了（p67-68）：OmniVista 无 2.4GHz 热图，根因是 WLAN 配置只建在 5GHz 射频——无 SSID 即无接口即无热图，先 iwconfig 确认接口存在。

## A2 · 触发场景（含与相邻 skill 的区分）

- 症状是"换位置/走动时掉线、漫游不衔接"→ 本 skill；静止状态掉线 → `client-connection-trouble`（功率/阈值/reason 8）。
- 症状是"SSID 没广播出来/RF 配置疑似没下发"→ 本 skill；客户端搜不到但别人正常（国家码问题）→ `client-connection-trouble`。
- 大范围覆盖差/干扰问题需要勘测与整改 → `site-survey-remediation`；本 skill 只管单点配置与邻居关系。

## E · 可执行步骤

1. iwconfig 列接口，按 athXYY 解码频段与 SSID，核对四项清单（重点 BSSID 有无 MAC）。
2. `cat /tmp/config/rfprofile.conf` 与网管配置逐项比对（全局五项 + 每射频五项）。
3. `iwlist athXXX channel` / `iwlist athXXX txpower` 确认实际信道与功率档位。
4. `adme show` 查邻居表：地理邻居缺失或 RSSI<20 → 挪近或加大功率；射频被建筑结构阻挡 → 双侧对称静态添加邻居。
5. 核对同 SSID 各 AP 的 VLAN 封装方式一致（tagged/untagged 不混用）。
6. wam.log 搜三类漫游关键字定性：有 start 无 success / 完全没有 / success。

## B · 边界与陷阱

- **untagged↔tagged 不漫游是产品限制**，信号再好也漫不过去，配置一致性是前置。
- BSSID 缺失（Access Point 栏无 MAC）= SSID 未广播，先解决广播再谈其他。
- 静态添加邻居必须**两台 AP 对称互加**，只加一边不生效。
- 热图缺失先查该频段有没有 WLAN 配置/接口，别先怪 OmniVista。
- 邻居 RSSI<20 的阈值判据按频段分别看（radioid 0 与 1），2.4G 好 5G 差是常态。

---
来源条目: p13, p14, p15, p23, ce03, ce04, ce05, ce06, ce24（术语 g04 athXYY, g06 Band Steering, g19 adme, g26 Heat Map, g27 L2/L3 Roaming）
