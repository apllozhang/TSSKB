# 术语词典

| 术语 | 全称/中文 | 释义 | 首见 |
|---|---|---|---|
| UPAM | Unified Policy Authentication Management，统一策略认证管理 | OmniVista 内的统一接入管理模块，含 captive portal 与 RADIUS 服务器，服务 OmniSwitch 与 OmniAccess Stellar | 两份笔记 p3 |
| Zero Trust | 零信任 | 安全范式：无论接入位置，永不信任、始终验证；身份确认是第一道检查 | 两份笔记 p3 |
| FSSO | Fortinet Single Sign-On | Fortinet 透明认证机制：用户经第三方系统认证后即被 FortiGate/FortiAuthenticator/FortiCache 识别 | Fortinet p3 |
| RSSO | RADIUS Single Sign-On | FSSO 的一种实现：防火墙从 RADIUS Accounting 消息提取身份；也是 FortiGate 上连接器与用户组的类型名 | Fortinet p11/p13 |
| FortiGate / FortiAuthenticator | — | Fortinet 下一代防火墙 / Fortinet 身份认证管理设备（多防火墙场景可做 accounting 汇聚点） | Fortinet p3/p5 |
| User-ID | — | PAN 防火墙标准特性，利用多种信息源（含 syslog）建立 IP-用户映射 | PAN p3 |
| RADIUS Accounting | RADIUS 记账 | 认证成功后周期上报的会话信息报文，Fortinet 方案的身份载体，UDP 1813 | Fortinet p5 |
| Accounting Interim Interval | 记账中间间隔 | 周期性记账报文的间隔，默认 600 秒；PAN 方案要求小于 User Identification Timeout（45 分钟） | Fortinet p7 / PAN p5 |
| Filter-Id / filterID | — | RADIUS/syslog 中承载角色的属性；取值即 UPAM 侧 ARP/uNP 名，防火墙按它组策略 | Fortinet p12 / PAN p5 |
| ARP | Access Role Profile，访问角色档案 | UPAM 中定义的角色；默认 ARP 是未匹配/未本地定义时的兜底角色，须先于 Authentication Strategy 创建 | PAN p8 |
| uNP | User Network Profile，用户网络档案 | 与 ARP 同类的角色载体，filterID 所代表的内容之一 | PAN p5 |
| AAA Server Profile | AAA 服务器档案 | OmniVista 模板，指定认证与记账分别发往哪个 RADIUS 服务器；两方案的分叉点 | Fortinet p7 / PAN p6 |
| Authentication Strategy | 认证策略 | UPAM 中定义用哪个认证数据库及相关参数 | 两份笔记 p8 |
| Access Policy | 接入策略 | UPAM 中按 SSID/NAS IP/Location 等条件把认证请求路由到对应 Authentication Strategy | 两份笔记 p8-9 |
| Access Auth Profile | 接入认证档案 | 挂接 AAA Server Profile、配置 MAC/802.1x 认证选项（含 default 与 pass-alternate）并应用到交换机/AP 组的模板 | 两份笔记 p9-10 |
| pass-alternate | — | 返回属性与本地已定义 profile 不匹配时采用的备用 profile | 两份笔记 p9-10 |
| BYOD | Bring Your Own Device，自带设备 | 员工个人设备，可能无 AD 账号，是 UPAM 集成路线的主要对象 | 两份笔记 p3-4 |
| IoT | Internet of Things，物联网设备 | 常走 MAC 认证的终端类型，示例中的 Camera/Sensor/机顶盒 | 两份笔记 p4 |
| AD / NPAS | Active Directory / Network Policy and Access Services | 微软目录服务及其策略服务；域设备的首选集成点 | 两份笔记 p4 |
| changeType | — | UPAM syslog 字段：Access（认证成功）/ Accounting（周期记账）/ Disconnect（下线） | PAN p5 |
| deviceIP | — | UPAM syslog 字段：终端 IP；通常仅存在于 Accounting/Disconnect 消息 | PAN p5 |
| User Identification Timeout | 用户识别超时 | PAN 侧映射老化时间，默认 45 分钟；收不到 accounting 更新即登出 | PAN p5 |
| Syslog Parse Profile | syslog 解析过滤器 | PAN 上定义如何从 UPAM 日志提取 username/filterID 的配置；每个 syslog 源仅能挂一个 | PAN p11-13 |
| Server Monitoring（Syslog Sender） | — | PAN 的 User Identification 监控服务器配置：绑定 UPAM IP、UDP 与解析过滤器 | PAN p13 |
| captive portal | 强制门户 | Web 认证页面；IoT 设备一般不用 | 两份笔记 p3/p6 |
| 802.1x / MAC 认证 | — | 端口级 EAP 认证 / 按终端 MAC 地址认证 | 两份笔记 p3 |
