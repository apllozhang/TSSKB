# DIGEST — Stellar 高密设计指南 + 微调最佳实践 + 部署协助服务 精华

本书册由三份文档构成（页码连续）：DOC1 高密设计指南（p1-44，体育场 VHD 端到端设计）；DOC2 无线微调最佳实践（p45-72，Enterprise 模式参数级微调）；DOC3 部署协助服务数据表（p73-75，ALE 专业服务定义）。

## 一、知识地图（三技能单元）

1. **高密设计**（sol-wlan-high-density）：五步法、容量 vs 覆盖、VHD 吞吐基线、AP 计数与布点、双 6900 架构、LAN 带宽公式（p5-25）。
2. **RF 微调**（sol-wlan-fine-tuning）：RDA 自动化、七要点、RSSI/速率阈值、Band Steering 陷阱、粘滞客户端与 802.11k/v/r、组播广播优化、语音专门化（p8-10、48-68）。
3. **三级配置与部署服务**（sol-wlan-profile-hierarchy）：RF Profile/AP Group/SSID 三级体系、Enterprise vs Express、模板与参数对照表、部署协助服务包（p27-44、66-75）。

## 二、三单元要点串讲

### 1. 高密：容量规划先行
需求分析是第一步（<<<PAGE 6>>>）：5 万座体育场 = 数万并发设备、AP 多于 5GHz 信道数。容量型优于覆盖型（<<<PAGE 50-51>>>）：更多 AP、更低功率、小蜂窝。VHD 吞吐基线：Wi-Fi 6 HE20 单用户 80Mbps → 60 并发衰减至 40Mbps → 再乘 25% 折减（<<<PAGE 11>>>）。计数标准：看台 120 终端/AP（150 座/AP）、其余 1 AP/100m²、30% 并发率（<<<PAGE 12>>>）。布点：屋顶 AP1322+扇区天线 1 AP/180 座、座椅下 NEMA 盒、卫星机柜 1/3200 座（<<<PAGE 16-17>>>）。架构：双 6900（40G/100G）+ OV2500 HA（4000 AP）+ Cirrus 云分析；LAN BW = 复用因子×AP 数×客户端×带宽再 +50%（<<<PAGE 18-21>>>）。

### 2. 微调：自动化优先
RDA（ACS+APC）默认开启勿关、勿过度手工微调（<<<PAGE 48-53>>>）。七要点：信道复用、强制 5GHz、低功率、DFS 分区、20MHz、Airtime Fairness、专用扫描射频（<<<PAGE 8-9>>>）。阈值：关联 RSSI 22（-74dBm）、漫游 25（-71dBm）、最低速率 2.4G 12M/5G 24M（<<<PAGE 55>>>）。粘滞客户端正解 = 802.11k/v（负载均衡解决不了）；Apple 对 Band Steering 过敏、Force 5G 拒 2.4G 关联、iPhone/Chromebook 与 DFS 不合（<<<PAGE 53-60>>>）。语音：专用 5GHz SSID+关 Band Steering+信道细分（5G Low 8/High 11）（<<<PAGE 61-62>>>）。

### 3. 配置与服务：三级体系落地
RF Profile（区域）/AP Group（设备组）/SSID（业务）三级各管一维，附录给访客与监控两套模板及默认/推荐值对照（<<<PAGE 27-44、66-72>>>）。模式：Enterprise（OV 集中 4000 AP/组）vs Express（256 AP/集群），高密用 Enterprise。服务：部署协助 5 天交付包（Ekahau 预测勘测+现场勘测+辅导+ACSE 认证），前置 ACFE+办公部署经验+HLD，eBuy PS-PAER-5-NET（<<<PAGE 73-75>>>）。

## 三、本书在知识库中的位置
与 stellar-wlan-enterprise-basic（基础配置）、stellar-wlan-adv-deploy（高级部署）、acfe-wlan（培训体系）和 stellar-wlan-adv-trouble（排障）互补——本书定位"设计方法论 + 参数微调依据"。跨书易混点：Airtime Fairness 默认关、高密必开；背景扫描间隔 >60s 损 RDA 与 wIPS；SSID 数量与同信道 AP 数的乘积效应是空口开销主因。

## 来源
DOC1 ale-omniaccess-stellar-high-density-design-guidelines-en.pdf（p1-44）；DOC2 omniaccess-stellar-wireless-fine-tuning-best-practices-techbrief-en.pdf（p45-72）；DOC3 omniaccess-stellar-wlan-specific-deployment-assistance-datasheet-en.pdf（p73-75）。verified.md：cases C1-C21；principles P1-P46；counter-examples X1-X20；frameworks F1-F4；glossary 63 条。
