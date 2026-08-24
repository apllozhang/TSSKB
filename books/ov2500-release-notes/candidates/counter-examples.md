# counter-examples · OV 2500 NMS 4.9R2 Release Notes

> 提取范围：第 5 章 Known Problems 全量（p24-39）、2.4 HA 安装限制（p19）、1.5.3 功能矩阵中的硬限制（p11-13）。
> 这些是升级评估与排障的第一入口弹药库。页码为 fulltext.md 中 <<<PAGE N>>> 标记的 PDF 页号。

## 5.1 AP 注册（p24）

- id: ce01
  title: IE11 打不开 Stellar AP Web 管理工具
  type: counter-example
  source_chapter: "p24"
  source_quote: |
    Internet Explorer, Version 11 does not work when connecting to a Stellar AP using the AP Web Management Tool. Workaround: Set another web browser as your default browser. PR# OVE-2096
  summary: |
    用 IE11 连接 Stellar AP 的 Web 管理工具完全不可用。规避：换 Chrome/Firefox/Edge 作为默认浏览器。
  tags: [IE11, Stellar AP, Web 管理, 浏览器]

- id: ce02
  title: 802.1X 证书创建时同名 Key File 无法再次上传
  type: counter-example
  source_chapter: "p24"
  source_quote: |
    When you re-load an "Upload Key File" with the same name as the existing key file, the "Import" button is disabled. Files with the same name cannot be uploaded again. Workaround: Upload a file with a different name. PR# OVE-12732
  summary: |
    重新上传与现有密钥文件同名的 "Upload Key File" 时 Import 按钮置灰，同名文件不能二次上传。规避：换一个文件名再传。
  tags: [802.1X, 证书, 密钥文件, 文件名]

## 5.2 Discovery（p24）

- id: ce03
  title: AP Reason Down 字段不随状态恢复空白
  type: counter-example
  source_chapter: "p24"
  source_quote: |
    The "Reason Down" field is blank if an AP is UP. If and AP goes down and then returns to an UP state, the "Reason Down" field does not return to a blank field. Workaround: ... For APs, ignore this field if the AP Status is "Up". No workaround at this time. PR# OVE-2131
  summary: |
    AP down 后再 up，Discovery 里 Reason Down 字段不恢复空白。无修复方案；判断口径：只要 AP Status 是 Up 就忽略该字段，不要拿它做告警依据。
  tags: [Discovery, AP 状态, 显示问题, 监控误报]

- id: ce04
  title: 大量 AP 执行 Save to Running 极慢（约 10 秒/台）
  type: counter-example
  source_chapter: "p24"
  source_quote: |
    Performing a "Save to Running" action on a large number of APs in the Discovery application takes a long time (it takes approximately 10 seconds for each AP). Workaround: No workaround at this time. PR# OVE-2264
  summary: |
    对大批 AP 做 Save to Running 每台约耗时 10 秒，几百台就是小时级。无 workaround；变更窗口要按此估算时长，或分批操作。
  tags: [Discovery, Save to Running, 性能, 批量操作]

- id: ce05
  title: NaaS 设备进入降级模式时 OV 不显示失败原因
  type: counter-example
  source_chapter: "p24"
  source_quote: |
    OmniVista does not indicate the reason for a failure when a configuration or software upgrade through Managed Devices fails because the NaaS license has expired on the device. Workaround: No workaround at this time. PR# OVE-11354
  summary: |
    设备 NaaS 许可过期导致降级模式时，通过 Managed Devices 下发配置或软件升级失败，但 OV 不提示真实原因。排障思路：配置/升级莫名失败且无理由时，先去设备侧查 NaaS 许可状态。
  tags: [NaaS, 降级模式, 升级失败, 排障思路]

## 5.3 Locator（p25）

- id: ce06
  title: Locator 不支持 OS2200，无法定位终端
  type: counter-example
  source_chapter: "p25"
  source_quote: |
    Unable to locate end stations connected to OS2200 Switch. Workaround: The Locator application is not supported on OS2200 switches. PR# OVE-1226
  summary: |
    无法定位接在 OS2200 交换机上的终端——这是功能边界：Locator 应用不支持 OS2200，不要在这类设备上规划终端定位需求。
  tags: [Locator, OS2200, 功能边界]

## 5.4 mDNS（p25-26）

- id: ce07
  title: Chromecast 跨 VLAN 无法被发现、无法投屏
  type: counter-example
  source_chapter: "p25"
  source_quote: |
    if your video source (e.g., Chromebook, laptop) is connected to ... VLAN x, and the Chromecast device is in VLAN Y, the video source cannot see Chromecast device and cannot cast video. Workaround: For service sharing to work, the Chromecast device must be on same VLAN as the video source ... Problem will be fixed on AOS 8.7R2. PR# OVE-8941
  summary: |
    mDNS 服务共享下，视频源（Chromebook/笔记本）与 Chromecast 分处不同 VLAN 时互相不可见、无法投屏。规避：Chromecast 与视频源放同一 VLAN，且接在配置为 mDNS Edge Device 的 AP 上、下挂 mDNS Responder。官方称 AOS 8.7R2 修复。
  tags: [mDNS, Chromecast, 跨 VLAN, 投屏]

- id: ce08
  title: 客户端先接入、管理员后配置 Responder/Edge，服务不共享
  type: counter-example
  source_chapter: "p25"
  source_quote: |
    If a client connects to an SSID on an AP and starts sharing mDNS services before the OmniVista Administrator configures Responder and Edge Devices, services will not be shared with other users. Workaround: Follow the expected mDNS Responder configuration sequence: Configure Responder Switch and Edge Devices first. PR# OVE-9848
  summary: |
    mDNS 配置顺序敏感：客户端先接入并开始共享，之后才配置 Responder/Edge Device 的话，服务不会共享给别人。规避：先配 Responder 交换机与 Edge 设备，再放用户入网；顺序错了就要求用户重新共享一次服务。
  tags: [mDNS, 配置顺序, 服务共享]

- id: ce09
  title: 禁用 mDNS Responder 后 AirPlay 投屏仍能继续
  type: counter-example
  source_chapter: "p25"
  source_quote: |
    Even after the MDNS Responder and mDNS Edge Device are administratively disabled, the MAC Book Client ... is able to cast the video to an Apple TV ... the mirroring continues to work for MAC Book Pro and Apple TV until they are aged out or until they are disconnected and reconnected to the network. Workaround: Informational. PR# OVE-9112
  summary: |
    管理性禁用 mDNS Responder/Edge 后，MacBook 到 Apple TV 的镜像投屏仍继续工作，直到会话老化或断开重连——给人"禁用不生效"的错觉。属预期行为（禁用后只是不再回 mDNS 查询响应包）。安全审计时要知道这条，验证禁用效果需让客户端重连。
  tags: [mDNS, AirPlay, 禁用不生效, 安全审计]

- id: ce10
  title: AP1351/AP1301 只接 Eth1 口时无法部署 mDNS
  type: counter-example
  source_chapter: "p26"
  source_quote: |
    Connecting AP1351/AP1301 to the switch only on Eth1 port does not support mDNS service deployment. Workaround: When deploying mDNS, use either the Eth0 port only or link aggregation (Eth0 and Eth1) on AP1351/AP1301 to connect to the switch. PR# OVE-11033
  summary: |
    AP1351/AP1301 仅用 Eth1 口上联时不能部署 mDNS 服务，AP 也不会加入 Edge 列表。规避：只用 Eth0，或做 Eth0+Eth1 链路聚合。
  tags: [mDNS, AP1351, AP1301, Eth1, 端口]

## 5.5 PolicyView（p26）

- id: ce11
  title: OS6900-Q32 专家模式策略动作不支持 Port Type
  type: counter-example
  source_chapter: "p26"
  source_quote: |
    OS6900-Q32 Does Not Support Port Type in Expert Mode Policy Action. Workaround: No workaround at this time. PR# 201688
  summary: |
    OS6900-Q32 在 PolicyView 专家模式的策略动作里不支持 Port Type。无 workaround，策略设计时避开该机型组合。
  tags: [PolicyView, OS6900-Q32, 专家模式, 策略]

- id: ce12
  title: 从 OV 4.2.2 GA 升级来的策略列表含 Send Trap 属性推不下去
  type: counter-example
  source_chapter: "p26"
  source_quote: |
    The "Send Trap" attribute is present in default policies but is not supported in AOS 8.x switches. If you upgrade to OV 4.3R1 from OV 4.2.2 GA and configured policy lists in OV 4.2.2 GA containing this attribute, you will not be able to push that policy list to devices. Workaround: Create new policies/policy lists to replace the old policy lists containing the attribute. PR# OVE-653
  summary: |
    历史遗留策略里的 "Send Trap" 属性在 AOS 8.x 交换机不支持；从 OV 4.2.2 GA 升级路径带过来的含该属性策略列表将无法推送。规避：新建策略/策略列表替换旧列表（4.2.2 MR2 升级或全新安装不受影响）。
  tags: [PolicyView, Send Trap, 升级遗留, AOS 8.x]

## 5.6 Resource Manager（p26-27）

- id: ce13
  title: OS6900 8.3.1 全量备份丢失 SSH Key 和用户表
  type: counter-example
  source_chapter: "p26"
  source_quote: |
    The SSH Key and User Table are missing after performing a full backup of OS6900 Switch running AOS 8.3.1.R01. User Table cannot be backed up. Workaround: No workaround at this time. PR# 219688
  summary: |
    对运行 AOS 8.3.1.R01 的 OS6900 做全量备份，SSH Key 与 User Table 不会被备份。无 workaround；用备份恢复设备后要手工补这两项，不能假设备份完整。
  tags: [备份, OS6900, AOS 8.3.1, SSH Key, 用户表]

- id: ce14
  title: U-Boot 文件名少一个点导致升级失败
  type: counter-example
  source_chapter: "p26"
  source_quote: |
    If the U-Boot file name is "u-boot.5.2R03.3.tar.gz", the upgrade will fail. Workaround: Rename the U-Boot file to "u-boot.5.2.R03.3.tar.gz". PR# OVE-13346
  summary: |
    文件名 "u-boot.5.2R03.3.tar.gz"（5.2 与 R03 之间缺点号）会让 U-Boot 升级失败。规避：改名为 "u-boot.5.2.R03.3.tar.gz"。经典文件名校验陷阱，遇到 U-Boot 升级报错先查文件名。
  tags: [U-Boot, 文件名, 升级失败, 排障思路]

- id: ce15
  title: OS9907/9912 U-Boot 升级需按 CPU 类型分两次
  type: counter-example
  source_chapter: "p26-27"
  source_quote: |
    When performing a U-Boot upgrade on OS9907 and OS9912 switches, there are two U-Boot files involved: one regular and one Denverton ... The CMM2 and CNI-U20 modules have Denverton CPUs, so the Denverton coreboot Zip file is used (coreboot-uboot.denverton). The CMM1 and all the rest of the NI models have Rangeley CPUs ... PR# OVE-13040, OVE-13032
  summary: |
    OS9907/9912 从 OV 做 U-Boot 升级"不工作"的真相：混装不同 NI 模块时必须执行两次升级、各用对应文件——CMM2/CNI-U20 是 Denverton CPU 用 coreboot-uboot.denverton，CMM1 及其余 NI 是 Rangeley CPU 用 coreboot-uboot。每次升级只对匹配的模块成功。
  tags: [U-Boot, OS9907, OS9912, Denverton, Rangeley, NI 模块]

## 5.7 Topology（p27）

- id: ce16
  title: ERP-RPL 链路的 AMAP 条目不显示，ERPv2 场景应改用 LLDP
  type: counter-example
  source_chapter: "p27"
  source_quote: |
    AMAP is a proprietary protocol and has been deprecated, so AMAP Entries for ERP-RPL Links are not always displayed. Workaround: ... Use LLDP as the adjacency protocol when working with ERPv2. PR# 177202
  summary: |
    AMAP（私有协议，已弃用）在 ERP-RPL 链路上工作不正常，可能影响 ERPv2 功能，拓扑条目也不总显示。规避：跑 ERPv2 时把邻接协议换成 LLDP。
  tags: [AMAP, ERPv2, LLDP, 拓扑, 邻接协议]

- id: ce17
  title: 选中超过 2 台设备时不显示 SPT 可用链路
  type: counter-example
  source_chapter: "p27"
  source_quote: |
    SPT Available links are not shown when more than 2 devices are selected using 'Multiple Selection'. Workaround: SPB Topology will only display SPT links between 2 nodes. If more than 2 nodes are selected, the "Show SPT Available Links" function is disabled. PR# OVE-1491
  summary: |
    SPB 拓扑里 SPT 可用链路只在两台设备之间显示；多选超过 2 节点时 Show SPT Available Links 功能直接禁用。使用习惯：查 SPT 链路一次只选两台。
  tags: [SPB, SPT, 拓扑, 多选]

- id: ce18
  title: AOS 8.8R1 交换机与 AWOS 4.0.4 AP 之间 LLDP 链路不显示
  type: counter-example
  source_chapter: "p27"
  source_quote: |
    If an AP is connected to an OmniSwitch running AOS 8.8R1, the LLDP link between the OmniSwitch and the AP does not always display on the OmniVista Topology Map ... the port alias is not advertised to the AP ... Problem will be fixed in the AOS 8.8R2 release. PR# CRAOS8X-31942
  summary: |
    交换机跑 AOS 8.8R1 时，与 AWOS 4.0.4 AP 间的 LLDP 链路在拓扑图上不总显示，端口别名也不通告给 AP（旧版本 AOS 正常）。无 workaround，AOS 8.8R2 修复。拓扑缺链路先核对交换机 AOS 版本组合。
  tags: [LLDP, 拓扑, AOS 8.8R1, AWOS 4.0.4, 版本组合]

## 5.8 Unified Access（p28-29）

- id: ce19
  title: OS6900-Q32/X72 设备配置里端口与动态服务接入认证档案显示错误
  type: counter-example
  source_chapter: "p28"
  source_quote: |
    Device Config - Port and Dynamic Service Access Auth Profile Displayed Incorrectly for OS6900-Q32/X72 switches. Workaround: Switch issue. No workaround at this time. PR# 219133
  summary: |
    OS6900-Q32/X72 在 Device Config 页面，端口与动态服务接入认证档案显示不正确。属交换机侧问题，无 workaround；核对配置时以设备 CLI 实际配置为准。
  tags: [Unified Access, OS6900-Q32, OS6900-X72, 显示错误]

- id: ce20
  title: 无法查看 AOS 8.2.1 设备的 Access Role Profile
  type: counter-example
  source_chapter: "p28"
  source_quote: |
    Cannot view Access Role Profiles on Device Config Screen. Workaround: No workaround at this time. PR# 220259
  summary: |
    AOS 8.2.1 设备在 Device Config 界面看不到 Access Role Profile（ARP 档案）。无 workaround，需到设备侧查看。
  tags: [Access Role Profile, AOS 8.2.1, 显示问题]

- id: ce21
  title: Unified Policy 开 Reflexive 选项后 Drop 策略漏丢包
  type: counter-example
  source_chapter: "p28"
  source_quote: |
    When a user configured a Layer 3 Destination IP address Unified Policy to "Drop" traffic with the Reflexive option, some packets were not dropped. Workaround: Do not turn on the Reflexive option. PR# OVE-10083
  summary: |
    三层目的地址 Drop 策略叠加 Reflexive 选项时，部分报文未被丢弃——安全策略出现放行漏洞。规避：不要开 Reflexive 选项。做安全阻断类策略时务必检查此项。
  tags: [Unified Policy, Reflexive, Drop 策略, 安全漏洞]

- id: ce22
  title: OS6465/OS6560 策略列表规则不支持源 MAC 条件
  type: counter-example
  source_chapter: "p28"
  source_quote: |
    Policy lists containing a rule with a source MAC address condition are not supported on OS6465/OS6560 switches. This is an AOS restriction on these switches. Workaround: Do not include a source MAC address condition in a policy list rule. PR# OVE-10696
  summary: |
    OS6465/6560 的 AOS 限制：策略列表（policy list）规则里不能带源 MAC 地址条件（单独用源 MAC 条件可以）。规避：策略列表规则里不要放源 MAC 条件。
  tags: [策略列表, 源 MAC, OS6465, OS6560, AOS 限制]

- id: ce23
  title: 客户端 MAC 认证先成功后失败，仍保留成功时的 ARP
  type: counter-example
  source_chapter: "p28"
  source_quote: |
    If a client connected to a switch successfully authenticates but later fails authentication, the switch retains the Access Role Profile (ARP) from the successful authentication ... This issue is resolved in AWOS 5.0.1 and later ... Workaround: No workaround for switches. For APs, upgrade AWOS to 5.0.1. PR# OVE-13317
  summary: |
    交换机侧客户端认证成功后再失败，交换机仍保留成功时分配的 Access Role Profile 并继续生效（从未成功认证过的客户端不受影响）。AP 侧已在 AWOS 5.0.1+ 修复；交换机无 workaround。安全影响：撤销授权不会即时生效，账号失效后客户端可能保持原有权限。
  tags: [MAC 认证, Access Role Profile, 授权残留, AWOS 5.0.1]

- id: ce24
  title: 交换机撤出 VC 后 vcpolicy.cfg 残留，Unified Policy 选择器不显示重复 ID 设备
  type: counter-example
  source_chapter: "p29"
  source_quote: |
    If you remove a switch from a Virtual Chassis (VC) configuration to operate as a standalone unit, the switch still maintains the same VC ID ... Workaround: Delete the "/flash/network/vcpolicy.cfg" file from the standalone switch and reboot the switch to generate a new switch ID. PR# OVC-9896
  summary: |
    从虚拟机箱（VC）拆出交换机后，其 /flash/network/vcpolicy.cfg 仍保留 VC 的 LDAP ID，导致出现重复 ID；Unified Policy Switch Picker 遇到重复 ID 就不全部显示。规避：在独立交换机上删除 /flash/network/vcpolicy.cfg 并重启，重新生成 switch ID。拆 VC 后策略选不到设备先查这里。
  tags: [Virtual Chassis, vcpolicy.cfg, Unified Policy, 重复 ID, 拆箱]

## 5.9 UPAM（p29-31）

- id: ce25
  title: HSTS 网站第二次访问不再重定向到门户页
  type: counter-example
  source_chapter: "p29"
  source_quote: |
    The first time a user opens an HSTS website, they are redirected to the portal page, as expected. The second time a user opens an HSTS website, the redirection will not work ... Chrome is very strict, so the problem is always seen, Firefox is not as strict. PR# OVE-779
  summary: |
    HSTS 网站首次打开能正常重定向到认证门户，第二次失效；清浏览器缓存可恢复一次。与浏览器相关：Chrome 必现，Firefox 稍好。无 workaround。Captive Portal 验收测试要用 HSTS 站点时注意此差异。
  tags: [UPAM, HSTS, 重定向, Captive Portal, 浏览器差异]

- id: ce26
  title: 外部 LDAP 用户配置加密密码后 UPAM 认证失败
  type: counter-example
  source_chapter: "p29"
  source_quote: |
    UPAM authentication does not work if you are using an external LDAP with an Encryption Password (e.g., MD5, SHA) configured for the user. Workaround: If using an external LDAP Server for UPAM authentication, use a plain text password. PR# OVE-818
  summary: |
    外部 LDAP 服务器上给用户配了加密密码（MD5/SHA 等）时 UPAM 认证不工作。规避：外部 LDAP 用户的密码用明文存储。
  tags: [UPAM, 外部 LDAP, 加密密码, 认证失败]

- id: ce27
  title: UPAM Captive Portal 页面不支持完整 HTML 定制
  type: counter-example
  source_chapter: "p29-30"
  source_quote: |
    Full HTML customization is not available when creating UPAM Captive Portal Page in OmniVista. Workaround: No workaround at this time. OmniVista does not support HTML-level customization. PR# OVE-834
  summary: |
    创建 UPAM 认证门户页时不能做 HTML 级别的完整定制。这是产品能力边界，不是 bug；有深度品牌定制需求要在方案阶段就排除。
  tags: [UPAM, Captive Portal, HTML 定制, 功能边界]

- id: ce28
  title: UPAM 作 RADIUS 服务器时，有线 CP 认证依赖客户网络 DNS
  type: counter-example
  source_chapter: "p30"
  source_quote: |
    CP/Guest-Authentication fails with UPAM as RADIUS Server ... Workaround: There must be a DNS Server in the Customer Network for Captive Portal user authentication for wired devices if AOS is the network authenticating device. The DNS must resolve to the secondary OV IP address (UPAM address). This is not required for wireless devices authenticating through an AP. PR# OVE-1693
  summary: |
    AOS 交换机做有线认证设备、UPAM 做 RADIUS 服务器时，门户重定向要求客户网络有 DNS 服务器，且 DNS 要解析到 OV 的辅助 IP（UPAM 地址），否则客户端打不开 redirect-url 门户。无线经 AP 认证无此要求。有线访客网故障先查 DNS。
  tags: [UPAM, 有线认证, DNS, 门户重定向, RADIUS]

- id: ce29
  title: 外部 Windows LDAP 服务器的 802.1X 用户凭据登录失败
  type: counter-example
  source_chapter: "p30"
  source_quote: |
    802.1X Authentication using an external Windows LDAP Server fails when Logging in with user credentials. Workaround: Currently, UPAM does not work when using a Windows LDAP server for external LDAP Authentication. Use OpenLDAP on a Linux machine or AD on Windows Server. PR# OVE-3000
  summary: |
    UPAM 不支持用 Windows LDAP 服务器（Windows 系统上的 LDAP 服务）做外部认证。规避：外部 LDAP 用 Linux 上的 OpenLDAP，或 Windows Server 上的 AD。
  tags: [UPAM, Windows LDAP, 802.1X, OpenLDAP, AD]

- id: ce30
  title: LDAPS 服务器停止后 RADIUS（freeradius）服务无法重启
  type: counter-example
  source_chapter: "p30"
  source_quote: |
    If the LDAPs Server is shut down, the freeradius service goes down and cannot be restarted. This is not an issue for unsecure LDAP, the issue exists only for Secure LDAP. Workaround: Enable the LDAP Server or Disable LDAP/AD Server on the LDAP/AD Configuration Screen (UPAM – Settings – LDAP/AD Configuration). PR# OVE-8986
  summary: |
    安全 LDAP（LDAPS）服务器关停会把 OV 内 freeradius 服务带崩且无法重启；非安全 LDAP 不受影响。规避：恢复 LDAP 服务器，或在 UPAM – Settings – LDAP/AD Configuration 里禁用 LDAP/AD。_LDAPS 后端维护窗口要预告此风险。_
  tags: [UPAM, LDAPS, freeradius, 服务崩溃, 维护窗口]

- id: ce31
  title: Guest 账户过期后状态仍显示 Enabled
  type: counter-example
  source_chapter: "p30"
  source_quote: |
    The Guest Account status in the UPAM Guest Account List still displays "Enabled" after the Validity Period for the account has expired. Workaround: Set the Guest Account Deletion Policy ... to delete accounts after they expire ... immediately upon expiration or set a number of days before deletion (1 – 90 days). PR# OVE-10128
  summary: |
    访客账户过了有效期，列表状态仍显示 Enabled（实际已不可用，纯显示问题）。规避：在 UPAM Guest Access 全局配置里设置过期删除策略——立即删除或 1-90 天后删除，账户到期即从列表清除。
  tags: [UPAM, 访客账户, 过期, 显示问题]

- id: ce32
  title: WiFi4EU 门户默认有效期 30 天，超出 24 小时合规要求
  type: counter-example
  source_chapter: "p31"
  source_quote: |
    The validity period for Captive Portal authentication defaults to 30 days, but WiFi4EU requirement is maximum 24 hours. Workaround: Change the validity period to 24 hours. PR# OVE-11164
  summary: |
    Captive Portal 认证有效期默认 30 天，而 WiFi4EU（欧盟公共 Wi-Fi 项目）要求最长 24 小时，导致 WiFi4EU 客户端不再被重定向到门户。规避：把有效期改成 24 小时。
  tags: [WiFi4EU, 门户有效期, 合规, 访客网络]

- id: ce33
  title: 创建 TLS RADIUS 服务器时界面没有 TLS Port 字段
  type: counter-example
  source_chapter: "p31"
  source_quote: |
    When creating a TLS-enabled Radius server, the Create RADIUS Server screen (Security – Authentication Servers – Radius) does not offer a field to specify the TLS Port value. Workaround: Specify the TLS Port value in the "Authentication Port" field, which is 2083 by default. PR# OVE-12747
  summary: |
    Security – Authentication Servers – Radius 创建启用 TLS 的 RADIUS 服务器时没有 TLS 端口输入框。规避：把 TLS 端口值填在 "Authentication Port" 字段（默认 2083）。
  tags: [RADIUS, TLS, 端口, UI 缺陷, 2083]

## 5.10 用户与用户组（p31）

- id: ce34
  title: 给角色配 Analytics 权限会连带配置 Performance Monitoring
  type: counter-example
  source_chapter: "p31"
  source_quote: |
    if you upgrade to OV 4.3R1 from OV 422 MR2, the default permissions for the Performance Monitoring application are automatically derived from Analytics application permissions because the Performance Monitoring application is a sub-application of the Analytics application. This is expected behavior. PR# OVE-1847
  summary: |
    从 OV 4.2.2 MR2 升级上来的环境，Performance Monitoring 权限自动继承 Analytics 权限（后者是前者的子应用），两者无法完全分开配置。属预期行为；做细粒度权限设计时要知道这条继承关系。
  tags: [权限, Analytics, Performance Monitoring, 升级行为]

## 5.11 VM Manager（p31-32）

- id: ce35
  title: vCenter 的 VM 模板被 OV 当成虚拟设备管理
  type: counter-example
  source_chapter: "p31"
  source_quote: |
    vCenter treats Virtual Machine Templates and Virtual Machines in a similar manner. A MAC address is assigned to templates ... vCenter returns VM Template in the list of Virtual Machines like any other VM, and OmniVista 2500 NMS treats VM Templates like any other Virtual Machine. Workaround: N/A. PR# 163314
  summary: |
    VM 模板会被分配 MAC 且 vCenter 把它当普通 VM 返回，OV 于是把模板也当虚拟设备对待。设计使然（working as designed），统计 VM 数量与许可占用时要意识到模板在列。
  tags: [VMM, VM 模板, vCenter, 计数]

- id: ce36
  title: 多物理网卡 VM 在 VMM Locator 中显示多行
  type: counter-example
  source_chapter: "p31-32"
  source_quote: |
    If VMs are using multiple Physical NIC Interfaces, the same VM will be bound to different MAC Addresses and OmniVista 2500 NMS will display multiple rows for the VM in VMM Locator ... the VMM License Manager will count multiple references as single Virtual Machine its UUID. PR# 163885
  summary: |
    VM 配多块物理网卡时绑定多个 MAC，VMM Locator 搜索/浏览里同一 VM 出现多行，看起来数量超过许可或 vCenter 上报值。实际许可按 UUID 只计一台，不影响授权；只是显示冗余。
  tags: [VMM, Locator, 多网卡, 计数, 许可]

- id: ce37
  title: 删除 LAG 口默认 UNP 后 VLAN 通知延迟产生
  type: counter-example
  source_chapter: "p32"
  source_quote: |
    VLAN notification does not come up when the default UNP of a Link Agg Port is deleted ... When the default UNP is taken away from the LAG, the switch takes longer than usual to populate the MAC Learning Table ... Both commands 'show unp user' and 'show mac-learning' have no entry of the VM's MAC address. PR# 174181
  summary: |
    从链路聚合口删除默认 UNP 后，交换机回填 MAC 学习表比正常慢，期间 VM 的 MAC 在 show unp user / show mac-learning 里都查不到，VLAN 通知要等交换机表填完才出现。交换机侧问题，普通物理口无此现象；运维时表现为"VM 短暂失联又自愈"。
  tags: [VMM, UNP, LAG, MAC 学习表, 通知延迟]

## 5.12 Web Content Filtering（p32-33）

- id: ce38
  title: 手机 App 流量绕过 WCF 过滤
  type: counter-example
  source_chapter: "p32"
  source_quote: |
    When client access uses a mobile application (e.g., Facebook, Twitter, YouTube, etc.), there are no restrictions; the application is not blocked and will load properly, as if WCF is disabled on the AP. Workaround: No workaround at this time. PR# OVE-10205
  summary: |
    客户端用手机 App（Facebook、Twitter、YouTube 等）访问时 WCF 完全不拦截，如同未开启。无 workaround；WCF 只能管浏览器流量，做上网行为管控方案时必须把 App 流量的豁免算进去。
  tags: [WCF, 移动应用, 过滤失效, 方案边界]

- id: ce39
  title: 客户端走 HTTP/HTTPS 代理上网时 WCF 失效
  type: counter-example
  source_chapter: "p32"
  source_quote: |
    When a client is behind a proxy, the client doesn't request the AP to resolve the DNS query but directly requests the proxy server. As a result, the AP does not get the opportunity to perform the WCF function. PR# OVE-11466
  summary: |
    客户端配置了代理后，DNS 请求直接发给代理服务器，AP 拿不到解析机会，WCF 的允许/拦截策略失效。无 workaround；部署 WCF 的前提是客户端直连 DNS。
  tags: [WCF, 代理, DNS, 过滤失效]

- id: ce40
  title: HA 升级后再做 failover，WCF 失效且许可信息错误
  type: counter-example
  source_chapter: "p32-33"
  source_quote: |
    After you upgrade an HA installation from 4.8R1 to 4.8R2 ... 4. Perform a failover operation ... 5. After the failover, WCF is no longer enabled and the WCF licensing information is incorrect on the Active node (OV1). Workaround: Manually restart the WMA service. PR# OVE-13159
  summary: |
    场景链：4.8R1 HA 双节点（已启用 WCF）→ 先 Standby 后 Active 升到 4.8R2（升级后角色互换）→ 再做一次 failover 切回原 Active → 该节点 WCF 不再启用且许可信息错误。规避：手工重启 WMA 服务。升级后凡做过 failover 的 HA 环境都要复查 WCF 状态。
  tags: [WCF, HA, 升级, failover, WMA 服务]

## 5.13 WLAN（p33-34）

- id: ce41
  title: GRE 隧道档案 Entropy 与 Tunnel ID 的组合规则
  type: counter-example
  source_chapter: "p33"
  source_quote: |
    You can create two tunnel Profiles with the same Remote IP address and VPN-ID and a different Entropy Status ... but the configuration will not work ... The following combinations of values are not supported: Tunnel ID > 0 and Support of Entropy = Disabled; Tunnel ID = 0 and Support of Entropy = Enabled.
  summary: |
    同一 Remote IP + VPN-ID 建两条 Entropy 状态不同的隧道档案时配置不生效。规则：四类合法场景——AP→AOS 交换机 GRE 隧道（Tunnel ID 非 0 + Entropy 开）；AP→非 AOS 交换机/服务器（ID=0 + Entropy 关）；AP↔OV VPN Server 数据 VPN（ID=0 + 关）；数据 VPN 之上再 GRE 到 AOS（ID 非 0 + 开）。非法组合：ID>0+关、ID=0+开。配隧道前对照本表。
  tags: [GRE 隧道, Entropy, Tunnel ID, VPN, 配置规则]

- id: ce42
  title: 2 万台侵入式 AP 时页面与部件超时
  type: counter-example
  source_chapter: "p33"
  source_quote: |
    There are around 20000 intrusive APs on the customer side. WMA needs 65 seconds to query the completed data. However, the policy queries timeout is 50 seconds, causing the timeout error. Workaround: No workaround at this time. PR# OVE-9693
  summary: |
    客户侧约 2 万台侵入式（rogue）AP 时，WMA 完整查询需 65 秒而策略查询超时上限 50 秒，页面报超时。无 workaround；大规模无线环境的侵入式 AP 页面不可作为可靠数据源。
  tags: [WMA, 侵入式 AP, 超时, 大规模]

- id: ce43
  title: AP1201BG 不支持 RF Profile（BLE 网关）
  type: counter-example
  source_chapter: "p34"
  source_quote: |
    Stellar OAW-AP1201BG does not support RF profiles, as it is a BLE gateway. Workaround: No workaround at this time. PR# OVE-10781
  summary: |
    OAW-AP1201BG 本质是 BLE 网关，不支持 RF Profile。给 AP 组统一下发 RF 配置时要把它排除在外。
  tags: [RF Profile, AP1201BG, BLE 网关, 功能边界]

- id: ce44
  title: Standby 节点 WMA 长期显示 Not Responding
  type: counter-example
  source_chapter: "p34"
  source_quote: |
    Sometimes WMA will stay in a "Not Responding" state on the Standby node. This has no impact to OmniVista or network operations when this occurs. Workaround: When the Standby node becomes Primary, the WMA status will automatically change to "Running". PR# OVE-10513
  summary: |
    HA 备节点上 WMA 服务可能停在 Not Responding 状态，对 OV 与网络运行无实际影响；该节点转主后状态自动恢复 Running。巡检看到备节点 WMA 异常不要误判故障。
  tags: [WMA, Standby 节点, HA, 巡检误报]

- id: ce45
  title: 无线客户端摘要信息不全（浏览器与服务器时区不一致）
  type: counter-example
  source_chapter: "p34"
  source_quote: |
    The wireless client device summary in OmniVista is not displaying the complete information when querying the data. Workaround: Set the timezone of the browser to the same as that of the server. PR# OVC-9976
  summary: |
    无线客户端设备摘要查询显示信息不完整。规避：把浏览器时区设置成与服务器一致。报表数据"缺行"先查时区。
  tags: [无线客户端, 时区, 报表, 显示问题]

## 5.14 其他（p34-39）

- id: ce46
  title: OS6450 的 U-Boot 版本在库存报告里显示 NA
  type: counter-example
  source_chapter: "p34"
  source_quote: |
    U-Boot Version for OS6450 Devices Shows as "NA" in OmniVista 2500 NMS Inventory Report. Workaround: This is a hardware issue with the OS6450. No workaround at this time. PR# 181085
  summary: |
    OS6450 硬件限制：U-Boot 版本在 OV 库存报告中显示 NA。做固件基线盘点时该机型该项无数据属正常。
  tags: [U-Boot, OS6450, 库存报告, 硬件限制]

- id: ce47
  title: Windows 2012 R2 上 IE 用 IP 地址本地访问 Web UI 失败
  type: counter-example
  source_chapter: "p34"
  source_quote: |
    Unable to access Web UI using IP address on Internet Explorer browser, locally on a Windows 2012 R2 system. Workaround: Have the correct mapping for 'localhost' in the hosts file and use 'localhost' instead of IP address to access the Web UI locally. PR# 194913
  summary: |
    在 Windows 2012 R2 本机用 IE 按服务器 IP 访问 OV Web UI 失败。规避：hosts 文件里正确映射 localhost，本地访问改用 localhost。
  tags: [IE, 本地访问, hosts, Windows 2012 R2]

- id: ce48
  title: SNMP community 字符串不能含撇号（单引号）
  type: counter-example
  source_chapter: "p34"
  source_quote: |
    Apostrophe Is an Invalid Character in SNMP Community String. Workaround: Remove Apostrophe from the SNMP community string. PR# 195715
  summary: |
    SNMP community 字符串里的撇号（'）是非法字符。规避：从 community 字符串中去掉撇号。自动化脚本生成凭据时提前过滤。
  tags: [SNMP, community, 非法字符]

- id: ce49
  title: OV 主机名最多 15 字符
  type: counter-example
  source_chapter: "p35"
  source_quote: |
    When configuring the OmniVista Hostname in the VA Menu, the name can contain a maximum of 15 characters. Workaround: Informational. PR# CRNOV-793
  summary: |
    VA 菜单里配置 OV 主机名上限 15 字符（与 NetBIOS 类限制相关）。命名规范里提前约束，另注意 HA 环境主机名不能用大写（见 ce69）。
  tags: [主机名, VA 菜单, 命名规范]

- id: ce50
  title: 添加 Hyper-V Hypervisor 报错：DCOM 与防火墙未就绪
  type: counter-example
  source_chapter: "p35"
  source_quote: |
    Error messages are displayed when trying to add a Hyper-V Hypervisor in the VM Manager Hypervisor Systems Screen. Workaround: Make sure that the VMM Ports are configured as shown in Section 2.2.1 ... If the problem persists, follow the applicable DCOM procedure as detailed in Appendix A. PR# OVE-1568
  summary: |
    VM Manager 里添加 Hyper-V 宿主机报错。规避两步走：先按 2.2.1 端口表放通 VMM 端口（TCP 135 + RPC 动态口 49152-65535），仍失败则按附录 A 的 PowerShell 脚本启用 DCOM（单机版与 HA 集群版脚本不同，均需先备份注册表）。
  tags: [VMM, Hyper-V, DCOM, 防火墙, 附录 A]

- id: ce51
  title: HA 节点数据同步期间发生 failover，Standby 起不来
  type: counter-example
  source_chapter: "p35"
  source_quote: |
    there could be a case when a failover occurs during a sync between the Active and Standby Nodes in a High-Availability Installation. Since the failover interrupts the data sync, the Standby Node will not come up as the Active Node because it does not have the latest data ... On the HA Virtual Appliance Menu select 3 – Configure Cluster, then select 14 – Cluster Error Check. PR# OVE-1629
  summary: |
    极端场景：同步期间 failover，备节点因缺最新数据无法升主。处理：若原主只是临时故障可等它回来补完同步；若原主彻底挂了，SSH 到备节点，HA VA 菜单 → 3 Configure Cluster → 14 Cluster Error Check，检查完成后备节点升主（可能缺最近数据）。这是 HA 应急手册必备步骤。
  tags: [HA, failover, 数据同步, 应急处理, Cluster Error Check]

- id: ce52
  title: 导入口令保护私钥的 SSL 证书后 Nginx 起不来
  type: counter-example
  source_chapter: "p35"
  source_quote: |
    If you update the OmniVista SSL Web Certificate using the VA Menu option, The OmniVista Nginx Service does not start up even if the VM is restarted. Workaround: OmniVista does not support importing a Web Server SSL certificate with private key that was encrypted with password. Import a new SSL certificate with a private key not protected with a password and reboot OmniVista. PR# OVE-1776
  summary: |
    OV 不支持导入私钥带口令加密的 Web 服务器 SSL 证书；导入后 Nginx 服务无法启动，重启 VM 也没用。规避：换用私钥不带口令的证书重新导入并重启 OV。证书替换 SOP 里必须写明"私钥不得加密"。
  tags: [SSL 证书, Nginx, 私钥口令, 证书替换]

- id: ce53
  title: 运行中修改系统端口后，代理类功能断网
  type: counter-example
  source_chapter: "p35-36"
  source_quote: |
    If a user changes the System Port using the VA Menu on a system that has been running, the system will not be able to reach the internet (for PALM, upgrades, etc.) via the network proxy since the port has been changed. Workaround: Change the Proxy Port back to correct network Proxy Port. Go to Preferences - System Settings - Proxy. PR# OVE-2127
  summary: |
    系统运行后用 VA 菜单改系统端口，会导致经代理的外网访问（升级、原 PALM 等）失败。规避：到 Preferences – System Settings – Proxy 把代理端口改回正确值。
  tags: [系统端口, 代理, VA 菜单, 升级失败]

- id: ce54
  title: Web 客户端报 "OmniVista Error Fail to get current user"
  type: counter-example
  source_chapter: "p36"
  source_quote: |
    OmniVista became unavailable to web clients, displaying the following error message on the browser: "OmniVista Error Fail to get current user". Workaround: Restart ovclient or tomcat service. PR# OVE-2220
  summary: |
    Web 客户端整体不可用并报 "Fail to get current user"。规避：重启 ovclient 或 tomcat 服务。Web 整体故障的快速恢复手段。
  tags: [Web 不可用, ovclient, tomcat, 服务重启]

- id: ce55
  title: AOS 6.4.6 交换机不能推送含 IPv6 条件的策略
  type: counter-example
  source_chapter: "p36"
  source_quote: |
    User cannot push policies with IPv6 Conditions to AOS 6.4.6 switches. IPv6 is not supported on AOS 6.4.6 switches. It is only supported on AOS 6.7.2R7 and later, and AOS 8.6R2 and later. Workaround: Upgrade to a supported build. PR# OVE-5793
  summary: |
    IPv6 策略条件仅支持 AOS 6.7.2R7+ 与 AOS 8.6R2+，AOS 6.4.6 不支持推送。规避：升级交换机固件。IPv6 策略 rollout 前先做交换机版本清点。
  tags: [IPv6, 策略推送, AOS 6.4.6, 版本要求]

- id: ce56
  title: 4.4R2→4.5R1/4.5R1→4.5R2 升级选 Download Only 会失败
  type: counter-example
  source_chapter: "p36"
  source_quote: |
    When upgrading the OmniVista VA from 4.4R2 to 4.5R1 or from 4.5R1 to 4.5R2, the VA displays an error and the download fails when choosing the "Download only" option during the upgrade. Workaround: You must use the 'Download and Upgrade" option. PR# OVE-8050
  summary: |
    从 4.4R2 升 4.5R1 或 4.5R1 升 4.5R2 时，"Download Only" 选项报错失败。规避：这两段升级必须选 "Download and Upgrade"。老版本升级路径上的历史坑。
  tags: [升级, Download Only, 4.4R2, 历史问题]

- id: ce57
  title: Firefox 显示大量设备时卡顿告警
  type: counter-example
  source_chapter: "p36"
  source_quote: |
    A warning message appears when using a Firefox Browser to view a large number of devices on the Managed Devices Screen – "A webpage is slowing down your browser". This occurs when the response returned from the server exceeds 1MB. PR# OVE-8019
  summary: |
    Firefox 打开大量设备的 Managed Devices 页会报 "A webpage is slowing down your browser"（服务器响应超 1MB 触发）。规避：优先用新版 Chrome/Edge；坚持用 Firefox 则在 about:config 里把 devtools.netmonitor.responseBodyLimit 设 0、dom.max_script_run_time 设 20。
  tags: [Firefox, 性能, 大列表, about:config]

- id: ce58
  title: 加入集群时 VA 控制台 stdin/stdout 警告可忽略
  type: counter-example
  source_chapter: "p36"
  source_quote: |
    While joining the peer node, the message "WARN: stdin/stdout is not a TTY; using /dev/console" may be displayed. This happens because OmniVista opens an internal session to a DRBD service for synchronizing data between two nodes. Workaround: You can ignore this message. PR# OVE-10576
  summary: |
    节点加入 HA 集群时控制台可能打印 "WARN: stdin/stdout is not a TTY; using /dev/console"，源于 OV 为双节点同步打开 DRBD 内部会话。可忽略，不影响 Join Cluster。
  tags: [HA, DRBD, 控制台告警, 可忽略]

- id: ce59
  title: VA 登录屏提示 cockpit.socket 信息属正常
  type: counter-example
  source_chapter: "p37"
  source_quote: |
    The message "Activate the web console with: systemctl enable –now cockpit.socket" appears on the login screen. Workaround: Ignore this message; it is normal. PR# OVE-12730
  summary: |
    VA 控制台登录屏出现 "Activate the web console with: systemctl enable –now cockpit.socket" 属正常提示，忽略即可。
  tags: [VA 控制台, cockpit, 可忽略]

- id: ce60
  title: VMware 环境 Flexible NIC 升级 4.8R1 失败
  type: counter-example
  source_chapter: "p37"
  source_quote: |
    When using VMWare hypervisor to upgrade from a previous release to 4.8R1, the upgrade will fail if a Flexible NIC was used. Workaround: Re-configure the IP with a different NIC type. PR# OVE-12783
  summary: |
    VMware 上用 Flexible NIC 的 VA 升级 4.8R1 会失败。规避：换一种网卡类型重新配置 IP 再升级。
  tags: [VMware, Flexible NIC, 升级失败, 网卡类型]

- id: ce61
  title: KVM 上 OV 检测不到前两块新增硬盘
  type: counter-example
  source_chapter: "p37"
  source_quote: |
    OmniVista on KVM does not detect the first two disks but does detect the third disk onward ... Workaround: 1. Add "SATA disk1" with 1KB capacity ... 3. Add "SATA disk3" with the desired capacity ... 5. Do not remove "SATA disk1" and "SATA disk2". PR# OVE-13167
  summary: |
    KVM 部署的 OV 检测不到新增的前两块磁盘（默认 VirtIO 两盘之外，SATA disk1/disk2 不可见，从第三块起可见）。扩容操作法：disk1、disk2 各给 1KB 占位，容量全给 disk3，VA 菜单里用 disk3 扩容，且占位盘不许删除。
  tags: [KVM, 磁盘扩容, SATA, 占位盘, VA 菜单]

- id: ce62
  title: L3 HA 备节点接管后 Top N 应用/客户端停止采集
  type: counter-example
  source_chapter: "p37"
  source_quote: |
    In an L3 High Availability configuration, when the standby node takes over from the primary node, the Top N Application and Top N Clients stop collecting data. Workaround: No workaround at this time. PR# OVE-13474
  summary: |
    L3 HA 配置中备节点接管主节点后，Top N Application 与 Top N Clients 停止数据采集。无 workaround；L3 HA 环境的流量分析报表在 failover 后会出现数据断档。
  tags: [L3 HA, Top N, 接管, 数据断档]

- id: ce63
  title: OS6570M 的 8.9R4 U-Boot 只认签名镜像，升级后不可降级
  type: counter-example
  source_chapter: "p37-38"
  source_quote: |
    If the U-Boot and AOS version is 8.9R4 or above and you downgrade the AOS version to 8.9R3 and reboot the switch, the switch cannot reboot. The 8.9R4 U-Boot only accepts signed images. OS6570M has a signed image; there is no unsigned image. PR# OVE-13356
  summary: |
    单向门闩：U-Boot 升到 8.9R4+ 后只接受签名镜像；OS6570M 恰好只有签名镜像（其余机型为非签名），于是 OS6570M 一旦升到 AOS 8.9R4/8.10R1 就无法降回 8.9R3 及以下，强降会变砖（无法重启）。旧 U-Boot（不做签名校验）的 OS6570M 升降自由。升级评审必须把"能否回退"纳入评估。
  tags: [OS6570M, U-Boot, 签名镜像, 不可降级, 升级风险]

- id: ce64
  title: AP1511 与 AP1521 不支持应用可见性（DPI）
  type: counter-example
  source_chapter: "p38"
  source_quote: |
    The Application Visibility (DPI) feature is not supported on the AP1511 and AP1521 in this release. Workaround: Informational.
  summary: |
    本版本 AP1511、AP1521 不支持 Application Visibility（深度包识别）。选型或启用 DPI 签名档案时排除这两个型号。
  tags: [应用可见性, DPI, AP1511, AP1521, 功能边界]

- id: ce65
  title: 拔线触发 failover 后，原 Active 节点重连时自动重启
  type: counter-example
  source_chapter: "p38"
  source_quote: |
    When the network cables for the active node (OV1) are disconnected, the standby node (OV2) becomes the active node. When the OV1 node is then reconnected to the network, OV1 (now the standby node) automatically reboots. However, both nodes continue to function normally despite the reboot of OV1. PR# OVE-13650
  summary: |
    HA 主节点断网线 → 备节点升主 → 原主节点重新接入时自动重启（转为备角色），但双节点随后工作正常。已知问题、后续版本修复；演练拔线测试时预期到这次自动重启，不要当成二次故障。
  tags: [HA, 拔线测试, 节点重启, failover]

- id: ce66
  title: HA 4.9R1 升 4.9R2 时的数据同步警告
  type: counter-example
  source_chapter: "p38"
  source_quote: |
    When upgrading from OmniVista HA 4.9R1 to HA 4.9R2, you may encounter the following warning message: Please make sure data is fully synchronized between 2 nodes before continue ... Workaround: Wait enough time to allow all services to come up after upgrading the Standby Node to upgrade the Active Node. This issue is fixed in the next release. PR# OVE-13842
  summary: |
    HA 4.9R1→4.9R2 升级中可能出现 "请确认两节点数据已完全同步" 的警告。规避：升完 Standby 后等足够时间让所有服务起来，再去升 Active。下版本修复。
  tags: [HA, 升级警告, 数据同步, 4.9R2]

- id: ce67
  title: 升级到 4.9R2 后 Enforce Strong Password 被自动启用并强制改密
  type: counter-example
  source_chapter: "p38-39"
  source_quote: |
    If you disable the Enforce Strong Password setting in OmniVista 4.9R1, then upgrade to release 4.9R2 ... The Enforce Strong Password setting is automatically enabled. OmniVista logs you out and requires you to change your password. Workaround: Change the password and log in again with the new password. PR# OVE-13859
  summary: |
    在 4.9R1 关掉了强口令设置、升级到 4.9R2 后：强口令设置会被自动重新启用，且系统强制登出要求改密。规避：按提示改密后重新登录。升级公告里要提前告知所有用户，避免升级后大面积"登不上去"的工单。
  tags: [强口令, 升级, 强制改密, 用户通知]

- id: ce68
  title: OS6860/6860E 跑 AOS 8.10R3 时无法应用 DPI 签名档案
  type: counter-example
  source_chapter: "p39"
  source_quote: |
    When applying an Application Visibility (DPI) signature profile to an OmniSwitch 6860/6860E running AOS 8.10R3, an error occurs. However, signature profiles applied to an OmniSwitch 6860/6860E running an earlier AOS release, continue to function after an upgrade to AOS 8.10R3. Workaround: There is no workaround at this time. (CRAOS8X-53944)
  summary: |
    对跑 AOS 8.10R3 的 OS6860/6860E 新下发 DPI 签名档案会报错；但升级前已下发的档案在升到 8.10R3 后仍继续工作。无 workaround；存量环境可先升交换机（档案保留），新配置要等修复。
  tags: [应用可见性, DPI, OS6860, AOS 8.10R3, 签名档案]

## 2.4 HA 安装限制（p19）

- id: ce69
  title: HA 安装不支持的功能清单（IP/主机名/内存同步/L2 转 L3）
  type: counter-example
  source_chapter: "p19-20"
  source_quote: |
    The following functionality is not supported in a High-Availability (HA) Installation: Cluster IP configuration in L3 Cluster; Converting 4.9R2 Standalone to 4.9R2 HA if the 4.9R2 Standalone was upgraded from 4.3R1 Standalone; Changing the OmniVista IP address and Hostname after creating the Cluster; Hostname in upper case; Memory synchronization ... Failover while re-syncing between nodes.
  summary: |
    HA 安装的七条硬限制：L3 集群不支持集群 IP 配置；从 4.3R1 单机升级链来的 4.9R2 单机不能转 HA（4.7R1 Patch 2 及之后可以）；建集群后不能改 OV 的 IP 与主机名；主机名不能大写；不做内存同步（服务故障切换时内存数据丢失）；节点重同步期间不能 failover；L2 HA 不能转 L3 HA（只能全新 L3 安装，或给全新 4.9R2 单机加节点/4.9R1 单机升级后转 L3）。架构设计阶段逐条核对。
  tags: [HA, 安装限制, 主机名, 集群 IP, L2 转 L3]

## 1.5.3 功能矩阵硬限制（p11-13）

- id: ce70
  title: VM Manager 仅支持 Hyper-V 2012/2012R2/2016，且只认证英文版
  type: counter-example
  source_chapter: "p12"
  source_quote: |
    The VM Manager (VMM) application is supported on Hyper-V 2012, 2012 R2, and 2016. VMM is not supported on Hyper-V 2019 or higher ... only the English version of third-party software (VMware's vSphere or Microsoft Hyper-V) that VM Manager interfaces with is tested and certified ... VM Manager does not support Windows server 2022. VMM VLAN configuration is not supported.
  summary: |
    VMM 应用只支持 Hyper-V 2012/2012R2/2016；Hyper-V 2019+ 与 Windows Server 2022 均不支持；对接的第三方虚拟化软件只有英文版经过测试认证（其他语言"可能可用但不认证"）；VMM 的 VLAN 配置功能不支持。新虚拟化平台环境基本告别 VMM，需走其他管理途径。
  tags: [VMM, Hyper-V 2019, Windows Server 2022, 英文版, 功能边界]

- id: ce71
  title: OS2260/OS2360 不支持动态 VLAN 配置
  type: counter-example
  source_chapter: "p12"
  source_quote: |
    Dynamic VLAN configuration is not supported on OS2260 and OS2360 switches; only static VLAN configuration and MVRP is supported.
  summary: |
    OS2260/OS2360 只支持静态 VLAN 配置与 MVRP，不支持动态 VLAN 下发。VLAN 自动化方案里这两款要单独处理。另：Analytics 的 Top N Clients 也不支持这两款（矩阵注 14）。
  tags: [动态 VLAN, OS2260, OS2360, MVRP, 功能边界]

- id: ce72
  title: IoT Enforcement 仅限 OS6560-P48Z16 特定部件号
  type: counter-example
  source_chapter: "p12"
  source_quote: |
    IoT Enforcement is only supported on OS6560-P48Z16 models with part number 904044-90. Models with part number 903954-90 are not supported.
  summary: |
    IoT 强制（Enforcement）只支持部件号 904044-90 的 OS6560-P48Z16；同型号部件号 903954-90 不支持。采购与启用 IoT 管控前必须核对部件号，同型号不同 PN 能力不同。
  tags: [IoT, Enforcement, OS6560-P48Z16, 部件号]

- id: ce73
  title: WCF 与应用可见性在部分 AP 型号上不可用
  type: counter-example
  source_chapter: "p12"
  source_quote: |
    Web Content Filtering is supported on Stellar APs running AWOS 4.0.2 and higher (except AP1101, AP1201H, AP1201L, and AP1201HL models) ... The Application Visibility feature ... is supported on all Stellar APs models, except AP1101, AP1201H, AP1201L, AP1201HL, and AP15XX. (AP132x and AP136x models require minimum Signature Kit version of 3.6.11. AP1301, AP1301H, and AP1311 require minimum Signature Kit version 3.8.3.)
  summary: |
    型号排除清单：WCF 需 AWOS 4.0.2+ 且排除 AP1101/AP1201H/AP1201L/AP1201HL；应用可见性同样排除这四款加 AP15XX 系列，且 AP132x/AP136x 需签名包 >=3.6.11、AP1301/AP1301H/AP1311 需 >=3.8.3。另有 OS6860（非 E/N）不支持应用可见性，除非虚拟机箱内至少含一台 OS6860E（矩阵注 19）。无线功能规划先过这张排除表。
  tags: [WCF, 应用可见性, AP 型号, 签名包版本, 排除清单]
