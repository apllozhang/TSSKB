# GLOSSARY · Network Security Guidelines + 视频监控白皮书

> 页码为全册连续 `<<<PAGE N>>>` 标记。按安全体系/管理面/安全模式/控制面/数据面/无线/网管/生命周期分组，精选 48 条。

## 安全体系与认证
- **PSIRT**：ALE 产品安全事件响应团队，受理漏洞报告并发布安全通告 <<<PAGE 7>>>
- **CVE**：通用漏洞披露唯一编号，与 CERT-IST/NVD/US-CERT 联动 <<<PAGE 7>>>
- **SA（Security Advisory）**：漏洞确认后发布的含修复与缓解措施的安全通告 <<<PAGE 7>>>
- **签名镜像**：AOS 镜像 RSA-4096+SHA-256 签名，重载时验签；U-boot ≥8.9.70.R04 仅支持签名镜像 <<<PAGE 6>>>
- **ASLR**：每次启动生成唯一内存布局的软件多样化技术 <<<PAGE 6>>>
- **IV&V**：独立第三方源代码白盒/黑盒测试 <<<PAGE 6>>>
- **Common Criteria EAL2 / NDcPP**：ALE 产品国际安全评估认证 <<<PAGE 6>>>
- **FIPS 140-2**：NIST 密码模块标准；FIPS 模式下仅允许强加密算法 <<<PAGE 6, 28>>>
- **TAA 合规**：美国供应链规定，OmniSwitch 可指定美国原产 <<<PAGE 6>>>
- **DPI**：深度包检测，识别流量类型与异常模式 <<<PAGE 6>>>
- **BYOD**：自带设备办公，扩大攻击面的典型场景 <<<PAGE 5>>>

## 管理面
- **U-boot / ONIE**：两种引导加载器，可设口令防物理层篡改 <<<PAGE 9>>>
- **镜像完整性校验**：image integrity-check 比对 SHA256 哈希与密钥文件 <<<PAGE 9>>>
- **EMP**：专用带外以太网管理口，绕过业务 NI 直连 CMM <<<PAGE 10>>>
- **管理 VRF**：无带外条件时将管理协议收敛到专用 VRF 与数据隔离 <<<PAGE 10>>>
- **IP 管理站白名单**：仅预定义 IP 可管理，上限 64 个 <<<PAGE 11>>>
- **secureadmin**：首登强制改密的特权账户，可校验镜像与 vcboot.cfg 完整性 <<<PAGE 11>>>
- **SSH 强加密（strong-ciphers / strong-HMACs）**：强制 hmac-sha2-256/512 等强算法 <<<PAGE 13>>>
- **PKA**：SSH 公钥认证，installsshkey 安装公钥免口令登录 <<<PAGE 13-14>>>
- **login-grace-time**：未完成 SSH 会话超时，默认 120 秒 <<<PAGE 14>>>
- **IP 锁定阈值（ip-lockout-threshold）**：认证失败达阈值封禁来源 IP，清单上限 128 <<<PAGE 15>>>
- **MFA / 2FA**：多因素认证（Google Authenticator/Duo/Email） <<<PAGE 16, 72>>>
- **AAA**：认证/授权/记账，RADIUS/LDAP/TACACS+ 集中化访问控制 <<<PAGE 16>>>
- **RADIUS over TLS / RadSec**：TLS 加密 RADIUS 报文，消除 MD5 攻击风险 <<<PAGE 17, 80>>>
- **命令域/族（domain/family）**：AOS 按 domain-network 等划分权限粒度 <<<PAGE 18>>>
- **command.log**：全量 CLI 命令历史审计文件 <<<PAGE 19>>>
- **SNMPv3 三模型**：VACM（视图访问）/USM（用户安全）/TSM（传输安全） <<<PAGE 19>>>
- **TSM**：SNMP over TLS/DTLS，需证书身份映射（tsm-map） <<<PAGE 20>>>
- **PKI 三模式**：No Validation（默认）/Server Cert Validation/Mutual Authentication <<<PAGE 21>>>
- **OCSP / CRL**：X.509 证书有效性校验，失败即断 TLS <<<PAGE 22>>>
- **SWLOG**：交换机日志，默认 info(6)，支持 TLS 远端发送 <<<PAGE 21>>>

## 安全模式
- **CC 模式（Common Criteria）**：仅 console+SSH，默认禁 FTP/Telnet/WebView/HTTP/RADIUS/LDAP/SNMP；默认 admin 仅装机用 <<<PAGE 26>>>
- **JITC 模式**：军用认证，口令≥15 字符、SSH 每小时/每 GB rekey、升级前验签；与 CC 互斥 <<<PAGE 26-27>>>
- **FIPS 模式**：OpenSSL 层强制 FIPS 140-2 算法，SNMPv3 仅 SHA+AES，需重启 <<<PAGE 28>>>
- **ASA enhanced**：Authenticated Switch Access 增强模式，常规加固推荐 <<<PAGE 24>>>

## 控制面与数据面
- **keychain 认证**：带起止时间与生命周期的密钥轮换，OSPF/IS-IS 最安全选项 <<<PAGE 30>>>
- **Root Guard（restricted-role）**：阻止端口成为根端口，防外部桥影响生成树 <<<PAGE 32>>>
- **TCN 限制（restricted-tcn）**：阻止边缘口传播拓扑变更 <<<PAGE 32>>>
- **LLDP Agent Security**：端口仅信一个 LLDP 远端代理，rogue 接入即 violation（trap/shutdown） <<<PAGE 33>>>
- **GARP（免费 ARP）**：可被伪造用于 MiTM；建议阻断入向 <<<PAGE 34-35>>>
- **DHCP Snooping**：信任/非信任端口分类+绑定表，防 rogue DHCP <<<PAGE 38>>>
- **DAI / IP Source Filtering**：依 Snooping 绑定表校验源，防 ARP 欺骗 <<<PAGE 39>>>
- **DHCPv6 Guard / RA 过滤**：IPv6 防 rogue DHCPv6 与非法 RA <<<PAGE 40, 45-46>>>
- **MACsec / MKA / SAK**：以太网点对点加密（0x88E5），SAK 静态四密钥或 MKA 动态轮换 <<<PAGE 43-44>>>
- **LPS（Learned Port Security）**：边缘口 MAC 学习授权，限数/限窗/违规 shutdown <<<PAGE 46-47>>>
- **DoS 过滤**：默认开启，覆盖 Ping of Death/Land/ARP Flood(>500/s)/Ping overload(>100/s) <<<PAGE 41>>>

## 无线安全
- **wIPS 三类 AP**：interfering（未接有线，非直接威胁）/rogue（接有线，威胁）/friendly <<<PAGE 63, 66>>>
- **Rogue Containment**：探测 AP 向 rogue 客户端发 DEAUTH 驱离 <<<PAGE 63, 66>>>
- **WPA3-Personal / SAE**：口令不暴露，免疫离线字典攻击；PMF 强制 <<<PAGE 68>>>
- **OWE / Wi-Fi Enhanced Open**：开放 SSID 机会式加密，6 GHz 强制 <<<PAGE 69>>>
- **客户端隔离**：同 AP 同 SSID 阻断互访；跨 AP 需 SSID 级 ACL <<<PAGE 70>>>

## 网管与生命周期
- **Network ID**：DHCP Option 43 Sub-Option 133 下发的设备安全上线标识，Strict Mode 拒无 ID 设备 <<<PAGE 75-76>>>
- **UPAM**：OmniVista 策略与接入管理，内置 RADIUS/802.1X 与证书管理 <<<PAGE 61, 80>>>
- **Z-Score 异常检测**：30 天小时级端口利用率为基线标记偏离点 <<<PAGE 78>>>
- **Quarantine Manager**：联动 IPS 在交换机/AP 级隔离可疑终端 <<<PAGE 83-84>>>
- **OAuth 2.0 / JWT**：OmniVista REST API 令牌认证（RFC 7519） <<<PAGE 84>>>
- **NLM**：网络生命周期管理，规划到退役全程框架 <<<PAGE 89>>>
- **Five S's**：视频监控规划五要素（Software/Surveillance IoT/Servers-Storage/Switches/Services-Support） <<<PAGE 90>>>
- **UNP**：通用网络档案，按用户/设备/应用动态下发网络行为 <<<PAGE 93>>>
- **Lightning Config**：开箱即用部署，50 分钟培训的技术员 5 分钟装机 <<<PAGE 93>>>
- **OmniVista Network Advisor**：AI 驱动实时监控、风险告警与修复 <<<PAGE 98>>>

---
合计：50 条。
