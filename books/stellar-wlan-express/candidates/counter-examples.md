# 陷阱/警告 · OmniAccess Stellar WLAN Express (DT00XTE455EN)

> 来源：source/fulltext.md（页码即教材 PDF 页码）。Express 模式的规模陷阱、Mesh/Bridge 限制、Portal 行为例外与勘测常见错误。

- id: ce01
  title: 陷阱：第 256 台 AP 静默失效——不停 joining、不被纳管
  type: counter-example
  source_chapter: "p81"
  source_quote: |
    "A Group can not contain more than 255 APs. The 256th AP is not taken into account and will stay in 'joining' mode."
  summary: |
    超过 255 台后不会有任何报错提示：第 256 台 AP 就是不被接管，一直卡在 joining 状态。现场表现是"新装的 AP 灯正常、就是进不了集群"，很容易被误判为网络或配置问题。规避：规划期按 255 分域（多 Group ID 或多 VLAN）；排障期看到 joining 卡死先数集群规模，再查 Group ID 与子网。

  tags: [255-limit, joining-state, silent-failure, cluster-sizing]

- id: ce02
  title: 陷阱：跨集群漫游落空——L2/L3 都不支持
  type: counter-example
  source_chapter: "p81"
  source_quote: |
    "Limitations: No Layer 3 Roaming. No Layer 2 Roaming between clusters."
  summary: |
    用多个集群拆分超 255 台网络时容易踩的坑：终端在两个集群覆盖交界处移动，二层、三层漫游都不会发生，必然掉线重连。仓库搬运、医院移动查房这类跨区移动场景，把漫游期望写进多集群设计就会翻车。规避：移动连续的区域划进同一集群，集群边界放在低移动区域。

  tags: [no-roaming, cluster-boundary, l2-l3, mobility]

- id: ce03
  title: 兼容性警告：AP1101/AP1201/AP1201H 桥接不支持 VLAN 标签
  type: counter-example
  source_chapter: "p112"
  source_quote: |
    "* AP1101, AP1201 & AP1201H are not compatible with VLAN tagging over a bridge."
  summary: |
    教材脚注明确列出的型号兼容性限制：AP1101、AP1201、AP1201H 三款在做 WiFi Bridge 时不能携带 VLAN 标签（VLANs can be used over the bridge 的星号例外）。在这些型号上规划"桥接链路跑多 VLAN 隔离流量"会失败。规避：桥接场景选支持 VLAN tagging 的型号（如 AP1321/1322 级别及以上），或改用 Mesh（其 VLAN 分离走的是 SSID 侧）。

  tags: [vlan-tagging, bridge, ap1101, ap1201, compatibility]

- id: ce04
  title: 误用警告：拿 WiFi Bridge 当覆盖用——桥上不能服务客户端
  type: counter-example
  source_chapter: "p112"
  source_quote: |
    "WIFI BRIDGE PROPERTIES: Cannot provide service (WiFi) to WiFi clients. WIFI MESH PROPERTIES: Can provide service (WiFi) to WiFi clients."
  summary: |
    Bridge 与 Mesh 的本质区别被忽略时的经典误用：Bridge 是纯回程链路，两端的 AP 在桥接 SSID 上不为任何 WiFi 客户端提供服务；需要同时给终端供网就必须用 Mesh（或另建业务 SSID 走有线）。把 Bridge 当"顺手放个 WiFi"用，客户端根本搜不到服务。判断口诀：只连线选 Bridge，要覆盖选 Mesh。

  tags: [bridge-vs-mesh, no-client-service, misuse]

- id: ce05
  title: 限制清单：Mesh 网络四条硬上限（4 跳/单跳 5 台/全网 16 台/仅 5 个 SSID）
  type: counter-example
  source_chapter: "p114"
  source_quote: |
    "WIFI MESH – LIMITATIONS: UP TO 4 HOPS. UP TO 5 APS IN A SINGLE HOP IN A PEER TO MULTI PEER CONNECTION. UP TO 16 APS IN THE MESH NETWORK. ALL APS CAN BROADCAST UP TO 5 SSIDS FOR CLIENTS."
  summary: |
    Express Mesh 的规模红线一次列全：链路最多 4 跳；点对多点连接里单跳最多 5 台 AP；整个 Mesh 网络最多 16 台 AP；每个节点对客户端最多广播 5 个 SSID。大型仓储/园区想靠 Mesh 无限级联会直接撞墙。规避：超过 16 节点就回有线/光纤拉接入点，Mesh 只做最后几跳的延伸；跳数控制在 4 跳内保时延。

  tags: [mesh-limits, 4-hops, 16-aps, 5-ssids, mesh-planning]

- id: ce06
  title: 行为例外：客户端访问 https URL 不会被重定向到内置 Portal
  type: counter-example
  source_chapter: "p143"
  source_quote: |
    "Check if the client enters https URL. If so, enter a http URL because the https redirect for captive portal web page is not yet supported."
  summary: |
    内置 Captive Portal 的已知行为限制：不支持对 https 请求做重定向。访客连上 Guest SSID 后默认打开的往往是 https 首页，结果门户页永远不弹，被当成"Portal 坏了"。规避与处置：引导用户手动输入一个 http 网址（如 http://neverssl.com）触发跳转；这是产品当前版本限制，排障时排在白名单/walled garden 检查之后（p142-143 顺序）。

  tags: [captive-portal, https-redirect, guest-onboarding, known-limitation]

- id: ce07
  title: 行为例外：白名单/walled garden 命中的客户端不弹 Portal
  type: counter-example
  source_chapter: "p143"
  source_quote: |
    "Check if the client MAC address is in the white list or if the client IP is in the walled garden list. If one or both cases are true, the client cannot be redirected to the captive portal web page."
  summary: |
    内置 Portal 的"正常的不弹页"：客户端 MAC 在白名单、或客户端 IP 在 walled garden（围墙花园，允许不经认证访问的地址清单）里，命中任意一条就直接放行、不做重定向。这是设计行为，排障时先核对这两个清单，别把放行当故障；反过来也可利用它给打印机/POS 等哑设备开免认证通道。

  tags: [white-list, walled-garden, portal-bypass, by-design]

- id: ce08
  title: 管理边界：远程集群管理做不了 AP Group 镜像升级
  type: counter-example
  source_chapter: "p86"
  source_quote: |
    "All operations supported (except AP Group image upgrade)."
  summary: |
    远程集群管理的唯一例外操作：AP Group 级别的镜像/固件升级不支持远程执行。把全网升级计划安排成纯远程操作会卡在最后一步。规避：固件升级批次安排现场或通过本地管理通道执行，其余日常操作（配置、监控、维护）都可远程完成（前提是防火墙为 Group Management IP 放行）。

  tags: [remote-management, image-upgrade, exception, planning]

- id: ce09
  title: 排障清单：PoE 不供电的五个常见原因（线长超 100m 居首）
  type: counter-example
  source_chapter: "p157"
  source_quote: |
    "PoE is disabled on the Switch. Enable it first. The cable is too long. Replace it with a shorter cable, less than 100m. The crystal heads of the cable are not up to standard. Replace the cable. The PoE Switch does not meet the 802.3af or 802.3at standard. Change the PoE Switch. Swap the AP by another one in order to check if the issue is caused by the AP."
  summary: |
    AP 接 PoE 交换机不上电的五查清单：（1）交换机 PoE 功能没开——先开；（2）网线太长——换 100 米以内的短线；（3）水晶头做工不达标——整根换线；（4）交换机不符合 802.3af/at 标准——换交换机；（5）对调一台正常 AP 验证是否 AP 本身问题。施工侧最常见的是第 2、3 条：超长线与劣质水晶头。教材原文第 4 条写作"802.3af or 802.3af"，按上下文应为 802.3af/802.3at 笔误，引用时注意。

  tags: [poe, cable-100m, crystal-head, poe-standard, five-checks]

- id: ce10
  title: 部署错误：AP 装在障碍物正前方，墙后出现死角
  type: counter-example
  source_chapter: "p167"
  source_quote: |
    "Access Point placement: bad location (wall, pillar). Placement of AP in front of obstructing object. Concrete wall. Dead zone. Add a new AP. Place an AP on both side of the obstructing wall."
  summary: |
    勘测章给出的头号布放错误：AP 正对混凝土墙/柱子安装，能量被遮挡，墙后整片死区（Dead zone）。两种修正：在遮挡墙两侧各放一台 AP；或在死区补一台新 AP。原则是 AP 别贴着障碍物正面装，勘测时优先标注这类"AP 在、信号无"的遮挡区。

  tags: [ap-placement, dead-zone, obstruction, concrete-wall]

- id: ce11
  title: 选型错误：天线类型与覆盖需求不匹配
  type: counter-example
  source_chapter: "p169"
  source_quote: |
    "Wrong type of antennas. Directional antenna: Small Area covered. Omnidirectional antenna: [Large] Area covered. Use the appropriate type of antenna based on the environment."
  summary: |
    信号问题四大根因之一（另三类：布放遮挡、环境衰减、干扰）：定向天线只覆盖一小片定向区域，全向天线覆盖周边大范围。长走廊用了全向（能量一半浪费在走廊外）、开阔办公区用了定向（覆盖扇区外没信号），都属于"设备正常、覆盖形状错"。规避：按环境覆盖形状选天线类型；需要异形覆盖时选可接外置天线的型号（尾数 2，见 p30）。

  tags: [antenna-mismatch, directional, omnidirectional, coverage-shape]

- id: ce12
  title: 射频陷阱：同频/邻频干扰——吞吐下降、丢包、数据损坏
  type: counter-example
  source_chapter: "p170"
  source_quote: |
    "Co-channel Interference. Adjacent channel Interference. Loss of throughput → Change AP channel. Packets loss. Corrupted data → Change AP channel."
  summary: |
    自己 AP 之间规划的信道互相打架：同频干扰（多 AP 同信道竞争空口）与邻频干扰（相邻信道部分重叠）。症状为吞吐损失、丢包、数据损坏。教材对策直接给动作：换信道。用 Ekahau（Windows）或 WiFi Analyzer（Android）在现场确认干扰类型后立即调整；设计期就应错开信道与收窄带宽（p22）。

  tags: [co-channel, adjacent-channel, interference, throughput-loss]

- id: ce13
  title: 账户陷阱：Portal 用户有效期过期即失效、从账户列表消失
  type: counter-example
  source_chapter: "p151"
  source_quote: |
    "Check if the valid period of the user account has expired. If so, the user account is invalid and shall disappear from the account list."
  summary: |
    内置用户数据库的访客账户带有效期：过期后账户立即失效，并从账户列表里消失。现场表现是"昨天还能上的访客今天 Portal 认证失败"，而运维在列表里已查不到该账户，容易误判为账号被删或系统故障。规避：给长期访客建账户时设足够有效期；排障顺序是先验账号密码、再查有效期、最后查 EAG 进程（ps | grep eag 及 eag.log）。

  tags: [account-expiry, portal-auth, user-database, case-9]

- id: ce14
  title: 容量陷阱：客户端数顶到 MaxClients 上限后拒绝新连接
  type: counter-example
  source_chapter: "p149"
  source_quote: |
    "Check if the clients count reached the maximum number of clients allowed. If the limit is already reached, modify the 'MaxClients' parameter."
  summary: |
    每 SSID/射频有最大客户端数（MaxClients）参数：在线数顶到上限后新客户端一律被拒，表现是"老用户都正常、新用户连不上"。这与密码错误、黑名单的表现混在一起，教材把它排在连接排障的第三查。规避：高密度场景（会议室、大堂）上线前按容量预算调大 MaxClients；排障时在 Web 上看当前在线数与上限的差距。

  tags: [maxclients, capacity, new-client-rejected, case-8]

- id: ce15
  title: 配置残留：AP 的 option proto 停在 static 导致拿不到 DHCP 地址
  type: counter-example
  source_chapter: "p131"
  source_quote: |
    "Check the IP mode of the AP ('option proto') using the command 'cat /etc/config/network'. If the 'option proto' is set to static, use the command 'ifconfig br-wan' to get the AP's IP address. Access the web GUI of the AP using this IP and modify the IP type to DHCP."
  summary: |
    AP 之前被手工配过静态 IP，之后再接入 DHCP 环境就永远拿不到地址——因为 option proto 还是 static，设备根本不发 DHCP 请求。Web 与 SSH 都进不去时只能走 Console（115200-8-N-1）：cat /etc/config/network 看 option proto，为 static 就用 ifconfig br-wan 读出现有 IP，借该 IP 进 Web 把 IP 类型改回 DHCP。教训：改过静态地址的设备入新网前先恢复 DHCP。

  tags: [static-ip, option-proto, dhcp-failure, console-rescue]
