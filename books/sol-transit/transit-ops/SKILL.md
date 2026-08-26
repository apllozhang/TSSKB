---
name: 轨交 SPB 网运维监控（OmniVista/OOB 与带内管理/802.1ag L2 ping-trace/SAA 性能测试/Overload 与 Graceful Restart）
description: 运维已建成的轨交 SPB 网时使用：OmniVista 2500 的 SPB 拓扑视图、带外（OOBMN+EMP）与带内（管理 ISID/管理 VLAN 随 BVLAN）五种管理通道方案、802.1ag 在 BVLAN/CVLAN 两级维护域的 L2 ping 与 L2 trace、SAA 自动测时延抖动丢包、Overload state 优雅下线维护与 IS-IS Graceful Restart。
source_book: Transportation Networks Design Guide & SPB-based Transportation Networks Design Guide
---

## R（何时用）
- 规划轨交网的管理通道（带外/带内、管理 VLAN/ISID 设计）
- 部署 OAM（802.1ag）做 SPB 骨干与端到端业务的连通性排查
- 建立时延/抖动/丢包的持续性能基线（SAA auto-create）
- 计划维护窗口：节点下线用 Overload、VC/双主控切换靠 Graceful Restart 保转发

## I（核心理念）
管理面先通才能运维：设备侧 Console/Telnet/SSH/Web，远程管理要 IP 连通，还要通 RADIUS（AAA 与终端准入）（通用版 p51-52）。管理通道两大家族：带外（独立物理网，走 EMP 专用口或 ACL 锁定的标准口）与带内（管理 ISID + hairpin、管理 VLAN 随 BVLAN 同跑并配 STP/ERP、或将来的 in-line routing）（通用版 p52）。故障排查主用 802.1ag 的 L2 ping（LBM/LBR）与 L2 trace（LTM/LTR）：BVLAN 级给所有 BEB 配 virtual MEP（可选 BCB）、MIP 自动生成，因无 CCM，trace 输出只显示 B-MAC；CVLAN 级 OAM 放在更高维护域级别，可测站到站、站到 OCC 的端到端业务连通（通用版 p52-53）。性能基线用 `saa auto-create` 在所有 BEB/BCB 间、所有 BVLAN 上自动建时延/抖动/丢包测试（通用版 p54）。维护两板斧：Overload state 让其他节点不再经由本节点转发（等效全链路调大 metric 但更快），可无限期或定时恢复；Graceful Restart 让 VC 主控/CMM 切换期间保邻接、保 FDB，靠 RR TLV 通告重启、邻居回灌 LSDB（通用版 p54-55）。

## A1（决策要点）
1. 管理通道选型：安全等级高的项目选 OOBMN（EMP 口仅 10K/9900/6860E 有）；带内则管理 ISID + hairpin 最干净，管理 VLAN 随 BVLAN 跑要配 STP/ERP 防环（通用版 p52）
2. 标准口做带外管理时必须 ACL 锁定、并禁止路由协议在管理口收发（通用版 p52）
3. OAM 分级：BVLAN 级 MEP 全 BEB（排骨干）、CVLAN 级更高维护域（排端到端业务）；CCM 与 SPB 不配套，别指望系统名，认 B-MAC（通用版 p52-53）
4. SAA 用 `saa auto-create` 一次铺全网基线，配合 OmniVista 2500（4.3 起 SPB 拓扑视图：单播/组播链路、SPB 服务端口展示）（通用版 p54、p51）
5. 计划维护先设 Overload（定时恢复更稳），再做硬件操作（通用版 p54）
6. VC 或双主控机型必开 Graceful Restart，避免切换期拆除邻接重建拓扑造成的流量损伤（通用版 p54-55）

## A2（细节速查表）

| 管理方案 | 形态 | 要点 | 页码 |
|---|---|---|---|
| 带外-EMP | 专用管理物理口 | 仅 10K/9900/6860E 具备；只走管理流量 | 通用版 p52 |
| 带外-标准口 | 专用管理 VLAN + loopback IP | ACL 锁定；路由协议不进管理口 | 通用版 p52 |
| 带内-管理 ISID | 管理 VLAN 经 hairpin+SAP 映射 ISID | 与业务共物理网但逻辑隔离 | 通用版 p52 |
| 带内-VLAN 随行 | 管理 VLAN 与 BVLAN 同跑骨干口 | 需 STP/ERP 防环 | 通用版 p52 |
| 带内-in-line routing | loopback IP 直接驻留管理 ISID | OS9900 路线图特性，需向 ALE 确认 | 通用版 p52 |

| 运维工具 | 用途 | 配置要点 | 页码 |
|---|---|---|---|
| L2 ping（LBM/LBR） | BEB 间连通验证 | BVLAN 级 virtual MEP 配全 BEB | 通用版 p52-53 |
| L2 trace（LTM/LTR） | 逐跳路径核查 | 输出引用 B-MAC（无 CCM 无系统名） | 通用版 p52-53 |
| CVLAN 级 OAM | 站间/站到中心端到端测试 | 维护域级别须高于 BVLAN OAM | 通用版 p53 |
| SAA auto-create | 时延/抖动/丢包基线 | 全 BEB+BCB、全 BVLAN 自动建 | 通用版 p54 |
| OmniVista 2500 | 拓扑与 SPB 视图 | 4.3 起：BVLAN 单播/组播链路、服务端口展示 | 通用版 p51 |
| Overload state | 优雅下线维护 | 等效全链路 metric 调大但更快；可定时回退 | 通用版 p54 |
| Graceful Restart | 主控切换保转发 | RR TLV 通告；邻居保持邻接并回灌 LSDB | 通用版 p54-55 |

## E（场景案例）
- BEB 之间用 LBM/LBR 验证连通、LTM/LTR 逐跳核查路径的 OAM 实操（通用版 p53）
- L2 设计下用 CVLAN 级 OAM 验证"站—OCC/BCC"端到端业务通道（通用版 p53）
- 维护窗口流程：设 Overload → 流量绕行 → 换板/升级 → Overload 回退（通用版 p54）
- VC master 切换：开 GR 后邻接不拆、FDB 不清、LSDB 快速重建（通用版 p54-55）

## B（限制与坑）
- 指望 CCM 做故障检测——SPB 有 IS-IS 控制面，CCM 不与 SPB 配套（通用版 p52）
- trace 输出找系统名——没有 CCM 映射，只有 B-MAC，要备好 B-MAC 与节点的对照（通用版 p52）
- CVLAN OAM 维护域级别配得不高 BVLAN OAM——域层级冲突（通用版 p53）
- in-line routing 当现网特性写进方案——它是 OS9900 路线图项（roadmap feature），需向 ALE 确认（通用版 p52）
- 带外标准口不锁 ACL、放路由协议进管理口——管理通道被业务流量与路由更新污染（通用版 p52）
- 通用版评审批注对 802.1ag 与 SPB 的支持口径提出需 PLM 复核，落地前建议再确认（通用版 p52）

## 来源
Transportation Networks Design Guide（p51-55）+ SPB-based Transportation Networks Design Guide（p38-41，无 OmniVista 小节）
