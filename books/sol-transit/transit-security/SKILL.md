---
name: 轨交网络安全纵深防御（IoT 终端加固/防火墙边界/交换机登录与管理面加固/DoS 过滤/MACsec/NAC 准入/容器隔离/IDS 联动处置）
description: 为轨交承载网设计安全体系时使用（仅通用版含此章）：defense-in-depth 分层框架、IoT 设备四项加固、系统间通信走防火墙、认证登录与管理协议加固清单、OmniSwitch 内置 DoS 攻击类型与阈值、MACsec 线速加密的机型支持表、Access Guardian 三种准入认证、SPB 容器隔离与 IDS 联动隔离处置、Common Criteria/FIPS/JITC 认证。
source_book: Transportation Networks Design Guide
---

## R（何时用）
- 编写轨交项目的网络安全方案（分区分域、纵深防御）
- 加固交换机管理面（登录、协议、DoS 过滤）与数据面（MACsec）
- 设计 IoT 终端（摄像头、售票机、传感器）的准入与隔离方案
- 应答业主的安全合规问询（Common Criteria/FIPS/JITC）

## I（核心理念）
轨交关键基础设施安全必须走"纵深防御（defense-in-depth）"，主动与被动机制并用（通用版 p55）。分层布防：终端层给 IoT 设备做密码/证书/加密管理/补丁四项加固；边界层让系统间通信只经防火墙、按细粒度策略放行（可结合用户身份/设备/应用/位置的动态策略）；网络层做交换机登录外置（RADIUS/LDAP）、禁明文协议、开 DoS 过滤、启用 AOS secure diversified code 源码级加固；数据面用 MACsec 在 MAC 层做线速认证与加密，重点是保护经过物理安全区外公共空间的链路；准入层用 Access Guardian 三种认证（802.1x/MAC/Captive Portal）返回 User Network Profile 动态绑 VLAN 与策略；架构层靠 SPB 容器（ISID）天然分段、出容器必过防火墙；响应层 OmniVista 与 IDS 经 Syslog 联动定位攻击者端口并隔离（通用版 p55-65）。

## A1（决策要点）
1. 方案骨架按七层搭：IoT 终端 → 边界防火墙 → 网络设备加固 → DoS 过滤 → MACsec 数据面 → NAC 准入 → 容器隔离与联动处置（通用版 p55-65）
2. IoT 设备四件套：中心化密码策略、X.509 证书双向认证（兼做 NAC）、TLS 管理禁明文、按厂商规范打补丁（通用版 p56）
3. 管理面基线：Telnet/FTP/SNMPv1v2 全禁、SSHv2 密钥>2048、SNMPv3 带认证加密、TLS 1.1/1.2 连 RADIUS/LDAP/Syslog、admin 本地库仅作 console 口的兜底（通用版 p57）
4. MACsec 部署点：公共空间链路（易被搭线窃听）为主场景；骨干节点间 10G 用 6860/9900，站点接入用 6860/6465（含加固场景），对照机型支持表选型（通用版 p59-61）
5. 准入选型：有 supplicant 用 802.1x；哑终端用 MAC 认证；访客/BYOD 用 Captive Portal；认证返回 UNP 联动 VLAN/ACL/QoS（通用版 p63-64）
6. 容器化：SPB 的 MAC-in-MAC + ISID 天然把 IoT 分进容器，容器外通信必过防火墙；接入层按设备类型发 Network Profile（通用版 p64）
7. 政企/公共部门项目核对认证：NDcPP EAL-2、FIPS 140-2、JITC（通用版 p61-63）

## A2（细节速查表）

| 防御层 | 机制 | 要点 | 页码 |
|---|---|---|---|
| IoT 终端 | 密码/证书/加密/补丁 | 证书可用于与服务器双向认证及 NAC | p56 |
| 边界 | 防火墙 | 系统间通信只经防火墙；可做身份感知动态策略 | p56 |
| 登录与审计 | RADIUS/LDAP 外置 | 本地 admin 仅 console 兜底；记录会话统计 | p57 |
| 管理面 | 协议加固 | 禁 Telnet/FTP/TFTP/明文 SNMP；SSHv2/HTTPS/SNMPv3/TLS | p57 |
| DoS 过滤 | 内置攻击识别 | Ping of Death、Land、ARP Flood（>500/s）、Invalid IP、ICMP 过载（>100/s，默认关）、端口扫描等 | p57-58 |
| OS 加固 | Secure diversified code | 源码独立验证、目标码多样化、安全交付；每个新版持续应用 | p59 |
| 数据面 | MACsec（802.1AE） | 硬件线速、零时延代价；防中间人/嗅探/伪造/重放 | p59 |
| 准入 | Access Guardian | 802.1x（EAP）/MAC 认证/Captive Portal；返回 UNP | p63-64 |
| 分段 | 容器化 | ISID 容器隔离，出容器过防火墙；NP 按设备类型下发 VLAN/ACL/QoS | p64 |
| 响应 | IDS 联动 | OmniVista 收 Syslog 定位端口并 quarantine（关端口或隔离 profile） | p64-65 |
| 分析 | Smart Analytics | SNMP+sFlow，DPI 应用识别（6860E 接入口可做应用策略） | p65 |

| MACsec 支持（节选） | 硬件支持 | 软件版本 | 页码 |
|---|---|---|---|
| OS6465-P6/P12 | 全端口 | AOS 8.5R01 | p59 |
| OS6465-P28 | 全部 1G 口 + 4 个 10G 口中的 2 个 | AOS 8.5R02 | p59 |
| OS6860（多数型号） | 仅 10G 口 | AOS 8.4.1R03 | p59-60 |
| OS6860E-P24 | 1G 与 10G 口 | AOS 8.4.1R03 | p60 |
| OS9900 | 除 CNI-U8 模块与 CMM 40G 口外全端口 | AOS 8.4.1R03 | p60 |

| 认证 | 覆盖产品 | 级别 | 页码 |
|---|---|---|---|
| Common Criteria NDcPP | 6250/6350/6450（AOS 6.7.1）等 | EAL-2 | p62 |
| FIPS 140-2 | AOS 6.7.1R04、8.3.1R01 | 密码模块 | p63 |
| JITC | 6860/6865/6900/9900 | 美国防部互操作 | p63 |

## E（场景案例）
- SPB 网中 MACsec 部署：骨干 10G 链路（6860/9900）+ 站点接入链路（6860/6465）的组合保护（通用版 p60-61）
- IDS 检出攻击 → Syslog（含攻击者地址）→ OmniVista 定位交换机端口 → 关端口或套隔离 profile（限制性 VLAN+ACL）→ 补丁清理的闭环（通用版 p64-65）
- sFlow-RT 实时检测 DDoS → SDN 应用驱动控制器下发丢流规则的缓解路径（通用版 p65）
- 容器化落地：接入层 NP 认证绑 VLAN → 802.1q 上联 → BEB SAP 映射 SPB 容器（通用版 p64）

## B（限制与坑）
- 本单元仅来自通用版第 6 章，SPB 版只有需求级安全描述（SPB 版 p11）
- 只做预防不做响应——原文强调没有 IDS 联动隔离的安全策略不完整（通用版 p64）
- MACsec 当全网开关——它是逐链路点到点机制，按"公共空间链路"选点部署（通用版 p59-61）
- OS6465-P28 的 MACsec 只覆盖部分 10G 口，插错口等于没加密（通用版 p59）
- ICMP 过载检测默认关闭，需要时应显式开启（通用版 p58）
- 6450/6560/6350 等接入机型无 MACsec 硬件支持表项，加密诉求下不能选（通用版 p59-60）

## 来源
Transportation Networks Design Guide（p55-65；SPB 版仅 p11 有安全需求级描述）
