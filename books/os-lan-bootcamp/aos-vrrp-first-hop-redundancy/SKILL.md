---
name: VRRP 首跳冗余（虚拟网关主备/抢占/Tracking）
description: 需要配置 OmniSwitch VRRP 虚拟网关主备、理解 Master_Down_Interval 与 Skew Time、Tracking 联动切换、Group 集体管理或 VRRP 双组负载分担时使用本技能。
source_book: DT00CTE120 OmniSwitch R6/R8 Bootcamp Issue 25
---

## R（触发场景）
- 网关冗余：两台三层交换机为同一 VLAN 提供虚拟默认网关
- 主备切换演练或 Master 故障后流量未切走的排障
- 上行口故障需要联动降优先级（Tracking）触发切换
- 多虚拟路由器负载分担规划

## I（核心理念）
VRRP（RFC 2338）用一个虚拟 IP + 虚拟 MAC（00-00-5E-00-01-{VRID}）把多台路由器虚拟成一台，最高优先级者为 Master 负责转发与 ARP 应答，IP 拥有者直接 Master（P99/P100，<<<PAGE 524-526>>>）。收敛的时钟设计是 Master_Down_Interval = 3×通告间隔 + Skew_Time，而 Skew_Time=(256-Priority)/256——优先级越低的 Backup 等得越久，天然错峰升主，防止多备同时抢占（P101，<<<PAGE 527>>>）。可靠性闭环靠 Tracking：跟踪口断则按策略扣优先级触发切换（P103，<<<PAGE 531>>>）。

## A1（决策/选型）
1. 首跳冗余选型：VRRP 标准协议；与 Cisco HSRP 不兼容，混布网络不能两侧各跑一个（X53，<<<PAGE 524>>>）
2. 负载分担：两个虚拟路由器互为主备，主机按不同默认网关分摊（P102，<<<PAGE 528>>>）
3. 多虚拟路由器统一管理用 VRRP Group（组内统一改优先级/通告间隔/抢占）（P104，<<<PAGE 533>>>）

## A2（操作步骤）
1. 基本主备（两台同配）：`ip vrrp 1 interface int_20` → `ip vrrp 1 interface int_20 address 192.168.20.254` → `ip vrrp 1 interface int_20 admin-state enable`（C25，<<<PAGE 529-537>>>）
2. 验证：`show ip vrrp 1`（Priority 100、Virtual MAC 00-00-5E-00-01-01）；`show ip vrrp statistics` 看 A Master/B Backup——同优先级时比 router-id（C25，<<<PAGE 529-537>>>）
3. Tracking：`ip vrrp track 3 admin-state enable priority 30 port 1/1/3` → `ip vrrp 1 interface int_20 track-association 3`；断跟踪口后优先级 100-30=70 让位（C25/P103，<<<PAGE 529-537>>>）
4. Group：`ip vrrp group 2` + `group association` 统一参数（C25，<<<PAGE 529-537>>>）

## E（实证案例）
- C25 VRRP 主备+抢占+Tracking 全流程：两台 6860 同配虚拟 IP，断跟踪口观察 Master 迁移（<<<PAGE 529-537>>>）

## B（反例与坑）
- VRRP 与 HSRP 不兼容（X53，<<<PAGE 524>>>）
- 备份路由器之间优先级应彼此不同，避免 Master 故障时同时升主（X54，<<<PAGE 527>>>）——Skew_Time 只能部分错峰，显式分层更稳
- 抢占（Preempt）默认行为与通告间隔调整要在两侧一致，否则会看到意外震荡（<<<PAGE 527, 529-530>>>）

## 来源
- principles·P99-P104；cases·C25；counter-examples·X53/X54
