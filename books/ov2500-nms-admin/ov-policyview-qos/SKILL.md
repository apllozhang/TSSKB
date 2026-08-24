---
name: PolicyView QoS 策略配置
description: 需要下发 QoS/ACL 策略到交换机（OneTouch 一键模式 Voice/Data/ACL，或 Expert Mode 专家向导做复杂条件策略如按源目 IP 阻断）时使用。
source_book: DT00XTE311 OmniVista 2500 NMS Administration R4
---

## R（触发场景）
- 要给语音/数据流分配差异化优先级（Platinum/Gold/Silver/Bronze）
- 需要按 L2/L3/L4 条件做精细策略，比如阻断某网段访问某网段
- 策略下发后不确定交换机是怎么拿到策略的（Policy Flow）

## I（核心理念）
PolicyView 双模式：OneTouch 面向常见场景（Voice/Data/ACL），"Sets parameters once, Distributed to devices at the same time"；Expert Mode 面向复杂策略（含验证机制）。底层架构是 LDAP 策略仓库：策略创建后存入安装时配置的 LDAP 服务器，交换机被通知后自行拉取。

## A1（行动框架）
1. **四步法**（<<<PAGE 275>>>）："Create a Policy Condition / Create a Policy Action / Create a Policy Rule / Apply the Policy"
2. **OneTouch**（<<<PAGE 273/276-278>>>）：三子模式——Voice、Data（Platinum/Gold/Silver/Bronze 优先级）、ACL（Accept/Drop）
3. **Expert Mode 向导**（<<<PAGE 279-284>>>）：Create Policy（名称/Precedence/高级选项）→ Device Selection → Set Condition（L2 MAC/L3 IP/DSCP/L4/L7）→ Set Action（QoS/Disposition/TCM）→ Validity Period and Review
4. **下发与确认**：Existing Policies 选策略 → Select Device → "Click on Notify Selected and wait for the Notify Success! Message"（<<<PAGE 293>>>）

## A2（进阶应用）
- 策略归一化（应用侧，<<<PAGE 365-366>>>）："The Policy has to be included in a Policy List. Then, the Policy List is included as part of the Access Role Profile configuration."；Unified Policy 本身 "are part of the Access Role Profile configuration"（<<<PAGE 246>>>）
- SIP Snooping 联动：识别并标记 SIP 及 RTP/RTCP 流（DSCP 字段），计算 Delay/Jitter/RTT/R factor/MOS；OneTouch 媒体模板固定优先级——Voice dscp 46/precedence 50000、Video dscp 34/44000、Other dscp 24/44001（<<<PAGE 438/442>>>）

## E（实证案例）
- Expert Mode 阻断客户端访问 Loopback0 网段：Name=Block_Loopback0_access、Precedence=30001、Device=switch8、Condition：L3 IPs，Source 192.168.80.0/24 → Destination 192.168.200.0/24、Action：QOS + Disposition=DROP、Validity=AllTheTime；验证 ping 192.168.200.# 不通、ping 192.168.100.102 正常——cases·PolicyView Expert（<<<PAGE 290-293>>>）

## B（边界与陷阱）
- 下发后必须等到 "Notify Success!" 才算确认，没等到就验证会误判（<<<PAGE 293>>>）
- Precedence 数值决定策略优先顺序，实验用 30001，需与现网既有策略序号统筹（<<<PAGE 291>>>）
- 策略生效依赖 LDAP 仓库链路：PolicyView 创建 → 存入 Policy Directory Server → Policy Enabled → 交换机从 LDAP 拉取（<<<PAGE 272/286>>>）

## 来源
- frameworks·QoS 四步法（<<<PAGE 275>>>）、双模式框架（<<<PAGE 273-284>>>）、Policy Flow（<<<PAGE 272/286>>>）
- principles·LDAP 仓库架构（<<<PAGE 272/285>>>）、SIP Snooping（<<<PAGE 438/442>>>）
- cases·Expert Mode 阻断实验（<<<PAGE 290-293>>>）
