---
name: AOS 8 CLI 命令地图——组播/QoS/策略/准入域（组播/QoS/Policy Server/AAA/AG/AppMon，第 33-44/49/58 章）
description: 需要在 OmniSwitch AOS 8 上配置组播交换与路由（IPMS/MVR/PIM/DVMRP）、QoS 队列与策略（policy condition/action/rule/list）、AAA、Access Guardian/UNP、LPS、PPPoE-IA 时，用本地图定位 CLI Reference 对应章节与代表命令。
source_book: OmniSwitch AOS Release 810R04 CLI Reference User Guide
---

## R（触发场景）
- 查组播命令（ip igmp/ip pim/ip dvmrp/mvr/mcs）或 QoS 策略命令语法
- 写 QoS 策略：policy condition/action/rule/list 四级模型与 group 复用
- 部署准入：AAA、Access Guardian/UNP、Captive Portal、LPS、PPPoE-IA
- 策略经 PolicyView 创建后 CLI 改不动——优先级与只读规则核对

## I（核心理念）
策略模型（P23，<<<PAGE 3953>>>）：policy rule = policy condition + policy action；rule 编入 policy list 后生效；策略可经 CLI/SNMP/PolicyView（LDAP 端 GUI）三种途径创建。Access Guardian 架构（P29，<<<PAGE 4470>>>）：UNP（Universal Network Profile）为统一框架——端口使能 UNP 后对用户认证/分类进 profile，profile 映射 VLAN 或 SAP；组件含 BYOD（UPAM/ClearPass，含 mDNS/SSDP GRE 隧道）、Captive Portal、QMR、IoT Device Profiling；199 条为全书最大命令章。组播分层（F7）：三层组播（PIM/DVMRP/IGMP）与二层组播交换（MCS/MVR）分层。QoS 双章分工（P28）：第 38 章管硬件队列/调度/端口参数，第 39 章管策略软件模型。

## A1（决策框架）
1. **二层组播**→ 第 33 章（IPMS/MCS，106 条）/第 34 章（MVR）
2. **三层组播**→ 第 35 章 DVMRP /第 36 章 PIM /第 37 章 Multicast Routing
3. **QoS**→ 硬件队列第 38 章；策略模型第 39 章；Policy Server 第 40 章
4. **准入**→ AAA 第 41 章；Access Guardian/UNP 第 42 章；LPS 第 49 章；PPPoE-IA 第 58 章
5. **应用识别**→ 第 43 章 AppMon /第 44 章 Application Fingerprinting

## A2（操作步骤）·章节清单与代表命令
- **Ch33 IP Multicast Switching（<<<PAGE 3227>>>，约 106 条）**：`ip ms`/`ip igmp`（IGMP 侦听/MCS 二层组播交换）
- **Ch34 IP Multicast VLAN（<<<PAGE 3471>>>，约 12 条）**：`mvr`（组播 VLAN 业务通道）
- **Ch35 DVMRP（<<<PAGE 3495>>>，约 23 条）**：`ip dvmrp`
- **Ch36 PIM（<<<PAGE 3542>>>，约 99 条）**：`ip pim`（PIM-SM/SSM/DM）
- **Ch37 Multicast Routing（<<<PAGE 3769>>>，约 14 条）**：组播路由全局/边界/静态
- **Ch38 QoS（<<<PAGE 3797>>>，约 70 条）**：硬件队列/调度/端口 QoS 参数（P28）
- **Ch39 QoS Policy（<<<PAGE 3953>>>，约 111 条）**：`policy condition`（40+ 子命令：ip/ipv6/ip-port/tcp-port/udp-port/ethertype/tcpflags/service/icmp/tos/dscp/mac/vlan/802.1p/port/vrf/fragments/app-mon 等，inner 前缀支持 QinQ 内层字段）（P25）；`policy action`（disposition accept/drop/deny、cir+cbs/pir/pbs、802.1p/dscp 改写、redirect、mirror、port-disable 等）（P26）；`policy rule` 绑 condition+action；`policy list` 编排；`policy network/mac/port/vlan/map/service group` 成组复用（P27）
- **Ch40 Policy Server（<<<PAGE 4190>>>，约 9 条）**：LDAP 端 PolicyView 联动
- **Ch41 AAA（<<<PAGE 4205>>>，约 119 条）**：`aaa`/`radius`/`tacacs`（服务器组与认证方法链，为 AG 提供底座）（P31）
- **Ch42 Access Guardian（<<<PAGE 4470>>>，约 199 条）**：`unp` 全局配置（dynamic-vlan-configuration、auth-server-down、redirect 族、mac-mobility 等）与 profile 配置（trust-tagged-vlans、qos-policy-list、captive-portal 等），另加 port/domain/user/show 组（P29/P30）
- **Ch43 AppMon（<<<PAGE 4934>>>，约 37 条）**：应用识别与流量管控
- **Ch44 Application Fingerprinting（<<<PAGE 5016>>>，约 12 条）**：应用指纹库管理
- **Ch49 LPS（<<<PAGE 5212>>>，约 18 条）**：`lps`（学习型端口安全）
- **Ch58 PPPoE Intermediate Agent（<<<PAGE 5571>>>，约 12 条）**：`pppoe ia`

## E（实证案例）
- 命令地图型 skill，不搬运案例；原书每条命令自带 Example，按章首页码回查（cases 原件未创建）

## B（反例/坑）
- PolicyView 创建的规则不能经 CLI 修改（CLI 只能以更高优先级新建策略覆盖）（X21，<<<PAGE 3953>>>）
- QoS Policy 章部分命令在一个或多个平台不受支持，需查各命令平台矩阵与 release notes（X4，<<<PAGE 3953>>>）
- UNP multi-untag SAP 与 persistent profile 互斥（X13，<<<PAGE 4470>>>）
- 私有 VLAN 不能配置为 Trust-Tagged VLAN；关联 Trust-Tagged VLAN 的 UNP profile 不能映射到 service domain；使用时端口 Trust-Tag 必须禁用（X14）
- UNP 动态创建的 VLAN 不能用标准 `no vlan vlan_id` 删除（X15）
- linkagg 与 AppMon 互斥：聚合不能配在 AppMon 已启用的端口上（X12，<<<PAGE 1092>>>）
- Application Fingerprinting 规格表全平台 Currently not supported（Specifications Guide 佐证）

## 来源
OmniSwitch AOS Release 810R04 CLI Reference User Guide 第 33-44、49、58 章（<<<PAGE 3227-4205、4934-5039、5212-5256、5571-5597>>>）。条目来源：principles P23-P31；counter-examples X4/X12/X13/X14/X15/X21；frameworks F7/F8/F10。
