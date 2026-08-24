---
name: AOS 配置目录管理与软件升级
description: 当需要在 OmniSwitch 上保存/回滚配置、操作 working/certified 目录、做 USB 备份或执行 AOS 镜像升级时使用本技能。
source_book: DT00XTE301 LAN & WLAN Installation & Configuration for SMB
---

## R（触发场景）
- 改完配置要保存，或重启后配置意外丢失
- 需要在 working / certified / 自建目录之间切换启动目录或验证回滚行为
- 需要升级 AOS 镜像（含 uboot/FPGA）或做配置的 USB 备份

## I（核心理念）
AOS 的配置管理是"三层目录 + RAM 运行配置"的状态机：certified 是已认证的稳定目录，working 是待验证目录，还可自建 user-defined 目录。运行配置在 RAM 里，不保存就丢；`reload all` 永远从 certified 启动，验证新配置必须用 `reload from working no rollback-timeout`。升级同理：先升 working、验证无误再 `copy running certified` 固化。

## A1（行动框架）
1. 查看目录与状态：
   ```
   -> ls -l /flash/working          // 或 /flash/certified
   -> show microcode working | certified | loaded
   -> show running-directory        // RUNNING / CERTIFY NEEDED / SYNCHRONIZED
   ```
2. 修改配置后判断状态：改 RAM（如 `vlan 2`）后 running-directory 变 NOT SYNCHRONIZED；保存 `-> write memory`；验证新配置重启用 `-> reload from working no rollback-timeout`（C07，<<<PAGE 131>>>–<<<PAGE 137>>>）。
3. 一步保存+认证：`-> write memory flash-synchro`（= write memory + copy running certified，P16，<<<PAGE 122>>>）。
4. 自建目录实验：`mkdir lab` → `cp working/*.* lab` → `reload from lab no rollback-timeout` → `copy running certified` / `modify running-directory working`（C07，<<<PAGE 131>>>–<<<PAGE 137>>>）。
5. USB 自动备份：
   ```
   -> usb enable
   -> usb backup admin-state enable
   -> write memory        // 自动同步到 /uflash
   -> cd /uflash; ls      // 验证 certified/working 目录
   ```
   拔出前必须 `usb disable`（C08，<<<PAGE 138>>>–<<<PAGE 139>>>）。
6. 镜像升级七步：读 release note → 下载 → FTP 传到交换机 → 升级镜像 → 验证 → `copy running certified` 固化 → 按需升 uboot/FPGA（F03，<<<PAGE 465>>>–<<<PAGE 469>>>）：
   ```
   -> update uboot cmm all file u-boot.8.4.1.R03.141.tar.gz
   -> update fpga-cpld cmm all file fpga_kit_3312
   -> reload from working no rollback-timeout
   -> copy running certified
   -> show running-directory
   ```
   （C25，<<<PAGE 469>>>）
7. 恢复出厂（仅自有设备）：`-> rm /flash/working/vcboot.cfg` → `-> reload from working no rollback-timeout`，约 5 分钟（C04，<<<PAGE 105>>>）。

## A2（进阶应用）
- 冷启动目录选择规则：running 与 certified 内容一致则从 running 启动，不一致回退 certified（P14，<<<PAGE 132>>>）。
- 启动序列：U-Boot 引导 → 硬件初始化 → 内存诊断 → 镜像选择 → AOS 拷入 RAM 运行（P13，<<<PAGE 119>>>）。
- Thin Client 模式：本地不存配置，全部从 OV2500 拉取，`write memory` 可执行但不生效（P18，<<<PAGE 127>>>）。
- USB 备份可设密码加密，且 `write memory` / `copy running certified` 触发自动镜像（P17，<<<PAGE 126>>>、<<<PAGE 138>>>）。
- CLI 效率技巧：部分关键字补全（`sh vl`）、`| grep <MAC>` 过滤、`?` 在线帮助（P19，<<<PAGE 128>>>）。

## E（实证案例）
- 目录管理全流程实验：改 VLAN 后状态变 NOT SYNCHRONIZED，经 write memory / reload / copy running certified / modify running-directory 完整走一遍状态机（C07，<<<PAGE 131>>>–<<<PAGE 137>>>）。
- USB 备份启用后 write memory 自动同步，`cd /uflash; ls` 见到 certified/working（C08，<<<PAGE 138>>>–<<<PAGE 139>>>）。
- AOS 升级命令链 uboot → fpga-cpld → reload → certify（C25，<<<PAGE 469>>>）。

## B（边界与陷阱）
- `reload all` 无条件从 certified 启动，会回退到旧配置；验证新配置必须 `reload from working no rollback-timeout`（CE03，<<<PAGE 132>>>）。
- RAM 中未 `write memory` 的修改重启即丢（CE04，<<<PAGE 133>>>）。
- 从 certified 目录运行时 `write memory` 报错 "not permitted"，须先 `modify running-directory working`（CE05/P15，<<<PAGE 135>>>、<<<PAGE 124>>>）。
- 拷贝 working 目录时 boot.md5 报 Permission denied 属正常（自动生成文件），忽略继续（CE21，<<<PAGE 136>>>）。
- 教学/托管环境不要做真恢复出厂（`rm vcboot.cfg` + reload 会破坏预置基线）（CE02，<<<PAGE 105>>>）。

## 来源
- case·目录管理全流程实验（<<<PAGE 131>>>–<<<PAGE 137>>>）
- case·USB 备份与查看 uflash（<<<PAGE 138>>>–<<<PAGE 139>>>）
- case·OS6360 恢复出厂（<<<PAGE 105>>>）
- case·AOS 镜像升级实操命令链（<<<PAGE 469>>>）
- framework·AOS 软件升级七步流程（<<<PAGE 465>>>–<<<PAGE 469>>>）
- framework·Flash 目录与回滚模型（<<<PAGE 118>>>–<<<PAGE 124>>>）
- principle·write memory flash-synchro 组合语义（<<<PAGE 122>>>）
- counter·reload all 回退 certified（<<<PAGE 132>>>）
- counter·未保存配置重启丢失（<<<PAGE 133>>>）
- counter·certified 模式无法保存（<<<PAGE 135>>>）
