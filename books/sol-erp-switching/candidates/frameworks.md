# frameworks — sol-erp-switching（决策框架 / 思维模型）

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
