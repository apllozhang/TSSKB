# frameworks — bp-omniswitch-datasheets（产品线定位矩阵/代际演进）

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
