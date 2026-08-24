# counter-examples.md · 失败模式/警告/局限/陷阱候选（OmniAccess Stellar WLAN Presales Ed28）
> 提取阶段产物，未做筛选，宁多勿漏；后续有独立验证阶段。
> 引用均为书中英文原文，source_chapter 为原文页码标记。

```yaml
- id: ce01
  title: 三套 License 体系并存，part number 互不通用，Cirrus 4 与 10 迁移路径书里没讲清
  type: counter-example
  source_chapter: "p128, p153, p144/p167"
  source_quote: |
    "Stellar Enterprise On Premise (OmniVista 2500) / Stellar Express / No License / 5 permanent licenses / Stellar Enterprise Cloud (OmniVista Cirrus 4) ... Total number of license part numbers: 7 x 3 x 3 = 63 part numbers"
  summary: |
    同一本书里并存三套报价语言：OV2500 用 OV-AP-NM-X-N / OV-GA-X-N（p136），Cirrus 4 用 OVC-AP-BAS-XY / OVC-AP-BIZ-XY（p144），Cirrus 10 用 OVCX-[类别]-[级别]-[时长] 共 63 个 part number（p153/p167）。三者语法相近但完全不通用。
    踩坑场景：售前在一张报价单里混用体系（如给 Cirrus 10 客户报了 OVC-AP-BAS-3Y），或老客户已买 Cirrus 4 订阅、续费时被按 Cirrus 10 语法重报。后果是订单被 eBuy 退回或激活失败，续费口径对不上客户已有资产。
    更大的坑：书里同时教 Cirrus 4 和 Cirrus 10（p60 云管理"OmniVista Cirrus 4 Or OmniVista Cirrus 10"），但 Cirrus 4 老订阅如何迁到 Cirrus 10、已付费用能否折算，全书着墨极少（BOOK_OVERVIEW 批判章节同样点名此盲点）。
    规避方法：报价前先确认客户网管平台是 OV2500 / Cirrus 4 / Cirrus 10 哪一个，再选对应 part number 表；Cirrus 4 存量客户续约时单独向 ALE 确认迁移政策，不要凭书内内容作答。书中 p155 还把 Cirrus 10 Premium 级别误写成 "Premium subscription level: BAS"，本身就是这个体系容易混淆的证据。
  tags: [license, quotation, cirrus4, cirrus10, risk, ov2500]

- id: ce02
  title: Cirrus 4 Freemium 免费云管不能做网络配置，只能看不能改
  type: counter-example
  source_chapter: "p139"
  source_quote: |
    "Freemium: Self Registration; Free of charge; No device capacity limitation; No duration limitation; No network Configuration; On-time Network Device Upgrade; Restricted OV Cirrus capabilities; Can be upgraded to Premium"
  summary: |
    Freemium 账户免费、不限设备数、不限时长，但明确 "No network Configuration"（不能做网络配置）、只能一次性设备升级、云管能力受限。
    踩坑场景：售前为拿下订单向客户宣传"免费云管"，客户自行注册 Freemium 后发现改不了 SSID、推不了配置，设备升级也只支持一次性操作，现场直接翻脸。后果是被指虚假承诺，还得补 Premium 订阅预算。
    规避方法：把 Freemium 定位讲成"监控/试用入口"而非管理工具；客户需要远程改配置、批量升级就必须买 Premium 订阅（eBuy 下单 + Subscription Manager 建订阅 + 激活码导入，p142-148）。Freemium 可升级到 Premium，但升级前不能替代付费版做任何配置操作。
  tags: [license, freemium, cirrus4, cloud-management, expectation-management]

- id: ce03
  title: Base 服务包不含设备 TAC 与硬件更换服务（Cirrus 4 和 Cirrus 10 都是）
  type: counter-example
  source_chapter: "p141, p155"
  source_quote: |
    "Access to the TAC and technical assistance for the SaaS application OmniVista Cirrus – but not for the equipments ... TAC access for the equipments: Not Available (*) ... Node AVR-NBD service: Not Available ... *: Available to partners and end customers if a separate support contract has been purchased for the equipment under the Base license."
  summary: |
    Cirrus 4 的 Base 服务包只覆盖 SaaS 应用本身的 TAC 支持，不含设备的技术支持和 AVR-NBD（次日备件更换）硬件服务；Cirrus 10 的 Base 同样 "TAC access: Not Available"、"Hardware service (advanced replacement) and support: Not Available, sold separately"，且固件更新"Only software upgrade, limited to the available version in OVC10"（只能升 OVC10 内可用版本）。
    踩坑场景：为压总价给客户报 Base 级订阅，设备出故障后客户找 ALE TAC 被拒、无硬件备换，售后纠纷直接烧到售前。含糊承诺"订阅含服务"是最常见的翻车点。
    规避方法：Base 只适合"客户已有独立维保合同"的场景（p141 脚注明确要另购设备支持合同）；对依赖厂商售后的客户报 Business（面向合作伙伴）或 Premium（面向最终客户）级别，并把三级差异写进方案对比表。
  tags: [license, base-bundle, tac, hardware-service, support, cirrus4, cirrus10]

- id: ce04
  title: Cirrus 10 不覆盖 AP1101 / AP1201H / AP1201L / AP1201LH，交换机还必须跑 8.9R
  type: counter-example
  source_chapter: "p166"
  source_quote: |
    "Network devices • All OmniAccess Stellar Access Points models, except AP1101, AP1201H/L/LH • All Alcatel OmniSwitch models running in version 8.9Rx"
  summary: |
    Cirrus 10 的报价指引明确排除四款老 AP：AP1101、AP1201H、AP1201L、AP1201LH；OmniSwitch 侧还要求运行 8.9R 版本。
    踩坑场景：客户现网有上述老 AP 或旧版本交换机，售前按"全机型支持"报了 Cirrus 10 订阅，激活后这批设备根本无法被纳管，客户等于白买这部分 License。升级交换机 AOS 版本的工作量和风险也没进报价。
    规避方法：做 Cirrus 10 报价前先盘点存量设备清单，老 AP 留在原有平台管理或规划换机，交换机版本先升到 8.9R 再买订阅；把"不支持机型清单"作为报价前置检查项。
  tags: [license, cirrus10, ap1101, ap1201, compatibility, legacy]

- id: ce05
  title: Express 集群 255 台硬上限，第 256 台静默卡在 joining 不报错
  type: counter-example
  source_chapter: "p46, p48"
  source_quote: |
    "A Group can not contain more than 255 APs. The 256th AP is not taken into account. Will stay in 'joining' mode. To have more than 255 APs on a network it is necessary to configure several Group-ids or to configure two separate VLANs"
  summary: |
    Express 模式一个 AP-Group 硬上限 255 台；超出时第 256 台不会报错，而是永远停在 "joining" 状态不被纳管，只能拆多个 Group-ID 或分 VLAN 部署。
    踩坑场景：SMB 客户扩容到 256 台以上，新装的 AP 全部"上线失败"，现场排查很久才发现是集群上限。另外集群超过 64 台时书里明确要求做网络冗余设计：每台 OmniSwitch 最多接 32 台 AP、每个堆叠最多 64 台、每个堆叠里至少放 2 台可当 PVM/SVM 的 AP（p48）。
    规避方法：售前做容量规划时把 255 / 64 当作两道红线；超过就设计多集群（独立管理域+射频域）或直接转 Enterprise/Cloud 模式。
  tags: [express, sizing, cluster, scaling, deployment]

- id: ce06
  title: Express 转 Enterprise 要恢复出厂且集群配置全部丢失（"Easy conversion"有水分）
  type: counter-example
  source_chapter: "p66, p84"
  source_quote: |
    "AP Mode is hard coded at first boot: Mode can not be changed. Requires a factory reset (push button) and reboot. Migration from existing Express to Enterprise mode ... Perform a factory reset/reboot. No configuration migration, AP 'cluster' configuration is lost"
  summary: |
    AP 出厂默认 Express，模式在首次启动时固化，之后不能在线切换；要迁到 Enterprise 必须加载新软件、加 DHCP option 138、恢复出厂并重启，且"集群配置不做迁移、全部丢失"。而 p84 的卖点页却写着 "Easy conversion of Express AP to Enterprise AP"。
    踩坑场景：客户先用 Express 跑了一两年，SSID/认证/ACL 全在集群里，转 Enterprise 时才发现所有配置要手工重做一遍，停机窗口和工作量远超预期。售前如果只背了 p84 的"轻松转换"话术，就会当场被打脸。
    规避方法：把"可从 Express 成长到 Enterprise"讲成路径可行但要重建配置；迁移项目单独报实施工作量（配置重做+停机窗口），别混在"免费升级"叙事里。
  tags: [express, enterprise, migration, config-loss, factory-reset, expectation-management]

- id: ce07
  title: Express 远程集群管理的能力例外：不能远程升级 AP 组镜像
  type: counter-example
  source_chapter: "p82"
  source_quote: |
    "AP Group can be managed remotely (opening the Firewall settings for AP Group Management IP). All operations supported. Except AP Group image upgrade"
  summary: |
    Express 模式支持通过 Group Management IP 远程管理 AP 组（需在防火墙放通），但明确排除"AP 组镜像升级"这一项。
    踩坑场景：连锁零售/多分支客户用 Express 远程运维，到了全网固件升级时才发现远程做不了镜像升级，只能派人到每个站点，或临时改用其他方式。此外远程管理还依赖防火墙放行管理 IP，安全部门未必配合。
    规避方法：有定期固件升级诉求的客户，售前阶段就说明该例外并给出选项（现场升级 / 转 Enterprise 或 Cloud 模式获得集中镜像管理能力，p53"Centralized Image Upgrade"）。
  tags: [express, remote-management, firmware-upgrade, limitation]

- id: ce08
  title: AP 注册失败三条件（未信任/无 License/国家码不匹配）导致射频全关，且默认要手动 Trust
  type: counter-example
  source_chapter: "p68, p69"
  source_quote: |
    "AP is unmanaged when Registration fails: AP is not Trusted; AP is not Licensed; Country Code does not match the Country Code from the RF Profile ... Configuration not applied, All Radios are off. ... By default, new APs are not automatically registered and require a 'Trust' action in the registration tool (UnManaged AP section)"
  summary: |
    AP 想被 OV2500 纳管必须同时满足三个条件：已信任、有 License、国家码与 RF Profile 一致；任一不满足即注册失败，配置不下发、所有射频关闭。且默认策略是新 AP 不会自动注册，必须管理员在 UnManaged 区手动做 "Trust" 操作（手工创建/Excel 导入的 AP 视为已信任）。
    踩坑场景：批量开局时 AP 上电却"全部没信号"，工程师先怀疑硬件和供电，绕一大圈才发现是没点 Trust、License 没买够或 RF Profile 国家码设错。跨国项目（如 ME/JP 区域码设备，p136）尤其容易踩国家码。
    规避方法：开局手册里把"License 数量盘点 → Trust 动作 → 国家码核对"列为前三步；跨国订单先核对设备 Region 后缀与 RF Profile 国家码。
  tags: [deployment, ap-registration, country-code, license, troubleshooting]

- id: ce09
  title: Zigbee IoT 方案的机型例外：AP1301 和 AP1230 系列不支持
  type: counter-example
  source_chapter: "p98"
  source_quote: |
    "Zigbee ... Aim: Manage the Zigbee endpoints from the OmniVista ... Compatible Stellar APs: All models, except AP1301 and AP1230 series"
  summary: |
    通过 AP 内置 Zigbee 电台做 IoT 管理（如酒店数字门锁集中管理）时，兼容机型"除 AP1301 和 AP1230 系列外全部"，这两款恰好是入门 Wi-Fi 6 和 Wi-Fi 5 老机型。
    踩坑场景：酒店/医疗客户要上 Zigbee 门锁或楼宇自动化，售前按入门价报了 AP1301，签约后发现这批 AP 干不了 Zigbee，要么补 dongle 要么换机型，直接侵蚀利润。
    规避方法：IoT 需求入场时就筛掉 AP1301/AP1230，改推 AP1311 及以上带 BLE5.1/ZigBee 的机型（p18 起）；把"机型×IoT 协议兼容表"放进方案附录。
  tags: [iot, zigbee, ap1301, ap1230, compatibility, hospitality]

- id: ce10
  title: 老机型能力例外集中清单：AP1101 不支持 RAP，AP1101/AP1201/AP1201H 桥接不支持 VLAN 标签
  type: counter-example
  source_chapter: "p99, p110"
  source_quote: |
    "Prerequisites: Stellar AP models: ALL except AP1101; Stellar AP version: 4.0.0 and above; OmniVista Cirrus: 4.5.1 and above ... * AP1101, AP1201 & AP1201H are not compatible with VLAN tagging over a bridge. ... Cannot provide service (WiFi) to WiFi clients"
  summary: |
    两处老机型例外容易在方案里漏查：远程接入点（RAP，居家办公/小微分支场景）要求 AP 版本 4.0.0+、网管 4.5.1+，且 AP1101 不支持；Wi-Fi 桥接场景下 AP1101、AP1201、AP1201H 不支持在桥上打 VLAN 标签，流量无法隔离开。另外 Wi-Fi Bridge 本身"不能给 WiFi 客户端提供服务"，选错形态（该用 Mesh 却用 Bridge）会导致客户端无法接入。
    踩坑场景：客户用老 AP1101 做家庭办公 RAP 拉不起来；两地楼宇桥接后 VLAN 隔离失效，安全审查不过。
    规避方法：涉及 RAP/桥接的项目先做机型与软件版本双核对；桥上要 VLAN 隔离就避开三款老机型；需要同时回传和覆盖客户端时选 Mesh 而非 Bridge。
  tags: [rap, wifi-bridge, ap1101, ap1201, vlan, compatibility, versioning]

- id: ce11
  title: Mesh 组网硬上限：16 台 AP / 8 从节点 / 4 跳，且只能广播 5 个 SSID
  type: counter-example
  source_chapter: "p112"
  source_quote: |
    "WIFI MESH – LIMITATIONS • UP TO 8 SLAVE APS • UP TO 4 HOPS • UP TO 5 APS IN A SINGLE HOP IN A PEER TO MULTI PEER CONNECTION • UP TO 16 APS IN THE MESH NETWORK • ALL APS CAN BROADCAST UP TO 5 SSIDS FOR CLIENTS"
  summary: |
    Mesh 拓扑有四道规模红线：从节点最多 8 台、跳数最多 4 跳、单跳对多点连接最多 5 台、整个 Mesh 网最多 16 台 AP；而且 Mesh 内 AP 只能对外广播最多 5 个 SSID。
    踩坑场景：营地/仓库/码头客户想靠 Mesh 链式延伸覆盖，规模一超 16 台或层级超 4 跳就组不起来；企业多 SSID 规划（员工/访客/IoT/语音等超过 5 个）在 Mesh 节点上放不下。
    规避方法：大范围无布线场景优先做点位设计（立杆+室外 AP1361）而不是无限 Mesh；确实要 Mesh 就按 16 台/4 跳/5 SSID 做预算切分，并把最佳实践带上：5GHz 建链、信道选 100 以上（Wi-Fi 6E 可用 6GHz）。
  tags: [mesh, sizing, limitation, outdoor, ssid]

- id: ce12
  title: 快速漫游协议矩阵：OKC 只支持 WPA2-Enterprise，选错认证方式漫游必卡
  type: counter-example
  source_chapter: "p89"
  source_quote: |
    "Fast Roaming supported: OKC for WPA2 Enterprise only; 802.11r for WPA2 Personal and Enterprise"
  summary: |
    两种快速漫游机制的适用面不同：OKC（机会性密钥缓存）仅限 WPA2-Enterprise；802.11r 对 WPA2 Personal 和 Enterprise 都支持。
    踩坑场景：语音或移动扫描枪项目用了 WPA2-Personal（PSK）认证，方案里写了"启用 OKC 保障漫游"，实际该组合不受支持，终端漫游时重认证延迟明显，通话掉字、扫码中断。反向坑：部分老终端不支持 802.11r，开了 11r 反而连不上。
    规避方法：按认证方式选漫游机制（Enterprise 可 OKC 或 11r，Personal 只能 11r）；上 11r 前核对终端驱动支持情况，必要时分 SSID 隔离老终端。
  tags: [roaming, okc, 802.11r, wpa2, vowlan, compatibility]

- id: ce13
  title: Guest 隧道有硬数量上限：每 AP 16 条、6860/E 终结 750 条、6900 终结 1000 条
  type: counter-example
  source_chapter: "p115"
  source_quote: |
    "Max 16 tunnel starts per AP; 6860/E →750 tunnel terminations; 6900 →1000 tunnel termination"
  summary: |
    访客流量隧道（L2 GRE，从 AP 到 OS6860/E 或 OS6900 交换机终结）有三层容量上限：单 AP 最多发起 16 条隧道、一台 6860/E 最多终结 750 条、一台 6900 最多 1000 条。
    踩坑场景：大学/园区项目把几千台 AP 的 Guest 流量都指到一两台核心交换机终结，超限后新隧道建不起来，访客网局部瘫痪；或单 AP 上按角色拆了太多隧道（每 Access Role Profile 一条）撞 16 条上限。
    规避方法：设计阶段按"AP 数 × 每角色隧道数"核算两端容量，必要时多台交换机分摊终结、或收缩隧道化的角色数量。
  tags: [guest-access, tunneling, gre, capacity, design]

- id: ce14
  title: Web 内容过滤 License 按 10 台 AP 一份起卖，零头也要整份买
  type: counter-example
  source_chapter: "p131"
  source_quote: |
    "Web Content Filtering License - OV-AP-WCF • Web Content Filtering feature • One license for 10 Access Points"
  summary: |
    OV2500 的网页内容过滤（WCF，基于 DNS 嗅探 + Brightcloud 分类）License 粒度是"一份覆盖 10 台 AP"，且该功能依赖 OmniVista 平台（p90），不是 AP 单机能力。
    踩坑场景：客户 12 台 AP 只要了 1 份 WCF License，激活后 2 台 AP 无过滤能力，策略不一致被安全部门质疑；或 Express 模式客户以为买了 License 就能用 WCF，实际没有 OV 平台根本跑不起来。
    规避方法：报价按 ceil(AP 数/10) 向上取整买 WCF License；Express 客户要用 WCF 必须先转 Enterprise/Cloud 模式，把平台前置条件写进方案。
  tags: [license, wcf, web-filtering, ov2500, granularity]

- id: ce15
  title: WPA3-Enterprise 开 CNSA 模式后只放 WPA3 客户端，老终端直接被拒
  type: counter-example
  source_chapter: "p105"
  source_quote: |
    "Optional 192-bit security mode (CNSA option): CNSA enabled: Only wpa3 client authorized on the SSID; CNSA disabled: wpa2 or wpa3 clients authorized on the SSID"
  summary: |
    WPA3-Enterprise 的 CNSA（192 位国密级安全）选项一旦开启，该 SSID 只允许 WPA3 客户端接入；关闭时 WPA2 和 WPA3 客户端都能入网。
    踩坑场景：为满足高安全合规开启 CNSA，结果仓库里一批只支持 WPA2 的老旧扫码枪/打印机全部掉线，业务停摆。
    规避方法：开 CNSA 前做终端无线能力盘点；新老终端混跑就保持 CNSA 关闭（WPA2/WPA3 混合），或为老终端单独开一个过渡 SSID 并排期淘汰。
  tags: [security, wpa3, cnsa, legacy-clients, compatibility]

- id: ce16
  title: Enterprise 模式下 AP 管理面只走 IPv4，没有 IPv6 管理接口（Express 反而支持）
  type: counter-example
  source_chapter: "p107"
  source_quote: |
    "AP Management through IPv4 • IPv4 for AP/OmniVista communication • No IPv6 network interface on AP • DPI support for IPv6 clients"
  summary: |
    Enterprise 模式里 AP 与 OmniVista 之间的管理通信只走 IPv4，AP 没有 IPv6 网络接口；客户端侧的 IPv6 流量、认证、Portal 都支持， Radius/UPAM 之间也是 IPv4。而 Express 模式反而支持 AP 管理接口拿 IPv6 地址（p106，SLAAC+DHCPv6）。
    踩坑场景：IPv6-only 或双栈优先的数据中心客户，装 Enterprise 模式时发现管理面拉不起来，被迫为 AP 管理单独维护一套 IPv4 网络，与客户"去 IPv4"战略冲突。
    规避方法：方案评审时核对客户管理网地址族；纯 IPv6 管理诉求要么走 Express 模式，要么在标书应答里如实写"管理面需 IPv4"，不要硬应标。
  tags: [ipv6, enterprise-mode, ap-management, limitation]

- id: ce17
  title: 五星酒店用例：装后 Ekahau 审计发现信道重叠与局部低带宽，靠缩信道宽度补救
  type: counter-example
  source_chapter: "p178"
  source_quote: |
    "Post-installation audit performed by the business partner with Ekahau: good results globally but low bandwidth in specific areas. Channels overlap issue, solved by reducing the channel width of these APs. Precautions to be taken in the server room (plaster dust)"
  summary: |
    酒店案例是全书唯一一个"装完才发现问题"的复盘：整体结果好，但局部区域带宽低，Ekahau 审计定位为信道重叠，最终靠"缩小这些 AP 的信道宽度"（如 5GHz 降到 20/40MHz）解决。案例还附了一句环境提醒：机房要防石膏粉尘。
    踩坑场景：高密度同质环境（酒店客房走廊、每房一 AP）里 AP 间距小、互相可见，默认信道宽度下同频干扰严重，客户感知"新网不如旧网快"。这类问题验收阶段才暴露，整改要返工 RF 参数。
    规避方法：把装后审计（Ekahau/AirMagnet）写进交付标准；高密度区域主动预配窄信道（酒店客房场景推荐 HT20，p247）；施工环境风险（粉尘、吊顶工艺）提前与装修方交底。
  tags: [hospitality, rf-design, channel-width, interference, ekahau, post-install-audit]

- id: ce18
  title: 轮渡用例：金属船体影响覆盖，装前勘察推翻原 AP 数量规划被迫加量
  type: counter-example
  source_chapter: "p188, p190"
  source_quote: |
    "The metallic structure of the ferry impacts the radio coverage. ... Pre-installation audit performed by ALE ProServ with Ekahau: good results globally. Stellar APs placement has been optimized due to the metallic structure of the ferry. Increased number of outdoor AP1251 required to cover all parts of the bridge."
  summary: |
    轮渡船队案例的挑战页就写明"金属结构影响射频覆盖"，技术描述页进一步承认：装前 Ekahau 勘察后 AP 摆位被重新优化，且甲板覆盖所需的室外 AP1251 数量比原计划增加。
    踩坑场景：金属密集环境（船体、厂房、仓储货架）按普通室内经验做链路预算和 AP 数量估算，信号衰减远超预期，签约价覆盖不了实际用量，项目亏损或覆盖不达标。
    规避方法：金属环境必须在报价前做现场勘察（该案例由 ALE 专业服务执行），AP 数量留余量或写明"以勘察结果为准"的调价条款；甲方/船厂结构图纸要拿到手。
  tags: [transportation, rf-survey, metallic-environment, ap-count, scope-risk]

- id: ce19
  title: 承重墙衰减 30dB：隔房部署在 5GHz 直接无信号，必须每房一台 AP
  type: counter-example
  source_chapter: "p243, p245, p260"
  source_quote: |
    "Load-bearing wall signal attenuation = 30 dBm. Worst case: 5GHz signal in area in the room without AP = -80 dBm →No access; 2.4GHz signal in area in the room without AP = -70 dBm →Extremely poor. AP installation: 1 access point per room"
  summary: |
    酒店客房部署指引给出硬数据：普通墙衰减 15dB（可隔房部署、信号最差 -65dBm 可用），承重墙衰减 30dB——隔房时 5GHz 跌到 -80dBm"无法接入"、2.4GHz -70dBm"极差"，结论是承重墙场景必须每房一台 AP。数量公式为 AP 数 = M/2+N+(M+N)*5%（M 普通墙房间数、N 承重墙房间数）。墙装还有禁忌：装太低或贴承重墙侧面会导致信号快速衰减（p260）。
    踩坑场景：售前不区分墙体类型，按"隔房一台"报低价，实际楼宇全是承重墙，AP 用量翻倍，预算和工期双爆。
    规避方法：勘察阶段逐层标注承重墙位置；报价按公式分档（普通墙/承重墙两套数量）；安装规范写明墙装高度 1.5 米以上、避开电视/金属柜等遮挡（p246）。
  tags: [deployment, hospitality, load-bearing-wall, attenuation, ap-count, rf-design]

- id: ce20
  title: 软终端语音质量随终端硬件/操作系统浮动，802.11v 漫游辅助要三星 S9 起步
  type: counter-example
  source_chapter: "p203"
  source_quote: |
    "Roaming assistance with 802.11r/k/v protocols • iOS 8 and above • Samsung Galaxy S7 minimum • S9 minimum for 802.11v. Voice over WLAN quality may vary depending on the hardware/Operating System of the device on which the voice application is installed"
  summary: |
    书里明示：装在手机/笔记本上的语音应用（Rainbow 等软终端）通话质量"取决于设备硬件和操作系统"，不是网络好就一定好；终端门槛还分档——iOS 8 起、三星 S7 起步，而 802.11v 漫游辅助要 S9 以上。
    踩坑场景：客户拿员工的一批旧安卓机跑 Rainbow 软电话，投诉"无线语音断续"，网络侧查无问题，根因是终端太老（不支持 11v 甚至性能不足），责任扯皮扯到售前头上。
    规避方法：VoWLAN 方案里加一页"终端准入清单"：固话选 8118/8128/8158s/8168s（p202），软终端明确机型/OS 下限；旧终端要么升级要么不承诺语音体验。
  tags: [vowlan, softphone, rainbow, endpoint-requirements, 802.11v, roaming]

- id: ce21
  title: Network Advisor 的隐性成本与门槛：虚拟机自购、版本下限、2000 设备上限、License 激活即倒计时
  type: counter-example
  source_chapter: "p230, p232, p233"
  source_quote: |
    "OS 6xxx and 9xxx models, AOS 8.7.R2 or Higher ... OS 2xxx models, AOS 5.2.R1 or Higher ... Stellar APs, AWOS 4.0.3 MR-3 or Higher ... Virtual Appliance to be acquired separately (not sold by ALE) ... License duration start decreasing as soon as they have been activated. A 30 days grace period is attached ... Limits: 2000 Network devices"
  summary: |
    AI 运维伴侣 Network Advisor 有四类隐性约束：其一，边缘计算虚拟机（四核/8GB/50GB）要客户自购，ALE 不卖；其二，设备版本门槛——OmniSwitch 6xxx/9xxx 要 AOS 8.7.R2+、2xxx 要 5.2.R1+、Stellar AP 要 AWOS 4.0.3 MR-3+，现网老旧版本先升级才能纳管；其三，整套系统上限 2000 台网络设备；其四，License 时长从"激活那一刻"就开始倒计时，只有 30 天宽限期。
    踩坑场景：按目录价（AP 50 美元/年等，p231，且书里注明是 List Price 无区域折扣）报了价，交付时才发现还要客户自备服务器、先升级一批交换机；License 提前激活囤着，没上线就白白烧掉订阅期。
    规避方法：报价附"版本核对+虚拟机规格+激活时机"三张检查单；License 在客户上线节点再激活；超 2000 台的规模不推此方案。
  tags: [network-advisor, hidden-cost, versioning, license-lifecycle, list-price, limitation]

- id: ce22
  title: 推荐配置里的功能依赖冲突：关 BG-S 就没有 WIPS/APC/快速漫游，开 ATF 伤及无 AP 房间
  type: counter-example
  source_chapter: "p247, p252, p261"
  source_quote: |
    "BG-S Disable: It is recommended that this feature be disabled unless there are special requirements for WIPS\ APC\fast roaming. ... ATF Disable: May reduce the user experience in hospitality rooms where there is no AP installed."
  summary: |
    三套场景化推荐配置（酒店客房/高密度场馆/中小会议室）都建议关闭 BG-S（后台扫描），但附带条件是"除非有 WIPS、APC、快速漫游的特殊需求"；BG-S 一关，Voice/Video awareness 也随之不可用（配置表里明确"Is not applicable as BG-S had been disabled"）。另外酒店客房场景建议关 ATF，理由是"会降低没有安装 AP 的房间的用户体验"。
    踩坑场景：照抄推荐配置模板上线，之后客户要加无线入侵防护（WIPS）或语音快速漫游，发现底层扫描已被关掉，功能全失效，来回改参数引发新的性能问题。
    规避方法：把推荐配置当"性能优先基线"而非万能模板；客户有安全/语音诉求时改用开启 BG-S 的配置档，并同步说明吞吐损失；ATF 只在"每房都有 AP"的格局下才考虑开启。
  tags: [configuration, bg-s, atf, wips, fast-roaming, feature-dependency, trade-off]

- id: ce23
  title: 教材时代局限与自相矛盾：2025 Ed28 数据、目录价无折扣、只讲赢单不讲翻车、个别参数前后打架
  type: counter-example
  source_chapter: "p243 (对照 p17/p95), p231, p37"
  source_quote: |
    "AP1301H: 2.4GHz and 5GHz dual radio frequency. 802.11ac. Up to 1024 clients."
  summary: |
    引用本书数据时要挂"时效验证"标签：一，书中自相矛盾处——p243 把 AP1301H 写成"802.11ac"，与 p17 硬件章"802.11ax (Wi-Fi 6)"冲突；p95 BLE 兼容清单出现不存在的机型"AP1421"（产品线里只有 AP1521），照抄进标书会出硬伤。二，时代局限——Ed28 为 2025-02 版（Wi-Fi 7 标注 2024 年商用，p37），AP 矩阵、价格与 License 规则随产品线演进很快过期。三，覆盖盲点——Network Advisor 只给美元/欧元目录价且注明"All are in List Prices"，区域折扣只字未提；六个行业用例全是赢单复盘，没有落选或翻车案例可参考风险；Wi-Fi 7（AP1511/AP1521）内容浅，无与 Cisco Catalyst 9130 等竞品的对比数据（BOOK_OVERVIEW 批判章节同此判断）。
    规避方法：投标前用 MyPortal 的 WPL（价格表）和产品线矩阵复核 part number、价格、机型在售状态；竞品对比与折扣体系另行索取最新材料，不引用本书；书内参数冲突时以硬件规格页（p15-27）和官方数据表为准。
  tags: [book-limitation, data-accuracy, typo, list-price, wi-fi7, competitor-gap, ed28]
```
