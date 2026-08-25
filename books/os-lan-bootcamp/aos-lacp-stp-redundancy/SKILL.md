---
name: 链路聚合与生成树冗余（LACP/STP-RSTP-MSTP-PVST+/DHL）
description: 需要配置 LACP 或静态聚合（hash-control/主端口）、STP/RSTP/MSTP 根桥与负载分担、PVST+ 互操作、DHL 双归属 Active-Active 上行及 MAC 冲刷时使用本技能。
source_book: DT00CTE120 OmniSwitch R6/R8 Bootcamp Issue 25
---

## R（触发场景）
- 上行带宽扩容与链路冗余：LACP 动态聚合或 OmniChannel 静态聚合
- 园区防环与收敛优化：根桥规划、RSTP 端口角色、MSTP 多实例负载分担
- 与 Cisco 共存网络的 PVST+ 互操作
- 接入双上联两台不同核心、不想跑 STP 阻塞：DHL Active-Active
- 堆叠/VC 场景外的二层冗余选型对比

## I（核心理念）
聚合把多物理口合成单逻辑链路：静态 OmniChannel 仅限 OmniSwitch 间且两端参数必须完全一致；LACP（802.3ad）用 LACPDU 协商可跨厂商（P74，<<<PAGE 396>>>），关联靠 actor admin key 两端同值（P75，<<<PAGE 398-404>>>）。STP 家族的选型矩阵：协议 802.1D/802.1w（默认）/802.1s/ERPv2 × 模式 flat/1x1（默认）（F7，<<<PAGE 415>>>）。MSTP 的精髓是"同域三要素（域名+修订级+VLAN-实例映射）一致才是一个域，一帧 BPDU 携带全部实例"（P86/P87，<<<PAGE 438-443>>>），负载分担靠不同 MSTI 选不同根桥。DHL 用 VLAN-链路映射代替 STP 防环，两条上行都活跃、100% 带宽（P90/P93，<<<PAGE 477-481>>>）。冗余方案横向对比：STP 50% 带宽 < LACP 仅链路 < VC 全冗余 < DHL 链路+设备冗余 100% 带宽（F16，<<<PAGE 481>>>）。

## A1（决策/选型）
1. 动态 vs 静态聚合：跨厂商/防误配用 LACP；纯 OmniSwitch 间可用静态
2. 聚合规模：组大小仅 2/4/8/16；一端口只能属一个组（P73，<<<PAGE 395>>>）
3. 哈希档位：brief 仅 IP 对；extended 加 UDP/TCP 端口更均匀；组播默认走主端口，可开 non-ucast 哈希分担（P76/P77，<<<PAGE 401-402>>>）
4. STP 模式：flat 每机一棵树（MSTP/MVRP 必需）；1x1 每 VLAN 一棵树（默认，实例上限 R6=252/R7=128/R8=100）（P82/P83，<<<PAGE 427-429>>>）
5. 路径开销：STP/RSTP 用 16bit（GE=4）、MSTP 用 32bit（GE=20000），默认 auto（P84，<<<PAGE 432>>>）

## A2（操作步骤）
1. LACP 聚合：6450 `lacp linkagg 5 size 2 actor admin key 5` + `lacp agg 1/11 actor admin key 5`；6860(R8) `linkagg lacp agg 5 size 2 actor admin-key 5` + `linkagg lacp port 1/1/23-24 actor admin-key 5` → 激活端口 → `show linkagg`（Oper UP、Att/Sel 2/2）→ down 一成员口 ping 不丢验证（C17，<<<PAGE 404-406>>>）
2. 静态聚合：6860 `linkagg static agg 5 size 2` → `linkagg static port 1/1/23-24 agg 5`；删除须先清成员口再删组（直接删非空组报 LAERR53）（C19/P198，<<<PAGE 999-1002>>>）
3. STP 根桥控制：`show spantree`（默认 RSTP、priority 32768）→ `bridge 1x1 vid priority` / `spantree vlan instance {port|linkagg} priority`；GE cost=4 推断根口（C20/P79，<<<PAGE 418-464>>>）；根桥选举四判据：最低 Root Bridge ID > 最低路径开销 > 最低发送者 Bridge ID > 最低端口 ID（P79，<<<PAGE 420-425>>>）
4. MSTP 双实例负载分担：`bridge mode flat` → `bridge protocol mstp` → `bridge mst region name myregion` + `revision level 1` → `bridge cist protocol mstp` → `bridge msti 1 vlan 1-15`、`bridge msti 2 vlan 16-20`；A 机 cist/msti1 优先级 4096、msti2 8192，B 机对调；验证 `show spantree mst port 1/1`（MST1 ROOT/FORW、MST2 ALT/BLK）（C21/P89，<<<PAGE 444-472>>>）
5. DHL Active-Active：双上行打标签 → `dhl num 1` → `dhl num 1 linka port 1/3 linkb port 1/4` → `dhl num 1 vlan-map linkb 30` → `dhl num 1 admin-state enable`；验证 `show dhl num 1`（LinkA Active 1 20 / LinkB Active 30）；故障演练 `dhl num 1 mac-flushing raw` + ping –t（C22，<<<PAGE 487-489>>>）
6. PVST+ 互操作：用户口自动检测 PVST+ BPDU 转为 PVST+ 口；端口必须 1x1 模式（P85，<<<PAGE 433-434>>>）

## E（实证案例）
- C17 LACP 双端配置与成员口故障不丢包（<<<PAGE 404-406>>>）
- C21 MSTP 双实例负载分担（A/B 机优先级对调）（<<<PAGE 444-472>>>）
- C22 DHL Active-Active 与链路故障切换（<<<PAGE 487-489>>>）
- C19 静态聚合删除顺序报错实证（<<<PAGE 999-1002>>>）

## B（反例与坑）
- 一端口只能属一个聚合组；组非空不能删（X41，<<<PAGE 395, 1001>>>）
- 组播默认只走聚合主端口（X42，<<<PAGE 402, 887>>>）
- 1x1 与 MSTP 不能同时配置，MSTP 须 flat 模式；切 MSTP 会 reset flat 优先级与路径开销（X43/X44，<<<PAGE 471>>>）
- MSTP 链路须承载实例全部 VLAN，否则该实例不承载任何 VLAN（X45，<<<PAGE 444>>>）；32bit 开销与 802.1d/w 默认 16bit 不兼容注意（X46，<<<PAGE 471-472>>>）
- PVST+ 端口必须 1x1 模式（X47，<<<PAGE 434>>>）
- DHL 每机仅一个会话；DHL 口上 STP 自动禁用，须配 MAC 冲刷（None/MVRP Enhanced/RAW）（X48/P92，<<<PAGE 478-479>>>）；MVRP Enhanced 不支持 6250/6450，DHL 冲刷只能选 RAW（X49，<<<PAGE 479>>>）
- RSTP 把 802.1D 的 disabled/blocking/listening 合并为 discarding，亚秒收敛（P80/P81，<<<PAGE 420-423>>>）

## 来源
- principles·P72-P93/P198；frameworks·F7/F16；cases·C17-C22；counter-examples·X41-X49
