# glossary — 术语表（OmniSwitch AOS 8.10R4 Specifications Guide）

格式：`- **术语**：中文解释 <<<PAGE N>>>`（页码为 fulltext.md 真实标记；按章分组）

## 系统与管理（Ch1）

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
