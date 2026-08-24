---
name: stp-loop-troubleshooting
description: 何时用：疑似桥接环路、MAC 漂移、CPU 飙高伴 DoS 刷屏、STP 状态异常、MSTP 行为飘、DHL 双上联全 blocking。
source_book: DT00XTE221EN OmniSwitch LAN Troubleshooting
---

# STP 与桥接环路排障

## R · 原文引用

> "Example of checklist recapitulating some of the actions available to troubleshoot stp: 1. Retrieve general information about network topology ... 2. Turn on events to monitor the network" (p173)

> "If ports that should be in a blocking state are now forwarding, there are two likely causes: A physical failure in a link that was previously forwarding. BPDUs from the root are being dropped." (p180)

> "MAC address flapping is mostly caused by a layer 2 loop in the network (which are not detected by STP). The command 'show mac-learning mac-address <mac>' show if the MAC address is flapping between two ports. ... port 1/1/4 has flapped 3655 times" (p181)

> "All VLANs within an MSTI must be tagged on all interswitch links otherwise MSTP becomes unpredictable ... All switches participating in the same region must have an identical MSTP configuration." (p184)

## I · 方法论骨架

1. **环路八步清单**（f08）：① 取拓扑（逻辑 VLAN/广播域 + 物理互连端口）；② 开监控——swlog 提到 debug2（portMgrCmm/intfCmm/VlanMgrCmm/portMgrNi/VlanMgrNi）+ `swlog output flash-file-size 12500`；③ 核 MAC 反复 flush/重学；④ 收集 STP 配置——全网同一模式（1x1/FLAT/MSTP）、根桥位置、非默认 cost/priority、阻塞口位置（show spantree / show spantree vlan）；⑤ 核定时器/根 ID/根端口——timers 跨链路必须一致，Topology Changes 快速递增 = 设备无法就根桥达成一致（BPDU 可能被丢）；⑥ 本应阻塞的口变转发的两大原因（p20）；⑦ MAC flapping 三板斧（p22）；⑧ MSTP 专项三致性。应急止血：优先禁用"本应阻塞"的端口。
2. **MAC flapping 检测三板斧**（p22）：show mac-learning mac-address <mac> 执行两次看出端口切换；show interfaces | grep Number 找 Status Change 大数值端口；show interfaces | grep Last + show system 对时。深挖：`swlog appid slNi subapp macmove level debug2` → show log swlog | grep MACMOVE。
3. **BPDU 收发统计**（p23）：debug stp bpdu-stats <实例> start → show → stop；某端口只 tx 无 rx = 单向链路或对端不发。
4. **设计期防故障九原则**（p24）：priority 明确定根；记录每个 VLAN 哪些口该阻塞；尽量少阻塞口；**不调 STP 定时器**（只许动桥优先级与端口 cost/priority）；不用 VLAN 1；修剪 VLAN；配 Loop Guard/UDLD/LBD/Root Guard/qos user-port filter bpdu；尽量依赖 L3；单个阻塞口误转发可瘫痪大半个网络。
5. **DHL（双归属链路）判据**（g21/c05）：两条链路 native（untagged）VLAN 必须一致才能配对做 VLAN 分担；状态 forwarding/dhl-blocking 属正常分担，双双 blocking = native VLAN 不一致。
6. **协议背景**（g15-g17）：STP/RSTP/MSTP 与 flat/per-VLAN 模式；TCN 每 1-4 分钟一次 = 频繁拓扑变化，追查从哪个 VLAN/端口进来；SPB（g41）与 ERPv2（g42）是替代性 L2 冗余方案（无 STP 阻塞）。

## A1 · 书中案例（LAB 故障根因）

- **c04（LAB2 案例2，p199-203）**：6860-B 刷 "DoS type invalid ip ... to 224.0.0.18"、CPU 98%、访问迟缓。真根因：6870-A 上 VLAN 278 STP 状态 OFF，端口 1/1/15、1/1/16 直连成 L2 环，本机 VRRP 通告（源 MAC 00:00:5e:00:01:02）被环回从错误端口收回触发 invalid-ip 告警。修复：先禁两端口 → spantree Vlan 278 admin-state enable → 端口放回 vlan 1 重新 enable → 日志调回 info。判别口诀：DoS invalid ip 刷屏 + CPU 高 + 源 MAC 是 00:00:5e → 先查环，不当攻击处置（ce19）。
- **c05（LAB3 案例1，p223-226）**：6360 两条 DHL 链路所有相关 VLAN 全 dhl-blocking。排查发现 6860-B 侧 vlan 57 在链路 A tagged、在链路 B untagged——两条 DHL 链路 native VLAN 不一致。修复：统一 `vlan 57 members linkagg 8 untagged` 后恢复分担。判据：DHL 排障先核两条链路 native VLAN 一致性。

## A2 · 触发场景（含与相邻 skill 的区分）

- 触发：广播风暴、CPU 高 + DoS 告警、MAC 在两端口漂移、链路利用率异常高、STP 拓扑变化计数暴涨、MSTP region 行为异常、DHL 全 blocking。
- 区分：单端口 down/错配 → l2-connectivity；VC 成员口/VFL 问题 → virtual-chassis；环路期间管理面不可达必须走 console/EMP（ce01）属本 skill 的前置动作。DoS 统计判读（g40）在本 skill，但真实攻击处置需结合 OVNA（ovna skill）。

## E · 可执行步骤

1. 环路疑似时：**先占住 console 口**（Telnet/SSH 大概率不可用；远程经 EMP IP SSH 兜底）。
2. 应急止血：`interfaces <本应阻塞端口> admin-state disable`。
3. 执行八步清单（f08）：拓扑 → swlog debug2 + flash-file-size 12500 → MAC 重学核查 → show spantree vlan 全网核对模式/根/阻塞口 → timers/Topology Changes → 端口状态比对 → MAC flapping 三板斧 → MSTP 三致性。
4. MAC 漂移确认：`swlog appid slNi subapp macmove level debug2`；`show log swlog | grep MACMOVE` 看 INS/DEL 端口交替。
5. BPDU 疑似丢失：`debug stp bpdu-stats 1 start` → `debug stp bpdu-stats show 1` → stop。
6. MSTP 三致性检查：region 名一致；`show spantree msti vlan-map` 核 VLAN-MSTI 映射；MSTI 内 VLAN 全部在互联链路 tagged（`show vlan members` 逐链路核端口类型）。
7. DHL：`show vlan members` 比对两条链路的 untagged VLAN；不一致则 disable 链路两侧 → 统一 native VLAN → enable。
8. **收尾强制项**：`swlog appid slNi subapp macmove level info`（及所有调过的 appid）调回 info（ce04）。

## B · 边界与陷阱

- **ce01**：环路风暴把管理面打挂，不占 console 就只能干等；EMP 是带外兜底。
- **ce19**：DoS invalid ip + CPU 高 + 00:00:5e 源 MAC → 是环不是攻击，先开 MACMOVE 日志查漂移。
- **ce17**：随手调 STP 定时器"优化收敛"会影响直径与稳定性；唯二可调的是桥优先级与端口 cost/priority。
- **ce16**：MSTI 的 VLAN 没在互联链路 tagged，后果是"MSTP 行为不可预测"而非报错——比直接故障更难查。
- debug stp bpdu-stats 输出量大，限定实例、尽快 stop。
- Auto Fabric 开启时 spantree 模式被强制 flat（p178 附注），核对模式前先确认该开关。
- 阻塞口文档是排障前提：平时就要在网络图上标出每个物理环与破环的阻塞口（p20）。

---
来源条目: f08, p20, p21, p22, p23, p24, p25, ce01, ce16, ce17, ce19, g15, g16, g17, g18, g20, g21, g40, g41, g42, c04, c05
