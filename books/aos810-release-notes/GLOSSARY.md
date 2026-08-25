# GLOSSARY — OmniSwitch AOS 8.10R4 Release Notes 核心术语

从 verified 术语库精选 63 条，按主题分组。版本/固件/许可/命令保留英文，页码为原书页码。

## 版本与固件体系

- **GA（General Availability，正式发布版）**：如 8.10.86.R04 (GA)，区别于 MR 与 EA（<<<PAGE 4>>>）
- **MR（Maintenance Release，维护版）**：如 8.9.130.R04 MR1，常作为 ISSU 源版本列出（<<<PAGE 68>>>）
- **EA（Early Availability，早期可用）**：可配置但未走完整验证、不受官方支持（<<<PAGE 15>>>）
- **U-Boot**：嵌入式引导加载器；Secure Boot 镜像要求 8.10.37.R04（6360/6465/6560/6570M），`show hardware-info` 查版本（<<<PAGE 4>>>）
- **FPGA**：承载电源/风扇/PoE/端口物理行为的固件，按机型列 Minimum/Current（<<<PAGE 4>>>）
- **ONIE（开放网络安装环境）**：6860N/6870/6900/6920 等机型的引导/安装层，升级走 pkgmgr 装 deb 包（<<<PAGE 10>>>）
- **CPLD**：复杂可编程逻辑器件，ONIE 机型多颗（Main/CPU/LED），updater kit 逐颗升级（<<<PAGE 11>>>）
- **Coreboot-Uboot / Control FPGA / Power FPGA**：9900 平台引导与控制/电源固件三层（<<<PAGE 13>>>）
- **diag.img**：出厂内部诊断镜像，可安全删除（<<<PAGE 15>>>）
- **imgsha256sum**：镜像校验文件，仅 Common Criteria 模式需要（<<<PAGE 72>>>）
- **Signed AOS Image**：签名 AOS 镜像（6570M 8.9R4 起，需配套 U-Boot）（<<<PAGE 53>>>）
- **HSP（Hitless Security Patch Upgrade）**：不打断业务的安全补丁升级（<<<PAGE 52>>>）

## 升级机制

- **Standard Upgrade（标准升级）**：镜像放 Running 目录整机/整 VC 重启（<<<PAGE 67>>>）
- **ISSU（In Service Software Upgrade）**：在服务升级，VC 按 chassis-id 低到高逐台重启、模块化机箱先备 CMM（<<<PAGE 67>>>）
- **Certified/Working 目录**：认证（回滚兜底）/工作（试验）双目录；`copy running certified` 固化、`reload from certified` 回退（<<<PAGE 70>>>）
- **rollback-timeout**：reload 参数（no rollback-timeout），跳过回滚等待直接切换（<<<PAGE 73>>>）
- **write memory flash-synchro**：保存配置并同步 Flash（VC/CMM 间），升级前置与 ISSU 后认证均用（<<<PAGE 70>>>）
- **issu_version**：ISSU 升级包内的版本描述文件，ISSU 目录必备（<<<PAGE 74>>>）
- **VFL（Virtual Fabric Link）**：VC 内部互联链路；内网固定 IP 127.10.<chassis>.65；4X25G splitter 场景需调 inter-frame-gap 防 CRC（<<<PAGE 75, 42>>>）
- **chassis-id**：VC 成员编号；出厂首启自动 VC 固定为 1，可能引发冲突（<<<PAGE 15>>>）
- **vcboot.cfg / vcsetup.cfg**：VC 启动/设置配置；明文 key 直接加载会导致哈希错误（<<<PAGE 15, 91>>>）
- **Secure Boot**：启动期认证校验只运行可信软件，需引导件升级+专用镜像+（ONIE 型）BIOS 使能三件配合（<<<PAGE 34, 104>>>）

## 许可体系

- **CAPEX License**：一次性买断型许可（<<<PAGE 19>>>）
- **MACsec Site License（OS-SW-MACSEC）**：8.6R1 起 MACsec 需站点许可，免费生成、免重启生效（<<<PAGE 15, 19>>>）
- **Performance License（OS####-SW-PERF）**：解锁端口速率（6560 10G、6570M 25G、6870 50G），默认降速运行（<<<PAGE 19>>>）
- **Metro License**：8.9R1 起 6560 城域特性包（CPE Test Head/PPPoE-IA/OAM/SAA/VLAN Stacking/DPA/IPMVLAN 等）（<<<PAGE 19>>>）
- **Advanced Routing License**：OSPF/PIM/VRF/ISIS/GRE/IP-IP/BGP；6560 版限 2 OSPF 区域、8.10R4 新增 BGP（<<<PAGE 20>>>）
- **Premium Bundle License（OS6570-SW-PRMxx / OS6870-SW-PRMx）**：8.10R4 捆绑许可，单文件多子许可（SPB/AR/25G/50G/VxLAN-EVPN）（<<<PAGE 20>>>）
- **VC Parity: Match / Local-Only**：子许可 VC 生效语义——Match=全成员一致才生效；Local-Only=仅本机（<<<PAGE 20>>>）
- **NAAS 2.0 Licensing**：Network-as-a-Service 许可框架，8.10R4 扩到 6575（<<<PAGE 28>>>）
- **SILOS（Site License Client/Manager）**：站点许可客户端/管理器，6870/6900-X 支持（<<<PAGE 53>>>）

## 管理与安全新特性

- **Router Mode / Edge-router Mode**：capability profile 切换的转发规模形态（6870 router mode；6900 edge-router 更大 MAC 规模，需重启生效）（<<<PAGE 26, 37>>>）
- **Secure su Account**：su 超级用户提示符必须设口令，仅 admin 可配、忘却只能恢复出厂（<<<PAGE 26>>>）
- **Change Password on First Access**：admin 默认口令首登强制改密（<<<PAGE 27>>>）
- **ALE CA Signed Certificate**：ALE 内部 CA 签发设备 X.509 证书（5 年有效、到期前 1 年更新），存 /flash/switch/cert.d/（<<<PAGE 27>>>）
- **Crypto Strong Security**：弱加密算法（SHA/MD5 等）禁用开关（<<<PAGE 28>>>）
- **Lightning Config Mode（闪电配置）**：出厂/EMP 口快速开局模式；6575 支持 1/1/1-1/1/2，6920 支持 EMP 口（<<<PAGE 28>>>）
- **AAA Certificate convert-cert**：CER/CRT/DER/P7B/PKCS#12 证书转 PEM（<<<PAGE 26>>>）
- **Session Prompt 64**：CLI 提示符长度 32→64 字符（<<<PAGE 26>>>）
- **AOS 内嵌 Linux 命令**：watch/cut/paste/tee 包装后直接在 AOS CLI 使用（<<<PAGE 28>>>）
- **TLS 1.3 / 默认 TLS 1.2**：8.10R4 默认 TLS 从 1.0 升 1.2、可配 1.3（RADIUS/LDAP/SYSLOG NG/SNMP/WebView）（<<<PAGE 33>>>）
- **PKIX SSH / CAC·PIV**：智能卡 X.509 证书 SSH 登录（JITC STIGS）（<<<PAGE 33>>>）
- **IP 分片攻击防护（tear-drop / icmp-frag-drop）**：重叠畸形分片与分片 ICMP 丢弃（<<<PAGE 34>>>）
- **IPv6 DoS Detection**：NI 上检测 8 种攻击并上报 CMM（<<<PAGE 38>>>）
- **802.1X max-req 1-50**：EAP 重问次数扩容覆盖 PC 启动延迟场景（<<<PAGE 33>>>）

## L3 与业务新特性

- **IPv6 BGP Aggregation**：合并明细为聚合路由通告（admin-state/as-set/community 等）（<<<PAGE 29>>>）
- **PIM over GRE**：GRE 隧道上建 PIM 邻接转发组播（<<<PAGE 29>>>）
- **sFlow BGP Gateway**：流样本携带 BGP 网关归因字段（<<<PAGE 30>>>）
- **PEG（PIM EVPN Gateway）**：EVPN 网络与外部 PIM 域的网关（<<<PAGE 31>>>）
- **OISM**：优化的跨子网组播，fabric 内选择性转发（<<<PAGE 31>>>）
- **EVPN 多站点模型库**：Clos-3/Collapsed/Clos-5/DCI/Multi-PoD/Multi-site 选型（<<<PAGE 30>>>）
- **Manual RD/RT**：EVPN 手工路由目标，支撑多站点选择性导入与 E-Tree（<<<PAGE 33>>>）
- **ERP over SPB / spb-remote-flush**：ERP 环 MAC flush 传播到 SDP 端口（<<<PAGE 31>>>）
- **SPB on 6570M/6575**：6570M 需 premium bundle、6575 默认支持；推荐 Fabric TCAM profile（<<<PAGE 31>>>）
- **Multi-Site SPB / SBN / site-id**：站点内 ISIS L1、站点边界节点以 site-id 互联成 L2，突破 500-1000 节点上限（<<<PAGE 40>>>）
- **DPA / MAC Forced Forwarding**：动态代理 ARP（6560/6570M 8.10R4）（<<<PAGE 29>>>）
- **DHL Active-Standby**：双归链路 LACP 主备，standby 秒级接替+pre-empt 回切；无缝 failover 边界 128 VLAN/1000 MAC（<<<PAGE 37, 97>>>）
- **RoCEv2 / DCQCN / DCBX**：RDMA over Ethernet v2 与 ECN+PFC 拥塞控制、LLDP 能力交换（6900/6920）（<<<PAGE 36>>>）
- **PROFINET**：工业协议，6575 通过 IO-Device 认证（<<<PAGE 37>>>）
- **Telemetry（IPFIX 推送）**：本地 Redis DPI/流数据按 IPFIX 推送到 Telegraf/InfluxDB/Grafana（<<<PAGE 39>>>）
- **Threat-Insight / DGA·MITM·JA3**：AppMon 每流威胁智能三属性（<<<PAGE 36>>>）
- **MKA VLAN Tag / TPID**：MKA 控制包打 VLAN 标签隧道化过中间节点（<<<PAGE 35>>>）
- **Device Profiling 自动启用**：全局启用后边缘端口默认开设备画像（<<<PAGE 37>>>）
- **ISFv6 on SAPs**：业务域 IPv6 源过滤（<<<PAGE 31>>>）

## 硬件与光模块

- **OS6575 家族**：-40~75°C 加固工业交换机（P12/U28/MP16 三形态）（<<<PAGE 21>>>）
- **OS6920-D32**：1RU 32×400G QSFP-DD 平台，本版无 VC（<<<PAGE 21>>>）
- **QSFPD-400G 系列**：400G QSFP-DD 光模块/DAC/AOC（C/DR4/FR4/LR4/A10M/SR4.2，SR4.2 可 4×100G 拆分）（<<<PAGE 22>>>）
- **QSFP-100G-SR1.2 / PSM4**：100G 新模块（SR1.2 配 SR4.2 拆分；PSM4 MPO 2km）（<<<PAGE 22>>>）
- **SFP-10G-T / SFP-GIG-T**：10G/1G 铜口模块，Open CR 多条涉及其速率协商缺陷（<<<PAGE 42>>>）
- **Splitter（4X10G/4X25G）**：高速口拆分模式，快速收敛与部分 MACsec 不支持（<<<PAGE 15, 63>>>）
- **VFL**：VC 内部互联专用上行口组（6575/6570M/6870）（<<<PAGE 15>>>）
- **EMP 端口**：以太网管理端口，Lightning Config 相关（<<<PAGE 28>>>）
- **RTC（实时时钟）**：6360 无 RTC，断电丢时间需 NTP（<<<PAGE 17>>>）

## 运维与支持

- **Hot-Swap（热插拔）**：NI 间隔 30 秒、CMM 15-20 分钟、插入后 5 分钟+LED 正常，且必须同型号（<<<PAGE 47>>>）
- **Fast PoE / Perpetual PoE（fpoe/ppoe）**：快速/持续供电，换异种电源前须禁用并 reload（<<<PAGE 48>>>）
- **Dying Gasp**：断电临终告警（trap/syslog）（<<<PAGE 52, 98>>>）
- **RCD（Remote Chassis Detection）**：远程机箱检测/零触摸开局（<<<PAGE 53>>>）
- **AMS（AOS Micro Services）**：AOS 微服务框架（deb 包形态）（<<<PAGE 52>>>）
- **pkgmgr**：AOS/第三方 Debian 包管理器（verify/install/remove）（<<<PAGE 101>>>）
- **CMM / NI / CFM**：机箱管理模块/网络接口模块/风扇模块（<<<PAGE 47>>>）
- **Severity 1-4**：ALE 技术支持严重度分级（1=生产网中断……4=咨询）（<<<PAGE 50>>>）
- **CRAOS8X-xxxxx**：ALE 问题报告编号体系，Fixed/Open CR 的索引键（<<<PAGE 41>>>）
- **show tech-support eng complete**：含 SWLOG 的完整诊断 TAR，升级基线必备（<<<PAGE 71>>>）
- **FOSS（/flash/foss）**：第三方开源组件许可声明目录（<<<PAGE 51>>>）
