# GLOSSARY — OmniVista 2500 NMS 4.9R2 User Guide 核心术语

从 verified 术语库精选约 140 条，按主题分组。界面/产品名保留英文，页码为原书页码。

## 平台与控制台

- **NMS (Network Management System)**：网管系统，此处指 OmniVista 2500（<<<PAGE 1>>>）
- **LAN+WLAN Menu / WLAN Menu**：两种应用菜单视图，后者仅重组入口为 WLAN 专用分组，内容相同（<<<PAGE 31, 33>>>）
- **Dashboard / Widget**：主页仪表盘及其应用小部件，可增删/拖拽/配置刷新率（最小与默认 5 分钟）（<<<PAGE 37, 45, 50>>>）
- **Unacknowledged Alarm Display**：所有页面底部实时显示的未确认告警分类计数（<<<PAGE 31>>>）
- **Favorites Widget**：应用快捷方式收藏部件，加入后同步出现在主导航 Favorites 标签（<<<PAGE 36>>>）
- **Table View / List View**：表格/列表两种显示模式；List View 不可打印/导出（<<<PAGE 37-39>>>）
- **Watchdog**：OV 内部服务状态监控与启停（<<<PAGE 249>>>）
- **Scheduler Jobs（System/User-Defined）**：系统自动任务（不可改）/用户任务；Overlap/Crash 策略（<<<PAGE 250-251>>>）
- **User Role**：可访问地图×应用读写×VLAN/VXLAN 对象限制三维度的权限模型，可多角色叠加（<<<PAGE 780-808>>>）
- **2FA / TOTP**：Google Authenticator 六位时间码双因素认证（<<<PAGE 780-808>>>）
- **Fleet Supervision / OV ID**：设备生命周期云服务 / OV 实例标识；每 2 周上传库存（<<<PAGE 421-424>>>）
- **Inactivity Timeout**：无操作登出计时，默认 15 分钟（<<<PAGE 419>>>）

## 发现与拓扑

- **Discovery Range / Discovery Profile**：IP 范围与发现参数集（SNMP/凭据/Shell），多档案按序回退（<<<PAGE 255-256>>>）
- **Write Community Name**：SNMP 写团体名，发现后默认 public；只能交换机本端配（<<<PAGE 42>>>）
- **certified / working / running**：AOS flash 已认证目录 / 待测试目录 / RAM 运行配置（重启即丢）（<<<PAGE 43>>>）
- **Changes (Certified/Uncertified/Unsaved)**：交换机配置保存状态三值（<<<PAGE 273>>>）
- **Shell Preference**：设备默认 CLI（SSH/Telnet），SSH 时 Resource Manager 用 SFTP（<<<PAGE 260>>>）
- **Get Bulk / Max Repetitions**：SNMPv2 大表批量读取及每次行数（<<<PAGE 260>>>）
- **Full/Occasional/Regular/Frequent Updates**：四级自动发现轮询，内容逐级递增（<<<PAGE 297-298>>>）
- **Manual Link**：手工创建的持久链路，断链红色显示（<<<PAGE 290>>>）
- **Scheduled Upgrade / Time Window / Recurrence**：定时升级计划；窗口耗尽未升级设备等下次递归（<<<PAGE 292-293>>>）
- **NaaS / CAPEX / Grace Period / Degraded Mode**：订阅式许可模式 / 过期 30 天宽限 / 降级（禁改配置禁升级）（<<<PAGE 283-285>>>）
- **Mibset / Import MIBs**：第三方设备 MIB 集目录与其导入（<<<PAGE 287-288>>>）
- **REST API Polling**：以 REST 替代 SNMP 轮询，AOS 8.7R3+（<<<PAGE 299>>>）
- **IP Failover**：主 IP 失败后 OV 改用设备备用 IP（<<<PAGE 299>>>）
- **Geo Map / Topology Map**：地理图（默认视图）/传统拓扑图（<<<PAGE 554, 556>>>）
- **Physical Network Map / Child Map / Logical Map / Dynamic Map**：自动全网图 / 子图 / 无父图逻辑图 / 过滤器驱动图（<<<PAGE 554, 558, 580-581>>>）
- **Geo Map Site / Sub-Site**：地理位置站点及 Building/Floor 子图；设备仅属一站（<<<PAGE 575-576>>>）
- **Highlight Panel / Map Cluster**：按状态过滤高亮面板 / 缩放聚簇（<<<PAGE 560-564>>>）
- **SPB / ISID / SAP / SDP / BVLAN / SPT / RPL**：最短路径桥接体系及其构件（<<<PAGE 297, 524-527, 565-573>>>）
- **Locate / Browse；Historical / Live Search**：按终端找端口/按端口列终端；历史库/实时（Live=最近 5 分钟活跃）（<<<PAGE 336-339>>>）
- **ARP / Netforward Results Table**：IP-MAC 历史表 / 桥转发表定位结果表（<<<PAGE 338>>>）
- **Network Advisor / Application UUID**：云异常检测实例及其标识（<<<PAGE 264-266>>>）

## Analytics 与报表

- **Analytics Profile**：定义监控的交换机/端口与信息类型，Top N 报表前置（<<<PAGE 66>>>）
- **sFlow**：流采样协议，Top N Apps/Clients 数据来源，端口 6343（<<<PAGE 67, 134>>>）
- **EMP Port**：交换机管理口，sFlow 不能经其发送（<<<PAGE 75>>>）
- **Summary / Detail / Trending View**：报表汇总/明细/趋势三级视图；下钻粒度月→周→日→时→15 分钟（<<<PAGE 68-74>>>）
- **Collection Profile / View Profile**：统计采集档案（设备+属性+轮询 5min+保留 30d）/查看档案（≤50 计数器）（<<<PAGE 120-124>>>）
- **Counter / Scale**：图表一条统计线；Scale 绘图乘数 0.001-1000（<<<PAGE 123>>>）
- **Z-Score / Anomaly**：端口利用率异常检测统计量；最少需 11 天数据（<<<PAGE 133-134>>>）
- **Applications Management（Range-Based/Enumerated）**：端口↔应用映射两种模式（<<<PAGE 132-133>>>）
- **Report Configuration / Add to Report / Purging Policy**：两步报表模型与过期清理（<<<PAGE 484-485>>>）

## 无线（AP Registration / SSIDs / WLAN）

- **Stellar AP (OAW)**：ALE OmniAccess Stellar 无线接入点系列（<<<PAGE 137>>>）
- **Managed / Unmanaged AP**：已信任+已授权 / 未信任或冲突滞留的 AP（<<<PAGE 142>>>）
- **AP Group**：AP 管理单位（≤512 AP），配置按组下发，AP 仅属一组（<<<PAGE 137, 139, 165>>>）
- **DHCP Option 43 / Option 138**：AP 定位 OV 的 DHCP 选项（<<<PAGE 140, 142>>>）
- **Country Code Conflict**：国家码不一致导致 AP 无法纳管（<<<PAGE 143>>>）
- **Remote AP (RAP)**：经 VPN+OmniVista Cirrus 由本地 OV 管理的远端 AP（<<<PAGE 142, 160>>>）
- **Use Private Config**：单 AP 覆盖 AP Group 配置的开关（<<<PAGE 147>>>）
- **Mesh / MLO**：无线网状回传 / Wi-Fi 7 多链路操作（仅 Wi-Fi 7 机型）（<<<PAGE 150>>>）
- **Extended SSID Scale**：AP Group 扩展到 14 SSID 的开关（<<<PAGE 166>>>）
- **WCF (Web Content Filtering)**：按安全/内容类别的网页过滤（<<<PAGE 151, 171>>>）
- **RadSec**：RADIUS over TLS；Stellar AP 仅支持单个 RadSec 服务器（<<<PAGE 168, 225>>>）
- **QoE Events**：AP 上报 Cirrus 的高级分析事件（12 类）（<<<PAGE 193>>>）
- **Data VPN Server**：Remote AP 用户流量隧道端点（<<<PAGE 195-196>>>）
- **SSIDs 一步式模型 / 五种 Usage**：创建 SSID 自动派生八个配置对象；Usage 预设 Guest/BYOD/802.1X/PSK/PSK+BYOD（<<<PAGE 861-863>>>）
- **Enhanced Open (OWE) / Transition Mode**：机会无线加密；双 BSSID 兼容模式需 AWOS 4.0.8+（<<<PAGE 649-655, 864-874>>>）
- **PPSK (Private Group PSK)**：按口令分组建组入不同 Access Role Profile（<<<PAGE 864-874>>>）
- **Device Specific PSK**：每台设备按 MAC 派发不同 PSK，仅配 UPAM RADIUS（<<<PAGE 697-702, 864-874>>>）
- **Band Steering (Force/Prefer/Band Balancing)**：5G 引导三模式（<<<PAGE 599>>>）
- **Forward Mode (Tunnel/Bridge/Split/Decrypt Tunnel)**：无线转发四模式（<<<PAGE 598>>>）
- **802.11r / OKC / L3 Roaming**：快速 BSS 切换 / PMK 缓存漫游 / 跨子网漫游（<<<PAGE 603>>>）
- **Zigbee / BLE Beaconing / LQI / PAN ID**：AP IoT 射频体系；LQI>30% 可靠（<<<PAGE 148-149, 316>>>）
- **WiFi RTLS / Advanced Analytics Server Profile**：定位/高级分析上报目标（<<<PAGE 171, 191-194>>>）

## 接入认证（Unified Access / UPAM）

- **Unified Access（三途径）**：Workflow / Template / Device Config + Profile Polling（<<<PAGE 590-592>>>）
- **UNP (User Network Profile) / Access Role Profile**：接入角色档案（Policy List+CP 等属性）（<<<PAGE 590, 593>>>）
- **Access Auth Profile**：UNP 边缘端口认证配置模板（802.1X/MAC/分类/AAA/默认角色）（<<<PAGE 593-594>>>）
- **L2/L3 Authentication & Classification**：L2 定初始 UNP+VLAN（不再变）/L3 动态改策略（<<<PAGE 591>>>）
- **Access Classification Rules（九种）**：MAC/MAC Range/IP/VLAN Tag/Location/ESSID/DHCP Option/Option 77/Encryption（<<<PAGE 621-623>>>）
- **Port Bounce / COA**：COA 换 VLAN 后端口重启触发 DHCP 重新（<<<PAGE 595>>>）
- **Trust Tag / Bypass VLAN**：信任 VLAN 标签分类 / 芯片直通 VLAN（优先于 Trust Tag）（<<<PAGE 595-596>>>）
- **WLAN Service Profile**：SSID 服务模板（Basic/Security/MLO/Advanced/QoS）（<<<PAGE 601-602>>>）
- **AAA Server Profile**：主+多级备份认证服务器模板；超时参数不追溯在线用户（<<<PAGE 614-618>>>）
- **Customer Domain**：数字 ID 的附加流量隔离域（<<<PAGE 624>>>）
- **Tunnel Profile**：L2 GRE 隧道配置（Keepalive/MTU 1476）（<<<PAGE 625-630>>>）
- **Captive Portal（三层）**：全局 Configuration → Profile → Domain Policy（realm 替换）（<<<PAGE 232-235>>>）
- **Realm (Suffix/Prefix)**：用户名中的登录域标识（<<<PAGE 234>>>）
- **UPAM**：内置 Captive Portal + RADIUS 服务器（<<<PAGE 678>>>）
- **NAS Client / All Managed Devices NAS**：UPAM 的 RADIUS 客户端；预置 NAS 密钥固定 123456（<<<PAGE 682-684>>>）
- **Access Policy / Authentication Strategy**：优先级匹配策略 / 认证源×Web 认证组合（<<<PAGE 687-693>>>）
- **Guest Access Strategy / Self-Registration**：访客策略（≤32 条）/自助注册（Sponsor 审批）（<<<PAGE 712-718, 746-756>>>）
- **BYOD Access Strategy**：自带设备策略（≤32 条；无自助注册/Access Code/Data Quota）（<<<PAGE 756-766>>>）
- **Guest Account / Access Code**：账密访客账号 / 纯口令账号（批量 ≤5000）（<<<PAGE 742-745>>>）
- **Remember Device / Remembered Device**：设备记住机制；仅 Activated 状态消耗许可（<<<PAGE 714-718, 746-756>>>）
- **Switch User Account (ASA)**：经 UPAM 认证的交换机管理账号（<<<PAGE 703-706>>>）
- **Authentication Record / Generate**：认证记录；可一键生成 PSK/Employee 账号/入 Company Property（<<<PAGE 710>>>）
- **Company Property**：公司资产设备清单，绑定 ARP 优先于 Strategy（<<<PAGE 697-702>>>）
- **WiFi4EU**：欧盟公共 Wi-Fi 模板；CP 有效期 ≤24h（<<<PAGE 712-718>>>）
- **Message-Authenticator**：RADIUS 抗伪造属性；UPAM 开 Require 会丢弃无该属性的请求（<<<PAGE 685-687>>>）

## 策略与隔离

- **PolicyView / QoS Policy / Unified Policy**：条件+动作的 QoS 策略体系（存内置 LDAP，Notify-拉取）（<<<PAGE 384, 387-388>>>）
- **One Touch Policy (Data/ACL/Voice)**：简化策略；自动成对生成（OneTouchDR/AR 前缀）（<<<PAGE 385, 404-409>>>）
- **Precedence（30001-65535 分区）**：策略优先级；外部工具勿占用该域（<<<PAGE 387>>>）
- **TCM (Tri-Color Marking)**：三色标记限速（CIR/PIR），无线不支持（<<<PAGE 394-395>>>）
- **QoS 等级映射**：Platinum=7 / Gold=5 / Silver=3 / Bronze=1（<<<PAGE 394>>>）
- **Validity Period**：策略生效时间窗（WorkingDay=周一至五 9-17）（<<<PAGE 395-396>>>）
- **Default Policy List / Notify All / Re-cache**：默认策略表 / 通知刷新（代价高，批量）（<<<PAGE 396-410>>>）
- **Quarantine Manager (QM)**：基于 IPS/Syslog/trap 的终端隔离系统（<<<PAGE 457>>>）
- **Candidates / Banned / Never Banned / Disabled Ports**：四个处置列表（<<<PAGE 458>>>）
- **Client Blocklist**：Stellar AP 无线违规客户端的替代封禁路径（365 天）（<<<PAGE 460>>>）
- **Trigger / Extraction Expression**：隔离规则触发正则/源地址抽取正则（<<<PAGE 468>>>）
- **QMR (Quarantine Manager Remediation)**：交换机侧补救应用，隔离客户端仅可访 Remediation Server（<<<PAGE 459, 473>>>）
- **Quarantined VLAN / MAC Group**：隔离基础设施三件套之二（<<<PAGE 473-474>>>）
- **Fast Re-Cache / TAD**：只刷隔离 MAC 组的机制 / 流量异常检测（OS6850/6855/9700）（<<<PAGE 462, 478>>>）

## 资源管理与自动化

- **Backup 三类型（Full/Configuration Only/Images Only）**：镜像只记版本号，Restore 须先导镜像（<<<PAGE 489-490>>>）
- **Upgrade Image Repository / File Set / LSM**：镜像仓库/升级文件集/描述文件（<<<PAGE 487, 496>>>）
- **BMF / U-Boot (Denverton/Rangeley) / ISSU**：底固件/双 CPU 型号 U-Boot/不中断升级（<<<PAGE 497-500>>>）
- **Auto Configuration / Instruction File (.alu) / Option 60/66/67**：DHCP+TFTP+FTP 三方自动开通（<<<PAGE 502-506>>>）
- **Backup Retention (Minimum Backups / Maximum Days)**：保留 max(b,n) 算法（<<<PAGE 510>>>）
- **Provisioning Rule / Cloud Agent / Call-Home**：按序列号/MAC/型号匹配的零接触部署（每 5 分钟联系 OV）（<<<PAGE 430, 434>>>）
- **as-lite.myovcloud.net / Option 43 Sub128/134**：本地 Activation Server FQDN 与端口（<<<PAGE 432>>>）
- **Golden Configuration / Force Provision**：基准配置回推 / 下次 Call-Home 强制重推（<<<PAGE 431, 434, 448-452>>>）
- **Thin Switch Client / Incremental Template**：瘦交换机模式（write memory 失效）/增量模板（<<<PAGE 436-437>>>）
- **SAA / MACSAA / RTT-Jitter-Packet Loss Threshold**：服务质量探针体系（仅 MACSAA；默认阈值 100/100/5）（<<<PAGE 512-514>>>）

## 脚本与集成

- **CLI Script File / Shared Admin Script (shadmin)**：CLI+JS 混编 .script /管理员共享前缀（<<<PAGE 238-239>>>）
- **内置变量（$IP_ADDRESS/$BASE_MAC 等）**：发送时自动替换的设备属性变量（<<<PAGE 242-243>>>）
- **expectPrompt / lastcmd / <tapps> 指令**：训练确认提示/防挂起/四脚本指令（<<<PAGE 241-244>>>）
- **Trap / Severity 五级 / Acknowledge-Clear**：Normal~Critical 五级告警；确认/清除（<<<PAGE 368-374>>>）
- **Trap Responder / Trap Variables（$Details$ 等）**：按 Agent+Trap Type 触发邮件/脚本/转发/确认（<<<PAGE 371-376>>>）
- **Trap Replay Polling / Trap Absorption**：补拉丢失 trap（按 upTime 回算）/相似 trap 吸并（<<<PAGE 368, 379>>>）
- **Audit / Log Central (ngnms.log)**：日志分类视图与单文件汇总（<<<PAGE 212-214>>>）

## VLAN / 组播 / 虚拟化 Fabric

- **VLAN Manager**：变更即时下发无 staging；表格显示取最低 IP 主机地址交换机数据（<<<PAGE 790-808>>>）
- **STP (STP/RSTP/MSTP) / Bridge Priority / Edge Port**：生成树体系；Bridge Priority 默认 32768（<<<PAGE 810-817>>>）
- **MVRP**：动态 VLAN 注册；Max VLAN Limit 默认 256（<<<PAGE 821-828>>>）
- **PIM / RP / BSR / C-RP / C-BSR**：组播路由体系；每域一个 BSR（<<<PAGE 324-327>>>）
- **mDNS（Gateway/Responder/Legacy）**：零配置服务发现三模式；默认 restrict all（<<<PAGE 350-352>>>）
- **VM Manager**：混合 vCenter(≤2)+Hyper-V 纳管，VM 上限 5000（<<<PAGE 830-840>>>）
- **Exclude VLAN / VLAN Notification Resolve**：OV 轮询忽略指定 VM VLAN / 自动修复缺失 Tag 规则（<<<PAGE 841-847>>>）
- **One-Touch SPB**：自动生成 UNP/SPB Profile（ISID=起始+VM VLAN ID，BVLAN 4 轮转）（<<<PAGE 841-847>>>）
- **VXLAN / VFI / VNID / VTEP**：L2 over UDP 封装（24 位 VNI）/虚拟转发实例；仅 OS6900-Q32/X72（<<<PAGE 848-852>>>）
- **VM Snooping（Basic/Advanced）**：识别 VXLAN 封装包入库；UDP 4789、Aging 300s（<<<PAGE 855-860>>>）

## 许可

- **Device License / Service License**：按设备数 /按服务（VM、Guest、On-Boarding、HA）（<<<PAGE 329-330>>>）
- **Starter Pack / Evaluation / Production**：免费 30 设备入门包 / 60 天评估 / 正式许可（<<<PAGE 332-333>>>）
- **Activate Add-On**：加购许可激活按钮，不点则旧许可到期自动生效（<<<PAGE 330>>>）
