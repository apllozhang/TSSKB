# principles.md — 原理机制候选（《OmniSwitch AOS Release 810R04 Switch Management User Guide》）

- 页码为 fulltext.md 中真实的 `<<<PAGE N>>>` 标记页（PDF 页码），非印刷页码。
- 摘录保留英文原文。

## 系统目录 / Flash

- **P1 出厂默认目录结构与回滚设计**：/flash 下有 certified（已认证最可靠文件）、working（新文件待验证）、network（swlog）、switch、system 等目录。<<<PAGE 52>>>
- **P2 certified 目录不可直接写**："The certified directory contains files that have been certified by an authorized user as the default files for the switch... Configuration changes CAN NOT be saved directly to the certified directory." <<<PAGE 94>>>
- **P3 RUNNING CONFIGURATION 位于 RAM**："The RUNNING CONFIGURATION is the current operating configuration of the switch obtained from the directory the switch booted from in addition to any additional configuration changes made by the user. The RUNNING CONFIGURATION resides in the switch's RAM." <<<PAGE 94>>>
- **P4 正常重启选择规则**："At the time of a normal boot (cold start or by using the reload command) the switch will reboot from CERTIFIED directory if contents (images and vcboot.cfg) are different from the RUNNING DIRECTORY. If contents are the same, the switch will reboot from the RUNNING DIRECTORY." <<<PAGE 95>>>
- **P5 软件回滚机制**：目录结构本身提供回滚能力——新镜像先放 working/用户目录测试，验证可靠后再 copy running certified；不可靠时可 "rolled back" 到 certified 旧版本。<<<PAGE 95>>>
- **P6 vcboot.cfg 是启动配置文件**："A configuration file, named vcboot.cfg, which is an ASCII-based text file, sets and controls the configurable functions inherent in the image files provided with the switch... When the switch boots, it looks for the file called vcboot.cfg." <<<PAGE 94>>>
- **P7 镜像文件（archive files）**：Image files 是 ALE 专有代码、"the repository of several smaller files grouped together under a common heading"，用户不可配置、只能升级。<<<PAGE 94>>>
- **P8 文件系统工具**：ls/pwd/cd/mkdir/cp/rmdir/rm/vi/chmod/freespace/fsck/newfs 构成文件与目录管理三组命令（目录/文件/工具）。<<<PAGE 53>>>、<<<PAGE 59>>>
- **P9 fsck 修复模式**：fsck 有 no-repair 与 repair 两选项；repair 会修复文件系统错误并显示诊断信息。<<<PAGE 59>>>
- **P10 AOS LINUX 命令直通**："select Linux tools are exposed directly in the CLI via a wrapper so it need to enter su mode to use them is not required. This initial LINUX command set includes watch, cut, paste, and tee." <<<PAGE 60>>>
- **P11 文件传输四模式**：交换机可作为 FTP/SFTP/SCP 服务器、TFTP 客户端、FTP/SFTP 客户端；镜像用 binary 模式传、配置文件用 ASCII 模式传。<<<PAGE 62>>>
- **P12 TFTP 限制原理**："A TFTP server does not prompt for a user to login and only one active TFTP session is allowed at any point of time." <<<PAGE 64>>>

## 升级 / 代码管理

- **P13 标准升级流程**：上传新镜像到 Running 目录 → reload → 验证 → certify；VC 场景 Master 会先把镜像拷给 Slave 再统一重启。<<<PAGE 22>>>（page 1-5）
- **P14 ISSU 原理（VC）**：按 chassis-id 从低到高逐台重启 Slave，最后重启 Master，"To restore the role of Master to the original Master chassis the current Master can be rebooted"。<<<PAGE 22>>>
- **P15 ISSU 验证文件**："The Validation File contains the information required to validate that an ISSU upgrade is possible. An ISSU upgrade is dependent upon the current version of software on the switch and the version of software the switch is being upgraded to." <<<PAGE 24>>>（page 1-8）
- **P16 ISSU 后 NI 复位**：模块化机箱 ISSU 后 NI 必须复位，"If the NIs are not reset by the time the NI reset timer expires, they will be reset individually by the system in ascending order beginning with slot 1." <<<PAGE 24>>>（page 1-9）
- **P17 升级前维护基线**：升级前清旧 tech-support 文件、检查 /pmd 目录、确认 certified/synchronized、采集 show tech-support 基线。<<<PAGE 23>>>（page 1-7）
- **P18 ALE Secured Code / ASLR**："In AOS 8.6.R01, ALE has adopted address system layout randomization (ASLR) as a standard feature. ASLR results in a unique memory layout of the running software each time the OmniSwitch reboots to impede or prevent software exploitation." <<<PAGE 65>>>
- **P19 签名镜像**："Using RSA-2048 and SHA-256, AOS images are signed with a private key allowing AOS to verify the signature with a corresponding public key during reload." 8.10R1 起公钥与中间 CA 自动预置。<<<PAGE 66>>>
- **P20 Secure Boot**："Secure Boot is a important security mechanism that ensures an OmniSwitch boots with only verified and trusted software." 需升级 u-boot/ONIE/BIOS。<<<PAGE 66>>>
- **P21 包管理器（pkgmgr/appmgr）框架**："Package manager (pkgmgr) - responsible for validation, extraction and installation of the non-AOS Debian packages on the AOS switch. Application manager (appmgr) - responsible for launching... without the need for the system reboot." <<<PAGE 85>>>
- **P22 包版本兼容语法**："The sign '>=' indicates that the package is compatible for AOS release version greater than or equal to the version displayed in 'Compatible release'." <<<PAGE 85>>>
- **P23 安装持久化**："After the package is installed successfully, use the write memory command to save the installation permanently." 未保存则重启/VC takeover 后丢失。<<<PAGE 87>>>
- **P24 升级包二进制备份与回滚**：Upgrade 类包（NTPD/SNMP/OpenSSH）安装时备份现有二进制，"The backed up binaries and libraries are restored during package removal and commit"；Patch 类（OpenSSL/OpenSSH）移除后需重启回固件版本。<<<PAGE 86>>>、<<<PAGE 88>>>

## License

- **P25 License 安装流程**：myportal 生成 license 文件（绑定 serial+MAC）→ 存 /flash → license apply → 重启（部分 license 免重启）→ show license-info 验证。<<<PAGE 66>>>
- **P26 License 写入 EEPROM**："Once the license is applied, it is written to the EEPROM and the license file is no longer needed." <<<PAGE 67>>>
- **P27 Premium 捆绑 license**："A premium (bundle) software license can be considered as a single super set of more than one software license." 子 license 分 Per Node / Match（VC 全员一致）/ Local-Only 三种行为。<<<PAGE 69>>>
- **P28 VC 子 license 一致性检查**："a license check is performed for all chassis IDs in the VC. If there is no sub-license parity match, the feature/configuration is not enabled." <<<PAGE 70>>>
- **P29 SILOS 架构**：SILOS（Site Local Licensing Server）为 Debian 包，运行在一台交换机/VC 上作为 license 服务器；SWLIC（Switch Local Licensing client）跑在每台需要的交换机上，"SWLIC will establish secure communication with the on-premises SILOS license server using secure MQTT (Message Queuing Telemetry Transport) protocol." <<<PAGE 71>>>
- **P30 SILOS 断连撤销规则**："If the connectivity loss lasts for 15 days, the license allocation is automatically revoked. If the demo period has not yet been fully used, the client will fall back to the remaining demo period." <<<PAGE 72>>>
- **P31 SILOS demo 期**："A demo period of 15 days is activated when a licensed feature is present in the system. The demo period will be extended an additional 15 days (total 30 days) when SILOS server and clients are configured regardless if a license key is applied on the server or not." <<<PAGE 72>>>
- **P32 SILOS VC 分裂宽限期**：license 所绑单元脱离 VC 触发 15 天 grace period，过期未回归则移除该 license 并发 trap。<<<PAGE 73>>>
- **P33 Site vs Node license**：Site license 浮动共享最多 4 个网络节点；Node license 一节点（standalone 或最多 8 单元 VC）一个。<<<PAGE 73>>>、<<<PAGE 74>>>

## 登录 / 会话 / EMP

- **P34 管理面默认锁定**："Management access is disabled (except through the console port) unless specifically enabled by a network administrator." 各接口需 aaa authentication 解锁。<<<PAGE 29>>>（page 2-1）
- **P35 登录默认参数**：session login-attempt 默认 3 次；session login-timeout 55 秒；session timeout（不活动超时）4 分钟。<<<PAGE 29>>>（page 2-2 之前表格）
- **P36 admin 恒可走 console**："Access to managing the switch is always available for the admin user through the console port, even if management access to the console port is disabled." <<<PAGE 166>>>、<<<PAGE 144>>>
- **P37 EMP 双层地址模型**：共享 EMP IP 存 vcboot.cfg（跨 CMM），每 CMM 的 NVRAM 地址可选；"All the EMP IP addresses and CMM's IP addreses must be in the same subnet." "There is no dedicated routing table for the EMP interface." <<<PAGE 35>>>
- **P38 USB Ethernet Dongle 等同 EMP**："This interface is treated just like an EMP interface. All functions and CLIs related to EMP are applicable to the USB-to-Ethernet dongle." 芯片 ASIX 8817/RealTek RTL8153。<<<PAGE 35>>>
- **P39 SSH 认证四阶段**：Protocol Identification（可读标识串）→ Algorithm and Key Exchange（密钥协商+主机认证）→ Authentication（服务器列出可用方法）→ Connection。<<<PAGE 40>>>、<<<PAGE 41>>>
- **P40 SSH 主机密钥存储**：密钥位于 /flash/system（ssh_host_key、ssh_host_dsa_key、ssh_host_rsa_key 及 .pub）；换钥需重启生效。<<<PAGE 40>>>
- **P41 SSH PKA 安装**：ssh-keygen 生成密钥对 → scp 公钥到 /flash/system → installsshkey user file →（可选）ssh enforce-pubkey-auth 强制公钥认证；revokesshkey 撤销。<<<PAGE 41>>>、<<<PAGE 42>>>
- **P42 登录横幅机制**：/flash/switch 下文本文件 + session {cli|ftp|http} banner 命令；pre_banner.txt 为登录前文本；"The banner text files located in the /flash/switch directory are not synchronized across CMMs"。<<<PAGE 43>>>、<<<PAGE 44>>>
- **P43 DNS 解析器**：最多 3 个 IPv4 + 3 个 IPv6 域名服务器轮询；三步启用：ip domain-name → ip domain-lookup → ip name-server。<<<PAGE 46>>>
- **P44 FIPS 模式**："When FIPS mode is enabled on OmniSwitch, FIPS 140-2 compliant encryption is used by the OmniSwitch devices in the various management interfaces such as SFTP, HTTP, SSh and SSL." 仅 SNMPv3 SHA+AES，"The FIPS mode is enabled/disabled only with a reboot of the switch." <<<PAGE 46>>>、<<<PAGE 47>>>
- **P45 并发会话限制**：session session-limit 可对 FTP/SSH/Telnet/HTTP(S) 限制并发数，超限拒绝。<<<PAGE 183>>>（page 8-19）

## CLI 机制

- **P46 单级命令体系**："the OmniSwitch CLI is different from industry standard interfaces in that it uses a single level command hierarchy... The OmniSwitch will accept any CLI command at any time because there is no hierarchy." <<<PAGE 122>>>（page 5-2）
- **P47 在线/离线配置**：CLI 命令可写入 ASCII 文本文件，configuration apply 应用；"This ability to store comprehensive network information in a single text file facilitates troubleshooting, testing, and overall network reliability." <<<PAGE 122>>>
- **P48 Bash 作为 CLI 输入层**："AOS uses the Bash shell for CLI input. This could result in certain special characters being interpreted by Bash instead of being applied to an AOS command or password." 特殊字符需单引号。<<<PAGE 123>>>
- **P49 部分关键字补全/缩写**：Tab 补全、最短唯一前缀缩写（sh vl）；"session cli-auto-complete-space enable" 可启用空格补全（默认关）。<<<PAGE 124>>>、<<<PAGE 125>>>
- **P50 ? 帮助按命令集分组**：`?` 列出按 Command Set 分组的关键字。<<<PAGE 125>>>
- **P51 历史与 bang 调用**：history 显示编号列表；`!4` 重放 4 号命令；`!!` 重放上一条。<<<PAGE 126>>>、<<<PAGE 127>>>
- **P52 命令日志（command-log）**：记录命令全文、用户名、时间、来源 IP、执行结果（SUCCESS/ERROR），写入 /flash 的 command.log；默认禁用。<<<PAGE 127>>>、<<<PAGE 128>>>
- **P53 屏幕与提示符定制**：tty 行列（10-150 行 / 20-150 列）；session prompt default 改 CLI 提示符。<<<PAGE 130>>>

## 配置文件管理

- **P54 配置文件三种生成方式**：工作站文本编辑器上传 / configuration snapshot 抓取 / 交换机内置 vi 编辑。<<<PAGE 136>>>（page 6-5）
- **P55 定时应用会话**：configuration apply 支持 at（定时）与 in（倒计时）；"Timer sessions are very useful for certain management tasks, especially synchronized batch updates." <<<PAGE 136>>>
- **P56 错误文件机制**：应用含错文件时生成 `<file>.n.err`；configuration error-file-limit 控制保留数量，超限删最旧。<<<PAGE 137>>>
- **P57 语法预检**："The configuration syntax check command is used to detect potential syntax errors contained in a configuration file before it is applied to the switch." <<<PAGE 137>>>
- **P58 快照（snapshot）机制**：configuration snapshot 按特性族导出非默认运行配置为 asc.n.snap；注释行以 `!` 开头被忽略；可编辑后作为配置文件复用。<<<PAGE 139>>>
- **P59 配置备份/恢复**：configuration backup 将 banner、当前 running 目录 vcboot.cfg、userTable 收集为 /flash/config-recovery 下的 tar，最多保留 10 份；restore 需重启生效。<<<PAGE 138>>>
- **P60 恢复出厂（reset-to-factory）三档**：config（清配置保留镜像/license/证书）、retain-vc（另保留 vcsetup.cfg）、all（再清 NVRAM、/flash/switch、/flash/system、license、证书）；"The switch must be certified and synchronized to activate or schedule this feature." <<<PAGE 141>>>

## 用户 / AAA 安全

- **P61 账户三元组**："A user account includes a login name, password, and user privileges. These privileges determine whether the user has read or write access to the switch and which command domains and command families the user is authorized to execute." 分区管理即 partitioned management。<<<PAGE 145>>>（page 7-3）
- **P62 双内置账户**：admin/switch（初始仅 console 可用、SNMP 不可用、除密码外不可修改）；secureadmin（首登强制改密；登录即切换增强模式并禁用 admin）。<<<PAGE 145>>>
- **P63 default 账户是模板**："The default user account on the switch is used for storing new user defaults for privileges and profile information. This account does not include a password and cannot be used to log into the switch." <<<PAGE 150>>>
- **P64 用户设置实时入库存**："Unlike other settings on the switch, user settings configured through the user and password commands are saved to the switch configuration automatically... At bootup, the switch reads the database file for user information (rather than the vcboot.cfg file)." <<<PAGE 150>>>
- **P65 密码策略体系**：全局密码策略含最小长度（默认 8）、禁含用户名（默认 enable）、大小写/数字/符号最小数量（各 1）、过期、历史（默认 4）、最小年龄。<<<PAGE 144>>>、<<<PAGE 153>>>
- **P66 锁定三参数**：lockout-window（观察窗）、lockout-threshold（阈值）、lockout-duration（锁时长）；均默认 0（不限制）；"Only the admin user is allowed to configure user lockout settings. The admin account is protected from lockout." <<<PAGE 156>>>、<<<PAGE 157>>>
- **P67 权限域/族两级模型**：read-only（show）/read-write（配置+show）；命令族是命令域子集，如 domain-network 包含 ip rip ospf bgp vrrp 等。<<<PAGE 159>>>
- **P68 用户级 SNMP 认证等级**：user 命令可设 no auth / sha / md5 / sha+des / md5+des / sha+aes / sha224 / sha256；修改 SNMP 等级必须重输密码（哈希依赖认证等级）。<<<PAGE 161>>>
- **P69 priv-password 双密码**："Two different passwords are supported for a SNMPv3 user, one for switch login and another for SNMPv3 frames authentication/encryption using the priv-password parameter." <<<PAGE 214>>>（page 10-12）
- **P70 ASA 认证链**：aaa authentication <iface> server1 server2 ... local；"The switch uses only one server for authentication—the first available server in the list... If local is specified, it must be last in the list." <<<PAGE 173>>>（page 8-9）
- **P71 exit-on-fail**："if the user information is not found on the first available server then the authentication request will fail. By default exit-on-fail is set to 'enable' for all access types." <<<PAGE 171>>>（page 8-7）
- **P72 认证服务器与接口矩阵**：RADIUS 支持 Telnet/FTP/HTTP/SSH；LDAP 与 local 另支持 SNMP。<<<PAGE 173>>>
- **P73 外部服务器失效回退**："If external servers are configured for other management interfaces... but the servers become unavailable, the switch will poll the local user database for login information." <<<PAGE 169>>>
- **P74 计费（accounting）**：aaa accounting session 指定 RADIUS/LDAP/local（Switch Logging）链，记录会话与登录尝试。<<<PAGE 175>>>
- **P75 ASA 增强模式密码加盐**："When a new user is created or a password changed, a 16-byte random salt is concatenated with the password and hashed. It will store both the salt and the hash to the local user database." <<<PAGE 180>>>（page 8-16）
- **P76 增强模式镜像完整性**：reload 自动比对镜像 SHA256 与 running 目录 imgsha256sum 文件；不匹配则回退 certified，均失败则循环重启，需 USB 灾备恢复。<<<PAGE 178>>>（page 8-14）
- **P77 增强模式 vcboot.cfg 完整性**：write memory 计算 vcboot.cfg 的 SHA256 存 /flash；重启校验失败则"boot up with an empty configuration file"并回退 certified。<<<PAGE 179>>>
- **P78 IP 锁定阈值**："aaa switch-access ip-lockout-threshold" 默认 6；超阈 IP 永久封禁，最多 128 个 banned IP，满后删最旧；aaa switch-access banned-ip release 解封。<<<PAGE 180>>>
- **P79 管理站白名单**：management-stations 启用后仅允许配置 IP 访问，最多 64 个。<<<PAGE 182>>>
- **P80 priv-mask 按接入类型限权**：aaa switch-access priv-mask ssh/telnet/console/http(s) read-only|read-write <族>；"The read-write privilege can be applied only for HTTP and HTTPS access types." <<<PAGE 181>>>
- **P81 JITC 模式**：军用认证要求——密码≥15 字符、不得与近 5 次相同、默认 60 天过期、SSH 每 GB/60 分钟 rekey、Diffie-Hellman-Group14-SHA1、升级前验签等。<<<PAGE 184>>>、<<<PAGE 185>>>
- **P82 Crypto Strong Security**：启用后禁弱算法（SHA/MD5/SHADES/MD5DES/SHAAES），仅允许 SHA224/256/384 系列。<<<PAGE 186>>>
- **P83 超级用户密码**：super-user-password 仅 admin 可设；"The super-user password cannot be recovered. In the case of a forgotten password a factory reset will need to be performed." <<<PAGE 186>>>
- **P84 多会话管理**：who 列会话（session 0 恒为 console）、whoami 看自身、kill <n> 终止他人会话（需管理权限）。<<<PAGE 163>>>、<<<PAGE 164>>>

## CMM / 机箱冗余

- **P85 CMM 冗余模型**："When two CMMs are running one CMM has the primary role and the other has the secondary role at any given time. The primary CMM manages the current switch operations while the secondary CMM provides backup (also referred to as 'fail over')." <<<PAGE 99>>>（page 4-7）
- **P86 运行配置自动同步**：主 CMM 的 running-configuration 自动同步到 secondary CMM；certified 需 copy flash-synchro / copy running certified flash-synchro 手动同步。<<<PAGE 99>>>、<<<PAGE 101>>>、<<<PAGE 110>>>
- **P87 takeover**：takeover 让 secondary 接管；"It's normal for the NIs to indicate a DOWN status for approximately 10 seconds while establishing communication to the secondary CMM, however this does not affect the flow of traffic." <<<PAGE 111>>>
- **P88 certify-on-reboot**：强制下次重启从 working 目录加载并自动 certify；失败则回退 certified；仅 VC-of-1 支持。<<<PAGE 107>>>
- **P89 定时重启**：reload all in 3:03 / at 20:00 june 30；reload cancel 取消；show reload 查看状态。<<<PAGE 103>>>
- **P90 USB 自动拷贝签名机制**："In order to prevent an accidental upgrade, a file named aossignature must be stored on the USB flash drive as well as having a directory with the same name as the product family"；重启后 auto-copy 自动关闭。<<<PAGE 113>>>、<<<PAGE 114>>>
- **P91 USB 灾备**：USB 根放 Trescue.img + 平台目录（6900/certified 等）→ 重启进恢复 → 'run rescue'；ONIE 设备用 Onie Rescue + onie-nos-install。<<<PAGE 116>>>
- **P92 镜像完整性人工校验**：image integrity check 比对目录镜像与 key file 的 SHA256；image integrity get-key 显示哈希。<<<PAGE 118>>>

## SNMP / WebView

- **P93 SNMP 模型**："The SNMP model defines two components, the SNMP Manager and the SNMP Agent." Agent 维护 MIB 变量，NMS 用 Get/GetNext/GetBulk/Set 操作，trap/inform 为主动通知。<<<PAGE 208>>>（page 10-6）
- **P94 SNMP 安全等级链**：no security → authentication set → authentication all → privacy set → privacy all（默认）→ traps only；等级决定接受哪些请求。<<<PAGE 215>>>（page 10-13）
- **P95 community string 映射**：v1/v2c 请求的 community 必须映射到本地用户（snmp community-map）；"A community string inherits the security privileges of the user account that creates it." <<<PAGE 212>>>
- **P96 SNMPv3 加密认证组合**：认证 SHA/MD5 + 加密 DES/AES；"The encryption key is derived from the authentication key, which is used to decrypt the PDU on the switch's side." <<<PAGE 213>>>、<<<PAGE 214>>>
- **P97 engine ID 生成规则**：默认 = 企业值 + 交换机 base MAC（如 8000195603+2c:fa:a2:13:e4:02）；可改为 IPv4/IPv6/MAC/text。<<<PAGE 216>>>
- **P98 trap 过滤两法**：按用户命令族（读权限收回即屏蔽对应 trap）或按 trap ID（snmp trap filter <ip> <id...>）。<<<PAGE 217>>>（page 10-15）
- **P99 trap 重放与吸收**：snmp trap replay 重发已存 trap（可指定序号起点）；"When trap absorption is enabled, traps that are identical to traps previously sent will be suppressed." <<<PAGE 218>>>
- **P100 TSM/TLS over SNMP**："To send SNMP traps over TLS connection, the SNMP station needs to be configured with TSM user along with certificate identities. These configurations are supported only for SNMP version 3." TSM 启用时丢弃 USM 请求。<<<PAGE 209>>>
- **P101 WebView 架构**：内嵌交换机的 Web 管理界面，URL 为 https://<ip>/new#/；"WebView access supports only partition manager family based authorization"；默认 force-ssl enable、443/80 端口。<<<PAGE 190>>>、<<<PAGE 191>>>、<<<PAGE 192>>>
- **P102 WebView WLAN 虚拟 IP 自动学习**："The OmniSwitch acquires the Cluster Virtual IP address from the LLDP TLV received from the Access Points (APs)." precedence 默认 lldp。<<<PAGE 199>>>

## OmniVista Cirrus / NaaS

- **P103 Cirrus 零接触组件**：DHCP Server（Option 43）、Activation Server（默认 license.ovng.myovcloud.com）、OV Cirrus 实例、Proxy、NTP、Image Server、VPN Server。<<<PAGE 226>>>
- **P104 无配置默认上云**："When the OmniSwitch is booted up for the first time, the switch will not have a [(vc)boot.cfg] configuration file. Hence, OmniVista Cirrus is enabled by default." 已有 vcboot.cfg 需 cloud-agent admin-state enable。<<<PAGE 224>>>
- **P105 自动管理特性启动顺序**：Auto VC → RCL（远程配置下载）→ Auto Fabric → Lightning/Cirrus agent；有 (vc)boot.cfg 则跳过 auto VC 与 RCL。<<<PAGE 230>>>
- **P106 NTP 缺省池**："The four available NTP pool servers are 'clock0.ovcirrus.com','clock1.ovcirrus.com', 'clock3.ovcirrus.com' and 'clock4.ovcirrus.com'." DHCP/NTP 均缺失时配置。<<<PAGE 228>>>
- **P107 NaaS license 模型**：Node Locked Permanent / Node Locked Subscription；四类订阅 Essential（默认）/ Advanced / Management / Upgrade；Management 过期走 30 天 grace 再 degraded，Upgrade 过期立即 degraded。<<<PAGE 232>>>
- **P108 NaaS 三类宽限**：Bootup 无 license 45 天；无连接有效 license 30 天；订阅到期默认 30 天。<<<PAGE 233>>>
- **P109 Capex 判定规则**：AOS 升级重启后按序列号连 License Activation Server；Unknown 时按制造日期（2021-06-01 前=Capex，之后=Undecided Capex 周期 call-home 30 分钟）。<<<PAGE 233>>>
- **P110 Thin Switch 模式**："In this mode no configuration can be saved in the 'Running' directory of the switch. Only the vcboot.cfg with minimal network reachability configuration is stored"；模式由 OmniVista 激活响应下发，交换机自身不感知。<<<PAGE 240>>>
- **P111 Cirrus LAN 管理推送模型**："LAN devices periodically push data or respond to on-demand requests initiated by OmniVista Cirrus. The configuration of switches within this system is facilitated through MQTT... rather than SNMP protocol." <<<PAGE 241>>>
- **P112 Cirrus Agent 组件**：Monitoring Agent（本地 REST API 采集 + MQTT 上报，JSON 配置文件定义采集组/间隔）与 Config Agent（订阅 MQTT topic 执行云侧配置）；以 Debian 包经 pkgmgr 安装。<<<PAGE 241>>>

## Web Services / 脚本 / AMS

- **P113 REST 双粒度**："The Web Services interface provides two levels of granularity, either through direct handling of MIB variables or using the embedded CLI commands to configure the switch." <<<PAGE 246>>>（page 12-2）
- **P114 REST URL 结构**：`<http|https>://<ip>/<domain>/<URN>?<vars>`；domain ∈ {mib, cli, info}；动词 GET/PUT/POST/DELETE。<<<PAGE 247>>>
- **P115 响应媒体类型**：application/vnd.alcatellucentaos+json / +xml；响应含 domain/diag/error/output/data。<<<PAGE 247>>>、<<<PAGE 249>>>
- **P116 REST 禁缓存头**：Cache-Control: no-cache, no-store / Pragma: no-cache / Vary: Content-Type。<<<PAGE 248>>>
- **P117 Python API 库**：AOSAPI + AOSConnection 依赖注入；login/logout/query/put/post/delete/success/diag。<<<PAGE 260>>>、<<<PAGE 262>>>
- **P118 CLI 脚本=Bash**："The AOS CLI relies on Bash scripting, it can be leveraged for creating CLI scripts without the need for an external tool." 循环/变量/函数/shift/$? 可用。<<<PAGE 265>>>
- **P119 嵌入式 Python 事件绑定**："administrators to create Python scripts and associate these scripts with specific traps. When the traps are generated by the switch, the pre-configured scripts will be run on the switch." 脚本须存 /flash/python。<<<PAGE 270>>>
- **P120 AMS 发布订阅**："AMS uses publish-subscribe messaging as the underlying protocol for communication among switches... The role of broker is played by OmniVista or by an OmniSwitch if OmniVista is not present." Broker 默认端口 8883。<<<PAGE 272>>>、<<<PAGE 273>>>
- **P121 AMS Topic 层级**：COMMUNITY_NAME/APPLICATION/APPLICATION_SUB_CONFIG；订阅 `COMMUNITY_NAME/#` 收全社区消息；Config-DB 负责新成员"configuration replay"。<<<PAGE 273>>>
- **P122 AMS Broker 信息获取两途**：DHCP VSO option 43（option 43 140 IP-address=...）或手改 /flash/working/pkg/ams/ams-broker.cfg 的 -h。<<<PAGE 273>>>、<<<PAGE 274>>>
- **P123 AMS Broker 冗余基于 VRRP**："It uses the VRRP protocol to handle the broker fail over"；客户端用同一 VIP 重连。<<<PAGE 278>>>
- **P124 OpenFlow 逻辑交换机**："An OpenFlow logical switch consists of a portion of the switch's resources that are managed by an OpenFlow Controller (or set of Controllers) via the OpenFlow Agent... Spanning tree and source learning do not operate on OpenFlow assigned ports." <<<PAGE 281>>>
- **P125 OpenFlow Hybrid(API) 模式**："the logical switch acts as an interface through which the Controller may insert flows. These flows are treated as QoS policy entries and offer the same functionality." <<<PAGE 281>>>
- **P126 Nutanix 插件**：Debian 包 yos-nutanix-v1.deb，"The Nutanix Plug-in automatically pulls the necessary configuration from the Nutanix Prism and applies it to the OmniSwitch"；仅 OS6900 部分型号支持。<<<PAGE 284>>>
- **P127 PROFINET 定位**：OmniSwitch 作为 PROFINET IO-Device、CC-B 一致性等级；"In this release OmniSwitch only supports Acyclic data or non-real time TCP/IP based communication." <<<PAGE 288>>>、<<<PAGE 289>>>

## 虚拟机箱（VC）

- **P128 VC 本质**："A Virtual Chassis is a group of switches managed through a single management IP address that operates as a single bridge and router." 免 STP/VRRP。<<<PAGE 300>>>（page 13-1）
- **P129 vcsetup.cfg vs vcboot.cfg**：前者是单机入 VC 的设置（Chassis ID、Group、priority、control VLAN、EMP、VFL），后者是 VC 整体配置（L2/L3/管理）。<<<PAGE 306>>>（page 13-7）
- **P130 Master 选举五准则**（高到低）：现任 Master → 最高 priority（默认 100）→ 最长 uptime → 最小 Chassis ID → 最小 MAC。<<<PAGE 310>>>（page 13-11）
- **P131 Slave 同步规则**："if there is a mismatch between the Master and Slave vcboot.cfg or images files, the Master will overwrite the files on the Slave chassis and the Slave will automatically reboot." <<<PAGE 307>>>
- **P132 控制 VLAN**："A special type of VLAN reserved for the inter-chassis communication exchange... Only VFL ports are assigned to this VLAN"（默认 4094）。<<<PAGE 306>>>、<<<PAGE 302>>>
- **P133 IS-IS VC 协议**："Proprietary protocol for managing a Virtual Chassis mesh topology... determining adjacencies, loop-detection and the shortest path between members of the VC." <<<PAGE 306>>>
- **P134 RCD 分裂检测**：各机箱经 EMP 口周期通告；VFL 全断时 former Slave "will shutdown all its front-panel user ports to prevent duplicate IP and chassis MAC addresses"。<<<PAGE 310>>>、<<<PAGE 311>>>
- **P135 VCSP 分裂保护**：经 helper 交换机的专用 linkagg 传 VCSP PDU；正常 3 秒一帧，尺寸变化时 50ms 一帧发 3-10 秒；收到 master MAC 不匹配的 3-5 帧后进 protection state（面板口 operationally down，仅 VCSP linkagg 保留）。<<<PAGE 340>>>、<<<PAGE 341>>>
- **P136 VCSP 恢复**：手动（guard-timer=0，重启后禁/启 VCSP 清状态）或自动（VFL 恢复后 sub-VC 重启，Master 等 60 秒逐台拉起）。<<<PAGE 342>>>
- **P137 Auto-VFL 机制**：自动 VFL 端口（默认端口集或 auto-vf-link-port 指定）自动分配 VFL ID，"Multiple ports connected to the same peer chassis will be aggregated and assigned the same VFL ID." <<<PAGE 334>>>、<<<PAGE 337>>>
- **P138 自动 Chassis ID**：无 vcsetup.cfg 启动时临时用 ID 1，VC 发现与选举后由 Master 统一分配唯一 ID 并写回 vcsetup.cfg，Slave 重启生效；"chassis with configured chassis id will always win over chassis with temporary chassis id"。<<<PAGE 336>>>
- **P139 VFL 模式互斥**：auto/static 两模式，"Chassis must have the same VFL mode to form a VC"；模式可运行时切换无需重启。<<<PAGE 333>>>
- **P140 VC 拓扑变更 trap 与写配置确认**：write memory 时比对当前与保存拓扑，元素缺失则警告"possible configuration purge"需确认。<<<PAGE 313>>>
- **P141 VFL 16 字节头开销**："Since all packets that traverse the VFL have an additional 16 byte header prepended to the packet this reduces the effective bandwidth of a given VFL port." <<<PAGE 322>>>

## 自动配置（RCL）/ Lightning / Auto Fabric / NTP / 其他

- **P142 RCL 触发条件**：无 vcboot.cfg、bootup 完成端口就绪、能经 VLAN 1 / Management VLAN / VLAN 127 连到 DHCP 与 TFTP。<<<PAGE 349>>>
- **P143 RCL 文件链**：DHCP（Option 66 TFTP、67 文件名）→ instruction file（*.alu，Keyword:Value 格式）→ FTP/SFTP 主/备服务器下载 image/config/debug/script/license；密码与用户名相同。<<<PAGE 348>>>、<<<PAGE 358>>>
- **P144 DHCP 客户端轮换机制**："initial DHCP client starts with untagged VLAN 1... waits for 30 seconds"；失败转 tagged VLAN 127 再 30 秒，交替；收到 LLDP 管理 VLAN 通告则切换；收到 LACP PDU 则自动建聚合。<<<PAGE 361>>>
- **P145 DHCP 服务器偏好序**：OVCloud > OmniVista > OXO ("alcatel.a4400.0") > 其他；高优先响应覆盖低优先，30 秒窗口等待。<<<PAGE 362>>>
- **P146 Nearest-Edge 模式**：管理交换机 LLDP 以专用组播 MAC 01:20:DA:02:01:73 发 Port VLAN ID TLV，"Newly connected switches without a vcboot.cfg file receive the Nearest-Edge LLDP PDUs, discover the Management VLAN, tag the port with that VLAN ID, and create a DHCP client interface on the Management VLAN." <<<PAGE 363>>>、<<<PAGE 364>>>
- **P147 LACP 自动检测**："The Remote Configuration Manager on OmniSwitch detects any LACP PDUs on any ports and configures a link aggregate automatically during Automatic Remote Configuration." 聚合加入 VLAN 127(tagged)+VLAN 1(untagged)，完成后删除。<<<PAGE 365>>>
- **P148 Lightning 模式默认 IP**：交换机配 192.168.0.1/24（VLAN 1），对 1/1/1、1/1/2、EMP、USB dongle 提供 DHCP（分配 192.168.0.200/24），HTTPS/SSH 连 192.168.0.1 进入向导。<<<PAGE 373>>>（page 15-2）
- **P149 Lightning 终止三途径**：超时（6360 等 2 小时 / 6860 等 1 小时）、WebView 显式禁用、检测到 CLI 登录会话隐式终止。<<<PAGE 373>>>、<<<PAGE 374>>>
- **P150 Auto Fabric 发现顺序**："The switch will attempt to discover and automatically set up an LACP configuration... After the LACP discovery process completes... SPB... After the SPB discovery process completes and if MVRP is enabled... MVRP"；IP 协议发现并行。<<<PAGE 380>>>
- **P151 Auto Fabric 端口资格**："The port has no previous configuration that would prevent the port from joining a link aggregate, forming an SPB adjacency, serving as a UNP SPB access port, and enabling MVRP"（default port state）。<<<PAGE 385>>>
- **P152 SPB 发现预置**："BVLANs 4000-4003 are created and mapped to Equal Cost Tree (ECT) IDs 1-4, respectively. BVLAN 4000 will serve as the control BVLAN"；bridge priority 置 0x8000。<<<PAGE 386>>>
- **P153 动态 SAP 双 profile**：single-service（untagged）与 auto-vlan（每个收到的 VLAN tag 建一个 SAP，默认）；端口级 set-profile 优先于全局 default-profile。<<<PAGE 387>>>、<<<PAGE 404>>>
- **P154 MVRP 与 STP 联动**："MVRP is supported only when the switch is operating in the flat Spanning Tree mode. If the switch is running in the per-VLAN (1x1) mode when Automatic Fabric discovery is started for MVRP, the Spanning Tree mode is automatically changed to the flat mode." <<<PAGE 388>>>
- **P155 Auto Fabric IP 自动配置**：已有 IP 接口监听 OSPF/IS-IS Hello，被动学习 Area/Level/计时器；"Automatic IP discovery is designed for use in more simplistic networks." <<<PAGE 389>>>、<<<PAGE 395>>>
- **P156 发现配置保存**：默认不保存；可 write memory 或启用 auto-fabric config-save（默认 300 秒间隔）；"If the discovered configuration is not saved... the learned configuration is lost on the next switch reboot." <<<PAGE 403>>>
- **P157 发现间隔建议**："Setting the discovery interval value to a time that is more than twice the value of the switch MAC address aging time is recommended." <<<PAGE 402>>>
- **P158 NTP stratum 模型**："Stratum is the term used to define the relative proximity of a node in a network to a time source... Stratum 1 is the server connected to the time source itself." <<<PAGE 411>>>
- **P159 NTP 轮询指数**：minpoll/maxpoll 为 2 的幂（默认 6/10，即 64s/1024s，可 3-17）；maxpoll 不得小于 minpoll。<<<PAGE 415>>>
- **P160 NTP burst/iburst**：burst 可达时每轮询周期发 8 包加速同步；iburst 不可达时立即发 8 包加速初始同步。<<<PAGE 416>>>
- **P161 NTP 认证**：MD5/SHA1 密钥文件须在两端（交换机路径 /flash/network/ntp.keys），ntp key load 载入、ntp server key <id> 指定、ntp key <id> trusted 信任；"Untrusted keys, even if they are in the switch memory and match an NTP server, will not authenticate NTP messages." <<<PAGE 413>>>、<<<PAGE 417>>>
- **P162 Keychain 集中密钥管理**："The keychain module is a centralized key management mechanism in AOS. Any module using key management service ensures enhanced security with regular rotation of the keys." 认证通过需活动 key、认证类型、摘要三者一致。<<<PAGE 83>>>
- **P163 系统时钟与 DHCP Option-2**："The user-defined time zone configuration (through CLI, WebView, SNMP) always gets priority over the DHCP server values."；DST 随时区自动启停、不可手工切换。<<<PAGE 78>>>、<<<PAGE 79>>>
- **P164 hash-control 影响面**："Changing the hash control mode affects the hashing algorithm for Link Aggregation, Server Load Balancing and ECMP." <<<PAGE 82>>>
- **P165 U-boot 访问与认证**：仅 admin 可开关；"If the AOS images are not valid or corrupted, switch goes to no response state... the switch must be returned to the factory for repair"（禁访问且镜像损坏时）。<<<PAGE 91>>>
- **P166 ONIE 认证同步范围**："In the case of a VC, the ONIE authentication will be synchronized to all existing units of the VC. The authentication will not be synchronized to any new unit joining the VC." <<<PAGE 92>>>
