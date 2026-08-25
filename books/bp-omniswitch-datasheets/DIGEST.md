# DIGEST — ALE OmniSwitch 数据表合集 精华

本书是 OmniSwitch 全产品线数据表合集（15 份文档 158 页），覆盖 SMB 接入（2260/2360）、企业接入（6360/6370/6560/6570M/6860/6870）、工业加固（6465/6465T/6575/6865）、核心与 DC（6900/6920/9900）四大阵营。定位"售前选型速查"：哪一层选哪个系列、PoE/上联/堆叠/许可的硬边界。

## 一、知识地图（四技能单元）

1. **接入层选型**（bp-sw-access-selection）：2260-6575 九系列矩阵、PoE 阶梯、堆叠能力地图、加固温度边界（p1-81）。
2. **汇聚与核心**（bp-sw-aggregation-core）：6860/6865/6870/6900/6920/9900、PoE 预算天花板、ISSU/CMM、MACsec E 后缀（p82-158）。
3. **许可制特性**（bp-sw-license-features）：SW-PERF/PRM/AR 许可家族、"hardware capable" 未交付陷阱（p17/p26/p65/p111）。
4. **Fabric 定位**（bp-sw-fabric-positioning）：6870 三 fabric 合一、SPB-M/VxLAN-EVPN/MPLS/RoCEv2 演进线（p83/p99/p110/p138）。

## 二、四单元要点串讲

### 1. 接入层：层级×场景×PoE 三问
价值线 2260（WebSmart+ 无堆叠）→2360（10G VC 8 台）→6360（416 口 VC，2x95W）→6560（6x10G+20G 堆叠+全口 MACsec）；Wi-Fi 7 供电线 6370-Z（多口 2.5G/60W+2x95W+Secure Boot）；城域线 6570M-U28X 全光；工业线 6465（-40~75°C）/6465T/6575（壁挂）。PoE 预算阶梯 370W→760W→3390W→10800W。

### 2. 汇聚核心：固定 vs 模块化 vs 400G
6860 接入旗舰（95W+200G 堆叠+3.4kW 天花板）；6870 OmniFabric 高端（premium/advanced 分档、256bit MACsec）；6900 固定核心（6.4Tb/s、VC 6 台+ISSU）；6920-D32 400G AI/HPC（RoCEv2+PFC 无损）；9900 模块化（288 GbE+10800W PoE、CMM 虚拟机化升级不掉线）。加密纪律：6900 认 X48E/C32E。

### 3. 许可经济学
速度许可（6360-SW-PERF / 6370 SW-PERF4/PERF2 / 6570M SW-PERF4+SW-PRM28 / 6870 50G）与路由许可（6570M-SW-AR）支持分期建设（C9）。两类脚注要分清："License purchase required"（花钱即得）vs "Hardware capable, requires future SW development"（6570M 的 25G/MACsec/1588v2 未交付，投标应答须核实）。

### 4. Fabric 演进线
L2+→基础 L3→SPB-M（6865/6900/9900/6860）→三 fabric 合一 OmniFabric（6870："The first solution to support SPBM, VxLAN-EVPN, and MPLS within the AOS unified service manager framework"）→RoCEv2+PFC 无损（6920）。SPB 园区接 VxLAN DC/MPLS WAN 不必网关转换。

## 三、本书在知识库中的位置

与 hw-6560（6560 硬件手册）、hw-6860/6865/6870/6900v2/9900（各系列手册）、os-lan-*（配置课程）互补：本书管"全家族横向选型"，系列书管纵深。与 Stellar AP 书联动：AP 侧 95W bt 需求 ↔ 6370-Z/6860N/6870 premium/9900 HPoE 口。跨书易混点：6560 的 E=enhanced 多千兆型，6900 的 E=全口 MACsec 版，同一后缀语义不同。

## 来源
bp-omniswitch-datasheets（15 份文档 158 页）。verified.md：cases C1-C12；counter-examples X1-X22（无 X6/X12）；frameworks F1-F6；principles P1-P26；glossary 约 70 条。
