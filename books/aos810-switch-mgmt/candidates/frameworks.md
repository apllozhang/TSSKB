# frameworks.md — 体系框架候选（《OmniSwitch AOS Release 810R04 Switch Management User Guide》）

- F1…，页码为真实 `<<<PAGE N>>>` 标记页。

- **F1 自动管理特性总体框架（Auto VC → RCL → Auto Fabric → Lightning/Cirrus）**：工厂默认交换机上电后按序执行：自动虚拟机箱（Auto VC）→ 远程配置下载（RCL）→ 自动 Fabric → Lightning/Cirrus；有配置文件则跳过自动阶段。"Power Up → Factory Default? → AutoVC Begins → VC Ready? → RCL Starts → RCL Success? → Auto Fabric Success? → Config Applied" <<<PAGE 21>>>（Figure 1-1）、<<<PAGE 230>>>
- **F2 CMM 双目录配置管理体系（certified/working/RUNNING + 回滚）**：certified（最可靠基线）+ working/用户目录（试验场）+ RUNNING CONFIGURATION（RAM）三层模型；write memory 落盘、copy running certified 认证、flash-synchro 同步，共同构成软件回滚与冗余体系。<<<PAGE 94>>>-<<<PAGE 101>>>
- **F3 认证交换机访问（ASA）安全框架**：管理接口（console/ftp/http/ssh/telnet/snmp）× 认证源（RADIUS/LDAP/local 链式故障切换）× 授权（命令域/族分区管理）× 计费（aaa accounting session）四层；default/enhanced/JITC 三档安全模式递进。<<<PAGE 167>>>-<<<PAGE 186>>>
- **F4 用户权限分区管理框架（domain/family 两级）**：命令域（domain-admin/system/physical/network/layer2/service/policy/security/mpls/vcm/datacenter/afn）下辖命令族，read-only/read-write/all/none/all-except 组合授权；适用于 user 与 aaa priv-mask 两处。<<<PAGE 159>>>、<<<PAGE 181>>>
- **F5 License 体系框架（传统单机 + Premium 捆绑 + SILOS 站点/节点 + NaaS 订阅）**：单机文件 license（EEPROM 化）→ 捆绑子 license（VC Match/Local-Only）→ SILOS 服务器/客户端（MQTT 分发、demo/grace/撤销）→ NaaS 云订阅（Essential/Advanced/Management/Upgrade、grace/degraded 状态机）。<<<PAGE 66>>>-<<<PAGE 77>>>、<<<PAGE 232>>>-<<<PAGE 233>>>
- **F6 包与应用管理框架（pkgmgr/appmgr/文件同步三组件）**：Debian 包的验证-安装-提交（write memory 持久化）-移除生命周期，以及应用的 start/stop/restart 免重启管理；支撑 AMS、WebView 2.0、NTP、Nutanix、PROFINET、Cirrus Agent 等生态。<<<PAGE 85>>>-<<<PAGE 90>>>
- **F7 虚拟机箱（VC）框架**：vcsetup.cfg（单机入组）+ vcboot.cfg（整体配置）双文件体系；Master/Slave 选举五准则；VFL（10/40/100G 聚合、16 字节封装头）+ 控制 VLAN + IS-IS VC 协议；RCD（EMP 带外）与 VCSP（helper linkagg）双分裂防护；Auto-VFL/自动 Chassis ID 零接触建组。<<<PAGE 305>>>-<<<PAGE 343>>>
- **F8 零接触部署框架（DHCP Option 43/66/67 + 指令文件 + Nearest-Edge LLDP）**：DHCP 客户端在 VLAN 1/127/管理 VLAN 轮换获取地址 → TFTP 指令文件（*.alu）→ 主备 FTP/SFTP 拉取镜像/配置/脚本/license → 脚本执行 → 自动重启；Nearest-Edge 用专用组播 MAC 的 LLDP 传播管理 VLAN；DHCP 服务器偏好序（OVCloud > OmniVista > OXO）。<<<PAGE 348>>>-<<<PAGE 364>>>
- **F9 网络可编程框架（REST Web Services + Python + CLI/Bash 脚本 + AMS 发布订阅）**：REST 双域（mib/cli）+ JSON/XML 媒体类型；AOSAPI Python 库；Bash 原生脚本与 grep/awk/sed 工具链；嵌入式 Python 事件（trap）绑定；AMS 以 MQTT broker/topic/community 实现跨交换机配置同步与 replay。<<<PAGE 246>>>-<<<PAGE 278>>>
- **F10 OmniVista Cirrus 云管理框架**：DHCP（Option 43 VSO）→ Activation Server（call-home、证书）→ VPN 隧道 → OV Cirrus 实例（SNMP over VPN）；NaaS license 状态机（Operational → Grace → Degraded）；Thin Switch 最小本地配置模式；LAN 管理改用 MQTT 推送替代 SNMP 轮询。<<<PAGE 226>>>-<<<PAGE 241>>>
- **F11 AOS Micro Services（AMS）微服务生态**：broker + topic（COMMUNITY/APPLICATION/SUB_CONFIG 层级）+ Config-DB（replay）+ config-sync + cron 定时任务；内置设备画像同步与 OS6465 电源配置同步两个示范应用；broker 冗余可借 VRRP。<<<PAGE 272>>>-<<<PAGE 279>>>
- **F12 时间同步框架（系统时钟 + NTP 分层 + Cirrus NTP 池）**：本地 system date/timezone（DST 自动）→ NTP 客户端/服务器/广播模式（minpoll/maxpoll 指数、burst/iburst、MD5/SHA1 认证、stratum 模型）→ 云场景 NTP 池（clockN.ovcirrus.com）保障证书时间有效性。<<<PAGE 78>>>-<<<PAGE 81>>>、<<<PAGE 406>>>-<<<PAGE 417>>>
