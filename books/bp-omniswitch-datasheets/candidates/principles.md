# principles — bp-omniswitch-datasheets（OmniSwitch 选型速查）

## SMB / 价值接入层

- **P1 OS2260：WebSmart+ 定位（低于全管理）** <<<PAGE 1>>>
  "The switches are a lower price alternative compared to managed switches for wired connectivity, while maintaining performance, Quality of Service (QoS), and scalability, using a simplified web management interface."
  要点：AOS 软件 + WebView 2.0 + CLI 子集；无堆叠；8/24/48 口，P10/P24/P48 PoE 预算 75/195/370W。

- **P2 OS2360：SMB 可堆叠（虚拟机箱 8 台）** <<<PAGE 8>>>
  "10 GigE virtual chassis bandwidth up to 8 units (stacking) or 216 ports"
  要点：X 型号带 SFP+ 10G 上联；P48X PoE 预算 740W；与 2260 拉开堆叠/上联差距。

- **P3 2260/2360 共同卖点：Perpetual/Fast PoE+** <<<PAGE 1>>> / <<<PAGE 8>>>
  "Perpetual and fast PoE+ support across all PoE models"
  要点：交换机重启期间不断电（Perpetual）、上电秒级供电（Fast），IP 话机/摄像头场景关键。

## 企业接入层

- **P4 OS6360：企业价值接入，堆叠 8 台/416 口** <<<PAGE 16>>>
  "10 GigE virtual chassis bandwidth up to 8 units (stacking) or 416 ports"
  要点：NDcPP (EAL1) 认证、Lightning Config、AirGroup；PH 型 RJ45/SFP 口可许可升 10G（p17 "license upgradable to 10G speeds with the OS6360-SW-PERF license"）。

- **P5 OS6360-P48X：接入层的 bt 95W 多千兆口** <<<PAGE 17>>>
  "OS6360-P48X/PH48 Multi-Gigabit PoE ports comply with IEEE 802.3bt (95 W) and IEEE 2.5GE 802.3bz standards"
  要点：46x1G + 2x1G/2.5G，760W 预算，Wi-Fi 6/7 AP 供电的低成本入口。

- **P6 OS6370：为 Wi-Fi 7 与重 PoE IoT 设计** <<<PAGE 24>>>
  "Engineered to support the most demanding IoT deployments... 12, 24 and 48-port Multi-Gigabit PoE models featuring 12, 8 and 16 ports of 2.5G; delivering 95W on two ports and 60W PoE on the remaining Multi-Gigabit ports"
  要点：Z 型多千兆（P12Z12/P24Z8/P48Z16）；Zero Trust "Secure by Default" + Secure Boot（p25）。

- **P7 OS6370 许可经济学** <<<PAGE 26>>>
  "OS6370-SW-PERF4 software license enables 4 SFP+ Ports to upgrade from 1G speed... OS6370-SW-PERF2... (applicable to OS6370-12, OS6370-P12, OS6370-PH24, OS6370-PH48, OS6370-P48X, and OS6370-48X models)"
  要点：10G 上联按需买许可；配合 p25 "advanced routing... activated through software license purchase"，先买硬件后升级。

- **P8 OS6560/E：校园多千兆接入 + 6x10G 上联** <<<PAGE 54>>>
  "24-port and 48-port, PoE and non-PoE with fixed small form factor pluggable (SFP+) with support for up to 6 x 10G interfaces / Support for 10 GigE stacking/remote stacking or 20 GigE stacking"
  要点：JTIC 认证 + NDcPP（p55）；MACsec 全端口（1G/2.5G 用户 + 10G 上联）；Z 型号 95W bt（p56 "All OmniSwitch Multi-Gigabit PoE ports comply with IEEE 802.3bt (95 W)"）。

- **P9 OS6570M：城域以太/SP 边缘（全光 + 备份电源）** <<<PAGE 64>>>
  "industry-leading edge and aggregation solution for both enterprise and service provider networks... Service provider managed services application: Customer Premises Equipment (CPE), Fibre aggregations"
  要点：U28X 20x SFP 全光；AC/DC 双电源；Metro Ethernet 服务特性内置；1588v2 Transparent Clock（U28X）。

- **P10 OS6570M 上联许可两级** <<<PAGE 65>>>
  "Supports additional 4x10 GigE uplink/VFL ports with the OS6570-SW-PERF4 license or 6x25 GigE with OS6570-SW-PRM28" + "Full OSPFv2 & OSPFv3, BGP, IS-IS, PIM and VRF support with OS6570M-SW-AR Advanced Routing license."
  要点：25G 与 BGP/IS-IS 都要走许可。

- **P11 OS6860：接入旗舰（95W + 200G 堆叠 + 全 fabric）** <<<PAGE 82>>>
  "With high-speed flexible uplinks, 200G stacking, industry leading 95W PoE, and high density 10G multi-gigabit ports ready for Wi-Fi 6, these platforms are the right choice for the next generation of enterprise switching networks... The first in the industry to offer application monitoring and visibility for network analytics"
  要点：E 增强（60/75W）/ N 高级（95W，SFP28 25G 上联）/ premium 模块化上联（4x10G/4x25G/2x40G/1x100G，p84）；SPB-M + VxLAN VTEP + MPLS（N 型，p83）。

- **P12 OS6860 PoE 预算天花板 3.4kW** <<<PAGE 83>>>
  "the best-in-class PoE budget of up to 3.4 kW"
  要点：双电源叠加（OS6860N-BPXL 双 PS 时 3390W@230VAC，p85）。

- **P13 OS6870：OmniFabric 三 fabric 合一** <<<PAGE 110>>>
  "The first solution to support SPBM, VxLAN-EVPN, and MPLS within the Alcatel-Lucent OS (AOS) unified service manager framework."
  要点：256bit MACsec 全端口、Secure Boot、AI 遥测引擎配合 Network Advisor（p110-111 "AI-Powered Optimization"）。

- **P14 OS6870 premium/advanced 分档** <<<PAGE 111>>>
  "Premium models: 24 10GbE Multi-gigabit ports or 48 5GbE Multi-gigabit, up to 95W 802.3bt PoE with 600W, 1200W and 2000W redundant PSU options... uplink module options of 2 100G ports or 6 25/50G ports. License required for 50G speed / Advanced models: 24/48 2.5GbE... 60W... fixed 2 x 100G VFL stacking ports"
  要点：200G VFL 堆叠；50G 也要许可；U32 型 8x25G SFP28 + 200G 堆叠（p111）。

## 工业加固层

- **P15 OS6465：工业以太（-40~75°C，DIN 导轨）** <<<PAGE 36>>>
  "ruggedized, fully manageable and fan-less Gigabit Ethernet switches... ideal for a wide variety of Industrial applications such as Intelligent Transportation, Railway, smart cities and Utilities"
  要点：P6/P12（DIN 导轨）与 P28（19"）；全型号 60W bt PoE、1588v2 PTP、MACsec、6KV 铜口防雷（p37 "surge protection of 6KV on all copper ports"）。

- **P16 OS6465 虚拟机箱 4 台起步** <<<PAGE 37>>>
  "Up to 4 switches can be connected in a Virtual Chassis configuration with option to scale up to 8 in future."
  要点：P28 用 10G SFP+ 堆叠；端口级能力差异（p38："All ports of OS6465-P28 are capable of IEEE 1588v2 & MACSec (except ports 27, 28)"）。

- **P17 OS6465T：宽温城域/三重播放（-10~60°C）** <<<PAGE 47>>>
  "extended temperature, value, Layer 3 Gigabit Ethernet switches... ideal for residential/metro Ethernet triple play applications"
  要点：半机架 1RU，45°C 以下风扇停转（p48）；P12 型 115W PoE。

- **P18 OS6575-MP16：壁挂工业小盒子** <<<PAGE 73>>>
  "ruggedized, fully manageable and fan-less... wall mountable switch"
  要点：-40~75°C、60W bt、MACsec-256、M23 6 针双电源输入、告警继电器（p74）；虚拟机箱最多 4 台（p74 规格表 "Maximum number of units in a VC: 4"）。

- **P19 OS6865：工业 L3 旗舰（75W + SPB-M）** <<<PAGE 99>>>
  "ruggedized, advanced Layer 3, scalable Ethernet switches... offering SPB-M based VPNs... 75W IEEE 802.3bt PoE... IEEE 1588v2 PTP"
  要点：-40~74°C；每型 4 口 75W PoE；U28X 带专用 20G VC 口；auto-fabric 零配置开局。

## 核心 / 数据中心层

- **P20 OS6900：固定配置核心/DC（6.4Tb/s）** <<<PAGE 125>>>
  "compact, high-density 10, 25, 40 and 100 Gigabit Ethernet (GigE) platforms... Wire-rate non-blocking up to 6.4 Tb/s"
  要点：1RU 最高 128x10G/80x25G/32x100G；VC 最多 6 台；V48 型 48x1/10/25G SFP28 + 8 QSFP28（p127）。

- **P21 OS6900 MACsec 分档** <<<PAGE 127>>>
  "OmniSwitch 6900X48E has 40 1/10G SFP+ ports... All ports support IEEE 802.1AE MAC Security standard with AES 128-bit and 256-bit encryption functionality."
  要点：X48E（及 C32E 后缀 E）为全口 MACsec 版本，选型时看 "E" 后缀。

- **P22 OS6920-D32：400G AI/HPC 交换机** <<<PAGE 138>>>
  "compact, high-density 400 Gigabit Ethernet switch... It provides 32 × 400G ports... Wire-rate non-blocking up to 12.8 Tb/s... With support for RoCEv2 and PFC, it enables a fully lossless fabric"
  要点：QSFP-DD 可拆分 128x10/25G、128x50/100G、64x200G（p139）；微软 Azure Local 官方认证；SPB L2 VPN。

- **P23 OS9900：模块化机箱旗舰** <<<PAGE 145>>>
  "high density, multi Terabit modular platform... OS9907 scaling up to 10800 W of inline PoE power and OS9912 scales up to 7920 W... highest 1 GigE/10GigE port density in its class"
  要点：OS9907 11RU（288 GbE/240 SFP+/108 QSFP28）、OS9912 17.25RU（480 GbE/480 SFP+/208 QSFP28）（p147）；双机箱 VC 可到 960x10G。

- **P24 OS9900 软件虚拟化控制面** <<<PAGE 146>>>
  "the Chassis Management Module (CMM) control plane and data plane management are virtualized and execute as virtual machines, enabling high availability during upgrades"
  要点：CMM 虚拟机化，升级不掉线；PoE 线卡 8 口 75W + 40 口 30W（p147）。

## 共性能力

- **P25 全线 Auto-Fabric/零配置** <<<PAGE 99>>>（6865）/ <<<PAGE 145>>>（9900）
  "out-of-the-box plug-and-play, Zero-touch provisioning and network automation with automatic protocol and topology discovery"
  要点：基于 802.1aq/802.1ak/LACP 标准自动发现，跨全线一致。

- **P26 管理三件套：Cirrus 云 / OV2500 / Lightning Config** <<<PAGE 2>>>（2260 起全线）
  "Cloud enabled with Alcatel-Lucent OmniVista® Cirrus... Support by Alcatel-Lucent OmniVista 2500"（6360 起加 Lightning Configuration，p16；6370 加 Smart Tool，p24）
