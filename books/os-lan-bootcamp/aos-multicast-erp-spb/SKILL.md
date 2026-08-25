---
name: 组播/ERP 环网/Intelligent Fabric（IPMS/PIM-SM/MVRP/G.8032/Auto-fabric/SPB）
description: 需要配置 OmniSwitch 二层组播（IPMS/IGMP）、三层 PIM-SM（RP/BSR/SPT）、MVRP 动态 VLAN、G.8032 ERP 环网保护、Auto-fabric 零接触部署或理解 SPB 织构定位时使用本技能。
source_book: DT00CTE120 OmniSwitch R6/R8 Bootcamp Issue 25
---

## R（触发场景）
- 园区内 IPTV/视频会议流量只发给订阅端口，不做全 VLAN 洪泛
- 跨网段组播需要 PIM-SM（RP/BSR 规划）
- 环形拓扑要 50ms 级保护倒换（ERP G.8032）
- VLAN 手工维护成本高，要动态注册裁剪（MVRP）
- 新交换机零接触上线（Auto-fabric：Auto-VC/LACP/Routing/MVRP）
- 评估用 SPB 替代 STP 做二层织构（6865/6900 iFab）

## I（核心理念）
组播分两层解（F14，<<<PAGE 874>>>）：同 VLAN 用 IPMS 硬件侦听 IGMP 按端口建转发表（默认禁用，须显式开，P172，<<<PAGE 875-878>>>）；跨网段用 PIM-SM 显式加入 + RP 共享树，末跳自动 SPT 切换（默认启用）（P177，<<<PAGE 908-909>>>）。IGMP 本身 TTL=1 永不出本段（P170，<<<PAGE 871>>>）。ERP 的机制是"牺牲一条 RPL 链路换全环无环"：APS 协议协调，RPL owner 负责阻塞/解阻塞（P178，<<<PAGE 926-929>>>）。Auto-fabric 七步零接触（Auto-VC → RCL → Auto-LACP → Auto-Routing → Auto-SPB → Auto-Network Profiling → Auto-MVRP），失败即删除并禁用配置（P27/F5，<<<PAGE 155, 936>>>）。SPB 用 IS-IS 替代 STP：简化业务开通、全链路可用（P186/F15，<<<PAGE 73, 68>>>）。

## A1（决策/选型）
1. 组播地址映射：D 类 224.0.0.0-239.255.255.255，MAC 取 01:00:5e + IP 低 23 位（P169，<<<PAGE 867>>>）
2. IGMP 版本：v2 加 Leave/快速离开；v3 加源过滤 SSM（P171，<<<PAGE 872>>>）
3. 组数管控：全局/VLAN/端口三级 max-group（端口级覆盖）（P174，<<<PAGE 885>>>）；不跑 PIM 的孤岛可用 IGMP Relay（helper）封装转发（P175，<<<PAGE 884>>>）
4. 二层冗余协议选型：STP/RSTP/MSTP vs ERPv2（F7，<<<PAGE 415>>>）——环形专网/汇聚环优先 ERP
5. MVRP 前提：全局使能 + STP flat 模式；只裁剪不建三层（P191，<<<PAGE 968>>>）

## A2（操作步骤）
1. IPMS 二层组播：`show ip multicast` 确认默认 disabled → `ip multicast admin-state enable`(R8) → `ip multicast querying enable` → `ip multicast querier-forwarding enable`（流源在非查询者交换机时启用，P173，<<<PAGE 879>>>）；验证 `show ip multicast group/neighbor/forward`，客户端加组后仅必要端口转发（C48，<<<PAGE 877-883, 916-918>>>）
2. PIM-SM：RP/BSR 侧 `ip load pim` → `ip pim sparse admin-state enable` → `ip pim interface int_217/int_218/int_110` → `ip pim cbsr 192.168.110.1` → `ip pim candidate-rp 192.168.110.1 231.1.1.0/24`；验证 `show ip pim cbsr/candidate-rp/neighbor/group-map/groute 225.0.0.101/sgroute …/mroute`（C49/P176/P177，<<<PAGE 908-913, 923>>>）
3. ERP 环网：各节点 `vlan 50 name "Ring1"`（Service VLAN 承载 R-APS/CCM）+ `vlan 60 name "subnet60"`（Protected VLAN），ring 口 tag 50 untag 60 → RPL owner（6900-A）：`erp-ring 1 port1 1/3 port2 2/1 service-vlan 50 level 2` → `erp-ring 1 rpl-node port 1/3` → `erp-ring 1 wait-to-restore-timer 1` → `erp-ring 1 enable`（其余节点仅 ring 定义+enable）→ 激活 ring 口 → `show erp`（Ring State Pending、rpl 标记）→ ping –t 中断链路观察切换与 WTR 恢复（C50/P178/P179，<<<PAGE 926-932>>>）
4. MVRP：前置 `spantree mode flat`（R6 `bridge mode flat`）→ `mvrp enable` → `mvrp port 1/3 enable`、`mvrp linkagg 5 enable` → 限额 `mvrp maximum vlan 150`(6450)/`mvrp maximum-vlan 150`(6860)；对端建 VLAN + tag 后本机 `show vlan` 出现 type dyn；验证 `show mvrp port 1/1/4 statistics/timers/last-pdu-origin`；结束恢复 `spantree mode per-vlan`（C53/P191/P192，<<<PAGE 968-971>>>）
5. Auto-fabric：`show auto-fabric config` → `auto-fabric discovery start` → `auto-fabric admin-state enable` → `auto-fabric config-save admin-state enable`；验证 `show linkagg port`（Auto-LACP agg 127/admin-key 65535，P183，<<<PAGE 943>>>）、`show vlan`（dyn VLAN）、`show mvrp port`（Discovery Status Enabled）（C51/P184/P185/P182，<<<PAGE 943-951, 941>>>）
6. Auto-VC/Auto-Routing 原理：无 vcsetup.cfg 时自动 Chassis ID、最低 MAC 为 Master（P181，<<<PAGE 940>>>）；侦听 OSPF/IS-IS Hello 学区域/类型/定时器自动建邻接（P184，<<<PAGE 944>>>）

## E（实证案例）
- C48 IPMS：开启前后泛洪 vs 端口级精准转发对比（<<<PAGE 877-883, 916-918>>>）
- C49 PIM-SM：RP/BSR + groute/sgroute 验证（<<<PAGE 908-913, 923>>>）
- C50 ERP：6560x2 + 6900x2 环网故障切换与 WTR 恢复（含拆/恢复 6900 VC）（<<<PAGE 926-932>>>）
- C51 Auto-fabric 三件套验证（Auto-LACP/Auto-MVRP/动态 VLAN）（<<<PAGE 943-951>>>）

## B（反例与坑）
- IGMP TTL=1 永不被路由器转发；查询发 224.0.0.1、离开发 224.0.0.2（P170/X70，<<<PAGE 871>>>）
- IPMS 默认禁用，组播交换须显式开启（X71，<<<PAGE 877, 916>>>）
- ERP RPL 只能配在已禁用的环上；无 RPL 或多 RPL 均为错误配置（X72，<<<PAGE 929>>>）；每环建议 ≤16 节点（X73/P180）；环数上限依机型（X74，<<<PAGE 929>>>）
- PIM-SM 的 SPT 状态默认启用（X75，<<<PAGE 903>>>）；rp-threshold 决定何时切源树（P177，<<<PAGE 909>>>）
- MVRP 须 STP flat 模式且不能配在 mirror/mobile/VPLS 口（X50，<<<PAGE 968>>>）；调低动态 VLAN 上限（默认 256）需重启 MVRP 生效（X51/P192，<<<PAGE 969>>>）
- Auto-VC 依赖出厂 Demo License；Auto-LACP 默认聚合 127、admin-key 65535，与手工聚合编号错开（<<<PAGE 938, 943>>>）

## 来源
- principles·P169-P186/P191/P192；frameworks·F5/F14/F15；cases·C48-C51/C53；counter-examples·X70-X75/X50/X51
