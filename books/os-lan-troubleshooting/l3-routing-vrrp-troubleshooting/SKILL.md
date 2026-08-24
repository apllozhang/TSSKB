---
name: l3-routing-vrrp-troubleshooting
description: 何时用：IP 不通/丢包定位、DHCP 拿不到地址、OSPF/RIP 邻居起不来路由消失、VRRP 状态异常或 VRID Errors 刷屏。
source_book: DT00XTE221EN OmniSwitch LAN Troubleshooting
---

# 三层路由与 VRRP 排障

## R · 原文引用

> "Basic IP troubleshooting Methodology: Local host configuration OK? -> Switch configuration OK? -> Server configuration OK? -> Can you connect using IP addresses?" (p209)

> "Example: SW1 & SW2 are not in FULL state! Modify the log level to have the maximum verbosity: SW1 -> swlog appid ospf_0 subapp all level debug3 ... Check the Hello Interval on both switches" (p246)

> "Skew_Time: (256 - Priority)/256 ... Master_Down_Interval: (3 * Advertisement_Interval) + Skew_time. When a host sends an ARP request ... the Master Router must respond using the Virtual MAC Address" (p250)

> "Tx Server: Total Count = 0"（DHCP 中继没有向服务器转发，p227）

## I · 方法论骨架

1. **IP 排障决策树**（f10）：本机配置 OK? → 交换机配置/ACL OK? → IP 地址/子网/网关/路由/ARP OK? → 服务器配置 OK? → 用 IP 直连验证。命令族：show ip traffic/interface/routes/route-pref/redist/access-list/router database/protocols/router-id + ping/traceroute。
2. **丢包定位双工具**（f11/p26）：① QoS 计数策略——policy condition（source ip + icmptype 8 请求 / icmptype 0 回复）→ action → rule 加 log → qos apply；show active policy rule 看 Packets/Bytes、show qos log 看命中明细；路径两端部署对比计数找丢包段（上游有计数下游没有=丢在这段）。② 出向流量用 port-monitoring 抓包（策略只匹配 ingress）。
3. **DHCP 中继判据**（p27）：show ip dhcp relay statistics——Reception From Client 在涨=请求到达中继；Tx Server Total Count=0=中继没向服务器转发（目的地配错或服务器不可达）；Forw Delay/Max Hops/Invalid Gateway 违规计数定位报文合法性。抓包级：debug ip packet protocol udp start timeout 60，看 UDP 67,67 与 67,68 的 R/S 行。
4. **OSPF 流程**（f12）：show ip ospf neighbor 看状态 → show ip ospf interface 核参数（Hello/Dead、认证、Area ID、MTU、掩码、DR/BDR）→ 两台 `swlog appid ospf_0 subapp all level debug3` → show log swlog | grep ospf_0 读丢弃原因 → 对症修复 → 验证 Full + 路由回来 → **调回 info**。典型错配（p238）：timer、认证、区域、Area 类型、掩码。日志样例直读（p30）："oversized LSA ... size 3588 > limit 1452"=查 MTU；"invalid helloInterval 10"=对齐 timer；"pktKey = alcatell, intfKey = alcatel"=改 auth-key。
5. **RIP 检查点**（p28）：物理 up；路由两侧存在；掩码正确；VLAN Forwarding 标志；v1/v2 兼容（RIP-2 收 RIP-1 请求回 RIP-1 响应；只发 v2 时对 RIP-1 不响应）；认证 auth-type/auth-key 一致。show ip rip interface/peer/routes（A=Active/H=Holddown/G=Garbage）。
6. **VRRP 三角核对**（f14）：show ip vrrp（Admin Status/VRID/虚拟 IP/Priority/Preempt/通告间隔两台一致）↔ show ip vrrp statistics（Checksum/Version/VRID 三错误计数；Master/Backup/Initialize 状态）↔ show configuration snapshot vrrp 逐行比对。机制（p31/g25）：Skew_Time=(256-P)/256；Master_Down=3×Adv+Skew；Master 必须以虚拟 MAC 00-00-5E-00-01-<VRID> 应答 ARP。深挖 swlog appid vrrp_0 subapp all level debug3。

## A1 · 书中案例（LAB 故障根因）

- **c06（LAB3 案例2，p223-227）**：四客户端 DHCP 拿不到地址。Reception From Client 计数在涨但对 172.168.100.102 的 Tx Server=0——**目的地地址本身就是错的**（172 vs 192 一字之差）。修复：no 掉错误 destination → `ip dhcp relay destination 192.168.100.102` → 复查计数重新累计。
- **c07（LAB4 案例1，p278-284）**：VRRP 三连错——sw7 VRID2 没 admin-state enable；sw8 虚拟 IP 配成 .154（应为 .254）导致 VRID Errors=41 两台互认非法报文；重建时报 "At least one IP address must be associated" 根因是 int_30 接口本身 DOWN。判据：VRID Errors>0 优先怀疑虚拟 IP/VRID 不匹配；Initialize 状态优先查接口与 admin-state。
- **c08（LAB4 案例2，p279-289）**：路由表 22→17 条。debug3 日志直接给答案：第一层 auth-key alcatell vs alcatel（一字母之差）；修完 "Not solve, check if there is not another problem"——第二层 hello-interval 20 vs 10。修完复测路由回 22 条、日志调回 info。
- **c09（LAB4 案例3）**：单播通组播不通 → 见 multicast skill。

## A2 · 触发场景（含与相邻 skill 的区分）

- 触发：跨网段不通、丢包需定位段、DHCP 中继失效、OSPF/RIP 邻居 Init/2-Way 卡住或路由消失、VRRP 双 Master/Initialize/VRID Errors、ECMP 退化为单路径。
- 区分：同网段二层问题 → l2-connectivity；组播不通但单播通 → multicast；丢包计数/抓包工具的 QoS 命令细节 → app-logging-qos skill；DoS invalid ip 刷屏指向 VRRP 虚拟 MAC 时是环路 → stp-loop（ce19）。

## E · 可执行步骤

1. 走 f10 决策树隔离端点/交换机/服务器，配 show ip routes + ping/traceroute。
2. 丢包定位：路径两端部署相同计数策略（icmptype 8 与 0 各一条）→ qos apply → 对比 show active policy rule 计数 → 出向或大包用 port-monitoring 抓包。
3. DHCP：show configuration snapshot ip-dhcp-relay → show ip dhcp relay statistics 核 Tx Server → 必要时 debug ip packet protocol udp start timeout 60。
4. OSPF：show ip ospf neighbor → show ip ospf interface（两端对比 Hello/Dead/认证/Area/MTU）→ swlog appid ospf_0 subapp all level debug3 → grep ospf_0 读日志直给的差异值 → 修复 → 复测 Full + 路由数回基线 → 调回 info。
5. RIP：show ip rip interface 核 Send/Receive-Version 与 AuthType → show ip rip peer/routes。
6. VRRP：三角核对（vrrp / statistics / configuration snapshot vrrp）→ VRID Errors>0 逐行比对虚拟 IP → Initialize 状态先 show ip interface 查接口 → 修复后核 Become Master 与 Adv. Rcvd 计数增长。

## B · 边界与陷阱

- **ce20**：多错叠加是常态，每修一层必须复测（邻居 Full + 路由数回基线）才能收工。
- **ce15**：VRRP 虚拟 IP 抄错一位表现为对端 VRID Errors 刷屏，新手易误判为攻击/bug；重建 VRID 报 "at least one IP address" 错误时先查接口是否 DOWN。
- **ce13**：QoS 策略只匹配 ingress，统计/镜像出向流量永远 0 命中——出向改用 port-monitoring。
- debug 级日志用完必须调回 info（ce04）。
- 同 VRID 通告间隔必须全网一致；Master 用物理 MAC 应答 ARP 即配置异常（p31）。
- ECMP 双路径退化为单路径是 OSPF 邻居故障的可视信号（g38），show ip routes 里 + 标记消失即警。

---
来源条目: f10, f11, f12, f14, p26, p27, p28, p29, p30, p31, ce13, ce15, ce20, g25, g26, g27, g38, g39, c06, c07, c08
