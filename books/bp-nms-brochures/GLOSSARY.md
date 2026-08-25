# GLOSSARY · ALE 网管与运维工具彩页合集

> 页码为原书 `<<<PAGE N>>>` 标记。按五技能对应产品分组（主数据表平台/订阅、Network Advisor、Fleet、Milestone、Smart Tool/版本），精选 42 条。

## 主数据表：平台与代际（p9-21）
- **OmniVista Cirrus**：新一代云端网管平台，微服务架构，支持多租户/MSP <<<PAGE 9>>>
- **OmniVista Terra**：新一代本地部署网管，≤5000 设备，1-3 虚机，Active-Active L2 高可用 <<<PAGE 10>>>/<<<PAGE 15>>>
- **OmniVista 2500**：上一代本地网管，新平台迁移来源 <<<PAGE 10>>>
- **OmniVista Cirrus 4**：上一代云网管，迁移来源 <<<PAGE 10>>>
- **UPAM（Unified Policy Access Manager）**：内置 NAC 模块，认证/角色/访客/BYOD <<<PAGE 9>>>
- **Multi-tenancy**：多租户（MSP 顶层→租户→站点），仅 Cirrus 支持 <<<PAGE 10>>>/<<<PAGE 15>>>
- **Multi-sites Management**：单组织多站点，Cirrus 与 Terra 均支持 <<<PAGE 10>>>
- **Active-Active L2**：Terra 本地高可用模式 <<<PAGE 10>>>
- **Zero-Touch Provisioning**：AP 零触摸上线；交换机走模板自动化 <<<PAGE 10>>>
- **MSP（Managed Service Provider）**：托管服务商，Cirrus 多租户顶层角色 <<<PAGE 15>>>
- **NaaS（Network as a Service）**：网络即服务 OPEX 运营模式 <<<PAGE 10>>>

## 主数据表：平台功能术语（p9-21）
- **QoE（Quality of Experience）**：连接成功率/连接时长/漫游时间/覆盖等体验指标 <<<PAGE 12>>>
- **Heatmap**：Wi-Fi 覆盖与客户端密度热图，容量规划用 <<<PAGE 13>>>
- **AP-Group**：AP 管理实体，组内 AP 继承 SSID/ARP/RF 全部配置 <<<PAGE 14>>>
- **Access Role Profile（ARP）**：设备接入角色模板（QoS/隧道/VLAN/带宽） <<<PAGE 14>>>
- **RF Profile**：射频配置模板（频段/信道/regulatory domain） <<<PAGE 14>>>
- **Golden Configuration**：金标配置，比对与漂移审计 <<<PAGE 14>>>
- **DPI（Deep Packet Inspection）**：应用级深度包检测 <<<PAGE 14>>>
- **SPB（Shortest Path Bridging）**：最短路径桥接，新平台提供图形化 fabric 视图 <<<PAGE 14>>>/<<<PAGE 15>>>
- **RADsec**：RADIUS over TLS，认证加密 <<<PAGE 14>>>
- **SAML 2.0 SSO**：单点登录，支持 Okta 与 Microsoft Azure AD <<<PAGE 14>>>
- **MFA / 2FA**：多因子/双因子认证 <<<PAGE 10>>>
- **Celona Private 5G**：可被 Cirrus 集成纳管的私有 5G 小站 <<<PAGE 15>>>

## 主数据表：订阅 SKU（p9-21）
- **OVCX-\*-BIZ/BAS/PRM-nY**：Cirrus 预付订阅（Base/Business/Premium，1/3/5 年） <<<PAGE 17>>>
- **OVTX-\*-BAS/BIZ/PRM-nY**：Terra 预付订阅（1/3/5/7 年） <<<PAGE 19>>>
- **OVCX-APL-\***：低端 AP 订阅（AP1x0x/x1x/x2x） <<<PAGE 17>>>
- **OVCX-APH-\***：高端 AP 订阅（AP1x3x 及以上） <<<PAGE 17>>>
- **OVC-C-ESS-M**：Flexible Pay Essential 月度许可（AP+OS6360/6465/6560/6570M） <<<PAGE 19>>>
- **OVC-C-ADV-M**：Flexible Pay Advanced 月度许可（OS6860-9900 等） <<<PAGE 19>>>
- **Flexible Pay（OPEX mode）**：仅 Cirrus 可用的按月付费，12-60 月 <<<PAGE 16>>>/<<<PAGE 19>>>
- **AVR**：设备高级换新维护，Business/Premium 档包含 <<<PAGE 16>>>
- **NETAD-AP/SWITCH/TP-1Y/3Y/5Y**：Network Advisor 按设备类型订阅 <<<PAGE 4>>>

## Network Advisor（p1-4）
- **OmniVista Network Advisor**：AI/ML 运维伴随工具，异常检测+一键/自动修复 <<<PAGE 1>>>
- **Rainbow CPaaS**：ALE 协作云平台，NetAdvisor 的 Bot/Bubble 交互载体 <<<PAGE 1>>>
- **Anomaly（异常）**：AI/ML 定义的偏离正常行为事件，可自定义 <<<PAGE 2>>>
- **Remediation**：修复动作，自动或用户发起 <<<PAGE 1>>>
- **Microsoft Teams support**：NetAdvisor 协作支持 Teams <<<PAGE 2>>>

## Fleet Supervision（p5-6）与 Milestone Plugin（p7-8）
- **Network Fleet Supervision**：免费在线资产与支持合规工具，自助注册 <<<PAGE 5>>>
- **End of Sales / End of Life**：停售/停维生命周期节点 <<<PAGE 5>>>
- **NIS2**：欧盟网络安全指令，支持合同合规检查场景 <<<PAGE 6>>>
- **OmniSwitch Milestone Plugin**：与 Milestone VMS 集成的视频监控运维插件 <<<PAGE 7>>>
- **PoE priority per camera**：按摄像机设 PoE 优先级，超预算保关键设备 <<<PAGE 8>>>

## Smart Tool（p22-23）与版本门槛
- **OST（OmniVista Smart Tool）**：OT 现场独立运维工具，免云免 CLI <<<PAGE 22>>>
- **PoE Wizard**：60 秒内诊断修复常见 PoE 问题的向导 <<<PAGE 23>>>
- **TDR**：时域反射电缆健康测试 <<<PAGE 23>>>
- **Lightning Config**：OmniSwitch 首装配置向导 <<<PAGE 22>>>
- **AOS**：OmniSwitch 操作系统（NetAdvisor 要求 8.7R2+，新平台 8.9R1+） <<<PAGE 3>>>/<<<PAGE 15>>>
- **AWOS**：Stellar AP 无线操作系统（NetAdvisor 4.0.3MR-3+，新平台 5.0.1MR+） <<<PAGE 3>>>/<<<PAGE 15>>>

---
合计：42 条。
