# DIGEST — OmniVista 2500 NMS 4.9R2 User Guide 精华

本书是 ALE OmniVista 2500 网管平台的 935 页 GUI 参考手册（38 个功能章，按菜单 A-Z 组织），技术栈为 OV2500 4.9R2 + OmniSwitch AOS 6.x-8.x + Stellar AP (AWOS)。它没有叙事结构，是"某功能在哪配、怎么配、默认值是什么"的查询底座：先用功能地图定位应用，再按技能单元的 Profile/向导流程操作。以下按十个技能单元摘要，页码均指原书。

## 一、知识地图（十技能单元）

1. **控制台与仪表盘**（ov-console-basics-dashboard）：菜单两视图、Dashboard 四标签、Widget/Favorites/过滤器、用户与 2FA（p31-64）。
2. **Analytics 与报表**（ov-analytics-reports）：Profile 驱动报表、sFlow、Statistics 采集/查看、AppVis 签名、定时报表（p64-136、201-211、484-486）。
3. **发现与拓扑**（ov-discovery-topology-views）：Range+Profile 发现、四级轮询、三层地图+Geo 站点、手工链路、Locator（p40-44、255-301、336-349、554-587）。
4. **Resource Manager 运维**（ov-resource-manager-ops）：备份三类型、镜像升级、Auto Configuration、零接触 Provisioning/Thin Switch、SAA（p429-456、487-521）。
5. **CLI Scripting 与 MIB**（ov-cli-scripting-mib）：CLI+JS 混编、内置变量/expectPrompt/tapps、第三方 MIB 导入（p238-248、285-288）。
6. **Unified Access**（ov-unified-access-profiles）：Workflow/Template/Device Config 三途径、Access Auth/Role/WLAN Service Profile、L2/L3 分层（p590-655）。
7. **UPAM 与 Guest/BYOD**（ov-upam-guest-byod）：内置 CP+RADIUS、三种认证工作流、Guest/BYOD 策略体系、社交登录、WiFi4EU（p678-778）。
8. **SSIDs 与 WLAN 高级**（ov-wlan-ssid-advanced）：一步式创建、五种 Usage、WPA3/6GHz/PPSK/Device Specific PSK、VLAN 池限制（p601-655、861-874）。
9. **Quarantine 与 PolicyView**（ov-quarantine-policyview）：IPS 事件流/Candidates/Banned 状态机、QMR 三件套、QoS 策略 Notify 机制（p384-412、457-479）。
10. **VM/VXLAN Fabric**（ov-vm-vxlan-fabric）：vCenter/Hyper-V 纳管、VM VLAN 塑形、One-Touch SPB、VXLAN 核心、VM Snooping（p830-860）。

## 二、十单元要点串讲

### 1. 控制台：先拿功能地图再干活
Network / Configuration / Unified Access / Security / Administration / UPAM / WLAN 七大菜单区是全书总目录（<<<PAGE 31-32>>>）；WLAN Menu 视图仅重组入口、内容相同（<<<PAGE 33>>>）。Dashboard 分 Global/WLAN Advanced/IoT/Performance Monitoring 四标签，Performance Monitoring 挂 Analytics Chart View Profile（≤20 widget）（<<<PAGE 45, 54-56>>>）。所有页面底部有 Unacknowledged Alarm 实时告警栏。权限三维度（地图×应用读写×VLAN 对象）多角色叠加，预置 admin/netadmin/writer/user 四账号默认密码全部 switch（<<<PAGE 780-789>>>）。

### 2. Analytics：Profile 驱动 + sFlow 数据面
Top N Apps/Clients/Ports 报表必须先建 Analytics Profile；Availability/Alarms/Health/SIP 免 Profile（<<<PAGE 66-67>>>）。建 Profile 时 OV 自动成为 sFlow Receiver，应用识别靠 TCP/UDP 端口（<<<PAGE 67, 74>>>）。统计采集与查看解耦（Collection Profile + View Profile ≤50 计数器）（<<<PAGE 117, 120-124>>>）。三大静默坑：SNMP 源 IP 与发现 IP 不一致收不到数据（<<<PAGE 119>>>）、删 Profile 连带删全部历史（<<<PAGE 121, 129>>>）、外部 RADIUS 用户不能排程报表（<<<PAGE 64>>>）。AppVis 是三步法（签名文件→Signature Profile→应用），一机一档且会清掉 CLI 配置（<<<PAGE 202-209>>>）。

### 3. 发现与拓扑：Range×Profile + 四级轮询
首次纳管五步法（发现→修正凭据→配 trap→保存→QoS 后再保存）是全书最常被引用的流程（<<<PAGE 40-44>>>）。多 Discovery Profile 按序回退，重新发现不覆盖已录入参数（<<<PAGE 256>>>）。四级轮询 Full⊇Occasional⊇Regular⊇Frequent，间隔随网络规模分档（<<<PAGE 298-299>>>）。拓扑三层地图：Physical（自动不可删）→Child→Logical，加 Dynamic（过滤器）；Geo Map 是默认视图，Site 自动生成同名逻辑图（<<<PAGE 554-581, 575-578>>>）。手工链路持久显示、断链变红，适合核心监控（<<<PAGE 290>>>）。Locator 一切搜索归结为 MAC，Live=最近 5 分钟（<<<PAGE 336-339>>>）。

### 4. Resource Manager：备份只记版本号，升级防 FTP 超时
Backup 三类型（Full/Config Only/Images Only），镜像不物理备份只记录版本——Restore 前必须先导镜像进 Repository（<<<PAGE 489-490>>>）。备份文件含源机器 IP/MAC 二进制信息，严禁拷给其他机器（<<<PAGE 493>>>）。升级铁律：先 Image 后 U-Boot；FTP 默认 5 分钟超时，大文件先 `session ftp timeout` 调大（<<<PAGE 497>>>）。Provisioning 是 DHCP Option 43+Cloud Agent Call-Home+SSH 推模板的零接触链路（<<<PAGE 430-436>>>）；Thin Switch write memory 失效、属性不可改（<<<PAGE 436-438>>>）。SAA 仅 MACSAA，建议 ≤50 个（<<<PAGE 512-514>>>）。

### 5. CLI Scripting：混编脚本 + 训练技巧
.script 文件 CLI+JS 混编；内置变量 $IP_ADDRESS/$BASE_MAC 等发送时替换（<<<PAGE 242-243>>>）。三个训练技巧：expectPrompt 应答确认提示（reload 示例）、<tapps> lastcmd 防挂起、setTimeout/<tapps> set timeout 处理慢命令（<<<PAGE 241-244>>>）。脚本不能发 Stellar 无线设备（<<<PAGE 239>>>）。第三方 MIB：OID 只填 enterprises 后段，依赖顺序排好再 Apply，导入后不立即解析（<<<PAGE 285-288>>>）。

### 6. Unified Access：三途径 + L2/L3 分层
Workflow（六种引导流）/Template（批量）/Device Config（单机微调）三途径（<<<PAGE 592>>>）。L2 认证定 UNP+VLAN 之后不变，L3 动态改策略（<<<PAGE 591-592>>>）。角色分配优先级：认证返回角色 > Classification Rules > Default ARP（<<<PAGE 602-603>>>）。映射方法六选一（VLAN/SPB/VXLAN/Static Service/Tunnel/VLAN+Tunnel）（<<<PAGE 608-613>>>）。高频坑：AAA 超时改了不追溯在线用户（<<<PAGE 614-618>>>）、tagged 口与聚合成员不能启 UNP（<<<PAGE 594-601>>>）、Redirect 开启后只能映射 VLAN（<<<PAGE 608-613>>>）。

### 7. UPAM：内置 CP+RADIUS 双角色
UPAM 同时做 Captive Portal 与 RADIUS 服务器（<<<PAGE 678>>>）。三种工作流：BYOD（MAC+CP）、Guest（MAC+CP+自助注册）、MAC or 802.1X（无 CP）（<<<PAGE 681-682>>>）。预置 All Managed Devices NAS 密钥固定 123456，托管设备每 15 分钟自动入库（<<<PAGE 682-684>>>）。Guest 策略 ≤32 条，Login Strategy 四种 + 社交登录（FB/Google/Rainbow/WeChat 需 OAuth+DNS）；WiFi4EU 专用模板且 CP 有效期 ≤24h（<<<PAGE 712-718>>>）。BYOD 无自助注册/Access Code/Data Quota，Max Device 仅 1-10（<<<PAGE 756-766>>>）。

### 8. SSIDs：一步式联动生成八对象
创建 SSID 自动派生 Access Role Profile/Access Policy/Authentication Strategy/Guest/BYOD Strategy/AAA/Tunnel Profile/Global Configuration（<<<PAGE 861-863>>>）。五种 Usage：Guest Network(Open+CP)、Employee BYOD、Enterprise 802.1X、Protected Network(PSK±CP)、Protected for Employees(PSK+BYOD Portal)。Usage 与 Strategy 不匹配的 SSID 不能编辑。安全矩阵：6GHz 强制 OWE、WPA3 不支持机型回退 WPA2、Transition Mode 需 AWOS 4.0.8+（<<<PAGE 649-655, 864-874>>>）。PPSK 每 SSID ≤16 Entry、单 AP 合计 ≤64；Device Specific PSK 仅配 UPAM RADIUS（Prefer/Force）（<<<PAGE 864-874>>>）。Stellar AP VLAN 池按机型限 2/4/7 个 WLAN（<<<PAGE 864-874>>>）。

### 9. Quarantine 与 PolicyView：状态机 + 通知-拉取
事件链：IPS/Syslog→规则（Banned 优先）→Candidates（流量照常）/Banned（进隔离 VLAN 走 QMR）/Disabled Ports（全部条目释放端口才启用）（<<<PAGE 457, 460-465>>>）。基础设施三件套（Quarantined VLAN+同名 MAC 组+Drop 策略）缺一则 Banned 设备照样通流量（<<<PAGE 473-475>>>）。无线客户端走 Client Blocklist（365 天）而非 Banned（<<<PAGE 460>>>）。PolicyView 策略存内置 LDAP、Notify 触发全网 flush+重载（代价高，批量一次）（<<<PAGE 396-397>>>）；优先级域 30001-65535 分段给 One Touch Voice/Data 与 Expert，外部工具勿占用（<<<PAGE 387>>>）；QoS 执行后全网 Unsaved，必须两步保存（<<<PAGE 44>>>）。

### 10. VM/VXLAN：塑形模型 + 大二层
vCenter(≤2)+Hyper-V 混合纳管，VM 上限 5000；Hypervisor 时间必须与 OV 同步（<<<PAGE 830-840>>>）。塑形模型：VM VLAN→UNP Tag 规则→每 VLAN 一个 UNP，vMotion 免改配置（<<<PAGE 830-840>>>）。One-Touch SPB 自动生成 UNP/ISID/BVLAN(4 轮转+ECT)（<<<PAGE 841-847>>>）。VXLAN 仅 OS6900-Q32/X72：VFI=SAP 学客户 MAC+SDP 学网络 MAC；组播隧道要求全网 PIM 统一（<<<PAGE 848-852>>>）。VM Snooping 默认 UDP 4789、Aging 300s（<<<PAGE 855-860>>>）。

## 三、高价值章节页码索引

| 主题 | 页码 |
|---|---|
| 功能地图（LAN+WLAN/WLAN 菜单） | 31-34 |
| 首次纳管五步法 | 40-44 |
| Top N 报表与 Analytics Profile | 66-91, 130-131 |
| Statistics Collection/Chart View | 117-124 |
| Application Visibility 三步法 | 201-209 |
| Captive Portal 定制四步 | 235-236 |
| CLI Scripting 全流程 | 238-248 |
| Discovery Range/Profile/操作集 | 255-264 |
| 第三方 MIB 导入 | 285-288 |
| Locator 定位 | 336-349 |
| PolicyView Unified Policy 向导 | 386-396 |
| Provisioning 工作流/Thin Switch | 429-439 |
| Quarantine 三列表与规则 | 457-475 |
| Report 两步模型 | 484-486 |
| Backup/Restore/Upgrade | 488-501 |
| Auto Configuration 四步 | 502-506 |
| SAA | 512-515 |
| Topology 地图体系 | 554-581 |
| Unified Access 三途径 | 590-592 |
| Access Role Profile | 608-613 |
| UPAM 工作流与策略 | 678-693, 712-718 |
| Guest Account/自助注册 | 742-766 |
| UPAM Settings 集成 | 767-778 |
| Users/User Groups/2FA | 780-808 |
| VM Manager/VXLAN/VM Snooping | 830-860 |
| SSIDs 一步式/PPSK/WPA3 | 861-874 |

## 四、一句话总纲

OV2500 是 Profile 驱动的参考型网管：先在功能地图里找到应用，再按"建 Profile→应用到设备→Notify/保存"的固定节奏操作；所有静默失败（SNMP 源 IP、Unsaved 跳过、凭据缺失）都靠本手册的默认值与反例清单兜底。
