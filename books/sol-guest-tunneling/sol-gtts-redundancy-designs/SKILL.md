---
name: GTTS 冗余设计（R0-R4 五级阶梯与选型）
description: 需要为 GTTS 隧道聚合交换机做高可用设计时使用：R0 无冗余/R1 Hairpin 链路聚合/R2 Primary-Backup/R3 Virtual-Chassis/R4 每 SSID 一对交换机的对比选型、收敛时间量级、Preemption 抢占与对应 CLI 配置（linkagg/service sap）。
source_book: Guest Traffic Tunnelling Services Application Note (23032701, April 2023)
---

## R（触发场景）
- GTTS 聚合交换机不能成为单点故障，需选择冗余等级
- Hairpin 端口故障或带宽不足，需链路聚合扩容
- 要求故障切换秒级（Primary/Backup）或亚秒级（Virtual-Chassis）
- 多 SSID 关键业务要求地理级容灾（每 SSID 独立交换机对）
- Primary 恢复后需要会话回切（Preemption 规划）

## I（核心理念）
冗余五级阶梯（F2，<<<PAGE 14-19>>>）：R0 单交换机+单 Hairpin，交换机/Hairpin/连接三单点任一故障 SSID 全灭（X7）；R1 给 Hairpin 两侧各建 linkagg——只修端口级故障并顺带翻倍带宽，不修整机与连接（X8），可与 R2/R3/R4 叠加；R2 SSID 填 Backup GRE Server IP，整机切换秒级收敛，备机配置=主机（VPN ID 必须一致），Preemption 可回切（P16）；R3 两机组 Virtual-Chassis + 跨成员 linkagg，亚秒收敛，Hairpin/连接/整机全覆盖；R4 每 SSID 一对交换机（建议异地），连续故障或整站宕机只伤单个 SSID，最高等级。选型主线：预算从低到高、收敛从秒到亚秒、爆炸半径从全网到单 SSID。

## A1（行动框架）
1. 定可用性目标：容忍秒级中断→R2；要求亚秒不中断→R3；地理容灾/按业务分级→R4
2. 任何等级都叠 R1：SAP/ACCESS 各建 linkagg（端口冗余+带宽扩容，Hairpin 数不限 2 条）
3. R2：备机复制主机配置（vpnid 一致）→ SSID 填 Backup IP → 视需要开 Preemption+倒计时
4. R3：先组 VC → 跨成员建双 linkagg → service/sap 指向 linkagg
5. R4：每 SSID 独立交换机对（异地）→ 重复 R2 或 R3 配置 → 各 SSID 指向各自交换机
6. 容量校验：VC 不抬高单机隧道数上限（1000/2000/6000 按机型，<<<PAGE 8>>>）

## A2（操作步骤）
- **R1 Hairpin 冗余**（C6，<<<PAGE 15-16>>>）：
  ```
  linkagg lacp agg 1 size 2 admin-state enable
  linkagg lacp agg 1 name "GTTS-HAIRPIN-1"
  linkagg lacp port 1/1/25 actor admin-key 1
  linkagg lacp port 1/1/26 actor admin-key 1
  linkagg lacp agg 2 size 2 admin-state enable
  linkagg lacp agg 2 name "GTTS-HAIRPIN-2"
  linkagg lacp port 1/1/27 actor admin-key 2
  linkagg lacp port 1/1/28 actor admin-key 2
  service l2profile "guest-l2profile" stp drop gvrp drop mvrp drop
  service access linkagg 1 vlan-xlation enable l2profile "guest-l2profile"
  service 100 l2gre vpnid 50 stats enable vlan-xlation enable remove-ingress-tag enable
  service 100 sap linkagg 1:50
  vlan 50 members linkagg 2 untagged
  ```
  （SAP 相关配置把 port 换成 linkagg 即可）
- **R2 Primary & Secondary**（C7，<<<PAGE 16-17>>>）：备机配置与主机相同（vpnid 必须一致）→ SSID 面板填 Backup GRE Tunnel Server IP → 可选 Preemption + Preemption Countdown Timer（到期 AP 重连 Primary 并迁移全部会话）
- **R3 Virtual-Chassis**（C8，<<<PAGE 17-18>>>）：两机组 VC → 双 linkagg 跨成员（agg1=1/1/25+2/1/25，agg2=1/1/27+2/1/27）→ service/sap/vlan 配置同 R1
- **R4 每 SSID 一对交换机**（C9，<<<PAGE 18-19>>>）：建多套 VC → 各配 SAP/ACCESS linkagg → 每个 SSID 分别配置指向各自交换机对

## E（实证案例）
- R1/R3 的完整可用 CLI 配置（端口/描述/ID 齐全，<<<PAGE 15-18>>>）
- R2 收敛时间实测口径：Primary→Secondary failover "a few seconds"；R3 VC "sub-second"（<<<PAGE 16-17>>>）
- R4 异地部署原则：交换机对不同地点防地理性故障，仅对应 SSID 受影响（<<<PAGE 18>>>）

## B（反例与坑）
- R0 上生产：三个单点（整机/自环线/连接）任一故障 GTTS SSID 不可用（X7，<<<PAGE 14>>>）
- 把 R1 当整机冗余卖：它只保 SAP/ACCESS 各 1 端口故障无感，交换机与连接仍单点（X8，<<<PAGE 15>>>）
- R2 备机 vpnid 与主机不一致：AP 靠 VPN ID 开隧道，不一致则切换后隧道建不起来（X11，<<<PAGE 16>>>）
- 以为 VC 能抬高隧道数上限：上限按单机机型定档，VC 不增加（X6，<<<PAGE 8>>>）
- 忘开 Preemption 规划回切：Primary 恢复后流量滞留 Secondary，主备角色与预期漂移（<<<PAGE 10>>><<<PAGE 17>>>）
- 单 Hairpin 带宽瓶颈：SSID 吞吐=Hairpin 线速，高带宽场景必须多 Hairpin/linkagg（X12，<<<PAGE 8>>>）

来源：Guest Traffic Tunnelling Services Application Note，GTTS redundancy designs 章（p14-19）
