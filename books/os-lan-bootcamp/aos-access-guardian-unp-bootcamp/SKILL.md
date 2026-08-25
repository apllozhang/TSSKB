---
name: Access Guardian / UNP 准入与 IoT 画像
description: 需要配置 OmniSwitch Access Guardian 端口自动感知认证、UNP 用户网络档案（RADIUS Filter-ID 下发）、分类规则与降级链、Captive Portal、Location/Period 策略或 IoT 设备画像（DHCP 指纹/MAC OUI）时使用本技能。
source_book: DT00CTE120 OmniSwitch R6/R8 Bootcamp Issue 25
---

## R（触发场景）
- 同一端口混接 802.1X 主机、打印机、访客设备，需要自动感知分类
- 用户认证后 VLAN/QoS/ACL 档案随人走（UNP）
- 无 supplicant 设备用 MAC 认证；认证失败要走降级链（分类规则/默认 UNP/Captive Portal/阻断）
- 按接入位置或时间窗限制角色（Location/Period 策略）
- IoT 设备自动识别（DHCP Option 55/60 指纹 + MAC OUI）并自动指派档案

## I（核心理念）
Access Guardian 的核心是"端口自动感知多客户端认证"：同一口上自动检测 802.1X 与非 802.1X 设备（P120，<<<PAGE 630>>>）。身份的载体是 UNP（Universal Network Profile）= VLAN + QoS/ACL 策略列表 +（R8 加 Location/Period），档案随用户动态应用到端口（P121，<<<PAGE 631>>>）。下发路径：RADIUS Access-Accept 的 Filter-ID 携 UNP 名；无返回时走降级链——分类规则 → 默认 UNP → Captive Portal → 阻断（P122/F10，<<<PAGE 632, 635-638>>>）。R8 端口分类规则有 16 级固定优先序（Port > Port+VLAN tag > Domain 组合 > MAC > OUI > Range > LLDP > Auth-type > IP > VLAN tag）（P124，<<<PAGE 638>>>）。IoT 画像三组件：本地签名收集器 + 本地 profiler + UNP 画像，识别后自动指派 UNP（P127/P128/F11，<<<PAGE 686-690>>>）。

## A1（决策/选型）
1. 认证方式：802.1X（有 supplicant）vs MAC 认证（交换机以源 MAC 为用户名/密码构造 RADIUS 请求，P123，<<<PAGE 633>>>）vs 免认证纯分类
2. R6 路线：mobile 口 + 802.1x enable + `aaa classification-rule … user-network-profile`；R8 路线：`unp port … port-type BRIDGE` + `unp classification …`（P120/C33，<<<PAGE 630, 642-677>>>）
3. Captive Portal 用于 Web 认证引流，注意它是终结策略（X61，<<<PAGE 1014>>>）

## A2（操作步骤）
1. UNP 配置五步（P125，<<<PAGE 640>>>）：分类规则 → 认证服务器 → 设备分类策略 → UNP 档案 → 端口
2. 端口准备：R6 `vlan port mobile 3/1` + `vlan port 3/1 802.1x enable`；R8 `unp port 1/1/1 port-type BRIDGE`（C33，<<<PAGE 642-677>>>）
3. UNP 策略列表：`policy list list_name type unp`；R6 `aaa user-network-profile name profile_name policy-list-name list_name` / R8 `unp profile profile_name qos-policy-list …`；VLAN 映射 `unp profile profile_name map vlan vlan_id`（C33，<<<PAGE 642-677>>>）
4. 分类规则（R8）：`unp classification mac-address 00:11:22:33:44:55 port 1/1/5 PROFILE1 Pr1`、`unp classification mac-oui 00:11:22 PROFILE1 myProfile1`、`unp classification lldp med-endpoint ip-phone p PROFILE1 myProfile1`、`unp classification authentication-type 802.1X/MAC …`（C33，<<<PAGE 642-677>>>）
5. RADIUS 档案：`aaa profile ap-1` → `aaa profile ap-1 device-authentication mac rad1 rad2` / `device-authentication 802.1x rad1 rad2` → `unp port 1/1/5 aaa-profile ap-1`（可按 linkagg/范围）；联调 `aaa test-radius-server My_radius type authentication user employee password password`（C33/P207，<<<PAGE 642-677>>>）
6. Location/Period 策略：`system location <string>` + `unp policy validity-location "Alcatel" port 1/1/10`；`unp policy validity-period "Office-Time" days MONDAY time-zone CET hours 9:00 to 17:00`（C34/P126，<<<PAGE 649-650>>>）
7. IoT 画像：启用签名收集（DHCP Option 55/60）与本地 profiler，比对签名库后自动指派 UNP；维护已知/未知设备库供补录（F11，<<<PAGE 686-690>>>）

## E（实证案例）
- C33 AG 部署：R6/R8 双语法 + MAC/OUI/LLDP 分类规则 + RADIUS 档案 + test-radius-server 联调（<<<PAGE 642-677>>>）
- C34 Location/Period 策略：按位置与办公时间窗限制（<<<PAGE 649-650>>>）

## B（反例与坑）
- Captive Portal/Profile/Block 是终结策略，后面不能跟其他策略（X61，<<<PAGE 1014>>>）
- 6450 可对 UNP 直接限速，R8 不行——R8 限速要放在 QoS 策略列表里（X60，<<<PAGE 676>>>）
- R6 需 mobile+802.1x 口才能跑 AG，普通静态口不行（P120，<<<PAGE 630>>>）
- 认证排障先 `aaa test-radius-server` 验证服务器连通，再看 Filter-ID 是否返回（<<<PAGE 677>>>）
- Location/Period 不满足时自动转未授权角色——时段策略变更要预留维护窗口（P126，<<<PAGE 649-650>>>）

## 来源
- principles·P120-P128/P207；frameworks·F10/F11；cases·C33/C34；counter-examples·X60/X61
