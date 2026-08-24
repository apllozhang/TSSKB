---
name: MSTP 多生成树与负载分担
description: 需要在 OmniSwitch 上部署 MSTP（MST 域/实例/VLAN 映射）或用 MSTI 实现 VLAN 组流量分担时使用本技能。
source_book: DT00XTE216 OmniSwitch LAN Core Switching Ed15
---

## R（触发场景）
- 大量 VLAN 需要生成树，1x1 per-VLAN 模式开销过大，要收敛到少量实例
- 双核心/三核心拓扑希望不同 VLAN 组走不同链路（负载分担）
- 排查"交换机不同域/实例行为不一致"的 MST Region 配置问题

## I（核心理念）
MSTP（802.1s）把多个 VLAN 映射到至多 16 个 MSTI，用 CIST（实例 0）承载全部实例的单一 BPDU。同域三要素是 region name、revision level、VLAN-to-MSTI 映射，必须完全一致；对外整个 region 表现为一台交换机。负载分担的本质是让不同 MSTI 选不同根桥（差异化优先级）。

## A1（行动框架）
1. 切模式：`spantree mode flat` → `spantree mst region name lab_region` → `spantree mst region revision-level 1` → `spantree protocol mstp`（<<<PAGE 141>>>）
2. 建实例并映射 VLAN：`spantree msti 1` / `spantree msti 2` + `spantree msti 1 vlan 20` / `spantree msti 2 vlan 30`（<<<PAGE 143>>>）
3. 验证：`show spantree msti vlan-map`（如 CIST: 1-19,21-29,31-4094）（<<<PAGE 143>>>）
4. 负载分担：`spantree msti 1 priority 16384`（sw7）/ `spantree msti 2 priority 16384`（sw8），或官方示例 `spantree cist priority 4096 / msti 1 priority 4096 / msti 2 priority 8192` + 端口级 `spantree msti 1 1/1/1 priority 1`（<<<PAGE 146>>>、<<<PAGE 128>>>）
5. 回退：`spantree mode per-vlan` + `no spantree mst region name` + `no spantree msti 1/2`（<<<PAGE 149>>>）

## A2（进阶应用）
- 三交换机分担：A/B/C 各在一个 MSTI 上 priority 4096 做根；`show spantree mst port` 显示 DESG FORW / ALT BLK 角色分配（<<<PAGE 130>>>、<<<PAGE 129>>>）
- 开销与桥 ID 语义：MST 用 32 位路径开销（对比 802.1d/w 的 16 位）；bridge priority = 配置值 + MSTI 号（32768+1=32769）（<<<PAGE 142>>>、<<<PAGE 148>>>）
- 未映射 VLAN 自动归属 MSTI 0（IST）；hop count 最大 40、默认 20（<<<PAGE 116>>>、<<<PAGE 118>>>）

## E（实证案例）
- C-10 6360 虚拟机箱 + MST 域 + 双实例负载分担全生命周期含验证与还原（<<<PAGE 141>>>-<<<PAGE 149>>>）
- C-12 三交换机流量分担，`show spantree mst port` 输出 DESG FORW / ALT BLK（<<<PAGE 130>>>、<<<PAGE 129>>>）

## B（边界与陷阱）
- 1x1 与 MSTP 不能共存，必须先 `spantree mode flat`；实验后记得还原 per-vlan（<<<PAGE 143>>>、<<<PAGE 149>>>）
- 优先级必须是 4096 的倍数（8192、12288…61440），随意填值不生效（<<<PAGE 146>>>）

## 来源
- framework·F-08 MSTP 配置六步法（<<<PAGE 121>>>-<<<PAGE 126>>>）
- principle·P-16 Region 三要素（<<<PAGE 117>>>、<<<PAGE 123>>>）
- principle·P-17 MSTI/CIST 关系（<<<PAGE 116>>>、<<<PAGE 118>>>、<<<PAGE 119>>>）
- principle·P-18 32 位开销与优先级语义（<<<PAGE 142>>>、<<<PAGE 148>>>）
- principle·P-19 负载分担设计（<<<PAGE 126>>>、<<<PAGE 130>>>）
- case·C-10/C-11/C-12；counter·X-08/X-09
