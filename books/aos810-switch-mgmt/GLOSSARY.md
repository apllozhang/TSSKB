# GLOSSARY — OmniSwitch AOS 8.10R4 Switch Management Guide 核心术语

从 verified 术语库（224 条）精选约 120 条，按主题分组。命令/协议名保留英文，页码为原书页码。

## 系统与升级

- **AOS**：Alcatel-Lucent Enterprise OmniSwitch 操作系统，本书 8.10R4 版（<<<PAGE 1>>>）
- **ISSU**：In Service Software Upgrade，在线软件升级，VC/机箱最小 disruption 升级（<<<PAGE 22>>>）
- **Validation File**：ISSU 升级兼容性验证文件（<<<PAGE 24>>>）
- **ALE Secured Code**：ALE 第三方加固代码计划（源码审查、漏洞扫描）（<<<PAGE 65>>>）
- **ASLR**：Address Space Layout Randomization，重启随机化内存布局防利用（<<<PAGE 65>>>）
- **Signed AOS Images**：RSA-2048+SHA-256 签名的 AOS 镜像（<<<PAGE 66>>>）
- **Secure Boot**：启动链验证，只引导可信软件（<<<PAGE 66>>>）
- **pkgmgr**：Package Manager，Debian 包验证/安装/移除（<<<PAGE 85>>>）
- **appmgr**：Application Manager，应用 start/stop/restart 免重启（<<<PAGE 85>>>）
- **U-boot**：引导加载器，可设访问与密码认证（<<<PAGE 91>>>）
- **ONIE**：开放网络安装环境；灾备用 Onie Rescue（<<<PAGE 92, 116>>>）
- **Validation File**：ISSU 兼容性验证文件（<<<PAGE 24>>>）
- **Trescue.img**：USB 灾备恢复镜像（<<<PAGE 116>>>）
- **aossignature**：USB 自动拷贝防误触发的签名空文件（<<<PAGE 113>>>）
- **image integrity check / get-key**：镜像 SHA256 校验/取值命令（<<<PAGE 118>>>）

## Flash 目录与配置

- **/flash**：闪存根目录，含 certified/working/network/switch/system 等（<<<PAGE 52>>>）
- **certified directory**：已认证的默认可靠目录，配置不可直接写入（<<<PAGE 94>>>）
- **working directory**：新文件暂存/测试目录（<<<PAGE 94>>>）
- **RUNNING DIRECTORY**：当前配置保存目标目录，任意目录均可设为运行目录（<<<PAGE 94>>>）
- **RUNNING CONFIGURATION**：RAM 中的当前运行配置（<<<PAGE 94>>>）
- **vcboot.cfg**：启动配置文件（ASCII）（<<<PAGE 94>>>）
- **Software Rollback**：软件回滚，借目录结构回旧版本（<<<PAGE 95>>>）
- **certify-on-reboot**：下次重启强制从 working 加载并自动认证（<<<PAGE 107>>>）
- **copy running certified**：运行目录内容认证到 certified（<<<PAGE 106>>>）
- **copy flash-synchro**：同步主备 CMM 的 certified 内容（<<<PAGE 110>>>）
- **fsck / newfs / freespace**：文件系统检查/重建/剩空间命令（<<<PAGE 59>>>）
- **watch/cut/paste/tee**：CLI 直接暴露的 Linux 工具（<<<PAGE 60>>>）
- **Configuration File**：含 CLI 命令的 ASCII 文本（<<<PAGE 122>>>）
- **configuration apply / syntax-check**：应用与语法预检（<<<PAGE 133, 137>>>）
- **Timer Session**：配置文件定时/倒计时应用会话（<<<PAGE 136>>>）
- **configuration snapshot**：导出非默认配置快照（asc.n.snap）（<<<PAGE 139>>>）
- **configuration backup / restore**：用户配置 tar 备份（上限 10 份）与恢复（<<<PAGE 138>>>）
- **reset-to-factory**：恢复出厂（config/retain-vc/all 三档）（<<<PAGE 141>>>）
- **.err file**：配置应用/检查出错日志（<<<PAGE 137>>>）
- **swlog**：交换机日志文件（/flash/network）（<<<PAGE 52>>>）
- **command-log**：命令审计日志（command.log，含用户/IP/结果）（<<<PAGE 127>>>）

## 登录与会话

- **CLI**：Command Line Interface，AOS 单级命令体系（<<<PAGE 29, 122>>>）
- **Console Port**：控制台串口（micro-USB/RJ-45），默认 9600-8-N-1（<<<PAGE 33>>>）
- **EMP**：Ethernet Management Port，绕过 NI 直接管理 CMM 的以太网口（<<<PAGE 31>>>）
- **USB Ethernet Dongle**：USB 转以太网适配器，等效 EMP（<<<PAGE 35>>>）
- **SSH / SFTP**：加密远程登录与文件传输（<<<PAGE 38>>>）
- **PKA**：Public Key Authentication，SSH 公钥认证（<<<PAGE 41>>>）
- **Login Banner / pre_banner.txt**：登录横幅文件（仅 ASCII .txt，FTP 不支持 pre-banner）（<<<PAGE 43-44>>>）
- **session timeout**：会话不活动超时（默认 4 分钟）（<<<PAGE 29>>>）
- **session login-attempt / login-timeout**：登录尝试次数/时限（<<<PAGE 45>>>）
- **DNS Resolver**：域名解析，最多 3 IPv4 + 3 IPv6 服务器（<<<PAGE 46>>>）
- **FIPS**：FIPS 140-2 加密合规模式，切换需重启（<<<PAGE 46>>>）
- **Single-level CLI / Partial Keyword Completion**：单级命令体系与 Tab 最短唯一前缀补全（<<<PAGE 122, 124>>>）
- **no form**：命令的 no 形式撤销配置（<<<PAGE 124>>>）
- **history buffer / !n**：命令历史与 bang 重放（<<<PAGE 126>>>）
- **who / whoami / kill**：会话查看与终止（<<<PAGE 163-164>>>）

## 用户与 AAA

- **admin user**：默认管理员（admin/switch），恒可 console 登录（<<<PAGE 145>>>）
- **secureadmin user**：高安全默认账户，首登强制改密并切增强模式（<<<PAGE 145>>>）
- **default user**：新用户默认权限模板账户，不可登录（<<<PAGE 150>>>）
- **Partitioned Management / Command Domain / Command Family**：按命令域/族分区授权（<<<PAGE 145, 159>>>）
- **Password History / Expiration**：旧密码保留数（默认 4）与密码过期（<<<PAGE 154-155>>>）
- **Lockout Window/Threshold/Duration**：锁定观察窗/阈值/时长（<<<PAGE 156>>>）
- **user lockout unlock**：手工锁定/解锁用户（<<<PAGE 158>>>）
- **AAA**：Authentication, Authorization, Accounting（<<<PAGE 168>>>）
- **RADIUS / LDAP**：AAA 外部服务器（SNMP 仅支持 LDAP/local）（<<<PAGE 168, 174>>>）
- **aaa authentication**：各管理接口认证源链配置（<<<PAGE 170>>>）
- **exit-on-fail**：仅用第一个可用服务器、失败即拒绝（默认 enable）（<<<PAGE 171>>>）
- **aaa accounting session**：ASA 会话计费（<<<PAGE 175>>>）
- **ASA Enhanced Mode**：增强安全模式（加盐/单会话/TLS1.2/镜像校验）（<<<PAGE 176>>>）
- **priv-mask**：按接入类型（ssh/telnet/console/http）的权限掩码（<<<PAGE 181>>>）
- **ip-lockout-threshold / banned-ip**：按来源 IP 的封禁（<<<PAGE 180>>>）
- **Management Station**：远程管理 IP 白名单（上限 64）（<<<PAGE 182>>>）
- **JITC Mode**：军用安全认证模式（与增强/CC 互斥）（<<<PAGE 184>>>）
- **Crypto Strong Security**：禁弱哈希/加密算法特性（<<<PAGE 186>>>）
- **super-user-password**：su 超级用户密码，不可恢复（<<<PAGE 186>>>）
- **Salt**：增强模式 16 字节密码盐（<<<PAGE 180>>>）
- **imgsha256sum**：增强/JITC 模式镜像校验和文件（<<<PAGE 178, 185>>>）
- **hardware-self-test / process-self-test**：硬件/进程自检（<<<PAGE 146, 183>>>）

## SNMP 与 WebView

- **SNMP Agent / Manager / MIB / PDU**：SNMP 双角色与被管对象体系（<<<PAGE 208>>>）
- **Get/GetNext/GetBulk/Set**：SNMP 读/写操作（<<<PAGE 208>>>）
- **Trap / Inform**：代理主动通知；inform 需确认（<<<PAGE 208, 210>>>）
- **Community String / snmp community-map**：v1/v2c 口令式标识及其到用户的映射（<<<PAGE 210, 212>>>）
- **USM / VACM / TSM**：SNMPv3 安全模型（用户/视图/TLS）（<<<PAGE 209, 211>>>）
- **SNMP Engine ID**：代理引擎标识（默认企业值+MAC）（<<<PAGE 216>>>）
- **Trap Filtering / Absorption / Replay**：trap 过滤/吸收去重/重放（<<<PAGE 217-218>>>）
- **priv-password**：SNMPv3 用户独立加密密码（<<<PAGE 214>>>）
- **WebView**：内嵌 Web 管理界面（https://<ip>/new#/）（<<<PAGE 32, 190>>>）
- **webview force-ssl**：强制 HTTPS（默认启用）（<<<PAGE 190>>>）

## 云管理与 NaaS

- **OmniVista Cirrus**：ALE 云管理平台，零接触开通（<<<PAGE 222>>>）
- **Cloud Agent**：交换机连云代理（cloud-agent admin-state）（<<<PAGE 224>>>）
- **Activation Server / Call-home**：激活服务器与序列号注册取 license（<<<PAGE 223, 229>>>）
- **DHCP Option 43 (VSO)**：厂商自定义选项，下发激活/代理子选项（<<<PAGE 229, 234>>>）
- **VPN Server / Image Download Server**：云端 OpenVPN 接入与镜像下载（<<<PAGE 228>>>）
- **NaaS**：Network as a Service 订阅模式（<<<PAGE 232>>>）
- **Essential/Advanced/Management/Upgrade License**：NaaS 四类订阅（<<<PAGE 232>>>）
- **Grace Period / Degraded Mode**：NaaS 宽限期与降级模式（<<<PAGE 233, 238>>>）
- **Capex / Undecided Capex mode**：永久买断模式及未定态（<<<PAGE 233>>>）
- **Thin Switch**：瘦交换机模式，本地仅存最小连通配置（<<<PAGE 240>>>）
- **Monitoring Agent / Config Agent**：Cirrus agent 双组件（MQTT 上报/配置执行）（<<<PAGE 241>>>）

## Web Services 与自动化

- **REST / REST Verbs（GET/PUT/POST/DELETE）**：RESTful 架构与四动词（<<<PAGE 246>>>）
- **URN / Domain（mib/cli/info）**：REST 资源与访问域（<<<PAGE 247>>>）
- **AOSAPI / AOSConnection**：Python Web Services 客户端库（<<<PAGE 260, 262>>>）
- **HEREDOC / awk / grep / sed**：Bash 脚本与文本处理工具（<<<PAGE 265, 268>>>）
- **event-action / /flash/python**：trap 事件绑定脚本及其必须目录（<<<PAGE 270>>>）
- **AMS / Broker / Topic / Community**：AOS Micro Services 发布订阅体系（MQTT，端口 8883）（<<<PAGE 272-273>>>）
- **Config-DB / config-sync**：AMS 配置回放与本地消费组件（<<<PAGE 273>>>）
- **AMS Broker Redundancy**：基于 VRRP 的 broker 故障切换（<<<PAGE 278>>>）
- **OpenFlow / Logical Switch / Hybrid(API) Mode**：SDN 控制/转发分离与混合模式（<<<PAGE 281>>>）
- **PROFINET / IO-Device / GSDML**：工业以太标准及设备描述文件（<<<PAGE 288, 293>>>）

## 虚拟机箱

- **VC / Master / Slave Chassis**：虚拟机箱及其主从机箱（<<<PAGE 300, 306>>>）
- **VFL**：Virtual Fabric Link，VC 互联聚合链路（16 字节封装头）（<<<PAGE 306>>>）
- **Control VLAN**：VC 控制专用 VLAN（默认 4094，仅 VFL 端口）（<<<PAGE 306>>>）
- **IS-IS VC**：VC 专有拓扑管理协议（与路由 IS-IS 无关）（<<<PAGE 306>>>）
- **RCD**：Remote Chassis Detection，EMP 带外分裂检测（<<<PAGE 306, 311>>>）
- **VCSP / VCSP Helper**：分裂保护协议及其转发邻机（<<<PAGE 306, 340>>>）
- **Guard Timer / Protection State**：VCSP 恢复等待计时器与保护态（<<<PAGE 340>>>）
- **vcsetup.cfg**：单机入 VC 设置文件（Chassis ID/Group/priority 等）（<<<PAGE 306>>>）
- **convert-configuration**：standalone 转 VC 配置转换命令（<<<PAGE 307>>>）
- **Auto-VFL / auto-vf-link-port**：自动 VFL 端口与自动 VFL ID（<<<PAGE 333-334>>>）
- **Automatic Chassis ID Assignment**：无 vcsetup.cfg 启动由 Master 分配 ID（<<<PAGE 336>>>）
- **ssh-chassis / virtual-chassis shutdown**：VC 跨机箱访问与受控下架（<<<PAGE 327>>>）
- **Mixed VFL Mode**：X48C4E 与其他 6900 混合 VC 所需模式（<<<PAGE 319>>>）
- **EMP-VC / Chassis EMP**：VC 整体管理 IP 与单机管理 IP（<<<PAGE 306, 325>>>）

## 自动化部署与时钟

- **RCL**：Automatic Remote Configuration Download，无 vcboot.cfg 时 DHCP+TFTP/FTP 自动下载（<<<PAGE 345, 348>>>）
- **Instruction File（*.alu）**：TFTP 指令文件（Keyword:Value，大小写敏感）（<<<PAGE 346, 359>>>）
- **Nearest-Edge Mode**：管理交换机 LLDP 通告管理 VLAN 的模式（专用组播 MAC）（<<<PAGE 363>>>）
- **VLAN 127 / DHCP Option 66/67**：RCL 的 tagged DHCP 广播 VLAN 与 TFTP 选项（<<<PAGE 346, 354>>>）
- **LACP Auto Detection**：RCL 期间检测 LACP PDU 自动建聚合（<<<PAGE 365>>>）
- **Lightning Configuration Mode**：出厂机 WebView/SSH 快速开局向导（默认 192.168.0.1/24）（<<<PAGE 373>>>）
- **Automatic Fabric（auto-fabric）**：自动发现配置 LACP/SPB/MVRP/IP（<<<PAGE 377, 383>>>）
- **config-save（auto-fabric）**：发现配置自动保存（默认 300 秒）（<<<PAGE 379, 403>>>）
- **SPB / BVLAN / ECT**：自动发现建 BVLAN 4000-4003、ECT 1-4（<<<PAGE 386>>>）
- **MVRP**：Multiple VLAN Registration Protocol，仅 flat STP 下支持（<<<PAGE 388>>>）

## License 与时钟杂项

- **License apply**：安装 license 命令（file 或 key 方式）（<<<PAGE 66>>>）
- **Premium (Bundle) License**：捆绑多子 license 的单一大 license（<<<PAGE 69>>>）
- **SILOS / SWLIC**：站点 license 服务器及其客户端（MQTT 通信）（<<<PAGE 71>>>）
- **Site license / Node license**：4 节点浮动 / 单节点绑定 license（<<<PAGE 73-74>>>）
- **MQTT**：消息协议，SILOS/AMS/Cirrus 共用（<<<PAGE 71, 272>>>）
- **Keychain**：集中密钥管理，密钥带生命周期轮转（<<<PAGE 83>>>）
- **hash-control（brief/extended）**：哈希模式，影响 LAG/SLB/ECMP（<<<PAGE 82>>>）
- **NTP / Stratum / minpoll-maxpoll / burst-iburst**：时间同步体系（<<<PAGE 406-416>>>）
- **ntp.keys / trusted key**：NTP 认证密钥文件与可信密钥（<<<PAGE 417>>>）
- **DST / DHCP Option-2**：夏令时随时区自动 / DHCP 下发时区（用户配置优先）（<<<PAGE 78>>>）
