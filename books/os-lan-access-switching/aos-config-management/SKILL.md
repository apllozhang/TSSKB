---
name: aos-config-management
description: 何时用：在 OmniSwitch AOS R8 上做配置保存/回滚/目录管理、备份恢复或软件镜像升级时。
source_book: DT00XTE215EN Access Switching
---

# AOS 配置管理：三目录模型、保存语义与回滚

## R · 原文引用

"Command to force reboot from CERTIFIED directory: -> reload all. Command to force reboot from WORKING directory or user defined directory: -> reload from working no rollback-timeout. * Running configuration (RAM): current operating configuration of the switch retrieved from the running directory in addition to any configuration changes made by the user."（p69-71）

"At the time of a normal boot (cold start): The switch will reboot from certified directory if contents (images and vcboot.cfg) are different from the running directory... If contents are the same, the switch will reboot from the running directory."（p81）

"sw7 (OS6860-A) -> write memory / -> copy running certified / -> write memory flash-synchro = write memory + copy running certified"（p70-71）

"IF THE OMNISWITCH IS REBOOTED WITH THE 'RELOAD ALL' COMMAND, IT WILL REBOOT FROM THE CERTIFIED DIRECTORY, NO MATTER WHAT THE CONTENT OF THE RUNNING DIRECTORY IS."（p81）

## I · 方法论骨架

AOS 用"目录式配置"而非单一 startup-config：
- **三个候选启动目录**：certified（认证基线）、working（测试暂存）、user-defined（用户自建，可多套）。每个目录 = AOS 镜像 + vcboot.cfg（启动配置）+ vcsetup.cfg（VC 参数）三件套。
- **running configuration** 在 RAM：启动目录内容 + 未保存改动。改动立即生效但重启即丢。
- **保存语义层级**：write memory（RAM→running 目录）→ copy running certified（固化基线）→ write memory flash-synchro（一步做两件事）。
- **回滚即重启**：冷启动时比较 running 目录与 certified 的镜像+vcboot.cfg，不一致自动回退 certified。
- 判断状态看 `show running-directory`：NOT SYNCHRONIZED / CERTIFY NEEDED / CERTIFIED。

## A1 · 书中案例（Lab 配置精要）

Lab 目录全流程（p79-88）：建 VLAN 2/3/99（只在 RAM）→ show running-directory 见 NOT SYNCHRONIZED → write memory 变 CERTIFY NEEDED → reload all 回退 certified、VLAN 全丢 → reload from working 找回 → certified 模式下 write memory 报错 "Write memory is not permitted when switch is running in certified mode" → mkdir lab + cp working/*.* lab（boot.md5 Permission denied 可忽略）→ reload from lab no rollback-timeout → copy running certified 固化。附 USB 备份：usb enable → usb backup admin-state enable → write memory flash-synchro（拔 U 盘前必须 usb disable）。

## A2 · 触发场景（含与相邻 skill 的区分）

- 配置改完要不要保存、保存到哪、怎么回退——本 skill。
- 多台机组 Virtual Chassis 后的主从同步（write memory flash-synchro 的 VC 语义）→ virtual-chassis-deployment。
- 日常运维工具（日志/抓包/健康检查）→ poe-ops-diagnostics。

## E · 可执行步骤

1. 改动前：`show running-directory` 确认当前运行目录与 Certify/Restore Status。
2. 改配置（RAM 立即生效）。
3. 保存：`write memory`（写回 running 目录）。
4. 验证通过后固化：`copy running certified`；或一步到位 `write memory flash-synchro`。
5. 想测试新目录：`reload from <目录名> no rollback-timeout`，绝不用 `reload all`。
6. 备份：configuration backup 命令生成 configuration_backup.tar（/flash/config-backup-recovery，上限 10 份）；或 usb backup admin-state enable [key …]。
7. user 目录操作：mkdir <name> → cp working/*.* <name> → reload from <name>。

## B · 边界与陷阱

- **reload all 恒从 certified 启动**，与目录内容是否一致无关（p81/83/85 三处 Warning）——验证 working/user 配置必须用 reload from working。
- **certified 运行模式锁定**：write memory 报错、目录间不能移文件；须先 reload from working 切回。
- **RAM 未保存改动断电即丢**：working 与 certified 内容一致时重启直接回滚 working，VLAN 2/3/99 全失。改动生效 ≠ 已保存。
- 镜像文件按型号命名（6360=Nos.img、6900 V72/C32=kaos.img 等），拷贝目录时不可混用。
- 配置备份 tar 只含 banner、userTable、vcboot.cfg 三类；上限 10 份自动淘汰旧档。

---
来源条目: f01, f02, p02, p03, p04, p05, p06, p07, p08, ce01, ce02, ce03, c02, g01, g02, g03, g04, g05, g39
