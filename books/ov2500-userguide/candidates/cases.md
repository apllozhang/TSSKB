# cases 候选提取 · OmniVista 2500 NMS 4.9R2 User Guide

来源: source/fulltext.md（页码为原文 <<<PAGE N>>> 标记）

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
