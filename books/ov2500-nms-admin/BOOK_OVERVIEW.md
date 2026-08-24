# BOOK_OVERVIEW — DT00XTE311 · OmniVista 2500 NMS Administration R4 (Edition 09)

## 基本信息与定位
- **课程编号**：DT00XTE311EN（Participant's Guide，581 页）
- **受众**：使用 OmniVista 2500（OV2500）管理 OmniSwitch 6870/6900/6560/6360 网络的管理员
- **形式**：讲授 + 动手实验（Lecture + Hands-on Labs）
- **技术栈**：OV2500 R4（虚拟机形态 NMS）+ OmniSwitch AOS R8

## 全书结构（章节地图）
| 页码范围 | 章节 | 核心内容 |
|---|---|---|
| p1-10 | Administration | 课程表、评估 |
| p11-41 | Presentation | OV2500 概览：响应式界面、Nodal/Release 模式、高可用（HA）、应用更新、NMS 组件、Discovery/Topology/Locator/VM Manager、配置/统一接入/安全/管理、WLAN 与 UPAM |
| p42-78 | Installation & System Setup | 虚机设备（Virtual Appliance）部署：平台与容量规划（Sizing）、安装步骤、Dashboard、Web 偏好、License、OmniSwitch 初始设置（SNMP source address）、Watchdog、系统健康、会话管理、Thin Client |
| p79-87 | Remote Lab Connection | 连接 Data R-Lab、虚拟机、DHCP 服务器 |
| p107-168 | Discovery & Topology & 资源管理 | Discovery Profile（General/SNMP/Advanced）、Links/Ports 发现、Topology Maps、Locator、Ethernet OAM/SAA 统计、通知与告警声音、用户活动报告、Resource Manager（镜像升级/Inventory）、双因素认证（2FA）、CLI Scripting（Telnet 脚本/发送脚本/日志）、SSH/Telnet 交换机账户管理 |
| p169-224 | 设备配置管理 | 配置备份/比较/部署、批量配置 |
| p225-256 | Unified Access（统一接入） | 认证服务器、集中式安全特性、用户角色导向访问策略、Unified Profile（Home/Workflows/Templates）、AAA Server Profile、Access Role Profile（有线/无线）、Access Auth Profile（默认/失败/备用策略）、Access Classification 规则类型、Unified Policy、Captive Portal 配置与定制 |
| p257-294 | PolicyView | QoS 规则配置步骤、One Touch 模式（Voice/Data/ACL）、Expert Mode 向导（设备选择→条件→动作→有效期）、Policy Flow |
| p295-320 | Quarantine Manager | 隔离管理器（基于 802.1X 健康检查的终端隔离） |
| p321-581 | 后半部：WLAN/UPAM 管理、报表、告警、日志、备份恢复、综合实验 | 无线管理、系统维护 |

## 关键技术主题（提取器重点关照）
1. **OV2500 虚机部署与容量规划**：Sizing 表（vCPU/内存/磁盘 vs 管理设备数）、安装步骤序列
2. **Discovery Profile 三层配置**：General/SNMP/Advanced 的参数与发现范围控制
3. **Resource Manager 批量镜像升级**：升级镜像流程与 Inventory 管理
4. **Unified Access 策略模型**：Access Role Profile（用户角色）+ Access Auth Profile（认证策略）+ Unified Policy（策略执行）三层抽象，有线无线统一
5. **PolicyView QoS 一键模式与专家向导**：One Touch Voice/Data/ACL vs Expert Mode（条件-动作-有效期）
6. **Quarantine Manager 隔离流程**：不健康终端隔离机制
7. **2FA 双因素认证初始设置**、CLI Scripting 批量脚本下发
8. **Captive Portal 配置与定制**（与 UPAM 联动）

## 原文风格与引用注意
- 截图密集型教材（400+ 配置截图），操作路径多为 "Home → X → Y" 面包屑式
- 与 ov2500-install（安装指南书）互补：本书是管理员视角的完整功能操作手册

## 与站内其他书的关系
- ov2500-install / ov2500-rap-vpn / ov2500-release-notes 是配置手册线，本书是管理培训线，功能覆盖最全
