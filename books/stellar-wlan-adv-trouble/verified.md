# 阶段 1.5 验证结果 · OmniAccess Stellar WLAN Advanced Troubleshooting (DT00XTE478EN)

> 验证日期：2026-08-23 · 验证器：cangjie-skill 流水线阶段 1.5
> 输入：candidates/（101 条）+ source/fulltext.md（187 页全文，逐条比对）
> 规则：V1 原文真实性（quote 在对应页命中）/ V2 可操作价值（排障命令、阈值、根因清单均算）/ V3 独特性（排障决策路径与 LED 判读表均算独特，仅"重启试试"级常识不过）；glossary 免验保留。

## 汇总

| 类型 | 候选 | 通过 | 淘汰 | 备注 |
|---|---|---|---|---|
| frameworks | 10 | 10 | 0 | 全部通过 |
| principles | 26 | 26 | 0 | 全部通过 |
| counter-examples | 30 | 30 | 0 | ce19 引文有一处日期笔误，保留但需修正（见附注 A） |
| glossary | 35 | 35（免验保留） | 0 | 未执行三重验证，按规则整体保留 |
| **合计** | **101** | **101** | **0** | 淘汰明细见 rejected/ 目录（各类型均无淘汰） |

淘汰为 0 的原因：候选集全部锚定到具体页码且带引文，抽查比对 66 条送验条目的 quote 均能在对应页命中实质内容；内容普遍含命令语法、阈值、判据或根因清单（V2 达标），且多为 Stellar/教材特有（V3 达标，仅有少数偏通用方法论条目，按"排障决策路径算独特"的口径保留，见附注 C）。

---

## 一、框架/排障流程（frameworks，10/10 通过）

- **f01 七步排障流程**（p10）
  V1：Identify/Locate/Isolate/Re-Create/Solve/Verify/Document 七步要点在 p10 逐段命中。V2：每步有明确动作与产出，含"无法复现即回第一步重新提问"的回退规则。V3：OSI 定层 + 复现回路是贯穿全书的主决策路径，非通用套话。
- **f02 WLAN 故障三域根因地图**（p5-8）
  V1：三域全部要素在 p5-8 逐项命中（含 DHCP 四参数、802.1X/RADIUS、LDAP/AD、互联网侧"不在网管员管控内"原句）。V2：接手故障前的根因覆盖清单，保证不漏层。V3：含 OmniVista、Stellar AP 等产品组件的分层地图。
- **f03 排障访谈四问定位法**（p17）
  V1：p17 表格四问、四答、四推断原文命中。V2：逐级收窄的提问脚本，每个答案直接决定下一问方向。V3："同位置受影响 → 排除全局 OmniVista 配置问题"等推断链是教材特有的推理路径。
- **f04 实验室复现法**（p12）
  V1：四类配置采集（vcboot.cfg / OmniVista 组织 / AP 配置备份 / 服务器备份）与两条 Re-create 原句在 p12 命中。V2：具体采集清单加 1:1 重建步骤。V3：vcboot.cfg 等产品特定文件名与"复现以排除隐藏根因"的用法。
- **f05 验证-记录-跟踪闭环**（p13-14）
  V1：先自测后进客户环境、Rainbow/voice/mail 稳定性验证、记录五字段、"方案永久且无副作用"在 p13-14 命中。V2：定义关单标准的操作清单。V3：沉淀到 ALE TKC 数据库的闭环为本书方法论特有。
- **f06 勘测类型选择矩阵**（p106-107）
  V1：三类勘测定义（p106）与阶段映射（p107）原句命中。V2：直接的选型决策规则。V3：Passive/Active/Predictive × 部署前后的能力边界矩阵。
- **f07 现场排障三步法**（p114-117）
  V1：Step 1 图纸三件事、Step 2 五项观察、Step 3 五类纠正动作在 p114-117 逐项命中。V2：现场作业清单与动作库。V3："移除低数据速率逼终端贴近好 AP"等纠正手段具体且常被忽略。
- **f08 TKC 用例检索与版本比对流程**（p127-130）
  V1：故障描述样例（p128）、版本比对三分支（p129）、结论复核与套用条件（p130）原句命中。V2：知识库排障的完整操作规程。V3：ALE TKC 专属流程，含"必须亲自重复诊断步骤、结论一致才套用"的硬性门槛。
- **f09 802.1X 认证失败三段排查法**（p88-90）
  V1：三段核对清单在 p88-90 逐项命中（客户端四查、AP 侧绑定与参数、服务器侧七查）。V2：按段排查的根因清单加顺序。V3：Radius station IP=Stellar AP 地址、防火墙放行认证/计费端口等核对点具体且非通用。
- **f10 分层排障路径**（p10, p38-102）
  V1：Isolate 定义（p10）与四大专项层章节起点 Basic p38 / Wireless p61 / Client p73 / Network p92 均在原文命中。V2：OSI 定层后进入对应专项层的导航决策。V3：书结构即决策树，"先低层后高层"避免误判为高层故障。

## 二、原则/参数（principles，26/26 通过）

- **p01 NTP 前置**（p22）：V1 p22 原句命中。V2 排障第零步核查项。V3 多设备日志对齐的具体理由（Error 10 时间错位演示）。
- **p02 AP 本地接入三通道**（p23-26）：V1 串口 115200 8N1、public_group.conf 的 ssh_connect、Web UI URL 与 Cirrus 开 "AP web" 在 p23-26 命中。V2 直接可用的连接参数与开关位置。V3 云管理模式必须先在 Provisioning Configuration 开 AP web 才能登录，产品特定坑。
- **p03 有线抓包 tcpdump 三步**（p30）：V1 p30 命中，br-wan 接口语义说明为原文。V2 完整命令语法（ssudo tcpdump -i br-wan -w …）加 SFTP 回传分析流程。V3 br-wan 为 AP 有线桥接口，产品特定。
- **p04 Air Capture 五要素与上限**（p31-32）：V1 五个操作要素与 "10MB or 5min" 警告在 p31 命中（p32 为云模式同流程）。V2 操作步骤加抓包预算硬限制。V3 TFTP 回传、MAC/帧类型过滤为产品特定。
- **p05 配置备份/恢复**（p33）：V1 p33 命中（Backup All Configuration、pub-config.tar、config-pub.tar）。V2 文件级操作步骤。V3 复现故障与技术支持工单共享的双用途为教材明示。
- **p06 LED 状态判读表**（p41-44）：V1 单三色 LED 六种状态（p41）、AP1201H PoE 橙灯三态（p42）、AP1251/AP1360 七 LED（p43-44）逐项命中。V2 免登录的第一道硬件体检表。V3 规则明示 LED 判读表算独特。
- **p07 support 账号与默认密码 aos2016**（p45-46）：V1 p46 登录块原样命中。V2 CLI 排障入口凭据与 Enterprise 自定义密码路径。V3 训练环境默认密码与 AP Group 激活 SSH 的流程产品特定。
- **p08 系统信息命令集**（p45-48）：V1 showsysinfo 输出（p45/p47）、showver 3.0.7.20、getmode 三态、show_cluster 表（p48）命中。V2 四条基础核查命令及输出解读。V3 getmode 的 CLUSTER/OV/OVNG 三态映射产品特定。
- **p09 意外重启核查**（p50）：V1 p50 原句命中。V2 date+uptime 两命令先钉住事实。V3 "时间不可信则日志定位无意义"的顺序纪律。
- **p10 CPU/内存/进程诊断**（p51-53）：V1 高 CPU 影响（p51）、R/S 正常与 X/Z 异常（p53）、工单附进程列表（p52）命中。V2 top/ps 判定标准与上报动作。V3 僵尸进程吃内存的 AP 视角判据（与 ce17/ce18 重叠，见附注 B）。
- **p11 Captive Portal 检查**（p55-56）：V1 eag_cli show user all 字段与三问清单（p55）、eag.log 三阶段（p56）命中。V2 命令加核对清单。V3 eag 进程族与 eag.log 为门户故障唯一权威日志源。
- **p12 Express 集群健康三查**（p58-59）：V1 PVC 查询（p58）、成员表与双 cluster_mgt 线程异常判定（p59）命中。V2 三条命令加异常判据。V3 "两个 cluster_mgt 线程=异常行为"是产品特定信号。
- **p13 iwconfig 与 athXYY 命名**（p63）：V1 p63 原句命中（含 "If there is no MAC address for Access Point, the SSID is not broadcasted"）。V2 四项核对加 BSSID 缺失判据。V3 athXYY 编码（0=2.4G、1=5G、2=6G、Y=SSID 1-16）产品特定。
- **p14 RF profile 落地核对**（p64）：V1 核对清单与 rfprofile.conf 字段样例（bandSteering/countryCode FR/channelWidth 20/signalStrengthThreshold 0）在 p64 命中。V2 配置路径加逐项比对清单。V3 字段名与 /tmp/config/ 路径产品特定。
- **p15 信道与功率核查**（p65）：V1 iwlist channel（57 信道、Channel 6）与 txpower 档位表（0-17dBm）在 p65 命中。V2 两条命令确认信道与功率档位。V3 档位表与"当前 Tx-Power=17dBm(50mW)"解读产品特定。
- **p16 VoWLAN 信号阈值**（p78-79）：V1 RSSI≥29（-67dBm）、SNR≥25 与三档判读（10=差 / 29=语音下限 / 43=完美）在 p78-79 命中。V2 明确可执行的阈值。V3 Stellar 正值 RSSI 刻度（dBm=RSSI 值-96）为厂商特有换算。
- **p17 客户端总表 sta_list**（p75）：V1 字段表（STA_MAC/IPv4/OnlineTime/RX/TX/AUTH/Final_role/VLANID 等）与核对清单在 p75 命中。V2 客户端排障第一条命令的六字段核对。V3 Final_role、TUNNELID 等字段语义产品特定。
- **p18 认证属性详查 wam_debug**（p77）：V1 p77 清单与 JSON 输出命中。V2 JSON 级认证结果核查方法。V3 assignedVLAN/macAuthResult/CPAuthResult/redirectURLFromMACAuth 等字段产品特定。
- **p19 空口信号与 OS 识别**（p76, p78）：V1 wlanconfig ath12 list 输出（SNR 57、HT/VHT Yes）与 kes_syslog grep tid 的 ostype 行在两页命中。V2 空口指标加终端 OS 识别两条命令。V3 TID_DHCP_PROTOCOL 行可识别 ostype/hostname，产品特定。
- **p20 关联/断连日志与 disassoc reason**（p80）：V1 p80 命中，reason 8 日志原样在页。V2 grep 客户端 MAC 加读 reason code 的方法。V3 reason 8=非激进负载均衡搬客户端，独家判读（与 ce21 重叠，见附注 B）。
- **p21 RADIUS 配置核对**（p89）：V1 AAA_server.conf（1812/1813/timeout 5/retries 2）、wlanservice.conf（Enterprise/wpa2-aes/aaaProfile）、AAA_profile.conf（primaryServer）在 p89 命中。V2 三份文件的核对点与默认值。V3 三文件绑定链产品特定。
- **p22 网络连通性四命令**（p94-95）：V1 ifconfig br-wan、route -n、ssudo ping/traceroute 在 p94-95 命中。V2 AP 视角的连通性分段排查组合。V3 ssudo 前缀、br-wan 接口与"逐个测网关/NTP/DHCP/DNS/防火墙/OmniVista"的产品语境。
- **p23 邻居 AP 判读 adme show**（p69, p96）：V1 表头字段（p69）与 RSSI<20 判定及两种处置（p96）命中。V2 命令加阈值加动作。V3 "地理邻居不可见或 RSSI<20 即漫游病灶"为产品判据（与 ce24 重叠，见附注 B）。
- **p24 时间与 DNS 配置核对**（p97）：V1 resolv.conf、/tmp/TZ=UTC+08（标注 Wrong time zone）、kes_syslog grep ntp（pool.ntp.org）在 p97 命中。V2 三条核查命令。V3 "时区错但时间同步正常仍致日志整体偏移"的排查项。
- **p25 syslog 不上报三步验证**（p101）：V1 syslog.conf（log_remote 1/IP/514）、ps 查 logread -f -r 进程、logger -p emerg 实测在 p101 命中。V2 三步分别排除配置错、进程挂、网络不通。V3 logread -f -r 进程核查产品特定（与 ce16 重叠，见附注 B）。
- **p26 OmniVista 接管网络前置**（p170, p179）：V1 防火墙端口 9093/30123-25、出向 443/80/123/53、DHCP 选项 1/2/6/28/42/43（代理加 129-133/138）、AWOS 4.0.6 GA+（Cirrus）/4.0.7.14+（Terra）在两页命中。V2 可直接执行的端口与选项清单。V3 不支持型号（AP1101、AP1201L/H/HL）与版本门槛为厂商硬前置。

## 三、失败模式/警告（counter-examples，30/30 通过）

- **ce01 主案例 VLAN 配错**（p11-13, p17-18）：V1 "Wifi client can not log into the SSID Employee"（p17）、VLAN 10/20 比对与 Root cause/Resolution（p18）命中。V2 根因加解决动作（更新 tagged VLAN ID=20）。V3 "全员连不上而 AP 本身正常 → 优先怀疑交换机侧 VLAN"是全书核心案例。
- **ce02 看不到 SSID 三根因**（p82）：V1 p82 三问与国家码处置原句命中。V2 有序根因清单加 RF profile 手动指定兼容信道的规避。V3 国家码不匹配表现为"别人看得到我看不到"。
- **ce03 热图生成不了**（p67-68）：V1 p67-68 原句命中。V2 iwconfig 查接口 → 查 WLAN 配置的排查路径。V3 "无 WLAN 配置即无接口即无热图"为产品机制。
- **ce04 漫游失败三根因**（p69）：V1 p69 三条原因原句命中。V2 漫游失败根因清单。V3 untagged 与 tagged VLAN 之间不漫游是产品限制。
- **ce05 射频互不可见的静态邻居**（p70）：V1 p70 原句与 Device Catalog > Neighbor APs > Manage neighbor 菜单路径命中。V2 对称静态添加邻居的操作路径。V3 直角走廊阻挡、客户端上下文改走 LAN 的解法独特。
- **ce06 漫游成功验证**（p71）：V1 wam.log 三类关键字原句命中。V2 start/success 关键字验证法（只有 start 无 success=漫游失败）。V3 L2/L3 漫游日志关键字产品特定。
- **ce07 拿不到 IP 之一：路径丢包**（p83）：V1 p83 原句与 tcpdump -i eth0 -s0 -w trace.pcap 命中。V2 客户端/AP 双端抓包比对 DHCP 四步交互。V3 双侧 pcap 对照定位丢失段的方法。
- **ce08 拿不到 IP 之二：VLAN/Final_role**（p84）：V1 p84 三问原句命中。V2 sta_list 查 VLANID 加 Final_role 是否过滤 DHCP。V3 认证角色滤掉 DHCP 导致永远拿不到地址，隐蔽根因。
- **ce09 频繁掉线之一：功率最小**（p85-86）：V1 Current Tx-Power=3dBm(1mW)、RSSI 16、Bad signal quality 原值命中。V2 症状 → 命令 → 阈值 → 修复的完整链。V3 功率被压到最小档的实际案例判读。
- **ce10 频繁掉线之二：踢除阈值过高**（p87）：V1 signalStrengthThreshold:70、"Threshold too high. Decrease the value." 与空口抓包兜底在 p87 命中。V2 阈值核查加 disassoc/deauth 抓包区分"被踢与失联"。V3 阈值 70（约 -26dBm）导致正常功率下也掉线的判定。
- **ce11 802.1X 客户端侧四查**（p88）：V1 p88 原句命中。V2 四项自查清单。V3 教材三段法第一段（与 f09 第一段同源，阶段 2 注意合并，见附注 B）。
- **ce12 802.1X AP 侧核对**（p89）：V1 p89 原句命中。V2 SSID 绑定服务器与 IP/端口/共享密钥一致性核对。V3 共享密钥不匹配的静默失败特征（与 p21 互补）。
- **ce13 802.1X 服务器侧七查**（p90）：V1 p90 七项原句命中。V2 服务器侧完整核对清单。V3 Radius station IP=Stellar AP 地址必须登记为合法客户端等具体项。
- **ce14 AP 拿不到 IP 之一：静态模式**（p99）：V1 p99 原句与 /etc/config/network 的 option proto 'dhcp' 命中。V2 proto 判定加两条切回 DHCP 的路径。V3 wan 接口 proto 字段判读。
- **ce15 AP 拿不到 IP 之二：DHCP-NAK 判据**（p100）：V1 p100 原句命中。V2 上联口抓包加"健康服务器至少回 NAK"的判据。V3 "连 NAK 都没有 = 报文未抵达服务器而非地址池问题"的推理独特。
- **ce16 syslog 不上报**（p101）：V1 p101 三步原句命中。V2 三步定位法。V3 与 p25 同页同法，跨类型重叠（阶段 2 二选一深化，见附注 B）。
- **ce17 高 CPU 四根因**（p52）：V1 四类原因与工单上报要求在 p52 命中。V2 top 定位元凶进程加开票附进程列表。V3 "过量日志/跟踪引发计算型高 CPU"的归因少见（drm 81% 示例在页）。
- **ce18 僵尸进程吃内存**（p53）：V1 p53 原句命中。V2 R/S/X/Z 判定标准。V3 与 p10 后半段重复（阶段 2 合并，见附注 B）。
- **ce19 无 NTP/时区错**（p22, p97）：V1 主体命中——No NTP server、Error 10 三设备日志块、/tmp/TZ=UTC+08、Wrong time zone 均在页；**但引文有一处日期笔误：AP Logs 首条应为 10/11/2019 08:15:30，候选误作 11/11/2019**（11/11/2019 12:09:34 是同页另一日志块），实质（多天错位破坏关联分析）无误，保留并要求阶段 2 修正（附注 A）。V2 排障前对时纪律的具体反例。V3 跨设备日志错位的 Error 10 演示。
- **ce20 意外重启先对时**（p50）：V1 p50 原句命中。V2 uptime+date 先定事实再翻日志。V3 与 p09 同页同法（重叠提示，见附注 B）。
- **ce21 reason 8 是负载均衡**（p80）：V1 p80 日志原样命中（recv rssi 63, min 55, max 64）。V2 reason code 定性掉线性质。V3 "系统主动搬客户端 ≠ 故障"的防误报警读（与 p20 重叠提示）。
- **ce22 门户重定向次序**（p56）：V1 p56 三阶段原句命中。V2 eag.log 按 IP 获取次序定位卡点。V3 "卡在 IP 未知阶段 = DHCP 未完成，先查地址获取而非门户本身"的排障次序。
- **ce23 双 cluster_mgt 线程异常**（p59）：V1 p59 原句命中。V2 进程数异常判据。V3 产品特定异常信号（与 p12 第三查重叠提示）。
- **ce24 邻居不可见或 RSSI<20**（p96）：V1 p96 原句命中。V2 阈值加两种处置（挪近或加大功率）。V3 漫游断连的前置病灶判读（与 p23 重叠提示）。
- **ce25 AP 正对遮挡物**（p109）：V1 p109 原句命中。V2 布点审查项与"遮挡墙两侧各布一台 AP"的解法。V3 照射阴影死区的勘测期发现项。
- **ce26 材料衰减清单**（p110）：V1 4 米 1-4 面墙 RSSI=-70dBm、Not enough for VoWLAN、七类材料清单在 p110 命中。V2 量化衰减数据加覆盖设计留裕量原则。V3 实测数值（-70dBm 不够语音，需 -67 以上）与材料清单。
- **ce27 天线类型选错**（p111）：V1 p111 命中；图例碎片 "No (20 meters) Area covered" 转写略乱但各词元均在页，语义（定向=小扇区、全向≈20 米整圆）忠实。V2 按环境选天线原则加末位"2"=可外接天线型号规则（p157 佐证）。V3 覆盖形状与空间形状匹配的判读角度。
- **ce28 同频/邻频干扰三症状**（p112）：V1 三症状与换信道处置在 p112 命中。V2 症状 → 处置（Change AP channel）的映射。V3 吞吐下降/丢包/数据损坏三联加勘测工具定位（Ekahau/WiFi Analyzer 在页）。
- **ce29 勘测五类发现**（p115-116）：V1 五项观察（p115）与 Default transmit power (17dBm)（p116）命中。V2 现场观察清单。V3 默认功率 17dBm 需按覆盖调大的实测提醒（与 f07 步骤二重叠提示）。
- **ce30 勘测纠正动作清单**（p117）：V1 五类动作在 p117 逐项命中。V2 可执行的纠正动作库。V3 "移除低数据速率逼终端贴近信号更好的 AP"是常被忽略的优化项（与 f07 步骤三重叠提示）。

## 四、术语表（glossary，35 条免验保留）

按规则不执行三重验证，整体保留（内容仍抽查过页码锚点，未发现页码错误）：

g01 RSSI · g02 SNR · g03 BSSID · g04 athXYY 接口命名 · g05 br-wan · g06 Band Steering · g07 Load Balance · g08 Air Time Fairness · g09 PVC · g10 Cluster · g11 getmode 三态 · g12 OmniVista Cirrus · g13 OmniVista Terra · g14 TKC · g15 UPAM · g16 Captive Portal · g17 eag 进程 · g18 WAM · g19 adme · g20 RADIUS/AAA · g21 802.1X/EAP · g22 DHCP-NAK · g23 PoE/PSE · g24 同频/邻频干扰 · g25 三类勘测 · g26 Heat Map · g27 L2/L3 Roaming · g28 Air Capture · g29 Ekahau · g30 Wireshark · g31 Access Role Profile/Final_role · g32 NTP · g33 僵尸进程 · g34 Monitor Mode · g35 Wi-Fi 代际

---

## 附注（供阶段 2 蒸馏参考）

**A. 引文修正项（1 处）**
- ce19：AP Logs 首条时间应为 **10/11/2019 08:15:30**（候选引文与摘要写作 11/11/2019；11/11/2019 12:09:34 属同页另一日志块）。摘要"相差四天"应随日期修正为"相差五天"（10 日 vs 15 日）或改引 11/11/2019 12:09:34 块并注明设备归属。修正后方可进入 skill 正文。

**B. 跨类型重叠组（8 组，阶段 2 合并 skill 时注意去重/分工）**
1. f09（三段法总纲）⊇ ce11 + ce12 + ce13（三段各自的展开）
2. p09 ≈ ce20（同为 p50 重启核查）
3. p25 ≈ ce16（同为 p101 syslog 三步）
4. p20 ≈ ce21（同为 p80 reason 8 判读）
5. p12（第三查）≈ ce23（p59 双 cluster_mgt）
6. p23 ≈ ce24（p96 邻居 RSSI<20）
7. p10（后半）⊇ ce17 + ce18（高 CPU 根因与进程状态）
8. f07（步骤二/三）⊇ ce29 + ce30（勘测发现与纠正动作）

建议：总纲类（f09/f07/p10）保留为流程骨架，细目类保留具体命令与阈值，正文合并时避免同一段引文出现两次。

**C. V3 边界条目（均按规则保留，理由备案）**
- f01/f05 为方法论层条目，单独看偏通用，但含"复现失败回退第一步""先自有环境测试再进客户环境""验证无副作用才关单"等教材特有决策规则，且规则明示"排障决策路径算独特"。
- p22（ifconfig/route/ping/traceroute）与 ce28（干扰换信道）所含单项知识偏通用网工常识，但均嵌在 Stellar 语境（ssudo、br-wan、Ekahau 勘测闭环）中，未达到"重启试试"级常识线，保留。
