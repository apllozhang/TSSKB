# 框架/排障流程 · OmniAccess Stellar WLAN Advanced Troubleshooting (DT00XTE478EN)

> 来源：source/fulltext.md（页码即教材 PDF 页码）

- id: f01
  title: 七步排障流程（识别→定位→隔离→复现→解决→验证→记录）
  type: framework
  source_chapter: "p10"
  source_quote: |
    Identify: Determine if problem exists, Ask questions & collect infos. Locate: Tied to physical space, Tied to specific devices, Use OSI model to define layer. Isolate: Identify OSI Layer, Specific devices, Specific locations, Driver versions. Re-Create: If you can't recreate this issue, return to step one and ask more questions. Solve: Formulate & Implement plans. Verify: Extensive testing to confirm and verify the solution did indeed solve the issue. Document: Document initial issues, processes, diagnostics & resolutions.
  summary: |
    教材的顶层排障方法论：先把问题问清楚（Identify），再绑定到物理位置和设备（Locate），用 OSI 模型定层（Isolate），随后在自有环境复现（Re-Create），无法复现就回到第一步重新提问。复现成功才动手制定并实施解决方案（Solve，可能涉及驱动、配置或设计变更），做充分测试确认修复（Verify），最后记录问题、过程、诊断与解决方案并跟进（Document）。这条流程贯穿全书所有用例。

  tags: [methodology, process, osi-model]

- id: f02
  title: WLAN 故障三域根因地图（无线侧/本地网络/互联网）
  type: framework
  source_chapter: "p5-8"
  source_quote: |
    Wireless: End User, Wi-Fi Device, Client, RF Medium, Stellar AP. Local Network: LAN, Switch, Firewall & WAN Router, Servers (DHCP Configuration, Lease duration, Address Pool scope, DHCP options; DNS; 802.1X/RADIUS; LDAP/AD). Internet: Bandwidth Throttling, Jitter, Latency, External DNS, External Captive Portal - Issues independent from the network administrator.
  summary: |
    接手任何 WLAN 故障前先扫这张地图：无线侧（终端用户技能/设备开关、驱动、射频能力、802.1X 配置文件、最低速率要求、漫游算法、关联/认证/加密/上层协议、射频介质 RSSI/SNR/覆盖、AP 配置固件）、本地网络侧（PoE/天线/布放/物理层、交换机 VLAN/端口速率/QoS、防火墙 ACL/NAT/限速、DHCP/DNS/RADIUS/LDAP 服务器群）、互联网侧（出口带宽、抖动时延、外部 DNS 与外部门户——这类问题不在网络管理员管控内）。用途是保证排障时不漏掉任何一层。

  tags: [root-cause-map, layered, wlan]

- id: f03
  title: 排障访谈四问定位法（范围→位置→设备→SSID 逐级收窄）
  type: framework
  source_chapter: "p17"
  source_quote: |
    Same behavior for all users? Yes - The issue is not related to a specific device/hardware. Do you observe this issue at the same location or everywhere in the building? In the same section of the building - Not a global OmniVista configuration issue. The impacted clients are all associated to the Stellar APs connected to the same access switch? Yes - The issue might come from the SSID configuration or the access switch configuration. Same issue on other SSIDs in the same location? No, only the connection to the Employee SSID is impacted.
  summary: |
    用"问题-回答-推断-下一步"的表格化访谈逐级收窄故障范围：四问依次确认（1）是否所有用户都受影响（排除个别终端硬件问题）；（2）是固定位置还是全楼（排除全局 OmniVista 配置问题，否则全楼同 SSID 的 AP 都会受影响）；（3）受影响客户端是否都挂在同一台接入交换机下（指向 SSID 配置或该交换机配置）；（4）是否只影响单个 SSID（进一步锁定到该 SSID 的 VLAN/配置）。每一步答案都决定下一问的方向，前面的答案会关闭后面的通用问题。

  tags: [interview, scope-narrowing, use-case]

- id: f04
  title: 实验室复现法（采集四类配置，在自有环境重建拓扑与故障）
  type: framework
  source_chapter: "p12"
  source_quote: |
    Gather network configuration from customer: Access switches: vcboot.cfg; OmniVista: Access the Organization; Stellar AP: APs configuration Backup; Servers: Backup configuration. Re-create customer topology in your environment. Re-create customer issue in your environment.
  summary: |
    定位（Identify/Locate/Isolate）之后的复现手段：向客户采集四类配置——接入交换机配置文件（vcboot.cfg）、OmniVista 组织配置、Stellar AP 配置备份、服务器（DHCP/RADIUS 等）配置备份，然后在自有实验环境按 1:1 重建客户拓扑，再在其上重现客户问题。复现的价值是排除客户描述偏差，确认没有另一个隐藏根因（教材用例原话：复现没有显示出该问题的其他根因）。

  tags: [reproduction, lab, use-case]

- id: f05
  title: 验证-记录-跟踪闭环（先实验后生产，验证无副作用才算关单）
  type: framework
  source_chapter: "p13-14"
  source_quote: |
    Test the solution in your environment. Apply the correction in the customer environment. Ask the client to test their day-to-day wireless applications (Rainbow, voice, mail,...) and wireless devices to check the solution stability. Document the troubleshooting case: Issue description, Topology, Firmware versions, Diagnostic, Resolution. Follow the case - Check that the solution is permanent - No side effects due to the resolution.
  summary: |
    解决方案的落地顺序是三段式：先在自己的环境测试，再应用到客户环境，最后让客户用日常真实业务（Rainbow、语音、邮件等）和设备验证稳定性。结案时要完整记录问题描述、拓扑、固件版本、诊断、解决方案（配置修改/目标固件版本/硬件更换），并持续跟踪确认方案是永久性的、没有因修复引入副作用。沉淀目的地是 ALE 技术知识中心（TKC）数据库。

  tags: [verification, documentation, closure]

- id: f06
  title: 勘测类型选择矩阵（被动/主动/预测 × 场景）
  type: framework
  source_chapter: "p106-107"
  source_quote: |
    Passive: Listen WLAN traffic, No authentication and 802.11 association, All frequencies are scanned, Detects Access Points, Measure signal strength, Measure noise. Active: Associate survey tool to (multiple) access point, Measure packets loss, retransmission, physical rates. Predictive: Simulation tool, Import site plan & RF characteristics of objects, No field measurements. Predictive: Pre-deployment, place new APs; Passive: Post-deployment, RF analysis; Active: Post-deployment, clients performance analysis.
  summary: |
    三类勘测对应三个阶段：预测勘测（Predictive）用于部署前，导入平面图和物体射频特性做仿真、自动摆放 AP，不做实地测量；被动勘测（Passive）用于部署后，只监听不下联，扫全频段，能发现 AP、测信号强度和噪声；主动勘测（Active）也用于部署后，勘测工具真实关联 AP，除被动指标外还能测丢包、重传和物理速率。选型口诀：新网/换网前用预测，上线后查射频用被动，查客户端性能用主动；排障时被动+主动组合。

  tags: [site-survey, passive, active, predictive]

- id: f07
  title: 现场排障三步法（拿图纸→勘测观察→纠正动作）
  type: framework
  source_chapter: "p114-117"
  source_quote: |
    Step 1 - Get the floor plans: Identify potential issues: obstacles, walls, ceiling height; Identify areas where WiFi is required; Locate Access Point. Step 2 - Site Survey observation: Identify AP model same as original design? RF overlap - Co/Adjacent channel interference? Areas with no radio coverage? AP transmission power default or customized? AP location troublesome? Step 3 - Corrective actions: Change AP model, Rework RF wireless design, Rework channel width, Remove lower data rates, Improve AP placement.
  summary: |
    "WiFi 网络表现不佳"类问题的现场作业流程。第一步拿平面图，标出障碍物、所需覆盖区域（按高/中优先级）和 AP 位置；第二步实地勘测观察五项——AP 型号是否与原设计一致、AP 间射频重叠是否造成同频/邻频干扰、无覆盖区域是 AP 宕机还是没布、发射功率是默认值还是定制值、AP 位置是否别扭；第三步执行纠正动作：换更强天线/户外型 AP、重调发射功率和信道、压缩信道宽度抑制干扰、移除低数据速率逼客户端贴近信号好的 AP、改善布放。

  tags: [on-site, survey-workflow, corrective-action]

- id: f08
  title: TKC 用例检索与版本比对流程
  type: framework
  source_chapter: "p127-130"
  source_quote: |
    Issue description: After replacing the legacy wifi network... some clients experience disconnections while roaming. Compare version build. Same version: Check the case Resolution. Older version: Check case Resolution & Solution -> Issue might already be fixed with a build. Do you reach the same conclusions? Yes: Apply the solution and validate it. No: Search for another use case or contact the technical support to create a new one.
  summary: |
    用 TKC（技术知识中心）排障的流程：用自己的故障描述检索用例库，多个结果时逐个比对选最相关的；先看描述是否匹配自己的问题，再看版本构建号——同版本直接看 Resolution，案例版本更旧说明问题可能已被某个 build 修复（查 Solution 升级），更新则可能最新 build 已修。套用方案前必须亲自重复案例的诊断步骤，结论一致才应用并验证；不一致就换下一个用例或联系技术支持创建新用例。前提是确认自己有设备和客户端的访问权限。

  tags: [tkc, knowledge-base, version-comparison]

- id: f09
  title: 802.1X 认证失败三段排查法（客户端→AP→RADIUS 服务器）
  type: framework
  source_chapter: "p88-90"
  source_quote: |
    1) On Client side: Check Username and password, Encryption type, Security type/key, Certificate on client (if any). 2) On AP side: Correct Radius server attached to the SSID? Compare Radius configuration to Radius server: IP and ports, Shared Secret key. 3) On Radius server side: Compare Radius configuration and database to client and AP configuration: Username/password, Shared Secret, Radius client IP, Radius station IP (IP address of the Stellar AP), Certificate, Radius service enabled? Firewall allows authentication and accounts ports?
  summary: |
    802.1X 链路上有三个可断点，按序排查：客户端侧查用户名密码、加密类型、安全类型/密钥、客户端证书；AP 侧查 SSID 是否绑定了正确的 RADIUS 服务器、AAA 配置与服务器的 IP/端口/共享密钥是否一致；服务器侧查用户数据库、共享密钥、RADIUS 客户端 IP 与站点 IP（即 AP 的地址）、证书、认证计费端口，还要确认 RADIUS 服务已启用且防火墙放行端口。任何一环不匹配都表现为"连不上"。

  tags: [802.1x, radius, three-segment]

- id: f10
  title: 分层排障路径（OSI 定层 + 基础/无线/客户端/网络四层展开）
  type: framework
  source_chapter: "p10, p38-102"
  source_quote: |
    Isolate: Identify OSI Layer, Specific devices, Specific locations, Driver versions. Basic Troubleshooting (p38): The hardware of the Stellar Access Points, The system of the Stellar Access Points, The Captive Portal solution, A cluster in Express mode. Wireless Troubleshooting (p61). Client Troubleshooting (p73). Network Troubleshooting (p92).
  summary: |
    隔离阶段的原则是用 OSI 模型确定故障所在层，然后进入对应的专项排障层：基础层（AP 硬件 LED、系统与固件、Captive Portal、Express 集群）、无线层（SSID/RF 配置、热图、漫游）、客户端层（关联、IP 获取、掉线、802.1X）、网络层（AP 的 IP 配置、连通性、邻居、服务器）。先低层后高层，避免一上来就怀疑高层的认证/DNS 而实际是 PoE 或 VLAN 的底层问题。

  tags: [osi-model, layered-troubleshooting, decision-path]
