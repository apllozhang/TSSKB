# glossary — bp-nms-brochures（型号与规格术语，按产品分组）

## OmniVista 平台
- **OmniVista Cirrus**：新一代云端网管平台，微服务架构，支持多租户/MSP <<<PAGE 9>>>
- **OmniVista Terra**：新一代本地部署网管，最多 5000 设备，VMware/Hyper-V 虚机 <<<PAGE 15>>>
- **OmniVista 2500**：上一代本地网管（本书仅目录级出现，迁移来源） <<<PAGE 10>>>
- **OmniVista Cirrus 4**：上一代云网管（迁移来源） <<<PAGE 10>>>
- **UPAM（Unified Policy Access Manager）**：内置 NAC 模块，认证/角色/访客/BYOD <<<PAGE 9>>>
- **QoE（Quality of Experience）**：用户体验质量指标：连接成功率、连接时长、漫游时间、覆盖 <<<PAGE 12>>>
- **AP-Group**：AP 管理实体，组内 AP 继承 SSID/ARP/RF 等全部配置 <<<PAGE 14>>>
- **Access Role Profile (ARP)**：设备接入角色模板（QoS/隧道/VLAN/带宽） <<<PAGE 14>>>
- **RF Profile**：射频配置模板（频段/信道/regulatory domain/关联速率） <<<PAGE 14>>>
- **Golden Configuration**：金标配置，用于配置比对与漂移审计 <<<PAGE 14>>>
- **DPI（Deep Packet Inspection）**：应用级深度包检测，交换机与 AP 均支持 <<<PAGE 14>>>
- **Heatmap**：Wi-Fi 覆盖/客户端密度热图，用于容量规划 <<<PAGE 13>>>
- **SPB（Shortest Path Bridging）**：最短路径桥接，Terra/Cirrus 提供图形化 fabric 视图 <<<PAGE 15>>>
- **Zero-Touch Provisioning**：AP 零触摸上线，免现场配置 <<<PAGE 10>>>
- **RADsec**：RADIUS over TLS，用户/设备认证加密 <<<PAGE 14>>>
- **MFA / 2FA**：多因子/双因子认证，网管登录保护 <<<PAGE 10>>>
- **SAML 2.0 SSO**：单点登录，支持 Okta 与 Microsoft Azure AD <<<PAGE 14>>>
- **GDPR / CCPA**：欧盟/加州数据隐私法规，Cirrus 数据中心合规 <<<PAGE 15>>>
- **SOC1 / SOC2**：数据中心安全审计认证 <<<PAGE 10>>>
- **NIS2**：欧盟网络安全指令，Fleet Supervision 支持合同合规检查场景 <<<PAGE 6>>>
- **Active-Active L2**：Terra 本地高可用模式 <<<PAGE 10>>>
- **MSP（Managed Service Provider）**：托管服务商，Cirrus 多租户顶层角色 <<<PAGE 15>>>

## 订阅 SKU 体系
- **OVCX-\*-BIZ/BAS/PRM-nY**：Cirrus 预付订阅（Base/Business/Premium，n=1/3/5 年） <<<PAGE 17>>>
- **OVTX-\*-BAS/BIZ/PRM-nY**：Terra 预付订阅（n=1/3/5/7 年） <<<PAGE 19>>>
- **OVCX-APL-***：低端 AP 订阅（AP1x0x/x1x/x2x） <<<PAGE 17>>>
- **OVCX-APH-***：高端 AP 订阅（AP1x3x/x4x/x5x/x6x/x7x） <<<PAGE 17>>>
- **OVC-C-ESS-M**：Cirrus Flexible Pay Essential 月度许可（AP+OS6360/6465/6560/6570M） <<<PAGE 19>>>
- **OVC-C-ADV-M**：Cirrus Flexible Pay Advanced 月度许可（OS6860/6865/6870/6900/9900 等） <<<PAGE 19>>>
- **NETAD-AP/SWITCH/TP-1Y/3Y/5Y**：Network Advisor 按设备类型订阅（AP/交换机/第三方） <<<PAGE 4>>>
- **AVR**：设备高级换新维护（Business/Premium 档包含） <<<PAGE 16>>>
- **Flexible Pay（OPEX mode）**：仅 Cirrus 可用的按月灵活付费模式 <<<PAGE 16>>>
- **NaaS（Network as a Service）**：网络即服务 Opex 运营模式 <<<PAGE 10>>>

## Network Advisor
- **OmniVista Network Advisor**：AI/ML 网络运维伴随工具，异常检测+一键/自动修复 <<<PAGE 1>>>
- **Rainbow CPaaS**：ALE 协作云平台，NetAdvisor 的 Bot/Bubble 交互载体 <<<PAGE 1>>>
- **Anomaly（异常）**：AI/ML 定义的偏离正常网络行为事件，可自定义 <<<PAGE 2>>>
- **Remediation**：修复动作，自动或用户发起 <<<PAGE 1>>>
- **Microsoft Teams support**：NetAdvisor 协作支持 Teams <<<PAGE 2>>>

## Fleet Supervision
- **Network Fleet Supervision**：免费在线资产与支持合规工具，自助注册 <<<PAGE 5>>>
- **End of Sales / End of Life**：停售/停维生命周期节点，用于换新预算规划 <<<PAGE 5>>>
- **Asset Collection**：资产采集，自动（多 OmniVista 系统）+手工导入序列号 <<<PAGE 6>>>

## Milestone Plugin
- **OmniSwitch Milestone Plugin**：与 Milestone VMS 集成的视频监控运维插件 <<<PAGE 7>>>
- **Milestone Systems VMS**：视频管理系统（第三方） <<<PAGE 7>>>
- **PoE priority per camera**：按摄像机设置 PoE 优先级，超预算保关键设备 <<<PAGE 8>>>

## Smart Tool
- **OST（OmniVista Smart Tool）**：OT/IoT 现场独立运维工具，免云免 CLI <<<PAGE 22>>>
- **PoE Wizard**：60 秒内诊断修复常见 PoE 问题的向导 <<<PAGE 23>>>
- **PoE Power Cycle**：一键 PoE 断电重启，保留人工确认 <<<PAGE 23>>>
- **TDR**：时域反射电缆健康测试 <<<PAGE 23>>>
- **Lightning Config**：OmniSwitch 首装配置向导 <<<PAGE 22>>>

## 版本/平台术语
- **AOS**：Alcatel-Lucent OmniSwitch 操作系统（NetAdvisor 要求 8.7R2+，新平台 8.9R1+） <<<PAGE 3>>> / <<<PAGE 15>>>
- **AWOS**：OmniAccess Stellar AP 无线操作系统（NetAdvisor 要求 4.0.3MR-3+，新平台 5.0.1MR+） <<<PAGE 3>>> / <<<PAGE 15>>>
- **ESXi**：VMware 虚拟化平台，Terra 要求版本 8+ <<<PAGE 15>>>
- **AVX/AVX2**：CPU 指令集，Terra 虚机硬性要求 <<<PAGE 15>>>
