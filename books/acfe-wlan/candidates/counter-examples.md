# 反例提取 · ACFE WLAN - Basic Deployment With OmniVista Ed04

> 来源：D:\Claude code\TSSKB\books\acfe-wlan\source\fulltext.md（585 页）+ BOOK_OVERVIEW.md
> 提取规则：失败模式 / 警告 / 局限 / 陷阱；每条标注页码，引用原文 ≤100 英文词。

```yaml
- id: ce01
  title: 模式切换不迁移配置——Express 转 Enterprise/Cloud 会丢掉整个集群配置
  type: counter-example
  source_chapter: "p18"
  source_quote: |
    "Mode can be changed: Manually in Express mode with a 'Convert to Enterprise' button
    Or requires a factory reset (push button) and reboot ...
    No configuration migration, AP « cluster » configuration is lost"
  summary: |
    场景：客户先用 Wi-Fi Express（standalone cluster）跑了一段时间，后要迁到 OmniVista 管理（Enterprise/Cloud）。
    踩坑点：切换模式（手动点 Convert to Enterprise，或加 DHCP option 138 后恢复出厂/重启）不迁移任何配置，
    AP 集群里的 SSID、Portal、VLAN 等全部丢失，需要在新平台上重建。
    规避：切换前导出/记录 Express 侧全部配置（SSID、密码、VLAN、Portal 账号），把切换当成"重新开局"来做项目计划；
    生产环境切换安排在维护窗口，并提前在 OV 侧建好 AP Group、Provisioning、SSID 等对象。
  tags: [deployment, risk, config-loss, express-mode]

- id: ce02
  title: DHCP option 138 决定 AP 管理模式——配错则 AP 进错模式或不上线
  type: counter-example
  source_chapter: "p100"
  source_quote: |
    "IF DHCP SERVER SENDS OFFER WITH OPTION 138 = YES (IP@ OF OV2500) -> AP REGISTERS AND RETRIEVES
    ITS CONFIGURATION FROM OV2500; IF DHCP SERVER SENDS OFFER WITH OPTION 138 = NO -> AP CONTACTS OV CIRRUS;
    IF AP REGISTERED IN OV CIRRUS (MAC/SN) = NO -> AP BOOTS IN EXPRESS MODE"
  summary: |
    场景：AP 上电后走决策树：DHCP offer 带 option 138（OV2500 地址）则进 Enterprise；没有 138 则尝试联系 OV Cirrus，
    只有 MAC/序列号已在 Cirrus 注册过才取云配置，否则落到 Express 模式。
    后果：option 138 指向错误/遗漏、或设备未在 Cirrus Device Catalog 声明，AP 会静默落入 Express 模式，
    广播默认 mywifi-XXXX，不在云上出现，且可能与已有集群组成意外的 AP Group。
    规避：给 AP 管理 VLAN 的 DHCP scope 正确下发 option 138；云管场景先在 Device Catalog 声明序列号再上电；
    排障时用 getmode 确认 AP 实际所处模式（OV/OVNG/Cluster）。
  tags: [deployment, dhcp, mode-selection, troubleshooting]

- id: ce03
  title: isc-dhcp-server 不认识 option 138——必须先自定义 option 才能下发
  type: counter-example
  source_chapter: "p33"
  source_quote: |
    "# Create custom option 138 as it is not known to isc-dhcp-server
    option ovwma code 138 = ip-address;"
  summary: |
    场景：用 Linux 开源 isc-dhcp-server 给 Stellar AP 分配管理地址并指向 OmniVista。
    踩坑点：option 138 不是 isc-dhcp-server 的内置标准选项，直接在 pool 里写 option 138 会报错或不下发，
    AP 收不到 OV 地址。教材还演示用 vendor-class-identifier（前缀 HAP.）把 AP 与其他客户端分流到专用 pool。
    规避：先声明自定义 option（option ovwma code 138 = ip-address），再在 AP 专用 pool 中下发；
    OmniSwitch 做 DHCP 服务器时语法不同（option 138 直接写）。
  tags: [dhcp, configuration, deployment]

- id: ce04
  title: OV Cirrus 网络前提清单——防火墙端口/NTP/支持型号不满足则设备无法上云
  type: counter-example
  source_chapter: "p167"
  source_quote: |
    "All Stellar models supported, except: AP1101, AP1201L/H/HL ... Open Firewall ports 9093, 30123, 30124, 30125
    And to allow outbound traffic from local network: 443, 80, 123, 53 ...
    Enable DHCP standard options: 1, 3, 6, 28, 42, 43 ... NTP server: At least 1 configured."
  summary: |
    场景：AP/OmniSwitch 要注册到 OV Cirrus 前的网络准备。
    后果：任一前提不满足都表现为"Call Home 失败/不上线"——防火墙没开 9093/30123-30125 入站或 443/80/123/53 出站、
    没有可用 NTP（证书校验对时间敏感）、AP 型号不在支持列表（AP1101、AP1201L/H/HL 不支持）、
    软件版本过低（AP 需 AWOS 4.0.6 GA+，交换机需 AOS 8.9R1+）、走代理时 DHCP options 129-133/138 未启用。
    规避：开局前按此清单逐项核查防火墙、DNS、NTP、DHCP options 与设备版本；排障时先 ping activation 域名验证连通性。
  tags: [prerequisites, firewall, ntp, cloud-onboarding, troubleshooting]

- id: ce05
  title: OVC4 迁移到 OVC：无迁移工具，序列号禁止在两套云上同时登记
  type: counter-example
  source_chapter: "p219"
  source_quote: |
    "The serial number of a network device cannot be declared in both OmniVista CIRRUS 4 and OmniVista CIRRUS.
    Make sure to remove all your equipment first: 1. Select all equipment 2. Delete all equipment"
  summary: |
    场景：从 OmniVista Cirrus 4（4.9R1）迁移到新版 OmniVista Cirrus（10.4.3）。
    踩坑点：当前版本没有自动迁移工具，AP Group、Provisioning、SSID、Access Policy 都要在新 OVC 手工重建并对齐；
    设备序列号不能同时挂在 OVC4 和 OVC 两边，如果旧云上没删除，新云上设备无法完成注册。
    规避：先在新 OVC 手工复刻配置并核对，然后在 OVC4 Device Catalog 删除全部设备，再在新 OVC 声明；
    AP 等待下一次 Call Home（最长 30 分钟）或直接重启 AP 加速，OmniSwitch 用 reload 或重启 cloud-agent 进程。
  tags: [migration, license-registry, cloud-onboarding, risk]

- id: ce06
  title: eBuy 采购的 license 最长 24 小时后才出现在 Subscription Manager
  type: counter-example
  source_chapter: "p175"
  source_quote: |
    "Note: The licenses purchased in eBuy can take up to 24h before coming up in Subscription Manager."
  summary: |
    场景：交付当天才下单买 Cirrus 订阅，指望立刻导入客户组织。
    后果：eBuy 下单后到 Subscription Manager 可见最长有 24 小时延迟，期间无法 Create Subscription，
    设备只能停留在未授权/受限管理状态，现场开通会卡住。
    规避：提前至少一天（建议留足缓冲）完成 eBuy 下单；开通流程按 eBuy 下单 → Subscription Manager 建订阅
    （记下 Subscription ID + Activation Code）→ OVC 组织内 Import Licenses 三步走。
  tags: [license, subscription, planning, delay]

- id: ce07
  title: OVC 10.4.3 一个邮箱账号只能归属一个 MSP portal——多 MSP 要用子地址
  type: counter-example
  source_chapter: "p198"
  source_quote: |
    "In OVC 10.4.3, a unique account (linked to a mail address) can only be assigned to one MSP portal.
    If a user want access to multiple MSP portals, he must use different mail addresses ...
    Or using the sub-addressing method for his email"
  summary: |
    场景：同一工程师需要访问多个 MSP（托管服务商）portal，例如服务两家不同 MSP 的客户。
    后果：用同一邮箱在第二个 MSP 创建账号会被拒/产生冲突，无法多门户并存。
    规避：每个 MSP portal 用独立邮箱，或用子地址（MyMail+msp1@MyCompany.com、MyMail+msp2@...）派生地址注册；
    激活链接仍发到原始邮箱，主流邮件服务商均支持子地址。
  tags: [account, msp, limitation, workaround]

- id: ce08
  title: 组织级破坏性操作——移出 MSP 后全员失访、误删组织不可恢复
  type: counter-example
  source_chapter: "p208"
  source_quote: |
    "An Organization can be extracted from an MSP ... Be aware that all users within the MSP
    will no longer have access to that organization once removed from the MSP"
  summary: |
    场景：MSP 管理员对组织执行 Disassociate（移出 MSP）或 Delete。
    后果：组织一旦移出 MSP，该 MSP 全部用户立即失去对这个组织的访问（客户侧管理员仍在，但 MSP 侧断管）；
    教材在 Lab 中明确警告"DO NOT use the action Delete on your Organization"（p243），删除组织即丢整个管理面。
    规避：移动组织用 Actions > Change MSP 并填目标 MSP 管理员邮箱；删除/移出前确认客户自有管理员账号可登录；
    生产环境删组织前先导出配置与备份。
  tags: [organization, risk, destructive-action, msp]

- id: ce09
  title: 远程实验室 Reset 脚本加载的"默认配置"不是空配置且所有接口被禁用
  type: counter-example
  source_chapter: "p80"
  source_quote: |
    "WARNING: THE OMNISWITCH SWITCHES DEFAULT CONFIGURATION IS NOT AN EMPTY CONFIGURATION!
    WHEN CLICKING ON THE SHORTCUT: A SPECIFIC CONFIGURATION IS APPLIED TO THE SWITCHES;
    ALL THE INTERFACES ARE DISABLED. DURING THE NEXT LABS, IT WILL BE ASKED TO ENABLE THE INTERFACES THAT YOU WILL USE."
  summary: |
    场景：跑 Reset_PodX 脚本重置实验设备后，发现 AP/客户端全不通。
    后果：脚本给交换机灌的是"特定预配置"（含三层路由、VLAN 等），并把所有接口 disable；忘开端口设备就不通；
    重置耗时约 5 分钟（交换机）/1.5-2 分钟（AP），没等完就操作会误判失败。
    规避：重置后按 Lab 步骤逐个 enable 要用的端口（如 1/1/6 AP 口、1/1/1 客户端口）；
    把这套"预配置底座+手动开端口"的思路类比到生产：区分脚本基线与增量配置，别覆盖基线。
  tags: [lab, reset, switch-configuration, gotcha]

- id: ce10
  title: 重置脚本运行期间按键——一次回车就把交换机带进 Miniboot 中断重启
  type: counter-example
  source_chapter: "p240"
  source_quote: |
    "In the OmniSwitch console window, DO NOT press any key during the reset process.
    Pressing Enter during the OmniSwitch reboot phase will lead you to the Miniboot of the switch
    and interrupt the reboot cycle."
  summary: |
    场景：执行 reset_PODX 脚本时控制台窗口还开着，习惯性敲回车/空格。
    后果：OmniSwitch 重启阶段收到按键会落入 Miniboot 引导模式，重启被中断，设备起不来，
    需要额外干预才能恢复，脚本也可能没跑完。
    规避：脚本执行期间不碰任何控制台；误入 Miniboot 后按交换机 Miniboot 恢复流程处理，再重跑重置脚本。
  tags: [lab, switch, recovery, gotcha]

- id: ce11
  title: 不要对实验室交换机执行真正的恢复出厂——会破坏专用预配置
  type: counter-example
  source_chapter: "p120"
  source_quote: |
    "DON'T TEST THE FOLLOWING PART ON YOUR LAB! THE SWITCHES THAT ARE USED IN OUR REMOTE-LAB ARE
    LOADED WITH A SPECIFIC DEFAULT CONFIGURATION. REINITIALIZING THEM TO THEIR FACTORY DEFAULT
    CONFIGURATION MAY LEAD TO ISSUES!"
  summary: |
    场景：教材附录教了"删除 vcboot.cfg + reload"的交换机恢复出厂方法，学员想在实验室交换机上练手。
    后果：实验室交换机依赖 reset 脚本灌入的专用配置（路由、DHCP relay 等由它承担），真正恢复出厂会让
    整个 POD 断网、后续实验全部失败，且难以自行恢复。
    规避：区分"rm /flash/working/vcboot.cfg + reload from working"这类出厂操作与脚本重置；
    只在自有设备上练习出厂操作。类推到生产：核心/汇聚设备承载隐性依赖（DHCP、路由）时，
    恢复出厂前必须确认没有其他设备依赖其现有配置。
  tags: [lab, switch, destructive-action, risk]

- id: ce12
  title: 树莓派 Wi-Fi 客户端的以太网卡是生命线——动了就失联
  type: counter-example
  source_chapter: "p75"
  source_quote: |
    "Never touch the Ethernet card (configuration or disconnection), because it is from the wired network
    that you can join the raspberry pi desktop."
  summary: |
    场景：远程实验室里通过 VNC 操作树莓派做无线测试，顺手改了有线网卡配置或拔了网线。
    后果：VNC 桌面经由有线网络提供，动以太网卡立即失去对客户端的全部访问，只能等超时或求助管理员重置。
    规避：所有无线实验只在 wlan 接口上做；改 IP/路由前先确认走的不是管理通道。
    一般化为交付守则：任何带外/管理通道（console、mgmt VLAN、VNC 通道）在变更前先保住。
  tags: [lab, client, out-of-band, gotcha]

- id: ce13
  title: 改掉 AP 默认管理 IP 或切成 DHCP 后立刻失联——要用新地址或域名重连
  type: counter-example
  source_chapter: "p127"
  source_quote: |
    "You no longer have access to the access point administration web interface since the administration
    IP address is now dynamically assigned. ... we can no longer use the IP address.
    We will use the URL instead mywifi.al-enterprise.com:8080."
  summary: |
    场景：Express 模式下把 AP 的管理 IP 从默认 192.168.1.254 改为静态新地址（p118），或从静态切到 DHCP（p127）。
    后果：保存瞬间 Web 管理界面失联，用旧地址/默认地址都打不开；所有 Stellar AP 出厂默认管理 IP 相同（192.168.1.254），
    多台 AP 同网段还会地址冲突。
    规避：改完立即用新 IP 重连；DHCP 模式下用域名 mywifi.al-enterprise.com:8080 或从 DHCP 服务器租约表查地址；
    多台 AP 上线前规划好先隔离再改 IP。
  tags: [express-mode, ap-management, ip-address, gotcha]

- id: ce14
  title: 设备激活失败状态集——从错误状态反推原因，VPN profile 变更后必须恢复出厂
  type: counter-example
  source_chapter: "p262"
  source_quote: |
    "Factory Reset required: The VPN profile was changed/updated. A Factory Reset is required on the device.
    ... Unsupported Device Model: OmniVista Cirrus does not support the device."
  summary: |
    场景：Device Catalog 里设备 Activation Status 长期停在失败态。
    教材列出的失败状态（p261）：Failed To Get Certificate、Upgrade Failed、Configuring VPN Failed、
    Provisioning Failed、Device Validation Failed、Factory Reset Required、Unsupported Device Model。
    各自对应：证书服务不可达/时间错误、固件升级失败、VPN 通道建立失败、下发配置处理失败、
    设备校验失败、VPN profile 已变更（唯一解是现场恢复出厂）、型号不支持。
    规避：用 Action > Diagnostic Tools > View Activation Log 看具体原因（p253）；
    换 VPN profile 的变更要预先计划成"需现场 reset"的窗口操作。
  tags: [activation, cloud-onboarding, troubleshooting, vpn]

- id: ce15
  title: Call Home 间隔可能等太久——用 cloud-agent 重启或设备重启强制立即上线
  type: counter-example
  source_chapter: "p250"
  source_quote: |
    "The Activation process is performed automatically on the OmniSwitch and Stellar Access Points.
    But the call home interval might take too much time. You can force the call home
    with one of the following methods of your choice"
  summary: |
    场景：设备已在 Device Catalog 声明，但等它自动 Call Home 完成激活等了很久（默认间隔可到 30 分钟量级）。
    后果：现场交付时间被激活等待拖长，容易被误判为故障。
    规避：OmniSwitch 推荐用 cloud-agent admin-state restart（约 2 分钟走完 Connected to OV → Provisioning → OV Managed），
    或 reload from working no rollback-timeout；Stellar AP 用 firstboot/reboot 触发（p302）。
    排障时 show cloud-agent status（交换机）与 ocloud_show（AP）查看状态与下次 Call Home 倒计时。
  tags: [activation, call-home, troubleshooting, time-saving]

- id: ce16
  title: AP 不上云的三层排障链——L2/PoE/VLAN → AP 侧模式与 DHCP → L3 连通
  type: counter-example
  source_chapter: "p305"
  source_quote: |
    "To register to the OmniVista Cirrus, the Stellar AP must run in OVNG (OmniVista Cirrus) mode:
    support@AP-0E:E0:~$ getmode ... 5.2.3 Checking the Stellar AP DHCP Mode (DHCP/Static):
    support@AP-0E:E0:~$ cat /etc/config/network"
  summary: |
    场景：AP 在 Cirrus 上始终 Waiting for first contact / 不被发现。
    教材标准排障链：L2 层 show lanpower（PoE 是否 Powered On）、show interfaces（线缆 up）、
    show vlan members port（管理 VLAN 是否 default/untagged 在 AP 口上，p304）；
    AP 侧先恢复出厂（Reset 键 6 秒至 LED 闪红，或串口 ssudo firstboot），再 getmode 确认为 OVNG、
    cat /etc/config/network 确认 proto dhcp、ssudo ifconfig br-wan 查 IP、getovinfo 查激活服务器地址（p305-306）；
    L3 层从 AP ping eu.activation.ovng.myovcloud.com 验证路由与 DNS（p306）。
    踩坑点：管理 VLAN 没 untagged 到 AP 口是最常见根因——教材明确"没有 VLAN 10，AP1321 拿不到 IP 也联系不上 Cirrus"（p296）。
  tags: [troubleshooting, cloud-onboarding, vlan, checklist]

- id: ce17
  title: UNP 方式 onboard AP 的安全盲区——AP 不过 802.1x，Rogue AP 的 VLAN 流量照样转发
  type: counter-example
  source_chapter: "p291"
  source_quote: |
    "The Stellar AP is not authenticated with 802.1x.
    If 802.1x is enabled on the port where the Stellar AP is connected, and the Stellar AP fails 802.1x
    authentication, the VLAN-tagged client traffic is trusted and forwarded on the UNP port"
  summary: |
    场景：用 UNP defaultWLANProfile（LLDP 自动分类 AP）开局，同时接入口启用了 802.1x 认证。
    后果：UNP 只靠 LLDP 识别"这是个 AP"，不对其做 802.1x 认证；AP 不响应 EAP 时交换机把它当非 supplicant 设备，
    但其发出的 VLAN-tagged 客户端流量仍被信任转发——私接/仿冒 AP 可以借此把打标签的流量送进内网 VLAN。
    规避：安全要求高的环境不要单独依赖 UNP 分类；在 SSID VLAN 侧加 ACL/策略限制，
    或改用 MACsec/AP 侧 802.1x 等更强准入手段，并配合 WIPS 检测 rogue AP。
  tags: [security, unp, onboarding, rogue-ap]

- id: ce18
  title: 手动分类法开局——每台新 AP 的端口都要手工配全 VLAN，漏配即不通
  type: counter-example
  source_chapter: "p286"
  source_quote: |
    "The AP Management VLAN must be manually configured on the port(s) where the AP devices are connected to.
    If a new AP is connected on a port, the AP Management VLAN AND the VLAN mapped to SSIDs
    must be assigned to this port manually."
  summary: |
    场景：用 Manual Classification（方法 1）开局：AP 管理 VLAN untagged + 各 SSID VLAN tagged 逐口配置。
    后果：扩容加装 AP 时忘配某个 VLAN——管理 VLAN 漏了 AP 不上线；SSID VLAN 漏了对应业务不通，
    且故障隐蔽（其他 SSID 正常）。规模一大配置漂移严重。
    规避：新 AP 上线用固定检查单核对端口 VLAN（管理 untagged + 全部 SSID VLAN tagged）；
    大规模部署改用 UNP 自动分类或模板化配置，减少手工逐口操作。
  tags: [onboarding, vlan, scalability, operations]

- id: ce19
  title: AOS release 5 的 OmniSwitch 不被 OV Cirrus 支持
  type: counter-example
  source_chapter: "p242"
  source_quote: |
    "The Alcatel-Lucent OmniSwitch running in release 5 are not supported by OmniVista Cirrus.
    This is the reason why we do not onboard the OS2360 during these labs."
  summary: |
    场景：存量网络里有 AOS R5 交换机（如 OS2360），想统一纳入 Cirrus 云管。
    后果：R5 交换机无法 onboard 到 OVC，只能本地管理；教材实验中 OS2360 的 VLAN 都要开 console 手工配（p336、p376），
    形成云管/手工双轨。
    规避：规划 Cirrus 统一管理前盘点交换机版本（OVC 支持 8.9RX/8.10RX，p167）；
    R5 设备要么升级要么保留本地管理并写进交付文档，避免交付后"半纳管"状态引发扯皮。
  tags: [compatibility, switch, cloud-onboarding, limitation]

- id: ce20
  title: Device Specific PSK 不支持 AUTO_WPA_WPA2 加密类型
  type: counter-example
  source_chapter: "p327"
  source_quote: |
    "Basic Configuration • Encryption AUTO_WPA_WPA2 is NOT supported • PSK/PassPhrase: only active
    with « Prefer Device Specific PSK » • Device Specific PSK: Enabled"
  summary: |
    场景：SSID 要启用按设备 PSK（DSPSK，MAC 认证后下发该设备专属密码）。
    踩坑点：加密类型选了兼容模式 AUTO_WPA_WPA2 时 DSPSK 直接不可用；SSID 级全局 PSK 只有在
    "Prefer Device Specific PSK" 模式下才能与设备专属 PSK 共存（Force 模式则只认每设备密码）。
    规避：DSPSK 部署统一用明确的 WPA2/WPA3 加密类型，规划好 Force/Prefer 两种模式的选择；
    配套在 Company Property 数据库为设备 MAC 预录专属 passphrase。
  tags: [ssid, security, psk, configuration]

- id: ce21
  title: 认证方式安全权衡——MAC 可伪造无加密、共享 PSK 可被整体破解
  type: counter-example
  source_chapter: "p310"
  source_quote: |
    "MAC authentication • Cons: MAC can be spoofed, no traffic encryption ...
    WPA/WPA2/WPA3 Personal = Pre-Shared Key (PSK) • Pros: Easy set up ... • Cons: But all keys can be
    hacked or stolen (key shared by all users)"
  summary: |
    场景：给打印机/扫描仪等哑设备选 MAC 认证，或图省事全公司用一个 PSK。
    后果：MAC 认证可被克隆绕过且流量不加密；PSK 全员共享，泄露即全网失守，且无法按人撤销。
    规避：哑设备场景用 DSPSK/PPSK（按设备/按组发不同密钥）或 MAC + 动态 VLAN 的组合并配 ACL 收权；
    人员网络用 802.1X（Enterprise）；教材明确开放网络 + Captive Portal "No Security"，只能靠 Portal 与后置策略兜底。
  tags: [security, authentication, ssid, design]

- id: ce22
  title: Guest/BYOD Portal 排障三查——AP 时间、DNS、非 https 触发重定向
  type: counter-example
  source_chapter: "p385"
  source_quote: |
    "A guest account has an expiration date. It is important to check that the date and time
    are correctly set up ... A valid DNS configuration is mandatory in order to redirect
    successfully the client(s) to the Captive Portal page"
  summary: |
    场景：Guest 连上 SSID 后 Portal 页面弹不出来，或账号明明没过期却认证失败。
    根因链：AP 日期/时间不对导致账号有效期判断错误（date 命令核查）；AP 的 resolv.conf DNS 配置缺失
    导致重定向失败（cat /etc/resolv.conf）；Portal 重定向必须由访问非 https URL 触发，
    且 Raspberry Pi/Debian 类系统连上后不会自动弹浏览器，必须手工开浏览器访问 http:// 开头地址（p381）。
    深入排查用 eag_cli show user all 看 portal 认证用户、tail -f /tmp/log/eag.log 看门户日志（p388）。
  tags: [troubleshooting, captive-portal, guest, dns, ntp]

- id: ce23
  title: 802.1X 连不上——查 AP 侧 AAA 配置文件，最后用 tcpdump 抓 RADIUS
  type: counter-example
  source_chapter: "p347"
  source_quote: |
    "If the radius authentication still fails:
    - Capture and analyze the data by using the following command: tcpdump -i br-wan –s 0 host radiusIP
    - Check the Radius server configuration"
  summary: |
    场景：Employee SSID（802.1X）客户端反复认证失败。
    排障链（p345-347）：先确认客户端侧 802.1X 设置与账号无误；再在 AP 上核对下发的配置是否到位——
    cat /var/config/wlanservice.conf（SSID/AAA profile 引用）、AAA_profile.conf（主 RADIUS 服务器）、
    AAA_server.conf（服务器 IP、端口 1812/1813、secret、超时重试）；仍未解决则 tcpdump 抓包看报文交互，
    同时核查 RADIUS 服务器侧配置。
    踩坑点：UPAMRadiusServer 的地址/密钥由云下发，若 Provisioning 未生效，AP 上配置为空而界面看不出。
  tags: [troubleshooting, 802.1x, radius, cli-diagnostics]

- id: ce24
  title: Band Steering 默认禁用的原因——5GHz 覆盖弱/有洞时会把客户端推进火坑
  type: counter-example
  source_chapter: "p459"
  source_quote: |
    "To function properly, band steering generally assumes that the coverage areas on both the 2.4 GHz
    bands and 5 GHz bands are the same ... band steering will prove problematic if coverage on 5 GHz is
    significantly weaker and has coverage holes ... a 5 GHz-capable device is automatically redirected
    to the 5 Ghz band ... even if the 5 GHz signal is low."
  summary: |
    场景：看到 RF Profile 里 Band Steering 默认关闭，想当然打开提性能。
    后果：双频覆盖不对等（5G 穿墙衰减大、有覆盖洞）时，支持 5G 的终端被强行引到 5G 弱信号区，
    体验反而变差；Force 5G/6G 更绝——2.4G 关联请求直接被忽略，弱覆盖区终端无法回退到 2.4G（p460）。
    规避：设计阶段保证 2.4G/5G 覆盖大致对等再开 Band Steering；存量网络覆盖差异大就不开，
    或用 Exclude MAC OUI 把扫描枪、MIPT 电话等老终端排除在牵引之外。
  tags: [rf-management, band-steering, coverage, design]

- id: ce25
  title: Association RSSI Threshold 设得比客户端信号还高——全网客户端被拒之门外
  type: counter-example
  source_chapter: "p463"
  source_quote: |
    "As the Wifi Client RSSI = 51dB is less than the Association RSSI Threshold = 90, then it is not
    possible for the wifi Client (and other devices with a RSSI less than 90) to connect to any SSID
    broadcasted by Access Points assigned to My-AP-Group."
  summary: |
    场景：想用准入 RSSI 阈值赶走弱信号终端，把 Association RSSI Threshold 调得过高（实验里故意设 90）。
    后果：低于阈值的客户端关联请求被 AP 直接忽略，表现为"全网都连不上但设备看起来正常"，
    属于隐蔽的全局性故障；QoE 分析（Network > Analytics > QoE）里能看到 association failure 记录（p464）。
    规避：阈值按推荐值渐进设置（低值 10 放行多弱终端、高值 25 吞吐更好，p451；推荐 2.4G=5、5G=10，p445）；
    变更后立即用 QoE 关联失败数验证，异常立刻回退 RF Profile 到 Default。
  tags: [rf-management, rssi, misconfiguration, recovery]

- id: ce26
  title: 背景扫描期间无线客户端没有数据——入侵检测与性能天生互斥
  type: counter-example
  source_chapter: "p448"
  source_quote: |
    "During scanning wireless clients are impacted – no 802.11 data.
    Scanning is required for WIPS ... Default interval = 20 sec – Range = 5-10800 sec;
    Default Duration = 50 ms – Range = 50-110 ms"
  summary: |
    场景：开着背景扫描（WIPS 必需）同时跑高要求业务。
    后果：每个扫描周期内该 radio 不传 802.11 数据，扫描更频繁/更久则入侵检出率高但客户端性能下降，反之亦然（p451）。
    规避：保留默认 interval 20s/duration 50ms 的平衡点；对语音视频敏感场景开 Voice and Video Awareness
    （检测到 SIP/H.323 会话时跳过扫描）；高要求场景用专用扫描 radio/AP（Dedicated AP scanning mode）；
    RF 环境差且客户端密集时应关闭 Short Guard Interval（p451）。
  tags: [rf-management, scanning, wips, performance, tradeoff]

- id: ce27
  title: Client-aware 关闭时 ACS 换信道会直接打断在线客户端
  type: counter-example
  source_chapter: "p461"
  source_quote: |
    "When enabled, the Auto Channel Selection does not change channels for Stellar APs with connected
    client. When disabled, the Stellar AP may change to a more optimal channel but may disrupt
    connected clients."
  summary: |
    场景：希望自动选信道（ACS）时刻保持最优，把 Per Band 里的 Client-aware 关掉。
    后果：ACS 判定有更优信道就切换，正在连接的客户端会被打断——语音/视频/瘦终端类业务出现闪断。
    规避：有在线客户端的业务网络保持 Client-aware 开启（换信道等客户端走了再说）；
    接受打断换优化的场景（高密度会议室空窗调优）才显式关闭；换信道问题在 AP 上查
    cat /proc/kes_syslog | grep ACS 日志定位（p466）。
  tags: [rf-management, acs, client-impact, configuration]

- id: ce28
  title: 漫游协议有加密前提——OKC 仅限 Enterprise，802.11r 仅限 WPA2/WPA3 加密
  type: counter-example
  source_chapter: "p471"
  source_quote: |
    "L3 Roaming disabled by default ... Fast Roaming disabled by default ... Fast Roaming feature
    configured per SSID: OKC can be enabled with WPA2/WPA3 Enterprise only;
    802.11r (Fast Roaming) can be enabled with WPA2/WPA3 encryption only (Personal or Enterprise)"
  summary: |
    场景：给开放/Portal SSID 或 MAC 认证 SSID 开 802.11r 快速漫游，或给 Personal PSK 网络开 OKC。
    后果：前提不满足时功能不可用或配置被拒——OKC（机会性密钥缓存，802.11k 辅助）只支持 WPA2/WPA3 Enterprise；
    802.11r（FT）要求 WPA2/WPA3 加密（Personal 或 Enterprise 均可），开放网络无从谈起；
    L3 Roaming 与 Fast Roaming 默认都是关闭的，不开就没有相应能力。
    规避：规划漫游先核对 SSID 安全等级（p489 guidelines）；开放 Guest SSID 只能靠普通漫游；
    L3 漫游需求在 SSID 配置里显式开启。
  tags: [roaming, 802.11r, security-prerequisite, configuration]

- id: ce29
  title: 地理相邻的 AP 互相"看不见"——无客户端上下文共享即无漫游
  type: counter-example
  source_chapter: "p491"
  source_quote: |
    "In some cases, Stellar APs are geographical neighbors but can't see each other
    (i.e: radio waves blocked by corridor with right angles,…). Client context can't be shared. No roaming.
    Solution: On both AP, add statically the neighbor Stellar AP from the list of known AP."
  summary: |
    场景：走廊直角、厚重墙体等导致两台物理上相邻的 AP 空口互相探测不到（over-the-air 发现失败）。
    后果：客户端上下文（含 PMK 缓存、VLAN/ARP）无法在两台 AP 间共享，客户端走过去等于全新接入，
    重新全量认证，漫游体验断裂；同理两 AP 射频无重叠覆盖区也无漫游可言（p490）。
    规避：在 AP Registration > Access Point 视图用 Neighbor AP 链接，在两台 AP 上互为静态邻居，
    上下文改走 LAN 交换恢复漫游；勘测阶段用 Heat Map 按 2.4G/5G/6G 分别核对覆盖重叠。
  tags: [roaming, rf-coverage, troubleshooting, workaround]

- id: ce30
  title: Roaming RSSI 阈值的两难——太低粘住弱 AP，太高漫游过频丢包
  type: counter-example
  source_chapter: "p492"
  source_quote: |
    "If the RSSI threshold is too low, the client remains on a low signal strength site, even with a
    stronger site nearby. If the RSSI threshold is too high, the client roams too much
    that could result to packet loss."
  summary: |
    场景：调 Roaming RSSI Threshold 解决 sticky client（终端死守一台 AP）。
    后果：阈值调低，终端继续粘在弱信号 AP 上，整体吞吐被拖垮；调太高，终端频繁切换 AP，
    每次切换带来丢包，实时业务受损。
    规避：按推荐值起步（2.4G RSSI=10、5G RSSI=15，范围 0-100），配合 802.11k/802.11v 让终端获得
    更优漫游目标列表；漫游决定权在终端侧，网络只能引导，调参后用客户端会话历史里的漫游时间线验证。
  tags: [roaming, rssi, tuning, tradeoff]

- id: ce31
  title: 跨云/无 WLAN service 时上下文被丢弃——漫游退化成全新接入
  type: counter-example
  source_chapter: "p475"
  source_quote: |
    "On Receiving AP, Add/Del Message discarded when • AP is not managed by the same OminVista
    Cirrus / Terra • AP does not have the WLAN service"
  summary: |
    场景：两台相邻 AP 分属不同 OVC 实例（如两家 MSP 各管一半），或新 AP 没有配置相同 WLAN service。
    后果：客户端上下文的 Add/Del 消息被接收 AP 丢弃，客户端走过去被当成全新客户端处理（p476 判定表：
    无上下文 → No Roaming, new client），重新认证、重新取 IP，敏感业务中断；
    漫游形态还取决于上下文 VLAN 与新 AP 上 ARP 映射 VLAN 是否一致，一致 L2 漫游、不一致才走 L3 GRE 隧道。
    规避：同一漫游域的 AP 必须同一 OVC 管理、同一 SSID/WLAN service 覆盖；
    AP Group 间 VLAN 映射差异要有意识设计（这正是 L2/L3 漫游选择条件，p476）。
  tags: [roaming, vlan-mapping, design, troubleshooting]

- id: ce32
  title: WIPS Rogue 反制的杀伤半径——de-auth 会波及邻居无线网络，Friendly 一票豁免
  type: counter-example
  source_chapter: "p523"
  source_quote: |
    "Do not modify the parameters, unless instructed to. Actions applied to Rogue AP can have big
    consequences to other wireless networks. ... your Stellar Access Point sends a de-authentication
    packet to the Wi-Fi clients associated to rogue Access Points."
  summary: |
    场景：随手收紧 Rogue AP Policy（信号阈值、SSID 关键字、OUI）或扩大 containment 范围。
    后果：Rogue containment 默认开启，会对被判 Rogue 的 AP 下发 de-auth 打其关联客户端——
    分类参数过宽会把邻居公司/楼上的合法 AP 误判成 Rogue 并持续攻击，引发投诉甚至法律风险；
    反之加进 Friendly 名单的 AP 永不被判 Rogue，即使它广播了命中 Rogue 关键字的 SSID（p525 实验）。
    规避：改策略前评估半径；用 Detect Valid SSID 等精确条件；已知合法的外部 AP（含其他学员 POD 的 AP）加入 Friendly；
    注意一台 AP 双频有多个 BSSID 条目，加 Friendly 时按 OUI 全选（p524）。WIPS 依赖背景扫描开启（p513）。
  tags: [wips, rogue-ap, containment, risk]

- id: ce33
  title: WIPS 客户端黑名单的局限——攻击源 MAC 未必是真实客户端
  type: counter-example
  source_chapter: "p517"
  source_quote: |
    "Limitations: The attacker source MAC can be anything (an AP mac, a BSSID mac, a wireless NIC card mac..)
    Blocklisting the attacker source MAC is only relevant when the source MAC is an actual wireless client"
  summary: |
    场景：检测到无线攻击后启用 Client Blocklist Policy 自动拉黑攻击源 MAC。
    后果：攻击报文的源 MAC 可能是 AP 的、BSSID 的或攻击者伪造的网卡 MAC——只有当它确实是
    无线客户端 MAC 时拉黑才有意义，否则拉黑无效甚至误伤被冒用的合法地址。
    规避：启用前理解该策略适用面（默认关闭、10 次/60 秒认证失败触发、老化 1 天，p524）；
    对 AP 侧攻击依赖 AP/Client Attack Detection 分级检测与 containment，别把黑名单当万能措施。
  tags: [wips, blocklist, security, limitation]

- id: ce34
  title: RAP 部署三坑——AP1101 不兼容、conf 文件必须留存、OV2500 要加回程路由
  type: counter-example
  source_chapter: "p497"
  source_quote: |
    "* AP1101 not compatible with the RAP Feature" (p497);
    "KEEP THIS CONF FILE, AS WE WILL NEED TO IMPORT IT IN THE VPN SERVER VIRTUAL APPLIANCE" (p557);
    "To make it possible for the OmniVista 2500 NMS to reach the Remote Access Point, a default route
    must be created" (p566)
  summary: |
    场景：把 Stellar AP 部署到远程站点做 RAP（经 VPN server 回总部）。
    坑一：选型时挑了 AP1101——该型号不支持 RAP 功能，直接选型失败。
    坑二：Cirrus/OV2500 导出的 VPN 配置 .conf 文件要导入 VPN Server 虚拟机，弄丢就得重导重配。
    坑三：OV2500 NMS 默认到不了 VPN 隧道网段，必须手工加默认路由（如 192.168.0.0/24 网关指向 VPN server 私网 IP），
    否则 RAP 发现不了；SSID 用 Use Tunnel 时 Tunnel ID 必须为 0（p570）。
    规避：RAP 选型避开 AP1101；部署手册把 conf 文件归档；OV2500 路由配置列为必检项；
    用 VPN Server 维护菜单的 VPN Status（peer/handshake/transfer）确认隧道建立（p565）。
  tags: [rap, vpn, compatibility, routing, checklist]

- id: ce35
  title: OV Cirrus 没有一键恢复默认——组织清理必须按依赖顺序手工拆 25 步
  type: counter-example
  source_chapter: "p545"
  source_quote: |
    "The AP Group can only be deleted if no custom provisioning configuration is assigned. ...
    If you get an error while trying to delete it, Edit this profile and set the RF profile parameter
    with 'Default RF Profile'."
  summary: |
    场景：换设备/搬家/重配网络，想把云上组织清回初始状态。
    后果：云平台无法一键还原默认（p544 明示），清理要按依赖顺序走：先把设备移回 default device group、
    AP Group 解绑自定义 Provisioning、Provisioning 里的 RF Profile 改回 Default，才能逐层删除
    AP Group → Provisioning → RF Profile → SSID → 策略/模板 → 账号 → 站点；顺序错了报删除失败。
    规避：把教材 p542-547 的 25 步清理清单作为 SOP 存档；每次交付搭好环境后同步记录创建的对象清单，
    拆除时逆序执行。
  tags: [operations, cleanup, dependency-order, cloud-management]

- id: ce36
  title: 删除 Site 是级联操作——楼栋楼层连同入网设备一起删
  type: counter-example
  source_chapter: "p547"
  source_quote: |
    "This action deletes the site, the building and floors attached, as well as all the network
    devices assigned to the site. The next step is a verification step."
  summary: |
    场景：整理站点结构时删掉一个"看起来只是地图坐标"的 Site。
    后果：级联删除该站点下的 building、floors 以及分配到该站点的全部网络设备（Device Catalog 清空），
    设备纳管关系丢失，需要重新 onboard。
    规避：删 Site 前把设备迁到保留站点；删除后到 Inventory > Device Catalog 核实设备列表状态，
    残留设备手工清除（p547 验证步骤）。
  tags: [site-management, destructive-action, cascade-delete, cloud-management]

- id: ce37
  title: AP 内置 DHCP 地址池大小就是并发设备上限
  type: counter-example
  source_chapter: "p155"
  source_quote: |
    "The DHCP range contains 40 IP addresses. So only 40 devices can be connected simultaneously.
    If a larger amount of employee devices is planned, it is of course possible to increase this amount."
  summary: |
    场景：Express 模式小站点直接用 AP 内置 DHCP server 给 SSID 用户发地址，按实验默认配了 40 个地址的池。
    后果：第 41 台设备拿不到地址无法上网，故障表现为"部分新设备连不上"，与信号无关，易误判为无线问题。
    规避：按并发终端规模规划池大小（含访客/BYOD 峰值与物联网终端）；超规模时扩大池或改用外部 DHCP；
    排障先看客户端是否拿到 IP（ifconfig/ipconfig）再查无线层。
  tags: [dhcp, capacity, express-mode, troubleshooting]

- id: ce38
  title: 员工账号密码策略默认宽松——生产环境必须收紧
  type: counter-example
  source_chapter: "p422"
  source_quote: |
    "Edit employees password and login policy. • Minimum length • Complexity
    Weak password/username by default"
  summary: |
    场景：用 UPAM 本地数据库发员工账号，沿用默认策略（实验里账号密码就是 Employee/password 级别）。
    后果：默认弱密码/弱用户名策略下，账号易被暴力猜测；结合 Blocklist 默认 10 次/60 秒的阈值，
    撞库尝试在告警层面也不显眼。
    规避：上线前在 Employee Accounts Settings 里设置最小长度与复杂度；
    高安全场景认证源改外部 RADIUS/LDAP/Azure AD（p354），并启用账号锁定与审计（Authentication Records）。
  tags: [security, account-policy, upam, hardening]

- id: ce39
  title: 勘测纠出的四类信号杀手——AP 放位、遮挡材料、天线选型、同邻频干扰
  type: counter-example
  source_chapter: "p532"
  source_quote: |
    "Access Point placement: bad location (wall, pillar) ... Place an AP on both side of the obstructing
    wall ... Signal degrades when going through: Concrete (walls), Wood (doors), Metal (cabinet, shelves,…),
    Steel (building structure), Glass & Mirrors, Brick (fireplace), Water"
  summary: |
    场景：网络"性能不行"投诉，现场勘测（Ekahau）后定位。
    教材归纳四类根因：一是 AP 摆在遮挡物正前方形成死区——改为在墙体两侧各放一台；二是材料衰减
    （混凝土、金属货架、钢结构、玻璃镜面、水体都显著衰减，4 米穿 1-4 面墙 RSSI 可掉到 -70dBm，不够 VoWLAN 用，p533）；
    三是天线类型选错——定向天线覆盖区小，该用全向的场景覆盖不达标（p534）；
    四是同频/邻频干扰致吞吐下降丢包——换信道解决（p535）。
    规避：交付后勘测按 Step1 拿平面图圈重点区域 → Step2 核对 AP 型号/重叠/功率/位置 → Step3 出整改
    （换型号、调功率信道、修信道宽度、删低速率逼终端贴近 AP、挪 AP，p537-540）。
  tags: [site-survey, rf-coverage, interference, troubleshooting]

- id: ce40
  title: 教材自身局限——强依赖远程实验室、OV2500 本地 GUI 未覆盖、与售前课内容重叠
  type: counter-example
  source_chapter: "BOOK_OVERVIEW.md"
  source_quote: |
    "强依赖远程实验室（Stellar Remote-Lab），无实验环境时 Lab 章节只能读不能练；
    以 Cirrus 云管为主线，OV2500 本地管的 GUI 操作不在此课；
    内容与《Stellar WLAN Presales》(DT00XPS288) 有概念重叠，但视角完全不同（怎么做 vs 怎么卖）。"
  summary: |
    场景：拿这本书做团队自学或交付 SOP 底稿时高估其覆盖面。
    局限一：全书 Lab 绑定 ALE Remote-Lab POD 环境（账号、Reset 脚本、pfSense/DHCP 服务器均为托管预置），
    没有实验环境时实操章节只能读，需自建等效环境（两台交换机+两台 AP+DHCP+NTP+外网）。
    局限二：RAP 章节虽涉及 OV2500，但 OV2500 本地管理的 GUI 操作不在本课范围，混合管理场景要补其他材料。
    局限三：与售前教材概念重叠，引用时注意区分"部署视角"与"销售视角"。
    规避：培训采购时连 Remote-Lab 一起买；SOP 编写以本课为主线、OV2500 GUI 部分引用官方配置指南补齐。
  tags: [book-limitation, training, scope]
```
