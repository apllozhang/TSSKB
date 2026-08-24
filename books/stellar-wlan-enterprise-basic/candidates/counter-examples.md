# 陷阱/警告 · OmniAccess Stellar WLAN Enterprise Basic (DT00XTE368EN)

> 来源：source/fulltext.md（页码即教材 PDF 页码）

- id: ce01
  title: 陷阱：现场禁用 WEP（40/104 位密钥均可破）
  type: counter-example
  source_chapter: "p63"
  source_quote: |
    "WEP: Encryption Algorithm: Rivest Cipher 4 (RC4); 2 Modes: 40-BIT KEY + 24-BIT IV; 104-BIT KEY + 24-BIT IV... TOO WEAK. TOO WEAK. NEVER USE WEP ON SITE. 128 Bits Mode -> TOO WEAK."
  summary: |
    教材用全大写强调的红线：WEP 无论 64 位（40 位密钥+24 位 IV）还是 128 位（104 位密钥+24 位 IV）模式都太弱，现场永远不要用。这是全书唯一用"NEVER"字样的安全禁令。遇到遗留 WEP 网络（老打印机/老扫描仪环境）应迁移到 MAC 认证过渡或直接换 WPA2/WPA3，同时注意 6E/WiFi7 时代 PMF 强制、老协议根本进不了 6 GHz 频段。

  tags: [wep, security, forbidden, rc4]

- id: ce02
  title: 陷阱：勘测只是时间快照，预测不了未来
  type: counter-example
  source_chapter: "p133"
  source_quote: |
    "No matter how accurately the wireless site survey is done, its not possible to accurately determine future: Usage patterns; Expansions; External interferences. The Site survey is a snapshot in time. The more snapshots you have the better you can understand the environment."
  summary: |
    对勘测报告的期望管理：再精确的勘测也无法准确预知后续的使用模式变化、扩容和外部干扰出现——勘测是某一时刻的快照。应对办法是做周期性复测，多份快照对比才能理解环境的演化趋势（教材配了 1st/2nd/3rd/4th 四次快照示意）。给客户交付勘测报告时应写明这一局限性，避免"测一次管五年"的错误预期。

  tags: [site-survey, snapshot, expectation, periodic]

- id: ce03
  title: 陷阱：无线网络不要过度配置（Over provisioning）
  type: counter-example
  source_chapter: "p134"
  source_quote: |
    "Over provisioning is not a good option with wireless networks. Wireless controllers can take care of the channel interference but there are a limited number of channels in the 2.4 Ghz, 5 Ghz and 6GHz bands."
  summary: |
    有线网"多买设备总没错"的思路在无线不成立：2.4/5/6 GHz 每个频段的信道数是硬上限，AP 摆得再多，同频复用密度过高后自干扰抵消增益，控制器能自动调信道功率也救不回信道不够用的根本约束。容量不足的正确解法是重做 RF 设计（更宽频段/更窄蜂窝/卸载到 6 GHz），而非盲目堆 AP。

  tags: [over-provisioning, co-channel, capacity, design-error]

- id: ce04
  title: 陷阱：勘测复现不了大规模并发，也算不出天线朝向
  type: counter-example
  source_chapter: "p135"
  source_quote: |
    "It is difficult to replicate the whole set-up for wireless network, during the site survey. The results of a large number of concurrent users simultaneously accessing the wireless network is different from the site survey results. Site survey software cannot accommodate/suggest antenna orientation or directional coverage. Antennas must be adjusted manually."
  summary: |
    勘测数据的两个盲区：（1）勘测环境很难 1:1 复刻真实负载，大量用户并发接入时的实测表现会偏离勘测结果——勘测热图好不代表高峰期体验好；（2）勘测软件无法建议天线朝向或定向覆盖形状，外接天线的方向图必须人工调整验证。交付后遇到"勘测全绿、用户吐槽"的场景，先查这两条。

  tags: [survey-limitation, concurrency, antenna-orientation, gap]

- id: ce05
  title: 陷阱：金属吸波、电梯屏蔽、镀膜玻璃掉信号
  type: counter-example
  source_chapter: "p136"
  source_quote: |
    "Materials such as brick, plaster, cement, metal, stone, and double-glazed glass may cause problems. Metal absorb Wi-Fi signals. Elevators block Wi-Fi signals to a great extent. To cover inside an elevator place APs at the top or bottom of the shaft or in the car itself. Tinted glass and window film have metal in them so expect a drop in signal strength."
  summary: |
    建筑材质的三个高频翻车点：金属直接吸收 WiFi 信号（货架、文件柜、机柜旁都是弱覆盖区）；电梯井对信号近乎全屏蔽，要覆盖轿厢内必须把 AP 放井道顶部/底部或轿厢内；着色玻璃和窗贴膜含金属成分，穿过后信号强度会明显下降。非多孔材质墙体也会让覆盖半径变小或速率变慢。勘测画墙时这些要与 p113-115 的 dB 常数一起计入。

  tags: [materials, metal, elevator, tinted-glass, attenuation]

- id: ce06
  title: 陷阱：Express 切 Enterprise 不迁移配置，集群配置全丢
  type: counter-example
  source_chapter: "p157"
  source_quote: |
    "Mode can be changed: Manually in Express mode with a 'Convert to Enterprise' button; Or requires a factory reset (push button) and reboot... Add option 138 in the DHCP server for the AP management scope... No configuration migration, AP cluster configuration is lost."
  summary: |
    模式迁移的代价必须提前告知客户：从 WiFi Express（集群）切到 WiFi Enterprise（OV 管理）时，原集群的配置不迁移、直接丢失。正确姿势是先在 DHCP 管理 VLAN 作用域加 option 138，再用 Express 界面的 Convert to Enterprise 按钮或恢复出厂重启用 AP 进 Enterprise 模式，然后在 OV2500 里重建 SSID/策略等配置。变更窗口里要预留配置重建时间。

  tags: [mode-change, migration, config-loss, express-to-enterprise]

- id: ce07
  title: 陷阱：AP 不出现在 Unregistered 列表的五查清单
  type: counter-example
  source_chapter: "p250"
  source_quote: |
    "Check the Managed tab (the AP has been manually added)... The AP did not contact OmniVista: Check option 138 on the DHCP Server: Option 138 is missing; Wrong IP address in the option 138. Check the network infrastructure: Management VLAN is missing; Missing route in a L3 network; 'ip dhcp-relay' not configured on the OmniSwitch. OmniVista 2500 is not ready: Check that all the OmniVista services are started from the Watchdog."
  summary: |
    AP 无影的排查顺序：先看 Managed 页（可能已被手工添加自动入列）；再查 option 138（缺失或 IP 填错都直接断联系）；再查网络侧（管理 VLAN 没放通、三层缺路由、交换机没配 ip dhcp-relay）；最后查 OV2500 本身——从 Watchdog 确认所有服务状态为 Running。这五条覆盖了 Enterprise 上线故障的绝大多数根因，按序排查避免乱抓。

  tags: [troubleshooting, ap-registration, option-138, dhcp-relay, watchdog]

- id: ce08
  title: 陷阱：国家码不匹配=射频全关；实验室禁选 USA/日本/以色列
  type: counter-example
  source_chapter: "p243/270"
  source_quote: |
    "AP is unmanaged when Registration fails... Country Code does not match the Country Code from the RF Profile. Configuration not applied & All Radios are off." / "DO NOT CHOOSE THE COUNTRY CODE USA, JAPAN OR ISRAEL AS THE STELLAR ACCESS POINTS USED IN THE REMOTE LAB ARE NOT COMPATIBLE WITH THESE COUNTRY CODES."
  summary: |
    两层教训：（1）通用规则——AP 国家码与 OV2500 RF Profile 国家码不一致即注册失败进 Unmanaged，配置不下发且全部射频关闭；跨国项目里灰 parallel 进口设备常踩这条；（2）实验室特例——R-Lab 的 Stellar AP 硬件与 USA/日本/以色列国家码不兼容，选国家码必须选 FR-France，否则直接兼容性问题。设定国家码时硬件来源与 RF Profile 两边都要核。

  tags: [country-code, rf-profile, radios-off, registration-failure]

- id: ce09
  title: 陷阱：AP Group 属性里不要开 SSH Login
  type: counter-example
  source_chapter: "p271"
  source_quote: |
    "WARNING: DO NOT ENABLE THE 'SSH LOGIN' SETTING (in the AP Group properties)."
  summary: |
    实验与生产中都适用的告警：AP Group 属性面板里的 SSH Login 选项不要启用。Enterprise 模式下 AP 的 SSH 控制台默认是关闭的（OV2500 的 CLI Terminal 进不去），官方路径是 Network > AP Registration > AP Group 里编辑并修改 support/root 密码来激活 SSH；但课程明确要求不要开该选项——AP 侧排障应使用实验室预置的 AP 控制台连接，并保持 AP Group 密码不动，避免破坏环境一致性。

  tags: [ssh-login, ap-group, security, warning]

- id: ce10
  title: 陷阱：许可 key 只贴 key 不贴整行，文件与 key 二选一
  type: counter-example
  source_chapter: "p220"
  source_quote: |
    "2 possibilities: Inserting directly the license file... Inserting the license keys. Don't do both!... COPY AND PASTE ONLY THE LICENSE KEYS AND NOT THE ENTIRE LINES! EVAL-NM-EX-20-N, KEQWEXRH-VXDJBEUM-4EX$299Z-..."
  summary: |
    安装评估许可的两个易错点：（1）文件导入与 key 手工粘贴两种方式只能选其一，同时做会冲突；（2）粘 key 时只复制许可 key 本身，不要把整行（含许可名如 "EVAL-NM-EX-20-N,"）一起复制，否则提交失败。许可文件本身是明文，用记事本打开即可逐条取 key。装完记得删除本地许可文件，防止下期培训混淆。

  tags: [license, installation, key-format, warning]

- id: ce11
  title: 陷阱：Roaming RSSI 阈值过低粘终端、过高频切换
  type: counter-example
  source_chapter: "p424"
  source_quote: |
    "If the RSSI threshold is too low, the client remains on a low signal strength site, even with a stronger site nearby. If the RSSI threshold is too high, the client roams too much that could result to packet loss."
  summary: |
    漫游调参的双向失败模式：阈值太低——终端守着弱信号 AP 不肯走，明明旁边有更强信号也不切换（粘性终端症状）；阈值太高——终端过于敏感频繁换 AP，每次切换都可能丢包。推荐起点 2.4 GHz=10、5 GHz=15（范围 0-100），配合 802.11k/802.11v。调优时症状对号：用户"信号差还不断线"查偏低，"频繁掉线切换"查偏高。

  tags: [rssi-threshold, sticky-client, roaming, tuning, failure-mode]

- id: ce12
  title: 陷阱：背景扫描打断实时业务（语音除外）
  type: counter-example
  source_chapter: "p425"
  source_quote: |
    "When a user roams, his real time traffic can be interrupted if the new AP on which he is connected is using the background scanning. No impact on the voice traffic. The AP is voice aware and will deactivate the background scanning when a voice call is detected. Other real-time traffic can be impacted. Solution: Deactivate the Background scanning on the Stellar APs, or Install new Stellar APs acting as dedicated scanning APs."
  summary: |
    背景扫描与实时业务的冲突：用户漫游到一台正在做背景扫描的 AP 时，实时流量可能被打断。语音有幸免机制——AP 具备语音感知，检测到通话会暂停背景扫描；但其他实时业务（视频会议、流媒体）没有这层保护。两种解法：直接关 AP 的背景扫描，或加装专用扫描 AP（代价是要额外采购 AP）。高实时业务占比的场馆/医院网络要在设计期就决策。

  tags: [background-scanning, real-time, voice-aware, design-tradeoff]

- id: ce13
  title: 陷阱：AP 地理相邻却电波互不可见，漫游失效
  type: counter-example
  source_chapter: "p423"
  source_quote: |
    "In some cases, Stellar APs are geographical neighbors but can't see each other (i.e: radio waves blocked by corridor with right angles...). The client context can't be shared. No roaming. Solution: On both AP, add statically the neighbor Stellar AP from the list of known AP. The client context can be shared through the LAN and the client can roam."
  summary: |
    漫游失效的一类隐蔽根因：两台 AP 空间上相邻，但电波被直角走廊等结构遮挡，互相发现不了——空口邻居发现失败导致客户端上下文无法共享，漫游直接不发生。解法是在两台 AP 上互配静态 Neighbor AP（AP Registration > Access Point 视图里点 Neighbor AP 链接编辑，两边都要配），让上下文改走 LAN 共享，漫游恢复。排查"走到固定区域必掉线"类工单时优先怀疑这个。

  tags: [neighbor-ap, roaming-failure, rf-blocked, static-config]

- id: ce14
  title: 陷阱：OV2500 没配 DNS，WCF 直接 Not in service
  type: counter-example
  source_chapter: "p401"
  source_quote: |
    "The Web Content Filtering feature requires the DNS configuration on the OmniVista server. If the DNS configuration is missing in the OmniVista 2500, the status of the WCF feature will be 'Not in service' and the OmniVista won't be able to join the Brightcloud API."
  summary: |
    WCF 部署的前置条件常被漏掉：OV2500 服务器本身必须配好 DNS，否则 WCF 状态停在 Not in service，根本连不上 Brightcloud 云分类 API——此时 AP Group 开了 WCF、Profile 配了类目也全部无效。修复路径：vSphere 进 OV2500 控制台，菜单 [2]/[6] 配置 DNS 服务器（本实验为 10.130.5.130 与 10.0.0.51），服务需重启生效。验收 WCF 部署时第一步先看 WCF Profile 页的运行状态。

  tags: [wcf, dns, brightcloud, not-in-service, prerequisite]

- id: ce15
  title: 陷阱：策略在认证时套用，改完不重连不生效
  type: counter-example
  source_chapter: "p391"
  source_quote: |
    "BEFORE PERFORMING THE TEST, BE SURE TO DISCONNECT AND RECONNECT THE VIRTUAL MACHINE FROM THE NETWORK TO FORCE THE RE AUTHENTICATION AS THE POLICY IS APPLIED ONCE THE CLIENT AUTHENTICATION IS SUCCESSFUL."
  summary: |
    Unified Policy/Policy List 的生效时机：策略在客户端认证成功那一刻套用到用户角色上。修改或新下发策略后，已在线的用户不会自动吃到新策略——必须断开重连（强制重新认证）才应用。测试策略与生产变更都适用：改完 Access Role Profile/Policy List 后先让目标用户重连再验结论，否则会误判"策略没生效"。

  tags: [policy, re-authentication, timing, testing]

- id: ce16
  title: 陷阱：访客账号过期与服务器/AP 时间不同步
  type: counter-example
  source_chapter: "p382-383"
  source_quote: |
    "A guest account has an expiration date. It is important to check that the date and time are correctly set up... OmniVista 2500 Console: Choose option [10] Advanced Mode, From the CLI, use the command date... support@AP-0E:E0:~$ date (on the Stellar AP)."
  summary: |
    访客认证失败的隐藏变量：Guest 账号带有效期，而有效期判断依赖系统时钟——OV2500 与 AP 两端的日期时间任一不准，都会出现"账号明明没到期却登录失败"。排障动作固定两步：OV2500 虚机菜单 [10] Advanced Mode 后执行 `date`；AP 串口下执行 `date`。同类问题也影响门户 HTTPS 证书校验。部署时给 OV2500 与 AP 配 NTP 是根治方案。

  tags: [guest-account, expiration, ntp, time-sync, troubleshooting]
