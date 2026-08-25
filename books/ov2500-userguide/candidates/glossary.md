# glossary 候选提取 · OmniVista 2500 NMS 4.9R2 User Guide

来源: source/fulltext.md（页码为原文 <<<PAGE N>>> 标记）

## 第 1-2 章 入门/仪表盘
- **NMS (Network Management System)**：网管系统，此处指 OmniVista 2500 <<<PAGE 1>>>
- **Dashboard / Widget**：主页仪表盘及其应用小部件，可增删/拖拽/配置刷新率 <<<PAGE 45, 50>>>
- **LAN+WLAN Menu / WLAN Menu**：两种应用菜单视图，后者仅重组入口为 WLAN 专用分组，内容相同 <<<PAGE 31, 33>>>
- **Unacknowledged Alarm Display**：所有页面底部实时显示的未确认告警分类计数 <<<PAGE 31>>>
- **Favorites Widget**：应用快捷方式收藏部件，加入后同步出现在主导航 Favorites 标签 <<<PAGE 36>>>
- **Table View / List View**：表格/列表两种显示模式；List View 不可打印/导出 <<<PAGE 37>>>
- **Discovery Profile**：发现参数集（SNMP 版本、FTP/Telnet 密码等）<<<PAGE 40>>>
- **Write Community Name**：SNMP 写团体名，发现后默认 public <<<PAGE 42>>>
- **certified / working directory**：AOS 交换机 flash 中已认证/待测试配置目录 <<<PAGE 43>>>
- **running configuration**：RAM 中当前运行配置，重启即丢 <<<PAGE 43>>>
- **EMP Port**：交换机管理口，sFlow 不能经其发送 <<<PAGE 75>>>

## 第 3 章 Analytics
- **Analytics Profile**：定义监控的交换机/端口与信息类型，Top N 报表前置条件 <<<PAGE 66>>>
- **sFlow**：流采样协议，Top N Apps/Clients 数据来源，按 TCP/UDP 端口识别应用 <<<PAGE 67>>>
- **Summary View / Detail View / Trending View**：报表汇总/明细/趋势三级视图 <<<PAGE 68, 71, 72>>>
- **Applications Management**：端口↔应用映射维护屏 <<<PAGE 66>>>
- **Anomaly**：基于历史使用偏离正常范围的利用率数据点 <<<PAGE 66>>>
- **Signature Profile**：Application Visibility 中定义的 L7 应用签名监控配置 <<<PAGE 66>>>
- **UNP (User Network Profile)**：统一网络档案，即按用户/终端分类的接入角色档案 <<<PAGE 88>>>
- **App Flow Count / App Bandwidth Usage**：L7 应用流量两类视图（流数 vs 包/字节数）<<<PAGE 82, 86>>>
- **Network Advisor**：OmniVista Network Advisor 云实例，可接管设备监控 <<<PAGE 58>>>

- **Collection Profile / View Profile**：统计采集档案（设备+属性+轮询+保留期）/ 统计查看档案（≤50 计数器）<<<PAGE 120, 122>>>
- **Counter / Scale**：图表中一条统计线；Scale 为绘图乘数(0.001-1000) <<<PAGE 123>>>
- **Z-Score / Anomaly**：端口利用率异常检测统计量；偏离既定模式的数据点 <<<PAGE 133>>>
- **Prediction: Training Timeout / Training Error**：端口利用率机器学习预测的训练时长/目标误差 <<<PAGE 105, 134>>>
- **AP Uptime/Downtime**：基于注册时间或 alaOVSwitchUp/Down trap 的 AP 可用性报表（30 天/5000 条）<<<PAGE 116>>>

## 第 4 章 AP Registration
- **Stellar AP (OAW)**：ALE OmniAccess Stellar 无线接入点系列 <<<PAGE 137>>>
- **Managed / Unmanaged AP**：已信任+已授权的可管理 AP / 未信任、未授权或配置冲突的 AP <<<PAGE 142>>>
- **AP Group**：AP 管理单位，配置按组下发，AP 仅属一组，初始在 Default AP Group <<<PAGE 137, 139>>>
- **DHCP Option 43 / Option 138**：AP 定位 OmniVista 的 DHCP 选项（ALE vendor ID / OV 服务器 IP）<<<PAGE 140, 142>>>
- **Country Code Conflict**：AP 与 AP Group 国家码不一致导致 AP 无法纳管 <<<PAGE 143>>>
- **Init Registration App**：首次打开 AP Registration 的预配置窗口（国家码、Trust 状态）<<<PAGE 143>>>
- **Remote AP (RAP)**：经 VPN 由本地 OV 管理的远端 AP，需 AWOS 4.0.0.xx+ <<<PAGE 142>>>
- **Web UI Device Management Tool**：通过证书建立的 OV-AP 安全连接管理单台 AP 的 Web 工具 <<<PAGE 138>>>
- **Data VPN / Management VPN**：AP 与 VPN 服务器间承载数据流量的隧道 / AP 与 OV 间管理隧道 <<<PAGE 157, 178（TOC）>>>

- **Use Private Config**：单 AP 覆盖 AP Group 配置的开关（IoT Radio/RF/WCF/位置服务）<<<PAGE 147>>>
- **Zigbee / BLE Beaconing**：AP IoT Radio 两种模式；BLE 用于定位/资产追踪（iBeacon/Eddystone 协议）<<<PAGE 148-149>>>
- **PAN ID**：Zigbee 个域网标识，默认取 AP MAC 后两字节 <<<PAGE 148>>>
- **Dedicated Scanning Mode**：AP 专用射频扫描模式（Once/Always/Off）<<<PAGE 146-147>>>
- **Mesh / Bridge Mode**：AP 无线网桥/网状回传工作模式；MLO 多链路操作仅 Wi-Fi 7 <<<PAGE 150, 154>>>
- **Auto Group VLANs**：AP Group 按 LLDP 管理 VLAN 自动归组 <<<PAGE 165>>>
- **Extended SSID Scale**：AP Group 扩展到 14 SSID 的开关 <<<PAGE 166>>>
- **Post Mortem Dump (PMD)**：AP 故障信息转储到 TFTP 服务器 <<<PAGE 167>>>
- **Client Behavior Tracking**：客户端行为日志上传（SFTP/TFTP/Syslog）<<<PAGE 167>>>
- **RadSec**：RADIUS-over-TLS，AP 与第三方 RADIUS 的安全通信 <<<PAGE 168>>>
- **OmniVista Cirrus**：ALE 云端网管（Freemium 账号用于 RAP 激活）<<<PAGE 160>>>
- **WiFi RTLS / Advanced Analytics Server Profile**：AP 上报实时定位/高级分析数据的目标服务器档案 <<<PAGE 171>>>
- **WCF (Web Content Filtering)**：按安全/内容类别的网页过滤，挂在 Access Role Profile 或 SSID 下推给 AP Group <<<PAGE 151, 171>>>
- **Virtual IP Address (Captive Portal)**：AP 内 Captive Portal 重定向用虚拟 IP，可自定义以隐藏管理口 <<<PAGE 171>>>
- **Called-Station-Id**：RADIUS 属性，可携带 AP 位置等信息给认证服务器 <<<PAGE 172>>>

- **Certificate（AP Registration）**：Web Server/外部 Portal、Local LDAP、802.1X Client、Local RadSec、Stellar BLE、Syslog Over TLS、Stellar WiFi RTLS、Default Internal CP 八类证书 <<<PAGE 178-187>>>
- **cportal Certificate**：AP 内置 Captive Portal 证书，全局档案到期前 30 天告警 <<<PAGE 186>>>
- **Kafka**：BLE/WiFi RTLS 数据上报通道 <<<PAGE 182>>>
- **Aeroscout / Stellar Asset Tracking / Assa Abloy Visionline**：定位引擎/BLE 资产追踪/Zigbee 门锁服务器 <<<PAGE 191-192>>>
- **QoE Events**：AP 上报 Cirrus 的高级分析事件类型（用户/AP/无线/非法 AP 等 12 类）<<<PAGE 193>>>
- **Data VPN Server**：Remote AP 用户流量隧道端点，可导出 .conf <<<PAGE 195-196>>>
- **L3 Redundancy (HA)**：OV 双机主备（Keepalive/Retries/Preemption），AP13XX+AWOS5.0+ <<<PAGE 197>>>

## 第 5 章 App Launch
- **App Launch**：OV 内嵌 Web 应用快捷方式页，图标 ≤60x60 px <<<PAGE 199>>>

## 第 6 章 Application Visibility
- **Application Visibility**：基于应用签名的 L7 流量识别+QoS/UNP 管控（OS6860E 与 AP）<<<PAGE 201>>>
- **Signature File / Signature Profile**：ALE 提供的应用签名库 / 从签名文件挑出的监控+管控组合 <<<PAGE 202>>>
- **Application Enforcement**：按签名组给流量施加 QoS/UNP 策略（需配合 Access Role Profile）<<<PAGE 202>>>
- **Sync Status**：交换机上签名档案与 OV 档案是否一致 <<<PAGE 203>>>

- **Default Profile (Signature)**：导入签名文件时自动生成的全量档案，可克隆修改但不可编辑 <<<PAGE 208>>>
- **Out of Sync**：设备签名档案与 OV 存档不一致状态 <<<PAGE 203>>>

## 第 7 章 Audit
- **Audit 应用**：按类型查看/搜索/过滤/下载 OV 日志（Network/Configuration/Unified Access/Security/System/UPAM 等分类）<<<PAGE 212-213>>>
- **Log Central (ngnms.log)**：所有日志实时汇总的单文件视图 <<<PAGE 214>>>
- **Collect Support Information**：从设备收集 swlog/cfg/Show Tech 系列日志打 ZIP 给 ALE 支持，不支持无线设备 <<<PAGE 216>>>
- **User Activity Report**：用户活动报表，默认保留 90 天 <<<PAGE 217>>>

## 第 8 章 Authentication Servers
- **LDAP / LDAPS**：目录认证协议；SSL 时端口自动 389→636 <<<PAGE 219, 221>>>
- **VSA (Vendor Specific Attribute)**：RADIUS 厂商私有属性，承载认证/授权/配置详情 <<<PAGE 219>>>
- **ACE Server**：双因素认证服务器，单台限制，靠 sdconf.rec 文件下发配置 <<<PAGE 219>>>
- **TACACS+**：基于 TCP 的认证/授权/计费协议（RFC 1321 提及），交换机内置客户端 <<<PAGE 219>>>
- **Shared Secret**：RADIUS 服务器共享密码（≤64 字符）<<<PAGE 225>>>
- **RadSec**：RADIUS over TLS；Stellar AP 仅支持单个 RadSec 服务器 <<<PAGE 225>>>
- **Use as On-Premises Server**：LDAP 私有化部署选项，AP 认证请求直连本地 LDAP/AD（仅 BYOD）<<<PAGE 221>>>
- **Search Base**：LDAP 认证信息查找起始点（如 o=alcatel.com）<<<PAGE 221>>>

## 第 9 章 Captive Portal
- **Captive Portal**：Web 页面取凭证 + RADIUS 认证；OmniSwitch 内置 Web 服务器呈现页面 <<<PAGE 231>>>
- **Captive Portal Configuration/Profile/Domain Policy**：全局配置 / 按角色档案覆盖 / 按登录域(realm)替换策略三层模型 <<<PAGE 232-235>>>
- **Realm (Suffix/Prefix)**：用户名中的域标识（如 NA02/tut 或 tu@alu.com）<<<PAGE 234>>>
- **Redirect IP/Success Redirect URL**：Portal 重定向地址与认证成功跳转 URL <<<PAGE 232>>>
- **Customization Archive**：交换机 CP 网页文件 zip 包，可导入-编辑-回推 <<<PAGE 235>>>

## 第 10 章 CLI Scripting
- **CLI Script File**：文本脚本（.script），CLI+JavaScript 混编，批量配置设备 <<<PAGE 238>>>
- **Shared Admin Script (shadmin)**：管理员共享脚本前缀 <<<PAGE 239>>>
- **<tapps> 指令**：set timeout / import / second password / lastcmd 四个脚本指令 <<<PAGE 243-244>>>
- **内置变量 ($IP_ADDRESS/$BASE_MAC 等)**：发送时自动替换的设备属性变量 <<<PAGE 242-243>>>
- **expectPrompt/lastcmd**：训练脚本应答确认提示 / 声明最后命令防会话挂起 <<<PAGE 241, 244>>>

## 第 11 章 Control Panel
- **Watchdog**：OV 内部服务状态监控与启停 <<<PAGE 249>>>
- **Scheduler Jobs（System/User-Defined）**：系统自动任务（不可改）/ 用户任务 <<<PAGE 250>>>
- **Overlap Policy / Crash Policy**：任务重叠（跳过/重启）与崩溃（重来/续跑）策略 <<<PAGE 251>>>
- **Session Management**：在线客户端会话列表，可强制登出 <<<PAGE 253>>>

## 第 12 章 Discovery
- **Discovery Range / Discovery Profile**：IP 范围与发现参数集（SNMP/凭据/Shell），多档案按序回退 <<<PAGE 255-256>>>
- **Shell Preference**：设备默认 CLI（SSH/Telnet），SSH 时 Resource Manager 用 SFTP，默认 SSH <<<PAGE 260>>>
- **Get Bulk / Max Repetitions**：SNMPv2 大表批量读取操作及每次请求行数 <<<PAGE 260>>>
- **Discover Link (Normally / As OEM Device)**：邻接协议发现 / Locator 终端搜索算法发现 <<<PAGE 280>>>
- **SNMP Status**：AOS 设备可管理性状态（区别于 Up/Down 可达性）<<<PAGE 272>>>
- **Changes (Certified/Uncertified/Unsaved)**：交换机配置保存状态三值 <<<PAGE 273>>>
- **Running From**：AOS 当前从 certified 还是 working 目录启动 <<<PAGE 273>>>
- **NaaS / CAPEX / CAPEX Undecided**：订阅式/买断式/未决设备许可模式（AOS 8.8R1+）<<<PAGE 283>>>
- **Grace Period / Degraded Mode**：NaaS 过期 30 天宽限 / 降级（禁改配置禁升级）<<<PAGE 285>>>
- **Mibset / Import MIBs**：第三方设备 MIB 集目录与其导入（.mib 文件）<<<PAGE 287-288>>>
- **Thin Switch Client**：瘦交换机模式（AOS 8.8R1+，Call-Home 每 30 分钟上报状态）<<<PAGE 271>>>
- **Network Advisor**：基于 Syslog 的异常检测云工具，经 Rainbow 告警 <<<PAGE 264>>>
- **Application UUID**：Network Advisor 实例唯一标识，装好后在实例首页查看 <<<PAGE 266>>>
- **Manual Link**：手工创建的持久链路，断链红色显示 <<<PAGE 290>>>

- **Scheduled Upgrade / Time Window / Recurrence**：定时升级计划（一次性/日/周/月/工作日），窗口耗尽未升级设备等下次递归 <<<PAGE 292-293>>>
- **BMF**：U-Boot/Miniboot 固件升级类型（与 Image 并列）<<<PAGE 294>>>
- **ERP (Ethernet Ring Protection) / Ring ID**：以太环网保护及其链路标识 <<<PAGE 292>>>
- **Full/Occasional/Regular/Frequent Updates**：四级自动发现轮询（含内容逐级递增）<<<PAGE 297-298>>>
- **IP Failover**：主 IP 失败后 OV 改用设备备用 IP <<<PAGE 299>>>
- **REST API Polling**：以 REST 替代 SNMP 轮询（Locator/LLDP/SPB），AOS 8.7R3+ <<<PAGE 299>>>
- **SPB / ISID / SAP / SDP / BVLAN**：最短路径桥接、服务标识、服务接入点、服务分发点、承载 ISIS-SPB 控制流量的基础 VLAN <<<PAGE 297>>>
- **External Apps API Key**：外部应用访问 OV 的 API 安全密钥 <<<PAGE 301>>>

## 第 14 章 Groups
- **MAC/VLAN/Network/Multicast/Service Group**：五类策略条件用组，存于 OV 内置 LDAP <<<PAGE 302-305>>>
- **Service / Service Port**：协议+源/目的端口的服务定义与端口对象 <<<PAGE 306-307>>>

## 第 15 章 IoT
- **IoT 应用**：终端指纹识别与分类清单（MQTT+Device Fingerprinting Service）<<<PAGE 308-309>>>
- **Device Fingerprinting Service (api.fingerbank.org)**：云端设备指纹分类服务 <<<PAGE 310>>>
- **Category / Category Hierarchy**：设备类别及其层级（Category/Manufacturer/Endpoint name）<<<PAGE 311-312>>>
- **UNP Type（六种）**：Default/Pass-Alternate/Auth-Server Down/From Classification/From RADIUS/From OmniVista Enforcement <<<PAGE 312>>>
- **Enforcement Status**：IoT 分类强制状态（Initial/Excluded/Enforced/Failed/Pending/Disabled）<<<PAGE 312-313>>>
- **Google Workspace 集成**：对接 Google 采集 Chrome 设备信息（AOS 8.6R2+）<<<PAGE 310, 314>>>

- **LQI (Link Quality Index)**：Zigbee 链路质量百分比，>30% 可靠、<10% 断通 <<<PAGE 316>>>
- **IoT Enforcement / Exception List**：按类别绑定 Access Role Profile 的强制及四类豁免 <<<PAGE 319, 321>>>

## 第 16 章 IP Multicast (PIM)
- **PIM (Protocol-Independent Multicast)**：组播路由协议，VXLAN 组播的前置 <<<PAGE 324>>>
- **PIM Global Profile / PIM Interface / PIM Candidate**：全局使能档案 / 组播路由接口 / C-BSR+C-RP 候选 <<<PAGE 324-327>>>
- **RP / BSR / C-RP / C-BSR**：汇聚点 / 自举路由器及其候选；每域一个 BSR，高优先级（同优先比高 IP）当选 <<<PAGE 327>>>

## 第 17 章 License Management
- **Device License / Service License**：按设备数授权 / 按服务授权（VM、Guest、On-Boarding、HA）<<<PAGE 329-330>>>
- **Starter Pack / Evaluation / Production**：免费 30 设备入门包 / 60 天全功能评估 / 正式许可 <<<PAGE 332-333>>>
- **Activate Add-On**：加购许可激活按钮，不点则旧许可到期自动生效 <<<PAGE 330>>>

## 第 18 章 Locator
- **Locate / Browse**：按终端找端口 / 按端口列终端（Browse 仅历史库）<<<PAGE 336, 338>>>
- **Historical / Live Search**：查历史库 / 实时查交换机；Live=最近 5 分钟活跃 <<<PAGE 336, 339>>>
- **ARP / Netforward Results Table**：IP-MAC 历史结果表 / 桥转发表定位结果表 <<<PAGE 338>>>
- **1st Match Only / All Matches**：Live 搜索首个匹配/全部匹配 <<<PAGE 337>>>
- **Netforward 视图 (Location/Classification/Data Center/Template)**：四种结果视图，自定义模板 ≤2/用户 <<<PAGE 340-341>>>

## 第 19 章 Multimedia Services (mDNS)
- **mDNS / Bonjour / SSDP**：零配置服务发现协议（Apple/非 Apple）；OV 支持 Gateway/Responder/Legacy 三模式 <<<PAGE 350>>>
- **Gateway Device**：mDNS 网关交换机，向指定 VLAN 泛洪 <<<PAGE 352>>>
- **Responder / Edge Device**：核心侧响应交换机 / 终端侧边缘设备（交换机或 AP Group）<<<PAGE 354, 356>>>
- **Service Rule / Server Policy / Client Policy**：服务共享规则及其两端策略（各至少一个匹配条件）<<<PAGE 356, 360, 362>>>
- **Service Cache**：Responder 学到的服务缓存，每小时轮询 <<<PAGE 363>>>
- **Legacy mDNS (L2 GRE Tunnel)**：交换机与 WLAN 控制器间 GRE 隧道中继，仅限 L2 <<<PAGE 352, 363>>>
- **Loopback0 IP**：Responder/Edge 设备的环回地址，缺失则 operational down <<<PAGE 355, 358>>>

## 第 20 章 Notifications
- **Trap / Severity 五级**：Normal/Warning/Minor/Major/Critical（整数 1-5）<<<PAGE 368, 374>>>
- **Acknowledge / Clear**：确认隐藏（可 UNACK 找回）/永久删除 trap <<<PAGE 369>>>
- **Trap Definition**：MIB 定义的 trap 清单，可改 severity 与 synopsis <<<PAGE 370>>>
- **Trap Responder**：按 Agent+Trap Type 触发邮件/服务器脚本/转发/自动确认 <<<PAGE 371>>>
- **Trap Variables ($Details$/$TrapName$ 等)**：响应模板变量集 <<<PAGE 373-376>>>
- **Trap Replay Polling**：启动及周期性补拉丢失 trap（按 upTime 回算时间戳）<<<PAGE 368, 379>>>
- **Trap Absorption**：相似 trap 吸并为 trapAbsorbtionTrap（默认关，周期 15s 可续期）<<<PAGE 379>>>
- **Trap Subscription State (On/Off/Delete)**：trap 订阅三态，Delete 清除旧 OV 地址 <<<PAGE 378>>>

## 第 21 章 OV System Health
- **VA (Virtual Appliance) Health**：OV 虚拟机 CPU/内存/网络/分区健康监控 <<<PAGE 381>>>
- **OV Misconfiguration**：VM 配置检查（CPU/RAM/HDD/Reservation）<<<PAGE 382>>>
- **Waiting Time For Next Same Trap**：同类健康 trap 的抑制间隔（默认 60 分钟）<<<PAGE 383>>>

## 第 22 章 PolicyView
- **PolicyView / QoS Policy**：条件+动作的 QoS 策略，存内置 LDAP <<<PAGE 384>>>
- **Unified Policy**：有线+无线通用的策略（独立于 Expert 表；不能直接下 IAP）<<<PAGE 387-388>>>
- **One Touch Policy (Data/ACL/Voice)**：简化策略模式，自动应用于全部 QoS 设备 <<<PAGE 385, 387>>>
- **Expert Mode**：手工逐参数定义条件/动作的策略模式（仅 AOS 设备）<<<PAGE 386>>>
- **Precedence**：策略优先级；PolicyView 域 30001-65535，冲突时高者优先 <<<PAGE 387>>>
- **Provisioned QoS**：默认尽力而为，动作可指定队列/带宽/优先级 <<<PAGE 385>>>
- **Condition / Action**：流量的匹配条件（L2/L3/L4/L7/ICMP）与处理动作 <<<PAGE 388-389>>>

- **Validity Period (AllTheTime/Weekdays/Weekends/WorkingDay/Custom)**：策略生效时间窗，WorkingDay=周一至五 9-17 点 <<<PAGE 395-396>>>
- **TCM (Tri-Color Marking)**：三色标记限速（CIR/PIR，绿/黄/红），无线不支持 <<<PAGE 394-395>>>
- **QoS 等级映射**：Platinum=7 / Gold=5 / Silver=3 / Bronze=1 <<<PAGE 394>>>
- **Reflexive**：允许回程连接的策略属性（仅 AOS Wireless，只支持 No Reflexive）<<<PAGE 388>>>
- **OV-L3-AcceptAllPolicy / DenyAllPolicy / Device-Default**：Policy List 未匹配流量的默认动作三选项 <<<PAGE 399>>>
- **Resource / Resource Group**：目的 IP/服务组资源对象，快速生成策略（默认 precedence 50000）<<<PAGE 401>>>
- **Notify All / Notify Selected / Re-cache**：通知设备刷新策略表的操作（代价高，建议批量）<<<PAGE 396>>>

- **OneTouchDR / OneTouchAR**：One Touch Data/ACL 策略在 LDAP 中的命名前缀（$S=源/$D=目的）<<<PAGE 404-405>>>
- **Default Policy List**：交换机恒存的默认策略表，新建规则自动入列且不因加入其他列表而移出 <<<PAGE 410>>>
- **Policies by Switch**：按设备查看其已缓存策略及 re-cache 状态 <<<PAGE 412>>>

## 第 23 章 Preferences
- **User Settings / System Settings**：个人偏好（Locale/Theme/超时/温度单位/Device Naming/颜色/声音）/系统级设置（需 Account Admin）<<<PAGE 416-417>>>
- **Inactivity Timeout**：无操作登出计时（15 分钟~25 周，默认 15）<<<PAGE 419>>>
- **Device Naming Pattern**：全局设备显示名规则（IP/名称/DNS）<<<PAGE 419>>>
- **Fleet Supervision / OV ID / Call Home Backend**：设备生命周期云服务 / OV 实例标识 / 后端 us.fluentnetworking.com，每 2 周上传 <<<PAGE 421-422>>>
- **Branding / Proxy**：自定义 Logo / 四外部站点代理（443）<<<PAGE 421>>>
- **SMS Provider (Plivo/Telefonica/Vodafone/Aliyun)**：短信网关四供应商 <<<PAGE 426>>>
- **Zulu CEK**：Zulu 密码扩展包，SNMP SHA256+AES192/256 必装 <<<PAGE 417>>>

## 第 24 章 Provisioning
- **Provisioning Rule**：按序列号/MAC/型号匹配的部署规则（含 Management+Config 模板）<<<PAGE 430>>>
- **Cloud Agent / Call-Home**：交换机侧云代理，每 5 分钟联系 OV 直至匹配规则 <<<PAGE 434, 436>>>
- **as-lite.myovcloud.net**：本地 Activation Server FQDN，DNS 须解析到 OV IP <<<PAGE 432>>>
- **DHCP Option 43 Sub-Option 128/134**：激活服务器 FQDN 与端口（默认 443）<<<PAGE 432>>>
- **Default Mgmt Users Template**：默认管理凭据模板（新机建 ov-enterprise 用户/在用机复用凭据）<<<PAGE 433-435>>>
- **Golden Configuration**：基于备份标记的基准配置，可审计与回推 <<<PAGE 431>>>
- **Force Provision**：下次 Call-Home 匹配规则时强制重推配置 <<<PAGE 431, 434>>>
- **Thin Switch Client**：AOS 8.8R1+ 瘦模式，CLI 禁配、write memory 失效 <<<PAGE 436>>>
- **Incremental Template**：瘦交换机 Periodic Call-Home 时一次性下发的增量模板 <<<PAGE 437>>>

## 第 25 章 Quarantine Manager
- **Quarantine Manager (QM)**：基于 IPS/Syslog/trap 的终端隔离系统 <<<PAGE 457>>>
- **Candidates / Banned / Never Banned / Disabled Ports**：四个处置列表（候选观察/已隔离/永不隔离/端口禁用）<<<PAGE 458>>>
- **Trigger / Extraction Expression**：规则触发正则 / 源地址抽取正则 <<<PAGE 468>>>
- **Quarantined VLAN / MAC Group**：预置隔离 VLAN 与同名 MAC 组（基础设施三件套之一）<<<PAGE 473-474>>>
- **QMR (Quarantine Manager Remediation)**：交换机侧补救应用，隔离客户端仅可访 Remediation Server <<<PAGE 459, 473>>>
- **Client Blocklist**：Stellar AP 无线违规客户端的替代封禁路径（365 天）<<<PAGE 460>>>
- **Fast Re-Cache**：只刷新隔离 MAC 组不 flush 其他策略的机制（部分机型）<<<PAGE 462>>>
- **TAD (Traffic Anomaly Detection)**：端口进出速率差异常检测（OS6850/6855/9700）<<<PAGE 478>>>
- **Incident Count**：候选设备异常累计次数 <<<PAGE 461>>>

## 第 26 章 Report
- **Report Configuration / Add to Report**：两步报表模型（先建配置，再到源应用绑定）<<<PAGE 484-485>>>
- **Purging Policy**：报表在服务器上的过期清理策略 <<<PAGE 485>>>

## 第 27 章 Resource Manager
- **Backup/Restore 三类型**：Full（含镜像版本记录）/Configuration Only/Images Only <<<PAGE 489-490>>>
- **Upgrade Image Repository / File Set / LSM**：镜像仓库 / 按设备类型的升级文件集 / 包描述文件 <<<PAGE 487, 496>>>
- **BMF (BootROM/MiniBoot/FPGA)**：底固件升级类别 <<<PAGE 499>>>
- **U-Boot (Denverton/Rangeley)**：OS9907/9912 双 CPU 型号对应两种 U-Boot 文件 <<<PAGE 497>>>
- **ISSU (In-Service Software Upgrade)**：冗余 CMM 不中断升级（OS10K/6900/6860，须冗余+certified+同步）<<<PAGE 499-500>>>
- **File Diff**：备份/本地文本文件逐行比较工具（不支持二进制）<<<PAGE 495>>>
- **Auto Configuration / Instruction File**：DHCP+TFTP(OV)+FTP/SFTP 三方自动开通机制 <<<PAGE 502-503>>>
- **Switch File Set (Banner/Captive Portal)**：自定义横幅与 CP 页面文件集 <<<PAGE 487>>>
- **Summary View**：备份/还原/升级操作结果汇总视图 <<<PAGE 495-496>>>

- **Instruction File (.alu) / Option 60/66/67**：自动开通指令文件及 DHCP 选项（机型/TFTP 地址/文件路径）<<<PAGE 503, 505>>>
- **Script File (Auto Config)**：开通后执行的 CLI 脚本；缺省自动 reload working <<<PAGE 504, 506>>>
- **Banner / Captive Portal 文件名规范**：banner.txt、cpLoginWelcome.inc 等固定名 <<<PAGE 508>>>
- **Backup Retention (Minimum Backups / Maximum Days)**：备份保留 max(b,n) 算法 <<<PAGE 510>>>

## 第 28 章 SAA
- **SAA (Service Assurance Agent)**：交换机/VM 对间 RTT、抖动、丢包探针（AOS 8.x+）<<<PAGE 512>>>
- **Ethernet OAM / Profile Association**：交换机对 SAA 配置 / VM 对 SAA 配置 <<<PAGE 513>>>
- **MACSAA**：唯一支持的测试类型（MAC 地址 ping）<<<PAGE 514>>>
- **RTT/Jitter/Packet Loss Threshold**：三类指标阈值，超标发 alaSaa* trap <<<PAGE 514>>>
- **ISID Check**：用 ISID 标识 PBB 网络中的 SPB 服务 <<<PAGE 515>>>

- **SAAExpertProfile / SAAVMProfile**：交换机对/VM 对 SAA 档案自动命名前缀 <<<PAGE 519>>>
- **Days to Retain (SAA)**：SAA 运行与数据保留期（默认 30 天，到期自动停）<<<PAGE 521>>>

## 第 29 章 Services (SPB)
- **SPBM / PBB / ISIS-SPB**：最短路径桥接 MAC / 骨干桥封装 / 链路状态控制协议 <<<PAGE 524>>>
- **BEB / BCB**：骨干边缘桥(有 SAP) / 骨干核心桥(无 SAP) <<<PAGE 525>>>
- **Service ID / ISID / BVLAN / Tunnel ID**：服务标识 / 骨干服务实例(绑 BVLAN+Service ID) / 承载 VLAN / 隧道标识 <<<PAGE 524, 527>>>
- **Multicast Mode (Headend/Tandem)**：组播复制模式，同 BVLAN 全网必须统一 <<<PAGE 525>>>
- **SAP (Service Access Point) / SDP**：服务接入点（客户流量入口）/ 服务分发点 <<<PAGE 525, 527>>>
- **L2 Profile (Services)**：定义 SAP 上控制包处理方式的档案 <<<PAGE 523>>>

## 第 30 章 SIP
- **SIP Snooping**：识别 SIP/RTP/RTCP 并 DSCP 标记+QoS 处理；路径须对称（不支持 MC-LAG/ECMP/VRRP）<<<PAGE 531>>>
- **RTP / RTCP / MOS / R-Factor / RTD**：媒体流协议与四项话音质量指标 <<<PAGE 531, 533>>>
- **One Touch Profile (SIP)**：单命令下发默认 SIP 配置（Voice dscp46/Video 34/Other 24）<<<PAGE 538-539>>>
- **SIP Profile（六子档案）**：Global Params/Trusted Servers/Threshold/SOS/TCP Port/UDP Port 组合 <<<PAGE 541>>>
- **In Sync / Out of Sync / Unassigned**：SIP Profile 三态（子档案改动即 Out of Sync）<<<PAGE 543>>>
- **SOS Call Number**：紧急呼叫检测串（精确 URI，≤4 条）<<<PAGE 548>>>
- **Port Mode (Automatic/Force Edge/Force Non-Edge)**：按 LLDP 推导或强制的端口边缘模式 <<<PAGE 542>>>

## 第 31 章 Topology
- **Geo Map / Topology Map**：地理图（默认视图）/传统拓扑图 <<<PAGE 554, 556>>>
- **Physical Network Map / Child Map**：自动生成的全网图 / 自建子图（状态上卷显示）<<<PAGE 554, 558>>>
- **Map Cluster**：缩放时按邻近聚簇的设备组（数量阈值可配）<<<PAGE 560-561>>>
- **External Link**：跨图链路箭头图标（Mesh AP 桥接不支持）<<<PAGE 559-560>>>
- **Poll Links**：手动触发链路发现（ping sweep 后加速显示）<<<PAGE 558>>>
- **Map Level Actions / Go To Table View**：图级操作菜单/切表格视图 <<<PAGE 555>>>

- **SPB Network / ERP Network Mode**：Map Level Actions 进入的 SPB/ERP 专题叠加视图 <<<PAGE 565, 573>>>
- **SPT (Shortest Path Tree)**：ISIS-SPB 最短路径树；选两 BEB+BVLAN 高亮 <<<PAGE 572>>>
- **RPL (Ring Protection Link) / APS**：ERP 环保护链路 / 自动保护交换协议 <<<PAGE 573>>>
- **Geo Map Site / Sub-Site**：地理位置站点及其子图（设备仅属一站）<<<PAGE 575-576>>>
- **Highlight Panel**：按状态/类型/配置/告警过滤高亮设备的面板 <<<PAGE 564>>>

## 第 32 章 Unified Access
- **Unified Access（四应用）**：Unified Profile/Unified Policy/Multimedia Services/Paid Services(BYOD) <<<PAGE 590>>>
- **UNP (User Network Profile) / Access Role Profile**：接入角色档案（QoS Policy List+CP 等属性）<<<PAGE 590, 593>>>
- **Access Auth Profile**：UNP 边缘端口认证配置模板（802.1X/MAC/分类/AAA/默认角色）<<<PAGE 593-594>>>
- **L2/L3 Authentication & Classification**：L2 定初始 UNP+VLAN（不再变）/L3 动态改策略 <<<PAGE 591>>>
- **Access Classification Rules（六类条件）**：Port/Group ID/MAC/LLDP/认证类型/IP 地址 <<<PAGE 592>>>
- **Port Bounce / COA**：COA 换 VLAN 后端口重启触发 DHCP 重新 <<<PAGE 595>>>
- **AP Mode / Secure**：端口自动识别管理 Stellar AP / 认证通过才信任客户端流量 <<<PAGE 595>>>
- **Trust Tag / Bypass VLAN**：信任 VLAN 标签分类 / 芯片直通 VLAN（优先于 Trust Tag，免认证）<<<PAGE 595-596>>>
- **Bypass Status / MAC Allow EAP (Pass/Fail/No Auth/None)**：802.1X 跳过与 EAP 允许组合逻辑 <<<PAGE 596-597>>>
- **Forward Mode (Tunnel/Bridge/Split/Decrypt Tunnel)**：无线转发四模式（GRE 隧道/本地桥/分流/解密隧道）<<<PAGE 598>>>
- **Band Steering (Force/Prefer/Band Balancing)**：5G 引导三模式 <<<PAGE 599>>>
- **User Derivation Rules**：客户端关联时按属性（如 MAC OUI）先于认证分配角色 <<<PAGE 598>>>
- **Client Isolation / Allowed Contacts List**：SSID 内客户端互相隔离+白名单 MAC <<<PAGE 597, 602>>>
- **WLAN Service Profile**：SSID 服务模板（Basic/Security/MLO/Advanced/QoS）<<<PAGE 601-602>>>
- **MLO (MultiLink Operation)**：Wi-Fi 7 多链路操作，依赖 radio+EHT <<<PAGE 603>>>
- **802.11r / OKC / L3 Roaming**：快速 BSS 切换/PMK 缓存漫游/跨子网漫游 <<<PAGE 603>>>
- **Customer Domain**：按数字 ID 的附加流量隔离域 <<<PAGE 593-594>>>
- **Far End IP List / Static Service / VXLAN Profile / Tunnel Profile**：映射到 Access Role Profile 的服务端点/静态服务/VXLAN/L2 GRE 隧道配置 <<<PAGE 594>>>

<!-- APPEND -->
