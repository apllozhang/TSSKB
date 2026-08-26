---
name: 站点接入网挂接骨干与防环（ERPv2 子环两种闭环法/STP 挂接/Loopback Detection/Network Profiles 自动开通）
description: 站点（车站/段场）接入网双归接入 SPB 骨干时的挂接与防环设计：ERPv2 子环经 SAP UNI 挂接与经 ERP UNI 借 BEB 互联链路闭环（后者可保 50ms）两种方式、STP 挂接的域隔离与 MSTP 区域法、LBD 环回检测保骨干、Network Profiles 按 MAC/IP/VLAN/认证自动绑 VPN 与策略。
source_book: Transportation Networks Design Guide & SPB-based Transportation Networks Design Guide
---

## R（何时用）
- 设计车站/站点接入网（ERP 环或 STP）到骨干 BEB 的挂接方式
- 双归双 BEB 后的成环风险治理（STP 域规划、LBD 部署）
- 规划成千上万端设备的自动开通方案（Network Profiles + RADIUS + MVRP）
- 排查接入网广播风暴冲击骨干、SAP 端口被误 shutdown 等问题

## I（核心理念）
站点接入网双归到两台 BEB 后，SPB 骨干逻辑上就是一台"大交换机"，接入侧的误配置和故障可能造出横跨接入网与骨干的大环、引发广播风暴（通用版 p48）。防环三层递进：ERP 挂接、STP 挂接、LBD 兜底。ERP 挂接两法：子环经 SAP 口接到两台 BEB、只通过 SPB 骨干闭环（通用，但不是所有故障模式都能保 50ms）；或利用骨干本身也是环、两台 BEB 间有直连链路的特点，让 ERP 保护 VLAN 与业务 VLAN 直接跑在 BEB 互联链路上用 ring port 闭环、再经 hairpin 映射 SAP（可保子环故障 50ms）（通用版 p45-47）。STP 挂接时 NNI 口对 BVLAN 自动关闭 STP、SAP 口默认透传 BPDU；L2 全站共享 VLAN/ISID 会让所有站落进同一个 STP 域，须按站分 MSTP region 并用 max-hop 约束（通用版 p47）。LBD 周期发探测帧、收到即判定成环并 shutdown 整个物理端口，应在所有 UNI 口开启（通用版 p48）。开通自动化靠 Network Profiles：按 MAC/IP/VLAN 标签/802.1x 或 MAC 认证把设备绑到 VLAN 或 SPB 服务，VLAN/服务不存在可动态创建，并携带 ACL 与 QoS 策略（通用版 p49-51）。

## A1（决策要点）
1. ERP 子环挂接选型：追求子环故障 50ms 收敛选 ERP UNI 闭环法（借 BEB 互联链路跑 ring port）；通用场景用 SAP UNI 挂接法，但明确不承诺所有故障模式 50ms（通用版 p45-47）
2. 子环不得用额外 ring/SAP 口自行闭环，只能经 SPB 骨干闭环；子环业务 VLAN 必须与 BEB SAP 匹配（tagged/untagged 均可）（通用版 p45）
3. STP 挂接：NNI 口 BVLAN 的 STP 自动关闭；共享 VLAN/ISID 的 L2 场景必须按站分 MSTP region + max-hop（通用版 p47）
4. LBD 在所有 UNI 口开启；SAP 口检测到环会 shutdown 整个物理口（不只是该 SAP），要有运维预案（通用版 p48）
5. 开通方案定型：接入交换机按认证/MAC/IP 绑 VLAN + MVRP 动态上联；BEB 侧 SAP UNI 用 SPB NP 按 VLAN 标签绑服务、可动态建服务；VLAN UNI 侧则配 trunk 静态放行；hairpin 两侧静态配置（通用版 p50）
6. Network Profiles 同时承载差异化 ACL/QoS——安全与 SLA 随设备类型自动下发（通用版 p50-51）

## A2（细节速查表）

| 挂接/防环方式 | 机制 | 关键约束 | 页码 |
|---|---|---|---|
| ERPv2 子环 + SAP UNI | 子环经两 BEB 的 SAP 口、由 SPB 骨干闭环，R-APS PDU 经骨干隧道 | 子环业务 VLAN 须匹配 SAP；非所有故障模式保 50ms | 通用版 p45-46 |
| ERP + ERP UNI（BEB 直连链路闭环） | ERP VLAN 与 BVLAN 同跑 BEB 互联链路，ring port 闭环 + hairpin 映射 SAP | SAP 口不能做 ring port，故用 hairpin；可保 50ms；L2/L3 设计均可用 | 通用版 p46-47 |
| STP 挂接 | 站内非环拓扑或三方设备不支持 ERP 时用 | NNI 口 BVLAN 自动关 STP；SAP 默认透传 BPDU；共享 VLAN/ISID 需分 MSTP region + max-hop | 通用版 p47 |
| Loopback Detection | 周期发 LBD 帧，收到即 shutdown 端口 + trap + log | 与 STP/ERP 叠加运行；SAP 口检测到环关闭整个物理口；应开在所有 UNI 口 | 通用版 p48 |

| Network Profiles 绑定依据 | 适用 | 页码 |
|---|---|---|
| MAC 地址（或段） |哑终端、固定设备 | 通用版 p50 |
| IP 地址 | 固定地址终端 | 通用版 p50 |
| VLAN 标签 | 按 VLAN 归类（BEB SAP UNI 绑 SPB 服务） | 通用版 p50 |
| 802.1x / MAC 认证（RADIUS） | 需准入控制的场景，返回 UNP | 通用版 p50、p63-64 |
| MVRP 动态上联 | 接入侧新建 VLAN 自动加到上联（前提 VLAN 已存在于他机） | 通用版 p50 |

## E（场景案例）
- ERPv2 子环经 SAP UNI 挂接、R-APS 经 SPB 隧道传到对端 BEB 的参考拓扑（通用版 p46）
- 借 BEB 互联链路用 ring port 闭环 ERP 环、hairpin 完成 SAP 映射的 50ms 方案（通用版 p47）
- 全站共享 VLAN/ISID 导致所有站在同一 STP 域、用 MSTP region + max-hop 拆分的场景（通用版 p47）
- LBD 探测帧从各 SAP 发出、命中即关端口的骨干保护场景（通用版 p48-49）
- 接入交换机认证绑 VLAN → MVRP 上联 → BEB SPB NP 动态建服务的端到端自动开通链（通用版 p50-51）

## B（限制与坑）
- SAP UNI 挂接法对外承诺 50ms——原文明确"非所有故障模式都能 50ms"（通用版 p45）
- 子环私接 ring/SAP 口自行闭环——破坏"只经骨干闭环"的设计前提（通用版 p45）
- L2 共享 VLAN/ISID + SAP 透传 BPDU = 全网一个 STP 域，域内故障全域震荡（通用版 p47）
- LBD 误伤：一个 SAP 成环 shutdown 整个物理口，同口其他 SAP 陪葬（通用版 p48）
- 通用版文档评审批注提示：ERP UNI 闭环法与 STP 挂接的实验室验证状态不一、LBD 存在已知问题可能不再推荐——落地前须向 ALE 核实最新支持状态（通用版 p46-48）

## 来源
Transportation Networks Design Guide（p45-51）+ SPB-based Transportation Networks Design Guide（p34-38，内容基本对应）
