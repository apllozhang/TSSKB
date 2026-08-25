# frameworks 候选提取 · OmniVista 2500 NMS 4.9R2 User Guide

来源: source/fulltext.md（页码为原文 <<<PAGE N>>> 标记）

## F1. OV2500 应用功能地图（LAN+WLAN 菜单） <<<PAGE 31-32>>>
摘录："Network: Discovery/Topology/AP Registration/SAA/Locator/Notifications/VM Manager/Analytics/Application Visibility/Provisioning/IoT; Configuration: VLANs/Services/VXLANs/IP Multicast/CLI Scripting/PolicyView/SIP/Captive Portal/Groups/...; Unified Access; Security: ...Quarantine Manager; Administration: Control Panel/Preferences/Audit/License/OV System Health; UPAM: Summary/Authentication/Guest Access/BYOD Access/Settings/Web Content Filtering; WLAN: SSIDs/WIPS/RF Management/Heat Map/Floor Plan/Client"。
说明：查"某任务在哪个应用里配"的总地图。另见 WLAN Menu 视图 <<<PAGE 33-34>>>（SSID/APs/Analytics/Clients/IoT/Guest-BYOD/Authentication/Policies/RF/Security/Alarms-Logs/Administration 分组；内容与 LAN+WLAN 相同，仅入口重组）。

## F2. 仪表盘四标签定制框架 <<<PAGE 45, 54-56>>>
摘录："The Global tab displays all selected widgets for all applications (Default); the WLAN Advanced tab...IoT tab...Performance Monitoring tab displays all selected Analytics Statistics Charts"。
说明：Dashboard = Global / WLAN Advanced / IoT / Performance Monitoring 四标签；Performance Monitoring 挂 Analytics Chart View Profile（Network→Analytics→Statistics→Chart Views 创建），最多 20 个 widget，删 Profile 则 widget 一并移除。

## F3. Analytics 报表前置工作流（Profile 驱动） <<<PAGE 66-67>>>
摘录："to generate Top N Applications, Top N Clients, and Top N Ports Utilization Reports, you must first create an Analytics Profile... You do not need to create a profile for Network Availability, Alarms, Network Health, or SIP Reports"。
说明：流程 = Profiles 建 Analytics Profile（设备/端口+信息类型）→ Reports 出报表；Top N Apps-Advanced 由 Application Visibility 的 Signature Profile 驱动；实时类报表（Availability/Alarms/Health/SIP）免 Profile。

## F4. Analytics 数据趋势下钻模型 <<<PAGE 72-74>>>
摘录："Monthly Details View - A Weekly Trending View; Weekly Details View - Daily; Daily Details View - Hourly; Hourly Details View - 15-minutes"。
说明：固定粒度下钻链：月→周→日→时→15 分钟。

## F5. Analytics Statistics 四屏采集/查看模型 <<<PAGE 117>>>
摘录："Statistics - Used to quickly view current statistics...Collection - Used to create custom Collection Profiles...Chart Views - Used to create View Profiles to view statistics data...Settings - Used to enable and configure automatic statistics collection from new switches"。
说明：采集与查看解耦：Collection Profile（采集什么）＋View Profile（怎么看，独立于 Collection Profile）＋Default Collection Profile（所有托管交换机自动入组）。

## F6. 基础统计工作流四步 <<<PAGE 117-118>>>
1) View/Modify Default Collection Profile（Statistics→Collection→Edit Default Profile）；2) Managed Devices 表选交换机→Features→Enable Statistics；3) Statistics→Chart Views 建 View Profile；4) 点 Profile 名看图（可入 Performance Monitoring Dashboard）。自动模式：Settings 里 "Enable Statistics Automatically On" 设 All/N 台，新交换机自动入 Default Profile。

## F7. Stellar AP 纳管状态机/工作流 <<<PAGE 137, 139>>>
摘录："OmniVista initially classifies the AP as 'unmanaged'...The Network Admin can review these APs and place them into a 'trusted' state"。
流程：接入→DHCP Option 43/138 找到 OV→注册进 Unmanaged List（可能因未授权/未信任/国家码冲突滞留）→管理员 Trust→进 Managed List + Hardware Inventory + Topology + Default AP Group→可建新 AP Group 移入（AP 只属一组）→按组下发配置。Trust All/Untrust All 锁图标控制新 AP 默认信任行为 <<<PAGE 143>>>。

## F8. AP 作为 802.1X 客户端的四种认证拓扑 <<<PAGE 140-141>>>
① UPAM 作 802.1X 服务器+AP 内置证书；② UPAM+自定义客户端证书（外部生成→AP Registration-Certificate 导入→UPAM-Settings-AP 802.1X Trust CA 导入 CA→推给 AP）；③ 外部 RADIUS+内置证书（从 UPAM 下载 CA 导入外部 RADIUS）；④ 外部 RADIUS+自定义证书。另有用户名(AP MAC)方式：UPAM 配 user/pass=MAC，返回 UNP profile/VLAN。

## F9. mDNS 三种部署模式地图 <<<PAGE 350-352>>>
摘录："Gateway mDNS - Uses an OmniSwitch as a gateway to relay mDNS messages...Responder mDNS - Uses Responder Switches...also enables you to configure and apply rules and policies...Legacy mDNS - Uses a GRE Tunnel between an OmniSwitch and a WLAN Controller...limited to L2"。
说明：无 WLAN 控制器选 Gateway（VLAN 泛洪，模型简单）；需跨 VLAN+策略管控选 Responder（Responder+Edge+Service Rule/Server Policy/Client Policy）；旧 WLAN 控制器环境用 Legacy（L2 GRE 隧道，仅同 VLAN 发现）。

## F10. Responder mDNS 配置工作流 <<<PAGE 354-356>>>
1) 建 Responder Device（Loopback0 IP 自动预填/新建）；2) 配 Edge Devices（可勾 "Use These Common Configs" 统一下发 VLAN/SSID/mDNS 状态；Edge=AOS 8.5R1+ 交换机或 AWOS 4.0.1+ AP 除 AP1101）；3) 建 Service Rules（= Service ID + Server Policy + Client Policy，二者必居其一）。顺序敏感：先配 Responder/Edge 再放用户入网，否则用户须重新共享服务。

## F11. Provisioning（零接触部署）工作流 <<<PAGE 430-436>>>
摘录："When a switch boots up, it contacts the DHCP Server and gets the location of the OmniVista Activation Server. The Cloud Agent on the switch then makes an HTTPS call...matched to a Provisioning Rule...OmniVista then uses SSH to log into the switch"。
流程：DHCP（Option 43 Sub128=as-lite.myovcloud.net + Sub134=端口 443）→DNS 解析 as-lite 到 OV→交换机 Cloud Agent 每 5 分钟 Call-Home→匹配 Provisioning Rule（按序列号/MAC/型号）→SSH 推送 Management+Configuration 模板→入 Managed Devices→自动建备份任务。未匹配时两种策略：Allow Onboard（推默认管理模板）或 Do Not Allow（自动建序列号 Rule 状态 No Match）。

## F12. Thin Switch（瘦交换机）部署模型 <<<PAGE 436-438>>>
AOS 8.8R1+；交换机自身不知道自己是瘦模式（OV 通过 Call-Home 告知）；write memory 失效；Initial Call-Home（每次重启后第一次，OV 宣告瘦模式）与 Periodic Call-Home（增量模板仅在此时下发）两类；Desired Switch Config 三选：Template+Incremental / 最新备份快照 / Golden Config 快照（默认）；规则只按序列号/MAC 匹配（型号不适用）；已托管交换机必须先删除才能建瘦规则。

## F13. Quarantine Manager 事件处理链（状态机） <<<PAGE 457, 460-465>>>
摘录："Quarantine Manager Rules determine which Syslog events or SNMP traps cause a device to be placed in the Candidates List or Banned List, or released"。
状态流：IPS/交换机事件→规则匹配（Banned 优先于 Candidate）→①Candidate List（流量照常，管理员 Release/Ban/Never Ban）→②Banned List（进隔离 VLAN，State: Scheduled to be Banned→Completed/Partially Banned，管理员 Release）→③Disabled Ports（端口禁用列表，须逐条 Release 后端口才恢复）；关键设备走 Never Banned（OV 与交换机隐式在内）；无线客户端改走 Client Blocklist。

## F14. Topology 三层地图体系 <<<PAGE 580-581>>>
Physical Network Map（自动、全设备、不可删）→ Child Map（从父图建，设备从父图移入）→ Logical Map（无父图，设备可同时在多图）；Dynamic Map 用过滤器动态加减设备（不能与 Logical 互转，可改过滤器）；克隆地图预选全部设备；Admin 建/删图、Netadmin/Write 编辑；大图减少设备可提升渲染性能。

## F15. Unified Access 配置三途径 <<<PAGE 592>>>
Workflow（六种引导流程：分类规则/802.1X/MAC/802.1X+MAC/MAC+Captive Portal/ClearPass 全家桶）→ Template（Access Auth Profile、WLAN Service Profile、Access Role Profile、AAA Server Profile 等模板批量下发）→ Device Config（单设备微调）＋Profile Polling（轮询同步）。
认证分层：L2（802.1X/MAC/分类规则→定 UNP+VLAN，之后不变）→L3（QMR、MAC 黑名单、位置/时间校验动态改 Policy List/Role）。

## F16. UPAM 应用地图 <<<PAGE 678>>>
摘录："UPAM supports both captive portal server and RADIUS server; and can be used to implement multiple authentication methods...Summary / Authentication / Guest Access / BYOD Access / Settings"。
Authentication 子屏：Summary（认证结果/Top10 NAS/失败原因）/Workflow（BYOD/Guest/MAC-802.1X 三类引导流）/NAS Clients/Access Policy/Authentication Strategy/Role Mapping for LDAP/Employee Account/Company Property/Switch User Account/Authentication Record/Captive Portal Access Record/Switch Access Record。

## F17. UPAM 三种认证工作流 <<<PAGE 681-682>>>
BYOD Access（MAC+Captive Portal 对本地/外部库）：SSID→MAC 的 Network Enforcement→认证源→Portal 页→Login Strategy→Web 认证 Enforcement；Guest Access（MAC+CP 对 Guest 账号库）：同上+Self-Registration；MAC or 802.1X（无 CP）：SSID→认证源→Network Enforcement 三步。

## F18. UPAM Guest Access 策略体系 <<<PAGE 712-718>>>
Guest Access Strategy（≤32 条，含预置 Default）：General（Portal 模板+https/http+FQDN/IP）→Login Strategy（四种登录方式：Username&Password / Terms&Condition / Access Code / Simple Persona；重置密码邮件/SMS 验证码；社交登录 FB/Google/Rainbow/WeChat 需 OAuth ID+DNS 解析）→Registration Strategy（Remember Device+有效期，Terms/Persona 时必填）→Post Portal Enforcement（固定 ARP+Policy List+数据配额+Quota Exhausted URL）→Self-Registration Strategy（仅账密登录适用；账号名取 Guest Name/Email/Phone；密码手动/自动邮件；审批 Employee Sponsor（邮箱后缀/全址）或 Guest Operator（位置路由）；≤20 自定义属性；验证码校验）→Service Level（多档服务绑定不同 ARP）→WiFi4EU（须专用模板+有效期 ≤24h）。

<!-- APPEND -->
