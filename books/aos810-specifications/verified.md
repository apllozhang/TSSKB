# Verified 候选（V1 原文真实性核对 + V2/V3 抽查）

## counter-examples

## VC 组网限制
- **X1** 6920 与 OS9912 机箱完全不支持 VC；OS9907 仅 VC-of-2 且依赖 CMM/CFM 组合 <<<PAGE 23>>>/<<<PAGE 24>>>
- **X2** VC 混搭白名单只有这些：6900-V72/C32(E)/X48C6/T48C6/V48C8/X24C2/T24C2 之间（最多 6）；X48C4E 混上述型号需 mixed VFL 模式；6860+6865 可混；6465-P6/P12/P28/6465T 可混（用 1G SFP）；6360 10 口型仅 4 成员（SFP 口）。**OS6860N 与 OS686x 禁止混 VC**："OS6860N and OS686x models should not be mixed in a Virtual Chassis." <<<PAGE 24>>>
- **X3** MAC Learning Mode 在 OS6900 VC 上不支持 <<<PAGE 24>>>
- **X4** VFL 在 4X25G splitter 口上必须两侧 inter-frame gap=13，否则 CRC <<<PAGE 24>>>
- **X5** 1588v2 只支持 VC-of-1（跨 VC 不支持）；6570M/6860/6865/6870 不支持 10/100 半双工（CSMA/CD）<<<PAGE 29>>>
- **X6** VC 的 ARP 容量短板效应：6900 VC 的 ARP 总量=最低能力模块的值："Equal to capacity of module with lowest number of supported ARPs." <<<PAGE 42>>>
## 平台特性缺口（N/S 矩阵要点）
- **X9** MACsec 平台缺口：6360、6865、6900（除 X48C4E）、6920 不支持；需站点许可 <<<PAGE 29>>>
- **X10** Fast/Perpetual PoE 仅 6360/6860/6860N/6865/6870 支持（6575 无）<<<PAGE 29>>>
- **X11** Ethernet OAM(802.1ag/Y.1731) 不支持 OS6360 与 OS9900 <<<PAGE 73>>>
- **X12** Application Fingerprinting 全平台"Currently not supported"（规格表保留但无实现）<<<PAGE 64>>>
- **X13** WRED 全平台 N/S（8.6R2 起移除的遗留）<<<PAGE 58>>>
- **X15** BFD 不支持 IPv6 协议、不支持 Demand 模式 <<<PAGE 49>>>
- **X16** SLB 仅 6860/6860N/6865/6870/6900-X 支持 <<<PAGE 55>>>
- **X18** MBR（组播边界路由）不支持 6360/6465/6560/6570M <<<PAGE 86>>>
- **X19** MRP 仅 6465/6575/6865 三平台 <<<PAGE 76>>>
- **X20** CPE Testhead 仅 6465/6560/6570M/6575 <<<PAGE 74>>>
- **X21** DHL 在 6900-V72/C32 与 6920 不支持 <<<PAGE 36>>>
- **X22** UDLD 在 6900-V72/C32 与 9900 不支持（X48C4E 除外）<<<PAGE 30>>>
## 容量上限（规划红线）
- **X24** PVLAN 每端口/聚合成员上限：6560/6570M/6575/6920=256，6860 系/6870/6900=1；主 VLAN 下每口共存 secondary VLAN 仅 1 <<<PAGE 31>>>
- **X25** STP per-VLAN 实例：多数平台 100（6900/6920/9900 128）；Flat 模式 MSTI 16（另加 MSTI 0/CIST）<<<PAGE 32>>>
- **X26** HA VLAN：6570M/6575/6860/6860N/6865/6870=16，6865N=32，6360/6465/6560/6920/9900 不支持 <<<PAGE 32>>>
- **X27** MVRP VLAN 上限：6360/6465=256，其余 512 <<<PAGE 38>>>
- **X28** ERP 每节点 64 环、每环推荐 16 节点、WTR 1-12 分钟、guard 1-200 厘秒；dual end blocking 不支持 <<<PAGE 37>>>
- **X29** LLDP 每口 network policy 8；每 VC 8-32 <<<PAGE 41>>>
- **X31** 6360 静态路由仅 256（黑洞路由计入）；IPv6 接口 4、IPv6 静态路由 4 <<<PAGE 43>>>/<<<PAGE 46>>>
- **X32** IPv6 单播地址每接口 1 个（6575 需 AR 许可可 50）<<<PAGE 46>>>
- **X33** RIP 规模：接口 8-16、对等体 8-100、路由 128-10K；6560/6570M 路由 256（ECMP 下 1024）<<<PAGE 48>>>
- **X34** 认证服务器上限：单 authority 4（6900/6920 8）、多 authority 4/8 <<<PAGE 60>>>
- **X35** UNP 用户 VC 上限两种语义：多数平台=每机箱×成员数（脚注 1），但 6860 系/6900/6920 为 VC 封顶不随成员增加（脚注 2）："The maximum number of users per VC does not increase with additional chassis." <<<PAGE 61>>>
- **X36** Captive Portal 同时 Web 登录均值 40；profile 8；认证/计费服务器各认证类型 4 <<<PAGE 62>>>
- **X37** L2 GRE Access 隧道多数平台仅 1 条（6560/6570M 为 8）——BYOD 隧道规划瓶颈 <<<PAGE 63>>>
- **X38** 端口监控会话仅 1；镜像+监控合并会话 2-7 <<<PAGE 66>>>
- **X39** RMON 只有 4 基础组，Host/Matrix/Filter/捕获等 RMON2 功能必须外置探针 <<<PAGE 69>>>
- **X40** VLAN Stacking service 仅 4 个；SAP profile 一旦分配优先级/带宽，8K 降到 1K <<<PAGE 71>>>
- **X41** PPPoE-IA Circuit/Remote-ID 最长 63 字节、选项 5 个 <<<PAGE 75>>>
- **X42** 自动远程配置（RCD）限制：ISSU 与 IPv6 不支持；uboot/miniboot/FPGA 升级不支持；FTP/SFTP 用户名 15 字符；DHCP 租约尝试 6 次；OK LED 过程中闪琥珀 <<<PAGE 25>>>
- **X44** 6570M/6575 的 VRF、OSPF/OSPFv3/IS-IS、BGP 均需 Advanced Routing license；6560 的 OSPF/BGP 同 <<<PAGE 44>>>/<<<PAGE 79>>>-<<<PAGE 82>>>
- **X46** OSPF 区域上限：6560=2（AR 许可下）、6860/6870/6570M=4-8、6900-X/9900=10-15——6560 只能单区域+骨干 <<<PAGE 79>>>
- **X47** DHCPv6 snooping VLAN 数全平台 64；guard VLAN 64 <<<PAGE 51>>>/<<<PAGE 52>>>
- **X48** linkagg 聚合成员口 8-16，9900 的 ID 0/126/127 保留不可用 <<<PAGE 35>>>
- **X49** SPB MTU 在 6860 系"not configurable at this time"（固定 9K）<<<PAGE 34>>>
- **X50** SPB RFP 域最多 8（且与其它 Ethernet OAM 域共享预算，已有 OAM 域时更少）<<<PAGE 34>>>

---
合计：50 条（X1-X50）。

## frameworks

- **F1** AOS 文档地图四阶段法：Stage 1 首次开箱（硬件指南+Release Notes）→ Stage 2 熟悉单机（硬件指南+Switch Management Guide）→ Stage 3 入网（Network Config / Advanced Routing / Data Center Switching）→ Anytime（CLI Reference 全量命令）；本手册自身定位为四本配置手册的规格表配套，只答"能到多少"不答"怎么配"。 <<<PAGE 8>>>/<<<PAGE 9>>>
- **F2** 平台规模三梯队选型框架：接入级（6360/6465/6560：MAC 16K、路由 32-2K、聚合 32 组）→ 汇聚级（6570M/6575/6860 系：MAC 32-64K、路由 12-13K、聚合 128）→ 核心/数据中心级（6870/6900/6920/9900：MAC 104-228K、路由 113-384K、聚合 252+）；同级内再看 SM/RM/ER 转发 profile 二次放大。规划口诀：先选梯队、再选 profile、最后对 TCAM 档位。 <<<PAGE 30>>>/<<<PAGE 42>>>
- **F3** TCAM profile 零和分配框架：TCAM 总量固定，profile 在 QoS 入规则/SAP 分类/VSTK 翻译/业务隧道/DHCP snooping/UNP 用户/PVLAN 之间做此消彼长（如 6870 QoS ACL 档 QoS 4096 但 SAP 1024；6570M Fabric 档隧道+UNP 换掉 PVLAN/VSTK）；选型三步——列出必开特性清单→逐 profile 核对资源列→接受牺牲项后 reload 生效。 <<<PAGE 87>>>-<<<PAGE 92>>>
- **F4** VC 规格解读框架：所有 maximum 默认作用于整 VC（非单机）→ 三类例外要辨明——按机箱×成员数扩的（UNP 用户脚注 1 平台）、VC 封顶的（脚注 2 平台、6900 ARP 取最低模块）、仅单机的（1588v2 VC-of-1）；混搭先查白名单（6900 系内/6860+6865/6465 系内），6860N 是孤岛。 <<<PAGE 12>>>/<<<PAGE 23>>>/<<<PAGE 24>>>

---
合计：4 条（F1-F4）。

## glossary

- **Nosa/Nos/Wos/Dos/Uos/Uosn/Kaos/Yos/Ypos/Mos.img**：各平台 AOS 镜像文件名（6360/6465·6560/6570M/6575/6860·6865/6860N/6870/6900/6920/9900）<<<PAGE 14>>>
- **vcboot.cfg / vcsetup.cfg**：VC 启动/设置配置文件 <<<PAGE 14>>>
- **rescue.img（Narescue/Nrescue/Wrescue/Drescue/Urescue/Mrescue）**：各平台 USB 灾难恢复镜像；ONIE 机型走 ONIE 恢复 <<<PAGE 17>>>
- **ALE 认证 U 盘**：唯一支持的 USB 介质，FAT32 格式、目录名小写 <<<PAGE 17>>>
- **RUNNING 目录 30 字符限制**：作运行目录时文件/目录名上限 30 字符（普通场景 255）<<<PAGE 15>>>
- **Snapshot（命令捕获）**：把交换机配置捕获成文本文件的功能，含错误报告 <<<PAGE 18>>>
- **SNMPv3 USM/VACM**：基于用户的安全模型/视图访问控制（RFC 2574/2575），认证 SHA·MD5、加密 DES·AES <<<PAGE 20>>>
- **Web Services（Python API）**：HTTP/HTTPS+XML/JSON 的机内北向接口，4 会话，附 consumer.py 示例库 <<<PAGE 21>>>
- **AMS（AOS Micro Services）**：AOS 微服务框架，全平台支持 <<<PAGE 21>>>
- **RCD（Remote Chassis Detection）**：自动远程配置/零触摸特性；DHCP 客户端跑在 VLAN 1/tagged VLAN 127/LLDP 管理 VLAN <<<PAGE 23>>>/<<<PAGE 25>>>
- **Automatic Fabric**：自动 fabric 发现配置，支持 OSPFv2/v3、IS-IS v4/v6 自动配 IP（6360/6465 不支持高级路由）<<<PAGE 26>>>
- **Automatic LACP**：自动 LACP（tagged VLAN 127、untagged VLAN 1 上传递）<<<PAGE 25>>>

## VC/链路层（Ch1-2）
- **VC（Virtual Chassis）**：多台交换机组成单一逻辑机箱；最大值语义面向整 VC <<<PAGE 12>>>
- **VFL（Virtual Fabric Link）**：VC 内部互联链路；每机箱 peer 数、成员口数、端口类型因平台而异 <<<PAGE 23>>>
- **chassis-id / priority / group**：VC 成员编号（1-8）/优先级（0-255）/组（0-255）<<<PAGE 23>>>
- **Mixed VFL mode**：6900-X48C4E 与其它 6900 混 VC 时要求的 VFL 模式 <<<PAGE 24>>>
- **SM/RM/ER（Switch/Router/Edge-router Mode）**：三种 capability profile，决定 MAC/路由/ARP/ND 规模档位 <<<PAGE 30>>>
- **集中式 MAC 学习（Centralized MAC Source Learning）**：规格表 MAC 容量的前提模式 <<<PAGE 30>>>
- **Jumbo Frame**：1G+ 端口 9216 字节、10/100M 1553 字节 <<<PAGE 29>>>
- **IPCL/EPCL**：VLAN 级入/出端口分类列表规则（每 VLAN 256）<<<PAGE 31>>>
- **MSTI/CIST**：MSTP 实例（Flat 模式 16 个）与公共内部生成树 <<<PAGE 32>>>
- **HA VLAN（High Availability VLAN）**：服务器集群高可用 VLAN（16-32/VC）<<<PAGE 32>>>

## SPB/VXLAN/EVPN（Ch2）
- **SPBM（MAC-in-MAC）**：最短路径桥ging 的 MAC-in-MAC 模式（802.1aq/802.1ah）<<<PAGE 33>>>
- **BVLAN（Backbone VLAN）**：SPB 骨干 VLAN，每 VC 最多 16 <<<PAGE 33>>>
- **I-SID（Service Instance ID）**：SPB 业务实例标识（512-8K/VC）<<<PAGE 33>>>
- **ECT（Equal Cost Tree）**：等价树算法，ID 1-16 可分配给 BVLAN <<<PAGE 33>>>
- **Inline Routing（SPB）**：业务域内联路由形态（L3 VPN-Lite）<<<PAGE 34>>>
- **External Loopback Routing**：SPB L3 的外环回路由形态，与 Inline 互补 <<<PAGE 34>>>
- **RFP（Remote Fault Propagation）**：SPB 远端故障传播域（最多 8，与 OAM 域共享）<<<PAGE 34>>>
- **SAP（Service Access Point）**：业务接入点；VLAN Stacking 与 SPB/VXLAN 共用概念 <<<PAGE 34>>>/<<<PAGE 71>>>
- **VTEP**：VXLAN 隧道端点（网络内 500）<<<PAGE 39>>>
- **VNI（VXLAN Network ID）**：VXLAN 网络标识（4K）<<<PAGE 39>>>
- **BIDIR-PIM**：双向 PIM，VXLAN 组播下层协议 <<<PAGE 39>>>
- **Fabric VPN**：EVPN 对称 IRB 的 fabric 级 VPN 实体（4 个/VRF 对应 1 个）<<<PAGE 40>>>
- **RT2**：EVPN MAC/IP 通告路由（10K 主机生成 20K RT2）<<<PAGE 40>>>

## 路由与安全（Ch2-3）
- **VRF MAX/LOW profile**：VRF 实例规格两档（MAX 64/LOW 128 每 VC）<<<PAGE 44>>>
- **VRF Route Leaking**：VRF 间路由泄漏 <<<PAGE 44>>>
- **软件路由（Software Routing）**：硬件路由超限后的兜底路径，消耗内存与性能 <<<PAGE 43>>>
- **MSK（Master Security Key）**：IPsec 主安全密钥（16 字节 hex 或 16 字符字符串）<<<PAGE 47>>>
- **SPI**：IPsec 安全参数索引（256-999999999）<<<PAGE 47>>>
- **LSDB（Link State Database）**：链路状态数据库（OSPF/IS-IS 规格项）<<<PAGE 79>>>/<<<PAGE 81>>>
- **Route Leaking（IS-IS）**：IS-IS 两级前缀分发（RFC 2966）<<<PAGE 81>>>
- **Anycast RP**：任播 RP，PIM-SM 中多 RP 同地址（最多 8）<<<PAGE 86>>>
- **MBR（Multicast Border Router）**：PIM-SM 规范的组播边界路由功能，与 DVMRP 互操作 <<<PAGE 86>>>
- **SSM 地址段**：232.0.0.0/8（v4）与 FF3x::/32（v6）源特定组播保留段 <<<PAGE 85>>>

## 接入与 QoS（Ch2）
- **UNP（Universal Network Profile）**：统一网络 profile（4K/VC），分类后套用 VLAN/SPB/VXLAN 业务 <<<PAGE 61>>>
- **QMR（Quarantine Manager and Remediation）**：隔离与修复，隔离用户 256-1K <<<PAGE 62>>>
- **CPPM/UPAM**：ClearPass Policy Manager / User Profile Application Manager，BYOD 方案服务器 <<<PAGE 62>>>
- **COA/DM（RFC 3576）**：RADIUS 动态授权/断开请求，支持限 ClearPass <<<PAGE 62>>>
- **L2 GRE Access/Aggregation Tunnel**：BYOD mDNS/SSDP 的接入/汇聚隧道（Access 多数平台仅 1）<<<PAGE 63>>>
- **LPS（Learned Port Security）**：学习型端口安全；每口 1000 学习 MAC/100 过滤 MAC/8 范围；聚合口不适用 <<<PAGE 65>>>
- **RPMIR**：远程端口镜像（每会话 1 VLAN）<<<PAGE 66>>>
- **ENC 文件格式**：端口监控抓包文件格式（Network General Sniffer）<<<PAGE 67>>>
- **QSP（Queue Set Profile）**：队列组 profile（2-4 档；6920 NBDC-2/DCB-4）<<<PAGE 58>>>
- **VSTK（VLAN Stacking）**：QinQ 业务；SAP profile 带 QoS 时容量 8K→1K <<<PAGE 71>>>
- **SVLAN/CVLAN**：业务 VLAN/客户 VLAN（QinQ 外层/内层）<<<PAGE 71>>>

## 监控与 OAM（Ch2）
- **Switch Health**：资源利用率监控（CPU/带宽/内存/温度，60 秒原始样本）<<<PAGE 70>>>
- **RMON 4 组/RMON2**：内置仅 Statistics/History/Alarm/Events；RMON2 需外置探针 <<<PAGE 69>>>
- **sFlow 采样字段**：帧长/类型/MAC/VLAN/优先级/IP/端口/TCP flags/TOS <<<PAGE 68>>>
- **MD/MA/MEP（802.1ag）**：维护域（8）/维护关联（128）/维护端点（256）<<<PAGE 72>>>
- **CCM**：连通性检查消息，最小间隔 100ms <<<PAGE 73>>>
- **Link OAM（802.3ah/EFM）**：链路级 OAM，镜像口不支持 <<<PAGE 73>>>
- **CPE Testhead**：UNI 入向测试头（Generator/Analyzer/Loopback 三角色）<<<PAGE 74>>>
- **SAA（Switch Access Agent）**：业务活性探测（128 会话；SPB SAA 每 BVLAN 128）<<<PAGE 75>>>
- **MRP（Media Redundancy Protocol）**：IEC 62439-2 工业环网（3 环/50 节点/200·500ms）<<<PAGE 76>>>
- **PPPoE-IA**：PPPoE 中间代理（Circuit/Remote-ID 各 63 字节）<<<PAGE 75>>>

## TCAM（Ch4）
- **TCAM Profile**：按应用分配 TCAM 规则数的档位配置，reload 生效 <<<PAGE 87>>>
- **6870 五档 profile**：Default / Metro services / QoS ACL / Source IPv6 ACL / Bidirectional IPv6 ACL <<<PAGE 89>>>
- **Fabric profile（6570M/6575）**：面向 SPB fabric 的档位（隧道/UNP 增、QoS/PVLAN 减）<<<PAGE 90>>>/<<<PAGE 92>>>
- **System TTI**：SAP 分类 TCAM 资源名（UNI/SAP 流量映射 SVLAN/业务）<<<PAGE 89>>>
- **Qos-AntiSpoof / v6**：QoS 防欺骗 TCAM 资源（v6 变体仅特定 profile 有）<<<PAGE 89>>>

---
合计：60 条。

## principles

## 平台资源基线（Ch1）
- **P1** 13 平台镜像文件名体系：6360=Nosa.img、6465/6560=Nos.img、6570M=Wos.img、6575=Dos.img、6860/6865=Uos.img、6860N=Uosn.img、6870=Kaos.img、6900=Yos.img、6920=Ypos.img、9900=Mhost.img+Mos.img+Meni.img；VC 配置文件 vcboot.cfg/vcsetup.cfg <<<PAGE 14>>>
- **P2** 管理会话并发上限全平台一致：Telnet 6、SSH 8、HTTP(WebView) 4；SSH 公钥支持 Password/DSA/RSA/ECDSA <<<PAGE 14>>>
- **P4** 内存/Flash 平台矩阵：6360=1G/1G、6570M=2G/8G、6575=2G/4G、6860N=4G/16G、6870=8G/32G、6900-X 系列=8G/32G（V48C8/C32E=16G/64G 物理 32G 分区）、6920=32G/64G、9900=16G（9907 2G Flash/9912 32G）<<<PAGE 16>>>
- **P5** USB 灾难恢复按平台用对应 rescue 镜像（Narescue/Nrescue/Wrescue/Drescue/Urescue/Mrescue.img），6860N/6870/6900/6920 为 ONIE-based；ALE 认证 U 盘必须 FAT32、目录名小写 <<<PAGE 17>>>
- **P7** SNMPv3 安全栈：认证 SHA/MD5、加密 DES/AES，请求类型覆盖非认证/认证/加密三档 Sets/Gets/Get-Nexts；v1/v2 仅 community 无加密 <<<PAGE 20>>>
- **P8** Web Services：HTTP/HTTPS + Python API，响应 XML/JSON，最大 4 会话；内嵌 Python 3；AMS 全平台支持 <<<PAGE 21>>>
- **P9** OpenFlow 仅 6860 支持：Normal/Hybrid(API) 模式、版本 1.0/1.3.1、每逻辑交换机 3 控制器、最多 3 逻辑交换机（Hybrid 1）、流表 1535、MAC 表 48K、TCP 6633、支持 VC <<<PAGE 22>>>
## VC 与链路（Ch1-2）
- **P11** VC 成员数平台档：6360 24/48 口=8（10 口=4）、6465=4、6560/6570M/6860/6865/6870=8、6575=4、6900-X=6、9907=2、9912/6920 不支持；chassis-id/priority/group 范围 1-8/0-255/0-255 <<<PAGE 23>>>
- **P12** VFL 规格三档：多数平台每机箱 2 peer、每 VFL 8 成员口、VFL id 0-1；6900 每 5 peer、16 成员口、VFL id 0-4；控制 VLAN 2-4094、hello 间隔 1-65535 <<<PAGE 23>>>
- **P13** VC 最大值语义：文档中的 maximum 对整个 VC 生效而非单机，除非另行说明："Any maximum limitation values documented apply to the entire Virtual Chassis and not to each individual switch unless stated otherwise." <<<PAGE 12>>>
- **P14** 最大帧长两级：10/100M 口 1553 字节、1G/10G/40G/100G 口 9216 字节（巨帧）；EEE/802.3az 全平台 <<<PAGE 29>>>
- **P16** 路由软超载机制：硬件路由超限时旧的不常用路由移入软件、活跃路由保硬件，总路由量取决于内存——超出即部分流量走软件路由："Exceeding the maximum hardware routes will result in some traffic being routed in software." <<<PAGE 43>>>
- **P17** 聚合规模梯度：6360/6465/6560=32 组×8 口；6570M 静态 32/LACP 96；6860 系=128×16；6870=252 组；6920=253 组×16；9900 ID 0/126/127 保留 <<<PAGE 35>>>/<<<PAGE 36>>>
## SPB/VXLAN/EVPN（Ch2）
- **P19** SPB 实现为 SPBM(MAC-in-MAC)+IP over SPBM；ISIS-SPB 实例每 VC 1 个；BVLAN 16（但 Release Notes 建议 Auto Fabric 默认收敛到 4）；ECT 算法 1-16 可选 <<<PAGE 33>>>
- **P20** I-SID/SAP 规模梯队：6570M/6575=512、6860 系=2K、6900-X48C6 等=8K（X/T24C2 2K）、9900=1K；每 I-SID VLAN/SVLAN 数 2K-4K；SPB MTU 9K（6860 系当前不可配） <<<PAGE 33>>>/<<<PAGE 34>>>
- **P22** VXLAN（6860N/6870/6900）：段 1600 万、业务实例/SAP 8K、VTEP 500、VNI 4K、组播组 500（BIDIR-PIM）、UDP 目的端口可配 8 个（默认 4789）、每接入口 VLAN 范围 SAP 8 个 <<<PAGE 39>>>
- **P23** EVPN（6900）规模画像：主机 10K（生成 20K RT2）、业务 50（全 IRB）、VRF 4、Fabric VPN 4、前缀路由 500、组播组 200（OISM+PEG 全启用）、接入连接 140（100 单归属+40 多归属）；RFC 7432/9135/9136/9161/9251/9625 <<<PAGE 40>>>
## IP/IPv6/路由（Ch2-3）
- **P24** IP 接口规模：每系统 128-4K（6465 仅 24）；每 VLAN 路由接口 8-32；硬件路由从 6360 的 256 到 6900-X RM 312K 梯度分布（SM/RM/ER 三态） <<<PAGE 42>>>
- **P26** IPv6 硬件路由 128-bit/64-bit 双轨：如 6900-X48C6 RM 156K(128-bit)/64K(64-bit)；IPv6 主机（ND）SM/RM/ER 三态（如 6900-X 32K SM/24K ER/8K RM）<<<PAGE 46>>>
- **P27** VRF 两档 profile：MAX profile（64 实例/VC，6900-X 达 28-300 LOW 混布）与 LOW profile（128/VC）；每 VLAN 仅 1 VRF；OSPF/RIP VRF 实例 16、BGP 32 <<<PAGE 44>>>
- **P28** IPsec 仅 6860/6865：ESP 加密 NULL/3DES-CBC/AES-CBC(128/192/256)，AH 认证 HMAC-SHA1/MD5/AES-XCBC/SHA256/384/512，仅 Transport 模式，策略优先级 1-1000、规则 index 1-10、SPI 256-999999999 <<<PAGE 47>>>
- **P29** 路由协议规模基线：OSPF 区域 2-15、接口 8-200、LSDB 1K-100K、路由 512-64K（9900）；IS-IS 区域 3、L1/L2 邻接每口 70、路由 24K（L1 12K+L2 12K）；BGP 对等 32-512（每 VRF 32）、路由 2K-256K（9900）<<<PAGE 79>>>-<<<PAGE 82>>>
- **P30** BFD 会话：每机箱 32 / 每 VC 100；联动 BGP/OSPF/VRRP 远地址跟踪/静态路由；IPv6 协议不支持；仅异步 Echo 模式 <<<PAGE 49>>>
- **P31** 组播接口预算：PIMv4+PIMv6+DVMRP 合计 384 接口；PIM 与 DVMRP 不能同接口；RP 100、BSR 1、SSM v4 段 232.0.0.0/8、v6 段 FF3x::/32 <<<PAGE 84>>>/<<<PAGE 85>>>
- **P33** DHCP Snooping 源过滤条目按 VLAN 数反比缩放：如 6860 系 32 VLAN×223 客户端 / 4 VLAN×251 客户端；端口级 253-254 客户端；VC 的 VLAN 级条目=单机值×VC 成员数 <<<PAGE 51>>>
- **P34** 内部 DHCP Server：租约 8000、租约文件 375K；静态 BootP/静态 DHCP/动态 DHCP 三种分配；v4 配置 dhcpd.conf/pcy/dhcpsrv.db、v6 同构三件套 <<<PAGE 53>>>
- **P36** SLB（6860/6865/6870/6900-X）：32 集群×32 物理服务器；L3 按目的 IP、L2 走 QoS 条件；健康检查 Ping+链路；高可用=硬件 failover/VRRP/CMM 冗余 <<<PAGE 55>>>
- **P37** 组播流（IPMS）规模梯队：接入 1K、6860 系 12K-40K（6860N 40K）、6900-X 40K、9900 128K；v6（MLD v1/v2）对应 1K-128K <<<PAGE 56>>>/<<<PAGE 57>>>
- **P38** QoS 规模：策略规则/条件/动作三值相等（128-4K，6870 依 TCAM profile 2K/4K）；组数 1023-2047；每组条目 128-1024（service 组 256）；每口 8 CoS 队列；QSP 2-4（6920 NBDC-2/DCB-4）；策略列表 32（含默认）、每 UNP 1 个；WRED 全平台 N/S <<<PAGE 58>>>
- **P39** AAA 服务器：认证服务器单/多 authority 模式各 4-8；AG 每认证类型（MAC/802.1X/CP）4 认证+4 计费服务器；AAA profile 8、CP profile 8；BYOD 服务器 CPPM/UPAM；COA RFC 3576 支持限 ClearPass <<<PAGE 60>>>/<<<PAGE 62>>>
- **P40** UNP/AG 用户规模：AG 用户系统级 320-1K（6900 每 NI 1K/VC 2K）；QMR 隔离 256-1K；Captive Portal 同时登录均值 40；UNP profile 4K/VC（6920 2K）；UNP 用户每机箱 80-2K、每 VC 求和或封顶（依平台脚注 1/2）<<<PAGE 61>>>/<<<PAGE 62>>>
- **P41** L2 GRE 隧道：Access 隧道多数平台 1（6560/6570M 8）；Aggregation 隧道 6860 系 2K（6900 8K、9900 1K）；mDNS/SSDP GRE 仅 IPv4 <<<PAGE 62>>>/<<<PAGE 63>>>
- **P42** LPS 规则：每口学习 MAC 1000、过滤 MAC 100、MAC 范围 8；聚合口与 trunk 聚合口不适用 <<<PAGE 65>>>
- **P43** 端口镜像/监控会话：镜像会话 2-7、监控会话 1；合并上限与镜像会话同值；N-to-1 镜像 128:1；镜像目的地每会话 1-2（9900 128）；RPMIR 每会话 1 VLAN；监控文件格式 ENC（Sniffer）<<<PAGE 66>>>/<<<PAGE 67>>>
- **P44** sFlow：Receiver/Sampler/Polling 实例 2；采样字段含帧长/类型/MAC/VLAN/优先级/IP/端口/TCP flags/TOS；轮询 10 项计数器 <<<PAGE 68>>>
- **P45** RMON 仅基础 4 组（Statistics/History/Alarm/Events），10 组与 RMON2 需外置探针；History 间隔 1-3600 秒、Alarm 间隔 1-2147483647 秒、trap Rising/Falling <<<PAGE 69>>>
- **P46** Switch Health 语义：资源利用率记录当前/1 分钟均值/1 小时均值/1 小时最大，原始样本保留 60 秒；利用率 0=未测量、1=<2% 的非零值；阈值跨 switch/module/port 全层级自动生效 <<<PAGE 70>>>
- **P47** VLAN Stacking（QinQ）：service 4、SVLAN 4K、SAP 8K；SAP profile 8K（分配优先级/带宽时降为 1K）；每 SAP CVLAN 4K（6860 3.5K）；6900 系 SAP-UNI-CVLAN 3072 <<<PAGE 71>>>
- **P48** Syslog：RFC 5424、12 服务器、级别 2-9（Alarm→Debug3）；Ethernet OAM（802.1ag/Y.1731）MD 8/MA 128/MEP 256、最小 CCM 100ms <<<PAGE 72>>>
- **P49** Link OAM（802.3ah）支持 6465-6575-6860 系-6870，镜像口不支持；CPE Testhead（6465/6560/6570M/6575）每机 32 测试 ID、同时仅 1 活动测试、角色 Generator/Analyzer/Loopback <<<PAGE 73>>>/<<<PAGE 74>>>
- **P50** SAA 128 会话；SPB SAA 每 BVLAN 128（9900 320）；MRP（6465/6575/6865）3 环、50 节点、重组时间 200/500ms（IEC 62439-2）<<<PAGE 75>>>/<<<PAGE 76>>>
## TCAM Profile 机制（Ch4）
- **P51** TCAM profile 机制本质：按应用分配不同数量的 TCAM 规则，配置后必须 reload 激活；6870 五档（Default/Metro services/QoS ACL/Source IPv6 ACL/Bidirectional IPv6 ACL），6570M 两档（Default/Fabric），6575 三档（Default/Fabric/Source IPv6 ACL）："The user can configure the required TCAM profile and reload the switch to activate the configured TCAM profile." <<<PAGE 87>>>
- **P52** 6870 TCAM 权衡典型：QoS Ingress Default 2048→QoS ACL 4096，但 SAP 分类从 2048 降到 1024；Metro services 档 VSTK 出方向翻译升到 1024 但业务隧道降到 1024、UNP 用户降到 1024——档位间是零和重分配 <<<PAGE 89>>>
- **P53** 6570M Fabric 档：服务隧道 256→513（U28 达 1536）、UNP 用户 256→750（U28），代价是 QoS 入规则 384→256、PVLAN/VSTK 归零——fabric 场景牺牲 VPN 特性换隧道容量 <<<PAGE 90>>>
- **P54** 6575 双 fabric 特例：Fabric 档把隧道 225→512，且 DHCPv6 ISF 保持 0；要 IPv6 snooping 只能选 Source IPv6 ACL 档（DHCP6_RLY_ISF 81、AntiSpoofv6 53），代价 QoS 入 384→128 <<<PAGE 92>>>

---
合计：54 条（P1-P54）。
