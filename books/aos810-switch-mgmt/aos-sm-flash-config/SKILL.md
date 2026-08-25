---
name: AOS 8 Flash 双目录与配置文件管理（certified/working/快照/恢复出厂）
description: 需要在 OmniSwitch AOS 8 上管理 /flash 目录、certified/working 双目录与 RUNNING CONFIGURATION、write memory/copy running certified、reload 回滚、配置文件 apply/syntax-check/snapshot、reset-to-factory 恢复出厂时使用。
source_book: OmniSwitch AOS Release 8.10R4 Switch Management Guide
---

## R（触发场景）
- 搞不清 certified / working / RUNNING DIRECTORY / RUNNING CONFIGURATION 的关系，改动重启后丢失
- 要把试验配置先放用户目录验证，再认证回 certified（软件回滚）
- 要上传/应用 ASCII 配置文件（configuration apply）、定时批量下发、应用前语法预检
- 要抓取当前非默认配置快照（snapshot）、tar 备份/恢复、或恢复出厂（reset-to-factory）
- 文件传输选型：FTP/SFTP/SCP/TFTP；TFTP 单会话、空间限制排障

## I（核心理念）
CMM 双目录配置管理体系（F2，<<<PAGE 94-101>>>）：certified（已认证的最可靠基线，不可直接写）+ working/用户目录（新文件试验场）+ RUNNING CONFIGURATION（RAM 中的当前配置）三层模型。正常重启时若 certified 与 RUNNING DIRECTORY 内容不同则从 certified 启动（P4，<<<PAGE 95>>>），这套目录结构本身就是回滚机制——新镜像/新配置先进 working 验证，可靠后 `copy running certified`（P5）。vcboot.cfg 是启动配置文件，启动时按名查找（P6，<<<PAGE 94>>>）。配置文件即 ASCII 文本，可上传、快照、定时应用，构成可复制的批量部署底座（P47，<<<PAGE 122>>>）。

## A1（决策框架）
1. **改动要落盘**：运行目录为 certified 时不能直接保存（X1），先 `modify running-directory` 切用户目录，`write memory` 落盘，验证后 `copy running certified`（C20，<<<PAGE 104, 106>>>）
2. **要试验回滚**：`reload from working rollback-timeout 5` 带回滚超时重启，超时自动正常重启兜底（C21，<<<PAGE 105>>>）
3. **批量配置下发**：工作站文本编辑器/快照/内置 vi 三种来源（P54），`configuration syntax-check` 预检（P57）→ `configuration apply`（可 at/in 定时，P55）→ `show configuration status` 验证（C27/C28）
4. **留档/回退**：`configuration snapshot` 导出非默认配置（P58）；`configuration backup` tar 备份上限 10 份（P59）；`reset-to-factory` config/retain-vc/all 三档（P60）
5. **文件传输选型**：FTP/SFTP/SCP 加密优先，TFTP 仅单会话且受 flash 空间限制（P11/P12）

## A2（操作步骤）
- **目录查看与运行目录管理**：`ls /flash`、`cd`、`freespace`；`show running-directory`（不 certified 则 `write memory flash-synchro`）（C3，<<<PAGE 23>>>）
- **切换运行目录并保存**：`modify running-directory user-config1` → `write memory` → `copy running certified`（C20，<<<PAGE 104, 106>>>）
- **带回滚重启/定时重启**：`reload from working rollback-timeout 5`；`reload from working no rollback-timeout in 3:03`（C21，<<<PAGE 105>>>）
- **配置文件应用**：PC 建 dhcp_relay.txt → 上传 → `configuration apply dhcp_relay.txt` → `show configuration status` → 业务命令验证（C27，<<<PAGE 133>>>）；定时 `configuration apply bncom_cfg.txt at 09:00 july 4` / `in 6:15`，`configuration cancel` 取消（C28，<<<PAGE 134-135>>>）
- **快照与恢复出厂**：`configuration snapshot all`（或 vlan qos snmp/名称.snap）；`reset-to-factory config retain-vc in 60`（C29，<<<PAGE 139, 141>>>）
- **文件系统维护**：`fsck no-repair|repair` 修复（P9）；`newfs` 极危险；Linux 工具 watch/cut/paste/tee 直接可用（P10）
- **TFTP 传输**：镜像 binary 模式、配置 ASCII 模式（P11）

## E（实证案例）
- 保存运行配置绕开 certified 限制全流程（C20，<<<PAGE 104, 106>>>）
- 指定目录带回滚超时重启（C21，<<<PAGE 105>>>）
- DHCP Relay 三命令配置文件教程（C27，<<<PAGE 133>>>）
- 配置文件定时应用会话（C28，<<<PAGE 134-135>>>）
- 快照与恢复出厂三档（C29，<<<PAGE 139, 141>>>）

## B（反例/坑）
- certified 目录不能直接保存配置，运行目录为 certified 时改动重启即丢（X1，<<<PAGE 94, 95>>>）
- 未保存的 RUNNING CONFIGURATION 重启后回退 certified，改动全丢（X2，<<<PAGE 95>>>）
- FTP/TFTP 用主机名需先配好 DNS 解析器（X7，<<<PAGE 63>>>）
- TFTP 同一时刻仅一个会话；下载文件不得超过剩余 flash 空间（X8，<<<PAGE 64>>>）
- Bash 特殊字符（$、!）会被解释为变量/参数，CLI 中须单引号包裹（X28，<<<PAGE 123>>>）
- 同时只能有一个配置定时会话，后设覆盖先设（X30，<<<PAGE 136>>>）
- 应用出错生成 `.n.err` 文件，error-file-limit 控制保留（P56，<<<PAGE 137>>>）
- reset-to-factory all 档连 license/证书一并清除（P60，<<<PAGE 141>>>）

## 来源
OmniSwitch AOS 8.10R4 Switch Management Guide 第 3 章 System Files（<<<PAGE 52-64>>>）、第 4 章 CMM Directory（<<<PAGE 94-107>>>）、第 6 章 Configuration Files（<<<PAGE 122-141>>>）。条目来源：cases C3/C20/C21/C27/C28/C29；principles P1-P12/P47/P54-P60；counter-examples X1/X2/X7/X8/X28/X30；frameworks F2。
