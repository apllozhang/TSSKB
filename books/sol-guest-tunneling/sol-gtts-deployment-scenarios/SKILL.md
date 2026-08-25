---
name: GTTS 部署场景（DMZ 访客隧道/园区多站汇聚/单机多租户）
description: 需要为访客隔离、园区多站点或运营商多租户选择并落地 GTTS 部署架构时使用：三用例定位（访客/安全策略/迁移）、DMZ 三区隔离基线、Campus AP Group 统一隧道到数据中心、单台聚合交换机多客户隔离的选型与配置要点。
source_book: Guest Traffic Tunnelling Services Application Note (23032701, April 2023)
---

## R（触发场景）
- 客户要把 Guest SSID 与内网彻底隔离（只出 Internet）
- 校园/医院/多分支：同一批 SSID 多站点广播、流量统一汇聚到数据中心施策
- 运营商/SP：多客户流量集中终结、客户间逻辑隔离
- 从控制器架构迁移分布式，边缘不想加 VLAN（迁移用例）
- IPS 等安全设备需串在无线流量路径上（bump in the wire）

## I（核心理念）
三用例 × 三场景体系（F1）：用例决定"为什么隧道"——访客隔离（DMZ 终点只出 Internet）、安全策略（中心 scrub/IPS 串行）、迁移（边缘零新增 VLAN，VLAN 只配中心）（<<<PAGE 3>>>）。场景决定"落在哪"：DMZ 基线（Corporate/DMZ/External 三区防火墙分隔，访客"第一扇门"开在 DMZ，病毒在防火墙处失效，C3，<<<PAGE 11>>>）；Campus（AP Group 粒度使多站点同 SSID 同隧道终点，C4，<<<PAGE 12>>>）；多租户（每客户一 AP Group + 运营商交换机 IP，借 SD-WAN/SPB/MPLS 既有链路，C5，<<<PAGE 13>>>）。三个场景的聚合交换机配置完全同一套（p9 五步）。

## A1（行动框架）
1. 用例定位：访客隔离 / 安全串行 / 迁移免扩 VLAN（<<<PAGE 3>>>）
2. 场景选型（按组织形态）：单企业→DMZ；多站点园区→Campus 汇聚数据中心；SP 服务多客户→单机多租户
3. 安全边界设计：聚合交换机置于 DMZ/防火墙围护区；DHCP 部署同区（<<<PAGE 4>>><<<PAGE 11>>>）
4. AP Group 规划：园区=全站 AP 一组；多租户=每客户一组（各自 OmniVista 亦可）
5. 传输链路确认：跨网时核对 MTU+24B 与运营商协商（<<<PAGE 8>>>）
6. 套用交换机五步 + AP Use Tunnel 配置（见 sol-gtts-architecture-config）

## A2（操作步骤）
- **DMZ 访客隧道**（C3，<<<PAGE 11>>>）：Guest SSID 隧道终点=DMZ 聚合交换机 → DMZ 内配 DHCP 给访客发地址 → 访客流量只经 DMZ 出 External，不触 Corporate
- **Campus 汇聚**（C4，<<<PAGE 12>>>）：OV2500 中所有站点 AP 加入同一 AP Group → 对该组应用 GTTS SSID 配置 → 全站广播同 SSID 指向同隧道终点（支持漫游）→ 交换机配置同 p9 五步
- **多租户**（C5，<<<PAGE 13>>>）：每客户独立 AP Group（可各有 OmniVista）→ 各组 AP Group 配运营商聚合交换机 IP → 隧道流量走客户-SP 既有链路（SD-WAN/SPB/MPLS）→ SP 侧落隧道施安全策略
- **迁移用例**：无需在边缘新增 VLAN，VLAN 配置只在中心聚合交换机（<<<PAGE 3>>>）

## E（实证案例）
- DMZ 三区架构：Corporate（员工+访客接入）/DMZ（聚合交换机+DHCP+Web/存储服务器）/External（Internet/SD-WAN/运营商网）（<<<PAGE 11>>>）
- 园区架构：1 数据中心 + 多站点，学生/教师各有 SSID 统一隧道，恶意软件无法在网内扩散（<<<PAGE 12>>>）
- SP 与多客户交互轻视图：客户侧 AP Group → SP 聚合交换机（<<<PAGE 13>>>）

## B（反例与坑）
- 多客户共用一个 AP Group → 租户间隔离被破坏（每客户独立 AP Group 是隔离边界，<<<PAGE 13>>>）
- 访客 DHCP/Portal 部署在内网而非 DMZ 同区 → 违背隔离初衷且可能不可达（<<<PAGE 4-5>>>）
- 跨运营商/他公司链路未协商 MTU → +24B 封装导致丢包（<<<PAGE 8>>>）
- 多站点各配各的隧道终点却指望漫游体验一致 → 同 SSID 应指向同一隧道终点（<<<PAGE 12>>>）
- 迁移场景仍沿用"边缘加 VLAN"思路 → GTTS 的中心化 VLAN 增值被浪费（<<<PAGE 3>>>）

来源：Guest Traffic Tunnelling Services Application Note，Scenarios 章（p11-13）+ OmniAccess Stellar Traffic Tunnelling（p3）
