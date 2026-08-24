---
name: employee-ssid-8021x
description: 何时用：在 OV2500 上为员工创建 802.1X SSID（含向导/专家模式、UPAM 本地库或 AD 外部认证）及空口优化。
source_book: DT00XTE368EN Stellar WLAN Enterprise Basic
---

# Employee SSID 与 AD 认证（802.1X / PEAP）

## R · 原文引用

> "Step 1 Create SSID: Name the SSID Service; Name the SSID; Select the SSID Usage. Step 2 Customize SSID: Basic Parameters, Allowed Band... Security Settings; Default VLAN/Network; ACL/QoS rules; Authentication Strategy. Step 3 AP Group Assignment & Schedule." (p283-289)

> "Enterprise Network for Employees: 802.1X." (p284)

> "Select UPAM > SETTINGS > LDAP/AD Configuration: LDAP/AD Server: Enable; Server Type: AD; NETBIOS Domain Name: COMPANY... Click on Test Connection... Select External LDAP/AD > Apply." (p326-331)

## I · 方法论骨架

1. **向导三步**：命名/选 Usage（模板决定认证+门户组合）→ 定制（频段/加密/默认 VLAN 或 VLAN 池/Access Role/认证策略）→ 绑 AP Group + 广播排程。
2. **Usage 模板矩阵**：Employee 企业网=纯 802.1X；Employee BYOD=802.1X/MAC+BYOD 门户；Guest=Open/MAC+门户；Protected=纯 PSK。
3. **专家模式七步**（对象模型）：WLAN Service → AAA Server Profile → Access Role Profile（映射 VLAN）→ Authentication Strategy → Access Policy → 本地员工账号 → 下发 AP Group。
4. **认证源解耦**：SSID 与 VLAN 不动，认证策略可从 UPAM 本地库一键切到 External LDAP/AD。
5. **VLAN Pooling**：高密场景用 VLAN 池避免单一大广播域。

## A1 · 书中案例（Lab 精要）

- c05：建 EmployeesX——Usage 选 Enterprise Network for Employees，2.4+5 GHz，WPA3_AES，RADIUS=UPAMRadiusServer，账号 Employee/password（UPAM > Authentication > Employee Account，支持 xls/csv 批量导入），VLAN 20，绑 APGX。验证：树莓派 PEAP/MSCHAPv2/不校验 CA，IP 落 10.7.X.32/27。内置 NAS 条目 All Managed Devices 共享密钥 123456。排障：`ssudo sta_list`/`wam_debug sta_list` 看 JSON（含 assignedVLAN/assignedAR）、`cat /var/config/wlanservice.conf` 与 `AAA_server.conf` 核对 1812/1813，必要时 tcpdump 抓 RADIUS。
- c06：接 AD——UPAM > SETTINGS > LDAP/AD 声明域控（类型 AD、NETBIOS/DNS 域名、域控 IP、端口 389），Test Connection 通过再 Apply；SSID 认证源改 External LDAP/AD；客户端清已存网络后用 AD 凭据重连。

## A2 · 触发场景（含与相邻 skill 的区分）

- 员工/内部终端的安全 SSID 与认证源切换——用本 skill。
- 访客门户/带宽/内容过滤——转 upam-guest-access；AP 尚未注册受管——先走 enterprise-mode-onboarding。

## E · 可执行步骤

1. 建业务 VLAN（如 VLAN 20 EMPLOYEES），核心交换机配 IP 接口。
2. 向导建 SSID：Usage=Enterprise Network for Employees，频段按需，加密优先 WPA3_AES（混合终端可 WPA2_AES）。
3. 认证策略选 UPAMRadiusServer；本地库用 Manage Employee Accounts 建号或批量导入。
4. 设默认 VLAN/VLAN 池，Save and Apply to AP Group，把 SSID 从 default 组改绑目标组。
5. 接 AD：LDAP/AD Configuration 声明域控 → Test Connection → Apply → SSID 认证源改 External LDAP/AD。
6. 客户端以 PEAP + MSCHAPv2 验证；用 WLAN > Client List 与 UPAM Authentication Record 确认。
7. 空口优化（Advanced WLAN Service）：广播密钥轮换（Enterprise 级，默认 15 min）、Broadcast Filter ARP、组播优化（利用率 90%/客户端 6 上限自动停）；WMM 映射按推荐表（Voice=1p5/DSCP46-EF，Video=1p4/34-AF41）。

## B · 边界与陷阱

- 混合 WPA2/WPA3 终端网慎开 CNSA（开启后仅 WPA3 可入）。
- AAA Profile 在 Enterprise 与 Personal 级都是必填，漏配直接失败。
- 改认证源后客户端要清掉已存网络重连，否则沿用旧凭据误判失败。
- RADIUS 走 IPv4（即使管理面已 IPv6）。
- 加密枚举要与终端能力匹配（含 TKIP 的老选项仅作兼容）。

---
来源条目: f09, f10, p25, p26, p27, p33, p34, c05, c06, g24, g35, g36, g44
