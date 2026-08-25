# frameworks — sol-spb（F1…）

- **F1 SPB 双平面架构框架**：DP（802.1ah PBB：B-VID/ISID/B-SA/B-DA，只查 FDB）+ CP（RFC 6329 IS-IS：拓扑发现、SPT 计算、服务成员泛播、FDB 预填充）；DP/CP 职责分离是理解全书一切机制的骨架 <<<PAGE 9>>>
- **F2 服务框架三层标识体系**：Service（本地有效）→ ISID（全局服务/租户标识）→ BVLAN（承载与负载分担）；虚拟端口 SAP（UNI 侧绑定物理口+流量类型）与 SDP（NNI 侧动态指向远端 BEB）；服务只在 BEB 实例化、BCB 零感知 <<<PAGE 13>>>
- **F3 BUM 三模式选型矩阵**（Table 1）：head-end / tandem (S,G) / tandem (*,G) × 带宽效率 / 资源效率 / 同余性 / 建议场景（低组播带宽+多源少收 / 高组播带宽+少源多收 / 根桥为源宿或第三方互通）<<<PAGE 16>>>
- **F4 CE 接入冗余四级模型**：非冗余 → 冗余链路（LAG）→ 冗余链路+节点（DHL / 动态路由）→ 全冗余（CE 双机 + MSTP/VRRP）；L2 与 L3、L3-CE 与 L2-CE 分别套用；VC+LAG 可与所有档位组合 <<<PAGE 49>>>
- **F5 iFab 自动化分层框架**：Auto-Fabric 六阶段（VC/RCD/LACP/SPB/MVRP/IP）打底 → UNP+认证做动态 SAP → Dynamic Services 按 VLAN 标签即时生成 UNP/服务（BSN/Domain ID/Service Modulo 公式体系）<<<PAGE 36>>>
- **F6 中型园区部署参考架构**（部署指南）：2×BCB 全网格 + N×BEB 双归 LAG + PBR 策略路由器；VRF 按部门分段、VRRP 网关冗余（.1 虚地址 + 末位 BEB 号）、/30 点对点连 PBR、OSPF 按 VRF 分 area、PBR 集中策略；可平滑加 BCB 横向扩展 <<<PAGE 63>>>
