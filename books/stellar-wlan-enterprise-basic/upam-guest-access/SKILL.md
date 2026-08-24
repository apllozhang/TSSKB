---
name: upam-guest-access
description: 何时用：建 Guest SSID（门户/踢线/黑名单）、配用户角色带宽控制、Unified Policy 限制与 WCF 网页过滤时。
source_book: DT00XTE368EN Stellar WLAN Enterprise Basic
---

# UPAM Guest 与用户角色（门户 / 带宽 / 策略 / WCF）

## R · 原文引用

> "Create a Guest SSID with the usage Guest Network; Activate the Captive portal option; Select the RADIUS server in the Authentication Strategy; Create a Guest account if the UPAM internal RADIUS server is used... Assign a VLAN to the Guest SSID." (p343)

> "Matches a DPI application in the Policy List? Y: Application Specific BW... N: Matches an ACL?... N: Access Role set with BW Control? Y: User BW... N: SSID set with BW Control? Y: Shared BW... N: No BW Limitation." (p364)

> "Stellar AP DNS Snooping: 1. DNS request FQDN... 2. FQDN filtered? 3. FQDN category?... 5. Create Block ACL rule to IP of the FQDN... No DNS -> WCF not in Service." (p366-367)

## I · 方法论骨架

1. **Guest 工作流**：Guest Usage 建 SSID → 勾强制门户 → 认证选 RADIUS（内置 UPAMRadiusServer）→ 建 Guest 账号（可配数据配额）→ Guest Access Strategy 定登录方式与 Post Portal 角色 → 绑 Guest VLAN。
2. **带宽四级判定链**（细→粗）：DPI 应用规则 → ACL 规则 → Access Role 按用户 → SSID 射频共享；设计限速按此反推放哪层。
3. **User Role = Policy List**：有序规则（Accept/Drop、限速、802.1p/DSCP、DPI），双向执行；来源 RADIUS 或 Access Role Profile 默认。
4. **WCF 链路**：AP DNS 嗅探 → OV2500（Brightcloud）查类目 → 回发 AP 生成阻断 ACL 本地拦截；Profile 绑 Access Role（一对一）。
5. **UPAM 边界**：Guest/BYOD 许可均按接入设备数计，与账号数无关。

## A1 · 书中案例（Lab 精要）

- c07：建 GuestsX（Usage=Guest Network、OV-UPAM 门户、VLAN 30），访客 Guest/password；客户端访问任意非 HTTPS URL（http://2.2.2.2）触发门户重定向。管控：UPAM > Guest Device 踢线 KickOff；WLAN > Client List 拉黑 Blocklist。
- c08：Unified Policy 拒 telnet/SSH——建 Service Group（TCP23/22）→ Policy 动作 QoS Disposition=DROP → Policy List 顺序 DeniedServ + OV-L3-AcceptAllPolicy → 塞进访客角色 __GuestsX → Apply to Devices（VLAN 30，OS6870+APGX）。
- c09：WCF-guests 拒 Social Networking 与 Gambling 类目，绑 __GuestsX 后必须 Apply to Devices 才推到 AP；google.com 通、facebook.com 拒。

## A2 · 触发场景（含与相邻 skill 的区分）

- 访客上网、门户认证、访客限速/内容过滤、策略下发——用本 skill。
- 员工 802.1X SSID——转 employee-ssid-8021x；访客流量集中隔离的 GRE 隧道在分支场景——与 rap-remote-deployment 的 GRE 条目配合。

## E · 可执行步骤

1. 建 Guest VLAN（如 VLAN 30），核心交换机配 IP 接口。
2. 向导建 GuestsX：Usage=Guest Network，勾 Captive Portal（类型 OV-UPAM），频段 2.4+5。
3. Manage Guest Accounts 建访客账号（可设 Data Quota 与有效期）。
4. Guest Access Strategy：门户页、登录方式（账密/接入码/条款）、Post Portal 角色；默认 VLAN 30，绑 AP Group。
5. 限速设计：访客按人限速放 Access Role 级；SSID 级做整体兜底；精确应用用 DPI 规则。
6. 策略限制：Unified Policy 建条件（如 L4 Services）+动作（DROP/限速/标记）→ 组 Policy List（拒绝规则在前、AcceptAll 兜底）→ 绑 Access Role Profile → Apply to Devices → Notify All。
7. WCF：AP Group 勾启用 WCF → 建 WCF Profile 设类目 Reject → 绑访客角色 → Apply to Devices → 验证 Profile 页运行状态为 in service。

## B · 边界与陷阱

- OV2500 必须配 DNS，否则 WCF 停在 Not in service、连不上 Brightcloud——验收第一步看状态。
- AP1101/AP1201H 不支持 WCF；WCF Profile 与 Access Role 一对一。
- 策略在认证成功时套用：改完必须断开重连强制重认证，否则误判"没生效"。
- 访客账号有有效期：OV2500 与 AP 时间不同步会导致"没过期却登不上"，两侧 `date` 核对，根治配 NTP。
- 门户重定向需 HTTP 触发（访问 HTTPS 站点不会跳门户）。
- Unified Policy 部分特性仅 OS6870 与 AP 支持（OS2360/6360 不支持）。

---
来源条目: f11, f12, p28, p29, p30, p39, c07, c08, c09, ce14, ce15, ce16, g29, g30, g37, g38, g43, g45
