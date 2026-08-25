# BOOK_OVERVIEW — sol-network-security

## 书册构成（页码全册连续）

| DOC | 源文档 | 页码范围 | 性质 |
|---|---|---|---|
| 1 | network-infrasctructure-solution-security-tech-brief-en.pdf（Network Security Guidelines 技术简报） | p1-86 | ALE OmniSwitch / Stellar WLAN / OmniVista 全栈安全加固配置手册 |
| 2 | maximizing-security-and-performance-whitepaper-en.pdf（视频监控网络全生命周期白皮书） | p87-100 | 视频监控网络 7 阶段生命周期管理方法论 |

## DOC 1 主线（p1-86）
按"管理面 / 控制面 / 数据面"三平面 × "交换 / 无线 / 网管"三产品域组织：
- 通用建议：软件及时打补丁、物理访问控制、人员培训（p7-9）
- 交换机管理面：U-boot/ONIE 口令、镜像完整性、OOB/管理 VRF、管理站 IP 白名单、默认口令、控制台、SSH 强加密套件与 PKA、会话超时与 IP 锁定、WebView、MFA、AAA/RADIUS over TLS、SNMPv3、PKI/SSL cipher、ASA enhanced / CC / JITC / FIPS 四种安全模式、口令策略（p9-30）
- 交换机控制面：RIP/OSPF/IS-IS（keychain 轮换）/BGP/LDP 认证、STP Root Guard 与 TCN 限制、BPDU 过滤、LLDP Agent Security、ARP 过滤/GARP/ARP 欺骗检测、NTP 认证、ICMP 裁剪、DHCP Snooping/DAI、DHCPv6 Snooping/Guard、MVRP 关闭、DoS 过滤、交换机 supplicant（p30-43）
- 交换机数据面：MACsec、定向广播禁用、IPv6 RA 过滤与邻居缓存限制、LPS（p43-47）
- 无线：改默认口令、8 类证书管理、账户/横幅、NTP、syslog over TLS、SNMPv3（SHA/AES128 固定）、wIPS（rogue/interfering/friendly、containment、client blocklist）、WPA3/SAE、OWE、客户端隔离、漫游上下文 DTLS 加密（p47-70）
- 网管 OmniVista：防火墙最小权限、默认口令、2FA、停用未用服务、Network ID 安全上线、审计与分析（Z-Score 异常检测）、UPAM 证书、Quarantine Manager、REST API 安全、Web Services（p71-90）
- 版本基线：AOS 8.10R2 / AWOS 5.0.1 / OmniVista 2500 R4.9.1 / Cirrus R10.4.3

## DOC 2 主线（p87-100）
视频监控网络生命周期管理（NLM）7 阶段：规划设计（Five S's 框架）→ 部署（UNP、Lightning Config）→ 运营管理（OmniVista 监控、Milestone 插件、API）→ 故障维护（软件工具包、PoE 向导、冗余升级）→ 升级优化（AI、Network Advisor）→ 合规文档（网络保险）→ 退役重部署；附客户生命周期差异与价值论述。

## 提取配额完成情况
- principles.md：P1-P52（目标 40-60 ✔）
- cases.md：C1-C14（目标 10-20 ✔）
- counter-examples.md：X1-X20（目标 15-25 ✔）
- frameworks.md：F1-F4（目标 3-6 ✔）
- glossary.md：58 条（目标 45-65 ✔）
