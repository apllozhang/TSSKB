---
name: l2-connectivity-troubleshooting
description: 何时用：同网段/跨网段 ping 不通、端口 down、VLAN 归属或端口类型错配、ARP 不解析等基础二层连通问题。
source_book: DT00XTE221EN OmniSwitch LAN Troubleshooting
---

# 二层连通性排障（物理 → 配置 → ARP 三层走法）

## R · 原文引用

> "Issues that could cause the communication to fail: Physical problems (Bad, missing, or miswired cables, Bad ports...) Misconfiguration (Missing or wrong VLANs, Native VLAN mismatch, VLANs not allowed on linkagg...) ARP problems" (p118)

> "show vlan member (R8): Verify the ports are in the correct VLAN, Verify spanning tree status (forwarding instead of blocking or inactive), Verify port type match what it is connecting to (default or qtagged enabled)" (p124)

> "1. Make sure that the MAC address of device A and device B are learned on the right port and in correct VLAN ... 5. Check that the device has resolved the ARP entry to the gateway IP address -> show mac-learning port ... -> show arp ... -> debug ip packet start ip-address <ip> start" (p127-128)

> "Increase MAC Address aging time ... Add silent devices MAC address in the MAC address table as permanent -> mac-learning {vlan vlan_id {port ... | linkagg ...}} static mac-address <mac> [bridging | filtering]" (p129)

## I · 方法论骨架

1. **三类故障源分序排查**（f07）：物理（线缆/端口/LED）→ 配置（VLAN/端口类型/ACL）→ ARP（MAC 学习/网关指向/解析）。
2. **端口级判读**（p10）：operational status、速率双工与对端一致；多次采样 Error Frames/CRC/Alignment，持续增长→查线缆与网卡；全双工下 Collision 增长→查对端双工配置（一端被强制半双工）；互 ping 时 Bytes Received 不增长→查网卡；Last Time Link Changed 与 Number of Status Change 看链路抖动。
3. **show vlan member 三要素**（p12）：端口在正确 VLAN；端口类型与对端匹配（终端 default/untagged，交换机间 trunk qtagged）；STP 状态 forwarding（blocking/inactive 转 STP skill）。配合 show configuration snapshot all 排 deny ACL。
4. **ARP 五步法**（p13）：① show mac-learning port 确认 MAC 学在正确端口/VLAN → ② show ip interface vlan <num> 取接口名再查 Router MAC → ③ 终端网关指向正确 → ④ show arp 确认交换机生成网关 ARP 条目 → ⑤ 终端 arp -a 确认解析。MAC 已学但 ARP 不解析 → debug ip packet start ip-address <ip> start 看 1 R/1 S 行。
5. **静默设备对策**（p14）：不主动发流量的设备 MAC 老化后被淹——加大 mac-learning aging-time 或配 static MAC（bridging/filtering）。

## A1 · 书中案例（LAB 故障根因）

- **c02（LAB1 主案例，p140-143）**：Client10 ping 不通认证后的 Client5。三层根因叠加：① 6360-A 端口 1/1/1 在 vlan 1 中 inactive——端口被禁用，`interfaces 1/1/1 admin-state enable` 恢复；② 6860-B 上 vlan 30 的 IP 接口 int_30 未启用，到 contractor 网段无路由且 DHCP 中继无归属；③ UNP 会话卡住需 `unp user flush port 1/1/1`。教训：认证 OK 不等于路径通，逐段核 VLAN/端口/接口三元状态。

## A2 · 触发场景（含与相邻 skill 的区分）

- 触发：终端互 ping 不通、端口 down、新接设备不通、VLAN 变更后断流、ARP 疑似异常。
- 区分：本 skill 处理"单段二层路径"问题。出现 MAC 漂移/环路/STP 状态异常 → stp-loop；DHL 双上联 dhl-blocking → stp-loop（含 DHL）；堆叠成员口异常 → virtual-chassis；网关冗余/路由协议 → l3-routing；组播流不通但单播通 → multicast。

## E · 可执行步骤

1. 物理层：沿数据路径查 LED → 每端口 `show interfaces` 判读（oper status/双工/错误计数采样两次/Bytes Received）。
2. 客户端侧先自查排除本机因素：ipconfig /all、ping/tracert、arp -a、nslookup、route print。
3. 交换机侧：`show configuration snapshot all` 核 VLAN 创建与端口归属 → `show vlan member` 核三要素（VLAN/端口类型/STP 状态）。
4. ARP 五步法走 p13 清单；需要时 `debug ip packet start ip-address <ip> start`（判读 1 R/1 S），用完 `debug ip packet stop`。
5. 交换机有回 ARP 但终端没有 → 交换机与终端间接 sniffer；全正常仍不通 → 终端配静态 MAC 试。
6. 静默设备：`mac-learning aging-time <seconds>` 或 `mac-learning vlan <vid> port <c/s/p> static mac-address <mac> bridging`。

## B · 边界与陷阱

- **ce10**：clear arp-cache 会触发全网重新 ARP 学习，高峰期在核心交换机上执行会造成短暂中断——先评估时段与设备位置，选维护窗口。
- **ce03**：debug ip packet 裸跑刷爆屏幕并推高 CPU，必须带过滤维度（ip-address / ip-pair / protocol / ether-type / direction / board / output，可加 timeout 60）。
- 端口类型错配（default vs qtagged）不报错只丢流量，show vlan member 逐口核对。
- 认证环境（UNP）下先看 show unp user 是否 Active，别急着怪 VLAN（c02 教训）。

---
来源条目: f07, p10, p12, p13, p14, ce03, ce10, g22, c02
