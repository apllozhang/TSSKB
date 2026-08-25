---
name: SPB 架构机制（IS-IS 控制面/BVLAN/ECT/Fabric 防环）
description: 需要理解或设计 SPB 骨干——为什么用 IS-IS 取代 STP、BVLAN/ECT 如何建树与负载分担、BEB/BCB 分工、BUM 三种复制模式选型、RPFC/LBD 双重防环时使用。
source_book: SPB Architecture Tech Brief（sol-spb DOC1）
---

## R（触发场景）
- 向客户/团队解释 SPB 与 STP/MPLS 的本质差异，或做骨干技术选型
- 规划 BVLAN 数量、ECT-ID 分配与等价路径负载分担
- 选择 BUM 复制模式（head-end / tandem (S,G) / tandem (*,G)）
- 排查骨干环路、瞬态环、广播风暴类问题（RPFC/LBD/风暴控制）

## I（核心理念）
双平面架构框架（F1，<<<PAGE 9>>>）：DP=802.1ah PBB（B-VID/ISID/B-SA/B-DA，只查 FDB 不做决策）+ CP=RFC 6329 IS-IS（拓扑发现、SPT 计算、服务成员泛播、FDB 预填充）。每节点以自己为根建 SPF 树，全部链路可用且路径最短（P1/P2，<<<PAGE 7>>>/<<<PAGE 11>>>）；MAC-in-MAC 把 CMAC 学习限制在 BEB 边缘，BCB 零感知（P4/P15，<<<PAGE 7>>>/<<<PAGE 10>>>）。每节点每 BVLAN 一棵树，ECT-ID 打破平局实现按服务负载分担（P17/P18，<<<PAGE 11-12>>>）；路径对称与确定性保障帧有序送达与 OAM 单向时延推算（P19/P20，<<<PAGE 12>>>）。防环分预防+缓解双机制：RPFC 校验入帧源 BMAC 与 FDB 一致性丢非合规帧（P45，<<<PAGE 51>>>）。

## A1（行动框架）
1. 骨干搭建四步（C1，<<<PAGE 16>>>）：建 BVLAN 配 ECT-ID → 定控制 BVLAN → 定义 SPB IS-IS 接口 → 启用 SPB IS-IS
2. BVLAN 容量规划：BVLAN 数量=物理等价路径数，不多建（P25，<<<PAGE 52>>>）；控制 BVLAN 一个（如 4000）
3. BUM 模式选型矩阵（F3，<<<PAGE 16>>>）：低组播带宽+多源少收→head-end（+IGMP Snooping）；高组播带宽+少源多收→tandem (S,G)（默认）；根桥为源宿或第三方互通→tandem (*,G)
4. 骨干防环三件套：RPFC（对称性破瞬态环，<<<PAGE 51>>>）+ LBD 全 UNI 口启用（P46，<<<PAGE 51>>>）+ 风暴控制默认开（<<<PAGE 52>>>）

## A2（操作步骤）
- **骨干验证命令族**（C2，<<<PAGE 18>>>）：`show spb isis interface`（L1 邻接、metric=10、Hello 9s/持失 27s）→ `show spb isis nodes`（system ID=BMAC、source ID、bridge priority）→ `show spb isis adjacency` → `show spb isis bvlans`（ECT 算法、(S,G)/(*,G)）→ `show spb isis unicast-table` → `show spb isis spf bvlan`
- **链路度量调优**（P49/P50，<<<PAGE 54>>>）：按速率反比设置（100G=1000…1G=100000），引导流量走高容量链路；必须两端同时改
- **LAG 哈希补熵**（P48，<<<PAGE 53>>>）：MAC-in-MAC 外层只剩 BMAC 缺熵，启用 tunnel-protocol 后可按 CMAC 或 IP+端口哈希
- **无扰维护**（P41/P42，<<<PAGE 48>>>）：overload 状态让节点退出中转（可定时回退）；graceful restart 保邻接平滑主备切换

## E（实证案例）
- 3 条等价路径样例拓扑建 4 个 BVLAN（4000-4003，4000 控制专用）（C1，<<<PAGE 16>>>）
- 骨干全套 show 命令逐项验证（C2，<<<PAGE 18>>>）

## B（反例与坑）
- STP 三宗罪：禁链路费带宽、非根间绕行次优路径、秒级收敛且瞬态成环（X1/X2/X3，<<<PAGE 5>>>）
- 以太网泛洪学习+全网学 MAC 不可扩展；Q-in-Q 服务实例上限 4096（X4/X5/X6，<<<PAGE 6>>>）
- MPLS 需协议栈（LDP/OSPF/MP-BGP），SPB 单协议搞定（X7，<<<PAGE 6>>>）
- BUM 模式取舍：head-end 复制费带宽、tandem (S,G) 每服务多耗 SPT/组播 FDB、tandem (*,G) 共享树不走最短路（X8/X9/X10，<<<PAGE 15-16>>>）
- BVLAN 超过等价路径数徒增控制面负担与收敛时间（X20，<<<PAGE 52>>>）
- overload 后若无备选路径则流量中断，维护前先确认替代路径（X19，<<<PAGE 48>>>）
- 客户网配置错误可引发跨 SPB+接入网的广播风暴，LBD 是最后防线（X29，<<<PAGE 51>>>）

来源：SPB Architecture Tech Brief（sol-spb DOC1，p5-56）
