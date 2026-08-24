---
name: management-mode-selection
description: 何时用：客户问"免管/本地/云管怎么选"、Express 规模上限、模式迁移或 AP 上线不上班排障时。
source_book: DT00XPS288EN Stellar WLAN Presales
---

# 三种管理模式选型与 Express 集群工程（Express / OV2500 / Cirrus）

## R · 原文引用

> "NETWORK MANAGEMENT MODES - OVERVIEW: Wi-Fi Express Standalone mode; Wi-Fi Enterprise - In Premise - Managed mode with OmniVista 2500 NMS; Wi-Fi Cloud - Cloud based - Managed mode with OmniVista Cirrus NMS. Move from Express to Enterprise/Cloud when/if needed."（p41）

> "A Group can not contain more than 255 APs. The 256th AP is not taken into account. Will stay in 'joining' mode."（p46）

> "AP is managed when Registration succeeds: AP is Trusted, AP is Licensed, Country Code matches RF profile CC. AP is unmanaged when Registration fails … Configuration not applied, All Radios are off."（p68）

> "Migration from existing Express to Enterprise mode: load the new software. Add option 138 in the DHCP server … Perform a factory reset/reboot. No configuration migration, AP 'cluster' configuration is lost."（p66）

## I · 方法论骨架

决策两变量：**网络规模**（小→中→大）× **管理偏好**（免管 / 本地部署 / 云订阅）。

| 维度 | Express | Enterprise（OV2500 本地） | Cloud（Cirrus） |
|---|---|---|---|
| 面向 | SMB | 中大型/安全敏感 | 各规模、多分支 |
| License | 免、送 5 个永久 | 永久买断 | 订阅 |
| 容量红线 | 255 AP/集群；>64 台需冗余 | 4000 AP / 100K 客户端 | 4000 AP / 100K 客户端 |
| 成长路径 | 可迁 Enterprise/Cloud（配置不迁移） | — | — |

Express 集群规则：同 VLAN 多 AP 启动时按"最高型号 + 最高 MAC"选 PVM，MAC 次高为 SVM；默认管理 SSID `mywifi-0102`；每台 OmniSwitch ≤32 AP、每堆叠 ≤64 台且至少 2 台可任 PVM/SVM。

模式判定开关：DHCP 有无 Option 138（OV 服务器地址）——出厂即 Express，模式首次启动固化，切换须恢复出厂。

AP 纳管三条件（与门）：Trusted（默认需手动 Trust，导入/手工创建视为可信）+ Licensed + 国家码与 RF Profile 一致；任一失败即 Unmanaged、射频全关。

## A1 · 书中案例

- 文理学院换 Ubiquiti：BP 用 OmniVista Cirrus 远程运维监管（c04）。
- 大学 600 AP 演进：一期 AP1321 + OV Cirrus 云管（c03）。

## A2 · 触发场景（含与相邻 skill 的区分）

- 触发：客户说"我只要简单 WiFi"（→Express，5 免费 License 起步）；合规要求本地部署（→OV2500）；多分支连锁（→Cirrus）。以及"AP 上线但没信号"排障、Express 扩容卡 joining、Express→Enterprise 割接方案。
- 区分：本 skill 管"模式怎么选、怎么迁、怎么排障"；License 报价与 part number 去 `license-quotation`；具体 RF/场景配置去 `rf-scenario-baseline`。

## E · 可执行步骤

1. 问规模与偏好 → 套三选一表；SMB 首推 Express（零软件成本起步）。
2. Express 容量校核：AP 数 ≤255？超则拆多 Group-ID/多 VLAN 或转 Enterprise/Cloud。
3. 冗余设计：集群 >64 台时每堆叠放 ≥2 台可任 PVM/SVM 的机型。
4. 割接方案（Express→Enterprise）：Web 加载新软件 → DHCP 加 Option 138 → 恢复出厂重启 → 配置重建；单独报实施工作量与停机窗口。
5. 排障"上线不上班"：查 License 数量 → 查 Trust 动作 → 查国家码/区域码匹配。
6. 连锁客户有固件升级诉求：提前说明 Express 远程不能升镜像，建议转 Enterprise/Cloud。

## B · 边界与陷阱

- 第 256 台静默卡 joining 不报错（ce05）。
- "Easy conversion"话术与配置丢失现实冲突：迁移时集群配置全部丢失（ce06）。
- Express 远程管理不支持 AP 组镜像升级（ce07）。
- Enterprise 管理面仅 IPv4、AP 无 IPv6 管理接口（Express 反而支持 v6）；纯 v6 管理客户别硬应标（ce16）。
- 批量开局"全部没信号"根因常是默认手动 Trust 未点（ce08）。

---
来源条目: f02, f03, f04, f05, p03, p04, p05, p06, ce05, ce06, ce07, ce08, ce16；glossary: Stellar Express、Stellar Enterprise (On-Premise)、Stellar Enterprise Cloud、DHCP Option 138、PVM/SVM、Controller-less Architecture、OmniVista 2500、HA
