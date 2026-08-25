# principles 候选提取 · OmniVista 2500 NMS 4.9R2 User Guide

来源: source/fulltext.md（页码为原文 <<<PAGE N>>> 标记）

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
