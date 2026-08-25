---
name: AOS 网络安全与 VRF/MACsec（LPS/PBR/ACL 组/Snooping/Port Mapping）
description: 需要配置 OmniSwitch 端口安全（LPS）、PBR 策略路由防火墙重定向、UserPorts/DropServices 防欺骗、DoS/ARP 防御、DHCP Snooping+Option 82、Port Mapping、MACsec 链路加密或 VRF 多租户路由隔离/泄漏时使用本技能。
source_book: DT00CTE120 OmniSwitch R6/R8 Bootcamp Issue 25
---

## R（触发场景）
- 接入口限制 MAC 数量/白名单（防私接傻瓜交换机）
- 流量强制经防火墙清洗（PBR 重定向）且要防回环
- 端口防 IP 欺骗、病毒端口批量阻断（UserPorts/DropServices）
- ARP 毒化/DoS 攻击检测与缓解
- 防 rogue DHCP 服务器（DHCP Snooping）+ 终端定位（Option 82）
- 用户口-网络口硬隔离（Port Mapping）
- 链路级加密（MACsec 802.1AE）
- 多租户/多业务路由隔离（VRF）与受控互通（Route Leak）

## I（核心理念）
AOS 安全是一整套组合拳（F9，<<<PAGE 799>>>）：接入面 LLDP Rogue Detection + LPS，转发面 PBR/高级 ACL 组（UserPorts/DropServices/port-disable），控制面 DoS/ARP 防御，数据面 DHCP Snooping+Option82+Port Mapping+MACsec+Storm Control。共同思路是"默认收紧、显式信任"：非信任 DHCP 口只收 Discover/Request（P161，<<<PAGE 829-830>>>）；端口默认只学 1 个 MAC（P152，<<<PAGE 850>>>）。VRF 把一台物理交换机切成多个路由实例、可重复 IP，隔离是默认、互通是例外——只能经 route-map 在 VRF 与 GRT 间泄漏（P165/P168，<<<PAGE 855-864>>>）。

## A1（决策/选型）
1. 端口 MAC 管控：LPS 限学 MAC 数/白名单（不支持聚合口）；违规动作 restrict（只滤违规流量）vs shutdown（全口阻断）（P151/P152，<<<PAGE 804-806>>>）
2. PBR 用于硬件级覆盖路由表的定向转发，回程必须加 source port 条件防打环（P154/P155，<<<PAGE 811-814>>>）
3. MACsec 模式：Static SA（交换机间手工 key-chain）vs Dynamic SA（PSK/EAP，MKA 协商）（P160，<<<PAGE 826-827>>>）
4. VRF 感知面：静态/RIP/OSPF/BGP/PIM/VRRP/QoS/AAA 均 VRF-aware；规模 8~64 依机型（P166，<<<PAGE 855-856>>>）

## A2（操作步骤）
1. LPS：`port-security 1/1 enable` → `port-security max-filtering 0` → `port-security 1/1 violation shutdown` → `port-security convert-to-static enable` 固化当前 MAC；违规后 300 秒自动清或 `port-security slot/port release`；进阶 `maximum num`、`mac-range low high`（8 段/口）、`learn-trap-threshold num`（C42/P153，<<<PAGE 805-809, 850-852>>>）
2. LLDP Rogue Detection：`lldp 1/1 trust-agent enable` + `lldp 1/1 trust-agent violation-action trap|shutdown`；验证 `show lldp trusted remote-agent`；违规恢复 `interfaces <slot>/<port> clear-violation-all`（C41/P150，<<<PAGE 802, 801-802>>>）
3. PBR 防火墙重定向：`policy condition Traffic10 source ip 10.10.0.0 mask 255.255.0.0` → `policy action Firewall permanent gateway ip 192.168.99.254` → 规则绑定；回程 `policy condition TrafficFromFW source IP 10.10.0.0 … source port 2/1` + action 指回内网网关（C43，<<<PAGE 813-814>>>）
4. UserPorts 防欺骗：`policy port group UserPorts 1/1-24 2/1-24 3/1 4/1` → `qos user-port filter spoof rip ospf bgp`；病毒端口 `policy service tcp135/tcp445/udp137` + DropServices 组 + port-disable 动作 + `interfaces violation-recovery-time <num>`、`violation-recovery-trap enable`；`show qos log` 查 "Spoofed traffic triggered user-port shutdown"（C44/P156/P157，<<<PAGE 816-818>>>）
5. ARP/DoS 加固：`ip dos arp-poison restricted-address 192.168.100.152`（每接口最多 2 个）→ `show ip dos arp-poison` 看攻击计数；`ip directed-broadcast off`、`no ip service telnet`、`no ip service port 23`；ICMP 5 秒窗 >100pps 判 DoS（C45/P158/P159，<<<PAGE 819-824>>>）
6. DHCP Snooping + Option 82 + Port Mapping：`ip helper dhcp-snooping enable` → `ip helper dhcp-snooping vlan 24` → 端口角色 `[block/trust/client-only]` → `ip helper dhcp-snooping option-82 data-insertion format ascii …`；映射 `port mapping 1 user-port 1/1-2 network-port 3/2` → `port mapping 1 dynamic-proxy-arp enable` → `port mapping 1 enable` → `show port mapping 1 status`、`show ip dynamic-proxy-arp`（C46/P161-P163，<<<PAGE 829-839>>>）
7. MACsec Static SA：接口下 `interface 1/1/25 macsec sci-tx key-chain …`/`sci-tx encryption`/`sci-rx 0x2 …` 两端成对配置；删除逐项 no（C55，<<<PAGE 1049>>>）
8. VRF：`vrf create IpOne` → `vrf IpOne` 进上下文 → `ip interface intf100 address 100.1.1.1/24 vlan 100` → `show vrf`；泄漏 `ip route-map R1 action permit` + `match protocol static` → `ip export route-map R1`；`ip import vrf V1 route-map R2` → `ip route-pref import 100`（C47/P165-P168，<<<PAGE 859-864>>>）
9. Storm Control：广播/组播/未知单播按 %、mbps、pps 三种阈值限洪泛（P164，<<<PAGE 886>>>）

## E（实证案例）
- C42 LPS：换设备触发违规 → RESTRICT 默认 → 300 秒自动清（<<<PAGE 805-809>>>）
- C43 PBR 防火墙重定向与回程防环（<<<PAGE 813-814>>>）
- C46 DHCP Snooping + Option 82 + Port Mapping 组合拳（<<<PAGE 829-839>>>）
- C47 VRF 创建与静态路由泄漏到 GRT（<<<PAGE 859-864>>>）

## B（反例与坑）
- LPS 不支持聚合口（X78，<<<PAGE 804>>>）；默认违规 restrict、300 秒自动清；端口默认只学 1 个 MAC，接傻瓜交换机/集线器即违规（X79/X80，<<<PAGE 850, 852>>>）
- ARP 毒化受限地址每接口最多 2 个（X81，<<<PAGE 824>>>）
- DHCP 非信任口丢弃 Offer/ACK（只收 Discover/Request）——接 DHCP 服务器/中继的口必须标 trust（X82，<<<PAGE 830>>>）
- MACsec 支持面：6860 仅 10G 口；E-P24Z8 不支持 2.5G 口；99-CMM 仅 4x10G 模式（X83，<<<PAGE 827>>>）
- VRF 名大小写敏感；VLAN 编号不可在 VRF 间重复使用（X68，<<<PAGE 859, 861>>>）；一个 IP 接口+其 VLAN 同时只能属一个 VRF（X69/P167，<<<PAGE 861>>>）
- LLDP Rogue：每口仅一个可信 agent，超时/重复即违规（P150，<<<PAGE 801-802>>>）

## 来源
- principles·P150-P168；frameworks·F9；cases·C41-C47/C55；counter-examples·X78-X83/X68/X69
