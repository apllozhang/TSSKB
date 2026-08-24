---
name: QoS / ACL / Access Guardian 策略配置
description: 当需要在 OmniSwitch 上做限速与优先级标记（QoS Policy）、禁端口禁服务（ACL）、基于 802.1X/MAC 认证动态下 VLAN（Access Guardian/UNP）、或给 IP 话机自动下发语音 VLAN（LLDP-MED）时使用。
source_book: DT00XTE310 OmniSwitch LAN Access & OmniAccess Stellar WLAN Express
---

## R（触发场景）
- 要限制某 VLAN 的带宽或提升其转发优先级
- 要求员工网段禁 FTP、外发包禁 HTTP、用户口防环（BPDU guard）
- 需要认证后动态分配 VLAN/QoS（802.1X 或 MAC 认证），或话机上电自动进语音 VLAN

## I（核心理念）
OmniSwitch 的策略体系是"condition + action + rule"三件套，`qos apply` 才下发硬件。角色化控制分两层：交换机侧 Access Guardian（UNP 用户网络档案），无线侧 ARP（Access Role Profile）。话机场景用 LLDP-MED Network Policy TLV 自动下发语音 VLAN + L2 priority + DSCP。

## A1（行动框架）
1. **QoS 限速**（<<<PAGE 724>>>-<<<PAGE 726>>>）：`policy condition client_traffic source vlan 20` → `policy action priority_5 802.1p 5` → `policy rule rule1 <condition+action>` → `qos apply` → 大包 ping 触发 Red Packets 验证限速生效。
2. **ACL 禁协议**（<<<PAGE 749>>>-<<<PAGE 751>>>）：
   - 员工禁 FTP：`policy condition ftpfromvlan20 source vlan 20 destination ip-port 20-21 ip-protocol 6` + `policy action deny disposition deny` + `precedence 65535`；
   - 禁外包 HTTP：`policy service group http` + deny；
   - 用户口防环：`policy port group UserPorts 1/1/1-2` + `qos user-port shutdown bpdu`。
3. **Access Guardian 动态 VLAN**（<<<PAGE 777>>>-<<<PAGE 783>>>）：
   - `aaa radius-server my_radius host 192.168.100.102 key alcatel-lucent` → `aaa device-authentication 802.1x my_radius`；
   - 建 UNP-employee / UNP-contractor（map vlan 20/30 + qos-policy-list）；
   - `unp port 1/1/1 port-type bridge` + `802.1x-authentication` + `mac-authentication`；
   - 客户端 802.1X 登录 → `show unp user details`（Profile Source: Auth-Pass-Server UNP）→ `unp user flush port 1/1/1` 清会话重测；
   - 验证 RADIUS：`aaa test-radius-server my_radius type authentication user employee password password`。
4. **LLDP-MED 语音下发**（<<<PAGE 787>>>-<<<PAGE 794>>>）：`lldp network-policy 1 application voice vlan 151 l2-priority 5 dscp 46` → 交换机发 LLDP 帧，话机自动获语音 VLAN/QoS；配合 `unp profile 'voip-temp' mobile-tag … lldp med-endpoint ip-phone classification`。
5. **DHCP Relay**（<<<PAGE 669>>>-<<<PAGE 670>>>）：`ip dhcp relay destination 192.168.100.102` + `admin-state enable` → `show ip dhcp relay statistics` 看 Reception/Tx 计数。

## A2（进阶应用）
- **condition/action 能力边界**（<<<PAGE 699>>>）：condition 可达 L1-L4（source port/MAC/VLAN/IP/DSCP/TCP-UDP port）；action 含 disposition accept|drop|deny、priority、bandwidth、mirror、redirect。规则默认 accept 不匹配流量。
- **ACL 安全组**（<<<PAGE 739>>>-<<<PAGE 740>>>）：UserPorts 默认用于防端口 IP 欺骗：`qos user-port {filter | shutdown} {spoof|bgp|bpdu|rip|ospf|vrrp|…}`；DropServices 保留服务组可按服务丢包；port-disable 命中即管理关闭端口。
- **UNP 分类规则优先级**：Port/Linkagg > Domain > MAC > MAC-OUI > MAC range > LLDP > Auth-type > IP > VLAN tag（<<<PAGE 506>>>），动态分类排障按此顺序。
- **WMM 侧呼应**：Voice DSCP 46 → 802.1p 6，与无线侧 QoS 映射对齐（<<<PAGE 874>>>、<<<PAGE 932>>>）。

## E（实证案例）
- QoS 组合实战：VLAN 20 流量标记 802.1p 5 + qos apply，大包 ping 出现 Red Packets 证明限速（<<<PAGE 724>>>-<<<PAGE 726>>>）。
- Access Guardian 全流程：RADIUS + 双 UNP 档案 + 802.1X/MAC 认证，show unp user details 确认服务器下发档案（<<<PAGE 777>>>-<<<PAGE 783>>>）。
- DHCP Relay + QoS/ACL/Access Guardian 组合部署（<<<PAGE 669>>>-<<<PAGE 670>>>、<<<PAGE 724>>>-<<<PAGE 783>>>）。

## B（边界与陷阱）
- 规则写完必须 `qos apply` 才进硬件；默认策略 accept 不匹配流量（<<<PAGE 699>>>）。
- UserPorts 防欺骗默认存在，叠加自定义 ACL 时注意 precedence（如 65535）与命中顺序（<<<PAGE 739>>>-<<<PAGE 751>>>）。
- Mobile Tag 仅在移动口（话机口）生效，静态 802.1Q tag 在 mobile 口不支持（<<<PAGE 173>>>、<<<PAGE 793>>>）。

## 来源
- principles·P38 QoS Policy 三件套（<<<PAGE 699>>>）
- principles·P39 ACL 安全组（<<<PAGE 739>>>-<<<PAGE 740>>>）
- principles·P40 LLDP-MED 网络策略 TLV（<<<PAGE 787>>>-<<<PAGE 794>>>）
- principles·P16 UNP 动态 VLAN 分类优先级（<<<PAGE 506>>>）
- cases·C30 DHCP Relay + QoS/ACL/Access Guardian（<<<PAGE 669>>>-<<<PAGE 670>>>、<<<PAGE 724>>>-<<<PAGE 726>>>、<<<PAGE 749>>>-<<<PAGE 751>>>、<<<PAGE 777>>>-<<<PAGE 783>>>）
