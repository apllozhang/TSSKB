# Verified 候选（V1 原文真实性核对 + V2/V3 抽查）

## cases

- **C1 正常态 A/B 用户通信与各节点 FDB 快照**："communication between users A and B will be performed over the single available path which is over the direct ring link between ring nodes 1 and 2. Figure 5 also presents the forwarding database for each node." <<<PAGE 8>>>
- **C2 单链故障全流程状态走查（节点 1-2 间断链）**：hold-off → 两端节点本地阻塞/flush/双向发 SF → 其余节点各 flush 两次 → RPL Owner 解阻 RPL。<<<PAGE 8-10>>>
- **C3 故障后 FDB 重建过程**："Due to the FDB flushing, initial communication between users A and B will be flooded. However, once two-way communication is established, the MAC addresses of the users will be learned on the respective ports." <<<PAGE 10>>>
- **C4 RPL 自身故障例外场景（DNF 位）**："the process remains the same for the nodes at both ends of the RPL, except that a Do-Not-Flush (DNF) flag is included in the R-APS messages." <<<PAGE 11>>>
- **C5 回切恢复全流程（guard→NR→单端阻塞→WTR→NR,RB→全网 unblock+flush）**："When this timer expires, the RPL owner node: Starts blocking traffic over the RPL - flushes its FDB and Starts sending R-APS messages with the code No_Request, RPL-Blocked (NR, RB)." <<<PAGE 11-12>>>
- **C6 WTR 期间新 SF 打断回切**："the above-mentioned process may be stopped if a new R-APS SF message is received by the RPL owner during the WTR time countdown." <<<PAGE 11>>>
- **C7 非回切模式运维场景**："scheduled maintenance windows are preferred. In this mode, the network administrator has full control over the recovery process." <<<PAGE 12>>>
- **C8 多环设计实例（major + sub-ring，双 ERP 实例）**："the network in Figure 11 is designed to have two ERP instances... two different links are used as RPL for each ERP instance." <<<PAGE 13-14>>>
- **C9 R-APS Virtual Channel 实例**："When there are multiple sub-rings using the same shared links between interconnecting nodes, different VLANs will be used for the different R-APS virtual channels." <<<PAGE 14>>>
- **C10 收敛时间预算分解案例**：检测 + SF 生成发送 + 环传播 + 处理与 flush 四项合成。<<<PAGE 15>>>
- **C11 VC+LACP 弹性部署案例**："By deploying ring links consisting of multiple fibre links that are, using the LACP protocol, connected to different physical nodes of a ring node running VC / By dual-homing connectivity of the access layer devices to different physical nodes running VC." <<<PAGE 15>>>
- **C12 ERP+STP 分域协作与失效场景**："if network node 2 fails, the VLAN connectivity of the associated STP domain is completely disconnected... an alternative architecture, such as an ERP sub-ring, should be considered." <<<PAGE 16>>>
- **C13 附录配置拓扑（major ring ERP#1 + sub-ring ERP#2）**："a ring topology with a major ring running ERP instance #1 and a sub-ring running ERP instance #2. The user VLAN domain 1001 is connected to node #3, which is also the RPL owner node for the major ring." <<<PAGE 16-17>>>
- **C14 产品组合落地案例**：9900/6900 核心到 6865/6465T 室外严苛环境全谱系支持 ERPv2。<<<PAGE 16>>>

## counter-examples

- **X1 不阻 RPL 即成环**："In the Ethernet ring, the RPL is blocked for traffic to prevent loops."（反面：闭合环不阻塞必广播风暴）。<<<PAGE 5>>>
- **X2 间歇性链路故障误触发保护切换**："to allow automatic link recovery from intermittent link faults within this period"（hold-off 的存在理由）。<<<PAGE 8>>>
- **X3 重复 R-APS SF 导致反复 flush**："reception of subsequent messages will not cause the FDB to be flushed again. To avoid repeated flushing of the FDB, the ring nodes will check the pair (Node ID, Blocked Port ID)." <<<PAGE 9>>>
- **X4 RPL 故障时无谓 flush 拖慢收敛**："The Do-Not-Flush bit is set in the R-APS message so that other ring nodes in the network know that they don't need to flush their own FDBs, which would increase the convergence time." <<<PAGE 12>>>
- **X5 过期 R-APS 消息可能造成环路**："This is to prevent the nodes from receiving and acting on outdated R-APS messages which could create a loop in the network." <<<PAGE 11>>>
- **X6 间歇故障期间回切误动作**：WTR 的存在 "allowing the network to stabilise and preventing the operation of the protection switching due to intermittent link failure defects." <<<PAGE 11>>>
- **X7 自动收敛造成非预期业务中断（非回切模式动因）**："The network may be deployed in non-revertive mode to minimise the potential impact of automatic convergence following link recovery." <<<PAGE 12>>>
- **X8 STP 拉长收敛且可能引发不稳定**："any form of Spanning Tree Protocol is not recommended since they increase convergence time and could potentially cause network instability." <<<PAGE 13>>>
- **X9 DHL 不适用多节点接入层**："this technology is not a solution where multiple nodes are required in the access layer with a limited fibre optics availability." <<<PAGE 13>>>
- **X10 违反多环三原则的后果（R-APS 串环/双 RPL 冲突）**：三原则为 must——"the following principles must be respected: The R-APS protocol is not shared across Ethernet ring interconnections..." <<<PAGE 13>>>
- **X11 超规格环（>16 节点或 >1200km 或拥塞）保不住 50ms**："If any of these conditions are not met, the protection switching mechanism may take longer than 50ms." <<<PAGE 14>>>
- **X12 把 50ms 当端到端收敛的误解**："should not be interpreted as an end-to-end convergence time." VRRP/接入-核心间 L2 防环协议 "can significantly increase the overall network convergence time." <<<PAGE 15>>>
- **X13 MPLS FRR 同样不是端到端 50ms**："FRR does not provide end-to-end network convergence and service recovery within 50 ms for every event of network failure." <<<PAGE 15>>>
- **X14 VC 与 ERP 叠加增加收敛时间**："may increase its convergence time due to the added complexity of the control plane and the synchronisation of FDBs flushes." <<<PAGE 15>>>
- **X15 STP 域挂单节点故障全网断连**："if network node 2 fails, the VLAN connectivity of the associated STP domain is completely disconnected from the network." <<<PAGE 16>>>
- **X16 BPDUs 仍会经环口泛洪**："the ERP ports do not participate in the STP process, BPDUs could still be flooded over the ring ports and links." <<<PAGE 13>>>
- **X17 UNI 口误用作 ERP 口**："User-to-Network Interface (UNI) ports... cannot be used as ERP ring ports." <<<PAGE 16>>>

## frameworks

## F1 接入/汇聚层接入核心环的选型框架
三选项对比：STP/RSTP/MSTP（不推荐——收敛慢、潜在不稳定、且单挂节点故障断域）、DHL（仅适用单节点接入、按 VLAN 改转发状态）、multi-ring + ERP v2（推荐，支持多节点接入与光纤受限场景）。判定变量：接入节点数量、光纤资源、全网冗余要求。
- 引用："The recommended solution to connect one or more access devices to the core ring network is to use a multi-ring topology which is supported with ERP v2." <<<PAGE 13>>>
## F2 恢复模式选型框架（revertive vs non-revertive）
决策变量：能否接受链路修复后自动回切带来的短暂扰动。revertive：guard→NR→WTR（>guard）→(NR,RB) 全网回切，自动化但依赖定时器防抖；non-revertive：等待管理员 clear 或维护窗口，控制力最强、影响最小。
- 引用："In non-revertive mode... Only upon a 'clear' command initiated by a network administrator on the RPL owner node, non-revertive operation is cleared." <<<PAGE 12>>>
## F3 ERP 故障-恢复状态机框架（保护切换时间预算）
四段式时间分解：故障检测（hold-off 0-10s 可调）→ SF 消息生成发送 → 环上传播（节点数<16、光纤<1200km、无拥塞、全 idle 时 ≤50ms）→ 各节点处理与 FDB flush。规划时逐段核对 50ms 四前提，并区分"保护切换时间"与"端到端收敛"（叠加 VRRP/L2 防环协议）。
- 引用："several components must be considered, including: Time to detect... / Ring propagation delay... / R-APS SF message processing and FDB flushing..." <<<PAGE 14-15>>>
## F4 多环（multi-ring）设计规则框架
输入：major ring + N 个 sub-ring。规则：每环独立 ERP 实例与 RPL（不同链路）；互联节点可同时跑多实例，但每端口只受一个环控制；子环经互联节点共享链路时用 R-APS virtual channel（多子环用不同 VLAN）；互联链路本身归 major ring 管。可选：AOS 允许子环不用 virtual channel（R-APS 在互联节点终结，不在子环 RPL 阻塞）。
- 引用："Since the link(s) between interconnection nodes are controlled by the ERP1 instance, the ERP2 instance at the interconnection nodes must use the R-APS virtual channel." <<<PAGE 14>>>

## glossary

- **ERP / ERPS (Ethernet Ring [Protection] Switching)**：ITU-T G.8032/Y.1344 定义的以太环保护倒换技术，亚秒收敛、控制面开销低。<<<PAGE 5>>>
- **G.8032/Y.1344**：ITU-T 环保护建议书；本文基于 2020 版 Corrigendum 1（2022 年 2 月）。<<<PAGE 5>>>
- **Ethernet ring**：由至少两个环口的环节点连成闭合物理环的集合。<<<PAGE 5>>>
- **RPL (Ring Protection Link)**：环上平时被阻塞以防环的那条链路；故障时解阻保连通。<<<PAGE 5>>>
- **RPL Owner Node**：RPL 一端负责阻塞/解阻的节点；正常态发 (NR, RB)。<<<PAGE 5>>>
- **RPL Neighbour Node**：可选，负责阻塞 RPL 另一端的节点。<<<PAGE 5>>>
- **R-APS (Ring Automatic Protection Switching)**：协调所有环节点保护动作的协议；走专用 R-APS channel VLAN。<<<PAGE 5-7>>>
- **R-APS 消息码 (NR/RB/SF/DNF)**：No Request（无请求）、RPL Blocked（RPL 阻塞）、Signal Failure（信号故障）、Do Not Flush（免 flush 标志）。<<<PAGE 7-11>>>
- **Idle state**：正常态下所有环节点所处状态，仅 RPL Owner 周期发 (NR, RB)。<<<PAGE 7>>>
- **Hold-off timer**：故障检测后的等待定时器（0-10 秒可配），过滤间歇性链路故障。<<<PAGE 8>>>
- **FDB (Forwarding Database) flush**：保护切换时清空转发表以强制重新学习；环单链故障时全环节点各 flush 两次。<<<PAGE 8-9>>>
- **(Node ID, Blocked Port ID) 去重**：环节点用该二元组识别已知 SF 消息、避免重复 flush。<<<PAGE 9>>>
- **DNF (Do Not Flush)**：RPL 自身故障时 SF 消息携带的标志，通知全环无需 flush（拓扑未变）。<<<PAGE 11>>>
- **Guard timer**：链路恢复后两端忽略新 R-APS 消息的时段，防过期消息成环。<<<PAGE 11>>>
- **R-APS NR**：No Request 消息，故障消除后由恢复链路两端发送。<<<PAGE 11>>>
- **低/高优先级 ID 解阻规则**：guard 过后，ID 较低一端解阻、较高一端继续阻塞，形成单端阻塞。<<<PAGE 11>>>
- **WTR (Wait-to-Restore) timer**：RPL Owner 收 NR 后启动的回切等待定时器，须长于 guard timer。<<<PAGE 11>>>
- **R-APS (NR, RB)**：RPL Owner 回切时通告"无请求且 RPL 已阻塞"，触发全网 unblock 与一次性 flush。<<<PAGE 11>>>
- **Revertive mode**：故障修复后经 WTR 自动回切到 RPL 阻塞态的模式。<<<PAGE 11-12>>>
- **Non-revertive mode**：修复后不自动回切，等管理员在 RPL Owner 上执行 clear。<<<PAGE 12>>>
- **Major ring / Sub-ring**：多环结构中的主环与子环；子环自身不闭合，与互联节点间链路共同成环。<<<PAGE 6>>>
- **Interconnection node**：同时接入 major ring（双环口）与一个或多个 sub-ring（单口）的互联节点。<<<PAGE 6>>>
- **R-APS Virtual Channel**：子环实例经互联节点共享链路传 R-APS 消息所用的（虚拟）通道 VLAN；多子环用不同 VLAN 区分。<<<PAGE 14>>>
- **DHL (Dual Home Link)**：单节点双归接入环网的技术，按 VLAN 修改转发状态防环；不适用多节点接入层。<<<PAGE 13>>>
- **50ms 保护切换**：ERP 收敛指标，仅在无拥塞、全 idle、节点<16、光纤<1200km 四条件下成立；非端到端收敛。<<<PAGE 14-15>>>
- **VC (Virtual Chassis)**：多物理节点虚拟成单逻辑节点；与 ERP 组合可加弹性但增加收敛时间。<<<PAGE 15>>>
- **FRR (Fast Reroute)**：MPLS 中预装备份下一跳的快速保护；同样不保证端到端 50ms。<<<PAGE 15>>>
- **NNI / UNI**：网络间接口（可配为 ERP 环口保护 SVLAN）/ 用户网络接口（不可作 ERP 环口）。<<<PAGE 16>>>
- **VLAN stacking / 802.1ad**：ALE ERP 支持在 802.1ad 网络上运行，用 VLAN 堆栈保护 Service VLAN。<<<PAGE 16>>>
- **Access Guarding**：ALE 面向用户/设备/IoT 高级安全接入框架，与 ERP 叠加增强关键业务网络。<<<PAGE 5>>>

## principles

- **P1 防环靠"任一时刻只阻塞一条环链路"**："Loop avoidance, this principle guarantees that at any time traffic can flow through all but one ring link." <<<PAGE 7>>>
- **P2 正常态 RPL Owner 阻塞 RPL 并周期通告 (NR, RB)**："All ring nodes are in Idle state with only the RPL node sending R-APS messages, using a dedicated VLAN for it, informing other nodes in the ring that the RPL is blocked (RB) and there is no request (NR)." <<<PAGE 7>>>
- **P3 故障检测先过 hold-off 再动作**："This detection will initiate their hold-off timer before taking any protection switching action to allow automatic link recovery from intermittent link faults within this period that could be configured between 0 and 10 seconds." <<<PAGE 8>>>
- **P4 检测节点三连动作：本地阻塞 + FDB flush + 双向发 SF**："Internally block for traffic on the failed ring port / Perform flushing of their FDB / Start sending R-APS messages with Signal Failure (SF) code." <<<PAGE 8>>>
- **P5 收到首个 SF 即 flush，靠 (Node ID, Blocked Port ID) 去重**："the ring nodes will check the pair (Node ID, Blocked Port ID) within the R-APS SF message and will not respond to the receipt of messages with already known and stored pair of IDs." <<<PAGE 9>>>
- **P6 RPL Owner 收 SF 解阻 RPL**："On receipt of the first R-APS message with the SF code, the RPL owner will also unblock its end of the RPL." <<<PAGE 9>>>
- **P7 RPL 自身故障带 DNF 位免全网 flush**："a Do-Not-Flush (DNF) flag is included in the R-APS messages along with the SF condition... there is no need to flush their FDBs as the topology is not changed." <<<PAGE 11>>>
- **P8 恢复期 guard timer 屏蔽过期 R-APS 防环**："nodes at both ends of the link will start a guard timer during which both nodes will ignore newly received R-APS messages... could create a loop in the network." <<<PAGE 11>>>
- **P9 恢复后低优先级 ID 端先解阻，形成单端阻塞**："The node with the lower priority ID will unblock its port of the recovered link for traffic while the node with the higher ID will continue to block traffic." <<<PAGE 11>>>
- **P10 WTR 长于 guard timer，防抖后再回切**："the RPL owner node will start the Wait-to-Restore timer (WTR), which is configured to be longer than the guard timer, allowing the network to stabilise." <<<PAGE 11>>>
- **P11 回切由 RPL Owner 发 (NR, RB) 触发全网 unblock + 一次性 flush**："Upon receiving R-APS (NR, RB) messages, all ring nodes should unblock any blocked link ports... The FDB flush is only performed upon receiving the first R-APS (NR, RB) message." <<<PAGE 11>>>
- **P12 非回切模式把控制权交给管理员**："Only upon a 'clear' command initiated by a network administrator on the RPL owner node, non-revertive operation is cleared." <<<PAGE 12>>>
- **P13 多环三原则**："The R-APS protocol is not shared across Ethernet ring interconnections / On each ring port, each R-APS control protocol and protected VLANs are controlled by only one Ethernet ring / Each major or sub-ring must have its own RPL." <<<PAGE 13>>>
- **P14 子环跨共享链路必须用 R-APS Virtual Channel**："the ERP2 instance at the interconnection nodes must use the R-APS virtual channel for its R-APS protocol messages." 多子环共用互联链路时用不同 VLAN 区分。<<<PAGE 14>>>
- **P15 接入层接环推荐 multi-ring，不推荐 STP**："The recommended solution to connect one or more access devices to the core ring network is to use a multi-ring topology which is supported with ERP v2." <<<PAGE 13>>>
- **P16 ERP 口自动禁 STP，域内分工协作**："When configuring an ERP network by setting up a port as an ERP ring port, the Spanning Tree Protocol would be automatically disabled on that port since the port state would be controlled by the ERP protocol." <<<PAGE 15>>>
- **P17 50ms 有四个前提条件**："There is no congestion / All nodes are in the idle state / The number of nodes in the ring is less than 16 / The ring fibre length is less than 1200km." <<<PAGE 14>>>
- **P18 50ms 是保护切换时间，不是端到端收敛**："The 50 ms period for the protection switching mechanism should not be interpreted as an end-to-end convergence time." <<<PAGE 15>>>
- **P19 ERP 与 VC 组合可提升弹性但代价是收敛变慢**："combining these two technologies in the network may increase its convergence time due to the added complexity of the control plane and the synchronisation of FDBs flushes." <<<PAGE 15>>>
- **P20 NNI 可作 ERP 口保护 SVLAN，UNI 不可**："The Network-to-Network Interface (NNI) ports can be configured as ERP ports to protect the Service VLANs (SVLANs)... User-to-Network Interface (UNI) ports... cannot be used as ERP ring ports." <<<PAGE 16>>>
