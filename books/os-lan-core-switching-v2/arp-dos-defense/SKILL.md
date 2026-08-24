---
name: ARP 欺骗与 DoS 安全防御
description: 需要防御 ARP 投毒、DoS 泛洪、同子网主机互访失控（Port Mapping/MFF）或配置风暴控制时使用本技能。
source_book: DT00XTE216 OmniSwitch LAN Core Switching Ed15
---

## R（触发场景）
- 接入网出现 ARP 欺骗、网关被冒充，需要检测与过滤手段
- CPU 利用率异常升高，怀疑 ARP 泛洪/DoS 攻击
- 运营商式小区/宿舍网要求用户彼此二层隔离、流量强制上行网关

## I（核心理念）
AOS 交换机把二层安全做成一组可叠加的小特性：DoS Filtering 内置攻击指纹与速率检测；ARP 防御只认可自己发起请求的应答并主动探测受限地址；Port Mapping 用会话隔离 user 口；MFF（RFC 4562）借 DHCP ACK 里的网关 IP 把同子网 ARP 一律应答为网关 MAC，强制所有流量过网关。各特性粒度小、可组合，按威胁面逐项启用。

## A1（行动框架）
1. DoS 检测：`ip dos ...` 体系覆盖 PoD/SYN/Land/Teardrop/Bonk/Boink/Pepsi、无效 IP、组播 IP/MAC 不匹配、ICMP>100pps 判攻击、ARP 限速到 CPU（<<<PAGE 168>>>）
2. ARP 欺骗检测：`ip dos arp-poison restricted-address`（每 IP 接口最多 2 个受限地址，交换机对其主动发探测请求；只接受自己发起请求对应的应答）（<<<PAGE 176>>>、<<<PAGE 177>>>）
3. 本地代理 ARP + 过滤：Local Proxy ARP per-VLAN 用路由口 MAC 应答所有请求；`arp filter` 按 sender/target allow/block 控制代理应答范围（<<<PAGE 179>>>、<<<PAGE 180>>>）
4. Port Mapping 会话：`port-mapping 1 user-port 1/1/1 network-port linkagg 7` + `port-mapping 1 enable`，user 口彼此隔离仅经 network 口通信（最多 8 会话）；`show port-mapping status`（<<<PAGE 182>>>、<<<PAGE 202>>>）
5. MFF 三件套：`port-mapping 1 user-port 1/1/1-2 network-port linkagg 8` + `port-mapping 1 dynamic-proxy-arp enable` + `dhcp-snooping vlan 20 admin-state enable` + `port-mapping 1 enable`（<<<PAGE 186>>>）
6. 风暴控制：`flood-limit {bcast|mcast|uucast|all} rate {pps|mbps|cap%} [low-threshold] action {shutdown|trap|default}`（<<<PAGE 188>>>、<<<PAGE 397>>>）

## A2（进阶应用）
- 未解析下一跳丢弃：ARP 解析期间建 drop-entry 去重，12 次×5s 后超时，保护 CPU（<<<PAGE 175>>>）
- ARP 表项：动态默认 300s 老化；`arp <ip> <mac> [alias]` 做静态/代理（<<<PAGE 178>>>）
- UDP Relay：`ip udp relay port <num>` + `ip udp relay service {tftp|tacacs|ntp...} vlan <id> address <ip>`；`show ip udp relay statistics`（<<<PAGE 170>>>-<<<PAGE 171>>>）
- SNMP 认证 trap 三模式：`snmp authentication-trap mode {standard|private|both}`，private 的 alaAuthenticationFailure 带客户端 IP（<<<PAGE 173>>>）
- 单向会话的 network 口可与其他单向会话共享，但不能与双向会话共享（<<<PAGE 199>>>）

## E（实证案例）
- C-14 双向会话实验：port-mapping 1 走 linkagg 7、port-mapping 2 走 2/1/3，client 只能 ping 到各自 network 口对端；复用已占端口报错（<<<PAGE 202>>>）
- C-15 MFF 三件套配置，`show port-mapping status` 显示 Direction: bi、DPA Status: enable（<<<PAGE 186>>>）

## B（边界与陷阱）
- 一个 user 端口只能属于一个 Port Mapping 会话，跨会话复用直接报 "ERROR: port user already part of an existing PMAP session"（<<<PAGE 202>>>）
- restricted-address 每 IP 接口最多 2 个地址（<<<PAGE 177>>>）

## 来源
- principle·P-24 DoS 检测清单（<<<PAGE 168>>>）
- principle·P-25 未解析下一跳丢弃（<<<PAGE 175>>>）
- principle·P-26 ARP 欺骗检测（<<<PAGE 176>>>、<<<PAGE 177>>>）
- principle·P-27 本地代理 ARP 与过滤（<<<PAGE 179>>>、<<<PAGE 180>>>）
- principle·P-28 ARP 表项属性（<<<PAGE 178>>>）
- principle·P-29 Port Mapping 语义（<<<PAGE 182>>>、<<<PAGE 199>>>）
- principle·P-30 MFF（<<<PAGE 185>>>、<<<PAGE 186>>>）
- principle·P-31 风暴控制（<<<PAGE 188>>>、<<<PAGE 397>>>）
- principle·P-34 SNMP trap 三模式（<<<PAGE 173>>>）
- case·C-14/C-15/C-18；counter·X-10
