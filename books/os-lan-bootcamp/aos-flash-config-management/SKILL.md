---
name: AOS Flash 双目录与配置管理（含代码升级）
description: 需要理解/操作 OmniSwitch working/certified 双目录回滚机制、配置快照恢复、CLI/远程访问/AAA 账户管理、诊断日志（swlog/sFlow/镜像），或执行 AOS 代码升级与 USB 灾难恢复时使用本技能。
source_book: DT00CTE120 OmniSwitch R6/R8 Bootcamp Issue 25
---

## R（触发场景）
- 变更前需要设计回滚路径（reload rollback-timeout / certified 备份）
- 误删配置后需要从 snapshot 文本快速恢复
- 代码升级：上传镜像到 working、验证、认证到 certified
- 配置管理访问（SSH/WebView/FTP）、用户账户分区权限、密码策略
- 排障需要 swlog 分级日志、command-log、端口镜像、sFlow

## I（核心理念）
AOS Flash 的核心是双目录互为回滚：working（可写运行目录）与 certified（只读认证目录）各存一套镜像+boot.cfg，认证版本即升级失败的退路（P17/F4，<<<PAGE 126-127>>>）。启动规则：两目录不一致时从 certified 启动，此时改动无法保存，须先切回 working（P19/P24，<<<PAGE 130-131, 148>>>）。R8 增加了用户自定义目录与 running directory 概念，可直接对自定义目录保存配置（P21/P22，<<<PAGE 145-146>>>）。变更文化的口诀是"先拿到可回退状态再推进"：`reload working no rollback-timeout` → 验证 → `copy working certified`（P20，<<<PAGE 132-133>>>）。

## A1（决策/选型）
1. 回滚方式：带 rollback-timeout 的 reload 到时自动回滚（实验/灰度）；no rollback-timeout 表示确认不回滚（P23，<<<PAGE 147>>>）
2. 配置备份：snapshot 文本（可离线编辑、`configuration syntax check` 校验）vs write memory（仅存运行目录）（P30，<<<PAGE 164>>>）
3. 认证链：`aaa authentication <service>` 后可列最多 3 个备份服务器（含 local）按序轮询（P35，<<<PAGE 185>>>）
4. 升级传输通道：FTP（须先 `aaa authentication ftp local`，默认落 working 目录，X14，<<<PAGE 136, 964>>>）或 USB auto-copy/灾难恢复（P189/P190，<<<PAGE 139-140>>>）

## A2（操作步骤）
1. 回滚实操：`reload working no rollback-timeout`(R6)/`reload from working no rollback-timeout`(R8) 重启确认；`reload working rollback-timeout 1` 观察 `WARNING: "sysResetHardwareFlag" flag is SET` 与 CERTIFY NEEDED 状态；`show running-directory`、`ls /flash/working`（C3，<<<PAGE 215-217>>>）
2. 快照：`configuration snapshot all snapall` → `vi/more snapall` → `configuration snapshot vlan snapvlan` → `configuration syntax check snapvlan verbose`(R6)/`configuration syntax-check`(R8) → 误删后 `configuration apply snapvlan` 恢复（C4，<<<PAGE 229-230>>>）
3. 代码升级四步：`show microcode working/certified` 对比版本 → FTP binary 模式上传镜像入 /flash/working → `reload from working no rollback-timeout` → 验证后 `copy working certified`（C52/P187，<<<PAGE 962-965>>>）
4. USB 灾难恢复：U 盘放 6900/certified 与 6900/working 目录 + 根目录 Trescue.img，miniboot 下 `run rescue`（P189，<<<PAGE 139>>>）；USB auto-copy 用 aossignature 触发、完成自动禁用防重复升级（P190，<<<PAGE 140>>>）
5. 远程访问安全：`aaa authentication http local`、`aaa authentication ftp local`、`aaa authentication ssh local`；R6 需 `ip http ssl`，R8 默认强制 SSL（C7/C9，<<<PAGE 239-240, 246>>>）
6. 账户分区权限：`user userread password ...` + `user userread read-only ip|all|none|domain-layer2`；read-write 分功能域授权（C8，<<<PAGE 242-246>>>）
7. 诊断日志：`swlog output console/flash/socket ipaddr ...`（socket 需先配 Loopback0）；按模块调级 `swlog appid ospf_0 subapp hello level debug3`（默认 info=6）；`command-log enable`（P54/P55/P56，<<<PAGE 326-335>>>）；sFlow 三要素 `sflow receiver/sampler/poller`（P63，<<<PAGE 347-350>>>）
8. CLI 辅助：`?`/TAB 补全/`!22` 调历史/`show history`(R6)/`history`(R8)；别名存 boot.cfg（P31/C5，<<<PAGE 233-235, 165>>>）

## E（实证案例）
- C3 Working/Certified 回滚实操：rollback-timeout 引发的 CERTIFY NEEDED 状态观察（<<<PAGE 215-217>>>）
- C4 快照保存与恢复：删 VLAN 后 `configuration apply snapvlan` 全量回滚（<<<PAGE 229-230>>>）
- C14 诊断综合实验：swlog 三输出 + command-log + sFlow sampler 512:1 采样（<<<PAGE 326-356>>>）
- C52 代码升级：FTP 上传 → reload 验证 → 认证（<<<PAGE 962-965>>>）

## B（反例与坑）
- certified 目录不可直接保存配置，也不可跨目录移动文件（X12，<<<PAGE 131, 145, 148, 218>>>）
- R6 无 `modify running-directory` 命令（X13，<<<PAGE 224>>>）
- USB 默认禁用；拔出前必须 `usb disable`（X15，<<<PAGE 138, 225>>>）；USB backup 与 auto-copy 互斥（X16，<<<PAGE 141>>>）
- admin 账户仅 console 可登录/改密码（X17/P32，<<<PAGE 176>>>）；所有远程访问默认关闭（X18，<<<PAGE 184>>>）
- 新建 end-user profile 默认无任何权限；删被引用的 profile 会锁死用户（X19，<<<PAGE 182>>>）
- R8 WebView 默认强制 SSL，R6 不强制（X20，<<<PAGE 240>>>）
- 镜像传输必须 binary、配置必须 ASCII（X85/P188，<<<PAGE 965>>>）；*.img 勿移动/删除（X21，<<<PAGE 237>>>）
- command.log 在启用期间不可删（X34，<<<PAGE 334>>>）；镜像与端口监控不能同 NI（X35，<<<PAGE 339, 342>>>）；镜像目标端口容量须一致（X37/P57，<<<PAGE 337>>>）
- 无 boot.cfg 的目录 write memory 时会自动创建 boot.cfg（X22，<<<PAGE 216>>>）；RCL 有路径长度/无 IPv6/无 EMP 限制（X23，<<<PAGE 157>>>）

## 来源
- principles·P16-P31/P54-P63/P187-P190；frameworks·F4；cases·C3/C4/C5/C6/C7/C8/C9/C14/C52；counter-examples·X12-X23/X34-X37/X85
