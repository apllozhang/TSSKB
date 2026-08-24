# DIGEST — OmniVista 2500 NMS Administration R4（DT00XTE311）精华

本书是 ALE OmniVista 2500 网管平台的管理员培训教材（581 页，讲授 + 动手实验），技术栈为 OV2500 R4 虚拟机网管 + OmniSwitch AOS R8。以下为知识地图与十个最重要知识点的串讲，页码均指原书。

## 一、知识地图

全书可归为五条主线、十个技能单元：

1. **平台线**：虚机部署与许可（ov-va-install-license）→ HA 与系统运维、告警通知（ov-ha-services-alerting）。
2. **纳管线**：交换机侧 SNMP 与基础网络准备（ov-switch-snmp-bootstrap）→ Discovery/拓扑/Locator（ov-discovery-topology-locator）→ Resource Manager 备份升级与模板化 Provisioning（ov-resource-manager-provisioning）→ CLI Scripting 批量操作（ov-cli-scripting-batch）。
3. **接入安全线**：Unified Access 三层策略与 802.1X（ov-unified-access）→ PolicyView QoS（ov-policyview-qos）→ Quarantine Manager 攻击隔离（ov-quarantine-manager）。
4. **可观测线**：Analytics/AppVis/IoT/OVNA（ov-analytics-appvis-iot）。
5. **横向概念**：NMS 组件模型（SNMP/sFlow/MIB/Traps/RMON，<<<PAGE 21>>>）与 CLI vs GUI 取舍（<<<PAGE 22-24>>>）贯穿全书。

章节分布：p42-78 安装与系统设置，p107-168 发现与资源管理，p169-224 设备配置管理，p225-256 Unified Access，p257-294 PolicyView，p295-320 Quarantine Manager，p321 起为分析、WLAN/UPAM 与综合实验。

## 二、十大知识点串讲

### 1. 纯虚机形态与 Network Size 一次性分档

OV2500 没有独立安装器——"OmniVista 2500 = Virtual Appliance"，镜像内同时包含 Linux OS 和 OV 应用，跑在 ESXi/Hyper-V/KVM 上（<<<PAGE 25/44>>>）。部署即 vSphere 部署 OVF 模板（磁盘建议 Thick Provision），控制台依次填 IP、端口、**Network Size**、主机名/DNS/NTP 后重启（<<<PAGE 54-60>>>）。Network Size 是安装时锁定的容量档位（Low <500 / Medium 500-2000 / High 2000-5000 / Very High 5000-10000 台），系统按档分配内存（<<<PAGE 45/58>>>）。最容易被忽略的联动：4000 台 Stellar AP 在 High 档下只能带 500 台 AOS 交换机，Very High 档才到 1000 台——无线重的环境选错档就是天花板（<<<PAGE 45>>>）。

### 2. 许可两条线与安装禁区

License 分 Device（Starter 免费 30 台 / Evaluation 90 天 60 台 / Production 最多 10000 台）与 Service（VM/Guest/On-Boarding/HA/Web Content Filtering）（<<<PAGE 46-49>>>）。HA 自 4.3R1 起不需要双倍许可；VC 内每台物理设备各占一个 license 单元（<<<PAGE 50-51>>>）。安装时两个经典翻车点：许可文件与 License Keys 二选一，"Don't do both!"；粘贴 Key 只取逗号后的部分（<<<PAGE 104>>>）。EULA 页不要勾 Enable Fleet Supervision（<<<PAGE 104>>>）。

### 3. 交换机默认不可管理——SNMP 是纳管的前提

"By default, an OmniSwitch cannot be managed by OmniVista"（<<<PAGE 97>>>）。标准准备是逐台执行 SNMPv3 序列：建 read-write 用户（SHA+DES）、`snmp security privacy all`、`snmp station <OV IP> snmpuserv3 v3 enable`、开 trap absorption/to-webview（<<<PAGE 97>>>）。安全档位矩阵决定接受什么：privacy all 只接受加密 v3 读写，traps only 则拒绝所有请求（<<<PAGE 69>>>）。管理寻址用 Loopback0——snmp source ip 默认优先 loopback0，Discovery 也靠 Loopback0 地址找设备；路由表缺 Loopback0 属环境级故障（<<<PAGE 70/90>>>）。

### 4. Discovery 三段式 Profile 与拓扑/定位

Discovery Profile 分 General（CLI/FTP 账号）、SNMP（版本/Timeout 5000/Retry 3/v3 用户）、Advanced（Trap Station User、Discover Link、Shell=SSH、GetBulk、Max Repetitions 10）三段，配 IP 范围后 Discover Now（<<<PAGE 110-114/170-172>>>）。链路靠 AMAP/LLDP 自动发现；关键链路建议手工添加——手工链路持久化、down 时显红色，监控能力更强（<<<PAGE 117-118>>>）。拓扑缺链路就用右侧 Operations 窗口的 Poll Device/Poll Link（<<<PAGE 176>>>）。Locator 按 IP/MAC/授权用户做 Live/Historical 检索，命中即在拓扑定位，是排障取证利器（<<<PAGE 30/187-188>>>）。

### 5. 配置生命周期：备份、升级、Golden Config、Provisioning

Resource Manager 管存量：Backup by Devices（提示补 FTP 凭据就补 admin/switch）→ Configuration Only 备份；Restore 选备份文件恢复（<<<PAGE 197-201>>>）。镜像升级后必须 SSH 到交换机从 working 目录 reload 并执行 Copy Working Certified，漏做升级不生效（<<<PAGE 203-206>>>）；批量场景用 Scheduled Upgrades，可多台同时、每台不同版本（<<<PAGE 124-126>>>）。新设备零接触上线走 Provisioning Rule：交换机每 5 分钟联系 OV，命中序列号/MAC/型号即推送模板；动态模板（$VLAN/$PORTS 变量）必须配 Value Mapping（<<<PAGE 461-464>>>）。配置被误改时从 Golden Configuration（最近三次备份之一）回滚，Force Provisioning 可在下次接触时强制推送（<<<PAGE 466-467>>>）。

### 6. Unified Access 三层模板模型

这是全书概念密度最高的部分：AAA Server Profile（认证服务器参数）→ Access Role Profile（UNP 属性：QoS 策略表、Access Policies、Captive Portal）→ Access Auth Profile（把 UNP 端口配置指派到边缘端口），Unified Policy 挂在 Access Role Profile 之下（<<<PAGE 235/246>>>）。实操链路：RADIUS_VM → AAA_RADIUS → UNP-employee（Map to VLAN 80）→ UNP_template 应用到 6860B 端口 1/1/1，验证靠 `aaa test-radius-server` 返回 Filter-ID、`show unp user`、Locator 按 Auth. User 查询（<<<PAGE 258-268>>>）。三个高频陷阱：UNP 名必须与 Filter-ID 完全一致（<<<PAGE 263>>>）；重测前 `unp user flush` 清残留（<<<PAGE 268>>>）；客户端要取消缓存凭据/自动 Windows 登录/证书校验（<<<PAGE 267-268>>>）。

### 7. PolicyView 双模式与 LDAP 策略仓库

OneTouch 面向 Voice/Data（Platinum-Gold-Silver-Bronze）/ACL 常见场景，参数设一次同时分发（<<<PAGE 273/276-278>>>）；Expert Mode 五步向导处理复杂策略——典型实验是按源 192.168.80.0/24 → 目的 192.168.200.0/24、Action=DROP、Precedence 30001 阻断客户端访问 Loopback0 网段，下发后等 "Notify Success!" 再验证 ping（<<<PAGE 279-293>>>）。底层机制要记住：策略存于安装时配置的 LDAP 目录服务器，交换机被通知后自行拉取（<<<PAGE 272/286>>>）——解释了为什么策略下发是"通知-拉取"而非直接推送。

### 8. Quarantine Manager：默认全禁用与三列表语义

检测来源开放（AOS DoS trap、第三方 IPS、Brick Firewall、WLAN Rogue Alert），规则含内置族（AlaDosTrap/Fortinet/OA WLAN）与自定义四要素（名称/描述/触发表达式/提取表达式/动作），执行手段从 `vlan 999 <mac>` 隔离到 ACL、端口关断分级（<<<PAGE 298-307>>>）。两个语义关键：所有内置规则默认禁用，"以为开了其实没开"最常见（<<<PAGE 304>>>）；Candidates 名单设备流量继续放行、只是等管理员决策，Banned 才是真隔离且必须手动释放，OV 自身与已发现交换机隐式在 Never Banned（<<<PAGE 308-310>>>）。

### 9. 可观测体系：sFlow 采样到应用封禁的完整链路

Analytics 数据面是 sFlow：交换机采样发包 → OV Analytics Service → Mongo DB → WebServer 呈现，应用识别靠 sFlow 里的 TCP/UDP 端口（<<<PAGE 316/322/325>>>）。报表分 Visibility（需先建 Analytics Profile）与 Availability（<<<PAGE 317-318>>>）。AppVis 在此之上用签名文件做深度识别并可 enforcement DROP——实验里建 MyApps 组（Facebook/Twitter/youtube/bet365）封社交游戏流量，交换机侧 `show app-mon` 命令族可验证，注意要等 15-20 分钟数据才出来（<<<PAGE 371-383>>>）。铁律是"一机一档"：Analytics/Signature/统计 Profile 都要求一台交换机只属一个同类 Profile，新建前先解绑 Default（<<<PAGE 342/372/391>>>）。

### 10. HA 与运维底座

单 OV 故障的后果：管理员失去监控与配置能力，UPAM 场景下新客户端无法认证（<<<PAGE 18>>>）。HA 双实例常驻、Main 保持 Standby 同步、故障时服务整体接管，Trap 双实例自动配置、failover 自动 Replay 并弹告警横幅（<<<PAGE 17-19>>>）。应用层看 Watchdog（Control Panel 可逐服务启停、查依赖，Scheduler History 看事件历史）（<<<PAGE 71/221>>>）。告警链路是 SMTP 配置 + Trap Responder（务必禁用 Normal 级别防刷屏，交换机端口需 link-trap enable）（<<<PAGE 191-194>>>）。账号侧按用户组授权 + 按角色启用 2FA（Google Authenticator TOTP）（<<<PAGE 157-159/216-218>>>）。

## 三、一句话总纲

OV2500 的管理逻辑可以压成一句：**设备先给 SNMP 和 Loopback0 才能被管；平台安装时定死容量档；接入策略走 AAA→Role→Auth 三层模板；QoS 与隔离都是"规则+执行"闭环；一切分析数据源头是 sFlow 采样。** 掌握这五句加上十个技能单元的操作路径，就覆盖了这本 581 页教材的可迁移内核。
