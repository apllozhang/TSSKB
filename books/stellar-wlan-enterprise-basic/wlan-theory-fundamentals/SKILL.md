---
name: wlan-theory-fundamentals
description: 何时用：需要解释 802.11 标准演进、WiFi 6/7 关键技术、天线选型或无线安全协议原理时（培训与售前讲解）。
source_book: DT00XTE368EN Stellar WLAN Enterprise Basic
---

# 无线理论基础（802.11 / 天线 / 安全原理）

## R · 原文引用

> "BSS (Basic Service Set): Set formed by the access point (AP) and the equipment located in its coverage area. BSSID: an identifier of 6 bytes (Access Point MAC@). ESS: One or more interconnected basic service sets (BSS) and their associated LANs. ESSID, also called SSID, represents the name of the ESS network (32 characters)." (p10-11)

> "OFDMA DL/UL: Enables an 802.11ax access point to simultaneously communicate with multiple devices by dividing each WiFi channel into smaller sub-channels known as Resource Units (RU)... MU-MIMO: 802.11ax devices will use beamforming techniques to direct packets simultaneously to spatially diverse users. WiFi 5: 4x4, Downlink only. WiFi 6: 8x8, Uplink/Downlink." (p31-32)

> "OMNIDIRECTIONAL: RF Signal > Equal in all directions; Point to Multipoint; Short Distance (Dipole). SEMI-DIRECTIONAL: Patch/Panel, Yagi. HIGHLY-DIRECTIONAL: Grid; Long Distance." (p49-53)

> "WEP... TOO WEAK. NEVER USE WEP ON SITE. 128 Bits Mode -> TOO WEAK." (p63)

## I · 方法论骨架

1. **标准演进主线**：802.11 基线（1997）→ b/a/g/n/ac/ax/be；与 ALE 产品对应（AP1301-1360=WiFi 6，AP1411/1431/1451=6E，AP1511/1521=WiFi 7）。
2. **WiFi 6/7 技术分工**：MU-MIMO 管大包高带宽（容量），OFDMA 管小包低时延（效率）；QAM 密度决定速率（256→1024→4096）；BSS Coloring/TWT/MRU/MLO 逐代叠加。
3. **天线三分类**：全向（内置默认，点对多点短距）/ 半定向（Patch/Yagi，点对点中短距）/ 高定向（Grid，长距）。
4. **安全演进链**：WEP（禁用）→ WPA/TKIP（过渡）→ WPA2/AES-CCMP（当代最低线）→ WPA3（SAE + 可选 CNSA 192 位）；认证信任梯：Open+门户 < MAC < PSK < 802.1X。
5. **监管红线**：6 GHz 室外需 AFC（FCC 域 36 dBm，EU 禁标准功率室外，LPI 23 dBm / VLP 14 dBm）；换天线必须复核 EIRP。

## A1 · 书中案例（Lab 精要）

教材 Lab 用 WPA3_AES + 802.1X（PEAP/MSCHAPv2）构建员工 SSID（p305 起），体现理论链的落地形态：Enterprise 认证 + AES 加密 + 内置 UPAM RADIUS。WPA3 CNSA 选项开启后仅 WPA3 终端可入，AP1101 唯一不支持 CNSA。

## A2 · 触发场景（含与相邻 skill 的区分）

- 讲解/答疑"WiFi 6 比 5 强在哪""为什么 6 GHz 更可靠""WPA3 改了什么"——用本 skill。
- 只涉及勘测选型/画墙——转 site-survey-ekahau；只涉及 OV2500 配置——转对应配置类 skill。
- 现场残留 WEP 老设备（打印机/扫描仪）：迁移到 MAC 认证过渡或直接换 WPA2/WPA3。

## E · 可执行步骤

1. 判断终端/业务类型：大包高带宽看 MU-MIMO，小包低时延（IoT/语音）看 OFDMA/TWT。
2. 选天线：室内覆盖用内置全向；走廊覆盖用半定向；楼宇间桥接用高定向；选型后核对法定 EIRP。
3. 选安全级别：员工=802.1X+WPA3；访客=门户；哑终端=MAC；遗留 WEP 立即迁移。
4. 部署 6E 室外前核对本地区功率等级（FCC AFC / EU LPI/VLP）。
5. 排障速率问题时按"SNR→QAM 回落"链解释：距离远/干扰强自动降调制阶数。

## B · 边界与陷阱

- WEP 任何位宽都禁用（全书唯一 NEVER 红线）；6 GHz 频段 PMF 强制、老协议进不去。
- CNSA 开启即排除 WPA2 终端，混合终端网慎开。
- 6 GHz 是 Greenfield：无向下兼容负担是优点，也意味着老终端完全不可见该频段。
- MU-MIMO 与 OFDMA 非二选一，实际网络叠加使用；别用单一技术解释性能。

---
来源条目: g01, g02, g03, g04, g05, g06, g07, g08, g09, g10, g11, g12, g13, g14, g15, g16, g17, g18, g21, g22, g23, g24, g25, g26, g27, g28, g31, p05, p07, p09, p11, p12, ce01
