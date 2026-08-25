# principles — sol-wlan-design

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
