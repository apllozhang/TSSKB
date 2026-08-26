---
name: 轨交网络业务系统与需求基线（四大类系统/VPN 隔离/可用性/环境加固）
description: 规划轨道交通或智能交通（ITS）承载网时摸底业务与需求用：Control/Safety/Communications/Information 四大类系统清单（信标/ATC/CCTV/PIS/AFC 等）、六大网络需求（虚拟化多租户、亚秒收敛、可扩展、QoS、安全、工业环境），以及 SPB 收敛能力与信号系统 50ms 红线的关系。
source_book: Transportation Networks Design Guide & SPB-based Transportation Networks Design Guide
---

## R（何时用）
- 新建轨交/有轨电车/智能交通项目立项，需要梳理"网上到底要跑哪些业务系统"
- 与业主或信号专业对齐网络需求指标（隔离、收敛、规模、环境）
- 判断信号（Signaling/ATC）这类 50ms 级业务能否上 SPB 统一网
- 编写需求规格书或方案书的"业务与需求"章节

## I（核心理念）
轨交业务系统分四类：Control（控制）、Safety（安全）、Communications（通信）、Information（信息），全部跑在一张共享网络 上，靠 VPN/容器做逻辑分割（通用版 p11-12、p14）。网络设计被六大需求驱动：多租户虚拟隔离、无单点故障的亚秒级收敛、可扩展到几十系统/几百节点/几千终端、单级 QoS 按系统分级、设备加固与准入安全、轨道旁设备须满足 EN 50121 / NEMA TS-2 工业规格（通用版 p14-17）。一条硬红线：SPB 收敛时间通常大于 200ms（8.5R2 目标 100ms 以内），满足不了信号系统 50ms 要求，这类业务必须走独立网络（SDH/SONET 或 MPLS）（通用版 p7、p15）。

## A1（决策要点）
1. 先按四类清点业务系统，逐系统确认带宽流向（OCC→车站 / 车站→OCC / 站间 / 本地），这是后续链路容量规划的输入（通用版 p12-14、p39-40）
2. 每个系统一个 VPN 容器、一个流量等级——单级 QoS 够用，不必上层次化 QoS（通用版 p16）
3. 收敛指标口径：网络无 SPOF 时中断时长等于收敛时间，本指南按"亚秒级"设计（通用版 p15）
4. 车载、车地、车车通信不在本设计指南范围内（SPB 版 p5、通用版 p7-8）
5. 选设备前先核对环境等级：轨道旁须无风扇、抗振、耐极端温度、EMI/EMC 达标（通用版 p16-17）

## A2（细节速查表）

| 业务类别 | 代表系统（轨交） | 说明 | 页码（通用版） |
|---|---|---|---|
| Control | Signaling、ATC（ATP/ATO/ATS） | 防碰撞、保持安全车距、按图停站与调度 | p12 |
| Safety | Video Surveillance、Emergency Call、Fire/Alarm、Access Control | 人身与资产安全、事件响应 | p12 |
| Communications | Telephony、Wireless LAN | 员工通信，兼作紧急呼叫与广播的底层 | p12-13 |
| Information | PIS、Passenger Announcement、Infotainment、Internet | 乘客信息与增值收入 | p13-14 |

| 需求维度 | 要点 | 页码 |
|---|---|---|
| 虚拟化 | 一张物理网，VPN 容器隔离多系统/多租户 | 通用版 p14-15 |
| 可用性 | 无 SPOF、自动恢复、在线维护；SPB 收敛 >200ms（8.5R2 目标 <100ms） | 通用版 p15、p7 |
| 可扩展 | 几十个系统、几百节点、几千终端与组播流 | 通用版 p15-16 |
| 性能与 QoS | 按系统映射流量等级，单级 QoS 足够 | 通用版 p16 |
| 安全 | 节点加固抗 DDoS、准入与角色访问、隔离受损设备；通用版增加完整性与机密性 | SPB 版 p11、通用版 p16 |
| 环境 | EN 50121（轨道旁）、NEMA TS-2（路边机柜）、无风扇加固 | 通用版 p16-17 |

## E（场景案例）
- 轻轨单线（OCC+BCC+20 站）按此框架清点出 CCTV/PA/PIS/电话/AFC/门禁/TDS 七个系统并逐一估带宽（通用版 p40）
- ITS 场景：TMS/VSL/收费/TIS 与轨交系统重叠清点（通用版 p11-12）
- 信号系统 50ms 需求被明确排除出 SPB 网、另行建 SDH/MPLS 网的边界决策（SPB 版 p5）

## B（限制与坑）
- 把信令/ATC 塞进 SPB 网——收敛能力不达标，属于范围错误（通用版 p7）
- 忽视轨道旁环境等级，用普通商用交换机上架——不满足 EN 50121/NEMA TS-2（通用版 p16-17）
- 业务系统只报"路数"不报流向（本地 vs 上环），容量规划必然失真（通用版 p39-40）
- 默认所有业务同等级承载——拥塞或故障绕行时无差别丢包，必须按系统分流量等级（通用版 p16）

## 来源
Transportation Networks Design Guide（p7-17、p39-40）+ SPB-based Transportation Networks Design Guide（p5、p8-11）
