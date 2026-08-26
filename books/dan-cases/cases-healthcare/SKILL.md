---
name: 医疗客户案例集（19 例）
description: 查医疗行业（医院、养老、医疗研究机构）客户用了哪些 ALE 产品与方案时使用。Shengjing Hospital、Aster DM、Oroville Hospital、Rainbow 远程医疗、 OmniPCX Enterprise、OmniAccess Stellar 无线网络
source_book: dan-cases（customer-reference-ebook-en-2024 p4-22）
---

## R（何时用）
- 售前打医院、诊所、养老护理、医疗集团客户，需要同行业标杆案例做证据
- 客户痛点在：全院无线覆盖、多院区互联、移动查房/护理通话、远程医疗（telehealth）、24/7 关键业务不中断
- 需要论证"网络+通信融合方案（Converged）"在医院场景的价值

## I（核心理念）
医疗是全书案例最多的行业（19 例），痛点高度一致：带宽爆炸式增长（医疗数字化、电子病历、影像视频）、医护移动化（WLAN 话机/软终端随处接打）、24/7 业务不中断、多院区/多站点统一通信。主流方案组合是"OmniSwitch 有线 + OmniAccess/ Stellar 无线 + OmniVista 2500/8770 管理 + OmniPCX Enterprise（OXE）语音 + Rainbow 云协作"，疫情场景中 Rainbow 视频远程问诊成为亮点（Cantabrian 5000 名医护人员、WEHI 远程办公）。明星产品：OXE（19 例中约 12 例）、OmniVista 2500、Rainbow、ClearPass（访客/设备准入）、Visual Automated Attendant（前台话务台）。

## A1（案例速查表）
| 客户 | 国家/地区 | 项目背景/挑战 | 采用的 ALE 方案与产品 | 成效关键数字 | 页码 |
|---|---|---|---|---|---|
| The Shengjing Hospital of China Medical University | 中国 | 扩建需匹配的网络与通信系统 | Converged：OmniSwitch 9700/6850/6250、OmniAccess 6000、AP60&93、OXE | 中国医疗系统最大无线网络；应急抢救与住院流程省时 | p4 |
| Shanghai Punan Hospital | 中国上海 | 3 栋楼互联、建 active/active 虚拟化数据中心、全区无线覆盖 | Network：OmniSwitch 9700E/6850E/6450/6900、AP103H、OmniVista 2500 + VM Manager | 约 1000 名员工、36 个临床科室、年手术超 1 万台、年接诊约 100 万人次；运维成本显著下降 | p5 |
| Medcare | 阿联酋 | 6 个院区融合、医护人员跨院区移动 | Converged：OmniSwitch 6900/6860/6450、OmniAccess WLAN 控制器与 AP、OXE、Premium DeskPhones | 医生即时调阅医疗信息，5 星级患者体验 | p6 |
| Fertilys Clinic | 加拿大 | 辅助生殖中心两院区话务可靠处理 | Communication：OXE、OpenTouch Message Center、OmniVista 8770、DeskPhones、Visual Automated Attendant | 患者呼叫处理统一高效，临床运营改善 | p7 |
| Inspira Health Network | 美国 | 临床应用随处访问、护士移动生产力 | Converged：OXE、OmniSwitch 堆叠、OmniAccess WLAN 控制器、OmniTouch 8128 WLAN 话机 | 患者满意度与护士生产力提升 | p8 |
| Thomas Holt | 澳大利亚 | 养老社区"像家一样的技术体验"+ 24/7 健康监测 | Network：OXE、IQ Messenger、OmniSwitch、OmniAccess Stellar AP、DeskPhones | 居民健康数据 24/7 监测，护士移动随时取关键医疗信息 | p9 |
| Care Outlook | 英国 | 居家护理机构需要可靠云端话务 | Communication：Rainbow UCaaS Office/Enterprise 订阅、8008 DeskPhone | 云 UC 支撑居家护理服务，呼叫 diversion 响应迅速 | p10 |
| WEHI | 澳大利亚 | 疫情远程办公、新址共享工位、Mac 95%/Windows 5% 混合终端 | Communication：OXE、Rainbow、Microsoft Teams Connector、ALE 300 话机、Softphones | 混合通信方案实现 anywhere 远程办公 | p11 |
| Asian Hospital and Medical Center | 菲律宾 | 带宽需求爆炸、需易运维的 WLAN | Converged：OmniAccess Stellar AP1311/1321、OmniVista 2500、Rainbow、OXE | 高速安全网络保障医患客可靠连接 | p12 |
| Kent and Medway NHS Partnership Trust (KMPT) | 英国 | 关键应用（电子病历/影像/视频会议）可靠访问，人均 4 台设备 | Communication：OmniVista 3600 Air Manager、OmniAccess WLAN AP、ClearPass Policy Manager | 多媒体流量优先级保障，门诊/住院/社区团队安全互联 | p13 |
| Triaplus AG | 瑞士 | 开放平台+DECT、单向寻呼升级为双向定位报警 | Communication：OXE、Rainbow、MobiCall（New Voice） | 双向语音+文本报警、紧急呼叫精确定位，员工安全提升 | p14 |
| Oroville Hospital | 美国 | 网络三阶段演进、LAN/WLAN 标准化、边缘刷新 | Network：OmniAccess 4704、OmniSwitch 6450E/6860/6900、OmniVista 2500、Professional Services | 简化基础设施、降低复杂度 | p15 |
| East Sussex Healthcare NHS Trust | 英国 | 面向未来的基础设施、医生移动设备 | Network：OmniSwitch 6900、6450-P48、OmniAccess 4650 控制器、WLAN AP、RAP3WN、ClearPass | 冗余可靠、经济高效地支撑行政与临床协同 | p16 |
| Aster DM Healthcare | 阿联酋 | 新建多专科医院、24x7 医疗数据访问、跨院区移动协作 | Converged：OmniSwitch 6900/6450、Stellar AP1221/1201、OmniVista 2500/8770、OXE、Premium DeskPhones、Rainbow | 55 床疫情治疗设施以创纪录速度上线 | p17 |
| Emirates Specialty Hospital (ESH) | 阿联酋 | 迪拜国际患者多专科医院、高可用网络底座 | Converged：OmniSwitch、OmniAccess WLAN AP+控制器、OmniVista 8770、ClearPass、OXE、DeskPhones、Professional Services | 24/7 医疗数据访问 | p18 |
| Royal Prince Alfred Hospital | 澳大利亚 | 数字化医疗转型、个人设备/VoIP/电子病历全无线支撑 | Converged：OXE、OmniSwitch 堆叠、OmniAccess WLAN 交换机 | 全院把网络当"理所当然可用"——高可用实证 | p19 |
| Kingsway Hospitals | 印度 | 24/7 关键实时通信底座 | Communication：OXE、OmniVista 8770、Premium DeskPhones、Rainbow | OXE+Rainbow 云服务提供富媒体、无边界的移动协作 | p20 |
| Mayotte Hospital Centre | 法国（马约特） | 15 个院区电话现代化、全员无线移动 | Communication：OXE、OmniVista 8770、Premium DeskPhones、8118/8128 WLAN 话机、OmniTouch CC Standard、Visual Automated Attendant、IP 软终端 | 15 站点可靠通信、内外线话务专业化处理 | p21 |
| Cantabrian Health Service | 西班牙 | 疫情下远程医疗视频问诊 | Communication：Rainbow | 视频问诊系统服务 5000 名医护人员，覆盖医院/卫生中心/医疗稽查 | p22 |

## A2（精选案例详解）

### 1. Cantabrian Health Service（西班牙，p22）——Rainbow 大规模远程医疗标杆
- 挑战：全球疫情下必须维持患者照护，需要可靠、安全、易用的医患视频连接（telehealth）。
- 方案：仅用 Rainbow 云通信平台即构建大规模视频问诊系统。
- 成效：服务 5000 名医护人员（医院、卫生中心、医疗稽查），高效管理问诊、优化患者照护交付。售前要点：单一云产品即可落地全区域远程医疗，部署轻。

### 2. Aster DM Healthcare（阿联酋，p17）——新建医院 Converged 全家桶
- 挑战：新建多专科医院，需 24x7 医疗数据访问、临床应用支撑与跨院区移动协作。
- 方案：OmniSwitch 6900/6450 有线 + Stellar AP1221/1201 无线 + OmniVista 2500/8770 管理 + OXE + Premium DeskPhones + Rainbow。
- 成效：55 床疫情治疗设施"以创纪录时间"上线；集团在阿联酋多院区复用同套方案，验证可复制性。

### 3. Shanghai Punan Hospital（中国上海，p5）——多院区+数据中心高可用
- 挑战：3 栋异地楼宇互联；服务器农场需 active/active 虚拟化数据中心；全院区无线全覆盖。
- 方案：OmniSwitch 9700E 核心/6850E/6900/6450、AP103H、OmniVista 2500 + Virtual Machine Manager。
- 成效：支撑约 1000 员工、36 个科室、年手术 1 万+、年接诊约 100 万人次；安全防护提升的同时运维成本显著降低、问诊时长缩短。

### 4. KMPT（英国，p13）——NHS 信托无线+准入
- 挑战：电子病历、影像、视频会议等关键应用可靠访问；人均最多 4 台设备；多媒体流量需优先级。
- 方案：OmniVista 3600 Air Manager + OmniAccess WLAN AP + ClearPass Policy Manager。
- 成效：集中管理的可靠无线支撑门诊、住院与社区团队的创新工作方式。售前要点：英国 NHS 客户普遍认可"partnership"叙事（参见 East Sussex 与 Khipu 合作）。

### 5. WEHI（澳大利亚，p11）——混合办公+Mac 环境通信
- 挑战：疫情远程办公；新址共享工位；Mac 用户占 95%；关键电话集成云协作应用；桌面打手机/固话成本控制。
- 方案：OXE + Rainbow + Microsoft Teams Connector + ALE 300 话机 + 软终端。
- 成效：hybrid 通信实现 anywhere 远程办公，CIO 公开背书 ALE 的 PoC 与迭代能力。

## E（售前怎么用这些案例）
- 按痛点选案例：无线全覆盖/移动查房 → Shengjing、Inspira、Mayotte；多院区融合 → Medcare、Aster、Mayotte（15 站点）；远程医疗/疫情 → Cantabrian、WEHI；高可用数据中心 → Punan；NHS 类公立客户 → KMPT、East Sussex（强调伙伴式交付）。
- 中国客户优先引用 Shengjing（"中国医疗系统最大无线网络"）与 Punan（同城上海、数字可查）。
- 量化话术：Cantabrian"5000 名医护人员"、Punan"年接诊 100 万人次"、Aster"55 床设施创纪录上线"。
- 案例均标注了 Customer success story / video / reference 三类资产，可向市场部要原文或视频做 PO 资产。

## B（引用注意）
- 本电子书为 2024 年 1 月版（p98 版权页），部分案例为早年项目（如 GRU/Movis 等 2013-2015 年代产品如 OmniVista 4760、IP Touch 40xx 已退市或接近 EoL），引用时注意产品线时效，避免给客户报旧型号。
- "最大无线网络""5 星体验"等为客户证言口径，非第三方审计数字，勿写成承诺。
- 成效数字（100 万接诊、5000 用户等）为客户披露口径，仅代表该客户当时规模，不代表 ALE 产品通用指标。

来源：dan-cases · customer-reference-ebook-en-2024，p4-22
