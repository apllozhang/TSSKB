---
name: express-mode-bootstrap
description: 何时用：Stellar AP 开局判定部署模式（Express/Enterprise/Cloud）、准备 PoE/VLAN/DHCP 前置、管理 Express 集群与首次接入排障。
source_book: DT00XTE360EN ACFE WLAN Basic Deployment
---

# 部署模式决策与开局前置（Express 模式底座）

## R · 原文引用

> "NETWORK DEPLOYMENT MODE SELECTION — DHCP REQUEST: IF DHCP SERVER SENDS OFFER WITH OPTION 138 = YES (IP@ OF OV2500) ... AP REGISTERS AND RETRIEVES ITS CONFIGURATION FROM OV2500; IF ... OPTION 138 = NO ... AP CONTACTS OV CIRRUS; IF AP REGISTERED IN OV CIRRUS (MAC/SN) = YES ... RETRIEVES ITS CONFIGURATION FROM OV CIRRUS; IF ... = NO ... AP BOOTS IN EXPRESS MODE" (p100)

> "Trunk Port with POE: Untagged/Native vlan = AP Mgt VLAN; Tagged VLANs = SSID VLANs. DHCP Scope for All AP Mgt VLANs (Require option 138 for OV IP address) and All SSID VLANs. DNS Server for All subnets. L3 protocols / Routing ... IP interfaces / Routers for All VLANs" (p25)

> "BY DEFAULT, THE OMNIACCESS STELLAR AP: BROADCASTS A SSID 'MYWIFI-ABCD' (ABCD = LAST BYTES OF THE AP MAC@); HAS THE IP@ = 192.168.1.254 ... TO ACCESS THE WEB ADMIN INTERFACE: OPEN A WEB BROWSER AND INSERT THE FOLLOWING URL HTTP://<IP@ OF THE AP>:8080" (p101)

> "PVM/SVM Election — Criteria 1: highest Stellar AP model; Criteria 2: highest MAC address ... up to 255 APs in a group." (p11)

## I · 方法论骨架

**1. 模式决策树（上电三级判定，反向用于模式规划）**
1. DHCP offer 带 option 138（OV2500 地址）→ Enterprise 模式
2. 无 138 → 联系 OV Cirrus，MAC/序列号已登记 → Cloud 模式
3. 都不满足 → Express 模式（默认），广播 mywifi-XXXX

想上云就先在 Cirrus 声明序列号；想进企业模式就在管理作用域配 option 138。

**2. 三平面模型（端口规划与排障的根基）**
- 管理平面：集中在网管（Express=PVM / 云管=Cirrus），管理流量**恒 untagged**（Native VLAN）
- 控制平面：每台 AP，空口邻居发现 + LAN 射频上下文共享
- 数据平面：AP 本地终结，按 SSID **恒 tagged** 上行，纯二层、无隧道回网管，路由交给 LAN

**3. 开局前置清单（五项逐条核对）**

| 项目 | 要求 |
|---|---|
| 端口 | PoE trunk；Native=管理 VLAN；SSID VLAN 全 tagged |
| DHCP | 管理 VLAN + 全部 SSID VLAN 各建作用域；企业模式管理作用域加 option 138 |
| DNS | 覆盖全部管理/SSID 子网 |
| 路由 | 所有 VLAN 有三层接口 |
| 供电 | 按型号 af/at/bt；af 下 AP1311 禁 PSE/USB，AP1230 需 at 60W，AP1351 需 bt |

**4. Express 集群机制**
- 成组规则：Group ID 相同 + VLAN 相同自动同组（出厂 Group ID 100 / VLAN 1）
- 选举：先比最高型号、再比最大 MAC → PVM；第二高 MAC → SVM；其余 Member；单组上限 255
- 容量建议：>64 台必须做弹性设计；每台 OmniSwitch ≤32 AP、每堆叠 ≤64 AP
- 管理平台规模：OV2500 ≤4000 AP；Cirrus 单实例 12000 设备（10000 AP+2000 交换机）

**5. 关键常数速查**
- 默认 SSID：mywifi-ABCD（MAC 末 4 位）；默认 IP 192.168.1.254；Web 管理端口 8080
- DHCP 模式下可用域名 mywifi.al-enterprise.com:8080 访问
- AP 控制台凭据 support/aos2016；OmniSwitch 出厂 admin/switch（仅控制台，Telnet/SSH/Web 全禁）
- 恢复出厂：Reset 键 10 秒，或 `ssudo firstboot -y && ssudo reboot`
- isc-dhcp-server 需先声明 `option ovwma code 138 = ip-address;`，再用 vendor-class 前 4 字节 "HAP." 类匹配 Stellar AP 下发

## A1 · 书中案例（Lab 步骤精要）
- **c03/p108-119**：控制台启用端口 `interfaces 1/1/6 admin-state enable` → 建管理 IP `ip interface int_1 address 192.168.1.2/24 vlan 1` → `write memory flash-synchro` → 浏览器 192.168.1.254:8080 → 向导改密/国家/建 SSID → 改静态 IP 后用新地址重连。
- **c04/p121-129**：`show lanpower slot 1/1` 验 PoE → `vlan 10/20/30 name ...` → AP 口 1/1/6：vlan10 untagged + vlan20/30 tagged；上联 1/1/3 全 tagged → AP 改 DHCP 后失联，改用域名 mywifi.al-enterprise.com:8080 重连。
- **c08/p33**：isc-dhcp-server 完整样例——class "STELLAR" match "HAP." + option ovwma + 专用 pool。

## A2 · 触发场景（含与相邻 skill 的区分）
- 新项目开局，要决定 AP 用哪种管理模式、做网络前置准备时用本 skill。
- 现场无网管/DHCP，要先把单台 AP 配起来（Express 最小路径）。
- **区分**：设备已决定上 Cirrus 云、要声明/激活/排障"不上云"→ `device-cloud-onboarding`；买许可/建组织/账号 → `cirrus-license-org-lifecycle`；建 SSID（含 Express 内嵌门户版）→ `ssid-authentication-suite`；本 skill 只管"模式判定 + 网络底座 + Express 集群"。

## E · 可执行步骤
1. 盘点目标模式：Enterprise（有 OV2500）/ Cloud（买 Cirrus 订阅）/ Express（SMB 无网管）。
2. 按前置清单配置交换机：管理 VLAN untagged、SSID VLAN tagged、DHCP/DNS/路由；企业模式在管理作用域配 option 138（isc-dhcp-server 先声明自定义 option）。
3. 核对 PoE 等级满足型号要求（`show lanpower`）。
4. Express 场景：连 mywifi-ABCD → http://192.168.1.254:8080 → 向导改密/国家/建 SSID；多台 AP 同二层自动成组，从 PVM 的 Web 统一管理。
5. 验证：`getmode` 确认 AP 实际模式；`show vlan members port` 确认端口 VLAN；客户端能拿对应网段地址。
6. 排障第一查项：option 138 是否正确下发、设备是否已在云上登记（配错则 AP 静默落 Express 广播 mywifi-XXXX）。

## B · 边界与陷阱
- **模式切换丢配置**：Express → Enterprise/Cloud 无配置迁移，集群配置全部丢失；切换前导出/记录全部 SSID/密码/VLAN/Portal 账号，当"重新开局"排期（ce01）。
- option 138 配错/遗漏或序列号未声明 → AP 静默落 Express，可能与已有集群意外成组（ce02）；用 `getmode` 排查。
- isc-dhcp-server 不认识 option 138，直接写会报错（ce03）。
- 改 AP 管理 IP 或切 DHCP 的保存瞬间即失联：立即用新 IP 或域名重连；多台 AP 默认 IP 相同会冲突，先隔离再改（ce13）。
- 不要对承载隐性依赖（DHCP/路由）的核心设备真恢复出厂（ce11 的生产类推）。
- Express 内置服务容量有限，后续 SSID/门户/策略复杂化时应整体迁云而不是硬撑。

---
来源条目: f01, f02, f03, f04, f05, p01, p02, p03, p04, p05, p06, p07, p08, p09, p11, p13, p14, p15, p16, c03, c04, c08, ce01, ce02, ce03, ce11, ce13 · 术语锚点: g15, g16, g22, g37, g38, g43, g52, g07
