---
name: AOS 8 IP/IPv6 服务（接口/VRF/隧道/IPsec/DHCP/DNS）
description: 需要在 OmniSwitch AOS 8 上配置 IP/IPv6 接口与静态路由、VRF 与 route leak、GRE/IPIP 隧道、IPsec 策略、DHCP Relay/Snooping/内部 Server、DHCPv6/RA Guard、Generic UDP Relay 时使用。
source_book: OmniSwitch AOS Release 8.10R4 Network Configuration Guide
---

## R（触发场景）
- 交换机做三层网关：建 IP 接口、静态/默认/黑洞路由
- 一台交换机分割多个 L3 租户：VRF 部署与跨 VRF 泄露
- IPv6 接入：寻址、ND/RA 过滤、DHCPv6 Relay/Snooping/RA Guard
- 跨网段 DHCP：内部/外部 relay、Option-82、Snooping 绑定表
- L3 流量加密：IPsec AH/ESP 策略

## I（核心理念）
IP 接口绑定 VLAN 是三层路由基本模型：`ip interface <name> address <ip> vlan <vid>`（P109，<<<PAGE 709>>>）。VRF 类比 VLAN 分割 L2，用来分割 L3：每 VRF 独立路由表+独立路由协议实例，可重复用 IP 地址空间；AOS VRF 不要求 BGP/MPLS 骨干，可经 GRE/IP-IP 隧道承载（P111-P113，<<<PAGE 756>>>）。DHCP 全栈框架（F12，<<<PAGE 903>>>/<<<PAGE 925>>>）：外部 relay（路由器）→内部 relay（global/per-interface、Option-82）→Generic UDP Relay→内部 DHCP Server（policy/配置/数据库文件）→Snooping（L2/L3、绑定表、信任口）→DHCPv6（relay/snooping/RA guard/ISF）。IPsec 只支持传输模式（P119，<<<PAGE 819>>>）。

## A1（决策框架）
1. **基础三层**：建 VLAN→加端口→`ip interface ... vlan`→静态/默认/黑洞路由（`ip static-route` 系列，P110，<<<PAGE 709>>>）
2. **租户隔离选 VRF**：跨 VRF 通信必须显式 route leak，天然隔离导致"配了通不了"的常见误判（X43，<<<PAGE 756>>>）；管理流量可划 Management VRF（<<<PAGE 759>>>）
3. **DHCP 场景分档**：跨 VLAN 中继选内部 relay（global 或 per-interface 模式）；要定位用户加 Option-82（Circuit ID/Remote ID）；要防私接服务器加 Snooping+信任口
4. **IPv6 地址类型**：link-local（仅链路内不可路由）跨链路通信必须配全局单播地址（X44，<<<PAGE 774>>>）；防恶意 RA 用 RA Guard/RA Filtering
5. **加密选型**：机密性必须 ESP；AH 只认证不加密，误当机密性方案是典型错用（X47，<<<PAGE 819>>>）

## A2（操作步骤）
- **IP 转发快配**：建 VLAN→加端口→`ip interface vlan-20 address 171.11.1.1 vlan 20`→静态/默认/黑洞路由（cases·C34，<<<PAGE 709>>>）
- **VRF 部署**：`vrf <name>`→VRF profile→IP 接口划入 VRF→VRF 内路由协议实例；验证 show vrf（cases·C35，<<<PAGE 756>>>）；跨 VRF 泄露走 VRF Route Leak 快配步骤（cases·C36，<<<PAGE 712>>>）
- **IPsec AH 策略**：`ipsec` master key→policy（AH/HMAC-SHA1）→SA→绑定接口/流（cases·C38，<<<PAGE 819>>>）
- **DHCP Relay 六步**：`ip dhcp relay admin-state enable`→`ip dhcp relay destination 128.100.16.1`→（可选）`ip dhcp relay per-interface-mode`→接口级 destination→`ip dhcp relay forward-delay 30`+`ip dhcp relay maximum-hops 10`→`ip dhcp relay insert-agent-information`；验证 `show ip dhcp relay interface`（cases·C42，<<<PAGE 902>>>）
- **内部 DHCP Server**：写 policy file+dhcpd 配置文件→数据库文件路径→使能；验证 show dhcp server（cases·C44，<<<PAGE 893>>>）
- **DHCPv6 Relay/Snooping/RA Guard**：使能 relay 服务→relay 接口→max hops；snooping 绑定表+ISF 源过滤；RA guard 端口策略（cases·C45，<<<PAGE 917>>>）
- **GRE/IP-IP 隧道**：IP over IP 封装（<<<PAGE 721>>>），可作 VRF 点对点承载
- **Generic UDP Relay**：按预配端口转 UDP 到 VLAN/service/IP（P132，<<<PAGE 904>>>）

## E（实证案例）
- DHCP Relay 六步全流程（C42，<<<PAGE 902>>>）
- VRF 部署与 VRF Route Leak（C35/C36，<<<PAGE 756>>>/<<<PAGE 712>>>）
- IPsec AH 策略（C38，<<<PAGE 819>>>）

## B（反例/坑）
- L3 Snooping 必须让客户端与服务器分居不同 VLAN，否则 relay 不介入、snooping 失效（X52/P134，<<<PAGE 925>>>）
- 全局 Option-82 使能时任意级别 DHCP Snooping 都不可用；交换机级与 VLAN 级 Snooping 互斥（X53/P137，<<<PAGE 925>>>）
- 非信任口带 Option-82 的包默认丢弃（X55，<<<PAGE 925>>>）
- relay 校验 forward-delay 与 maximum-hops，不满足即丢弃；多目的地址时全发（P129，<<<PAGE 903>>>）
- 内部 DHCP Server 由 policy file+配置文件+数据库文件驱动，注意与 VRF/Snooping/IP 接口交互（P138，<<<PAGE 894>>>）
- OmniSwitch IPsec 只支持传输模式，无隧道模式（X46/P119，<<<PAGE 819>>>）
- JITC 模式下 FEC0::/10 Site-Local 地址禁配（X45/P117，<<<PAGE 774>>>）
- IPv6 ND 替代 ARP/广播；RA Filtering 过滤恶意/多余 RA（P114/P115，<<<PAGE 773-777>>>）

## 来源
OmniSwitch AOS 8.10R4 Network Configuration Guide 第 21 章 IP（<<<PAGE 709-721>>>）、第 22 章 VRF（<<<PAGE 756-759>>>）、第 23 章 IPv6（<<<PAGE 773-777>>>）、第 24 章 IPsec（<<<PAGE 819-823>>>）、第 27 章 DHCP Relay/Snooping（<<<PAGE 902-926>>>）、第 28 章 Internal DHCP Server（<<<PAGE 893-894>>>）。条目来源：cases C34-C36/C38/C42/C44/C45；principles P108-P138；counter-examples X43-X47/X52-X55；frameworks F12。（注：DNS 在本书 verified 条目中无独立内容，如需 DNS 配置需另查原书。）
