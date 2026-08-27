---
name: AOS 8.10R4 软件特性需求矩阵精粹（Management/高可靠/L2/L3/QoS/安全/SPB/VXLAN/PoE 按域抽样）
description: 写交换机标书软件功能章节时使用：从 OmniSwitch Golden RFP 8.10R4 总表（97 页、12 个机型族）按功能域抽取的 80+ 条最有标书价值的需求条目，含虚拟化链路聚合 VC、ERPv2 环网、UNP 准入、SPB/EVPN-VXLAN fabric、Signed AOS 安全启动、PTP 授时等，附机型可用性与页码出处。
source_book: OMNISWITCH GOLDEN RFP - 8.10R4（grfp-sw-features，97 页）
---

## R（何时用）
- 标书软件功能章节需要逐条写"交换机必须支持……"式需求并给出 ALE 应答
- 快速判断某特性在哪个机型档位有/没有（如 ERPv2 只有部分接入机型列、VXLAN 只在中高端）
- 组标书功能矩阵：同一条目跨 OS6360→OS9900 抽样对比

## I（核心理念）
总表结构：每个机型族一张"Golden RFP – OSxxxx"，内分 Section 1-21 功能域，条目格式为"编号 + ALE 特性名 + 描述 + Pass C/PC/NC"。同一 Section 在不同机型的差异本身就是选型信息——例如 Section 8（Multi-technology fabric）与 Section 9（Service technologies，SPB 全家桶）只在 6575/6865/6870/6920 等中高端出现（6360/6465 版本无此节）；Section 19 Data Center 仅出现在 OS6920。下面按域抽样，页码为 sources/grfp-sw-features.md 的 <<<PAGE N>>> 标记。

## A1（决策要点）
选型时按四个档位判断需求下限：接入轻量（6360/6465）、接入堆叠（6560/6570M）、汇聚全功能（6575/6860N/6865/6870，带 SPB+EVPN-VXLAN fabric）、核心数据中心（6900/6920/9900，加 DC 节）。若招标需求包含 IEEE 802.1aq SPB 或 EVPN，低阶机型直接 NC，不要硬凑。

## A2（细节速查表）

**S1 Management**（P3 起，各机型均有）
| 条目 | 要点 | 出处 |
|---|---|---|
| Automatic Remote Configuration Download (RCL) | 大规模部署免手工逐台配置 | P3 |
| Dying Gasp | 断电经 SNMP/syslog 上报（光进铜退/远端局场景高频考点） | P3 |
| Embedded Python Scripting / RESTful API (SDN 20.1) | 内嵌 Python；可编程 OS RESTful API | P3, P8 |
| Thin Client 模式 | 本机不保存最终配置，由 NMS 下发 | P3 |

**S2 Resiliency / 高可靠**（P3-P4）
| 条目 | 要点 | 出处 |
|---|---|---|
| Virtual chassis up to 8 nodes | 多虚一统一管理，节点+链路冗余无需 STP/VRRP | P3 |
| VCSP 脑裂保护 | VC 分裂时子 VC 关闭面板端口防环路 | P4 |
| Remote virtual chassis | 最长 10km 远程堆叠 | P4 |
| STP(1X1/RSTP/MSTP) + LACP 802.3ad/802.1AX + LBD 非协议环检测 | 二层基本功组合 | P4 |
| VRRP with tracking（IPv4）/ VRRP v3（IPv6 节） | 网关冗余 | P4 |

**S3 Layer 2**
| 条目 | 要点 | 出处 |
|---|---|---|
| ITU-T G.8032/Y.1344 ERPv2 以太环网 | 重点圈阅项 | P3 |
| MVRP 动态 VLAN 注册传播 | 802.1Q 配套 | P3 |
| Port Mapping 用户口/网络口隔离 | 类似端口隔离私网 | P3 |
| LLDP + MED | 发现相邻设备/IP 电话 | P3 |

**S4/S5 IPv4/IPv6**：DHCP relay（v4/v6）、ARP 各变体（proxy/gratuitous/filtering）、ECMP、静态路由、DHCP Snooping/RA Guard/DHCP Guard 等 IPv6 安全套件（P4）。

**S6 QoS**
| 条目 | 要点 | 出处 |
|---|---|---|
| 入向分类标记：IP precedence / 802.1p / Auto QoS for IP Phone | 语音自动提优先级 | P5 |
| 每端口 8 个硬件出队列，QSP 队列模板（预定义+自定义），SP/WRR 调度 | 硬件 QoS 底座 | P5 |
| Condition groups + QoS policy list（多 IPv4/MAC/服务/端口/VLAN 组条件） | 策略颗粒度卖点 | P5 |
| 双向限速：ingress policing / egress shaping per port | 带宽管理 | P5 |

**S10 Security**（P6，以 6870 版最全）
| 条目 | 要点 | 出处 |
|---|---|---|
| Signed AOS Image（RSA-2048 + SHA-256 签名校验）+ Secure Boot + Uboot/ONIE 认证 | 供应链安全三件套 | P6/P64 |
| Change Password on First Access / ALE CA 签发证书 | 合规基线 | P6 |
| MACsec 点对点链路加密 + "MACsec on Network Port for SPB/L2GRE/VxLAN"；IPsec L3 | 数据面加密 | P64 |
| LPS（MAC 学习授权：按时限/按数量）+ Quarantine Manager 隔离用户 | 接入面管控 | P6/P65 |

**S11 Security framework / UNP 准入**
| 条目 | 要点 | 出处 |
|---|---|---|
| UNP 网络档案：MAC/802.1X/内外部 Captive Portal 认证后动态下发 VLAN、QoS、ACL | ALE 统一准入核心话术 | P6-P7 |
| IoT Device Profiling（DHCP fingerprinting + MAC OUI） | 物联网终端识别 | P7 |
| ARP Poisoning Protection + DoS Filtering（IPv4/IPv6）+ Storm control（广播/未知单播/组播限速，可 trap/shutdown） | 攻击防护组合 | P7/P65 |

**S8/S9 Fabric 与业务技术**（中高端，P63-64 为 6870 版）
| 条目 | 要点 | 出处 |
|---|---|---|
| Hardware-ready: EVPN over VXLAN / MPLS / GRE / VXLAN / SPB-M 802.1aq | 五种 fabric 硬件就绪声明 | P63 |
| SPB：PBB 802.1ah、≥16 ECT、head-end/tandem 复制组播、E-LINE/E-LAN/E-Tree/L3 VPN over I-SID、ERP over SPB | 运营商级以太网卖点最密一节 | P63-64 |
| L2 GRE 隧道及聚合终结（tunnel domain ↔ VLAN domain） | 跨 IP 网二层打通 | P65 |
| 17 Metro Ethernet（部分机型）：CFM/OAM 类需求 | 城域合规 | 对应机型节 |

**S12/S15/S16/S18/S21**
| 条目 | 要点 | 出处 |
|---|---|---|
| Timing：NTP v4/IPv6；中高端加 PTP 1588v2 End-to-End Transparent Clock；SyncE（高端/工业口） | 授时分档 | P7/P65 |
| SAA 流量生成测性能 | 网络健康测量 | P7 |
| PoE：Perpetual PoE、Fast PoE、PoE scheduling 定时供电、LLDP 802.3at功率 TLV、HPOE | PoE 六连问 | P7 |
| Monitoring：port mirroring（本地/远程/policy-based）、sFlow、RMON、Syslog | 可观测性全家桶 | P8 |
| Certifications：Common Criteria NDcPP (EAL1) 认证（附证书链接 st_vid11404） | 安全认证压舱石 | P8 |

核心路由（OS6900/9900）另有 OSPF/BGP/BFD/MPLS/VRF 大节，见该机型 Section 4/9（如 OS9900 从 P8131 行起）。

## E（场景案例/怎么用）
- 写"安全性要求"章节：把 S10+S11+S21 组合成三层叙事——供应链安全（签名镜像/安全启动/CC 认证）、数据面加密（MACsec/IPsec）、接入管控（UNP/IoT 识别/Quarantine），每层引 2-3 条原文条目标 C。
- 客户对比友商问"你们环网保护和 SPB 能不能共存"：直接引 "ERP Over SPB for Unicast Client / Multiple ERP ring over SPB"（P64）答 C。
- 写 PoE 章节：复制 S16 六条 + lan-access 单元的 budget 数字表。

## B（限制与坑）
- **分机型可用性必须核对**：上文每条都注明是哪个档位的版本；把 6870 才有的 MACsec-over-VXLAN 抄到 6360 标书就是虚假应答。通用做法：先查对应机型族那张表。
- Section 编号有跳号（无 S13/S14 于多数机型；S14 Industrial protocols、S17 Metro Ethernet 仅部分机型出现），抄编号前看原文。
- OCR 文本断行严重，条目描述要人工拼回完整句再引用英文原句。
- 版本锁定 AOS 8.10R4；客户环境更老/更新都要重新对版。

来源：OMNISWITCH GOLDEN RFP - 8.10R4（sources/grfp-sw-features.md，OS6360 P3-P8 / OS6870 P62-P66 为代表性引用页）
