# counter-examples — sol-erp-switching（书中警告的失败模式，英文原句 + 真实页码）

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
