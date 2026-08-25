# principles — sol-network-security

## 安全总体理念

- **P1 安全是过程而非产品**：Security is not a tangible product or feature that can be purchased but rather a process that involves the organization's methods for protecting information systems against unauthorized access. <<<PAGE 5>>>
- **P2 多层纵深防御**：Implementing robust network security necessitates a comprehensive strategy employing multiple layers of defense. <<<PAGE 5>>>
- **P3 安全对终端用户须透明**：From an end-user perspective, security must be provided transparently to avoid adding complexity. <<<PAGE 5>>>
- **P4 分层安全框架（用户/设备/应用/网络/IoT 五层）**：At Alcatel-Lucent Enterprise, we recommend an integrated security approach that begins with network integrity, device security, user profiles, application analytics, and subsequently progresses to the levels of IoT containment... <<<PAGE 5>>>
- **P5 IoT 用虚拟容器隔离**：devices are placed in virtual containers using network virtualization techniques... if a breach does occur in one part of the virtual network, it does not affect other applications. <<<PAGE 6>>>
- **P6 Secure By Design / 默认安全**：Alcatel-Lucent Enterprise products follow a secure by design approach... DoS Filtering: By default, the switch filters denial of service (DoS) attacks. <<<PAGE 6>>>
- **P7 及时打补丁**：Since vulnerabilities are publically disclosed they are also known by malicious attackers who will exploit these vulnerabilities, which is why it is critical to apply these patches as soon as they are available. <<<PAGE 7>>>
- **P8 订阅安全通告**：Recommendation: Subscribe to ALE security advisory alerts. <<<PAGE 7>>>
- **P9 物理访问是安全边界**：Physical access to switches, APs, and wiring closets allows a malicious actor to power cycle a switch, remove or replace critical components, or to alter cable wiring... It is recommended that critical switches be housed in locked rooms with limited access. <<<PAGE 8>>>
- **P10 人员安全意识培训**：organizations have to adapt to these changes and educate employees on maintaining a good cybersecurity hygiene. <<<PAGE 8>>>
- **P11 监控冷/热启动陷阱检测设备重启**：The OmniSwitch's coldStart and warmStart traps should be monitored to detect cycling of critical switches. <<<PAGE 8>>>

## 管理面

- **P12 引导加载器加口令**：Recommendation: Secure U-boot/ONIE access with password authentication. <<<PAGE 9>>>
- **P13 校验镜像完整性**：Recommendation: Signed images feature automatically verifies the integrity of the AOS image. Verifying the integrity of the image manually... is recommended to be done before upgrading your software. <<<PAGE 10>>>
- **P14 带外管理优先**：Recommendation: Setup a dedicated physical Out-Of-Band (OOB) management network separate from the data network... If this is not possible, then in-band management can be configured using a dedicated network segment (VLAN/VRF) but will not provide the same level of security. <<<PAGE 10>>>
- **P15 管理 VRF 隔离并在数据 VRF 关管理端口**：Recommendation: If you are using in-band management, use a separate VRF for management access, and another VRF for data... In the data VRF, disable all management access and the relevant TCP/UDP ports. <<<PAGE 10>>>
- **P16 管理访问白名单化**：Recommendation: Restrict management access to management stations IP addresses. <<<PAGE 11>>>
- **P17 首次开机改默认口令**：Recommendation: Change the "admin" account password at first boot-up and keep it safe. <<<PAGE 11>>>
- **P18 限制控制台访问**：Recommendation: Secure and restrict console access. <<<PAGE 11>>>
- **P19 先全关服务再按需开安全协议**：Recommendation: Disable all IP services and selectively enable required secure protocols. <<<PAGE 12>>>
- **P20 不安全协议必须替换**：Insecure protocols are provided by AOS to support legacy systems. They are not recommended. Secure protocols are available which provide the same type of functionality.（Telnet→SSH、FTP→SFTP/SCP、SNMPv1/2→SNMPv3、HTTP→HTTPS） <<<PAGE 12>>>
- **P21 强制强 SSH 加密套件与 HMAC**：Recommendation: Enforce strong SSH Cipher algorithms and HMAC configuration. <<<PAGE 13>>>
- **P22 SSH 公钥认证**：Recommendation: Use PKA for SSH connections... This significantly enhances security by eliminating password risk and protects against brute-force attacks. <<<PAGE 14>>>
- **P23 限制登录尝试次数防暴力破解**：Recommendation: Minimize the number of login attempts to prevent brute-force attacks. <<<PAGE 14>>>
- **P24 收敛登录与会话超时**：Recommendation: Minimize SSH login grace timeout and session timeout to protect against resource abuse and unauthorized access. <<<PAGE 14>>>
- **P25 配置 IP 锁定阈值**：Recommendation: Configure IP Lockout Threshold to protect switch access from brute-force attacks. <<<PAGE 15>>>
- **P26 关闭不用的 WebView**：Recommendation: Disable the webview server from the switch and the relevant TCP/UDP ports if it is not needed to reduce the attack surface and mitigate security risks. <<<PAGE 15>>>
- **P27 使用 MFA**：Recommendation: Use MFA since it provides a significantly higher level of security than traditional single-factor authentication methods. <<<PAGE 16>>>
- **P28 AAA 集中化**：Recommendation: Centralize access control through external servers to improve the consistency of access control, allow network-wide control of accounts... <<<PAGE 16>>>
- **P29 RADIUS over TLS**：Recommendation: Configure RADIUS over TLS for enhanced security. <<<PAGE 17>>>
- **P30 基于角色的权限划分**：Recommendation: Implement role-based access control by setting up custom authorization per user. <<<PAGE 17>>>
- **P31 启用记账审计**：Recommendation: Enable accounting for auditing and compliance purposes to a centralized location. <<<PAGE 18>>>
- **P32 命令日志留痕**：Recommendation: Enable command logging to keep an audit trail of all commands entered through the CLI. <<<PAGE 19>>>
- **P33 只用 SNMPv3**：Recommendation: SNMPv1/2/2c should be avoided entirely as they are insecure. SNMPv3 is significantly more secure with added encryption, robust authentication, message integrity, and role-based access control. <<<PAGE 19>>>
- **P34 SNMP 专用账户禁 SSH**：Recommendation: Use a separate user account for SNMP management access. Disable SSH and other management features for this user... <<<PAGE 19>>>
- **P35 启用 SNMP 认证陷阱**：Recommendation: Enable SNMP authentication traps. <<<PAGE 20>>>
- **P36 TSM/USM 按条件选择**：Recommendation: Use TSM SNMP model when you already have PKI infrastructure available, otherwise use USM SNMP model. <<<PAGE 20>>>
- **P37 集中 syslog 并用 TLS + 冗余**：Recommendation: Centralize syslog logging using TLS encryption and add a second syslog server for redundancy. <<<PAGE 21>>>
- **P38 PKI 证书校验防欺骗**：Recommendation: Configure PKI to validate client and server certificates to prevent spoofing attacks. <<<PAGE 22>>>
- **P39 SSL cipher 级别设为 high**：Recommendation: Set the SSL Cipher level to high. <<<PAGE 23>>>
- **P40 自签默认证书不可依赖**：Recommendation: Configure a custom SSL certificate for WebView access and do not rely on the built-in self-signed certificate. <<<PAGE 23>>>
- **P41 Portal 证书用公共 CA 签发**：since most use cases for captive portal authentication is used for external guest users, it is recommended to sign your certificate by an official Public CA. <<<PAGE 58>>>
- **P42 LDAP 走 SSL**：Recommendation: Use SSL with LDAP authentication using a custom SSL certificate. <<<PAGE 24>>>
- **P43 启用 ASA enhanced 模式**：Recommendation: For enhanced security restrictions to the OmniSwitch, it is recommended to set the ASA mode to enhanced. <<<PAGE 24>>>
- **P44 设置登录警示横幅**：Recommendation: Setup a warning banner, which are brief messages that are used to inform users of policies and legislation. <<<PAGE 28>>>
- **P45 强口令策略**：Recommendation: Configure a strong password policy on the switch to enforce password complexity when a password is created, modified, and used. <<<PAGE 28>>>

## 控制面

- **P46 路由协议邻居认证**：Recommendation: Use MD5 authentication in networks that require RIP protocol. / Configure keychain authentication with key rotation between OSPF peers. / Configure MD5 authentication between BGP peers. / Configure MD5 authentication between LDP peers. <<<PAGE 30-31>>>
- **P47 keychain 密钥轮换**：a keychain is a form of authentication that allows a regular rotation of keys to be used for limited periods of time. We will cover the keychain authentication as it is the most secure option. <<<PAGE 30>>>
- **P48 Root Guard 防外部桥影响生成树**：Recommendation: Enable Root Guard functionality on the downlink ports from the core (root) switches in your network. <<<PAGE 32>>>
- **P49 边缘限制 TCN 传播**：Recommendation: Enable TCN Restriction feature on your edge ports. <<<PAGE 32>>>
- **P50 用户端口过滤/关闭 BPDU**：Recommendation: Filter or shutdown user port upon receiving a BPDU to protect the network from malicious or unauthorized devices being connected to the network. <<<PAGE 33>>>
- **P51 LLDP 代理安全防 rogue 设备**：Recommendation: Configure LLDP Agent security feature. <<<PAGE 33>>>
- **P52 ARP 过滤防欺骗**：Recommendation: Configure ARP filtering to control how ARP traffic is handled and prevent ARP spoofing, ARP poisoning, or Man-in-the-Middle (MiTM) attacks. <<<PAGE 34>>>
- **P53 阻断入向 GARP**：Recommendation: Block incoming GARP packets to avoid spoofed GARP messages which can be used in MiTM attacks and enable sending GARP packets. <<<PAGE 35>>>
- **P54 ARP 欺骗检测限址**：Recommendation: Configure ARP Poisoning detection and define restricted addresses on critical hosts such as servers, gateways and routers, critical IoT devices, firewalls and IDS/IPS systems... <<<PAGE 35>>>
- **P55 NTP 认证保证日志时间可信**：Recommendation: Configure NTP with authentication and encryption to ensure the network switches are synchronized only with trusted and verified NTP servers. <<<PAGE 36>>>
- **P56 裁剪无用 ICMP 消息**：Recommendation: Disable all unused IPv4 ICMP messages as highlighted in the table below. <<<PAGE 37>>>
- **P57 DHCP Snooping + DAI 组合**：Recommendation: Configure DHCP Snooping feature along with Dynamic ARP Inspection (IP Source Filtering). <<<PAGE 38>>>
- **P58 IPv6 环境三件套**：Recommendation: Configure DHCPv6 snooping and IPv6 source filtering features in IPv6 environments. / Configure DHCPv6 Guard in IPv6 environments. / Configure IPv6 RA Filtering in IPv6 environments to prevent rogue RA from unauthorized systems. <<<PAGE 39-45>>>
- **P59 不用即关（MVRP）**：Recommendation: Disable MVRP unless required. <<<PAGE 41>>>
- **P60 交换机作 802.1X 客户端**：Recommendation: Configure the switch supplicant feature using custom certificates for enhanced network security and to prevent MiTM attacks. <<<PAGE 42>>>

## 数据面

- **P61 链路级加密 MACsec**：Recommendation: Configure MACsec for integrity and encryption between critical endpoints if supported on your switching model. <<<PAGE 45>>>
- **P62 禁用定向广播**：Recommendation: Disable directed broadcasts. <<<PAGE 45>>>
- **P63 IPv6 邻居缓存限額防资源耗尽**：Recommendation: Configure IPv6 Neighbor Cache Limit to prevent DoS attacks that exhaust network resources. <<<PAGE 46>>>
- **P64 边缘端口 LPS**：Recommendation: Configure LPS on all edge ports to protect against unauthorized device connections. <<<PAGE 46>>>

## 无线与网管

- **P65 AP 只用 HTTPS 管理**：Recommendation: Only use HTTPS for AP web management. <<<PAGE 48>>>
- **P66 不用账户保持禁用**：Recommendation: Keep the Viewer and GuestOperator accounts disabled unless required to avoid exposure. <<<PAGE 52>>>
- **P67 AP 802.1X 用自定义证书**：Recommendation: Do not rely on the Default Client Certificate on APs and the Default Server Certificate on UPAM but install Custom Client Certificates... <<<PAGE 61>>>
- **P68 持续运营 wIPS**：Recommendation: Configure, maintain, and monitor the wIPS policies regularly. wIPS is critical for securing wireless networks against unauthorized access, rogue devices, and various wireless attacks. <<<PAGE 63>>>
- **P69 WPA3 优先**：Recommendation: Use WPA3 Encryption when configuring SSIDs to enable more robust authentication, deliver increased cryptographic strength, and maintain resiliency. <<<PAGE 68>>>
- **P70 开放 SSID 启用 OWE**：Recommendation: Enable the Enhanced Open feature to secure communication between endpoints if you are using an Open WLAN SSID. <<<PAGE 69>>>
- **P71 访客客户端隔离**：Recommendation: Configure client isolation between guest SSID users. <<<PAGE 70>>>
- **P72 漫游上下文加密**：Recommendation: Encrypt the client context exchange between APs when the client is roaming from one AP to another. <<<PAGE 70>>>
- **P73 最小权限防火墙开孔**：Recommendation: As best practice, you should maintain concept of least privilege between your network components by allowing only the required firewall ports for proper communication. <<<PAGE 71>>>
- **P74 全平台启用 2FA**：Recommendation: Enable two-factor authentication for all users on the MSP and organization level as it provides a robust defense against unauthorized access. <<<PAGE 72>>>
- **P75 停用未用服务**：Recommendation: Disable any unused services to prevent any unnecessary security exposure. <<<PAGE 73>>>
- **P76 Network ID 防误接入**：Recommendation: use the Network ID feature to securely onboard your network devices to OmniVista Cirrus NMS platforms. <<<PAGE 75>>>
- **P77 角色化最小权限账户**：Recommendation: Create role-based access and use the principle of least privilege when creating user accounts. <<<PAGE 77>>>
- **P78 持续监控发现 IoC**：Recommendation: Regularly monitoring your network and client activities is very important from a security standpoint to detect any anomalies and Indicators of compromise (IoC). <<<PAGE 77>>>
- **P79 隔离恶意终端阻断横向移动**：Recommendation: Integrate Quarantine Manager application with IPS to protect the network from attacks by isolating the malicious device avoiding lateral movement. <<<PAGE 84>>>
- **P80 API 凭据不入代码、专用账户、最小权限**：Store your authentication credentials securely and don't store them in the code. / Create a dedicated user credentials for API access. / Apply the principle of least privilege. <<<PAGE 84>>>

## 生命周期方法（DOC 2）

- **P81 全生命周期管理（NLM）**：they require a systematic lifecycle management approach to adapt to evolving technological, operational and security needs. <<<PAGE 89>>>
- **P82 设计期即面向未来**：The solution should also incorporate lifecycle thinking to plan for future growth, even during the design phase. <<<PAGE 91>>>
- **P83 入门级交换机不满足 AI 需求**：High-quality components are fundamental... entry-level network switches are inadequate for the latest artificial intelligence (AI) systems. <<<PAGE 91>>>
- **P84 边缘设备纳入生命周期管理**：Edge devices are part of the network and should be brought into the "best practice" lifecycle management infrastructure. <<<PAGE 92>>>
- **P85 空气隔离已不现实**：Today, IP video networks are mostly connected and no longer depend on "air gaps" to prevent unauthorized access. <<<PAGE 93>>>
- **P86 "装完就不管"不成立**：The concept of "set it and forget it" does not apply. <<<PAGE 95>>>
- **P87 冗余设计支撑零停机升级**：Designing redundancy into the system enables managing system upgrades with no downtime: firmware can be installed while a redundant system is carrying the video load. <<<PAGE 96>>>
- **P88 物理安全依赖网络安全**：There is no physical security without cybersecurity. Any cybersecurity liability has a resulting physical security liability, such as if a camera watching a door is remotely disabled. <<<PAGE 99>>>
- **P89 网络保险驱动合规**：Many organizations now require video surveillance systems to comply with cybersecurity standards for insurance purposes. <<<PAGE 99>>>
- **P90 退役须安全清数据**：Any equipment containing sensitive information should be wiped and disposed of in line with data privacy laws. <<<PAGE 99>>>
- **P91 过度工程可作为未来预留**：In some cases, over-engineering elements of a system can prepare for future expansion and worst-case scenarios during a system's lifecycle. <<<PAGE 100>>>
- **P92 长期服务承诺倒逼选好设备**：If the integrator is responsible for ongoing maintenance costs, it behooves them to use the best equipment with the best warranty to ensure fewer expensive "truck rolls"... <<<PAGE 100>>>
