# glossary — 术语表（OmniSwitch AOS 8.10R4 Release Notes）

格式：`- **术语**：中文解释 <<<PAGE N>>>`（页码为 fulltext.md 真实标记；按章分组）

## 版本与固件（System Specifications / Prerequisites）

- **GA（General Availability）**：正式发布版，如 8.10.86.R04 (GA)，区别于 MR（维护版）与 EA <<<PAGE 4>>>
- **MR（Maintenance Release）**：维护版本（如 8.9.130.R04 MR1），作为 ISSU 源版本时常被列出 <<<PAGE 68>>>
- **EA（Early Availability）**：早期可用特性——可配置但未走完整验证流程、不受官方支持："they have not gone through the complete AOS validation cycle and are therefore not officially supported." <<<PAGE 15>>>
- **U-Boot**：嵌入式引导加载器；Secure Boot 镜像要求 8.10.37.R04（6360/6465/6560/6570M），`show hardware-info` 查版本 <<<PAGE 4>>>
- **FPGA**：现场可编程门阵列固件，承载电源/风扇/PoE/端口物理行为，按机型有 Minimum/Current 两列 <<<PAGE 4>>>
- **ONIE**：开放网络安装环境，6860N/6870/6900/6920 等 ONIE 型机型的引导/安装层，升级走 pkgmgr 装 deb 包 <<<PAGE 10>>>
- **CPLD**：复杂可编程逻辑器件，ONIE 机型多颗（Main/CPU/LED），updater kit 逐颗升级 <<<PAGE 11>>>
- **Coreboot-Uboot / Control FPGA / Power FPGA**：9900 平台的引导与控制/电源固件三层 <<<PAGE 13>>>
- **diag.img**：出厂可能附带的内部诊断镜像文件，可安全删除 <<<PAGE 15>>>
- **imgsha256sum**：镜像校验文件，仅 Common Criteria 模式需要 <<<PAGE 72>>>

## 升级机制（Appendix D-F）

- **Standard Upgrade（标准升级）**：镜像放 Running 目录整机/整 VC 重启的升级方式 <<<PAGE 67>>>
- **ISSU（In Service Software Upgrade）**：在服务软件升级，VC 按 chassis-id 低到高逐台重启、模块化机箱先备 CMM，业务中断最小化 <<<PAGE 67>>>
- **Certified/Working 目录**：认证（回滚兜底）/工作（试验运行）双目录机制；`copy running certified` 固化、`reload from certified` 回退 <<<PAGE 70>>>
- **rollback-timeout**：reload 参数（no rollback-timeout），用于跳过回滚等待直接切换 <<<PAGE 73>>>
- **write memory flash-synchro**：保存配置并同步 Flash（VC 成员/CMM 间），升级前置与 ISSU 后认证均用 <<<PAGE 70>>>
- **issu_version**：ISSU 升级包内的版本描述文件，ISSU 目录必备 <<<PAGE 74>>>
- **VFL（Virtual Fabric Link）**：VC 内部互联链路；内网固定 IP 127.10.<chassis>.65；4X25G splitter 场景需调 inter-frame-gap 防 CRC <<<PAGE 75>>>/<<<PAGE 42>>>
- **chassis-id**：VC 成员编号；出厂首启自动 VC 会固定为 1，可能引发重复 chassis-id 冲突 <<<PAGE 15>>>
- **vcboot.cfg / vcsetup.cfg**：VC 启动/设置配置文件；明文 key 直接加载会导致哈希错误 <<<PAGE 15>>>/<<<PAGE 91>>>

## 许可体系（Licensed Features）

- **CAPEX License**：一次性买断型许可，区别于订阅 <<<PAGE 19>>>
- **MACsec Site License（OS-SW-MACSEC）**：8.6R1 起 MACsec 需站点许可（免费生成、免重启生效） <<<PAGE 15>>>/<<<PAGE 19>>>
- **Performance License（OS####-SW-PERF）**：解锁端口速率（6560 的 10G、6570M 的 25G、6870 的 50G），默认端口降速运行 <<<PAGE 19>>>
- **Metro License**：8.9R1 起 6560 的城域特性包（CPE Test Head/PPPoE-IA/OAM/SAA/VLAN Stacking/DPA/IPMVLAN 等） <<<PAGE 19>>>
- **Advanced Routing License（OS6570M-SW-AR / OS6560-SW-AR）**：OSPF/PIM/VRF/ISIS/GRE/IP-IP/BGP 等路由特性；6560 版限 2 OSPF 区域、8.10R4 新增 BGP <<<PAGE 20>>>
- **Premium (Bundle) License（OS6570-SW-PRMxx / OS6870-SW-PRMx）**：8.10R4 引入的捆绑许可，单文件多子许可（SPB/AR/25G/50G/VxLAN-EVPN） <<<PAGE 20>>>
- **VC Parity: Match / Local-Only**：子许可 VC 生效语义——Match=全成员一致才生效；Local-Only=仅本机生效 <<<PAGE 20>>>
- **NAAS 2.0 Licensing**：Network-as-a-Service 许可框架，8.10R4 扩到 6575 <<<PAGE 28>>>
- **SILOS（Site License Client/Manager）**：站点许可客户端/管理器，6870/6900-X 系列支持 <<<PAGE 53>>>

## 8.10R4 新特性（New Features）

- **Router Mode / Edge-router Mode**：capability profile 切换的转发规模形态（6870 router mode；6900 edge-router 更大 MAC 规模，需重启生效） <<<PAGE 26>>>/<<<PAGE 37>>>
- **Secure su Account**：su 超级用户提示符必须设口令，仅 admin 可配 <<<PAGE 26>>>
- **Change Password on First Access**：admin 默认口令首登强制改密 <<<PAGE 27>>>
- **ALE CA Signed Certificate**：ALE 内部 CA 签发的设备 X.509 证书（5 年有效、到期前 1 年更新），取代自签证书，存 /flash/switch/cert.d/ <<<PAGE 27>>>
- **Crypto Strong Security**：弱加密算法（SHA/MD5 等）禁用开关 <<<PAGE 28>>>
- **Lightning Config Mode（闪电配置）**：出厂/EMP 口的快速开局模式；6575 支持 1/1/1-1/1/2，6920 支持 EMP 口 <<<PAGE 28>>>
- **AAA Certificate convert-cert**：CER/CRT/DER/P7B/PKCS#12 证书转 PEM <<<PAGE 26>>>
- **Session Prompt 64**：CLI 提示符长度 32→64 字符 <<<PAGE 26>>>
- **AOS 内嵌 Linux 命令**：watch/cut/paste/tee 经包装直接在 AOS CLI 使用，免进 su <<<PAGE 28>>>
- **DPA / MAC Forced Forwarding**：动态代理 ARP（6560/6570M 8.10R4 支持） <<<PAGE 29>>>
- **PIM over GRE**：GRE 隧道上跑 PIM 组播路由邻接 <<<PAGE 29>>>
- **sFlow BGP Gateway**：sFlow 样本携带 BGP 网关归因字段 <<<PAGE 30>>>
- **PEG（PIM EVPN Gateway）**：EVPN 网络与外部 PIM 域的网关 <<<PAGE 31>>>
- **OISM**：优化的跨子网组播，fabric 内选择性转发 <<<PAGE 31>>>
- **ERP over SPB / spb-remote-flush**：ERP 环跑在 SPB 上时让 MAC flush 传播到 SDP 端口的特性 <<<PAGE 31>>>
- **Manual RD/RT**：EVPN 服务手工路由目标配置，支撑多站点/PoD 选择性导入与 E-Tree <<<PAGE 33>>>
- **Threat-Insight**：AppMon 集成的每流威胁智能（DGA/MITM/JA3） <<<PAGE 36>>>
- **DGA Score / MITM Score / JA3 Fingerprint**：域名生成算法评分／中间人概率／TLS Client Hello 指纹三属性 <<<PAGE 36>>>
- **RoCEv2 / DCQCN**：RDMA over Converged Ethernet v2 与基于 ECN+PFC 的拥塞控制（6900/6920） <<<PAGE 36>>>
- **DCBX**：数据中心桥接能力交换协议（LLDP TLV 承载） <<<PAGE 36>>>
- **PROFINET**：工业协议，6575 通过 IO-Device 认证 <<<PAGE 37>>>
- **DHL Active-Standby**：双归链路 LACP 主备模式，standby 秒级接替+pre-empt 回切 <<<PAGE 37>>>
- **Telemetry（IPFIX 推送）**：本地 Redis DPI/流数据按 IPFIX (RFC 7011) 推送到 Telegraf/InfluxDB/Grafana <<<PAGE 39>>>
- **Multi-Site SPB / SBN / site-id**：多站点层级 SPB——站点内 ISIS L1、站点边界节点（SBN）以 3 字节 site-id 互联成 L2 <<<PAGE 40>>>
- **MKA VLAN Tag / TPID（alaSecyMkaVlan/Tpid）**：MKA 控制包打指定 VLAN 标签隧道化过中间节点 <<<PAGE 35>>>
- **PKIX SSH / CAC·PIV**：智能卡 X.509 证书 SSH 登录（JITC STIGS） <<<PAGE 33>>>
- **Device Profiling 自动启用**：全局启用后边缘端口默认启用设备画像 <<<PAGE 37>>>
- **ISFv6 on SAPs**：业务域 IPv6 源过滤（dhcpv6-snooping ipv6-source-filter service） <<<PAGE 31>>>

## 硬件与光模块（New Hardware / Open CR）

- **OS6575 家族**：-40~75°C 加固工业交换机（P12/U28/MP16 三形态） <<<PAGE 21>>>
- **OS6920-D32**：1RU 32×400G QSFP-DD 平台 <<<PAGE 21>>>
- **QSFPD-400G 系列**：400G QSFP-DD 光模块/DAC/AOC（C/DR4 500m/FR4 2km/LR4 10km/A10M 10m/SR4.2 100m 可 4×100G 拆分） <<<PAGE 22>>>
- **QSFP-100G-SR1.2 / PSM4**：100G 新模块（SR1.2 配 SR4.2 拆分；PSM4 MPO 2km） <<<PAGE 22>>>
- **SFP-10G-T / SFP-GIG-T**：10G/1G 铜口光模块，Open CR 多条涉及其速率协商缺陷 <<<PAGE 42>>>
- **Splitter（4X10G/4X25G 拆分）**：高速口拆分模式，快速收敛与部分 MACsec 不支持 <<<PAGE 15>>>/<<<PAGE 63>>>
- **VFL**：VC 内部互联用的专用上行口组（6575/6570M/6870） <<<PAGE 15>>>
- **EMP 端口**：以太网管理端口；Lightning Config 与静态 IP 支持相关 <<<PAGE 28>>>
- **RTC（实时时钟）**：6360 无 RTC，断电丢时间，需 NTP <<<PAGE 17>>>

## 运维与支持（Hot-Swap / Support / Appendices）

- **Hot-Swap（热插拔）**：运行中插拔模块；NI 间隔 30 秒、CMM 15-20 分钟、插入后 5 分钟+LED 正常，且必须同型号 <<<PAGE 47>>>
- **Fast PoE / Perpetual PoE（fpoe/ppoe）**：快速/持续供电，换异种电源前须禁用并 reload <<<PAGE 48>>>
- **Dying Gasp**：断电临终告警（trap/syslog），非默认 SNMP 端口场景 8.10R4 修复 <<<PAGE 52>>>/<<<PAGE 98>>>
- **RCD（Remote Chassis Detection）**：远程机箱检测/零触摸开局特性 <<<PAGE 53>>>
- **AMS（AOS Micro Services）**：AOS 微服务框架（deb 包形态） <<<PAGE 52>>>
- **pkgmgr**：AOS/第三方 Debian 包管理器（verify/install/remove） <<<PAGE 101>>>
- **HSP（Hitless Security Patch Upgrade）**：不打断业务的安全补丁升级 <<<PAGE 52>>>
- **Signed AOS Image**：签名 AOS 镜像（6570M 8.9R4 起，需配套 U-Boot） <<<PAGE 53>>>
- **CMM / NI / CFM**：机箱管理模块／网络接口模块／风扇模块（9900/6900 机箱语境） <<<PAGE 47>>>
- **Severity 1-4**：ALE 技术支持严重度分级（1=生产网中断……4=咨询） <<<PAGE 50>>>
- **CRAOS8X-xxxxx**：ALE 问题报告编号体系（8X=AOS 8.x），Fixed/Open CR 的索引键 <<<PAGE 41>>>
- **show tech-support eng complete**：生成含 SWLOG 的完整诊断 TAR，升级基线必备 <<<PAGE 71>>>
- **FOSS（/flash/foss）**：第三方开源组件许可声明目录 <<<PAGE 51>>>

---
合计：63 条。
