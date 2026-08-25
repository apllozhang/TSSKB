---
name: AOS 8 TCAM 零和分配与特性支持矩阵（6870/6570M/6575 档位 + 平台 N/S 缺口）
description: 需要为 OmniSwitch 6870/6570M/6575 选择 TCAM profile、理解 QoS/SAP/UNP/VLAN Stacking 等特性的 TCAM 此消彼长、核对 MACsec/OAM/Fingerprinting 等平台缺口时使用。
source_book: OmniSwitch AOS Release 8 Specifications Guide (8.10R4)
---

## R（触发场景）
- 要开 QoS 入规则、SAP 分类、IPv6 ACL、SPB fabric 隧道等特性，TCAM 资源不够
- 6870/6570M/6575 选 TCAM profile 档位
- 部署前核对某特性在目标平台是否支持（MACsec/Ethernet OAM/UDLD/DHL 等 N/S 项）
- 特性组合上线后容量莫名缩水（SAP profile 带 QoS 降容、OAM 域挤占 RFP）

## I（核心理念）
TCAM profile 零和分配框架（F3，<<<PAGE 87-92>>>）：TCAM 总量固定，profile 在 QoS 入规则/SAP 分类/VSTK 翻译/业务隧道/DHCP snooping/UNP 用户/PVLAN 之间做此消彼长；配置后必须 reload 激活（P51）。选型三步——列出必开特性清单→逐 profile 核对资源列→接受牺牲项后 reload 生效。档位间是零和重分配（6870 QoS ACL 档 QoS 4096 但 SAP 从 2048 降到 1024，P52）；fabric 场景牺牲 VPN 特性换隧道容量（6570M Fabric 档 PVLAN/VSTK 归零，P53）。平台特性缺口是另一维度：N/S 矩阵项（MACsec/WRED/Fingerprinting 等）不因 TCAM 或版本改变。

## A1（决策框架）
1. **列必开清单**：QoS ACL 条数、SAP 分类数、IPv6 snooping、SPB 隧道数、UNP 用户数、PVLAN/VSTK 是否需要
2. **逐 profile 核对**：6870 五档（Default/Metro services/QoS ACL/Source IPv6 ACL/Bidirectional IPv6 ACL）、6570M 两档（Default/Fabric）、6575 三档（Default/Fabric/Source IPv6 ACL）（P51）
3. **接受牺牲项**：Fabric 档牺牲 QoS/PVLAN/VSTK；Source IPv6 ACL 档牺牲 QoS 入规则
4. **reload 生效**：TCAM profile 切换必须重启，安排维护窗
5. **平台缺口另查**：见 A2 的 N/S 清单，缺口特性直接换平台

## A2（操作步骤）·档位明细与平台缺口
- **6870 权衡典型**（P52，<<<PAGE 89>>>）：QoS Ingress Default 2048→QoS ACL 4096，但 SAP 分类 2048→1024；Metro services 档 VSTK 出方向翻译升到 1024 但业务隧道降 1024、UNP 用户降 1024
- **6570M Fabric 档**（P53，<<<PAGE 90>>>）：服务隧道 256→513（U28 达 1536）、UNP 用户 256→750（U28），代价 QoS 入规则 384→256、PVLAN/VSTK 归零
- **6575 双 fabric 特例**（P54，<<<PAGE 92>>>）：Fabric 档隧道 225→512 但 DHCPv6 ISF 为 0；要 IPv6 snooping 只能选 Source IPv6 ACL 档（DHCP6_RLY_ISF 81、AntiSpoofv6 53），代价 QoS 入 384→128
- **平台 N/S 缺口清单**：MACsec——6360、6865、6900（除 X48C4E）、6920 不支持，且需站点许可（X9，<<<PAGE 29>>>）；Fast/Perpetual PoE 仅 6360/6860/6860N/6865/6870，6575 无（X10）；Ethernet OAM(802.1ag/Y.1731) 不支持 6360 与 9900（X11）；Application Fingerprinting 全平台 Currently not supported（X12）；WRED 全平台 N/S（X13）；UDLD 在 6900-V72/C32 与 9900 不支持（X48C4E 除外）（X22）；DHL 在 6900-V72/C32 与 6920 不支持（X21）；CPE Testhead 仅 6465/6560/6570M/6575（X20）
- **TCAM 相关联动**：6870 QoS 规模依 TCAM profile 2K/4K（P38）；System TTI=SAP 分类资源名（UNI/SAP 流量映射 SVLAN/业务）（glossary，<<<PAGE 89>>>）

## E（实证案例）
- 本书为纯规格手册，无配置案例；"场景"即档位评审——三步法（清单→核对→接受牺牲+reload）走完后，去 Network Configuration Guide 对应特性章落地配置

## B（反例/坑）
- TCAM profile 配置后不 reload 不激活（P51，<<<PAGE 87>>>）
- Fabric 档下 PVLAN/VSTK 归零——还要用 QinQ 或 PVLAN 的节点不能上 Fabric 档（P53）
- 6575 要 SPB fabric 与 IPv6 snooping 二选一：Fabric 档无 DHCPv6 ISF，Source IPv6 ACL 档才有（P54）
- SPB RFP 域最多 8 且与其它 Ethernet OAM 域共享预算，已有 OAM 域时更少（X50，<<<PAGE 34>>>）
- SAP profile 一旦分配优先级/带宽，VLAN Stacking SAP 容量 8K 降到 1K（X40，<<<PAGE 71>>>）
- 6860 系 SPB MTU 当前不可配（固定 9K）（X49，<<<PAGE 34>>>）

## 来源
OmniSwitch AOS Release 8 Specifications Guide Ch4 TCAM Profiles（<<<PAGE 87-92>>>）、Ch2 平台支持矩阵散点（<<<PAGE 29-76>>>）。条目来源：principles P38/P51-P54；counter-examples X9-X13/X20-X22/X40/X49/X50；frameworks F3。
