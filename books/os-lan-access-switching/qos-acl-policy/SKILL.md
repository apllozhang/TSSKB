---
name: qos-acl-policy
description: 何时用：在 OmniSwitch 上做流量优先级标记、限速、ACL 过滤、PBR 策略路由或策略镜像时。
source_book: DT00XTE215EN Access Switching
---

# QoS 与 ACL：统一策略引擎

## R · 原文引用

"policy condition client_traffic source vlan 20 / policy action priority_5 802.1p 5 / policy rule rule1 condition client_traffic action priority_5 / qos apply. A policy (or a policy rule) is made up of: 1. a condition 2. an action"（p317-328）

"By default, QoS is enabled on the switch... disposition Default: Accept. By default, the port default values for 802.1p and ToS/DSCP are 0... By default, switched ports are untrusted."（p318-326）

"The global setting is active immediately; however, modifying a port configuration requires qos apply to activate the change."（p346）

## I · 方法论骨架

AOS 的 QoS 与 ACL 共用一套三元组策略引擎：
- **condition**（匹配）：L1-L4——端口/MAC/VLAN/IP/ip-port/ip-protocol/DSCP/服务组等；可用 policy group（port/mac/network/service）复用。
- **action**（动作）：priority / maximum bandwidth / 802.1p 标记 / redirect / mirror / disposition（accept|drop|deny）等。
- **rule**（组装）：condition + action + 可选 precedence/log/count/trap；最后 **qos apply** 下发硬件。
- 默认值：QoS 默认启用；端口 802.1p/DSCP 默认 0、默认 untrusted（流量按 default 值重标）；未命中任何规则的流默认 accept。
- 出口调度：QSP 队列模板（QSP1=8 严格优先级、QSP2=1 EF+7SP）→ QSI 端口实例。
- 保留组 UserPorts / DropServices：用户口入组即防源 IP 欺骗 + 丢弃高危服务端口，免写规则。

## A1 · 书中案例（Lab 配置精要）

- **QoS Lab（p344-350）**：qos flush 复位 → `qos port 1/1/1 default 802.1p 7` 给未打标流量最高优先级 → `qos port 1/1/1 trusted` + qos apply（trusted 保留原标记）。策略限速：condition(source vlan 20) + action(802.1p 5 + maximum bandwidth 100k) + rule → qos apply → show active policy rule 看命中计数；大包 `ping -l 65000` 触发 TCM 三色丢弃（Red 包出现）。排障用 policy rule log + show qos log。
- **ACL Lab（p369-374）**：员工 VLAN20 禁 FTP、承包商 VLAN30 禁 HTTP。L2 拒绝：condition source mac + action disposition deny；FTP：condition `source vlan 20 destination ip-port 20-21 ip-protocol 6`；HTTP：5 条 policy service（80/8080/8000/443/4343）组成 service group 入条件。收尾：`policy port group Userports 1/1/1-2` 防源 IP 欺骗、`qos user-port shutdown bpdu` 使用户口收 STP 帧即关闭。

## A2 · 触发场景（含与相邻 skill 的区分）

- 限速、标记优先级、按 MAC/IP/协议/端口封流量、把流量引流到指定下一跳（PBR permanent gateway）——本 skill。
- 端口抓包/镜像（port-mirroring 抓物理口）→ poe-ops-diagnostics；按流量条件做镜像（RPM 策略镜像）在本 skill。
- IP 话机自动优先级（alaPhones）在本 skill；话机 VLAN/策略下发（LLDP-MED/UNP）→ access-guardian-unp。
- 按 VLAN 的基础转发/聚合 → vlan-link-redundancy。

## E · 可执行步骤

1. 清场：`qos flush`（清策略）/ `qos reset`（回默认）。
2. 端口级：`qos port <口> default 802.1p N`；trusted 口 `qos port <口> trusted`。
3. 策略三元组：
   - `policy condition <名> <匹配字段> <值>`
   - `policy action <名> <动作> [<参数>]`
   - `policy rule <名> condition <c> action <a> [precedence N] [log]`
4. **`qos apply`**（不 apply 不生效）。
5. 验证：`show active policy rule`（命中计数）/ `show qos log`。
6. ACL 化使用：action 加 `disposition drop|deny`；服务组 `policy service group <名> from cli <s1…s5>`。
7. 防欺骗加固：`policy port group UserPorts <口段>` + `qos user-port shutdown bpdu`。
8. PBR：action `permanent gateway ip <下一跳>`，条件加 source port 防回流环路。

## B · 边界与陷阱

- **不 qos apply 不生效**：端口级修改与所有 policy rule 都要 apply 才下发硬件；show active policy rule 里看不到 = 没 apply 或被 disable。
- 端口默认 untrusted：不 trusted 的口流量统一按 default 值（默认 0）重标，已有标记会被抹掉。
- IP 话机自动优先级默认开（alaPhones MAC 组给 priority 5），可用 qos no phones 关、qos phones priority N 改；与手工话机策略可能叠加，先确认。
- UserPorts 组的策略对路由流量自动生效，规划时别误伤上联口。
- PBR 仅 6570M/6860/6865/6900/9900 支持。
- 策略镜像（RPM）镜像 VLAN 内不许跑别的流量，控制包（LACP/LLDP/802.1x）不被镜像。

---
来源条目: f12, p37, p38, ce09, c12, c13, g28, g29, g30, g31, g32, g33
