---
name: VM Manager 与 VXLAN/SPB Fabric
description: 需要纳管 vCenter/Hyper-V 虚拟机、配置 VM VLAN 流量塑形（UNP Tag 规则）、One-Touch SPB 自动生成、部署 VXLAN 核心（VFI/SAP/SDP/组播隧道）、VM Snooping 入库统计时使用。
source_book: OmniVista 2500 NMS 4.9R2 User Guide
---

## R（触发场景）
- vMotion 迁移后虚拟机网络配置要免改——VM VLAN + UNP 塑形
- 数据中心要 L2 over IP 大二层（VXLAN），段间 MAC 可重
- VM 迁移丢 UDP（SNMP）流量、历史定位出现 false positive
- VXLAN 封装包识别与策略入库（VM Snooping）

## I（核心理念）
VM Manager 纳管混合 vCenter（≤2 个）+Hyper-V，总 VM 上限 5000；流量塑形模型：VM 打 VLAN Tag → 交换机 UNP Tag 规则把 VM VLAN 映射到 UNP+VLAN → 每 VM VLAN 一个 UNP + 一条 VLAN Tag 分类规则 → VM 跨 Host 迁移免改配置。VXLAN 仅 OS6900-Q32/X72 支持：VXLAN Service = VFI（SAP 侧学客户 MAC + SDP 侧学网络 MAC），24 位 VNI 支持 1600 万隔离段。

## A1（行动框架）
1. **VM 纳管前置**（principles·P191，<<<PAGE 830-840>>>）：vCenter URL 需 /sdk 后缀；所有 Hypervisor 系统时间必须与 OV 同步；Hypervisor 连接口或本身须关链路发现协议（否则发 LLDP 被当成桥设备）
2. **Fabric 选型**：SPB 路线（OS10K/6900 AOS 7.3.1.R01+，需 Advanced License，One-Touch 自动生成）vs VXLAN 路线（OS6900-Q32/X72，ECMP 提升利用率）（principles·P192/P193）
3. **VM Snooping 模式**：Basic（UDP 端口+VNI+内层源 MAC+IPv4）vs Advanced（加 IP 协议+L4 端口，IPv6）（principles·P194，<<<PAGE 855-860>>>）

## A2（操作步骤）
- **VM VLAN 配置与 One-Touch SPB**：Exclude VLAN 让 OV 忽略管理类 VM VLAN；VLAN Notification 的 Active/Ignored 两列（有替代配置可 Ignore）；Resolve 向导自动修复缺失 Tag 规则——自动生成 UNP Profile 名 "UNP XX"（XX=VLAN ID）；SPB Profile 的 ISID=Starting ISID+VM VLAN ID（改起始值可建独立 L2 域），BVLAN 4 个轮转+各自 ECT ID；自动生成的 Profile Policy List 留空仅保连通，后续手工补（principles·P192，<<<PAGE 841-847>>>）
- **VXLAN 核心**：VXLAN Service=VFI；VNID 置 0 自动生成；删除 Service 须先禁用 Service 及关联 SAP/SDP；SDP 隧道须设备有 Loopback0（可跳转 VLANs 应用创建）；Unicast 隧道 Bidirectional（两端建 SDP）/Unidirectional；Multicast 隧道要求全部节点入同一 PIM 组（缺 PIM 配置会警告，可一键套默认）；SAP 每端口最多 8 个，Trusted 默认 True（principles·P193，<<<PAGE 848-852>>>）
- **VM Snooping**：Policy Mode Basic/Advanced；Policy Resource Default/Extended（策略数翻倍）；Aging 0-86400 默认 300（0=永不老化）；Trap Threshold 默认 80%；UDP 目的端口默认 4789 可加最多 7 个附加端口（多端口降低速度）；统计经 FTP/SFTP 收集（设备须配 CLI/FTP 凭据）；VSnoop Purge Scheduler 默认每 15 分钟（principles·P194，<<<PAGE 855-860>>>）
- **VM 定位**：Live Search 查实时位置；历史搜索有 false positive（旧 uplink 信息持久，用 Locator timestamp 判断）；连 Host 的交换机应加入 VMM Devices List 保证数据最新（principles·P191）

## E（实证案例）
- VM 跨 Host 迁移免改配置的完整链路（Tag→UNP 映射→分类规则）（principles·P191，<<<PAGE 830-840>>>）
- One-Touch SPB 自动生成 ISID/BVLAN/ECT 布局（principles·P192，<<<PAGE 841-847>>>）
- Resolve 向导修复缺失 Tag 规则（principles·P192）

## B（反例/坑）
- OV 自身跑在 VM 上时，VM 迁移可能丢 UDP（SNMP）流量（principles·P191，<<<PAGE 830-840>>>）
- 历史 VM 位置搜索有 false positive——旧 uplink 信息持久，须用 Locator timestamp 判断（principles·P191）
- VM Server 建后仅密码可编辑（principles·P191）
- SPB 自动生成依赖 One-Touch SPB 首配参数未被改动，改过须重新执行；同 Hypervisor 网络不同 ISID 的 VM 互不通信（principles·P192，<<<PAGE 841-847>>>）
- 非 SPB 设备自动跳过 SPB 属性仅更新桥接 UNP；VM Polling 间隔建议与 Discovery Regular Updates 一致（principles·P192）
- VXLAN Reapply 仅中间步骤失败可用——远端或首步失败则设备被移出且不可 Reapply（principles·P193，<<<PAGE 848-852>>>）
- Locator 的 802.1q Port Filtering 须用 Standard 模式否则 VM 检测不到（VM 用 tagged 包通信）（principles·P101，<<<PAGE 348-349>>>）
- 附加 Snooping UDP 端口勿用 IANA 保留口；多端口降低速度（principles·P194，<<<PAGE 855-860>>>）
- VXLAN 组播隧道要求全网 Multicast Mode 统一（Headend/Tandem 同 BVLAN 必须一致）（principles·P152，<<<PAGE 523-525>>>）

## 来源
OmniVista 2500 NMS 4.9R2 User Guide 第 36 章 VM Manager（<<<PAGE 830-847>>>）、第 37 章 VXLAN（<<<PAGE 848-860>>>）、SPB 概念（<<<PAGE 523-525>>>）。条目来源：principles P101/P152/P191-P194。
