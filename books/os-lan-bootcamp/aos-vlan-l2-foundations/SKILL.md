---
name: VLAN 与二层基础（802.1Q/动态 VLAN/IP 接口/DHCP Relay/LLDP）
description: 需要配置 OmniSwitch VLAN 创建与端口指派、802.1Q 跨交换机标签、VLAN 规则动态分类（mobile 口）、VLAN 间路由 IP 接口、DHCP Relay、LLDP/LLDP-MED 话机策略时使用本技能。
source_book: DT00CTE120 OmniSwitch R6/R8 Bootcamp Issue 25
---

## R（触发场景）
- 新建 VLAN 并把端口静态/打标签划入，跨交换机桥接多 VLAN
- 按 MAC/网段规则动态指派 VLAN（mobile 口 + VLAN Rules）
- VLAN 间三层互通：给 VLAN 挂 IP 接口、配 DHCP 中继
- IP 话机自动入语音 VLAN（LLDP-MED Network Policy）
- 管理面需要 Loopback0 常驻地址

## I（核心理念）
VLAN 即广播域，端口经静态配置、移动/认证、802.1q、Mobile Tag 四种途径入 VLAN（P64，<<<PAGE 360>>>）。动态分类的优先序固定：MAC > MAC Range > Network > Protocol > Default（P66，<<<PAGE 367-368>>>）。三层互通的开关很简单——VLAN 挂上 IP 接口路由即激活，无活跃成员则 oper down（P68，<<<PAGE 373>>>）。管理面的锚点是 Loopback0：不绑 VLAN 恒 up，RIP/OSPF 自动通告（BGP 不），是 router-id/RP/RADIUS 源 IP 的标准身份地址（P94，<<<PAGE 492>>>）。LLDP 默认全交换机使能，LLDP-MED 的 Network Policy TLV 让话机拿到 VLAN+802.1p+DSCP 三件套自动上线（P97/P98，<<<PAGE 509-517>>>）。

## A1（决策/选型）
1. 静态 VLAN（默认 VLAN 指派）vs 动态 VLAN（规则/认证匹配）vs 802.1Q tag（跨交换机 trunk）
2. Mobile Tag 用于 mobile 口同时收多 VLAN 打标流量，优先于一切 VLAN 规则；802.1Q 标签不适用于 mobile 口（P70，X40，<<<PAGE 382, 383>>>）
3. 802.1Q 标签 4 字节：12bit VID（4096 个）+ 3bit 802.1p（8 级优先级）（P69，<<<PAGE 379>>>）
4. DHCP 中继 vs UDP 中继：`ip helper address` 指 DHCP 服务器；`ip udp relay DNS` 转发指定 UDP 端口（P96，<<<PAGE 498-499>>>）

## A2（操作步骤）
1. 建 VLAN 与静态指派：`vlan 20` → `vlan 20 port default 1/2`(R6)/`vlan 20 members port 1/1/2 untagged`(R8) → `interfaces 1/2 admin up`(R6)/`interface 1/1/2 admin-state enable`(R8) → `show vlan 20 port` 验证（C15，<<<PAGE 385-390>>>）
2. VLAN 规则动态分类：`vlan 2 ip 10.1.20.0 255.255.255.0`、`vlan 3 mac-range 00:80:9f:00:00:00 00:80:9f:ff:ff:ff`、`vlan port mobile 1/1`、`vlan 3 mobile-tag enable` → `show vlan rules` 验证命中（C16，<<<PAGE 370-382>>>）
3. 802.1Q 跨交换机：四台各建 VLAN 20/30 + IP 接口（`ip interface int_20 address 192.168.20.7/24 vlan 20`）→ 打标签 `vlan 20 30 802.1q 3/4`(R6)/`vlan 20 members port 1/3/4 tagged`(R8) → 跨机 ping 网关验证（C18，<<<PAGE 407-411>>>）
4. VLAN 间路由与 DHCP Relay：IP 接口激活路由；`ip helper address {Server}`（可多地址/按 VLAN）；`ip udp relay DNS`；`show ip helper` + 客户端获取地址验证（C23，<<<PAGE 492-499>>>）
5. LLDP-MED 话机策略：`vlan 10` + `vlan port mobile 1/10` + `vlan 10 mobile-tag enable` → `lldp 1/10 tlv med network-policy enable` → `lldp network-policy 1 application voice vlan 10 l2-priority 7 dscp 46` → `lldp 1/10 med network-policy 1` → `show lldp remote-system med inventory` 看话机型号/固件（C24，<<<PAGE 511-520>>>）
6. LLDP 邻居验证：`show lldp statistics`、`show lldp remote-system`（邻机系统名/能力/VLAN）（C24，<<<PAGE 511-520>>>）

## E（实证案例）
- C15 VLAN 创建：初始仅 VLAN 1（4094 为 VCM IPC 保留），无成员 VLAN oper 状态 inactive（<<<PAGE 385-390>>>）
- C16 VLAN 规则：ip-net/mac-range 双规则命中验证（<<<PAGE 370-382>>>）
- C18 四交换机 802.1Q 桥接（<<<PAGE 407-411>>>）
- C24 LLDP-MED 话机上线全流程（<<<PAGE 511-520>>>）

## B（反例与坑）
- VLAN 1 不可删除，只能禁用（P71/X38，<<<PAGE 385>>>）
- 管理状态 down 的接口不响应 ping、不会被路由协议通告（X39，<<<PAGE 387>>>）
- mobile 口不能用 802.1Q 标签，须用 Mobile Tag（X40，<<<PAGE 383>>>）
- LLDP 只能在 port/NI/chassis 层配置，不能按 linkagg 配置（X52，<<<PAGE 519>>>）
- 802.1x 认证成功后 MAC 才关联目标 VLAN/UNP——排障先看认证状态（P67，<<<PAGE 371>>>）

## 来源
- principles·P64-P71/P94-P98；cases·C15/C16/C18/C23/C24；counter-examples·X38-X40/X52
