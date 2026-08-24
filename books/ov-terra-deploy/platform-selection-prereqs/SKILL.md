---
name: 平台选型与前置条件
description: 当需要在 OmniVista Cirrus（SaaS）与 OmniVista Terra（本地部署）之间做选型，或部署前核对容量、防火墙端口、设备软件版本要求时使用。
source_book: DT00XTE317 OmniVista Cirrus/Terra Deployment and Configuration
---

## R（触发场景）
- 客户问"上云还是本地部署"，需要 Cirrus vs Terra 的差异对比
- 项目规划阶段需要核对防火墙端口开通清单、NTP/DHCP 前置
- 存量 AP/交换机软件版本老旧，不确定能否被平台纳管

## I（核心理念）
OmniVista 家族有两条产品线：Cirrus 是 SaaS 模式零部署（"Zero Deployment"），Terra 是客户自托管的本地部署 3-VM 集群、单租户。两者功能对等（Features parity）、商业结构一致、UI 体验一致，核心差异在容量上限与网络前置条件。选型的第一步永远是核对设备型号与软件版本的准入门槛。

## A1（行动框架）
1. **产品定位对比**：Cirrus = SaaS、零部署（<<<PAGE 5>>>）；Terra = On-Premises、虚拟化 3-VM 集群、单租户（<<<PAGE 13>>><<<PAGE 14>>>）。
2. **容量核对**：
   - Cirrus：最多 12000 台网络设备（10000 AP + 2000 OmniSwitch）（<<<PAGE 6>>>）
   - Terra：最多 2000 台（1600 Stellar AP + 400 OmniSwitch）（<<<PAGE 14>>>）
3. **防火墙端口清单**：
   - Cirrus：AP→云需开放 9093/30123/30124/30125，出向 443/80/123/53（<<<PAGE 9>>><<<PAGE 18>>>）
   - Terra：仅需出向 443/80/123/53（<<<PAGE 18>>><<<PAGE 140>>>）
4. **DHCP/NTP 前置**：标准 options 1,3,6,28,42,43；使用代理时加 129-133,138；至少 1 个 NTP 服务器（<<<PAGE 9>>><<<PAGE 18>>>）。
5. **设备软件版本门槛**：
   - Stellar AP：Cirrus 要求 AWOS 4.0.6 GA+，Terra 要求 AWOS 4.0.7.14+（<<<PAGE 9>>><<<PAGE 18>>>）
   - OmniSwitch：Cirrus 要求 AOS 8.9R1+，Terra 要求 AOS 8.9.82R01+（<<<PAGE 9>>><<<PAGE 18>>>）

## A2（进阶应用）
- 超过 2000 台规模或合规要求本地化数据时选 Terra，否则 Cirrus 运维成本更低。
- Terra 与 Cirrus 功能对等、商业结构相同（"Same commercial structure than OVCX … Consistent User Interface & Experience"，<<<PAGE 17>>>），跨平台技能可复用。
- 老旧 AP1101 不兼容 RAP（远程 AP）特性（<<<PAGE 421>>>），远程办公场景需提前排除。

## E（实证案例）
- **案例 1**：客户全网 8000 AP，若选 Terra（上限 1600 AP）将无法承载，必须选 Cirrus（上限 10000 AP）（<<<PAGE 6>>><<<PAGE 14>>>）。
- **案例 2**：Cirrus 场景客户防火墙只开了 443，AP 无法激活——因为 AP→云还需要 9093/30123/30124/30125（<<<PAGE 9>>>）。

## B（边界与陷阱）
- **不支持型号禁区**：AP1101、AP1201L/H/HL 不被支持（"All Stellar models supported, except: AP1101, AP1201L/H/HL"，<<<PAGE 9>>><<<PAGE 18>>><<<PAGE 140>>>）。
- **版本混查陷阱**：Cirrus 与 Terra 的最低版本要求不同，照 Cirrus 文档给 Terra 项目定版本会翻车（<<<PAGE 9>>><<<PAGE 18>>>）。

## 来源
- principles·Cirrus vs Terra 产品定位差异（<<<PAGE 5>>><<<PAGE 13>>><<<PAGE 14>>>）
- principles·容量差异 12000 vs 2000（<<<PAGE 6>>><<<PAGE 14>>>）
- principles·Terra 功能与 Cirrus 对等（<<<PAGE 14>>><<<PAGE 17>>>）
- principles·防火墙端口差异（<<<PAGE 9>>><<<PAGE 18>>><<<PAGE 140>>>）
- principles·设备软件版本前置（<<<PAGE 9>>><<<PAGE 18>>>）
- counter-examples·不支持的 AP 型号（<<<PAGE 9>>><<<PAGE 18>>><<<PAGE 140>>>）
