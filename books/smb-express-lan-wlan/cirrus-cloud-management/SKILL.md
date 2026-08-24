---
name: Cirrus 云管上线与 SSID 下发
description: 当需要把交换机或 Stellar AP 上云（OmniVista Cirrus）、排查激活状态机、或在云管下创建员工 802.1X / 访客 Portal SSID 时使用。
source_book: DT00XTE310 OmniSwitch LAN Access & OmniAccess Stellar WLAN Express
---

## R（触发场景）
- 交换机/AP 要注册到 Cirrus 云管平台，call home 迟迟不上线
- Cirrus 激活状态卡在中间态或报 Failed，需要对照状态机排障
- 云管下要创建带 802.1X（UPAM RADIUS）的员工 SSID 或访客 Captive Portal SSID

## I（核心理念）
云管上线是一条"许可证→订阅→组织/站点→SN 宣告→call home→OV Managed"的流水线，每一步中间态（Registered / Obtaining Certificate / VPN Configuring…）都有明确定义。SSID 下发共用五步向导，用户策略通过 ARP（Access Role Profile）三级优先级裁决。

## A1（行动框架）
1. **订阅准备**：License（如 OVCX-68-BAS-3Y：BASE 级 / 3 年）→ eBuy → OVC Subscription Manager 导入 Subscription ID + Activation Code（<<<PAGE 285>>>-<<<PAGE 312>>>）。
2. **交换机上云**（<<<PAGE 353>>>-<<<PAGE 364>>>）：
   - 确认 `ls /flash/working` 有 cloudagent.cfg（缺则 `cp /flash/cirrus/cloudagent.cfg /flash/working/`，<<<PAGE 356>>>）；
   - 建管理 VLAN 与 IP：`vlan 1305 name SW-MANAGEMENT`、`ip interface "int_sw-mgmt" address 10.130.5.5/24 vlan 1305`、`ip static-route 0.0.0.0/0 gateway 10.130.5.7`；
   - 辅助服务：`snmp security authentication all`、`ntp client admin-state enable`、`ip name-server 9.9.9.9`、`ip domain-lookup`；
   - `cloud-agent admin-state enable`；
   - Cirrus 建 Site/Building/Floor → Device Catalog 用 `show chassis` 的 SN 建 Device；
   - 强制 call home：`cloud-agent admin-state disable force` + `enable` → `show cloud-agent status` 看 DeviceManaged/completeOK。
3. **AP 上云 Provisioning**：AP Console `showsysinfo` 取 SN → Device Catalog 建 Stellar AP（Do Not Upgrade）→ Create AP Group → Create Provisioning Configuration（Name/Site/Default RF Profile/Timezone）→ `ocloud_show` 验证 VPN Status connected（<<<PAGE 369>>>-<<<PAGE 375>>>）。
4. **员工 SSID（802.1X）**：Wireless > SSIDs > Create（Usage: Enterprise Network for Employees (802.1X)，WPA2_AES）→ RADIUS Server=UPAMRadiusServer → 建 Employee 账号 → Access Policy Local Database → Network Assignments 选 AP Group → VLAN/Tunnel Mapping=VLAN 20 → 客户端 PEAP/MSCHAPv2 连接验证 → Network > Access Records > Authentication Records 查认证记录（<<<PAGE 407>>>-<<<PAGE 414>>>）。
5. **访客 SSID**：Create Guest Access Strategy（含 Captive Portal Template：Layout）→ Login By: Username & Password → 建 Guest 账号 → 映射 VLAN 30 → 客户端 http 跳转认证 → 需要时 Kick Off：Network > Analytics > Clients > Actions > Kick Off（<<<PAGE 437>>>-<<<PAGE 443>>>）。

## A2（进阶应用）
- **激活状态机排障**（<<<PAGE 327>>>-<<<PAGE 328>>>）：中间态 Registered / Obtaining Certificate / Upgrade / Assigned / VPN Configuring / Connected to OV → OV Managed；失败态含 Failed To Get Certificate、Upgrade Failed、Configuring VPN Failed、Provisioning Failed、Device Validation Failed、Factory Reset Required（VPN profile 变更需恢复出厂）。
- **ARP 三级优先级**：外部 RADIUS/LDAP Filter-ID 下发的 ARP > 认证策略内 ARP > SSID 默认 ARP（__SSIDname）（<<<PAGE 394>>>、<<<PAGE 400>>>-<<<PAGE 403>>>）。ARP 内容 = VLAN tag / QoS policy / 防火墙 ACL / L7 规则 / 位置 / 时段。
- **DHCP option 138/43**：DHCP Server 通过 option 138/43 把管理平台 IP 告知 AP（<<<PAGE 280>>>、<<<PAGE 377>>>）；DHCP proxy 场景注意透传 129-133/138。
- **云管 VLAN 可视化**：Cirrus 建 VLAN20 时可 GUI 点选 6360 端口 tagged，但 OS2360 等仍需手工 CLI（<<<PAGE 407>>>-<<<PAGE 414>>>）。

## E（实证案例）
- 交换机 Onboarding 全流程：cloudagent.cfg 检查 → 管理 VLAN/静态路由/SNMP/NTP/DNS → cloud-agent enable → Device Catalog 建 Device → disable force/enable 强制激活 → completeOK（<<<PAGE 353>>>-<<<PAGE 364>>>）。
- 员工 802.1X SSID 全流程：UPAM RADIUS + Employee 账号 + VLAN 20 映射，客户端 PEAP/MSCHAPv2 拿到 192.168.20.7x（<<<PAGE 407>>>-<<<PAGE 414>>>）。
- 访客 Portal + 踢下线：Captive Portal 模板 → Guest 账号 → VLAN 30 → Kick Off 操作（<<<PAGE 437>>>-<<<PAGE 443>>>）。

## B（边界与陷阱）
- **OVC4→OVC10 迁移**：设备序列号不能同时声明在两个平台，先在 OVC4 删除全部设备再到 OVC10 宣告；AP 最长等 30 分钟 call home，交换机 30 分钟或重启 cloud-agent（<<<PAGE 318>>>）。
- **call home 慢**：优先 `cloud-agent admin-state disable force` + `enable` 手动强制，而非整机重启（<<<PAGE 331>>>、<<<PAGE 363>>>）。
- cloudagent.cfg 缺失需手工从 /flash/cirrus 拷到 /flash/working（<<<PAGE 356>>> Warning）。
- 不要在 Organization 上用 Delete 动作（<<<PAGE 358>>>）。

## 来源
- frameworks·F7 Cirrus 上线流程（<<<PAGE 285>>>-<<<PAGE 315>>>、<<<PAGE 272>>>）
- frameworks·F8 激活状态机（<<<PAGE 327>>>-<<<PAGE 328>>>）
- frameworks·F9 SSID 五步向导（<<<PAGE 383>>>、<<<PAGE 390>>>、<<<PAGE 423>>>、<<<PAGE 431>>>）
- frameworks·F10 ARP 优先级裁决（<<<PAGE 394>>>、<<<PAGE 400>>>-<<<PAGE 403>>>）
- principles·P36 DHCP Option 138/43（<<<PAGE 280>>>、<<<PAGE 377>>>）
- cases·C17 交换机上云（<<<PAGE 353>>>-<<<PAGE 364>>>）
- cases·C18 AP 上云 Provisioning（<<<PAGE 369>>>-<<<PAGE 375>>>）
- cases·C20 员工 802.1X SSID（<<<PAGE 407>>>-<<<PAGE 414>>>）
- cases·C21 访客 SSID + Kick Off（<<<PAGE 437>>>-<<<PAGE 443>>>）
- counter-examples·X7 序列号双平台冲突（<<<PAGE 318>>>）
- counter-examples·X8 强制激活（<<<PAGE 331>>>、<<<PAGE 363>>>、<<<PAGE 356>>>）
