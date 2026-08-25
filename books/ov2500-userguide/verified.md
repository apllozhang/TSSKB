# Verified 候选（V1 原文真实性核对 + V2/V3 抽查）

## cases

## C1. 首次纳管设备五步法 <<<PAGE 40-44>>>
摘录："open the Discovery application...Click on the Discover New Devices button and enter a range of devices to discover. You can use the Default Discovery Profile"。
步骤：1) Discovery→Discover New Devices 输入 IP 范围（可用 Default Discovery Profile）；2) 在 Managed Devices 里 Edit 修正主 IP/write community/CLI-FTP 凭据/SNMP 版本；3) Notifications 配 trap（Topology 需 coldStart/warmStart/linkUp/linkDown）；4) 保存变更（Copy Working/Running to Certified，在 Topology 中选设备执行）；5) 需 QoS 时跑 PolicyView 后再次保存。
## C2. 向 Dashboard 添加/删除/布局 widget <<<PAGE 34-36, 52-53>>>
"click on the Settings icon and select Add Widget...Select an available widget from the list and click OK. The widget will be added to the upper-left of the dashboard"（一次只能加一个）；删除点 widget 右上角 x；布局 Settings→Change Layout，默认 Auto。
## C3. 创建自定义表格过滤器 <<<PAGE 38>>>
"Click the filter button...click Add...Enter a Filter Name...specify the strictness of the conditions (ANY/ALL)...have/not have...contains/begins with/ends with/equal/not equal...non-case sensitive/case sensitive"，可 Add new Condition / 新条件组。
## C4. 生成 Top N Applications 报表 <<<PAGE 74-82>>>
前置：Profiles 建 Analytics Profile（选交换机/端口）。操作：Analytics→Reports→Top N Applications；默认 Summary 饼图（过去 24 小时）；Filter by Profile/Select Devices 过滤；点饼图扇区→Clients/Switches 下钻看客户端或交换机分布；Configuration 配 Top 数(1-20)/Interval Type(Up Until Now|Custom)/Time Interval(24h|7d|4w)；Actions→Add to Report 转为定时 PDF 报表。
## C5. App Advanced 表格视图过滤 <<<PAGE 85-86, 89-90>>>
"Click on the Filter Bar...Time Slice (Device View Only)...Application...App Group...Source IP (Source View Only)...Device...UNP...Time Range: Most Recent - last 7 days / Custom"。
## C6. 建康阈值设置（Network Health） <<<PAGE 99-100>>>
Analytics→Network Health→选类别(CPU/Memory/Temperature)→Devices/AP Groups ADD 选设备→Configure Health Thresholds→逐设备 Edit 阈值→Save；一次最多 20 台。可点 Configure Traps 直通 Notifications Trap 向导（健康阈值 trap 已预选，按设备出现 Configure AOS 6.x / 7.x-8.x Traps 选项）→Next→Summary→Finish。
## C7. 创建 Collection Profile（统计采集） <<<PAGE 120-121>>>
Analytics→Statistics→Collection→Add：Name/Description、Poll Devices Periodically (On/Off，默认 On)、Poll Interval (1-60 默认 5 分钟)、Data Retention (1-180 天默认 30)、Add 选设备（Switch Picker/Topology Map）、选 Attributes（默认全选）→Create。
排程：先 Stop→选 Schedule→设 Start/End/Interval/Repeat(0-999)→重启 Profile。
## C8. 创建 Chart View Profile（统计查看） <<<PAGE 122-124>>>
Chart Views→Add：Profile Name、Choose Attributes（可整类选）、Selected Devices、Counters（>50 个时须手动挑 ≤50 加入选定）、Line Options（颜色/线宽）、Scale(0.001-1000)→Create；点 Profile 名查看，默认显示最近 1 小时，可 Switch to Table / Save to PNG。
## C9. 创建 Analytics Profile（Top N 报表前置） <<<PAGE 130-131>>>
Profiles→Add→Configuration 屏（Profile Name；Profile Type: Top N Apps & Clients / Top N Ports Utilization / Top N PoE Ports Utilization；Sampling Rate；PoE Usage Threshold 1-99 默认 99 仅 AOS 8.x）→Device/Port Selection 屏（可用 Default Ports Template 批量套端口如 1/1-1/10，可按机型建多模板；Add/Remove Switches；Add/Remove Ports 逐台选）→Create。PoE Profile 无需选端口（自动含全部 PoE 口）。
## C10. 端口↔应用映射（Applications Management） <<<PAGE 132-133>>>
模式：Range-Based（范围内端口被监控，未映射端口显示 Unknown）或 Enumuated（仅映射端口被监控）。Add→Application Name + Ports（范围用 "-" 如 20-21）。可 Import/Export .json 映射文件（导入会覆盖现有映射）；映射端口不可改，只能删除重建。
## C11. 信任一台未管理 AP <<<PAGE 143>>>
Network→AP Registration→Access Points→Unmanaged List 勾选 AP→点 "Change to Trust Status"（圆圈勾图标）→OK；反向用 "Change to Untrusted Status"。默认信任策略由锁图标 Trust All/Untrust All 切换。首次打开出现 Init Registration App 窗口预设国家码/信任状态。
## C12. 国家码冲突修复（两场景） <<<PAGE 143-144>>>
装 OV 时选错国家码：WLAN→RF→RF Profile→选 Default RF Profile→改 Country Code 与 OV 安装国家一致。跨国管理（美+加）：建两个 AP Group 各配对应国家 RF Profile，分别指派两国 AP。
## C13. 手工预添加 AP（单台/批量） <<<PAGE 144-145>>>
单台：Unmanaged List→Add：AP MAC、AP Name、AP Location（可勾 Get location for LLDP，1-255 字符仅 "," "/" 特殊字符）、Group Name（可下拉内 Add 新建组）、RF Profile→保存；接入后自动识别入 Managed List。批量：Upload .csv/.xls→Upload File→Import（可先下载 Template zip 样例）；导入 AP 默认 trusted。
## C14. 创建 AP Group 全字段 <<<PAGE 165-171>>>
AP Registration→AP Group→Add：General（Group Name ≤64 字符、Auto Group VLANs 按管理 VLAN 自动入组、RF Profile）、Extended SSID Scale、Time（Timezone/DST/NTP Server List）、802.1X Supplicant（Built-in/自定义证书）、Syslog（远程+TLS 证书+Log Level）、Post Mortem Dump（TFTP）、SSH（Support 密码+Root Password Seed，AWOS 4.0.0+）、AP Web、Client-Context（Roaming Domain 密码）、Client Behavior Tracking（SFTP/TFTP/Syslog 上传，Log Upload Period 1-24h 默认 1）、Certificate（Web Server/外部 Portal/Local LDAP/Local RadSec）、SNMP Setting（Agent+Trap）、IoT Radio（BLE/Zigbee）、IoT/Location/AA Server、Data VPN、WCF、Miscellaneous（Virtual IP、Called Station ID、IPv6 L3 Forwarding、IGMP Snooping）→Create。删除组时组内 AP 回 Default Group。
## C15. 配置 AP 为 Mesh 节点 <<<PAGE 150>>>
Access Points→选 AP→Edit→Edit Mesh Configuration：Enable=Yes、Is Root（根节点）、SSID、MLO（Wi-Fi 7 机型选 MLO Band ≥2 频段）、Band（2.4G/5G/6G）、Encryption Type（Both(WPA&WPA2)/WPA-2-Personal/Both(WPA2&WPA3)/WPA-3-Personal，按机型显示）、Mcast Rate（默认 24）、Passphrase→Apply。开机即用 Mesh：只需指定 root，其余 AP 用硬编码参数自动建网。
## C16. 添加 Remote AP（RAP） <<<PAGE 160-165>>>
前置：装 VPN VM + OmniVista Cirrus Freemium 账号（registration.ovcirrus.com 注册，邮件验证；AP 需 AWOS 4.0.0.xx+）。Cirrus→Network→Inventory→Device Catalog→Add→输序列号→Is this a Remote AP=Yes→VPN Settings（Server Public IP/Port/Server VPN IP、OV Enterprise Server IP、Client VPN IP Pool 范围/掩码）→Save VPN Settings and Create Device。AP 接入后经 Cirrus Activation Server 取配置入本地 OV 管理。
## C17. 单 AP 私有覆盖配置（Use Private Config） <<<PAGE 147-151>>>
Access Points→选 AP→Edit→分别可选 Edit IoT Radio Configuration（Zigbee/BLE 私有参数）、Edit Radio Configuration、Web Content Filtering（启用/禁用 WCF）、Location/Advanced Analytics Server（Cirrus WiFi RTLS / Advanced Analytics）——开启 Use Private Config 后设置即覆盖组配置。
## C18. 生成并上传 Web Server 证书（openssl 全流程） <<<PAGE 179>>>
1) openssl genrsa -des3 -out ap_server.key 2048；2) openssl req -new -key ap_server.key -out ap_server.csr -sha256（CN 必须填 mywifi.al-enterprise.com）；3) openssl x509 -req -in ap_server.csr -CA rootCA.pem -CAkey rootCA.key -CAcreateserial -out ap_server.crt -days 3560 -sha256；4) 合并 crt+key 为 .pem；OV Certificate→Add→Web Server/External Portal Server 上传。
## C19. 创建 IoT/Location/AA Server 服务档案 <<<PAGE 192-194>>>
AP Registration→IoT/Location/Advanced Analytics Server→Add：Name、Engine Type（Aeroscout/Stellar Asset Tracking/Cirrus WiFi RTLS/Cirrus Advanced Analytics/Assa Abloy）、Server IP/Host（Stellar 默认 FQDN kafka.omniaccess-stellar-asset-tracking.com；Cirrus AA 选区域）→按引擎配参数（上报间隔/Allowlist/RSSI Format/QoE 事件）→Create；再到 AP Group 的 IoT/Location Server 字段选用。
## C20. 创建 Data VPN Server <<<PAGE 196>>>
AP Registration→Data VPN Servers→Add：Name(1-64)/Description、Server's Public IP/Port(1-65535)/VPN IP、Client VPN IP Pool（IP Range 或 Shorthand Mask 如 192.168.1.0/24）、Server 公私钥→Create；Export VPN Settings 导出 .conf 供远端 VPN Server VM 使用。已被 AP Group 引用的 VPN Server 不能删除。
## C21. Application Visibility 配置三步法 <<<PAGE 202-203>>>
1) 下载/导入 ALE Signature File（可开自动更新）；2) 建 Signature Profile（向导选监控组+Enforcement 组；Enforcement 还需在 Unified Access 配 Access Role Profile）；3) 将 Signature Profile 应用到交换机/端口。之后用 Analytics 的 Top N Applications - Advanced 看数据。
## C22. 定制 Captive Portal 网页四步法 <<<PAGE 235-236>>>
Customization→Add→向导：1) Import the Archive（Select Switch 从交换机拉默认/自定义文件包，或 Browse 本地导入——本地导入跳过 2/3 步）；2) Download 解包到本地编辑 html/jpeg；3) Upload 编辑后的 archive；4) Apply/Push to Switches 选交换机下发（会覆盖交换机上现有 Custom Archive）。取消分配：把交换机移到左列再 Push。
## C23. 创建并发送 CLI 脚本 <<<PAGE 239-246>>>
CLI Scripting→Scripts→Add：Filename（自动加 .script）、勾 Shared Admin Script（前缀 shadmin）、命令区（CLI+JS 混编，每行一条；描述用 /* @@desc@@ */）→Add。发送：选脚本→Send Script→Script Info→Device Selection（Switch Picker 或 Topology 选设备）→Scheduler（Now / Periodically: Simple 或 Cron）→Define User Variables 填变量值→Send Script。日志在 Logs 屏按命令查看。
## C24. Watchdog 启停 OV 服务 <<<PAGE 249-250>>>
Administration→Control Panel→Watchdog：滑块启停单个服务（连带依赖）；Start All/Restart All 批量操作；停 ActiveMQ/Tomcat 等会导致 Web 关闭需手工恢复。
## C25. CLI 处理确认提示型命令（reload 示例） <<<PAGE 241, 244>>>
用 JS 训练提示：cli.sendCmd("more"); cli.expectPrompt("Confirm Activate (Y/N):"); ... cli.sendCmd("reload working no rollback-timeout in 10:10"); cli.sendCmd("y")；对会挂起的命令前加 <tapps> lastcmd </tapps>。
## C26. 执行设备发现（Range + Profile） <<<PAGE 256>>>
Discovery→Managed Devices→Discover New Devices→Ranges List：用现有 Range 直接 Discover Now，或 Add 新建（Start IP/End IP/Subnet Mask/Description + 勾选 Discovery Profiles，多档案可拖拽排序）→Discover Now→完成后设备入 Managed Devices。更新单台设备信息用 Rediscover。
## C27. 手工添加/克隆/多选编辑设备 <<<PAGE 257-261>>>
Add：General（IP、Assign Site、Location、CLI/FTP 凭据、Secondary Password）+ SNMP + Advanced（Trap Station User Name、Discover Link、Shell Preference、Use Get Bulk/Max Repetitions、Allow Port Disabling）。克隆：Clone 后改 IP/密码。多选编辑：值不一致的字段留空/灰化，用 "Click to Overwrite" 统一赋值，"Retain Original Values" 反悔。
## C28. 设备操作集（Actions） <<<PAGE 262-264>>>
Ping / Poll For Traps / Poll Links / Configure Health Thresholds（附 Configure Traps 直通向导）/ Locate End Stations / Webpage / Device Inventory / Backup Device / SSH / SSH Custom（SecureCRT）/ Configure Traps / View Traps / Reboot（选 Working/Certified/Other 目录+延迟）/ Copy Working to Certified / Copy Certified to Working / Save to Running / Scheduled Upgrades。
## C29. 配置 SecureCRT 作为 SSH Custom 客户端 <<<PAGE 268-270>>>
装 SecureCRT→Options→Global Options→Web Browser→勾 "Use registry setting for web browser"→OK；浏览器需支持 SSH2 且 SecureCRT 设为默认 SSH2 应用。
## C30. 启用 Network Advisor 监控 <<<PAGE 264-267>>>
前置：在 Global Dashboard 的 Network Advisor widget 声明实例（Name/URL/Application UUID——UUID 在 NA 实例 Home Dashboard）。启用：Managed Devices 选设备→Features→Enable OmniVista Network Advisor→选实例→OK。移除实例前须先解除设备分配。单个 NA 实例只能同步一个 OV 安装。
## C31. 导入第三方设备 MIB <<<PAGE 288>>>
先在 Third-Party Devices Support 建 OID 条目（OID 只填 enterprises 后段；MIB Directory Name 可为不存在的目录，导入时自动创建）→Import MIBs→选 Mibset→Import→Upload Files（Chrome 支持 Upload Folder）→用 Up/Down 箭头调整编译顺序→Apply。
## C32. 配置 OV 支持 Zigbee 三步 <<<PAGE 317>>>
1) AP Registration→IoT/Location Server 添加 Assa Abloy Zigbee Server（OV 须能连到客户现场服务器）；2) AP Group 设 IoT Radio Mode=Zigbee + IoT/Location Server Profile 选该服务器，加入要用作 Zigbee 网关的 AP（推荐组级配置，也可单 AP 私有配置）；3) 设备发现后（默认 Auto Rejected）在 IoT→Zigbee Devices 选中→Accept 启用。
## C33. IoT 自动/手动 Enforcement <<<PAGE 320-321>>>
自动：Enforcement 屏顶部 Automatic Enforcement=On→逐类别在 Access Role Profile 列选档案（须已存在于交换机/AP Group）。手动：顶部 Off→选类别→Enable Enforcement。例外清单：Exception List 添加 SSID/端点 MAC/AP Group/交换机 IP；已被 Enforcement 的端点要先移除 Enforcement 再入例外（交换机会缓存 UNP）。
## C34. 导入许可 <<<PAGE 335>>>
License→Add or Import：导入 .dat 文件，或逐行输入 License Key（多个 key 各占一行）→Submit。加购许可用 Activate Add-On 按钮（不点则旧许可到期时自动激活）。
## C35. Locator 定位终端 <<<PAGE 337-339>>>
Locate 屏：Search by 选 IP/Host Name、MAC、Auth User →输条件→Historical/Live 切换（Live 可选 1st Match Only/All Matches）→Locate；结果看 ARP 表（IP-MAC 历史）+ Netforward 表（设备/槽位/端口+时间戳）；行内 Action 可 Locate On Map / Quarantine Manager / Port 启停 / ClearPass 认证查询 / Access Guardian 诊断。
## C36. 创建 Trap Responder（邮件/脚本/转发/确认） <<<PAGE 371-376>>>
Notifications→Trap Responder→Add：Agent（Device IP 范围或 AP Group——Stellar AP 必须选 AP Group）→Trap Type（滑块选 severity 或 Filter：Any/All selected filters；条件可含 Name/Synopsis/Agent/Date-Time/Severity/SNMP Variables）→Response（Send an E-Mail：地址分号分隔、主题默认含 $TrapSeverityCount$、正文默认 $Details$；Run an Application：Command/Arguments/Start Directory/Standard Input；Forward Traps：Destination IP+Port 162；Acknowledge Traps）→Summary→Create。
## C37. 配置设备 Trap 向导 <<<PAGE 376-378>>>
Notifications→Trap Configuration：Server Information（IP/Trap Port 只读）→Device Selection（Configure For: Device|AP Group；Device Type: All/AOS/AOS 7x-8x/6200；仅 Up 设备可选）→Configure Traps（Trap Subscription State On/Off/Delete + Save 粒度 + Protocol + 勾选 trap，按设备类型分页签）→Summary→Finish。
## C38. PolicyView 后保存配置四步 <<<PAGE 386>>>
1) Managed Devices 按 Changes 列排序；2) 选 Unsaved 设备→Actions→Save to Running（变 Uncertified）；3) 选 Uncertified 设备→Actions→Copy Working/Running to Certified（列变空，需几分钟）；4) 也可在 Topology 中执行同样操作。
## C39. 创建 Unified Policy 向导 <<<PAGE 388-396>>>
PolicyView→Users and Groups→Unified Policies→Add：Config for Policy（Name、Precedence 自动填最低未用值、Advanced: Default List/Enabled/Save/Log Matches/Send Trap/Reflexive）→Device Selection（Devices+AP Groups）→Set Condition（L2 MACs/L3 IPs/L3 DSCP-TOS/L4 Services/L7 Application Visibility/ICMP）→Set Action（QoS/TCM）→Validity Period→Review。
## C40. 创建 One Touch Data 策略 <<<PAGE 403>>>
PolicyView→One Touch→Data：选 Priority（Platinum/Gold/Silver/Bronze）→Add→输 Server IP→Create（状态 Unsaved）→Save 图标存 LDAP→Notify All 全网下发（触发全交换机 flush+reload，注意批量）。删除时选服务器→Delete→OK（自动清 LDAP 并 SNMP 通知设备 re-cache）。
## C41. 开启 Fleet Supervision <<<PAGE 423-424>>>
1) Preferences→System Settings→Fleet Supervision→滑块启用+接受协议→Apply（出现 Verify Proxy Configuration 链接）；2) myfleet.ovcirrus.com 注册账号（邮件确认）；3) Fleet Supervision 门户→Management System→Create：Name、Type=OmniVista 2500、OV ID（Test Connection 验证）、可选 Country/City/State→Create，Device Catalog 自动填充。手动上传：Preferences→Fleet Supervision→Upload Now。
## C42. 部署新交换机（Provisioning 全流程） <<<PAGE 433-434>>>
1) DHCP/DNS 预配置（Option 43 Sub1=alenterprise、Sub128=as-lite.myovcloud.net、Sub134=443）；2) Rules→Default Mgmt Users Template 配凭据（新机用 Create new credentials）；3) Add 建 Rule（序列号/MAC/型号+Management+Config 模板）；4) 控制台 reload from working no rollback-timeout；5) 8.6R1- 需 CLI 启用 Cloud Agent；6) 接入网络→自动匹配规则并配置→入 Managed Devices。
## C43. 部署 Thin Switch <<<PAGE 437-438>>>
1) 满足 DHCP/DNS/NTP（或 vcboot.cfg 写入最小配置+cloud-agent admin-state enable）；2) Rules→Add：Thin Switch=Yes、按序列号/MAC、Desired Switch Config 三选一；3) 重启或 cloud-agent enable 触发 Call-Home→OV 推配置并宣告瘦模式；4) OV 自动备份（vcboot.cfg+快照）；5) 后续 Periodic Call-Home 可推 Incremental Template。
## C44. Provisioning 故障排查 <<<PAGE 439>>>
Results 屏看 "Last Provisioning Message" 列；最常见原因是 OV 无正确 SSH/SFTP 凭据（Default/Custom Management Template 中修正）；模板问题改后等下次 Call-Home 自动重试；日志：Audit→Configuration→resource-manager-client-service；Activation Server 问题看 Audit→System→tomcat-*。
## C45. 配置 Quarantine Manager 基础设施 <<<PAGE 473-475>>>
1) Groups→MAC Groups 建 "Quarantined" 组；2) PolicyView→Unified Policies 建 L2 Source MAC Group(Quarantined)+Drop 策略并 Notify；3) Quarantine Manager→Configuration→编辑 Quarantined VLAN：VLAN/MAC 组名、可选 Remediation URL/IP、HTTP Proxy Port、Allow Port Disabling；Subnets 加 ≤3 个 Allowed 子网（含 Remediation Server IP）；4) Apply to Devices 选设备下发。可选：Topology 建 "Quarantine" 逻辑网+子网限制作用范围。
## C46. 创建自定义 Quarantine 规则 <<<PAGE 470-471>>>
Rules→Add：Name/Description、Trigger Expression（如 log_id=0421073001）、Extraction Expression（如 src=([0-9.]*)）、Action（Candidate List/Quarantine/Release——Release 可供工单系统自动解封）、Event Type（Syslog/Trap）、Enabled→Create。ALE 下发的规则 .xml 文件用 Import 导入（默认 Disabled）。
## C47. 处理隔离事件（Candidates/Banned/Disabled Ports） <<<PAGE 461-465>>>
Candidates：选设备→Release/Ban（无线客户端实入 Client Blocklist）/Never Ban。Banned：Add 手工封禁（IP/MAC+Reason）、Release 解封、Retry 重试失败操作、Redo Ban 重扫。Disabled Ports：逐条 Release（端口须全部条目释放才启用）、Retry。Fortinet 事件右键可跳 Fortinet 官网分析页。
## C48. 创建定时报表 <<<PAGE 484-485>>>
Report→Add：Report Title、Purging Policy、Schedule（Now / Periodically Simple|Cron）、E-Mail（单一收件人，前置 Preferences Email 配置）、Other Settings（页面大小/方向）→Create（产生空白报表）；再到 Discovery/Locator/Analytics 目标屏→Add to Report→选该 Report Configuration→OK。
## C49. 执行备份 <<<PAGE 488-491>>>
Resource Manager→Backup/Restore→Backup：Backup Method（By Devices / By Maps / By AP Groups）→Device Selection→Configuration（类型+目录/Security Files/Diagnostic Dump+Description+Schedule Setting Daily/Weekly/Monthly/Every Weekday）→Review→Backup。未定义 FTP 凭据的设备会逐台弹窗询问。
## C50. 升级设备镜像 <<<PAGE 496-499>>>
Upgrade Image→Import（ALE zip 自动解包）→选 File Set→Install→Firmware File Selection（AP 组全选不可取消，按型号自动匹配）→Devices Selection（Devices 或 AP Groups）→Software Installation（Upgrade BMF/Images/U-Boot all NIs/ISSU/Directory/6200 选项）→Install Software→完成后 Go to Topology to Reboot Device 重启生效，再 Copy Working to Certified。
## C51. 配置自动开通（Auto Configuration）四步 <<<PAGE 505-506>>>
1) DHCP 配 Option 66（OV TFTP 地址）与 Option 67（如 os6855/instruction1.alu）；2) 编写 Script File（如 reload working no rollback-timeout / copy working certified flash-synchro）；3) 固件/配置/调试/脚本文件放 FTP/SFTP 服务器；4) Resource Manager→Auto Configuration→Add 建 Instruction File（路径+名称 .alu+主/备服务器+Firmware Version 格式如 OS_6_4_6_101_R01+各文件位置）。已部署交换机升级：删 boot.cfg 重启即触发版本比对。
## C52. 创建交换机间 SAA <<<PAGE 513-515>>>
前置：Notifications 启用 SAA traps、SAA Settings 配默认指标。SAA→Ethernet OAM→Add：Ethernet Config（Name ≤32 字、Source/Destination IP、RTT/Jitter/Packet Loss 阈值、Interval、Admin Status）→MAC Config（VLAN、Inter Packet Delay、Number of Packets、Payload Size、可选 ISID Check）→Review→Create；统计在 Ethernet List 查看图形/表格。
## C53. 创建并下发 Access Role Profile <<<PAGE 608-613>>>
Unified Profile→Access Role Profile→Add：General（Auth Flag/Mobile Tag/Redirect Status/Policy List/Location+Period Policy/Inactivity Interval）+Bandwidth Control（上下行带宽/Burst）+Client Session Logging+WCF+Walled Garden+Allowed Contacts+CP Attributes（None/Internal/External）→Create→Apply To Devices：Configure Mapping Method（Map to VLAN/SPB/VXLAN/Static Service/Tunnel/VLAN+Tunnel）→Select Devices（含 ClearPass 蓝色条目）→Period Policy→Location Policy→Review→Apply。

<!-- APPEND -->

## counter-examples

## X1. sFlow 包不能经 EMP 端口发送 <<<PAGE 75, 92>>>
"sFlow packets cannot be sent through the EMP Port. If you want to gather Top N App data from a switch you cannot use the EMP IP when discovering the switch."
## X2. 未定义 FTP 凭据时逐台被询问 <<<PAGE 43>>>
"If you do not define the FTP login names and passwords and you attempt to save, restore, or update configuration files...you will be individually queried for the FTP login name and password of each individual switch"
## X3. PolicyView QoS 执行后不保存则配置丢失 <<<PAGE 44>>>
"once PolicyView QoS has executed, all AOS devices will be left with their running configuration in the Unsaved state. It is important to save the running configuration to the working directory and then the certified directory"
## X4. 未知设备的 sFlow 数据不进报表 <<<PAGE 67>>>
"If the device is not known to OmniVista (or if the Analytics Application is not supported on the device), sFlow information is sent to OmniVista, but the information is not included in those reports."
## X5. "Others" 类别不是数据缺失 <<<PAGE 68>>>
"There may be many others in the profile that are not in the 'top' 10 or 20. The 'Others' category gives you an idea of all of the other applications...with low utilization rates"
## X6. 外部 RADIUS 登录用户无法生成定时报表 <<<PAGE 64>>>
见 principles P13——用外部 RADIUS 认证的管理员只能出实时报表。
## X7. 改交换机 IP 后 Top N App & Clients Profile 失效 <<<PAGE 131>>>
"If you change the IP address of a switch after assigning a 'Top N App & Clients Profile' to the switch, you must re-assign the profile to the switch."
## X8. Statistics 采集静默失败：SNMP 源 IP 与发现 IP 不一致 <<<PAGE 119>>>
见 principles P24——设备侧 SNMP service 源地址与 OV 发现地址不同时收不到数据，无显式报错提示。
## X9. 删除 Statistics/View Profile 连带删除全部历史统计 <<<PAGE 121, 129>>>
"deleting a profile also deletes all statistical data associated with the profile"
## X10. 健康阈值修改最长 1 小时后才可见 <<<PAGE 100>>>
"changes made to health thresholds will not appear until the next polling cycle (up to an hour)"
## X11. AP 802.1X 客户端模式下不支持 untagged WLAN 与 Mesh <<<PAGE 140>>>
见 principles P32。
## X12. "Enable Statistics Automatically On" 选 All 大量加设备有性能风险 <<<PAGE 134>>>
"if you choose 'All' and you add a large number of network devices, there is a risk of performance impact"；新装默认 2000 台、升级默认 0 台——升级环境统计不会自动开启。
## X13. 默认客户端/服务器证书不安全 <<<PAGE 141>>>
"Do not rely on the Default Client Certificate on APs and the Default Server Certificate on UPAM. It is recommended that you install Custom...Certificates"
## X14. Default AP Group / Default BLEGW Group 不可删除，关键字段不可改 <<<PAGE 165, 172>>>
"Both the 'default group' and the 'default BLEGW group' can be edited; however, they cannot be deleted"；且 "You cannot edit the Group Name, Group Description, or Auto Group VLANs fields on the Default AP Group or Default BLEGW Group"。
## X15. 开启 Extended SSID Scale 后低配机型无法入组 <<<PAGE 166>>>
"When enabled (On), only AP models that support up to 14 SSIDs can join the AP Group"；6GHz 每组固定 4 SSID。
## X16. 无扫描射频的 AP 开专用扫描会断所有客户端 <<<PAGE 146>>>
"AP models without scanning radio—regular WLAN services are stopped on the AP and all clients are disconnected"；AP1451 的 6GHz 客户端也会断（可漫游至 2.4/5G）。
## X17. Zigbee 门锁 OUI 不能加进 Auto-Accept 列表 <<<PAGE 148>>>
"Do not enter the MAC OUI for supported door locks. These devices must be 'Manually Accepted' and enabled in the Zigbee Devices Table"
## X18. SNMP trap 目的地址填 OV 自身造成重复告警 <<<PAGE 169>>>
见 principles P43。
## X19. Migrate to Other OV 后 AP 在对端显示为 Unmanaged <<<PAGE 149>>>
"The AP will be released from your OmniVista Server and migrate to the other server, where it will be displayed in the Unmanaged AP Tab"——需对端管理员重新授权配置。
## X20. Root Password Seed 仅 AWOS 4.0.0+ 生效 <<<PAGE 167>>>
"A Root Account Password Seed will not be configured for any APs in the group running a lower AWOS"
## X21. 含不支持 AV 的 AP 的 AP Group 应用签名档案：操作"成功"但部分 AP 未生效 <<<PAGE 209>>>
"If a Signature Profile is applied to an AP Group that contains APs that do not support Application Visibility (AP1201, AP1201H, AP1101), the profile will not be applied to those APs. If none of the APs in the group support Application Visibility, the profile apply operation will still succeed."
## X22. 应用 Signature Profile 会清掉设备上 CLI 配置的 AV 配置 <<<PAGE 209>>>
"any pre-existing Application Visibility configuration on a device is erased and the new profile configuration is used, including any Application Visibility configuration done from the CLI"
## X23. 签名档案向导里配了 Access Role Profile 不会自动下发设备 <<<PAGE 208>>>
"this workflow will not assign the selected Access Role Profile to the devices. You must first assign the Access Role Profile to the devices from Unified Profile Application"
## X24. 删除认证服务器不影响交换机继续使用 <<<PAGE 221-222, 226>>>
"deleting an authentication server...will not cause switches that currently use that [LDAP/RADIUS] Server to cease using it"——会产生"幽灵服务器"状态。
## X25. UPAM RADIUS Shared Secret 改动须同步 NAS Client <<<PAGE 224>>>
"If you change the Shared Secret of the UPAM Radius Server, you also must update Shared Secret of NAS Client on the NAS Clients Screen (UPAM - Authentication - NAS Clients)"
## X26. 组内应用在组里的应用已被应用则 VPN Server / Signature File / Signature Profile 均不可删 <<<PAGE 196, 206, 209>>>
"you cannot delete a Signature File that has been assigned to switches"；"you cannot delete a Signature Profile that has been applied to devices"；Data VPN Server 同理。
## X27. Scheduled Upgrade 会降级高于目标版本的设备 <<<PAGE 296>>>
"The device will be downgraded. A message will inform the user that the device will be downgraded."
## X28. Unsaved 设备被升级计划静默跳过 <<<PAGE 296>>>
"If a device is 'unsaved' the device will not be upgraded. It will be skipped."
## X29. Stellar AP 手工加进 Managed Devices 吞掉第三方 License <<<PAGE 257-258>>>
见 principles P73。
## X30. REST API 轮询凭据错误引发 trap 风暴 <<<PAGE 300>>>
"Incorrect credentials may result in switches periodically generating many authentication failure traps."
## X31. 混选不同软件类型设备时 Set Same Version 只剩 Do Not Upgrade <<<PAGE 293-294>>>
"If you select devices that use different software (e.g., OAW-AP1221 and OS6450), 'Do Not Upgrade' will be your only option."
## X32. IoT 固定端口默认不上报指纹 <<<PAGE 309>>>
"When IoT is enabled on a switch, it is enabled globally on all UNP Ports. However, it is not enabled on fixed ports"——须逐口 CLI 开启。
## X33. AOS 设备上的 Stellar AP 自身出现在 IoT Inventory <<<PAGE 313>>>
"To prevent a Stellar AP from being displayed in the Inventory List, you must disable IoT profiling on the switch port connected to the AP using...device-profile port slot/port admin-state disable"
## X34. Provisioning 模板含禁用命令必失败 <<<PAGE 442>>>
"Certain commands that are handled by the Configuration Manager in AOS cannot be included in a Configuration Template (e.g., user admin password, write memory, configuration apply). If these commands are included...provisioning will fail."
## X35. OV 收不到配置确认回执时谎报成功 <<<PAGE 455>>>
见 principles P131——连接丢失/SSH 超时场景下 Results 显示 Succeeded 但配置可能未应用。
## X36. Certified 目录运行的交换机不能 Enforce Golden Config <<<PAGE 452>>>
"You cannot enforce the Golden Configuration on a switch running from the Certified Directory."
## X37. 从 Certified 目录 provision 的配置是临时的 <<<PAGE 434, 435>>>
"the configuration is temporary and will not be persisted. The switch will lose its configuration if it reboots"——须 reload working 后 Force Provision。
## X38. Quarantine 对无线客户端不进 Banned 而进 Client Blocklist <<<PAGE 460>>>
见 principles P132；旧版本（4.9R1 前）Banned 的无线客户端不会自动迁移。
## X39. 重复禁用同端口产生空 MAC 双条目，Release Banned 不会自动恢复端口 <<<PAGE 465>>>
"when you use the Banned Screen to release a MAC address, the port will not be re-enabled. The Network Administrator will have to manually re-enable the port by releasing the port from the Disabled Ports List"；端口要等所有引发封禁的条目都释放才启用。
## X40. QMR 与 QoS inner VLAN/802.1p 策略互斥 <<<PAGE 459>>>
"Configuring QMR and QoS inner VLAN or inner 802.1p policies is mutually exclusive...also true with QMR and VLAN Stacking services."
## X41. 备份文件拷贝到其他机器可能搞瘫网络 <<<PAGE 493>>>
"The saved files contain binary configuration information, including the IP address/MAC address of the source machine, and using these files on another machine could bring the network down."
## X42. Image 文件不真正备份，Restore 前须先导镜像 <<<PAGE 489, 490>>>
"Image files will not be FTPed from a device. OmniVista will only record file version(s). Therefore, before Restore is to proceed, the required image file set must be stored in the Upgrade Image Repository."
## X43. FTP 5 分钟超时导致大镜像升级失败 <<<PAGE 497>>>
"The switch FTP timeout default is 5 minutes...increase the FTP timeout in switches you are upgrading...session ftp timeout <time>"
## X44. Image 与 U-Boot 升级顺序不能颠倒 <<<PAGE 497>>>
"you must complete the image file upgrade before upgrading the U-Boot and Miniboot files."
## X45. Periodic 报表不能手动生成；外部 RADIUS 用户不能排程 <<<PAGE 484-486>>>
"You cannot manually generate a report configured with a 'Periodic' schedule"；"only users authenticated through the Local OmniVista Authentication Server can schedule reports."
## X46. 首次建报表配置生成的是空白报表 <<<PAGE 485>>>
"a blank report is automatically generated...because you have not yet associated the report with an application"
## X47. 混合地图备份漏掉 Stellar AP <<<PAGE 488>>>
"if a map contains AOS Devices and Stellar APs, the Stellar APs will not be backed up. Stellar APs can only be backed up by AP Group."

<!-- APPEND -->

## frameworks

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

## glossary

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

## principles

## P1. 仪表盘刷新率最小/默认 5 分钟 <<<PAGE 37>>>
"Enter a refresh rate, in minutes. (Minimum refresh rate = 5, Default = 5)"
## P2. List View 不可打印，Table View 才可 <<<PAGE 37, 39>>>
"information displayed in List View cannot be Printed via the OmniVista 2500 NMS Print button. To print...switch to Table View (if available)"
## P3. 大表设备选择在会话内持久，登出复位 <<<PAGE 40>>>
"Your device selection will remain persistent until you change it or log out of OmniVista. If you log out, the default setting (no display) returns."（适用 VLANs 等大表，默认不显示数据，需用 Device Selection Bar 选设备）
## P4. 自动发现主 IP 选择规则 <<<PAGE 42>>>
"OmniVista uses the first IP address that responds to a ping as that device's primary IP address. However, if multiple VLANs exist in the device, additional IP addresses...will also respond to pings"（Ping Sweep/ARP 发现多 VLAN 设备时主 IP 可能选错，需手工在 Edit Discovery Manager Entry 中改）
## P5. 发现设备默认 write community = public <<<PAGE 42>>>
"All devices that are discovered are initially specified to have the default write community name, public"；且"Switches' SNMP write (set) community names are not configurable from OmniVista"——community 只能登录交换机本端配置。
## P6. CLI/FTP 凭据只用于 FTP，不用于 Telnet <<<PAGE 43>>>
"The user names and passwords entered in these fields are used for FTP ONLY. They are not used for Telnet."
## P7. AOS 设备支持 SNMP v1/v2/v3，版本需先连通才能改 <<<PAGE 43>>>
"AOS devices support SNMP version 1, SNMP version 2 or SNMP version 3...cannot be changed until OmniVista has connected to the switch"
## P8. 各应用必需 trap 清单 <<<PAGE 43-44>>>
Topology: "coldStart, warmStart, linkUp, linkDown"（linkUp/linkDown 须逐端口启用）；PolicyView QoS: "policyEventNotification"。
## P9. AOS 交换机 certified/working 双目录持久化机制 <<<PAGE 43-44>>>
"The certified directory contains files that have been certified...The working directory...You cannot save configuration changes directly to the certified directory"；running config 在 RAM，重启丢失，须保存到 working 再拷贝到 certified。差异时重启自动加载 certified。
## P10. PolicyView QoS 执行后所有 AOS 设备进入 Unsaved 状态 <<<PAGE 44>>>
"PolicyView QoS...writes the address of the LDAP server to each QoS-enabled switch...all AOS devices will be left with their running configuration in the Unsaved state"（执行后必须保存，否则丢失）
## P11. Stellar AP 未保存变更无害（重启自动取最新配置） <<<PAGE 31, 46>>>
"Unsaved changes on Stellar APs are generally not a problem since Stellar APs receive the latest configuration at reboot."（可在 Settings 关闭该通知）
## P12. Client Health 信号强度分级 <<<PAGE 59>>>
"Best - Signal strength is more than -65; Good - between -80 and -65; Fair - less than -80"
## P13. 外部 RADIUS 认证用户只能生成实时报表 <<<PAGE 64>>>
"users authenticated through an external RADUIS Server can only generate live reports, not scheduled reports. Users authenticated through the Local OmniVista Authentication Server can generate both"
## P14. Top N Apps/Clients 基于 sFlow + 端口识别；OV 自动成为 receiver <<<PAGE 67, 74>>>
"The Top N Applications are determined using sFlow...identifies the applications using the TCP/UDP port obtained from sFlow packets"；"When these profiles are created, the OmniVista Server is automatically configured as the sFlow Receiver"；外部 CLI 配 sFlow 指向 OV 也计入报表。
## P15. Top N 报表参数默认值 <<<PAGE 82, 91>>>
Top N Apps: Number of Top Applications "Range = 1 - 20, Default = 5"；Custom 区间最多 3 个月数据；Auto Refresh "Range = 15 - 60, Default = 15"。App Advanced: Data Interval 15-120 默认 15；Top (apps) 1-50 默认 5；Updating Interval 1-20 默认 5；Data Unit 默认 MB。
## P16. 流记录环形缓冲上限 20,000 条 <<<PAGE 85>>>
"OmniVista can store up 20,000 records, at which point the data is overwritten with new records."
## P17. App Flow Count 支持矩阵 <<<PAGE 82-83>>>
"OS6860/OS6860E Switches and Stellar APs provide flow information (number of flows) in the App Flow Count view and packet/byte information in the App Bandwidth Usage view. All device types sample data."；Top Users/Apps per User 报表需 "AOS devices and Stellar APs (AWOS 3.0.6x and higher)" <<<PAGE 83>>>。
## P18. OS 版本低于 AOS 8.5R4/AWOS 3.0.6.x 时 Time Period Type 字段隐藏 <<<PAGE 91>>>
"if any of the reporting device OS's are lower than AOS 8.5R4/AWOS 3.0.6.x, the 'Time Period Type' field will not be displayed"
## P19. 健康阈值一次最多配 20 台设备 <<<PAGE 99>>>
"You can only configure health thresholds for up to 20 devices at a time...If you select more than 20 devices, the Configure Health Thresholds button will not activate"——多于 20 台须分批（每批 20）配置。
## P20. Stellar AP 无温度信息；温度阈值仅 AOS 6.x 可配 <<<PAGE 100>>>
"Stellar APs do not support or display Temperature information...you can only configure the Temperature Threshold on AOS 6.x devices. The Temperature Threshold is hard-coded on AOS 8.x devices"；阈值变更最长 1 小时（下个轮询周期）后生效。
## P21. Top N Ports 利用率低于 1% 不显示；PoE 为 0% 不显示 <<<PAGE 101, 106>>>
"port utilization must be greater than 1% (e.g., a one Gig port should have at least a 10 Mbps data rate) before data is displayed"；PoE 报表需 PoE 在端口上用 CLI 预先启用。
## P22. 端口利用率预测数据量 = 配置区间的一半 <<<PAGE 103-104>>>
Last 24 Hours→12 小时预测；7 Days→3 天；4 Weeks→2 周；训练参数 Training Timeout 15-600s 默认 60、Training Error 0.1-1.0 默认 0.5（机器学习算法）。到 3 个月数据上限后覆盖旧数据 <<<PAGE 105>>>。
## P23. AP Uptime/Downtime 数据源与容量 <<<PAGE 116>>>
数据基于 Last Registration Time 或 alaOVSwitchUp/Down trap；"By default, information for all APs for the last 30 days is displayed (up to 5,000 records). If there are more than 5,000 records...prompted to download the records...as a .csv file"
## P24. Statistics：SNMP 源 IP 必须与发现 IP 一致 <<<PAGE 119>>>
"The IP source address of the SNMP Service on a device must be the same as the IP address discovered for the device by OmniVista. Statistics cannot collect data if..."
## P25. Statistics Collection Profile 默认值 <<<PAGE 120>>>
Poll Interval "Range = 1 - 60, Default = 5"；Data Retention "Range = 1 - 180 Days, Default = 30 Days"；新装 OV 自动统计默认开 2000 台、升级默认 0 台 <<<PAGE 134>>>；Interval 不能小于 Data Retention Period <<<PAGE 121>>>。
## P26. View Profile 上限 50 个计数器；统计按 1 小时平均 <<<PAGE 123, 124>>>
"up to 50 Counters can be displayed in a View Profile"；"Statistics are collected based on a one-hour average for each attribute"；Counter 缩放 Scale 为乘数，范围 0.001-1000。
## P27. 同一 Profile Type 一台交换机只能入一个 Profile；删 Profile/移除端口连带删 sFlow 配置 <<<PAGE 130, 131>>>
"a switch can only be in one profile of a particular Profile Type at a time"；"removing a switch from a profile automatically removes any ports...and removes the sFlow configuration from the ports"。
## P28. Analytics 全局默认值集合 <<<PAGE 134-136>>>
sFlow Port 默认 6343；Max Top N Apps/Clients Data/Day 32-256 默认 64MB；异常检测 Z-Score 上下阈值默认 BEYOND3Z-SCORE；Top N Ports/Switches Purge 1-8 月默认 3；Apps/Clients Purge 1-24 月默认 3；PoE Polling 1-24h 默认 1h；Top N PoE Purge 默认 8 月；Default PoE Threshold Usage 1-100 默认 99（Profile 覆盖项仅 AOS 8.x 支持）。
## P29. 异常检测最少需 11 天数据、最多学习 30 天季节性 <<<PAGE 133-134>>>
"A minimum of 11 days of data is required for anomaly calculation. Also, seasonal variation for periods of more than 30 days cannot be adequately learned"
## P30. Stellar AP 纳管容量与批量操作建议 <<<PAGE 142>>>
"OmniVista supports up to 4,000 APs...it is recommended that you apply the configuration to 500 APs at a time"
## P31. AP 自动注册的 DHCP Option 43/138 机制 <<<PAGE 140, 142>>>
Option 43 Sub-Option 1 指定 ALE Vendor ID "alenterprise"（1:c:61:6c:65:6e:74:65:72:70:72:69:73:65:）；或 Option 138 指定 OmniVista Server IP，AP 即向 OV 注册。
## P32. AP 802.1X 客户端限制 <<<PAGE 140>>>
OAW-AP1101 因 flash 小不支持；"When an AP is operating as an 802.1X client, the AP does not support untagged WLAN/SSID/client and cannot participate in a Mesh deployment"；用户名方式认证时 AP Group 的 802.1X Supplicant 须 Off 且交换机端口启用 Secure Mode <<<PAGE 141>>>。
## P33. AP 只能属于一个 AP Group；配置按组下发 <<<PAGE 137, 139>>>
"OmniVista does not manage individual APs...Any configuration applied to an AP Group is applied to all APs in the group"；各应用中配置对象为 "AOS Devices and/or AP Groups"。
## P34. AP Group 容量与角色限制 <<<PAGE 165>>>
"An AP Group can contain up to 512 APs"；"Only 'admin' and 'netadmin' users can add, edit, delete AP Groups"；Default AP Group 与 Default BLEGW Group 可编辑但不可删除。
## P35. AP Group 的 RF Profile 国家码必须一致；不同 RF 参数的 AP 应分组 <<<PAGE 144, 165, 172>>>
"the Country Code parameter in the RF Profile must be the same for all APs in an AP Group"；编辑组时 "the RF Profile must be from the same country"；"Do not add APs with different RF parameters to the same AP Group"（如 160MHz 信道宽度支持差异）。
## P36. Extended SSID Scale 规则 <<<PAGE 166>>>
开启后 AP Group 可挂 14 个 SSID，但仅支持 14 SSID 的机型可入组（AP1201/1321/1322/1261/1361D/1362/1301H/1331/1351/1451/1411/1431/1201BG）；6GHz 网络固定每 AP Group 限 4 SSID，不受该开关影响。默认 Disabled。
## P37. Use Private Config 覆盖规则（单 AP 覆盖 AP Group 配置） <<<PAGE 147, 149, 170>>>
单 AP 的 IoT Radio/Radio/WCF 私有配置"will take precedence over the...configuration for the AP set in the AP Group configuration"；关闭私有配置后回到组配置。
## P38. Zigbee/BLE 关键默认值 <<<PAGE 148-149, 169-170>>>
PAN ID 默认由 AP MAC 后两字节生成（范围 1-65534，不建议手工设）；Zigbee Discovery Duration 60-900s 默认 120；门锁 Vendor OUI 00:17:7A 且必须手工接受；BLE Emission Frequency 20-9,000,000ms 默认 200；Tx Power -20~10dBm 默认 4；Scanning Interval 4-10240ms 默认 100；Stellar Asset Tracking 必须开 Advertising+iBeacon+Scanning。
## P39. Stellar AP 不用 SNMP 被 OV 管理；SNMP 仅供第三方监控 <<<PAGE 168>>>
"OmniVista does not use SNMP to manage Stellar APs. With defined SNMP MIBs, an Administrator can monitor..."；SNMP 版本仅 v3/v2c 默认 v3，认证/加密协议固定 SHA+AES 且 Auth/Priv 密码相同。
## P40. 专用扫描模式对 WLAN 业务的影响矩阵 <<<PAGE 146-147>>>
无扫描射频机型：业务停止、客户端断开；Wi-Fi 6 带扫描射频(AP132x/1331/1351/136x)：不受影响；Wi-Fi 6E(AP1451)：2.4/5G 不受影响、6G 业务停止；Wi-Fi 7(AP1521)：不受影响。"Once"模式单次扫描最长 5 分钟且期间无客户端可关联。
## P41. AP 编辑组后自动重启；Edit IP Mode 屏显滞后 <<<PAGE 146>>>
"if you edit an AP's Group, the AP will automatically reboot for the change to take effect"；改 IP Mode 后屏幕仍显示旧 IP 直到 AP 上报新值。
## P42. AP LED 状态语义 <<<PAGE 152>>>
RED 闪=系统异常/链路 Down；RED 常亮=启动；红蓝轮闪=OS 升级；BLUE 常亮=双频运行；GREEN 闪=无 SSID；GREEN 常亮=单频运行；三色轮闪=定位用。
## P43. SNMP trap Server IP 不建议填 OV 服务器地址（防重复 trap） <<<PAGE 169>>>
"It is not recommended that you use the OmniVista [Cirrus] Server IP address to avoid the posting of duplicate traps in OmniVista"
## P44. Mesh MLO 仅 Wi-Fi 7 AP 且依赖 radio+EHT 开启 <<<PAGE 150>>>
MLO 适用于 AP1511/AP1521；"the MLO function also relies on the radio status and the radio Extremely High Throughput (EHT) setting"；Mcast Rate 默认 24（可选 6/12/24/36/48/54）。
## P45. AP 证书仅支持 FQDN 不支持 IP <<<PAGE 179>>>
"APs only support certificates based on FQDN, not IP Address. When generating the CSR file, you must match the 'CN' field to the URL 'mywifi.al-enterprise.com.'"
## P46. RadSec 证书多 CA 无签发顺序时只解析第一个 <<<PAGE 181>>>
"Do not import multiple CAs without an issuance order. If you import multiple CAs without an issuance order, OmniVista only parses and applies the first one to the AP"；Client Certificate 与 Client Key 必须分文件（转 CRT 时私钥部分被忽略）。CA/Client 证书仅支持 PEM/DER，Key 仅 .key。
## P47. BLE/WiFi RTLS 数据走 Kafka，内置证书只对接 ALE 自家引擎 <<<PAGE 182, 185>>>
"the built-in common device certificate on the AP allows communication only with Stellar AP Asset Tracking solutions [Cirrus 10 Stellar WiFi engine]. You can upload a custom device certificate...to third-party"。
## P48. Default Internal CP Certificate 全局配置，到期前 30 天告警 <<<PAGE 186>>>
"The Default Internal CP Certificate is used for AP built-in cportal certificate renewal and provides a warning 30 days before the AP certificate is about to expire"；不可删除/改名，只能用 ALE 生成的证书文件。
## P49. LBS/引擎按 AP 型号支持矩阵 <<<PAGE 191-192>>>
BLE LBS(Stellar Asset Tracking): AP1201/1201BG/1230/1320/1360/1311/1311BG；Aeroscout RTLS: 全部；Cirrus WiFi RTLS 与 Advanced Analytics: AP1201/1220/1230/1250/1320/1360/1311/1351/1301；Zigbee(Assa Abloy): AP1201/1201BG/1320/1360/1311。
## P50. Location/AA Server 关键默认值 <<<PAGE 192-193>>>
Aeroscout AP Listen Port 默认 1144；Stellar/Cirrus Server Port 默认 9093、Assa Abloy 443；Stellar BLE Upload Interval 1-30s 默认 5 但 Asset Tracking 必须设 2s；Allowlist 必含 iBeacon、KonLoc、KonSP；Cirrus RTLS Upload 15-255s 默认 30；Aeroscout 最小上报间隔默认 30s。
## P51. QoE 事件上传间隔默认值组 <<<PAGE 193-194>>>
User Info/User Tracking/AP Info/AP Radio/AP WLAN/Wired User 默认 5 分钟(1-15)；Short AP Info 默认 3；AP Channel/Rogue/Neighbor/Rogue Client 默认 60(15-60)；AP Channel Change=Instant（每 30 秒）。
## P52. L3 冗余参数与限制 <<<PAGE 197-198>>>
Retries 3-5 默认 3，重试尽即切备；Preemption 默认 Disabled，开启后 Countdown 默认 300s；仅 AP13XX+ 且 AWOS 5.0+ 支持（AP11XX/AP12XX 不支持）；需 cliadmin 配 Preferred Node；切换期间 OV 显示 AP down 5-10 分钟但实际在线。
## P53. App Launch 图标限制 <<<PAGE 199>>>
"Images can be .jpg, .gif, or .png files, with a maximum size of 60 x 60 pixels"；每页 15/30/45 图标。
## P54. Application Visibility 平台支持与 FTP 前置 <<<PAGE 201>>>
"Application Visibility is supported on OS6860E Switches, including a virtual chassis...where at least one OS6860E is present, and APs"；OV 必须 FTP 到交换机取数——发现时须提供 CLI/FTP 用户名密码（或事后 Topology→Edit Device 补）。签名自动更新仅 OS6860/6860E 与 Stellar AP。
## P55. 签名档案每设备/AP 组仅一个；换档案须先移除旧档 <<<PAGE 209>>>
"a switch can be assigned only one Signature Profile"；"To apply a new profile to a switch with an existing profile, you must first remove the old profile"；应用新档案会"erase...any Application Visibility configuration done from the CLI"。
## P56. 签名文件自动更新仅跨同 Major 版本 <<<PAGE 204, 211>>>
1.1.1→1.2.1 自动更新档案并下发；2.x 文件会下载但不更新 1.x 档案。Audit Switch Every 1-24h 默认 1；仓库预填 https://ep1.fluentnetworking.com/omnivista/signature/pull；下载失败重试 5 次、间隔 5 分钟；日志 afn_autoupdate.log。链路聚合成员口配置仅 OS6860N 8.7R2+ 支持 <<<PAGE 209>>>。
## P57. 审计日志归档参数 <<<PAGE 217>>>
Maximum Audit Entries 50-10,000 默认 2,000；Maximum Audit File Copies 0-100 默认 5；Max Log File Size 1-30,000KB 默认 10,240；User Activity Report 保留 7-365 天默认 90；Collect Support Info 不支持无线设备。
## P58. 认证服务器管理边界 <<<PAGE 218, 220>>>
"OmniVista cannot manage authentication server content"——OV 只登记服务器存在与连接参数；内置 OV LDAP 是唯一可由 OV 管理用户的。LDAP 服务器名不可改，须删了重建；删除服务器不改变交换机在用状态（直到重指派）。
## P59. LDAP 默认值与 SSL 端口行为 <<<PAGE 220-221>>>
Retries 1-3 默认 3（无线设备忽略）；Timeout 1-30s 默认 2；Port 默认 389，SSL 开启时交换机自动设为 636；SSL=NS/True/False，True 需选 LDAPS 证书；OS6860 (AOS 8.1.1 R01) 不支持 LDAP SSL。
## P60. RADIUS 关键约束 <<<PAGE 224-226>>>
Shared Secret ≤64 字符，>16 字符时 OV 仅支持 PAP/CHAP；认证端口默认 1812、计费 1813；TLS 开启时 Authentication Port 即 TLS 端口、Accounting Port 被忽略；Stellar AP 仅支持单个 RadSec 服务器（同 AP Group 的所有 SSID 必须用同一 RadSec）；AP1101/1201H/1201L/1201HL/1261-RW-B 不支持 AP RadSec 客户端；RadSec 不适用于 AP 的有线客户端；HA 时 Active+Standby 节点 IP 都须在 RADIUS 侧设为 Trusted。
## P61. ACE 服务器单台限制 <<<PAGE 219, 227>>>
"You are limited to a single ACE Server, because file sdconf.rec must be FTPed from the ACE Server to the switch's /network directory"；ACE 不存用户权限（权限由交换机自身决定）；不能用于二层认证或策略。
## P62. Captive Portal 配置层次（全局→Profile→Domain） <<<PAGE 232-235>>>
全局 Configuration 下发到交换机；Captive Portal Profile 只在启用了 CP 认证的 Access Role Profile 上有效并覆盖全局值；Domain Policy 再按登录域(Suffix/Prefix realm)替换 Policy List。Retries 1-99 默认 3。它是二次认证——"does not change the Access Role Profile assignment...provides a secondary level of authentication" <<<PAGE 231>>>。
## P63. CLI Script 不能发往 Stellar 无线设备 <<<PAGE 239>>>
"You cannot send scripts to Stellar Wireless Devices"；发送前 OV 必须已知每台设备的 CLI/FTP 凭据。
## P64. CLI Script 内置变量表 <<<PAGE 242-243>>>
$BASE_MAC/$BOOT_DIR/$CHASSIS_TYPE/$IP_ADDRESS/$LOGIN_ID/$LOGIN_PWD/$READ_PWD/$SECOND_PWD/$SYS_LOCATION/$SYS_NAME/$SYSTEM_OID/$SYS_VERSION/$WRITE_PWD；JS 中使用须加引号。cli 对象函数：sendCmd/lastResponse/setTimeout/trace/expectPrompt/deviceType/cliSleep/errorLog/forgetPrompt。
## P65. CLI Script 慢命令超时机制 <<<PAGE 241-243>>>
setTimeout(min,sec) 仅作用于下一条命令，之后恢复默认；最小 1 秒；<tapps> set timeout N 同效；慢命令（write memory flashsynchro）作末条命令会话即断——需补一条命令或设 tapps 超时。
## P66. 需确认提示的操作命令不能写进脚本 <<<PAGE 242>>>
"Operational commands that automatically issue a confirmation prompt...are not supported in CLI script files. Examples include takeover, reload, fsck"——除非用 expectPrompt/more/lastcmd 技巧处理。lastcmd 用于 reload 等会挂起会话的命令 <<<PAGE 244>>>。
## P67. CLI Scripting 日志保留默认 180 天 <<<PAGE 248>>>
Days to Retain "Range = 1 - 365, Default = 180"；日志位于 data\cli_scripting_logs，按设备 IP 分目录。
## P68. Watchdog 服务依赖连锁与 Web 服务自锁 <<<PAGE 249-250>>>
停服务会连带停其依赖服务；"If you stop certain services (e.g., ActiveMQ, Apache Tomcat)...the web server will shut down, and you will have to restart the service manually"。
## P69. Scheduler 任务模型 <<<PAGE 250-252>>>
System Jobs 不可改；User-Defined 可编辑（仅 Paused/Waiting 状态，admin 用户）；Overlap Policy: Ignore/Replace When Overlap；Crash Policy: Start Afresh/Resume From Crash；Priority 1-10；Retry Count/Interval 0-99；Timeout 20-9999s；Pause 保存进度并移出计划，Start 从断点恢复。
## P70. Discovery 设备可见性按用户角色过滤 <<<PAGE 255>>>
"Admin and Netadmin users will see all discovered network devices. For other users...Only the devices in the maps associated with a User's Role will be displayed"
## P71. 发现 IP 范围不得含广播地址 <<<PAGE 255>>>
"An IP range must not include a broadcast IP. If your network is divided into subnets, create multiple IP ranges with one IP range per subnet"
## P72. Discovery Profile 多档案回退机制 <<<PAGE 256>>>
一个 Range 可挂多个 Discovery Profile，拖拽排序：先用第一档案，失败换下一个，全失败用 default profile；成功后该设备固定使用此档案（除非手工编辑）。重新发现不会用新档案参数覆盖已录入的设备级参数（CLI/FTP 凭据等只对新发现设备生效）。
## P73. 手工添加 Down 状态的 Stellar AP 会占用第三方 License 且无法释放 <<<PAGE 257-258>>>
"If you manually add a 'Down' Stellar AP to the Managed Devices List, it will consume a Third-Party License. Once the AP comes 'Up' and registers...you will not be able to delete the previous entry or release the license"；正确做法是走 AP Registration 的 Unmanaged Devices 页签。
## P74. SNMP 默认参数与 v3 细节 <<<PAGE 258-260>>>
AOS 默认 SNMPv2（v1/v3 可选）；Timeout 默认 5000ms；Retry Count 默认 3；community 为 public 时可留空；v3 时 community 被忽略；SHA256+AES 192/256 需在 Preferences 装 Zulu CEK；Auth 密码空则认证+加密都不用；Context Name/ID 仅非默认第三方设备需要。
## P75. Trap Station User Name 缺省规则与 community string mapping 例外 <<<PAGE 260>>>
留空时：v3 用 v3 用户名；v1/v2 用 read community（community string mapping 未启用时 community 等效交换机用户名）；启用 mapping 时必须显式填有效设备用户名。
## P76. AOS Ping 操作的二级探测链 <<<PAGE 262>>>
SNMP ping 失败→发 alaSNMPDown trap→再试 SSH/Telnet ping（按 Shell Preference）→仍失败报 down 并发 alaOvSwitchDown；Stellar AP 用 WMA 检查可达性/可管理性。
## P77. 批量重启的防拥塞延迟公式 <<<PAGE 263-264>>>
"there is a minimum delay of 30 seconds...the delay is equal to roundoff of (30 + (deviceCount/4), in seconds"——1000 台延迟 280 秒。
## P78. 变更状态字段语义（Changes / Synchronized） <<<PAGE 273-274>>>
Changes: Certified（working=certified）/Uncertified（已存 working 未拷 certified）/Unsaved（running 未存）/Blank；VC of 1 的 Synchronized Status 恒为 Synchronized；stack 分裂后 license 数保持预分裂值以备恢复。
## P79. NaaS License 生命周期规则 <<<PAGE 284-285>>>
NaaS 过期后 30 天宽限期按设备活跃天数计（不活跃不顺延倒计时）；宽限期结束进入 degraded 模式（不可改配置/升级）；Upgrade License 过期无宽限直接 degraded；CLI 查询命令 show naas license；NaaS 仅支持 AOS 8.8R1+，Stellar AP 不支持。
## P80. 第三方设备 OID 录入规则 <<<PAGE 285-286>>>
只填 enterprises 分支后的值（Cisco=9，Extreme=1916）可识别全厂商设备；也可填具体型号 OID 共用 mibset；默认支持通用 MIB-2 trap，导入自定义 MIB 会自动扫描集成 trap 并即时生成 synopsis（可在 Trap Definition 修改）。
## P81. MIB 导入约束 <<<PAGE 287-288>>>
文件必须 .mib 扩展名；新目录须导入完整 MIB 集（含被引用的标准 MIB）；按依赖顺序排列（文件名与 import 语句常不一致）；不建议向 OV 自带 MIB 目录加文件；导入后不立即解析——发现对应 OID 设备或重启服务器时才解析。
## P82. Hardware Inventory/Ports 选择上限 <<<PAGE 288-289>>>
Hardware Inventory 一次最多 512 台；Ports 一次最多 50 台；Discovery Ports 不支持 AOS 6.x 的 Last Time Link Changed/Number of Status Changes；Port Split 仅 OS6900-Q32/X72 AOS 7.3.4.R01+。
## P83. 手工链路 vs 自动发现链路显示差异 <<<PAGE 290>>>
自动发现链路不可达时从拓扑消失；手工链路持久显示，断链时变红——适合核心链路监控。
## P84. Scheduled Upgrade 规则集 <<<PAGE 292-296>>>
设备只能属于一个升级计划；加入 VC 则整 VC 纳入；设备须 managed 且 running config 已保存（"unsaved" 会被跳过）；已运行目标版本则跳过；高于目标版本会被**降级**（有提示）；时间窗耗尽未升级的设备等下次 recurrence；升级必然自动重启；Image 与 BMF(U-Boot/Miniboot) 可分别设置 Install Action，Install Directory 默认 /flash/working；镜像须先从 Business Portal 下载并导入 Resource Manager。
## P85. 自动发现默认轮询间隔按网络规模分档 <<<PAGE 298-299>>>
规模 Low(≤500)/Medium(500-2000)/High(2000-5000)/Very High(5000-10000) 对应 Full Discovery 8/10/12/18 小时、Occasional 4/6/8/12h、Regular 1/2/4/8h、Frequent 5/15/30 分钟/2h。层级包含：Full⊇Occasional⊇Regular⊇Frequent（Regular 含 AMAP/ARP/BFT 轮询，Frequent 含 down 轮询+sysName/sysDescr+配置变更状态）。
## P86. IP Failover 与 REST API 轮询 <<<PAGE 299-300>>>
IP Failover 开启后主 IP SNMP 失败切备用 IP 并后续流量全走新地址；REST API Polling 默认开启（AOS 8.7R3+，Locator/LLDP/SPB 性能更好），前置：aaa authentication http、webview server enable、ip service http admin-state enable、设备属性中 CLI 用户有读权限；失败自动回退 SNMP（Audit 日志搜 "Fallback"）；凭据错误会造成 trap 风暴；每次 HTTPS 登录在 swlog 记 INFO 属正常。
## P87. Groups：所有被策略引用的组都不可删 <<<PAGE 303-307>>>
MAC/VLAN/Network/Multicast/Service Group 及 Service/Service Port "in use by policy conditions cannot be deleted"；组名不可改只能删除重建；Service Group 不能混用 Source 和 Destination Service。
## P88. IoT 机制与限制 <<<PAGE 308-313>>>
MQTT 实时上报+云指纹服务(fingerbank)分类，分类随指纹累积逐级细化；支持 AOS 8.6R1+ 与 Stellar AP 3.0.7.xx+，仅 IPv4；IoT 开启只作用于全部 UNP 口，固定端口需 CLI device-profile port x/x/x admin-state enable；数据保留最多 60 天覆盖；每设备默认显示最新 1 会话（最多存 3 个：当前+2 历史）；IPv6 终端 AOS 下 15 分钟才显示、Stellar AP 不显示；Alcatel IP Phone 需 CLI "qos no phones" 才上报指纹。
## P89. IoT 状态语义陷阱 <<<PAGE 311-312>>>
删除交换机/关闭其 IoT 后其下所有终端显示 Offline（无视真实状态）；交换机 down 不自动改终端状态；Enforcement Status: Initial/Excluded/Enforced/Failed/Pending(可能 ARP 未配)/Disabled(手动模式)。
## P90. IoT Settings 容量参数 <<<PAGE 322>>>
Days Before Purge 1-60 默认 30；Historical Records Count 0-25 默认 2；Total Records 1-500,000 默认 100,000（超限先清历史再清离线记录）。
## P91. Zigbee 设备接受状态机 <<<PAGE 315-316>>>
New Devices(Auto Rejected 默认)→Accept→Accepted Devices；Reject→Rejected Devices；LQI >30% 才可靠通信、<10% 无法通信；Auto Accept 由 AP 白名单 OUI 决定；Zigbee 设备不经指纹服务，AP 直读+Zigbee Server。
## P92. PIM Profile 唯一性与默认档案 <<<PAGE 325>>>
最多 4 个 PIM Profile 且两两参数组合不能相同；Default PIM Profile 不可删除只能从交换机移除；移除/删除档案会把 Sparse/Bi-Direction 重置为 Disable。
## P93. PIM BSR 选举规则 <<<PAGE 327>>>
每 PIM 域仅一个 BSR；"The Candidate BSR with the highest priority level is elected as the BSR...If two or more Candidate BSRs have the same priority value, the C-BSR with the highest IP address is elected"；每交换机仅支持一个 RP 地址；Candidate Profile 只在已配 PIM Interface 的设备上可选。
## P94. License 类型与升级矩阵 <<<PAGE 330-334>>>
三类：Starter Pack（免费 30 设备：10 AOS+10 三方+20 Stellar AP；VM 10；Guest 10，不过期）/ Evaluation（60 天全功能）/ Production；HA License 仅 Production；管理规模认证上限 10,000 台；VM Manager 支持 5,000 VM（超出告警写 VMM log）；升级规则核心：新许可设备数≥现有→直接升；否则须先减设备；Production→Evaluation 属降级不允许；AP/WCF/Guest/On-boarding 许可按 10/20/50/100/500（Guest 另有 1000）档位。
## P95. Locator 搜索机制 <<<PAGE 336-339>>>
一切搜索最终归结为 MAC（IP/用户名先解析 MAC）；Live Search 的 "Live" 定义为最近 5 分钟内活跃；Live Search 不轮询 Stellar AP（找不到其客户端）；IP 搜索要求网关设备被 OV 支持（否则 IP 无法解析成 MAC）；按 IP 搜索 Netforward 表列出历史全部关联 MAC——可用于查 IP 冲突；仅支持 IPv4。
## P96. 自定义 Netforward 视图限制 <<<PAGE 341>>>
最多 2 个 Custom Template，新建会替换旧视图；模板按用户隔离。
## P97. mDNS 设备角色互斥与平台支持 <<<PAGE 352, 354>>>
"A switch can be configured as either a Gateway Device or a Responder Device. It cannot be configured for both"；也不能既做 Responder 又做别人的 Edge。Gateway 支持 OS6450 AOS 6.7.2.R02+、OS6860E/6865/6900 8.4.1.R02+；Responder 支持 OS6860/6865/6900/9900 AOS 8.7R1+；Edge 支持 OS6465/6560/6860/6865/6900/9900 AOS 8.5R1+ 及 AWOS 4.0.1+（AP1101 除外）。
## P98. mDNS 默认行为是 restrict all <<<PAGE 351>>>
"If there is no rule/policy configured on a switch, the default behavior AOS behavior is 'restrict all'"——配完 Responder 必须再配 Service Rules，否则不处理任何客户端查询；Responder/Edge 之间 IP 连通性属基础设施配置（可能需静态路由，可用 CLI Scripting 批量下发）。
## P99. mDNS Location 推导链 <<<PAGE 360-361>>>
Port Alias > System Location+Port ID > System Name+Port ID > Chassis ID+Port ID；AP 的 Location 取其上联 AOS 端口位置。Server/Client Policy 名 ≤31 字符，须至少一个匹配条件（VLAN/Access Role Profile(AOS 8.7R2+/AWOS 4.0.1+)/Location/UserName/MAC）。
## P100. mDNS 查询包 VLAN tag 固定 4095；缓存每小时轮询 <<<PAGE 355, 363>>>
"For every query packet generated by the Responder Device, the mDNS packet has a VLAN tag of 4095"；"Service Cache is polled every one hour"；Legacy mDNS 每设备仅一套配置、仅 L2 GRE。
## P101. Locator 设置项 <<<PAGE 348-349>>>
三个超时（历史/实时/轮询）；802.1q Port Filtering：Standard 模式必须用于 VM Manager（VM 用 tagged 包通信），否则 VM 检测不到；Data Retention 默认 30 天，不启用则数据无限累积。
## P102. Trap 重放时间戳回算机制 <<<PAGE 368>>>
重放 trap 的 Date/Time 按设备当前 upTime 与 trap 内 upTime 之差回算原始时间——"if the network was down for hours, you may suddenly see traps appear from hours ago"。
## P103. Trap Responder：severity 与 filter 是 OR 不是 AND <<<PAGE 371>>>
"you cannot specify traps using both severity levels and filters...the trap responder will respond to all traps with the specified severity (even if they do not match the filter), and all traps that match the specified filters"；Stellar AP 的 Responder 必须用 AP Group 选项（Device IP 范围无效）；邮件动作前置 Preferences 邮件服务器配置。
## P104. Trap Email 合并防风暴 <<<PAGE 379-380>>>
默认满 1 分钟或 100 条 trap 才发一封合并邮件（Maximum Trap Limit / Maximum Time Limit 可调）。
## P105. Trap 存储与端口默认 <<<PAGE 379>>>
Max No. of Notifications 1,000-300,000 环形覆盖；Trap Port 默认 162；Trap Replay Polling 默认 On；Trap Absorption 默认 Off（吸收周期 0-600s 默认 15s，收到相似 trap 会续期）；WIPS traps 接收默认 On。"充分相似"=名称+Agent IP+OID+severity+enterprise OID+全部变量相同。
## P106. Trap 配置向导的 Save 细分 <<<PAGE 378>>>
Trap Subscription State: On/Off/Delete（Delete 用于 OV 服务器换 IP 后清理）；Save 可选 All/Port Only/State Only/Traps Only/Protocol Only；首次配置时选任何 "Only" 等效 Save All；Protocol 默认 SNMPv3（仅 AOS/6200）；不能为 AOS 无线设备配 trap（可设备端配置后转发到 OV）。
## P107. OV System Health 阈值默认值 <<<PAGE 383>>>
CPU 90%、Memory 95%、Paging 10,000Kbps、Memory Commit 150%、Data/OS Partition 80%；同类 trap 间隔 30-120 分钟默认 60；采集 60-3600s 默认 60s；保留 1-90 天默认 30；widget 刷新 1-15 分钟默认 1。VM 配置检查项：CPU Core/RAM/HDD/CPU+Memory Reservation（后者仅 VMware ESXi+Tools）。
## P108. PolicyView 架构与 OpenFlow 冲突 <<<PAGE 384, 385>>>
策略存 OV 内置 LDAP，交换机经 SNMP 通知后自行取回并执行；"Enabling Open Flow will consume all available TCAM resources. If Open Flow is enabled, you will be unable to configure QoS Policies"（已有策略继续生效，新策略无法创建）。
## P109. Policy 优先级分区 <<<PAGE 387>>>
PolicyView 策略优先级 30001-65535：One Touch Voice 45000-65535、One Touch Data 40000-44999、Expert Mode 30000-39999；外部工具（CLI/WebView/MIB）可占用 0-65535 全域——切勿给外部策略分配 30001-65535；外部创建的策略不进 LDAP 不可由 PolicyView 管理。
## P110. 统一策略细节约束 <<<PAGE 387-389>>>
Unified Policies 单独成表（不与 Expert 策略混显）；不能直接应用到 IAP（须封装成 Policy List→Access Role Profile→下发）；Expert Mode 只能选 AOS 设备，Unified 可选有线+无线但不能选 IAP；编辑被策略引用的 Group 后不能只 re-notify，须建新 Group 并改策略；条件/动作会按所选设备校验。
## P111. L2 MAC 条件跨路由失效与通配符规则 <<<PAGE 390-391>>>
"Layer 2 Conditions...are 'lost' when traffic passes through a router"——多跳场景改用 L3 条件；MAC 通配符 * 必须逐位填写（00435C:****** 非 00435C:*）；AP 的 MAC 地址条件不支持通配符；同策略含源+目的 MAC 可能被部分平台拒绝，建议拆成两条策略。
## P112. ALE 语音/IP 电话 MAC 段 <<<PAGE 391>>>
Voice: 00809F3A/B/C 段；IP Phones: 00809F3D；Multi-Media: 00809F3E/F。Source MAC Range 仅 AOS Wireless 支持；MAC 条件在 IAP 上忽略；MAC Range 在 Stellar AP 上忽略。
## P113. 条件与动作的平台差异汇总 <<<PAGE 391-395>>>
同时指定源+目的 IP 会被交换机拒绝（拆两条策略）；IP 地址不允许 * 通配；Shorthand Mask/Group 对 Wireless Controller/IAP 忽略；Stellar AP 仅 IPv4 条件；NAT 动作要求条件与动作都用 Network Group；DSCP 0-63 与 TOS 0-7 互斥；DSCP/TOS 条件在 WC/IAP 忽略；QoS 动作在 IAP 忽略；TCM 与 Set Color of Packet 不支持无线设备；802.1p 0-7、出端口不支持 802.1p 时动作失败；QoS 等级映射 Platinum=7/Gold=5/Silver=3/Bronze=1。
## P114. Policy List 默认行为与设备差异 <<<PAGE 398>>>
未匹配流量的默认动作：AOS 交换机与 Stellar AP 为 accept，AOS Wireless 为 deny；可用 OV-L3-AcceptAllPolicy / OV-L3-DenyAllPolicy / Device-Default 覆盖；WC User Role 仅支持 Downstream Bandwidth Contract 且仅一条 QoS 规则（"Unified Policy List can't contain more than one QOS Action"）；OS6360/6465/6560/6570/6870 不支持 L2 Source MAC 条件。
## P115. Notify 代价与策略删除非联动 <<<PAGE 396-397, 400>>>
"When you notify network switches, all QoS-enabled switches flush their policy tables and reload policies from the LDAP repository, which is very expensive"——建议批量一次通知；在 OV 删除 Policy/Policy List 不会自动更新交换机，须再 Notify Selected；关联 Access Role Profile 的 Policy List 不可删。
## P116. Resource 策略默认参数 <<<PAGE 401>>>
Resource 定义后自动生成 LDAP 策略：默认 precedence 50000、action Accept、有效期 AllTheTime；Resource 名不可改只能删建。
## P117. One Touch 策略自动成对生成与命名 <<<PAGE 404-405, 407-409>>>
每输入一个 IP/MAC/Network Group 自动生成源+目的两条策略（OneTouchDR$S/IP、OneTouchDR$D/IP；OneTouchAR$S/D/组名）；One Touch Voice 固定 Platinum；Voice IP/MAC 策略删除时 L2+L3 一并删除；Expert 模式不能编辑 One Touch 策略；Priority 修改对表内全部服务器生效。
## P118. Preferences 关键默认值 <<<PAGE 416-420>>>
User Settings 任何用户可改，System Settings 需 Account Admin Role；Inactivity Timeout 15 分钟-25 周，默认 15；默认主题 Flat World；声音 .wav/.mp3 ≤500KB，自动确认的 trap 不发声。
## P119. Proxy 必需的四个外部站点 <<<PAGE 421>>>
ALE Central Repository ovrepo.fluentnetworking.com（升级软件）、AV Repository ep1.fluentnetworking.com（签名文件）、Fleet Supervision myfleet.ovcirrus.com、Call Home Backend us.fluentnetworking.com——均走 443。
## P120. Fleet Supervision 机制 <<<PAGE 421-424>>>
OV ID 安装时自动分配不可改；初始上传后每 2 周自动上传库存；Management System 按 OV ID 绑定 OV 实例（Test Connection 验证）；Device Catalog 未填充时先检查 OV 是否成功上传。
## P121. Email/SMS 集成约束 <<<PAGE 425-427>>>
SMTP 全字段必填且 From 须为有效地址否则被邮件服务器丢弃；UPAM 邮件在 UPAM Settings-Email Server 单独配置；SMS 四供应商 Plivo/Telefonica/Vodafone/Aliyun；Plivo 多源号码轮询。
## P122. Provisioning 平台与目录要求 <<<PAGE 430, 434>>>
支持 AOS 6.7.2.R06 GA+ 或 8.4.1.R03 GA+；交换机须从 Working Directory 运行（Thin Switch 例外，可 Certified/Working/自定义）；从 Certified 配置的交换机配置临时、重启即丢，须 reload working + Force Provision 补救；6.x 命令 reload working no rollback-timeout，8.x 为 reload from working no rollback-timeout；新交换机 8.6R2+ 自动 Call-Home，8.6R1 及以下须 CLI cloud-agent admin-state disable force 后再 enable。
## P123. Default Management Template 凭据策略 <<<PAGE 433-435>>>
新交换机：默认"Create new credentials"，OV 用默认 admin/switch 登录后创建 ov-enterprise 用户（密码自动生成）管理 SSH/SNMP/SFTP；已在用交换机：选"Use existing credentials"填现凭据；配置模板与现有配置冲突会导致 provisioning Failed，可改 Rule 后 Force Provision；成功部署后强烈建议改掉默认 admin 密码（CLI Scripting 批量）。
## P124. Thin Switch 关键约束 <<<PAGE 437-438>>>
Thin Switch 属性一经 provision 不可改（须删规则重建）；Thin=Yes 时 Save and Certify 强制 No；Incremental Template 仅在首次 Periodic Call-Home 后应用一次、不能在建规则时配置；vcboot.cfg 不被修改；无 vcboot.cfg 的裸机 8.6R2+ 可免最小配置直接瘦部署。
## P125. Strong Password 行为 <<<PAGE 429>>>
Password Expiry 90-365 天默认 90，到期前 30 天告警；关闭 Strong Password 时 Expiry 自动重置 Never；强密码规则不追溯既有用户（改密码时才生效）；忘记密码须用 VA 菜单重置。
## P126. Aliyun SMS 模板审批流程 <<<PAGE 428>>>
Apply 后生成模板（Pending Approval），审批约 2 小时；OV 不自动刷新状态，须反复点 Get Status；失败模板用 Regenerate Failed Templates 重建，全部通过才能发短信。Collect Support Info 保留 1-31 天默认 7。
## P127. Provisioning Rule 匹配优先级与约束 <<<PAGE 439-440>>>
序列号/MAC 与型号互斥（不能同填）；同一设备同时有序列号与 MAC 规则时序列号优先；序列号规则优先于型号规则；每型号仅一条规则；型号名必须精确（含 P48 等后缀，可省略 OS 和连字符）；目标设备已在 Managed Devices 时规则创建报错；模板编辑只影响后续匹配的交换机。
## P128. 配置模板禁用命令与变量规则 <<<PAGE 442-443>>>
Configuration Manager 管的命令（user admin password、write memory、configuration apply）不能进模板，否则 provisioning 失败；映射变量不能含特殊字符（@#+被忽略）、不能有空格（多词用下划线）；静态 IP 不能与 Managed Devices 中设备冲突。
## P129. Provisioning 状态机 <<<PAGE 447>>>
Rule 状态：No Match（设备已联系但无匹配规则，每 5 分钟重试）→Set Up（规则建好等设备）→Matched（至少匹配一台）；Results Status: Succeeded/Failed；Incremental Template Apply Status 成功后自动禁用不再重发。
## P130. Golden Configuration 机制 <<<PAGE 448-452>>>
从最近 3 次备份（provision 后每日备份）中选一作为 Golden；不含交换机用户（用户库受保护）；4.5R2 前的 Golden 无快照信息不能比较须重建；审计发现差异→Sync Status=Out of Sync→三选一：Enforce Golden Config Now（回推并 reload，Certified 目录运行的交换机不能 enforce）/Mark as New Golden Config/Clear；审计默认每天 0:00。
## P131. Thin-Client 默认参数与配置确认乐观假设 <<<PAGE 456, 455>>>
Time To Next Callhome 默认 30 分钟、Max Retry 默认 30 次；OV 下发 Configuration Apply 后靠 show configuration status 确认——若因连接丢失收不到回执，OV **假定成功**并报告 Succeeded、设备入 Managed Devices。
## P132. Quarantine Manager 架构与无线客户端特殊路径 <<<PAGE 457, 460>>>
外部 IPS（Fortinet 2.3）/交换机发 Syslog(端口 514)或 trap（含 IP/MAC）→规则触发→Candidate 或 Banned；EMP 子网设备不可隔离；无线客户端不进 Banned 而是进 Client Blocklist（WLAN-Client-Client Blocklist，保留 365 天）——避免关端口殃及同口其他客户端并防漫游逃逸；此路径要求在 Stellar AP 上启用 IoT；4.9R1 前已在 Banned 的无线客户端不自动迁移。
## P133. Quarantine 隐式 Never Banned 与 Fast Re-Cache <<<PAGE 464, 462>>>
OV 服务器和所有已发现交换机隐式在 Never Banned 列表（不显示也不可 ban）；OmniAccess WLAN 设备 ban 需在 Secondary Password 填 enable 密码；Fast Re-Cache（仅查隔离 MAC 组、不 flush 其他策略）仅 6400/6850/6855/9000 且 6.3.1.R01+。
## P134. Quarantine 规则优先级与内置规则 <<<PAGE 466>>>
"Banned rules have precedence over Candidate rules...match the first rule that places a device on the Banned list"；13 条 Built-In 规则默认 Disabled、默认动作 Candidate、可改不可删；QMR 与 QoS inner VLAN/802.1p 策略及 VLAN Stacking 互斥 <<<PAGE 459>>>。
## P135. Quarantine 内置规则的 Fortinet status 语义 <<<PAGE 467>>>
内置触发式排除 status=detected/pass_session（正则 status=[^p].[^t]）；Fortigate 设 Pass 的攻击仍发 Syslog 但不触发隔离；内置 13 条规则（Alcatel DOS Trap、Brick、Fortinet Anomaly/Signature/Virus、HTTP DOS、SafeGuard×2、OA WLAN×5）默认 Disabled+Candidate 动作。
## P136. Quarantine 规则正则要点 <<<PAGE 468-470>>>
Trigger Expression 匹配 Syslog/trap（Java 正则，类 PERL/AWK）；Extraction Expression 用 ( ) 捕获源地址（支持十六进制 IP）；AOS DOS Trap 内置 TrapName=alaDoSTrap.*alaDoSType=[0|2|6]，扩展到 0/2/6/9/10-13 写法 ([0|2|6|9]|1[0123])，注意 [0-13] 是错误语义；抽取失败查 server.txt。
## P137. Quarantine 基础设施三件套 <<<PAGE 473-475>>>
预置 Quarantined VLAN 需配套：①Groups 建 "Quarantined" MAC Group（名字必须匹配）；②PolicyView 建 L2 Source MAC Group 条件+Drop 动作的策略；③Configuration 屏配置 VLAN/MAC 组/Remediation URL+IP/HTTP Proxy Port/Default QMR Page/Allow Port Disabling（全局+逐设备两级开关）/Allowed Subnets（≤3 个，必须含 Remediation Server）；未配置 VLAN/MAC 组时 Banned 设备照样能通流量；端口禁用只看 Locator Live Search 不看历史。
## P138. QMR 数据面机制 <<<PAGE 473>>>
隔离客户端 MAC 入 LDAP MAC 组→QMR 拉取填充交换机 Quarantined 组→仅可访问 Remediation Server+例外子网+ARP/DHCP/DNS；解除后 QMR 下次查 LDAP 时恢复。
## P139. Quarantine Responder 变量集 <<<PAGE 477>>>
$Action$/$Reason$/$MacAddress$/$IpAddress$(未知显示 0.0.0.0)/$VlanName$/$MacGroupName$/$Details$；Banned/Released 两个触发维度分别 Respond/Ignore；邮件依赖 Preferences Email 全字段。
## P140. TAD 支持范围 <<<PAGE 478>>>
"Traffic Anomaly Detection is supported on OS6850, OS6855, OS9700 Switches running AOS 6.4.6.R01"——按端口进/出速率差+流量模式匹配检测异常，超阈值可 log/trap/隔离端口。
## P141. TAD 参数与异常类型默认 Count <<<PAGE 478-479>>>
最多 32 个监控组（组名 ≤32 字符）；14 种异常类型（ARP×3/ICMP×3/TCP×8），默认 Count 如 arpflood 90/synflood 90/arpaddrscan 50/rstcount 50/arpfailure 6/finscan 6 等（范围 1-100,000）；Sensitivity 1-100 默认 50；Period 5-3600s 默认 30；Log/Trap/Quarantine 默认全 Disabled；Syslog Listener 默认 514。
## P142. Report 两步创建模型与限制 <<<PAGE 484-486>>>
先在 Report 应用建配置（Schedule Now/Periodically Simple|Cron、Purging Policy、唯一一个邮件收件人、打印参数），再到源应用（Discovery/Locator/Analytics）点 Add to Report 绑定；首次配置生成空白报表直到绑定；外部 RADIUS 用户不能定时报表；Periodic 报表不能手动 Generate（仅 Now 可）；邮件超邮件服务器大小限制（如 Gmail 25MB）会失败；Generating 状态的报表不可删。
## P143. Backup 三类型与 FTP 语义 <<<PAGE 488-493>>>
Full（Certified 或 All=Working+Certified+Switch+Network 目录，可选 Diagnostic/Dump 默认排除）/Configuration Only（全部目录配置文件，AOS 可排除 Security Files 默认包含）/Images Only；镜像文件不 FTP 只记录版本号——Restore 前必须把对应镜像导入 Upgrade Image Repository（无版本信息的文件才物理拷贝）；删设备连删其备份；Backup by Maps 混合地图时 Stellar AP 不被备份（只能按 AP Group 备）；>50 台建议按 Maps；备份中途失败则全部作废；仅备份主 MPM flash；不备份 .err/.dmp；备份文件未压缩且含源机器 IP/MAC 二进制信息——严禁拷给其他机器；设备配置 SSH 时用 SFTP。
## P144. Restore 约束 <<<PAGE 494>>>
只能还原到原设备（否则 IP 错配）；AOS 6.x 且仅选 Certified 文件时可选还原到 Working 或 Working+Certified（7.x/8.x 无此选项）；chassis 变更/发现新镜像文件默认阻断（两个 Continue 复选框放行）；Stellar AP 不能配置还原但可镜像还原；还原后必须重启设备。
## P145. Compare 与 Upgrade 约束 <<<PAGE 495-501>>>
Diff 仅文本文件（boot.cfg 为主），不能比较二进制(.img/jpg/jar)；升级文件必须来自 ALE 客服（含 LSM 描述文件，OV 拒绝不支持升级）；*.zip 自动解压勿手工解；FTP 超时默认 5 分钟——大文件升级前须 CLI 调大 session ftp timeout；先升 Image 再升 U-Boot/Miniboot；OS9907/9912 U-Boot 分 Denverton(CMM2/CNI-U20)与 Rangeley(CMM1/其他 NI)两种文件；ISSU 要求冗余+全 certified+同步，flash 至少须 mandatory images+3MB，不能选单文件，OV 不校验 ISSU 镜像与当前版本兼容性（由客服告知）；FPGA 升级仅 OS9000/6450/6250 AOS 6.6.4.R01+；多 Working Directory 支持 OS10K/6900/6860；降级安装有告警可能丢功能。
## P146. Auto Configuration 文件体系与触发条件 <<<PAGE 503-506>>>
触发：交换机 /flash/working 无 boot.cfg（新机或删文件重启）；DHCP Option 66=TFTP(OV) 地址、Option 67=Instruction File 路径、Option 60(厂商类)选型；Instruction File 扩展名必须 .alu，按机型每型一份；主服务器重试 3 次失败切备用服务器；Script 未指定/下载失败时自动执行 reload working no rollback-timeout；Script 含 write memory 会覆盖 boot.cfg（随配置文件下发时禁用）；OV TFTP 传输上限 4GB (RFC 2347)。
## P147. Switch File Set 文件名规范 <<<PAGE 508-509>>>
banner.txt / background.gif|.jpg|.png / cpLoginHelp.html / cpLoginWelcome|cpStatusWelcome|cpFailWelcome|cpBypassWelcome.inc / cpPolicy.html / logo.gif|.jpg|.png——名字固定；CP 按 gif→jpg→png 顺序找文件；先在单台交换机验证再全网推送。
## P148. Backup 保留策略算法 <<<PAGE 510>>>
Minimum Backups 1-365 默认 365；Maximum Days 1-365 默认 365；保留 max(b, n)（n=未超期备份数），新备份成功后应用；BMF 升级最小 CMM 空间默认 4.5MB。
## P149. SAA 前置与容量 <<<PAGE 512-514>>>
支持 AOS 8.x+（OS6560 需 Metro License）；前置：启用 8 个 alaSaa* trap（ID 117-119/146-150）+ Settings 配默认指标；最多 127 个 SAA（建议 ≤50 省资源）；仅支持 MACSAA 测试类型；交换机未保存配置重启后 SAA 残留于 OV 不可改删——需重新发现设备清除；运行中的 SAA 不能删。
## P150. SAA 默认阈值 <<<PAGE 514>>>
RTT/Jitter Threshold 1-1,000,000μs 默认 100；Packet Loss Threshold 1-100 默认 5 包；Interval 1-1500 分钟默认 150；Inter Packet Delay 100-1000ms；Number of Packets 1-100 默认 5；Payload 24-1472B 默认 32；ISID 256-16777214。
## P151. SAA VM Profile 与 VM 迁移规则 <<<PAGE 518>>>
VM 对不直接配 SAA 而是建 Profile 关联；同交换机迁移 Profile 不变；跨交换机迁移：有同配置 SAA 则关联（状态冲突时警告需手工改状态：Stop+Start 或 Start+Stop），无则自动新建同配置 SAA；Profile 前缀 SAAExpertProfile（交换机对）/SAAVMProfile（VM 对）；数据保留 1-90 天默认 30（到期自动停止，重启后超期数据删除）。
## P152. SPB 服务核心概念 <<<PAGE 523-525>>>
SPBM (IEEE 802.1aq)+PBB(802.1ah) MAC-in-MAC 封装；ISIS-SPB 建最短路径树；BEB=有 SAP 的边缘桥、BCB=无 SAP 但有 BVLAN+SPB 接口的核心桥；Service ID/ISID 1-32767 自动递增预填（ISID 绑定 BVLAN+Service ID）；BVLAN 须 CLI 预先配置；Multicast Mode Headend(默认,逐接收者单播复制)/Tandem(逐节点组播复制)——同一 BVLAN 全网必须一致且两种模式互通；VLAN Translation 默认 Disabled；VPN MTU 默认 1500。
## P153. SIP Snooping 机制与拓扑限制 <<<PAGE 531-532>>>
SIP Snooping 识别并 DSCP 标记 SIP/RTP/RTCP 流；从 RTCP 计算 delay/jitter/RTT/R-factor/MOS；要求信令与媒体流路径对称——"MC-LAG, ECMP routing and VRRP topologies are not supported"；Multi-Chassis 配置的 9000E 设备不显示且分配报错。
## P154. SIP One Touch 规则与固定优先级 <<<PAGE 538-539>>>
Voice: condition "sip audio" action dscp 46, precedence 固定 50000；Video: sip video/dscp 34/44000；Other: sip other/dscp 24/44001；Edge 设备端口全部 Automatic+Enabled，Non-Edge 需手工设 Port Mode；每交换机仅能有一个 One Touch/SIP Policy（换策略先移除）。
## P155. SIP Profile 子档案与同步语义 <<<PAGE 541-550>>>
SIP Profile = Global Params+Trusted Servers(≤8 IP,0.0.0.0 无效)+Threshold+SOS(≤4 条,精确 URI 无正则,字符 a-zA-Z0-9@,留空字段下发时清空交换机旧值)+TCP Port(≤8)+UDP Port(≤8) 各最多一份；子档案被编辑→SIP Profile 标 Out of Sync，已应用设备保持旧配置直到重推；子档案重应用会完全替换交换机旧配置（非增量）；Threshold 默认：Jitter Audio 50/Video 100ms、Packet Loss 10/20%、RTD 80/250ms、R-Factor 70/80、MOS 3.6/3.0（新范围 0-5 为旧 0-50 的 1/10）；Global Params: DSCP 0-63（0=NA）、Threshold No. of Calls 50-500。
## P156. Topology 视图与状态颜色体系 <<<PAGE 554-561>>>
默认打开是 Geo Map（地理图），可切传统 Topology Map 并设默认；设备状态圈：绿=Up（AOS 的 Up 不代表可管理，看 SNMP Status）/橙=Warning（有 trap）/红=不可达（网上可能仍在运行）；通知圈（右上小圆）：无=Normal/橙 Warning/紫 Minor/黄 Major/红 Critical；链路：绿全 Up/橙部分 Down/红全 Down/蓝未知；手工链路虚线（混合则实线）、聚合链路椭圆、Multi-Chassis 黑边椭圆、Mesh 链路 Wi-Fi 图标；ping sweep 发现后链路要等下次轮询或手动 Poll Links 才显示；缩放聚合 Cluster 颜色规则同设备/告警；颜色可改（Preferences-Colors）；网格显示影响性能仅排图时开。
## P157. Topology SPB/ERP 专题视图机制 <<<PAGE 565-574>>>
SPB/ERP 均在交换机 CLI 配置、OV 只读展示；SPB Map：Map Level Actions→SPB Network，配置/端口小盒绿=全 Up、橙=部分 Down、红=全 Down；SPT 链路须选两个 BEB+BVLAN 才高亮；SPB 数据每 3 小时自动轮询（Poll Latest Data 手动）；SPT 中设备 down 后到下次轮询前仍显示旧路径；L2 交换机链路信息要求其 SAP 端口挂 802.1ab(Peer) 的自定义 L2 Service Profile；ERP Map 按搜索 Ring ID 过滤环链路；SAP VLAN 显示规则：1/1/x:0 或 1/1/x:Inner 可管理，单外层 VLAN 显示一个、内外都有显示两个、untagged 无显示。
## P158. Geo Map 站点模型 <<<PAGE 575-578>>>
Site（街道/坐标定位）自动生成同名逻辑图；Sub-Site=Site 图下的子图（Building/Floor）；设备只能属于一个 Site/Sub-Site（移动须先移除）；建 Sub-Site 的推荐顺序：先建空 Site 再在 Sub-Site 建时分配设备；编辑 Sub-Site 用 Edit Map 而非 Edit Site；Site 圆圈显示设备总数+状态汇总+最高级别 trap 状态；有 Geo Location 的设备移出 Site 后单独显示在 Geo Map。
## P159. L2 认证与分类决策流 <<<PAGE 591-592>>>
全部用户经软件学习（forwarding/filtering）；优先 802.1X，非 supplicant 或禁用时用 MAC 认证；RADIUS 返回有效 UNP 名→映射 Access Role Profile+VLAN（显式 policy list 名可覆盖 UNP 自带策略）；认证未启用/失败/无有效 UNP 且启用分类→按 Port/Group ID/MAC/LLDP/Authentication Type/IP Address 分类规则给 Default UNP；UNP 与 VLAN 一旦分配不再改变。
## P160. Topology 设备操作集与限制 <<<PAGE 584-587>>>
右键或 Detail Panel 操作：Overlay View（VC/Stack/无线/AP-Node 关系叠加视图）、Copy Device to Map、Remove from Map（Physical/系统生成/动态图不可移除）、Edit/Delete/Copy as New Device、Ping/Poll Device/Poll Link、Reboot、Copy Working↔Certified、Save to Running、Webpage、Configure Health Thresholds、SSH/Telnet、Locate End Stations、View/Poll/Configure Traps、Backup Device、Upgrade Image、SAA Ethernet；VC 保存配置遇拓扑变化会警告并可产生 virtualchassisstatuschange trap。
## P161. Unified Profile 模板清单与平台差异 <<<PAGE 593-594>>>
Access Auth Profile（UNP 端口全属性）/WLAN Service/Access Role Profile/QoS/CP）/AAA Server Profile（仅 8.x 与无线，6.x/7.x 用 Global AAA）/Location+Period Policy/Access Classification/Customer Domain（数字 ID 再隔离）/SPB Profile/Far End IP/Static Service/VXLAN Profile/Tunnel Profile（L2 GRE Guest）/Legacy Wireless Profiles/Global Configuration；Captive Portal 不支持 OS6350。
## P162. Access Auth Profile 关键机制 <<<PAGE 594-601>>>
Port Bounce：COA 换 VLAN 后触发 DHCP 重新的手段（无线与 AOS 6x 恒开）；AP Mode 默认开（自动检测 Stellar AP），Secure 未勾时 AP 认证失败其客户端流量仍被信任；Trust Tag 默认关（隐式 VLAN 标签分类）；Bypass VLAN（AP1201H/1201HL AWOS4.0.2+、1301H/1311 4.0.5+）：直通交换芯片跳过 CPU，优先级高于 Trust Tag，配置后该 VLAN 不能应用认证/ACL/策略，推荐 HD IPTV 场景；Bypass Status/MAC Allow EAP 组合决定 802.1X 跳过逻辑（无线对应 l2-auth-fail-through 且须配 MAC Allow EAP 才生效）；Stellar AP Bypass=Enable 时先 MAC 后 802.1X，Disable 时仅 802.1X；分配端口类型 VLAN/SPB Access/VXLAN Access；UNP VLANs（静默设备如打印机，6.7.1.R02+/8.6R1+）；常见分配失败：链路聚合成员/tagged 口不能启 UNP/VLAN 不存在或非 Standard VLAN/Port-Template 与 L2 Profile 冲突；取消分配的正规流程是 Device Config 删除后重推剩余端口。
## P163. 无线转发四模式与 Band Steering <<<PAGE 598-599>>>
Tunnel（GRE 到控制器处理全部）/Bridge（AP 本地处理）/Split Tunnel（按目的分流）/Decrypt Tunnel（AP 解密后 802.3 入 GRE）；Drop Broadcast/Multicast 与 ARP 转 Unicast 仅限 Tunnel 模式（Bridge 模式控制器无法过滤本地流量）；Band Steering 三模式：Force-5GHz/Prefer-5GHz（默认）/Band Balancing；仅 Bridge/Split-Tunnel 的 AP 间不共享 5G 客户端信息；DMO 阈值 2-255 默认 5。
## P164. WLAN Service 角色分配优先级与 MLO <<<PAGE 602-603>>>
ESSID ≤32 字符（含空格加引号）；Hide SSID 几乎无安全价值；角色分配优先级：802.1X/MAC 认证返回角色 > Classification Rules（仅当认证未返回角色或返回角色未匹配时用）> Default Access Role Profile；Security Level: Open（默认）/Personal/Enterprise（802.1X）；MLO 频段取自 Allowed Band 且依赖 radio+EHT 开启；802.11r/OKC/L3 Roaming/FDB Update on Association 属漫游控制。
## P165. WLAN Service 无线参数默认值 <<<PAGE 603-606>>>
Max Clients Per Band 1-128 默认 64；最小客户端速率建议 2.4G=12、5G=24；Broadcast Key Rotation 1-1440 分钟默认 15；Broadcast Filter All（Stellar AP 专用，除 DHCP/ARP 全丢广播）；Broadcast Filter ARP=AP 做 ARP 代理（不响应 Gratuitous ARP）；Multicast Based Channel Utilization 0-100 默认 90；802.1p 映射（WMM 四类→上下行 802.1p，上行为单值下行可多值，Voice 上行 6/下行 6,7、Video 上 4/下 4,5、Best Effort 0/0,3、Background 1/1,2）；DSCP 映射同构（Voice 46/46,48,56、Video 40/24,36,40）。
## P166. Access Role Profile 关键规则 <<<PAGE 608-613>>>
每档案仅 1 个 Policy List（多档案可共用）；Redirect 开启后只能映射 VLAN；PolicyView Expert 策略只适用 AOS 设备且档案设备集须与策略设备集一致；带宽控制 0=不限，AOS 7.3.4 不支持，8.9R4 仅 OS6860/6865/6900；Client Session Logging 三级（HTTP/HTTPs、ALL、None 仅上下线）；WCF Profile 每档案 1 个；Walled Garden 社交登录自动配白名单域（FB/Google/Rainbow），自定义 Allowlist 须 FQDN（禁 IP/协议前缀）；Client Isolation Allowed Contacts 支持 5 种 MAC 格式+尾通配符（OUI 批量）；映射方法六选一（VLAN/SPB/VXLAN/Static Service/Tunnel/VLAN+Tunnel），Stellar AP VLAN 1-4094 或 untagged 否则忽略，支持 VLAN Pool（10-20,21,23 式）；Dynamic VLAN：6.7R08+ 可映射动态协议学到的 VLAN（须已存在），8.6R1+ 可映射任意 VLAN（交换机自动建 UNP Dynamic VLAN），前置 Global Configuration 开启动态创建；常见错误：VLAN 不存在/非 Standard VLAN。
## P167. AAA Server Profile 细节 <<<PAGE 614-618>>>
每类服务器（802.1X/CP/MAC × 认证/计费）可配主+二三四级备份（各须不同服务器）；无线：802.1X/MAC 主备生成认证服务器组，CP 主备被忽略；IAP 无独立 MAC 服务器（用 802.1X 主备）；无线计费仅 RADIUS（他类型报错）；高级设置无线忽略；Session Timeout 12000-86400 默认 43200；Inactivity 60-1200 默认 600（须大于交换机 MAC 老化时间否则不生效）；802.1X 重认证 600-7200 默认 3600；Accounting Interim 60-1200 默认 600；**所有超时参数修改不追溯已在线用户**（flush 或重新认证后生效）；NAS Port ID/NAS ID 默认取 chassis/slot/port 与系统名；各类 Delimiter/Case 定制 RADIUS 属性格式。
## P168. Access Classification 九种规则类型 <<<PAGE 621-623>>>
MAC（双平台；规则改动会 flush 已分类 MAC）/MAC Range（仅 AOS）/IP Address（仅 AOS）/VLAN Tag（Tag Position Inner/Outer 仅 7x）/Location（仅 Legacy AP，Stellar 不支持）/ESSID/DHCP Option（Signature ID）/DHCP Option 77（User Class）/Encryption Type；均可附 VLAN Tag 与 Customer Domain ID；分配映射 VLAN/SPB/VXLAN/Static Service 四选一（VLAN 须已存在，设备列表随映射过滤）；Extended Rule 端口选择可选（仅 UNP 口，From-To 连续端口或 Port Group）。
## P169. Customer Domain 语义 <<<PAGE 624>>>
数字 ID 把物理 UNP 口/链路聚合组成逻辑域；端口只应用同 Domain ID 的分类规则；默认全部端口与规则在 Domain 0。
## P170. SPB/VXLAN/Static Service/Tunnel Profile 映射机制 <<<PAGE 625-630>>>
SPB/VXLAN Profile：设备经认证/分类动态入档案时自动创建 SAP 转发流量（Tag 值 untagged 时封装值 0 如 1/12:0）；Static Service 只映射已静态存在的 Service ID（1-32767），交换机不动态建服务；VXLAN 含 VNID+Far End IP（VTEP 的 Loopback0 列表动态建 SDP）+组播 IP+Headend/Tandem/Hybrid 三种复制模式。Tunnel Profile：Tunnel ID 0-16777215（建议 64001-65000，0=不发 GRE Key）；Keepalive 2-5s 默认 5、Response Timeout 2s、Retries 3-5 默认 3、Preemption Countdown 默认 300s；MTU 建议 Raw GRE 1476 / GRE over wireguard 1416；TCPMSS 500-1460 默认 1250；Tunnel ID 与 Entropy 的四种合法组合（AOS 终结=非 0 ID+Entropy 开；非 AOS/OV VPN=0 ID+Entropy 关），"ID>0+Entropy 关"与"ID=0+Entropy 开"不支持；Local Breakout 每 tunnel 仅一个 VLAN；同 AP 多 SSID 静态路由会累积且目的子网不得重复、勿手写隧道 VLAN 对应子网路由（AP 自动建，手写致性能劣化）。
## P171. 802.1X/MAC 无线认证 Profile 默认值 <<<PAGE 631-633>>>
802.1X：Max Auth Failures 0-5 默认 0（0=不拉黑）；重认证默认关（定时器默认 24h）；Max Reauth 1-10 默认 3；Termination 支持 EAP-PEAP（内层 EAP-GTC/MSCHAPV2）或 EAP-TLS；Enforce Machine Authentication 时按机器/用户认证结果分别给 Default Machine/User Role（默认 guest）；802.1X 三角色：supplicant/authenticator（无线控制器，EAP 类型透传）/authentication server（RADIUS）。MAC：Max Auth Failures 0-10 默认 0；Delimiter Colon/Dash/None（默认无分隔）；Case 默认 Lower。
## P172. Global Configuration Setting 关键参数 <<<PAGE 634-635>>>
应用于所有未配 Access Auth Profile 的 UNP 口；Redirect Pause Timer 60-65535 默认 0（COA 换 VLAN 且无 port bounce 时过滤非 supplicant 流量等状态清理）；Auth Server Down Timeout 10-1000 默认 60（超时重试认证直到成功）；Redirect Port Bounce 默认 Enabled（无线恒 Enabled）；UNP Dynamic VLAN 开关（8.6R1+）与 Auto-Create Dynamic VLANs on Switch Reload（6.7R08+）；Auth Server Down Access Role Profile=RADIUS 不可达时的兜底角色。
## P173. UPAM RADIUS/ASA 用例矩阵 <<<PAGE 641-642>>>
支持：UPAM 库同时做 ASA+客户端认证（ASA 无需显式 Access Policy）；UPAM 做 ASA+外部 RADIUS 做客户端（UPAM 代理，802.1X/MAC 各需 Wired 网络类型策略）。**不支持**：外部 RADIUS 做 ASA + UPAM 做客户端；外部 RADIUS 同时做两者。交换机访问认证可按 Default/Telnet/SSH/HTTP/FTP/Console 分别指定服务器+Session Accounting。
## P174. DHCP Option 82（Stellar AP）与 Redirect Allowed <<<PAGE 643-644>>>
Option 82 支持 AWOS 3.0.6.x+，在 Access Role Profile 中启用；Circuit ID 子选项可组 SSID/AP Model/AP Name/AP MAC/AP Location/VLAN-ID/AP-Port/自定义；Remote ID=Client-MAC/AP Location/自定义；自定义串用 $ 前缀（如 "$$vlan-$ssid-$apmac"）。Redirect Allowed Profile 补充 UPAM/CPPM 重定向之外可达的子网白名单。
## P175. WLAN Service（Device Config 版）安全矩阵 <<<PAGE 649-655>>>
Security Level 四级：Open / Enhanced Open（OWE；Transition Mode 双 BSSID 兼容旧客户端，仅 AWOS 4.0.8+，旧版本重启后 SSID 退化为 open；6GHz 强制启用且不可关）/Enterprise（DYNAMIC_WEP~WPA3_AES256 六种加密；WPA3_AES256 不支持的 AP 自动回退 WPA2_AES，AP1101 全频段/AP1201H 2.4G 不支持）/Personal（STATIC_WEP~WPA3_PSK_SAE_AES 七种）；Backward Compatibility：6GHz SSID 的 2.4/5G 自动继承 WPA3_SAE_AES，开启后 2.4/5G 用混合模式 WPA3_PSK_SAE_AES（MLO 含 6GHz 时自动禁用）；PMF 三态 Disabled/Optional/Required；Hotspot 2.0 仅 Enterprise WPA2_AES/WPA3_AES256，Operator/Venue Name ≤252 字符、Domain ≤16 个、Roaming OI ≤16 个；Origin=SSIDs 的 WLAN Service 只能在 SSIDs 应用编辑/删除；Device Config 改动只影响所选设备不回写模板；Max Clients Per Band 此处 1-256 默认 64。
## P176. UPAM NAS Client 机制 <<<PAGE 682-684>>>
系统预置 "All Managed Devices" NAS（不可删）：OV 托管设备每 15 分钟自动入 UPAM NAS 库，共享密钥固定 "123456"，与 UPAMRadiusServer（Security-Authentication Servers 中创建）配套经 WLAN Service 下发；NAS IP 必须等于设备在 OV 中的管理 IP（多 IP 设备不符时手工建 NAS 段）；UPAM 作代理时 Shared Secret 必须四处一致：NAS Client+UPAM RADIUS+UPAM External RADIUS+第三方 RADIUS；DM/COA 消息用 User Name/Calling Station ID 定位会话。
## P177. Message-Authenticator 检查规则 <<<PAGE 685-687>>>
AP 请求恒带 Message-Authenticator；OmniSwitch 默认不带也不校验响应——须 CLI aaa radius message-authenticator（AOS 8.10R2+ 全局命令）开启；UPAM 侧开启 Require 检查会丢弃无该属性的请求（即丢弃 AOS 8.10R1 及以下的交换机请求）；混合网络建多个 NAS 段分别设置标志；TLS RADIUS 不支持该标志；新装默认 Enabled、从 4.9R1 升级默认 Disabled（改后保留）；强烈建议开启防 UDP RADIUS 响应伪造；AP 侧（AWOS ≥5.0.2）可用 AAA Server 的 Require 标志校验响应。Profile Polling：Unified Profile 轮询 10 分钟-24 小时默认 1 小时，单次最多 512 台 <<<PAGE 677>>>。
## P178. UPAM Access Policy/Authentication Strategy 模型 <<<PAGE 687-693>>>
Access Policy：Priority 1-99（1 最高），匹配多策略时最高优先生效；Basic 属性（认证类型/网络类型/SSID/NAS IP/Identifier/Port ID/Port Desc/设备名/位置/AP Group）+ Advanced 属性（Service Type 全集/EAP 类型限制/NAS Port Type/Alcatel 专有属性）；Strategy：认证源四选（None=仅 MAC+CP、Local DB、External LDAP/AD、External RADIUS）×Web 认证（None/Guest/Employee/两者）四推荐组合（None+Web=纯 CP、Local DB+None=MAC/802.1X、外部源+None=802.1X）；Employee Account 上绑定的 Access Role Profile/Policy List **优先于** Strategy 配置；其他属性 Session Timeout 12000-86400 默认 43200、Accounting Interim 60-1200 默认 600、WISPr 上下行带宽；Role Mapping 仅外部 LDAP/AD（Priority 1-99，Unmatched Action Accept/Reject）；Employee 账号支持 xls/csv/xlsx 批量导入（可下载模板）。
## P179. UPAM Company Property 与 Device Specific PSK <<<PAGE 697-702>>>
公司资产设备清单（MAC/名称/关联员工/类别/厂商/OS）；绑定设备的 ARP/Policy List 优先于 Strategy；Device Specific PSK：每台设备按 MAC 派发不同 PSK（须同时在 SSIDs/WLAN Service (Expert) 与设备上启用），可打印 PSK 或二维码；支持 xls/csv/xlsx 批量导入；Online Devices 可 Kick Off 强制下线；Acct-Terminate-Cause 码：1 User Request/4 Idle Timeout/6 Admin Reset/7 Admin Reboot/8 Port Error/9 NAS-Error；Framed MTU 固定 1400；Called Station ID：交换机=MAC，AP=radio_MAC:SSID；MAC 认证的 Accounting Start 通常不含客户端 IP。
## P180. Switch User Account (ASA) <<<PAGE 703-706>>>
权限三级 Read-Write（默认）/Read Only/Advanced（AOS 6 与 AOS 8 各有 BitMap Calculator 按域族定制，AOS 8 的 All 会忽略不支持项）；UPAM 本地库 ASA 默认禁用（默认走外部认证）；ASA 用例矩阵与 P173 相同（外部 RADIUS ASA+UPAM 客户端认证不支持）；ASA 工作流：建用户→AAA Profile（Unified Profile-Global Configuration-AAA）名填用户名、User's Access to Switches 设 UPAM 为各访问类型服务器→Apply to Devices 到交换机；Authentication Record 可 Generate 一键生成 PSK/Employee 账号/加入 Company Property。
## P181. Authentication Record 的 Generate 条件 <<<PAGE 710>>>
Generate→PSK：任意记录可生成（按 MAC+Session Time 派生口令并入 Company Property）；Generate→Employee Account 仅限 Result=Fail+Auth Resource=Local Database+Service Type=802.1X/Voice；Generate→Company Property 仅限 Fail+Local DB+Service Type=Call Check（MAC 认证）。Reject Reason 三类：Overdue license/无效用户名密码/无法匹配 Access Policy。
## P182. Guest 访问关键规则 <<<PAGE 714-718>>>
Guest Access Strategy 最多 32 条；认证资源恒为 Local Database（Guest 账号库）；Data Quota 仅对账密登录生效（Access Code/条款用户不限）；Custom Attributes ≤20 个（名 ≤32 字符、值 1-255 字符，Terms 登录时才可配，信息可在 Captive Portal Access Record 查看）；Remember Device 有效期默认 Days=30/Hours=24/Minutes=60；Social 登录需本地 DNS 把 Portal Server Domain 解析到 UPAM IP；自助注册审批可限定员工邮箱后缀或按位置路由 Guest Operator；Service Level=None 时用 Global Configuration 的注册策略；WiFi4EU 要求专用 Portal 模板且 CP 有效期 ≤24 小时。
## P183. Guest Account 机制 <<<PAGE 742-745>>>
两种账号：Account（账密）与 Access Code；Data Quota 默认 1MB（可经 Service Level 覆盖）；账号有效期不能超 Global Configuration 的上限（如全局 180 天则最多 180 天），批量创建有效期 1-365 天默认 90；Batch Creation 需在 Global Configuration 启用，前缀+递增编号，一次最多 5000 个账号；Create and Print / Print Tickets 打印登录凭据票；支持 xls/csv/xlsx 导入+模板；可为账号手工加 Remembered Device（MAC+类别/厂商/OS）；Sponsor Name 四种来源：Admin-*/EmployeeSponsor-*/GuestSponsor-*/SelfRegister-*；社交登录：Facebook/Google 需 OAuth Client ID+Authorized Origins 回填，Rainbow 需 Web 应用+Implicit Grant+Running 状态，WeChat 手机端用门店插件参数（shopId/appId/secretKey），PC 端须建网站应用且 Verified（付费）+回调域=Portal FQDN <<<PAGE 720-742>>>。
## P184. Guest 设备/自助注册/Guest Operator 补充规则 <<<PAGE 746-756>>>
Guest Account Deletion Policy：Never（默认）/Immediately/过期后 1-90 天；Access Code 账号支持 Extend 延期（仍受全局上限约束）；AP 移除/迁移后其客户端在 Guest Device 仍显示在线直到超时；Remembered Device 的 Active Status：只有曾实际登录（Activated）的设备消耗 Guest 许可（手工加的 Inactive 不占）；一台设备可被多个 Guest Access Strategy 记住；Remember Method=Static（手工）/Auto（CP 认证自动）；Self-Registration 状态 Unchecked/Approved/Rejected（结果邮件通知访客），审批人三类 Admin-/EmployeeSponsor-/GuestSponsor-；Guest Operator 按位置接收该站点的注册请求。
## P185. Guest Global Configuration 与 BYOD 差异 <<<PAGE 756-766>>>
Guest 全局：Batch Creation 默认前缀+Effective at First Login（默认关，即有效期从建号起算）+Access Code 长度 6-16 默认 6；账号有效期全局 1-365 天默认 90（账号页只能≤此值）；Device Validity 1-365 天默认 30；Max Device Per Account 1-500,000 默认 10；Service Level 每档绑定 ARP+Policy List+Data Quota+自己的有效期/删除策略/设备策略。BYOD：策略同样 ≤32 条含 Default；认证源四选（Local/External LDAP-AD/External RADIUS/On-Premise LDAP——后者认证直连 AP 与本地 LDAP 不经公网）；Expire 支持 Never Expire 或 1-365 默认 90（-1=永不过期）；Max Device Per Account 仅 1-10 默认 5；无自助注册/Access Code/Data Quota；BYOD Active 设备才消耗 BYOD 许可（同 Guest）；Guest Operator 登录用 OV 的 secondary IP 管理界面。
## P186. UPAM Settings 集成配置集 <<<PAGE 767-778>>>
Email：SMTP+SSL/TLS+认证开关，Send From 10-64 字符、密码 8-64；External Log Server：MySQL/MSSQL/Syslog 三种，UPAM 本地日志仅存 1 个月，外置可存历史（Test Connection 验证）；LDAP：Retries 1-3 默认 3、Timeout 1-30 默认 5、端口默认 389/TLS 636、TLS 三式 NS/LDAPS/StartTLS；AD 认证须将 AD 设为 DNS 服务器，字段含 Netbios/DNS 域名+DC FQDN；External RADIUS：共享密钥 4-64、1812/1813 端口、Require Message Authenticator 校验响应、UPAM-IP as NAS-IP Proxy（私网自动填 UPAM IP，公网手工指定）；LDAPS/RADIUS 证书默认密码 "password"，同时只能激活一张（激活新证书自动替换旧的），活动证书不可删（RADIUS 侧）；Additional Trust CA 内置 Built_in_CA 默认信任，自定义 CA 须手动 Trust 且使用时 AP Group 的 802.1x Supplicant 须指定同一证书文件；Captive Portal 页：6 种系统布局+EU WiFi 布局，自定义 Logo/Function 面板（透明度 1-10）/广告图/轮播/视频，页面自适应设备尺寸；RADIUS 服务器证书生成六步 openssl 流程（rootCA.key→rootCA.pem→radius_server.key→CSR→签名→激活）。
## P187. WCF 与 Users/User Groups 体系 <<<PAGE 780-789>>>
WCF：仅 AWOS 4.0.2.x+（AP1101/1201H/1201L/1201HL 除外）；需 WCF License 按数量购，AP Group 级开启即全组支持的 AP 各耗一个许可（可单 AP 关闭回退）；OV 须连云端 WCF 服务（状态 In/Not in Service，日志 brightcloud.log）；WCF Profile=条件(如 Malware/Gambling)×Accept/Reject 多条；编辑 Profile 后须重新启用 AP Group 的 WCF 才生效；被 ARP/SSID 引用的 Profile 不可删。RADIUS Attribute Dictionary：Vendor=IETF/Alcatel/Other，属性可标记用于 Access Policy/Enforcement Policy/RADIUS-DM，Sync to RADIUS 后服务器重启，标准属性不可删 <<<PAGE 779-780>>>。预置用户：admin(Account Admin，密码 switch，唯一能改用户/组)/netadmin(Network Admin)/writer(Write)/user(Read)，默认密码全部为 switch（至少要改密码）；User Role = 可访问地图×应用读写×VLAN/VXLAN 对象限制三维度，可多角色叠加（不同地图不同应用不同权限）；系统定义 Role 不可编辑/删除；2FA 用 Google Authenticator 六位时间码按 Role 启用。
## P188. Users 补充与 VLAN Manager 机制 <<<PAGE 790-808>>>
用户可属多组，权限取**最高特权组**；admin 用户不可删、Administrators/Default 组不可删、系统 Role 不可改；登录服务器仅 Local 或远程 RADIUS（RadSec 不支持作登录服务器），远程不可达时可从 Local 登录或 VA 菜单(选项7)改服务器；2FA 仅能全局启用/禁用（不能按 Role 差异化），用户启用/禁用会收通知邮件，2FA 状态 None/Setup/Verify，Verify 卡住用 Reset 2FA 重置；CPPM 登录需向其字典加 ALE Nms-Group/First/Name/Description 四属性。VLAN Manager：变更即时下发无 staging，出错不回滚已成功部分；表格显示值取**最低 IP 主机地址交换机**的数据，但修改会应用到所有含该 VLAN 的交换机；VLAN 1-4094（创建用 2-4094，1 为默认全端口 VLAN）；VLAN 无 active 端口则 oper inactive；Admin disable 保留端口分配但不转发；创建/编辑单次最多 200 台设备；VLAN Overwrite 开启会用新配置覆盖 OV 已发现的现有配置；Default/Q-Tagged Ports Template 按端口存在性套用到所选设备；Stellar AP 的 VLAN 只能经 Access Role Profile 映射创建（VLAN Manager 仅显示）。
## P189. VLAN/STP/IP Router 关键参数 <<<PAGE 810-817>>>
VLAN by Maps：地图内设备有 mobile port 生成的 LLDP 链路则不建 VLAN；删除 VLAN 单次 ≤200 台；VLAN ID 不可编辑，Copy 建 VLAN 走向导换新 ID。STP：协议 STP(默认)/RSTP/MSTP（MSTP 视图仅显示 Instance 0/VLAN 1）；Bridge Priority 0-65535 默认 32768（小者优先做根）；Max Age 6-40 默认 20；Port Priority 0-15 默认 7（同 cost 比低端口号）；Path Cost 0=按链路速率默认（0-65535）；模式 Flat（单实例全 VLAN）/1x1（每 VLAN 一实例，AOS 默认）；端口状态机 Disabled/Blocking/Listening/Learning/Forwarding；Manual Mode 可手工钉死 Blocking/Forwarding 脱离 STP 算法；Edge Port 收到 BPDU 会退化为 No Point to Point；端口级禁 STP 即转 forwarding。IP Router：接口 IP 须唯一；掩码默认按地址类；IP Forwarding 禁用则接口仅作主机；VRF 创建后不可改（接口 VRF 不可编辑，VRF 实例由 CLI/WebView 建）；VLAN 可路由条件=至少一个路由接口+一个 active 端口，否则该 VLAN 端口等效被防火墙隔离。
## P190. MVRP 与 IP Interface 细则 <<<PAGE 821-828>>>
MVRP：全局禁用即删除全部 MVRP 学到的动态 VLAN；仅 Flat STP 模式支持；Max VLAN Limit 32-4094 默认 256（调小于现有动态 VLAN 数须禁用再启用才生效）；Registrar Mode Normal/Fixed/Forbidden；Applicant Mode Participant/Non-Participant/Active（默认 Active）；Periodic Timer 默认 1s（勿乱改致 MVRP 失衡）；仅 fixed/802.1Q/aggregate/VLAN Stacking Network 口支持（镜像口、Stacking User 口不支持）；5x 设备不支持动态 VLAN。IP Interface：每 VLAN 接口数 OS6800/6850/9000 系 8 个，OS6860/6900/9900/10K 系 16 个；Device Type 可绑 VLAN/EMP/Loopback/GRE 隧道（GRE 仅 OS10K）/IPIP；Interface Name/Device Type/VRF 建后不可编辑；Local Proxy ARP 开启后 VLAN 内流量改路由不走桥接；Primary Interface 默认第一个绑定者；5x 动态 VLAN 不支持。
## P191. VM Manager 机制 <<<PAGE 830-840>>>
混合 vCenter（最多 2 个，URL 需 /sdk 后缀）+Hyper-V，总 VM 上限 5000；OV 自身跑 VM 时 VM 迁移可能丢 UDP（SNMP）流量；所有 Hypervisor 系统时间必须与 OV 同步；Hypervisor 连接口或其本身须关闭链路发现协议（部分 Hypervisor 发 LLDP 会被当成桥设备）；流量塑形模型：VM 打 VLAN Tag→交换机 UNP Tag 规则把 VM VLAN 映射到 UNP+VLAN→每 VM VLAN 一个 UNP+一条 VLAN Tag 分类规则→VM 跨 Host 迁移免改配置；管理网络（vMotion/NFS）建议独立物理口+独立 UNP 规则；VM Server 建后仅密码可编辑；Live Search 查实时位置，历史搜索会有 false positive（旧 uplink 信息持久，用 Locator timestamp 判断）；连 Host 的交换机应加入 VMM Devices List 保证 Locator 数据最新。
## P192. VM VLAN 配置与 One-Touch SPB <<<PAGE 841-847>>>
Exclude VLAN 让 OV 轮询忽略指定 VM VLAN（如管理 VLAN）；SPB 仅 OS10K/6900 AOS 7.3.1.R01+ 且需 Advanced License（非 SPB 设备自动跳过 SPB 属性仅更新桥接 UNP）；VLAN Notification：Active/Ignored 两列（已知可用替代配置可 Ignore），Resolve 向导自动修复缺失 Tag 规则；Resolve 自动生成规则：UNP Profile 名 "UNP XX"（XX=VLAN ID，默认 UNP1=VLAN1）；SPB Profile 的 ISID=Starting ISID+VM VLAN ID（可改起始值建独立 L2 域），BVLAN 4 个轮转分配+各自 ECT ID；自动生成的 Profile Policy List 留空（仅保连通，后续手工补）；SPB 自动生成依赖 One-Touch SPB 首配参数未被改动（改过须重新执行）；同 Hypervisor 网络不同 ISID 的 VM 互不通信。VM Polling 间隔建议与 Discovery Regular Updates 一致。
## P193. VXLAN 核心机制 <<<PAGE 848-852>>>
仅 OS6900-Q32/X72 支持；VXLAN=L2 over UDP/IP 封装（24 位 VNI，1600 万段，段间 MAC 可重），借 ECMP 提升利用率；VXLAN Service=VFI（SAP 侧学客户 MAC+SDP 侧学网络 MAC）；VNID 置 0 自动生成；删除 Service 须先禁用 Service 及关联 SAP/SDP；Default Network Profile 不可改删；SDP 隧道须设备有 Loopback0（可跳转 VLANs 应用创建）；Unicast 隧道方向 Bidirectional（两端建 SDP）/Unidirectional；Multicast 隧道要求全部节点入同一 PIM 组（设备缺 PIM Sparse+Bidir 会警告，可一键套默认 PIM 配置）；Reapply 仅中间步骤失败可用（远端或首步失败则设备被移出且不可 Reapply）；SAP 每端口最多 8 个，Trusted 默认 True（信任 tagged 优先级，False 则用固定 Priority 0-7）。
## P194. VM Snooping 参数 <<<PAGE 855-860>>>
识别 VXLAN 封装包并入库；Policy Mode Basic（UDP 端口+VNI+内层源 MAC+IPv4）/Advanced（加 IP 协议+L4 端口，IPv6 用内层 IPv6+L4）；Policy Resource Default/Extended（策略数翻倍）；Inner Header Tagged/Untagged/默认（Basic=两者，Advanced=tagged）；Aging 0-86400 默认 300（0=永不老化）；Trap Threshold 60-90 默认 80%；UDP 目的端口默认 4789，可加最多 7 个附加端口（多端口降低速度且勿用 IANA 保留口）；统计经 FTP/SFTP 收集（设备须配 CLI/FTP 凭据，Prefer SSH 则走 SFTP）；VSnoop Purge Scheduler 默认每 15 分钟采集；统计查询行数 500-5000 默认 1000，Custom Template ≤2 个。
## P195. SSIDs 应用一步式配置模型 <<<PAGE 861-863>>>
创建 SSID 时自动派生并联动创建 Access Role Profile/Access Policy/Authentication Strategy/Guest Access Strategy/BYOD Access Strategy/AAA Server Profile/Tunnel Profile/Global Configuration（以 SSID 派生名命名）；SSID Service Name 与 SSID 分离（多服务共用一个 SSID 名）；五种 Usage 预设：Guest Network(Open/CP)、Employee BYOD、Enterprise 802.1X、Protected Network(PSK+可选 CP)、Protected Network for Employees(PSK+BYOD Portal)；CP 二选 OV-UPAM / External；SSID ≤31 字符；一屏最多显示 15 个 SSID（可自定义顺序）；**Usage 与 Authentication Strategy 不匹配的 SSID 不能编辑**（如 Guest CP 用途却配了 Local DB+无 Web 认证）；SSID 也可在 WLAN Service (Expert) 配置，WLAN Name/WLAN Service Name 即 SSID Service Name。
## P196. SSID 定制补充规则 <<<PAGE 864-874>>>
Allowed Band 增加 6GHz 选项（Enhanced Open 6GHz 强制开启且不可关；Transition Mode 需 AWOS 4.0.8+，旧版重启后 SSID 退化为 open）；WPA3_AES256 不支持机型自动回退 WPA2_AES（AP1101 全频段、AP1201H/1201L 2.4G 不支持；AP1101/1201H/1201L 完全不支持 WPA3）；AUTO_WPA_WPA2 混合模式两谱系均可用；Device Specific PSK 仅配 UPAM RADIUS：Prefer（无 AES-CBC-128 属性时用 SSID 配置的 key）/Force（恒用 AAA 返回值，此模式隐藏 Private Group PSK 配置）；**Private Group PSK (PPSK)**：按不同口令分组建组入不同 Access Role Profile，每 SSID ≤16 条 Entry，单 AP 全部 SSID 合计 ≤64 条，Entry 名与口令均不可重复；TLS RADIUS：选 TLS 服务器的 SSID 生成 AAA 仅含 802.1X 主服务器；TLS 服务器不支持 CP/MAC 认证，事后把 TLS-disabled 服务器改开 TLS 会失败；自动生成的 AAA Profile 与 SSID 同名——要换 RADIUS 应改 SSID 而非直接改该 Profile；Stellar AP VLAN 池按机型限 WLAN 数：AP1301H=2、AP1311/1301/1431/1411=4、AP1320/1331/1351/1451=7（各 256 VLAN/WLAN）；WCF 首访放行陷阱：AP 对首次访问的 URL 先放行再判定，受限于 DNS 缓存过期后首个访客不受过滤。

<!-- APPEND -->
