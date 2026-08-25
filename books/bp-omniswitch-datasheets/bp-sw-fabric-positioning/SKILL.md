---
name: OmniSwitch Fabric 定位（6870 三 fabric 合一 / SPB / VxLAN-EVPN / 9900/6920）
description: 售前做园区-DC-WAN 打通方案时定位 fabric 技术：6870 OmniFabric（SPBM+VxLAN-EVPN+MPLS 统一服务管理框架）、6865/6900/9900 SPB-M、6920 RoCEv2 无损，以及多 fabric 演进免网关的选型论证时使用。
source_book: bp-omniswitch-datasheets（OS6860 p83 / OS6865 p99 / OS6870 p110-111 / OS6900 p126 / OS6920 p138 / OS9900 p145）
---

## R（触发场景）
- 既有 SPB 园区要接 VxLAN-EVPN 数据中心或 MPLS WAN
- 园区 fabric 新建：SPB-M vs VxLAN-EVPN vs 三合一的取舍
- AI/存储无损 fabric（RoCEv2+PFC）方案定位
- 大型园区零配置开局（auto-fabric）论证

## I（核心理念）
Fabric 技术演进线（F5，<<<PAGE 83>>>/<<<PAGE 99>>>/<<<PAGE 110>>>/<<<PAGE 138>>>）：L2+/静态路由（2260/2360）→ 基础 L3（6360/6570M）→ SPB-M（6865/6900/9900/6860）→ 三 fabric 合一 OmniFabric（6870/6920，"The first solution to support SPBM, VxLAN-EVPN, and MPLS within the AOS unified service manager framework"）→ RoCEv2+PFC 无损（6920 AI/HPC）。核心卖点：跨 fabric 场景（SPB 园区 ↔ VxLAN DC ↔ MPLS WAN）不必网关转换，一台 6870 一步到位（C8）。

## A1（行动框架）
1. 画 fabric 版图：园区（SPB）↔ DC（VxLAN-EVPN）↔ WAN（MPLS），识别跨界点
2. 单一 fabric 场景：纯 SPB 园区/工业 VPN → 6865/6900/9900；纯 AI/存储无损 → 6920-D32
3. 跨 fabric 场景：跨界点选 6870（OmniFabric 统一服务管理框架 + AI 遥测联动 Network Advisor）
4. 配套安全：6870 全端口 256bit MACsec + Secure Boot
5. 开局方式：全线 auto-fabric/零配置（802.1aq/802.1ak/LACP 标准自动发现，P25）

## A2（选型速查表）
| fabric 能力 | 代表系列 | 关键规格 | 页码 |
|---|---|---|---|
| SPB-M VPN（工业 L3） | OS6865 | SPB-M based VPNs，auto-fabric 零配置，专用 20G VC 口 | <<<PAGE 99>>> |
| SPB + VxLAN VTEP + MPLS | OS6860 N 型 | 全 fabric 接入旗舰 + 应用可视化 | <<<PAGE 83>>> |
| OmniFabric 三合一 | OS6870 | SPBM+VxLAN-EVPN+MPLS 统一服务管理框架；256bit MACsec；AI 遥测 | <<<PAGE 110-111>>> |
| SPB L2 VPN + 无损 | OS6920-D32 | RoCEv2+PFC 全无损；SPB L2 VPN | <<<PAGE 138>>> |
| 核心 SPB/智能 fabric | OS6900 / OS9900 | SPB；9900 Intelligent Fabric 自动发现 | <<<PAGE 126>>>/<<<PAGE 145>>> |
| VxLAN/BGP-EVPN | 6900/6860/6870 | VTEP 支持 | <<<PAGE 126>>>/<<<PAGE 83>>>/<<<PAGE 110>>> |

## E（选型决策案例）
- SPB 老园区向多 fabric 演进：6870 一步到位（SPBM/VxLAN-EVPN/MPLS 三协议同框架），接 VxLAN DC 或 MPLS WAN 不必网关转换，配合 Network Advisor AI 遥测（C8，<<<PAGE 110>>>/<<<PAGE 111>>>）
- AI/存储无损网络：6920-D32 RoCEv2+PFC 全无损 fabric，32x400G 拆分配 spine/super-spine/border-leaf（C4，<<<PAGE 138>>>）
- 交通/轨道要 75W PoE+10G+SPB VPN：6865 工业加固 + SPB-M（C6，<<<PAGE 99>>>）

## B（反例与坑）
- 三 fabric 合一是 6870（及 6920 的无损扩展）专属卖点；6360/6570M 只有基础 L3（部分还需许可），勿在低端方案承诺 fabric 能力（F5，<<<PAGE 17>>>/<<<PAGE 65>>>）
- 6870 的 50G 上联需许可，fabric 高速互联预算勿漏（X16，<<<PAGE 111>>>）
- 6920 无 VC 堆叠、无 PoE/接入能力，纯 DC/AI 骨干定位（X13，<<<PAGE 138>>>）
- 9900 双机箱 VC 960x10G 属未来支持，fabric 容量规划按当前交付能力（X10，<<<PAGE 147>>>）
- SPB 图形化管理需新 OmniVista 平台配合（跨书引用：NMS 书 P27）

来源：bp-omniswitch-datasheets verified.md（C4/C6/C8/X10/X13/X16/F5/P11/P13/P19/P22/P25）
