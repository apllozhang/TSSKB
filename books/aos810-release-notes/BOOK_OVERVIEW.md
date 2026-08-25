# OmniSwitch AOS Release 8.10R4 Release Notes — 全书概览

- 书名：Release Notes — OmniSwitch 6360/6465/6560(E)/6570M/6575/6860(E)/6860N/6865/6870/6900/6920/9900, Release 8.10R4
- 出版：ALE（Alcatel-Lucent Enterprise），2025-12，Part No. 033808-00 Rev. A
- 页数：105 页（fulltext.md 页码标记 `<<<PAGE N>>>`，与 PDF 页码一致）
- 性质：版本发布说明——升级前提、新特性、许可、已知问题（Open CR）、修复列表（Fixed CR）、升级流程附录。信息密度高、大量内容为"手册里没有"的独占信息（原书自述："Since much of the information in these release notes is not included in the hardware and software user manuals, it is important that you read all sections"）

## 章节结构与蒸馏重点

| 页 | 章节 | 蒸馏重点 |
|---|---|---|
| 4-14 | System Specifications | 各机型 SDRAM/Flash 配置；各机型 U-Boot/FPGA/ONIE/CPLD 最低版与当前版矩阵（升级硬前提） |
| 15-18 | [MUST READ] Prerequisites and Deployment | 出厂首次启动 VC 自动化副作用、OS6560-P48Z16(903954-90) 聚合限制、快速收敛例外、MACsec 站点许可、SHA-1/ssh-rsa 禁用、按版本列出的废弃特性（EVB/NTP/WRED/OVSDB/EVPN VRF 化等） |
| 19-20 | Licensed Features | CAPEX 特性许可表（MACsec/10G/MPLS/50G）、Metro 许可、Advanced Routing 许可差异 |
| 21-22 | New Hardware Support | OS6575 三款工业机型、OS6920-D32、400G/100G 新光模块 |
| 23-40 | 8.10R4 New Features | 管理类（Router Mode/su 安全/首访改密/ALE CA 证书/弱加密禁用/Linux 命令）、L3（IPv6 BGP 聚合/PIM over GRE/sFlow BGP 网关）、业务类（EVPN 多站点/VXLAN EVPN on 6870/PEG/SPB on 6570M·6575/ERP over SPB）、安全类（TLS 1.3/Secure Boot/IP 分片攻击防护/PKIX SSH/MKA VLAN Tag）、其他（Threat-Insight/RoCEv2 DCQCN/PROFINET/DHL Active-Standby/Telemetry/Multi-Site SPB） |
| 41-46 | Open Problem Reports | 发布时已知未修问题：光模块/链路类（SFP-10G-T 只跑 10G、SFP-GIG-T 10M 抖动、4X25G 分光纤 CRC）、EVPN toggle 掉流、VC sdp/sap MAC 丢失、MACsec 静态无加密 mismatch 仍通、OS6920 隧道不支持等 |
| 47-49 | Hot-Swap/Redundancy Guidelines | NI 拔插间隔 30 秒、CMM 15-20 分钟、同型号才能热换、fast/perpetual PoE 换异种电源流程 |
| 52-61 | Appendix A: Feature Matrix | 13 平台 × 数百特性首次支持版本矩阵（Y/N/版本号/EA） |
| 62-63 | Appendix B: MACsec Platform Support | 各平台/模块 MACsec 端口级支持与密钥长度（128/256-bit、Static/Dynamic） |
| 64-66 | Appendix C: SPB L3 VPN-Lite | Inline Routing 与 External Loopback 协议支持表；BVLAN 收敛到 4 条的指南与 `show spb isis bvlans` 判活 |
| 67-71 | Appendix D: Upgrade Requirements | 标准/ISSU 两路径、ISSU 支持版本清单、升级前置检查（certified 配置、U-Boot/FPGA 版本、tech-support 基线） |
| 72-73 | Appendix E: Standard Upgrade | 5 步标准升级：下载→FTP→reload from working→验证→copy running certified |
| 74-76 | Appendix F: ISSU | 12 步 ISSU：mkdir issu 目录→清理 Slave 同名目录→issu from→show issu status→certify |
| 77-80 | Appendix G: FPGA/U-boot Upgrade | 按 CR 索引的 FPGA/CPLD/U-Boot 升级表 + `update fpga-cpld`/`update uboot` 命令 |
| 81-82 | Appendix H: CPLD/ONIE Upgrade | ONIE 机型 CPLD kit 逐个升级 + `pkgmgr install *-onie-v1.deb` |
| 83-100 | Appendix I: Fixed Problem Reports | 本版修复的数十条 CR（DHCP snooping 绑定、MSTP 跨域 TCN、SSH 内存泄漏、VC DHCP 停转、SPB 控制 MAC 回落等），多数含根因解释 |
| 101-102 | Appendix J: Packages | pkgmgr 安装/卸载、AMS/IoT-Profiler 升级前明文密码处理 |
| 103 | Appendix K: Fixed CVEs | CVE-2025-49794/49795/49796、6965、3277、49844、46817、1861 等 |
| 104-105 | Appendix L: Secure Boot | 各平台 Secure Boot 镜像/U-Boot/BIOS 要求与升级次序 |

## 蒸馏策略（本书特调）

- **counter-examples 是大头**：升级陷阱（Secure Boot 前必须先升 U-Boot、ISSU 不支持的平台、8.10R3 EVPN 必须手工迁 VRF）、已知未修问题（Open CR 全量收）、废弃特性（EVB 配置存在则无法升 8.5R4+）、平台/端口级限制（MACsec 端口矩阵、OS6560-P48Z16 聚合）
- **principles 收新特性机制**：Secure Boot 信任链、ALE CA 证书生命周期、DHL Active-Standby、Telemetry IPFIX 管道、Multi-Site SPB 层级、MKA VLAN/TPID 隧道化等
- **cases 收升级流程**：标准升级、ISSU、FPGA/U-Boot、CPLD/ONIE、Secure Boot、包管理六套
- **frameworks**：升级方法论（Standard/ISSU 二分）、固件三件套（AOS/U-Boot·ONIE/FPGA·CPLD）分层、Feature Matrix 查询法
- **glossary**：版本/固件/许可/新特性术语
