---
name: Quarantine Manager 隔离与 PolicyView QoS 策略
description: 需要配置终端隔离体系（IPS 事件流/Candidates/Banned/Never Banned/Disabled Ports、QMR 隔离 VLAN、自定义规则正则）或 PolicyView QoS 策略（Unified Policy/One Touch/Expert、TCM、Notify 机制）时使用。
source_book: OmniVista 2500 NMS 4.9R2 User Guide
---

## R（触发场景）
- IPS/Syslog/trap 报攻击事件，要把涉事终端隔离到修复 VLAN
- 自定义隔离规则（正则匹配 Syslog 字段）
- 排查"设备进了 Banned 但流量还能通"
- 做有线+无线统一 QoS 策略、按 L7 应用限速、One Touch 语音策略

## I（核心理念）
Quarantine Manager 是事件驱动的状态机：IPS/交换机事件→规则匹配（Banned 优先于 Candidate）→ Candidates（流量照常，等决策）/ Banned（进隔离 VLAN，走 QMR）/ Disabled Ports（端口禁用，须逐条释放）/ Never Banned（OV 与交换机隐式在内）；无线客户端不进 Banned 而进 Client Blocklist。PolicyView 策略存 OV 内置 LDAP，交换机被 SNMP 通知后自行拉取（Notify 是"通知-拉取"不是推送）。

## A1（行动框架）
1. **事件处理链**（frameworks·F13，<<<PAGE 457, 460-465>>>）：IPS（Fortinet 2.3）/交换机发 Syslog(514)或 trap（含 IP/MAC）→规则→①Candidates（管理员 Release/Ban/Never Ban）→②Banned（Scheduled to be Banned→Completed/Partially Banned；Release 解封）→③Disabled Ports（全部条目释放端口才启用）
2. **隔离基础设施三件套**（principles·P137，<<<PAGE 473-475>>>）：Quarantined VLAN + "Quarantined" MAC Group + L2 Source MAC Group Drop 策略——缺一则 Banned 设备照样通流量
3. **PolicyView 模式选型**：One Touch（Data/ACL/Voice 简化）vs Expert（手工逐参数，仅 AOS）vs Unified Policy（有线+无线通用，不能直接下 IAP）（principles·P108-P110，<<<PAGE 384-389>>>）

## A2（操作步骤）
- **配置 Quarantine 基础设施**：Groups 建 Quarantined MAC 组→PolicyView 建 L2 Source MAC Group+Drop 策略并 Notify→Quarantine Manager→Configuration 编辑 Quarantined VLAN（VLAN/MAC 组名/Remediation URL/IP/HTTP Proxy Port/Allow Port Disabling/Allowed Subnets ≤3 个含 Remediation Server）→Apply to Devices（cases·C45，<<<PAGE 473-475>>>）
- **创建自定义规则**：Rules→Add：Name/Trigger Expression（如 log_id=0421073001）/Extraction Expression（如 src=([0-9.]*)）/Action（Candidate List/Quarantine/Release——Release 可供工单系统自动解封）/Event Type（Syslog/Trap）/Enabled→Create；ALE 下发的 .xml 规则用 Import 导入（默认 Disabled）（cases·C46，<<<PAGE 470-471>>>）
- **处理隔离事件**：Candidates 选设备 Release/Ban/Never Ban；Banned 可 Add 手工封禁（IP/MAC+Reason）/Release/Retry/Redo Ban；Disabled Ports 逐条 Release；Fortinet 事件右键跳官网分析页（cases·C47，<<<PAGE 461-465>>>）
- **创建 Unified Policy 向导**：PolicyView→Unified Policies→Add：Config for Policy（Name/Precedence 自动填最低未用值）→Device Selection（Devices+AP Groups）→Set Condition（L2 MACs/L3 IPs/L3 DSCP-TOS/L4 Services/L7 Application Visibility/ICMP）→Set Action（QoS/TCM）→Validity Period→Review（cases·C39，<<<PAGE 388-396>>>）
- **One Touch Data 策略**：选 Priority（Platinum/Gold/Silver/Bronze）→Add 输 Server IP→Create（Unsaved）→Save 存 LDAP→Notify All 下发（触发全网 flush+reload，注意批量）（cases·C40，<<<PAGE 403>>>）
- **PolicyView 后保存配置四步**：按 Changes 列排序→Unsaved 设备 Save to Running→Uncertified 设备 Copy Working/Running to Certified（cases·C38，<<<PAGE 386>>>）
- **TAD 流量异常检测**：OS6850/6855/9700 AOS 6.4.6.R01+；最多 32 组、14 种异常类型（ARP×3/ICMP×3/TCP×8）；Sensitivity 默认 50；Log/Trap/Quarantine 默认全 Disabled（principles·P140/P141，<<<PAGE 478-479>>>）

## E（实证案例）
- Quarantine 基础设施三件套 + Apply to Devices（cases·C45，<<<PAGE 473-475>>>）
- 自定义规则（Trigger/Extraction 正则）（cases·C46，<<<PAGE 470-471>>>）
- Candidates/Banned/Disabled Ports 三列表处置（cases·C47，<<<PAGE 461-465>>>）
- Unified Policy 七步向导（cases·C39，<<<PAGE 388-396>>>）

## B（反例/坑）
- 未配置 VLAN/MAC 组时 Banned 设备照样能通流量——三件套缺一不可（principles·P137，<<<PAGE 473-475>>>）
- 无线客户端不进 Banned 而进 Client Blocklist（365 天），且要求 Stellar AP 启用 IoT；4.9R1 前已在 Banned 的无线客户端不自动迁移（counter·X38 / principles·P132，<<<PAGE 460>>>）
- 重复禁用同端口产生空 MAC 双条目；Release Banned 不会自动恢复端口——须再到 Disabled Ports List 手工释放；端口要等所有引发封禁的条目都释放才启用（counter·X39，<<<PAGE 465>>>）
- QMR 与 QoS inner VLAN/inner 802.1p 策略及 VLAN Stacking 互斥（counter·X40 / principles·P134，<<<PAGE 459>>>）
- EMP 子网设备不可隔离；OV 服务器与所有已发现交换机隐式在 Never Banned（principles·P132/P133，<<<PAGE 457, 464>>>）
- 内置 13 条规则默认 Disabled、默认动作 Candidate，可改不可删（principles·P134/P135，<<<PAGE 466-467>>>）
- 正则坑：[0-13] 是错误语义，扩展 DOS 类型应写 ([0|2|6|9]|1[0123])；抽取失败查 server.txt（principles·P136，<<<PAGE 468-470>>>）
- PolicyView QoS 执行后所有 AOS 设备进入 Unsaved 状态，不保存则配置丢失（counter·X3 / principles·P10，<<<PAGE 44>>>）
- Notify 代价极高：全网 QoS 交换机 flush 策略表再从 LDAP 重载，务必批量一次通知；删除策略不联动设备，须再 Notify Selected（principles·P115，<<<PAGE 396-397, 400>>>）
- PolicyView 优先级域 30001-65535（One Touch Voice 45000+ / Data 40000+ / Expert 30000+），外部工具切勿占用该域（principles·P109，<<<PAGE 387>>>）
- 同时指定源+目的 IP 会被交换机拒绝（拆两条）；L2 MAC 条件过路由即失效（principles·P111/P113，<<<PAGE 390-395>>>）
- 启用 OpenFlow 会耗尽 TCAM，之后无法再配 QoS 策略（principles·P108，<<<PAGE 384-385>>>）
- 编辑被策略引用的 Group 后不能只 re-notify，须建新 Group 改策略（principles·P110，<<<PAGE 387-389>>>）

## 来源
OmniVista 2500 NMS 4.9R2 User Guide 第 22 章 PolicyView（<<<PAGE 384-412>>>）、第 25 章 Quarantine Manager（<<<PAGE 457-479>>>）、入门章保存流程（<<<PAGE 44>>>）。条目来源：frameworks F13；cases C38/C39/C40/C45/C46/C47；principles P108-P117/P132-P142；counter-examples X3/X38/X39/X40。
