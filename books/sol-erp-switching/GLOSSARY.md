# GLOSSARY · Ethernet Ring Protection Switching Application Note

> 页码为原书 `<<<PAGE N>>>` 标记。按基础概念/消息与状态/定时器/恢复模式/多环/选型对比/端口与产品分组，精选 35 条。

## 基础概念
- **ERP / ERPS (Ethernet Ring [Protection] Switching)**：ITU-T G.8032/Y.1344 定义的以太环保护倒换，亚秒收敛、控制面开销低 <<<PAGE 5>>>
- **G.8032/Y.1344**：ITU-T 环保护建议书；本书基于 2020 版 Corrigendum 1（2022-02） <<<PAGE 5>>>
- **Ethernet ring**：至少两个环口的环节点连成的闭合物理环 <<<PAGE 5>>>
- **RPL (Ring Protection Link)**：平时被阻塞防环的那条链路；故障时解阻保连通 <<<PAGE 5>>>
- **RPL Owner Node**：RPL 一端负责阻塞/解阻的节点；正常态周期发 (NR, RB) <<<PAGE 5>>>
- **RPL Neighbour Node**：可选，负责阻塞 RPL 另一端 <<<PAGE 5>>>
- **FDB flush**：保护切换时清空转发表强制重学习；单链故障全环各 flush 两次 <<<PAGE 8-9>>>
- **Access Guarding**：ALE 面向用户/设备/IoT 的高级安全接入框架，可与 ERP 叠加 <<<PAGE 5>>>

## R-APS 消息与状态
- **R-APS (Ring Automatic Protection Switching)**：协调全环保护动作的协议；走专用 R-APS channel VLAN <<<PAGE 5-7>>>
- **R-APS 消息码 NR/RB/SF/DNF**：No Request / RPL Blocked / Signal Failure / Do Not Flush <<<PAGE 7-11>>>
- **Idle state**：正常态所有环节点所处状态，仅 RPL Owner 周期发 (NR, RB) <<<PAGE 7>>>
- **(Node ID, Blocked Port ID) 去重**：识别已知 SF 消息、避免重复 flush 的二元组 <<<PAGE 9>>>
- **R-APS NR**：No Request 消息，故障消除后由恢复链路两端发送 <<<PAGE 11>>>
- **R-APS (NR, RB)**：RPL Owner 回切通告，触发全网 unblock 与一次性 flush <<<PAGE 11-12>>>
- **DNF (Do Not Flush)**：RPL 自身故障时 SF 携带的标志，全环免 flush <<<PAGE 11>>>

## 定时器体系
- **Hold-off timer**：故障检测后等待定时器（0-10s 可配），过滤间歇性链路故障 <<<PAGE 8>>>
- **Guard timer**：链路恢复后两端忽略新 R-APS 的时段，防过期消息成环 <<<PAGE 11>>>
- **WTR (Wait-to-Restore) timer**：RPL Owner 收 NR 后的回切等待定时器，须长于 guard <<<PAGE 11>>>
- **低/高优先级 ID 解阻规则**：guard 过后低 ID 端解阻、高 ID 端继续阻塞，成单端阻塞 <<<PAGE 11>>>

## 恢复模式
- **Revertive mode**：修复后经 WTR 自动回切到 RPL 阻塞态 <<<PAGE 11-12>>>
- **Non-revertive mode**：修复后不回切，等管理员在 RPL Owner 上 clear；适合计划维护窗口 <<<PAGE 12>>>
- **Clear 命令**：non-revertive 模式下由管理员在 RPL Owner 发起的回切解除操作 <<<PAGE 12>>>

## 多环体系
- **Major ring / Sub-ring**：主环与子环；子环自身不闭合，与互联节点间链路共同成环 <<<PAGE 6>>>
- **Interconnection node**：同时接 major ring（双环口）与 sub-ring（单口）的节点 <<<PAGE 6>>>
- **R-APS Virtual Channel**：子环经互联节点共享链路传 R-APS 的通道 VLAN；多子环用不同 VLAN <<<PAGE 14>>>
- **多环三原则**：R-APS 不跨环共享；每端口单环控制；每环独立 RPL <<<PAGE 13>>>

## 选型对比与收敛
- **DHL (Dual Home Link)**：单节点双归接环技术，按 VLAN 改转发状态；不适用多节点接入层 <<<PAGE 13>>>
- **50ms 保护切换**：收敛指标；四前提 = 无拥塞/全 idle/节点<16/光纤<1200km；非端到端收敛 <<<PAGE 14-15>>>
- **VC (Virtual Chassis)**：多物理节点虚拟成单逻辑节点；与 ERP 组合加弹性但收敛变慢 <<<PAGE 15>>>
- **FRR (Fast Reroute)**：MPLS 预装备份下一跳的快速保护；同样不保证端到端 50ms <<<PAGE 15>>>
- **LACP 捆绑环链路**：环链路多光纤捆绑到 VC 不同物理节点提弹性 <<<PAGE 15>>>

## 端口、协议交互与产品
- **NNI**：网络间接口，可配为 ERP 环口保护 SVLAN <<<PAGE 16>>>
- **UNI**：用户网络接口，不可作 ERP 环口 <<<PAGE 16>>>
- **VLAN stacking / 802.1ad**：ALE ERP 可在 802.1ad 网络上运行，用 VLAN 堆栈保护 Service VLAN <<<PAGE 16>>>
- **ERP 口自动禁 STP**：端口设为 ERP 环口后 STP 自动禁用，端口状态归 ERP 控制 <<<PAGE 15>>>
- **BPDU 泛洪风险**：ERP 口不参与 STP 但 BPDUs 仍可经环口泛洪 <<<PAGE 13>>>
- **ERP 产品谱系**：9900/6900/6860E-N/6560/6570M/6865/6465T 全系支持 ERPv2 <<<PAGE 16>>>
- **配置拓扑参考**：major ring ERP#1 + sub-ring ERP#2 + 用户 VLAN 域 1001（节点 #3 为 RPL Owner） <<<PAGE 16-17>>>

---
合计：35 条。
