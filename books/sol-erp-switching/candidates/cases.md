# cases — sol-erp-switching（作者亲自演练的案例，页码为真实标记）

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
