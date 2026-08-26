---
name: AOS 8 CLI 命令地图——管理与 OAM 域（监测/sFlow/RMON/日志/OAM/CMM/NTP/文件/SNMP 及数据中心散章，第 18-19/45-48/50-70 章）
description: 需要在 OmniSwitch AOS 8 上配置监控排障（镜像/sFlow/RMON/Health/OAM/CFM/SAA/CPE Test Head）、日志、机箱硬件管理、NTP/文件/配置/SNMP/OpenFlow，及 FCoE/VXLAN Snooping 等散章时，用本地图定位 CLI Reference 对应章节与代表命令。含 LLDP/镜像/sFlow/日志/双 OAM/SAA/机箱/配置/SNMP 分域核心命令速查表（A3，70+ 条语法/默认值/示例/页码）。
source_book: OmniSwitch AOS Release 810R04 CLI Reference User Guide
---

## R（触发场景）
- 网络排障：要镜像端口、采 sFlow、配 RMON 告警、查 Switch Health
- OAM 诊断：802.1ag CFM（MEP/MAID）、802.3ah LINK OAM、CPE Test Head 拨测、SAA 探测
- LLDP 邻居发现与 TLV 控制
- 系统管理：日志、CMM/机箱风扇电源温度、NTP、文件系统、配置文件、SNMP、Web、OpenFlow、DNS

## I（核心理念）
双 OAM 体系（P33）：Ethernet OAM/CFM（802.1ag，MEP/MAID/远端 MEP 状态）面向连通性故障管理；LINK OAM（802.3ah）面向单链路监测。管理命令集中在全书尾部（<<<PAGE 5313-6240>>>）；LLDP（第 18 章）属监测域但页码靠前。页码取 PDF 全文标记 `<<<PAGE N>>>`。

## A1（决策框架）
1. **流量观测**：镜像/监控→第 50 章；sFlow→51；RMON→52
2. **健康与日志**：Health→54；Syslog→53
3. **OAM**：CFM→55；LINK OAM→56；CPE Test Head→57；SAA→59
4. **邻居与数据中心散章**：LLDP→18；FIP Snooping→45；FCoE/FC Gateway→46；VXLAN Snooping→47；Port Mapping→48；SIP→19
5. **系统管理**：CMM→60；机箱硬件→61；NTP→62；会话→63；文件→64；Web→65；配置文件→66；SNMP→67；OmniVista Cirrus→68；OpenFlow→69；DNS→70

## A2（操作步骤）·章节清单与代表命令
- **Ch18 802.1AB/LLDP（<<<PAGE 1390>>>，约 40 条）**：`lldp`（LLDPDU/邻居数据库/TLV）；`ethernet-service uni` 控制带标签/无标签 LLDPDU 处理——默认两者均丢弃（P32/X24）
- **Ch19 SIP（<<<PAGE 1486>>>，约 18 条）**：会话/互联类（章名缩写未展开，域归属待确认）
- **Ch50 Port Mirroring and Monitoring（<<<PAGE 5256>>>，约 9 条）**：`ports mirror`
- **Ch51 sFlow（<<<PAGE 5277>>>，约 13 条）**：`sflow`
- **Ch52 RMON（<<<PAGE 5305>>>，约 4 条）**：`rmon`
- **Ch53 Switch Logging（<<<PAGE 5313>>>，约 14 条）**：`syslog`（级别/服务器/过滤）
- **Ch54 Health Monitoring（<<<PAGE 5347>>>，约 6 条）**：CPU/内存/进程阈值检查
- **Ch55 Ethernet OAM（<<<PAGE 5358>>>，约 46 条）**：`cfm`/`ethernet-oam`（MEP/MAID/CCM）
- **Ch56 LINK OAM（<<<PAGE 5432>>>，约 23 条）**：802.3ah 远端发现/环回/远端故障指示
- **Ch57 CPE Test Head（<<<PAGE 5503>>>，约 31 条）**：接入侧业务拨测
- **Ch59 SAA（<<<PAGE 5597>>>，约 19 条）**：`saa`（ping/ftp/http 等业务质量探测）
- **Ch60 CMM（<<<PAGE 5645>>>，约 29 条）**：CMM 控制模块冗余/同步
- **Ch61 Chassis Management（<<<PAGE 5697>>>，约 91 条）**：`chassis`/`temperature`/`fan`/`psu`
- **Ch62 NTP（<<<PAGE 5884>>>，约 25 条）**：`ntp`/SNTP
- **Ch63 Session Management（<<<PAGE 5936>>>，约 35 条）**：CLI 会话/telnet/SSH 超时
- **Ch64 File Management（<<<PAGE 5999>>>，约 21 条）**：`copy`/`delete`/`directory`/脚本
- **Ch65 Web Management（<<<PAGE 6040>>>，约 11 条）**：内嵌 Web 开关与 HTTP/HTTPS
- **Ch66 Configuration File Manager（<<<PAGE 6060>>>，约 11 条）**：`configuration`/`working-set`（running/committed 双区、VC 批量配置）（P34）
- **Ch67 SNMP（<<<PAGE 6079>>>，约 26 条）**：v1/v2c/v3 团体/用户/陷阱
- **Ch68 OmniVista Cirrus（<<<PAGE 6132>>>，约 10 条）**：云管理平台对接
- **Ch69 OpenFlow（<<<PAGE 6151>>>，约 8 条）**：SDN 控制器/流表混合模式
- **Ch70 DNS（<<<PAGE 6169>>>，约 6 条）**：DNS 客户端解析
- **数据中心散章**：Ch45 FIP Snooping（<<<PAGE 5039>>>，约 22 条）；Ch46 FCoE/FC Gateway（<<<PAGE 5090>>>，约 27 条）；Ch47 VXLAN Snooping（<<<PAGE 5152>>>，约 20 条）；Ch48 Port Mapping（<<<PAGE 5195>>>，约 9 条）

## A3（核心命令速查）

语法/默认值/示例均摘自原书第 18-19、45-48、50-70 章对应条目；页码为 fulltext `<<<PAGE N>>>` 标记值。`{enable | disable}` 表示"多选一"。

### LLDP（第 18 章）

| 命令 | 语法要点 | 关键参数与默认值 | 典型用法（一行示例） | 页码 |
|---|---|---|---|---|
| lldp lldpdu | `lldp [non-tpmr \| nearest-customer \| nearest-bridge \| all] {port c/s/p[-p2] \| slot c/s} lldpdu {tx \| rx \| tx-and-rx \| disable}` | 按 agent 控制收发；带标签/无标签控制帧默认丢弃（X24，需 ethernet-service uni / l2profile 处理） | `-> lldp port 1/1/5 lldpdu tx-and-rx` | 1402 |
| lldp transmit interval / hold-multiplier | `lldp transmit interval seconds` / `lldp transmit hold-multiplier num` | 全局通告计时器 | `-> lldp transmit interval 30` | 1394/1396 |
| lldp tlv management / dot1 / dot3 / med | `lldp [agent] {port ...} tlv {management {port-description \| system-name \| ...} \| dot1 ... \| dot3 ... \| med ...} {enable \| disable}` | TLV 粒度控制 | `-> lldp port 1/1/5 tlv management system-name enable` | 1411-1422 |
| lldp network-policy / med network-policy | `lldp network-policy {policy-id ...}` / `lldp med network-policy ...` | 语音/策略通告 | `-> lldp network-policy voice vlan 110` | 1406/1409 |
| lldp trust-agent | `lldp trust-agent ...` + `violation-action` | 信任代理与违例动作 | `-> lldp trust-agent ...` | 1476/1479 |
| show lldp config / remote-system | `show lldp config [port ...]` / `show lldp remote-system [port ...]`；med/application-tlv/power-via-mdi 变体 | 邻居首查 | `-> show lldp remote-system` | 1446/1453 |
| show lldp statistics / system-statistics | `show lldp statistics [port ...]` | 计数排障 | `-> show lldp statistics` | 1436/1434 |

### 端口镜像与监测（第 50 章）

| 命令 | 语法要点 | 关键参数与默认值 | 典型用法（一行示例） | 页码 |
|---|---|---|---|---|
| port-mirroring source destination | `port-mirroring session_id source port c/s/p[-p2] destination {port c/s/p \| linkagg id} [rpmir-vlan vlan] [bidirectional \| inport \| outport] [loopback] [tag-remove] [enable \| disable]`；`no source/destination` 拆源/目的 | 会话级镜像 | `-> port-mirroring 1 source port 1/1/5 destination port 1/1/10 enable` | 5257 |
| port-monitoring source | `port-monitoring session_id source port c/s/p [file filename [size n] \| no file] [overwrite {on \| off}] [inport \| outport \| bidirectional] [timeout s] [capture-type {full \| brief}]` | 抓包到文件 | `-> port-monitoring 1 source port 1/1/5 file cap.txt bidirectional` | 5262 |
| show port-mirroring / port-monitoring status | `show port-mirroring status [session_id]` / `show port-monitoring status` + `file` | — | `-> show port-mirroring status` | 5271/5273-5275 |

### sFlow / RMON（第 51-52 章）

| 命令 | 语法要点 | 关键参数与默认值 | 典型用法（一行示例） | 页码 |
|---|---|---|---|---|
| sflow receiver | `[vrf name] sflow receiver index {name string \| timeout {seconds \| forever} \| address ip \| udp-port p \| packet-size n \| version n \| release}` | 采集器定义 | `-> sflow receiver 1 address 10.0.0.99` | 5281 |
| sflow sampler | `[vrf name] sflow sampler num port c/s/p {receiver index \| rate value \| sample-hdr-size n}`，`no` 删除 | 端口采样率 | `-> sflow sampler 1 port 1/1/5 receiver 1 rate 512` | 5284 |
| sflow poller | `[vrf name] sflow poller num port ... {receiver index \| interval s}` | 计数器轮询 | `-> sflow poller 1 port 1/1/5 receiver 1 interval 20` | 5286 |
| show sflow | `show sflow {agent \| receiver [n] \| sampler [n] \| poller [n]}` | — | `-> show sflow sampler` | 5294-5302 |
| rmon probes | `rmon probes {stats \| history \| alarm} [entry_number] {enable \| disable}` | 探针类别开关 | `-> rmon probes alarm 4012 enable` | 5306 |
| show rmon | `show rmon probes [entry]`；`show rmon events` | — | `-> show rmon probes` | 5308/5311 |

### 日志与健康（第 53-54 章）

| 命令 | 语法要点 | 关键参数与默认值 | 典型用法（一行示例） | 页码 |
|---|---|---|---|---|
| swlog | `swlog {enable \| disable \| preamble \| hash-time-limit seconds \| duplicate-detect \| console level num \| default level level}`，`no swlog [preamble \| duplicate-detect]` | 日志总开关与去重 | `-> swlog enable` | 5314 |
| swlog output / appid / syslog-facility-id | `swlog output {console \| file \| socket} ...`；`swlog appid ...`；`swlog syslog-facility-id ...` | 输出目的地/应用级别 | `-> swlog output file enable` | 5320+ |
| swlog clear | `swlog clear` | 清日志 | `-> swlog clear` | 5327 |
| show log swlog / show log events | `show log swlog` / `show log events [output ...]` | 查询历史 | `-> show log swlog` | 5333/5343 |
| health threshold | `health threshold {rx pct \| txrx pct \| memory pct \| cpu pct \| flash pct}` | 资源阈值告警 | `-> health threshold cpu 80` | 5348 |
| health interval | `health interval seconds` | 采样间隔 | `-> health interval 20` | 5350 |
| show health | `show health [configuration \| all]` | 健康总览 | `-> show health all` | 5352-5356 |

### Ethernet OAM / CFM 802.1ag（第 55 章）

| 命令 | 语法要点 | 关键参数与默认值 | 典型用法（一行示例） | 页码 |
|---|---|---|---|---|
| ethoam domain | `ethoam domain md_name format {none \| dnsname \| mac-address-uint \| string} level num`，`no` 删除 | MD 层级 level 0-7 | `-> ethoam domain MD format none level 3` | 5362 |
| ethoam association | `ethoam association ma_name format {vpnid \| unsignedint \| string \| primaryvid \| icc-based} domain md_name`，`no` 删除 | MA（维护集） | `-> ethoam association MA format string domain MD` | 5368 |
| ethoam association ccm-interval | `ethoam association ma domain md ccm-interval {interval100ms \| interval1s \| interval10s \| interval1m \| interval10m}` | CCM 周期 | `-> ethoam association MA domain MD ccm-interval interval1s` | 5376 |
| ethoam endpoint | `ethoam endpoint mep_id domain md association ma direction {up \| down} {port c/s/p \| virtual \| linkagg id} [primary-vlan vlan \| cvlan vlan]`，`no` 删除 | MEP 创建 | `-> ethoam endpoint 100 domain MD association MA direction down port 1/1/5` | 5391 |
| ethoam endpoint ccm | `ethoam endpoint mep_id domain md association ma ccm {enable \| disable}` | 连续性检测报文 | `-> ethoam endpoint 100 domain MD association MA ccm enable` | 5397 |
| ethoam loopback | `ethoam loopback {target-endpoint mep \| target-macaddress mac} source-endpoint mep domain md association ma [number n] [data string]` | LBM/LBR 连通性探测 | `-> ethoam loopback target-endpoint 101 source-endpoint 100 domain MD association MA` | 5407 |
| ethoam linktrace | `ethoam linktrace {target-macaddress mac \| target-endpoint mep} source-endpoint mep domain {md \| mac} association ma [flag ...] [hop-count n]` | 逐跳路径追踪 | `-> ethoam linktrace target-endpoint 101 source-endpoint 100 domain MD association MA` | 5405 |
| ethoam one-way-delay / two-way-delay | `ethoam {one-way-delay \| two-way-delay} {target-endpoint mep \| ...} source-endpoint mep domain md association ma` | 时延/抖动测量 | `-> ethoam two-way-delay target-endpoint 101 source-endpoint 100 domain MD association MA` | 5414/5416 |
| show ethoam | `show ethoam [domain [md [association [end-point]]]]`；另有 remote-endpoint/linktrace-reply/statistics/config-error 等 | CFM 排障族 | `-> show ethoam domain MD association MA end-point` | 5419-5449 |

### LINK OAM 802.3ah（第 56 章）

| 命令 | 语法要点 | 关键参数与默认值 | 典型用法（一行示例） | 页码 |
|---|---|---|---|---|
| efm-oam admin-state | `efm-oam admin-state {enable \| disable}` | 全局默认 disabled | `-> efm-oam admin-state enable` | 5454 |
| efm-oam port admin-state / mode | `efm-oam port c/s/p admin-state {enable \| disable}` / `efm-oam port c/s/p mode {active \| passive}` | mode 默认 active | `-> efm-oam port 1/1/1 mode passive` | 5456/5458 |
| efm-oam port keepalive / hello interval | `efm-oam port c/s/p {keepalive-interval \| hello-interval} seconds` | 计时器 | `-> efm-oam port 1/1/1 hello-interval 5` | 5460/5462 |
| efm-oam port remote-loopback | `efm-oam port c/s/p remote-loopback {process \| ignore}` + `start` 发起 | 默认 ignore 对端环回请求 | `-> efm-oam port 1/1/1 remote-loopback process` | 5464/5466 |
| efm-oam port l1-ping | `efm-oam port c/s/p l1-ping [num-frames n] [delay ms] [start]` | 物理层 ping | `-> efm-oam port 1/1/12 l1-ping num-frames 6 delay 300 start` | 5478 |
| efm-oam errored-frame 族 | `efm-oam {errored-frame \| errored-frame-period \| errored-frame-seconds-summary \| multiple-pdu-count} ...` | 误帧阈值监测 | `-> efm-oam errored-frame ...` | 5470-5477 |
| show efm-oam | `show efm-oam [configuration \| port [detail \| statistics \| remote detail \| history \| l1-ping detail]]` | — | `-> show efm-oam port detail` | 5480-5497 |

### CPE Test Head / SAA（第 57/59 章）

| 命令 | 语法要点 | 关键参数与默认值 | 典型用法（一行示例） | 页码 |
|---|---|---|---|---|
| test-oam | `test-oam name [descr description]`，`no` 删除 | CPE 拨测测试定义 | `-> test-oam Test1` | 5505 |
| show test-oam | `show test-oam [statistics [saa] \| group [saa statistics \| statistics]]` | 拨测结果 | `-> show test-oam statistics` | 5530-5569 |
| saa | `[vrf name] saa string [descr d] [interval i] [jitter-threshold j] [rtt-threshold r]`，`no` 删除 | SAA 探测实例 | `-> saa saa1 interval 10` | 5598 |
| saa type ip-ping / mac-ping / ethoam-loopback 等 | `[vrf] saa name type {ip-ping destination-ip ip source-ip ip [num-pkts n] [inter-pkt-delay d] [payload-size s] \| mac-ping ... \| ethoam-loopback ... \| ethoam-two-way-delay ...}` | 探测类型配置；`saa spb ...` 为 SPB 专测 | `-> saa saa1 type ip-ping destination-ip 10.0.0.8 source-ip 10.0.0.1` | 5601-5617 |
| saa start / stop | `[vrf] saa name start [at yyyy-mm-dd,hh:mm:ss]` / `stop [never \| at ...]` | 默认立即开始/停止 | `-> saa saa1 start` | 5620/5622 |
| show saa | `show saa [type config \| statistics \| spb \| xml \| vrf]` | — | `-> show saa statistics` | 5628-5642 |

### CMM / 机箱硬件 / NTP / 会话 / 文件（第 60-64 章）

| 命令 | 语法要点 | 关键参数与默认值 | 典型用法（一行示例） | 页码 |
|---|---|---|---|---|
| write memory | `write memory [flash-synchro]` | running→running-directory（主 CMM） | `-> write memory flash-synchro` | 5660 |
| copy certified | `copy certified image_dir [make-running-directory]` | certified→指定目录 | `-> copy certified mydir` | 5655 |
| copy flash-synchro | `copy flash-synchro` | 主备 CMM certified 同步 | `-> copy flash-synchro` | 5666 |
| show chassis / slot / module | `show chassis` / `show slot [c/s]` / `show module [long \| status]` | 硬件清单首查 | `-> show module` | 5763-5774 |
| show powersupply / fan / temperature | `show powersupply` / `show fan [tray]` / `show temperature` | 电源/风扇/温度 | `-> show temperature` | 5776-5783 |
| show system / tech-support | `show system` / `show tech-support` | 一键收集 | `-> show tech-support` | 5758/5820 |
| ntp client | `ntp client admin-state {enable \| disable}` | NTP 默认 disabled | `-> ntp client enable` | 5894 |
| ntp server / peer / master | `ntp server {ip \| name} [key id] [prefer] [burst \| iburst]`；`ntp peer ip ...`；`ntp master stratum` | 时间源三层 | `-> ntp server 10.0.0.99 prefer` | 5886/5916/5908 |
| show ntp status / server status | `show ntp status` / `show ntp server status` | 同步状态 | `-> show ntp status` | 5919/5927 |
| session timeout | `session {cli \| http \| ftp} timeout minutes` | CLI/HTTP/FTP 空闲超时 | `-> session cli timeout 5` | 5944 |
| telnet / show ssh | `[vrf name] telnet {port [default \| p] \| admin-state ...}`；`show ssh` | 管理服务 | `-> telnet admin-state disable` | 5978/5997 |
| copy / delete / dir（文件管理） | `copy source destination`、`delete filename`、`directory` 等（第 64 章） | flash 文件操作 | `-> copy certified /flash/mydir` | 5999+ |

### 配置文件 / SNMP / OpenFlow / DNS（第 66-70 章）

| 命令 | 语法要点 | 关键参数与默认值 | 典型用法（一行示例） | 页码 |
|---|---|---|---|---|
| configuration apply | `configuration apply filename [at hh:mm month dd [year]] [in hh[:mm]] [verbose]` | 立即/定时应用配置 | `-> configuration apply cfg.txt in 5 verbose` | 6061 |
| configuration snapshot | `configuration snapshot [feature_list \| all] [path/filename]` | 默认文件名 asc.#.snap | `-> configuration snapshot all` | 6071 |
| configuration apply network-sync | `configuration apply network-sync filename [community name \| local-apply]` | AMS 发布/订阅网络级同步 | `-> configuration apply network-sync preprovision.txt` | 6078 |
| write terminal | `write terminal` | 查看当前运行配置 | `-> write terminal` | 6075 |
| snmp station | `snmp station {ip \| ipv6 \| domain} [port] [username] [v1 \| v2 \| v3 [tsm ...]] [enable \| disable]`，`no` 删除 | trap 接收站 | `-> snmp station 10.0.0.99 v3` | 6081 |
| snmp community-map | `snmp community-map {community_string} user useraccount [enable \| disable]`，`no` 删除 | 团体串映射用户（默认认证启用） | `-> snmp community-map public user snmpuser` | 6091 |
| snmp security | `snmp security {no-security \| authentication set \| all \| privacy set \| all \| trap-only \| tls {enable \| disable}}` | SNMPv3 安全模式 | `-> snmp security authentication all` | 6097 |
| show snmp | `show snmp {station \| security \| statistics \| community-map ...}` | — | `-> show snmp station` | 6084+ |
| openflow logical-switch | `openflow logical-switch name [probe-time n \| failure-detect-time n \| dpid string] [admin-state ...] [mode {normal \| api \| pfc-channel}] [version {1.0 \| 1.3.1}] [vlan vlan_id] [table-miss-action {drop \| controller}]`，`no` 删除 | SDN 逻辑交换机 | `-> openflow logical-switch LS1 admin-state enable` | 6156 |
| openflow logical-switch controller | `openflow logical-switch name controller {ip \| domain}[:port] [priority n] admin-state {enable \| disable}` | 控制器连接 | `-> openflow logical-switch LS1 controller 10.0.0.10 admin-state enable` | 6159 |
| show openflow | `show openflow [logical-switch [name]]` | — | `-> show openflow logical-switch` | 6163/6165 |
| ip name-server | `ip name-server server1 [server2 [server3]]` | 最多 3 个 DNS 服务器 | `-> ip name-server 10.255.11.66` | 6172 |
| show dns | `show dns` | 解析配置 | `-> show dns` | 6178 |

## E（实证案例）
- 命令地图型 skill，不搬运案例；原书每条命令自带 Example，按章首页码回查（cases 原件未创建）

## B（反例/坑）
- LLDP 控制帧默认丢弃：带标签与无标签 802.1AB 控制帧默认均丢弃，需 `ethernet-service uni` 显式配置处理方式（X24，<<<PAGE 1390>>>）
- LINK OAM 镜像口不支持（Specifications Guide 佐证）
- 第 19 章 SIP 域归属为建议值（章名缩写在目录中未展开，待确认）

## 来源
OmniSwitch AOS Release 810R04 CLI Reference User Guide 第 18-19、45-48、50-70 章（<<<PAGE 1390-1486、5039-5212、5256-6240>>>）。条目来源：principles P32-P34；counter-examples X24；frameworks F9/F11。
