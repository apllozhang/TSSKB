# glossary · OV 2500 NMS 4.9R2 Release Notes

> 仅收录本册 Release Notes 中反复出现、影响理解的关键概念。文档自身未展开的缩写按书中用法描述，不外推。
> 页码为 fulltext.md 中 <<<PAGE N>>> 标记的 PDF 页号。

- id: g01
  term: OmniVista 2500 NMS（OV 2500 / OVE）
  type: glossary
  source_chapter: "p5"
  source_quote: |
    This document details known problems and limitations in OmniVista 2500 NMS 4.9R2 (OV 2500 NMS 4.9R2), and workarounds are included.
  definition: |
    ALE（Alcatel-Lucent Enterprise）的企业级网络管理系统，本册主角，文档中常缩写为 OV 2500 或 OVE。以虚拟设备（VA）交付，内含 Discovery、Topology、Locator、PolicyView、Resource Manager、UPAM、WLAN、VM Manager 等应用，通过 SNMP/REST/MQTT 等协议管理 AOS 交换机与 Stellar AP。相关云版本称 OV Cirrus / OVC。
  tags: [网管系统, NMS, 主角]

- id: g02
  term: VA（Virtual Appliance）与 VA 菜单
  type: glossary
  source_chapter: "p5, p7"
  source_quote: |
    OmniVista 2500 NMS 4.9R2 is installed as a Virtual Appliance ... The user can go to the "Change Password" option in the VA Menu for the OmniVista 2500 instance to change the password.
  definition: |
    虚拟设备：OV 2500 的交付形态，部署在 ESXi/Hyper-V/KVM 上。VA 菜单是其控制台管理入口，本册多处运维操作都走它：改 CLI 管理员密码（Change Password）、扩展 HDD2 磁盘、Run Watchdog Command、HA 菜单（3 Configure Cluster → 14 Cluster Error Check）等。RAP VPN VA 是其远端接入VPN 服务器的姊妹设备。
  tags: [虚拟设备, 控制台, 运维入口]

- id: g03
  term: AOS
  type: glossary
  source_chapter: "p6"
  source_quote: |
    AOS 5.2R7 – OmniVista 2500 NMS now supports AOS 5.2R7 for the OS2260 and OS2360 Series Switches. AOS 8.9R4 MR – ... on all previously supported AOS Switches.
  definition: |
    OmniSwitch 交换机的网络操作系统。本册涉及 5.x（OS2260/2360）、6.x（OS6350/6450）、8.x（OS6360 到 OS9912）三条大版本线，能力差异大（如 IPv6 策略条件需 6.7.2R7+ 或 8.6R2+；Blast-RADIUS 的 aaa radius message-authenticator 命令需 8.10R2+）。版本号形如 8.9R4、8.10R3。
  tags: [交换机系统, 版本线, AOS]

- id: g04
  term: AWOS
  type: glossary
  source_chapter: "p6"
  source_quote: |
    AWOS 5.0.2 – OmniVista 2500 NMS now supports AWOS 5.0.2 on all previously supported Stellar APs.
  definition: |
    OmniAccess Stellar 无线 AP 的操作系统。4.9R2 推荐全网运行 AWOS 5.0.2（先升 OV 再升 AP）。本册多处功能有 AWOS 版本门槛：Enhanced Open Transition Mode 需 4.0.8+，WCF 需 4.0.2+，Message-Authenticator 响应校验需 5.0.2+，MAC 认证授权残留修复于 5.0.1。
  tags: [AP 系统, AWOS, 版本依赖]

- id: g05
  term: Stellar AP（OmniAccess Stellar）
  type: glossary
  source_chapter: "p6, p14"
  source_quote: |
    There were no new OmniAccess Stellar AP models introduced with this release ... The following AP models are supported. The recommended AWOS version is 5.0.2.
  definition: |
    ALE 的 Wi-Fi 6/6E 接入点系列（OAW-AP1201 至 AP1521 等约 20 余型号，部分型号限中国/巴西销售）。经 OV 的 AP Registration/WLAN 应用管理，通过 MQTT（端口 1883）注册。功能支持与型号强相关：AP1101/AP1201 系列与 AP15XX 多项功能被排除，AP1201BG 是 BLE 网关。升级按 AP Group 进行；Mesh 网络须逐跳手工升级。
  tags: [无线 AP, Stellar, 型号差异]

- id: g06
  term: UPAM
  type: glossary
  source_chapter: "p8"
  source_quote: |
    UPAM as RADIUS Server for AP/OmniSwitch – UPAM RADIUS server accepts RADIUS requests from clients within a specified IP range.
  definition: |
    OV 内置的接入认证组件（本册未展开缩写），承担 RADIUS 服务器/代理、Captive Portal、访客账户、BYOD 注册、LDAP/AD 对接、短信网关等职能，对应 OV 的辅助 IP 地址（UPAM address）与 1812-1815、3799 等端口。已知问题大户：HSTS 重定向、LDAPS 依赖、门户定制限制等（见 ce25-33）。
  tags: [认证, RADIUS, 访客门户, BYOD]

- id: g07
  term: HA（High Availability，L2/L3 集群）
  type: glossary
  source_chapter: "p15"
  source_quote: |
    "L2 High-Availability Upgrade Workflow" to upgrade an L2 HA installation. "L3 High-Availability Upgrade Workflow" to upgrade an L3 HA installation ... An L3 HA cluster is supported only with a fresh HA installation.
  definition: |
    OV 双节点高可用集群，分 L2（二层，访问虚拟 IP）与 L3（三层，访问当前 Active 节点 IP）两种。核心规则：升级先 Standby 后 Active；节点间走 TCP 8000/7801/2224 + UDP 5405，底层用 DRBD 同步；HA 最多管 4000 台设备且需 Medium 以上规格；L3 只能全新安装；建集群后不能改 IP/主机名。已知坑见 ce40、ce51、ce62、ce65、ce66、ce69。
  tags: [高可用, 集群, L2, L3, DRBD]

- id: g08
  term: NaaS 与降级模式（Degraded Mode）
  type: glossary
  source_chapter: "p24"
  source_quote: |
    OmniVista does not indicate the reason for a failure when a configuration or software upgrade through Managed Devices fails because the NaaS license has expired on the device.
  definition: |
    Network as a Service：设备按订阅模式运行（Opex 模式）。设备上的 NaaS 许可过期后进入降级模式，经 Managed Devices 下发配置或升级会失败，且 OV 不显示失败原因（ce05）——排障时"无理由失败"要先怀疑 NaaS 许可。
  tags: [NaaS, 订阅, 降级模式, 排障]

- id: g09
  term: PALM 与 Fleet Supervision
  type: glossary
  source_chapter: "p6"
  source_quote: |
    The ProActive LifeCycle Management (PALM) application is no longer available as a service and support option. OmniVista now provides Fleet Supervision as a PALM replacement for monitoring Service and Support entitlement, hardware status, and software versions.
  definition: |
    PALM（ProActive LifeCycle Management）是旧的生命周期管理服务，4.9R2 起下线；接替者 Fleet Supervision（https://myfleet.ovcirrus.com/）监控服务与支持权益、硬件状态、软件版本等。OV 需访问的 Call Home 后端域名为 us.fluentnetworking.com。
  tags: [生命周期管理, 订阅服务, 替代关系]

- id: g10
  term: Blast-RADIUS 与 Message-Authenticator
  type: glossary
  source_chapter: "p8"
  source_quote: |
    A new Require Message Authenticator flag is now available to specify whether to check RADIUS packets for the Message-Authenticator attribute ... resolves CVE-2024-3596 (#Blast-RADIUS).
  definition: |
    Blast-RADIUS（CVE-2024-3596）是针对 RADIUS 协议的中间人攻击；防御手段是强制校验报文中的 Message-Authenticator 属性。4.9R2 在 AAA 服务器配置里新增 Require Message Authenticator 开关；OmniSwitch 侧需执行 aaa radius message-authenticator 全局命令（AOS 8.10R2+），AP 侧 AWOS>=5.0.2 才校验响应报文。
  tags: [安全漏洞, RADIUS, CVE-2024-3596, 认证属性]

- id: g11
  term: Wi-Fi Enhanced Open（OWE）过渡模式
  type: glossary
  source_chapter: "p7"
  source_quote: |
    one legacy Open SSID on 2.4GHz/5.0GHz band and one Enhanced Open SSID on 2.4GHz/5.0GHz/6.0GHz band. This allows both Enhanced Open and Non-Enhanced Open clients to connect to the same open SSID.
  definition: |
    Enhanced Open 即 OWE（机会性无线加密），给开放网络提供个体化加密。过渡模式让 AP 同时广播传统开放 BSSID 与 OWE BSSID，新旧客户端共用同一 SSID 名平滑迁移。仅限 Guest/BYOD 用途的 SSID，且要求 AP 跑 AWOS 4.0.8+（旧版本重启后 SSID 会退回纯开放）。
  tags: [无线安全, OWE, 开放网络, 平滑迁移]

- id: g12
  term: WCF（Web Content Filtering）
  type: glossary
  source_chapter: "p16"
  source_quote: |
    Web Content Filtering – api.bcti.brightcloud.com ... Web Content Filtering is supported on Stellar APs running AWOS 4.0.2 and higher (except AP1101, AP1201H, AP1201L, and AP1201HL models).
  definition: |
    Web 内容过滤：在 Stellar AP 上按域名分类放行/拦截网站，依赖外部 BrightCloud 云端分类库（防火墙须放行 api.bcti.brightcloud.com）。基于 AP 代答 DNS 实现，因此手机 App 流量与代理上网两种场景全部失效（ce38、ce39），是它的能力边界。
  tags: [内容过滤, 无线, BrightCloud]

- id: g13
  term: mDNS Gateway / Responder / Edge Device
  type: glossary
  source_chapter: "p11-12"
  source_quote: |
    mDNS Gateway is only supported on OS6450, OS6860E, OS6865, OS6900, and OS6860N ... The following devices can be configured as Responder Devices: OS6570, OS6860/E, OS6865, OS6900, OS9900. The following devices can be configured as Edge Devices: OS6465, OS6560, OS6860/E, OS6865, OS6900, OS9900, and Stellar APs (except for OAW-AP1101).
  definition: |
    mDNS 服务跨 VLAN 共享的三种角色：Gateway/Responder 在交换机上应答与代理 mDNS 查询，Edge Device（交换机或 AP）标记哪些端口/SSID 的服务可被共享。配置顺序敏感（先 Responder/Edge 后放用户入网，ce08）；AP 上仅 Eth0 或 Eth0+Eth1 聚合口可用（ce10）。典型场景：Chromecast、AirPlay 跨 VLAN 发现。
  tags: [mDNS, 服务发现, 跨 VLAN, 角色模型]

- id: g14
  term: U-Boot 与 CPLD
  type: glossary
  source_chapter: "p26-27"
  source_quote: |
    Cannot upgrade U-Boot with File Name "u-boot.5.2R03.3.tar.gz" ... there are two U-Boot files involved: one regular and one Denverton.
  definition: |
    交换机底层固件：U-Boot 是引导加载程序（升级对文件名、CPU 类型敏感，见 ce14、ce15；8.9R4 起 OS6570M 只认签名镜像，见 ce63）；CPLD 是管理板级逻辑的固件，OV 不支持对 OS6870 做 CPLD 升级，须按 AOS Release Notes 在 ONIE 交换机上操作。固件升级排障时先分清这三层：AOS 系统镜像、U-Boot、CPLD。
  tags: [固件, 引导, 底层升级, ONIE]

- id: g15
  term: UNP（Unified Access 中的接入档案）
  type: glossary
  source_chapter: "p10, p32"
  source_quote: |
    UNP X X X X X X (13) ... VLAN notification does not come up when the default UNP of a Link Agg Port is deleted ... UNP bridge port, service access port, and UNP Service Access Point
  definition: |
    Unified Access 模块中面向用户/终端接入的配置档案（本册未展开缩写），与端口绑定形成 UNP bridge port、UNP Service Access Point 等概念；LAG 口删除默认 UNP 会引发 MAC 学习表延迟回填（ce37）。UNP 功能仅支持 OAW Controller 与 OAW IAP（矩阵注 13）。
  tags: [统一接入, 接入档案, UNP]
