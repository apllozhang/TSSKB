---
name: OmniSwitch 纳管准备：SNMP 与基础网络初始化
description: 交换机默认不能被 OmniVista 管理，需要在设备侧配置 SNMP（v3 或 v1/v2 社区映射）、Loopback0 管理地址与路由，再交给 Discovery 纳管时使用。
source_book: DT00XTE311 OmniVista 2500 NMS Administration R4
---

## R（触发场景）
- 新装/出厂交换机要纳入 OV2500 管理，发现失败或 SNMP 超时
- 需要规划管理寻址（Loopback0）并验证全网管理路由可达
- 不确定 SNMP 安全级别（no security / authentication / privacy / traps only）怎么设

## I（核心理念）
OV2500 通过 SNMP/Traps 管理设备，而"By default, an OmniSwitch cannot be managed by OmniVista"——必须先在交换机侧开放 SNMP 访问。管理寻址推荐 Loopback0：snmp source ip 默认优先用 loopback0 作为源地址，Discovery 也用 Loopback0 地址发现设备。安全级别矩阵决定接受哪类请求，是安全与可用性的权衡。

## A1（行动框架）
1. **SNMPv3 准备（推荐）**，逐台执行（<<<PAGE 97>>>）：
   ```
   aaa authentication default local
   user snmpuserv3 read-write all password "Superuser=1" sha+des
   snmp security privacy all
   snmp authentication-trap enable
   snmp station 192.168.100.107 snmpuserv3 v3 enable
   snmp-trap absorption enable
   snmp-trap to-webview enable
   ```
2. **SNMPv1/v2 变体**（弱安全环境）：`snmp community map public user test1234 enable` + `snmp security no security`（<<<PAGE 68>>>）
3. **管理寻址**：`snmp source ip preferred {default | no-loopback | ip_address}`——Default 时有 loopback0 则用其作源 IP，否则用 IP 栈第一个可用地址（<<<PAGE 70>>>）
4. **基础网络初始化**：逐台配置 Loopback0（`ip interface Loopback0 address 192.168.200.x`）、vlan、ip interface、OSPF（`ip ospf area 0.0.0.0` + redist）、静态默认路由、LACP（`linkagg lacp agg 12`）、dhcp relay（<<<PAGE 92-95>>>）
5. **验证**：`show ip routes` 必须包含全部 Loopback0/32 路由；从核心机 ping 各 192.168.200.x（<<<PAGE 90-91>>>）

## A2（进阶应用）
- 安全级别矩阵（<<<PAGE 69>>>）：no security → 接受所有请求；authentication set → 接受 v1/v2 Get 及非认证 v3 Get；privacy all → 仅加密 v3 Set/Get；traps only → "All SNMP requests are rejected"（纯上报模式）
- CLI vs GUI 取舍：CLI 胜在熟练度/脚本化/"ASCII 配置文件可在交换机间复制粘贴"；GUI 胜在颜色编码、减少 fat-finger 错误、批量操作；WebView 是单设备原生网元管理器，"100% CLI equivalent features. Integrated with OmniVista"（<<<PAGE 22-24>>>）
- NMS 组件模型：Agents ↔ Managed Devices ↔ NMS，协议栈 SNMP、sFlow（Analytics）、MIB、Traps、RMON（<<<PAGE 21>>>）
- 4.3R2+ 可直接 SSH/Telnet 到尚未被 SNMP 覆盖的新设备做预配置（<<<PAGE 164>>>）

## E（实证案例）
- 六台交换机逐台执行 SNMPv3 命令序列后成功纳管——cases·SNMP 准备（<<<PAGE 97>>>）
- sw1(6900A) 至 sw8(6860B) 逐台初始化脚本（Loopback0+OSPF+LACP+DHCP relay）并通过 ping/路由验证——cases·基础网络初始化（<<<PAGE 90-95>>>）

## B（边界与陷阱）
- 默认状态下交换机不能被 OV 管理，"SNMP users and community strings need to be configured on devices before they can be managed by OmniVista"（<<<PAGE 97/164>>>）
- 路由表缺 Loopback0 地址属于环境级故障，不是配置失误——"IF THE ROUTING TABLE DOES NOT CONTAIN LOOPBACK0 ADDRESSES, PLEASE CONTACT THE TRAINER!"（<<<PAGE 90>>>）
- 初始化恢复命令块仅限初次配置失败时使用，且需培训师批准（<<<PAGE 92>>>）

## 来源
- principles·SNMP 安全级别矩阵（<<<PAGE 69>>>）、source address/Loopback0（<<<PAGE 70/90>>>）、NMS 组件模型（<<<PAGE 21>>>）、CLI vs GUI（<<<PAGE 22-24>>>）
- cases·SNMP 准备/基础网络初始化/恢复命令（<<<PAGE 97/68/92-95/90-91>>>）
- counter-examples·默认不可管理/路由表缺 Loopback0（<<<PAGE 97/164/90>>>）
