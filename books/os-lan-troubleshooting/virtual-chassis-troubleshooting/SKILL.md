---
name: virtual-chassis-troubleshooting
description: 何时用：Virtual Chassis（VC 堆叠）组建失败、成员掉线、VFL 不 up、NOK 码报错、vcsetup.cfg 解析失败、脑裂防护。
source_book: DT00XTE221EN OmniSwitch LAN Troubleshooting
---

# Virtual Chassis（虚拟机箱）排障

## R · 原文引用

> "-> show virtual-chassis topology ... -> show virtual-chassis consistency ... -> cat vcsetup.cfg ... -> debug show virtual-chassis status" (p162)

> "Upon boot-up, a switch will read its local vcsetup.cfg file and attempt to connect to the other neighbor switches ... they will discover the topology, elect a Master ... All Slaves, if they do not have a local copy of vcboot.cfg, or if their local copy does not match ... will download the vcboot.cfg from the Master chassis and reboot" (p161)

> "NOK_08: There are no virtual-fabric member ports configured on this switch ... NOK_17: The virtual-chassis manager protocol did not discover any peer switch within the discovery time window (i.e. 4 minutes)" (p195)

> "WARNING - Virtual chassis topology change detected. Chassis 2 missing! Configuration associated with missing chassis will be erased permanently! Confirm to continue (Y/N)" (p197)

## I · 方法论骨架

1. **四层递进排障**（f09）：① show virtual-chassis topology（角色/运行状态/Chassis ID/Priority/Group）→ ② show virtual-chassis consistency（核带星号必一致项：Chassis Type、Chas ID、Group、Hello Interval、Control Vlan、License）→ ③ 逐台 cat vcsetup.cfg 比对（chassis-id、vf-link-mode、member-port、chassis-group、EMP 地址）→ ④ debug show virtual-chassis status 按 L0-L8 层级定位失败层，对照 NOK 码。辅助：show virtual-chassis vf-link、debug show virtual-chassis connection、/flash 下 vcsetup.cfg.*.err 错误文件（含解析失败的行号与原因）。
2. **启动与同步机制**（p18）：开机读本地 vcsetup.cfg → VFL 连邻居 → 交换参数、发现拓扑、选举 Master → slave 的 vcboot.cfg 缺失或不一致时从 Master 下载并以它重启。Auto-VC：出厂新机无 vcsetup.cfg 时对 auto VFL 端口自动检测、自动分 VFL ID/chassis-id 并建组。
3. **NOK 码速查**（p19）：NOK_08=没配 VFL 成员口；NOK_09=成员口没 operationally up；NOK_14=配置的 VFL 链路未全部 up（必须全 up 才 OK）；NOK_17=4 分钟发现窗口内没发现对等体（无对端/VFL 不通/VCM 协议包不通）。
4. **脑裂防护**（g13）：VFL 双断导致重复 MAC/IP 两套 Master。RCD（带外，经 EMP 口）与 VCSP（带内，需 helper 交换机）检测分裂；检测到后非 Master 侧自动进 Protection 模式关闭所有用户口。堆叠平台对应 SSP。EMP 管理口双重价值：带外访问 + RCD 承载（g12）。
5. **背景参数**（g10/g11/g14）：规模上限按机型（8×OS6560、4×OS6360、6×OS6900、2×OS9900）；Master 选举：最高优先级 → 最长 uptime（差>10 分钟）→ 最小 chassis ID → 最小 MAC；VFL 内部以 LACP 聚合，速率不可混用；ISSU 按 Chassis ID 顺序逐台升级后 Master takeover。

## A1 · 书中案例（LAB 故障根因）

- **c03（LAB2 案例1，p191-198）**：6360 两台组 VC 不工作。show virtual-chassis topology 各自成 Master 单机；debug status 报 NOK_08/09/14/17 链；cat vcsetup.cfg.1.err 给出确切原因——A 台 "vf-link-mode static" 在 stackport 平台不支持；B 台同样的 static 错误外加 member-port 3/1/27 与本机 chassis-id 2 不一致（应为 2/1/27）。修复：A 台改 `virtual-chassis vf-link-mode auto` → write memory（chassis 2 missing 警告确认）→ B 台重写 vcsetup.cfg（auto + auto-vf-link-port 2/1/27、2/1/28）→ reload from working no rollback-timeout → 验证 1=Master/2=Slave Running。

## A2 · 触发场景（含与相邻 skill 的区分）

- 触发：VC 建不起来、成员机箱掉线、VFL 口不 up、debug status 出 NOK 码、vcsetup.cfg 报错、ISSU/升级后 VC 异常、疑似脑裂。
- 区分：单业务口 down → l2-connectivity；整机模块 DOWN/微码问题 → boot-system；VC 内链路聚合成员口 down 的日志因果链见 ovna skill 的 c12。VC 故障常表现为"多台同时异常"，先 show virtual-chassis topology 判断是不是 VC 层问题。

## E · 可执行步骤

1. show virtual-chassis topology：确认每台角色与运行状态（是否各自成 Master）。
2. show virtual-chassis consistency：核对带星号参数是否一致。
3. 逐台 `cat /flash/working/vcsetup.cfg` 比对关键行；检查 /flash 下是否有 vcsetup.cfg.*.err 文件——有则直接按文件中的 ERROR 行定位。
4. `debug show virtual-chassis status` 按 L0-L8 看哪层 NOK，对照 NOK 码表：NOK_08 查 `show virtual-chassis vf-link member-port | grep "<chassis-id>/"`；NOK_09 加查 show interfaces port；NOK_17 查对端是否存在与 VFL 连通性。
5. 修复 vcsetup.cfg：用 CLI 生成或严格按模板；member-port 必须以本机 chassis-id 开头；改完 cat 复核再 reload from working。
6. 怀疑脑裂：查 EMP 上 RCD 通告 / VCSP helper 配置；Protection 模式的子 VC 用户口全关是设计行为，先恢复 VFL 再恢复业务。
7. 变更后 write memory 遇 "Chassis N missing ... erased permanently" 警告：停下确认拓扑变化是否预期再 Y。

## B · 边界与陷阱

- **ce07**：stackport 平台（6360 等）不支持 vf-link-mode static，配置直接解析报错；必须 auto + auto-vf-link-port。
- **ce08**：VFL member-port 第一段必须等于本机 chassis-id——从其他配置复制粘贴后忘改编号是典型错。
- **ce06**：手工编辑 vcsetup.cfg 越界会进 error mode，前面板所有用户口（含 VFL 成员口）保持 disabled，表现为整机瘫；文件内 [SAVED INFO] 区绝对不动。
- **ce18**：VC 变更/半拆状态 write memory 弹 chassis missing 警告随手确认 Y → 缺失机箱配置被永久删除。
- VFL 链路速率不可混用（p515）；多条 VFL 链路必须全部 up 才报 OK（NOK_14 判读）。
- 无 EMP 机型组 VC 需指定管理 VLAN+IP 接口替代 EMP 做 RCD（p534）。

---
来源条目: f09, p18, p19, ce06, ce07, ce08, ce18, g09, g10, g11, g12, g13, g14, c03
