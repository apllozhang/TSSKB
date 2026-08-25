---
name: OmniSwitch 6900 运维与排障（气流失配重启/温度双阈值/LED 诊断/QSFP-DD 十二态/EMP 首登）
description: 需要诊断 OS6900 气流失配（循环重启/琥珀闪）、温度 Warning/Danger 阈值处置、按 LED（PS/Diag/Fan/LOC/QSFP-DD 十二态）判读故障、show module/temperature/fan 巡检、EMP 首次配置与登录排障时使用。
source_book: OmniSwitch 6900 Hardware Users Guide
---

## R（触发场景）
- 交换机反复重启或 OK/PS LED 异常闪烁：排查电源与风扇气流方向失配
- 温度告警 trap：Warning 阈值处置或 Danger 关机后的恢复流程
- 前面板 LED 判读：QSFP-DD 十二态色表、PS/Diag/Fan/LOC 与端口速率分色
- 首次登录与 EMP 带外管理配置（默认 192.168.1.1/24、解锁会话类型）

## I（核心理念）
气流失配三段式后果链（P15，<<<PAGE 50>>>/<<<PAGE 52>>>）：错误+trap → 启动时失配=OK/PS 绿琥珀交替闪且持续循环重启直至纠正；运行中热插入失配件=OK/PS 闪琥珀、到温度 Danger 阈值才重启。温度双阈值机制（P34，<<<PAGE 75>>>）：Warning 可查可配、超限发 trap 业务继续；Danger 出厂固化不可配置、超限自动关机须人工处理并手动启动。LED 是第一诊断面：系统五组 LED + 端口速率分色 + QSFP-DD 十二态色表覆盖大部分硬件状态判读（P31-P33，<<<PAGE 48>>>）。EMP 远程访问有前置：设 IP 后还必须解锁会话类型，否则 Telnet/SSH/HTTP/SNMP 全不通（P38/X32，<<<PAGE 22>>>）。

## A1（行动框架）
1. 遇重启类故障先查气流三件套一致性（风扇+双电源 F/R 后缀逐一核对），再查温度
2. 温度告警分级处置：Warning→查气流阻塞/室温/`show fan`；Danger→处理根因后手动开机
3. 硬件巡检四命令例行化：`show module` / `show module long` / `show temperature` / `show fan`
4. 带外管理搭建：console 先行改 EMP IP → 解锁会话类型 → 改密码 → 时间/可选项 → `write memory`

## A2（操作步骤）
- **失配诊断**：核对风扇托盘与两电源的 F/R 后缀；启动时失配=循环重启、运行中失配=琥珀闪至 Danger 重启（F2/X2，<<<PAGE 50>>>/<<<PAGE 52>>>）
- **温度处置**：Warning→查气流阻塞/室温/风扇状态；Danger→查阻塞或方向失配/室温/风扇，处理后手动开机（C18，<<<PAGE 75>>>）
- **监控四命令**：`show module` / `show module long` / `show temperature`（Warning/Danger 阈值与状态）/ `show fan`（C17，<<<PAGE 74>>>/<<<PAGE 75>>>）
- **首次登录七步**：console（admin/switch，115200-8N1 rollover）→ 设 EMP IP（`ip interface emp address 168.22.2.120 mask 255.255.255.0`，默认 192.168.1.1/24）→ 解锁会话（`aaa authentication default local` 或逐类型）→ `password` 改密 → 时区/夏令时 → 日期时间 → 可选项+`write memory`（C3-C7，<<<PAGE 21>>>-<<<PAGE 25>>>）
- **EMP 线缆**：接交换机用直通线、接计算机用交叉线（P37，<<<PAGE 18>>>）
- **LOC 定位**：LOC LED 闪琥珀=远程管理已激活，用于机柜中定位单台设备（C19，<<<PAGE 48>>>）
- **风扇停转响应**：任一风扇意外停转即发 trap 且 FAN LED 转琥珀（P35，<<<PAGE 75>>>）

## E（实证案例）
- 气流失配两种表现对照：启动时失配循环重启 vs 运行中热插失配件达 Danger 阈值重启（X2/P15，<<<PAGE 50>>>/<<<PAGE 52>>>）
- EMP 设 IP 与验证全流程（console 先行 + `show ip interface` 验证）（C4，<<<PAGE 22>>>）
- 温度告警处置两分支（Warning 排查不停机 / Danger 关机后手动恢复）（C18，<<<PAGE 75>>>）

## B（反例与坑）
- Danger 阈值出厂固化不可配置；超限自动关机后必须手动启动，不会自愈（X33，<<<PAGE 75>>>）
- 配好 EMP IP 仍不能远程访问——未解锁会话类型前 Telnet/FTP/HTTP/SSH/SNMP 全不通（X32，<<<PAGE 22>>>）
- 密码丢失后果严重：OmniSwitch 上覆盖已配置密码受限制，必须牢记或安全记录（X44，<<<PAGE 23>>>）
- 气流阻塞可致过热失效："Never obstruct chassis air vents"，盲板缺位会加重风扇负担（X7/P18，<<<PAGE 17>>>/<<<PAGE 50>>>/<<<PAGE 53>>>）
- 运行中勿将手指伸入电源槽或触背板；雷暴天气禁止插拔线缆与作业（X34/X36，<<<PAGE 86>>>/<<<PAGE 85>>>）
- 光口空置时辐射不可见激光，勿直视孔口，空口装保护盖（X38/X37，<<<PAGE 86>>>/<<<PAGE 84>>>）
- 检修/搬动前断开全部电源线（多电源可能有多根线）（X35，<<<PAGE 86>>>/<<<PAGE 90>>>）
- console 无硬件流控，须用软件流控 XON/XOFF（P39，<<<PAGE 76>>>）
- CDE 风险：Cat5e/6/6a 线可蓄大量静电，接线前先对地放电（X20/P40，<<<PAGE 15>>>/<<<PAGE 16>>>）

来源：OmniSwitch 6900 Hardware Users Guide（Ch2 首登 + Ch3 LED/监控/气流，p18-76；附录 A 安全，p83-90）
