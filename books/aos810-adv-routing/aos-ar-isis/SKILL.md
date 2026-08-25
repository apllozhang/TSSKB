---
name: AOS 8 IS-IS（area-id/Level-1-2/认证/汇总/M-ISIS 多拓扑）
description: 需要在 OmniSwitch AOS 8 上配置 IS-IS（area-id 与 NET、Level-1/L2 层级、IIH/LSP/CSNP 报文体系、分层认证、路由汇总、L1→L2 泄漏、M-ISIS 多拓扑 IPv4/IPv6 双栈、宽度量）时使用。
source_book: OmniSwitch AOS Release 8.10R4 Advanced Routing Guide
---

## R（触发场景）
- 新上线 IS-IS：area-id → level 能力 → 电路（接口）→ admin-state 十步流程
- 规划 Level-1/L1-2/L2 路由器角色与区域归属（路由器整体属单区域，与 OSPF 接口分域不同）
- 要配分层认证（全局/level/电路/电路级四层）或 keychain
- 要做 L1→L2 泄漏、L2→L1 前缀分发、路由汇总；IPv4/IPv6 双栈要选单拓扑还是 M-ISIS 多拓扑

## I（核心理解）
IS-IS 两层层级（P42）：Level-1 区内、Level-2 区间；与 OSPF 最大差异是路由器整体属于单一区域（P47）。NSAP 三字段 Area ID + System ID + NSEL，NSEL=00 时称 NET（P43）。报文四类：IIH 发现邻居、LSP 承载链路状态、CSNP 全量清单同步、PSNP 请求确认（P46）。邻接三要素：认证匹配、IS 类型、MTU（P45）。M-ISIS 为 IPv4/IPv6 各自独立 SPF 与 RIB（MT ID：IPv4=0、IPv6=2），解决单拓扑混布黑洞问题（P54/P55）。

## A1（决策框架）
1. **角色规划**：区内路由器 level-1、区间路由器 level-1/2、纯骨干 level-2；全局与接口 level 能力组合决定潜在邻接（P48）
2. **认证分层**：全局 → level → 电路 → 电路级，低层覆盖全局（P50）；排障期可 auth-check 关闭只报错不丢包（P51）
3. **域间路由**：L1→L2 泄漏经 route map（P53/C17）；内部路由不能在 L1 汇总，只有外部重分发路由可以（X20）
4. **双栈选型**：域内有 v4-only/v6-only 设备时必须 M-ISIS 多拓扑（P54），否则单拓扑即可（但混布会黑洞）
5. **度量**：metric > 64 必须先开 wide-metrics（X18）

## A2（操作步骤）
- **十步上线**：`vlan 5` → `ip interface vlan-5 ...` → `ip load isis` → `ip isis area-id 49.0001` → `ip isis admin-state enable` → `ip isis activate-ipv4` → `ip isis vlan 5` + `address-family v4` → `ip isis vlan 5 admin-state enable` → `show ip isis status`（C14，<<<PAGE 92>>>）
- **双栈双路由器**：各建 vlan-isis（v4+v6 地址）→ `ip isis level-capability level-1/2` → `ip isis vlan vlan-isis address-family v4v6` + enable → `show ip isis adjacency/routes/spf`（C15，<<<PAGE 117-119>>>）
- **认证**：全局 `ip isis auth-type md5 key 12345`；level 级 `ip isis level 2 auth-type md5 encrypt-key ...`；电路级 `ip isis vlan 10 hello-auth-type md5 key 12345`；keychain `ip isis auth-type key-chain 2`（C16，<<<PAGE 106-108>>>）
- **L1→L2 泄漏**：`ip route-map is2is sequence-number 1 action permit` + `match route-type level1` + `set level level2` → `ip redist isis into isis route-map is2is status enable`（C17，<<<PAGE 115>>>）
- **汇总**：`ip isis summary-address 100.1.0.0/16 level-2`；IPv6 `ip isis summary-address6 4001::/16 level-1`；`show ip isis summary-address[6]`（C18，<<<PAGE 104-105>>>）
- **M-ISIS**：`ip isis multi-topology`；切换模式会复位全部邻接（C19/X23，<<<PAGE 120-121>>>）

## E（实证案例）
- IS-IS 十步上线与验证（C14，<<<PAGE 92>>>）
- 双路由器 L1/L2 双栈应用例（C15，<<<PAGE 117-119>>>）
- 认证四层配置（C16，<<<PAGE 106-108>>>）
- L1→L2 泄漏 route map（C17，<<<PAGE 115>>>）
- 汇总 v4/v6（C18，<<<PAGE 104-105>>>）与 M-ISIS 切换（C19，<<<PAGE 120-121>>>）

## B（反例/坑）
- IS-IS GR 当前仅支持 helper 模式（X14）；且仅在堆叠备/空闲交换机的活动口上支持（X15）；次 CMM 路由 MAC 不同或 VLAN 端口在主模块时 STP 重收敛可能中断 GR 转发（X16）（<<<PAGE 116>>>）
- route map 的 tag 参数当前版本不支持（X17，<<<PAGE 110>>>）
- metric 大于 64 必须先开 wide-metrics（X18，<<<PAGE 115>>>）
- 每路由器最多 3 个 area ID（X19，<<<PAGE 102>>>）
- L1 内部路由不能汇总（只有外部重分发路由可以）（X20，<<<PAGE 104>>>）
- 点到点链路 L1 未配认证时，无论 L2 怎么配，L1 hello 都裸奔（X21，<<<PAGE 107>>>）
- retransmit 间隔必须大于往返时延否则无谓重传（X22，<<<PAGE 110>>>）
- 切换 multi-topology 模式复位全部 IS-IS 邻接（X23，<<<PAGE 120>>>）
- encrypt-key 只接受系统生成的合法值（X24，<<<PAGE 106>>>）
- 从内存移除 IS-IS 必须手改 boot.cfg 并重启（X10，<<<PAGE 102>>>）
- DIS 选举按接口优先级（默认 64），平局比 SNPA/MAC（P44，<<<PAGE 95>>>）
- 点到点口无共同拓扑不成邻接；广播网即使无共同拓扑也成邻接（P57，<<<PAGE 120>>>）

## 来源
OmniSwitch AOS 8.10R4 Advanced Routing Guide 第 3 章 IS-IS（<<<PAGE 89-121>>>）。条目来源：cases C14-C19；principles P42-P59；counter-examples X10/X14-X24；frameworks F1/F2/F3/F6。
