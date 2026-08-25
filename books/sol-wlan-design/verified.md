# Verified 候选（V1 原文真实性核对 + V2/V3 抽查）

## cases

- **C1 5 万座体育场需求画像**：Several tens of thousands of seats (the example given in this note is for a stadium with up to 50,000 seats)... More access points than channels in the 5GHz band... Users are mainly guests (up to 2 devices per person). <<<PAGE 5>>>
- **C2 VHD 单用户吞吐衰减基线**：A measured throughput of 80Mbps (MCS8 modulation) for a single Wi-Fi 6 user on a 5GHz channel... dropping to 40Mbps when there's a high concentration of clients connected on the same channel (average of 60 clients). <<<PAGE 11>>>
- **C3 25% VHD 场景折减系数**：A 25% ratio, specific to VHD in stadium, is introduced to account CCI/ACI effects... Wi-Fi interference, non-Wi-Fi interference and considering a moderate duty cycle. <<<PAGE 11>>>
- **C4 52,000 座并发负载推算**：For example, in a stadium with a capacity of 52,000 seats, this equates to a load of 21,000 concurrent devices, or 60 devices per AP and more.（30% 并发率） <<<PAGE 12>>>
- **C5 AP 型号-场景映射表**：AP1360=户外周边/监控；AP1322=看台定向（<15m 结构）；AP1361D=看台猫道；AP1331/AP1351=媒体/大厅/礼堂；AP1311=办公室。 <<<PAGE 13>>>
- **C6 5 万座屋顶定向 AP 布点实例**：a study for the location of 260 AP1322s equipped with ANT-S-M4-60 and ANT-S-M4-30 external antennas... each AP1322 covers an average of up to 180 seats. <<<PAGE 16-17>>>
- **C7 卫星机柜配比**：One telecom satellite cabinet is required approximately every 3,200 seats, with each cabinet equipped with a 24-port switch in this example. <<<PAGE 17>>>
- **C8 双 6900 核心架构**：OmniAccess Stellar high-density WLAN is based here on a network core consisting of two redundant Omniswitch 6900s... Guaranteed 40Gbps traffic, with the ability to peak at 100Gbps. <<<PAGE 18-19>>>
- **C9 第三方 Captive Portal 容量底线**：the solution must be able to support at least 15,000 users immediately (for example, the UCOPIA Edge solution...). <<<PAGE 19>>>
- **C10 LAN 带宽估算实例**：1 * 260 * 60 * 2 = 31,200 Mbps. To account for wired bandwidth, a precautionary additional 50% is included... resulting in a total of 47 Gbps for the core LAN. <<<PAGE 21>>>
- **C11 OmniVista 2500 支撑规模**：supporting up to 4000 APs per appliance, along with compatibility for all AP models suitable for their deployment within a stadium. <<<PAGE 22>>>
- **C12 媒体包厢自定义仪表盘**：all these statistics can be grouped into a single dashboard ("Custom Dashboard" menu), entirely customized for the use of this area. <<<PAGE 23>>>
- **C13 SSID×同信道 AP 空口开销矩阵**：if one configures ten SSIDs on twelve Access Points operating on the same channel this will consume 50% of the available airtime. <<<PAGE 53>>>
- **C14 2.4GHz 开销更糟**：The analysis for the 2.4Ghz band shows worse results, there is over 50% overhead for just three SSIDs for eight APs on the same channel. <<<PAGE 53>>>
- **C15 Apple iOS 对 Band Steering 的黑名单行为**：Apple ios devices can have issues with the 'band steering' variable when enabled where it may blacklist the SSID for a few minutes. <<<PAGE 54>>>
- **C16 信号强度行业基准表**：-67 dBm = Minimum signal strength for applications that require time-sensitive communications (VoIP / VoWLAN, Video streaming); -70 dBm = Email, web; -80 dBm = 最低连接（不可靠）。 <<<PAGE 54>>>
- **C17 RSSI-dBm 换算**：we are using -96 dBm as the base noise floor less the RSSI threshold value of (29) it provides the value of -67 dBm. <<<PAGE 55>>>
- **C18 时敏场景漫游阈值加严案例**：at one of our customer deployments we configured roaming RSSI thresholds of 34 for 2.4G and 28 for 5G bands. <<<PAGE 55>>>
- **C19 AP1230 双 5G 信道细分配置**：select all 8 channels for the 5G Low... select 11 channels to have sufficient isolation... for the 5G High option, change the channel width from Auto to 20MHz. <<<PAGE 62>>>
- **C20 Cirrus 信道分布 widget 调优闭环**：all the clients are well distributed, utilizing 9.1% of each of the 5GHz channels except for channel 40 which is being utilized by more clients than the other channels. <<<PAGE 65>>>
- **C21 部署协助服务五天交付包**：This service is based on delivery over a five-day period... must be ordered using eBuy part number PS-PAER-5-NET.（前置：ACFE 认证+一次办公部署经验+HLD 已完成） <<<PAGE 75>>>

## counter-examples

- **X1 宽信道带来噪声与 CCI 惩罚**：that implementation introduces the Co-Channel Interference (CCI), plus the introduction of an extra 3dB of noise to the channel, doubling the noise... It equates to a lower SNR... which will in turn force a lower Modulation Coding Scheme (MCS) rate, shrinking the throughput. <<<PAGE 49>>>
- **X2 关闭背景扫描的代价**：When it's turned OFF, the foreign AP detection and rogue suppression will stop, and the RDA technology will drop its precision. <<<PAGE 49>>>
- **X3 手工定义信道值引发干扰**：When RDA is disabled there is more risk that the manually defined values will create channel interference for new applications or roaming clients. <<<PAGE 49>>>
- **X4 覆盖型设计的性能陷阱**：The APs operate at a higher transmit power and therefore cover larger areas.（反面：大功率大蜂窝导致低速率关联与更多干扰） <<<PAGE 51>>>
- **X5 同信道 AP 堆叠 SSID 的空口开销**：as one increases the number of SSIDs it contributes to the Wi-Fi network overhead based on the added beacons and probe response frames. <<<PAGE 53>>>
- **X6 过度微调反受其害**：be careful and do not go overboard in trying to fine-tune certain parameters. <<<PAGE 53>>>
- **X7 Apple 设备对 Band Steering 过敏**：Apple ios devices can have issues with the 'band steering' variable when enabled where it may blacklist the SSID for a few minutes. Caution when enabling for heavy Apple ios device deployments. <<<PAGE 54>>>
- **X8 混合客户端环境开 Force 5G 会拒联**：This functionality is recommended stay disabled for environments where the client population has a mixture of 2.4GHz and 5GHz clients. When enabled it will reject all association requests from 2.4Ghz clients. <<<PAGE 54>>>
- **X9 -80dBm 下发包不可靠**：-80 dBm — Minimum signal strength for device connectivity. Packet delivery is unreliable. <<<PAGE 54>>>
- **X10 粘滞客户端现象**：The sticky-client issue happens when Wi-Fi clients attempt to roam; those clients tend to hang on to the original access point they associated with, rather than moving to a nearby AP that has better signal strength. <<<PAGE 57>>>
- **X11 每次漫游都做完整 802.1X 重认证抵消移动性**：If re-authentication happened every time a client roamed it would defeat the purpose for device mobility. <<<PAGE 57>>>
- **X12 负载均衡解决不了粘滞客户端**：none of that functionality solves the problem of sticky clients or guarantees that the Wi-Fi network is providing optimal performance to all its connected clients. <<<PAGE 58>>>
- **X13 802.11k/v 依赖客户端支持**：keep in mind the lowest common denominator is that the client needs to support those standard amendments to force the roaming gracefully. <<<PAGE 58>>>
- **X14 AP 不代理免费 ARP**：The APs do not act as ARP proxy for gratuitous ARP packets. <<<PAGE 60>>>
- **X15 iPhone/Chromebook 与 DFS 动态信道不兼容**：These problems may cause iPhones and Chomebooks to have issues when roaming, sticky-client, and randomness poor performance. <<<PAGE 60>>>
- **X16 高密场馆禁用低性能 AP**：The use of low-performance Wi-Fi 6 APs is not recommended for stadiums with more than 5,000 seats. <<<PAGE 13>>>
- **X17 座椅下 AP 易遭人为破坏**：APs must be protected from intentional destruction when installed in this manner. <<<PAGE 16>>>
- **X18 手工功率超型号能力时设置失效**：If manually configured, and when the setting value exceeds the capability of the model, the AP will work with a maximum transmitting power rather than the setting value. <<<PAGE 67>>>
- **X19 关闭 High Efficiency 使 11ax 降级**：when disabled, HE 802.11ax capable APs will downgrade to VHT (Very High Throughput) mode. <<<PAGE 68>>>
- **X20 扫描间隔过长损 RDA 精度与 wIPS**：Keep in mind that an interval longer than 60 seconds loses RDA accuracy, and it affects the wIPS functionality, it recommended to keep it under 40 seconds. <<<PAGE 56>>>

## frameworks

## F1 高密 WLAN 设计五步法 <<<PAGE 6-7>>>
1. 需求分析（客户端类型/应用/并发与带宽容量计划/接入安全与 QoS 要求）
4. 验证（实时性能对比规划指标、真实用户调查）
5. 交付（BOM/AP 点位图/勘测报告/安装指南/配置指南/人员培训）
## F2 高密 RF 管理七要点 <<<PAGE 8-9>>>
1. 信道复用规则化降低 CCI/ACI
2. 强制 5GHz + AP 间负载均衡
3. 室内低发射功率（户外按需 10-15dBm）
4. 分区信道规划：看台用 DFS、室内用非 DFS
5. 20MHz 基准带宽
6. Airtime Fairness
7. 选用带专用全频扫描射频的 AP + 多 RF Profile 管理
## F3 容量 vs 覆盖两种设计范式 <<<PAGE 50-51>>>
- 覆盖型（竞争者主张）：AP 少、间距大、功率高、蜂窝大 → 连得上但性能差
- 容量型（ALE 主张）：AP 多、功率低、蜂窝小 → 高速率关联、更优性能；配合 ACS/APC/RDA 自动射频管理压制邻近干扰；新部署一律推荐容量型
## F4 Stellar 三级配置体系 <<<PAGE 27-38, 66-72>>>
1. RF Profile：频段/信道计划(DRM/Channel List)/信道宽度/收发功率范围/信标间隔/扫描——按区域差异化
2. AP Group：SSH/SNMP/IGMP Snooping/日志上送——按设备组统一
3. SSID：认证方式/最低速率/漫游(11r/k/v/OKC/FDB)/带宽合约/广播组播优化/QoS 映射——按业务差异化
（HD 指南附录给出访客与监控两套完整模板；微调简报附录给出默认值与推荐值对照表）

## glossary

- **HD / VHD（高密/极高密）**：High-density / Very-high density，体育场看台等为 VHD 典型场景 <<<PAGE 5, 6>>>
- **容量规划（Capacity planning）**：评估事件期间并发客户端数与并发带宽的负载测算 <<<PAGE 6>>>
- **预测勘测（Predictive survey）**：基于数字地图在部署前预测 AP 点位与覆盖的设计手段 <<<PAGE 7, 74>>>
- **CCI（同频干扰）**：Co-Channel Interference，同信道 AP 相互干扰 <<<PAGE 8>>>
- **ACI（邻频干扰）**：Adjacent-Channel Interference <<<PAGE 8>>>
- **DFS 信道**：与其他无线电业务共用的频率（如 UNII-2e 100-140），看台高密区优选，须守当地法规 <<<PAGE 8, 26>>>
- **信道复用计划（Channel reuse plan）**：5GHz 信道按规则图样复用以降干扰 <<<PAGE 8>>>
- **Airtime Fairness（空口时间公平）**：保证各客户端公平占用空口时间，默认关、高密必开 <<<PAGE 8, 56>>>
- **专用扫描射频**：Wi-Fi 6 AP 的独立全频扫描射频，工作信道不受扫描影响 <<<PAGE 9>>>
- **Band Steering（频段引导）**：引导双频客户端优先连 5GHz；Apple iOS 可能短暂拉黑 SSID <<<PAGE 54, 66>>>
- **Force 5GHz**：强制拒绝 2.4GHz 关联请求，仅双频客户端环境适用 <<<PAGE 54>>>
- **RSSI 阈值（关联/漫游）**：以 -96dBm 为底噪换算：关联阈值 22=-74dBm，漫游阈值 25=-71dBm <<<PAGE 55, 66>>>
- **最低客户端数据速率**：低于门限拒绝关联；微调推荐 2.4G=12Mbps、5G=24Mbps <<<PAGE 10, 55>>>
- **最低管理帧速率（Minimum MGMT Rate）**：管理帧传输速率下限，须≤关联数据速率 <<<PAGE 55, 71>>>
- **Sticky client（粘滞客户端）**：客户端抱住信号变差的原始 AP 不漫游的问题 <<<PAGE 57>>>
- **802.11k**：无线电资源测量修正案，邻居报告辅助漫游决策 <<<PAGE 57>>>
- **802.11v**：BSS Transition Management，AP 引导客户端漫游到指定/优选 AP <<<PAGE 58>>>
- **802.11r（Fast BSS Transition）**：BSS 间快速切换，降低漫游时延 <<<PAGE 58, 70>>>
- **OKC（机会性密钥缓存）**：漫游复用缓存 PMK 免完整 802.1X 重认证 <<<PAGE 57, 70>>>
- **PMK（成对主密钥）**：OKC 缓存复用的密钥实体 <<<PAGE 57>>>
- **FDB Update on Association**：客户端漫游后 AP 发 ARP 通知交换机刷新转发表 <<<PAGE 30, 57>>>
- **L2/L3 Roaming**：二层/三层漫游参数，均建议开启，L3 由有线侧重策略与 ACL <<<PAGE 57, 70>>>
- **Smart Load Balance（SLB，智能负载均衡）**：引导客户端去空闲信道/AP、拒弱信号关联的功能集 <<<PAGE 52>>>
- **Dynamic Load Balance**：相邻 AP 间按客户端数量负载分担 <<<PAGE 27, 66>>>
- **RDA / DRM（Radio Dynamic Adjustment / Dynamic Radio Management）**：自动信道+功率调整技术，含 ACS 与 APC <<<PAGE 48, 56>>>
- **ACS（自动信道选择）**：AP 自动择优信道算法 <<<PAGE 48>>>
- **APC（自动功率控制）**：AP 自动择优发射功率 <<<PAGE 48>>>
- **背景扫描（Background Scanning）**：wIDS/wIPS/RDA 的基础，默认开，间隔建议 <40s <<<PAGE 49, 56>>>
- **信道利用率（Channel Utilization）**：≥50% 即显著损害容量 <<<PAGE 52>>>
- **SSID 空口开销**：SSID 数×同信道 AP 数产生的 beacon/probe 开销占比 <<<PAGE 53>>>
- **OFDMA**：Wi-Fi 6 正交频分多址，上下行高效共享信道、降时延 <<<PAGE 12, 51>>>
- **MU-MIMO**：多用户多入多出，AP 同时服务更多并发客户端 <<<PAGE 12, 51>>>
- **1024-QAM**：同频谱编码更多数据提升吞吐 <<<PAGE 51>>>
- **TWT（Target Wake Time）**：目标唤醒时间，节电与调度 <<<PAGE 51>>>
- **BSS Coloring**：Wi-Fi 6 干扰着色机制，利于高密信道复用 <<<PAGE 12>>>
- **MCS（调制编码方案）**：MCS8=256QAM 3/4，速率越高对 SNR 要求越高 <<<PAGE 11, 49>>>
- **2x2:2 MIMO**：当前主流客户端天线配置 <<<PAGE 9>>>
- **AP 计数标准**：看台 120 终端/AP（150 座/AP）、其余区域 1 AP/100m² <<<PAGE 12>>>
- **30% 并发率**：高使用场景下连接人数占总观众比例的经验值 <<<PAGE 12>>>
- **NEMA 防护盒**：座椅下/猫道安装 AP 的防护外壳（IP3/IP4） <<<PAGE 13>>>
- **扇区天线（Sector antenna）**：ANT-S-M4-30/60 等定向天线，屋顶定向覆盖看台 <<<PAGE 17, 40>>>
- **OmniSwitch 6900**：双机冗余核心，40G 保底/100G 峰值、虚拟机箱、autofabric <<<PAGE 18-19>>>
- **卫星机柜（Telecom satellite cabinet）**：约每 3200 座一个、配 24 口交换机 <<<PAGE 17>>>
- **信道复用因子（Channel reuse factor）**：可用信道/已用信道之比，VHD 力争逼近 1，座椅部署最高 3 <<<PAGE 21>>>
- **LAN 带宽公式**：LAN BW = 复用因子 × AP 数 × 每 AP 客户端数 × 每客户端带宽；有线再加 50% 冗余 <<<PAGE 21>>>
- **OmniVista 2500 HA**：双数据库高可用 NMS，单机支持 4000 AP <<<PAGE 19, 22>>>
- **Captive Portal（强制门户）**：访客 Web 认证，OV2500 可托管或用 UCOPIA（≥15,000 用户） <<<PAGE 19>>>
- **QoE（体验质量）**：连接成功率、连接时长、漫游、容量可用性等综合评分 <<<PAGE 25, 64>>>
- **Custom Dashboard**：Cirrus 10 为特定区域（媒体包厢）聚合统计的自定义仪表盘 <<<PAGE 23>>>
- **客户端密度图（Client density map）**：Cirrus 10.4.1+ 的覆盖与使用密度可视化 <<<PAGE 24>>>
- **Multicast Optimization（组播优化）**：组播转单播发送，Number of Clients 默认 6 <<<PAGE 37, 59>>>
- **IGMP Snooping**：按组播成员端口定向转发，AP Group 级启用 <<<PAGE 38, 59>>>
- **Broadcast Key Rotation**：广播密钥按周期轮换（1-1440 分钟，默认 15） <<<PAGE 32, 59>>>
- **Broadcast Filter ARP**：AP 作 ARP 代理，只发不播，优化广播域 <<<PAGE 32, 60>>>
- **Broadcast Filter All**：丢弃除 DHCP/ARP 外的全部广播帧 <<<PAGE 32>>>
- **Bandwidth Contract**：SSID 级上/下行及突发带宽合约（0-2621440 Kbps） <<<PAGE 32, 72>>>
- **WMM 访问类别**：AC_BK/BE/VI/VO 四级无线多媒体类别 <<<PAGE 32, 63>>>
- **802.1p / DSCP 映射**：WMM 类别与有线 QoS 标记的转换；Trust Original DSCP 信任上行原值 <<<PAGE 32, 63>>>
- **Voice and Video Awareness**：语音/视频会话期间暂停背景扫描 <<<PAGE 61, 66>>>
- **Beacon Interval（信标间隔）**：默认 100ms，极高负载可增至 150ms <<<PAGE 29, 68>>>
- **DTIM Interval**：组播/广播传递指示，Apple 互通建议设 3 <<<PAGE 71>>>
- **Client Isolation（客户端隔离）**：SSID 内客户端互访隔离，附加安全层 <<<PAGE 70>>>
- **PMF（Protected Management Frame）**：受保护管理帧，WPA3/WPA2 企业级可选 <<<PAGE 70>>>
- **High Efficiency（HE）模式**：802.11ax 高效模式开关，关闭则降级 VHT <<<PAGE 68>>>
- **Enterprise / Express 模式**：Stellar AP 两种运营模式——OmniVista 集中管理（4000 AP/组）或集群自治（256 AP/集群） <<<PAGE 47>>>
- **Ekahau Pro**：业界预测勘测与干扰分析工具 <<<PAGE 49, 74>>>
- **部署协助服务（Deployment Assistance）**：ALE 专业服务包：预测勘测、现场勘测、辅导、培训与 ACSE 认证，5 天交付，PS-PAER-5-NET <<<PAGE 73-75>>>
- **ACFE / ACSE 认证**：项目前置的基础认证 / 完成后获得的技术支持准入认证 <<<PAGE 75>>>
- **HLD（High-Level Design）**：订购部署协助服务前必须完成的高层设计 <<<PAGE 75>>>

## principles

## 高密设计总纲
- **P1 需求分析是高密设计第一步**：A requirements analysis is the first and essential step in high-density Wi-Fi design, that is clearly identifying client types and the different applications used. <<<PAGE 6>>>
- **P2 容量规划先于部署**：a WLAN Network design project based on capacity planning is essential. This planning enables us to assess how the network will be used at high density. <<<PAGE 6>>>
- **P3 设计-部署-验证方法论闭环**：The Design, Deployment and Validation steps depicted in the figure above underline the importance of methodology in the implementation of high-density WLAN. <<<PAGE 7>>>
- **P4 项目交付物清单化**：BOM, AP layouts, Survey site reports, Installation guide, Configuration guide, Training of staff. <<<PAGE 7>>>
- **P5 高密选型专用自治网络架构**：It consistently calls for the implementation of a dedicated and autonomous network architecture provided by the ALE network solution managed in Enterprise mode. <<<PAGE 5>>>
- **P6 RF 管理是高密成败关键**：Success in deployment of a high-density Wi-Fi network in a stadium relies heavily on effective RF management. <<<PAGE 8>>>
## RF 原则
- **P7 信道复用规则化**：Channel reuse plan: channels available in the 5GHz band in an area are re-used in regular patterns, reducing then CCI and ACI interference in the area. <<<PAGE 8>>>
- **P8 强制 5GHz 并做 AP 间负载均衡**：Force the 5GHz band and balance the load between APs to avoid overloading certain APs. <<<PAGE 8>>>
- **P9 高密室内降发射功率**：for high-density indoor areas of stadium it's often advisable to set lower Tx transmission levels to reduce interference. <<<PAGE 8>>>
- **P10 分区信道规划（DFS 看台 / 非 DFS 室内）**：use DFS channels in stands for better use of 5GHz band, and non-DFS channels for better performance in indoor areas. <<<PAGE 8>>>
- **P11 20MHz 基准带宽**：20 MHz channel width greatly minimizes interference in outdoor areas, especially CCI (Co-Channel Interference). <<<PAGE 8>>>
- **P12 Airtime Fairness 必开**：Airtime fairness: essential in high-density environments, as it efficiently manages a number of clients with varying throughput requirements at a single access point. <<<PAGE 8>>>
- **P13 选型带专用扫描射频的 AP**：It is therefore recommended to select APs that support a dedicated full-band scanning radio. <<<PAGE 9>>>
- **P14 RF Profile 分区管理**：Defining multiple Stellar RF profiles make it easy to manage all the RF points... including a channel plan selection and Auto Channel Selection. <<<PAGE 8>>>
## 客户端与 SSID 原则
- **P15 按客户端画像定参数**：Around 90% of equipment/smartphones are dual-band compatible... The majority of Wi-Fi clients today operate in 2x2:2 MIMO mode. <<<PAGE 9>>>
- **P16 SSID 数量克制**：A stadium requires a variety of Wi-Fi services (up to 7 SSIDs maximum are possible for an average channel utilization in the 5 GHz band of around 12%). <<<PAGE 9>>>
- **P17 SSID 按角色差异化**：访客=开放+Captive Portal+限速；媒体 VIP=802.1X WPA2+高 QoS+不限速；售票=实时+QoS；监控=802.1X+流速率限制。 <<<PAGE 9-10>>>
- **P18 双频 SSID + RF 级 5GHz 引导**：Dual-band 2.4 GHz/5 GHz SSIDs with band forcing to 5 GHz at RF level. <<<PAGE 10>>>
- **P19 最低数据速率兜底**：Minimum data rates of 12 Mbps to take account of different client types. <<<PAGE 10>>>
- **P20 ARP 广播过滤保漫游**：The application of the ARP broadcast filter is recommended to avoid these problems during their roaming/association.（Apple/Chromebook） <<<PAGE 10>>>
- **P21 粘滞避免（Sticky avoidance）在 RF 层管理**：The "Sticky avoidance" must be managed at RF level for these high-density SSIDs. <<<PAGE 10>>>
## AP 计数与安装
- **P22 按区域类型的 AP 计数标准**：Tiered/seats: Up to 120 devices per AP/radio (up to 150 seats/AP)... Press/media/VIP, Halls, Surrounding, Service: 1 AP/100m². <<<PAGE 12>>>
- **P23 30% 并发率经验值**：a ratio of 30% of connected people to the total number of visitors is generally applied. <<<PAGE 12>>>
- **P24 Wi-Fi 6 特性面向高密**：OFDMA and BSS coloring... offer numerous advantages in high-density applications. <<<PAGE 12>>>
- **P25 低性能 AP 的使用禁区**：The use of low-performance Wi-Fi 6 APs is not recommended for stadiums with more than 5,000 seats. <<<PAGE 13>>>
- **P26 安装方式随场景**：座椅下/扶手安装贴近观众；墙体/结构安装补盲区；NEMA 防护盒（IP3/IP4）保护。 <<<PAGE 13>>>
- **P27 物理勘测决定最终点位**：The physical placement of each AP depends on the physical site survey, which guarantees the strongest signal coverage while minimizing channel interference. <<<PAGE 16>>>
- **P28 座椅下 AP 需防破坏**：APs must be protected from intentional destruction when installed in this manner. <<<PAGE 16>>>
## 架构与分析
- **P29 关键网络双核心全冗余、双站点**：The network core provides full redundancy for all appliances in the data center, with a physical location across two separate sites. <<<PAGE 19>>>
- **P30 NMS 高可用**：Omnivista 2500 NMS operates in high availability (HA) mode with a duplicated database. <<<PAGE 19>>>
- **P31 信道复用因子逼近 1**：it's essential to aim for a channel reuse factor as close to 1 as possible, especially within VHD areas. <<<PAGE 21>>>
- **P32 LAN 带宽估算公式**：LAN BW = channel reuse factor * number of APs * number of clients per AP * VHD bandwidth per client. <<<PAGE 21>>>
- **P33 管理面与云分析互补**：The combination with an Omnivista Cirrus 10 Cloud instance for statistical and analytical tasks... complements with interest Omnivista 2500 NMS management of the site. <<<PAGE 22>>>
- **P34 QoE 评分驱动运维**：Achieving a QoE score and maintaining control over the density of certain Wi-Fi coverage areas is essential for the maintenance of a high-density WLAN. <<<PAGE 25>>>
## 微调最佳实践（DOC 2）
- **P35 RF 管理自动化优先、默认开启勿关**：these settings are enabled by default and should remain enabled with minor adjustments based on the quality of connectivity user experience (QoE) scores. <<<PAGE 48>>>
- **P36 容量设计优于覆盖设计**：ALE recommends the capacity designs for a higher density of APs to provide the optimal performance. <<<PAGE 50>>>
- **P37 小蜂窝低功率**：in a balanced AP design... more APs are deployed operating at a lower transmit power to keep the cell size smaller. <<<PAGE 51>>>
- **P38 RDA 保持开启避免手工信道冲突**：To avoid any of these possible 'pitfalls' keep the RDA enabled for Stellar APs and let it's algorithm determine the best channels and transmitting power. <<<PAGE 49>>>
- **P39 不要过度手工微调**：be careful and do not go overboard in trying to fine-tune certain parameters, the Wi-Fi environment will be better served when enabling most of its auto functionality. <<<PAGE 53>>>
- **P40 信道利用率 50% 红线**：If the channel utilization reaches 50% or greater before deployment the WLAN capacity will be significantly impacted. <<<PAGE 52>>>
- **P41 关联 RSSI 阈值 22（-74dBm）**：The recommended minimum "Association RSSI Threshold" setting is (22) for both 2.4G and 5G bands. <<<PAGE 55>>>
- **P42 漫游 RSSI 阈值 25（-71dBm）**：the Roaming RSSI threshold is recommended to be (25) for both 2.4G and 5G bands to trigger roaming at -71 dBm. <<<PAGE 55>>>
- **P43 最低客户端速率须≥最低管理速率**：The association Minimum Client Data Rate setting needs to be equal or higher than the Minimum MGMT Rate. <<<PAGE 55>>>
- **P44 802.11k/v 是解粘滞客户端的正解**：the enabling of the 802.11k / 802.11v supplemental standards to force roaming when connection speeds reach low rates is a requirement to avoid the 'sticky-client' issues. <<<PAGE 58>>>
- **P45 语音用专用 5GHz SSID 且关 Band Steering**：for Time Sensitive applications, (like Voice over WLAN) we should dedicate a SSID with only the 5 GHz enabled and no Band Steering. <<<PAGE 61>>>
- **P46 AP 作 ARP 代理减少广播**：The Broadcast Filter ARP attribute is recommended to be enabled so the AP can act as an "ARP Proxy". <<<PAGE 60>>>
