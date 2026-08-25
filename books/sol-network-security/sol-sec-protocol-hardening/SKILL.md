---
name: 协议加固与替换表（控制面/数据面：路由认证、STP/ARP/DHCP 防护、MACsec、安全协议替换）
description: 需要加固交换机控制面与数据面协议时使用：RIP/OSPF/BGP/LDP 邻居认证与 keychain 轮换、Root Guard/TCN/BPDU、LLDP Agent Security、ARP/GARP/DHCP Snooping/DAI、IPv6 三件套、ICMP 裁剪、MACsec、LPS，以及 Telnet/FTP/SNMPv1/HTTP 到安全协议的替换决策表。
source_book: Network Security Guidelines
---

## R（触发场景）
- 加固路由与标签协议邻居（RIP/OSPF/IS-IS/BGP/LDP 认证、keychain 轮换）
- 防生成树攻击（Root Guard/TCN 限制/BPDU 过滤）与 rogue 设备（LLDP Agent Security）
- 防 ARP 欺骗/MiTM/rogue DHCP（ARP 过滤、GARP 阻断、Snooping+DAI、IPv6 三件套）
- 关键链路加密（MACsec/MKA）与边缘端口防护（LPS）
- 用安全协议替换 Telnet/FTP/TFTP/SNMPv1/HTTP

## I（核心理念）
开机默认全开的服务端口是 DoS 攻击面（X3，<<<PAGE 12>>>）：先全关服务再按需开安全协议（P19，<<<PAGE 12>>>）。不安全协议仅为兼容遗留系统保留，必须替换（P20，<<<PAGE 12>>>）。控制面防护逻辑 = 协议认证（谁可参与）+ 拓扑防护（防外部影响生成树）+ 地址防护（防 ARP/DHCP/RA 欺骗）。keychain 是 OSPF/IS-IS 最安全选项，密钥带起止时间定期轮换（P47，<<<PAGE 30>>>）。

## A1（行动框架）
1. 协议替换对照框架（F3/P20，<<<PAGE 12>>>）：Telnet→SSH（无加密无证书）；FTP/TFTP→SFTP/SCP；SNMPv1/v2c→SNMPv3（仅社区串认证）；HTTP→HTTPS（明文）
2. 控制面加固路线（<<<PAGE 30-43>>>）：路由/标签协议认证（P46）→ STP 三防（P48-P50）→ LLDP Agent Security（P51）→ ARP/GARP 防欺骗（P52-P54）→ NTP 认证（P55）→ ICMP 裁剪（P56）→ DHCP Snooping+DAI（P57）→ IPv6 三件套（P58）→ 不用即关 MVRP（P59）→ 交换机 supplicant（P60）
3. 数据面加固路线（<<<PAGE 43-47>>>）：MACsec 链路加密（P61）→ 禁定向广播（P62）→ IPv6 邻居缓存限额（P63）→ 边缘 LPS（P64）

## A2（操作步骤）
- **OSPF keychain 三密钥轮换**（C10，<<<PAGE 30>>>）：`security key 1/2/3 algorithm sha256 ... start-time/lifetime` → `security key-chain 1 name "OSPF"` → `ip ospf interface vlan-101 auth-type key-chain 1`
- **STP 三防**（P48-P50，<<<PAGE 32-33>>>）：核心下行口开 Root Guard（restricted-role）；边缘口开 TCN 限制（restricted-tcn）；用户口收 BPDU 即过滤或 shutdown
- **LLDP Agent Security**：端口仅信一个 LLDP 远端代理，rogue 设备接入即触发 violation（trap/shutdown）并阻塞 NNI 口（C11/P51，<<<PAGE 33>>>）
- **ARP 防欺骗组合**：ARP 过滤 + 阻断入向 GARP + 对服务器/网关等关键主机配 arp-poison restricted-address 检测（P52-P54，<<<PAGE 34-35>>>）
- **DHCP Snooping + DAI**（C12/P57，<<<PAGE 38-39>>>）：`dhcp-snooping vlan 140 admin-state enable` + 服务器端口 `trust` + `dhcp-snooping ip-source-filter vlan 140 admin-state enable`（依绑定表校验源，防 ARP 欺骗）
- **IPv6 三件套**（P58，<<<PAGE 39-46>>>）：DHCPv6 Snooping + IPv6 Source Filtering（需 TCAM 模式调整）；DHCPv6 Guard（仅信任口放服务器报文）；RA 过滤（ra-filter 丢非法 RA）
- **NTP 认证**：/flash/network/ntp.keys 存 MD5/SHA1 密钥并设 trusted，保证日志时间可信（P55，<<<PAGE 36-37>>>）
- **ICMP 裁剪**：按风险表禁 Echo/Redirect/RA/Timestamp 等无用消息（P56，<<<PAGE 37-38>>>）
- **MACsec/MKA**：etherType 0x88E5 点对点加密；静态 SAK 四密钥（一用三备）或 MKA 动态轮换（P61，<<<PAGE 43-44>>>）
- **LPS**：边缘端口 MAC 学习授权，限数/限窗/违规 shutdown（P64，<<<PAGE 46-47>>>）

## E（实证案例）
- OSPF keychain 三密钥轮换配置（C10，<<<PAGE 30>>>）
- LLDP Agent Security 检测 rogue 接入并阻塞 NNI 口（C11，<<<PAGE 33>>>）
- DHCP Snooping + IP Source Filtering 组成 DAI（C12，<<<PAGE 39>>>）
- DoS 过滤默认开启：Ping of Death/Land/ARP Flood(>500/s)/Ping overload(>100/s)；端口扫描按 penalty 累计超阈值（如 2000）发 trap（<<<PAGE 41-42>>>）

## B（反例与坑）
- 开机全开 TCP/UDP 知名服务端口，易被 DoS（X3，<<<PAGE 12>>>）
- Telnet/FTP/TFTP/HTTP/明文 SNMP 均为不安全协议（X4，<<<PAGE 12>>>）
- GARP 可被伪造用于 MiTM——阻断入向、放行出向（P53，<<<PAGE 35>>>）
- DHCP Option-82 与 Snooping 互斥（<<<PAGE 38>>>）
- MVRP 不用即关（P59，<<<PAGE 41>>>）
- 定向广播默认丢弃，勿随意开受控放行（P62，<<<PAGE 45>>>）
- IPv6 邻居缓存可被 DoS 耗尽——配限额（P63，<<<PAGE 46>>>）

来源：Network Security Guidelines（Control Plane + Data Plane 章，p12、30-47）
