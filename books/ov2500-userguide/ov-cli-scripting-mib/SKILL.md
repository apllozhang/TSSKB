---
name: CLI Scripting 脚本训练与 MIB 导入
description: 需要编写/发送 CLI+JavaScript 混编脚本批量配置设备（内置变量、expectPrompt 确认提示训练、tapps 指令、定时 Cron 发送）、导入第三方设备 MIB、定制自定义工具菜单时使用。
source_book: OmniVista 2500 NMS 4.9R2 User Guide
---

## R（触发场景）
- 同一段配置要下发到几十台交换机，CLI 逐台敲不动
- 脚本里有 reload/写闪等会弹确认提示或挂起会话的命令
- 网里第三方设备（Cisco/Extreme 等）的 trap 与 MIB 对象 OV 不认识
- 把常用外部工具挂进 OV 的自定义菜单

## I（核心理念）
CLI Script 是 .script 文本文件，CLI 命令与 JavaScript 混编（每行一条 CLI；JS 用 cli 对象驱动交互）。两类难点：一是"应答"——确认提示型命令用 expectPrompt 训练，挂起型命令用 <tapps> lastcmd；二是"慢命令"——write memory flash-synchro 等作末条命令会话即断，须设超时或补命令。第三方 MIB 走 OID 条目 + Mibset 目录 + 依赖顺序导入。

## A1（行动框架）
1. **判断命令类型**：普通命令直接写；确认提示型（takeover/reload/fsck）须 expectPrompt 处理；慢命令（写闪）须 setTimeout/<tapps> set timeout；挂起型（reload）前加 <tapps> lastcmd（principles·P65/P66，<<<PAGE 241-244>>>）
2. **变量化**：设备属性用内置变量（$IP_ADDRESS/$BASE_MAC 等），用户输入用 User Variables（发送时填值）（principles·P64，<<<PAGE 242-243>>>）
3. **MIB 导入路径**：先建 OID 条目（识别厂商/型号）→建 Mibset 目录→按依赖顺序导入（principles·P80/P81，<<<PAGE 285-288>>>）

## A2（操作步骤）
- **创建并发送脚本**：CLI Scripting→Scripts→Add：Filename（自动加 .script）、勾 Shared Admin Script（前缀 shadmin）、命令区（描述用 /* @@desc@@ */）→Add。发送：选脚本→Send Script→Script Info→Device Selection（Switch Picker 或 Topology）→Scheduler（Now / Periodically: Simple 或 Cron）→Define User Variables→Send Script；日志在 Logs 屏按命令查看（cases·C23，<<<PAGE 239-246>>>）
- **处理确认提示（reload 示例）**：`cli.sendCmd("more"); cli.expectPrompt("Confirm Activate (Y/N):");` 之后 `cli.sendCmd("reload working no rollback-timeout in 10:10"); cli.sendCmd("y")`；会挂起的命令前加 `<tapps> lastcmd </tapps>`（cases·C25，<<<PAGE 241, 244>>>）
- **内置变量表**：$BASE_MAC/$BOOT_DIR/$CHASSIS_TYPE/$IP_ADDRESS/$LOGIN_ID/$LOGIN_PWD/$READ_PWD/$SECOND_PWD/$SYS_LOCATION/$SYS_NAME/$SYSTEM_OID/$SYS_VERSION/$WRITE_PWD；JS 中使用须加引号。cli 对象函数：sendCmd/lastResponse/setTimeout/trace/expectPrompt/deviceType/cliSleep/errorLog/forgetPrompt（principles·P64，<<<PAGE 242-243>>>）
- **导入第三方 MIB**：Third-Party Devices Support 建 OID 条目（OID 只填 enterprises 后段，如 Cisco=9、Extreme=1916；MIB Directory Name 可为不存在目录，导入时自动创建）→Import MIBs→选 Mibset→Upload Files（Chrome 支持 Upload Folder）→Up/Down 箭头调编译顺序→Apply（cases·C31，<<<PAGE 288>>>）
- **SecureCRT 作为 SSH Custom 客户端**（自定义工具菜单场景）：Options→Global Options→Web Browser→勾 Use registry setting；浏览器需支持 SSH2 且 SecureCRT 为默认 SSH2 应用（cases·C29，<<<PAGE 268-270>>>）

## E（实证案例）
- 创建并发送 CLI 脚本（Cron 排程 + User Variables）（cases·C23，<<<PAGE 239-246>>>）
- reload 确认提示训练（expectPrompt + y）（cases·C25，<<<PAGE 241, 244>>>）
- 第三方 MIB 导入（OID 条目 + 顺序调整）（cases·C31，<<<PAGE 288>>>）

## B（反例/坑）
- CLI 脚本不能发往 Stellar 无线设备；发送前 OV 必须已知每台设备 CLI/FTP 凭据（principles·P63，<<<PAGE 239>>>）
- 自动弹确认提示的操作命令（takeover、reload、fsck）不支持直接写入脚本，必须 expectPrompt/more/lastcmd 处理（principles·P66，<<<PAGE 242>>>）
- 慢命令作末条命令会话即断：write memory flash-synchro 之后要补一条命令或设 tapps 超时；setTimeout(min,sec) 仅作用于下一条命令（principles·P65，<<<PAGE 241-243>>>）
- MIB 文件必须 .mib 扩展名；新目录须导入完整 MIB 集（含被引用标准 MIB）；依赖顺序按 import 语句排，文件名常不可信；不建议向 OV 自带 MIB 目录加文件（principles·P81，<<<PAGE 287-288>>>）
- MIB 导入后不立即解析——发现对应 OID 设备或重启服务器才解析（principles·P81，<<<PAGE 287-288>>>）
- 脚本日志保留默认 180 天，位于 data\cli_scripting_logs 按设备 IP 分目录（principles·P67，<<<PAGE 248>>>）

## 来源
OmniVista 2500 NMS 4.9R2 User Guide 第 10 章 CLI Scripting（<<<PAGE 238-248>>>）、第三方设备支持与 MIB 导入（<<<PAGE 285-288>>>）、SSH Custom（<<<PAGE 268-270>>>）。条目来源：cases C23/C25/C29/C31；principles P63-P67/P80/P81。
