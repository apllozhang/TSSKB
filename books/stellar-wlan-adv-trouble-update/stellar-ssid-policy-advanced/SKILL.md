---
name: stellar-ssid-policy-advanced
description: 何时用：需在 OV2500 建/改 SSID（员工 802.1X、AD 对接、访客门户、WCF、BYOD 动态 VLAN）及限速策略排障时。
source_book: DT00XTE378EN Stellar WLAN Adv Troubleshooting & Update
---

# SSID 与策略进阶：802.1X / AD / 访客门户 / WCF / BYOD 与带宽判定

## R · 原文引用

> "SSID: Wizard driven tool. Pre-defined Usage (Guest, Employee, BYOD,...). All the configuration is performed from the wizard. Recommended mode. WLAN service (expert): Manual configuration... Limited usage for specific SSIDs." (p243)

> "Matches a DPI application in the Policy List? Y: Application Specific BW Enforcement as per DPI Rule... Access Role set with BW Control? Y: User BW Enforcement... SSID set with BW Control? Y: Shared BW Enforced as per WLAN Service/SSID. N: No BW Limitation." (p284)

> "The shared secret in the system-defined 'All Managed Devices' NAS profile is '123456'." (p307)

> "BE SURE TO DISCONNECT AND RECONNECT THE VIRTUAL MACHINE FROM THE NETWORK TO FORCE THE RE AUTHENTICATION AS THE POLICY IS APPLIED ONCE THE CLIENT AUTHENTICATION IS SUCCESSFUL." (p338)

## I · 方法论骨架

1. **Usage 模板定骨架**：向导选 Usage = 选安全模板（Guest=Open/MAC+门户；Employee BYOD=802.1X+BYOD 注册；Enterprise for Employees=纯 802.1X；Protected=PSK+可选门户），再逐步微调。
2. **必填项清单**：Enterprise 级 AAA Profile 必填（加密六选一至 WPA3_AES）；Personal 级 Passphrase+Key Format 必填（含 WPA3_SAE_AES）；Default Access Role Profile（承载 QoS/门户/带宽并映射 VLAN）一律必填。
3. **认证源三级**：UPAM 本地库 → 企业 AD（LDAP/AD Configuration 两步切换）→ 外部 RADIUS。
4. **限速四层判定**（从细到粗）：DPI 应用规则 → ACL 规则 → 用户级 Access Role → SSID 共享；配置入口分别在 Unified Policy Policy List / Advanced Access Role / Advanced WLAN Service。
5. **变更闭环三步**：改配置 → Apply/Notify 推送 → 受影响客户端断开重连强制重认证（策略只在认证瞬间应用）。

## A1 · 书中案例（Lab 精要）

- **c03 员工 SSID**：EmployeesX，Usage 选 Enterprise Network for Employees，WPA3_AES + UPAMRadiusServer，默认 VLAN 20；客户端 PEAP/MSCHAPv2（不校验 CA）接入。Expert 模式等价七对象：WLAN Service → AAA Server Profile → Access Role Profile（Apply to Devices 映射 VLAN）→ Authentication Strategy → Access Policy（条件 SSID=xxx）→ 部署。AP 侧排障：`cat wlanservice.conf` / `AAA_server.conf` 核对 RADIUS 参数，`tcpdump -i br-wan host <radiusIP>` 抓认证报文。
- **c04 对接 AD**：UPAM > SETTINGS > LDAP/AD Configuration 填 Server Type=AD、NETBIOS/DNS 域名、域控 IP、绑定账号、端口 389，Test Connection 后 Apply；再把 SSID 的 Authentication Strategy 从本地库改 External LDAP/AD。
- **c05 访客门户**：GuestsX 启用 OV-UPAM 门户；重定向验证用 http://非HTTPS URL；KickOff 踢线可重连、Add to Blocklist 拉黑不可重连。
- **c06 WCF**：AP Group 激活 WCF → UPAM 建 WCF-guests（Social Networking/Gambling=Reject）→ 绑到 __GuestsX 角色档案 → **Apply to Devices**（否则只改在服务器本地）。原理：AP 窥探 DNS 取 FQDN → Brightcloud 分类 → 生成针对解析 IP 的阻断 ACL。
- **c07 BYOD 动态 VLAN**：不建新 VLAN——预认证落 Guest VLAN 30，门户认证（Post Portal Authentication Enforcement 设 Fixed Access Role=_EmployeesX）后动态迁到 Employee VLAN 20。
- **ce06**：OV2500 虚机没配 DNS → WCF 状态 "Not in service"、连不上 Brightcloud API；虚机菜单 [2]→[6] 补 DNS。

## A2 · 触发场景（含与相邻 skill 的区分）

- 新建/改造员工、访客、BYOD SSID；认证源切换到 AD；访客网页过滤；基于角色的限速不生效。
- 与 `stellar-enterprise-onboarding` 的区分：设备已纳管（在 AP Group 里），本 skill 处理空口业务与认证策略。
- 与 `stellar-wifi7-hardware-rf-quickref` 的区分：本 skill 不处理射频参数（漫游/阈值/Band Steering 属那边）。

## E · 可执行步骤

1. 向导建 SSID：服务名 + 空口名（可多服务共用）→ 选 Usage 模板 → 频段/加密/PSK/默认 VLAN/认证策略 → 绑 AP Group（可调度广播时段）。
2. 802.1X：AAA Profile 选 UPAMRadiusServer（内嵌 UPAM）或外部；建员工账号或接 AD。
3. 接 AD：UPAM LDAP/AD Configuration 填域信息 → Test Connection → Apply → SSID 认证策略切 External LDAP/AD。
4. 访客：启用 OV-UPAM 门户 + Guest 账号（注意有效期）；管理动作用 KickOff/Blocklist。
5. WCF：AP Group 激活+Commit → 建档案 → 绑角色 → Apply to Devices；前置检查 OV2500 DNS。
6. BYOD：Post Portal Enforcement 设员工角色，默认 VLAN 放访客段，靠动态迁移。
7. 限速：按四层判定选入口配置（DPI/ACL → Access Role → SSID 共享）。
8. 每次改完：Apply to Devices/Notify All → 客户端断开重连验证。

## B · 边界与陷阱

- **策略只在认证瞬间应用**：推完不重连重认证就测试，会误判"配置有错"。
- **UPAM 系统级 NAS 项 "All Managed Devices" 共享密钥固定 123456**——802.1X 排障第一怀疑点。
- **Apply to Devices 缺失**：改 Access Role Profile 只留在服务器，不推 AP（c06 教材原文警告）。
- **DPI/WCF 硬件排除 AP1101 与 AP1201H**：混装这两款的区域策略只"部分生效"。
- **WPA3 CNSA 192 位开启后只允许 WPA3 客户端**（WPA2 终端被拒）；AP1101 不支持 CNSA。
- **WMM 映射**：OV2500 默认值与推荐值不一致（推荐 Voice 5/46-EF、Video 4/34-AF41），语音视频项目按推荐表改。
- **广播密钥轮换仅企业级**；Multicast Optimization 有熔断（信道利用率>90% 或高吞吐客户端>6 自动停）。
- Guest 访客账号排障先核时间/日期（有效期）。

---
来源条目: f01, f04, p06, p07, p08, p09, p10, p21, p22, c03, c04, c05, c06, c07, ce06, ce07
