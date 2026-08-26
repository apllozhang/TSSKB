---
name: AOS 8 CLI 命令地图——组播/QoS/策略/准入域（组播/QoS/Policy Server/AAA/AG/AppMon，第 33-44/49/58 章）
description: 需要在 OmniSwitch AOS 8 上配置组播交换与路由（IPMS/MVR/PIM/DVMRP）、QoS 队列与策略（policy condition/action/rule/list）、AAA、Access Guardian/UNP、LPS、PPPoE-IA 时，用本地图定位 CLI Reference 对应章节与代表命令。含组播/QoS 策略/AAA/UNP 分域核心命令速查表（A3，60+ 条语法/默认值/示例/页码）。
source_book: OmniSwitch AOS Release 810R04 CLI Reference User Guide
---

## R（触发场景）
- 查组播命令（ip igmp/ip pim/ip dvmrp/mvr/mcs）或 QoS 策略命令语法
- 写 QoS 策略：policy condition/action/rule/list 四级模型与 group 复用
- 部署准入：AAA、Access Guardian/UNP、Captive Portal、LPS、PPPoE-IA
- 策略经 PolicyView 创建后 CLI 改不动——优先级与只读规则核对

## I（核心理念）
策略模型（P23，<<<PAGE 3953>>>）：policy rule = policy condition + policy action；rule 编入 policy list 后生效；策略可经 CLI/SNMP/PolicyView（LDAP 端 GUI）三种途径创建。Access Guardian 架构（P29，<<<PAGE 4470>>>）：UNP（Universal Network Profile）为统一框架——端口使能 UNP 后对用户认证/分类进 profile，profile 映射 VLAN 或 SAP；组件含 BYOD（UPAM/ClearPass，含 mDNS/SSDP GRE 隧道）、Captive Portal、QMR、IoT Device Profiling；199 条为全书最大命令章。组播分层（F7）：三层组播（PIM/DVMRP/IGMP）与二层组播交换（MCS/MVR）分层。QoS 双章分工（P28）：第 38 章管硬件队列/调度/端口参数，第 39 章管策略软件模型。

## A1（决策框架）
1. **二层组播**→ 第 33 章（IPMS/MCS，106 条）/第 34 章（MVR）
2. **三层组播**→ 第 35 章 DVMRP /第 36 章 PIM /第 37 章 Multicast Routing
3. **QoS**→ 硬件队列第 38 章；策略模型第 39 章；Policy Server 第 40 章
4. **准入**→ AAA 第 41 章；Access Guardian/UNP 第 42 章；LPS 第 49 章；PPPoE-IA 第 58 章
5. **应用识别**→ 第 43 章 AppMon /第 44 章 Application Fingerprinting

## A2（操作步骤）·章节清单与代表命令
- **Ch33 IP Multicast Switching（<<<PAGE 3227>>>，约 106 条）**：`ip ms`/`ip igmp`（IGMP 侦听/MCS 二层组播交换）
- **Ch34 IP Multicast VLAN（<<<PAGE 3471>>>，约 12 条）**：`mvr`（组播 VLAN 业务通道）
- **Ch35 DVMRP（<<<PAGE 3495>>>，约 23 条）**：`ip dvmrp`
- **Ch36 PIM（<<<PAGE 3542>>>，约 99 条）**：`ip pim`（PIM-SM/SSM/DM）
- **Ch37 Multicast Routing（<<<PAGE 3769>>>，约 14 条）**：组播路由全局/边界/静态
- **Ch38 QoS（<<<PAGE 3797>>>，约 70 条）**：硬件队列/调度/端口 QoS 参数（P28）
- **Ch39 QoS Policy（<<<PAGE 3953>>>，约 111 条）**：`policy condition`（40+ 子命令：ip/ipv6/ip-port/tcp-port/udp-port/ethertype/tcpflags/service/icmp/tos/dscp/mac/vlan/802.1p/port/vrf/fragments/app-mon 等，inner 前缀支持 QinQ 内层字段）（P25）；`policy action`（disposition accept/drop/deny、cir+cbs/pir/pbs、802.1p/dscp 改写、redirect、mirror、port-disable 等）（P26）；`policy rule` 绑 condition+action；`policy list` 编排；`policy network/mac/port/vlan/map/service group` 成组复用（P27）
- **Ch40 Policy Server（<<<PAGE 4190>>>，约 9 条）**：LDAP 端 PolicyView 联动
- **Ch41 AAA（<<<PAGE 4205>>>，约 119 条）**：`aaa`/`radius`/`tacacs`（服务器组与认证方法链，为 AG 提供底座）（P31）
- **Ch42 Access Guardian（<<<PAGE 4470>>>，约 199 条）**：`unp` 全局配置（dynamic-vlan-configuration、auth-server-down、redirect 族、mac-mobility 等）与 profile 配置（trust-tagged-vlans、qos-policy-list、captive-portal 等），另加 port/domain/user/show 组（P29/P30）
- **Ch43 AppMon（<<<PAGE 4934>>>，约 37 条）**：应用识别与流量管控
- **Ch44 Application Fingerprinting（<<<PAGE 5016>>>，约 12 条）**：应用指纹库管理
- **Ch49 LPS（<<<PAGE 5212>>>，约 18 条）**：`lps`（学习型端口安全）
- **Ch58 PPPoE Intermediate Agent（<<<PAGE 5571>>>，约 12 条）**：`pppoe ia`

## A3（核心命令速查）

语法/默认值/示例均摘自原书第 33-44、49、58 章对应条目；页码为 fulltext `<<<PAGE N>>>` 标记值。`{enable | disable}` 表示"多选一"。

### 二层组播交换 IPMS（第 33 章）

| 命令 | 语法要点 | 关键参数与默认值 | 典型用法（一行示例） | 页码 |
|---|---|---|---|---|
| ip multicast admin-state | `ip multicast [vlan vlan_id[-id2] \| service service_id[-id2]] admin-state {enable \| disable}` | VLAN/服务或全局启用 IPMS | `-> ip multicast vlan 10 admin-state enable` | 3229 |
| ip multicast querying | `ip multicast [vlan ...] querying {enable \| disable}` | IGMP 查询器开关 | `-> ip multicast vlan 10 querying enable` | 3260 |
| ip multicast query-interval | `ip multicast [vlan ...] query-interval seconds` | 查询间隔（默认见原书表） | `-> ip multicast vlan 10 query-interval 125` | 3248 |
| ip multicast robustness | `ip multicast [vlan ...] robustness value` | 健壮性系数 | `-> ip multicast vlan 10 robustness 2` | 3262 |
| ip multicast router-timeout | `ip multicast [vlan ...] router-timeout seconds` | 路由器端口老化 | `-> ip multicast vlan 10 router-timeout 300` | 3256 |
| ip multicast fast-join / zapping | `ip multicast [vlan ...] {fast-join ... \| zapping ...}` | 快速加入/快速换台优化 | `-> ip multicast vlan 10 fast-join` | 3282/3268 |
| ip multicast static-group / static-querier / static-neighbor | `ip multicast [vlan ...] static-group ip_address [port ...]` 等 | 静态组/查询器/邻居 | `-> ip multicast vlan 10 static-group 239.1.1.1` | 3246/3244/3242 |
| ip multicast spoofing | `ip multicast [vlan ...] spoofing {enable \| disable}`；`static-source-ip` 变体 | 源欺骗防护 | `-> ip multicast vlan 10 spoofing enable` | 3264 |
| ip multicast profile / apply-profile | `ip multicast [vlan ...] profile name ...` + `apply-profile` | 预置参数模板并下发 | `-> ip multicast vlan 10 apply-profile` | 3304/3308 |
| ipv6 multicast 族 | `ipv6 multicast ...` 与 IPv4 版同构（admin-state/querying/static-group/profile 等） | MLD 对应命令 | `-> ipv6 multicast vlan 20 admin-state enable` | 3310+ |
| show ip multicast | `show ip multicast [vlan id \| service id]` | IPMS 状态首查 | `-> show ip multicast` | 3390 |
| show ip multicast forward / group | `show ip multicast forward [ip] [vlan ...] [all-vrf]` / `show ip multicast group [ip] ...` | 转发表/成员表 | `-> show ip multicast forward` | 3399/3408 |
| show ip multicast port / querier / source | `show ip multicast {port \| querier \| source}` | 端口/查询器/源 | `-> show ip multicast querier` | 3396/3405/3412 |

### 组播 VLAN MVR（第 34 章）

| 命令 | 语法要点 | 关键参数与默认值 | 典型用法（一行示例） | 页码 |
|---|---|---|---|---|
| ipmvlan | `ipmvlan ipmvlan-id mode {enterprise \| ...} [admin-state {enable \| disable}] [name desc]`，`no` 删除 | 组播 VLAN 通道 | `-> ipmvlan 1003 mode enterprise admin-state enable` | 3473 |
| ipmvlan c-tag | `ipmvlan ipmvlan-id c-tag {ctag \| ctag1-ctag2}`，`no` 删除 | c-tag 转换规则 | `-> ipmvlan 1003 c-tag 100` | 3481 |
| ipmvlan receiver-port / source-port | `ipmvlan ipmvlan-id {receiver-port \| source-port} {port ...}` | 收/发端口角色 | `-> ipmvlan 1003 receiver-port port 1/1/5` | 3477+ |
| show ipmvlan | `show ipmvlan config [ipmvlan-id]`；另有 port-config/address | — | `-> show ipmvlan config 100` | 3485+ |

### DVMRP / PIM / 组播边界（第 35-37 章）

| 命令 | 语法要点 | 关键参数与默认值 | 典型用法（一行示例） | 页码 |
|---|---|---|---|---|
| ip dvmrp admin-state / interface | `ip dvmrp admin-state {enable \| disable}`；`ip dvmrp interface if_name` | 全局/接口启停 | `-> ip dvmrp interface vlan-10` | 3497/3503 |
| ip dvmrp 计时器族 | `flash-interval / graft-timeout / neighbor-interval / neighbor-timeout / prune-lifetime / prune-timeout / report-interval / route-holddown / route-timeout` | — | `-> ip dvmrp prune-lifetime 700` | 3505-3533 |
| show ip dvmrp | `show ip dvmrp [interface \| neighbor [ip] \| nexthop \| prune \| route \| tunnel]` | — | `-> show ip dvmrp neighbor` | 3540-3564 |
| ip pim sparse/bidir/dense admin-state | `ip pim {sparse \| bidir \| dense} admin-state {enable \| disable}` | 三种模式全局开关 | `-> ip pim sparse admin-state enable` | 3546-3556 |
| ip pim cbsr | `ip pim cbsr ip_address [priority p] [mask-length bits]`，`no` 删除 | Candidate-BSR | `-> ip pim cbsr 10.0.0.1 priority 30` | 3558 |
| ip pim candidate-rp | `ip pim candidate-rp rp_address group/prefix [[no] bidir] [priority p] [interval s]` | C-RP 通告 | `-> ip pim candidate-rp 10.0.0.1 239.0.0.0/8` | 3564 |
| ip pim static-rp | `ip pim static-rp group/prefix rp_address [[no] bidir] [[no] override] [priority p]` | 默认 priority 未设、override/bidir 为 false | `-> ip pim static-rp 239.0.0.0/8 10.0.0.1` | 3560 |
| ip pim ssm group | `ip pim ssm group group/prefix [[no] override] [priority p]` | SSM 组映射 | `-> ip pim ssm group 232.0.0.0/8` | 3554 |
| ip pim interface | `ip pim interface if_name ...`（含 stub、joinprune-mtu/delay 等子参数），`no` 删除 | 接口入 PIM | `-> ip pim interface vlan-203` | 3594 |
| ip pim bfd-state | `ip pim bfd-state {enable \| disable}`；all-interfaces/接口级变体 | — | `-> ip pim bfd-state enable` | 3685+ |
| show ip pim | `show ip pim {neighbor [ip] \| bsr \| cbsr \| candidate-rp \| interface [if] \| group-map \| static-rp \| anycast-rp \| groute [g] \| sgroute}` | 排障族 | `-> show ip pim groute 225.0.0.0` | 3642-3720 |
| ip mroute-boundary | `ip mroute-boundary if_name scoped_address mask`，`no` 删除 | 组播地址边界 | `-> ip mroute-boundary vlan-2 239.0.0.0 255.0.0.0` | 3771 |
| ip mroute mbr | `ip mroute mbr admin-state {enable \| disable}` | MBR 默认 disabled；DVMRP/PIM 互通 | `-> ip mroute mbr admin-state enable` | 3777 |

### QoS 硬件与策略模型（第 38-39 章）

| 命令 | 语法要点 | 关键参数与默认值 | 典型用法（一行示例） | 页码 |
|---|---|---|---|---|
| qos trust-ports | `qos trust-ports` / `qos no trust-ports` | 端口默认全部 untrusted | `-> qos trust-ports` | 3801 |
| qos user-port | `qos user-port {filter \| shutdown} {spoof \| bgp \| bpdu \| rip \| ospf \| vrrp \| dvmrp \| pim \| isis \| dhcp-server \| dns-reply ...}` | 用户口控制协议防护 | `-> qos user-port filter bpdu` | 3816 |
| qos dei | `qos dei {ingress \| egress}` / `qos no dei ...` | 默认不做 DEI 标记/映射 | `-> qos dei ingress` | 3819 |
| qos apply / revert / flush / reset | `qos apply`（下发并写 flash）/ `qos revert`（回退未应用配置）/ `qos flush`（清 pending 策略）/ `qos reset`（恢复默认） | 策略生命周期四命令 | `-> qos apply` | 3822-3828 |
| show qos port / statistics / config | `show qos port [c/s/p]` / `show qos statistics` / `show qos config` | — | `-> show qos port 1/1/5` | 3864-3880 |
| policy condition | `policy condition cond_name [source ip ...] [destination ip ...] [ip-port/tcp-port/udp-port ...] [ethertype ...] [dscp ...] [802.1p ...] [vlan ...] [fragments] [vrf ...]`（40+ 匹配子命令，inner 前缀支持 QinQ 内层，P25） | — | `-> policy condition c1 source ip 10.1.0.0/16` | 4002+ |
| policy action | `policy action action_name [disposition {accept \| drop \| deny}] [cir kbps cbs bytes pir kbps pbs bytes] [802.1p p] [tos t] [redirect port ...] [mirror ...] [no-cache]` | 默认无丢弃算法、队列不共享 | `-> policy action a1 disposition drop` | 4114+ |
| policy rule | `policy rule rule_name [enable \| disable] [precedence p] [condition c] [action a] [validity-period n] [log] [count {packets \| bytes}] [trap] [default-list]` | condition+action 组合（P23） | `-> policy rule r1 condition c1 action a1` | 3957 |
| policy list | `policy list list_name type {unp \| egress \| appfp \| empacl} [enable \| disable]` + `policy list list_name rules r1 [r2...]` | 开机存在 default list | `-> policy list L1 type egress` | 3969 |
| policy network/port/vlan/mac/service group | `policy {network \| port \| vlan \| mac \| service} group name ...`（多对象成组复用，P27） | — | `-> policy network group NET1 10.1.0.0/16` | 3975-3988 |
| show policy | `show [applied] policy {condition [n] \| action \| rule [n] \| list ...}` | applied 前缀查已生效配置 | `-> show applied policy rule` | 4170+ |

### AAA 准入（第 41 章）

| 命令 | 语法要点 | 关键参数与默认值 | 典型用法（一行示例） | 页码 |
|---|---|---|---|---|
| aaa authentication | `aaa authentication {console \| telnet \| ftp \| http \| snmp \| ssh \| default} server1 [server2...] [local] [exit-/on-fail {enable \| disable}]`，`no` 移除 | 启动时 console 默认 local 认证 | `-> aaa authentication default rad1 local` | 4231 |
| aaa server-group / radius / tacacs | `aaa server-group name [radius \| tacacs+]`；`radius-server host ip [key ...]`（同构 tacacs） | 服务器组与主机定义 | `-> aaa server-group RAD1 radius` | 4205+ |
| show aaa / radius | `show aaa authentication`；`show radius-server [...]` | 当前认证配置 | `-> show aaa authentication` | 4333+ |

### Access Guardian / UNP（第 42 章，199 条）

| 命令 | 语法要点 | 关键参数与默认值 | 典型用法（一行示例） | 页码 |
|---|---|---|---|---|
| unp dynamic-vlan-configuration | `unp dynamic-vlan-configuration`，`no` 关闭 | RADIUS 下发不存在 VLAN 时动态建 VLAN；默认 disabled；动态 VLAN 不可 `no vlan` 删（X15） | `-> unp dynamic-vlan-configuration` | 4476 |
| unp auth-server-down | `unp auth-server-down [voice] {profile1 name [profile2 name] [profile3 name]}` | RADIUS 不可达时的回落 profile | `-> unp auth-server-down profile1 dead-profile` | 4482 |
| unp mac-mobility | `unp mac-mobility`，`no` 关闭 | 全局 MAC 移动性默认 disabled（支持 SPB 域 VRRP） | `-> unp mac-mobility` | 4517 |
| unp profile | `unp profile profile_name [vlan vlan_id \| sap ...] [qos-policy-list ...] [captive-portal ...] [trust-tagged-vlans ...] [inactivity-interval s] [mac-mobility] [saa-profile ...]`，`no` 删除 | 创建时各参数取默认值（见原书表）；multi-untag SAP 与 persistent profile 互斥（X13） | `-> unp profile VOICE vlan 110` | 4525 |
| unp port profile | `unp {port c/s/p[-p2] \| linkagg id} profile profile_name`，`no` 移除 | 静态绑定 profile（默认无） | `-> unp port 1/1/5 profile VOICE` | 4654 |
| unp port domain | `unp {port ... \| linkagg ...} domain domain_id`，`no` 移除 | 默认 domain 0 | `-> unp port 1/1/1 domain 1` | 4640 |
| show unp profile / port / user | `show unp profile [name] [trust-tagged-vlans]`；`show unp port [c/s/p] [type {bridge \| access}]`；`show unp user [port ...] [mac-address mac] [profile ...] [count]` | 用户/MAC/认证状态查询 | `-> show unp user count` | 4831/4868/4890 |

### AppMon / LPS / PPPoE-IA（第 43/49/58 章）

| 命令 | 语法要点 | 关键参数与默认值 | 典型用法（一行示例） | 页码 |
|---|---|---|---|---|
| app-mon admin-state | `app-mon admin-state {enable \| disable}` | 应用识别总开关；与 linkagg 互斥（X12） | `-> app-mon admin-state enable` | 4936 |
| port-security | `port-security [port ...] {enable \| disable}`（LPS 学习型端口安全，第 49 章） | — | `-> port-security port 1/1/3 enable` | 5213 |
| port-security maximum / mac / violation | `port-security [port ...] maximum n`；`port-security mac ...`；`port-security port violation ...` | MAC 数上限/静态 MAC/违例动作 | `-> port-security port 1/1/3 maximum 5` | 5225/5222/5234 |
| show port-security | `show port-security [port ...] [brief] [mac-range] [learning-window]` | — | `-> show port-security brief` | 5245-5253 |
| pppoe-ia | `pppoe-ia {enable \| disable}`（第 58 章） | PPPoE 中间代理全局开关 | `-> pppoe-ia enable` | 5572 |
| pppoe-ia port / trust | `pppoe-ia {port c/s/p \| linkagg id} ...`；`pppoe-ia {trust \| client} ...` | 端口级与信任模式 | `-> pppoe-ia port 1/1/2` | 5575/5577 |
| pppoe-ia circuit-id / remote-id | `pppoe-ia circuit-id ...` / `pppoe-ia remote-id ...`（option82/option82 风格字段） | — | `-> pppoe-ia remote-id ...` | 5581/5584 |
| show pppoe-ia | `show pppoe-ia {configuration \| port ... \| statistics}` | — | `-> show pppoe-ia statistics` | 5588-5594 |

## E（实证案例）
- 命令地图型 skill，不搬运案例；原书每条命令自带 Example，按章首页码回查（cases 原件未创建）

## B（反例/坑）
- PolicyView 创建的规则不能经 CLI 修改（CLI 只能以更高优先级新建策略覆盖）（X21，<<<PAGE 3953>>>）
- QoS Policy 章部分命令在一个或多个平台不受支持，需查各命令平台矩阵与 release notes（X4，<<<PAGE 3953>>>）
- UNP multi-untag SAP 与 persistent profile 互斥（X13，<<<PAGE 4470>>>）
- 私有 VLAN 不能配置为 Trust-Tagged VLAN；关联 Trust-Tagged VLAN 的 UNP profile 不能映射到 service domain；使用时端口 Trust-Tag 必须禁用（X14）
- UNP 动态创建的 VLAN 不能用标准 `no vlan vlan_id` 删除（X15）
- linkagg 与 AppMon 互斥：聚合不能配在 AppMon 已启用的端口上（X12，<<<PAGE 1092>>>）
- Application Fingerprinting 规格表全平台 Currently not supported（Specifications Guide 佐证）

## 来源
OmniSwitch AOS Release 810R04 CLI Reference User Guide 第 33-44、49、58 章（<<<PAGE 3227-4205、4934-5039、5212-5256、5571-5597>>>）。条目来源：principles P23-P31；counter-examples X4/X12/X13/X14/X15/X21；frameworks F7/F8/F10。
