---
name: stellar-wifi7-hardware-rf-quickref
description: 何时用：AP 选型（Wi-Fi 7/天线/兼容红线）、模式与规模容量规划、RF 漫游阈值调优、Mesh/Bridge 组网时查参数。
source_book: DT00XTE378EN Stellar WLAN Adv Troubleshooting & Update
---

# 新硬件与 RF 特性速览：Wi-Fi 7 家族 · 模式规模红线 · 漫游阈值 · Mesh/Bridge

## R · 原文引用

> "AP1511: Tri radio; 2.4GHz radio: 688Mbps (2x2:2SS/EHT40); 5GHz radio: 2.88Gbps (2x2:2SS/EHT160); 6GHz radio: 5.76Gbps (2x2:2SS/EHT320); Up to 32 SSID; 512 clients per AP; 802.3at/bt POE (up to 35W). AP1521: 1 x 1/2.5/5/10GE multi-gigabit uplink; 802.3bt POE (up to 60W)." (p152-153)

> "Self configured AP cluster, up to 255 APs... Max Up to 32 APs per OmniSwitch; Max Up to 64 APs per stack; Minimum 2xAP123X, AP13xx, 14xx or 15X1 in each Stack. Up to 4000 APs." (p169-176)

> "(p365) To convert the RSSI value to dBm you just need to subtract 96 to the RSSI value. -18 dBm = 78. (p186) RSSI 10 = -86 dBm; RSSI 20 = -76; RSSI 30 = -66." (p186, p365)

> "WIFI MESH – LIMITATIONS: UP TO 4 HOPS; UP TO 5 APS IN A SINGLE HOP...; UP TO 16 APS IN THE MESH NETWORK; ALL APS CAN BROADCAST UP TO 5 SSIDS FOR CLIENTS." (p399-401)

## I · 方法论骨架

四组速查知识：

1. **硬件选型**：Wi-Fi 7 双雄（1511 入门 / 1521 中档）规格对比；外接天线判定规则；Mesh/Bridge 兼容红旗；DPI/WCF 排除型号。
2. **模式与规模**：Express（自组集群 255 AP，单交换机 32 / 单堆叠 64，每堆叠至少 2 台高端型号当 PVM/SVM）/ Enterprise（OV2500，4000 AP）/ Cloud（Cirrus）；IPv6 支持深度差异（Express 全栈，Enterprise 管理面仅 IPv4）。
3. **RF 参数**：RSSI↔dBm 换算（dBm = RSSI − 96）；漫游特性与安全级别绑定（OKC 仅 WPA2-Enterprise，11r 推荐且 WPA2 可用）；Roaming RSSI 阈值推荐 2.4G=10 / 5G=15。
4. **Mesh/Bridge**：硬限制四条 + 最佳实践（回程 5/6GHz、信道 >100）；Bridge 是"无线网线"不服务客户端、单 Root；Mesh 可多 Root 可服务客户端。

## A1 · 书中案例（Lab 精要）

- **c08 RF Profile 阈值实验**：客户端信号 -18dBm（RSSI 78），把 Association RSSI Threshold 设为 90，AP 直接忽略其关联请求（任何 SSID 都连不上）；切回默认 Profile 恢复。核验命令：`cat /tmp/config/rfprofile.conf` 看 signalStrengthThreshold / roamingSignalStrengthThreshold 实际下发值；客户端 RSSI 用 `wlanconfig ath102 list`。
- **ce01 Band Steering 默认关闭的设计权衡**：假设双频同覆盖；5G 有覆盖洞时设备仍被赶去差频段，Force 5GHz 更无退路。对策：双频同覆盖设计，或 Exclude MAC OUI 排除扫描枪/MIPT 话机等设备。
- **ce08 漫游撞后台扫描**：新 AP 正在后台扫描会打断实时业务；语音有感知豁免（检测到呼叫自动停扫），视频会议等其他实时流量无豁免。对策：敏感区域关 Background Scanning，或设专职扫描 AP。
- **ce09 Roaming 阈值两头是坑**：太低→客户端粘着弱 AP；太高→漫游过度丢包。从推荐值起步小幅调。
- **p13 BLE Beaconing**：AP1230/13xx 内置 BLE 可做信标，按 AP Group 配置（默认关，iBeacon 模式，UUID/Major/Minor），配合 AeroScout RTLS 做资产定位。

## A2 · 触发场景（含与相邻 skill 的区分）

- 新购选型（要 10G 上联/60W 供电选 1521，成本敏感选 1511）；需要外接天线定向覆盖；Express 还是 Enterprise 的容量测算；粘滞客户端/漫游体验差调阈值；两栋楼无线互联选 Bridge 还是 Mesh。
- 与 `stellar-enterprise-onboarding` / `stellar-ssid-policy-advanced` 的区分：那两个管"设备纳管"和"SSID 业务"；本 skill 管选型参数、模式容量、射频调优——设备已在网、配置已下发但体验/覆盖有问题时来查这里。
- 与 `stellar-rap-backup-upgrade-ops` 的区分：Mesh 是本地回程组网，RAP 是跨公网 VPN，两者都延伸覆盖但机制完全不同。

## E · 可执行步骤

**选型速查**：
1. Wi-Fi 7：AP1511（三射频 2x2，6G EHT320 5.76G，32 SSID/512 客户端，上联 1/2.5/5GE，PoE ≤35W）vs AP1521（同射频，上联 1/2.5/5/10GE + 1GE 下联，802.3bt ≤60W，低功率模式 at 仅 15W）。
2. 外接天线：型号尾数为 2 才支持（AP1322/1362）；所有 AP 标配内置全向天线；具体天线型号查数据手册天线矩阵。
3. 兼容红旗清点：AP1101 不支持 RAP/CNSA/DPI/WCF；AP1201H 不支持 DPI/WCF；AP1101/1201/1201H 不支持桥上 VLAN tagging。
4. 容量：Express 集群 ≤255 AP、每交换机 ≤32、每堆叠 ≤64（堆叠内至少 2 台 AP123X/13xx/14xx/15X1）；Enterprise ≤4000 AP。IPv6 刚性项目：管理面要 IPv6 只能 Express（Enterprise 下 AP 管理/UPAM RADIUS 走 IPv4，客户端侧 IPv6 可用）。

**RF 调优**：
5. 一切阈值先换算：dBm = RSSI − 96（OV2500 客户端列表显示 dBm，AP RF 设置用 RSSI，两侧比较前必须统一单位）。信号分档：RSSI 29+（约 -67dBm 以上）为推荐，10-19 差（别跑视频语音）。
6. 漫游：按 home/foreign AP 是否同 VLAN 定二层/三层漫游；开 802.11r（WPA2 下推荐）；OKC 仅 WPA2-Enterprise；Roaming RSSI 阈值从 2.4G=10 / 5G=15 起步，配 11k/11v；直角走廊等射频互不可见的相邻 AP 手动互加 Neighbor AP。
7. 阈值不生效/需核验时：AP 侧 cat rfprofile.conf 看实际下发值。

**Mesh/Bridge**：
8. 核对四条硬限制：≤4 跳、单跳 ≤5 台、全网 ≤16 台、每台 ≤5 个客户端 SSID。
9. 回程用 5GHz（或 6GHz）、信道 >100；两端 SSID/频段/Passphrase 一致；Bridge 恰 1 台 Root，Mesh 可多 Root。
10. Auto Mesh：有线侧 Mesh Root 广播隐藏 SSID "Stellar-MESH"（5GHz），无网线 AP 自动以非 Root 入网。

## B · 边界与陷阱

- **Band Steering 默认关闭是设计决策不是疏忽**：5G 覆盖弱时开了反而有害；Force 5GHz 让客户端无退路。
- **阈值单位混用是 RF 调优第一大坑**：-18dBm 对应 RSSI 78，要挡住它阈值需 ≥78（教材用 90）。
- **漫游与安全级别绑定**：WPA3-Enterprise 下 OKC/11r 的可用性按教材以 WPA2 表述为准，升级 SSID 安全级别时回查漫游特性。
- **语音感知豁免只覆盖语音**：视频会议等其他实时流量会被后台扫描打断。
- **Mesh 16 台/4 跳是硬红线**，超规模用 RAP 或有线回程解决。
- BLE Beaconing 默认关闭，配置粒度是 AP Group 不是单台 AP。

---
来源条目: p02, p04, p05, p11, p12, p13, p14, p15, p20, c08, ce01, ce08, ce09
