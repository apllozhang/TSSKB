---
name: AOS 8.10R4 新特性与废弃变更（迁移必查）
description: 需要了解 OmniSwitch AOS 8.10R4 新增特性（Router Mode/EVPN 多站点/PEG/Threat-Insight/Multi-Site SPB 等）、特性许可体系、以及跨版本升级时的废弃与行为变更清单时使用。
source_book: OmniSwitch AOS Release 8.10R4 Release Notes
---

## R（触发场景）
- 评估或规划升级到 8.10R4，要盘点能拿到哪些新能力
- 升级前检查存量配置是否踩废弃/行为变更（EVB、OVSDB、EVPN VRF 化、ip helper 改名）
- 选型时核对特性许可（Premium 捆绑、Advanced Routing、Metro、Performance）
- 新硬件（OS6575/OS6920-D32/400G 模块）支持情况查询

## I（核心理念)
8.10R4 变更分三层看：新特性（管理安全类、L3/业务类、安全类、运维类）按 Feature Matrix 核对平台与首版（F4，<<<PAGE 52-61>>>/<<<PAGE 19>>>：Y=历来支持 / N=不支持 / 版本号=该版引入 / EA=Early Availability 未完整验证不受支持）；许可分层模型（P48，<<<PAGE 19-20>>>）：Data Center 许可（本版均不支持 DCB/FIP/FCoE）→ Feature/Performance（MACsec/10G/MPLS/50G）→ Metro（8.9R1 起 6560 收费）→ Advanced Routing（6560 版限 2 OSPF 区域；8.10R4 加 BGP）→ Premium 捆绑（单文件多子许可，VC 内 Match=全成员一致才生效 / Local-Only=仅本机，P36/X"VC Parity"）。废弃与行为变更（8.5R4-8.10R4）是升级迁移的硬前提，带 EVB 配置的交换机直接禁止升级（X6）。

## A1（决策框架）
1. **升前查废弃清单**：存量配置含 EVB/OVSDB/分布式 ARP/WRED/qos dscp-table/ip helper 旧格式等，先清理或改写再升级
2. **8.10R3+ EVPN 强制 VRF 语境**：旧版 EVPN 配置必须手工迁入对应 VRF context，否则失效（X5，<<<PAGE 18>>>）
3. **新特性启用三步**：查 Feature Matrix 定平台列→看特性行首版→对照 Licensed Features 表确认许可
4. **EA 特性不上生产**：可配置但未走完整验证流程、不受官方支持（glossary·EA，<<<PAGE 15>>>）
5. **自动化适配**：首访强制改密（X8）与 TLS 默认 1.2（P8）影响 REST API/脚本

## A2（操作步骤）
- **新特性速查**（8.10R4 要点）：Router Mode/Edge-router Mode 规模切换（P16/P17，<<<PAGE 26>>>/<<<PAGE 37-38>>>）、IPv6 BGP 聚合（P19）、PIM over GRE（P20）、sFlow BGP Gateway（P21）、EVPN 多站点模型库 Clos-3/5/Collapsed Core/DCI/Multi-PoD/Multi-site（P22）、手工 RD/RT（P23）、PEG+OISM（P24）、ERP over SPB spb-remote-flush（P25）、SPB on 6570M/6575（P26，推荐 Fabric TCAM profile）、Multi-Site SPB/SBN/site-id 突破平面 500-1000 节点上限（P27）、DHL Active-Standby（P18）、Threat-Insight DGA/MITM/JA3（P32）、RoCEv2/DCQCN（P33）、Telemetry IPFIX→Telegraf/InfluxDB/Grafana（P31）、MKA VLAN/TPID 隧道化（P13/C19）、PKIX SSH 智能卡（P9）、TLS 1.3 可配（P8）
- **许可核对**：Performance License 解锁端口速率（6560 10G/6570M 25G/6870 50G，默认降速）；MACsec Site License 8.6R1 起强制（免费生成、免重启，P12）；Premium 捆绑按 MAC/序列号生成
- **新硬件**：OS6575 家族三形态（P46）、OS6920-D32 32×400G（P45）、QSFPD-400G 系列（C/DR4 500m/FR4 2km/LR4 10km/A10M/SR4.2 可拆 4×100G）、QSFP-100G-SR1.2/PSM4（<<<PAGE 21-22>>>）
- **跨版本配置漂移自查**：NTP `ip service source-ip ntp` 参数 8.5R4 废弃、8.6R2 恢复（X73）；DHCPv6 Guard 接口名格式改 vlan 形式（X69）

## E（实证案例）
- SPB on 6570M 部署：需 premium bundle 许可，6575 默认支持；default 与 Fabric TCAM profile 都支持，推荐 Fabric 获更好性能（P26，<<<PAGE 31>>>）
- DHL 无缝切换规模边界：4000 VLAN 场景下无缝 failover 支持 128 VLAN/1000 MAC，超出需把 pre-empt timer 从 30 秒提到 60 秒防残留 MAC（P44，<<<PAGE 97>>>）
- ERP 与 MACsec 交互：单侧关闭 MACsec/MKA 时 R-APS 仍可交换、环可能回 Idle/RPL 阻塞——预期行为（P43，<<<PAGE 90-91>>>）

## B（反例/坑）
- 带 EVB 配置的交换机禁止升到 8.5R4 及以上（X6，<<<PAGE 16>>>）
- 8.10R3 起旧版 EVPN 配置必须手工迁入 VRF context（X5，<<<PAGE 18>>>）
- OVSDB 8.10R2 起移除；automatic fabric admin-state 8.10R2 起默认禁用（X68，<<<PAGE 17>>>）
- 分布式 ARP、WRED、qos dscp-table 于 8.6R2 移除；ip helper→ip dhcp relay（8.6R1，旧 vcboot.cfg 兼容）（X69，<<<PAGE 16>>>）
- 8.9R1 起 6560 Metro 特性转收费：CPE Test Head/PPPoE-IA/Ethernet OAM/SAA/Link OAM/VLAN Stacking/DPA/IPMVLAN 需 Metro 许可（X11，<<<PAGE 19>>>）
- 6560 两款电源（BP-PH 600W/BP-PX 920W）强制最低 AOS 8.8R1（X10，<<<PAGE 17>>>）
- mrp interconnect 三条命令 8.8R1 存在但不支持（X70，<<<PAGE 17>>>）；Kerberos Snooping 8.7R3 不支持 bridge mode（X71，<<<PAGE 17>>>）
- SPB Auto Fabric BVLAN 默认 16→4（8.7R1）仅对出厂默认且无 vcboot.cfg 的设备生效，升级不改存量（X72，<<<PAGE 17>>>）
- NTP 遵循 RFC 不再同步 stratum 16 服务器，OmniSwitch 级联对时的存量部署会断同步（P41，<<<PAGE 16>>>）
- WebView 法语支持 8.8R2 起移除，默认法语的设备升级后回落英语（X33，<<<PAGE 17>>>）
- 6570M TDR 仅限铜口：12/12D 口 1-8；U28 仅 hybrid 口 21-24 且 hybrid-mode=copper（X34，<<<PAGE 38>>>）
- FTP 用户名（RCD）上限 15 字符（X36，<<<PAGE 91>>>）；vcboot.cfg 含明文 key 导致哈希错误，必须用交换机生成的 hash-key/hash-salt（X37，<<<PAGE 91>>>）
- 软件获取卡停止随箱附带，软件走 Business Portal（X75，<<<PAGE 16>>>）；8.8R1 起 CVE-2024-6387（regreSSHion）修复默认内建（X74，<<<PAGE 17>>>）

## 来源
OmniSwitch AOS Release 8.10R4 Release Notes New Features（<<<PAGE 23-40>>>）、Licensed Features（<<<PAGE 19-20>>>）、New Hardware（<<<PAGE 21-22>>>）、Prerequisites 废弃清单（<<<PAGE 15-19>>>）、Appendix A Feature Matrix（<<<PAGE 52-61>>>）。条目来源：principles P8-P27/P31-P33/P36/P41/P43/P44/P45/P46/P48；counter-examples X5/X6/X10/X11/X33/X34/X36/X37/X68-X75；frameworks F4。
