# 陷阱/警告/限制 · OmniAccess Stellar AP User Guide (AWOS 5.0.3)

> 来源：source/fulltext.md（页码即手册 PDF 页码）

- id: ce01
  title: 默认凭据 admin/admin 与必须改密的账户清单
  type: counter-example
  source_chapter: "p14, p16, p33"
  source_quote: |
    Login with the Administrator account and the default password 'admin'. ... It is highly recommended and a best security practice to change the default passwords for the predefined login accounts. ... For security the admin must change the CLI root, and support passwords before use.
  summary: |
    Web 管理员默认密码为 admin。除了 Web 的 Administrator/Viewer/GuestOperator 外，CLI 的 root 与 support 密码"使用前必须修改"（手册原话）。root 密码仅由客户持有、由 AP 生成真实 root 凭据，不改等于把最高权限留在默认态。
  tags: [default-credential, security, cli]

- id: ce02
  title: 开局时一次只接一台 AP
  type: counter-example
  source_chapter: "p13"
  source_quote: |
    Note 3-2: It is recommended to connect only one AP at a time to the network and complete the configuration, then plug in other APs one by one to synchronize the configurations.
  summary: |
    初始化配置时应一次只把一台 AP 接入网络、完成配置后，再逐台插入其他 AP 同步配置。多台同时首次上电会各自成组，配置无法按预期收敛。
  tags: [initial-setup, deployment-order]

- id: ce03
  title: 初始化向导期间终端不能离开 mywifi-xxxx
  type: counter-example
  source_chapter: "p17"
  source_quote: |
    Note 3-9: While configuring the Initialization Wizards, please make sure your configuring terminal is connected to the pre-defined WLAN 'mywifi-xxxx' to keep the communication operational ... If not, you may encounter the following prompt and fail to complete the wizard configuration correctly.
  summary: |
    配置初始化向导全程，配置终端必须保持连在预置 WLAN "mywifi-xxxx" 上；中途切到其他网络会导致向导中断、配置失败。且向导完成后 mywifi-xxxx 即被删除（Note 3-10），后续无线管理必须改连向导里新建的 WLAN 再用新管理员密码登录。
  tags: [initializing-wizard, mywifi-ssid, connectivity]

- id: ce04
  title: 初始化向导不能指定 VLAN
  type: counter-example
  source_chapter: "p16"
  source_quote: |
    Note 3-8: The VLAN assignment for the WLAN is not available in the initial wizard phase. You can modify the mapping VLAN value after the initial setup is completed, using the steps described in "Modify your WLAN" section.
  summary: |
    初始化向导创建 WLAN 时不支持配置 VLAN 映射，只能等向导完成后通过 "Modify Your WLAN" 补配。规划开局时要把 VLAN 调整算作向导后的必做步骤，否则员工/访客业务 VLAN 落不到位。
  tags: [wizard, vlan, two-step]

- id: ce05
  title: AP1201 混入高端组时需手动干预 PVM
  type: counter-example
  source_chapter: "p18"
  source_quote: |
    If AP1201 coexists with AP1220/AP1230/AP1251 in the same cluster, and AP1201 is selected as PVM by the system automatically, suggest to manually intervene and turn one of the AP1220/AP1230/AP1251 to be the PVM for better management performance consideration.
  summary: |
    AP1201 与 AP1220/AP1230/AP1251 同组且被自动选为 PVM 时，建议手动把 AP1220/AP1230/AP1251 提升为 PVM（AP Window 的 "Update to PVM"），否则管理性能受损。同理，AP1101/AP1201H/AP1201L/AP1201HL 当 PVM 时整组只能扩到 32 台。
  tags: [pvm, mixed-model, performance]

- id: ce06
  title: DHCP 失效导致全组 IP 冲突
  type: counter-example
  source_chapter: "p87"
  source_quote: |
    If the APs reboot and the DHCP server is not accessible, all the APs return to the system default IP -192.168.1.254. This means there are duplicate IPs in the broadcast domain. All the APs work separately as the PVM and broadcast the same WLANs.
  summary: |
    AP 重启时若 DHCP 服务器不可达，所有 AP 都回退到默认 IP 192.168.1.254，同一广播域内出现大量 IP 冲突，且每台 AP 各自成 PVM、广播相同 WLAN。手册强烈建议此时先修 DHCP 让无线服务恢复，而不是逐台手工处理。
  tags: [dhcp-failure, ip-conflict, 192.168.1.254]

- id: ce07
  title: 后台扫描关闭或拉长间隔的连锁劣化
  type: counter-example
  source_chapter: "p46"
  source_quote: |
    When it's turned OFF, the foreign AP detection and rogue suppression will stop and the RDA will drop its precision. ... If the interval is longer than 1 minutes, RDA and wIPS feature accuracy will be impacted.
  summary: |
    后台扫描关闭后，外部 AP 检测与 rogue 抑制直接停止、RDA 精度下降；扫描间隔超过 1 分钟也会影响 RDA 和 wIPS 准确性。为时延调大间隔或只扫工作信道时，要接受安全/射频优化能力的损失。
  tags: [background-scanning, rda, wips, tradeoff]

- id: ce08
  title: Allowlist 与 Walled Garden 仅对 Portal 生效
  type: counter-example
  source_chapter: "p53-54"
  source_quote: |
    The allowlist is applied to captive portal authentication ONLY. ... The allowlist does not support Enterprise/Personal WLANs. This means that the clients in the allowlist are not allowed to access Enterprise/Personal WLANs without using correct credentials.
  summary: |
    客户端 Allowlist 只对 captive portal 认证生效，不能豁免 Enterprise/Personal WLAN 的认证（名单里的客户端连这两种 WLAN 仍要正确凭据）。Walled Garden 同样只用于 Portal 场景；要放行某资源必须在认证前知道其 IP 或域名并加入 Walled Garden。而 Blocklist 则是对所有安全等级 WLAN 全局生效的封禁。
  tags: [allowlist, walled-garden, captive-portal, scope]

- id: ce09
  title: CNSA 加密在不支持机型上静默回退 WPA2
  type: counter-example
  source_chapter: "p62"
  source_quote: |
    AP1101 full band does not support WPA3 CNSA encryption, AP1201H and AP1201L 2.4Ghz band does not support WPA3 CSNA encryption. ... When CSNA encryption is applied to an AP that does not support it, the encryption will automatically fall back to non-CSNA mode (WPA2).
  summary: |
    AP1101 全频段、AP1201H/AP1201L 的 2.4G 频段不支持 WPA3 CNSA（Suite B）；对不支持的机型配置 CNSA 时会"自动回退到非 CNSA 模式（WPA2）"，没有报错。高安全场景（政务/金融）按机型核对，否则实际加密强度低于预期。
  tags: [cnsa, wpa3, fallback, silent]

- id: ce10
  title: 固件升级后必须清浏览器缓存
  type: counter-example
  source_chapter: "p79"
  source_quote: |
    Note 6-2: In order to make sure you're running the latest software, we strongly recommend to clear the browsing data in your browser after the software upgrade, including: Cookies, Cache.
  summary: |
    AP 固件升级完成后，官方强烈建议清除浏览器的 Cookies 与 Cache，否则 Web 管理界面可能仍加载旧版本资源、表现异常。这是升级排障时最容易漏掉的一步。
  tags: [firmware-upgrade, browser-cache]

- id: ce11
  title: 低端机型做无线桥接不转发 VLAN 标签
  type: counter-example
  source_chapter: "p106"
  source_quote: |
    AP1201, AP1201L, AP1201H, AP1201HL is low performance than other mid-end/high-end APs, and those APs do not support bridging the packets with VLAN tags, so not recommend deploying wireless bridge with above AP models. ... MESH AP can provide service to wireless client accompanied with MESH link. While Wireless Bridge AP can only provide bridge link.
  summary: |
    AP1201/AP1201L/AP1201H/AP1201HL 不支持带 VLAN 标签的桥接报文，不建议用于无线桥接（MESH 部署则正常）；确需使用要联系 ALE 支持。另外 Wireless Bridge 模式的 AP 只提供桥接链路、不能给无线客户端提供服务，这与 MESH 不同。
  tags: [wireless-bridge, ap1201, vlan-tag]

- id: ce12
  title: 无扫描射频机型进扫描模式会踢掉全部客户端
  type: counter-example
  source_chapter: "p110"
  source_quote: |
    AP models without scanning radio, regular Wi-Fi services will be stopped (all clients will be disconnected). ... AP1451 has scanning radio in 2.4G/5GHz so Wi-Fi clients on 2.4/5GHz will NOT be affected, but 6GHz service will be stopped.
  summary: |
    查看 RF Environment 扫描数据需要 AP 进入扫描模式，但机型差异很大：无扫描射频的机型会中断常规 Wi-Fi 服务（所有客户端掉线）；AP1451 的 6GHz 服务会中断（客户端被挤到 2.4G/5G）；带扫描射频的 Wi-Fi 6/Wi-Fi 7 机型不受影响。生产环境做扫描前先核对机型。
  tags: [scanning-mode, service-interruption, model-difference]

- id: ce13
  title: 组间不漫游与 Enterprise 模式切换的边界
  type: counter-example
  source_chapter: "p86, p24"
  source_quote: |
    Note 6-3: Without Omni Vista management, each group is managed independently and roaming between groups is not supported. ... Convert all the APs in the cluster to be managed through OmniVista On-Premise. Once configured, AP will reboot and register to On-Premise OV server.
  summary: |
    没有 OmniVista 统一管理时，多个 AP 组各自独立管理、组之间不支持漫游——多组方案要用在漫游边界清晰的位置。另外把 AP 切到 Enterprise 模式（转 OV On-Premise 管理）或转换云管时 AP 会重启注册，需在变更窗口执行。
  tags: [roaming, multi-group, enterprise-mode, reboot]

- id: ce14
  title: Portal 账号登录只认本地库且无设备数限制
  type: counter-example
  source_chapter: "p94"
  source_quote: |
    Note 7-2: If you have selected login by account method for the captive portal authentication, it ONLY supports users in the local user database. It does not support connecting to an external authentication server. ... Note 7-3: Single user account can be used by multiple devices simultaneously.
  summary: |
    Portal "账号+密码"登录方式只支持 AP 本地用户库（上限 2000 账户），不能外接认证服务器——需要外部 RADIUS 的场景不要选这种方式。同时单个账号可被无限台设备同时使用，无法按账号限制终端数，防蹭网要靠访问码轮换或行为日志审计。
  tags: [captive-portal, local-db, no-radius, account-sharing]
