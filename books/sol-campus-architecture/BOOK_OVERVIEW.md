# BOOK_OVERVIEW — sol-campus-architecture（移动园区架构，47 页）

## 书目构成（页码全册连续）

| 子文档 | 页码范围 | 内容 |
|---|---|---|
| DOC 1 ale_campus-architecture-guide-en.pdf（Mobile Campus Architecture Guide） | p1–43 | 园区网全栈设计：LAN（两层/三层模型、VC、VLAN/Trunk/LACP、SPB/EVPN/MPLS、动态路由）、WLAN（RF 规划、分布式控制面、桥接/隧道、管理模式、AP 接入、漫游、VLAN 池、QoS、Mesh/网桥/RAP/VoWLAN/mDNS/资产追踪）、NMS、安全（UPAM/NAC/ARP/认证/隔离/WCF/WIPS） |
| DOC 2 ale-hybrid-pol-solution-brochure-en.pdf（Hybrid POL 彩页） | p44–47 | 混合无源光局域网：POL+以太混合架构、降本点、适用画像、两种推荐架构与差异化优势 |

## 核心主线

1. **设计目标**（p5）：高可用、可扩展、安全、性能；Digital Age Networking 三支柱（自治网络、IoT 安全接入、业务创新自动化）。
2. **LAN 设计**（p6–12）：两层折叠核心 vs 三层模型取舍；VC/Stack；VLAN+MVRP 动态注册解决用户移动；Trunk/LACP；SPB/EVPN/MPLS 定位对比；OSPF/BGP/IS-IS/RIP 选型（RIP 不推荐）。
3. **WLAN 设计**（p12–35）：RF 规划七要素（覆盖/容量/信道/安装/功率天线/预测热图/RDA）；Stellar 无控制器分布式控制面（over-the-air + over-the-LAN）；数据面桥接 vs L2GRE 隧道按 ARP 动态选择；三种管理模式（Express/Enterprise/Cloud）；AP 组与 RF profile；AP-交换机接口（VLAN 域与服务域两套 discovery 流程与命令）；信任标签；漫游判定矩阵与 L2GRE L3 漫游；VLAN 池；WMM/DPI/带宽契约 QoS；六大专项用例。
4. **NMS**（p35–36）：OmniVista Enterprise（Standalone/L2 HA/L3 HA）与 Cirrus；AP call-home onboarding。
5. **安全**（p36–42）：UPAM 统一接入；角色化 ARP/UNP；Access Guardian；认证谱系（IoT 指纹/802.1x/访客自注册/SSID/BYOD）；Quarantine Manager；WCF；wIDS/wIPS（干扰 AP vs 流氓 AP）。
6. **Hybrid POL**（p44–47）：Nokia POL 光分配 + ALE 以太/无线；省铜缆/省机房/去汇聚层；两种推荐架构（SFP ONT+OmniSwitch vs 纯 ONT）；全层冗余与高级特性（SPB/ERP/MACsec）。

## 候选提取状态

- principles.md：P1…（目标 30–45 条）
- cases.md：C1…（部署/配置流程，目标 8–15 条）
- counter-examples.md：X1…（英文原句，目标 10–18 条）
- frameworks.md：F1…（目标 3–6 条）
- glossary.md：按主题分组（目标 35–50 条）
