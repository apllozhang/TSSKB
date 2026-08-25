---
name: AOS 8 QoS 与策略体系（分类/标记/限速/policy/ACL/SIP snooping）
description: 需要在 OmniSwitch AOS 8 上配置 QoS 分类与标记、队列调度（QSet）、policing/shaping/tri-color、policy 条件-动作-规则、条件组/map group、L2/L3/IPv6 ACL 安全策略，以及 SIP snooping 语音 QoS 时使用。
source_book: OmniSwitch AOS Release 8.10R4 Network Configuration Guide
---

## R（触发场景）
- 语音/视频流量要优先转发：分类标记+队列调度
- 某些应用/用户要限速：policing/shaping、tri-color 三色
- 按五元组/MAC/端口做精细策略：policy condition+action+rule
- 大量同类地址要复用条件：条件组（network/service/MAC/port group）
- 安全需求：ACL drop/accept 规则入 policy
- IP 语音要按 SIP 信令识别媒体流给 QoS：SIP snooping

## I（核心理念）
QoS 四步处理链（F8/P156，<<<PAGE 1103>>>）：分类标记→拥塞管理（入队调度）→拥塞避免（随机丢弃防 tail drop）→policing/shaping。策略三元组：policy=condition+action+rule；流不匹配任何策略则用端口默认 QoS，多策略命中取最高 precedence（P158，<<<PAGE 1133>>>）。每端口 8 条队列，入队依据策略+ToS/802.1p+端口信任状态（P159）。策略来源决定修改权：PolicyView(LDAP) 建的只能 PolicyView 改，CLI/WebView 建的只能本端改（P160/X61，<<<PAGE 1133>>>）。四类策略列表：default/UNP/egress/AFP（AFP 仅 OS6900）（P161，<<<PAGE 1134>>>）。

## A1（决策框架）
1. **先定分类**：信任口采信报文已有 802.1p/ToS；802.1Q tagged 口默认 untrusted——上联口语音/视频标记不生效的常见原因（X64，<<<PAGE 1134>>>）
2. **再定队列与限速**：QSet profile 配每口调度参数；带宽控制选 policy 带宽 policing（sr/tcm 三色）或端口 bandwidth policing
3. **复杂策略走 policy 体系**：条件组（network/service/MAC/port group）免逐地址建条件；map group 做标记映射；ACL 条件+drop/accept 动作入 policy rule（F8，<<<PAGE 1103>>>/<<<PAGE 1133>>>）
4. **语音流识别选 SIP snooping**：trusted call server+RTCP 阈值（注意一揽子限制，见 B）

## A2（操作步骤）
- **条件组与 map group**：network group/service group/MAC group/port group 建好后挂到单个 condition；map group 做标记映射；验证 show policy group/map（cases·C52，<<<PAGE 1176>>>）
- **ACL 安全策略**：L2/L3/IPv6 ACL 条件+drop/accept 动作入 policy rule，`qos apply` 生效（cases·C53，<<<PAGE 1142>>>）
- **端口限速/整形与 tri-color**：policy 带宽 policing（sr/tcm 三色）+端口 bandwidth policing（cases·C54，<<<PAGE 1118>>>）
- **提交**：policy condition/action/rule 配置后必须 `qos apply` 才激活（P164，<<<PAGE 1149>>>）
- **LDAP 策略服务器**：交换机按 `aaa ldap-server` 系列配置主机/端口/检索库/SSL，策略经 PolicyView 下发（P165，<<<PAGE 1175>>>）
- **SIP snooping**：配 trusted SIP server、RTCP 阈值，端口使能（<<<PAGE 704>>>）

## E（实证案例）
- 条件组复用（C52，<<<PAGE 1176>>>）
- ACL 安全策略+qos apply（C53，<<<PAGE 1142>>>）
- policy/端口两级带宽 policing（C54，<<<PAGE 1118>>>）

## B（反例/坑）
- policy 配置后不 `qos apply` 不生效——最常见的"配了没反应"（X60，<<<PAGE 1149>>>）
- LDAP/PolicyView 创建的 QoS 对象不能在 CLI 改，反之亦然（X61，<<<PAGE 1133>>>）
- IPv4 与 IPv6 条件不能组合进同一 condition；destination VLAN 条件仅组播规则可用；source ip+ARP 组合仅 OS6860/E 支持（X62/P163，<<<PAGE 1135>>>）
- 有效的规则也可能因依赖功能（如路由）未开而无法执行（X63，<<<PAGE 1134>>>）
- SIP Snooping 一揽子限制：仅 IPv4、仅 UDP（含 UDP/TCP），不支持 TLS/SCTP/MPLS、加密 RTCP/SDP、DNS/FQDN、无 VRF/NAT 感知（X65，<<<PAGE 704>>>）
- SIP 所有初始消息必须过同一 SIP Server，端到端直连会话不支持；电话侧 outbound proxy 必须与交换机 trusted call server 一致（X66，<<<PAGE 704>>>）
- 边缘口 SIP IP 与 RTP IP 不一致时 TCAM 表项不建、QoS 不生效；TCAM 装表前的早发媒体流得不到 QoS 待遇（X67/X68，<<<PAGE 704>>>）

## 来源
OmniSwitch AOS 8.10R4 Network Configuration Guide 第 20 章 SIP Snooping（<<<PAGE 704>>>）、第 33 章 QoS（<<<PAGE 1103-1176>>>）、第 34 章 Policy Servers（<<<PAGE 1175>>>）。条目来源：cases C52-C54；principles P156-P165；counter-examples X60-X68；frameworks F8。
