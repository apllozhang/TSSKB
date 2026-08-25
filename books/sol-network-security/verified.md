# Verified 候选（V1 原文真实性核对 + V2/V3 抽查）

## cases

- **C1 签名镜像验证供应链完整**：Using RSA-4096 and SHA-256, AOS images are signed with a private key allowing AOS to verify the signature with a corresponding public key during reload and flash synchronization. U-boot version 8.9.70.R04 and above supports AOS signed images only. <<<PAGE 6>>>
- **C2 PSIRT 漏洞响应流程与第三方协作**：ALE PSIRT works with third-party coordination centers such as CERT-IST, NVD and US-CERT to manage vulnerabilities notices. The reports are referred to with a unique Common Vulnerabilities and Exposures (CVE) number. <<<PAGE 7>>>
- **C3 U-boot 口令丢失导致返厂**：if the flash is corrupted and U-boot fails to start the AOS with the password enabled and the password is forgotten, the switch must be returned to the factory for repair. <<<PAGE 9>>>
- **C4 secureadmin 特权账户首登强制改密**：The "secureadmin" user must change the default password during first login... with features including: Check integrity of image... Process self-test functions. <<<PAGE 11>>>
- **C5 管理 VRF 收敛攻击面**：vrf data ssh admin-state disable / vrf data telnet admin-state disable / vrf data webview server disable —— 在数据 VRF 内逐项关闭管理服务。 <<<PAGE 10>>>
- **C6 SSH PKA 部署七步**：ssh-keygen 生成密钥对→保存私钥→scp 公钥上交换机→建用户→installsshkey→公钥登录→ssh enforce-pubkey-auth。 <<<PAGE 14>>>
- **C7 IP 锁定与封禁清单**：IP address is permanently blocked/banned if the number of authentication failures from a particular IP reaches the IP lockout threshold... A maximum of 128 IPs will be added to the banned list. <<<PAGE 15>>>
- **C8 RADIUS 服务器排序回退链**：aaa authentication ssh rad1 ldap2 local —— The switch uses the first available server in the list... If ldap2 then becomes unavailable, the switch will use the local user database. <<<PAGE 16>>>
- **C9 SNMP over TLS（TSM）映射证书身份**：snmp tsm-map remote-identity manager.crt user NMSuserV3MD5DES —— 用户账户必须映射到 TSM 模式下的远端证书。 <<<PAGE 20>>>
- **C10 OSPF keychain 轮换三密钥配置**：security key 1/2/3 algorithm sha256 ... start-time/lifetime → security key-chain 1 name "OSPF" → ip ospf interface vlan-101 auth-type key-chain 1。 <<<PAGE 30>>>
- **C11 LLDP Agent Security 检测 rogue 接入**：when someone tries to take control over the network by connecting non-registered devices to an NNI port, the LLDP Security mechanism is activated... The NNI port that is connected to the rogue device is blocked. <<<PAGE 33>>>
- **C12 DHCP Snooping + IP Source Filtering 组成 DAI**：dhcp-snooping vlan 140 admin-state enable + dhcp-snooping port 1/1/5 trust (DHCP Server Port) + dhcp-snooping ip-source-filter vlan 140 admin-state enable。 <<<PAGE 39>>>
- **C13 JITC 模式强制安全细则**：The minimum password length must be 15 characters or more... The SSH sessions will rekey at a minimum every one gigabyte or every 60 minutes... Software upgrades are allowed only after the digital signature of the software component is verified. <<<PAGE 27>>>
- **C14 wIPS rogue AP 治理组合拳**：AP allowlist（可信外来 AP）+ AP blocklist（ rogue 禁止角色切换）+ Suppress（发 DEAUTH 驱离客户端）+ Dynamic blocklist（ad-hoc 自动拉黑）。 <<<PAGE 63-64>>>
- **C15 Z-Score 端口利用率异常检测**：Anomaly detection uses Z-Score to check for anomalies in the latest port utilization data gathered from hourly polling over the past 30 days. <<<PAGE 78>>>
- **C16 Quarantine Manager 与 IPS 联动隔离**：works with an external Intrusion Prevention System (IPS), such as Fortinet... the suspicious device is isolated at its attached switch or AP level, avoiding lateral movements in the intranet. <<<PAGE 83-84>>>
- **C17 Stellar AP 作为 802.1X 客户端五种上线场景**：UPAM+内置证书 / UPAM+自定义证书 / 外部 RADIUS+内置证书 / 外部 RADIUS+自定义证书 / 用户名（AP MAC）认证。 <<<PAGE 61-62>>>
- **C18 Lightning Config 五分钟部署**：With Lightning Config, an installer with 50 minutes of training can install a network device within five minutes. <<<PAGE 93>>>
- **C19 PoE 向导一键诊断**：The PoE wizard verifies every PoE device on a switch and diagnoses and resolves common PoE problems with one click. <<<PAGE 97>>>
- **C20 Milestone VMS 插件打通视频与网络监控**：information about ALE's managed switches is available through integration with the Milestone XProtect VMS system using a plug-in. <<<PAGE 95>>>

## counter-examples

- **X1 默认口令"switch"风险**：By default, two user management accounts are available at the first bootup of the switch. They are "admin" and "secureadmin" user account, both having the default password of "switch". <<<PAGE 11>>>
- **X2 控制台直连可重置管理员口令**：With console access to the switch, the malicious actor can easily reset the admin password. <<<PAGE 11>>>
- **X3 开机全开的服务端口易被 DoS**：When a switch initially boots up, all supported TCP/UDP well-known service ports are enabled (open). Although these ports provide access for essential switch management services... they also are vulnerable to DoS attacks. <<<PAGE 12>>>
- **X4 Telnet/FTP/TFTP/HTTP/明文 SNMP 为不安全协议**：telnet does not use encryption nor certificates / SNMPv1 does not provide for user authentication nor encryption. <<<PAGE 12>>>
- **X5 密码认证固有弱点**：password-based authentication presents several security weaknesses, including: predictability, re-use, issues with complexity, sharing and phishing, brute force attacks, and longevity. <<<PAGE 16>>>
- **X6 U-boot 暴露系统参数**：The U-boot provides access to system parameters, with which boot images and system variables can be manipulated by any user having physical or console access to the switch. <<<PAGE 9>>>
- **X7 公开漏洞即攻击武器**：Since vulnerabilities are publically disclosed they are also known by malicious attackers who will exploit these vulnerabilities. <<<PAGE 7>>>
- **X8 网络插孔直通防火墙内网**：Physical access to network jacks allows a malicious actor to enter the network inside the firewall. <<<PAGE 8>>>
- **X9 未培训员工无意暴露**：without information security awareness training the employees may inadvertently leave network elements vulnerable to misuse. <<<PAGE 8>>>
- **X10 默认 PKI 模式不校验证书**：No Validation: This is the default mode, in this mode the client applications do not provide certificate and not validate server certificate. <<<PAGE 21>>>
- **X11 自签证书触发浏览器告警**：When accessing WebView using the default settings, a self-signed certificate will be used which will generate a certificate warning on the web browser. <<<PAGE 23>>>
- **X12 工厂默认口令策略弱（无大小写要求数）**：Minimum number of English uppercase characters: Factory Default Values — Disable. <<<PAGE 25>>>
- **X13 工厂默认无用户锁定**：User Lockout Setting / Threshold: Factory Default Values — Disable. <<<PAGE 25>>>
- **X14 CC 模式下默认 admin 日常使用是反模式**：the default "admin" user must be used only to perform installation and initial configuration of the TOE. The general switch administration or management must be performed by the users with appropriate administrative privileges... but not by the default "admin" user. <<<PAGE 26>>>
- **X15 无线网络天然开放无边界**：An 802.11 network is open and borderless, making it vulnerable to attack (e.g., rogue APs, unauthorized clients, DoS attacks). <<<PAGE 63>>>
- **X16 干扰 AP 与 rogue AP 混淆误报**：An interfering AP... is not considered a direct security threat, because it is not connected to the wired network. / A rogue AP is an unauthorized AP plugged into the wired side of the network... <<<PAGE 63>>>
- **X17 WPA2 字典攻击失效前提**：With SAE, the passphrase is never exposed, making it impossible for an attacker to find the passphrase through brute force dictionary attacks.（反面：WPA2/PSK 可被离线字典攻击） <<<PAGE 68>>>
- **X18 去认证攻击利用可选 PMF**：providing an additional layer of protection from deauthentication and disassociation attacks.（反面：PMF 可选时代未开启即受此类攻击） <<<PAGE 68>>>
- **X19 开放 SSID 无加密可被窃听**：OmniAccess Stellar provides enhanced security and privacy for open SSIDs in WLAN networks with support of the new Wi-Fi Enhanced Open security standard based on Opportunistic Wireless Encryption (OWE).（反面：传统开放 SSID 明文传输） <<<PAGE 69>>>
- **X20 WPA3_AES256 自动回退降级**：Note that when WPA3_AES256 encryption is applied to an AP that does not support it, the encryption will automatically fall back to WPA2_AES. <<<PAGE 68>>>
- **X21 漫游域默认空口令**：By default, the Roaming Domain is set to "automatic" (password is empty). <<<PAGE 70>>>
- **X22 客户端隔离不跨 AP 生效**：if isolation between guests is required even if they are associated to different APs, then an ACL (at SSID level) may be configured... <<<PAGE 70>>>
- **X23 API 凭据硬编码**：don't store them in the code. You can use a third-party application to store and manage tokens, passwords, certificates, and API keys.（反面：把凭据写进代码） <<<PAGE 84>>>
- **X24 API 暴露公网**：Avoid exposing APIs to the outside world (internet). <<<PAGE 84>>>
- **X25 "装完就不管"心态**：The concept of "set it and forget it" does not apply. <<<PAGE 95>>>
- **X26 能力不足的容量规划导致返工**：As network demand grows, systems that lack proper capacity planning can experience slowdowns, data loss, or require costly retrofits. <<<PAGE 91>>>
- **X27 低质设备拉高长期成本**：If the integrator is responsible for ongoing maintenance costs, it behooves them to use the best equipment... to ensure fewer expensive "truck rolls".（反面：贪便宜设备导致反复上门） <<<PAGE 100>>>

## frameworks

## F1 ALE 五层集成安全框架 <<<PAGE 5-6>>>
自下而上/由内而外的分层防御清单：
2. 设备级：设备认证 + 合规检查（杀毒、OS 版本预扫描）
3. 应用级：按应用设规则（阻断、限速、身份限定）
4. 网络级：交换机/AP 智能分析提供可见性 + DPI 识别异常流量
5. IoT 级：虚拟容器（网络虚拟化）隔离，单点失陷不扩散
## F2 三平面安全加固框架 <<<PAGE 9-47>>>
全册主结构，适用于任何网络设备安全审计：
1. 管理面（Management Plane）：设备访问、AAA、证书、SNMP、日志、安全模式
2. 控制面（Control Plane）：路由/标签/链路管理/发现/网管协议认证与防护
3. 数据面（Data Plane）：链路加密（MACsec）、地址族防护、端口安全（LPS）
## F3 协议替换对照框架 <<<PAGE 12>>>
不安全协议 → 安全替换的决策表：
| 不安全 | 替换 | 原因 |
|---|---|---|
| Telnet | SSH | 无加密无证书 |
| FTP/TFTP | SFTP/SCP | 无加密无证书 |
| SNMPv1/v2c | SNMPv3 | 仅社区串认证 |
| HTTP | HTTPS | 明文协议 |
## F4 视频监控网络生命周期 7 阶段框架（NLM） <<<PAGE 89>>>
1. 规划与设计（Five S's：Software / Surveillance IoT / Servers-Storage / Switches / Services-Support）
2. 部署（UNP、Lightning Config、边缘认证上线）
3. 运营管理（持续监控、API/VMS 集成、主动补丁）
4. 故障维护（固件升级、冗余切换、软件工具包）
5. 升级优化（AI、Network Advisor、分阶段换新）
6. 合规与文档（安全审计、网络保险、文档留存）
7. 退役与重部署（数据安全迁移、按隐私法擦除处置）

## glossary

- **PSIRT（产品安全事件响应团队）**：ALE 专职团队，受理漏洞报告、协调修复并发布安全通告 <<<PAGE 7>>>
- **CVE（通用漏洞披露编号）**：漏洞报告的唯一编号，与 CERT/NVD 等协调中心联动 <<<PAGE 7>>>
- **SA（Security Advisory，安全通告）**：漏洞确认后由安全通告委员会发布，含修复与缓解措施 <<<PAGE 7>>>
- **BYOD（自带设备办公）**：员工自带终端接入，扩大攻击面的典型场景 <<<PAGE 5>>>
- **DPI（深度包检测）**：ALE 智能分析能力，识别流量类型与异常模式 <<<PAGE 6>>>
- **ASLR（地址空间布局随机化）**：每次交换机启动生成唯一内存布局的软件多样化技术 <<<PAGE 6>>>
- **IV&V（独立第三方验证与确认）**：源代码白盒/黑盒测试寻找外部接口漏洞 <<<PAGE 6>>>
- **Common Criteria EAL2 / NDcPP**：ALE 产品获得的国际安全评估认证 <<<PAGE 6>>>
- **FIPS 140-2**：NIST 密码模块安全标准，FIPS 模式下仅允许强加密算法 <<<PAGE 6, 28>>>
- **TAA 合规**：美国供应链规定，OmniSwitch 可指定美国原产国 <<<PAGE 6>>>
- **U-boot / ONIE**：OmniSwitch 两种引导加载器，可设口令认证防止物理层篡改 <<<PAGE 9>>>
- **镜像完整性校验**：image integrity-check 命令比对 SHA256 哈希与密钥文件 <<<PAGE 9>>>
- **EMP（以太网管理口）**：专用带外管理端口，绕过业务 NI 模块直连 CMM <<<PAGE 10>>>
- **管理 VRF**：无带外条件时，将全部管理协议收敛到专用 VRF 与数据隔离 <<<PAGE 10>>>
- **IP 管理站（Management Station）**：仅允许预定义 IP 管理交换机，上限 64 个 <<<PAGE 11>>>
- **secureadmin**：首登强制改密的特权账户，可校验镜像与 vcboot.cfg 完整性 <<<PAGE 11>>>
- **SSH 强加密（strong-ciphers / strong-HMACs）**：强制启用 hmac-sha2-256/512 等强算法 <<<PAGE 13>>>
- **PKA（公钥认证）**：SSH 免口令登录，installsshkey 安装公钥 <<<PAGE 13-14>>>
- **登录宽限期（login-grace-time）**：未完成 SSH 会话的超时，默认 120 秒 <<<PAGE 14>>>
- **IP 锁定阈值（ip-lockout-threshold）**：认证失败次数达阈值即封禁来源 IP，清单上限 128 <<<PAGE 15>>>
- **MFA（多因素认证）**：Google Authenticator、Duo 等多道身份验证 <<<PAGE 16>>>
- **ASA（Authenticated Switch Access）**：交换机管理接入认证体系，分 default 与 enhanced 模式 <<<PAGE 16, 24>>>
- **AAA（认证/授权/记账）**：本地或 RADIUS/LDAP/TACACS+ 集中化的访问控制框架 <<<PAGE 16>>>
- **RADIUS over TLS**：用 TLS 加密 RADIUS 报文，消除 MD5 攻击风险 <<<PAGE 17>>>
- **命令域/命令族（domain/family）**：AOS 按 domain-network、domain-security 等划分用户权限粒度 <<<PAGE 18>>>
- **记账（Accounting）**：记录登录登出、会话时长等供审计 <<<PAGE 18>>>
- **命令日志（command.log）**：全量 CLI 命令历史审计文件 <<<PAGE 19>>>
- **SNMPv3 三模型**：VACM（基于视图的访问控制）、USM（基于用户的安全模型）、TSM（传输安全模型） <<<PAGE 19>>>
- **TSM**：SNMP over TLS/DTLS 的安全传输模型，需证书身份映射 <<<PAGE 20>>>
- **SNMP 认证陷阱**：收到未授权实体请求时向网管站告警 <<<PAGE 20>>>
- **SWLOG（交换机日志）**：默认 info(6) 级别，可按应用分配 1-8 严重级别，支持 TLS 远端发送 <<<PAGE 21>>>
- **PKI 三种公钥安全模式**：No Validation / Server Certificate Validation / Mutual Authentication <<<PAGE 21>>>
- **OpenSSL cipher 安全级别**：All/Low/Medium/High 四档，默认 medium，CC 模式为 high <<<PAGE 22>>>
- **OCSP / CRL**：X.509 证书有效性校验手段，校验失败即断开 TLS <<<PAGE 22>>>
- **Captive Portal（强制门户）**：Web 认证页面，默认自签证书 default_cportalCert.pem 可替换 <<<PAGE 23>>>
- **CC 模式（Common Criteria）**：仅允许 console+SSH，默认禁用 FTP/Telnet/WebView/HTTP/RADIUS/LDAP/SNMP <<<PAGE 26>>>
- **TOE（评估对象）**：CC 评估语境下被评估的 OmniSwitch 产品 <<<PAGE 26>>>
- **JITC 模式**：军用认证模式，口令≥15 字符、SSH 每小时/每 GB 重协商、升级前验签；与 CC/enhanced 互斥 <<<PAGE 26-27>>>
- **FIPS 模式**：OpenSSL 层强制 FIPS 140-2 算法，SNMPv3 仅 SHA+AES，需重启生效 <<<PAGE 28>>>
- **登录横幅（Login Banner）**：/flash/switch 下 banner.txt 经 session banner 启用的合规告示 <<<PAGE 28>>>
- **盐渍哈希口令存储**：新口令与 16 字节随机盐拼接后哈希入库 <<<PAGE 28>>>
- **keychain 认证**：带起止时间与生命周期的密钥轮换机制，OSPF/IS-IS 最安全选项 <<<PAGE 30>>>
- **LDP（标签分发协议）**：MPLS 中 LSR 间分发标签，MD5 认证防 TCP 伪造 <<<PAGE 31>>>
- **Root Guard（restricted-role）**：阻止端口成为根端口，防外部桥影响生成树拓扑 <<<PAGE 32>>>
- **TCN 限制（restricted-tcn）**：阻止边缘端口传播拓扑变更，避免核心区无谓 MAC 冲刷 <<<PAGE 32>>>
- **BPDU 过滤/关闭**：用户端口收到 BPDU 即过滤或 shutdown <<<PAGE 33>>>
- **LLDP Agent Security**：端口仅信一个 LLDP 远端代理，超限进入 violation 态（trap/shutdown） <<<PAGE 33>>>
- **GARP（Gratuitous ARP，免费 ARP）**：源目 MAC 相同的通告广播，可被伪造用于 MiTM <<<PAGE 34-35>>>
- **ARP 欺骗检测（arp-poison restricted-address）**：受限地址收到 ARP 应答即告警 <<<PAGE 35>>>
- **NTP key file**：/flash/network/ntp.keys 存 MD5/SHA1 认证密钥，须设 trusted <<<PAGE 36-37>>>
- **ICMP 裁剪表**：Echo/Redirect/Router Advertisement/Timestamp 等按风险禁用 <<<PAGE 37-38>>>
- **DHCP Option-82**：中继在客户端报文中插入端口识别信息；与 Snooping 互斥 <<<PAGE 38>>>
- **DHCP Snooping**：信任/非信任端口分类 + 绑定表，防 rogue DHCP <<<PAGE 38>>>
- **DAI / IP Source Filtering（动态 ARP 检测）**：依 Snooping 绑定表校验源信息，防 ARP 欺骗 <<<PAGE 39>>>
- **DHCPv6 Snooping / IPv6 Source Filtering**：IPv6 版绑定表与源过滤，需配合 TCAM 模式调整 <<<PAGE 39-40>>>
- **DHCPv6 Guard**：仅信任端口放行 DHCPv6 服务器报文，防 rogue DHCPv6 <<<PAGE 40>>>
- **MVRP**：动态 VLAN 注册协议，安全建议默认禁用 <<<PAGE 41>>>
- **DoS 过滤**：默认开启，覆盖 Ping of Death、Land、ARP Flood（>500/s）、Ping overload（>100/s）等 <<<PAGE 41>>>
- **端口扫描惩罚值机制**：按端口类型累计 penalty，超过阈值（如 2000）触发 SNMP trap <<<PAGE 41-42>>>
- **Switch Supplicant（交换机请求者）**：交换机作为 802.1X 客户端上线，需 X509 证书 <<<PAGE 42-43>>>
- **MACsec / MKA**：以太网点对点加密（etherType 0x88E5），SAK 会话密钥，静态四密钥或 MKA 动态轮换 <<<PAGE 43-44>>>
- **SAK（安全关联密钥）**：MACsec 会话密钥，静态模式每信道四把（一用三备） <<<PAGE 44>>>
- **定向广播（directed broadcast）**：默认丢弃，可配受控信任源放行 <<<PAGE 45>>>
- **IPv6 RA 过滤（ra-filter）**：丢弃非法路由通告，仅信任端口转发 <<<PAGE 45-46>>>
- **LPS（Learned Port Security）**：边缘端口 MAC 学习授权机制，可限数、限窗、违规 shutdown <<<PAGE 46-47>>>
- **Stellar 证书八类**：Web 服务器（mywifi.al-enterprise.com）/ Portal / 本地 LDAP / 802.1X 客户端 / BLE / RTLS / RadSec / Syslog over TLS <<<PAGE 48>>>
- **Wi-Fi Express（集群模式）**：Stellar AP 免网管独立组网模式，含 wIDS/wIPS 面板 <<<PAGE 47, 63>>>
- **账户三级**：Administrator / Viewer / GuestOperator，默认仅 Administrator 启用 <<<PAGE 52>>>
- **wIPS 三类 AP**：interfering（未接有线，非直接威胁）/ rogue（接有线或冒同 SSID，威胁）/ friendly（允许清单） <<<PAGE 63, 66>>>
- **Rogue AP Containment（抑制）**：探测 AP 向 rogue 关联客户端发 DEAUTH 驱离 <<<PAGE 63, 66>>>
- **WIPS 检测级别**：High / Medium / Low(默认) / Custom 四档策略强度 <<<PAGE 66>>>
- **WPA3-Personal / SAE**：对等同步认证，口令不暴露，免疫离线字典攻击；PMF 强制 <<<PAGE 68>>>
- **WPA3_AES256（CNSA/Suite B）**：192 位商用国家安全算法套件，AP 不支持时自动回退 WPA2_AES <<<PAGE 68>>>
- **WPA3_PSK_SAE_AES**：WPA3/WPA2 混合模式，兼容双代客户端 <<<PAGE 68>>>
- **OWE / Wi-Fi Enhanced Open（增强开放）**：开放 SSID 的机会式无线加密，6 GHz 频段强制启用 <<<PAGE 69>>>
- **客户端隔离（Client Isolation）**：同 AP 同 SSID 内阻断客户端互访，仅放行去往路由器 <<<PAGE 70>>>
- **漫游上下文 DTLS 加密**：AP 间漫游切换时客户端上下文走 DTLS 隧道 <<<PAGE 70>>>
- **2FA（两步验证）**：OmniVista Cirrus 10 支持 Email 与 Google Authenticator 两种模式 <<<PAGE 72>>>
- **Network ID（网络标识安全上线）**：DHCP Option 43 Sub-Option 133 下发，Strict Mode 拒绝无 ID 设备 <<<PAGE 75-76>>>
- **MSP / Organization 用户**：OmniVista Cirrus 10 两级用户体系（托管服务商用户/组织用户） <<<PAGE 77>>>
- **Z-Score 异常检测**：以 30 天小时级端口利用率为基线标记偏离点的统计方法 <<<PAGE 78>>>
- **UPAM（OmniVista 策略与接入管理）**：内置 RADIUS/802.1X 服务器组件，含证书与信任 CA 管理 <<<PAGE 61, 80>>>
- **RadSec（RADIUS over TLS）**：TLS 加密的 RADIUS 传输，UPAM 可作 RadSec 客户端 <<<PAGE 60, 80>>>
- **Quarantine Manager / QMR**：联动 IPS 的终端隔离应用与交换机侧修复组件 <<<PAGE 83-84>>>
- **IoC（失陷指标）**：持续监控网络与客户端活动所要发现的异常证据 <<<PAGE 77>>>
- **OAuth 2.0 / JWT**：OmniVista 两代 REST API 令牌认证机制（RFC 7519） <<<PAGE 84>>>
- **Web Services（AOS）**：基于 MIB 变量与 CLI 的 REST 管理接口，遵循 WebView 安全模型 <<<PAGE 85>>>
- **NLM（网络生命周期管理）**：覆盖规划到退役全程的结构化管理框架 <<<PAGE 89>>>
- **Five S's**：视频监控规划五要素：Software、Surveillance IoT、Servers/Storage、Switches、Services/Support <<<PAGE 90>>>
- **UNP（Universal Network Profiling，通用网络档案）**：按用户/设备/应用动态下发网络行为的画像机制 <<<PAGE 93>>>
- **Lightning Config**：ALE 开箱即用部署工具，受训 50 分钟的技术员 5 分钟装好设备 <<<PAGE 93>>>
- **Milestone Plugin**：交换机信息集成进 XProtect VMS 的可视化插件 <<<PAGE 94-95>>>
- **OmniVista Network Advisor**：AI 驱动的实时监控、风险告警与网络修复系统 <<<PAGE 98>>>
- **Air Gap（空气隔离）**：物理孤立网络的老式安全措施，联网化后已弃用 <<<PAGE 93>>>

## principles

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
