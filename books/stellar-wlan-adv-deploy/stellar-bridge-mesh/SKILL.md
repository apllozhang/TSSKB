---
name: stellar-bridge-mesh
description: 何时用：两栋楼间无线桥接（Bridge）替代布线，或布线困难区域用 Mesh 无线回传组网时用。
source_book: DT00XTE361EN Stellar WLAN Advanced Deployment
---

# Bridge 点对点桥接与 WiFi Mesh 组网

## R · 原文引用

> "SSID ... Must be the same on both APs; Band ... Must be the same on both APs; Passphrase ... Must be the same on both APs." (p114-115)

> "UP TO 8 SLAVE APS; UP TO 4 HOPS; UP TO 5 APS IN A SINGLE HOP IN A PEER TO MULTI PEER CONNECTION; UP TO 16 APS IN THE MESH NETWORK; ALL APS CAN BROADCAST UP TO 5 SSIDS FOR CLIENTS. WIFI MESH – BEST PRACTICE: BAND: 5 GHZ; CHANNEL > 100." (p114-115)

> "In the Device Catalog section, select the AP that will be part of the Mesh or Bridge configuration and go to Actions > Edit Device > Mesh/Bridge Configuration." (p118)

> "* AP1101, AP1201 & AP1201H are not compatible with VLAN tagging over a bridge." (p113)

## I · 方法论骨架

- **Bridge**：点对点无线桥接替代物理布线；可用 VLAN 分隔桥上流量，但不能向 Wi-Fi 客户端提供服务。
- **Mesh**：Root AP 接 LAN、Repeater 无线回传；可多 Root；Mesh 链路上仍可对客户端广播 SSID（每 AP 最多 5 个）。
- **建链三要素**：SSID、频段、密码两端必须完全一致——这是能不能建链的第一判据。
- **容量红线**：全网 ≤16 AP、每 Root ≤8 从 AP、≤4 跳、单跳点对多点 ≤5 AP。
- **最佳实践**：回传用 5GHz、信道选 100 以上（避开常用客户端信道）。
- **Auto Mesh**：免配置快速组网——接 LAN 且设为 Root 的 AP 广播隐藏 SSID "Stellar-MESH"（5GHz），未接 LAN 的 AP 自动入网。

## A1 · 书中案例（Lab 精要）

Lab（p117-121）：Device Catalog 选中 AP → Actions > Edit Device > Mesh/Bridge Configuration → 填模式/频段/SSID/密钥管理与密码（Mesh 多一个 Is Root 选项）→ 保存后两端生效。监控：Mesh Topology 列表显示每台 AP 的 MAC、角色（Root/Repeater）、Level、BSSID、频段、SSID 与 Parent Address（即上游 Root AP 的 MAC），用于确认拓扑按预期成链。Auto Mesh（p116）演示免配置组网。综合演练末段（p299）把两台 AP 改成 Mesh：AP1321 为 Root、自定义 Mesh SSID、WPA2-Personal。

## A2 · 触发场景（含与相邻 skill 的区分）

- 跨楼宇/厂房拉线困难，需要无线桥或回传组网 → 本 skill。
- 常规室内覆盖部署（AP 全部有线上联）→ stellar-deployment-checklist。
- Mesh 建不起来或链路不稳：先查本 skill 三要素与容量红线，再考虑射频环境（低功率陷阱见 stellar-troubleshooting-cli 的 ce07）。
- 桥上要多 VLAN 隔离 → 注意选型限制（见 B）。

## E · 可执行步骤

1. 选型确认：需要桥上 VLAN 打标时避开 AP1101/AP1201/AP1201H。
2. 核对规模：对照容量红线（16/8/4/5）确认 AP 数与跳数可行。
3. Device Catalog 选参与 AP → Actions > Edit Device > Mesh/Bridge Configuration。
4. 填参数：模式（Bridge 或 Mesh）、频段（建议 5GHz、信道>100）、SSID、密钥管理、密码；Mesh 指定 Is Root。两端三要素逐项核对一致。
5. 保存后到 Mesh Topology 看角色与 Parent Address，确认成链。
6. （可选）快速部署场景用 Auto Mesh：一台接 LAN 设 Root，其余开机自动入网。
7. 验证业务：Repeater 侧关联客户端，确认能拿到正确 VLAN 的 IP。

## B · 边界与陷阱

- 三要素不一致是最常见建链失败原因，逐字核对（含大小写与隐藏空格）。
- 超容量红线（如 5 跳、17 台 AP）无解，只能加 Root 或改有线回传。
- AP1101/AP1201/AP1201H 桥接不支持 VLAN 打标，选型阶段就要排除。
- Bridge 模式不给 Wi-Fi 客户端提供服务，想同时放客户端要用 Mesh 或另配。
- Mesh 回传信道选 100 以下是实践禁忌：会和客户端业务信道互相干扰。

---
来源条目: f06, c04, p09, p10, ce10, g28, g29, g30, g31
