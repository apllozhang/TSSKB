# GLOSSARY — OmniVista 2500 NMS Administration R4（DT00XTE311）

术语解释基于本书 verified 内容概括；界面/产品名保留英文。页码为原书页码。

## 平台与部署

- **OmniVista 2500 (OV2500)**：ALE 的网络管理系统（NMS，网络管理系统），以 Virtual Appliance 虚拟机形态交付，内含 Linux OS 与 OV 应用，无独立安装器（<<<PAGE 25/44>>>）。
- **Virtual Appliance (VA)**：打包了操作系统与应用的虚拟机镜像，部署到 ESXi/Hyper-V/KVM 即可用（<<<PAGE 25/44>>>）。
- **Network Size**：安装时选择的平台容量档位（Low <500 / Medium 500-2000 / High 2000-5000 / Very High 5000-10000 台设备），系统按档位分配内存（<<<PAGE 45/58>>>）。
- **Sizing**：容量规划；决定 vCPU/内存/磁盘与管理设备数的匹配关系（<<<PAGE 45>>>）。
- **Hypervisor**：虚拟化宿主平台，支持 VMware ESXi 6.5-8.0、Hyper-V 2012R2-2022、KVM Ubuntu 22.04（<<<PAGE 44>>>）。
- **OVF Template**：vSphere 的虚拟机模板部署格式；部署 OV2500 时 Disk Formatting 推荐 Thick Provision（<<<PAGE 54>>>）。
- **cliadmin**：VA 控制台初始化时设置的管理账号密码（<<<PAGE 56>>>）。
- **Snapshot（快照）**：保存 VA 初始参数（IP/网关/network size）的恢复点；无快照则无法恢复初始配置（<<<PAGE 100>>>）。
- **R-Lab / Remote Lab**：远程培训实验室环境，经 https://rdp.al-mydemo.com/ 连接；有音频缺失与 Firefox 剪贴板限制（<<<PAGE 81/86/195>>>）。

## 许可（License）

- **Device License**：按设备计数的许可，分 Starter Pack（免费 30 台：10 AOS+10 三方+10 Stellar）、Evaluation（90 天 60 台）、Production（最多 10000 台）（<<<PAGE 46-49>>>）。
- **Service License**：功能型许可：VM/Guest/On-Boarding/HA/Web Content Filtering（<<<PAGE 46-49>>>）。
- **Evaluation License**：评估许可；在 lds.al-enterprise.com 用 Customer ID 99999 / Order Number "evaluation" / Passcode omnivista 生成（<<<PAGE 103-104>>>）。
- **Enable Fleet Supervision**：EULA 确认页的可选项，本书明确不要勾选（<<<PAGE 104>>>）。
- **NaaS（Network as a Service）**：设备向 License Activation Server 获取许可的模式；状态含 CAPEX 与 CAPEX Undecided（未取得许可）（<<<PAGE 127>>>）。

## 高可用与系统管理

- **HA（High Availability）**：Main/Standby 双 OV 实例常驻、状态同步、故障自动接管；HA 许可无需双倍购买（<<<PAGE 17-19/50>>>）。
- **Main OV / Standby OV**：HA 中承担全部功能的主实例与保持同步的备实例（<<<PAGE 18>>>）。
- **Watchdog**：OV 服务管理应用（GUI/CLI），可启停服务、查看服务信息与依赖（<<<PAGE 71/221>>>）。
- **Control Panel**：管理员查看 Watchdog Screen 与 Scheduler History 的入口（<<<PAGE 221>>>）。
- **System Health**：VA 的 CPU/内存/网络流量概览，并提示 VA 配置问题（<<<PAGE 72>>>）。
- **Session Management**：列出所有客户端登录会话，可强制登出（<<<PAGE 73>>>）。
- **2FA / TOTP**：双因素认证；登录密码后需输入 Google Authenticator 生成的时间型 6 位码（<<<PAGE 157-159>>>）。
- **User Group / Group Rights**：用户组权限模型，如 Read 只读组（<<<PAGE 216-218>>>）。

## 设备纳管与发现

- **SNMP**：简单网络管理协议；设备被 OV 管理的前提（默认不可管理）（<<<PAGE 97/164>>>）。
- **SNMPv3 / SHA+DES**：带认证加密的 SNMP 版本；privacy all 档仅接受加密 v3 Set/Get（<<<PAGE 69/97>>>）。
- **snmp community map**：v1/v2 社区字符串到用户的映射命令（<<<PAGE 68>>>）。
- **snmp source ip**：SNMP 源地址选择命令；默认优先 loopback0（<<<PAGE 70>>>）。
- **Loopback0**：交换机管理用环回接口；Discovery 用其地址发现设备（<<<PAGE 70/90>>>）。
- **Trap**：设备主动上报的事件报文；trap 需 snmp station 指向 OV 并启用（<<<PAGE 97>>>）。
- **Discovery Profile**：发现配置三段式（General/SNMP/Advanced）+ IP 范围 + Discover Now（<<<PAGE 110-114>>>）。
- **Trap Station**：接收 trap 的站点配置，Advanced 段设 User（<<<PAGE 110-112>>>）。
- **AMAP / LLDP**：链路层发现协议，拓扑链路自动发现手段（<<<PAGE 117>>>）。
- **Manual Link**：手工添加的持久链路，down 时显示红色，建议用于关键链路（<<<PAGE 118>>>）。
- **Topology / Site**：拓扑应用与物理站点；Create Site 后拖拽排布设备（<<<PAGE 175-176>>>）。
- **Poll Device / Poll Link**：拓扑右侧 Operations 窗口的手工轮询，补显示缺失的设备/链路（<<<PAGE 176>>>）。
- **Locator**：按 IP/MAC/授权用户定位终端位置（交换机槽/端口）的工具，分 Live/Historical（<<<PAGE 30/136-137/187-188>>>）。
- **Mibset**：第三方设备自定义 MIB 集（OID/Display Name/MIB 目录）；MIB-2 兜底填 mib-2（<<<PAGE 121-123>>>）。
- **WebView**：单设备原生网元管理器，100% CLI 等价功能，与 OV 集成（<<<PAGE 23>>>）。
- **SAA / Ethernet OAM**：交换机对之间的服务质量统计（Jitter/RTT/Packet Loss）（<<<PAGE 140-141>>>）。

## 配置与升级管理

- **Resource Manager**：配置备份/恢复、镜像升级、Inventory 报表的统一入口（<<<PAGE 197-206>>>）。
- **Backup Type: Configuration Only**：只备份配置（不含镜像）（<<<PAGE 197>>>）。
- **FTP Authentication**：备份向导中补录交换机 FTP 凭据（admin/switch）（<<<PAGE 198>>>）。
- **Upgrade Image / Install Software**：镜像导入与按设备批量安装固件（<<<PAGE 203-206>>>）。
- **Copy Working Certified**：升级后把 working 目录配置认证为 certified 的收尾命令，漏做升级不生效（<<<PAGE 206>>>）。
- **Scheduled Upgrades**：定时批量升级，可多台同时、每台不同版本与目录（<<<PAGE 124-126>>>）。
- **Inventory Report**：设备清单报表（<<<PAGE 202>>>）。
- **CLI Scripting**：脚本集中存储、向导下发（立即/Periodically/Simple/Cron）、日志留痕（<<<PAGE 209-214>>>）。
- **VLAN Manager / VLAN Wizard**：批量建 VLAN 与 Q Tagged 端口分配、IP 接口的向导（<<<PAGE 180-184>>>）。

## Provisioning 与 Thin Client

- **Template Based Provisioning**：基于规则与模板的新设备零接触上线机制（<<<PAGE 414>>>）。
- **Provisioning Rule**：按序列号/MAC/型号匹配交换机并推送模板的规则；交换机每 5 分钟联系 OV（<<<PAGE 461-462>>>）。
- **Golden Configuration**：从最近三次备份中标记的"黄金配置"，配置被误改时可回滚（<<<PAGE 417/467>>>）。
- **Force Provisioning Config**：下次交换机联系 OV 时强制推送 Rule 配置的按钮（<<<PAGE 467>>>）。
- **Static / Dynamic Template**：无变量静态模板 vs 带 $VLAN/$PORTS 变量的动态模板；后者必须配 Value Mapping（<<<PAGE 463-464>>>）。
- **Value Mapping**：动态模板的变量值表（<<<PAGE 463-464>>>）。
- **Thin Client（OmniSwitch）**：交换机零本地配置模式（仅 vcboot.cfg），配置存 OV，经 call-home 获取；仅 AOS 8.8R1+（<<<PAGE 75-77>>>）。
- **Incremental Template**：追加型模板，在下一次周期 call-home（默认 30 分钟）应用一次（<<<PAGE 77>>>）。
- **RCL / Bootstrap**：DHCP Option 43 Sub-Option 128 或 DNS 别名指向 OV 激活服务器的引导机制（<<<PAGE 460>>>）。
- **Factory-default / Bootstrapped / Provisioned**：设备上线三阶段状态（<<<PAGE 414>>>）。

## Unified Access 与安全

- **UPAM**：OV 的统一策略与接入管理组件，负责 BYOD/Guest 认证下发；也代管交换机用户账号（<<<PAGE 18/166>>>）。
- **AAA Server Profile**：定义 RADIUS 等 AAA 服务器参数的模板（<<<PAGE 235>>>）。
- **Access Role Profile**：定义 UNP 属性（QoS 策略表、Access Policies、Captive Portal 认证）的模板（<<<PAGE 235>>>）。
- **Access Auth Profile**：把预定义 UNP 端口配置指派到边缘端口的模板（含 Port Bounce、Pass Alt、Failure Policy）（<<<PAGE 235/241-242>>>）。
- **UNP（User Network Profile）**：用户网络档案；名称必须与 RADIUS 返回的 Filter-ID 一致（<<<PAGE 263>>>）。
- **Filter-ID**：RADIUS 返回的属性值，即 UNP 名（<<<PAGE 263>>>）。
- **802.1X / EAP-MSCHAP v2**：端口级接入认证协议及客户端认证方法（<<<PAGE 258-268>>>）。
- **MAC Auth**：基于 MAC 的认证方式，仅适用于有线设备（与 802.1X 同）（<<<PAGE 241>>>）。
- **Port Bounce**：COA 换 VLAN 时端口管理性 down，触发 DHCP 续租与重认证（<<<PAGE 241>>>）。
- **Access Classification**：认证不可用时的回退分类规则（有线/无线各一组类型）（<<<PAGE 243-244>>>）。
- **Captive Portal**：Web 认证门户；Profile 仅对启用 CP 认证的 Access Role Profile 有效；可用 html/jpeg 定制（<<<PAGE 252-255>>>）。
- **Unified Policy**：统一策略，挂在 Access Role Profile 配置之下（<<<PAGE 246>>>）。

## PolicyView 与 QoS

- **PolicyView**：QoS/ACL 策略管理应用，双模式 OneTouch / Expert Mode（<<<PAGE 273>>>）。
- **OneTouch**：一键模式，Voice/Data（Platinum/Gold/Silver/Bronze）/ACL 三子模式，参数设一次同时分发（<<<PAGE 273/276-278>>>）。
- **Expert Mode**：专家向导，五步：Create Policy → Device Selection → Set Condition（L2/L3/DSCP/L4/L7）→ Set Action（QoS/Disposition/TCM）→ Validity（<<<PAGE 279-284>>>）。
- **Precedence**：策略优先级序号（如 30001）（<<<PAGE 291>>>）。
- **Disposition (DROP/Accept)**：策略动作中的丢弃/放行决定（<<<PAGE 278/292>>>）。
- **Policy Flow / LDAP Repository**：策略存于安装时配置的 LDAP 目录服务器，交换机被通知后拉取（<<<PAGE 272/286>>>）。
- **DSCP**：差分服务代码点，报文优先级标记字段；SIP Snooping 用其标记语音流（<<<PAGE 438/442>>>）。
- **SIP Snooping**：识别标记 SIP/RTP/RTCP 并计算 Delay/Jitter/RTT/R factor/MOS（<<<PAGE 438>>>）。

## Quarantine Manager

- **Quarantine Manager (QM/AQM)**：攻击检测与隔离模块（<<<PAGE 303>>>）。
- **AlaDosTrap**：AOS 交换机的 DoS 检测 trap 族（Teardrop/Ping of Death/Port Scan）（<<<PAGE 304>>>）。
- **自定义规则四要素**：名称、描述、触发表达式、提取表达式（取源地址）+ 动作（<<<PAGE 305>>>）。
- **Candidates List**：候选名单；设备流量继续放行，等管理员决策（<<<PAGE 308>>>）。
- **Banned List**：隔离名单；保持隔离直至管理员手动释放（<<<PAGE 309>>>）。
- **Never Banned List**：永不隔离名单；OV 服务器与已发现交换机隐式加入（<<<PAGE 310>>>）。
- **Responder**：QM 的响应动作：发邮件（可带变量）或执行外部程序/脚本（<<<PAGE 311>>>）。

## Analytics / AppVis / IoT / OVNA

- **Analytics**：流量与性能分析模块，报表分 Visibility 与 Availability 两类（<<<PAGE 317-318>>>）。
- **Analytics Profile**：生成 Visibility 报表的前置配置（选设备与端口）；一机一档（<<<PAGE 318/342>>>）。
- **sFlow**：流量采样协议，Analytics 的数据来源，携带 L1-L4 信息（<<<PAGE 316/322>>>）。
- **Sampling Rate**：采样率；100 表示每 100 个包生成 1 个样本（<<<PAGE 341>>>）。
- **Top N 趋势预测**：基于机器学习的端口利用率预测（Training Timeout/Training Error 参数）（<<<PAGE 334>>>）。
- **Applications Management（Range-Based / Enumerated）**：端口映射双模式；未映射端口显示 Unknown（<<<PAGE 350>>>）。
- **Application Visibility (AppVis)**：基于签名文件的应用识别与带宽治理（<<<PAGE 360/371-375>>>）。
- **Signature File / Signature Profile**：签名文件与签名档案；一机一 Profile；OS6860E/N 支持 Auto-Update（<<<PAGE 360/372>>>）。
- **App Group（如 MyApps）**：AppVis 中监控/封禁的应用分组（<<<PAGE 371-375>>>）。
- **app-mon（show app-mon …）**：交换机侧应用监控 CLI 命令族（<<<PAGE 377-383>>>）。
- **Statistics Collection Profile / View Profile**：统计采集档案与视图档案分离；默认全体交换机在 Default Profile（<<<PAGE 343/390-394>>>）。
- **Report Configuration**：定期 PDF 报表（Simple/Cron 调度，Purging Policy）（<<<PAGE 354-357>>>）。
- **IoT Inventory**：IoT 终端清单（MAC/IP/状态/类别/厂商/端口），5/15 分钟刷新，仅 IPv4（<<<PAGE 404-405>>>）。
- **DHCP FingerPrinting**：用 DHCP Option 55/60 指纹识别 IoT 设备（<<<PAGE 400>>>）。
- **IoT Enforcement**：按 Category 关联 Access Role Profile 的类级认证，可按 SSID/MAC/AP Group/IP 豁免（<<<PAGE 408>>>）。
- **OVNA（OmniVista Network Advisor）**：云端网络顾问；Edge Computing 本地收 syslog/SSH 采集 + Cloud Processing，经 Rainbow 通知与脚本化处置；与 OVE 每小时同步（<<<PAGE 422-434>>>）。
- **VM Manager**：vCenter 接口跟踪 VM 与网络关联、管理 VM 的 UNP VLAN（<<<PAGE 30>>>）。
- **Stellar AP**：ALE 无线接入点产品线；容量规划与 IoT 刷新周期中反复出现（<<<PAGE 45/405>>>）。
