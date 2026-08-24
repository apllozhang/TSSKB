---
name: bridge-mesh-deployment
description: 何时用：无法布线场景下用 WiFi Bridge 点对点连楼、或用 Mesh/Auto Mesh 延伸覆盖建网时。
source_book: DT00XTE455EN Stellar WLAN Express
---

# WiFi Bridge / Mesh 特殊组网

## R · 原文引用

> "WIFI BRIDGE PROPERTIES: Cannot provide service (WiFi) to WiFi clients. WIFI MESH PROPERTIES: Can provide service (WiFi) to WiFi clients. * AP1101, AP1201 & AP1201H are not compatible with VLAN tagging over a bridge." (p112)

> "SSID: WLAN used to setup wireless bridge connection. Must be the same on both APs. Band: Must be the same on both APs. Is Root: Specify the root AP of the wireless bridge, 1 AP must be set as Root. Passphrase: Must be the same on both APs." (p113)

> "AUTO MESH. Aim: quick & easy deployment of a Mesh topology. If a Stellar AP is: Connected to the LAN, Configured as MESH root, It will Broadcast an hidden SSID « Stellar-MESH », Band: 5 GHz. If a Stellar AP is: Not connected to the LAN, It will Have MESH enabled as non-root." (p115)

## I · 方法论骨架

先做选型判断，再套配置规则：

1. **Bridge vs Mesh 选型口诀**：只做两点连线（跨街楼宇延伸 LAN）选 Bridge；要延伸覆盖（终端也要连）选 Mesh。本质区别：Bridge 是纯回程链路、不给客户端供 WiFi；Mesh 节点回程与服务并存，允许多根（多出口），可用 VLAN 按 SSID 分离客户端流量。
2. **Bridge 四属性 = 三同一根**：SSID/Band/Passphrase 双方一致，Is Root 只有一端为 Yes。任何一项不满足桥建不起来。
3. **Mesh 配置同理 + 多根**：属性规则同 Bridge，但可定义多台 root。
4. **Auto Mesh 零配置建网**：只配接 LAN 的根节点（自动广播隐藏 SSID "Stellar-MESH"、5GHz），其余 AP 不接线摆到位通电即以非根身份入网。
5. **回程最佳实践**：频段 5GHz（或 6GHz）、信道 >100，避开 2.4G 与低段 5G，不与业务信道互扰。

## A1 · 书中案例

- 跨街楼宇 Bridge（p112-113）：无法铺线的两栋楼，根端 SSID=STELLAR-BRIDGE、Band=5GHz、Is Root=Yes、Passphrase=ALCATEL123!；对端同 SSID/同频段/同密码、Is Root=No。可照抄改密码即用。
- 营地 Mesh（p112, p114）：根节点与 Mesh 节点各自广播业务 SSID "WIFI GUESTS"（2.4+5GHz、开放加密走 Portal），同时以 "STELLAR-MESH"（5GHz、加密）建回程——业务/回程 SSID 分离的完整写法。
- Auto Mesh 通电即入网（p115）：现场只配一台根，其余 AP 摆位通电自动入网，适合弱电条件差的仓库/营地。

## A2 · 触发场景（含与相邻 skill 的区分）

- 触发：两栋楼间无法布线要打通 LAN、露天/大空间要快速拉开无线覆盖、临时场地建网。
- 区分：普通"AP+交换机"的集群上线与分域规划用 `express-cluster-onboarding`；信号弱/覆盖差但已有有线回程的场景用 `rf-survey-tuning`（补点、调功率），只有回程本身要用无线解决时才用本 skill。识别现场是否走了 Auto Mesh：搜隐藏 SSID "Stellar-MESH"。

## E · 可执行步骤

Bridge 部署：
1. 两端 AP 各配四属性：SSID、Band、Passphrase 三项两端一致；一端 Is Root=Yes、另一端 No。
2. 回程按最佳实践选 5GHz（或 6GHz）、信道 >100。
3. 需要在桥上分离流量时加 VLAN 标签（先确认型号支持，见边界）。

Mesh 部署：
4. 手工方式：同 Bridge 属性，根可配多台；业务 SSID 与回程 SSID 分开规划。
5. Auto Mesh 方式：把接 LAN 的 AP 配成 Mesh root → 确认其广播隐藏 SSID "Stellar-MESH"（5GHz）→ 其余 AP 断 LAN、摆位、通电 → 验证自动入网。

验收与排障：
6. 桥建不起来：按"三同一根"逐项核对两端配置（双根或无根是常见根因）。
7. Mesh 节点不入网：核对该节点是否未接 LAN、是否为 Stellar 型号、隐藏 SSID 是否可达。

## B · 边界与陷阱

- **别拿 Bridge 当覆盖用**：桥上不为任何 WiFi 客户端提供服务，客户端根本搜不到服务——要覆盖必须 Mesh。
- **Mesh 四条硬红线**：最多 4 跳；单跳（点对多点）最多 5 台 AP；全网最多 16 台 AP；每节点对客户端最多 5 个 SSID。大型园区想靠 Mesh 无限级联会撞墙，超 16 节点回有线，Mesh 只做最后几跳。
- **VLAN 兼容性**：AP1101/AP1201/AP1201H 做 Bridge 不支持 VLAN 标签（教材星号脚注），桥上跑多 VLAN 的规划在这三款上会失败——换型号或改 Mesh。
- Auto Mesh 的默认参数（隐藏 SSID "Stellar-MESH"/5GHz/非 LAN 即非根）是出厂行为，无需也无法逐台预配置。

---
来源条目: f04, f05, p07, p08, p09, p10, c03, c04, c05, ce03, ce04, ce05, g20, g21, g22, g23
