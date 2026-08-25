# glossary — bp-omniswitch-datasheets（型号与规格术语，按系列分组）

## SMB 接入
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
