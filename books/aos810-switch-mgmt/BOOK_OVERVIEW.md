# OmniSwitch AOS Release 810R04 Switch Management User Guide

- 全文：`books/aos810-switch-mgmt/fulltext.md`（511 页，页码标记 `<<<PAGE N>>>`）
- Part No. 060968-00, Rev. A，December 2025，ALE USA Inc.
- 定位：AOS 8.10R4 多产品线通用的交换机管理指南（系统文件、配置、安全、管理接口、自动化）。

## 章节结构与正文行号（fulltext.md）

| 章 | 标题 | 内容要点 | 正文起始行（约） |
|---|---|---|---|
| 1 | Getting Started and Upgrading AOS | 自动管理特性、独立/虚拟机箱模式、软件升级 | 599 |
| 2 | Logging Into the Switch | 登录默认值、控制台/EMP 口、Telnet/SSH、登录横幅、FIPS、DNS 解析 | 864 |
| 3 | Managing System Files | 交换机管理概览、文件/目录管理、AOS Linux 命令、加载软件、ALE Secured Code/Secure Boot、License（含 SILOS）、系统时钟、hash 控制、keychain、PAM 包管理、U-boot/ONIE 认证 | 1620 |
| 4 | Managing CMM Directory Content | CMM 文件、单 CMM 配置管理、CMM 冗余、USB 闪存、镜像完整性 | 3638 |
| 5 | Using the CLI | CLI 概览、命令输入规则、帮助、CLI 命令日志、屏幕显示定制 | 4588 |
| 6 | Working With Configuration Files | 配置文件教程、快照配置、恢复出厂 | 4957 |
| 7 | Managing Switch User Accounts | 用户默认值、建用户、密码策略、锁定、权限、SNMP 访问、多会话 | 5384 |
| 8 | Managing Switch Security | ASA 认证管理、AAA/TACACS+/RADIUS、并发会话限制、JITC、crypto strong | 6260 |
| 9 | Using WebView | WebView（Web 管理）默认值、浏览器设置、CLI 命令 | 7175 |
| 10 | Using SNMP | SNMP 默认值、v1/v2c/v3、trap 过滤、engine ID、MIB | 7483 |
| 11 | Using OmniVista Cirrus | Cirrus 云管理、DHCP Option 43、NaaS、Thin Switch | 8167 |
| 12 | Web Services, CLI Scripting, OpenFlow, AMS | REST/Web Services、Python、CLI 脚本、AOS Micro Services、OpenFlow、Nutanix 插件、PROFINET | ~9024 |
| 13 | Configuring Virtual Chassis | 虚拟机箱（VC）默认值、拓扑、配置、自动组建、VCSP 分裂保护 | 11408 |
| 14 | Managing Automatic Remote Configuration Download | 自动远程配置下载、DHCP 客户端自动配置、Nearest-Edge、LACP 自动检测 | 13121 |
| 15 | Lightning Configuration Mode | 闪电配置模式（WebView 首联向导） | 14194 |
| 16 | Configuring Automatic Fabric | 自动 Fabric（USFA）默认值、发现、配置 | 14333 |
| 17 | Configuring NTP | NTP 默认值、配置、验证 | 15539 |
| A/B | 附录 | 软件许可；SNMP trap/MIB/系统事件表 | ~15970 起 |

## 候选提取范围
principles（原理）、cases（配置案例）、counter-examples（限制/陷阱）、frameworks（体系框架）、glossary（术语）五类，输出于 `candidates/`。
