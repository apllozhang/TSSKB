---
name: AOS 双分区配置管理
description: 当需要在 OmniSwitch AOS R8 上保存/回滚配置、理解 working/certified 双目录状态机、做配置备份或镜像升级时使用。
source_book: DT00XTE310 OmniSwitch LAN Access & OmniAccess Stellar WLAN Express
---

## R（触发场景）
- 在 OmniSwitch 上执行 `write memory` 报错 "not permitted when switch is running in certified mode"
- 改完配置重启后配置"丢失"，需要理解回滚机制或找回未认证配置
- 需要做配置备份（内置 tar / USB）或升级软件镜像并保留回退能力

## I（核心理念）
AOS R8 用 working / certified / user-defined 三目录实现"配置即文件"的管理模型：运行配置（running）随时可写入 working，但只有 `copy running certified` 认证后才能在冷启动时稳定生效。冷启动会比较 working 与 certified 内容决定启动目录，这是一套防"半配置"开机的回滚保护机制。

## A1（行动框架）
1. **理解状态机**：`write memory`（running→working）→ `copy running certified`（认证）→ `write memory flash-synchro`（= write memory + copy running certified 三合一，<<<PAGE 89>>>）。
2. **查看当前运行目录**：`show running-directory`（关注 NOT SYNCHRONIZED / CERTIFY NEEDED / CERTIFIED 状态，<<<PAGE 127>>>-<<<PAGE 131>>>）。
3. **从 working 启动（不回滚）**：`reload from working no rollback-timeout`。
4. **切换运行目录**：`modify running-directory working`。
5. **实验/回滚流程**：改配置（如 `vlan 2/3/99`）→ `show running-directory`（NOT SYNCHRONIZED）→ `write memory`（CERTIFY NEEDED）→ `reload all` 回到 CERTIFIED、新配置丢失 → `reload from working no rollback-timeout` 找回（<<<PAGE 127>>>-<<<PAGE 131>>>）。
6. **配置备份**：
   - 内置备份命令生成 .tar（含 banner、userTable、vcboot.cfg），存于 /flash/config-backup-recovery，最多保留 10 个 .tar（<<<PAGE 92>>>）。
   - USB 备份：`usb enable` → `usb backup admin-state enable` → `write memory` 自动同步到 /uflash → `cd /uflash` + `ls` 验证 certified/working 两目录（<<<PAGE 93>>>、<<<PAGE 132>>>-<<<PAGE 133>>>）。

## A2（进阶应用）
- **软件镜像升级流程**（<<<PAGE 1013>>>-<<<PAGE 1017>>>）：读 release note 核对内存/UBoot/FPGA 要求 → FTP 上传升级文件 → 升级 image → 验证 → certify → 必要时 `update uboot cmm all file u-boot.X.X.X.tar.gz` + `copy running certified`。出问题可回滚到先前 certified 版本。
- **user-defined 目录实验法**：`mkdir lab` / `cp working/*.* lab` → `reload from lab no rollback-timeout`，可在不动生产目录的前提下做实验（<<<PAGE 127>>>-<<<PAGE 131>>>）。
- **AP 侧首次配置**（同属"保存与基线"思路）：Console 登录 support/aos2016 → `ssudo firstboot -y` → `ssudo reboot` 恢复出厂；或按住 Reset 键 6 秒至 LED 闪红（<<<PAGE 122>>>、<<<PAGE 376>>>）。

## E（实证案例）
- 双分区目录全流程实验：建 VLAN → write memory → reload all 回滚丢失 → reload from working 找回 → user 目录 → certify（<<<PAGE 127>>>-<<<PAGE 131>>>）。
- 实测报错 "ERROR: Write memory is not permitted when switch is running in certified mode"（<<<PAGE 129>>>）。
- USB 备份/恢复全流程验证 certified/working 双目录落盘（<<<PAGE 132>>>-<<<PAGE 133>>>）。

## B（边界与陷阱）
- **`reload all` 无条件从 certified 启动**，不管 running 目录内容是什么——未认证的改动会丢（<<<PAGE 126>>> WARNING）。
- RAM 未保存就重启 → running 的全部改动被覆盖（案例中 VLAN 2/3/99 全丢，<<<PAGE 127>>>）。
- Certified 模式下只读：不能 write memory、不能跨目录移动文件（<<<PAGE 91>>>、<<<PAGE 129>>>）。解法：`reload from working no rollback-timeout` 或 `modify running-directory working`。
- Fast PoE / Perpetual PoE 需升级 FPGA/CPLD，OS6360-P10A 不支持（<<<PAGE 147>>>-<<<PAGE 148>>>）。

## 来源
- frameworks·AOS R8 双分区配置管理流程（<<<PAGE 85>>>、<<<PAGE 88>>>-<<<PAGE 91>>>、<<<PAGE 126>>>-<<<PAGE 131>>>）
- frameworks·配置备份与恢复（<<<PAGE 92>>>-<<<PAGE 93>>>、<<<PAGE 132>>>-<<<PAGE 133>>>）
- frameworks·软件镜像升级流程（<<<PAGE 1013>>>-<<<PAGE 1017>>>）
- principles·双分区启动判定规则（<<<PAGE 126>>>、<<<PAGE 88>>>）
- principles·Certified 模式只读原理（<<<PAGE 91>>>、<<<PAGE 129>>>）
- cases·C6 双分区目录全流程实验（<<<PAGE 127>>>-<<<PAGE 131>>>）
- cases·C7 USB 备份/恢复（<<<PAGE 132>>>-<<<PAGE 133>>>）
- cases·C5 AP 出厂复位两法（<<<PAGE 122>>>、<<<PAGE 376>>>）
- counter-examples·X1/X2/X3（<<<PAGE 126>>>、<<<PAGE 127>>>、<<<PAGE 129>>>）
