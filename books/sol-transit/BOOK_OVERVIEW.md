# ALE 轨道交通网络设计指南 · 课程书总览

## 两份源文档的定位差异

| | Transportation Networks Design Guide（通用版） | SPB-based Transportation Networks Design Guide（SPB 版） |
|---|---|---|
| 篇幅 | 70 页，2023 年 2 月版 | 42 页，早期版本 |
| 定位 | 通用版 = SPB 版全部技术内容 + 三块独有扩展 | SPB 方案版，聚焦 SPB 织构（iFab）在轨交骨干的设计 |
| 独有内容 | 第 6 章安全纵深防御（IoT/边界/DoS/MACsec/NAC/容器化/IDS 联动/认证）；第 7 章产品选型（角色-机型映射、OS6465、USB 备份/告警继电器）；第 8 章 10 年长期支持；OmniVista 2500 SPB 拓扑视图；收敛目标更新（8.5R2 冲 100ms） | 内容被通用版完整吸收，仅个别表述不同（如 Head-End 优化条件写作 Multicast Optimization Phase II；机型提及 OS6855） |
| 共有内容 | 业务系统四大类、六大网络需求、环网/OCC/BCC 架构、L2/L3 VPN 站点设计、BVLAN/LAG/VC/metric/QoS、组播三模式、20 站轻轨容量案例、ERP/STP/LBD 挂接、Network Profiles、管理/OAM/SAA/Overload/GR | 同左 |
| 使用建议 | 默认以通用版为准 | 交叉核对用；通用版内嵌大量评审批注（实验室验证状态、官方支持口径），两版对照能识别"哪些结论未定论" |

## 单元导航（9 个技能单元）

| 单元 | 主题 | 主要来源与页码 |
|---|---|---|
| transit-overview | 业务系统四大类与六大网络需求基线 | 两版第 1-2 章（通用版 p7-17、SPB 版 p5-11） |
| transit-architecture | 环网拓扑、OCC/BCC、L2 vs L3 VPN 站点架构、双归、规格表 | 两版第 3-4 章 + 5.1（通用版 p18-28、SPB 版 p12-20） |
| transit-spb-design | BVLAN/LAG tunnel-protocol/VC/link metric/QoS 映射 | 两版 5.2-5.6（通用版 p29-34、SPB 版 p21-26） |
| transit-multicast | BUM 三种复制模式、PIM/SSM、复制流量推演表 | 两版 5.7（通用版 p35-39、SPB 版 p26-29） |
| transit-capacity | 链路容量规划与 20 站轻轨流量矩阵案例 | 两版 5.8（通用版 p39-45、SPB 版 p30-34） |
| transit-attachment | 站点接入挂接（ERP/STP）、LBD 防环、Network Profiles 自动开通 | 两版 5.9-5.10（通用版 p45-51、SPB 版 p34-38） |
| transit-ops | 管理通道、802.1ag、SAA、Overload、Graceful Restart | 两版 5.11（通用版 p51-55、SPB 版 p38-41） |
| transit-security | 安全纵深防御（IoT/边界/DoS/MACsec/NAC/容器/IDS） | 仅通用版第 6 章（p55-65） |
| transit-products | 角色到机型映射、OS6465、10 年 LTS | 仅通用版第 7-8 章（p65-70） |

源文件：`sources/transportation-networks-design-guide-fulltext.md`（通用版）、`sources/spb-transportation-networks-design-guide-fulltext.md`（SPB 版）。
