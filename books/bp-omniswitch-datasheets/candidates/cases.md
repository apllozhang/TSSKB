# cases — bp-omniswitch-datasheets（交换机选型决策案例）

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
