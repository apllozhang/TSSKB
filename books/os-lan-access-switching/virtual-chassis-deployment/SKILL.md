---
name: virtual-chassis-deployment
description: 何时用：组建/运维 OmniSwitch Virtual Chassis（堆叠）——选举控制、VFL、主从同步、脑裂防护或 ISSU 升级时。
source_book: DT00XTE215EN Access Switching
---

# Virtual Chassis 部署与运维

## R · 原文引用

"Assign a Chassis ID / Assign a Chassis Group ID and a Priority / Configure VFL link & ports - Automatic or static / Restart Chassis to Virtual-Chassis Directory. Assign a Chassis Group number: Must be the same on all the switches belonging to the Virtual Chassis. Define a Priority: Between 0 to 255, switch with the highest priority is elected Master."（p105-107）

"Master/Slave election based on virtual chassis protocol (ISIS-VC): Highest chassis priority value / Longest chassis uptime (if difference in uptime >10 mn) / Smallest Chassis ID value / Smallest chassis MAC address"（p95）

"The former Slave chassis will shutdown all its front-panel user ports to prevent duplicate IP and chassis MAC addresses in the network."（p99-100）

## I · 方法论骨架

VC = 多台交换机经 VFL 互联后呈现为单一逻辑设备（单管理点、免 STP/VRRP、免许可）。核心骨架：
- **静态部署五步**：唯一 chassis ID → 相同 chassis-group + priority（0-255 预定 master）→ VFL（auto 端口自动检测 / static 显式建 VFL ID 挂口）→ write memory → 从含 vcsetup.cfg 的目录 reload。
- **选举链**（ISIS-VC）：priority 最大 → uptime 最长（差 >10 分钟才比）→ chassis ID 最小 → MAC 最小。固定 master 就显式调大 priority。
- **同步**：配置只存 master；`write memory flash-synchro` 或 `copy running certified` 把镜像+配置同步到所有 slave 的 certified（show running-directory 看 SYNCHRONIZED）。
- **脑裂防护两条路**：带外 RCD（EMP 口互发通告，split 时前 slave 关全部用户口、状态 Split-Topology）；带内 VCSP（成员各出一口到 helper 交换机组成 VCSP LAG）。
- **ISSU**：新代码放独立目录 → issu 命令分发 → 按 chassis ID 从小到大逐台重启。

## A1 · 书中案例（Lab 配置精要）

6360 双机 Lab（p112-122）：A 端 `virtual-chassis chassis-group 1` + `chassis-id 1 configured-chassis-priority 200`；B 端 `configured-chassis-id 2`；`virtual-chassis vf-link-mode auto` + `auto-vf-link-port 1/1/27`（P10 型号用 1/1/11）；`interfaces 1/1/27-28 admin-state enable`；write memory 后各 reload（priority/chassis-id 改动必须重启生效；B 端 write memory 弹 "Chassis 1 missing! Configuration associated with missing chassis will be erased permanently! Confirm (Y/N)" 警告）。监控：show virtual-chassis topology（"+"=未保存）、show virtual-chassis vf-link member-port、show virtual-chassis consistency、`ssh-chassis admin@2` 跳到从机。

## A2 · 触发场景（含与相邻 skill 的区分）

- 接入层多机合一管理、跨机箱端口聚合、免 STP/VRRP——本 skill。
- 只是两台核心做网关冗余（不组堆叠）→ ip-services-basic 的 VRRP。
- 单机目录保存/回滚语义 → aos-config-management（flash-synchro 的 VC 扩展语义在本 skill）。

## E · 可执行步骤

1. 规划：chassis ID 全 VC 唯一；chassis-group 全员相同；master 候选 priority 调大（如 200）。
2. 选 VFL 模式：auto（两端均须 auto 候选口；6360-24 用 27/28、6360-48 用 51/52、6900 X/T 每槽最后 5 口、9900 仅静态）或 static（vf-link ID + 成员口）。
3. 逐台：virtual-chassis chassis-group N → chassis-id X configured-chassis-priority P → vf-link 配置 → 激活端口 → write memory → reload。
4. 验证：show virtual-chassis topology / consistency；ssh-chassis 登成员。
5. 配置同步：write memory flash-synchro。
6. ISSU 升级：上传新代码+vcsetup.cfg+vcboot.cfg 到 issu_dir → issu 命令 → 等待按 chassis ID 升序逐台重启。
7. 启用脑裂防护：带外确认 EMP/RCD；带内 `virtual-chassis split-protection [helper] admin-state/linkagg`。

## B · 边界与陷阱

- **priority / chassis-id 改动须 reload 才生效**：配 200 后 Oper Pri 仍 100，Lab 环境留 4-5 分钟重启窗口。
- **VC 中 write memory 的清除警告**：拓扑变化（成员缺失/chassis-id 改动）时确认 Y 会永久清除缺失机箱的配置段，看懂再按。
- **新 master 不让位**：原 master 回归不重选，以 slave 身份回归（MAC retention 恒开）——属预期行为不是故障。
- slave 收到新镜像/配置后须重启才生效。
- master 故障只影响自身，slave 流量不受损；但 VFL 全断而无 RCD/VCSP 会双活冒 IP/MAC。

---
来源条目: f03, f04, f05, p13, p14, p15, p16, p17, ce04, ce07, c03, g08, g09, g10, g11, g12, g13, g40
