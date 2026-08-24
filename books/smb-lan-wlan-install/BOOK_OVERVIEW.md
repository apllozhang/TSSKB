# BOOK_OVERVIEW — DT00XTE301 · LAN & WLAN Installation & Configuration for SMB (Edition 04)

## 基本信息与定位
- **课程编号**：DT00XTE301EN（Participant's Guide，512 页）
- **受众**：面向 SMB（中小企业）网络的安装/配置工程师，售前售后通用基础课
- **时长**：2 天（理论 Live Session + R-Labs 远程动手实验）
- **技术栈**：OmniSwitch R8（OS6900/OS6560/OS6360 等）+ OmniAccess Stellar AP + OmniVista Cirrus 云管理

## 三大目标
1. 在接入网络中部署和维护 OmniSwitch 交换机
2. 部署和维护 OmniAccess Stellar WLAN 无线接入点
3. 使用 OmniVista Cirrus 云平台配置和监管交换机与 AP

## 全书结构（章节地图）
| 页码范围 | 章节 | 核心内容 |
|---|---|---|
| p1-9 | Introduction | 课程目标、2 天议程、Internet 资源（Knowledge Hub、Spacewalkers 社区、Datasheets） |
| p10-46 | Portfolio + Hardware Overview | OmniSwitch LAN 家族、Stellar AP 家族（AP 产品线/天线/附件）、Wi-Fi 技术（802.11 代际、MU-MIMO、信道/频段） |
| p47-55 | Devices Start-Up | 供电（PoE/电源模块）、Stellar AP 启动流程、出厂默认 SSID 行为、升级 |
| p56-77 | Accessing the Administration Interface | Console/EMP 端口、Webview、SNMP、Stellar AP 的 Web 管理界面、Lightning 快速配置向导 |
| p78-116 | Switch Management Basics | 目录管理（Directories Mgmt）、用户账户/密码、Flash/Bootrom、固件升级 |
| p116-221 | PoE & VLANs | PoE 分类与供电配置、VLAN 划分、802.1Q、端口成员关系 |
| p221-267 | Deployment Modes（Stellar 三管理模式） | Express/Native 模式对比、AP 上线流程、Wi-Fi Networks Creation（SSID/VLAN 映射/安全策略） |
| p267-330 | STP & LACP | 生成树协议（STP/RSTP）防环、链路聚合 LACP 配置、多交换机多 AP 环境（实验室场景） |
| p330-435 | Cloud Mode + OV Cirrus | Cloud 模式切换、Cirrus 注册与设备申报（Eqpt Declaration）、从 Cirrus 下发配置 |
| p435-500 | Cirrus 高级业务 | Employees SSID 创建（含 ARP 认证）、Guests SSID 创建（访客门户）、Operation & Maintenance（运维巡检） |
| p500-512 | Conclusion | 总结与评估 |

## 关键技术主题（提取器重点关照）
1. **Stellar 三管理模式**：Express（闪电式无控制器）、Native（设备本地 Web）、Cloud（Cirrus 云管）的选型逻辑与切换路径
2. **SMB 场景快速交付流程**：开箱→供电→默认 SSID→Lightning 配置→Cirrus 申报，全链条可操作步骤
3. **PoE 供电设计**：Class 0-8 功率等级、预算计算、per-port 配置命令
4. **VLAN 与 Wi-Fi 网络映射**：SSID→VLAN→子网的规划方法
5. **STP/LACP 在 SMB 多交换机环境的防环与带宽聚合**
6. **Cirrus 云管下的员工/访客 SSID 分权分域设计**（含 UPAM 统一策略认证模块、Captive Portal）
7. **默认凭据与安全加固**：admin 默认密码、首次登录强制修改、HTTP/HTTPS 管理

## 原文风格与引用注意
- 大量幻灯片式短句与图表，命令行示例以 `>>>` 提示符出现
- UPAM（Unified Policy Authentication Manager）在访客门户章节反复出现，是内置策略引擎的关键词
- 实验环节（Lab）描述含拓扑与步骤编号，是"可执行步骤"类候选的主要来源

## 与站内其他书的关系
- 与 stellar-wlan-express（T310）重叠约 40%（同属 SMB/Stellar 交付），差异在本书更偏 Cirrus 云管与交换机侧
- 与 ov2500-* 系列互补：本书云端用 Cirrus，OV2500 是本地 NMS
