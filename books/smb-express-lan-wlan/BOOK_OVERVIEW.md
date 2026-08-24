# BOOK_OVERVIEW — DT00XTE310 · OmniSwitch LAN Access & OmniAccess Stellar WLAN Express (Edition 05)

## 基本信息与定位
- **课程编号**：DT00VTE310（Participant's Guide，1083 页）
- **受众**：交付工程师，覆盖 LAN 接入交换 + Stellar WLAN 三种部署模式 + 语音 WLAN + 云管
- **时长**：5 天（Live Session + R-Labs）
- **技术栈**：OmniSwitch R8 + OmniAccess Stellar AP（Express/Enterprise/Cloud 三模式）+ OV Cirrus + 语音话机

## 三大目标
1. 在接入网络中部署和维护 OmniSwitch 交换机
2. 部署和维护 OmniAccess Stellar WLAN AP
3. 使用 OmniVista Cirrus 配置和监管交换机与 AP

## 全书结构（章节地图）
| 页码范围 | 章节 | 核心内容 |
|---|---|---|
| p1-13 | Introduction | 5 天议程、实验环境、Internet 资源 |
| p14-50 | Portfolio + Hardware | OmniSwitch 家族、Stellar AP 家族、Wi-Fi 技术（MU-MIMO、Wi-Fi 代际性能） |
| p51-59 | Devices Start-Up | 供电、AP 启动、默认 SSID、加载/升级 |
| p60-81 | 管理界面访问 | Console/EMP/Webview/SNMP、Stellar Web 管理、Lightning 配置向导 |
| p82-96 | 文件/目录管理 | AOS 文件系统、配置备份恢复、Thin Client、vi 编辑器 |
| p97-158 | 系统与固件管理 | 认证目录、配置状态（certified/working 双分区）、PoE（标准/功率预算/管理/监控/LED） |
| p159-184 | VLAN 管理 | 静态 VLAN、VLAN 间路由（Inter VLAN Routing） |
| p185-221 | Stellar 部署模式 + Wi-Fi 网络创建 | Express/Enterprise/Cloud 三模式详解；Wi-Fi Express 下员工 SSID（密码认证）、访客 SSID（Captive Portal）、自动 VLAN 分配、内置 DHCP/DNS/NAT、QoS/ACL |
| p222-258 | STP/LACP/多设备环境 + 语音 WLAN | 语音话机产品线、Voice over WLAN 部署流程（准备→实施→运维） |
| p259-330 | Wi-Fi Cloud（Cirrus）+ Wi-Fi Enterprise | Cloud 模式选择、Cirrus AP Group、Enterprise 分布式控制架构（无控制器分布式数据面）及配置步骤 |
| p330-1083 | 后半部：交换机深入 + 故障排查 + 综合实验 | 端口/链路管理、AAA/802.1X、DHCP、路由基础、故障排查（troubleshooting）方法论、综合 Lab |

## 关键技术主题（提取器重点关照）
1. **Stellar 三部署模式全景**：Express（无云快速开通）、Enterprise（分布式控制、无控制器架构）、Cloud（Cirrus）——选型决策树与切换
2. **Enterprise 分布式控制架构**：AP 间分布式数据面、配置步骤序列（p268-273）
3. **Wi-Fi Express 全流程**：AP 组、统一 Web 管理、员工/访客 SSID、自动 VLAN 分配、内置 DHCP/DNS/NAT/QoS/ACL
4. **Voice over WLAN 部署三阶段**：Preparation→Implementation→Operation，话机选型
5. **AOS 双分区配置状态**：certified/working 目录、配置备份恢复流程
6. **PoE 完整管理**：802.3 标准演进（af/at/bt）、功率预算、监控命令、LED 判断
7. **Inter VLAN Routing**：SMB 场景 VLAN 间路由配置

## 原文风格与引用注意
- 幻灯片短句 + 命令示例（`>>>` 提示符）+ Lab 步骤编号
- 与 T301（smb-lan-wlan-install）约 40% 内容同源（同为 SMB 交付线），提取时优先保留本书独有的 Enterprise 模式、语音 WLAN、故障排查深度内容

## 与站内其他书的关系
- stellar-wlan-express（本书）是 SMB 线最全的一本，覆盖三模式 + 语音 + 排查
- 与 campus-lan-presales 互补：本书偏动手配置，Campus LAN 偏方案设计
