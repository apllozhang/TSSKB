# glossary.md — 术语候选（《OmniSwitch AOS Release 810R04 Switch Management User Guide》）

- 格式：`- **术语**：解释 <<<PAGE N>>>`；按章分组；页码为真实标记页。

## 第 1-2 章 入门 / 登录

- **AOS**：Alcatel-Lucent Enterprise OmniSwitch 操作系统，本书描述 8.10R4 版。<<<PAGE 1>>>
- **ISSU**：In Service Software Upgrade，在线软件升级，"used to upgrade the software on a VC or modular chassis with minimal network disruption"。<<<PAGE 22>>>
- **Validation File**：ISSU 升级兼容性验证文件，含版本匹配信息。<<<PAGE 24>>>
- **CLI**：Command Line Interface，文本配置界面，AOS 为单级命令体系。<<<PAGE 29>>>、<<<PAGE 122>>>
- **EMP**：Ethernet Management Port，以太网管理口，"allows you to bypass the Network Interface (NI) modules and remotely manage the switch directly through the CMM"。<<<PAGE 31>>>
- **ASA**：Authenticated Switch Access，经本地数据库或外部服务器认证管理用户。<<<PAGE 31>>>
- **WebView**：交换机内嵌的 Web 管理界面（HTTPS，URL 含 /new#/）。<<<PAGE 32>>>
- **Console Port**：控制台串口（micro-USB 或 RJ-45），默认 9600-8-N-1。<<<PAGE 33>>>
- **SSH**：Secure Shell，加密远程登录，防 IP 欺骗/DNS 欺骗/明文截获等。<<<PAGE 38>>>
- **SFTP**：Secure Shell FTP，SSH 子系统的加密文件传输。<<<PAGE 38>>>
- **PKA**：Public Key Authentication，SSH 公钥认证。<<<PAGE 41>>>
- **Login Banner**：登录横幅，/flash/switch 下文本文件经 session banner 命令启用。<<<PAGE 43>>>
- **pre_banner.txt**：登录提示前显示的文本文件，FTP 会话不支持。<<<PAGE 44>>>
- **DNS Resolver**：域名解析服务，最多 3 IPv4 + 3 IPv6 服务器。<<<PAGE 46>>>
- **FIPS**：Federal Information Processing Standards，FIPS 140-2 加密合规模式，切换需重启。<<<PAGE 46>>>
- **session timeout**：会话不活动超时（默认 4 分钟）。<<<PAGE 29>>>
- **USB Ethernet Dongle**：USB 转以太网适配器，等效 EMP（ASIX 8817 / RTL8153 芯片）。<<<PAGE 35>>>

## 第 3 章 系统文件

- **/flash**：闪存根目录，含 certified/working/network/switch/system 等。<<<PAGE 52>>>
- **certified directory**：已认证的默认可靠文件目录，配置不可直接写入。<<<PAGE 94>>>
- **working directory**：新文件暂存/测试目录，可保存配置。<<<PAGE 94>>>
- **RUNNING DIRECTORY**：当前配置保存目标目录，"any directory can be configured to be the RUNNING DIRECTORY"。<<<PAGE 94>>>
- **RUNNING CONFIGURATION**：RAM 中的当前运行配置。<<<PAGE 94>>>
- **vcboot.cfg**：启动配置文件（ASCII），VC 模式整体配置。<<<PAGE 94>>>、<<<PAGE 306>>>
- **Image files / archive files**：镜像文件，多个内部文件的聚合容器。<<<PAGE 94>>>
- **swlog**：交换机日志文件（/flash/network 下 swlog.0/1 等）。<<<PAGE 52>>>
- **fsck**：文件系统检查/修复命令（no-repair/repair）。<<<PAGE 59>>>
- **newfs**：删除整个文件系统的命令（危险）。<<<PAGE 59>>>
- **freespace**：显示文件系统剩余空间。<<<PAGE 59>>>
- **watch/cut/paste/tee**：CLI 直接暴露的 Linux 工具集。<<<PAGE 60>>>
- **TFTP**：Trivial File Transfer Protocol，无登录、单会话。<<<PAGE 64>>>
- **ALE Secured Code**：ALE 第三方加固代码计划（源码审查、漏洞扫描等）。<<<PAGE 65>>>
- **ASLR**：Address Space Layout Randomization，每次重启随机化内存布局防利用。<<<PAGE 65>>>
- **Signed AOS Images**：RSA-2048+SHA-256 签名的 AOS 镜像。<<<PAGE 66>>>
- **Secure Boot**：启动链验证，确保只引导可信软件。<<<PAGE 66>>>
- **License apply**：安装 license 的命令（file 或 key 方式）。<<<PAGE 66>>>
- **Premium (Bundle) License**：捆绑多子 license 的单一大 license（OS6570-SW-PRM12/28、OS6870-SW-PRM1/2）。<<<PAGE 69>>>
- **SILOS**：Site Local Licensing Server，跑在交换机上的站点 license 服务器（Debian 包）。<<<PAGE 71>>>
- **SWLIC**：Switch Local Licensing client，向 SILOS 取 license 的客户端。<<<PAGE 71>>>
- **MQTT**：Message Queuing Telemetry Transport，SILOS/SWLIC 与 AMS/Cirrus 使用的消息协议。<<<PAGE 71>>>、<<<PAGE 272>>>
- **Site license**：最多 4 节点共享的浮动 license。<<<PAGE 73>>>
- **Node license**：绑定单个网络节点（standalone 或 ≤8 单元 VC）的 license。<<<PAGE 73>>>、<<<PAGE 74>>>
- **DST**：Daylight Savings Time，随时区自动启停。<<<PAGE 78>>>
- **UTC/GMT**：协调世界时，system timezone 基于 UTC 偏移。<<<PAGE 78>>>
- **DHCP Option-2**：DHCP 下发时区偏移（仅默认值时可被设置）。<<<PAGE 78>>>
- **hash-control**：哈希模式（brief/extended），影响 LAG/SLB/ECMP 哈希算法。<<<PAGE 82>>>
- **load-balance non-ucast**：链路聚合非单播负载分担开关（默认关）。<<<PAGE 82>>>
- **Keychain**：集中密钥管理模块，密钥带生命周期轮转。<<<PAGE 83>>>
- **pkgmgr**：Package Manager，Debian 包验证/安装/移除。<<<PAGE 85>>>
- **appmgr**：Application Manager，应用 start/stop/restart。<<<PAGE 85>>>
- **U-boot**：引导加载器，可设访问与密码认证。<<<PAGE 91>>>
- **ONIE**：开放网络安装环境，可设认证；灾备用 Onie Rescue。<<<PAGE 92>>>、<<<PAGE 116>>>

## 第 4 章 CMM 目录

- **CMM**：Chassis Management Module，机箱管理模块；双 CMM 提供冗余。<<<PAGE 93>>>
- **Primary/Secondary CMM**：主/备 CMM，secondary 提供 fail over。<<<PAGE 93>>>、<<<PAGE 99>>>
- **Software Rollback**：软件回滚，借目录结构回到旧版本。<<<PAGE 95>>>
- **copy running certified**：将运行目录内容认证到 certified。<<<PAGE 106>>>
- **copy flash-synchro**：同步主备 CMM 的 certified 内容。<<<PAGE 110>>>
- **takeover**：secondary CMM 接管为主。<<<PAGE 111>>>
- **certify-on-reboot**：下次重启强制从 working 加载并自动认证的特性。<<<PAGE 107>>>
- **show running-directory**：显示当前运行目录与同步状态。<<<PAGE 107>>>
- **show microcode**：显示目录内/已加载镜像版本。<<<PAGE 108>>>
- **/uflash**：USB 闪存挂载点。<<<PAGE 113>>>
- **aossignature**：USB 自动拷贝防误触发的签名空文件。<<<PAGE 113>>>
- **usb auto-copy / usb backup**：USB 自动升级与备份特性（互斥）。<<<PAGE 113>>>、<<<PAGE 114>>>
- **Trescue.img**：USB 灾备恢复镜像。<<<PAGE 116>>>
- **image integrity check / get-key**：镜像 SHA256 校验/取值命令。<<<PAGE 118>>>

## 第 5-6 章 CLI / 配置文件

- **Single-level CLI**：无命令模式层级，任意时刻可输入任意命令。<<<PAGE 122>>>
- **Partial Keyword Completion**：Tab 最短唯一前缀补全。<<<PAGE 124>>>
- **no form**：命令的 no 形式，撤销配置。<<<PAGE 124>>>
- **command-log**：命令日志（command.log，含用户/IP/结果）。<<<PAGE 127>>>
- **history buffer**：命令历史缓存，配合 !n 调用。<<<PAGE 126>>>
- **tty 命令**：设置屏幕行列（10-150 行 / 20-150 列）。<<<PAGE 130>>>
- **Configuration File**：含 CLI 命令的 ASCII 文本，configuration apply 应用。<<<PAGE 122>>>、<<<PAGE 136>>>
- **Timer Session**：配置文件的定时/倒计时应用会话。<<<PAGE 136>>>
- **.err file**：配置应用/检查出错时生成的错误日志文件。<<<PAGE 137>>>
- **configuration syntax-check**：应用前语法预检。<<<PAGE 137>>>
- **configuration snapshot**：导出当前非默认配置为快照文件（asc.n.snap）。<<<PAGE 139>>>
- **configuration backup / restore**：用户配置 tar 备份（/flash/config-recovery，上限 10 份）与恢复。<<<PAGE 138>>>
- **reset-to-factory**：恢复出厂（config/retain-vc/all 三档）。<<<PAGE 141>>>
- **write terminal**：显示当前全部运行配置。<<<PAGE 142>>>
- **Vi editor**：交换机内置行编辑器。<<<PAGE 138>>>

## 第 7-8 章 用户 / 安全

- **admin user**：默认管理员（admin/switch），恒可 console 登录。<<<PAGE 145>>>
- **secureadmin user**：高安全默认账户，首登强制改密并切增强模式。<<<PAGE 145>>>
- **default user**：存储新用户默认权限的模板账户，不可登录。<<<PAGE 150>>>
- **Partitioned Management**：按命令域/族分配用户权限的机制。<<<PAGE 145>>>
- **Command Domain / Command Family**：命令域与命令族（族为域子集）。<<<PAGE 159>>>
- **Password History**：旧密码保留数（默认 4），防重复使用。<<<PAGE 155>>>
- **Password Expiration**：密码过期（全局 1-365 天或单用户指定日期）。<<<PAGE 154>>>
- **Lockout Window/Threshold/Duration**：锁定观察窗/阈值/时长三参数。<<<PAGE 156>>>
- **user lockout unlock**：手工锁定/解锁用户。<<<PAGE 158>>>
- **priv-password**：SNMPv3 用户独立于登录密码的加密密码。<<<PAGE 214>>>
- **who / whoami / kill**：会话查看与终止命令。<<<PAGE 163>>>、<<<PAGE 164>>>
- **RADIUS**：Remote Authentication Dial-In User Service，AAA 服务器。<<<PAGE 168>>>
- **LDAP**：Lightweight Directory Access Protocol，AAA 服务器（SNMP 可用）。<<<PAGE 168>>>
- **AAA**：Authentication, Authorization, Accounting。<<<PAGE 168>>>
- **aaa authentication**：配置各管理接口认证源链的命令。<<<PAGE 170>>>
- **exit-on-fail**：仅用第一个可用服务器、失败即拒绝的选项（默认 enable）。<<<PAGE 171>>>
- **aaa accounting session**：ASA 计费（会话日志）配置。<<<PAGE 175>>>
- **ASA Enhanced Mode**：增强安全模式（更强密码/锁定默认值、单会话、TLS1.2、完整性校验等）。<<<PAGE 176>>>
- **aaa console admin-only**：仅 admin 可用安全 console 会话。<<<PAGE 169>>>
- **ip-lockout-threshold**：按来源 IP 的封禁阈值（默认 6，上限 128 banned IP）。<<<PAGE 180>>>
- **Management Station**：远程管理 IP 白名单（上限 64）。<<<PAGE 182>>>
- **priv-mask**：按接入类型（ssh/telnet/console/http）的权限掩码。<<<PAGE 181>>>
- **JITC Mode**：Joint Interoperability Test Command 军用安全认证模式。<<<PAGE 184>>>
- **Crypto Strong Security**：禁弱哈希/加密算法的特性。<<<PAGE 186>>>
- **super-user-password**：su 超级用户账户密码（不可恢复）。<<<PAGE 186>>>
- **hardware-self-test / process-self-test**：增强模式硬件/进程自检命令。<<<PAGE 146>>>、<<<PAGE 183>>>
- **imgsha256sum**：增强模式/JITC 镜像校验和文件。<<<PAGE 178>>>、<<<PAGE 185>>>
- **Salt（增强模式密码盐）**：16 字节随机盐与密码一同哈希存储。<<<PAGE 180>>>

## 第 9-10 章 WebView / SNMP

- **webview force-ssl**：强制 HTTPS（默认启用）。<<<PAGE 190>>>
- **Web Service / REST**：RESTful 管理接口（mib/cli/info 域，JSON/XML）。<<<PAGE 246>>>、<<<PAGE 247>>>
- **aaa certificate install-certificate webview**：安装 WebView 自定义 SSL 证书。<<<PAGE 192>>>
- **WLAN Cluster-Virtual-IP**：OAW-AP 集群虚拟管理 IP（LLDP 自动学习或手工配置）。<<<PAGE 198>>>、<<<PAGE 199>>>
- **SNMP**：Simple Network Management Protocol，网络管理协议。<<<PAGE 203>>>
- **NMS**：Network Management System/Station，接收 trap 的管理工作站。<<<PAGE 205>>>
- **SNMP Agent / Manager**：代理（交换机内）与管理器（工作站）两角色。<<<PAGE 208>>>
- **MIB**：Management Information Base，被管对象数据库。<<<PAGE 208>>>
- **PDU**：Protocol Data Unit，SNMP 报文。<<<PAGE 208>>>
- **Get/GetNext/GetBulk/Set**：SNMP 读/写操作。<<<PAGE 208>>>
- **Trap / Inform**：代理主动通知；inform 需确认。<<<PAGE 208>>>、<<<PAGE 210>>>
- **Community String**：v1/v2c 的口令式标识（≤32 字符）。<<<PAGE 210>>>、<<<PAGE 212>>>
- **snmp community-map**：community 到用户的映射库。<<<PAGE 212>>>
- **snmp security 等级链**：no security → authentication set/all → privacy set/all（默认）→ traps only。<<<PAGE 215>>>
- **USM**：User-Based Security Model，SNMPv3 安全模型。<<<PAGE 211>>>
- **VACM**：View-Based Access Control Model。<<<PAGE 211>>>
- **TSM**：TLS Security Model，SNMP over TLS（仅 v3）。<<<PAGE 209>>>
- **SNMP Engine ID**：代理引擎标识（默认企业值+MAC）。<<<PAGE 216>>>
- **Trap Filtering**：按命令族或按 trap ID 过滤。<<<PAGE 217>>>
- **Trap Absorption**：抑制重复相同 trap。<<<PAGE 218>>>
- **snmp trap replay**：重放已存储 trap。<<<PAGE 218>>>
- **authentication trap**：SNMP 认证失败 trap（standard/private/both 三模式）。<<<PAGE 218>>>
- **show snmp mib-family**：MIB 表与命令族映射。<<<PAGE 220>>>

## 第 11 章 OmniVista Cirrus / NaaS

- **OmniVista Cirrus**：ALE 云管理平台，零接触开通。<<<PAGE 222>>>
- **Cloud Agent**：交换机上连云的代理（cloud-agent admin-state）。<<<PAGE 224>>>
- **Activation Server**：激活服务器（默认 license.ovng.myovcloud.com）。<<<PAGE 223>>>、<<<PAGE 227>>>
- **DHCP Option 43 (VSO)**：厂商自定义选项，下发激活/代理等子选项（1/128-133/138）。<<<PAGE 229>>>、<<<PAGE 234>>>
- **Call-home**：交换机以序列号向激活服务器注册/取 license 的过程。<<<PAGE 229>>>、<<<PAGE 237>>>
- **discovery-interval**：call-home 重试间隔（默认 30 分钟）。<<<PAGE 223>>>、<<<PAGE 224>>>
- **VPN Server**：云端 OpenVPN 接入点，建立管理隧道。<<<PAGE 228>>>
- **Image Download Server**：云端镜像下载服务器（HTTPS）。<<<PAGE 228>>>
- **NaaS**：Network as a Service，订阅式网络服务模式。<<<PAGE 232>>>
- **Essential/Advanced/Management/Upgrade License**：NaaS 四类订阅。<<<PAGE 232>>>
- **Grace Period**：NaaS 宽限期（45/30/30 天三类）。<<<PAGE 233>>>
- **Degraded Mode**：降级模式，仅转发流量、禁管理/升级。<<<PAGE 238>>>
- **Capex / Undecided Capex mode**：永久买断模式及其未定状态（按制造日期 2021-06-01 判定）。<<<PAGE 233>>>
- **Thin Switch**：瘦交换机模式，本地仅存最小连通配置。<<<PAGE 240>>>
- **Monitoring Agent / Config Agent**：Cirrus agent 的两个组件（MQTT 上报/配置执行）。<<<PAGE 241>>>
- **Greenfield / Brownfield Deployment**：绿地（全新部署）/棕地（存量网络新增）部署场景。<<<PAGE 231>>>

## 第 12 章 Web Services / 脚本 / AMS / OpenFlow

- **REST**：Representational State Transfer 架构风格（无状态、可缓存、URI 命名资源）。<<<PAGE 246>>>
- **REST Verbs（GET/PUT/POST/DELETE）**：读/建/改/删四种动词。<<<PAGE 246>>>
- **URN / Domain（mib/cli/info）**：REST 资源名与访问域。<<<PAGE 247>>>
- **AOSAPI / AOSConnection**：Python Web Services 客户端库核心类。<<<PAGE 260>>>、<<<PAGE 262>>>
- **HEREDOC（<<）**：Bash 块输入重定向。<<<PAGE 265>>>
- **awk / grep / sed**：CLI 文本处理工具。<<<PAGE 268>>>
- **event-action**：trap 事件绑定 Python 脚本的命令。<<<PAGE 270>>>
- **/flash/python**：事件脚本必须存放的目录。<<<PAGE 270>>>
- **AMS**：AOS Micro Services，交换机间发布订阅生态。<<<PAGE 272>>>
- **Broker**：AMS 消息中继（OmniVista 或一台 OmniSwitch，默认端口 8883）。<<<PAGE 272>>>、<<<PAGE 273>>>
- **Topic / Community**：AMS 订阅主题（层级字符串）与交换机社区。<<<PAGE 273>>>
- **Config-DB / config-sync**：AMS 的配置记录回放与本地消费组件。<<<PAGE 273>>>
- **ams-broker.cfg / config-sync.cfg / cron.cfg**：AMS 三配置文件。<<<PAGE 274>>>、<<<PAGE 275>>>
- **Device Profiling Agent**：IoT 设备画像签名同步应用。<<<PAGE 273>>>
- **AMS Broker Redundancy**：基于 VRRP 的 broker 故障切换。<<<PAGE 278>>>
- **OpenFlow**：SDN 控制/转发分离接口。<<<PAGE 281>>>
- **OpenFlow Logical Switch**：受控制器管理的逻辑交换机（含 VLAN/端口资源）。<<<PAGE 281>>>
- **Hybrid (API) Mode**：OpenFlow 混合模式，flow 作为 QoS 策略插入。<<<PAGE 281>>>
- **OpenFlow Group（ALL/INDIRECT）**：动作桶组合。<<<PAGE 282>>>
- **Nutanix Prism**：超融合管理 UI；OmniSwitch 经 Nutanix 插件对接。<<<PAGE 284>>>
- **PROFINET**：工业以太标准；OmniSwitch 作 IO-Device（CC-B）。<<<PAGE 288>>>
- **IO-Controller / IO-Device / IO-Supervisor**：PROFINET 三类节点。<<<PAGE 288>>>
- **GSDML**：PROFINET 设备描述文件（随包提供）。<<<PAGE 293>>>
- **profinet vlan / device-name**：PROFINET 专用 VLAN 与设备名命令。<<<PAGE 289>>>、<<<PAGE 298>>>

## 第 13 章 虚拟机箱

- **VC**：Virtual Chassis，多交换机单 IP 管理的虚拟机箱。<<<PAGE 300>>>
- **Master / Slave Chassis**：VC 主/从机箱。<<<PAGE 306>>>
- **VFL**：Virtual Fabric Link，VC 互联虚拟 fabric 链路（聚合）。<<<PAGE 306>>>
- **Control VLAN**：VC 控制专用 VLAN（默认 4094，仅 VFL 端口）。<<<PAGE 306>>>、<<<PAGE 302>>>
- **IS-IS VC**：VC 专有拓扑管理协议（与路由 IS-IS 无关）。<<<PAGE 306>>>
- **RCD**：Remote Chassis Detection，EMP 带外分裂检测协议。<<<PAGE 306>>>、<<<PAGE 311>>>
- **VCSP**：Virtual Chassis Split Protection，经 helper 的分裂保护协议。<<<PAGE 306>>>、<<<PAGE 340>>>
- **VCSP Helper / VCSP Link Aggregate**：帮助转发 VCSP PDU 的邻机与专用聚合。<<<PAGE 340>>>
- **Active-VC / Sub-VC**：分裂后的主/子 VC。<<<PAGE 340>>>
- **Protection State**：分裂后端口操作关闭的保护状态。<<<PAGE 340>>>
- **Guard Timer**：VCSP 恢复前等待计时器。<<<PAGE 340>>>
- **vcsetup.cfg**：单机入 VC 的设置文件（Chassis ID、Group、priority 等）。<<<PAGE 306>>>
- **convert-configuration**：standalone 转 VC 的配置转换命令。<<<PAGE 307>>>
- **EMP-VC / Chassis EMP**：VC 整体管理 IP 与单机管理 IP。<<<PAGE 306>>>、<<<PAGE 325>>>
- **Startup Error Mode**：vcsetup.cfg 损坏时的回退模式（Invalid-Chassis-Id 等）。<<<PAGE 309>>>
- **Duplicate-Chassis / Mismatch-Chassis-Group**：ID 冲突/组不一致的失败状态。<<<PAGE 320>>>、<<<PAGE 322>>>
- **Auto-VFL / auto-vf-link-port**：自动 VFL 端口与自动 VFL ID 分配。<<<PAGE 333>>>、<<<PAGE 334>>>
- **VFL Mode（auto/static）**：VFL 两种互斥配置模式。<<<PAGE 333>>>
- **Automatic Chassis ID Assignment**：无 vcsetup.cfg 启动时由 Master 分配 ID。<<<PAGE 336>>>
- **virtual-chassis shutdown**：受控隔离一台 VC 成员便于下架。<<<PAGE 327>>>
- **ssh-chassis**：VC 内跨机箱 SSH 访问命令。<<<PAGE 327>>>
- **Remote VC (Remote Stacking)**：10G SFP+ 端口作 auto-VFL 延伸 VC 距离。<<<PAGE 312>>>
- **Mixed VFL Mode**：OS6900-X48C4E 与其他 6900 机型混合 VC 所需模式。<<<PAGE 319>>>

## 第 14 章 自动远程配置（RCL）

- **RCL / Automatic Remote Configuration Download**：无 vcboot.cfg 时经 DHCP+TFTP/FTP 自动下载配置/镜像。<<<PAGE 345>>>、<<<PAGE 348>>>
- **Instruction File（*.alu）**：TFTP 上的指令文件（Keyword:Value）。<<<PAGE 346>>>、<<<PAGE 357>>>
- **Bootup Configuration File**：下载后保存为 vcboot.cfg 的启动配置。<<<PAGE 359>>>
- **AlcatelDebug.cfg**：自动下载的调测配置文件。<<<PAGE 360>>>
- **Script File**：下载后按序执行的命令脚本。<<<PAGE 360>>>
- **auto-config-abort**：人工中止 RCL 的命令。<<<PAGE 356>>>
- **Nearest-Edge Mode**：管理交换机以专用 MAC（01:20:DA:02:01:73）LLDP 通告管理 VLAN 的模式。<<<PAGE 363>>>
- **VLAN 127**：RCL 用 tagged DHCP 广播 VLAN（上行口预定义表）。<<<PAGE 346>>>、<<<PAGE 352>>>
- **DHCP Option 66/67**：TFTP 服务器名与启动文件名。<<<PAGE 354>>>
- **LACP Auto Detection**：RCL 期间检测 LACP PDU 自动建聚合。<<<PAGE 365>>>

## 第 15-17 章 Lightning / Auto Fabric / NTP

- **Lightning Configuration Mode**：出厂交换机 WebView/SSH 快速开局向导（默认 192.168.0.1/24，客户端 192.168.0.200）。<<<PAGE 373>>>
- **JSON 模板（EXPORT/IMPORT）**：Lightning 向导的配置模板文件。<<<PAGE 374>>>
- **Automatic Fabric（auto-fabric）**：自动发现配置 LACP/SPB/MVRP/IP 的特性。<<<PAGE 377>>>、<<<PAGE 383>>>
- **Discovery Window / discovery-interval**：发现窗口与周期间隔（默认 0=禁用）。<<<PAGE 379>>>、<<<PAGE 385>>>
- **config-save（auto-fabric）**：发现配置自动保存（默认 300 秒）。<<<PAGE 379>>>、<<<PAGE 403>>>
- **UNP**：User Network Profiles，支持动态 SPB 服务 profile。<<<PAGE 386>>>
- **SAP**：Service Access Point，绑定接入端口与 SPB 服务的逻辑实体。<<<PAGE 386>>>
- **single-service / auto-vlan profile**：动态 SAP 两种 profile（untagged/每 tag）。<<<PAGE 387>>>、<<<PAGE 404>>>
- **SPB**：Shortest Path Bridging；自动发现建 BVLAN 4000-4003、ECT 1-4。<<<PAGE 386>>>
- **BVLAN / Control BVLAN**：SPB 骨干 VLAN（4000 为控制）。<<<PAGE 386>>>
- **MVRP**：Multiple VLAN Registration Protocol；仅 flat STP 下支持。<<<PAGE 388>>>
- **LBD**：Loopback Detection，SAP 口环回检测。<<<PAGE 387>>>
- **NTP**：Network Time Protocol，时间同步协议。<<<PAGE 406>>>
- **Stratum**：距时间源的层级（1 为直连）。<<<PAGE 411>>>
- **minpoll/maxpoll**：NTP 轮询区间指数（2^n，默认 6/10）。<<<PAGE 415>>>
- **burst / iburst**：NTP 加速同步的包突发模式。<<<PAGE 416>>>
- **ntp broadcast-client / broadcast-delay**：广播客户端模式与其时延（默认 4000 μs）。<<<PAGE 414>>>、<<<PAGE 407>>>
- **ntp.keys**：NTP 认证密钥文件（/flash/network/ntp.keys）。<<<PAGE 417>>>
- **trusted key**：标记可信的 NTP 密钥 ID。<<<PAGE 417>>>
- **preempt（NTP）**：服务器可抢占关联模式。<<<PAGE 416>>>
