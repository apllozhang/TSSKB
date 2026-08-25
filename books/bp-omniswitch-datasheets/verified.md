# Verified 候选（V1 原文真实性核对 + V2/V3 抽查）

## cases

- **C1 小微办公 50 信息点、预算极紧：OS2260 而非 OS2360**
  场景：单层办公、无堆叠需求、外包运维只会 web 界面。依据 <<<PAGE 1>>>："The switches are a lower price alternative compared to managed switches for wired connectivity... using a simplified web management interface"。多楼层/需统一管理/10G 上联时升 2360（p8 "10 GigE virtual chassis up to 8 units"）。
- **C2 Wi-Fi 7 高密楼层接入：OS6370-P48Z16 vs OS6360-P48X**
  同为 48 口带 2x95W 多千兆。6370-Z 型每台 16 口 2.5G + 2x95W + 60W 多千兆（p26），且 "Secure by Default"/Secure Boot（p25）与 Smart Tool（p24）配套 OT 装维；6360-P48X 只有 2 口 1G/2.5G。Wi-Fi 7 AP 全上 2.5G 的楼层选 6370-Z，过渡期少量多千兆选 6360。
- **C3 核心层选择：固定 6900 vs 模块化 9900**
  中型园区/DC ToR 用 6900：1RU 6.4Tb/s、128x10G（p125）。大型园区要 GbE 密度 + PoE 核心用 9900：OS9907 288 GbE + 10800W PoE、线卡混插（p145/p147）；后续按线卡扩容，"modular design provides investment protection allowing for scaling out with future inline upgrades"。
- **C4 AI/存储无损网络：OS6920-D32**
  场景：GPU 集群、RoCEv2 存储。依据 <<<PAGE 138>>>："With support for RoCEv2 and PFC, it enables a fully lossless fabric"；32x400G 可拆分灵活配 spine/super-spine/border-leaf；Azure Local 混云认证是差异化。
- **C5 需要加密的校园/DC 上行：认准 E 后缀与 256bit MACsec**
  6900 系列只有 X48E/C32E 全口 MACsec（p127）；接入层 6560 全系、6860/6870 全系支持；6870 升级到 256bit 且含用户口（p111 "All ports support 256-bit MACsec"）。
- **C6 交通/轨道沿线室外机柜：OS6465（DIN 导轨）vs OS6575-MP16（壁挂）vs OS6865（L3/SPB）**
  依据 <<<PAGE 36>>>（6465 "Intelligent Transportation, Railway"）、<<<PAGE 73>>>（6575 壁挂 + M23 双电源输入 + 告警继电器）、<<<PAGE 99>>>（6865 "-40°C to +74°C... SPB-M based VPNs"）。需要 75W 大功率 PoE + 10G + SPB VPN 组网选 6865；轨旁小点位选 6575；机柜内多口选 6465。
- **P → C7 运营商/城域光纤汇聚：OS6570M-U28X**
  依据 <<<PAGE 64>>>："Service provider managed services application: Customer Premises Equipment (CPE), Fibre aggregations"；20x100FX/1G SFP 全光 + 4 combo + 25G 许可上联 + 1588v2 时钟（p65）。站点无 AC 时选 -12D/U28D 直流版（p66）。
- **C8 SPB 老网向多 fabric 演进：OS6870 一步到位**
  依据 <<<PAGE 110>>>："The first solution to support SPBM, VxLAN-EVPN, and MPLS within the AOS unified service manager framework"。既有 SPB 园区要接 VxLAN-EVPN DC 或 MPLS WAN 时不必网关转换；配合 Network Advisor AI 遥测（p111）。
- **C9 分期建设省钱：PERF 许可路线**
  场景：预算只够先建 1G，两年后升 10G/25G。依据 <<<PAGE 26>>>（6370 SW-PERF4/PERF2 许可把 SFP+ 从 1G 升 10G）、<<<PAGE 17>>>（6360 PH 型许可升 10G）、<<<PAGE 65>>>（6570M SW-PERF4/SW-PRM28 升 10G/25G、SW-AR 加 BGP/IS-IS）、<<<PAGE 111>>>（6870 50G 许可）。买硬件不买速度，后期按需激活。
- **C10 核心交换机升级不中断：虚拟机箱 + ISSU**
  依据 <<<PAGE 127>>>（6900 "Virtual chassis 1+N redundant supervisor manager / Virtual chassis In-Service Software Upgrade (ISSU)"）、<<<PAGE 146>>>（9900 CMM 虚拟机化）、<<<PAGE 24>>>（6370 ISSU）。医院/生产网要求业务连续时把 ISSU 写进技术条款。
- **C11 AP 供电预算规划：95W 口不是每口都 95W**
  6860N-P24Z：12 口 60W + 12 口 95W（p84）；6370-P48Z16：32x30W + 14x60W + 2x95W（p26）；9900 PoE 线卡仅前 8 口 75W（p147 "Up to 75 W of PoE (HPoE) per port on first eight ports"）。高功率设备（AP1570、PTZ）要映射到指定端口段。
- **C12 半径 500m 的分支汇聚：OS6560 堆叠 vs 单台**
  6560 支持 10G/20G 堆叠与远程堆叠（p54 "10 GigE stacking/remote stacking or 20 GigE stacking"），48 口 + 6x10G 上联即可做分支汇聚，避免上 6900。

## counter-examples

## 平台能力边界
- **X1 OS2260 无备份电源、无堆叠** <<<PAGE 3>>>
  "Backup power: N/A"（全型号矩阵）；性能表也无 stacking 字段。
  要点：冗余需求必须上 2360 及以上。
- **X2 OS2260 8 口型号 CPU 仅 800MHz MIPS** <<<PAGE 3>>>
  "800 MHz MIPS-34Kc"（-10/P10），24/48 口为 1GHz 双核。
  要点：8 口型大 ACL/QoS 规模时性能余量小。
- **X3 OS2260 部分功能带星号待实现** <<<PAGE 2>>>
  "including an embedded denial of service (DoS) engine to filter out unwanted traffic attacks*" / "static routing for both IPv4 and IPv6*" / "port mapping*"
  要点：星号特性以当前 AOS 版本确认为准。
- **X4 OS6465-P28 的 27/28 口不支持 1588v2/MACsec** <<<PAGE 37>>>
  "All ports of OS6465-P28 are capable of IEEE 1588v2 & MACSec (except ports 27, 28)."
  要点：时间同步/加密链路别接到 P28 的最后两口。
- **X5 OS6465 虚拟机箱当前限 4 台** <<<PAGE 37>>>
  "Up to 4 switches can be connected in a Virtual Chassis configuration with option to scale up to 8 in future."
  要点：8 台是"未来"能力，方案按 4 台设计。
- **X7 OS6575-MP16 虚拟机箱限 4 台、容量上限小** <<<PAGE 74>>>
  "Maximum number of units in a VC: 4 / Total number of IPv4 routes: 8,000 / Total number of MAC addresses: 32,000"
  要点：大路由表场景不适用。
- **X8 OS6570M 的 25G/MACsec/1588v2 是"硬件就绪、软件待开发"** <<<PAGE 65>>>
  "**Note: Hardware capable, requires future SW development."（对应 MACsec、PTP 条目）/ "*Note: License purchase required."（25G）
  要点：数据表脚注明确部分能力未在当前软件提供，投标应答需核实版本。
- **X9 OS6900 非 E 型号无全口 MACsec** <<<PAGE 127>>>
  仅 "OmniSwitch 6900X48E... All ports support IEEE 802.1AE"；V48/X24/T24/C32（无 E）未标注全口 MACsec。
  要点：加密需求认准 X48E/C32E。
- **X10 OS9900 双机箱 VC 的高档数字属"未来支持"** <<<PAGE 147>>>
  "*Two OS9912 in virtual chassis can support up to 960 10 GigE ports, 960 GigE ports or 400 GigE ports. * Supported in future"
  要点：960 口规格尚未交付。
- **X11 OS9900 PoE 线卡仅前 8 口 75W** <<<PAGE 147>>>
  "Up to 75 W of PoE (High Power-over-Ethernet, HPoE) per port on first eight ports / Capacity to deliver 1800 W of PoE power"
  要点：每线卡 75W 口数量有限，核心直连大功率 AP 时要算口位。
- **X13 OS6920 单一型号（D32）** <<<PAGE 138>>>
  全册仅 OS6920-D32 一型，32x400G 固定配置；无 GbE/PoE 接入能力。
  要点：纯 DC/AI 骨干，接入层必须另配。
- **X14 OS6465T 风扇 45°C 以上才转** <<<PAGE 48>>>
  "* Fans run only if switch is operated at an ambient temperature of +45°C to +60°C."
  要点：静音/防尘环境注意 45~60°C 区间有噪音。
## 订购/许可注意
- **X15 6360/6370/6570M 的 10G/25G 速度默认关闭** <<<PAGE 17>>> / <<<PAGE 26>>> / <<<PAGE 66>>>
  "Default speed is 1G. License upgradable to 10G or 25G."（6570M-U28 SFP28 口）；6360 需 OS6360-SW-PERF、6370 需 SW-PERF2/PERF4。
  要点：硬件到货不等于速度全开，许可行项勿漏。
- **X16 OS6870 50G 上联需许可** <<<PAGE 111>>>
  "Uplink module options of 2 100G ports or 6 25/50G ports. License required for 50G speed"
- **X17 OS6570M 高级路由需 SW-AR 许可** <<<PAGE 65>>>
  "Full OSPFv2 & OSPFv3, BGP, IS-IS, PIM and VRF support with OS6570M-SW-AR Advanced Routing license."
  要点：默认只有 basic L3（静态/部分协议）。
- **X18 OS6370 NDcPP 认证尚未完成** <<<PAGE 25>>>
  "Designed for NDcPP certification* ... * Supported in future release"
  要点：写标书时不能声称"已认证"（6360/6560 已 NDcPP EAL1 认证，可对比）。
- **X19 OS6465 部分 PoE 特性分型号** <<<PAGE 37>>>
  "Fast / Perpetual PoE* support ... * select models"
  要点：Fast/Perpetual PoE 并非全型号默认，下单前核对。
- **X20 OS6860 电源分档命名复杂（BP/BP-D/BPPH/BPPX/BPXL）** <<<PAGE 84>>>
  "Supported power supplies: OS6860-BP, OS6860-BP-D... OS6860-BP-PH / OS6860-BP-PX / OS6860N-BPPH / OS6860N-BPPX"
  要点：PoE 预算 450W~3390W 跨度大，电源与机型必须成对选；3390W 档需 230VAC（p85 "3390W @230 VAC"）。
- **X21 OS6870 订购以 bundle 形式提供** <<<PAGE 112>>>
  "The bundle offered: OS6870-24-## / OS6870-PH24Z-##..."（型号带 ## bundle 号）
  要点：6870 按捆绑包下单，需确认包内电源/许可内容。
- **X22 OS6860N-P48M 的 3390W 仅 230V 市电下可达** <<<PAGE 85>>>
  "665W @115 VAC / 1570W @115 VAC / 1570W @230 VAC / 3390W @230 VAC"
  要点：日本/美国等 115V 站点达不到最高 PoE 预算。

## frameworks

- **F1 OmniSwitch 层级×场景定位矩阵**
  ```
             SMB/分支          企业接入                工业加固               核心/DC
  价值型    OS2260(WebSmart)  OS6360                  OS6465T(-10~60°C)    —
            OS2360(可堆叠)    OS6560/E                                      OS6900(固定)
            OS6370(多千兆PoE) OS6570M(城域/SP)        OS6465(-40~75°C)
  高性能    —                 OS6860(95W/全fabric)    OS6575-MP16(壁挂)    OS6920-D32(400G)
                              OS6870(OmniFabric)      OS6865(L3/SPB)       OS9900(模块化)
  ```
  选型第一问：部署层级 + 是否恶劣环境 + PoE 功率需求。定位依据：<<<PAGE 1>>>（2260）/ <<<PAGE 36>>>（6465）/ <<<PAGE 125>>>（6900）。
- **F2 型号命名解码框架**
  ```
  OS<系列号><特性码>：
    P 前缀/嵌入 = PoE（P24/P48）；PH = 高功率 PoE；X = 10G SFP+ 上联
    Z<数字> = 多千兆口数量（Z8/Z16/Z24；6370 的 Z 表 2.5G 口）
    U<数字> = 全光 SFP 用户口（U28/U28X/U32）；D 后缀 = DC 直流电源
    M = Metro/多千兆混合（6570M；6860N-P24M 的 M=多千兆 10G）
    E 后缀（6900X48E/C32E）= 全口 MACsec；6560 的 E = enhanced 多千兆型
    CMM = 9900 机箱管理模块；C32/V48/X48/T48 = 端口形态
  许可家族：SW-PERF（10G 上联）/ SW-PRM（25G）/ SW-AR（高级路由）/ SW-ADV 等
  ```
  依据各型号表：<<<PAGE 17>>> / <<<PAGE 26>>> / <<<PAGE 65>>> / <<<PAGE 84>>> / <<<PAGE 111>>> / <<<PAGE 127>>>。
- **F3 PoE 供电能力阶梯（对齐 Wi-Fi 世代）**
  ```
  30W af/at：2260-P/2360-P/6360-P（入门 AP/话机）
  60W bt：6465 全系/6575/6370 Z 型多口/6860E/6870 advanced（Wi-Fi 6 高端、AP1521 degraded 之外）
  75W：9900 线卡前 8 口/6865 4 口
  95W bt：6360-P48X 2 口/6370-Z 2 口/6560-Z 全部/6860N/6870 premium（AP1501/1511/1570、AP1540 需 bt）
  预算上限：370W(2260)→760W(6360)→1545W(6860N)→3390W(6860XL)→10800W(9907)
  ```
  依据：<<<PAGE 3>>> / <<<PAGE 17>>> / <<<PAGE 26>>> / <<<PAGE 54>>> / <<<PAGE 83>>> / <<<PAGE 84>>> / <<<PAGE 85>>> / <<<PAGE 147>>>。
- **F4 堆叠/虚拟机箱（VC）能力地图**
  ```
  无：2260、6465T、6465(4台)、6575(4台)
  10G VC 8 台：2360(216口)/6360(416口)/6370/6570M
  20G：6560；40G：6860E(QSFP+)
  100G：6860N/6870 advanced；200G：6870 premium/U32
  专用 VC 口：6865-U28X(20G QSFP+)、6920 无 VC
  核心级：6900 VC 6 台；9900 双机箱 VC（960x10G 未来支持）
  ```
  依据各型号 stacking/VFL 描述：<<<PAGE 8>>> / <<<PAGE 16>>> / <<<PAGE 54>>> / <<<PAGE 82>>> / <<<PAGE 99>>> / <<<PAGE 111>>> / <<<PAGE 125>>> / <<<PAGE 147>>>。
- **F5 Fabric 技术演进线**
  ```
  L2+/静态路由（2260/2360）
  → 基础 L3（6360/6465T/6570M 需许可）
  → SPB-M（6865/6900/9900/6860）
  → SPB + VxLAN-EVPN + MPLS 三合一 OmniFabric（6870/6920）
  → RoCEv2+PFC 无损（6920 AI/HPC）
  ```
  依据：<<<PAGE 83>>>（6860 SPB/VxLAN/MPLS）、<<<PAGE 99>>>（6865 SPB-M VPN）、<<<PAGE 110>>>（6870 OmniFabric）、<<<PAGE 138>>>（6920 RoCEv2）。
- **F6 管理与自动化演进**
  ```
  WebView+CLI 子集（2260）→ +OV2500/Cirrus（2360 起）
  → +Lightning Config（6360 起）
  → +Smart Tool 现场 OT 工具（6370）
  → +AI 遥测/Network Advisor 联动（6870）
  ```
  依据：<<<PAGE 1>>> / <<<PAGE 8>>> / <<<PAGE 16>>> / <<<PAGE 24>>> / <<<PAGE 110>>>。

## glossary

- **OS2260（-10/P10/24/P24/48/P48）**：WebSmart+ GbE，web/CLI 子集管理，PoE 75/195/370W <<<PAGE 3>>>
- **OS2360（-24/P24/48/P48/P24X/P48X）**：SMB 可堆叠 GbE，10G VC 8 台/216 口，P48X 740W <<<PAGE 8>>>
- **WebSmart+**：介于非管理与全管理之间的 web 管理定位 <<<PAGE 1>>>
- **WebView 2.0**：内置 web 管理界面 <<<PAGE 2>>>

## 企业接入
- **OS6360（10/P10/24/P24/48/P48/PH24/PH48/P24X/P48X）**：企业价值接入，VC 8 台/416 口 <<<PAGE 16>>>
- **OS6360-SW-PERF**：PH 型 RJ45/SFP 口 1G 升 10G 的许可 <<<PAGE 17>>>
- **OS6370（12/P12/24/P24/48/P48/PH/P24X/P48X/P12Z12/P24Z8/P48Z16/U24X）**：多千兆 PoE 接入，Z=2.5G 口 <<<PAGE 26>>>
- **OS6370-SW-PERF4 / PERF2**：4 口/2 口 SFP+ 升 10G 许可 <<<PAGE 26>>>
- **OS6560/E（24X4/P24X4/48X4/P48X4/X10/E-P24Z8/P24Z24/E-P48Z16）**：校园多千兆，6x10G 上联，20G 堆叠 <<<PAGE 54>>>
- **OS6570M（12/12D/U28X/U28XD）**：城域 GbE，全光 U28X 20x SFP；D=DC 电源 <<<PAGE 64>>> / <<<PAGE 66>>>
- **OS6570M-SW-AR**：高级路由许可（OSPFv2/v3、BGP、IS-IS、PIM、VRF） <<<PAGE 65>>>
- **OS6570-SW-PERF4 / SW-PRM28**：10G/25G 上联许可 <<<PAGE 65>>>
- **OS6860（E-24/E-P24/E-48/E-P48/N-U28/N-P24Z/N-P48Z/E-P24Z8/N-P24M/N-P48M）**：接入旗舰，200G 堆叠，95W bt <<<PAGE 82>>> / <<<PAGE 84>>>
- **OS6860-BP/BP-D/BP-PH/BP-PX/N-BPPH/N-BPPX/N-BPXL**：6860 电源家族（450W~3390W） <<<PAGE 84>>> / <<<PAGE 85>>>
- **OS6870（24/48/P24Z/P48Z/U32/V12/P24M/P48Z premium 等）**：OmniFabric 高端接入，256bit MACsec <<<PAGE 111>>> / <<<PAGE 112>>>
- **OS6870-24-##（bundle）**：6870 以捆绑包号订购 <<<PAGE 112>>>

## 工业加固
- **OS6465（P6/P12/P28）**：DIN 导轨/19" 工业交换机，-40~75°C，60W bt <<<PAGE 36>>> / <<<PAGE 37>>>
- **OS6465H-P12**：6465 的另一订购号系列（p38 表头 Orderable Part #'s） <<<PAGE 38>>>
- **OS6465T（12/P12）**：宽温城域 L3，-10~60°C，半机架 <<<PAGE 47>>>
- **OS6575-MP16**：壁挂工业 GbE，60W bt，MACsec-256，M23 双电源 <<<PAGE 73>>>
- **OS6865（P16X/U12X/U28X）**：工业 L3 旗舰，-40~74°C，75W bt，SPB-M <<<PAGE 99>>>

## 核心/DC
- **OS6900（V48/X48E/X24/T24/C32E/X48/T48）**：固定核心/DC，6.4Tb/s，VC 6 台 <<<PAGE 125>>> / <<<PAGE 127>>>
- **OS6920-D32**：32x400G QSFP-DD，12.8Tb/s，RoCEv2+PFC 无损 <<<PAGE 138>>>
- **OS9900 系列（OS9907/OS9912）**：模块化机箱 11RU/17.25RU，PoE 10800W/7920W <<<PAGE 145>>>
- **CMM（Chassis Management Module）**：9900 机箱管理模块，控制面虚拟机化 <<<PAGE 146>>>
- **QSFP-DD / QSFP28 / QSFP+ / SFP28 / SFP+**：400G/100G(4x25G)/40G/25G/10G 光模块封装 <<<PAGE 127>>> / <<<PAGE 139>>>

## 堆叠与高可用
- **Virtual Chassis（VC）**：多台交换机组为单一逻辑实体；2260 无、2360/6360 8 台、6465/6575 4 台、6900 6 台 <<<PAGE 8>>> 等
- **VFL（Virtual Fabric Link）**：堆叠/上联两用口 <<<PAGE 17>>>
- **ISSU（In-Service Software Upgrade）**：不中断业务升级 <<<PAGE 24>>>
- **Smart continuous switching**：6900 持续交换技术 <<<PAGE 127>>>
- **ITU-T G.8032 ERPS**：以太网环保护 <<<PAGE 127>>>
- **Configuration rollback**：配置回滚 <<<PAGE 9>>>

## PoE 术语
- **802.3af/at/bt**：15.4/30/60-90W 供电标准 <<<PAGE 16>>>
- **HPoE（75/95W）**：高功率 PoE 口 <<<PAGE 83>>>
- **Fast PoE**：上电数秒内供电 <<<PAGE 24>>>
- **Perpetual PoE**：交换机重启期间保持供电 <<<PAGE 24>>>
- **PoE budget**：整机 PoE 预算（W） <<<PAGE 84>>>

## 安全与准入
- **MACsec（802.1AE）/ 256bit MACsec**：二层加密；6870/6575 为 256bit <<<PAGE 54>>> / <<<PAGE 73>>>
- **Secure Boot**：出厂供应链保护，仅运行可信固件 <<<PAGE 25>>>
- **NDcPP (EAL1)**：网络设备协作保护轮廓认证（6360/6560 已认证） <<<PAGE 16>>>
- **JTIC**：美国联合情报界认证（6560） <<<PAGE 55>>>
- **Access Guardian**：802.1x/MAC/captive portal 认证 <<<PAGE 16>>>
- **UNP（User Network Profile）**：用户网络档案 <<<PAGE 2>>>
- **LPS（Learned Port Security）**：学习端口安全 <<<PAGE 2>>>
- **CoA（Change of Authorization）**：动态改授权 <<<PAGE 16>>>
- **DoS engine**：内嵌拒绝服务过滤引擎 <<<PAGE 2>>>

## Fabric/虚拟化
- **SPB-M / SPBM（802.1aq）**：最短路径桥接 fabric <<<PAGE 99>>>
- **VxLAN / VTEP / BGP-EVPN**：网络虚拟化 overlay 及隧道端点 <<<PAGE 83>>> / <<<PAGE 126>>>
- **OmniFabric**：6870 的 SPB+VxLAN-EVPN+MPLS 统一框架 <<<PAGE 110>>>
- **MPLS / l2vpn**：多协议标签交换虚拟专网 <<<PAGE 83>>>
- **VRF**：虚拟路由转发 <<<PAGE 83>>>
- **Auto-Fabric / Intelligent Fabric**：标准协议自动发现与零配置开局 <<<PAGE 99>>> / <<<PAGE 145>>>
- **RoCEv2 / PFC**：RDMA 融合以太网/基于优先级流控，无损网络 <<<PAGE 126>>> / <<<PAGE 138>>>

## 管理与运维
- **OmniVista Cirrus / 2500**：云网管 / 本地网管 <<<PAGE 2>>>
- **OmniSwitch Lightning Configuration**：开箱即用配置向导 <<<PAGE 16>>>
- **OmniVista Smart Tool**：OT 现场 PoE/线缆诊断工具 <<<PAGE 24>>>
- **AirGroup**：Bonjour/DLNA 服务跨网段分发 <<<PAGE 16>>> / <<<PAGE 83>>>
- **RESTful API / OpenFlow / OpenStack**：SDN 可编程接口 <<<PAGE 83>>>
- **EMP**：带外以太管理口 <<<PAGE 84>>>
- **IEEE 1588v2 PTP**：精密时间协议（透明时钟） <<<PAGE 36>>>
- **M23 6-pin / 端子块电源**：6575/6465 工业双电源输入 <<<PAGE 74>>> / <<<PAGE 37>>>
- **告警继电器（Alarm relay）**：外接告警系统触点 <<<PAGE 37>>>
- **6KV 浪涌保护**：铜口防雷等级（6465/6865） <<<PAGE 37>>> / <<<PAGE 100>>>

## principles

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
