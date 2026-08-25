---
name: SPB L2/L3 服务（ISID 二层服务/VRF/L3 VPN/路由泄漏）
description: 需要在 SPB 骨干上创建二层 VPN 服务（service+ISID+BVLAN+SAP）、做 VLAN 翻译与 L2Profile、规划三层路由形态（单次直通/两次回环）、部署 L3 VPN 或 VPN Lite、实现共享服务路由泄漏时使用。
source_book: SPB Architecture Tech Brief（sol-spb DOC1）
---

## R（触发场景）
- 创建多站点 L2 服务（ISID/BVLAN/SAP）并验证
- 同一服务下 tagged/untagged 客户互通（VLAN 翻译）或控制 SAP 上 STP 等协议（L2Profile）
- 规划 L3：选 VPN Lite 还是 L3 VPN、两代 ASIC 路由形态判定
- 共享服务（如公共服务器区）经 VRF 路由泄漏供多租户访问

## I（核心理念）
三层标识体系（F2，<<<PAGE 13>>>）：Service（本地有效）→ ISID（全局服务/租户标识，24 位 16M）→ BVLAN（承载与负载分担）；SAP=UNI 侧虚拟端口、SDP 由控制面动态生成只为有 SAP 的远端 BEB 创建（P22，<<<PAGE 14>>>）。服务只在 BEB 实例化、BCB 零配置（P9，<<<PAGE 8>>>）。L3 服务靠边缘路由：路由只发生在入/出 BEB，WAN 是单跳 L3（P28，<<<PAGE 29>>>）；L3 VPN 复用 IS-IS TLV 直接传 VRF 路由，单协议更简（P29，<<<PAGE 30>>>）；域内选 L3 VPN、边界对接外部才用 VPN Lite（P30，<<<PAGE 34>>>）。

## A1（行动框架）
1. L2 服务创建三步（C3，<<<PAGE 20>>>）：`service N spb isid X bvlan Y` → 物理口设为 SAP → 定义匹配客户流量的 SAP；只配相关 BEB
2. 服务号治理（P27，<<<PAGE 21>>>）：service 本地有效可各节点不同；ISID 全局一致必须全 BEB 匹配
3. L3 方案分档：域内→L3 VPN（IS-IS 带路由）；边界→VPN Lite（L2 服务上叠 OSPF/BGP）；共享服务→VRF 路由泄漏五步（C11，<<<PAGE 35>>>）
4. 路由形态判定（C7，<<<PAGE 26>>>）：新 ASIC 单次直通（IP 接口直接绑服务）；老 ASIC 外部物理回环或内部前面板回环（dummy VLAN 中转）

## A2（操作步骤）
- **L2 服务验证**（C4，<<<PAGE 22>>>）：`show service spb`（BEB/BCB 视图）→ `show spb isis services` → `show service access`（SAP 类型与 L2Profile）→ `show service spb ports` → `show mac-learning domain spb`（BCB 不学 CMAC）
- **VLAN 翻译**（C5，<<<PAGE 23>>>）：服务级 `service service_id vlan-translation enable` + SAP 级 `service access port vlan-xlation enable` 双开关
- **L2Profile**（C6，<<<PAGE 24>>>）：`service l2profile name stp action…` 定义 peer/drop/tunnel
- **外部物理回环**（C8，<<<PAGE 28>>>）：每路由服务建 dummy VLAN；回环口一端作 VLAN 口、另一端作 SAP；IP 接口加 `rtr-port` 防 VLAN 扩散并关 STP
- **L3 VPN 五步**（C9，<<<PAGE 31>>>）：L2 服务 → 租户 VRF → LAN/WAN 侧 IP 接口（WAN 直挂或 dummy VLAN）→ 绑 ISID → VRF 与 IS-IS ISID 实例互导路由
- **L3 VPN 验证**（C10，<<<PAGE 33>>>）：远端 LAN 网段为 IMPORT 路由、下一跳指远端 BEB WAN 地址；ARP 动态学远端网关
- **路由泄漏五步**（C11，<<<PAGE 35>>>）：shared_services VRF 经 route-map 过滤导出全局表 → 导入客户 VRF → 客户路由导入 shared VRF → 从各客户 ISID 导入远端客户路由 → shared 路由重分发回各客户 ISID

## E（实证案例）
- 服务器 tagged/客户端 untagged 经 VLAN 翻译互通（C5，<<<PAGE 23>>>）
- L3 VPN 验证输出：IMPORT 路由+远端下一跳+动态 ARP（C10，<<<PAGE 33>>>）
- 两代 ASIC 三种路由形态的判定与各自适用（C7，<<<PAGE 26>>>）

## B（反例与坑）
- VPN Lite 配置量爆炸：4 客户服务×8 BEB = 64 个 OSPF 配置；路由协议叠加收敛变慢（IS-IS 先收 OSPF 才能收）（X12/X13，<<<PAGE 34>>>）
- L3 VPN 依赖 SPB IS-IS，无法直连外部网络——边界必配 VPN Lite（X14，<<<PAGE 34>>>）
- 路由泄漏前提：客户间及与共享服务地址空间不重叠（X15，<<<PAGE 34>>>）
- 第一代 ASIC 跨服务路由需双次过交换矩阵+外部物理回环（X11，<<<PAGE 26>>>）
- 两次路由时标准 VLAN 口应信 CoS 而非 DSCP，否则 CoS 端到端丢失（P52，<<<PAGE 54>>>）

来源：SPB Architecture Tech Brief（sol-spb DOC1，p20-35）
