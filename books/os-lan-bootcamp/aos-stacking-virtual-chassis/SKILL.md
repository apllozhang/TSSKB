---
name: 堆叠与虚拟机箱（Stacking R6 / Virtual Chassis R8）
description: 需要规划或配置 OmniSwitch 堆叠（Slot-ID/角色选举/同步/takeover）、R8 Virtual Chassis（VFL/Master 选举/防脑裂 RCD-VCSP）、auto-VC 零接触组网，或排障堆叠脑裂/槽号冲突时使用本技能。
source_book: DT00CTE120 OmniSwitch R6/R8 Bootcamp Issue 25
---

## R（触发场景）
- 多台同家族交换机需要单一 IP 管理、设备级冗余
- 堆叠出现 Slot-ID 冲突（Pass-Through/DUP-SLOT）需要修正槽号
- 计划 takeover 主备切换演练，或堆叠拆分
- R8 6900/6860 要建 Virtual Chassis（含出厂 auto-VC 流程）
- VFL 断裂担心双 Master 脑裂（同 IP 同 MAC 冲突）

## I（核心理念）
堆叠把 2-8 台同家族交换机变成一个管理实体，四角色 Primary/Secondary/Idle/Pass-Through，Slot-ID 冲突时后来者进 Pass-Through（不阻流量但不成栈）（P38/P39，<<<PAGE 251-255>>>）。R8 的 Virtual Chassis 更进一步：多台物理机经 VFL 互联成单一路由器/网桥，接入-核心之间免 STP/VRRP（P46，<<<PAGE 290>>>）。两个体系共同的纪律是"切换前必须同步"（P42，<<<PAGE 260>>>）和"原主回来不重选举、MAC retention 恒开"（P50，<<<PAGE 297>>>）。脑裂是 VC 最大风险——两 Master 同 IP 同 MAC 会引发网络级故障，须用 RCD/VCSP 双保险（P53，<<<PAGE 306-307>>>）。

## A1（决策/选型）
1. 冗余方案定位：STP 仅 50% 带宽 → LACP 仅链路冗余 → VC 链路+设备冗余+统一管理 → DHL 链路+设备冗余 100% 带宽（F16，<<<PAGE 481>>>）
2. 机型混堆规则：仅同家族可堆叠；6450-10 只能与 6450-10 混堆、不支持远程堆叠；6350-10/P10 不支持堆叠（<<<PAGE 251-253>>>）
3. VC 规格：6900 最多 6 台 mesh、5 VFL/机箱、16 端口/VFL；6860 最多 8 台 ring、专用 2x20G VFL 口；6860/6865 混合 VC 上限仍 8 台 ring（P51/P52，<<<PAGE 299-301>>>）
4. 防脑裂选型：有 EMP 口用 RCD（周期通告）；无 EMP（如 6860）用 VCSP（经 helper 链路聚合发 PDU）（P53，<<<PAGE 306-307>>>）

## A2（操作步骤）
1. 堆叠槽号修正：全部写 boot.slot.cfg slot 1 同时上电 → `show stack topology` 见 PASS-THRU DUP-SLOT → `stack set slot 1001 saved-slot 2`（逐台）→ `reload all` → 验证 1 PRIMARY/2 SECONDARY/3-4 IDLE（C10，<<<PAGE 251-262>>>）；无 boot.slot.cfg 时按 MAC 法（15 秒内同时上电）或 uptime 法分配（P40，<<<PAGE 256>>>）
2. 同步与切换：`write memory` → `copy working certified flash-synchro` → `takeover` → `show stack topology` 确认角色迁移、`show running-directory` 看 Flash SYNCHRONIZED（C11/P43，<<<PAGE 264-286>>>）
3. MAC Retention：`mac-retention status enable` + `mac-retention dup-mac-trap enable`；takeover 后 `show mac-retention status` 显示 Retained；`mac release` 主动释放（C12/P44，<<<PAGE 273, 271-272>>>）
4. 拆堆叠：`stack set slot N mode standalone`（逐台）→ `rm boot.slot.cfg` → 恢复 labinit 配置 → `reload working no rollback-timeout`（C11，<<<PAGE 264-286>>>）
5. VC 建立（R8）：vcsetup.cfg（机箱 ID/组/VFL）+ vcboot.cfg 双文件须在运行目录（P48，<<<PAGE 294>>>）；Master 选举五级：现任 Master > chassis priority > 最长在线 > 最小 Chassis ID > 最小 MAC（P49，<<<PAGE 296>>>）
6. auto-VC 出厂流程：boot 提示 "Do you want to disable auto-configurations [Y/N]?" 输 N → 自动 VFL/Chassis ID 协商（无 vcsetup.cfg 时自动选 Chassis ID、最低 MAC 为 Master）→ `show stack topology` 查看（C13/P181，<<<PAGE 937-940>>>）
7. 禁 VC/恢复：`no virtual-chassis vf-link 0 member 2/1` 逐口删 → 恢复 `reload from virtual_dir no rollback-timeout`（C13，<<<PAGE 937-940>>>）
8. SSP（R6 堆叠分裂保护）：堆叠链双断时备份子堆叠经 helper 收 SSP PDU 后关用户端口、不升主（P45，<<<PAGE 275>>>）

## E（实证案例）
- C10 Slot-ID 选举三法对比（saved-slot/MAC/uptime）（<<<PAGE 251-262>>>）
- C11 同步→takeover→拆堆叠全流程（<<<PAGE 264-286>>>）
- C13 6900 auto-VC 与禁用恢复（<<<PAGE 937-940>>>）

## B（反例与坑）
- 堆叠不超过 8 台且版本必须一致（X25，<<<PAGE 261>>>）；无法登录 Idle/Pass-Through 单元（X26）；Secondary 上仅允许 takeover 等极少数命令（X27，<<<PAGE 262>>>）
- 槽号必须唯一且建议从 1 连续分配（X28，<<<PAGE 279>>>）；takeover 前必须完成同步（X29）、`reload all` 可能落在 certified 分区（X30，<<<PAGE 260>>>）
- 6450-10 混堆限制（X4）、6350-10/P10 不可堆叠（X5）、6450-10/P10 不支持远程堆叠（X6，<<<PAGE 252-253>>>）
- VC 仅限 AOS R8 且须同机型（X32，<<<PAGE 290>>>）；VC 脑裂双 Master 同 IP 同 MAC（X33，<<<PAGE 305>>>）
- 6860 无 EMP 口故不能用 RCD 防脑裂（X11，<<<PAGE 306>>>）；专用 VFL 口不能当普通口（X9，<<<PAGE 300>>>）；6900-T 固定 10GBase-T 口不能作 VFL（X10，<<<PAGE 299>>>）
- VC 中 write memory 在拓扑变化时受保护警告（X31/X89，<<<PAGE 317>>>）；VC 成员含非 E 型 6860 仍需有效 license（X86，<<<PAGE 59>>>）；V72/C32 用 Yos.img（X84，<<<PAGE 86-87>>>）

## 来源
- principles·P38-P53/P181；frameworks·F12/F16；cases·C10-C13；counter-examples·X4-X6/X9-X11/X25-X33/X84/X86/X89
