# 候选条目 · 陷阱/警告（反例）
来源：OV 2500 RAP and VPN VA Installation Guide (4.9R2 RevA, 84 页)
页码约定：pN 为 fulltext.md 中 <<<PAGE N>>> 的 PDF 页码。

- id: ce01
  title: ESXi 5.5 不被支持
  type: counter-example
  source_chapter: "p5"
  source_quote: |
    "ESXi versions 6.5, 6.7, 7.0.2, 8.0 are supported (ESXi 5.5 is not supported)."
  summary: |
    陷阱：在 ESXi 5.5 老环境上部署 RAP VPN VA。前置条件明确 6.5/6.7/7.0.2/8.0 可用，5.5 被排除；Hyper-V 则要求 2016/2019/2022。规划迁移或新建 hypervisor 时先核对版本。
  tags: [版本兼容, ESXi]

- id: ce02
  title: 导入虚拟机时未删除 *.mf 文件
  type: counter-example
  source_chapter: "p14, p24"
  source_quote: |
    "The Zip file also contains an *.mf File. Delete the *.mf File from the folder before importing the files in Step 5. ... Remember, do not include the *.mf File; only the *ovf file and the two *vmkd Files."
  summary: |
    陷阱：把 OVF 包里自带的 *.mf 清单文件一并选入导入。VMware 与 Hyper-V 两条路径都被强调：导入前只保留 OVF 文件 + 两块 VMDK（ovnmse-vpn-4.9.2.2-disk001/002.vmdk），*.mf 必须先从目录删除，否则导入失败或校验报错。
  tags: [OVF导入, mf文件]

- id: ce03
  title: RAP VPN VA 不支持冗余——不能按 HA 设计
  type: counter-example
  source_chapter: "p14"
  source_quote: |
    "Known Limitations: RAP VPN VA does not support redundancy."
  summary: |
    陷阱：给 VPN VA 做双机热备/高可用设计。已知限制明确 RAP VPN VA 不支持冗余；规模增长（超过 250 台 RAP）官方建议是部署第二台 VPN VA 分担（p13），而非主备冗余。SLA 承诺和割接窗口要按单点设备评估，升级时的停机也需纳入（见升级流程约 5 分钟断连）。
  tags: [无冗余, 高可用, 容量拆分]

- id: ce04
  title: VPN 设置文件三类失效场景：改名、改配置不重传、导出后又加 AP
  type: counter-example
  source_chapter: "p61-63, p69"
  source_quote: |
    "If you add an AP to the Device Catalog in your OmniVista Freemium account after exporting the VPN Settings file, you will have to redo the export, SFTP, and reconfigure the VPN VA. ... Important Note: Do not change the name of the VPN Settings file. ... Any time you modify VPN settings you must generate a New VPN Settings File and FTP the file to the VPN Server."
  summary: |
    三个常见踩坑：①手工改名 VPN 设置文件（如 LAB4.conf）导致 VA 识别失败；②在 Freemium/OV 侧修改了 VPN 设置却没有重新导出并 SFTP 上传，VA 上仍是旧配置；③导出文件之后又往 Device Catalog 加了 AP，新 AP 的公钥/AllowedIPs 不在旧文件里，必须重做"导出→SFTP→VA 重配"全流程。管理隧道与数据隧道（p69）的设置文件同规则。
  tags: [VPN设置文件, 改名, 配置漂移]

- id: ce05
  title: 给数据隧道桥接网卡误配 IP 地址
  type: counter-example
  source_chapter: "p55, p69"
  source_quote: |
    "To set up a Data Tunnel, you use the third NIC on the VA. You must not configure an IP address for this NIC because it will be a Layer 2 Tunnel. You also need to enable "Promiscuous Mode" for this NIC in your Hypervisor. ... Be sure to select the right ethernet interface for bridging traffic (e.g., eth2 without IP Address)."
  summary: |
    陷阱：按习惯给第三块网卡（Hyper-V 的 Eth2 / KVM 第三网卡 / VPN Endpoints 的桥接接口）配 IP。数据隧道是二层（L2）桥接，该网卡必须无 IP，且要在 hypervisor 开混杂模式；VPN Endpoints 配数据隧道时也要选对这块无 IP 网卡（如 eth2）。配了 IP 或选错接口会导致桥接流量不通。
  tags: [L2隧道, 网卡误配IP, 桥接]

- id: ce06
  title: vSwitch 混杂模式默认 Reject 且 Override 未全设 Accept
  type: counter-example
  source_chapter: "p20, p81"
  source_quote: |
    "Make sure Promiscuous Mode, MAC address changes, and Forged transmits are set to "Accept". ... Client is not able to ping any device or gateway within same subnet. Make sure that Promiscuous Mode is enabled and set to "Accept" on the vswitch (by default this is set to reject). ... Promiscuous Mode is enabled but it is not working. Check if the Override checkbox is disabled. If enabled ensure the setting is set to "Accept"."
  summary: |
    陷阱一：ESXi vSwitch/端口组的混杂模式出厂默认 Reject，不开启则双隧道都 up、客户端仍无法访问同网段任何设备/网关。陷阱二：只在端口组开了混杂模式但 Override 勾选未生效，或三项（Promiscuous Mode、MAC address changes、Forged transmits）没有全部设为 Accept；端口组"Inherit from vSwitch"时若 vSwitch0 是 Reject 同样失效。排障章节把它列为"客户端不通 LAN"的首要检查项。
  tags: [混杂模式, vSwitch, Override]

- id: ce07
  title: Local Breakout 静态路由三类重叠/重复错误
  type: counter-example
  source_chapter: "p73-74, p84"
  source_quote: |
    "Do not specify an explicit Route with Destination = 192.168.41.0, as that will confuse the AP and lead to poor performance. ... If a route to IP subnet X already exists in an SSID and that SSID is applied to an AP, another route to the same IP subnet X must not be specified in the same or a different SSID that is applied to the same AP. ... If the AP attempts to access to 192.168.10.100 ... it will fail because the packet will be forward to the tunnel and sent to Corporate HQ."
  summary: |
    三类错误：①为进入隧道的 VLAN 网段手工配路由（如隧道承载 VLAN 41、对应 192.168.41.0/24）——AP 会自动生成该路由，显式再配会让 AP 混乱、性能下降；②跨 SSID 重复——静态路由在 AP 上跨所有 SSID 累积，同一目的子网在 同一 AP 的任何 SSID 上都只能出现一次；③Local Breakout 路由与 AP 本地网络网段重叠（如路由 192.168.10.0/24 撞上 AP 本地同网段）——AP 自己访问本地 192.168.10.100 的包会被推进隧道发往总部，导致 AP 与本地网失联。配置 Local Breakout 时务必避开与 AP 本地网重叠。
  tags: [Local-Breakout, 路由重叠, 跨SSID重复]

- id: ce08
  title: Hyper-V NIC Teaming 选了不兼容的负载均衡组合
  type: counter-example
  source_chapter: "p36-37"
  source_quote: |
    "Switch Independent / Switch Independent / Hyper-V Port / None / No; Switch Independent / Switch Independent / Hyper-V Port / NIC1/NIC2 / No; Switch Independent / Switch Independent / Dynamic / None / No; Switch Independent / Switch Independent / Dynamic / NIC1/NIC2 / No"
  summary: |
    陷阱：二层交换模式为 Switch Independent（交换机独立）时选 Hyper-V Port 或 Dynamic 负载均衡——实测均不通过（No），不管是否配 Stand-By 适配器。该模式下只有 Address Hash 可用。Linkagg static 与 LACP 模式下三种负载均衡均可。做网卡绑定前先按兼容矩阵选组合。
  tags: [NIC-Teaming, 负载均衡, 兼容矩阵]

- id: ce09
  title: KVM 部署跳过 qcow2 Discard unmap 设置
  type: counter-example
  source_chapter: "p50"
  source_quote: |
    "Before beginning the installation (Step 18), reduce qcow2 disk size. Select VirtIO Disk 1 on the left side of the screen. Select Advanced options, then select Performance options and set the Discard Mode to unmap. Repeat for the VirtIO Disk 2."
  summary: |
    陷阱：KVM/Ubuntu 部署时直接点 Begin Installation，忘记对两块 VirtIO 磁盘把性能选项中的 Discard Mode 设为 unmap。该步骤用于缩减 qcow2 磁盘占用，一旦开始安装就无法回头补设，只能重部署。同页还要求 3 块网卡必须用 Macvtap device 网络源，漏配网卡同样要返工。
  tags: [KVM, qcow2, unmap, 返工]

- id: ce10
  title: Local Breakout 的 DNS 三类故障（AP 双 DNS、绕隧道、运营商不匹配）
  type: counter-example
  source_chapter: "p83-84"
  source_quote: |
    "At this moment, the AP has two DNS Server IP addresses - A and B. When the AP tries to access OVC'FQDN, it will randomly use DNS Server A or B. If DNS Server B cannot resolve OVC'FQDN, the AP will be down in OVC. ... If there is a DNS Server with IP 192.168.10.177 and it cannot be found, the client will fail to access the website. ... when the client attempts to access youtube.com or any other URL, it will be slow."
  summary: |
    开启 Local Breakout 后的三类 DNS 故障：①AP 双 DNS——AP 本地拿到 DNS A、又经数据隧道从总部拿到 DNS B，随机选用，若 B 解析不了 OVC 的 FQDN，AP 会从 OVC 掉线；解决：配正确的总部 DNS。②客户端 DNS 绕隧道——Local Breakout 含 192.168.10.0/24 路由而客户端 DNS 是 192.168.10.177，访问外网的 DNS 请求也被送进总部隧道，变慢。③本地无该 DNS——路由不含该网段时 DNS 请求走本地，本地找不到 192.168.10.177 则直接无法上网；或拿到的是异地运营商 DNS（如 219.141.136.10 属运营商 B 而本地是运营商 A），解析和访问都慢。解决：为客户端配置正确的总部 DNS 服务器。
  tags: [Local-Breakout, DNS故障, 掉线]

- id: ce11
  title: AWOS 版本口径不一致：5.0.1 / 5.0.2 / 4.0.1 三处说法
  type: counter-example
  source_chapter: "p6-7, p71"
  source_quote: |
    "The Remote AP feature is supported on Stellar APs running AWOS 5.0.2. and higher. ... APs must be running a minimum software version of AWOS 5.0.1. ... Allow Local Breakout: Disabled (will be supported with AWOS 4.0.1)"
  summary: |
    陷阱：文档内三处版本口径打架——RAP 功能要求 AWOS 5.0.2+（p6 与 p5 前置条件），而 Freemium 注册邮件的软件下载说明写最低 AWOS 5.0.1（p7），SSID 界面又写 Local Breakout "将在 AWOS 4.0.1 支持"（p71，与 5.0.2 要求明显矛盾，疑为文档笔误）。交付时应以最严格的 5.0.2+ 为准，遇到 Local Breakout 支持性问题时先核对实际 AWOS 版本与官方最新 release note，不要照抄 4.0.1/5.0.1 字样。
  tags: [版本口径, AWOS, 文档矛盾]

- id: ce12
  title: CSV 批量导入时 RAP 字段未设 TRUE 导致 VPN 设置缺失
  type: counter-example
  source_chapter: "p12"
  source_quote: |
    "Modify the Template with AP Serial Numbers and any additional information you want to add. If you want to add VPN Setting information (VpnSettingName), the RAP field must be "TRUE"."
  summary: |
    陷阱：批量导入模板里 RAP 列填了 FALSE/留空，却期望 VpnSettingName 生效。规则是：要携带 VPN Setting 信息（VpnSettingName 列），RAP 字段必须为 TRUE。导入结果看似成功但 AP 不带隧道配置，只能逐台补配或重导。
  tags: [CSV导入, RAP字段, 批量配置]
