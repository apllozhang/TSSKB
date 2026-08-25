# frameworks — sol-network-security

## F1 ALE 五层集成安全框架 <<<PAGE 5-6>>>
自下而上/由内而外的分层防御清单：
1. 用户级：始终认证授权，用策略与配置文件约束访问权
2. 设备级：设备认证 + 合规检查（杀毒、OS 版本预扫描）
3. 应用级：按应用设规则（阻断、限速、身份限定）
4. 网络级：交换机/AP 智能分析提供可见性 + DPI 识别异常流量
5. IoT 级：虚拟容器（网络虚拟化）隔离，单点失陷不扩散

## F2 三平面安全加固框架 <<<PAGE 9-47>>>
全册主结构，适用于任何网络设备安全审计：
1. 管理面（Management Plane）：设备访问、AAA、证书、SNMP、日志、安全模式
2. 控制面（Control Plane）：路由/标签/链路管理/发现/网管协议认证与防护
3. 数据面（Data Plane）：链路加密（MACsec）、地址族防护、端口安全（LPS）

## F3 协议替换对照框架 <<<PAGE 12>>>
不安全协议 → 安全替换的决策表：
| 不安全 | 替换 | 原因 |
|---|---|---|
| Telnet | SSH | 无加密无证书 |
| FTP/TFTP | SFTP/SCP | 无加密无证书 |
| SNMPv1/v2c | SNMPv3 | 仅社区串认证 |
| HTTP | HTTPS | 明文协议 |

## F4 视频监控网络生命周期 7 阶段框架（NLM） <<<PAGE 89>>>
1. 规划与设计（Five S's：Software / Surveillance IoT / Servers-Storage / Switches / Services-Support）
2. 部署（UNP、Lightning Config、边缘认证上线）
3. 运营管理（持续监控、API/VMS 集成、主动补丁）
4. 故障维护（固件升级、冗余切换、软件工具包）
5. 升级优化（AI、Network Advisor、分阶段换新）
6. 合规与文档（安全审计、网络保险、文档留存）
7. 退役与重部署（数据安全迁移、按隐私法擦除处置）
