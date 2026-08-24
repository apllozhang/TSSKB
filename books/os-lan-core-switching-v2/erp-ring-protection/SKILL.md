---
name: ERP 以太网环网保护部署
description: 需要在 OmniSwitch 上部署/排查 ERPv2 环网（主环、子环、RPL、WTR 回切）时使用本技能。
source_book: DT00XTE216 OmniSwitch LAN Core Switching Ed15
---

## R（触发场景）
- 园区/汇聚层需要二层环网并提供约 50ms 故障倒换，不想依赖 STP 慢收敛
- 现网 ERP 环出现反复倒换或回切抖动，需要定位 RPL/WTR/Guard 配置问题
- 需要在主环下挂子环（Laddered/Subtending）扩展覆盖范围

## I（核心理念）
ERPv2 用"稳态阻塞唯一一条 RPL 链路"换取环内无环；故障时 R-APS SF 消息触发 RPL Owner 解阻塞倒换，恢复时靠 NR + WTR 定时器（默认 5 分钟）防抖回切。整个环是一台协同的状态机，任何一台交换机的 Service VLAN/MEG Level/RPL 配置不一致都会破坏这个协同。

## A1（行动框架）
1. 建环并指定 Service VLAN 与 MEG Level（全网一致，0-7）：
   `erp-ring 1 port1 1/1/3 port2 1/1/27 service-vlan 1001 level 2`（<<<PAGE 53>>>）
2. 在 RPL Owner 上配置（必须在环未 enable 时）：`erp-ring 1 rpl-node port 1/1/27`，可选 `erp-ring 1 wait-to-restore-timer 1`（<<<PAGE 55>>>）
3. 加入受保护 VLAN：环配置中带 Protected VLAN（如 20/30），子环 VLAN 跨环打 tagged（<<<PAGE 59>>>）
4. 启用：`erp-ring 1 enable`；验证 `show erp`（Ring State: idle，Ring Node: rpl/non-rpl）（<<<PAGE 56>>>）
5. 子环：单口接入用 `erp-ring 2 sub-ring-port 1/1/5 service-vlan 1002 level 2` + `erp-ring 2 rpl-node port 1/1/5`；`show erp` 中子环只有一个 ring port（<<<PAGE 59>>>-<<<PAGE 60>>>）
6. 断链测试：`interfaces 1/1/3 admin-state disable`，持续 ping 验证不中断（<<<PAGE 58>>>）

## A2（进阶应用）
- 状态机三态：idle（RPL 阻塞）/ Protection（故障转发）/ Pending（WTR 计时中）；稳态 NR/RB、故障 SF、恢复 NR+WTR（<<<PAGE 40>>>-<<<PAGE 42>>>、<<<PAGE 56>>>）
- 子环借主环虚通道闭合，R-APS 用子环 Service VLAN 的 S-tag 传递（<<<PAGE 43>>>）
- Guard Timer 默认 50 厘秒，丢弃过期 R-APS 防误倒换（<<<PAGE 56>>>）
- 实验回收：`rm -r labERP` → `reload from working no rollback-timeout`（<<<PAGE 62>>>-<<<PAGE 63>>>）

## E（实证案例）
- C-01 主环 4 节点全流程：建目录→VLAN 1001 Service/20/30 Protected→RPL→enable→`show erp` idle→断链 ping 不中断（<<<PAGE 53>>>-<<<PAGE 58>>>）
- C-02 子环 sub-ring-port 单口接入，RPL 在子环上唯一（<<<PAGE 59>>>-<<<PAGE 61>>>）

## B（边界与陷阱）
- RPL 缺失或多个 = 非法配置；RPL 只能配在已存在且未 enable 的环上（<<<PAGE 55>>>）
- 每环建议最多 16 节点，环数受机型限制，超规模需查 Network Configuration Guide（<<<PAGE 55>>>）

## 来源
- framework·ERP 配置五步法（<<<PAGE 45>>>-<<<PAGE 49>>>）
- framework·ERP 状态机三态模型（<<<PAGE 40>>>-<<<PAGE 42>>>、<<<PAGE 56>>>）
- principle·P-01 RPL 阻塞机制（<<<PAGE 37>>>、<<<PAGE 38>>>、<<<PAGE 40>>>）
- principle·P-02 R-APS 消息体系（<<<PAGE 38>>>、<<<PAGE 41>>>、<<<PAGE 42>>>）
- principle·P-03 WTR/Guard 定时器（<<<PAGE 42>>>、<<<PAGE 56>>>）
- principle·P-04 子环虚通道（<<<PAGE 43>>>）
- principle·P-05 环规模与端口约束（<<<PAGE 55>>>）
- case·C-01/C-02/C-03；counter·X-01/X-02
