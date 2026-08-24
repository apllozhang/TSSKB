---
name: special-topologies
description: 何时用：无线回程（Bridge/Mesh）、远程接入（RAP）、ESL 价签、Zigbee/RTLS IoT、访客隧道与安全合规等特殊组网时。
source_book: DT00XPS288EN Stellar WLAN Presales
---

# 特殊组网（Bridge / Mesh / RAP / ESL / IoT / 访客隧道 / 安全合规）

## R · 原文引用

> "WIFI BRIDGE AIM: Replace physical cabling … Cannot provide service (WiFi) to WiFi clients. WIFI MESH … Can provide service (WiFi) to WiFi clients."（p110）

> "WIFI MESH – LIMITATIONS • UP TO 8 SLAVE APS • UP TO 4 HOPS … UP TO 16 APS IN THE MESH NETWORK • ALL APS CAN BROADCAST UP TO 5 SSIDS. BEST PRACTICE • BAND: 5 GHZ … CHANNEL > 100."（p112）

> "RAP – REMOTE ACCESS POINT • Use Cases • Homeworking • Corporate Branch Offices • Solution • VPN Server in the corporate network • Clients data encrypted between the Stellar AP and the VPN Server."（p99）

> "Proprietary ESL transmitter -> Not selected. Because new deployment (wiring, device installation) required. Proprietary ESL USB dongle -> Selected. To be connected to the existing Stellar infrastructure. Minimal impact."（p197）

## I · 方法论骨架

**Bridge vs Mesh 单判据二分**：要不要给 Wi-Fi 终端提供服务？只替代布线（跨街楼宇、露营回传）→ Bridge（可 VLAN 隔离但不发 WiFi，两端 SSID/频段/密码一致，仅 1 台 Root）；既要回传又要覆盖 → Mesh（可多 Root；红线：8 从 AP / 4 跳 / 单跳对多点 5 台 / 全网 16 台 / 5 个客户端 SSID；最佳实践 5GHz 建链、信道 >100；Auto Mesh 隐藏 SSID "Stellar-MESH" 自动成网）。

**RAP 远程接入**：公司网内部署 VPN 服务器，AP-VPN 间加密传数据（支持 VLAN 标）；前提：除 AP1101 外全部机型、AP ≥4.0.0、网管 ≥4.5.1；账号组合——有 OV2500 配 Cirrus Freemium 账号，无 OV2500 需 Cirrus Premium 账号。

**ESL 电子价签**（零售）：AP 激活 USB Type A/C 母口 → Hanshow USB Dongle（USB-C 公头）取电，2.4GHz 专有射频连价签 + 连 Hanshow 云；对比"新装专有发射器"，复用既有 AP 是核心卖点；AP 可在 Express 或 Cirrus 模式管理，需互联网访问两个云。

**IoT 定位与门锁**：Zigbee 除 AP1301/AP1230 外全系列内置（门锁数字钥匙，经 Assa Abloy HTTP 隧道集中管理）；BLE Beacon 默认关、默认 iBeacon 模式、按 AP Group 配。RTLS：AeroScout 标签发 802.11 报文、Stellar AP 采 RSSI 送引擎定位——不建专网。

**访客 GRE 隧道**：按 Access Role Profile 从 AP 建到 OS6860/E（终结 750 条）或 OS6900（终结 1000 条）；每 AP 最多发起 16 条。

**安全合规**：WPA3 Personal=SAE 128 位；Enterprise 可选 CNSA 192 位——CNSA 开启后 SSID 只放 WPA3 终端；WiFi4EU 要求 HTTPS Portal + 会话超时可配至 12 小时。

## A1 · 书中案例

- Bridge 露营覆盖 vs Mesh 隔街楼宇成对配置示例（含 SSID/密码示例 STELLAR-BRIDGE / STELLAR-MESH）（c15）。
- 零售 40+ 门店 150 台 AP 上 ESL Dongle（c07）。
- Zigbee 客房门锁数字钥匙（c13）、AeroScout 厂房人员追踪（c14）、RAP 居家/分支（c16）。

## A2 · 触发场景（含与相邻 skill 的区分）

- 触发：客户要跨楼宇/无布线覆盖、居家办公远程接入、零售数字化价签、资产定位、高安全 WPA3 应标。
- 区分：本 skill 管特殊组网与 IoT；普通场景数量配置去 `rf-scenario-baseline`；行业案例叙事去 `industry-use-cases`。

## E · 可执行步骤

1. 回程需求先问一句"要不要给终端发 WiFi"→ 定 Bridge 或 Mesh。
2. Mesh 校核四道红线（16/8/4/5），超限改点位设计（立杆 + AP1361）。
3. RAP 项目先核机型（排除 AP1101）与版本（AP 4.0.0+ / 网管 4.5.1+），再定 Freemium/Premium 账号组合。
4. IoT 需求入场即筛机型：Zigbee 排除 AP1301/AP1230，出"机型×协议兼容表"附方案。
5. 访客隔离：按 AP 数 × 每角色隧道数核算交换机终结容量（750/1000）。
6. 高安全应标：开 CNSA 前盘终端 WPA3 能力，老终端单独过渡 SSID。

## B · 边界与陷阱

- Mesh 超 16 台/4 跳组不起来；SSID 规划 >5 个放不下（ce11）。
- AP1101/AP1201/AP1201H 桥上不支持 VLAN 标签（ce10）。
- Zigbee 入门机型例外侵蚀利润（ce09）。
- 访客隧道超限局部瘫痪（ce13）；WCF 需 OV 平台，Express 模式买了也跑不起来（ce14）。
- CNSA 拒老终端：扫码枪/打印机掉线风险，先盘点（ce15）。

---
来源条目: f06, p09, p10, p11, p12, p13, p14, p25, c07, c13, c14, c15, c16, ce09, ce10, ce11, ce12, ce13, ce14, ce15；glossary: Wi-Fi Bridge、Wi-Fi Mesh、RAP、ESL、RTLS、AeroScout RTLS、Zigbee、GRE Guest Tunneling、WPA3、Hotspot 2.0、UNP、Access Guardian、AWOS、BYOD、DRM
