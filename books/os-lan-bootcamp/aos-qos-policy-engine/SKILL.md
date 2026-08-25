---
name: QoS 策略引擎（分类/标记/限速/ACL/SIP Snooping）
description: 需要配置 OmniSwitch QoS 队列调度（SP/WRR/WFQ）、策略三元组（condition/action/rule）做标记限速、ACL 过滤（L2/L3/白名单）、Auto-QoS 话机信任或 SIP Snooping 自动语音 QoS 时使用本技能。
source_book: DT00CTE120 OmniSwitch R6/R8 Bootcamp Issue 25
---

## R（触发场景）
- 语音/关键业务流量需要队列优先或带宽保障
- 按流标记 802.1p/DSCP、限速或重定向
- ACL 需求：L2 拒绝主机、L3 网段拒绝、白名单式内部防火墙
- 话机信任（Auto-QoS）或 SIP 信令自动识别 RTP 流
- 排查"配了 QoS 反而全网断"类事故

## I（核心理念）
AOS 的 QoS 与 ACL 是同一套策略引擎：解析器之后硬件分类引擎按 L2-L4 条件匹配，策略三元组 Condition+Action+Rule（可选生效时段）执行标记/限速/重定向/镜像（P105/P106/P107，<<<PAGE 542-545>>>）。R8 的队列模型分层为 QSet（每口 8 单播+4 组播队列）→ QSI 实例 → QSet Profile（8SP / 1EF+7SP / 1EF+7WFQ）（P109/F8，<<<PAGE 548-552>>>）。两条默认值是事故之源：未匹配流量默认全 accept（配 deny 后全断）、交换端口默认不信任任何标记（P112/P117，<<<PAGE 581-590, 610-618>>>）。信任要显式给：`qos phones trusted`/`qos nms priority` 或端口级信任（P112，<<<PAGE 581-590>>>）。

## A1（决策/选型）
1. R6 调度三算法：Strict Priority（低队列饿死风险）/ WRR（1-15 包，0=严格）/ DRR（按体量 1=10KB）（P108，<<<PAGE 547>>>）
2. R8 用 QSet Profile 选 8SP / 1EF+7SP（EF 带限速保护）/ 1EF+7WFQ（P109，<<<PAGE 548-552>>>）
3. ACL 即 QoS 子集：整机全局、仅入方向、L1-L4 硬件过滤、precedence 0-65535 大者先（P115/P116，<<<PAGE 607>>>）
4. 黑名单（全局 accept + deny 规则）vs 白名单（全局 deny + 精确 accept，内部防火墙范式）（P119，<<<PAGE 614>>>）
5. 策略组复用：network/mac/service/port group 供多条件复用（P110，<<<PAGE 569>>>）

## A2（操作步骤）
1. 队列观察与调度：`qos port 1/1 monitor` → `show qos queue 1/9` → `qos stats reset egress`；调度 `qos port <slot/port> servicing mode wrr` 或 `qos default servicing mode wrr`（C26，<<<PAGE 547, 578>>>）
2. 标记策略：`policy condition Traffic destination port 3/2 802.1p 4` → `policy action SetBits 802.1p 7` → `policy rule Rule2 condition Traffic action SetBits`；L3 版 `policy condition cond3 source ip 10.10.2.3` + `policy action action2 priority 7`；验证 `show active policy rules`、`show policy classify l3 …`；管理 `qos reset` 清空（C27，<<<PAGE 574-593>>>）
3. Egress 策略列表（R8）：`policy list eggress1 type egress rules rule1 rule2 rule3`（C28/P111，<<<PAGE 575>>>）
4. Auto-QoS：`policy mac group alaPhones` → `qos phones [priority|trusted]` → `qos nms priority`（C29，<<<PAGE 581-582>>>）
5. L2 拒绝主机：`qos default bridged disposition accept` → `policy condition Cond-Deny-Host1 source mac D4:85:64:EC:33:EF source vlan 5` → `policy action Act-deny-Host1 disposition deny` → `policy rule Rule-Deny-Host1 … log` → `qos apply`；`show qos log` 看命中（C30，<<<PAGE 612>>>）
6. L3 白名单：`qos default routed disposition deny` + 两条精确 accept 规则（allow-host1 / subnet-100）→ `qos apply`（C31，<<<PAGE 613-614>>>）；黑名单用 `policy network group netgroup1 192.168.82.0 mask 255.255.255.0 …` + deny + `precedence 65535`（C31，<<<PAGE 613-614>>>）
7. 服务组批量过滤：`policy service telnet1 protocol 6 destination ip port 23`、`policy service group tel-ftp telnet1 ftp1`、`policy port group visitor_ports 2/1 3/1-24`；调序 `policy rule telnet_rule precedence 1000 …`（C32，<<<PAGE 621-622>>>）
8. established 回程放行：检查 ACK/RST 位放行已建 TCP 连接（P118，<<<PAGE 615>>>）
9. SIP Snooping：硬件侦听 SIP 信令动态学习话机 RTP 流自动加 QoS；默认转发的 SIP 包不受策略（P113，<<<PAGE 601>>>）

## E（实证案例）
- C27 标记与限速策略：L2 802.1p 重标 + L3 源 IP 优先（<<<PAGE 574-593>>>）
- C31 白名单式 L3 ACL：全局 deny + 精确 accept（<<<PAGE 613-614>>>）
- C30 L2 拒绝主机 + qos log 命中验证（<<<PAGE 612>>>）

## B（反例与坑）
- QoS 默认放行一切未匹配流量；一旦把默认 disposition 配成 deny，未匹配流量全断（X55，<<<PAGE 558, 586, 620>>>）
- `qos phones/nms` 信任仅支持按 ifIndex 顺序的前 8 个接口（X56，<<<PAGE 582>>>）
- condition/action 被规则引用时不可删；部分 action 参数只与特定 condition 参数兼容（X57/P114，<<<PAGE 593-594>>>）
- 交换端口默认不信任标记——不显式配信任，终端自带 802.1p/DSCP 会被清零（X58，<<<PAGE 590, 598>>>）
- Egress 过滤仅限特定平台/方向（X59/P111，<<<PAGE 575>>>）
- 严格优先级下低队列有饿死（Starvation）风险，EF 队列配限速保护（<<<PAGE 550-552>>>）

## 来源
- principles·P105-P119；frameworks·F8；cases·C26-C32；counter-examples·X55-X59
