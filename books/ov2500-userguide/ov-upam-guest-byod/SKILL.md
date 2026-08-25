---
name: UPAM 认证中枢与 Guest/BYOD 策略
description: 需要配置 UPAM（内置 Captive Portal + RADIUS 服务器）、三种认证工作流（BYOD/Guest/MAC-802.1X）、NAS Client 与 Access Policy/Authentication Strategy、Guest 自助注册与社交登录、BYOD 策略、WiFi4EU、交换机用户账号（ASA）时使用。
source_book: OmniVista 2500 NMS 4.9R2 User Guide
---

## R（触发场景）
- 访客网络要 Web 认证 + 自助注册 + 短信/邮件审批
- 员工自带设备（BYOD）要 MAC+Portal 认证并绑定角色
- 交换机管理账号想统一走 UPAM 认证（ASA）
- 社交账号（Facebook/Google/Rainbow/WeChat）登录 Guest Wi-Fi

## I（核心理念）
UPAM 同时充当 Captive Portal 服务器与 RADIUS 服务器，应用分为 Summary / Authentication / Guest Access / BYOD Access / Settings 五区。认证策略双层：Access Policy（Priority 1-99 匹配）→ Authentication Strategy（认证源 × Web 认证四组合）。Guest 与 BYOD 是两套独立策略体系（各 ≤32 条含 Default），账号、有效期、设备数上限语义不同。

## A1（行动框架）
1. **UPAM 应用地图**（frameworks·F16，<<<PAGE 678>>>）：Authentication 子屏含 Summary/Workflow/NAS Clients/Access Policy/Authentication Strategy/Role Mapping for LDAP/Employee Account/Company Property/Switch User Account/Authentication Record/Captive Portal Access Record/Switch Access Record
2. **三种认证工作流选型**（frameworks·F17，<<<PAGE 681-682>>>）：BYOD（MAC+CP 对本地/外部库：SSID→MAC 的 Network Enforcement→认证源→Portal 页→Login Strategy→Web 认证 Enforcement）；Guest（MAC+CP 对 Guest 账号库，多一步 Self-Registration）；MAC or 802.1X（无 CP：SSID→认证源→Network Enforcement 三步）
3. **ASA 用例矩阵**（principles·P173，<<<PAGE 641-642>>>）：支持 UPAM 库同时做 ASA+客户端认证、UPAM 做 ASA+外部 RADIUS 做客户端；不支持外部 RADIUS 做 ASA+UPAM 做客户端

## A2（操作步骤）
- **NAS Client**：系统预置 All Managed Devices NAS（不可删），托管设备每 15 分钟自动入库，共享密钥固定 123456，与 UPAMRadiusServer 配套经 WLAN Service 下发；NAS IP 必须等于设备管理 IP；UPAM 作代理时 Shared Secret 四处一致（NAS Client+UPAM RADIUS+UPAM External RADIUS+第三方 RADIUS）（principles·P176，<<<PAGE 682-684>>>）
- **Access Policy / Authentication Strategy**：Access Policy Priority 1-99（1 最高）按 Basic+Advanced 属性匹配；Strategy 认证源四选（None/Local DB/External LDAP-AD/External RADIUS）× Web 认证（None/Guest/Employee/两者）四推荐组合；Employee Account 上绑定的 Access Role Profile/Policy List 优先于 Strategy（principles·P178，<<<PAGE 687-693>>>）
- **Guest Access Strategy**（frameworks·F18，<<<PAGE 712-718>>>）：General（Portal 模板+FQDN/IP）→Login Strategy（账密/条款/Access Code/Simple Persona 四种；社交登录 FB/Google/Rainbow/WeChat 需 OAuth ID+DNS 解析）→Registration Strategy（Remember Device+有效期）→Post Portal Enforcement（固定 ARP+Policy List+数据配额）→Self-Registration（审批 Employee Sponsor 或 Guest Operator；≤20 自定义属性）→Service Level（多档绑定不同 ARP）→WiFi4EU（专用模板+有效期 ≤24h）
- **Guest Account 机制**：Account 与 Access Code 两类；Data Quota 默认 1MB；批量创建一次最多 5000 个（前置 Global Configuration 启用）；打印凭据票；xls/csv/xlsx 导入（principles·P183，<<<PAGE 742-745>>>）
- **Company Property / Device Specific PSK**：公司资产设备清单绑定 ARP/Policy List 优先于 Strategy；每台设备按 MAC 派发不同 PSK；Online Devices 可 Kick Off（principles·P179，<<<PAGE 697-702>>>）
- **Switch User Account (ASA)**：建用户→AAA Profile（Unified Profile-Global Configuration-AAA）→Apply to Devices；权限三级 Read-Write/Read Only/Advanced（BitMap Calculator）（principles·P180，<<<PAGE 703-706>>>）
- **UPAM Settings 集成**：Email SMTP；External Log Server（MySQL/MSSQL/Syslog，本地日志仅存 1 个月）；LDAP/AD（AD 须设为 DNS 服务器）；External RADIUS；Captive Portal 页六种布局+自定义 Logo/广告；RADIUS 服务器证书六步 openssl 流程（principles·P186，<<<PAGE 767-778>>>）

## E（实证案例）
- Guest Access Strategy 七段式配置（General→Login→Registration→Enforcement→Self-Registration→Service Level→WiFi4EU）（frameworks·F18，<<<PAGE 712-718>>>）
- Authentication Record 的 Generate：任意记录可生成 PSK；Fail+Local DB+802.1X 可生成 Employee Account；Fail+Call Check 可入 Company Property（principles·P181，<<<PAGE 710>>>）
- Guest 自助注册审批链（Employee Sponsor 邮箱后缀/位置路由 Guest Operator）（principles·P184，<<<PAGE 746-756>>>）

## B（反例/坑）
- UPAM RADIUS Shared Secret 改动必须同步 NAS Client 屏，否则全网认证失败（counter·X25，<<<PAGE 224>>>）
- 删除认证服务器不影响交换机继续使用——会产生"幽灵服务器"（counter·X24，<<<PAGE 221-222, 226>>>）
- Message-Authenticator：UPAM 开 Require 会丢弃无该属性的请求（即 AOS 8.10R1 及以下交换机的请求）；混合网络建多个 NAS 段分别设置（principles·P177，<<<PAGE 685-687>>>）
- Guest Data Quota 仅对账密登录生效，Access Code/条款用户不限（principles·P182，<<<PAGE 714-718>>>）
- Guest 账号有效期不能超 Global Configuration 全局上限（默认 90 天）；Remembered Device 只有 Activated 状态才消耗 Guest 许可（principles·P183/P184，<<<PAGE 742-756>>>）
- 社交登录需本地 DNS 把 Portal Server Domain 解析到 UPAM IP；WeChat PC 端须建网站应用且 Verified（付费）（principles·P183，<<<PAGE 720-742>>>）
- BYOD 无自助注册/Access Code/Data Quota；Max Device Per Account 仅 1-10 默认 5（Guest 默认 10）（principles·P185，<<<PAGE 756-766>>>）
- Guest Operator 登录用 OV 的 secondary IP 管理界面（principles·P185）
- 默认客户端/服务器证书不安全，正式环境必须换自定义证书（counter·X13，<<<PAGE 141>>>）
- UPAM 邮件要在 UPAM Settings-Email Server 单独配置，不吃 OV 的 Preferences（principles·P121，<<<PAGE 425-427>>>）

## 来源
OmniVista 2500 NMS 4.9R2 User Guide 第 33 章 UPAM（<<<PAGE 678-778>>>）、认证服务器相关（<<<PAGE 218-227>>>）。条目来源：frameworks F16/F17/F18；principles P173-P186；counter-examples X13/X24/X25。
