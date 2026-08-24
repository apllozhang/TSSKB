---
name: stellar-enterprise-onboarding
description: 何时用：需把 OmniSwitch 与 Stellar AP 纳入 OmniVista 2500 本地网管（Enterprise 模式上线/发现/注册排障）时。
source_book: DT00XTE378EN Stellar WLAN Adv Troubleshooting & Update
---

# Enterprise 设备上线工作流：交换机发现 + AP 云注册 + AP Group 纳管

## R · 原文引用

> "The Stellar Access Points that we are going to use during this training need to: Receive an IP Address from the DHCP Server > IP DHCP Relay; Forward the Wi-Fi clients traffic to a default route > Static route; Have the switch interface where they are connected enabled; Receive power from the OmniSwitches > The Power over Ethernet (PoE) feature must be enabled." (p213)

> "The DHCP Server will then send a DHCP Offer with the option 138 (IP address of the OmniVista 2500). Once this option received, the Stellar Access Point will work in Enterprise mode." (p224-239)

> "OS6870, OS6360, OS2360: -> user snmpuserv3 read-write all password \"Superuser=1\" sha+des -> snmp station 10.130.5.5X 162 snmpuserv3 v3 enable" (p213-223)

> "Warning: DO NOT CHOOSE THE COUNTRY CODE USA, JAPAN OR ISRAEL AS THE STELLAR ACCESS POINTS USED IN THE REMOTE LAB ARE NOT COMPATIBLE WITH THESE COUNTRY CODES." (p231)

## I · 方法论骨架

四层递进，每层可独立验证后再进下一层：

1. **网络层就绪**：Backbone VLAN 互联管理设备（交换机/OV2500/DHCP），每台交换机配三层 IP 接口，互 ping 验证。
2. **管理通道（交换机）**：全网配 SNMPv3 → OV2500 建同参数 Discovery Profile → 按 IP 段发现。
3. **AP 上线链路**：AP 管理 VLAN → DHCP relay（Offer 带 option 138 = OV2500 地址）→ 静态路由 → 端口启用 + PoE 上电。
4. **纳管**：AP 从 Unmanaged 列表改 Trust 状态 → 加入 AP Group（OV2500 只按 AP Group 管理 AP，配置对组内全部 AP 生效）。

## A1 · 书中案例（Lab 精要）

- **c01 交换机发现**：三台 OmniSwitch 各建 snmpuserv3（SHA+DES），trap 指向 OV2500:162；OV2500 侧 Profile 参数 Timeout 5000/Retry 3，按三个 IP 段 Discover Now。
- **c02 AP 云上线**：VLAN Manager 一次给三台交换机建 VLAN 40（default 口 + Q-tag 级联）；核心 6870 配 DHCP relay 与静态路由；`lanpower slot 1/1 service stop/start` 重启 PoE 逼 AP 注册；Windows DHCP 服务器预定义 Code 138（IP Address 类型）填 OV2500 地址。
- **ce02 国家码坑**：OV2500 首次 AP Registration 选国家码决定信道与功率；教材 AP 与 USA/JAPAN/ISRAEL 区域码不兼容，选错则"设备完好却拒绝工作"。
- **ce03 评估许可坑**：文件导入与密钥手填二选一（Don't do both）；密钥方式只贴 key 部分，整行复制必失败。

## A2 · 触发场景（含与相邻 skill 的区分）

- 新站点部署 / 存量网络纳管 OV2500、AP 不出现在网管、发现失败排障。
- 与 `stellar-ssid-policy-advanced` 的区分：本 skill 管"设备进网管"，SSID/认证/策略在设备纳管之后才做。
- 与 `stellar-rap-backup-upgrade-ops` 的区分：那两个是云管（Cirrus）与远程 AP（RAP）场景；本 skill 只管本地 OV2500 Enterprise 模式。

## E · 可执行步骤

1. 建 Backbone VLAN，各交换机配 IP 接口，双向 ping 通。
2. 交换机 CLI：`user snmpuserv3 read-write all password <pwd> sha+des`；`snmp station <OV2500 IP> 162 snmpuserv3 v3 enable`。
3. OV2500：NETWORK > DISCOVERY > Managed Devices > Discover New Devices，Discovery Profile 与交换机侧参数一致。
4. 建 AP 管理 VLAN；核心交换机配 `ip dhcp relay destination <DHCP IP>` + admin-state enable + 静态路由。
5. DHCP 服务器预定义 option 138 = OV2500 IP。
6. 启用 AP 端口，`lanpower` stop/start 让 AP 重启注册。
7. OV2500 选国家码（务必与 AP 硬件销售区域匹配）与时区；Unmanaged 列表 → Change to Trust Status。
8. 建 AP Group，把 AP Change Group 入组，配置随组下发。

AP 不上线排障分层：二层 `show interfaces` / `show vlan members port` → 三层 `show ip interface`、OV2500 虚机菜单查 IP → AP 串口（support 账号）`getmode`（是否 OV 模式）/`getovinfo`（OV 地址）/tcpdump 抓 DHCP Offer 验 option 138/43 → `show lanpower` 查供电。

## B · 边界与陷阱

- **OV2500 只认 AP Group**：不进组的 AP 不受配置管理，一切"配了不生效"先确认 AP 在组里。
- **国家码 = 区域合规**：跨境调拨/二手设备，出厂区域与网管国家码不一致会假死；先查标签/序列号。
- **评估许可两种导入二选一**；密钥只贴键值不贴整行。
- option 138 是 ALE 私有引导方式，DHCP 服务器不做预定义则 AP 永远拿不到 OV2500 地址。
- 本 skill 不覆盖 IPv6 管理面：Enterprise 模式下 AP 管理只走 IPv4（见 `stellar-wifi7-hardware-rf-quickref` 的模式差异条目）。

---
来源条目: f02, c01, c02, ce02, ce03
