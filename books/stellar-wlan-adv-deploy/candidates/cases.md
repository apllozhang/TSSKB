# cases · Lab 案例（stellar-wlan-adv-deploy / DT00XTE361）

```yaml
- id: c01
  title: Lab：远程实验室连接与环境发现
  type: case
  source_chapter: "p35-p42"
  source_quote: |
    "This topology contains: clients, Stellar Access points, OmniSwitches, servers and an OmniVista Cirrus. It simulates a three-tier end user topology (Access, Aggregation and Core)."
  summary: |
    通过 https://rdp.al-mydemo.com 远程桌面接入 POD（推荐 Chrome/Edge），认识三层拓扑：接入层 OS-6360/OS-2360 与有线客户端 Client5（vSphere VM）、无线客户端树莓派（VNC）；汇聚层 OS-6870（DHCP relay、动态路由，脚本预置不得删改）；核心 OS-6900 与 AAA/DHCP、NAT/pfSense 服务器完全透明不管理。要点：树莓派键盘语言跟随远程桌面；"Hunting Group Busy" 表示已有别的 TeraTerm 会话占用控制台。
  tags: [Lab, 远程实验室, 拓扑]

- id: c02
  title: Lab：实验室复位与基础 WLAN 配置
  type: case
  source_chapter: "p43-p73"
  source_quote: |
    "You can then configure a basic WLAN environment composed of two SSIDs Guest and Employee. (p45)"
  summary: |
    完整基础部署链路：运行 reset_PODX 脚本复位 → 建 My Site 站点 + Building A/Ground Floor 并对齐楼层平面图（画周长约 1200-1300m² 的楼层边界）→ 用 show chassis 取序列号把 OS-6870A/OS-6360A 与 AP1321/AP1301 逐台加入设备目录（cloud-agent admin-state restart 加速激活，状态走 Waiting for first Contact → Connected to OV → Provisioning → OV Managed，约 2 分钟；AP 用 ssudo firstboot -y + reboot 强制 call home）→ 手工配 VLAN 10/20/30 与 IP 接口 → 建 EmployeesX（WPA2-Enterprise/802.1X/本地库账号，VLAN 20）与 GuestsX（OV-UPAM Captive Portal，VLAN 30）SSID 并映射到 My-AP-Group → 树莓派验证（Employee 拿 192.168.20.70-79，Guest 拿 192.168.30.70-79，ping DHCP 服务器与网关）。
  tags: [Lab, 上线, SSID, VLAN, 基础配置]

- id: c03
  title: Lab：Stellar AP 有线口 MAC 认证示例
  type: case
  source_chapter: "p89-p98"
  source_quote: |
    "In this example: MAC Authentication; Stellar AP port: Ethernet1. AP « Home-AP » (p90)"
  summary: |
    按 f05 四步流程在 AP 的 Eth1 口做 MAC 认证：ARP_DEFAULT（受限+限速）作默认角色、ARP_PASS（全通）作认证通过角色，AAA Server Profile 指向 UPAMRadiusServer（MAC 用途），Access Policy 匹配 Authentication Type=MAC 且源为 Local Database，最后在 Company Property 录入客户端 MAC 11:22:33:44:55:66。监控在 Device Catalog > Wired Ports 看端口与 UNP 客户端，Analytics > Clients 看在线/历史有线会话（时间窗最近 1 小时到 1 个月）。
  tags: [Lab, 有线客户端, MAC认证]

- id: c04
  title: Lab：Mesh/Bridge 配置
  type: case
  source_chapter: "p117-p121"
  source_quote: |
    "Configure the parameters according to the configuration for either Mesh or Bridge. Mesh config only (119). Displays the mesh topology. (p120)"
  summary: |
    在 Device Catalog 选中 AP → Actions > Edit Device > Mesh/Bridge Configuration，配置模式/频段/SSID/密钥管理与密码（Mesh 多 Is Root）。监控页 Mesh Topology 列出 MAC、角色（Root/Repeater）、Level、BSSID、频段、SSID 与 Parent Address，用于确认链路父节点。Auto Mesh（p116）可实现免配置快速组网：接 LAN 且设为 Root 的 AP 广播隐藏 SSID "Stellar-MESH"（5GHz），未接 LAN 的 AP 自动以非 Root 身份入网。
  tags: [Lab, Mesh, Bridge, Auto-Mesh]

- id: c05
  title: Lab：QoE、网络与客户端分析实操
  type: case
  source_chapter: "p156-p163"
  source_quote: |
    "OmniVista Cirrus provides the following advanced WLAN analytics to monitor and enhance the Wi-Fi user experience: Quality of Experience (QoE), Network and Client Analytics."
  summary: |
    前提：树莓派先连上 Employee SSID 产生数据。① QoE：Network > Analytics > QoE，确认站点选择，逐项查看六指标，用 Configure Thresholds 调阈值，More details 看失败分类器（时间窗可扩到 Last 7 days）；交换机仅有 Device Uptime 一项 QoE。② Network Analytics：看 2.4/5/6GHz 信道分布与利用率（点信道跳 RF Details），按 AP 看 CPU/内存/闪存与健康阈值。③ Client Analytics：按小时点选柱图联动各分布组件，看吞吐、连接时长、每用户设备数。
  tags: [Lab, QoE, 网络分析, 客户端分析]

- id: c06
  title: Lab：监控（客户端、访问记录与报表）
  type: case
  source_chapter: "p183-p187"
  source_quote: |
    "Go to Network > Reports. Click on the + Create Report button. Select Analytics Data Report... Metric: Wireless Client Sessions... Data Range: Last 7 days; Report Type: Instant Report."
  summary: |
    ① Clients 仪表盘：Live Wireless Clients 找到树莓派 MAC，Additional Information 看 RSSI/噪声底、吞吐消费、PHY 速率、告警与网络事件（设备名与 IPv4 需几分钟才浮现）。② 访问记录：Authentication Records 看 UPAM 认证条目（在线/历史切换）；Captive Portal Records 看访客登录记录，Auth result 与 Reject Reason 区分成败。③ 报表：创建 Analytics Data Report（指标 Wireless Client Sessions、PDF、范围 Site、Last 7 days、Instant），结果邮件自动发到 podXX@ale-training.com，经 https://mail.ale-training.com 收取。
  tags: [Lab, 监控, 访问记录, 报表]

- id: c07
  title: Lab：设备目录与拓扑
  type: case
  source_chapter: "p242-p249"
  source_quote: |
    "The topology application can be used to display your network devices, ethernet and fiber links, and unmanaged devices connected on your network."
  summary: |
    Device Catalog 对 AP 的 Actions 全集：Edit Device（信息/IP 模式/位置/Group 与 RF Profile/站点/期望版本/升级计划/健康阈值/射频私有配置/Mesh-Bridge/RTLS/IoT 射频）、SSH（需先在 Provisioning 配置启用）、Web UI、Configuration Management > Save to running 等。拓扑应用：识别云、交换机、AP 与未托管设备图标；按颜色判设备/链路状态（见 p21）；悬停看链路类型与设备楼层；搜索、过滤环路/未托管设备、横/竖/环形布局；点设备开 Device Detail 看 7 天 trap 与 Analytics 入口。
  tags: [Lab, 设备目录, 拓扑]

- id: c08
  title: Lab：Stellar AP 运维（升级计划、事件、支持信息、告警、远程命令）
  type: case
  source_chapter: "p250-p257"
  source_quote: |
    "The Device Troubleshooting application is used to send commands to network devices to troubleshoot and resolve device problems. A list of commands is provided."
  summary: |
    ① 升级计划：四步向导走读（本实验只演示不执行），升级时长默认 6 小时窗口。② Network Events：分 AP Traps / Switch Traps / QoE Analytics 三类事件浏览。③ Collect Support Info：AP 直接收集 tar.gz；交换机可选 swlog/cfg/Tech Support（L2/L3/Engineering Complete 分层），状态由 Uploading 变 Collected 后下载。④ Alerts：顶部汇总+底部 Entry List，新告警实时更新并有红点提示。⑤ Device Troubleshooting：给 AP 分配 setDateTime 等命令（可改参数），几分钟后查结果。
  tags: [Lab, 运维, 升级, 事件, 支持信息]

- id: c09
  title: Lab：全流程部署综合演练
  type: case
  source_chapter: "p286-p299"
  source_quote: |
    "Three SSIDs, using different authentication methods are required in our environment... The design of each part of the lab has been defined to permit the mix of different features."
  summary: |
    端到端交付考核（详见 f08）：从复位、双站点组织建模、设备上线（含不能云管的 OS-2360 手工配置），到三个差异化 SSID（企业 802.1X 调度+按角色封 HTTP、访客门户限速封 SSH/Telnet+按天调度+账号限时限量、打印机 2.4GHz 低功率固定信道 DPSK）、RF Profile 负载均衡与 -50dBm 关联门限、WIPS 流氓分类（同 SSID 名+指定 MAC OUI）与认证失败黑名单、Golden Config 与 VLAN 1000 变量模板、周报与阈值调整，最后把拓扑改成 Mesh（AP1321 为 Root、专用 SSID、WPA2-Personal）。可作为真实项目交付 checklist 模板。
  tags: [Lab, 综合演练, 交付, checklist]

- id: c10
  title: Lab：组织清理
  type: case
  source_chapter: "p313-p319"
  source_quote: |
    "In this lab, we will undo the configuration performed during this training. Then, for your use case, you can reconfigure your network, starting with the first labs."
  summary: |
    按 f10 的 29 步逆向拆除全部自定义配置（升级计划→备份→排障命令→WIPS 重置→AP 组与 Provisioning 解绑删除→SSID→策略/角色/门户→账号/公司资产→Golden Config→报表/支持信息→分析阈值重置→站点→设备目录确认为空→CLI 模板/值映射）。清理后设备目录回到空状态，可重新开始部署。依赖关系注意：AP 组只有解绑自定义 Provisioning 配置后才能删；删 Provisioning 配置报错时先把其中 RF Profile 改回 Default。
  tags: [Lab, 清理, 依赖顺序]

- id: c11
  title: 排障用例：客户端看不到 SSID
  type: case
  source_chapter: "p276"
  source_quote: |
    "1) Is the SSID broadcasted by the AP? 2) Which radio does the client support? Compatible with the SSID broadcasted? 3) Country Code of the AP? Supported by the client?"
  summary: |
    三问排查：SSID 是否真的在该射频广播（iwconfig 确认）；客户端射频是否与 SSID 频段兼容；AP 国家码是否被客户端支持——国家码错误时在 RF Profile 里手工指定一个客户端兼容的信道即可规避（无需改国家码）。
  tags: [排障用例, SSID, 国家码]

- id: c12
  title: 排障用例：客户端拿不到 IP / 频繁掉线 / 802.1X 失败
  type: case
  source_chapter: "p277-p284"
  source_quote: |
    "1) Capture DHCP messages on the client (wireshark) and the AP (tcpdump)... 2) Client assigned to the correct VLAN? Does the Final_role filter DHCP traffic? (p277-278)"
  summary: |
    三个经典用例：① 拿不到 IP——双侧抓 DHCP 报文看丢包，再用 sta_list 核对 VLAN 与 Final_role 是否过滤了 DHCP；② 频繁掉线——查 AP 发射功率是否被设到最小（iwlist txpower，案例中 Tx-Power=3dBm 导致 RSSI 16/SNR 30 临近掉线）、RF Profile 的 signalStrengthThreshold 是否设得过高（案例 70）把弱信号客户端主动踢掉、空口抓包看去关联/去认证帧；③ 802.1X 失败——三段对照：客户端（账号/加密/证书）↔ AP（AAA_server.conf 的 IP/端口/共享密钥、wlanservice.conf 绑定的 aaaProfile）↔ RADIUS 服务器（用户库、共享密钥、NAS IP、防火墙放行 1812/1813）。
  tags: [排障用例, DHCP, 掉线, 802.1X]

- id: c13
  title: 排障用例：系统高 CPU 与僵尸进程
  type: case
  source_chapter: "p214-p217"
  source_quote: |
    "Most common causes for high CPU utilization: Abnormal process... Process infinite loop → Probably software issue... Stellar AP under DoS attack. ... Too many Zombie processes will consume large portion of memory."
  summary: |
    用 top 看全局 CPU/内存与进程清单：单进程 %CPU 异常（案例 /usr/sbin/drm 占 81%）通常是死循环（软件问题）、大量日志/追踪或 DoS 攻击，进程清单应随工单交给技术支持。ps 看进程状态：R/S 正常，X（Dead）与 Z（Zombie）异常，僵尸进程过多会大量吃内存。另用 date/uptime 核对系统时间与 NTP 同步、判断是否有意外重启。
  tags: [排障用例, CPU, 僵尸进程, top]
```
