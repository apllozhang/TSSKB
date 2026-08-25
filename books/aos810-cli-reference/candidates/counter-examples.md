# counter-examples — 命令限制/平台限定/互斥（X1…X24）

来源：代表章 Usage Guidelines/Notes 原文摘录整理（页码为 `<<<PAGE N>>>` 标记）。

## 平台限定

- **X1 spb bvlan 平台支持（第 10 章，<<<PAGE 745>>>）**：BVLAN 仅 6570M/6860/6860N/6865/6870/6900/6575/6920/9900 支持；6360/6465/6560 为 No。
- **X2 ip ospf spf-timer / hello-interval 平台（第 28 章，<<<PAGE 2409>>>/<<<PAGE 2434>>>）**：6360/6465 不支持；6560 起全部支持。
- **X3 ip bgp default local-preference / maximum-paths 平台（第 31 章，<<<PAGE 2759>>>/<<<PAGE 2776>>>）**：6360/6465/6575 不支持（6575 对 maximum-paths 为 No）。
- **X4 QoS Policy 章通用限制（第 39 章，<<<PAGE 3953>>>）**：原书明示"部分命令当前在一个或多个平台不受支持，需查各命令平台矩阵与 release notes"。

## 前置条件（必须先做什么）

- **X5 BGP 全局参数修改前必须停协议（第 31 章）**：`ip bgp default local-preference`、`ip bgp maximum-paths` 等命令要求先用 `ip bgp admin-state` 禁用 BGP 才能执行。
- **X6 PoE power rule 生效链（第 2 章，<<<PAGE 254>>>）**：power rule 必须先创建、再绑定到具体槽位/端口（经 lanpower power-policy）才生效；使用 lanpower power-policy 前必须已存在至少一条 power rule。
- **X7 PoE 802.3at 分级检测（第 2 章）**：要按 802.3at 供电必须先 `lanpower slot class-detection` 启用分级检测；802.3bt 下则自动启用、相关手工命令不受支持。
- **X8 路由协议加载（第 24/27/28/30/31 章）**：RIP/OSPF/IS-IS/BGP/VRRP 命令生效前需 `ip load <protocol>` 加载对应模块。
- **X9 OS 6465 PoE 电源（第 2 章）**：OmniSwitch 6465 不能自动检测电源类型，必须手工配置，否则系统与 PoE 功率信息显示错误。
- **X10 VC chassis id 生效时机（第 14 章，<<<PAGE 1198>>>）**：配置的 chassis identifier 要到目标机箱下次重启才生效。

## 互斥与冲突

- **X11 ISID 与 VRF 绑定互斥（第 10 章）**：同一 ISID 不能既绑定又重分发到同一 VRF 实例。
- **X12 linkagg 与 AppMon 互斥（第 13 章，<<<PAGE 1092>>>）**：链路聚合不能配置在 AppMon（应用监测）已启用的端口上。
- **X13 UNP multi-untag SAP 与 persistent profile 互斥（第 42 章，<<<PAGE 4470>>>）**：persistent profile 存在时两者互斥。
- **X14 Trust-Tagged VLAN 限制（第 42 章）**：私有 VLAN 不能配置为 Trust-Tagged VLAN；关联 Trust-Tagged VLAN 的 UNP profile 不能映射到 service domain；使用 Trust-Tagged VLAN 时端口的 Trust-Tag 必须禁用。
- **X15 动态 VLAN 删除限制（第 42 章）**：UNP 动态创建的 VLAN 不能用标准 `no vlan vlan_id` 删除。
- **X16 hash-control brief 模式退化（第 13 章）**：brief 模式下聚合哈希仅基于源 MAC（L2）或源 IP（L3），负载分担粒度下降。

## 使用限制与边界

- **X17 BVLAN 一致性要求（第 10 章，<<<PAGE 745>>>）**：每台 SPB 桥的 BVLAN 配置必须完全一致，否则 ISIS-SPB 邻居发现与最短路径计算失败。
- **X18 reserved VLAN 不可常规配置（第 7 章，<<<PAGE 476>>>）**：VLAN Stacking 的保留 VLAN 不能用标准 vlan 命令配置；NNI 口一旦成为 stacking 口，其 TPID（非 0x8100 时）不可再修改。
- **X19 legacy BPDU 双限制（第 7 章）**：legacy BPDU 仅当交换机处于 flat STP 模式时支持，且只应在连接 legacy 设备的 VLAN Stacking 网络端口上启用。
- **X20 VC 同型限制（第 14 章）**：Virtual Chassis 只支持同型号两台交换机之间（如 6860 与 6900 之间不支持）；`no virtual-chassis` 形式仅在交换机上无任何 VFL 配置时可用。
- **X21 PolicyView 规则只读（第 39 章，<<<PAGE 3953>>>）**：经 PolicyView 创建的规则不能经 CLI 修改（CLI 只能以更高优先级新建策略覆盖）。
- **X22 VLAN prompt-on-deletion（第 5 章，<<<PAGE 428>>>）**：默认删除带成员端口的 VLAN 不弹确认，误删风险由 prompt-on-deletion 参数兜底（默认 disable）。
- **X23 OSPF hello=0 语义（第 28 章，<<<PAGE 2434>>>）**：hello-interval 设 0 的含义是创建被动接口（不发送 hello），并非更快收敛。
- **X24 LLDP 控制帧默认丢弃（第 18 章，<<<PAGE 1390>>>）**：带标签与无标签 802.1AB 控制帧默认均丢弃，需 `ethernet-service uni` 显式配置处理方式。
