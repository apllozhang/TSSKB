---
name: ssid-authentication-suite
description: 何时用：在 Cirrus/Express 上创建 Employee(802.1X)/Guest(门户)/BYOD SSID、选型 PSK 四级密钥体系，以及认证/门户类客户端排障。
source_book: DT00XTE360EN ACFE WLAN Basic Deployment
---

# SSID 全家桶：Employee / Guest / BYOD + PSK 四体系

## R · 原文引用

> "SECTION 1 «SSID SETTINGS»: Select the SSID Usage (each usage leads to a predefined template) ... SECTION 2 «NETWORK ASSIGNMENTS»: Apply the SSID to one site, one or multiple AP Groups ... SECTION 3 «SCHEDULE AND VLAN MAPPINGS»: Apply Schedule ... Apply VLAN/Tunnel Mapping: One or multiple VLAN (up to 256), One Guest Tunnel" (p312)

> "The BYOD employee device will be placed first in the Guest VLAN (pre-authentication). Once authenticated via a Captive Portal, it will be moved to the Employee VLAN (post-authentication)." (p391)

> "Device Specific PSK: Option enabled; Device performs MAC authentication; a specific PSK pass phrase is assigned to the MAC address ... Dynamic Private Group PSK: A user uses one passphrase from the list, and is assigned to the corresponding VLAN ID and ARP." (p326-330)

> "Encryption AUTO_WPA_WPA2 is NOT supported (with Device Specific PSK); PSK/PassPhrase: only active with 'Prefer Device Specific PSK'" (p327)

## I · 方法论骨架

**1. 认证选型（信任梯度从低到高）**
Open+Captive Portal（无加密、兼容一切，访客）< MAC 认证（可伪造、无加密，仅哑终端）< PSK（简单但全员共钥）< 802.1X（最强、可管理可扩展，需 RADIUS）。产品级组合：哑设备用 DSPSK/PPSK，人员用 802.1X。

**2. Usage 模板映射（Cirrus 选 Usage 即套模板）**

| Usage | 安全模型 |
|---|---|
| Guest Network | Open 或 MAC + 门户 |
| Employee BYOD Network | 802.1X 或 MAC + BYOD 门户 |
| Enterprise Network for Employees | 802.1X |
| Protected Network | PSK（+可选门户） |

**3. 三段式创建流程（所有 SSID 复用）**
1. SSID Settings：Profile 名/广播名/Usage/认证策略/默认 VLAN/可选 ACL-QoS
2. Network Assignments：选 Site + 一个或多个 AP Group
3. Schedule & VLAN Mappings：按组设调度 + 映射（单 VLAN / VLAN 池 ≤256 避免大广播域 / Guest 隧道）
前置顺序固定：先建 VLAN 与三层接口再回来映射。

**4. PSK 密钥体系四级选型（运维粒度递进）**
1. 全局 PSK：一钥全员
2. DSPSK：MAC 认证 + Company Property 库按 MAC 发专属口令；Force=取消全局口令，Prefer=保留兜底
3. PPSK：多条"名称+口令+ARP"条目，用哪条落哪个角色
4. 动态 PPSK：口令条目直接绑 VLAN ID + ARP（同一 ARP 复用多 VLAN），配 Priority ARP/VLAN-ID 选归属

**5. 三种 SSID 的关键开关**
- Employee：WPA2_AES + UPAMRadiusServer + Auth Source=Local Database（或外部 RADIUS）+ Web Auth=None；客户端 PEAP/MSCHAPv2；UPAM 常数 1812/1813、重试 2、超时 5s
- Guest：Captive Portal=YES（OV-UPAM 型）+ Allow All EAPs=Yes + Auth Source=None + Web Auth=Guest；Guest Access Strategy 定登录方式（账号/接入码/条款/自注册+审批）与 Post Portal Enforcement；Guest Tunneling=按 ARP 建 L2 GRE 隧道，可加备份隧道
- BYOD：SSID 级 VLAN=Guest VLAN（预认证沙箱）→ BYOD Strategy 的 Post Portal Enforcement 绑 ARP（内配 Employee VLAN）→ 认证后从 VLAN30 切 VLAN20
- Express 内嵌版：门户三选一（账号/接入码/条款，大小写敏感）；AP 内置 DHCP 三步：Network 配 IP → 建 Pool → Bind Network 才生效

**6. 客户端接入排障两套命令链（AP CLI，support/aos2016）**
- 802.1X：`iwconfig` / `iwlist channel|txpower|bitrate` → `ssudo sta_list`、`ssudo wlanconfig athX list`、`ssudo wam_debug sta_list`（JSON 含 VLAN/ARP/各阶段认证结果）→ `cat /proc/kes_syslog | grep <MAC>` → 核对 `/var/config/wlanservice.conf`、`AAA_profile.conf`、`AAA_server.conf` → `tcpdump -i br-wan -s 0 host <radiusIP>`
- 门户：`date`（账号有效期）→ `cat /etc/resolv.conf`（DNS 必需）→ `ps | grep eag` → `eag_cli show user all` / `eag_cli kick user index N` → `tail -f /tmp/log/eag.log`

## A1 · 书中案例（Lab 步骤精要）
- **c13/p332-347**：VLAN20 建好并 tagged → IP 接口 int_employees 192.168.20.7/24（IP Forward）→ SSID EmployeesX（Enterprise/802.1X/WPA2_AES）→ 建 Employee 账号 → VLAN 映射 20 → 树莓派 PEAP 连接拿 20.x → Authentication Records + Clients 监控 → 全套 CLI 排障。
- **c15/p372-388**：VLAN30 + int_guests → GuestsX（Guest Network + OV-UPAM Portal + Allow All EAPs）→ 建 Guests_OVX 策略 + 门户模板（Login By Username&Password）→ 连接后开 http://2.2.2.2 触发重定向 → Kick Off 练习 → eag 排障链。
- **c16/p389-395**：BYODX → My_BYOD_Strategy → Post Portal 建 ARP Employee_BYODX（VLAN 20）→ SSID 级映射 VLAN30 → 认证后 Clients 里 VLAN 变 20。
- **c14/p324-330**：PSK 四方案逐屏配置样例（含 Priority VLAN-ID over ARP 语义验证）。
- **c05/c06/p144-157**：Express 版员工/访客 SSID + AP 内置 DHCP（40 地址池=40 并发）。

## A2 · 触发场景（含与相邻 skill 的区分）
- 要为员工/访客/自带设备开通无线接入、按设备类型选认证与密钥体系、客户端连不上做认证侧排障时用。
- **区分**：只做模式/网络底座 → `express-mode-bootstrap`；设备上云 → `device-cloud-onboarding`；认证后的限权/限速/配额 → `upam-policy-bandwidth`；本 skill 管"身份如何进门"。

## E · 可执行步骤
1. 按终端类型沿信任梯度选认证；Cirrus 上用 Usage 模板起步。
2. 先建 VLAN + 三层接口（2360 等 R5 交换机控制台手配）。
3. 三段式建 SSID，按身份类型设关键开关（见骨架 5）。
4. PSK 场景按运维粒度选级：设备级 DSPSK、组级 PPSK、按 VLAN 隔离选动态 PPSK；DSPSK 统一 WPA2/WPA3 明确加密。
5. 建 RADIUS 认证源（内嵌 UPAMRadiusServer 或外部），账号配好有效期。
6. 验证：客户端拿对应 VLAN 地址；Authentication Records / Captive Portal Records / Clients 三张表核对。
7. 连不上按两套 CLI 链排查（骨架 6）。

## B · 边界与陷阱
- DSPSK 与 AUTO_WPA_WPA2 互斥；全局 PSK 字段仅 Prefer 模式可填（ce20）。
- MAC/共享 PSK 安全弱点：MAC 可伪造、共钥泄露即全网失守且无法按人撤销——哑设备用 DSPSK/PPSK，人员用 802.1X（ce21）。
- 门户排障三查：AP 时间（date）、DNS（resolv.conf）、必须访问非 https URL 才触发重定向；树莓派/Debian 不会自动弹浏览器（ce22）。
- 802.1X 失败先查三个 .conf（UPAM 地址/密钥由云下发，Provisioning 未生效时 AP 配置为空而界面看不出），最后 tcpdump 抓 RADIUS（ce23）。
- AP 内置 DHCP 池=并发上限（40 地址=40 台），"部分新设备连不上"先查 IP 再查无线（ce37）。
- Express 门户账号大小写敏感；访客账号有起止日期，依赖 AP 时间正确。

---
来源条目: f10, f11, f12, f13, f23, f28, p18, p19, p20, p21, p33, p34, p35, p36, p37, p38, p39, p40, p41, p42, p43, c05, c06, c13, c14, c15, c16, ce20, ce21, ce22, ce23, ce37 · 术语锚点: g01, g11, g13, g17, g19, g21, g25, g26, g39, g42, g53
