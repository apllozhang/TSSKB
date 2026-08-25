# DIGEST — ALE OmniSwitch 数据表合集 精华

本书是 OmniSwitch 全产品线数据表合集（15 份文档 158 页），覆盖 SMB 接入（2260/2360）、企业接入（6360/6370/6560/6570M/6860/6870）、工业加固（6465/6465T/6575/6865）、核心与 DC（6900/6920/9900）四大阵营。定位"售前选型速查"：哪一层选哪个系列、PoE/上联/堆叠/许可的硬边界。

## 一、知识地图（15 技能单元，每系列一个技能）

| 系列 | 型号档 | 层级定位 | 页码 |
|---|---|---|---|
| bp-os2260-datasheet | OS2260（8/24/48 口） | SMB WebSmart+ 价值接入，无堆叠 | p1-7 |
| bp-os2360-datasheet | OS2360（24/48 口 + X 型） | SMB 可堆叠，10G VC 8 台/216 口 | p8-14 |
| bp-os6360-datasheet | OS6360（10/24/48/PH/X） | 企业价值接入，VC 8 台/416 口，P48X 2x95W | p15-23 |
| bp-os6370-datasheet | OS6370（Z 型多千兆） | Wi-Fi 7/IoT 多千兆 PoE 接入，2.5G+2x95W | p24-35 |
| bp-os6465-datasheet | OS6465（P6/P12/P28） | 工业 DIN/19" 加固，-40~75°C，60W bt | p36-46 |
| bp-os6465t-datasheet | OS6465T（12/P12） | 宽温城域 L3/三重播放，-10~60°C | p47-53 |
| bp-os6560e-datasheet | OS6560/E（千兆+Z 型） | 校园多千兆，6x10G 上联 + 20G 堆叠 + 全口 MACsec | p54-63 |
| bp-os6570m-datasheet | OS6570M（12/U28X） | 城域/SP 边缘，U28 全光 + 25G 许可升速 | p64-72 |
| bp-os6575-datasheet | OS6575-MP16 | IP67 壁挂工业小盒，60W bt + MACsec-256 | p73-81 |
| bp-os6860-datasheet | OS6860（E/N/premium） | 接入旗舰，95W + 200G 堆叠 + 3.4kW + 全 fabric | p82-98 |
| bp-os6865-datasheet | OS6865（P16X/U12X/U28X） | 工业 L3 旗舰，75W + SPB-M VPN + -40~74°C | p99-109 |
| bp-os6870-datasheet | OS6870（advanced/premium） | OmniFabric 三 fabric 合一，全口 256bit MACsec | p110-124 |
| bp-os6900-datasheet | OS6900（X/T/V/C 七型号） | 固定核心/DC，6.4Tb/s，VC 6 台 + ISSU | p125-137 |
| bp-os6920-datasheet | OS6920-D32 | 400G AI/HPC 骨干，12.8Tb/s，RoCEv2 无损 | p138-144 |
| bp-os9900-datasheet | OS9900（9907/9912） | 模块化机箱旗舰，480 GbE + 10800W PoE | p145-158 |

## 二、层级分组串讲

### 接入层 SMB（2260/2360）
价值线起点 2260（WebSmart+ web/CLI 子集管理、无堆叠、370W PoE）→ 2360（加 10G VC 8 台、X 型 2x10G 上联、P48X 740W、全光 U24X/U48X）。要点：两系均无备份电源、仅 af/at；星号"未来软件"特性在 2260 要按版本确认。

### 接入层千兆企业（6360/6370/6570M）
6360 是企业价值接入（NDcPP EAL1 + Lightning Config；P48X/PH48 2 口 2.5G bt 95W、PH 型 SW-PERF 许可升 10G）；6370 为 Wi-Fi 7 时代多千兆档（Z 型多口 2.5G + 2x95W + Secure Boot + Smart Tool；SW-PERF4/PERF2 与 SW-AR 许可制；NDcPP 未完成认证）；6570M 是城域/SP 边缘（U28 全光 20x SFP + 1588v2 + Metro 特性；25G/MACsec 等"hardware capable 待软件"）。三系共同坑：10G/25G 速度默认关闭、许可行项勿漏。

### 接入层多千兆与工业（6560E/6465/6465T/6575）
6560/E 校园多千兆（最多 6x10G 上联 + 20G QSFP 堆叠 + JTIC/NDcPP + MACsec；Z 型全口 95W bt）；工业阵营按防护与角色分：6465（-40~75°C DIN/19"、60W bt、1588v2/MACsec、VC 4 台）、6465T（宽温城域三重播放、115W）、6575（IP67 壁挂、内置完整动态路由 + SPB、Bypass 口）、6865（工业 L3 旗舰，75W + SPB-M VPN + VC 8 台 + MIL-STD）。选型口诀：机柜多口 6465、轨旁小盒 6575、要 L3/SPB VPN 上 6865。

### 汇聚（6860/6865）
6860 三档（E 增强 60/75W → N 高级 95W/25G 上联 → premium 模块化上联 1x100G），200G/100G 堆叠、VC 8 台、3.4kW PoE 天花板（需 230VAC + BPXL）、SPB + VxLAN VTEP（N 型 + MPLS 按节点许可）；6865 把 fabric 能力带进工业环境。

### 核心（6870/6900/6920/9900）
6870 OmniFabric 一步到位（SPB+VxLAN-EVPN+MPLS 统一框架，全口 256bit MACsec，AI 遥测）；6900 固定核心（6.4Tb/s、1RU 128x10G/80x25G/32x100G，VC 6 台 + ISSU，加密认 X48E/C32E）；6920-D32 专攻 400G AI/HPC（RoCEv2+PFC 无损、Azure Local 认证、单型号）；9900 模块化机箱（9907/9912、CMM 虚拟机化、线卡混配、10800W PoE）。共同纪律：MPLS/50G/大 VC 档位多走许可或"未来支持"，投标应答逐条核实。

## 三、本书在知识库中的位置

与 hw-6560（6560 硬件手册）、hw-6860/6865/6870/6900v2/9900（各系列手册）、os-lan-*（配置课程）互补：本书管"全家族横向选型"，系列书管纵深。与 Stellar AP 书联动：AP 侧 95W bt 需求 ↔ 6370-Z/6860N/6870 premium/9900 HPoE 口。跨书易混点：6560 的 E=enhanced 多千兆型，6900 的 E=全口 MACsec 版，同一后缀语义不同。

## 来源
bp-omniswitch-datasheets（15 份文档 158 页）。verified.md：cases C1-C12；counter-examples X1-X22（无 X6/X12）；frameworks F1-F6；principles P1-P26；glossary 约 70 条。
