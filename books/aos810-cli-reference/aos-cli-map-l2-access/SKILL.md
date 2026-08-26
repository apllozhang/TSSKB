---
name: AOS 8 CLI 命令地图——L2 接入域（端口/PoE/VLAN/聚合/VC/环网，第 1-8/12-17/20 章）
description: 需要在 OmniSwitch AOS 8 上配置端口物理参数、PoE 供电、VLAN/PVLAN/VLAN Stacking/MVRP、链路聚合、STP/环网保护、Virtual Chassis 时，用本地图定位 CLI Reference 对应章节与代表命令。含端口/PoE/VLAN/STP/聚合/VC/环网/MVRP 分域核心命令速查表（A3，90+ 条语法/默认值/示例/页码）。
source_book: OmniSwitch AOS Release 810R04 CLI Reference User Guide
---

## R（触发场景）
- 要查某条 L2/接入命令的完整语法、默认值、平台支持矩阵
- 不确定某配置属于哪一章，需要"域→章→命令"导航
- 端口违例恢复、PoE 分级、聚合哈希、VLAN 删除语义等关键默认值核对

## I（核心理念）
CLI Reference 是 6240 页命令字典，每条命令按"语法→参数→默认值→平台矩阵→用法指南→示例→Release History→相关命令→MIB Objects"固定结构展开；正确用法是先定位章（按本地图），再回书按页码查命令全文，不做通读。本域覆盖接入层命令：`interfaces`（30+ 子命令）、`lanpower`、`vlan`/`pvlan`、`linkagg`、`spanty`/`bridge`、`erp`/`mrp`、`virtual-chassis`。页码取 PDF 全文标记 `<<<PAGE N>>>`（第 1 章始于 <<<PAGE 67>>>，对应书内页 1-1）。

## A1（决策框架）
1. **物理层/端口参数**→第 1 章；**PoE 供电**→第 2 章；**UDLD**→第 3 章
2. **MAC 学习**→第 4 章；**VLAN/PVLAN**→第 5 章；**HA VLAN**→第 6 章；**QinQ**→第 7 章；**MVRP**→第 17 章
3. **环路防护**→第 8 章（STP）/第 12 章（LBD）；**聚合**→第 13 章；**环网**→第 15 章（ERP）/第 16 章（MRP）
4. **VC**→第 14 章；**自动织构**→第 20 章
5. 查到章后按章首页码进原书，用命令名检索条目

## A2（操作步骤）·章节清单与代表命令
- **Ch1 Ethernet Port（<<<PAGE 67>>>，约 85 条）**：`interfaces <port> speed|duplex|fec|break-out|eee|ddm`、`interfaces link-monitoring link-flap-threshold`、`violation`/`clear violation`；`show interfaces status/counters/counters errors/ddm`（P1/P2）
- **Ch2 PoE（<<<PAGE 254>>>，约 38 条）**：`lanpower slot port ...`（供电/预算/优先级/power rule）；802.3at 须先 `lanpower slot class-detection`，802.3bt（固件 3.xx）自动启用；power rule 先创建再绑定（P3/X7）；6465 不能自动检测电源类型，必须手工配置（P4/X9）
- **Ch3 UDLD（<<<PAGE 327>>>，约 12 条）**：`udld port ...` 单向链路检测
- **Ch4 Source Learning（<<<PAGE 351>>>，约 33 条）**：`mac-address-table` 学习/过滤/老化
- **Ch5 VLAN Management（<<<PAGE 427>>>，约 13 条）**：`vlan vlan_id [admin-state {enable|disable}] [name | prompt-on-deletion]`（默认 enable/disable）；`vlan 10-15` 区间写法；删除 VLAN 自动剥离成员、端口回落 VLAN 1（P5/P6）；`pvlan`/`pvlan secondary`/`pvlan mapping`（P7）
- **Ch6 HA VLAN（<<<PAGE 455>>>，约 10 条）**：跨机箱 VLAN 高可用同步
- **Ch7 VLAN Stacking（<<<PAGE 476>>>，约 40 条）**：`vlan stacking`（QinQ 双层标签/保留 VLAN/NNI-UNI 角色）；保留 VLAN 不能用标准 vlan 命令配（X18）
- **Ch8 Distributed Spanning Tree（<<<PAGE 567>>>，约 50 条）**：`spanty`/`bridge`
- **Ch12 Loopback Detection（<<<PAGE 1070>>>，约 11 条）**：`loopback-detection`
- **Ch13 Link Aggregation（<<<PAGE 1092>>>，约 46 条）**：`linkagg ...`（静态/LACP，动态仅兼容 IEEE 802.3ad）；`hash-control brief` 模式哈希退化为源 MAC（L2）/源 IP（L3）（P10/X16）；聚合不能配在 AppMon 已启用端口（X12）
- **Ch14 Virtual Chassis（<<<PAGE 1198>>>，约 32 条）**：`virtual-chassis`（VFL/chassis group）；chassis id 下次重启才生效（X10）；VC 只支持同型号两台（如 6860 与 6900 之间不支持）（X20）
- **Ch15 ERP（<<<PAGE 1268>>>，约 16 条）**：`erp`（ITU-T G.8032 环倒换）
- **Ch16 MRP（<<<PAGE 1306>>>，约 11 条）**：`mrp`（IEC 62439-2 工业环）
- **Ch17 MVRP（<<<PAGE 1340>>>，约 23 条）**：`mvrp`（802.1ak 动态 VLAN 注册）
- **Ch20 Automatic Fabric（<<<PAGE 1523>>>，约 12 条）**：`fabric`/`auto-fabric`

## A3（核心命令速查）

语法/默认值/示例均摘自原书第 1-8、12-17、20 章对应条目；页码为 fulltext `<<<PAGE N>>>` 标记值。`{enable | disable}` 表示"多选一"。

### 端口物理层（第 1 章）

| 命令 | 语法要点 | 关键参数与默认值 | 典型用法（一行示例） | 页码 |
|---|---|---|---|---|
| interfaces | `interfaces {slot chassis/slot \| port chassis/slot/port[-port2]} {autoneg {enable \| disable} ...}` | 端口/槽位级参数入口，支持端口区间 | `-> interfaces port 1/3/1 autoneg disable` | 70 |
| interfaces speed | `interfaces {slot ... \| port ...} speed {auto \| 10 \| 100 \| 1000 ...}` | 默认 auto | `-> interfaces port 1/3/1 speed 100` | 72 |
| interfaces duplex | `interfaces {slot ... \| port ...} duplex {full \| half \| auto}` | 默认 auto | `-> interfaces port 1/3/1 duplex auto` | 77 |
| interfaces max-frame-size | `interfaces {slot ... \| port ...} max-frame-size size` | size 1518-9216（依平台） | `-> interfaces port 1/3/1 max-frame-size 1518` | 83 |
| interfaces fec | `interfaces {slot ... \| port ...} fec {auto \| fc \| rs ...}` | 默认 auto | `-> interfaces port 1/1/1 fec fc` | 113 |
| interfaces break-out mode | `interfaces port chassis/slot/port break-out mode {4x100g \| 2x200g \| 2x100g-8 ...}` | 默认单口模式（None）；先 `break-out enable` | `-> interfaces port 1/1/1 break-out mode 4x100g` | 111 |
| interfaces pause | `interfaces {slot ... \| port ...} pause {tx \| rx \| tx-and-rx}` | 默认流控 disabled | `-> interfaces port 1/2/4 pause rx` | 93 |
| interfaces flood-limit | `interfaces {...} flood-limit {bcast \| uucast \| all} rate {mbps value \| cap% value} [low-threshold pct] [action {trap \| shutdown}]` | 广播/未知单播泛洪限速 | `-> interfaces port 1/1/1 flood-limit bcast rate mbps 60 low-threshold 40` | 87 |
| interfaces link-monitoring link-flap-threshold | `interfaces {...} link-monitoring link-flap-threshold count` | 默认 5 次；time-window 默认 300 秒 | `-> interfaces port 1/1/1 link-monitoring link-flap-threshold 3` | 177 |
| interfaces ddm | `interfaces ddm {enable \| disable}` | 光模块数字诊断 | `-> interfaces ddm enable` | 97 |
| violation recovery-time | `violation [slot ... \| port ...] recovery-time seconds` | 全局默认 300 秒 | `-> violation recovery-time 600` | 127 |
| clear violation | `clear violation {port chassis/slot/port[-port2] \| linkagg id}` | 清除违例记录使端口恢复 | `-> clear violation port 1/1/10` | 123 |
| show interfaces status | `show interfaces [slot ... \| port ...] status` | 端口状态首查 | `-> show interfaces status` | 138 |
| show interfaces counters errors | `show interfaces [port ...] counters errors` | 错误计数排障 | `-> show interfaces port 1/2/1 counters errors` | 148 |
| show interfaces ddm | `show interfaces [port ...] ddm [w-low \| w-high \| a-low \| a-high \| status]` | 光功率阈值/状态 | `-> show interfaces ddm status` | 156 |
| show transceivers | `show transceivers [slot chassis/slot [transceiver num]]` | 光模块信息 | `-> show transceivers` | 163 |

### PoE 供电（第 2 章）

| 命令 | 语法要点 | 关键参数与默认值 | 典型用法（一行示例） | 页码 |
|---|---|---|---|---|
| lanpower service | `lanpower {chassis id \| slot c/s} service {start \| stop}` | PoE 全局默认 disabled | `-> lanpower slot 2/1 service start` | 256 |
| lanpower port admin-state | `lanpower port chassis/slot/port admin-state {enable \| disable}` | 端口级供电开关 | `-> lanpower port 2/1/1 admin-state enable` | 258 |
| lanpower power | `lanpower {chassis id \| slot c/s \| port c/s/p} power milliwatts` | 预算默认见硬件手册 | `-> lanpower port 1/1/24 power 25000` | 259 |
| lanpower priority | `lanpower {chassis \| slot \| port ...} priority {low \| high \| critical}` | 断电抢占优先级 | `-> lanpower port 1/1/6 priority critical` | 264 |
| lanpower class-detection | `lanpower {chassis id \| slot c/s} class-detection {enable \| disable}` | 802.3at 必须先启用（X7）；802.3bt 自动启用 | `-> lanpower slot 1/1 class-detection enable` | 275 |
| lanpower power-rule | `lanpower power-rule name [admin-state {enable \| disable}] power {on \| off} at {time hh:mm \| minutes n} days ... [timezone utc]`，`no` 删除 | 定时供电规则；先创建后绑定 | `-> lanpower power-rule RuleTest2 admin-state enable power on at minutes 10 days fri` | 270 |
| lanpower power-policy | `lanpower [slot c/s \| port c/s/p] power-policy name`，`no` 解除 | 将规则编成策略绑定对象 | `-> lanpower port 1/1/23 power-policy NewPolicy` | 273 |
| lanpower usage-threshold | `lanpower {chassis \| slot ...} usage-threshold pct` | 功耗告警阈值 | `-> lanpower slot 1/1 usage-threshold 50` | 279 |
| lanpower 802.3bt / 4pair | `lanpower {slot c/s \| port c/s/p} {802.3bt \| 4pair} {enable \| disable}` | bt 供电（固件 3.xx 自动启用） | `-> lanpower slot 1/1 802.3bt enable` | 289 |
| lanpower port reset | `lanpower port chassis/slot/port reset` | 端口供电复位 | `-> lanpower port 1/1/1 reset` | 301 |
| show lanpower | `show lanpower {slot c/s [port-config] ...}` | 供电总览 | `-> show lanpower slot 1/1` | 307 |
| show lanpower status | `show lanpower slot chassis/slot status` | 各端口 PD 状态 | `-> show lanpower slot 1/1 status` | 325 |

### UDLD / MAC 学习（第 3-4 章）

| 命令 | 语法要点 | 关键参数与默认值 | 典型用法（一行示例） | 页码 |
|---|---|---|---|---|
| udld | `udld {enable \| disable}` | 单向链路检测全局开关 | `-> udld enable` | 328 |
| udld port | `udld port chassis/slot/port[-port2] {enable \| disable}` | 端口级启用 | `-> udld port 1/1/3 enable` | 330 |
| udld mode | `udld [port ...] mode {normal \| aggressive}` | aggressive 状态机更严格 | `-> udld mode aggressive` | 332 |
| udld probe-timer / echo-wait-timer | `udld [port ...] {probe-timer \| echo-wait-timer} seconds`，`no` 恢复默认 | 探测/等待计时器 | `-> udld probe-timer 20` | 334/336 |
| show udld status port | `show udld status port [chassis/slot/port]` | 默认列出全部端口 | `-> show udld status port` | 348 |
| mac-learning | `mac-learning {vlan vlan[-vlan2] \| port ... \| linkagg id} {enable \| disable}` | 按域关闭源学习 | `-> mac-learning vlan 10 disable` | 353 |
| mac-learning aging-time | `mac-learning aging-time {seconds \| default}`，`no` 恢复 | 默认 300 秒 | `-> mac-learning aging-time 1200` | 389 |
| mac-learning static mac-address | `mac-learning vlan vlan_id port c/s/p static mac-address mac {bridging \| filtering}` | 静态桥接/过滤表项 | `-> mac-learning vlan 10 port 1/1/10 static mac-address 00:00:39:59:f1:0c bridging` | 373 |
| mac-learning flush | `mac-learning flush {dynamic \| static} [mac-address mac]`；domain 子域 all/vlan/spb/vxlan/l2gre/local/vpls/evpn-vxlan 可选 | 清除动态/静态 MAC | `-> mac-learning flush dynamic` | 355 |
| show mac-learning | `show mac-learning [summary]`；domain 子域同上 | 默认全部表项 | `-> show mac-learning domain vlan summary` | 392 |
| mac-ping | `mac-ping dst-mac mac vlan vlan_id [count n] [size n] [isid-check id]` | L2 连通性探测 | `-> mac-ping dst-mac 00:11:11:11:11:11 vlan 10` | 424 |

### VLAN / PVLAN（第 5 章）

| 命令 | 语法要点 | 关键参数与默认值 | 典型用法（一行示例） | 页码 |
|---|---|---|---|---|
| vlan | `vlan vlan_id [admin-state {enable \| disable}] [name desc] [prompt-on-deletion {enable \| disable}]`，`no vlan vlan_id` | 默认 enable；prompt-on-deletion 默认 disable（删 VLAN 不弹确认，X22）；支持区间 `vlan 10-15` | `-> vlan 200 name "Corporate VLAN"` | 428 |
| vlan members tagged/untagged | `vlan vlan_id[-id2] members {port c/s/p[-p2] \| linkagg id[-id2]} {tagged \| untagged}`，`no` 移除 | VLAN 1 为全部端口默认 untagged VLAN | `-> vlan 20 members port 1/1/1-24 tagged` | 430/432 |
| vlan mtu-ip | `vlan vlan_id mtu-ip size` | 默认 1500 字节 | `-> vlan 200 mtu-ip 9198` | 434 |
| show vlan / members | `show vlan [vlan_id]` / `show vlan [id] members [port ...]` | 默认全部 | `-> show vlan members` | 436/439 |
| pvlan | `pvlan vlan_id[-id2] [admin-state ...] [name ...]`，`no` 删除 | 主 PVLAN | `-> pvlan 200 name "Corporate PVLAN"` | 442 |
| pvlan secondary | `pvlan vlan_id secondary vlan_id[-id2] type {isolated \| community}` | 从 VLAN 类型 | `-> pvlan 200 secondary 250 type isolated` | 444 |
| pvlan members | `pvlan vlan_id members {port ... \| linkagg ...} {tagged \| untagged} [isl]` | — | `-> pvlan 200 members port 1/1/1-5 tagged` | 446 |
| show pvlan / mapping | `show pvlan [vlan_id]` / `show pvlan [id] mapping` | 默认全部 | `-> show pvlan mapping` | 448-450 |

### VLAN Stacking / QinQ（第 7 章）

| 命令 | 语法要点 | 关键参数与默认值 | 典型用法（一行示例） | 页码 |
|---|---|---|---|---|
| ethernet-service svlan | `ethernet-service svlan {svlan_id[-id2]} [admin-state {enable \| disable}] [name desc]`，`no` 删除 | 服务商 VLAN；平台 6360/6920 为 No | `-> ethernet-service svlan 1001-1005 admin-state enable name "Customer ABC"` | 478 |
| ethernet-service nni | `ethernet-service nni {port ... \| linkagg ...} [tpid tpid_value] [[stp \| mvrp] legacy-bpdu {enable \| disable}]`，`no` 撤销 | NNI 口；非 0x8100 TPID 配后不可改（X18） | `-> ethernet-service nni port 1/1/1 tpid 0x9100` | 482 |
| ethernet-service sap | `ethernet-service sap sap_id service-name service_name`，`no ethernet-service sap sap_id` | 创建即关联 default-sap-profile | `-> ethernet-service sap 10 service-name CustomerA` | 487 |
| ethernet-service uni-profile | `ethernet-service uni-profile name [bandwidth ...] [priority ...] [protocol 动作] ...`，`no` 删除 | 协议动作 peer/discard/tunnel/mac-tunnel（stp 默认 tunnel 等，见原书表）；sap-profile 默认 shared、0 Mbps、preserve、fixed 0 | `-> ethernet-service uni-profile ...`（详见原书 7-23） | 498 |
| ethernet-service mac-tunneling | `ethernet-service mac-tunneling {enable \| disable}` | 默认 enable；全局改动需重启生效；默认隧道 MAC 01:00:0C:CD:CD:D0 | `-> ethernet-service mac-tunneling enable` | 512 |
| show ethernet-service | `show ethernet-service [svlan ...]` | SVLAN/NNI/UNI/SAP 全套子命令（sap/nni/uni/port/uni-profile/mac-tunneling） | `-> show ethernet-service sap` | 522+ |

### 分布式生成树 STP（第 8 章）

| 命令 | 语法要点 | 关键参数与默认值 | 典型用法（一行示例） | 页码 |
|---|---|---|---|---|
| spantree mode | `spantree mode {flat \| per-vlan}` | 默认 per-vlan | `-> spantree mode flat` | 569 |
| spantree protocol | `spantree [cist \| vlan vlan_id] protocol {stp \| rstp \| mstp}` | 默认 RSTP | `-> spantree protocol mstp` | 571 |
| spantree priority | `spantree [cist \| msti id \| vlan id] priority priority` | 桥优先级默认 32768；端口优先级默认 7 | `-> spantree priority 8192` | 585 |
| spantree hello-time / max-age / forward-delay | `spantree [cist \| vlan id] {hello-time \| max-age \| forward-delay} seconds` | hello=2、max-age=20、forward-delay=15 | `-> spantree max-age 10` | 588-592 |
| spantree mst region | `spantree mst region {name n \| revision-level n \| max-hops n}` | name 默认空、revision 0、max-hops 20 | `-> spantree mst region name SalesRegion` | 575 |
| spantree msti vlan | `spantree msti msti_id vlan vlan_id[-id2]`，`no` 移除 | 默认全部 VLAN 属 MSTI 0（CIST） | `-> spantree msti 10 vlan 100-115` | 583 |
| spantree cist / vlan（端口级） | `spantree {cist \| vlan id} {port ... \| linkagg ...} {enable \| disable}` | 默认 eligible 端口启用 | `-> spantree cist port 1/4/1 enable` | 602/604 |
| spantree path-cost | `spantree {cist \| msti id \| vlan id} {port ... \| linkagg ...} path-cost cost` | 默认 0（自动） | `-> spantree cist port 1/4/1 path-cost 19` | 606-610 |
| spantree admin-edge / auto-edge | `spantree {cist \| vlan id} {port ... \| linkagg ...} {admin-edge \| auto-edge} {enable \| disable}` | admin-edge 默认 off；auto-edge 默认 on | `-> spantree cist linkagg 15 admin-edge enable` | 622/626 |
| spantree loop-guard | `spantree {port ... \| linkagg ...} loop-guard {enable \| disable}` | 默认 disabled | `-> spantree port 1/1/2 loop-guard enable` | 614 |
| show spantree | `show spantree`；子命令 cist/msti/vlan/ports/mst/mode/map-msti | 拓扑首查 | `-> show spantree vlan 200` | 642-687 |

### 链路聚合 LACP/DHL（第 13 章）

| 命令 | 语法要点 | 关键参数与默认值 | 典型用法（一行示例） | 页码 |
|---|---|---|---|---|
| linkagg static agg | `linkagg static agg agg_id[-id2] size size [name n] [admin-state ...] [hash ...]`，`no` 删除 | 静态聚合；size 为成员端口上限 | `-> linkagg static agg 4 size 2` | 1094 |
| linkagg static port agg | `linkagg static port chassis/slot/port[-port2] agg agg_id`，`no` 移除 | — | `-> linkagg static port 1/2/1-5 agg 4` | 1107 |
| linkagg lacp agg | `linkagg lacp agg agg_id[-id2] size size [name n] [admin-state ...] [actor ...]`，`no` 删除 | 动态 LACP 聚合（IEEE 802.3ad） | `-> linkagg lacp agg 2-5 size 4` | 1109 |
| linkagg lacp agg actor system-priority | `linkagg lacp agg agg_id actor system-priority value`，`no` 恢复 | LACP 系统 ID 仲裁 | `-> linkagg lacp agg 3 actor system-priority 100` | 1120 |
| linkagg lacp agg pre-empt / timer | `linkagg lacp agg agg_id pre-empt {enable \| disable} [timer seconds]` | timer 默认 30 秒 | `-> linkagg lacp agg 2 pre-empt enable` | 1157/1159 |
| linkagg lacp port actor admin-state | `linkagg lacp port c/s/p actor admin-state {[active] [timeout] [aggregate] [synchronize] [collect] [distribute] \| none}` | LACP 端口状态位 | `-> linkagg lacp port 1/4/2 actor admin-state synchronize collect distribute` | 1133 |
| dhl | `dhl dhl_num linka {port c/s/p \| linkagg id} linkb {port c/s/p \| linkagg id}`；`dhl dhl_num admin-state {enable \| disable}` | 双主链路；每机箱仅 1 个 DHL 会话、2 条链路 | `-> dhl 1 linka port 1/1/1 linkb port 1/1/2` | 1161-1165 |
| show linkagg | `show linkagg [agg agg_id[-id2]] [port ...]`；另有 accounting/counters/traffic | 默认全部聚合组 | `-> show linkagg port` | 1178 |
| clear linkagg-statistics | `clear linkagg-statistics [agg agg_id[-id2]]` | 默认清全部 | `-> clear linkagg-statistics agg 10` | 1196 |

### Virtual Chassis（第 14 章）

| 命令 | 语法要点 | 关键参数与默认值 | 典型用法（一行示例） | 页码 |
|---|---|---|---|---|
| virtual-chassis configured-chassis-id | `virtual-chassis [chassis-id oper] configured-chassis-id id`，`no` 撤销 | chassis id 下次重启生效（X10） | `-> virtual-chassis configured-chassis-id 1` | 1200 |
| virtual-chassis chassis-group | `virtual-chassis [chassis-id oper] chassis-group group` | VC 只支持同型号两台（X20） | `-> virtual-chassis chassis-id 1 chassis-group 10` | 1202 |
| virtual-chassis vf-link create / member-port | `virtual-chassis [chassis-id oper] vf-link vfl_id create` + `vf-link vfl_id member-port slot/port`，`no` 删除 | VFL 成员口 | `-> virtual-chassis vf-link 1 create` | 1210 |
| virtual-chassis split-protection | `virtual-chassis split-protection {admin-state {enable \| disable} \| linkagg agg_id \| guard-timer t}` | 双活保护 | `-> virtual-chassis split-protection admin-state enable` | 1252 |
| show virtual-chassis topology | `show virtual-chassis [chassis-id id] topology`；另有 consistency/vf-link/neighbors/split-protection | VC 拓扑首查 | `-> show virtual-chassis topology` | 1231 |
| vc-takeover / ssh-chassis | `vc-takeover` / `ssh-chassis [user@chassis-id]` | VC 内主备切换/跨机箱登录 | `-> ssh-chassis guest@2` | 1225/1227 |

### 环网 ERP / MRP（第 15-16 章）

| 命令 | 语法要点 | 关键参数与默认值 | 典型用法（一行示例） | 页码 |
|---|---|---|---|---|
| erp-ring | `erp-ring ring_id port1 {c/s/p \| linkagg} port2 {...} service-vlan vlan level {0-7} [enable]`，`no` 删除 | G.8032 主环；创建时默认 disabled | `-> erp-ring 1 port1 1/1/1 port2 2/4/1 service-vlan 10 level 2 enable` | 1269 |
| erp-ring rpl-node | `erp-ring ring_id rpl-node {port c/s/p \| linkagg id}`，`no` 撤销 | RPL 拥塞节点每环一个 | `-> erp-ring 1 rpl-node port 1/2/1` | 1273 |
| erp-ring wait-to-restore / guard-timer | `erp-ring ring_id {wait-to-restore min \| guard-timer sec}`，`no` 恢复 | WTR 默认 5 分钟 | `-> erp-ring 1 wait-to-restore 6` | 1275/1279 |
| erp-ring revertive / clear | `erp-ring ring_id revertive {enable \| disable}` / `erp-ring ring_id clear` | 回切模式/清状态 | `-> erp-ring 1 clear` | 1286/1288 |
| show erp / statistics | `show erp [ring id [port ...]]` / `show erp statistics [...]`；`clear erp statistics` | 默认全部环 | `-> show erp statistics ring 5` | 1296-1298 |
| mrp domain | `mrp domain domain_index [name n] [uuid u] port1 {...} port2 {...} [admin-role {manager \| client}] [recovery-time ...]`，`no` 删除 | IEC 62439-2 工业环 | `-> mrp domain 1 vlan 10` | 1309 |
| show mrp | `show mrp [domain ... [detail \| counters \| elected-manager]]`；另有 port/interconnect 子命令；`clear mrp ... counters` | — | `-> show mrp domain counters` | 1317-1334 |

### MVRP / 环回检测 / 自动织构（第 17/12/20 章）

| 命令 | 语法要点 | 关键参数与默认值 | 典型用法（一行示例） | 页码 |
|---|---|---|---|---|
| mvrp | `mvrp {enable \| disable}` | 全局默认 disabled | `-> mvrp enable` | 1341 |
| mvrp port / linkagg | `mvrp {port c/s/p[-p2] \| linkagg id[-id2]} {enable \| disable}` | 端口级默认 disabled | `-> mvrp port 1/1/2 enable` | 1343 |
| mvrp maximum-vlan | `mvrp maximum-vlan vlan_limit` | 默认 256 | `-> mvrp maximum-vlan 100` | 1347 |
| mvrp registration | `mvrp {port ... \| linkagg ...} registration {normal \| fixed \| forbidden}` | 注册模式 | `-> mvrp port 1/1/5 registration normal` | 1349 |
| mvrp timer | `mvrp {port ... \| linkagg ...} timer {join ms \| leave ms \| leaveall ms \| periodic-timer s}` | 计时器组 | `-> mvrp port 1/1/2 timer join 600` | 1353-1359 |
| show mvrp | `show mvrp {configuration \| port ... \| timer \| statistics \| last-pdu-origin ...}`；`mvrp clear-statistics` | — | `-> show mvrp port 1/1/1 statistics` | 1369-1387 |
| loopback-detection | `loopback-detection [remote-origin] {enable \| disable}`；`loopback-detection port c/s/p[-p2] [remote-origin] {enable \| disable}` | 全局/端口级 LBD | `-> loopback-detection enable` | 1071 |
| loopback-detection transmission-timer / autorecovery-timer | `loopback-detection {transmission-timer \| autorecovery-timer} seconds` | 发送/自恢复计时 | `-> loopback-detection transmission-timer 35` | 1077/1079 |
| show loopback-detection | `show loopback-detection [port ...]`；另有 linkagg/statistics port 子命令 | 默认显示全局 LBD 配置 | `-> show loopback-detection port` | 1081-1088 |
| auto-fabric admin-state / discovery | `auto-fabric admin-state {enable \| disable}` / `auto-fabric discovery start` | 自动织构开关与手动发现 | `-> auto-fabric admin-state enable` | 1524/1528 |
| auto-fabric protocols | `auto-fabric protocols {lacp \| mvrp \| spb \| loopback-detection \| ip ospfv2/ospfv3/isis ...} admin-state ...` | 按协议启停并套默认模板 | `-> auto-fabric protocols spb default-profile single-service` | 1529 |
| show auto-fabric config | `show auto-fabric config [interface ...]` | 织构配置总览 | `-> show auto-fabric config` | 1542 |

## E（实证案例）
- 本系列为命令地图型 skill，不搬运配置案例；原书每条命令自带 Example 小节，定位到章后按页码回查即可（cases 原件未创建，E 段说明见书报告）

## B（反例/坑）
- 802.3at 供电必须先 `lanpower slot class-detection` 启用分级检测；802.3bt 下自动启用、手工命令不受支持（X7）
- 6465 不能自动检测电源类型，不手工配置则系统与 PoE 功率信息显示错误（X9）
- 默认删除带成员端口的 VLAN 不弹确认——误删风险由 prompt-on-deletion 兜底，默认 disable（X22，<<<PAGE 428>>>）
- VLAN Stacking 保留 VLAN 不可用标准 vlan 命令配置；NNI 口成为 stacking 口后 TPID（非 0x8100 时）不可再改（X18）
- legacy BPDU 仅 flat STP 模式支持，且只应在连 legacy 设备的 Stacking 网络端口启用（X19）
- VC 只支持同型号两台；`no virtual-chassis` 仅在无任何 VFL 配置时可用（X20）
- UNP 动态创建的 VLAN 不能用标准 `no vlan vlan_id` 删除（X15，第 42 章，详见 aos-cli-map-mgmt-oam 域说明）
- chassis identifier 到目标机箱下次重启才生效（X10）

## 来源
OmniSwitch AOS Release 810R04 CLI Reference User Guide 第 1-8、12-17、20 章（<<<PAGE 67-689、1070-1390、1523-1549>>>）。条目来源：principles P1-P7/P10；counter-examples X7/X9/X10/X12/X15/X16/X18-X20/X22；frameworks F1-F3/F5（域分组）。
