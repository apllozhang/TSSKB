---
name: AOS 8 CLI 命令地图——管理与 OAM 域（监测/sFlow/RMON/日志/OAM/CMM/NTP/文件/SNMP 及数据中心散章，第 18-19/45-48/50-70 章）
description: 需要在 OmniSwitch AOS 8 上配置监控排障（镜像/sFlow/RMON/Health/OAM/CFM/SAA/CPE Test Head）、日志、机箱硬件管理、NTP/文件/配置/SNMP/OpenFlow，及 FCoE/VXLAN Snooping 等散章时，用本地图定位 CLI Reference 对应章节与代表命令。
source_book: OmniSwitch AOS Release 810R04 CLI Reference User Guide
---

## R（触发场景）
- 网络排障：要镜像端口、采 sFlow、配 RMON 告警、查 Switch Health
- OAM 诊断：802.1ag CFM（MEP/MAID）、802.3ah LINK OAM、CPE Test Head 拨测、SAA 探测
- LLDP 邻居发现与 TLV 控制
- 系统管理：日志、CMM/机箱风扇电源温度、NTP、文件系统、配置文件、SNMP、Web、OpenFlow、DNS

## I（核心理念）
双 OAM 体系（P33）：Ethernet OAM/CFM（802.1ag，MEP/MAID/远端 MEP 状态）面向连通性故障管理；LINK OAM（802.3ah）面向单链路监测。管理命令集中在全书尾部（<<<PAGE 5313-6240>>>）；LLDP（第 18 章）属监测域但页码靠前。页码取 PDF 全文标记 `<<<PAGE N>>>`。

## A1（决策框架）
1. **流量观测**：镜像/监控→第 50 章；sFlow→51；RMON→52
2. **健康与日志**：Health→54；Syslog→53
3. **OAM**：CFM→55；LINK OAM→56；CPE Test Head→57；SAA→59
4. **邻居与数据中心散章**：LLDP→18；FIP Snooping→45；FCoE/FC Gateway→46；VXLAN Snooping→47；Port Mapping→48；SIP→19
5. **系统管理**：CMM→60；机箱硬件→61；NTP→62；会话→63；文件→64；Web→65；配置文件→66；SNMP→67；OmniVista Cirrus→68；OpenFlow→69；DNS→70

## A2（操作步骤）·章节清单与代表命令
- **Ch18 802.1AB/LLDP（<<<PAGE 1390>>>，约 40 条）**：`lldp`（LLDPDU/邻居数据库/TLV）；`ethernet-service uni` 控制带标签/无标签 LLDPDU 处理——默认两者均丢弃（P32/X24）
- **Ch19 SIP（<<<PAGE 1486>>>，约 18 条）**：会话/互联类（章名缩写未展开，域归属待确认）
- **Ch50 Port Mirroring and Monitoring（<<<PAGE 5256>>>，约 9 条）**：`ports mirror`
- **Ch51 sFlow（<<<PAGE 5277>>>，约 13 条）**：`sflow`
- **Ch52 RMON（<<<PAGE 5305>>>，约 4 条）**：`rmon`
- **Ch53 Switch Logging（<<<PAGE 5313>>>，约 14 条）**：`syslog`（级别/服务器/过滤）
- **Ch54 Health Monitoring（<<<PAGE 5347>>>，约 6 条）**：CPU/内存/进程阈值检查
- **Ch55 Ethernet OAM（<<<PAGE 5358>>>，约 46 条）**：`cfm`/`ethernet-oam`（MEP/MAID/CCM）
- **Ch56 LINK OAM（<<<PAGE 5432>>>，约 23 条）**：802.3ah 远端发现/环回/远端故障指示
- **Ch57 CPE Test Head（<<<PAGE 5503>>>，约 31 条）**：接入侧业务拨测
- **Ch59 SAA（<<<PAGE 5597>>>，约 19 条）**：`saa`（ping/ftp/http 等业务质量探测）
- **Ch60 CMM（<<<PAGE 5645>>>，约 29 条）**：CMM 控制模块冗余/同步
- **Ch61 Chassis Management（<<<PAGE 5697>>>，约 91 条）**：`chassis`/`temperature`/`fan`/`psu`
- **Ch62 NTP（<<<PAGE 5884>>>，约 25 条）**：`ntp`/SNTP
- **Ch63 Session Management（<<<PAGE 5936>>>，约 35 条）**：CLI 会话/telnet/SSH 超时
- **Ch64 File Management（<<<PAGE 5999>>>，约 21 条）**：`copy`/`delete`/`directory`/脚本
- **Ch65 Web Management（<<<PAGE 6040>>>，约 11 条）**：内嵌 Web 开关与 HTTP/HTTPS
- **Ch66 Configuration File Manager（<<<PAGE 6060>>>，约 11 条）**：`configuration`/`working-set`（running/committed 双区、VC 批量配置）（P34）
- **Ch67 SNMP（<<<PAGE 6079>>>，约 26 条）**：v1/v2c/v3 团体/用户/陷阱
- **Ch68 OmniVista Cirrus（<<<PAGE 6132>>>，约 10 条）**：云管理平台对接
- **Ch69 OpenFlow（<<<PAGE 6151>>>，约 8 条）**：SDN 控制器/流表混合模式
- **Ch70 DNS（<<<PAGE 6169>>>，约 6 条）**：DNS 客户端解析
- **数据中心散章**：Ch45 FIP Snooping（<<<PAGE 5039>>>，约 22 条）；Ch46 FCoE/FC Gateway（<<<PAGE 5090>>>，约 27 条）；Ch47 VXLAN Snooping（<<<PAGE 5152>>>，约 20 条）；Ch48 Port Mapping（<<<PAGE 5195>>>，约 9 条）

## E（实证案例）
- 命令地图型 skill，不搬运案例；原书每条命令自带 Example，按章首页码回查（cases 原件未创建）

## B（反例/坑）
- LLDP 控制帧默认丢弃：带标签与无标签 802.1AB 控制帧默认均丢弃，需 `ethernet-service uni` 显式配置处理方式（X24，<<<PAGE 1390>>>）
- LINK OAM 镜像口不支持（Specifications Guide 佐证）
- 第 19 章 SIP 域归属为建议值（章名缩写在目录中未展开，待确认）

## 来源
OmniSwitch AOS Release 810R04 CLI Reference User Guide 第 18-19、45-48、50-70 章（<<<PAGE 1390-1486、5039-5212、5256-6240>>>）。条目来源：principles P32-P34；counter-examples X24；frameworks F9/F11。
