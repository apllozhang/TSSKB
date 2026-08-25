---
name: AOS 8 日志与健康监测（command-log/swlog/tech-support/自检/时钟）
description: 需要在 OmniSwitch AOS 8 上启用命令审计日志（command-log）、查看交换机日志 swlog、采集 show tech-support 诊断包、执行硬件/进程自检、检查系统状态与文件系统健康、配置系统时钟时区时使用。
source_book: OmniSwitch AOS Release 8.10R4 Switch Management Guide
---

## R（触发场景）
- 要审计谁在交换机上执行了什么命令（合规/追责）：启用 command-log
- 排障要采集完整诊断基线：show tech-support（layer2/layer3/eng complete）
- 要查交换机运行日志 swlog、检查文件系统（fsck/freespace）、验证镜像完整性
- 冗余/增强安全场景要做硬件自检（hardware-self-test）与进程自检（process-self-test）
- 要设系统日期/时区（NTP 见 aos-sm-mgmt-services）

## I（核心理念）
AOS 运维监测分四层：命令级审计（command-log 记录命令全文/用户/时间/来源 IP/结果，默认禁用，P52）→ 系统日志（swlog 落 /flash/network，<<<PAGE 52>>>）→ 诊断快照（show tech-support 按层采集基线，升级与排障前必采，P17/C3）→ 主动健康检查（fsck 文件系统修复、image integrity check 镜像校验、硬件/进程自检、show system 总览）。时钟是日志可信的前提：`system date/timezone`，DST 随时区自动（P163）。

## A1（决策框架）
1. **合规审计开 command-log**：`command-log enable` 自动建 /flash/command.log，降序查看含 Command/UserName/Date/IP/Result（C26）
2. **排障/升级前采基线**：`show system` 总览 → 清旧日志释放空间 → `show tech-support layer2|layer3|eng complete` 分层采集（C3）
3. **文件系统异常**：`fsck no-repair` 先诊断、`fsck repair` 修复；`freespace` 看剩余空间（P8/P9）
4. **怀疑镜像损坏**：`image integrity check` 比对 SHA256 与 key file（P92）
5. **增强安全/冗余场景**：`hardware-self-test` / `process-self-test` 自检（增强模式默认要求）

## A2（操作步骤）
- **命令日志**：`command-log enable` → `show command-log status` → `show command-log`（降序）→ `command-log disable`（C26，<<<PAGE 127-128>>>）
- **维护例行（升级前基线）**：`show system` → `rm *.log` / `rm *.tar` → 清 /pmd → `show running-directory` → `show tech-support [layer2|layer3|eng complete]`（C3，<<<PAGE 23>>>）
- **文件系统**：`freespace`、`fsck no-repair|repair`（P8/P9，<<<PAGE 59>>>）
- **镜像校验**：`image integrity check` / `image integrity get-key`（P92，<<<PAGE 118>>>）
- **系统时钟**：`system date 06/23/2002`（mm/dd/yyyy）、`system timezone pst`、`system time 10:45:00`（C15，<<<PAGE 78-79>>>）
- **会话监控**：`who` 列会话、`kill <n>` 终止异常会话（P84）

## E（实证案例）
- 命令日志启用/查看/停用（C26，<<<PAGE 127-128>>>）
- 升级前维护例行与 tech-support 基线采集（C3，<<<PAGE 23>>>）
- 系统时钟与时区配置（C15，<<<PAGE 78-79>>>）

## B（反例/坑）
- command.log 在命令日志功能启用期间不可删除（X29，<<<PAGE 127>>>）
- 增强模式下查看 swlog 需要输入用户名密码（X53，<<<PAGE 178>>>）
- 密码策略等部分设置不自动保存，监控类改动注意落盘（X31，<<<PAGE 151>>>）
- swlog 位于 /flash/network，清空间时注意保留排障所需日志（<<<PAGE 52>>>）
- `newfs` 会删除整个文件系统，仅在灾备场景使用（<<<PAGE 59>>>）
- 时间不准时日志时间戳与证书/云认证都会连锁出问题；用户配置的时区优先于 DHCP Option-2（P163，<<<PAGE 78-79>>>）

## 来源
OmniSwitch AOS 8.10R4 Switch Management Guide 第 1 章维护例行（<<<PAGE 23>>>）、第 3 章 System Files（<<<PAGE 52-60, 78-79>>>）、第 4 章镜像完整性（<<<PAGE 118>>>）、第 5 章命令日志（<<<PAGE 127-128>>>）、第 7 章会话管理（<<<PAGE 163-164>>>）。条目来源：cases C3/C15/C26；principles P8-P10/P17/P52/P53/P84/P92/P163；counter-examples X29/X31/X53；frameworks F12（时钟部分）。
