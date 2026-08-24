# 陷阱/反例 · OmniAccess Stellar WLAN Advanced Troubleshooting and Update (DT00XTE378EN)

> 来源：source/fulltext.md（页码即教材 PDF 页码）
> 范围：仅 p134 以后的 Features Update 增量内容（升级/新特性相关坑；p1-133 排障篇以姊妹书 T478 为准）

- id: ce01
  title: Band Steering 默认关闭的原因——5GHz 覆盖弱时会把客户端赶去差频段，Force 5GHz 更无退路
  type: counter-example
  source_chapter: "p364"
  source_quote: |
    "Band steering generally assumes that the coverage areas on both the 2.4 GHz bands and 5 GHz bands are the same... band steering will prove problematic if coverage on 5 GHz is significantly weaker and has coverage holes... a 5 GHz-capable device is automatically redirected to the 5 Ghz band by the band steering feature, even if the 5 GHz signal is low. (Force 5 GHz) the network will not allow the client device to 'fall back' to the 2.4 GHz network."
  summary: |
    RF Profile 里 Band Steering 默认关闭不是疏忽：它默认假设 2.4G 与 5G 覆盖大体相同，一旦 5G 覆盖明显更弱（有覆盖洞），支持 5G 的设备仍会被强行引导到 5G——信号再差也留在差频段。Force 5GHz 更极端，直接忽略 2.4G 关联请求，客户端无路可退。正确做法：新网络按双频同覆盖设计；存量改造做不了双频同覆盖时避免开 Band Steering，或用 Exclude MAC OUI 把老旧/时延敏感设备（扫描枪、MIPT 话机）排除在引导之外。

  tags: [band-steering, force-5ghz, coverage-hole, rf-profile, default-off]

- id: ce02
  title: AP 注册国家码选错直接导致 AP 拒绝工作——远程实验室禁选 USA/JAPAN/ISRAEL
  type: counter-example
  source_chapter: "p231"
  source_quote: |
    "Select Country/Region = FR-France (selecting your own country code here may lead to compatibility problem with the Stellar APs used in this infrastructure! See the WARNING section below to learn why). Warning: DO NOT CHOOSE THE COUNTRY CODE USA, JAPAN OR ISRAEL AS THE STELLAR ACCESS POINTS USED IN THE REMOTE LAB ARE NOT COMPATIBLE WITH THESE COUNTRY CODES."
  summary: |
    OmniVista 首次进 AP Registration 要选国家码，这个选择决定 AP 允许的信道与功率。教材实验室的 AP 硬件区域码与 USA/JAPAN/ISRAEL 不兼容，选了这三个国家码 AP 会上不了线。推广到现网：跨境项目或二手设备调拨时，AP 出厂区域与网管侧国家码不一致就会出现"设备完好却无法提供服务"的假故障；先用标签/序列号确认 AP 销售区域，再在网管里选匹配的国家码。

  tags: [country-code, regional-compliance, ap-registration, onboarding-failure]

- id: ce03
  title: 评估许可的两种导入方式二选一，且密钥只能贴键值不能整行复制
  type: counter-example
  source_chapter: "p209-210"
  source_quote: |
    "2 possibilities: Inserting directly the license file obtained in the previous part; Inserting the license keys. Don't do both! Warning: COPY AND PASTE ONLY THE LICENSE KEYS AND NOT THE ENTIRE LINES! (HIGHLIGHTED THE INFO THAT YOU HAVE TO COPY AND PASTE)."
  summary: |
    OmniVista 2500 评估许可（90 天，一个文件打包全部设备与服务许可）安装有两个坑：(1) 文件导入与密钥手填两种方式只能选一种，两个都做会出问题；(2) 走密钥方式时，license 文件里每行是"许可名 + 密钥"的组合，License Key 输入框里只允许贴密钥部分（去掉行首的许可名如 EVAL-NM-EX-20-N），整行复制会导入失败。此外生成新许可前先删掉桌面上旧的 "-EVAL-OV2500…" 文件，避免新旧混淆；导入成功后也要删掉本地许可文件。

  tags: [evaluation-license, license-install, copy-paste, omnivista-2500]

- id: ce04
  title: Restore 显示成功但配置没生效——文件只落 WORKING/CERTIFIED，不碰 RUNNING
  type: counter-example
  source_chapter: "p429"
  source_quote: |
    "The configuration files are transferred in the WORKING and CERTIFIED folders but are NOT applied on the RUNNING configuration (could cause major problems in real cases scenarios if it was the case). To force the configuration restored in the WORKING directory to be used by the OmniSwitch, launch the following command: reload from working no rollback-timeout."
  summary: |
    教材现场复现了这个坑：恢复备份后 Result 页显示 SUCCESS，但实验中临时创建的 VLAN 70-80 依然存在——因为恢复只把 vcboot.cfg 写进 WORKING 和 CERTIFIED 目录（故意不碰 RUNNING，否则直接覆盖运行配置会引发生产事故），需要 reload from working no rollback-timeout 重启交换机（约 3 分钟）才真正生效，之后还要在 VLAN Manager 里点 Poll 强制刷新缓存视图。经验：把"恢复成功"理解为"文件已就位"，生效必须跟一次显式 reload，变更窗口要把这几分钟算进去。

  tags: [restore, working-certified-running, reload-working, false-success, omniswitch]

- id: ce05
  title: ALE 固件包是 WinZip 自解压格式——手动解压再导入等于废掉升级文件
  type: counter-example
  source_chapter: "p431"
  source_quote: |
    "All upgrade files supplied by Alcatel-Lucent Enterprise Customer Service are packaged as WinZip executables and have a *.zip file extension. Do not attempt to unzip the firmware files manually. When you Import the WinZip executable, OmniVista automatically unzips the executable as part of the import process."
  summary: |
    ALE 客户服务交付的交换机/AP 固件包是 WinZip 自解压可执行文件（扩展名 .zip）。Resource Manager 的 Import 会自动完成解包，工程师若习惯性先手动解压再上传，导入流程反而会失败。正确顺序：拿到 .zip 原包直接 Browse 上传 → Import 自动解压 → 列表里选中该固件 → Install 时核对固件支持的设备型号清单与在网设备匹配 → 按设备或按 AP 组下发。

  tags: [firmware, upgrade, winzip, import, resource-manager]

- id: ce06
  title: OV2500 没配 DNS，WCF 直接"Not in service"且连不上 Brightcloud API
  type: counter-example
  source_chapter: "p287, p348"
  source_quote: |
    "Configure DNS: No DNS -> WCF not in Service. In the OmniVista CLI, configure DNS. DNS -> WCF in Service. (p348) The Web Content Filtering feature requires the DNS configuration on the OmniVista server. If the DNS configuration is missing in the OmniVista 2500, the status of the WCF feature will be 'Not in service' and the OmniVista won't be able to join the Brightcloud API."
  summary: |
    WCF 的分类查询依赖 OmniVista 2500 服务器访问云端 Brightcloud API，服务器自身没有 DNS 就解析不了 API 域名，WCF 状态停在 "Not in service"，无论 AP 侧和档案配得多正确都不工作。修复路径：vSphere Web Console 进 OV2500 虚机（cliadmin），配置菜单选项 [2] → [6] 检查并补 DNS 服务器（实验环境 DNS1 10.130.5.130 / DNS2 10.0.0.51），确认重启生效后在 UPAM > Web Content Filtering 页确认状态转 "in service"。部署 WCF 前先把服务器 DNS 列为前置检查项。

  tags: [wcf, dns, brightcloud, not-in-service, prerequisite]

- id: ce07
  title: 访客策略推完不生效——Policy 只在客户端认证成功那一刻应用，必须强制重连重认证
  type: counter-example
  source_chapter: "p338"
  source_quote: |
    "BEFORE PERFORMING THE TEST, BE SURE TO DISCONNECT AND RECONNECT THE VIRTUAL MACHINE FROM THE NETWORK TO FORCE THE RE AUTHENTICATION AS THE POLICY IS APPLIED ONCE THE CLIENT AUTHENTICATION IS SUCCESSFUL."
  summary: |
    把 Policy List（如禁止访客 telnet/SSH）挂到 Access Role Profile 并 Notify All 推送后，已在线的访客不会被立即套用新策略——策略仅在客户端认证成功的瞬间下发。教材用加粗警告提醒：测试前必须把客户端断开重连（或踢下线）强制重新认证，否则会误判"策略没生效/配置有错"。同理适用于一切依赖 Access Role Profile 下发的变更（带宽、WCF 档案等）：改完配置 → 推送到设备 → 让受影响客户端重新认证，三步缺一不可。

  tags: [policy-list, re-authentication, access-role-profile, ineffective-change]

- id: ce08
  title: 漫游瞬间撞上后台扫描——语音有感知豁免，其他实时业务照样被打断
  type: counter-example
  source_chapter: "p192"
  source_quote: |
    "When a user roams, his real time traffic can be interrupted if the new AP on which he is connected is using the background scanning. No impact on the voice traffic. The AP is voice aware and will deactivate the background scanning when a voice call is detected. Other real-time traffic can be impacted."
  summary: |
    后台扫描（Background Scanning）与漫游的冲突场景：客户端刚漫游到的新 AP 正在做后台扫描，实时业务会被打断。AP 具备语音感知，检测到语音呼叫会自动暂停扫描，所以语音没事；但视频会议、软终端以外的实时流量没有这层豁免，仍会受影响。两个对策：对时延敏感区域直接关闭 AP 的 Background Scanning；或在网络里加装几台专职扫描 AP（只做扫描不服务客户端），代价是额外购置 AP。射频调优特性与业务体验冲突时，先识别哪类流量会被豁免、哪类不会。

  tags: [background-scanning, roaming, real-time-traffic, voice-awareness]

- id: ce09
  title: Roaming RSSI 阈值设两头都是坑——太低粘着弱 AP，太高漫游过度丢包
  type: counter-example
  source_chapter: "p191"
  source_quote: |
    "The Roaming RSSI Threshold controls the signal strength a client needs to see before searching for another site. If the RSSI threshold is too low, the client remains on a low signal strength site, even with a stronger site nearby. If the RSSI threshold is too high, the client roams too much that could result to packet loss."
  summary: |
    粘滞客户端治理参数本身是双刃剑：Roaming RSSI Threshold（RF Profile，配 802.11k/11v 使用，范围 0-100，推荐 2.4G=10、5G=15）设得过低，客户端守着信号很差的 AP 不走，旁边有更强 AP 也不切；设得过高，客户端频繁切换 AP，漫游风暴反而带来丢包。调参思路是从推荐值起步，按现场信号分布小幅调整并观察漫游次数与丢包率，而不是一次性拉满或拉空。

  tags: [roaming-rssi-threshold, sticky-client, over-roaming, packet-loss]

- id: ce10
  title: 给 Stellar AP 做 Restore 是行不通的——配置由 AP Group 下推，备份文件另有用途
  type: counter-example
  source_chapter: "p430"
  source_quote: |
    "It is not possible to perform a restore on a Stellar AP, as most of the configuration is pushed when the Access Points is inserted in an AP Group. However, backup files of Stellar APs can be used to analyze/troubleshoot problems with APs. See the Troubleshooting lab for more information."
  summary: |
    从交换机操作习惯迁移过来的工程师常期望"AP 备份→AP 恢复"对称可用，但 Stellar AP 的架构决定了它不行：绝大多数配置是 AP 加入 AP Group 时由网管下推的，单台 AP 没有"回灌配置"的通道。Resource Manager 的 Restore 只对 AOS 交换机开放。AP 备份文件的正确用途是离线分析、排障比对和提供给技术支持。要"恢复"一台配置异常的 AP，实际路径是修正 AP Group 配置后让 AP 重新拉取，或干脆恢复出厂（reset 键 6 秒 / ssudo firstboot -y）重新入组。

  tags: [stellar-ap, restore-not-supported, ap-group, firstboot, mental-model]
