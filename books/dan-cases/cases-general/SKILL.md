---
name: 综合行业客户案例集（12 例）
description: 查制造、工程、电力、零售、体育赛事、纺织服务、园区、银行等行业客户用了哪些 ALE 产品与方案时使用。宝钢梅钢、BMW International Open、Pittsburgh Steelers、Banner Bank、Rainbow CPaaS、OmniSwitch
source_book: dan-cases（customer-reference-ebook-en-2024 p85-97）
---

## R（何时用）
- 售前打制造/钢铁、化工工程、电气经销、机械制造、能源、体育场馆/赛事、纺织服务、零售奥特莱斯、创意园区、银行等泛行业客户，需要同行业标杆案例做证据
- 客户痛点在：老 PBX/旧网络换代到 IP 与 UCC、临时大型活动组网、呼叫中心与应急通知、仓库/园区 WLAN、网络虚拟化分段
- 找不到专属行业章案例时的"兜底案例库"

## I（核心理念）
综合章 12 例，行业高度分散但规律清晰：一半是"老旧系统现代化"（CSF Inox 老 PBX 换 IP+云、Polytype 百兆无 PoE 网络换代、Steelers 15 年老话音替换、MEWA 全欧异构电信标准化、Baosteel 网络虚拟化分段），一半是"场景型项目"（BMW 高尔夫赛事临时组网、Genting 奥特莱斯高可用+IoT、Kreativ House 多租户 BYOD、Banner Bank 疫情 200 坐席呼叫中心）。新技术亮点集中在 Rainbow 生态：CPaaS/API Hub 做虚拟助手（CSF Inox 查库存/工单时间减半）、WebRTC Gateway（BMW）、云协作应急（Banner Bank）。主流组合仍是"OmniSwitch 6900/6860/6450 + OmniVista + OXE + Rainbow"。明星产品：OXE（7 例）、OmniSwitch 6900/6860、Rainbow 全家族、OpenTouch。

## A1（案例速查表）
| 客户 | 国家/地区 | 项目背景/挑战 | 采用的 ALE 方案与产品 | 成效关键数字 | 页码 |
|---|---|---|---|---|---|
| Meisteel factory of Baosteel group（宝钢梅钢） | 中国 | 最具竞争力钢铁集团：旧网更新、业务虚拟化分段、数据中心升级 | Network：OmniSwitch 9702E、6850E（Application Fluent Network） | 网络性能、可靠性、管理三提升，支撑虚拟化与 IT 转型 | p86 |
| Tianchen Engineering Corporation (TCC) | 中国 | 3 栋办公楼 4000 VoIP 用户、6000 网络口的全融合网络 | Converged：OmniSwitch 9000E/6900/6450/6250、OmniAccess AP103H/93H、IP Touch 40xx、OmniVista 2500/8770 | IT 水平"领先同行化学工程院近 20 年"（客户口径） | p87 |
| SMC Electric Supply (SMC) | 美国 | 员工外出漏接客户来电，需可携带话机+呼叫转移 | Converged：OmniSwitch 6450/6900/6860、OmniAccess AP、IP Touch 4038/4068、OpenTouch Business Edition、8118 WLAN 话机 | 全部站点单一系统，客户服务改善、商机不再流失 | p88 |
| CSF Inox | 意大利 | 老 PBX 更换为 IP 电话，并要云端统一通信+员工移动 | Communication：Rainbow Essential、Rainbow API Hub、OXE、4059 话务台、8018/8019s/8029/8039 话机 | Rainbow 驱动的虚拟助手 CSF Assistant：查库存/工单/订单状态时间减半 | p89 |
| Polytype | 瑞士 | 老系统撑不起 UCC；接入交换机无 PoE、百兆接入、上行 1G 瓶颈 | Converged：OmniSwitch 6560、Stellar AP1320、OXE、DECT 8254、OpenTouch Multimedia Services/Conversation、OmniVista 8770 | 从硬件话音升级到虚拟化 VoIP UCC 环境 | p90 |
| Energy One | 澳大利亚 | UC 上线前的网络体检暴露连接问题，需可扩展集中管理 | Network：OmniSwitch 6350、Stellar AP1222、OmniVista 2500、PALM | 跨悉尼/墨尔图两站点一致的用户体验 | p91 |
| BMW International Open | 德国 | 高尔夫赛事：郊区信号弱+数万观众/媒体/赞助商的高带宽需求 | Converged：OXO Connect、Premium 话机、8378 DECT IP-xBS、DECT 8212-8262、Cloud Connect、Rainbow+WebRTC Gateway、OmniSwitch 6450/6560/6860/6900、Stellar AP、OmniVista 2500、4 公里 1/10G 光纤、POS 集成 | 全程零故障零投诉（客户口径） | p92 |
| Pittsburgh Steelers | 美国 | 15 年老话音替换：票务呼叫中心、会议、场馆移动；ERP 与标牌依赖数据网 | Converged：OmniSwitch 6450/6900、OmniVista 2500、OXE、OmniTouch 8082 | 数据+话音全网 ALE，从票务到场馆全覆盖 | p93 |
| MEWA Textil-Service | 德国 | 2017 年起全欧洲站点电信架构从异构到标准化 | Communication：OXE、8018(s)/8028(s)/8058s/8029(s) 话机、OmniVista 8770、OpenTouch UC、OpenTouch Softphone、robot5 Agent Line/Alarmserver | 2020 年春疫情下远程运营零中断、零生产力损失 | p94 |
| Genting Highlands Premium Outlets | 马来西亚 | 奥特莱斯高可用网络保障计费/客户管理应用，并为 IoT 做准备 | Converged：OmniSwitch 6900/6450、OXE、Professional Services（咨询设计+集成部署） | 稳健可扩展方案同时支撑 IoT 目标，网络可视化加分 | p95 |
| Kreativ House | 英国 | 多租户创意园区：展览活动最多 200 人，需跨站点一致服务+简单安全 BYOD | Network：Stellar AP1221、OmniSwitch 6860E、OmniVista 2500 | 为租户与访客提供可靠连接，可复制到新站点 | p96 |
| Banner Bank | 美国 | 2020 疫情：200 名坐席快速上远程，全分支来电统一管理+应急实时可见 | Communication：OXE、OpenTouch Customer Service/MultiMedia Services、OmniPCX Record、8068s 话机、OmniVista 8770、Emergency Notification Server | 200 坐席快速投产；通话路由按需分配、运维成本更低 | p97 |

## A2（精选案例详解）

### 1. BMW International Open（德国，p92）——临时大型活动组网样板
- 挑战：高尔夫球场远离城区信号弱；主办方、赞助商、全球媒体与数万观众同时产生高带宽需求。
- 方案：OXO Connect + 全线 OmniSwitch 6450-6900 + Stellar AP + DECT + Cloud Connect + Rainbow WebRTC + 4 公里 1/10G 光纤 + POS 集成。
- 成效：客户原话"零故障、零投诉，一切如设想般进行"。售前要点：大型赛事/展会/临时场地的"军事级"组网参考，产品线覆盖最全的单页案例。

### 2. CSF Inox（意大利，p89）——Rainbow CPaaS 落地制造业
- 挑战：老 PBX 换代；要与既有设施集成的云端统一通信，提升员工移动性。
- 方案：OXE + Rainbow Essential + Rainbow API Hub + 全系列 8 系话机。
- 成效：自建虚拟助手"CSF Assistant"，用对话查询库存、泵加工进度、订单状态——处理时间减半。售前要点：全书少见的 API/CPaaS 量化成效，打数字化创新需求。

### 3. Banner Bank（美国，p97）——疫情呼叫中心应急
- 挑战：2020 年疫情突袭，需让 200 名坐席尽快远程就位，统一管理全分支来电并实时可见应急事件。
- 方案：OXE + OpenTouch Customer Service + OmniPCX Record 录音 + 8068s 话机 + OmniVista 8770 + Emergency Notification Server。
- 成效：200 坐席快速投产；客户评价"来电即接真人、按需路由、运维成本更低、易扩展"。售前要点：金融行业+呼叫中心+应急通知三合一案例。

### 4. Tianchen Engineering（中国，p87）——中国大型园区融合网
- 挑战：3 栋办公楼、4000 VoIP 用户、6000 网络端口，要求端到端高性能、高可靠、集中管理、低功耗。
- 方案：OmniSwitch 9000E 核心 + 6900/6450/6250 + OmniAccess AP + IP Touch 全系 + OmniVista 2500/8770。
- 成效：客户 IT 总监称"IT 水平领先其他化工工程院近 20 年"。售前要点：打中国大型工厂/设计院的全家桶参考，规模数字（4000 用户/6000 端口）好用。

### 5. MEWA Textil-Service（德国，p94）——泛欧标准化
- 挑战：2017 年决定用一套标准方案替换全欧洲高度异构的电信基础设施，含话音、聊天、语音信箱、协作，且须支持远程。
- 方案：OXE + OpenTouch UC/Softphone + 全系 8 系话机 + OmniVista 8770 + robot5 告警。
- 成效：2020 年春疫情最紧时远程运营"零中断、零生产力损失"。售前要点：跨国多站点标准化 + 疫情压力测试双重叙事。

## E（售前怎么用这些案例）
- 按痛点选案例：老 PBX/旧网换代 → CSF Inox、Polytype、Steelers、MEWA；大型活动/临时组网 → BMW International Open；呼叫中心+应急 → Banner Bank；中国制造/工程园区 → Baosteel 梅钢、TCC；零售/商业地产 → Genting；多租户园区 → Kreativ House；分销/外勤接电话 → SMC。
- 打中国客户用宝钢梅钢（央企钢铁龙头）与 TCC（4000 用户/6000 端口）。
- 量化话术：CSF Inox"处理时间减半"、TCC"4000 VoIP 用户+6000 端口"、BMW"4 公里光纤、零故障"、Banner"200 坐席"。
- 找不到行业专属案例时（金融、赛事、零售、能源等），本章是兜底库；但优先级仍低于六个行业章。
- Rainbow API Hub/CPaaS 是差异化亮点，遇到客户问"AI/自动化能干什么"用 CSF Assistant 举例。

## B（引用注意）
- p91 Energy One 页的引文排版错误（误贴了 CSF Inox 的证言），引用 Energy One 证言时须回原 PDF 核对。
- TCC、SMC、Steelers 使用 IP Touch 40xx、OmniTouch 8082 等旧型号，新项目须换 8/9 系。
- "领先同行 20 年""零故障"为客户主观口径，勿写入承诺性文案。
- BMW International Open 产品页注明引言人署名为 SMC 的 Charles Givens，疑为原书排版错误，引用署名时注意核对。

来源：dan-cases · customer-reference-ebook-en-2024，p85-97
