# DIGEST · OmniSwitch 有线排障精华（不读全书、只看精华）

> 目标读者：拿到故障单要立刻动手的网工。本文浓缩 587 页教材（DT00XTE221EN）+ 9 个排障 skill 的判据、命令与红线，数字与命令均带原书页码。

## 一、一页看懂有线排障

**七步主流程**（p52）：Identify 收集症状 → Re-Create 复现 → Isolate 隔离 → Locate 定位（用 OSI 定到层/设备/物理位置）→ Solve 修复 → Verify 验证（复测回基线才算修好）→ Document 记录并保存变更。不可复现就回到第一步继续追问，不许跳去"修复"。

**OSI 六种切入法**（p57-58）：Bottom-Up（物理层往上，硬件线缆线索，慢而稳）、Top-Down（应用往下，软件导向）、Divide and Conquer（中间层二分，复杂新问题首选）、Follow the path（沿数据路径走）、Spot the differences（对比正常/异常设备配置差异）、Move the problem（组件换位观察）。

**TKC 先查库再动手**（p24-31）：ALE 官方知识库，Partner Portal / My Portal 进入，检索框直接写自然语言；用例结构固定为 Case Description（拓扑/场景/环境/诊断）+ Resolution（配置/热补丁/固件升级）。版本相关故障（如 VC 重载后 linkagg 保持 DOWN、UNP 用户卡 In progress）往往一条检索直接命中修复版本（p132）。第二渠道是 Spacewalkers 开放社区（www.spacewalkers.com）。开 eService Request 前按 p54 备齐拓扑、版本、日志、已做动作，信息不全会被打回。

排障前提是九类文档基线（p53）；缺了就用 `show lldp remote-system`、`show vlan members`、`show linkagg port` 重建拓扑。

## 二、故障域路由图（现象 → skill 分流）

| 故障现象 | 分流判据 | 去 skill |
|---|---|---|
| 任意故障，刚开始 | 先定方法、先查 TKC | lan-troubleshooting-methodology |
| 无法启动/密码丢/模块 DOWN/CPU 高/温度告警 | 整机或系统级，POWER ON + operational DOWN = 先怀疑软件（p100） | boot-system-troubleshooting |
| 同网段 ping 不通、端口 down、VLAN/端口类型错配、ARP 不解析 | 单段二层路径问题 | l2-connectivity-troubleshooting |
| MAC 漂移、广播风暴、CPU 98% + DoS invalid ip 刷屏（源 MAC 00:00:5e） | 是环不是攻击，先查环（p199） | stp-loop-troubleshooting |
| 多台同时异常、VFL 不 up、NOK 码、vcsetup.cfg 报错 | 先 `show virtual-chassis topology` 判断 VC 层 | virtual-chassis-troubleshooting |
| 跨网段不通、DHCP 拿不到地址、OSPF/RIP 邻居卡 Init、VRRP VRID Errors | 三层路由与网关冗余 | l3-routing-vrrp-troubleshooting |
| 单播通、组播不通 | PIM 未在路径某接口启用或 RPF 不通（p280） | multicast-troubleshooting |
| 要读/调日志、QoS 计数找丢包段、抓包、802.1X 认证失败 | 工具层，服务所有协议排障 | app-logging-qos-troubleshooting |
| 部署 AI 运维、纳管告警、Teams Bot、处置闭环 | 工具链层面；根因仍回各协议 skill | ovna-deployment-teams-bot |

两条跨域口诀：CPU 高 + DoS 刷屏先查环（环路把管理面打挂时必须走 console/EMP，p199）；组播不通先 traceroute 单播路径——RPF 依赖单播路由，单播不通先修单播。

## 三、命令速查表

| 场景 | 命令 | 页码/判读 |
|---|---|---|
| 系统体检入口 | show system → show chassis/cmm → show running-directory → show module status/long → show hardware-info → show health | p04；短 uptime = 刚重启过，重要线索 |
| CPU 水位与隔离 | show health [all cpu] → show health slot <c/s> → su 维护 shell 用 top/ps -T | p110-111；四大根因：异常进程/规模设计不当/DoS/上 CPU 报文过多 |
| 端口判读 | show interfaces（Error Frames/CRC 两次采样、Collision、Last Time Link Changed） | p10；全双工下 Collision 涨 = 对端被强制半双工 |
| VLAN 三要素 | show vlan member | p124；端口在正确 VLAN、端口类型匹配（default/qtagged）、STP 状态 forwarding |
| ARP 五步 | show mac-learning port → show ip interface vlan → show arp → 终端 arp -a | p127-128 |
| 日志检索 | show log swlog \|grep <appid> [timestamp …] [reverse] | p17；三板斧 grep/时间戳/reverse |
| 日志调级 | swlog appid ospf_0 subapp all level debug3 → **排障后必须调回 info** | p151/p246；OSPF 子应用：14=HELLO 15=AUTH 16=STATE |
| MAC 漂移 | show mac-learning mac-address <mac>（执行两次）；swlog appid slNi subapp macmove level debug2 → \|grep MACMOVE | p181；"flapped 3655 times" 即实锤 |
| BPDU 统计 | debug stp bpdu-stats <实例> start/show/stop | p23；某口只 tx 无 rx = 单向链路 |
| VC 四层 | show virtual-chassis topology → consistency → cat vcsetup.cfg → debug show virtual-chassis status | p162；NOK_08 没配 VFL 口、NOK_14 VFL 未全 up、NOK_17 四分钟没发现对等体（p195） |
| 丢包定位 | policy condition source ip + icmptype 8/0 → rule … log → qos apply → show active policy rule / show qos log | p214；两端部署对比计数找丢包段 |
| OSPF 邻居 | show ip ospf neighbor → show ip ospf interface → swlog … level debug3 → \|grep ospf_0 | p246；日志直接给差异值（helloInterval、pktKey） |
| DHCP 中继 | show ip dhcp relay statistics | p227；Tx Server Total Count = 0 = 中继没转发 |
| VRRP 三角 | show ip vrrp ↔ show ip vrrp statistics ↔ show configuration snapshot vrrp | p250；VRID Errors>0 优先查虚拟 IP/VRID 不匹配 |
| 组播 | show ip multicast [group/forward/source] → show ip pim interface/neighbor/sgroute | p257；沿单播路径逐口核 PIM enabled |
| 抓包 | port-monitoring 1 source port <口> capture-type full enable file /flash/capture.cap | 六类流量设计上抓不到：LACP/LLDP/802.1X/OAM/L3 控制报文/GARP |

## 四、五大 LAB 根因复盘

- **LAB1（L2 连通）**：Client10 认证后 ping 不通 Client5，三层根因叠加——端口 1/1/1 被禁用（inactive）、6860-B 的 vlan 30 IP 接口未启用、UNP 会话卡 In progress 需 `unp user flush port 1/1/1`。教训：认证 OK 不等于路径通（p140-143）。
- **LAB2（VC + STP）**：案例 1——6360 两台各自成 Master，vcsetup.cfg.1.err 直指 `vf-link-mode static` 在 stackport 平台不支持、member-port 编号与 chassis-id 不符；改 auto 后 write memory 弹 "Chassis 2 missing … erased permanently" 警告需停下确认（p191-198）。案例 2——CPU 98% + DoS invalid ip 刷屏，真根因是 VLAN 278 STP 被 OFF，两端口成环把自己的 VRRP 通告环回收；修复路径：禁端口 → `spantree Vlan 278 admin-state enable` → 恢复（p199-203）。
- **LAB3（L3 + DHL）**：案例 1——DHL 双链路全 dhl-blocking，根因两条链路 native VLAN 不一致（vlan 57 一边 tagged 一边 untagged）（p223-226）。案例 2——DHCP 拿不到地址，Tx Server = 0，中继目的地 172.168.100.102 抄错（应为 192）（p223-227）。
- **LAB4（路由协议/组播）**：VRRP 三连错——VRID2 没 enable、虚拟 IP .154 应为 .254、接口 DOWN 导致 Initialize（p278-284）；OSPF 双层错——auth-key 一字母之差（alcatell/alcatel）叠 hello-interval 20 vs 10，debug3 日志直给答案，修一层复测再挖下一层，路由数 22→17→22 回基线（p279-289）；组播案例——单播通组播不通，路径上 6900-A 的 int_217 没启用 PIM，join 到不了源侧（p280-292）。
- **LAB5（Network Advisor）**：su 维护 shell 用 `logger -t swlogd` 注入 DoS/PMD 日志，走完检测→通知→处置→留档闭环；DoS 选 Disable Port 由 OVNA 经 SSH 下发，PMD 崩溃类只取证升级 TAC，登录失败 Acknowledge 即可（p380-385）。

## 五、高可用排障专题

**STP 环路八步清单**：① 取逻辑+物理拓扑；② 开监控（swlog 调 debug2 + `swlog output flash-file-size 12500`）；③ 核 MAC 反复 flush/重学；④ 收集全网 STP 配置（同一模式/根桥/阻塞口位置）；⑤ 核定时器与 Topology Changes（快速递增 = 设备无法就根桥达成一致，BPDU 可能被丢，p180）；⑥ 本应阻塞的口变转发只有两大原因——原转发链路物理故障、根桥 BPDU 被丢；⑦ MAC flapping 三板斧；⑧ MSTP 三致性（region 名/ VLAN-MSTI 映射/互联链路全 tagged，p184）。应急止血：优先禁用"本应阻塞"的端口。

**VC 四层递进**：topology（角色/状态）→ consistency（带星号项必一致：Chassis Type/Chas ID/Group/Hello Interval/Control Vlan/License）→ 逐台 cat vcsetup.cfg（看 .err 文件的行号与原因）→ debug status 按 L0-L8 定位 NOK 码。脑裂防护：VFL 双断时 RCD（带外，走 EMP）与 VCSP（带内）检测分裂，非 Master 侧自动进 Protection 模式关闭全部用户口——这是设计行为，先恢复 VFL 再谈业务。

## 六、学习路径（9 个 skill 顺序）

1. lan-troubleshooting-methodology（总纲：七步法 + OSI 六法 + TKC）
2. boot-system-troubleshooting（系统层判读，一切 LAB 的前置）
3. l2-connectivity-troubleshooting（物理→配置→ARP 三层走法）
4. app-logging-qos-troubleshooting（swlog/QoS/抓包工具层）
5. stp-loop-troubleshooting（环路八步 + DHL）
6. virtual-chassis-troubleshooting（VC 四层 + NOK 码）
7. l3-routing-vrrp-troubleshooting（OSPF/RIP/VRRP/DHCP）
8. multicast-troubleshooting（IPMS/DVMRP/PIM 分层）
9. ovna-deployment-teams-bot（AI 运维闭环，工具链收口）

先方法、再系统、再二层、再工具、再逐协议上探、最后运维平台——与原书三天课程结构一致（DAY1 p3-143 / DAY2 p144-227 / DAY3 p228-385）。

## 七、排障红线

- **先占 console**：环路风暴把 Telnet/SSH 全打挂，不占 console 口就只能干等；EMP 是带外兜底（ce01）。
- **su 维护 shell 慎用**：不是后门，只在技术支持指导下进；动作限定只读观察（top/ps），找到可疑进程联系 ALE，绝不自行杀进程，用完立即 exit（ce02）。
- **write memory 警告必须停下**：VC 变更/半拆状态下弹 "Chassis N missing … erased permanently"，随手按 Y = 缺失机箱配置永久删除（ce18）。同类不可逆：Teams Bot 的 Client secret 只显示一次。
- **debug 用完调回 info**：debug 级日志持续高速写 flash，本身制造高 CPU/日志风暴次生故障——`swlog appid … level info` 收尾要写进 SOP（ce04）；`debug ip packet` 必须带过滤维度（ip-address/protocol/timeout 60）并尽快 stop（ce03）。
- **不调 STP 定时器**：唯二可调的是桥优先级与端口 cost/priority（ce17）；升级顺序铁律——先 AOS 再 U-Boot/FPGA/CPLD，颠倒会出问题（ce09）。
- **clear arp-cache 触发全网重学**：高峰期在核心上执行会短暂中断，选维护窗口（ce10）。
- **ONIE 密码恢复只能从 console 做**，网管侧做不了（ce11）。

---
由 cangjie-skill 流水线从 DT00XTE221EN 蒸馏生成。
