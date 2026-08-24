---
name: STP 防环与链路聚合配置
description: 当网络存在冗余链路需要防环、调 STP 优先级做负载分担，或需要配置静态/LACP 聚合提升上联带宽时使用本技能。
source_book: DT00XTE301 LAN & WLAN Installation & Configuration for SMB
---

## R（触发场景）
- 交换机间有多条冗余链路，需要防环或做按 VLAN 的负载分担
- 上联带宽不足，要把多条物理链路聚合成一条逻辑链路
- 按模板接线后出现环路风险，需要确认防环已启用

## I（核心理念）
STP 是二层防环的底线，OmniSwitch 默认 per-VLAN 模式；RSTP/MSTP 收敛 <1 秒而老 STP 要 50 秒，无理由不用快协议。聚合分静态（仅 ALE 设备互通）与 LACP（跨厂商、LACPDU 动态协商），带宽扩展优先 LACP。per-VLAN STP 的 bridge priority 可以按 VLAN 错开阻塞端口，白拿负载分担。

## A1（行动框架）
1. STP 模式与协议：
   ```
   -> spantree mode {flat | per-vlan}
   -> spantree [cist|vlan id] protocol {stp|rstp|mstp}
   -> spantree path-cost-mode auto    // 16bit/32bit 随协议自动切换
   ```
2. 按 VLAN 调优先级做负载分担：
   ```
   -> spantree vlan 20 priority 20000      // 根桥迁移
   -> spantree vlan 200 port 2/1/1 priority 15
   ```
3. 监控验证：
   ```
   -> show spantree
   -> show spantree vlan 20 ports active
   -> show spantree ports
   ```
   （C28，<<<PAGE 243>>>–<<<PAGE 247>>>）
4. 静态聚合（仅 ALE 互通）：
   ```
   -> linkagg static agg <n> size <s> admin-state enable
   -> linkagg static port <c/s/p> agg <n>
   ```
5. LACP 动态聚合：
   ```
   -> linkagg lacp agg <n> size <s> admin-state enable
   -> linkagg lacp agg <n> actor admin-key <k>
   -> linkagg lacp port <c/s/p> actor admin-key <k>
   ```
6. VLAN 挂聚合口：`-> vlan <vid> members linkagg <n> tagged|untagged`（C28，<<<PAGE 253>>>–<<<PAGE 255>>>）

## A2（进阶应用）
- 收敛时间对照：STP(802.1d) 50 秒，RSTP(802.1w)/MSTP(802.1s) <1 秒（P25，<<<PAGE 238>>>）。
- 路径开销双体系：16bit（STP/RSTP）与 32bit（MSTP），如 1Gbps = 4 / 20000（P26，<<<PAGE 239>>>）。
- 哈希负载均衡：brief 不含 UDP/TCP 端口，extended 含四层端口、分担更均匀；6360/6465/6900 默认 brief，其余默认 extended，`hash-control extended` 显式开启（P29，<<<PAGE 259>>>）。
- 组播默认走聚合组主端口，需显式开启 non-ucast 哈希才全组分担（P30，<<<PAGE 260>>>）。
- SMB 参考拓扑：中型纯二层 = Virtual Chassis 最多 8 台 + 20G 聚合；Mesh/SPB 档 = 全三层 OSPF/BGP/SPB/PIM + 双核心 100G 堆叠（F14，<<<PAGE 491>>>–<<<PAGE 493>>>）。

## E（实证案例）
- `spantree vlan 20 priority 20000` 后 VLAN 20 根桥迁移到 SW-C，与另一 VLAN 的阻塞端口错开实现负载分担（P27，<<<PAGE 240>>>；C28，<<<PAGE 243>>>–<<<PAGE 247>>>）。
- LACP 聚合：建 agg + 设 actor admin-key，两端 key 一致即协商成功，再把 VLAN members linkagg 挂上（C28，<<<PAGE 253>>>–<<<PAGE 255>>>）。

## B（边界与陷阱）
- 物理环路未做防环会拖垮全网（广播帧持续绕圈、减速甚至中断通信）；按模板接线出现环路前必须 STOP 并与方案架构师确认 loop avoidance 已实施（CE14，<<<PAGE 494>>>）。
- 静态聚合只在 ALE OmniSwitch 之间工作；跨厂商必须用 LACP（P28，<<<PAGE 252>>>）。
- Lightning Config 前禁止把未配置交换机互联（默认同 IP 192.168.0.1 会冲突）（CE13，<<<PAGE 486>>>）。

## 来源
- case·STP/LACP 配置命令组（<<<PAGE 243>>>–<<<PAGE 247>>>、<<<PAGE 253>>>–<<<PAGE 255>>>）
- principle·STP 双模式三协议与收敛时间（<<<PAGE 238>>>）
- principle·STP 默认路径开销（<<<PAGE 239>>>）
- principle·per-VLAN STP 负载分担手法（<<<PAGE 240>>>）
- principle·LACP 动态聚合协商原理（<<<PAGE 252>>>）
- principle·哈希负载均衡 brief/extended（<<<PAGE 259>>>）
- principle·聚合口组播分担默认行为（<<<PAGE 260>>>）
- framework·SMB 标准拓扑模板（<<<PAGE 491>>>–<<<PAGE 493>>>）
- counter·物理环路未做防环拖垮全网（<<<PAGE 494>>>）
