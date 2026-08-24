# frameworks · 框架/流程（stellar-wlan-adv-deploy / DT00XTE361）

```yaml
- id: f01
  title: QoE 分析六指标体系
  type: framework
  source_chapter: "p125-p129, p158"
  source_quote: |
    "OmniVista Cirrus provides six metrics to be monitored: Successful Connects, Time To Connect, Roaming, Coverage, Available Capacity, Device Uptime. (p158)"
  summary: |
    体验质量（QoE，Quality of Experience）分析用六个指标刻画终端用户真实体验：
    1) Successful Connects 成功连接数（计数器，无阈值）；
    2) Time To Connect 连接耗时（关联/授权/DHCP/Portal 四阶段总时长）；
    3) Roaming 漫游成功率；
    4) Coverage 覆盖（信号高于阈值的时间占比）；
    5) Available Capacity 可用容量（RF 信道可用时间占比）；
    6) Device Uptime 设备平均在线率（仅 AP/交换机适用，交换机只有这一项 QoE 指标）。
    每个指标都带失败分类器（如 DHCP、Association、Weak Signal、Asymmetry Downlink/Uplink），可下钻定位失败原因。
  tags: [QoE, OmniVista-Cirrus, 监控, WLAN分析]

- id: f02
  title: QoE 仪表盘分析流程（过滤→阈值→摘要→详情）
  type: framework
  source_chapter: "p125-p126"
  source_quote: |
    "QOE DASHBOARD — Filters / Thresholds / Summary / Details / Shortcuts (p125)"
  summary: |
    使用 QoE 仪表盘的标准路径：先用 Filters 选站点/设备类型（AP 或交换机）和时间范围；再用 Thresholds 按站点调整各指标阈值；在 Summary 区看六指标汇总与失败阶段占比；对异常指标点 More details 下钻到按连接模式/设备类型/OS/SSID 分布的失败会话明细；最后经 Shortcuts 跳转相关页面。时间范围建议先扩到 Last 7 days，最近一小时没有失败样本时看不到失败分类器（p159）。
  tags: [QoE, 仪表盘, 工作流, OmniVista-Cirrus]

- id: f03
  title: 网络分析工作流（信道→设备健康→端口级下钻）
  type: framework
  source_chapter: "p138-p145"
  source_quote: |
    "NETWORK ANALYTICS — Channel Distribution (2.4/5/6GHz), Channel Utilization, Network Devices Health (CPU, Memory, Flash), Network Devices Uptime. (p138)"
  summary: |
    网络分析四步：① 看全局信道分布（Channel Distribution）与信道利用率（Channel Utilization），点击具体信道可跳转使用该信道的 AP 的 RF Details；② 用设备过滤器切到 AP，看 CPU/内存/闪存健康（Health Thresholds 可改百分比阈值）；③ 点进单台 AP 看健康趋势、连接客户端数、信道利用、吞吐、发射功率、在线客户端；④ 切到交换机看 CPU/内存、带宽、帧统计（广播/组播/单播）、错误计数、PoE，以及 VLAN/LLDP/UNP/Golden Configuration 等信息。
  tags: [网络分析, 信道利用率, 设备健康, OmniVista-Cirrus]

- id: f04
  title: 客户端分析工作流（连接曲线→分布→吞吐→时长→人均设备）
  type: framework
  source_chapter: "p147-p153"
  source_quote: |
    "CLIENT ANALYTICS — Connected Clients Over Time; Client Distribution per frequency bands / across managed Access Point / on Access Point per client range. (p147)"
  summary: |
    客户端分析看五个维度：① Connected Clients Over Time 按小时柱状图点选某小时，下方组件联动；② 客户端分布——按频段（2.4/5/6GHz）、按连接模式/设备类型/OS/健康/SSID、按 AP、按"每 AP 客户端数区间"；③ 吞吐消费（客户端收发字节）；④ 会话连接时长；⑤ 每用户设备数。用途判断：客户端是否粘在某个 AP、拥挤区域是否需要加 AP 或换更高性能型号、是否有异常流量。
  tags: [客户端分析, 客户端分布, 吞吐, OmniVista-Cirrus]

- id: f05
  title: 有线客户端 MAC 认证四步配置流程
  type: framework
  source_chapter: "p90-p95"
  source_quote: |
    "2 – Access Auth Profile Configuration; 1 – AAA Server Profile Configuration; [PRE] – Access Role Profiles Preconfigured; 3 – Access Policy Configuration; 4 – Declare Client MAC address in local database. (p90)"
  summary: |
    在 Stellar AP（或 OmniSwitch）有线口上做 MAC 认证的标准四步：
    0) [预置] 创建并应用两个访问角色 ARP_DEFAULT（受限+限带宽）和 ARP_PASS（全通）；
    1) 配 AAA Server Profile（Configure > Network Access > Unified Access，主认证服务器 UPAMRadiusServer，用途选 MAC）；
    2) 配 Access Auth Profile（认证方法 MAC、AAA Profile、默认角色 ARP_DEFAULT、应用到 AP 组并启用端口 Eth1；交换机则选接入端口）；
    3) 配 Access Policy（映射条件 Authentication Type = MAC，认证源 Local Database，角色 ARP_PASS，Web 重定向 None）；
    4) 在 Accounts > Company Property 把客户端 MAC（如 11:22:33:44:55:66）录入本地数据库，再接上有线客户端。
  tags: [有线客户端, MAC认证, Access-Role-Profile, 配置流程]

- id: f06
  title: Mesh/Bridge 配置与监控流程
  type: framework
  source_chapter: "p118-p120"
  source_quote: |
    "In the Device Catalog section, select the AP that will be part of the Mesh or Bridge configuration and go to Actions > Edit Device > Mesh/Bridge Configuration. (p118)"
  summary: |
    配置流程：在设备目录选中参与 Mesh/Bridge 的 AP → Actions > Edit Device > Mesh/Bridge Configuration → 按场景填参数（模式、频段、SSID、密钥管理、密码；Mesh 独有"Is Root"选项）→ 保存后两端生效。监控：Mesh Topology 列表显示每台 AP 的角色（Root/Repeater）与 Parent Address（即 Root AP 的 MAC），用于确认拓扑是否按预期成链。
  tags: [Mesh, Bridge, 配置流程, 监控]

- id: f07
  title: 设备运维工作流（升级/备份/排障/支持信息收集）
  type: framework
  source_chapter: "p224-p236"
  source_quote: |
    "Scheduled Upgrades: Creation of scheduled upgrade, Management of scheduled update... Configuration Backups: Start immediate Backup on the selected device... Scope selection: switch, site, floor. (p233)"
  summary: |
    日常运维五大抓手：① Edit Device 统一改 IP 模式/位置/组与 RF Profile/期望软件版本/管理模式（Analytics Only 或 Full Management）/健康阈值/射频与 Mesh 配置；② 升级计划四步向导（Schedule Setting → AP Groups/设备选择 → Set Software Version → Review），按站点/AP 组/单 AP 维度执行；③ 配置备份（可含安全文件，可按交换机/站点/楼层排程）；④ Device Troubleshooting 给设备下发排障命令（可编辑参数）；⑤ Collect Support Info 收集日志包（AP 是 tar.gz 快照；交换机可选 swlog/cfg/Tech Support 各层级）。另有拓扑应用实时显示链路状态（约 2 秒刷新）。
  tags: [运维, 升级, 备份, 排障, OmniVista-Cirrus]

- id: f08
  title: 全流程部署综合演练（需求驱动的完整交付流程）
  type: framework
  source_chapter: "p286-p299"
  source_quote: |
    "The purpose of this exercise is to practice on Stellar Access Points and OmniVista Cirrus by working on a WLAN Stellar installation... You will be in charge to install and configure the network based on the given requirements. (p288)"
  summary: |
    综合演练把全部技能串成一条交付主线，可当交付 checklist 用：
    ① 复位设备并验证连通（ping DHCP 服务器/外网）；
    ② 组织建模——BREST 主站点（West 楼两层 + East 楼预留）、PARIS 站点预留，导入楼层平面图；
    ③ 设备上线——两交换机 + 两 AP（OS-2360 不能上云管，只能手工配）；
    ④ WLAN——三个 SSID：EmployeesX（WPA2-Enterprise、仅 5GHz、VLAN 20、工作时间调度）、GuestsX（内部 Captive Portal、限 1Mbit/s、封 SSH/Telnet、VLAN 30、周一至周三）、PrinterX（仅 2.4GHz、最小发射功率、固定信道、WPA2 PSK + 按设备 PSK、复用 Employee VLAN）；RF Profile 开负载均衡、关联门限 -50dBm；
    ⑤ 安全——WIPS 流氓 AP 分类规则、失败 5 次/分钟进黑名单、Guest 开客户端隔离、AP 关闭 SSH/Web 管理；
    ⑥ 运维——Golden Config、备份、VLAN 1000 模板（IP 用变量）、标签、支持信息收集、周一 8:00 周报、健康阈值 70%、2.4G 利用率阈值 20%、可用容量 25%；
    ⑦ 拓扑变更——两 AP 建 Mesh（AP1321 为 Root，自定义 Mesh SSID，WPA2-Personal）。
  tags: [综合演练, 交付checklist, 全流程部署, SSID, WIPS, Mesh]

- id: f09
  title: VoWLAN 部署五阶段流程（Prepare→Plan→Design→Implement→Operate）
  type: framework
  source_chapter: "p305-p311"
  source_quote: |
    "These are the major steps for the deployment of VoWLAN in a WLAN Stellar environment... Prepare / Plan / Design / Implement / Operate. (p306)"
  summary: |
    语音无线部署五阶段：
    1) Prepare 准备——明确覆盖/带宽需求，站点勘测（site survey）分析 RF 环境与干扰源，计算 AP 数量与布放（语音按 1 AP/255m²、每 AP 20-25 用户），识别需双 AP 冗余的区域；
    2) Plan 规划——定义语音服务与带宽、"Voice" WLAN 配置、安全等级；RF 管理优先 5GHz；容量规划 20-25 客户端/AP、36Mbps 用户吞吐；漫游激活 802.11r/k/v，同能力设备放专用 SSID；保证 AP 侧网络可靠冗余；
    3) Design 设计——天线与信道选择（相邻 AP 用非重叠信道）、QoS 策略（WMM 队列端到端标记 DSCP/802.1p）、可选 DPI 语音应用管控、语音专用 VLAN、接入交换机千兆端口；
    4) Implement 实施——布线、语音服务器、Radius/DNS/DHCP、IMS3 管理话机、配置话机 SSID、OmniVista 配置；
    5) Operate 运营——监控语音覆盖（SNR/RF 扫描）、VoIP 审计、系统性能、基础设施更新、勘测（Ekahau/AirMagnet）、专业服务支持。
  tags: [VoWLAN, 部署流程, 语音, QoS]

- id: f10
  title: 组织清理流程（云管配置逆向拆除）
  type: framework
  source_chapter: "p313-p319"
  source_quote: |
    "As OmniVista Cirrus 10 is cloud-based, it is not possible to revert the configuration back to the default parameters with one click. (p315)"
  summary: |
    云管没有"一键恢复默认"，拆除要按依赖顺序逆向删：先删运行任务（升级计划/备份/排障命令）→ 重置 WIPS 策略 → 把 AP 改回 default device group、AP 组改回 Default Provisioning Config → 删自定义 AP 组/Provisioning 配置/RF Profile → 删 SSID → 删 Unified Policy List/Policy/ARP/Guest Access Strategy/Captive Portal 模板 → 删员工/访客账号、注册 Profile、Company Property → 取消 Golden Config → 删报表/支持信息 → 重置 Network 与 QoE 分析阈值 → 删站点（连带删楼栋楼层及归属设备）→ 确认设备目录为空 → 删 CLI 模板与值映射。适用于换设备、搬办公室、重配网络前的清理。
  tags: [组织清理, 卸载流程, 云管, OmniVista-Cirrus]

- id: f11
  title: 无线/客户端排障 CLI 检查清单
  type: framework
  source_chapter: "p260-p274"
  source_quote: |
    "Check wireless configuration — Check List: SSID broadcasted on the selected radio(s)? Transmission Power as selected in the RF profile? Encryption activated? BSSID is present? (p260)"
  summary: |
    AP 侧 CLI 排障按层检查：
    ① 无线配置——iwconfig 确认 SSID 在目标射频广播、发射功率与 RF Profile 一致、加密开启、BSSID 存在（无 MAC 即未广播）；接口命名 athXYY：X=0 是 2.4GHz、1 是 5GHz、2 是 6GHz，YY 是 SSID 编号；
    ② RF 配置——cat /tmp/config/rfprofile.conf 对照全局参数（Band Steering/Load Balance/Scanning/国家码/Air Time Fairness）与每射频参数（信道/带宽/功率）；
    ③ 客户端——ssudo sta_list 看 VLAN/IP/在线时长/收发计数/认证方式/最终角色；cat /proc/kes_syslog 看 DHCP 与关联日志；ssudo wlanconfig athXX list 看 RSSI/MINRSSI/MAXRSSI/SNR；
    ④ 接入日志——kes_syslog 按 MAC 过滤看重关联/去关联原因码；
    ⑤ 漫游——adme show 看邻居 AP 与 RSSI；wam.log 搜 "L3 roaming-start/success"、"L2 roaming-success"（p264-265）。
  tags: [排障, CLI, 检查清单, iwconfig, sta_list]

- id: f12
  title: Guest Tunnel 配置流程（附录）
  type: framework
  source_chapter: "p320-p322"
  source_quote: |
    "Figure p320: OS6860-GTTS 和 OS6860-Edge 之间的网络连接，包括 VLAN、IP 地址以及 DHCP 服务器设置；Figure p322: 配置 GTTT 映射方法，选择设备组进行应用。（figures_captions.md，附录原文因字体编码无法完整提取）"
  summary: |
    附录 Guest Tunnel（访客隧道）把访客流量用隧道送到远端集中出口：在 SSID 的 VLAN/Tunnel Mapping 中选择 Tunnel 方式（对应 Tunnel ID 与 Tunnel 终结交换机 TTS 的 IP，见 p76 "Tunnel ID and Tunnel Termination Switch (TTS) IP"），边缘侧由 OS6860-GTTS 交换机终结隧道并与远端 Edge 设备经专用 VLAN/IP 互联，DHCP 由远端提供；配置时先配 GTTT（Guest Tunnel）映射方法，再选择要应用的设备组。注意：附录三页（p320-322）正文为损坏的字体编码，以上依据可读片段与插图标注整理，细节待对照原版 PDF 确认。
  tags: [Guest-Tunnel, 隧道, TTS, 附录, 待确认]
```
