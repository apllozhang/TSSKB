# DIGEST — OmniSwitch AOS Release 8 Specifications Guide (8.10R4) 精华

本书是 AOS 8.10R4 的规格速查手册（98 页），按"特性 × 13 平台"矩阵给出最大值/支持项/RFC 清单，不含任何配置与 CLI（原书自述："This guide is designed to provide feature specification information only"）。它回答"能到多少"，不回答"怎么配"——配置去 Network Configuration / Advanced Routing 手册，命令查 CLI Reference。全书为纯规格表格，蒸馏以 glossary/principles/counter-examples 为主体（cases 为 0）。以下按三个技能单元摘要，页码均指原书。

## 一、知识地图（三技能单元）

1. **平台三梯队选型与规格解读法**（aos-spec-platform-tiers）：平台规模梯队（接入/汇聚/核心）、SM/RM/ER profile、VC"整机上限"语义与混搭白名单、管理面资源、文档地图（前言+Ch1+Ch2 前半，<<<PAGE 7-46>>>）。
2. **容量红线速查**（aos-spec-capacity-limits）：VC/链路层/SPB/VXLAN/EVPN/IP/路由/DHCP/组播/QoS/接入/OAM 全特性容量上限（Ch2+Ch3，<<<PAGE 27-86>>>）。
3. **TCAM 零和分配与特性支持矩阵**（aos-spec-tcam-features）：6870/6570M/6575 的 TCAM profile 档位权衡、平台 N/S 缺口清单（Ch4+Ch2 散点，<<<PAGE 87-92>>>）。

## 二、三单元要点串讲

### 1. 平台三梯队：先选梯队、再选 profile、最后对 TCAM 档位
平台规模三梯队框架（F2，<<<PAGE 30, 42>>>）：接入级（6360/6465/6560：MAC 16K、路由 32-2K、聚合 32 组）→ 汇聚级（6570M/6575/6860 系：MAC 32-64K、路由 12-13K、聚合 128）→ 核心/数据中心级（6870/6900/6920/9900：MAC 104-228K、路由 113-384K、聚合 252+）。VC 规格解读（F4，<<<PAGE 12, 23-24>>>）：maximum 默认作用于整 VC 而非单机（P13），三类例外要辨明——按机箱×成员数扩的、VC 封顶的（UNP 用户脚注 2，X35）、仅单机的（1588v2 VC-of-1）；混搭白名单之外 **6860N 与 OS686x 禁止混 VC**（X2）；6900 VC 的 ARP 总量=最低能力模块的值（X6，<<<PAGE 42>>>）。管理面全平台一致：Telnet 6/SSH 8/HTTP 4（P2）；各平台镜像与 USB 救援文件名体系见 P1/P5（<<<PAGE 14, 17>>>）。

### 2. 容量红线：许多容量互相反比
骨干选型：SPB（BVLAN 16、I-SID 512-8K 按平台，P19/P20）vs VXLAN（段 1600 万/SAP 8K/VTEP 500/VNI 4K/组播组 500，P22）vs EVPN on 6900（主机 10K 生成 20K RT2、业务 50、VRF 4，P23）。路由：硬件路由 6360 256 → 6900-X RM 312K，超限走软件路由（P16）；OSPF 区域 2-15、BGP 路由 2K-256K（P29）；6560 OSPF 仅 2 区域（X46）。容量反比规律：DHCP Snooping 条目按 VLAN 数反比缩放（P33）；PIMv4+PIMv6+DVMRP 接口合计 384 全局预算（P31）；UNP 用户 VC 两种脚注语义（X35，<<<PAGE 61>>>）；VLAN Stacking service 仅 4、SAP profile 带 QoS 时 8K 降 1K（X40，<<<PAGE 71>>>）；RMON 仅基础 4 组（X39）；L2 GRE Access 隧道多数平台仅 1 是 BYOD 规划瓶颈（X37）；6570M/6575 路由特性需 Advanced Routing license（X44）。

### 3. TCAM 零和：档位间是重分配，缺口不因版本改变
TCAM profile 机制（F3/P51，<<<PAGE 87>>>）：按应用分配 TCAM 规则数，配置后必须 reload 激活。6870 五档（Default/Metro services/QoS ACL/Source IPv6 ACL/Bidirectional IPv6 ACL）——QoS ACL 档 QoS 入规则 2048→4096 但 SAP 分类降到 1024（P52，<<<PAGE 89>>>）；6570M Fabric 档隧道与 UNP 换掉 PVLAN/VSTK（归零）与 QoS 入规则（P53，<<<PAGE 90>>>）；6575 特例：要 IPv6 snooping 只能选 Source IPv6 ACL 档（P54，<<<PAGE 92>>>）。平台 N/S 缺口是另一维度：MACsec 6360/6865/6900（除 X48C4E）/6920 不支持且需站点许可（X9）；Application Fingerprinting 全平台未实现（X12）；WRED 全平台 N/S（X13）；Ethernet OAM 不支持 6360 与 9900（X11）；MRP 仅 6465/6575/6865（X19）。

## 三、高价值章节页码索引

| 主题 | 页码 |
|---|---|
| 文档地图 / About | 7-11 |
| 镜像文件名 / 管理会话 / 内存 Flash / USB 救援 | 14-17 |
| SNMP / Web Services / AMS / OpenFlow | 20-22 |
| VC / VFL / 混搭白名单 / RCD / Automatic Fabric | 23-26 |
| 帧长 / MAC 三模式 / MACsec / PoE / UDLD | 29-30 |
| PVLAN / STP / HA VLAN / IPCL | 31-32 |
| SPB（BVLAN/I-SID/SAP/Inline Routing/RFP） | 33-34 |
| 聚合 / DHL | 35-36 |
| ERP / MVRP | 37-38 |
| VXLAN / EVPN | 39-40 |
| LLDP / ARP / IP 接口 / 静态路由 | 41-43 |
| VRF / IPv6 / IPsec / RIP / BFD | 44-49 |
| DHCP 全家（Relay/Snooping/Server/v6） | 50-53 |
| VRRP / SLB / IPMS 组播 / QoS | 54-58 |
| AAA / UNP / AG / QMR / Captive Portal | 60-62 |
| L2 GRE / mDNS / LPS | 62-65 |
| 镜像 / 端口监控 / sFlow / RMON / Switch Health | 66-70 |
| VLAN Stacking (QinQ) | 71 |
| Syslog / Ethernet OAM (MD/MA/MEP) | 72-73 |
| Link OAM / CPE Testhead / SAA / PPPoE-IA / MRP | 73-76 |
| OSPF / IS-IS / BGP / 组播边界 (MBR/SSM) | 77-86 |
| TCAM Profiles（6870/6570M/6575） | 87-92 |

## 四、条目统计与技能对应

verified 计数：principles 54 / counter-examples 50 / frameworks 4 / glossary 60 / cases 0（纯规格手册无配置流程）。技能对应：aos-spec-platform-tiers（F1/F2/F4+P1-P17+X1-X6/X42/X48）；aos-spec-capacity-limits（F2/F4+P16/P19-P50+容量类 X）；aos-spec-tcam-features（F3+P38/P51-P54+缺口类 X9-X13/X20-X22）。

## 五、一句话总纲

规格手册是网络设计的红线底座：先按三梯队选平台、再用 SM/RM/ER 放大规模、最后用 TCAM 档位换资源；所有"为什么超了/为什么缩水"（VC 整机语义、反比容量、零和 TCAM、N/S 缺口）都能在本手册矩阵中找到权威答案。
