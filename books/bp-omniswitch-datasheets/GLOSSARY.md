# GLOSSARY · OmniSwitch 数据表合集

> 页码为原书 `<<<PAGE N>>>` 标记。按层级分组（SMB 接入/企业千兆接入/多千兆与工业/汇聚/核心），再按许可/堆叠高可用/PoE/安全准入/Fabric/管理运维分组，精选 46 条。

## SMB 接入层
- **OS2260（-10/P10/24/P24/48/P48）**：WebSmart+ GbE，web/CLI 子集管理，PoE 75/195/370W，无堆叠 <<<PAGE 1-3>>>
- **OS2360（-24/P24/48/P48/P24X/P48X/U24X/U48X）**：SMB 可堆叠 GbE，10G VC 8 台/216 口，P48X 740W <<<PAGE 8>>>
- **WebSmart+**：介于非管理与全管理之间的 web 管理定位（2260） <<<PAGE 1>>>

## 企业千兆接入层
- **OS6360（10/24/48/PH/P24X/P48X）**：企业价值接入，VC 8 台/416 口，NDcPP EAL1；P48X 2x95W bt <<<PAGE 16-17>>>
- **OS6370（P12Z12/P24Z8/P48Z16/U24X 等）**：多千兆 PoE 接入（Wi-Fi 7 时代），Z=2.5G 口，2 口 95W，Secure Boot <<<PAGE 24-26>>>
- **OS6570M（12/12D/U28X/U28XD）**：城域 GbE，U28X 20x SFP 全光，1588v2，AC/DC 双电源；D=DC <<<PAGE 64-66>>>
- **OmniVista Smart Tool**：OT 现场 PoE/线缆诊断工具（6370 起） <<<PAGE 24>>>
- **Lightning Configuration**：开箱即用配置向导（6360 起） <<<PAGE 16>>>

## 多千兆与工业加固层
- **OS6560/E（24X4/P48X4/X10/E-P24Z8/E-P48Z16/P24Z24 等）**：校园多千兆，6x10G 上联，20G 堆叠，JTIC+NDcPP，Z 型 95W bt <<<PAGE 54-56>>>
- **OS6465（P6/H-P12/P28）**：DIN 导轨/19" 工业交换机，-40~75°C，60W bt，1588v2，MACsec，6KV 防雷；VC 4 台 <<<PAGE 36-37>>>
- **OS6465T（12/P12）**：宽温城域 L3，-10~60°C，半机架，三重播放 <<<PAGE 47-48>>>
- **OS6575-MP16**：IP67 壁挂工业 GbE，-40~75°C，60W bt，MACsec-256，M23 双电源+告警继电器，VC 4 台 <<<PAGE 73-74>>>
- **OS6865（P16X/U12X/U28X）**：工业 L3 旗舰，-40~74°C，每型 4 口 75W bt，SPB-M VPN，专用 20G VC 口 <<<PAGE 99>>>
- **M23 6-pin / 告警继电器 / 6KV 浪涌保护**：工业电源输入/外接告警/铜口防雷 <<<PAGE 37>>>/<<<PAGE 74>>>

## 汇聚层
- **OS6860（E-24/E-P48/E-P24Z8/N-U28/N-P24Z/N-P48Z/N-P24M/N-P48M）**：接入旗舰，200G 堆叠，95W bt（N 型），PoE 预算最高 3.4kW，SPB/VxLAN/MPLS（N 型） <<<PAGE 82-85>>>
- **OS6860 电源家族（BP/BP-D/BP-PH/BP-PX/N-BPPH/N-BPPX/N-BPXL）**：450W~3390W；3390W 仅 230VAC；E/N 不通用 <<<PAGE 84-85>>>/<<<PAGE 87>>>
- **OS6870（24/48/P24Z/P48Z/U32/V12/P24M/P48M）**：OmniFabric 高端接入，premium 95W/advanced 60W，256bit MACsec 全端口，按 bundle（##）订购 <<<PAGE 110-112>>>
- **OS68-XNI-U4 / VNI-U4 / QNI-U2 / CNI-U1**：6860 premium 上联模块（4x10G/4x25G/2x40G/1x100G） <<<PAGE 86>>>
- **OS6870-LNI-U6 / CNI-U2**：6870 premium 上联模块（6x10/25/50G 需 SW-PERF 才有 50G；2x40/100G） <<<PAGE 114>>>

## 核心 / DC 层
- **OS6900（X24/T24/X48/T48/X48E/V48/C32E）**：固定核心/DC，6.4Tb/s，1RU 最高 128x10G，VC 6 台+ISSU；仅 X48E/C32E 全口 MACsec <<<PAGE 125-127>>>
- **OS6920-D32**：32x400G QSFP-DD，12.8Tb/s，RoCEv2+PFC 无损，Azure Local 认证 <<<PAGE 138-139>>>
- **OS9900（OS9907/OS9912）**：模块化机箱 11RU/17.25RU，288/480 GbE，PoE 10800W/7920W <<<PAGE 145-147>>>
- **CMM/CMM2（Chassis Management Module）**：9900 机箱管理模块（2x40G / 4x100G 上联），控制面虚拟机化，升级高可用 <<<PAGE 146>>>/<<<PAGE 154>>>
- **OS99 线卡家族（GNI/XNI/CNI）**：1G/10G/40/100G 线卡，MPLS ready + MACsec；部分多千兆线卡仅 9907 <<<PAGE 154-157>>>
- **QSFP-DD / QSFP56 / QSFP28 / QSFP+ / SFP28 / SFP+**：400G/200G/100G(4x25G)/40G/25G/10G 光模块封装 <<<PAGE 127>>>/<<<PAGE 139>>>/<<<PAGE 144>>>

## 许可与速度
- **OS6360-SW-PERF**：6360 PH 型 RJ45/SFP 口 1G 升 10G 许可 <<<PAGE 17>>>
- **OS6370-SW-PERF4 / PERF2**：6370 四型 SFP+ 升 10G 许可（PERF4 仅 PH48） <<<PAGE 26>>>/<<<PAGE 30>>>
- **OS6570-SW-PERF4 / SW-PRM28 / SW-PRM12**：6570M 加 4x10G / 6x25G+SPB+AR / 12 型 SPB+AR 许可 <<<PAGE 65>>>/<<<PAGE 68>>>
- **OS6570M-SW-AR**：高级路由许可（OSPFv2/v3、BGP、IS-IS、PIM、VRF） <<<PAGE 65>>>
- **OS6860N-MPLS-1 / MPLS-4**：6860N 按节点（1/4 台）MPLS 许可 <<<PAGE 96>>>
- **OS6870-SW-PERF**：6870 LNI-U6 口 50G 速度许可；SW-PRM1/PRM2 分档 premium 特性 <<<PAGE 111>>>/<<<PAGE 122>>>
- **"Hardware capable, requires future SW development"**：6570M 的 25G/MACsec/1588v2 脚注——硬件就绪软件未交付 <<<PAGE 65>>>
- **OS-SW-MACSEC**：免费站点级 MACsec 许可（每客户一份，6465/6465T/6560/6575/6860/6865/6870/6900/9900 通用） <<<PAGE 45>>>/<<<PAGE 157>>>

## 堆叠与高可用
- **Virtual Chassis（VC）**：多台组单一逻辑实体；2260 无、6465/6465T/6575 4 台、2360/6360/6370/6570M/6560/6860/6865/6870 8 台、6900 6 台、9900 双机箱 <<<PAGE 8>>> 等
- **VFL（Virtual Fabric Link）**：堆叠/上联两用口 <<<PAGE 17>>>
- **ISSU（In-Service Software Upgrade）**：不中断业务升级（6370/6900/9900 等） <<<PAGE 24>>>/<<<PAGE 127>>>
- **Smart continuous switching / 持续交换**：主备切换期间保持转发 <<<PAGE 127>>>
- **ITU-T G.8032 ERPS**：以太网环保护（<50ms 收敛） <<<PAGE 127>>>

## PoE 术语
- **802.3af/at/bt**：15.4/30/60-90W 供电标准 <<<PAGE 16>>>
- **HPoE（75/95W）**：高功率 PoE 口（9900 线卡前 8 口 75W；6860N/6870 premium 95W） <<<PAGE 83>>>/<<<PAGE 147>>>
- **Fast PoE / Perpetual PoE**：上电秒级供电 / 重启期间保持供电 <<<PAGE 24>>>
- **PoE budget**：整机 PoE 预算；370W(2260)→3390W(6860XL)→10800W(9907) <<<PAGE 84>>>/<<<PAGE 147>>>

## 安全与准入
- **MACsec（802.1AE）/ 256bit MACsec**：二层加密；6870/6575 全口 256bit；6900 认 E 后缀 <<<PAGE 54>>>/<<<PAGE 73>>>/<<<PAGE 127>>>
- **Secure Boot**：仅运行可信固件（6370/6570M/6870/6920） <<<PAGE 25>>>/<<<PAGE 138>>>
- **NDcPP (EAL1)**：网络设备协作保护轮廓认证（6360/6560/6865/6860/6900/9900 已认证；6370 未来版本） <<<PAGE 16>>>/<<<PAGE 25>>>
- **JTIC**：美国联合情报界认证（6560/6865/6860/6900/9900） <<<PAGE 55>>>/<<<PAGE 103>>>
- **Access Guardian / UNP / LPS / CoA**：认证与用户档案体系 <<<PAGE 2>>>/<<<PAGE 16>>>
- **IEEE 1588v2 PTP**：精密时间协议（透明时钟；6570M 部分能力待软件） <<<PAGE 36>>>/<<<PAGE 65>>>

## Fabric / 虚拟化
- **SPB-M / SPBM（802.1aq）**：最短路径桥接 fabric（6865/6900/9900/6860/6870） <<<PAGE 99>>>
- **VxLAN / VTEP / BGP-EVPN**：overlay 网络虚拟化及隧道端点（6860N/6900/6870） <<<PAGE 83>>>/<<<PAGE 126>>>
- **OmniFabric**：6870 的 SPB+VxLAN-EVPN+MPLS 统一服务管理框架 <<<PAGE 110>>>
- **RoCEv2 / PFC**：RDMA 融合以太网/优先级流控，无损网络（6920；6900 亦支持 RoCEv2） <<<PAGE 126>>>/<<<PAGE 138>>>
- **Auto-Fabric / Intelligent Fabric**：标准协议自动发现与零配置开局 <<<PAGE 99>>>/<<<PAGE 145>>>

## 管理与运维
- **OmniVista Cirrus / 2500**：云网管/本地网管（2260 起全线支持） <<<PAGE 2>>>
- **OmniVista Network Advisor**：AI 驱动遥测与优化（6870 配套） <<<PAGE 111>>>
- **AirGroup**：Bonjour/DLNA 服务跨网段分发 <<<PAGE 16>>>/<<<PAGE 83>>>
- **EMP**：带外以太管理口 <<<PAGE 84>>>

---
合计：46 条（按 15 系列技能分组对齐）。
