# verified.md · 阶段 1.5 三重验证通过条目（OmniAccess Stellar WLAN Presales Ed28）

## 汇总

- **通过 140 / 淘汰 2**（候选共 142 条）
- 分类型：frameworks **20/21** · principles **34/35** · cases **18/18** · counter-examples **23/23** · glossary **45/45**（免验计入通过，45 个词条无重复，全部保留）
- 淘汰去向：`rejected/frameworks.md`（f19）、`rejected/principles.md`（p02）
- 验证口径：
  - **V1 原文真实性**：本次对四类共 97 条逐一做了 fulltext.md 原文比对（远超"每 5 条抽 2"下限），全部在标注页码找到实质对应；多处因原文换行导致的初次未命中，经逐页核对均确认存在。
  - **V2 预测力/可操作价值**：通过条目均可回答实际选型/报价/排障问题或直接指导售前行动（License part number 规则、容量常数、场景配置基线、案例话术等）。
  - **V3 独特性**：淘汰 2 条属"任何网工都知道"的常识（Wi-Fi 代际参数表、勘察二分法），其余条目含产品特有规则、常数或本书独有的场景数据。

## 原文笔误标注（相关条目保留，引用时须修正）

| 笔误位置 | 书内原文 | 影响 | 涉及条目 |
|---|---|---|---|
| p155 | "OmniVista Cirrus 10 Premium subscription level: **BAS** (ex: OVCX-xx-PRM-nY)" | Premium 级别缩写误写为 BAS，正确为 PRM（以编码示例 OVCX-xx-PRM-nY 为准） | f11、p24、ce01、ce03 |
| p243 | "AP1301H: 2.4GHz and 5GHz dual radio frequency. **802.11ac**. Up to 1024 clients." | AP1301H 误标 802.11ac，与 p17 硬件章（Wi-Fi 6 / 802.11ax）冲突，按 Wi-Fi 6 理解 | f20、p29、c18、ce19、ce23 |
| p95 | "AP1511 and **AP1421** (built-in)" | 产品线无 AP1421，应为 AP1521 | ce23（该条目已如实记录为书内错误） |

另注：f16 summary 中"内置 40+ 预置异常库（p220）"未获原文支持——p219-220 实际列出 17 个具名预置异常并注明"regularly updated"，引用时以"预置异常库（持续更新）"表述为宜。

## frameworks（20 条）

- **f01** AP 选型三维矩阵法（代际×形态×分层）——三维护 narrowing 选型结构配合本书独有机型档位（AP1301H/AP1361/AP1521），p11 lineup 核实无误。
- **f02** 网络管理模式三选一决策法——Express/Enterprise/Cloud 决策变量明确，"5 个免费 License 起步、可迁移"是报价判断的落点（p41 核实）。
- **f03** Express 集群容量与弹性设计法——255/64/32 三道容量红线是 SMB 方案答标与规模质疑的硬数据。
- **f04** Express→Enterprise 迁移四步法——option 138 + 恢复出厂 + 配置丢失风险，割接方案必备。
- **f05** AP 纳管三条件判定流——"AP 上线不上班"类排障的标准检查清单（p68 核实）。
- **f06** Bridge vs Mesh 二分选型法——单判据（是否给终端服务）+ 8/4/16 组网常数，无线回程选型可直答。
- **f07** License 三体系总览——模式与商务形态一一对应，"先锁模式再拼报价"的防错依据。
- **f08** OV2500 License 1+4 组合法——含 OV2500-NG-AP 等 part number 的报价结构，可分档取整。
- **f09** 报价四要素清单法——四格防漏项 + PW/SP 维保编码语法，自查报价单即用。
- **f10** Cirrus 4 Freemium→Premium 双轨法——免费起步/订阅变现叙事 + 附送额度数据，云管商务骨架。
- **f11** Cirrus 10 Part Number 三维语法法——7×3×3=63 编码可拼装（p153 核实），"知道型号+级别+年限即出编码"的防报错工具（注意 p155 笔误标注）。
- **f12** 云订阅三步激活流程——eBuy→Subscription Manager→云导入，可当实施交接清单（p158 核实）。
- **f13** 行业案例四段式论证法——Identity/Challenges/Why ALE?/Benefits 模板 + 反复出现的赢单理由（联合 POC、controllerless）话术库。
- **f14** VoWLAN 五步部署法——每步有明确输入输出物（布点图/配置模板等），可当项目 WBS 骨架。
- **f15** 无线语音容量工程常数法——255m²/AP、20-25 用户/AP、-62dBm 漫游阈值，无勘察数据时快速报量的底牌（p207 核实）。
- **f16** Network Advisor 三循环法——Identify/Mitigate/Optimize 价值叙事，可按客户痛点选切入循环（p227 核实；"40+ 异常数"表述见顶部标注）。
- **f17** 问题生命周期四阶段支撑法——按客户工作流时间轴摆产品能力，运维工具售前的差异化论证结构（p228 核实）。
- **f18** 无线需求识别五要素法——五问访谈提纲 + 场景→机型对照（p239 核实：Offices 500+/50% 并发/10G+ 上行→AP1231/13xx/14xx/15xx）。
- **f20** 客房 AP 密度计算法——M/2+N+(M+N)×5% 公式 + 15/30dB 墙体衰减分级 + 安装规范三件套（注意 p243 笔误标注）。
- **f21** 场景化配置基线表法——四场景同构"特性→推荐值→理由"表，同特性反值有据，可当交付验收 checklist。

## principles（34 条）

- **p01** 外接天线尾数"2"规则——AP1322/AP1362 命名速判，选型零成本检查（p32 核实）。
- **p03** Express PVM/SVM 选举与 255 上限——"最高型号+最高 MAC"选举规则 + mywifi-0102 默认 SSID。
- **p04** DHCP Option 138 模式开关——出厂 Express、有 138 即 Enterprise 的判定 + 配置丢失警告。
- **p05** AP 注册三条件——Trusted/Licensed/国家码与门，与 f05 互为清单/框架两用（p68/p69 核实）。
- **p06** 4000 AP / 100K 客户端上限——Enterprise/Cloud 规模校核硬顶（p52/p60/p75 三处一致）。
- **p07** 智能负载均衡 SNR 门限——2.4G=18dB/5G=12dB 默认值与 0-40dB 范围。
- **p08** 快速漫游协议适用规则——OKC 仅 Enterprise、11r 双适用的认证方式适配矩阵。
- **p09** BLE/Zigbee 能力边界——机型清单 + 默认参数（iBeacon、默认关闭）。
- **p10** RAP 前提条件——机型/版本门槛 + Cirrus 账号组合规则。
- **p11** WPA3 规则——CNSA 开关对终端准入的实际影响是高安全项目的关键判据（p105 核实）。
- **p12** WiFi4EU 12 小时会话常数——欧盟公共场馆项目硬性合规参数。
- **p13** Mesh 限制与最佳实践——8 从 AP/4 跳/16 台/5 SSID + 5GHz 信道>100。
- **p14** Guest GRE 隧道容量——16/750/1000 三层数字，访客隔离方案校核。
- **p15** 三模式 License 边界——Express 免 License 送 5 永久授权，报价起点判断。
- **p16** OV2500 License 模块与 Starter Pack——五类模块 + 评估版 60 天规则。
- **p17** OV2500 下单编码——OV-AP-NM-X-N 等档位取整规则。
- **p18** OAW-APxxxx-Region 与配件命名——区域码错配会直接导致注册失败，联动 p68 国家码。
- **p19** PW/SP 维保编码逐位解码——P/S、W/P、年数、R/N 的完整语法。
- **p20** Freemium vs Premium（5000 上限）——云管账号形态边界与订阅弹性。
- **p21** 每 AP 1 License 附 50 Guest + 50 BYOD——与 OV2500 Starter 10+10 对比的附送额度。
- **p22** Cirrus 4 下单 Part Number——OVC-AP-BAS/BIZ/XY 旧版体系（防与 Cirrus 10 混用的基线知识）。
- **p23** OVCX 编码细则——63 个 PN + AP1431→APH、OS6860N-P24Z→68 的判定示例。
- **p24** Cirrus 10 三档服务差异表——TAC/硬件服务的对象差异是推荐档位的决策依据（注意 p155 笔误标注）。
- **p25** ESL USB Dongle 方案规则——发射器 vs Dongle 选型结论 + 2.4GHz 专有射频细节。
- **p26** 软终端门槛——iOS 8/S7/S9(11v) 分档，BYOD 语音评估先盘终端。
- **p27** 语音覆盖常数——255m²/AP、20-25 用户，快速估算基准公式。
- **p28** VoWLAN 规划参数——5GHz 优先、36Mbps 吞吐、-62dBm 漫游阈值三件套。
- **p29** 客房数量公式与墙体衰减——15/30dB 分级 + -65/-70/-80dBm 推导链（注意 p243 笔误标注）。
- **p30** 客房推荐配置——RSSI 20/15、HT20、限速 2/4Mbps 等可背清单（p247 核实）。
- **p31** 高密场馆估算链——1500 人×50%→750 并发→8-10 台三射频 AP（p249 核实）。
- **p32** 场馆推荐配置——功率≤15dBm、HT40、GI 0.8/1.6us 与客房取值相反有理由。
- **p33** 会议室速查表——40-60/80-120/160-200 客户端→1/2/4 台（p258 核实）。
- **p34** 户外部署规则——20% 并发、6-8 台 AP1361、抱杆最高点、802.3at 供电。
- **p35** Network Advisor 定价——NETAD-* 牌价与 1 年约占总网成本 1.8% 的报价锚点（p231/p233 核实）。

## cases（18 条）

- **c01** 千床医院换 Aruba——双认证/UCOPIA/VPN MPLS 拓扑等完整方案话术，医疗行业模板（p171 核实）。
- **c02** 五星酒店 802.11ac wave2 改造——含装后审计发现信道重叠、缩信道宽度整改的完整复盘情节。
- **c03** 理工大学换 Cisco——EDUROAM 兼容应答 + Chillispot 门户 + GRE 访客隧道兜底。
- **c04** 文理学院换 Ubiquiti——混凝土墙/雷暴恶劣环境 + 400→2000 用户弹性的差异化论证。
- **c05** 轮渡船队全船 Wi-Fi——金属船体覆盖 + 客舱 VoD 场景，交通行业独有案例。
- **c06** 音乐学院智慧城市——UPAM/LDAP/OPEN 门户 500 会话等集成细节最全的政府类案例。
- **c07** 零售 ESL——"复用既有 AP USB 口、免布线"的增量销售模板（p196-198 核实）。
- **c08** AP1301H 规格实例——下联 PoE 出电 + 直通口服务客房/病房选型（p17 核实，规格以 p17 为准）。
- **c09** AP1231 规格实例——三射频规格 + p249 高密场馆用法联动。
- **c10** AP1511/AP1521 Wi-Fi 7 规格实例——两款差异（5G 2x2 vs 4x4、上联 5GE vs 10GE）经 p26/p27 逐行核实。
- **c11** VoWLAN 话机产品线——8118/8128/8158s/8168s 矩阵 + RTLS/IMS3 配套。
- **c12** Aruba 过渡共存双路径——ClearPass 复用与 OV 反向接管，竞品替换降风险话术。
- **c13** Zigbee 门锁用例——数字钥匙集中管理，智慧酒店关键用例（p98 核实）。
- **c14** AeroScout RTLS 用例——复用 Stellar AP 做定位，"不建专网"的迁移话术。
- **c15** Bridge/Mesh 成对用例——露营覆盖 vs 隔街楼宇两组配置示例（含 SSID/密码示例）。
- **c16** RAP 用例——居家/分支场景 + OV2500 与 Cirrus 账号组合规则。
- **c17** Network Advisor 报价实例——设备清单+订阅明细+1.8% 占比的完整报价演练（p233 核实）。
- **c18** 客房公式部署实例——公式+布放+配置基线三联动（注意 p243 笔误标注）。

## counter-examples（23 条）

- **ce01** 三套 License 体系并存陷阱——混用 part number 的退单场景 + Cirrus 4→10 迁移盲区提醒。
- **ce02** Freemium 只看不能改——"免费云管"过度承诺的期望管理反例。
- **ce03** Base 不含设备 TAC/硬件服务——Cirrus 4（p141）与 Cirrus 10（p155）双重核实，压价翻车点。
- **ce04** Cirrus 10 机型排除清单——AP1101/AP1201H/L/LH 白买风险 + 8.9R 版本门槛（p166 核实）。
- **ce05** 255 静默 joining——不报错的扩容故障模式（p46 逐句核实）。
- **ce06** "Easy conversion" 话术与配置丢失现实——p84 卖点页与 p66 迁移页的对打点，两处原文均核实。
- **ce07** Express 远程管理不能升镜像——连锁客户固件升级的例外条款（p82 核实）。
- **ce08** 注册失败射频全关 + 默认手动 Trust——批量开局"全部没信号"排障路径（p68/p69 核实）。
- **ce09** Zigbee 机型例外——AP1301/AP1230 恰是入门机型，IoT 项目利润侵蚀点。
- **ce10** 老机型例外集中清单——AP1101 不支持 RAP + 三款桥接不支持 VLAN 打标。
- **ce11** Mesh 四道红线——16 台/8 从/4 跳/5 SSID 的规模预算切分依据。
- **ce12** OKC/11r 选错认证方式——Personal 场景写 OKC 的漫游卡顿反例。
- **ce13** 隧道三层容量上限——访客网局部瘫痪的设计校核反例。
- **ce14** WCF 10 台一份取整——12 台买 1 份导致策略不一致的报价细节。
- **ce15** CNSA 拒老终端——高合规开启后扫码枪/打印机掉线的盘点前置要求。
- **ce16** Enterprise 管理面仅 IPv4——与"去 IPv4"战略客户的冲突点（Express 反而支持 v6 的反差）。
- **ce17** 酒店装后审计整改——信道重叠靠缩信道宽度解决的真实验收复盘（p178 核实）。
- **ce18** 金属船体推翻 AP 规划——勘察前置与"以勘察结果为准"调价条款的教训。
- **ce19** 承重墙 30dB 报价分档教训——不区分墙体导致 AP 用量翻倍的预算双爆场景。
- **ce20** 软终端质量随硬件/OS 浮动——责任界定与终端准入清单的规避法。
- **ce21** Network Advisor 隐性成本四件套——虚拟机自购/版本门槛/2000 上限/激活即倒计时（p230/p232/p233 核实）。
- **ce22** BG-S 关闭的连带失效——WIPS/APC/快速漫游依赖与 ATF 反例的配置依赖陷阱。
- **ce23** 教材时代局限与自相矛盾——p243 802.11ac 误标与 p95 AP1421 不存在机型均经原文实证，引用时效自检清单。

## glossary（45 条，免验保留）

45 个词条无重复术语，全部保留：802.11r/k/v、Access Guardian、AeroScout RTLS、AWOS、BLE Beaconing、BYOD、Captive Portal、Controller-less Architecture、DHCP Option 138、DPI、DRM、eBuy、EDUROAM、Ekahau、ESL、Freemium/Premium、GRE Guest Tunneling、HA、Hotspot 2.0、Maintenance Contract (PW/SP)、Network Advisor、OAW-APxxxx-Region、OmniVista 2500、OmniVista Cirrus 4、OmniVista Cirrus 10、OV2500-NG-AP、OVCX-[Category]-[Level]-[Duration]、PVM/SVM、Rainbow、RAP、RTLS、Smart Load Balancing、Starter Pack、Stellar Enterprise (On-Premise)、Stellar Enterprise Cloud、Stellar Express、UNP、UPAM、VoWLAN、WCF、Wi-Fi Bridge、Wi-Fi Mesh、WIPS/wIDS、WPA3、Zigbee。

原文与词条定义抽样一致（如 p95 BLE 默认参数、p141 服务包、p130 Starter Pack）。g21 中"30+ 种预置异常"与 f16 的"40+"同样属未获原文支持的数量表述，p219-220 实列 17 个具名异常，后续蒸馏时统一改为"预置异常库（持续更新）"为宜。
