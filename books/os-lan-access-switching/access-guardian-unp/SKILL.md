---
name: access-guardian-unp
description: 何时用：在 OmniSwitch 上做动态 VLAN（UNP 分类）、802.1X/MAC 准入认证（Access Guardian）或 LLDP 邻居发现时。
source_book: DT00XTE215EN Access Switching
---

# 接入安全与准入：UNP / Access Guardian / LLDP

## R · 原文引用

"-> aaa radius-server my_radius host 192.168.100.102 key alcatel-lucent / -> aaa authentication 802.1x my_radius / -> unp profile corporate / -> unp profile corporate map vlan 20 / -> unp port 1/1/1 port-type bridge / -> unp port 1/1/1 default-profile def_unp"（p389）

"UNP Port classification rules: 1. Port/Linkagg 2. Domain 3. MAC address 4. MAC-OUI 5. MAC address range 6. LLDP 7. Auth-type 8. IP address 9. VLAN tag. Precedence: Extended rule > Binding Rule > Simple Rule"（p129-132）

"IEEE 802.1AB - Link Layer Discovery Protocol (LLDP) / L2 discovery protocol / Enabled by default on the OmniSwitches. LLDP is configured at port level (or NI or chassis), but not at linkagg level."（p409/423）

## I · 方法论骨架

- **UNP（User Network Profile）**：一个 profile 聚合 VLAN 映射 + QoS/ACL 策略列表 + 位置/时段策略；由分类规则或 RADIUS Filter-Id 命中后套到端口上的用户。分类规则 9 级次序匹配（Port/Linkagg 最先、VLAN tag 最后），组合优先级 Extended > Binding > Simple。
- **Access Guardian** = UNP + 802.1X/MAC 认证：端口自动识别 supplicant（802.1X）与非 supplicant（MAC），RADIUS 以 Filter-Id 返回 profile 名自动套用；服务器不可达走 auth-server-down profile。
- **LLDP**（802.1AB）默认收发双开，TLV 交换邻居信息；LLDP-MED 面向话机（Network Policy TLV 下发 VLAN+L2 优先级+DSCP）。配置层级只有端口/槽位/整机。

## A1 · 书中案例（Lab 配置精要）

- **Access Guardian 完整流（p397-406）**：`aaa radius-server my_radius host 192.168.100.102 key alcatel-lucent` + `aaa device-authentication 802.1x my_radius` + `aaa accounting mac my_radius`；ACL 规则装 `policy list deny_employees type unp enable`；`unp profile UNP-employee qos-policy-list deny_employees` + `map vlan 20`（contractor→vlan 30）；端口 `unp port 1/1/1 802.1x-authentication` + `mac-authentication`。客户端启 PEAP-MSCHAPv2 后 `unp user flush port 1/1/1` 重认证：employee 进 VLAN20+角色、contractor 进 VLAN30；RADIUS 无条目则 Status=Block。`aaa test-radius-server my_radius type authentication user …` 独立验证服务器。
- **动态 VLAN（p133/p144-157）**：`unp profile employee` + `map vlan 40` → `unp classification mac-address 00:50:56:90:ee:0a profile1 employee` → `unp port 2/1/1 port-type bridge` → `unp user flush port 2/1/1` → show unp user 见端口自动进 VLAN 40（unpUntag）。
- **LLDP（p422-426）**：`lldp port 1/1/3 notification enable` + `tlv management port-description enable`；chassis 级开 system-name/system-description/management-address；show lldp remote-system 对比开 TLV 前后（System Name 从 (null) 变 Pod20sw7）。

## A2 · 触发场景（含与相邻 skill 的区分）

- 端到端口按人/设备身份动态分 VLAN、上准入认证、邻居发现/话机策略下发——本 skill。
- 静态划 VLAN/trunk（不按身份）→ vlan-link-redundancy。
- 认证后的 ACL/QoS 规则本体语法 → qos-acl-policy（本 skill 管"挂到 profile"这层）。
- 管理员登录交换机的 AAA（ASA）→ switch-management-access。

## E · 可执行步骤

动态 VLAN（免认证）：
1. 建 VLAN（vlan 20）。
2. `unp profile <名>` → `unp profile <名> map vlan 20`。
3. 兜底：`unp profile def_unp` + map vlan 10。
4. `unp classification-rule <规则> mac-address-range <起> <止>`（或 MAC/OUI/IP/LLDP 等）+ `… profile1 <名>`。
5. `unp port <口> port-type bridge` + `unp port <口> default-profile def_unp`。
6. `unp user flush port <口>` → `show unp user` 验证。
Access Guardian：
1. 声明 RADIUS：aaa radius-server …；挂认证：aaa authentication 802.1x / aaa device-authentication 802.1x、aaa accounting mac。
2. 建 VLAN + UNP profile（map vlan、可挂 qos-policy-list/location-policy）。
3. 端口 port-type bridge + 802.1x-authentication / mac-authentication + default-profile（兜底）。
4. 可选 port-template 批量下发认证参数与 pass-alternate profile。
5. 验证：aaa test-radius-server → unp user flush → show unp user [status|details]。
LLDP：
1. `lldp port <口> notification enable`；按需开管理 TLV（system-name/management-address 等，chassis 级）。
2. `show lldp remote-system` / `show lldp statistics` 验证。

## B · 边界与陷阱

- **LLDP 不能配在 linkagg 级**：只能端口/槽位/整机，聚合口要逐成员口配。
- 分类规则组合优先级固定（Extended > Binding > Simple），规则次序 Port 最先、VLAN tag 最后——诊断"为什么命中了别的 profile"按此链查。
- RADIUS 无 MAC 条目时用户直接 Block，不是超时重试；先 aaa test-radius-server 定位。
- 认证关闭或失败时 UNP 分类规则直接作用于端口流量（default-profile 兜底别忘配，否则端口行为漂移）。
- Mobile Tag：普通 802.1Q 只能配固定端口，mobile 口收 tagged 流需 UNP profile mobile-tag。
- unp user flush 是重分类/重认证的触发器，改完规则不 flush 看不到变化。

---
来源条目: f07, f13, p21, p40, c14, c15, ce14, g18, g19, g21, g36
