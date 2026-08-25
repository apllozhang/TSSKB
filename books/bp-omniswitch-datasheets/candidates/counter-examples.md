# counter-examples — bp-omniswitch-datasheets（限制/边界/订购注意）

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

- **X6 OS6465T 无冗余电源** <<<PAGE 48>>>
  "OS6465T-12... Primary power: Internal AC / Backup power: N/A"
  要点：与 6465（双端子）不同，仅内置单电源。

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

- **X12 OS6860 MPLS 仅 N 型且需许可** <<<PAGE 83>>>
  "MPLS support for virtualized environments... The feature is supported on OS6860N. The software license required for the feature usage."
  要点：E 增强型不带 MPLS。

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
