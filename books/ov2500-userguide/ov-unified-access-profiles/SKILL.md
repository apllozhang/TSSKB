---
name: Unified Access 三途径与接入档案体系
description: 需要配置有线/无线统一接入认证（Workflow 引导流/Template 模板/Device Config 单机微调三途径）、Access Auth Profile、Access Role Profile、WLAN Service Profile、Access Classification 分类规则、AAA Server Profile、SPB/VXLAN/Tunnel 映射时使用。
source_book: OmniVista 2500 NMS 4.9R2 User Guide
---

## R（触发场景）
- 园区要做 802.1X / MAC 认证，认证结果映射 UNP + VLAN
- 打印机/IPTV 等静默设备不走认证，要按分类规则给默认角色
- RADIUS 不可达时的兜底角色、COA 换 VLAN 后的 Port Bounce
- 认证/分类结果要映射到 SPB 服务、VXLAN、GRE Tunnel

## I（核心理念）
Unified Access 有三个配置途径：Workflow（六种引导流程：分类规则/802.1X/MAC/802.1X+MAC/MAC+Captive Portal/ClearPass）→ Template（Access Auth/WLAN Service/Access Role/AAA Server 等模板批量下发）→ Device Config（单设备微调）＋Profile Polling 轮询同步。认证分层：L2（802.1X/MAC/分类规则→定 UNP+VLAN，之后不变）→ L3（QMR、MAC 黑名单、位置/时间校验动态改 Policy List/Role）。

## A1（行动框架）
1. **途径选型**（frameworks·F15，<<<PAGE 592>>>）：新场景走 Workflow 向导；标准化批量走 Template；个别设备差异走 Device Config（改动只影响所选设备不回写模板）
2. **L2 认证与分类决策流**（principles·P159，<<<PAGE 591-592>>>）：优先 802.1X，非 supplicant 或禁用时用 MAC；RADIUS 返回有效 UNP→映射 Access Role Profile+VLAN；认证未启用/失败/无有效 UNP 且启用分类→按 Port/Group ID/MAC/LLDP/认证类型/IP 分类规则给 Default UNP；UNP 与 VLAN 一旦分配不再改变
3. **模板清单**（principles·P161，<<<PAGE 593-594>>>）：Access Auth Profile / WLAN Service / Access Role Profile / AAA Server Profile / Location+Period Policy / Access Classification / Customer Domain / SPB / Far End IP / Static Service / VXLAN / Tunnel / Legacy Wireless / Global Configuration

## A2（操作步骤）
- **创建并下发 Access Role Profile**：Unified Profile→Access Role Profile→Add：General（Auth Flag/Mobile Tag/Redirect Status/Policy List/Location+Period Policy/Inactivity Interval）+Bandwidth Control+Client Session Logging+WCF+Walled Garden+Allowed Contacts+CP Attributes→Create→Apply To Devices：Configure Mapping Method（Map to VLAN/SPB/VXLAN/Static Service/Tunnel/VLAN+Tunnel）→Select Devices→Apply（cases·C53，<<<PAGE 608-613>>>）
- **Access Auth Profile 关键机制**：Port Bounce（COA 换 VLAN 后触发 DHCP 重新，无线与 AOS 6x 恒开）；AP Mode 默认开（自动检测 Stellar AP）；Trust Tag 默认关；Bypass VLAN 芯片直通（优先于 Trust Tag，推荐 HD IPTV）；Bypass Status/MAC Allow EAP 组合决定 802.1X 跳过逻辑（principles·P162，<<<PAGE 594-601>>>）
- **无线转发模式**：Tunnel（GRE 到控制器）/Bridge（AP 本地）/Split Tunnel/Decrypt Tunnel；Drop Broadcast/Multicast 与 ARP 转 Unicast 仅限 Tunnel 模式；Band Steering：Force/Prefer（默认）/Band Balancing（principles·P163，<<<PAGE 598-599>>>）
- **WLAN Service 角色分配优先级**：802.1X/MAC 认证返回角色 > Classification Rules（仅当认证未返回或未匹配时）> Default Access Role Profile；ESSID ≤32 字符（principles·P164，<<<PAGE 602-603>>>）
- **AAA Server Profile**：每类服务器可配主+多级备份；无线 CP 主备被忽略；Session Timeout 默认 43200；Inactivity 默认 600（须大于交换机 MAC 老化时间）；所有超时参数修改不追溯已在线用户（principles·P167，<<<PAGE 614-618>>>）
- **Access Classification 规则**：九种类型（MAC/MAC Range/IP Address/VLAN Tag/Location(仅 Legacy AP)/ESSID/DHCP Option/DHCP Option 77/Encryption Type）；均可附 VLAN Tag 与 Customer Domain ID；映射 VLAN/SPB/VXLAN/Static Service 四选一（principles·P168，<<<PAGE 621-623>>>）
- **SPB/VXLAN/Static Service/Tunnel 映射**：SPB/VXLAN Profile 设备动态入档案时自动建 SAP；Tunnel Profile：Keepalive 默认 5s、MTU 建议 Raw GRE 1476；Tunnel ID 与 Entropy 只有两种合法组合（AOS 终结=非 0 ID+Entropy 开；非 AOS/OV VPN=0 ID+Entropy 关）（principles·P170，<<<PAGE 625-630>>>）
- **Global Configuration**：Redirect Pause Timer 默认 0；Auth Server Down Timeout 默认 60；Redirect Port Bounce 默认 Enabled；Auth Server Down Access Role Profile=RADIUS 不可达兜底角色（principles·P172，<<<PAGE 634-635>>>）

## E（实证案例）
- Access Role Profile 从建档案到 Apply To Devices 全字段（cases·C53，<<<PAGE 608-613>>>）
- L2 认证/分类决策流全链路（principles·P159，<<<PAGE 591-592>>>）
- 802.1X/MAC 无线认证 Profile 组合（principles·P171，<<<PAGE 631-633>>>）

## B（反例/坑）
- Redirect 开启后 Access Role Profile 只能映射 VLAN（principles·P166，<<<PAGE 608-613>>>）
- 每 Access Role Profile 仅 1 个 Policy List；PolicyView Expert 策略设备集须与档案设备集一致（principles·P166）
- 常见分配失败：链路聚合成员/tagged 口不能启 UNP；VLAN 不存在或非 Standard VLAN；Port-Template 与 L2 Profile 冲突（principles·P162，<<<PAGE 594-601>>>）
- AP Mode 的 Secure 未勾时，AP 认证失败其客户端流量仍被信任（principles·P162）
- 取消端口分配的正规流程：Device Config 删除后重推剩余端口，不要直接改档案（principles·P162）
- Stellar AP VLAN 须 1-4094 或 untagged 否则忽略；Stellar AP 的 VLAN 只能经 Access Role Profile 映射创建（principles·P166 / P188，<<<PAGE 608-613, 790-808>>>）
- 分类规则（MAC 规则）改动会 flush 已分类 MAC；Location 分类仅 Legacy AP，Stellar 不支持（principles·P168，<<<PAGE 621-623>>>）
- AAA 超时参数改了不追溯已在线用户，要 flush 或重新认证才生效（principles·P167，<<<PAGE 614-618>>>）
- 同 AP 多 SSID 静态路由会累积且目的子网不得重复；勿手写隧道 VLAN 对应子网路由（AP 自动建，手写致性能劣化）（principles·P170，<<<PAGE 625-630>>>）
- Captive Portal 不支持 OS6350（principles·P161，<<<PAGE 593-594>>>）
- Hide SSID 几乎无安全价值（principles·P164，<<<PAGE 602-603>>>）

## 来源
OmniVista 2500 NMS 4.9R2 User Guide 第 32 章 Unified Access（<<<PAGE 590-655>>>）、Profile Polling（<<<PAGE 677>>>）、DHCP Option 82（<<<PAGE 643-644>>>）。条目来源：frameworks F15；cases C53；principles P159-P175。
