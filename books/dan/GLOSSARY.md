# 术语词典

| 术语 | 含义 | 出处页码 |
|---|---|---|
| Digital Age Networking (DAN) | ALE 面向数字化转型的企业网络愿景与方案总称，基于三支柱 | dan-overview p2；dan-wp-apac p4 |
| Autonomous Network（自主网络） | 三支柱之一：自动配置开通网络服务、自动化关键任务运维；OmniSwitch LAN + OmniAccess Stellar WLAN + iFab + 单一 NMS | dan-overview p3；dan-wp-apac p5 |
| IoT onboarding | 三支柱之一：海量 IoT 设备的安全开通与管理 | dan-overview p2 |
| Business Innovation | 三支柱之一：以自动化工作流（位置数据 + Rainbow）替代重复人工任务、催生新营收 | dan-overview p2；dan-wp-apac p10 |
| Service Defined Network | DAN 的连接基础：从一个用户或物体到授权应用的自动安全连接（2019 白皮书核心概念） | dan-wp-global p3/p5 |
| iFab（Intelligent Fabric） | 智能织网技术：自动化网络部署、简化 MAC（搬迁/新增/变更） | dan-overview p3；dan-wp-global p5 |
| SPB（Shortest Path Bridging, IEEE 802.1aq） | 最短路径桥接标准：iFab 底层，最大化全部物理链路利用率、弹性架构 | dan-wp-global p5；dan-edu p3 |
| UnP（Universal network Profiles） | 通用网络档案：接入层统一下发部门/应用访问、安全、性能与 QoS 策略 | dan-wp-global p5 |
| IoT containment | IoT 收容法：发现分类→虚拟分段→持续监控三步安全接入机制 | dan-wp-global p8；dan-wp-apac p8 |
| Virtual segmentation（虚拟分段） | 把单张物理网切分为独立虚拟容器，按应用隔离 IoT 流量 | dan-wp-global p8；dan-trans p5 |
| 29+ million 设备库 | 设备指纹数据库，自动识别接入设备并下发配置（2019 版口径为 17 million） | dan-wp-apac p8；dan-edu p4；dan-wp-global p8 |
| Fingerprinting（设备指纹） | 通过特征识别设备型号的能力，配合设备库实现自动分类 | dan-wp-global p4；dan-health p5 |
| QoE（Quality of Experience） | 用户体验质量：网络自动识别并优化，劣于阈值时定位问题 | dan-wp-global p3/p10 |
| DPI（Deep Packet Inspection） | 内嵌于 AP/交换机的 L2-L7 深度包检测，支撑应用可视与按应用管控 | dan-wp-global p6 |
| NMS（Network Management System） | 单一网络管理系统：统一有线无线的服务管理、策略与全网可视（本地/云/混合） | dan-overview p3；dan-wp-apac p6 |
| Augmented intelligence（增强智能） | ML + 数据分析：异常通知、优化建议、变更提案-批准-自动化执行闭环 | dan-wp-global p10 |
| Cloud economics | 云经济：pay-as-you-go 商业模式让 IT 成为业务引擎 | dan-wp-global p4/p11 |
| NoD（Network on Demand） | ALE 订阅模式：网络基础设施即服务，CAPEX 转月度固定 OPEX | dan-wp-global p11 |
| LBS（Location-based Services） | 位置服务：wayfinding 室内导航 + geonotifications 位置推送，云端管理 | dan-wp-global p11/p12；dan-hosp p6 |
| Wayfinding | 室内自主导航（类似车载转弯指引），LBS 组件 | dan-wp-global p12；dan-hosp p6 |
| Geonotification / Geo fence | 按地理位置推送消息；虚拟边界越界即触发动作（推送/告警/策略执行） | dan-wp-global p12；dan-hosp p6 |
| OmniAccess Stellar Asset Tracking | 资产追踪：Wi-Fi + Bluetooth 实时/历史定位、热点追踪、contact tracing、占用管理 | dan-wp-apac p10；dan-health p6 |
| Contact tracing | 历史接触追溯：定位密接人员并跟进通知（化学品暴露/传染病场景） | dan-edu p5；dan-health p6 |
| Occupancy management | 占用管理：预定义区域人员密度检查，超限自动告警 | dan-edu p5；dan-health p6 |
| Rainbow | ALE 协作平台：与位置数据集成，用 triggers/rules/actions 实现工作流自动化 | dan-wp-apac p10；dan-hosp p7 |
| Triggers / Rules / Actions | 工作流三要素：事件触发 → 规则判定 → 自动执行动作 | dan-edu p6；dan-hosp p7 |
| OmniVista Cirrus | 云端 NMS-as-a-Service：pay-as-you-go，内置访客接入、BYOD、分析 | dan-wp-apac p10；dan-hosp p4 |
| Guardian | 待确认：本次 9 份 DAN 文档中未出现 "Guardian" 术语；ALE 语境下另有 Guardian 相关产品线时以产品资料为准 | — |
| IoMT（Internet of Medical Things） | 医疗物联网：联网医疗设备（固定/移动）的统称 | dan-health p5 |
| Connected but not consolidated | 医疗融合网络原则：多张科室网接入单一基础设施但保持虚拟隔离 | dan-health p3 |
| VNA（Visual Notification Assistant） | 可视通知助手：与 Asset Tracking 标签按钮联动，精细派发呼叫/消息，缓解警报疲劳 | dan-health p8 |
| EHR / EMR | 电子健康档案 / 电子病历：需随时随地低时延调阅的核心医疗应用 | dan-health p2/p5 |
| IoT Hub | ALE IoT 控制器：经标准 API 与第三方网关集成非原生标准（BLE/Zigbee 之外）的 IoT 技术 | dan-hosp p5 |
| WPA3 | 第三代 Wi-Fi 安全协议：OmniAccess Stellar AP 支持 | dan-trans p4 |
| OS hardened switch（secure diversified code） | 安全多样化代码实现的操作系统加固交换机 | dan-trans p4；dan-wp-apac p5 |
| 4000 AP 单集群 | OmniAccess Stellar WLAN 免集中控制器的单集群扩展上限 | dan-trans p4 |
| ITS（Intelligent Transportation System） | 智能交通系统：信息通信技术用于交通管理，提安全效率、降拥堵 | dan-trans p2 |
| SCADA | 数据采集与监控系统：轨道关键任务网典型承载业务 | dan-trans p2/p4 |
| SD-WAN / SASE | 软件定义广域网 / 安全访问服务边缘：用于养老照护等远程小站安全互联 | dan-health p9 |
| BYOD（Bring Your Own Device） | 自带设备办公/学习：访客与个人设备接入场景 | dan-wp-apac p10；dan-edu p4 |
| MAC（Moves, Adds, Changes） | 网络运维中的搬迁/新增/变更操作，iFab 的核心简化对象 | dan-wp-global p5 |
| TCO（Total Cost of Ownership） | 总拥有成本：免控制器架构与云管的降本论据 | dan-wp-global p6；dan-hosp p3 |
| Ruggedised（加固型） | 承受恶劣环境的室外交换机/AP，交通与工业场景专用 | dan-trans p4 |
